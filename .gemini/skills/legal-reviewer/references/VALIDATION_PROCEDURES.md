# Systematic Validation Procedures

Detailed step-by-step procedures for verifying all legal facts, citations, and sources in parliamentary resolutions.

## Table of Contents
1. Citation Extraction
2. Constitutional Citation Verification
3. Supreme Court Case Verification
4. Statutory Reference Verification
5. Bangsamoro Autonomy Act Verification
6. Quotation Exactness Verification
7. Error Documentation
8. Report Generation

## 1. Citation Extraction

### Procedure: Extract All Citations from Resolution

**Input:** Resolution file (markdown format)

**Process:**

1. Read the resolution document systematically from top to bottom
2. Identify each WHEREAS clause
3. For each WHEREAS clause, extract:
   - Superscript citation numbers (e.g., ¹, ², ³)
   - Any legal authority mentioned (Constitution, BOL, Supreme Court case, Republic Act)
   - Any quotations (text in quotation marks)
   - Note the exact location (WHEREAS #)

4. For RESOLVED clauses:
   - Note any legal authorities referenced
   - Record any quotations

5. Review all footnotes:
   - Extract each footnote reference
   - Note the corresponding WHEREAS/RESOLVED location
   - Document the exact citation information

6. Create an inventory table with columns:
   - Citation Number
   - Type (Constitutional / Supreme Court / Republic Act / Bangsamoro Autonomy Act / Other)
   - Citation Text as Written
   - Location (WHEREAS #, RESOLVED #, or Footnote #)
   - G.R. Number (if Supreme Court case)
   - Section/Article Reference
   - Quoted Text (if applicable)

**Example Table:**

| Citation # | Type | Citation as Written | Location | G.R. Number | Status |
|-----------|------|-------------------|----------|------------|--------|
| 1 | Constitutional | 1987 Philippine Constitution, Article X, Section 15 | WHEREAS 1 | N/A | To Verify |
| 2 | BOL | Rep. Act No. 11054, Article VII, Section 3 | WHEREAS 2 | N/A | To Verify |
| 3 | Supreme Court | Province of Sulu v. Executive Secretary, G.R. Nos. 242255, 243246, 243693 | WHEREAS 7 | 242255, 243246, 243693 | To Verify |

## 2. Constitutional Citation Verification

### Procedure: Verify 1987 Philippine Constitution References

**For each Constitutional citation extracted:**

1. **Identify the specific provision:**
   - Article number (e.g., Article X)
   - Section number (e.g., Section 15)
   - Subsection if applicable (e.g., (a), (b), etc.)

2. **Verify against authoritative source:**
   - Access official 1987 Philippine Constitution text (from Official Gazette or lawphil.net)
   - Locate the exact article and section cited
   - Confirm the provision still exists and has not been superseded

3. **For quoted Constitutional text:**
   - Extract exact wording from official Constitution
   - Compare character-by-character with quoted text in resolution
   - Note any differences in punctuation, capitalization, or wording

4. **Document findings:**
   - Status: VERIFIED or ERROR
   - If ERROR, note type:
     - Wrong article/section reference
     - Quoted text doesn't match official wording
     - Provision superseded or no longer in effect

5. **Record verification source:**
   - Source document (e.g., "Official Gazette Constitution Database")
   - Access date
   - URL if applicable

**Verification Checklist:**
- [ ] Article number is correct
- [ ] Section number is correct
- [ ] Subsection (if cited) is correct
- [ ] Quoted text matches official Constitution wording exactly
- [ ] Provision is currently in effect (not superseded)
- [ ] Source verified through official database

## 3. Supreme Court Case Verification

### Procedure: Verify Supreme Court Citations with G.R. Numbers

**For each Supreme Court case citation:**

1. **Extract citation components:**
   - Case name (e.g., "Province of Sulu v. Executive Secretary")
   - G.R. number(s) - **MANDATORY** (e.g., G.R. Nos. 242255, 243246, 243693)
   - Decision date (e.g., September 3, 2024)
   - SCRA reference if cited (e.g., "50 SCRA 30")

2. **Verify G.R. number exists:**
   - Check that G.R. number format is correct (G.R. No./Nos. + number(s))
   - Access official Supreme Court database (SC Online Database or lawphil.net)
   - Search for G.R. number
   - **CRITICAL**: If no matching case is found, this is a CRITICAL ERROR

3. **Cross-verify case information:**
   - Case name matches database record exactly
   - Decision date matches database record
   - Court is Supreme Court (not lower court)
   - Case citation is from official Supreme Court database

4. **For quoted case holdings:**
   - Locate official case text (from Supreme Court database)
   - Extract relevant holding or statement
   - Compare with resolution's quoted text
   - Verify quotation matches official case text exactly

5. **Document findings:**
   - Status: VERIFIED or ERROR
   - G.R. number verified: YES or NO
   - Case name verified: YES or NO
   - Decision date verified: YES or NO
   - Quoted holding accurate: YES or NO (if quoted)

6. **If G.R. number is missing or incorrect:**
   - Search court databases for correct G.R. number based on case name and date
   - Document correct G.R. number
   - Mark as CRITICAL ERROR requiring correction

**Verification Checklist:**
- [ ] G.R. number is present
- [ ] G.R. number exists in official Supreme Court database
- [ ] Case name matches official database record exactly
- [ ] Decision date matches official record
- [ ] SCRA reference (if cited) is correct
- [ ] Any quoted holding matches official case text exactly
- [ ] Case is still good law (not reversed, overruled, or superseded)

## 4. Statutory Reference Verification

### Procedure: Verify Republic Act and National Law Citations

**For each Republic Act or National Law citation:**

1. **Extract citation components:**
   - Law name (e.g., "Bangsamoro Organic Law")
   - Republic Act number (e.g., "Republic Act No. 11054")
   - Year (e.g., 2018)
   - Article number if cited (e.g., Article VII)
   - Section number if cited (e.g., Section 3)

2. **Verify statute exists:**
   - Access official legislative database (lawphil.net or Official Gazette)
   - Search for Republic Act number
   - Confirm law exists and has been enacted

3. **Verify article/section references:**
   - Locate the specific article and section cited
   - Confirm article/section numbers are correct
   - Verify section is currently in effect (not repealed)

4. **For quoted statutory text:**
   - Extract exact wording from official legislative source
   - Compare with quoted text in resolution
   - Verify word-for-word exactness

5. **Check current status:**
   - Verify law has not been repealed or superseded
   - Check if law has been amended
   - Note any amendments relevant to the cited provision

6. **Document findings:**
   - Status: VERIFIED or ERROR
   - Law exists: YES or NO
   - Article/section reference correct: YES or NO
   - Quoted text matches: YES or NO (if quoted)
   - Law currently in effect: YES or NO

**Verification Checklist:**
- [ ] Republic Act number is correct
- [ ] Law name matches official legislative record
- [ ] Article number (if cited) is correct
- [ ] Section number (if cited) is correct
- [ ] Quoted statutory text matches official law text exactly
- [ ] Law is currently in effect (not repealed)
- [ ] Any amended provisions are noted

## 5. Bangsamoro Autonomy Act Verification

### Procedure: Verify Bangsamoro Autonomy Act Citations

**For each Bangsamoro Autonomy Act citation:**

1. **Extract citation components:**
   - Autonomy Act name (e.g., "Bangsamoro Administrative Code")
   - Autonomy Act number (e.g., "Bangsamoro Autonomy Act No. 13")
   - Section number if cited (e.g., Section 5)
   - Subsection if cited

2. **Verify act exists and is current:**
   - Access Official Bangsamoro Gazette
   - Search for Bangsamoro Autonomy Act by number
   - Confirm act has been enacted
   - Verify act is currently in effect (not superseded)

3. **Verify section references:**
   - Locate the specific section cited
   - Confirm section number is correct
   - Verify section is currently in effect

4. **For quoted provisions:**
   - Extract exact wording from official Bangsamoro Gazette source
   - Compare with quoted text in resolution
   - Verify word-for-word exactness

5. **Verify BARMM constitutional compliance:**
   - Confirm act is authorized by Bangsamoro Organic Law
   - Check that act does not conflict with BOL provisions
   - Verify act is within Parliament's authority

6. **Document findings:**
   - Status: VERIFIED or ERROR
   - Act exists: YES or NO
   - Section reference correct: YES or NO
   - Quoted text matches: YES or NO (if quoted)
   - Act currently in effect: YES or NO
   - BOL compliance verified: YES or NO

**Verification Checklist:**
- [ ] Bangsamoro Autonomy Act number is correct
- [ ] Act name matches official Bangsamoro Gazette record
- [ ] Section number is correct
- [ ] Quoted text matches official act text exactly
- [ ] Act is currently in effect
- [ ] Act is authorized by Bangsamoro Organic Law
- [ ] No conflicts with BOL provisions

## 6. Quotation Exactness Verification

### Procedure: Verify All Quoted Legal Text Matches Source Documents

**For each quotation in the resolution (any text in quotation marks):**

1. **Identify the quotation:**
   - Locate text in quotation marks
   - Determine if it's legal text or other content
   - Identify source document (Constitution, statute, case, etc.)

2. **Extract source text:**
   - Access authoritative source document
   - Locate the corresponding passage
   - Copy exact official wording

3. **Compare quotation with source:**
   - Match resolution quotation character-by-character with official source
   - Check for identical:
     - Spelling
     - Capitalization
     - Punctuation
     - Spacing
     - Paragraph breaks

4. **Identify discrepancies:**
   - Any differences = ERROR
   - Examples of discrepancies:
     - "provides that the Parliament shall have authority" vs. "shall have the authority" (word difference)
     - "Autonomous Regions" vs. "autonomous regions" (capitalization)
     - "persons, companies" vs. "persons; companies" (punctuation)
     - Extra words not in original
     - Missing words from original

5. **Classify quotation errors:**
   - **EXACT MATCH** = PASS
   - **MINOR DISCREPANCY** (punctuation, capitalization) = SIGNIFICANT ERROR
   - **PARAPHRASE (not exact)** = CRITICAL ERROR if in quotation marks
   - **MISSING TEXT** from original = CRITICAL ERROR

6. **Document findings:**
   - Location: WHEREAS #, RESOLVED #, or Footnote #
   - Original quotation: [as written]
   - Correct quotation: [from authoritative source]
   - Type of error (if any)

**Verification Checklist:**
- [ ] All text in quotation marks is from legitimate legal sources
- [ ] Quoted text matches source document exactly
- [ ] Capitalization matches source
- [ ] Punctuation matches source
- [ ] No words are missing or added
- [ ] No paraphrases are presented as quotations
- [ ] Ellipses ([...]) correctly indicate omitted text

## 7. Error Documentation

### Format for Documenting Each Error:

```
**ERROR #[Number]**
- **Location**: [WHEREAS #, RESOLVED #, or Footnote #]
- **Type**: [Critical/Significant/Minor]
- **Category**: [Wrong G.R. number / Misquoted text / Incorrect section / etc.]
- **Original Citation**: [Exact text as written in resolution]
- **Error Description**: [What is wrong with this citation]
- **Correct Citation**: [What the correct citation should be]
- **Source Verification**: [Where verified - database name, access date]
- **Impact**: [How this error affects the resolution's accuracy]
```

### Example Error Documentation:

```
**ERROR #1**
- **Location**: WHEREAS 7, Footnote ⁷
- **Type**: Critical Error
- **Category**: Missing G.R. Numbers
- **Original Citation**: Province of Sulu v. Executive Secretary, Supreme Court of the Philippines (September 3, 2024)
- **Error Description**: Supreme Court case citation missing mandatory G.R. numbers
- **Correct Citation**: Province of Sulu v. Executive Secretary, G.R. Nos. 242255, 243246, 243693, Supreme Court of the Philippines (September 3, 2024)
- **Source Verification**: Supreme Court Online Database (November 3, 2024)
- **Impact**: Critical - G.R. numbers are mandatory for all Supreme Court citations per Philippine legal citation standards
```

## 8. Validation Report Generation

### Section: Error Summary and Statistics

Create summary statistics:

| Error Category | Critical | Significant | Minor | Total |
|---|---|---|---|---|
| Wrong G.R. numbers | X | - | - | X |
| Misquoted text | X | Y | - | X+Y |
| Incorrect references | - | Z | - | Z |
| **TOTAL ERRORS** | **X** | **Y+Z** | **0** | **X+Y+Z** |

### Section: Accuracy Metrics

Calculate accuracy percentages:

- **Constitutional Citations Accuracy**: [# verified]/[# total] = [%]
- **Supreme Court Cases Accuracy**: [# verified]/[# total] = [%]
- **Statutory References Accuracy**: [# verified]/[# total] = [%]
- **Bangsamoro Autonomy Acts Accuracy**: [# verified]/[# total] = [%]
- **Quotation Exactness**: [# exact]/[# total quotes] = [%]
- **Overall Accuracy Rate**: [# verified]/[# total] = [%]

### Quality Gate Determination

**PASS Status Requirements:**
- Zero critical errors
- Zero significant errors
- Overall accuracy rate: 100%
- All G.R. numbers verified
- All quoted text matches source documents exactly
- All sources verified through authoritative databases

**FAIL Status Requirements:**
- Any critical errors present, OR
- Any significant errors present, OR
- Overall accuracy rate less than 100%, OR
- Any missing G.R. numbers, OR
- Any misquoted text, OR
- Any unverifiable sources

**Overall Status:** PASS (Ready for parliamentary submission) or FAIL (Requires corrections)
