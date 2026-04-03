# Deep Research - Academy Skill

## Overview

Deep Research is an intensive, multi-step research methodology for Academy that mirrors Google Gemini's Deep Research approach. It systematically explores complex topics through iterative web searching, reading, and synthesis to produce comprehensive research briefs.

**Inspired by**: [Gemini Deep Research](https://blog.google/products/gemini/google-gemini-deep-research/)

**When to use**: This reference is invoked by [research-capability.md](research-capability.md) when Deep Research is required.

---

## Two-Layer Research Architecture

Academy uses a **two-layer research process** that combines the standalone `/deep-research` skill with curriculum-focused validation:

```
┌─────────────────────────────────────────────────────────────┐
│                    LAYER 1: /deep-research skill            │
│                                                             │
│  Invoke: /deep-research                                     │
│  Location: .gemini/skills/deep-research/SKILL.md            │
│                                                             │
│  Workflows:                                                 │
│  1. Initial Deep Research (Plan → Search → Read → Iterate)  │
│  2. Research Validation (revisit sources, cross-reference)  │
│  3. Factual Accuracy Verification (dates, numbers, names)   │
│  4. Refinement (corrections, strengthen citations)          │
│                                                             │
│  OUTPUT: Research Brief with Works Cited                    │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                    LAYER 2: Academy Validation              │
│                                                             │
│  This document defines the curriculum-focused validation    │
│  process for MoroAcademy course and workshop design.        │
│                                                             │
│  Validation Criteria:                                       │
│  • Curriculum applicability                                 │
│  • Regulatory compliance (CDA, CSC, etc.)                   │
│  • Pedagogical alignment (adult learning, Bloom's taxonomy) │
│  • Target audience fit                                      │
│  • Assessment alignment                                     │
│                                                             │
│  OUTPUT: Validated Research Brief for curriculum design     │
└─────────────────────────────────────────────────────────────┘
```

### How to Use Two-Layer Research

1. **Invoke `/deep-research` first** with your topic
2. **Receive the Research Brief** from Layer 1
3. **Apply Layer 2 validation** using this document's criteria
4. **Produce Validated Research Brief** for curriculum design

---

## Core Methodology

Deep Research follows the **Plan → Search → Read → Iterate → Output** cycle:

```
┌─────────────────────────────────────────────────────────────────┐
│                    DEEP RESEARCH CYCLE                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│    ┌─────────┐                                                  │
│    │  PLAN   │ ← Create multi-step research plan               │
│    └────┬────┘                                                  │
│         │                                                       │
│         ▼                                                       │
│    ┌─────────┐     ┌─────────┐     ┌─────────┐                 │
│    │ SEARCH  │────▶│  READ   │────▶│ ITERATE │                 │
│    └─────────┘     └─────────┘     └────┬────┘                 │
│         ▲                               │                       │
│         │                               │                       │
│         └───────────────────────────────┘                       │
│              (repeat until comprehensive)                       │
│                                                                 │
│         │                                                       │
│         ▼                                                       │
│    ┌─────────┐                                                  │
│    │ OUTPUT  │ → Comprehensive Research Brief                   │
│    └─────────┘                                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Minimum Effort Requirements

| Component | Minimum | Optimal |
|-----------|---------|---------|
| **Research Questions** | 5 | 10+ |
| **WebSearch Queries** | 10 | 15-20 |
| **WebFetch Deep Dives** | 5 | 8-10 |
| **Domains Covered** | 4 | All 5 |
| **Iteration Cycles** | 1 | 2-3 |
| **Sources Cited** | 10 | 20+ |

---

## Phase 1: PLAN (Research Strategy)

Create a structured research plan before executing any searches.

### 1.1 Define Research Questions

Generate 5-10 research questions covering:

| Category | Example Questions |
|----------|-------------------|
| **Subject Matter** | What are the core concepts? What terminology is used? |
| **Target Audience** | Who are the learners? What's their current knowledge level? |
| **Standards/Regulations** | What official requirements exist? What certifications apply? |
| **Pedagogy** | What teaching methods work best for this topic? |
| **Assessment** | How should learning be measured? What competencies matter? |
| **Best Practices** | What do successful programs do? What are common pitfalls? |

### 1.2 Create Search Strategy

Plan search queries across 5 domains:

```
Research Plan: [Topic] Training Curriculum

Domain 1: Subject Matter Expertise (3 queries)
├── "[topic] fundamentals key concepts"
├── "[topic] terminology glossary"
└── "[topic] comprehensive guide [year]"

Domain 2: Industry Standards (3 queries)
├── "[regulatory body] [topic] requirements"
├── "[topic] certification standards [country]"
└── "[topic] compliance training requirements"

Domain 3: Curriculum & Training (3 queries)
├── "[topic] training curriculum design"
├── "[topic] course outline structure"
└── "[topic] learning objectives examples"

Domain 4: Pedagogical Approaches (3 queries)
├── "[topic] adult learning strategies"
├── "[topic] workshop activities exercises"
└── "teaching [topic] effectively methods"

Domain 5: Assessment & Evaluation (3 queries)
├── "[topic] assessment methods rubric"
├── "[topic] competency evaluation"
└── "[topic] training effectiveness measurement"
```

**For domain-specific query templates**, see [research-capability.md](research-capability.md#search-query-library).

---

## Phase 2: SEARCH (Broad Exploration)

Execute searches systematically, covering all planned domains.

**Requirements:**
- 10+ unique WebSearch queries
- Cover at least 4 different domains
- Note promising sources for deep dives

**Search Execution Pattern:**

```
For each domain in research plan:
    Execute 2-4 WebSearch queries
    Review results for:
        ├── Authoritative sources (official, academic, industry)
        ├── Comprehensive guides and frameworks
        ├── Case studies and examples
        └── Gaps requiring further investigation
    Note URLs for Phase 3 deep dives
    Identify new questions/topics discovered
```

---

## Phase 3: READ (Deep Dive)

Fetch and analyze authoritative sources in detail.

**Requirements:**
- 5+ WebFetch deep dives
- Prioritize official/authoritative sources
- Extract specific, actionable information

**Priority Sources:**

| Priority | Source Type | Examples |
|----------|-------------|----------|
| **1 (Highest)** | Official regulations | CDA memorandums, CSC guidelines, legal frameworks |
| **2** | Industry standards | ICA principles, certification requirements, competency frameworks |
| **3** | Academic/research | Peer-reviewed papers, university resources |
| **4** | Best practice guides | Professional associations, training organizations |
| **5** | Case studies | Success stories, implementation examples |

**For trusted source domains**, see [research-capability.md](research-capability.md#trusted-source-domains).

**Deep Dive Process:**

```
For each high-value source:
    WebFetch the URL
    Extract:
        ├── Key concepts and definitions
        ├── Specific requirements or standards
        ├── Recommended frameworks or methodologies
        ├── Data, statistics, or evidence
        ├── Practical examples or case studies
        └── Citations to other valuable sources
    Document source with URL for attribution
```

---

## Phase 4: ITERATE (Refine & Expand)

Based on findings, identify gaps and conduct additional searches.

**Iteration Triggers:**

| Finding | Action |
|---------|--------|
| Knowledge gap discovered | New search queries for missing information |
| Conflicting information | Search for authoritative resolution |
| New terminology found | Search for definitions and context |
| Referenced framework | Fetch original source for details |
| Outdated information | Search for current data |

**Iteration Pattern:**

```
After initial search/read cycle:
    Review findings against research questions
    Identify:
        ├── Unanswered questions → New searches
        ├── Interesting leads discovered → Deep dives
        ├── Conflicting sources → Clarification searches
        └── Referenced materials → Fetch originals
    Execute additional searches (typically 3-5 more)
    Continue until comprehensive coverage achieved
```

**Completion Criteria:**
- All original research questions answered
- No critical knowledge gaps remain
- Sufficient source material for curriculum development
- Multiple authoritative sources for key claims

---

## Citation Standards (Footnote Methodology)

Following Gemini Deep Research's citation approach, all research outputs must include proper source attribution using **inline numeric citations with a Works Cited list**.

### Citation Format

**Inline Citations**: Use numeric superscript or bracketed numbers throughout the text corresponding to source entries.

```
The Rochdale Pioneers established the first modern cooperative in 1844.[1]
Business Model Canvas was first proposed by Alexander Osterwalder in 2005.[2]
CDA MC 2015-09 mandates training for all cooperative officers.[3]
```

**Alternative Format**: For context where superscript isn't available:

```
The Rochdale Pioneers established the first modern cooperative in 1844. [1]
Business Model Canvas was first proposed by Alexander Osterwalder in 2005. [2]
```

### Works Cited Format

At the end of every Research Brief, include a numbered Works Cited list:

```markdown
## Works Cited

[1] International Co-operative Alliance. "History of the Cooperative Movement."
    ICA, 2024. https://ica.coop/en/cooperatives/history-cooperative-movement

[2] Osterwalder, Alexander & Pigneur, Yves. Business Model Generation.
    Wiley, 2010. https://www.strategyzer.com/books/business-model-generation

[3] Cooperative Development Authority. "MC 2015-09: Mandatory Training for
    Cooperative Officers." CDA, 2015. https://cda.gov.ph/issuances/mc-2015-09
```

### Citation Components

Each citation must include:

| Component | Required | Example |
|-----------|----------|---------|
| **Author/Organization** | Yes | "International Co-operative Alliance" |
| **Title** | Yes | "History of the Cooperative Movement" |
| **Publisher/Source** | Yes | "ICA" |
| **Year** | Yes | "2024" |
| **URL** | Yes | Full URL to source |
| **Access Date** | Optional | "Accessed December 2025" |
| **Page/Section** | If applicable | "p. 15" or "Section 3" |

### Citation Rules

1. **Every claim needs a source**: Facts, statistics, definitions, and requirements must be cited
2. **Number citations sequentially**: First source mentioned is [1], second is [2], etc.
3. **Reuse numbers for repeated sources**: If citing source [1] again, use [1] not a new number
4. **Group related citations**: When multiple sources support one claim, use [1, 2, 3]
5. **Prioritize authoritative sources**: Official documents > Academic papers > Industry guides
6. **Include page numbers for specific claims**: "According to CDA MC 2015-09, Section 3.2..." [3, p. 5]
7. **Verify URLs are accessible**: Test all links before finalizing

### Source Type Formatting

| Source Type | Format |
|-------------|--------|
| **Government Document** | [#] Agency. "Document Title (Number)." Year. URL |
| **Academic Paper** | [#] Author(s). "Paper Title." Journal, Vol(Issue), Year. URL or DOI |
| **Book** | [#] Author(s). Title. Publisher, Year. URL (if available) |
| **Website** | [#] Organization/Author. "Page Title." Site Name, Year. URL |
| **Report** | [#] Organization. "Report Title." Year. URL |

### In-Text Citation Examples

**Single Source:**
```
The 7 cooperative principles were adopted by the ICA in 1995.[1]
```

**Multiple Sources:**
```
Cooperative governance emphasizes democratic member control.[1, 2]
```

**Source with Page Reference:**
```
PEARLS monitoring includes 44 financial ratios.[3, p. 12]
```

**Direct Quote:**
```
According to the ICA, cooperatives are "autonomous associations of persons
united voluntarily to meet their common economic, social, and cultural
needs."[1]
```

**Paraphrase:**
```
The Business Model Canvas provides a visual framework for designing and
analyzing business models using nine building blocks.[2]
```

---

## Phase 5: OUTPUT (Research Brief)

Synthesize all findings into a comprehensive Research Brief.

### Research Brief Template

```markdown
# Research Brief: [Course/Workshop Title]

## Metadata
- **Date**: [Date]
- **Topic**: [Topic]
- **Target Audience**: [Audience]
- **Research Depth**: Deep (X searches, Y deep dives)

## Executive Summary
[2-3 paragraph summary of key findings and recommendations]

## Research Questions Answered

### 1. Subject Matter Overview
[Comprehensive summary of the topic]

**Key Concepts:**
- **[Concept 1]**: [Definition and explanation]
- **[Concept 2]**: [Definition and explanation]
- **[Concept 3]**: [Definition and explanation]

**Essential Terminology:**
| Term | Definition |
|------|------------|
| [Term 1] | [Definition] |
| [Term 2] | [Definition] |

### 2. Industry Standards & Requirements
[Summary of regulatory/compliance requirements]

**Applicable Standards:**
- [Standard 1]: [Description, source]
- [Standard 2]: [Description, source]

**Compliance Requirements:**
- [Requirement 1]: [Details]
- [Requirement 2]: [Details]

### 3. Target Audience Analysis
[Profile of intended learners]

- **Current Knowledge Level**: [Description]
- **Key Challenges**: [Description]
- **Learning Motivations**: [Description]
- **Prerequisites**: [Description]

### 4. Pedagogical Recommendations
[Best practices for teaching this topic]

**Recommended Teaching Methods:**
1. [Method 1]: [Why effective, how to implement]
2. [Method 2]: [Why effective, how to implement]

**Common Pitfalls to Avoid:**
- [Pitfall 1]: [How to avoid]
- [Pitfall 2]: [How to avoid]

### 5. Recommended Learning Objectives
[Evidence-based objectives using Bloom's verbs]

By the end of this training, learners will be able to:
1. [Objective 1 - Remember/Understand level]
2. [Objective 2 - Apply level]
3. [Objective 3 - Analyze/Evaluate level]
4. [Objective 4 - Create level]

### 6. Recommended Curriculum Structure
[Suggested organization based on research]

Module 1: [Title] - [Duration]
├── Session 1.1: [Topic]
└── Session 1.2: [Topic]

Module 2: [Title] - [Duration]
├── Session 2.1: [Topic]
└── Session 2.2: [Topic]

### 7. Assessment Recommendations
[Evidence-based assessment strategies]

| Type | Method | Purpose |
|------|--------|---------|
| **Formative** | [Method] | [Purpose] |
| **Summative** | [Method] | [Purpose] |
| **Practical** | [Method] | [Purpose] |

## Content Sources
[High-quality sources for curriculum development]

1. **[Source Title]** - [URL]
   - Use for: [Specific content area]

2. **[Source Title]** - [URL]
   - Use for: [Specific content area]

## Works Cited

[1] Author/Organization. "Title." Publisher, Year. URL
[2] Author/Organization. "Title." Publisher, Year. URL
[3] Author/Organization. "Title." Publisher, Year. URL
[4] ...

## All Sources Consulted
[Complete list of sources reviewed, organized by type]

**Official/Regulatory:**
1. [Title] - [URL]
2. [Title] - [URL]

**Academic/Research:**
3. [Title] - [URL]
4. [Title] - [URL]

**Industry/Professional:**
5. [Title] - [URL]
6. [Title] - [URL]
```

---

## Quality Checklist

Before completing Deep Research, verify:

**Research Completeness:**
- [ ] **Comprehensive Coverage**: All research questions answered
- [ ] **Multiple Sources**: At least 10 sources consulted
- [ ] **Authoritative Sources**: Official/academic sources prioritized
- [ ] **Current Information**: Sources within last 3-5 years
- [ ] **Local Context**: Philippine/BARMM context considered
- [ ] **Audience Appropriate**: Research considers learner needs
- [ ] **Actionable Findings**: Research translates to curriculum decisions
- [ ] **No Critical Gaps**: Key topics fully covered
- [ ] **Iteration Complete**: Follow-up questions addressed

**Citation Standards:**
- [ ] **Inline Citations**: Every claim has a numbered citation [1], [2], etc.
- [ ] **Works Cited List**: Complete list with all source details
- [ ] **Citation Format**: Follows standard format (Author, Title, Year, URL)
- [ ] **URLs Verified**: All links tested and accessible
- [ ] **Sources Numbered**: Sequential numbering throughout document
- [ ] **Page References**: Specific claims include page/section numbers

---

## Example Deep Research Session

### Topic: Cooperative Financial Management Training

**Phase 1: Plan**
```
Research Questions:
1. What financial management concepts do coop officers need?
2. What are CDA requirements for financial training?
3. What is the PEARLS monitoring system?
4. How do successful programs teach coop finance?
5. What practical skills should be included?

Search Strategy:
- Domain 1: CDA regulations and requirements (3 queries)
- Domain 2: Cooperative financial concepts (3 queries)
- Domain 3: PEARLS system (2 queries)
- Domain 4: Training methodologies (3 queries)
- Domain 5: Assessment approaches (2 queries)
```

**Phase 2: Search (13 queries executed)**
```
WebSearch: "CDA financial management training requirements cooperatives"
WebSearch: "CDA MC 2015-09 mandatory training"
WebSearch: "cooperative treasurer training curriculum Philippines"
WebSearch: "PEARLS ratio analysis cooperative monitoring"
WebSearch: "cooperative financial statement analysis"
WebSearch: "patronage refund calculation training"
WebSearch: "cooperative bookkeeping non-accountants"
WebSearch: "financial literacy training cooperatives"
WebSearch: "cooperative audit preparation training"
WebSearch: "cash flow management small cooperatives"
WebSearch: "cooperative financial training best practices"
WebSearch: "adult financial literacy teaching methods"
WebSearch: "cooperative financial competency assessment"
```

**Phase 3: Read (7 deep dives)**
```
WebFetch: CDA MC 2015-09 full text
WebFetch: CDA Standard Chart of Accounts for Cooperatives
WebFetch: PEARLS Monitoring System Guide
WebFetch: ICA Financial Standards for Cooperatives
WebFetch: CDA Annual Report template and guidelines
WebFetch: Cooperative financial statement formats
WebFetch: Asian Credit Union training curriculum
```

**Phase 4: Iterate (5 additional queries)**
```
WebSearch: "patronage refund interest on capital calculation"
WebSearch: "cooperative reserve fund requirements CDA"
WebSearch: "financial ratio interpretation cooperatives"
WebSearch: "cooperative audit checklist CDA"
WebSearch: "cooperative budget preparation template"
```

**Phase 5: Output**
```
Research Brief: Cooperative Financial Management Training

Key Findings:
- CDA MC 2015-09 requires 8-16 hours financial training based on coop size
- PEARLS system has 44 ratios across 6 categories
- Training must cover: statements, ratios, budgeting, patronage refund
- Hands-on calculator exercises essential for adult learners
- Pre/post assessment required for compliance

Recommended Structure:
- Module 1: Financial Statements (4 hours)
- Module 2: PEARLS Ratio Analysis (4 hours)
- Module 3: Budgeting & Cash Flow (4 hours)
- Module 4: Patronage Refund & Reserves (4 hours)

Sources: 18 sources documented with URLs
```

---

## Integration with Academy Workflow

Deep Research is **Stage 0** in the Academy workflow:

```
STAGE 0: DEEP RESEARCH (Two-Layer)
├── Layer 1: /deep-research skill (4 workflows)
└── Layer 2: Academy validation (this reference)
    ↓
STAGE 1: ANALYZE (informed by Validated Research Brief)
    ↓
STAGE 2: DESIGN (using validated findings)
    ↓
STAGE 3: DEVELOP (referencing verified sources)
    ↓
STAGE 4: IMPLEMENT
    ↓
STAGE 5: EVALUATE
```

Research findings directly inform:
- **Learning objectives** (from competency frameworks found)
- **Content structure** (from curriculum examples found)
- **Assessment design** (from best practices found)
- **Facilitator guides** (from teaching strategies found)
- **Compliance** (from regulatory requirements found)

---

## Layer 2: Academy Curriculum Validation

After receiving the Research Brief from `/deep-research` skill (Layer 1), apply the following curriculum-focused validation before proceeding to course/workshop design.

### Validation Checklist

```
LAYER 2 VALIDATION CHECKLIST

□ 1. CURRICULUM APPLICABILITY
  □ Findings translate to learnable content?
  □ Content appropriate for training format (course vs workshop)?
  □ Sufficient depth for intended duration?
  □ Practical examples available?

□ 2. REGULATORY COMPLIANCE
  □ CDA requirements addressed (for cooperative training)?
  □ CSC guidelines followed (for government training)?
  □ Mandatory training hours met?
  □ Certification requirements identified?

□ 3. PEDAGOGICAL ALIGNMENT
  □ Adult learning principles applicable?
  □ Bloom's taxonomy levels appropriate?
  □ Active learning opportunities identified?
  □ Assessment methods validated?

□ 4. TARGET AUDIENCE FIT
  □ Prerequisites accurately defined?
  □ Language level appropriate?
  □ Cultural context considered (BARMM)?
  □ Technology constraints addressed?

□ 5. ASSESSMENT ALIGNMENT
  □ Learning objectives measurable?
  □ Assessment methods match objectives?
  □ Competency standards identified?
  □ Passing criteria defined?
```

### Validation Criteria Details

#### 1. Curriculum Applicability

| Check | Pass Criteria | Action if Fails |
|-------|---------------|-----------------|
| Learnable content | Clear concepts, skills identifiable | Request clarification from Layer 1 |
| Format appropriate | Matches course (self-paced) or workshop (live) | Adjust format recommendation |
| Sufficient depth | Enough material for duration | Expand or narrow scope |
| Practical examples | Real-world cases available | Search for additional case studies |

#### 2. Regulatory Compliance

| Domain | Regulator | Key Requirements |
|--------|-----------|------------------|
| **Cooperatives** | CDA | MC 2015-09, officer training hours, competency requirements |
| **Social Enterprise** | DTI/DSWD | SE registration, impact measurement |
| **Government** | CSC | Training accreditation, competency standards |
| **Financial** | BSP/CDA | Prudential standards, PEARLS monitoring |

**Validation Questions:**
- Does research address mandatory training requirements?
- Are compliance deadlines/durations noted?
- Are non-compliance consequences understood?

#### 3. Pedagogical Alignment

| Principle | Validation Check |
|-----------|------------------|
| **Adult Learning** | Self-directed, experience-based, problem-centered, immediately applicable |
| **Bloom's Taxonomy** | Objectives use appropriate verbs (Remember → Create) |
| **Active Learning** | 70% activities, 30% lecture for workshops |
| **Chunking** | Content broken into digestible segments |
| **Multimodal** | Visual, auditory, kinesthetic options available |

**Bloom's Taxonomy Validation:**

| Level | Verbs | Check |
|-------|-------|-------|
| Remember | List, define, identify | Foundational content covered? |
| Understand | Explain, summarize, describe | Concepts clearly explained? |
| Apply | Calculate, demonstrate, use | Practice opportunities identified? |
| Analyze | Compare, differentiate, examine | Analysis activities possible? |
| Evaluate | Assess, justify, recommend | Evaluation criteria available? |
| Create | Design, develop, formulate | Creation projects feasible? |

#### 4. Target Audience Fit

| Factor | Cooperative Officers | SE Founders | Government Staff |
|--------|---------------------|-------------|------------------|
| **Education** | Varies (HS to college) | College+ | College+ |
| **Tech Access** | Limited | Moderate | High |
| **Time** | After-hours, weekends | Flexible | Work hours |
| **Language** | Filipino + local | English/Filipino | English (formal) |
| **Motivation** | Compliance, skills | Growth, impact | Career, compliance |

**BARMM Context Considerations:**
- Halal compliance if food/finance related
- Cultural sensitivity to Islamic values
- Local language options (Maguindanaon, Tausug, etc.)
- Limited internet connectivity in some areas

#### 5. Assessment Alignment

| Component | Validation Check |
|-----------|------------------|
| **Objectives → Assessments** | Each objective has corresponding assessment |
| **Competency Standards** | Industry/regulatory competencies addressed |
| **Practical Skills** | Hands-on demonstrations included |
| **Knowledge Checks** | Quizzes/tests for conceptual understanding |
| **Passing Criteria** | Clear thresholds (e.g., 70% score, 80% attendance) |

### Layer 2 Validation Output

After validation, append to Research Brief:

```markdown
## Layer 2 Validation Summary

### Validation Status: ✓ PASSED / ⚠ CONDITIONAL / ✗ NEEDS REVISION

### Curriculum Applicability
- [ ] Content suitable for training: [Yes/No]
- [ ] Format recommendation: [Course/Workshop]
- [ ] Duration alignment: [X hours sufficient]

### Regulatory Compliance
- [ ] Applicable regulations: [List]
- [ ] Requirements addressed: [Yes/Partial/No]
- [ ] Gaps identified: [List if any]

### Pedagogical Alignment
- [ ] Adult learning principles: [Applied/Not applied]
- [ ] Bloom's levels covered: [List levels]
- [ ] Active learning ratio: [X% activities]

### Target Audience Fit
- [ ] Prerequisites: [List]
- [ ] Language level: [Grade X / Professional]
- [ ] BARMM context: [Addressed/Needs attention]

### Assessment Alignment
- [ ] Learning objectives measurable: [Yes/No]
- [ ] Assessment methods: [List]
- [ ] Competency standards: [Met/Partial/Not met]

### Validation Notes
- [Any issues to address]
- [Recommendations for design phase]

### Validated By
Academy Skill - Layer 2 Validation
Date: [Date]
```

### Conditional Pass Handling

If validation identifies issues:

| Issue Type | Action |
|------------|--------|
| **Missing regulatory info** | Additional targeted search |
| **Pedagogical gaps** | Consult teaching methodology sources |
| **Audience mismatch** | Adjust prerequisites or scope |
| **Assessment gaps** | Research competency frameworks |

### Handoff to Stage 1: Analyze

After Layer 2 validation passes, proceed to Stage 1 with:

1. **Validated Research Brief** (Layer 1 + Layer 2 summary)
2. **Regulatory requirements** clearly identified
3. **Target audience profile** confirmed
4. **Learning objectives** aligned to Bloom's taxonomy
5. **Assessment strategy** preliminarily defined

---

## Curriculum Template Placement

When incorporating Deep Research findings into curriculum templates (courses and workshops), follow this structure:

### Template Structure Standard

```markdown
# [Template Title]

[Brief description]

> **Template Version**: X.X | **Guidelines**: See [../_template-guidelines.md]

---

## Overview
[Main content starts here]

...

[All curriculum content sections]

...

## Skill Integration Notes
[Integration guidance]

---

## Deep Research References        ← PLACE AT END, before Version History

> **Research conducted [Date]** | Sources: [Key sources]

### Key Topic Context
[Research context table]

### Key Research Findings
[Numbered findings]

### Additional References
[Links to authoritative sources]

---

## Version History                  ← FINAL SECTION
[Version table]
```

### Placement Rules

| Section | Placement | Required |
|---------|-----------|----------|
| **Title & Description** | Beginning | Yes |
| **Overview** | After title | Yes |
| **Curriculum Content** | Middle sections | Yes |
| **Skill Integration Notes** | Before references | Optional |
| **Deep Research References** | **Near end, before Version History** | Yes |
| **Version History** | **Final section** | Yes |

### Rationale

Placing Deep Research References at the end:
- **Keeps focus on curriculum**: Content sections remain prominent
- **Reference appendix pattern**: Research citations function as appendix material
- **Consistent with academic style**: Works Cited typically appears at end
- **Easy maintenance**: References can be updated without restructuring main content

### Example Templates

See these templates for correct Deep Research References placement:
- `assets/templates/startups/dt-101-design-thinking-fundamentals.md`
- `assets/templates/startups/dt-500-design-thinking-sprint-workshop.md`

---

## Sources

- [Gemini Deep Research Overview](https://gemini.google/overview/deep-research/)
- [How to Use Deep Research](https://blog.google/products/gemini/tips-how-to-use-deep-research/)
- [Deep Research Technical Documentation](https://ai.google.dev/gemini-api/docs/deep-research)
- [Google Gemini Deep Research Announcement](https://blog.google/products/gemini/google-gemini-deep-research/)
