# Chapter 11 — AI for Legislation and Codification

The Bangsamoro Transition Authority Parliament has enacted 89 Bangsamoro Autonomy Acts since February 2019.[^1] These 89 laws created ministries, established commissions, appropriated budgets, upgraded hospitals, founded municipalities, enacted priority codes, and defined the institutional architecture of the Bangsamoro Autonomous Region. They are the single most tangible product of the transition period.

But 89 separate enactments do not make a legal system. A legal system requires **codification** — the organization of enacted laws into a coherent, internally consistent, searchable body of legislation. It requires **harmonization** — the identification and resolution of conflicts between provisions enacted at different times, under different political conditions, by different BTA compositions. And it requires **maintenance** — the continuous updating of the legal corpus as new laws are enacted, old provisions are amended, and implementing rules fill in the operational detail.

The Bangsamoro Parliament has not yet completed this work. The transition period prioritized enactment speed — passing the laws BARMM needed to function. Codification, harmonization, and systematic maintenance received less institutional attention. This is not unusual for a new autonomous government. The challenge now is to build the systems that transform 89 discrete enactments into an organized, accessible, and internally consistent Bangsamoro legal corpus.

AI makes this work feasible at a scale and speed that manual methods cannot match. It does not replace the legal judgment required to resolve genuine policy conflicts between provisions. But it identifies those conflicts in minutes rather than months. It maps cross-references across dozens of laws simultaneously. It flags terminology inconsistencies that human reviewers miss after reading their fortieth BAA in a row. And it generates first drafts of implementing rules that legal staff can refine rather than build from scratch.

This chapter covers AI's role across the full post-enactment cycle: from organizing the existing legislative output through codification and harmonization, to drafting IRRs, to managing parliamentary operations, to closing the loop by feeding enacted legislation back into the planning process.

---

## 11.1 The Legislative Output of the BTA and What Comes Next

### What Parliament Has Enacted

The 89 BAAs fall into 13 domain categories.[^2] Understanding the distribution matters because codification must respect these domains while identifying the connections between them.

### Table 11.1: BAA Distribution by Domain

| Domain | Count | Key BAAs | Notes |
|--------|-------|----------|-------|
| **Budget & Appropriations** | 16 | BAA 3, 15, 23, 32, 65, 84, 85 | Annual GAAs, SDF extensions, supplemental budgets, Budget System Act |
| **Health** | 11 | BAA 21, 25-30, 73, 74, 76, 78-80 | Hospital upgrades and new facilities across all provinces |
| **Local Government** | 10 | BAA 41-48, 53-55, 70-71 | 11 new municipalities, mostly in Maguindanao and the SGA |
| **Electoral** | 5 | BAA 35, 58, 77, 86, 87-88 | Electoral Code, redistricting (77 struck down, 86 enacted), amendments |
| **Symbols & Identity** | 5 | BAA 1, 2, 7, 16, 20 | Flag, emblem, hymn, parliamentary seal, dual calendar |
| **Social Welfare & Human Rights** | 5 | BAA 4, 8, 10, 62, 64, 83, 89 | BHRC, BWC, BYC, IDP Protection, IP Rights, Nutrition Commission, Transitional Justice |
| **Governance & Administration** | 5 | BAA 5, 11, 13, 17, 37 | Attorney-General, appointments, Administrative Code, Civil Service Code, seat of government |
| **Education & Culture** | 4 | BAA 12, 18, 40, 50, 81 | BSC, Education Code, Science High School, Kulliyyah, Salamat Award |
| **Economy & Labor** | 4 | BAA 9, 19, 59, 72, 82 | Recruitment regulation, overseas workers, agriculture training, bereavement leave, Labor Code |
| **Environment & Development** | 2 | BAA 6, 31 | Development planning system, Sustainable Development Board |
| **Peace & Security** | 3 | BAA 57, 60, 61 | Mujahideen financial assistance, memorial sites |
| **Holidays** | 1 | BAA 39 | BARMM Holidays Code |
| **Miscellaneous** | 4 | BAA 56, 66-69 | Titles not on public record |

### The Six Fundamental Codes

BOL Article XVI, Section 4 mandates the BTA to enact **seven priority codes** during the transition period.[^3] As of March 2026, four have been enacted:

1. **Bangsamoro Administrative Code** (BAA 13, October 2020) — structures the bureaucracy
2. **Bangsamoro Civil Service Code** (BAA 17, February 2021) — merit and fitness system
3. **Bangsamoro Education Code** (BAA 18, May 2021) — integrated education system
4. **Bangsamoro Electoral Code** (BAA 35, 2023) — election rules, amended by BAA 87 and BAA 88

Three priority codes remain unenacted:

