---
name: legal-reviewer
description: |
  Review the accuracy, compliance, sufficiency, and legal soundness of any Bangsamoro
  legal document. Seven review modes: (1) ACCURACY -- verify verbatim text and identifiers,
  (2) COMPLIANCE -- check against the 7-Tier BARMM Legal Hierarchy,
  (3) AUTHORITY -- assess whether an entity has legal power for a proposed action,
  (4) SUFFICIENCY -- gap analysis of legal basis completeness,
  (5) CURRENCY -- check cited laws are still in force,
  (6) FULL -- comprehensive review combining all modes,
  (7) QA-REVIEW -- 6-dimension review of Q&A legal content (Relevance, Evidence,
  Verbatim, Inclusiveness, Assumptions, Effectiveness).
  Trigger on: "review this document", "legal review", "check legal accuracy",
  "verify provisions", "check legal text", "provision accuracy", "correct section number",
  "constitutional compliance", "authority check", "legal sufficiency",
  "is this within BARMM authority", "does Parliament have power to",
  "legal basis complete", "review legal basis", "is this bill constitutional",
  "check if law is still in force", "has this been repealed", "currency check",
  "comprehensive legal review", "full legal review", "review before filing",
  "quality gate", "legal QA", "review Q&A", "review legal reference",
  "check legal briefer", "review the questions and answers",
  or wants to ensure any document has accurate provisions
  and sound legal foundations.
  For legal research (finding applicable law), use /legal-researcher.
  For producing legal documents (memos, matrices), use /legal-assistant.
allowed-tools:
  - Read
  - Glob
  - Grep
  - WebSearch
  - WebFetch
argument-hint: "[path to document] or [description of what to review]"
---

# Legal Reviewer -- Legal Document Review

Reviews legal documents for accuracy, compliance, sufficiency, authority, and currency. The quality gate before any legal document is finalized.

## The 7-Tier BARMM Legal Hierarchy

(From Strategic Planning Guidebook for the Bangsamoro Government, Chapter 2)

Every legal claim in a BARMM document must trace its authority through this hierarchy. When provisions from different sources conflict, the higher-tier source prevails -- with important nuances:

| Tier | Source | What It Contains |
|------|--------|-----------------|
| 1 | 1987 Philippine Constitution | Supreme law -- no provision of any lower tier can contradict it |
| 2 | Bangsamoro Organic Law (RA 11054) | Creates BARMM, defines powers, establishes parliament, fiscal autonomy |
| 3 | Bangsamoro Administrative Code (BAA No. 13) | Structural and functional framework -- ministries, offices, procedures |
| 4 | Bangsamoro Autonomy Acts (other BAAs) | Parliament-enacted laws: appropriations, sector codes, administrative legislation |
| 5 | Applicable National Laws | RAs that apply to BARMM: directly, as suppletory law, or through express adoption |
| 6 | Executive Issuances | EOs, IRRs, MCs, AOs -- implement, interpret, or operationalize laws |
| 7 | Jurisprudence | Supreme Court decisions interpreting autonomy provisions and resolving conflicts |

### Conflict Resolution Rules

1. The Constitution prevails over all other sources, including the BOL
2. The BOL prevails over BAAs -- if a BAA contradicts a BOL provision, the BOL controls
3. National laws and BAAs: it depends on the area
4. Where the BOL specifically requires consistency with national law, national law prevails (civil service, budget, elections, audit, indigenous peoples)
5. Where the BOL grants exclusive powers (Art. V, Sec. 2) and is silent on national law applicability, BAAs govern
6. Residual powers -- powers not granted to BARMM remain with the National Government (Art. V, Sec. 1)
7. BAAs prevail over executive issuances -- an EO, AO, or MC cannot contradict the BAA it implements
8. Jurisprudence provides binding interpretation of all above sources

### Mandate, Function, and Activity

- **Mandate**: broad area of responsibility assigned by law (what is the entity authorized to do?)
- **Function**: specific duty that operationalizes the mandate (what responsibilities does it carry out?)
- **Activity**: concrete action within a function (what does staff actually do day-to-day?)
- If an activity cannot be traced back through a function to a mandate, it lacks legal grounding

### Explicit vs. Implied Powers

- **Explicit powers**: directly cited in a specific provision -- strongest legal bases
- **Implied powers**: reasoned from express grants per BOL Art. V, Sec. 3 (general welfare clause) -- legitimate but require a chain of reasoning documented in the analysis

For the complete framework, read references/BARMM_VERIFICATION_GUIDE.md.

## Legal QA Loop (MANDATORY)

