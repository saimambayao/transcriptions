---
name: deep-research
description: "Multi-phase deep research agent with multi-source validation and confidence-classified claims. Use when conducting thorough research on ANY topic — cooperative development, policy analysis, technology evaluations, market research, regulatory compliance, RA 9520, or any question requiring authoritative sources with citations. Triggers on 'research this', 'find out about', 'investigate', 'what does the evidence say', 'comprehensive analysis of', or any request needing multiple verified sources. Incorporates orchestrator-worker architecture, agentic RAG search, contradiction detection, and iterative self-correction patterns from Gemini/Gemini/OpenAI deep research agents. Produces citation-rich reports with confidence scores and Works Cited lists."
argument-hint: "[research topic]"
allowed-tools:
  - Agent
  - WebSearch
  - WebFetch
  - Read
  - Write
  - Bash
  - Glob
  - Grep
---

# Deep Research Skill

Multi-phase research agent that produces authoritative, confidence-classified research briefs with full citation trails.

This skill orchestrates parallel research agents to produce citation-rich, confidence-classified research briefs on any topic.

## When to Use This vs. Other Research Skills

| Situation | Use | Why |
|---|---|---|
| Need to **find** sources on a topic (no sources in hand) | **This skill** | Spawns researchers to search web + local archives |
| BARMM legal question (BOL, BAA, constitutional analysis) | **This skill** (BARMM Legal route) | Domain routing hits local files + legal pipeline |
| Have **existing sources** (PDFs, URLs) to analyze | `/research-pipeline` | Uploads to NotebookLM (free) — Claude only fills gaps |
| Summarize a long document (200+ pages) | `/research-pipeline` | NotebookLM handles heavy reading for free |
| Specific legal document (memo, opinion, matrix) | `/legal-assistant` directly | Skip research orchestration; use the legal pipeline |
| Quick fact-check, not full research | `/fact-checker` | Lighter weight, no research phase needed |

**Simple rule:** No sources in hand → `/deep-research`. Sources in hand → `/research-pipeline`. Legal document needed → `/legal-assistant`.

## Agent Teams Architecture

**Preferred:** `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS: "1"` in `.claude/settings.local.json`

**Single-agent fallback:** If Agent Teams is not enabled, run all phases sequentially
in the main context. Replace parallel researcher spawns with sequential web searches
(Phase 1), skip parallel reviewers and self-review instead (Phase 3). Output quality
is comparable but slower. The skill works either way — Agent Teams just enables parallelism

```
┌──────────────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR (Lead Agent)                      │
│  Phase 0: Plan · Phase 1: Spawn · Phase 2: Synthesize           │
│  Phase 3: Validate · Phase 4: Correct · Produce final output    │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  PHASE 1: PARALLEL RESEARCH     PHASE 3: PARALLEL VALIDATION     │
│  ┌──────────────────────┐       ┌──────────────────────────┐     │
│  │ Researcher A          │       │ Technical Reviewer       │     │
│  │ (sub-tasks 1-2)       │       │ (citations, confidence)  │     │
│  ├──────────────────────┤       ├──────────────────────────┤     │
│  │ Researcher B          │       │ Accuracy Reviewer        │     │
│  │ (sub-tasks 3-4)       │       │ (facts, contradictions)  │     │
│  ├──────────────────────┤       ├──────────────────────────┤     │
│  │ Researcher C          │       │ Styling Reviewer         │     │
│  │ (sub-tasks 5-6)       │       │ (format, citations)      │     │
│  └──────────────────────┘       └──────────────────────────┘     │
│  3-layer search → shut down      Review in parallel → report     │
└──────────────────────────────────────────────────────────────────┘
```

### Researcher Scaling

| Topic Complexity | Sub-tasks | Researchers | Query Target | Estimated Time |
|-----------------|-----------|-------------|--------------|----------------|
| Focused (1-2 domains) | 2-3 | 1-2 | 20-40 queries | 3-5 min |
| Standard (3-4 domains) | 4-5 | 3-4 | 40-80 queries | 5-15 min |
| Comprehensive (5+ domains) | 6-7 | 5+ | 80-160 queries | 15-30 min |

### Tools

| Tool | Purpose | Used By |
|------|---------|---------|
| **WebSearch** | Broad exploration, finding sources | Researchers |
| **WebFetch** | Deep dive into specific sources | Researchers |
| **Read** | Local file awareness | Orchestrator |

