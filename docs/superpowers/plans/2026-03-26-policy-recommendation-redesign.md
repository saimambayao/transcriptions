# Policy Recommendation Skill Redesign — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the /policy-recommendation skill from OOBC-specific to a generic, standards-based policy recommendation tool usable by all BARMM ministries, offices, agencies, and external consultants.

**Architecture:** The skill becomes agency-agnostic with a modular template system. The core SKILL.md uses Bardach's Eightfold Path as its analytical backbone, international standard document structures (World Bank/ADB/OECD-informed), and BARMM-contextualized M&E frameworks. OOBC becomes one reference template among potentially many agency-specific templates.

**Tech Stack:** Claude Code skill (Markdown + YAML frontmatter), reference files for templates and examples.

---

## File Structure

```
policy-recommendation/
├── SKILL.md                              # REWRITE — generic skill, Bardach-based workflow
├── analysis-report.md                    # KEEP — historical record
└── references/
    ├── generic-template.md               # CREATE — standards-based generic template
    ├── oobc-template.md                  # UPDATE — becomes agency-specific example template
    ├── examples.md                       # UPDATE — add generic examples alongside OOBC example
    ├── policy-analysis-guide.md          # CREATE — Bardach's Eightfold Path + tools reference
    └── document-types.md                 # CREATE — brief vs paper vs recommendation guide
```

Sync targets (all 3 locations):
- `~/.claude/skills/policy-recommendation/` (active skill)
- `~/Vault/Claude-Skills/policy-recommendation/` (vault archive, lowercase `skill.md`)
- `~/apps/skills-bucket/policy-recommendation/` (skills-bucket, uppercase `SKILL.md`)

---

### Task 1: Create the Generic Policy Recommendation Template

**Why:** The current template is OOBC-specific. We need a standards-based generic template that any BARMM agency can use, informed by World Bank/ADB/OECD structures validated in research.

**Files:**
- Create: `references/generic-template.md`

- [ ] **Step 1: Write the generic template**

The template must include these sections, synthesized from international standards:

