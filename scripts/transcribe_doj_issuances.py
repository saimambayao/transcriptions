#!/usr/bin/env python3
"""
Batch transcription of DOJ Issuances PDFs.

Reads all PDFs from legislation/issuances/doj/pdfs/, extracts embedded text
using pdfplumber, and updates the corresponding markdown metadata files with
the full transcription.

Usage:
    python3 scripts/transcribe_doj_issuances.py [options]

Options:
    --pdf-dir <dir>     PDF directory (default: legislation/issuances/doj/pdfs)
    --md-dir <dir>      Markdown directory (default: legislation/issuances/doj)
    --overwrite         Overwrite existing transcriptions (default: skip)
    --file <pdf>        Transcribe a single PDF file only
    --help              Show this help message
"""

import os
import sys
import re
import argparse
import glob
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(SCRIPT_DIR)
TRANSCRIBER_SCRIPTS = os.path.expanduser('~/.claude/skills/transcriber/scripts')

# Add transcriber scripts to path
sys.path.insert(0, TRANSCRIBER_SCRIPTS)

def has_embedded_text(pdf_path):
    """Check if a PDF has embedded text or requires OCR."""
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages[:3]:  # check first 3 pages
                text = page.extract_text() or ''
                if len(text.strip()) > 20:
                    return True
        return False
    except Exception:
        return False


def extract_pdf_text_embedded(pdf_path):
    """Extract embedded text from a PDF using pdfplumber."""
    try:
        import pdfplumber
    except ImportError:
        return None, "pdfplumber not installed"

    pages_text = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text() or ''
                pages_text.append(f"### Page {i + 1}\n\n{text.strip()}")
    except Exception as e:
        return None, str(e)

    return '\n\n'.join(pages_text), None


def extract_pdf_text_ocr(pdf_path):
    """Extract text from a scanned PDF using PyMuPDF + pytesseract."""
    try:
        import fitz  # pymupdf
        import pytesseract
        from PIL import Image
        import io
    except ImportError as e:
        return None, f"Missing dependency: {e}"

    pages_text = []
    try:
        doc = fitz.open(pdf_path)
        for i, page in enumerate(doc):
            mat = fitz.Matrix(400 / 72, 400 / 72)  # 400 DPI
            pix = page.get_pixmap(matrix=mat)
            img = Image.open(io.BytesIO(pix.tobytes('png')))
            text = pytesseract.image_to_string(img, lang='eng')
            pages_text.append(f"### Page {i + 1}\n\n{text.strip()}")
        doc.close()
    except Exception as e:
        return None, str(e)

    return '\n\n'.join(pages_text), None


def extract_pdf_text(pdf_path):
    """Extract text from a PDF, using OCR fallback for scanned PDFs."""
    if has_embedded_text(pdf_path):
        return extract_pdf_text_embedded(pdf_path)
    else:
        return extract_pdf_text_ocr(pdf_path)


def clean_transcription(text):
    """Clean up extracted text: remove letterhead artifacts, normalize whitespace."""
    # Remove common DOJ letterhead noise
    noise_patterns = [
        r'^S\s*tNT\s*o[,.]?\s*',
        r'Republika ng Pilipinas\s*',
        r'KAGAWARAN NG KATARUNGAN\s*',
        r'Department of Justice\s*',
        r'Manila\s*',
        r'^hd\s*a\s*$',
        r'^NO\.m\s*$',
    ]
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        skip = False
        stripped = line.strip()
        for pattern in noise_patterns:
            if re.match(pattern, stripped, re.IGNORECASE):
                skip = True
                break
        if not skip:
            cleaned_lines.append(line)

    # Collapse 3+ consecutive blank lines to 2
    result = '\n'.join(cleaned_lines)
    result = re.sub(r'\n{4,}', '\n\n\n', result)
    return result.strip()


