---
name: citation
description: Add proper academic and legal citations to any BARMM document. Scans every paragraph for uncited legal references (BOL, BAA, RA, Constitution), data points, frameworks, and verbatim quotes, then adds footnotes using Philippine Manual of Legal Citations (Feliciano 10th Ed.) format. Use this skill whenever the user mentions "add citations", "add footnotes", "cite sources", "citation pass", "reference check", or after writing any chapter or document that references laws, statistics, or borrowed frameworks. Also trigger proactively after /guidebook-writer Phase 3 (DRAFT), after /policy-recommendation drafts, after /legislative-briefer outputs, or any document destined for publication. MUST be used — uncited legal claims in published BARMM documents damage the author's credibility as a governance consultant.
---

# Citation — Legal and Academic Citation Engine for BARMM Documents

Every published BARMM document must properly cite its sources. Uncited legal claims, unattributed frameworks, and unsourced statistics damage credibility. This skill runs a citation pass on any document — scanning every paragraph and adding footnotes where they're missing.

## When to Use

- **After writing any chapter** in /guidebook-writer (Phase 3 post-processing)
- **After drafting** any /policy-recommendation, /legislative-briefer, or /bill-drafter output
- **Before publication** of any document that references laws, statistics, or borrowed methodologies
- **When the user says** "add citations", "cite this", "add footnotes", "reference check"
- **Proactively** — if you see a document with legal references but no footnotes, offer to run this skill

## The Rule

**Every paragraph that makes a factual claim must have a source.** Specifically:

| Claim Type | Requires Footnote? | Example |
|---|---|---|
| Verbatim legal quotation | YES — always | BOL text, BAA provisions, RA sections |
| Legal reference by number | YES — always | "Under BAA 17...", "Art. VII, Sec. 6..." |
| Specific statistic or data point | YES — always | "29.80% poverty incidence", "50,467 positions" |
| Borrowed framework or methodology | YES — first use | ADDRESS IT, STAR method, PPR, SBI |
| General knowledge about BARMM | NO | "BARMM is an autonomous region" |
| Author's original analysis | NO | "This suggests that..." |
| Instructions to the reader | NO | "Review your PDS before submitting" |

## Citation Format — Philippine Manual of Legal Citations (Feliciano 10th Ed.)

### Footnote Syntax (Markdown)

Inline marker: `[^N]` after the claim
Definition at bottom of chapter: `[^N]: Source text here.`

### Citation Templates by Source Type

**Republic Acts:**
```
[^1]: Rep. Act No. 11054, sec. 6, art. VII.
```

**Bangsamoro Autonomy Acts:**
```
[^2]: BAA No. 17, sec. 12.
```

**Philippine Constitution:**
```
[^3]: Const. art. XI, sec. 17.
```

**Bangsamoro Development Plan:**
```
[^4]: 2nd Bangsamoro Development Plan 2023-2028, ch. 4, p. 12.
```

**CSC Issuances:**
```
[^5]: CSC Memorandum Circular No. 14, s. 2018.
```

**Executive Orders:**
```
[^6]: Exec. Order No. 91, s. 2025.
```

**Supreme Court Decisions:**
```
[^7]: Province of Sulu v. Medialdea, G.R. Nos. 242255, 243246, 243693 (Sept. 9, 2024).
```

**Books and Guidebooks:**
```
[^8]: Mambayao, Saidamen R., *Complete Staff Work Guidebook for the Bangsamoro Autonomous Region* (2026), ch. 3.
```

**Feliciano Manual (for citation rules themselves):**
```
[^9]: Feliciano, Myrna S., *Philippine Manual of Legal Citations*, 10th ed. (Quezon City: U.P. Law Complex, 2019), Rule 4.6, p. 19.
```

**Subsequent reference to same source:**
```
[^10]: *Id.*, sec. 25.
[^11]: *Id.* at 19.
```

**Previously cited source (not immediately preceding):**
```
[^12]: Rep. Act No. 11054, *supra* note 1, sec. 10, art. XII.
```

### Data Point Attribution

When a statistic comes from a government report but you can't cite the exact page:
```
[^13]: BDP 2023-2028 Chapter 5 on Governance (data as of November 2022). Note: these figures predate the exclusion of Sulu from BARMM per SC ruling finalized November 2024.
```

