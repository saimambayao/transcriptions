# Appendices

---

## Appendix A — Prompt Library for Common Government Tasks

This appendix provides ready-to-use prompts for six governance domains. Each prompt follows the structure taught in Chapters 2 and 3: role, context, task, format, constraints. Copy the prompt, replace the bracketed placeholders with your specifics, and review the output against the quality check before using it.

**How to use this library:** Find your governance domain (A.1 through A.6). Pick the prompt closest to your task. Modify the bracketed items. Run the prompt. Verify the output against the quality check listed with each prompt.

---

### A.1 Planning and Strategy Prompts

**Prompt A.1.1 — BDP Alignment Check**

*Task:* Verify whether a proposed program aligns with BDP 2023-2028 goals.

```
You are a planning officer for a BARMM ministry.

I am preparing a program proposal for [PROGRAM NAME]. The program aims to [BRIEF DESCRIPTION, 2-3 sentences].

Review this program against the 2nd Bangsamoro Development Plan (BDP 2023-2028) and identify:
1. Which of the 6 BDP goals this program supports (list goal number and name)
2. Which specific BDP strategies it addresses
3. Any BDP macroeconomic or sectoral targets it contributes to
4. Gaps — BDP goals or strategies this program does NOT address but could

Format your response as a table with columns: BDP Goal, Strategy, Target, Alignment Evidence, Gap/Opportunity.
```

*Expected output:* Alignment matrix table with 4-6 rows.
*Quality check:* Verify BDP goal numbers and strategy names against the actual BDP 2023-2028 document.

**Prompt A.1.2 — Situational Analysis Organizer**

*Task:* Structure raw data into a SWOT framework for an office strategic plan.

```
You are a planning analyst for [OFFICE NAME] in BARMM.

I will provide raw data from stakeholder consultations, performance reports, and environmental scans. Organize this data into a SWOT analysis following these rules:
- Strengths and Weaknesses are INTERNAL (within the office's control)
- Opportunities and Threats are EXTERNAL (in the environment)
- Each item must be specific and evidence-based, not generic
- Limit to 5-7 items per quadrant
- For each item, note the source (consultation, report, or scan)

Here is the raw data:
[PASTE YOUR DATA]
```

*Expected output:* Four-quadrant SWOT table with sourced entries.
*Quality check:* Confirm internal/external classification is correct. Remove any generic items ("limited budget" without specifics).

**Prompt A.1.3 — Theory of Change Narrative**

*Task:* Draft a theory of change statement for a program proposal.

```
You are a development planning specialist for BARMM.

Draft a Theory of Change narrative for the following program:
- Program: [NAME]
- Problem statement: [WHAT PROBLEM DOES IT ADDRESS]
- Target beneficiaries: [WHO]
- Key interventions: [WHAT THE PROGRAM WILL DO]
- Expected outcomes: [WHAT CHANGES SHOULD HAPPEN]

Structure the narrative as:
1. If-Then chain: "If [intervention], then [output], leading to [outcome], contributing to [impact]"
2. Assumptions: What must be true for each link in the chain to hold
3. Risks: What could break the chain
4. Evidence base: What evidence supports each causal link

Keep it under 500 words. Write in active voice, present tense.
```

*Expected output:* Theory of change narrative with explicit causal logic.
*Quality check:* Test each "if-then" link. Does the logic hold? Are assumptions realistic for BARMM conditions?

**Prompt A.1.4 — Development Indicator Formulation**

*Task:* Convert a vague objective into measurable indicators.

```
I am preparing the Results Framework for [OFFICE/PROGRAM NAME].

Convert the following objective into SMART indicators:
Objective: "[PASTE YOUR OBJECTIVE]"

For each indicator, provide:
- Indicator statement (specific, measurable)
- Baseline value (or note if baseline data collection is needed)
- Target value with timeline
- Data source
- Collection frequency
- Responsible office

Generate 2-3 indicators per objective: at least one output indicator and one outcome indicator.
```

*Expected output:* Results framework table with 2-3 indicators.
*Quality check:* Each indicator must be independently verifiable. Remove any indicator you cannot actually measure with available data.

**Prompt A.1.5 — Stakeholder Mapping**

*Task:* Identify and classify stakeholders for a new program or policy.

```
You are a planning officer preparing a stakeholder analysis for [PROGRAM/POLICY NAME] in BARMM.

Map all relevant stakeholders using this framework:
- Classify by influence (high/low) and interest (high/low)
- For each stakeholder, note: name/office, role in the program, engagement strategy, potential risk if not engaged
- Include: BARMM ministries, national government agencies, LGUs, CSOs, private sector, development partners, traditional/religious leaders, affected communities

Present as a table, then provide a brief engagement priority note (who to engage first and why).
```

*Expected output:* Stakeholder matrix with 10-15 entries.
*Quality check:* Verify that no major stakeholder category is missing. Check that influence/interest classifications match reality.

**Prompt A.1.6 — GAD Analysis for Program Design**

*Task:* Integrate gender analysis into a program proposal.

```
Analyze [PROGRAM NAME] for gender responsiveness. Provide: (1) gender issues in the sector, (2) how the program addresses or fails to address them, (3) recommended adjustments, (4) sex-disaggregated indicators, (5) GAD budget approach. Reference RA 9710 and PCW Harmonized GAD Guidelines.

Program description: [BRIEF DESCRIPTION]
```

*Expected output:* GAD analysis with specific recommendations.
*Quality check:* Confirm RA 9710 references are accurate. Ensure recommendations are actionable within BARMM context.

---

### A.2 Budgeting and Finance Prompts

**Prompt A.2.1 — Budget Variance Analysis**

*Task:* Analyze year-over-year changes in a ministry's budget.

```
You are a budget analyst for the Bangsamoro Parliament.

I will provide two years of budget data for [MINISTRY NAME]:
- FY [YEAR 1] GAA allocation: [PASTE OR DESCRIBE]
- FY [YEAR 2] proposed budget: [PASTE OR DESCRIBE]

Analyze:
1. Total budget change (amount and percentage)
2. Line-item changes: which programs increased, decreased, or are new
3. Top 3 largest increases and their justification (if stated)
4. Top 3 largest decreases and potential impact
5. Personnel Services vs. MOOE vs. Capital Outlay ratio comparison
6. Flags: any unusual patterns (e.g., >50% increase in a single line item, new programs without enabling legislation)

Present findings in a summary table followed by a narrative analysis.
```

*Expected output:* Variance analysis table and 300-500 word narrative.
*Quality check:* Verify all dollar figures and percentages by manual calculation on the top 5 line items.

**Prompt A.2.2 — Budget Scrutiny Questions**

*Task:* Generate questions for committee budget deliberations.

```
You are a committee secretary preparing budget scrutiny questions for the Committee on [COMMITTEE NAME].

Based on the following ministry budget proposal:
[PASTE BUDGET SUMMARY OR KEY FIGURES]

Generate 10 scrutiny questions covering:
- Utilization rate of prior year's budget
- Justification for significant increases
- Alignment with BDP 2023-2028 priorities
- Personnel complement vs. filled positions
- Status of prior year's unfunded programs
- Capital outlay implementation readiness
- Revenue generation targets (if applicable)

For each question, note: the specific budget item it targets and the expected response format.
```

*Expected output:* Numbered list of 10 questions with budget item references.
*Quality check:* Confirm each question references an actual line item in the budget proposal.

**Prompt A.2.3 — COA Finding Response Drafter**

*Task:* Draft management responses to audit observations.

```
You are an accountant preparing management comments for COA audit observations.

For each audit observation below, draft a management response that:
1. Acknowledges the finding (do not be defensive)
2. Explains the context (why the situation occurred)
3. States the corrective action taken or planned
4. Provides the timeline for completion
5. Names the responsible officer

Observation: [PASTE COA OBSERVATION]

Write in formal but clear language. Each response should be 100-200 words.
```

*Expected output:* Structured management response per observation.
*Quality check:* Ensure corrective actions are specific and have realistic timelines. Have the accountant verify technical accuracy.

**Prompt A.2.4 — Obligation and Disbursement Tracker Summary**

*Task:* Summarize financial performance for a quarterly report.

```
Analyze the following obligation and disbursement data for [OFFICE NAME], Q[QUARTER] FY [YEAR]:

[PASTE DATA: allotment, obligations, disbursements by expense class]

Provide:
1. Obligation rate by expense class (PS, MOOE, CO) and total
2. Disbursement rate by expense class and total
3. Comparison to same quarter previous year (if data provided)
4. Programs with lowest obligation rates and potential causes
5. Recommendations to improve utilization before year-end

Format as a dashboard summary: table first, then 3-5 bullet points of key findings.
```

*Expected output:* Financial dashboard summary.
*Quality check:* Recalculate rates manually for the three largest line items.

**Prompt A.2.5 — Annual Procurement Plan AI Review**

*Task:* Check an APP for completeness and compliance.

```
Review the following Annual Procurement Plan for compliance with:
- RA 9184 (Government Procurement Reform Act) requirements
- BAA 84 (Bangsamoro Budget System Act) provisions on procurement planning
- DBM-GPPB Joint Circular guidelines

Check for:
1. Completeness of required columns (PMO, mode of procurement, schedule, ABC)
2. Procurement modes selected — are they appropriate for the ABC amounts?
3. Items that may require early procurement action based on lead times
4. Any items that appear to duplicate existing contracts
5. Total ABC vs. approved budget — is the APP within budget limits?

[PASTE APP DATA OR KEY SECTIONS]
```

