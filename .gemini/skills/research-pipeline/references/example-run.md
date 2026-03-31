# Example Run: Cooperative Development Frameworks in BARMM

## Phase 1: Research Prompt Architecture (/prompter)

**User input**: "Research cooperative development in BARMM"

**Structured research brief** (approved by user):

- **Sub-question 1**: What legal frameworks govern cooperative formation and regulation in BARMM under the Bangsamoro Organic Law?
- **Sub-question 2**: How do existing cooperatives in BARMM perform compared to national averages (membership, capitalization, loan default rates)?
- **Sub-question 3**: What Shariah-compliant financing models are being used or proposed for BARMM cooperatives?
- **Sub-question 4**: What capacity gaps prevent cooperative growth in conflict-affected BARMM municipalities?
- **Scope**: BARMM region only, post-BOL (2019-present), exclude Mindanao-wide cooperatives not operating in BARMM
- **Angles**: Legal/regulatory, economic performance, Islamic finance compatibility, post-conflict development
- **Expected output**: Policy brief with actionable recommendations for BARMM Ministry of Trade

## Phase 2: NotebookLM Source Ingestion (FREE)

```bash
notebooklm create "Research: BARMM Cooperative Development"
notebooklm source add "https://www.cda.gov.ph/resources/statistics/cooperative-statistics-2023"
notebooklm source add "https://bangsamoro.gov.ph/news/cooperative-development-program-2024"
notebooklm source add "https://pcw.gov.ph/republic-act-11364-cooperative-code"
notebooklm source add "https://www.adb.org/publications/islamic-finance-cooperatives-mindanao"
notebooklm source add-research "BARMM cooperative development Bangsamoro shariah financing" --mode deep --import-all
# Timeout: 300000ms, foreground only
notebooklm source list   # Verify: 11 sources imported
notebooklm ask "What are the key legal frameworks and performance data for BARMM cooperatives?" > /tmp/nlm-findings.md
notebooklm ask "What contradictions exist between national cooperative regulations and Shariah compliance?" >> /tmp/nlm-findings.md
notebooklm ask "What evidence exists on capacity gaps in conflict-affected municipalities?" >> /tmp/nlm-findings.md
```

## Phase 3: Gap Analysis (Orchestrator)

After reading `/tmp/nlm-findings.md`, the orchestrator identifies:

- **Claims needing verification**: CDA reported 2,847 cooperatives in BARMM as of 2023; 40% default rate claim for micro-lending coops
- **Missing perspectives**: No data from BARMM Ministry of Trade's own cooperative registry; no input from actual cooperative leaders
- **Source recency concern**: ADB Islamic finance report is from 2019 — pre-BOL implementation
- **Planned sub-agent tasks**: 3 parallel validators

## Phase 4: Sub-Agent Validation (Parallel)

**Agent 1 — Claim Verifier**

> **Summary**: CDA 2023 statistics confirm 2,847 registered cooperatives in BARMM (verified). However, the 40% default rate applies only to Lanao del Sur micro-lending coops, not BARMM-wide. National average default rate is 12%; BARMM average is 23%.
>
> **Evidence**: CDA Annual Report 2023, Table 14; BSP Financial Inclusion Survey Q3 2024; PhilDHRRA field assessment Dec 2023.

**Agent 2 — Counter-Argument Finder**

> **Summary**: Several sources argue cooperative models are inappropriate for BARMM's clan-based economic structures. Hadji Murad Foundation (2023) found that 60% of failed BARMM cooperatives collapsed due to clan-faction disputes over leadership, not financial mismanagement. Islamic scholars at MSU-Marawi argue that conventional cooperative interest-based models violate riba prohibitions even when relabeled.
>
> **Evidence**: Hadji Murad Foundation "Cooperatives and Clan Dynamics" working paper 2023; MSU-Marawi Islamic Economics Department position paper 2024; Bangsamoro Development Agency internal review (leaked, reported by MindaNews Jan 2024).

**Agent 3 — Source Authority Checker**

> **Summary**: CDA statistics are authoritative but lag 12-18 months. The ADB Islamic finance report (2019) is outdated — BARMM's Islamic banking framework has changed significantly since BOL implementation. PhilDHRRA field data is current and credible (direct field observations). The Hadji Murad Foundation paper is a gray literature working paper, not peer-reviewed, but the organization has strong BARMM field presence.
>
> **Evidence**: Cross-referenced CDA publication dates; ADB report predates BARMM Executive Order 2021-003 on Islamic finance; PhilDHRRA methodology reviewed.

## Phase 5: Synthesis with Confidence Tags

- **[S]** BARMM has 2,847 registered cooperatives as of CDA 2023 data — verified by CDA Annual Report and cross-referenced with BARMM Ministry records
- **[S]** BARMM cooperative default rates (23%) are nearly double the national average (12%) — confirmed by CDA and BSP data
- **[P]** Clan-faction disputes are the primary driver of cooperative failure in BARMM — supported by Hadji Murad Foundation data but not independently verified by a second study
- **[?]** Shariah-compliant cooperative financing models show 15% higher retention — single ADB source from 2019, pre-BOL; may not reflect current conditions
- **[U]** BARMM Ministry of Trade's cooperative registration system covers all active cooperatives — no evidence found; multiple sources suggest significant informal cooperatives are unregistered

## Phase 6: Final Output

Saved to `~/Vault/research/deep-research/260323-barmm-cooperative-development.md`:

```markdown
---
date: 2026-03-23
tags: [research, deep-research, barmm, cooperatives, islamic-finance]
source: [cda.gov.ph, bangsamoro.gov.ph, adb.org, phildrra.net]
method: research-pipeline (NotebookLM + sub-agent validation)
---

# Research: Cooperative Development Frameworks in BARMM

> **Date**: 2026-03-23 | **Method**: NotebookLM + 3 validators
> **Confidence**: 2 [S], 1 [P], 1 [?], 1 [U]
> **Sources**: 11 analyzed

## Key Findings
- [S] 2,847 registered cooperatives; 23% default rate vs 12% national average
- [P] Clan dynamics, not financial mismanagement, drive most cooperative failures
- [?] Shariah-compliant models may improve retention but evidence is outdated

## Contradictions & Debates
- National cooperative code assumes secular governance; BARMM BOL grants authority over Islamic finance regulation — jurisdictional overlap unresolved
- Conventional interest-based cooperative lending models conflict with riba prohibitions

## Source Assessment
- CDA data: authoritative but 12-18 month lag
- ADB 2019 report: outdated, pre-BOL — use with caution
- Hadji Murad Foundation: credible field presence but gray literature

## Recommendations
- Commission updated Shariah-compliant cooperative financing study (post-BOL data)
- Pilot clan-inclusive governance models in 5 municipalities before scaling
- Establish BARMM cooperative registry independent of CDA to capture informal cooperatives

## Works Cited
[1] CDA. "Cooperative Statistics 2023." cda.gov.ph, 2024.
[2] ADB. "Islamic Finance and Cooperatives in Mindanao." adb.org, 2019.
[3] Hadji Murad Foundation. "Cooperatives and Clan Dynamics." Working Paper, 2023.
[4] BSP. "Financial Inclusion Survey Q3 2024." bsp.gov.ph, 2024.
```

Condensed takeaways saved to `~/Vault/research/260323-barmm-cooperative-development-takeaways.md`.
