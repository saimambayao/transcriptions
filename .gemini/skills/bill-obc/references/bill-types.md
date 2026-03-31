# Legislative Document Templates

Standardized formatting templates for Bangsamoro legislative documents based on official Parliament publications.

---

## Document Type Overview

| Document Type | Description | Status | Requires CM Approval |
|---------------|-------------|--------|----------------------|
| **Bill** | Proposed legislation under deliberation | Draft/Pending | No |
| **BAA** | Enacted Bangsamoro Autonomy Act | Law | Yes |
| **Resolution** | Parliamentary sense/action, non-legislative | Adopted | No |

---

## 1. BANGSAMORO AUTONOMY ACT (BAA) Template

BAAs are enacted laws that have been passed by the Parliament and approved by the Chief Minister.

### Header Structure

```
[Top Left Corner]
BILL NO. [ORIGINAL BILL NUMBER]

[Centered Header]
                    Republic of the Philippines
                    **BANGSAMORO PARLIAMENT**
           Bangsamoro Autonomous Region in Muslim Mindanao
                  BARMM Compound, Cotabato City
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                **BANGSAMORO TRANSITION AUTHORITY**
                   **(FIRST REGULAR SESSION)**

               **BANGSAMORO AUTONOMY ACT NO. [N]**

  Begun and held in Cotabato City, on [Day], the [Date] day of [Month], [Year].
```

### Full BAA Template

```markdown
BILL NO. [ORIGINAL NUMBER]

Republic of the Philippines
**BANGSAMORO PARLIAMENT**
Bangsamoro Autonomous Region in Muslim Mindanao
BARMM Compound, Cotabato City

---

**BANGSAMORO TRANSITION AUTHORITY**
**([SESSION] REGULAR SESSION)**

**BANGSAMORO AUTONOMY ACT NO. [NUMBER]**

Begun and held in Cotabato City, on [Day], the [Date] day of [Month], [Year].

**AN ACT**
**[FULL TITLE IN UPPERCASE DESCRIBING THE ACT AND FOR OTHER PURPOSES]**

_Be it enacted by the Bangsamoro Transition Authority Parliament in session assembled:_

**SECTION 1.** ***Short Title.*** – This Act shall be known as the "[Short Title] Act of [Year]".

**SEC. 2.** ***Declaration of Policy.*** – [Policy statement describing the state's intent and objectives].

**SEC. 3.** ***Definition of Terms.*** – For purposes of this Act, the following terms shall mean:

a. "[Term]" – [Definition];

b. "[Term]" – [Definition];

c. "[Term]" – [Definition].

**SEC. 4.** ***[Section Title].*** – [Section content].

[Include as many substantive sections as needed, numbered sequentially]

**SEC. [N].** ***Appropriations.*** – [Funding provisions if applicable, amounts in words and figures].

**SEC. [N+1].** ***Implementing Rules and Regulations.*** – Within [number] days from the effectivity of this Act, the [designated agency] shall promulgate the necessary rules and regulations for the effective implementation of this Act.

**SEC. [N+2].** ***Separability Clause.*** – If any provision of this Act is declared unconstitutional or invalid, the remainder of this Act or the provisions not otherwise affected shall remain in full force and effect.

**SEC. [N+3].** ***Repealing Clause.*** – All laws, decrees, orders, rules and regulations or parts thereof inconsistent with this Act are hereby repealed or modified accordingly.

**SEC. [N+4].** ***Effectivity.*** – This Act shall take effect fifteen (15) days after its publication in a newspaper of regional circulation in the Bangsamoro Autonomous Region in Muslim Mindanao.

**APPROVED.**

(Sgd.)
**ATTY. ALI PANGALIAN M. BALINDONG**
Speaker

This Act was passed by the Bangsamoro Parliament on [Gregorian Date].

(Sgd.)
**PROF. RABY B. ANGKAL**
Secretary-General

**APPROVED:**

(Sgd.)
**[CHIEF MINISTER NAME]**
Chief Minister
Date: [Approval Date and Time]
```