*Expected output:* Compliance review with specific findings.
*Quality check:* Verify procurement thresholds against current RA 9184 IRR schedules.

**Prompt A.2.6 — Budget Brief Talking Points**

*Task:* Prepare talking points for a budget presentation to Parliament.

```
Prepare budget presentation talking points for [MINISTRY NAME] FY [YEAR] budget defense before the Committee on Appropriations.

Key data:
- Total proposed budget: [AMOUNT]
- Key programs: [LIST TOP 5]
- Major changes from prior year: [SUMMARY]

Structure as:
1. Opening statement (2-3 sentences): mandate, key achievement, budget request
2. Priority programs (3-5 bullets each): what it does, who benefits, budget amount, expected output
3. Anticipated questions and prepared responses (5 items)
4. Closing appeal (2-3 sentences)

Keep total under 800 words. Use specific numbers, not vague claims.
```

*Expected output:* Structured talking points document.
*Quality check:* Verify all budget figures match the official proposal. Remove any claim not supported by actual data.

---

### A.3 Legislative and Policy Prompts

**Prompt A.3.1 — Policy Landscape Scan**

*Task:* Map existing laws relevant to a proposed bill.

```
You are a legislative researcher for the Bangsamoro Parliament.

I am preparing a bill on [TOPIC]. Scan the following list of enacted Bangsamoro Autonomy Acts and identify every BAA that:
1. Directly addresses this topic
2. Contains provisions that may overlap or conflict
3. Establishes agencies, commissions, or offices with related mandates
4. Defines terms that this bill must adopt or reconcile

Also identify relevant national laws (Republic Acts) that apply to the same subject matter.

Present findings as a table: Law, Key Provisions, Relationship to Proposed Bill (supports/conflicts/supplements).

[PASTE BAA LIST OR PROVIDE TOPIC DETAILS]
```

*Expected output:* Legal landscape matrix.
*Quality check:* Verify every BAA number and title cited. Cross-check against the official BAA index.

**Prompt A.3.2 — Explanatory Note Drafter**

*Task:* Draft an explanatory note for a filed bill.

```
You are a legislative staff member of the Bangsamoro Parliament.

Draft an explanatory note for [BILL TITLE/NUMBER] following this structure:
1. Context and rationale — what problem does this bill address?
2. Legal basis — BOL provisions, national laws, and existing BAAs that authorize this legislation
3. Objectives — what the bill aims to achieve
4. Key features — summary of major provisions (numbered)
5. Fiscal impact — estimated cost and funding source
6. Expected beneficiaries — who benefits and how

Background information:
[PASTE POLICY BRIEF, RESEARCH NOTES, OR BILL SUMMARY]

Write in formal legislative language. Keep under 1,500 words.
```

*Expected output:* Complete explanatory note draft.
*Quality check:* Verify every BOL article and BAA cited. Confirm the bill's provisions match the explanatory note's claims.

**Prompt A.3.3 — Interpellation Question Tree**

*Task:* Prepare questions for interpellation of a bill sponsor.

```
You are a legislative researcher preparing interpellation material for [MP NAME], who will question the sponsor of [BILL TITLE/NUMBER].

Generate a question tree with:
1. Opening questions (scope and intent) — 3 questions
2. Technical questions (specific provisions) — 5 questions
3. Fiscal questions (budget and funding) — 3 questions
4. Implementation questions (who, when, how) — 3 questions
5. Follow-up branches: for each question, provide one follow-up if the sponsor answers "yes" and one if they answer "no"

Base questions on: [PASTE BILL SUMMARY OR KEY PROVISIONS]

Write questions in parliamentary language. Each question should target a specific section or provision.
```

*Expected output:* Branching question tree with 14+ questions.
*Quality check:* Ensure each question references a real provision in the bill.

**Prompt A.3.4 — Committee Report Structure**

*Task:* Draft the structure and key sections of a committee report.

```
Draft a committee report for [BILL TITLE/NUMBER] as reviewed by the Committee on [COMMITTEE NAME].

Include:
1. Background and referral history
2. Summary of committee hearings (dates, resource persons, key testimony)
3. Key issues raised during deliberations
4. Committee amendments (if any) with justification
5. Committee recommendation (approval, approval with amendments, or further study)

Source information:
[PASTE HEARING NOTES, TESTIMONY SUMMARIES, OR COMMITTEE DISCUSSION POINTS]

Follow the format prescribed by the BTA Rules of Procedure and the Bill Drafting Guidebook.
```

*Expected output:* Committee report draft.
*Quality check:* Verify hearing dates and resource person names against actual records.

**Prompt A.3.5 — Policy Recommendation Memo**

*Task:* Draft a policy recommendation for executive action.

```
Draft a policy recommendation memo for [DECISION-MAKER TITLE AND NAME].

Subject: [POLICY ISSUE]

Structure:
1. Issue statement (1 paragraph)
2. Background and context (2-3 paragraphs)
3. Options analysis (3 options minimum):
   - Description of each option
   - Pros and cons
   - Fiscal implications
   - Legal considerations
   - Implementation feasibility
4. Recommended option with justification
5. Proposed next steps with timeline

Base the analysis on: [PASTE RESEARCH DATA, STAKEHOLDER INPUT, OR PRIOR MEMOS]
```

*Expected output:* Decision-ready policy memo.
*Quality check:* Ensure the recommended option is genuinely the strongest, not just the first one listed. Verify fiscal figures.

**Prompt A.3.6 — Amendment Language Drafter**

*Task:* Draft specific amendment text for a bill under deliberation.

```
Draft amendment language for [BILL TITLE/NUMBER].

Amendment target: Section [NUMBER], which currently reads:
"[PASTE CURRENT TEXT]"

Proposed change: [DESCRIBE WHAT THE AMENDMENT SHOULD DO]

Provide:
1. The amended text (showing deletions in strikethrough and additions in bold, or using "DELETE... INSERT..." format)
2. Brief justification (2-3 sentences)
3. Impact on other sections of the bill (cross-reference check)
4. Potential objections the sponsor may raise

Use formal legislative drafting conventions per the Bill Drafting Guidebook.
```

*Expected output:* Amendment text with justification and impact analysis.
*Quality check:* Verify the current text matches the actual bill. Check that the amendment does not create internal contradictions.

**Prompt A.3.7 — IRR Framework Generator**

*Task:* Create the skeletal framework for implementing rules and regulations.

```
Generate an IRR framework for [BAA NUMBER AND TITLE].

For each section of the law that requires implementing rules, provide:
1. The BAA section requiring IRR provisions
2. What the IRR must specify (rules, procedures, standards, timelines)
3. Which agency or office should lead drafting
4. Stakeholders who should be consulted
5. Timeline recommendation

Organize by chapter/article of the BAA. Flag any provisions that are self-executing and do not require IRR.

[PASTE BAA TEXT OR SUMMARY]
```

*Expected output:* IRR development roadmap table.
*Quality check:* Verify every section reference against the actual BAA. Confirm the implementing agencies exist.

---

### A.4 Administrative and Correspondence Prompts

**Prompt A.4.1 — Executive Order Drafter**

*Task:* Draft an executive order or administrative order.

```
Draft an [Executive Order / Administrative Order] for [ISSUING AUTHORITY].

Subject: [TOPIC]
Purpose: [WHAT IT ESTABLISHES, DIRECTS, OR AUTHORIZES]
Legal basis: [ENABLING LAW OR AUTHORITY]

Structure per standard BARMM format:
1. WHEREAS clauses (3-5, establishing context and authority)
2. NOW, THEREFORE clause
3. Numbered sections (purpose, scope, definition of terms, substantive provisions, effectivity)
4. Signature block with title and date

Substantive content: [PASTE YOUR NOTES OR POLICY DECISIONS]
```

*Expected output:* Complete EO/AO draft.
*Quality check:* Verify the legal basis is valid. Confirm the issuing authority has jurisdiction.

**Prompt A.4.2 — Official Correspondence Drafter**

*Task:* Draft a formal letter from a BARMM official.

```
Draft an official letter from [SENDER NAME, TITLE, OFFICE] to [RECIPIENT NAME, TITLE, OFFICE].

Purpose: [REQUEST/ENDORSEMENT/REPLY/TRANSMITTAL/INVITATION]

Key points to cover:
[LIST THE SUBSTANTIVE CONTENT]

Requirements:
- Formal Philippine government correspondence format
- Opening salutation appropriate to the recipient's rank
- Clear action requested or information conveyed
- Appropriate closing and complimentary close
- Reference number placeholder: [REF NO.]

Keep under 400 words. Direct and respectful tone.
```

*Expected output:* Formal letter draft.
*Quality check:* Verify recipient's correct title and office name. Ensure the action requested is clear.

**Prompt A.4.3 — Meeting Minutes Organizer**

*Task:* Convert raw meeting notes into structured minutes.

```
Convert the following raw meeting notes into formal minutes:

[PASTE RAW NOTES]

Format:
1. Header: meeting title, date, time, venue, presiding officer
2. Attendees (with titles and offices)
3. Agenda items (numbered)
4. For each agenda item: summary of discussion, decisions made, action items (who, what, when)
5. Next meeting date
6. Prepared by / Noted by lines

Write in past tense, third person. Attribute decisions to the body, not individuals, unless a specific directive was given.
```