5. **Revenue Code** — own-source revenue generation framework
6. **Local Government Code** — though BAA 49 (Bangsamoro Local Governance Code) addresses this substantially
7. **Investment Code** — investment promotion and economic zone framework

Beyond the seven priority codes, Parliament has also enacted the **Bangsamoro Budget System Act** (BAA 84) and the **Bangsamoro Labor and Employment Code** (BAA 82), which function as fundamental codes in their respective domains.[^4]

### What Comes Next

The first parliamentary elections will transform the legislative agenda. Elected Members of Parliament will bring constituency priorities that differ from those of the appointed BTA. The legislative pipeline will shift from foundational institution-building toward **implementation refinement**, **amendment of existing codes**, and **responsive legislation** addressing emerging needs.

This means the codification challenge will intensify. Every new BAA must be integrated into the existing legal corpus. Every amendment must be tracked against the provision it modifies. Every new mandate must be checked for conflicts with existing mandates. Without AI, this work quickly exceeds the capacity of any parliamentary staff team.

---

## 11.2 AI for Codification and Legal Harmonization

### The Problem Codification Solves

Consider what happens when a legislative researcher in the Bangsamoro Parliament needs to answer a seemingly simple question: **What are all the provisions in enacted BAAs that grant powers to the Ministry of Health?**

Without codification, the researcher must read all 89 BAAs. The obvious starting point is BAA 13 (Administrative Code), which defines ministry mandates. But hospital upgrade BAAs (BAA 25-30, 73, 74, 76, 78-80) also grant implementation mandates to MOH. BAA 85 (GAA FY 2026) allocates specific health budgets with spending conditions. BAA 83 (Bangsamoro Nutrition Commission) creates an agency with overlapping health jurisdiction. The researcher might miss any of these cross-references.

**Codification organizes all enacted provisions by subject matter** so that related provisions from different BAAs appear together. **Harmonization identifies and resolves conflicts** between provisions that contradict each other or create ambiguity. AI handles both tasks at scale.

### Cross-Referencing Provisions Across BAAs

The first codification task is **mapping** — building a cross-reference index that connects every provision to every other provision it relates to. This is exactly the kind of pattern-matching work where AI outperforms human effort.

> **Sample Prompt — Cross-Reference Mapping:**
>
> ```
> You are a legal codification specialist for the Bangsamoro
> Parliament.
>
> I am uploading the full text of [NUMBER] enacted Bangsamoro
> Autonomy Acts. Build a cross-reference index as follows:
>
> For each BAA, identify every section that:
> 1. Explicitly amends or repeals a provision in another BAA
>    (cite both the amending and amended provisions)
> 2. Creates a mandate, power, or function that overlaps with
>    a mandate in another BAA (cite both provisions and describe
>    the overlap)
> 3. Defines a term that is also defined differently in another
>    BAA (cite both definitions and flag the inconsistency)
> 4. References another BAA by number or subject matter
>
> Output format: a table with columns:
> BAA (Source) | Section | BAA (Target) | Section | Relationship
> Type (amends, repeals, overlaps, defines differently, references)
>
> Sort by BAA number. Flag all definitional inconsistencies as
> [TERMINOLOGY CONFLICT].
> ```

### Identifying Conflicts

Not all overlaps are conflicts. BAA 82 (Labor Code) and BAA 13 (Administrative Code) both address employment conditions, but they operate in different domains — one covers the private sector, the other structures government. A **conflict** exists when two provisions impose contradictory requirements on the same actor in the same situation.

> **Sample Prompt — Conflict Detection:**
>
> ```
> From the cross-reference index, extract all entries marked
> as "overlaps" or "defines differently."
>
> For each entry, assess:
> 1. Do the two provisions impose contradictory obligations on
>    the same entity?
> 2. Could a person or office attempting to comply with both
>    provisions face an impossible or ambiguous situation?
> 3. Does one provision appear to supersede the other (enacted
>    later, more specific, or explicitly intended to prevail)?
>
> Classify each overlap as:
> - CONFLICT (contradictory obligations, no clear resolution)
> - AMBIGUITY (unclear which provision controls)
> - COMPLEMENTARY (overlapping but compatible)
> - SUPERSEDED (one clearly prevails over the other)
>
> For each CONFLICT or AMBIGUITY, recommend a resolution approach:
> amendment, IRR clarification, or parliamentary interpretation.
> ```

### Terminology Consistency

One of the most common sources of legal ambiguity is **inconsistent terminology**. The same concept may be called different names in different BAAs enacted years apart. A ministry renamed through reorganization may still carry its old name in earlier enactments. A technical term defined in one code may be used without definition in another.

