---
name: toc
description: "Provides Theory of Change planning and evaluation expertise for the Bangsamoro Development Platform. Use when designing ToC courses/workshops (with /academy), consulting on program design, strategic planning, or impact pathways, building M&E or impact measurement platform features, or helping cooperatives, social enterprises, or NGOs develop Theory of Change. Serves as Phase 3: DETERMINE & DIRECT Business Impact in the 4D SE Development Journey (invoked by /social-enterprise). Covers Carol Weiss methodology (Aspen Institute), NPC Ten Steps, backward mapping, logic models, impact pathways, assumptions testing, indicators development, and BARMM adaptations. Integrates with /design-thinking (Phase 1), /lean-canvas (Phase 2), and /enterprise-dev (Phase 4)."
argument-hint: "[topic]"
---

# Theory of Change Skill

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's TOC request                              ║
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
| **SE Development - Phase 3: Determine & Direct** | Mode 4: SE Development Journey |
| ToC course/workshop design | Mode 1 with `/academy` for curriculum |
| Program design consulting | Mode 2 with ToC frameworks |
| M&E platform features | Mode 3 with `/featuredev` |
| Coop/SE/NGO strategic planning | Provide context-adapted guidance |

---

## Core Concepts

### What is Theory of Change?

A comprehensive planning methodology that maps how and why a desired change is expected to happen. It uses backward mapping from long-term goals to identify preconditions, assumptions, and interventions needed for change.[1]

**Key Statistics:**
- Adopted exponentially since Carol Weiss's 1995 work at Aspen Institute
- Over 50% of nonprofits now use ToC
- Standard methodology across UN, government agencies, and foundations

### Core Components

| Component | Purpose | From /lean-canvas |
|-----------|---------|-------------------|
| **Long-Term Goals** | Ultimate change (impact) | UVP / impact statement |
| **Outcomes Pathway** | Short, medium, long-term changes | Solution effectiveness |
| **Preconditions** | Necessary conditions for each outcome | Business model assumptions |
| **Assumptions** | Explicit beliefs about why pathway works | Validation hypotheses |
| **Interventions** | Specific activities | Solution features |
| **Indicators** | Measures to track progress | Key Metrics |

### ToC vs Logic Model vs Logframe

| Aspect | Theory of Change | Logic Model | Logframe |
|--------|-----------------|-------------|----------|
| Format | Diagram (flexible) | Flowchart | Matrix |
| Purpose | Strategic design | Visual summary | Project monitoring |
| Causality | Explains "why" | High-level | Limited |
| Scope | Big picture | Program | Project |

**Key Distinction:**
- ToC asks: "If we do X, then Y will change *because*..."
- Logframe answers: "We plan to do X, which will give Y result"

---

## Workflow Modes

### Mode 1: Curriculum Design (with /academy)

When designing ToC courses or workshops:

#### STAGE 0: Deep Research (Mandatory)

**Before curriculum design, invoke `/deep-research` to gather evidence-based content.**

#### Curriculum Design Steps

1. **Identify learning level**: Foundational / Intermediate / Advanced
2. **Select competency focus**: See [curriculum-design.md](references/curriculum-design.md)
3. **Choose module structure**: Standard 8-module or custom
4. **Design assessments**: ToC development, facilitation practice

**Standard ToC Course Modules:**
1. Introduction to Theory of Change
2. Core Components of ToC
3. Backward Mapping
4. Developing Your ToC
5. Assumptions and Risks
6. Indicators and Measurement
7. Using ToC for Learning
8. Facilitation Skills

---

### Mode 2: Program Design Consulting

For ToC development consulting:

1. **Assess organization stage**: New program / Existing program / Evaluation
2. **Apply appropriate framework**:
   - New: Full NPC Ten Steps process
   - Existing: Articulate current theory, fill gaps
   - Evaluation: Test assumptions, assess pathways
3. **Consider context**: Cooperative principles, SE mission, BARMM priorities

**Templates available:**
- [ToC Template](assets/toc-template.md)
- [BARMM Examples](assets/toc-examples.md)

---

### Mode 3: Platform Feature Development

When building ToC/M&E features for the platform:

1. Read [barmm-adaptation.md](references/barmm-adaptation.md) for context
2. Support dual-track outcomes for social enterprises
3. Integrate cooperative principles into outcomes
4. Connect to existing M&E frameworks

---

### Mode 4: SE Development Journey (Phase 3: Determine & Direct)