---

## 5-Phase Architecture

| Phase | Name | Actor | Purpose |
|-------|------|-------|---------|
| **0** | Research Planning | Orchestrator + user | Decompose query, build DAG, present plan |
| **1** | Parallel Research | Researchers (spawned) | Adaptive 3-layer search with source tracking |
| **2** | Synthesis & Contradiction Detection | Orchestrator | Consolidate, cross-reference, classify claims |
| **3** | Multi-Agent Validation | Reviewers (spawned) | Verify facts, check citations, resolve contradictions |
| **4** | Self-Correction & Refinement | Orchestrator | Apply fixes, run quality checklist, produce final output |

---

## Phase 0: Research Planning

Decompose the query into a reviewable research plan before execution.

### 0.0 Domain Detection and Routing

Before decomposing the query, identify which domain it falls into. This determines the research strategy — web-first vs. local-first — and which specialized skills to invoke.

| Domain Signal | Route | Why |
|---|---|---|
| Mentions BOL, BAA, BARMM, Bangsamoro, Shari'ah, Parliament, BTA, enumerated powers, constitutional floor | **BARMM Legal** | Local archives have 11,866 RAs, 89 BAAs, 38,857 SC decisions, verbatim BOL. Web search is slower and less reliable. |
| Mentions Philippine law, RA, Republic Act, Supreme Court, Constitution, LGC | **Philippine Legal** | Local national laws archive + jurisprudence archive. |
| Any other topic | **General** (default) | Standard web-first 3-layer search. |

**BARMM Legal route — Local-First Research Pipeline:**

When the domain is BARMM Legal, replace the standard 3-layer web search with the legal skills pipeline:

```
Phase 0: /prompter → refine the legal question
Phase 1: /legal-researcher → 5-step methodology against LOCAL sources:
         - BOL: ~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/
         - BAAs: ~/Vault/bangsamoro/bangsamoro-laws/index.md + BAA-*.md files
         - National laws: legislation/national-laws/INDEX.md (11,866 RAs)
         - Jurisprudence: jurisprudence/ (38,857 SC decisions)
         - Executive orders: legislation/executive-orders/
         Web search ONLY for: recent SC decisions not yet in archive, pending bills, current events
Phase 2: /legal-assistant → produce the analysis document (MEMO, CONSTITUTIONAL, DIVERGENCE, etc.)
Phase 3: /legal-reviewer → verify accuracy, compliance, sufficiency
Phase 4: /fact-checker → P0-P10 + IC-1 through IC-5 integrity checks
```

**Token savings:** ~80% reduction for BARMM legal questions. Local file reads cost ~0 vs. web search + fetch cycles.

**Subagent standards for legal route:** Every subagent dispatched for BARMM legal work MUST include:
1. The source-preload-protocol (`~/.gemini/skills/fact-checker/references/source-preload-protocol.md`)
2. The 5-layer constitutional constraint framework (constitutional rights → BOL "shall prevail" → BOL minimum standards → institutional retention → "shall not diminish")
3. The BOL conformity provision check — scan the specific BOL article for "conform to," "consistent with," "shall prevail," "shall not diminish," or institutional jurisdiction retention BEFORE stating what BARMM can or cannot do
4. The honesty rules (EXTRACTED/INFERRED tagging)
5. File paths to local authoritative sources (BOL, BAA index, national laws INDEX)

**Philippine Legal route:** Same as BARMM Legal but without the BOL-specific checks. Use the national laws and jurisprudence archives directly.

**General route:** Standard web-first 3-layer search (the existing Phase 1 workflow).

### 0.1 Query Decomposition

Break the research topic into 4-7 sub-tasks structured as a DAG:
```
Sub-task 1: [Foundation question] — no dependencies
Sub-task 2: [Regulatory context] — no dependencies
Sub-task 3: [Industry practices] — depends on 1
Sub-task 4: [Case studies] — depends on 1, 3
Sub-task 5: [Comparative analysis] — depends on 2, 3
...
```

Identify which sub-tasks can run in parallel vs. which require sequential execution. Parallelizing independent sub-tasks cuts research time by 3-5x.

### 0.2 Source Domain Selection

Select trusted source domains relevant to the topic:
- Government/regulatory sites
- Academic databases
- Industry bodies
- Known authoritative publishers

