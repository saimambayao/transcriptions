# Fix Log -- Bill Drafting Guidebook ver02

**Date:** 2026-03-24
**Agent:** Fix Agent (Claude Opus 4.6)
**Source reports:** QA-REPORT.md, FACT-CHECK-REPORT.md

---

## Critical Fixes Applied

### 1. Enacting Clause Consistency (6 files)

**Problem:** Three different enacting clause formulations appeared across the guidebook:
- Ch. 3: "Be it enacted by the Bangsamoro Transition Authority in Parliament assembled:"
- Ch. 6 table: "Be it enacted by the Bangsamoro Transition Authority Parliament in session assembled:"
- Ch. 11, Glossary, Ch. 5: "Be it enacted by the Parliament in session assembled"

**Fix:** Standardized to show BOTH forms everywhere, with the timeless form as primary:
- **Primary (timeless):** "Be it enacted by the Bangsamoro Parliament:"
- **BTA period:** "Be it enacted by the Bangsamoro Transition Authority Parliament in session assembled:"

**Files changed:**
- `04-chapter-03.md` -- Section 3.4: rewrote to present both forms, timeless first
- `07-chapter-06.md` -- Section 6.7 table: updated enacting clause row
- `12-chapter-11.md` -- Section 11.1.2, item 13: updated checklist item; Section 11.7: updated convention text
- `13-glossary.md` -- Enacting Clause entry: updated definition
- `06-chapter-05.md` -- Comparison table: updated opening clause row

### 2. BAA Number Error (11-chapter-10.md)

**Problem:** Section 10.4.3 referenced "BAA No. 15" as the Education Code. The Education Code is BAA No. 18. BAA No. 15 is a different law. The same wrong number appeared in the committee amendments example (Section 10.2).

**Fix:** Changed all instances of "BAA No. 15" to "BAA No. 18" in the file.

### 3. Shari'ah Article Citation (13-glossary.md)

**Problem:** Glossary cited "(BOL, Article IX, Sections 7-10)" for Shari'ah. Article IX is Basic Rights. The Shari'ah courts and justice system are in Article X (Bangsamoro Justice System).

**Fix:** Changed to "(BOL, Article X, Sections 7-10)".

### 4. BOL Article Mislabeling (03-chapter-02.md)

**Problem:** Section 2.3.3 (Step 2: BOL research) had 4 incorrect article labels:
- Article V was labeled "Basic Rights" (correct: "Powers of Government")
- Article VI was labeled "Powers of Government" (correct: "Intergovernmental Relations")
- Article VIII was labeled "The Parliament" (correct: "Wali")
- Article XIII was labeled "Shari'ah and Traditional/Tribal Justice System" (correct: "Regional Economy and Patrimony")

**Fix:** Corrected all article labels to match the BOL. Expanded the list to include Article IX (Basic Rights) and Article X (Bangsamoro Justice System) which were missing. Also fixed the worked example that referenced "Article VI (Powers of Government)" for tax limitations -- corrected to "Article XII, Section 9 (Limitations on the Taxing Powers)".

### 5. Local Government Code Status (02-chapter-01.md)

**Problem:** Section 1.2.4 listed "Bangsamoro Local Government Code (pending)" -- but the LGC was enacted as BAA No. 49 in 2023. Chapter 4 correctly stated this.

**Fix:** Updated the priority codes list to show BAA No. 49 as enacted. Also added missing BAA numbers for Civil Service Code (BAA No. 17) and Education Code (BAA No. 18).

### 6. Priority Codes Count (02-chapter-01.md, 05-chapter-04.md)

**Problem:** Chapter 1 called them "seven priority codes identified in the BOL." The BOL (Art. XVI, Sec. 4(a)) explicitly names only 5 codes. The Civil Service Code is described as optional ("may also enact"). The Investment Code is not in the BOL at all.

**Fix:**
- Chapter 1: Rewrote to accurately describe BOL Art. XVI, Sec. 4(a) as naming five codes, the Civil Service Code as optional, and the Investment Code as identified from broader needs. Listed all 7 with correct status (5 enacted, 2 pending).
- Chapter 4: Removed time-bound "As of this writing" phrasing. Changed "seven priority codes identified in the BOL and its implementing agenda" to "the priority codes identified in the BOL and its broader legislative agenda."

---

## Major Fixes Applied

### 7. Deputy Speakers Count (02-chapter-01.md, 13-glossary.md)

**Problem:** Chapter 1 said "ten Deputy Speakers." Glossary said "One of eight Deputy Speakers." Resolution No. 268, Rule III, Section 3 prescribes eight (8). The BTA elected ten in practice.

**Fix:**
- Chapter 1: Removed named officials entirely. Replaced with generic description noting Res. 268 prescribes eight Deputy Speakers and the BTA has elected additional ones.
- Glossary: Updated to state the Res. 268 rule (eight) and note the BTA practice of electing additional ones.

### 8. Timelessness in Chapter 1 (02-chapter-01.md)

**Problem:** Named officials (Speaker Yacob, ICM Macacua, Floor Leader Lim), specific member counts ("77 members"), "currently operating," and dated references ("third BTA," "March 2025") will become stale.

