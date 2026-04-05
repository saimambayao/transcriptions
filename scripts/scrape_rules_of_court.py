#!/usr/bin/env python3
"""
Scrape Rules of Court from lawphil.net and save as markdown files.

Usage:
    python3 scripts/scrape_rules_of_court.py

Sources:
    - Civil Procedure (Rules 1-35): am_19-10-20-sc_2019.html (2019 Amendments)
    - Civil Procedure (Rules 36-71): rc_1-71_civil.html
    - Criminal Procedure (Rules 110-127): rc_110-127_crim.html
    - Evidence (Rules 128-133): am_19-08-15-sc_2019.html (2019 Amendments)
    - Evidence (Rule 134): rc_128-134_evidence.html
    - Special Proceedings (Rules 72-109): rc_72-109_sp.html (if available)
"""

import os
import sys
import time
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

OUTPUT_DIR = "/Users/saidamenmambayao/apps/transcriptions/legislation/rules-of-court"
BASE_URL = "https://lawphil.net/courts/rules"

PAGES = [
    {
        "url": f"{BASE_URL}/am_19-10-20-sc_2019.html",
        "filename": "civil-procedure-rules-1-35.md",
        "title": "Rules of Civil Procedure (Rules 1-35) — 2019 Amendments (AM No. 19-10-20-SC)",
    },
    {
        "url": f"{BASE_URL}/rc_1-71_civil.html",
        "filename": "civil-procedure-rules-36-71.md",
        "title": "Rules of Civil Procedure (Rules 36-71)",
    },
    {
        "url": f"{BASE_URL}/rc_110-127_crim.html",
        "filename": "criminal-procedure-rules-110-127.md",
        "title": "Revised Rules of Criminal Procedure (Rules 110-127)",
    },
    {
        "url": f"{BASE_URL}/am_19-08-15-sc_2019.html",
        "filename": "evidence-rules-128-133.md",
        "title": "Revised Rules on Evidence (Rules 128-133) — 2019 Amendments (AM No. 19-08-15-SC)",
    },
    {
        "url": f"{BASE_URL}/rc_128-134_evidence.html",
        "filename": "evidence-rule-134.md",
        "title": "Rules on Evidence (Rule 134) — Perpetuation of Testimony",
    },
    {
        "url": f"{BASE_URL}/rc_72-109_sp.html",
        "filename": "special-proceedings-rules-72-109.md",
        "title": "Rules on Special Proceedings (Rules 72-109)",
    },
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}


def scrape_page(page):
    url = page["url"]
    filename = page["filename"]
    title = page["title"]

    print(f"Fetching: {url}")
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"  SKIP (HTTP {resp.status_code}): {url}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"  ERROR: {e}")
        return False

    soup = BeautifulSoup(resp.text, "html.parser")

    # Remove scripts, styles, nav elements
    for tag in soup.find_all(["script", "style", "nav", "header", "footer"]):
        tag.decompose()

    # Find the main content — lawphil typically uses a main content div or body
    content = soup.find("body")
    if not content:
        content = soup

    # Convert to markdown
    markdown_text = md(str(content), heading_style="ATX", strip=["img"])

    # Clean up excessive whitespace
    lines = markdown_text.split("\n")
    cleaned = []
    blank_count = 0
    for line in lines:
        stripped = line.rstrip()
        if not stripped:
            blank_count += 1
            if blank_count <= 2:
                cleaned.append("")
        else:
            blank_count = 0
            cleaned.append(stripped)

    body = "\n".join(cleaned).strip()

    # Write output
    output_path = os.path.join(OUTPUT_DIR, filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"**Source:** [{url}]({url})\n\n")
        f.write("---\n\n")
        f.write(body)
        f.write("\n")

    size_kb = os.path.getsize(output_path) / 1024
    print(f"  Saved: {output_path} ({size_kb:.1f} KB)")
    return True


def write_index(results):
    index_path = os.path.join(OUTPUT_DIR, "INDEX.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("# Rules of Court — Philippine Judiciary\n\n")
        f.write("Source: [lawphil.net](https://lawphil.net)\n\n")
        f.write("## Contents\n\n")
        f.write("### Civil Procedure\n")
        f.write("- [Rules 1-35 (2019 Amendments)](civil-procedure-rules-1-35.md)\n")
        f.write("- [Rules 36-71](civil-procedure-rules-36-71.md)\n\n")
        f.write("### Criminal Procedure\n")
        f.write("- [Rules 110-127](criminal-procedure-rules-110-127.md)\n\n")
        f.write("### Evidence\n")
        f.write("- [Rules 128-133 (2019 Amendments)](evidence-rules-128-133.md)\n")
        f.write("- [Rule 134 — Perpetuation of Testimony](evidence-rule-134.md)\n\n")
        f.write("### Special Proceedings\n")
        f.write("- [Rules 72-109](special-proceedings-rules-72-109.md)\n\n")
        f.write("---\n\n")
        f.write("## Scrape Results\n\n")
        for page, success in results:
            status = "OK" if success else "FAILED/SKIPPED"
            f.write(f"- {page['title']}: **{status}**\n")
    print(f"\nIndex written: {index_path}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    results = []
    for page in PAGES:
        success = scrape_page(page)
        results.append((page, success))
        time.sleep(1)  # Be polite
    write_index(results)
    print("\nDone.")


if __name__ == "__main__":
    main()
