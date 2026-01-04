import os
import re

directories = [
    "/Users/saidamenmambayao/apps/transcriptions/docs/BAAs",
    "/Users/saidamenmambayao/apps/transcriptions/docs/bills",
    "/Users/saidamenmambayao/apps/transcriptions/docs/resolution"
]

def is_plain(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content.strip(): return False
            # Count markdown distinctives
            bold_count = content.count('**')
            header_count = content.count('# ')
            # If very few bolds/headers, treat as plain
            return bold_count < 5 and header_count == 0
    except:
        return False

def standardize_content(content):
    lines = content.split('\n')
    new_lines = []
    
    in_title = False
    
    for line in lines:
        stripped = line.strip()
        
        # Bold Main Headers
        if re.match(r'^(BANGSAMORO AUTONOMY ACT NO\.|RESOLUTION NO\.|BILL NO\.|PROPOSED RESOLUTION NO\.|PARLIAMENT BILL NO\.)', stripped, re.IGNORECASE):
            line = f"**{stripped}**"
            
        elif stripped.upper() == "AN ACT" or stripped.upper() == "A RESOLUTION":
            line = f"**{stripped}**"
            in_title = True
        
        # Bold Article Headers
        elif re.match(r'^ARTICLE\s+[IVX\d]+', stripped, re.IGNORECASE):
            line = f"**{stripped}**"
            
        # Bold Section Headers
        elif re.match(r'^(Section|Sec\.?)\s*\d+', stripped, re.IGNORECASE):
            # Attempt to split by separator " – " or " - "
            match_sep = re.search(r'\s([–-])\s', stripped)
            if match_sep:
                sep_idx = match_sep.start()
                head = stripped[:sep_idx]
                tail = stripped[sep_idx:]
                line = f"**{head}**{tail}"
            else:
                # Fallback: look for Section X. Title.
                # Match Section X. .*? .
                match_dot = re.match(r'^(Section|Sec\.?)\s*\d+\.\s*.*?\.', stripped, re.IGNORECASE)
                if match_dot:
                    head = match_dot.group(0)
                    tail = stripped[len(head):]
                    line = f"**{head}**{tail}"
                else:
                    # Just bold the "Section X." part? Or leave it?
                    # Let's bold "Section X."
                    match_basic = re.match(r'^(Section|Sec\.?)\s*\d+\.', stripped, re.IGNORECASE)
                    if match_basic:
                        head = match_basic.group(0)
                        tail = stripped[len(head):]
                        line = f"**{head}**{tail}"
        
        # Handle Title block (lines after AN ACT before Be it enacted)
        elif in_title:
            if re.match(r'^Be it enacted', stripped, re.IGNORECASE):
                in_title = False
            elif stripped and not stripped.replace('*', '') == "":
                # Bold title lines
                line = f"**{stripped}**"

        new_lines.append(line)
        
    return '\n'.join(new_lines)

processed_count = 0
for d in directories:
    if os.path.exists(d):
        for f in os.listdir(d):
            if f.endswith('.md') and f.lower() != 'index.md':
                path = os.path.join(d, f)
                if is_plain(path):
                    print(f"Processing {path}...")
                    with open(path, 'r', encoding='utf-8') as file:
                        content = file.read()
                    
                    new_content = standardize_content(content)
                    
                    with open(path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    processed_count += 1

print(f"Standardized {processed_count} files.")
