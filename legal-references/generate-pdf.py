#!/usr/bin/env python3
"""Generate PDF from all completed legal reference markdown files."""

import os
import sys
import markdown
from pathlib import Path

# Add the PDF skill's venv
sys.path.insert(0, os.path.expanduser("~/.claude/skills/pdf/venv/lib/python3.13/site-packages"))
from weasyprint import HTML

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR

# Ordered list of completed power folders
POWERS = [
    "01-a-administration-of-justice",
    "02-b-administrative-organization",
    "03-c-agriculture",
    "04-d-ancestral-domain",
    "05-e-barter-trade",
    "06-f-budgeting",
    "07-g-business-name-registration",
    "08-h-cadastral-land-survey",
    "09-i-civil-service",
    "10-j-classification-of-public-lands",
    "11-k-cooperatives",
    "12-l-creation-of-municipalities",
    "13-m-creation-of-goccs",
    "14-n-creation-of-revenue-sources",
    "15-o-cultural-exchange",
    "16-p-culture-and-language",
    "17-q-customary-laws",
    "18-r-development-programs",
    "19-s-disaster-risk-reduction",
    "20-t-solid-waste",
    "21-u-economic-zones",
    "22-v-education",
    "23-w-eminent-domain",
    "24-x-environment-parks-forests",
    "25-y-fishery-marine",
    "26-z-grants-and-donations",
    "27-aa-hajj-and-umrah",
    "28-bb-health",
    "29-cc-housing",
    "30-dd-humanitarian-services",
    "31-ee-human-rights",
    "32-ff-indigenous-peoples-rights",
    "33-gg-inland-waters",
    "34-hh-inland-waterways",
    "35-ii-islamic-banking",
    "36-jj-labor-employment",
    "37-kk-libraries-museums",
    "38-ll-loans-credits",
    "39-mm-consultation-mechanisms",
    "40-nn-peoples-organizations",
    "41-oo-power-sector",
    "42-pp-public-utilities",
    "43-qq-public-works",
    "44-rr-quarantine",
    "45-ss-registration-births-marriages-deaths",
    "46-tt-regulation-of-food-drugs",
    "47-uu-science-and-technology",
    "48-vv-social-services",
    "49-ww-sports-and-recreation",
    "50-xx-technical-cooperation",
    "51-yy-tourism",
    "52-zz-trade-and-industry",
    "53-aaa-urban-rural-planning",
    "54-bbb-urban-land-reform",
    "55-ccc-water-supply",
]