def find_markdown_file(pdf_filename, md_dir):
    """Find the markdown file corresponding to a PDF filename."""
    # PDF filenames look like "DC 010.pdf", "DC2016NOV059 ...pdf", etc.
    pdf_base = os.path.splitext(pdf_filename)[0].strip()

    # Try to match by searching for the Local PDF field in markdown files
    md_files = glob.glob(os.path.join(md_dir, '*.md'))
    md_files = [f for f in md_files if os.path.basename(f) != 'INDEX.md']

    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            # Look for "Local PDF: pdfs/<filename>"
            if f'pdfs/{pdf_filename}' in content or f'pdfs/{pdf_base}' in content:
                return md_file
        except Exception:
            continue

    return None


def update_markdown_transcription(md_path, transcription_text, overwrite=False):
    """Update the Transcription section in a markdown file."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if transcription already exists
    transcription_placeholder = '_Transcription pending. Run the /transcriber skill on the PDF file._'
    has_placeholder = transcription_placeholder in content
    has_existing = '## Transcription' in content and not has_placeholder

    if has_existing and not overwrite:
        return False, 'skipped (transcription exists)'

    new_transcription_section = f'## Transcription\n\n{transcription_text}'

    if has_placeholder:
        new_content = content.replace(
            f'## Transcription\n\n{transcription_placeholder}',
            new_transcription_section
        )
    elif '## Transcription' in content:
        # Replace existing transcription section
        new_content = re.sub(
            r'## Transcription\n\n.*$',
            new_transcription_section,
            content,
            flags=re.DOTALL
        )
    else:
        # Append at end
        new_content = content.rstrip() + f'\n\n{new_transcription_section}\n'

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, 'updated'


def main():
    parser = argparse.ArgumentParser(description='Batch transcribe DOJ Issuances PDFs')
    parser.add_argument('--pdf-dir', default=os.path.join(REPO_DIR, 'legislation/issuances/doj/pdfs'))
    parser.add_argument('--md-dir', default=os.path.join(REPO_DIR, 'legislation/issuances/doj'))
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing transcriptions')
    parser.add_argument('--file', help='Transcribe a single PDF file (just the filename, not path)')
    args = parser.parse_args()

    pdf_dir = os.path.abspath(args.pdf_dir)
    md_dir = os.path.abspath(args.md_dir)

    print('=== DOJ Issuances Batch Transcriber ===')
    print(f'PDFs:      {pdf_dir}')
    print(f'Markdown:  {md_dir}')
    print(f'Overwrite: {args.overwrite}')
    print('')

    # Get list of PDFs to process
    if args.file:
        pdf_files = [args.file]
    else:
        pdf_files = sorted([
            f for f in os.listdir(pdf_dir)
            if f.lower().endswith('.pdf')
        ])

    total = len(pdf_files)
    print(f'Found {total} PDFs to process.\n')

    success = 0
    skipped = 0
    failed = 0
    no_md = 0

    for i, pdf_filename in enumerate(pdf_files):
        pdf_path = os.path.join(pdf_dir, pdf_filename)
        print(f'[{i+1}/{total}] {pdf_filename}: ', end='', flush=True)

        # Find corresponding markdown file
        md_path = find_markdown_file(pdf_filename, md_dir)
        if not md_path:
            print(f'NO MARKDOWN FILE FOUND')
            no_md += 1
            continue

        md_name = os.path.basename(md_path)

        # Extract text from PDF
        text, error = extract_pdf_text(pdf_path)
        if error:
            print(f'EXTRACT ERROR: {error[:80]}')
            failed += 1
            continue

        if not text or len(text.strip()) < 20:
            print(f'EMPTY/SHORT TEXT (len={len(text) if text else 0})')
            failed += 1
            continue

        # Clean up the extracted text
        cleaned_text = clean_transcription(text)

        # Update markdown file
        updated, status = update_markdown_transcription(md_path, cleaned_text, overwrite=args.overwrite)

        if updated:
            print(f'{status} ({md_name}, {len(cleaned_text):,} chars)')
            success += 1
        else:
            print(f'{status}')
            skipped += 1

        # Small rate limit
        time.sleep(0.05)

    print(f'\n=== Transcription Complete ===')
    print(f'Total:       {total}')
    print(f'Updated:     {success}')
    print(f'Skipped:     {skipped}')
    print(f'No markdown: {no_md}')
    print(f'Failed:      {failed}')


if __name__ == '__main__':
    main()
