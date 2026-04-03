import os
import json

def audit_transcriptions():
    map_path = "legislation/bills/scraped/pdf_map.json"
    if not os.path.exists(map_path):
        print("Error: pdf_map.json not found.")
        return

    with open(map_path, 'r', encoding='utf-8') as f:
        pdf_map = json.load(f)

    # Categories
    transcribed = []
    missing_pdf = []
    failed_transcription = [] # Has PDF but no text
    missing_file = [] # File not found at all

    for unique_id, data in pdf_map.items():
        md_path = data["md_path"]
        pdf_path = data["pdf_path"]
        parliament = data["parliament"]
        bill_id = data["bill_id"]

        if not os.path.exists(md_path):
            missing_file.append(unique_id)
            continue

        with open(md_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
            has_text = "## Full Text" in content
            
            # Identify if it's explicitly marked as "No PDF" or just a stub
            is_no_pdf_stub = "(No PDF)" in content or "❌ No PDF" in content or pdf_path is None or pdf_path.strip() == ""
            
            if has_text:
                transcribed.append(unique_id)
            elif is_no_pdf_stub:
                missing_pdf.append(unique_id)
            else:
                failed_transcription.append(unique_id)

    # Print Report
    print(f"=== TRANSCRIPTION AUDIT REPORT ===")
    print(f"Total Mapped Bills: {len(pdf_map)}")
    print(f"✅ Successfully Transcribed: {len(transcribed)}")
    print(f"ℹ️ Verified (No PDF available): {len(missing_pdf)}")
    print(f"❌ FAILED (Has PDF but missing text): {len(failed_transcription)}")
    print(f"⚠️ Missing Files: {len(missing_file)}")
    
    if failed_transcription:
        print("\n--- Failed Transcription Details (First 20) ---")
        for fid in failed_transcription[:20]:
            print(f"- {fid}")
            
    if missing_file:
        print("\n--- Missing File Details ---")
        for mid in missing_file:
            print(f"- {mid}")

if __name__ == "__main__":
    audit_transcriptions()
