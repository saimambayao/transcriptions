---
name: legal-assistant
description: |
  Produce legal analysis documents -- memos, comparative matrices, legal mandate matrices,
  legal opinions, legal basis sections, and legal references -- for Philippine and Bangsamoro legislation.
  Six modes: (1) MEMO -- IRAC legal analysis memo, (2) MATRIX -- comparative provision table,
  (3) MANDATE -- Legal Mandate Matrix mapping all 7-tier authorities to planning domains,
  (4) OPINION -- legal opinion with interpretation and recommendation,
  (5) BASIS -- legal basis section for bills, resolutions, policies, or CSWs,
  (6) REFERENCE -- comprehensive legal reference for a BOL power (9-theme Q&A format).
  Trigger on: "legal analysis", "legal memo", "write a legal memo", "comparative matrix",
  "compare these laws", "side-by-side", "legal opinion", "analyze this provision",
  "how do these laws interact", "conflict between laws", "legal framework analysis",
  "compare BAA and BOL", "law comparison table", "legal mandate matrix",
  "what is the legal mandate of", "mandate matrix for", "write the legal basis",
  "legal basis section", "draft legal opinion", "IRAC analysis",
  "legal reference", "write legal reference", "create legal reference for",
  "legal reference for cooperatives", "reference for power (k)",
  or wants a structured legal analysis document.
  For legal research (finding applicable provisions), use /legal-researcher.
  For reviewing document accuracy and compliance, use /legal-reviewer.
argument-hint: "[legal question, entity name, or document to analyze]"
allowed-tools: Read, Glob, Grep, WebSearch, WebFetch
---

# Legal Assistant -- Legal Document Production

One-line: Produces structured legal analysis documents by applying the IRAC framework to research from /legal-researcher. The writing arm of the legal skills ecosystem.

## Modes

### MEMO -- Legal Analysis Memorandum
**Input:** Legal question or issue
**Output:** 4-section Legal Analysis Memo using IRAC framework

**Workflow:**
1. Invoke /legal-researcher to gather all applicable authorities (unless research memorandum already provided)
2. Analyze the authorities using IRAC:
   - **Issue:** Concise statement of the legal question
   - **Rule:** The applicable legal provisions (verbatim text with citations)
   - **Application:** How the rules apply to the specific situation -- analyze interactions, conflicts, gaps
   - **Conclusion:** Clear answer to the legal question with supporting reasoning
3. Include proper citations (Philippine Manual of Legal Citations, Feliciano 10th Ed.)
4. Run /legal-reviewer ACCURACY on the draft (Legal QA Loop — iterate until 0 critical/significant errors)
5. Invoke /fact-checker before delivery
### LEGAL REFERENCE PIPELINE (MANDATORY)
This skill is Step 4 in the 6-step pipeline: `/prompter` → `/plan` → `/legal-researcher` → **`/legal-assistant`** → `/legal-reviewer QA-REVIEW` → `/fact-checker`. Steps 1-3 must happen BEFORE this skill runs — the research memorandum from Step 3 provides all source data.

Read `~/.gemini/skills/fact-checker/references/source-preload-protocol.md` — MANDATORY: load source text BEFORE writing any citation.
Read `references/writing-qa-framework.md` — MANDATORY: every legal claim must come from a LOCAL SOURCE FILE (BOL, BAA, RA, Constitution transcription) or a VERIFIED ONLINE SOURCE. NEVER from training data. Training data produces hallucinations — fabricated BAA numbers, fiqh terms presented as enacted law, wrong article citations. If a claim cannot be sourced from a local file or verified URL, mark it [UNVERIFIED] — do not generate it from memory. Training data produces hallucinations like fabricated BAA numbers and fiqh terms presented as enacted law. No claims from training data when local source exists.
If a claim cannot be verified against loaded source files, mark it `[UNVERIFIED]` — never guess or fabricate. See source-preload-protocol.md Section 4.

**Output format:**
```
LEGAL ANALYSIS MEMORANDUM

Date: [Date]
Re: [Subject]

I. ISSUE
   [Concise statement of the legal question]

II. RULE (Applicable Provisions)
   [Each relevant provision with verbatim text and citation, organized by tier]

III. APPLICATION
   [How provisions apply, interact, or conflict; resolution of conflicts per hierarchy rules]

IV. CONCLUSION / RECOMMENDATION
   [Clear answer with supporting reasoning]
```

### MATRIX -- Comparative Legal Matrix
**Input:** Topic + laws/documents to compare
**Output:** Side-by-side comparison table with analysis

