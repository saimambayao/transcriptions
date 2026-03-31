# Universal Verification Framework

Canonical reference for all content skills. Every skill that produces BARMM content must read this file and follow the protocol appropriate to its output type.

**Problem**: 66 documented errors across 7 guidebooks (38 critical). AI fabricates facts and dresses them as authoritative citations. The same 10 error patterns recur independently across documents.

**Solution**: Three-layer verification (Prevent, Detect, Confirm) with priority-ordered taxonomy (P1-P10).

---

## 1. Verification Taxonomy (P1-P10)

Every factual claim falls into one of ten priority categories. Higher priority = higher risk of institutional damage if wrong. Every claim in P1-P10 requires a `[^N]` footnote in Feliciano 10th Ed. format. No exception.

| Priority | Category | What to Verify | Authoritative Source | Citation Format |
|----------|----------|----------------|---------------------|-----------------|
| **P1** | Constitutional provisions | Article, section numbers; verbatim text | Constitution transcription | `Const. art. N, sec. N.` |
| **P2** | BOL provisions | Article (18 total), section numbers; verbatim text | `bol-key-provisions.md`, BOL transcription (5 files) | `Rep. Act No. 11054, art. N, sec. N.` |
| **P3** | Legislative references | BAA number-to-title mapping; RA numbers; Resolution numbers | `baa-quick-reference.md`, `INDEX.md`, resolution classification | `BAA No. N.` / `Rep. Act No. N.` |
| **P4** | Verbatim legal text | Word-for-word accuracy of quoted provisions | BOL transcription, BAA full text, RA source PDFs | Blockquote + footnote |
| **P5** | Proper nouns -- persons | Names, middle initials, current titles, current positions | `barmm-officials-2025-2026.md` | Full name + title on first mention |
| **P6** | Proper nouns -- institutions | Ministry names, abbreviations, attached agencies, commissions | `moa-structure.md`, error log | Correct abbreviation per whitelist (Section 7) |
| **P7** | Statistical data | Percentages, ratios, counts, monetary values | BDP chapter summaries, PSA data | `2nd BDP 2023-2028, Ch. N.` |
| **P8** | Temporal claims | Facts that may be outdated due to court rulings, elections, new legislation, leadership changes | Error log (Sulu SC ruling 2024, EO 91 2025), WebSearch | Dated citation + caveat if contested |
| **P9** | Attributed frameworks | Author names, framework names, publication details | Source books, bibliography | `Author, *Title* (City: Publisher, Year).` |
| **P10** | All other factual claims | Dates, events, places, counts, causal claims | Multiple sources | Appropriate citation per claim type |

**Cross-cutting rule**: Every P1-P10 claim requires a `[^N]` Feliciano footnote. No exception.

---

## 1B. Hallucination Taxonomy (Source Classification)

Every error falls into one of four hallucination types. This taxonomy determines WHERE the error originated and HOW to prevent recurrence. Source: Matt Pocock, "Never Trust An LLM" — comprehensive taxonomy of LLM hallucinations applied to BARMM legal workflows.

| Type | Definition | Risk Level | Mitigation |
|------|-----------|------------|------------|
| **Factual Error (Extrinsic)** | Wrong claim from training data — model was never given correct info | HIGH | Load authoritative source BEFORE generation |
| **Fabricated Entity** | Invented BAA number, package name, government program, person | CRITICAL | Verify against whitelist (BAA index, officials list, MOA structure) |
| **Intrinsic Error** | Error about info explicitly provided in context | MEDIUM | Re-read the source passage after generation |
| **Contextual Inconsistency** | Output contradicts document already loaded in context window | CRITICAL | Verify-Regenerate Loop (see Section 1C) |

**Key distinction — Intrinsic vs. Extrinsic:**
- **Intrinsic** knowledge = information you explicitly loaded into the context (BOL files, BAA text, officials list). Errors here are less common but more alarming — the model saw the correct answer and still got it wrong.
- **Extrinsic** knowledge = information the model draws from training data alone. This is where 80%+ of BARMM errors originate (BOL article misattribution, BAA number fabrication, ministry abbreviation errors).
- **Rule**: ALWAYS convert extrinsic to intrinsic by loading Tier 1 source files before generation. Never rely on training data for BOL articles, BAA numbers, official names, or ministry structures.

---

## 1C. Verify-Regenerate Loop (Zero-Hallucination Protocol)

