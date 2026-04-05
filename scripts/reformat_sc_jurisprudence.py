#!/usr/bin/env python3
"""
Reformat SC-scraped jurisprudence files (2021-2026) to match lawphil format.

Fixes:
  P1+P2: Add Case Number field + fix H1 to formal case number
  P3:    Reorder metadata fields to lawphil standard
  P4:    Fix [UNKNOWN] ponente by extracting from body text
  P5:    Strip OCR noise from start of body text
  P6:    Detect opinion type from body text/filename

Usage:
  python3 scripts/reformat_sc_jurisprudence.py                   # all years
  python3 scripts/reformat_sc_jurisprudence.py --year 2025        # single year
  python3 scripts/reformat_sc_jurisprudence.py --dry-run          # report only
  python3 scripts/reformat_sc_jurisprudence.py --file path/to.md  # single file
"""

import argparse
import os
import re
import sys
from pathlib import Path

# ── Constants ─────────────────────────────────────────────────────────────────

FIELD_ORDER = ['Case Number', 'Case Title', 'Date', 'Ponente', 'Division', 'Type', 'Source']

JUSTICES_2021_2026 = [
    'GESMUNDO', 'LEONEN', 'CAGUIOA', 'HERNANDO', 'LAZARO-JAVIER',
    'INTING', 'ZALAMEDA', 'GAERLAN', 'ROSARIO', 'LOPEZ',
    'DIMAAMPAO', 'MARQUEZ', 'KHO', 'SINGH', 'VILLANUEVA',
    'JAVIER',  # sometimes without LAZARO- prefix
]

# Justice surnames that appear as filename suffixes
JUSTICE_SUFFIXES = set(JUSTICES_2021_2026 + [
    'PERALTA', 'PERLAS-BERNABE', 'REYES', 'JARDELEZA', 'TIJAM',
    'BERSAMIN', 'DEL-CASTILLO', 'CARPIO', 'LEONARDO-DE-CASTRO',
    'CARANDANG', 'DELOS-SANTOS', 'BALTAZAR-PADILLA',
])

# Opinion type keywords (ordered longest-first for greedy match)
OPINION_TYPES = [
    ('CONCURRING AND DISSENTING OPINION', 'Concurring and Dissenting Opinion'),
    ('SEPARATE CONCURRING OPINION', 'Separate Concurring Opinion'),
    ('SEPARATE CONCURRING', 'Separate Concurring Opinion'),
    ('CONCURRING OPINION', 'Concurring Opinion'),
    ('DISSENTING OPINION', 'Dissenting Opinion'),
    ('SEPARATE OPINION', 'Separate Opinion'),
]

JURISPRUDENCE_DIR = Path(__file__).resolve().parent.parent / 'jurisprudence'


# ── Case Number Derivation ────────────────────────────────────────────────────

def strip_justice_suffix(basename):
    """Strip known justice surname suffix from filename base.
    e.g. 'GR-274778-LEONEN' → 'GR-274778', suffix='LEONEN'
    """
    parts = basename.split('-')
    # Check if last part (or last few parts) is a justice name
    for i in range(len(parts) - 1, 0, -1):
        candidate = '-'.join(parts[i:]).upper()
        if candidate in JUSTICE_SUFFIXES:
            return '-'.join(parts[:i]), candidate
        # Also check single last part
        if parts[i].upper() in JUSTICE_SUFFIXES:
            return '-'.join(parts[:i]), parts[i].upper()
    # Check for opinion-type suffixes embedded in filename
    upper = basename.upper()
    for label in ['CON-OP', 'CONCURRING', 'DISSENTING', 'SEPARATE']:
        idx = upper.find(label)
        if idx > 0:
            # strip from the label onwards, plus any preceding dash
            prefix = basename[:idx].rstrip('-')
            return prefix, basename[idx:]
    return basename, None