> **Sample Prompt — Terminology Audit:**
>
> ```
> Conduct a terminology audit across all uploaded BAAs.
>
> 1. Extract every defined term from each BAA's "Definition of
>    Terms" section
> 2. Identify terms that appear in multiple BAAs — compare
>    definitions for consistency
> 3. Identify terms used in BAA provisions that are NOT defined
>    in that BAA but ARE defined in another BAA
> 4. Identify instances where different BAAs use different terms
>    for what appears to be the same concept (e.g., "barangay
>    health station" vs. "barangay health center" vs. "community
>    health facility")
> 5. Flag all inconsistencies as [DEFINE], [RECONCILE], or
>    [STANDARDIZE]
>
> Output: a terminology concordance table sorted alphabetically,
> with each term showing all BAAs where it appears and how it
> is defined or used.
> ```

### Building the Bangsamoro Legal Corpus Database

The long-term codification goal is a **searchable legal corpus** — a structured database where every provision is tagged by subject, ministry, date of enactment, amendment history, and related provisions. AI can generate the initial structure.

**Practical steps for building the corpus:**

1. **Digitize all enacted BAAs** in a consistent format (markdown or structured text)
2. **Tag every provision** with metadata: BAA number, section number, subject category, responsible ministry, effective date
3. **Map all amendments** — when BAA 37 amends BAA 13, Section 9, link them bidirectionally
4. **Generate subject-matter clusters** — all provisions related to health, all provisions related to procurement, all provisions related to local government
5. **Build a change log** — when a new BAA amends or repeals an existing provision, the corpus updates automatically

This connects directly to **Chapter 4 (Data, Documents, and Knowledge Management)**, where building BARMM-specific AI knowledge bases is covered in detail.

---

## 11.3 AI for IRR Development

### Why IRRs Matter

An enacted BAA sets the legal framework. The **Implementing Rules and Regulations (IRR)** translate that framework into operational detail. The BAA says what must be done. The IRR specifies how, by whom, within what timeline, using what forms, following what procedures.

Without an IRR, an enacted BAA often remains partially or fully unimplemented. This is not a theoretical problem in BARMM. Chapter 10 documented the compliance tracking challenge: some priority codes have been enacted for years without complete IRRs.[^5] The delay is not always about political will. Drafting an IRR requires deep legal analysis, operational expertise, and interagency coordination — resources that implementing agencies may lack.

AI does not replace the implementing agency's operational knowledge. But it generates the **structural framework** of an IRR from the enacted BAA text, which the agency then fills in with operational specifics.

### Extracting IRR Requirements from Enacted BAAs

Before drafting an IRR, you need to know exactly what the BAA requires.

> **Sample Prompt — IRR Requirement Extraction:**
>
> ```
> You are a legal analyst supporting IRR development for the
> Bangsamoro Government.
>
> I am uploading [BAA NUMBER AND TITLE]. Extract every provision
> that requires implementing rules, regulations, guidelines, or
> operational procedures.
>
> For each provision:
> 1. Section number and title
> 2. The specific obligation ("shall issue implementing rules,"
>    "as may be prescribed by rules," "in accordance with
>    guidelines to be promulgated," etc.)
> 3. The implementing body (which ministry, office, or commission
>    is responsible)
> 4. The deadline (if specified in the BAA)
> 5. The scope — what operational detail the IRR must supply
>
> Also identify provisions that do NOT explicitly require an IRR
> but that are too general to implement without additional
> operational guidance. Flag these as [RECOMMENDED IRR PROVISION].
>
> Output: a table sorted by section number.
> ```

### Drafting IRR Frameworks

Once requirements are extracted, AI can generate an IRR framework — the structural skeleton that the implementing agency completes.

> **Sample Prompt — IRR Framework Draft:**
>
> ```
> Draft an IRR framework for [BAA NUMBER AND TITLE].
>
> Structure the IRR as follows:
> RULE I — Title and Authority
> RULE II — Definition of Terms (carry over definitions from
>   the BAA; add operational definitions needed for implementation)
> RULE III — Coverage and Applicability
> RULE IV onward — One rule per major substantive provision of
>   the BAA that requires operational detail
> FINAL RULE — Effectivity and Repealing Clause
>
> For each rule:
> 1. Cite the specific BAA section being implemented
> 2. State the implementing agency's obligation
> 3. Identify the operational details the IRR must specify
>    (forms, timelines, procedures, responsible offices)
> 4. Leave placeholders marked [AGENCY TO SUPPLY] where
>    operational specifics depend on the agency's internal
>    structure and resources
>
> Include a compliance timeline: which rules take effect
> immediately upon promulgation and which have phased
> implementation dates.
>
> [Upload the full BAA text]
> ```

### The IRR Quality Checklist

Use AI to verify that a draft IRR meets quality standards before promulgation.

