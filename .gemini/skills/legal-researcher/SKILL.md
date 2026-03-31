---
name: legal-researcher
description: |
  Conduct systematic legal research for Philippine and Bangsamoro legislation.
  Follows the professional 5-step methodology: (1) Issue Analysis, (2) Landscape Review
  (secondary sources), (3) Systematic Source Search (primary sources across the 7-Tier
  BARMM Legal Hierarchy), (4) Provision Chain Trace, (5) Verification of good law.
  Produces Research Memoranda that identify all applicable legal authority.
  Trigger on: "legal research", "research the legal basis", "what law applies to",
  "find all applicable laws", "what is the legal mandate of", "research memorandum",
  "what does the BOL say about", "find all BAAs about", "legal basis for",
  "what laws govern", "applicable provisions", "provision lookup", "search legislation",
  "find the relevant law", "show me the provision", "what does BAA [number] say",
  "look up RA", "find Republic Act", "extract provision", "supply verbatim text",
  "what section deals with", "legal landscape for", "7-tier search",
  or any request to research, locate, extract, or inventory legal authorities.
  For legal analysis documents (memos, matrices, opinions), use /legal-assistant.
  For reviewing accuracy and compliance of legal documents, use /legal-reviewer.
allowed-tools:
  - Read
  - Glob
  - Grep
  - WebSearch
  - WebFetch
argument-hint: "[legal question, topic, or provision identifier]"
---

# Legal Researcher — Systematic Legal Research

Conducts professional legal research following the 4-step methodology, producing Research Memoranda with all applicable authorities organized by the 7-Tier BARMM Legal Hierarchy.

### LEGAL REFERENCE PIPELINE (MANDATORY)
This skill is Step 3 in the 6-step pipeline: `/prompter` → `/plan` → **`/legal-researcher`** → `/legal-assistant` → `/legal-reviewer QA-REVIEW` → `/fact-checker`. Steps 1-2 (prompter + plan) must happen BEFORE this skill runs — they identify which local files to read and which INDEX terms to search.

### RESEARCH QA FRAMEWORK (MANDATORY)
Read `references/research-qa-framework.md` before any research task. Every finding must come from a LOCAL SOURCE FILE or VERIFIED ONLINE SOURCE — NEVER from training data. Tag every finding as EXTRACTED (with source file:line) or INFERRED (with reasoning chain). Shari'ah/fiqh terms must be labeled as Islamic jurisprudence — not presented as enacted law.

### ANTI-FABRICATION RULE (NON-NEGOTIABLE)

NEVER paraphrase or summarize legal provisions from memory. For every provision cited:
1. READ the actual source file containing the provision
2. QUOTE the verbatim text — copy-paste, do not retype
3. VERIFY the section/article/law number against the source file
4. If a provision cannot be found in any local source file, mark it as [UNVERIFIED] and note the source gap

