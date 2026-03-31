# Verification Workflow

## Overview

The verification workflow compares OCR output against existing markdown transcriptions to identify and correct discrepancies.

## Phase 1: Preparation

### 1.1 Assess PDF Quality
```bash
python scripts/assess_pdf.py "path/to/document.pdf"
```

Output tells you whether to use:
- **pdfplumber** - For PDFs with embedded text
- **PyMuPDF + pytesseract** - For scanned/image-based PDFs

### 1.2 Find Chapter Boundaries
```bash
python scripts/find_chapter.py "path/to/document.pdf"
```

Lists all chapter start pages.

### 1.3 Extract Chapter
```bash
# For scanned PDFs (most common)
python scripts/extract_chapter.py "path/to/document.pdf" <start> <end> /tmp/chapter_ocr.txt

# For text-based PDFs
python scripts/extract_text_only.py "path/to/document.pdf" <start> <end> /tmp/chapter.txt
```

## Phase 2: Comparison

### 2.1 Read Both Files
1. Read OCR output from `/tmp/chapter_ocr.txt`
2. Read existing markdown from `references/<dir>/<file>.md`

### 2.2 Systematic Comparison

Compare section by section:
1. Chapter title and headers
2. Each paragraph for word accuracy
3. Each table for structure and values
4. Lists for completeness
5. Numeric data (highest priority)
6. Proper nouns and citations

### 2.3 Document Discrepancies

Create a discrepancy table:

| # | Location | Markdown (Current) | PDF (OCR Source) | Action |
|---|----------|-------------------|------------------|--------|
| 1 | Line 57 | "7.9 million" | "1.9 million" | Fix - numeric error |
| 2 | Line 89 | Missing | "Additional paragraph" | Add - content missing |
| 3 | Table 3.1 | "542" | "942" | Verify - OCR may be wrong |

### 2.4 Verify Discrepancies

For each discrepancy:
1. **If OCR is clearly correct** → Fix markdown
2. **If unclear** → Check original PDF visually
3. **If OCR is wrong** → Keep markdown, note OCR limitation

## Phase 3: Corrections

### 3.1 Apply Fixes
Use Edit tool for each correction:
```
Edit: file_path, old_string, new_string
```

### 3.2 Batch Corrections
For multiple corrections in same file:
1. List all corrections
2. Apply from bottom to top (preserves line numbers)
3. Or apply all at once if using unique strings

### 3.3 Verification Pass
After corrections:
1. Re-read the markdown file
2. Confirm all fixes applied
3. Check no new errors introduced

## Phase 4: Documentation

### 4.1 Mark as Verified
Add to file footer:
```markdown
---
**Verified:** [Date] - Compared against PDF pages [N]-[M]
```

### 4.2 Update INDEX
If maintaining an index:
```markdown
| Chapter | Status | Verified Date |
|---------|--------|---------------|
| Chapter 1 | Verified | 2025-01-19 |
```

## Verification Checklist

For each chapter:
- [ ] PDF quality assessed
- [ ] Chapter boundaries identified
- [ ] OCR extraction completed
- [ ] Section-by-section comparison done
- [ ] Discrepancies documented
- [ ] Corrections applied
- [ ] Verification pass completed
- [ ] Chapter marked as verified

## Tips

### Handling Large Chapters
- Process in sections (e.g., every 5 pages)
- Focus on tables and numeric data first
- Use grep to find specific terms

### Common Judgment Calls
- **Formatting differences** - Keep markdown conventions
- **Spelling variations** - Use source spelling
- **Abbreviations** - Follow source (don't expand)
- **Table layout** - Prioritize readability over exact match

### When OCR is Wrong
OCR can misread source too. Trust:
1. Context (does the number make sense?)
2. Surrounding text
3. Visual inspection if truly uncertain