When a statistic is widely known but primary source unavailable:
```
[^14]: Philippine Statistics Authority, 2020 Census. Cited in BDP 2023-2028, ch. 3.
```

## Process — The Citation Pass

### Step 1: Scan

Read the target file paragraph by paragraph. For each paragraph, identify:
- Legal references (BOL articles, BAA numbers, RA numbers, constitutional provisions)
- Statistics and data points (percentages, counts, monetary amounts, dates)
- Framework references (ADDRESS IT, STAR, PPR, SBI, SPMS, etc.)
- Verbatim quotes (text in blockquotes or quotation marks attributed to a source)
- Claims about government processes (posting rules, assessment weights, leave credits)

### Step 2: Check Existing Footnotes

If the paragraph already has a footnote covering the claim, skip it. Count existing footnotes to determine the next available number.

### Step 3: Verify Against Local Sources

Before adding a footnote, verify the claim against authoritative local files:

| Source Type | Verify Against |
|---|---|
| BOL articles | `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` or `~/.gemini/skills/bangsamoro/references/bol-key-provisions.md` |
| BAA numbers | `~/Vault/bangsamoro/bangsamoro-laws/index.md` |
| BDP data | `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/` |
| Officials | `~/.gemini/skills/bangsamoro/references/barmm-officials-2025-2026.md` |
| Ministry structure | `~/.gemini/skills/bangsamoro/references/moa-structure.md` |
| Governance data | `~/.gemini/skills/bangsamoro/references/governance-framework.md` |

**If the claim cannot be verified**, add the footnote with a caveat:
```
[^N]: Source unverified. Commonly cited figure; verify against [specific agency] official reports before publication.
```

### Step 4: Add Footnotes

Add `[^N]` inline markers and definitions at the bottom of the file (or bottom of each major section for very long files). Use sequential numbering starting from the next available number.

### Step 5: Report

After completing the pass, output a summary:

```
## Citation Pass Report

**File**: [filename]
**Existing footnotes**: N
**Footnotes added**: N
**Total footnotes**: N

### Added Citations
1. [^N]: [source] — for claim "[brief description]"
2. [^N]: [source] — for claim "[brief description]"

### Unverifiable Claims (flagged)
- Line N: "[claim]" — source unknown, marked with caveat

### Uncitable (general knowledge, left without footnote)
- Line N: "[claim]" — general knowledge, no citation needed
```

## Composing with Other Skills

This skill is designed to be invoked as a post-processing step by other skills:

| Parent Skill | When to Invoke /citation |
|---|---|
| /guidebook-writer | After each chapter draft (Phase 3), before Phase 4 review |
| /policy-recommendation | After drafting the recommendation document |
| /legislative-briefer | After generating the 13-section briefer |
| /bill-drafter | After drafting provisions (verify BOL/BAA references) |
| /speech-writer | After drafting (cite any laws or statistics mentioned) |
| /csw | After generating any CSW document type |

## Common Mistakes to Avoid

1. **Citing the wrong BOL article** — Art. IX is Basic Rights, not Shari'ah (Art. X). See the error log at `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md` for the full pattern.
2. **Citing a BAA number from memory** — Always verify against `~/Vault/bangsamoro/bangsamoro-laws/index.md`. The numbering is chronological, not thematic.
3. **Using "Id." when the previous footnote cites a different source** — "Id." means "same source as immediately preceding footnote." If you need to refer back to an earlier source, use "supra note N."
4. **Omitting the section/article for legal citations** — "Rep. Act No. 11054" alone is insufficient. Specify the section and article: "Rep. Act No. 11054, sec. 6, art. VII."
5. **Footnoting general knowledge** — "BARMM is located in Mindanao" doesn't need a footnote. Save footnotes for specific, verifiable claims.
6. **Data without temporal context** — "Poverty is 29.80%" should specify the year: "Poverty incidence was 29.80% in 2021."

## Quality Check

Before finalizing any document, verify:
- [ ] Every blockquoted legal provision has a footnote
- [ ] Every BAA/BOL/RA number has a footnote on first use
- [ ] Every specific statistic has a source footnote
- [ ] Every borrowed framework credits the source on first use
- [ ] No "Id." follows a footnote to a different source
- [ ] All footnote numbers are sequential (no gaps, no duplicates)
- [ ] Unverifiable data is flagged, not presented as fact
