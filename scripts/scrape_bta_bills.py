"""
scrape_bta_bills.py — Scrape all Bangsamoro Parliament proposed bills
Covers BTA 1 (2019-2022) and BTA 2 (2022-present).

Usage:
  python3 scripts/scrape_bta_bills.py --bta 1              # BTA 1 only
  python3 scripts/scrape_bta_bills.py --bta 2              # BTA 2 only (fills gaps)
  python3 scripts/scrape_bta_bills.py --bta all            # Both (default)
  python3 scripts/scrape_bta_bills.py --bta all --manifest-only
  python3 scripts/scrape_bta_bills.py --bta 2 --start 425 # BTA 2 bills from #425 up

Output:
  legislation/bills/scraped/bta-1/PB-{number}.md   (BTA 1 bills — metadata stubs)
  legislation/bills/scraped/bta-2/PB-{number}.md   (BTA 2 bills — metadata stubs, skips nothing)
  source-pdfs/bills/bta-1/{filename}.pdf            (BTA 1 PDFs)
  source-pdfs/bills/bta-2/{filename}.pdf            (BTA 2 PDFs)
  legislation/bills/bills_manifest.json             (full manifest)

Note: legislation/bills/proposed/ contains MANUALLY TRANSCRIBED bills — do NOT write there.
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from html.parser import HTMLParser

# ── Configuration ──────────────────────────────────────────────────────────── #

BASE_URL = "https://parliament.bangsamoro.gov.ph"
API_BTA1 = f"{BASE_URL}/wp-json/wp/v2/bta-bills"
API_BTA2 = f"{BASE_URL}/wp-json/wp/v2/bta-bills-22"

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent

OUT_BTA1 = REPO_ROOT / "legislation" / "bills" / "scraped" / "bta-1"
OUT_BTA2 = REPO_ROOT / "legislation" / "bills" / "scraped" / "bta-2"
PDF_BTA1 = REPO_ROOT / "source-pdfs" / "bills" / "bta-1"
PDF_BTA2 = REPO_ROOT / "source-pdfs" / "bills" / "bta-2"
MANIFEST_PATH = REPO_ROOT / "legislation" / "bills" / "bills_manifest.json"

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
REQUEST_DELAY = 0.3   # seconds between detail page fetches
PDF_DELAY = 0.5       # seconds between PDF downloads

# ── Helpers ─────────────────────────────────────────────────────────────────── #

def fetch(url: str, timeout: int = 20, retries: int = 3) -> bytes:
    """Fetch a URL with retries. Returns raw bytes."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)
        except Exception as e:
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)


def fetch_json(url: str) -> dict | list:
    return json.loads(fetch(url))


