# Chapter 7 — AI for Legislative and Policy Work

The Bangsamoro Parliament has enacted 89 Bangsamoro Autonomy Acts since 2019.[^1] These 89 laws span 13 domains — governance, budget, health, education, labor, local government, electoral, environment, social welfare, symbols, peace and security, and more.[^2] Behind every enacted BAA sits a chain of documents: explanatory notes, committee reports, legislative briefers, comparative matrices, interpellation questions, floor amendment proposals, and policy research papers. Each document requires research, cross-referencing, and drafting under tight parliamentary timelines.

This is the legislative reality AI was built to accelerate. AI does not vote on bills. It does not exercise political judgment. But it can scan 89 enacted BAAs for conflicts in under a minute. It can draft an explanatory note from a policy brief overnight. It can prepare interpellation questions that anticipate the sponsor's likely responses. The staff analyst who once spent three days preparing a legislative briefer can now produce a stronger first draft in three hours — and spend the remaining time on the analysis that requires human judgment.

This chapter maps AI onto the entire legislative process, from initial research through enactment. It gives you specific prompts, real BARMM examples, and cross-references to the *Bill Drafting Guidebook for the Bangsamoro Parliament* where deeper procedural guidance exists.[^3]

---

## 7.1 AI in the Legislative Process — From Research to Enactment

The Bangsamoro Parliament follows a defined process for enacting legislation. The *Bill Drafting Guidebook* documents this in full across Chapters 2 and 7.[^4] Here, the focus is on **where AI enters** at each stage and **what it can do** at that point.

### Table 7.1: Legislative Process Stages with AI Entry Points

| Stage | What Happens | Key Documents | AI Can | AI Cannot |
|-------|-------------|---------------|--------|-----------|
| **1. Legislative Directive** | MP identifies a policy need; staff receives instructions | Initial Legislative Template | Scan BDP 2023-2028 for alignment; check if existing BAAs already cover the topic | Decide what legislation to pursue |
| **2. Legislative Research** | Staff researches the policy landscape, existing laws, comparative models | Legislative Research Briefer, Policy Landscape Scan | Search and summarize existing BAAs, national laws, and comparative legislation; identify gaps and conflicts | Assess political feasibility or stakeholder sentiment |
| **3. First Draft** | Drafter prepares the bill text, explanatory note, and comparative matrix | Working Outline, Draft Bill, Comparative Matrix | Generate first drafts of provisions, definitions, and explanatory notes from policy research | Guarantee BOL compliance without human legal review |
| **4. Consultation** | Experts, agencies, and constituents provide feedback | Consultation summaries, expert position papers | Synthesize consultation inputs; identify recurring themes and objections | Replace face-to-face stakeholder engagement |
| **5. Review and Revision** | Staff revises draft based on consultation findings | Revised Draft, Gap Analysis | Compare drafts to flag what changed; check internal consistency | Make political trade-off decisions |
| **6. Finalization and Filing** | MP approves; co-authors sign; bill filed with Bills and Index Division | Final Draft Bill | Format the bill per parliamentary conventions; generate co-authorship memo | Authorize filing or represent MP intent |
| **7. Committee Stage** | Committee examines the bill, holds hearings, proposes amendments | Committee Report, Hearing Minutes | Prepare committee briefers; draft proposed amendments with justifications | Conduct committee hearings |
| **8. Interpellation** | MPs question the bill's sponsor on the floor | Interpellation questions, anticipated answers, manifestations | Generate question trees; anticipate sponsor responses; draft manifestations | Exercise parliamentary privilege |
| **9. Floor Amendments and Voting** | Plenary debates, amends, and votes | Floor amendments, voting manifestations | Draft amendment language; prepare vote manifestation talking points | Cast votes |
| **10. Enrollment and Executive Action** | Enrolled bill transmitted to Chief Minister | Enrolled copy | Verify enrolled text against approved version | Authenticate the enrolled bill |

Use this table as your master reference. Every section in this chapter corresponds to one or more of these stages. When you receive a legislative assignment, locate the stage first, then go to the relevant section.

---

## 7.2 Legislative Research with AI

Legislative research is the foundation. A bill built on weak research will collapse during interpellation. AI transforms this phase by compressing weeks of manual searching into hours of structured analysis. But the human researcher still directs the inquiry, validates the sources, and exercises judgment about relevance.

The *Bill Drafting Guidebook*, Chapter 2, Section 2.3, covers legislative research in procedural detail.[^5] This section focuses on the AI techniques that make that research faster and deeper.

---

### 7.2.1 Policy Landscape Scanning

Before drafting a single provision, you need the **policy landscape** — a map of every law, regulation, policy, plan, and ongoing initiative that touches your bill's subject matter.

**The manual approach:** Open each of the 89 BAAs, read the title and scope provisions, check for relevance, note overlaps, and compile a list. Then do the same for relevant national laws, executive orders, and IRRs. This takes days.

