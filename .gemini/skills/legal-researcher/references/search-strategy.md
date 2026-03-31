# Search Strategy — Legislative Archive

Prioritized search paths for finding legal provisions. Always search in this order.

## Tier 1: Markdown Transcriptions (Primary)

These are the fastest and most accurate sources. Always search here first.

### Bangsamoro Autonomy Acts (BAAs)
- **Path**: `~/apps/transcriptions/legislation/BAAs/`
- **Count**: 89+ enacted BAAs
- **Index**: `INDEX.md` in the same directory — search this first for BAA number/title lookup
- **File pattern**: `BAA-{N}.md` (e.g., `BAA-13.md`)
- **Search tips**: Use Grep for section numbers (`Section [0-9]+`), article numbers (`Article [IVX]+`), or topic keywords

### Filed Bills
- **Path**: `~/apps/transcriptions/legislation/Bills/`
- **Count**: 414+ filed bills
- **Index**: `INDEX.md` — search for bill number or topic
- **File pattern**: `PB-{N}.md` (e.g., `PB-123.md`)

### Adopted Resolutions
- **Path**: `~/apps/transcriptions/legislation/Resolutions/`
- **Count**: 555+ adopted resolutions
- **Index**: `INDEX.md`
- **File pattern**: `resolution{N}.md` (e.g., `resolution123.md`)

### Proposed Resolutions
- **Path**: `~/apps/transcriptions/legislation/Resolutions/proposed/` (if exists)
- **Count**: 676+ proposed resolutions

### National Laws
- **Path**: `~/apps/transcriptions/legislation/national-laws/`
- **Contents**: Transcriptions of national Republic Acts relevant to BARMM

### Parliamentary Records
- **Path**: `~/apps/transcriptions/parliamentary/`
- **Contents**: Parliamentary session records, committee reports

### Pre-reorganization Parliamentary Resolutions
- **Path**: `~/apps/transcriptions/PR-1-70/`
- **Count**: 70 Parliamentary Resolutions from the 1st Bangsamoro Parliament
- **File pattern**: `PR-{N}.md`

## Tier 2: BOL Verbatim Text

The authoritative local source for the Bangsamoro Organic Law.

- **Path**: `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/`
- **Files**: 5 chapter files covering all 18 articles
- **Fallback PDF**: `~/apps/transcriptions/source-pdfs/other/RA 11054.pdf`
- **Use for**: Any BOL provision lookup — ALWAYS check here before web search

### BOL Chapter File Mapping
| File | Articles Covered |
|------|-----------------|
| chapter-1.md | Articles I-IV (General Provisions, Rights, Territory, Government) |
| chapter-2.md | Articles V-VII (Parliament, Chief Minister, Powers) |
| chapter-3.md | Articles VIII-XII (Revenue, Shari'ah, Justice, Fiscal) |
| chapter-4.md | Articles XIII-XVI (Writ of Amparo, Basic Sectors, Transitory) |
| chapter-5.md | Articles XVII-XVIII (Amendments, Final Provisions) |

## Tier 3: Local PDFs

Use `/transcriber` to extract text from these PDFs when markdown transcriptions are unavailable.

### BAA and Resolution Source PDFs
- **Path**: `~/apps/transcriptions/source-pdfs/`
- **Contents**: Original PDF versions of BAAs, Resolutions, and other documents

### Cooperative Law PDFs
- **Path**: `~/Library/Mobile Documents/com~apple~CloudDocs/Business Development/Cooperatives/`
- **Key files**:
  - `RA 9520 - EDITABLE.pdf` — Philippine Cooperative Code of 2008
  - `RA-11364-CDA-Law.pdf` — CDA Charter
  - `BAA No. 13 - Bangsamoro Admin Code.pdf`
  - `Memorandum Circulars/` — CDA Memorandum Circulars

### Other Reference PDFs
- **Parliament assignments**: `~/apps/transcriptions/source-pdfs/other/Parliament-and-Committee-2025.pdf`
- **BOL fallback**: `~/apps/transcriptions/source-pdfs/other/RA 11054.pdf`

## Tier 4: Web Search (Last Resort)

Only use when the provision is not available in any local source.

### Authoritative Web Sources
| Source | URL Pattern | Best For |
|--------|------------|----------|
| Official Gazette | officialgazette.gov.ph | Republic Acts, Executive Orders |
| LawPhil | lawphil.net | All Philippine laws, searchable |
| Supreme Court E-Library | elibrary.judiciary.gov.ph | Case law, G.R. numbers |
| Senate Legislative Database | legacy.senate.gov.ph | National legislation |

### Web Source Labeling
Always label web-sourced provisions:
```
[Source: web — verify against official copy]
```

## Search Techniques

### By Section Number
```
Grep pattern: "Section\s+{N}" or "Sec\.\s+{N}"
Example: Search for Section 45 → Grep "Section\s+45\b"
```

### By Article Number
```
Grep pattern: "Article\s+{Roman}" or "Art\.\s+{Roman}"
Example: Search for Article VII → Grep "Article\s+VII\b"
```

### By Topic Keywords
```
Use multiple related keywords to cast a wider net.
Example: "education" OR "school" OR "curriculum" OR "learning"
```

### By BAA Number
```
1. First check INDEX.md for the BAA title
2. Then read BAA-{N}.md directly
Example: BAA No. 13 → Read BAA-13.md
```

### By Bill Number
```
Same pattern: check INDEX.md → read PB-{N}.md
```
