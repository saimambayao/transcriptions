---
type: reference
---

# Policy Document Types — Routing Guide

Use this guide to choose the correct document type before invoking a skill.

## Comparison Table

| Type | Purpose | Audience | Length | Structure | Skill |
|------|---------|----------|--------|-----------|-------|
| **Policy Brief** | Front-loaded, action-oriented | Busy decision-makers | 2–8 pages | Recommendations first, evidence supporting | `/policy-recommendation` (Tier 1) |
| **Policy Recommendation** | Strategic, principle-based | Government officials, evaluators | 8–15 pages | Full Bardach analytical structure | `/policy-recommendation` (Tier 2) — DEFAULT |
| **Policy Paper** | Rear-loaded, evidence-heavy | Technical specialists, researchers | 20+ pages | Extensive evidence justification before conclusions | `/policy-paper` |
| **Policy Memo** | Internal communication | Intra-agency recipients | 1–2 pages | Abbreviated brief format | `/policy-recommendation` with `"memo"` argument |

---

## Decision Tree — Which Format Should I Use?

**1. Who is the audience?**
- Decision-maker with limited time → Policy Brief or Policy Memo
- Government official needing full analysis → Policy Recommendation (DEFAULT)
- Technical specialist or researcher → Policy Paper

**2. What is the purpose?**
- Drive a decision or action → Policy Brief or Policy Recommendation
- Document knowledge or provide deep evidence → Policy Paper
- Coordinate internally within an agency → Policy Memo

**3. How much time does the reader have?**
- Minutes (executive) → Policy Brief (2–8 pages) or Policy Memo (1–2 pages)
- Hours (analyst, evaluator) → Policy Recommendation (8–15 pages) or Policy Paper (20+ pages)

**4. Is this for internal or external use?**
- Internal (within agency or office) → Policy Memo
- External (legislature, executive, public) → Policy Brief, Policy Recommendation, or Policy Paper

---

## /policy-paper vs /policy-recommendation

Use `/policy-paper` when:
- The audience is academic or technical
- Evidence must be extensively justified before any conclusion is drawn
- The document will be cited as a research reference
- Length of 20+ pages is appropriate and expected

Use `/policy-recommendation` (default) when:
- The audience is a government official or evaluator
- A clear, actionable recommendation is the primary output
- Bardach's Eightfold Path methodology applies
- Length of 8–15 pages is appropriate
- Use `Tier 1` for a shorter brief variant, or pass `"memo"` for intra-agency use