This loop runs on EVERY P1-P4 claim (Constitutional, BOL, legislative, verbatim text). It does not exit until every claim is VERIFIED or marked [UNVERIFIED]. Modeled on `/legal-reviewer`'s mandatory QA Loop.

```
FOR each P1-P4 claim in generated output:
  1. EXTRACT the specific citation (article, section, BAA number, quoted text)
  2. IDENTIFY the authoritative source file for this claim type:
     - P1 (Constitution): ~/Vault/bangsamoro/ Constitution transcription
     - P2 (BOL): ~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/ (5 files)
     - P3 (BAA/RA): ~/Vault/bangsamoro/bangsamoro-laws/index.md + BAA full text
     - P4 (Verbatim): the specific source document being quoted
  3. READ the source passage (use Read tool — not from memory, not from training data)
  4. COMPARE: does the generated text match the source?
     - Verbatim quotes: character-by-character match
     - Article/section references: exact number match
     - BAA number-to-title mappings: match against BAA index
     - Official names/titles: match against barmm-officials-2025-2026.md
  5. IF MATCH -> mark VERIFIED, record source path + line number
  6. IF MISMATCH -> REGENERATE the claim using the actual source text
  7. RE-VERIFY the regenerated claim (re-read source again)
  8. IF still mismatched after 3 attempts -> mark [UNVERIFIED], alert user
  9. NEVER output a P1-P4 claim without VERIFIED or [UNVERIFIED] status
```

**Legitimate Sources (Tier 1 — the ONLY acceptable sources for this loop):**
- BOL: `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` (5 chapter files)
- BAA index: `~/Vault/bangsamoro/bangsamoro-laws/index.md` (89 BAAs)
- Officials: `~/.gemini/skills/bangsamoro/references/barmm-officials-2025-2026.md`
- BDP: `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/` (15 chapters)
- MOA structure: `~/.gemini/skills/bangsamoro/references/moa-structure.md`
- Error log: `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md`

**Training data is NOT a legitimate source for**: BOL article/section numbers, BAA number-to-title mappings, official names/titles/positions, ministry names/abbreviations, budget figures, statistical data.

**When to run this loop:**
- MANDATORY: Bills, resolutions, legislative briefers, guidebooks citing legislation, policy recommendations
- RECOMMENDED: Speeches (P5-P6 claims only), research outputs
- OPTIONAL: Transcripts (P5 name verification only)

---

## 2. Known Fabrication Patterns

These are the 10 patterns AI most frequently fabricates, extracted from 66 documented errors across 7 guidebooks. Every content skill must guard against them.

### Pattern 1: BOL Article Misattribution (13+ occurrences)

**What goes wrong**: The BOL has 18 articles (I-XVIII), not 13. Claude maps only 13 articles, causing cascading misattributions -- especially for Transition (cited as Art. VIII, actually Art. XVI), Special Development Fund (cited as Art. XII Sec. 10, actually Art. XIV Sec. 2), and Rehabilitation provisions.

**The most dangerous swaps**:
1. **Art. IX vs Art. X**: "Shari'ah" is Art. X, not Art. IX. Art. IX is "Basic Rights." (5 occurrences)
2. **Art. V vs Art. VI**: "Powers of Government" is Art. V, not Art. VI. Art. VI is "Intergovernmental Relations." (3 occurrences)
3. **Art. VII vs Art. VIII**: "Parliament" is in Art. VII. Art. VIII is "Wali," not "Transition." (3 occurrences)
4. **Art. VIII vs Art. XVI**: "Transition" is Art. XVI, not Art. VIII. Art. VIII is "Wali."
5. **Art. XII Sec. 10 vs Art. XIV Sec. 2**: "Special Development Fund" is Art. XIV, Sec. 2, not Art. XII, Sec. 10.
6. **Art. XII Sec. 9 vs Art. XII Sec. 15-16**: "Annual Block Grant" is Art. XII, Sec. 15-16, not Sec. 9.

**Correct answer**: See Section 8 (BOL 18-Article Map) for the complete mapping.

**Source to verify against**: `~/.gemini/skills/bangsamoro/references/bol-key-provisions.md` or `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/`

### Pattern 2: BAA Number Fabrication (5+ occurrences)

**What goes wrong**: Claude invents BAA number-to-title mappings that do not exist. The BAA index has 89 enacted BAAs and the numbering is chronological, not thematic.

