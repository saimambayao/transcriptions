# Product Management Frameworks Reference

## RICE Scoring Framework

### Standard RICE
```
RICE Score = (Reach × Impact × Confidence) / Effort
```

| Factor | Scale | Description |
|--------|-------|-------------|
| **Reach** | Number | Users/customers affected per quarter |
| **Impact** | 0.25, 0.5, 1, 2, 3 | Minimal, Low, Medium, High, Massive |
| **Confidence** | 0-100% | How confident in estimates |
| **Effort** | Person-months | Development time required |

### SE-Adapted RICE
```
RICE Score = (Reach × Impact × Confidence × Mission) / Effort
```

| Factor | Scale | SE Consideration |
|--------|-------|------------------|
| **Reach** | 1-10 | Include beneficiaries, not just customers |
| **Impact** | 0.25-3 | Measure outcome improvement |
| **Confidence** | 0.5-1.0 | Evidence from validation |
| **Mission** | 0.5, 1, 1.5 | Low, Medium, High alignment |
| **Effort** | 1-10 | Person-months to build |

---

## MoSCoW Prioritization

| Category | Definition | Decision Criteria |
|----------|------------|-------------------|
| **Must Have** | Essential for launch | Without it, product fails or is unsafe |
| **Should Have** | Important, not critical | Painful without, but workarounds exist |
| **Could Have** | Nice to have | Improves UX, not critical path |
| **Won't Have** | Out of scope this time | Explicitly deferred to future |

### MoSCoW for Social Enterprises

| Category | Business Lens | Impact Lens |
|----------|--------------|-------------|
| **Must** | Core revenue | Core impact delivery |
| **Should** | Revenue enhancement | Impact enhancement |
| **Could** | Competitive edge | Differentiation |
| **Won't** | Future opportunity | Future expansion |

---

## Kano Model

### Feature Categories

| Type | If Present | If Absent | Example |
|------|-----------|-----------|---------|
| **Basic** | Neutral | Dissatisfaction | Safety, reliability |
| **Performance** | Satisfaction | Dissatisfaction | Speed, price |
| **Delighter** | High satisfaction | Neutral | Unexpected features |

### Kano Questionnaire Format

For each feature, ask two questions:
1. **Functional**: "How would you feel if this feature is present?"
2. **Dysfunctional**: "How would you feel if this feature is absent?"

Response options: Like, Expect, Neutral, Tolerate, Dislike

### Kano Evaluation Table

|  | Like | Expect | Neutral | Tolerate | Dislike |
|--|------|--------|---------|----------|---------|
| **Like** | Q | A | A | A | O |
| **Expect** | R | I | I | I | M |
| **Neutral** | R | I | I | I | M |
| **Tolerate** | R | I | I | I | M |
| **Dislike** | R | R | R | R | Q |

Key: M=Must-be, O=One-dimensional, A=Attractive, I=Indifferent, R=Reverse, Q=Questionable

---

## Jobs to Be Done (JTBD)

### Job Statement Format
```
When [situation], I want to [motivation], so I can [expected outcome].
```

### Job Map Structure

1. **Define** - What needs to be accomplished?
2. **Locate** - Where to find inputs?
3. **Prepare** - How to set up?
4. **Confirm** - Is it ready?
5. **Execute** - Do the core task
6. **Monitor** - Track progress
7. **Modify** - Make adjustments
8. **Conclude** - Finish and clean up

### JTBD for Social Enterprises

| Job Level | Business Job | Social Job |
|-----------|-------------|------------|
| **Core** | Generate revenue | Create impact |
| **Related** | Grow customer base | Expand beneficiary reach |
| **Emotional** | Feel successful | Feel purposeful |
| **Social** | Gain recognition | Build community |

---

## Product-Market Fit Indicators

### Sean Ellis Test
> "How would you feel if you could no longer use this product?"
> - Very disappointed: >40% indicates PMF
> - Somewhat disappointed
> - Not disappointed

### Key Metrics for PMF

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Retention** | >40% at 30 days | Cohort analysis |
| **NPS** | >50 | Survey |
| **Organic growth** | >50% of acquisition | Attribution |
| **Usage frequency** | Daily/weekly | Analytics |

### PMF Pyramid (Dan Olsen)

1. Target Customer
2. Underserved Needs
3. Value Proposition
4. Feature Set
5. UX
6. Product-Market Fit

---

## Sources

- Intercom on Product Management
- Marty Cagan, "Inspired"
- Teresa Torres, "Continuous Discovery Habits"
- Ash Maurya, "Running Lean"
- Anthony Ulwick, "Jobs to Be Done"
