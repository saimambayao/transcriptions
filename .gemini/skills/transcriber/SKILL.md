---
name: transcriber
description: |
  Document transcription, extraction, review, and correction for PDFs and Word documents.
  5-phase PDF workflow: EXTRACT (marker-pdf primary, Tesseract/pdfplumber fallback) → STRUCTURE
  (add metadata, fix markdown) → REVIEW (compare against source PDF) → FIX (correct errors,
  preserve original as .raw.md) → FINALIZE (save corrected .md with verification footer).
  Word capabilities: Create, edit, analyze .docx files with tracked changes, comments, formatting.
  Use when: (1) transcribing PDFs to markdown, (2) verifying/correcting transcriptions,
  (3) creating/editing Word documents, (4) working with tracked changes.
  For Excel spreadsheets (.xlsx), use the /xlsx skill.
argument-hint: "[pdf-or-docx-path]"
allowed-tools: Read, Bash, Grep, Glob, Write, Edit
---

# Transcriber Skill

Document transcription, review, and correction for PDFs and Word documents.

> **Note**: For Excel spreadsheets (.xlsx, .csv), use the [`/xlsx`](../xlsx/SKILL.md) skill.

## Use Cases

### PDF Documents
1. **Transcribe PDFs** — Extract text to clean markdown (scanned or text-based)
2. **Review transcriptions** — Compare markdown against source PDF for accuracy
3. **Fix errors** — Correct OCR artifacts, missing content, garbled text
4. **Preserve originals** — Keep raw extraction as `.raw.md`, save corrected as `.md`

### Word Documents
5. **Create new documents** — Generate .docx files with proper formatting
6. **Edit existing documents** — Modify content with tracked changes
7. **Analyze documents** — Extract text, read comments, review structure

---

## PDF Setup

### Primary: marker-pdf (recommended)
```bash
# Install via pipx (one-time)
pipx install marker-pdf
```
marker-pdf is free, open source (Apache 2.0). Produces native markdown with proper headers, tables, and structure. Works on both scanned and text-based PDFs.

### Fallback: Tesseract + pdfplumber
```bash
brew install tesseract
pip install pymupdf pytesseract pillow pdfplumber
```

### Word Document Tools
```bash
brew install pandoc
npm install -g docx
brew install libreoffice poppler
pip install defusedxml
```

---

## PDF Workflow: 5 Phases

### Phase 1: EXTRACT

Use the 3-tier extraction strategy. Try Tier 1 first; fall back only if it fails.

**Tier 1: marker-pdf** (primary — best quality, handles both scanned and text PDFs)
```bash
marker_single "<pdf_path>" --output_dir /tmp/marker-output --disable_image_extraction --disable_multiprocessing
```
Output: `/tmp/marker-output/<filename>/<filename>.md`

**Tier 2: pdfplumber** (fallback for text-based PDFs)
```bash
cd "${CLAUDE_SKILL_DIR}"
python3 scripts/assess_pdf.py "<pdf_path>"       # Check if text-based
python3 scripts/extract_text_only.py "<pdf_path>" <start> <end> /tmp/output.txt
```

**Tier 3: Tesseract OCR** (fallback for scanned PDFs when marker fails)
```bash
cd "${CLAUDE_SKILL_DIR}"
python3 scripts/extract_chapter.py "<pdf_path>" <start> <end> /tmp/output.txt
```

### Phase 2: STRUCTURE

Transform raw extraction into clean markdown:

1. **Add front matter header:**
```markdown
# <Book Title>

**Author:** <Name>
**Pages:** <N>

**Source:** `<filename>.pdf`
**Transcription Method:** marker-pdf | pdfplumber | OCR (Tesseract, 400 DPI)
**Transcribed:** YYYY-MM-DD

---
```

2. **Fix markdown structure:**
   - Ensure chapter/section headers use proper `#`/`##`/`###` levels
   - Clean up page separator artifacts if using Tier 2/3
   - Fix garbled characters, broken words, OCR noise
   - Ensure tables are properly formatted
   - Remove running headers/footers (page numbers, chapter labels)