*Expected output:* Formatted meeting minutes.
*Quality check:* Verify attendee names and titles. Confirm action items have specific responsible persons and deadlines.

**Prompt A.4.4 — Travel/Activity Report**

*Task:* Draft a post-activity report from field notes.

```
Draft an activity report based on the following field notes:

Activity: [NAME]
Date(s): [DATES]
Venue: [LOCATION]
Participants: [NUMBER AND TYPE]
Conducted by: [OFFICE/TEAM]

Raw notes:
[PASTE YOUR NOTES]

Structure:
1. Activity overview (1 paragraph)
2. Objectives
3. Proceedings/Activities conducted (chronological)
4. Key findings or outputs
5. Issues and challenges encountered
6. Recommendations
7. Annexes list (attendance sheet, photos, handouts)
```

*Expected output:* Complete activity report.
*Quality check:* Verify dates, participant counts, and venue names.

**Prompt A.4.5 — Memorandum of Agreement Framework**

*Task:* Draft a framework MOA between two BARMM entities.

```
Draft a MOA between [PARTY A — name, office, represented by] and [PARTY B — name, office, represented by].
Purpose: [WHAT THE MOA ESTABLISHES]. Duration: [PERIOD].

Include: WHEREAS clauses, purpose, scope, responsibilities of each party, financial arrangements, confidentiality, amendment/termination, dispute resolution, effectivity, signature blocks.

Key terms: [PASTE KEY TERMS AND RESPONSIBILITIES]
```

*Expected output:* MOA framework draft.
*Quality check:* Verify both parties have authority to enter the agreement. Ensure financial terms are specific.

---

### A.5 Research and Reporting Prompts

**Prompt A.5.1 — Literature Review Synthesizer**

*Task:* Synthesize multiple sources into a structured review.

```
Synthesize the following sources into a literature review on [TOPIC]:

[PASTE SUMMARIES, EXCERPTS, OR SOURCE LIST]

Structure:
1. Overview of the research landscape (what has been studied, what gaps exist)
2. Key themes across sources (organize by theme, not by source)
3. Points of agreement across sources
4. Points of disagreement or debate
5. Implications for BARMM policy/governance
6. Research gaps that future work should address

Cite sources using [Author, Year] format. Keep to 1,500-2,000 words.
```

*Expected output:* Thematic literature review.
*Quality check:* Verify that claims attributed to specific sources actually appear in those sources.

**Prompt A.5.2 — Annual Report Section Drafter**

*Task:* Draft a section of an office annual report from raw data.

```
Draft the [SECTION NAME] section of the FY [YEAR] Annual Report for [OFFICE NAME].

Data provided:
[PASTE KEY ACCOMPLISHMENTS, STATISTICS, NARRATIVES]

Structure:
1. Overview (2-3 sentences summarizing the year's performance)
2. Major accomplishments (bulleted, with specific numbers)
3. Key performance indicators achieved vs. targets (table format)
4. Challenges encountered
5. Plans for the coming year

Tone: factual, achievement-oriented, but honest about challenges. Write in past tense.
Use specific numbers and percentages, not vague qualifiers.
```

*Expected output:* Annual report section draft.
*Quality check:* Verify every number against source data. Remove any unsupported superlatives.

**Prompt A.5.3 — Position Paper Drafter**

*Task:* Draft an office position paper on a policy issue.

```
Draft a position paper for [OFFICE NAME] on [POLICY ISSUE].

Office position: [SUMMARIZE THE OFFICE'S STANCE]

Structure:
1. Executive summary (200 words)
2. Background and context
3. Analysis of the issue (including stakeholder perspectives)
4. Office position and rationale
5. Supporting evidence
6. Recommendations
7. Conclusion

Sources and evidence: [PASTE RELEVANT DATA, LEGAL REFERENCES, PRECEDENTS]

Write in formal analytical tone. 2,000-2,500 words.
```

*Expected output:* Position paper draft.
*Quality check:* Ensure the position is internally consistent. Verify all legal citations.

**Prompt A.5.4 — Comparative Analysis Table Builder**

*Task:* Build a comparison matrix across jurisdictions or programs.

```
Build a comparative analysis table for [TOPIC] across the following [jurisdictions/programs/offices]:
[LIST 3-5 ITEMS TO COMPARE]

Comparison dimensions:
[LIST 5-8 CRITERIA]

For each cell, provide: the specific practice or provision (not a vague summary), and note the source. Add a final row: "Key Takeaway for BARMM" — what BARMM can adopt or adapt from each.
```

*Expected output:* Structured comparison matrix.
*Quality check:* Verify each cell's content against the actual source.

---

### A.6 M&E and Oversight Prompts

**Prompt A.6.1 — KPI Dashboard Builder**

*Task:* Create a performance monitoring dashboard from raw data.

```
Create a KPI dashboard for [OFFICE/PROGRAM NAME] based on the following data:

[PASTE PERFORMANCE DATA: targets, actual accomplishments, timelines]

For each KPI:
1. KPI name and definition
2. Target value
3. Actual value
4. Achievement rate (%)
5. Status: On Track (≥80%), At Risk (50-79%), Off Track (<50%)
6. Brief explanation for any Off Track or At Risk items

Present as a table. Then provide a 3-sentence executive summary highlighting: best performing KPI, worst performing KPI, and overall program health.
```

*Expected output:* KPI dashboard table with executive summary.
*Quality check:* Recalculate achievement rates manually for the top 3 items.

**Prompt A.6.2 — Program Evaluation Framework**

*Task:* Design an evaluation framework for a BARMM program.

```
Design an evaluation framework for [PROGRAM NAME].

Program details:
- Duration: [START-END]
- Budget: [AMOUNT]
- Beneficiaries: [WHO AND HOW MANY]
- Key activities: [LIST]
- Expected outcomes: [LIST]

Include:
1. Evaluation questions (5-7, covering relevance, efficiency, effectiveness, impact, sustainability)
2. For each question: indicators, data sources, data collection methods, analysis approach
3. Evaluation timeline (when to conduct midterm vs. endline)
4. Stakeholder participation in the evaluation
5. Ethical considerations
6. Suggested evaluation team composition
```

*Expected output:* Evaluation framework document.
*Quality check:* Ensure evaluation questions are answerable with available data. Confirm timeline is realistic.

**Prompt A.6.3 — COA Compliance Self-Assessment**

*Task:* Prepare a self-assessment against common COA findings.

```
Conduct a self-assessment for [OFFICE NAME] against the most common COA audit findings in BARMM:

Common finding categories:
1. Cash advances not liquidated within prescribed period
2. Procurement not following RA 9184 procedures
3. Fund utilization below 80% of allotment
4. Incomplete or missing supporting documents
5. Non-compliance with DBM budget execution guidelines
6. Payroll discrepancies
7. Property and inventory management gaps

For each category, help me document:
- Current office status (compliant/partially compliant/non-compliant)
- Evidence of compliance (what records exist)
- Gaps identified
- Corrective actions needed
- Timeline for corrective action
```

*Expected output:* Self-assessment checklist with corrective action plan.
*Quality check:* Each compliance claim must be supported by documentary evidence.

**Prompt A.6.4 — Oversight Analysis of Agency Performance**

*Task:* Analyze an agency's performance report for parliamentary oversight.

```
You are a legislative researcher analyzing [AGENCY NAME]'s performance for the Committee on [COMMITTEE NAME].

Performance data: [PASTE ANNUAL REPORT DATA OR KPIs]
Budget data: [PASTE BUDGET VS. UTILIZATION]

Analyze:
1. Overall mandate fulfillment: is the agency doing what its enabling law requires?
2. Budget utilization: how effectively is the budget being spent?
3. Output delivery: are committed outputs being delivered on time?
4. Gaps between legislative intent and actual implementation
5. Red flags: any patterns suggesting systemic problems

Generate 5 oversight questions for the committee chair to ask the agency head.
```

*Expected output:* Oversight analysis brief with questions.
*Quality check:* Verify budget figures. Confirm the agency's enabling law is correctly cited.

**Prompt A.6.5 — Quarterly Monitoring Report Template**

*Task:* Generate a standardized quarterly monitoring report.

```
Generate a quarterly monitoring report for [PROGRAM/PROJECT NAME], Q[QUARTER] FY [YEAR].

Data:
[PASTE: physical targets vs. accomplishments, financial data, timeline status]

Structure:
1. Executive summary (5 sentences)
2. Physical performance (table: target, actual, %, variance explanation)
3. Financial performance (table: allotment, obligation, disbursement, rates)
4. Implementation issues and bottlenecks
5. Corrective actions taken
6. Outlook for next quarter
7. Recommendations
```

*Expected output:* Complete quarterly monitoring report.
*Quality check:* Verify all percentages by manual calculation. Confirm physical targets match the approved work plan.

---

## Appendix B — Tool Setup Guides

These guides get you from zero to productive in one sitting. Each covers one tool. Screenshots will vary as interfaces update, but the logic stays the same.

---

### B.1 Claude (Web and Desktop)

**Getting started:**