**Table 11.2: IRR Quality Verification Checklist**

| Check | What AI Verifies | What Humans Verify |
|-------|-----------------|-------------------|
| **Completeness** | Every BAA provision requiring an IRR has a corresponding rule | Whether the operational detail is sufficient for field implementation |
| **Legal fidelity** | IRR rules do not exceed, contradict, or narrow the authority granted by the BAA | Whether the interpretation of BAA provisions reflects legislative intent |
| **Definitional consistency** | Terms defined in the IRR match the BAA's definitions; no undefined terms | Whether operational definitions align with agency practice |
| **Timeline feasibility** | Compliance deadlines are internally consistent | Whether the agency can realistically meet the deadlines |
| **Interagency clarity** | Where multiple agencies share implementation responsibility, roles are clearly delineated | Whether the agencies have agreed to the delineation |
| **BOL alignment** | IRR provisions fall within the Bangsamoro Government's powers under BOL Article V, Section 2 | Whether the IRR triggers intergovernmental coordination requirements under BOL Article VI |

---

> **Case Study: Drafting the IRR Framework for BAA 84 (Bangsamoro Budget System Act)**
>
> BAA 84 establishes the Bangsamoro budget system framework, covering the entire budget cycle from preparation through accountability.[^6] The Budget System Act is one of the most operationally complex BAAs in the Bangsamoro corpus because it touches every ministry, every office, and every local government unit within BARMM.
>
> An AI-assisted IRR workflow for BAA 84 would proceed as follows:
>
> **Step 1 — Extract.** Upload the full text of BAA 84. Prompt the AI to extract every provision requiring implementing rules. The extraction should identify provisions on budget preparation calendars, submission formats, allotment release procedures, obligation authority limits, accountability reporting requirements, and the roles of the Ministry of Finance, Budget, and Management (MFBM) in each stage.
>
> **Step 2 — Map dependencies.** BAA 84 does not operate in isolation. It interacts with annual GAAs (BAA 85 for FY 2026), the Administrative Code (BAA 13), and the Civil Service Code (BAA 17) for personnel budgeting. Prompt the AI to identify all cross-references between BAA 84 and other enacted BAAs. Where BAA 84 creates obligations that depend on provisions in other BAAs, the IRR must address the coordination mechanism.
>
> **Step 3 — Draft.** Generate the IRR framework with one rule per major budget cycle stage. Leave operational placeholders for MFBM to supply: specific forms, submission deadlines for the next fiscal year, allotment release schedules, and accountability report templates.
>
> **Step 4 — Verify.** Run the draft IRR through the quality checklist (Table 11.2). Confirm that every BAA 84 provision has a corresponding rule. Check that definitions match. Verify that the IRR does not create obligations beyond what BAA 84 authorizes.
>
> **What the AI cannot do:** Determine whether MFBM has the staff capacity to implement a quarterly budget review cycle or whether a monthly allotment release schedule is operationally feasible. Those judgments require the implementing agency's institutional knowledge.

---

## 11.4 AI for Resolution Drafting and Parliamentary Operations

### Resolutions vs. Bills

The Bangsamoro Parliament produces two main types of legislative measures: **bills** (which become BAAs when enacted) and **resolutions** (which express the sense of Parliament without the force of law, or which address internal parliamentary matters).[^7] Chapter 7 covered AI for bill drafting. This section addresses the distinct requirements of resolution drafting and the parliamentary operations that surround it.

Resolutions serve several purposes in the Bangsamoro Parliament:

- **Congratulatory resolutions** — recognizing achievements of individuals, organizations, or communities
- **Commendatory resolutions** — commending specific actions or milestones
- **Commemorative resolutions** — marking historical events, holidays, or occasions
- **Policy resolutions** — expressing Parliament's position on a policy issue without enacting binding law
- **Oversight resolutions** — directing committees to investigate or report on specific matters
- **Internal resolutions** — governing parliamentary procedures, committee creation, or rules amendments

### The WHEREAS-RESOLVED Structure

Every resolution follows a standard two-part structure: **preamble clauses** (WHEREAS) that establish the factual and legal basis, followed by **operative clauses** (RESOLVED) that state what Parliament is actually doing.[^8]

AI can generate both components from a brief description of the resolution's purpose.