3. **Save as raw extraction:** `<filename>.raw.md`
   - This preserves the unedited machine output for reference

### Phase 3: REVIEW

Compare the transcription against the source PDF for accuracy:

1. **Read the PDF** visually (use Read tool on PDF) for sample pages — check:
   - Table of contents structure matches
   - Chapter/section headers are correct
   - Key numeric data (article numbers, section numbers, dates) are accurate
   - Legal citations (RA, GR, Art., Sec.) are correctly transcribed
   - Proper nouns (case names, author names) are spelled correctly

2. **Spot-check high-priority content:**
   - First and last pages of each chapter
   - All tables (structure, values, alignment)
   - Footnotes and endnotes
   - Legal form templates (exact wording matters)

3. **Document discrepancies** in a review table:

| # | Location | Transcription | PDF Source | Action |
|---|----------|--------------|------------|--------|
| 1 | Ch. 3, p.45 | "7.9 million" | "1.9 million" | Fix — numeric error |
| 2 | Ch. 5, p.89 | Missing paragraph | Present in PDF | Add — content gap |
| 3 | Table 2.1 | "542" | "942" | Verify — possible OCR error |

### Phase 4: FIX

Correct all errors identified in the Review phase:

1. **Fix each discrepancy** from the review table using the Edit tool
2. **Priority order:**
   - Legal citations and article/section numbers (highest — errors here are dangerous)
   - Numeric data (financial figures, dates, statistics)
   - Proper nouns (case names, author names)
   - Missing content (paragraphs, table rows, footnotes)
   - Formatting issues (headers, lists, tables)
   - OCR artifacts (garbled characters, broken words)
3. **Never guess** — if uncertain, check the PDF source page directly

### Phase 5: FINALIZE

1. **Preserve the original raw extraction:** `<filename>.raw.md` (already saved in Phase 2)
2. **Save the corrected version:** `<filename>.md` (the FIXED final version)
3. **Add verification footer:**
```markdown
---
**Verified:** YYYY-MM-DD — Compared against PDF source, <N> corrections applied
**Method:** marker-pdf + manual review
```

4. **Report to user:** List the corrections made and overall quality assessment

---

## Scaling by Document Size

| Size | Approach |
|------|----------|
| < 100 pp | Extract all at once, full review |
| 100-500 pp | Extract in chunks, spot-check review (every 5th page) |
| 500+ pp | Extract in chunks, targeted review (TOC, tables, citations only) |

---

## Legacy PDF Scripts (Tier 2/3 Fallback)

All scripts are in `scripts/` relative to the skill directory:

| Script | Purpose | Usage |
|--------|---------|-------|
| `assess_pdf.py` | Determine extraction method | `python scripts/assess_pdf.py <pdf>` |
| `find_chapter.py` | Find chapter page boundaries | `python scripts/find_chapter.py <pdf> [chapter_num]` |
| `extract_chapter.py` | OCR extraction (scanned PDFs) | `python scripts/extract_chapter.py <pdf> <start> <end> [output]` |
| `extract_text_only.py` | Text extraction (embedded text) | `python scripts/extract_text_only.py <pdf> <start> <end> [output]` |

### DPI Selection (Tier 3 OCR)

| DPI | Use Case |
|-----|----------|
| 300 | Standard quality, faster |
| 400 | Better accuracy (default) |
| 600 | Problematic pages, small text |

---

## Word Document Workflows

### Workflow Decision Tree

**Reading/Analyzing Content**: Use text extraction or raw XML access

**Creating New Document**: Use docx-js workflow

**Editing Existing Document**:
- Your own document + simple changes: Use basic OOXML editing
- Someone else's document: Use **Redlining workflow** (recommended)
- Legal, academic, business, or government docs: Use **Redlining workflow** (required)

### Reading Word Document Content

