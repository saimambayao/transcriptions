#!/usr/bin/env python3
"""
Extract text from PDFs with embedded text (not scanned).

Usage:
    python extract_text_only.py <pdf_path> <start_page> <end_page> [output_file]

Example:
    python extract_text_only.py "references/pdf-files/BDP.pdf" 45 62 /tmp/chapter.txt

Note: This only works for PDFs with embedded text. For scanned PDFs, use extract_chapter.py.

Requirements:
    pip install pdfplumber
"""

import sys
import pdfplumber


def extract_text(pdf_path: str, start_page: int, end_page: int) -> str:
    """
    Extract text from PDF pages (text-based PDFs only).

    Args:
        pdf_path: Path to PDF file
        start_page: First page to extract (1-indexed)
        end_page: Last page to extract (1-indexed)

    Returns:
        Extracted text with page markers
    """
    all_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        # Convert to 0-indexed
        for page_num in range(start_page - 1, end_page):
            page = pdf.pages[page_num]
            text = page.extract_text() or ""

            all_text += f"\n\n{'=' * 60}\nPAGE {page_num + 1}\n{'=' * 60}\n{text}"

            print(f"Processed page {page_num + 1}/{end_page}", file=sys.stderr)

    return all_text


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)

    pdf_path = sys.argv[1]
    start_page = int(sys.argv[2])
    end_page = int(sys.argv[3])
    output_file = sys.argv[4] if len(sys.argv) > 4 else "/tmp/chapter.txt"

    print(f"Extracting pages {start_page}-{end_page} from {pdf_path}", file=sys.stderr)

    text = extract_text(pdf_path, start_page, end_page)

    with open(output_file, "w") as f:
        f.write(text)

    print(f"\nExtraction complete. Output saved to {output_file}", file=sys.stderr)


if __name__ == "__main__":
    main()
