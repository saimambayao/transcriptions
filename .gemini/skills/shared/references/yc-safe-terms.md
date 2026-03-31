# YC SAFE Investment Terms Reference

> **Primary Use:** `/investor` skill
> **Related Skills:** `/startup`, `/cofounder`

---

## What is a SAFE?

**SAFE = Simple Agreement for Future Equity**

A SAFE is an investment instrument created by Y Combinator in 2013 to simplify early-stage fundraising. It is:

- **Not debt** - No interest, no maturity date
- **Not equity** - No immediate ownership
- **A promise** - Converts to equity in a future priced round

---

## YC Standard Deal (2024)

| Component | Amount | Terms |
|-----------|--------|-------|
| **Initial Investment** | $125,000 | 7% equity (common stock) |
| **MFN SAFE** | $375,000 | Uncapped, Most Favored Nation |
| **Total** | $500,000 | Combined investment per company |

### Why This Structure?

1. **$125K for 7%** = Immediate equity stake for YC
2. **$375K MFN SAFE** = Additional capital without setting valuation cap

---

## SAFE Types

### 1. Valuation Cap SAFE

```
Investor gets: Shares at lower of cap or discount at conversion
Example: $5M cap, company raises at $10M pre → investor converts at $5M
```

**Best For:** Investors who want protection if company becomes very valuable

### 2. Discount SAFE

```
Investor gets: Shares at X% discount to next round price
Example: 20% discount, $10/share round → investor gets shares at $8/share
```

**Best For:** When parties can't agree on cap

### 3. MFN SAFE (Most Favored Nation)

```
Investor gets: Best terms of any future SAFEs before conversion
Example: If founder later offers 15% discount to someone, MFN holders get 15% too
```

**Best For:** Early investors who want protection against later, better deals

### 4. Uncapped SAFE

```
Investor gets: Shares at next round price (no cap, no discount)
Example: Company raises at $10M, investor converts at $10M
```

**Best For:** Very early, very risky bets (founder-friendly)

---

## SAFE Conversion Mechanics

### Conversion Triggers

| Event | What Happens |
|-------|--------------|
| **Equity Financing** | SAFE converts to shares at priced round |
| **Liquidity Event** | SAFE converts to cash or shares at acquisition |
| **Dissolution** | SAFE holder gets money back (if available) |

### Conversion Math

**With Valuation Cap:**
```
Conversion Price = Cap / Post-Money Capitalization
Shares = Investment / Conversion Price

Example:
- SAFE: $100K at $5M cap
- Series A: $20M pre-money, 10M shares
- Conversion price: $5M / 10M = $0.50/share
- Investor gets: $100K / $0.50 = 200,000 shares
```

**With Discount:**
```
Conversion Price = Series A Price × (1 - Discount)
Shares = Investment / Conversion Price

Example:
- SAFE: $100K at 20% discount
- Series A: $1.00/share
- Conversion price: $1.00 × 0.80 = $0.80/share
- Investor gets: $100K / $0.80 = 125,000 shares
```

---

## Pre-Money vs Post-Money SAFEs

### Post-Money SAFE (YC Standard since 2018)

**Key Feature:** Cap includes all SAFEs in ownership calculation

```
If you raise $1M on $10M post-money cap:
- SAFE holders get 10% ($1M / $10M)
- Founders know exactly how much they're giving up
```

**Advantage:** Clear dilution calculation upfront

### Pre-Money SAFE (Original)

**Key Feature:** Cap doesn't include SAFE itself

```
If you raise $1M on $9M pre-money cap:
- Post-money = $10M
- SAFE holders get 10% ($1M / $10M)
- But cap was calculated differently
```

**Issue:** Ambiguous ownership until priced round

---

## SAFE vs Convertible Note

| Feature | SAFE | Convertible Note |
|---------|------|------------------|
| **Interest** | None | Yes (6-8% typical) |
| **Maturity Date** | None | Yes (18-24 months typical) |
| **Repayment** | No | Yes (technically) |
| **Legal Complexity** | Low | Medium |
| **Legal Cost** | $0-500 | $2,000-5,000 |
| **Board Seat** | Never | Sometimes |
| **Conversion** | Next priced round | Same |