> **Sample Prompt — Resolution Draft:**
>
> ```
> You are a legislative drafter for the Bangsamoro Parliament.
>
> Draft a [TYPE] resolution for the following purpose:
> [DESCRIBE THE PURPOSE IN 2-3 SENTENCES]
>
> Structure:
> 1. TITLE: "A Resolution [verb]-ing [subject]"
> 2. WHEREAS CLAUSES (preamble):
>    - Clause 1: Legal basis (cite the BOL provision, BAA, or
>      Constitutional provision that gives Parliament authority)
>    - Clause 2: Factual background (what happened or what
>      condition exists)
>    - Clause 3-5: Supporting facts, prior legislative action,
>      or policy context
>    - Each WHEREAS clause should be one sentence
>    - Begin with "WHEREAS," followed by the statement, ending
>      with a semicolon
> 3. RESOLVED CLAUSES (operative):
>    - "NOW, THEREFORE, BE IT RESOLVED, as it is hereby resolved,"
>      followed by the operative provision
>    - If multiple operative clauses: "RESOLVED, FURTHER,"
>    - Final clause: effectivity
>
> Use formal legislative language. Cite specific BAA sections
> and BOL articles where applicable.
>
> [Provide any supporting documents or factual details]
> ```

### Strengthening WHEREAS Clauses

Weak preamble clauses undermine even well-intentioned resolutions. A WHEREAS clause that says "WHEREAS, the Bangsamoro Parliament recognizes the importance of education" adds nothing. A strong WHEREAS clause cites a specific provision, references specific data, or states a specific fact.

> **Sample Prompt — WHEREAS Clause Strengthening:**
>
> ```
> Review the following draft resolution for the Bangsamoro
> Parliament. Strengthen each WHEREAS clause by:
>
> 1. Adding specific legal citations (BOL article and section,
>    BAA number and section, or national law)
> 2. Replacing general statements with specific facts, data
>    points, or documented events
> 3. Ensuring each WHEREAS clause builds logically on the
>    previous one (legal basis → factual background →
>    specific circumstances → justification for action)
> 4. Removing redundant clauses that repeat the same point
>    in different words
>
> For any factual claim you cannot verify from the uploaded
> documents, mark it as [VERIFY: source needed].
>
> [Paste the draft resolution]
> ```

### Parliamentary Operations Support

Beyond individual resolutions, AI assists with the operational machinery of Parliament:

**Table 11.3: Parliamentary Operations with AI Support**

| Operation | Manual Process | AI-Assisted Process |
|-----------|---------------|-------------------|
| **Order of Business preparation** | Secretary manually compiles agenda items from committee reports and pending measures | AI generates draft order of business from committee status reports, pending bills, and calendar deadlines |
| **Committee referral** | Speaker's office determines appropriate committee(s) based on subject matter | AI recommends primary and secondary committee referrals by matching bill subject against committee jurisdictions |
| **Co-authorship tracking** | Staff manually tracks which MPs have signed onto each measure | AI maintains a co-authorship database and generates reports on sponsorship patterns |
| **Session minutes synthesis** | Staff transcribes and summarizes plenary proceedings | AI converts session recordings or transcripts into structured minutes with speaker attribution |
| **Legislative calendar management** | Manual tracking of filing deadlines, committee report deadlines, and plenary scheduling | AI generates timeline alerts and identifies scheduling conflicts |

---

## 11.5 AI for Legislative Tracking and Status Reporting

### The Tracking Challenge

At any given time, the Bangsamoro Parliament has dozens of measures at different stages: bills filed but not yet referred, bills in committee, bills reported out for plenary debate, bills pending interpellation, resolutions awaiting adoption. Staff, committee chairs, and Members of Parliament all need to know the status of specific measures — and no one has time to compile the answer manually from scattered records.

AI builds and maintains the **legislative tracking system** that makes status reporting instantaneous.

### Building the Legislative Status Database

The foundation is a structured database that captures every measure and its current status.

> **Sample Prompt — Legislative Status Database Design:**
>
> ```
> Design a legislative tracking database structure for the
> Bangsamoro Parliament.
>
> Fields for each measure:
> 1. Measure type (bill or resolution)
> 2. Measure number (e.g., PB-424, PR-47)
> 3. Short title
> 4. Principal author(s)
> 5. Co-author(s)
> 6. Date filed
> 7. Committee referral (primary and secondary committees)
> 8. Date referred to committee
> 9. Committee action (hearing scheduled, hearing completed,
>    committee report filed, substitute bill proposed)
> 10. Date of committee report
> 11. Plenary status (first reading, second reading,
>     interpellation, period of amendments, third reading,
>     enrolled)
> 12. Date of plenary action
> 13. For bills: BAA number assigned upon enactment
> 14. Related measures (companion bills, substitute bills,
>     amendments to existing BAAs)
>
> Include status categories:
> FILED → REFERRED → IN COMMITTEE → REPORTED OUT → PLENARY
> (1ST READING → 2ND READING → 3RD READING) → ENROLLED → ENACTED
>
> Generate sample entries using the following real measures:
> - PB-424 (latest filed bill)
> - BAA 86 (Parliamentary District Act, enacted January 2026)
> - BAA 84 (Budget System Act)
> ```

