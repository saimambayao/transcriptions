#!/usr/bin/env python3
"""
Generate separate PDF documents for each appendix (A through G)
of the Bill Drafting Guidebook for the Bangsamoro Parliament.

Usage:
    python3 generate-appendices.py

Dependencies:
    pip3 install markdown weasyprint
"""

import os
import sys
import re
import markdown
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).parent
TEMPLATE_PATH = BASE_DIR / "guidebook-template.html"
OUTPUT_DIR = BASE_DIR / "appendices"

# Source markdown files for appendices
SOURCE_FILES = {
    "A-D": BASE_DIR / "14-appendices-a-d.md",
    "E-G": BASE_DIR / "15-appendices-e-g.md",
}

# Appendix definitions: key, output filename, source group, landscape flag
APPENDICES = [
    {"key": "A", "filename": "Appendix-A-Enumerated-Powers.pdf",           "source": "A-D", "landscape": False},
    {"key": "B", "filename": "Appendix-B-Sample-BAA-Annotated.pdf",        "source": "A-D", "landscape": False},
    {"key": "C", "filename": "Appendix-C-Sample-Resolution-Annotated.pdf", "source": "A-D", "landscape": False},
    {"key": "D", "filename": "Appendix-D-Pre-Drafting-Checklist.pdf",      "source": "A-D", "landscape": False},
    {"key": "E", "filename": "Appendix-E-Quality-Review-Checklist.pdf",    "source": "E-G", "landscape": False},
    {"key": "F", "filename": "Appendix-F-Legislative-Briefer-Template.pdf","source": "E-G", "landscape": True},
    {"key": "G", "filename": "Appendix-G-Budget-Briefer-Template.pdf",     "source": "E-G", "landscape": True},
]

# Markdown extensions (same as generate-pdf.py)
MD_EXTENSIONS = [
    "tables",
    "fenced_code",
    "codehilite",
    "toc",
    "smarty",
    "attr_list",
    "def_list",
    "md_in_html",
]


def read_source_files() -> dict[str, str]:
    """Read both source markdown files."""
    sources = {}
    for key, fpath in SOURCE_FILES.items():
        if not fpath.exists():
            print(f"  [ERROR] Missing source file: {fpath}")
            sys.exit(1)
        content = fpath.read_text(encoding="utf-8")
        sources[key] = content
        print(f"  [OK]  Read {fpath.name} ({len(content):,} chars)")
    return sources


def split_appendices(sources: dict[str, str]) -> dict[str, str]:
    """Split the markdown content at appendix headings.

    File 14 uses: ## Appendix A: Title (H2 with colon)
    File 15 uses: # Appendix E -- Title  (H1 with em-dash)

    Both patterns are matched. Each appendix's heading is promoted to H1
    in the output for consistent PDF rendering.

    Returns a dict mapping appendix key (A, B, C, ...) to its markdown content.
    """
    appendix_content = {}

    for source_key, full_text in sources.items():
        # Split on any heading level that starts with "Appendix [A-G]"
        # This handles both ## Appendix A: and # Appendix E --
        parts = re.split(r'(?=^#{1,2} Appendix [A-G])', full_text, flags=re.MULTILINE)

        for part in parts:
            part = part.strip()
            if not part:
                continue

            # Extract the appendix letter from the heading (H1 or H2)
            match = re.match(r'^(#{1,2}) Appendix ([A-G])', part)
            if match:
                heading_level = match.group(1)
                letter = match.group(2)

                # Promote H2 headings to H1 for consistent rendering
                if heading_level == '##':
                    # Replace the first ## with # and normalize separator
                    part = re.sub(r'^## (Appendix [A-G]):', r'# \1 —', part, count=1)

                appendix_content[letter] = part
                print(f"  [OK]  Extracted Appendix {letter} ({len(part):,} chars)")

    return appendix_content


def convert_md_to_html(md_text: str) -> str:
    """Convert a markdown string to HTML using python-markdown."""
    return markdown.markdown(
        md_text,
        extensions=MD_EXTENSIONS,
        output_format="html5",
    )


def post_process_html(html: str) -> str:
    """Apply post-processing fixes to the generated HTML.

    Same transformations as generate-pdf.py.
    """
    # Convert page break comments to CSS page breaks
    html = html.replace("<!-- PAGE BREAK -->", '<div style="page-break-before: always;"></div>')
    html = html.replace("&lt;!-- PAGE BREAK --&gt;", '<div style="page-break-before: always;"></div>')

    # Convert landscape markers to landscape page divs
    html = html.replace("<!-- LANDSCAPE START -->", '<div class="landscape-page">')
    html = html.replace("<!-- LANDSCAPE END -->", '</div>')
    html = html.replace("&lt;!-- LANDSCAPE START --&gt;", '<div class="landscape-page">')
    html = html.replace("&lt;!-- LANDSCAPE END --&gt;", '</div>')

    # Convert checkbox patterns to Unicode
    html = html.replace("[ ]", "&#9744;")  # empty checkbox
    html = html.replace("[x]", "&#9745;")  # checked checkbox
    html = html.replace("[X]", "&#9745;")

    # Replace dot patterns with proper CSS form lines
    html = re.sub(r'\.{10,}', '<span class="form-line-wide"></span>', html)
    html = re.sub(r'\.{4,9}', '<span class="form-line"></span>', html)

    # Tag checklist tables (5-col tables with Yes/No/N/A headers)
    html = re.sub(
        r'<table>\s*<thead>\s*<tr>\s*<th[^>]*>No\.</th>\s*<th[^>]*>Item</th>\s*<th[^>]*>Yes</th>\s*<th[^>]*>No</th>\s*<th[^>]*>N/A</th>',
        '<table class="checklist-table"><thead><tr><th>No.</th><th>Item</th><th>Yes</th><th>No</th><th>N/A</th>',
        html
    )

    # Add anchor IDs to all H1 headings
    def add_anchor_to_h1(match):
        content = match.group(1)
        anchor = re.sub(r'[^a-z0-9]+', '-', content.lower()).strip('-')
        return f'<h1 id="{anchor}">{content}</h1>'

    html = re.sub(r'<h1>(.*?)</h1>', add_anchor_to_h1, html)

    return html


