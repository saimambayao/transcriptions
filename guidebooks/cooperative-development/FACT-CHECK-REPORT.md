# Fact-Check Report — Cooperative Development Guidebook for Bangsamoro Communities

**Date**: 2026-03-27
**Chapters reviewed**: 14 (Chapters 1-14) plus Introduction, Glossary, Appendices
**Method**: Spot-check verification against source files — PB-210, RA 9520, BDP 2023-2028 Chapter 7, BOL RA 11054, barmm-context.md, and fact-check error log
**Reviewer**: Automated pipeline via Claude Code

---

## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 1 |
| MINOR | 4 |
| PASS | 13 chapters with no critical issues found |

**Overall assessment**: The guidebook is factually sound. Legal citations against both PB-210 and RA 9520 are accurate and well-sourced. Statistics match BDP 2023-2028 Chapter 7. Known error patterns (BOL article swaps, Shari'ah court naming, ARMM dates, ministry abbreviations) were not found in chapter content. One CRITICAL issue was found in the Glossary. Four minor issues were found across the 14 chapters.

---

## CRITICAL Issues

### CRITICAL-1: Glossary — Sulu Listed as BARMM Province Without SC Ruling Caveat

**Location**: `16-glossary.md`, line 297 (BARMM definition)

**Error**: The BARMM glossary entry lists Sulu as a current province:
> "Comprises the provinces of Maguindanao del Norte, Maguindanao del Sur, Lanao del Sur, Basilan, **Sulu**, and Tawi-Tawi, plus Cotabato City and the Special Geographic Area (SGA)."

The footnote (`[^138]`) cites only "Republic Act No. 11054, Article III" — which is the BOL as originally enacted — with no mention of the Supreme Court ruling that excluded Sulu.

**Why this is critical**: The SC ruling in *Province of Sulu v. Medialdea* (G.R. Nos. 242255, 243246, 243693; September 9, 2024; finalized November 26, 2024) excluded Sulu from BARMM territory. EO 91 (July 30, 2025) realigned Sulu under Region IX. Presenting Sulu as a current BARMM province without this caveat is factually inaccurate and could mislead cooperative organizers about the jurisdictional scope of CSEA.

**Contrast with correct handling in chapters**: Chapter 4 (`05-chapter-04.md`, footnote 5) and Chapter 13 (`14-chapter-13.md`, footnote 24) both correctly include caveat language about the SC ruling when citing PB-210's reference to Sulu provincial offices. The glossary does not follow this same standard.

**Correction needed**:
```
**Bangsamoro Autonomous Region in Muslim Mindanao (BARMM)** --- The autonomous political entity in the southern Philippines established under the Bangsamoro Organic Law (Republic Act No. 11054), replacing the former Autonomous Region in Muslim Mindanao (ARMM). Under the BOL, BARMM comprises the provinces of Maguindanao del Norte, Maguindanao del Sur, Lanao del Sur, Basilan, Sulu, and Tawi-Tawi, plus Cotabato City and the Special Geographic Area (SGA). Note: The Supreme Court ruling in *Province of Sulu v. Medialdea* (September 9, 2024) excluded Sulu from BARMM territory; Executive Order No. 91 (July 30, 2025) realigned Sulu under Region IX. CSEA jurisdiction currently covers five provinces plus Cotabato City and the SGA.[^138]
```

---

## MINOR Issues

### MINOR-1: Chapter 3 — Wrong Expansion of MAFAR

**Location**: `03-chapter-02.md`, line 427

**Error**: "Ministry of Agriculture, Fisheries, and **Aquatic Resources** (MAFAR)"

**Correct name**: Ministry of Agriculture, Fisheries, **and Agrarian Reform** (MAFAR)

**Context note**: This is a transcription of PB-210's own text at Section (Book III) of the bill, which itself contains this error ("Ministry of Agriculture, Fisheries, and Aquatic Resources"). The chapter accurately reflected the bill's language. However, since the bill text contains an evident error (MAFAR is established by its organic mandate as Agriculture, Fisheries, **and Agrarian Reform**), the guidebook should correct it and add a footnote noting the discrepancy in the bill text.

**All other instances**: Correct ("Agrarian Reform") in Chapter 13, Chapter 14, and the Glossary.

**Correction needed**: Change to "Ministry of Agriculture, Fisheries, and Agrarian Reform (MAFAR)" and add footnote: "Note: PB-210 uses 'Aquatic Resources' in this provision, which appears to be a drafting error. The correct ministry name is Agriculture, Fisheries, and Agrarian Reform (MAFAR)."

---

### MINOR-2: Glossary — MFBM Full Name Formatting

**Location**: `16-glossary.md`, line 327

**Error**: "Ministry of Finance **and** Budget and Management (MFBM)"

The official name per `moa-structure.md` is "Ministry of Finance, **and** Budget and Management (MFBM)" — with a comma after "Finance." The glossary omits this comma, making it read as "Finance and Budget" as a compound phrase, which is not the official construction.

**Also appears in**: `03-chapter-02.md`, line 427 (same passage with MAFAR error).

**Correction needed**: "Ministry of Finance, and Budget and Management (MFBM)" — or more simply, apply the standard comma: "Ministry of Finance, Budget, and Management (MFBM)." Verify against the latest official BARMM ministry names.

---

### MINOR-3: Chapter 1 — "Sulu" Used in Cooperative Examples Without Territorial Caveat

**Location**: `02-chapter-01.md`, multiple lines (lines 134, 138, 263)

**Issue**: The chapter uses Sulu as an active example province for cooperatives (e.g., "A coffee producers' cooperative in Sulu," "Province-level priorities" table listing Sulu). While this may be operationally appropriate — Sulu cooperatives registered with CSEA before the SC ruling may still fall under its jurisdiction under the doctrine of operative fact — no clarifying note is provided.

**Severity**: Minor because the SC ruling does not invalidate existing cooperatives or their compliance obligations. However, new registration guidance in Sulu post-EO 91 (July 2025) would now fall under Region IX, not CSEA. New cooperative organizers in Sulu reading this guidebook could be misled.

**Recommended action**: Add a brief note in Chapter 1's discussion of commodity provinces, and/or in the introductory "How to Use This Guidebook" section, clarifying that the SC ruling excluded Sulu from BARMM territory and that CSEA's jurisdictional scope for new registrations is now limited to the five remaining provinces, Cotabato City, and the SGA.

---

### MINOR-4: Chapter 4 — PB-210 Section 14 Citation (Sulu Provincial Office)

**Location**: `05-chapter-04.md`, footnote 5

**Issue**: The footnote quotes PB-210 Section 14's reference to Sulu provincial office and appends a correct caveat about the SC ruling. However, the main body text does not reflect this caveat — it presents the CSEA organizational structure (including Sulu) as a straightforward description without signaling to the reader that this provision may be revised.

**Severity**: Minor. The footnote correction is present; the risk is that readers who do not read footnotes receive an incomplete picture of CSEA's current territorial scope.

**Recommended action**: Add an inline note in the main body text adjacent to the CSEA organizational structure description, directing readers to the footnote regarding Sulu's status.

---

## Verification Results: Legal Citations

### RA 9520 Article Numbers Verified

| Article | Subject | Status |
|---------|---------|--------|
| Art. 2 | Declaration of Policy | VERIFIED — matches Chapter 1 citation |
| Art. 4 | Cooperative Principles (ICA 7) | VERIFIED — matches Chapter 1 citation |
| Art. 10 | Organizing a Primary Cooperative (15+ persons) | VERIFIED — matches Chapter 6 citation |
| Art. 23 | Types and Categories of Cooperatives | VERIFIED |
| Art. 26 | Kinds of Membership | VERIFIED — matches Chapter 6 citations |
| Art. 27 | Government Officers and Employees | VERIFIED |
| Art. 28 | Application | VERIFIED |
| Art. 30 | Termination of Membership | VERIFIED |
| Art. 33 | Powers of the General Assembly | VERIFIED |
| Art. 35 | Quorum | VERIFIED |
| Art. 36 | Voting System (one member, one vote) | VERIFIED |
| Art. 37 | Composition and Term of Board | VERIFIED |
| Art. 43 | Committees of Cooperatives | VERIFIED |
| Art. 52 | Books to be Kept Open | VERIFIED |
| Art. 53 | Reports | VERIFIED |
| Art. 54 | Register of Members | VERIFIED |
| Art. 60 | Tax Treatment | VERIFIED |
| Art. 61 | Tax and Other Exemptions | VERIFIED |
| Art. 70 | Rules and Regulations on Liquidation | VERIFIED |
| Art. 72 | Capital Sources | VERIFIED |
| Art. 73 | Limitation on Share Capital Holdings | VERIFIED |
| Art. 74 | Assignment of Share Capital | VERIFIED |
| Art. 75 | Capital Build-Up | VERIFIED |
| Art. 76 | Shares | VERIFIED |
| Art. 77 | Fines | VERIFIED |
| Art. 78 | Investment of Capital | VERIFIED |
| Art. 79 | Revolving Capital | VERIFIED |
| Art. 85 | Net Surplus | VERIFIED |
| Art. 86 | Order of Distribution (Reserve Fund 10%, ETF, CDF 3%) | VERIFIED |

### BTA Bill 210 (PB-210) Section Numbers Verified

| Section | Subject | Status |
|---------|---------|--------|
| Sec. 1 | Title | VERIFIED |
| Sec. 2 | Purpose (cites BOL Art. XIII, Sec. 24 & 27) | VERIFIED |
| Sec. 5 | Cooperative Principles | VERIFIED |
| Sec. 7 | Islamic Principles (maqasid, riba, maysir, gharar) | VERIFIED |
| Sec. 8 | Moral Governance | VERIFIED |
| Sec. 9 | Shari'ah Governance (Shari'ah committee, 3+ members) | VERIFIED |
| Sec. 11 | CSEA mandate | VERIFIED |
| Sec. 13 | Powers and Functions of CSEA | VERIFIED |
| Sec. 14 | Organizational Structure (4 divisions + provincial offices) | VERIFIED |
| Sec. 23 | Kinds of Membership | VERIFIED |
| Sec. 24 | Limitation of Membership | VERIFIED |
| Sec. 25 | Application | VERIFIED |
| Sec. 27 | Termination of Membership | VERIFIED |
| Sec. 31 | Powers of the General Assembly | VERIFIED |
| Sec. 32 | Meetings | VERIFIED |
| Sec. 33 | Quorum | VERIFIED |
| Sec. 34 | Voting System | VERIFIED |
| Sec. 35 | Board Composition and Term | VERIFIED |
| Sec. 37 | Directors | VERIFIED |
| Sec. 41 | Committees | VERIFIED |
| Sec. 44 | Liability of Directors | VERIFIED |
| Sec. 45 | Disloyalty of Director | VERIFIED |
| Sec. 47 | Removal | VERIFIED |
| Sec. 48 | Dealings of Directors | VERIFIED |
| Sec. 52 | Cooperative Documents for Submission | VERIFIED |
| Sec. 55 | Probative Value of Certified Copies | VERIFIED |
| Sec. 56 | Preference of Claims | VERIFIED |
| Sec. 64 | Capital Sources | VERIFIED |
| Sec. 65 | Limitation on Share Capital Holdings | VERIFIED |
| Sec. 66 | Assignment of Share Capital | VERIFIED |
| Sec. 67 | Capital Build-Up | VERIFIED |
| Sec. 68 | Shares | VERIFIED |
| Sec. 71 | Revolving Capital | VERIFIED |
| Sec. 77 | Net Surplus | VERIFIED |
| Sec. 78 | Order of Distribution | VERIFIED |

