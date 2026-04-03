# Markdown to Word Conversion Script

## Requirements

The `convert_to_docx.py` script requires the `python-docx` library.

### Installation

```bash
pip3 install --user --break-system-packages python-docx
```

Or if you prefer a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install python-docx
```

## Usage

```bash
python3 convert_to_docx.py <input-file.md> [output-file.docx]
```

If no output file is specified, the script will create a .docx file with the same name as the input file.

## Formatting

The conversion maintains:
- Font: Bookman Old Style, 12pt
- Single spacing
- Standard margins (1 inch)
- Page numbers in footer
- ALL CAPS titles (centered)
- Bold text
- Superscript footnote citations (¹, ², ³, ...)
- WHEREAS clauses (indented 0.5 inch)
- RESOLVED clauses (indented 0.5 inch)