**Errors found**:
| Wrong | Actual |
|-------|--------|
| BAA 8 = "Revenue Code" | BAA 8 = Bangsamoro Women Commission (BWC) |
| BAA 9 = "BHRC" | BAA 9 = Recruitment Agencies Regulation; BHRC = BAA 4 |
| BAA 10 = "Electoral Code" | BAA 10 = Youth Commission (BYC); Electoral Code = BAA 35 |
| BAA 11 = "Education Code" | BAA 11 = Power of Appointment; Education Code = BAA 18 |
| BAA 25 = "Environment Code" | BAA 25 = Hospital upgrade (verify against index) |
| BAA 45 = "Civil Service Code" | BAA 45 = Municipality of Kapalawan; Civil Service Code = BAA 17 |
| BAA 60 = "BEZA" | BEZA is created by BOL Art. XII, Sec. 6 directly, not by a BAA |
| BAA 86 = "SGA municipalities" | BAA 86 = Parliamentary District Seats Act; SGA municipalities = BAAs 41-48 |

**Key BAAs worth memorizing**:
| BAA | What It Is |
|-----|-----------|
| 4 | BHRC (Human Rights Commission) |
| 8 | BWC (Women Commission) |
| 10 | BYC (Youth Commission) |
| 13 | Bangsamoro Administrative Code |
| 17 | Bangsamoro Civil Service Code |
| 18 | Education Code |
| 35 | Electoral Code |
| 41-48 | 8 SGA Municipalities |
| 49 | Bangsamoro Local Governance Code |
| 64 | Indigenous Peoples' Affairs (MIPA) |
| 82 | Labor and Employment Code |
| 84 | Budget System Act |
| 86 | Parliamentary District Seats Act |

**Correct answer**: Always verify BAA numbers against the quick reference or index. Never assume a BAA number from the topic.

**Source to verify against**: `~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md` or `~/Vault/bangsamoro/bangsamoro-laws/index.md`

### Pattern 3: Ministry Abbreviation Errors (5 occurrences)

**What goes wrong**: Claude invents abbreviation variants that do not exist.

| Wrong | Correct |
|-------|---------|
| MOL | **MOLE** (Ministry of Labor and Employment) |
| MST | **MOST** (Ministry of Science and Technology) |
| MPWH | **MPW** (Ministry of Public Works) |

**Correct answer**: See Section 7 (Ministry Abbreviation Whitelist) for the complete list of 15 ministries.

**Source to verify against**: `~/.gemini/skills/bangsamoro/references/moa-structure.md`

### Pattern 4: Sulu Territorial Status

**What goes wrong**: Sulu listed as a BARMM province without caveat, or "6 provinces" stated instead of 5.

**Correct answer**:
- Sulu is **excluded from BARMM territory** per SC ruling in *Province of Sulu v. Medialdea* (G.R. Nos. 242255, 243246, 243693; Sept 9, 2024; finalized Nov 26, 2024)
- Sulu rejected the BOL by 54.3% in the 2019 plebiscite
- **EO 91** (July 30, 2025) realigned Sulu under Region IX
- BTA appointments from Sulu are NOT invalidated -- **doctrine of operative fact** protects prior acts
- The BOL still says 80 MPs (Art. VII, Sec. 6) -- the SC ruling did NOT change the BOL composition
- Tausug people remain culturally Bangsamoro regardless of the territorial ruling
- **BARMM has 5 provinces**: Lanao del Sur, Maguindanao del Norte, Maguindanao del Sur, Basilan, Tawi-Tawi

**Source to verify against**: Error log Pattern #4, SC ruling, EO 91

### Pattern 5: Shari'ah Court Naming Error

**What goes wrong**: "Shari'ah Appellate Court" used instead of the correct name.

**Correct answer**: The correct name is **Shari'ah High Court**. BOL Art. X, Sec. 7 establishes Shari'ah High Courts. The correct hierarchy: Shari'ah Circuit Courts, Shari'ah District Courts, **Shari'ah High Courts**. Never use "Appellate" for Shari'ah courts in the BARMM context.

**Source to verify against**: BOL Art. X, Sec. 7

### Pattern 6: ARMM Creation Date Misattribution

**What goes wrong**: ARMM attributed to the 1996 Final Peace Agreement (FPA).

