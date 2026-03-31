import os
import requests
import json
import re
import time
from html import unescape

# Configuration
BASE_URL = "https://api.quran.com/api/v4"
HADITH_URL_TEMPLATE = "https://quran.com/api/proxy/content/api/qdc/hadith_references/by_ayah/{verse_key}/hadiths?language=en"
OUTPUT_DIR = "/Users/saidamenmambayao/apps/transcriptions/shari'ah/hadith/hadith-per-verse"
TRANSLATION_ID = 20  # Sahih International

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://quran.com/",
    "Accept": "application/json"
})

def get_chapters():
    url = f"{BASE_URL}/chapters?language=en"
    res = session.get(url)
    res.raise_for_status()
    return res.json()['chapters']

def clean_html(html_text):
    if not html_text: return ""
    # Remove HTML tags
    text = re.sub(r'<[^>]*>', '', html_text)
    return unescape(text).strip()

def fetch_verse_data(chapter_id):
    # Fetch Uthmani
    uthmani_url = f"{BASE_URL}/quran/verses/uthmani?chapter_number={chapter_id}"
    uthmani_res = session.get(uthmani_url).json()['verses']
    
    # Fetch Translation
    trans_url = f"{BASE_URL}/quran/translations/{TRANSLATION_ID}?chapter_number={chapter_id}"
    trans_res = session.get(trans_url).json()['translations']
    
    return uthmani_res, trans_res

def scrape_chapter_hadiths(chapter):
    ch_id = chapter['id']
    name = chapter['name_simple']
    verse_count = chapter['verses_count']
    
    filename = f"{ch_id:03d}-{name}.md"
    file_path = os.path.join(OUTPUT_DIR, filename)
    
    if os.path.exists(file_path):
        print(f"[{ch_id:03d}] {name} already exists. Skipping.")
        return
        
    print(f"[{ch_id:03d}] Processing {name} ({verse_count} verses)...")
    
    uthmani, translations = fetch_verse_data(ch_id)
    
    content = [
        f"# Surah {name}\n",
        f"\n",
        f"- **Chapter:** {ch_id}\n",
        f"- **Verses:** {verse_count}\n",
        f"\n",
        f"---\n\n"
    ]
    
    for i in range(verse_count):
        verse_num = i + 1
        verse_key = f"{ch_id}:{verse_num}"
        
        # 1. Verse Header
        content.append(f"## Verse {verse_num}\n\n")
        
        # 2. Arabic Text
        content.append(f"> {uthmani[i]['text_uthmani']}\n\n")
        
        # 3. Translation
        content.append(f"{clean_html(translations[i]['text'])}\n\n")
        
        # 4. Fetch Hadiths
        hadith_url = HADITH_URL_TEMPLATE.format(verse_key=verse_key)
        try:
            # Set specific referer for this verse
            headers = {"Referer": f"https://quran.com/{verse_key}/hadith"}
            h_res = session.get(hadith_url, headers=headers, timeout=10)
            
            if h_res.status_code == 200:
                h_data = h_res.json().get('hadiths', [])
                if h_data:
                    content.append("**Linked Hadiths:**\n\n")
                    for h in h_data:
                        coll = h.get('collection', 'Unknown')
                        num = h.get('hadithNumber', '')
                        body = ""
                        for loc in h.get('hadith', []):
                            if loc.get('lang') == 'en': # Note: sometimes it's 'lang', sometimes 'language'
                                body = loc.get('body', '')
                                break
                            elif loc.get('language') == 'en':
                                body = loc.get('body', '')
                                break
                        
                        content.append(f"#### {coll.title()} {num}\n")
                        content.append(f"{clean_html(body).strip()}\n\n")
                else:
                    content.append("*No explicitly linked Hadiths found on Quran.com for this verse.*\n\n")
            else:
                content.append(f"*Error fetching Hadiths for this verse (Status {h_res.status_code}).*\n\n")
            
            # Be gentle with the API
            time.sleep(0.1)

        except Exception as e:
            content.append(f"*Exception during Hadith fetch: {e}*\n\n")
            
        content.append("---\n\n")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(content)
    
    print(f"[{ch_id:03d}] Completed {name}.")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    try:
        chapters = get_chapters()
        for ch in chapters:
            scrape_chapter_hadiths(ch)
            time.sleep(0.5) 
            
        print("Hadith-per-Verse Scrape Complete.")
    except Exception as e:
        print(f"Process Error: {e}")

if __name__ == "__main__":
    main()
