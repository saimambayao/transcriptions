import os
import re
import json

def generate_index(parliament):
    base_dir = f"legislation/bills/scraped/{parliament}"
    if not os.path.exists(base_dir):
        return

    bill_files = sorted([f for f in os.listdir(base_dir) if f.startswith("PB-") and f.endswith(".md")], 
                        key=lambda x: int(re.search(r'\d+', x).group()))

    index_content = f"# {parliament.upper()} Bills Index\n\n"
    index_content += "| bill_id | Title | Status | As of | PDF | Transcription |\n"
    index_content += "| --- | --- | --- | --- | --- | --- |\n"

    for f in bill_files:
        path = os.path.join(base_dir, f)
        with open(path, 'r', encoding='utf-8', errors='replace') as file:
            content = file.read()
            
        # Extract metadata
        title_match = re.search(r'^# .*?\n\n\*\*(.*?)\*\*', content, re.MULTILINE | re.DOTALL)
        title = title_match.group(1).replace('\n', ' ').strip() if title_match else "No Title"
        
        status_match = re.search(r'\*\*Status:\*\* (.*)', content)
        as_of_match = re.search(r'\*\*As of:\*\* (.*)', content)
        pdf_match = re.search(r'\[Filed Copy \(PDF\)\]\((.*?)\)', content)
        
        bill_id = f.replace(".md", "")
        status = status_match.group(1).strip() if status_match else "Unknown"
        as_of = as_of_match.group(1).strip() if as_of_match else "Unknown"
        pdf_link = f"[PDF]({pdf_match.group(1)})" if pdf_match else "❌ No PDF"
        
        # Check Transcription Status
        if "## Full Text" in content:
            trans_status = "✅ Complete"
        elif "No PDF" in pdf_link or "pending PDF transcription" in content:
             trans_status = "❌ No PDF" if "No PDF" in pdf_link else "⏳ Pending"
        else:
             trans_status = "⏳ Pending"
             
        # Shorten extreme titles for table readability
        if len(title) > 100:
            title = title[:97] + "..."

        index_content += f"| [{bill_id}]({f}) | {title} | {status} | {as_of} | {pdf_link} | {trans_status} |\n"

    with open(os.path.join(base_dir, "INDEX.md"), 'w', encoding='utf-8') as file:
        file.write(index_content)
    print(f"Index generated for {parliament}")

if __name__ == "__main__":
    generate_index("bta-1")
    generate_index("bta-2")