See [references/architecture-patterns.md](references/architecture-patterns.md) for DAG decomposition patterns.

### 0.3 Present Plan to User

Present the research plan (sub-tasks, estimated scope, source strategy) for user review. Proceed after confirmation or incorporate their refinements.

---

## Phase 1: Parallel Research

Spawn N researchers based on the scaling table. Each researcher operates independently on assigned sub-tasks.

Apply the **adaptive 3-layer search strategy** per researcher:
1. **Broad Exploration** -- Map the landscape, identify key sources and terminology (3-5 searches)
2. **Targeted Deep Dive** -- Extract specific facts from authoritative sources (5-10 searches + fetches)
3. **Verification & Gap-Filling** -- Verify claims, fill gaps, resolve contradictions (2-5 searches)

This 3-layer approach matters because naive single-pass search misses 35-50% of relevant sources.

See [references/agentic-rag-search.md](references/agentic-rag-search.md) for full search strategy, query rewriting, and multi-granularity retrieval.

### Error Handling

- **Bounded retries**: 2-3 attempts on transient failures (timeouts, rate limits)
- **Fallback chain**: Rewrite query -> alternative source domains -> note gap and proceed
- **Graceful degradation**: Partial results logged before failure; orchestrator redistributes failed sub-tasks

See [references/architecture-patterns.md](references/architecture-patterns.md) for error classification and fallback strategy chain.

### Researcher Output

Require each researcher to return:
1. **Key Findings** with inline citations [N] and **confidence classifications** [S]/[P]/[?]/[U]
2. **Source Log** table (ID | URL | Type | Key Claims | Confidence)
3. **Works Cited** list ([N] Author. "Title." Source, Year. URL)
4. **Contradictions noted** (if any claims conflict across sources)

See [references/researcher-spawn-prompts.md](references/researcher-spawn-prompts.md) for full prompt template.

Source priority order:
1. **Local authoritative files** (fastest, zero-cost, most reliable):
   - BOL verbatim: `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` (6 chapter files)
   - BAA index + full text: `~/Vault/bangsamoro/bangsamoro-laws/index.md` + `BAA-*.md`
   - National laws: `legislation/national-laws/INDEX.md` (11,866 RAs)
   - Executive orders: `legislation/executive-orders/` (2,572 EOs)
   - Jurisprudence: `jurisprudence/` (38,857 SC decisions)
   - BDP 2023-2028: `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/`
   - BARMM officials: `~/.gemini/skills/bangsamoro/references/barmm-officials-2025-2026.md`
2. Official government/regulatory websites (when local archive is insufficient)
3. Academic papers and frameworks
4. Industry reports and standards
5. Case studies and practical examples

**Local-first rule:** For BARMM and Philippine legal questions, exhaust local sources BEFORE any web search. A Grep on `legislation/national-laws/INDEX.md` finds an RA in milliseconds; a web search takes seconds and may return outdated text.

---

## Phase 2: Synthesis & Contradiction Detection

Consolidate findings, cross-reference claims, and classify confidence levels.

See [references/confidence-classification.md](references/confidence-classification.md) for full classification methodology.

### 2.1 Consolidate Findings

Group extracted facts by sub-task and merge overlapping claims from different sources.

### 2.2 Verification Matrix

Build a cross-reference for each major claim:
```
| Claim | Source IDs | Agreement | Classification |
|-------|-----------|-----------|----------------|
| [claim] | 1, 3, 5 | All agree | SUPPORTED |
| [claim] | 2 | Single source | UNCERTAIN |
| [claim] | 1 vs 4 | Conflict | Flag for Phase 3 |
```

### 2.3 Claim Classification

Classify every claim using one of four levels:

| Level | Tag | Criteria |
|-------|-----|----------|
| **Supported** | `[S]` | 2+ independent sources agree |
| **Probable** | `[P]` | 1 strong source, or 2+ with minor discrepancies |
| **Uncertain** | `[?]` | Single non-authoritative source, or conflicting data |
| **Unsupported** | `[U]` | No reliable source, or all sources conflict |

Tag every claim visibly -- readers need to know claim reliability at a glance.

### 2.4 Generate Draft Research Brief

Produce an initial draft with inline citations and confidence tags. Flag all contradictions for Phase 3 resolution. The real value of multi-source research is finding where sources disagree, not just where they agree -- surface every conflict explicitly.

