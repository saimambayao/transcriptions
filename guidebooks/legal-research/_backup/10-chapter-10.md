# Chapter 10 — Quality, Verification, and Continuous Learning

A research memorandum with one wrong article number damages the credibility of every other citation in the document. A legal opinion that quotes a repealed provision leads the decision-maker to act on authority that no longer exists. A legislative briefer that misattributes a mandate to the wrong institution sends a bill in the wrong direction.

Quality in legal research is not a final polish. It is a discipline that runs through every step. This chapter collects the verification practices scattered throughout this guidebook into a single reference, adds the patterns of error you are most likely to encounter, and establishes the habits that keep your research current over time.

---

## 10.1 Purpose

Verification is Step 5 of the five-step methodology. But verification is not only a step — it is a mindset. Every citation you record, every provision you quote, every conclusion you draw is a claim about what the law says. Each claim is either right or wrong. The purpose of this chapter is to make sure yours are right.

---

## 10.2 Confirming Good Law

"Good law" means a provision that is currently in force, has not been repealed or amended, and has not been declared unconstitutional. Confirming good law requires three checks:

**Check 1: Has it been repealed?** Search for later legislation that expressly repeals the provision. BAAs commonly include repealing clauses — Section 17 of many BAAs states "All other regional laws, rules, and regulations or parts thereof inconsistent with this Act are hereby repealed, amended or modified accordingly." If a later BAA covers the same subject, check whether it supersedes the earlier provision.

**Check 2: Has it been amended?** Some BAAs amend specific provisions of earlier BAAs. Example: BAA 70 amends BAA 54 (municipality boundary), and BAA 71 amends BAA 55. BAA 87 and BAA 88 both amend BAA 35 (Electoral Code). When you cite a provision, verify that the version you are citing is current — not the original text that has since been modified.

**Check 3: Has it been declared unconstitutional?** Supreme Court decisions can invalidate BAAs or specific provisions. BAA 58 and BAA 77 were both struck down (October 2025). If a provision you cite has been the subject of judicial review, check the outcome. A provision declared unconstitutional is no longer good law — even if it has not been formally repealed by Parliament.[^1]

---

## 10.3 Verbatim Accuracy

The single most important quality practice: **copy provisions from the source text, do not paraphrase from memory.**

Why this matters:
- "Shall ensure the protection" is not "shall take into consideration"
- "Bangsamoro Government" is not "regional government"
- "Article XII, Sections 15-16" is not "Article XII, Section 9"
- "Arresto menor" is not "minor imprisonment"

Each of these substitutions changes the legal meaning. Paraphrasing is the mechanism through which research errors enter the system and propagate through downstream outputs.

**The verbatim discipline:**
1. Open the source file containing the provision
2. Locate the exact section
3. Copy the text directly — do not retype
4. Paste into your Research Memorandum with a blockquote marker
5. Record the source path (file, page, line number)
6. Verify the article, section, and subsection numbers match the source

If you are working from a physical document (printed BAA, PDF printout), type the text character by character from the source — then re-read both the source and your transcription to catch any discrepancies.

---

## 10.4 Source Hierarchy for Verification

Not all sources are equally reliable. Verify provisions in this order:

| Priority | Source | Reliability | Speed |
|----------|--------|------------|-------|
| 1 | **Local markdown transcriptions** | Verbatim-accurate, verified against PDFs | Fastest — searchable, local |
| 2 | **Original PDF source documents** | Authoritative originals | Slower — requires PDF reading |
| 3 | **Official Gazette** | Official publication of record | Medium — requires web access |
| 4 | **LawPhil / Chan Robles** | Secondary compilations | Medium — verify against official copy |
| 5 | **Web search results** | Variable reliability | Slowest — always cross-check |

**Rule:** Never cite a provision you have not verified against a Priority 1 or Priority 2 source. If you find a provision through web search (Priority 5), verify it against the local transcription or official PDF before citing it.

**Local source paths (BARMM):**
- BOL: `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` (5 chapter files)
- BAAs: `~/Vault/bangsamoro/bangsamoro-laws/BAA-{N}.md` (89 files)
- BAA index: `~/Vault/bangsamoro/bangsamoro-laws/index.md`
- Resolutions: `~/Vault/bangsamoro/bangsamoro-resolutions/resolution{N}.md` (556 files)
- Officials: `~/.claude/skills/bangsamoro/references/barmm-officials-2025-2026.md`

---

## 10.5 Known Fabrication Patterns

The following errors have been documented across multiple BARMM guidebooks and official documents. Study them before producing any research output.[^2]

### Pattern 1: BOL Article Misattribution (13+ documented occurrences)

