#!/usr/bin/env python3
"""Generate standalone PDF for the OBC Cross-Cutting Legal Reference."""

import os
import sys
import markdown
from pathlib import Path

sys.path.insert(0, os.path.expanduser("~/.claude/skills/pdf/venv/lib/python3.13/site-packages"))
from weasyprint import HTML

BASE_DIR = Path(__file__).parent
MD_FILE = BASE_DIR / "legal-reference-other-bangsamoro-communities.md"

CSS = """
@page {
    size: letter;
    margin: 0.9in 0.75in 1in 0.75in;
    @top-left {
        content: "OBC Cross-Cutting Legal Reference";
        font-family: 'Inter', 'Helvetica Neue', sans-serif;
        font-size: 7.5pt;
        color: #888;
    }
    @top-right {
        content: "Office for Other Bangsamoro Communities";
        font-family: 'Inter', 'Helvetica Neue', sans-serif;
        font-size: 7.5pt;
        color: #888;
    }
    @bottom-left {
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Inter', 'Helvetica Neue', sans-serif;
        font-size: 7.5pt;
        color: #888;
    }
    @bottom-right {
        content: "OOBC — Office of the Chief Minister, BARMM";
        font-family: 'Inter', 'Helvetica Neue', sans-serif;
        font-size: 7.5pt;
        color: #888;
    }
}
@page cover {
    margin: 0;
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-left { content: none; }
    @bottom-right { content: none; }
}
body {
    font-family: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.45;
    color: #1a1a1a;
}
.cover-page {
    page: cover;
    height: 100vh;
    width: 100vw;
    box-sizing: border-box;
    background: linear-gradient(135deg, #1B365D 0%, #2C5F7C 100%);
    padding: 2.5in 1.2in 1in 1.2in;
    color: white;
    display: flex;
    flex-direction: column;
}
.cover-page .accent {
    width: 60px; height: 4px; background: #C5A54E; margin-bottom: 8px;
}
.cover-page .accent2 {
    width: 40px; height: 4px; background: #C5A54E; margin-bottom: 8px;
}
.cover-page .accent3 {
    width: 20px; height: 4px; background: #C5A54E; margin-bottom: 24px;
}
.cover-page h1 {
    font-size: 26pt;
    font-weight: 700;
    line-height: 1.15;
    margin-bottom: 0.3em;
    color: white;
}
.cover-page .subtitle {
    font-size: 14pt;
    color: #C5A54E;
    font-weight: 600;
    margin-top: 0.3em;
}
.cover-page .bol-ref {
    font-size: 10pt;
    color: rgba(255,255,255,0.7);
    font-style: italic;
    margin-top: 1em;
    padding-top: 1em;
    border-top: 1pt solid rgba(197,165,78,0.3);
}
.cover-page .meta {
    margin-top: 1.5em;
    font-size: 10pt;
    color: rgba(255,255,255,0.65);
    line-height: 1.8;
}
.cover-page .meta strong {
    color: rgba(255,255,255,0.9);
}
.cover-page .institution {
    margin-top: auto;
    font-size: 9pt;
    font-weight: 600;
    color: #C5A54E;
    letter-spacing: 1.5pt;
    text-transform: uppercase;
    border-top: 2pt solid rgba(197,165,78,0.5);
    padding-top: 16pt;
}
.cover-page .sub-institution {
    font-size: 8pt;
    color: rgba(255,255,255,0.5);
    margin-top: 4pt;
    letter-spacing: 0.5pt;
}

/* Content */
h1 {
    font-size: 18pt;
    color: #1B365D;
    border-bottom: 2pt solid #C5A54E;
    padding-bottom: 6pt;
    margin-top: 24pt;
    margin-bottom: 16pt;
    page-break-after: avoid;
}
h2 {
    font-size: 14pt;
    color: #1B365D;
    margin-top: 20pt;
    margin-bottom: 8pt;
    border-bottom: 1pt solid #ddd;
    padding-bottom: 4pt;
    page-break-after: avoid;
}
h3 {
    font-size: 11.5pt;
    color: #2C5F7C;
    margin-top: 16pt;
    margin-bottom: 6pt;
    page-break-after: avoid;
}
h4 {
    font-size: 10.5pt;
    color: #333;
    margin-top: 12pt;
    margin-bottom: 4pt;
    page-break-after: avoid;
}
blockquote {
    border-left: 3pt solid #C5A54E;
    margin: 8pt 0;
    padding: 4pt 12pt;
    color: #333;
    background: #fafaf5;
    font-size: 9.5pt;
}
table {
    width: 100%;
    max-width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
    word-wrap: break-word;
    overflow-wrap: break-word;
    overflow: hidden;
    font-size: 8.5pt;
    margin: 8pt 0;
    page-break-inside: auto;
}
th {
    background: #1B365D;
    color: white;
    padding: 5pt 6pt;
    text-align: left;
    font-weight: 600;
    font-size: 8pt;
}
td {
    padding: 4pt 6pt;
    border-bottom: 0.5pt solid #ddd;
    vertical-align: top;
    overflow: hidden;
    word-wrap: break-word;
    overflow-wrap: break-word;
}
tr:nth-child(even) td { background: #f8f9fa; }
.footnotes {
    margin-top: 20pt;
    padding-top: 8pt;
    border-top: 1pt solid #ccc;
    font-size: 8pt;
    color: #555;
}
.footnotes ol { padding-left: 16pt; }
.footnotes li { margin-bottom: 2pt; }
p strong:first-child { color: #1B365D; }
em strong, strong em {
    color: #1a1a1a;
    font-style: italic;
    font-weight: 700;
}
"""

def main():
    print("Building OBC Legal Reference PDF...")

    with open(MD_FILE, "r") as f:
        md_content = f.read()

    body_html = markdown.markdown(
        md_content,
        extensions=["tables", "footnotes", "fenced_code", "attr_list"],
        output_format="html5",
    )

    cover = """
    <div class="cover-page">
        <div class="accent"></div>
        <div class="accent2"></div>
        <div class="accent3"></div>
        <h1>Other Bangsamoro Communities and Bangsamoro Governance</h1>
        <div class="subtitle">A Cross-Cutting Legal Reference</div>
        <div class="bol-ref">
            BOL Art. VI, Sec. 12 — "The Bangsamoro Government, in coordination with the local
            government units where these communities are located and the appropriate national
            government agencies, shall provide assistance to enhance their economic, social,
            and cultural development."
        </div>
        <div class="meta">
            <strong>Scope:</strong> All OBC provisions across the BOL, BAA 13, enacted BAAs, national laws, and the Constitution<br>
            <strong>Coverage:</strong> 55 enumerated powers mapped for OBC dimensions<br>
            <strong>Structure:</strong> Legal Framework — Legal Sources — Legal Briefer (9 themes) — 55-Power Matrix
        </div>
        <div class="institution">Office for Other Bangsamoro Communities</div>
        <div class="sub-institution">Office of the Chief Minister — Bangsamoro Autonomous Region in Muslim Mindanao</div>
    </div>
    """

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
{cover}
{body_html}
</body>
</html>"""

    html_path = BASE_DIR / "OBC-Legal-Reference.html"
    pdf_path = BASE_DIR / "OBC-Legal-Reference.pdf"

    with open(html_path, "w") as f:
        f.write(full_html)
    print(f"HTML saved: {html_path}")

    print("Generating PDF...")
    HTML(filename=str(html_path)).write_pdf(str(pdf_path))
    size_mb = pdf_path.stat().st_size / (1024 * 1024)
    print(f"PDF saved: {pdf_path} ({size_mb:.1f} MB)")

if __name__ == "__main__":
    main()
