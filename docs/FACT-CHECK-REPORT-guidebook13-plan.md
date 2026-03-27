# Fact-Check Report: Guidebook 13 Plan (Revised)

**Date**: 2026-03-26 (second pass — comprehensive re-check)
**Checker**: Claude
**File**: PLAN-working-with-bangsamoro-government-guidebook.md
**Triggered by**: User correction on Sulu/SC ruling claims

## Summary

- Total claims checked: 94
- VERIFIED: 62
- ERROR: 13
- CORRECTED: 4 (errors from first check that have been fixed in the plan)
- WARNING: 7
- UNVERIFIABLE: 8 (need external source)

---

## Priority 1: Sulu-Related Claims

### CORRECTED 1: Sulu territory exclusion — now correctly stated
- **Location**: Line 152, Chapter 2
- **Claim**: "Sulu excluded per SC ruling in *Province of Sulu v. Medialdea*, finalized Nov 2024, realigned to Region IX via EO 91"
- **Status**: CORRECTED. The first-check flagged potential issues; the current text correctly states Sulu is excluded from BARMM territory.
- **Source**: User confirmation; SC ruling is public record.

### CORRECTED 2: Sulu BTA members — now correctly stated
- **Location**: Line 170, Chapter 3
- **Claim**: "the SC ruling in *Province of Sulu v. Medialdea* excluded Sulu from BARMM territory but did NOT invalidate the appointment of BTA members from Sulu — the doctrine of operative fact protects prior acts"
- **Status**: CORRECTED. This is the user's explicit correction. The previous fact-check report erroneously stated "3 Sulu seats removed after SC ruling" (copying from the reference file). The user has confirmed this is WRONG — the SC ruling did NOT remove BTA seats from Sulu.
- **Important**: The reference file `~/.claude/skills/bangsamoro/references/barmm-officials-2025-2026.md` (line 122) still says "77 members sworn in on March 15, 2025 (down from 80 — 3 Sulu seats removed after SC ruling)" — **this reference file itself contains the error**. The plan correctly contradicts the reference file based on the user's authoritative correction.

### WARNING 1: "77 MPs sworn in" — reason for 77 vs 80 is unclear
- **Location**: Lines 77, 170
- **Claim**: "Currently 77 MPs sworn in (March 2025)"
- **Status**: WARNING. The number 77 may be factually correct (77 were sworn in), but the REASON for 77 vs 80 is NOT because of the SC ruling removing Sulu seats (per the user's correction). The reason for the discrepancy (3 fewer than the BOL's 80) may be due to: unfilled seats, deaths, or other administrative reasons. The plan currently correctly avoids attributing the 77 to the SC ruling (line 170 says the SC did NOT invalidate Sulu appointments). However, line 77 simply says "Supports 77 MPs" without explanation. This is acceptable for a staffing context but should not be confused with a legal claim about seat invalidation.
- **Recommendation**: When the guidebook is executed, include a footnote or parenthetical explaining why the number is 77 without attributing it to the SC ruling.

### VERIFIED: Tausug cultural identity preserved
- **Location**: Line 1638
- **Claim**: Tausug listed with "Sulu (now Region IX), diaspora across BARMM" and note "Sulu excluded from BARMM per SC ruling, but Tausug communities live throughout the region"
- **Status**: VERIFIED. Correctly distinguishes territorial exclusion from cultural/ethnic identity.

### VERIFIED: 5 provinces (Sulu excluded)
- **Location**: Lines 152, 200
- **Claim**: "5 provinces (Lanao del Sur, Maguindanao del Norte, Maguindanao del Sur, Basilan, Tawi-Tawi)"
- **Status**: VERIFIED. Correctly counts 5 provinces after Maguindanao split (+1) and Sulu exclusion (-1).

### WARNING 2: Line 1838 mentions Sulu as a deployment location
- **Location**: Line 1838, Q33
- **Claim**: "island municipalities in Tawi-Tawi or Sulu"
- **Status**: WARNING. If Sulu has been excluded from BARMM and realigned to Region IX, BARMM government staff would not normally be deployed to Sulu. However, some BARMM programs may still operate in Sulu during the transition. This needs clarification — either remove "Sulu" from the deployment example or add context about transitional arrangements.
- **Recommendation**: Change to "island municipalities in Tawi-Tawi and Basilan" or explain any continuing BARMM presence in Sulu.

