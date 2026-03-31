---
name: csw
description: >
  Universal Complete Staff Work (CSW) document generator using the ADDRESS IT methodology
  for any BARMM entity (Bangsamoro Parliament, Ministries, Offices, and Agencies). Use this
  skill whenever the user mentions "CSW", "complete staff work", "completed staff work",
  "prepare a briefer", "write a staff work", "ADDRESS IT", "budget briefer", "csw for [topic]",
  "staff work for [assignment]", "prepare a proposal for [decision-maker]", "write a report
  for [superior]", or needs to produce any formal document that requires supervisor clearance
  and decision-maker approval. Also trigger when the user has a task assigned by a superior
  and needs to produce a comprehensive analysis with recommendation. Also trigger when the
  user says "CSW training", "train staff on CSW", "design a CSW workshop", "CSW competencies",
  "ACSCCRaPATFEE", or wants to build capacity in Complete Staff Work for any BARMM entity.
  Do NOT trigger for legislative briefers specifically requested as "13-section briefer"
  (use /legislative-briefer), standalone policy recommendations (use /policy-recommendation),
  or guidebooks about CSW methodology (use /guidebook-writer).
---

# CSW — Complete Staff Work Engine

Produce publication-ready Complete Staff Work documents following the **ADDRESS IT** 7-step methodology for any BARMM entity. This skill is the universal CSW execution engine — it determines the CSW type, selects the right template, walks through the ADDRESS IT process, and produces the final document with transmittal memorandum.

## How This Skill Relates to Others

This skill is a **hub** that orchestrates specialized skills:

| CSW Type | This skill handles | Delegates to |
|---|---|---|
| Legislative Analysis Briefer | ADDRESS IT Steps 1-2 (context + problem) | `/legislative-briefer` for 13-section document |
| Budget Briefer | Full ADDRESS IT + BB-coded form | `/financial-analyst` for budget data |
| Policy Recommendation | ADDRESS IT Steps 1-3 (context + problem + research) | `/policy-recommendation` for the document |
| Legal Opinion | Full ADDRESS IT + CSW document | `/legal-reviewer` for provision verification |
| Project Proposal | Full ADDRESS IT + CSW document | Standalone |
| Personnel/Admin Action | Full ADDRESS IT + CSW document | Standalone |
| Custom Type | Full ADDRESS IT + generates new template | User defines sections |

For **guidebooks about CSW methodology**, use `/guidebook-writer` instead.

## Verification Protocol

This skill follows the Universal Verification Framework (Prevent → Detect → Confirm).
Read `~/.gemini/skills/fact-checker/references/verification-framework.md` for the full protocol.
Read `~/.gemini/skills/fact-checker/references/source-preload-protocol.md` — MANDATORY: load source text BEFORE writing any citation. No claims from training data when local source exists.
If a claim cannot be verified against loaded source files, mark it `[UNVERIFIED]` — never guess or fabricate. See source-preload-protocol.md Section 4.

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

## Phase 1: INTAKE — Assignment Interview

Before starting any ADDRESS IT step, conduct this interview to understand the assignment. Skip questions already answered in the user's prompt.

### Required Inputs

1. **Assignment** — What task or issue has been assigned? (verbatim if possible)
2. **Assigning Authority** — Who assigned this? (MP, Minister, Director, Chief Minister, Committee Chair)
3. **BARMM Entity** — Which entity?
   - Bangsamoro Parliament (BTA) — committee, office, or individual MP
   - Ministry (e.g., MBHTE, MOH, MAFAR, MILG, MENRE)
   - Office or Agency (e.g., OOBC, BPDA, MOTC, BDA)