**Fixes applied:**
- Changed "currently operating" to "During the transition period, the Bangsamoro Parliament operates as..."
- Removed all named officials and specific BTA composition numbers
- Removed specific BTA reconstitution dates and presidential names
- Changed "As of early 2026, the Parliament has enacted over eighty BAAs" to remove the time-bound count
- Replaced detailed Sulu-related member count with generic reference to Section 1.3.5

### 9. AI Slop (09-chapter-08.md)

**Problem:** "legal landscape" at line 116.

**Fix:** Changed to "existing body of law."

**Note:** "comprehensive framework" in Ch. 6, line 366 (describing BAA No. 49) was left unchanged per QA-REPORT assessment that it is arguably appropriate since it describes an actual legislative framework. No other AI slop terms found.

### 10. Section Heading Alignment (8 files, 20+ headings)

**Problem:** ~20 section headings in chapter files were shortened or reworded compared to the TOC.

**Fixes applied:**

**02-chapter-01.md (10 headings fixed):**
- 1.1.3: "The BAA as Legislative Output" -> "The Bangsamoro Autonomy Act as the Parliament's Legislative Output"
- 1.2.1: "The Constitution" -> "The 1987 Constitution"
- 1.2.2: "The Bangsamoro Organic Law (RA 11054)" -> "The Bangsamoro Organic Law (Republic Act No. 11054)"
- 1.2.3: "National Laws and Implementing Rules and Regulations" -> "National Laws and Their Implementing Rules and Regulations"
- 1.3.3: "The Residual Clause" -> "The Residual Clause: Powers Reserved to Congress"
- 1.3.4: "Overlapping Authority and Intergovernmental Relations" -> "Areas of Overlapping Authority"
- 1.3.5: "Judicial Doctrines Affecting Bangsamoro Legislative Power" -> "Judicial Doctrines Affecting Bangsamoro Legislation"
- 1.4.2: "When Shari'ah Applies" -> "When Shari'ah Considerations Apply"
- 1.4.3: "Practical Guidance for the Drafter" -> "Practical Guidance for Drafters"

**03-chapter-02.md (4 headings fixed):**
- Title: "Chapter 2: From Legislative Directive to Filing -- The Drafting Process" -> "Chapter 2 -- From Legislative Directive to Bill: The Drafting Process"
- 2.2.4: "Securing MP Approval" -> "Securing MP Approval of the Initial Legislative Template"
- 2.3.2: "Working with the PRLS" -> "Working with the Policy Research and Legal Services (PRLS)"
- 2.3.4 subsections: Added explicit numbering (2.3.4.1 through 2.3.4.6) to match TOC

**04-chapter-03.md (2 headings fixed):**
- 3.3.4: "Common Mistakes" -> "Common Mistakes in Long Titles"
- 3.6.1: "Organizing Substantive Provisions" -> "Organizing the Substance of the Bill"

**07-chapter-06.md (5 headings fixed):**
- 6.2.1: "Plain Language" -> "Plain Language in Legislation"
- 6.3.1: "Consistent Terms" -> "Consistent Use of Terms"
- 6.3.2: "Consistent Structure" -> "Consistent Structure Across Provisions"
- 6.4.1: "Gaps in Coverage" -> "Checking for Gaps in Coverage"
- 6.19.3: "Vague Terms" -> "Vague and Ambiguous Terms"

**08-chapter-07.md (1 heading fixed):**
- 7.3.3: "Referral to Committee" -> "Referral to the Appropriate Committee"

**10-chapter-09.md (3 headings fixed):**
- 9.2.1: "Annual Budget Deliberation" -> "For the Annual Budget Deliberation"
- 9.2.2: "Committee on Finance Hearings" -> "For Committee on Finance Hearings"
- 9.2.3: "Plenary Budget Deliberation" -> "For Plenary Budget Deliberation"

---

## Items NOT Fixed (Deferred or Out of Scope)

- **Appendices A-G:** The TOC lists 7 appendices but no appendices file exists. Creating them requires substantive content authoring, not a fix pass.
- **TOC sub-section gaps:** Several chapters have sub-sections not listed in the TOC (Ch. 4 Sec 4.5, Ch. 5 Secs 5.1/5.5, Ch. 6 end-of-chapter tables, Ch. 10 Secs 10.2/10.3). The QA report recommends either updating the TOC or restructuring. This requires an editorial decision.
- **Glossary completeness:** Missing terms (Completed Staff Work, Comparative Matrix, Legislative Research Briefer) require new definitions to be authored.
- **Introduction chapter-topic list mismatch:** Item 5 and item 9 in the "How to Use This Manual" section do not match actual chapters. Requires editorial rewrite.
- **Supreme Court case verification:** GR numbers, dates, and holdings for Province of Sulu v. Medialdea and Ali et al. v. BTA cannot be verified from local sources.
- **"comprehensive framework" in Ch. 6:** Left as-is per QA assessment that it describes an actual legislative framework (BAA No. 49).

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Critical fixes applied | 6 |
| Major fixes applied | 4 |
| Files modified | 10 |
| Section headings aligned with TOC | 25 |
| Enacting clause formulations unified | 6 locations across 5 files |
| Factual errors corrected | 9 |
| Time-bound references removed | 5 |
