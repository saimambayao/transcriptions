"""
retranscribe_all.py — Re-transcribe all BTA bills using /transcriber workflow.

For each bill in pdf_map.json:
  1. assess_pdf.py  — determine OCR vs embedded-text method
  2. extract_chapter.py (scanned) or extract_text_only.py (text-based) — extract
  3. inject into stub (force-overwrite existing stub marker OR ## Full Text)

Usage (run from repo root):
  python3 scripts/retranscribe_all.py              # all 563 bills
  python3 scripts/retranscribe_all.py --bta 1      # BTA 1 only
  python3 scripts/retranscribe_all.py --bta 2      # BTA 2 only
  python3 scripts/retranscribe_all.py --dry-run    # list bills + method, no extraction
  python3 scripts/retranscribe_all.py --workers 4  # parallel workers (default: 4)

Transcriber scripts used:
  ~/.claude/skills/transcriber/scripts/assess_pdf.py
  ~/.claude/skills/transcriber/scripts/extract_chapter.py   (OCR, scanned)
  ~/.claude/skills/transcriber/scripts/extract_text_only.py (embedded text)
"""

import argparse
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent.parent  # repo root
MAP_PATH = BASE_DIR / "legislation" / "bills" / "scraped" / "pdf_map.json"
TRANSCRIBER = Path.home() / ".claude" / "skills" / "transcriber" / "scripts"

# Import assess_pdf directly — fast, pure Python + fitz
if str(TRANSCRIBER) not in sys.path:
    sys.path.insert(0, str(TRANSCRIBER))
from assess_pdf import assess_pdf  # noqa: E402

STUB_MARKER = "> **Note:** This is a metadata stub"
FULL_TEXT_HEADING = "## Full Text"


# ── Extraction ─────────────────────────────────────────────────────────────────

def extract(pdf_path: str, total_pages: int, method: str, output_path: str) -> tuple[bool, str]:
    """Run the appropriate transcriber extraction script via subprocess."""
    script = TRANSCRIBER / (
        "extract_chapter.py" if method == "ocr" else "extract_text_only.py"
    )
    env = {**os.environ, "PATH": "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"}
    result = subprocess.run(
        [sys.executable, str(script), pdf_path, "1", str(total_pages), output_path],
        capture_output=True, text=True, env=env, timeout=900
    )
    return result.returncode == 0, result.stderr.strip()


# ── Injection (force overwrite) ────────────────────────────────────────────────

def inject_force(md_path: Path, extracted_text: str) -> None:
    """Replace stub marker or existing ## Full Text section with fresh extraction."""
    content = md_path.read_text(encoding="utf-8")

    # Find cut point: prefer stub marker, fall back to ## Full Text heading
    cut = content.find(STUB_MARKER)
    if cut == -1:
        m = re.search(r'(?m)^## Full Text\b', content)
        cut = m.start() if m else -1

    if cut != -1:
        base = content[:cut].rstrip()
    else:
        base = content.rstrip()

    new_content = base + "\n\n## Full Text\n\n" + extracted_text.strip() + "\n"
    md_path.write_text(new_content, encoding="utf-8")


# ── Worker ─────────────────────────────────────────────────────────────────────

def process_bill(uid: str, data: dict) -> str:
    """Assess → extract → inject one bill. Returns a one-line status string."""
    pdf_path = BASE_DIR / data["pdf_path"]
    md_path  = BASE_DIR / data["md_path"]
    tmp_out  = f"/tmp/{uid}_retranscribe.txt"

    if not pdf_path.exists():
        return f"✗ {uid}: PDF not found ({data['pdf_path']})"

    try:
        # 1. Assess
        info   = assess_pdf(str(pdf_path))
        method = "text" if info["has_embedded_text"] else "ocr"
        pages  = info["total_pages"]

        # 2. Extract
        ok, err = extract(str(pdf_path), pages, method, tmp_out)
        if not ok:
            return f"✗ {uid}: extraction failed [{method}, {pages}pp] — {err[:120]}"

        text = Path(tmp_out).read_text(encoding="utf-8", errors="replace").strip()
        if not text:
            return f"✗ {uid}: empty output [{method}, {pages}pp]"

        # 3. Inject (force)
        inject_force(md_path, text)
        return f"✓ {uid}: {pages}pp [{method}]"

    except Exception as exc:
        return f"✗ {uid}: {exc}"