POWER_LABELS = {
    "01-a": "(a) Administration of Justice",
    "02-b": "(b) Administrative Organization",
    "03-c": "(c) Agriculture, Livestock, and Food Security",
    "04-d": "(d) Ancestral Domain and Natural Resources",
    "05-e": "(e) Barter Trade and Countertrade",
    "06-f": "(f) Budgeting",
    "07-g": "(g) Business Name Registration",
    "08-h": "(h) Cadastral Land Survey",
    "09-i": "(i) Civil Service",
    "10-j": "(j) Classification of Public Lands",
    "11-k": "(k) Cooperatives and Social Entrepreneurship",
    "12-l": "(l) Creation of Municipalities and Barangays",
    "13-m": "(m) Creation of GOCCs and Pioneer Firms",
    "14-n": "(n) Creation of Revenue Sources",
    "15-o": "(o) Cultural Exchange and Economic Cooperation",
    "16-p": "(p) Culture and Language",
    "17-q": "(q) Customary Laws",
    "18-r": "(r) Development Programs",
    "19-s": "(s) Disaster Risk Reduction and Management",
    "20-t": "(t) Ecological Solid Waste Management",
    "21-u": "(u) Economic Zones, Industrial Centers, and Free Ports",
    "22-v": "(v) Education",
    "23-w": "(w) Eminent Domain",
    "24-x": "(x) Environment, Parks, and Forests",
    "25-y": "(y) Fishery, Marine, and Aquatic Resources",
    "26-z": "(z) Grants and Donations",
    "27-aa": "(aa) Hajj and Umrah",
    "28-bb": "(bb) Health",
    "29-cc": "(cc) Housing and Human Settlements",
    "30-dd": "(dd) Humanitarian Services and Institutions",
    "31-ee": "(ee) Human Rights",
    "32-ff": "(ff) Indigenous Peoples' Rights",
    "33-gg": "(gg) Inland Waters",
    "34-hh": "(hh) Inland Waterways for Navigation",
    "35-ii": "(ii) Islamic Banking and Finance",
    "36-jj": "(jj) Labor and Employment",
    "37-kk": "(kk) Libraries, Museums, and Similar Institutions",
    "38-ll": "(ll) Loans, Credits, and Other Forms of Indebtedness",
    "39-mm": "(mm) Mechanisms for Consultations",
    "40-nn": "(nn) People's Organizations",
    "41-oo": "(oo) Power Generation and Electrical Industry",
    "42-pp": "(pp) Public Utilities",
    "43-qq": "(qq) Public Works",
    "44-rr": "(rr) Quarantine Regulations",
    "45-ss": "(ss) Registration of Births, Marriages, and Deaths",
    "46-tt": "(tt) Regulation of Food, Drinks, Drugs, and Tobacco",
    "47-uu": "(uu) Science and Technology",
    "48-vv": "(vv) Social Services",
    "49-ww": "(ww) Sports and Recreation",
    "50-xx": "(xx) Technical Cooperation",
    "51-yy": "(yy) Tourism Development",
    "52-zz": "(zz) Trade and Industry",
    "53-aaa": "(aaa) Urban and Rural Planning",
    "54-bbb": "(bbb) Urban Land Reform and Land Use",
    "55-ccc": "(ccc) Water Supply",
}

