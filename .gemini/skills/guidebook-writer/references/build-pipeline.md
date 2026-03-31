# Build Pipeline — Adapting PDF and DOCX Generation

Each guidebook needs its own `generate-pdf.py` and `generate-docx.py` scripts, adapted from the bill-drafting template. This reference documents what to customize.

---

## Source Template

The proven scripts are at:
```
guidebooks/mop-formulation/generate-pdf.py   (canonical — cover page fixed)
guidebooks/mop-formulation/generate-docx.py  (canonical — cover page fixed)
guidebooks/mop-formulation/guidebook-template.html  (canonical — cover page fixed)
```

Copy all three into the new guidebook directory, then customize. Do NOT use older templates (bill-drafting ver02) — they may have the duplicate BARMM cover page bug. These templates include chapter cover pages, section page breaks, and footnote rendering standards documented below.

---

## What to Customize in generate-pdf.py

### 1. Configuration Block (lines 20-45)

```python
# CHANGE THESE:
OUTPUT_PDF = BASE_DIR / "{Guidebook-Title}.pdf"
OUTPUT_HTML = BASE_DIR / "guidebook-rendered.html"

# UPDATE THIS LIST to match the new guidebook's markdown files:
MD_FILES = [
    "00-table-of-contents.md",
    "00b-about.md",
    "00c-author.md",
    "01-introduction.md",
    "02-chapter-01.md",
    # ... add all chapter files in order
    "{N}-glossary.md",
]
```

### 2. No Other Changes Needed

The markdown processing, HTML conversion, TOC building, post-processing, and PDF rendering are all generic. They work with any markdown content that follows the heading/formatting conventions.

---

## What to Customize in generate-docx.py

### 1. Configuration (lines 26-55)

```python
OUTPUT_FILE = SCRIPT_DIR / "{Guidebook-Title}.docx"

SOURCE_FILES = [
    # Same ordered list as generate-pdf.py
]
```

### 2. Title Page (create_title_page function)

Update:
- Main title text (e.g., "POLICY RECOMMENDATIONS GUIDEBOOK")
- Subtitle text (e.g., "A Practical Guide for MOA Policy Units and Parliament Committee Staff")
- Institution name (e.g., "Ministry of the Interior and Local Government — BARMM")
- Location line

### 3. Running Header/Footer (add_header_footer function)

Update:
- Header text: `"{Guidebook Title} — {Institution}"`
- Author name in footer if needed

---

## What to Customize in guidebook-template.html

### 1. Title and Metadata

```html
<title>{Guidebook Title}</title>
```

### 2. Cover Page Content

Update the cover page section (near line 600+):
- Main title
- Subtitle
- Author name
- Institution (bottom block only)
- Location

**CRITICAL — No duplicate BARMM text:** The cover page must NOT have "Bangsamoro Autonomous Region in Muslim Mindanao" at both the top and bottom. It appears ONLY in the bottom block. The correct pattern is:

```
Title (large, navy, white text) → Gold separator line → Subtitle (slate, italic)
→ Author name → Bottom block: "Bangsamoro Government" / "BARMM" / "Cotabato City"
```

Do NOT add a `.cover-institution-top` div or a gold "BANGSAMORO AUTONOMOUS REGION..." line above the title. This was a recurring error fixed multiple times. Reference `guidebooks/mop-formulation/guidebook-template.html` as the canonical template.

Similarly in `generate-docx.py`, the `create_title_page()` function must NOT have a gold institution line before the title. Start with spacing, then the title directly.

### 3. Color Scheme (Optional)

The default BARMM institutional palette:
```css
Navy:   #1B365D  (headings, cover background)
Gold:   #C5A54E  (accents, separators)
Slate:  #2C5F7C  (H3/H4, secondary text)
Body:   #2D2D2D  (paragraph text)
```

If a specific MOA has its own branding, adjust these CSS variables. Most MOAs use the standard BARMM palette.

### 4. Running Footer

```css
@bottom-left {
    content: "{Guidebook Title} — {Institution}\A {Author Name}";
}
```

---

## Dependencies

```bash
pip3 install markdown weasyprint python-docx
```

