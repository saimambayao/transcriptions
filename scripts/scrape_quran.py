import os
import requests
import time
import re

BASE_DIR = "/Users/saidamenmambayao/apps/transcriptions/shari'ah/quran"
os.makedirs(BASE_DIR, exist_ok=True)

# 20 = Sahih International
TRANSLATION_ID = "20"

def get_chapters():
    url = "https://api.quran.com/api/v4/chapters?language=en"
    res = requests.get(url)
    res.raise_for_status()
    return res.json().get('chapters', [])

def get_verses(chapter_id):
    verses = []
    page = 1
    while True:
        url = f"https://api.quran.com/api/v4/verses/by_chapter/{chapter_id}?language=en&words=false&translations={TRANSLATION_ID}&fields=text_uthmani&page={page}&per_page=50"
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        v_list = data.get('verses', [])
        verses.extend(v_list)
        pagination = data.get('pagination', {})
        if page >= pagination.get('total_pages', 1):
            break
        page += 1
        time.sleep(0.1)
    return verses

def main():
    chapters = get_chapters()
    print(f"Fetched {len(chapters)} chapters. Starting download (Sahih International)...")
    for chap in chapters:
        c_id = chap['id']
        c_name = chap['name_simple']
        c_arabic = chap['name_arabic']
        c_trans = chap['translated_name']['name']
        c_rev = chap['revelation_place'].capitalize()
        c_verses_count = chap['verses_count']
        
        safe_name = re.sub(r'[^A-Za-z0-9]+', '-', c_name).strip('-')
        filename = f"{c_id:03d}-{safe_name}.md"
        filepath = os.path.join(BASE_DIR, filename)
        
        verses = get_verses(c_id)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# Surah {c_name} ({c_arabic})\n\n")
            f.write(f"- **English Name:** {c_trans}\n")
            f.write(f"- **Translation:** Sahih International\n")
            f.write(f"- **Revelation Place:** {c_rev}\n")
            f.write(f"- **Verses:** {c_verses_count}\n\n")
            f.write("---\n\n")
            
            for v in verses:
                ayah_num = v['verse_number']
                uthmani = v.get('text_uthmani', '')
                
                trans_text = ""
                for t in v.get('translations', []):
                    if str(t.get('resource_id')) == TRANSLATION_ID:
                        trans_text = t.get('text', '')
                
                # Cleanup HTML tags
                trans_text = re.sub(r'<[^>]+>', '', trans_text)
                
                f.write(f"### Ayah {ayah_num}\n\n")
                f.write(f"> {uthmani}\n\n")
                f.write(f"{trans_text}\n\n")
        
        print(f"[{c_id:03d}/114] Saved {filename} with Sahih International translation.")
        time.sleep(0.1)
        
    print("\nFINISHED — All 114 Surahs updated with Sahih International metadata.")

if __name__ == '__main__':
    main()