CSS = """
@page {
    size: letter;
    margin: 0.9in 0.75in 1in 0.75in;
    @top-left {
        content: string(power-name);
        font-family: 'Inter', 'Helvetica Neue', sans-serif;
        font-size: 7.5pt;
        color: #888;
    }
    @top-right {
        content: "Legal Reference on the Powers of the Bangsamoro Government";
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
        content: element(footer-toc-link);
    }
}
@page cover {
    margin: 0;
    background: linear-gradient(135deg, #1B365D 0%, #2C5F7C 100%);
    @top-center { content: none; }
    @bottom-left { content: none; }
    @bottom-right { content: none; }
}
@page toc {
    @top-center { content: none; }
    @bottom-right { content: none; }
}
body {
    font-family: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.45;
    color: #1a1a1a;
}
.cover { page: cover; }
.cover-page {
    height: 100vh;
    width: 100vw;
    padding: 3.5in 1in 1in 1in;
    color: white;
    box-sizing: border-box;
}
.cover-top-accent {
    margin-bottom: 1.5em;
}
.cover-page h1 {
    font-size: 28pt;
    font-weight: 700;
    line-height: 1.15;
    margin-bottom: 0.4em;
    color: white;
}
.cover-page .subtitle {
    font-size: 15pt;
    color: #C5A54E;
    font-weight: 600;
    margin-top: 0.3em;
}
.cover-page .volume {
    font-size: 11pt;
    color: rgba(255,255,255,0.7);
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
    font-size: 10pt;
    font-weight: 600;
    color: #C5A54E;
    letter-spacing: 1.5pt;
    text-transform: uppercase;
    border-top: 2pt solid rgba(197,165,78,0.5);
    padding-top: 16pt;
}
.cover-bottom-detail {
    margin-top: 12pt;
    font-size: 8pt;
    color: rgba(255,255,255,0.4);
    letter-spacing: 0.5pt;
}
.toc-page { page: toc; page-break-before: always; }
.toc-page h2 {
    font-size: 18pt;
    color: #1B365D;
    border-bottom: 2pt solid #C5A54E;
    padding-bottom: 6pt;
    margin-bottom: 16pt;
}
.toc-page .toc-item {
    display: flex;
    justify-content: space-between;
    padding: 4pt 0;
    border-bottom: 0.5pt dotted #ccc;
    font-size: 9.5pt;
}
.toc-page .toc-item .toc-label { color: #1a1a1a; }
.toc-page .toc-item .toc-num { color: #1B365D; font-weight: 600; }
.toc-page .toc-link {
    display: flex;
    justify-content: space-between;
    text-decoration: none;
    color: inherit;
    width: 100%;
}
.toc-page .toc-link:hover { color: #2C5F7C; }
.back-to-toc { display: none; }
.footer-toc-link {
    position: running(footer-toc-link);
}
.footer-toc-link a {
    font-family: 'Inter', 'Helvetica Neue', sans-serif;
    font-size: 7.5pt;
    color: #1B365D;
    text-decoration: none;
}
.toc-note {
    margin-top: 20pt;
    padding: 12pt 16pt;
    background: #f0f4f8;
    border-left: 3pt solid #1B365D;
    font-size: 9pt;
    color: #444;
}

/* Chapter cover page */
@page chapter-cover {
    margin: 0;
    background: #1B365D;
    @top-center { content: none; }
    @bottom-left { content: none; }
    @bottom-right { content: none; }
}
.chapter-cover {
    page: chapter-cover;
    page-break-before: always;
    height: 100vh;
    width: 100vw;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 2in 1.2in;
    color: white;
}
.chapter-cover .power-letter {
    font-size: 48pt;
    font-weight: 700;
    color: #C5A54E;
    margin-bottom: 8pt;
    line-height: 1;
}
.chapter-cover .power-title {
    font-size: 22pt;
    font-weight: 700;
    color: white;
    line-height: 1.25;
    border-bottom: 3pt solid #C5A54E;
    padding-bottom: 12pt;
    margin-bottom: 16pt;
    string-set: power-name content();
}
.chapter-cover .power-bol {
    font-size: 10pt;
    color: rgba(255,255,255,0.7);
    font-style: italic;
    margin-bottom: 24pt;
}
.chapter-cover .power-meta {
    font-size: 9pt;
    color: rgba(255,255,255,0.6);
    line-height: 1.6;
}
.chapter-cover .power-meta strong {
    color: rgba(255,255,255,0.85);
}

/* Chapter content styling */
.chapter { page-break-before: always; }
.chapter h1 {
    font-size: 18pt;
    color: #1B365D;
    border-bottom: 2pt solid #C5A54E;
    padding-bottom: 6pt;
    margin-top: 0;
    margin-bottom: 16pt;
}
.chapter h2 {
    font-size: 14pt;
    color: #1B365D;
    margin-top: 20pt;
    margin-bottom: 8pt;
    border-bottom: 1pt solid #ddd;
    padding-bottom: 4pt;
}
.chapter h3 {
    font-size: 11.5pt;
    color: #2C5F7C;
    margin-top: 16pt;
    margin-bottom: 6pt;
}
.chapter h4 {
    font-size: 10.5pt;
    color: #333;
    margin-top: 12pt;
    margin-bottom: 4pt;
}
blockquote {
    border-left: 3pt solid #C5A54E;
    margin: 8pt 0;
    padding: 4pt 12pt;
    color: #333;
    background: #fafaf5;
    font-size: 9.5pt;
}

/* Tables */
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

/* Footnotes */
.footnotes {
    margin-top: 20pt;
    padding-top: 8pt;
    border-top: 1pt solid #ccc;
    font-size: 8pt;
    color: #555;
}
.footnotes ol { padding-left: 16pt; }
.footnotes li { margin-bottom: 2pt; }

/* Q&A styling */
p strong:first-child { color: #1B365D; }

/* Verbatim legal text */
em strong, strong em {
    color: #1a1a1a;
    font-style: italic;
    font-weight: 700;
}
"""

