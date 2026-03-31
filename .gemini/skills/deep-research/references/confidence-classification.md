# Confidence Classification & Contradiction Detection

## Claim Confidence Classification

Every factual claim in the research output must be classified by confidence level.

### Classification Levels

| Level | Symbol | Definition | Criteria |
|-------|--------|------------|----------|
| **SUPPORTED** | [S] | Claim verified by 2+ independent sources | Multiple authoritative sources agree |
| **PARTIALLY SUPPORTED** | [P] | Claim has some evidence but incomplete | 1 authoritative source OR multiple weak sources |
| **UNSUPPORTED** | [U] | No evidence found to verify | Claim made without supporting sources |
| **UNCERTAIN** | [?] | Conflicting evidence exists | Sources disagree; requires human judgment |

### How to Apply

In the Source Log, mark each claim:

```markdown
## Key Findings

### Topic Area 1
- Government cooperatives increased 23% since 2020 [S][1, 3, 7]
- Training programs reached 5,000 participants [P][2]
- Implementation costs decreased by 40% [?][4 vs 6]
- The program was "highly successful" [U]
```

### When to Escalate

| Classification | Action |
|---------------|--------|
| [S] | Include in report with citations |
| [P] | Include with caveat: "Based on limited evidence..." |
| [U] | Omit OR include with explicit disclaimer |
| [?] | Present both sides, flag for user review |

---

## Contradiction Detection

### Detection Process

During synthesis (Phase 2), systematically check for contradictions:

1. **Extract all factual claims** from researcher outputs
2. **Group claims by topic** (same subject matter)
3. **Compare claims within each group** for consistency
4. **Flag any conflicts** with both sources

### Contradiction Types

| Type | Example | Resolution |
|------|---------|------------|
| **Factual conflict** | Source A: "Founded in 2015" vs Source B: "Founded in 2018" | Check primary source (official records) |
| **Statistical conflict** | Source A: "23% growth" vs Source B: "31% growth" | Check methodology, timeframe, definitions |
| **Interpretive conflict** | Source A: "Program was successful" vs Source B: "Program had limited impact" | Present both perspectives with evidence |
| **Temporal conflict** | Source A (2020): "Policy X in effect" vs Source B (2024): "Policy X repealed" | Use most recent, note the change |

### Resolution Strategies

#### Strategy 1: Primary Source Arbitration
When two sources conflict, defer to the primary/official source:
```
Hierarchy: Law text > Implementing rules > Government reports > Academic papers > News articles
```

#### Strategy 2: Multi-Agent Debate (for Interpretive Conflicts)
When the conflict is about interpretation rather than facts:
1. Present both positions with full evidence
2. Assess strength of evidence for each side
3. Apply probabilistic reasoning (weight by number + authority of supporting sources)
4. If still unresolved, present both views in the final output

#### Strategy 3: Temporal Resolution
When sources from different time periods conflict:
1. Identify the date of each source
2. Determine if the situation changed over time
3. Use most recent authoritative source
4. Note the historical progression if relevant

### Contradiction Report Template

```markdown
## Contradictions Identified

### Contradiction 1: [Topic]
- **Claim A**: [statement] — Source [X], [Year]
- **Claim B**: [statement] — Source [Y], [Year]
- **Resolution**: [Primary source arbitration / Temporal / Unresolved]
- **Action**: [Which claim used in final output and why]

### Contradiction 2: [Topic]
...
```

---

## Cross-Reference Verification Matrix

For key claims, build a verification matrix:

```markdown
| Claim | Source 1 | Source 2 | Source 3 | Confidence |
|-------|----------|----------|----------|------------|
| Population of BARMM: 4.4M | ✓ PSA Census | ✓ BARMM Gov | ✓ World Bank | [S] |
| GDP growth: 7.2% | ✓ NEDA | ✗ PSA (6.8%) | — | [?] |
| Cooperative count: 12,500 | ✓ CDA | — | — | [P] |
```

**Legend:**
- ✓ = Source confirms claim
- ✗ = Source contradicts (note the conflicting value)
- — = Source does not address this claim

---

## Final Output Requirements

Every research brief must include:

1. **Confidence summary** at the top:
   ```markdown
   > **Confidence**: X claims [S], Y claims [P], Z claims [?], W claims [U]
   > **Contradictions**: N identified, M resolved, K flagged for review
   ```

2. **Inline confidence markers** on key claims (see "How to Apply" above)

3. **Contradiction report** section (if any [?] claims exist)

4. **Source diversity note**:
   ```markdown
   > **Sources**: N total | Government: X | Academic: Y | Industry: Z | Other: W
   ```
