---
name: social-enterprise
description: "Orchestrates social enterprise development for the Bangsamoro Development Platform. Use when developing new social enterprises (full 4D journey), designing SE courses/workshops (with /academy), consulting on SE development, feasibility, scaling, or impact measurement, building SE-related platform features, or researching SE frameworks and best practices. Orchestrates the 4D SE Development Journey: (1) DISCOVER & DESIGN Business Idea via /design-thinking, (2) DEFINE & DEVELOP Business Model via /lean-canvas, (3) DETERMINE & DIRECT Business Impact via /toc, (4) DELIVER & DRIVE Business Results via /enterprise-dev (Marketing, Product, Finance). Covers global frameworks (B-Corp, SBMC, IRIS+), Philippine context (PRESENT Bill), and BARMM specifics (BTA Bill 210, Shari'ah-compliant principles)."
argument-hint: "[topic]"
---

# Social Enterprise Development Skill

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's social enterprise request                ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

## The 4D SE Development Journey

This skill orchestrates a comprehensive journey using the **4D Framework**:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE 4D SE DEVELOPMENT FRAMEWORK                           │
│                                                                              │
│        /social-enterprise orchestrates → invokes specialized skills          │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  PHASE 1: DISCOVER & DESIGN                        → Business Idea          │
│  ─────────────────────────────                                              │
│  Skill: /design-thinking                                                    │
│  Focus: Problem discovery, user empathy, opportunity framing                │
│  Output: Problem Statement, User Personas, Insights, HMW Statements         │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  PHASE 2: DEFINE & DEVELOP                         → Business Model         │
│  ────────────────────────────                                               │
│  Skill: /lean-canvas                                                        │
│  Focus: Business model creation, validation, iteration                      │
│  Output: Validated Lean Canvas, Key Metrics, UVP, Customer Segments         │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  PHASE 3: DETERMINE & DIRECT                       → Business Impact        │
│  ──────────────────────────────                                             │
│  Skill: /toc                                                                │
│  Focus: Impact pathway, outcomes mapping, M&E framework                     │
│  Output: Theory of Change, Assumptions, Indicators, Impact Statements       │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  PHASE 4: DELIVER & DRIVE                          → Business Results       │
│  ───────────────────────────                                                │
│  Skill: /enterprise-dev (orchestrates /marketer, /product, /finance)        │
│  Focus: Marketing Management, Product Management, Finance Management        │
│  Output: Marketing Plan, Product Roadmap, Financial Projections             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### The 4D Framework Summary

| Phase | Two D's | Focus | Skill | Output |
|-------|---------|-------|-------|--------|
| 1 | **Discover & Design** | Business Idea | `/design-thinking` | Problem, Users, Insights |
| 2 | **Define & Develop** | Business Model | `/lean-canvas` | Canvas, Metrics, UVP |
| 3 | **Determine & Direct** | Business Impact | `/toc` | ToC, Assumptions, Indicators |
| 4 | **Deliver & Drive** | Business Results | `/enterprise-dev` | Marketing, Product, Finance |

### Data Flow Between Skills

| From Skill | Output | To Skill | Input |
|------------|--------|----------|-------|
| `/design-thinking` | Problem Statement | `/lean-canvas` | Problem block |
| `/design-thinking` | User Personas | `/lean-canvas` | Customer Segments |
| `/design-thinking` | HMW Statements | `/lean-canvas` | Solution direction |
| `/lean-canvas` | Problem + Solution | `/toc` | Interventions |
| `/lean-canvas` | Key Metrics | `/toc` | Outcome Indicators |
| `/lean-canvas` | UVP | `/toc` | Impact Statement basis |
| `/toc` | Theory of Change | `/enterprise-dev` | Impact framework |
| `/toc` | Indicators | `/enterprise-dev` | Success metrics |
| `/toc` | Assumptions | `/design-thinking` | Test hypotheses |
| `/enterprise-dev` | Marketing Plan | All skills | Implementation feedback |

---

## When to Use

| Trigger | Action |
|---------|--------|
| **Full SE development** | Use Mode 4: SE Development Journey (invokes all skills) |
| SE course/workshop design | Use Mode 1 with `/academy` for curriculum expertise |
| SE consulting (feasibility, scaling) | Use Mode 2 with consulting frameworks |
| SE platform features | Use Mode 3 with `/featuredev` for implementation |
| SE research questions | Provide evidence-based guidance |