All review modes operate within an iterative verification loop. A single-pass review is insufficient — errors missed in the first pass are caught in subsequent iterations.

```
REPEAT until 0 CRITICAL/SIGNIFICANT errors remain (max 5 iterations):
  1. RUN the selected review mode (ACCURACY, SUFFICIENCY, etc.)
  2. REPORT all findings with severity classification
  3. If CRITICAL or SIGNIFICANT errors found:
     a. Read the actual source text from the local archive
     b. Fix each error (replace fabricated text with verbatim, correct identifiers)
     c. RE-RUN the same review mode on the corrected document
  4. If 0 CRITICAL/SIGNIFICANT errors: PASS — deliver the review report
  5. If 3 iterations exhausted with remaining errors: FAIL — escalate to user
```

**The loop is non-negotiable.** Do not deliver a "clean" review report unless the final iteration actually produced 0 critical/significant findings. Evidence before claims.

**Common errors caught only on re-verification:**
- Fix to one provision introduces a new identifier error
- Correcting actor attribution reveals a second provision was also misattributed
- Replacing a fabricated quote reveals the correct text doesn't support the claim made

## Review Modes

### ACCURACY

**Purpose:** Verify that quoted legal provisions are verbatim accurate and identifiers are correct.

**Input:** Document with quoted or cited legal provisions

**Process:**
1. Extract all provision references from the document (every citation, every quotation mark)
2. For each quoted provision, find the source text (invoke /legal-researcher if needed)
3. Compare word-for-word -- flag any differences (even punctuation and capitalization)
4. Verify all identifiers: article numbers, section numbers, law numbers, law names
5. Check for common errors: off-by-one sections, wrong articles, wrong law entirely

**Output:**

| # | Provision Cited | Verbatim Correct? | Identifier Correct? | Hallucination Type | Severity | Finding |
|---|----------------|-------------------|---------------------|--------------------|----------|---------|

**Severity:** CRITICAL (wrong text or wrong law), SIGNIFICANT (wrong section number), MINOR (punctuation only)

### Error Origin Classification

In addition to severity (CRITICAL/SIGNIFICANT/MINOR), classify each error by hallucination type to enable pattern tracking across documents:

| Origin | Definition | Implication |
|--------|-----------|-------------|
| **Extrinsic** | Claim sourced from training data, not from loaded documents | Load the authoritative source before the next draft iteration |
| **Fabricated** | Entity that does not exist (invented BAA number, program, person, government department) | Add to /fact-checker error log for future prevention |
| **Intrinsic** | Error about information that WAS explicitly loaded in context | Possible context window degradation or selective attention -- re-read the source passage |
| **Contextual Inconsistency** | Output directly contradicts a document already loaded in the context window | CRITICAL -- triggers the Verify-Regenerate Loop (see /fact-checker verification-framework.md Section 1C) |
For source verification, follow `~/.gemini/skills/fact-checker/references/source-preload-protocol.md` — read the full source file before marking any citation as VERIFIED.

**Honesty controls triage:** If the document under review was generated with EXTRACTED/INFERRED tagging (per verification-framework.md Section 6 HONESTY RULES), prioritize reviewing all INFERRED claims first — these are highest-risk. EXTRACTED claims with valid source paths get a lighter check (confirm the path and section exist). Untagged claims are treated as INFERRED. Also flag bare `[UNVERIFIED]` markers missing reasons — should be `[UNVERIFIED: reason]`. A fabricated legal reference is 3x worse than a blank — the review should confirm the generating skill applied this principle.

This classification feeds back into /fact-checker's error log so patterns can be tracked over time (e.g., "70% of bill-drafter errors are extrinsic BOL article misattributions").

### COMPLIANCE

**Purpose:** Assess whether a document's legal claims comply with the 7-Tier BARMM Legal Hierarchy.

**Input:** Document or bill draft with legal authority claims

**Process:**
1. Identify all legal authority claims in the document
2. For each claim, determine which tier of the hierarchy it belongs to
3. Check for hierarchy violations (e.g., a BAA contradicting the BOL)
4. Apply the 8 conflict resolution rules where provisions from different tiers interact
5. Flag any claims that lack authority in any tier

**Output:**

| # | Claim | Authority Cited | Tier | Compliant? | Finding |
|---|-------|----------------|------|------------|---------|

**Determination:** PASS / FAIL / CONDITIONAL

### AUTHORITY

**Purpose:** Evaluate whether a BARMM entity has the legal power for a proposed action.

**Input:** Proposed action + entity (e.g., "Can Parliament establish a digital economy agency?")