1. **Create an account.** Go to claude.ai. Sign up with your email address. The free tier gives you access to conversational AI. Claude Pro (paid) gives higher usage limits and access to more capable models.

2. **Your first government prompt.** Once logged in, you see a text box. Type a task from Appendix A — start with Prompt A.4.2 (Official Correspondence). Replace the bracketed items with real information. Press Enter. Read the output. Edit it. Send a follow-up prompt asking for changes. You have just completed the four-step workflow from Chapter 3.

3. **Set up a Project.** Claude Projects let you create a persistent workspace with custom instructions and uploaded reference documents.
   - Click "Projects" in the sidebar
   - Create a new project named after your office or function (e.g., "Committee on Appropriations" or "MFBM Budget Division")
   - In Project Instructions, paste a role description: "You are a [role] for [office]. You follow BARMM procedures and reference Philippine laws."
   - Upload key reference documents: your office's mandate (from the enabling BAA), the BDP summary, your office SOP, or any recurring reference you use daily
   - Every conversation within this project will have access to those instructions and documents automatically

4. **Desktop app.** Download Claude Desktop from the Anthropic website. It works the same as the web version but runs as a standalone application. Use it when you want AI assistance while working in other applications.

**Key habits:** Start with a clear task. Provide context. Review every output. Save prompts that work well.

---

### B.2 NotebookLM

**Getting started:**

1. **Access NotebookLM.** Go to notebooklm.google.com. Sign in with your Google account. NotebookLM is free.

2. **Create your first notebook.** Click "New Notebook." Name it after the project or topic (e.g., "BAA 85 Budget Analysis" or "Committee on Education Hearing Prep").

3. **Add sources.** Click "Add Source." You can upload:
   - PDFs (legislative texts, committee reports, audit findings)
   - Google Docs
   - Google Slides
   - Web URLs
   - Pasted text

   Upload 2-5 sources to start. NotebookLM reads and indexes them automatically.

4. **Ask questions.** In the chat panel, ask questions about your sources. NotebookLM answers with citations pointing to specific passages in your uploaded documents. This is the key advantage: every claim is traceable to a source you provided.

5. **Generate outputs.** Use the notebook guide features to:
   - Generate a summary of all sources
   - Create an FAQ from the documents
   - Build a study guide or briefing document
   - Generate an audio discussion (useful for reviewing material while commuting)

**For government use:** Create one notebook per legislative measure, budget review, or oversight inquiry. Upload all relevant documents into that notebook. Use it as your research assistant during deliberations.

---

### B.3 Obsidian as a Government Knowledge Base

**Getting started:**

1. **Install Obsidian.** Download from obsidian.md. It is free for personal use. Obsidian runs locally on your computer — your files never leave your device unless you choose to sync them.

2. **Create a vault.** A vault is a folder on your computer. Create one named after your office (e.g., "BARMM-Budget-Division"). Obsidian will manage everything inside it.

3. **Structure for government use.** Create these top-level folders:

   ```
   /reference/        — Laws, policies, standing documents
   /projects/         — One subfolder per active project or measure
   /meetings/         — Meeting notes
   /templates/        — Reusable templates (briefers, memos, reports)
   /ai-outputs/       — Saved AI-generated drafts for review
   /archive/          — Completed projects (move, don't delete)
   ```

4. **Link your notes.** Obsidian's strength is linking. When you mention a BAA in a meeting note, type `[[BAA 84]]` to create a link to your reference note on that law. Over time, these links create a web of institutional knowledge.

5. **Use with AI.** When preparing a prompt for Claude or NotebookLM, open the relevant Obsidian notes and copy the context you need. When AI produces a useful output, save it in your vault under the relevant project folder. Your vault becomes the institutional memory that survives staff turnover.

**Key principle:** Write notes in your own words. Link them to each other. Review them before meetings. Your vault compounds in value over time.

---

## Appendix C — AI Readiness Assessment Checklist

Use this checklist to assess your office's readiness for AI adoption. Score each item: **Yes = 1 point**, **No = 0 points**. Total your score at the end.

*Instruction:* Have 2-3 staff members complete this independently, then compare scores. Discrepancies reveal areas where readiness varies within the office.

---

### Infrastructure (5 items)

| # | Item | Yes | No |
|---|------|-----|----|
| 1 | Staff have individual computers or laptops with internet access | ☐ | ☐ |
| 2 | Internet speed is sufficient for web-based tools (can load websites and stream video) | ☐ | ☐ |
| 3 | Staff have access to personal or office email accounts (needed for AI tool registration) | ☐ | ☐ |
| 4 | The office has a file storage system (shared drive, Google Drive, or local server) | ☐ | ☐ |
| 5 | Staff can install software on their computers or have IT support to do so | ☐ | ☐ |

**Infrastructure subtotal: ___ / 5**

### Staff Skills (5 items)

| # | Item | Yes | No |
|---|------|-----|----|
| 6 | Most staff can type at a functional speed (can compose a 200-word email in under 10 minutes) | ☐ | ☐ |
| 7 | At least one staff member has used an AI tool (Claude, ChatGPT, Gemini, or similar) | ☐ | ☐ |
| 8 | Staff regularly use digital tools for work (email, spreadsheets, word processing) | ☐ | ☐ |
| 9 | Staff are comfortable learning new software with guidance | ☐ | ☐ |
| 10 | At least one staff member can serve as a peer trainer for new digital tools | ☐ | ☐ |

**Staff Skills subtotal: ___ / 5**

### Document Organization (5 items)

| # | Item | Yes | No |
|---|------|-----|----|
| 11 | Key reference documents (enabling laws, SOPs, plans) exist in digital format | ☐ | ☐ |
| 12 | Documents are organized in a consistent folder structure | ☐ | ☐ |
| 13 | The office maintains soft copies of its outputs (reports, briefers, memos) | ☐ | ☐ |
| 14 | Historical documents from the past 2+ years are retrievable | ☐ | ☐ |
| 15 | Document naming follows a consistent convention (or could be standardized quickly) | ☐ | ☐ |

**Document Organization subtotal: ___ / 5**

### Policy Framework (5 items)

| # | Item | Yes | No |
|---|------|-----|----|
| 16 | The office has a data privacy awareness (even informal) — staff know not to share confidential data publicly | ☐ | ☐ |
| 17 | The office has documented standard operating procedures for major functions | ☐ | ☐ |
| 18 | There is a quality review process for official documents (at least one reviewer before release) | ☐ | ☐ |
| 19 | The office has or can quickly draft guidelines for new technology use | ☐ | ☐ |
| 20 | Records management policies exist (even basic rules for filing and retention) | ☐ | ☐ |

**Policy Framework subtotal: ___ / 5**

### Leadership Support (5 items)

| # | Item | Yes | No |
|---|------|-----|----|
| 21 | The office head is aware of AI tools and their potential for government work | ☐ | ☐ |
| 22 | The office head would support staff experimenting with AI for work tasks | ☐ | ☐ |
| 23 | Budget exists (or can be reallocated) for tool subscriptions (even small amounts) | ☐ | ☐ |
| 24 | The office culture allows trying new approaches (not strictly "this is how we've always done it") | ☐ | ☐ |
| 25 | A champion — someone willing to lead the AI adoption effort — can be identified | ☐ | ☐ |

**Leadership Support subtotal: ___ / 5**

---

### Scoring Rubric

| Score | Readiness Level | What It Means | Next Step |
|-------|----------------|---------------|-----------|
| **20-25** | Ready | Your office has the foundation. Begin with Chapter 13's 90-day plan. | Start Appendix H immediately |
| **15-19** | Almost Ready | Most elements are in place. Address the gaps first. | Fix 0-score categories, then start Chapter 13 |
| **10-14** | Needs Work | Several foundations are missing. Focus on prerequisites. | Address Infrastructure and Document Organization first |
| **Below 10** | Start with Foundations | The office needs basic digital readiness before AI adoption. | Begin with Chapter 2 for literacy, build infrastructure |

---

## Appendix D — Sample AI Policy for a BARMM Office

> *This is a model policy template. Replace all bracketed items with your office's specifics. Adapt sections to your context. Have your legal officer review before issuance.*

---

**[OFFICE NAME]**

**Administrative Order No. [NUMBER]**
**Series of [YEAR]**

**SUBJECT: POLICY ON THE USE OF ARTIFICIAL INTELLIGENCE TOOLS IN [OFFICE NAME] OPERATIONS**

---

**WHEREAS**, the Bangsamoro government is committed to improving public service delivery and administrative efficiency through responsible adoption of technology;

**WHEREAS**, artificial intelligence tools have demonstrated the capacity to assist government staff in research, drafting, analysis, and reporting functions;

**WHEREAS**, the responsible use of such tools requires clear guidelines to protect data privacy, ensure output quality, and maintain public trust;

**WHEREAS**, Republic Act No. 10173 (Data Privacy Act of 2012) and its Implementing Rules and Regulations establish requirements for the protection of personal and sensitive information;

**NOW, THEREFORE**, the following policy is hereby adopted:

---

### Section 1. Purpose

This policy establishes guidelines for the responsible use of artificial intelligence (AI) tools by personnel of [OFFICE NAME] in the performance of their official functions.

### Section 2. Scope

This policy applies to all personnel of [OFFICE NAME], including regular, contractual, casual, and job order employees who use AI tools for work-related tasks, whether on office equipment or personal devices.

