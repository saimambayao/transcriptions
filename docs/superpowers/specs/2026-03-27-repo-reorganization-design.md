# Repo Reorganization Design

## Context

The transcriptions repository has grown organically to 37+ subdirectories under docs/ with mixed concerns: legislative documents, guidebooks, video transcripts, reference material, source PDFs, and planning documents all coexist without clear hierarchy. Finding files is difficult, the structure doesn't communicate content types, and more guidebooks are coming. This reorganization creates a scalable, content-type-based structure.

## Target Structure

```
transcriptions/
├── legislation/
│   ├── baas/                        # BAA-1.md ... BAA-92.md + INDEX.md
│   ├── bills/
│   │   ├── enacted/                 # Merged: Bills/ + bills140-424/
│   │   └── proposed/                # From: Proposed Bills/
│   ├── resolutions/
│   │   ├── enacted/                 # Merged: Resolutions/ + resolution/
│   │   └── proposed/                # From: Proposed-Resolutions/
│   └── national-laws/               # RA-11861, RA-11054, etc.
│
├── guidebooks/
│   ├── bill-drafting/               # ver03 (latest)
│   │   ├── chapters/                # 00-*.md through 16-*.md
│   │   ├── appendices/              # Appendix A-G (.html, .pdf, .docx)
│   │   ├── images/                  # PNG/JPG assets
│   │   ├── mop/                     # Manual of Operations (.md, .pdf, .docx, .html)
│   │   └── output/                  # Final .pdf, .docx, generation scripts, templates
│   ├── csw/                         # Complete Staff Work guidebook
│   ├── mop-formulation/             # MOP Formulation guidebook
│   ├── policy-recommendations/      # Policy Recommendations guidebook
│   ├── speech-writing/              # Speech Writing guidebook
│   ├── supervision/                 # Supervision guidebook
│   ├── working-with-bangsamoro-government/  # Working with BARMM guidebook
│   └── _archive/
│       ├── bill-drafting-ver01/
│       ├── bill-drafting-ver02/
│       └── little-green-book/
│
├── transcripts/
│   ├── ai-claude-code/
│   ├── ai-claude-cowork/
│   ├── ai-design/
│   ├── ai-engineering/
│   ├── bangsamoro-governance/
│   └── lean-startup/
│       ├── business-model/
│       ├── founder-mindset/
│       ├── mvp-and-validation/
│       ├── sales-and-growth/
│       └── startup-strategy/
│
├── reference/
│   ├── constitution/                # 1987 Philippine Constitution
│   ├── bdp/                         # Bangsamoro Development Plan
│   ├── systems-ebooks/              # 32 reference ebooks
│   └── baa-no-85/                   # Detailed BAA-85 breakdown
│
├── source-pdfs/                     # Tracked, consolidated
│   ├── baas/                        # ~92 BAA PDFs (from docs/BAA-PDFs/)
│   ├── resolutions/                 # ~442 Resolution PDFs (from docs/Resolutions-PDFs/)
│   └── other/                       # Parliament assignments, RA 11054, etc. (from PDFs/)
│
├── parliamentary/
│   └── PR-47.md                     # From PR-1-70/
│
├── planning/
│   ├── GUIDEBOOK-PRODUCTION-PLAN.md
│   ├── PLAN-working-with-bangsamoro-government-guidebook.md
│   ├── PLAN-working-with-bangsamoro-government-guidebook.md.backup
│   ├── PLAN-working-with-bangsamoro-government-guidebook.md.backup-partii
│   ├── PLAN-working-with-bangsamoro-government-guidebook-autoresearch-report.md
│   ├── PLAN-working-with-bangsamoro-government-guidebook-autoresearch-report-partii.md
│   ├── PLAN-working-with-bangsamoro-government-guidebook-autoresearch-report-thins.md
│   ├── EVAL-working-with-bangsamoro-government-guidebook.md
│   └── FACT-CHECK-REPORT-guidebook13-plan.md
│
├── presentations/                   # From PPTs/
│
├── scripts/                         # Python utilities moved from root
│   ├── generate_indexes.py
│   ├── standardize_md.py
│   ├── apply_standardization.py
│   ├── audit_files.py
│   ├── debug_baa.py
│   ├── download_baas.py
│   └── download_baas.sh
│
├── docs/
│   └── superpowers/                 # Claude superpowers specs (kept)
│
├── .gitignore
├── CLAUDE.md
└── README.md
```

## Migration Rules

### Legislation consolidation

