---
name: mop
description: >
  Produces complete Manuals of Operations (MOPs) for specific BARMM entities — Ministries,
  Offices, Agencies, Divisions, and LGUs. Use this skill when the user asks to "create a MOP",
  "manual of operations", "MOP for [office]", "operations manual for [division]", "document our
  procedures", "standardize our processes", "SOP manual for [entity]", "write a MOP", "draft
  an operations manual", "formulate a MOP", "MOP formulation", "operational procedures manual".
  This skill produces the ACTUAL MOP document with chapters, procedures, flowcharts, and forms
  for a specific organizational unit. Do NOT trigger for guidebooks about MOP methodology or
  how to create MOPs in general (use /guidebook-writer). Do NOT trigger for individual SOPs
  or standalone procedures (handle inline). Do NOT trigger for CSW documents (use /csw).
---

# MOP -- Manual of Operations Producer

Produce publication-ready Manuals of Operations for BARMM entities following the 7-Phase MOP Formulation Methodology. Each MOP is tailored to the entity's mandate, structure, and operational scope -- from full 9-chapter Provincial MOPs to focused 3-4 chapter Office MOPs.

## How This Skill Relates to Others

| Need | This Skill Does | Delegates To |
|------|----------------|--------------|
| Bangsamoro domain context | Loads before drafting | `/bangsamoro` |
| Legal compliance check | Flags BAA/BOL references | `/legal-reviewer` |
| Fact verification | Verifies names, titles, structures | `/fact-checker` |
| CSW wrapper for submission | MOP formulation IS a CSW assignment | `/csw` |
| Training rollout | Implementation training plan | `/training-assistant` |
| Guidebook about MOP methodology | Not this skill | `/guidebook-writer` |

## Verification Protocol

This skill follows the Universal Verification Framework (Prevent → Detect → Confirm).
Read `~/.gemini/skills/fact-checker/references/verification-framework.md` for the full protocol.
Read `~/.gemini/skills/fact-checker/references/source-preload-protocol.md` — MANDATORY: load source text BEFORE writing any citation. No claims from training data when local source exists.
If a claim cannot be verified against loaded source files, mark it `[UNVERIFIED]` — never guess or fabricate. See source-preload-protocol.md Section 4.

**Before writing (PREVENT):**
1. Invoke `/bangsamoro` to load domain context
2. Read the fact-check error log at `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md`
3. Read authoritative reference files relevant to the topic

**After writing (DETECT):**
Invoke `/fact-checker` on the complete document.

**Before delivery (CONFIRM):**
Present the fact-check report to the user. Fix all errors before delivery.

---

## Phase 1: SCOPE -- Office Profile Interview

Before drafting, gather these inputs. Skip questions already answered in the user's prompt.

1. **Entity** -- Which BARMM entity? (Ministry, Office, Agency, LGU, Division)
2. **Division/Unit** -- Which specific division or unit within the entity?
3. **Mandate** -- Legal basis (BAA 13 provisions, enabling BAA, executive order)
4. **Organizational Structure** -- Current org chart, staffing complement, reporting lines
5. **Key Processes** -- Major outputs and services delivered
6. **Existing Documentation** -- Any current SOPs, manuals, issuances, or office orders
7. **MOP Scope** -- Full entity MOP (9 chapters) or division-level (5-6 chapters) or office-level (3-4 chapters)
8. **Stakeholders** -- Who will use this MOP? Who approves it?

After the interview, invoke `/bangsamoro` to load domain context.

### Scope Determination

| Entity Type | Recommended Chapters | Typical Length |
|-------------|---------------------|----------------|
| Provincial/Ministry | Full 9 chapters | 80-150 pages |
| Division | 5-6 chapters (I-III, V-VI, selected VII-VIII) | 40-80 pages |
| Office/Unit | 3-4 chapters (I-II, core function chapter, IX) | 20-40 pages |

---

## Phase 2: ASSESS -- Needs Assessment

1. **Gap analysis** -- Compare current documented procedures against actual practice
2. **Stakeholder mapping** -- Identify process owners, SMEs, approval authorities
3. **Priority areas** -- Rank processes by impact, compliance risk, and frequency
4. **Data gathering plan** -- Which staff to interview, which documents to review

Read `${GEMINI_SKILL_DIR}/references/mop-compliance-checklist.md` for BAA 13 requirements that apply to the entity type.

---

## Phase 3: GATHER -- Information Gathering

1. **Document review** -- Collect and analyze existing issuances, office orders, forms
2. **Stakeholder interviews** -- Structured questions per process area (read `${GEMINI_SKILL_DIR}/references/mop-process-mapping.md` for interview methodology)
3. **Workflow observation** -- Document actual steps, decision points, handoffs
4. **Process mapping** -- Create flowcharts and RACI matrices for each key process. For process flowcharts and swimlane diagrams, use the `/excalidraw` skill with BARMM palette. Render to PNG and embed in the chapter markdown. For process infographics, visual SOPs, and one-page visual summaries, use `/visualize` to generate self-contained HTML visualizations that can be converted to PNG for embedding.

---

## Phase 4: DRAFT -- Chapter-by-Chapter Writing

### MOP Chapter Structure (9-Chapter Pattern)

