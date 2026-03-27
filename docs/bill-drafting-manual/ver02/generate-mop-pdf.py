#!/usr/bin/env python3
"""
Generate a professional PDF of the Manual of Operations for Bill Drafting
from the single Markdown source file.

Usage:
    python3 generate-mop-pdf.py

Dependencies:
    pip3 install markdown weasyprint
"""

import sys
import markdown
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).parent
SOURCE_MD = BASE_DIR / "Manual-of-Operations-Bill-Drafting.md"
TEMPLATE_PATH = BASE_DIR / "guidebook-template.html"
OUTPUT_PDF = BASE_DIR / "Manual-of-Operations-Bill-Drafting.pdf"
OUTPUT_HTML = BASE_DIR / "mop-rendered.html"  # intermediate, for debugging

# Markdown extensions
MD_EXTENSIONS = [
    "tables",
    "fenced_code",
    "toc",
    "smarty",
    "attr_list",
    "def_list",
    "md_in_html",
]


def read_template() -> str:
    """Read the guidebook HTML template and extract the CSS."""
    if not TEMPLATE_PATH.exists():
        print(f"[ERROR] Template not found: {TEMPLATE_PATH}")
        sys.exit(1)
    return TEMPLATE_PATH.read_text(encoding="utf-8")


def extract_css(template_html: str) -> str:
    """Extract the <style> block from the guidebook template."""
    import re
    match = re.search(r'<style>(.*?)</style>', template_html, re.DOTALL)
    if not match:
        print("[ERROR] Could not extract CSS from template.")
        sys.exit(1)
    return match.group(1)


def customize_css(css: str) -> str:
    """Customize the guidebook CSS for the MOP — update headers/footers."""
    # Replace the running header content
    css = css.replace(
        'content: string(chapter-title);',
        'content: "Manual of Operations \\2014  Legislative Drafting";',
        1  # only first occurrence (default @page)
    )
    # Replace remaining occurrences in landscape page
    css = css.replace(
        'content: string(chapter-title);',
        'content: "Manual of Operations \\2014  Legislative Drafting";',
    )

    # Replace footer left text
    css = css.replace(
        'content: "Bill Drafting Guidebook \\2014  Bangsamoro Parliament\\A Saidamen R. Mambayao";',
        'content: "Manual of Operations \\2014  Bangsamoro Parliament";',
    )

    return css


def build_cover_html() -> str:
    """Build the MOP cover page HTML."""
    return """
<!-- ======== COVER PAGE ======== -->
<div class="cover-page">
  <div class="cover-institution-top">Bangsamoro Parliament</div>
  <div class="cover-title">MANUAL OF OPERATIONS</div>
  <div class="cover-gold-line"></div>
  <div class="cover-subtitle">Legislative Drafting for MP Offices</div>
  <div class="cover-author">Saidamen R. Mambayao</div>
  <div class="cover-bottom-block">
    <div class="cover-institution">Bangsamoro Parliament</div>
    <div class="cover-institution-barmm">Bangsamoro Autonomous Region in Muslim Mindanao</div>
    <div class="cover-location">Bangsamoro Government Center, Cotabato City</div>
  </div>
</div>
"""


def convert_md_to_html(md_text: str) -> str:
    """Convert markdown string to HTML."""
    return markdown.markdown(
        md_text,
        extensions=MD_EXTENSIONS,
        output_format="html5",
    )


def wrap_chapters(html_content: str) -> str:
    """Wrap each H1 section in a <div class="chapter"> for page breaks."""
    import re
    # Split on H1 tags, keeping the tags
    parts = re.split(r'(<h1[^>]*>)', html_content)

    result = []
    chapter_open = False
    for part in parts:
        if part.startswith('<h1'):
            if chapter_open:
                result.append('</div>')
            result.append('<div class="chapter">')
            chapter_open = True
        result.append(part)

    if chapter_open:
        result.append('</div>')

    return ''.join(result)


def build_full_html(css: str, cover_html: str, content_html: str) -> str:
    """Assemble the complete HTML document."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Manual of Operations — Legislative Drafting for MP Offices</title>
<style>
{css}
</style>
</head>
<body>

{cover_html}

{content_html}

</body>
</html>
"""


def generate_pdf(html_path: Path, pdf_path: Path):
    """Generate PDF from HTML using WeasyPrint."""
    try:
        from weasyprint import HTML
    except ImportError:
        print("[ERROR] WeasyPrint not installed. Run: pip3 install weasyprint")
        sys.exit(1)

    print(f"  Generating PDF with WeasyPrint...")
    HTML(filename=str(html_path)).write_pdf(str(pdf_path))
    print(f"  [OK] PDF saved: {pdf_path}")


def main():
    print("=" * 60)
    print("  Manual of Operations — PDF Generator")
    print("=" * 60)

    # 1. Read source markdown
    if not SOURCE_MD.exists():
        print(f"[ERROR] Source file not found: {SOURCE_MD}")
        sys.exit(1)

    md_text = SOURCE_MD.read_text(encoding="utf-8")
    print(f"  [OK] Read source: {SOURCE_MD.name} ({len(md_text):,} chars)")

    # 2. Read and customize CSS from guidebook template
    template_html = read_template()
    css = extract_css(template_html)
    css = customize_css(css)
    print(f"  [OK] Extracted and customized CSS from template")

    # 3. Convert markdown to HTML
    content_html = convert_md_to_html(md_text)
    content_html = wrap_chapters(content_html)
    print(f"  [OK] Converted markdown to HTML ({len(content_html):,} chars)")

    # 4. Build cover page
    cover_html = build_cover_html()

    # 5. Assemble full HTML
    full_html = build_full_html(css, cover_html, content_html)

    # 6. Write intermediate HTML (for debugging)
    OUTPUT_HTML.write_text(full_html, encoding="utf-8")
    print(f"  [OK] Intermediate HTML saved: {OUTPUT_HTML.name}")

    # 7. Generate PDF
    generate_pdf(OUTPUT_HTML, OUTPUT_PDF)

    # 8. Report file size
    pdf_size = OUTPUT_PDF.stat().st_size
    if pdf_size > 1_048_576:
        print(f"  [OK] PDF size: {pdf_size / 1_048_576:.1f} MB")
    else:
        print(f"  [OK] PDF size: {pdf_size / 1024:.0f} KB")

    print("=" * 60)
    print("  Done!")
    print("=" * 60)


if __name__ == "__main__":
    main()