### Section 3. Definition of Terms

- **AI Tool** — Any software application that uses artificial intelligence to generate, analyze, summarize, translate, or otherwise process text, data, or images. This includes but is not limited to Claude, ChatGPT, Gemini, NotebookLM, and similar platforms.
- **AI-Assisted Output** — Any document, analysis, draft, or report produced in whole or in part with the assistance of an AI tool.
- **Confidential Information** — Information classified as confidential, restricted, or sensitive under existing BARMM information classification guidelines, including personal data of individuals, pre-decisional policy documents, and security-related information.

### Section 4. Authorized Uses

Personnel may use AI tools for the following purposes:
1. Drafting correspondence, reports, briefers, and other documents
2. Summarizing and analyzing publicly available laws, policies, and reports
3. Conducting research and literature reviews
4. Preparing presentation materials and talking points
5. Translating documents between English, Filipino, and Arabic
6. Organizing and structuring data for analysis
7. Generating templates for routine office processes
8. Proofreading and improving drafted documents

### Section 5. Prohibited Uses

Personnel shall NOT use AI tools for the following:
1. Uploading confidential, classified, or sensitive government information to cloud-based AI tools
2. Uploading personal data of citizens, employees, or officials to AI tools without data privacy compliance
3. Submitting AI-generated outputs as final documents without human review and approval
4. Making official decisions or commitments based solely on AI recommendations
5. Using AI tools for personal, commercial, or political purposes on government time or equipment
6. Generating false information, fake documents, or misleading content
7. Bypassing established review and approval workflows

### Section 6. Quality Assurance Requirements

All AI-assisted outputs shall undergo the following quality assurance process before submission or publication:
1. **Factual verification** — Every factual claim, statistic, legal reference, and name in the output must be verified against primary sources
2. **Legal review** — Any output citing laws, BAAs, or regulations must have citations verified against the actual legal text
3. **Supervisor review** — AI-assisted outputs must pass through the standard document review chain before release
4. **Bias check** — Outputs must be reviewed for bias, culturally inappropriate content, and assumptions that do not apply to the Bangsamoro context

### Section 7. Data Privacy Compliance

1. Personnel shall classify information before inputting it into any AI tool using the office's information classification guide.
2. Personal data as defined under RA 10173 shall not be uploaded to AI tools unless the tool provides enterprise-grade data protection and a processing agreement is in place.
3. When in doubt about whether information can be shared with an AI tool, personnel shall consult the office Data Protection Officer or immediate supervisor.

### Section 8. Attribution and Disclosure

1. AI-assisted outputs shall be disclosed as such when submitted for review. A simple notation is sufficient: "This draft was prepared with AI assistance and has been reviewed for accuracy."
2. Final published documents do not require AI disclosure unless the office head determines it appropriate.
3. Personnel shall not represent AI-generated work as entirely their own in contexts where authorship matters (e.g., academic papers, official certifications, sworn statements).

### Section 9. Training Requirements

1. All personnel who use AI tools shall complete the office AI literacy orientation within [30/60/90] days of this policy's effectivity.
2. The orientation shall cover: basic prompting, quality assurance procedures, data privacy guidelines, and prohibited uses.
3. The [designated unit/AI Champion] shall conduct refresher training at least once annually.
4. Completion of AI training shall be documented and included in individual training records.

### Section 10. Review and Amendment

1. This policy shall be reviewed [annually / semi-annually] by [designated unit/officer].
2. Amendments may be proposed by any personnel and shall be reviewed by [designated body].
3. Significant changes in AI technology or government policy shall trigger an off-cycle review.

### Section 11. Effectivity

This Administrative Order shall take effect immediately upon signing.

Issued this ___ day of __________, [YEAR], at [LOCATION].

---

**[NAME OF AUTHORIZING OFFICIAL]**
[Title]

---

## Appendix E — AI-Assisted CSW: ADDRESS IT with AI at Every Step

The ADDRESS IT methodology is BARMM's seven-step framework for Complete Staff Work.[^1] This appendix maps AI assistance to each step, showing what AI can do, what it cannot, and how to prompt it. For the full ADDRESS IT methodology, refer to the *Complete Staff Work Guidebook for BARMM*.[^2]

---

### E.1 Analyze Context with AI

**The step:** Understand the situation, identify the trigger, gather background information, determine who is involved and affected.

**What AI can do:**
- Summarize background documents (prior memos, committee reports, audit findings)
- Identify stakeholders from legal mandates and organizational charts
- Map the regulatory landscape (which laws, policies, and plans are relevant)
- Generate a structured situational analysis from raw notes

**What AI cannot do:**
- Assess the political sensitivity of the situation
- Judge the urgency from an organizational perspective
- Know internal office dynamics, informal power structures, or unwritten priorities
- Replace conversation with the supervisor who assigned the task

**Sample prompt:**

```
I am preparing a CSW document. Help me analyze the context.

Trigger: [WHAT INITIATED THIS TASK — directive, inquiry, problem, opportunity]
Background: [PASTE AVAILABLE INFORMATION — memos, reports, data]
Decision-maker: [WHO WILL ACT ON THIS CSW]

Provide:
1. Situation summary (3-5 sentences)
2. Key stakeholders and their interests
3. Relevant laws and policies (BOL, BAAs, national laws)
4. Information gaps — what do I still need to find out?
5. Suggested scope boundaries — what should this CSW cover and NOT cover?
```

**Quality check:** Does the AI's situational summary match your understanding? Are the stakeholders complete? Did you add the stakeholders and dynamics the AI would not know about?

---

### E.2 Define/Deliberate the Problem with AI

**The step:** Frame the problem precisely. Distinguish the root cause from symptoms. Define what a successful resolution looks like.

**What AI can do:**
- Help frame a problem statement from scattered symptoms
- Apply problem analysis frameworks (5 Whys, fishbone diagram, problem tree)
- Identify whether the problem is technical, political, legal, or operational
- Draft clear problem statements in CSW-appropriate language

**What AI cannot do:**
- Determine the "real" problem when political considerations obscure it
- Replace the judgment call about which framing the decision-maker will accept
- Know whether this problem has been raised and rejected before

**Sample prompt:**

```
Help me define the problem for a CSW document.

Symptoms observed: [LIST WHAT IS GOING WRONG]
Context: [BRIEF BACKGROUND FROM E.1]
Decision-maker: [WHO]

Apply the 5 Whys technique to move from symptoms to root causes.
Then draft a problem statement in this format:
"The [specific problem] is causing [specific harm] to [specific stakeholders], resulting in [measurable impact]."

Provide 2-3 alternative problem framings so I can choose the most accurate one.
```

**Quality check:** Does the problem statement describe a problem the decision-maker can actually act on? Is it specific enough to guide the analysis?

---

### E.3 Research with AI

**The step:** Gather evidence, legal references, precedents, data, and expert perspectives relevant to the problem.

**What AI can do:**
- Search and summarize legal provisions (BOL, BAAs, national laws)
- Compile comparative data from uploaded documents
- Identify precedents — how was a similar problem handled before?
- Organize research findings by theme or relevance
- Generate annotated bibliographies from source documents

**What AI cannot do:**
- Access classified or internal-only government records
- Verify whether a cited precedent was actually followed or abandoned
- Replace field research, stakeholder interviews, or primary data collection
- Guarantee that its legal citations are complete and current

**Sample prompt:**

```
I am researching the following problem for a CSW document:
Problem: [PASTE PROBLEM STATEMENT FROM E.2]

Research the following:
1. Legal framework: What provisions of the BOL, BAAs, and national laws
   address this issue? Quote specific sections.
2. Policy context: What existing policies, plans, or directives relate
   to this issue?
3. Precedent: Has a similar issue been addressed by any BARMM office
   or comparable government entity?
4. Data: What data points or statistics are relevant?
5. Expert perspectives: What do published sources say about best
   practices for this type of issue?

For each finding, note the source and confidence level (confirmed from
primary source / inferred / needs verification).
```

**Quality check:** Every legal citation must be verified against the actual legal text. Every data point must be traced to its source. Mark anything unverified.

---

### E.4 Explore Options with AI

**The step:** Generate and analyze at least three viable options for resolving the problem.

**What AI can do:**
- Generate multiple options based on research findings
- Apply consistent evaluation criteria across all options
- Draft pros-and-cons analysis for each option
- Estimate implementation complexity and resource requirements
- Identify risks associated with each option

**What AI cannot do:**
- Know which option the decision-maker is inclined to accept
- Assess political feasibility with the accuracy of a human insider
- Guarantee cost estimates without actual budget data
- Replace stakeholder consultation on option preferences

**Sample prompt:**

```
Based on the following problem and research:
Problem: [PASTE FROM E.2]
Key research findings: [PASTE FROM E.3]

Generate 3-4 viable options to address this problem. For each option:
1. Description (2-3 sentences)
2. Legal basis (what authorizes this approach)
3. Pros (3-5 points)
4. Cons (3-5 points)
5. Resource requirements (budget, personnel, time)
6. Implementation timeline
7. Risk assessment (what could go wrong)
8. Alignment with BDP 2023-2028 goals

Then provide a comparison matrix and indicate which option appears
strongest based on the analysis. Note: the final recommendation is
mine to make, not yours.
```

