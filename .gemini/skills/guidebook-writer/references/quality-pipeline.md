# Quality Pipeline — Detailed Procedures

The quality pipeline runs after all chapters are drafted. It produces three reports that identify issues to fix before generating final output.

---

## Step 1: Fact-Check Report

**Invoke**: `/fact-checker`

### What to Verify

1. **Names and Titles**
   - All BARMM officials mentioned — cross-reference against `~/.gemini/skills/bangsamoro/references/barmm-officials-2025-2026.md`
   - Full name on first mention, correct honorific (MP, Minister, Director, Atty.)
   - Historical figures — verify dates, roles, contributions

2. **Legislation References**
   - BAA numbers and titles — verify against local archives at `docs/` or `~/Vault/bangsamoro/bangsamoro-laws/`
   - BOL (RA 11054) articles and sections — verify against `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/`
   - National laws (Republic Acts) — verify titles and key provisions
   - Resolution numbers — verify against local archives

3. **Institutional Facts**
   - MOA names, mandates, and organizational structure — verify against BAA 13
   - Committee names and jurisdictions — verify against Parliament records
   - Organizational hierarchies and reporting relationships

4. **Dates and Numbers**
   - Historical dates (peace agreements, BOL ratification, BTA transitions)
   - Budget figures, population data, statistical claims
   - BDP goals, targets, and macroeconomic indicators

5. **Quotations**
   - Verbatim accuracy of any quoted text
   - Correct attribution

### Report Format

```markdown
# Fact-Check Report: {Guidebook Title}

**Date**: YYYY-MM-DD
**Chapters reviewed**: {list}
**Total claims checked**: {N}

## Findings

| # | Chapter | Claim | Status | Finding | Severity |
|---|---------|-------|--------|---------|----------|
| 1 | Ch. 2   | "BAA 13 establishes..." | VERIFIED | Confirmed in BAA 13, Sec. 4 | — |
| 2 | Ch. 5   | "Minister Ahmad..." | ERROR | Correct name is "Ahmed" | CRITICAL |
| 3 | Ch. 7   | "Block grant is 5%..." | ERROR | BOL Art. XII, Sec. 12 says "not less than 5%" | MINOR |

## Summary
- Verified: {N}
- Errors (Critical): {N} — must fix before publication
- Errors (Minor): {N} — should fix
- Unverifiable: {N} — flagged for manual verification
```

---

## Step 2: Legal Review Report

**Invoke**: `/legal-reviewer`

### What to Review

1. **Quoted Legal Provisions**
   - Every blockquoted legal text must be verbatim-accurate
   - Section/article/chapter numbering must match the source law
   - Correct identification of the source (BOL vs. BAA vs. national law)

2. **Legal Statements**
   - Claims about what the law requires, permits, or prohibits
   - Interpretive statements about scope, limitations, or applicability
   - References to judicial doctrines or legal principles

3. **Legal Hierarchy**
   - Consistent representation of the hierarchy: Constitution → BOL → BAAs → EOs → Local Ordinances
   - Correct identification of which level of law governs specific matters

### Source Priority

1. Local markdown transcriptions in the repository
2. BOL verbatim text at `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/`
3. Local PDFs (PDFs/ directory)
4. Web search (last resort)

### Report Format

```markdown
# Legal Review Report: {Guidebook Title}

**Date**: YYYY-MM-DD
**Reviewer**: Claude (AI-assisted, requires human legal validation)

## Provision Verification

| # | Chapter | Provision Cited | Source | Status | Finding | Severity |
|---|---------|----------------|--------|--------|---------|----------|
| 1 | Ch. 1   | BOL Art. V, Sec. 2 | bol-ra-11054 | ACCURATE | Verbatim match | — |
| 2 | Ch. 3   | BAA 13, Sec. 15 | local archive | INACCURATE | Section 15 says "may" not "shall" | CRITICAL |

## Legal Statement Review

| # | Chapter | Statement | Assessment | Recommendation |
|---|---------|-----------|------------|----------------|
| 1 | Ch. 4   | "MOAs have plenary authority..." | OVERSTATED | BOL limits MOA authority to delegated powers |

## Disclaimer
This AI-assisted legal review is for quality assurance purposes. Final legal validation should be performed by a licensed attorney.
```

---

## Step 3: QA Report

### What to Check

1. **Internal Consistency**
   - Terms defined in the glossary are used consistently throughout
   - Cross-references between chapters are accurate (chapter numbers, section numbers)
   - Acronyms are spelled out on first use in each chapter

2. **Completeness**
   - No placeholder text ("[TBD]", "[INSERT]", "lorem ipsum")
   - All sections have substantive content (no empty chapters)
   - All appendices referenced in the text exist
   - TOC matches actual chapter titles and numbering

3. **Formatting**
   - Heading hierarchy is consistent (H1 for chapters, H2 for sections, H3 for subsections)
   - Tables use proper markdown pipe syntax
   - Blockquotes are used for legal text
   - Lists are properly formatted (bullets or numbers, consistent indentation)
   - Horizontal rules separate major sections

4. **Style**
   - Audience-appropriate tone maintained throughout
   - Bold key terms for scannability
   - No run-on paragraphs (break into bullets where appropriate)
   - Practical examples and tips included where useful

### Report Format

```markdown
# QA Report: {Guidebook Title}

**Date**: YYYY-MM-DD
**Total issues**: {N}

## Issues by Category

### Consistency Issues
| # | Location | Issue | Fix |
|---|----------|-------|-----|
| 1 | Ch. 2, 5 | "drafting process" vs "drafting procedure" — inconsistent term | Standardize to "drafting process" |

### Completeness Issues
| # | Location | Issue |
|---|----------|-------|
| 1 | Ch. 8, §8.3 | Section is only 2 sentences — needs expansion |

### Formatting Issues
| # | Location | Issue | Fix |
|---|----------|-------|-----|
| 1 | Ch. 4, table | Missing separator row | Add `|---|---|---|` |

### Style Issues
| # | Location | Issue | Fix |
|---|----------|-------|-----|
| 1 | Ch. 6, §6.2 | Dense 200-word paragraph | Break into bullet list |
```
