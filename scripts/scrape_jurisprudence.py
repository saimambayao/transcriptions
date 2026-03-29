#!/usr/bin/env python3
"""
Scrape Philippine Supreme Court jurisprudence from lawphil.net.

Usage:
    python3 scripts/scrape_jurisprudence.py --year 2024
    python3 scripts/scrape_jurisprudence.py --year 2024 --month jan
    python3 scripts/scrape_jurisprudence.py --generate-master-index
"""

import argparse
import os
import re
import sys
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md_convert
from urllib.parse import urljoin

OUTPUT_DIR = "/Users/saidamenmambayao/apps/transcriptions/jurisprudence"
BASE_URL = "https://lawphil.net/judjuris"
MONTHS = ["jan", "feb", "mar", "apr", "may", "jun",
          "jul", "aug", "sep", "oct", "nov", "dec"]
MONTH_NAMES = {
    "jan": "January", "feb": "February", "mar": "March", "apr": "April",
    "may": "May", "jun": "June", "jul": "July", "aug": "August",
    "sep": "September", "oct": "October", "nov": "November", "dec": "December"
}

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
})


def build_month_list(year):
    """Fetch year page and return list of active month abbreviations."""
    url = f"{BASE_URL}/juri{year}/juri{year}.html"
    try:
        resp = session.get(url, timeout=30)
        resp.raise_for_status()
        # Find month links in the HTML
        active = []
        for mon in MONTHS:
            pattern = rf'{mon}{year}/{mon}{year}\.html'
            if re.search(pattern, resp.text, re.IGNORECASE):
                active.append(mon)
        return active
    except Exception as e:
        print(f"  ERROR fetching year {year}: {e}")
        return []


def scrape_month_index(year, month):
    """Fetch month page and return list of (filename, url, title) tuples."""
    url = f"{BASE_URL}/juri{year}/{month}{year}/{month}{year}.html"
    results = []
    try:
        resp = session.get(url, timeout=30)
        resp.raise_for_status()

        # Extract decision links using regex (handles malformed HTML)
        # Match patterns like gr_262600_2024.html, am_ca-23-001-p_2024.html
        href_matches = re.findall(
            rf'href="?([^">\s]*?(?:gr|am|ac|bm|oca|udk|pet|sbc)_[^">\s]+_{year}\.html)"?',
            resp.text, re.IGNORECASE
        )

        seen = set()
        # Also try to get titles from <a> tags
        soup = None
        try:
            soup = BeautifulSoup(resp.text, "html.parser")
        except:
            pass

        for href in href_matches:
            # Normalize the href
            filename = os.path.basename(href)
            if filename in seen:
                continue
            seen.add(filename)

            full_url = f"{BASE_URL}/juri{year}/{month}{year}/{filename}"

            # Try to get title from the link text
            title = ""
            if soup:
                link = soup.find("a", href=re.compile(re.escape(filename)))
                if link:
                    title = link.get_text(strip=True)

            results.append((filename, full_url, title))

    except Exception as e:
        print(f"  ERROR fetching {month} {year}: {e}")

    return results


def sanitize_filename(href_filename, year):
    """Convert 'gr_262600_2024.html' -> 'GR-262600.md'"""
    # Remove .html
    name = re.sub(r'\.html$', '', href_filename, flags=re.IGNORECASE)
    # Remove year suffix
    name = re.sub(rf'_{year}$', '', name)
    # Split on first underscore
    parts = name.split('_', 1)
    case_type = parts[0].upper()
    identifier = parts[1].upper() if len(parts) > 1 else ""
    return f"{case_type}-{identifier}.md"