**Use this mode when invoked by `/social-enterprise` for SE development.**

This mode focuses on Phase 3: DETERMINE & DIRECT Business Impact, receiving from `/lean-canvas` and providing feedback loops to other skills.

#### Step 1: Receive Inputs from /lean-canvas

```text
INPUTS FROM DESIGN PHASE:
│
├── Problem + Solution
│   └── → Use as Interventions/Activities
│
├── Key Metrics
│   └── → Starting point for Indicators
│
├── UVP (Value Proposition)
│   └── → Basis for Impact Goal
│
└── Customer Segments
    ├── Beneficiaries → Primary target group
    └── Customers → Secondary stakeholders
```

#### Step 2: Define Long-Term Impact

**From the UVP, articulate the ultimate change:**

```text
IMPACT DEFINITION FOR SE:
│
├── Social Impact Goal
│   └── What sustained change do beneficiaries experience?
│
├── Business Sustainability Goal
│   └── What ensures the SE continues operating?
│
└── Combined Impact Statement
    └── How do social and business goals reinforce each other?
```

**Example:**
- UVP: "Authentic Maranao crafts that preserve heritage and empower artisans"
- Impact: "Maranao cultural heritage preserved AND artisan families thrive economically"

#### Step 3: Backward Map Outcomes Pathway

**Work backward from impact to current activities:**

```text
BACKWARD MAPPING FOR SE:
│
├── IMPACT (3-5+ years)
│   └── What sustained change do you want to see?
│
├── LONG-TERM OUTCOMES (2-3 years)
│   └── What must happen for impact to occur?
│
├── MEDIUM-TERM OUTCOMES (1-2 years)
│   └── What must happen for LTOs to occur?
│
├── SHORT-TERM OUTCOMES (0-12 months)
│   └── What must happen for MTOs to occur?
│
└── INTERVENTIONS/ACTIVITIES (from /lean-canvas Solution)
    └── What does the SE do?
```

**SE-Specific Dual Track:**

```text
SOCIAL TRACK:                    BUSINESS TRACK:
├── Social Impact               ├── Financial Sustainability
│   ├── LTO: Beneficiary        │   ├── LTO: Revenue growth
│   │       wellbeing improved  │   │
│   ├── MTO: Skills/assets      │   ├── MTO: Market position
│   │       acquired            │   │
│   └── STO: Services           │   └── STO: Products/services
│           delivered           │           sold
│                               │
└── Both tracks feed from same interventions
```

#### Step 4: Identify Assumptions

**At each link in the pathway, ask "Why do we believe this works?"**

```text
ASSUMPTION TYPES:
│
├── Causal Assumptions
│   └── "If we do X, Y will happen because..."
│   └── Why activities lead to outcomes
│
├── Contextual Assumptions
│   └── "This will work because the context is..."
│   └── External conditions that must be true
│
└── Implementation Assumptions
    └── "We can do this because..."
    └── Organizational capacity requirements
```

**Critical for SEs:**
- Assumption: "Customers will pay premium for social impact"
- Assumption: "Beneficiaries will engage with our solution"
- Assumption: "Impact and profit don't conflict"

#### Step 5: Develop Indicators

**Connect to Lean Canvas Key Metrics:**

```text
INDICATOR DEVELOPMENT:
│
├── For Each Outcome Level
│   ├── What would we observe if this outcome occurred?
│   ├── How would we measure it?
│   └── What's the target?
│
├── Align with Lean Canvas
│   ├── Key Metrics → Short-term outcome indicators
│   └── Impact Metrics → Long-term outcome indicators
│
└── IRIS+ Framework Integration
    ├── What: Outcomes and outputs
    ├── Who: Target populations
    ├── How Much: Scale, depth, duration
    ├── Contribution: Attribution
    └── Risk: What could go wrong
```

#### Step 6: Package Feedback Outputs

```text
FEEDBACK TO OTHER SKILLS:
│
├── To /design-thinking:
│   └── Assumptions to test
│       └── "We assumed X. Can you validate through user research?"
│
├── To /lean-canvas:
│   ├── Impact goals → Validate Unfair Advantage
│   │   └── "Mission lock-in supported by this ToC"
│   └── Indicator alignment → Validate Key Metrics
│       └── "These metrics connect to these outcomes"
│
└── To /social-enterprise:
    └── Complete ToC for implementation
        └── Ready for Phase 4: IMPLEMENT & ITERATE
```

---

## Quick Reference

### The Six Essential Stages

