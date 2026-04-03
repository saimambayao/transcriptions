---
name: guidebook-writer
description: >
  Professional guidebook and manual creation for BARMM (Bangsamoro Parliament, Ministries,
  Offices, and Agencies). Use this skill whenever the user mentions "guidebook", "write a
  guidebook", "create a manual", "operations manual", "manual of operations", "guidebook for
  [topic]", "competency guide", "policy notes guidebook", "staff work manual", "write a guide
  for", "institutional manual", "procedures manual", "create a handbook", or wants to produce
  a multi-chapter professional document for any BARMM entity. Also trigger when the user
  references the Bill Drafting Guidebook as a template for creating similar documents, or
  mentions creating training manuals, standard operating procedures, or reference guides for
  government staff. Do NOT trigger for single-page documents, individual briefers, or one-off
  policy recommendations (those have their own skills).
---

# Guidebook Writer

Professional multi-chapter guidebook engine for the Bangsamoro Autonomous Region in Muslim Mindanao (BARMM). Produces publication-ready guidebooks in markdown, PDF, and DOCX formats for the Bangsamoro Parliament and its Ministries, Offices, and Agencies (MOAs).

## Proven Pattern

This skill follows the architecture of the **Bill Drafting Guidebook** (330 pages, 11 chapters + glossary + 7 appendices) — a production-tested pattern with:
- Modular markdown chapters (`NN-filename.md` ordering)
- Professional PDF generation (WeasyPrint) with navy/gold institutional styling
- Professional DOCX generation (python-docx) with matching typography
- Built-in quality pipeline (fact-check, legal review, QA reports)

## When to Use

- Creating a **new guidebook** for any BARMM competency, workflow, or institutional process
- Building a **manual of operations** for a ministry, office, or parliamentary division
- Developing **policy notes series** with improved structure beyond existing PRLS format
- Producing **CSW (Complete Staff Work) manuals**, speech writing guides, briefer guides, or legal review handbooks
- Any multi-chapter reference document targeting BARMM government staff

## When NOT to Use

- Single documents: use `/policy-recommendation`, `/legislative-briefer`, `/speech-writer`, or `/bill-drafter` directly
- Quick reference sheets or one-pagers
- Training materials: use `/training-assistant`

## Verification Protocol

This skill follows the Universal Verification Framework (Prevent → Detect → Confirm).
Read `~/.claude/skills/fact-checker/references/verification-framework.md` for the full protocol.
Read `~/.claude/skills/fact-checker/references/source-preload-protocol.md` — MANDATORY: load source text BEFORE writing any citation. No claims from training data when local source exists.
If a claim cannot be verified against loaded source files, mark it `[UNVERIFIED]` — never guess or fabricate. See source-preload-protocol.md Section 4.
**NEVER cite other BARMM guidebooks as primary sources for factual claims** (legislation numbers, BOL articles, official data). Guidebooks are still in development and may contain errors. Always trace factual claims back to the enacted law, BOL provision, or official document — cite THAT, not the guidebook. Guidebooks may only be referenced for format/structure templates, methodology patterns, or writing style.

**Before writing (PREVENT):**
1. Invoke `/bangsamoro` to load domain context
2. Read the fact-check error log at `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md`
3. Fast research: check for recent developments on the topic (new BAAs, leadership changes, court rulings)
4. Read authoritative reference files relevant to the topic
5. Build a Fact Sheet from verified sources — sole source of truth for writing
6. Include Fact Sheet + fabrication warnings in all subagent prompts

**After writing (DETECT):**
Invoke `/fact-checker` on the complete document. The enhanced fact-checker runs P1-P10 checks automatically.

**Before publishing (CONFIRM):**
Present the fact-check report to the user. Fix all CRITICAL and HIGH errors. Regenerate output only after report is clean.

---

## Workflow Overview

```
Phase 1: SCOPE    →  Pre-draft interview (subject, audience, chapters, skills)
Phase 2: PLAN     →  Table of contents + chapter outline (user approval)
Phase 3: RESEARCH →  Build Chapter Fact Sheets from verified local sources (NO writing yet)
Phase 4: DRAFT    →  Write from fact sheets with inline citations (never from memory)
Phase 5: REVIEW   →  Quality pipeline (fact-check, legal review, QA, citation audit)
Phase 6: BUILD    →  Generate PDF + DOCX output files
```

### Anti-Hallucination Standard

This skill follows a **research-first protocol** to prevent fabricated data. Read `references/research-first-protocol.md` for the full procedure. The core rule: **if you didn't read it in a source file, don't write it.** Agents must RESEARCH before WRITING. Citations are built inline during writing, not added after. Unverifiable claims are flagged with `[UNVERIFIED]` markers, never presented as fact.

---

## Phase 1: SCOPE — Pre-Draft Interview

Before writing anything, conduct this interview to disambiguate requirements. Adapt questions based on answers — skip what's already clear from context.

### Required Inputs

