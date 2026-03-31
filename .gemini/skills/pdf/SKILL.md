---
name: pdf
description: |
  Comprehensive PDF creation, editing, manipulation, and analysis skill focused on producing
  professional, beautifully designed PDF documents. Use when: (1) creating new PDF reports,
  proposals, letters, certificates, or any styled document, (2) merging or splitting PDFs,
  (3) adding watermarks, headers, or footers, (4) converting HTML/markdown to PDF,
  (5) filling PDF forms, (6) extracting text or tables from PDFs, (7) any task involving
  .pdf files. This skill should be used whenever the user mentions PDF, wants to generate
  a printable document, needs a polished report output, or wants to convert content to PDF
  format — even if they don't explicitly say "PDF." If the output should look like a
  professional printed document, use this skill.
argument-hint: "[file-path]"
allowed-tools: Read, Bash, Glob, Grep
---

# PDF Creation, Editing, and Analysis

## Overview

Create professional, beautifully designed PDF documents using an HTML+CSS-to-PDF workflow.
This approach gives you full control over typography, layout, colors, and page structure
using familiar web technologies — producing results that rival professional typesetting.

The primary engine is **WeasyPrint** (HTML/CSS to PDF), which supports CSS Paged Media
for headers, footers, page numbers, margins, and multi-column layouts. For programmatic
needs, **reportlab** is available. For manipulation (merge, split, rotate), use **pypdf**.

## Workflow Decision Tree

### Creating a New PDF Document
Use the **"HTML-to-PDF" workflow** below — this is the primary and recommended approach.
It produces the highest quality output with the most design control.

### Reading/Extracting Content from PDFs
Use **pdfplumber** for text and table extraction.

### Manipulating Existing PDFs (merge, split, rotate, watermark)
Use **pypdf** — see "PDF Manipulation" section.

### Filling PDF Forms
Use **pypdf** — see "Form Filling" section.

### Converting Other Formats to PDF
- **Markdown to PDF**: Convert md to HTML first, then use WeasyPrint
- **DOCX to PDF**: `soffice --headless --convert-to pdf document.docx`
- **Images to PDF**: Use reportlab or pypdf

---

## HTML-to-PDF Workflow (Primary)

This is the recommended approach for creating professional PDFs. You write styled HTML,
then WeasyPrint converts it to a pixel-perfect PDF with proper page breaks, headers,
footers, and print-quality typography.

### Why HTML-to-PDF?

CSS gives you precise control over everything that matters in a professional document:
page size, margins, fonts, colors, tables, headers/footers, page numbers, columns,
and decorative elements. WeasyPrint faithfully renders CSS Paged Media, which was
designed specifically for print layout.

### Step-by-Step

1. **Design the HTML document** with embedded CSS
2. **Run the creation script** to convert to PDF
3. **Review** the output and iterate

### Creating the HTML

Write a single HTML file with `<style>` containing your CSS. Structure the document
with semantic HTML (`<header>`, `<section>`, `<table>`, `<footer>`, etc.).

**Critical CSS patterns for PDF:**

```css
@page {
  size: letter;              /* or A4, legal, letter landscape */
  margin: 1in 0.75in;       /* top/bottom left/right */

  @top-center {
    content: "Document Title";
    font-family: 'Inter', sans-serif;
    font-size: 8pt;
    color: #666;
  }

  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
    font-family: 'Inter', sans-serif;
    font-size: 8pt;
    color: #666;
  }
}

/* First page often has different margins/no header */
@page :first {
  margin-top: 0;
  @top-center { content: none; }
}

body {
  font-family: 'Inter', sans-serif;
  font-size: 10pt;
  line-height: 1.4;
  color: #1a1a1a;
}
```

### Tables (MANDATORY)

**Every PDF must include these table rules.** Without them, tables overflow the page and columns get cut off.

```css
/* MANDATORY — prevents table overflow */
table {
  width: 100%;
  max-width: 100%;
  table-layout: fixed;       /* NEVER use 'auto' — causes page overflow */
  border-collapse: collapse;
  word-wrap: break-word;
  overflow-wrap: break-word;
  overflow: hidden;
  font-size: 9pt;
}

td, th {
  overflow: hidden;
  word-wrap: break-word;
  overflow-wrap: break-word;
  padding: 4px 6px;
}
```

