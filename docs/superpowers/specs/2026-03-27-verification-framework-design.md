# Universal Verification Framework — Design Spec

**Date**: 2026-03-27
**Author**: Saidamen R. Mambayao (with Claude Code)
**Problem**: 50 documented errors across 6 guidebooks (31 critical). AI fabricates facts and dresses them as authoritative citations. The same error patterns recur independently across documents.
**Solution**: Three-layer verification framework (Prevent, Detect, Confirm) embedded into all content skills via an enhanced `/fact-checker` and a reference document.
**Scope**: All work requiring accuracy — guidebooks, bills, resolutions, speeches, briefers, transcripts, research, policy papers, training materials, vault notes with factual claims.

---

## 1. Verification Taxonomy (P1-P10)

Every factual claim falls into one of ten priority categories. Higher priority = higher risk of institutional damage if wrong. Every claim in P1-P10 requires a `[^N]` footnote in Feliciano 10th Ed. format. No exception.

| Priority | Category | What to verify | Authoritative Source | Citation Format |
|----------|----------|---------------|---------------------|-----------------|
| **P1** | Constitutional provisions | Article, section numbers; verbatim text | Constitution transcription | `Const. art. N, sec. N.` |
| **P2** | BOL provisions | Article (18 total), section numbers; verbatim text | `bol-key-provisions.md`, BOL transcription (5 files) | `Rep. Act No. 11054, art. N, sec. N.` |
| **P3** | Legislative references | BAA number-to-title mapping; RA numbers; Resolution numbers | `baa-quick-reference.md`, `INDEX.md`, resolution classification | `BAA No. N.` / `Rep. Act No. N.` |
| **P4** | Verbatim legal text | Word-for-word accuracy of quoted provisions | BOL transcription, BAA full text, RA source PDFs | Blockquote + footnote |
| **P5** | Proper nouns — persons | Names, middle initials, current titles, current positions | `barmm-officials-2025-2026.md` | Full name + title on first mention |
| **P6** | Proper nouns — institutions | Ministry names, abbreviations, attached agencies, commissions | `moa-structure.md`, error log | Correct abbreviation per whitelist |
| **P7** | Statistical data | Percentages, ratios, counts, monetary values | BDP chapter summaries, PSA data | `2nd BDP 2023-2028, Ch. N.` |
| **P8** | Temporal claims | Facts that may be outdated due to court rulings, elections, new legislation, leadership changes | Error log (Sulu SC ruling 2024, EO 91 2025), WebSearch | Dated citation + caveat if contested |
| **P9** | Attributed frameworks | Author names, framework names, publication details | Source books, bibliography | `Author, *Title* (City: Publisher, Year).` |
| **P10** | All other factual claims | Dates, events, places, counts, causal claims | Multiple sources | Appropriate citation per claim type |

### Known Fabrication Patterns (from 50 documented errors)

These are the patterns AI most frequently fabricates. Every content skill must guard against them:

| Pattern | What goes wrong | Correct reference |
|---------|----------------|-------------------|
| BOL article swap | Art. IX (Basic Rights) cited as Shari'ah; Art. X (Justice/Shari'ah) cited as Basic Rights | `bol-key-provisions.md` — 18 articles, not 13 |
| BAA number fabrication | Invented mappings (BAA 25 = "Environment Code") | `baa-quick-reference.md` — 89 enacted BAAs |
| Ministry abbreviation | MOLE written as MOL, MOST as MST, MPW as MPWH | `moa-structure.md` — 15 ministries, exact abbreviations |
| Sulu territorial status | Listed as BARMM province without SC ruling caveat | SC ruling Sept 2024, EO 91 July 2025 — Sulu excluded |
| Shari'ah court name | "Shari'ah Appellate Court" | **Shari'ah High Court** (BOL Art. X, Sec. 7) |
| ARMM creation date | Attributed to 1996 FPA | **RA 6734 (1989)** created ARMM |
| Program name fabrication | Invented acronyms (ESKEY scholarship, KIOSK portal) | Verify against official program lists |
| Priority code count | "twelve priority codes" | **Seven** identified by BOL; 5 enacted, 2 pending |
| BEZA source | Attributed to a BAA | Created by **BOL Art. XII, Sec. 6** directly |
| Section numbering | Chapter 14 sections numbered "13.1, 13.2..." | Always match section prefix to chapter number |

---

## 2. Three Verification Layers

### Layer 1: PREVENT (before writing)

The cheapest intervention. A subagent with loaded references will not fabricate.