def extract_decision_content(html):
    """Extract metadata and body from a decision page."""
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()

    # --- Title from <title> tag ---
    title = ""
    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.get_text(strip=True)

    # --- Case number + date from bracket text ---
    case_number = ""
    date_decided = ""

    # Pattern: [ G.R. No. 262600, January 31, 2024 ]
    bracket = re.search(
        r'\[\s*([A-Z][A-Z\.\s]+No\.\s*[^\],]+?)\s*,\s*(\w+\s+\d{1,2},?\s*\d{4})\s*\]',
        text
    )
    if bracket:
        case_number = bracket.group(1).strip()
        date_decided = bracket.group(2).strip()
    else:
        # Fallback: look for case number in meta description or title
        meta_subj = soup.find("meta", attrs={"name": "subject"})
        if meta_subj and meta_subj.get("content"):
            subj = meta_subj["content"]
            cn_match = re.search(r'([A-Z][A-Z\.\s]+No\.\s*[\w\-]+)', subj)
            if cn_match:
                case_number = cn_match.group(1).strip()

    # --- Case title from meta description ---
    case_title = ""
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc and meta_desc.get("content"):
        desc = meta_desc["content"].strip()
        # Remove "Philippine Jurisprudence - " prefix if present
        desc = re.sub(r'^Philippine\s+Jurisprudence\s*-\s*', '', desc, flags=re.IGNORECASE)
        case_title = desc

    if not case_title and title:
        case_title = title

    # --- Division ---
    division = ""
    div_match = re.search(
        r'(FIRST|SECOND|THIRD|SPECIAL\s+FIRST|SPECIAL\s+SECOND|SPECIAL\s+THIRD)\s+DIVISION|EN\s+BANC',
        text
    )
    if div_match:
        division = div_match.group(0).strip()

    # --- Ponente ---
    ponente = ""
    # Look for "NAME, J.:" or "NAME, SAJ.:" or "NAME, CJ.:" on its own line
    pon_match = re.search(
        r'\n\s*([A-Z][A-Z\-]+(?:\s+[A-Z\-]+)*),\s*(?:Acting\s+)?(?:C\.?|SA)?J\.?\s*[:\.]?\s*\n',
        text
    )
    if pon_match:
        ponente = pon_match.group(1).strip().title() + ", J."
    elif re.search(r'PER\s+CURIAM', text):
        ponente = "Per Curiam"

    # --- Decision type ---
    decision_type = "Decision"
    if re.search(r'R\s*E\s*S\s*O\s*L\s*U\s*T\s*I\s*O\s*N', text):
        decision_type = "Resolution"

    # --- Body content ---
    for tag in soup.find_all(['script', 'style', 'link', 'meta', 'img']):
        tag.decompose()

    blockquote = soup.find('blockquote')
    if not blockquote:
        blockquote = soup.find('body')
    if not blockquote:
        return case_number, case_title, date_decided, ponente, division, decision_type, ""

    for hr in blockquote.find_all('hr'):
        hr.decompose()

    body_md = md_convert(
        str(blockquote),
        heading_style="ATX",
        bullets="-",
        strong_em_symbol="*",
        strip=['a'],
    )

    # Clean up
    body_md = re.sub(r'\n{4,}', '\n\n\n', body_md)
    lines = [line.rstrip() for line in body_md.split('\n')]
    body_md = '\n'.join(lines).strip()

    # Remove footer text
    body_md = re.sub(r'The Lawphil Project.*$', '', body_md, flags=re.MULTILINE | re.IGNORECASE)
    body_md = re.sub(r'Arellano Law Foundation.*$', '', body_md, flags=re.MULTILINE | re.IGNORECASE)

    return case_number, case_title, date_decided, ponente, division, decision_type, body_md.strip()


def save_decision(filename, case_number, case_title, date_decided, ponente,
                  division, decision_type, body_text, source_url, year):
    """Save a decision as a markdown file."""
    year_dir = os.path.join(OUTPUT_DIR, str(year))
    os.makedirs(year_dir, exist_ok=True)
    filepath = os.path.join(year_dir, filename)

    heading = case_number if case_number else filename.replace('.md', '')

    lines = []
    lines.append(f"# {heading}")
    lines.append("")
    if case_title:
        lines.append(f"**{case_title}**")
        lines.append("")
    lines.append("## Metadata")
    lines.append("")
    if case_number:
        lines.append(f"- **Case Number**: {case_number}")
    if case_title:
        lines.append(f"- **Case Title**: {case_title}")
    if date_decided:
        lines.append(f"- **Date**: {date_decided}")
    if ponente:
        lines.append(f"- **Ponente**: {ponente}")
    if division:
        lines.append(f"- **Division**: {division}")
    if decision_type:
        lines.append(f"- **Type**: {decision_type}")
    lines.append(f"- **Source**: [lawphil.net]({source_url})")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(body_text)
    lines.append("")

    content = "\n".join(lines)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def scrape_decision(filename, url, year, retries=3):
    """Download and parse a single decision."""
    for attempt in range(retries):
        try:
            resp = session.get(url, timeout=30)
            resp.raise_for_status()

            case_number, case_title, date_decided, ponente, division, decision_type, body_text = \
                extract_decision_content(resp.text)

            if not body_text or len(body_text) < 100:
                print(f"  WARNING: {filename} has very short content ({len(body_text)} chars)")

            md_filename = sanitize_filename(filename, year)
            save_decision(md_filename, case_number, case_title, date_decided,
                         ponente, division, decision_type, body_text, url, year)
            return md_filename, case_number, case_title, date_decided, ponente, division

        except requests.exceptions.HTTPError:
            if resp.status_code == 404:
                print(f"  {filename}: 404 Not Found - skipping")
                return None
            print(f"  {filename}: HTTP {resp.status_code} (attempt {attempt + 1}/{retries})")
        except Exception as e:
            print(f"  {filename}: Error - {e} (attempt {attempt + 1}/{retries})")

    print(f"  {filename}: FAILED after {retries} attempts")
    return None


