---
name: product
description: "Provides product management expertise for the Bangsamoro Development Platform. Use when designing product management courses/workshops (with /academy), consulting on product strategy, roadmaps, or feature prioritization, building product planning platform features, or helping cooperatives and social enterprises develop products. Serves as Product Management within Phase 4: DELIVER & DRIVE in the 4D SE Development Journey (invoked by /enterprise-dev). Covers product strategy, roadmap development (Now/Next/Later), feature prioritization (RICE, MoSCoW, Kano), product-market fit, product lifecycle management, and BARMM adaptations. Integrates with /enterprise-dev for Phase 4 orchestration, /design-thinking for user research, and /lean-canvas for business model alignment."
argument-hint: "[topic]"
---

# Product Management Skill

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's product request                          ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

## SE Development Journey Integration

See [references/extracted-content.md](references/extracted-content.md) for details.

## When to Use

| Trigger | Action |
|---------|--------|
| **SE Development - Product Management** | Mode 4: Invoked by /enterprise-dev |
| Product management course/workshop design | Mode 1 with `/academy` for curriculum |
| Product strategy consulting | Mode 2 with PM frameworks |
| Platform features for product planning | Mode 3 with `/featuredev` |
| Coop/SE product development questions | Provide context-adapted guidance |

---

## Core Concepts

### What is Product Management?

The discipline of guiding a product from conception through development, launch, and continuous improvement. For social enterprises, product management balances:

1. **User Value** - What do customers/beneficiaries need?
2. **Business Value** - What sustains the organization?
3. **Impact Value** - What creates social good?

### The Product Management Triangle (SE-Adapted)

```text
                    USER VALUE
                    (Desirability)
                         ▲
                        / \
                       /   \
                      /     \
                     /   ◆   \
                    /  PRODUCT \
                   /     ◆      \
                  /_______________\
    BUSINESS VALUE ◄─────────────► IMPACT VALUE
    (Viability)                    (Mission)
```

### Key Frameworks

| Framework | Purpose | When to Use |
|-----------|---------|-------------|
| **Now/Next/Later** | Roadmap structure | Planning timelines |
| **RICE** | Prioritization scoring | Objective ranking |
| **MoSCoW** | Priority categories | Stakeholder alignment |
| **Kano Model** | Feature satisfaction | Customer research |
| **Jobs to Be Done** | User needs | Problem discovery |

---

## Workflow Modes

### Mode 1: Curriculum Design (with /academy)

When designing product management courses or workshops:

#### STAGE 0: Deep Research (Mandatory)

**Before curriculum design, invoke `/deep-research` to gather evidence-based content.**

#### Curriculum Design Steps

1. **Identify learning level**: Foundational / Intermediate / Advanced
2. **Select competency focus**: See [curriculum-design.md](references/curriculum-design.md)
3. **Choose module structure**: Standard 8-module or custom
4. **Design assessments**: Product roadmap creation, prioritization exercises

**Standard Product Management Course Modules:**
1. Introduction to Product Management
2. Product Vision and Strategy
3. Understanding Users (link to `/design-thinking`)
4. Feature Prioritization Frameworks
5. Roadmap Development
6. MVP and Lean Product Development
7. Quality and Delivery
8. Product Metrics and Iteration

---

### Mode 2: Product Consulting

For product strategy consulting:

1. **Assess product stage**: Idea → MVP → Growth → Scale
2. **Apply appropriate framework**:
   - Idea: Jobs to Be Done, opportunity sizing
   - MVP: Feature prioritization, scope definition
   - Growth: Metrics optimization, roadmap planning
   - Scale: Platform thinking, product portfolio
3. **Consider context**: Cooperative principles, SE mission, BARMM needs

**Templates available:**
- [Product Roadmap Template](assets/product-roadmap-template.md)
- [Feature Prioritization Template](assets/feature-prioritization-template.md)
- [MVP Canvas Template](assets/mvp-canvas-template.md)

---

### Mode 3: Platform Feature Development

When building product management features for the platform:

1. Read [barmm-context.md](references/barmm-context.md) for local considerations
2. Align with cooperative principles (member-driven product decisions)
3. Support social enterprise dual-track (impact + sustainability)
4. Integrate with existing Coop/SE portal architecture

---

### Mode 4: SE Development Journey (Product Management)

**Use this mode when invoked by `/enterprise-dev` for SE development.**

This mode focuses on Product Management, receiving inputs from all three prior phases (`/design-thinking`, `/lean-canvas`, `/toc`) and providing deliverables for implementation.

#### Step 1: Receive Inputs

```text
INPUTS FROM PREVIOUS PHASES:
│
├── From /design-thinking (Phase 1):
│   ├── User Personas → Target user profiles
│   ├── Empathy Maps → Pain points to address
│   ├── Journey Maps → User touchpoints for features
│   ├── Prototypes → Validation insights for MVP
│   └── How Might We → Feature opportunities
│
├── From /lean-canvas (Phase 2):
│   ├── Solution → Product feature candidates
│   ├── Problem → Jobs to be done
│   ├── Key Metrics → Success measurement
│   └── Channels → Distribution strategy
│
└── From /toc (Phase 3):
    ├── Theory of Change → Impact-driven features
    ├── Indicators → Success metrics
    └── Assumptions → Risk factors
```

#### Step 2: Define Product Vision

**Product Vision Statement Formula:**

```text
FOR [target customer/beneficiary]
WHO [statement of need or opportunity]
THE [product name] IS A [product category]
THAT [key benefit, reason to buy/use]
UNLIKE [primary competitive alternative]
OUR PRODUCT [statement of primary differentiation]
```

**SE-Specific Additions:**
- Mission alignment statement
- Impact mechanism description
- Beneficiary outcome goals

#### Step 3: Prioritize Features

**RICE Scoring (SE-Adapted):**

```text
RICE SCORE = (Reach × Impact × Confidence × Mission) / Effort

Where:
- Reach: How many users/beneficiaries affected? (1-10)
- Impact: How much does it improve outcomes? (0.25, 0.5, 1, 2, 3)
- Confidence: How sure are we? (0.5, 0.8, 1.0)
- Mission: How aligned with social mission? (0.5, 1, 1.5)
- Effort: Person-months to build (1-10)
```

**MoSCoW Categories:**

| Category | Definition | SE Consideration |
|----------|------------|------------------|
| **Must Have** | Essential for launch | Core impact delivery |
| **Should Have** | Important but not critical | Enhanced impact |
| **Could Have** | Nice to have | User experience |
| **Won't Have** | Out of scope for now | Future consideration |

**Kano Model Application (MVaP Framework):**

The Kano Model classifies features by customer response, revealing which features create value vs. waste resources. Use this to build a **Minimum Valuable Product (MVaP)** - not just viable, but genuinely valuable.

| Feature Type | Description | Customer Response | SE Examples | Strategy |
|--------------|-------------|-------------------|-------------|----------|
| **Must-Have (Basic)** | Table stakes - expected by default | Absence = dissatisfaction; presence = neutral | Product safety, basic quality, compliance | Meet threshold, use existing solutions |
| **Performance** | More is better (to a point) | Linear - more investment = more satisfaction | Delivery speed, variety, pricing | Define Minimum Performance Metrics (MPM) |
| **Delighters** | Unexpected, disproportionate satisfaction | Absence = okay; presence = delight | Impact stories, community connection, transparency | Build UVP around ONE delighter |
| **Zone of Indifference** | Lukewarm response | "Meh" - neither satisfied nor dissatisfied | "Nice to have" features nobody asked for | AVOID - cut from backlog |
| **Reverse** | More is worse | More presence = less satisfaction | Ads, complexity, excessive notifications | Minimize or eliminate |

**MVaP Priority Order**: Delighters > Performance > Must-Haves

**The 4-Step MVP Cocktail Framework:**