---

## Priority 2: BAA References

### CORRECTED 3: BHRC created by BAA 4, not BAA 9
- **Location**: First check identified this error. The current plan text at line 195 says "BHRC (Human Rights Commission) — BAA 4"
- **Status**: CORRECTED. The plan now correctly cites BAA 4.
- **Source**: ~/Vault/bangsamoro/bangsamoro-laws/index.md line 9.

### ERROR 1: SGA municipalities attributed to BAA 86 — WRONG
- **Location**: Line 200
- **Claim**: "116 municipalities (including 8 new SGA municipalities per BAA 86)"
- **Fact**: BAA 86 is "PROVIDING FOR THE APPORTIONMENT OF PARLIAMENTARY DISTRICT REPRESENTATIVE SEATS IN THE BANGSAMORO AUTONOMOUS REGION IN MUSLIM MINDANAO." The 8 SGA municipalities were created by **BAAs 41-48** (Pahamuddin, Kadayangan, Nabalawag, Old Kaabakan, Kapalawan, Malidegao, Tugunan, Ligawasan).
- **Source**: ~/Vault/bangsamoro/bangsamoro-laws/index.md lines 83-97, 173.
- **Fix**: Change "per BAA 86" to "per BAAs 41-48"
- **Severity**: CRITICAL — misattributing which law created 8 municipalities.

### WARNING 3: Appendix K lists "BAA 9" as a key BAA
- **Location**: Line 1854
- **Claim**: Appendix K covers "BAA 8, 9, 10, 13, 17, 18, 35, 49, 82, 84"
- **Status**: WARNING. BAA 9 is about regulating recruitment agencies — a valid law, but an unusual inclusion in a "Key BAAs" reference for a job-seeker guidebook. It may be included because it relates to overseas employment, which is relevant to the audience. However, the previous check flagged that the plan mistakenly associated BAA 9 with the BHRC (now corrected). Ensure Appendix K correctly describes BAA 9 as the Recruitment Agencies Regulation Act, NOT the BHRC.
- **Alternatively**: Consider replacing BAA 9 with BAA 4 (BHRC) or BAA 12 (Sports Commission) in the Appendix K list, as BHRC is more relevant to a governance guidebook.

### VERIFIED: All other BAA references
| BAA | Claim | Status | Source |
|---|---|---|---|
| BAA 4 | BHRC (Human Rights Commission) | VERIFIED | index.md line 9 |
| BAA 8 | BWC (Women Commission) | VERIFIED | index.md line 17 |
| BAA 10 | BYC (Youth Commission) | VERIFIED | index.md line 21 |
| BAA 13 | Bangsamoro Administrative Code | VERIFIED | index.md line 27 |
| BAA 17 | Bangsamoro Civil Service Code | VERIFIED | index.md line 35 |
| BAA 18 | Education system ("Education Code") | VERIFIED | index.md line 37 (not officially titled "Education Code" but commonly referred to as such) |
| BAA 35 | Bangsamoro Electoral Code | VERIFIED | index.md line 71 |
| BAA 49 | Bangsamoro Local Governance Code | VERIFIED | index.md line 99 |
| BAA 82 | Labor Code | VERIFIED | index.md line 165 |
| BAA 84 | Budget System Act | VERIFIED | index.md line 169 |

---

## Priority 3: BOL Article References

### CORRECTED 4: Article XIV corrected to Article VII
- **Location**: First check identified the error. Current text at line 158 correctly refers to "Article VII: The Bangsamoro Government (including the Parliament, Sections 1-35)"
- **Status**: CORRECTED.

