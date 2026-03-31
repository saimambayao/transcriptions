# Research Capability - Academy Skill

## Overview

The Academy skill includes research capability to ensure curriculum is current, evidence-based, and aligned with professional standards. This document is the **entry point** for all research activities and determines the appropriate research depth.

## Tools Available

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **WebSearch** | Search the web for information | Finding sources, exploring topics, gathering data |
| **WebFetch** | Fetch and read specific URLs | Deep dive into specific sources, official documents |

---

## Research Decision Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                 RESEARCH DECISION FLOW                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  START: Research task received                                  │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────────────────────────────────┐                   │
│  │ Is this a NEW course or workshop?       │                   │
│  └────────────────┬────────────────────────┘                   │
│                   │                                             │
│         ┌────────┴────────┐                                    │
│         │                 │                                     │
│        YES               NO                                     │
│         │                 │                                     │
│         ▼                 ▼                                     │
│  ┌─────────────┐  ┌─────────────────────────┐                  │
│  │    DEEP     │  │ Check other triggers... │                  │
│  │  RESEARCH   │  └───────────┬─────────────┘                  │
│  │ (mandatory) │              │                                 │
│  └─────────────┘              ▼                                 │
│         │          ┌───────────────────────┐                   │
│         │          │ Unfamiliar topic?     │──YES──▶ DEEP      │
│         │          │ Regulatory/compliance?│──YES──▶ DEEP      │
│         │          │ Certification-based?  │──YES──▶ DEEP      │
│         │          │ High-stakes training? │──YES──▶ DEEP      │
│         │          │ External audiences?   │──YES──▶ DEEP      │
│         │          └───────────┬───────────┘                   │
│         │                     NO                                │
│         │                      │                                │
│         │                      ▼                                │
│         │          ┌───────────────────────┐                   │
│         │          │ Content refresh?      │──YES──▶ STANDARD  │
│         │          │ Minor additions?      │──YES──▶ STANDARD  │
│         │          └───────────┬───────────┘                   │
│         │                     NO                                │
│         │                      │                                │
│         │                      ▼                                │
│         │          ┌───────────────────────┐                   │
│         │          │ Fact verification?    │──YES──▶ QUICK     │
│         │          │ Minor update?         │──YES──▶ QUICK     │
│         │          └───────────────────────┘                   │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────────────────────────────────┐                   │
│  │ DEEP: Invoke deep-research.md           │                   │
│  │ STANDARD: Use Standard workflow below   │                   │
│  │ QUICK: Use Quick workflow below         │                   │
│  └─────────────────────────────────────────┘                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Research Depth Levels

| Level | Effort | When to Use | Reference |
|-------|--------|-------------|-----------|
| **Deep** | 10+ searches, 5+ fetches | New courses/workshops, unfamiliar topics, compliance | [deep-research.md](deep-research.md) |
| **Standard** | 5-7 searches, 2-3 fetches | Content refresh, familiar domain additions | Below |
| **Quick** | 2-3 searches | Fact verification, minor updates | Below |

