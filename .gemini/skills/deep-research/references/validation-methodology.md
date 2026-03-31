# Validation Methodology

## Claim Verification Steps

For every factual claim in the research output, apply this verification sequence:

### Step 1: Identify the Claim Type

| Claim Type | Examples | Verification Approach |
|-----------|----------|----------------------|
| **Statistical** | Percentages, counts, monetary figures | Trace to primary data source |
| **Temporal** | Dates, timelines, deadlines | Cross-check 2+ sources with publication dates |
| **Definitional** | Legal definitions, technical terms | Verify against authoritative definition source |
| **Attributive** | "X said...", "According to Y..." | Locate original statement or document |
| **Causal** | "X caused Y", "X led to Z" | Verify mechanism, check for confounding factors |
| **Comparative** | "X is larger than Y", rankings | Verify both values independently |

### Step 2: Locate Primary Source

1. If the claim cites a secondary source, trace backward to the primary source
2. If the primary source is a government document, fetch it directly from `.gov` or `.gov.ph`
3. If the primary source is academic, verify via the journal or institutional repository
4. If no primary source exists, downgrade confidence to `[P]` or `[U]`

### Step 3: Cross-Reference

Verify each major claim against at least 2 independent sources. "Independent" means:
- Different organizations (not one quoting the other)
- Different methodologies (not both using the same dataset)
- Different publication dates (confirms the claim persists over time)

## Source Cross-Referencing Protocol

### Build the Verification Matrix

For each key claim, populate:

```markdown
| Claim | Source A | Source B | Source C | Agreement | Tag |
|-------|---------|---------|---------|-----------|-----|
| [claim] | Confirms (URL) | Confirms (URL) | — | Full | [S] |
| [claim] | States X (URL) | States Y (URL) | — | Conflict | [?] |
| [claim] | Confirms (URL) | — | — | Partial | [P] |
```

### Cross-Reference Rules

- **2+ independent confirmations** = `[S]` (Supported)
- **1 authoritative source only** = `[P]` (Probable)
- **Sources disagree on specifics** = `[?]` (Uncertain) — document both values
- **No source found** = `[U]` (Unsupported) — flag for removal or explicit disclaimer

## Contradiction Detection

### Systematic Scan

After consolidating all researcher outputs:

1. **Group claims by subject** — cluster all claims about the same entity, event, or metric
2. **Compare values within each cluster** — look for numeric, temporal, or qualitative disagreements
3. **Check source authority** — when values conflict, which source has higher authority?
4. **Check source recency** — is the conflict due to temporal change?

### Resolution Decision Tree

```
Sources conflict on a claim
├── Is one source primary and the other secondary?
│   └── YES → Use primary source, note secondary [S]
├── Are sources from different time periods?
│   └── YES → Use most recent authoritative source, note change [S]
├── Do sources use different methodologies?
│   └── YES → Present both with methodology context [?]
├── Is one source significantly more authoritative?
│   └── YES → Use higher-authority source [P]
└── Sources are equally authoritative and current
    └── Present both perspectives, flag for user review [?]
```

## Confidence Tag Assignment Criteria

### [S] SUPPORTED — Use when ALL of these are true:
- 2+ independent authoritative sources confirm the claim
- No credible source contradicts it
- The claim is specific and verifiable (not a vague generalization)
- Sources are reasonably current for the topic

### [P] PROBABLE — Use when ANY of these apply:
- Only 1 authoritative source confirms it, but the source is highly credible
- 2+ sources agree but with minor discrepancies (e.g., "approximately 23%" vs "23.4%")
- The claim is from a strong source but cannot be independently verified

### [?] UNCERTAIN — Use when ANY of these apply:
- 2+ credible sources directly contradict each other
- The only source is non-authoritative or potentially biased
- The claim involves projections, estimates, or contested interpretations
- Evidence is circumstantial rather than direct

### [U] UNSUPPORTED — Use when ANY of these apply:
- No source found despite targeted searching
- The only sources are unreliable (content marketing, anonymous blogs)
- The claim appears to be fabricated or hallucinated
- All available sources explicitly contradict the claim

## Fact-Checking Procedures

### Names and Titles
- Verify spelling of all proper nouns against official sources
- Confirm current titles and positions (people change roles)
- Check organization names have not been renamed or restructured

### Numbers and Statistics
- Trace every statistic to its original dataset or publication
- Verify the year the data was collected (not just published)
- Confirm units, currency, and methodology
- Flag rounded numbers that may obscure precision

### Legislation References
- Verify Republic Act numbers against `officialgazette.gov.ph` or `lawphil.net`
- Confirm BAA numbers against `bta.gov.ph` or parliamentary records
- Check that cited sections and articles actually exist in the law
- Verify effectivity dates and any amendments

### Dates and Timelines
- Cross-check dates against 2+ sources
- Distinguish between announcement date, signing date, and effectivity date
- For historical events, prefer primary sources over secondary accounts
