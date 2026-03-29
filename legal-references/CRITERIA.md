# Criteria for a Well-Written Legal Reference

Quality standards for evaluating each BOL power's legal reference entry. Every entry must meet **all mandatory criteria** and aim for the quality indicators.

---

## Mandatory Criteria (Pass/Fail)

Each entry MUST satisfy all of these. A single failure means the entry needs revision.

### 1. Verbatim Accuracy
- [ ] BOL power text is copied verbatim from the local BOL transcription (not paraphrased)
- [ ] All quoted provisions use exact text from source files
- [ ] Article, section, and subsection numbers are correct and verified against local files
- [ ] BAA numbers and titles match the BAA index (`legislation/baas/INDEX.md`)

### 2. Source Verification
- [ ] Every BAA cited exists in `legislation/baas/BAA-{N}.md`
- [ ] Every bill cited exists in `legislation/bills/enacted/`
- [ ] Every resolution cited exists in `legislation/resolutions/enacted/`
- [ ] Every national law cited exists in `legislation/national-laws/` or can be verified
- [ ] BOL provisions are verified against `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/`
- [ ] No fabricated BAA numbers, bill numbers, or provision citations

### 3. Completeness
- [ ] Power classification table is fully populated (type, lead ministry, BDP chapter)
- [ ] All related BOL provisions beyond Art. V Sec. 2 are identified (scan all 18 articles)
- [ ] BAA search covers all 89+ enacted BAAs (not just obvious ones)
- [ ] Legislative gaps section is present (even if "No gaps identified" with explanation)
- [ ] Footnotes use Feliciano 10th Edition format

### 4. No Prohibited Content
- [ ] No draft legislation cited as enacted law
- [ ] No guidebooks cited as primary sources for legal claims
- [ ] No fabricated or hallucinated legislation references
- [ ] No paraphrased text presented as verbatim quotes
- [ ] No commentary or policy recommendations (this is reference, not analysis)

---

## Quality Indicators (Scoring Rubric)

Rate each entry 1-5 on these dimensions. Target: average 4+ across all dimensions.

### A. Breadth of Coverage (1-5)

| Score | Description |
|-------|-------------|
| 1 | Only lists the BOL provision itself; no implementing legislation found |
| 2 | Lists 1-2 obvious BAAs; misses related provisions in other BOL articles |
| 3 | Covers BAAs and some bills; identifies main BOL cross-references |
| 4 | Comprehensive BAA/bill/resolution coverage; thorough BOL cross-references; some national laws |
| 5 | Exhaustive: every tier of the 7-tier hierarchy represented where applicable; national laws mapped; EOs included; BDP fully aligned |

### B. National Law Relationship (1-5)

| Score | Description |
|-------|-------------|
| 1 | No indication of whether national law consistency is required |
| 2 | States "no national law requirement" without citing BOL provisions |
| 3 | Correctly identifies whether BOL requires national law consistency; lead ministry identified |
| 4 | Cites specific BOL provision requiring (or not requiring) national law consistency; identifies intergovernmental coordination bodies if any; supporting agencies identified |
| 5 | Complete BOL-grounded analysis: specific provisions cited, intergovernmental bodies noted, suppletory national law identified where no BAA exists, Art. VI coordination mechanisms documented |

### C. Cross-Reference Depth (1-5)

| Score | Description |
|-------|-------------|
| 1 | No cross-references to other BOL articles |
| 2 | 1-2 obvious cross-references (e.g., fiscal provisions for budget power) |
| 3 | Cross-references to 3+ BOL articles with brief explanations |
| 4 | Systematic scan of all relevant BOL articles; each cross-reference explains the relationship type |
| 5 | Comprehensive with relationship taxonomy (defines scope, sets limits, creates body, grants fiscal authority, establishes rights, mandates consultation) |

### D. Gap Analysis Quality (1-5)

| Score | Description |
|-------|-------------|
| 1 | No gap analysis |
| 2 | States "no standalone BAA" without identifying which ministry exercises the power through BAA 13 |
| 3 | Identifies Type A gaps (no standalone legislation) and names the BAA 13 ministry that exercises the power |
| 4 | Identifies Type A + B gaps; specifies what a standalone BAA would codify vs. what BAA 13 already covers |
| 5 | All three gap types analyzed (A: no standalone legislation, B: partial implementation, C: national law interaction); recommended actions are specific; BAA 13 coverage acknowledged for all Type A gaps |

### E. Citation Quality (1-5)

