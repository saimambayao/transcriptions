# BARMM Guidebook Production Plan

**Created**: 2026-03-26
**Author**: Saidamen R. Mambayao (with Claude Code)
**Purpose**: Execution plan for remaining guidebooks. Pick up in next session with "execute guidebook plan" or reference specific guidebook by title.

---

## Completed Guidebooks (6)

| # | Guidebook | Words | Pages | Status |
|---|---|---|---|---|
| 1 | Bill Drafting Guidebook (ver02) | ~100K | 330 | Published PDF/DOCX |
| 2 | Bill Drafting MOP | ~10K | ~40 | Published PDF/DOCX |
| 3 | CSW Guidebook (ADDRESS IT) | 33,394 | ~190 | Published PDF/DOCX |
| 4 | Supervision Guidebook | 33,579 | ~150 | Published PDF/DOCX |
| 5 | Systems Change in the Bangsamoro | ~62K | ~210 | Draft PDF/DOCX (2026-03-27) |
| 6 | Strategic Planning Guidebook (10-Point Framework) | ~80K | ~300 | Draft PDF/DOCX (2026-03-27) |

---

## Remaining Guidebooks (8) — Prioritized

### Priority A: Ready to Build (source material + skill + TOC/template exists)

#### Speech Writing Guidebook

**Composing skill**: `/speech-writer`
**Audience**: Parliament staff (legislative staff, communications officers, speechwriters)
**Tier**: Standard (8-10 chapters, 150-250 pages)
**Pre-existing work**: TOC already drafted during /guidebook-writer eval test at `~/.claude/skills/guidebook-writer/guidebook-writer-workspace/iteration-1/eval-1-speech-writing/with_skill/outputs/toc.md` — 10 chapters, 7 appendices, fully structured with &emsp; indentation
**Source materials**:
- /speech-writer skill (speech types, Islamic protocols, language conventions, rhetorical techniques)
- Bill Drafting Guidebook (proven pattern for chapter structure and voice)
- Existing speeches from parliamentary sessions (if available)
**Chapter structure** (from eval TOC):
1. The Role of Speech in Bangsamoro Governance
2. Understanding Your Speaker
3. Speech Types in the Bangsamoro Parliament (authorship, privilege, manifestation, interpellation, committee, motions)
4. Speeches for Executive and Special Occasions (keynotes, budget, commemorative, crisis)
5. The Speech Writing Process (6-stage workflow)
6. Language, Culture, and Protocol (Islamic greetings, honorifics, 13 ethnolinguistic groups)
7. Rhetorical Techniques for Bangsamoro Governance
8. From Speech to Public Communication (social media, press, archiving)
9. Common Mistakes and How to Avoid Them
10. Quality Standards and Review
**Appendices**: A-G (speech templates, Islamic greeting protocols, officials reference, sample speeches, speaker profile template, quality checklist, process flowchart)
**Estimated effort**: 1 session (TOC exists, skill is rich)
**Dependencies**: None — ready to execute

---

#### Policy Recommendations Guidebook

