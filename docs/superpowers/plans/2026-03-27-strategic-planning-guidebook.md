# Strategic Planning Guidebook Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Write the complete *Strategic Planning Guidebook for the Bangsamoro Government* — a practitioner's guide to the 10-Point Strategic Planning Framework for BARMM MOAs.

**Architecture:** 12 substantive chapters (Introduction + 10 framework points + Consolidation), plus front matter, glossary, and 7 appendices. Each framework chapter produces a modular template that rolls up into a complete MOA Strategic Plan. Markdown source files in `guidebooks/strategic-planning/`, following the same conventions as the CSW guidebook.

**Tech Stack:** Markdown content, `/bangsamoro` + `/guidebook-writer` + `/citation` skills, Feliciano 10th Ed. footnotes.

**Design spec:** `docs/superpowers/specs/2026-03-27-strategic-planning-guidebook-design.md`

**Primary source material:** `~/apps/e-Bangsamoro/.claude/skills/devwork/assets/architecture/e-Ministry/e-Planning/` (12 architecture files, ~26,700 lines)

**Secondary sources:**
- BOL (RA 11054): `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/`
- BDP 2023-2028: `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/`
- BAA 13: `legislation/baas/BAA-13.md`
- BAA 84: `legislation/baas/BAA-84.md`
- BAA 85: `legislation/baas/BAA-85.md`
- BARMM Officials: `~/.claude/skills/bangsamoro/references/barmm-officials-2025-2026.md`

**Existing guidebook reference (for voice/format consistency):** `guidebooks/csw/` — use 00-table-of-contents.md, 00b-about.md, 00c-author.md, 01-introduction.md as structural templates.

---

## Pre-Implementation Setup

### Task 0: Create directory and invoke domain context

**Files:**
- Create: `guidebooks/strategic-planning/` (directory)

- [ ] **Step 1: Invoke `/bangsamoro` skill** to load BARMM domain context (officials, governance structure, BOL provisions). This context persists for all subsequent chapter writing.

- [ ] **Step 2: Create the guidebook directory**

```bash
mkdir -p guidebooks/strategic-planning
```

- [ ] **Step 3: Commit scaffold**

```bash
git add guidebooks/strategic-planning
git commit -m "Add strategic-planning guidebook directory"
```

---

## Front Matter

### Task 1: Table of Contents

**Files:**
- Create: `guidebooks/strategic-planning/00-table-of-contents.md`

**Source:** Design spec Section 4 (Chapter Map)

- [ ] **Step 1: Write the TOC**

Follow the CSW guidebook TOC format (`guidebooks/csw/00-table-of-contents.md`). Include:
- Full title and subtitle
- All 12 chapters with section/subsection numbering using `&emsp;` indentation
- Glossary
- All 7 appendices (A-G)

Section numbering within each chapter follows this pattern (matching the standard chapter anatomy from the design spec):
- X.1 Purpose
- X.2 Key Concepts
- X.3 Step-by-Step Instructions (with sub-steps)
- X.4 Worked Example
- X.5 For Decision-Makers
- X.6 Common Pitfalls
- X.7 Template: [Template Name]
- X.8 Quality Checklist

Chapter 1 (Introduction) and Chapter 12 (Consolidation) have custom section structures — see Tasks 3 and 14 for their outlines.

- [ ] **Step 2: Review** — verify all 12 chapters, glossary, and 7 appendices are listed. Cross-check against design spec Chapter Map table.

### Task 2: About and Author pages

**Files:**
- Create: `guidebooks/strategic-planning/00b-about.md`
- Create: `guidebooks/strategic-planning/00c-author.md`

- [ ] **Step 1: Write the About page** (`00b-about.md`)

