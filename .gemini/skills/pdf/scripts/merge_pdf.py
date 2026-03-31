#!/usr/bin/env python3
"""Merge multiple PDF files into one.

Usage:
    python merge_pdf.py output.pdf input1.pdf input2.pdf [input3.pdf ...]
"""

import sys
from pypdf import PdfWriter


def merge_pdfs(output_path: str, input_paths: list[str]):
    writer = PdfWriter()
    for path in input_paths:
        writer.append(path)
        print(f"  Added: {path}")
    writer.write(output_path)
    writer.close()
    print(f"Merged PDF: {output_path}")


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python merge_pdf.py output.pdf input1.pdf input2.pdf ...")
        sys.exit(1)
    merge_pdfs(sys.argv[1], sys.argv[2:])