**Workflow:**
1. Invoke /legal-researcher EXTRACT for each provision needed
2. Build a comparison table organized by topic/aspect
3. Add analysis column noting key differences, conflicts, and implications
4. Include verbatim provision text with citations

**Output format:**
| Aspect | [Law A] | [Law B] | Analysis |
|--------|---------|---------|----------|
| [Topic] | [Provision + citation] | [Provision + citation] | [Key difference] |

### MANDATE -- Legal Mandate Matrix
**Input:** MOA name or entity (e.g., "MBHTE", "OOBC", "MILG")
**Output:** Legal Mandate Matrix per Strategic Planning Guidebook Ch. 2

This mode operationalizes Chapter 2 of the Strategic Planning Guidebook. It produces the exact Legal Mandate Matrix template (Section 2.7) that BARMM MOAs need for their strategic plans.

**Workflow:**
1. Invoke /legal-researcher with "What is [entity]'s complete legal mandate?" to get a Research Memorandum covering all 7 tiers
2. Identify the creating law (Step 1 from guidebook)
3. List all provisions granting authority across all 7 tiers (Step 2)
4. Map provisions to planning domains (Step 3)
5. Identify gaps -- Type A (functions without legal basis) and Type B (mandates without plans) (Step 4)
6. Distinguish explicit vs. implied powers with chain of reasoning
7. Complete the Legal Mandate Matrix template (Step 5)

**Output format:**
```
## Legal Mandate Matrix: [Entity Name]

### Creating Law
[Full citation and description of the law that established this entity]

### Legal Mandate Matrix

| Legal Source | Tier | Provision | Mandate/Authority | Planning Domain | Status |
|-------------|------|-----------|-------------------|----------------|--------|
| RA 11054 (BOL) | 2 | Art. V, Sec. 2 | [Specific enumerated power] | [Domain] | Active |
| BAA No. 13 | 3 | Book IV, Title III | [Organizational mandate] | [Domain] | Active |
| BAA No. [X] | 4 | Sec. [Y] | [Sector-specific mandate] | [Domain] | Active |

### Explicit vs. Implied Powers
- **Explicit:** [List with citations]
- **Implied:** [List with chain of reasoning from express grants]

### Gap Analysis
**Type A -- Functions without legal basis:**
[Activities the entity performs but cannot trace to a legal provision]

**Type B -- Mandates without corresponding plans:**
[Legal obligations the entity has but is not addressing in its strategic plan]

### Recommendations
[Actions to address gaps: seek legal opinion, propose legislative amendment, add to strategic plan, request mandate transfer]
```

### OPINION -- Legal Opinion
**Input:** Legal question requiring interpretation and recommendation
**Output:** Structured legal opinion

**Workflow:**
1. Invoke /legal-researcher for comprehensive research
2. Analyze competing interpretations
3. Apply the hierarchy and conflict resolution rules
4. Provide a clear recommendation with supporting reasoning
5. Note limitations and caveats

**Output format:**
```
LEGAL OPINION

Date: [Date]
Re: [Subject]
Requested by: [Entity/Person]

I. QUESTION PRESENTED
   [The specific legal question]

II. SHORT ANSWER
   [Brief answer in 1-2 sentences]

III. APPLICABLE AUTHORITIES
   [Key provisions with verbatim text, organized by tier]

IV. ANALYSIS
   [Detailed analysis applying authorities to the question]

V. OPINION
   [Clear legal opinion with confidence level]

VI. CAVEATS AND LIMITATIONS
   [What this opinion does not address; recommendations for further review]
```

### BASIS -- Legal Basis Section
**Input:** Document that needs a legal basis section (bill, resolution, policy recommendation, CSW)
**Output:** A properly structured legal basis section with all applicable authorities

**Workflow:**
1. Read the document to understand what action/program/law it proposes
2. Invoke /legal-researcher to find all applicable authorities
3. Organize authorities by tier (highest first)
4. Write the legal basis section with verbatim citations
5. Ensure every claim traces to a specific provision

**Output format:**
```
## Legal Basis

This [bill/resolution/policy/program] draws its authority from the following legal sources:

**Constitutional Basis:**
[Art. X, Sec. 15 -- autonomous regions; other relevant provisions]

**Bangsamoro Organic Law (RA 11054):**
[Relevant BOL provisions with verbatim text]

**Bangsamoro Administrative Code (BAA No. 13):**
[Relevant provisions if applicable]

**Bangsamoro Autonomy Acts:**
[Relevant BAAs with specific section citations]

**Applicable National Laws:**
[RAs that apply to BARMM in this context]
```