def derive_case_number(filename):
    """Derive formal case number from filename.
    GR-270257 → G.R. No. 270257
    AC-10731 → A.C. No. 10731
    AC-NO-13986 → A.C. No. 13986
    AM-P-24-192 → A.M. No. P-24-192
    BM-426 → B.M. No. 426
    """
    base = Path(filename).stem  # remove .md
    base_original = base.upper()
    base_stripped, _suffix = strip_justice_suffix(base)

    b = base_stripped.upper()

    # AC-NO-{digits} pattern
    m = re.match(r'^AC-NO-(.+)$', b)
    if m:
        return f'A.C. No. {m.group(1)}'

    # AC-{rest}
    m = re.match(r'^AC-(.+)$', b)
    if m:
        return f'A.C. No. {m.group(1)}'

    # AM-{rest} (complex identifiers like P-24-192, 25-11-28-SC, MTJ-17-1894)
    m = re.match(r'^AM-(.+)$', b)
    if m:
        return f'A.M. No. {m.group(1)}'

    # BM-{rest}
    m = re.match(r'^BM-(.+)$', b)
    if m:
        return f'B.M. No. {m.group(1)}'

    # OCA-IPI-{rest}
    m = re.match(r'^OCA-IPI-(.+)$', b)
    if m:
        return f'OCA IPI No. {m.group(1)}'

    # UDK-{rest}
    m = re.match(r'^UDK-(.+)$', b)
    if m:
        return f'UDK-{m.group(1)}'

    # GR- prefix: handle pathological filenames and special cases
    m = re.match(r'^GR-(.+)$', b)
    if m:
        rest = m.group(1)

        # RTJ/MTJ/SDC cases misclassified as GR (actually A.M.)
        am_prefixes = ('RTJ-', 'MTJ-', 'SDC-', 'P-', 'CA-')
        for pfx in am_prefixes:
            if rest.startswith(pfx):
                return f'A.M. No. {rest}'

        # Pathological: SECOND-DIVISION-G.R.NO_.260640DECISION
        # Extract the embedded case number (5+ digit sequence)
        embedded = re.search(r'(\d{5,})', rest)
        if embedded and ('DIVISION' in rest or 'BANC' in rest or 'NO_' in rest):
            return f'G.R. No. {embedded.group(1)}'

        # Pathological: Separate-Concurring-Opinion-Associate-Justice-Singh-236548
        # or Concurring-Opinion-Associate-Justice-Benjamin-S.-Caguioa-264071
        # Search the ORIGINAL filename (before suffix stripping) for case number
        if 'OPINION' in rest or 'JUSTICE' in rest or 'OPINION' in base_original or 'JUSTICE' in base_original:
            # Search original for 5+ digit number
            all_nums = re.findall(r'\d{5,}', base_original)
            if all_nums:
                return f'G.R. No. {all_nums[0]}'

        return f'G.R. No. {rest}'

    # Fallback: return as-is with dots
    return base_stripped


# ── File Parsing ──────────────────────────────────────────────────────────────

def parse_file(content):
    """Parse a jurisprudence .md file into sections.
    Returns: (h1_line, subtitle, metadata_dict, body_lines, raw_metadata_start, raw_metadata_end)
    """
    lines = content.split('\n')

    h1_line = ''
    subtitle = ''
    metadata = {}
    body_lines = []
    meta_start = -1
    meta_end = -1

    # Find H1
    h1_idx = -1
    for i, line in enumerate(lines):
        if line.startswith('# ') and not line.startswith('## '):
            h1_line = line[2:].strip()
            h1_idx = i
            break

    if h1_idx < 0:
        return None  # can't parse

    # Find subtitle (bold line after H1)
    for i in range(h1_idx + 1, min(h1_idx + 5, len(lines))):
        if lines[i].startswith('**') and lines[i].endswith('**'):
            subtitle = lines[i][2:-2]
            break

    # Find ## Metadata
    for i, line in enumerate(lines):
        if line.strip() == '## Metadata':
            meta_start = i
            break

    if meta_start < 0:
        return None  # no metadata section

    # Parse metadata lines until ---
    for i in range(meta_start + 1, len(lines)):
        line = lines[i].strip()
        if line == '---':
            meta_end = i
            break
        m = re.match(r'^- \*\*(.+?)\*\*:\s*(.*)$', line)
        if m:
            metadata[m.group(1)] = m.group(2).strip()

    if meta_end < 0:
        return None  # no separator found

    # Body is everything after ---
    body_lines = lines[meta_end + 1:]
    # Strip leading blank lines from body
    while body_lines and body_lines[0].strip() == '':
        body_lines.pop(0)

    return h1_line, subtitle, metadata, body_lines


# ── P4: Ponente Extraction ────────────────────────────────────────────────────