Read `${GEMINI_SKILL_DIR}/references/mop-chapter-structure.md` for detailed sub-sections and templates per chapter.

| Ch. | Title | Core Content |
|-----|-------|-------------|
| I | Introduction | Purpose, scope, legal basis, definitions, amendment procedures |
| II | Organizational Structure | Org chart, departments/divisions, roles and responsibilities |
| III | Human Resources | Staffing, recruitment, performance evaluation, leave management |
| IV | Financial Management | Budgeting, revenue collection, accounting, audit, disbursement |
| V | Planning and Programming | Development planning, work and financial planning, M&E framework |
| VI | Service Delivery | Frontline services, citizen feedback, service standards |
| VII | Procurement and Property Management | Procurement process, asset management, inventory |
| VIII | Reporting and Accountability | Reporting requirements, transparency mechanisms, records management |
| IX | Annexes | Forms, flowcharts, directory, legal references, glossary |

### Drafting Rules

- Write procedures in step-by-step format with numbered actions
- Include responsible party, timeline, and required forms for each procedure
- Use flowcharts for processes with decision points (read process mapping reference)
- Cross-reference related procedures across chapters
- Include the legal basis (BAA, BOL article, office order) for each policy
- Use consistent numbering: Chapter.Section.Subsection (e.g., 3.2.1)

### Chapter Adaptation

Not every entity needs all 9 chapters. For smaller entities:

- **Always include**: Chapters I (Introduction), II (Org Structure), and IX (Annexes)
- **Core function chapters**: Select from III-VIII based on the entity's actual operations
- **Merge where appropriate**: Small offices may combine HR + Finance into one chapter

---

## Phase 5: REVIEW -- Quality Pipeline

Run these checks before finalizing:

1. **Fact-check** (invoke `/fact-checker`) -- Verify official names, titles, organizational references
2. **Legal review** (invoke `/legal-reviewer`) -- Verify BAA/BOL citations, compliance requirements
3. **Consistency check** -- Ensure all cross-references resolve, no placeholder text remains
4. **Completeness check** -- Every procedure has: steps, responsible party, timeline, forms, legal basis
5. **Compliance check** -- Read `${GEMINI_SKILL_DIR}/references/mop-compliance-checklist.md` to verify all mandatory elements are present

### Severity-Based Fixes

- **CRITICAL** (wrong legal citations, incorrect org structure, misnamed officials): Must fix before finalization
- **MINOR** (formatting, style inconsistencies): Should fix but does not block

---

## Phase 6: IMPLEMENT -- Rollout

1. **Transmittal** -- Generate transmittal memo using `${GEMINI_SKILL_DIR}/assets/mop-transmittal-template.md`
2. **CSW wrapper** -- Since MOP formulation is a CSW assignment, invoke `/csw` if the user needs the full CSW package
3. **Implementation plan** -- Timeline for rollout, orientation schedule, feedback collection
4. **Training** -- Delegate to `/training-assistant` to design MOP orientation sessions for staff
5. **M&E framework** -- Include review schedule (annual), amendment procedures, feedback mechanisms

---

## Reference Files

| File | When to Read |
|------|-------------|
| `references/mop-chapter-structure.md` | Phase 4 -- detailed chapter templates with sub-sections and interview guides |
| `references/mop-process-mapping.md` | Phase 3 -- process documentation methodology, interview techniques, SOP template |
| `references/mop-compliance-checklist.md` | Phases 2 and 5 -- BAA 13 requirements, BOL compliance, mandatory elements |
| `assets/mop-transmittal-template.md` | Phase 6 -- transmittal memorandum for MOP submission |

---

## Output Format

Produce the MOP in markdown organized by chapter. When the user approves, generate DOCX using `/docx` for formal submission. Each chapter should be a separate section with clear headers following the numbering convention (Chapter.Section.Subsection).

## Gotchas

- BOL article numbers are the #1 fabrication target — always verify against ~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/
- BAA numbers are the #2 fabrication target — verify against ~/Vault/bangsamoro/bangsamoro-laws/index.md
- Use BARMM ministry abbreviations (MFBM not DBM, MOLE not DOLE, MBHTE not DepEd, MILG not DILG) — never national equivalents
- Mas Matatag na Bangsamoro Agenda (2026-2028) replaces 12-Point Priority Agenda — update all references
- Never cite guidebooks as primary sources — trace back to enacted law (BAA, RA, BOL)
- A wrong BAA number, BOL article, or official title is 3x worse than writing [UNVERIFIED]. When in doubt, mark it.
- Organizational structures must match actual BTA/Ministry org charts, not assumed hierarchies
- Process flows must reference specific BAA provisions that authorize each function
- Staffing tables must use BARMM position titles and salary grades, not national CSC equivalents

## Subagent Honesty Rules

Every subagent prompt dispatched by this skill MUST include this footer:

> HONESTY RULES:
> 1. Only extract values explicitly stated in source documents. If ambiguous or missing, leave blank with a one-line reason.
> 2. A wrong answer is 3x worse than a blank answer. When in doubt, leave it blank.
> 3. Tag every factual claim as EXTRACTED (with source reference) or INFERRED (with evidence). Inferred claims will be verified first.