**The AI approach:** Load the full list of enacted BAAs (with short titles and categories) into your AI context. Ask it to identify every BAA that intersects with your topic. Then expand to national laws using web search or uploaded reference documents.

> **Sample Prompt — Policy Landscape Scan:**
>
> ```
> You are a legislative researcher for the Bangsamoro Parliament.
>
> I am preparing a bill on [TOPIC]. Scan the following list of 89
> enacted Bangsamoro Autonomy Acts and identify every BAA that:
> 1. Directly addresses this topic
> 2. Contains provisions that may overlap or conflict
> 3. Establishes agencies, commissions, or offices with related mandates
> 4. Defines terms that this bill must adopt or reconcile
>
> For each relevant BAA, provide:
> - BAA number and short title
> - Specific relevant provisions (section/article numbers if available)
> - Nature of the relationship (direct overlap, adjacent authority,
>   definitional dependency, potential conflict)
>
> Also identify relevant national laws (Republic Acts) that apply
> within BARMM under BOL Article V's power allocation framework.
>
> [Paste the BAA quick-reference table or index here]
> ```

**What to verify:** AI may miss BAAs whose relevance is indirect. Always cross-check its list against the full categorized index. If your bill touches health, do not rely only on BAAs the AI categorized as health-related — also check social welfare, local government, and budget BAAs that may contain health provisions. For example, BAA 85 (GAA FY 2026) contains special purpose funds that may affect health program delivery.[^6]

---

### 7.2.2 Comparative Legislation Analysis

Every strong bill draws from **comparative models** — how other jurisdictions addressed the same policy problem. For BARMM, this means three tiers of comparison:

1. **National Philippine laws** on the same subject (e.g., for a Bangsamoro Labor Code, compare with the national Labor Code and subsequent amendments)
2. **ARMM Muslim Mindanao Autonomy Acts (MMAAs)** that the Bangsamoro Parliament may have repealed, amended, or superseded
3. **International frameworks** relevant to the Bangsamoro context (ASEAN standards, OIC guidelines, UN conventions the Philippines has ratified)

AI handles comparative analysis well because it involves pattern-matching across structured documents. Feed it two or three laws on the same topic. Ask it to identify differences in scope, coverage, definitions, enforcement mechanisms, and institutional arrangements.

> **Sample Prompt — Comparative Legislation Analysis:**
>
> ```
> Compare the following three laws addressing [TOPIC]:
>
> 1. [National law - paste or summarize key provisions]
> 2. [BAA or MMAA - paste or summarize key provisions]
> 3. [International framework - paste or summarize key provisions]
>
> For each law, analyze:
> - Scope and coverage (who is covered, what activities, what territory)
> - Key definitions and whether they align or conflict
> - Enforcement mechanisms and penalties
> - Institutional responsibilities (which agency implements)
> - Gaps that the proposed Bangsamoro bill could address
>
> Present findings in a comparison matrix with rows for each criterion
> and columns for each law. After the matrix, list the three most
> significant gaps the proposed bill should fill.
> ```

**Real BARMM example:** When the BTA enacted BAA 82 (Bangsamoro Labor and Employment Code), drafters needed to reconcile provisions with the national Labor Code while exercising the Bangsamoro's enumerated power over labor under BOL Article V, Section 2.[^7] A comparative analysis using AI would map every section of the national Labor Code against BAA 82's provisions, flagging areas where the Bangsamoro law extends, modifies, or defers to national law.

---

### 7.2.3 Cross-Referencing 89 BAAs

The 89 enacted BAAs form an interconnected legal web. BAA 37 amends BAA 13. BAA 70 amends BAA 54. BAA 87 and BAA 88 both amend BAA 35.[^8] BAA 86 replaced the unconstitutional BAA 58 and BAA 77 after the Supreme Court's ruling in *Ali et al. v. BTA* and *Macapaar et al. v. COMELEC*.[^9] Miss one of these amendment chains and your bill may contradict an already-amended provision.

**Why cross-referencing matters:** A bill proposing to create a new government body must check BAA 13 (Administrative Code) for organizational requirements, BAA 17 (Civil Service Code) for staffing rules, BAA 11 (Power of Appointment) for how leaders are appointed, and the current GAA for funding implications. Skip any one and the committee will catch it during hearings.

**The AI approach:** Load the BAA index or quick-reference table into your AI context. Then give it your draft bill's key provisions and ask it to trace every connection.

