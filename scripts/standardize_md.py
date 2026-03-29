import re
import sys

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
        # Pattern: Section 1. Title. or Section 1. Title -
        # We want to turn: "Section 1. Title. – content" into "**Section 1. _Title._** – content"
        # Or simplistic: "**Section 1. Title.** – content"
        
        elif re.match(r'^(Section|Sec\.?)\s*\d+', stripped, re.IGNORECASE):
            # Try to split into Header and Content
            # Look for explicit delimiter like "–", "-", or just the first period ending the title?
            # BAA-5: "Section 1. Title. – This Act..."
            # Regex to capture "Section X. Title."
            match = re.match(r'^(?:Section|Sec\.?)\s*\d+\.\s*[^–\-\n]+', stripped, re.IGNORECASE)
            if match:
                header = match.group(0).strip()
                # Check if header ends with '.'
                # "Section 1. Title."
                remainder = stripped[len(header):].strip()
                
                # Further refine header: split Section X. and Title
                # Maybe just bold the whole header part
                
                # clean up header
                if header.endswith('.') or header.endswith(','): 
                    # Try to separate Title for italics?
                    # Too complex for regex, just Bold the header
                    pass
                
                line = line.replace(header, f"**{header}**", 1)
        
        # Handle Title block (lines after AN ACT before Be it enacted)
        elif in_title:
            if re.match(r'^Be it enacted', stripped, re.IGNORECASE):
                in_title = False
            elif stripped and not strip_markdown(stripped) == "":
                # Bold title lines
                line = f"**{stripped}**"

        new_lines.append(line)
        
    return '\n'.join(new_lines)

def strip_markdown(text):
    return text.replace('*', '')

if __name__ == "__main__":
    filepath = sys.argv[1]
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(standardize_content(content))
