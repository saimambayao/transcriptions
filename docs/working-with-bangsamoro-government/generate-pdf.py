#!/usr/bin/env python3
"""
Generate a professional PDF of the Working with the Bangsamoro Government
guidebook from Markdown source files.

Usage:
    python3 generate-pdf.py

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
OUTPUT_PDF = BASE_DIR / "Working-with-the-Bangsamoro-Government.pdf"
OUTPUT_HTML = BASE_DIR / "guidebook-rendered.html"  # intermediate, for debugging

# Ordered list of markdown files
MD_FILES = [
    "00-table-of-contents.md",
    "00b-about.md",
    "00c-author.md",
    "01-introduction.md",
    "02-chapter-02.md",
    "03-chapter-03.md",
    "04-chapter-04.md",
    "05-chapter-05.md",
    "06-chapter-06.md",
    "07-chapter-07.md",
    "08-chapter-08.md",
    "09-chapter-09.md",
    "10-chapter-10.md",
    "11-chapter-11.md",
    "12-chapter-12.md",
    "13-chapter-13.md",
    "14-chapter-14.md",
    "15-chapter-15.md",
    "16-chapter-16.md",
    "17-chapter-17.md",
    "18-glossary.md",
]

# Markdown extensions for richer conversion
MD_EXTENSIONS = [
    "tables",
    "fenced_code",
    "codehilite",
    "toc",
    "smarty",
    "attr_list",
    "def_list",
    "md_in_html",
    "footnotes",
]


def read_markdown_files() -> list[tuple[str, str]]:
    """Read all markdown files in order, returning (filename, content) pairs."""
    sections = []
    for fname in MD_FILES:
        fpath = BASE_DIR / fname
        if not fpath.exists():
            print(f"  [WARN] Missing file: {fname}, skipping.")
            continue
        content = fpath.read_text(encoding="utf-8")
        sections.append((fname, content))
        print(f"  [OK]  Read {fname} ({len(content):,} chars)")
    return sections


def convert_md_to_html(md_text: str) -> str:
    """Convert a markdown string to HTML using python-markdown."""
    return markdown.markdown(
        md_text,
        extensions=MD_EXTENSIONS,
        output_format="html5",
    )


def build_toc_html(md_text: str) -> str:
    """Build a structured HTML Table of Contents from the markdown TOC file."""
    lines = md_text.split("\n")
    html_parts = []

    title_done = False
    subtitle_done = False
    toc_started = False

    for line in lines:
        stripped = line.strip()

        if not stripped:
            continue

        # H1 title - skip (cover page handles this)
        if stripped.startswith("# ") and not stripped.startswith("## "):
            if not title_done:
                title_done = True
                continue

        # H2 subtitle or TOC heading
        if stripped.startswith("## "):
            heading_text = stripped.lstrip("# ").strip()
            if "Table of Contents" in heading_text:
                html_parts.append(f'<h1>{heading_text}</h1>')
                html_parts.append('<div class="toc-entries">')
                toc_started = True
                continue
            elif not subtitle_done:
                subtitle_done = True
                continue

        if stripped == "---":
            continue

        if not toc_started:
            continue

        # Count &emsp; for indentation level
        emsp_count = line.count("&emsp;")
        entry_text = stripped.replace("&emsp;", "").strip()

        if not entry_text:
            continue

        is_chapter = entry_text.startswith("**") and entry_text.endswith("**")

        if is_chapter:
            entry_text = entry_text.strip("*").strip()
            css_class = "toc-chapter"
            anchor = re.sub(r'[^a-z0-9]+', '-', entry_text.lower()).strip('-')
            html_parts.append(f'<div class="{css_class}"><a href="#{anchor}">{entry_text}</a></div>')
        else:
            if emsp_count >= 3:
                css_class = "toc-entry toc-level-3"
            elif emsp_count >= 2:
                css_class = "toc-entry toc-level-2"
            elif emsp_count >= 1:
                css_class = "toc-entry toc-level-1"
            else:
                css_class = "toc-entry toc-level-0"
            html_parts.append(f'<div class="{css_class}">{entry_text}</div>')

    html_parts.append('</div>')  # close toc-entries

    return "\n".join(html_parts)


def wrap_section(fname: str, html_content: str, index: int) -> str:
    """Wrap each file's HTML in a styled <div> with appropriate classes."""

    if "table-of-contents" in fname:
        return f'<div class="toc-section">\n{html_content}\n</div>\n'

    back_link = '<div class="back-to-toc"><a href="#table-of-contents">Back to Table of Contents</a></div>'

    if "introduction" in fname:
        return f'<div class="chapter" id="introduction">\n{html_content}\n{back_link}\n</div>\n'

    if "glossary" in fname:
        return f'<div class="chapter" id="glossary">\n{html_content}\n{back_link}\n</div>\n'

    if "author" in fname:
        return f'<div class="chapter" id="author">\n{html_content}\n{back_link}\n</div>\n'

    if "about" in fname:
        return f'<div class="chapter" id="about">\n{html_content}\n{back_link}\n</div>\n'

    chapter_match = re.search(r"chapter-(\d+)", fname)
    ch_num = chapter_match.group(1) if chapter_match else str(index)
    return f'<div class="chapter" id="chapter-{ch_num}">\n{html_content}\n{back_link}\n</div>\n'


