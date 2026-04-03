---
name: investor
description: "Provides investor and investment banker perspective on valuation, M&A, capital markets, deal structuring, and due diligence. Use when designing investment banking courses (with /academy), consulting on investment decisions, advising on M&A processes, evaluating companies for acquisition, building investment thesis, or capital raising advisory. Covers DCF, comparables, precedent transactions, LBO analysis, and portfolio strategy. For technical financial analysis (ratios, models, statements), use /financial-analyst instead."
argument-hint: "[topic]"
---

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's investment/deal request                  ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

## What is an Investor Perspective?

> "Investment banking is a bridge between those who need capital and those who have it." — Goldman Sachs

The investor perspective differs from financial analysis in its:
1. **Decision Focus** - Making investment and deal decisions
2. **Return Orientation** - Evaluating risk-adjusted returns
3. **Deal Mindset** - Structuring transactions and negotiations
4. **Capital Allocation** - Deciding where to invest resources

### Investor vs. Financial Analyst

| Dimension | Investor | Financial Analyst |
|-----------|----------|-------------------|
| **Goal** | Decide and allocate | Understand and evaluate |
| **Focus** | Investment thesis | Technical analysis |
| **Output** | Investment decisions | Analysis and reports |
| **Questions** | "Should I invest?" | "What is the financial health?" |
| **Skill** | `/investor` | `/financial-analyst` |

---

## THE PERSPECTIVE vs THE TECHNICAL SKILL

```text
┌─────────────────────────────────────────────────────────────────────────────────┐
│          INVESTOR vs FINANCIAL ANALYST: COMPLETE PICTURE                         │
│                                                                                  │
│   /investor = THE PERSPECTIVE (the investment decision-maker viewpoint)         │
│   /financial-analyst = THE TECHNICAL SKILL (the analysis capabilities)          │
│                                                                                  │
│   Use BOTH together for complete financial guidance!                             │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                         THE RELATIONSHIP                                         │
│                                                                                  │
│   ┌──────────────────────────────────────┐                                      │
│   │     /financial-analyst               │                                      │
│   │     THE TECHNICAL SKILL              │                                      │
│   │     • Financial statement analysis   │                                      │
│   │     • Ratio analysis                 │                                      │
│   │     • Financial modeling mechanics   │                                      │
│   └──────────────────────────────────────┘                                      │
│                      │                                                           │
│                      │ PROVIDES FOUNDATION FOR                                   │
│                      ▼                                                           │
│   ┌──────────────────────────────────────────────────────────────┐              │
│   │              /investor (THE PERSPECTIVE)                      │              │
│   │     • Investment thesis development                          │              │
│   │     • Valuation for deal decisions                           │              │
│   │     • M&A process and due diligence                          │              │
│   │     • Deal structuring and negotiation                       │              │
│   │     • Capital markets (IPO, debt, equity)                    │              │
│   │     • Risk-adjusted return analysis                          │              │
│   │     • Portfolio strategy                                     │              │
│   └──────────────────────────────────────────────────────────────┘              │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## When to Use

| Trigger | Action |
|---------|--------|
| **Investment banking course/workshop design** | Mode 1: Curriculum Design (with `/academy`) |
| **Investment decision consulting** | Mode 2: Investment Consulting |
| **M&A advisory** | Mode 3: M&A Advisory |
| **Capital raising** | Mode 4: Capital Markets |
| **SE/Coop investment evaluation** | Mode 2 + `/social-enterprise` or `/cooperative` |

---

## Quick Reference

### The Four Core Valuation Methods

```text
VALUATION METHODS HIERARCHY:
│
├── 1. DISCOUNTED CASH FLOW (DCF)
│   ├── Intrinsic value based on future cash flows
│   ├── Discounted by WACC
│   └── Best for: Stable, predictable businesses
│
├── 2. COMPARABLE COMPANY ANALYSIS (Comps)
│   ├── Relative value based on trading multiples
│   ├── Uses public company peers
│   └── Best for: Quick market-based valuation
│
├── 3. PRECEDENT TRANSACTIONS (M&A Comps)
│   ├── Value based on historical deals
│   ├── Includes control premium
│   └── Best for: M&A scenarios
│
└── 4. LEVERAGED BUYOUT (LBO)
    ├── Value based on PE return requirements
    ├── IRR-driven analysis
    └── Best for: PE acquisition scenarios
