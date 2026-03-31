# Domain-Specific Search Query Templates

## Policy Research

```
"[policy topic]" Philippines regulation [year]
"[agency name]" "[policy topic]" implementing rules
site:gov.ph "[policy topic]" memorandum circular
"[Republic Act number]" implementing rules regulations IRR
"[policy topic]" BARMM OR Bangsamoro OR "Bangsamoro Transition Authority"
"[policy topic]" "policy brief" OR "policy paper" Philippines [year]
"[policy topic]" comparative analysis ASEAN OR "Southeast Asia"
```

## Technology Evaluation

```
"[technology]" vs "[alternative]" comparison [year]
"[technology]" benchmark performance [year]
"[technology]" production deployment case study
"[technology]" limitations OR drawbacks OR challenges
site:github.com "[technology]" stars:>1000
"[technology]" official documentation getting started
"[technology]" architecture best practices [year]
"[technology]" scalability OR "high availability" enterprise
```

## Legal and Regulatory

```
"[law name]" full text OR verbatim Philippines
"Republic Act No. [number]" "[specific section]"
site:officialgazette.gov.ph "[law name]"
site:lawphil.net "[law name]" OR "[RA number]"
"[regulatory body]" circular OR advisory OR order [year]
"[legal topic]" Supreme Court decision Philippines
"Bangsamoro Autonomy Act" "[topic]" BTA Parliament
"[law name]" amendment OR repeal OR effectivity
```

## Market Research

```
"[industry]" market size Philippines [year]
"[industry]" growth rate forecast [year]-[year]
"[company/sector]" annual report Philippines [year]
"[industry]" competitive landscape Philippines
site:psa.gov.ph "[industry]" statistics [year]
"[industry]" SWOT analysis Philippines OR BARMM
"[product/service]" adoption rate Philippines
"[industry]" investment opportunities Mindanao OR BARMM
```

## Academic Research

```
"[topic]" systematic review OR meta-analysis [year]
"[topic]" peer-reviewed journal Philippines
site:scholar.google.com "[topic]" "[key author]"
"[topic]" framework OR methodology OR model
"[topic]" empirical study OR case study Philippines
"[topic]" literature review [year range]
"[topic]" filetype:pdf [university name]
```

## Philippine / BARMM-Specific

```
site:bangsamoro.gov.ph "[topic]"
site:bta.gov.ph "[topic]" resolution OR bill
site:cda.gov.ph "[topic]" cooperative
site:dict.gov.ph "[topic]" digital OR technology
site:psa.gov.ph BARMM "[topic]" [year]
"Bangsamoro Development Plan" "[topic]"
"[BARMM ministry name]" "[topic]" report OR plan
```

## Query Rewriting Strategies

When initial queries fail, rewrite systematically:

| Problem | Strategy | Before | After |
|---------|----------|--------|-------|
| Zero results | Remove qualifiers, broaden scope | "BARMM cooperative compliance 2024" | "Philippine cooperative regulation" |
| Irrelevant results | Add quotes, domain terms | cooperative governance | "cooperative board governance" Philippines |
| Outdated results | Add recency markers | cooperative law Philippines | cooperative law Philippines 2025 OR 2026 |
| Paywalled sources | Target open-access domains | [topic] research paper | [topic] site:gov.ph OR site:edu.ph OR site:org |
| Wrong geographic scope | Add location qualifiers | cooperative best practices | cooperative best practices Philippines OR ASEAN |
| Too academic | Target practitioner sources | [topic] theoretical framework | [topic] implementation guide OR handbook |
| Too shallow | Target deep sources | [topic] overview | [topic] filetype:pdf comprehensive OR detailed |

## Query Composition Rules

1. **Start broad, then narrow** — Layer 1 queries use general terms; Layer 2 uses vocabulary discovered in Layer 1
2. **Use exact phrases** — Wrap multi-word concepts in quotes: `"fiscal autonomy"` not `fiscal autonomy`
3. **Combine with operators** — Use `OR` for alternatives, `-site:` for exclusions, `site:` for targeting
4. **Include year markers** — Add `[year]` or `[year] OR [year-1]` for current topics
5. **Vary phrasings** — Search the same concept 2-3 ways to catch different terminology