```text
STEP 1: Build UVP Around ONE Delighter
└── What can you offer that competitors can't?
└── What creates emotional response, not just functional value?
└── Example: Tesla's software updates that add new features over time

STEP 2: Define Minimum Performance Metrics (MPM)
└── For each performance feature, define competitive threshold
└── Stop investing beyond this point - redirect to delighters
└── Example: "Response time under 4 hours" (not "instant")

STEP 3: Layer in Second Axis of Differentiation
└── Once delighter is established, add secondary differentiator
└── Creates defensible positioning: "We're the only X that also Y"

STEP 4: Innovate Around Basics Using Existing Solutions
└── For must-haves, use existing solutions - don't reinvent
└── "Wizard of Oz MVP" - polished front-end, manual/existing back-end
└── Example: Use Stripe for payments, don't build your own
```

**Warning Signs of MUP (Maximally Undifferentiated Product):**
- You can't articulate ONE clear differentiator
- Your features list looks like competitors
- Customers describe you as "another option"

See: `../shared/references/mvap-framework.md` for complete framework.

#### Step 4: Create Roadmap

**Now/Next/Later Framework:**

```text
┌─────────────────────────────────────────────────────────────────────┐
│                       PRODUCT ROADMAP                                │
├─────────────────┬─────────────────┬─────────────────────────────────┤
│      NOW        │      NEXT       │            LATER                │
│   (0-3 months)  │   (3-6 months)  │         (6-12 months)           │
├─────────────────┼─────────────────┼─────────────────────────────────┤
│ MVP Features    │ Growth Features │ Scale Features                  │
│                 │                 │                                 │
│ • Core product  │ • Enhanced UX   │ • Platform expansion            │
│ • Basic impact  │ • More channels │ • New product lines             │
│ • Initial users │ • Analytics     │ • Automation                    │
│                 │                 │                                 │
│ Goal: Validate  │ Goal: Grow      │ Goal: Scale                     │
│ problem-solution│ user base       │ impact                          │
└─────────────────┴─────────────────┴─────────────────────────────────┘
```

**Roadmap Template:**

```text
QUARTER: [Q1 2025]
THEME: [e.g., "Launch MVP"]

GOALS:
1. [Measurable goal]
2. [Measurable goal]

FEATURES:
┌─────────────────┬──────────┬────────┬───────────┐
│ Feature         │ Priority │ Effort │ Owner     │
├─────────────────┼──────────┼────────┼───────────┤
│ [Feature 1]     │ Must     │ M      │ [Name]    │
│ [Feature 2]     │ Should   │ S      │ [Name]    │
│ [Feature 3]     │ Could    │ L      │ [Name]    │
└─────────────────┴──────────┴────────┴───────────┘

SUCCESS METRICS:
- [Metric 1]: Target [X]
- [Metric 2]: Target [Y]
```

#### Step 5: Define Quality Standards

**Acceptance Criteria Template:**

```text
FEATURE: [Feature Name]

USER STORY:
As a [user type], I want to [action] so that [benefit].

ACCEPTANCE CRITERIA:
Given [context]
When [action]
Then [expected result]

IMPACT CRITERIA:
- How does this feature contribute to social impact?
- What ToC outcome does it support?

QUALITY CRITERIA:
- Performance requirements
- Accessibility requirements
- Security requirements
```

**Definition of Done:**

```text
□ Feature meets acceptance criteria
□ Code reviewed and approved
□ Tests written and passing
□ Documentation updated
□ Impact metrics defined
□ Stakeholder sign-off
```

#### Step 6: Package Outputs

```text
OUTPUTS FOR IMPLEMENTATION:
│
├── Product Roadmap
│   ├── Now/Next/Later visualization
│   ├── Quarterly breakdown
│   └── Theme and goals per quarter
│
├── Feature Backlog
│   ├── Prioritized list (RICE scores)
│   ├── User stories
│   └── Acceptance criteria
│
├── MVP Specification
│   ├── Scope definition
│   ├── Core features only
│   └── Success criteria
│
└── Quality Standards
    ├── Definition of Done
    ├── Testing approach
    └── Delivery process
```

