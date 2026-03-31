import os
import requests
import json
import re
import time

# Configuration
TAFSIR_ID = 168  # Ma'arif al-Qur'an (English)
BASE_URL = "https://api.quran.com/api/v4"
OUTPUT_DIR = "/Users/saidamenmambayao/apps/transcriptions/shari'ah/tafseer/tafsir-maarif"

session = requests.Session()

def get_chapters():
    url = f"{BASE_URL}/chapters?language=en"
    res = session.get(url)
    res.raise_for_status()
    return res.json()['chapters']

def clean_html(html):
    if not html: return ""
    # Basic HTML tag removal/conversion
    text = html.replace('<p>', '\n\n').replace('</p>', '').replace('<br>', '\n').replace('<br/>', '\n')
    text = re.sub(r'<[^>]*>', '', text)
    # Decode some entities
    text = text.replace('&nbsp;', ' ').replace('&lsquo;', "'").replace('&rsquo;', "'").replace('&ldquo;', '"').replace('&rdquo;', '"')
    return text.strip()

def scrape_surah(chapter_id, name, verse_count):
    filename = f"{chapter_id:03d}-{name}.md"
    file_path = os.path.join(OUTPUT_DIR, filename)
    
    if os.path.exists(file_path):
        print(f"  Surah {chapter_id} ({name}) already exists. Skipping.")
        return filename
        
    print(f"Scraping Surah {chapter_id} ({name})...")
    
    content = [
        f"# {name}\n",
        f"\n",
        f"- **Surah:** {chapter_id}\n",
        f"- **Verses:** {verse_count}\n",
        f"- **Tafsir:** Ma'arif al-Qur'an (Mufti Muhammad Shafi)\n",
        f"\n",
        f"---\n\n"
    ]
    
    prev_text = ""
    surah_entries = []
    
    for ayah_num in range(1, verse_count + 1):
        url = f"{BASE_URL}/tafsirs/{TAFSIR_ID}/by_ayah/{chapter_id}:{ayah_num}"
        retries = 3
        while retries > 0:
            try:
                res = session.get(url, timeout=10)
                res.raise_for_status()
                data = res.json()
                raw_text = data['tafsir']['text']
                
                if raw_text == prev_text:
                    if surah_entries:
                        surah_entries[-1]['end_ayah'] = ayah_num
                else:
                    surah_entries.append({
                        'start_ayah': ayah_num,
                        'end_ayah': ayah_num,
                        'text': raw_text
                    })
                    prev_text = raw_text
                break
            except Exception as e:
                print(f"    Error fetching {chapter_id}:{ayah_num}: {e}. Retrying...")
                retries -= 1
                time.sleep(2)
        
    # Process entries into content
    for entry in surah_entries:
        if entry['start_ayah'] == entry['end_ayah']:
            content.append(f"## Ayah {entry['start_ayah']}\n\n")
        else:
            content.append(f"## Ayah {entry['start_ayah']} - {entry['end_ayah']}\n\n")
            
        content.append(f"{clean_html(entry['text'])}\n\n")
        content.append(f"---\n\n")
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(content)
    
    return filename

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    try:
        chapters = get_chapters()
        for ch in chapters:
            scrape_surah(ch['id'], ch['name_simple'], ch['verses_count'])
            # Minimal delay for reliability
            time.sleep(0.1)
            
        print("Ma'arif al-Qur'an Scrape Complete.")
    except Exception as e:
        print(f"Main Loop Error: {e}")

if __name__ == "__main__":
    main()