- **markdown**: Markdown to HTML conversion with extensions
- **weasyprint**: HTML to PDF rendering (primary)
- **python-docx**: Direct DOCX generation
- **playwright** (optional fallback): `npx playwright install chromium` for PDF if WeasyPrint fails

---

## Generation Workflow

```bash
# 1. Generate PDF
python3 generate-pdf.py
# Outputs: {Guidebook-Title}.pdf + guidebook-rendered.html (debug)

# 2. Generate DOCX
python3 generate-docx.py
# Outputs: {Guidebook-Title}.docx
```

Both scripts:
1. Read markdown files in order from MD_FILES/SOURCE_FILES list
2. Convert to target format with professional styling
3. Report file size on completion

---

## Visual QA Loop (REQUIRED)

After generating the PDF, you MUST run the Visual QA Loop before declaring the guidebook complete. This catches rendering problems that are invisible in markdown but obvious in the PDF.

### The Loop

```
REPEAT (max 5 iterations per problem):
  1. SCREENSHOT — Convert PDF pages with diagrams/tables to images
     pdftoppm -png -r 150 -f {page} -l {page} output.pdf /tmp/page
     Then READ the image to visually inspect it.

  2. INSPECT — Check each screenshot against this checklist:
     [ ] Diagrams render horizontally (not tall vertical stacks)
     [ ] Diagrams use BARMM palette (Navy #1B365D, Gold #C5A54E, Slate #2C5F7C)
     [ ] No ASCII art in the PDF (no +---, |, ┌, └, ═, ━ characters)
     [ ] No literal markdown artifacts (*bold*, _italic_, ** visible as text)
     [ ] Tables fit within page margins (no columns cut off on the right)
     [ ] Tables with 5+ columns use smaller font (8-9pt) or landscape
     [ ] Mermaid diagrams are compact (not taking up a full page each)
     [ ] Images are present (no broken image placeholders)
     [ ] Cover page has no duplicate BARMM text

  3. FIX — For each problem found:
     - Diagram too tall → rewrite .mmd as flowchart LR, re-render PNG
     - ASCII art surviving → replace with Mermaid diagram or styled HTML table
     - Table overflow → add table-layout:fixed or split table
     - Markdown artifacts → fix the generate-pdf.py conversion
     - Wrong colors → update .mmd theme variables

  4. RE-RENDER — Regenerate the PNG and/or PDF
  5. RE-INSPECT — Screenshot the fixed page and verify
```

### Which Pages to Check

After PDF generation, identify pages containing:
- Any `<img>` tag (Mermaid diagrams, embedded images)
- Any `<table>` with 5+ columns
- The cover page (page 1)
- The table of contents (page 2-3)

### Mermaid Rendering Standards (simple diagrams)

- **Render command**: `npx -y -p @mermaid-js/mermaid-cli mmdc --input file.mmd --output file.png --scale 2`
- **Orientation**: Use `flowchart LR` for process flows; `flowchart TB` only for hierarchies
- **Colors**: Always use BARMM palette in `%%{init}%%` block
- **Output**: PNG at 2x scale for crisp rendering in PDF
- **Fan-out patterns**: Mermaid renders these vertically regardless of LR direction — restructure as linear chains

### Excalidraw Rendering Standards (complex diagrams)

For diagrams that hit Mermaid limitations (fan-out, mind maps, swimlanes, multi-color), use `/excalidraw`:

- **Render command**: `~/.gemini/skills/excalidraw/scripts/venv/bin/python3 ~/.gemini/skills/excalidraw/scripts/render_excalidraw.py input.excalidraw -o output.png`
- **Color palette**: BARMM palette at `~/.gemini/skills/excalidraw/references/color-palette.md`
- **Roughness**: `0` for government documents, `1` for training materials
- **Output**: Both `.excalidraw` (editable) and `.png` (embeddable) — embed PNG in markdown like Mermaid
- **Self-validation**: Render PNG, visually inspect, fix JSON, re-render (same Visual QA Loop)

### Visualize Standards (infographics and dashboards)

For infographics, dashboards, and visual summaries, use `/visualize` to generate HTML → convert to PNG via Playwright (`npx playwright screenshot`) or WeasyPrint → embed in guidebook.

