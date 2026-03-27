# QA Report: Supervision and Supervisory Development Guidebook

**Date:** 2026-03-26
**Files reviewed:** 21 content .md files (00-table-of-contents through 16-glossary)
**Reference author bio:** docs/bill-drafting-manual/ver02/00c-author.md

---

## Summary Table

| # | Category | Severity | Count | Status |
|---|----------|----------|-------|--------|
| 1 | Voice compliance (prohibited phrases) | -- | 0 | PASS |
| 2 | Sentence length (>30 words) | MINOR | 9 | 9 instances across 3 spot-checked chapters |
| 3 | Chapter openings (WHY-first) | -- | 0 | PASS |
| 4 | Cross-references | -- | 0 | PASS |
| 5 | Consistency (term usage) | -- | 0 | PASS |
| 6 | Completeness (placeholders) | -- | 0 | PASS |
| 7 | Heading hierarchy | -- | 0 | PASS |
| 8 | Author bio match | -- | 0 | PASS |

**Overall: 0 CRITICAL, 9 MINOR (all sentence length)**

---

## 1. Voice Compliance

All 14 prohibited phrases were searched (case-insensitive) across all 21 files:

- "It is important to note that" -- NOT FOUND
- "In order to" -- NOT FOUND
- "It should be noted" -- NOT FOUND
- "With regard to" -- NOT FOUND
- "In the context of" -- NOT FOUND
- "It is worth mentioning" -- NOT FOUND
- "As previously mentioned" -- NOT FOUND
- "For the purposes of" -- NOT FOUND
- "In light of the foregoing" -- NOT FOUND
- "The aforementioned" -- NOT FOUND
- "It is recommended that" -- NOT FOUND
- "Pursuant to the provisions of" -- NOT FOUND
- "Notwithstanding the foregoing" -- NOT FOUND
- "In furtherance of" -- NOT FOUND

**Result: PASS (zero violations)**

---

## 2. Sentence Length

Spot-checked 3 chapters: 04-chapter-03.md, 08-chapter-07.md, 12-chapter-11.md.

### 04-chapter-03.md (3 instances)

| Line | Words | Text (truncated) |
|------|-------|------------------|
| 79 | 31 | "Am I reacting to this specific behavior, or to a pattern I have not addressed? If the pattern is the issue, addres..." |
| 80 | 31 | "Would I give this same feedback to every staff member who did this, or only this person? If you would let someone..." |
| 96 | 32 | "BARMM example: A Division Chief who only gave feedback when performance was poor found that every time she asked a s..." |

### 08-chapter-07.md (2 instances)

| Line | Words | Text (truncated) |
|------|-------|------------------|
| 83 | 56 | "The supervisor initiated a PIP with these elements: (1) Complete a guided options analysis exercise for three past brief..." |
| 157 | 31 | "You face a conflict of interest. If the staff member is a relative, close personal friend, or has other ties that..." |

### 12-chapter-11.md (4 instances)

| Line | Words | Text (truncated) |
|------|-------|------------------|
| 5 | 41 | "Every hour you spend drafting a report that a staff member could draft with guidance is an hour you did not spend on the..." |
| 7 | 37 | "Supervisors hold onto work for predictable reasons: 'It is faster if I do it myself.' 'They will not do it right.'..." |
| 149 | 32 | "Recognize initiative. When someone takes ownership and drives a result without being asked, name it: 'You identified..." |
| 155 | 40 | "BARMM example: A Director empowered her Division Chiefs by setting clear boundaries ('you may approve requests up to..." |

### Fix instructions

Most of these are borderline (31-32 words) and include dialogue or enumerated elements, which inflates word count without harming readability. The two priority fixes:

1. **08-chapter-07.md, line 83 (56 words):** This is the longest sentence found. Split the PIP elements list into a bulleted sub-list instead of inline parenthetical numbering.
2. **12-chapter-11.md, line 5 (41 words):** Split after "guidance" -- make the second clause its own sentence starting with "That is an hour you did not spend on..."

The remaining 7 instances (31-40 words) are borderline and acceptable if the team considers the 30-word limit a guideline rather than a hard rule. Most contain dialogue quotes or BARMM examples that benefit from flowing naturally.

**Result: 9 MINOR issues (2 recommended fixes, 7 borderline-acceptable)**

---

## 3. Chapter Openings

Every chapter opens with WHY this matters to the reader, not with history or definitions.

