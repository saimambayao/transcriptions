# PDF Transcription Guide

Transcribe PDF documents (government plans, legal documents, reports) to markdown files in the `references/` directory for use as platform reference data.

## Command Pattern

```bash
/documenter transcribe <pdf-path> --chapter <N> --output <output-dir>
```

**Examples:**
```bash
/documenter transcribe references/pdf-files/1st-BDP-2020-2022.pdf --chapter 2 --output references/bdp1
/documenter transcribe references/pdf-files/BOL-RA-11054.pdf --all --output references/bol
```

## OCR Process

### Step 1: Setup (First Time Only)

**System dependencies:**
```bash
brew install tesseract poppler
```

**Python packages (use backend venv):**
```bash
source backend/venv/bin/activate
pip install pypdf pdfplumber pdf2image pytesseract pillow
```

### Step 2: Locate Chapter/Section

```python
import pdfplumber

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if f"CHAPTER {chapter_num}" in text.upper():
            print(f"Chapter {chapter_num} starts at PDF page {i+1}")
            break
```

### Step 3: Extract with OCR

```python
from pdf2image import convert_from_path
import pytesseract

# Convert PDF pages to images at 300 DPI
images = convert_from_path(pdf_path, first_page=start, last_page=end, dpi=300)

# OCR each page
for i, img in enumerate(images):
    text = pytesseract.image_to_string(img)
    print(text)
```

### Step 4: Format as Markdown

**Output structure:**
```markdown
# CHAPTER N

# Chapter Title

Introduction paragraph...

---

## Section Heading

Body text...

### Subsection

More content...

**Table X.X Title**

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data     | Data     | Data     |

*Source: PSA*

---

*Source: Document Name, Chapter N (Pages X-Y)*
```

## Output Location

All transcribed files go to `references/` subdirectories:

```
references/
├── bdp1/                    # 1st BDP 2020-2022
│   ├── chapter-1-*.md
│   ├── chapter-2-*.md
│   └── ...
├── bdp2/                    # 2nd BDP 2023-2028
├── bol/                     # Bangsamoro Organic Law
├── bbsa/                    # Bangsamoro Budget System Act
└── pdf-files/               # Source PDFs (not transcribed)
```

## Output Naming Convention

| Document | Directory | File Pattern |
|----------|-----------|--------------|
| 1st BDP 2020-2022 | `references/bdp1/` | `chapter-N-title-slug.md` |
| 2nd BDP 2023-2028 | `references/bdp2/` | `chapter-N-title-slug.md` |
| Bangsamoro Organic Law | `references/bol/` | `article-N-title-slug.md` |
| BBSA (BAA No. 84) | `references/bbsa/` | `chapter-N-title-slug.md` |
| Other laws/documents | `references/<abbrev>/` | `section-N-title-slug.md` |

## Formatting Guidelines

1. **Chapter headers**: Use `# CHAPTER N` followed by `# Title`
2. **Sections**: Use `##` for main sections, `###` for subsections
3. **Tables**: Preserve in markdown table format with alignment
4. **Quotes**: Use `>` blockquote for cited text
5. **Footnotes**: Add at bottom with numbered references
6. **Source citation**: Always include source and page numbers at end
7. **Preserve verbatim**: Transcribe word-for-word, do not summarize
