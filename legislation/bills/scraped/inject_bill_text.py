"""
inject_bill_text.py — Extract PDF text and inject into stub markdown files.

For each PB-N.md stub that has a Filed Copy PDF link, this script:
1. Looks up the downloaded PDF in pdfs/bta-1/ or pdfs/bta-2/
2. Extracts text using pdftotext (poppler)
3. Replaces the stub note with the full bill text

Requirements: pdftotext (brew install poppler)

Usage:
  python3 inject_bill_text.py             # process both BTA 1 and BTA 2
  python3 inject_bill_text.py --bta 1     # BTA 1 only
  python3 inject_bill_text.py --bta 2     # BTA 2 only
  python3 inject_bill_text.py --dry-run   # show counts without writing
  python3 inject_bill_text.py --force     # re-inject even if already done
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
BTA1_MD  = BASE_DIR / "bta-1"
BTA2_MD  = BASE_DIR / "bta-2"
BTA1_PDF = BASE_DIR / "pdfs" / "bta-1"
BTA2_PDF = BASE_DIR / "pdfs" / "bta-2"

STUB_MARKER = "> **Note:** Metadata stub. Full bill text extraction pending PDF transcription"


def check_pdftotext() -> bool:
    return shutil.which("pdftotext") is not None


def extract_pdf_links(md_content: str) -> list[str]:
    """Return list of PDF URLs from the Documents section."""
    return re.findall(r"\[Filed Copy \(PDF\)\]\((https?://[^)]+\.pdf)\)", md_content, re.I)


def pdf_filename_from_url(url: str) -> str:
    return url.split("/")[-1]


def extract_text(pdf_path: Path) -> str | None:
    """Run pdftotext and return cleaned text, or None on failure."""
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), "-"],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode != 0:
            return None
        text = result.stdout
        # Clean up: normalize line endings, collapse excessive blank lines
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        text = re.sub(r"\n{4,}", "\n\n\n", text)
        text = text.strip()
        return text if text else None
    except Exception:
        return None


def inject_text(md_path: Path, bill_text: str) -> None:
    """Replace the stub marker with full bill text in the markdown file."""
    content = md_path.read_text(encoding="utf-8")

    bill_text_section = (
        "## Full Text\n\n"
        "```\n"
        + bill_text +
        "\n```\n"
    )

    # Replace stub marker line
    if STUB_MARKER in content:
        # Remove the blockquote stub line and append full text
        content = re.sub(
            r"> \*\*Note:\*\* Metadata stub\..*?\n?$",
            "",
            content,
            flags=re.MULTILINE
        ).rstrip()
        content = content + "\n\n" + bill_text_section
    else:
        # Already processed or different format — append
        content = content.rstrip() + "\n\n" + bill_text_section

    md_path.write_text(content, encoding="utf-8")


def process_directory(
    md_dir: Path,
    pdf_dir: Path,
    dry_run: bool,
    force: bool,
    bta_label: str
) -> tuple[int, int, int, int]:
    """Inject text into stubs. Returns (injected, skipped_done, skipped_no_pdf, failed)."""
    if not md_dir.exists():
        print(f"  {bta_label}: directory not found: {md_dir}")
        return 0, 0, 0, 0

    stubs = sorted(
        md_dir.glob("PB-*.md"),
        key=lambda f: int(re.search(r"PB-(\d+)", f.name).group(1))
    )

    injected = skipped_done = skipped_no_pdf = failed = 0

    for stub in stubs:
        content = stub.read_text(encoding="utf-8")

        # Skip if already injected (no stub marker and has Full Text section)
        if STUB_MARKER not in content and "## Full Text" in content:
            if not force:
                skipped_done += 1
                continue

        # Find PDF links
        pdf_urls = extract_pdf_links(content)
        if not pdf_urls:
            skipped_no_pdf += 1
            continue

        # Use the first (Filed Copy) PDF
        pdf_url = pdf_urls[0]
        filename = pdf_filename_from_url(pdf_url)
        pdf_path = pdf_dir / filename

        if not pdf_path.exists():
            skipped_no_pdf += 1
            continue

        if dry_run:
            print(f"  [DRY] {stub.name} ← {filename}")
            injected += 1
            continue

        # Extract text
        text = extract_text(pdf_path)
        if not text:
            print(f"  FAIL (empty text): {stub.name}")
            failed += 1
            continue

        # Inject
        inject_text(stub, text)
        word_count = len(text.split())
        print(f"  ✓ {stub.name} ({word_count:,} words)")
        injected += 1

    return injected, skipped_done, skipped_no_pdf, failed


def main():
    if not check_pdftotext():
        print("ERROR: pdftotext not found. Install with: brew install poppler")
        sys.exit(1)

    parser = argparse.ArgumentParser(
        description="Inject bill text from PDFs into scraped markdown stubs"
    )
    parser.add_argument("--bta", choices=["1", "2", "all"], default="all")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true",
                        help="Re-inject even if already done")
    args = parser.parse_args()

    total = [0, 0, 0, 0]

    if args.bta in ("1", "all"):
        print(f"\nBTA 1 ({BTA1_MD}):")
        counts = process_directory(BTA1_MD, BTA1_PDF, args.dry_run, args.force, "BTA 1")
        for i, c in enumerate(counts):
            total[i] += c
        print(f"  Injected: {counts[0]} | Already done: {counts[1]} | No PDF: {counts[2]} | Failed: {counts[3]}")

    if args.bta in ("2", "all"):
        print(f"\nBTA 2 ({BTA2_MD}):")
        counts = process_directory(BTA2_MD, BTA2_PDF, args.dry_run, args.force, "BTA 2")
        for i, c in enumerate(counts):
            total[i] += c
        print(f"  Injected: {counts[0]} | Already done: {counts[1]} | No PDF: {counts[2]} | Failed: {counts[3]}")

    print(f"\nTotal — Injected: {total[0]} | Already done: {total[1]} | No PDF: {total[2]} | Failed: {total[3]}")


if __name__ == "__main__":
    main()