| Step | Action | Time | Mandatory for |
|------|--------|------|---------------|
| **1a** | Invoke `/bangsamoro` to load domain context | 30 sec | Any BARMM content |
| **1b** | Read the fact-check error log at `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md` | 30 sec | Any BARMM content |
| **1c** | Fast research: WebSearch or check authoritative sources for recent developments on the topic (new BAAs, leadership changes, court rulings, updated statistics) | 2-5 min | Time-sensitive topics, governance, statistics |
| **1d** | Read authoritative reference files relevant to the topic (only what the topic touches — not all files every time) | 1-2 min | Any content with P1-P7 claims |
| **1e** | Build a Fact Sheet: structured table of verified claims with source file paths — this is the SOLE source of truth for writing | 5-10 min | Guidebooks (per chapter), bills, policy papers |
| **1f** | Include in every subagent prompt: fact sheet, reference file paths, 5 most dangerous fabrication patterns, and the rule "If not in your sources, write [UNVERIFIED]" | 1 min | Any work dispatching subagents |

**Authoritative reference files (canonical list):**

| File | What it covers | Path |
|------|---------------|------|
| BOL key provisions | 18-article BOL structure, section numbers | `~/.claude/skills/bangsamoro/references/bol-key-provisions.md` |
| BOL full text | Verbatim BOL transcription | `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` (5 files) |
| BAA quick reference | All 89 BAAs with short titles by category | `~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md` |
| BAA full text | Verbatim BAA transcriptions | `~/Vault/bangsamoro/bangsamoro-laws/BAA-{N}.md` |
| Resolution classification | 556+ resolutions classified by type | `~/Vault/bangsamoro/bangsamoro-resolutions/resolution-classification.md` |
| BDP chapter summaries | 6 goals, 8 strategies, macro targets, sector data | `~/Vault/bangsamoro/bangsamoro-development/bdp-chapter-summaries.md` |
| BDP full chapters | 15 chapters of the 2nd BDP 2023-2028 | `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/` |
| BARMM officials | Current leadership, ministers, MPs | `~/.claude/skills/bangsamoro/references/barmm-officials-2025-2026.md` |
| MOA structure | 15 ministries, OCM, attached agencies, commissions | `~/.claude/skills/bangsamoro/references/moa-structure.md` |
| Fact-check error log | 50 documented errors, 10 recurring patterns | `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md` |
| Author bio | Canonical author bio for all publications | `~/Vault/reference/author-bio-standard.md` |

**Subagent prompt template (mandatory inclusion):**

```
## VERIFICATION RULES (NON-NEGOTIABLE)

Before writing ANY factual claim, you MUST:
1. Check the Fact Sheet provided below for verified data
2. If citing a BAA: verify the number-to-title mapping against the BAA reference
3. If citing BOL: verify the article number (18 articles total — Art. IX = Basic Rights, Art. X = Justice/Shari'ah, Art. XII = Fiscal Autonomy)
4. If naming a ministry: use ONLY these abbreviations: MAFAR, MBHTE, MENRE, MFBM, MOH, MHSD, MILG, MIPA, MOLE, MPOS, MPW, MOST, MSSD, MTIT, MOTC
5. If mentioning Sulu: add caveat about SC ruling (Sept 2024) excluding Sulu from BARMM
6. If you CANNOT verify a claim from your sources: write [UNVERIFIED] — NEVER guess

Reference files you MUST read before writing:
- [specific paths for this chapter's topic]

Known fabrication patterns to AVOID:
- BOL has 18 articles, not 13. Art. IX = Basic Rights. Art. X = Shari'ah/Justice.
- BAA 25 = Hospital upgrade, NOT Environment Code. BAA 60 = Memorial site, NOT BEZA.
- BEZA is created by BOL Art. XII Sec. 6, NOT by a separate BAA.
- ARMM was created by RA 6734 (1989), NOT by the 1996 FPA.
- There are 7 priority codes (not 12): Administrative, Civil Service, Education, Electoral, Local Governance, Revenue (pending), Investment (pending).
```

### Layer 2: DETECT (after writing)

Enhanced `/fact-checker` runs after output is produced. One invocation covers all 10 priority categories in order.

| Step | Category | Check | Method |
|------|----------|-------|--------|
| **2a** | P1: Constitution | Every constitutional citation has correct article/section | Cross-check against Constitution source |
| **2b** | P2: BOL | Every BOL art/sec citation is correct (18-article map) | Cross-check against `bol-key-provisions.md` |
| **2c** | P3: Legislation | Every BAA number matches its actual title; every RA number exists | Run `verify-references.py` logic against `baa-quick-reference.md` |
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
- Severity: CRITICAL (P1-P4 errors), HIGH (P5-P8 errors), MEDIUM (P9-P10 errors)

**Mandatory actions after detection:**
- **CRITICAL errors**: Must be fixed before any output is generated (PDF, DOCX, etc.)
- **HIGH errors**: Must be fixed before publication
- **MEDIUM errors**: Should be fixed; may proceed with user approval if time-constrained

### Layer 3: CONFIRM (before publishing)