### BAA Formatting Rules

| Element | Format | Example |
|---------|--------|---------|
| Original Bill Reference | Plain text, top left | `BILL NO. 7` |
| Republic Header | Plain text, green*, centered | `Republic of the Philippines` |
| Parliament Name | **Bold**, centered | `**BANGSAMORO PARLIAMENT**` |
| Region Name | Plain text, green*, centered | `Bangsamoro Autonomous Region in Muslim Mindanao` |
| Location | Plain text, centered | `BARMM Compound, Cotabato City` |
| Body Name | **Bold**, centered | `**BANGSAMORO TRANSITION AUTHORITY**` |
| Session | **Bold**, parentheses | `**(FIRST REGULAR SESSION)**` |
| Act Number | **Bold**, centered | `**BANGSAMORO AUTONOMY ACT NO. 1**` |
| Session Date | Plain text | `Begun and held in Cotabato City, on Friday, the 29th day of March, 2019.` |
| "AN ACT" | **Bold**, UPPERCASE | `**AN ACT**` |
| Long Title | **Bold**, UPPERCASE | `**ADOPTING THE OFFICIAL FLAG OF THE...**` |
| Enacting Clause | _Italic_ | `_Be it enacted..._` |
| First Section | **Bold** `SECTION 1.` | `**SECTION 1.**` |
| Subsequent Sections | **Bold** `SEC. N.` | `**SEC. 2.**`, `**SEC. 3.**` |
| Section Title | ***Bold Italic*** with period | `***Short Title.***`, `***Declaration of Policy.***` |
| Section Dash | En-dash (–) | ` – ` (not hyphen) |
| Subsections | Lowercase letters, no parens | `a.`, `b.`, `c.` |
| Sub-subsections | Arabic numerals | `1.`, `2.`, `3.` |
| Signature Prefix | Plain text | `(Sgd.)` |
| Signer Name | **Bold** | `**ATTY. ALI PANGALIAN M. BALINDONG**` |
| Title | Plain text below name | `Speaker` |

> **\*Color Note:** In rendered documents (frontend), "Republic of the Philippines" and "Bangsamoro Autonomous Region in Muslim Mindanao" are displayed in green (`#009966` or `text-emerald-600`) to match official Parliament document styling. In plain markdown files, this is noted but cannot be rendered.

### Session Reference

Session numbering **restarts** when a new BTA term begins.

**BTA 1 (First BTA Officers, Begun March 29, 2019)**

| Session | Year | BAA Range |
|---------|------|-----------|
| FIRST REGULAR SESSION | 2019 | BAA 1-10 |
| SECOND REGULAR SESSION | 2020 | BAA 11-17 (starts BAA-11) |
| THIRD REGULAR SESSION | 2021 | BAA 18-24 (starts BAA-18) |
| FOURTH REGULAR SESSION | 2022 | BAA 25-31 (starts BAA-25) |

**BTA 2 (New Officers, Extended Term, Begun September 15, 2022)**

| Session | Years | BAA Range |
|---------|-------|-----------|
| FIRST REGULAR SESSION | 2022-2023 | BAA 32-35 (starts BAA-32) |
| SECOND REGULAR SESSION | 2023-2024 | BAA 36-58 (starts BAA-36) |
| THIRD REGULAR SESSION | 2024-2025 | BAA 59-75 (starts BAA-59) |
| FOURTH REGULAR SESSION | 2025-present | BAA 76+ (starts BAA-76) |

**Note:** The "Begun and held" date in BAA headers indicates the BTA term start:

- "March 29, 2019" = BTA 1
- "September 15, 2022" = BTA 2

### Bill Numbering System

**Important:** Bill numbering **restarted at Bill No. 1** when BTA 2 began (September 15, 2022).

