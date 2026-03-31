# WeasyPrint Reference

CSS Paged Media reference for creating professional PDFs with WeasyPrint.

## Table of Contents

1. [Page Setup](#page-setup)
2. [Headers and Footers](#headers-and-footers)
3. [Page Breaks](#page-breaks)
4. [Fonts](#fonts)
5. [Images](#images)
6. [Advanced Features](#advanced-features)
7. [Python API](#python-api)
8. [Troubleshooting](#troubleshooting)

---

## Page Setup

### Page Sizes

```css
@page { size: letter; }           /* 8.5in x 11in */
@page { size: letter landscape; }  /* 11in x 8.5in */
@page { size: A4; }               /* 210mm x 297mm */
@page { size: A4 landscape; }
@page { size: legal; }            /* 8.5in x 14in */
@page { size: 6in 9in; }          /* Custom size */
```

### Margins

```css
@page {
  margin: 1in;                    /* All sides */
  margin: 1in 0.75in;            /* top/bottom left/right */
  margin: 1in 0.75in 1in 0.75in; /* top right bottom left */
}
```

### Named Pages

```css
@page cover { margin: 0; }
@page landscape-page { size: letter landscape; }

.cover-section { page: cover; }
.wide-table { page: landscape-page; }
```

### First, Left, Right Pages

```css
@page :first { margin-top: 2in; }
@page :left { margin-left: 1.25in; margin-right: 0.75in; }
@page :right { margin-left: 0.75in; margin-right: 1.25in; }
```

---

## Headers and Footers

WeasyPrint supports margin boxes for headers/footers via CSS `@page` rules.

### Available Margin Boxes

```
@top-left-corner  @top-left  @top-center  @top-right  @top-right-corner
@left-top                                              @right-top
@left-middle                                           @right-middle
@left-bottom                                           @right-bottom
@bottom-left-corner @bottom-left @bottom-center @bottom-right @bottom-right-corner
```

### Page Numbers

```css
@page {
  @bottom-center {
    content: counter(page);               /* Just the number */
  }
  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);  /* Page X of Y */
  }
}
```

### Running Headers (from Document Content)

```css
/* Set the string from an h1 element */
h1 { string-set: chapter-title content(); }

@page {
  @top-left {
    content: string(chapter-title);
    font-size: 8pt;
    color: #888;
  }
}
```

### Suppress Header/Footer on First Page

```css
@page :first {
  @top-left { content: none; }
  @top-right { content: none; }
  @bottom-center { content: none; }
}
```

### Styled Headers/Footers

```css
@page {
  @top-center {
    content: "Company Name — Confidential";
    font-family: 'Inter', sans-serif;
    font-size: 7.5pt;
    color: #999;
    letter-spacing: 0.5pt;
    text-transform: uppercase;
    border-bottom: 0.5pt solid #ddd;
    padding-bottom: 4pt;
  }
  @bottom-left {
    content: "Draft — Not for Distribution";
    font-family: 'Inter', sans-serif;
    font-size: 7.5pt;
    color: #c00;
  }
}
```

---

## Page Breaks

### Forcing Breaks

```css
.page-break { page-break-before: always; }
.new-chapter { break-before: page; }
```

### Preventing Breaks

```css
/* Don't break inside these elements */
table, figure, .callout, .card {
  page-break-inside: avoid;
}

/* Keep heading with the content that follows */
h1, h2, h3 {
  page-break-after: avoid;
}
```

### Orphans and Widows

```css
p {
  orphans: 3;   /* Min lines at bottom of page */
  widows: 3;    /* Min lines at top of page */
}
```

---

## Fonts

### System Fonts

WeasyPrint uses system-installed fonts. On macOS, Inter is often available.

```css
body { font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif; }
```

### Custom Fonts via @font-face

```css
@font-face {
  font-family: 'Inter';
  src: url('fonts/Inter-Regular.woff2') format('woff2'),
       url('fonts/Inter-Regular.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
}

@font-face {
  font-family: 'Inter';
  src: url('fonts/Inter-Bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
}
```

### Font from URL (Google Fonts workaround)

WeasyPrint cannot fetch from Google Fonts URLs directly. Download the font files
and use local `@font-face` declarations instead.

---

## Images

### Embedding Images

```html
<img src="chart.png" style="width: 100%; max-height: 4in;">
<img src="logo.png" style="width: 1.5in; height: auto;">
```

### Images in Headers

```css
@page {
  @top-left {
    content: url('logo.png');
    height: 0.4in;
  }
}
```

### Background Images

```css
.cover {
  background-image: url('cover-bg.jpg');
  background-size: cover;
  background-position: center;
}
```

### Base64 Inline Images

```html
<img src="data:image/png;base64,iVBOR...">
```

---

## Advanced Features

### Footnotes

```css
.footnote {
  float: footnote;
  font-size: 8pt;
}

::footnote-marker {
  content: counter(footnote) ". ";
}

::footnote-call {
  content: counter(footnote);
  font-size: 7pt;
  vertical-align: super;
}
```

### Bookmarks (PDF Table of Contents)

```css
h1 { bookmark-level: 1; }
h2 { bookmark-level: 2; }
h3 { bookmark-level: 3; }
```

This creates a navigable table of contents in PDF readers.

### Columns

```css
.two-columns {
  columns: 2;
  column-gap: 24pt;
  column-rule: 0.5pt solid #ddd;
}
```

### PDF Metadata

Set via Python API:

```python
from weasyprint import HTML

doc = HTML('document.html').render()
doc.write_pdf(
    'output.pdf',
    presentational_hints=True
)
```

### Links

HTML links (`<a href="...">`) are preserved as clickable links in the PDF.

```html
<a href="https://example.com">Visit Example</a>
<a href="#section-2">Jump to Section 2</a>
```

---

## Python API

### Basic Usage

```python
from weasyprint import HTML, CSS

# From file
HTML('document.html').write_pdf('output.pdf')

# From string
HTML(string='<h1>Hello</h1>').write_pdf('output.pdf')

# From URL
HTML('https://example.com').write_pdf('output.pdf')

# With base_url for resolving relative paths
HTML(string=html, base_url='/path/to/assets/').write_pdf('output.pdf')
```

### Adding External Stylesheets

```python
from weasyprint import HTML, CSS

html = HTML('document.html')
css = CSS(string='@page { margin: 1in; } body { font-size: 10pt; }')
html.write_pdf('output.pdf', stylesheets=[css])
```

### Multiple Stylesheets

```python
html = HTML('document.html')
html.write_pdf('output.pdf', stylesheets=[
    CSS('base.css'),
    CSS('theme.css'),
    CSS(string='@page { size: A4; }'),
])
```

### Getting Page Count

```python
doc = HTML('document.html').render()
page_count = len(doc.pages)
doc.write_pdf('output.pdf')
```

---

## Troubleshooting

### Common Issues

**Fonts not rendering**: Ensure the font is installed system-wide or use `@font-face`.
On macOS: `fc-list | grep -i inter` to check.

**Images not loading**: Use absolute paths or set `base_url` to the directory
containing the images.

**Tables breaking across pages**: Add `page-break-inside: avoid;` to tables.
For very long tables, this may force them to the next page — accept this tradeoff
or split large tables manually.

**Flexbox not working in @page margin boxes**: Margin boxes have limited CSS support.
Use simple text content and basic properties only.

**CSS Grid**: WeasyPrint has limited CSS Grid support. Prefer flexbox or table-based
layouts for complex arrangements.

**Background colors not printing**: Add `-webkit-print-color-adjust: exact;` and
`print-color-adjust: exact;` to elements with backgrounds.

### Performance Tips

- Optimize images before embedding (resize to needed dimensions)
- Avoid very large HTML files — split into sections if needed
- Use `presentational_hints=True` for better rendering of HTML attributes
