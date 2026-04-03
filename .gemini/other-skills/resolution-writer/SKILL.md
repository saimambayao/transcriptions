---
name: resolution-writer
description: "Draft complete Bangsamoro Parliament resolutions from scratch. Use when the user requests drafting, writing, or creating parliamentary resolutions for the Bangsamoro Parliament (BARMM). Supports all resolution types per BTA Parliament Approved Resolution No. 268 (Simple, Concurrent, Joint Committee). Resolutions are also organized by practical purpose-based categories: internal/procedural, commendatory, policy/statement, and budget/financial. Conducts research to create properly formatted resolutions with accurate WHEREAS clauses and RESOLVED directives following Bangsamoro parliamentary procedures and legal hierarchy (Constitution, BOL, National Laws, Bangsamoro Administrative Code, Bangsamoro Autonomy Acts)."
---

# Resolution Writer for Bangsamoro Parliament

Draft complete, properly formatted resolutions for the Bangsamoro Parliament based on user-specified topics.

## Quick Start

When a user requests a resolution:

1. **Clarify the request** - Ask about:
   - Topic/subject matter
   - Purpose (commend, investigate, urge action, approve budget, etc.)
   - Any specific details or requirements

2. **Assess research needs** - Determine if comprehensive background research is needed (see Two-Tier Research Approach below)

3. **Invoke deepresearch skill (if needed)** - For complex policy topics, use deepresearch skill to conduct comprehensive 4-phase research with 30+ sources

4. **Conduct focused legal validation** - Verify constitutional/BOL provisions, validate factual claims, ensure citation accuracy

5. **Determine resolution type and category** - See [references/resolution-categories.md](references/resolution-categories.md)

6. **Draft the resolution** - Use appropriate template from [assets/](assets/), incorporating research findings

7. **Review and refine** - Ensure format compliance per [references/format-guide.md](references/format-guide.md)

8. **Save the resolution** - Write completed resolution to `/Users/saidamenmambayao/apps/Parliamentarian/Proposed-Resolutions/` with descriptive filename

## Resolution Types and Categories

**Per BTA Parliament Approved Resolution No. 268, there are three (3) official resolution TYPES:**
- Type 1: Simple Resolution (most common)
- Type 2: Concurrent Resolution (joint with Cabinet)
- Type 3: Joint Committee Resolution (multiple committees)

**Additionally, for practical organization, resolutions are classified by purpose-based CATEGORIES**:
- Internal/Procedural
- Commendatory/Recognition
- Policy/Statement
- Budget/Financial
- Other categories

See [references/resolution-categories.md](references/resolution-categories.md) for detailed descriptions, selection guidance, and when to use each type and category.

## Two-Tier Research Approach

This skill uses a **two-tier research methodology** to ensure comprehensive, accurate resolutions:

**Tier 1: Comprehensive Foundation Research (deepresearch skill)**
- Comprehensive 4-phase research with 30+ sources
- Constitutional provisions, BOL authority, national laws, jurisprudence
- Policy context, statistical data, stakeholder analysis
- Comparative best practices from other jurisdictions
- Implementation feasibility assessment
- Produces detailed research report with numbered citations

**Tier 2: Focused Legal Validation (this skill)**
- Validates Tier 1 research findings for accuracy
- Verifies constitutional and BOL citations are exact
- Cross-checks factual claims against sources
- Ensures legal hierarchy is respected
- Identifies any gaps or errors from Tier 1
- Focuses on legal precision and citation accuracy

### When to Use Deepresearch (Tier 1)

**USE deepresearch for:**
- **Policy/statement resolutions** requiring substantial background on complex governance issues
- **Resolutions addressing new or emerging topics** without clear precedents
- **Resolutions with significant legal/constitutional questions** requiring jurisprudence research
- **Comparative research needs** - learning from other jurisdictions' approaches
- **Implementation feasibility questions** - fiscal impact, capacity assessment
- **User explicitly requests** comprehensive research or "research about [topic]"

**SKIP deepresearch for:**
- **Simple commendatory resolutions** with clear, verifiable achievements
- **Routine internal/procedural resolutions** with established precedents
- **Urgent/time-sensitive resolutions** requiring quick turnaround
- **Well-established topics** where facts and legal authority are already clear
- **Minor recognition resolutions** with straightforward biographical information

### Two-Tier Research Workflow

**Option A: With Deepresearch (Complex Topics)**
1. Clarify user request
2. Invoke deepresearch skill with research question
3. Review deepresearch report (saved to Research-Reports/)
4. Conduct focused legal validation (Step 1 below)
5. Draft resolution using both research tiers
6. Review and save

**Option B: Direct Drafting (Simple Topics)**
1. Clarify user request
2. Conduct focused legal validation directly (Step 1 below)
3. Draft resolution using validated research
4. Review and save

**Benefits of two-tier approach:**
- Deepresearch provides comprehensive foundation (Tier 1)
- Resolution-writer validates and catches errors (Tier 2)
- Legal citations verified twice for 100% accuracy
- Factual claims supported by extensive sources
- Reduces risk of inaccuracies in final resolution

