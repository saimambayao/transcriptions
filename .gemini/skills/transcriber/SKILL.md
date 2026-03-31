---
name: transcriber
description: |
  PDF text extraction and transcription verification skill.
  Extract text from PDFs using OCR, verify transcriptions against source PDFs, correct discrepancies.
  Use when: (1) extracting text from scanned PDFs, (2) verifying markdown transcriptions,
  (3) correcting transcription errors.
  For Word documents (.docx), use the /docx skill. For Excel spreadsheets (.xlsx), use the /xlsx skill.
argument-hint: "[pdf-path]"
allowed-tools: Read, Bash, Grep, Glob
---

# Transcriber Skill

PDF text extraction, transcription verification, and error correction.

> **Note**: For Word documents (.docx), use the [`/docx`](../docx/SKILL.md) skill. For Excel spreadsheets (.xlsx, .csv), use the [`/xlsx`](../xlsx/SKILL.md) skill.

## Use Cases

1. **Extract text from PDFs** - OCR scanned documents to markdown
2. **Verify transcriptions** - Compare existing markdown against PDF source
3. **Correct discrepancies** - Identify and fix transcription errors

## Setup

```bash
# System dependencies
brew install tesseract

# Python packages
source venv/bin/activate  # or your project's venv
pip install pymupdf pytesseract pillow pdfplumber
```

## PDF Scripts

All PDF scripts are in `scripts/` and executable via Bash:

| Script | Purpose | Usage |
|--------|---------|-------|
| `assess_pdf.py` | Determine extraction method | `python scripts/assess_pdf.py <pdf>` |
| `find_chapter.py` | Find chapter page boundaries | `python scripts/find_chapter.py <pdf> [chapter_num]` |
| `extract_chapter.py` | OCR extraction (scanned PDFs) | `python scripts/extract_chapter.py <pdf> <start> <end> [output]` |
| `extract_text_only.py` | Text extraction (embedded text) | `python scripts/extract_text_only.py <pdf> <start> <end> [output]` |

## PDF Workflows

### Extract Pages from a PDF

```bash
source venv/bin/activate
cd "${GEMINI_SKILL_DIR}"

# 1. Assess PDF to determine extraction method
python scripts/assess_pdf.py "path/to/document.pdf"

# 2. Find chapter/section boundaries (optional)
python scripts/find_chapter.py "path/to/document.pdf"

# 3. Extract pages (use appropriate script based on assessment)
# For scanned/image-based PDFs:
python scripts/extract_chapter.py "path/to/document.pdf" 1 20 /tmp/output.txt

# For PDFs with embedded text:
python scripts/extract_text_only.py "path/to/document.pdf" 1 20 /tmp/output.txt
```

### Verify a Transcription

1. Extract pages via OCR (above)
2. Read both OCR output and existing markdown
3. Compare section by section
4. Document discrepancies in table format
5. Apply corrections via Edit tool

See [references/verification-workflow.md](references/verification-workflow.md) for detailed workflow.

---

## References

| Reference | Content |
|-----------|---------|
| [ocr-errors.md](references/ocr-errors.md) | Common OCR misreads and fixes |
| [formatting-guide.md](references/formatting-guide.md) | Markdown formatting standards |
| [verification-workflow.md](references/verification-workflow.md) | Step-by-step verification process |

## DPI Selection (PDF)

| DPI | Use Case |
|-----|----------|
| 300 | Standard quality, faster |
| 400 | Better accuracy (default) |
| 600 | Problematic pages, small text |

Modify DPI in `extract_chapter.py` if needed.

---

## Related Skills

| Skill | Use For |
|-------|---------|
| [`/docx`](../docx/SKILL.md) | Word documents (.docx) - creation, editing, tracked changes, comments |
| [`/xlsx`](../xlsx/SKILL.md) | Excel spreadsheets (.xlsx, .xlsm, .csv) - creation, editing, analysis, charts, formulas |