Follow the CSW pattern (`guidebooks/csw/00b-about.md`). Include:
- **Purpose** — what this guidebook does (practitioner's guide to the 10-Point Framework; produces modular documents that assemble into an MOA Strategic Plan)
- **Intended Audience** — three tiers:
  1. Planning Officers, Budget Officers, M&E Officers (primary — the drafters)
  2. Ministers, Executive Directors, Division Chiefs (secondary — decision-makers)
  3. BPDA staff (tertiary — reviewers and certifiers)
- **How to Use This Guidebook** — reading paths for:
  - First-time users (read sequentially)
  - Experienced planners updating a specific component (jump to relevant chapter)
  - Decision-makers (read "For Decision-Makers" callouts + Ch 12)
  - BPDA reviewers (Ch 12 submission workflow + appendix templates)
- **Conventions Used** — bold, italic, callout box types:
  - **TIP** — practical advice
  - **CAUTION** — common mistakes
  - **BANGSAMORO NOTE** — BARMM-specific adaptations
  - **FOR DECISION-MAKERS** — what leaders need to decide/approve
- **Relationship to Other BARMM Guidebooks** — links to CSW Guidebook (analytical process), Bill Drafting Guidebook (legislative output), and planned BAA 84 Budget System guidebook (budget forms)

- [ ] **Step 2: Write the Author page** (`00c-author.md`)

Reuse the author bio from `guidebooks/csw/00c-author.md` verbatim — same author, same bio.

- [ ] **Step 3: Commit front matter**

```bash
git add guidebooks/strategic-planning/00-table-of-contents.md guidebooks/strategic-planning/00b-about.md guidebooks/strategic-planning/00c-author.md
git commit -m "Add strategic-planning guidebook front matter"
```

---

## Chapter Writing

**Standard procedure for every framework chapter (Tasks 4-13):**

Before writing each chapter:
1. Read the corresponding architecture source file in full (path specified per task)
2. Extract the methodology: frameworks, workflows, decision logic, validation rules, domain knowledge
3. Strip away: UI components, API endpoints, TypeScript types, database models, React patterns, Ambient AI references
4. Translate into practitioner language using the standard chapter anatomy

After writing each chapter:
1. Invoke `/citation` to add Feliciano 10th Ed. footnotes for all legal references (BOL articles, BAAs, BDP chapters, national laws)
2. Verify all BARMM-specific references (ministry names, official titles, BAA numbers) against authoritative sources
3. Commit the chapter

### Task 3: Chapter 1 — Introduction to Strategic Planning in BARMM

**Files:**
- Create: `guidebooks/strategic-planning/01-introduction.md`

**Source files:**
- `~/apps/e-Bangsamoro/.claude/skills/devwork/assets/architecture/e-Ministry/e-Planning/arch-mod-planning.md` (module overview)
- `~/apps/e-Bangsamoro/.claude/skills/devwork/assets/architecture/e-Ministry/e-Planning/arch-ministerial-planning.md` (master framework)
- `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` (legal authority)
- `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/` (BDP context)

**Reference for voice/format:** `guidebooks/csw/01-introduction.md`

- [ ] **Step 1: Read source files** — Read `arch-mod-planning.md` in full and the first 200 lines of `arch-ministerial-planning.md` for module overview, purpose, legal/policy alignment, and access control.

- [ ] **Step 2: Write the Introduction chapter**

Sections (custom structure — not the standard chapter anatomy):
1. **Opening hook** — similar to CSW intro ("Your Minister just asked for a strategic plan..."). Ground the reader in a concrete scenario.
2. **The Problem This Guidebook Solves** — MOAs lack a standardized planning process. Plans are inconsistent, misaligned with BDP, and don't connect to budgets or M&E.
3. **What Is Strategic Planning in BARMM?** — define it in context. Reference BOL mandate, BAA 13 (Administrative Code), BDP 2023-2028 requirement for MOA alignment.
4. **The 10-Point Strategic Planning Framework** — overview diagram/table of all 10 points with one-line descriptions. Show the visual flow: Foundation (1-3) → Analysis (4-5) → Design (6-7) → Execution (8-9) → Accountability (10).
5. **What You Will Produce** — list of 10 template outputs + the consolidated MOA Strategic Plan. Reference Appendix D (blank templates) and Appendix E (worked example).
6. **Who Does What** — role matrix table:
   - Planning Officer: drafts Points 1-7, consolidates all
   - Budget Officer: leads Points 8-9 (resource/annual financial planning)
   - M&E Officer: leads Point 10 (RBME)
   - Minister/ED: approves at each stage (reference "For Decision-Makers" callouts)
   - BPDA: reviews and certifies completed plan
   - MFBM: reviews budget feasibility
7. **The Planning Calendar** — when each point typically happens in the BARMM fiscal year (Q1: strategic review and legal alignment; Q2: stakeholder/strategy/ToC; Q3: PPA and resource planning; Q4: annual work plan and M&E setup).
8. **How to Read This Guidebook** — reading paths (sequential for first-time, reference for updates, decision-maker track).

- [ ] **Step 3: Invoke `/citation`** — add Feliciano footnotes for BOL, BAA 13, BDP references.

- [ ] **Step 4: Commit**

```bash
git add guidebooks/strategic-planning/01-introduction.md
git commit -m "Add Ch 1: Introduction to Strategic Planning in BARMM"
```

---

### Task 4: Chapter 2 — Establishing Your Legal Mandate (Point 1)

**Files:**
- Create: `guidebooks/strategic-planning/02-chapter-01.md`

**Source file:** `~/apps/e-Bangsamoro/.claude/skills/devwork/assets/architecture/e-Ministry/e-Planning/arch-subm-planning-01-legal-alignment.md` (3,542 lines)

**Secondary sources:**
- BOL (RA 11054): `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/`
- BAA 13: `legislation/baas/BAA-13.md`

- [ ] **Step 1: Read source file** — Read `arch-subm-planning-01-legal-alignment.md` in full. Extract: 7-tier legal hierarchy, mandate mapping methodology, legal basis identification workflow, validation rules.

- [ ] **Step 2: Write the chapter** following the standard chapter anatomy:

**2.1 Purpose** — Why legal alignment comes first. Every MOA's authority derives from law. A plan without legal basis is unenforceable.

**2.2 Key Concepts:**
- The 7-tier BARMM legal hierarchy: (1) 1987 Philippine Constitution, (2) BOL / RA 11054, (3) Bangsamoro Administrative Code / BAA 13, (4) Bangsamoro Autonomy Acts, (5) Applicable national laws, (6) Executive issuances (Executive Orders, Administrative Orders, Memorandum Circulars), (7) Jurisprudence
- Mandate vs. function vs. activity — hierarchy of authority
- Explicit vs. implied powers under BOL Article V

**2.3 Step-by-Step Instructions:**
1. Identify your MOA's creating law (which BAA, BOL article, or executive issuance established your office)
2. List all legal provisions that grant your MOA authority (enumerate from each tier)
3. Map provisions to planning domains (e.g., "BAA 85 Sec. 12 → education scholarship programs")
4. Identify gaps — areas where your MOA operates without clear legal basis (flag for legal review)
5. Complete the Legal Mandate Matrix template

**2.4 Worked Example** — Use a realistic BARMM ministry (e.g., MENRE) walking through Steps 1-5. Show the actual BOL articles (Art. IX Sec. 1-2 on environment), relevant BAAs, and how they map to planning domains.

**2.5 For Decision-Makers** — Callout box: Ministers/EDs should review the Legal Mandate Matrix to confirm: (a) no unauthorized functions are being planned, (b) no mandated functions are missing from the plan, (c) legal basis is current (check for new BAAs passed since last plan).

**2.6 Common Pitfalls:**
- Planning activities without legal authority
- Citing repealed or superseded legislation
- Ignoring national laws that apply to BARMM (e.g., procurement law, COA rules)
- Conflating "what we've always done" with "what the law mandates"

**2.7 Template: Legal Mandate Matrix** — Table format:

| Legal Source | Provision | Mandate/Authority | Planning Domain | Status |
|-------------|-----------|-------------------|-----------------|--------|
| BOL Art. IX Sec. 1 | Environmental protection | Mandatory | Environment & Natural Resources | Active |
| BAA No. XX | ... | ... | ... | ... |

**2.8 Quality Checklist:**
- [ ] All 7 tiers of the legal hierarchy reviewed
- [ ] Creating law of the MOA identified and cited
- [ ] Every planning domain has at least one legal basis
- [ ] No expired, repealed, or superseded laws cited
- [ ] Minister/ED has reviewed and confirmed the matrix

- [ ] **Step 3: Invoke `/citation`** — Feliciano footnotes for all BOL articles, BAAs, and national laws cited.

- [ ] **Step 4: Commit**

```bash
git add guidebooks/strategic-planning/02-chapter-01.md
git commit -m "Add Ch 2: Establishing Your Legal Mandate (Point 1)"
```

---

### Task 5: Chapter 3 — Aligning with the Bangsamoro Development Plan (Point 2)

**Files:**
- Create: `guidebooks/strategic-planning/03-chapter-02.md`

**Source file:** `~/apps/e-Bangsamoro/.claude/skills/devwork/assets/architecture/e-Ministry/e-Planning/arch-subm-planning-02-bdp-alignment.md` (2,738 lines)

**Secondary source:** `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/` (BDP 2023-2028, 15 chapters)

- [ ] **Step 1: Read source file** — Extract: BDP's 6 Development Goals, 8 Key Strategies, goal-to-sector mapping, alignment methodology, contribution statement format.

- [ ] **Step 2: Write the chapter** following the standard chapter anatomy:

**3.1 Purpose** — MOA plans must contribute to the Bangsamoro Development Plan. This chapter maps your legal mandates (from Ch 2) to BDP goals and strategies.

**3.2 Key Concepts:**
- The 6 BDP Development Goals (list all 6 with descriptions)
- The 8 Key Strategies (list all 8)
- Goal-to-sector mapping — which ministries naturally align with which goals
- Primary vs. contributory alignment — your MOA may primarily serve one goal but contribute to others
- BDP alignment is not optional — it's the basis for budget justification

**3.3 Step-by-Step Instructions:**
1. Read the BDP Quick Reference (Appendix B) to understand all 6 goals and 8 strategies
2. Identify your MOA's primary BDP goal(s) — which goal does your mandate most directly serve?
3. Identify contributory goals — which other goals does your work support indirectly?
4. For each aligned goal, write a Contribution Statement: "Through [mandate], [MOA] contributes to BDP Goal [X] by [specific mechanism]"
5. Map to Key Strategies — which of the 8 strategies does your work employ?
6. Complete the BDP Alignment Map template

**3.4 Worked Example** — Same ministry as Ch 2 (MENRE or similar) continuing the planning process. Show actual BDP goal text and how environmental mandates map.

**3.5 For Decision-Makers** — Review BDP alignment for completeness and accuracy. Ensure the MOA isn't claiming alignment where none exists (credibility risk in BPDA review).

**3.6 Common Pitfalls:**
- Forcing alignment where none exists (not every activity maps to BDP — that's ok, it maps to legal mandate)
- Aligning only at the goal level without specifying the strategy or mechanism
- Ignoring the BDP's cross-cutting themes (gender, peace, environment)
- Using the BDP 2020-2022 instead of the current 2023-2028 plan

**3.7 Template: BDP Alignment Map** — Table format:

| Legal Mandate (from Ch 2) | BDP Goal | BDP Strategy | Contribution Statement | Alignment Type |
|--------------------------|----------|-------------|----------------------|----------------|
| Environmental protection (BOL Art. IX) | Goal 4: ... | Strategy 3: ... | Through environmental regulation, MENRE contributes to... | Primary |

**3.8 Quality Checklist:**
- [ ] All legal mandates from the Legal Mandate Matrix have been reviewed for BDP alignment
- [ ] Primary BDP goal(s) identified with specific contribution statements
- [ ] Contributory goals identified where applicable
- [ ] Key strategies mapped
- [ ] No false or forced alignments
- [ ] Current BDP (2023-2028) used, not the previous plan

- [ ] **Step 3: Invoke `/citation`** — Feliciano footnotes for BDP chapters and sections cited.

- [ ] **Step 4: Commit**

```bash
git add guidebooks/strategic-planning/03-chapter-02.md
git commit -m "Add Ch 3: Aligning with the Bangsamoro Development Plan (Point 2)"
```

---

### Task 6: Chapter 4 — Mapping to the Priority Agenda (Point 3)

**Files:**
- Create: `guidebooks/strategic-planning/04-chapter-03.md`

**Source file:** `~/apps/e-Bangsamoro/.claude/skills/devwork/assets/architecture/e-Ministry/e-Planning/arch-subm-planning-03-priority-agenda.md` (2,053 lines)

- [ ] **Step 1: Read source file** — Extract: 12-Point Enhanced Priority Agenda content, alignment methodology, gap analysis approach, government-wide coverage analysis.

- [ ] **Step 2: Write the chapter** following the standard chapter anatomy:

**4.1 Purpose** — The Chief Minister's 12-Point Enhanced Priority Agenda is the current administration's political commitment. MOA plans must show how they contribute.

**4.2 Key Concepts:**
- The 12-Point Enhanced Priority Agenda (list all 12 with brief descriptions)
- Difference between BDP alignment (long-term development) and Priority Agenda alignment (current administration priorities)
- Direct vs. enabling contributions — some MOAs directly implement a priority; others enable it through support functions
- Not every MOA maps to every priority — but every MOA should map to at least one

**4.3 Step-by-Step Instructions:**
1. Review all 12 priorities (reference Appendix C for full text)
2. Map your MOA's mandates to relevant priorities
3. For each mapped priority, describe your MOA's specific contribution (direct or enabling)
4. Identify any priorities where your MOA could contribute but currently does not (gap analysis)
5. Complete the Priority Agenda Alignment Sheet

**4.4 Worked Example** — continuing with the same ministry.

**4.5 For Decision-Makers** — priority agenda alignment is politically significant. Ministers should ensure the alignment is defensible and not overstated.

**4.6 Common Pitfalls:**
- Claiming alignment with every priority (not credible)
- Conflating "we want to help" with "we have mandate and capacity to contribute"
- Ignoring the priority agenda entirely (signals political misalignment)

**4.7 Template: Priority Agenda Alignment Sheet**

| Priority # | Priority Description | MOA Contribution | Contribution Type | Supporting Mandate |
|-----------|---------------------|-----------------|-------------------|-------------------|
| 3 | ... | ... | Direct | BAA No. XX |

**4.8 Quality Checklist:**
- [ ] All 12 priorities reviewed (not just the obvious ones)
- [ ] Each claimed contribution has a supporting legal mandate
- [ ] Contribution type (direct/enabling) correctly classified
- [ ] Gap analysis completed — unaddressed priorities acknowledged
- [ ] Alignment is defensible and not overstated

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

```bash
git add guidebooks/strategic-planning/04-chapter-03.md
git commit -m "Add Ch 4: Mapping to the Priority Agenda (Point 3)"
```

---

### Task 7: Chapter 5 — Analyzing Your Stakeholders (Point 4)

**Files:**
- Create: `guidebooks/strategic-planning/05-chapter-04.md`

**Source file:** `~/apps/e-Bangsamoro/.claude/skills/devwork/assets/architecture/e-Ministry/e-Planning/arch-subm-planning-04-stakeholder.md` (2,902 lines)

- [ ] **Step 1: Read source file** — Extract: stakeholder categories (CSOs, LGUs, development partners, communities, other MOAs), power/interest matrix, engagement strategy design, dual-mode workflow.

- [ ] **Step 2: Write the chapter** following the standard chapter anatomy:

**5.1 Purpose** — Identify everyone affected by or able to influence your programs. Stakeholder analysis prevents blind spots and builds support.

**5.2 Key Concepts:**
- Stakeholder categories in BARMM: (a) BTA Parliament and committees, (b) other MOAs, (c) LGUs (provinces, cities, municipalities, barangays), (d) CSOs and NGOs, (e) development partners (international organizations, donor agencies), (f) private sector, (g) traditional/religious leaders, (h) affected communities and beneficiaries
- Power/Interest matrix: High Power-High Interest (manage closely), High Power-Low Interest (keep satisfied), Low Power-High Interest (keep informed), Low Power-Low Interest (monitor)
- Engagement levels: Inform, Consult, Involve, Collaborate, Empower

**5.3 Step-by-Step Instructions:**
1. List all potential stakeholders using the 8 categories above
2. For each stakeholder, assess their power (ability to influence) and interest (degree of concern)
3. Plot on the Power/Interest matrix
4. Define engagement strategy for each quadrant
5. Identify key relationships — which stakeholders are critical for plan approval or implementation?
6. Complete the Stakeholder Register & Engagement Plan

**5.4 Worked Example** — continuing with the same ministry. Show real BARMM stakeholders (LGUs, relevant CSOs, development partners active in BARMM).

**5.5 For Decision-Makers** — review stakeholder list for political completeness. Are traditional leaders included? Are affected communities represented, not just institutional partners?

**5.6 Common Pitfalls:**
- Listing only institutional stakeholders (ignoring communities and beneficiaries)
- Treating all stakeholders the same (no differentiated engagement)
- Forgetting Parliament — the BTA committees with oversight over your MOA
- Not updating stakeholder analysis when the political landscape changes

**5.7 Template: Stakeholder Register & Engagement Plan**

| Stakeholder | Category | Power | Interest | Quadrant | Engagement Strategy | Key Contact | Frequency |
|------------|----------|-------|----------|----------|-------------------|------------|-----------|

**5.8 Quality Checklist:**
- [ ] All 8 stakeholder categories considered
- [ ] Power and interest assessed for each stakeholder
- [ ] Engagement strategy defined per quadrant
- [ ] Communities and beneficiaries included (not just institutions)
- [ ] BTA Parliament committees included
- [ ] Traditional/religious leaders considered where relevant

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

```bash
git add guidebooks/strategic-planning/05-chapter-04.md
git commit -m "Add Ch 5: Analyzing Your Stakeholders (Point 4)"
```

---

### Task 8: Chapter 6 — Defining Your Strategic Direction (Point 5)

**Files:**
- Create: `guidebooks/strategic-planning/06-chapter-05.md`

**Source file:** `~/apps/e-Bangsamoro/.claude/skills/devwork/assets/architecture/e-Ministry/e-Planning/arch-subm-planning-05-strategy.md` (1,705 lines)

- [ ] **Step 1: Read source file** — Extract: Vision/Mission/Values framework, SWOT analysis methodology, problem statement construction, SMART strategic objectives, strategy formulation.

- [ ] **Step 2: Write the chapter** following the standard chapter anatomy:

**6.1 Purpose** — Define where your MOA is going (Vision), why it exists (Mission), what it stands for (Values), and what it will achieve (Strategic Objectives). This is where legal mandates and BDP alignment become an actionable direction.

**6.2 Key Concepts:**
- Vision statement — aspirational, future-focused (5-10 years)
- Mission statement — what your MOA does, for whom, and how
- Core values — principles guiding behavior and decisions (include BARMM moral governance values)
- SWOT Analysis — Strengths, Weaknesses (internal), Opportunities, Threats (external)
- Problem statements — structured articulation of the issues your MOA must address
- Strategic objectives — SMART (Specific, Measurable, Achievable, Relevant, Time-bound) goals that bridge the gap between current state and vision

**6.3 Step-by-Step Instructions:**
1. Draft or review your MOA's Vision statement
2. Draft or review your MOA's Mission statement
3. Identify core values (align with BOL preamble and BARMM governance principles)
4. Conduct SWOT analysis with your planning team
5. Formulate problem statements from the SWOT
6. Write 3-7 Strategic Objectives that are SMART
7. Complete the Vision-Mission-Values Statement and Strategic Objectives document

**6.4 Worked Example** — continuing with the same ministry. Show a realistic Vision, Mission, SWOT, and strategic objectives.

**6.5 For Decision-Makers** — the Vision and Mission are the Minister/ED's prerogative. Staff draft, leaders decide. Strategic objectives must be approved before PPA planning begins.

**6.6 Common Pitfalls:**
- Vision statements that are generic and could belong to any organization
- Mission statements that list activities instead of purpose
- SWOT analysis that is a brainstorm dump with no prioritization
- Strategic objectives that are not measurable or time-bound
- Confusing objectives (outcomes) with activities (outputs)

**6.7 Template: Vision-Mission-Values Statement + Strategic Objectives**

Two-part template:
- Part A: Vision, Mission, Core Values (narrative format)
- Part B: Strategic Objectives table:

| Objective # | Strategic Objective | BDP Goal Alignment | Baseline | Target | Timeline |
|------------|--------------------|--------------------|----------|--------|----------|

**6.8 Quality Checklist:**
- [ ] Vision is aspirational and BARMM-specific
- [ ] Mission describes purpose, audience, and approach
- [ ] Values reflect BARMM governance principles
- [ ] SWOT completed with internal and external factors
- [ ] Each strategic objective passes the SMART test
- [ ] Objectives link back to BDP goals (from Ch 3)
- [ ] Minister/ED has approved Vision, Mission, and Objectives

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

```bash
git add guidebooks/strategic-planning/06-chapter-05.md
git commit -m "Add Ch 6: Defining Your Strategic Direction (Point 5)"
```

---

### Task 9: Chapter 7 — Building Your Theory of Change (Point 6)

**Files:**
- Create: `guidebooks/strategic-planning/07-chapter-06.md`

**Source file:** `~/apps/e-Bangsamoro/.claude/skills/devwork/assets/architecture/e-Ministry/e-Planning/arch-subm-planning-06-toc.md` (1,485 lines)

- [ ] **Step 1: Read source file** — Extract: results chain (Impact → Outcomes → Outputs → Activities → Inputs), causal logic, assumptions and risks, theory of change narrative format.

- [ ] **Step 2: Write the chapter** following the standard chapter anatomy:

**7.1 Purpose** — Articulate HOW your MOA's activities lead to the desired impact. The Theory of Change makes the causal logic explicit — if we do X, then Y happens, assuming Z.

**7.2 Key Concepts:**
- Results chain: Impact (long-term change) → Outcomes (medium-term results) → Outputs (direct products) → Activities (what you do) → Inputs (what you use)
- Causal pathways — the logical links between levels
- Assumptions — conditions that must hold for the causal pathway to work
- Risks — factors that could break the causal pathway
- The difference between a ToC and a logframe (ToC explains WHY; logframe tracks WHAT)

**7.3 Step-by-Step Instructions:**
1. Start with Impact — what long-term change does your MOA contribute to? (Link to BDP Goals from Ch 3)
2. Define Outcomes — what medium-term results must happen to achieve the impact? (Link to Strategic Objectives from Ch 6)
3. Define Outputs — what tangible products/services must your MOA produce?
4. List Activities — what will your staff actually do?
5. Identify Inputs — what resources are needed? (Preview for Ch 9, Resource Planning)
6. Draw the causal pathways — connect each level with "if...then" logic
7. Identify assumptions at each level — what must be true for the link to work?
8. Identify risks — what could break the link?
9. Write the Theory of Change Narrative (1-2 pages explaining the diagram in prose)
10. Complete the Theory of Change Diagram + Narrative template

**7.4 Worked Example** — continuing with the same ministry. Show a complete results chain with diagram and narrative.

**7.5 For Decision-Makers** — the ToC is the intellectual foundation of the entire plan. If the causal logic is wrong, the plan will fail regardless of execution quality. Leaders should challenge assumptions.

**7.6 Common Pitfalls:**
- Confusing outputs with outcomes (building a school = output; improved literacy = outcome)
- Assuming direct causation without evidence
- Listing assumptions that are actually activities ("training will be conducted" is an activity, not an assumption)
- Making the ToC so complex it becomes unusable
- Skipping this chapter — plans without a ToC cannot be evaluated for effectiveness

**7.7 Template: Theory of Change Diagram + Narrative**

Part A: Diagram template (table format representing the results chain):

| Level | Statement | Causal Link ("If...then...") | Assumptions | Risks |
|-------|-----------|------------------------------|-------------|-------|
| Impact | ... | — | — | — |
| Outcome 1 | ... | If [outputs], then [outcome] | ... | ... |
| Output 1.1 | ... | If [activities], then [output] | ... | ... |
| Activity 1.1.1 | ... | If [inputs], then [activity] | ... | ... |
| Inputs | ... | — | — | — |

Part B: Narrative template (1-2 page prose explaining the logic)

**7.8 Quality Checklist:**
- [ ] Impact links to BDP Goal(s)
- [ ] Outcomes link to Strategic Objectives (from Ch 6)
- [ ] Every level has a "if...then" causal statement
- [ ] Assumptions identified at each level (not just the top)
- [ ] Risks identified for the most critical pathways
- [ ] Narrative explains the logic in plain language
- [ ] A non-specialist can read the ToC and understand your MOA's theory

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

```bash
git add guidebooks/strategic-planning/07-chapter-06.md
git commit -m "Add Ch 7: Building Your Theory of Change (Point 6)"
```

---

### Task 10: Chapter 8 — Designing Programs, Projects, and Activities (Point 7)

**Files:**
- Create: `guidebooks/strategic-planning/08-chapter-07.md`

**Source file:** `~/apps/e-Bangsamoro/.claude/skills/devwork/assets/architecture/e-Ministry/e-Planning/arch-subm-planning-07-ppa.md` (2,639 lines)

- [ ] **Step 1: Read source file** — Extract: PPA hierarchy (Program → Project → Activity), UACS classification, output linkages, implementation details, timeline planning, validation rules.

- [ ] **Step 2: Write the chapter** following the standard chapter anatomy:

**8.1 Purpose** — Translate your Theory of Change into concrete Programs, Projects, and Activities (PPAs) with timelines, responsibilities, and output targets.

**8.2 Key Concepts:**
- PPA hierarchy: Program (continuing, cross-cutting) → Project (time-bound, specific deliverable) → Activity (routine, recurring)
- UACS (Unified Accounts Code Structure) classification — required for budget linkage
- Output-to-PPA linkage — every PPA must produce at least one output from the Theory of Change
- Flexible hierarchy — not every PPA needs all three levels. A standalone activity is valid.

**8.3 Step-by-Step Instructions:**
1. Review your Theory of Change outputs and activities (from Ch 7)
2. Group related activities into logical Programs or Projects
3. For each PPA, define: name, type (program/project/activity), description, responsible unit, timeline, expected outputs, UACS code
4. Link each PPA to its Theory of Change output
5. Verify completeness — every ToC output must have at least one PPA delivering it
6. Complete the PPA Register

**8.4 Worked Example** — continuing with the same ministry.

**8.5 For Decision-Makers** — PPA approval is a resource commitment. Review for strategic fit, feasibility, and whether the MOA has capacity to deliver.

**8.6 Common Pitfalls:**
- Creating PPAs that don't link to any Theory of Change output (orphan activities)
- Mixing program-level and activity-level items in the same register without hierarchy
- Ignoring UACS codes (causes budget preparation problems later)
- Overloading the plan with PPAs the MOA cannot realistically implement

**8.7 Template: PPA Register**

| PPA Code | PPA Name | Type | Description | ToC Output | Responsible Unit | Timeline | UACS Code | Expected Output | Target |
|---------|---------|------|-------------|-----------|-----------------|----------|-----------|-----------------|--------|

**8.8 Quality Checklist:**
- [ ] Every ToC output has at least one PPA
- [ ] No orphan PPAs (every PPA links to a ToC output)
- [ ] PPA type (program/project/activity) correctly classified
- [ ] UACS codes assigned where applicable
- [ ] Timelines are realistic given MOA capacity
- [ ] Responsible units identified for each PPA

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

```bash
git add guidebooks/strategic-planning/08-chapter-07.md
git commit -m "Add Ch 8: Designing Programs, Projects, and Activities (Point 7)"
```

---

### Task 11: Chapter 9 — Planning Your Resources (Point 8)

**Files:**
- Create: `guidebooks/strategic-planning/09-chapter-08.md`

**Source file:** `~/apps/e-Bangsamoro/.claude/skills/devwork/assets/architecture/e-Ministry/e-Planning/arch-subm-planning-08-resource.md` (1,568 lines)

**Secondary source:** `legislation/baas/BAA-84.md` (Budget System Act — budget planning linkages)

- [ ] **Step 1: Read source file** — Extract: resource categories (human, physical, partnerships), staffing estimation, competency gap identification, equipment needs, budget optimization, partnership mapping.

- [ ] **Step 2: Write the chapter** following the standard chapter anatomy:

**9.1 Purpose** — Identify all resources needed to implement your PPAs: people, money, equipment, facilities, and partnerships. This chapter bridges planning and budgeting.

**9.2 Key Concepts:**
- Three resource categories: (a) Human resources — staffing, competencies, training needs, (b) Physical resources — equipment, facilities, technology, supplies, (c) Partnerships — MOUs, development partner support, LGU coordination, CSO engagement
- Resource gap analysis — what you need vs. what you have
- Budget linkage — resource requirements feed directly into the Annual Financial Plan (Ch 10)
- BAA 84 (Bangsamoro Budget System Act) — the legal framework for resource allocation

**9.3 Step-by-Step Instructions:**
1. For each PPA (from Ch 8), list required human resources (positions, competencies, FTE)
2. Identify staffing gaps — positions needed vs. current plantilla
3. For each PPA, list physical resource requirements
4. Identify equipment/facility gaps
5. Map potential partnerships (development partners, other MOAs, LGUs, CSOs)
6. Estimate costs for each resource category (reference BAA 84 budget line items)
7. Complete the Resource Requirements Matrix

**9.4 Worked Example** — continuing with the same ministry.

**9.5 For Decision-Makers** — resource planning reveals the true cost of the strategic plan. If resources exceed what's available, priorities must be set. This is where trade-offs happen.

**9.6 Common Pitfalls:**
- Planning without considering resource constraints (aspirational plans that can't be funded)
- Ignoring human resource development needs (assuming current staff can do everything)
- Not exploring partnerships as a resource strategy
- Disconnecting resource planning from the budget cycle

**9.7 Template: Resource Requirements Matrix**

| PPA Code | PPA Name | HR Required | HR Gap | Physical Resources | Physical Gap | Partnerships | Estimated Cost | Funding Source |
|---------|---------|-------------|--------|-------------------|-------------|-------------|---------------|---------------|

**9.8 Quality Checklist:**
- [ ] Every PPA has a resource assessment
- [ ] Human resource gaps identified with mitigation strategy (hire, train, or partner)
- [ ] Physical resource gaps identified
- [ ] Partnership opportunities explored
- [ ] Cost estimates are realistic and reference BAA 84 budget categories
- [ ] Total resource requirement is within a reasonable range of available budget

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

```bash
git add guidebooks/strategic-planning/09-chapter-08.md
git commit -m "Add Ch 9: Planning Your Resources (Point 8)"
```

---

### Task 12: Chapter 10 — Preparing the Annual Work Plan (Point 9)

**Files:**
- Create: `guidebooks/strategic-planning/10-chapter-09.md`

**Source file:** `~/apps/e-Bangsamoro/.claude/skills/devwork/assets/architecture/e-Ministry/e-Planning/arch-subm-planning-09-annual.md` (2,495 lines)

**Secondary source:** `legislation/baas/BAA-84.md` (budget forms and cycle)

- [ ] **Step 1: Read source file** — Extract: Annual Work Plan (AWP) structure, Annual Financial Plan (AFP) format, Annual Procurement Plan (APP) requirements, prior-year performance analysis, target distribution, budget allocation methodology.

- [ ] **Step 2: Write the chapter** following the standard chapter anatomy:

**10.1 Purpose** — Translate the multi-year strategic plan into this year's specific commitments: what you will do (AWP), what it will cost (AFP), and what you will buy (APP).

**10.2 Key Concepts:**
- Annual Work Plan (AWP) — year-specific PPA targets, timelines, and responsibilities
- Annual Financial Plan (AFP) — budget allocation by PPA, aligned with BAA 84 requirements
- Annual Procurement Plan (APP) — goods, services, and infrastructure to be procured
- The three plans are interdependent: AWP drives AFP, AFP constrains APP
- Prior-year performance review — what was achieved last year informs this year's targets
- Budget calendar — key dates in the BARMM budget cycle (Budget Call, submission deadlines)

**10.3 Step-by-Step Instructions:**
1. Review prior-year performance (what was achieved vs. targeted?)
2. Set annual priorities — which PPAs are priorities for this fiscal year?
3. Set annual targets for each priority PPA (subset of multi-year targets)
4. Develop quarterly milestones and timelines
5. Allocate budget to each PPA (reference BAA 84 budget forms)
6. Prepare procurement requirements for the APP
7. Complete the Annual Work Plan, Annual Financial Plan, and Annual Procurement Plan

**10.4 Worked Example** — continuing with the same ministry. Show AWP, AFP, and APP excerpts.

**10.5 For Decision-Makers** — annual planning is where strategy meets reality. The AFP determines your MOA's budget request. Ministers/EDs must approve annual priorities and budget allocation before submission.

**10.6 Common Pitfalls:**
- Copy-pasting last year's AWP without reviewing performance
- Setting targets without budget reality (planning more than you can fund)
- Missing the Budget Call deadline (MFBM's annual circular sets the submission date)
- Disconnecting the APP from the AWP (procuring items not linked to planned activities)

**10.7 Templates: Annual Work Plan + Annual Financial Plan + Annual Procurement Plan**

Three templates:

**AWP template:**

| PPA Code | PPA Name | Annual Target | Q1 Milestone | Q2 Milestone | Q3 Milestone | Q4 Milestone | Responsible | Budget (PhP) |
|---------|---------|--------------|-------------|-------------|-------------|-------------|-------------|-------------|

**AFP template:**

| PPA Code | Expense Class | Object Code | Amount (PhP) | Source of Funds | BAA 84 Reference |
|---------|--------------|------------|-------------|----------------|-----------------|

**APP template:**

| Item | PPA Code | Mode of Procurement | Estimated Cost (PhP) | Schedule | End User |
|------|---------|--------------------|--------------------|----------|---------|

**10.8 Quality Checklist:**
- [ ] Prior-year performance reviewed and lessons incorporated
- [ ] Annual priorities aligned with strategic objectives
- [ ] Targets are achievable within the fiscal year
- [ ] Budget allocation matches PPA priorities
- [ ] AFP follows BAA 84 format requirements
- [ ] APP items link to AWP activities
- [ ] Budget Call deadline noted and submission timeline planned

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

```bash
git add guidebooks/strategic-planning/10-chapter-09.md
git commit -m "Add Ch 10: Preparing the Annual Work Plan (Point 9)"
```

---

### Task 13: Chapter 11 — Setting Up Monitoring and Evaluation (Point 10)

**Files:**
- Create: `guidebooks/strategic-planning/11-chapter-10.md`

**Source file:** `~/apps/e-Bangsamoro/.claude/skills/devwork/assets/architecture/e-Ministry/e-Planning/arch-subm-planning-10-me.md` (2,005 lines)

- [ ] **Step 1: Read source file** — Extract: RBME framework, indicator design (impact/outcome/output indicators), data collection methods, performance tracking, variance analysis, reporting, evaluation, adaptive management.

- [ ] **Step 2: Write the chapter** following the standard chapter anatomy:

**11.1 Purpose** — Design the system that tells you whether your plan is working. M&E is not an afterthought — it's built into the plan from the start, linked directly to the Theory of Change.

**11.2 Key Concepts:**
- Results-Based Monitoring & Evaluation (RBME) — measures results (outcomes, impact), not just activities
- Indicator hierarchy: Impact indicators → Outcome indicators → Output indicators → Process indicators
- Each indicator needs: definition, unit of measure, baseline, target, data source, collection frequency, responsible officer
- Monitoring (continuous tracking) vs. Evaluation (periodic assessment of effectiveness)
- Adaptive management — using M&E data to adjust the plan mid-course

**11.3 Step-by-Step Instructions:**
1. Review your Theory of Change (Ch 7) — each results level needs at least one indicator
2. Design indicators for each level (impact, outcome, output)
3. For each indicator, define: baseline value, annual targets, data source, collection method, frequency, responsible M&E officer
4. Design the data collection plan — who collects what, when, and how
5. Define reporting schedule — quarterly progress reports, annual performance reports
6. Define evaluation approach — when will you evaluate effectiveness (mid-term, end-of-plan)?
7. Establish adaptive management triggers — what M&E results would cause you to revise the plan?
8. Complete the M&E Framework and Indicator Registry

**11.4 Worked Example** — continuing with the same ministry. Show indicators linked to the ToC from Ch 7.

**11.5 For Decision-Makers** — M&E data should reach leadership regularly (quarterly at minimum). Leaders need to act on M&E findings — not just receive reports. Define what decisions M&E data will inform.

**11.6 Common Pitfalls:**
- Designing M&E after the plan is approved (too late — indicators should inform plan design)
- Measuring only activities (e.g., "training conducted") instead of results ("competency improved")
- Setting indicators with no baseline data
- Collecting data that nobody reads or acts on
- Not budgeting for M&E activities (data collection, evaluation studies cost money)

**11.7 Templates: M&E Framework + Indicator Registry**

**M&E Framework template:**

| Results Level | Statement (from ToC) | Indicator | Baseline | Year 1 Target | Year 2 Target | Year 3 Target | Data Source | Collection Frequency | Responsible |
|--------------|---------------------|-----------|----------|--------------|--------------|--------------|------------|--------------------|-----------|

**Indicator Registry template (detailed):**

| Indicator ID | Indicator Name | Definition | Unit | Baseline | Target | Data Source | Collection Method | Frequency | Responsible Officer | Reporting To |
|-------------|---------------|-----------|------|----------|--------|------------|------------------|-----------|--------------------|-----------|

**11.8 Quality Checklist:**
- [ ] Every ToC results level has at least one indicator
- [ ] Each indicator has a baseline (or a plan to establish one)
- [ ] Targets are set for each year of the plan period
- [ ] Data sources are identified and accessible
- [ ] Collection frequency is realistic for the MOA's capacity
- [ ] Reporting schedule defined (quarterly, annual)
- [ ] Evaluation approach defined (mid-term, end-of-plan)
- [ ] M&E activities are budgeted in the Resource Plan (Ch 9) and AFP (Ch 10)

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

```bash
git add guidebooks/strategic-planning/11-chapter-10.md
git commit -m "Add Ch 11: Setting Up Monitoring and Evaluation (Point 10)"
```

---

### Task 14: Chapter 12 — Assembling the MOA Strategic Plan

**Files:**
- Create: `guidebooks/strategic-planning/12-chapter-11.md`

**Source file:** `~/apps/e-Bangsamoro/.claude/skills/devwork/assets/architecture/e-Ministry/e-Planning/arch-ministerial-planning.md` (submission workflow, approval process, data lifecycle)

- [ ] **Step 1: Read source file** — Read `arch-ministerial-planning.md` focusing on: data flow integration, submission workflow, access control for approval, plan lifecycle.

- [ ] **Step 2: Write the chapter** (custom structure — not the standard anatomy):

**12.1 What You Have Built** — recap of all 10 template outputs produced in Chapters 2-11. Table listing each document, its chapter, and its role in the final plan.

**12.2 The MOA Strategic Plan Document Structure** — how the 10 outputs assemble into one submission package:
1. Cover page and executive summary
2. Legal Mandate Matrix (from Ch 2)
3. BDP Alignment Map (from Ch 3)
4. Priority Agenda Alignment Sheet (from Ch 4)
5. Stakeholder Register & Engagement Plan (from Ch 5)
6. Vision-Mission-Values Statement & Strategic Objectives (from Ch 6)
7. Theory of Change Diagram & Narrative (from Ch 7)
8. PPA Register (from Ch 8)
9. Resource Requirements Matrix (from Ch 9)
10. Annual Work Plan, Annual Financial Plan, Annual Procurement Plan (from Ch 10)
11. M&E Framework & Indicator Registry (from Ch 11)
12. Annexes (supporting documents, legal references)

**12.3 Writing the Executive Summary** — instructions for a 2-3 page executive summary that decision-makers and BPDA reviewers read first. Template provided.

**12.4 The Submission and Approval Workflow:**
- Internal review: Division → Service/Directorate → Minister/ED
- MOA Planning Officer submits to BPDA
- BPDA technical review and certification
- MFBM budget feasibility review
- OCM strategic oversight (if applicable)
- Timeline: when to submit relative to the budget cycle

**12.5 Plan Updating and Revision Cycles:**
- Annual updates — revise AWP, AFP, APP each fiscal year
- Mid-term review — revisit strategic objectives and ToC at the plan's midpoint
- Triggered revisions — when new legislation (BAA), leadership change, or M&E findings require plan modification

**12.6 Worked Example: A Complete MOA Strategic Plan** — reference Appendix E for the full worked example. In this chapter, show the executive summary and document assembly for the running example ministry.

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

```bash
git add guidebooks/strategic-planning/12-chapter-11.md
git commit -m "Add Ch 12: Assembling the MOA Strategic Plan"
```

---

## Back Matter

### Task 15: Glossary

**Files:**
- Create: `guidebooks/strategic-planning/13-glossary.md`

- [ ] **Step 1: Compile glossary terms** from all chapters. Include at minimum:
- AFP (Annual Financial Plan)
- APP (Annual Procurement Plan)
- AWP (Annual Work Plan)
- BAA (Bangsamoro Autonomy Act)
- BDP (Bangsamoro Development Plan)
- BOL (Bangsamoro Organic Law / RA 11054)
- BPDA (Bangsamoro Planning and Development Authority)
- BTA (Bangsamoro Transition Authority)
- LGU (Local Government Unit)
- M&E (Monitoring and Evaluation)
- MFBM (Ministry of Finance, Budget, and Management)
- MOA (Ministry, Office, or Agency)
- OCM (Office of the Chief Minister)
- PPA (Program, Project, Activity)
- RBME (Results-Based Monitoring and Evaluation)
- SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
- SWOT (Strengths, Weaknesses, Opportunities, Threats)
- ToC (Theory of Change)
- UACS (Unified Accounts Code Structure)

Each entry: term, full expansion, one-sentence definition in BARMM context.

- [ ] **Step 2: Commit**

```bash
git add guidebooks/strategic-planning/13-glossary.md
git commit -m "Add glossary for strategic-planning guidebook"
```

---

### Task 16: Appendices A-G

**Files:**
- Create: `guidebooks/strategic-planning/14-appendices.md`

**Sources:**
- Appendix A: `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` (legal hierarchy)
- Appendix B: `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/` (BDP goals/strategies)
- Appendix C: `arch-subm-planning-03-priority-agenda.md` appendix (12-Point Agenda full text)
- Appendix D: Templates from Chapters 2-11
- Appendix E: Composite worked example assembled from all chapter examples
- Appendix F: Terms compiled in Task 15
- Appendix G: BOL, BAA 13, BAA 84, BAA 85 key provisions

- [ ] **Step 1: Write Appendix A — BARMM Legal Hierarchy Reference**

The 7-tier hierarchy with key provisions at each tier relevant to strategic planning. Reference `arch-subm-planning-01-legal-alignment.md` for the hierarchy structure and BOL for specific articles.

- [ ] **Step 2: Write Appendix B — BDP 2023-2028 Quick Reference**

6 Development Goals (full text of each), 8 Key Strategies, and a goal-to-sector mapping table showing which MOAs primarily serve which goals. Source from BDP chapters.

- [ ] **Step 3: Write Appendix C — 12-Point Enhanced Priority Agenda**

Full text of all 12 priorities with the responsible MOA(s) for each. Source from `arch-subm-planning-03-priority-agenda.md` appendix and verify against current official sources.

- [ ] **Step 4: Write Appendix D — Complete Blank Templates**

Consolidate all 10 templates from Chapters 2-11 into one appendix, formatted for printing/photocopying. Each template gets a full page with header identifying the chapter and planning point it belongs to.

Templates to include:
1. Legal Mandate Matrix (Ch 2)
2. BDP Alignment Map (Ch 3)
3. Priority Agenda Alignment Sheet (Ch 4)
4. Stakeholder Register & Engagement Plan (Ch 5)
5. Vision-Mission-Values Statement + Strategic Objectives (Ch 6)
6. Theory of Change Diagram + Narrative (Ch 7)
7. PPA Register (Ch 8)
8. Resource Requirements Matrix (Ch 9)
9. Annual Work Plan (Ch 10)
10. Annual Financial Plan (Ch 10)
11. Annual Procurement Plan (Ch 10)
12. M&E Framework (Ch 11)
13. Indicator Registry (Ch 11)
14. Executive Summary (Ch 12)

- [ ] **Step 5: Write Appendix E — Worked Example: A Complete MOA Strategic Plan**

Assemble all worked examples from Chapters 2-11 into one complete, continuous MOA Strategic Plan for the composite ministry used throughout the guidebook. Include executive summary. This is the reference output — what a finished plan looks like.

- [ ] **Step 6: Write Appendix F — Glossary of Planning Terms**

Reference or duplicate the glossary from Task 15, formatted for the appendix.

- [ ] **Step 7: Write Appendix G — Legal References**

Key provisions from:
- BOL (RA 11054) — articles on governance authority, planning mandates, fiscal autonomy
- BAA 13 (Administrative Code) — MOA organizational mandates, administrative procedures
- BAA 84 (Budget System Act) — budget preparation, resource allocation, fiscal management
- BAA 85 (General Appropriations) — ministry/agency-specific mandates and allocations

Each entry: law, provision number, relevant text excerpt, and how it applies to planning.

- [ ] **Step 8: Invoke `/citation`** — Feliciano footnotes throughout appendices.

- [ ] **Step 9: Commit**

```bash
git add guidebooks/strategic-planning/14-appendices.md
git commit -m "Add appendices A-G for strategic-planning guidebook"
```

---

## Quality Assurance

### Task 17: Fact-check and cross-reference review

- [ ] **Step 1: Invoke `/fact-checker`** — run across all chapter files. Verify:
- All BAA numbers are correct
- All BOL article references are accurate
- Ministry names and abbreviations are current
- BDP goals and strategies are accurately stated
- 12-Point Priority Agenda items are correct
- Official titles match `barmm-officials-2025-2026.md`

- [ ] **Step 2: Cross-reference check** — verify that:
- Every template referenced in Ch 12 exists in the relevant chapter
- Every chapter's worked example uses the same composite ministry consistently
- All cross-chapter references (e.g., "see Ch 7" in Ch 11) point to the correct chapter
- Appendix D contains all templates from all chapters
- Appendix E assembles all worked examples coherently

- [ ] **Step 3: Fix any issues found**

- [ ] **Step 4: Commit fixes**

```bash
git add guidebooks/strategic-planning/
git commit -m "QA: fact-check and cross-reference fixes for strategic-planning guidebook"
```

---

### Task 18: Update INDEX.md and production plan

**Files:**
- Modify: `INDEX.md` (root)
- Modify: `planning/GUIDEBOOK-PRODUCTION-PLAN.md`

- [ ] **Step 1: Add strategic-planning to root INDEX.md** under the Guidebooks section:

```markdown
- [Strategic Planning](guidebooks/strategic-planning/) — Strategic Planning Guidebook for the Bangsamoro Government (10-Point Framework)
```

- [ ] **Step 2: Update GUIDEBOOK-PRODUCTION-PLAN.md** — move "Strategic Planning for BARMM Entities" from Tier 2 to Completed, with word count and page estimate.

- [ ] **Step 3: Update vault catalog** at `~/Vault/bangsamoro/guidebooks/guidebook-brainstorm-catalog.md` — move from "New Ideas" to "Completed" table.

- [ ] **Step 4: Commit**

```bash
git add INDEX.md planning/GUIDEBOOK-PRODUCTION-PLAN.md
git commit -m "Update INDEX.md and production plan with strategic-planning guidebook"
```

---

## Summary

| Task | Description | Files | Est. Effort |
|------|-------------|-------|-------------|
| 0 | Setup | directory | 2 min |
| 1 | Table of Contents | 00-table-of-contents.md | 15 min |
| 2 | About + Author | 00b-about.md, 00c-author.md | 15 min |
| 3 | Ch 1: Introduction | 01-introduction.md | 30 min |
| 4 | Ch 2: Legal Mandate (Pt 1) | 02-chapter-01.md | 45 min |
| 5 | Ch 3: BDP Alignment (Pt 2) | 03-chapter-02.md | 45 min |
| 6 | Ch 4: Priority Agenda (Pt 3) | 04-chapter-03.md | 30 min |
| 7 | Ch 5: Stakeholders (Pt 4) | 05-chapter-04.md | 45 min |
| 8 | Ch 6: Strategy (Pt 5) | 06-chapter-05.md | 45 min |
| 9 | Ch 7: Theory of Change (Pt 6) | 07-chapter-06.md | 45 min |
| 10 | Ch 8: PPA Planning (Pt 7) | 08-chapter-07.md | 45 min |
| 11 | Ch 9: Resources (Pt 8) | 09-chapter-08.md | 30 min |
| 12 | Ch 10: Annual Plan (Pt 9) | 10-chapter-09.md | 45 min |
| 13 | Ch 11: M&E (Pt 10) | 11-chapter-10.md | 45 min |
| 14 | Ch 12: Consolidation | 12-chapter-11.md | 30 min |
| 15 | Glossary | 13-glossary.md | 15 min |
| 16 | Appendices A-G | 14-appendices.md | 60 min |
| 17 | QA: fact-check + cross-ref | all files | 30 min |
| 18 | Update INDEX + production plan | INDEX.md, production plan, vault | 10 min |
