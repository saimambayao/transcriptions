import os
import re

def clean_text(text):
    if not text: return ""
    # Remove long sequences of dashes or underscores (decorative separators)
    text = re.sub(r'[-_=]{3,}', '', text)
    # Remove superscript numbers (common in these docs for footnotes/references)
    text = re.sub(r'[¹²³⁴⁵⁶⁷⁸⁹⁰]', '', text)
    # Remove markdown bold/italic
    text = re.sub(r'\*+', '', text)
    # Remove quotes and redundant symbols
    text = re.sub(r'[\"“”]', '', text)
    # Normalize whitespace
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
    if re.search(r'^Authored by', line, re.IGNORECASE):
        return True
    if re.search(r'^Co-Author', line, re.IGNORECASE):
        return True
    return False

def extract_baa_info(content, filename):
    # Prefer filename if it matches BAA-X.md or similar
    fn_match = re.search(r'\d+', filename)
    baa_num = fn_match.group() if fn_match else "Unknown"

    # Fallback to content only if filename doesn't have a number
    if baa_num == "Unknown":
        match_num = re.search(r'BANGSAMORO AUTONOMY ACT NO[\.\s]+(\d+)', content, re.IGNORECASE)
        baa_num = match_num.group(1) if match_num else "Unknown"

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
    return baa_num, clean_text(title)

def extract_bill_info(content, filename):
    # Prefer filename if it matches PB-X.md or similar
    fn_match = re.search(r'\d+', filename)
    bill_num = fn_match.group() if fn_match else "Unknown"

    # Fallback to content only if filename doesn't have a number
    if bill_num == "Unknown":
        match_num = re.search(r'(?:BTA Bill No\.|Parliament Bill No\.|Bill No\.|BTA BILL NO\.|Parliament Bill No|PB No\.|Parliament PB No\.|BTA PB No\.)[\.\s]*(?:\*\*)?(\d+)', content, re.IGNORECASE)
        bill_num = match_num.group(1) if match_num else "Unknown"
    
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
    return bill_num, clean_text(title)

