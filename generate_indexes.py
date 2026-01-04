import os
import re

def clean_text(text):
    if not text:
        return ""
    # Remove markdown bold/italic
    text = re.sub(r'\*+', '', text)
    # Remove quotes
    text = re.sub(r'[\"“”]', '', text)
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_line(line):
    # Remove stars, quotes (smart and straight)
    return line.strip().replace('*', '').replace('"', '').replace('“', '').replace('”', '').strip()

def is_marker(line):
    # Check if the line is a break marker
    # Markers: Be it enacted, Section X, Article X, Explanatory Note, Introduced by
    # Using regex for robust matching at the start of the line
    
    if re.search(r'^Be it enacted', line, re.IGNORECASE):
        return True
    if re.search(r'^(Section|Sec\.)\s*\d+', line, re.IGNORECASE):
        return True
    if re.search(r'^Article\s+[IVX\d]+', line, re.IGNORECASE):
        return True
    if re.search(r'^Explanatory Note', line, re.IGNORECASE):
        return True
    if re.search(r'^Introduced by', line, re.IGNORECASE):
        return True
    return False

def extract_baa_info(content, filename):
    # ID
    match_num = re.search(r'BANGSAMORO AUTONOMY ACT NO[\.\s]+(\d+)', content, re.IGNORECASE)
    baa_num = match_num.group(1) if match_num else "Unknown"
    if baa_num == "Unknown":
        fn_match = re.search(r'\d+', filename)
        if fn_match: baa_num = fn_match.group()

    # Title
    lines = content.split('\n')
    found_act = False
    title_lines = []
    for line in lines:
        clean_l = clean_line(line)
        upper_l = clean_l.upper()
        if not found_act:
            if upper_l == "AN ACT":
                found_act = True
                continue
            elif upper_l.startswith("AN ACT "):
                found_act = True
                title_lines.append(clean_l[7:])
                continue
        
        if found_act:
            if not clean_l:
                if title_lines: break
                else: continue
            
            # Check for markers using the more specific function
            if is_marker(clean_l):
                break
                
            if upper_l == "AN ACT": continue 
            title_lines.append(clean_l)
    
    title = " ".join(title_lines)
    return baa_num, f"BAA {baa_num} - {clean_text(title)}"

def extract_bill_info(content, filename):
    # ID
    match_num = re.search(r'(?:BTA Bill No\.|Parliament Bill No\.|Bill No\.|BTA BILL NO\.|Parliament Bill No)[\.\s]*(?:\*\*)?(\d+)', content, re.IGNORECASE)
    bill_num = match_num.group(1) if match_num else "Unknown"
    if bill_num == "Unknown":
        fn_match = re.search(r'\d+', filename)
        if fn_match: bill_num = fn_match.group()
    
    # Title
    lines = content.split('\n')
    found_act = False
    title_lines = []
    for line in lines:
        clean_l = clean_line(line)
        upper_l = clean_l.upper()
        if not found_act:
            if upper_l == "AN ACT":
                found_act = True
                continue
            elif upper_l.startswith("AN ACT "):
                found_act = True
                title_lines.append(clean_l[7:])
                continue
        
        if found_act:
            if not clean_l:
                if title_lines: break
                else: continue
            
            if is_marker(clean_l):
                break
                
            if upper_l == "AN ACT": continue
            title_lines.append(clean_l)

    title = " ".join(title_lines)
    return bill_num, f"BILL {bill_num} - {clean_text(title)}"

