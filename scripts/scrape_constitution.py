#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import os
import re
from datetime import datetime

URL = "https://lawphil.net/consti/cons1987.html"
# Ensure the path matches the user request exactly
OUTPUT_PATH = "/Users/saidamenmambayao/apps/transcriptions/legislation/Constitution/1987-constitution.md"

def scrape():
    print(f"Scraping {URL}...")
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    })
    
    try:
        resp = session.get(URL, timeout=30)
        resp.raise_for_status()
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return

    soup = BeautifulSoup(resp.text, "html.parser")
    
    # Remove non-content elements
    for tag in soup.find_all(['script', 'style', 'link', 'meta', 'title', 'gcse:searchbox-only']):
        tag.decompose()
        
    # LawPhil specific: remove images
    for img in soup.find_all('img'):
        img.decompose()
        
    # Get the body content
    body = soup.find('body')
    if not body:
        print("Could not find body node")
        return

    # Convert to markdown
    # Strip links to avoid the doubling effect from anchor/text overlap
    content_md = md(
        str(body), 
        strip=['a'], 
        heading_style="ATX", 
        bullets="-"
    )
    
    # --- Post-processing ---
    
    # 1. Trim the top: find "PREAMBLE" to start from the actual content
    preamble_match = re.search(r'\n?PREAMBLE\n?', content_md)
    if preamble_match:
        content_md = content_md[preamble_match.start():]
    
    # 2. Trim the bottom: remove LawPhil footer artifacts
    content_md = re.sub(r'The Lawphil Project.*$', '', content_md, flags=re.DOTALL | re.IGNORECASE)
    content_md = re.sub(r'Arellano Law Foundation.*$', '', content_md, flags=re.DOTALL | re.IGNORECASE)
    
    # 3. Clean up doubled markers (e.g. ARTICLE I ARTICLE I)
    content_md = re.sub(r'(ARTICLE [IVXLCDM]+)\s+\1', r'\1', content_md)
    
    # 4. Remove excessive blockquote markers if markdownify introduced them from nested blockquotes
    content_md = re.sub(r'^\s*>\s*', '', content_md, flags=re.MULTILINE)
    
    # 5. Collapse excessive blank lines
    content_md = re.sub(r'\n{4,}', '\n\n\n', content_md)
    
    # 6. Clean up line-end trailing whitespace
    lines = content_md.split('\n')
    lines = [line.rstrip() for line in lines]
    content_md = '\n'.join(lines).strip()

    # Header with metadata
    header = f"""# 1987 Constitution of the Republic of the Philippines

## Metadata

- **Source**: {URL}
- **Scraped Date**: {datetime.now().strftime('%Y-%m-%d')}

---

"""
    final_content = header + content_md
    
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(final_content)
    
    print(f"Successfully saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    scrape()