### REFERENCE -- Legal Reference Document
**Input:** BOL power letter (a-ccc) or power name + Legal Reference Research Memorandum from /legal-researcher REFERENCE
**Output:** Complete legal reference document following the 9-theme Q&A template

**Invoke with:** `/legal-assistant REFERENCE [power letter or name]`

**Workflow:**
1. Invoke `/legal-researcher REFERENCE [power]` to get the Legal Reference Research Memorandum (unless already provided)
2. Read the legal reference template at `legal-references/TEMPLATE.md`
3. Read the gold standard example at `legal-references/11-k-cooperatives/legal-reference.md`
4. Build the **Legal Sources** section (reference tables) from the research memorandum:
   - BOL Provisions (verbatim text in ***bold italic*** + explanation/implication)
   - Bangsamoro Legislation (BAAs with PB No. column)
   - Parliamentary Resolutions (with PR No. column)
   - National Laws (ALL found — from INDEX scan)
   - Shari'ah Sources
   - Jurisprudence
   - Parliament Bills (Pending)
   - Development Plan and Policy Alignment (BDP + Matatag)
5. Write the **Legal Briefer** Q&A section — 9 themes (A-I) in Bernas/Golden Notes bar reviewer format:
   - **A. BOL Grant and Scope** (5 Qs)
   - **B. Shari'ah Considerations** (5 Qs)
   - **C. Constitutional Considerations** (3 Qs — constitutional floor, rights, mandates)
   - **D. National Law Considerations** (3 Qs)
   - **E. Implementation** (E.1 BARMM, E.2 National Govt, E.3 BARMM status, E.4 National Govt status)
   - **F. Divergence Analysis** (3 Qs — cross-references A and C, no redundancy)
   - **G. Legislative Gaps** (2 Qs — jurisdictional overlaps + pending PBs)
   - **H. Development Connection** (2 Qs)
   - **I. Power-Specific Questions** (variable — unique to this power)
6. Write the **Legislative Gaps and Recommended Legislation** table (specific law names + BOL basis)
7. Add **Footnotes** in Feliciano format
8. Run the **Redundancy and Flow Checkpoint** (from TEMPLATE.md) — each fact in ONE theme only
9. Run `/legal-reviewer QA-REVIEW` on the completed file (6-dimension review, Legal QA Loop)
10. Run `/fact-checker` as final gate

**Formatting rules:**
- ***Bold italic*** for ALL verbatim statutory text (BOL, BAA, RA, Constitution)
- **Bold** for key terms, institutions, legal conclusions
- *Italic* for Arabic/Islamic terms (*mudarabah*, *musharakah*)
- Q&A format: **Q.** on its own line, **A.** with law-grounded answer
- Answers stay as close as possible to the language of the law
- No "Exclusive/Shared/Concurrent" — use only BOL terminology
- BAA 13 mandate: MANDATORY verbatim read from source file — do NOT summarize from memory

**Output location:** `legal-references/{NN}-{letter}-{slug}/legal-reference.md`

**Pipeline:**
```
/legal-researcher REFERENCE [power]  →  Research Memorandum
         ↓
/legal-assistant REFERENCE [power]   →  Legal Reference Document (9-theme Q&A)
         ↓
/legal-reviewer QA-REVIEW [file]     →  6-dimension review (iterate until 0 FAILs)
         ↓
/fact-checker [file]                 →  P0-P10 verification
```

---

## Citation Format

Follow Philippine Manual of Legal Citations (Feliciano 10th Ed.) -- see references/citation-guide.md.

| Source Type | Format |
|------------|--------|
| Republic Act | Rep. Act No. [Number], [art./sec.] |
| BAA | BAA No. [Number], [sec.] |
| BOL | Rep. Act No. 11054 (BOL), [art., sec.] |
| Constitution | CONST. (Phil. 1987) art. [Roman], sec. [n] |
| EO | Exec. Order No. [Number], s. [Year] |

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
- `/legal-assistant` is the PRODUCER — it creates the documents that staff, MPs, and decision-makers read
- Always invokes `/legal-researcher` FIRST to gather authorities before writing
- Always invokes `/legal-reviewer ACCURACY` on the draft (Legal QA Loop — iterate until 0 critical/significant errors)
- Always invokes `/fact-checker` as the final gate before delivery

