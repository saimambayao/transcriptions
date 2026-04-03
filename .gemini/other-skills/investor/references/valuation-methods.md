# Valuation Methods

## Table of Contents
- [Overview of Valuation Methods](#overview-of-valuation-methods)
- [Discounted Cash Flow (DCF)](#discounted-cash-flow-dcf)
- [Comparable Company Analysis](#comparable-company-analysis)
- [Precedent Transaction Analysis](#precedent-transaction-analysis)
- [LBO Analysis](#lbo-analysis)
- [Choosing the Right Method](#choosing-the-right-method)

---

## Overview of Valuation Methods

### The Four Core Methods

| Method | Type | Basis | Typical Use |
|--------|------|-------|-------------|
| **DCF** | Intrinsic | Future cash flows | Strategic decisions |
| **Comparables** | Relative | Public market multiples | Quick market reference |
| **Precedent Transactions** | Relative | Historical deal multiples | M&A negotiations |
| **LBO** | Return-based | PE fund economics | PE floor price |

### Typical Valuation Ranking

```text
VALUATION OUTPUT RANKING (Highest to Lowest):

1. PRECEDENT TRANSACTIONS (Highest)
   └── Includes control premium (20-40%)

2. DCF (Medium-High)
   └── Reflects intrinsic value expectations

3. COMPARABLE COMPANIES (Medium)
   └── Market value without control

4. LBO (Lowest)
   └── Floor price based on PE returns
```

---

## Discounted Cash Flow (DCF)

### Core Concept

The value of a company equals the present value of its future free cash flows, discounted at a rate reflecting the time value of money and risk.

### DCF Formula

```text
Enterprise Value = Σ FCF_t / (1 + WACC)^t + Terminal Value / (1 + WACC)^n

Where:
- FCF = Free Cash Flow
- WACC = Weighted Average Cost of Capital
- n = Number of forecast years
- Terminal Value = Value beyond forecast period
```

### Free Cash Flow Calculation

```text
FREE CASH FLOW (FCFF):
│
├── EBIT
├── × (1 - Tax Rate)
├── = NOPAT (Net Operating Profit After Tax)
├── + Depreciation & Amortization
├── - Capital Expenditures
├── - Change in Net Working Capital
└── = Free Cash Flow to Firm
```

### WACC Calculation

```text
WACC = (E/V) × Re + (D/V) × Rd × (1 - T)

Where:
- E = Market value of equity
- D = Market value of debt
- V = E + D (total value)
- Re = Cost of equity
- Rd = Cost of debt
- T = Tax rate
```

### Cost of Equity (CAPM)

```text
Re = Rf + β × (Rm - Rf)

Where:
- Rf = Risk-free rate
- β = Beta (systematic risk)
- Rm = Expected market return
- (Rm - Rf) = Equity risk premium
```

### Terminal Value Methods

| Method | Formula | When to Use |
|--------|---------|-------------|
| **Perpetuity Growth** | FCF_n × (1+g) / (WACC - g) | Stable, growing businesses |
| **Exit Multiple** | EBITDA_n × Multiple | When comparable exits exist |

### DCF Sensitivities

Key variables that significantly impact DCF value:
- WACC (±1% can change value by 15-25%)
- Terminal growth rate
- Revenue growth assumptions
- Margin assumptions

---

## Comparable Company Analysis

### Process Overview

```text
COMPARABLE COMPANY ANALYSIS STEPS:
│
├── 1. SELECT COMPARABLE COMPANIES
│   ├── Same industry/sector
│   ├── Similar size (revenue, market cap)
│   ├── Similar growth profile
│   └── Similar business model
│
├── 2. GATHER FINANCIAL DATA
│   ├── Market capitalization
│   ├── Enterprise value
│   ├── Revenue, EBITDA, Net Income
│   └── Growth rates
│
├── 3. CALCULATE MULTIPLES
│   ├── EV/Revenue
│   ├── EV/EBITDA
│   ├── P/E
│   └── Other relevant metrics
│
├── 4. DETERMINE TRADING RANGE
│   ├── Low (25th percentile)
│   ├── Median
│   ├── Mean
│   └── High (75th percentile)
│
└── 5. APPLY TO TARGET
    ├── Target metric × Peer multiple
    └── Derive implied valuation range
```

### Key Valuation Multiples

| Multiple | Formula | Best For |
|----------|---------|----------|
| **EV/Revenue** | EV / Revenue | High-growth, unprofitable |
| **EV/EBITDA** | EV / EBITDA | Most common; cash flow proxy |
| **EV/EBIT** | EV / EBIT | Capital-intensive businesses |
| **P/E** | Price / EPS | Profitable companies |
| **P/B** | Price / Book Value | Asset-heavy, financials |

### Enterprise Value Calculation

```text
Enterprise Value = Market Cap + Debt - Cash + Preferred + Minority Interest
```

### Adjustment Considerations

When comparing, adjust for:
- Size differences
- Growth rate differences
- Profitability differences
- Geographic differences
- Capital structure differences

---

## Precedent Transaction Analysis

### Core Concept

Value a company based on multiples paid in similar M&A transactions, which typically include a control premium.

### Process Overview

```text
PRECEDENT TRANSACTION ANALYSIS:
│
├── 1. IDENTIFY RELEVANT TRANSACTIONS
│   ├── Same industry
│   ├── Similar size
│   ├── Recent (within 3-5 years)
│   └── Similar deal dynamics
│
├── 2. GATHER TRANSACTION DATA
│   ├── Purchase price
│   ├── Target financials at deal time
│   └── Deal terms and structure
│
├── 3. CALCULATE TRANSACTION MULTIPLES
│   ├── EV/Revenue
│   ├── EV/EBITDA
│   └── Premium to unaffected price
│
├── 4. DETERMINE RANGE
│   ├── Low, median, high
│   └── Adjust for market conditions
│
└── 5. APPLY TO TARGET
    ├── Target metric × Transaction multiple
    └── Derive implied valuation range
```

### Control Premium

```text
Control Premium = (Acquisition Price - Unaffected Market Price) / Unaffected Market Price

Typical range: 20-40%
Reflects: Value of controlling the company
```

### Data Sources

- CapitalIQ, Bloomberg, PitchBook
- SEC filings (merger proxies)
- Company announcements
- Industry databases

---

## LBO Analysis

### Core Concept

Determine the maximum price a financial sponsor can pay while achieving target returns (typically 20%+ IRR).

### LBO Value Drivers

```text
LBO RETURN DRIVERS:
│
├── ENTRY MULTIPLE
│   └── Lower entry = higher returns
│
├── EBITDA GROWTH
│   ├── Revenue growth
│   └── Margin expansion
│
├── DEBT PAYDOWN
│   └── Reduces equity needed at exit
│
├── MULTIPLE EXPANSION
│   └── Higher exit multiple than entry
│
└── EXIT MULTIPLE
    └── Higher exit = higher returns
```

### LBO Model Structure

```text
LBO MODEL FRAMEWORK:
│
├── SOURCES & USES
│   ├── Uses: Purchase price, fees, cash to B/S
│   └── Sources: Debt tranches, sponsor equity
│
├── OPERATING MODEL
│   ├── Revenue projections
│   ├── EBITDA projections
│   └── Free cash flow
│
├── DEBT SCHEDULE
│   ├── Mandatory amortization
│   ├── Cash sweep
│   └── Interest expense
│
└── RETURNS ANALYSIS
    ├── Exit enterprise value
    ├── Less: Exit debt
    ├── = Exit equity value
    └── IRR and MoM calculation
```

### Return Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| **IRR** | Internal Rate of Return | 20-25%+ |
| **MoM** | Exit Equity / Entry Equity | 2.0-3.0x |
| **Cash-on-Cash** | Total Distributions / Equity Invested | 2.5x+ |

### Debt Structures

| Tranche | Typical Terms | Purpose |
|---------|--------------|---------|
| **Revolver** | Floating, 5 years | Working capital |
| **Term Loan A** | Floating, 5-7 years | Senior debt |
| **Term Loan B** | Floating, 7 years | Institutional debt |
| **High Yield** | Fixed, 7-10 years | Unsecured debt |
| **Mezzanine** | 15%+, warrants | Subordinated capital |

---

## Choosing the Right Method

### Method Selection Guide

| Situation | Primary Method | Secondary |
|-----------|---------------|-----------|
| **Stable, profitable** | DCF | Comparables |
| **High-growth, no profit** | Comparables (Revenue) | DCF (with assumptions) |
| **M&A valuation** | Precedent, DCF | Comparables |
| **PE acquisition** | LBO | DCF, Precedent |
| **IPO pricing** | Comparables | DCF |
| **Distressed** | Asset-based | LBO |

### Football Field Presentation

```text
VALUATION SUMMARY (Football Field):

              $50M         $75M         $100M        $125M
                │            │             │            │
DCF             ├────────────────────────────────┤
                         $65M - $95M

Comparables          ├────────────────────┤
                      $70M - $85M

Precedent                    ├────────────────────────┤
                              $85M - $110M

LBO              ├──────────────┤
                  $55M - $70M
```

---

*Based on: 365 Careers, Wall Street Prep, Street of Walls, CFI*


---

# Core Frameworks (from SKILL.md)

## Core Frameworks

### Discounted Cash Flow (DCF)

**Formula:**

```text
Enterprise Value = Σ FCF_t / (1 + WACC)^t + Terminal Value / (1 + WACC)^n
```

**Key Components:**

| Component | Description | How to Calculate |
|-----------|-------------|------------------|
| **Free Cash Flow** | Cash available to all capital providers | EBIT(1-t) + D&A - CapEx - ΔNWC |
| **WACC** | Weighted average cost of capital | E/(E+D) × Re + D/(E+D) × Rd × (1-t) |
| **Terminal Value** | Value beyond forecast period | FCF_n × (1+g) / (WACC - g) |

### Comparable Company Analysis

**Process:**

```text
COMPARABLE ANALYSIS STEPS:
│
├── 1. SELECT COMPARABLES
│   ├── Same industry
│   ├── Similar size
│   ├── Similar growth profile
│   └── Similar business model
│
├── 2. CALCULATE MULTIPLES
│   ├── EV/Revenue
│   ├── EV/EBITDA
│   ├── P/E
│   └── Other relevant multiples
│
├── 3. APPLY MULTIPLES
│   ├── Take median/mean of comps
│   ├── Apply to target metrics
│   └── Adjust for differences
│
└── 4. DERIVE VALUATION RANGE
    ├── Low (25th percentile)
    ├── Mid (median)
    └── High (75th percentile)
```

### LBO Analysis

**Key Drivers:**

| Driver | Impact on Returns |
|--------|------------------|
| **Entry Multiple** | Lower entry = higher returns |
| **Exit Multiple** | Higher exit = higher returns |
| **Leverage** | More debt = higher equity returns (and risk) |
| **Revenue Growth** | Drives EBITDA growth |
| **Margin Expansion** | Increases cash flow |
| **Debt Paydown** | Increases equity value |

---


---

# Capital Markets Mode (from SKILL.md)

### Mode 4: Capital Markets

For capital raising advisory.

#### Capital Raising Options

| Type | Description | Best For |
|------|-------------|----------|
| **IPO** | Initial public offering | Large, mature companies |
| **Private Placement** | Private equity/debt | Growth companies |
| **Debt Issuance** | Bonds, loans | Asset-backed, stable CF |
| **Convertible** | Debt with equity option | Growth with downside protection |
| **SPAC** | Special purpose acquisition | Quick public path |

#### Capital Raising Process

```text
CAPITAL RAISING STAGES:
│
├── 1. PREPARATION
│   ├── Prepare management presentation
│   ├── Financial projections (→ /financial-analyst)
│   ├── Due diligence preparation
│   └── Valuation analysis
│
├── 2. MARKETING
│   ├── Identify potential investors
│   ├── Roadshow and presentations
│   ├── Answer investor questions
│   └── Build book of interest
│
├── 3. PRICING
│   ├── Determine demand
│   ├── Set price/terms
│   └── Allocate to investors
│
└── 4. CLOSING
    ├── Execute documentation
    ├── Fund transfer
    └── Post-closing obligations
```

---