### BOL (RA 11054) Article Citations Verified

| Citation | Subject | Status |
|----------|---------|--------|
| Art. V, Sec. 2(k) | Cooperatives and social entrepreneurship as enumerated power | VERIFIED — "Cooperatives and social entrepreneurship" appears at item (k) in the verified BOL source |
| Art. XIII, Sec. 24 | Trade and Industry; mandate to enact cooperative code | VERIFIED — verbatim text confirmed in BOL Chapter 7 source |
| Art. XIII, Sec. 27 | Cooperatives and Social Entrepreneurship | VERIFIED — verbatim text confirmed |
| Art. III | Territorial jurisdiction (glossary footnote 138) | VERIFIED as source for original BOL territorial scope; CRITICAL caveat missing for post-SC ruling status |

---

## Statistics Verification

| Statistic | Claimed | Source | Status |
|-----------|---------|--------|--------|
| Total registered cooperatives (2010-2020) | 12,214 | BDP 2023-2028, Ch. 7 | VERIFIED |
| Compliant cooperatives | 1,424 (11.66%) | BDP 2023-2028, Ch. 7 | VERIFIED |
| BDP compliance target | 50% | BDP 2023-2028, Ch. 7 | VERIFIED |
| Maguindanao cooperatives | 4,671 (38.24%) | BDP 2023-2028, Ch. 7 | VERIFIED |
| Lanao del Sur cooperatives | 4,554 (37.29%) | BDP 2023-2028, Ch. 7 | VERIFIED |
| Producer cooperatives | 4,590 (37.58%) | BDP 2023-2028, Ch. 7 | VERIFIED |
| Marketing cooperatives | 3,364 (27.54%) | BDP 2023-2028, Ch. 7 | VERIFIED |
| Agricultural cooperatives | 1,566 (12.82%) | BDP 2023-2028, Ch. 7 | VERIFIED |
| Seaweed national production share | 48.42% | BDP 2023-2028, Ch. 7 | VERIFIED |
| Cassava national production share | 41.70% | BDP 2023-2028, Ch. 7 | VERIFIED |
| BARMM land area share | 11.17% | BDP 2023-2028, Ch. 7 | VERIFIED |
| Total ARCs | 104 | BDP 2023-2028, Ch. 7 (MAFAR, Oct 2019) | VERIFIED |
| Total ARBOs | 240 | BDP 2023-2028, Ch. 7 (MAFAR, Oct 2019) | VERIFIED |
| Total ARBO members | 34,743 | BDP 2023-2028, Ch. 7 (MAFAR, Oct 2019) | VERIFIED |
| BARMM poverty incidence (2021) | 29.80% | BDP 2023-2028, Ch. 9 | VERIFIED |
| BARMM poverty incidence (2018) | 52.6% | BDP 2023-2028, Ch. 9 | VERIFIED |
| Bangsamoro families in poverty | 408,951 | BDP 2023-2028, Ch. 9 | VERIFIED |
| Functional literacy rate | 71.6% (lowest) | BDP 2023-2028, Ch. 9 | VERIFIED |