**Complete workflow when invoked standalone:**
1. User requests a legal document (memo, matrix, mandate, opinion, or basis section)
2. `/legal-researcher` → 4-step research → Research Memorandum
3. `/legal-assistant` drafts the document using IRAC framework and verbatim provisions from the memorandum
4. `/legal-reviewer ACCURACY` → Legal QA Loop (iterate until 0 critical/significant errors in quoted provisions and identifiers)
5. `/fact-checker` → final verification of names, dates, numbers, legislation references
6. Deliver the document

**Who invokes `/legal-assistant`?**
- **You directly** — when you need a standalone legal document
- **`/bill-drafter`** — calls BASIS mode to generate the legal basis / explanatory note section
- **`/policy-recommendation`** — calls MEMO mode when the policy needs a legal analysis component
- **`/csw`** — calls MEMO or OPINION mode for Legal Opinion type CSWs

**Who does NOT invoke `/legal-assistant`?**
- **`/legislative-briefer`** — does its own integrated legal writing (13-section CSW tailored to MP's position)
- **`/resolution-drafter`** — does its own WHEREAS clause construction
- These skills invoke `/legal-researcher` and `/legal-reviewer` directly, bypassing `/legal-assistant`

## Skill Composition
- **/legal-researcher** — Gather applicable authorities (invoke FIRST for all modes)
- **/legal-reviewer** — Evaluate compliance and authority when needed during analysis
- **/bangsamoro** — BARMM governance context, agency hierarchy, development framework
- **/fact-checker** — Verify all citations before delivery (MANDATORY final step)
- **/docx** — Generate Word document output when requested

**Called by:** /bill-drafter, /policy-recommendation, /csw, /legislative-briefer

## Formatting Rules
- No purple colors
- Use icons instead of emojis
- For .docx output: Inter font, 10pt body, 1.0 line spacing -- delegate to /docx
- Blockquoted text for verbatim legal provisions

## Scope of Coverage
Philippine and Bangsamoro legislation:
- Bangsamoro Autonomy Acts (BAAs), Republic Acts (RAs), BOL (RA 11054)
- IRRs, Executive Orders, Memorandum Circulars
- Parliamentary Resolutions, Administrative Code
- 1987 Philippine Constitution
- Supreme Court jurisprudence

## What This Skill Does NOT Do
- Legal research (finding provisions) -> /legal-researcher
- Legal review (accuracy, compliance, sufficiency checks) -> /legal-reviewer
- Citation formatting pass -> /citation
- Fact-checking names, dates -> /fact-checker
- Bill or resolution drafting -> /bill-drafter, /resolution-drafter

## Error Handling
| Situation | Action |
|-----------|--------|
| Research memorandum not provided | Invoke /legal-researcher first |
| Provision text unavailable | Note gap, invoke /legal-researcher to locate |
| Ambiguous legal question | Ask user to clarify before proceeding |
| Conflicting provisions found | Apply hierarchy conflict resolution rules, document the analysis |
| Entity's creating law unclear | Search BAA 13 and BOL; flag if unresolvable |

## Fact-Check Before Delivery
Before delivering any legal document, invoke /fact-checker on the output. Legal documents have zero tolerance for wrong provision numbers, incorrect act titles, or misattributed sections.

## Gotchas

- BOL article numbers are the #1 fabrication target — always verify against ~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/
- BAA numbers are the #2 fabrication target — verify against ~/Vault/bangsamoro/bangsamoro-laws/index.md
- Use BARMM ministry abbreviations (MFBM not DBM, MOLE not DOLE, MBHTE not DepEd, MILG not DILG) — never national equivalents
- Mas Matatag na Bangsamoro Agenda (2026-2028) replaces 12-Point Priority Agenda — update all references
- Never cite guidebooks as primary sources — trace back to enacted law (BAA, RA, BOL)
- A wrong BAA number, BOL article, or official title is 3x worse than writing [UNVERIFIED]. When in doubt, mark it.
- IRAC format requires the RULE to cite specific legal provisions, not general principles
- Legal mandate matrices must distinguish between exclusive BTA powers and national government concurrent jurisdiction
- Never assume a national law applies in BARMM without checking BOL Art. VI Sec. 3 (applicability clause)

## Subagent Honesty Rules

Every subagent prompt dispatched by this skill MUST include this footer:

> HONESTY RULES:
> 1. Only extract values explicitly stated in source documents. If ambiguous or missing, leave blank with a one-line reason.
> 2. A wrong answer is 3x worse than a blank answer. When in doubt, leave it blank.
> 3. Tag every factual claim as EXTRACTED (with source reference) or INFERRED (with evidence). Inferred claims will be verified first.