def build_toc_html():
    items = []
    for i, folder in enumerate(POWERS, 1):
        key = "-".join(folder.split("-")[:2])
        label = POWER_LABELS.get(key, folder)
        anchor = folder.replace("-", "")
        items.append(f'<div class="toc-item"><a href="#{anchor}" class="toc-link"><span class="toc-label">{label}</span><span class="toc-num">{i}</span></a></div>')
    # Add cross-cutting references at the end
    items.append('<div style="margin-top:12pt;border-top:1pt solid #C5A54E;padding-top:8pt;"></div>')
    items.append('<div class="toc-item" style="font-size:8pt;color:#888;padding-bottom:2pt;"><span>Cross-Cutting Legal References</span></div>')
    items.append('<div class="toc-item"><a href="#shariah-crosscut" class="toc-link"><span class="toc-label" style="font-weight:700;color:#1B365D;">Shari\'ah and Bangsamoro Governance</span><span class="toc-num"></span></a></div>')
    items.append('<div class="toc-item"><a href="#obc-crosscut" class="toc-link"><span class="toc-label" style="font-weight:700;color:#1B365D;">Other Bangsamoro Communities (OBC)</span><span class="toc-num"></span></a></div>')
    return "\n".join(items)

def convert_md_to_html(md_path):
    with open(md_path, "r") as f:
        md_content = f.read()
    return markdown.markdown(
        md_content,
        extensions=["tables", "footnotes", "fenced_code", "attr_list"],
        output_format="html5",
    )

