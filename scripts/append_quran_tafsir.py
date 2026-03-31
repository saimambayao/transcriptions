import os
import requests
import re
import html
import time

# Tafsir Resource: Ibn Kathir (Abridged) (ID: 169)
TAFSIR_ID = "169"
BASE_DIR = "/Users/saidamenmambayao/apps/transcriptions/shari'ah/quran"

def html_to_markdown(html_text):
    if not html_text: return ""
    # Simple conversion
    html_text = re.sub(r'<h[1-3][^>]*>(.*?)</h[1-3]>', r'\n### \1\n', html_text, flags=re.IGNORECASE | re.DOTALL)
    html_text = re.sub(r'<(strong|b)[^>]*>(.*?)</\1>', r'**\2**', html_text, flags=re.IGNORECASE | re.DOTALL)
    html_text = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', html_text, flags=re.IGNORECASE | re.DOTALL)
    html_text = re.sub(r'<br\s*/?>', r'\n', html_text, flags=re.IGNORECASE)
    html_text = re.sub(r'<li[^>]*>(.*?)</li>', r'\n- \1', html_text, flags=re.IGNORECASE | re.DOTALL)
    html_text = re.sub(r'<[^>]+>', '', html_text)
    html_text = html.unescape(html_text)
    html_text = re.sub(r'\n{3,}', '\n\n', html_text)
    return html_text.strip()

def fix_tafsir_in_file(chapter_id):
    pattern = re.compile(rf"^{chapter_id:03d}-.*\.md$")
    target_file = next((f for f in os.listdir(BASE_DIR) if pattern.match(f)), None)
    
    if not target_file:
        print(f"[{chapter_id:03d}] Warning: File not found.")
        return False
    
    file_path = os.path.join(BASE_DIR, target_file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip existing Ibn Kathir section if it exists
    tafsir_header = "## Tafsir: Ibn Kathir (Abridged)"
    if tafsir_header in content:
        print(f"[{chapter_id:03d}] Stripping existing tafsir from {target_file}...")
        content = content.split("---")[0].strip() + "\n\n---\n\n"
    else:
        # Just ensure its at the end
        content = content.strip() + "\n\n---\n\n"

    # Fetch Tafsirs for the chapter - ensuring we get all of them
    # Set per_page=300 to capture all verses of any surah
    print(f"[{chapter_id:03d}] Fetching FULL Tafsir for {target_file} (per_page=300)...")
    url = f"https://api.quran.com/api/v4/tafsirs/{TAFSIR_ID}/by_chapter/{chapter_id}?per_page=300"
    try:
        res = requests.get(url)
        res.raise_for_status()
        tafsir_data = res.json().get('tafsirs', [])
        print(f"[{chapter_id:03d}] Received {len(tafsir_data)} tafsir entries.")
    except Exception as e:
        print(f"Error fetching: {e}")
        return False
        
    if not tafsir_data:
        print(f"[{chapter_id:03d}] No data received.")
        return False
        
    # Append new full section
    full_section = f"## Tafsir: Ibn Kathir (Abridged)\n\n"
    for entry in tafsir_data:
        verse_key = entry.get('verse_key')
        text = html_to_markdown(entry.get('text', ''))
        full_section += f"### Verse {verse_key}\n\n{text}\n\n---\n\n"
        
    with open(file_path, 'w', encoding='utf-8') as f:
        # Append to the original stripped content (which must keep the original Quran text)
        # Actually, my previous script appended it to the very end.
        # But wait, my splitting logic 'split("---")[0]' might be dangerous if the file had multiple ---
        # Let's re-think the split.
        pass

def better_fix_tafsir(chapter_id):
    pattern = re.compile(rf"^{chapter_id:03d}-.*\.md$")
    target_file = next((f for f in os.listdir(BASE_DIR) if pattern.match(f)), None)
    if not target_file: return
    
    file_path = os.path.join(BASE_DIR, target_file)
    with open(file_path, 'r', encoding='utf-8') as f:
        file_lines = f.readlines()
    
    # Find the first occurrence of "## Tafsir: Ibn Kathir (Abridged)"
    # and truncate the file there.
    new_lines = []
    found = False
    for line in file_lines:
        if "## Tafsir: Ibn Kathir (Abridged)" in line:
            found = True
            # Backtrack to remove the "---" separator if it's there
            if new_lines and "---" in new_lines[-1]:
                new_lines.pop()
            if new_lines and not new_lines[-1].strip():
                new_lines.pop()
            break
        new_lines.append(line)
    
    clean_content = "".join(new_lines).strip()
    
    # Fetch FULL data
    url = f"https://api.quran.com/api/v4/tafsirs/{TAFSIR_ID}/by_chapter/{chapter_id}?per_page=300"
    res = requests.get(url)
    res.raise_for_status()
    tafsirs = res.json().get('tafsirs', [])
    
    # Build complete string
    tafsir_section = "\n\n---\n\n## Tafsir: Ibn Kathir (Abridged)\n\n"
    for entry in tafsirs:
        tafsir_section += f"### Verse {entry['verse_key']}\n\n"
        tafsir_section += f"{html_to_markdown(entry['text'])}\n\n---\n\n"
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(clean_content + tafsir_section)
    print(f"[{chapter_id:03d}] {target_file} updated. Verses: {len(tafsirs)}")

def main():
    for chapter_id in range(1, 115):
        try:
            better_fix_tafsir(chapter_id)
            time.sleep(0.5)
        except Exception as e:
            print(f"Error at {chapter_id}: {e}")

if __name__ == "__main__":
    main()