```

### Valuation Methods Comparison

| Method | Basis | Typical Valuation | Best Use |
|--------|-------|-------------------|----------|
| **DCF** | Intrinsic | Medium-High | Strategic decisions |
| **Comparables** | Market | Medium | Quick reference |
| **Precedent Transactions** | Historical deals | Highest (control premium) | M&A negotiations |
| **LBO** | PE returns | Lowest (high discount rate) | PE floor price |

### M&A Process Stages

```text
M&A DEAL LIFECYCLE:
│
├── 1. STRATEGY & PLANNING
│   ├── Define acquisition criteria
│   ├── Screen potential targets
│   └── Develop initial investment thesis
│
├── 2. TARGET IDENTIFICATION
│   ├── Initial outreach
│   ├── Preliminary discussions
│   └── Sign NDA
│
├── 3. VALUATION & ANALYSIS
│   ├── Financial due diligence (→ /financial-analyst)
│   ├── Apply valuation methods
│   └── Develop deal structure
│
├── 4. LETTER OF INTENT (LOI)
│   ├── Negotiate key terms
│   ├── Establish exclusivity
│   └── Define due diligence scope
│
├── 5. DUE DILIGENCE
│   ├── Financial review
│   ├── Legal assessment
│   ├── Operational analysis
│   └── Commercial validation
│
├── 6. DEAL EXECUTION
│   ├── Final negotiations
│   ├── Definitive agreement
│   ├── Regulatory approvals
│   └── Closing
│
└── 7. POST-MERGER INTEGRATION
    ├── Integration planning
    ├── Synergy realization
    └── Value creation
```

---

## Workflow Modes

### Mode 1: Curriculum Design (with /academy)

When designing investment banking or investor courses.

#### STAGE 0: Deep Research (Mandatory)

**Before curriculum design, invoke `/deep-research` to gather evidence-based content.**

**Research Topics for Investment Training:**
- Investment banking fundamentals
- Valuation methodologies
- M&A process and deal structuring
- Capital markets (IPO, debt, equity)
- Private equity and venture capital
- Deal case studies

#### Step 1: Determine Course Level

| Level | Audience | Duration | Focus |
|-------|----------|----------|-------|
| **Foundation** | Business students, entrepreneurs | 8-16 hours | Investment basics, valuation concepts |
| **Intermediate** | Finance professionals, analysts | 24-40 hours | Full valuation methods, M&A process |
| **Advanced** | Investment professionals, PE/VC | 40+ hours | Complex deals, LBO, restructuring |
| **Executive** | C-suite, board members | 8-16 hours | Deal strategy, capital raising |

#### Step 2: Select Curriculum Modules

**Foundation Course:**
1. Introduction to Investment Banking
2. Understanding Capital Markets
3. Introduction to Valuation
4. Basic M&A Concepts
5. Investment Decision Making

**Intermediate Course:**
1. Investment Banking Industry Deep Dive
2. DCF Valuation Methodology
3. Comparable Company Analysis
4. Precedent Transaction Analysis
5. M&A Process and Deal Lifecycle
6. Due Diligence Framework
7. Deal Structuring Basics
8. Investment Thesis Development

**Advanced Course:**
1. Advanced DCF and WACC
2. LBO Analysis and Modeling
3. Complex M&A Structures
4. Capital Markets (IPO, Debt Offerings)
5. Private Equity Investment Framework
6. Venture Capital Methodology
7. Restructuring and Distressed Investing
8. Deal Negotiation and Execution

See [references/curriculum-design.md](references/curriculum-design.md) for detailed curriculum.

---

### Mode 2: Investment Consulting

For investment decision consulting.

#### Step 1: Identify Investment Type

```text
INVESTMENT TYPE SELECTION:
│
├── STRATEGIC ACQUISITION
│   ├── Acquiring for synergies/growth
│   ├── Focus: Strategic fit, synergy valuation
│   └── Methods: DCF, Precedent, Synergy analysis
│
├── FINANCIAL INVESTMENT
│   ├── Investing for returns
│   ├── Focus: Risk-adjusted returns
│   └── Methods: DCF, LBO, IRR analysis
│
├── MINORITY INVESTMENT
│   ├── Taking stake without control
│   ├── Focus: Valuation, governance rights
│   └── Methods: DCF, Comparables
│
├── CAPITAL RAISING
│   ├── Raising funds for company
│   ├── Focus: Valuation, terms, dilution
│   └── Methods: Comparables, precedent raises
│
└── PORTFOLIO STRATEGY
    ├── Allocating across investments
    ├── Focus: Risk-return optimization
    └── Methods: Portfolio theory, diversification