> **Sample Prompt — BAA Cross-Reference Check:**
>
> ```
> I am drafting a bill that creates a [NEW BODY/PROGRAM/REGULATION]
> in BARMM.
>
> Cross-reference this draft against the following enacted BAAs and
> identify potential conflicts, dependencies, or required references:
>
> Key provisions of my draft:
> [Paste your draft bill or its working outline]
>
> Check specifically:
> 1. Does any existing BAA already establish a body with overlapping
>    mandate? (Check BAAs 4, 5, 6, 8, 10, 12, 31, 49, 59, 83)
> 2. Does the draft comply with organizational requirements under
>    BAA 13 (Administrative Code)?
> 3. Does the draft comply with civil service requirements under
>    BAA 17 (Civil Service Code)?
> 4. Does the appointment mechanism comply with BAA 11
>    (Power of Appointment)?
> 5. Does the draft use terms defined differently in any existing BAA?
> 6. Are there amendment chains I need to account for?
>    (e.g., BAA 37 amends BAA 13; BAA 70 amends BAA 54)
>
> For each finding, cite the specific BAA and section.
> [Paste BAA quick-reference table]
> ```

**What to verify:** AI cross-referencing is only as good as the data you provide. If you feed it only BAA titles and short descriptions, it will catch obvious overlaps but miss subtle definitional conflicts buried in specific sections. For high-stakes bills, supplement the AI scan with manual review of the most relevant BAAs — especially the four priority codes (BAA 13, BAA 17, BAA 18, BAA 35) that form BARMM's core legal infrastructure.[^10]

---

## 7.3 AI-Assisted Bill Drafting

Bill drafting is the core legislative craft. The *Bill Drafting Guidebook* devotes four chapters to it: Chapter 3 (Anatomy of a Bill), Chapter 4 (Special Bill Types), Chapter 6 (Legislative Style), and Chapter 10 (Amendments).[^11] AI does not replace mastery of those chapters. It accelerates the mechanical work so the drafter can focus on substance and precision.

### What AI Can Draft

AI is effective for generating **first drafts** of the following bill components:

- **Explanatory Notes** — the policy narrative that accompanies the bill, explaining its purpose, context, and expected impact
- **Declaration of Policy** sections — articulating the legislative intent in the format the Parliament expects
- **Definition of Terms** — generating initial definitions based on the bill's subject matter, then refining them against existing BAA definitions
- **Administrative Provisions** — implementing agencies, reporting requirements, IRR timelines
- **Final Provisions** — separability, repealing, and effectivity clauses that follow standardized formulas
- **Comparative Matrices** — side-by-side comparison of the draft bill against existing laws

### What AI Should Not Draft Alone

These components require drafter judgment, political awareness, and legal expertise that AI cannot replicate:

- **Substantive provisions** that create rights, impose obligations, or allocate powers — AI can generate options, but the drafter must decide what the law commands
- **Penalty provisions** — criminal penalties, civil sanctions, and administrative fines require calibration against proportionality principles and existing penal frameworks
- **Appropriation provisions** — budget amounts must come from MFBM data, not AI estimates
- **Shari'ah compliance provisions** — require consultation with Islamic legal scholars per BOL Article X[^12]

### The AI-Assisted Drafting Workflow

Follow this five-step workflow for AI-assisted bill drafting:

**Step 1 — Feed the research.** Upload or paste your policy landscape scan, comparative analysis, and cross-reference findings. The more context the AI has, the better its draft.

**Step 2 — Start with the explanatory note.** Draft the explanatory note first. It forces you to articulate the problem, the proposed solution, and the expected impact before writing a single provision. The *Bill Drafting Guidebook*, Chapter 3, Section 3.1.1, describes the explanatory note's purpose and structure.[^13]

> **Sample Prompt — Explanatory Note:**
>
> ```
> Draft an explanatory note for a proposed Bangsamoro Autonomy Act on
> [TOPIC]. Use the following structure:
>
> 1. BACKGROUND AND CONTEXT — The problem this bill addresses.
>    Include relevant statistics and conditions in BARMM.
> 2. POLICY AND LEGAL BASIS — Why the Bangsamoro Parliament has
>    the authority to legislate on this topic. Cite BOL Article V,
>    Section 2, and the specific enumerated power.
> 3. SALIENT FEATURES — The bill's key provisions in summary.
> 4. EXPECTED IMPACT — What the bill will achieve if enacted.
> 5. ALIGNMENT — How the bill supports the Bangsamoro Development
>    Plan 2023-2028 and the Chief Minister's 12-Point Priority Agenda.
>
> Source material:
> [Paste research findings, policy brief, and BDP alignment notes]
>
> Write in direct, professional legislative prose. Avoid filler
> language. Every sentence must advance the argument for enactment.
> Mark any claim without a source as [VERIFY].
> ```

**Step 3 — Draft the working outline.** Use the AI to convert your explanatory note into a **working outline** — the skeletal structure of the bill showing articles, sections, and subsections. The *Bill Drafting Guidebook*, Chapter 2, Section 2.4.1, describes this step.[^14]

**Step 4 — Draft individual provisions.** Work section by section. Give the AI the working outline, the relevant portion of your research, and clear instructions about what each section should accomplish. Review each provision against the style rules in the *Bill Drafting Guidebook*, Chapter 6 — particularly the rules on "shall," "may," and "must" (Section 6.9); active voice (Section 6.11); and sentence length (Section 6.12).[^15]

