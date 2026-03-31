---
name: lean-canvas
description: "Provides Lean Canvas business modeling expertise for cooperatives and social enterprises in BARMM. Use when designing Lean Canvas courses (with /academy), consulting on business model development or validation, building business planning platform features, or as Phase 2 DEFINE & DEVELOP in the 4D SE Development Journey (invoked by /social-enterprise). Covers Ash Maurya's Running Lean methodology, 9 building blocks, Lean Startup integration, customer interviews, and BARMM adaptations."
argument-hint: "[topic]"
---

# Lean Canvas Skill

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's lean canvas request                      ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

## When to Use

| Trigger | Action |
|---------|--------|
| **SE Development - Phase 2: Define & Develop** | Mode 4: SE Development Journey |
| Lean Canvas course/workshop design | Mode 1 with `/academy` for curriculum |
| Business model consulting | Mode 2 with canvas frameworks |
| Platform features for business planning | Mode 3 with `/featuredev` |
| Coop/SE business model questions | Provide context-adapted guidance |

---

## Core Concepts

### What is Lean Canvas?

A 1-page business modeling tool created by Ash Maurya (2010), adapting BMC for startups under uncertainty. Running Lean synthesizes Customer Development (Blank), Lean Startup (Ries), and Bootstrapping.

### Pre-Canvas Vision Exercise (M-2)

Before canvas creation begins, require the founder to answer three questions. Do not proceed to fill blocks until all three are clear:

| Question | Prompt | Purpose |
|----------|--------|---------|
| **Who** | Who is the specific customer segment? (be precise — not "SMEs", but "female market vendors in Cotabato City with 3–10 employees") | Anchors all canvas blocks to a real person |
| **Value-Creating Action** | What does your product/service actually do for them? (one sentence, active voice) | Clarifies the core job-to-be-done before UVP is written |
| **MSC (Minimum Success Criteria)** | What is the smallest 3-year outcome that would justify continuing this investment? (be specific — revenue, lives affected, retention rate) | Prevents scope creep; creates a testable success benchmark |

If any answer is vague, prompt the founder to sharpen it before proceeding. The MSC is especially important: founders who skip it tend to move goalposts or over-build.

### The 3 Rings Framework (M-10)

Structure canvas work in three concentric rings. Complete the inner ring before moving outward — each ring de-risks a different assumption layer:

```
+-------------------------------------------+
|  MARKET RING (external)                   |
|  existing alternatives, cost structure,   |
|  revenue streams                          |
|   +-------------------------------+       |
|   |  CUSTOMER RING (relational)   |       |
|   |  customer segments, channels, |       |
|   |  early adopters               |       |
|   |   +-----------------+         |       |
|   |   |  FOUNDER RING   |         |       |
|   |   |  problem,       |         |       |
|   |   |  solution,      |         |       |
|   |   |  unfair adv,    |         |       |
|   |   |  key metrics    |         |       |
|   |   +-----------------+         |       |
|   +-------------------------------+       |
+-------------------------------------------+
```

| Ring | Blocks | Core Question | Proceed When |
|------|--------|---------------|--------------|
| **Founder Ring** (innermost) | Problem, Solution, Unfair Advantage, Key Metrics | "Do I understand the problem deeply enough to build a solution?" | Problem interviews complete; must-have problem validated |
| **Customer Ring** | Customer Segments, Channels, Early Adopters | "Who will I learn from first, and how do I reach them?" | Early adopter profile defined; first 10 customers identified |
| **Market Ring** (outermost) | Existing Alternatives, Cost Structure, Revenue Streams | "Is there a viable business here at market scale?" | Unit economics pencil out; pricing tested with at least one customer |

### The 9 Building Blocks

| Block | Purpose | SE Adaptation |
|-------|---------|---------------|
| **Problem** | Top 3 customer problems | Social problem + market problem |
| **Customer Segments** | Target customers + early adopters | Beneficiaries + paying customers |
| **Unique Value Proposition** | Why you're different | Social impact + business value |
| **Solution** | Top 3 features (keep small) | Impact delivery mechanism |
| **Channels** | Path to customers | Impact channels + sales channels |
| **Revenue Streams** | How you make money | Earned income + grants/donations |
| **Cost Structure** | Major costs | Impact costs + operational costs |
| **Key Metrics** | The ONE number that matters | Impact metrics + business metrics |
| **Unfair Advantage** | What cannot be easily copied | Mission lock-in, community trust |