- **Use cases**: chapter-level infographics, one-page visual summaries, process dashboards, data stories, visual policy briefs
- **Output**: self-contained HTML file → convert to PNG for embedding in markdown and PDF
- **Playwright**: `npx playwright screenshot --full-page visualization.html visualization.png`
- **WeasyPrint**: use the existing WeasyPrint pipeline if the HTML conforms to guidebook CSS standards

### Footnote Standards (MANDATORY)

Footnotes must render on a **separate page** with a "Footnotes" heading, NOT inline at the end of the chapter text. This requires:
- `page-break-before: always` on the `.footnote` container
- A `::before` pseudo-element with `content: "Footnotes"` styled as a heading
- The `footnotes` extension must be in the MD_EXTENSIONS list in `generate-pdf.py`
- Footnote reference numbers must be superscript navy (`#1B365D`)
- This applies to ALL guidebooks — update every `guidebook-template.html` accordingly

### Chapter Cover Page Standards (MANDATORY)

Every chapter in a guidebook gets a **dedicated cover page** before its content begins. This is a professional publishing standard inspired by the 2nd Bangsamoro Development Plan format.

**Numbered chapters** (the main content chapters):
- Full-page cover with large chapter number (96pt, navy `#1B365D`, bold 800-weight)
- Chapter title below the number (28pt, dark `#2D2D2D`, 600-weight) — **strip the "Chapter N:" prefix** since the number already conveys this
- Gold accent line below the title
- Gold bar at top of page, navy gradient at bottom
- No header/footer on cover pages (`@page chapter-cover` rule)

**Front/back matter** (About, Author, Introduction, Glossary, Appendices):
- Full-page cover with title only (32pt, navy, no number)
- Same gold bar and navy gradient decoration

**Implementation in `generate-pdf.py`:**
- `extract_chapter_number()` — pulls the number from the H1 title ("Chapter 5: ..." → "05")
- `strip_chapter_prefix()` — removes "Chapter N: " from the title for cover display
- `build_chapter_cover()` — generates the cover page HTML, inserted before each chapter div in `build_full_html()`
- TOC gets no cover page

**Implementation in `guidebook-template.html`:**
- `@page chapter-cover` — suppresses header/footer
- `.chapter-cover-page` — full A4 page with flexbox centering
- `.chapter-cover-page.front-matter` — hides the number, uses larger title

### Heading Visual Hierarchy Standards (MANDATORY)

Headings use a three-tier visual system to create clear structure without separate cover pages for sections:

**H2 (Major sections: 2.1, 2.2, 2.3):**
```css
h2 {
  color: #FFFFFF;
  background: linear-gradient(135deg, #1B365D 0%, #243F6B 100%);
  padding: 3.5mm 5mm;
  border-radius: 2pt;
}
```
Navy background band with white text — makes sections stand out as major visual boundaries.

**H3 (Sub-sections: Step 1, Key Concepts):**
```css
h3 {
  color: #1B365D;
  padding-left: 4mm;
  border-left: 4pt solid #C5A54E;
}
```
Gold left border bar — marks sub-sections clearly without background color.

**H4 (Sub-items: Tier headings, worked example sub-headings):**
```css
h4 {
  color: #2C5F7C;
  padding-left: 3mm;
  border-left: 2pt solid #2C5F7C;
}
```
Slate left border — subtle but visible marker for the deepest heading level.

This applies to ALL guidebooks. The visual hierarchy lets readers scan quickly without needing separate pages for every section.

### Section Page Break Standards (MANDATORY)

Every H2 section (`##`) must start on a new page. This prevents orphaned section headers at the bottom of a page with content continuing on the next.

**CSS rule:**
```css
h2 {
  page-break-before: always;
}
```

This applies to ALL guidebooks. Combined with chapter cover pages, it ensures clean visual separation at every structural level of the document.

### Inline Guide Questions Standards (MANDATORY)

Every guidebook chapter must include **granular inline guide questions** placed immediately after the specific paragraph or instruction they relate to. These are italic blockquotes that prompt the practitioner to pause, reflect, and check their work before continuing.

**Format:**
```markdown
[Instructional paragraph about identifying your MOA's creating law]

> *What is the specific BAA or BOL provision that creates your MOA? Not what inspires it — what establishes it as an institution.*

[Next instructional paragraph]
```

