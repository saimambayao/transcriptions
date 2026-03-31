# PDF Design Guide

Professional design patterns for creating beautiful PDF documents with CSS and WeasyPrint.

## Table of Contents

1. [Color Palettes](#color-palettes)
2. [Typography](#typography)
3. [Layout Patterns](#layout-patterns)
4. [Table Styling](#table-styling)
5. [Cover Page Designs](#cover-page-designs)
6. [Decorative Elements](#decorative-elements)

---

## Color Palettes

### Corporate / Professional

| Name | Primary | Secondary | Accent | Background |
|------|---------|-----------|--------|------------|
| **Ocean Blue** | #0f4c81 | #1a6eb0 | #e8f4f8 | #f8f9fa |
| **Forest** | #2d6a4f | #40916c | #d8f3dc | #f8f9fa |
| **Slate** | #334155 | #475569 | #e2e8f0 | #f8fafc |
| **Crimson** | #991b1b | #b91c1c | #fee2e2 | #fef2f2 |
| **Amber** | #92400e | #b45309 | #fef3c7 | #fffbeb |

### Warm / Creative

| Name | Primary | Secondary | Accent | Background |
|------|---------|-----------|--------|------------|
| **Terracotta** | #c2410c | #d97706 | #fed7aa | #fffbeb |
| **Rose** | #9f1239 | #be123c | #fce7f3 | #fff1f2 |
| **Sage & Gold** | #4d7c0f | #ca8a04 | #ecfccb | #fefce8 |

### Cool / Technical

| Name | Primary | Secondary | Accent | Background |
|------|---------|-----------|--------|------------|
| **Steel** | #0f172a | #475569 | #cbd5e1 | #f1f5f9 |
| **Teal** | #115e59 | #0d9488 | #ccfbf1 | #f0fdfa |
| **Indigo** | #312e81 | #4338ca | #e0e7ff | #eef2ff |

### Government / Institutional

| Name | Primary | Secondary | Accent | Background |
|------|---------|-----------|--------|------------|
| **Navy** | #1e3a5f | #2c5282 | #dbeafe | #f0f4f8 |
| **Burgundy** | #5d1d2e | #7f1d1d | #f5e6e6 | #fdf2f2 |

---

## Typography

### Font Pairings

| Heading Font | Body Font | Mood |
|-------------|-----------|------|
| Inter Bold | Inter Regular | Modern, clean, versatile |
| Georgia Bold | Inter Regular | Authoritative yet readable |
| Inter Bold | Georgia Regular | Technical with warmth |

### Size Scale

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| Document title | 26-32pt | 700 | 1.2 |
| Cover subtitle | 14-16pt | 400 | 1.3 |
| Section heading (h2) | 16-18pt | 600 | 1.3 |
| Sub-heading (h3) | 12-13pt | 600 | 1.4 |
| Body text | 10-11pt | 400 | 1.4-1.6 |
| Table text | 9-9.5pt | 400 | 1.3 |
| Captions/footnotes | 8-8.5pt | 400 | 1.3 |
| Header/footer | 8pt | 400 | 1.0 |

### Spacing

| Between | Spacing |
|---------|---------|
| Paragraphs | 0.6-0.8em |
| Before h2 | 1.5-2em |
| Before h3 | 1.2-1.5em |
| After heading | 0.3-0.5em |
| Table rows | 6-8pt padding |
| Sections | 24-36pt |

---

## Layout Patterns

### Page Margins by Document Type

| Document | Top | Bottom | Left | Right |
|----------|-----|--------|------|-------|
| Report | 1in | 1in | 0.75in | 0.75in |
| Letter | 1in | 1in | 1in | 1in |
| Invoice | 0.75in | 0.75in | 0.75in | 0.75in |
| Certificate | 0.5in | 0.5in | 0.5in | 0.5in |
| Academic | 1in | 1in | 1in | 1in |

### Two-Column Layout

```css
.two-col {
  display: flex;
  gap: 24pt;
}
.two-col > div {
  flex: 1;
}
/* Unequal columns */
.two-col .sidebar { flex: 0 0 35%; }
.two-col .main { flex: 1; }
```

### Sidebar Layout

```css
.with-sidebar {
  display: flex;
  gap: 20pt;
}
.sidebar {
  flex: 0 0 2in;
  background: #f0f4f8;
  padding: 16pt;
  border-radius: 4pt;
}
.content { flex: 1; }
```

### Key-Value / Data Pairs

```css
.kv-row {
  display: flex;
  border-bottom: 0.5pt solid #eee;
  padding: 6pt 0;
}
.kv-label {
  flex: 0 0 2in;
  font-weight: 600;
  color: #555;
}
.kv-value { flex: 1; }
```

---

## Table Styling

### Professional Table

```css
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 9pt;
  page-break-inside: avoid;
}
th {
  background: #0f4c81;
  color: white;
  padding: 8pt 10pt;
  text-align: left;
  font-weight: 600;
  font-size: 8.5pt;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}
td {
  padding: 6pt 10pt;
  border-bottom: 0.5pt solid #e5e7eb;
}
tr:nth-child(even) td {
  background: #f8f9fa;
}
```

### Minimal Table

```css
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 9pt;
}
th {
  padding: 6pt 8pt;
  text-align: left;
  font-weight: 600;
  border-bottom: 1.5pt solid #1a1a1a;
}
td {
  padding: 6pt 8pt;
  border-bottom: 0.5pt solid #e5e7eb;
}
```

### Financial Table

```css
table.financial td { text-align: right; font-variant-numeric: tabular-nums; }
table.financial td:first-child { text-align: left; }
table.financial .subtotal { border-top: 1pt solid #999; font-weight: 600; }
table.financial .total {
  border-top: 2pt solid #1a1a1a;
  font-weight: 700;
  font-size: 10pt;
}
```

---

## Cover Page Designs

### Clean Corporate

```css
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
  border-bottom: 3pt solid #0f4c81;
  padding-bottom: 12pt;
  margin-bottom: 16pt;
}
.cover .subtitle {
  font-size: 14pt;
  color: #555;
}
.cover .meta {
  margin-top: 3em;
  font-size: 10pt;
  color: #666;
  line-height: 1.8;
}
```

### Bold Color Block

```css
.cover {
  height: 100vh;
  background: #0f4c81;
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 2in 1in;
  margin: -1in -0.75in 0;  /* bleed to page edges */
}
.cover h1 {
  font-size: 32pt;
  font-weight: 700;
  border-bottom: 3pt solid rgba(255,255,255,0.4);
  padding-bottom: 12pt;
}
.cover .subtitle {
  font-size: 14pt;
  color: rgba(255,255,255,0.8);
  margin-top: 8pt;
}
.cover .meta {
  margin-top: 2em;
  font-size: 9pt;
  color: rgba(255,255,255,0.6);
}
```

### Accent Line

```css
.cover {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.cover::before {
  content: '';
  display: block;
  width: 60pt;
  height: 4pt;
  background: #0f4c81;
  margin-bottom: 24pt;
}
.cover h1 {
  font-size: 30pt;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 8pt;
}
```

---

## Decorative Elements

### Accent Bars

```css
/* Top of each page */
@page {
  border-top: 3pt solid #0f4c81;
}

/* Section divider */
.divider {
  height: 2pt;
  background: linear-gradient(to right, #0f4c81, transparent);
  margin: 24pt 0;
}
```

### Callout Boxes

```css
/* Info callout */
.callout {
  background: #e8f4f8;
  border-left: 3pt solid #0f4c81;
  padding: 12pt 16pt;
  margin: 1em 0;
  font-size: 9.5pt;
  page-break-inside: avoid;
}

/* Warning callout */
.callout-warning {
  background: #fef3c7;
  border-left: 3pt solid #d97706;
  padding: 12pt 16pt;
  margin: 1em 0;
}

/* Success callout */
.callout-success {
  background: #d1fae5;
  border-left: 3pt solid #059669;
  padding: 12pt 16pt;
  margin: 1em 0;
}
```

### Badges / Tags

```css
.badge {
  display: inline-block;
  padding: 2pt 8pt;
  border-radius: 10pt;
  font-size: 7.5pt;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}
.badge-primary { background: #dbeafe; color: #1e40af; }
.badge-success { background: #d1fae5; color: #065f46; }
.badge-warning { background: #fef3c7; color: #92400e; }
.badge-danger { background: #fee2e2; color: #991b1b; }
```

### Pull Quotes

```css
.pull-quote {
  font-size: 14pt;
  font-style: italic;
  color: #0f4c81;
  border-top: 2pt solid #0f4c81;
  border-bottom: 2pt solid #0f4c81;
  padding: 16pt 0;
  margin: 1.5em 1in;
  text-align: center;
}
```

---

## Print-Specific Tips

- Use `pt` for font sizes (not `px`) — they map directly to print
- Use `in` or `cm` for margins and page layout
- Use `page-break-inside: avoid` on tables, figures, and callouts
- Use `page-break-before: always` for new sections/chapters
- Use `page-break-after: avoid` on headings to keep them with content
- Keep body text at 10-11pt — smaller is hard to read in print
- Use `font-variant-numeric: tabular-nums` for aligned numbers in tables
- Test with actual print preview, not just screen rendering