| Score | Description |
|-------|-------------|
| 1 | No footnotes; informal references |
| 2 | Some footnotes but inconsistent format |
| 3 | Feliciano format used; most provisions cited |
| 4 | All provisions have footnotes; consistent Feliciano format; cross-references between sections |
| 5 | Publication-grade: every claim footnoted, subsequent references use *Id.*, pinpoint citations (article + section + subsection), amendment history noted |

### F. Practical Utility (1-5)

| Score | Description |
|-------|-------------|
| 1 | Raw data dump; not organized for quick reference |
| 2 | Organized but missing context for non-specialists |
| 3 | Usable by legal officers; clear table structure |
| 4 | Usable by planning officers AND legal officers; relationship descriptions are actionable |
| 5 | A parliamentary staff member can use this entry alone to: (a) identify all legislation touching this power, (b) determine which ministry leads, (c) find gaps for new legislation, (d) verify compliance with national law |

### G. Legal Briefer Quality (1-5)

| Score | Description |
|-------|-------------|
| 1 | No Legal Briefer section |
| 2 | Q&A exists but answers are generic, don't quote the law, or miss major themes |
| 3 | All 5 themes (A-E) present with Q&A pairs; most answers cite specific provisions; 800-1,000 words |
| 4 | Bar reviewer quality: every answer quotes or closely tracks the language of the law; a reader can look up any specific question and find a direct answer with inline citations; all ~17 Q&A pairs present; 1,000-1,500 words |
| 5 | Publication-grade Bernas/Golden Notes quality: answers are near-verbatim statutory language with case citations where available; legislative gap answers name specific proposed laws with coverage details; a law student or parliamentary researcher can use this as a study reviewer for this power area; 1,500-2,000 words |

---

## Verification Checklist (Post-Production)

Run after each entry is written. This is the DETECT layer of the Universal Verification Framework.

### Automated Checks
- [ ] Run `verify-references.py` on the entry to cross-check all BAA numbers
- [ ] Grep each cited BAA number against `legislation/baas/` to confirm file exists
- [ ] Grep each cited bill number against `legislation/bills/enacted/` to confirm file exists
- [ ] Verify BOL article/section numbers against the BOL index

### Manual Review
- [ ] Read the entry as if you are a parliamentary researcher looking up this power for the first time
- [ ] Confirm the national law relationship is correctly identified using BOL provisions
- [ ] Check that no BAA is listed under the wrong power (some BAAs touch multiple powers — ensure the primary mapping is correct)
- [ ] Verify gap analysis is accurate — a power flagged as "no implementing BAA" genuinely has none

### Cross-Entry Consistency
- [ ] BAAs listed under multiple powers are consistently described
- [ ] Ministry assignments don't conflict across related powers
- [ ] National law relationship determinations are consistent across related powers (e.g., if Education has no national law consistency requirement, Skills Training should be the same unless a specific BOL provision says otherwise)

---

## Anti-Patterns (What to Avoid)

| Anti-Pattern | Why It's Wrong | Correct Approach |
|-------------|----------------|------------------|
| Fabricating BAA numbers | Known hallucination pattern; BAA numbers are sequential and finite | Verify every BAA number against the index file |
| Citing "BAA 25 = Environment Code" | Known fabrication (BAA 25 is actually about something else) | Read the actual BAA file to confirm the title |
| Paraphrasing BOL text as "verbatim" | Creates authority for words the law didn't use | Copy-paste from transcription files |
| Listing proposed bills as enacted | Misleads about the current legal landscape | Only cite enacted legislation; note pending bills separately if at all |
| Generic gap analysis | "More legislation is needed" adds no value | Specify WHAT legislation is needed and WHY |
| Ministry assignment by assumption | Guessing which ministry handles what | Derive from BAA 13 mandate assignments and BAA 85 organizational structure |
| Missing national law interaction | Ignoring how national law relates to this power | Every power must address whether BOL requires national law consistency, and identify suppletory national laws where no BAA exists |
| Using "Exclusive/Shared/Concurrent" | These are doctrinal/academic terms NOT used in the BOL | Use only BOL language: "enumerated power" (Art. V Sec. 2), "national law consistency required" (cite specific BOL provision), "intergovernmental coordination" (Art. VI), "expressly granted / necessarily implied / necessary, appropriate, or incidental" (Art. V Sec. 3) |
| Citing guidebooks as authority | Guidebooks are NOT authoritative sources; they may contain errors | Trace every factual claim back to enacted law (BOL, BAA, RA, Constitution) |
