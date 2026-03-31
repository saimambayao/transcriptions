---
name: financial-analyst
description: "Provides financial analysis competencies and methodologies including financial statement analysis, ratio analysis, DuPont decomposition, financial modeling, cash flow analysis, and Excel for finance. Use when designing financial analysis courses (with /academy), consulting on financial health assessment, building financial models, performing ratio analysis for cooperatives or social enterprises, or teaching CFA-level analytical skills. For investment decision-making perspective, use /investor instead."
argument-hint: "[topic]"
---

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's financial analysis request               ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

## What is Financial Analysis?

> "Financial analysis is the process of evaluating businesses, projects, budgets, and other finance-related entities to determine their performance and suitability." — CFA Institute

Financial analysis differs from investing in its:
1. **Technical Focus** - Competencies and methodologies for analysis
2. **Objective Assessment** - Understanding financial health, not making investment decisions
3. **Tool Mastery** - Excel, ratios, models as analytical instruments
4. **Foundational Nature** - Building blocks for all finance roles

### Financial Analyst vs. Investor

| Dimension | Financial Analyst | Investor |
|-----------|-------------------|----------|
| **Goal** | Understand and evaluate | Decide and allocate |
| **Focus** | Technical analysis | Investment thesis |
| **Output** | Analysis, models, reports | Investment decisions |
| **Questions** | "What is the financial health?" | "Should I invest?" |
| **Skill** | `/financial-analyst` | `/investor` |

---

## THE TECHNICAL SKILL vs THE PERSPECTIVE

```text
┌─────────────────────────────────────────────────────────────────────────────────┐
│          FINANCIAL ANALYST vs INVESTOR: COMPLETE PICTURE                         │
│                                                                                  │
│   /financial-analyst = THE TECHNICAL SKILL (the analysis capabilities)          │
│   /investor = THE PERSPECTIVE (the investment decision-maker viewpoint)         │
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
│   │     • Ratio analysis (DuPont, etc.)  │                                      │
│   │     • Financial modeling in Excel    │                                      │
│   │     • Cash flow analysis             │                                      │
│   │     • Working capital analysis       │                                      │
│   │     • Trend analysis & forecasting   │                                      │
│   │     • Valuation mechanics (how)      │                                      │
│   └──────────────────────────────────────┘                                      │
│                      │                                                           │
│                      │ FEEDS INTO                                                │
│                      ▼                                                           │
│   ┌──────────────────────────────────────────────────────────────┐              │
│   │              /investor (THE PERSPECTIVE)                      │              │
│   │    Investment decisions, deal evaluation, portfolio strategy │              │
│   └──────────────────────────────────────────────────────────────┘              │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## When to Use

| Trigger | Action |
|---------|--------|
| **Financial analysis course/workshop design** | Mode 1: Curriculum Design (with `/academy`) |
| **Financial statement analysis consulting** | Mode 2: Analysis Consulting |
| **Building financial models** | Mode 3: Financial Modeling |
| **Platform finance features** | Mode 4: Platform Features (with `/featuredev`) |
| **SE/Coop financial health assessment** | Mode 2 + `/social-enterprise` or `/cooperative` |

---

## Quick Reference

### The Financial Analysis Framework (CFA)

```text
FINANCIAL ANALYSIS PROCESS:
│
├── 1. ARTICULATE PURPOSE
│   ├── What questions need answering?
│   ├── What level of detail is required?
│   └── What factors and relationships matter?
│
├── 2. COLLECT INPUT DATA
│   ├── Financial statements (Income, Balance Sheet, Cash Flow)
│   ├── Industry data and benchmarks
│   └── Economic and market data
│
├── 3. PROCESS THE DATA
│   ├── Calculate ratios
│   ├── Build models
│   └── Perform adjustments
│
├── 4. ANALYZE AND INTERPRET
│   ├── Compare to benchmarks
│   ├── Identify trends
│   └── Assess drivers
│
└── 5. DEVELOP CONCLUSIONS
    ├── Answer the original questions
    ├── Make recommendations
    └── Communicate findings