| BTA Term | Bill Number Range | BAA Range | Status |
|----------|-------------------|-----------|--------|
| BTA 1 | Unknown sequence | BAA 1-31 | Bill numbers not yet documented |
| BTA 2 | Bill No. 1+ | BAA 32+ | Bill No. 1 = 1st Regular Session of BTA 2 |

**Known Bill-to-BAA Mappings (BTA 2):**

| BAA | Bill No. | Notes |
|-----|----------|-------|
| BAA-32 | 54 | |
| BAA-33 | 128 | |
| BAA-49 | 30 | |
| BAA-62 | 32 | |
| BAA-64 | 273 | |
| BAA-72 | 270, 281 | Consolidated from two bills |

**Known Bill-to-BAA Mappings (BTA 1 - from official documents):**

| BAA | Bill No. | Notes |
|-----|----------|-------|
| BAA-4 | 35 | Bangsamoro Human Rights Act of 2019 |
| BAA-13 | 60 | |
| BAA-17 | 59 | |
| BAA-18 | 70 | |

> **Note:** BAA 1-31 bill numbers require verification from official Parliament archives as BTA 1 used a different bill numbering system.

### Standard Clauses (Boilerplate)

These clauses appear in most BAAs in this order at the end:

1. **Appropriations** (if funding is needed)
2. **Implementing Rules and Regulations** (if IRR required)
3. **Separability Clause** (mandatory)
4. **Repealing Clause** (mandatory)
5. **Effectivity Clause** (mandatory)

---

## 2. PARLIAMENT BILL Template

Bills are proposed legislation under deliberation. They become BAAs when enacted. Bill formatting follows BAA styling as closely as practicable.

### Bill Types

| Type | Description | Structure |
|------|-------------|-----------|
| **With Explanatory Note** | Bills with author's explanation of purpose/rationale | Header → Explanatory Note → Bill Text |
| **Without Explanatory Note** | Bills that go directly to provisions | Header → Bill Text only |

---

### 2A. Bill WITH Explanatory Note

Bills with Explanatory Notes have two sections, each starting with the full header block:
1. **Explanatory Note** - Author's rationale, ending with signature
2. **Bill Text** - Full header repeated, then enacting clause and provisions

```markdown
BILL NO. [NUMBER]

Republic of the Philippines
**BANGSAMORO PARLIAMENT**
Bangsamoro Autonomous Region in Muslim Mindanao
BARMM Compound, Cotabato City

---

**BANGSAMORO TRANSITION AUTHORITY**
**([SESSION] REGULAR SESSION)**

**Parliament Bill No. [NUMBER]**

Authored by
**[AUTHOR NAME WITH TITLE]**

Co-authored by
**[CO-AUTHOR NAMES]**

**AN ACT**
**[FULL TITLE IN UPPERCASE DESCRIBING THE BILL AND FOR OTHER PURPOSES]**

**EXPLANATORY NOTE**

[Paragraph 1: Context and background - the problem or gap the bill addresses]

[Paragraph 2: Legal basis - relevant constitutional or statutory provisions]

[Paragraph 3: Proposed solution and expected benefits]

[Paragraph 4: Supporting evidence, statistics, or precedents]

For these reasons, this representation earnestly asks for the approval of the bill.

(Sgd.)
**[PRINCIPAL AUTHOR NAME]**
Member of the Parliament – Bangsamoro Transition Authority

---

BILL NO. [NUMBER]

Republic of the Philippines
**BANGSAMORO PARLIAMENT**
Bangsamoro Autonomous Region in Muslim Mindanao
BARMM Compound, Cotabato City

---

**BANGSAMORO TRANSITION AUTHORITY**
**([SESSION] REGULAR SESSION)**

**Parliament Bill No. [NUMBER]**

Authored by
**[AUTHOR NAME WITH TITLE]**

Co-authored by
**[CO-AUTHOR NAMES]**

**AN ACT**
**[FULL TITLE IN UPPERCASE DESCRIBING THE BILL AND FOR OTHER PURPOSES]**

_Be it enacted by the Bangsamoro Transition Authority Parliament in session assembled:_

**SECTION 1.** ***Short Title.*** – This Act shall be known as the "[Short Title] Act of [Year]".

**SEC. 2.** ***Declaration of Policy.*** – [Policy statement describing the state's intent and objectives].

**SEC. 3.** ***Definition of Terms.*** – For purposes of this Act, the following terms shall mean:

a. "[Term]" – [Definition];

b. "[Term]" – [Definition];

c. "[Term]" – [Definition].

**SEC. 4.** ***[Section Title].*** – [Section content].

[Include as many substantive sections as needed, numbered sequentially]

**SEC. [N].** ***Appropriations.*** – [Funding provisions if applicable].

**SEC. [N+1].** ***Implementing Rules and Regulations.*** – Within [number] days from the effectivity of this Act, the [designated agency] shall promulgate the necessary rules and regulations.

**SEC. [N+2].** ***Separability Clause.*** – If any provision of this Act is declared unconstitutional or invalid, the remainder shall remain in full force and effect.

**SEC. [N+3].** ***Repealing Clause.*** – All laws, decrees, orders, rules and regulations inconsistent with this Act are hereby repealed or modified accordingly.

**SEC. [N+4].** ***Effectivity.*** – This Act shall take effect fifteen (15) days after its publication in a newspaper of regional circulation.

**APPROVED.**

Author:

(Sgd.)
**[PRINCIPAL AUTHOR NAME]**
Member of the Parliament

Co-authors:

(Sgd.)
**[CO-AUTHOR 1 NAME]**
Member of the Parliament

(Sgd.)
**[CO-AUTHOR 2 NAME]**
Member of the Parliament
```