---

## Workflow Modes

### Mode 1: Curriculum Design (with /academy)

When designing SE courses or workshops:

#### STAGE 0: Deep Research (Mandatory)

**Before curriculum design, invoke `/deep-research` to gather evidence-based content.**

```text
STAGE 0: DEEP RESEARCH (MANDATORY) → Output: Validated Research Brief
│
├── LAYER 1: Invoke /deep-research skill
│   └── OUTPUT: Research Brief with Works Cited
│
└── LAYER 2: Social Enterprise Curriculum Validation
    ├── Cross-reference with EU/OECD, B-Corp, GIIN, PhilSEN sources
    ├── Validate against Philippine SE context (PRESENT Bill, RA 9520)
    └── OUTPUT: Validated Research Brief for SE curriculum design
```

#### General -> BARMM Contextualization Standard

See [curriculum-design.md](references/curriculum-design.md) for the two-layer approach, exception rules, and implementation checklist.

#### Curriculum Design Steps

1. **Identify learning level**: Foundational / Intermediate / Advanced
2. **Select competency focus**: See [curriculum-design.md](references/curriculum-design.md)
3. **Choose module structure**: Standard 8-module or custom
4. **Design assessments**: Portfolio, business plan, impact exercise

**Standard SE Course Modules:**
1. Introduction to Social Entrepreneurship
2. Identifying Social Problems (invoke `/design-thinking`)
3. Social Business Model Development (invoke `/lean-canvas`)
4. Impact Measurement (invoke `/toc`)
5. Financial Management for SEs
6. Marketing and Communication
7. Legal Structures and Governance
8. Scaling and Sustainability

---

### Mode 2: SE Consulting

For SE development consulting:

1. **Assess lifecycle stage**: Incubation → Birth → Nurturing → Maturity
2. **Apply appropriate framework**:
   - Ideation: `/design-thinking` + Social Business Model Canvas
   - Planning: `/lean-canvas` + `/toc`
   - Growth: Scaling strategy selection
   - Impact: IRIS+ measurement
3. **Consider context**: Philippine law, BARMM regulations, Shari'ah compliance

**Templates available:**
- [Social Business Model Canvas](assets/social-business-model-canvas.md)
- [Theory of Change Template](assets/theory-of-change-template.md)
- [Feasibility Assessment Template](assets/feasibility-assessment-template.md)

---

### Mode 3: Platform Feature Development

When building SE features for the platform:

1. Read [barmm-context.md](references/barmm-context.md) for CSEA requirements
2. Align with BTA Bill 210 SE classification
3. Ensure Shari'ah-compliant principles where applicable
4. Integrate with existing Coop/SE portal architecture

---

### Mode 4: SE Development Journey (Full Orchestration)

**Use this mode when helping someone develop a new social enterprise from scratch.**

This mode orchestrates the complete journey by invoking specialized skills at each phase.

#### Phase 1: DISCOVER & DESIGN Business Idea

**Invoke `/design-thinking`** to deeply understand the problem and users.

```text
PHASE 1 WORKFLOW: DISCOVER & DESIGN
│
├── 1.1 Invoke /design-thinking
│   ├── Empathize: Interview beneficiaries, observe context
│   ├── Define: Frame the social problem clearly
│   ├── Ideate: Generate initial solution concepts
│   │
│   └── OUTPUTS for next phase:
│       ├── Problem Statement (→ Lean Canvas Problem block)
│       ├── User Personas (→ Lean Canvas Customer Segments)
│       ├── Key Insights (→ inform UVP development)
│       └── HMW Statements (→ solution direction)
│
└── 1.2 Transition Checkpoint
    └── Confirm: "Business idea discovered and designed. Ready for business model?"
```

#### Phase 2: DEFINE & DEVELOP Business Model

**Invoke `/lean-canvas`** to develop and validate the business model.