**Correct answer**: ARMM was created by **Republic Act 6734 (1989)**, not by the 1996 FPA. The correct timeline:
1. RA 6734 (1989) -- created ARMM
2. 1996 FPA -- signed between GRP and MNLF
3. RA 9054 (2001) -- expanded and strengthened ARMM
4. RA 11054 (2018) -- replaced ARMM with BARMM

**Source to verify against**: Error log Pattern #6

### Pattern 7: Program Name Fabrication

**What goes wrong**: Claude invents program names, acronyms, or expansions that do not exist.

| Fabricated | Correct |
|-----------|---------|
| "ESKEY" scholarship program | Does not exist. Use **BASE/BASE-MERIT** (MOST) |
| "Al-Huda Madrasah Education" (AHME expansion) | AHME = **Access to Higher and Modern Education** |
| "CSC KIOSK" at kiosk.csc.gov.ph | Portal is called **CSC Job Portal** at csc.gov.ph/career |
| OHRAORA | **ORAOHRA** (Omnibus Rules on Appointments and Other Human Resource Actions) |

**Correct answer**: Never expand an acronym from guessing. If unsure, search official sources or flag as `[UNVERIFIED]`.

**Source to verify against**: Official agency websites, CSC issuances

### Pattern 8: Priority Code Count

**What goes wrong**: "Twelve priority codes" stated when there are only seven.

**Correct answer**: There are **7 priority codes** identified by the BOL (Art. XVI):
1. Administrative Code (BAA 13 -- enacted)
2. Civil Service Code (BAA 17 -- enacted)
3. Education Code (BAA 18 -- enacted)
4. Electoral Code (BAA 35 -- enacted)
5. Local Governance Code (BAA 49 -- enacted)
6. Revenue Code (pending)
7. Investment Code (pending)

Five enacted, two pending.

**Source to verify against**: BOL Art. XVI, BAA quick reference

### Pattern 9: BEZA Source Misattribution

**What goes wrong**: BEZA (Bangsamoro Economic Zone Authority) attributed to a BAA.

**Correct answer**: BEZA is created by **BOL Art. XII, Sec. 6** directly. It is not created by a separate BAA.

**Source to verify against**: BOL Art. XII, Sec. 6

### Pattern 10: Section Numbering in Multi-Chapter Documents

**What goes wrong**: Copy-paste artifacts cause chapter N sections to be numbered with the previous chapter's prefix (e.g., Chapter 14 sections numbered "13.1, 13.2...").

**Correct answer**: After writing each chapter, verify that all section numbers match the chapter number. Chapter N sections must be numbered N.1, N.2, etc.

**Source to verify against**: Visual inspection of each chapter

---

## 3. Authoritative Source File Paths

Every reference file used by the verification framework.

| File | What It Covers | Path |
|------|---------------|------|
| BOL key provisions | 18-article BOL structure, section numbers | `~/.gemini/skills/bangsamoro/references/bol-key-provisions.md` |
| BOL full text | Verbatim BOL transcription (5 chapter files) | `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` |
| BAA quick reference | All 89 BAAs with short titles by category | `~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md` |
| BAA full text | Verbatim BAA transcriptions | `~/Vault/bangsamoro/bangsamoro-laws/BAA-{N}.md` |
| BAA index | Master list of all BAAs | `~/Vault/bangsamoro/bangsamoro-laws/index.md` |
| Resolution classification | 556+ resolutions classified by type | `~/Vault/bangsamoro/bangsamoro-resolutions/resolution-classification.md` |
| BDP chapter summaries | 6 goals, 8 strategies, macro targets, sector data | `~/Vault/bangsamoro/bangsamoro-development/bdp-chapter-summaries.md` |
| BDP full chapters | 15 chapters of the 2nd BDP 2023-2028 | `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/` |
| BARMM officials | Current leadership, ministers, MPs (2025-2026) | `~/.gemini/skills/bangsamoro/references/barmm-officials-2025-2026.md` |
| MOA structure | 15 ministries, OCM, attached agencies, commissions | `~/.gemini/skills/bangsamoro/references/moa-structure.md` |
| Fact-check error log | 66 documented errors, 10 recurring patterns | `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md` |
| Author bio | Canonical author bio for all publications | `~/Vault/reference/author-bio-standard.md` |
| Verification framework | This document (canonical protocol) | `~/.gemini/skills/fact-checker/references/verification-framework.md` |

---

## 4. Three-Layer Protocol

### Layer 1: PREVENT (before writing)

The cheapest intervention. A subagent with loaded references will not fabricate.

