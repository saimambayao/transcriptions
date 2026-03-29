# Systems Change Guidebook Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Write the complete *Systems Change in the Bangsamoro: How to Ensure that the Bangsamoro will Succeed* — a strategic reference and advocacy document applying systems thinking and complexity theory to Bangsamoro governance and development.

**Architecture:** 8 substantive chapters (Introduction + 7 framework chapters + 1 capstone application chapter), plus front matter, glossary, bibliography, and 4 appendices. Each chapter follows a theory-then-BARMM-application pattern. Chapters 2 and 8 use a causal chain organization (Governance → Peace → Economy → Education → Social). Markdown source files in `guidebooks/systems-change-bangsamoro/`, following the same conventions as the Bill Drafting and CSW guidebooks.

**Tech Stack:** Markdown content, `/bangsamoro` + `/guidebook-writer` + `/citation` skills, Feliciano 10th Ed. footnotes, Mermaid diagrams rendered to PNG.

**Primary source material:** `reference/systems-ebooks/` (32 ebooks on systems thinking, complexity theory, change models, political/economic/social complexity)

**Key source files:**
- `reference/systems-ebooks/system-change.md` — core text (Systems Change: An Introduction by Joss Colchester)
- `reference/systems-ebooks/system-thinking.md` — Systems Thinking overview
- `reference/systems-ebooks/complexity-theory.md` — Complexity Theory overview
- `reference/systems-ebooks/complex-adaptive-system.md` — CAS overview
- `reference/systems-ebooks/Theory-of-Change.md` — Hivos ToC Guidelines
- `reference/systems-ebooks/political-complexity.md` — Political systems as CAS
- `reference/systems-ebooks/economic-complexity.md` — Economic systems as CAS
- `reference/systems-ebooks/social-complexity.md` — Social systems as CAS
- `reference/systems-ebooks/system-dynamics.md` — Causal loop diagrams, stocks and flows
- `reference/systems-ebooks/system-innovation.md` — Leverage points, transitions

**Secondary sources:**
- BOL (RA 11054): `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/`
- BDP 2023-2028: `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/`
- BAA Quick Reference: `~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md`
- BARMM Officials: `~/.claude/skills/bangsamoro/references/barmm-officials-2025-2026.md`

**Existing guidebook reference (for voice/format consistency):** `guidebooks/bill-drafting/` — use 00-table-of-contents.md, 00b-about.md, 00c-author.md, generate-pdf.py, generate-docx.py, guidebook-template.html as structural templates.

**Author bio:** Always use the canonical version from `~/Vault/reference/author-bio-standard.md` — never improvise.

---

## Pre-Implementation Setup

### Task 0: Create directory and invoke domain context

**Files:**
- Create: `guidebooks/systems-change-bangsamoro/` (directory)
- Create: `guidebooks/systems-change-bangsamoro/images/` (diagrams)
- Create: `guidebooks/systems-change-bangsamoro/appendices/` (practical tools)

- [ ] **Step 1: Invoke `/bangsamoro` skill** to load BARMM domain context (officials, governance structure, BOL provisions, BDP goals, BAA index). This context persists for all subsequent chapter writing.

- [ ] **Step 2: Create the guidebook directories**

```bash
mkdir -p guidebooks/systems-change-bangsamoro/{images,appendices}
```

- [ ] **Step 3: Commit scaffold**

```bash
git add guidebooks/systems-change-bangsamoro
git commit -m "Add systems-change-bangsamoro guidebook directory"
```

---

## Front Matter

### Task 1: Table of Contents

**Files:**
- Create: `guidebooks/systems-change-bangsamoro/00-table-of-contents.md`

- [ ] **Step 1: Write the TOC**

Follow the Bill Drafting guidebook TOC format. Include:
- Full title: "Systems Change in the Bangsamoro"
- Subtitle: "How to Ensure that the Bangsamoro will Succeed"
- All 8 chapters with section/subsection numbering using `&emsp;` indentation
- Glossary and Bibliography
- All 4 appendices (A-D)