The BOL has **18 articles (I-XVIII)**, not 13. The most dangerous swaps:

| Wrong | Correct | Why It Happens |
|-------|---------|---------------|
| Art. IX cited for Shari'ah | **Art. X** is Justice System / Shari'ah | Art. IX is Basic Rights — adjacent numbering causes confusion |
| Art. V cited for Intergovernmental Relations | **Art. VI** is Intergovernmental Relations | Art. V is Powers of Government — adjacent |
| Art. VII cited for Wali | **Art. VIII** is Wali | Art. VII is Bangsamoro Government (Parliament) — adjacent |
| Art. VIII cited for Transition | **Art. XVI** is Transition | Art. VIII is Wali — completely wrong article |
| Art. XII, Sec. 9 cited for Block Grant | **Art. XII, Secs. 15-16** | Sec. 9 is "Limitations on the Taxing Powers" |
| Art. XII, Sec. 10 cited for SDF | **Art. XIV, Sec. 2** | SDF is in a different article entirely |

**Prevention:** Print the 18-article map (Appendix A). Post it on your desk. Check every BOL citation against it before including the citation in any output.

### Pattern 2: BAA Number Fabrication

| Fabricated Claim | Reality |
|-----------------|---------|
| "BAA 25 (Education Code)" | BAA 25 is a hospital upgrade (Datu Blah Sinsuat Hospital). Education Code = **BAA 18** |
| "BAA 60 (BEZA Act)" | BAA 60 is a memorial site (Sheikh Salamat Hashim). BEZA is created by **BOL Art. XII, Sec. 6** |
| "BAA 11 (Education Code)" | BAA 11 is the Power of Appointment Act. Education Code = **BAA 18** |
| Any BAA > 89 | Only 89 BAAs enacted as of February 2026 |
| "BAA 46 (Revenue Code)" | BAA 46 creates the Municipality of Malidegao. No Bangsamoro Revenue Code has been enacted |

**Prevention:** Verify every BAA number against the index before citing it.

### Pattern 3: Ministry Abbreviation Errors

| Wrong | Correct | Full Name |
|-------|---------|-----------|
| MOL | **MOLE** | Ministry of Labor and Employment |
| MST | **MOST** | Ministry of Science and Technology |
| MPWH | **MPW** | Ministry of Public Works |
| MOSD | **MSSD** | Ministry of Social Services and Development |

The Bangsamoro Government has **15 line ministries** (not 16). The OCM is not a ministry.

**Prevention:** Use the official abbreviation list: MAFAR, MBHTE, MENRE, MFBM, MOH, MHSD, MIPA, MILG, MOLE, MPOS, MPW, MOST, MSSD, MTIT, MOTC.

### Pattern 4: Temporal Errors

| Error | Correct |
|-------|---------|
| "6 provinces in BARMM" | **5 provinces** after SC Sulu ruling (September 2024) |
| "ARMM created by 1996 FPA" | ARMM created by **RA 6734 (1989)**. The 1996 FPA led to RA 9054, which amended the ARMM organic act |
| "Shari'ah Appellate Court" | **Shari'ah High Court** (BOL Art. X, Sec. 7) |
| "OHRAORA" | **ORAOHRA** |

---

## 10.6 Peer Review Protocols

Before submitting any research output with institutional consequences (legal opinions, legislative briefers, mandate matrices for strategic plans), have it reviewed by a second researcher or legal officer.

**What the reviewer checks:**
- [ ] Every BOL article number verified against the 18-article map
- [ ] Every BAA number verified against the index
- [ ] Every verbatim quotation verified against the source text
- [ ] Every provision confirmed as good law (not repealed, amended, or struck down)
- [ ] The national law relationship is correctly applied
- [ ] The Comparative Matrix conflicts are correctly resolved
- [ ] The Search Record is complete — all 7 tiers covered or exclusions documented
- [ ] Citations follow Feliciano 10th Edition format

**When peer review is mandatory:**
- Legal opinions issued by legal officers or the Attorney-General's Office
- Legislative research briefers that will be presented to committee
- Legal mandate matrices that will be submitted to BPDA
- Any output that will be cited in an enacted BAA or adopted resolution

**When peer review is recommended but not mandatory:**
- Internal research memoranda for working use
- Preliminary analyses shared within the office
- Draft matrices subject to further revision

---

## 10.7 Keeping Current

The BARMM legal landscape changes constantly. Parliament passes new BAAs. The Chief Minister issues executive orders. The Supreme Court renders decisions. National laws are amended. Your Research Memorandum from six months ago may cite provisions that have since been modified.

**Three habits for staying current:**

**Habit 1: Monitor the Bangsamoro Gazette.** The Gazette is the official publication vehicle for BAAs, executive orders, and memorandum circulars. Check it regularly — at minimum, at the start of every new research task.