| Step | Action | Time | Mandatory For |
|------|--------|------|---------------|
| **1a** | Invoke `/bangsamoro` to load domain context | 30 sec | Any BARMM content |
| **1b** | Read the fact-check error log at `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md` | 30 sec | Any BARMM content |
| **1c** | Fast research: WebSearch or check authoritative sources for recent developments on the topic (new BAAs, leadership changes, court rulings, updated statistics) | 2-5 min | Time-sensitive topics, governance, statistics |
| **1d** | Read authoritative reference files relevant to the topic (only what the topic touches -- not all files every time) | 1-2 min | Any content with P1-P7 claims |
| **1e** | Build a Fact Sheet: structured table of verified claims with source file paths -- this is the SOLE source of truth for writing | 5-10 min | Guidebooks (per chapter), bills, policy papers |
| **1f** | Include in every subagent prompt: fact sheet, reference file paths, 5 most dangerous fabrication patterns, and the rule "If not in your sources, write [UNVERIFIED]" (see Section 6 for template) | 1 min | Any work dispatching subagents |

### Layer 2: DETECT (after writing)

Enhanced `/fact-checker` runs after output is produced. One invocation covers all 10 priority categories in order.

| Step | Category | Check | Method |
|------|----------|-------|--------|
| **2a** | P1: Constitution | Every constitutional citation has correct article/section | Cross-check against Constitution source |
| **2b** | P2: BOL | Every BOL art/sec citation is correct (18-article map) | Cross-check against `bol-key-provisions.md` |
| **2c** | P3: Legislation | Every BAA number matches its actual title; every RA number exists | Cross-check against `baa-quick-reference.md` |
| **2d** | P4: Verbatim text | Every quoted legal provision is word-for-word accurate | Invoke `/legal-reviewer` VERIFY mode |
| **2e** | P5: Person names | Every named person has correct name spelling, title, and position | Check against `barmm-officials-2025-2026.md` |
| **2f** | P6: Institutions | Every ministry/agency name and abbreviation is correct | Check against `moa-structure.md` whitelist |
| **2g** | P7: Statistics | Every percentage, ratio, and count matches its source | Cross-check against BDP chapter summaries |
| **2h** | P8: Temporal | No outdated claims (Sulu, ARMM date, official positions, BAA count) | Scan for known patterns from error log |
| **2i** | P9: Frameworks | Author names and framework names are correct | Check against source material / bibliography |
| **2j** | P10: Citations | Every factual claim has a `[^N]` footnote; every footnote has a definition; no orphans | Automated scan |

**Output**: `FACT-CHECK-REPORT.md` with:
- Each claim: category, text, source checked against, status (VERIFIED / ERROR / UNVERIFIED)
- Organized by priority (P1 first, P10 last)
- Summary: total claims checked, verified count, error count, unverified count
- Severity labels: **CRITICAL** (P1-P4 errors), **HIGH** (P5-P8 errors), **MEDIUM** (P9-P10 errors)

**Mandatory actions after detection**:
- **CRITICAL errors**: Must be fixed before any output is generated (PDF, DOCX, etc.)
- **HIGH errors**: Must be fixed before publication
- **MEDIUM errors**: Should be fixed; may proceed with user approval if time-constrained

### Layer 3: CONFIRM (before publishing)

The human gate. No output is final until the user approves the fact-check report.

| Step | Action |
|------|--------|
| **3a** | Present the fact-check report to the user with summary statistics |
| **3b** | Fix all CRITICAL (P1-P4) and HIGH (P5-P8) errors |
| **3c** | Resolve all UNVERIFIED items (user provides source, claim is removed, or claim is verified via research) |
| **3d** | Re-run Layer 2 (Detect) on fixed sections to confirm fixes are clean |
| **3e** | Regenerate output (PDF/DOCX/final document) after all fixes |
| **3f** | User reviews and approves for publication |

---

## 5. Depth by Output Type

Not every output needs the same verification depth. The framework scales.

