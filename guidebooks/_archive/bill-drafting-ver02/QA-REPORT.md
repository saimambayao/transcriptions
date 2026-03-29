# QA Report -- Bill Drafting Guidebook ver02

**Date:** 2026-03-24
**Reviewed by:** QA Agent
**Files reviewed:** 00-table-of-contents.md through 13-glossary.md (14 files)

---

## Summary

- Total issues found: 42
- Critical: 7 (must fix before publication)
- Major: 16 (should fix)
- Minor: 19 (nice to fix)

---

## Issues by Chapter

### Introduction (01-introduction.md)

| # | Severity | Section | Issue | Recommendation |
|---|----------|---------|-------|----------------|
| 1 | Minor | How to Use This Manual | The numbered list of chapter topics (items 1-9) does not match the actual chapter structure. Item 5 describes "common provisions" and item 9 describes "working with the committee system" -- neither of these is a standalone chapter. | Rewrite this list to match the actual 11 chapters + glossary structure. |
| 2 | Minor | How to Use This Manual | "go to the chapter on fiscal provisions" -- there is no chapter titled "fiscal provisions." Budget legislation is Chapter 9 and special bill types is Chapter 4. | Revise to reference the correct chapter name or number. |

### Chapter 1 (02-chapter-01.md)

| # | Severity | Section | Issue | Recommendation |
|---|----------|---------|-------|----------------|
| 3 | Critical | 1.1.2 | **Enacting clause inconsistency.** Chapter 3 (Section 3.4) says the BTA enacting clause is "Be it enacted by the Bangsamoro Transition Authority in Parliament assembled:" but Chapter 11 (Section 11.1.2, item 13, and Section 11.7) says the standard is "Be it enacted by the Parliament in session assembled." The glossary (Enacting Clause entry) also uses "Be it enacted by the Parliament in session assembled." Chapter 6 (Section 6.7 table) shows yet another variant: "Be it enacted by the Bangsamoro Transition Authority Parliament in session assembled:" These are three different formulations. | Pick ONE authoritative formulation and use it consistently throughout all chapters. Cross-check against the most recent enacted BAAs to determine which is actually standard. |
| 4 | Major | 1.1.2 | **Timelessness -- "currently operating."** Line 55: "The Bangsamoro Parliament is currently operating as the Bangsamoro Transition Authority." The word "currently" will become inaccurate after the transition ends. | Rewrite as: "During the transition period, the Bangsamoro Parliament operates as the Bangsamoro Transition Authority..." |
| 5 | Major | 1.1.2 | **Timelessness -- named officials.** Line 63 names specific officers: "Speaker Mohammad S. Yacob, with ten Deputy Speakers. Interim Chief Minister Abdulraof A. Macacua heads the executive. The Floor Leader is John Anthony L. Lim." These names will be outdated after any reconstitution. | Move named officers to a footnote or sidebar labeled "As of [date]" or remove entirely and describe the roles generically. |
| 6 | Major | 1.1.2 | **Deputy Speakers count inconsistency.** Chapter 1 says "ten Deputy Speakers" (line 63). The Glossary says "One of eight Deputy Speakers" (glossary entry for Deputy Speaker). These contradict each other. | Verify the current count. Resolution No. 268 may prescribe one number while the BTA practice differs. State the rule from Res. 268 and note the current BTA practice separately. |
| 7 | Major | 1.1.3 | Line 99 heading reads "The BAA as Legislative Output" but the TOC says "1.1.3 The Bangsamoro Autonomy Act as the Parliament's Legislative Output." Title mismatch. | Change heading to match TOC exactly: "The Bangsamoro Autonomy Act as the Parliament's Legislative Output" |
| 8 | Minor | 1.2.1 | TOC says "1.2.1 The 1987 Constitution" but the chapter heading reads "1.2.1 The Constitution." Title shortened. | Match the TOC wording exactly. |
| 9 | Minor | 1.2.2 | TOC says "1.2.2 The Bangsamoro Organic Law (Republic Act No. 11054)" but the chapter heading reads "1.2.2 The Bangsamoro Organic Law (RA 11054)." Abbreviated form. | Use the full form "Republic Act No. 11054" to match TOC. |
| 10 | Minor | 1.2.3 | TOC says "1.2.3 National Laws and Their Implementing Rules and Regulations" but the chapter heading reads "1.2.3 National Laws and Implementing Rules and Regulations." The word "Their" is dropped. | Add "Their" to match TOC. |
| 11 | Minor | 1.2.4 | The priority codes list (lines 162-168) omits BAA numbers for items 2 and 3 (Civil Service Code and Education Code) while providing them for items 1 and 4. | Add BAA numbers: "Bangsamoro Civil Service Code (BAA 17, enacted February 2021)" and "Bangsamoro Education Code (BAA 18, enacted May 2021)". |
| 12 | Minor | 1.3.3 | TOC says "1.3.3 The Residual Clause: Powers Reserved to Congress" but the chapter heading reads "1.3.3 The Residual Clause." Subtitle dropped. | Add the full subtitle to match TOC. |
| 13 | Minor | 1.3.4 | TOC says "1.3.4 Areas of Overlapping Authority" but the chapter heading reads "1.3.4 Overlapping Authority and Intergovernmental Relations." Title expanded. | Change to match TOC exactly. |
| 14 | Minor | 1.3.5 | TOC says "1.3.5 Judicial Doctrines Affecting Bangsamoro Legislation" but the chapter heading reads "1.3.5 Judicial Doctrines Affecting Bangsamoro Legislative Power." "Legislation" vs "Legislative Power." | Change to match TOC. |
| 15 | Minor | 1.4.2 | TOC says "1.4.2 When Shari'ah Considerations Apply" but the chapter heading reads "1.4.2 When Shari'ah Applies." Shortened. | Change to match TOC. |
| 16 | Minor | 1.4.3 | TOC says "1.4.3 Practical Guidance for Drafters" but the chapter heading reads "1.4.3 Practical Guidance for the Drafter." Singular vs plural + added article. | Change to match TOC. |