The human gate. No output is final until the user approves the fact-check report.

| Step | Action |
|------|--------|
| **3a** | Present the fact-check report to the user with summary statistics |
| **3b** | Fix all CRITICAL and HIGH errors |
| **3c** | Resolve all UNVERIFIED items (user provides source, claim is removed, or claim is verified via research) |
| **3d** | Re-run Layer 2 (Detect) on fixed sections to confirm fixes are clean |
| **3e** | Regenerate output (PDF/DOCX/final document) after all fixes |
| **3f** | User reviews and approves for publication |

---

## 3. Depth by Output Type

Not every output needs the same verification depth. The framework scales.

| Output Type | Layer 1 (Prevent) | Layer 2 (Detect) | Layer 3 (Confirm) | Total Time |
|-------------|-------------------|-------------------|-------------------|------------|
| **Guidebooks** | Full (1a-1f, per chapter) | Full (2a-2j, per chapter) | Full (3a-3f) | 30-60 min |
| **Bills, resolutions** | Full (1a-1f) | Full (2a-2j) | Full (3a-3f) | 20-30 min |
| **Policy papers, CSW** | Full (1a-1f) | Full (2a-2j) | Full (3a-3f) | 20-30 min |
| **Speeches** | 1a-1d (no fact sheet) | 2b, 2c, 2e, 2f, 2h, 2j | 3a, 3b, 3f | 10-15 min |
| **Legislative briefers** | Full (1a-1f) | Full (2a-2j) | Full (3a-3f) | 20-30 min |
| **Training materials** | 1a-1d | 2b, 2c, 2e-2h, 2j | 3a, 3b, 3f | 15-20 min |
| **Transcripts** | 1a, 1d (officials list) | 2e, 2f only (names, institutions) | 3a, 3f | 5-10 min |
| **Research outputs** | 1c, 1d | 2g, 2i, 2j (statistics, frameworks, citations) | 3a, 3f | 10-15 min |
| **Vault notes** | None (unless factual) | Optional | None | 0 min |

---

## 4. Skill Integration Map

How each content skill incorporates the three layers:

### `/guidebook-writer`

| Phase | Verification Layer | What happens |
|-------|-------------------|-------------|
| Phase 1 (Scope) | — | Interview, no factual claims yet |
| Phase 2 (Plan) | — | TOC and structure, no factual claims yet |
| Phase 3 (Research) | **PREVENT (1a-1f)** | `/bangsamoro` invoked, error log read, fast research, fact sheets built per chapter |
| Phase 4 (Draft) | Inline | Write from fact sheets only. Every claim gets `[^N]` as written. Subagent prompts include verification template. |
| Phase 4b (Verify) | **DETECT (2a-2j)** | Enhanced `/fact-checker` on every chapter. `verify-references.py` runs as sub-step. |
| Phase 5 (Review) | **DETECT continued** | `/legal-reviewer` for verbatim text (2d). QA report for internal consistency. |
| Pre-Build | **CONFIRM (3a-3f)** | User reviews fact-check report. All CRITICAL/HIGH errors fixed. Re-detect on fixed sections. |
| Phase 6 (Build) | — | Generate PDF/DOCX only after CONFIRM passes |

### `/bill-drafter`

| Stage | Verification Layer |
|-------|-------------------|
| Before drafting | **PREVENT**: `/bangsamoro`, error log, fast research on bill topic, verify all BAAs/BOL provisions to be cited |
| During drafting | Inline: every provision cited with `[^N]`, every BOL reference verified against source |
| After drafting | **DETECT**: enhanced `/fact-checker` on full bill text |
| Before filing | **CONFIRM**: user reviews report, fixes applied |

### `/resolution-drafter`

Same as `/bill-drafter`, with additional check on WHEREAS clause factual claims (every "WHEREAS" claim is a P7-P10 assertion that needs verification).

### `/speech-writer`

| Stage | Verification Layer |
|-------|-------------------|
| Before writing | **PREVENT**: verify speaker name/title, verify all BAAs/resolutions to be cited, fast research on topic |
| After writing | **DETECT**: names (2e), institutions (2f), legislation (2c), temporal (2h), citations (2j) |
| Before delivery | **CONFIRM**: user reviews |

### `/legislative-briefer` and `/csw`

Same as `/guidebook-writer` Phase 3-5, applied to the single document.

### `/youtube-transcriber`

| Stage | Verification Layer |
|-------|-------------------|
| After transcription | **DETECT**: verify all person names against officials list (2e), verify institution names (2f) |
| Before publishing | **CONFIRM**: user reviews transcript |

### `/policy-recommendation` and `/policy-paper`

Same as `/bill-drafter` — full three layers.

### `/training-assistant`