| Stage | Focus |
|-------|-------|
| 1. Goals | Identify long-term impact |
| 2. Backward Mapping | Work from goals to preconditions |
| 3. Assumptions | Make causal logic explicit |
| 4. Interventions | Define program activities |
| 5. Indicators | Develop measurement approach |
| 6. Narrative | Create written explanation |

### NPC Ten Steps

1. Situation Analysis
2. Target Groups
3. Impact
4. Outcomes
5. Activities
6. Change Mechanisms
7. Sequencing
8. Diagram
9. Stakeholders
10. Assumptions

### Quality Criteria

**Plausibility:**
- Does the logic make sense?
- Is there evidence supporting causal claims?

**Feasibility:**
- Can the program realistically influence outcomes?
- Are resources sufficient?

**Testability:**
- Can outcomes be measured?
- Are indicators valid?

### BARMM Adaptations

**For Cooperatives:**
- Map ICA principles to outcomes
- Include member participation indicators
- Democratic governance in pathway

**For Social Enterprises:**
- Dual-track: Social impact + Business sustainability
- Distinguish beneficiaries from customers
- Shari'ah compliance where applicable

**For Development Programs:**
- Peace sensitivity in assumptions
- Align with BDP priorities
- Connect to UN SDGs

---

## Reference Files

| File | Use When |
|------|----------|
| [toc-methodology.md](references/toc-methodology.md) | Need methodology details, backward mapping, NPC steps |
| [barmm-adaptation.md](references/barmm-adaptation.md) | Need coop/SE/development adaptations, Shari'ah context |
| [curriculum-design.md](references/curriculum-design.md) | Designing ToC courses with /academy |

## Asset Files

| File | Use When |
|------|----------|
| [toc-template.md](assets/toc-template.md) | Creating new Theory of Change |
| [toc-examples.md](assets/toc-examples.md) | Need BARMM-specific coop/SE/development examples |

---

## Skill Integration Network

| Skill | Relationship | Data Exchange |
|-------|--------------|---------------|
| `/social-enterprise` | **Orchestrator** | SE invokes ToC for Phase 3: Determine & Direct |
| `/lean-canvas` | **Phase 2: Define & Develop** | Canvas outputs → ToC inputs |
| `/design-thinking` | **Feedback loop** | ToC assumptions → DT testing |
| `/enterprise-dev` | **Phase 4: Deliver & Drive** | ToC impact framework → Enterprise implementation |
| `/academy` | Curriculum design | ToC expertise for course development |
| `/cooperative` | Context adaptation | Cooperative principles in outcomes |
| `/featuredev` | Implementation | M&E feature requirements |
| `/deep-research` | Research foundation | Evidence for all modes |

### Data Flow

```text
/lean-canvas OUTPUTS:                  /toc INPUTS:
├── Problem + Solution        ────►    Interventions
├── Key Metrics              ────►    Outcome Indicators
├── UVP                      ────►    Impact statement basis
└── Customer Segments        ────►    Target groups

/toc OUTPUTS:                          /enterprise-dev INPUTS:
├── Theory of Change         ────►    Impact framework
├── Indicators               ────►    Success metrics
├── Assumptions              ────►    Risk management
└── Impact Statements             ────►    Strategic direction

                         ◄──── FEEDBACK LOOPS ────►
/toc OUTPUTS:                          FEEDBACK TO:
├── Assumptions to test      ────►    /design-thinking (user research)
├── Impact Statements             ────►    /lean-canvas (unfair advantage)
└── Indicator alignment      ────►    /lean-canvas (key metrics)
```

---

## Workflow: Theory of Change in Cooperatives

See [references/toc-methodology.md](references/toc-methodology.md) for detailed content.

## Cooperative Integration

When this skill encounters cooperative contexts, invoke `/cooperative` for specialized knowledge.
See [references/cooperative-integration.md](references/cooperative-integration.md) for triggers, patterns, and `/cooperative` assets.

## Constraints

- Use authoritative sources (ActKnowledge, Aspen Institute, NPC, UNDP)
- Align with evaluation best practices
- Support BARMM development priorities
- Adapt for cooperative and SE contexts
- Follow Shari'ah-compliant principles for BARMM programs
- Treat ToC as living documents requiring regular review
- Avoid purple colors in any UI recommendations
- When invoked for SE development, always prepare handoff outputs for /enterprise-dev
- Receive inputs from /lean-canvas when in SE Development Journey mode
- Provide feedback to /design-thinking for assumption testing
