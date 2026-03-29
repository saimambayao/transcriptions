#!/usr/bin/env python3
"""
Generate a professional PDF of the Strategic Planning Guidebook
for the Bangsamoro Government from Markdown source files.

All markdown is converted to HTML via the python-markdown library.
No custom regex parsing of markdown syntax. HTML → PDF via WeasyPrint.

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
OUTPUT_PDF = BASE_DIR / "Strategic-Planning-Guidebook-Bangsamoro.pdf"
OUTPUT_HTML = BASE_DIR / "guidebook-rendered.html"  # intermediate, for debugging

# Ordered list of markdown files
MD_FILES = [
    "00-table-of-contents.md",
    "00b-about.md",
    "00c-author.md",
    "01-introduction.md",
    "02-chapter-01.md",
    "03-chapter-02.md",
    "04-chapter-03.md",
    "05-chapter-04.md",
    "06-chapter-05.md",
    "07-chapter-06.md",
    "08-chapter-07.md",
    "09-chapter-08.md",
    "10-chapter-09.md",
    "11-chapter-10.md",
    "12-chapter-11.md",
    "13-glossary.md",
    "14-appendices.md",
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
    """Convert a markdown string to HTML using python-markdown.
    This is the ONLY markdown-to-HTML conversion function. All files use it."""
    return markdown.markdown(
        md_text,
        extensions=MD_EXTENSIONS,
        output_format="html5",
    )


def inline_md_to_html(text: str) -> str:
    """Convert markdown inline formatting to HTML."""
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text


def build_toc_html(md_text: str) -> str:
    """Build a structured HTML Table of Contents with proper indentation.
    The TOC uses &emsp; for indentation levels and **bold** for chapter titles,
    which the markdown library renders as flat inline text. This function
    creates proper <div> elements with CSS classes for each entry."""
    lines = md_text.split("\n")
    html_parts = []

    title_done = False
    subtitle_done = False
    toc_started = False

    for line in lines:
        stripped = line.strip()

        if not stripped:
            continue

        if stripped.startswith("# ") and not stripped.startswith("## "):
            if not title_done:
                title_done = True
                continue

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
            entry_text = inline_md_to_html(entry_text)
            if emsp_count >= 3:
                css_class = "toc-entry toc-level-3"
            elif emsp_count >= 2:
                css_class = "toc-entry toc-level-2"
            elif emsp_count >= 1:
                css_class = "toc-entry toc-level-1"
            else:
                css_class = "toc-entry toc-level-0"
            html_parts.append(f'<div class="{css_class}">{entry_text}</div>')

    html_parts.append('</div>')
    return "\n".join(html_parts)


def classify_section(fname: str, index: int) -> tuple[str, str]:
    """Return (section_id, css_class) for a given filename."""
    if "table-of-contents" in fname:
        return "table-of-contents", "toc-section"
    if "about" in fname and "author" not in fname:
        return "about", "frontmatter-page"
    if "author" in fname:
        return "author", "frontmatter-page"
    if "introduction" in fname:
        return "introduction", "chapter"
    if "glossary" in fname:
        return "glossary", "chapter"
    if "appendices" in fname:
        return "appendices", "chapter"

    chapter_match = re.search(r"chapter-(\d+)", fname)
    ch_num = chapter_match.group(1) if chapter_match else str(index)
    return f"chapter-{ch_num}", "chapter"



def extract_h1_title(md_text: str) -> str:
    """Extract the first H1 title from markdown text."""
    for line in md_text.split("\n"):
        line = line.strip()
        if line.startswith("# ") and not line.startswith("## "):
            return line.lstrip("# ").strip()
    return ""


def extract_chapter_number(title: str) -> str:
    """Extract chapter number from an H1 title like 'Chapter 2: Title' → '02'."""
    match = re.search(r'Chapter\s+(\d+)', title)
    if match:
        return match.group(1).zfill(2)
    return None


def strip_chapter_prefix(title: str) -> str:
    """Remove 'Chapter N:' prefix from title for cover page display.
    'Chapter 5: Analyzing Your Stakeholders' → 'Analyzing Your Stakeholders'"""
    return re.sub(r'^Chapter\s+\d+\s*[:\-—]+\s*', '', title).strip()


def build_chapter_cover(fname: str, md_content: str) -> str:
    """Generate a chapter cover page HTML div for the given file.
    Returns empty string if no cover page is needed (e.g., TOC)."""
    if "table-of-contents" in fname:
        return ""

    # No cover pages for About and Author — they use frontmatter-page style
    if any(k in fname for k in ["about", "author"]):
        return ""

    # Determine if this is a chapter file or front/back matter
    is_chapter = "chapter-" in fname or "introduction" in fname
    is_front_matter = False
    is_back_matter = any(k in fname for k in ["glossary", "appendices"])

    if not is_chapter and not is_front_matter and not is_back_matter:
        return ""

    title = extract_h1_title(md_content)

    if is_chapter:
        # Extract the display number from the H1 title (e.g., "Chapter 2:" → "02")
        display_num = extract_chapter_number(title)
        if not display_num:
            # Fallback to filename number
            ch_match = re.search(r'chapter-(\d+)', fname)
            display_num = ch_match.group(1).zfill(2) if ch_match else "00"

        # Strip "Chapter N:" prefix — the big number already conveys this
        cover_title = strip_chapter_prefix(title)

        return (
            f'<div class="chapter-cover-page">\n'
            f'  <div class="chapter-cover-number">{display_num}</div>\n'
            f'  <div class="chapter-cover-title">{cover_title}</div>\n'
            f'  <div class="chapter-cover-gold-line"></div>\n'
            f'</div>\n'
        )
    else:
        # Front/back matter — title only, no number
        cover_titles = {
            "about": "About This Guidebook",
            "author": "About the Author",
            "introduction": "Introduction",
            "glossary": "Glossary",
            "appendices": "Appendices",
        }
        cover_title = next((v for k, v in cover_titles.items() if k in fname), title)
        return (
            f'<div class="chapter-cover-page front-matter">\n'
            f'  <div class="chapter-cover-title">{cover_title}</div>\n'
            f'  <div class="chapter-cover-gold-line"></div>\n'
            f'</div>\n'
        )


def post_process_html(html: str) -> str:
    """Post-process the fully-converted HTML. Operates on HTML only, not markdown."""

    # Page break comments → CSS
    html = html.replace("<!-- PAGE BREAK -->", '<div style="page-break-before: always;"></div>')
    html = html.replace("&lt;!-- PAGE BREAK --&gt;", '<div style="page-break-before: always;"></div>')

    # Landscape markers
    html = html.replace("<!-- LANDSCAPE START -->", '<div class="landscape-page">')
    html = html.replace("<!-- LANDSCAPE END -->", '</div>')
    html = html.replace("&lt;!-- LANDSCAPE START --&gt;", '<div class="landscape-page">')
    html = html.replace("&lt;!-- LANDSCAPE END --&gt;", '</div>')

    # Checkboxes
    html = html.replace("[ ]", "&#9744;")
    html = html.replace("[x]", "&#9745;")
    html = html.replace("[X]", "&#9745;")

    # Form lines
    html = re.sub(r'\.{10,}', '<span class="form-line-wide"></span>', html)
    html = re.sub(r'\.{4,9}', '<span class="form-line"></span>', html)

    # Checklist tables
    html = re.sub(
        r'<table>\s*<thead>\s*<tr>\s*<th[^>]*>No\.</th>\s*<th[^>]*>Item</th>\s*<th[^>]*>Yes</th>\s*<th[^>]*>No</th>\s*<th[^>]*>N/A</th>',
        '<table class="checklist-table"><thead><tr><th>No.</th><th>Item</th><th>Yes</th><th>No</th><th>N/A</th>',
        html
    )

    # Anchor IDs on H1 headings for TOC linking
    def add_anchor_to_h1(match):
        content = match.group(1)
        anchor = re.sub(r'[^a-z0-9]+', '-', content.lower()).strip('-')
        return f'<h1 id="{anchor}">{content}</h1>'

    html = re.sub(r'<h1>(.*?)</h1>', add_anchor_to_h1, html)

    return html


def build_full_html(sections: list[tuple[str, str]]) -> str:
    """Build the complete HTML document. Every file goes through the markdown
    library — no custom regex parsing of markdown syntax."""

    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    all_sections_html = []
    back_link = '<div class="back-to-toc"><a href="#table-of-contents">Back to Table of Contents</a></div>'

    for i, (fname, md_content) in enumerate(sections):
        section_id, css_class = classify_section(fname, i)

        # Insert chapter cover page before each chapter/section
        cover_html = build_chapter_cover(fname, md_content)
        if cover_html:
            all_sections_html.append(cover_html)

        if css_class == "toc-section":
            # TOC needs structural layout (indented divs with CSS classes)
            html_content = build_toc_html(md_content)
            wrapped = f'<div class="{css_class}" id="{section_id}">\n{html_content}\n</div>\n'
        else:
            # All other files go through the markdown library
            html_content = convert_md_to_html(md_content)
            wrapped = f'<div class="{css_class}" id="{section_id}">\n{html_content}\n{back_link}\n</div>\n'

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
    print("  Strategic Planning Guidebook — PDF Generator")
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
    print("[2/4] Converting Markdown to HTML (via python-markdown library)...")
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
    # Auto-sync: copy PDF to _guidebook-pdf-copies/
    copies_dir = BASE_DIR.parent / '_guidebook-pdf-copies'
    if copies_dir.exists() and OUTPUT_PDF.exists():
        import shutil
        shutil.copy2(str(OUTPUT_PDF), str(copies_dir / OUTPUT_PDF.name))
        print(f'  Synced to: {copies_dir / OUTPUT_PDF.name}')
        # Also sync to iCloud
        icloud_dir = Path.home() / 'Library' / 'Mobile Documents' / 'com~apple~CloudDocs' / '_agentic-workflows' / '_guidebook-pdf-copies'
        if icloud_dir.exists():
            shutil.copy2(str(OUTPUT_PDF), str(icloud_dir / OUTPUT_PDF.name))
            print(f'  Synced to iCloud: {icloud_dir / OUTPUT_PDF.name}')

    else:
        print(f"\n  [FAIL] PDF generation failed.")
        print(f"  The intermediate HTML is available at:")
        print(f"  {OUTPUT_HTML}")
        print(f"  You can open it in a browser and print to PDF.")
        sys.exit(1)


if __name__ == "__main__":
    main()