---

### 2B. Bill WITHOUT Explanatory Note

Bills without Explanatory Notes go directly from the header to the bill provisions.

```markdown
BILL NO. [NUMBER]

Republic of the Philippines
**BANGSAMORO PARLIAMENT**
Bangsamoro Autonomous Region in Muslim Mindanao
BARMM Compound, Cotabato City

---

**BANGSAMORO TRANSITION AUTHORITY**
**([SESSION] REGULAR SESSION)**

**Parliament Bill No. [NUMBER]**

Authored by
**[AUTHOR NAME WITH TITLE]**

Co-authored by
**[CO-AUTHOR NAMES]**

**AN ACT**
**[FULL TITLE IN UPPERCASE DESCRIBING THE BILL AND FOR OTHER PURPOSES]**

---

_Be it enacted by the Bangsamoro Transition Authority Parliament in session assembled:_

**SECTION 1.** ***Short Title.*** – This Act shall be known as the "[Short Title] Act of [Year]".

**SEC. 2.** ***Declaration of Policy.*** – [Policy statement].

**SEC. 3.** ***Definition of Terms.*** – For purposes of this Act:

a. "[Term]" – [Definition];

b. "[Term]" – [Definition].

[Additional substantive sections...]

**SEC. [N].** ***Separability Clause.*** – If any provision of this Act is declared unconstitutional, the remainder shall not be affected.

**SEC. [N+1].** ***Repealing Clause.*** – All inconsistent laws are hereby repealed or modified accordingly.

**SEC. [N+2].** ***Effectivity.*** – This Act shall take effect fifteen (15) days after its publication.

**APPROVED.**

Author:

(Sgd.)
**[AUTHOR NAME]**
Member of the Parliament

Co-authors:

(Sgd.)
**[CO-AUTHOR 1]**
Member of the Parliament
```

---

### Bill Formatting Rules