```text
PHASE 2 WORKFLOW: DEFINE & DEVELOP
│
├── 2.1 Invoke /lean-canvas
│   ├── Transfer from Phase 1:
│   │   ├── Problem Statement → Problem block
│   │   └── User Insights → Customer Segments
│   │
│   ├── Complete remaining blocks:
│   │   ├── Unique Value Proposition (build around ONE Delighter - MVaP)
│   │   ├── Solution (Minimum Valuable Product, not just Viable)
│   │   ├── Channels
│   │   ├── Revenue Streams
│   │   ├── Cost Structure
│   │   ├── Key Metrics (define Minimum Performance Metrics)
│   │   └── Unfair Advantage (second axis of differentiation)
│   │   REFERENCE: ../shared/references/mvap-framework.md
│   │
│   └── OUTPUTS for next phase:
│       ├── Validated Business Model
│       ├── Key Metrics (→ ToC Indicators)
│       └── Problem + Solution (→ ToC Interventions)
│
└── 2.2 Transition Checkpoint
    └── Confirm: "Business model defined and developed. Ready for impact planning?"
```

#### Phase 3: DETERMINE & DIRECT Business Impact

**Invoke `/toc`** to develop Theory of Change and impact measurement framework.

```text
PHASE 3 WORKFLOW: DETERMINE & DIRECT
│
├── 3.1 Invoke /toc
│   ├── Transfer from Phase 2:
│   │   ├── Solution → Interventions
│   │   └── Key Metrics → Indicator development
│   │
│   ├── Develop ToC:
│   │   ├── Define long-term impact goal
│   │   ├── Map outcomes pathway (backward mapping)
│   │   ├── Identify assumptions
│   │   ├── Develop indicators
│   │   └── Write narrative
│   │
│   └── OUTPUTS for next phase:
│       ├── Theory of Change diagram
│       ├── Assumptions to test
│       └── Impact measurement framework
│
└── 3.2 Transition Checkpoint
    └── Confirm: "Impact pathway determined and directed. Ready for implementation?"
```

#### Phase 4: DELIVER & DRIVE Business Results

**Invoke `/enterprise-dev`** for Marketing, Product, and Finance Management.

```text
PHASE 4 WORKFLOW: DELIVER & DRIVE
│
├── 4.1 Invoke /enterprise-dev
│   ├── Transfer from Phase 3:
│   │   ├── Theory of Change → Impact framework
│   │   ├── Indicators → Success metrics
│   │   └── Business Model → Operations foundation
│   │
│   ├── Invoke specialized sub-skills:
│   │   │
│   │   ├── /marketer (Marketing Management)
│   │   │   ├── Market segmentation and targeting
│   │   │   ├── Brand positioning and messaging
│   │   │   ├── Marketing channels and campaigns
│   │   │   └── Customer acquisition strategy
│   │   │
│   │   ├── /product (Product Management) - Apply MVaP Framework
│   │   │   ├── Product roadmap development
│   │   │   ├── Feature prioritization using Kano Model:
│   │   │   │   ├── Delighters (build UVP here)
│   │   │   │   ├── Performance (meet MPM threshold)
│   │   │   │   ├── Must-Haves (use existing solutions)
│   │   │   │   └── Avoid Zone of Indifference
│   │   │   ├── Product-market fit validation
│   │   │   └── Quality and delivery processes
│   │   │   REFERENCE: ../shared/references/mvap-framework.md
│   │   │
│   │   └── /finance (Finance Management)
│   │       ├── Financial projections and pricing
│   │       ├── Cash flow management
│   │       ├── Cost structure optimization
│   │       └── Investment and funding strategy
│   │
│   └── OUTPUTS:
│       ├── Marketing Plan
│       ├── Product Roadmap
│       ├── Financial Projections
│       └── Go-to-Market Strategy
│
├── 4.2 Launch & Monitor
│   ├── Execute marketing campaigns
│   ├── Track Key Metrics (from /lean-canvas)
│   ├── Test Assumptions (from /toc)
│   └── Measure Impact (IRIS+ framework)
│
└── 4.3 Iteration Loop
    ├── If metrics declining → return to /lean-canvas for pivot
    ├── If assumptions false → update /toc
    └── Periodic user research via /design-thinking
```

---

## Core Concepts

### What is a Social Enterprise?

Business organizations that:
1. Run **commercial activities** (entrepreneurial dimension)
2. Achieve **social/environmental good** (social dimension)
3. Have **governance reflecting their mission** (ownership dimension)

**BARMM Definition** (BTA Bill 210): Organizations primarily addressing social, cultural, or environmental challenges, with profit generation being secondary.

### SE vs Traditional Business vs NGO