### Generating Status Reports

Once the database exists, AI generates status reports on demand.

> **Sample Prompt — Legislative Pipeline Report:**
>
> ```
> From the legislative tracking database, generate a status
> report covering:
>
> 1. PIPELINE SUMMARY: Total measures filed, in committee,
>    reported out, enacted — broken down by type (bill vs.
>    resolution)
> 2. COMMITTEE WORKLOAD: For each standing committee, list
>    the number of measures pending, measures acted on this
>    quarter, and average days from referral to committee report
> 3. AGING REPORT: List all measures that have been in committee
>    for more than [N] days without action
> 4. ENACTMENT RATE: Percentage of filed bills that reached
>    enactment, by session period
> 5. PRIORITY LEGISLATION STATUS: Status of any measures
>    identified as priority by the Chief Minister or the Speaker
>
> Format: executive summary (1 paragraph) followed by detailed
> tables. Flag all measures older than 180 days in committee
> as [REVIEW NEEDED].
> ```

### Committee Referral Recommendations

When a new bill is filed, it must be referred to the appropriate committee. Some bills clearly belong to a single committee. Others involve multiple policy domains and require referral to a primary committee with secondary referral to other committees.

> **Sample Prompt — Committee Referral Analysis:**
>
> ```
> A new bill has been filed in the Bangsamoro Parliament:
>
> Title: [BILL TITLE]
> Subject: [BRIEF DESCRIPTION]
>
> Based on the following committee jurisdictions of the
> Bangsamoro Parliament, recommend:
> 1. PRIMARY COMMITTEE: The committee with principal
>    jurisdiction over the bill's primary subject matter
> 2. SECONDARY COMMITTEE(S): Any committees with overlapping
>    jurisdiction that should review specific provisions
> 3. JUSTIFICATION: For each recommendation, cite the specific
>    provisions of the bill that fall within that committee's
>    jurisdiction
>
> If the bill involves budgetary implications, always include
> the Committee on Appropriations as a secondary referral.
>
> [Paste the bill title, explanatory note, or full text]
> [Paste the committee jurisdiction list]
> ```

### Tracking Amendments to Existing BAAs

Some of the 89 BAAs have already been amended. BAA 3 was amended by BAA 14. BAA 13 was amended by BAA 37. BAA 23 was amended by BAA 33. BAA 32 was amended by BAA 52. BAA 35 was amended by BAA 87 and BAA 88. BAA 54 was amended by BAA 70. BAA 55 was amended by BAA 71. BAA 58 was superseded by BAA 86 after the Supreme Court struck down both BAA 58 and BAA 77.[^9]

Tracking these amendment chains manually is error-prone. AI maintains the amendment history.

> **Sample Prompt — Amendment Chain Tracker:**
>
> ```
> From the following list of 89 BAAs, identify every amendment
> relationship.
>
> For each amendment:
> 1. Amending BAA (number and title)
> 2. Amended BAA (number and title)
> 3. Specific section(s) amended
> 4. Nature of amendment (modifies text, extends deadline,
>    repeals provision, adds new provision)
> 5. Whether the amendment is the most recent change to that
>    section (or whether it has been further amended)
>
> Also identify:
> - BAAs that have been struck down by the Supreme Court
>   (cite the case)
> - BAAs that repeal provisions of predecessor laws (e.g., MMAA
>   provisions repealed by BAAs)
>
> Output: amendment chain table sorted by original BAA number,
> showing the full amendment history for each.
>
> [Paste or upload the BAA index with amendment notes]
> ```

---

## 11.6 Closing the Cycle: How Enacted Legislation Becomes Planning Input

### The Legislation-Planning Loop

The governance cycle in BARMM does not end with enactment. Every enacted BAA creates new conditions that the planning process must account for. The **Bangsamoro Development Plan 2023-2028** identifies six overarching goals and eight cross-cutting strategies.[^10] Each enacted BAA either advances those goals or creates new implementation requirements that the next planning cycle must address.

This feedback loop is the most neglected stage in most governments. Laws are enacted, and the planning agencies continue working from their original assumptions as if nothing changed. AI can close this gap by systematically extracting the planning implications of every new enactment.

### From Enacted BAA to Planning Input

