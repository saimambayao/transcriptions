# Transcription Formatting Guide

## Document Structure

### Chapter Headers
```markdown
# Chapter N: Title

## Section Title

### Subsection Title
```

### Frontmatter (if present)
Include executive summaries, forewords, or prefaces before Chapter 1.

## Text Elements

### Paragraphs
- Preserve paragraph breaks from source
- Single blank line between paragraphs
- Do not add artificial line breaks within paragraphs

### Lists
```markdown
- Unordered item
- Another item

1. Ordered item
2. Another item

a. Lettered item (use for legal/policy documents)
b. Another item
```

### Blockquotes
Use for cited text, official statements, or excerpts:
```markdown
> This is a direct quote from the source document.
> It may span multiple lines.
```

## Tables

### Standard Format
```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
```

### Alignment
```markdown
| Left     | Center   | Right    |
|:---------|:--------:|---------:|
| text     | text     | 1,234.56 |
```

### Large Tables
For tables spanning multiple pages in source:
1. Combine into single markdown table
2. Note original page breaks in HTML comment if needed

## Numeric Data

### Currency
- Use peso sign: `₱1,234,567.89`
- Include commas for thousands
- Two decimal places for currency

### Percentages
- Format: `45.6%`
- Include decimal where shown in source

### Years and Dates
- Years: `2023-2028`
- Full dates: `December 9, 2025`

## Footnotes

Place at end of chapter:
```markdown
---

**Notes:**

[^1]: First footnote text.
[^2]: Second footnote text.
```

Or inline if brief:
```markdown
This is the main text.[^1]

[^1]: Brief explanatory note.
```

## Source Citation

End each file with:
```markdown
---

**Source:** [Document Title], [Publisher], [Year]. Pages [N]-[M].
```

## File Naming Convention

| Document Type | Pattern | Example |
|---------------|---------|---------|
| BDP Chapters | `NN-chapter-N-title-slug.md` | `05-chapter-5-governance.md` |
| BOL Articles | `article-N-title-slug.md` | `article-10-fiscal-autonomy.md` |
| BBSA Chapters | `chapter-N-title-slug.md` | `chapter-3-budget-preparation.md` |

## Quality Checklist

Before finalizing:
- [ ] Chapter title matches source exactly
- [ ] All sections and subsections present
- [ ] Tables properly formatted
- [ ] Numeric data verified against source
- [ ] Footnotes included
- [ ] Source citation added
- [ ] No OCR artifacts remaining