**IMPORTANT**: All research outputs must follow the [Citation Standards](deep-research.md#citation-standards-footnote-methodology) using inline footnotes and a Works Cited list.

---

## Deep Research Trigger

**Invoke [deep-research.md](deep-research.md) when ANY of these apply:**

| Trigger | Why Deep Research |
|---------|-------------------|
| New course or workshop | Need comprehensive subject matter expertise |
| Unfamiliar topic/domain | Must build foundational knowledge |
| Regulatory/compliance requirements | Must find all official guidelines |
| Certification-based training | Must ensure accuracy of requirements |
| High-stakes training (legal, financial, safety) | Errors have serious consequences |
| Content for external audiences | Quality and accuracy critical |

---

## Standard Research Workflow

Use when refreshing existing content or making moderate additions to familiar domains.

**Effort**: 5-7 WebSearch queries + 2-3 WebFetch deep dives

```
1. DEFINE SCOPE (2-3 questions)
   ├── What specific information is needed?
   ├── What has changed since last update?
   └── What sources should be checked?

2. SEARCH (5-7 queries)
   ├── "[topic] [specific aspect] [year]"
   ├── "[topic] latest developments"
   ├── "[topic] best practices update"
   └── [Domain-specific queries from library below]

3. VERIFY (2-3 fetches)
   ├── Official source for key claims
   ├── Updated statistics or data
   └── New framework or methodology

4. UPDATE
   ├── Document changes with inline citations [1], [2]
   └── Include Works Cited list
```

**Output**: Update notes with inline citations and Works Cited list

---

## Quick Research Workflow

Use for fact verification, minor updates, or checking specific details.

**Effort**: 2-3 WebSearch queries

```
1. IDENTIFY
   └── What specific fact/detail needs verification?

2. SEARCH (2-3 queries)
   ├── "[specific fact] [authoritative source]"
   └── "[topic] [year] official"

3. VERIFY
   └── Confirm from authoritative source

4. DOCUMENT
   └── Include citation in format: [1] Author. "Title." Source, Year. URL
```

**Output**: Verified fact with formatted citation

---

## Citation Requirements

All research outputs (at any depth level) must include proper source attribution following the **Gemini Deep Research citation approach**.

### Quick Citation Reference

| Element | Format | Example |
|---------|--------|---------|
| **Inline Citation** | [#] after claim | "Cooperatives have 7 principles.[1]" |
| **Multiple Sources** | [#, #] | "Democratic control is fundamental.[1, 2]" |
| **Page Reference** | [#, p. X] | "PEARLS has 44 ratios.[3, p. 12]" |
| **Works Cited Entry** | [#] Author. "Title." Source, Year. URL | See below |

### Works Cited Format

```markdown
## Works Cited

[1] International Co-operative Alliance. "Cooperative Identity."
    ICA, 2024. https://ica.coop/en/cooperatives/cooperative-identity

[2] Cooperative Development Authority. "MC 2015-09: Mandatory Training."
    CDA, 2015. https://cda.gov.ph/issuances/mc-2015-09
```

### Citation Rules Summary

1. **Every factual claim needs a citation** - Facts, statistics, definitions, requirements
2. **Number citations sequentially** - [1], [2], [3] in order of first appearance
3. **Reuse numbers for repeated sources** - Same source = same number
4. **Include URLs** - All sources must have accessible URLs
5. **Prioritize authoritative sources** - Official > Academic > Industry

**Full citation standards**: [deep-research.md#citation-standards-footnote-methodology](deep-research.md#citation-standards-footnote-methodology)

---

## Search Query Library

Use these templates for all research levels.

### Subject Matter

```
"[topic] fundamentals explained"
"[topic] key concepts terminology"
"[topic] comprehensive guide [year]"
"what is [topic] definition"
"[topic] for beginners introduction"
```

### Curriculum & Training

```
"[topic] training curriculum design"
"[topic] course outline structure"
"[topic] learning objectives examples"
"[topic] competency framework"
"how to teach [topic] effectively"
"[topic] workshop activities exercises"
```

### Industry Standards

```
"[industry] training requirements [country/region]"
"[certification] requirements [year]"
"[regulatory body] guidelines [topic]"
"[topic] professional standards"
"[topic] compliance training requirements"
```

### Best Practices

```
"[topic] training best practices"
"effective [topic] teaching methods"
"[topic] adult learning strategies"
"[topic] workshop facilitation tips"
"[topic] training case studies success"
```

### Assessment

```
"[topic] assessment methods"
"[topic] quiz questions examples"
"[topic] competency evaluation"
"[topic] practical assessment rubric"
"measuring [topic] learning outcomes"
```

---

## Domain-Specific Queries

### Cooperative Training

| Topic | Search Queries |
|-------|----------------|
| **Governance** | "cooperative governance training curriculum", "CDA MC 2015-09 requirements", "cooperative board training best practices" |
| **Financial** | "cooperative financial management training", "PEARLS ratio analysis cooperatives", "cooperative treasury management" |
| **Compliance** | "cooperative compliance requirements Philippines", "CDA annual reports requirements", "cooperative audit standards" |
| **Principles** | "ICA cooperative principles training", "Rochdale principles modern application", "cooperative identity values" |

### Social Enterprise

| Topic | Search Queries |
|-------|----------------|
| **Fundamentals** | "social enterprise training curriculum", "social entrepreneurship course outline", "SE business models" |
| **Impact** | "social impact measurement training", "SROI calculation methodology", "B Impact Assessment preparation" |
| **Legal** | "social enterprise legal frameworks", "RA 11232 cooperatives Philippines", "SE registration requirements BARMM" |
| **Sustainability** | "sustainable business model canvas", "triple bottom line training", "social enterprise financial sustainability" |

### Government Training

| Topic | Search Queries |
|-------|----------------|
| **CSW** | "completed staff work training curriculum", "CSW Philippines government", "staff work standards civil service" |
| **Leadership** | "government executive leadership training", "public sector leadership development", "civil service leadership competencies" |
| **M&E** | "results-based monitoring evaluation training", "government M&E framework", "public program evaluation methods" |
| **Planning** | "strategic planning government training", "public sector strategic planning framework", "government planning tools" |

### Business Skills

| Topic | Search Queries |
|-------|----------------|
| **Finance** | "financial literacy training small business", "bookkeeping basics non-accountants", "SME financial management" |
| **Marketing** | "marketing training cooperatives", "digital marketing small enterprises", "social media marketing SMEs" |
| **Operations** | "operations management training SMEs", "quality management small business", "process improvement basics" |
| **Halal** | "halal certification training", "halal business requirements Philippines", "halal compliance BARMM" |

---

## Trusted Source Domains

### Philippine Government & Regulatory (Priority 1)

| Domain | Organization |
|--------|--------------|
| cda.gov.ph | Cooperative Development Authority |
| dti.gov.ph | Department of Trade and Industry |
| csc.gov.ph | Civil Service Commission |
| dbm.gov.ph | Department of Budget and Management |
| neda.gov.ph | National Economic and Development Authority |
| bangsamoro.gov.ph | BARMM Government |
| lawphil.net | Philippine Laws |

### International Organizations (Priority 2)

| Domain | Organization |
|--------|--------------|
| ica.coop | International Cooperative Alliance |
| ilo.org | International Labour Organization |
| undp.org | UN Development Programme |
| worldbank.org | World Bank |
| adb.org | Asian Development Bank |

### Academic & Professional (Priority 3)

| Domain | Type |
|--------|------|
| *.edu, *.edu.ph | Universities |
| researchgate.net | Academic papers |
| jstor.org | Academic journals |
| scholar.google.com | Academic search |

### Training & Development (Priority 4)

| Domain | Organization |
|--------|--------------|
| hbr.org | Harvard Business Review |
| mckinsey.com | Management consulting |
| atd.org | Association for Talent Development |
| shrm.org | HR/Training standards |

---

## Quick Reference

### Decision Summary

| Scenario | Research Level | Action |
|----------|----------------|--------|
| New course/workshop | **Deep** | → [deep-research.md](deep-research.md) |
| Unfamiliar topic | **Deep** | → [deep-research.md](deep-research.md) |
| Compliance/regulatory | **Deep** | → [deep-research.md](deep-research.md) |
| Content refresh | **Standard** | Use Standard workflow above |
| Fact verification | **Quick** | Use Quick workflow above |

### Minimum Effort by Level

| Level | WebSearch | WebFetch | Output |
|-------|-----------|----------|--------|
| **Deep** | 10+ | 5+ | Research Brief with Works Cited |
| **Standard** | 5-7 | 2-3 | Update Notes with Citations |
| **Quick** | 2-3 | 0-1 | Verified Fact with Citation |

### Citation Quick Reference

| Element | Format |
|---------|--------|
| Inline | `claim.[1]` or `claim.[1, 2]` |
| Page Ref | `claim.[1, p. 5]` |
| Works Cited | `[1] Author. "Title." Source, Year. URL` |

**Full standards**: [deep-research.md#citation-standards-footnote-methodology](deep-research.md#citation-standards-footnote-methodology)
