#!/usr/bin/env python3
"""
Find chapter boundaries in a PDF by scanning page headers.

Usage:
    python find_chapter.py <pdf_path> [chapter_num]

Example:
    python find_chapter.py "references/pdf-files/BDP.pdf" 5
    python find_chapter.py "references/pdf-files/BDP.pdf"  # Find all chapters

Requirements:
    pip install pymupdf
"""

import sys
import fitz  # PyMuPDF


def find_chapter_start(pdf_path: str, chapter_num: int) -> int | None:
    """Find the page number where a specific chapter starts."""
    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()

        # Look for chapter header patterns
        if f"Chapter {chapter_num}" in text or f"CHAPTER {chapter_num}" in text:
            doc.close()
            return page_num + 1  # Return 1-indexed page number

    doc.close()
    return None


def find_all_chapters(pdf_path: str) -> list[tuple[int, int]]:
    """Find all chapter boundaries in the PDF."""
    doc = fitz.open(pdf_path)
    chapters = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()[:500]  # Check first 500 chars

        # Look for chapter patterns
        for i in range(1, 20):  # Check chapters 1-19
            if f"Chapter {i}" in text or f"CHAPTER {i}" in text:
                # Avoid duplicates
                if not chapters or chapters[-1][0] != i:
                    chapters.append((i, page_num + 1))
                break

    doc.close()
    return chapters


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    pdf_path = sys.argv[1]

    if len(sys.argv) > 2:
        # Find specific chapter
        chapter_num = int(sys.argv[2])
        page = find_chapter_start(pdf_path, chapter_num)

        if page:
            print(f"Chapter {chapter_num} starts at page {page}")
        else:
            print(f"Chapter {chapter_num} not found")
    else:
        # Find all chapters
        chapters = find_all_chapters(pdf_path)

        print("Chapter boundaries found:")
        print("-" * 30)
        for chapter_num, page in chapters:
            print(f"Chapter {chapter_num}: page {page}")


if __name__ == "__main__":
    main()
