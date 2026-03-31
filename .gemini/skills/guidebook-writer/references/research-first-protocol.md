# Research-First Protocol — Anti-Hallucination Standard

This protocol prevents the #1 quality failure in BARMM guidebook production: **agents fabricating statistics, inventing program names, and citing wrong legal provisions** because they write from training data instead of verified local sources.

**The rule is simple: read first, write second. If you didn't read it, don't write it.**

---

## Why This Exists

In March 2026, Guidebook 13 was drafted with 17 chapters by parallel agents. The result:
- **Fabricated statistics**: "50,467 authorized positions" cited without verifying the source or temporal context
- **Invented program names**: "ESKEY" (doesn't exist), "Al-Huda Madrasah Education" (wrong AHME expansion)
- **Wrong legal citations**: Sulu "initially voted in favor" (they voted 54.3% AGAINST)
- **12 of 17 chapters had ZERO footnotes** despite citing dozens of laws and statistics

Every one of these failures happened because agents wrote from memory instead of reading the source files first.

---

## The Protocol: Three Phases Per Chapter

### Phase A: RESEARCH (before writing a single sentence)

For each chapter, the agent MUST read the relevant reference files and produce a **Chapter Fact Sheet** — a structured list of verified claims with exact source paths.

#### Which Files to Read Per Topic

| Chapter Topic | Required Reading | File Paths |
|---|---|---|
| BARMM governance, structure, officials | Governance framework, MOA structure, Officials | `~/.gemini/skills/bangsamoro/references/governance-framework.md`, `moa-structure.md`, `barmm-officials-2025-2026.md` |
| BOL provisions, territory, powers | BOL key provisions, BOL transcription | `~/.gemini/skills/bangsamoro/references/bol-key-provisions.md`, `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` |
| BAA references (any BAA number) | BAA index | `~/Vault/bangsamoro/bangsamoro-laws/index.md` |
| BDP goals, strategies, targets | BDP Chapter 4 | `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/04-chapter-4-development-framework.md` |
| Development data, statistics | Development framework, Social services, Economy | `~/.gemini/skills/bangsamoro/references/development-framework.md`, `social-services.md`, `economy.md` |
| Geography, provinces, municipalities | Geography | `~/.gemini/skills/bangsamoro/references/geography.md` |
| Peace process, history | History and peace process | `~/.gemini/skills/bangsamoro/references/history-peace-process.md` |
| Cultural diversity, ethnolinguistic groups | Cultural diversity | `~/.gemini/skills/bangsamoro/references/cultural-diversity.md` |
| CSW / ADDRESS IT | ADDRESS IT framework, CSW competencies | `~/.gemini/skills/csw/references/address-it-framework.md`, `csw-competencies.md` |
| Supervision, PPR, SBI | Supervisory tools | `~/.gemini/skills/supervision/references/supervisory-tools-and-frameworks.md` |
| Parliament staff competencies | Parliament staff competencies | `~/.gemini/skills/csw/references/parliament-staff-competencies.md` |
| Fact-check error patterns | Error log | `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md` |

**ALWAYS read the error log** before writing any chapter. It contains the most common mistakes and their correct answers.

#### Chapter Fact Sheet Format

```markdown
## Chapter N Fact Sheet

### Verified Claims (use these in the chapter)

| # | Claim | Source File | Line/Section | Citation Format |
|---|---|---|---|---|
| 1 | BARMM has 5 provinces: LDS, MagNor, MagSur, Basilan, Tawi-Tawi | bol-key-provisions.md | line 38 | [^N]: Rep. Act No. 11054, art. III; *Province of Sulu v. Medialdea*, G.R. Nos. 242255 et al. (Sept. 9, 2024). |
| 2 | 80 MPs per BOL Art. VII, Sec. 6 | bol-key-provisions.md | line 49 | [^N]: Rep. Act No. 11054, sec. 6, art. VII. |
| 3 | BAA 17 = Bangsamoro Civil Service Code | index.md | line 35 | [^N]: BAA No. 17. |

### Unverifiable Claims (flag if used)

| # | Claim | Why Unverifiable | Treatment |
|---|---|---|---|
| 1 | "50,467 authorized positions" | governance-framework.md cites this but doesn't name primary source | Use with caveat: "as reported in BDP Chapter 5 on Governance (November 2022)" |
| 2 | Salary grade amounts | No SSL table in local files | Use with caveat: "approximate, based on SSL; verify with DBM" |

### Claims NOT to Make (known errors)

| # | Wrong Claim | Why Wrong | Correct Claim |
|---|---|---|---|
| 1 | Sulu is a BARMM province | SC ruling excluded Sulu | 5 provinces, Sulu excluded |
| 2 | Art. IX = Shari'ah | Art. IX = Basic Rights | Art. X = Justice/Shari'ah |
```

### Phase B: WRITE (from the fact sheet, with inline citations)

The agent writes the chapter using ONLY claims from the Chapter Fact Sheet. Every factual claim gets a `[^N]` marker as it is written — not added later.

#### The Never-Fabricate Rules

1. **Never expand an acronym without reading the source.** If you can't find the expansion in a reference file, write the acronym unexpanded with a `[verify expansion]` marker.

2. **Never cite a statistic without a source file path.** If the number isn't in a reference file, do NOT include it. Write `[UNVERIFIED: (claimed statistic) — no local source found]` instead.

3. **Never cite a BOL article without checking bol-key-provisions.md.** The error log shows 13 instances of wrong BOL articles across previous guidebooks. Always verify.

4. **Never cite a BAA number without checking index.md.** The error log shows 6 instances of wrong BAA number-to-title mappings. Always verify.

5. **Never invent a program name.** If you're not sure a program exists, write `[verify: (program name)]` instead of guessing.

6. **Never present a data point without temporal context.** "Poverty is 29.80%" is wrong. "Poverty incidence was 29.80% in 2021 (PSA, cited in BDP 2023-2028)" is correct.

7. **If a claim is not in the fact sheet, do not include it.** If you believe the chapter needs additional information not in the fact sheet, add it to the "Gaps" section of the fact sheet and flag it for the user — do not fabricate to fill the gap.

#### Citation During Writing

Every factual sentence should look like this as it is written:

```markdown
The BOL establishes 55 areas of competence for the Bangsamoro Government.[^3]

[^3]: Rep. Act No. 11054, sec. 2, art. V.
```

NOT like this (citation-free, hoping someone adds it later):

```markdown
The BOL establishes 55 areas of competence for the Bangsamoro Government.
```

#### Handling Gaps

When the chapter outline requires content that isn't in the reference files:

```markdown
**[GAP: The plan calls for staffing data per ministry, but no ministry-level staffing
breakdown exists in local reference files. Options: (1) remove this section,
(2) user provides the data, (3) research via web search. Flagging for user decision.]**
```

This is infinitely better than fabricating numbers.

### Phase C: CITE (safety net pass)

After writing the chapter, invoke `/citation` to catch any claims that slipped through without footnotes. This is the SECOND citation pass — the first happened during writing.

The /citation pass checks:
- Every BOL/BAA/RA reference has a footnote
- Every statistic has a source
- Every framework is attributed on first use
- Every verbatim quote is cited
- No `[UNVERIFIED]` or `[verify]` markers remain without resolution

---

## Agent Dispatch Template

When dispatching parallel agents to write chapters, use this prompt structure:

```
You are writing Chapter N of [Guidebook Title].

## STEP 1: RESEARCH (do this BEFORE writing anything)

Read these files and build your Chapter Fact Sheet:
- [list specific files for this chapter's topic]
- ALWAYS read: ~/Vault/skill-outputs/fact-checker/fact-check-error-log.md

Extract every fact you will need. Verify every BOL article, BAA number,
and statistic against the source files. Build the fact sheet FIRST.

## STEP 2: WRITE (from your fact sheet only)

Write the chapter using ONLY verified facts from Step 1.
Add [^N] footnote markers inline AS YOU WRITE — not after.

NEVER FABRICATE RULES:
- Never expand acronyms without source verification
- Never cite statistics without a source file path
- Never cite BOL/BAA numbers from memory — verify against reference files
- If a fact is not in your sources, write [UNVERIFIED] instead of guessing
- Every data point needs temporal context (year, source)

## STEP 3: VERIFY

After writing, check that:
- Every [^N] marker has a corresponding definition
- No claims exist without footnotes
- No [UNVERIFIED] markers remain (flag them in your output)

## Chapter outline: [from plan]
## Output file: [path]
## Citation format: Philippine Manual of Legal Citations (Feliciano 10th Ed.)
```

---

## Quality Metrics

After implementing this protocol, measure:

| Metric | Before (Guidebook 13 v1) | Target |
|---|---|---|
| Chapters with zero footnotes | 12 of 17 (71%) | 0 of 17 (0%) |
| Fabricated statistics | 3+ found | 0 |
| Wrong BOL articles | 0 (fixed from prior patterns) | 0 |
| Invented program names | 2 (ESKEY, Al-Huda) | 0 |
| Unverified claims presented as fact | 5+ | 0 (flagged instead) |