**Quality check:** Are the options genuinely different, or are they variations of the same approach? Is there a "do nothing" or "status quo" option for comparison? Are the pros and cons honest?

---

### E.5 Submit with AI-Assisted Quality Review

**The step:** Compile the CSW document, run quality checks, and submit through the proper channel.

**What AI can do:**
- Format the CSW document according to office templates
- Check internal consistency (does the recommendation match the analysis?)
- Verify that all sections are complete
- Proofread for grammar, clarity, and conciseness
- Generate an executive summary from the full document

**What AI cannot do:**
- Certify that the CSW is ready for submission (only you can do that)
- Sign the document or take responsibility for its contents
- Know whether the document meets the specific expectations of the decision-maker
- Replace the routing and approval process

**Sample prompt:**

```
Review this CSW document for completeness and quality:

[PASTE YOUR COMPLETE CSW DRAFT]

Check for:
1. Completeness: Are all required sections present?
2. Internal consistency: Does the recommendation flow logically from
   the problem, research, and options analysis?
3. Factual accuracy: Flag any claims that lack citations or evidence
4. Clarity: Is the language clear and concise? Flag jargon or vague
   statements
5. Format: Does it follow proper CSW format?
6. Action clarity: Is the recommended action specific enough for the
   decision-maker to approve/disapprove immediately?

Provide specific, actionable feedback organized by section.
```

**Quality check:** Address every issue the AI flags. Then have a human colleague review the document independently.

---

### E.6 Sustain Implementation with AI Monitoring

**The step:** After the decision-maker approves, track implementation of the approved recommendation.

**What AI can do:**
- Generate an implementation tracking template from the approved CSW
- Draft implementation directives and assignment memos
- Create monitoring checklists from action items
- Summarize progress reports into status updates
- Flag delays or deviations from the implementation timeline

**What AI cannot do:**
- Monitor actual implementation (that requires physical oversight)
- Hold people accountable for their assigned tasks
- Detect problems not reported in documents
- Replace regular check-ins with implementing units

**Sample prompt:**

```
The following CSW recommendation has been approved:
[PASTE APPROVED RECOMMENDATION AND ACTION ITEMS]

Generate:
1. Implementation plan with tasks, responsible persons, and deadlines
2. Monitoring checklist (what to verify at each milestone)
3. Status report template for weekly/monthly updates
4. Risk register for implementation risks
5. Escalation protocol — when and how to escalate if implementation
   stalls
```

**Quality check:** Does the implementation plan cover every action item in the approved recommendation? Are deadlines realistic?

---

### E.7 Iterate and Improve with AI Feedback Loops

**The step:** Evaluate outcomes, capture lessons learned, and improve the process for next time.

**What AI can do:**
- Analyze implementation data against expected outcomes
- Draft lessons-learned reports from post-implementation reviews
- Identify process improvements for future CSW cycles
- Compare current CSW quality against previous iterations
- Generate recommendations for process standardization

**What AI cannot do:**
- Assess whether the decision-maker is satisfied with the outcome
- Know the informal feedback circulating in the office
- Replace the honest self-assessment that makes iteration valuable
- Determine whether the problem was truly resolved or merely addressed

**Sample prompt:**

```
The following CSW has been implemented. Evaluate the outcome:

Original problem: [PASTE]
Approved recommendation: [PASTE]
Implementation results: [PASTE ACTUAL OUTCOMES AND DATA]

Analyze:
1. Outcome vs. expectation: Was the problem resolved? Partially? Not at all?
2. Process efficiency: How long did the CSW cycle take? Where were bottlenecks?
3. Quality assessment: Were there factual errors, missed stakeholders, or gaps in the analysis?
4. Lessons learned: What would you do differently next time?
5. Recommendations: Specific process improvements for the next CSW on a similar issue
```

**Quality check:** Be honest in your assessment. The value of iteration is proportional to the honesty of the evaluation.

---

## Appendix F — AI-Assisted Legislative Briefer: 13-Section Template

This template maps the 13 sections of the CSW legislative briefer format to AI assistance. Use it alongside Chapter 7 and the *Bill Drafting Guidebook*.[^3]

| # | Section | AI Contribution | Sample Prompt Starter | Human Review Focus |
|---|---------|----------------|----------------------|-------------------|
| 1 | **Measure Description** | **High** — AI can summarize the bill's provisions, identify its scope, and describe key features | "Summarize [BILL NUMBER] in 300 words, covering: purpose, scope, key provisions, and implementing agency." | Verify the summary matches the actual bill text. Check for omissions. |
| 2 | **Background and Context** | **High** — AI can compile legislative history, related laws, and policy context | "Provide the legislative background for [TOPIC]: prior bills, existing BAAs, relevant national laws, and policy drivers." | Verify legislative history is complete. Add internal context the AI lacks. |
| 3 | **Legal Basis and Constitutional Framework** | **Medium** — AI can identify BOL provisions and national laws but cannot guarantee completeness | "Identify all BOL provisions, BAAs, and national laws that provide the legal basis for [BILL NUMBER]." | Verify every citation against the actual legal text. Check for missed provisions. |
| 4 | **Comparative Legislation** | **High** — AI excels at comparing provisions across jurisdictions | "Compare [BILL NUMBER]'s approach to [TOPIC] with: (a) the national law, (b) ARMM precedent, (c) 2-3 international models." | Verify foreign law citations. Assess whether comparisons are relevant to BARMM context. |
| 5 | **Stakeholder Impact Assessment** | **Medium** — AI can identify stakeholder categories but not actual stakeholder positions | "Identify all stakeholders affected by [BILL NUMBER] and analyze the likely impact on each group." | Add stakeholders the AI missed. Verify impact claims with actual stakeholder input. |
| 6 | **Fiscal Impact Analysis** | **Low** — AI can structure the analysis but cannot generate reliable cost estimates without data | "Create a fiscal impact analysis framework for [BILL NUMBER]: cost categories, revenue implications, and funding source options." | All numbers must come from MFBM or verified sources. AI structures; humans populate. |
| 7 | **Shari'ah and Islamic Values Assessment** | **Low** — AI can identify relevant principles but cannot make Shari'ah rulings | "Identify Islamic principles (Amanah, Adl, Maslahah, Shura) relevant to [BILL NUMBER] and note potential Shari'ah considerations." | Must be reviewed by a qualified Shari'ah scholar or the Bangsamoro Darul Ifta'. |
| 8 | **Gender and Inclusivity Analysis** | **Medium** — AI can apply standard GAD frameworks but may miss BARMM-specific gender dynamics | "Apply a Gender and Development lens to [BILL NUMBER]: differential impact on women, men, youth, elderly, PWDs, and IPs." | Verify against actual demographic data. Consult with the Gender Office. |
| 9 | **Implementation Feasibility** | **Medium** — AI can identify implementation requirements but not institutional capacity | "Assess the implementation feasibility of [BILL NUMBER]: institutional requirements, timeline, capacity needs, and potential bottlenecks." | Verify institutional capacity claims with the implementing agency. |
| 10 | **Interpellation Strategy** | **High** — AI excels at generating question trees and anticipating responses | "Generate 10 interpellation questions for [BILL NUMBER], targeting: provisions, fiscal impact, implementation, and legal basis." | Ensure questions reflect the MP's actual concerns and priorities. |
| 11 | **Proposed Amendments** | **Medium** — AI can draft amendment language but cannot assess political feasibility | "Draft 3 proposed amendments to [BILL NUMBER] addressing: [SPECIFIC CONCERNS]. Include amendment text and justification." | Verify amendment text is internally consistent. Assess political feasibility. |
| 12 | **Policy Recommendation** | **Low** — AI can present options but the recommendation must be the analyst's own judgment | "Present 3 policy options for [BILL NUMBER]: approve as filed, approve with amendments, request further study. Analyze each." | The recommendation is yours. AI presents; you decide. |
| 13 | **Parliamentary Speeches** | **High** — AI can draft speeches from the analysis, but voice and conviction must be the MP's own | "Draft a 3-minute manifestation for [MP NAME] on [BILL NUMBER], [supporting/opposing] the measure, based on the following key points." | The MP must review and own every word. Edit for the MP's speaking style. |

---

## Appendix G — AI-Assisted Budget Briefer: BB-Coded Template

This template maps the BB-coded sections of the CSW budget briefer to AI prompts. Use alongside Chapter 6 and the *Bill Drafting Guidebook*, Chapter 9.[^4]