**Step 5 — Run the quality review.** Use the AI to perform the self-review checklist from the *Bill Drafting Guidebook*, Chapter 11.[^16] Feed it the complete draft and ask it to check for:

- BOL compliance (does every provision fall within enumerated powers?)
- Internal consistency (are terms used the same way throughout?)
- Completeness (does every duty have an accountable body? does every violation have a consequence?)
- Existing BAA conflicts (does anything contradict an enacted law?)

---

> ### Case Study: AI-Assisted Cross-Referencing for BAA 86
>
> **The situation:** In October 2025, the Supreme Court declared BAA 58 (Parliamentary Districts Creation) and BAA 77 (Reconstituted Parliamentary Districts) unconstitutional in *Ali et al. v. BTA* (G.R. No. E-02219) and *Macapaar et al. v. COMELEC* (G.R. No. E-02235).[^17] The BTA needed to enact fresh redistricting legislation — fast.
>
> **The cross-referencing challenge:** The new bill had to account for the Sulu exclusion following *Province of Sulu v. Medialdea* (G.R. Nos. 242255, 243246, 243693; Sept. 9, 2024; finalized Nov. 26, 2024),[^18] the creation of 8 new SGA municipalities under BAAs 41-48, and the electoral machinery in BAA 35 (Electoral Code) as amended by BAAs 87 and 88.
>
> **How AI would accelerate this:** An AI cross-reference scan of the full BAA index against the term "parliamentary district" would surface BAAs 35, 58, 77, 86, 87, and 88 — the complete amendment chain. Scanning for "SGA" or "Special Geographic Area" would surface BAAs 41-48 (the eight new municipalities) and confirm their constituent barangays. Scanning for "Sulu" would flag every BAA that referenced Sulu in its coverage — allowing drafters to verify that the new law correctly excluded Sulu from the district allocation.
>
> **The result:** BAA 86 (Parliamentary District Act) was enacted on January 20, 2026, establishing 32 single-member parliamentary districts across the post-Sulu BARMM territory: Lanao del Sur (9 districts), Maguindanao del Norte (5), Maguindanao del Sur (5), Basilan (4), Tawi-Tawi (4), Cotabato City (3), and the SGA (2).[^19]
>
> **The lesson:** Cross-referencing is not a luxury — it is a legislative necessity. AI reduces the risk of missing an amendment chain, an excluded territory, or a conflicting provision. But the drafter must still verify every AI finding against the actual enacted text.

---

## 7.4 Preparing Legislative Briefers with AI — The 13-Section CSW Format

The **Legislative Analysis Briefer** is the single most important staff document in the Bangsamoro Parliament. It is the Completed Staff Work (CSW) that equips a Member of Parliament to engage intelligently during committee hearings, interpellation, and plenary voting. The *Bill Drafting Guidebook*, Chapter 8, lays out the full 13-section format.[^20]

AI does not replace the briefer writer. It accelerates the research-intensive sections and generates structured first drafts that the writer then validates and refines.

### The 13 Sections and Where AI Helps Most

| Section | Content | AI Contribution | Human Judgment Required |
|---------|---------|----------------|------------------------|
| **1. Brief Description** | What the bill does in 2-3 paragraphs | Draft from the bill's explanatory note and long title | Verify accuracy against actual bill text |
| **2. Related Laws and Issuances** | Every existing law that touches the bill | Full cross-reference scan (see Section 7.2.3) | Validate completeness; add IRRs and EOs |
| **3. Policy and Legal Analysis** | How the bill fits the legal hierarchy and BOL | Analyze BOL compliance, constitutional issues | Assess political dimensions the AI cannot see |
| **4. Impact Assessment** | Economic, social, institutional effects | Generate impact categories from the bill's provisions | Calibrate severity and likelihood of impacts |
| **5. Shari'ah Considerations** | Alignment with Islamic jurisprudence | Flag provisions that touch personal law, inheritance, or family matters | Consult Islamic legal scholars for authoritative rulings |
| **6. Gender Analysis** | Differential impact on men and women | Scan for gender-neutral language; identify provisions with gendered effects | Apply GAD lens to policy implications |
| **7. Implementing Agencies** | Who implements, with what resources | Extract from the bill's administrative provisions | Verify institutional capacity and readiness |
| **8. Implementation Timeline** | Phased rollout, IRR deadlines | Generate a timeline from the bill's transitory provisions | Assess whether the timeline is realistic |
| **9. Budgetary Implications** | Cost estimates and funding sources | Calculate from the bill's appropriation section and comparable BAAs | Verify with MFBM data and current fiscal position |
| **10. Prior Proceedings** | What happened in committee and previous readings | Summarize hearing minutes and committee reports | Confirm accuracy of procedural history |
| **11. Interpellation Questions** | Questions for the sponsor during plenary | Generate question trees (see Section 7.5) | Select the strategic questions that advance the MP's position |
| **12. Proposed Amendments** | Specific textual changes with justifications | Draft amendment language (see *Bill Drafting Guidebook*, Chapter 10) | Decide which amendments to prioritize |
| **13. MP's Position** | The Member's speech or vote manifestation | Draft talking points based on the full analysis | The MP's political judgment is final |