```

### Five Categories of Ratio Analysis

| Category | Purpose | Key Ratios |
|----------|---------|------------|
| **Liquidity** | Short-term obligations | Current, Quick, Cash, Defensive Interval |
| **Activity** | Operational efficiency | Inventory Turnover, Receivables Turnover, Asset Turnover |
| **Solvency** | Long-term debt capacity | Debt-to-Equity, Interest Coverage, Debt Ratio |
| **Profitability** | Earnings generation | Gross Margin, Net Margin, ROA, ROE |
| **Valuation** | Market value relative to fundamentals | P/E, P/B, EV/EBITDA |

### DuPont Analysis (3-Step)

```text
ROE = Net Profit Margin × Asset Turnover × Equity Multiplier
      (Profitability)     (Efficiency)     (Leverage)

        Net Income        Revenue          Total Assets
ROE = ─────────────── × ─────────────── × ───────────────
          Revenue        Total Assets    Shareholders' Equity
```

### DuPont Analysis (5-Step)

```text
ROE = Tax Burden × Interest Burden × EBIT Margin × Asset Turnover × Leverage

        Net Income     EBT      EBIT     Revenue     Total Assets
ROE = ─────────── × ────── × ────── × ────────── × ─────────────
          EBT        EBIT    Revenue  Total Assets   Equity
```

---

## Workflow Modes

### Mode 1: Curriculum Design (with /academy)

When designing financial analysis courses or workshops.

#### STAGE 0: Deep Research (Mandatory)

**Before curriculum design, invoke `/deep-research` to gather evidence-based content.**

**Research Topics for Financial Analysis Training:**
- CFA curriculum and competencies
- Financial statement analysis techniques
- Ratio analysis frameworks
- Financial modeling best practices
- Excel skills for finance professionals
- Industry-specific analysis methods

#### Step 1: Determine Course Level

| Level | Audience | Duration | Focus |
|-------|----------|----------|-------|
| **Foundation** | Business students, non-finance managers | 8-16 hours | Reading financial statements, basic ratios |
| **Intermediate** | Finance professionals, analysts | 24-40 hours | Full ratio analysis, modeling basics |
| **Advanced** | Senior analysts, FP&A | 40+ hours | Complex modeling, valuation, forecasting |
| **Executive** | C-suite, board members | 8-16 hours | Strategic financial insights, dashboards |

#### Step 2: Select Curriculum Modules

**Foundation Course:**
1. Introduction to Financial Statements
2. Reading the Income Statement
3. Understanding the Balance Sheet
4. Analyzing Cash Flow Statements
5. Basic Ratio Analysis

**Intermediate Course:**
1. Financial Statement Analysis Deep Dive
2. Liquidity and Activity Ratio Analysis
3. Profitability and Solvency Analysis
4. DuPont Analysis and ROE Decomposition
5. Introduction to Financial Modeling
6. Excel for Financial Analysis
7. Working Capital Analysis
8. Trend Analysis and Forecasting

**Advanced Course:**
1. Advanced Financial Statement Analysis
2. Financial Modeling Best Practices
3. Building Integrated Financial Models
4. Sensitivity and Scenario Analysis
5. Valuation Foundations (DCF Mechanics)
6. Industry-Specific Analysis
7. Cash Flow Forecasting
8. Management Reporting and Dashboards

See [references/curriculum-design.md](references/curriculum-design.md) for detailed curriculum.

---

### Mode 2: Analysis Consulting

For financial analysis consulting engagements.

#### Step 1: Identify Analysis Type

```text
ANALYSIS TYPE SELECTION:
│
├── PERFORMANCE ANALYSIS
│   ├── How is the company performing?
│   ├── What are the trends?
│   └── → Use profitability ratios, trend analysis
│
├── LIQUIDITY ANALYSIS
│   ├── Can the company meet short-term obligations?
│   ├── Is working capital adequate?
│   └── → Use liquidity ratios, cash flow analysis
│
├── SOLVENCY ANALYSIS
│   ├── Can the company meet long-term obligations?
│   ├── Is debt level sustainable?
│   └── → Use leverage ratios, coverage ratios
│
├── EFFICIENCY ANALYSIS
│   ├── How well are assets being used?
│   ├── Is the operating cycle optimal?
│   └── → Use activity ratios, DuPont analysis
│
└── COMPREHENSIVE ANALYSIS
    ├── Full financial health assessment
    └── → Use all ratio categories + modeling