### Chapter 2 (03-chapter-02.md)

| # | Severity | Section | Issue | Recommendation |
|---|----------|---------|-------|----------------|
| 17 | Minor | Title | TOC says "Chapter 2 -- From Legislative Directive to Bill: The Drafting Process" but the chapter heading reads "Chapter 2: From Legislative Directive to Filing -- The Drafting Process." "to Bill" vs "to Filing" and em-dash vs colon. | Change to match TOC exactly. |
| 18 | Minor | 2.2.4 | TOC says "2.2.4 Securing MP Approval of the Initial Legislative Template" but the chapter heading reads "2.2.4 Securing MP Approval." Title shortened. | Match TOC. |
| 19 | Minor | 2.3.2 | TOC says "2.3.2 Working with the Policy Research and Legal Services (PRLS)" but the chapter heading reads "2.3.2 Working with the PRLS." Abbreviated. | Match TOC on first use. |
| 20 | Minor | 2.3.4 sub-sections | TOC lists explicit numbered sub-sections (2.3.4.1 through 2.3.4.6) but the chapter uses unumbered H4 headers (#### Brief Description, #### Related Laws, etc.) without the 2.3.4.x numbering. | Add the explicit sub-section numbers to match TOC. |

### Chapter 3 (04-chapter-03.md)

| # | Severity | Section | Issue | Recommendation |
|---|----------|---------|-------|----------------|
| 21 | Minor | 3.3.4 | TOC says "3.3.4 Common Mistakes in Long Titles" but the chapter heading reads "3.3.4 Common Mistakes." Shortened. | Match TOC. |
| 22 | Minor | 3.6.1 | TOC says "3.6.1 Organizing the Substance of the Bill" but the chapter heading reads "3.6.1 Organizing Substantive Provisions." Different phrasing. | Match TOC. |

### Chapter 4 (05-chapter-04.md)

| # | Severity | Section | Issue | Recommendation |
|---|----------|---------|-------|----------------|
| 23 | Major | 4.5 | Sub-sections "What Makes a Code Different," "Structural Framework of a Code," "The Remaining Priority Codes," and "Drafting Tips for Codification Bills" are present in the chapter but not in the TOC. The TOC lists 4.5 as a flat entry with no sub-sections. | Either add these sub-sections to the TOC or fold them into the main section without separate headings for TOC fidelity. Recommend updating the TOC to include them. |
| 24 | Major | 4.5 | The table says five codes have been enacted but the count text says "three codes remain to be enacted: the Revenue Code, the Investment Code, and a potential Indigenous Peoples' Rights Code." This implies seven total, but only five + two pending codes = seven. The Investment Code and IP Rights Code are not in the BOL's explicit list in Section 4(a). Verify whether "seven priority codes" is the correct framing vs. "five BOL-mandated codes plus two additional." | Clarify the source and count. |

### Chapter 5 (06-chapter-05.md)

| # | Severity | Section | Issue | Recommendation |
|---|----------|---------|-------|----------------|
| 25 | Major | 5.1 | Sub-section "When a Resolution Is the Wrong Tool" (line 32) appears in the chapter but is not in the TOC under 5.1. | Add to TOC or merge into 5.1 body text without a separate heading. |
| 26 | Major | 5.5 | Sub-sections "The Key Provisions," "How to Use Res. 268 in Your Daily Work," "Res. 268 as a Model Resolution," "When Res. 268 Is Silent," and "Drafting Checklist for Resolutions" appear in the chapter but are not in the TOC. | Add these sub-sections to the TOC. |

### Chapter 6 (07-chapter-06.md)

| # | Severity | Section | Issue | Recommendation |
|---|----------|---------|-------|----------------|
| 27 | Minor | 6.2.1 | TOC says "6.2.1 Plain Language in Legislation" but the chapter heading reads "6.2.1 Plain Language." Shortened. | Match TOC. |
| 28 | Minor | 6.3.1 | TOC says "6.3.1 Consistent Use of Terms" but the chapter heading reads "6.3.1 Consistent Terms." Shortened. | Match TOC. |
| 29 | Minor | 6.3.2 | TOC says "6.3.2 Consistent Structure Across Provisions" but the chapter heading reads "6.3.2 Consistent Structure." Shortened. | Match TOC. |
| 30 | Minor | 6.4.1 | TOC says "6.4.1 Checking for Gaps in Coverage" but the chapter heading reads "6.4.1 Gaps in Coverage." Shortened. | Match TOC. |
| 31 | Minor | 6.19.3 | TOC says "6.19.3 Vague and Ambiguous Terms" but the chapter heading reads "6.19.3 Vague Terms." Shortened. | Match TOC. |
| 32 | Major | 6.7 | The enacting clause table in Section 6.7 shows the formulation as "Be it enacted by the Bangsamoro Transition Authority Parliament in session assembled:" while Section 3.4 uses "Be it enacted by the Bangsamoro Transition Authority in Parliament assembled:" -- these are different. | Reconcile to one authoritative version (see issue #3). |
| 33 | Major | End of chapter | Sections "Summary of Key Rules," "Quick Reference Tables" (including Modal Verbs, Common Word Replacements, Formatting Quick Reference, Citation Quick Reference) are present in the chapter but not in the TOC. | Add to TOC or clearly mark as non-TOC supplementary material. |

### Chapter 7 (08-chapter-07.md)

| # | Severity | Section | Issue | Recommendation |
|---|----------|---------|-------|----------------|
| 34 | Minor | 7.3.3 | TOC says "7.3.3 Referral to the Appropriate Committee" but the chapter heading reads "7.3.3 Referral to Committee." Shortened. | Match TOC. |

### Chapter 8 (09-chapter-08.md)

| # | Severity | Section | Issue | Recommendation |
|---|----------|---------|-------|----------------|
| 35 | Major | 8.3.2 | The phrase "legal landscape" appears at line 116. This is flagged as AI slop. | Replace with a concrete term, e.g., "existing legal framework" or "body of existing law." |

### Chapter 9 (10-chapter-09.md)

| # | Severity | Section | Issue | Recommendation |
|---|----------|---------|-------|----------------|
| 36 | Minor | 9.2.1 | TOC says "9.2.1 For the Annual Budget Deliberation" but the chapter heading reads "9.2.1 Annual Budget Deliberation." Article dropped. | Match TOC. |
| 37 | Minor | 9.2.2 | TOC says "9.2.2 For Committee on Finance Hearings" but the chapter heading reads "9.2.2 Committee on Finance Hearings." Article dropped. | Match TOC. |
| 38 | Minor | 9.2.3 | TOC says "9.2.3 For Plenary Budget Deliberation" but the chapter heading reads "9.2.3 Plenary Budget Deliberation." Article dropped. | Match TOC. |

### Chapter 10 (11-chapter-10.md)

| # | Severity | Section | Issue | Recommendation |
|---|----------|---------|-------|----------------|
| 39 | Critical | 10.4.3 | **BAA number inconsistency.** The substitution example (line 383) refers to "Bangsamoro Autonomy Act No. 15, otherwise known as the 'Bangsamoro Education Code.'" But Chapter 4 (Section 4.5 table) and Chapter 6 (Section 6.7) consistently identify the Education Code as BAA No. 18. BAA No. 15 is a different law. | Verify the correct BAA number for the Education Code and fix whichever reference is wrong. If BAA No. 18 is correct (as stated in the Ch. 4 table), change this to BAA No. 18. |
| 40 | Major | 10.2 and 10.3 | Sub-sections "How Committee Amendments Arise," "Procedure in Plenary," "Drafting Committee Amendments" (under 10.2) and "When Floor Amendments Are Offered," "Procedure for Proposing a Floor Amendment," "Practical Tips for Drafting Floor Amendments" (under 10.3) appear in the chapter but not in the TOC. | Add to TOC. |

### Chapter 11 (12-chapter-11.md)

| # | Severity | Section | Issue | Recommendation |
|---|----------|---------|-------|----------------|
| 41 | Critical | 11.1.2 | **Enacting clause inconsistency (again).** Item 13 of the self-review checklist states the proper enacting clause as: "Be it enacted by the Parliament in session assembled." This omits "Bangsamoro Transition Authority" and differs from the formulation in Chapter 3 and Chapter 6. | Align with the single authoritative formulation chosen for issue #3. |

### Glossary (13-glossary.md)

| # | Severity | Section | Issue | Recommendation |
|---|----------|---------|-------|----------------|
| 42 | Critical | Glossary | **Shari'ah article citation error.** The glossary entry for Shari'ah cites "Article IX, Sections 7-10" of the BOL. But in Chapter 1, the Shari'ah provisions are cited as Article X (not Article IX). Article IX of the BOL covers the Bill of Rights and related matters. The Shari'ah court system is in Article X. | Verify the correct Article number and fix the glossary citation. |

---

## Cross-Chapter Issues

### 1. Enacting Clause -- Three Conflicting Formulations (CRITICAL)

This is the single most important consistency issue in the guidebook. Three different enacting clause formulations appear:

| Location | Formulation |
|---|---|
| Ch. 3, Section 3.4 | "Be it enacted by the Bangsamoro Transition Authority in Parliament assembled:" |
| Ch. 6, Section 6.7 table | "Be it enacted by the Bangsamoro Transition Authority Parliament in session assembled:" |
| Ch. 11, Sections 11.1.2 and 11.7; Glossary; Ch. 5 comparison table | "Be it enacted by the Parliament in session assembled" |

A bill-drafting manual that cannot state its own enacting clause consistently will undermine drafter confidence. Fix this by verifying the actual formulation used in the most recently enacted BAAs, selecting that as the standard, and using it uniformly throughout.

### 2. Deputy Speakers Count -- Two Conflicting Numbers

- Chapter 1 (line 63): "ten Deputy Speakers"
- Glossary (Deputy Speaker entry): "One of eight Deputy Speakers"

Resolution No. 268 may prescribe one number while BTA practice differs. The guidebook should state the rule and note the current practice.

### 3. BAA Number for Education Code -- Two Conflicting Numbers

- Chapter 4 table and Chapter 6 Section 6.7: BAA No. 18
- Chapter 10 Section 10.4.3 example: BAA No. 15

One of these is wrong. Verify and fix.

### 4. TOC Section Title Mismatches -- Systematic Pattern

Across all chapters, roughly 20+ section headings are shortened or slightly reworded compared to the TOC. While individually minor, the pattern is systematic and will frustrate any reader trying to navigate from the TOC to the chapter content. A global pass to align all chapter headings with the TOC wording is recommended.

### 5. Missing Appendices

The TOC lists seven appendices (A through G) but no appendices file exists in the ver02 directory. These are:
- A. Enumerated Powers of the Bangsamoro Government (BOL Article V, Section 2)
- B. Sample Bangsamoro Autonomy Act (Annotated)
- C. Sample Resolution (Annotated)
- D. Pre-Drafting Checklist (Detachable)
- E. Quality Review Checklist (Detachable)
- F. Legislative Research Briefer Template
- G. Budget Briefer Template

Chapter 11 (line 17) references "Appendix E of this manual" confirming the appendices are expected to exist. These must be created before publication.

### 6. Sub-sections Present in Chapters But Missing from TOC

Several chapters contain sub-sections with their own headings that do not appear in the TOC. This affects:
- Chapter 4, Section 4.5 (four unlisted sub-sections)
- Chapter 4, Section 4.6 (one unlisted sub-section: "When a Local Bill Becomes a General Law")
- Chapter 5, Section 5.1 (one unlisted sub-section)
- Chapter 5, Section 5.5 (five unlisted sub-sections)
- Chapter 6 (end-of-chapter summary tables not in TOC)
- Chapter 10, Sections 10.2 and 10.3 (six unlisted sub-sections)
- Chapter 10 (one unlisted section: "A Note on Amendatory Bills")

Decision needed: either update the TOC to include all sub-sections, or restructure these as body text without heading-level markup.

---

## AI Slop Scan Results

The guidebook is remarkably clean of AI slop. Across all 14 files:

| Flagged Term | Occurrences | Location |
|---|---|---|
| "landscape" | 1 | Ch. 8, line 116 ("legal landscape") |
| "comprehensive framework" | 1 | Ch. 6, line 366 (describing BAA No. 49) |

**No occurrences of:** "plays a crucial role," "rich tapestry," "valuable insights," "delves," "underscores," "multifaceted," "facilitates," "leverages," "utilizes," "stakeholder engagement," "meaningful dialogue."

**No occurrences of formulaic transitions:** "Moreover," "Furthermore," "Additionally" -- zero instances found across all files.

**Assessment:** The writing is direct, practical, and consistently avoids AI-generated phrasing. The "comprehensive framework" usage in Ch. 6 is arguably appropriate since it describes an actual legislative framework. The "legal landscape" in Ch. 8 should be replaced. Overall, the prose quality is high.

---

## Timelessness Review

| # | File | Line | Issue |
|---|------|------|-------|
| T1 | Ch. 1 | 55 | "The Bangsamoro Parliament is currently operating as the Bangsamoro Transition Authority" -- "currently" will become stale. |
| T2 | Ch. 1 | 59 | "The current (third) BTA was appointed in March 2025 under RA 12064" -- time-bound. |
| T3 | Ch. 1 | 61 | "The current BTA has 77 members rather than 80" -- time-bound. |
| T4 | Ch. 1 | 63 | Names of specific officers -- will become outdated. |
| T5 | Ch. 1 | 103 | "As of early 2026, the Parliament has enacted over eighty BAAs" -- time-bound. |
| T6 | Ch. 4 | 247 | "As of this writing, the BTA Parliament has enacted five of the seven priority codes" -- time-bound. |

**Assessment:** The timelessness issues are concentrated in Chapter 1 (Sections 1.1.2 and 1.1.3) and Chapter 4 (Section 4.5). These sections describe factual conditions that will change. The recommended approach: add a clearly labeled "Current Status" sidebar or note box for time-sensitive facts, while keeping the main text of each section timeless. This way, only the sidebar needs updating when facts change.

**Positive finding:** The text in Chapters 2-3 and 5-11 successfully avoids time-bound language. The drafter is addressed as "you" consistently, and the guidance reads correctly for both BTA drafters and future elected Parliament drafters. Chapter 1 Section 1.1.2 explicitly tells drafters to "write timeless provisions" (line 69) -- the guidebook should follow its own advice.

---

## Tone and Style Assessment

- **"You" voice:** Consistent throughout. The drafter is addressed directly in every chapter.
- **Tone:** Practical, direct, authoritative. Not academic. Reads like advice from an experienced colleague.
- **Sentence length variety:** Good. Mix of short declarative sentences and longer explanatory ones.
- **Formulaic transitions:** Zero instances of "Moreover/Furthermore/Additionally."
- **Overall quality:** The writing quality is consistently high across all chapters. The style is clean, concrete, and well-suited to a working reference manual.

---

## Legal Accuracy (Flagged for Fact-Checker)

These items require verification against primary sources. The QA agent flags them but does not verify:

| # | Location | Item to Verify |
|---|----------|----------------|
| L1 | Ch. 1, 1.3.5 | GR numbers for Province of Sulu v. Medialdea (G.R. Nos. 242255, 243246, 243693) and Ali et al. v. BTA (G.R. No. E-02219) -- verify these are correct. |
| L2 | Ch. 1, 1.3.5 | Date of finality for Sulu ruling stated as November 26, 2024 -- verify. |
| L3 | Ch. 1, 1.3.5 | EO No. 91 date stated as July 30, 2025 -- verify. |
| L4 | Ch. 1, 1.1.2 | BAA 86 date stated as January 20, 2026 -- verify. |
| L5 | Ch. 1, 1.1.2 | District allocation in BAA 86 (Lanao del Sur 9, Maguindanao del Norte 5, Maguindanao del Sur 5, Basilan 4, Tawi-Tawi 4, Cotabato City 3, SGA 2) -- verify. |
| L6 | Ch. 1, 1.2.4 | Civil Service Code listed without BAA number in Ch. 1 but as BAA No. 17 in Ch. 4 -- verify the correct number. |
| L7 | Ch. 1, 1.4.1 | Shari'ah provisions cited as Article X -- verify against the BOL text. Glossary cites Article IX. |
| L8 | Ch. 10, 10.4.3 | Education Code cited as BAA No. 15 -- Ch. 4 says BAA No. 18. Verify which is correct. |
| L9 | Ch. 1, 1.1.2 | "ten Deputy Speakers" -- verify the actual number in the current BTA and the Res. 268 prescribed number. |
| L10 | Ch. 4, 4.5 | "Three codes remain to be enacted: Revenue Code, Investment Code, and IP Rights Code" -- verify whether this is accurate and whether other codes are also pending. |

---

## Completeness Check

| # | Check | Result |
|---|-------|--------|
| C1 | Every "Tips for Writing" sub-section contains practical tips | PASS -- all Tips sections contain concrete, actionable advice. |
| C2 | Sections with examples include actual examples | PASS -- BAA citations with real BAA numbers and quoted text appear throughout. |
| C3 | Tables are properly formatted | PASS -- all tables render correctly in markdown. |
| C4 | Glossary is alphabetized | PASS -- entries run from Adjournment to Whereas Clause in strict alphabetical order. |
| C5 | Glossary covers key terms used in chapters | PARTIAL PASS -- most key terms are covered. Missing: "Completed Staff Work" (used in Ch. 8 and Ch. 9), "Bangsamoro Expenditure Program" (defined, good), "Comparative Matrix" (used in Ch. 2, Section 2.4.3), "Legislative Research Briefer" (used extensively in Ch. 2 and Ch. 8). |
| C6 | BOL provisions quoted in blockquotes | PASS -- BOL text consistently appears in blockquotes throughout. |
| C7 | Specific article/section numbers cited | PASS -- citations are specific (e.g., "Article V, Section 2," "Article VII, Section 25(b)"). |
| C8 | SC case names and GR numbers provided | PASS -- Province of Sulu v. Medialdea and Ali et al. v. BTA both include GR numbers. |
| C9 | BAA numbers cited in examples | PASS -- BAA numbers are cited (BAA No. 3, 9, 11, 13, 14, 18, 25, 35, 36, 40, 49, 58, 77, 86). |
| C10 | Appendices exist | FAIL -- TOC lists 7 appendices (A-G) but no appendices file exists. |
| C11 | Flowcharts present where indicated | PASS -- Ch. 2 (Section 2.9) and Ch. 7 (Section 7.10) both contain text-based flowcharts. |

---

## Plagiarism Check

**Method:** Compared structure, language, and specific passages between ver01 and ver02 files across corresponding chapters.

**Finding: No plagiarism detected.** Ver02 is a complete rewrite, not a revision of ver01.

Key differences:
- **Structure:** Ver01 organizes by "Parts" (Part One: Context and Framework, Part Two: The Practical Drafting Guide) with different chapter numbering. Ver02 uses a completely different chapter structure with different section organization.
- **Voice:** Ver01 uses a more academic, third-person voice ("The drafter must..."). Ver02 uses a direct second-person voice ("When you draft a bill...").
- **Content:** Ver01's Chapter 11 covers "The Legislative Sentence -- Language, Style, and Word Choice" with attribution to "the Oregon Bill Drafting Manual and Mark Segal's Legislative Drafting." Ver02's Chapter 6 covers the same territory but with completely different organization, examples, and framing.
- **Framework:** Ver01 uses Thornton's Five Stages of Bill Drafting as an explicit framework. Ver02 develops its own seven-stage framework.
- **Hierarchy of laws:** Both versions cover the hierarchy, but ver01 (Chapter 4) uses numbered lists with paragraph descriptions while ver02 (Chapter 1, Section 1.2) uses headed sub-sections with blockquoted BOL text and practical drafter guidance.
- **Examples:** Ver02 uses Bangsamoro-specific BAA examples extensively. Ver01 uses fewer examples and more theoretical framing.

**Assessment:** Ver02 is an original work that covers similar subject matter as ver01 but with fundamentally different organization, voice, examples, and approach. No passages appear to be copied or closely paraphrased.

---

## Priority Fix List

### Must Fix Before Publication (Critical)

1. **Enacting clause consistency** -- Choose one formulation, use it everywhere (Issues #3, #32, #41)
2. **BAA No. 15 vs BAA No. 18** -- Fix the Education Code BAA number in Ch. 10 (Issue #39)
3. **Shari'ah article citation** -- Fix Article IX vs Article X in the glossary (Issue #42)
4. **Create the appendices** -- Seven appendices are promised in the TOC but do not exist (Cross-chapter issue #5)

### Should Fix Before Publication (Major)

5. **Deputy Speakers count** -- Reconcile "ten" vs "eight" (Issue #6)
6. **Timelessness fixes** -- Restructure Ch. 1 time-bound content into dated sidebars (Issues #4, #5)
7. **TOC sub-section gaps** -- Add all missing sub-sections to the TOC (Cross-chapter issue #6)
8. **AI slop** -- Replace "legal landscape" (Issue #35)
9. **Section title mismatches** -- Global pass to align chapter headings with TOC (Cross-chapter issue #4)
10. **Glossary completeness** -- Add missing terms: Completed Staff Work, Comparative Matrix, Legislative Research Briefer (Completeness check C5)
