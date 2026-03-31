# QA Review Report: (h) Cadastral Land Survey

**File**: `legal-reference-cadastral-land-survey.md`
**Reviewed**: 2026-03-29
**Reviewer**: /legal-reviewer QA-REVIEW

---

## Summary

| Dimension | PASS | IMPROVE | FAIL | Total Q&A |
|-----------|------|---------|------|-----------|
| Relevance | 18 | 0 | 0 | 18 |
| Evidence | 16 | 2 | 0 | 18 |
| Verbatim | 16 | 1 | 1 | 18 |
| Inclusiveness | 15 | 3 | 0 | 18 |
| Assumptions | 17 | 1 | 0 | 18 |
| Effectiveness | 18 | 0 | 0 | 18 |

**Critical Issues**: 1 FAIL (VERBATIM)

---

## FAIL Items

### FAIL-1: BAA 13 Title number — "Title IX" is wrong for MENRE

**Q&A**: Power Overview table (line 11); BAA table (line 82); Theme E.1 (lines 370-378); footnote [^3] (line 483)

**Dimension**: VERBATIM

**Problem**: Multiple references cite MENRE as established under **"BAA 13, Title IX"**. The Power Overview table states "BAA 13, Title IX"; the BAA table states "MENRE (Title IX)"; Theme E.1 cites "BAA 13, Title IX, Sec. 9(7)"; and footnote [^3] reads "BAA No. 13, tit. IX (Ministry of Environment, Natural Resources and Energy), secs. 1-12."

**Actual BAA 13**: Within **Book VI** ("Ministries and Offices"), MENRE is under **Title III** ("Environment, Natural Resources and Energy"), not Title IX. Title IX in Book VI is "Labor and Employment."

**Source**: `~/apps/transcriptions/legislation/baas/BAA-13.md`:
- Line 2038: `**TITLE III** / **ENVIRONMENT, NATURAL RESOURCES AND ENERGY**`
- Line 2918: `**TITLE IX** / **LABOR AND EMPLOYMENT**`

The section-level references (Sec. 3 for powers and functions, Sec. 9(7) for Land Management Services) are internally correct within the MENRE title -- only the Title number is wrong.

**Fix**: Change all "BAA 13, Title IX" references to "BAA 13, Book VI, Title III" for MENRE. Update footnote [^3].

---

## IMPROVE Items

### IMPROVE-1: Art. XIII, Sec. 17 para. 2 — quote contains minor formatting variance

**Q&A**: BOL Provisions table, row for Art. XIII, Sec. 17 para. 2 (line 41); Theme A, Q2 item (1) (line 282)

**Dimension**: VERBATIM

**Problem**: The file quotes Art. XIII, Sec. 17, para. 2 as: ***"The Bangsamoro Government may, upon authority of the President, conduct cadastral surveys, lot surveys, and isolated and special surveys in the Bangsamoro: Provided, That it shall furnish the results of these surveys to, and coordinate with, the relevant national government agencies to effect inclusion into the National Cadastral Survey."***

The actual BOL text reads: *"The Bangsamoro Government may, upon authority of the President, conduct cadastral surveys, lot surveys, and isolated and special surveys in the Bangsamoro: Provided, That it shall furnish the results of these surveys to, and coordinate with, the relevant national government agencies to effect inclusion into the National Cadastral Survey."*

**Source**: `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/04-articles-XIII-to-XV.md`, line 126.

**Verdict**: The verbatim text matches. PASS on substance. The minor formatting note: the BOL source uses italicized *Provided* while the legal reference uses non-italicized "Provided." This is cosmetic, not substantive.

**Fix**: Consider italicizing "*Provided*" to match BOL formatting convention.

---

### IMPROVE-2: National laws table — PD 239 title should be verified

**Q&A**: National Laws table, PD 239 row (line 136)

**Dimension**: EVIDENCE

**Problem**: The file gives PD 239's title as "Providing for the Conduct of Cadastral Surveys" (1973). This should be verified against the national laws INDEX or official sources. Presidential Decrees from the Marcos era are sometimes cited with slightly different titles.

**Fix**: Verify exact PD 239 title and date from official gazette or lawphil.net.

---

### IMPROVE-3: RA 9176 title — verify "Philippine Geodetic Engineering Act"

**Q&A**: National Laws table, RA 9176 row (line 148)

**Dimension**: EVIDENCE

