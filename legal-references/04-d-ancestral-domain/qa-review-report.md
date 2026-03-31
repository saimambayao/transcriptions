# QA Review Report: (d) Ancestral Domain and Natural Resources

**File**: `legal-reference-ancestral-domain.md`
**Reviewed**: 2026-03-29
**Reviewer**: /legal-reviewer QA-REVIEW

---

## Summary

| Dimension | PASS | IMPROVE | FAIL | Total Q&A |
|-----------|------|---------|------|-----------|
| Relevance | 22 | 1 | 0 | 23 |
| Evidence | 20 | 3 | 0 | 23 |
| Verbatim | 18 | 2 | 3 | 23 |
| Inclusiveness | 19 | 4 | 0 | 23 |
| Assumptions | 22 | 1 | 0 | 23 |
| Effectiveness | 22 | 1 | 0 | 23 |

**Critical Issues**: 3 FAILs (all VERBATIM)

---

## FAIL Items

### FAIL-1: Art. IX, Sec. 2 citation — wrong section number

**Q&A**: BOL Provisions table, row for Art. IX, Sec. 2 (line 86); also Theme A, item (7) (line 384)

**Dimension**: VERBATIM

**Problem**: The file cites **Art. IX, Sec. 2** for the transitional justice provision and quotes: ***"The Bangsamoro Parliament, taking into account the report of the Transitional Justice and Reconciliation Commission, shall enact a transitional justice mechanism..."***

**Actual BOL**: This quoted text is **Art. IX, Sec. 1** ("Transitional Justice"), not Sec. 2. Art. IX, Sec. 2 is "Reparation for Unjust Dispossession" with different text: *"The Parliament shall enact laws providing for adequate reparation to the Bangsamoro people affected by unjust dispossession of territorial and proprietary rights or customary land tenure..."*

**Source**: `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/02-articles-VI-to-IX.md`, lines 242-244.

**Fix**: Change all references from "Art. IX, Sec. 2" to "Art. IX, Sec. 1" for the transitional justice provision. The text quoted matches Sec. 1, not Sec. 2.

---

### FAIL-2: BAA 13 Title number — "Title IX" is wrong

**Q&A**: Power Overview table (line 11); BAA table (line 127); Theme E (lines 497-511); footnote [^7] (line 625)

**Dimension**: VERBATIM

**Problem**: Multiple references cite MENRE as established under **"BAA 13, Title IX"**. The file also cites MIAP under **"BAA 13, Title X"** (line 517, footnote [^8]).

**Actual BAA 13**: BAA 13 uses Book/Title structure. Within **Book VI** ("Ministries and Offices"):
- MENRE is under **Title III** ("Environment, Natural Resources and Energy"), not Title IX
- MIAP is under **Title VII** ("Indigenous Peoples' Affairs"), not Title X
- Title IX in BAA 13 Book VI is "Labor and Employment"
- Title X is "Public Order and Safety"

**Source**: `~/apps/transcriptions/legislation/baas/BAA-13.md`, lines 2038-2039 (Title III = MENRE), 2595-2596 (Title VII = MIAP), 2918-2919 (Title IX = Labor), 3103-3104 (Title X = Public Order).

**Fix**: Change all "BAA 13, Title IX" references to "BAA 13, Book VI, Title III" for MENRE. Change all "BAA 13, Title X" references to "BAA 13, Book VI, Title VII" for MIAP. Update footnotes [^7] and [^8] accordingly.

---

### FAIL-3: Art. IX, Sec. 3 verbatim quote incomplete/inaccurate

**Q&A**: BOL Provisions table, row for Art. IX, Sec. 3 (line 91)

**Dimension**: VERBATIM

**Problem**: The file quotes Art. IX, Sec. 3 as: ***"The Bangsamoro Government recognizes the rights of the indigenous peoples and shall adopt measures for the promotion and protection of the following rights: (a) Native titles or fusaka inged; ... (d) Equitable share in revenues from the utilization of resources in their ancestral lands; ..."***

The actual BOL text at Art. IX, Sec. 3(d) reads: *"Equitable share in revenues from the utilization of resources in their ancestral lands"* -- this matches. However, the file also states in the Explanation column that there are "Eight enumerated IP rights" but only quotes two. More critically, the last paragraph of Art. IX, Sec. 3 in the BOL reads: *"This Organic Law shall not in any manner diminish the rights and benefits of the non-Moro indigenous peoples in the Bangsamoro Autonomous Region under the Constitution, national laws, particularly Republic Act No. 8371, otherwise known as the 'Indigenous Peoples' Rights Act of 1997.'"* The file's National Laws table (line 205) quotes this as: ***"This Organic Law shall not in any manner diminish the rights and benefits of the non-Moro indigenous peoples ... under the Constitution, national laws, particularly Republic Act No. 8371."*** -- this omits "in the Bangsamoro Autonomous Region" and "otherwise known as..." The ellipsis masks a geographic qualifier.

**Source**: `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/02-articles-VI-to-IX.md`, lines 246-268.

**Fix**: Either quote the full text or ensure ellipses do not omit material qualifiers. The omission of "in the Bangsamoro Autonomous Region" changes the scope of the non-diminishment clause from region-specific to universal.

---

## IMPROVE Items

### IMPROVE-1: Theme A item count claims "11 provisions" but lists only 10 numbered items

**Q&A**: Theme A, Q2 (line 370)