| Source | Destination | Notes |
|--------|------------|-------|
| docs/BAAs/ | legislation/baas/ | Direct move, all files |
| docs/Bills/ | legislation/bills/enacted/ | Files like BILL126.md |
| docs/bills140-424/ | legislation/bills/enacted/ | Merge, deduplicate with Bills/ |
| docs/Proposed Bills/ | legislation/bills/proposed/ | Direct move |
| docs/Resolutions/ | legislation/resolutions/enacted/ | Direct move |
| docs/resolution/ | legislation/resolutions/enacted/ | Merge, deduplicate with Resolutions/ |
| docs/Proposed-Resolutions/ | legislation/resolutions/proposed/ | Direct move |
| docs/Draft-Bills/ | legislation/bills/proposed/ | Merge with Proposed Bills |
| docs/national-laws/ | legislation/national-laws/ | Direct move |

### Guidebooks

| Source | Destination |
|--------|------------|
| docs/bill-drafting-manual/ver03/ | guidebooks/bill-drafting/ |
| docs/bill-drafting-manual/ver01/ | guidebooks/_archive/bill-drafting-ver01/ |
| docs/bill-drafting-manual/ver02/ | guidebooks/_archive/bill-drafting-ver02/ |
| docs/bill-drafting-manual/little-green-book/ | guidebooks/_archive/little-green-book/ |
| docs/bill-drafting-manual/source-ppt/ | guidebooks/_archive/bill-drafting-source-ppt/ |
| docs/bill-drafting-manual/INTEGRATION-GUIDE.md | guidebooks/bill-drafting/ |
| docs/csw-guidebook/ | guidebooks/csw/ |
| docs/mop-formulation-guidebook/ | guidebooks/mop-formulation/ |
| docs/policy-recommendations-guidebook/ | guidebooks/policy-recommendations/ |
| docs/speech-writing-guidebook/ | guidebooks/speech-writing/ |
| docs/supervision-guidebook/ | guidebooks/supervision/ |
| docs/working-with-bangsamoro-government/ | guidebooks/working-with-bangsamoro-government/ |

### Transcripts

| Source | Destination |
|--------|------------|
| docs/video-transcripts/* | transcripts/ (preserve subfolder structure) |

### Reference

| Source | Destination |
|--------|------------|
| docs/1987-CONSTITUTION-.../ | reference/constitution/ |
| docs/bdp/ | reference/bdp/ |
| docs/systems-ebooks/ | reference/systems-ebooks/ |
| docs/BAA no.85/ | reference/baa-no-85/ |

### Source PDFs

| Source | Destination |
|--------|------------|
| docs/BAA-PDFs/ | source-pdfs/baas/ |
| docs/Resolutions-PDFs/ | source-pdfs/resolutions/ |
| PDFs/ | source-pdfs/other/ |

### Other moves

| Source | Destination |
|--------|------------|
| PPTs/ | presentations/ |
| PR-1-70/ | parliamentary/ |
| Root .py and .sh files | scripts/ |
| docs/PLAN-*, EVAL-*, FACT-CHECK-*, GUIDEBOOK-PRODUCTION-PLAN | planning/ |

### Deletions

- `docs/gaab/` -- empty directory, delete
- `BAA-5_preview.md` -- preview file, delete
- `test-results/` -- add to .gitignore, remove from tracking

## .gitignore updates

Add:
```
test-results/
```

Keep existing entries. Update `PDFs/` to `source-pdfs/other/` is NOT needed since PDFs/ is being moved entirely into source-pdfs/ which is tracked.

Remove `PDFs/` from .gitignore (content moves to tracked source-pdfs/).

## Post-move updates

1. **CLAUDE.md** -- update all path references to match new structure
2. **README.md** -- update repository structure section
3. **INDEX.md files** -- verify internal links still work after moves
4. **Generation scripts** -- update file paths in Python/JS scripts that reference chapter files
5. **.gitignore** -- add test-results/, remove PDFs/ (now tracked under source-pdfs/)

## Deduplication strategy

When merging Bills/ + bills140-424/ or Resolutions/ + resolution/:
1. Compare filenames first -- if same name exists in both, compare content
2. If content identical, keep one copy
3. If content differs, keep the newer/larger version (more complete transcription)
4. Log all deduplication decisions for review

## Verification

After migration:
1. `find . -empty -type d` -- no empty directories left
2. `git diff --stat` -- verify file count matches (no files lost)
3. Check all INDEX.md files for broken internal links
4. Run `python scripts/generate_indexes.py` to regenerate indexes
5. Verify .gitignore excludes test-results/ and node_modules/
6. Spot-check 5 random files from each category to confirm correct placement