```markdown
---
type: reference
source: Synthesized from World Bank, ADB, OECD/DAC, and UN policy document standards
---

# Policy Recommendation Template

## Reference Number Format
`[AGENCY]-PR-[YYYY]-[XXX]`
- AGENCY: Issuing agency acronym (e.g., MAFAR, MBHTE, OOBC, MILG)
- YYYY: Year of issuance
- XXX: Sequential number

## Complexity Tiers

### Tier 1: Policy Brief (2-8 pages)
Front-loaded structure for decision-makers who need quick action items.
- Executive Summary (1 paragraph)
- Problem Statement and Evidence
- Policy Options and Recommended Action
- Implementation Snapshot
- Appendix: Key Data Tables (optional)

### Tier 2: Standard Policy Recommendation (8-15 pages)
Full analytical structure for formal agency recommendations.
Sections 1-6 below.

### Tier 3: Comprehensive Policy Paper (20+ pages)
Extended analysis for complex, cross-cutting policy issues.
Full sections 1-6 + Extended Evidence Review + Comparative Analysis + Stakeholder Mapping Appendix.

---

## Document Structure (Tier 2 — Standard)

### EXECUTIVE SUMMARY (write last, 3-5 paragraphs)
- Problem and why it matters now
- Proposed policy response (1-2 sentences)
- Expected outcomes and beneficiaries
- Resource implications and timeline
- Key risk and primary mitigation

### 1. CONTEXT AND RATIONALE

**1.1 Problem Statement**
- Clear articulation of the policy gap, issue, or unmet need
- Who is affected and how (with disaggregated data where available)
- Why the current situation is insufficient or unsustainable

**1.2 Situation Analysis**
- Current policy landscape (existing laws, programs, institutional arrangements)
- Root cause analysis (use Problem Tree: causes > core problem > effects)
- Scope and scale (geographic coverage, affected population size, trends)

**1.3 Evidence Base**
- Primary data (needs assessments, consultations, field research)
- Secondary data (PSA statistics, agency reports, academic studies)
- Comparative analysis (similar interventions in other contexts — what worked, what didn't)

**1.4 Strategic Alignment**
- Alignment with BDP 2023-2028 goals (cite specific goal and strategy)
- Alignment with agency mandate (cite enabling legislation — BAA, EO, AO)
- Alignment with national framework (relevant RAs, Philippine Development Plan)
- Alignment with international commitments (SDGs, CEDAW, CRC, where applicable)

### 2. STAKEHOLDER ANALYSIS

**2.1 Stakeholder Mapping**
- Primary stakeholders (direct beneficiaries)
- Secondary stakeholders (implementing agencies, LGUs, partners)
- Tertiary stakeholders (oversight bodies, CSOs, development partners)

**2.2 Power-Interest Matrix**
- High power / high interest → manage closely
- High power / low interest → keep satisfied
- Low power / high interest → keep informed
- Low power / low interest → monitor

**2.3 Consultation Summary**
- Who was consulted, when, and how
- Key findings from consultations
- How stakeholder input shaped the recommendation

### 3. POLICY OPTIONS AND RECOMMENDATION

**3.1 Policy Alternatives**
For each option (minimum 3):
- Description of the intervention
- Expected outcomes
- Estimated cost
- Feasibility assessment (political, technical, administrative, financial)
- Trade-offs

**3.2 Evaluation Criteria**
Apply standard criteria (adapted from OECD/DAC + Bardach):
- **Relevance** — Does it address the root causes identified in Section 1?
- **Effectiveness** — Will it achieve the stated objectives?
- **Efficiency** — Is the cost proportional to expected outcomes?
- **Equity** — Does it reach marginalized groups? Gender-responsive?
- **Sustainability** — Will outcomes persist beyond the intervention period?
- **Political feasibility** — Is there institutional will and legal basis?

**3.3 Recommended Option**
- Which option and why (reference criteria scores)
- Theory of Change narrative (how inputs lead to outcomes lead to impact)
- Logic Model diagram: Inputs > Activities > Outputs > Outcomes > Impact

### 4. IMPLEMENTATION FRAMEWORK

**4.1 Institutional Arrangements**
- Lead agency and specific unit responsible
- Cooperating agencies and their roles
- LGU roles (where applicable)
- National government agency coordination (where applicable)
- Development partner contributions (where applicable)
- Coordination mechanism (inter-agency committee, TWG, etc.)

**4.2 Resource Requirements**
- Budget summary (by year, by component)
- Human resources (new hires, capacity building, technical assistance)
- Infrastructure and equipment needs
- Funding source(s) and mobilization strategy

**4.3 Phased Implementation Plan**
| Phase | Timeline | Key Activities | Milestones | Responsible |
|-------|----------|---------------|------------|-------------|
| Preparation | Months 1-3 | ... | ... | ... |
| Pilot/Launch | Months 4-6 | ... | ... | ... |
| Scale-up | Months 7-12 | ... | ... | ... |
| Full operation | Year 2+ | ... | ... | ... |

### 5. MONITORING, EVALUATION, AND LEARNING (MEL)

**5.1 Results Framework**
| Level | Indicator | Baseline | Target | Data Source | Frequency |
|-------|-----------|----------|--------|-------------|-----------|
| Impact | ... | ... | ... | ... | Annual |
| Outcome | ... | ... | ... | ... | Semi-annual |
| Output | ... | ... | ... | ... | Quarterly |

- All indicators must be SMART (Specific, Measurable, Attainable, Relevant, Time-bound)
- Include at least one sex-disaggregated indicator

**5.2 Data Collection and Reporting**
- Data collection methods and tools
- Reporting schedule and format
- Responsible unit for M&E

**5.3 Evaluation Plan**
- Mid-term review (timing and scope)
- End-of-project evaluation (timing and scope)
- Evaluation criteria (use OECD/DAC 6 criteria: Relevance, Coherence, Effectiveness, Efficiency, Impact, Sustainability)

### 6. RISK MANAGEMENT AND SUSTAINABILITY

**6.1 Risk Assessment**
| Risk | Likelihood | Impact | Mitigation Strategy |
|------|-----------|--------|-------------------|
| ... | High/Med/Low | High/Med/Low | ... |

**6.2 Sustainability Plan**
- Institutional sustainability (how will this be mainstreamed into regular operations?)
- Financial sustainability (recurrent costs and funding after project ends)
- Community ownership (how will beneficiaries sustain outcomes?)

**6.3 Exit Strategy** (if applicable)
- Transition plan
- Handover responsibilities

### APPENDICES
- A. Detailed Implementation Plan / Guidelines
- B. Detailed Budget
- C. Full Risk Register
- D. MEL Framework (expanded results framework)
- E. Stakeholder Consultation Records
- F. Theory of Change Diagram
- G. Legal Basis Summary (relevant legislation excerpts)
```

- [ ] **Step 2: Review template against research findings**

Verify the template includes all validated standards:
- Bardach's Eightfold Path integrated into Section 3 (Options + Criteria + Trade-offs) ✓
- Problem Tree in Section 1.2 ✓
- Stakeholder Analysis as full Section 2 ✓
- Theory of Change + Logic Model in Section 3.3 ✓
- OECD/DAC 6 criteria in Section 5.3 ✓
- Results-Based Management in Section 5.1 ✓
- SMART indicators in Section 5.1 ✓
- Gender mainstreaming in Sections 3.2 and 5.1 ✓
- Contextual adaptation in Section 1.4 ✓

---

### Task 2: Create the Policy Analysis Guide Reference