> **Sample Prompt — Legislative Impact on Planning:**
>
> ```
> You are a strategic planning analyst for the Bangsamoro
> Development Authority (BPDA).
>
> I am uploading [BAA NUMBER AND TITLE], recently enacted by
> the Bangsamoro Parliament. Analyze its implications for the
> Bangsamoro Development Plan 2023-2028.
>
> For each major provision:
> 1. Which BDP goal(s) does it advance? (cite the specific
>    goal and strategy)
> 2. Does it create new implementation obligations that require
>    planning resources (staffing, budget, infrastructure)?
> 3. Does it change the institutional landscape (new agencies,
>    new mandates, new coordination requirements)?
> 4. Does it require adjustments to existing plans or targets?
> 5. Does it create new monitoring indicators that should be
>    added to the BDP results framework?
>
> Output: a planning implications table with columns:
> BAA Provision | BDP Goal Affected | Planning Implication |
> Action Required | Responsible Agency
>
> Flag any provision that creates unfunded mandates as
> [BUDGET IMPLICATION - COORDINATE WITH MFBM].
> ```

### Mapping BAAs to BDP Goals

AI can build a comprehensive map connecting all 89 BAAs to their corresponding BDP goals. This map serves multiple purposes: it shows Parliament which development goals have strong legislative support and which have gaps. It shows the planning agencies which laws they must account for. And it provides the evidence base for the next planning cycle.

**Table 11.4: Sample BAA-to-BDP Goal Mapping**

| BDP Goal | BAAs That Advance This Goal | Coverage Assessment |
|----------|---------------------------|-------------------|
| **Goal 1: Just and lasting peace** | BAA 57 (Mujahideen Assistance), BAA 60-61 (Memorials), BAA 62 (IDP Protection), BAA 89 (Transitional Justice) | Moderate — peace financing and transitional justice addressed; community-level reconciliation programs need legislative framework |
| **Goal 2: Moral governance** | BAA 13 (Administrative Code), BAA 17 (Civil Service Code), BAA 84 (Budget System Act) | Strong foundational codes — IRR implementation is the gap |
| **Goal 3: Meaningful self-determination** | BAA 35, 86-88 (Electoral laws), BAA 49 (Local Governance Code), BAA 41-48, 53-55 (New municipalities) | Strong — electoral and local governance framework largely in place |
| **Goal 4: Economic development** | BAA 82 (Labor Code), BAA 9, 19, 59, 72 (Labor/employment measures) | Revenue Code and Investment Code still needed |
| **Goal 5: Quality social services** | BAA 18 (Education Code), BAA 25-30, 73-74, 76, 78-80 (Health), BAA 40 (Science HS), BAA 83 (Nutrition) | Health infrastructure strong; social protection framework needs expansion |
| **Goal 6: Cultural identity** | BAA 1, 2, 7, 16, 20 (Symbols), BAA 39 (Holidays), BAA 50 (Kulliyyah), BAA 64 (IP Rights) | Cultural symbols established; cultural industry development legislation needed |

### Feeding Oversight Findings Back into Legislation

Chapter 10 traced the **accountability chain** from AI-generated oversight analysis to formal parliamentary action.[^11] The final link in that chain connects back to this chapter: when oversight reveals a gap in existing legislation, the finding becomes the basis for a new bill or amendment.

**The complete governance cycle with AI support:**

1. **Plan** (Chapter 5) — BDP sets goals and strategies
2. **Budget** (Chapter 6) — GAA allocates resources to achieve goals
3. **Legislate** (Chapter 7) — Parliament enacts BAAs creating the legal framework
4. **Implement** (Chapter 8) — Ministries execute through IRRs and programs
5. **Monitor** (Chapter 9) — M&E tracks progress against targets
6. **Oversee** (Chapter 10) — Parliament holds the executive accountable
7. **Codify** (Chapter 11) — Enacted legislation is organized, harmonized, and fed back into planning

AI supports every stage. The output of each stage becomes the input for the next. The Bangsamoro legal corpus is not a static archive — it is a living system that grows, adapts, and informs the continuous cycle of governance.

### Cross-References to Other Chapters

| Topic | Where to Go |
|-------|------------|
| Building the BARMM legal knowledge base | Chapter 4, Section 4.3 |
| AI for strategic planning with BDP alignment | Chapter 5, Section 5.2 |
| Budget legislation and GAA analysis | Chapter 6, Sections 6.2-6.4 |
| AI for bill drafting (detailed process) | Chapter 7, Sections 7.2-7.5 |
| Oversight findings that trigger new legislation | Chapter 10, Section 10.6 |
| Ethics of AI in legal codification | Chapter 12, Section 12.3 |
| Prompt library for codification tasks | Appendix A, Section A.6 |

---

## Summary

The Bangsamoro Parliament's 89 BAAs are a legislative achievement. Transforming them into a coherent, searchable, internally consistent legal system is the next institutional challenge. Codification, harmonization, IRR development, parliamentary operations management, legislative tracking, and the legislation-planning feedback loop — these are the tasks that determine whether enacted laws translate into functioning institutions.

AI does not codify. It does not harmonize conflicting provisions based on policy intent. It does not decide which IRR interpretation best serves legislative purpose. It does not exercise the Speaker's judgment on committee referrals. Those are human functions.