```

#### Step 2: Develop Investment Thesis

**Investment Thesis Framework:**

```text
INVESTMENT THESIS TEMPLATE:
│
├── OPPORTUNITY
│   ├── What is the investment opportunity?
│   ├── Why is it attractive now?
│   └── What is the market context?
│
├── VALUE DRIVERS
│   ├── What drives the company's value?
│   ├── What are the growth catalysts?
│   └── What competitive advantages exist?
│
├── VALUATION
│   ├── What is the company worth? (Methods: DCF, Comps, Precedent)
│   ├── What price should we pay?
│   └── What is the expected return?
│
├── PRODUCT DIFFERENTIATION (MVaP Assessment)
│   ├── Does the company have ONE clear Delighter as UVP?
│   ├── Are Performance features at competitive threshold (not over-engineered)?
│   ├── Are Must-Haves handled efficiently (existing solutions)?
│   └── Is this a "Maximally Undifferentiated Product" (MUP)? → Red flag
│   REFERENCE: ../shared/references/mvap-framework.md
│
├── RISKS
│   ├── What are the key risks?
│   ├── How do we mitigate them?
│   └── What would make us exit?
│
└── EXECUTION
    ├── How do we execute the investment?
    ├── What is the timeline?
    └── What are the key milestones?
```

#### Step 3: Provide Recommendations

**Output Format:**

```text
INVESTMENT RECOMMENDATION

INVESTMENT OVERVIEW:
├── Target: [Company/Asset]
├── Type: [Strategic/Financial/Minority]
├── Thesis: [One-sentence thesis]
└── Recommendation: [Buy/Hold/Pass]

VALUATION SUMMARY:
| Method | Value Range | Weight |
|--------|-------------|--------|
| DCF | $X - $Y | 40% |
| Comparables | $X - $Y | 30% |
| Precedent | $X - $Y | 30% |
| Blended | $X - $Y | 100% |

KEY VALUE DRIVERS:
1. [Driver with quantification]
2. [Driver with quantification]

RISK ASSESSMENT:
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk] | High/Med/Low | High/Med/Low | [Strategy] |

RETURN ANALYSIS:
├── Expected IRR: X%
├── Expected Multiple: X.Xx
└── Payback Period: X years