> **Sample Prompt — Legislative Briefer (Sections 1-4):**
>
> ```
> Prepare the first four sections of a Legislative Analysis Briefer
> for [BILL NUMBER AND TITLE]. Use the 13-section CSW format.
>
> Section 1 — Brief Description:
> Summarize the bill in 2-3 paragraphs. State what it does, who it
> covers, and what it changes in the current legal framework.
>
> Section 2 — Related Laws and Issuances:
> List every existing law that relates to this bill. Include:
> - Relevant BOL provisions (cite article and section)
> - Enacted BAAs (cite number and short title)
> - National laws (cite RA number)
> - Existing IRRs and executive orders
> For each, explain the specific relationship to this bill.
>
> Section 3 — Policy and Legal Analysis:
> Analyze whether the bill falls within the enumerated powers of the
> Bangsamoro Government under BOL Art. V, Sec. 2. Identify any
> provisions that may overlap with national law and require
> intergovernmental coordination per BOL Art. VI.
>
> Section 4 — Impact Assessment:
> Assess the bill's expected impact on: (a) BARMM institutions,
> (b) affected populations, (c) the regional budget,
> (d) existing programs and services.
>
> Source material:
> [Paste the full bill text or its key provisions]
> [Paste the BAA quick-reference table]
> [Paste relevant BOL provisions]
>
> Mark any assertion without a verified source as [VERIFY].
> ```