Chapter 2 subsections follow the causal chain:
- 2.2.1 Understanding Complexity
- 2.2.2 Complexity in the Governance and Political System
- 2.2.3 Complexity in the Peace and Security System
- 2.2.4 Complexity in the Economic System
- 2.2.5 Complexity in the Education System
- 2.2.6 Complexity in the Social Services and Health System

Chapter 8 mirrors Chapter 2's causal chain:
- 8.1 Governance and Politics
- 8.2 Peace and Security
- 8.3 Economy
- 8.4 Education
- 8.5 Social

- [ ] **Step 2: Review** — verify all chapters, glossary, bibliography, and appendices are listed.

### Task 2: About and Author pages

**Files:**
- Create: `guidebooks/systems-change-bangsamoro/00b-about.md`
- Create: `guidebooks/systems-change-bangsamoro/00c-author.md`

- [ ] **Step 1: Write the About page** (`00b-about.md`)

Include:
- **Purpose** — introduces systems thinking as practical strategy for BARMM leaders
- **Intended Audience** — five groups:
  1. Bangsamoro leaders (MPs, Ministers, Chief Minister's Office, LGU executives)
  2. Peace and development workers (government, CSOs, international partners)
  3. Consultants and technical advisors
  4. Directors and planners in MOAs
  5. Academe and researchers
- **How to Use This Guidebook** — three reading paths:
  - Sequential (full learning journey, Chapters 1-8)
  - Targeted (jump to your sector in Chapter 8, refer back for frameworks)
  - Reference (glossary + appendices as needed)
- **What This Guidebook Is Not** — not a development plan, not a training curriculum, not a policy manual, not a critique of the BTA

- [ ] **Step 2: Write the Author page** (`00c-author.md`)

Use the canonical author bio from `~/Vault/reference/author-bio-standard.md` verbatim.

- [ ] **Step 3: Commit front matter**

```bash
git add guidebooks/systems-change-bangsamoro/00-table-of-contents.md guidebooks/systems-change-bangsamoro/00b-about.md guidebooks/systems-change-bangsamoro/00c-author.md
git commit -m "Add systems-change-bangsamoro guidebook front matter"
```

---

## Chapter Writing

**Standard procedure for every chapter:**

Before writing each chapter:
1. Read the corresponding source ebook sections (paths specified per task)
2. Read relevant BDP chapters for BARMM data
3. Extract frameworks, models, theorists, and key concepts
4. Build a Chapter Fact Sheet for BARMM-specific data claims

After writing each chapter:
1. Invoke `/citation` to add Feliciano 10th Ed. footnotes
2. Verify all BARMM-specific references (BAA numbers, BDP statistics, official titles)
3. Every factual claim must have a `[^N]` footnote marker

**Writing voice:**
- Direct second-person ("you", "your"). A senior colleague coaching a competent professional.
- Sentences: average 15-20 words, max 30. Split at semicolons.
- Paragraphs: max 5 sentences. One-sentence paragraphs for emphasis.
- Chapter openings: WHY this matters to the reader's work RIGHT NOW. Not history. Not definitions.
- Imperative mood for instructions. Bold key terms for scannability.
- Every principle followed by a concrete BARMM example. No principle stands alone.
- Active voice 80%+. No emojis.
- PROHIBITED phrases: "It is important to note that", "In order to", "It should be noted", "With regard to", "In the context of", "It is worth mentioning", "As previously mentioned", "For the purposes of", "In light of the foregoing", "The aforementioned", "It is recommended that", "Pursuant to the provisions of", "Notwithstanding the foregoing", "In furtherance of"

### Task 3: Introduction

**Files:**
- Create: `guidebooks/systems-change-bangsamoro/01-introduction.md`

**Source files:**
- `reference/systems-ebooks/system-change.md` (lines 1-100, Overview)
- BDP Chapter Summaries for BARMM data

**Target:** ~2,500 words (~8 pages)

- [ ] **Step 1: Read source files**

- [ ] **Step 2: Write the Introduction**

Sections:
1. **Why This Guidebook** — BARMM has the plan, the budget, the institutions — but something is missing. Frame with data: poverty 29.80%, literacy 71.6%, budget utilization 67-72%.
2. **Who This Guidebook Is For** — five audience scenarios (minister, director, CSO leader, development partner, planner)
3. **How to Use This Guidebook** — Chapters 1-7 build toolkit, Chapter 8 applies it. Three reading paths.
4. **The Core Argument** — the Bangsamoro will succeed only through systems change, not component fixes. Three levels: structural (policies, rules), relational (relationships, power), transformative (mental models).
5. **What This Guidebook Is Not** — not a plan, not a curriculum, not a policy manual, not a critique.

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

---

### Task 4: Chapter 1 — Wicked Problems: Systems of Problems in a Complex World

**Files:**
- Create: `guidebooks/systems-change-bangsamoro/02-chapter-01.md`

**Source files:**
- `reference/systems-ebooks/system-change.md` (lines 1-200, Overview/Context)
- `reference/systems-ebooks/system-innovation.md` (lines 1-80)

**Target:** ~6,000 words (~20 pages)

- [ ] **Step 1: Read source files** — Extract wicked problems concept, Rittel & Webber, Ackoff's "mess", Scharmer's "results nobody wants"

- [ ] **Step 2: Write the chapter**

**Opening:** "Why do the best-funded, best-intentioned programs in BARMM keep failing to move the needle?"

**1.1 What Are Wicked Problems?** — Rittel & Webber (1973), Ackoff, Scharmer. Contrast with "tame" problems.

**1.2 Properties of Wicked Problems** — 8 properties, each with a BARMM example.

**1.3 Wicked Problems in the Bangsamoro** — Frame BARMM challenges as interconnected "mess": poverty-literacy-employment-conflict cycle, governance-trust cycle. Use BDP data (poverty 29.80%, literacy 71.6%, GDP share 1.4%, physician ratio 1:51,187, budget utilization 67-72%).

**1.4 Why Traditional Approaches Fall Short** — Reductionist thinking, siloed ministries, linear planning, project-based development.

**1.5 A Different Approach** — Preview systems thinking, complexity theory, systems change. Chapter roadmap.

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

---

### Task 5: Chapter 2 — Systems Change through Systems Thinking and Complexity Theory

**Files:**
- Create: `guidebooks/systems-change-bangsamoro/03-chapter-02.md`

**Source files:**
- `reference/systems-ebooks/system-thinking.md` (full)
- `reference/systems-ebooks/complexity-theory.md` (first 800 lines)
- `reference/systems-ebooks/complex-adaptive-system.md` (first 300 lines)
- `reference/systems-ebooks/system-change.md` (lines 100-200)
- BDP Chapters 5, 7, 9, 10 for sector data

**Target:** ~10,000 words (~35 pages) — largest chapter

- [ ] **Step 1: Read source files**

- [ ] **Step 2: Write the chapter**

**Opening:** "Every day, when a fisherman in Tawi-Tawi harvests seaweed, a student in Lanao del Sur opens a textbook, and a legislator in Cotabato City files a bill — they are all operating within interconnected systems."

**2.1 What Is a System?** (~8 pages)
- 2.1.1 Sets versus Systems — Meadows definition, Senge on synthesis
- 2.1.2 Elements, Relationships, and Function — relationships define the system more than elements
- 2.1.3 Systems Properties — emergence, feedback, hierarchy with BARMM examples
- 2.1.4 BARMM as a System of Systems — five interconnected subsystems

**2.2 What Is Complexity?** (~20 pages, organized by causal chain)
- 2.2.1 Understanding Complexity — four dimensions (number, connectivity, diversity, adaptation), linear vs nonlinear, tipping points, CAS properties (self-organization, emergence, co-evolution, path dependence)
- 2.2.2 Complexity in the Governance and Political System — 16 MOAs as CAS, capacity-trust feedback loops, patronage as emergent property
- 2.2.3 Complexity in the Peace and Security System — conflict-displacement-poverty loop, rido as emergent, contested lands, tipping points
- 2.2.4 Complexity in the Economic System — agriculture lock-in, investment-conflict loop, MSME growth dynamics
- 2.2.5 Complexity in the Education System — literacy-poverty loop, madaris integration, nonlinear outcomes
- 2.2.6 Complexity in the Social Services and Health System — health-poverty spiral, physician ratio as structural ceiling, BHS stock constraint

Each sector section ends with a **bridge sentence** connecting to the next sector in the causal chain.

**2.3 What Is Systems Change and How to Achieve It?** (~7 pages)
- 2.3.1 Changing System Structure to Change Outcomes
- 2.3.2 Leverage Points (Meadows, intro — full treatment in Ch 6)
- 2.3.3 Six Conditions of Systems Change (Kania, Kramer, Senge 2018)
- 2.3.4 From Component Fixes to Structural Transformation — comparison table

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

---

### Task 6: Chapter 3 — Change Theories and Models

**Files:**
- Create: `guidebooks/systems-change-bangsamoro/04-chapter-03.md`

**Source files:**
- `reference/systems-ebooks/system-change.md` (lines 200-500, Change section)
- `reference/systems-ebooks/Theory-of-Change.md` (Parts A-B)
- `reference/systems-ebooks/system-innovation.md` (Transitions section)

**Target:** ~7,500 words (~25 pages)

- [ ] **Step 1: Read source files**

- [ ] **Step 2: Write the chapter**

**Opening:** "You cannot change what you do not understand. Before you design an intervention, before you draft a bill, before you allocate a budget — you need a theory of how change actually happens in complex systems."

**3.1 Theories of Change** — Hivos 8-step ToC process, making assumptions explicit, BDP as implicit ToC

**3.2 The Adaptive Cycle** — Holling's 4 phases (r, K, Omega, Alpha), panarchy, BARMM's position in the cycle

**3.3 The Two Loops Model** — Wheatley & Frieze, hospicing/illuminating, ARMM-to-BARMM as two loops

**3.4 Transitions** — Geels' Multi-Level Perspective, landscape/regime/niche, BOL as landscape shift

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

---

### Task 7: Chapter 4 — Systems Mapping

**Files:**
- Create: `guidebooks/systems-change-bangsamoro/05-chapter-04.md`

**Source files:**
- `reference/systems-ebooks/system-change.md` (lines 500-900, Mapping section)
- `reference/systems-ebooks/system-dynamics.md` (Modules 1-4)

**Target:** ~6,000 words (~20 pages) + 3 Mermaid diagrams

- [ ] **Step 1: Read source files**

- [ ] **Step 2: Write the chapter**

**Opening:** "You cannot change a system you cannot see. Systems mapping makes the invisible visible."

**4.1 Why Map Systems?** — Mental models, Senge, Pirsig, shared language

**4.2 Causal Loop Diagrams** — Variables, arrows, polarity, reinforcing/balancing loops, stocks/flows. Worked example: Budget Utilization Loop.

**4.3 Systems Archetypes** — Limits to Growth (MSME), Tragedy of Commons (contested lands), Success to Successful (mainland vs BaSulTa)

**4.4 Stakeholder Mapping** — Power/interest matrix, formal/informal power, BARMM stakeholders

**4.5 Incentives Mapping** — Game theory basics, zero-sum vs non-zero-sum, BARMM incentive analysis

**4.6 BARMM Systems Maps: Worked Examples** — Education-poverty loop, governance trust cycle, investment-conflict nexus. Include Mermaid diagram PNG references.

- [ ] **Step 3: Create Mermaid diagrams** in `images/`:
  - `figure-01-budget-loop.mmd` → PNG (Budget Utilization Loop)
  - `figure-02-education-poverty.mmd` → PNG (Education-Poverty Feedback)
  - `figure-03-investment-conflict.mmd` → PNG (Investment-Conflict Nexus)

Render with: `npx -y @mermaid-js/mermaid-cli -i images/figure-NN.mmd -o images/figure-NN.png -t neutral -b transparent -w 1200`

- [ ] **Step 4: Invoke `/citation`**

- [ ] **Step 5: Commit**

---

### Task 8: Chapter 5 — Futuring

**Files:**
- Create: `guidebooks/systems-change-bangsamoro/06-chapter-05.md`

**Source files:**
- `reference/systems-ebooks/system-change.md` (lines 800-1200, Envision section)

**Target:** ~6,000 words (~20 pages)

- [ ] **Step 1: Read source files** — Extract inner change, Theory U (Scharmer), Systems Leadership (Banerjee), narratives, horizon scanning

- [ ] **Step 2: Write the chapter**

**Opening:** "The Bangsamoro you want to build in 2030 does not yet exist. Futuring is how you design it before you build it."

**5.1 Inner Change and the Systems Leader** — Margaret Mead, Bateson, values, intrinsic motivation, 12 Pillars of Moral Governance

**5.2 Theory U** — Scharmer's framework, ego-system to eco-system, BARMM workshop thought experiment

**5.3 Systems Leadership** — Leadership 3.0, wholism, space-holding, creative tension, bridging, liminal space

**5.4 Narratives and Storytelling** — Old narrative (victimhood) vs new narrative (agency), BDP vision as narrative

**5.5 Horizon Scanning** — Signals, trends, drivers, three BARMM 2030 scenarios (Continuity, Breakthrough, Disruption)

**5.6 Envisioning BARMM 2030** — Vision exercise across governance, education, economy, social

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

---

### Task 9: Chapter 6 — Strategy Development

**Files:**
- Create: `guidebooks/systems-change-bangsamoro/07-chapter-06.md`

**Source files:**
- `reference/systems-ebooks/system-change.md` (lines 1200-1700, Strategy section)
- `reference/systems-ebooks/system-innovation.md` (Leverage Points, Iceberg Model)

**Target:** ~6,000 words (~20 pages)

- [ ] **Step 1: Read source files**

- [ ] **Step 2: Write the chapter**

**Opening:** "You have mapped the system. You have envisioned the future. Now: where do you intervene?"

**6.1 Leverage Points** — Meadows' 12 points in 4 tiers (Parameters → Feedback → Design → Paradigm), Iceberg Model, BARMM examples at every tier

**6.2 Multi-Level Perspective as Strategy** — Landscape/regime/niche strategies for BARMM

**6.3 Systems Aikido** — Redirecting clan networks, budget momentum

**6.4 Systems Acupuncture** — SEAL awards, IRR requirements, transparency platforms

**6.5 Systems Gardening** — BAA 49 as garden framework, cooperatives, command-to-cultivation shift

**6.6 Systems Entrepreneurship** — BEZA as platform, committee system, network scaling

**6.7 Strategic Implications for BARMM** — Summary table, strategic priority sequence

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

---

### Task 10: Chapter 7 — Collaborations in Ecosystems

**Files:**
- Create: `guidebooks/systems-change-bangsamoro/08-chapter-07.md`

**Source files:**
- `reference/systems-ebooks/system-change.md` (lines 1700-2100, Develop section)
- `reference/systems-ebooks/network-theory.md` (first 200 lines)

**Target:** ~6,000 words (~20 pages)

- [ ] **Step 1: Read source files**

- [ ] **Step 2: Write the chapter**

**Opening:** "No single ministry, no single leader, no single plan can change the Bangsamoro system alone."

**7.1 Collaboration versus Coordination** — Three levels (cooperation, coordination, collaboration), Marawi example

**7.2 Ecosystem Thinking** — From organizations to ecosystems, ecosystem properties

**7.3 Collective Impact** — Kania & Kramer's 5 conditions applied to BARMM

**7.4 Scaling Systems Change** — Hierarchical vs network scaling, tipping points, BARMM LGU example

**7.5 Sustaining Change** — Leadership transition risk, institutionalization (BAAs > EOs > programs), resilience, adaptive management

**7.6 The BARMM Development Ecosystem** — Full ecosystem map: government, CSOs, international partners, traditional/religious, private sector, academe, diaspora

- [ ] **Step 3: Invoke `/citation`**

- [ ] **Step 4: Commit**

---

### Task 11: Chapter 8 — Systems Change during the Transition Government

**Files:**
- Create: `guidebooks/systems-change-bangsamoro/09-chapter-08.md`

**Source files:**
- ALL source ebooks (for framework application)
- BDP Chapters 4, 5, 7, 9, 10
- BAA Quick Reference
- BOL Key Provisions

**Target:** ~11,000 words (~35 pages) — capstone chapter, longest and most important

**CRITICAL:** This chapter mirrors Chapter 2's causal chain: Governance → Peace → Economy → Education → Social. Each sector has 4 subsections following a consistent pattern.

- [ ] **Step 1: Read BARMM reference files** — Build Chapter Fact Sheet with verified data for all 5 sectors

- [ ] **Step 2: Write the chapter**

**Opening:** "The BTA transition was not just a change in government. It was a systems change experiment — the most ambitious in Philippine history."

**8.1 Governance and Politics** (~9 pages)
- 8.1.1 What the BTA Changed — adaptive cycle analysis, 89 BAAs, priority codes, institutional architecture
- 8.1.2 Two Loops Analysis — patronage dying, merit-based governance emerging, what hasn't crossed
- 8.1.3 What Still Needs to Change — Revenue Code, Investment Code, budget utilization, local governance
- 8.1.4 Prescriptions for the First Regular Government — leverage points by level (parameter through paradigm)

Bridge: "Governance is the operating system. But it cannot deliver if the environment is unstable."

**8.2 Peace and Security** (~9 pages)
- 8.2.1 What the BTA Changed — peace process as adaptive cycle, normalization, BAAs 57/60/61/62/89
- 8.2.2 Two Loops Analysis — armed struggle dying, community peace emerging, rido/contested lands unresolved
- 8.2.3 The Peace Wicked Problem — macro vs micro conflicts, conflict-poverty loop, BAA 89 as highest-risk/highest-reward
- 8.2.4 Prescriptions — land governance legislation, conflict early warning, community peace mechanisms, transitional justice with care

Bridge: "Peace creates the conditions for economic activity."

**8.3 Economy** (~9 pages)
- 8.3.1 The BARMM Economy as CAS — agriculture lock-in, contested lands constraint, investment-conflict loop
- 8.3.2 Key Interventions — BAA 82 (Labor Code), BEZA, MSME programs, cooperatives
- 8.3.3 The GDP Share Wicked Problem — 1.4% national share, interconnected suppressors
- 8.3.4 Prescriptions — Revenue/Investment Codes year 1, seaweed value chain (systems aikido), economic ecosystem

Bridge: "Economic activity creates the conditions for human development."

**8.4 Education** (~9 pages)
- 8.4.1 The Education System as CAS — agents, feedback loops, literacy as emergent property
- 8.4.2 Key Interventions — BAA 18 (Education Code), BAA 40, BAA 50, ISAL, AKAP
- 8.4.3 The Literacy Wicked Problem — 71.6% functional literacy, multi-factor bottleneck
- 8.4.4 Prescriptions — teacher quality, madaris accreditation, TVET-to-employment, redefine success

Bridge: "Education produces human capital. But human capital means nothing without health."

**8.5 Social** (~8 pages)
- 8.5.1 Social Services as CAS — health-poverty spiral, physician ratio as structural ceiling
- 8.5.2 Key Interventions — 12 hospital BAAs, BAA 62 (IDP), BAA 64 (IP), BAA 89 (Transitional Justice)
- 8.5.3 The Poverty Wicked Problem — 29.80%, remaining poverty is structural and self-reinforcing
- 8.5.4 Prescriptions — social protection code, BHS expansion, unified social registry, telemedicine (systems acupuncture)

**Closing** — Five sectors as one interconnected system. First regular government enters growth (r-phase). Choice: systems change by design or by default.

- [ ] **Step 3: Invoke `/citation`** — This chapter will have the most citations (60-80+). Verify all BAA numbers, BDP statistics, BOL references.

- [ ] **Step 4: Invoke `/fact-checker`** — Verify all statistical claims against BDP chapter summaries.

- [ ] **Step 5: Commit**

---

## Back Matter

### Task 12: Glossary

**Files:**
- Create: `guidebooks/systems-change-bangsamoro/10-glossary.md`

- [ ] **Step 1: Compile ~50 glossary terms** from all chapters. Include systems thinking terms (CAS, emergence, feedback loop, leverage point, etc.) and BARMM terms (BARMM, BOL, BTA, BDP, BAA, MOA, etc.). Each entry: term in bold, definition in BARMM context.

- [ ] **Step 2: Commit**

### Task 13: Bibliography

**Files:**
- Create: `guidebooks/systems-change-bangsamoro/11-bibliography.md`

- [ ] **Step 1: Compile bibliography** organized by category:
  - Primary Legal Sources (BOL, BAAs, Resolutions)
  - Development Planning (BDP)
  - Systems Thinking and Complexity Theory (Colchester, Meadows, Senge, Holland, von Bertalanffy)
  - Change Theory and Models (Holling, Geels, Kania/Kramer, Scharmer, Wheatley/Frieze, Hivos)
  - Wicked Problems (Rittel & Webber)
  - Networks and Scaling (Gladwell, Rogers)
  - Systems Leadership and Strategy (Banerjee, Kim, Pirsig, Westley)
  - Statistical Sources (PSA)

- [ ] **Step 2: Commit**

---

## Appendices

### Task 14: Appendices A-D

**Files:**
- Create HTML + PDF pairs in `guidebooks/systems-change-bangsamoro/appendices/`

- [ ] **Step 1: Write Appendix A — Systems Mapping Toolkit** (HTML)

Step-by-step guide for creating causal loop diagrams, stakeholder maps, and incentive maps for any BARMM policy issue. Include:
- 6-step CLD guide with polarity examples
- Worked education-poverty cycle example
- Stakeholder Power/Interest Matrix template (5-step process)
- Incentive mapping template (8-actor table, zero-sum analysis)

- [ ] **Step 2: Write Appendix B — BARMM Systems Diagnostic** (HTML)

Self-assessment checklist for adaptive cycle phase identification:
- Phase Identification Checklists (8 indicators each for Growth/Conservation/Release/Reorganization)
- Sector-Specific Assessment cards (Governance, Education, Economy, Peace, Social)
- Cross-Sector Alignment grid

- [ ] **Step 3: Write Appendix C — Futuring Workshop Guide** (HTML)

2-day facilitation guide for Theory U sessions:
- Day 1: Going Down the U (Open Mind, Open Heart, Open Will)
- Day 2: Coming Up the U (Crystallizing, Prototyping, Embodying)
- Facilitation notes (power dynamics, Islamic protocols, language)

- [ ] **Step 4: Write Appendix D — Change Agent Self-Assessment** (HTML)

30-item self-assessment across 4 sections:
- Systems Thinking Competencies (6 items)
- Leadership Capacities (6 items)
- Change Readiness (6 items)
- Values Alignment (12 items — one per Moral Governance pillar)
- Scoring guide and action planning template

- [ ] **Step 5: Render all appendices to PDF** using WeasyPrint

- [ ] **Step 6: Commit**

---

## Build Pipeline

### Task 15: PDF and DOCX generation

**Files:**
- Create: `guidebooks/systems-change-bangsamoro/generate-pdf.py`
- Create: `guidebooks/systems-change-bangsamoro/generate-docx.py`
- Create: `guidebooks/systems-change-bangsamoro/guidebook-template.html`

- [ ] **Step 1: Adapt guidebook-template.html** from `guidebooks/bill-drafting/guidebook-template.html`
  - Title: "Systems Change in the Bangsamoro"
  - Subtitle: "How to Ensure that the Bangsamoro will Succeed"
  - Color scheme: Navy (#1B365D) + Gold (#C5A54E)
  - Running footer: "Systems Change in the Bangsamoro — Saidamen R. Mambayao"
  - Keep ALL CSS: table-layout:fixed, footnotes, blockquotes, TOC, landscape pages

- [ ] **Step 2: Adapt generate-pdf.py** from `guidebooks/bill-drafting/generate-pdf.py`
  - MD_FILES list: 14 files (00-toc through 11-bibliography)
  - Output: `Systems-Change-in-the-Bangsamoro.pdf`
  - Add Mermaid code block warning step

- [ ] **Step 3: Adapt generate-docx.py** from `guidebooks/bill-drafting/generate-docx.py`
  - Same MD_FILES, output: `Systems-Change-in-the-Bangsamoro.docx`
  - Font config: Inter body, Consolas mono, Navy/Slate/Gold colors

- [ ] **Step 4: Test build**

```bash
python3 generate-pdf.py
python3 generate-docx.py
```

- [ ] **Step 5: Commit**

---

## Quality Assurance

### Task 16: Fact-check and citation audit

- [ ] **Step 1: Invoke `/fact-checker`** across Chapter 8 (most BARMM data). Verify:
  - All poverty, literacy, GDP, health statistics match BDP chapter summaries
  - All BAA numbers and short titles are correct
  - All BOL article/section citations are accurate
  - Ministry names and abbreviations are current

- [ ] **Step 2: Citation audit** across all chapters. Verify:
  - Every `[^N]` inline reference has a matching definition
  - Every definition has at least one inline reference
  - No sequence gaps or duplicates
  - Named theorists have source citations
  - BDP statistics have chapter citations

- [ ] **Step 3: Fix any issues found**

- [ ] **Step 4: Regenerate PDF and DOCX**

- [ ] **Step 5: Commit fixes**

---

### Task 17: Update INDEX and production plan

**Files:**
- Modify: `INDEX.md` (root)
- Modify: `planning/GUIDEBOOK-PRODUCTION-PLAN.md`

- [ ] **Step 1: Add to root INDEX.md** under Guidebooks section

- [ ] **Step 2: Update GUIDEBOOK-PRODUCTION-PLAN.md** — add to Completed Guidebooks table with word count and page estimate

- [ ] **Step 3: Commit**

---

## Summary

| Task | Description | Files | Est. Words |
|------|-------------|-------|------------|
| 0 | Setup | directory | — |
| 1 | Table of Contents | 00-table-of-contents.md | 600 |
| 2 | About + Author | 00b-about.md, 00c-author.md | 800 |
| 3 | Introduction | 01-introduction.md | 2,500 |
| 4 | Ch 1: Wicked Problems | 02-chapter-01.md | 6,000 |
| 5 | Ch 2: Systems Change (largest) | 03-chapter-02.md | 10,000 |
| 6 | Ch 3: Change Theories | 04-chapter-03.md | 7,500 |
| 7 | Ch 4: Systems Mapping + diagrams | 05-chapter-04.md + PNGs | 6,000 |
| 8 | Ch 5: Futuring | 06-chapter-05.md | 6,000 |
| 9 | Ch 6: Strategy | 07-chapter-06.md | 6,000 |
| 10 | Ch 7: Collaborations | 08-chapter-07.md | 6,000 |
| 11 | Ch 8: BARMM Application (capstone) | 09-chapter-08.md | 11,000 |
| 12 | Glossary | 10-glossary.md | 2,000 |
| 13 | Bibliography | 11-bibliography.md | 800 |
| 14 | Appendices A-D | 4 HTML + 4 PDF | — |
| 15 | Build pipeline | generate-pdf/docx.py + template | — |
| 16 | QA: fact-check + citation audit | all files | — |
| 17 | Update INDEX + production plan | INDEX.md, production plan | — |
| **TOTAL** | | **17 files + appendices + build** | **~65,000** |

**Parallel execution strategy:**
- Batch 1: Tasks 3+4 (Introduction + Ch 1) — foundational, independent
- Batch 2: Tasks 5+6 (Ch 2 + Ch 3) — can start once Batch 1 establishes voice
- Batch 3: Tasks 7+8 (Ch 4 + Ch 5) — methodology, independent
- Batch 4: Tasks 9+10 (Ch 6 + Ch 7) — application, independent
- Batch 5: Task 11 (Ch 8) — capstone, benefits from all previous chapters but can start BDP research in parallel
- Batch 6: Tasks 12-15 (back matter + build) — after all chapters complete
- Batch 7: Tasks 16-17 (QA + index) — final pass
