# QA Report: Complete Staff Work Guidebook

**Date:** 2026-03-26
**Files reviewed:** 20 content .md files (00-table-of-contents through 15-glossary)
**Reference author bio:** docs/bill-drafting-manual/ver02/00c-author.md

---

## Summary Table

| # | Category | Severity | Count | Status |
|---|----------|----------|-------|--------|
| 1 | Voice compliance (prohibited phrases) | -- | 0 | PASS |
| 2 | Sentence length (>30 words) | MINOR | 1 | 1 instance found |
| 3 | Chapter openings (WHY-first) | -- | 0 | PASS |
| 4 | Cross-references | -- | 0 | PASS |
| 5 | Consistency (term usage) | -- | 0 | PASS |
| 6 | Completeness (placeholders) | -- | 0 | PASS |
| 7 | Heading hierarchy | -- | 0 | PASS |
| 8 | Author bio match | -- | 0 | PASS |

**Overall: 0 CRITICAL, 1 MINOR**

---

## 1. Voice Compliance

All 14 prohibited phrases were searched (case-insensitive) across all 20 files:

- "It is important to note that" -- NOT FOUND in prose
- "In order to" -- NOT FOUND in prose
- "It should be noted" -- NOT FOUND in prose
- "With regard to" -- NOT FOUND in prose
- "In the context of" -- NOT FOUND in prose
- "It is worth mentioning" -- NOT FOUND
- "As previously mentioned" -- NOT FOUND in prose
- "For the purposes of" -- NOT FOUND in prose
- "In light of the foregoing" -- NOT FOUND in prose
- "The aforementioned" -- NOT FOUND in prose
- "It is recommended that" -- NOT FOUND in prose
- "Pursuant to the provisions of" -- NOT FOUND in prose
- "Notwithstanding the foregoing" -- NOT FOUND in prose
- "In furtherance of" -- NOT FOUND

Note: All matches found are in 14-chapter-13.md, lines 33-44, inside a "Phrases to Avoid" reference table. These are intentional examples of what NOT to write. No violations in actual prose.

**Result: PASS**

---

## 2. Sentence Length

Spot-checked 3 chapters: 06-chapter-05.md, 09-chapter-08.md, 12-chapter-11.md.

| File | Line | Word Count | Text (truncated) |
|------|------|------------|------------------|
| 06-chapter-05.md | 171 | 40 words | "Island municipalities in BARMM have 1 physician per 47,000 population versus the DOH standard of 1..." |

- 09-chapter-08.md: 0 long sentences found
- 12-chapter-11.md: 0 long sentences found

### Fix instruction
**06-chapter-05.md, line 171:** Split the 40-word example sentence into two sentences. Break after the comparison data point, then state the implication separately.

**Result: 1 MINOR issue**

---

## 3. Chapter Openings

Every chapter opens with WHY this matters to the reader, not with history or definitions.

| File | Opening Approach | Status |
|------|-----------------|--------|
| 01-introduction.md | "Your decision-maker just assigned you a task..." -- Practical scenario | PASS |
| 02-chapter-01.md | "Every time you submit incomplete work..." -- Stakes/consequence | PASS |
| 03-chapter-02.md | "Your CSW output does not exist in a vacuum..." -- Relevance | PASS |
| 04-chapter-03.md | "Your first decision when you receive an assignment is..." -- Action | PASS |
| 05-chapter-04.md | "You received an assignment. Before you open a blank document, stop." -- Action | PASS |
| 06-chapter-05.md | "A vague problem produces a vague solution." -- Consequence | PASS |
| 07-chapter-06.md | "Your problem is defined. Your objectives are set. Now you need evidence." -- Transition | PASS |
| 08-chapter-07.md | "You defined the problem. You gathered evidence. Now you must generate solutions..." -- Transition | PASS |
| 09-chapter-08.md | "Your analysis is complete... Now you must package everything..." -- Action | PASS |
| 10-chapter-09.md | "The decision-maker approved your recommendation. The hard part is over, right? Wrong." -- Challenge | PASS |
| 11-chapter-10.md | "The CSW process does not end with implementation..." -- Stakes | PASS |
| 12-chapter-11.md | "If you work in the Bangsamoro Parliament, your CSW directly shapes legislation." -- Relevance | PASS |
| 13-chapter-12.md | "If you work in a Ministry, Office, or Agency..." -- Relevance | PASS |
| 14-chapter-13.md | "Your analysis can be brilliant... But if the writing is unclear..." -- Stakes | PASS |
| 15-chapter-14.md | "A single training session does not create a CSW culture." -- Challenge | PASS |