**Workflow tip:** Draft the briefer in two passes. First pass: use AI for Sections 1, 2, 3, 7, and 8 (these are research-heavy and benefit most from AI's scanning speed). Second pass: draft Sections 4, 5, 6, 9, 11, and 12 with AI assistance but heavier human input. Sections 10 and 13 require institutional knowledge and the MP's direction — draft these last.

---

## 7.5 AI for Interpellation and Plenary Preparation

Interpellation is where legislative homework meets parliamentary performance. A well-prepared interpellator exposes weaknesses in a bill. A poorly prepared one wastes plenary time and loses credibility. The *Bill Drafting Guidebook*, Chapter 8, Sections 8.4.1 through 8.4.3, covers interpellation preparation in detail.[^21]

AI transforms interpellation preparation in three ways: it generates **question trees**, it **anticipates sponsor responses**, and it drafts **manifestation statements**.

### Generating Question Trees

A **question tree** starts with a strategic objective (what do you want to establish during interpellation?) and branches into primary questions, follow-up questions, and contingency questions based on possible answers.

> **Sample Prompt — Interpellation Question Tree:**
>
> ```
> I am preparing for interpellation of [BILL NUMBER AND TITLE].
>
> My strategic objectives are:
> 1. [Objective 1 — e.g., establish that the bill's implementing
>    agency lacks capacity]
> 2. [Objective 2 — e.g., demonstrate that the budget allocation
>    is insufficient]
> 3. [Objective 3 — e.g., show that Section X conflicts with BAA Y]
>
> For each objective, generate:
> - 3 primary questions (open-ended, establishing facts)
> - 2 follow-up questions per primary question (narrowing,
>   building the argument)
> - 1 closing question per objective (designed to establish the
>   record for your proposed amendment)
>
> For each question, anticipate the sponsor's likely response and
> indicate whether the response helps or hurts my objective.
>
> Format as a branching tree:
> Objective → Primary → Follow-up (if sponsor says X) →
> Follow-up (if sponsor says Y) → Closing
>
> Source material:
> [Paste the bill text and your legislative briefer analysis]
> ```

### Anticipating Sponsor Responses

The sponsor and their staff will also prepare for interpellation. AI can model the sponsor's likely defense by analyzing the bill's explanatory note, the committee report, and the sponsor's public statements on the topic.

> **Sample Prompt — Sponsor Response Analysis:**
>
> ```
> Based on the following bill and its explanatory note, predict how
> the bill's sponsor would respond to each of these interpellation
> questions:
>
> [Paste questions]
> [Paste bill text and explanatory note]
>
> For each predicted response, identify:
> 1. The strongest point in the sponsor's defense
> 2. The weakest point that a follow-up question could exploit
> 3. A suggested follow-up question targeting that weakness
> ```

### Drafting Manifestations

A **manifestation** is a statement a Member of Parliament makes on the record during plenary deliberation. It may express support, opposition, a reservation, or an explanation of vote. The *Bill Drafting Guidebook*, Chapter 8, Section 8.6, covers position speeches and vote manifestations.[^22]

> **Sample Prompt — Vote Manifestation:**
>
> ```
> Draft a 1-minute vote manifestation for [MP NAME] on
> [BILL NUMBER AND TITLE].
>
> Position: [SUPPORT / OPPOSE / SUPPORT WITH RESERVATIONS]
>
> Key points to include:
> 1. [Main reason for the position]
> 2. [Reference to a specific provision — cite section number]
> 3. [Reference to alignment or conflict with BDP 2023-2028
>    or BOL mandate]
>
> Tone: Parliamentary, direct, respectful. The manifestation will
> be read aloud in plenary. Keep it under 250 words.
> The MP speaks in [English/Filipino/Taglish].
> ```

---

## 7.6 Policy Recommendation Drafting with AI — Bardach's Eightfold Path Accelerated

Not all policy work results in legislation. Some produces **policy recommendations** — structured analyses that inform executive action, ministerial decisions, or intergovernmental positions. Eugene Bardach's **Eightfold Path** is the standard methodology taught in Philippine public policy programs.[^23] AI accelerates every step.

### The Eightfold Path with AI Entry Points

| Step | Bardach's Step | What You Do | AI Accelerates |
|------|---------------|-------------|----------------|
| 1 | **Define the Problem** | Articulate the policy problem in one clear statement | Scan BDP 2023-2028, BAAs, and situational data to sharpen the problem definition |
| 2 | **Assemble the Evidence** | Gather data, studies, reports, and stakeholder positions | Summarize uploaded documents; extract relevant data points; organize evidence by theme |
| 3 | **Construct the Alternatives** | Develop 3-5 policy options (always including "status quo") | Generate options from comparative analysis; ensure each option is distinct and actionable |
| 4 | **Select the Criteria** | Choose evaluation criteria (cost, effectiveness, equity, political feasibility, administrative feasibility) | Propose criteria based on the policy domain; weight them per BARMM governance priorities |
| 5 | **Project the Outcomes** | Estimate what each alternative would produce against each criterion | Model projected outcomes based on available data; flag assumptions as [ASSUMPTION] |
| 6 | **Confront the Trade-offs** | Compare alternatives and identify what you gain and lose with each | Generate a trade-off matrix; highlight where criteria conflict |
| 7 | **Decide** | Recommend the best alternative with justification | Draft the recommendation narrative; this remains a human decision |
| 8 | **Tell Your Story** | Present the recommendation clearly to the decision-maker | Draft the policy memo, executive summary, or presentation deck |

### The AI-Assisted Policy Recommendation Workflow

**Step 1 — Problem definition.** Feed the AI your raw situational data — BDP chapters, ministry reports, constituent complaints, media coverage. Ask it to synthesize these into a **one-paragraph problem statement** that identifies the gap between the current situation and the desired outcome.

**Step 2 — Evidence assembly.** Upload your documents into a context-rich AI session. Ask it to organize the evidence into categories: quantitative data, qualitative findings, legal provisions, and stakeholder positions. Have it flag evidence gaps where you need additional research.

**Step 3 — Alternative construction.** Ask the AI to generate four to five distinct policy options based on the evidence. Require it to include the **status quo** as one option (this is the baseline against which all alternatives are measured). Each option should be described in one paragraph with its core mechanism and expected coverage.

> **Sample Prompt — Policy Alternatives:**
>
> ```
> Based on the following problem statement and evidence summary,
> generate 5 policy alternatives for addressing [POLICY PROBLEM]
> in BARMM.
>
> Requirements:
> 1. Alternative 1 must be "Status Quo" — describe what happens
>    if the Bangsamoro Government takes no new action
> 2. Alternatives 2-5 must be distinct approaches, not variations
>    of the same approach
> 3. Each alternative must specify: the mechanism (what action is
>    taken), the implementing body, the estimated cost range, and
>    the timeline
> 4. At least one alternative must be achievable within existing
>    BAA authority (no new legislation required)
> 5. At least one alternative must involve new legislation
>
> Problem statement:
> [Paste your refined problem statement]
>
> Evidence summary:
> [Paste your organized evidence]
>
> Mark any cost estimate as [ESTIMATE - VERIFY WITH MFBM].
> ```

**Steps 4-6 — Criteria, projections, and trade-offs.** Ask the AI to build a **decision matrix** with alternatives as rows and criteria as columns. Have it score each alternative on a 1-5 scale, then generate the trade-off analysis. The human analyst reviews and adjusts the scores based on institutional knowledge the AI does not have — particularly **political feasibility** and **administrative capacity**, which depend on relationships and conditions that documents cannot fully capture.

**Steps 7-8 — Decision and storytelling.** The recommendation itself is a human decision. AI cannot weigh political risk, assess stakeholder power dynamics, or account for the Chief Minister's priorities beyond what is written in public documents. But once the decision is made, AI excels at **drafting the policy memo** that communicates it. Feed it the decision matrix, the selected alternative, and the justification. Ask it to draft in the format the decision-maker expects.

> **Sample Prompt — Policy Recommendation Memo:**
>
> ```
> Draft a policy recommendation memo for [DECISION-MAKER TITLE]
> on [TOPIC].
>
> Format:
> 1. EXECUTIVE SUMMARY (1 paragraph, max 100 words)
> 2. PROBLEM STATEMENT (from our analysis)
> 3. ALTERNATIVES CONSIDERED (summarize all 5 in 1 paragraph each)
> 4. EVALUATION (present the decision matrix)
> 5. RECOMMENDATION (state the selected alternative and justify)
> 6. IMPLEMENTATION STEPS (numbered, with timeline and responsible
>    office)
> 7. BUDGETARY IMPLICATIONS (cite specific sources for all figures)
>
> Decision matrix and selected alternative:
> [Paste the matrix and your chosen option]
>
> Mark any unverified data as [VERIFY]. All legal citations must
> reference specific section numbers.
> ```

### BARMM-Specific Considerations for Policy Recommendations

Policy recommendations in the Bangsamoro context must address dimensions that generic policy analysis frameworks may overlook:

- **BOL compliance.** Does the recommended action fall within the enumerated powers of the Bangsamoro Government under Article V, Section 2? If it requires intergovernmental coordination, cite Article VI.[^24]
- **Shari'ah alignment.** Does the recommendation affect areas governed by Islamic personal law (marriage, inheritance, family, property relations among Muslims)? If so, note this and recommend consultation with the Shari'ah High Court or Islamic legal scholars.[^25]
- **BDP alignment.** Map the recommendation to specific goals, strategies, and targets in the Bangsamoro Development Plan 2023-2028. The BDP identifies six overarching development goals and eight cross-cutting strategies.[^26]
- **Transition context.** BARMM remains in the transition period under the third BTA (2025-present) with elections scheduled under RA 12064.[^27] Any recommendation must account for the transition timeline and the institutional continuity requirements that come with it.
- **Moral governance.** The Chief Minister's governance framework emphasizes 12 pillars of moral governance. Policy recommendations gain traction when they explicitly align with these pillars.[^28]

---

## Summary

This chapter covered AI's role across the full legislative and policy cycle in BARMM. The core workflow is consistent throughout:

1. **Prepare context** — feed the AI your source documents, the BAA index, and the relevant BOL provisions
2. **Prompt precisely** — use the structured prompts in this chapter as templates, adapted to your specific task
3. **Review critically** — every AI output must be verified against the actual enacted text, not just summaries
4. **Refine iteratively** — the first AI draft is a starting point, not a final product

AI does not replace the legislative researcher, the bill drafter, or the policy analyst. It makes each of them faster, more thorough, and less likely to miss a cross-reference or a conflict. The decisions — what to legislate, what to recommend, how to vote — remain yours.

For the complete procedural framework behind every topic in this chapter, refer to the *Bill Drafting Guidebook for the Bangsamoro Parliament*.[^29] For the AI-assisted CSW templates with section-by-section prompts, see Appendix F of this guidebook.

---

### Cross-References to Other Chapters

| Topic | Where to Go |
|-------|------------|
| Building your BARMM knowledge base for legislative research | Chapter 4, Section 4.3 |
| AI for budget legislation and budget briefers | Chapter 6, Sections 6.2-6.6 |
| AI for oversight of enacted legislation | Chapter 10 |
| AI for codification and legal harmonization | Chapter 11 |
| Ethics of AI-assisted legislative work | Chapter 12 |
| Prompt library for legislative tasks | Appendix A, Section A.3 |
| AI-Assisted Legislative Briefer template | Appendix F |

---

## Footnotes

[^1]: As of January 2026, the Bangsamoro Transition Authority Parliament has enacted BAA 1 through BAA 89. See the BAA Quick-Reference Index for the full categorized list.

[^2]: The 13 domain categories are: Governance & Administration, Budget & Appropriations, Health, Education & Culture, Economy & Labor, Local Government, Electoral, Environment & Development, Social Welfare & Human Rights, Symbols & Identity, Peace & Security, Miscellaneous, and Human Rights. See BAA Quick-Reference Index.

[^3]: Saidamen R. Mambayao, *Bill Drafting Guidebook for the Bangsamoro Parliament: A Practical Guide for Members of Parliament, Parliamentary and Legislative Staff, Bill Drafters, and Consultants* (2026).

[^4]: Mambayao, *Bill Drafting Guidebook*, Chapters 2 (From Legislative Directive to Bill: The Drafting Process) and 7 (How a Bill Becomes a Bangsamoro Autonomy Act).

[^5]: Mambayao, *Bill Drafting Guidebook*, Chapter 2, Sec. 2.3 (Stage 2 — Legislative Research).

[^6]: BAA 85 (GAA FY 2026) contains Special Purpose Funds including the Quick Response Fund and the IMPACT fund, both of which may affect program delivery across multiple sectors.

[^7]: Republic Act No. 11054 (Bangsamoro Organic Law), Art. V, Sec. 2. The enumerated powers include 55 subject areas from (a) administration of justice through (ccc) water supply, among which labor is explicitly listed.

[^8]: BAA 37 amends BAA 13, Book 1, Ch. 2, Sec. 9 (seat of government). BAA 70 amends BAA 54, Sec. 5 (Municipality of Datu Sinsuat Balabaran). BAA 87 and BAA 88 both amend BAA 35 (Electoral Code). See the BAA Quick-Reference Index for the complete amendment chain.

[^9]: *Ali et al. v. BTA*, G.R. No. E-02219; *Macapaar et al. v. COMELEC*, G.R. No. E-02235 (Sept. 30, 2025). The Supreme Court declared BAA 58 and BAA 77 unconstitutional, requiring fresh redistricting legislation.

[^10]: The four enacted priority codes as of March 2026 are: BAA 13 (Administrative Code, Oct. 2020), BAA 17 (Civil Service Code, Feb. 2021), BAA 18 (Education Code, May 2021), and BAA 35 (Electoral Code, 2023). Three priority codes remain pending: Revenue Code, Local Government Code, and Investment Code.

[^11]: Mambayao, *Bill Drafting Guidebook*, Chapters 3 (Anatomy of a Bill), 4 (Special Bill Types), 6 (Legislative Style), and 10 (Amendments).

[^12]: Republic Act No. 11054 (BOL), Art. X (Bangsamoro Justice System). Shari'ah courts have jurisdiction over personal law, property relations among Muslims, and cases involving Muslims within BARMM.

[^13]: Mambayao, *Bill Drafting Guidebook*, Chapter 3, Sec. 3.1.1 (The Explanatory Note).

[^14]: Mambayao, *Bill Drafting Guidebook*, Chapter 2, Sec. 2.4.1 (Preparing the Working Outline).

[^15]: Mambayao, *Bill Drafting Guidebook*, Chapter 6, Secs. 6.9 (Shall, May, and Must), 6.11 (Active Voice and Present Tense), and 6.12 (Sentence Length and Structure).

[^16]: Mambayao, *Bill Drafting Guidebook*, Chapter 11 (Quality Review), Sec. 11.1 (The Drafter's Self-Review Checklist).

[^17]: *Ali et al. v. BTA*, G.R. No. E-02219; *Macapaar et al. v. COMELEC*, G.R. No. E-02235 (Sept. 30, 2025).

[^18]: *Province of Sulu v. Medialdea*, G.R. Nos. 242255, 243246, 243693 (Sept. 9, 2024; finalized Nov. 26, 2024). The Supreme Court upheld the BOL but ruled Sulu was not part of BARMM, as Sulu rejected the BOL by 54.3%. EO 91 (July 30, 2025) realigned Sulu under Region IX.

[^19]: BAA 86 (Parliamentary District Act, Jan. 20, 2026). Establishes 32 single-member parliamentary districts: Lanao del Sur (9), Maguindanao del Norte (5), Maguindanao del Sur (5), Basilan (4), Tawi-Tawi (4), Cotabato City (3), SGA (2).

[^20]: Mambayao, *Bill Drafting Guidebook*, Chapter 8 (Preparing a Legislative Briefer).

[^21]: Mambayao, *Bill Drafting Guidebook*, Chapter 8, Secs. 8.4.1 (Structuring Interpellation Questions), 8.4.2 (Anticipating Answers), and 8.4.3 (Preparing Follow-Up Manifestations).

[^22]: Mambayao, *Bill Drafting Guidebook*, Chapter 8, Sec. 8.6 (Preparing the MP's Position).

[^23]: Eugene Bardach and Eric M. Patashnik, *A Practical Guide for Policy Analysis: The Eightfold Path to More Effective Problem Solving*, 6th ed. (CQ Press, 2019).

[^24]: Republic Act No. 11054 (BOL), Art. V, Secs. 1-3 (Powers of Government); Art. VI (Intergovernmental Relations).

[^25]: Republic Act No. 11054 (BOL), Art. X (Bangsamoro Justice System). The Shari'ah High Court exercises appellate jurisdiction over Shari'ah courts in BARMM.

[^26]: Bangsamoro Development Plan 2023-2028. The six overarching goals address peace and security, good governance, human development, economic development, environmental sustainability, and cultural identity.

[^27]: Republic Act No. 12064 extended the transition period and scheduled the first parliamentary elections. The current (third) BTA was appointed by President Marcos in March 2025.

[^28]: The 12 pillars of moral governance are a core framework of Chief Minister Abdulraof A. Macacua's governance philosophy, emphasizing transparency, accountability, integrity, justice, and service orientation in public administration.

[^29]: Mambayao, *Bill Drafting Guidebook* (2026), complete Table of Contents in the front matter of this guidebook's Appendix L.