**Never use `table-layout: auto`** — it lets cell content push columns beyond the printable area. With `fixed`, columns share width equally and content wraps.

### Diagrams (MANDATORY)

**Never use ASCII art or monospace code-block flowcharts in PDFs.** They look unprofessional.

Render all diagrams as images:
1. Write in Mermaid syntax (`.mmd` file)
2. Render: `npx -y @mermaid-js/mermaid-cli mmdc -i diagram.mmd -o diagram.png -t neutral -b transparent -w 1200`
3. Embed as `<img>` in the HTML

If Mermaid CLI is unavailable, use styled HTML/CSS divs or the `/designer` skill.

### Page Breaks

Control page flow precisely:

```css
/* Force page break before element */
.page-break { page-break-before: always; }

/* Prevent break inside element */
table, figure { page-break-inside: avoid; }

/* Keep heading with next content */
h1, h2, h3 { page-break-after: avoid; }
```

### Running the Conversion

```bash
cd "${GEMINI_SKILL_DIR}"
source venv/bin/activate
python scripts/create_pdf.py input.html output.pdf
```

Or use WeasyPrint directly in a Python script:

```python
from weasyprint import HTML
HTML('document.html').write_pdf('output.pdf')
```

### Font Loading

WeasyPrint can use system fonts or fonts loaded via CSS `@font-face`. For Google Fonts
or custom fonts, download the font files and reference them:

```css
@font-face {
  font-family: 'Inter';
  src: url('path/to/Inter-Regular.woff2') format('woff2');
  font-weight: 400;
}
@font-face {
  font-family: 'Inter';
  src: url('path/to/Inter-Bold.woff2') format('woff2');
  font-weight: 700;
}
```

If Inter is installed on the system, just use `font-family: 'Inter', sans-serif;`.

---

## Design Principles

Professional PDFs need intentional design. Before writing code, consider:

1. **Purpose**: Is this a report, proposal, letter, certificate, invoice?
2. **Audience**: Internal stakeholders, clients, government, public?
3. **Branding**: Any organizational colors, logos, or style guides?
4. **Content density**: Mostly text? Data-heavy with tables? Visual with images?

### Typography

Good typography makes documents look professional without effort:

- **Body text**: 10-11pt, 1.3-1.5 line height, dark gray (#1a1a1a or #333)
- **Headings**: Clear hierarchy — size, weight, and spacing differentiate levels
- **Font pairing**: One serif + one sans-serif, or a single versatile family (Inter works well alone)
- **Margins**: Generous margins (0.75-1.25in) make content breathable

### Color Usage

Restraint is key. A professional palette uses 2-3 colors:

- **Primary**: For headings, accent lines, key callouts
- **Secondary**: For borders, subtle backgrounds, secondary text
- **Body text**: Near-black (#1a1a1a), never pure black (#000)

See [references/design-guide.md](references/design-guide.md) for color palettes and layout templates.

---

## Document Templates

### Report / Proposal

```html
<!DOCTYPE html>
<html>
<head>
<style>
@page {
  size: letter;
  margin: 1in 0.75in 1in 0.75in;
  @bottom-center {
    content: counter(page);
    font-family: 'Inter', sans-serif;
    font-size: 8pt;
    color: #888;
  }
}
@page :first {
  @bottom-center { content: none; }
}
body {
  font-family: 'Inter', sans-serif;
  font-size: 10pt;
  line-height: 1.5;
  color: #1a1a1a;
}
.cover {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 2in 0;
}
.cover h1 {
  font-size: 28pt;
  font-weight: 700;
  color: #0f4c81;
  margin-bottom: 0.5em;
  border-bottom: 3pt solid #0f4c81;
  padding-bottom: 0.5em;
}
.cover .subtitle {
  font-size: 14pt;
  color: #555;
  margin-top: 0.5em;
}
.cover .meta {
  margin-top: 2em;
  font-size: 10pt;
  color: #666;
}
h2 {
  font-size: 16pt;
  color: #0f4c81;
  border-bottom: 1pt solid #ddd;
  padding-bottom: 4pt;
  margin-top: 1.5em;
}
h3 {
  font-size: 12pt;
  color: #333;
  margin-top: 1.2em;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1em 0;
  font-size: 9pt;
  page-break-inside: avoid;
}
th {
  background: #0f4c81;
  color: white;
  padding: 8pt 10pt;
  text-align: left;
  font-weight: 600;
}
td {
  padding: 6pt 10pt;
  border-bottom: 0.5pt solid #ddd;
}
tr:nth-child(even) td { background: #f8f9fa; }
.callout {
  background: #e8f4f8;
  border-left: 3pt solid #0f4c81;
  padding: 12pt 16pt;
  margin: 1em 0;
  font-size: 9.5pt;
}
</style>
</head>
<body>
  <div class="cover">
    <h1>Report Title</h1>
    <div class="subtitle">Subtitle or Description</div>
    <div class="meta">
      <p>Prepared by: Author Name</p>
      <p>Date: March 15, 2026</p>
      <p>Organization Name</p>
    </div>
  </div>

  <div class="page-break"></div>

  <h2>1. Executive Summary</h2>
  <p>Content here...</p>

  <h2>2. Findings</h2>
  <table>
    <thead><tr><th>Item</th><th>Value</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>Item 1</td><td>100</td><td>Complete</td></tr>
    </tbody>
  </table>

  <div class="callout">
    <strong>Key Finding:</strong> Important insight highlighted here.
  </div>
</body>
</html>
```

### Letter / Memo

```html
<style>
@page {
  size: letter;
  margin: 1in;
  @bottom-center {
    content: counter(page);
    font-size: 8pt;
    color: #999;
  }
}
body {
  font-family: 'Inter', sans-serif;
  font-size: 10pt;
  line-height: 1.5;
  color: #1a1a1a;
}
.letterhead {
  border-bottom: 2pt solid #2c5282;
  padding-bottom: 12pt;
  margin-bottom: 24pt;
}
.letterhead h1 {
  font-size: 16pt;
  color: #2c5282;
  margin: 0;
}
.letterhead .address {
  font-size: 8.5pt;
  color: #666;
  margin-top: 4pt;
}
.date { margin: 24pt 0 12pt; }
.recipient { margin-bottom: 24pt; }
.signature { margin-top: 48pt; }
</style>
```

### Invoice / Financial Document

```html
<style>
@page { size: letter; margin: 0.75in; }
body {
  font-family: 'Inter', sans-serif;
  font-size: 9.5pt;
  color: #1a1a1a;
}
.invoice-header {
  display: flex;
  justify-content: space-between;
  border-bottom: 2pt solid #1a1a1a;
  padding-bottom: 16pt;
  margin-bottom: 24pt;
}
.amount-due {
  font-size: 24pt;
  font-weight: 700;
  color: #0f4c81;
}
table.line-items {
  width: 100%;
  border-collapse: collapse;
}
table.line-items th {
  background: #f0f0f0;
  padding: 8pt;
  text-align: left;
  font-weight: 600;
  border-bottom: 1.5pt solid #333;
}
table.line-items td {
  padding: 8pt;
  border-bottom: 0.5pt solid #e0e0e0;
}
.totals td { font-weight: 600; border-top: 1.5pt solid #333; }
</style>
```

---

## Large Document Workflow (Parallel Agents)

For documents over 20 pages (workbooks, manuals, training packages), use this parallel
agent workflow to build the HTML in sections and assemble into a single PDF.

### Why Parallel Agents?

Large documents (50-120+ pages) have too much content for a single agent to write
reliably. Splitting into 4-6 parallel agents, each writing one section, is faster and
produces more complete output. Each agent writes a body-only HTML fragment; one
designated agent writes the full HTML wrapper with ALL CSS.

### Architecture

```
/tmp/{project}-sections/
  section-01-frontmatter.html   # Full <html> + <head> + ALL CSS + cover + front matter
  section-02-part-i.html         # Body-only HTML fragment
  section-03-part-ii.html        # Body-only HTML fragment
  section-04-part-iii.html       # Body-only HTML fragment
  section-05-rest.html           # Body-only HTML fragment
  assemble.py                    # Concatenation + WeasyPrint conversion
```

### Agent 1: CSS + Wrapper

Agent 1 writes the complete `<html>`, `<head>`, and `<style>` block containing ALL CSS
for the entire document — every class that any agent will use. It also writes the cover
page and front matter content. **It must NOT close the document** — no `</main>`,
`</body>`, or `</html>` at the end. The assembly script appends other sections and
closes all tags.

### Agents 2-N: Body-Only Fragments

Each remaining agent writes body-only HTML (no `<html>`, `<head>`, `<style>`, `<body>`
tags). They use the CSS classes defined by Agent 1. Each agent reads the source content
file for exact text and writes fresh semantic HTML.

### Assembly Script

```python
#!/usr/bin/env python3
import os
from weasyprint import HTML

SECTIONS_DIR = "/tmp/{project}-sections"
OUTPUT_DIR = "/path/to/output"

# Read section 01 (has HTML wrapper, left OPEN)
with open(os.path.join(SECTIONS_DIR, "section-01-frontmatter.html"), "r") as f:
    frontmatter = f.read()

# Read body-only sections 02-N
sections = []
for fname in sorted(os.listdir(SECTIONS_DIR)):
    if fname.startswith("section-0") and fname != "section-01-frontmatter.html":
        with open(os.path.join(SECTIONS_DIR, fname), "r") as f:
            sections.append(f.read())

# Assemble: append sections then close all tags
assembled = frontmatter + "\n\n" + "\n\n".join(sections) + "\n\n</main>\n</body>\n</html>"

html_path = os.path.join(OUTPUT_DIR, "output.html")
with open(html_path, "w") as f:
    f.write(assembled)

HTML(filename=html_path).write_pdf(os.path.join(OUTPUT_DIR, "output.pdf"))
```

### Design System Pattern

For professional large documents, define a complete design system in Agent 1's CSS:

**Color tokens** as CSS custom properties:
```css
:root {
  --navy: #1B4F72;    /* Primary: headings, dark backgrounds */
  --blue: #2E86C1;    /* Secondary: subheadings, accents */
  --teal: #17A589;    /* Accent: stripes, badges, highlights */
  --teal-light: #D1F2EB;  /* Light accent backgrounds */
  --body: #2C3E50;    /* Body text */
  --line: #BDC3C7;    /* Form lines, borders */
  --gray: #7F8C8D;    /* Footer text, meta */
}
```

**Component classes** — define ALL of these in Agent 1, even if that section doesn't use them:
- `.cover` — cover page (assign named `@page cover` for footer suppression)
- `.part-page` — full-page section dividers (dark background, geometric SVG decorations, assign named `@page divider`)
- `.sess-block` + `.sess-badge` + `.sess-title` — session/chapter headers
- `.spr` — sprint/module headers with numbered circle badge
- `.tmpl` — template/form headers with gradient stripe
- `.scor` — scoring/rubric sheet headers
- `.persona-card` — profile cards with colored header bar
- `.form-field` + `.form-label` + `.form-line` — fillable form fields with dotted lines
- `.wl` — writing/notes lines (dotted, 24pt height)
- `.check` + `.check-box` — checkbox items with colored check character
- `.pull-quote` — highlighted callout with colored background + left border
- `.note-box` — info/tip box with light background
- `.pb` — page break utility class

**Named pages** for footer suppression:
```css
@page cover { @bottom-left { content: none; } @bottom-right { content: none; } }
@page divider { @bottom-left { content: none; } @bottom-right { content: none; } }
.cover { page: cover; }
.part-page { page: divider; }
```

**WeasyPrint margin box gotcha:** `@bottom-left` and `@bottom-right` do NOT inherit
`font-family` from body. Always set `font-family` explicitly in margin box rules.

### Geometric Decorations

Use inline SVG for circles, dot grids, and accent shapes. WeasyPrint renders inline SVG
well. Parent containers must have `position: relative; overflow: hidden;` for
absolute-positioned decorative elements.

```html
<!-- Semi-transparent decorative circle -->
<svg style="position:absolute;bottom:-30pt;left:-30pt;" width="140" height="140">
  <circle cx="70" cy="70" r="60" fill="#2E86C1" opacity="0.12"/>
</svg>

<!-- Dot grid pattern -->
<svg style="position:absolute;top:40pt;right:80pt;" width="48" height="36">
  <circle cx="4" cy="4" r="2.5" fill="rgba(255,255,255,0.15)"/>
  <circle cx="16" cy="4" r="2.5" fill="rgba(255,255,255,0.15)"/>
  <!-- ... repeat -->
</svg>

<!-- Accent stripes (CSS divs) -->
<div style="position:absolute;top:20pt;right:24pt;">
  <div style="width:40px;height:4px;background:#17A589;margin-bottom:6px;"></div>
  <div style="width:25px;height:4px;background:#17A589;margin-bottom:6px;"></div>
  <div style="width:15px;height:4px;background:#17A589;"></div>
</div>
```

### WeasyPrint Limitations (Important)

Do NOT use these in HTML for WeasyPrint:
- `clip-path` — not supported
- `transform` — limited support (no 3D, unreliable rotation)
- CSS Grid — partially supported, unreliable; use flexbox or floats
- `position: fixed` — not supported in paged media
- JavaScript — not executed at all
- `@page:first` for footer suppression — unreliable; use named pages instead

DO use:
- Inline SVG — renders perfectly
- CSS variables (`var()`) — fully supported, including in gradients
- Flexbox — well supported
- `border-radius` — works
- CSS gradients — work in backgrounds
- `@font-face` with local paths — works with `.ttf`, `.woff2`
- Named `@page` rules — reliable for per-section page formatting

### Checklist for Large Document Agents

Before launching parallel agents, verify:

1. [ ] Agent 1 defines ALL CSS classes (not just what it uses)
2. [ ] Agent 1 leaves document OPEN (no closing tags)
3. [ ] All agents use the same class names (shared design system)
4. [ ] Content source file path is given to each agent
5. [ ] Each agent told to READ source for content, write fresh HTML (not convert markdown)
6. [ ] Accuracy-critical content (legal citations, numbers) flagged per-agent
7. [ ] Assembly script appends sections then closes `</main></body></html>`
8. [ ] WeasyPrint venv path specified: `cd ~/.gemini/skills/pdf && source venv/bin/activate`

---

## PDF Manipulation (pypdf)

For working with existing PDF files — merging, splitting, rotating, watermarking.

### Merge PDFs

```python
from pypdf import PdfWriter

writer = PdfWriter()
for pdf_path in ['part1.pdf', 'part2.pdf', 'part3.pdf']:
    writer.append(pdf_path)
writer.write('merged.pdf')
writer.close()
```

### Split PDF

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader('document.pdf')
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    writer.write(f'page_{i+1}.pdf')
    writer.close()
```

### Extract Page Range

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader('document.pdf')
writer = PdfWriter()
for page_num in range(2, 6):  # pages 3-6 (0-indexed)
    writer.add_page(reader.pages[page_num])
writer.write('extract.pdf')
writer.close()
```

### Rotate Pages

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader('document.pdf')
writer = PdfWriter()
for page in reader.pages:
    page.rotate(90)  # 90, 180, 270
    writer.add_page(page)
writer.write('rotated.pdf')
writer.close()
```

### Add Watermark

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader('document.pdf')
watermark = PdfReader('watermark.pdf').pages[0]

writer = PdfWriter()
for page in reader.pages:
    page.merge_page(watermark)
    writer.add_page(page)
writer.write('watermarked.pdf')
writer.close()
```

### Encrypt / Password Protect

```python
from pypdf import PdfWriter

writer = PdfWriter('document.pdf')
writer.encrypt('user_password', 'owner_password')
writer.write('protected.pdf')
writer.close()
```

---

## Reading and Extracting from PDFs

### Text Extraction (pdfplumber)

```python
import pdfplumber

with pdfplumber.open('document.pdf') as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)
```

### Table Extraction

```python
import pdfplumber

with pdfplumber.open('document.pdf') as pdf:
    page = pdf.pages[0]
    tables = page.extract_tables()
    for table in tables:
        for row in table:
            print(row)
```

### Extract to DataFrame

```python
import pdfplumber
import pandas as pd

with pdfplumber.open('report.pdf') as pdf:
    table = pdf.pages[0].extract_table()
    df = pd.DataFrame(table[1:], columns=table[0])
```

---

## Form Filling

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader('form.pdf')
writer = PdfWriter()
writer.append(reader)

# Get form field names
fields = reader.get_fields()
for name, field in fields.items():
    print(f"{name}: {field.get('/V', 'empty')}")

# Fill fields
writer.update_page_form_field_values(
    writer.pages[0],
    {
        'field_name': 'Field Value',
        'date_field': '2026-03-15',
    }
)
writer.write('filled_form.pdf')
writer.close()
```

---

## Markdown to PDF

Convert markdown to PDF via an intermediate HTML step:

```bash
# Convert markdown to HTML
pandoc document.md -o document.html --standalone

# Then convert HTML to PDF
cd "${GEMINI_SKILL_DIR}"
source venv/bin/activate
python scripts/create_pdf.py document.html output.pdf
```

Or in Python with custom styling:

```python
import markdown
from weasyprint import HTML

# Read markdown
with open('document.md') as f:
    md_content = f.read()

# Convert to HTML with styling
html_content = f"""<!DOCTYPE html>
<html>
<head><style>
@page {{ size: letter; margin: 1in; }}
body {{ font-family: 'Inter', sans-serif; font-size: 10pt; line-height: 1.5; color: #1a1a1a; }}
h1 {{ font-size: 20pt; color: #0f4c81; }}
h2 {{ font-size: 14pt; color: #0f4c81; border-bottom: 0.5pt solid #ddd; padding-bottom: 4pt; }}
table {{ width: 100%; border-collapse: collapse; }}
th {{ background: #f0f4f8; padding: 6pt 8pt; text-align: left; }}
td {{ padding: 6pt 8pt; border-bottom: 0.5pt solid #eee; }}
code {{ background: #f5f5f5; padding: 1pt 4pt; font-size: 9pt; border-radius: 2pt; }}
pre {{ background: #f5f5f5; padding: 12pt; font-size: 8.5pt; overflow-x: auto; }}
blockquote {{ border-left: 3pt solid #0f4c81; margin-left: 0; padding-left: 16pt; color: #555; }}
</style></head>
<body>{markdown.markdown(md_content, extensions=['tables', 'fenced_code'])}</body>
</html>"""

HTML(string=html_content).write_pdf('output.pdf')
```

---

## Advanced: reportlab (Programmatic PDFs)

For highly programmatic PDFs (generated charts, dynamic layouts, pixel-precise positioning):

```python
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

doc = SimpleDocTemplate('output.pdf', pagesize=letter,
    topMargin=1*inch, bottomMargin=1*inch,
    leftMargin=0.75*inch, rightMargin=0.75*inch)

styles = getSampleStyleSheet()
story = []

# Title
title_style = ParagraphStyle('CustomTitle',
    parent=styles['Heading1'], fontSize=24, textColor=colors.HexColor('#0f4c81'))
story.append(Paragraph('Report Title', title_style))
story.append(Spacer(1, 24))

# Body
story.append(Paragraph('Body text here...', styles['BodyText']))

# Table
data = [['Item', 'Qty', 'Price'], ['Widget A', '10', '$50'], ['Widget B', '5', '$30']]
table = Table(data, colWidths=[3*inch, 1.5*inch, 1.5*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0f4c81')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#ddd')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')]),
]))
story.append(table)

doc.build(story)
```

Read [references/reportlab.md](references/reportlab.md) for advanced reportlab patterns.

---

## Setup

```bash
# Create venv and install dependencies
cd "${GEMINI_SKILL_DIR}"
python3 -m venv venv
source venv/bin/activate
pip install weasyprint pdfplumber pypdf reportlab markdown pandas

# System dependencies (macOS)
brew install pango cairo libffi weasyprint

# For markdown conversion
brew install pandoc

# For DOCX-to-PDF conversion
brew install libreoffice
```

---

## References

| Reference | Content |
|-----------|---------|
| [design-guide.md](references/design-guide.md) | Color palettes, typography, layout templates for professional PDFs |
| [weasyprint.md](references/weasyprint.md) | WeasyPrint CSS Paged Media reference, advanced features |

## Code Style

- Write concise code
- Avoid verbose variable names and redundant operations
- Avoid unnecessary print statements
- Prefer the HTML-to-PDF workflow for any document that needs to look polished