| Aspect | Traditional Business | Social Enterprise | NGO |
|--------|---------------------|-------------------|-----|
| Primary Goal | Profit | Social impact + sustainability | Social impact |
| Revenue | Market sales | Market + grants/donations | Grants/donations |
| Profit Use | Shareholders | Reinvested for mission | N/A |

### SE Lifecycle Stages (4D Framework Mapping)

| Stage | 4D Phase | Focus | Skill |
|-------|----------|-------|-------|
| **Incubation** | Discover & Design | Vision, problem discovery, opportunity framing | `/design-thinking` |
| **Birth** | Define & Develop | Business model, first customers, validation | `/lean-canvas` |
| **Nurturing** | Determine & Direct | Impact pathway, measurement framework | `/toc` |
| **Growth** | Deliver & Drive | Marketing, Product, Finance Management | `/enterprise-dev` |
| **Maturity** | Iteration | Scale, sustainability, continuous improvement | All skills |

---

## Quick Reference

### 7 Core SE Competencies

1. **Leadership** - Initiative and action
2. **Optimism** - Bold vision confidence
3. **Grit** - Perseverance and passion
4. **Resilience** - Learning from failure
5. **Creativity** - Unconventional solutions (via `/design-thinking`)
6. **Empathy** - Understanding beneficiaries (via `/design-thinking`)
7. **Emotional Intelligence** - Relationship building

### Impact Measurement (IRIS+ Dimensions)

| Dimension | Question | Skill Connection |
|-----------|----------|------------------|
| **What** | What outcomes matter? | `/toc` outcomes |
| **Who** | Who experiences change? | `/design-thinking` users |
| **How Much** | Scale, depth, duration? | `/lean-canvas` metrics |
| **Contribution** | What's our unique role? | `/lean-canvas` UVP |
| **Risk** | What could go wrong? | `/toc` assumptions |

---

## Reference Files

| File | Use When |
|------|----------|
| [global-frameworks.md](references/global-frameworks.md) | Need EU/OECD definitions, B-Corp, SBMC, IRIS+ details |
| [philippine-context.md](references/philippine-context.md) | Need PRESENT Bill, RA 9520, RA 11232, PhilSEN info |
| [barmm-context.md](references/barmm-context.md) | Need CSEA, BTA Bill 210, Shari'ah principles |
| [development-methodology.md](references/development-methodology.md) | Need lifecycle, feasibility, scaling frameworks |
| [curriculum-design.md](references/curriculum-design.md) | Designing SE courses with /academy |

---

## Skill Integration Network

| Skill | Relationship | Data Exchange |
|-------|--------------|---------------|
| `/design-thinking` | **Phase 1: Discover & Design** | Problem → Canvas, Insights → Segments |
| `/lean-canvas` | **Phase 2: Define & Develop** | Canvas → ToC (metrics, solution) |
| `/toc` | **Phase 3: Determine & Direct** | ToC → Enterprise Dev (impact framework, indicators) |
| `/enterprise-dev` | **Phase 4: Deliver & Drive** | Marketing, Product, Finance → All skills for iteration |
| `/finance` | **Phase 4 (Finance)** | Organizational budgeting, controls, PFRF compliance |
| `/financial-analyst` | **Phase 4 (Finance)** | Financial modeling, ratio analysis, projections |
| `/investor` | **Fundraising** | Impact investor pitches, term sheets, due diligence |
| `/academy` | Curriculum design | SE expertise for course development |
| `/cooperative` | Context adaptation | Coop-to-SE transitions, principles alignment |
| `/featuredev` | Implementation | SE feature requirements |
| `/deep-research` | Research foundation | Evidence for all modes |

---

## Workflow: Cooperative-SE Relationship

See [cooperative-se-relationship.md](references/cooperative-se-relationship.md) for coop vs SE comparison, CSEA dual mandate, structure selection decision tree, partnership models, and practical scenarios.

## Y Combinator Framework for Social Enterprises

See [yc-framework-se.md](references/yc-framework-se.md) for YC principles adapted for impact ventures, dual PMF requirements, and growth metrics.

## Constraints

- Use authoritative sources (EU, OECD, B-Corp, GIIN, PhilSEN)
- Align with Philippine legal context (no dedicated SE law yet)
- Support CSEA's regulatory mandate in BARMM
- Follow Shari'ah-compliant principles for BARMM SEs
- Avoid purple colors in any UI recommendations
- When orchestrating journey, always confirm phase transitions with user
