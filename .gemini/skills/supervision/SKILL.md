---
name: supervision
description: >
  This skill should be used when the user asks to "design a supervision system",
  "supervision system for [entity]", "supervisory development", "supervisory
  competencies", "supervisor training", "division chief training", "performance
  management system", "coaching framework for supervisors", "supervision policy",
  "how to manage staff", "how to evaluate performance", "delegation framework",
  "supervisory development course", "build supervisor capacity", "supervision
  for BARMM", "design supervision for [ministry]", or needs to create a framework
  for how supervisors and division chiefs manage, evaluate, coach, and develop
  their staff. Also trigger when the user references the MDN Supervision System,
  12 supervisory competencies, or needs a supervision M&E framework. Do NOT
  trigger for staff-level CSW production (use /csw), training package generation
  (use /training-assistant), or standalone policy recommendations (use
  /policy-recommendation).
---

# Supervision — Supervision System Designer

Design and implement supervision systems for BARMM entities. A supervision system is the organizational framework within which supervisors and division chiefs operate — it defines how they receive and evaluate staff work, manage performance, delegate authority, provide coaching, and ensure accountability.

This skill serves **supervisors and division chiefs** (the people who manage staff), not the staff themselves. For staff-level Complete Staff Work, use `/csw`.

## How This Skill Relates to Others

| Need | This skill handles | Delegates to |
|---|---|---|
| Supervision system document | Full design (all 4 phases) | `/csw` SV template for formal CSW format |
| Supervisory development course | Course design + competency framework | `/training-assistant` for materials |
| Supervision policy as formal recommendation | System design + policy rationale | `/policy-recommendation` for the document |
| BARMM governance context | Triggers domain loading | `/bangsamoro` for verified facts |

---

## Phase 1: ASSESS — Supervision Needs Assessment

Before designing anything, conduct this assessment. Skip questions already answered.

### Required Inputs

1. **Entity** — Which BARMM entity? (Ministry, Office, Agency, LGU, Parliament office)
2. **Target supervisors** — Who will use this system? (Directors, Division Chiefs, Section Heads, Unit Heads)
3. **Current state** — What supervision practices exist today? (formal/informal, documented/undocumented)
4. **Staffing** — How many supervisors? How many staff per supervisor (span of control)?
5. **Pain points** — What supervision problems exist? (unclear roles, no feedback culture, inconsistent evaluation, no coaching, weak delegation)
6. **Desired outcomes** — What should the supervision system achieve? (improved performance, staff development, accountability, CSW quality)
7. **Islamic governance alignment** — Should the system explicitly integrate Islamic leadership principles? (integrity/amanah, justice/adl, consultation/shura, compassion/rahmah, trustworthiness/sidq)

### Gap Analysis

After intake, assess gaps across the 5 supervisory competency clusters:

| Cluster | Key Question |
|---|---|
| Personal Effectiveness | Do supervisors understand their role transition from doer to leader? |
| Performance Management | Is there a structured cycle (plan, monitor, evaluate, improve)? |
| Coaching & Mentoring | Do supervisors give feedback and develop their staff? |
| Leading Teams | Can supervisors build team cohesion and manage cross-functional work? |
| Managing Change | Can supervisors lead their teams through organizational transitions? |

**Output**: Supervision Needs Assessment Report (2-3 pages) following this structure:

```markdown
## Supervision Needs Assessment — [Entity Name]
### 1. Entity Profile (mandate, structure, staffing, supervisory span)
### 2. Current Supervision Practices (what exists today, formal vs. informal)
### 3. Gap Analysis (scored across 5 clusters: Personal Effectiveness, Performance Management, Coaching, Teams, Change)
### 4. Priority Recommendations (top 3-5 actions ranked by impact)
```

### Example: Phase 1 Input/Output

**User says**: "Design a supervision system for the Ministry of Health"

**Phase 1 produces**:
> **Entity**: Ministry of Health — BARMM. 6 divisions, 23 provincial hospitals, ~1,200 staff.
> **Target supervisors**: Division Chiefs (6) + Hospital Chiefs (23) + Section Heads (~40).
> **Current state**: No formal supervision policy. Performance evaluation done annually per CSC SPMS but no ongoing coaching/feedback system. Delegation is informal.
> **Gap analysis**: Strongest in Performance Management (SPMS exists). Weakest in Coaching (no structured feedback) and Change Management (hospital transfers lack transition protocols).
> **Priority recommendations**: (1) Implement monthly check-in protocol, (2) Train Division Chiefs on SBI feedback, (3) Create delegation matrix for hospital operations.

---

## Phase 2: DESIGN — Supervision System Design

Read `${GEMINI_SKILL_DIR}/references/supervision-system-template.md` for the full template structure with all sections and guide notes.

### Core Components

