# Transcriptions

A documentation and transcription repository for Bangsamoro governance content -- legislative documents, guidebooks, video transcripts, and reference materials.

## Repository Structure

```
legislation/          Bangsamoro Autonomy Acts, Bills, Resolutions, national laws
guidebooks/           BARMM guidebooks (bill-drafting, CSW, MOP, supervision, etc.)
transcripts/          YouTube video transcripts organized by topic
reference/            Constitution, BDP, systems-ebooks, BAA No. 85
source-pdfs/          Source PDF documents (BAAs, Resolutions, Parliament assignments)
parliamentary/        Parliamentary records
planning/             Planning, evaluation, and fact-check documents
presentations/        PowerPoint presentations
scripts/              Python/shell utilities for markdown processing
```

## Scripts

All Python utilities are in `scripts/` and require no external dependencies (stdlib only):

- `generate_indexes.py` -- Generate INDEX.md files from legislative markdown documents
- `standardize_md.py` -- Standardize markdown formatting across files
- `apply_standardization.py` -- Batch apply standardization rules
- `audit_files.py` / `debug_baa.py` -- Diagnostic scripts for content auditing