**Dimension**: RELEVANCE

**Problem**: The answer states "Eleven provisions elaborate this power" then lists 10 numbered items ((1) through (10), with item (11) being Art. XIII, Sec. 1). However, item (6) bundles Art. XIII, Sec. 13-16 as a single item covering four sections. The count of "eleven" is defensible (counting each section separately) but the numbered list only goes to (11). No error, but the numbering could be clearer.

**Fix**: Either list all 11 individually or change the introductory count to match the list length.

---

### IMPROVE-2: Missing national laws — RA 11801 (2022) Expanded NIPAS amendments not checked

**Q&A**: National Laws table

**Dimension**: INCLUSIVENESS

**Problem**: The national laws table includes RA 7586 (NIPAS) and RA 11038 (Expanded NIPAS) but does not address whether any more recent protected area laws or executive orders (post-2018) affect BARMM. Search of the national laws INDEX would confirm completeness.

**Fix**: Confirm against national laws INDEX that no additional protected area or mining legislation enacted 2019-2025 affects this analysis.

---

### IMPROVE-3: No reference to PD 705 (Forestry Code)

**Q&A**: National Laws table

**Dimension**: INCLUSIVENESS

**Problem**: PD 705 (Revised Forestry Code of the Philippines) is the fundamental national law governing forest management -- directly relevant to the natural resources dimension of this power. Its absence is a gap.

**Fix**: Add PD 705 to the national laws table with its relationship to MENRE's forest management functions.

---

### IMPROVE-4: Jurisprudence section could note Cruz v. DENR Secretary holding

**Q&A**: Jurisprudence table (line 312)

**Dimension**: INCLUSIVENESS

**Problem**: The file correctly notes the Cruz v. DENR case but dismisses it as inconclusive (equally divided vote). However, the effect of the equally divided vote was to UPHOLD the constitutionality of IPRA -- this is material and should be stated explicitly.

**Fix**: State that the equally divided vote resulted in dismissal of the petition, effectively upholding IPRA's constitutionality.

---

### IMPROVE-5: Development Plan Mas Matatag Pillar assignment

**Q&A**: Development Plan table (line 354)

**Dimension**: EVIDENCE

**Problem**: The table assigns this power to "Pillar 4: Environmental Sustainability" of the Mas Matatag na Bangsamoro Agenda. This assignment should be verified against the actual OCM EO No. 2, s. 2026 text. The ancestral domain dimension may also connect to Pillar 1 (Good Governance) or Pillar 5 (Peace and Security).

**Fix**: Verify Pillar assignment against the authoritative source.

---

### IMPROVE-6: Theme B lacks enacted Shari'ah legislation check

**Q&A**: Theme B, Q3 (line 440)

**Dimension**: EVIDENCE

**Problem**: The answer correctly states that PD 1083 does not address natural resources. It could also note that BAA 87 (Shari'ah Courts) and BAA 20 (Shari'ah) may have provisions relevant to customary land disputes.

**Fix**: Check BAA 87 and BAA 20 for any provisions intersecting ancestral domain or natural resource disputes.

---

### IMPROVE-7: Theme E, MENRE functions list — subsection lettering mismatch

**Q&A**: Theme E.1, Q2 (lines 499-509)

**Dimension**: EVIDENCE

**Problem**: The file cites BAA 13 functions with letters (a), (d), (f), (h), (j)(1), (j)(3), (j)(4), (k), (l), (n). Verified against BAA 13 source (lines 2052-2082) -- these letter assignments are correct. However, the file labels these as "Title IX, Sec. 3" which is wrong (should be Book VI, Title III, Sec. 3).

**Fix**: Correct the Title reference per FAIL-2.

---

## PASS Items (Sample)

All remaining Q&A pairs scored PASS across all 6 dimensions. Key strengths:

- **Theme A**: Comprehensive coverage of BOL provisions; correct identification of all 5 limitation categories
- **Theme C**: Constitutional provisions correctly identified and quoted
- **Theme D**: National laws accurately described with correct relationship characterizations (directly applicable vs. suppletory)
- **Theme F**: Divergence analysis correctly differentiates the constraint levels across sub-areas (general natural resources vs. mining vs. fossil fuels)
- **Theme G**: Legislative gaps accurately identified with correct BOL basis citations
- **Theme H**: Development connections properly linked to BDP chapters
- **Theme I**: Power-specific questions well-constructed and non-duplicative
- **Legislative Gaps table**: All 5 recommended laws have correct BOL basis and scope

---

## Banned Term Check

No instances of "Exclusive", "Shared", or "Concurrent" used as power classification labels. PASS.

---

## Overall Assessment

The file is well-structured with comprehensive coverage of a complex, multi-dimensional power. The 3 FAILs are all VERBATIM issues that must be corrected before publication:

1. **Art. IX, Sec. 1 vs Sec. 2** -- the transitional justice provision is Sec. 1, not Sec. 2
2. **BAA 13 Title numbering** -- MENRE is Book VI, Title III (not Title IX); MIAP is Book VI, Title VII (not Title X)
3. **Art. IX, Sec. 3 ellipsis** -- omits "in the Bangsamoro Autonomous Region" geographic qualifier

The IMPROVE items are primarily INCLUSIVENESS gaps (missing PD 705, Cruz v. DENR holding) and minor EVIDENCE verification needs. These do not affect the accuracy of existing content but represent gaps in coverage.