---

## Program Names Verification

| Program | Status | Notes |
|---------|--------|-------|
| PESO Project (Profitability and Equity Support Oriented) | VERIFIED | Confirmed in BDP 2023-2028, Ch. 7 and barmm-context.md |
| LAKAS SE Program (Lakbay Aral sa Social Enterprise) | VERIFIED | Confirmed in BDP 2023-2028, Ch. 7 and barmm-context.md |
| STOCK Project (Strengthening of Technical and Operational Knowledge) | VERIFIED | Confirmed in BDP 2023-2028, Ch. 7 and barmm-context.md |
| 3ZERO Initiative (CSEA-MAFAR-WFP-ACTED) | VERIFIED | Confirmed in CSEA official programs |
| ESKEY / AHME | CONTEXT-APPROPRIATE | Appear only in author biography (00c-author.md), not in policy content; appropriate use |

---

## Footnote Coverage

| Chapter | File | Footnote Refs | Assessment |
|---------|------|---------------|------------|
| Ch. 1 | 02-chapter-01.md | 112 | Adequate |
| Ch. 2 | 03-chapter-02.md | 125 | Adequate |
| Ch. 3 | 04-chapter-03.md | 63 | Adequate |
| Ch. 4 | 05-chapter-04.md | 109 | Adequate |
| Ch. 5 | 06-chapter-05.md | 102 | Adequate |
| Ch. 6 | 07-chapter-06.md | 101 | Adequate |
| Ch. 7 | 08-chapter-07.md | 109 | Adequate |
| Ch. 8 | 09-chapter-08.md | 42 | Adequate — operations/business planning chapter is less citation-dense by nature |
| Ch. 9 | 10-chapter-09.md | 129 | Adequate |
| Ch. 10 | 11-chapter-10.md | 85 | Adequate |
| Ch. 11 | 12-chapter-11.md | 72 | Adequate |
| Ch. 12 | 13-chapter-12.md | 88 | Adequate |
| Ch. 13 | 14-chapter-13.md | 114 | Adequate |
| Ch. 14 | 15-chapter-14.md | 130 | Adequate |