| Output Type | Layer 1 (Prevent) | Layer 2 (Detect) | Layer 3 (Confirm) | Total Time |
|-------------|-------------------|-------------------|-------------------|------------|
| **Guidebooks** | Full (1a-1f, per chapter) | Full (2a-2j, per chapter) | Full (3a-3f) | 30-60 min |
| **Bills** | Full (1a-1f) | Full (2a-2j) | Full (3a-3f) | 20-30 min |
| **Resolutions** | Full (1a-1f) | Full (2a-2j) | Full (3a-3f) | 20-30 min |
| **Policy papers** | Full (1a-1f) | Full (2a-2j) | Full (3a-3f) | 20-30 min |
| **CSW** | Full (1a-1f) | Full (2a-2j) | Full (3a-3f) | 20-30 min |
| **Speeches** | 1a-1d (no fact sheet) | 2b, 2c, 2e, 2f, 2h, 2j | 3a, 3b, 3f | 10-15 min |
| **Legislative briefers** | Full (1a-1f) | Full (2a-2j) | Full (3a-3f) | 20-30 min |
| **Training materials** | 1a-1d | 2b, 2c, 2e-2h, 2j | 3a, 3b, 3f | 15-20 min |
| **Transcripts** | 1a, 1d (officials list) | 2e, 2f only (names, institutions) | 3a, 3f | 5-10 min |
| **Research outputs** | 1c, 1d | 2g, 2i, 2j (statistics, frameworks, citations) | 3a, 3f | 10-15 min |
| **Vault notes** | None (unless factual) | Optional | None | 0 min |

---

## 6. Subagent Prompt Template

The following block must be included in every subagent dispatched for BARMM content. Copy it verbatim into subagent prompts, filling in the bracketed sections.

```
## VERIFICATION RULES (NON-NEGOTIABLE)

Before writing ANY factual claim, you MUST:
1. Check the Fact Sheet provided below for verified data
2. If citing a BAA: verify the number-to-title mapping against the BAA reference
3. If citing BOL: verify the article number (18 articles total -- Art. IX = Basic Rights, Art. X = Justice/Shari'ah, Art. XII = Fiscal Autonomy)
4. If naming a ministry: use ONLY these abbreviations: MAFAR, MBHTE, MENRE, MFBM, MOH, MHSD, MILG, MIPA, MOLE, MPOS, MPW, MOST, MSSD, MTIT, MOTC
5. If mentioning Sulu: add caveat about SC ruling (Sept 2024) excluding Sulu from BARMM
6. If you CANNOT verify a claim from your sources: write [UNVERIFIED] -- NEVER guess

Reference files you MUST read before writing:
- BOL key provisions: ~/.gemini/skills/bangsamoro/references/bol-key-provisions.md
- BAA quick reference: ~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md
- BARMM officials: ~/.gemini/skills/bangsamoro/references/barmm-officials-2025-2026.md
- MOA structure: ~/.gemini/skills/bangsamoro/references/moa-structure.md
- [Additional paths specific to this chapter's topic]

Known fabrication patterns to AVOID:
- BOL has 18 articles, not 13. Art. IX = Basic Rights. Art. X = Shari'ah/Justice.
- BAA 25 = Hospital upgrade, NOT Environment Code. BAA 60 = Memorial site, NOT BEZA.
- BEZA is created by BOL Art. XII Sec. 6, NOT by a separate BAA.
- ARMM was created by RA 6734 (1989), NOT by the 1996 FPA.
- There are 7 priority codes (not 12): Administrative, Civil Service, Education, Electoral, Local Governance, Revenue (pending), Investment (pending).

## FACT SHEET
[Insert verified claims table with source file paths here]
```

---

## 7. Ministry Abbreviation Whitelist

All 15 line ministries of the Bangsamoro Autonomous Region. Use ONLY these abbreviations. The OCM (Office of the Chief Minister) is not a ministry.

| # | Abbreviation | Full Name |
|---|-------------|-----------|
| 1 | **MAFAR** | Ministry of Agriculture, Fisheries, and Agrarian Reform |
| 2 | **MBHTE** | Ministry of Basic, Higher, and Technical Education |
| 3 | **MENRE** | Ministry of Environment, Natural Resources, and Energy |
| 4 | **MFBM** | Ministry of Finance, Budget, and Management |
| 5 | **MOH** | Ministry of Health |
| 6 | **MHSD** | Ministry of Human Settlements and Development |
| 7 | **MILG** | Ministry of Interior and Local Government |
| 8 | **MIPA** | Ministry of Indigenous Peoples' Affairs |
| 9 | **MOLE** | Ministry of Labor and Employment (NOT "MOL") |
| 10 | **MPOS** | Ministry of Public Order and Safety |
| 11 | **MPW** | Ministry of Public Works (NOT "MPWH") |
| 12 | **MOST** | Ministry of Science and Technology (NOT "MST") |
| 13 | **MSSD** | Ministry of Social Services and Development |
| 14 | **MTIT** | Ministry of Trade, Investments, and Tourism |
| 15 | **MOTC** | Ministry of Transportation and Communications |