| Element | Format | Example |
|---------|--------|---------|
| Bill Reference | Plain text, top left | `BILL NO. 170` |
| Republic Header | Plain text, centered | `Republic of the Philippines` |
| Parliament Name | **Bold**, centered | `**BANGSAMORO PARLIAMENT**` |
| Region Name | Plain text, centered | `Bangsamoro Autonomous Region in Muslim Mindanao` |
| Location | Plain text, centered | `BARMM Compound, Cotabato City` |
| Body Name | **Bold**, centered | `**BANGSAMORO TRANSITION AUTHORITY**` |
| Session | **Bold**, parentheses, UPPERCASE | `**(FIRST REGULAR SESSION)**` |
| Bill Number | **Bold** | `**Parliament Bill No. 170**` |
| "Authored by" | Plain text | Line before author name |
| Author Name | **Bold** with honorific | `**MP ENGR. DON MUSTAPHA A. LOONG**` |
| "Co-authored by" | Plain text | Line before co-author names |
| Co-author Names | **Bold** | `**MPs ATTY. LAISA M. ALAMIA, ...**` |
| "AN ACT" | **Bold**, UPPERCASE | `**AN ACT**` |
| Long Title | **Bold**, UPPERCASE | `**PROVIDING FOR THE RECOGNITION OF...**` |
| Horizontal Rule | `---` | Separates sections |
| Explanatory Note Header | **Bold** | `**EXPLANATORY NOTE**` |
| Explanatory Content | Plain text paragraphs | Indented, justified |
| Signature Prefix | Plain text | `(Sgd.)` |
| Enacting Clause | _Italic_ | `_Be it enacted..._` |
| First Section | **Bold** `SECTION 1.` | `**SECTION 1.**` |
| Subsequent Sections | **Bold** `SEC. N.` | `**SEC. 2.**`, `**SEC. 3.**` |
| Section Title | ***Bold Italic*** with period | `***Short Title.***` |
| Section Dash | En-dash with spaces | ` – ` (not hyphen) |
| Subsections | Lowercase letters with period | `a.`, `b.`, `c.` |
| Sub-subsections | Arabic numerals | `1.`, `2.`, `3.` |
| Approval | **Bold**, UPPERCASE | `**APPROVED.**` |

### Key Differences: Bill vs BAA

| Element | Bill | BAA |
|---------|------|-----|
| Document Reference | `BILL NO. X` | `BILL NO. X` (original bill) |
| Title | `**Parliament Bill No. X**` | `**BANGSAMORO AUTONOMY ACT NO. X**` |
| Session Date Line | Not included | `Begun and held in Cotabato City, on...` |
| Explanatory Note | Present (if authored with one) | Not included |
| Speaker/Secretary Approval | At end (attestation) | Full signature block with dates |
| Chief Minister | Not included | **APPROVED:** with date/time |

### Explanatory Note Guidelines

The Explanatory Note should:
1. **Establish legal basis** - Reference constitutional provisions, RA 11054, or existing laws
2. **Identify the problem** - What gap or issue does the bill address?
3. **Propose the solution** - How does the bill solve the identified problem?
4. **Provide justification** - Statistics, studies, or precedents supporting the bill
5. **Close with appeal** - "For these reasons, this representation earnestly asks for the approval of the bill."

**Signature after Explanatory Note:**
- Principal author signs after the Explanatory Note
- Format: `(Sgd.)` followed by **bold name** and title
- Title: "Member of the Parliament – Bangsamoro Transition Authority"

---

## 3. RESOLUTION Template

Resolutions are non-legislative measures expressing the sense, will, or action of Parliament.

### Resolution Types

| Type | Purpose | Example |
|------|---------|---------|
| Simple Resolution | Internal Parliament matters | Approving parliamentary budget |
| Concurrent Resolution | Expressing Parliament's position | Urging government action |
| Joint Resolution | Parliamentary-Executive coordination | Commemorations, policy directives |

### Resolution Template

