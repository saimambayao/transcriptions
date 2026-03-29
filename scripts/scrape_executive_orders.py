#!/usr/bin/env python3
"""
Scrape Philippine Executive Orders from lawphil.net.

Usage:
    python3 scripts/scrape_executive_orders.py --year 2024
    python3 scripts/scrape_executive_orders.py --generate-master-index
"""

import argparse
import os
import re
import sys
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md_convert
from urllib.parse import urljoin

OUTPUT_DIR = "/Users/saidamenmambayao/apps/transcriptions/legislation/executive-orders"
BASE_URL = "https://lawphil.net/executive/execord"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
})


def scrape_year_index(year):
    """Fetch year page and return list of (eo_number, url, title) tuples."""
    url = f"{BASE_URL}/eo{year}/eo{year}.html"
    results = []
    try:
        resp = session.get(url, timeout=30)
        resp.raise_for_status()

        # Extract EO links via regex
        matches = re.findall(rf'eo_(\d+)_{year}\.html', resp.text)
        seen = set()

        # Try to get titles from link text
        soup = None
        try:
            soup = BeautifulSoup(resp.text, "html.parser")
        except:
            pass

        for eo_num_str in matches:
            eo_num = int(eo_num_str)
            if eo_num in seen:
                continue
            seen.add(eo_num)

            filename = f"eo_{eo_num_str}_{year}.html"
            full_url = f"{BASE_URL}/eo{year}/{filename}"

            title = ""
            if soup:
                link = soup.find("a", href=re.compile(re.escape(filename)))
                if link:
                    title = link.get_text(strip=True)

            results.append((eo_num, full_url, title))

        print(f"  Found {len(results)} EOs for {year}")
    except Exception as e:
        print(f"  ERROR fetching year {year}: {e}")

    return results


def extract_eo_content(html):
    """Extract metadata and body from an EO page."""
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()

    # Title from <title> tag
    title = ""
    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.get_text(strip=True)

    # Long title from meta description
    long_title = ""
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc and meta_desc.get("content"):
        desc = meta_desc["content"].strip()
        desc = re.sub(r'^Executive Orders?\s*-\s*', '', desc, flags=re.IGNORECASE)
        long_title = desc

    # EO number + date from bracket text
    eo_number = ""
    date_signed = ""
    bracket = re.search(
        r'\[\s*(EXECUTIVE ORDER NO\.\s*\d+)\s*,\s*(\w+\s+\d{1,2},?\s*\d{4})\s*\]',
        text, re.IGNORECASE
    )
    if bracket:
        eo_number = bracket.group(1).strip()
        date_signed = bracket.group(2).strip()
    else:
        # Fallback
        eo_match = re.search(r'(Executive Order No\.\s*\d+)', text, re.IGNORECASE)
        if eo_match:
            eo_number = eo_match.group(1)

    # Body content via markdownify
    for tag in soup.find_all(['script', 'style', 'link', 'meta', 'img']):
        tag.decompose()

    blockquote = soup.find('blockquote') or soup.find('body')
    if not blockquote:
        return eo_number, long_title, date_signed, ""

    for hr in blockquote.find_all('hr'):
        hr.decompose()

    body_md = md_convert(
        str(blockquote),
        heading_style="ATX",
        bullets="-",
        strong_em_symbol="*",
        strip=['a'],
    )

    body_md = re.sub(r'\n{4,}', '\n\n\n', body_md)
    lines = [line.rstrip() for line in body_md.split('\n')]
    body_md = '\n'.join(lines).strip()
    body_md = re.sub(r'The Lawphil Project.*$', '', body_md, flags=re.MULTILINE | re.IGNORECASE)
    body_md = re.sub(r'Arellano Law Foundation.*$', '', body_md, flags=re.MULTILINE | re.IGNORECASE)

    return eo_number, long_title, date_signed, body_md.strip()


def save_eo(eo_num, eo_number_full, long_title, date_signed, body_text, source_url, year):
    """Save an EO as a markdown file."""
    year_dir = os.path.join(OUTPUT_DIR, str(year))
    os.makedirs(year_dir, exist_ok=True)
    filename = f"EO-{eo_num}.md"
    filepath = os.path.join(year_dir, filename)

    heading = eo_number_full if eo_number_full else f"Executive Order No. {eo_num}"

    lines = [f"# {heading}", ""]
    if long_title:
        lines.extend([f"**{long_title}**", ""])
    lines.extend(["## Metadata", ""])
    lines.append(f"- **EO Number**: {eo_num}")
    if date_signed:
        lines.append(f"- **Date**: {date_signed}")
    lines.append(f"- **Source**: [lawphil.net]({source_url})")
    lines.extend(["", "---", "", body_text, ""])

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return filepath