1. **Subject** — What competency or workflow does this guidebook cover?
2. **Target Audience** — Who will use it? Name specific roles, not generic labels.
   - Parliament staff (legislative focus)
   - MOA staff (executive/administrative focus)
   - Cross-cutting (both Parliament and MOAs)
   - Specific division or office
   - **Audience validation (Pattern #12):** For each audience member listed, test: would this
     person actually open the guidebook and apply it to their daily work? Remove anyone who
     would not. "Administrative staff" and "government staff" are too generic — name the
     actual roles (bill drafters, legal researchers, policy analysts, ministry directors).
3. **Institutional Context** — Which BARMM entity is this for?
   - Bangsamoro Parliament (BTA)
   - A specific Ministry (e.g., MBHTE, MOH, MAFAR)
   - An Office or Agency (e.g., OOBC, BPDA, MOTC)
   - Cross-institutional
4. **Scope** — What chapters should it cover? (User may have a list, or ask for recommendations)
5. **Composing Skills** — Which existing skills feed into this guidebook?

   | Guidebook Type | Primary Skill | Audience |
   |----------------|---------------|----------|
   | Policy Recommendations | `/policy-recommendation` | MOAs, Parliament committees |
   | Speech Writing | `/speech-writer` | Parliament (MPs, Speaker, executives) |
   | Legislative Briefer / CSW | `/legislative-briefer` + ADDRESS IT framework | Parliament staff, MOA analysts |
   | Legal Review | `/legal-reviewer` | Parliament, MOA legal units |
   | Bill Drafting | `/bill-drafter` | Parliament staff, consultants |
   | Resolution Drafting | `/resolution-drafter` | Parliament staff |
   | Manual of Operations | — | MOAs, Parliament offices |
   | Policy Notes | — | PRLS, MOA policy units |
   | Other | (extensible) | Any BARMM entity |

6. **Complexity Tier**:
   - **Compact** (5-7 chapters, 80-120 pages) — focused workflow or single competency
   - **Standard** (8-12 chapters, 150-250 pages) — comprehensive competency guide
   - **Comprehensive** (12+ chapters, 250+ pages) — institutional reference manual

7. **Sample Documents** — Does the user have existing documents to improve upon? (Read them to extract patterns and identify gaps.)

### Handling Uncertainty

If the user is unsure about chapters or scope, recommend the chapter structure from `${CLAUDE_SKILL_DIR}/references/chapter-templates.md` for their guidebook type. If no composing skill applies, proceed as standalone — the guidebook itself becomes the reference. If a composing skill is unavailable or fails, write the chapter from domain knowledge (via `/bangsamoro`) without the specialized skill integration.

### Domain Context Loading

After the interview, invoke `/bangsamoro` to load domain context. This provides verified facts about BARMM governance, officials, BOL provisions, and the BDP framework — preventing factual errors throughout the guidebook.

---

## Phase 2: PLAN — Table of Contents

Generate a proposed chapter structure based on the interview. Read `${CLAUDE_SKILL_DIR}/references/chapter-templates.md` for recommended structures per guidebook type.

### Output Directory Setup

Create the guidebook directory under `guidebooks/`:
```
guidebooks/{guidebook-slug}/
├── 00-table-of-contents.md
├── 00b-about.md
├── 00c-author.md
├── 01-introduction.md
├── 02-chapter-01.md
├── ... (NN-chapter-NN.md)
├── {N}-glossary.md
├── {N+1}-bibliography.md
├── generate-pdf.py      (adapted from bill-drafting template)
├── generate-docx.py     (adapted from bill-drafting template)
├── guidebook-template.html  (adapted styling)
├── images/              (Mermaid-rendered diagrams)
├── appendices/
│   ├── Appendix-A-*.html
│   └── Appendix-A-*.pdf
└── PROGRESS.md          (multi-session progress tracker)
```

### TOC Format

Use `&emsp;` indentation for hierarchical TOC entries matching the bill-drafting pattern:
```markdown
## Table of Contents

**Chapter 1 — Title**
&emsp;1.1 Section
&emsp;&emsp;1.1.1 Subsection
```

Present the full TOC to the user for approval before proceeding. Expect 1-2 rounds of revision.

### Implementation Plan Generation

After the TOC is approved, generate a comprehensive implementation plan file and save it to `docs/superpowers/plans/YYYY-MM-DD-{guidebook-slug}.md`. This plan serves as the execution blueprint for agentic workers.

**Plan template:** Follow the format established in `docs/superpowers/plans/2026-03-27-systems-change-guidebook.md` (the canonical reference). Key elements:

1. **Header block** — Goal, architecture summary, tech stack, source material paths, secondary sources, existing guidebook reference for voice consistency
2. **Pre-Implementation Setup** — Task 0: directory creation + `/bangsamoro` invocation
3. **Front Matter Tasks** — TOC, About, Author (always use canonical bio from `~/Vault/reference/author-bio-standard.md`)
4. **Chapter Writing Tasks** — One task per chapter with:
   - Files to create
   - Source files to read (with specific paths and line ranges)
   - Target word count
   - Step-by-step: read sources → write chapter → invoke `/citation` → commit
   - Full section outline with subsection titles and content guidance
5. **Back Matter Tasks** — Glossary, Bibliography/Appendices
6. **Build Pipeline Task** — adapt generate-pdf.py, generate-docx.py, guidebook-template.html
7. **Quality Assurance Task** — `/fact-checker` + citation audit + cross-reference check
8. **Index Update Task** — update INDEX.md + GUIDEBOOK-PRODUCTION-PLAN.md
9. **Summary table** — all tasks with file names and estimated word counts
10. **Parallel execution strategy** — which tasks can run as concurrent agent batches

**Chapter organization principle:** When a guidebook covers multiple sectors or domains, organize them by **causal chain** (what drives what) rather than alphabetically or arbitrarily. Mirror the sector order between theory chapters and application chapters.

---

## Phase 3: RESEARCH — Build Chapter Fact Sheets

**Before writing a single sentence**, research the verified facts for each chapter. Read `references/research-first-protocol.md` for the complete procedure.

For each chapter, the agent (or you) must:

1. **Read the relevant reference files** listed in the research-first protocol's topic-to-file mapping table
2. **ALWAYS read the error log** at `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md` — this prevents the top recurring mistakes
3. **Build a Chapter Fact Sheet** — a structured table of verified claims with source file paths, line numbers, and pre-formatted citation text
4. **Flag unverifiable claims** — if the plan calls for data that isn't in any reference file, mark it as `[UNVERIFIED]` with options (remove, user provides, web search)
5. **List claims NOT to make** — known errors from the error log that relate to this chapter's topic

The fact sheet becomes the **sole source of truth** for writing. No claim enters the chapter unless it appears in the fact sheet.

### Agent Dispatch with Fact Sheets

When dispatching parallel agents, each agent's prompt MUST include:

```
## STEP 1: RESEARCH (do this BEFORE writing anything)
Read these files and build your Chapter Fact Sheet:
- [list specific files]
- ALWAYS: ~/Vault/skill-outputs/fact-checker/fact-check-error-log.md

## STEP 2: WRITE (from fact sheet only, with inline citations)
Never fabricate. If not in your sources, write [UNVERIFIED] instead.
Add [^N] footnote markers AS YOU WRITE — not after.

## STEP 3: VERIFY
Check every [^N] has a definition. Flag any [UNVERIFIED] markers.
```

### The Seven Never-Fabricate Rules

1. **Never expand an acronym** without reading the source document
2. **Never cite a statistic** without a source file path
3. **Never cite a BOL article** without verifying against bol-key-provisions.md
4. **Never cite a BAA number** without verifying against index.md
5. **Never invent a program name** — if unsure, write `[verify: name]`
6. **Never present data without temporal context** — always include the year and source
7. **If a claim is not in the fact sheet, do not include it** — flag the gap instead

---

## Phase 4: DRAFT — Chapter-by-Chapter Writing

Draft one chapter at a time, writing ONLY from the Chapter Fact Sheet produced in Phase 3. Present each to the user for approval before moving to the next.

### Citation From the Start

Every factual claim gets a `[^N]` footnote marker **as it is written** — not added later. This is structural, not cosmetic. A sentence like:

```markdown
The BOL establishes 55 areas of competence.[^3]

[^3]: Rep. Act No. 11054, sec. 2, art. V.
```

is correct. A sentence without its footnote is incomplete.

### Mandatory Citation Safety Net

**After drafting each chapter**, invoke `/citation` as a safety net to catch any claims that slipped through without footnotes. This is the SECOND citation pass — the first happened during writing. A chapter without footnotes is incomplete and must not be presented to the user.

### Per-Chapter QA Loop (MANDATORY)

**Every chapter must pass through this loop before proceeding to the next chapter.** Do not batch chapters — write one, QA it, fix it, regenerate, then move on. This catches errors early when they're cheapest to fix.

**The loop:**

```
1. RESEARCH — Read authoritative local sources for the chapter's topic:
   a. Identify which source files are needed (BOL chapters, BAA text, PD 1083 sections, BDP chapters,
      Qur'an/Hadith for Shari'ah content, reference files from /bangsamoro or /shariah)
   b. Read each source file using the Read tool — load the actual text into context
   c. Build a Chapter Fact Sheet: table of verified claims with source file path + line number
   d. Read the fact-check error log for known fabrication patterns on this topic
   e. List claims NOT to make (known errors from the error log)
   → The fact sheet is the SOLE source of truth for writing. No claim enters the chapter
     unless it appears in the fact sheet with a verified source path.

2. WRITE chapter (from fact sheet only, with inline [^N] citations as you write)
   - Every factual claim gets its footnote AT THE TIME OF WRITING, not added after
   - When quoting legal text, copy VERBATIM from the loaded source — never paraphrase from memory
   - When citing scriptural sources, grep the local Qur'an/Hadith files — never cite from training data

3. SCAN for prohibited phrases, internal path leaks, and skill terminology in published text

4. RUN /fact-checker VALIDATE on the chapter
   - Classify every factual claim (SOURCED / AUTHOR'S OBSERVATION / INFERENTIAL / UNSOURCED)
   - Verify every SOURCED claim against the loaded source files (BOL verbatim, BAA text, PD 1083)
   - Check footnote accuracy (correct article/section, source matches claim)
   - Flag any fabricated citations (wrong BAA numbers, invented BOL provisions, misquoted text)

5. FIX all CRITICAL (P1-P4) and HIGH (P5-P8) errors

6. REGENERATE PDF to verify the chapter renders correctly

7. VISUAL VERIFICATION — screenshot the PDF and iterate until correct:
   a. Convert PDF page(s) to image: `pdftoppm -jpeg -r 150 -f <page> -l <page> output.pdf /tmp/pdf-verify`
   b. Read the image: `Read /tmp/pdf-verify-<page>.jpg`
   c. Inspect for: layout issues, title wrapping, table overflow, missing content, rendering artifacts
   d. If ANY issue found: fix the source (CSS, markdown, or template), regenerate, screenshot again
   e. Loop steps a-d until the visual output is correct — do NOT present to user and wait for feedback
   f. Only proceed when the screenshot matches the intended design
   This applies to ALL visual changes: cover page design, chapter layouts, table formatting,
   diagram rendering, and any CSS modifications. The user should never have to send a
   screenshot back to point out a visual issue that was visible in the generated PDF.

8. UPDATE PROGRESS.md — mark chapter status as "Drafted + QA" with date

9. PRESENT the fact-check summary to the user, then proceed to the next chapter
```

**Exit condition:** 0 CRITICAL errors AND 0 HIGH errors in the fact-check report.

**Source file mapping — read BEFORE writing each chapter:**

| Topic | Local Source Files |
|-------|-------------------|
| BOL provisions | `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` (5 chapter files) |
| BAA references | `~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md` → full text at `BAA-{N}.md` |
| PD 1083 | `~/apps/transcriptions/legislation/national-laws/PD-1083.md` |
| BDP targets | `~/Vault/bangsamoro/bangsamoro-development/bdp-chapter-summaries.md` |
| Officials/institutions | `~/.claude/skills/bangsamoro/references/moa-structure.md`, `barmm-officials-2025-2026.md` |
| Qur'an | `~/apps/transcriptions/shari'ah/quran/` (grep by keyword) |
| Hadith (Kutub al-Sittah) | `~/apps/transcriptions/shari'ah/hadith/{bukhari,muslim,abudawud,tirmidhi,nasai,ibnmajah}/` |
| Known errors | `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md` |
| Constitutional provisions | `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/01-articles-I-to-V.md` (Art. X = Constitution) |

**Rule:** If a claim is not in the fact sheet, do not include it. Flag the gap instead.

**Known high-risk claims to verify for every chapter:**
- Every BOL article and section number → read the actual chapter file
- Every BAA number → cross-check against `baa-quick-reference.md`
- Every verbatim legal quote → compare word-for-word against source text
- Every footnote → verify the cited provision matches the claim it supports
- Preamble and purpose clause quotes → read the actual text, never paraphrase from memory
- Names of institutions → verify against `moa-structure.md` (e.g., "Shari'ah High Court" not "Shari'ah Appellate Court")

**What this loop catches that end-of-guidebook QA misses:**
- Fabricated citations that propagate across later chapters (Ch. 2 cites a wrong BAA → Ch. 5 repeats it)
- Training data leaking into legal quotes (preamble paraphrased from memory instead of verbatim)
- Internal skill terminology in published text (EXTRACTED, FIQH tags, local file paths)
- AI issue patterns presented as human researcher patterns

### Chapter Length Targets

Target chapter length varies by complexity tier — this keeps guidebooks proportional:
- **Compact**: 12-18 pages per chapter
- **Standard**: 15-25 pages per chapter
- **Comprehensive**: 20-30 pages per chapter

### Multi-Session Progress Tracking (MANDATORY FORMAT)

Create a `PROGRESS.md` file in the guidebook directory with this structure:

1. **Pipeline definition** — the 9-step per-chapter loop (copy from the Per-Chapter QA Loop above)
2. **Chapter status table** with columns for each pipeline step:
   `| # | Chapter | Written | Scanned | Validated | Fixed | PDF | Visual | QA Complete |`
   - "Validated" means full `/fact-checker VALIDATE` was run (claim-by-claim classification, source verification) — NOT inline spot-checks
   - Mark "Inline only" if you did spot-checks but not the full VALIDATE protocol
   - A chapter is not "QA Complete" until full VALIDATE has run with 0 CRITICAL + 0 HIGH
3. **Fact-check error log** — every error found and corrected during production, with chapter, error description, type, and fix applied
4. **Session log** — date entries for each session's work

**The rule:** If PROGRESS.md shows "Inline only" for any chapter, that chapter is NOT done. Run the full VALIDATE before claiming QA Complete. The user can check PROGRESS.md at any time to see exactly where each chapter stands in the pipeline.

### Chapter Structure Pattern

Each chapter follows this internal structure:
1. **H1** — Chapter title (triggers page break in PDF/DOCX)
2. **Opening paragraph** — Context and purpose of the chapter
3. **HR** (`---`) — Visual separator
4. **H2 sections** — Major topics with H3/H4 subsections
5. **Practical guidance** — Tips, checklists, examples throughout
6. **Blockquotes** — Verbatim legal text (BOL, BAAs) where relevant
7. **Tables** — Comparison matrices, reference data
8. **HR** at section boundaries

### Writing Standards

- **Audience-adaptive tone**: Formal but accessible. Parliament staff expect legislative terminology; MOA staff expect administrative/operational language.
- **Bold key terms** for scannability
- **Blockquote verbatim legal text** — always cite the source (BOL Article/Section, BAA number)
- **Practical examples** — show don't just tell. Include sample documents, filled-out forms, annotated templates.
- **Cross-references** — link chapters to each other ("See Chapter 3 for the anatomy of a bill")
- **Composing skill integration** — when a chapter covers a competency that has its own skill, invoke that skill for domain knowledge. The guidebook chapter teaches the *process and principles*; the skill handles the *execution*.

### Writing Voice — The BARMM Guidebook Standard

Every guidebook produced by this skill must follow the proven voice from the Bill Drafting Guidebook. Read `references/writing-style-guide.md` for full guidance, golden paragraphs, and anti-patterns.

**The voice in one sentence:** A senior colleague coaching a competent professional — authoritative, direct, practical.

**Mandatory rules:**
- **Person**: Direct second-person ("you", "your"). Never "one should" or "the drafter shall."
- **Sentences**: Average 15-20 words. Maximum 30. If it needs a semicolon, split it.
- **Paragraphs**: Maximum 5 sentences. One-sentence paragraphs allowed for emphasis.
- **Openings**: Each chapter opens with WHY this matters to the reader's work right now. Not history. Not definitions.
- **Instructions**: Imperative mood. "Draft the summary before the hearing." Not "The summary should be drafted."
- **Examples**: Every principle followed by a concrete BARMM example. No principle stands alone.
- **Active voice**: 80%+ of sentences. Passive only when actor is unknown.
- **Bold key terms** for scannability — the busy reader should get the gist from bold text alone.

**Prohibited phrases** (these signal AI-generated or academic writing):
"It is important to note that", "In order to", "It should be noted", "With regard to", "In the context of", "It is worth mentioning", "As previously mentioned", "For the purposes of", "In light of the foregoing", "The aforementioned", "It is recommended that", "Pursuant to the provisions of", "Notwithstanding the foregoing", "In furtherance of"

**Good vs. Bad:**

| Bad (academic/bureaucratic) | Good (BARMM guidebook voice) |
|---|---|
| "It is hereby recommended that legislative staff undertake a comprehensive review..." | "Review the bill before the hearing. Every provision. Every section." |
| "The implementation of the proposed measure necessitates..." | "Someone has to implement this bill. Is the agency ready?" |
| "In order to fully understand the implications of the proposed legislation..." | "What happens when this bill becomes law? Three things change." |

### MOA-Specific Adaptations

When the audience is a Ministry, Office, or Agency:
- Replace parliamentary terminology with executive/administrative equivalents
- Focus on **approval workflows**, **delegation hierarchies**, and **transmittal memoranda** (pattern from PRLS MOPs)
- Include **PRLS Form references** and standardized output tracking
- Add **role-based procedures** (Director → Chief of Division → Staff Officer)
- Reference **BAA No. 13** (Bangsamoro Administrative Code) for MOA structure and mandates

**MOA Voice Adjustments:**
- Replace "your MP" with "your Director" or "your Minister"
- Replace "the floor" with "the approval chain"
- Replace "interpellation" with "review and feedback"
- Tone shifts from "prepare for the hearing" urgency to "meet the compliance deadline" urgency
- Examples from budget execution, program delivery, and COA findings instead of plenary proceedings

### Front Matter Files

- **00b-about.md**: Purpose statement, intended audience, how to use the manual, acknowledgments
- **00c-author.md**: Author bio — always use the canonical version from `~/Vault/reference/author-bio-standard.md` verbatim. Never improvise or pull from `about-saidamen.md`.

### Glossary

Generate a domain-specific glossary (`{N}-glossary.md`) with terms defined within the guidebook's domain. Format: term in bold, followed by definition paragraph.

### Appendices

Include detachable practical tools as appendices:
- **Checklists** (pre-drafting, quality review, compliance)
- **Templates** (annotated samples of the competency's outputs)
- **Quick reference cards** (condensed workflow steps)

- **Forms** (standardized institutional forms)

Generate appendices in both markdown and HTML/PDF pairs (in `appendices/` subdirectory).

### Appendix Voice

Appendices serve a different purpose than chapters. Chapters coach. Appendices equip.

**Chapter voice**: Explanatory, example-rich, conversational. "Here is why this matters and how to do it well."

**Template appendix voice**: Clinical but human. Each section gets a brief instruction block:
- **Purpose** (1 sentence -- why this section exists)
- **What to include** (2-4 bullets -- what goes here)
- **Sources** (where to find the information -- name specific BARMM institutions)

The instruction block speaks to the reader directly but briefly. The fill-in fields below it are clean and spacious.

**Instruction tone test:**
- Good: "Give the MP a complete snapshot of the bill -- what it does, where it stands, what action is needed next."
- Bad: "This section is intended to provide a comprehensive overview of the legislative measure under consideration."

If the appendix instruction sounds like it came from a bureaucratic form, rewrite it until it sounds like a note from a helpful colleague.

---

## Phase 4b: VERIFY — Automated Reference Cross-Check (MANDATORY)

**This phase runs AFTER all chapters are drafted and BEFORE the quality pipeline.** It catches fabricated legislative references that `/citation` and `/fact-checker` miss.

### Why This Phase Exists

Subagents writing chapters may not have BAA reference files loaded. When they encounter a legislative claim, they fill in plausible-sounding BAA numbers from training data — and those numbers are often **wrong**. `/citation` then formats these wrong numbers into proper Feliciano footnotes, making fabricated references look authoritative. This phase catches those errors before they reach the reader.

### The Verification Script

Use `verify-references.py` (available at `guidebooks/systems-change-bangsamoro/verify-references.py` as the canonical version). Copy it into each new guidebook directory and run it.

```bash
python3 verify-references.py --ref ~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md
```

The script:
1. Reads ALL markdown files in the guidebook directory
2. Extracts every `BAA No. N` reference and cross-checks against the authoritative BAA list
3. Extracts every `Rep. Act No.` reference and checks article/section citations
4. Extracts every footnote definition and verifies its legislative claims
5. Flags statistics without footnote citations
6. Produces a `VERIFICATION-REPORT.md` with MATCH/MISMATCH/NOT_FOUND for every reference

### Mandatory Actions

- **MISMATCH**: Fix immediately. The BAA number exists but the claimed title is wrong (e.g., "BAA 25 (Environment Code)" when BAA 25 is actually a hospital upgrade).
- **NOT_FOUND**: The BAA number doesn't exist. Remove or replace with the correct reference.
- **Statistics without footnotes**: Add footnote citations or remove the claim.

### Known Fabrication Patterns (from production experience)

Subagents commonly fabricate these — always verify:
- BAA numbers for "Environment Code" (does not exist as of 2026)
- BAA numbers for BEZA (BEZA is created by the BOL, not a BAA)
- Swapped BAA numbers (e.g., calling BAA 13 the "Local Governance Code" when it is the "Administrative Code")
- Invented BAA numbers above 89 (only 89 BAAs enacted as of Feb 2026)
- Wrong BOL article numbers (e.g., Art. VI for parliamentary system when it is Art. VII)

### This Phase Is Non-Negotiable

Do NOT skip this phase. Do NOT proceed to Phase 5 until every MISMATCH and NOT_FOUND is resolved. A beautifully formatted wrong citation is worse than no citation — it damages institutional credibility.

---

## Phase 5: REVIEW — Quality Pipeline

After all chapters are verified (Phase 4b) and drafted, run the quality pipeline. Read `${CLAUDE_SKILL_DIR}/references/quality-pipeline.md` for detailed procedures.

### Step 1: Fact-Check (invoke `/fact-checker`) — run on EVERY chapter, not just the capstone
- Verify all names, titles, dates, legislation references
- Check BOL citations against `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/`
- Check BAA references against local archives
- Output: `FACT-CHECK-REPORT.md`

### Step 2: Legal Review (invoke `/legal-reviewer`)
- Verify all quoted legal provisions are verbatim-accurate
- Check section/article/chapter numbering
- Output: `LEGAL-REVIEW-REPORT.md`

### Step 3: QA Report
- Internal consistency (terms used consistently, cross-references valid)
- Completeness (no placeholder text, all sections substantive)
- Style compliance (heading hierarchy, markdown formatting)
- Real examples audit: Does every example in the guidebook cite a real BAA or Resolution number? Are hypothetical examples only used where no real example exists?
- Output: `QA-REPORT.md`

### Severity-Based Fix Workflow

- **CRITICAL** errors (wrong names, incorrect legal citations, misquoted BOL provisions): Must be fixed before Phase 5. These would damage institutional credibility.
- **MINOR** errors (style inconsistencies, formatting, suboptimal phrasing): Should be fixed but do not block PDF/DOCX generation.

Apply all critical fixes, then as many minor fixes as feasible, before proceeding.

---

## Real Examples Standard

Every guidebook produced by this skill must prioritize real examples from enacted legislation and adopted resolutions over hypothetical ones. This grounds the guidebook in actual BARMM legislative practice and gives readers verifiable reference points.

### 1. Real Examples First

When demonstrating any legislative pattern, structure, or format, search the vault legislative archive first for real examples from enacted BAAs or adopted resolutions:
- `~/Vault/bangsamoro/bangsamoro-laws/` — enacted Bangsamoro Appropriations Acts and other legislation
- `~/Vault/bangsamoro/bangsamoro-resolutions/` — adopted Parliament resolutions

Only use hypothetical examples when no real example exists for the pattern being demonstrated. If you must use a hypothetical, mark it explicitly: *"Hypothetical example — no enacted BAA currently demonstrates this pattern."*

### 2. Visual Screenshots

Include cropped screenshots from actual PDF source documents as figures in guidebook chapters. Source PDFs live in:
- `docs/BAA-PDFs/` — enacted BAA source documents
- `docs/Resolutions-PDFs/` — adopted resolution source documents

**Screenshot generation workflow:**
```bash
# Convert PDF page to JPEG
pdftoppm -jpeg -r 200 -f <page> -l <page> "source.pdf" output_prefix

# Crop to relevant portion using Python PIL
python3 -c "
from PIL import Image
img = Image.open('output_prefix-<page>.jpg')
cropped = img.crop((left, top, right, bottom))
cropped.save('images/figure-NN-description.jpg', quality=90)
"
```

Save all screenshot figures to the `images/` directory within the guidebook version folder.

### 3. Citation Convention

Every real example must cite the BAA number or Resolution number. Use this format for figure captions:

> **Figure 3:** BAA 67 — Hospital Bill header format

> **Figure 7:** BTA Resolution No. 182 — Whereas clause structure

In-text references follow the same pattern: *"As shown in BAA 84 (Budget System Act), the enacting clause reads..."*

### 4. Pattern Analysis as Evidence Base

Reference the pattern analysis documents in the vault as the empirical foundation for guidebook recommendations:
- `~/Vault/bangsamoro/bangsamoro-laws/baa-legislative-patterns.md` — analysis of 89 enacted BAAs covering formatting conventions, clause variants, and structural patterns
- `~/Vault/bangsamoro/bangsamoro-resolutions/resolution-drafting-patterns.md` — analysis of 30+ adopted resolutions covering structure and language patterns

When a guidebook makes a recommendation about standard practice (e.g., "Most BAAs use a short title section"), cite the pattern analysis data: *"Of the 89 enacted BAAs analyzed, 82 include a short title as Section 1."*

### 5. Standardized Clause Templates

When a guidebook covers standard legislative provisions — Separability Clause, Repealing Clause, Effectivity Clause, IRR Provision — use the prescribed templates from the pattern analysis documents rather than generic or hypothetical language. These templates reflect the actual wording used in enacted BARMM legislation.

---

## Footnotes and Attribution (MANDATORY)

**Every guidebook must properly cite all sources to avoid plagiarism.** This is non-negotiable.

### Footnote Format

Use markdown footnotes per the Philippine Manual of Legal Citations (Feliciano, 10th Ed., 2019):

```markdown
Text making a claim or quoting a source.[^1]

[^1]: Rep. Act No. 11054, sec. 22, art. IX.
```

### What Requires a Footnote

- **Every verbatim legal quotation** (BOL, Constitution, BAAs, Resolutions, Republic Acts)
- **Every borrowed methodology or framework** (Oregon Bill Drafting Manual, Segal, Thornton, etc.)
- **Every data point from research** (survey results, statistics, studies)
- **Every Feliciano Manual rule reference** (cite Rule number and page)
- **Every pattern analysis claim** (cite the corpus: "Analysis of 89 enacted BAAs, 2019-2026")

### Citation Formats (per Feliciano)

| Source Type | Footnote Format |
|-------------|----------------|
| Republic Act | `Rep. Act No. 11054, sec. 22, art. IX.` |
| BAA | `BAA No. 13, sec. 3, Book II.` |
| Resolution | `Adopted Res. No. 268, BTA Parliament.` |
| Constitution | `Const. art. VII, sec. 1.` |
| Feliciano Manual | `Feliciano, Myrna S., *Philippine Manual of Legal Citations*, 10th ed. (Quezon City: U.P. Law Complex, 2019), Rule 4.6, p. 19.` |
| Book | `Segal, Mark, *Legislative Drafting* (London: Routledge, 2018), ch. 3.` |
| Subsequent ref | `*Id.*, sec. 25.` or `*Id.* at 19.` |

### Bibliography

Every guidebook must end with a **Bibliography and References** section listing all cited works, organized by category (Primary Legal Sources, Citation Standards, Subject-Matter References, Training/Research Sources).

### Quality Check

Before finalizing any guidebook, verify:
- Does every blockquoted legal provision have a footnote citing the source?
- Does every borrowed framework credit the original author?
- Does every data point cite the study/survey?
- Is there a complete Bibliography section?

---

## Phase 6: BUILD — Output Generation

Adapt the proven generation scripts from the bill-drafting template. Read `${CLAUDE_SKILL_DIR}/references/build-pipeline.md` for the full adaptation guide.

### Customization Points

Each guidebook needs these adapted:
- **Cover page**: Title, subtitle, institution name, author
- **Color scheme**: Navy (#1B365D) + Gold (#C5A54E) is the default BARMM institutional palette. MOAs may have their own colors.
- **Running headers/footers**: Guidebook title, author, page numbers
- **MD_FILES list**: Ordered list of the guidebook's markdown files

### Mandatory Diagram Rendering

**CRITICAL**: Never use ASCII art or monospace code-block flowcharts in guidebook PDFs. They look unprofessional. All flowcharts, process diagrams, and organizational charts must be rendered as proper images.

**Approach — Mermaid to PNG:**
1. Write diagrams in Mermaid syntax in a `.mmd` file in the `images/` directory
2. Render to PNG using Mermaid CLI: `npx -y @mermaid-js/mermaid-cli mmdc -i diagram.mmd -o diagram.png -t neutral -b transparent -w 1200`
3. Reference the PNG in markdown: `![Figure N: Description](images/diagram.png)`
4. Delete the `.mmd` source file after rendering (keep only the PNG)

**Excalidraw (default for all diagrams):** Use the `/excalidraw` skill for all diagram generation. It produces higher quality output than Mermaid with BARMM colors, self-validation, and hand-drawn aesthetic. Render: `~/.claude/skills/excalidraw/scripts/venv/bin/python3 ~/.claude/skills/excalidraw/scripts/render_excalidraw.py input.excalidraw -o output.png`. Fall back to Mermaid only for sequence diagrams or ER diagrams.

**Infographics and visual summaries:** For chapter-level infographics, one-page visual summaries, dashboards, and visual briefs, use `/visualize` to generate self-contained HTML visualizations that can be converted to PNG for embedding.

**If Mermaid CLI is unavailable**, use the `/designer` skill to generate diagrams as SVG/PNG, or use HTML/CSS styled diagrams directly in the `guidebook-template.html`.

**Rules:**
- Every flowchart in the markdown must be an image, not a code block
- Process flows use Mermaid `flowchart TD` (top-down) or `flowchart LR` (left-right)
- Organizational charts use Mermaid `graph TD`
- Use the guidebook's color scheme in Mermaid theme config (Navy #1B365D for nodes, Gold #C5A54E for decision diamonds)
- Maximum diagram width: 1200px (fits A4 with margins)

**In `generate-pdf.py`**, add a pre-processing step that detects any remaining ` ```mermaid ` code blocks and renders them to PNG before HTML conversion. This is a safety net — diagrams should already be images by the time the build runs.

### Mandatory Footnote Rendering

**PDF Footnote Rendering:** When the document will be rendered as PDF, footnotes must appear on a separate page with a 'Footnotes' heading — never inline after chapter text. Ensure the `footnotes` markdown extension is enabled in generate-pdf.py, and the guidebook-template.html has `page-break-before: always` on the `.footnote` class. See `references/build-pipeline.md` for the full CSS pattern.

### Mandatory Table CSS Rules

**CRITICAL**: Every `guidebook-template.html` MUST include these table rules to prevent tables from overflowing the page. This is a recurring issue — tables without these rules get cut off on the right side in PDF output.

```css
/* MANDATORY — prevents table overflow in PDF */
table {
  width: 100%;
  max-width: 100%;
  table-layout: fixed;      /* NEVER use 'auto' — causes page overflow */
  border-collapse: collapse;
  word-wrap: break-word;
  overflow-wrap: break-word;
  overflow: hidden;
  font-size: 9pt;           /* Slightly smaller than body text for readability */
  line-height: 1.35;
}

td, th {
  overflow: hidden;
  text-overflow: ellipsis;
  word-wrap: break-word;
  overflow-wrap: break-word;
  padding: 2.5mm 3mm;
}

/* For tables with many columns (5+), reduce font further */
table td, table th {
  font-size: inherit;       /* Inherits from table's 9pt */
}
```

**Rules:**
- `table-layout: fixed` is non-negotiable — `auto` lets content push columns beyond the page
- All tables get `max-width: 100%` and `overflow: hidden`
- Cell content wraps with `word-wrap: break-word`
- For wide tables (6+ columns), consider splitting into multiple tables or rotating to landscape

### Generation Commands

```bash
python3 generate-pdf.py    # → {Guidebook-Title}.pdf
python3 generate-docx.py   # → {Guidebook-Title}.docx
```

Dependencies: `pip3 install markdown weasyprint python-docx`

---

## Improving on Existing Formats

When the user provides sample documents to improve upon, read them first and identify specific gaps. Read `${CLAUDE_SKILL_DIR}/references/improvement-patterns.md` for detailed improvement strategies for:
- **PRLS Manuals of Operations** — expand from procedural SOPs to include rationale, best practices, and quality standards
- **PRLS Policy Notes** — deepen from 7-page briefs to comprehensive analytical frameworks with methodology sections

---

## Subagent Honesty Rules

Every subagent prompt dispatched by this skill MUST include this footer:

> HONESTY RULES:
> 1. Only extract values explicitly stated in source documents. If ambiguous or missing, leave blank with a one-line reason.
> 2. A wrong answer is 3x worse than a blank answer. When in doubt, leave it blank.
> 3. Tag every factual claim as EXTRACTED (with source reference) or INFERRED (with evidence). Inferred claims will be verified first.

## Reference Files

| File | When to Read |
|------|-------------|
| `references/chapter-templates.md` | Phase 2 — chapter structure recommendations per guidebook type |
| `references/quality-pipeline.md` | Phase 4 — detailed fact-check, legal review, QA procedures |
| `references/build-pipeline.md` | Phase 5 — adapting generate-pdf.py and generate-docx.py |
| `references/improvement-patterns.md` | When improving existing document formats (MOPs, Policy Notes) |
| `references/address-it-csw-framework.md` | CSW guidebooks — the canonical 7-step ADDRESS IT methodology (user's proprietary framework) |
| `references/writing-style-guide.md` | Phase 3 — the proven BARMM guidebook voice: rules, golden paragraphs, anti-patterns, audience profiles |