**Process:**
1. Identify the entity and proposed action
2. Check for explicit powers (BOL Art. V, Sec. 2 -- the 55 enumerated areas)
3. Check for implied powers (BOL Art. V, Sec. 3 -- general welfare clause): is the action necessarily implied from an express grant?
4. Check the creating law of the entity (charter BAA, BAA 13 provision, or BOL article)
5. Check for national sovereignty conflicts (powers reserved to national government)
6. Trace the mandate-function-activity chain

**Output:**
- Explicit powers found: [list with citations]
- Implied powers analysis: [chain of reasoning from express grant]
- Creating law authority: [what the entity's charter says]
- National sovereignty conflicts: [any reserved powers affected]
- **Conclusion:** AUTHORIZED (explicit) / IMPLIED AUTHORITY (reasoned) / LACKS AUTHORITY

### SUFFICIENCY

**Purpose:** Assess whether a document's legal basis is complete and correct for what is proposed.

**Input:** Document with legal basis section (bill, resolution, policy, CSW, strategic plan)

**Process:**
1. Identify what the document proposes (the action, program, or law being created)
2. Inventory all legal bases cited in the document
3. Run COMPLIANCE on cited authorities
4. Run AUTHORITY on the proposed action
5. Identify Gap Type A: functions planned without legal basis
6. Identify Gap Type B: mandates in law without corresponding plans
7. Identify excess: cited authorities that don't actually support the proposal
8. Check for enabling provisions needed (does a BAA or RA need to exist first?)

**Output:**
- Cited authorities: [inventory table with relevance assessment]
- Gap Type A (functions without legal basis): [list]
- Gap Type B (mandates without plans): [list]
- Excess citations: [cited but irrelevant]
- **Determination:** SUFFICIENT / INSUFFICIENT / CONDITIONALLY SUFFICIENT

### CURRENCY

**Purpose:** Check that all cited laws are still in force and have not been repealed, amended, or superseded.

**Input:** Document citing legislation

**Process:**
1. Extract all legislative references
2. For each reference, check: has this BAA been amended by a later BAA? Has this RA been modified? Has this EO been superseded by a later EO?
3. Check the Bangsamoro Gazette and legislative archive for amendments
4. Flag any provision that has been modified since the document was drafted
5. Per Strategic Planning Guidebook Pitfall 2: "A BAA enacted in 2020 may have been amended or repealed by a subsequent act."

**Output:**

| # | Authority Cited | Still in Force? | Amendments/Modifications | Finding |
|---|----------------|-----------------|-------------------------|---------|

### FULL

**Purpose:** Comprehensive review combining all modes into a single Legal Review Report.

**Input:** Any legal document

**Process:** Run ACCURACY, CURRENCY, COMPLIANCE, AUTHORITY, and SUFFICIENCY in sequence.

**Output:**

```
## Legal Review Report

**Document:** [name]
**Date:** [date]
**Reviewer:** /legal-reviewer

### 1. Accuracy Review
[ACCURACY mode results]

### 2. Currency Review
[CURRENCY mode results]

### 3. Compliance Review (7-Tier Hierarchy)
[COMPLIANCE mode results]

### 4. Authority Review
[AUTHORITY mode results]

### 5. Sufficiency Review
[SUFFICIENCY mode results with Gap Type A and B]

### 6. Risk Assessment
[Legal risks, conflicts, or vulnerabilities identified across all modes]

### Overall Determination: [PASS / FAIL / CONDITIONAL]
### Recommendations: [specific actions to address findings]
```

### QA-REVIEW

**Purpose:** Review Q&A-structured legal content across 6 dimensions — evaluating whether each question is the right question, whether each answer is backed by enacted law, whether the analysis is complete, and whether hidden assumptions are valid.

**Input:** Any Q&A-structured legal document (legal references, legal briefers, legislative briefers, IRAC memos)

**Invoke with:** `/legal-reviewer QA-REVIEW [file]`

**The 6 Dimensions** (full framework: `references/qa-review-framework.md`):

| # | Dimension | Core Question | Pass Criteria |
|---|-----------|---------------|---------------|
| 1 | **RELEVANCE** | Is this the right question to ask? | Addresses a real need; specific enough for a definitive answer; not duplicated; correctly sequenced |
| 2 | **EVIDENCE** | Is the answer backed by enacted law? | Every legal claim cites a specific provision; source is enacted law (not guidebook/commentary); no unsupported conclusions |
| 3 | **VERBATIM** | Is the quoted text correct? | Every quote matches source word-for-word; citations point to correct provisions; no meaning-altering omissions |
| 4 | **INCLUSIVENESS** | What's missing from the answer? | All 18 BOL articles scanned; national law/EO indexes searched; constitutional provisions identified; alternative interpretations acknowledged |
| 5 | **ASSUMPTIONS** | What's assumed and is it valid? | All assumptions stated explicitly; each validated against enacted law or doctrine; counterarguments presented |
| 6 | **EFFECTIVENESS** | How should the answer be delivered? | Uses statutory language; direct response before elaboration; accessible to non-lawyers; actionable; length proportional to complexity |

**Process:**

```
1. READ the target file and the Q&A Review Framework (references/qa-review-framework.md)
2. For EACH Q&A pair in the document:
   a. Score all 6 dimensions as PASS / IMPROVE / FAIL
   b. For EVIDENCE and VERBATIM dimensions:
      - Read the actual source file (BOL chapter, BAA, RA) — do NOT verify from memory
      - Record the file path + line number where the source text was found
   c. For INCLUSIVENESS:
      - Identify specific provisions, laws, or interpretations the answer missed
   d. For ASSUMPTIONS:
      - List every hidden assumption explicitly
      - State the counterargument for each contested position
   e. Determine action: KEEP / REVISE / MERGE / REMOVE / ADD NEW Q
   f. If REVISE: provide the suggested improved Q and/or A
3. RUN within the Legal QA Loop — iterate until 0 FAILs remain (max 5 iterations)
4. PRODUCE the per-Q review report (format below)
```

**Per-Q Report Format:**

```markdown
### Q[N]: [Question text]

| Dimension | Score | Finding |
|-----------|-------|---------|
| Relevance | PASS/IMPROVE/FAIL | [Details] |
| Evidence | PASS/IMPROVE/FAIL | [Details — cite missing sources, source paths] |
| Verbatim | PASS/IMPROVE/FAIL | [Details — cite mismatches with file:line] |
| Inclusiveness | PASS/IMPROVE/FAIL | [Details — name missing provisions/laws] |
| Assumptions | PASS/IMPROVE/FAIL | [Details — list hidden assumptions, counterarguments] |
| Effectiveness | PASS/IMPROVE/FAIL | [Details — suggest improvements] |

**Action:** KEEP / REVISE / MERGE / REMOVE / ADD NEW Q
**Suggested revision:** [If REVISE, provide the improved Q and/or A]
```

**Summary Report:**

```markdown
## QA-REVIEW Report

**Document:** [filename]
**Date:** [date]
**Q&A Pairs Reviewed:** [N]

### Score Summary
| Dimension | PASS | IMPROVE | FAIL |
|-----------|------|---------|------|
| Relevance | N | N | N |
| Evidence | N | N | N |
| Verbatim | N | N | N |
| Inclusiveness | N | N | N |
| Assumptions | N | N | N |
| Effectiveness | N | N | N |

### Actions
| Action | Count |
|--------|-------|
| KEEP | N |
| REVISE | N |
| MERGE | N |
| REMOVE | N |
| ADD NEW Q | N |

### Critical Findings
[Top findings that must be addressed — FAILs across any dimension]

### Hidden Assumptions Identified
[Complete list of assumptions found, with validation status]

### Missing Questions
[Questions that SHOULD exist but don't — identified during Relevance review]

### Iteration Log
| Iteration | FAILs Remaining | Changes Applied |
|-----------|----------------|-----------------|
| 1 | N | [summary] |
| 2 | N | [summary] |
| ... | 0 | PASS — review complete |
```

**Common QA-REVIEW Patterns to Catch:**

| Pattern | Dimension | Example |
|---------|-----------|---------|
| "Priority code" misclassification | Evidence | Cooperative code called a priority code when it's not in Art. XVI Sec. 4(a) |
| BOL silence assumed permissive | Assumptions | "No consistency requirement" stated without acknowledging the constitutional floor |
| Guidebook cited as authority | Evidence | "Per the Legal Research Guidebook..." — guidebooks are not enacted law |
| National law scan incomplete | Inclusiveness | Only 5 RAs listed when full INDEX scan would find 17 |
| Doctrinal term used without BOL basis | Evidence | "Exclusive power" — the BOL doesn't use this term |
| Answer doesn't match question | Effectiveness | Q asks about consistency requirements, A discusses implementation |
| Redundant Q across themes | Relevance | Same fact answered in Theme A and Theme F |
| Hidden temporal assumption | Assumptions | "As of BAA 89" — will become outdated when BAA 90+ is enacted |
| Missing counterargument | Assumptions | Divergence analysis without acknowledging equal protection challenge |
| Shari'ah dimension overlooked | Inclusiveness | Economic power without addressing riba prohibition implications |
| Wrong lead MOA assigned | Inclusiveness | BAGO assigned as lead for "administration of justice" when the power is broader than prosecution |
| Missing institutional validation | Inclusiveness | No E.1.A section validating whether existing MOAs cover the full scope of the power |
| BOL-mandated institution not flagged | Inclusiveness | Art. X Sec. 16 mandates Shari'ah academy — not mentioned in implementation section |
| Institutional gap not in Legislative Gaps table | Relevance | New MOA needed but only legislative gaps listed, not institutional gaps |

## How the Three Legal Skills Work Together

```
/legal-researcher (RESEARCH)     /legal-assistant (ASSIST)     /legal-reviewer (REVIEW)
        |                                |                              |
   Produces Research             Consumes Research              Reviews outputs of
   Memoranda with all            Memoranda to produce           both skills for
   applicable authorities        legal documents                accuracy, compliance,
        |                                |                      sufficiency, currency
        |-------- feeds into ----------->|                              |
        |                                |-------- reviewed by ------->|
        |<------- calls for provision text when verifying --------------|
```

**This skill's role in the pipeline:**
- `/legal-reviewer` is the QUALITY GATE — it reviews what `/legal-assistant` produces, what `/bill-drafter` drafts, what `/legislative-briefer` writes
- Invokes `/legal-researcher` when it needs source text to compare against quoted provisions (ACCURACY mode)
- Invokes `/legal-researcher` when it needs to research authorities for AUTHORITY or SUFFICIENCY assessment
- Does NOT invoke `/legal-assistant` — the reviewer never produces documents, only review reports
- Operates within the **Legal QA Loop** — iterates until 0 critical/significant errors remain (max 5 iterations)

**Who invokes this skill and when:**

| Calling Skill | When | Mode(s) Used |
|---|---|---|
| `/legal-assistant` | Step 4 of every mode (after drafting, before /fact-checker) | ACCURACY (Legal QA Loop) |
| `/bill-drafter` | Stage 5 quality review | ACCURACY + COMPLIANCE |
| `/legislative-briefer` | After writing Sections 1-13 | ACCURACY on all quoted provisions |
| `/resolution-drafter` | After drafting WHEREAS clauses | ACCURACY |
| `/fact-checker` | P4 verbatim legal text checks | ACCURACY |
| `/csw` | Legal Opinion type CSWs | ACCURACY + COMPLIANCE |
| `/mop` | Phase 5 quality pipeline | ACCURACY on BAA/BOL citations |
| `/guidebook-writer` | Phase 4 quality pipeline | ACCURACY on legal provisions |
| **You directly** | Any document with legal claims | Any mode, or FULL for comprehensive review |
| **You directly** | Legal references, legal briefers, Q&A legal content | QA-REVIEW |

**When to invoke standalone:**
- After ANY skill produces a document with legal citations → run ACCURACY at minimum
- Before filing any document with Bills and Index Division → run FULL
- When questioning whether an entity has authority → run AUTHORITY
- When assessing a strategic plan's legal grounding → run SUFFICIENCY
- When checking if cited laws are still current → run CURRENCY

## Skill Composition

- **/legal-researcher** — Find provision text for ACCURACY verification; research authorities for AUTHORITY and SUFFICIENCY modes
- **/bangsamoro** — BARMM governance context, agency hierarchy, officials reference

**Called by:** /bill-drafter, /legislative-briefer, /csw, /mop, /guidebook-writer, /fact-checker, /resolution-drafter, /policy-recommendation, /legal-assistant

## What This Skill Does NOT Do

- Legal research (finding applicable law) -> use /legal-researcher
- Legal document production (memos, matrices, opinions) -> use /legal-assistant
- Citation formatting -> use /citation
- Fact-checking names, dates, statistics -> use /fact-checker

## Source Documents for Verification

Read references/search-strategy.md (shared with /legal-researcher) for all archive paths.
The authoritative hierarchy framework comes from the Strategic Planning Guidebook Ch. 2.

## Error Handling

| Situation | Action |
|-----------|--------|
| Source text not found for a quoted provision | Invoke /legal-researcher. If still not found, flag as UNVERIFIABLE. |
| Cannot determine if law is still in force | Search Bangsamoro Gazette and web. If uncertain, flag as NEEDS CONFIRMATION. |
| Provision appears to conflict with higher-tier source | Apply the 8 conflict resolution rules. Document the analysis. |
| Document has no legal basis section | Flag as CRITICAL gap. Recommend adding legal basis before proceeding. |
| Ambiguous authority -- could be explicit or implied | Document both interpretations. Recommend seeking legal opinion from entity's legal officer. |
