#!/usr/bin/env python3
"""
Scrape Republic Acts from lawphil.net and save as markdown files.

Usage:
    python3 scripts/scrape_lawphil.py --start-ra 12000 --end-ra 12115
    python3 scripts/scrape_lawphil.py --start-ra 9000 --end-ra 9200
"""

import argparse
import os
import re
import sys
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import urljoin

OUTPUT_DIR = "/Users/saidamenmambayao/apps/transcriptions/legislation/national-laws"
BASE_URL = "https://lawphil.net/statutes/repacts"
YEARS = list(range(1946, 2026))

# Widened RA ranges per year — overlapping to catch edge cases
YEAR_RA_RANGES = {
    1946: (1, 100),
    1947: (80, 200),
    1948: (190, 350),
    1949: (340, 430),
    1950: (420, 600),
    1951: (580, 680),
    1952: (670, 840),
    1953: (830, 980),
    1954: (970, 1210),
    1955: (1200, 1420),
    1956: (1400, 1620),
    1957: (1610, 2060),
    1958: (2040, 2100),
    1959: (2090, 2620),
    1960: (2610, 3030),
    1961: (3010, 3460),
    1962: (3440, 3520),
    1963: (3500, 3860),
    1964: (3840, 4180),
    1965: (4170, 4650),
    1966: (4640, 4870),
    1967: (4860, 5200),
    1968: (5180, 5460),
    1969: (5450, 6130),
    1970: (6120, 6180),
    1971: (6160, 6430),
    1972: (6420, 6640),
    1974: (6420, 6440),
    1987: (6630, 6700),
    1988: (6630, 6700),
    1989: (6680, 6850),
    1990: (6820, 7000),
    1991: (6950, 7200),
    1992: (7100, 7600),
    1993: (7550, 7650),
    1994: (7600, 7850),
    1995: (7800, 8200),
    1996: (8100, 8250),
    1997: (8150, 8450),
    1998: (8350, 8750),
    1999: (8700, 8800),
    2000: (8750, 9050),
    2001: (8900, 9200),
    2002: (9100, 9370),
    2003: (9150, 9420),
    2004: (9200, 9500),
    2005: (9250, 9530),
    2006: (9300, 9550),
    2007: (9350, 9600),
    2008: (9450, 9700),
    2009: (9500, 9910),
    2010: (9850, 10200),
    2011: (10100, 10200),
    2012: (10100, 10400),
    2013: (10300, 10700),
    2014: (10600, 10700),
    2015: (10600, 10800),
    2016: (10700, 10970),
    2017: (10900, 11000),
    2018: (10900, 11200),
    2019: (11100, 11500),
    2020: (11400, 11560),
    2021: (11500, 11700),
    2022: (11600, 11960),
    2023: (11900, 12000),
    2024: (11950, 12200),
    2025: (12100, 12300),
}

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
})


def get_relevant_years(start_ra, end_ra):
    """Return years whose RA ranges overlap with the requested range."""
    relevant = []
    for year in YEARS:
        yr_min, yr_max = YEAR_RA_RANGES.get(year, (0, 99999))
        if yr_max >= start_ra and yr_min <= end_ra:
            relevant.append(year)
    return relevant


def scrape_year_index(year):
    """Scrape a year's index page and return list of (ra_number, url) tuples."""
    url = f"{BASE_URL}/ra{year}/ra{year}.html"
    results = []
    try:
        resp = session.get(url, timeout=30)
        resp.raise_for_status()

        # Use regex directly on HTML (handles malformed pages like 2025)
        matches = re.findall(r'ra_(\d+)_(\d{4})\.html', resp.text)
        seen = set()
        for ra_str, yr_str in matches:
            ra_num = int(ra_str)
            if ra_num not in seen:
                seen.add(ra_num)
                full_url = f"{BASE_URL}/ra{yr_str}/ra_{ra_str}_{yr_str}.html"
                results.append((ra_num, full_url))

        print(f"  Year {year}: found {len(results)} RAs")
    except Exception as e:
        print(f"  Year {year}: ERROR - {e}")

    return results