## Drafting Workflow

### Step 0: Assess Research Needs and Invoke Deepresearch (If Needed)

**Before beginning drafting, assess whether deepresearch is needed:**

**Decision criteria:**
- Is this a policy/statement resolution on a complex topic? → Use deepresearch
- Does the topic require comparative analysis? → Use deepresearch
- Are there significant legal/constitutional questions? → Use deepresearch
- Is this a simple commendatory or routine procedural matter? → Skip deepresearch
- Did the user request "research about [topic]"? → Use deepresearch

**If deepresearch is needed:**

1. **Formulate research question** based on resolution topic
   - Example: "Research about the constitutional and legal framework for establishing a Shari'ah Division under the Policy Research and Legal Services"

2. **Invoke deepresearch skill** using the Skill tool:
   ```
   Use deepresearch skill with research question: [formulated question]
   ```

3. **Wait for deepresearch completion** - Deepresearch will:
   - Conduct comprehensive 4-phase research (30+ sources)
   - Produce detailed research report with executive summary
   - Save report to Research-Reports/ directory
   - Provide key findings and recommendations

4. **Review deepresearch report** - Note:
   - Constitutional and BOL provisions identified
   - Key factual findings and statistics
   - Comparative examples and best practices
   - Implementation considerations
   - Numbered citations for all claims

5. **Proceed to Step 1** with deepresearch report as foundation

**If deepresearch is NOT needed:**
- Proceed directly to Step 1 for focused legal validation

### Step 1: Focused Legal Validation and Verification

**This step conducts targeted research to validate findings (if using deepresearch) or gather essential information (if not using deepresearch).**

**Use WebSearch, WebFetch, and Read tools** for focused validation. The goal is **legal precision and accuracy verification.**

**Validation follows three phases:**

**A. Legal Validation** - Verify legal authority following Philippine legal hierarchy:

**If using deepresearch report:**
1. **Verify Constitutional provisions** - Cross-check that quoted constitutional text is exact
   - Use WebFetch(officialgazette.gov.ph) to verify Article X, Section 15 and other provisions
   - Confirm deepresearch citations match official Constitution text word-for-word

2. **Verify BOL provisions** - Cross-check that quoted BOL text is exact
   - Use WebFetch(lawphil.net) to verify BOL Article VI and other provisions
   - Confirm deepresearch citations match official RA 11054 text word-for-word

3. **Verify National Laws** - Confirm Republic Act numbers and provisions are accurate
   - Spot-check key statutory citations against official texts
   - Verify statute numbers, article/section references

4. **Verify Jurisprudence** - Confirm G.R. numbers and case holdings are accurate
   - Use WebFetch(sc.judiciary.gov.ph, lawphil.net) to verify complete G.R. numbers
   - Confirm case names, decision dates, legal principles match official decisions

5. **Verify Bangsamoro Autonomy Acts** - Confirm BAA numbers and provisions
   - Cross-check against official Bangsamoro Gazette or Parliament records

**If NOT using deepresearch (conducting original research):**
1. **Research Constitutional provisions (MANDATORY)** - Establish constitutional basis
2. **Research BOL provisions (MANDATORY)** - Cite specific BOL authority
3. **Research National Laws** - Related national legislation
4. **Research Related Jurisprudence** - When applicable and supports the resolution
5. **Research Bangsamoro Autonomy Acts** - Related regional legislation

**B. Factual Validation** - Verify or collect specific facts about the subject matter:

**If using deepresearch report:**
- Cross-check key statistics against original sources
- Verify dates and timelines mentioned
- Confirm organizational facts (establishment dates, structures, mandates)
- Spot-check 3-5 major factual claims for accuracy

**If NOT using deepresearch:**
- **Commendatory:** Full name, 3+ achievements with dates, impact, background
- **Policy/Statement:** Problem statement, 2-3 examples/statistics, current status
- **Budget/Financial:** Exact amount, purpose, source of funds, beneficiaries
- **Internal/Procedural:** Current structure, gaps, expected improvements

**C. Contextual Validation** - Verify or gather supporting context:

**If using deepresearch report:**
- Review comparative examples for BARMM applicability
- Verify implementation feasibility considerations
- Check parliamentary precedents cited

**If NOT using deepresearch:**
- Parliamentary precedents
- Best practices from other legislatures
- Stakeholder positions
- Academic studies
- Cultural/traditional context

**Quality standards for validation:**
- All constitutional and BOL quotes must be exact (zero tolerance for paraphrasing)
- All G.R. numbers must be complete and accurate
- All factual claims must be verifiable with at least one source
- If any deepresearch finding cannot be verified, conduct additional research to correct it

**See [references/research-guide.md](references/research-guide.md)** for the complete research methodology including:
- Legal hierarchy and citation guide for each source
- Three-tiered research approach (basic, standard, comprehensive)
- Source priorities and search strategies
- Quality standards and verification requirements

