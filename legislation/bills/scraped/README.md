# Scraped Bills — Bangsamoro Parliament

Metadata stubs scraped from [parliament.bangsamoro.gov.ph](https://parliament.bangsamoro.gov.ph/) via WP REST API.

> **Not to be confused with `legislation/bills/proposed/`** which contains **manually transcribed** full-text bills (PB-1 to PB-424). Do not write to `proposed/`.

## Directory Structure

```
scraped/
├── bta-1/          # BTA 1 (2019–2022) — 208 metadata stubs
│   └── INDEX.md    # Full bill list with PDF and status notes
├── bta-2/          # BTA 2 (Sep 2022–present) — 441+ metadata stubs
│   └── INDEX.md    # Full bill list with PDF and status notes
├── pdfs/
│   ├── bta-1/      # 187 PDFs downloaded (all available from parliament site)
│   └── bta-2/      # PDFs downloading (all available from parliament site)
├── README.md       # This file
├── download_pdfs.py    # Re-run to download any remaining PDFs
└── inject_bill_text.py # Inject pdftotext output into stubs (text-based PDFs only)
```

## Stub Format

Each `PB-N.md` stub contains:
- Bill number, title, parliament (BTA 1 or 2)
- Status and legislative history
- Principal and co-authors
- Filed Copy PDF link (if uploaded on parliament site)
- Full text section (only for the ~9 text-based PDFs; rest are scanned images)

## PDF Coverage Notes

**Most PDFs are scanned images** — `pdftotext` returns empty. OCR via `/transcriber` or `tesseract` is needed for full text extraction.

Bills with **no PDF on parliament site** (source gap, not a download failure):
- BTA 1: Bill Nos. 2, 12, 33, 44, 54, 57, 61, 62, 69, 70, 87, 112, 117, 119, 129, 131, 134, 144, 145, 149, 156, 186, 189, 194, 199, 200, 207
- BTA 2: Bill Nos. 113, 125, 212, 307, 311, 313, 317, 318, 361, 437, 438, 439, 440, 442

## Scripts

```bash
# Re-run the scraper (safe — skips existing stubs)
python3 scripts/scrape_bta_bills.py --bta all

# Download any remaining PDFs
python3 legislation/bills/scraped/download_pdfs.py

# Inject text from text-based PDFs into stubs
python3 legislation/bills/scraped/inject_bill_text.py

# Dry-run to see what would happen
python3 legislation/bills/scraped/download_pdfs.py --dry-run
python3 legislation/bills/scraped/inject_bill_text.py --dry-run
```

## Source

- REST API: `https://parliament.bangsamoro.gov.ph/wp-json/wp/v2/bta-bills` (BTA 1)
- REST API: `https://parliament.bangsamoro.gov.ph/wp-json/wp/v2/bta-bills-22` (BTA 2)
- Scraped: 2026-04-02
