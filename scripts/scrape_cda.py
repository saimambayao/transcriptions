#!/usr/bin/env python3
"""
Scrape Memorandum Circulars from the CDA website with OCR, retries, and PDF saving.
"""

import requests
import os
import re
import sys
import argparse
import time
import io
from bs4 import BeautifulSoup
import pdfplumber
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from urllib.parse import urljoin

BASE_DIR = "/Users/saidamenmambayao/apps/transcriptions/legislation/memorandum-circulars/cda-coop"
BASE_URL = "https://cda.gov.ph"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
})

def safe_get(url, retries=3, timeout=60):
    for i in range(retries):
        try:
            resp = session.get(url, timeout=timeout)
            return resp
        except Exception as e:
            print(f"  [Retry {i+1}/{retries}] {url}: {e}")
            time.sleep(2 * (i + 1))
    return None

def extract_text(pdf_path):
    full_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    full_text += t + "\n\n"
    except Exception as e:
        print(f"  [Error pdfplumber] {e}")

    clean_text = full_text.strip()
    if len(clean_text) < 300:
        print(f"  [OCR] Detected low text content ({len(clean_text)} chars). Running OCR...")
        full_text = run_ocr(pdf_path)
    
    return full_text.strip()

def run_ocr(pdf_path, dpi=400):
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            page = doc[page_num]
            mat = fitz.Matrix(dpi / 72, dpi / 72)
            pix = page.get_pixmap(matrix=mat)
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            page_text = pytesseract.image_to_string(img, lang='eng')
            text += f"\n\n--- PAGE {page_num + 1} ---\n\n{page_text}"
        doc.close()
    except Exception as e:
        print(f"  [Error OCR] {e}")
    return text

def get_pdf_url(landing_url):
    resp = safe_get(landing_url)
    if not resp or resp.status_code != 200: return None
    try:
        soup = BeautifulSoup(resp.text, "html.parser")
        links = soup.find_all("a", href=re.compile(r'\.pdf$', re.I))
        for link in links:
            href = link.get("href", "")
            lt = link.get_text().lower()
            if "mc-" in href.upper() or "circular" in href.lower() or "mc" in lt or "download" in lt:
                return urljoin(BASE_URL, href)
        if links: return urljoin(BASE_URL, links[0]["href"])
    except Exception as e:
        print(f"  [Error Landing Page] {e}")
    return None

def download_pdf(url, target_path):
    try:
        resp = session.get(url, timeout=120, stream=True)
        resp.raise_for_status()
        with open(target_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except Exception as e:
        print(f"  [Error Download] {e}")
        return False

def scrape_year(year):
    print(f"=== SCRAPING YEAR {year} ===")
    year_dir = os.path.join(BASE_DIR, str(year))
    os.makedirs(year_dir, exist_ok=True)
    page = 1
    entries = []
    
    while True:
        url = f"{BASE_URL}/{year}/?post_type=memorandum-circulars" if page == 1 else f"{BASE_URL}/{year}/page/{page}/?post_type=memorandum-circulars"
        print(f"  [Page {page}] Fetching {url}")
        resp = safe_get(url)
        if not resp: break
        if resp.status_code == 404: break
            
        soup = BeautifulSoup(resp.text, "html.parser")
        items = soup.find_all("a", href=re.compile(r'/memorandum-circulars/[^/]+/$'))
        if not items: items = soup.select("h2.entry-title a")
        if not items: break
            
        for item in items:
            title = item.get_text(strip=True)
            landing_url = item["href"]
            match = re.search(r'MC\s*(20\d{2}-\d+)', title, re.I)
            if not match: match = re.search(r'MC\s*(\d{2}-\d+)', title, re.I)
            mc_id = f"MC-{match.group(1)}" if match else landing_url.rstrip("/").split("/")[-1].upper()
            
            filename = f"{mc_id}.md"
            filepath = os.path.join(year_dir, filename)
            pdf_path = os.path.join(year_dir, f"{mc_id}.pdf")
            
            # Skip if BOTH exist and MD is substantial
            if os.path.exists(filepath) and os.path.exists(pdf_path):
                with open(filepath, "r") as r:
                    content = r.read()
                    if "Unable to extract text" not in content and "Low text content" not in content and len(content) > 1000:
                        print(f"  [Skip] {mc_id}")
                        entries.append((mc_id, title, landing_url))
                        continue

            print(f"  [Process] {mc_id} | {title}")
            pdf_url = get_pdf_url(landing_url)
            if not pdf_url:
                body = "*(No PDF document found on landing page)*"
            else:
                if not os.path.exists(pdf_path):
                    if not download_pdf(pdf_url, pdf_path):
                        print(f"    [Error] Could not download PDF for {mc_id}")
                
                if os.path.exists(pdf_path):
                    body = extract_text(pdf_path)
                    if not body: body = "*(Unable to extract text even with OCR)*"
                else:
                    body = f"*(Failed to download PDF - [Link]({pdf_url}))*"
            
            md = f"# {title}\n\n## Metadata\n- **MC Number**: {mc_id}\n- **Year**: {year}\n- **Source**: [{landing_url}]({landing_url})\n- **PDF URL**: [{pdf_url}]({pdf_url})\n\n---\n\n{body}\n"
            with open(filepath, "w", encoding="utf-8") as f: f.write(md)
            entries.append((mc_id, title, landing_url))
            time.sleep(1)
        
        # Pagination
        next_page = soup.select_one("a.next, a.pagination-next")
        if not next_page and page > 1: break
        page += 1
        
    generate_year_index(year, entries)
    return len(entries)

def generate_year_index(year, entries):
    entries.sort(key=lambda x: x[0], reverse=True)
    lines = [f"# CDA Memorandum Circulars — {year}", "", f"Total: {len(entries)} MCs", ""]
    for mid, title, link in entries: lines.append(f"- [{mid}]({mid}.md) — {title}")
    with open(os.path.join(BASE_DIR, str(year), "INDEX.md"), "w", encoding="utf-8") as f: f.write("\n".join(lines))

def generate_master_index():
    if not os.path.exists(BASE_DIR): return
    years = sorted([d for d in os.listdir(BASE_DIR) if d.isdigit()], reverse=True)
    lines = ["# CDA Memorandum Circulars Archive", "", "**Grand Total**: {total} Memorandum Circulars", "", "| Year | Link |", "|------|------|"]
    total = 0
    for y in years:
        y_dir = os.path.join(BASE_DIR, y)
        if not os.path.exists(y_dir): continue
        count = len([f for f in os.listdir(y_dir) if f.endswith(".md") and f != "INDEX.md"])
        lines.append(f"| {y} | [{y}]({y}/INDEX.md) ({count} MCs) |")
        total += count
    lines[2] = lines[2].replace("{total}", str(total))
    with open(os.path.join(BASE_DIR, "INDEX.md"), "w", encoding="utf-8") as f: f.write("\n".join(lines))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int)
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    if args.year: scrape_year(args.year)
    elif args.all:
        for y in range(2026, 1990, -1):
            try: scrape_year(y)
            except KeyboardInterrupt: break
            except Exception as e: print(f"  [Error] Year {y}: {e}")
    generate_master_index()

if __name__ == "__main__": main()
