import os
import subprocess
import time
from datetime import datetime

def check_progress():
    try:
        # 1. Run Injector
        subprocess.run(["/usr/bin/python3", "scripts/inject_transcriptions.py"], capture_output=True)
        # 2. Run Index Generator
        subprocess.run(["/usr/bin/python3", "scripts/generate_bill_index.py"], capture_output=True)
        
        # 3. Get Stats
        ocr_count = subprocess.run(["sh", "-c", "ls /tmp/PB-*_ocr.txt | wc -l"], capture_output=True, text=True).stdout.strip()
        transcribed_count = subprocess.run(["sh", "-c", 'grep -c "## Full Text" legislation/bills/scraped/bta-*/*.md | grep -v ":0" | wc -l'], capture_output=True, text=True).stdout.strip()
        
        # 4. Write to PROGRESS.md
        with open("legislation/bills/scraped/PROGRESS.md", "w") as f:
            f.write(f"# Transcription Progress Update\n\n")
            f.write(f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"| Metric | Count |\n")
            f.write(f"|:---|:---:|\n")
            f.write(f"| OCR Files Generated | {ocr_count} |\n")
            f.write(f"| Bills Successfully Transcribed | {transcribed_count} |\n\n")
            f.write(f"Next update in 3 minutes...\n")
            
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Progress updated: {transcribed_count} bills.")
    except Exception as e:
        print(f"Error in monitor: {str(e)}")

if __name__ == "__main__":
    print("Starting progress monitor (3-minute interval)...")
    while True:
        check_progress()
        time.sleep(180)
