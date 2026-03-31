#!/usr/bin/env python3
"""Convert an HTML file to a professionally styled PDF using WeasyPrint.

Usage:
    python create_pdf.py input.html output.pdf [--base-url BASE_URL]

Arguments:
    input.html    Path to the HTML file to convert
    output.pdf    Path for the output PDF file
    --base-url    Base URL for resolving relative paths (images, fonts, etc.)
                  Defaults to the directory containing the HTML file.
"""

import argparse
import os
import sys

try:
    from weasyprint import HTML
except ImportError:
    print("Error: weasyprint is not installed.")
    print("Install it with: pip install weasyprint")
    print("On macOS also run: brew install pango cairo libffi")
    sys.exit(1)


def create_pdf(input_html: str, output_pdf: str, base_url: str | None = None):
    """Convert HTML file to PDF."""
    if not os.path.exists(input_html):
        print(f"Error: Input file not found: {input_html}")
        sys.exit(1)

    if base_url is None:
        base_url = os.path.dirname(os.path.abspath(input_html))

    html = HTML(filename=input_html, base_url=base_url)
    html.write_pdf(output_pdf)
    print(f"PDF created: {output_pdf}")


def create_pdf_from_string(html_string: str, output_pdf: str, base_url: str | None = None):
    """Convert HTML string to PDF."""
    html = HTML(string=html_string, base_url=base_url or os.getcwd())
    html.write_pdf(output_pdf)
    print(f"PDF created: {output_pdf}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert HTML to PDF')
    parser.add_argument('input', help='Input HTML file')
    parser.add_argument('output', help='Output PDF file')
    parser.add_argument('--base-url', help='Base URL for resolving relative paths')
    args = parser.parse_args()

    create_pdf(args.input, args.output, args.base_url)