---

## Running Lean: Three-Stage Validation

```
+-------------------+     +-------------------+     +-------------------+
|  PROBLEM/SOLUTION |     |  PRODUCT/LAUNCH   |     |  PRODUCT/MARKET   |
|       FIT         | --> |       FIT         | --> |       FIT         |
+-------------------+     +-------------------+     +-------------------+
   "Do I have a           "Am I ready to           "Have I built
    problem worth          learn from               something people
    solving?"              customers?"              want?"
```

| Stage | Core Question | Key Activities | Exit Criteria |
|-------|---------------|----------------|---------------|
| **Problem/Solution Fit** | Problem worth solving? | Sketch canvas, Problem/Solution Interviews | Early adopters, must-have problem, pricing |
| **Product/Launch Fit** | Ready to learn? | MVP reduction, Activation Flow, AARRR | MVP ready, dashboard instrumented |
| **Product/Market Fit** | Built something wanted? | Retention focus, pivot experiments | 40% retention, Sean Ellis Test |

### The Sean Ellis Test

Ask users: "How would you feel if you could no longer use [product]?" If **40%+** say "very disappointed," you likely have Product/Market Fit.

### Evidence Ladder Validation Gate (FM-10)

Before any platform or product moves from planning to development, require Level 2+ evidence. This gate applies to all modes — consulting, platform features, and SE development.

| Level | Evidence Type | Examples | Sufficient? |
|-------|--------------|----------|-------------|
| **Level 1** | Stated interest | "Yes, I'd use that", "Sounds great", verbal encouragement | **NO** — not sufficient |
| **Level 2** | Behavioral interest | Signed up for waitlist, attended demo, shared contact info, referred a friend | **YES** — minimum to proceed |
| **Level 3** | Commitment | Paid deposit, signed pilot agreement, allocated budget, pre-order | **YES** — strong signal |

**Warning trigger:** If a founder (or platform feature request) presents only Level 1 evidence, surface this warning before proceeding:

> "You currently have Level 1 evidence (stated interest). This is not sufficient to justify building. Before development begins, gather at least Level 2 evidence — waitlist signups, demo attendance, or contact info exchange. Stated interest is cheap; behavioral evidence is not. What's your plan to get to Level 2?"

This gate applies especially to:
- Mode 3 (Platform Feature Development): do not build features backed only by stated interest
- Mode 4 SE Development: do not advance past canvas to product build without Level 2+ evidence
- Any consulting context where a founder is about to hire, spend, or build based on conversations alone

### AARRR Pirate Metrics

| Metric | Definition | Focus Stage |
|--------|------------|-------------|
| **Acquisition** | How users find you | Product/Launch Fit |
| **Activation** | Great first experience | Product/Launch Fit |
| **Retention** | Do they come back? | Product/Market Fit |
| **Revenue** | How you make money | Product/Market Fit |
| **Referral** | Do they tell others? | Scale |

---

## Customer Interview Scripts

### Problem Interview (20-30 min)

| Section | Duration | Purpose |
|---------|----------|---------|
| Welcome / Set Stage | 2 min | Explain format, emphasize learning not selling |
| Collect Demographics | 2 min | Test customer segment hypothesis |
| Tell a Story | 2 min | Set problem context |
| Problem Ranking | 4 min | Test which problems resonate |
| Explore Worldview | 15 min | How they solve today - THE HEART |
| Wrapping Up | 2 min | Permission to follow-up, referrals |

### Solution Interview (25-30 min)

Show mockups/demo BEFORE building. Test feature resonance and pricing. Key principle: "The right price is one the customer accepts but with a little resistance."

### MVP Interview (25-30 min)

5-second test for UVP comprehension, test pricing page, complete activation flow.

See [advanced-concepts.md](references/advanced-concepts.md) for cohort analysis, CHI, dashboard building, feature lifecycle, and pivot experiments.

---

## Workflow Modes

### Mode 1: Curriculum Design (with /academy)

1. Invoke `/deep-research` for evidence-based content (mandatory)
2. Select level: Foundational / Intermediate / Advanced
3. See [curriculum-design.md](references/curriculum-design.md) for detailed curriculum

**Standard Lean Canvas Course Modules:**
1. Introduction to Lean Canvas
2. Problem Discovery (link to `/design-thinking`)
3. Customer Segments
4. Unique Value Proposition
5. Solution Design
6. Channels & Revenue
7. Metrics & Costs
8. Unfair Advantage & Iteration (link to `/toc`)