# ── Main ───────────────────────────────────────────────────────────────────────

def fix_stale_paths(map_data: dict) -> int:
    """Fix known stale PDF paths in pdf_map.json. Returns count of fixes."""
    fixes = {
        "BTA1-PB-52": ("BILL-NO.-52.pdf", "Bill-No.-52.pdf"),
    }
    count = 0
    for uid, (old_suffix, new_suffix) in fixes.items():
        if uid not in map_data:
            continue
        old_path = map_data[uid]["pdf_path"]
        if old_suffix in old_path:
            new_path = old_path.replace(old_suffix, new_suffix)
            if (BASE_DIR / new_path).exists():
                map_data[uid]["pdf_path"] = new_path
                print(f"  Fixed {uid}: {old_suffix} → {new_suffix}")
                count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description="Re-transcribe all BTA bills from source PDFs")
    parser.add_argument("--bta", choices=["1", "2", "all"], default="all",
                        help="Which parliament session to process (default: all)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print bill list and assessed method without extracting")
    parser.add_argument("--workers", type=int, default=4,
                        help="Parallel workers (default: 4)")
    args = parser.parse_args()

    # Load map
    map_data = json.loads(MAP_PATH.read_text(encoding="utf-8"))

    # Fix stale paths before running
    print("Checking for stale pdf_map.json paths...")
    fixed = fix_stale_paths(map_data)
    if fixed:
        MAP_PATH.write_text(json.dumps(map_data, indent=2, ensure_ascii=False) + "\n",
                            encoding="utf-8")
        print(f"  Saved {fixed} fix(es) to pdf_map.json")
    else:
        print("  No stale paths found.")

    # Filter by BTA
    bills = []
    for uid, data in map_data.items():
        parl = data["parliament"]
        if args.bta == "1" and parl != "bta-1":
            continue
        if args.bta == "2" and parl != "bta-2":
            continue
        bills.append((uid, data))

    print(f"\nBills to retranscribe: {len(bills)}")

    if args.dry_run:
        print("\n[DRY RUN] Assessing PDFs...")
        ocr_count = text_count = missing = 0
        for uid, data in bills:
            pdf_path = BASE_DIR / data["pdf_path"]
            if not pdf_path.exists():
                print(f"  ✗ {uid}: PDF missing")
                missing += 1
                continue
            info = assess_pdf(str(pdf_path))
            method = "text" if info["has_embedded_text"] else "ocr"
            if method == "text":
                text_count += 1
            else:
                ocr_count += 1
            print(f"  {uid}: {info['total_pages']}pp [{method}]")
        print(f"\nSummary: {ocr_count} OCR | {text_count} text | {missing} missing")
        return

    # Run
    succeeded = failed = 0
    failed_list = []

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(process_bill, uid, data): uid for uid, data in bills}
        for future in as_completed(futures):
            result = future.result()
            print(result)
            if result.startswith("✓"):
                succeeded += 1
            else:
                failed += 1
                failed_list.append(result)

    print(f"\n{'='*60}")
    print(f"Retranscription complete")
    print(f"  ✓ Succeeded: {succeeded}")
    print(f"  ✗ Failed:    {failed}")

    if failed_list:
        print("\nFailed bills:")
        for line in sorted(failed_list):
            print(f"  {line}")

    print("\nRun audit:  python3 scripts/audit_transcriptions.py")


if __name__ == "__main__":
    main()
