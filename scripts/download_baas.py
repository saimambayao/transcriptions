#!/usr/bin/env python3
"""Download BAA PDFs from parliament.bangsamoro.gov.ph"""

import subprocess
import re
import time
import os
import json

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
OUTDIR = "/Users/saidamenmambayao/apps/transcriptions/docs/BAA-PDFs"
os.makedirs(OUTDIR, exist_ok=True)

# BAA numbers to skip (already downloaded or don't exist)
SKIP_BAAS = set(range(82, 90))  # 82-89 already downloaded
MISSING_BAAS = {56, 66, 67, 68, 69}  # Known to not have pages

def curl_get(url, timeout=30):
    """Fetch URL content using curl"""
    try:
        result = subprocess.run(
            ["curl", "-s", "-L", "-A", UA, "--max-time", str(timeout), url],
            capture_output=True, text=True, timeout=timeout+10
        )
        return result.stdout
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        return ""

def curl_download(url, filepath, timeout=60):
    """Download file using curl"""
    try:
        result = subprocess.run(
            ["curl", "-s", "-L", "-A", UA, "--max-time", str(timeout), "-o", filepath, url],
            capture_output=True, text=True, timeout=timeout+10
        )
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            if size < 1024:
                print(f"  WARNING: File too small ({size} bytes), likely not a real PDF")
                os.remove(filepath)
                return False
            return True
        return False
    except Exception as e:
        print(f"  ERROR downloading {url}: {e}")
        return False

# Step 1: Get all BAA page URLs
print("Step 1: Fetching BAA listing page...")
listing_html = curl_get("https://parliament.bangsamoro.gov.ph/baa-new/")
baa_urls = list(set(re.findall(r'href="(https://parliament\.bangsamoro\.gov\.ph/bta-acts/[^"]+)"', listing_html)))
baa_urls.sort()
print(f"  Found {len(baa_urls)} BAA page URLs")

# Step 2: For each page, find the BAA number and PDF link
print("\nStep 2: Scraping each BAA page for number and PDF link...")
results = {}  # baa_num -> {url, pdf_url, title}
unmatched = []

for i, url in enumerate(baa_urls):
    print(f"\n[{i+1}/{len(baa_urls)}] {url.split('/')[-2][:60]}...")
    html = curl_get(url)
    if not html:
        print("  FAILED to fetch page")
        unmatched.append(url)
        continue

    # Try to find BAA number from page content
    # Look for patterns like "Bangsamoro Autonomy Act No. 1" or "BAA No. 1" or "BTA Act No. 1"
    baa_num = None

    # Pattern 1: "Bangsamoro Autonomy Act No. XX" or "No. XX"
    matches = re.findall(r'(?:Bangsamoro\s+Autonomy\s+Act|BAA|BTA\s+Act)\s+No\.?\s*(\d+)', html, re.IGNORECASE)
    if matches:
        # Take the most common number (it appears in title, body, etc.)
        from collections import Counter
        num_counts = Counter(int(m) for m in matches)
        baa_num = num_counts.most_common(1)[0][0]

    if baa_num is None:
        # Pattern 2: Look in title tag
        title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.DOTALL)
        if title_match:
            title = title_match.group(1)
            num_match = re.search(r'No\.?\s*(\d+)', title)
            if num_match:
                baa_num = int(num_match.group(1))

    if baa_num is None:
        print("  Could not determine BAA number")
        unmatched.append(url)
        continue

    print(f"  BAA Number: {baa_num}")

    if baa_num in SKIP_BAAS:
        print(f"  SKIPPING BAA {baa_num} (already downloaded)")
        continue

    # Find PDF links
    pdf_links = re.findall(r'href="([^"]*\.pdf[^"]*)"', html, re.IGNORECASE)
    # Also check for links with pdf in query params
    pdf_links += re.findall(r'href="([^"]*\?[^"]*\.pdf[^"]*)"', html, re.IGNORECASE)
    # Deduplicate
    pdf_links = list(set(pdf_links))

    if not pdf_links:
        print(f"  No PDF links found on page")
        results[baa_num] = {"url": url, "pdf_url": None, "status": "no_pdf_on_page"}
        continue

    # Prefer parliament.bangsamoro.gov.ph PDFs, then officialgazette
    best_pdf = None
    for link in pdf_links:
        if "parliament.bangsamoro.gov.ph" in link:
            best_pdf = link
            break
    if not best_pdf:
        for link in pdf_links:
            if "officialgazette.bangsamoro.gov.ph" in link:
                best_pdf = link
                break
    if not best_pdf:
        best_pdf = pdf_links[0]

    print(f"  PDF: {best_pdf[:80]}...")
    results[baa_num] = {"url": url, "pdf_url": best_pdf, "status": "found"}

    # Small delay to be polite
    time.sleep(0.5)