| Stage | Verification Layer |
|-------|-------------------|
| Before writing | **PREVENT**: domain context, error log, verify all examples from real BAAs/resolutions |
| After writing | **DETECT**: legislation (2c), names (2e), institutions (2f), statistics (2g), temporal (2h), citations (2j) |
| Before production | **CONFIRM**: user reviews |

---

## 5. Enhanced `/fact-checker` Specification

The existing `/fact-checker` skill is enhanced to incorporate:

### New capabilities (add to existing skill)

1. **BAA cross-reference check**: Extract every `BAA No. N` / `BAA N` reference → verify number-to-title against `baa-quick-reference.md` → report MATCH/MISMATCH/NOT_FOUND

2. **BOL article map verification**: Extract every BOL article/section citation → verify against 18-article reference → flag known swaps (Art. IX vs X, Art. V vs VI, Art. VII vs VIII, Art. VIII vs XVI, Art. XII sec. 9 vs secs. 15-16)

3. **Known error pattern scan**: Read `fact-check-error-log.md` → scan document for any text matching documented patterns → flag with "KNOWN ERROR PATTERN: [pattern name]"

4. **Ministry abbreviation whitelist**: Accept ONLY: MAFAR, MBHTE, MENRE, MFBM, MOH, MHSD, MILG, MIPA, MOLE, MPOS, MPW, MOST, MSSD, MTIT, MOTC → flag any variant (MOL, MST, MPWH, etc.)

5. **Citation completeness check**: Scan body text for percentages, named persons, BAA/BOL references, dates → flag any without a `[^N]` footnote on the same sentence

6. **Temporal validation**: Scan for "Sulu" without SC ruling caveat, "ARMM" with wrong creation date, "6 provinces" (now 5), outdated official positions → flag with "TEMPORAL: may be outdated"

7. **Priority-ordered reporting**: Report findings in P1-P10 order with severity labels (CRITICAL/HIGH/MEDIUM)

### What stays the same

- Names and titles verification against officials reference
- Dates and event verification
- Statistics verification against BDP
- Web search for items not in local sources
- `FACT-CHECK-REPORT.md` output format

### Integration of `verify-references.py`

The script's logic is absorbed into `/fact-checker` step 2c. The standalone script remains available for quick runs, but the full `/fact-checker` invocation includes its checks automatically.

---

## 6. Reference Document Location

The framework document lives at: `~/.claude/skills/fact-checker/references/verification-framework.md`

It contains:
1. The verification taxonomy (P1-P10 table)
2. The known fabrication patterns table (updated from error log)
3. The authoritative source file paths
4. The subagent prompt template
5. The three-layer protocol with steps
6. The depth-by-output-type table

Every content skill's instructions include a line:
```
Before producing content, read `~/.claude/skills/fact-checker/references/verification-framework.md` and follow the three-layer protocol appropriate to your output type.
```

---

## 7. Error Log Maintenance

The fact-check error log at `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md` is a living document.

**Update protocol:**
- After every `/fact-checker` run that finds errors, append new errors to the log
- Categorize by pattern (add to existing pattern or create new pattern)
- Include: which document, which claim, what was wrong, what the correct answer is
- Update the "Known Fabrication Patterns" table in the verification framework reference document

**Review protocol:**
- Every 10 guidebooks (or quarterly), review the log for patterns that have been eliminated vs. patterns that persist
- Patterns that no longer appear after 5 consecutive documents without occurrence can be moved to an "Archived Patterns" section

---

## 8. Success Metrics

The framework succeeds when:

| Metric | Target | How to measure |
|--------|--------|---------------|
| BAA fabrications | 0 per document | `verify-references.py` MISMATCH count |
| BOL article errors | 0 per document | Fact-check report P2 errors |
| Ministry abbreviation errors | 0 per document | Whitelist check |
| Sulu territorial errors | 0 per document | Temporal scan |
| Chapters without footnotes | 0 per guidebook | Citation completeness check |
| Known error pattern recurrence | 0 | Error log scan matches |
| User-caught errors post-publication | Decreasing trend | User feedback |

---

## 9. Implementation Deliverables

| # | Deliverable | Description |
|---|-------------|-------------|
| 1 | Reference document | `~/.claude/skills/fact-checker/references/verification-framework.md` — the canonical framework |
| 2 | Enhanced `/fact-checker` skill | Updated `~/.claude/skills/fact-checker/skill.md` with new capabilities (BAA cross-ref, BOL map, known patterns, abbreviation whitelist, citation completeness, temporal validation, priority-ordered reporting) |
| 3 | Subagent prompt template | Included in the reference document; referenced by all content skills |
| 4 | Content skill updates | One-line addition to each content skill: "Read verification-framework.md and follow the protocol" |
| 5 | Global CLAUDE.md update | Add verification framework reference to the Global Rules section |
| 6 | Memory update | Save the framework as a feedback memory for cross-project persistence |
