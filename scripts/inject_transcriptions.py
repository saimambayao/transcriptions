import os

def inject_transcription(stub_path, ocr_path):
    if not os.path.exists(stub_path) or not os.path.exists(ocr_path):
        return

    with open(stub_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
        if "## Full Text" in content:
            return

    with open(ocr_path, 'r', encoding='utf-8', errors='replace') as f:
        ocr_text = f.read()

    # Clean OCR headers - simple string replacement for common patterns
    # (Since we're avoiding re.sub here, we do it carefully)
    
    # 100% Reliable String Slicing: Find the Marker and replace everything after it
    marker = "> **Note:** This is a metadata stub."
    note_start = content.find(marker)
    
    if note_start != -1:
        # Keep everything before the note, then add the full text
        new_content = content[:note_start] + f"## Full Text\n\n{ocr_text.strip()}\n"
        with open(stub_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully injected (verified): {os.path.basename(stub_path)}")
    else:
        print(f"Marker not found: {os.path.basename(stub_path)}")

def main():
    base_dir = "legislation/bills/scraped/"
    ocr_dir = "/tmp/"
    
    if not os.path.exists(ocr_dir):
        return

    for f in os.listdir(ocr_dir):
        if f.endswith("_ocr.txt"):
            filename = f.replace("_ocr.txt", "")
            ocr_path = os.path.join(ocr_dir, f)
            
            if filename.startswith("BTA1-"):
                pb_id = filename.replace("BTA1-", "")
                stub_path = os.path.join(base_dir, "bta-1", f"{pb_id}.md")
                inject_transcription(stub_path, ocr_path)
            elif filename.startswith("BTA2-"):
                pb_id = filename.replace("BTA2-", "")
                stub_path = os.path.join(base_dir, "bta-2", f"{pb_id}.md")
                inject_transcription(stub_path, ocr_path)
            elif filename.startswith("PB-"):
                pb_id = filename
                for p in ["bta-1", "bta-2"]:
                    stub_path = os.path.join(base_dir, p, f"{pb_id}.md")
                    if os.path.exists(stub_path):
                        inject_transcription(stub_path, ocr_path)

if __name__ == "__main__":
    main()
