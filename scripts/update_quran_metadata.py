import os
import requests
import re

BASE_DIR = "/Users/saidamenmambayao/apps/transcriptions/shari'ah/quran"
TRANSLATION_ID = "20"
TRANSLATION_NAME = "Sahih International"

def fix_chapter_1():
    print("Fixing Chapter 1 (Al-Fatihah)...")
    url = "https://api.quran.com/api/v4/verses/by_chapter/1?language=en&words=false&translations={}&fields=text_uthmani&per_page=50".format(TRANSLATION_ID)
    res = requests.get(url)
    res.raise_for_status()
    verses = res.json().get('verses', [])
    
    filepath = os.path.join(BASE_DIR, "001-Al-Fatihah.md")
    
    content = [
        "# Surah Al-Fatihah (الفاتحة)\n",
        "\n",
        "- **English Name:** The Opener\n",
        "- **Translation:** {}\n".format(TRANSLATION_NAME),
        "- **Revelation Place:** Makkah\n",
        "- **Verses:** 7\n",
        "\n",
        "---\n\n"
    ]
    
    for v in verses:
        content.append("### Ayah {}\n\n".format(v['verse_number']))
        content.append("> {}\n\n".format(v.get('text_uthmani', '')))
        
        trans_text = ""
        for t in v.get('translations', []):
            if str(t.get('resource_id')) == TRANSLATION_ID:
                trans_text = t.get('text', '')
        
        trans_text = re.sub(r'<[^>]+>', '', trans_text)
        content.append("{}\n\n".format(trans_text))
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(content)
    print("Done Fixing Chapter 1.")

def update_metadata_others():
    print("Updating metadata for other files...")
    for filename in sorted(os.listdir(BASE_DIR)):
        if filename.startswith("001-") or not filename.endswith(".md"):
            continue
            
        filepath = os.path.join(BASE_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        # Check if already has translation line
        has_trans = any("**Translation:**" in line for line in lines)
        if has_trans:
            continue
            
        # Find where to insert it (usually after verses)
        # 1: # Surah Name
        # 2: 
        # 3: - **English Name:** ...
        # 4: - **Revelation Place:** ...
        # 5: - **Verses:** ...
        new_lines = []
        inserted = False
        for line in lines:
            new_lines.append(line)
            if "- **Verses:**" in line and not inserted:
                new_lines.append("- **Translation:** {}\n".format(TRANSLATION_NAME))
                inserted = True
                
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
            
    print("All other files updated.")

if __name__ == '__main__':
    fix_chapter_1()
    update_metadata_others()
