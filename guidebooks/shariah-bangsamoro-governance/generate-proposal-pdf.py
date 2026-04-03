#!/usr/bin/env python3
"""
Generate a professional Proposal PDF for the Shari'ah and Bangsamoro Governance
Guidebook project from the Concept Note markdown.

Dependencies:
    pip3 install markdown weasyprint
"""

import os
import sys
import markdown
from pathlib import Path
from weasyprint import HTML

# Configuration
BASE_DIR = Path(__file__).parent
TEMPLATE_PATH = BASE_DIR / "proposal-template.html"
PROPOSAL_MD = BASE_DIR / "concept-note-shariah-governance.md"
OUTPUT_PDF = BASE_DIR / "Proposal-Shariah-Governance.pdf"

# Markdown extensions
MD_EXTENSIONS = [
    "tables",
    "fenced_code",
    "toc",
    "smarty",
    "attr_list",
    "footnotes",
]

def generate_pdf():
    print(f"Reading markdown: {PROPOSAL_MD.name}")
    if not PROPOSAL_MD.exists():
        print(f"Error: {PROPOSAL_MD} not found.")
        return

    md_content = PROPOSAL_MD.read_text(encoding="utf-8")
    
    # Pre-process MD (remove title if it's in the cover)
    if md_content.startswith("# "):
        lines = md_content.split("\n")
        md_content = "\n".join(lines[1:])

    # Convert MD to HTML
    print("Converting Markdown to HTML...")
    html_content = markdown.markdown(md_content, extensions=MD_EXTENSIONS)
    
    # Read Template
    print("Reading Template...")
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    
    # Combine
    final_html = template.replace("{{CONTENT}}", html_content)
    
    # Save intermediate HTML
    (BASE_DIR / "proposal-rendered.html").write_text(final_html, encoding="utf-8")
    
    # Generate PDF
    print(f"Generating PDF: {OUTPUT_PDF.name}...")
    try:
        HTML(string=final_html, base_url=str(BASE_DIR)).write_pdf(str(OUTPUT_PDF))
        print(f"Success! PDF saved to: {OUTPUT_PDF}")
    except Exception as e:
        print(f"Error during PDF generation: {e}")

if __name__ == "__main__":
    generate_pdf()