**Placement rules:**
- Questions appear **right after** the relevant instruction — not bunched at the top of a step
- Each question is contextually anchored — the reader should not need to remember questions from earlier pages
- Creates a "check-in rhythm" — read instruction, pause, ask yourself, continue
- Aim for **8-15 guide questions per chapter**, distributed across Key Concepts and Step-by-Step Instructions
- **Do NOT place** guide questions in worked examples (Section X.4), templates, quality checklists, or common pitfalls — these sections demonstrate or evaluate, not instruct

**Quality criteria for guide questions:**
- **Specific to BARMM context** — reference real institutions (BPDA, MFBM, BTA committees, OCM), legal instruments (BDP goals, BAA citations, BOL provisions), and real planning scenarios
- **Actionable** — the practitioner can answer the question using materials at hand
- **Challenging** — questions should surface blind spots, not confirm what the reader already knows
- **One concept per question** — do not combine multiple checks into a single question

**Anti-patterns:**
- Generic questions: "Have you thought about this?" — too vague
- Yes/no questions without consequence: "Did you complete this step?" — not useful
- Questions that repeat the instruction: "Did you identify your creating law?" — just restates what was said

**Good examples:**
- "Have you read the full 'Powers and Functions' section for your MOA in BAA No. 13? Most MOAs have 15-30 enumerated functions — planning teams often work from memory and miss half."
- "For each 'Direct' contribution you are claiming, ask: if this pillar fails to show progress, is my MOA one of the first agencies the Chief Minister's office would call to account?"
- "Does your provision reference 'rights'? What rights specifically? Have you traced them through the full BOL?"

This applies to ALL guidebooks — the Strategic Planning Guidebook has ~130 guide questions across 12 chapters as the reference pattern.

### Step Numbering Standards (MANDATORY)

Steps in guidebook chapters must use **clean sequential integers**: Step 1, Step 2, Step 3, Step 4, Step 5. **NEVER use sub-step labels** like Step 2b, Step 3b, Step 4b. This is a recurring error pattern that has been flagged multiple times.

- When adding content between existing steps, **renumber all subsequent steps**
- Step 1, 2, 3, 4 becomes Step 1, 2, 3, 4, 5 — not Step 1, 2, 3, 3b, 4
- Sub-items within a step (like bullet points or sub-sections) are fine — but the step numbers themselves must be integers
- Before generating the PDF, **scan all chapter files for any "b" suffix on step numbers** and fix them

### Legal Citation Verification Standards (MANDATORY)

Any worked example, template, or instructional section that cites legal provisions must go through the **legal pipeline** before and after writing. This prevents fabricated quotes, wrong attributions, and inaccurate paraphrases — a documented recurring error pattern.

**Before writing content that cites legal provisions:**
1. Run `/legal-researcher` to locate all applicable authorities with verbatim text
2. Use ONLY the verbatim text returned by the researcher — never paraphrase from memory
3. Verify which actor the provision assigns the obligation to (e.g., "National Government" vs. "Bangsamoro Government")

**After writing content that cites legal provisions — Legal QA Loop (REQUIRED):**
```
REPEAT until 0 errors remain (max 5 iterations):
  1. VERIFY — Run `/legal-reviewer ACCURACY` on the section
     - Check every quoted provision against source text (verbatim match)
     - Check every section/article/BAA number is correct
     - Check actor attribution (who has the obligation?)
     - Check that cited instruments are current (not superseded)

  2. GAP CHECK — Run `/legal-reviewer SUFFICIENCY`
     - Are there legal claims without citations?
     - Are there missing authorities that should be cited?
     - Is the creating law correctly identified (mandate vs. establishment)?

  3. FIX — For each error found:
     - Read the actual source text from the local archive
     - Replace the fabricated/incorrect text with verbatim quote
     - Update footnotes with correct identifiers

  4. RE-VERIFY — Run `/legal-reviewer ACCURACY` again on the fixed section
     - If 0 errors: proceed to PDF generation
     - If errors remain: loop back to step 3
```
Do NOT generate the PDF until the Legal QA Loop produces a clean ACCURACY report.