RECOMMENDATION:
[Detailed recommendation with conditions]
```

---

### Mode 3: M&A Advisory

See [ma-process.md](references/ma-process.md) for M&A deal types, due diligence framework, and deal structuring.

### Mode 4: Capital Markets

See [valuation-methods.md](references/valuation-methods.md) for capital raising options and process.

## Core Frameworks

See [valuation-methods.md](references/valuation-methods.md) for DCF formula, comparable company analysis, and LBO analysis details.

## When to Invoke /financial-analyst

Always consider `/financial-analyst` for technical analysis foundation:

| If working on... | /investor handles (PERSPECTIVE) | Consider /financial-analyst for (TECHNICAL) |
|------------------|--------------------------------|---------------------------------------------|
| Valuation | Investment decision, pricing | Model mechanics, ratio inputs |
| Due diligence | Deal evaluation | Financial statement analysis |
| M&A | Deal structuring, negotiation | Quality of earnings, cash flow |
| Investment thesis | Decision framework | Fundamental analysis |

---

## Y Combinator Investment Framework

YC's investment methodology provides an early-stage lens for this skill. See shared references for comprehensive YC content.

### YC Standard Deal Terms (2024)

| Component | Amount | Terms |
|-----------|--------|-------|
| **Initial Investment** | $125,000 | 7% equity (common stock) |
| **MFN SAFE** | $375,000 | Uncapped, Most Favored Nation |
| **Total** | $500,000 | Combined investment per company |

### YC's SAFE Investment Vehicle

**SAFE = Simple Agreement for Future Equity**
- Not debt, not equity—converts to equity in future priced round
- No valuation cap on the MFN portion
- Founder-friendly (no board seats, no control provisions)

### YC Due Diligence: Founder Evaluation

| Factor | Questions |
|--------|-----------|
| **Clarity** | Can they explain the idea in one sentence? |
| **Traction** | What's their weekly growth rate? (5-7% = good) |
| **Domain Expertise** | Why are they uniquely suited? |
| **Determination** | Evidence of grit in past challenges? |
| **Technical Ability** | Can they build it themselves? |

### YC Growth Metrics for Investors

| Weekly Growth | Investment Signal |
|---------------|-------------------|
| 0-2% | Struggling, risky bet |
| 3-5% | Promising, needs improvement |
| 5-7% | Good, fundable |
| 10%+ | Exceptional, competitive deal |

### YC Shared References

| Reference | Content |
|-----------|---------|
| [YC SAFE Terms](../shared/references/yc-safe-terms.md) | SAFE structure, conversion mechanics, due diligence |
| [YC Growth Metrics](../shared/references/yc-growth-metrics.md) | Benchmarks, PMF indicators, unit economics |
| [YC Methodology](../shared/references/yc-methodology.md) | What YC looks for in startups |

---

## References

| Reference | Purpose |
|-----------|---------|
| [valuation-methods.md](references/valuation-methods.md) | DCF, Comps, Precedent, LBO |
| [ma-process.md](references/ma-process.md) | M&A stages and due diligence |
| [capital-markets.md](references/capital-markets.md) | IPO, debt, equity raising |
| [curriculum-design.md](references/curriculum-design.md) | Training curriculum for /academy |
| [deal-structuring.md](references/deal-structuring.md) | Transaction structuring |

---

## Skill Integration Network

| Skill | Relationship | Data Exchange |
|-------|--------------|---------------|
| `/financial-analyst` | **THE TECHNICAL SKILL** | Technical analysis feeds investment decisions |
| `/academy` | Curriculum design | Investment banking course development |
| `/startup` | Investment perspective | Evaluating startup investments |
| `/enterprise-dev` | Growth financing | Capital raising for growth |
| `/social-enterprise` | Impact investing | SE investment evaluation |
| `/cooperative` | Coop investment | Coop financing structures |
| `/featuredev` | Implementation | Investment platform features |

---

## Constraints

- Use authoritative sources (WSP, CFI, 365 Careers, IB practitioners)
- Adapt for BARMM context (SE and cooperative investment)
- Support both traditional and impact investing perspectives
- Consider Shari'ah-compliant investment structures where applicable
- Avoid purple colors in any UI recommendations
- Prioritize practical, deal-focused approaches
- When technical analysis is needed, invoke /financial-analyst

---