**Composing skill**: `/policy-recommendation` (Bardach's Eightfold Path)
**Audience**: MOA policy units, Parliament committee staff, consultants/resource persons
**Tier**: Standard (8-10 chapters, 150-250 pages)
**Pre-existing work**: Chapter template exists in `references/chapter-templates.md` (Policy Recommendations section — 10 chapters + 5 appendices)
**Source materials**:
- /policy-recommendation skill (Bardach methodology, 3 document types: recommendation, brief, memo)
- /policy-paper skill (Tier 3 comprehensive papers)
- 20 OOBC Policy Recommendations + 10 Policy Briefs (real worked examples)
- NotebookLM research on policy frameworks (90+ sources from OECD, World Bank, ADB, UN)
- PRLS-LRD-Policy-Notes-003-2022 (sample to improve upon)
**Chapter structure** (from chapter-templates.md):
1. Introduction — Purpose, audience, how to use
2. The Policy Cycle in BARMM — Problem identification → analysis → formulation → adoption → implementation → evaluation
3. Understanding the Policy Environment — BOL framework, BDP 2023-2028, stakeholder mapping
4. Evidence-Based Policy Analysis — Research methods, data sources, needs assessment
5. Structuring a Policy Recommendation — The 4-section template (Context, Framework, Implementation, Management)
6. Legal Foundations and Compliance — BOL, BAAs, Shari'ah, avoiding ultra vires
7. Budgetary and Financial Analysis — Costing, funding sources, BAA 84, sustainability
8. Stakeholder Consultation and Validation — Protocols, community engagement, interagency coordination
9. Quality Review and Approval — Checklist, peer review, approval chain, transmittal
10. From Recommendation to Action — Implementation monitoring, M&E, feedback loops
**Appendices**: A-E (annotated template, evidence checklist, stakeholder guide, sample recommendation, glossary)
**Estimated effort**: 1 session
**Dependencies**: None — ready to execute

---

#### MOP Formulation Guidebook

**Composing skill**: `/mop` + MOP Formulation Methodology reference
**Audience**: MOA staff tasked with creating MOPs, consultants, organizational development officers
**Tier**: Standard (8-10 chapters, 150-250 pages)
**Pre-existing work**:
- `references/mop-formulation-methodology.md` in /guidebook-writer (condensed 46-page methodology)
- Chapter template exists in `references/chapter-templates.md` (Manual of Operations section — 10 chapters)
- Real MOP example: MDN Provincial MOP (158K chars, 9 chapters)
- PRLS-LRD and PRLS-LMLAD MOPs (samples to improve upon)
- `references/improvement-patterns.md` (specific improvements over PRLS MOPs)
**Source materials**:
- User's "Manual on How to Formulate and Implement a MOP for BARMM Ministries and Offices" (46 pages, ©SRM)
- /mop skill (chapter structure, process mapping, compliance checklist)
- MDN Provincial MOP (real 9-chapter example)
- OOBC MOP (real 9-chapter example produced in earlier session)
**Chapter structure** (7-phase MOP formulation process):
1. Introduction — Why MOPs matter, legal basis (BAA 13), this guidebook's purpose
2. Planning and Preparation — Identifying the need, forming the team (6 roles), needs assessment, project plan
3. Information Gathering — Document review, stakeholder interviews, workflow observation (shadowing, time/motion, process mapping), benchmarking
4. Drafting the Manual — Structure and format, common sections (6), numbering, typography, visual aids, consistency
5. Review and Approval — Circulating drafts, incorporating feedback, obtaining authority approval
6. Implementation and Training — Implementation plan, staff communication, training sessions, ongoing support
7. Monitoring and Evaluation — KPIs, effectiveness assessment, user feedback, updates and revisions
8. The MOP Chapter Structure — Detailed guide for each of the 9 standard MOP chapters
9. Process Mapping Techniques — Flowcharts, swim lanes, RACI matrices, SOP entry format
10. Compliance and Legal Framework — BAA 13 requirements, BOL provisions, mandatory forms
**Appendices**: A-G (office profile template, workflow procedure template, forms collection, quality checklist, performance dashboard, sample MOP excerpt, glossary)
**Estimated effort**: 1 session
**Dependencies**: None — ready to execute

---

### Priority B: Moderate Preparation Needed

#### Legal Review Guidebook

**Composing skill**: `/legal-reviewer`
**Audience**: Parliament legal division, MOA legal units, PRLS legal staff
**Tier**: Compact (6-8 chapters, 80-120 pages)
**Pre-existing work**: Chapter template exists in `references/chapter-templates.md` (Legal Review section — 8 chapters + 4 appendices)
**Source materials**:
- /legal-reviewer skill (verification methodology, source priority hierarchy)
- /legal-assistant skill (Philippine/Bangsamoro legal analysis)
- BOL verbatim transcription (18 articles at ~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/)
- 89 BAA markdowns (complete local archive)
- Bill Drafting Guidebook Chapter 12 (Quality Review — partial overlap)
**Chapter structure** (from chapter-templates.md):
1. Introduction — Role of legal review in Bangsamoro governance
2. The Bangsamoro Legal Hierarchy — Constitution → BOL → BAAs → EOs → Local Ordinances
3. Reviewing Bills and Resolutions — Constitutionality, BOL compliance, BAA consistency, Shari'ah, drafting quality
4. Reviewing MOA Legal Documents — Administrative orders, contracts, MOAs/MOUs, BAA 13 compliance
5. Verification Methodology — Source hierarchy, verbatim accuracy, citation formatting
6. Common Legal Issues in BARMM Legislation — Ultra vires, overlapping authority, reserved powers, Shari'ah conflicts
7. Preparing Legal Opinions and Memoranda — Structure, analysis framework, transmittal
8. Quality Standards — Review checklist, peer review, approval workflow
**Appendices**: A-D (legal review checklist, BOL enumerated powers, sample legal opinion, glossary)
**Estimated effort**: 1 session
**Dependencies**: None — but benefits from reviewing actual legal opinions from Parliament if available

---

#### Policy Notes Guidebook

**Composing skill**: None (standalone — this is a format guide)
**Audience**: PRLS (Parliament), MOA policy/research units
**Tier**: Compact (6-8 chapters, 80-120 pages)
**Pre-existing work**: Chapter template exists in `references/chapter-templates.md` (Policy Notes section — 8 chapters + 5 appendices). Improvement patterns documented in `references/improvement-patterns.md`.
**Source materials**:
- PRLS-LRD-Policy-Notes-003-2022 (existing format to improve upon — ISSN 2815-2115)
- /policy-recommendation skill (for methodology section)
- Improvement patterns: add methodology section, add policy options before recommendation, expand depth, add data visualization, standardize citations, include impact tracking
**Chapter structure** (from chapter-templates.md):
1. Introduction — Role of policy notes in Bangsamoro governance, the PRLS Policy Notes Series
2. Types of Policy Notes — Issue briefs, analytical papers, position papers, situation reports
3. Research Methodology — Literature review, data analysis, stakeholder consultation, legal analysis
4. Structure and Format — Enhanced format (9 sections including methodology + policy options)
5. Writing Standards — Academic rigor with accessibility, Chicago footnotes, tone calibration
6. Review and Publication — Internal review, peer review, ISSN tracking, publication schedule
7. Dissemination and Impact — Distribution to MPs, committee referral, tracking policy influence
8. Building a Policy Research Agenda — Aligning with BDP goals, proactive scanning
**Appendices**: A-E (enhanced template, research methodology checklist, citation guide, 3 sample policy notes, glossary)
**Estimated effort**: 1 session
**Dependencies**: None — but reviewing 2-3 actual PRLS Policy Notes for voice and format baseline would strengthen it

---

#### Competency Development Guidebook

**Composing skill**: `/csw` (ACSCCRaPATFEE) + `/supervision` (12 supervisory) + Parliament Staff Competencies
**Audience**: HR units, training coordinators, supervisors, organizational development officers across all BARMM entities
**Tier**: Comprehensive (12+ chapters, 250+ pages)
**Pre-existing work**: Three complete competency frameworks already documented:
- Parliament Staff Competencies (25 competencies, 3 tiers, 4-level rubric) — in `/csw` and `/supervision` references
- ACSCCRaPATFEE (12 CSW competencies, 5-level + 3-tier indicators) — in `/csw` references
- 12 Supervisory Competencies (MDN model, supervision cycle mapped) — in `/supervision` references
- CSW Competency Assessment Tool (7-level, 42 questions) — in `/csw` references
- 60-Skill Supervisory Framework (Managing Self/Others/Systems) — in `/supervision` references
**Chapter structure** (custom — no existing template):
1. Introduction — Why competency development matters in BARMM governance
2. The BARMM Competency Landscape — Three frameworks, how they connect, who uses which
3. Core Competencies (5) — Critical thinking, communication, collaboration, CSW, public service/cultural competence
4. Leadership Competencies (5) — Planning for change, high-trust culture, disciplined execution, high-performance teams, leading change
5. CSW Practitioner Competencies (ACSCCRaPATFEE — 12) — Deep dive with rubrics, indicators, development activities
6. Supervisory Competencies (12) — Deep dive with PPR grid, SBI feedback, coaching, evaluation
7. Functional Competencies by Role — PAOs, LSOs, PIMAOs (Parliament-specific)
8. Competency Assessment Methods — Self-assessment, supervisor assessment, 360-degree, pre/post training
9. Individual Development Plans (IDPs) — Design, implementation, monitoring
10. Organizational Competency Strategy — Mapping competencies to BDP goals, training plans, career pathing
11. Competency-Based Performance Management — Integrating competencies into SPMS, evaluation, promotion
12. Building a Learning Organization — Continuous development, knowledge management, communities of practice
**Appendices**: A-H (competency matrices, assessment tools by framework, IDP template, training needs analysis template, career path maps, learning resource guide, competency dictionary, glossary)
**Estimated effort**: 2 sessions (largest guidebook — unifies 3 frameworks + creates new content)
**Dependencies**: Best created after the CSW and Supervision guidebooks (which are now done)

---

### Priority C: Lower Priority / May Not Need Standalone Guidebook

#### Legislative Briefer (CSW) Guidebook

**Composing skill**: `/legislative-briefer`
**Audience**: Parliament PRLS staff, committee secretariat, legislative researchers
**Tier**: Standard (10-12 chapters, 150-250 pages)
**Pre-existing work**: Chapter template exists in `references/chapter-templates.md` (Legislative Briefer section — 12 chapters + 6 appendices). The `/legislative-briefer` skill is already the richest Parliamentary skill.
**Overlap concern**: The CSW Guidebook Chapter 11 already covers "CSW for Parliamentary Committees" including the 13-section briefer mapped to ADDRESS IT. A standalone guidebook would go deeper on each of the 13 sections.
**Decision needed**: Is this a standalone guidebook or an expansion of CSW Guidebook Chapter 11?
- **If standalone**: Dedicate one chapter per section of the 13-section format (deep procedural guide for PRLS staff)
- **If expansion**: Add it as a supplement/companion volume to the CSW Guidebook
**Estimated effort**: 1-2 sessions
**Dependencies**: Decide on standalone vs. companion format first

---

#### Resolution Drafting Guidebook

**Composing skill**: `/resolution-drafter`
**Audience**: Parliament staff
**Tier**: Compact (5-7 chapters, 80-120 pages)
**Overlap concern**: The Bill Drafting Guidebook (ver02) already covers resolutions in Chapter 5 (34.2KB, ~30 pages). A standalone guidebook would be substantial overlap.
**Decision needed**: Is this worth a standalone guidebook, or is the Bill Drafting Guidebook Chapter 5 sufficient?
- **If standalone**: Focus on the specific resolution types unique to BTA (proposed resolutions, committee resolutions, commemorative resolutions) with annotated samples
- **If not needed**: Mark as covered by Bill Drafting Guidebook Chapter 5 + Resolution Drafting MOP (if created)
**Estimated effort**: 0.5 sessions (compact, much content already exists)
**Dependencies**: Review Bill Drafting Guidebook Chapter 5 to assess coverage gap

---

## Execution Plan

### Session 1: Speech Writing + Policy Recommendations (Priority A)
1. Load eval TOC for Speech Writing → execute Phase 3-5 (all chapters + PDF/DOCX)
2. Load chapter template for Policy Recommendations → execute Phase 2-5
3. QA + fact-check both
4. Target: 2 guidebooks, ~50K words

### Session 2: MOP Formulation + Legal Review (Priority A/B)
1. Load chapter template for MOP Formulation → execute Phase 2-5
2. Load chapter template for Legal Review → execute Phase 2-5
3. QA + fact-check both
4. Target: 2 guidebooks, ~40K words

### Session 3: Policy Notes + Competency Development Part 1 (Priority B)
1. Load chapter template for Policy Notes → execute Phase 2-5
2. Start Competency Development guidebook → Phase 1-3 (chapters 1-6)
3. Target: 1.5 guidebooks, ~40K words

### Session 4: Competency Development Part 2 + Decisions (Priority B/C)
1. Complete Competency Development → Phase 3-5 (chapters 7-12 + appendices)
2. Decide on Legislative Briefer (standalone vs. companion) and Resolution Drafting (standalone vs. covered)
3. If standalone: execute Legislative Briefer guidebook
4. Target: 1-2 guidebooks, ~30-50K words

### Total Estimated Output
- **8 guidebooks** across **4 sessions**
- **~160-180K additional words** of guidebook content
- Combined with existing 4 guidebooks: **independent guidebooks totaling ~350K+ words**

---

## Quick Reference: Which Skill Feeds Each Guidebook

```
/guidebook-writer (the engine)
 ├── Bill Drafting Guidebook ← /bill-drafter + /bangsamoro
 ├── CSW Guidebook ← /csw (ADDRESS IT + ACSCCRaPATFEE)
 ├── Supervision Guidebook ← /supervision (12 competencies + tools)
 ├── Speech Writing Guidebook ← /speech-writer
 ├── Policy Recommendations Guidebook ← /policy-recommendation (Bardach)
 ├── MOP Formulation Guidebook ← /mop (formulation methodology)
 ├── Legal Review Guidebook ← /legal-reviewer
 ├── Policy Notes Guidebook ← standalone (improve PRLS format)
 ├── Competency Development Guidebook ← /csw + /supervision + Parliament Staff
 ├── Legislative Briefer Guidebook ← /legislative-briefer [decision pending]
 └── Resolution Drafting Guidebook ← /resolution-drafter [decision pending]
```

---

---

### New Addition: Working with the Bangsamoro Government

**Audience**: Fresh graduates, job seekers, career changers (EXTERNAL — first public-facing guidebook)
**Tier**: Standard (10 chapters, 150-200 pages)
**Composing skill**: `/bangsamoro` (governance context only — no specialized production skill)
**Unique**: Shifts voice from coaching-a-peer to welcoming-a-newcomer. Assumes zero government experience.
**Plan file**: `planning/PLAN-working-with-bangsamoro-government-guidebook.md` (full chapter structure + execution details)
**Legal grounding**: BAA 13, BAA 17 (Civil Service), BOL, CSC rules
**Content**: BARMM structure, position types (plantilla/JO/COS/consultant), salary grades, application process, interview prep, first 90 days, career growth, moral governance, Islamic values
**Execute**: Say **"Build the Working with the Bangsamoro Government guidebook"**

---

## To Execute in Next Session

Reference specific guidebooks by title: "Build the Speech Writing Guidebook", "Build the Legal Review Guidebook", etc.

The plan file is at: `planning/GUIDEBOOK-PRODUCTION-PLAN.md`
