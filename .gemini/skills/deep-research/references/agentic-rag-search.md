# Agentic RAG Search Strategy

## Overview

Agentic RAG (Retrieval-Augmented Generation) goes beyond basic "search and summarize" by having the agent actively manage its retrieval strategy — decomposing intent, rewriting queries, selecting tools at different granularities, and self-assessing retrieval quality.

**Key insight**: Instructed query generation improves recall by 35-50% over naive keyword search.

## Three-Layer Search Strategy

### Layer 1: Broad Exploration (Discovery)

**Goal**: Map the landscape, identify key sources and terminology.

```
Researcher Instructions:
1. Start with 3-5 broad searches using varied phrasings
2. Extract key terminology, author names, organization names from results
3. Identify the most authoritative source domains
4. Build a "search vocabulary" for deeper queries
```

**Query Patterns:**
- `"[topic] comprehensive guide [year]"`
- `"[topic] best practices framework"`
- `"[industry] standards requirements [topic]"`
- `"[topic] state of the art review"`

### Layer 2: Targeted Deep Dive (Extraction)

**Goal**: Extract specific facts, data points, and evidence from identified sources.

```
Researcher Instructions:
1. Use terminology discovered in Layer 1
2. Target specific source domains identified as authoritative
3. Fetch full pages from the most relevant URLs
4. Extract: definitions, statistics, requirements, quotes with context
```

**Query Patterns:**
- `site:[authoritative-domain] "[specific term]"`
- `"[author name]" "[topic]" [year]`
- `"[specific requirement]" "[regulatory body]"`
- `"[topic]" filetype:pdf [year]`

### Layer 3: Verification & Gap-Filling (Validation)

**Goal**: Verify claims, fill gaps, resolve contradictions.

```
Researcher Instructions:
1. Search specifically for claims that need verification
2. Look for alternative perspectives on contested claims
3. Fill gaps identified during synthesis
4. Verify dates, numbers, and names against primary sources
```

**Query Patterns:**
- `"[specific claim]" -site:[original-source]` (verify elsewhere)
- `"[topic]" criticism OR limitations OR challenges`
- `"[statistic]" source OR origin OR study`

## Adaptive Query Rewriting

When initial searches return poor results, rewrite systematically:

| Problem | Rewrite Strategy | Example |
|---------|-----------------|---------|
| Too few results | Broaden terms, remove qualifiers | "BARMM cooperative compliance 2024" → "Philippine cooperative regulation" |
| Too many irrelevant results | Add specificity, use quotes | cooperative governance → "cooperative board governance" Philippines |
| Wrong domain | Add domain terms | AI research → "AI research" "legislative analysis" government |
| Outdated results | Add recency markers | cooperative law → cooperative law 2024 OR 2025 OR 2026 |
| Paywalled results | Target open sources | [topic] → [topic] site:gov.ph OR site:org OR site:edu |

## Multi-Granularity Retrieval

Design retrieval at different levels of detail:

| Granularity | Tool | When to Use |
|-------------|------|-------------|
| **Overview** | WebSearch (titles/snippets) | Initial landscape mapping |
| **Summary** | WebFetch (first 2-3 sections) | Evaluating source relevance |
| **Full Detail** | WebFetch (complete page) | Extracting specific data |
| **Cross-Reference** | Multiple WebFetch | Verifying claims across sources |

## Source Prioritization

### Authority Hierarchy

```
Tier 1: Primary Sources
├── Official government documents, laws, regulations
├── Peer-reviewed academic papers
└── Official organizational publications

Tier 2: Authoritative Secondary
├── Established news outlets
├── Industry reports (McKinsey, Gartner, etc.)
└── Expert blogs from recognized practitioners

Tier 3: General
├── Wikipedia (use for overview, verify claims elsewhere)
├── Forum discussions (Stack Overflow, Reddit)
└── Blog posts from unknown authors
```

### Source Verification Checklist

Before citing any source, verify:
- [ ] Author/organization is identifiable
- [ ] Publication date is recent enough for the claim
- [ ] URL is from a recognized domain
- [ ] Claims are specific (not vague generalizations)
- [ ] Data has methodology described or referenced

### Red Flags (Do Not Cite)

- No identifiable author or organization
- No publication date
- Content marketing disguised as research
- Circular citations (source cites another source that cites it back)
- Statistics without methodology or sample size

## Minimum Query Requirements

| Research Type | Broad Searches | Targeted Searches | Verification Searches |
|--------------|----------------|-------------------|----------------------|
| Quick reference | 3-5 | 3-5 | 2-3 |
| Standard research | 5-10 | 5-10 | 5-7 |
| Comprehensive | 10-15 | 10-15 | 10+ |

## Search Quality Self-Assessment

After each search round, the researcher should assess:

1. **Coverage**: Have all research questions been addressed?
2. **Diversity**: Are sources from multiple perspectives?
3. **Authority**: Are primary/official sources included?
4. **Recency**: Is the most current information captured?
5. **Gaps**: What questions remain unanswered?

If any score is low, initiate additional targeted searches before reporting back.