def extract_resolution_info(content, filename):
    # Prefer filename if it matches PR-X.md or Res-X.md
    fn_match = re.search(r'\d+', filename)
    res_num = fn_match.group() if fn_match else "Unknown"

    # Fallback to content only if filename doesn't have a number
    if res_num == "Unknown":
        match_num = re.search(r'Proposed Resolution No[\.\s]+(\d+)', content, re.IGNORECASE)
        if not match_num:
            match_num = re.search(r'^\s*RESOLUTION NO[\.\s]+(\d+)', content, re.IGNORECASE | re.MULTILINE)
        res_num = match_num.group(1) if match_num else "Unknown"
    
    # Title
    lines = content.split('\n')
    title_lines = []
    found_start = False
    
    # First pass: find the real resolution ID if possible (especially for Proposed)
    # Search for "Proposed Resolution No. X" or similar
    id_match = re.search(r'(?:Proposed\s+)?Resolution\s+No[\.\s]+(\d+)', content, re.IGNORECASE)
    if id_match:
        res_num = id_match.group(1)
    
    # Second pass: Extract title. 
    # Logic: Start collecting after "RESOLUTION" or "A RESOLUTION" header 
    # Step 1: Skip metadata/header lines
    metadata_markers = [
        r'^RESOLUTION NO',
        r'^PROPOSED RESOLUTION NO',
        r'^AUTHORS?:',
        r'^CO-AUTHORS?:',
        r'^INTRODUCED BY:',
        r'^AUTHORED BY:',
        r'^MP ',
        r'^HON\. ',
        r'^EXPLANATORY NOTE'
    ]

    title_lines = []
    found_start = False
    
    for i, line in enumerate(lines):
        clean_l = clean_line(line)
        if not clean_l: continue
        upper_l = clean_l.upper()
        
        # Check if line is Metadata we should never include in title
        is_metadata = False
        for marker in metadata_markers:
            if re.search(marker, upper_l):
                is_metadata = True
                break
        if is_metadata:
            # If we were collecting title and hit metadata, we should probably stop or skip it
            if found_start: 
                # Exception: "MP" or "HON" might be part of a title sometimes but unlikely at start of line inside title block
                # But if we hit "WHEREAS" or similar it's already handled.
                # If we hit "INTRODUCED BY" while collecting title, it's a definite STOP.
                if re.search(r'^(AUTHORED|INTRODUCED|CO-AUTHOR|EXPLANATORY)', upper_l):
                    break
            continue

        if not found_start:
            # Look for "A RESOLUTION" or "RESOLUTION" (not followed by NO)
            # We want to catch the start of the title block.
            if (upper_l.startswith("RESOLUTION") and not re.search(r'^RESOLUTION NO', upper_l, re.I)) or upper_l.startswith("A RESOLUTION"):
                
                # Check if next few lines are Explanatory Note - if so, this is a header for it
                is_expl_header = False
                for j in range(i+1, min(i+5, len(lines))):
                    if "EXPLANATORY NOTE" in lines[j].upper():
                        is_expl_header = True
                        break
                if is_expl_header: continue

                found_start = True
                # If it's just "RESOLUTION", don't add it to title lines (it's a header)
                if upper_l != "RESOLUTION" and upper_l != "A RESOLUTION":
                    title_lines.append(clean_l)
                continue
        
        if found_start:
            # Stop markers
            if re.search(r'^(WHEREAS|RESOLVED|NOW THEREFORE|NOW, THEREFORE|BE IT RESOLVED|NOW BE IT|WHEREFORE|APPROVED|ADOPTED)', upper_l):
                break
            
            # Skip decorative separator lines (just dashes or underscores)
            if re.match(r'^[-_=]+$', clean_l):
                continue
            title_lines.append(clean_l)
                
    if not title_lines:
        # Fallback for files where the title is at the very top (Line 1)
        first_line = clean_line(lines[0])
        if first_line.upper().startswith("RESOLUTION "):
            title_lines = [first_line]

    title = " ".join(title_lines)
    # Clean up the prefix "A RESOLUTION" or "RESOLUTION" if it's the only thing on that line or just a header
    t_upper = title.upper()
    if t_upper.startswith("A RESOLUTION "):
        title = title[13:]
    elif t_upper.startswith("A RESOLUTION"):
        title = title[12:]
    elif t_upper.startswith("RESOLUTION "):
        title = title[11:]
    elif t_upper.startswith("RESOLUTION"):
        title = title[10:]
    
    # Use different prefix for Proposed vs Approved if we can detect it, 
    # but the process_directory handles the final label usually.
    return res_num, clean_text(title)

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
            num, title = extract_baa_info(content, filename)
            info = f"BAA {num} - {title}"
        elif doc_type == 'BILL':
            num, title = extract_bill_info(content, filename)
            # Re-normalize PB display for consistent prefix
            display_num = str(int(num)) if num.isdigit() else num
            info = f"PB-{display_num} - {title}"
        elif doc_type == 'RESOLUTION':
            num, title = extract_resolution_info(content, filename)
            prefix = "PR" if "Proposed" in directory else "Resolution"
            info = f"{prefix} {num} - {title}"
        
        # Normalize num for dictionary key to handle leading zeros
        if num.isdigit():
            num_int = int(num)
            if num_int > 10000: # Sanity check to avoid huge gaps
                continue
            num = str(num_int)
        
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
                if doc_type == 'BAA': 
                    entries[s_num] = f"BAA {s_num} - "
                elif doc_type == 'BILL': 
                    entries[s_num] = f"PB-{s_num} - "
                elif doc_type == 'RESOLUTION': 
                    prefix = "PR" if "Proposed" in directory else "Resolution"
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
bill_index = process_directory(os.path.join(base_dir, "Bills"), "BILL")
res_index = process_directory(os.path.join(base_dir, "Resolutions"), "RESOLUTION")
prop_res_index = process_directory(os.path.join(base_dir, "Proposed-Resolutions"), "RESOLUTION")

if baa_index:
    with open(os.path.join(base_dir, "BAAs/INDEX.md"), 'w') as f:
        f.write("# Index of BAAs\n\n")
        f.write("\n\n".join(baa_index) + "\n")

if bill_index:
    with open(os.path.join(base_dir, "Bills/INDEX.md"), 'w') as f:
        f.write("# Index of Proposed Bills (PB)\n\n")
        f.write("\n\n".join(bill_index) + "\n")

if res_index:
    with open(os.path.join(base_dir, "Resolutions/INDEX.md"), 'w') as f:
        f.write("# Index of Resolutions\n\n")
        f.write("\n\n".join(res_index) + "\n")

if prop_res_index:
    with open(os.path.join(base_dir, "Proposed-Resolutions/INDEX.md"), 'w') as f:
        f.write("# Index of Proposed Resolutions\n\n")
        f.write("\n\n".join(prop_res_index) + "\n")