---

## Quick Reference

### Prioritization Decision Tree

```text
Is it required for core value delivery?
│
├── YES → Is it technically feasible now?
│         │
│         ├── YES → MUST HAVE (Now)
│         └── NO → SHOULD HAVE (Next)
│
└── NO → Does it significantly enhance experience?
         │
         ├── YES → COULD HAVE (Next/Later)
         └── NO → WON'T HAVE (Backlog)
```

### Product Metrics Framework

| Metric Type | Examples | SE Consideration |
|-------------|----------|------------------|
| **Acquisition** | Sign-ups, downloads | Beneficiary reach |
| **Activation** | First use, onboarding | Value delivery |
| **Retention** | Return rate, churn | Sustained impact |
| **Revenue** | Sales, subscriptions | Sustainability |
| **Referral** | NPS, word-of-mouth | Community growth |
| **Impact** | Outcomes, changes | Mission fulfillment |

### BARMM Adaptations

**For Cooperatives:**
- Member participation in product decisions
- Democratic feature prioritization
- Community-driven roadmap input
- Patronage considerations in pricing

**For Social Enterprises:**
- Impact-first feature prioritization
- Beneficiary-centered design
- Mission alignment scoring
- Shari'ah-compliant product features

---

## Reference Files

| File | Use When |
|------|----------|
| [product-frameworks.md](references/product-frameworks.md) | Need RICE, MoSCoW, Kano, JTBD details |
| [roadmap-guide.md](references/roadmap-guide.md) | Need roadmap planning, Now/Next/Later |
| [barmm-context.md](references/barmm-context.md) | Need coop/SE adaptations |
| [curriculum-design.md](references/curriculum-design.md) | Designing courses with /academy |
| [edp-integration.md](references/edp-integration.md) | BARMM EDP curriculum content (WHAT/HOW/HOW MUCH, MVP, 90-Day Roadmap) |

## Asset Files

| File | Use When |
|------|----------|
| [product-roadmap-template.md](assets/product-roadmap-template.md) | Creating new product roadmap |
| [feature-prioritization-template.md](assets/feature-prioritization-template.md) | Prioritizing features |
| [mvp-canvas-template.md](assets/mvp-canvas-template.md) | Defining MVP scope |

---

## Skill Integration Network

| Skill | Relationship | Data Exchange |
|-------|--------------|---------------|
| `/enterprise-dev` | **Orchestrator** | ED invokes Product for PM |
| `/design-thinking` | **Input source** | Personas, Journey Maps, Prototypes → Product |
| `/lean-canvas` | **Input source** | Solution, Problem, Metrics → Product |
| `/toc` | **Input source** | ToC, Indicators → Impact features |
| `/marketer` | **Sibling** | Product features ↔ Marketing messaging |
| `/finance` | **Sibling** | Product costs ↔ Financial projections |
| `/academy` | Curriculum design | PM expertise for course development |
| `/cooperative` | Context adaptation | Democratic product governance |
| `/featuredev` | Implementation | Product feature requirements |
| `/deep-research` | Research foundation | Evidence for all modes |

## Workflow: Cooperative Platform Features

See [references/extracted-content.md](references/extracted-content.md) for details.

## Cooperative Integration

When this skill encounters cooperative contexts, invoke `/cooperative` for specialized knowledge.
See [references/cooperative-integration.md](references/cooperative-integration.md) for triggers, patterns, and `/cooperative` assets.

## Constraints

- Use authoritative sources (Marty Cagan, Teresa Torres, Strategyzer)
- Align with Lean Product Development methodology
- Support CSEA's regulatory mandate in BARMM
- Adapt for cooperative and SE contexts
- Follow Shari'ah-compliant principles for BARMM products
- Avoid purple colors in any UI recommendations
- When invoked for SE development, always provide roadmap outputs
- Receive inputs from /design-thinking, /lean-canvas, and /toc when in SE Development Journey mode
- Provide feedback to /design-thinking for user research iteration
