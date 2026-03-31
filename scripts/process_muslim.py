import os
import json
import requests
import re

# Source URLs for Sahih Muslim (hadith-api)
ARA_URL = "https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/ara-muslim.json"
ENG_URL = "https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-muslim.json"
OUTPUT_DIR = "/Users/saidamenmambayao/apps/transcriptions/shari'ah/hadith/muslim"

def download_json(url):
    print(f"Downloading {url}...")
    res = requests.get(url)
    res.raise_for_status()
    return res.json()

def clean_filename(s):
    # Remove non-alphanumeric except hyphens and spaces
    s = re.sub(r'[^\w\s-]', '', s)
    # Replace spaces with hyphens
    s = re.sub(r'[-\s]+', '-', s).strip('-')
    # Limit length
    if len(s) > 50:
        s = s[:47] + "..."
    return s

def process_muslim():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    ara_data = download_json(ARA_URL)
    eng_data = download_json(ENG_URL)
    
    # Map hadiths by hadithnumber (universal)
    ara_hadiths = {h['hadithnumber']: h for h in ara_data['hadiths']}
    eng_hadiths = {h['hadithnumber']: h for h in eng_data['hadiths']}
    
    # Get sections/books metadata
    sections_ara = ara_data['metadata']['sections']
    sections_eng = eng_data['metadata']['sections']
    
    # Group hadiths by book number
    books_data = {}
    
    for h_num, h_eng in eng_hadiths.items():
        # Hadith reference can be a list or a single value in some cases? 
        # Usually it's an int. Let's handle it as int.
        try:
            book_id = str(h_eng['reference']['book'])
            h_in_book = h_eng['reference']['hadith']
        except (KeyError, TypeError):
            continue

        if book_id not in books_data:
            books_data[book_id] = {
                'title_eng': sections_eng.get(book_id, f"Book {book_id}"),
                'title_ara': sections_ara.get(book_id, ""),
                'hadiths': []
            }
        
        h_ara = ara_hadiths.get(h_num, {})
        books_data[book_id]['hadiths'].append({
            'num': h_in_book,
            'arabic': h_ara.get('text', ''),
            'english': h_eng.get('text', '')
        })
        
    # Generate files
    for book_id, data in sorted(books_data.items(), key=lambda x: int(x[0])):
        if not data['hadiths']:
            continue
            
        # Get hadith range for numbering
        # Some are strings, some are ints. Handle both.
        def extract_num(n):
            if isinstance(n, int): return n
            # Extract first number from string like "1.01" or "1"
            m = re.search(r'\d+', str(n))
            return int(m.group()) if m else 0

        nums = [extract_num(h['num']) for h in data['hadiths']]
        h_start = min(nums)
        h_end = max(nums)
        
        clean_title = clean_filename(data['title_eng'])
        filename = f"{int(book_id):02d}-{clean_title}-{h_start}-{h_end}.md"
        file_path = os.path.join(OUTPUT_DIR, filename)
        
        print(f"Generating {filename}...")
        
        content = [
            f"# {data['title_eng']} ({data['title_ara']})\n",
            f"\n",
            f"- **Book:** {book_id}\n",
            f"- **Hadith Range:** {h_start} - {h_end}\n",
            f"- **Source:** Sunnah.com Sahih Muslim\n",
            f"\n",
            f"---\n\n"
        ]
        
        # Sort by the extracted number
        sorted_hadiths = sorted(data['hadiths'], key=lambda x: extract_num(x['num']))
        
        for h in sorted_hadiths:
            content.append(f"### Hadith {h['num']}\n\n")
            if h['arabic']:
                content.append(f"> {h['arabic']}\n\n")
            if h['english']:
                content.append(f"{h['english']}\n\n")
            else:
                content.append(f"*(Translation not available in this collection)*\n\n")
            content.append(f"---\n\n")
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(content)
            
    print("Muslim Processing Complete.")

if __name__ == "__main__":
    process_muslim()