def scrape_eo(eo_num, url, year, retries=3):
    """Download and parse a single EO."""
    for attempt in range(retries):
        try:
            resp = session.get(url, timeout=30)
            resp.raise_for_status()

            eo_number_full, long_title, date_signed, body_text = extract_eo_content(resp.text)

            if not body_text or len(body_text) < 50:
                print(f"  WARNING: EO-{eo_num} has very short content ({len(body_text)} chars)")

            save_eo(eo_num, eo_number_full, long_title, date_signed, body_text, url, year)
            return (eo_num, eo_number_full, long_title, date_signed)

        except requests.exceptions.HTTPError:
            if resp.status_code == 404:
                print(f"  EO-{eo_num}: 404 Not Found - skipping")
                return None
            print(f"  EO-{eo_num}: HTTP {resp.status_code} (attempt {attempt + 1}/{retries})")
        except Exception as e:
            print(f"  EO-{eo_num}: Error - {e} (attempt {attempt + 1}/{retries})")

    print(f"  EO-{eo_num}: FAILED after {retries} attempts")
    return None


def generate_year_index(year, entries):
    """Generate INDEX.md for a year."""
    year_dir = os.path.join(OUTPUT_DIR, str(year))
    os.makedirs(year_dir, exist_ok=True)

    lines = [f"# Executive Orders — {year}", "", f"Total: {len(entries)} Executive Orders", ""]
    for eo_num, eo_number_full, long_title, date_signed in sorted(entries, key=lambda x: x[0], reverse=True):
        cn = eo_number_full if eo_number_full else f"Executive Order No. {eo_num}"
        t = f" — {long_title[:80]}" if long_title else ""
        lines.append(f"- [{cn}](EO-{eo_num}.md){t}")
    lines.append("")

    with open(os.path.join(year_dir, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  INDEX.md: {len(entries)} entries")


def generate_master_index():
    """Generate master INDEX.md."""
    lines = ["# Philippine Executive Orders Index", ""]
    grand_total = 0
    year_data = []

    for year in range(2026, 1986, -1):
        year_dir = os.path.join(OUTPUT_DIR, str(year))
        if not os.path.isdir(year_dir):
            continue
        count = len([f for f in os.listdir(year_dir) if f.endswith('.md') and f != 'INDEX.md'])
        if count > 0:
            year_data.append((year, count))
            grand_total += count

    lines.append(f"Total: {grand_total} Executive Orders (1987-2026)")
    lines.extend(["", "| Year | EOs |", "|------|-----|"])
    for year, count in year_data:
        lines.append(f"| [{year}]({year}/INDEX.md) | {count} |")
    lines.append("")

    with open(os.path.join(OUTPUT_DIR, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Master INDEX.md: {grand_total} EOs across {len(year_data)} years")


def main():
    parser = argparse.ArgumentParser(description="Scrape Executive Orders from lawphil.net")
    parser.add_argument("--year", type=int, help="Year to scrape")
    parser.add_argument("--generate-master-index", action="store_true")
    args = parser.parse_args()

    if args.generate_master_index:
        generate_master_index()
        return

    if not args.year:
        print("Error: --year required (or --generate-master-index)")
        sys.exit(1)

    year = args.year
    print(f"=== Scraping Executive Orders for {year} ===")
    os.makedirs(os.path.join(OUTPUT_DIR, str(year)), exist_ok=True)

    # Get EO list
    eo_list = scrape_year_index(year)
    if not eo_list:
        print("No EOs found!")
        sys.exit(1)

    entries = []
    success = failed = skipped = 0

    for i, (eo_num, url, link_title) in enumerate(sorted(eo_list, reverse=True), 1):
        filepath = os.path.join(OUTPUT_DIR, str(year), f"EO-{eo_num}.md")
        if os.path.exists(filepath) and os.path.getsize(filepath) > 500:
            print(f"  [{i}/{len(eo_list)}] EO-{eo_num}: exists - skipping")
            skipped += 1
            entries.append((eo_num, "", link_title, ""))
            continue

        print(f"  [{i}/{len(eo_list)}] EO-{eo_num}: downloading...")
        result = scrape_eo(eo_num, url, year)
        if result:
            entries.append(result)
            success += 1
        else:
            failed += 1

    generate_year_index(year, entries)

    print(f"\n=== DONE — {year} ===")
    print(f"  Success: {success}")
    print(f"  Skipped: {skipped}")
    print(f"  Failed: {failed}")
    print(f"  Total: {success + skipped + failed}")


if __name__ == "__main__":
    main()