def build_appendix_html(appendix_key: str, md_content: str, use_landscape: bool) -> str:
    """Build the complete HTML document for a single appendix.

    Uses the guidebook-template.html but replaces the cover page with
    a simpler appendix-specific header, and injects the content.
    """
    # Read template
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    # Convert markdown to HTML
    html_content = convert_md_to_html(md_content)

    # Wrap in a chapter div
    wrapped = f'<div class="chapter" id="appendix-{appendix_key.lower()}">\n{html_content}\n</div>\n'

    # If the entire appendix should default to landscape (F, G),
    # wrap tables that aren't already in landscape divs
    if use_landscape:
        # Don't double-wrap - the LANDSCAPE START/END markers in the source
        # will be converted by post_process_html. For F and G, we also add
        # a CSS override for the default page to be landscape.
        pass

    # Apply post-processing
    wrapped = post_process_html(wrapped)

    # Replace the cover page in the template with nothing (no cover for appendices)
    # and inject content
    # First, remove the cover page div from the template
    modified_template = re.sub(
        r'<!-- ======== COVER PAGE ======== -->.*?(?=<!-- ======== CONTENT)',
        '',
        template,
        flags=re.DOTALL,
    )

    # For landscape appendices (F, G), add a default landscape page rule
    if use_landscape:
        landscape_override = """
/* Override default page to landscape for wide-table appendices */
@page {
  size: A4 landscape;
  margin: 22mm 25mm 25mm 25mm;
}
"""
        # Insert before the closing </style> tag
        modified_template = modified_template.replace('</style>', landscape_override + '</style>')

    # Inject content
    full_html = modified_template.replace("{{CONTENT}}", wrapped)

    return full_html


def generate_pdf(html: str, output_path: Path) -> bool:
    """Generate PDF using WeasyPrint."""
    try:
        from weasyprint import HTML
        HTML(string=html, base_url=str(BASE_DIR)).write_pdf(str(output_path))
        return True
    except Exception as e:
        print(f"  [ERROR] WeasyPrint failed: {e}")
        return False


def main():
    print("=" * 60)
    print("  Bill Drafting Guidebook — Appendix PDF Generator")
    print("=" * 60)
    print()

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Step 1: Read source files
    print("[1/4] Reading source markdown files...")
    sources = read_source_files()
    print()

    # Step 2: Split into individual appendices
    print("[2/4] Splitting into individual appendices...")
    appendix_content = split_appendices(sources)
    print(f"  Total: {len(appendix_content)} appendices extracted\n")

    # Verify all expected appendices were found
    expected = {a["key"] for a in APPENDICES}
    found = set(appendix_content.keys())
    missing = expected - found
    if missing:
        print(f"  [ERROR] Missing appendices: {', '.join(sorted(missing))}")
        sys.exit(1)

    # Step 3: Generate PDFs
    print("[3/4] Generating individual PDF files...")
    results = []

    for appendix in APPENDICES:
        key = appendix["key"]
        filename = appendix["filename"]
        landscape = appendix["landscape"]
        output_path = OUTPUT_DIR / filename

        print(f"\n  --- Appendix {key}: {filename} ---")

        # Get markdown content
        md_content = appendix_content[key]

        # Build HTML
        full_html = build_appendix_html(key, md_content, landscape)
        print(f"  HTML: {len(full_html):,} chars")

        # Save intermediate HTML for debugging
        html_debug_path = OUTPUT_DIR / filename.replace('.pdf', '.html')
        html_debug_path.write_text(full_html, encoding="utf-8")

        # Generate PDF
        print(f"  Rendering PDF...")
        success = generate_pdf(full_html, output_path)

        if success and output_path.exists():
            size_kb = output_path.stat().st_size / 1024
            print(f"  [OK]  {filename} ({size_kb:.0f} KB)")
            results.append((key, filename, True, size_kb))
        else:
            print(f"  [FAIL] {filename}")
            results.append((key, filename, False, 0))

    # Step 4: Summary
    print(f"\n{'=' * 60}")
    print("  SUMMARY")
    print(f"{'=' * 60}")
    print()

    success_count = 0
    for key, filename, success, size_kb in results:
        status = f"OK ({size_kb:.0f} KB)" if success else "FAILED"
        print(f"  Appendix {key}: {filename} — {status}")
        if success:
            success_count += 1

    print(f"\n  {success_count}/{len(APPENDICES)} PDFs generated successfully")
    print(f"  Output directory: {OUTPUT_DIR}")
    print(f"{'=' * 60}")

    if success_count < len(APPENDICES):
        sys.exit(1)


if __name__ == "__main__":
    main()