**YC Recommendation:** Use SAFEs for seed rounds

---

## SAFE Terms Glossary

| Term | Definition |
|------|------------|
| **Valuation Cap** | Maximum valuation at which SAFE converts |
| **Discount** | Percentage reduction from next round price |
| **Pro Rata Rights** | Right to invest in future rounds to maintain ownership |
| **MFN** | Most Favored Nation - get best terms of any future SAFEs |
| **Conversion Event** | Trigger that converts SAFE to equity |
| **Post-Money Cap** | Cap that includes all SAFEs in calculation |
| **Pre-Money Cap** | Cap that excludes SAFEs from calculation |

---

## Due Diligence Checklist for SAFE Investments

### Founder Evaluation (YC Style)

| Factor | Questions to Ask |
|--------|------------------|
| **Clarity** | Can they explain the idea in one sentence? |
| **Traction** | What's their weekly growth rate? |
| **Domain Expertise** | Why are they uniquely suited to solve this? |
| **Determination** | Have they shown grit in past challenges? |
| **Technical Ability** | Can they build it themselves? |

### Business Evaluation

| Factor | What to Look For |
|--------|------------------|
| **Market Size** | TAM > $1B for venture scale |
| **Growth Rate** | 5-7% weekly is good, 10% is exceptional |
| **Unit Economics** | Path to positive CAC/LTV |
| **Retention** | Users come back without prompting |
| **PMF Signals** | Organic growth, word-of-mouth |

### Terms Evaluation

| Item | Check |
|------|-------|
| **Cap** | Reasonable given traction and market |
| **Discount** | 15-25% is typical |
| **Pro Rata** | Important for doubling down on winners |
| **MFN** | Protection for early investors |
| **Side Letter** | Any special terms? |

---

## Cap Table Impact

### Before SAFE

```
Founder A: 50%
Founder B: 50%
Total: 100%
```

### After $500K SAFE at $5M Post-Money Cap

```
Founder A: 45%
Founder B: 45%
SAFE Holders: 10% (on conversion)
Total: 100%
```

### After Series A ($10M at $40M Pre-Money)

```
Founder A: 36%
Founder B: 36%
SAFE Holders: 8%
Series A: 20%
Total: 100%
```

---

## Red Flags in SAFE Terms

| Red Flag | Why It's Concerning |
|----------|---------------------|
| **Very high cap** | Founders may have unrealistic expectations |
| **No cap, no discount** | Investor taking unnecessary risk |
| **Board seat** | Unusual for SAFEs, could signal control issues |
| **Unusual conversion triggers** | May never convert |
| **Excessive pro rata** | Over-promises to investors |

---

## YC SAFE Documents

Official YC SAFE templates available at: https://ycombinator.com/documents

| Document | Use Case |
|----------|----------|
| **Post-Money SAFE: Valuation Cap** | Standard for most seed rounds |
| **Post-Money SAFE: Discount** | When cap can't be agreed |
| **Post-Money SAFE: MFN** | Very early rounds |

---

## Negotiation Framework

### For Founders

1. **Start with post-money cap** - Know your dilution upfront
2. **Use YC templates** - Investors trust them
3. **Avoid side letters** - Creates cap table complexity
4. **Get legal review** - Even simple docs need lawyer eyes

### For Investors

1. **Pro rata rights** - Essential for doubling down
2. **Information rights** - Regular updates on progress
3. **MFN protection** - If very early
4. **Reasonable cap** - Based on comparable rounds

---

## Sources

- [YC SAFE Documents](https://ycombinator.com/documents)
- [YC Safe Financing Documents](https://ycombinator.com/library/6z-safe-financing-documents)
- [Post-Money SAFE User Guide](https://ycombinator.com/library/6m-safe-user-guide)
- [Startup School: Fundraising Fundamentals](https://startupschool.org)

---

*Reference for SAFE investment evaluation and structuring.*
