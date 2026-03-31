#!/usr/bin/env python3
"""
Assess PDF quality to determine extraction method.

Usage:
    python assess_pdf.py <pdf_path>

Example:
    python assess_pdf.py "references/pdf-files/BDP.pdf"

Output:
    - Whether PDF has embedded text (use pdfplumber)
    - Whether PDF requires OCR (use PyMuPDF + pytesseract)
    - Number of images per page
    - Total page count

Requirements:
    pip install pymupdf
"""

import sys
import fitz  # PyMuPDF


def assess_pdf(pdf_path: str) -> dict:
    """
    Assess PDF quality and recommend extraction method.

    Returns:
        Dictionary with assessment results
    """
    doc = fitz.open(pdf_path)

    results = {
        "total_pages": len(doc),
        "has_embedded_text": False,
        "requires_ocr": True,
        "sample_pages": [],
        "recommendation": ""
    }

    # Sample first 3 pages
    sample_count = min(3, len(doc))
    total_text_chars = 0
    total_images = 0

    for i in range(sample_count):
        page = doc[i]
        text = page.get_text().strip()
        images = page.get_images()

        page_info = {
            "page": i + 1,
            "text_chars": len(text),
            "image_count": len(images),
            "has_text": len(text) > 100
        }
        results["sample_pages"].append(page_info)

        total_text_chars += len(text)
        total_images += len(images)

    doc.close()

    # Determine extraction method
    avg_chars = total_text_chars / sample_count
    avg_images = total_images / sample_count

    if avg_chars > 500:
        results["has_embedded_text"] = True
        results["requires_ocr"] = False
        results["recommendation"] = "Use pdfplumber - PDF has embedded text"
    elif avg_images > 0:
        results["recommendation"] = "Use PyMuPDF + pytesseract - PDF is image-based/scanned"
    else:
        results["recommendation"] = "Use PyMuPDF + pytesseract - PDF may be scanned"

    return results


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    pdf_path = sys.argv[1]
    results = assess_pdf(pdf_path)

    print(f"PDF Assessment: {pdf_path}")
    print("=" * 50)
    print(f"Total pages: {results['total_pages']}")
    print(f"Has embedded text: {results['has_embedded_text']}")
    print(f"Requires OCR: {results['requires_ocr']}")
    print()
    print("Sample pages:")
    for page in results["sample_pages"]:
        print(f"  Page {page['page']}: {page['text_chars']} chars, {page['image_count']} images")
    print()
    print(f"Recommendation: {results['recommendation']}")


if __name__ == "__main__":
    main()
