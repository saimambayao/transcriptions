---
name: research-pipeline
description: |
  Token-efficient research pipeline combining NotebookLM (free analysis) with sub-agent
  validation and Obsidian vault storage. Reduces token usage by ~80% compared to /deep-research
  by offloading heavy analysis to Google's servers. Use when user says "research pipeline",
  "research this efficiently", "deep research but cheaper", "analyze and validate",
  or wants thorough research without burning excessive tokens. Also trigger when user has
  multiple YouTube videos, PDFs, or web sources to analyze comprehensively.
  Prefer this over /deep-research for most research tasks.
allowed-tools: Read, Glob, Grep, Agent, Bash, Write
---

# Research Pipeline — Token-Efficient Deep Research

3-tier architecture: NotebookLM (free) → Sub-agent validation (cheap) → Lean synthesis.

Saves ~80% tokens vs /deep-research by offloading heavy analysis to Google's servers.

## When to Use This vs. Other Research Skills

| Situation | Use | Why |
|---|---|---|
| Have **existing sources** (PDFs, URLs, documents) to analyze | **This skill** | Upload to NotebookLM (free) — Claude only fills gaps |
| Summarize a **long document** (200+ page BDP, guidebook, report) | **This skill** | NotebookLM handles heavy reading for free |
| User provides **specific files** to research from | **This skill** | Source-first analysis, not exploration |
| Need to **find** sources (no sources in hand) | `/deep-research` | It spawns researchers to search web + local archives |
| BARMM **legal question** (BOL, BAA, constitutional analysis) | `/deep-research` (BARMM Legal route) | Routes to local files + legal pipeline |
| Specific **legal document** needed (memo, opinion, matrix) | `/legal-assistant` directly | Skip research orchestration entirely |
| Quick **fact-check**, not full research | `/fact-checker` | Lighter weight, no research phase |

**Simple rule:** Sources in hand → this skill. No sources → `/deep-research`. Legal document → `/legal-assistant`.

## Architecture

```
Tier 1: NotebookLM (FREE)     → Ingest sources, initial analysis
Tier 2: Sub-agents (CHEAP)    → Validate claims, find gaps, check contradictions
Tier 3: Orchestrator (LEAN)   → Summaries only, final synthesis
```

## Process

### Phase 1: Research Prompt Architecture (Orchestrator — use /prompter)

Before sending anything to NotebookLM, architect a structured research brief. Vague prompts produce vague results.

1. Invoke `/prompter` to refine the user's research question into:
   - **3-5 specific sub-questions** to investigate
   - **Scope boundaries** — what to include and exclude
   - **Angles to cover** — technical, market, competitive, regulatory, etc.
   - **What a good answer looks like** — expected output shape

2. Present the structured research brief to the user for approval before proceeding.

3. Once approved, use this brief (not the original vague question) as the input to NotebookLM deep research in Phase 2.

This step is what separates useful research from generic summaries. Claude is the research strategist; NotebookLM is the research executor.

### Phase 2: Source Ingestion (NotebookLM — FREE)

This phase uses the `/notebooklm` skill's CLI commands. See that skill for full command reference.

1. **CREATE + USE + VERIFY** — Create a NotebookLM notebook and explicitly set it as active:
   ```bash
   # Create and capture UUID
   NOTEBOOK_ID=$(notebooklm create "Research: [Topic]" 2>/dev/null | grep -oE '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
   # Explicitly set active notebook (create does NOT do this reliably)
   notebooklm use "$NOTEBOOK_ID"
   # Verify correct notebook is active
   notebooklm metadata --json 2>/dev/null | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Active: {d[\"title\"]}')"
   ```
   **CRITICAL: `create` does NOT reliably set the active notebook.** Without `use`, all
   subsequent commands silently target the PREVIOUSLY active notebook.

2. **ALL subsequent NotebookLM commands MUST run in the SAME foreground session.**
   Background processes (`run_in_background: true`) do NOT inherit the active notebook —
   they will silently target the wrong notebook or fail.

3. Add specific sources FIRST (web URLs, PDFs, local files):
   ```bash
   notebooklm source add "URL or file"   # Add known sources one at a time
   ```
   Add 3-6 specific high-quality sources before running deep research.

4. Run NotebookLM deep research (LONG operation — 2-10 minutes):
   ```bash
   notebooklm source add-research "topic keywords" --mode deep --import-all
   ```
   **CRITICAL: Run in FOREGROUND with timeout 600000ms (10 min).** Known issues:
   - Background mode produces empty output (0 bytes) or fails silently
   - Background processes lose the active notebook context, importing into the wrong notebook
   - IMPORT_RESEARCH RPC can fail with `null result data` — retry with `research wait --import-all`
   Always use `--mode deep` unless user requests fast mode.

5. **VERIFY sources were added** before proceeding:
   ```bash
   notebooklm source list
   ```
   If source count is 0, the deep research failed. Retry or fall back to `/deep-research`.

6. Ask NotebookLM key research questions (save output to temp file):
   ```bash
   notebooklm ask "What are the key findings and arguments?" > /tmp/nlm-findings.md
   notebooklm ask "What contradictions or debates exist?" >> /tmp/nlm-findings.md
   notebooklm ask "What evidence supports the main claims?" >> /tmp/nlm-findings.md
   ```

