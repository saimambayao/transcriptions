import os
import subprocess
import json
import re
import fitz # PyMuPDF
import pytesseract
from concurrent.futures import ProcessPoolExecutor

# Explicitly set tesseract path for background Workers
TESSERACT_BIN = "/opt/homebrew/bin/tesseract"
if os.path.exists(TESSERACT_BIN):
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_BIN

def ocr_bill(unique_id, data):
    pdf_path = data["pdf_path"]
    md_path = data["md_path"]
    
    # unique_id is already BTA1-PB-1 or BTA2-PB-1
    output_path = f"/tmp/{unique_id}_ocr.txt"
    
    if os.path.exists(output_path):
        return f"{unique_id}: Already OCR'd"
    
    script_path = ".gemini/skills/transcriber/scripts/extract_chapter.py"
    if not os.path.exists(script_path):
         return f"{unique_id}: Failed - script not found"
    
    try:
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        doc.close()
        
        env = os.environ.copy()
        env["PATH"] = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
        
        cmd = [
            "/usr/bin/python3", 
            script_path,
            pdf_path,
            "1", # Start Page
            str(total_pages), # End Page
            output_path # Output File
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, env=env)
        if result.returncode == 0:
            return f"{unique_id}: Success ({total_pages} pages)"
        else:
            return f"{unique_id}: Failed - {result.stderr}"
    except Exception as e:
        return f"{unique_id}: Error - {str(e)}"

def sort_key(unique_id):
    # Sort BTA1-PB-1, BTA1-PB-2, etc. (assumes format)
    num = int(re.search(r'\d+', unique_id).group())
    return num

def mass_ocr():
    map_path = "legislation/bills/scraped/pdf_map.json"
    if not os.path.exists(map_path):
        print("Map file not found.")
        return

    with open(map_path, 'r', encoding='utf-8') as f:
        pdf_map = json.load(f)

    # Filter out already transcribed ones
    pending_list = []
    for unique_id, data in pdf_map.items():
        if os.path.exists(data["md_path"]):
            with open(data["md_path"], 'r', encoding='utf-8', errors='replace') as f:
                if "## Full Text" not in f.read():
                    pending_list.append((unique_id, data))

    # Sort BTA 1 then BTA 2
    bta1_pending = sorted([x for x in pending_list if x[1]["parliament"] == "bta-1"], key=lambda x: sort_key(x[0]))
    bta2_pending = sorted([x for x in pending_list if x[1]["parliament"] == "bta-2"], key=lambda x: sort_key(x[0]))
    
    final_pending = bta1_pending + bta2_pending

    print(f"Total PDFs pending OCR: {len(final_pending)}")
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(ocr_bill, uid, d): uid for uid, d in final_pending}
        for future in futures:
            print(future.result())

if __name__ == "__main__":
    mass_ocr()