4. **Decision-Maker** — Who will approve the final CSW? (may differ from assigning authority)
5. **CSW Type** — What type of output is expected?

   | Code | CSW Type | Template |
   |------|----------|----------|
   | LA | Legislative Analysis Briefer | 13-section format (delegate to `/legislative-briefer`) |
   | BB | Budget Briefer | BB-coded sections (read `references/budget-briefer-template.md`) |
   | PR | Policy Recommendation | Bardach format (delegate to `/policy-recommendation`) |
   | LO | Legal Opinion / Review | LO-coded sections |
   | PP | Project Proposal | PP-coded sections |
   | PA | Personnel / Admin Action | PA-coded sections |
   | SV | Supervision System | SV-coded sections (read `references/supervision-system-template.md`) |
   | GN | General CSW | Generic ADDRESS IT template |
   | CU | Custom (user-defined) | Generate new template |

6. **Deadline** — When is it due?
7. **ADDRESS IT Progress** — Has the user already completed any steps? (They may arrive mid-process with research already done, or with a problem already defined.)

### Domain Context Loading

After the interview, invoke `/bangsamoro` to load domain context — verified facts about BARMM governance, officials, BOL provisions, and the BDP framework.

---

## Phase 2: EXECUTE — The ADDRESS IT Process

Walk through the 7 ADDRESS IT steps. Read `${GEMINI_SKILL_DIR}/references/address-it-framework.md` for detailed sub-steps. Skip steps the user has already completed.

At each step, produce a brief artifact (not the final document — these are working notes that feed into the final CSW).

### Step 1: Analyze the Context (A)
- Understand the assignment's purpose and desired outcomes
- Assess the office's function and the staff member's role
- Identify stakeholders (primary and secondary)
- Examine internal/external factors (PESTEL where applicable)
- Review relevant laws, policies, regulations (BOL, BAAs, national laws)
- Gather preliminary data
- **Artifact**: Context Analysis Brief (1-2 pages)

### Step 2: Define and Deliberate the Problem (DD)
- Articulate the problem or need statement
- Identify root causes (5 Whys, fishbone diagram where appropriate). Use the `/excalidraw` skill for fishbone diagrams, process flows, and other visual analyses. Render to PNG and embed inline. For visual executive summaries and decision briefs, use `/visualize` to generate self-contained HTML visualizations that can be converted to PNG for embedding.
- Assess consequences of inaction
- Establish scope and SMART objectives
- **Artifact**: Problem Statement (half-page, validated with user)

### Step 3: Research Needed Information (R)
- Develop research plan based on problem statement
- Identify and gather from relevant sources (government data, academic, stakeholder inputs)
- Conduct literature review where applicable
- Analyze and synthesize findings
- Identify best practices and potential solutions
- **Artifact**: Research Brief (2-5 pages depending on complexity)

### Step 4: Explore Options (E)
- Generate options based on research findings
- Evaluate against criteria: feasibility, effectiveness, efficiency, sustainability, alignment
- Conduct impact analysis and cost-benefit analysis where applicable
- Prioritize and prepare recommendation
- **Artifact**: Options Matrix (table comparing 2-4 options)

### Step 5: Submit Proposal or Report (SS)
- Select the appropriate CSW template based on type (from Phase 1)
- Fill in all coded sections following the template's guide notes
- Write executive summary last
- Include implementation plan
- Conclude with call to action
- **Artifact**: Complete CSW Document (the main deliverable)

### Step 6: Sustain Implementation (S)
- This step applies AFTER the decision-maker approves
- Prepare implementation action plan if the CSW recommends action
- Include in the document as an appendix or implementation section
- **Artifact**: Implementation Plan (if applicable — included in CSW document)

### Step 7: Iterate and Improve (IT)
- Include M&E framework or review mechanism in the CSW
- Define success metrics and review timeline
- **Artifact**: M&E Section (included in CSW document)

### Step Adaptations by Complexity