| Code | Section | AI Prompt | Human Review Focus |
|------|---------|-----------|-------------------|
| **BB01** | Budget Overview | "Summarize [MINISTRY]'s FY [YEAR] budget proposal: total amount, change from prior year, allocation by expense class (PS/MOOE/CO), and top 5 programs by allocation." | Verify all figures against the official budget document. |
| **BB02** | Mandate and Organizational Profile | "Describe [MINISTRY]'s mandate per [ENABLING BAA], organizational structure, and staffing complement. Note filled vs. vacant positions." | Verify enabling BAA citation. Confirm staffing data with HR. |
| **BB03** | Historical Budget Trend | "Analyze [MINISTRY]'s budget trends over the past 3 fiscal years: total allocation, obligation rate, disbursement rate. Identify patterns." | Verify historical figures from official GAA documents. |
| **BB04** | Variance Analysis | "Compare [MINISTRY]'s FY [YEAR] proposal to FY [PRIOR YEAR] GAA. Flag all items with >15% change and explain likely reasons." | Recalculate top 5 variance items manually. |
| **BB05** | BDP Alignment Assessment | "Assess how [MINISTRY]'s proposed programs align with BDP 2023-2028 goals and strategies. Identify funded vs. unfunded BDP targets." | Verify BDP goal numbers and strategy text. |
| **BB06** | KPI Review | "Review [MINISTRY]'s proposed KPIs for FY [YEAR]. Are they SMART? Do they measure outcomes or just outputs? Suggest improvements." | Confirm KPIs are achievable with available data collection capacity. |
| **BB07** | Personnel Services Analysis | "Analyze the PS component: rate of filled positions, average salary grade, contractual vs. regular ratio, training budget adequacy." | Verify PS data against DBM-approved plantilla. |
| **BB08** | MOOE Adequacy | "Assess whether MOOE allocation is sufficient for [MINISTRY]'s operational requirements. Flag underbudgeted items." | Confirm with actual operational requirements from the ministry. |
| **BB09** | Capital Outlay Review | "Review capital outlay proposals: project descriptions, implementation readiness, alignment with infrastructure plan, procurement timeline." | Verify project readiness certificates and procurement schedules. |
| **BB10** | Revenue Analysis | "Analyze [MINISTRY]'s revenue targets (if applicable): collection performance, year-over-year trend, and realism of FY [YEAR] targets." | Verify collection data against BIR/treasury records. |
| **BB11** | COA Findings Impact | "Summarize COA audit findings for [MINISTRY] from the past 2 years. Assess whether the proposed budget addresses systemic issues flagged by auditors." | Cross-reference with actual COA Annual Audit Reports. |
| **BB12** | Scrutiny Questions | "Generate 10 scrutiny questions for [MINISTRY]'s FY [YEAR] budget, targeting: utilization, variances, KPIs, personnel, and capital outlay." | Tailor questions to specific committee concerns. |
| **BB13** | Recommendation | "Based on the analysis above, present 3 options: approve as proposed, approve with conditions, or require revision. Justify each." | The recommendation is the analyst's judgment. AI informs; the analyst decides. |

---

## Appendix H — 90-Day AI Adoption Plan Template

Adapt this plan for your office. Replace bracketed items. See Chapter 13, Section 13.5 for detailed guidance on each phase.

### Week-by-Week Timeline

| Week | Phase | Activity | Responsible | Deliverable | Success Indicator |
|------|-------|----------|-------------|-------------|-------------------|
| 1-2 | **Foundation** | Complete AI Readiness Assessment (Appendix C); identify AI Champion; secure leadership buy-in | Office Head, AI Champion | Completed assessment scorecard; AI Champion designation memo | Assessment completed, champion identified |
| 3-4 | **Foundation** | Set up AI tools (Appendix B); create initial knowledge base; collect reference documents in digital format | AI Champion, IT support | Tool accounts created; initial vault/notebook with 10+ reference documents | All team members have tool access |
| 5-6 | **Quick Wins** | Conduct first AI training session (half-day); each staff member completes 3 practice tasks from Appendix A | AI Champion | Training attendance sheet; 3 completed practice outputs per person | 80% of staff complete practice tasks |
| 7-8 | **Quick Wins** | Apply AI to one real routine task per staff member; begin shared prompt library | All staff, AI Champion | Prompt library document with 10+ tested prompts; one AI-assisted output per person | Prompts documented and shared |
| 9-10 | **Integration** | Draft office AI policy (Appendix D); begin team-level AI workflow for one major process | AI Champion, Office Head | Draft AI policy; one AI-integrated SOP | Policy drafted, one process integrated |
| 11-12 | **Integration** | Conduct second training session focusing on the office's specific governance function; expand knowledge base | AI Champion | Updated training materials; knowledge base with 25+ documents | Staff applying AI to function-specific tasks |
| 12-13 | **Consolidation** | Finalize and issue AI policy; document lessons learned; set 90-day review date; report results to leadership | AI Champion, Office Head | Issued AI policy; lessons learned report; 90-day review memo | Policy issued, measurable improvement documented |

### Roles and Responsibilities

| Role | Person | Key Responsibilities |
|------|--------|---------------------|
| **Executive Sponsor** | [Office Head Name/Title] | Approve the plan, issue AI policy, allocate budget, remove institutional barriers |
| **AI Champion** | [Name/Title] | Lead implementation, conduct training, maintain knowledge base, troubleshoot issues, report progress |
| **IT Support** | [Name/Title or "IT Officer"] | Set up tool access, resolve technical issues, advise on data security |
| **Team Members** | All staff | Participate in training, practice AI tools, contribute to prompt library, report challenges |

### Milestone Checklist

- [ ] Week 2: AI Readiness Assessment completed and scored
- [ ] Week 2: AI Champion formally designated
- [ ] Week 4: All staff have AI tool accounts
- [ ] Week 4: Knowledge base created with 10+ reference documents
- [ ] Week 6: First training session completed
- [ ] Week 8: Shared prompt library has 10+ prompts
- [ ] Week 10: Draft AI policy completed
- [ ] Week 10: One major process has an AI-integrated SOP
- [ ] Week 12: Second training session completed
- [ ] Week 13: AI policy formally issued
- [ ] Week 13: Lessons learned documented
- [ ] Week 13: 90-day review date scheduled

---

## Appendix I — AI Training Workshop Design (3-Day Program)

This workshop design is ready to adapt for any BARMM office. Adjust session topics to match your office's governance function. See Chapter 14 for the pedagogical framework behind this design.

---

### I.1 Day 1: AI Literacy and First Prompts

| Session | Time | Duration | Objective | Activity | Materials |
|---------|------|----------|-----------|----------|-----------|
| **1.1 Opening and Context** | 8:30-9:30 | 60 min | Understand why AI matters for BARMM governance | Welcome; overview of AI in government worldwide; BARMM-specific opportunities and constraints (from Ch. 1); pre-training assessment quiz | Slide deck; pre-assessment form; printed quiz |
| **1.2 AI Foundations** | 9:45-11:15 | 90 min | Understand what AI is and how it works, in plain language | Lecture-discussion on how LLMs read, write, and reason (from Ch. 2); live demo of Claude and NotebookLM; myth-busting exercise (8 misconceptions from Ch. 2) | Projector; live internet; prepared demo prompts; misconceptions handout |
| **1.3 Your First Government Prompt** | 11:30-12:30 | 60 min | Write and run a first AI prompt for a government task | Guided practice: each participant writes a prompt from Appendix A (choose one matching their function); run it; review the output; identify one thing to fix | Laptops/tablets with internet; printed Appendix A excerpts; worksheet |
| **1.4 The Four-Step Workflow** | 1:30-3:00 | 90 min | Apply the Prepare-Prompt-Review-Refine workflow to a real task | Workshop: participants bring a real document they recently worked on; re-do it using AI with the four-step workflow from Ch. 3; compare AI-assisted vs. original; group discussion on quality differences | Participants' real documents; AI tool access; comparison worksheet |

---

### I.2 Day 2: AI for Your Governance Function

| Session | Time | Duration | Objective | Activity | Materials |
|---------|------|----------|-----------|----------|-----------|
| **2.1 Building Context** | 8:30-9:30 | 60 min | Learn to prepare documents for AI analysis | Hands-on: participants digitize 2-3 key reference documents; upload to NotebookLM notebook; practice asking questions about their own documents | Laptops; scanner/phone camera; Google accounts; selected office documents |
| **2.2 Function-Specific AI Application** | 9:45-11:45 | 120 min | Apply AI to the participant's specific governance function | Breakout groups by function (planning, budget, legislative, admin, M&E); each group works through 3-4 prompts from the relevant Appendix A subsection using real office data; facilitator rotates between groups | Function-specific prompt cards; real (non-confidential) office data; breakout space |
| **2.3 Quality Assurance Workshop** | 1:00-2:30 | 90 min | Learn to verify AI outputs systematically | Exercise: facilitator provides 3 AI-generated government documents with planted errors (wrong BAA numbers, incorrect budget figures, fabricated statistics); participants must find and correct all errors; debrief on verification techniques | Pre-prepared documents with errors; answer key; verification checklist from Ch. 3 |
| **2.4 Knowledge Base Setup** | 2:45-4:00 | 75 min | Begin building a team knowledge base | Workshop: participants set up Obsidian vault (Appendix B.3) or NotebookLM notebook organized for their team; add 5-10 reference documents; practice linking notes; discuss maintenance responsibility | Obsidian installed or NotebookLM access; vault structure template; team reference documents |

---

### I.3 Day 3: Team Workflow Integration and Policy Drafting