### Step 2: Structure the Resolution

All resolutions follow this structure (see [references/format-guide.md](references/format-guide.md)):

1. **Header** - Standard format with "**PROPOSED RESOLUTION NO. ___**" (bold)
2. **Title** - Clear, descriptive, ALL CAPS, in bold
3. **Authorship** - "**Authored by:**" (bold) followed by author names or placeholders
4. **WHEREAS Clauses** - Build logical argument (10-14 clauses typical), with "**WHEREAS,**" in bold and superscript footnote numbers¹, ², ³, etc.
5. **RESOLVED Clauses** - State directives clearly with "**NOW, THEREFORE, BE IT RESOLVED,**", "**RESOLVED FURTHER,**", and "**RESOLVED FINALLY,**" in bold
6. **Footnotes** - All citations and sources listed at the end, AFTER all RESOLVED clauses (this is the standard parliamentary format)

**CRITICAL FORMATTING REQUIREMENT - CONTINUOUS FLOW:**

The entire resolution must be one flowing document without internal section header dividers. Do NOT include markdown headers like `## WHEREAS CLAUSES`, `## RESOLVED CLAUSE`, or `## FOOTNOTES`. The resolution should flow naturally from title → WHEREAS clauses → RESOLVED clauses → footnotes, separated only by blank lines. Do NOT use horizontal dividers (`---`) anywhere in the resolution. This creates a professional parliamentary document that reads smoothly without artificial section breaks or visual separators.

**FORMATTING REQUIREMENTS FOR RESOLUTION PRESENTATION:**

When formatting the final resolution document for printing or formal submission:

- **Header (BOLD):** The resolution number should be in bold. Example:

```text
**PROPOSED RESOLUTION NO. ___**
```

- **Title (ALL CAPS, BOLD):** The full title should be in ALL CAPS and bold, centered across the page, broken into multiple lines if necessary. Example:

```markdown
**A RESOLUTION
URGING THE BANGSAMORO PARLIAMENT SPEAKER
TO ESTABLISH A SHARI'AH DIVISION UNDER THE
POLICY RESEARCH AND LEGAL SERVICES TO STRENGTHEN
LEGISLATIVE SUPPORT FOR SHARI'AH-RELATED MATTERS**
```

- **Authorship (BOLD):** The "Authored by:" label should be in bold. Author names may be in regular or bold font. Example:

```markdown
**Authored by:**
MP ATTY. SITTIE FAHANIE S. UY-OYOD, MBA
```

- **WHEREAS and Operative Clauses:** Indent all WHEREAS clauses and operative clauses (NOW, THEREFORE... and RESOLVED clauses) from the left margin. Standard indentation is 0.5 to 1 inch (or equivalent spacing). Example:

```text
              WHEREAS, the 1987 Philippine Constitution, Article X, Section 15,
          provides that "There shall be created autonomous regions...";

              NOW, THEREFORE, BE IT RESOLVED, as it is hereby resolved by the
          Bangsamoro Parliament, to urge the BTA Parliament Speaker to establish
          a Shari'ah Division under the Policy Research and Legal Services;
```

- **Footnotes:** Footnotes may be left-aligned or indented consistently with the rest of the document. Maintain clear visual hierarchy with superscript numbers matching WHEREAS clause references.

### Step 3: Draft WHEREAS Clauses

**Principle:** WHEREAS clauses build a comprehensive, well-researched case for swift parliamentary approval grounded in constitutional and legal authority. More detail = fewer MP questions. Each clause must be substantive and value-adding. Omit only truly tangential facts; include all legally necessary background, factual context, and justification.

**MANDATORY RULE - EXACT LEGAL TEXT FROM EXACT SOURCES:** When citing any Constitutional, statutory, or jurisprudential provision, use the EXACT wording from the source document in quotation marks. Always cite the exact source with complete identification details. Do NOT paraphrase or interpret.

**THREE REQUIREMENTS:**

1. **Exact Legal Text** - Quote directly from the source in quotation marks
2. **Exact Citation** - Include statute number, article, section, and year
3. **Exact Source** - For court cases, ALWAYS include G.R. (Gazette Report) number, court name, and decision date

**STANDARD CITATION FORMAT FOR LEGAL BASES:**

**Format Structure:** Start with the provision identifier (Section X, Article Y), followed by "of the" and then the law.

**First mention of a law:**
- Include full statute number and official name
- Example: `Section 15, Article X, of the 1987 Philippine Constitution`
- Example: `Section 3, Article VII, of Republic Act No. 11054, otherwise known as the Bangsamoro Organic Law (BOL)`

**Subsequent mentions of the same law:**
- Use the established short title
- Example: `Section 5(a), Article VII, of the BOL`
- Example: `Section 1, Article X, of the BOL`
- Do NOT repeat the full law name once established

**Why this format:**
- Provision identifier comes first for clarity
- Consistent structure improves readability
- Short titles reduce repetition and improve flow

**EXAMPLES - CORRECT CITATIONS:**

Constitutional provisions (first mention):