**Common fabrication patterns to watch for:**
- Misquoting BOL provisions (e.g., "shall take into consideration" when the actual text says "shall ensure the protection of")
- Attributing obligations to the wrong actor (e.g., attributing a National Government obligation to the Bangsamoro Government)
- Citing superseded instruments as current authority (e.g., citing the BTA Transition Plan when BAA No. 13 has superseded it)
- Stretching generic provisions to specific contexts (e.g., citing Art. V Sec. 2(a) "Administrative organization" as a specific mandate for a particular office)
- Inventing executive orders, memorandum circulars, or administrative arrangements without verification

**This applies to ALL guidebooks, CSWs, policy papers, and legislative documents.** The legal pipeline (`/legal-researcher` → `/legal-reviewer` → `/legal-assistant`) exists precisely to prevent these errors.

### Table Standards

- CSS: `table-layout: auto; width: 100%;` — WeasyPrint distributes based on content natively

### Table Design Standards (MANDATORY — BEFORE Writing)

Table column proportions must be decided **at content design time**, not during PDF rendering. Every table must be designed with appropriate column widths BEFORE it is written into the markdown.

**Rule: When writing any table, determine column widths FIRST.**

Before writing a markdown table, ask:
1. What kind of content goes in each column? (short labels, medium descriptions, long explanatory text)
2. What proportions are appropriate? (a "Status" column needs 10%, a "Description" column needs 40%)
3. Should this be a markdown pipe table (simple) or an HTML table with explicit widths (precise)?

**Use HTML tables with `<col>` for tables that need precise control:**
```html
<table>
<colgroup>
<col style="width:15%">
<col style="width:45%">
<col style="width:40%">
</colgroup>
<thead><tr><th>Legal Basis</th><th>Authority Granted</th><th>Justification</th></tr></thead>
<tbody>
<tr><td>BOL Art. VI, Sec. 12</td><td>...</td><td>...</td></tr>
</tbody>
</table>
```

**Use markdown pipe tables for simple tables where auto layout works well:**
- 2-3 columns with similar content lengths
- Tables where all columns have comparable text density
- Simple reference tables (term | definition)

**Column width guidelines by content type:**
| Content Type | Typical Width | Examples |
|---|---|---|
| ID / Number / Code | 8-12% | #, No., Tier, Status |
| Short label | 12-18% | Name, Type, Category |
| Medium description | 25-35% | Title, Provision, Legal Basis |
| Long text / explanation | 35-50% | Description, Justification, Authority |
| Fill-in blank (templates) | 30-40% | [Enter here], ............ |

**Template tables** (blank fill-in tables) MUST use HTML with explicit `<col>` widths — CSS `table-layout: auto` cannot distribute empty columns properly.

**Anti-pattern: Do NOT try to fix column widths via Python/regex in generate-pdf.py.** This has been attempted multiple times (keyword classification, content-length measurement, total-character-count) and failed every time. Table design belongs in the content, not the rendering pipeline.
- All cells: `word-wrap: break-word; overflow-wrap: break-word;`
- Tables with 5+ columns: reduce font to 8-9pt
- Tables with 7+ columns: consider landscape page or split into two tables
- **Smart column sizing (in generate-pdf.py):** The `post_process_html()` function injects `<colgroup>` with proportional widths based on header keyword matching:
  - **Narrow** (~8%): ID, Code, #, Type, Status, Tier, Level
  - **Medium** (~15%): Name, Title, Responsible, Timeline, Goal, Priority, Indicator, Target
  - **Wide** (~25%): Description, Statement, Narrative, Contribution, Provision, Mandate
  - Widths normalize to 100% per table. Add keywords to the classification lists as needed.
- **Column proportion check (Visual QA):** After rendering PDF, verify that:
  - Description/text columns are wider than ID/code/number columns
  - Template tables have adequate fill-in space
  - Header text fits without wrapping where possible
  - Long text cells wrap cleanly without orphaned words

---

## Appendix Generation

Individual appendices that need standalone distribution (detachable checklists, templates):

1. Create HTML versions in `appendices/` subdirectory
2. Convert each to PDF using WeasyPrint or the `/pdf` skill
3. Name consistently: `Appendix-{Letter}-{Title}.html` and `.pdf`

The main guidebook PDF includes appendices inline. The standalone PDFs in `appendices/` are for separate distribution.