| Session | Time | Duration | Objective | Activity | Materials |
|---------|------|----------|-----------|----------|-----------|
| **3.1 Team Workflow Design** | 8:30-10:00 | 90 min | Design an AI-integrated workflow for one team process | Workshop: each team selects one recurring task (e.g., weekly report, committee briefer, budget monitoring); maps the current process; identifies where AI enters; designs the AI-augmented version with human checkpoints; presents to the group | Process mapping template; current SOP documents; workflow design worksheet |
| **3.2 AI Policy Workshop** | 10:15-11:45 | 90 min | Draft an office AI policy | Using Appendix D as a template, teams draft their office-specific AI policy; discuss: authorized uses, prohibited uses, quality assurance, and training; facilitator guides discussion on contentious items | Printed Appendix D; policy drafting worksheet; projector for group editing |
| **3.3 90-Day Action Planning** | 1:00-2:30 | 90 min | Create a concrete adoption plan | Using Appendix H, each team completes their 90-Day AI Adoption Plan: assign roles, set milestones, identify quick wins for Week 1; present plans to the group for peer feedback | Printed Appendix H; planning worksheet; team roster |
| **3.4 Commitment and Closing** | 2:45-4:00 | 75 min | Consolidate learning and commit to action | Post-training assessment; comparison with pre-assessment scores; each participant writes a personal AI commitment card (one thing they will do in the first week); team AI champion identified; closing ceremony | Post-assessment form; commitment cards; certificate templates |

---

## Appendix J — BARMM Legal Framework Quick Reference for AI Users

This table provides a quick reference to the laws most relevant when using AI in government work. It does not replace reading the actual legal text.

| Law | Key Provision | AI Relevance |
|-----|--------------|--------------|
| **1987 Constitution, Art. III (Bill of Rights)** | Sec. 3: Privacy of communication and correspondence shall be inviolable. Sec. 7: Right of the people to information on matters of public concern. | AI tools must not compromise citizens' privacy. AI-generated analysis of government data should support — not undermine — the public's right to information. |
| **BOL (RA 11054), Art. IX (Basic Rights)** | Sec. 1-6: Right to life, liberty, equal protection, freedom of expression, privacy, and due process within BARMM. | AI-assisted government decisions must respect these rights. AI outputs used in policy-making must not introduce bias that violates equal protection. |
| **BOL (RA 11054), Art. V (Powers of Government)** | Sec. 1-3: Enumerated powers, reserved powers, and concurrent powers of the Bangsamoro Government. | AI tools assist — they do not exercise — governmental powers. Legislative and executive decisions remain with elected and appointed officials. |
| **BAA 13 (Bangsamoro Administrative Code)** | Establishes the administrative structure, procedures, and standards for BARMM offices. | AI-assisted outputs must comply with administrative procedures. Document formats, routing, and approval processes defined by the Administrative Code still apply. |
| **BAA 17 (Bangsamoro Civil Service Act)** | Establishes merit-based civil service; defines employee rights, obligations, and performance standards. | AI proficiency can be integrated into competency frameworks. AI does not replace civil servants; it augments their work. Performance evaluation remains human-led. |
| **BAA 84 (Bangsamoro Budget System Act)** | Governs budget preparation, authorization, execution, and accountability. Defines budget procedures, fiscal discipline requirements. | AI assists in budget analysis, variance detection, and reporting. Budget decisions remain with authorized officials. AI outputs must align with BAA 84's procedural requirements. |
| **RA 10173 (Data Privacy Act of 2012)** | Protects personal information in government and private sector processing. Establishes rights of data subjects and obligations of data controllers/processors. | Most directly relevant law for AI use. Personal data must not be uploaded to AI tools without compliance. AI-generated profiles or analyses involving personal data require DPA compliance. |
| **RA 9184 (Government Procurement Reform Act)** | Governs procurement of goods, services, and infrastructure. Requires competitive bidding, transparency, and accountability. | AI tool subscriptions above threshold amounts must follow RA 9184 procedures. AI cannot bypass procurement requirements for government IT spending. |

**Note:** This table reflects provisions as of March 2026. Laws may be amended. Always verify against current legal text.

---

## Appendix K — The Author's AI Toolkit

I use AI every day in my Bangsamoro governance work. Not as a curiosity. Not as an experiment. As infrastructure. This appendix describes what I use and how, in case it helps you build your own toolkit.

**Claude Code** is my primary AI tool. It runs in a terminal and has access to my local files, which means it can read a BAA, cross-reference it against the BOL, draft a legislative briefer, and save the output to my knowledge base — all in a single workflow. Over the past year, I have built 129 custom skills (specialized instruction sets) that automate recurring governance tasks:

- **/csw** generates Complete Staff Work documents using the ADDRESS IT methodology, producing analysis-ready briefers from raw inputs.
- **/bill-drafter** produces bill text, explanatory notes, and comparative matrices following the format prescribed in the *Bill Drafting Guidebook for the Bangsamoro Parliament*.
- **/legislative-briefer** generates the 13-section legislative analysis briefer mapped in Appendix F.
- **/policy-recommendation** drafts policy memos using the Bardach Eightfold Path methodology.
- **/speech-writer** produces speeches and manifestations for parliamentary proceedings, in Tagalog, English, or Taglish, with Islamic greeting protocols.
- **/bangsamoro** serves as a domain expert — loaded with verified data on BARMM governance structure, officials, the 89 enacted BAAs, BDP targets, and the BOL. Every content skill invokes it first to prevent factual errors.
- **/fact-checker** runs after every document to verify names, titles, legislation references, and claims against authoritative sources.

**NotebookLM** handles research at scale. When I need to analyze 15 committee hearing transcripts or compare provisions across a dozen related laws, I load the sources into a notebook and let Google's servers do the heavy processing. The cost is zero. The output is citation-grounded — every claim traces back to a specific passage in a specific source. I use it for the research phase of any large document, then bring the findings into Claude Code for drafting.

**Obsidian** is my knowledge base. Every law I transcribe, every briefer I draft, every research finding I produce, every meeting note I take — it goes into an Obsidian vault with bidirectional links between notes. When I write a bill summary, I link it to the relevant BAA, the committee that reviewed it, the ministry it affects, and the BDP goal it supports. Over time, the vault becomes a map of Bangsamoro governance that no single document could contain.

**The workflow in practice:** When the Parliament prepares to deliberate a bill, I load the bill text and all related documents into NotebookLM for research. I invoke `/bangsamoro` in Claude Code to load governance context. I run `/legislative-briefer` to generate the 13-section analysis. I invoke `/fact-checker` to verify every citation. I save the output to my Obsidian vault, linked to every relevant note. The result: a comprehensive, fact-checked legislative briefer in hours instead of days.

This toolkit did not appear overnight. It accumulated over months of daily use, iteration, and correction. The skills improved because I used them, found errors, fixed them, and used them again. The vault grew because I fed it consistently. The workflow sharpened because I paid attention to where it broke and redesigned those points.

You do not need 129 skills to start. You need one task, one tool, and the discipline to verify every output. The rest builds from there.

---

## Appendix L — Cross-Reference Index to Other BARMM Guidebooks

This guidebook is part of a family of governance publications produced for BARMM. Each guidebook covers a different domain. This index shows where they connect.

| Guidebook | Relevant Chapters in This Guidebook | Key Connection |
|-----------|-------------------------------------|----------------|
| **Bill Drafting Guidebook for the Bangsamoro Parliament** | Ch. 7 (Legislative Work), Ch. 11 (Legislation and Codification), Appendix F, Appendix G | AI techniques for every stage of the legislative process documented in the Bill Drafting Guidebook. Appendix F maps the 13-section briefer format. Appendix G maps the BB-coded budget briefer. |
| **Complete Staff Work (CSW) Guidebook for BARMM** | Ch. 3 (AI-Augmented Workflow), Appendix E | Appendix E maps AI assistance to every step of the ADDRESS IT methodology. Chapter 3's four-step workflow integrates directly with CSW procedures. |
| **Manual of Operations (MOP) Formulation Guidebook** | Ch. 8 (Implementation), Ch. 13 (Implementation Roadmap) | AI-integrated SOPs from Chapter 8 feed into MOP documentation. Chapter 13's adoption plan produces outputs that should be captured in the office MOP. |
| **Supervision and Supervisory Development Guidebook** | Ch. 14 (Training and Capacity), Ch. 13 (Change Management) | Supervisors play a defined role in AI adoption (Ch. 14, Sec. 14.3). The change management framework in Ch. 13 maps resistance patterns that supervisors must address. |
| **Strategic Planning Guidebook** | Ch. 5 (Strategic Planning), Ch. 9 (M&E) | AI techniques for environmental scanning, needs assessment, and results framework design (Ch. 5) directly support the planning methodology in the Strategic Planning Guidebook. |
| **Speech Writing Guidebook** | Ch. 7 (Interpellation and Plenary Preparation), Ch. 8 (Government Communications) | AI-assisted speech drafting for parliamentary proceedings. Chapter 7 covers manifestations and interpellation statements. |
| **Policy Recommendations Guidebook** | Ch. 7 (Policy Recommendation Drafting), Appendix E (E.4 Explore Options) | AI techniques for options analysis and policy memo drafting align with the Bardach methodology in the Policy Recommendations Guidebook. |

---

[^1]: For the complete ADDRESS IT methodology, see: *Complete Staff Work Guidebook for BARMM*, Chapters 3-9. The methodology was developed specifically for Bangsamoro government staff work and is referenced throughout this guidebook.

[^2]: *Complete Staff Work Guidebook for BARMM*. The guidebook provides the full procedural framework; this appendix focuses exclusively on AI integration at each step.

[^3]: *Bill Drafting Guidebook for the Bangsamoro Parliament*, particularly Chapters 7-8 on legislative briefers and committee procedures.

[^4]: *Bill Drafting Guidebook for the Bangsamoro Parliament*, Chapter 9: Budget Analysis and Appropriations Review.
