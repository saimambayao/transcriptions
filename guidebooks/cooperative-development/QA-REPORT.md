# QA Report — Cooperative Development Guidebook

**Date**: 2026-03-27
**Files reviewed**: 28 (20 main + 8 appendices)
**Total word count**: ~143,920

---

## Summary

| Category | Issues Found |
|----------|-------------|
| Consistency | 3 |
| Completeness | 2 |
| Style | 2 |
| Structure | 2 |
| **Total** | **9** |

---

## Issues

### CRITICAL (must fix before build)

**CRIT-01 — Scenario location mismatch: Sitio Marang**

The running scenario cooperative is set in different locations across chapters:

- **Chapter 3** (04-chapter-03.md, lines 160 and 175): "Barangay Simunul, Municipality of Simunul, Tawi-Tawi" and "Purok 3, Sitio Marang, Barangay Simunul, Simunul, Tawi-Tawi"
- **Chapter 4** (05-chapter-04.md, lines 163, 167, 181–182): "Municipality of Bongao, Province of Tawi-Tawi" and "Barangay Lamion, Municipality of Bongao, Province of Tawi-Tawi, 7500"

The cooperative is named "Sitio Marang Seaweed Farmers Marketing Cooperative" in Chapter 4 — but the barangay, municipality, and zip code are different from Chapter 3's economic survey. A reader following the scenario across chapters will see conflicting addresses. Decide on one canonical location (Simunul or Bongao) and apply it consistently to both chapters.

**CRIT-02 — Invalid cross-reference in Chapter 1**

`02-chapter-01.md`, line 62:
> "...alignment with both RA 9520 and BTA Bill 210 (Chapter 5)"

Chapter 5 is the governance chapter (General Assembly, Board, Committees). The RA 9520 vs. BTA Bill 210 legal comparison and transition analysis is in **Chapter 14**. The reference should read "Chapter 14" or be reworded (e.g., "throughout this guidebook, particularly Chapter 14").

---

### MINOR (should fix when feasible)

**MIN-01 — Inconsistent spelling: "multi-purpose" vs "multipurpose"**

The preferred house style appears to be "multi-purpose" (dominant in chapters 1–3, 5, 9, 10) but several chapters use "multipurpose" without hyphen:

| File | "multipurpose" uses |
|------|----------------------|
| 05-chapter-04.md | 4 uses |
| 07-chapter-06.md | 2 uses |
| 08-chapter-07.md | 1 use |
| 12-chapter-11.md | 6 uses |
| 16-glossary.md | 1 use (glossary entry header) |

The glossary entry is titled "**Multipurpose Cooperative**" (no hyphen), while Chapter 2 — which is the authoritative chapter on cooperative types — uses "Multi-Purpose" throughout (16 uses). The TOC also uses "Multi-Purpose." Standardize to "multi-purpose" (hyphenated) to match Chapter 2 and the TOC, OR update the glossary entry header to match. The glossary entry should be the controlling form.

**MIN-02 — CSEA expanded after first use in Chapter 1**

`02-chapter-01.md`, line 60: "regional cooperative officers from CSEA" — CSEA used without expansion. The expansion "Cooperative and Social Enterprise Authority (CSEA)" first appears at line 362 in the same chapter. Since this is an early paragraph in a chapter-length work, readers encountering line 60 will not yet know what CSEA means. Add the expansion at first use or add a note that CSEA is defined at Section 1.5.2.

**MIN-03 — CDA used without expansion in Chapter 6**

`07-chapter-06.md`, line 161: "The CDA Model Bylaws require all of the following" — CDA is used without expansion. This chapter never expands CDA (Cooperative Development Authority) before this reference. The term appears only in footnotes after this point. Add "(CDA)" expansion at first body-text use.

**MIN-04 — Section heading mismatch: TOC vs Chapter 9**

TOC lists: `9.1 Why Compliance Matters`
Actual heading in `10-chapter-09.md`: `## 9.1 Why Compliance Matters (And What Happens When You Fail)`