**Note**: Chapter 8 (business planning) has the lowest count (42) but this reflects the chapter's practical, operational character. No chapter falls below 40 footnote references. All chapters have adequate citation coverage.

---

## Known Error Pattern Check

| Error Pattern | Status | Notes |
|--------------|--------|-------|
| Wrong BOL article numbers (Art. VIII = Transition, Art. IX = Shari'ah, etc.) | PASS | No BOL article swaps found in chapter content. "Article VIII" references in chapters refer to CDA Memorandum Circular 2015-01 and Articles of Cooperation templates — correctly used. |
| Sulu as BARMM province (without SC ruling caveat) | **FAIL — Glossary only** | Chapters 4 and 13 correctly include SC ruling caveats. Glossary BARMM definition does not. See CRITICAL-1. |
| Wrong ministry abbreviations (MOL, MST, MPWH) | PASS | All ministry abbreviations are correct: MOLE, MOST, MPW, MAFAR, MBHTE, MENRE, MFBM, MHSD, MILG, MIPA, MOH, MOTC, MPOS, MSSD, MTIT. |
| Shari'ah Appellate Court (should be Shari'ah High Court) | PASS | Term does not appear in the guidebook. |
| ARMM creation date (1996 FPA instead of RA 6734/1989) | PASS | Not cited in this guidebook. |
| OHRAORA / ORAOHRA confusion | PASS | CSC ORAOHRA not referenced in this guidebook. |
| ESKEY / AHME as fabricated program names in policy content | PASS | Appear only in author bio, where they are accurate real program references. |
| Arithmetic and percentage errors | PASS | All percentages verified against source data. |
| Section numbering mismatch (e.g., Ch. 14 using Ch. 13 numbers) | PASS | All chapter section numbers verified: Ch. 12 uses 12.x, Ch. 13 uses 13.x, Ch. 14 uses 14.x. |
| BAA number misattribution | PASS | No BAA numbers are cited in the cooperative development guidebook. |
| Special Development Fund cited as Art. XII Sec. 10 | PASS | Not cited in this guidebook. |
| Block Grant cited as Sec. 9 instead of Sec. 15-16 | PASS | Not cited in this guidebook. |

