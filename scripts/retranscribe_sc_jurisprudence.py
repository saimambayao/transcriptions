#!/usr/bin/env python3
"""
Retranscribe SC-scraped jurisprudence files (2021-2026) with paragraph-aware extraction.

Re-extracts body text from source PDFs using pdfplumber word-level extraction with
vertical gap analysis to detect paragraph breaks. Preserves originals in _raw/ folders.
Also applies metadata fixes (Case Number, ponente, field order, opinion type).

Usage:
  python3 scripts/retranscribe_sc_jurisprudence.py --year 2026
  python3 scripts/retranscribe_sc_jurisprudence.py --file jurisprudence/2025/GR-267675-JAVIER.md
  python3 scripts/retranscribe_sc_jurisprudence.py --dry-run --year 2026
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
from statistics import median

# Import metadata fix functions from reformat script
sys.path.insert(0, str(Path(__file__).resolve().parent))
from reformat_sc_jurisprudence import (
    FIELD_ORDER, derive_case_number, parse_file, extract_ponente_from_body,
    format_ponente, detect_opinion_type, JUSTICES_2021_2026, OPINION_TYPES,
    strip_justice_suffix,
)

try:
    import pdfplumber
except ImportError:
    print("ERROR: pdfplumber not installed. Run: pip3 install pdfplumber")
    sys.exit(1)

JURISPRUDENCE_DIR = Path(__file__).resolve().parent.parent / 'jurisprudence'
TRANSCRIBER_SCRIPTS = Path.home() / '.claude/skills/transcriber/scripts'

# Page header patterns to strip
PAGE_HEADER_RE = re.compile(
    r'^(?:DECISION|RESOLUTION|DISSENT|CONCURRING OPINION|DISSENTING OPINION|'
    r'SEPARATE OPINION|SEPARATE CONCURRING)\s+\d+\s+(?:G\.R\.|A\.C\.|A\.M\.|B\.M\.)',
    re.IGNORECASE
)


# ── PDF Location ──────────────────────────────────────────────────────────────

def find_pdf_for_md(md_path, content):
    """Find the source PDF for an SC-scraped .md file."""
    # Extract PDF filename from Source URL
    m = re.search(r'sc\.judiciary\.gov\.ph/wp-content/uploads/\d{4}/\d{2}/(.+?\.pdf)', content)
    if not m:
        return None

    pdf_filename = m.group(1)
    # URL-decode common patterns
    pdf_filename = pdf_filename.replace('%20', ' ')

    pdf_dir = md_path.parent / 'pdf'
    pdf_path = pdf_dir / pdf_filename
    if pdf_path.exists():
        return pdf_path

    # Try URL-decoded version
    from urllib.parse import unquote
    decoded = unquote(pdf_filename)
    pdf_path2 = pdf_dir / decoded
    if pdf_path2.exists():
        return pdf_path2

    return None


# ── PDF Assessment ────────────────────────────────────────────────────────────

def assess_pdf_type(pdf_path):
    """Determine if PDF has embedded text (pdfplumber) or needs OCR."""
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(str(pdf_path))
        total_chars = 0
        pages_checked = min(3, len(doc))
        for i in range(pages_checked):
            text = doc[i].get_text()
            total_chars += len(text)
        doc.close()
        avg_chars = total_chars / pages_checked if pages_checked > 0 else 0
        return 'pdfplumber' if avg_chars > 500 else 'ocr'
    except Exception:
        return 'ocr'


# ── Paragraph-Aware Extraction (pdfplumber) ───────────────────────────────────

def extract_with_paragraphs(pdf_path):
    """Extract text from PDF with paragraph detection using vertical spacing."""
    pdf = pdfplumber.open(str(pdf_path))
    all_paragraphs = []
    current_paragraph = []

    for page_num, page in enumerate(pdf.pages):
        words = page.extract_words(keep_blank_chars=True, y_tolerance=3)
        if len(words) < 5:
            # Try fallback: basic text extraction
            text = page.extract_text()
            if text and len(text.strip()) > 50:
                # Can't do paragraph detection, just use as-is
                for line in text.split('\n'):
                    line = line.strip()
                    if line:
                        current_paragraph.append(line)
                    elif current_paragraph:
                        all_paragraphs.append(' '.join(current_paragraph))
                        current_paragraph = []
            continue

        # Group words by y-position into lines
        lines = defaultdict(list)
        for w in words:
            lines[round(w['top'], 1)].append(w)

        sorted_ys = sorted(lines.keys())
        if not sorted_ys:
            continue

        # Calculate median line gap for this page
        gaps = [sorted_ys[i+1] - sorted_ys[i] for i in range(len(sorted_ys)-1)]
        if gaps:
            med_gap = median(gaps)
            para_threshold = med_gap * 2.0
        else:
            para_threshold = 30

        for i, y in enumerate(sorted_ys):
            line_words = sorted(lines[y], key=lambda w: w['x0'])
            line_text = ' '.join(w['text'] for w in line_words)

            # Detect paragraph break
            is_para_break = False
            if i > 0:
                gap = y - sorted_ys[i-1]
                if gap > para_threshold:
                    is_para_break = True

            if is_para_break and current_paragraph:
                all_paragraphs.append(' '.join(current_paragraph))
                current_paragraph = []

            current_paragraph.append(line_text)

        # Page break = paragraph break
        if current_paragraph:
            all_paragraphs.append(' '.join(current_paragraph))
            current_paragraph = []

    # Flush remaining
    if current_paragraph:
        all_paragraphs.append(' '.join(current_paragraph))

    pdf.close()
    return all_paragraphs


# ── OCR Extraction + Line Joining ─────────────────────────────────────────────

def extract_with_ocr(pdf_path):
    """Extract text using OCR (tesseract) then join broken lines."""
    extract_script = TRANSCRIBER_SCRIPTS / 'extract_chapter.py'
    if not extract_script.exists():
        return None

    # Get page count
    try:
        import fitz
        doc = fitz.open(str(pdf_path))
        num_pages = len(doc)
        doc.close()
    except Exception:
        num_pages = 50  # guess

    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as tmp:
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            ['python3', str(extract_script), str(pdf_path), '1', str(num_pages), tmp_path],
            capture_output=True, text=True, timeout=300
        )
        if not os.path.exists(tmp_path):
            return None

        raw_text = Path(tmp_path).read_text(encoding='utf-8', errors='replace')
    except Exception:
        return None
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

    return join_ocr_lines(raw_text)


def join_ocr_lines(raw_text):
    """Join broken OCR lines into paragraphs."""
    # Remove page markers
    lines = []
    for line in raw_text.split('\n'):
        if re.match(r'^=+\s*PAGE\s+\d+\s*=+$', line):
            continue
        if re.match(r'^PAGE\s+\d+$', line.strip()):
            continue
        lines.append(line)

    paragraphs = []
    current = []

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Blank line = paragraph break
        if not stripped:
            if current:
                paragraphs.append(' '.join(current))
                current = []
            continue

        # Page header pattern — skip
        if PAGE_HEADER_RE.match(stripped):
            continue

        # Join with previous line if:
        # - previous line doesn't end with sentence-terminal punctuation
        # - this line starts with lowercase
        if current:
            prev = current[-1]
            if (not prev.rstrip().endswith(('.', '!', '?', ':', ';', '"'))
                    and stripped[0].islower()):
                # Join: continuation of same sentence
                # Handle hyphenation
                if prev.endswith('-'):
                    current[-1] = prev[:-1]
                current.append(stripped)
                continue

        current.append(stripped)

    if current:
        paragraphs.append(' '.join(current))

    return paragraphs


# ── Post-Processing ───────────────────────────────────────────────────────────

def postprocess_paragraphs(paragraphs):
    """Clean up extracted paragraphs."""
    cleaned = []
    for para in paragraphs:
        # Strip page headers that ended up inside paragraphs
        if PAGE_HEADER_RE.match(para.strip()):
            continue
        # Skip very short noise paragraphs (1-3 chars, non-word)
        stripped = para.strip()
        if len(stripped) <= 3 and not stripped.isalpha():
            continue
        # Collapse multiple spaces
        para = re.sub(r'  +', ' ', para)
        cleaned.append(para.strip())
    return cleaned


def format_as_blockquote(paragraphs):
    """Format paragraphs as markdown blockquote lines."""
    lines = []
    for i, para in enumerate(paragraphs):
        if i > 0:
            lines.append('>')  # blank blockquote line between paragraphs
        lines.append(f'> {para}')
    lines.append('')  # trailing newline
    return lines


# ── Quality Check ─────────────────────────────────────────────────────────────

def quality_check(old_body_lines, new_body_lines):
    """Compare old vs new body text quality."""
    def avg_line_len(lines):
        content_lines = [l.lstrip('> ').rstrip() for l in lines
                        if l.strip() and l.strip() != '>']
        if not content_lines:
            return 0
        return sum(len(l) for l in content_lines) / len(content_lines)

    def total_chars(lines):
        return sum(len(l.lstrip('> ').rstrip()) for l in lines
                  if l.strip() and l.strip() != '>')

    old_avg = avg_line_len(old_body_lines)
    new_avg = avg_line_len(new_body_lines)
    old_chars = total_chars(old_body_lines)
    new_chars = total_chars(new_body_lines)

    char_diff = ((new_chars - old_chars) / old_chars * 100) if old_chars > 0 else 0

    return {
        'old_avg': old_avg,
        'new_avg': new_avg,
        'old_chars': old_chars,
        'new_chars': new_chars,
        'char_diff_pct': char_diff,
        'ok': abs(char_diff) < 15 and new_avg > old_avg * 1.2,
    }


# ── Main Processing ───────────────────────────────────────────────────────────

def process_file(filepath, dry_run=False):
    """Retranscribe a single SC-scraped file."""
    filepath = Path(filepath)
    content = filepath.read_text(encoding='utf-8')

    # Only process SC-scraped files (check metadata Source line, not body)
    source_match = re.search(r'^\- \*\*Source\*\*:.*sc\.judiciary\.gov\.ph', content, re.MULTILINE)
    if not source_match:
        return None  # lawphil file

    # Parse existing file
    parsed = parse_file(content)
    if parsed is None:
        return {'status': 'PARSE_ERROR'}

    h1_line, subtitle, metadata, body_lines = parsed

    # Skip if already retranscribed (avg line length >120)
    content_lines = [l.lstrip('> ').rstrip() for l in body_lines
                    if l.strip() and l.strip() != '>']
    if content_lines:
        avg_len = sum(len(l) for l in content_lines) / len(content_lines)
        if avg_len > 120:
            return {'status': 'SKIP_ALREADY_CLEAN', 'avg_len': avg_len}

    # Find source PDF
    pdf_path = find_pdf_for_md(filepath, content)
    if pdf_path is None:
        return {'status': 'NO_PDF'}

    # Assess PDF type
    pdf_type = assess_pdf_type(pdf_path)

    if dry_run:
        return {
            'status': 'WOULD_RETRANSCRIBE',
            'pdf_type': pdf_type,
            'pdf': pdf_path.name,
        }

    # Preserve original in _raw/
    raw_dir = filepath.parent / '_raw'
    raw_path = raw_dir / filepath.name
    if not raw_path.exists():
        raw_dir.mkdir(exist_ok=True)
        shutil.copy2(filepath, raw_path)

    # Extract text
    if pdf_type == 'pdfplumber':
        paragraphs = extract_with_paragraphs(pdf_path)
    else:
        paragraphs = extract_with_ocr(pdf_path)

    if not paragraphs:
        return {'status': 'EXTRACTION_FAILED', 'pdf_type': pdf_type}

    # Post-process
    paragraphs = postprocess_paragraphs(paragraphs)
    if not paragraphs:
        return {'status': 'EMPTY_AFTER_CLEANUP', 'pdf_type': pdf_type}

    # Format as blockquote
    new_body_lines = format_as_blockquote(paragraphs)

    # Quality check
    qc = quality_check(body_lines, new_body_lines)

    # ── Apply metadata fixes ──────────────────────────────────────────────
    filename = filepath.name
    formal_cn = derive_case_number(filename)

    if 'Case Number' not in metadata:
        metadata['Case Number'] = formal_cn

    if not h1_line.startswith('G.R. No.') and not h1_line.startswith('A.'):
        h1_line = formal_cn

    if metadata.get('Ponente', '') == '[UNKNOWN]':
        body_text_for_ponente = '\n'.join(new_body_lines)
        ponente = extract_ponente_from_body(new_body_lines)
        if ponente:
            metadata['Ponente'] = ponente

    detected_type = detect_opinion_type(new_body_lines, filename)
    if detected_type != 'Decision' and metadata.get('Type', 'Decision') == 'Decision':
        metadata['Type'] = detected_type

    # ── Reconstruct file ──────────────────────────────────────────────────
    out_lines = []
    out_lines.append(f'# {h1_line}')
    out_lines.append('')
    if subtitle:
        out_lines.append(f'**{subtitle}**')
        out_lines.append('')
    out_lines.append('## Metadata')
    out_lines.append('')
    for key in FIELD_ORDER:
        if key in metadata:
            out_lines.append(f'- **{key}**: {metadata[key]}')
    for key in metadata:
        if key not in FIELD_ORDER:
            out_lines.append(f'- **{key}**: {metadata[key]}')
    out_lines.append('')
    out_lines.append('---')
    out_lines.append('')
    out_lines.extend(new_body_lines)

    output = '\n'.join(out_lines)
    if not output.endswith('\n'):
        output += '\n'

    filepath.write_text(output, encoding='utf-8')

    return {
        'status': 'OK' if qc['ok'] else 'QUALITY_WARNING',
        'pdf_type': pdf_type,
        'old_avg': qc['old_avg'],
        'new_avg': qc['new_avg'],
        'char_diff': qc['char_diff_pct'],
    }


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Retranscribe SC jurisprudence with paragraph-aware extraction')
    parser.add_argument('--year', type=int, help='Process only this year (2021-2026)')
    parser.add_argument('--dry-run', action='store_true', help='Report what would be done')
    parser.add_argument('--file', type=str, help='Process a single file')
    args = parser.parse_args()

    if args.file:
        filepath = Path(args.file)
        if not filepath.exists():
            print(f'File not found: {filepath}')
            sys.exit(1)
        result = process_file(filepath, dry_run=args.dry_run)
        if result is None:
            print(f'{filepath.name}: SKIP (not SC-scraped)')
        else:
            print(f'{filepath.name}: {result}')
        return

    years = [args.year] if args.year else list(range(2021, 2027))
    stats = {'ok': 0, 'warn': 0, 'skip': 0, 'fail': 0, 'lawphil': 0}

    for year in years:
        year_dir = JURISPRUDENCE_DIR / str(year)
        if not year_dir.exists():
            continue

        md_files = sorted(f for f in year_dir.glob('*.md') if f.name != 'INDEX.md')
        print(f'\n=== {year} ({len(md_files)} files) ===')

        for i, filepath in enumerate(md_files):
            result = process_file(filepath, dry_run=args.dry_run)

            if result is None:
                stats['lawphil'] += 1
                continue

            status = result.get('status', '')

            if status in ('SKIP_ALREADY_CLEAN',):
                stats['skip'] += 1
                continue

            if status == 'NO_PDF':
                stats['fail'] += 1
                print(f'  [{i+1}/{len(md_files)}] {filepath.name}: NO PDF FOUND')
                continue

            if status in ('PARSE_ERROR', 'EXTRACTION_FAILED', 'EMPTY_AFTER_CLEANUP'):
                stats['fail'] += 1
                print(f'  [{i+1}/{len(md_files)}] {filepath.name}: {status}')
                continue

            if status == 'WOULD_RETRANSCRIBE':
                stats['ok'] += 1
                print(f'  [{i+1}/{len(md_files)}] {filepath.name}: WOULD — {result["pdf_type"]}, pdf={result["pdf"]}')
                continue

            if status == 'OK':
                stats['ok'] += 1
                print(f'  [{i+1}/{len(md_files)}] {filepath.name}: {result["pdf_type"]}, '
                      f'avg: {result["old_avg"]:.0f}→{result["new_avg"]:.0f}, '
                      f'chars: {result["char_diff"]:+.1f}%')
            elif status == 'QUALITY_WARNING':
                stats['warn'] += 1
                print(f'  [{i+1}/{len(md_files)}] {filepath.name}: ⚠ {result["pdf_type"]}, '
                      f'avg: {result["old_avg"]:.0f}→{result["new_avg"]:.0f}, '
                      f'chars: {result["char_diff"]:+.1f}%')

    print(f'\n=== Summary ===')
    print(f'Retranscribed: {stats["ok"]}')
    print(f'Quality warnings: {stats["warn"]}')
    print(f'Skipped (lawphil): {stats["lawphil"]}')
    print(f'Skipped (already clean): {stats["skip"]}')
    print(f'Failed: {stats["fail"]}')


if __name__ == '__main__':
    main()