The fuller heading is more descriptive and should be in the TOC. This is cosmetic but will look wrong in a PDF with auto-generated page links.

**MIN-05 — Section heading mismatch: TOC vs Chapter 10**

TOC lists: `10.1 The Fifth Cooperative Principle`
Actual heading: `## 10.1 The Fifth Cooperative Principle: Education, Training, and Information`

Same issue — the TOC truncates the actual heading. Align both.

**MIN-06 — Dash style inconsistency in chapter H1 titles**

Some chapters use em dash (—), others use double hyphen (--):

| File | H1 dash style |
|------|---------------|
| 02-chapter-01.md | `--` (double hyphen) |
| 03-chapter-02.md | `—` (em dash) |
| 04-chapter-03.md | `—` (em dash) |
| 05-chapter-04.md | `--` (double hyphen) |
| 06-chapter-05.md | `—` (em dash) |
| 07-chapter-06.md | `—` (em dash) |
| 08-chapter-07.md | `—` (em dash) |
| 09-chapter-08.md | `—` (em dash) |
| 10-chapter-09.md | `—` (em dash) |
| 11-chapter-10.md | `—` (em dash) |
| 12-chapter-11.md | `—` (em dash) |
| 13-chapter-12.md | `--` (double hyphen) |
| 14-chapter-13.md | `--` (double hyphen) |
| 15-chapter-14.md | `—` (em dash) |

The TOC uses `—` (em dash) for all. Files 01, 04, 12, 13 should be updated to match. Low priority for prose reading, high priority for PDF rendering.

**MIN-07 — "In order to" in Ch13 footnote (direct quote)**

`14-chapter-13.md`, lines 305 and 482: "in order to legally conduct businesses" appears in both body text and footnote as a **verbatim quote from BDP 2023-2028**. This is acceptable since it is a direct citation, not original prose. No action needed — noted for completeness.

**MIN-08 — "is recommended" in Ch4 (passive voice)**

`05-chapter-04.md`, line 116: "An **odd number** is recommended to prevent tie votes." Minor passive construction in an otherwise direct chapter. Low priority.

**MIN-09 — Second Scenario ("Maimbung Seaweed Producers Cooperative") not cross-referenced**

Chapter 7 introduces a second named seaweed cooperative — the **Maimbung Seaweed Producers Cooperative** (75 members) — as a financial worked example. This is distinct from the Sitio Marang scenario used in Chapters 3–4. The distinction is fine (different examples serve different purposes), but the guidebook never acknowledges that these are separate illustrative cooperatives. Consider a one-line note at Chapter 7's first use: "The following worked examples use a different illustrative cooperative from the Sitio Marang scenario, as financial structures vary by cooperative size."

---

## File Inventory