- ✓ `Section 15, Article X, of the 1987 Philippine Constitution provides: "There shall be created autonomous regions..."`

Republic Acts (first mention):

- ✓ `Section 3, Article VII, of Republic Act No. 11054, otherwise known as the Bangsamoro Organic Law (BOL), vests in the Bangsamoro Parliament the authority to "enact laws on matters that are within the powers and competencies of the Bangsamoro Government"`

Republic Acts (subsequent mentions):

- ✓ `Section 5(a), Article VII, of the BOL further provides that...`
- ✓ `Section 1, Article X, of the BOL establishes that...`

Court decisions (WITH G.R. NUMBERS - REQUIRED):

- ✓ `Province of Sulu v. Executive Secretary, G.R. Nos. 242255, 243246, 243693, Supreme Court of the Philippines (September 3, 2024), held that [exact holding]`

**EXAMPLES - INCORRECT CITATIONS:**

- ❌ PARAPHRASED: "The Constitution grants autonomous regions the authority to enact laws"
- ❌ MISSING G.R. NUMBERS: "Supreme Court jurisprudence on autonomous regions' legislative authority"
- ❌ NO COURT NAME OR DATE: "A Supreme Court decision upheld the Bangsamoro Organic Law"
- ❌ INCOMPLETE: "Supreme Court cases on Bangsamoro legislative authority"

**CORRECT EQUIVALENT:**

- ✓ Include G.R. numbers: `G.R. Nos. 242255, 243246, 243693`
- ✓ Include court name: `Supreme Court of the Philippines`
- ✓ Include decision date: `(September 3, 2024)`
- ✓ Include exact legal principle: `held that [provision], thereby [principle]`

**MANDATORY: Constitutional and BOL provisions must always form the foundation. All other clauses build from this legal authority.**

**Structure a comprehensive progression (typically 10-13 clauses):**

1. **Philippine Constitutional Provision (MANDATORY)** - Cite the specific constitutional article/section that grants authority or relates to the resolution topic

   ```markdown
   **WHEREAS,** Section [Y], Article [X], of the 1987 Philippine Constitution provides that...
   ```

2. **Bangsamoro Organic Law Provision (MANDATORY)** - Cite the specific BOL article/section that grants Parliament authority or establishes the framework (include full name and establish BOL abbreviation on first mention)

   ```markdown
   **WHEREAS,** Section [Y], Article [X], of Republic Act No. 11054, otherwise known as the Bangsamoro Organic Law (BOL), establishes/provides that...
   ```

3. **Related BOL Provision(s)** - Cite additional BOL articles/sections that reinforce or expand on the authority/framework (when applicable) - Use BOL abbreviation for subsequent mentions

   ```markdown
   **WHEREAS,** Section [Z], Article [X], of the BOL further provides that...
   ```

4. **National Laws** - Cite applicable national legislation that relates to or coordinates with the resolution topic (when applicable)

   ```markdown
   **WHEREAS,** Republic Act [No. XXXX], which [establishes/authorizes/relates to], provides that...
   ```

5. **Related Jurisprudence** - Cite relevant court decisions, Supreme Court rulings, or legal precedents that support the resolution's legal basis (when applicable)

   ```markdown
   **WHEREAS,** in [Case Name], [Court], the [Court] ruled that [principle/holding relevant to resolution], thereby establishing precedent that...
   ```

6. **Bangsamoro Autonomy Acts** - Cite existing Bangsamoro Autonomy Acts that implement BOL provisions or relate to the resolution topic (when applicable)

   ```markdown
   **WHEREAS,** Bangsamoro Autonomy Act [No. XX], which [establishes/addresses], provides that...
   ```

7. **Institutional Context** - Describe the organization, structure, or existing framework relevant to the action

   ```markdown
   **WHEREAS,** [institution/office] was established to [purpose] and currently operates as follows: [details on structure, divisions, mandate]...
   ```

8. **Current Situation or Gap** - Present specific, researched facts about what exists now and what is lacking

   ```markdown
   **WHEREAS,** [current structure/situation], however, [identifies the gap or deficiency]...
   ```

9. **Substantive Facts** - Provide multiple specific facts, dates, events, statistics, or examples that demonstrate the need

   ```markdown
   **WHEREAS,** on [date], [specific event/fact occurred]; additionally, [related facts]; furthermore, [supporting evidence]...
   ```

10. **Impact or Significance** - Explain how this gap/situation affects Bangsamoro, Parliament operations, or specific constituencies

    ```markdown
    **WHEREAS,** [gap/situation] negatively affects [who/what], resulting in [specific impacts]...
    ```

11. **Best Practices** - Reference successful approaches from other jurisdictions, past successes, or comparative examples

    ```markdown
    **WHEREAS,** other legislatures and jurisdictions have [example], which has resulted in [outcomes]...
    ```

12. **Benefits and Advantages** - Describe concrete benefits if the action is taken

    ```markdown
    **WHEREAS,** establishing [action] would enable [specific benefits], strengthen [area], and improve [outcomes]...
    ```