Common fabrication patterns to prevent:
- Inventing quotes that sound plausible but aren't in the law
- Using "shall take into consideration" when the actual text says "shall ensure the protection"
- Attributing obligations to the wrong actor (e.g., saying Bangsamoro Government when it's the National Government)
- Citing superseded instruments (e.g., BTA Transition Plan when BAA 13 has enacted the structure)

For ANY provision that cannot be found in local source files, mark it `[UNVERIFIED — provision not found in local archive]` in the Research Memorandum. Never reconstruct legal text from memory.

## The 4-Step Legal Research Process

### Step 1: Issue Analysis

- Parse the legal question from the user's request
- Identify the jurisdiction (BARMM, national, or both)
- Identify the subject matter and relevant legal concepts
- Generate search terms and related concepts (include synonyms)
- Determine which tiers of the legal hierarchy are most relevant

### Step 2: Secondary Sources (Understand the Landscape)

Before searching primary law, understand the legal landscape:

- Consult the 7-Tier BARMM Legal Hierarchy (see "7-Tier BARMM Legal Hierarchy" section below)
- Invoke /bangsamoro for governance context, agency hierarchy, institutional relationships
- Review BDP 2023-2028 chapters for development context if relevant
- Check existing legal commentary and doctrine via web search when local sources insufficient
- This step prevents tunnel vision — understanding the landscape before diving into specific provisions

### Step 3: Primary Sources (Find Controlling Authority)

Systematic search through all 7 tiers of the BARMM Legal Hierarchy:

**Tier 1 — 1987 Philippine Constitution**
- Search for relevant constitutional provisions (Art. X for autonomous regions, Art. VI for legislative power, etc.)
- Source: web search or local reference files

**Tier 2 — Bangsamoro Organic Law (RA 11054)**
- Path: `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` (5 chapter files)
- Start with Art. V, Sec. 2 (55 enumerated powers) and Art. V, Sec. 3 (general welfare clause)
- Search relevant articles by subject matter

**Tier 3 — Bangsamoro Administrative Code (BAA No. 13)**
- Path: `~/apps/transcriptions/legislation/BAAs/BAA-13.md`
- Check Book II (ministries), Book IV (OCM offices), relevant titles for the entity

**Tier 4 — Bangsamoro Autonomy Acts (other BAAs)**
- Path: `~/apps/transcriptions/legislation/BAAs/` (89+ enacted BAAs, check INDEX.md first)
- Search for: creating/charter BAA, cross-cutting BAAs (BAA 38 procurement, BAA 31 civil service, BAA 84 budget), sector-specific BAAs

**Tier 5 — Applicable National Laws**
- Search for national RAs that apply to BARMM: directly (outside BOL exclusive powers), as suppletory law, or through express adoption by Parliament
- Key universal RAs: RA 9184 (procurement), RA 6713 (ethics), RA 3019 (anti-graft), RA 9710 (women), RA 10173 (data privacy)

**Tier 6 — Executive Issuances**
- EOs from Chief Minister or President affecting BARMM
- IRRs for specific BAAs
- Memorandum Circulars from OCM or relevant ministry
- Administrative Orders within the entity

**Tier 7 — Jurisprudence**
- Supreme Court decisions interpreting BARMM authority
- Key case: Province of Sulu v. Executive Secretary (G.R. Nos. 242255, 243246, 243693)
- Search SC E-Library for relevant rulings

**For each authority found, extract:**
- Full citation (Philippine Manual of Legal Citations format)
- Tier number
- Verbatim provision text (or precise summary)
- What mandate/authority it grants or imposes
- Source file path

### Step 4: Provision Chain Trace (MANDATORY for BOL and BAA 13)

After finding initial provisions, trace what they reference:

**1. EXTRACT traceable concepts from each found provision:**
- "rights" → scan Art. IX (Basic Rights), Art. II (Identity), Constitution Art. III
- "powers" → scan Art. V Sec. 2 (55 enumerated), Art. V Sec. 3 (general welfare)
- "obligations/duties" → scan the full article for all duty-bearing provisions
- "functions/mandates" → scan BAA 13 for the entity's full mandate section
- "protection" → scan what is being protected and by whom

**2. FULL-SOURCE SCAN: Read the ENTIRE relevant source document, not just keyword matches:**
- For BOL: read all 5 chapter files in `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/`
- For BAA 13: read the full text at `~/apps/transcriptions/legislation/BAAs/BAA-13.md`
- For Constitution: search for all relevant articles (Art. III Bill of Rights, Art. X Autonomous Regions, Art. XIII Social Justice)

**3. RELEVANCE FILTER:** Given the specific context of the research question, filter which traced provisions actually apply. Not every "rights" provision is relevant to every question.

**4. DEPTH LIMIT:** Follow chains up to 3 levels deep. Stop when:
- The concept is fully defined with verbatim text
- 3 levels of chaining have been reached
- No further references exist

**5. OUTPUT as Provision Chain Map** (include in Research Memorandum):

| Source Provision | Traceable Concept | Related Provisions Found | Relevance to Research Question |
|-----------------|-------------------|------------------------|-------------------------------|

### Step 5: Verification (Confirm "Good Law")

For each authority found:
- Check that it is still in force (not repealed, amended, or superseded)
- Identify any amendments or subsequent legislation that modified it
- Flag provisions that may have been modified by newer BAAs (Parliament has enacted 89+ BAAs since 2019)
- Note conflict resolution implications per the hierarchy rules
- Mark status: "In force", "Amended by [law]", "Superseded by [law]", "Under review"

## Output: Research Memorandum

ALWAYS produce this format:

```
## Legal Research Memorandum

**Question:** [the legal question researched]
**Jurisdiction:** [BARMM / National / Both]
**Date:** [date]
**Requested by:** [user or calling skill]

### Applicable Authorities

| # | Tier | Source | Provision | Authority/Mandate | Status |
|---|------|--------|-----------|-------------------|--------|
| 1 | 1 | 1987 Constitution | Art. X, Sec. 15 | Constitutional basis for autonomous regions | In force |
| 2 | 2 | BOL (RA 11054) | Art. V, Sec. 2(a) | Administrative organization | In force |
| 3 | 3 | BAA No. 13 | Book IV, Title III | Office establishment under OCM | In force |

### Key Provisions (Verbatim)

**[Citation]:**
> [Exact verbatim text]
— Source: [file path]

### Provision Chain Map

| Source Provision | Traceable Concept | Related Provisions Found | Relevance to Research Question |
|-----------------|-------------------|------------------------|-------------------------------|

### Conflict Analysis
[Any conflicts between tiers, with resolution per the 8 hierarchy rules]

### Gaps Identified
[Areas where authority is implied but not explicit, or where no authority exists]

### Explicit vs. Implied Powers
- **Explicit:** [powers directly cited in a specific provision]
- **Implied:** [powers reasoned from express grants per BOL Art. V, Sec. 3 general welfare clause]

### Search Record
[Keywords used, sources searched, tiers covered — for reproducibility and audit]
```

## 7-Tier BARMM Legal Hierarchy

The Bangsamoro legal system operates under a strict hierarchy. Higher tiers prevail over lower tiers in case of conflict.

| Tier | Source | Authority |
|------|--------|-----------|
| 1 | 1987 Philippine Constitution | Supreme law; Art. X creates autonomous regions |
| 2 | Bangsamoro Organic Law (RA 11054) | Organic act; defines BARMM powers and structure |
| 3 | Bangsamoro Administrative Code (BAA No. 13) | Organizational structure of the Bangsamoro Government |
| 4 | Other Bangsamoro Autonomy Acts | Sector-specific legislation enacted by Parliament |
| 5 | Applicable National Laws | National RAs that apply within BARMM |
| 6 | Executive Issuances | EOs, IRRs, MCs, AOs from CM or ministries |
| 7 | Jurisprudence | SC decisions interpreting BARMM authority |

**Conflict Resolution Rules:**
1. Constitution prevails over all
2. BOL prevails over all BAAs and national laws within BARMM exclusive powers
3. BOL Art. V, Sec. 2 exclusive powers — national law does NOT apply
4. BOL Art. V, Sec. 4 concurrent powers — national law applies suppletorily
5. BAA No. 13 organizes government; specific BAAs prevail over BAA 13 on their subject matter
6. Later BAA prevails over earlier BAA on the same subject (lex posterior)
7. Specific BAA prevails over general BAA on overlapping topics (lex specialis)
8. Executive issuances cannot exceed the authority granted by the BAA they implement

## Search Priority Order

For finding provision text in the legislative archive:

1. **Markdown transcriptions** (fastest):
   - `~/apps/transcriptions/legislation/BAAs/` — 89+ enacted BAAs (check INDEX.md first)
   - `~/apps/transcriptions/legislation/Bills/` — 414+ filed bills (check INDEX.md first)
   - `~/apps/transcriptions/legislation/Resolutions/` — 555+ adopted resolutions
   - `~/apps/transcriptions/legislation/national-laws/` — National laws
   - `~/apps/transcriptions/parliamentary/` — Parliamentary records

2. **BOL verbatim text**:
   - `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` — 5 chapter files

3. **Local PDFs** (via /transcriber):
   - `~/apps/transcriptions/source-pdfs/` — BAA PDFs, Resolution PDFs

4. **Web search** (last resort):
   - Official Gazette, LawPhil, Supreme Court E-Library
   - Always label: `[Source: web — verify against official copy]`

For detailed archive paths, read `references/search-strategy.md`.
For quick law lookups by name/number, read `references/law-index.md`.

## REFERENCE Mode — Legal Reference Research

**Invoke with:** `/legal-researcher REFERENCE [BOL power letter]` (e.g., `/legal-researcher REFERENCE k`)

**Purpose:** Produce a comprehensive Legal Reference Research Memorandum for one of the 55 BOL Art. V, Sec. 2 powers. This is a specialized research mode that feeds into `/legal-assistant REFERENCE` for document production.

**Input:** A BOL power letter (a through ccc) or power name (e.g., "cooperatives")

**MANDATORY: Before starting, read these two files:**
- `~/apps/transcriptions/legal-references/TEMPLATE.md` — the authoritative template defining the output structure (9 themes A-I, Legal Sources tables, institutional validation, redundancy rules)
- `~/apps/transcriptions/legal-references/11-k-cooperatives/legal-reference-cooperatives.md` — the gold standard example

**Process:**

1. **Identify the power** — read `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/01-articles-I-to-V.md` to find the verbatim Art. V, Sec. 2 text
2. **Scan ALL BOL provisions** — read all 6 BOL chapter files, extract every provision that elaborates, limits, or implements this power (not just the obvious article)
3. **Identify constitutional provisions** — which Art. III (Bill of Rights), Art. X (Autonomous Regions), Art. XII (Economy), Art. XIII (Social Justice), Art. XIV (Education) provisions apply? What is the constitutional floor?
4. **Scan BAA 13** — read the actual BAA 13 sections for the lead ministry/office. MANDATORY: read from `legislation/baas/BAA-13.md`, enumerate ALL functions verbatim
5. **Scan ALL 89+ BAAs** — check every BAA against this power area using `legal-references/_data/baa-power-map.md`
6. **Scan national laws** — MANDATORY: search `legislation/national-laws/INDEX.md` by keywords (not just obvious laws). Search `legislation/executive-orders/INDEX.md` for EOs. Check PD 1083 for Shari'ah relevance
7. **Search jurisprudence** — search `jurisprudence/INDEX.md` for SC decisions relevant to this power
8. **Scan Shari'ah sources** — does this power have a Shari'ah dimension? What Islamic legal principles apply?
9. **Identify pending PBs** — search `legislation/bills/proposed/INDEX.md` and `legislation/bills/enacted/INDEX.md` for filed bills
10. **Identify resolutions** — search `legislation/resolutions/enacted/INDEX.md` for relevant resolutions
11. **Map to BDP + Matatag** — identify BDP 2023-2028 chapter and Mas Matatag pillar connections
12. **Identify national government implementation** — what national agencies exercise authority? What ARMM-era devolution EOs exist?
13. **Institutional validation** — validate the lead MOA assignment: does the BAA 13 mandate actually cover the FULL scope of this power? List ALL existing BARMM institutions (lead, supporting, commissions, Shari'ah, LGU-level). Identify BOL-mandated institutions that haven't been created. Assess whether NEW institutions are needed beyond what the BOL names.

**Output:** Legal Reference Research Memorandum — structured data for each section of the legal reference template:

```markdown
## Legal Reference Research Memorandum: ({letter}) [Power Name]

### BOL Provisions Found
| Provision | Verbatim Text | Relationship |
[All provisions across 18 articles]

### Constitutional Provisions
| Article | Provision | Constitutional Floor? |
[All applicable constitutional provisions]

### BAA 13 Mandate (Verbatim)
[Full enumeration of ministry functions from BAA 13]

### Implementing BAAs
| BAA | PB No. | Title | Relevance |
[All relevant BAAs]

### National Laws
| Law | Title | Relationship | Application in BARMM |
[ALL found — from INDEX scan, not just obvious]

### Executive Orders
| EO | Title | Relevance |
[All relevant EOs — especially ARMM devolution EOs]

### Shari'ah Sources
| Source | Principle | Application |
[PD 1083, Art. X Sec. 4, Islamic principles]

### Jurisprudence
| Case | Date | Holding | Impact |
[SC decisions found]

### Parliamentary Resolutions
| Resolution | PR No. | Title | Relevance |

### Pending Parliament Bills
| PB No. | Title | Relevance | Status |

### Development Alignment
| Framework | Reference | Connection |

### National Government Implementation
[National agencies, programs, devolution status]

### Institutional Validation
| Institution | Creating Law | Operational? | Role for This Power |
[ALL existing BARMM institutions — lead, supporting, commissions, Shari'ah, LGU-level]

**Lead MOA Assessment:** [Is the assigned lead MOA correct? Does its BAA 13 mandate cover the FULL scope?]
**BOL-mandated institutions not yet created:** [List with BOL provision]
**New institutions needed:** [Beyond BOL mandates — regulatory bodies, tribunals, coordination mechanisms]

### Research Notes
[Search terms used, INDEX lines scanned, what was NOT found]
```

**CRITICAL RULES for REFERENCE mode:**
- Read the ACTUAL source files — NEVER summarize from memory
- Scan the FULL INDEX files (11,866 RAs + 2,572 EOs) — not just "obvious" laws
- The cooperatives example found 17 national laws vs. 5 originally — prove you scanned thoroughly
- No "Exclusive/Shared/Concurrent" — use only BOL terminology
- Record search terms and INDEX line numbers in Research Notes for verification

**Pipeline:** This memorandum feeds directly into `/legal-assistant REFERENCE` which produces the final legal reference document.

---

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

**Invocation patterns:**
- `/legal-assistant` invokes `/legal-researcher` FIRST → drafts document → invokes `/legal-reviewer ACCURACY` (Legal QA Loop) → invokes `/fact-checker`
- `/legal-reviewer` invokes `/legal-researcher` when it needs source text to verify a quoted provision (ACCURACY mode) or to research authorities for AUTHORITY/SUFFICIENCY assessment
- `/legal-researcher` does NOT invoke the other two — it is the foundation layer. It invokes `/bangsamoro` for governance context and `/transcriber` for PDF extraction.
- `/legislative-briefer` and `/resolution-drafter` invoke `/legal-researcher` directly (they do their own writing, bypassing `/legal-assistant`)
- `/bill-drafter` invokes both `/legal-researcher` (for research) AND `/legal-assistant BASIS` (for the legal basis section)

**Typical workflow (when /legal-assistant is the final product):**
1. `/legal-researcher` → 4-step research → Research Memorandum
2. `/legal-assistant` → drafts document using IRAC + verbatim provisions
3. `/legal-reviewer ACCURACY` → Legal QA Loop (iterate until 0 critical/significant errors)
4. `/fact-checker` → final verification
5. Deliver

**Typical workflow (when a specialized skill is the final product):**
1. `/legal-researcher` → Research Memorandum
2. Specialized skill (`/bill-drafter`, `/legislative-briefer`, `/resolution-drafter`) → produces its document
3. `/legal-reviewer ACCURACY` → Legal QA Loop
4. `/fact-checker` → final verification
5. Deliver

**When invoked standalone:**
- `/legal-researcher` alone: answers "what law applies?" → returns a Research Memorandum
- No QA loop needed on research memoranda — they contain only source text, not drafted claims

## Skill Composition

- **/bangsamoro** — BARMM governance context, agency hierarchy, BOL key provisions
- **/transcriber** — Extract text from PDFs when markdown transcriptions unavailable

**Called by:** /legal-assistant, /legal-reviewer, /bill-drafter, /legislative-briefer, /resolution-drafter, /policy-recommendation, /fact-checker

## What This Skill Does NOT Do

- Legal analysis or interpretation → use `/legal-assistant`
- Legal document review (accuracy, compliance, sufficiency) → use `/legal-reviewer`
- Citation formatting → use `/citation`
- Fact-checking names, dates, numbers → use `/fact-checker`

## Error Handling

| Situation | Action |
|-----------|--------|
| Provision not found in any local source | Search web. Label as `[Source: web]`. Recommend verification. |
| Ambiguous citation (multiple laws match) | Present all matches. Ask user to clarify. |
| Law appears repealed or superseded | Flag both original and superseding law. Note which is current. |
| PDF needed but /transcriber unavailable | Note path, suggest user invoke /transcriber. |
| Tier 7 (jurisprudence) — cannot verify G.R. number | Note as `[UNVERIFIED — confirm G.R. number against SC database]`. |

## Gotchas

- BOL article numbers are the #1 fabrication target — always verify against ~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/
- BAA numbers are the #2 fabrication target — verify against ~/Vault/bangsamoro/bangsamoro-laws/index.md
- Use BARMM ministry abbreviations (MFBM not DBM, MOLE not DOLE, MBHTE not DepEd, MILG not DILG) — never national equivalents
- Mas Matatag na Bangsamoro Agenda (2026-2028) replaces 12-Point Priority Agenda — update all references
- Never cite guidebooks as primary sources — trace back to enacted law (BAA, RA, BOL)
- A wrong BAA number, BOL article, or official title is 3x worse than writing [UNVERIFIED]. When in doubt, mark it.
- The 7-Tier legal hierarchy is: Constitution > BOL > BAAs > National Laws (consistent with BOL) > BTA Resolutions > Executive Orders > Implementing Rules
- Always check if a national RA has been superseded by a BAA in BARMM jurisdiction
- Jurisprudence search must include SC decisions on Bangsamoro autonomy (GR cases in ~/apps/transcriptions/jurisprudence/)

## Subagent Honesty Rules

Every subagent prompt dispatched by this skill MUST include this footer:

> HONESTY RULES:
> 1. Only extract values explicitly stated in source documents. If ambiguous or missing, leave blank with a one-line reason.
> 2. A wrong answer is 3x worse than a blank answer. When in doubt, leave it blank.
> 3. Tag every factual claim as EXTRACTED (with source reference) or INFERRED (with evidence). Inferred claims will be verified first.

## Examples

### Complete Worked Example: "What is OOBC's legal mandate?"

This example is drawn from a real case during the Strategic Planning Guidebook project, where a flat keyword search missed the provision chains that define OOBC's actual scope.

---

**Step 1 — Issue Analysis:**
- Question: What laws authorize the Office for Other Bangsamoro Communities (OOBC) to exist and operate, and what is the scope of its mandate?
- Jurisdiction: BARMM
- Subject matter: mandate of OOBC, legal basis for its creation, scope of "other Bangsamoro communities"
- Search terms: "other Bangsamoro communities", "OOBC", "Bangsamoro people", "rights of the Bangsamoro", "non-Moro indigenous peoples"
- Relevant tiers: Tier 2 (BOL), Tier 3 (BAA 13), Tier 5 (national laws)

**Step 2 — Secondary Sources:**
- /bangsamoro context: OOBC is an attached office under the Office of the Chief Minister (OCM), serving communities in the Bangsamoro that are not part of the majority Moro population
- BDP 2023-2028: Chapter 5 (Social Development) references inclusive development for all Bangsamoro peoples
- Institutional relationship: OOBC sits within OCM per BAA 13 organizational structure

**Step 3 — Primary Sources:**
- Tier 2: BOL Art. VI, Sec. 12 — "The Bangsamoro Government shall ensure the protection of the rights of the Bangsamoro people, including non-Moro indigenous peoples and other inhabitants of the Bangsamoro"
- Tier 2: BOL Art. V, Sec. 2(a) — administrative organization as an enumerated power
- Tier 2: BOL Art. V, Sec. 3 — general welfare clause (implied powers)
- Tier 3: BAA No. 13, Book IV, Title III, Secs. 5-6 — establishment and functions of OOBC under OCM
- Tier 4: BAA No. 38 (procurement), BAA No. 84 (budget) — cross-cutting operational authorities
- Tier 5: RA 8371 (IPRA) — indigenous peoples' rights (national law, suppletory)

**Step 4 — Provision Chain Trace:**

Starting from BOL Art. VI, Sec. 12, the provision references "rights of the Bangsamoro people" — this is a traceable concept.

*Full-source scan conducted*: Read all 5 BOL chapter files to trace every provision that defines, enumerates, or limits these rights.

| Source Provision | Traceable Concept | Related Provisions Found | Relevance to Research Question |
|-----------------|-------------------|------------------------|-------------------------------|
| BOL Art. VI, Sec. 12 | "rights of the Bangsamoro people" | BOL Art. IX, Secs. 1-14 (Basic Rights — enumerates 14 rights including identity, political participation, ancestral domain) | Defines the scope of what OOBC must protect — these are the specific rights |
| BOL Art. VI, Sec. 12 | "Bangsamoro people" | BOL Art. II, Sec. 1 (Definition — those who at the time of conquest were considered natives or original inhabitants) | Establishes who OOBC serves — the defined population |
| BOL Art. VI, Sec. 12 | "non-Moro indigenous peoples" | BOL Art. X (Indigenous Peoples' Rights in BARMM) | OOBC mandate extends to non-Moro IPs; Art. X defines their specific protections |
| BOL Art. IX, Sec. 3 | "right to meaningful political participation" | 1987 Constitution Art. II, Sec. 1 (Sovereignty); Art. X, Sec. 18 (Autonomous region composition) | Constitutional grounding for OOBC's inclusion mandate |
| BOL Art. X | "indigenous peoples" | RA 8371 (IPRA), Secs. 2-3 (Definition and scope of IP rights at national level) | National law that operates suppletorily within BARMM for IP rights not covered by BOL |
| BAA 13, Book IV, Sec. 5 | "functions and mandates" of OOBC | BAA 13, Book IV, Sec. 6 (Specific enumeration of OOBC functions) | The operational mandate — what OOBC actually does day-to-day |

*Without chain tracing, the research would have stopped at Art. VI, Sec. 12 — missing the 14 enumerated rights in Art. IX, the definition in Art. II, and the IP-specific protections in Art. X that together define the actual scope of OOBC's work.*

**Step 4 — Verification:**
- All cited BOL provisions: In force (BOL has not been amended)
- BAA 13: In force as the current Administrative Code
- RA 8371: In force nationally; applies suppletorily in BARMM
- Verbatim text confirmed by reading source files (not quoted from memory)
- Actor verification: Art. VI, Sec. 12 assigns the duty to "Bangsamoro Government" (not National Government)

**Output — Condensed Research Memorandum:**

```
## Legal Research Memorandum

**Question:** What is the legal basis and scope of OOBC's mandate?
**Jurisdiction:** BARMM
**Date:** 2026-03-28

### Applicable Authorities

| # | Tier | Source | Provision | Authority/Mandate | Status |
|---|------|--------|-----------|-------------------|--------|
| 1 | 2 | BOL (RA 11054) | Art. VI, Sec. 12 | Duty to protect rights of all Bangsamoro peoples including non-Moro IPs | In force |
| 2 | 2 | BOL (RA 11054) | Art. II, Sec. 1 | Definition of "Bangsamoro people" — scope of OOBC's constituency | In force |
| 3 | 2 | BOL (RA 11054) | Art. IX, Secs. 1-14 | 14 enumerated Basic Rights — defines what OOBC protects | In force |
| 4 | 2 | BOL (RA 11054) | Art. X | IP-specific rights within BARMM | In force |
| 5 | 2 | BOL (RA 11054) | Art. V, Sec. 2(a) | Administrative organization power | In force |
| 6 | 3 | BAA No. 13 | Book IV, Title III, Secs. 5-6 | OOBC creation, functions, organizational placement under OCM | In force |
| 7 | 5 | RA 8371 (IPRA) | Secs. 2-3 | National IP rights framework (suppletory) | In force |

### Key Provisions (Verbatim)

**BOL Art. VI, Sec. 12:**
> "The Bangsamoro Government shall ensure the protection of the rights of the Bangsamoro people, including non-Moro indigenous peoples and other inhabitants of the Bangsamoro."
— Source: ~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/

### Provision Chain Map

| Source Provision | Traceable Concept | Related Provisions Found | Relevance |
|-----------------|-------------------|------------------------|-----------|
| Art. VI, Sec. 12 | "rights of the Bangsamoro people" | Art. IX, Secs. 1-14 | Defines scope of protection duty |
| Art. VI, Sec. 12 | "Bangsamoro people" | Art. II, Sec. 1 | Defines constituency |
| Art. VI, Sec. 12 | "non-Moro indigenous peoples" | Art. X; RA 8371 | IP-specific protections |
| Art. IX, Sec. 3 | "political participation" | Const. Art. II, Sec. 1 | Constitutional basis for inclusion |

### Gaps Identified
- No standalone BAA creating OOBC as an independent office — authority derives from BAA 13 organizational provisions
- No BAA specifically operationalizing Art. X (IP rights within BARMM) — potential legislative gap

### Explicit vs. Implied Powers
- **Explicit:** Protection of rights (Art. VI, Sec. 12); OOBC functions (BAA 13, Book IV, Secs. 5-6)
- **Implied:** Coordination with NCIP on overlapping IP matters (from Art. V, Sec. 3 general welfare clause)

### Search Record
Keywords: "other Bangsamoro communities", "OOBC", "non-Moro indigenous", "Bangsamoro people definition", "basic rights"
Sources: BOL (5 chapter files), BAA 13, BAA index, RA 8371
Tiers covered: 1 (Constitution), 2 (BOL), 3 (BAA 13), 4 (other BAAs), 5 (national laws)
Provision chains traced: 4 chains from Art. VI, Sec. 12 starting provision
```