**Result: PASS**

---

## 4. Cross-References

All chapter cross-references verified:

| Source File | Reference | Target | Correct? |
|-------------|-----------|--------|----------|
| 01-introduction.md | "Chapter 1" through "Chapter 14" | All match actual chapter numbers | YES |
| 02-chapter-01.md:146 | "Chapter 2 shows how CSW operates..." | Chapter 2 = CSW in Bangsamoro Context | YES |
| 03-chapter-02.md:54 | "transmittal memorandum (see Chapter 8)" | Chapter 8 = Submit Proposal or Report | YES |
| 03-chapter-02.md:180 | "Chapter 3 introduces the nine types..." | Chapter 3 = Types of CSW | YES |
| 04-chapter-03.md:49 | "Chapter 11 provides detailed guidance on...Legislative Analysis Briefers" | Chapter 11 = CSW for Parliamentary Committees | YES |
| 04-chapter-03.md:282 | "Chapter 4 begins the ADDRESS IT process" | Chapter 4 = Analyze the Context | YES |
| 05-chapter-04.md:22 | "Chapter 3" for CSW type | Chapter 3 = Types of CSW | YES |
| 05-chapter-04.md:236 | "Chapter 5...Define and Deliberate" | Chapter 5 = Step 2 | YES |
| 06-chapter-05.md:186 | "Chapter 6...Research Needed Information" | Chapter 6 = Step 3 | YES |
| 07-chapter-06.md:235 | "Chapter 7...Explore Options" | Chapter 7 = Step 4 | YES |
| 08-chapter-07.md:244 | "Chapter 8...Submit Proposal or Report" | Chapter 8 = Step 5 | YES |
| 09-chapter-08.md:9 | "Chapter 3" for CSW type | Chapter 3 = Types of CSW | YES |
| 09-chapter-08.md:254 | "Chapter 9...Sustain Efforts" | Chapter 9 = Step 6 | YES |
| 10-chapter-09.md:180 | "Chapter 10...Iterate and Improve" | Chapter 10 = Step 7 | YES |
| 11-chapter-10.md:217 | "Chapter 11...Parliamentary committee work" | Chapter 11 = Parliamentary Committees | YES |
| 12-chapter-11.md:156 | "Chapter 12...MOA decision-making" | Chapter 12 = MOA Decision-Making | YES |
| 13-chapter-12.md:134 | "Chapter 8, Section 8.11" for transmittal memo | Section 8.11 = The Transmittal Memorandum | YES |
| 13-chapter-12.md:190 | "Chapter 13...writing standards" | Chapter 13 = Writing Standards | YES |
| 14-chapter-13.md:176 | "Chapter 8, Section 8.11" | Section 8.11 = The Transmittal Memorandum | YES |
| 14-chapter-13.md:218 | "Chapter 14...CSW culture" | Chapter 14 = Building a CSW Culture | YES |

**Result: PASS**

---

## 5. Consistency

### Term: "ADDRESS IT"
All 60+ occurrences across all files use **ADDRESS IT** (all caps). No instances of "Address It", "address it", or "ADDRESS it" found.

### Term: "ACSCCRaPATFEE"
All occurrences use **ACSCCRaPATFEE** consistently. No case variants found.

### Term: "CSW" / "Complete Staff Work"
Used consistently. "CSW" always refers to the same concept with no inconsistent expansions.

**Result: PASS**

---

## 6. Completeness

Searched for: `[TBD]`, `[INSERT]`, `[TODO]`, `[PLACEHOLDER]` (case-insensitive).

**No matches found.** All sections are fully written.

**Result: PASS**

---

## 7. Heading Hierarchy

All 20 files checked:

- Every content file has exactly one H1 (chapter title)
- Sections use H2 (e.g., `## 1.1 What CSW Means in Practice`)
- Subsections use H3 (e.g., `### 1.1.1 The Decision-Maker Should Only Need to Approve`)
- No H4 headers found
- No duplicate H1 headers found
- Front matter files (00-table-of-contents, 00b-about, 00c-author) each have one H1

**Result: PASS**

---

## 8. Author Bio

`00c-author.md` compared character-by-character against the reference at `docs/bill-drafting-manual/ver02/00c-author.md`.

**Identical.** Same heading, same paragraphs, same content.

**Result: PASS**

---

## Action Items

| Priority | File | Line | Action |
|----------|------|------|--------|
| MINOR | 06-chapter-05.md | 171 | Split the 40-word sentence into two shorter sentences (target: under 30 words each) |

**No CRITICAL issues found. This guidebook is ready for production.**