def extract_law_content(html):
    """Extract structured law content from HTML using markdownify."""
    soup = BeautifulSoup(html, "html.parser")

    # --- Extract metadata from <meta> tags and bracket text ---
    title = ""
    long_title = ""
    date_signed = ""

    # Get title from <title> tag
    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.get_text(strip=True)

    # Get long title from meta description
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc and meta_desc.get("content"):
        desc = meta_desc["content"]
        # Remove "Republic Acts - " prefix
        desc = re.sub(r'^Republic Acts?\s*-\s*', '', desc, flags=re.IGNORECASE)
        if desc:
            long_title = desc.strip()

    # Get date from the bracket text e.g. [ REPUBLIC ACT NO. 12066, November 08, 2024 ]
    bracket_p = soup.find("p", class_="cb")
    if bracket_p:
        bracket_text = bracket_p.get_text(strip=True)
        date_match = re.search(r',\s*(\w+\s+\d{1,2},?\s*\d{4})', bracket_text)
        if date_match:
            date_signed = date_match.group(1).strip()

    # --- Extract body content ---
    # Remove non-content elements
    for tag in soup.find_all(['script', 'style', 'link', 'meta', 'gcse:searchbox-only']):
        tag.decompose()

    # Remove images
    for img in soup.find_all('img'):
        img.decompose()

    # Find the main blockquote content (where law text lives)
    blockquote = soup.find('blockquote')
    if not blockquote:
        # Fallback: use body
        blockquote = soup.find('body')

    if not blockquote:
        return title, long_title, date_signed, ""

    # Remove the navigation/menu bars (they're in tables before the HR)
    # Remove <hr> tags
    for hr in blockquote.find_all('hr'):
        hr.decompose()

    # Convert to markdown using markdownify
    body_md = md(
        str(blockquote),
        heading_style="ATX",
        bullets="-",
        strong_em_symbol="*",
        strip=['a'],  # strip link tags but keep text
    )

    # --- Clean up the markdown ---
    # Remove the bracket title line (already captured in metadata)
    body_md = re.sub(r'^\s*\[?\s*REPUBLIC ACT NO\.\s*\d+.*?\]\s*$', '', body_md, flags=re.MULTILINE | re.IGNORECASE)

    # Remove the "AN ACT..." line if it duplicates long_title (already in metadata)
    # But keep it if there's no long_title
    # Actually, keep it in the body — it's part of the law text

    # Clean up excessive blank lines
    body_md = re.sub(r'\n{4,}', '\n\n\n', body_md)

    # Clean up leading/trailing whitespace per line
    lines = body_md.split('\n')
    lines = [line.rstrip() for line in lines]
    body_md = '\n'.join(lines).strip()

    # Remove any leftover navigation text
    body_md = re.sub(r'The Lawphil Project.*$', '', body_md, flags=re.MULTILINE | re.IGNORECASE)
    body_md = re.sub(r'Arellano Law Foundation.*$', '', body_md, flags=re.MULTILINE | re.IGNORECASE)

    return title, long_title, date_signed, body_md.strip()


def save_ra(ra_num, title, long_title, date_signed, body_text, source_url):
    """Save a Republic Act as a markdown file."""
    filename = f"RA-{ra_num}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    lines = []
    lines.append(f"# Republic Act No. {ra_num}")
    lines.append("")

    if long_title:
        lines.append(f"**{long_title}**")
        lines.append("")

    lines.append("## Metadata")
    lines.append("")
    lines.append(f"- **RA Number**: {ra_num}")
    if date_signed:
        lines.append(f"- **Date Signed**: {date_signed}")
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


def scrape_ra(ra_num, url, retries=3):
    """Download and parse a single RA page."""
    for attempt in range(retries):
        try:
            resp = session.get(url, timeout=30)
            resp.raise_for_status()

            title, long_title, date_signed, body_text = extract_law_content(resp.text)

            if not body_text or len(body_text) < 100:
                print(f"  WARNING: RA-{ra_num} has very short content ({len(body_text)} chars)")

            save_ra(ra_num, title, long_title, date_signed, body_text, url)
            return True

        except requests.exceptions.HTTPError:
            if resp.status_code == 404:
                print(f"  RA-{ra_num}: 404 Not Found - skipping")
                return False
            print(f"  RA-{ra_num}: HTTP {resp.status_code} (attempt {attempt + 1}/{retries})")
        except Exception as e:
            print(f"  RA-{ra_num}: Error - {e} (attempt {attempt + 1}/{retries})")

    print(f"  RA-{ra_num}: FAILED after {retries} attempts")
    return False


def main():
    parser = argparse.ArgumentParser(description="Scrape Republic Acts from lawphil.net")
    parser.add_argument("--start-ra", type=int, required=True, help="Starting RA number (highest)")
    parser.add_argument("--end-ra", type=int, required=True, help="Ending RA number (lowest)")
    args = parser.parse_args()

    start_ra = args.start_ra
    end_ra = args.end_ra

    print(f"=== Scraping RAs {start_ra} down to {end_ra} ===")
    print(f"Output: {OUTPUT_DIR}")
    print()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Step 1: Build RA -> URL mapping from year index pages
    print("Step 1: Building RA index from year pages...")
    ra_map = {}

    relevant_years = get_relevant_years(end_ra, start_ra)
    print(f"  Checking years: {relevant_years}")

    for year in relevant_years:
        entries = scrape_year_index(year)
        for ra_num, url in entries:
            if end_ra <= ra_num <= start_ra:
                ra_map[ra_num] = url

    print(f"\nFound {len(ra_map)} RAs in range {end_ra}-{start_ra}")

    if not ra_map:
        print("No RAs found! Check the year ranges.")
        sys.exit(1)

    # Step 2: Download each RA (from highest to lowest)
    print(f"\nStep 2: Downloading {len(ra_map)} RAs...")
    sorted_ras = sorted(ra_map.keys(), reverse=True)

    success = 0
    failed = 0
    skipped = 0

    for i, ra_num in enumerate(sorted_ras, 1):
        filepath = os.path.join(OUTPUT_DIR, f"RA-{ra_num}.md")
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            if size > 500:
                print(f"  [{i}/{len(sorted_ras)}] RA-{ra_num}: already exists ({size} bytes) - skipping")
                skipped += 1
                continue

        url = ra_map[ra_num]
        print(f"  [{i}/{len(sorted_ras)}] RA-{ra_num}: downloading...")

        if scrape_ra(ra_num, url):
            success += 1
        else:
            failed += 1

    print(f"\n=== DONE ===")
    print(f"  Success: {success}")
    print(f"  Skipped (existing): {skipped}")
    print(f"  Failed: {failed}")
    print(f"  Total in range: {len(sorted_ras)}")


if __name__ == "__main__":
    main()