7. Read the temp file — this is NotebookLM's analysis (already summarized, small token footprint).

**Fallback if NotebookLM fails:**

If NotebookLM auth fails, sources can't be added, or deep research returns empty:

1. **Auth failure** (`notebooklm login` needed): Tell the user to run `notebooklm login` in a
   separate terminal (it requires interactive browser auth that Gemini CLI cannot do).
   Wait for them to confirm, then retry. If still failing, fall back to Step 2 below.
2. **Fall back to sub-agent research**: Skip Phase 2 entirely. Instead, spawn 3 research
   sub-agents (using the Agent tool) that each take 1-2 sub-questions from Phase 1's brief
   and research via WebSearch + WebFetch. Each returns findings to a temp file. Continue
   to Phase 3 (Gap Analysis) using sub-agent outputs instead of NotebookLM outputs.
3. **Source add failures**: Verify with `notebooklm source list`. If sources are missing,
   try adding them one at a time. URL sources are more reliable than file uploads.
4. **Deep research returns 0 sources**: The `--import-all` flag silently fails in background
   mode. Re-run in foreground with `timeout: 600000`. If still empty, use option 2 above.

### Phase 3: Gap Analysis (Orchestrator — LEAN)

Read the NotebookLM analysis (already summarized — small token footprint). Identify:
- Claims that need independent verification
- Missing perspectives or counter-arguments
- Sources that need authority/recency checks
- Gaps in the analysis

Plan 2-4 targeted validation tasks for sub-agents.

### Phase 4: Parallel Validation (Sub-agents — ISOLATED CONTEXT)

Spawn sub-agents using the Agent tool. Each gets a specific, narrow task.

See [references/example-run.md](${GEMINI_SKILL_DIR}/references/example-run.md) for a
complete end-to-end example showing all 6 phases with concrete BARMM content.

**Required sub-agent output format** — each agent MUST structure output as:

```markdown
## Summary
[3-5 bullet findings — this is what the orchestrator reads]

## Evidence
[detailed sources, quotes, URLs — orchestrator skips this unless needed]
```

**Agent 1: Claim Verifier**
- Take the top 5-10 claims from NotebookLM's analysis
- Independently verify each via web search
- Return: verified/unverified status + supporting sources

**Agent 2: Counter-Argument Finder**
- Search for opposing viewpoints and contradictions
- Return: counter-arguments + sources that challenge the main findings

**Agent 3: Source Authority Checker**
- Evaluate the credibility and recency of key sources
- Return: source quality assessment + any outdated information flagged

Each sub-agent writes findings to a temp file. The orchestrator reads only the **Summary section** of each file — never the full Evidence output.

### Phase 5: Synthesis (Orchestrator — LEAN)

1. Read sub-agent summaries (not full outputs)
2. Combine NotebookLM analysis + validation findings
3. Classify claims with confidence levels:
   - **[S]** Supported — verified by multiple independent sources
   - **[P]** Probable — supported but not independently verified
   - **[?]** Uncertain — conflicting evidence or single source
   - **[U]** Unsupported — no verification found or contradicted
4. Produce the final research brief

### Phase 6: Output

Save to Obsidian vault:

1. **Full report** → `~/Vault/research/deep-research/yymmdd-topic-name.md`

```markdown
---
date: YYYY-MM-DD
tags: [research, deep-research, topic-tag]
source: [list of source URLs]
method: research-pipeline (NotebookLM + sub-agent validation)
---

# Research: [Topic]

> **Date**: YYYY-MM-DD | **Method**: NotebookLM + 3 validators
> **Confidence**: X [S], Y [P], Z [?], W [U]
> **Sources**: N analyzed

## Key Findings
- [claim with confidence tag and inline citation]

## Contradictions & Debates
- [conflicting viewpoints identified]

## Source Assessment
- [quality evaluation of key sources]

## Recommendations
- [actionable next steps]

## Works Cited
[1] Author. "Title." Source, Year. URL
```

2. **Condensed takeaways** → `~/Vault/research/yymmdd-topic-name-takeaways.md`
   - 3-5 key takeaways with [[vault links]]
   - Much shorter — just the signal

3. Update `~/Vault/INDEX.md` with new entry

4. Optionally generate NotebookLM deliverables:
   ```bash
   notebooklm generate audio        # podcast
   notebooklm generate slide-deck   # presentation
   notebooklm generate infographic  # visual summary
   ```

5. Run `/fact-checker` on the final output. Research outputs are high-risk for factual errors —
   wrong names, hallucinated citations, fabricated statistics. The fact-checker verifies all
   checkable claims and produces a verification report.

## When to Use This vs /deep-research

| Use `/research-pipeline` when: | Use `/deep-research` when: |
|-------------------------------|---------------------------|
| You have specific sources to analyze | You need broad web exploration |
| Token efficiency matters | Maximum rigor is required |
| YouTube videos or PDFs are primary sources | You need 80+ search queries |
| You want deliverables (podcasts, slides) | You need formal citation verification |
| Most research tasks (default choice) | Legal, compliance, or academic research |

## Gotchas

- NotebookLM outputs are free but not infallible — always validate key claims with sub-agents before accepting
- The pipeline must not treat NotebookLM summaries as primary sources — they are secondary analysis
- Token savings from NotebookLM offloading are only valuable if the research quality is maintained
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
