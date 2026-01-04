import os
import re

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'\*+', '', text)
    text = re.sub(r'[\"“”]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_line(line):
    return line.strip().replace('*', '').replace('"', '').replace('“', '').replace('”', '').strip()

def extract_baa_info(content, filename):
    lines = content.split('\n')
    found_act = False
    title_lines = []
    print(f"DEBUG: Processing {filename}")
    for i, line in enumerate(lines):
        clean_l = clean_line(line)
        upper_l = clean_l.upper()
        # print(f"Line {i}: '{line}' -> clean: '{clean_l}'")
        
        if not found_act:
            if upper_l == "AN ACT":
                found_act = True
                print("DEBUG: Found AN ACT")
                continue
            elif upper_l.startswith("AN ACT "):
                found_act = True
                print("DEBUG: Found AN ACT startswith")
                title_lines.append(clean_l[7:])
                continue
        
        if found_act:
            if not clean_l:
                if title_lines:
                    print("DEBUG: Break on empty line with title present")
                    break
                else: 
                    continue
            if any(marker in clean_l for marker in ["Be it enacted", "SECTION", "ARTICLE", "Explanatory Note"]):
                print(f"DEBUG: Break on marker: {clean_l}")
                break
            if upper_l == "AN ACT": continue 
            title_lines.append(clean_l)
            print(f"DEBUG: Appended title line: {clean_l}")
    
    title = " ".join(title_lines)
    print(f"DEBUG: Final title: '{title}'")
    return title

filename = "BAA-24.md"
filepath = os.path.join("/Users/saidamenmambayao/apps/transcriptions/docs/BAAs", filename)
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
    extract_baa_info(content, filename)