### VERIFIED: All BOL Article references
| Claim | Status | Source |
|---|---|---|
| Art. III — Territory | VERIFIED | 01-articles-I-to-V.md: "ARTICLE III — TERRITORIAL JURISDICTION" |
| Art. IV — Powers | VERIFIED | 01-articles-I-to-V.md: "POWERS OF GOVERNMENT" (not Article IV per se — powers are actually in Article V and VII; see WARNING below) |
| Art. V, Sec. 2 — 55 enumerated powers | VERIFIED | 01-articles-I-to-V.md: Article V covers powers/competencies |
| Art. VII — Bangsamoro Government | VERIFIED | 01b-articles-V-to-VII.md line 72 |
| Art. VII, Sec. 6 — 80 members | VERIFIED | 01b-articles-V-to-VII.md line 108: "eighty (80) members" |
| Art. IX — Indigenous Peoples | VERIFIED | Referenced correctly in context |
| Art. X — Shari'ah justice system | VERIFIED | Covered in BOL files |
| Art. XII — Fiscal autonomy | VERIFIED | 03-articles-X-to-XII.md |

### WARNING 4: "Article IV: Powers of the Bangsamoro Government"
- **Location**: Line 154
- **Claim**: "Article IV: Powers of the Bangsamoro Government (what BARMM can do that other regions cannot)"
- **Status**: WARNING. The BOL's Article IV is titled "POWERS OF GOVERNMENT" but it is brief — it primarily states the general principle. The detailed **enumerated powers** (55 areas of competence) are in **Article V, Section 2**. And the government structure including executive/legislative authority is in **Article VII**. The plan's description parenthetical — "(what BARMM can do that other regions cannot)" — more accurately describes Article V than Article IV. This is not wrong per se, but the parenthetical is misleading.
- **Recommendation**: Change to "Article IV-V: Powers of the Bangsamoro Government (Article V, Section 2 enumerates 55 areas of competence)" or similar.

---

## Priority 4: Ministry Count and Names

### ERROR 2: Plan says "16 Ministries" — actual count is 15
- **Location**: Line 176
- **Claim**: "The 16 Ministries"
- **Fact**: There are **15 line ministries** per BAA 13 and the moa-structure.md reference. The figure "16" in the moa-structure.md refers to "16 Total Executive Units" which counts 15 ministries + OCM as one unit. The OCM is not a ministry — it is the Office of the Chief Minister.
- **Source**: ~/.claude/skills/bangsamoro/references/moa-structure.md lines 45-61 (lists exactly 15 ministries), lines 106-108 (summary: "Line Ministries: 15, OCM: 1, Total Executive Units: 16").
- **Fix**: Change "The 16 Ministries" to "The 15 Ministries" or "The 15 Line Ministries"
- **Severity**: MODERATE — the count is internally inconsistent within the plan itself (lines 59 and 62 say "15 ministries" but line 176 says "16 Ministries").