def extract_resolution_info(content, filename):
    # ID
    match_num = re.search(r'RESOLUTION NO[\.\s]+(\d+)', content, re.IGNORECASE)
    res_num = match_num.group(1) if match_num else "Unknown"
    if res_num == "Unknown":
        fn_match = re.search(r'\d+', filename)
        if fn_match: res_num = fn_match.group()
    
    # Title
    lines = content.split('\n')
    title_lines = []
    found_target = False
    for line in lines:
        clean_l = clean_line(line)
        upper_l = clean_l.upper()
        if not found_target:
            # Look for line starting with RESOLUTION but not RESOLUTION NO.
            if upper_l.startswith("RESOLUTION") and not re.search(r'^RESOLUTION NO\.', upper_l, re.I):
                found_target = True
                if upper_l == "RESOLUTION":
                    continue
            elif upper_l.startswith("A RESOLUTION"):
                found_target = True
        
        if found_target:
            if not clean_l:
                if title_lines: break
                else: continue
            if "WHEREAS" in upper_l:
                break
            title_lines.append(clean_l)
            
    title = " ".join(title_lines)
    # Remove leading "RESOLUTION " or "A RESOLUTION" if it's there
    cleaned_upper = title.upper()
    if cleaned_upper.startswith("RESOLUTION "):
        title = title[11:]
    elif cleaned_upper.startswith("A RESOLUTION "):
        title = title[13:]
        
    return res_num, f"Resolution {res_num} - {clean_text(title)}"

def process_directory(directory, doc_type):
    if not os.path.exists(directory): return []
    files = [f for f in os.listdir(directory) if f.endswith('.md') and f.lower() != 'index.md' and f.lower() != 'sample.md' and not f.startswith('.')]
    
    entries = {} # num -> info
    
    for filename in files:
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
            
        if doc_type == 'BAA':
            num, info = extract_baa_info(content, filename)
        elif doc_type == 'BILL':
            num, info = extract_bill_info(content, filename)
        elif doc_type == 'RESOLUTION':
            num, info = extract_resolution_info(content, filename)
        
        # Normalize num for dictionary key to handle leading zeros
        if num.isdigit():
            num = str(int(num))
        
        # Deduplication logic: prefer entry with title
        current_title = info.split(' - ', 1)[1].strip() if ' - ' in info else ""
        
        if num in entries:
            existing_info = entries[num]
            existing_title = existing_info.split(' - ', 1)[1].strip() if ' - ' in existing_info else ""
            if not existing_title and current_title:
                entries[num] = info
        else:
            entries[num] = info

    # Fill gaps for all document types
    if entries:
        max_num = max(int(k) for k in entries.keys() if k.isdigit())
        
        # Ensure we cover at least up to 249 for Bills if max is lower (unlikely given index, but covers user intent)
        # Actually, for general "Do the same", simply filling 1..max_num is the standard approach.
        # However, for Bills, we have files up to 400+, so max_num will be correct.
        
        for i in range(1, max_num + 1):
            s_num = str(i)
            if s_num not in entries:
                prefix = ""
                if doc_type == 'BAA': prefix = "BAA"
                elif doc_type == 'BILL': prefix = "BILL"
                elif doc_type == 'RESOLUTION': prefix = "Resolution"
                
                entries[s_num] = f"{prefix} {s_num} - "
        
    def get_num(s):
        try:
            return int(s)
        except ValueError:
            return 999999
    
    # Sort by number
    sorted_items = sorted(entries.items(), key=lambda item: get_num(item[0]))
    return [item[1] for item in sorted_items]

base_dir = "/Users/saidamenmambayao/apps/transcriptions/docs"

baa_index = process_directory(os.path.join(base_dir, "BAAs"), "BAA")
bill_index = process_directory(os.path.join(base_dir, "bills"), "BILL")
res_index = process_directory(os.path.join(base_dir, "resolution"), "RESOLUTION")

if baa_index:
    with open(os.path.join(base_dir, "BAAs/INDEX.md"), 'w') as f:
        f.write("# Index of BAAs\n\n")
        f.write("\n\n".join(baa_index) + "\n")

if bill_index:
    with open(os.path.join(base_dir, "bills/INDEX.md"), 'w') as f:
        f.write("# Index of Bills\n\n")
        f.write("\n\n".join(bill_index) + "\n")

if res_index:
    with open(os.path.join(base_dir, "resolution/INDEX.md"), 'w') as f:
        f.write("# Index of Resolutions\n\n")
        f.write("\n\n".join(res_index) + "\n")
