"""
download_pdfs.py — Download PDFs for all scraped bills.

Reads all PB-*.md stubs in bta-1/ and bta-2/, extracts PDF links,
and downloads them to pdfs/bta-1/ and pdfs/bta-2/ respectively.
Skips files already downloaded (by filename + size > 1 KB).

Usage:
  python3 download_pdfs.py              # both BTA 1 and BTA 2
  python3 download_pdfs.py --bta 1      # BTA 1 only
  python3 download_pdfs.py --bta 2      # BTA 2 only
  python3 download_pdfs.py --dry-run    # print what would be downloaded
"""

import argparse
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}
DELAY = 0.5   # seconds between downloads
TIMEOUT = 120  # seconds per PDF
RETRIES = 3

BASE_DIR = Path(__file__).parent
BTA1_MD = BASE_DIR / "bta-1"
BTA2_MD = BASE_DIR / "bta-2"
BTA1_PDF = BASE_DIR / "pdfs" / "bta-1"
BTA2_PDF = BASE_DIR / "pdfs" / "bta-2"


def extract_pdf_links(md_path: Path) -> list[tuple[str, str]]:
    """Return list of (label, url) for all PDF links in a markdown stub."""
    content = md_path.read_text(encoding="utf-8")
    # Match markdown links: - [Label](url)
    links = re.findall(r"-\s*\[([^\]]+)\]\((https?://[^)]+\.pdf)\)", content, re.I)
    return links


def download_pdf(url: str, dest: Path) -> bool:
    """Download a PDF to dest. Returns True on success."""
    for attempt in range(RETRIES):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                data = resp.read()
            dest.write_bytes(data)
            return True
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return False
            if attempt == RETRIES - 1:
                return False
            time.sleep(2 ** attempt)
        except Exception:
            if attempt == RETRIES - 1:
                return False
            time.sleep(2 ** attempt)
    return False


def process_directory(md_dir: Path, pdf_dir: Path, dry_run: bool) -> tuple[int, int, int]:
    """Download PDFs for all stubs in md_dir. Returns (downloaded, skipped, failed)."""
    if not md_dir.exists():
        print(f"  Directory not found: {md_dir}")
        return 0, 0, 0

    pdf_dir.mkdir(parents=True, exist_ok=True)

    stubs = sorted(
        md_dir.glob("PB-*.md"),
        key=lambda f: int(re.search(r"PB-(\d+)", f.name).group(1))
    )

    downloaded = skipped = failed = 0
    total_with_pdf = 0

    for stub in stubs:
        links = extract_pdf_links(stub)
        if not links:
            continue
        total_with_pdf += 1

        for label, url in links:
            filename = url.split("/")[-1]
            dest = pdf_dir / filename

            # Skip if already downloaded and non-empty
            if dest.exists() and dest.stat().st_size > 1024:
                skipped += 1
                continue

            if dry_run:
                print(f"  [DRY RUN] {stub.name} → {filename}")
                downloaded += 1
                continue

            print(f"  [{stub.name}] {label[:40]} → {filename[:50]}...")
            ok = download_pdf(url, dest)
            if ok:
                size_kb = dest.stat().st_size // 1024
                print(f"    ✓ {size_kb} KB")
                downloaded += 1
            else:
                print(f"    ✗ FAILED: {url}")
                failed += 1
                if dest.exists() and dest.stat().st_size == 0:
                    dest.unlink()

            time.sleep(DELAY)

    print(f"  Stubs with PDFs: {total_with_pdf}/{len(stubs)}")
    return downloaded, skipped, failed


def main():
    parser = argparse.ArgumentParser(description="Download PDFs for scraped BTA bills")
    parser.add_argument("--bta", choices=["1", "2", "all"], default="all")
    parser.add_argument("--dry-run", action="store_true", help="List PDFs without downloading")
    args = parser.parse_args()

    total_dl = total_sk = total_fail = 0

    if args.bta in ("1", "all"):
        print(f"\nBTA 1 → {BTA1_PDF}")
        dl, sk, fail = process_directory(BTA1_MD, BTA1_PDF, args.dry_run)
        total_dl += dl; total_sk += sk; total_fail += fail
        print(f"  Downloaded: {dl} | Skipped: {sk} | Failed: {fail}")

    if args.bta in ("2", "all"):
        print(f"\nBTA 2 → {BTA2_PDF}")
        dl, sk, fail = process_directory(BTA2_MD, BTA2_PDF, args.dry_run)
        total_dl += dl; total_sk += sk; total_fail += fail
        print(f"  Downloaded: {dl} | Skipped: {sk} | Failed: {fail}")

    print(f"\nTotal — Downloaded: {total_dl} | Skipped: {total_sk} | Failed: {total_fail}")


if __name__ == "__main__":
    main()
