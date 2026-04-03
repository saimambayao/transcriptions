#!/usr/bin/env python3
"""
Scrape Bangsamoro Parliament Member Profiles.
Uses Playwright (via node script) for rendering and BeautifulSoup for parsing.
"""

import os
import sys
import json
import subprocess
import argparse
import time
import re
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE_DIR = "/Users/saidamenmambayao/apps/transcriptions/members-of-parliament"
SCRIPTS_DIR = "/Users/saidamenmambayao/apps/transcriptions/scripts"
MP_LIST_PATH = os.path.join(SCRIPTS_DIR, "mp_list.json")
JS_HELPER = os.path.join(SCRIPTS_DIR, "get_mp_data.js")

os.makedirs(BASE_DIR, exist_ok=True)

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def decode_cloudflare_email(encoded_string):
    """
    Decodes Cloudflare's email obfuscation.
    """
    try:
        r = int(encoded_string[:2], 16)
        email = ''.join([chr(int(encoded_string[i:i+2], 16) ^ r) for i in range(2, len(encoded_string), 2)])
        return email
    except:
        return encoded_string

def parse_mp_html(html, url, mp_name_orig):
    soup = BeautifulSoup(html, "html.parser")
    
    # 1. Basic Info
    # Name usually in et_pb_text_1_tb_body or similarly positioned module
    name_elem = soup.select_one(".et_pb_text_1_tb_body .et_pb_text_inner")
    name = name_elem.get_text(strip=True) if name_elem else mp_name_orig
    
    # Contact Details (Position, Email, etc.)
    position = "Member of Parliament"
    email = "N/A"
    contact_person = "N/A"
    contact_number = "N/A"
    office = "N/A"

    # 1. Primary: .member-details-wrap or .member-details
    details_wrap = soup.select_one(".member-details-wrap, .member-details")
    if details_wrap:
        for p in details_wrap.find_all("p"):
            text = p.get_text(separator=" ", strip=True)
            if "Position" in text:
                position = text.split(":", 1)[-1].strip() if ":" in text else position
            elif "Email" in text:
                email_link = p.select_one("a[href^='/cdn-cgi/l/email-protection#']")
                if email_link:
                    encoded = email_link['href'].split('#')[-1]
                    email = decode_cloudflare_email(encoded)
                else:
                    email = text.split(":", 1)[-1].strip() if ":" in text else email
            elif "Contact Person" in text:
                contact_person = text.split(":", 1)[-1].strip() if ":" in text else contact_person
            elif "Contact Number" in text:
                contact_number = text.split(":", 1)[-1].strip() if ":" in text else contact_number
            elif "Office Address" in text:
                office = text.split(":", 1)[-1].strip() if ":" in text else office
    else:
        # Fallback: Look for bits of info by labels in blurbs
        for blurb in soup.select(".et_pb_blurb"):
            text = blurb.get_text(strip=True)
            if "Position:" in text:
                position = text.replace("Position:", "").strip()
            elif "Email Address:" in text:
                # Check for Cloudflare encoded email
                email_link = blurb.select_one("a[href^='/cdn-cgi/l/email-protection#']")
                if email_link:
                    encoded = email_link['href'].split('#')[-1]
                    email = decode_cloudflare_email(encoded)
                else:
                    email = text.replace("Email Address:", "").strip()
            elif "Contact Person:" in text:
                contact_person = text.replace("Contact Person:", "").strip()
            elif "Contact Number:" in text:
                contact_number = text.replace("Contact Number:", "").strip()
            elif "Office Address:" in text:
                office = text.replace("Office Address:", "").strip()

    # 2. Tabs Content
    tabs = soup.select(".et_pb_all_tabs .et_pb_tab")
    
    biosketch = "N/A"
    principal_bills = []
    co_authored_bills = []
    principal_resolutions = []
    co_authored_resolutions = []
    committees = []

    # Map tabs by index based on observation
    # Index 0: Biosketch
    # Index 1: Principal Bills
    # Index 2: Co-Authored Bills
    # Index 3: Principal Resolutions (Proposed + Adopted usually combined or split)
    # Index 4: Co-Authored Resolutions
    # Index 5: Committees (Check the actual labels to be sure)
    
    tab_labels = [a.get_text(strip=True).lower() for a in soup.select(".et_pb_tabs_controls li a")]
    
    for i, tab in enumerate(tabs):
        label = tab_labels[i] if i < len(tab_labels) else f"tab-{i}"
        content = tab.select_one(".et_pb_tab_content")
        if not content: continue
        
        if "profile" in label or "biosketch" in label:
            biosketch = md(str(content)).strip()
        elif "principal authored bills" in label:
            links = content.select("a")
            principal_bills = [f"[{a.get_text(strip=True)}]({a['href']})" for a in links if a.has_attr('href')]
        elif "co-authored bills" in label:
            links = content.select("a")
            co_authored_bills = [f"[{a.get_text(strip=True)}]({a['href']})" for a in links if a.has_attr('href')]
        elif "principal authored resolutions" in label or "principal authored adopted resolutions" in label:
            links = content.select("a")
            principal_resolutions.extend([f"[{a.get_text(strip=True)}]({a['href']})" for a in links if a.has_attr('href')])
        elif "co-authored resolutions" in label:
            links = content.select("a")
            co_authored_resolutions = [f"[{a.get_text(strip=True)}]({a['href']})" for a in links if a.has_attr('href')]
        elif "committee memberships" in label:
            items = content.select("li")
            committees = [li.get_text(strip=True) for li in items]

    # Construction of Markdown
    md_output = f"# {name}\n\n"
    md_output += f"**Position:** {position}\n"
    md_output += f"**Email:** {email}\n"
    md_output += f"**Contact Person:** {contact_person}\n"
    md_output += f"**Contact Number:** {contact_number}\n"
    md_output += f"**Office Address:** {office}\n"
    md_output += f"**Source URL:** [{url}]({url})\n\n"
    
    md_output += "## Biosketch\n\n"
    md_output += biosketch + "\n\n"
    
    md_output += "## Legislative Record\n\n"
    
    md_output += "### Principal Authored Bills and Acts\n"
    if principal_bills:
        for b in principal_bills: md_output += f"- {b}\n"
    else: md_output += "*None recorded*\n"
    md_output += "\n"
    
    md_output += "### Co-Authored Bills and Acts\n"
    if co_authored_bills:
        for b in co_authored_bills: md_output += f"- {b}\n"
    else: md_output += "*None recorded*\n"
    md_output += "\n"
    
    md_output += "### Principal Authored Resolutions\n"
    if principal_resolutions:
        for r in principal_resolutions: md_output += f"- {r}\n"
    else: md_output += "*None recorded*\n"
    md_output += "\n"
    
    md_output += "### Co-Authored Resolutions\n"
    if co_authored_resolutions:
        for r in co_authored_resolutions: md_output += f"- {r}\n"
    else: md_output += "*None recorded*\n"
    md_output += "\n"
    
    md_output += "## Committee Memberships\n"
    if committees:
        for c in committees: md_output += f"- {c}\n"
    else: md_output += "*None recorded*\n"
    
    return md_output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", help="Run only on the first 3 MPs")
    args = parser.parse_args()

    with open(MP_LIST_PATH, "r") as f:
        mp_list = json.load(f)
    
    if args.test:
        mp_list = mp_list[:3]
        print("TEST MODE: Scraping only first 3 MPs")

    total = len(mp_list)
    print(f"Starting scrape of {total} MPs...")
    
    for i, mp in enumerate(mp_list, 1):
        name_orig = mp['name']
        url = mp['link']
        
        # Determine filename: last-name-first-name.md
        name_parts = name_orig.split(',')
        if len(name_parts) == 2:
            last = name_parts[0].strip().lower().replace('.', '').replace(' ', '-')
            first = name_parts[1].strip().lower().replace('.', '').replace(' ', '-')
            filename = f"{last}-{first}.md"
        else:
            filename = f"{slugify(name_orig)}.md"
            
        filepath = os.path.join(BASE_DIR, filename)
        
        if os.path.exists(filepath) and os.path.getsize(filepath) > 500:
            print(f"[{i}/{total}] Skipping {name_orig} (already exists)")
            continue
            
        print(f"[{i}/{total}] Scraping {name_orig}...")
        
        try:
            # Run the Playwright JS helper
            result = subprocess.run(
                ["node", JS_HELPER, url],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode != 0:
                print(f"  [Error] Failed to fetch {url}: {result.stderr}")
                continue
                
            html = result.stdout
            markdown_content = parse_mp_html(html, url, name_orig)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(markdown_content)
            
            print(f"  [Success] Saved to {filename}")
            
        except Exception as e:
            print(f"  [Error] Processing {name_orig}: {e}")
            
        time.sleep(0.5)  # Be nice to the server

    # Generate INDEX.md
    generate_index(mp_list)
    print("Done!")

def generate_index(mp_list):
    lines = ["# Members of Parliament (2022-2025)", "", f"Total: {len(mp_list)} members", "", "## List of MPs", ""]
    
    files = sorted([f for f in os.listdir(BASE_DIR) if f.endswith(".md") and f != "INDEX.md"])
    for f in files:
        name_formatted = f.replace(".md", "").replace("-", " ").title()
        lines.append(f"- [{name_formatted}]({f})")
        
    with open(os.path.join(BASE_DIR, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    main()