# Step 3: Download PDFs
print("\n\nStep 3: Downloading PDFs...")
downloaded = []
failed = []
no_pdf = []

# Process in batches of 5
baa_nums = sorted([n for n in results.keys() if results[n].get("pdf_url")])
for batch_start in range(0, len(baa_nums), 5):
    batch = baa_nums[batch_start:batch_start+5]
    print(f"\nBatch: BAAs {batch}")

    for baa_num in batch:
        info = results[baa_num]
        pdf_url = info["pdf_url"]
        filepath = os.path.join(OUTDIR, f"BAA-{baa_num}.pdf")

        if os.path.exists(filepath) and os.path.getsize(filepath) > 1024:
            print(f"  BAA-{baa_num}.pdf already exists, skipping")
            downloaded.append(baa_num)
            continue

        print(f"  Downloading BAA-{baa_num}...")
        if curl_download(pdf_url, filepath):
            size = os.path.getsize(filepath)
            print(f"  OK: BAA-{baa_num}.pdf ({size:,} bytes)")
            downloaded.append(baa_num)
        else:
            print(f"  FAILED: BAA-{baa_num}")
            failed.append(baa_num)

    time.sleep(1)  # Pause between batches

# Collect BAAs with no PDF on page
for baa_num, info in results.items():
    if info.get("status") == "no_pdf_on_page":
        no_pdf.append(baa_num)

# Step 4: Try official gazette for missing ones
missing_to_try = sorted(set(no_pdf + failed))
if missing_to_try:
    print(f"\n\nStep 4: Trying official gazette for BAAs: {missing_to_try}")
    for baa_num in missing_to_try:
        if baa_num in SKIP_BAAS or baa_num in MISSING_BAAS:
            continue
        # Try different year/month patterns
        print(f"\n  Trying gazette for BAA {baa_num}...")
        # We don't know the exact date, try searching
        gazette_url = f"https://officialgazette.bangsamoro.gov.ph/?s=bangsamoro+autonomy+act+no+{baa_num}"
        html = curl_get(gazette_url)
        if html:
            # Find specific BAA page
            gazette_links = re.findall(r'href="(https://officialgazette\.bangsamoro\.gov\.ph/[^"]*autonomy-act[^"]*)"', html, re.IGNORECASE)
            if not gazette_links:
                gazette_links = re.findall(r'href="(https://officialgazette\.bangsamoro\.gov\.ph/\d{4}/\d{2}/\d{2}/[^"]*)"', html)

            for glink in gazette_links:
                if f"no-{baa_num}" in glink or f"no_{baa_num}" in glink:
                    print(f"  Found gazette page: {glink}")
                    ghtml = curl_get(glink)
                    if ghtml:
                        gpdf_links = re.findall(r'href="([^"]*\.pdf[^"]*)"', ghtml, re.IGNORECASE)
                        if gpdf_links:
                            filepath = os.path.join(OUTDIR, f"BAA-{baa_num}.pdf")
                            print(f"  Downloading from gazette...")
                            if curl_download(gpdf_links[0], filepath):
                                size = os.path.getsize(filepath)
                                print(f"  OK: BAA-{baa_num}.pdf ({size:,} bytes)")
                                downloaded.append(baa_num)
                                if baa_num in failed:
                                    failed.remove(baa_num)
                                if baa_num in no_pdf:
                                    no_pdf.remove(baa_num)
                            break
        time.sleep(1)

# Final report
print("\n" + "="*60)
print("FINAL REPORT")
print("="*60)

all_expected = set(range(1, 82)) - SKIP_BAAS - MISSING_BAAS
downloaded_set = set(downloaded)
still_missing = sorted(all_expected - downloaded_set)

print(f"\nExpected BAAs (1-81, excluding skipped/missing): {len(all_expected)}")
print(f"Successfully downloaded: {len(downloaded_set)}")
print(f"Failed/No PDF: {len(still_missing)}")

if still_missing:
    print(f"\nMISSING BAA numbers (no PDF found): {still_missing}")

if unmatched:
    print(f"\nUnmatched URLs (could not determine BAA number):")
    for u in unmatched:
        print(f"  {u}")

# Disk space
total_size = 0
for f in os.listdir(OUTDIR):
    if f.endswith(".pdf"):
        total_size += os.path.getsize(os.path.join(OUTDIR, f))
print(f"\nTotal disk space used: {total_size / (1024*1024):.1f} MB")
print(f"Files in {OUTDIR}:")
for f in sorted(os.listdir(OUTDIR)):
    if f.endswith(".pdf"):
        size = os.path.getsize(os.path.join(OUTDIR, f))
        print(f"  {f} ({size:,} bytes)")
