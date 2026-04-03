---
name: fact-checker
description: |
  Verify factual accuracy of documents before finalization. Two modes: (1) VALIDATE mode —
  paragraph-by-paragraph claim classification (SOURCED/AUTHOR'S OBSERVATION/INFERENTIAL/UNSOURCED),
  catches unsourced assertions masquerading as established fact; (2) Standard mode — P0-P10
  pattern check for names, titles, dates, numbers, legislation references.
  Use this skill whenever the user says "fact-check", "verify this", "check accuracy",
  "validate facts", "validate claims", "check if claims are sourced", "are these names correct",
  "check the names", "verify officials", "check legislation references", "verify dates",
  "fact check this document", "is this accurate", "validate this chapter",
  or wants to ensure 100% accuracy of any document before publishing.
  Also trigger when the user mentions "verification report", "accuracy check",
  "claim validation", "unsourced claims", "name verification", "title verification",
  or produces official documents (guidebooks, minutes, transcripts, legislative briefers,
  policy recommendations, speeches) that need factual validation.
  This skill catches errors that AI generation introduces — unsourced claims presented
  as institutional findings, fabricated legislation numbers, wrong names and titles.
  Also trigger on "temporal validation", "internal consistency check", "integrity check",
  "check footnotes", "footnote quality", "cross-chapter consistency", "evidence currency",
  "are the sources current", "check if footnotes match", or "unnecessary footnotes".
argument-hint: "[file-path or text]"
---

## Verification Framework

This skill implements the Universal Verification Framework (Prevent → Detect → Confirm).
Before running, read `${CLAUDE_SKILL_DIR}/references/verification-framework.md` for the full
protocol, taxonomy (P1-P10), known fabrication patterns, and authoritative source paths.
For source verification, follow `~/.claude/skills/fact-checker/references/source-preload-protocol.md` — read the full source file before marking any citation as VERIFIED.

**Key rule:** Run this skill on EVERY chapter/section of a document, not just the final chapter.
The #1 process failure is running fact-checker on only part of the document.

# Fact-Checker — Document Accuracy Verification

Verify every checkable fact before a document ships. Official documents with wrong names,
titles, or legislation references destroy credibility. This skill catches what AI generation
and auto-captions get wrong.

## When to Use

### Automatic (built into these skills' workflows)
- `/deep-research` — runs after Phase 4 self-correction, before final output
- `/research-pipeline` — runs after vault save, before delivery
- `/youtube-transcriber` — runs after transcript save, catches garbled names
- `/bill-drafter` — runs before delivering final bill draft
- `/resolution-drafter` — runs before delivering final resolution
- `/legislative-briefer` — runs before delivering final briefer
- `/policy-recommendation` — runs before delivering final policy document
- `/speech-writer` — runs before delivering final speech
- `/content-research-writer` — runs before delivering final content
- `/training-assistant` — runs on facilitator guides and participant handouts
- `/legal-assistant` — runs before delivering legal analysis output

### Manual
Run `/fact-checker [file]` on any document before finalization. Pairs with `/humanizer`
(style) and `/writer` (tone) — this skill handles accuracy.

### Safety Net (Stop hook)
A Stop hook in `settings.json` reminds to run fact-checker if any of the above skills
were used in the session but fact-checking was not completed.

## VALIDATE Mode — Claim-by-Claim Source Validation

**Invoke with:** `/fact-checker VALIDATE [file]`

This mode goes paragraph by paragraph through a document and classifies every factual assertion. It runs BEFORE the standard P0-P10 check and BEFORE `/citation`. Its purpose is to catch unsourced claims that sound authoritative but have no evidence — the kind of error that standard pattern-matching misses.

### What VALIDATE Does

For each paragraph, it:
1. **Identifies** every factual assertion (not methodology instructions, not opinions, not questions)
2. **Classifies** each assertion into one of four categories
3. **Flags** any assertion that needs fixing before the document can proceed

### Claim Classifications

| Classification | Meaning | Action |
|---------------|---------|--------|
| **SOURCED** | Cites a specific enacted law, court decision, official document, or verifiable fact | Verify the citation is correct |
| **AUTHOR'S OBSERVATION** | Based on the author's professional experience — acceptable when framed as such | Flag if framed as institutional finding ("well-documented across BARMM") rather than personal observation |
| **INFERENTIAL** | Reasoned from evidence but not directly stated in any source | Acceptable if reasoning is shown; flag if presented as established fact |
| **UNSOURCED** | Stated as fact with no source and no attribution to the author's experience | Must be fixed — either find a source, reframe as the author's observation, or remove |

### Red Flags (highest priority)

These patterns indicate an UNSOURCED claim masquerading as established fact:

- "The most common error in BARMM documents..." — says who? Based on what data?
- "Well-documented across BARMM institutions..." — where is it documented?
- "Studies show..." / "Research has found..." — which studies? Which research?
- "It is widely recognized that..." — by whom?
- Internal statistics presented as institutional findings ("68 errors, 39 critical")
- References to internal tools, error logs, or development processes as if they're published sources
- Footnotes that restate the body text instead of citing a source
- Footnotes citing other in-development guidebooks as authoritative published works
- Footnotes citing internal file paths or development artifacts
- "Islamic governance" or "Islamic principles" when the BOL says "Shari'ah" — overgeneralization (Pattern #11)
- "administrative staff" or "government staff" listed as document audience — name specific roles (Pattern #12)
- Internal development jargon in external-facing text: "institutional boundary", "pipeline enforcement", "context rot" (Pattern #13)
- Goal, pillar, or framework names that don't match the source document verbatim — verify against BDP/OIC/SDG before citing (Pattern #14)
- "supreme authority" or "sole authority" for any BARMM institution — read the creating law's exact language before describing an institution's role (Pattern #15)

### Unnecessary Footnotes (over-footnoting)

Not every statement needs a footnote. Footnotes exist to cite **sources the reader cannot verify without the citation**. These do NOT need footnotes:

- **The author's own methodology or analysis** — "This chapter teaches you how to..." is the author's instruction, not a factual claim requiring a source
- **Standard legal definitions** — "Legal research is the systematic process of identifying applicable legal authority" does not need a citation
- **Restated body text** — a footnote that simply rephrases what the paragraph already says is not a citation, it's padding
- **The author's professional judgment** — "This is the most important step" is an observation, not a citable fact
- **Widely-known facts** — "The Philippines has three branches of government" needs no footnote
- **Internal references within the document** — "See Chapter 5 for the full list" is a cross-reference, not a citation

**What DOES need a footnote:**
- Verbatim quotations from enacted law, court decisions, or official documents
- Specific statistics, data points, or counts with a verifiable source
- Claims attributed to a named person, institution, or publication
- Legal provisions cited by article and section number

**The over-footnoting rule:** If removing a footnote leaves the reader no worse off — they can still verify the claim from context — the footnote is unnecessary. Remove it.

### AI Issue vs. Human Issue (critical distinction)

When a claim describes an error pattern, determine whether it is an **AI-generated error** or a **documented human researcher error**:

- **AI issue:** BOL article number swaps (Art. IX/X, Art. V/VI), BAA number fabrication, ministry abbreviation errors, fiqh presented as enacted law — these are LLM fabrication patterns from training data, NOT documented patterns in human-authored BARMM documents. Do not present AI weaknesses as institutional or human researcher problems.
- **Human issue:** Only flag as a human researcher pattern if there is verifiable evidence (COA findings, SC decisions citing wrong provisions, published errata). If the only evidence is the AI's own error log, it is an AI issue.
- **Rule:** Never write "this is the most common error in BARMM documents" based on AI-generated error data. If the error pattern comes from Claude's fact-check error log, it belongs in the AI in Practice callout or the AI Declaration — not in the methodology chapter as if human researchers routinely make this mistake.

### Integrity Checks — Second Dimension

The four-category classification (SOURCED/AUTHOR'S OBSERVATION/INFERENTIAL/UNSOURCED) answers: **does this claim have a source?** Integrity checks answer a different question: **is the claim internally sound?** A SOURCED claim can still fail integrity — if its source is outdated, if it contradicts another claim in the same document, or if it breaks causal logic.

Run integrity checks on ALL claims, including SOURCED ones. A claim that is both SOURCED and integrity-failed is worse than an unsourced claim — it looks authoritative but misleads.

#### IC-1: Source-Claim Temporal Alignment

The source must be current enough to support the claim's time context.

| Pattern | Example | Why It Fails |
|---------|---------|-------------|
| **Claim date > source date** | "As of 2026, there are 89 BAAs" cited to a 2024 BAA index | The 2024 index cannot validate a 2026 count — BAAs 82-89 were enacted Jan-Feb 2026 |
| **Source predates a known event that changed the facts** | BARMM population figure cited to a pre-Sept 2024 source | The Sulu exclusion (Sept 2024) changed BARMM's population; pre-ruling data includes Sulu |
| **Amended law cited without noting amendment** | Citing BAA 35 (Electoral Code) without noting BAA 87 and BAA 88 amendments | Reader gets the original version, not the current one |
| **Repealed law cited as current** | Citing RA 6938 (Cooperative Code of 1990) without noting it was superseded by RA 9520 (2008) | The cited source is no longer good law |

**How to check:** For every SOURCED claim + its footnote, ask:
1. What is the **date of the source** cited in the footnote?
2. What is the **date context of the claim** (explicit or implied)?
3. Has any **known event** between those dates changed the facts? (SC rulings, new BAAs, amendments, repeals)
4. Is the source the **most current version** of that authority?

Flag as: `TEMPORAL MISMATCH: [claim date context] validated by [source date] — [what changed between]`

#### IC-2: Internal Document Consistency

Claims within the same document must not contradict each other.

| Pattern | Example | Why It Fails |
|---------|---------|-------------|
| **Contradictory counts** | Ch. 2 says "89 BAAs" but Ch. 7 says "84 BAAs" | The document asserts two different numbers for the same thing |
| **Contradictory dates** | Ch. 1 says "October 2025" for SC ruling, Ch. 10 says "September 30, 2025" | Same event, different dates across chapters |
| **Contradictory provisions** | Ch. 3 says audit is "Art. XII, Sec. 34" but the template says "Art. XII, Sec. 2" | Same provision, different section numbers |
| **Contradictory status** | Ch. 5 says transitional justice is "Pending" but Ch. 6 lists BAA 89 as enacted | The status changed but not all references were updated |

**How to check:** After scanning each chapter, maintain a running **fact register** of key assertions:
- BAA count: [N]
- Province count: [N]
- Key dates: [event → date]
- Section citations: [provision → article.section]
- BAA status: [BAA N → enacted/pending/struck down]

When a new assertion appears, compare it against the register. If it differs, flag as: `INTERNAL CONTRADICTION: [Ch. X] says [A] but [Ch. Y] says [B]`

#### IC-3: Logical Sequence and Causality

Events and provisions must be described in an order that reflects their actual relationship.

| Pattern | Example | Why It Fails |
|---------|---------|-------------|
| **Effect before cause** | "BAA 86 established 32 districts" described before explaining that BAA 58/77 were struck down | The reader cannot understand BAA 86 without knowing what it replaced |
| **Reversed causality** | "The SC ruling happened because Parliament enacted BAA 86" | BAA 86 was the *response* to the ruling, not the cause |
| **Anachronistic reference** | "Under BAA 82 (Labor Code), which was enacted in January 2026..." in a section describing events from 2024 | The BAA didn't exist at the time the section describes |
| **Circular reasoning** | "BAA 13 is authoritative because it is the Administrative Code, and it is the Administrative Code because it is authoritative" | No independent basis established |

Flag as: `SEQUENCE ERROR: [description of the logical break]`

#### IC-4: Footnote Temporal Integrity

Every footnote must be checked for whether the cited source is temporally valid for the claim it supports.

**For each footnote, verify:**

1. **Is the cited source still good law?**
   - Has the BAA/RA/EO been amended, repealed, or struck down since the footnote was written?
   - If amended: does the footnote cite the **current** version or the **original**?
   - If repealed: the footnote is citing dead law — flag immediately

2. **Does the source date cover the claim's time frame?**
   - A footnote citing "BAA 13, Book VI, Title III" to support a claim about MENRE's *current* mandate must account for BAA 37 (which amended BAA 13)
   - A footnote citing "BDP 2023-2028, Chapter 7" to support a 2026 budget figure must verify the BDP chapter covers FY 2026 data (the BDP was written in 2023 — it contains projections, not actuals for 2026)

3. **Does the footnote cite the right granularity?**
   - Citing "RA 11054" (the entire BOL) for a specific section claim is too vague — cite the article and section
   - Citing "BAA 13" for a specific ministry mandate should cite the Book, Title, and Section

4. **Does the footnote match the claim it supports?**
   - Footnote [^8] defined as PD 1083 but attached to a claim about RA 9710 (Magna Carta of Women) = footnote mismatch
   - Footnote [^3] restates the body text instead of citing a source = not a real citation

Flag as: `FOOTNOTE INTEGRITY: [^N] — [issue description]`

#### IC-5: Evidence Currency

When multiple sources exist for the same claim, the most current authoritative source should be cited.

| Pattern | Example | Fix |
|---------|---------|-----|
| **Older source when newer exists** | Citing RA 6938 (Cooperative Code 1990) when RA 9520 (2008) superseded it | Cite RA 9520 as the current law; note RA 6938 as repealed |
| **Original law when amended version exists** | Citing BAA 35 without noting BAA 87/88 amendments | Cite "BAA 35, as amended by BAA 87 and BAA 88" |
| **Pre-event data when post-event data exists** | Using pre-Sulu-exclusion BARMM population data | Use post-Sept 2024 data or note the Sulu exclusion caveat |
| **Secondary source when primary exists** | Citing LawPhil for a provision when the Official Gazette version is available | Prefer the Official Gazette version |

Flag as: `EVIDENCE CURRENCY: [older source cited] — [newer/better source available]`

### VALIDATE Output

```markdown
## Claim Validation Report

**Document:** [filename]
**Date:** [date]
**Paragraphs scanned:** [N]
**Claims identified:** [N]

### Summary
| Classification | Count |
|---------------|-------|
| SOURCED | N |
| AUTHOR'S OBSERVATION | N |
| INFERENTIAL | N |
| UNSOURCED | N |

### Integrity Summary
| Check | Issues Found |
|-------|-------------|
| IC-1: Temporal Alignment | N |
| IC-2: Internal Consistency | N |
| IC-3: Logical Sequence | N |
| IC-4: Footnote Integrity | N |
| IC-5: Evidence Currency | N |

### Unsourced Claims (must fix)
| Location | Claim | Issue | Recommended Fix |
|----------|-------|-------|----------------|
| Ch. 1, para 3 | "most common error in BARMM documents" | No evidence cited | Reframe: "adjacent article numbers are easily confused" |

### Integrity Failures (must fix)
| Location | Claim | Check | Issue | Recommended Fix |
|----------|-------|-------|-------|----------------|
| Ch. 2, line 196 | "BAA 38 (procurement)" | IC-1 | BAA 38 is about fund releases, not procurement | Remove BAA 38 reference; note no procurement BAA exists |
| Ch. 3, line 66 vs Ch. 3, line 252 | "Art. XII, Sec. 34" vs "Art. XII, Sec. 2" for audit | IC-2 | Same provision cited with different section numbers | Correct to Sec. 2 (verified against BOL) |
| Ch. 12, [^8] | PD 1083 footnote attached to RA 9710 claim | IC-4 | Footnote definition doesn't match the claim it supports | Reassign footnote or create separate footnote for RA 9710 |
| Ch. 5, line 305 | "Transitional justice: Pending" | IC-2 | BAA 89 (Transitional Justice) enacted Feb 2026 | Update status to "Enacted (BAA 89)" |

### Footnote Quality
| Footnote | Type | Issue |
|----------|------|-------|
| [^2] | Unnecessary | Footnotes the author's own methodology — not a citable claim |
| [^3] | Restates body text | Not a citation — remove |
| [^5] | Cites internal artifact | Fact-Check Error Log is not a published source |
| [^7] | Cites unpublished work | Guidebooks in development are not citable sources |
| [^8] | Footnote mismatch | Defined as PD 1083 but attached to RA 9710 claim |
| [^12] | Cites amended law | BAA 35 cited without noting BAA 87/88 amendments |

### Claims Verified
| Location | Claim | Source | Integrity |
|----------|-------|-------|-----------|
| Ch. 1, para 5 | "89 BAAs enacted" | BAA index (Feb 2026) | PASS — date-aligned |
| Ch. 3, line 63 | "Art. VII, Sec. 39 — civil service" | BOL verbatim | PASS — current, unamended |
```

### When to Run VALIDATE

- **ALWAYS** before `/citation` — no point adding Feliciano footnotes to unsourced claims
- **ALWAYS** on any chapter of a guidebook before PDF generation
- **ALWAYS** on legal analysis documents (memos, briefers, opinions) before delivery
- After any major rewrite or content addition

### Scaling by Document Size

| Size | Pages | IC-2 Fact Register | IC Checks | Approach |
|------|-------|-------------------|-----------|----------|
| **Small** | 1-5 | Skip | IC-1, IC-4, IC-5 inline | Single pass, no register overhead |
| **Medium** | 5-50 | Maintain across chapters | All IC-1 through IC-5 | Sequential chapter-by-chapter with running register |
| **Large** | 50+ | Shared register across parallel agents | All IC-1 through IC-5 | Parallel agents per chapter, IC-2 cross-chapter sweep at end |

**For multi-chapter guidebooks (the most common use case):**
1. VALIDATE each chapter sequentially (not parallel — IC-2 register must accumulate)
2. After all chapters: run a dedicated IC-2 cross-chapter sweep comparing the register entries
3. The cross-chapter sweep checks: BAA counts, province counts, key dates, section citations, BAA status, ministry abbreviations — anything that appears in multiple chapters must be consistent

---

## Content Production Pipeline (MANDATORY for all publications)

```
1. WRITE      → Draft the content (any content skill)
2. VALIDATE   → /fact-checker VALIDATE (classify every claim, flag unsourced)
3. FIX        → Resolve all UNSOURCED claims (source them, reframe, or remove)
4. VERIFY     → /fact-checker (P0-P10 known pattern check)
5. CITE       → /citation (add Feliciano footnotes to sourced claims)
6. REVIEW     → /legal-reviewer ACCURACY (verify legal provisions verbatim)
7. DELIVER    → Generate PDF/DOCX
```

Each step depends on the previous one. Do not skip steps. Do not run `/citation` before VALIDATE — it adds professional-looking footnotes to potentially fabricated claims.

---

## Verification Categories (P0-P10 Priority Order)

Check claims in this priority order. Higher priority = higher risk of institutional damage if wrong.

**P0 — Contextual Inconsistency** (highest priority)
Check whether the output contradicts any document that was explicitly loaded into the context window during this session. This catches the "Air Canada failure mode" where the model generates content that contradicts its own loaded sources.

How to check:
1. List all source documents loaded during this session (BOL files, BAA text, officials list, BDP chapters)
2. For each P1-P4 claim in the output, identify which loaded document it should reference
3. Re-read that specific passage from the loaded document using the Read tool
4. Compare the output claim against the source passage
5. Flag any contradiction as CRITICAL — contextual inconsistency

| Priority | Category | What to Check | Example Error |
|----------|----------|--------------|---------------|
| **P1** | Constitutional provisions | Article, section numbers; verbatim text | Citing Art. X when it should be Art. IX |
| **P2** | BOL provisions | Article (18 total), section numbers | Art. XII Sec. 22 for block grant (should be Secs. 15-16) |
| **P3** | Legislative references | BAA/RA/Resolution number-to-title mapping | "BAA 25 (Environment Code)" — BAA 25 is a hospital upgrade |
| **P4** | Verbatim legal text | Word-for-word accuracy of quoted provisions | Misquoted BOL preamble |
| **P5** | Proper nouns — persons | Names, middle initials, current titles | "Abdulraof Makakua" → Abdulraof A. Macacua |
| **P6** | Proper nouns — institutions | Ministry names, abbreviations | "MOL" → MOLE; "MST" → MOST; "MPWH" → MPW |
| **P7** | Statistical data | Percentages, ratios, counts, monetary values | "12 provinces" when BARMM has 5 |
| **P8** | Temporal claims | Facts that may be outdated | Sulu listed as BARMM province (excluded by SC ruling 2024) |
| **P9** | Attributed frameworks | Author names, framework names | "Meadow's 12 leverage points" → Meadows |
| **P10** | Other factual claims | Dates, events, places, counts | ARMM created by 1996 FPA (should be RA 6734, 1989) |

**Cross-cutting:** Every claim in P1-P10 requires a `[^N]` footnote in Feliciano 10th Ed. format.

### Layer 2B: Verify-Regenerate Loop

After running P0-P10, execute the Verify-Regenerate Loop (defined in verification-framework.md Section 1C) on ALL claims scored P1-P4.

MANDATORY for: bills, resolutions, legislative briefers, guidebooks citing legislation, policy recommendations.
RECOMMENDED for: speeches (P5-P6 only).
OPTIONAL for: transcripts (P5 name verification only).

The loop does NOT terminate until every P1-P4 claim is either:
- VERIFIED (source passage matches, with file path + line number recorded)
- [UNVERIFIED] (3 regeneration attempts failed, user alerted)

## Source Priority

Check facts in this order — stop at the first authoritative match:

### Tier 1: Local References (fastest, most reliable)
- `/bangsamoro` skill references — officials, governance, BOL provisions
- `barmm-officials-2025-2026.md` — verified MP names, titles, committee chairs
- `~/Vault/bangsamoro/bangsamoro-laws/index.md` — 89 BAAs with titles and dates
- `e-bangsamoro/references/MP-names.md` — canonical MP name list
- Project-local reference files

### Tier 2: BARMM Official Websites
- `parliament.bangsamoro.gov.ph` — current MPs, committees, legislation
- `bangsamoro.gov.ph` — executive leadership, ministries, news
- `barmm.gov.ph` — official announcements, organizational structure

### Tier 3: Web Search
- Philippine government sites (officialgazette.gov.ph, senate.gov.ph, congress.gov.ph)
- News sources for event dates and recent appointments
- Academic and institutional sources

## Workflow

### Step 1: Scan the Document

Read the target file. Extract every verifiable claim into a checklist:

```
[ ] Person: [name as written] — [context/title mentioned]
[ ] Title: [position as written] — [person it's attributed to]
[ ] Legislation: [reference as written] — [context]
[ ] Date: [date as written] — [what it refers to]
[ ] Number: [figure as written] — [what it measures]
[ ] Organization: [name as written] — [context]
[ ] Place: [name as written] — [context]
```

### Step 1a: BAA Cross-Reference Check

Extract every "BAA No. N" or "BAA N" reference from the document.
For each, read `~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md` and verify
the number matches the claimed title.

Report: MATCH / MISMATCH (with correct title) / NOT_FOUND

Common fabrications to catch:
- BAA 25 ≠ Environment Code (it's a hospital upgrade)
- BAA 60 ≠ BEZA Act (it's a memorial site)
- BAA 11 ≠ Education Code (it's Power of Appointment; Education Code = BAA 18)
- Any BAA number > 89 (only 89 enacted as of Feb 2026)

### Step 1b: BOL Article Map Verification

Extract every BOL article/section citation. Verify against the 18-article map
in `${CLAUDE_SKILL_DIR}/references/verification-framework.md` (Section 8).

Flag known dangerous swaps:
- Art. IX (Basic Rights) vs Art. X (Justice/Shari'ah) — 5 documented occurrences
- Art. V (Powers) vs Art. VI (Intergovernmental) — 3 documented occurrences
- Art. VII (Parliament) vs Art. VIII (Wali) — 3 documented occurrences
- Art. VIII (Wali) vs Art. XVI (Transition) — multiple occurrences
- Art. XII Sec. 9 vs Secs. 15-16 (Block Grant location)

### Step 1c: Known Error Pattern Scan

Read `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md`.
Scan the document for any text matching documented patterns:

- "Shari'ah Appellate Court" → should be "Shari'ah High Court"
- ARMM creation attributed to 1996 FPA → should be RA 6734 (1989)
- "OHRAORA" → should be "ORAOHRA"
- Priority code count ≠ 7 → flag
- BEZA attributed to a BAA → created by BOL Art. XII Sec. 6
- "6 provinces" → should be 5 (after Sulu exclusion)

Flag with: "KNOWN ERROR PATTERN: [pattern name]"

### Step 1d: Novel Fabrication Detection

Beyond the 10 known patterns, actively search for NEW fabrications not yet in the error log:
1. Any BAA number cited that doesn't appear in `~/Vault/bangsamoro/bangsamoro-laws/index.md` — flag as "NOVEL FABRICATION: BAA [N] not found in index"
2. Any government program, office, or commission name not in `moa-structure.md` or officials list — flag as "NOVEL FABRICATION: [name] not found in references"
3. Any BOL section number cited that doesn't exist in the actual BOL chapter file — READ the chapter file and verify the section exists
4. Any person name + title combination not in the officials reference — flag for manual verification
5. If a novel fabrication is confirmed, add it to the error log (Step 5) as a new pattern for future prevention

### Step 1e: Ministry Abbreviation Whitelist

Extract every ministry abbreviation from the document.
Accept ONLY: MAFAR, MBHTE, MENRE, MFBM, MOH, MHSD, MILG, MIPA,
             MOLE, MPOS, MPW, MOST, MSSD, MTIT, MOTC

Flag any variant: MOL→MOLE, MST→MOST, MPWH→MPW, etc.
Also verify: there are 15 line ministries (not 16). The OCM is not a ministry.

### Step 1f: Citation Completeness Check

Scan body text (NOT footnote definitions starting with `[^N]:`) for:
- Percentages (N%)
- Named persons with titles
- BAA/BOL/RA references
- Specific dates and counts

Flag any that appear without a `[^N]` footnote on the same sentence.
Report: "[stat/name/ref] on line N has no footnote"

### Step 1g: Temporal & Integrity Validation

**Part A — Known temporal issues** (from error log):
- "Sulu" mentioned as BARMM territory/province without SC ruling caveat
- "6 provinces" → should be 5 after Sulu exclusion (Sept 2024 SC ruling, EO 91 July 2025)
- Official names/titles that may have changed since reference file date
- BAA count > 89 → may be fabricated
- "ARMM" with creation context → verify date is 1989/RA 6734

**Part B — Integrity checks IC-1 through IC-5** (from VALIDATE mode):
- **IC-1 (Temporal Alignment):** For every SOURCED claim, compare the claim's date context against the source's date. Flag if source predates a known event that changed the facts.
- **IC-2 (Internal Consistency):** Maintain a running fact register across chapters. Flag contradictions in counts, dates, provision numbers, or status.
- **IC-3 (Logical Sequence):** Verify causal chains and chronological order. Effects cannot precede causes.
- **IC-4 (Footnote Integrity):** For every footnote, verify: (a) source is still good law, (b) source date covers claim's time frame, (c) footnote definition matches the claim it supports.
- **IC-5 (Evidence Currency):** When a newer/better source exists for a claim, flag the older citation.

Flag with: `TEMPORAL: [description]` or `IC-[N]: [description]`

### Step 2: Triage & Verify Each Claim

**Triage rule**: If the generating skill tagged claims as EXTRACTED/INFERRED (per the honesty controls in verification-framework.md Section 6), verify all INFERRED claims first — these are highest-risk. EXTRACTED claims with valid source paths get a lighter check (confirm the source file path exists and the section number is correct). Untagged claims are treated as INFERRED.

Also check for bare `[UNVERIFIED]` markers missing reasons. Flag: "INCOMPLETE MARKER: [UNVERIFIED] on line N has no reason — should be [UNVERIFIED: reason]"

For each item on the checklist:

1. **Check Tier 1 sources first.** Read the relevant reference file. Most BARMM names and
   titles are already in `barmm-officials-2025-2026.md`.

2. **If not in local refs, check Tier 2.** Use web fetch or Playwright CLI (never Claude in
   Chrome) to check official BARMM websites.

3. **If still unverified, check Tier 3.** Web search with specific queries:
   `"[name] BARMM [year]"` or `"BAA No. [X] bangsamoro"`.

4. **Mark the result** (include ALL of these for every claim):
   - **Status**: VERIFIED / CORRECTED / UNVERIFIED
   - **Hallucination Type**: Extrinsic / Fabricated / Intrinsic / Contextual Inconsistency / N/A (if verified correct)
   - **Source Path**: file path + line number where the authoritative answer was found (e.g., `bol-ra-11054/chapter-3.md:45`)
   - **Note**: If CORRECTED, what was wrong and what the source says

   Every P1-P4 claim MUST have a source path recorded. No exceptions.

### Step 3: Apply Corrections

For each CORRECTED item:
- Fix the error in the document using Edit tool
- Log what was wrong and what it was changed to

For each UNVERIFIED item:
- Insert `[UNVERIFIED]` marker after the claim
- The author decides whether to keep, research further, or remove

### Step 4: Generate Verification Report

After all checks, produce a priority-ordered report:

```markdown
## Verification Report

**Document**: [filename]
**Checked**: [date]
**Framework**: Universal Verification Framework v1.0
**Verify-Regenerate Loop**: [Ran / Skipped (document type)] — [N] P1-P4 claims processed, [N] VERIFIED, [N] [UNVERIFIED], [N] iterations

### Summary
| Severity | Count |
|----------|-------|
| CRITICAL (P1-P4 errors) | N |
| HIGH (P5-P8 errors) | N |
| MEDIUM (P9-P10 errors) | N |
| VERIFIED | N |
| Total claims checked | N |

### P0: Contextual Inconsistency
| # | Claim | Loaded Source | Contradiction | Source Path | Status |
|---|-------|-------------|---------------|-------------|--------|

### P1-P4: Legal Provisions (Constitutional, BOL, Legislative, Verbatim)
| # | Priority | Claim | Source Path | Hallucination Type | Status |
|---|----------|-------|------------|-------------------|--------|

### P5: Person Names
| # | Name as Written | Verified Name | Source Path | Hallucination Type | Status |
|---|----------------|--------------|------------|-------------------|--------|

### P6: Institution Names
| # | Name as Written | Correct Form | Source Path | Hallucination Type | Status |
|---|----------------|-------------|------------|-------------------|--------|

### P7-P10: Data, Temporal, Frameworks, Other
| # | Priority | Claim | Source Path | Hallucination Type | Status |
|---|----------|-------|------------|-------------------|--------|

### Citation Completeness
| Line | Claim | Footnote Status |
|------|-------|----------------|

### Known Error Patterns Detected
| Pattern | Location | Details |
|---------|----------|---------|

### Severity Guide
- **CRITICAL**: Must be fixed before ANY output is generated (PDF, DOCX, etc.)
- **HIGH**: Must be fixed before publication
- **MEDIUM**: Should be fixed; may proceed with user approval if time-constrained

### Hallucination Type Key
- **Extrinsic**: Claim has no basis in any source — invented from training data
- **Fabricated**: Claim invents a specific identifier (BAA number, article, date) that does not exist
- **Intrinsic**: Claim contradicts information explicitly stated in source documents provided for the task
- **Contextual Inconsistency**: Claim contradicts a document loaded into this session's context window (Air Canada failure mode)
```

### Step 5: Update Error Log

After fact-checking, if NEW error patterns are discovered (not already in the log):
1. Append to `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md`
2. Categorize under existing pattern or create new pattern entry
3. Include: document name, what was wrong, what is correct, authoritative source
4. Update the count in the error log summary

### Step 6: QA Loop Until Zero Errors

After Steps 1-5, if the verification report shows ANY CRITICAL (P1-P4) or HIGH (P5-P8) errors that were CORRECTED:

1. Re-read the corrected sections of the document
2. Re-run Steps 1a-1g on ONLY the corrected sections (not the full document)
3. Verify that corrections are clean — no new errors introduced by the fix
4. If new errors found: correct and loop again
5. Exit condition: **0 CRITICAL errors AND 0 HIGH errors** in the re-verification pass

The loop does NOT terminate until:
- Every P1-P4 claim is VERIFIED with a source path, OR marked [UNVERIFIED: reason]
- Every P5-P8 claim is VERIFIED or flagged for user decision
- Every correction has been re-verified clean
- The final verification report shows 0 CRITICAL and 0 HIGH errors

If the loop exceeds 3 iterations on the same claim, escalate to the user with the specific claim and all attempted corrections.

## Rules

- **Never silently pass a suspicious claim.** If a name looks garbled (common with Whisper
  output), research it. The earlier session exposed "Danrajim Minenak Mani Rahim" being
  left unresearched — that was actually Hadja Bainon G. Karon (BWC Chairperson).

- **Cross-reference titles with names.** A person's title may have changed. The officials
  reference has current (2025-2026) data, but verify against the document's time context.

- **Legislation numbers are non-negotiable.** A wrong BAA or RA number in an official
  document is a serious error. Always verify against the laws index.

- **Update reference files.** When verification reveals a name or title not yet in the
  officials reference, add it. This prevents the same research from being repeated.

- **First-mention rule.** While checking names, also verify that the document follows the
  first-mention rule: full name + full position/title on first mention.

## Common Whisper/Auto-Caption Errors

These are the most frequent garbles in Bangsamoro transcripts. Check for these patterns:

| Error Pattern | Usually Means |
|--------------|---------------|
| Unrecognizable syllables for Filipino names | Garbled MP or official name — check officials ref |
| "BAA" numbers that don't match known legislation | Wrong number or garbled audio |
| Ministry acronyms without expansion | Verify the acronym matches the ministry name |
| "Chairman/Chairperson of [garbled]" | Commission or committee head — check refs |
| Numbers that seem too round or too specific | Cross-check against official statistics |

See `barmm-officials-2025-2026.md` for the full auto-caption error mapping table.

## Gotchas

- BOL article numbers are the #1 fabrication target — always verify against local transcription at ~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/
- BAA numbers are the #2 fabrication target — verify against ~/Vault/bangsamoro/bangsamoro-laws/index.md (89 BAAs enacted as of Feb 2026)
- Ministry abbreviations use BARMM equivalents (MFBM, MOLE, MBHTE, MILG, MOH) — never national (DBM, DOLE, DepEd, DILG, DOH)
- After generating content from source documents, re-read the specific cited passage and verify the output matches — contextual inconsistency (wrong output despite correct context) is the hardest failure mode to catch
- Official titles change frequently — always verify against ~/.claude/skills/bangsamoro/references/barmm-officials-2025-2026.md, not training data
- Filipino Muslim names from auto-captions (Whisper) are always garbled — verify every name against the officials reference file
- Never trust BAA numbers that appear in subagent output without verification — subagents fabricate BAA numbers that /citation then makes look authoritative

## Integration with Other Skills

| Skill | How It Connects |
|-------|----------------|
| `/youtube-transcriber` | Run fact-checker (P1-P10) on transcripts after organized notes are generated |
| `/humanizer` | Run fact-checker BEFORE humanizer — fix facts first, then style |
| `/writer` | Same — accuracy before tone |
| `/bangsamoro` | Primary knowledge source for BARMM-related verification (P1-P8) |
| `/legal-researcher` | Find and extract provision text for P1-P4 verification. When verifying legislative references (BAA numbers, BOL articles, section identifiers), invoke `/legal-researcher EXTRACT` to retrieve the authoritative source text for comparison. |
| `/legal-reviewer` | Verify verbatim accuracy of quoted legal provisions (P4 checks). Invoke ACCURACY mode to compare quoted text against source documents word-for-word. |
| `/legal-assistant` | For deep legislation verification beyond the laws index (P1-P4) |
| `/guidebook-writer` | Phase 4b: run fact-checker on EVERY chapter before PDF generation |