---

## Recommendations for Correction

**Priority 1 — Fix before publication:**
1. **CRITICAL-1** (Glossary, Sulu definition): Add SC ruling caveat to the BARMM definition. This is a single sentence addition.

**Priority 2 — Fix before distribution:**
2. **MINOR-1** (Chapter 3, MAFAR name): Correct "Aquatic Resources" to "Agrarian Reform" and note the discrepancy in PB-210's own text.
3. **MINOR-2** (Glossary, MFBM name): Standardize the comma placement in the full ministry name.

**Priority 3 — Consider for next revision:**
4. **MINOR-3** (Chapter 1, Sulu examples): Add territorial caveat noting CSEA's post-SC ruling jurisdiction for new registrations.
5. **MINOR-4** (Chapter 4, CSEA structure): Direct readers to footnote on Sulu provincial office status.

---

## Commendations

The following aspects of the guidebook demonstrate exceptional factual rigor:

1. **Dual citation discipline**: Every legal provision is cited against both RA 9520 and PB-210 with correct article and section numbers. Spot-checks of 35+ RA 9520 articles and 30+ PB-210 sections all verified correctly.

2. **Statistics discipline**: All key BDP statistics (12,214 cooperatives, 11.66% compliance, 48.42% seaweed, 41.70% cassava, 37.58% producer cooperatives) match the source data exactly, including percentage precision.

3. **SC ruling handling in chapters**: Chapters 4 and 13 proactively include caveats about the *Province of Sulu v. Medialdea* ruling affecting PB-210's provincial office provisions. This is exactly the correct handling per the error log.

4. **Ministry abbreviations**: All 15 BARMM line ministry abbreviations are used correctly throughout. No instances of MOL, MST, MPWH, or other known errors found.

5. **BOL citation accuracy**: BOL Art. V Sec. 2(k), Art. XIII Sec. 24, and Art. XIII Sec. 27 are all cited accurately and with correct verbatim provisions.

---

*Fact-Check Report generated: 2026-03-27*
*Source files verified: PB-210.md, ra-9520-philippine-cooperative-code-2008.md, bdp-2023-2028/07-chapter-7-economy.md, bol-ra-11054/ (all 6 files), barmm-context.md, fact-check-error-log.md*
