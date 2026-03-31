# Financial Analysis Frameworks

## Table of Contents
- [Financial Statement Analysis](#financial-statement-analysis)
- [Ratio Analysis Framework](#ratio-analysis-framework)
- [DuPont Analysis](#dupont-analysis)
- [Common-Size Analysis](#common-size-analysis)
- [Trend Analysis](#trend-analysis)

---

## Financial Statement Analysis

### The Three Core Statements

| Statement | Purpose | Key Components |
|-----------|---------|----------------|
| **Income Statement** | Profitability over period | Revenue, Expenses, Net Income |
| **Balance Sheet** | Financial position at point | Assets, Liabilities, Equity |
| **Cash Flow Statement** | Cash movements over period | Operating, Investing, Financing |

### Interrelationship of Statements

```text
STATEMENT CONNECTIONS:
│
├── Net Income (Income Statement)
│   └── → Retained Earnings (Balance Sheet)
│   └── → Starting point for Operating CF (Cash Flow)
│
├── Cash (Cash Flow Statement ending balance)
│   └── → Cash on Balance Sheet
│
└── D&A (Income Statement)
    └── → Accumulated Depreciation (Balance Sheet)
    └── → Add-back in Operating CF (Cash Flow)
```

---

## Ratio Analysis Framework

### Liquidity Ratios

**Purpose:** Assess ability to meet short-term obligations.

| Ratio | Formula | Interpretation |
|-------|---------|----------------|
| **Current Ratio** | Current Assets / Current Liabilities | >1 can cover short-term obligations; 1.5-2 generally healthy |
| **Quick Ratio** | (CA - Inventory) / CL | Stricter test; >1 indicates good liquidity |
| **Cash Ratio** | Cash / Current Liabilities | Most conservative; ability to pay with cash only |
| **Defensive Interval** | (Cash + Receivables + Marketable Securities) / Daily Cash Expenditures | Days company can operate without new cash |

### Activity Ratios

**Purpose:** Measure operational efficiency.

| Ratio | Formula | Interpretation |
|-------|---------|----------------|
| **Inventory Turnover** | COGS / Average Inventory | Higher = faster inventory movement |
| **Days Inventory Outstanding** | 365 / Inventory Turnover | Days to sell inventory |
| **Receivables Turnover** | Revenue / Average AR | Higher = faster collection |
| **Days Sales Outstanding** | 365 / Receivables Turnover | Days to collect receivables |
| **Payables Turnover** | COGS / Average AP | Higher = faster payment to suppliers |
| **Days Payables Outstanding** | 365 / Payables Turnover | Days to pay suppliers |
| **Asset Turnover** | Revenue / Average Total Assets | Revenue generated per asset dollar |
| **Fixed Asset Turnover** | Revenue / Average Fixed Assets | Efficiency of fixed asset use |

### Cash Conversion Cycle

```text
CCC = DIO + DSO - DPO

Days Inventory Outstanding (DIO)
+ Days Sales Outstanding (DSO)
- Days Payables Outstanding (DPO)
= Cash Conversion Cycle

Lower CCC = Better working capital efficiency
Negative CCC = Company gets paid before paying suppliers
```

### Profitability Ratios

**Purpose:** Evaluate earnings generation.

| Ratio | Formula | Interpretation |
|-------|---------|----------------|
| **Gross Margin** | Gross Profit / Revenue | Production profitability |
| **Operating Margin** | Operating Income / Revenue | Core business profitability |
| **Net Profit Margin** | Net Income / Revenue | Bottom-line profitability |
| **EBITDA Margin** | EBITDA / Revenue | Cash operating profitability |
| **ROA** | Net Income / Average Total Assets | Return on assets |
| **ROE** | Net Income / Average Equity | Return to shareholders |
| **ROIC** | NOPAT / Invested Capital | Return on all capital |

### Solvency Ratios

**Purpose:** Assess long-term debt capacity.

| Ratio | Formula | Interpretation |
|-------|---------|----------------|
| **Debt-to-Equity** | Total Debt / Total Equity | Leverage level; higher = more levered |
| **Debt-to-Capital** | Total Debt / (Debt + Equity) | Debt as % of total capital |
| **Debt-to-Assets** | Total Debt / Total Assets | Portion of assets funded by debt |
| **Interest Coverage** | EBIT / Interest Expense | Ability to pay interest; >3 generally safe |
| **Fixed Charge Coverage** | (EBIT + Lease) / (Interest + Lease) | Broader obligation coverage |

### Valuation Ratios

**Purpose:** Assess market value relative to fundamentals.

| Ratio | Formula | Interpretation |
|-------|---------|----------------|
| **P/E** | Price / EPS | Price per earnings dollar |
| **P/B** | Price / Book Value per Share | Price vs. accounting value |
| **P/S** | Price / Revenue per Share | Price vs. sales |
| **EV/Revenue** | Enterprise Value / Revenue | Total value vs. sales |
| **EV/EBITDA** | Enterprise Value / EBITDA | Total value vs. cash earnings |

---

## DuPont Analysis

### 3-Step DuPont Model

```text
ROE = Net Profit Margin × Asset Turnover × Equity Multiplier

        Net Income        Revenue          Total Assets
ROE = ─────────────── × ─────────────── × ───────────────
          Revenue        Total Assets    Shareholders' Equity

      (Profitability)   (Efficiency)      (Leverage)
```

### 5-Step DuPont Model

```text
ROE = Tax Burden × Interest Burden × EBIT Margin × Asset Turnover × Leverage

        Net Income     EBT        EBIT       Revenue      Total Assets
ROE = ─────────── × ────── × ────────── × ────────── × ─────────────
          EBT        EBIT     Revenue    Total Assets    Equity
```

### Interpreting DuPont Components

| Component | What It Measures | Improvement Levers |
|-----------|------------------|-------------------|
| **Net Profit Margin** | Cost management | Price, cost control |
| **Asset Turnover** | Asset efficiency | Sales growth, asset optimization |
| **Equity Multiplier** | Financial leverage | Debt usage |
| **Tax Burden** | Tax efficiency | Tax planning |
| **Interest Burden** | Interest impact | Debt cost management |

---

## Common-Size Analysis

### Vertical Common-Size

**Income Statement:** Express all items as % of Revenue
**Balance Sheet:** Express all items as % of Total Assets

```text
EXAMPLE - VERTICAL ANALYSIS:
│
├── Revenue               100.0%
├── COGS                   65.0%
├── Gross Profit           35.0%
├── Operating Expenses     20.0%
├── Operating Income       15.0%
├── Interest Expense        2.0%
├── Pre-tax Income         13.0%
├── Taxes                   3.0%
└── Net Income             10.0%
```

### Horizontal Common-Size

Express all items as % of base year (or year-over-year change).

```text
EXAMPLE - HORIZONTAL ANALYSIS:
                     Year 1    Year 2    Year 3
Revenue               100%      115%      132%
Gross Profit          100%      112%      125%
Net Income            100%      105%      118%
```

---

## Trend Analysis

### Key Trends to Track

| Metric | What to Look For |
|--------|-----------------|
| **Revenue** | Growth rate, consistency, seasonality |
| **Margins** | Expansion/contraction, sustainability |
| **Working Capital** | Cash conversion, efficiency trends |
| **Leverage** | Debt accumulation, coverage trends |
| **Returns** | ROE/ROA trends, improvement/decline |

### Trend Analysis Process

```text
TREND ANALYSIS STEPS:
│
├── 1. GATHER DATA
│   ├── 3-5 years historical
│   └── Ensure comparability (adjustments)
│
├── 2. CALCULATE METRICS
│   ├── Key ratios for each period
│   └── Growth rates year-over-year
│
├── 3. IDENTIFY PATTERNS
│   ├── Improving vs. declining
│   ├── Consistent vs. volatile
│   └── Cyclical vs. secular
│
├── 4. COMPARE TO BENCHMARKS
│   ├── Industry averages
│   ├── Competitor performance
│   └── Historical company norms
│
└── 5. DRAW CONCLUSIONS
    ├── Explain the drivers
    ├── Assess sustainability
    └── Project future direction
```

---

*Based on: CFA Institute, 365 Careers, Corporate Finance Institute*