```markdown
Republic of the Philippines
Bangsamoro Autonomous Region in Muslim Mindanao
**BANGSAMORO PARLIAMENT**
Bangsamoro Government Center, Cotabato City

**[SESSION] REGULAR SESSION**

**RESOLUTION NO. <u>[NUMBER]</u>**

**[RESOLUTION TITLE IN UPPERCASE - A CONCISE STATEMENT OF THE RESOLUTION'S PURPOSE]**

**WHEREAS,** [First whereas clause establishing context or background];

**WHEREAS,** [Second whereas clause providing additional background or legal basis];

**WHEREAS,** [Third whereas clause stating the specific circumstances or need];

**WHEREAS,** [Continue with additional whereas clauses as needed];

**NOW, THEREFORE,** be it

**RESOLVED,** as it is hereby resolved by the Bangsamoro Transition Authority, [main resolution action statement].

**RESOLVED, FURTHER,** [additional resolution action if needed].

**RESOLVED, FINALLY,** [final resolution action if needed].

**ADOPTED,** [Month Day, Year].

                                        Certified Correct:

                                        **PROF. RABY B. ANGKAL**
                                        Secretary-General

Attested:

**ATTY. ALI PANGALIAN M. BALINDONG**
Speaker

/PR[NUMBER]
```

### Resolution Formatting Rules

| Element | Format | Example |
|---------|--------|---------|
| Session | **Bold**, UPPERCASE | `**SECOND REGULAR SESSION**` |
| Resolution Number | **Bold**, number underlined | `**RESOLUTION NO. <u>113</u>**` |
| Resolution Title | **Bold**, UPPERCASE | `**RESOLUTION EXPRESSING FULL SUPPORT...**` |
| "WHEREAS," | **Bold** (including comma) | `**WHEREAS,**` |
| Whereas content | Plain text | Follows bold comma, ends with semicolon |
| "NOW, THEREFORE," | **Bold** (including comma) | `**NOW, THEREFORE,** be it` |
| "be it" | Plain text | Follows "NOW, THEREFORE," on same line |
| "RESOLVED," | **Bold** (including comma) | `**RESOLVED,** as it is hereby resolved...` |
| "RESOLVED, FURTHER," | **Bold** (including comma) | Optional additional clauses |
| "RESOLVED, FINALLY," | **Bold** (including comma) | Optional final clause |
| "ADOPTED," | **Bold** (including comma) | `**ADOPTED,** March 17, 2021.` |
| Adoption Date | Gregorian only | `March 17, 2021.` |
| Certified Correct | Right-aligned | Secretary-General signs here |
| Attested | Left-aligned | Speaker signs here |
| PR Reference | Plain text, bottom left | `/PR395` |

### Whereas Clause Guidelines

- Each WHEREAS clause should cover ONE topic or point
- End each clause with a semicolon (;) except the last before "NOW, THEREFORE"
- Last WHEREAS clause before resolution ends with colon (:)
- Keep clauses factual and reference legal bases where applicable
- Common patterns:
  - Legal authority: "WHEREAS, Section X of [Law] provides that..."
  - Background: "WHEREAS, the [entity] conducted..."
  - Context: "WHEREAS, the Bangsamoro region faces..."

---

## 4. Common Formatting Standards

### Typography Guide

| Style | Usage | Markdown |
|-------|-------|----------|
| **Bold** | Headers, titles, names, key terms | `**text**` |
| _Italic_ | Section titles, emphasized terms, foreign words, enacting clause | `_text_` |
| **Bold** + _Italic_ | Not typically combined in BTA documents | Avoid |
| UPPERCASE | Act titles, session names, formal headers, resolution titles | Direct typing |
| lowercase | Subsection letters | `a.`, `b.`, `c.` |

### Punctuation Standards

| Element | Standard | Example |
|---------|----------|---------|
| Section dash | En-dash with spaces | ` – ` (not hyphen `-`) |
| Subsection markers | Lowercase letters with period | `a.`, `b.`, `c.` |
| Sub-subsection markers | Arabic numerals with period | `1.`, `2.`, `3.` |
| Item lists within text | Semicolons between items | `item one; item two; and item three.` |
| Final list item | "and" before last item | `a. First; b. Second; and c. Third.` |
| Legal references | No italics for law names | `Republic Act No. 11054` |
| Short titles in text | Quotes and italics | `"_Bangsamoro Organic Law_"` |