### Mode 2: Business Consulting

1. Assess stage using Three-Stage Validation
2. Apply appropriate framework (interviews, MVP, retention)
3. Consider context: Cooperative principles, SE mission, BARMM regulations

### Mode 3: Platform Feature Development

1. Read [barmm-adaptation.md](references/barmm-adaptation.md) for context
2. Align with cooperative principles (ICA 7 principles)
3. Support Social Lean Canvas for SEs

### Mode 4: SE Development Journey (Phase 2: Define & Develop)

**Inputs from /design-thinking:** Problem Statement, User Personas, Key Insights, HMW Statements

**SE-Adapted Canvas Block Guidance:**
- **Problem**: Core social problem + market problem + systemic barrier
- **Customer Segments**: Beneficiaries + Customers + Early Adopters
- **UVP**: Social value + customer value combined
- **Solution**: Use MVaP (Minimum Valuable Product) approach - Delighter as UVP, performance at threshold, must-haves via existing solutions
- **Revenue**: Earned income + contributed income + blended

**Outputs for /toc:** Problem + Solution → Interventions, Key Metrics → Outcome Indicators, UVP → Impact statement

### MVaP: The Solution Block Framework

| Type | Customer Response | Strategy |
|------|-------------------|----------|
| **Must-Have** | Dissatisfaction if absent | Meet threshold, use existing solutions |
| **Performance** | Linear - more = more satisfaction | Define MPM, stop at threshold |
| **Delighter** | Absent = okay; present = WOW | Build UVP here (80% focus) |
| **Zone of Indifference** | "Meh" | AVOID - cut from roadmap |

See: `../shared/references/mvap-framework.md` for complete framework.

---

## BARMM Adaptations

**For Cooperatives:** Add member-owner perspective to Segments, include patronage in Revenue, consider democratic governance in Solution.

**For Social Enterprises:** Distinguish beneficiaries from paying customers, add impact metrics, ensure Shari'ah compliance where applicable.

See [cooperative-integration.md](references/cooperative-integration.md) for detailed cooperative business model adaptations, member value proposition framework, revenue models by cooperative type, and practical scenarios.

---

## Reference Files

| File | Use When |
|------|----------|
| [lean-canvas-framework.md](references/lean-canvas-framework.md) | Need 9 blocks details, BMC comparison |
| [barmm-adaptation.md](references/barmm-adaptation.md) | Need coop/SE adaptations, ICA principles |
| [curriculum-design.md](references/curriculum-design.md) | Designing courses with /academy |
| [advanced-concepts.md](references/advanced-concepts.md) | Cohort analysis, CHI, dashboards, feature lifecycle, pivot experiments |
| [cooperative-integration.md](references/cooperative-integration.md) | Cooperative business models, member value proposition, revenue models, practical scenarios |

## Asset Files

| File | Use When |
|------|----------|
| [lean-canvas-template.md](assets/lean-canvas-template.md) | Creating new Lean Canvas |
| [lean-canvas-examples.md](assets/lean-canvas-examples.md) | Need BARMM-specific examples |

---

## Skill Integration Network

| Skill | Relationship | Data Exchange |
|-------|--------------|---------------|
| `/social-enterprise` | **Orchestrator** | SE invokes LC for Phase 2 |
| `/design-thinking` | **Phase 1** | DT outputs → Canvas inputs |
| `/toc` | **Phase 3** | Canvas outputs → ToC inputs |
| `/enterprise-dev` | **Phase 4** | Canvas → Marketing, Product, Finance |
| `/academy` | Curriculum design | LC expertise for course development |
| `/cooperative` | Context adaptation | Coop principles in canvas |
| `/finance` | Organizational finance | Budgeting, controls, PFRF |
| `/financial-analyst` | Financial modeling | Revenue projections, unit economics |
| `/investor` | Fundraising | Term sheets, valuations, pitch |
| `/deep-research` | Research foundation | Evidence for all modes |

---

## Constraints

- Use authoritative sources (Ash Maurya, Eric Ries, Strategyzer)
- Align with Lean Startup methodology
- Support CSEA's regulatory mandate in BARMM
- Adapt for cooperative and SE contexts
- Follow Shari'ah-compliant principles for BARMM businesses
- Avoid purple colors in any UI recommendations
- When invoked for SE development, always prepare handoff outputs for /toc
- Receive inputs from /design-thinking when in SE Development Journey mode