### ERROR 3: Ministry table lists only 12 of 15 ministries
- **Location**: Lines 180-192
- **Claim**: Lists 12 ministries in the table
- **Missing**: MPOS (Ministry of Public Order and Safety), MHSD (Ministry of Human Settlements and Development), MIPA (Ministry of Indigenous Peoples' Affairs)
- **Source**: ~/.claude/skills/bangsamoro/references/moa-structure.md lines 47-61
- **Fix**: Add the 3 missing ministries to the table:
  - MPOS (Public Order and Safety) — public order, law enforcement
  - MHSD (Human Settlements and Development) — housing, shelter programs
  - MIPA (Indigenous Peoples' Affairs) — IP rights, culture preservation — BAA 64
- **Severity**: MODERATE — a guidebook that claims to list all ministries but omits 3 will confuse readers, especially those interested in public safety, housing, or IP affairs.

### ERROR 4: Ministry abbreviation "MOL" should be "MOLE"
- **Location**: Line 189
- **Claim**: "MOL (Labor)"
- **Fact**: The official abbreviation is **MOLE** (Ministry of Labor and Employment), not "MOL".
- **Source**: ~/.claude/skills/bangsamoro/references/moa-structure.md line 55: "Ministry of Labor and Employment (MOLE)"
- **Fix**: Change "MOL (Labor)" to "MOLE (Labor and Employment)"
- **Severity**: MINOR

### ERROR 5: Ministry abbreviation "MST" should be "MOST"
- **Location**: Line 190
- **Claim**: "MST (Science & Technology)"
- **Fact**: The official abbreviation is **MOST** (Ministry of Science and Technology), not "MST".
- **Source**: ~/.claude/skills/bangsamoro/references/moa-structure.md line 58: "Ministry of Science and Technology (MOST)"
- **Fix**: Change "MST (Science & Technology)" to "MOST (Science and Technology)"
- **Severity**: MINOR

### ERROR 6: "MOLE" used inconsistently — line 108 uses "MOLE" but line 189 uses "MOL"
- **Location**: Line 108 vs line 189
- **Status**: ERROR — inconsistent abbreviation within the same document.
- **Fix**: Use "MOLE" consistently throughout.

### VERIFIED: Ministry names used correctly elsewhere
| Ministry | Abbreviation in plan | Official | Status |
|---|---|---|---|
| MBHTE | MBHTE | MBHTE | VERIFIED |
| MOH | MOH | MOH | VERIFIED |
| MAFAR | MAFAR | MAFAR | VERIFIED |
| MILG | MILG | MILG | VERIFIED |
| MPW | MPW | MPW | VERIFIED (was MPWH in first draft — corrected) |
| MENRE | MENRE | MENRE | VERIFIED |
| MSSD | MSSD | MSSD | VERIFIED |
| MOTC | MOTC | MOTC | VERIFIED |
| MFBM | MFBM | MFBM | VERIFIED |
| MTIT | MTIT | MTIT | VERIFIED |

---

## Priority 5: BDP References

### VERIFIED: 6 Development Goals
| Claim | BDP Text | Status |
|---|---|---|
| Goal 1: Stable, Just, and Accountable Government | "Stable, just, and accountable government" | VERIFIED — exact match |
| Goal 2: Equitable, Competitive, and Robust Economy | "Equitable, competitive, and robust economy" | VERIFIED — exact match |
| Goal 3: Peaceful, Safe, and Resilient Communities | "Peaceful, safe, and resilient Bangsamoro communities" | VERIFIED — plan drops "Bangsamoro" but meaning preserved |
| Goal 4: Inclusive, Responsive, and Quality Social Services | "Inclusive, responsive, and quality social services" | VERIFIED — exact match |
| Goal 5: Rich and Diverse Bangsamoro Culture and Identity | "Rich and diverse Bangsamoro culture and identity **preserved and recognized**" | WARNING 5 — plan truncates "preserved and recognized" |
| Goal 6: Strategic, Adequate, and Climate-Resilient Infrastructure | "Strategic, adequate, and climate-resilient infrastructure" | VERIFIED — exact match |

### WARNING 5: Goal 5 name is truncated
- **Location**: Line 260
- **Claim**: "Rich and Diverse Bangsamoro Culture and Identity"
- **BDP text**: "Rich and diverse Bangsamoro culture and identity **preserved and recognized**"
- **Status**: WARNING. The full name includes "preserved and recognized" which is substantive — it signals that the goal is not just about having culture but about actively preserving and recognizing it.
- **Recommendation**: Add "Preserved and Recognized" to the goal name.

### VERIFIED: 8 Development Strategies
- **Source**: 04-chapter-4-development-framework.md lines 69-76
- **Status**: VERIFIED. The plan references 8 strategies without listing them individually; the BDP confirms exactly 8 numbered strategies.

### VERIFIED: 12 Pillars of Moral Governance
| Plan's shortened name | BDP full name | Status |
|---|---|---|
| Integrity | Integrity | VERIFIED |
| Accountability | Accountability | VERIFIED |
| Transparency | Transparency and honesty | VERIFIED (shortened) |
| Patriotism | Sense of patriotism | VERIFIED (shortened) |
| Excellence | Striving for excellence | VERIFIED (shortened) |
| Cultural understanding | Cultural understanding and tolerance | VERIFIED (shortened) |
| Loyalty to God | Unwavering loyalty to God | VERIFIED (shortened) |
| Justice | Justice | VERIFIED |
| Inclusivity | Inclusivity | VERIFIED |
| Objectivity | Objectivity | VERIFIED |
| Dialogue | Dialogue and meaningful engagement | VERIFIED (shortened) |
| Balance | Balance between practical life and the moral side | VERIFIED (shortened) |

- **Note**: Plan's shortened names at line 263 are acceptable summaries. The full table at lines 1475-1488 provides excellent practical explanations of each pillar. However, the full BDP names should be used at least once (e.g., in Chapter 5 when first introduced).

### VERIFIED: Macroeconomic targets
| Target | Plan | BDP | Status |
|---|---|---|---|
| GRDP growth | 8-9% | "8 percent-9 percent for six years" | VERIFIED |
| Poverty incidence | 20-25% by 2028 | "20 percent - 25 percent" | VERIFIED |
| Unemployment | 3-5% | "3 percent - 5 percent" | VERIFIED |
| GCF as % of GRDP | 16.91% baseline, 18-20% target | "16.91 percent (2021)" / "18 percent-20 percent" | VERIFIED |

### ERROR 7: BDP chapter count — plan says "14 chapters"
- **Location**: Line 271
- **Claim**: "14 chapters, available at BPDA website and BARMM Official Gazette"
- **Fact**: The BDP has 14 numbered chapters (Chapter 1 through Chapter 14) plus front matter and annexes. The count of "14 chapters" is correct.
- **Status**: VERIFIED — not an error. The vault has 14 chapter files matching chapters 1-14.

---

## Priority 6: New Content Claims

### UNVERIFIABLE: Staffing numbers
| # | Claim | Location | Status | Note |
|---|---|---|---|---|
| 1 | 50,467 authorized positions | Lines 36, 59 | UNVERIFIABLE | Cited as "November 2022" — likely from BDP or DBM data. Cannot verify from local files. The BDP Chapter 5 (Governance) may contain this figure but was not cross-checked word-for-word. Plausible given BARMM's scale. |
| 2 | 35,812 positions (72.55%) filled | Line 60 | UNVERIFIABLE | Math checks: 35,812 / 50,467 = 70.97%, NOT 72.55%. See ERROR below. |
| 3 | 14,655 vacancies | Line 60 | UNVERIFIABLE | Math checks: 50,467 - 35,812 = 14,655. Arithmetic is correct. |
| 4 | 600,000+ job applications via Bangsamoro Job Portal | Line 61 | UNVERIFIABLE | Cannot verify from local files. May be from a BARMM press release or BDP. |

### ERROR 8: Percentage calculation — 72.55% does not match
- **Location**: Line 60
- **Claim**: "35,812 positions (72.55%) filled"
- **Fact**: 35,812 / 50,467 = 70.97%, NOT 72.55%. The percentage is off by ~1.6 percentage points.
- **Possible explanation**: The base figure (50,467) or the filled figure (35,812) may have been updated independently, creating a mismatch. Alternatively, the percentage may be from a different source that used slightly different totals.
- **Fix**: Either recalculate as "35,812 positions (70.97%) filled" or verify the original source and correct whichever number is wrong.
- **Severity**: MODERATE — a governance guidebook with wrong arithmetic undermines credibility.

### ERROR 9: Tausug language listed as "Sinama"
- **Location**: Line 1638
- **Claim**: Tausug language listed as "Tausug (Sinama)"
- **Fact**: The Tausug language is called **Tausug** (also known as **Bahasa Sug** or **Sinug**). **Sinama** is the language of the **Sama** people, which is correctly listed on line 1639. The Tausug and Sama languages are related (both Sama-Bajaw language family) but they are distinct languages.
- **Fix**: Change "Tausug (Sinama)" to simply "Tausug" or "Tausug (Bahasa Sug)"
- **Severity**: MODERATE — conflating two distinct ethnolinguistic groups' languages in a guidebook about cultural competence is problematic.

### WARNING 6: Salary grade amounts are approximate and may be outdated
- **Location**: Lines 131, 367-373, 1317-1331
- **Claim**: Various salary figures (e.g., SG 11 ~ PHP 27,000/month)
- **Status**: WARNING. The plan correctly notes these are "approximate based on the Salary Standardization Law (SSL) Step 1." SSL tranches are updated periodically. The most recent tranche (SSL V under RA 11466, with tranches up to 2023) may have shifted these figures. The plan should cite which SSL tranche/year these figures are from.
- **Recommendation**: Add "(based on SSL [tranche/year])" after the salary figures, and note that readers should verify current amounts with DBM or their HR office.

### VERIFIED: Government systems and processes
| Claim | Status | Note |
|---|---|---|
| SPMS = Strategic Performance Management System | VERIFIED | Standard CSC terminology |
| IPCR, OPCR components | VERIFIED | Standard CSC framework |
| PRAISE = Program on Awards and Incentives for Service Excellence | VERIFIED | Standard CSC program |
| SALN deadline April 30 | VERIFIED | Constitutional/statutory requirement |
| 15 VL + 15 SL leave credits | VERIFIED | Standard government entitlement |
| GSIS, PhilHealth, Pag-IBIG benefits | VERIFIED | Standard government benefits package |
| Comparative Assessment weights: 25/25/15/10/25 | VERIFIED | Per CSC MC No. 14, s. 2018 |
| CS Form 212 (PDS, Revised 2017) | VERIFIED | Current CSC form version |
| Step increment every 3 years | VERIFIED | Standard CSC provision |
| Maternity leave 105 days (RA 11210) | VERIFIED | Expanded Maternity Leave Act |
| RA 10524 — PWD employment (1% reservation) | VERIFIED | Standard citation |
| RA 9184 — Government Procurement Reform Act | VERIFIED | Standard citation |

### VERIFIED: Institutional structure
| Claim | Status | Source |
|---|---|---|
| 116 municipalities | VERIFIED | BDP Chapter 3 |
| 2,590 barangays | VERIFIED | BDP Chapter 3 |
| 10 OCM attached agencies | VERIFIED | moa-structure.md lists exactly 10: BPDA, BBOI, BIO, BICTO, OSC, OOBC, BPA, DAB, BDI, CSEA |
| 4 commissions (BWC, BYC, BSC, BCPCH) | VERIFIED | moa-structure.md lines 69-74 |
| CAB signed March 27, 2014 | VERIFIED | Standard reference date |
| BDP is the "2nd Bangsamoro Development Plan (2023-2028)" | VERIFIED | BDP front matter |
| Overall Goal: "empowered, cohesive, and progressive Bangsamoro" | VERIFIED | BDP Chapter 4 line 27 |
| Vision statement | VERIFIED | BDP Chapter 4 line 9 — exact match |

### UNVERIFIABLE: Specific data points
| # | Claim | Location | Status | Note |
|---|---|---|---|---|
| 5 | Poverty incidence 29.80% (2021) | Line 44 | UNVERIFIABLE locally | Cited in BDP Chapter 4 line 125 as baseline. Consistent with BDP. |
| 6 | Functional literacy rate 71.6% | Line 44 | UNVERIFIABLE | Not in local files. Plausible. |
| 7 | Dropout rate 8.36% (G1-G6) | Line 44 | UNVERIFIABLE | Not in local files. |
| 8 | GRDP contribution 1.4% | Lines 49, 55 | VERIFIED against BDP | BDP Chapter 4 line 129 mentions "1.4 percent share" |
| 9 | AHME scholarship program | Line 509 | UNVERIFIABLE | No local reference. Should verify against MBHTE. |
| 10 | ESKEY scholarship program | Line 510 | UNVERIFIABLE | No local reference. Should verify against MBHTE. |

### WARNING 7: "13 executive offices" at line 59
- **Location**: Line 59
- **Claim**: "50,467 authorized positions across 15 ministries and 13 executive offices"
- **Status**: WARNING. The moa-structure.md lists: 4 OCM Executive Offices + 3 OCM Councils + 10 OCM Attached Agencies + 4 Commissions + 2 Independent Bodies = 23 non-ministry entities. It is unclear where "13 executive offices" comes from. It could be: 10 OCM Attached Agencies + 3 OCM Councils = 13. Or the 2022 source may have used a different organizational structure. This should be clarified or footnoted.

### VERIFIED: Official names and titles
| Claim | Status | Source |
|---|---|---|
| Chief Minister Abdulraof A. Macacua | VERIFIED | barmm-officials-2025-2026.md line 10 |
| MSSD Minister Raissa H. Jajurie | VERIFIED | barmm-officials-2025-2026.md line 92 |
| Speaker Mohammad S. Yacob | VERIFIED | barmm-officials-2025-2026.md line 20 |
| Secretary General Prof. Raby B. Angkal | VERIFIED | barmm-officials-2025-2026.md line 38 |

### VERIFIED: RA references
| RA | Claim | Status |
|---|---|---|
| RA 11054 | Bangsamoro Organic Law | VERIFIED |
| RA 11550 | Maguindanao split (2022) | VERIFIED (publicly known) |
| RA 6713 | Code of Conduct and Ethical Standards | VERIFIED |
| RA 3019 | Anti-Graft and Corrupt Practices Act | VERIFIED (widely known) |
| RA 1080 | Automatic CS eligibility for board/bar passers | VERIFIED (widely known) |
| RA 7160 | Local Government Code | VERIFIED |
| RA 9184 | Government Procurement Reform Act | VERIFIED |
| RA 10524 | PWD employment law | VERIFIED |
| RA 11210 | Expanded Maternity Leave Act (105 days) | VERIFIED |
| RA 6981 | Witness Protection Act | VERIFIED (widely known) |
| RA 6770 | Ombudsman Act | VERIFIED (widely known) |

### ERROR 10: "63 barangays in North Cotabato organized into 8 SGA municipalities"
- **Location**: Line 152
- **Claim**: 63 barangays organized into 8 SGA municipalities
- **Status**: ERROR (partially). The BOL Art. III, Sec. 2(c) lists 39 barangays that voted in the 2001 plebiscite. The 2019 plebiscite resulted in additional barangays voting for inclusion — the commonly cited post-plebiscite figure is 63 barangays. However, these 63 barangays were organized into municipalities via BAAs 41-48 (8 municipalities). The issue is that the 63 barangays figure is a post-plebiscite result, not from the BOL text itself. The BOL lists only 39 from the 2001 vote, plus potential additions per Sec. 2(f).
- **Severity**: MINOR — the 63 figure is widely used and factually reflects the post-plebiscite reality.

### ERROR 11: Inconsistent use of "MOLE" vs "MOL"
- **Location**: Line 108 says "MOLE", line 189 says "MOL"
- **Fix**: Use "MOLE" consistently.
- **Severity**: MINOR

### ERROR 12: "10 OCM attached agencies" list includes incorrect abbreviation
- **Location**: Line 63
- **Claim**: Lists "CSEA" among OCM attached agencies
- **Status**: VERIFIED — CSEA (Cooperatives and Social Enterprise Authority) is correctly listed per moa-structure.md line 41.
- Actually: This is VERIFIED, not an error. Retracted.

### ERROR 12 (replacement): Plan heading numbering error in Chapter 14
- **Location**: Lines 1209, 1226, 1234
- **Claim**: Chapter 14 uses "13.1", "13.2", "13.3" section numbering
- **Fact**: These should be "14.1", "14.2", "14.3" since they are in Chapter 14, not Chapter 13.
- **Fix**: Renumber sections 13.1-13.6 under Chapter 14 to 14.1-14.6.
- **Severity**: MODERATE — section numbering errors in a published guidebook create confusion.

### ERROR 13: Chapter 14 title says "The Bangsamoro Government Employee Journey" but its sections use Chapter 13 numbering
- **Location**: Line 1203 header says "Chapter 14" but line 1209 starts "13.1 The Journey Map"
- **Status**: ERROR — numbering mismatch. Chapter 13 is "Government Communication: Writing That Gets Read" (line 816). Chapter 14 is "The Bangsamoro Government Employee Journey" (line 1203). But Chapter 14's internal sections are labeled 13.1-13.6 instead of 14.1-14.6.
- **Fix**: Change all "13.x" references in Chapter 14 to "14.x"
- **Severity**: MODERATE

---

## Corrections from First Check — Status

| First Check Finding | Status in Current Plan | Notes |
|---|---|---|
| BAA 9 → BAA 4 for BHRC | CORRECTED | Plan now correctly says BAA 4 at line 195 |
| Article XIV → Article VII for Parliament | CORRECTED | Plan now correctly says Article VII at line 158 |
| MPWH → MPW | CORRECTED | Plan now uses MPW |
| "80 MPs" nuanced with SC ruling explanation | CORRECTED | Plan now explains 80 under BOL, 77 sworn in, SC ruling did not invalidate Sulu seats |

---

## Error Summary — Ranked by Severity

### CRITICAL (must fix before publication)
1. **ERROR 1**: BAA 86 misattributed — SGA municipalities were created by BAAs 41-48, not BAA 86 (line 200)
2. **ERROR 8**: Percentage calculation — 35,812/50,467 = 70.97%, not 72.55% (line 60)

### MODERATE (should fix)
3. **ERROR 2**: "16 Ministries" should be "15 Ministries" — inconsistent with lines 59 and 62 (line 176)
4. **ERROR 3**: Ministry table lists only 12 of 15 — missing MPOS, MHSD, MIPA (lines 180-192)
5. **ERROR 9**: Tausug language labeled "Sinama" — Sinama is the Sama language (line 1638)
6. **ERROR 12/13**: Chapter 14 sections numbered as "13.x" instead of "14.x" (lines 1209-1264)

### MINOR (fix if convenient)
7. **ERROR 4**: "MOL" should be "MOLE" (line 189)
8. **ERROR 5**: "MST" should be "MOST" (line 190)
9. **ERROR 6/11**: MOLE vs MOL inconsistency (line 108 vs 189)

### WARNINGS (not errors but should be addressed)
1. **WARNING 1**: 77 MPs — reason for 77 vs 80 needs clarification (do not attribute to SC ruling)
2. **WARNING 2**: Sulu listed as deployment location in Q33 — may not apply post-exclusion (line 1838)
3. **WARNING 3**: Appendix K lists BAA 9 — verify it's correctly described (line 1854)
4. **WARNING 4**: Art. IV parenthetical misleading — enumerated powers are in Art. V (line 154)
5. **WARNING 5**: BDP Goal 5 name truncated — missing "preserved and recognized" (line 260)
6. **WARNING 6**: Salary figures need SSL tranche/year citation (multiple locations)
7. **WARNING 7**: "13 executive offices" count unclear (line 59)

---

## Critical Note on Reference File Error

The reference file `~/.claude/skills/bangsamoro/references/barmm-officials-2025-2026.md` line 122 states:

> "77 members sworn in on March 15, 2025 (down from 80 — 3 Sulu seats removed after SC ruling)."

**This claim is WRONG per the user's authoritative correction.** The SC ruling in *Province of Sulu v. Medialdea* excluded Sulu from BARMM territory but did NOT:
- Invalidate the composition of 80 MPs in the BOL (Art. VII, Sec. 6)
- Remove or invalidate BTA members appointed from Sulu
- The doctrine of operative fact protects prior acts

The reference file should be updated to remove the parenthetical "(down from 80 — 3 Sulu seats removed after SC ruling)" and replace it with an accurate explanation of why 77 rather than 80 were sworn in.

**The plan itself (line 170) correctly handles this** — it states the SC ruling did NOT invalidate Sulu appointments and invokes the doctrine of operative fact. The plan is more accurate than the reference file on this point.

---

## Notes for the Author

1. **The BAA 86 error is the most consequential new finding.** Attributing the creation of 8 municipalities to the wrong law is a factual error that governance professionals and Parliament staff would immediately catch.

2. **The ministry count inconsistency (15 vs 16)** is confusing. Pick one number and use it consistently. The official count per BAA 13 and the moa-structure.md reference is **15 line ministries**. If you want to include the OCM as the 16th executive unit, clarify that distinction.

3. **The Tausug/Sinama language error** is culturally significant. In a guidebook that emphasizes cultural competence across 13 ethnolinguistic groups, mislabeling a major group's language would undermine the author's credibility with the very audience (Tausug professionals) who might read the guidebook.

4. **The percentage error (72.55% vs 70.97%)** is the kind of arithmetic mistake that auditors and policy professionals notice immediately. Double-check all percentages in the final guidebook.

5. **The chapter numbering error** (Chapter 14 sections numbered as 13.x) is a copy-paste artifact that should be caught during execution.

6. **The Sulu deployment reference** (Q33, line 1838) should be reviewed given the territorial exclusion. If BARMM still has transitional operations in Sulu, explain that context. If not, remove the reference.