**Why:** Analysts need a quick reference for the methodologies referenced in the template. This prevents the SKILL.md from being bloated with methodology explanations.

**Files:**
- Create: `references/policy-analysis-guide.md`

- [ ] **Step 1: Write the policy analysis guide**

Content:
1. **Bardach's Eightfold Path** — Full 8 steps with BARMM-contextualized examples
2. **Problem Tree Analysis** — How to construct one (causes > problem > effects)
3. **Stakeholder Analysis** — Power-Interest Matrix with BARMM example
4. **Cost-Benefit Analysis** — When to use, NPV explained simply
5. **Theory of Change** — How to write the narrative + construct the logic model
6. **OECD/DAC Evaluation Criteria** — All 6 criteria defined with policy document application

Each methodology section should be ~200 words max with a practical example from BARMM governance context.

---

### Task 3: Create the Document Types Reference

**Why:** Users need to understand when to use a policy brief vs paper vs recommendation. The current skill conflates them.

**Files:**
- Create: `references/document-types.md`

- [ ] **Step 1: Write the document types guide**

Content — comparison table + guidance for each:
- **Policy Brief** (2-8 pages): Front-loaded, for decision-makers, advocacy or objective
- **Policy Recommendation** (8-15 pages): Strategic, principle-based, full analytical structure — DEFAULT
- **Policy Paper** (20+ pages): Rear-loaded, evidence-heavy, for technical audiences
- **Policy Memo** (1-2 pages): Internal, same as brief but for intra-agency use
- **When to use each** — decision tree based on audience, purpose, and complexity

---

### Task 4: Update OOBC Template to Agency-Specific Example

**Why:** The OOBC template becomes one example of how to customize the generic template for a specific agency. It demonstrates the adaptation pattern.

**Files:**
- Modify: `references/oobc-template.md`

- [ ] **Step 1: Reframe as agency-specific adaptation**

Add a header explaining this is an agency-specific adaptation of the generic template:
```markdown
---
type: reference
source: OOBC-specific adaptation of the Generic Policy Recommendation Template
---

# OOBC Policy Recommendation Template

> This is an agency-specific adaptation of `generic-template.md` for the Office
> for Other Bangsamoro Communities. It demonstrates how to customize the generic
> template for a specific BARMM agency's mandate, target population, and evidence
> sources.

## What's Different from the Generic Template
- Reference number: `OOBC-PR-YYYY-XXX`
- Evidence base: OBC-MANA assessment data + diaspora consultations
- Target communities: Bangsamoro communities OUTSIDE the region
- Strategic alignment: 6 OOBC goal areas (institutional strengthening, rights
  protection, social development, economic development, cultural preservation,
  peace advocacy)
- Stakeholders: Includes host LGUs, national agencies (DepEd, DSWD, DOLE)
```

Keep the existing section structure but mark it as an adaptation. Add notes on what sections change vs stay the same.

---

### Task 5: Update Examples Reference

**Why:** Need generic examples alongside the OOBC-specific one. Consultants working with MAFAR or MBHTE need to see how the template adapts.

**Files:**
- Modify: `references/examples.md`

- [ ] **Step 1: Add a generic executive summary example**

Add an example for a non-OOBC agency (e.g., MAFAR agricultural policy or MBHTE education policy) that shows:
- Different reference number format
- Different evidence sources
- Different institutional framework
- Same analytical rigor and structure

- [ ] **Step 2: Keep existing OOBC example and style demonstrations**

The existing content is good. Just reorder so generic example comes first, OOBC example second, then style before/after demonstrations.

---

### Task 6: Rewrite SKILL.md

**Why:** The main skill file needs to become agency-agnostic, use Bardach's methodology, reference the new generic template, and keep OOBC as one use case.

**Files:**
- Rewrite: `SKILL.md`

- [ ] **Step 1: Rewrite YAML frontmatter**

New description must:
- Remove OOBC-first framing
- Add generic triggers ("policy recommendation for [any agency]")
- Keep OOBC as one trigger among many
- Add triggers for all BARMM agency types
- NOT summarize the workflow (per skill guidelines)

