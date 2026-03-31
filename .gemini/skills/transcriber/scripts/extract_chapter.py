#!/usr/bin/env python3
"""
Extract chapter from PDF using OCR (PyMuPDF + pytesseract).

Usage:
    python extract_chapter.py <pdf_path> <start_page> <end_page> [output_file]

Example:
    python extract_chapter.py "references/pdf-files/BDP.pdf" 45 62 /tmp/chapter_ocr.txt

Requirements:
    brew install tesseract
    pip install pymupdf pytesseract pillow
"""

import sys
import io
import fitz  # PyMuPDF
import pytesseract
from PIL import Image


def extract_pages(pdf_path: str, start_page: int, end_page: int, dpi: int = 400) -> str:
    """
    Extract text from PDF pages using OCR.

    Args:
        pdf_path: Path to PDF file
        start_page: First page to extract (1-indexed)
        end_page: Last page to extract (1-indexed)
        dpi: Resolution for OCR (300=standard, 400=better, 600=best)

    Returns:
        Extracted text with page markers
    """
    doc = fitz.open(pdf_path)
    all_text = ""

    # Convert to 0-indexed
    for page_num in range(start_page - 1, end_page):
        page = doc[page_num]

        # Render at specified DPI (72 is PDF default)
        mat = fitz.Matrix(dpi / 72, dpi / 72)
        pix = page.get_pixmap(matrix=mat)

        # Convert to PIL Image for OCR
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text = pytesseract.image_to_string(img, lang='eng')

        all_text += f"\n\n{'=' * 60}\nPAGE {page_num + 1}\n{'=' * 60}\n{text}"

        # Progress indicator
        print(f"Processed page {page_num + 1}/{end_page}", file=sys.stderr)

    doc.close()
    return all_text


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)

    pdf_path = sys.argv[1]
    start_page = int(sys.argv[2])
    end_page = int(sys.argv[3])
    output_file = sys.argv[4] if len(sys.argv) > 4 else "/tmp/chapter_ocr.txt"

    print(f"Extracting pages {start_page}-{end_page} from {pdf_path}", file=sys.stderr)
    print(f"Output: {output_file}", file=sys.stderr)

    text = extract_pages(pdf_path, start_page, end_page)

    with open(output_file, "w") as f:
        f.write(text)

    print(f"\nExtraction complete. Output saved to {output_file}", file=sys.stderr)


if __name__ == "__main__":
    main()
