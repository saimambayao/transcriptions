import os
import re

def clean_text(text):
    if not text:
        return ""
    # Remove markdown bold/italic
    text = re.sub(r'\*+', '', text)
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text).strip()
    return text

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
        clean_l = line.strip().replace('*', '')
        if not found_act:
            if clean_l == "AN ACT":
                found_act = True
                continue
            elif clean_l.startswith("AN ACT "):
                found_act = True
                title_lines.append(clean_l[7:])
                continue
        
        if found_act:
            if not clean_l:
                if title_lines: break
                else: continue
            if any(marker in clean_l for marker in ["Be it enacted", "SECTION", "ARTICLE", "Explanatory Note"]):
                break
            if clean_l == "AN ACT": continue # Skip redundant AN ACT
            title_lines.append(clean_l)
    
    title = " ".join(title_lines)
    return f"BAA {baa_num} - {clean_text(title)}"

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
        clean_l = line.strip().replace('*', '')
        if not found_act:
            if clean_l == "AN ACT":
                found_act = True
                continue
            elif clean_l.startswith("AN ACT "):
                found_act = True
                title_lines.append(clean_l[7:])
                continue
        
        if found_act:
            if not clean_l:
                if title_lines: break
                else: continue
            if any(marker in clean_l for marker in ["Be it enacted", "SECTION", "ARTICLE", "Explanatory Note", "Introduced by"]):
                break
            if clean_l == "AN ACT": continue
            title_lines.append(clean_l)

    title = " ".join(title_lines)
    return f"BILL {bill_num} - {clean_text(title)}"

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
        clean_l = line.strip().replace('*', '')
        if not found_target:
            # Look for line starting with RESOLUTION but not RESOLUTION NO.
            if clean_l.startswith("RESOLUTION") and not re.search(r'^RESOLUTION NO\.', clean_l, re.I):
                found_target = True
        
        if found_target:
            if not clean_l:
                if title_lines: break
                else: continue
            if "WHEREAS" in clean_l:
                break
            title_lines.append(clean_l)
            
    title = " ".join(title_lines)
    # Remove leading "RESOLUTION " if it's there
    if title.upper().startswith("RESOLUTION "):
        title = title[11:]
        
    return f"Resolution {res_num} - {clean_text(title)}"

def process_directory(directory, doc_type):
    index = []
    if not os.path.exists(directory): return []
    files = [f for f in os.listdir(directory) if f.endswith('.md') and f.lower() != 'index.md' and f.lower() != 'sample.md' and not f.startswith('.')]
    
    for filename in files:
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
            
        if doc_type == 'BAA':
            info = extract_baa_info(content, filename)
        elif doc_type == 'BILL':
            info = extract_bill_info(content, filename)
        elif doc_type == 'RESOLUTION':
            info = extract_resolution_info(content, filename)
        
        index.append(info)
        
    def get_num(s):
        m = re.search(r'\d+', s)
        return int(m.group()) if m else 0
    
    index.sort(key=get_num)
    return index

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