def extract_ponente_from_body(body_lines):
    """Try to extract ponente from body text using 4-strategy cascade."""
    body_text = '\n'.join(body_lines)

    # Strategy 1: Regex after DECISION/RESOLUTION
    # Look for pattern: DECISION/RESOLUTION followed by NAME, J.:
    patterns = [
        # Standard: JUSTICE_NAME, J.:
        r'(?:D\s*E\s*C\s*I\s*S\s*I\s*O\s*N|DECISION|RESOLUTION)\s*(?:\n[>\s]*)*'
        r'(?:\**)?\s*([A-Z][A-Z\.\-\s,]+?)\s*,\s*'
        r'(?:S\.?\s*A\.?\s*J|C\.?\s*J|J)\s*[./~:]*\s*[:;]?',
        # With bold markers
        r'(?:D\s*E\s*C\s*I\s*S\s*I\s*O\s*N|DECISION|RESOLUTION)\s*(?:\n[>\s]*)*'
        r'\*+\s*([A-Z][A-Z\.\-\s,]+?)\s*,?\s*'
        r'(?:\*?\s*J\s*[./~:]*|S\.?\s*A\.?\s*J[./~:]*)',
    ]

    for pat in patterns:
        match = re.search(pat, body_text, re.IGNORECASE | re.MULTILINE)
        if match:
            name = match.group(1).strip().rstrip(',').strip()
            # Clean up OCR artifacts
            name = re.sub(r'\s+', ' ', name)
            name = name.strip('*').strip()
            if len(name) > 2 and name.upper() not in ('THE', 'THIS', 'PER', 'UPON'):
                return format_ponente(name)

    # Strategy 2: PER CURIAM
    if re.search(r'PER\s*CUR[/I]?A?M', body_text, re.IGNORECASE):
        return 'Per Curiam'

    # Strategy 3: Known justice fuzzy match near DECISION keyword
    # Find the DECISION/RESOLUTION keyword position
    dec_match = re.search(
        r'(?:D\s*E\s*C\s*I\s*S\s*I\s*O\s*N|DECISION|RESOLUTION)',
        body_text, re.IGNORECASE
    )
    if dec_match:
        # Look in the next 500 chars after DECISION
        search_region = body_text[dec_match.end():dec_match.end() + 500].upper()
        for justice in JUSTICES_2021_2026:
            if justice in search_region:
                return format_ponente(justice)

    return None


def format_ponente(name):
    """Format extracted ponente name to standard form: 'Name, J.'"""
    name = name.strip().upper()
    # Remove trailing punctuation artifacts
    name = re.sub(r'[,\s]+$', '', name)
    # Title case
    parts = name.split('-')
    titled = '-'.join(p.capitalize() for p in parts)
    # Special case: LAZARO-JAVIER
    titled = titled.replace('Lazaro-Javier', 'Lazaro-Javier')
    return f'{titled}, J.'


# ── P5: OCR Noise Stripping ──────────────────────────────────────────────────

def strip_ocr_noise(body_lines):
    """Strip OCR garbage from the start of body text."""
    # Find where real content starts
    real_content_patterns = [
        r'manila', r'republic', r'supreme\s*court',
        r'en\s*banc', r'first\s*division', r'second\s*division',
        r'third\s*division', r'g\.?\s*r\.?', r'a\.?\s*c\.?',
        r'a\.?\s*m\.?', r'b\.?\s*m\.?',
    ]

    cleaned = []
    noise_stripped = False
    content_started = False

    for line in body_lines:
        if content_started:
            cleaned.append(line)
            continue

        stripped = line.lstrip('> ').strip()

        # Empty/blank blockquote lines are OK
        if stripped == '' or line.strip() == '>':
            if not noise_stripped:
                continue  # skip leading blanks
            cleaned.append(line)
            continue

        # Check if this line has recognizable content
        is_content = False
        for pat in real_content_patterns:
            if re.search(pat, stripped, re.IGNORECASE):
                is_content = True
                break

        # Also consider length — real content lines are usually >5 chars
        if len(stripped) > 10:
            is_content = True

        if is_content:
            content_started = True
            cleaned.append(line)
        else:
            # Short garbage line — strip it
            noise_stripped = True

    return cleaned, noise_stripped


# ── P6: Opinion Type Detection ────────────────────────────────────────────────

def detect_opinion_type(body_lines, filename):
    """Detect opinion type from body text and filename."""
    body_text = '\n'.join(body_lines[:100])  # check first 100 lines
    upper = body_text.upper()

    for keyword, label in OPINION_TYPES:
        if keyword in upper:
            return label

    return 'Decision'


# ── Main Processing ───────────────────────────────────────────────────────────