| Complexity | Steps to emphasize | Steps to abbreviate |
|---|---|---|
| **Routine** (straightforward, low-risk) | Steps 1, 5 | Steps 3-4 (brief research, obvious recommendation) |
| **Standard** (moderate complexity) | Steps 1-5 | Steps 6-7 (include but don't over-elaborate) |
| **Complex** (high-stakes, multi-stakeholder) | All 7 steps fully | None — every step matters |

---

## Phase 3: FORMAT — Template Selection and Document Production

### Coded Section Pattern

All CSW templates use a consistent coded section structure inspired by the Budget Briefer (BB-Ver0):

```
| CODE | SECTION | GUIDE / NOTES |
|------|---------|---------------|
| XX01 | Section Name | CSW Section Objective: [purpose of this section]
|      |              | CSW Guide / Notes for this Section: [instructions]
|      |              | Review Questions for this Section: [scrutiny questions] |
```

Where XX = the type code (BB, LA, LO, PP, PA, GN).

### Template Library

Read the appropriate template from `${GEMINI_SKILL_DIR}/references/`:

| CSW Type | Template File |
|---|---|
| Budget Briefer (BB) | `references/budget-briefer-template.md` |
| Legal Opinion (LO) | `references/legal-opinion-template.md` |
| Project Proposal (PP) | `references/project-proposal-template.md` |
| General CSW (GN) | `references/general-csw-template.md` |
| Supervision System (SV) | `references/supervision-system-template.md` |
| Custom (CU) | Generate new template following the coded pattern |

For types that delegate (LA → `/legislative-briefer`, PR → `/policy-recommendation`), this skill runs ADDRESS IT Steps 1-3 to prepare the context, then hands off to the specialized skill with the research artifacts.

### Creating Custom Templates

When the user needs a CSW type not in the library:

1. Ask the user what sections are needed
2. Generate coded sections (CU01, CU02, etc.) with section objectives, guide notes, and review questions
3. Save the new template to `references/` for future reuse
4. Fill the template following ADDRESS IT

---

## Phase 4: TRANSMIT — Transmittal and Quality

### Quality Pipeline

Before finalizing, run:
1. **Fact-check** (invoke `/fact-checker`) — verify names, titles, dates, legislation references
2. **Legal review** (invoke `/legal-reviewer`) — verify any quoted legal provisions
3. **Consistency check** — ensure all coded sections are filled, no placeholders remain

### Severity-Based Fix Workflow
- **CRITICAL** (wrong names, incorrect legal citations, misquoted BOL): Must fix before transmittal
- **MINOR** (style, formatting): Should fix but does not block

### Transmittal Memorandum

Generate a transmittal memo wrapping the CSW for supervisor clearance. Read `${GEMINI_SKILL_DIR}/assets/transmittal-memo-template.md` for the format.

The transmittal memo includes:
- To: [Supervisor/Decision-Maker]
- From: [Staff Member/Office]
- Date
- Subject: [CSW Title]
- Reference: [Assignment reference, if any]
- Brief description of the CSW and recommended action
- Attachments list

### Output Format

Produce the CSW document in markdown for review. When the user approves, generate DOCX using the `/docx` skill for formal submission.

---

## Phase 5: TRAIN — CSW Training Mode

When the user asks to design CSW training, assess staff competencies, or build CSW capacity, switch to Training Mode. This mode uses the **ACSCCRaPATFEE** competency framework — 12 competencies the user developed for CSW practitioners.

### Training Mode Triggers
- "CSW training", "train staff on CSW", "design a CSW workshop"
- "CSW competencies", "ACSCCRaPATFEE", "assess CSW skills"
- "capacity building for CSW", "CSW onboarding"

### Training Mode Workflow

1. **Needs Assessment** — Identify the audience (Parliament staff, MOA staff, LGU officials), their current CSW proficiency level, and the training objectives
2. **Training Design** — Read `${GEMINI_SKILL_DIR}/references/csw-training-design.md` for the session blueprint. Adapt the ADDRESS IT training to the audience's context.
3. **Competency Framework** — Read `${GEMINI_SKILL_DIR}/references/csw-competencies.md` for the 12 ACSCCRaPATFEE competencies with indicators and rubrics. Use for pre/post assessment design.
4. **Materials Production** — Delegate to `/training-assistant` to generate the full training package (facilitator guide, participant handouts, evaluation forms, pre/post tests)
5. **Assessment Tools** — Generate competency assessment rubrics based on the 5-level scale (Limited → Developing → Proficient → Advanced → Expert)

### The 12 ACSCCRaPATFEE Competencies (Quick Reference)

| # | Competency | Primary ADDRESS IT Steps |
|---|---|---|
| 1 | **A**nalytical and Critical Thinking | Steps 1, 3 |
| 2 | **C**reativity and Innovation | Step 4 |
| 3 | **S**trategic Thinking | Steps 1, 4, 7 |
| 4 | **C**ommunication | Steps 5, 6 |
| 5 | **C**ollaboration and Teamwork | Steps 2, 6 |
| 6 | **R**esearch and **A**nalysis | Step 3 |
| 7 | **P**roblem-Solving and Decision Making | Steps 2, 4 |
| 8 | **A**ttention to Details and Quality | Step 5 |
| 9 | **T**ime and Attention Management | All steps |
| 10 | **F**lexibility and Adaptability | Steps 6, 7 |
| 11 | **E**motional Intelligence and Accountability | Steps 2, 6 |
| 12 | **E**thics and Integrity | All steps |

Each competency includes 3-tier indicators (Simple/Intermediate/Complex) and 5-level rubrics. Read the full reference for training design and assessment.

---

## Reference Files

| File | When to Read |
|------|-------------|
| `references/address-it-framework.md` | Phase 2 — detailed ADDRESS IT sub-steps for each of the 7 steps |
| `references/budget-briefer-template.md` | When CSW type is Budget Briefer (BB) |
| `references/legal-opinion-template.md` | When CSW type is Legal Opinion (LO) |
| `references/project-proposal-template.md` | When CSW type is Project Proposal (PP) |
| `references/general-csw-template.md` | When CSW type is General (GN) or starting point for Custom |
| `references/supervision-system-template.md` | When CSW type is Supervision System (SV) |
| `references/csw-competencies.md` | Phase 5 — 12 ACSCCRaPATFEE competencies with indicators and rubrics |
| `references/csw-training-design.md` | Phase 5 — training session blueprint (upgraded from 5-step to ADDRESS IT) |
| `references/csw-assessment-tool.md` | Phase 5 — 7-level competency self-assessment instrument for pre/post training evaluation |
| `assets/transmittal-memo-template.md` | Phase 4 — transmittal memorandum format |

## Gotchas

- BOL article numbers are the #1 fabrication target — always verify against ~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/
- BAA numbers are the #2 fabrication target — verify against ~/Vault/bangsamoro/bangsamoro-laws/index.md
- Use BARMM ministry abbreviations (MFBM not DBM, MOLE not DOLE, MBHTE not DepEd, MILG not DILG) — never national equivalents
- Mas Matatag na Bangsamoro Agenda (2026-2028) replaces 12-Point Priority Agenda — update all references
- Never cite guidebooks as primary sources — trace back to enacted law (BAA, RA, BOL)
- A wrong BAA number, BOL article, or official title is 3x worse than writing [UNVERIFIED]. When in doubt, mark it.
- ADDRESS IT methodology has 7 steps — never skip or merge steps
- The recommending authority chain depends on the BARMM entity type (Ministry vs Office vs Agency)
- Budget implications must reference BAA 84 and the current Budget Call Memorandum

## Subagent Honesty Rules

Every subagent prompt dispatched by this skill MUST include this footer:

> HONESTY RULES:
> 1. Only extract values explicitly stated in source documents. If ambiguous or missing, leave blank with a one-line reason.
> 2. A wrong answer is 3x worse than a blank answer. When in doubt, leave it blank.
> 3. Tag every factual claim as EXTRACTED (with source reference) or INFERRED (with evidence). Inferred claims will be verified first.
