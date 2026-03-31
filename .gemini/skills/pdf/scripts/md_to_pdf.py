#!/usr/bin/env python3
"""Convert a Markdown file to a professionally styled PDF.

Usage:
    python md_to_pdf.py input.md output.pdf [--title TITLE] [--style minimal|report|academic]

The script converts markdown to HTML with professional CSS styling,
then uses WeasyPrint to produce a print-quality PDF.
"""

import argparse
import os
import sys

try:
    import markdown
except ImportError:
    print("Error: markdown is not installed. Run: pip install markdown")
    sys.exit(1)

try:
    from weasyprint import HTML
except ImportError:
    print("Error: weasyprint is not installed. Run: pip install weasyprint")
    sys.exit(1)


STYLES = {
    "minimal": """
@page {
  size: letter;
  margin: 1in;
  @bottom-center {
    content: counter(page);
    font-family: 'Inter', 'Helvetica Neue', sans-serif;
    font-size: 8pt;
    color: #999;
  }
}
body {
  font-family: 'Inter', 'Helvetica Neue', sans-serif;
  font-size: 10pt;
  line-height: 1.5;
  color: #1a1a1a;
  max-width: 100%;
}
h1 { font-size: 22pt; font-weight: 700; color: #111; margin-top: 0; margin-bottom: 0.5em; }
h2 { font-size: 15pt; font-weight: 600; color: #222; margin-top: 1.5em; border-bottom: 0.5pt solid #e0e0e0; padding-bottom: 4pt; }
h3 { font-size: 12pt; font-weight: 600; color: #333; margin-top: 1.2em; }
p { margin: 0.6em 0; }
table { width: 100%; border-collapse: collapse; margin: 1em 0; font-size: 9pt; page-break-inside: avoid; }
th { background: #f5f5f5; padding: 6pt 8pt; text-align: left; font-weight: 600; border-bottom: 1pt solid #ddd; }
td { padding: 6pt 8pt; border-bottom: 0.5pt solid #eee; }
code { background: #f5f5f5; padding: 1pt 4pt; font-size: 9pt; border-radius: 2pt; }
pre { background: #f5f5f5; padding: 12pt; font-size: 8.5pt; overflow-x: auto; border-radius: 4pt; }
blockquote { border-left: 3pt solid #ddd; margin-left: 0; padding-left: 16pt; color: #555; }
ul, ol { padding-left: 1.5em; }
li { margin: 0.3em 0; }
hr { border: none; border-top: 0.5pt solid #ddd; margin: 1.5em 0; }
""",

    "report": """
@page {
  size: letter;
  margin: 1in 0.75in;
  @top-center {
    content: string(doc-title);
    font-family: 'Inter', 'Helvetica Neue', sans-serif;
    font-size: 8pt;
    color: #888;
  }
  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
    font-family: 'Inter', 'Helvetica Neue', sans-serif;
    font-size: 8pt;
    color: #888;
  }
}
@page :first {
  @top-center { content: none; }
  @bottom-right { content: none; }
}
body {
  font-family: 'Inter', 'Helvetica Neue', sans-serif;
  font-size: 10pt;
  line-height: 1.5;
  color: #1a1a1a;
}
h1 {
  font-size: 26pt;
  font-weight: 700;
  color: #0f4c81;
  string-set: doc-title content();
  margin-bottom: 0.5em;
  border-bottom: 3pt solid #0f4c81;
  padding-bottom: 0.4em;
}
h2 { font-size: 16pt; color: #0f4c81; border-bottom: 1pt solid #ddd; padding-bottom: 4pt; margin-top: 1.5em; }
h3 { font-size: 12pt; color: #333; margin-top: 1.2em; }
p { margin: 0.6em 0; }
table { width: 100%; border-collapse: collapse; margin: 1em 0; font-size: 9pt; page-break-inside: avoid; }
th { background: #0f4c81; color: white; padding: 8pt 10pt; text-align: left; font-weight: 600; }
td { padding: 6pt 10pt; border-bottom: 0.5pt solid #ddd; }
tr:nth-child(even) td { background: #f8f9fa; }
code { background: #f0f4f8; padding: 1pt 4pt; font-size: 9pt; border-radius: 2pt; }
pre { background: #f0f4f8; padding: 12pt; font-size: 8.5pt; border-radius: 4pt; }
blockquote { border-left: 3pt solid #0f4c81; margin-left: 0; padding-left: 16pt; color: #555; background: #f0f4f8; padding: 12pt 16pt; }
ul, ol { padding-left: 1.5em; }
li { margin: 0.3em 0; }
hr { border: none; border-top: 1pt solid #ddd; margin: 1.5em 0; }
.callout { background: #e8f4f8; border-left: 3pt solid #0f4c81; padding: 12pt 16pt; margin: 1em 0; }
""",

    "academic": """
@page {
  size: letter;
  margin: 1in;
  @bottom-center {
    content: counter(page);
    font-family: 'Georgia', 'Times New Roman', serif;
    font-size: 10pt;
    color: #333;
  }
}
body {
  font-family: 'Georgia', 'Times New Roman', serif;
  font-size: 11pt;
  line-height: 1.6;
  color: #1a1a1a;
}
h1 { font-size: 18pt; font-weight: 700; text-align: center; margin-bottom: 0.3em; }
h2 { font-size: 14pt; font-weight: 700; margin-top: 1.5em; }
h3 { font-size: 12pt; font-weight: 700; margin-top: 1.2em; }
p { margin: 0.8em 0; text-align: justify; }
table { width: 100%; border-collapse: collapse; margin: 1em 0; font-size: 10pt; page-break-inside: avoid; }
th { padding: 6pt 8pt; text-align: left; font-weight: 700; border-top: 1.5pt solid #000; border-bottom: 1pt solid #000; }
td { padding: 6pt 8pt; border-bottom: 0.5pt solid #ccc; }
code { font-family: 'Courier New', monospace; font-size: 9.5pt; }
pre { font-family: 'Courier New', monospace; font-size: 9pt; padding: 12pt; background: #f9f9f9; }
blockquote { margin-left: 2em; font-style: italic; color: #444; }
ul, ol { padding-left: 2em; }
li { margin: 0.3em 0; }
hr { border: none; border-top: 0.5pt solid #999; margin: 1.5em 0; }
"""
}


def md_to_pdf(input_md: str, output_pdf: str, title: str | None = None, style: str = "report"):
    with open(input_md) as f:
        md_content = f.read()

    html_body = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'toc', 'attr_list', 'meta']
    )

    css = STYLES.get(style, STYLES["report"])
    doc_title = title or os.path.splitext(os.path.basename(input_md))[0]

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{doc_title}</title>
<style>{css}</style>
</head>
<body>
{html_body}
</body>
</html>"""

    base_url = os.path.dirname(os.path.abspath(input_md))
    HTML(string=html_content, base_url=base_url).write_pdf(output_pdf)
    print(f"PDF created: {output_pdf} (style: {style})")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Markdown to styled PDF')
    parser.add_argument('input', help='Input markdown file')
    parser.add_argument('output', help='Output PDF file')
    parser.add_argument('--title', help='Document title')
    parser.add_argument('--style', choices=['minimal', 'report', 'academic'],
                        default='report', help='Document style (default: report)')
    args = parser.parse_args()

    md_to_pdf(args.input, args.output, args.title, args.style)