#### Text Extraction
Convert document to markdown using pandoc:
```bash
# Convert document to markdown with tracked changes
pandoc --track-changes=all path-to-file.docx -o output.md
# Options: --track-changes=accept/reject/all
```

#### Raw XML Access
For comments, complex formatting, document structure, embedded media, and metadata:
```bash
# Unpack document
python ooxml/scripts/unpack.py document.docx unpacked/
```

Key file structures:
- `word/document.xml` - Main document contents
- `word/comments.xml` - Comments referenced in document.xml
- `word/media/` - Embedded images and media files
- Tracked changes use `<w:ins>` (insertions) and `<w:del>` (deletions) tags

### Creating New Word Documents

Use **docx-js** (JavaScript/TypeScript):

1. **MANDATORY**: Read [references/docx-js.md](references/docx-js.md) completely before proceeding
2. Create a JavaScript/TypeScript file using Document, Paragraph, TextRun components
3. Export as .docx using `Packer.toBuffer()`

### Editing Existing Word Documents

Use the **Document library** (Python for OOXML manipulation):

1. **MANDATORY**: Read [references/ooxml.md](references/ooxml.md) completely before proceeding
2. Unpack: `python ooxml/scripts/unpack.py <docx> <output_dir>`
3. Create and run Python script using Document library
4. Pack: `python ooxml/scripts/pack.py <input_dir> <output.docx>`

### Redlining Workflow (Tracked Changes)

For comprehensive tracked changes in professional documents:

1. **Get markdown representation**:
   ```bash
   pandoc --track-changes=all document.docx -o current.md
   ```

2. **Identify and group changes**: Organize into logical batches (3-10 changes each)

3. **Read documentation and unpack**:
   - Read [references/ooxml.md](references/ooxml.md) - pay attention to "Tracked Change Patterns"
   - `python ooxml/scripts/unpack.py document.docx unpacked/`
   - Note the suggested RSID from unpack script

4. **Implement changes in batches**:
   - Map text to XML: grep for text in `word/document.xml`
   - Create and run script using `get_node` and `doc.save()`

5. **Pack the document**:
   ```bash
   python ooxml/scripts/pack.py unpacked reviewed-document.docx
   ```

6. **Verify**:
   ```bash
   pandoc --track-changes=all reviewed-document.docx -o verification.md
   ```

### Converting Documents to Images

For visual analysis:
```bash
# Convert DOCX to PDF
soffice --headless --convert-to pdf document.docx

# Convert PDF pages to JPEG
pdftoppm -jpeg -r 150 document.pdf page
# Creates page-1.jpg, page-2.jpg, etc.
```

---

## OOXML Scripts (Word)

| Script | Purpose | Usage |
|--------|---------|-------|
| `unpack.py` | Extract .docx to directory | `python ooxml/scripts/unpack.py <docx> <output_dir>` |
| `pack.py` | Create .docx from directory | `python ooxml/scripts/pack.py <input_dir> <output.docx>` |
| `validate.py` | Validate document structure | `python ooxml/scripts/validate.py <docx>` |

## Code Style Guidelines (Word)

When generating code for DOCX operations:
- Write concise code
- Avoid verbose variable names and redundant operations
- Avoid unnecessary print statements

---

## References

| Reference | Content |
|-----------|---------|
| [ocr-errors.md](references/ocr-errors.md) | Common OCR misreads and fixes |
| [formatting-guide.md](references/formatting-guide.md) | Markdown formatting standards |
| [verification-workflow.md](references/verification-workflow.md) | Step-by-step verification process |
| [docx-js.md](references/docx-js.md) | JavaScript library for creating Word documents |
| [ooxml.md](references/ooxml.md) | OOXML technical reference for editing Word documents |

---

## Related Skills

| Skill | Use For |
|-------|---------|
| [`/xlsx`](../xlsx/SKILL.md) | Excel spreadsheets (.xlsx, .xlsm, .csv) - creation, editing, analysis, charts, formulas |