```yaml
---
name: policy-recommendation
description: |
  Draft standards-based policy recommendations for any BARMM ministry, office, or agency,
  or as an external consultant advising BARMM. Produces structured policy documents grounded
  in Bardach's Eightfold Path methodology with World Bank/ADB/OECD-informed structure.
  Supports 4 document types: policy brief (2-5pp), standard recommendation (8-15pp),
  comprehensive policy paper (20+pp), and policy memo (1-2pp).
  Use this skill whenever the user mentions "policy recommendation", "policy brief",
  "policy paper", "policy memo", "policy document", "policy analysis",
  "executive summary for policy", "implementation plan", "M&E framework",
  "risk assessment for policy", "sustainability plan", "stakeholder analysis",
  "theory of change", "problem tree", "cost-benefit analysis", "options analysis",
  "OOBC", "MAFAR", "MBHTE", "MENRE", "MFBM", "MOH", "MHSD", "MIPA", "MILG",
  "MOLE", "MPOS", "MPW", "MOST", "MSSD", "MTIT", "MOTC", "OCM",
  "needs assessment", "policy paper", "diaspora communities",
  "Bangsamoro outside BARMM", or any policy drafting work for BARMM agencies.
  Also trigger when the user provides consultation minutes, needs assessment data,
  or stakeholder feedback and wants to turn it into a policy recommendation.
  For legislative documents (bills, resolutions), use /bill-drafter or /resolution-drafter.
allowed-tools:
  - Read
  - Glob
  - Grep
  - WebSearch
  - WebFetch
  - Write
argument-hint: "[document-type] [policy topic] for [agency] — e.g., 'recommendation on education access for MBHTE' or 'policy brief on agriculture for MAFAR'"
---
```

- [ ] **Step 2: Write the core skill body**

Structure:
1. **Role** — Generic: senior policy analyst for BARMM (not OOBC-specific)
2. **Methodology** — Bardach's Eightfold Path as the analytical backbone (reference `policy-analysis-guide.md`)
3. **Document Types** — Reference `document-types.md` for choosing the right format
4. **Templates** — Generic template is default (`generic-template.md`); agency-specific templates available (`oobc-template.md`)
5. **Skill Composition** — Same composed skills (/bangsamoro, /legal-assistant, /financial-analyst, /humanizer)
6. **Pre-Draft Interview** — Generalized from OOBC to any agency:
   - Problem statement (same)
   - **Agency**: Which BARMM agency is this for? (NEW — replaces "OOBC goal area")
   - **Policy area**: Which sector/mandate area? (NEW — more flexible than 6 OOBC goals)
   - Target population/communities (generalized from "Target OBC communities")
   - Available evidence (generalized)
   - Document type: Brief, Recommendation, Paper, or Memo (expanded from "Complexity tier")
   - Budget source (same)
7. **Workflow** — Bardach-aligned:
   - Step 1: Define the problem (Interview + evidence gathering)
   - Step 2: Assemble evidence (local sources + WebSearch + agency data)
   - Step 3: Construct alternatives (minimum 3 policy options)
   - Step 4: Evaluate options (OECD/DAC criteria + feasibility)
   - Step 4b: Project outcomes and confront trade-offs (Bardach Steps 5-6)
   - Step 5: Draft section by section (using chosen template)
   - Step 6: Write Executive Summary last
   - Step 7: Output (.md or .docx via /docx)
8. **Legal Citations** — Same rules (footnotes for policy papers)
9. **Style Rules** — Same anti-AI-pattern rules + plain language best practices from research
10. **Error Handling** — Expanded table (current 6 + new scenarios for unknown agencies, consultant use)
11. **BARMM Agencies** — Same reference to /bangsamoro's moa-structure.md
12. **Research** — Same tools section
13. **Fact-Check** — Same /fact-checker gate
14. **Agency-Specific Customization** — Section explaining how to adapt the generic template for specific agencies (OOBC example, pattern for others)

- [ ] **Step 3: Review against skill guidelines**

Check against `~/Vault/Claude-Skills/Guidelines.md`:
- Description is trigger-focused, not workflow summary ✓
- Has `allowed-tools` ✓
- Has `argument-hint` ✓
- Progressive disclosure (references load on demand) ✓
- Error handling present ✓
- Examples in references ✓

---

### Task 7: Sync to All Three Locations

**Files:**
- Sync to: `~/.claude/skills/policy-recommendation/` (SKILL.md + references/)
- Sync to: `~/Vault/Claude-Skills/policy-recommendation/` (skill.md + references/)
- Sync to: `~/apps/skills-bucket/policy-recommendation/` (SKILL.md + references/)

**Direction: Active skill directory (`~/.claude/skills/policy-recommendation/`) is the source of truth. All syncs copy FROM active TO targets.**

- [ ] **Step 1: Ensure skills-bucket has oobc-template.md** (currently missing from skills-bucket/references/)
- [ ] **Step 2: Copy from active skill dir to vault** (vault uses lowercase `skill.md`)
- [ ] **Step 3: Copy from active skill dir to skills-bucket** (skills-bucket uses uppercase `SKILL.md`)
- [ ] **Step 4: Verify all three locations have identical content** (excluding `analysis-report.md` which only lives in active skill dir)

Run: `diff -rq` between the three directories, ignoring filename case of skill.md/SKILL.md and analysis-report.md.

---

### Task 8: Update Vault Index

**Files:**
- Modify: `~/Vault/Claude-Skills/index.md`

- [ ] **Step 1: Update the policy-recommendation entry**

Change from OOBC-focused description to generic description reflecting the redesign.