### Number Formatting

| Type | Format | Example |
|------|--------|---------|
| Currency | Words + (Symbol + Figures) | `Five Million Pesos (₱5,000,000.00)` |
| Percentages | Figures + words in parens | `sixty percent (60%)` |
| Days/Time periods | Words + (Figures) | `fifteen (15) days` |
| Section references | Figures | `Section 4`, `SEC. 12` |
| Year | Four digits | `2024`, not `'24` |

### Date Formats

| Context | Format | Example |
|---------|--------|---------|
| Session Date | Full text | `Friday, the 29th day of March, 2019` |
| Adoption Date (Dual) | Hijri/Gregorian | `Jumada Al-Ula 16, 1443/December 21, 2021` |
| Adoption Date (Single) | Gregorian | `December 23, 2020` |
| Approval Date | Date + Time | `Aug. 28, 2019, 10:31 AM` |
| References in text | Month Day, Year | `August 17, 2021` |

### Standard Signatories

**BTA Parliament (2019-Present):**
- Speaker: **ATTY. ALI PANGALIAN M. BALINDONG**
- Secretary-General: **PROF. RABY B. ANGKAL**

**Chief Minister:**
- Current: **AHOD BALAWAG EBRAHIM** (also written as **AHOD B. EBRAHIM**)

---

## 5. File Naming Conventions

| Document Type | Pattern | Example |
|---------------|---------|---------|
| BAA (Enacted) | `BAA-[NUMBER].md` | `BAA-1.md`, `BAA-77.md` |
| Bill (Filed) | `BILL[NUMBER].md` | `BILL170.md`, `BILL240.md` |
| Resolution | `resolution[NUMBER].md` | `resolution100.md`, `resolution200.md` |
| Index Files | `INDEX.md` | `INDEX.md` |

---

## 6. Validation Checklist

### For BAAs

- [ ] Original Bill Number included at top left
- [ ] Header matches: Republic > Parliament > BARMM > Location
- [ ] Session name matches the year
- [ ] Act number is sequential and correct
- [ ] Session date is accurate
- [ ] "AN ACT" and long title are in UPPERCASE and **bold**
- [ ] Enacting clause is in _italics_
- [ ] First section uses `SECTION 1.` (full word)
- [ ] Subsequent sections use `SEC.` (abbreviated)
- [ ] Section titles are in _italics_ followed by period
- [ ] En-dash (–) used after section titles, not hyphen (-)
- [ ] Subsections use lowercase letters: `a.`, `b.`, `c.`
- [ ] Standard clauses present (Separability, Repealing, Effectivity)
- [ ] All signatures include `(Sgd.)` prefix
- [ ] Names are in **bold**
- [ ] Chief Minister approval includes date and time

### For Bills

- [ ] Bill number is correct
- [ ] Author and co-author names are listed
- [ ] Explanatory Note is present
- [ ] All sections match BAA formatting rules
- [ ] Author signature appears after Explanatory Note
- [ ] Certification signatures at end

### For Resolutions

- [ ] Session name is correct for the year
- [ ] Resolution number is sequential
- [ ] Title is descriptive and in UPPERCASE
- [ ] All WHEREAS clauses start with **bold** "WHEREAS,"
- [ ] "NOW, THEREFORE, be it" is on its own line
- [ ] RESOLVED clauses properly formatted
- [ ] ADOPTED date uses appropriate calendar format
- [ ] PR reference number included at end (`/PR###`)

---

## 7. Examples from Official Documents

### Example: BAA Section Formatting

From BAA No. 1 (Official Flag Act):