But AI identifies every cross-reference across 89 BAAs in minutes. It flags every terminology inconsistency. It generates IRR frameworks that agencies can refine rather than build from nothing. It tracks amendment chains that no staff member can hold in memory. It builds the legislative tracking system that makes pipeline management instantaneous. And it maps enacted legislation back to development goals so the planning cycle stays current.

The practical workflow follows the same pattern as every chapter in this guidebook:

1. **Prepare the corpus** — digitize and tag all enacted BAAs, resolutions, and IRRs
2. **Prompt precisely** — use the structured prompts in this chapter, adapted to your specific codification or tracking task
3. **Verify against enacted text** — AI-generated cross-references, conflict flags, and IRR frameworks must be checked against the actual provisions
4. **Connect to action** — every codification finding should lead to a concrete outcome: an amendment proposal, an IRR deadline, a planning adjustment, or a harmonization recommendation

The final chapters of this guidebook address the ethical framework (Chapter 12), the implementation roadmap (Chapter 13), training and capacity building (Chapter 14), and the long-term vision for AI-augmented governance in BARMM (Chapter 15).

---

## Footnotes

[^1]: The Bangsamoro Transition Authority Parliament has enacted BAA 1 through BAA 89 as of January 2026. See the BAA Quick-Reference Index for the complete categorized list.

[^2]: The 13 domain categories are derived from the BAA Quick-Reference Index: Governance & Administration, Budget & Appropriations, Health, Education & Culture, Economy & Labor, Environment & Development, Social Welfare & Human Rights, Electoral, Local Government, Symbols & Identity, Peace & Security, Holidays, and Miscellaneous.

[^3]: Republic Act No. 11054 (Bangsamoro Organic Law), Art. XVI, Sec. 4. The BOL mandates the BTA to enact priority codes including the Administrative Code, Revenue Code, Electoral Code, Local Government Code, Civil Service Code, Education Code, and Investment Code during the transition period.

[^4]: BAA 84 (Bangsamoro Budget System Act of 2025) establishes the comprehensive budget cycle framework for the Bangsamoro Government. BAA 82 (Bangsamoro Labor and Employment Code) provides the labor and employment regulatory framework for BARMM.

[^5]: See Chapter 10, Section 10.4 (Compliance Monitoring Across BAAs) and the case study on tracking IRR compliance across priority codes.

[^6]: BAA 84 (Bangsamoro Budget System Act of 2025). The Budget System Act covers budget preparation, authorization, execution, and accountability for the Bangsamoro Government.

[^7]: Saidamen R. Mambayao, *Bill Drafting Guidebook for the Bangsamoro Parliament: A Practical Guide for Members of Parliament, Parliamentary and Legislative Staff, Bill Drafters, and Consultants* (2026), Chapters 2 and 5. The Bill Drafting Guidebook distinguishes between bills (which become BAAs) and resolutions (which express the sense of Parliament).

[^8]: The WHEREAS-RESOLVED structure follows standard parliamentary drafting convention. WHEREAS clauses establish the preamble (factual and legal basis); RESOLVED clauses state the operative provisions. See the *Bill Drafting Guidebook*, Chapter 5, for the complete resolution drafting framework.

[^9]: Amendment chain as of March 2026: BAA 14 amends BAA 3 (extends FY 2020 appropriations). BAA 37 amends BAA 13 (seat of government). BAA 33 amends BAA 23 (extends FY 2022 GAA). BAA 52 amends BAA 32 (extends FY 2023 GAA). BAA 87 and BAA 88 amend BAA 35 (Electoral Code). BAA 70 amends BAA 54 (Municipality of Datu Sinsuat Balabaran). BAA 71 amends BAA 55 (Municipality of Sheik Abas Hamza). BAA 77 and BAA 58 were declared unconstitutional by the Supreme Court in *Ali et al. v. BTA* (G.R. No. E-02219) and *Macapaar et al. v. COMELEC* (G.R. No. E-02235), decided September 30, 2025. BAA 86 (Parliamentary District Act) was enacted in January 2026 as the replacement.

[^10]: Bangsamoro Development Plan 2023-2028, Chapter 4. The BDP identifies six overarching development goals: (1) Just and lasting peace, (2) Moral governance, (3) Meaningful self-determination, (4) Economic development and poverty reduction, (5) Quality social services, (6) Cultural identity and diversity. Eight cross-cutting strategies support these goals.

[^11]: See Chapter 10, Section 10.6 (The Accountability Chain: From AI Analysis to Formal Action). The six-link accountability chain traces the path from AI-generated detection through verification, preparation, committee action, follow-up, and formal recommendation.