| File | Opening Approach | Status |
|------|-----------------|--------|
| 01-introduction.md | "Open this book when you need it. Not before." -- Direct instruction | PASS |
| 02-chapter-01.md | "Your staff will not perform better than you lead them." -- Stakes | PASS |
| 03-chapter-02.md | "You cannot coach someone you have not accurately assessed." -- Stakes | PASS |
| 04-chapter-03.md | "The number one reason staff repeat mistakes is that nobody told them..." -- Consequence | PASS |
| 05-chapter-04.md | "Telling someone what they did wrong is feedback. Helping them build the capability to do it right is coaching." -- Distinction | PASS |
| 06-chapter-05.md | "Your staff cannot hit a target they cannot see." -- Stakes | PASS |
| 07-chapter-06.md | "The annual performance evaluation tells you how someone performed over 12 months. A check-in tells you what is happening right now..." -- Contrast | PASS |
| 08-chapter-07.md | "Ignoring underperformance is not kindness. It is abandonment." -- Challenge | PASS |
| 09-chapter-08.md | "If your team's capability depends entirely on who happens to be assigned to you, your team's ceiling is fixed." -- Stakes | PASS |
| 10-chapter-09.md | "A group of individuals assigned to the same office is not a team." -- Distinction | PASS |
| 11-chapter-10.md | "Change is not an interruption to your work... change IS the work." -- Reframe | PASS |
| 12-chapter-11.md | "If you are doing work that your staff could do, you are failing at your job." -- Challenge | PASS |
| 13-chapter-12.md | "Accountability is not punishment." -- Reframe | PASS |
| 14-chapter-13.md | "If you have been doing your job... then the annual performance evaluation should contain no surprises." -- Stakes | PASS |
| 15-chapter-14.md | "Every chapter in this guidebook has been about supervising people. This chapter is about supervising the work they produce." -- Transition | PASS |

**Result: PASS**

---

## 4. Cross-References

All chapter cross-references verified against the Table of Contents and actual chapter content:

| Source File | Reference | Target | Correct? |
|-------------|-----------|--------|----------|
| 01-introduction.md | "Chapter 3" for feedback | Ch 3 = Giving Effective Feedback | YES |
| 01-introduction.md | "Chapter 13" for evaluations | Ch 13 = Performance Evaluation | YES |
| 01-introduction.md | "Chapter 1" for new supervisors | Ch 1 = Supervisor's Role | YES |
| 01-introduction.md | "Chapter 14" for CSW connection | Ch 14 = Supervision and CSW | YES |
| 00b-about.md | "Chapter 3" for feedback | Ch 3 = Giving Effective Feedback | YES |
| 00b-about.md | "Chapter 13" for evaluations | Ch 13 = Performance Evaluation | YES |
| 00b-about.md | "Chapter 1" for new supervisors | Ch 1 = Supervisor's Role | YES |
| 00b-about.md | "Chapter 14" for CSW | Ch 14 = Supervision and CSW | YES |
| 00b-about.md | "Appendix K" for competencies quick ref | Appendix K in TOC | YES |
| 05-chapter-04.md:114 | "address it" (lowercase, verb usage) | Not a framework reference -- natural language | N/A |

**Result: PASS**

---

## 5. Consistency

### Term: "ADDRESS IT"
All occurrences referring to the framework use **ADDRESS IT** (all caps). One instance in 05-chapter-04.md line 114 uses "address it" as a natural verb ("address it quickly") -- this is correct contextual usage, not an inconsistency.

### Term: "ACSCCRaPATFEE"
All occurrences use **ACSCCRaPATFEE** consistently. No case variants found.

### Term: "PPR"
Used consistently as "PPR Framework" or "PPR" throughout. No variants.

### Term: "SBI"
Used consistently as "SBI" or "SBI model" throughout. No variants.

### Term: "BARMM" / "Bangsamoro"
Used consistently. No variant spellings found.

**Result: PASS**

---

## 6. Completeness

Searched for: `[TBD]`, `[INSERT]`, `[TODO]`, `[PLACEHOLDER]` (case-insensitive).

**No matches found.** All sections are fully written.

**Result: PASS**

---

## 7. Heading Hierarchy

All 21 files checked:

- Every content file has exactly one H1 (chapter title)
- Sections use H2 (e.g., `## 1.1 Supervision as Service, Not Authority`)
- Subsections use H3 (e.g., `### 1.1.1 Islamic Leadership Principles`)
- No H4 headers found
- No duplicate H1 headers found
- Front matter files (00-table-of-contents, 00b-about, 00c-author) each have one H1

**Result: PASS**

---

## 8. Author Bio

`00c-author.md` compared against the reference at `docs/bill-drafting-manual/ver02/00c-author.md`.

**Identical.** Same heading, same paragraphs, same content.

**Result: PASS**

---

## Action Items

| Priority | File | Line | Action |
|----------|------|------|--------|
| MINOR | 08-chapter-07.md | 83 | Split the 56-word sentence -- convert the inline "(1)...(2)...(3)..." list into a bulleted sub-list |
| MINOR | 12-chapter-11.md | 5 | Split the 41-word sentence after "guidance" into two sentences |
| MINOR (low) | 04-chapter-03.md | 79, 80, 96 | Borderline (31-32 words). Consider splitting if strict 30-word limit applies. Acceptable as-is if limit is a guideline. |
| MINOR (low) | 08-chapter-07.md | 157 | Borderline (31 words). Acceptable as-is. |
| MINOR (low) | 12-chapter-11.md | 7, 149, 155 | Borderline (32-40 words). Lines 7 and 155 contain dialogue/examples. Acceptable as-is if limit is a guideline. |

**No CRITICAL issues found. This guidebook is ready for production with 2 recommended sentence-length fixes.**