---

## Phase 3: Multi-Agent Validation

Spawn three reviewers in parallel, each checking a different dimension.

| Reviewer | Focus | Key Additions |
|----------|-------|---------------|
| **Technical Reviewer** | Citation quality, source authority | Verify confidence classifications [S]/[P]/[?]/[U] are justified |
| **Accuracy Reviewer** | Fact/date/number verification | Verify contradiction resolutions are correct |
| **Styling Reviewer** | Markdown structure, citation format | Verify confidence summary header is present and accurate |

Require each reviewer to return a structured report with flags and suggested fixes.

See [references/reviewer-spawn-prompts.md](references/reviewer-spawn-prompts.md) for full prompts and checklists.

---

## Phase 4: Self-Correction & Refinement

Apply corrections, run quality checks, and produce the final output.

### 4.1 Apply Corrections

- Update factual errors from Phase 3
- Fix broken or inaccurate citations
- Resolve or annotate contradictions
- Remove unsupported claims or mark them explicitly
- Only retain changes that improve accuracy (do not introduce new errors)

### 4.2 Quality Gate

The final brief represents the skill's credibility -- every weak citation or untagged claim undermines trust in the entire output. Before declaring the brief complete, verify these dimensions:

- **Content completeness**: Confirm every Phase 0 sub-task is addressed and all recommendations trace back to evidence. Flag any remaining unsupported claims with `[U]`.
- **Citation integrity**: Ensure every claim carries an inline citation `[1]`, the Works Cited list is complete with sequential numbering, and all URLs resolve.
- **Source strength**: Prioritize authoritative sources (government, academic, industry), prefer recent publications (within 2-3 years for current topics), and include page/section numbers where possible.
- **Cross-check**: Walk through the verification matrix one final time -- no claim should lack a confidence tag.

### 4.3 Fact-Check

Before delivering the final output, run `/fact-checker` on the research brief. Research briefs
are high-risk for factual errors — hallucinated citations, wrong names, fabricated statistics.
The fact-checker verifies all names, titles, dates, numbers, legislation references, and
organizations against authoritative sources and produces a verification report.

### 4.4 Final Output

Save to `~/Vault/research/deep-research/yymmdd-topic-name.md`

> **Token-efficient alternative:** For research on specific sources (YouTube, PDFs, web URLs),
> prefer `/research-pipeline` which offloads heavy analysis to NotebookLM (free) and uses
> ~80% fewer tokens. Use `/deep-research` when you need broad web exploration, maximum rigor,
> or legal/compliance/academic research requiring 40+ search queries.

```markdown
# Research Brief: [Topic]

> **Research Date**: [Date] | **Validated**: Yes
> **Method**: Agent Teams (Orchestrator + [N] Researchers + 3 Reviewers)
> **Confidence**: X claims [S], Y claims [P], Z claims [?], W claims [U]
> **Contradictions**: N identified, M resolved, K flagged for review
> **Sources**: N total | Government: X | Academic: Y | Industry: Z

## Executive Summary
[2-3 paragraph overview with key confidence notes]

## Research Questions
[Numbered list from Phase 0 sub-tasks]

## Key Findings
[Organized sections with inline citations and confidence tags]

### [Section 1]
- Finding [S].[1]
- Finding [P].[2, 3]

### [Section 2]
- Finding [S].[4, 5]

## Recommendations
[Evidence-based recommendations with citations]

## Source Log
| ID | Type | URL | Key Claims |
|----|------|-----|------------|
| 1 | Official | [url] | [claims] |
| 2 | Academic | [url] | [claims] |

## Works Cited
[1] Author. "Title." Source, Year. URL
[2] ...

---
*Research validated using 5-phase Agent Teams methodology*
*Reviewed by: Technical Reviewer, Accuracy Reviewer, Styling Reviewer*
```

---

## Citation Standards

Use inline footnote citations with a Works Cited list -- this makes claims traceable and lets readers verify sources quickly.

See [references/citation-standards.md](references/citation-standards.md) for complete standards.

**Quick Reference:**

| Element | Format |
|---------|--------|
| Inline | `claim.[1]` or `claim.[1, 2]` |
| Page ref | `claim.[1, p. 5]` |
| Works Cited | `[1] Author. "Title." Source, Year. URL` |

---

## References