| File | Exists | Word Count | Footnotes | Status |
|------|--------|------------|-----------|--------|
| 00-table-of-contents.md | Y | 1,653 | 0 | OK — front matter |
| 00b-about.md | Y | 522 | 0 | OK — front matter |
| 00c-author.md | Y | 289 | 0 | OK — front matter |
| 01-introduction.md | Y | 1,621 | 7 | OK |
| 02-chapter-01.md | Y | 7,128 | 59 | Issue (CRIT-02, MIN-02) |
| 03-chapter-02.md | Y | 6,246 | 69 | OK |
| 04-chapter-03.md | Y | 7,323 | 33 | Issue (CRIT-01) |
| 05-chapter-04.md | Y | 9,416 | 55 | Issue (CRIT-01, MIN-08) |
| 06-chapter-05.md | Y | 9,169 | 49 | OK |
| 07-chapter-06.md | Y | 7,011 | 52 | Issue (MIN-03) |
| 08-chapter-07.md | Y | 8,498 | 55 | Issue (MIN-09) |
| 09-chapter-08.md | Y | 7,042 | 22 | OK |
| 10-chapter-09.md | Y | 8,119 | 67 | Issue (MIN-04) |
| 11-chapter-10.md | Y | 7,325 | 45 | Issue (MIN-05) |
| 12-chapter-11.md | Y | 6,110 | 36 | Issue (MIN-01) |
| 13-chapter-12.md | Y | 6,429 | 44 | Issue (MIN-06) |
| 14-chapter-13.md | Y | 8,002 | 63 | Issue (MIN-06) |
| 15-chapter-14.md | Y | 5,853 | 66 | OK |
| 16-glossary.md | Y | 7,482 | 158 | Issue (MIN-01) |
| 17-appendices.md | Y | 313 | 0 | OK — index only |
| appendices/Appendix-A-AOC-Templates.md | Y | 3,639 | 0 | OK — template doc |
| appendices/Appendix-B-Bylaws-Template.md | Y | 6,770 | 0 | OK — template doc |
| appendices/Appendix-C-Registration-Checklist.md | Y | 1,978 | 0 | OK — template doc |
| appendices/Appendix-D-Compliance-Calendar.md | Y | 3,078 | 0 | OK — template doc |
| appendices/Appendix-E-Meeting-Templates.md | Y | 2,732 | 0 | OK — template doc |
| appendices/Appendix-F-Financial-Templates.md | Y | 3,854 | 0 | OK — template doc |
| appendices/Appendix-G-Training-Templates.md | Y | 3,522 | 0 | OK — template doc |
| appendices/Appendix-H-Quick-Reference-Cards.md | Y | 2,525 | 0 | OK — template doc |

Notes:
- Appendices have no footnotes — this is expected and acceptable; they are template documents, not expository prose.
- 17-appendices.md has no footnotes — it is a brief index/cover page; acceptable.
- 00-table-of-contents.md, 00b-about.md, 00c-author.md: front matter; no footnotes expected.

---

## Cross-Reference Check

