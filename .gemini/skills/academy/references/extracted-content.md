# Academy - Extracted Detailed Content

## Table of Contents

- [Research Capability](#research-capability)
- [General → BARMM Contextualization Standard](#general-→-barmm-contextualization-standard)
- [Lesson Design (Courses)](#lesson-design-courses)
- [Cooperative Integration](#cooperative-integration)
- [Use Templates](#use-templates)
- [Essential Courses & Workshops](#essential-courses-&-workshops)
- [MoroAcademy Content Structure](#moroacademy-content-structure)
- [ADDIE Framework for Course Design](#addie-framework-for-course-design)
- [Additional References](#additional-references)
- [Module Structure Patterns](#module-structure-patterns)
- [MoroAcademy Data Structures](#moroacademy-data-structures)
- [Session Design (Workshops)](#session-design-workshops)

---

## Research Capability

**CRITICAL: New Course/Workshop = Two-Layer Deep Research (MANDATORY)**

When starting any new course or workshop, always perform **Two-Layer Deep Research** before design.

### Two-Layer Research Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    LAYER 1: /deep-research skill            │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Workflow 1: Initial Deep Research                      │ │
│  │   Plan → Search (10+) → Read (5+) → Iterate → Draft    │ │
│  ├────────────────────────────────────────────────────────┤ │
│  │ Workflow 2: Research Validation                        │ │
│  │   Revisit sources → Cross-reference claims             │ │
│  ├────────────────────────────────────────────────────────┤ │
│  │ Workflow 3: Factual Accuracy Verification              │ │
│  │   Verify dates/numbers/names → Check citations         │ │
│  ├────────────────────────────────────────────────────────┤ │
│  │ Workflow 4: Refinement                                 │ │
│  │   Apply corrections → Strengthen citations             │ │
│  └────────────────────────────────────────────────────────┘ │
│                          ↓                                  │
│                  OUTPUT: Research Brief                     │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                    LAYER 2: /academy validation             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Curriculum-Focused Validation                          │ │
│  │   • Review for curriculum applicability                │ │
│  │   • Cross-reference domain sources (CDA, ICA, etc.)    │ │
│  │   • Validate against regulatory requirements           │ │
│  │   • Ensure pedagogical alignment                       │ │
│  │   • Verify adult learning best practices               │ │
│  └────────────────────────────────────────────────────────┘ │
│                          ↓                                  │
│            OUTPUT: Validated Research Brief                 │
└─────────────────────────────────────────────────────────────┘
```

**How to Invoke:**
1. First, invoke `/deep-research` skill with your topic
2. Then, validate the output using Academy's curriculum validation (Layer 2)

**Full /deep-research skill**: `.gemini/skills/deep-research/SKILL.md`
**Layer 2 methodology**: [references/deep-research.md](references/deep-research.md)

### Research Depth Levels

| Level | Effort | When to Use |
|-------|--------|-------------|
| **Deep** | 10+ searches + 5+ fetches | **DEFAULT for all new courses/workshops** |
| **Standard** | 5-7 searches + 2-3 fetches | Content refresh, familiar domain |
| **Quick** | 2-3 searches | Minor updates, verification only |

### Deep Research Workflow

```
STEP 1: Define Research Questions (5+ questions)
├── What subject matter knowledge is needed?
├── What industry standards/regulations apply?
├── What are best practices for teaching this topic?
├── What pedagogical approaches work for this audience?
└── What case studies and examples exist?

STEP 2: Broad Search (WebSearch) - 5+ queries
├── "[topic] training curriculum best practices"
├── "[topic] learning objectives framework"
├── "[industry] certification requirements [year]"
├── "[topic] adult learning strategies"
└── "[topic] competency framework"

STEP 3: Targeted Search (WebSearch) - 5+ queries
├── "[topic] for [audience] training"
├── "[topic] workshop activities exercises"
├── "[topic] assessment methods rubric"
├── "[topic] case studies examples"
└── "[topic] common challenges solutions"

STEP 4: Deep Dive (WebFetch) - 5+ sources
├── Official guidelines and regulations
├── Academic papers and frameworks
├── Industry reports and standards
├── Detailed case studies
└── Authoritative training resources

STEP 5: Synthesize Findings → Research Brief
├── Key concepts and terminology
├── Industry/regulatory requirements
├── Recommended learning objectives
├── Suggested curriculum structure
├── Assessment recommendations
└── Source list with URLs
```

### Research Topics by Domain

**Cooperative Training:**
- CDA/CSEA regulations and memorandum circulars
- ICA cooperative principles
- Cooperative governance frameworks
- PEARLS financial monitoring
- Patronage refund calculations

**Social Enterprise:**
- Social enterprise legal frameworks
- Impact measurement (SROI, B Impact)
- Sustainable business models
- Social innovation methodologies

**Government Training:**
- Civil Service Commission guidelines
- Completed Staff Work (CSW) standards
- Results-Based Performance Management
- Public financial management

**Business Skills:**
- Financial literacy frameworks
- Marketing for small enterprises
- Digital transformation for SMEs
- Halal certification and compliance

### Research Output Format

```markdown
# Research Brief: [Topic]


## General → BARMM Contextualization Standard

**CRITICAL**: This pedagogical standard MUST be applied to ALL curriculum design for MoroAcademy courses and workshops.

### The Two-Layer Approach

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                    GENERAL → BARMM CONTEXTUALIZATION                         │
│                                                                              │
│  LAYER 1: GENERAL (NATIONAL/UNIVERSAL)         Present FIRST                │
│  ─────────────────────────────────────────────────────────────               │
│  • What is taught by ALL cooperatives/SEs/organizations nationwide           │
│  • ICA principles, RA 9520, CDA memorandum circulars                         │
│  • Philippine-wide standards, best practices, frameworks                     │
│  • Universal concepts applicable across all regions                          │
│                                                                              │
│                               ↓ THEN ↓                                       │
│                                                                              │
│  LAYER 2: BARMM CONTEXTUALIZATION              Present SECOND                │
│  ─────────────────────────────────────────────────────────────               │
│  • BARMM-specific application of Layer 1 concepts                            │
│  • CSEA regulations, BTA Bill 210, BDP 2023-2028 alignment                   │
│  • Islamic principles (Shari'ah compliance, Moral Governance)                │
│  • Local case studies, examples, and success stories                         │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Exception: BARMM-First Delivery

**When general context is NOT applicable or CONTRADICTORY**, BARMM context may be delivered first:

| Scenario | Reason | Example |
|----------|--------|---------|
| **No national equivalent** | Topic is BARMM-specific with no general counterpart | CSEA-specific regulations, BTA Bill 210 provisions |
| **Contradictory principles** | General practice conflicts with BARMM requirements | Riba (interest) vs Shari'ah-compliant alternatives |
| **Regional-only programs** | Programs that only exist in BARMM | BARMM-specific government programs, regional initiatives |
| **Cultural specificity** | Content inherently tied to Bangsamoro culture | Moral Governance 12 pillars, Islamic values in operations |

### Decision Tree

```text
START: Designing curriculum content
    │
    ├─► Is there a GENERAL (national/universal) concept?
    │       │
    │       ├─► YES → Does it CONTRADICT BARMM requirements?
    │       │           │
    │       │           ├─► YES → BARMM-FIRST (with note on general context)
    │       │           │         Example: "Conventional interest vs Shari'ah-compliant"
    │       │           │
    │       │           └─► NO → TWO-LAYER APPROACH
    │       │                   Layer 1: General concept first
    │       │                   Layer 2: BARMM application second
    │       │
    │       └─► NO → BARMM-FIRST
    │               This is a BARMM-specific topic
    │
    └─► OUTPUT: Properly structured curriculum content
```

### Application Example: Cooperative Values Module

**WRONG (Too Straight)**:
```
Module 2: Cooperative Values
├── Lesson 2.1: Self-Help and Self-Responsibility
├── Lesson 2.2: Democracy and Equality
├── Lesson 2.3: Equity and Solidarity
├── Lesson 2.4: Ethical Values
└── Lesson 2.5: Islamic Principles in Cooperative Operations ❌
    (Jumps straight to BARMM without establishing general context)
```

**CORRECT (Two-Layer Approach)**:
```
Module 2: Cooperative Values
│
├── LAYER 1: GENERAL (National/Universal)
│   ├── Lesson 2.1: ICA Cooperative Values Overview
│   │   └── Self-help, self-responsibility, democracy, equality, equity, solidarity
│   ├── Lesson 2.2: Core Values in Practice
│   │   └── Self-help, self-responsibility, democracy, equality
│   ├── Lesson 2.3: Equity and Solidarity
│   │   └── Fair treatment, sharing risks/rewards, standing together
│   └── Lesson 2.4: Ethical Values (ICA)
│       └── Honesty, openness, social responsibility, caring for others
│
└── LAYER 2: BARMM CONTEXTUALIZATION
    └── Lesson 2.5: Cooperative Values in Bangsamoro Context
        ├── How ICA values align with Islamic principles
        │   ├── Self-help ↔ Taawun (mutual assistance)
        │   ├── Solidarity ↔ Ukhuwwah (brotherhood)
        │   ├── Equity ↔ Adl (justice)
        │   └── Caring for others ↔ Ihsan (excellence in service)
        ├── Shari'ah-compliant practices (no riba, halal transactions)
        └── Moral Governance alignment
```

### Implementation Checklist

When designing any course or workshop, verify:

- [ ] **Layer 1 content is complete** - General/national concepts are fully presented
- [ ] **Layer 2 follows Layer 1** - BARMM context builds on general foundation
- [ ] **Exception cases identified** - BARMM-first topics are properly justified
- [ ] **Connections explicit** - Show how BARMM context relates to general concepts
- [ ] **No "jumping straight"** - Avoid presenting regional content without general context

### Curriculum Templates

All curriculum templates in `/references/templates/` MUST follow this standard:
- `coop/*.md` - Cooperative training templates
- `se/*.md` - Social enterprise training templates
- `government/*.md` - Government training templates
- `business/*.md` - Business skills templates

---


## Lesson Design (Courses)

### Video Lessons

**Maximum 15 minutes per video.** Use purposeful durations based on content complexity:

| Duration | Purpose | Content Type |
|----------|---------|--------------|
| **3 min** | Quick definitions | Single term/concept introduction |
| **5 min** | Single concepts | One idea with brief explanation |
| **7 min** | Concepts + examples | Idea with 2-3 practical examples |
| **10 min** | Processes/workflows | Step-by-step procedures |
| **12 min** | Complex topics | Multi-part concepts with practice |
| **15 min** | Comprehensive | Full topic coverage with application |

**Design principles:**
- One concept per video
- Include visual aids and examples
- End with key takeaways
- Require bilingual scripts (English + Filipino)

### Script Requirements

Each video lesson requires:
1. **English Script** - Primary language for formal terms
2. **Filipino Script** - Localized version for accessibility
3. **Timing Markers** - Scene/slide change indicators
4. **Visual Cues** - On-screen text and graphics notes

**Script Template:**

```markdown
LESSON: [Title]
DURATION: [X] minutes
LANGUAGE: [English/Filipino]

---

[00:00] OPENING
Visual: [Description]
Narration: "[Script text]"

[00:30] SECTION 1: [Topic]
Visual: [Description]
Narration: "[Script text]"

[Continues...]

[XX:XX] CLOSING
Visual: Key takeaways
Narration: "[Summary and transition]"
```

**Lesson Template Pattern:**

```markdown
**Lesson X.X: [Title]** (VIDEO - [X] min)
- [Bullet point 1]
- [Bullet point 2]
- [Bullet point 3]
- **Script**: English + Filipino
- **Visuals**: [Description of visual elements]
```

**Text Lesson Pattern:**

```markdown
**Lesson X.X: [Title]** (TEXT - [X] min)
- [Bullet point 1]
- [Bullet point 2]
- **Reading**: English + Filipino versions
```

### Text Lessons

- Clear headings and subheadings
- Bullet points for lists
- Examples and case studies
- Practical tips in callout boxes

### Quiz Lessons

- 5-10 questions per quiz
- Mix question types:
  - Multiple choice (conceptual)
  - True/false (factual)
  - Short answer (application)
- Immediate feedback on answers
- 70% passing score recommended


## Cooperative Integration

When this skill encounters cooperative-related contexts, invoke `/cooperative` for specialized knowledge.

### Cooperative Triggers

Invoke `/cooperative` when you detect:
- Keywords: "cooperative", "coop", "RA 9520", "CDA", "primary cooperative", "secondary cooperative", "CSEA"
- Topics: PRS curriculum, officer training, cooperative education (Art. 59 ETF), CDA MC 2015-09 mandatory training, cooperative principles, member education
- Entities: Cooperative members, officers, BOD, GA, committees, statutory funds

### Integration Pattern

```
/academy + /cooperative Integration
|
+-- Detect cooperative context in user request
+-- Invoke /cooperative for domain knowledge
|   +-- RA 9520 provisions (especially Art. 59 ETF)
|   +-- CDA memorandum circulars (especially MC 2015-09)
|   +-- BARMM/CSEA requirements
+-- Apply /academy's methodology with cooperative context
+-- Reference /cooperative assets as needed
```

### Key /cooperative Assets

| Asset | Path | Use When |
|-------|------|----------|
| RA 9520 Full Text | `../cooperative/assets/ra-9520-philippine-cooperative-code-2008.md` | Verbatim legal citations for curriculum |
| RA 9520 Guide | `../cooperative/references/ra-9520-guide.md` | Understanding provisions for course design |
| Templates Index | `../cooperative/assets/templates/index.md` | Document templates for training materials |
| Memorandum Circulars | `../cooperative/references/memorandum-circulars/index.md` | CDA training requirements and guidelines |

### Academy-Specific Cooperative Topics

| Topic | RA 9520 Reference | Curriculum Application |
|-------|-------------------|------------------------|
| **Pre-Registration Seminar (PRS)** | CDA Requirement | 6-8h mandatory pre-registration training for organizers; covers cooperative identity, types, legal framework, registration process |
| **Education & Training Fund (ETF)** | Article 59 | Max 10% of net surplus; funds officer training, member education, staff development; requires annual ETF utilization report |
| **ETF Utilization Planning** | Article 59 | Training plan development, expense documentation, eligible/non-eligible expenses, reporting requirements |
| **Mandatory Officer Training** | CDA MC 2015-09 | COOP-101 + COOP-201 (16h micro, 32h larger); complete within first half of term; non-compliance = disqualification |
| **S&C Additional Training** | CDA MC 2015-09 | COOP-301 + Risk Mgmt + Credit Mgmt + Internal Control for coops with >PHP 5M deposits |
| **Cooperative Principles** | Article 4 | Foundation module for all cooperative courses (ICA 7 principles) |
| **Member Rights & Responsibilities** | Articles 18-22 | Content for member education programs; voting, patronage, equity |
| **Board Duties** | Articles 38-43 | Governance training curriculum; fiduciary duties, decision-making |
| **Training Delivery Modes** | — | Online (MoroAcademy), blended, live workshops, TSP-delivered; mode selection guidance |
| **Member Education Programs** | Article 59 (ETF) | Beyond officer training: financial literacy, cooperative identity, GA participation |
| **Officer Training Pathway** | CDA MC 2015-09 | PRS → COOP-101 → COOP-201 → COOP-301 → Specialized training progression |

---

**Remember**: Academy designs learning experiences. For storytelling and narrative design, invoke `/storyteller`. For gamification and simulations, invoke `/gamifier`. For presentation slides (session pages, facilitator control), invoke `/presentation`. For implementation (writing code, creating pages), invoke `/frontend`, `/backend`, or `/featuredev`. For explaining existing MoroAcademy features, use `/explainer`.


## Use Templates

Ready-to-use curriculum templates organized by category. See [references/templates/README.md](references/templates/README.md) for full index.

### Cooperative Training (CDA/CSEA-Mandated)

| Code | Template | Type | Duration |
|------|----------|------|----------|
| COOP-101 | [coop-101-fundamentals.md](references/templates/coop/coop-101-fundamentals.md) | Course | 8-16h |
| COOP-201 | [coop-201-governance.md](references/templates/coop/coop-201-governance.md) | Course | 8-16h |
| COOP-301 | [coop-301-financial.md](references/templates/coop/coop-301-financial.md) | Course | 8h |

### Social Enterprise Training

| Code | Template | Type | Duration |
|------|----------|------|----------|
| SE-101 | [se-101-fundamentals.md](references/templates/se/se-101-fundamentals.md) | Course | 8h |

### Business Skills (Cross-Cutting)

| Code | Template | Type | Duration |
|------|----------|------|----------|
| BIZ-101 | [biz-101-accounting.md](references/templates/business/biz-101-accounting.md) | Course | 8h |
| BIZ-201 | [biz-201-marketing.md](references/templates/business/biz-201-marketing.md) | Course | 8h |

### Government Training

| Code | Template | Type | Duration |
|------|----------|------|----------|
| GOV-101 | [gov-101-csw.md](references/templates/government/gov-101-csw.md) | Workshop | 16-24h |
| GOV-201 | [gov-201-supervision.md](references/templates/government/gov-201-supervision.md) | Workshop | 16-24h |
| GOV-301 | [gov-301-leadership.md](references/templates/government/gov-301-leadership.md) | Workshop | 24h |
| GOV-401 | [gov-401-planning.md](references/templates/government/gov-401-planning.md) | Workshop | 16-24h |
| GOV-501 | [gov-501-project-management.md](references/templates/government/gov-501-project-management.md) | Workshop | 24-40h |
| GOV-502 | [gov-502-results-based-me.md](references/templates/government/gov-502-results-based-me.md) | Workshop | 24h |

### Multi-Day Workshops

| Code | Template | Type | Duration |
|------|----------|------|----------|
| EDP-500 | [edp-500-enterprise-development.md](references/templates/workshops/edp-500-enterprise-development.md) | Workshop | 3 days |
| FRAMES | [frames-compliance-workshop.md](references/templates/workshops/frames-compliance-workshop.md) | Workshop | 2-5 days |

---


## Essential Courses & Workshops

MoroAcademy must develop these core training programs for cooperatives and social enterprises.

### Priority Courses (Must Develop First)

| Priority | Course | Code | Type | Duration | Target |
|----------|--------|------|------|----------|--------|
| **1** | Fundamentals of Cooperatives | COOP-101 | Course | 8-16h | All Coop Officers |
| **2** | Governance & Management of Cooperatives | COOP-201 | Course | 8-16h | BOD, Officers |
| **3** | Financial Management | COOP-301 | Course | 8h | Treasurers, Managers |
| **4** | Fundamentals of Social Entrepreneurship | SE-101 | Course | 8h | SE Founders |
| **5** | Enterprise Development Program (EDP) | EDP-500 | Workshop | 3 days (24h) | Coops, SEs |
| **6** | Basic Accounting for Non-Accountants | BIZ-101 | Course | 8h | Officers, Staff |

### CDA/CSEA Mandatory Training (MC 2015-09)

Cooperative officers must complete within **first half of their term** (per CDA MC 2015-09, adopted by CSEA for BARMM cooperatives):

| Cooperative Type | Required Training |
|------------------|-------------------|
| Micro Coops (≤₱3M assets) | COOP-101 (8h) + COOP-201 (8h) |
| Larger Coops (>₱3M assets) | COOP-101 (16h) + COOP-201 (16h) |
| S&C Coops (₱5M+ deposits) | + COOP-301 + Risk Mgmt + Credit Mgmt |

**Non-compliance**: Disqualification from officer positions, affects Certificate of Compliance.

### Additional Programs

**Specialized (Savings & Credit Coops)**:
- Risk Management (4h)
- Credit Management (4h)
- Internal Control Systems (4h)

**Business Skills (Cross-cutting)**:
- Marketing for Coops & SEs
- Strategic Planning
- Human Resource Management
- Leadership and Values

**Full course catalog and development templates**: [references/essential-courses.md](references/essential-courses.md)

---


## MoroAcademy Content Structure

### Unified Terminology

| Level | Course (Virtual) | Workshop (Live) | Purpose |
|-------|------------------|-----------------|---------|
| Container | Course | Workshop | The training program |
| Time Block | — | Day | Multi-day scheduling |
| Topic Group | **Module** | **Module** | Groups related content |
| Learning Unit | **Lesson** | **Session** | Individual activity |

### 1. Online Courses (Self-Paced)

```
Course
└── Module (topic group)
    └── Lesson (learning unit)
        ├── VIDEO - YouTube-based video content
        ├── TEXT - Rich text/markdown content
        ├── QUIZ - Assessment questions
        └── ASSIGNMENT - Practical exercises
```

- **Module** = A topic group (e.g., "Financial Management Basics")
- **Lesson** = Self-paced learning unit (e.g., "Introduction to Bookkeeping")

### 2. Live Workshops (Facilitated)

```
Workshop
└── Day (for multi-day programs)
    └── Module (topic group)
        └── Session (learning unit)
            ├── LECTURE
            ├── WORKSHOP (hands-on activity)
            ├── SIMULATION
            ├── GROUP_DISCUSSION
            ├── ASSESSMENT
            └── BREAK / LUNCH
```

- **Module** = A topic group (same concept as courses)
- **Session** = Live facilitated activity (equivalent of Lesson for workshops)


## ADDIE Framework for Course Design

Apply the ADDIE model for systematic instructional design:

### 1. Analyze

- Identify target learners (cooperatives, SEs, government)
- Assess prerequisite knowledge
- Define performance gaps
- Determine constraints (time, technology access)

### 2. Design

- Write measurable learning objectives (see below)
- Structure content into logical modules
- Select delivery methods (video, text, interactive)
- Plan assessments aligned to objectives

### 3. Develop

- Create content for each lesson/session
- Produce videos, write text, design quizzes
- Build facilitator guides for workshops
- Prepare materials and templates

### 4. Implement

- Publish course/workshop to MoroAcademy
- Train facilitators (for workshops)
- Enroll learners
- Monitor progress

### 5. Evaluate

- Collect learner feedback
- Analyze completion rates
- Review assessment scores
- Iterate and improve


## Additional References

### BARMM Context & Development Planning
- [references/barmm-bdp-alignment.md](references/barmm-bdp-alignment.md) - **BARMM Development Plan 2023-2028 alignment with curriculum design, moral governance integration, workforce skills gaps, Islamic education integration**

### Workflows
- [references/course-creation-workflow.md](references/course-creation-workflow.md) - Complete course creation process
- [references/workshop-creation-workflow.md](references/workshop-creation-workflow.md) - Complete workshop creation process
- [references/skill-integration.md](references/skill-integration.md) - How to integrate with other skills

### Research
- [references/deep-research.md](references/deep-research.md) - **Deep Research methodology (Plan → Search → Read → Iterate → Output)**
- [references/research-capability.md](references/research-capability.md) - Research triggers, depth levels, domain-specific queries

### Video Design
- [references/video-duration-methodology.md](references/video-duration-methodology.md) - **Evidence-based video duration guidelines (MIT/edX research, cognitive load theory)**

### Instructional Design
- [references/curriculum-design.md](references/curriculum-design.md) - **Comprehensive curriculum design (UbD, SAM, competency-based, TNA, Kirkpatrick)**
- [references/addie-framework.md](references/addie-framework.md) - Detailed ADDIE guidance
- [references/workshop-facilitation.md](references/workshop-facilitation.md) - Facilitation techniques
- [references/assessment-design.md](references/assessment-design.md) - Quiz and rubric patterns
- [references/facilitator-control.md](references/facilitator-control.md) - **Live workshop locking system for facilitators**

### Course Catalogs
- [references/essential-courses.md](references/essential-courses.md) - **Essential courses for Coops & SEs (CDA/CSEA MC 2015-09 compliant)**
- [references/government-training-catalog.md](references/government-training-catalog.md) - **Government training (CSW, Leadership, M&E, etc.)**

### Curriculum Templates
- [references/templates/edp-program.md](references/templates/edp-program.md) - Enterprise Development Program (3 days)
- [references/templates/compliance-training.md](references/templates/compliance-training.md) - FRAMES compliance training
- [references/templates/government-training.md](references/templates/government-training.md) - CSW and government training
- [references/templates/business-skills.md](references/templates/business-skills.md) - Marketing, finance, operations

---


## Module Structure Patterns

These patterns apply to **Module** organization (for both Courses and Workshops):

### Pattern 1: Concept-to-Application

```
Module 1: Foundations (What)
Module 2: Principles (Why)
Module 3: Methods (How)
Module 4: Practice (Apply)
Module 5: Assessment (Verify)
```

### Pattern 2: Progressive Complexity

```
Module 1: Basic concepts (Beginner)
Module 2: Core processes (Beginner)
Module 3: Advanced techniques (Intermediate)
Module 4: Complex scenarios (Advanced)
Module 5: Real-world application (Advanced)
```

### Pattern 3: Problem-Solution

```
Module 1: Problem identification
Module 2: Analysis framework
Module 3: Solution options
Module 4: Implementation steps
Module 5: Monitoring and adjustment
```


## MoroAcademy Data Structures

### Course Fields

```typescript
{
  title: string;
  slug: string;
  description: string;
  short_description: string;  // Max 500 chars
  category: CourseCategory;
  difficulty: 'BEGINNER' | 'INTERMEDIATE' | 'ADVANCED';
  target_audience: 'COOPERATIVE' | 'SOCIAL_ENTERPRISE' | 'GOVERNMENT' | 'PUBLIC';
  duration_hours: number;
  learning_outcomes: string[];
  instructor_name: string;
  instructor_bio: string;
}
```

### Session Types (Workshops)

```
OPENING_CEREMONY | REGISTRATION | LECTURE | WORKSHOP |
SIMULATION | GALLERY_WALK | GROUP_DISCUSSION | TEAM_ACTIVITY |
ASSESSMENT | BREAK | LUNCH | SYNTHESIS | CLOSING | CUSTOM
```

### Lesson Types (Courses)

```
VIDEO | TEXT | QUIZ | ASSIGNMENT
```


## Session Design (Workshops)

### Session Duration Guidelines

| Session Type | Duration | Notes |
|--------------|----------|-------|
| Lecture | 20-30 min | Include Q&A time |
| Group Discussion | 15-20 min | Clear prompts needed |
| Workshop Activity | 45-90 min | Include debrief |
| Simulation Game | 60-120 min | Requires facilitator guide |
| Break | 15-30 min | Every 90 minutes |

### Engagement Patterns

- **Watch-Try-Coach**: Demo (5 min) -> Solo practice (5 min) -> Peer coaching (10 min)
- **Think-Pair-Share**: Individual reflection -> Partner discussion -> Group sharing
- **Gallery Walk**: Teams post work -> Rotate and comment -> Synthesis discussion

### Facilitator Guide Structure

```json
{
  "preparation": ["Room setup", "Materials checklist", "Tech requirements"],
  "script": "Opening remarks and transition cues",
  "timing_notes": "15 min intro, 30 min activity, 15 min debrief",
  "common_questions": ["Q1", "Q2"],
  "troubleshooting": ["If participants struggle with X, try Y"]
}
```




---

## Government Training

Training programs for government agencies and workers in BARMM.

### Priority Government Courses

| Priority | Course | Code | Type | Duration | Target |
|----------|--------|------|------|----------|--------|
| **1** | Completed Staff Work (CSW) | GOV-101 | Workshop | 2-3 days (16-24h) | All staff |
| **2** | Supervision | GOV-201 | Workshop | 2-3 days (16-24h) | Supervisors |
| **3** | Performance Management | GOV-202 | Workshop | 2-3 days (16-24h) | Supervisors, HR |
| **4** | Executive Leadership | GOV-301 | Workshop | 3 days (24h) | Directors, Executives |
| **5** | Strategic Planning | GOV-401 | Workshop | 2-3 days (16-24h) | Planners, Managers |
| **6** | Theory of Change | GOV-402 | Course | 8-24h | M&E, Program staff |
| **7** | Project & Program Management | GOV-501 | Workshop | 3 days (24h) | Project managers |
| **8** | Results-Based M&E | GOV-502 | Workshop | 2-3 days (16-24h) | M&E officers |

**Duration Limits**: Workshops max 3 days unless specifically approved.

**Full government training catalog**: [references/government-training-catalog.md](references/government-training-catalog.md)

---

## Multi-Day Workshop Design

### Day Structure Template

```
Day N: [Theme Title]
├── Morning (8:00-12:00)
│   ├── Module 1: [Topic]
│   │   ├── Session: Lecture (30 min)
│   │   └── Session: Workshop Activity (60 min)
│   ├── Break (15 min)
│   └── Module 2: [Topic]
│       └── Session: Group Discussion (45 min)
├── Lunch (12:00-1:00)
└── Afternoon (1:00-5:00)
    ├── Module 3: [Topic]
    │   └── Session: Simulation (90 min)
    ├── Break (15 min)
    └── Module 4: Synthesis
        └── Session: Gallery Walk + Closing (60 min)
```

### Multi-Day Flow

- **Day 1**: Foundations, team building, baseline assessment
- **Days 2-N**: Core content delivery with increasing complexity
- **Final Day**: Synthesis, output creation, post-assessment, certification

## Assessment Strategies

### Formative (During Learning)

- Lesson/session quizzes
- Reflection prompts
- Discussion participation
- Peer feedback

### Summative (End of Course/Workshop)

- Final exam (comprehensive)
- Project/output submission
- Practical demonstration
- Portfolio review

### Workshop-Specific Assessments

- Pre/post knowledge tests
- Simulation performance scoring
- Output quality rubrics
- Peer evaluations