def process_file(filepath, dry_run=False):
    """Process a single file. Returns list of changes or None if skipped."""
    content = Path(filepath).read_text(encoding='utf-8')

    # Only process SC-scraped files
    if 'sc.judiciary.gov.ph' not in content:
        return None

    parsed = parse_file(content)
    if parsed is None:
        return ['PARSE_ERROR']

    h1_line, subtitle, metadata, body_lines = parsed
    changes = []
    filename = Path(filepath).name

    # ── P1+P2: Case Number + H1 ──────────────────────────────────────────
    formal_cn = derive_case_number(filename)

    if 'Case Number' not in metadata:
        metadata['Case Number'] = formal_cn
        changes.append(f'+Case Number: {formal_cn}')

    # Fix H1 if it's in filename format (GR-270257 instead of G.R. No. 270257)
    if h1_line != formal_cn and not h1_line.startswith('G.R. No.') and not h1_line.startswith('A.'):
        h1_line = formal_cn
        changes.append(f'H1→{formal_cn}')

    # ── P3: Reorder metadata ──────────────────────────────────────────────
    current_order = list(metadata.keys())
    target_order = [k for k in FIELD_ORDER if k in metadata]
    # Add any extra fields not in FIELD_ORDER
    for k in current_order:
        if k not in target_order:
            target_order.append(k)

    if current_order != target_order:
        changes.append('reordered metadata')

    # ── P4: Fix [UNKNOWN] ponente ─────────────────────────────────────────
    if metadata.get('Ponente', '') == '[UNKNOWN]':
        ponente = extract_ponente_from_body(body_lines)
        if ponente:
            metadata['Ponente'] = ponente
            changes.append(f'ponente→{ponente}')

    # ── P5: Strip OCR noise ───────────────────────────────────────────────
    cleaned_body, had_noise = strip_ocr_noise(body_lines)
    if had_noise:
        body_lines = cleaned_body
        changes.append('stripped OCR noise')

    # ── P6: Opinion type ──────────────────────────────────────────────────
    detected_type = detect_opinion_type(body_lines, filename)
    current_type = metadata.get('Type', 'Decision')
    if detected_type != 'Decision' and current_type == 'Decision':
        metadata['Type'] = detected_type
        changes.append(f'type→{detected_type}')

    # ── Reconstruct ───────────────────────────────────────────────────────
    if not changes:
        return []

    if not dry_run:
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
        # Any extra fields
        for key in metadata:
            if key not in FIELD_ORDER:
                out_lines.append(f'- **{key}**: {metadata[key]}')
        out_lines.append('')
        out_lines.append('---')
        out_lines.append('')
        out_lines.extend(body_lines)

        # Ensure trailing newline
        output = '\n'.join(out_lines)
        if not output.endswith('\n'):
            output += '\n'

        Path(filepath).write_text(output, encoding='utf-8')

    return changes


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Reformat SC-scraped jurisprudence files')
    parser.add_argument('--year', type=int, help='Process only this year (2021-2026)')
    parser.add_argument('--dry-run', action='store_true', help='Report changes without writing')
    parser.add_argument('--file', type=str, help='Process a single file')
    args = parser.parse_args()

    if args.file:
        filepath = Path(args.file)
        if not filepath.exists():
            print(f'File not found: {filepath}')
            sys.exit(1)
        changes = process_file(filepath, dry_run=args.dry_run)
        if changes is None:
            print(f'{filepath.name}: SKIP (not SC-scraped)')
        elif not changes:
            print(f'{filepath.name}: no changes needed')
        else:
            print(f'{filepath.name}: {", ".join(changes)}')
        return

    years = [args.year] if args.year else list(range(2021, 2027))
    total_files = 0
    total_changed = 0
    total_skipped = 0
    total_errors = 0
    fix_counts = {}

    for year in years:
        year_dir = JURISPRUDENCE_DIR / str(year)
        if not year_dir.exists():
            continue

        md_files = sorted(year_dir.glob('*.md'))
        md_files = [f for f in md_files if f.name != 'INDEX.md']

        print(f'\n=== {year} ({len(md_files)} files) ===')

        for i, filepath in enumerate(md_files):
            total_files += 1
            changes = process_file(filepath, dry_run=args.dry_run)

            if changes is None:
                total_skipped += 1
                continue

            if changes and changes[0] == 'PARSE_ERROR':
                total_errors += 1
                print(f'  [{i+1}/{len(md_files)}] {filepath.name}: PARSE ERROR')
                continue

            if changes:
                total_changed += 1
                prefix = 'WOULD' if args.dry_run else 'DONE'
                print(f'  [{i+1}/{len(md_files)}] {filepath.name}: {prefix} — {", ".join(changes)}')
                for c in changes:
                    key = c.split('→')[0].split(':')[0].strip('+')
                    fix_counts[key] = fix_counts.get(key, 0) + 1

    # Summary
    print(f'\n=== Summary ===')
    print(f'Total files scanned: {total_files}')
    print(f'SC files changed:    {total_changed}')
    print(f'Lawphil skipped:     {total_skipped}')
    print(f'Parse errors:        {total_errors}')
    if fix_counts:
        print(f'\nFix breakdown:')
        for fix, count in sorted(fix_counts.items()):
            print(f'  {fix}: {count}')


if __name__ == '__main__':
    main()