| Reference | Source | Points to | Valid? |
|-----------|--------|-----------|--------|
| "Chapter 5" (BTA Bill 210 alignment) | 02-chapter-01.md:62 | Chapter 5 = Governance | **NO** — should be Chapter 14 |
| "Chapter 4" (registration) | 00b-about.md | Chapter 4 = Registration | YES |
| "Chapter 5" (governance) | 00b-about.md, 01-introduction.md | Chapter 5 = Governance | YES |
| "Chapter 7" (financial management) | 00b-about.md | Chapter 7 = Financial Mgmt | YES |
| "Chapter 9" (compliance) | 00b-about.md | Chapter 9 = Compliance | YES |
| "Chapter 13" (CSEA ecosystem) | 01-introduction.md:29 | Chapter 13 = CSEA Ecosystem | YES |
| "Chapter 14" (BTA Bill 210 transition) | 01-introduction.md:29, 47 | Chapter 14 = BTA Future | YES |
| "Chapter 10" (training framework) | 04-chapter-03.md footnote ^33 | Chapter 10 = Training | YES |
| "Chapter 7" (Shari'ah finance) | 04-chapter-03.md:469 | Chapter 7 = Financial Mgmt | YES |
| "Chapter 4" (bank account) | 09-chapter-08.md:475 | Chapter 4 = Registration | YES |
| "Section 9.3" (CAFS) | 10-chapter-09.md:102 | Section 9.3 = CAFS section | YES |
| "Chapter 9" (compliance calendar) | 14-chapter-13.md:138 | Chapter 9 = Compliance | YES |
| "Chapter 4, Section 4.2" | 17-appendices.md:8 | Section 4.2 = AOC content | YES |
| "Chapter 4, Section 4.3" | 17-appendices.md:11 | Section 4.3 = Bylaws | YES |
| "Chapter 4, Section 4.4" | 17-appendices.md:14 | Section 4.4 = Documentary Reqs | YES |
| "Chapter 5" | 17-appendices.md:20 | Chapter 5 = Governance | YES |
| "Section 5.4.2" (Shari'ah Committee) | 06-chapter-05.md:290 | Section 5.4.2 exists | YES |
| "Section 2.2.2" (Multi-Purpose mistakes) | 03-chapter-02.md:53 | Section 2.2.2 exists | YES |

**Invalid cross-references found: 1** (CRIT-02 above)

---

## Placeholder Scan

Searched for: `[TODO]`, `[TBD]`, `[UNVERIFIED]`, `[verify:]`, `[GAP:]`, `[placeholder]`

**Result: No placeholder markers found.** All chapters appear complete.

---

## Style Compliance Spot-Check

**Chapters spot-checked**: 02 (Ch1), 06 (Ch5), 10 (Ch9)

| Check | Ch1 | Ch5 | Ch9 | Result |
|-------|-----|-----|-----|--------|
| "It is important to note" | 0 | 0 | 0 | PASS |
| "It should be noted" | 0 | 0 | 0 | PASS |
| "In order to" | 0 | 0 | 0 | PASS |
| "With regard to" | 0 | 0 | 0 | PASS |
| "In the context of" | 0 | 0 | 0 | PASS |
| Second-person ("you/your") | 43 uses | 27 uses | 88 uses | PASS |
| Bold key terms (**Term**) | 95 instances | 202 instances | 160 instances | PASS |

Note: "In order to" appears twice in `14-chapter-13.md` but both are **verbatim quotes from BDP 2023-2028** — acceptable.

---

## Cooperative Type Terminology

| Term | Main user | Chapters |
|------|-----------|---------|
| "multi-purpose" (hyphenated) | Chapter 2, TOC, Chs 1, 5, 9, 10 | Dominant form |
| "multipurpose" (no hyphen) | Chs 4, 6, 7, 11, Glossary | Needs standardization |

**Recommendation**: Standardize to "multi-purpose" throughout. The glossary entry header "Multipurpose Cooperative" should be updated to "Multi-Purpose Cooperative" to match the TOC.

---

## Seaweed Scenario Consistency

The guidebook uses two distinct seaweed cooperative examples:

1. **Sitio Marang Seaweed Farmers Marketing Cooperative** — used in Chapters 3 and 4 as the running pre-formation and registration scenario. **Location conflict: Simunul (Ch3) vs. Bongao/Barangay Lamion (Ch4).** See CRIT-01.

2. **Maimbung Seaweed Producers Cooperative** (75 members) — used in Chapter 7 for financial worked examples (capital build-up, net surplus, patronage refunds). This is a separate illustrative cooperative and is not connected to the Sitio Marang scenario. It is used consistently within Chapter 7 only. No issues — but consider a brief clarifying note at first use.

Both scenarios are internally consistent within their respective chapters (except for the CRIT-01 location conflict).

---

## Summary of Actions Required

| Priority | Issue | File(s) | Fix |
|----------|-------|---------|-----|
| CRITICAL | CRIT-01: Sitio Marang location mismatch | 04-chapter-03.md, 05-chapter-04.md | Pick one location (Simunul or Bongao) and standardize across both files |
| CRITICAL | CRIT-02: Invalid "Chapter 5" cross-reference | 02-chapter-01.md:62 | Change to "Chapter 14" or "throughout this guidebook, particularly Chapter 14" |
| Minor | MIN-01: multi-purpose vs multipurpose | Chs 4, 6, 7, 11, Glossary | Replace all "multipurpose" with "multi-purpose" |
| Minor | MIN-02: CSEA not expanded at first use | 02-chapter-01.md:60 | Add "(Cooperative and Social Enterprise Authority)" at first use |
| Minor | MIN-03: CDA not expanded at first use | 07-chapter-06.md:161 | Add "(Cooperative Development Authority)" or "(CDA)" at first body-text use |
| Minor | MIN-04: TOC section heading truncated (Ch9) | 00-table-of-contents.md | Update to match actual heading |
| Minor | MIN-05: TOC section heading truncated (Ch10) | 00-table-of-contents.md | Update to match actual heading |
| Minor | MIN-06: Em dash vs double-hyphen in H1 titles | Chs 1, 4, 12, 13 | Replace `--` with `—` in chapter H1 headings |
| Low | MIN-09: Second scenario not flagged | 08-chapter-07.md | Add brief clarifying note at first use of Maimbung Cooperative |
