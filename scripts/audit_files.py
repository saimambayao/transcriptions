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
            return bold_count < 2 and header_count == 0
    except:
        return False

plain_files = []

for d in directories:
    if os.path.exists(d):
        for f in os.listdir(d):
            if f.endswith('.md') and f.lower() != 'index.md':
                path = os.path.join(d, f)
                if is_plain(path):
                    plain_files.append(path)

print(f"Found {len(plain_files)} potentially plain markdown files.")
for p in plain_files[:10]:
    print(p)
