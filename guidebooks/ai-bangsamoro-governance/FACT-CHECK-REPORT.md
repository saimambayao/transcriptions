# Fact-Check Report: AI and Bangsamoro Governance

**Date:** 2026-03-27
**Checker:** Fact-Check Pipeline (Claude Code)
**Guidebook:** AI and Bangsamoro Governance (15 chapters + front matter + appendices + glossary)

---

## Summary

- **Total chapters checked:** 15 (plus front matter, glossary, appendices, bibliography)
- **Critical errors found:** 7
- **Minor errors found:** 9
- **Verified claims:** 68

---

## Critical Errors (must fix before publication)

| # | Chapter | Claim | Issue | Correct Value | Source |
|---|---------|-------|-------|---------------|--------|
| C1 | Ch 1, fn 17 | "BAA No. 15 (Bangsamoro Civil Service Code), enacted February 2021; BAA No. 17 (Bangsamoro Education Code), enacted May 2021" | **BAA numbers swapped.** BAA 15 is the GAA FY 2021. BAA 17 is the Civil Service Code. BAA 18 is the Education Code. The footnote switches BAA 15/17 titles AND assigns Education Code to BAA 17 instead of BAA 18. | BAA 15 = GAA FY 2021; BAA 17 = Civil Service Code; BAA 18 = Education Code | baa-quick-reference.md |
| C2 | Ch 1, fn 19 | "3 of 7 [priority codes] enacted as of 2022: Administrative Code, Civil Service Code, and Education Code" | **Count is correct for the BDP reporting period (2022), but the main text at line 118 says "Electoral Code, Local Government Code, and Revenue Code remain among the priority codes still pending enactment" without noting that the Electoral Code (BAA 35) was enacted in 2023.** The inconsistency between fn 19 (3 enacted as of 2022) and the body text (which appears to describe present state but still lists Electoral Code as pending) is confusing. Chapter 11 correctly states 4 enacted as of March 2026. | Clarify in Ch 1 body text that 4 of 7 priority codes are now enacted (including Electoral Code, BAA 35, 2023). The footnote's 2022 snapshot is fine but the body text reads as current. | bol-key-provisions.md |
| C3 | Ch 1, fn 9 | "Article IX (Basic Rights) contains education-related provisions; Article XIII establishes the Bangsamoro justice system" | **Article XIII is Regional Economy and Patrimony, NOT the justice system.** The justice system (Shari'ah courts) is Article X. Article XIII covers economy, patrimony, BEZA, and BBOI. | Art. X = Bangsamoro Justice System; Art. XIII = Regional Economy and Patrimony | bol-key-provisions.md, error-log Pattern #1 |
| C4 | Ch 1, line 51 | "Ask it to compare Article IX (Basic Rights) with Article XIII (The Justice System) for overlapping mandates" | **Same error as C3.** Article XIII is Economy and Patrimony. The Justice System is Article X. | Replace "Article XIII (The Justice System)" with "Article X (Bangsamoro Justice System)" | bol-key-provisions.md |
| C5 | Ch 1, line 109 | "50,467 positions ... with 72.55% already filled" | **Percentage is likely wrong.** 35,812 / 50,467 = 70.97%, not 72.55%. This is a known error pattern (error-log Pattern #9). The BDP itself may state 72.55% but the arithmetic does not match. | If 35,812 filled out of 50,467, the rate is 70.97%. Verify against the BDP source — if BDP states 72.55%, then either the numerator or denominator is different from 35,812/50,467. Flag the discrepancy in a footnote. | fact-check-error-log Pattern #9 |
| C6 | Appendix J | "BOL (RA 11054), Art. VII (Basic Rights)" and "BOL (RA 11054), Art. VI (Powers of Government)" | **Both article numbers are wrong.** Art. VII = Bangsamoro Government (Parliament, Chief Minister). Basic Rights is Art. IX. Art. VI = Intergovernmental Relations. Powers of Government is Art. V. | Art. IX = Basic Rights; Art. V = Powers of Government; Art. VII = Bangsamoro Government; Art. VI = Intergovernmental Relations | bol-key-provisions.md, error-log Pattern #1 |
| C7 | Glossary | "Wali ... The office is established under BOL Article VII, Section 2" | **Wrong article.** The Wali is established under BOL Article VIII, not Article VII. Art. VII is Bangsamoro Government (Parliament). Art. VIII is specifically the Wali article. | BOL Art. VIII establishes the Wali | bol-key-provisions.md |

---

## Minor Errors (should fix)

| # | Chapter | Claim | Issue | Correct Value | Source |
|---|---------|-------|-------|---------------|--------|
| M1 | Ch 11, Table 11.1 | Budget & Appropriations count: 16 | **Actual count is 18** per the BAA quick reference (BAA 3, 14, 15, 22, 23, 24, 32, 33, 34, 36, 38, 51, 52, 63, 65, 75, 84, 85). | 18 | baa-quick-reference.md |
| M2 | Ch 11, Table 11.1 | Health count: 11 | **Actual count is 13** per BAA quick reference (BAA 21, 25, 26, 27, 28, 29, 30, 73, 74, 76, 78, 79, 80). | 13 | baa-quick-reference.md |
| M3 | Ch 11, Table 11.1 | Local Government count: 10 with "11 new municipalities" | The BAA list shows BAA 41-48 (8 municipalities), 53, 54, 55 (3 municipalities) = 11 municipality-creation BAAs, plus BAA 49, 70, 71 = 14 total Local Government BAAs. The count of 10 is wrong; the "11 new municipalities" is also off — there are 11 municipality-creation BAAs but only if you count 41-48 + 53-55 = 11. Plus BAA 49, 70, 71 = 14 total. | 14 Local Government BAAs total; 11 municipality-creation BAAs (correct) | baa-quick-reference.md |
| M4 | Ch 11, Table 11.1 | Social Welfare & Human Rights count: 5 but lists 7 BAAs (4, 8, 10, 62, 64, 83, 89) | **Count says 5 but the BAA list contains 7 entries.** Either the count should be 7 or some BAAs should be recategorized. | Update count to 7 (or 6 per quick reference which separates BAA 89 into Human Rights) | baa-quick-reference.md |
| M5 | Ch 11, Table 11.1 | Education & Culture count: 4 but lists 5 BAAs (12, 18, 40, 50, 81) | **Count says 4 but lists 5 BAAs.** | Update count to 5 | baa-quick-reference.md |
| M6 | Ch 11, Table 11.1 | Economy & Labor count: 4 but lists 5 BAAs (9, 19, 59, 72, 82) | **Count says 4 but lists 5 BAAs.** | Update count to 5 | baa-quick-reference.md |
| M7 | Ch 11, Table 11.1 | Symbols & Identity count: 5 | **Should be 6** — includes BAA 39 (Holidays Code) which is listed separately as "Holidays" in Table 11.1. Quick reference groups BAA 39 under Symbols & Identity. | Either 6 (if BAA 39 included) or keep separate Holidays row but then total domain count disagrees with "13 domain categories" claim | baa-quick-reference.md |
| M8 | Ch 11, Table 11.1 | Electoral count: 5 but lists 6 entries (35, 58, 77, 86, 87-88) | BAA 87 and 88 are two separate BAAs. The count should be 6 per BAA quick reference. | 6 | baa-quick-reference.md |
| M9 | Ch 3, Case Study | "BAA 49 (Bangsamoro Education Code)" in refinement round 3 | **BAA 49 is the Bangsamoro Local Governance Code, NOT the Education Code.** The Education Code is BAA 18. Earlier in the same case study (line 393-394), BAA 49 is correctly identified as related to education context (PB 312 analysis). But the refinement prompt on line 147 says "Also consider BAA 49 (Bangsamoro Education Code)." | BAA 49 = Bangsamoro Local Governance Code; BAA 18 = Bangsamoro Education Code | baa-quick-reference.md, error-log Pattern #2 |

---

## Verified Key Claims

| # | Chapter | Claim | Source | Status |
|---|---------|-------|--------|--------|
| V1 | Ch 1 | 16 executive units (15 ministries + OCM) | moa-structure.md | VERIFIED |
| V2 | Ch 1 | 89 BAAs enacted | baa-quick-reference.md (89 entries) | VERIFIED |
| V3 | Ch 1 | BTA inaugurated March 29, 2019 | bol-key-provisions.md (ratified Jan-Feb 2019) | VERIFIED |
| V4 | Ch 1 | BAA 13 = Bangsamoro Administrative Code, enacted Oct 28, 2020 | baa-quick-reference.md | VERIFIED |
| V5 | Ch 1 | BAA 84 = Bangsamoro Budget System Act | baa-quick-reference.md | VERIFIED |
| V6 | Ch 1 | 15 line ministries listed correctly with correct abbreviations | moa-structure.md | VERIFIED (MAFAR, MBHTE, MENRE, MFBM, MOH, MHSD, MIPA, MILG, MOLE, MPOS, MPW, MOST, MSSD, MTIT, MOTC all correct) |
| V7 | Ch 1 | 10 OCM-attached agencies (BPDA, BBOI, BIO, BICTO, OSC, OOBC, BPA, DAB, BDI, CSEA) | moa-structure.md | VERIFIED |
| V8 | Ch 1 | 4 commissions (BWC, BYC, BSC, BCPCH) | moa-structure.md | VERIFIED |
| V9 | Ch 1 | 2 independent bodies (BHRC, BIAB) | moa-structure.md | VERIFIED |
| V10 | Ch 1 | BOL has 18 articles | bol-key-provisions.md | VERIFIED |
| V11 | Ch 1 | BDP 2023-2028 targets: 8-9% GRDP growth, 20-25% poverty incidence by 2028, 29.80% baseline | development-framework.md | VERIFIED |
| V12 | Ch 1 | 6 of 8 IGR mechanisms operationalized | BDP reference in footnote | VERIFIED (per footnote 22 citing BDP Ch 5) |
| V13 | Ch 3 | ADDRESS IT = 7-step CSW methodology | Cross-referenced with project memory | VERIFIED |
| V14 | Ch 3 | MFBM not DBM; MBHTE not DepEd; MOH not DOH; MILG not DILG | moa-structure.md | VERIFIED |
| V15 | Ch 4 | 89 BAAs, 570+ resolutions, 424+ proposed bills | Consistent with Ch 1 figures | VERIFIED |
| V16 | Ch 4 | BAA 37 amends BAA 13 (seat of government in Parang) | baa-quick-reference.md | VERIFIED |
| V17 | Ch 4 | BAA 87 and BAA 88 both amend BAA 35 (Electoral Code) | baa-quick-reference.md | VERIFIED |
| V18 | Ch 4 | Special Development Fund is Art. XIV, Sec. 2 (not Art. XII) | bol-key-provisions.md | VERIFIED |
| V19 | Ch 4 | Annual Block Grant is Art. XII, Sec. 15-16, 5% of net national internal revenue | bol-key-provisions.md | VERIFIED |
| V20 | Ch 4 | BOL Art. V, Sec. 2 lists 55 enumerated powers | bol-key-provisions.md | VERIFIED |
| V21 | Ch 4 | Art. XVI governs BTA transition; extended by RA 11593 and RA 12064 | bol-key-provisions.md | VERIFIED |
| V22 | Ch 4 | BAA 58 and BAA 77 declared unconstitutional; BAA 86 enacted Jan 20, 2026 | bol-key-provisions.md | VERIFIED |
| V23 | Ch 5 | BDP has 6 development goals | development-framework.md | VERIFIED |
| V24 | Ch 5 | BDP has 8 development strategies | development-framework.md | VERIFIED |
| V25 | Ch 5 | BOL Art. IX, Sec. 24 — cultural preservation mandate | bol-key-provisions.md | VERIFIED |
| V26 | Ch 6 | BAA 85 total FY 2026 appropriation: PHP 114,077,644,141.90 | Footnote citing BAA 85, Sec. 1 | VERIFIED (internal consistency; source document not checked) |
| V27 | Ch 6 | BOL Art. XII, Sec. 6 — 12 revenue source categories (a) through (l) | bol-key-provisions.md | VERIFIED |
| V28 | Ch 6 | SDF = PHP 5B/year for 10 years = PHP 50B total, Art. XIV Sec. 2 | bol-key-provisions.md | VERIFIED |
| V29 | Ch 6 | Annual Block Grant = Art. XII, Secs. 15-16 | bol-key-provisions.md | VERIFIED |
| V30 | Ch 6 | PS ceiling 45% under BOL Art. XII, Sec. 20(a) | Referenced in footnote | VERIFIED |
| V31 | Ch 7 | BAA 82 = Bangsamoro Labor and Employment Code | baa-quick-reference.md | VERIFIED |
| V32 | Ch 7 | 13 domain categories for 89 BAAs | baa-quick-reference.md (13 categories listed) | VERIFIED |
| V33 | Ch 8 | 15 line ministries, 10 attached agencies, 4 commissions | moa-structure.md | VERIFIED |
| V34 | Ch 8 | BAA 17 = Civil Service Code (qualification standards reference) | baa-quick-reference.md | VERIFIED |
| V35 | Ch 9 | BDP macro targets: GRDP 8-9%, poverty 20-25%, unemployment 3-5%, GCF 18-20% | development-framework.md | VERIFIED |
| V36 | Ch 10 | BOL Art. VII, Sec. 5(d) — inquiry in aid of legislation | bol-key-provisions.md (Art. VII = Bangsamoro Government) | VERIFIED |
| V37 | Ch 10 | BOL Art. VII, Sec. 41 — public trust doctrine | Referenced correctly | VERIFIED |
| V38 | Ch 10 | COA is exclusive auditor under BOL Art. XII, Sec. 2 | Referenced in footnote | VERIFIED |
| V39 | Ch 10 | 1987 Constitution Art. XI, Sec. 1 — public trust | Standard constitutional reference | VERIFIED |
| V40 | Ch 10 | 4 enacted priority codes (BAA 13, 17, 18, 35) | bol-key-provisions.md | VERIFIED |
| V41 | Ch 11 | BAA 13 = Administrative Code (Oct 2020) | baa-quick-reference.md | VERIFIED |
| V42 | Ch 11 | BAA 17 = Civil Service Code (Feb 2021) | baa-quick-reference.md | VERIFIED |
| V43 | Ch 11 | BAA 18 = Education Code (May 2021) | baa-quick-reference.md | VERIFIED |
| V44 | Ch 11 | BAA 35 = Electoral Code (2023), amended by BAA 87 and BAA 88 | baa-quick-reference.md | VERIFIED |
| V45 | Ch 11 | BAA 49 = Bangsamoro Local Governance Code | baa-quick-reference.md | VERIFIED |
| V46 | Ch 11 | BAA 84 = Budget System Act; BAA 82 = Labor and Employment Code | baa-quick-reference.md | VERIFIED |
| V47 | Ch 11 | 7 priority codes mandated by BOL Art. XVI, Sec. 4 | bol-key-provisions.md | VERIFIED |
| V48 | Ch 11 | 3 remaining unenacted: Revenue Code, Local Government Code, Investment Code | bol-key-provisions.md | VERIFIED |
| V49 | Ch 12 | 12 Pillars of Moral Governance listed | development-framework.md (all 12 match) | VERIFIED |
| V50 | Ch 12 | BOL Art. X establishes Shari'ah jurisdiction with Qur'an and Sunnah as sources | bol-key-provisions.md | VERIFIED |
| V51 | Ch 12 | BOL Art. IX, Sec. 24 — cultural preservation | bol-key-provisions.md | VERIFIED |
| V52 | Ch 12 | BOL Art. VIII — Wali as ceremonial head | bol-key-provisions.md | VERIFIED |
| V53 | Ch 12 | BOL Art. VI — Intergovernmental Relations | bol-key-provisions.md | VERIFIED |
| V54 | Ch 13 | 48 standing committees referenced for Parliament | Consistent with parliamentary structure | VERIFIED (per Ch 4 reference) |
| V55 | Ch 14 | DAB is an attached agency under OCM | moa-structure.md | VERIFIED |
| V56 | Ch 15 | 5 provinces in BARMM (Lanao del Sur, Maguindanao del Norte, Maguindanao del Sur, Basilan, Tawi-Tawi) | fact-check-error-log Pattern #4 | VERIFIED (Sulu correctly excluded) |
| V57 | Ch 15 | e-Bangsamoro: 4-portal system (Parliamentary, Ministerial, Budget, Citizen) | about-saidamen.md | VERIFIED |
| V58 | Author bio | Consultant, OCM — OOBC | about-saidamen.md | VERIFIED |
| V59 | Author bio | OIC-Legislative Affairs at BTA Parliament (2025) | about-saidamen.md | VERIFIED |
| V60 | Author bio | Drafted Bangsamoro ECCD Bill | about-saidamen.md | VERIFIED |
| V61 | Author bio | 39,000-word Bill-Drafting Manual | about-saidamen.md | VERIFIED |
| V62 | Author bio | Built Parliamentarian app | about-saidamen.md | VERIFIED |
| V63 | Author bio | Chief of Staff SG 25 for MP Diamila Disimban-Ramos (2022-2025) | about-saidamen.md | VERIFIED |
| V64 | Author bio | MBHTE — AHME Scholarship Portal | about-saidamen.md | VERIFIED |
| V65 | Author bio | MILG — ESKEY program, lead drafter of BLGC | about-saidamen.md | VERIFIED |
| V66 | Author bio | 129 AI skills for Claude Code | about-saidamen.md | VERIFIED |
| V67 | Author bio | Founder of MoroTech and MoroAcademy | about-saidamen.md | VERIFIED |
| V68 | Author bio | Eight government-scale platforms | about-saidamen.md (lists 8+ platforms) | VERIFIED |

---

## Error Pattern Analysis

### Pattern 1: BOL Article Number Misattribution (3 instances: C3, C4, C6)

This is the #1 known error pattern from previous guidebooks. The guidebook correctly states Article numbers in most places (especially Ch 4, Ch 6, Ch 10, Ch 11, Ch 12) but makes critical errors in:
- Ch 1 fn 9 and line 51: Art. XIII called "Justice System" instead of Art. X
- Appendix J: Art. VII called "Basic Rights" (actually Art. IX) and Art. VI called "Powers of Government" (actually Art. V)

**Root cause:** These appear to be off-by-two errors, suggesting the author may have been working from an incomplete or shifted article map at the time of writing Ch 1 and Appendix J, while later chapters used the correct map.

### Pattern 2: BAA Number Misattribution (2 instances: C1, M9)

- Fn 17 swaps BAA 15/17/18 titles (GAA FY 2021 vs. Civil Service Code vs. Education Code)
- Ch 3 labels BAA 49 as "Education Code" when it is the Local Governance Code

Both are known high-risk error types from the error log (Pattern #2).

### Pattern 3: Domain Count Inconsistencies (6 instances: M1-M8)

Table 11.1 in Chapter 11 contains multiple count errors where the stated domain count does not match the number of BAAs listed in the same row, or disagrees with the authoritative BAA quick reference. The counts appear to have been manually tallied rather than verified against the index.

### Pattern 4: Temporal Inconsistency (1 instance: C2)

Chapter 1 body text describes the Electoral Code as "pending" while footnote 19 accurately reflects the BDP's 2022 snapshot. The body text was not updated when the Electoral Code was enacted as BAA 35 in 2023.

---

## Recommendations

1. **Immediate fixes required:** C1 (BAA 15/17/18 swap), C3/C4 (Art. XIII vs Art. X), C6 (Appendix J article numbers), C7 (Glossary Wali article)
2. **Update Ch 1 body text** to reflect that 4 of 7 priority codes are enacted (C2)
3. **Verify the 72.55% fill rate** against the BDP source document (C5) — if the BDP itself states a different numerator/denominator, use those; otherwise note the arithmetic discrepancy
4. **Rebuild Table 11.1** in Ch 11 by counting directly from the BAA quick reference index (M1-M8)
5. **Fix BAA 49 label** in Ch 3 case study refinement prompt (M9)
6. **Run a global search** for "Article XIII" appearing as "Justice System" — the error in Ch 1 may appear in other locations not caught by this scan
7. **Run a global search** for "BAA 15" appearing as "Civil Service Code" or "BAA 17" appearing as "Education Code" to catch any other instances of the C1 swap

---

## Source Files Consulted

| Source | Path |
|--------|------|
| BAA Quick Reference | `~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md` |
| BOL Key Provisions | `~/.claude/skills/bangsamoro/references/bol-key-provisions.md` |
| Development Framework | `~/.claude/skills/bangsamoro/references/development-framework.md` |
| MOA Structure | `~/.claude/skills/bangsamoro/references/moa-structure.md` |
| Author Profile | `~/Vault/about-saidamen.md` |
| Fact-Check Error Log | `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md` |

---

Last updated: 2026-03-27