1. **Policy Statement** — Philosophy, objectives, Islamic governance principles
2. **Supervisory Roles** — Expectations by level (Director, Division Chief, Section Head)
3. **Competency Framework** — Read `${GEMINI_SKILL_DIR}/references/supervisory-competencies.md` for the 12 competencies
4. **Performance Management Cycle** — Planning, monitoring, evaluation, improvement
5. **Coaching and Feedback Protocols** — Check-in cadences, feedback models, documentation
6. **Delegation Matrix** — Authority levels, escalation paths, acting authority
7. **Staff Development Framework** — IDPs, career pathing, training plans
8. **Accountability Mechanisms** — Reporting, audits, progressive discipline, grievance
9. **M&E for the System** — How the supervision system itself is reviewed and improved

### Design Principles

- **Coaching over compliance** — supervision develops people, not just checks boxes
- **Moral governance** — integrates Islamic leadership values (amanah, adl, shura, rahmah, sidq)
- **CSW integration** — supervision touchpoints map to ADDRESS IT steps (via `/csw` SV template)
- **Proportionate** — scaled to entity size and supervisory span of control
- **Evidence-based** — built on the 12 supervisory competencies from the MDN model

**Output**: Draft Supervision System Document (15-30 pages depending on entity complexity)

### Example: Phase 2 Excerpt

> **Section III: Supervisory Roles and Responsibilities**
>
> **Division Chief** (Director II / Chief of Division):
> - Conducts monthly check-ins with each Section Head using the 4-step protocol
> - Evaluates staff performance using PPR framework (Performance-Potential-Readiness)
> - Provides feedback using SBI model (Situation-Behavior-Impact)
> - Submits quarterly supervision report to the Director
> - Guided by *amanah* (trustworthiness) in handling personnel matters and *shura* (consultation) in decision-making

---

## Phase 3: DEVELOP — Training and Capacity Building

Read `${GEMINI_SKILL_DIR}/references/supervision-training-design.md` for the 5-day course blueprint.

### Supervisory Development Course Design

1. **Audience analysis** — Current competency levels of target supervisors (use pre-assessment rubric from competencies reference)
2. **Course structure** — 5-day intensive based on the 12 supervisory competencies
3. **Competency mapping** — Which competencies to emphasize based on Phase 1 gap analysis
4. **Materials production** — Delegate to `/training-assistant` for facilitator guide, participant handouts, evaluation forms, pre/post tests
5. **Practicum design** — Scenario-based exercises using the entity's actual supervision challenges
6. **Post-training support** — 90-day coaching plan, peer learning circles, supervisor communities of practice

### The 12 Supervisory Competencies (Quick Reference)

| # | Competency | Supervision Cycle |
|---|---|---|
| 1 | Foundations of Supervision | All phases |
| 2 | Assessing Performance, Potential, and Readiness | Evaluation |
| 3 | Giving Effective Feedback | Monitoring, Evaluation |
| 4 | Coaching for Performance and Development | Improvement |
| 5 | Setting Goals and Expectations | Planning |
| 6 | Conducting Effective Check-Ins | Monitoring |
| 7 | Managing Underperformance | Evaluation, Improvement |
| 8 | Developing Talent | Improvement |
| 9 | Leading Teams | All phases |
| 10 | Managing Change | All phases |
| 11 | Delegation and Empowerment | Planning, Monitoring |
| 12 | Building a Culture of Accountability | All phases |

Full definitions, key behaviors, and development activities are in the competencies reference file.

**Output**: Supervisory Development Course Design Document + delegation to `/training-assistant`

---

## Phase 4: INSTITUTIONALIZE — Policy and Implementation

### Policy Document Production

1. **Supervision policy draft** — Formal policy document based on the system design from Phase 2
2. **Issuance pathway** — Determine the right instrument:
   - Ministry Order (for ministry-level systems)
   - Office Order (for agency/office-level systems)
   - Executive Order (for cross-cutting systems)
3. **CSW format** — If the supervision policy needs formal CSW transmittal, delegate to `/csw` using the SV template type
4. **Policy recommendation** — If the system needs to go through a policy approval process, delegate to `/policy-recommendation`

### Implementation Plan

- Phased rollout: pilot division, then entity-wide
- Training schedule aligned with the Supervisory Development Course from Phase 3
- Quick wins: immediate improvements supervisors can implement (weekly check-ins, feedback protocols)
- Communication plan: how to introduce the system to supervisors and staff

### M&E Framework

For supervision cycle diagrams and organizational flowcharts, use `/excalidraw`. For supervision dashboard visuals and one-page visual summaries, use `/visualize` to generate self-contained HTML visualizations that can be converted to PNG for embedding.

- **Supervision system health indicators**: check-in compliance rate, feedback frequency, IDP completion rate, staff satisfaction with supervision
- **Review cycle**: semi-annual operational review, annual comprehensive review
- **Feedback loops**: supervisor satisfaction surveys, staff upward feedback, performance data trends

**Output**: Implementation Plan + M&E Framework, following this structure:

```markdown
## Implementation Plan — [Entity] Supervision System

### 1. Phased Rollout
- Phase A (Month 1-2): Pilot division + supervisor orientation
- Phase B (Month 3-4): Entity-wide rollout + training
- Phase C (Month 5-6): Full operation + first review cycle

### 2. Quick Wins (implement immediately)
- [e.g., Weekly 15-min check-ins using 4-step protocol]
- [e.g., SBI feedback training for all Division Chiefs]

### 3. Training Schedule (linked to Phase 3 course design)

### 4. Communication Plan (how to introduce to supervisors and staff)

### 5. M&E Framework
- Indicators: [check-in compliance, feedback frequency, IDP completion, staff satisfaction]
- Review cycle: semi-annual operational, annual comprehensive
- Feedback loops: supervisor surveys, upward feedback, performance data
```

---

## Handling Edge Cases

### Missing Inputs
- If the entity is specified but staffing data is not, ask: "How many supervisors and staff does [entity] have? What's the typical span of control?"
- If no pain points are stated, offer the 5-cluster gap analysis as a diagnostic starting point
- If Islamic governance alignment preference is unclear, default to including it (it's expected in BARMM context) but confirm

### Partial Invocations
- If the user requests only Phase 3 (training) without Phase 1-2, ask: "Has a supervision needs assessment and system design been completed? If so, share the key findings so the training can target the right gaps."
- If the user requests only Phase 2 (design), proceed but note assumptions about gaps that would normally come from Phase 1

### Ambiguous Requests
- "Help me with supervision" → Ask: "Do you need a complete supervision system (Phases 1-4), a supervisory development course (Phase 3), or a specific tool like a feedback protocol?"
- "My staff are underperforming" → This could be a supervision issue OR a staff competency issue. Use the PPR grid (from tools reference) to diagnose: Is it a performance problem (supervisor should coach) or a CSW skill gap (route to `/csw` training)?

### Skill Routing Example
**User says**: "Train my staff on how to write briefers"
**Response**: This is a staff CSW competency need, not a supervision system task. Route to `/csw` Phase 5 (Training Mode) which covers CSW training using the ACSCCRaPATFEE framework. The `/supervision` skill would be relevant if the question were "How should I evaluate the quality of my staff's briefers?" — that's a supervisor evaluating CSW quality.

---

## Reference Files — Progressive Loading

Load only what each phase needs to conserve context:

| Phase | Read These References | Skip These |
|---|---|---|
| **Phase 1 only** | No references needed (assessment questions are in SKILL.md) | All — save tokens |
| **Phase 2** | `supervisory-competencies.md` + `supervision-system-template.md` + `supervisory-tools-and-frameworks.md` | training-design, csw-integration |
| **Phase 3** | `supervision-training-design.md` + `supervisory-tools-and-frameworks.md` | system-template |
| **Phase 4** | `supervision-csw-integration.md` (for formal policy CSW) | competencies, tools |
| **Parliament context** | Also read `parliament-staff-competencies.md` | — |
| **CSW quality diagnosis** | Also read `supervision-csw-integration.md` | — |

### Full Reference Index

| File | Content |
|------|---------|
| `references/supervisory-competencies.md` | 12 competencies with definitions, rubrics, and supervision cycle mapping |
| `references/supervision-system-template.md` | 10-section system design template with Islamic governance principles |
| `references/supervision-training-design.md` | 5-day Supervisory Development Course blueprint |
| `references/supervision-csw-integration.md` | How supervision and CSW connect, CSW quality diagnosis, transmittal workflow |
| `references/parliament-staff-competencies.md` | 25 Parliament staff competencies (shared with /csw) |
| `references/supervisory-tools-and-frameworks.md` | PPR grid, SBI feedback, coaching process, goal setting, check-ins, performance evaluation, 60-skill framework |

---

## Domain Context

Invoke `/bangsamoro` at the start of any supervision system design for a BARMM entity to load verified governance context (officials, BOL provisions, BDP goals, organizational mandates).

## Gotchas

- BOL article numbers are the #1 fabrication target — always verify against ~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/
- BAA numbers are the #2 fabrication target — verify against ~/Vault/bangsamoro/bangsamoro-laws/index.md
- Use BARMM ministry abbreviations (MFBM not DBM, MOLE not DOLE, MBHTE not DepEd, MILG not DILG) — never national equivalents
- Mas Matatag na Bangsamoro Agenda (2026-2028) replaces 12-Point Priority Agenda — update all references
- Never cite guidebooks as primary sources — trace back to enacted law (BAA, RA, BOL)
- A wrong BAA number, BOL article, or official title is 3x worse than writing [UNVERIFIED]. When in doubt, mark it.
- Supervisory competency frameworks must align with BARMM HR policies, not generic CSC frameworks
- Division chief responsibilities vary by Ministry — always verify against the specific entity's BAA mandate
- Performance evaluation criteria must reference the specific BAA that created the supervisory position

## Subagent Honesty Rules

Every subagent prompt dispatched by this skill MUST include this footer:

> HONESTY RULES:
> 1. Only extract values explicitly stated in source documents. If ambiguous or missing, leave blank with a one-line reason.
> 2. A wrong answer is 3x worse than a blank answer. When in doubt, leave it blank.
> 3. Tag every factual claim as EXTRACTED (with source reference) or INFERRED (with evidence). Inferred claims will be verified first.