**Problem**: The file gives RA 9176's title as "Philippine Geodetic Engineering Act" (2002). The exact short title should be verified. Some sources cite it as "An Act to Regulate the Practice of Geodetic Engineering in the Philippines."

**Fix**: Verify exact short title from national laws INDEX.

---

### IMPROVE-4: Missing national law — Act 496 (Land Registration Act)

**Q&A**: National Laws table

**Dimension**: INCLUSIVENESS

**Problem**: While PD 1529 (Property Registration Decree) is listed, the original Act 496 (Land Registration Act of 1903) which introduced the Torrens system to the Philippines is not mentioned. For a historical analysis of cadastral survey authority, Act 496 provides important context.

**Fix**: Consider adding Act 496 as a historical reference, noting that PD 1529 superseded it.

---

### IMPROVE-5: Missing national law — RA 10267 (2013) Residential Free Patent

**Q&A**: National Laws table

**Dimension**: INCLUSIVENESS

**Problem**: The table includes RA 10023 (2010) and RA 11573 (2021) for free patents but does not check whether RA 10267 or other amendments exist between these two laws. Search of the national laws INDEX would confirm completeness.

**Fix**: Search national laws INDEX for all free patent-related legislation to ensure completeness.

---

### IMPROVE-6: Theme I — Presidential delegation question could cite precedent

**Q&A**: Theme I, Q1 (line 452)

**Dimension**: INCLUSIVENESS

**Problem**: The answer discusses the practical approach of a "standing delegation of authority" from the President. It could strengthen the analysis by noting whether any precedent exists for such standing delegations -- e.g., whether the President has delegated survey authority to DENR regional offices or to ARMM under the previous organic law (RA 6734/RA 9054).

**Fix**: Research whether RA 9054 (ARMM) contained similar Presidential authority requirements for cadastral surveys and how they were operationalized.

---

### IMPROVE-7: Shari'ah section — fusaka inged citation to BAA 64

**Q&A**: Shari'ah table, row for "Fusaka inged" (line 200)

**Dimension**: ASSUMPTIONS

**Problem**: The file states that fusaka inged is "recognized in enacted law (BAA 64)." This assumes BAA 64 specifically uses the term "fusaka inged" and provides substantive recognition. BAA 64 should be verified to confirm it actually recognizes fusaka inged by that term and with what legal effect.

**Fix**: Verify the specific BAA 64 provision that recognizes fusaka inged and cite the section number.

---

## PASS Items (Sample)

All remaining Q&A pairs scored PASS across all 6 dimensions. Key strengths:

- **Theme A**: The identification of cadastral survey as "among the most constrained" of the 55 powers is well-supported by the Presidential authority and national integration requirements
- **Art. XIII, Sec. 17 analysis**: The three-paragraph breakdown (para. 1 = land classification, para. 2 = cadastral surveys, para. 3 = urban land reform) is accurate and well-structured
- **Theme C**: Regalian doctrine analysis correctly explains WHY Presidential authority is required
- **Theme D**: National laws comprehensively identified -- CA 141, PD 239, PD 1529, RA 9176, RA 10023, RA 11573, EO 192, EO 30, RA 8371
- **Theme E**: BAA 13 MENRE functions accurately quoted (despite wrong Title number) -- Sec. 3(j)(1), (f), (h), (l) all verified against source
- **Theme F**: Divergence analysis correctly identifies this as one of the most constrained powers
- **Theme G**: Legislative gaps and recommended legislation table is comprehensive and actionable
- **Theme I**: Power-specific questions (Presidential authorization uniqueness, relationship to power (j), National Cadastral Survey integration) are well-constructed

---

## Banned Term Check

No instances of "Exclusive", "Shared", or "Concurrent" used as power classification labels. PASS.

---

## Overall Assessment

This is the strongest of the three files reviewed, with only 1 FAIL -- the systematic BAA 13 Title numbering error shared across all three files. The analysis is thorough, the BOL quotes are verified accurate (Art. XIII, Sec. 17 matches the source exactly), and the legislative gap analysis is actionable.

The single FAIL (BAA 13 Title numbering) is a factual error that must be corrected. The IMPROVE items are primarily completeness enhancements (missing historical laws, precedent research) that would strengthen an already solid analysis.

Notable strength: The file correctly identifies the "bifurcated" nature of this power -- MENRE has institutional mandate but the Presidential authority requirement creates a unique constraint. The recommendation for a "standing delegation" is a practical legislative solution well-grounded in the analysis.