def main():
    print("Building Legal Reference PDF...")

    # Cover page
    cover = f"""
    <div class="cover">
    <div class="cover-page">
        <div class="cover-top-accent">
            <div class="accent-line" style="width:60px;height:4px;background:#C5A54E;margin-bottom:8px;"></div>
            <div class="accent-line" style="width:40px;height:4px;background:#C5A54E;margin-bottom:8px;"></div>
            <div class="accent-line" style="width:20px;height:4px;background:#C5A54E;"></div>
        </div>
        <h1>Legal Reference on the Powers of the Bangsamoro Government</h1>
        <div class="subtitle">Under Republic Act No. 11054</div>
        <div class="subtitle" style="font-size:10pt;color:rgba(197,165,78,0.7);margin-top:4pt;line-height:1.4;">An Act Providing for the Organic Law for the Bangsamoro Autonomous Region in Muslim Mindanao</div>
    </div>
    </div>
    """

    # TOC
    toc = f"""
    <div class="toc-page" id="toc">
        <h2>Table of Contents</h2>
        {build_toc_html()}
        <div class="toc-note">
            <strong>Note:</strong> This is the complete edition, covering all 55 of the 55 powers
            enumerated under Art. V, Sec. 2 of the Bangsamoro Organic Law. This is the complete legal reference covering all 55 powers enumerated under Art. V, Sec. 2 of the Bangsamoro Organic Law. Each power is a self-contained legal reference
            with Legal Sources tables and a 9-theme Q&amp;A Legal Briefer following the analytical flow:
            BOL grant → constitutional floor → national law → implementation → Shari'ah dimension →
            divergence → gaps → development.
        </div>
    </div>
    """

    # Shari'ah cross-cutting reference (front-matter, after TOC)
    shariah_path = BASE_DIR / "00-shariah-cross-cutting" / "legal-reference-shariah-bangsamoro-governance.md"
    if shariah_path.exists():
        print("  [Shari'ah] Cross-cutting legal reference")
        shariah_cover = """
        <div class="chapter-cover" id="shariah-crosscut">
            <div class="power-letter" style="font-size:36pt;">Shari'ah</div>
            <div class="power-title">A Cross-Cutting Legal Reference</div>
            <div class="power-meta">
                <p><strong>Covers all 55 enumerated powers</strong> — BOL Shari'ah architecture, institutions, courts, Islamic finance, divergence analysis</p>
            </div>
        </div>
        """
        shariah_html = convert_md_to_html(shariah_path)
        shariah_crosscut = f'{shariah_cover}\n<div class="chapter">\n{shariah_html}\n</div>'
    else:
        shariah_crosscut = ""

    # OBC cross-cutting reference
    obc_path = BASE_DIR / "00-obc-other-bangsamoro-communities" / "legal-reference-other-bangsamoro-communities.md"
    if obc_path.exists():
        print("  [OBC] Cross-cutting legal reference")
        obc_cover = """
        <div class="chapter-cover" id="obc-crosscut">
            <div class="power-letter" style="font-size:36pt;">OBC</div>
            <div class="power-title">Other Bangsamoro Communities — A Cross-Cutting Legal Reference</div>
            <div class="power-bol">BOL Art. VI, Sec. 12 — Assistance to Other Bangsamoro Communities</div>
            <div class="power-meta">
                <p><strong>Covers all 55 enumerated powers</strong> — OBC rights framework, institutional structure (OOBC), national law landscape, implementation analysis</p>
                <p>Office for Other Bangsamoro Communities (OOBC) — Office of the Chief Minister</p>
            </div>
        </div>
        """
        obc_html = convert_md_to_html(obc_path)
        obc_crosscut = f'{obc_cover}\n<div class="chapter">\n{obc_html}\n</div>'
    else:
        obc_crosscut = ""

    # Convert all chapters
    chapters = []
    for i, folder in enumerate(POWERS, 1):
        folder_path = BASE_DIR / folder
        md_files = list(folder_path.glob("legal-reference-*.md"))
        if not md_files:
            print(f"  SKIP: {folder} (no legal-reference file)")
            continue
        md_path = md_files[0]
        print(f"  [{i:2d}/27] {folder}")

        key = "-".join(folder.split("-")[:2])
        label = POWER_LABELS.get(key, folder)
        # Extract the letter portion, e.g. "(a)" or "(aa)"
        letter_part = label.split(")")[0] + ")" if ")" in label else key.split("-")[1]
        title_part = label.split(") ", 1)[1] if ") " in label else label

        anchor = folder.replace("-", "")

        # Chapter cover page
        chapter_cover = f"""
        <div class="chapter-cover" id="{anchor}">
            <div class="power-letter">{letter_part}</div>
            <div class="power-title">{title_part}</div>
            <div class="power-bol">BOL Art. V, Sec. 2{letter_part}</div>
            <div class="power-meta">
                <p><strong>Power {i} of 55</strong> — Enumerated under Republic Act No. 11054</p>
                <p>Legal Sources + 9-Theme Q&amp;A Legal Briefer</p>
            </div>
        </div>
        """

        # Back to TOC link
        back_link = '<div class="back-to-toc"><a href="#toc">Back to Table of Contents</a></div>'

        html_content = convert_md_to_html(md_path)
        chapters.append(f'{chapter_cover}\n<div class="chapter">\n{html_content}\n{back_link}\n</div>')

    # Assemble
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
<div class="footer-toc-link"><a href="#toc">Back to Table of Contents</a></div>
{cover}
{toc}
{"".join(chapters)}
{shariah_crosscut}
{obc_crosscut}
</body>
</html>"""

    html_path = OUTPUT_DIR / "Legal-Reference-Powers-of-the-Bangsamoro-Government.html"
    pdf_path = OUTPUT_DIR / "Legal-Reference-Powers-of-the-Bangsamoro-Government.pdf"

    with open(html_path, "w") as f:
        f.write(full_html)
    print(f"\nHTML saved: {html_path}")

    print("Generating PDF (this may take a minute)...")
    HTML(filename=str(html_path)).write_pdf(str(pdf_path))
    size_mb = pdf_path.stat().st_size / (1024 * 1024)
    print(f"PDF saved: {pdf_path} ({size_mb:.1f} MB)")

if __name__ == "__main__":
    main()