```

#### Step 2: Apply Appropriate Framework

| Analysis Type | Framework | Key Deliverables |
|---------------|-----------|------------------|
| **Performance** | Trend Analysis, Common-Size | Performance dashboard, trend charts |
| **Liquidity** | Working Capital Analysis | Liquidity report, cash position |
| **Solvency** | Leverage Analysis | Debt capacity assessment |
| **Efficiency** | DuPont, Activity Ratios | Efficiency scorecard |
| **Comprehensive** | Full Ratio Suite + Model | Integrated financial report |

#### Step 3: Provide Recommendations

**Output Format:**

```text
FINANCIAL ANALYSIS REPORT

ANALYSIS PURPOSE: [What question are we answering]

EXECUTIVE SUMMARY:
[Key findings in 3-5 bullet points]

FINANCIAL HEALTH OVERVIEW:
├── Profitability: [Strong/Adequate/Weak] - [Key metrics]
├── Liquidity: [Strong/Adequate/Weak] - [Key metrics]
├── Solvency: [Strong/Adequate/Weak] - [Key metrics]
└── Efficiency: [Strong/Adequate/Weak] - [Key metrics]

DETAILED FINDINGS:
[Organized by ratio category with trends]

KEY DRIVERS:
- [Driver 1 and its impact]
- [Driver 2 and its impact]

RECOMMENDATIONS:
1. [Action item with expected impact]
2. [Action item with expected impact]

WATCH AREAS:
- [Risk or concern to monitor]
```

#### Context-Specific Considerations

**For Cooperatives** (use with `/cooperative`):
- Consider patronage refund impact on profitability
- Analyze statutory fund allocations (CETF, Reserve)
- Assess member equity vs. institutional capital
- See [references/cooperative-finance.md](references/cooperative-finance.md)

**For Social Enterprises** (use with `/social-enterprise`):
- Balance financial and impact metrics
- Consider grant income vs. earned revenue
- Assess sustainability alongside impact
- See [references/se-finance.md](references/se-finance.md)

---

### Mode 3: Financial Modeling

For building financial models in Excel.

#### Financial Model Types

| Model Type | Purpose | Complexity |
|------------|---------|------------|
| **3-Statement Model** | Integrated projections | Medium |
| **Budget Model** | Planning and control | Low-Medium |
| **Forecasting Model** | Revenue/expense projections | Medium |
| **Working Capital Model** | Cash conversion optimization | Medium |
| **DCF Model** | Valuation (mechanics) | High |
| **Scenario Model** | What-if analysis | Medium-High |

#### Best Practices for Financial Modeling

```text
FINANCIAL MODELING BEST PRACTICES:
│
├── STRUCTURE
│   ├── Separate inputs, calculations, outputs
│   ├── Use consistent formatting
│   └── Document assumptions clearly
│
├── FORMULAS
│   ├── Keep formulas simple and auditable
│   ├── Avoid circular references (or handle properly)
│   └── Use named ranges for key inputs
│
├── ERROR CHECKING
│   ├── Build in balance sheet checks
│   ├── Include reasonableness tests
│   └── Use data validation
│
└── PRESENTATION
    ├── Create summary dashboards
    ├── Use charts for key metrics
    └── Format for printing/sharing