def html_to_text(html_fragment: str) -> str:
    """Strip HTML tags and decode common entities."""
    text = re.sub(r"<br\s*/?>", "\n", html_fragment, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    text = text.replace("&nbsp;", " ").replace("&#039;", "'").replace("&quot;", '"')
    # Numeric and named entities for em-dash, en-dash, etc.
    text = text.replace("&#8211;", "–").replace("&#8212;", "—")
    text = text.replace("&#8216;", "'").replace("&#8217;", "'")
    text = text.replace("&#8220;", """).replace("&#8221;", """)
    text = re.sub(r"&#\d+;", "", text)   # strip remaining numeric entities
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_tab_content(html: str, tab_index: int) -> str:
    """Extract the inner HTML of Divi tab N (0-indexed) from the page HTML.

    Divi nests <ul> and <p> inside et_pb_tab_content, so we cannot
    stop at the first </div>. Instead we find the opening <div class="et_pb_tab_content">
    and balance angle-brackets to find its closing tag.
    """
    # Locate the tab PANEL div (not the <li> nav item — both share the same class name).
    # We look specifically for the <div> variant, not the <li> variant.
    panel_marker = f'<div class="et_pb_tab et_pb_tab_{tab_index}_tb_body'
    tab_start = html.find(panel_marker)
    if tab_start == -1:
        return ""

    # Find the et_pb_tab_content div that follows
    content_start = html.find('<div class="et_pb_tab_content">', tab_start)
    if content_start == -1:
        return ""

    # Walk forward balancing div open/close to find the matching </div>
    inner_start = content_start + len('<div class="et_pb_tab_content">')
    depth = 1
    pos = inner_start
    while pos < len(html) and depth > 0:
        open_pos = html.find("<div", pos)
        close_pos = html.find("</div>", pos)
        if close_pos == -1:
            break
        if open_pos != -1 and open_pos < close_pos:
            depth += 1
            pos = open_pos + 4
        else:
            depth -= 1
            if depth == 0:
                return html[inner_start:close_pos]
            pos = close_pos + 6
    return html[inner_start:pos]


def parse_detail_page(html: str, url: str) -> dict:
    """Parse all structured data from a bill detail page."""
    result = {
        "url": url,
        "bill_number": None,
        "status": None,
        "as_of": None,
        "legislative_history": "",
        "committee_referrals": [],
        "baa_link": None,
        "baa_title": None,
        "principal_authors": [],
        "co_authors": [],
        "filed_copy_pdf": None,
        "second_reading_pdf": None,
        "committee_report_links": [],
        "attachment_links": [],
        "other_pdf_links": [],
    }

    # ── Tab 0: General Info ──
    tab0 = extract_tab_content(html, 0)
    if tab0:
        m = re.search(r"<strong>Bill Number:</strong>(\d+)", tab0)
        if m:
            result["bill_number"] = int(m.group(1))

        m = re.search(r"<strong>Bill Status:</strong>([^<\n]+)", tab0)
        if m:
            result["status"] = m.group(1).strip()

        m = re.search(r"<strong>As of:</strong>([^<\n]+)", tab0)
        if m:
            result["as_of"] = m.group(1).strip()

        # Legislative history block
        m = re.search(r"<strong>Legislative History:</strong>(.*?)(?:<strong>|</div>)", tab0, re.DOTALL)
        if m:
            result["legislative_history"] = html_to_text(m.group(1)).strip()

        # Committee referrals
        referrals = re.findall(r'class="cf-link"[^>]*href="([^"]+)"[^>]*>([^<]+)</a>', tab0)
        result["committee_referrals"] = [
            {"name": name.strip(), "url": href}
            for href, name in referrals
            if "committees" in href or "committee" in href.lower()
        ]

        # BAA link
        m = re.search(r'post_type=bta-acts[^"]*"[^>]*>([^<]+)</a>', tab0)
        if m:
            baa_link_m = re.search(r'href="([^"]+post_type=bta-acts[^"]*)"', tab0)
            result["baa_title"] = m.group(1).strip()
            if baa_link_m:
                result["baa_link"] = baa_link_m.group(1)

    # ── Tab 1: Authors ──
    tab1 = extract_tab_content(html, 1)
    if tab1:
        principal_m = re.search(
            r"<strong>Principal Author\(s\):</strong>(.*?)(?:<strong>Co-Author|</div>)",
            tab1, re.DOTALL
        )
        if principal_m:
            result["principal_authors"] = [
                name.strip()
                for name in re.findall(r"class=\"cf-link\"[^>]*>([^<]+)</a>", principal_m.group(1))
            ]

        coauth_m = re.search(
            r"<strong>Co-Author\(s\):</strong>(.*?)(?:</div>|$)", tab1, re.DOTALL
        )
        if coauth_m:
            result["co_authors"] = [
                name.strip()
                for name in re.findall(r"class=\"cf-link\"[^>]*>([^<]+)</a>", coauth_m.group(1))
            ]

    # ── Tab 2: Documents ──
    tab2 = extract_tab_content(html, 2)
    if tab2:
        # Filed copy PDF
        m = re.search(r"<strong>Filed Copy:</strong>\s*(?:<[^>]+>)*\s*<[^>]*href=\"([^\"]+)\"", tab2)
        if m:
            result["filed_copy_pdf"] = m.group(1)

        # Second reading PDF
        m = re.search(r"<strong>Second Reading Copy:</strong>\s*(?:<[^>]+>)*\s*<[^>]*href=\"([^\"]+)\"", tab2)
        if m:
            result["second_reading_pdf"] = m.group(1)

        # Committee report links
        result["committee_report_links"] = re.findall(
            r'post_type=committee_report[^"]*"', tab2
        )

        # All PDF links in tab2
        all_pdfs = re.findall(
            r'href="(https?://parliament\.bangsamoro\.gov\.ph/wp-content/uploads/[^"]+\.pdf)"',
            tab2, re.I
        )
        result["other_pdf_links"] = all_pdfs

    return result


def slugify_title(title: str) -> str:
    """Convert title to a filename-safe slug (max 80 chars)."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")[:80]
    return slug


def make_markdown(meta: dict, bill_record: dict, bta: int) -> str:
    """Generate metadata markdown stub for a bill."""
    # title may come from meta (already cleaned string) or from the REST API record (dict with "rendered" key)
    raw_title = bill_record.get("title", "")
    if isinstance(raw_title, dict):
        raw_title = raw_title.get("rendered", "")
    title = html_to_text(raw_title) if raw_title else meta.get("title", "")
    bill_number = meta.get("bill_number", "?")
    status = meta.get("status", "")
    as_of = meta.get("as_of", "")
    history = meta.get("legislative_history", "").strip()
    principal = ", ".join(meta.get("principal_authors", []))
    coauthors = ", ".join(meta.get("co_authors", []))
    filed_pdf = meta.get("filed_copy_pdf") or ""
    second_pdf = meta.get("second_reading_pdf") or ""
    source_url = meta.get("url", "")
    baa_title = meta.get("baa_title", "")
    baa_link = meta.get("baa_link", "")
    api_date = bill_record.get("date", "")[:10]

    bta_label = "1" if bta == 1 else "2"
    parliament_label = f"BANGSAMORO TRANSITION AUTHORITY {bta_label}"

    lines = [
        f"# BTA Parliament Bill No. {bill_number}",
        "",
        f"**{title}**",
        "",
        "---",
        "",
        f"**Parliament:** {parliament_label}",
        f"**Bill Number:** {bill_number}",
        f"**Status:** {status}",
        f"**As of:** {as_of or api_date}",
        "",
    ]

    if principal:
        lines += [f"**Principal Author(s):** {principal}", ""]
    if coauthors:
        lines += [f"**Co-Author(s):** {coauthors}", ""]

    lines += ["## Legislative History", ""]
    if history:
        for h_line in history.split("\n"):
            h_line = h_line.strip()
            if h_line:
                lines.append(h_line)
        lines.append("")
    else:
        lines += ["*(Not yet available)*", ""]

    lines += ["## Documents", ""]
    if filed_pdf:
        lines.append(f"- [Filed Copy (PDF)]({filed_pdf})")
    if second_pdf:
        lines.append(f"- [Second Reading Copy (PDF)]({second_pdf})")
    if not filed_pdf and not second_pdf:
        lines.append("*(No PDFs available)*")
    lines.append("")

    if baa_title:
        lines += [
            "## Enacted As",
            "",
            f"- [{baa_title}]({baa_link})" if baa_link else f"- {baa_title}",
            "",
        ]

    lines += [
        "---",
        "",
        f"*Source: [{source_url}]({source_url})*",
        "",
        "> **Note:** This is a metadata stub. Full bill text extraction pending PDF transcription.",
    ]

    return "\n".join(lines)


def generate_index(out_dir: Path, bta: int) -> None:
    """Regenerate INDEX.md for a bills directory."""
    files = sorted(out_dir.glob("PB-*.md"), key=lambda f: int(re.search(r"PB-(\d+)", f.name).group(1)))
    bta_label = "BTA 1 (2019-2022)" if bta == 1 else "BTA 2 (2022-Present)"

    lines = [
        f"# Bangsamoro Parliament Bills — {bta_label}",
        "",
        f"Total: **{len(files)} bills**",
        "",
        "| Bill No. | Title | Status |",
        "|----------|-------|--------|",
    ]

    for f in files:
        content = f.read_text(encoding="utf-8")
        title_m = re.search(r"^# BTA Parliament Bill No\. \d+\s*\n\n\*\*(.*?)\*\*", content, re.M)
        title = title_m.group(1).strip() if title_m else "(unknown)"
        num_m = re.search(r"PB-(\d+)", f.name)
        num = num_m.group(1) if num_m else "?"
        status_m = re.search(r"\*\*Status:\*\* (.+)", content)
        status = status_m.group(1).strip() if status_m else ""
        lines.append(f"| [{num}]({f.name}) | {title[:80]} | {status} |")

    (out_dir / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  INDEX.md updated: {len(files)} entries")


# ── REST API fetching ────────────────────────────────────────────────────────── #

def fetch_all_bills_from_api(api_url: str, label: str) -> list[dict]:
    """Fetch all bills from a WP REST API endpoint (paginated)."""
    all_bills = []
    page = 1
    while True:
        url = f"{api_url}?per_page=100&page={page}&_fields=id,date,modified,title,link,status,legislative_doc_status,bta_session"
        try:
            raw = fetch(url)
            resp_data = json.loads(raw)
            if not resp_data:
                break
            all_bills.extend(resp_data)
            # Parse total pages from response headers (can't easily do with urlopen but 100/page is fine)
            if len(resp_data) < 100:
                break
            page += 1
            time.sleep(0.2)
        except urllib.error.HTTPError as e:
            if e.code == 400:
                break  # No more pages
            raise
    print(f"  {label}: fetched {len(all_bills)} bills from REST API")
    return all_bills


# ── Main scraping logic ──────────────────────────────────────────────────────── #

def scrape_bills(bta_filter: str, manifest_only: bool, start_bill: int) -> None:
    """Main entry point for scraping."""

    # Create output dirs
    for d in [OUT_BTA1, OUT_BTA2, PDF_BTA1, PDF_BTA2, MANIFEST_PATH.parent]:
        d.mkdir(parents=True, exist_ok=True)

    # Load existing manifest if any
    manifest = {}
    if MANIFEST_PATH.exists():
        try:
            manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        except Exception:
            manifest = {}

    if "bta1" not in manifest:
        manifest["bta1"] = {}
    if "bta2" not in manifest:
        manifest["bta2"] = {}

    # ── Fetch bill lists ──
    print("\n[1/4] Fetching bill lists from REST API...")

    if bta_filter in ("1", "all"):
        bta1_api_bills = fetch_all_bills_from_api(API_BTA1, "BTA 1 (bta-bills)")
        # Filter: only pre-Oct 2022 are real BTA 1 bills
        bta1_bills = [b for b in bta1_api_bills if b["date"] < "2022-10-01"]
        print(f"  BTA 1 after date filter: {len(bta1_bills)} bills")
    else:
        bta1_bills = []

    if bta_filter in ("2", "all"):
        bta2_bills = fetch_all_bills_from_api(API_BTA2, "BTA 2 (bta-bills-22)")
    else:
        bta2_bills = []

    # ── Scrape detail pages ──
    print(f"\n[2/4] Scraping detail pages...")

    def process_bill_list(bills: list[dict], bta: int, out_dir: Path, pdf_dir: Path) -> int:
        scraped = 0
        skipped = 0
        errors = 0
        total = len(bills)

        for i, bill in enumerate(bills, 1):
            bill_url = bill["link"]
            bill_id = str(bill["id"])
            title = bill["title"]["rendered"]
            title_clean = html_to_text(title)

            # Check if already in manifest with detail data
            manifest_key = "bta1" if bta == 1 else "bta2"
            if bill_id in manifest[manifest_key] and manifest[manifest_key][bill_id].get("bill_number"):
                existing = manifest[manifest_key][bill_id]
                bill_num = existing.get("bill_number")
                if bill_num and bill_num >= start_bill:
                    md_file = out_dir / f"PB-{bill_num}.md"
                    if md_file.exists() and not (bta == 2 and bill_num >= start_bill):
                        skipped += 1
                        continue

            print(f"  [{i}/{total}] BTA{bta} | {title_clean[:55]}...")

            # Fetch detail page
            try:
                html = fetch(bill_url).decode("utf-8", errors="replace")
                time.sleep(REQUEST_DELAY)
            except urllib.error.HTTPError as e:
                print(f"    SKIP (HTTP {e.code})")
                errors += 1
                continue
            except Exception as e:
                print(f"    ERROR: {e}")
                errors += 1
                continue

            # Parse detail
            meta = parse_detail_page(html, bill_url)
            meta["title"] = title_clean
            meta["api_date"] = bill["date"][:10]

            # Merge into manifest
            manifest[manifest_key][bill_id] = {
                **bill,
                "title": title_clean,
                **meta,
            }

            bill_num = meta.get("bill_number")
            if not bill_num:
                print(f"    WARNING: No bill number found at {bill_url}")
                continue

            # Skip BTA 2 bills below start threshold
            if bta == 2 and bill_num < start_bill:
                skipped += 1
                continue

            # Check if markdown already exists
            md_file = out_dir / f"PB-{bill_num}.md"
            if md_file.exists():
                skipped += 1
                continue

            # Generate markdown (pass meta as bill_record so title is already a clean string)
            if not manifest_only:
                md_content = make_markdown(meta, meta, bta)
                md_file.write_text(md_content, encoding="utf-8")
                scraped += 1

                # Download PDFs
                pdfs_to_download = []
                if meta.get("filed_copy_pdf"):
                    pdfs_to_download.append(("filed", meta["filed_copy_pdf"]))
                if meta.get("second_reading_pdf"):
                    pdfs_to_download.append(("second-reading", meta["second_reading_pdf"]))

                for pdf_type, pdf_url in pdfs_to_download:
                    filename = pdf_url.split("/")[-1]
                    pdf_path = pdf_dir / filename
                    if pdf_path.exists() and pdf_path.stat().st_size > 1000:
                        continue
                    try:
                        pdf_data = fetch(pdf_url, timeout=60)
                        pdf_path.write_bytes(pdf_data)
                        print(f"    PDF saved: {filename}")
                        time.sleep(PDF_DELAY)
                    except Exception as e:
                        print(f"    PDF ERROR ({pdf_type}): {e}")

        print(f"  Done: {scraped} new, {skipped} skipped, {errors} errors")
        return scraped

    new_bta1 = 0
    new_bta2 = 0

    if bta1_bills:
        print(f"\n  Processing {len(bta1_bills)} BTA 1 bills → {OUT_BTA1}")
        new_bta1 = process_bill_list(bta1_bills, 1, OUT_BTA1, PDF_BTA1)

    if bta2_bills:
        print(f"\n  Processing {len(bta2_bills)} BTA 2 bills → {OUT_BTA2}")
        new_bta2 = process_bill_list(bta2_bills, 2, OUT_BTA2, PDF_BTA2)

    # ── Save manifest ──
    print(f"\n[3/4] Saving manifest to {MANIFEST_PATH}...")
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  BTA 1 entries: {len(manifest['bta1'])}")
    print(f"  BTA 2 entries: {len(manifest['bta2'])}")

    # ── Update INDEX files ──
    print(f"\n[4/4] Updating INDEX.md files...")
    if list(OUT_BTA1.glob("PB-*.md")):
        generate_index(OUT_BTA1, 1)
    if list(OUT_BTA2.glob("PB-*.md")):
        generate_index(OUT_BTA2, 2)

    print(f"\nDone. New files: {new_bta1} BTA1 + {new_bta2} BTA2")


# ── CLI ──────────────────────────────────────────────────────────────────────── #

def main():
    parser = argparse.ArgumentParser(
        description="Scrape all Bangsamoro Parliament proposed bills (BTA 1 & BTA 2)"
    )
    parser.add_argument(
        "--bta", choices=["1", "2", "all"], default="all",
        help="Which parliament to scrape (default: all)"
    )
    parser.add_argument(
        "--manifest-only", action="store_true",
        help="Only generate manifest JSON, do not write markdown or download PDFs"
    )
    parser.add_argument(
        "--start", type=int, default=1,
        help="For BTA 2: only process bills with bill number >= START (default: 1)"
    )
    args = parser.parse_args()

    print(f"BTA Bills Scraper")
    print(f"  Parliament: {args.bta}")
    print(f"  Manifest only: {args.manifest_only}")
    if args.bta in ("2", "all"):
        print(f"  BTA 2 start from bill #: {args.start}")

    scrape_bills(
        bta_filter=args.bta,
        manifest_only=args.manifest_only,
        start_bill=args.start,
    )


if __name__ == "__main__":
    main()
