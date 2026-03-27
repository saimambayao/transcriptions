# Speech Writing Guidebook — Progress Tracker

## Status: COMPLETE (Initial Draft)

## Files Created

| # | File | Status | Word Count (approx) |
|---|------|--------|---------------------|
| 1 | 00-table-of-contents.md | Done | TOC structure |
| 2 | 00b-about.md | Done | ~400 |
| 3 | 00c-author.md | Done | ~300 (copied from bill-drafting-manual) |
| 4 | 01-introduction.md | Done | ~800 |
| 5 | 02-chapter-01.md | Done | ~2,800 |
| 6 | 03-chapter-02.md | Done | ~2,500 |
| 7 | 04-chapter-03.md | Done | ~3,200 |
| 8 | 05-chapter-04.md | Done | ~2,800 |
| 9 | 06-chapter-05.md | Done | ~3,000 |
| 10 | 07-chapter-06.md | Done | ~3,200 |
| 11 | 08-chapter-07.md | Done | ~3,100 |
| 12 | 09-chapter-08.md | Done | ~2,500 |
| 13 | 10-chapter-09.md | Done | ~3,000 |
| 14 | 11-chapter-10.md | Done | ~2,800 |
| 15 | 12-glossary.md | Done | ~1,200 (35 terms) |
| 16 | generate-pdf.py | Done | Adapted from bill-drafting-manual |
| 17 | generate-docx.py | Done | Adapted from bill-drafting-manual |
| 18 | guidebook-template.html | Done | BARMM palette (Navy/Gold/Slate) |
| 19 | PROGRESS.md | Done | This file |

## Content Summary

- **10 chapters** covering the full speech writing lifecycle for the Bangsamoro Parliament
- **35 glossary terms** specific to parliamentary speech writing
- **BARMM-specific content**: Islamic greeting protocols (Arabic + transliteration), honorific systems, 13 ethnolinguistic groups, BDP framework references, BOL citations
- **Speech types covered**: Authorship, privilege, manifestation, interpellation, committee, motion, keynote, budget, commemorative, crisis, official messages
- **Voice**: Direct second-person, imperative mood, 15-20 word average sentences, concrete BARMM examples throughout

## Color Palette

- Navy: #1B365D
- Gold: #C5A54E
- Slate: #2C5F7C

## Generation

To generate PDF:
```
cd docs/speech-writing-guidebook/
pip3 install markdown weasyprint
python3 generate-pdf.py
```

To generate DOCX:
```
cd docs/speech-writing-guidebook/
pip3 install python-docx markdown
python3 generate-docx.py
```

## Appendices (Not Yet Created)

The following appendices are referenced in the TOC but not yet created as separate files:
- Appendix A: Speech Templates by Type (Annotated)
- Appendix B: Islamic Greeting Protocols Quick Reference
- Appendix C: BARMM Officials and Titles Reference
- Appendix D: Sample Speeches by Type (Annotated)
- Appendix E: Speaker Profile Template (Detachable)
- Appendix F: Speech Quality Review Checklist (Detachable)
- Appendix G: Speech Writing Process Flowchart

These appendices can be created as separate markdown files and added to the MD_FILES list in the generation scripts.
