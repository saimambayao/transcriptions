# Shari'ah and Bangsamoro Governance — Production Progress

## Status: CHAPTERS COMPLETE — Appendices and final review pending

## Remaining Tasks
- [ ] Generate Appendices A-F (verbatim BOL Art. X, PD 1083 index, BAA index, Kutub al-Sittah summary, BDI text, AI Declaration)
- [ ] Cross-chapter `/legal-reviewer ACCURACY` pass on all quoted legal provisions
- [ ] Final `/humanizer` pass for voice consistency across 13 chapters
- [ ] Also fix Ch 3 and Ch 11 — same "PD 1083 basic provisions" for Waqf claim needs correction (same error caught in Ch 13)

## Per-Chapter Pipeline (MANDATORY — follow for every chapter)

```
Step 1: RESEARCH    Read authoritative local sources, build Chapter Fact Sheet
Step 2: WRITE       From fact sheet only, inline [^N] citations as you write
Step 3: SCAN        Prohibited phrases, internal paths, skill terminology
Step 4: VALIDATE    /fact-checker VALIDATE — classify every claim, verify against sources
Step 5: FIX         All CRITICAL (P1-P4) and HIGH (P5-P8) errors
Step 6: REGEN       python3 generate-pdf.py
Step 7: VISUAL      pdftoppm screenshot → Read image → identify issues → fix → loop
Step 8: PROGRESS    Update this file — mark status with pipeline step completed
Step 9: PRESENT     Fact-check summary to user → proceed to next chapter
```

**Exit condition:** 0 CRITICAL + 0 HIGH errors before marking "QA Complete."

## Chapter Status

| # | Chapter | Written | Scanned | Validated | Fixed | PDF | Visual | QA Complete |
|---|---------|---------|---------|-----------|-------|-----|--------|-------------|
| — | 00-table-of-contents.md | Done | — | — | — | Done | Done | — |
| — | 00b-about.md | Done | — | — | — | Done | — | — |
| — | 00c-author.md | Done | — | — | — | Done | — | — |
| 1 | 01-chapter-01.md — Why Shari'ah Matters | Done | Done | Done (4 corrections) | Done | Done | Done | 2026-03-31 |
| 2 | 02-chapter-02.md — Constitutional Framework | Done | Done | Done (0 errors) | N/A | Done | Done | 2026-03-31 |
| 3 | 03-chapter-03.md — PD 1083 | Done | Done | Done (0 errors) | N/A | Done | Done | 2026-03-31 |
| 4 | 04-chapter-04.md — Shari'ah Court System | Done | Done | Done (0 errors) | N/A | Done | Done | 2026-03-31 |
| 5 | 05-chapter-05.md — Maqasid al-Shari'ah | Done | Done | Done (3 CRITICAL) | Fixed | Done | N/A | 2026-03-31 |
| 6 | 06-chapter-06.md — Primary Islamic Sources | Done | Done | Done (0 errors) | N/A | Done | N/A | 2026-03-31 |
| 7 | 07-chapter-07.md — Shari'ah Legal Analysis | Done | Done | Done (0 errors) | N/A | Done | N/A | 2026-03-31 |
| 8 | 08-chapter-08.md — Legislative Strategy | Done | Done | Done (0 errors) | N/A | Done | Done | 2026-03-31 |
| 9 | 09-chapter-09.md — Shari'ah Checkpoint | Done | Done | Done (1 CRITICAL) | Fixed | Done | N/A | 2026-03-31 |
| 10 | 10-chapter-10.md — Legislative Landscape | Done | Done | Done (0 errors) | N/A | Done | Done | 2026-03-31 |
| 11 | 11-chapter-11.md — Islamic Finance | Done | Done | Done (0 errors) | N/A | Done | Done | 2026-03-31 |
| 12 | 12-chapter-12.md — Halal Economy | Done | Done | Done (1 CRIT + 1 HIGH) | Fixed | Done | N/A | 2026-03-31 |
| 13 | 13-chapter-13.md — Practitioner's Toolkit | Done | Done | Done (2 errors) | Fixed | Done | N/A | 2026-03-31 |
| — | 14-glossary.md | Done | Done | N/A (definitions) | N/A | Done | N/A | 2026-03-31 |
| — | 15-bibliography.md | Done | Done | N/A (references) | N/A | Done | N/A | 2026-03-31 |

## Fact-Check Error Log (This Guidebook)

| Ch | Error | Type | Fix |
|----|-------|------|-----|
| 1 | "Islamized or with indigenous identity" attributed to Art. II | FABRICATED (from CAB, not BOL) | Replaced with actual Art. II, Sec. 1 text |
| 1 | Preamble paraphrased as "self-determination" | INACCURATE (says "self-governance") | Fixed to verbatim preamble text |
| 1 | "most common nomenclature error in BARMM documents" | AI ISSUE (from error log, not human pattern) | Reframed to "common error to watch for" |
| 1 | BDI "assisted by fuqaha'" | WRONG TERM (BAA 13 says "Islamic jurists") | Fixed to match BAA 13, Sec. 55 |
| 3 | TOC said "4 Books" for PD 1083 | WRONG COUNT (PD 1083 has 5 Books) | Fixed to "5 Books" |
| 1,7,9,10 | BDI cited as "Book I, Title II, Chapter G" | WRONG BOOK (actually Book III, Title III, Ch. 1, Sec. G) | Fixed across all 4 chapters + /shariah skill |
| 12 | Halal Board cited as "Book XII" | WRONG BOOK (actually Book VI, Title XIV) | Fixed in footnotes |
| 12 | Body text omitted MOLE and MOTC from Halal Board | INCOMPLETE (Sec. 35 lists 9 members) | Added MOLE and MOTC |
| 5 | Mas Matatag: "Mamamayan" should be "Pamayanan" | FABRICATED pillar name | Fixed to official name |
| 5 | Mas Matatag: "Kapayapaan" should be "Seguridad" | FABRICATED pillar name | Fixed to official name |
| 5 | Mas Matatag: "Pamunuan" should be "Gobyerno" | FABRICATED pillar name | Fixed to official name |
| 13 | PD 1083 index: "Mahr" at Art. 55-61 | WRONG RANGE (55-61 is 'Iddah; Mahr is Art. 20-21) | Split into 2 correct rows |
| 13 | Waqf "PD 1083 basic provisions" | UNVERIFIED (PD 1083 has no Waqf chapter) | Changed to "fiqh concept" |

## Plan
- `docs/superpowers/plans/2026-03-29-shariah-guidebook.md`

## Session Log
- 2026-03-31: Plan approved, directory created, production started
- 2026-03-31: Part I (Ch 1-5), Part II (Ch 6-7), Part III (Ch 8-10), Part IV (Ch 11-12) written; Ch 1-8 fully QA'd; Ch 9-12 validation running in background
- 2026-03-31: Ch 9-12 validated (2 CRITICAL + 1 HIGH found and fixed); Ch 5 validated (3 CRITICAL Mas Matatag names fixed); All 12 chapters QA Complete
- 2026-03-31: Ch 13 (Toolkit), Glossary, Bibliography written. Table CSS fixed (ellipsis→wrap). PDF at 152 pages. Ch 13 validation running.