**Habit 2: Track BAA enactments.** Maintain or access a running list of enacted BAAs. As of February 2026, there are 89. When Parliament enacts BAA 90, update your reference. BAAs 82-89 were enacted in January-February 2026 alone — including the Labor Code (BAA 82), the Budget System Act (BAA 84), the Parliamentary District Act (BAA 86), and the Transitional Justice Program (BAA 89).

**Habit 3: Review the Legal Mandate Matrix annually.** The Strategic Planning Guidebook recommends reviewing the Legal Mandate Matrix at the start of every planning cycle.[^3] Apply the same discipline to your research: when a new BAA is enacted in your sector, update your reference files and note the change.

---

## 10.8 Building Institutional Research Capacity

Legal research is not a solo activity. It is an institutional competency that grows stronger when practiced, shared, and systematized.

**Build a shared research library.** When you complete a Research Memorandum, file it where other researchers can find it. A shared drive or document management system that organizes memoranda by topic, date, and researcher prevents duplicate research and builds institutional memory.

**Standardize outputs across your office.** Use the formats in Chapter 9 consistently. When every researcher in the office uses the same Research Memorandum template, the same citation format, and the same Comparative Matrix structure, outputs become interchangeable and reviewable.

**Train new staff on the methodology.** This guidebook is a training manual as much as a reference manual. When a new legislative researcher, legal officer, or planning staff member joins your office, have them read Chapters 1-3 and complete a practice research task using the worked examples as models.

**Update the error log.** When you find a new error pattern — a BAA number that is commonly miscited, a BOL article that is frequently confused with an adjacent one — document it. Share it with colleagues. The known fabrication patterns in Section 10.5 were all discovered through real research. Your discoveries make the next researcher's work more reliable.

---

## 10.9 Quality Checklist — Master

This is the comprehensive quality checklist for any legal research output. It consolidates the chapter-level checklists from Chapters 2-9 into a single reference.

### Research Process
- [ ] Research question documented (three-part frame: subject, jurisdiction, action)
- [ ] National law relationship test applied (Enumerated — no consistency required / National law consistency required / Residual national power / Gap)
- [ ] All seven tiers searched (or exclusions documented in Search Record)
- [ ] Comparative Matrix built for subjects addressed by multiple tiers
- [ ] Provision chains traced (up to 3 levels) for key provisions
- [ ] Shari'ah checkpoint completed (dimension identified or confirmed absent)
- [ ] Search Record complete: terms, tiers, sources, date, researcher

### Verification
- [ ] Every provision verified against source text (not from memory)
- [ ] Every BOL article number checked against the 18-article map
- [ ] Every BAA number checked against the index (no number > 89)
- [ ] Every provision confirmed as good law (not repealed, amended, or struck down)
- [ ] Actor correctly identified for every obligation ("Bangsamoro Government" vs. "National Government")
- [ ] Ministry abbreviations verified against the official 15-ministry list
- [ ] Territory references note Sulu status (5 provinces post-SC ruling, September 2024)

### Output
- [ ] Research Memorandum produced as foundation for all downstream outputs
- [ ] Output format matches audience and purpose
- [ ] All citations follow Feliciano 10th Edition format
- [ ] Seven Never-Fabricate Rules applied
- [ ] Verbatim text copied from source, not paraphrased
- [ ] Peer review completed (if required per Section 10.6)

---

## Key Takeaways

1. **Verification is not the last step — it runs through every step.** Check as you go, not only at the end.

2. **Verbatim accuracy is non-negotiable.** Copy from the source. Do not paraphrase. Do not type from memory.

3. **Know the error patterns.** The BOL 18-article map, the BAA fabrication list, the ministry abbreviation whitelist — these are your defenses against the most common mistakes.

4. **Good law is current law.** The Bangsamoro Parliament enacts new legislation every session. Verify that every provision you cite is still in force.

5. **Legal research is an institutional competency.** Share your work, standardize your formats, train your colleagues, and update the error log. Your research makes the next researcher's work better.

---

[^1]: BAA 58 (Parliamentary Districts) and BAA 77 (Reconstituted Parliamentary Districts) were declared unconstitutional by the Supreme Court (October 2025). BAA 86 (Parliamentary District Act, January 2026) was enacted as the replacement.

[^2]: Fact-Check Error Log (living document, last updated March 2026). Maintained at `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md`.

[^3]: Strategic Planning Guidebook for the Bangsamoro Government (Cotabato City: Bangsamoro Government, 2026), Chapter 2, Section 2.6, Common Pitfall 5 ("Treating the legal mandate review as a one-time exercise").
