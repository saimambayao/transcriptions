import os
import re
import json

def map_pdfs():
    base_dir = "legislation/bills/scraped/"
    pdf_map = {}
    
    for parliament in ["bta-1", "bta-2"]:
        p_short = "BTA1" if parliament == "bta-1" else "BTA2"
        md_dir = os.path.join(base_dir, parliament)
        if not os.path.exists(md_dir):
            continue
            
        files = [f for f in os.listdir(md_dir) if f.startswith("PB-") and f.endswith(".md")]
        for f in files:
            bill_id = f.replace(".md", "")
            md_path = os.path.join(md_dir, f)
            
            with open(md_path, 'r', encoding='utf-8', errors='replace') as stub:
                content = stub.read()
                pdf_link_match = re.search(r'\[Filed Copy \(PDF\)\]\((.*?)\)', content)
                if pdf_link_match:
                    pdf_url = pdf_link_match.group(1).strip()
                    pdf_filename = os.path.basename(pdf_url)
                    
                    pdf_local_path = os.path.join(base_dir, "pdfs", parliament, pdf_filename)
                    if os.path.exists(pdf_local_path):
                        # Use Unique ID including Parliament prefix
                        pdf_map[f"{p_short}-{bill_id}"] = {
                            "pdf_path": pdf_local_path,
                            "md_path": md_path,
                            "parliament": parliament,
                            "bill_id": bill_id
                        }
    
    with open("legislation/bills/scraped/pdf_map.json", 'w', encoding='utf-8') as j:
        json.dump(pdf_map, j, indent=2)
    
    print(f"Mapped {len(pdf_map)} unique Parliament bill IDs to PDFs.")

if __name__ == "__main__":
    map_pdfs()