| Reference | Purpose |
|-----------|---------|
| [architecture-patterns.md](references/architecture-patterns.md) | Orchestrator-worker patterns, DAG decomposition, error handling |
| [agentic-rag-search.md](references/agentic-rag-search.md) | Adaptive 3-layer search strategy, query rewriting |
| [confidence-classification.md](references/confidence-classification.md) | Claim classification, contradiction detection & resolution |
| [researcher-spawn-prompts.md](references/researcher-spawn-prompts.md) | Researcher prompt templates |
| [reviewer-spawn-prompts.md](references/reviewer-spawn-prompts.md) | Reviewer prompt templates + final output format |
| [search-query-library.md](references/search-query-library.md) | Domain-specific search query templates |
| [trusted-sources.md](references/trusted-sources.md) | Authoritative source domains by category |
| [validation-methodology.md](references/validation-methodology.md) | Detailed validation procedures |

---

## Quick Start

```
0. PLAN (Orchestrator) -- Decompose into 4-7 sub-tasks (DAG), select trusted sources, present plan for user approval
1. RESEARCH (Researchers, Phase 1) -- Each uses 3-layer search (Broad -> Targeted -> Verification), classifies claim confidence, returns Findings + Source Log + Works Cited
2. SYNTHESIZE (Orchestrator, Phase 2) -- Merge by theme, cross-reference claims, detect contradictions, classify all claims [S]/[P]/[?]/[U], draft brief with confidence header
3. VALIDATE (3 Reviewers, Phase 3, parallel) -- Technical (citations + confidence), Accuracy (facts + contradictions), Styling (format + header)
4. CORRECT (Orchestrator, Phase 4) -- Apply corrections (retain only improvements), re-verify confidence summary, save final output to ~/Vault/research/deep-research/
```

## Gotchas

- Multi-phase research must validate sources across phases — a claim accepted in Phase 1 can be disproven in Phase 2
- Confidence classification (HIGH/MEDIUM/LOW) must be based on source quality, not model certainty
- When researching BARMM topics, always load local authoritative sources before web searching
- BOL article numbers are the #1 fabrication target — always verify against ~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/
- BAA numbers are the #2 fabrication target — verify against ~/Vault/bangsamoro/bangsamoro-laws/index.md
- Use BARMM ministry abbreviations (MFBM not DBM, MOLE not DOLE, MBHTE not DepEd, MILG not DILG) — never national equivalents
- Mas Matatag na Bangsamoro Agenda (2026-2028) replaces 12-Point Priority Agenda — update all references
- Never cite guidebooks as primary sources — trace back to enacted law (BAA, RA, BOL)
- A wrong BAA number, BOL article, or official title is 3x worse than writing [UNVERIFIED]. When in doubt, mark it.

## Subagent Honesty Rules

Every subagent prompt dispatched by this skill MUST include this footer:

> HONESTY RULES:
> 1. Only extract values explicitly stated in source documents. If ambiguous or missing, leave blank with a one-line reason.
> 2. A wrong answer is 3x worse than a blank answer. When in doubt, leave it blank.
> 3. Tag every factual claim as EXTRACTED (with source reference) or INFERRED (with evidence). Inferred claims will be verified first.

### Additional Rules for BARMM Legal Subagents

When domain routing (Phase 0.0) selects the BARMM Legal route, add these to every subagent prompt:

> BARMM LEGAL STANDARDS:
> 4. Read LOCAL SOURCE FILES before making any legal claim. BOL at ~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/. BAA index at ~/Vault/bangsamoro/bangsamoro-laws/index.md. National laws at legislation/national-laws/INDEX.md.
> 5. NEVER cite a BAA number without verifying against the index. BAA 25 is a hospital, not an Education Code. Any BAA > 89 does not exist.
> 6. NEVER cite a BOL article without checking the 18-article map. Art. IX = Basic Rights, Art. X = Justice System — adjacent numbers cause errors.
> 7. Before stating "BARMM can/cannot diverge from national law," CHECK the specific BOL article for conformity language: "conform to," "consistent with," "shall prevail," "shall not diminish." The constraint varies by power.
> 8. Use Feliciano 10th Ed. citation format. Use BARMM ministry abbreviations (MFBM not DBM, MOLE not DOLE).
> 9. Mark any claim not from a local source file as [UNVERIFIED]. Training data fabricates BAA numbers and fiqh terms.
