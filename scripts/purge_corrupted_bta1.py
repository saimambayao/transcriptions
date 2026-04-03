import os
import re

def purge_corrupted_bta1():
    base_dir = "legislation/bills/scraped/bta-1/"
    if not os.path.exists(base_dir):
        return

    purged_count = 0
    for f in os.listdir(base_dir):
        if not f.endswith(".md"):
            continue
            
        path = os.path.join(base_dir, f)
        with open(path, 'r', encoding='utf-8', errors='replace') as file:
            content = file.read()
            
        # Corrupted indicators: BTA 1 content mentioning BTA 2 markers
        is_corrupted = False
        if "## Full Text" in content:
            # Check for BTA 2 or Second Parliament markers
            if "SECOND PARLIAMENT" in content or "Second Regular Session" in content or "BTA 2" in content:
                is_corrupted = True
                
        if is_corrupted:
            # Reset to a clean stub
            marker_start = content.find("## Full Text")
            if marker_start != -1:
                clean_content = content[:marker_start].strip() + "\n\n> **Note:** This is a metadata stub. Full bill text extraction pending PDF transcription.\n"
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(clean_content)
                purged_count += 1
                print(f"Purged corrupted file: {f}")

    print(f"\nTotal BTA 1 files purged of corrupted BTA 2 text: {purged_count}")

if __name__ == "__main__":
    purge_corrupted_bta1()