**Common errors to watch for**: MOL (wrong -- use MOLE), MST (wrong -- use MOST), MPWH (wrong -- use MPW).

---

## 8. BOL 18-Article Map

Complete mapping of Republic Act No. 11054 (Bangsamoro Organic Law). The BOL has **18 articles**, not 13. Every BOL citation must be verified against this map.

| Article | Subject | Key Provisions | Common Wrong Attribution |
|---------|---------|----------------|--------------------------|
| **I** | Name and Purpose | Establishes the Bangsamoro Autonomous Region in Muslim Mindanao | -- |
| **II** | Bangsamoro Identity | Definition of Bangsamoro people, right to self-identification | -- |
| **III** | Territorial Jurisdiction | Geographic coverage, core territory, contiguous areas | -- |
| **IV** | General Principles and Policies | Guiding principles of governance | Often confused with Art. V (powers) |
| **V** | Powers of Government | 55 enumerated powers in Sec. 2 | Often swapped with Art. VI |
| **VI** | Intergovernmental Relations | National-Bangsamoro relations, concurrent/shared powers | Often swapped with Art. V |
| **VII** | Bangsamoro Government | Parliament (Sec. 1-6), Chief Minister (Sec. 7-9), Cabinet (Sec. 10-12) | Often cited as Art. VIII |
| **VIII** | Wali | Ceremonial head of the Bangsamoro Government | Often cited as "Parliament" or "Transition" |
| **IX** | Basic Rights | Including IP rights (Sec. 3), Settler communities (Sec. 15) | Often cited as "Shari'ah" |
| **X** | Justice System | Shari'ah courts: Circuit, District, **High Court** (Sec. 7) | Often attributed to Art. IX |
| **XI** | National Defense and Security, Public Order and Safety, and Coast Guard Services | Security sector provisions | Often mislabeled as "Economy" |
| **XII** | Fiscal Autonomy | Block Grant (Sec. 15-16), annual revenue share, taxing powers; BEZA (Sec. 6), Special Development Fund (Sec. 25) | Block Grant wrongly cited as Sec. 9 |
| **XIII** | Regional Economy and Patrimony | Natural resources, trade, investment | Often mislabeled as "Transitory Provisions" |
| **XIV** | Rehabilitation and Development | Special Development Fund (Sec. 2), normalization, decommissioning | Often omitted; SDF wrongly cited as Art. XII Sec. 10 |
| **XV** | Plebiscite | Ratification process, geographic components | Often mislabeled as "Normalization" |
| **XVI** | Transition | BTA mandate, timeline, 7 priority codes, transition authority | Often cited as Art. VIII |
| **XVII** | Amendments | Process for amending the BOL | Often omitted entirely |
| **XVIII** | Final Provisions | Effectivity, separability, repealing clauses | Often mislabeled as just "Effectivity" |

**Critical section-level details to remember**:
- **Block Grant** = Art. XII, Sec. 15-16 (NOT Sec. 9)
- **Special Development Fund** = Art. XIV, Sec. 2 (NOT Art. XII, Sec. 10)
- **BEZA** = Art. XII, Sec. 6 (NOT a separate BAA)
- **Shari'ah High Court** = Art. X, Sec. 7 (NOT "Appellate Court")
- **55 enumerated powers** = Art. V, Sec. 2
- **7 priority codes** = Art. XVI (5 enacted, 2 pending)
- **80 MPs** = Art. VII, Sec. 6 (unchanged by SC Sulu ruling)

---

## Update Protocol

This document is maintained alongside the fact-check error log. When new error patterns are discovered:

1. Append new errors to `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md`
2. If a new pattern emerges (3+ occurrences), add it to Section 2 of this document
3. Update the subagent prompt template in Section 6 if the top 5 most dangerous patterns change
4. Update Section 7 (Ministry Whitelist) if ministries are reorganized
5. Update Section 8 (BOL Map) only if the BOL is amended (requires Art. XVII process)

Every 10 guidebooks (or quarterly), review the error log for patterns that have been eliminated vs. patterns that persist. Patterns that no longer appear after 5 consecutive documents without occurrence can be moved to an "Archived Patterns" section in the error log.