def generate_year_index(year, decisions_by_month):
    """Generate INDEX.md for a single year."""
    year_dir = os.path.join(OUTPUT_DIR, str(year))
    os.makedirs(year_dir, exist_ok=True)

    total = sum(len(decs) for decs in decisions_by_month.values())

    lines = []
    lines.append(f"# Philippine Supreme Court Jurisprudence — {year}")
    lines.append("")
    lines.append(f"Total: {total} decisions")
    lines.append("")

    for mon in MONTHS:
        if mon not in decisions_by_month or not decisions_by_month[mon]:
            continue
        decs = decisions_by_month[mon]
        lines.append(f"## {MONTH_NAMES[mon]} {year} ({len(decs)} decisions)")
        lines.append("")
        for md_filename, case_number, case_title, date_decided, ponente, division in decs:
            cn = case_number if case_number else md_filename.replace('.md', '')
            title_short = case_title[:80] + "..." if case_title and len(case_title) > 80 else (case_title or "")
            pon = ponente if ponente else ""
            lines.append(f"- [{cn}]({md_filename}) — {title_short}")
        lines.append("")

    filepath = os.path.join(year_dir, "INDEX.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"  INDEX.md written: {total} decisions")


def generate_master_index():
    """Generate master INDEX.md across all years."""
    lines = []
    lines.append("# Philippine Supreme Court Jurisprudence Index")
    lines.append("")

    grand_total = 0
    year_counts = []

    for year in range(2025, 1986, -1):
        year_dir = os.path.join(OUTPUT_DIR, str(year))
        if not os.path.isdir(year_dir):
            continue
        count = len([f for f in os.listdir(year_dir)
                     if f.endswith('.md') and f != 'INDEX.md'])
        if count > 0:
            year_counts.append((year, count))
            grand_total += count

    lines.append(f"Total: {grand_total} decisions (1987-2025)")
    lines.append("")
    lines.append("| Year | Decisions |")
    lines.append("|------|-----------|")
    for year, count in year_counts:
        lines.append(f"| [{year}]({year}/INDEX.md) | {count} |")
    lines.append("")

    filepath = os.path.join(OUTPUT_DIR, "INDEX.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Master INDEX.md written: {grand_total} decisions across {len(year_counts)} years")


def main():
    parser = argparse.ArgumentParser(description="Scrape SC jurisprudence from lawphil.net")
    parser.add_argument("--year", type=int, help="Year to scrape (e.g., 2024)")
    parser.add_argument("--month", type=str, help="Specific month (e.g., jan)")
    parser.add_argument("--generate-master-index", action="store_true",
                        help="Generate master INDEX.md from existing year folders")
    args = parser.parse_args()

    if args.generate_master_index:
        generate_master_index()
        return

    if not args.year:
        print("Error: --year is required (or use --generate-master-index)")
        sys.exit(1)

    year = args.year
    print(f"=== Scraping jurisprudence for {year} ===")
    print(f"Output: {OUTPUT_DIR}/{year}/")
    print()

    os.makedirs(os.path.join(OUTPUT_DIR, str(year)), exist_ok=True)

    # Step 1: Get active months
    if args.month:
        active_months = [args.month.lower()]
        print(f"Scraping single month: {args.month}")
    else:
        print("Step 1: Finding active months...")
        active_months = build_month_list(year)
        print(f"  Active months: {active_months}")

    if not active_months:
        print("No active months found!")
        sys.exit(1)

    # Step 2-3: For each month, get decisions and scrape them
    decisions_by_month = {}
    total_success = 0
    total_failed = 0
    total_skipped = 0

    for month in active_months:
        print(f"\n--- {MONTH_NAMES.get(month, month)} {year} ---")
        entries = scrape_month_index(year, month)
        print(f"  Found {len(entries)} decisions")

        month_decisions = []

        for i, (filename, url, link_title) in enumerate(entries, 1):
            md_filename = sanitize_filename(filename, year)
            filepath = os.path.join(OUTPUT_DIR, str(year), md_filename)

            if os.path.exists(filepath) and os.path.getsize(filepath) > 500:
                print(f"  [{i}/{len(entries)}] {md_filename}: exists - skipping")
                total_skipped += 1
                # Still add to index
                month_decisions.append((md_filename, "", link_title, "", "", ""))
                continue

            print(f"  [{i}/{len(entries)}] {md_filename}: downloading...")
            result = scrape_decision(filename, url, year)

            if result:
                month_decisions.append(result)
                total_success += 1
            else:
                total_failed += 1

        decisions_by_month[month] = month_decisions

    # Step 4: Generate year INDEX.md
    print(f"\nGenerating INDEX.md for {year}...")
    generate_year_index(year, decisions_by_month)

    print(f"\n=== DONE — {year} ===")
    print(f"  Success: {total_success}")
    print(f"  Skipped (existing): {total_skipped}")
    print(f"  Failed: {total_failed}")
    total = total_success + total_skipped + total_failed
    print(f"  Total: {total}")


if __name__ == "__main__":
    main()