```

#### Integration with /investor

When models are used for investment decisions, invoke `/investor` for:
- Investment thesis development
- Deal evaluation perspective
- Return requirements and hurdle rates
- Risk-adjusted analysis

---

### Mode 4: Platform Features (with /featuredev)

When building finance-related features for the platform.

#### Feature Areas

| Feature | Description | Portal |
|---------|-------------|--------|
| **Financial Dashboard** | Key ratio visualization | Coop/SE Portal |
| **Ratio Calculator** | Interactive ratio analysis | Coop/SE Portal |
| **Financial Health Score** | Automated assessment | CSEA Portal |
| **Trend Visualizer** | Multi-period comparison | Coop/SE Portal |
| **Cash Flow Tracker** | Cash position monitoring | Coop/SE Portal |
| **Benchmark Comparison** | Industry/peer comparison | CSEA Portal |

#### Integration Points

- **MoroAcademy**: Financial analysis courses
- **CSEA Portal**: Cooperative/SE financial monitoring
- **Coop/SE Portal**: Self-service financial analysis tools

---

## Core Frameworks

### Financial Statement Analysis

**Three Core Statements:**

| Statement | Purpose | Key Questions |
|-----------|---------|---------------|
| **Income Statement** | Profitability over period | Is the company profitable? Are margins healthy? |
| **Balance Sheet** | Financial position at point in time | What does the company own/owe? Is it solvent? |
| **Cash Flow Statement** | Cash movements over period | Where does cash come from? Where does it go? |

**Common-Size Analysis:**
- Vertical: Express items as % of base (revenue or total assets)
- Horizontal: Express items as % change from base period

### Ratio Analysis Framework

**Liquidity Ratios:**

| Ratio | Formula | Interpretation |
|-------|---------|----------------|
| Current Ratio | Current Assets / Current Liabilities | >1 means can cover short-term obligations |
| Quick Ratio | (CA - Inventory) / CL | Stricter liquidity test |
| Cash Ratio | Cash / Current Liabilities | Most conservative measure |

**Activity Ratios:**

| Ratio | Formula | Interpretation |
|-------|---------|----------------|
| Inventory Turnover | COGS / Avg Inventory | How fast inventory sells |
| Receivables Turnover | Revenue / Avg AR | How fast receivables collect |
| Asset Turnover | Revenue / Avg Total Assets | Revenue per asset dollar |

**Profitability Ratios:**

| Ratio | Formula | Interpretation |
|-------|---------|----------------|
| Gross Margin | Gross Profit / Revenue | Production profitability |
| Net Margin | Net Income / Revenue | Bottom-line profitability |
| ROA | Net Income / Avg Total Assets | Return on assets |
| ROE | Net Income / Avg Equity | Return on equity |

**Solvency Ratios:**

| Ratio | Formula | Interpretation |
|-------|---------|----------------|
| Debt-to-Equity | Total Debt / Total Equity | Leverage level |
| Interest Coverage | EBIT / Interest Expense | Ability to pay interest |
| Debt Ratio | Total Debt / Total Assets | Debt as % of assets |

---

## When to Invoke /investor

Always consider `/investor` when working on `/financial-analyst` topics that require investment perspective:

| If working on... | /financial-analyst handles (TECHNICAL) | Consider /investor for (PERSPECTIVE) |
|------------------|----------------------------------------|--------------------------------------|
| Valuation | DCF mechanics, model building | Investment decision, buy/sell |
| Financial analysis | Ratios, trends, models | Investment thesis, risk-adjusted returns |
| Company assessment | Financial health | Investment attractiveness |
| Due diligence support | Data analysis | Deal evaluation |

---

## References

| Reference | Purpose |
|-----------|---------|
| [financial-analysis-frameworks.md](references/financial-analysis-frameworks.md) | Ratio analysis, DuPont, common-size analysis |
| [financial-modeling.md](references/financial-modeling.md) | Excel modeling best practices |
| [curriculum-design.md](references/curriculum-design.md) | Training curriculum for /academy |
| [cooperative-finance.md](references/cooperative-finance.md) | Coop-specific financial analysis |
| [se-finance.md](references/se-finance.md) | SE-specific financial analysis |

---

## Skill Integration Network

| Skill | Relationship | Data Exchange |
|-------|--------------|---------------|
| `/investor` | **THE PERSPECTIVE** | Financial analysis feeds investment decisions |
| `/academy` | Curriculum design | Financial analysis course development |
| `/cooperative` | Context adaptation | Coop financial health assessment |
| `/social-enterprise` | Context adaptation | SE financial sustainability |
| `/lean-canvas` | Business model | Financial projections for canvas |
| `/enterprise-dev` | Operations | Financial analysis for scaling |
| `/featuredev` | Implementation | Financial analysis platform features |

---

## Constraints

- Use authoritative sources (CFA Institute, CFI, Kaplan)
- Adapt for BARMM context (cooperative and SE focus)
- Support both for-profit and social enterprise analysis
- Align with CDA requirements for cooperative financial reporting
- Avoid purple colors in any UI recommendations
- Prioritize practical, Excel-based approaches
- When investment decisions are involved, invoke /investor

---