13. **Potential Impact** - Articulate the expected positive impact on governance, Parliament operations, constituencies, or Bangsamoro autonomy

    ```markdown
    **WHEREAS,** [action] would contribute to [broader goals] and position Bangsamoro to [future advantages]...
    ```

14. **Appropriateness Clause** - Conclude with "fitting and proper" statement

   ```markdown
   **WHEREAS,** it is fitting and proper that the Bangsamoro Parliament [take this action]...
   ```

**Key points:**

- Each WHEREAS clause ends with semicolon (;)
- Start each with "**WHEREAS,**" (bold, with comma)
- Use formal, legislative language
- **MANDATORY Legal Hierarchy:** Always follow Philippine legal hierarchy:
  1. Philippine Constitution (MANDATORY)
  2. Bangsamoro Organic Law (MANDATORY)
  3. Related BOL provisions (when applicable)
  4. National Laws (when applicable and relevant)
  5. Related Jurisprudence (when applicable and supports the resolution)
  6. Bangsamoro Autonomy Acts (when applicable and relevant)
- **Base every claim on research findings**—cite specific facts, dates, numbers, examples
- Include multiple supporting facts per clause (e.g., "Additionally...", "Furthermore...")
- Build logical flow: Constitutional Authority → BOL Authority → National Laws → Jurisprudence → Autonomy Acts → Institutional Context → Current Situation → Gap → Facts/Examples → Impact → Best Practices → Benefits/Potential Impact → Appropriateness
- Include substantive detail to minimize MP questions and support swift approval
- If no relevant constitutional or BOL provision exists for the resolution topic, note this explicitly after the footnotes as a limitation
- If no National Laws, Autonomy Acts, or jurisprudence apply, simply omit those steps
- Remove only truly tangential details (facts that don't support the core case)

### Step 4: Draft RESOLVED Clauses

**Principle:** The RESOLVED clause gives the responsible agency a mandate. Do not include implementation details, timelines, or procedural requirements—let the agency decide how to implement, consistent with their legal authority and mandate.

**BTA Parliament Drafting Practice:** BTA resolutions follow a simple, direct style. The main RESOLVED often restates the resolution's title or core action. Avoid numbered sub-points or elaborate nested structures.

**Structure for RESOLVED clauses:**

**Main RESOLVED (always present):**

```markdown
**NOW, THEREFORE, BE IT RESOLVED,** as it is hereby resolved by the Bangsamoro Parliament, [restate or briefly summarize the title/main directive];
```

**Example (simple style):**

```markdown
**NOW, THEREFORE, BE IT RESOLVED,** as it is hereby resolved by the Bangsamoro Parliament, to urge the BTA Parliament Speaker to establish a Shari'ah Division under the Policy Research and Legal Services;
```

**RESOLVED FURTHER (ONLY IF NEEDED - conditional, not automatic):**

Include a "RESOLVED FURTHER" clause ONLY if there is a substantive additional directive that:

- Adds necessary administrative detail (e.g., designating a specific office to receive copies)
- Specifies a distinct, separate action beyond the main RESOLVED (e.g., directing a committee to investigate AND report findings)
- Establishes a complementary action that requires explicit statement (e.g., main RESOLVED approves budget; RESOLVED FURTHER establishes oversight mechanism)

Do NOT include "RESOLVED FURTHER" merely to add minor supporting details. If it doesn't materially change the resolution's effect or add a distinct new directive, omit it.

**Example (with RESOLVED FURTHER only when necessary):**

```markdown
**NOW, THEREFORE, BE IT RESOLVED,** as it is hereby resolved by the Bangsamoro Parliament, to direct the Commission on Audit to conduct a comprehensive review of all expenditures for the fiscal year 2024;

**RESOLVED FURTHER,** that the Commission shall submit its audit report to Parliament within one hundred twenty (120) days from approval of this Resolution.
```

(Note: The RESOLVED FURTHER here adds a distinct timeline directive that materially affects implementation. Without it, the main RESOLVED alone would be insufficient.)

**Final administrative clause (always include):**

```markdown
**RESOLVED FINALLY,** that copies of this Resolution be furnished to [list relevant offices/officials];
```

**Guidelines:**

- **Keep main RESOLVED simple and direct** - Restate the resolution's core purpose; avoid complex structures
- **No implementation details in RESOLVED clauses** - Timelines, procedures, responsible officers, budget amounts, and scope decisions belong with the responsible agency, not the resolution
- **Use RESOLVED FURTHER sparingly** - Only include if it adds a materially distinct directive
- **Urging resolutions:** Main RESOLVED only + RESOLVED FINALLY (no RESOLVED FURTHER unless there's a distinct secondary directive)
- **Directed/approved resolutions:** Main RESOLVED may be followed by RESOLVED FURTHER if needed for distinct administrative requirements
- **Always include RESOLVED FINALLY** - Standard administrative clause for document distribution
- For all resolution types: the RESOLVED states the action; the agency implements
- Let the agency's legal authority and judgment guide implementation details

### Step 5: Determine Recipients

List entities that should receive copies (for RESOLVED FINALLY):

**Always include (if relevant):**

- Office of the Chief Minister
- Relevant Ministry/Office
- Commission on Audit (for budget matters)

**Consider including:**

- National government agencies (for matters involving national coordination)
- Local government units affected
- Honorees (for commendatory resolutions)
- Investigating committees
- Subject matter stakeholders

### Step 6: Adding Citations and Footnotes

**Principle:** Every factual claim, statutory reference, organizational detail, or external reference must include a citation. This allows MPs to verify information and strengthens the resolution's credibility.

**Citation approach - Philippine Legal Standards:**

**IN WHEREAS CLAUSES:**

Follow the **STANDARD CITATION FORMAT** (provision identifier first, then law):

- **Constitutional references (first mention):**
  - Format: `Section [Y], Article [X], of the 1987 Philippine Constitution`
  - Example: `Section 15, Article X, of the 1987 Philippine Constitution provides: "[exact quote]"`

- **Republic Acts/National Laws (first mention):**
  - Format: `Section [Y], Article [X], of Republic Act No. [XXXX], otherwise known as the [Official Name] ([ABBREVIATION])`
  - Example: `Section 3, Article VII, of Republic Act No. 11054, otherwise known as the Bangsamoro Organic Law (BOL), provides: "[exact quote]"`

- **Republic Acts/National Laws (subsequent mentions):**
  - Format: `Section [Y], Article [X], of the [ABBREVIATION]`
  - Example: `Section 5(a), Article VII, of the BOL further provides that...`

- **Bangsamoro Autonomy Acts (first mention):**
  - Format: `Bangsamoro Autonomy Act No. [XX], otherwise known as the [Official Name] ([ABBREVIATION])`
  - Example: `Bangsamoro Autonomy Act No. 13, otherwise known as the Bangsamoro Administrative Code (BAC), provides that...`

- **Bangsamoro Autonomy Acts (subsequent mentions):**
  - Format: Use established abbreviation
  - Example: `Section 5 of the BAC further provides that...`

- **Jurisprudence/Court Cases (WITH G.R. NUMBERS - REQUIRED):** Format: `[Case Name], G.R. No. [number(s)], [Court], [Year], held that [exact principle]`
  - Example: `Province of Sulu v. Executive Secretary, G.R. Nos. 242255, 243246, 243693, Supreme Court of the Philippines (September 3, 2024), held that the Bangsamoro Organic Law is constitutional and autonomous regions possess legislative authority within their competencies`
  - **REQUIREMENT:** Always include complete G.R. numbers, court name, and decision date. Never cite jurisprudence without these details.

- **Organizational/Institutional facts:** Cite source document with date
  - Example: `Bangsamoro Parliament Resolution No. 96 (December 2020) established the Policy Research and Legal Services`

- **Statistics and dates:** Cite the source document or news reference
  - Example: `As of August 2024, the national government expanded the Shari'ah court system...`

- **Comparative examples:** Cite the source jurisdiction and structure
  - Example: `The Saudi Consultative Assembly (Shura Council) includes specialized committees...`

**IN FOOTNOTES (COMPLETE CITATIONS):**

- **Constitution:** `1987 Philippine Constitution, Article X, Section 15. Official Gazette of the Philippines.`

- **Republic Act:** `Republic Act No. 11054 (Bangsamoro Organic Law), Article VII, Section 3. Available at: https://lawphil.net/statutes/repacts/ra2018/ra_11054_2018.html`

- **Bangsamoro Autonomy Act:** `Bangsamoro Autonomy Act No. 13 (Bangsamoro Administrative Code). Available at: [official gazette link]`

- **Court Decision (WITH COMPLETE G.R. NUMBERS - REQUIRED):** `[Case Name], G.R. No(s). [all numbers, comma-separated], [Court Name], ([Date of Decision]), [reporter citation if available]`
  - Example: `Province of Sulu v. Executive Secretary, G.R. Nos. 242255, 243246, 243693, Supreme Court of the Philippines (September 3, 2024).`
  - **REQUIREMENT:** Always include ALL G.R. numbers (if consolidated cases), court name, and decision date. Never omit any of these details.

- **Official Documents:** `[Document Title] ([Date/Year]). Retrieved from: [official source/website]`

- **News/Current Events:** `"[Article Title]," [Publication], [Date]. [URL if available]`

**Footnote placement (IMPORTANT):**

- Place superscript numbers¹, ², ³, etc. after the claim or at the end of the relevant phrase in WHEREAS clauses
- **Group ALL footnotes at the END of the resolution, AFTER all RESOLVED clauses** (this is standard parliamentary format)
- Use consistent sequential numbering throughout (¹, ², ³, ... ¹³, etc.)
- Do NOT insert footnotes between WHEREAS and RESOLVED clauses
- Proper structure: WHEREAS clauses → RESOLVED clauses → FOOTNOTES section

**Example with citations:**

```markdown
**WHEREAS,** the Bangsamoro Organic Law (Republic Act No. 11054), Article VII, Section 3, vests in the Bangsamoro Parliament broad legislative authority;¹

**WHEREAS,** the Policy Research and Legal Services (PRLS), established by the Parliament through Resolution No. 96 (December 2020),² is mandated to provide "efficient legal assistance across legislative measures..."³

---

FOOTNOTES:

¹ Republic Act No. 11054 (Bangsamoro Organic Law), Article VII, Section 3. Available at: [https://lawphil.net/statutes/repacts/ra2018/ra_11054_2018.html](https://lawphil.net/statutes/repacts/ra2018/ra_11054_2018.html)

² Bangsamoro Parliament Resolution No. 96 (December 2020). Policy Research and Legal Services Official Mandate Document.

³ Policy Research and Legal Services Official Website - Mandate and Services. Retrieved from: [https://prls-parliament.bangsamoro.gov.ph/about-us/our-mandate/](https://prls-parliament.bangsamoro.gov.ph/about-us/our-mandate/)
```

**Guidelines for footnote format:**

- Include complete reference information (title, date, source/URL)
- For BOL citations: include the statute number, article, section
- For official documents: include the document title, date, and source
- For websites: include the URL
- For news articles: include publication, date, and URL
- For reports: include author/institution, date, and availability

### Step 7: Validation Phase

Before finalizing, validate the resolution draft:

### Validation Question 1: Is the operative clause (NOW, THEREFORE...) simple and does it reflect the resolution title's intent?

- The main RESOLVED should directly restate the title/purpose
- For urging resolutions: use "urge," "commend," "recognize"—not directive language
- For budget/directed resolutions: use "direct," "approve," "authorize"
- **Test:** Can someone read just the title + main RESOLVED and understand the resolution's purpose?

### Validation Question 2: Are all WHEREAS clauses substantive and value-adding? Or are there tangential riders?

- Each WHEREAS must provide legal authority, factual basis, or justification for swift approval
- Remove flowery language or facts that don't directly support the action
- Keep only legally/factually necessary background
- Ensure each clause is exhaustive enough to justify the action, but not excessive
- **Test:** Does each WHEREAS build toward justifying the RESOLVED? Would removing it weaken the justification?

### Validation Question 3: Are all RESOLVED clauses free of implementation details?

- Remove any timelines, procedural details, specific officer assignments, or budget amounts
- The RESOLVED states the action; the responsible agency decides implementation
- Only keep administrative clauses (e.g., "copies be furnished to...")
- If a RESOLVED FURTHER clause prescribes how something must be done, delete it
- **Test:** Does the RESOLVED tell the agency what to do, not how to do it?

### Validation Question 4: Is every fact in the resolution 100% accurate? Conduct spot-checks on key claims

- Verify dates, names, titles, organizational structure
- Verify any statistics or quotes
- Verify BOL citations and legal references
- **Test:** If challenged, can this be defended with source documentation?

### Validation Question 5: Is the language appropriate for the resolution type?

- Urging resolutions: softer language, requesting/encouraging action
- Commendatory: celebratory, achievement-focused
- Policy/statement: reasoned, balanced, evidence-based
- Budget: precise amounts, clear fiscal purpose (amounts belong in WHEREAS justification, not RESOLVED directives)

### Validation Question 6: Are Constitutional and BOL provisions present as mandatory foundation?

- **Check for Philippine Constitution citation (MANDATORY):** Is there at least one WHEREAS clause citing the 1987 Philippine Constitution?
- **Check for BOL provisions (MANDATORY):** Are there at least one or two WHEREAS clauses citing specific Bangsamoro Organic Law articles/sections that authorize the action?
- **Verify provision accuracy:** Check article/section numbers against actual statute text (lawphil.net)
- **Test logical flow:** Do Constitutional/BOL provisions form the foundation? Do all other WHEREAS clauses build from this legal authority?

### Validation Question 6A: Are National Laws, Autonomy Acts, and Jurisprudence included when applicable?

- **Check for National Laws:** If the resolution involves national-regional coordination or is affected by national legislation, are relevant national laws cited? (CONDITIONAL - required only when applicable)
- **Check for Jurisprudence:** If there are relevant Supreme Court rulings, appellate decisions, or legal precedents that support the resolution's legal basis, are they cited? (CONDITIONAL - required only when applicable)
- **Check for Bangsamoro Autonomy Acts:** If prior Autonomy Acts exist on the topic, are they cited to show legislative progression? (CONDITIONAL - required only when applicable)
- **Verify citation accuracy:** Check statute numbers, court case names, and ruling summaries against original sources
- **If no National Laws/Jurisprudence/Autonomy Acts exist on topic:** That is acceptable; simply skip to next validation question
- **Test legal hierarchy:** Is the logical flow Constitutional → BOL → National Laws → Jurisprudence → Autonomy Acts → Supporting details?

### Validation Question 7: Are all footnotes correct, complete, and verifiable?

- Every factual claim, statutory citation, organizational reference, and external reference must have a corresponding footnote
- **Verify BOL citations:** Check article, section, and provision numbers against the actual statute ([https://lawphil.net/statutes/repacts/ra2018/ra_11054_2018.html](https://lawphil.net/statutes/repacts/ra2018/ra_11054_2018.html))
- **Verify constitutional citations:** Check against the 1987 Philippine Constitution text
- **Verify organizational facts:** Confirm dates, titles, and structural details through official websites or documents
- **Verify statistics and dates:** Cross-check news dates, event timelines, and numbers with original sources
- **Verify comparative examples:** Ensure foreign legislature/jurisdiction examples are accurate
- **Check footnote completeness:** Each footnote must include full title, date (if applicable), and source/URL
- **Test accessibility:** Verify that URLs work and point to the correct source material
- **Test verifiability:** Ask: "Could an MP or staffperson easily verify this claim using the provided citation?"
- **Test accuracy of quotes:** If quoting directly, ensure the quote is verbatim and in context
- **Test citations for ambiguity:** Avoid vague references like "Official Records" without specific document/date

## Templates

Use appropriate template based on resolution category:

- **Simple resolutions:** [assets/template-simple.md](assets/template-simple.md)
- **Commendatory resolutions:** [assets/template-commendatory.md](assets/template-commendatory.md)
- **Policy/statement resolutions:** [assets/template-policy.md](assets/template-policy.md)
- **Budget/financial resolutions:** [assets/template-budget.md](assets/template-budget.md)

Templates provide structure - customize all bracketed placeholders with researched content.

## Format Requirements

**See [references/format-guide.md](references/format-guide.md)** for complete formatting rules including capitalization, punctuation, and citation standards.

## Examples

Review complete examples for reference: [references/examples.md](references/examples.md)

Examples cover all four resolution categories with realistic content demonstrating:

- Proper WHEREAS clause progression
- Appropriate citation of legal authorities
- Specific, actionable RESOLVED clauses
- Correct formatting and structure

## Quality Checklist

Before finalizing:

- [ ] Researched topic thoroughly with specific facts/dates
- [ ] Selected correct resolution type and category (per AR 268)
- [ ] WHEREAS clauses build logical progression
- [ ] Cited relevant BOL provisions (if applicable)
- [ ] RESOLVED clauses are specific and actionable
- [ ] Included timelines/deadlines where appropriate
- [ ] Listed appropriate recipients for copies
- [ ] Verified formatting (ALL CAPS title, semicolons, etc.)
- [ ] Used formal, legislative language throughout

## Output Configuration

**DUAL OUTPUT: Save both Markdown and Word versions**

### Step A: Save Markdown Version

**Save all completed resolutions to:**

```bash
/Users/saidamenmambayao/apps/Parliamentarian/Proposed-Resolutions/
```

**File naming convention:**

Use descriptive filenames that clearly identify the resolution content:

- Format: `[Category]-[Brief-Description].md`
- Examples:
  - `Commendatory-Frontline-Health-Workers.md`
  - `Policy-BOL-Block-Grant-Inquiry.md`
  - `Budget-FY2025-Supplemental-Appropriation.md`
  - `Internal-Special-Committee-Indigenous-Peoples.md`

**File format:**

- Save as Markdown (.md) files
- Include all resolution content from header to final RESOLVED clause
- Preserve exact formatting (spacing, capitalization, punctuation)

### Step B: Convert to Word (.docx) Format

**After saving the Markdown file, automatically convert it to Word format using the conversion script:**

```bash
python3 scripts/convert_to_docx.py [path-to-markdown-file.md]
```

**Example:**
```bash
python3 /Users/saidamenmambayao/apps/Parliamentarian/.gemini/skills/resolution-writer/scripts/convert_to_docx.py /Users/saidamenmambayao/apps/Parliamentarian/Proposed-Resolutions/Policy-BOL-Block-Grant-Inquiry.md
```

This will create:
- `Policy-BOL-Block-Grant-Inquiry.docx` (Word document in same directory)

**Word document formatting:**
- Font: Bookman Old Style, 12pt
- Single spacing
- Standard margins (1 inch)
- Page numbers in footer
- WHEREAS clauses: Indented (0.5 inch)
- RESOLVED clauses: Indented (0.5 inch)
- ALL CAPS titles: Centered and preserved
- Bold text: Preserved
- Superscript footnote citations: Maintained (¹, ², ³, ...)

**Benefits of dual output:**
- Markdown (.md): Version control, easy editing, text-based collaboration
- Word (.docx): Official distribution, printing, sharing with parliamentary staff who use MS Word
- Both formats maintain identical content and formatting

## Bangsamoro Context and Legal Citations

**For Bangsamoro-specific terminology, BOL citations, and cultural context:** See [references/context.md](references/context.md) for:

- Key Bangsamoro terminology and government structure
- Common BOL article/section citations by topic
- Frequent resolution recipients
- Research sources priority list
- Historical and cultural context