```markdown
**SECTION 1.** _Adoption of the Official Flag._ – Pursuant to Section 2 Article II of RA 11054, there is hereby adopted an Official Flag of the Bangsamoro Autonomous Region in Muslim Mindanao (BARMM), hereinafter referred to as the Bangsamoro Flag.

**SEC. 2.** _Declaration of Policy._ – In the exercise of its right to self-governance, the Bangsamoro Autonomous Region in Muslim Mindanao is free to adopt its Bangsamoro Flag that is reflective of its peoples' identity, history, heritage, struggles and aspiration.

**SEC. 3.** _Design, Symbolism, and interpretation._ – The Bangsamoro Flag shall be in the shape and dimension of a standard flag, three (3) feet by five-and-a-half (5½) feet, and shall contain four (4) distinctive colors, a Crescent, a seven-rayed Star, and a Kris. The said colors and symbols be interpreted as follows:

a. The top side portion of the whole length of the Bangsamoro Flag shall be in green (HEX CODE: #009966) and occupies one-third (1/3) of the whole flag. It reflects the Islamic teachings and principles that majority of the population subscribe to.

b. The middle portion of the length of the Bangsamoro Flag shall be in white (HEX CODE: #FFFFFF), signifying peace, sakina (tranquility) and righteousness. It shall likewise occupy one-third (1/3) of the whole flag.
```

### Example: Resolution Formatting

From Resolution No. 113 (COVID-19 Vaccination Support):

```markdown
**WHEREAS,** the COVID-19 pandemic continues to spread throughout practically all nooks and corners of the world, in the Philippines including the BARMM areas, thus persisting to create social and economic havoc and threat to human lives;

**WHEREAS,** under the principle of moral governance, the BARMM government ensures the conduct and implementation of its duties and responsibilities as prescribed under Section 22, Article IX of Republic Act No. 11054 otherwise known as the "Organic Law for the Bangsamoro Autonomous Region in Muslim Mindanao", that is to provide for a comprehensive and integrated health service delivery for its constituents...;

**WHEREAS,** there is a need to elicit the full support and participation of all government units, agencies and instrumentalities, concerned private sector as well as the entire Bangsamoro constituents to the afore-mentioned vaccination plans including but not limited to the aspect of risk communication and community engagement to enhance community awareness on the importance of the program;

**NOW, THEREFORE,** be it

**RESOLVED,** as it is hereby resolved by the Bangsamoro Transition Authority, to express full support to the National and MOH-BARMM deployment and vaccination plans for covid-19 vaccines and urging all government units, agencies and instrumentalities in the Bangsamoro Autonomous Region to provide full cooperation including advocacy, education and information campaign for its successful implementation.

**RESOLVED, FURTHER,** to forward this Resolution to all Bangsamoro Ministries, for information and appropriate consideration.

**ADOPTED,** March 17, 2021.
```

---

## 8. Quick Reference Card

### BAA Structure
```
1. Bill Reference (top left)
2. Header Block (centered)
3. Body & Session
4. Act Number
5. Session Date
6. "AN ACT" + Long Title
7. Enacting Clause
8. SECTION 1. _Title._ – Content
9. SEC. 2-N. _Title._ – Content
10. Standard Clauses (Appropriations, IRR, Separability, Repealing, Effectivity)
11. Speaker Signature
12. Secretary-General Attestation
13. Chief Minister Approval
```

### Bill Structure
```
1. Header Block
2. Body & Session
3. Bill Number
4. Author/Co-authors
5. "AN ACT" + Long Title
6. Explanatory Note
7. Author Signature
8. Bill Text (same as BAA body)
9. Author/Co-author Signatures
10. Secretary-General Certification
11. Speaker Attestation
```

### Resolution Structure
```
1. Header Block (with Parliament seals)
2. Session (bold, centered)
3. Resolution Number (bold, number underlined)
4. Resolution Title (bold, uppercase, centered)
5. WHEREAS Clauses (3+ typical, each ends with semicolon)
6. NOW, THEREFORE, be it
7. RESOLVED Clause(s)
8. ADOPTED, [Date].
9. Certified Correct: (right) - Secretary-General
10. Attested: (left) - Speaker
11. /PR[NUMBER] (bottom left)
```