def post_process_html(html: str) -> str:
    """Apply post-processing fixes to the generated HTML."""

    # Convert page break comments to CSS page breaks
    html = html.replace("<!-- PAGE BREAK -->", '<div style="page-break-before: always;"></div>')
    html = html.replace("&lt;!-- PAGE BREAK --&gt;", '<div style="page-break-before: always;"></div>')

    # Convert landscape markers
    html = html.replace("<!-- LANDSCAPE START -->", '<div class="landscape-page">')
    html = html.replace("<!-- LANDSCAPE END -->", '</div>')
    html = html.replace("&lt;!-- LANDSCAPE START --&gt;", '<div class="landscape-page">')
    html = html.replace("&lt;!-- LANDSCAPE END --&gt;", '</div>')

    # Convert checkbox patterns
    html = html.replace("[ ]", "&#9744;")
    html = html.replace("[x]", "&#9745;")
    html = html.replace("[X]", "&#9745;")

    # Replace dot patterns with form lines
    html = re.sub(r'\.{10,}', '<span class="form-line-wide"></span>', html)
    html = re.sub(r'\.{4,9}', '<span class="form-line"></span>', html)

    # Tag checklist tables
    html = re.sub(
        r'<table>\s*<thead>\s*<tr>\s*<th[^>]*>No\.</th>\s*<th[^>]*>Item</th>\s*<th[^>]*>Yes</th>\s*<th[^>]*>No</th>\s*<th[^>]*>N/A</th>',
        '<table class="checklist-table"><thead><tr><th>No.</th><th>Item</th><th>Yes</th><th>No</th><th>N/A</th>',
        html
    )

    # Add anchor IDs to all H1 headings for TOC linking
    def add_anchor_to_h1(match):
        content = match.group(1)
        anchor = re.sub(r'[^a-z0-9]+', '-', content.lower()).strip('-')
        return f'<h1 id="{anchor}">{content}</h1>'

    html = re.sub(r'<h1>(.*?)</h1>', add_anchor_to_h1, html)

    return html


def build_full_html(sections: list[tuple[str, str]]) -> str:
    """Build the complete HTML document from sections and template."""

    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    all_sections_html = []
    for i, (fname, md_content) in enumerate(sections):
        if "table-of-contents" in fname:
            toc_html = build_toc_html(md_content)
            wrapped = f'<div class="toc-section">\n{toc_html}\n</div>\n'
        else:
            html_content = convert_md_to_html(md_content)
            wrapped = wrap_section(fname, html_content, i)
        all_sections_html.append(wrapped)

    combined = "\n".join(all_sections_html)
    combined = post_process_html(combined)

    full_html = template.replace("{{CONTENT}}", combined)

    return full_html


def generate_pdf_weasyprint(html: str, output_path: Path) -> bool:
    """Generate PDF using WeasyPrint."""
    try:
        from weasyprint import HTML
        print("\n  Rendering PDF with WeasyPrint...")
        HTML(string=html, base_url=str(BASE_DIR)).write_pdf(
            str(output_path),
        )
        return True
    except Exception as e:
        print(f"\n  [ERROR] WeasyPrint failed: {e}")
        return False


def generate_pdf_playwright(html_path: Path, output_path: Path) -> bool:
    """Fallback: Generate PDF using Playwright."""
    try:
        import subprocess
        print("\n  Attempting Playwright fallback...")

        result = subprocess.run(
            [
                "npx", "playwright", "pdf",
                str(html_path),
                str(output_path),
                "--format", "A4",
                "--margin-top", "25mm",
                "--margin-bottom", "30mm",
                "--margin-left", "25mm",
                "--margin-right", "22mm",
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode == 0:
            return True
        else:
            print(f"  Playwright error: {result.stderr}")

            print("  Trying Playwright Python API...")
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.set_content(html_path.read_text(encoding="utf-8"))
                page.pdf(
                    path=str(output_path),
                    format="A4",
                    margin={
                        "top": "25mm",
                        "bottom": "30mm",
                        "left": "25mm",
                        "right": "22mm",
                    },
                    print_background=True,
                )
                browser.close()
            return True
    except Exception as e:
        print(f"  [ERROR] Playwright fallback failed: {e}")
        return False


def main():
    print("=" * 60)
    print("  Working with the Bangsamoro Government — PDF Generator")
    print("=" * 60)
    print()

    # Step 1: Read markdown files
    print("[1/4] Reading markdown files...")
    sections = read_markdown_files()
    if not sections:
        print("  No markdown files found. Aborting.")
        sys.exit(1)
    print(f"  Total: {len(sections)} files\n")

    # Step 2: Build HTML
    print("[2/4] Converting Markdown to HTML...")
    full_html = build_full_html(sections)
    print(f"  HTML generated: {len(full_html):,} chars\n")

    # Step 3: Save intermediate HTML
    print("[3/4] Saving intermediate HTML...")
    OUTPUT_HTML.write_text(full_html, encoding="utf-8")
    print(f"  Saved: {OUTPUT_HTML}\n")

    # Step 4: Generate PDF
    print("[4/4] Generating PDF...")
    success = generate_pdf_weasyprint(full_html, OUTPUT_PDF)

    if not success:
        print("\n  WeasyPrint failed. Trying Playwright fallback...")
        success = generate_pdf_playwright(OUTPUT_HTML, OUTPUT_PDF)

    if success and OUTPUT_PDF.exists():
        size_mb = OUTPUT_PDF.stat().st_size / (1024 * 1024)
        print(f"\n{'=' * 60}")
        print(f"  PDF generated successfully!")
        print(f"  Path: {OUTPUT_PDF}")
        print(f"  Size: {size_mb:.1f} MB")
        print(f"{'=' * 60}")
    else:
        print(f"\n  [FAIL] PDF generation failed.")
        print(f"  The intermediate HTML is available at:")
        print(f"  {OUTPUT_HTML}")
        print(f"  You can open it in a browser and print to PDF.")
        sys.exit(1)


if __name__ == "__main__":
    main()
