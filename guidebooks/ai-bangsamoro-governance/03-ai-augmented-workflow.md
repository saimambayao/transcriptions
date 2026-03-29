# Chapter 3 — The AI-Augmented Workflow

You already know how to do government work. You analyze problems, research solutions, draft recommendations, and submit them for approval. AI does not change what you do. It changes how fast and how well you can do it.

This chapter gives you a repeatable workflow for using AI in any government task. It connects directly to the ADDRESS IT framework you may already use for Complete Staff Work.[^1] By the end of this chapter, you will know when to use AI, when not to, and how to verify everything it produces.

---

## 3.1 The Human-AI Partnership Model

The foundational principle of Complete Staff Work is this: **the decision-maker should only need to approve or disapprove**.[^2] The staff member does all the analysis, research, option development, and drafting. The principal makes the final call.

AI fits this model exactly. Think of AI as a very fast, very knowledgeable junior staff member. It drafts. You decide.

**What AI does well:**

- **Drafts documents** — first versions of briefers, memoranda, policy recommendations, and legislative text
- **Researches and synthesizes** — scans long documents, compares provisions across multiple BAAs, identifies relevant sections of the BOL
- **Organizes information** — structures raw data into tables, timelines, and formatted reports
- **Translates and paraphrases** — converts technical language into plain explanations, works across English, Filipino, and Arabic
- **Checks consistency** — finds contradictions between a draft bill and existing legislation

**What AI does not do:**

- **Make policy decisions** — AI has no authority, no mandate, and no accountability
- **Replace professional judgment** — it cannot weigh political realities, cultural sensitivities, or community relationships
- **Guarantee accuracy** — every AI output can contain errors, fabrications, or outdated information
- **Take responsibility** — your name goes on the document, not the AI's

The partnership works like this: **AI handles volume and speed. You handle judgment and accountability.** A policy analyst who uses AI can produce a legislative briefer in two hours instead of two days. But the analyst still reads every line, checks every citation, and signs the transmittal memo. The quality bar does not drop. The throughput rises.

> **The Rule of Signature**: If you would not sign a document without reading it, do not submit an AI-generated document without reviewing it. Your signature means you verified the content — regardless of who or what produced the first draft.

### Three Levels of AI Partnership

The partnership operates differently depending on the complexity of the task:

**Level 1 — AI as Drafter.** You assign a well-defined task with a clear template. The AI produces a first draft. You review and finalize. This applies to routine correspondence, meeting summaries, and standard-format documents. Most government staff will start here.

**Level 2 — AI as Research Assistant.** You assign an open-ended research task. The AI scans multiple documents, identifies relevant provisions, and synthesizes findings. You evaluate the research, add your professional knowledge, and shape the conclusions. This applies to legislative briefers, policy analyses, and comparative studies.

**Level 3 — AI as Thinking Partner.** You discuss a complex problem with the AI, testing different framings and challenging your assumptions. The AI generates options, identifies blind spots, and pressure-tests your reasoning. You make all decisions. This applies to strategic planning, program design, and difficult policy trade-offs.

Most government work falls into Levels 1 and 2. Level 3 is where AI becomes most valuable for senior analysts and decision-support staff — but it requires more skill in prompting and a stronger ability to evaluate AI outputs critically.

---

## 3.2 The Four-Step AI Workflow for Government Tasks

Every AI-assisted task follows four steps. These are not theoretical. They mirror how the most effective AI practitioners work, whether drafting legislation or preparing budget proposals.[^3]

| Step | What You Do | What AI Does | Time Saved |
|------|------------|-------------|------------|
| 1. Prepare Context | Gather documents, define the task, set boundaries | Nothing yet — waiting for your input | 0% (investment phase) |
| 2. Prompt Clearly | Write clear instructions with examples | Generates first draft based on your guidance | 60-80% of drafting time |
| 3. Review Critically | Check facts, verify citations, assess quality | Nothing — this is your job | 0% (quality gate) |
| 4. Refine Iteratively | Give specific feedback, request changes | Revises based on your corrections | 50-70% of revision time |

Notice the pattern: Steps 1 and 3 are entirely human. Steps 2 and 4 are where AI contributes. **You frame the work and verify the output. AI does the heavy lifting in between.**

### 3.2.1 Step 1: Prepare Context (Gather Relevant Documents, Define the Task, Set Boundaries)

A prompt without context is like a CSW assignment without background materials. The AI will produce something — but it will be generic, possibly wrong, and definitely not tailored to BARMM.

**Before you type a single prompt, gather these:**

1. **The source documents.** If you are drafting a legislative briefer for a proposed bill, have the bill text ready. If you are preparing a budget analysis, have the BAA 84 provisions and the relevant Budget Call Memorandum.[^4]

2. **The legal framework.** Which provisions of the Bangsamoro Organic Law apply? Which existing BAAs are relevant? What national laws intersect?[^5]

3. **The audience and format.** Are you writing for a committee chair? A plenary session? A minister? The format and depth change depending on who will read it.

4. **The boundaries.** Tell the AI what it should *not* do. "Do not draft new provisions — only analyze existing ones." "Do not recommend policy changes — only summarize the current state." Clear boundaries prevent the AI from overstepping.

**Practical example:** You are asked to prepare a briefer on BAA 85 (Annual Budget for FY 2025). Before prompting the AI, you would gather: the full text of BAA 85, relevant sections of BAA 84 (Bangsamoro Budget System Act), the BDP 2023-2028 investment priorities, and the committee's specific questions. Paste or upload these documents into your AI tool before writing the prompt.

> **Time investment:** Context preparation takes 15-30 minutes for most tasks. Skip it and you will spend two hours fixing a bad output. This is the same "measure twice, cut once" logic that drives good CSW practice.

### 3.2.2 Step 2: Prompt Clearly (Write Clear Instructions — Like a Good CSW Assignment Memo)

A prompt is an instruction. Treat it like an assignment memo from a decision-maker to a staff member. The best assignment memos are specific, structured, and clear about what "done" looks like. The best prompts follow the same pattern.

**The anatomy of a good government prompt:**

```
[ROLE] You are a legislative analyst for the Bangsamoro Parliament.

[TASK] Draft a legislative briefer analyzing Proposed Bill No. 245
(Bangsamoro Revenue Code).

[FORMAT] Use the 13-section legislative briefer format from the
CSW Guidebook. Include sections I through XIII.

[SOURCES] Base your analysis on:
- The bill text (pasted below)
- BAA 84 (Bangsamoro Budget System Act)
- BOL Articles VII and XII on fiscal autonomy
- RA 11054 (Bangsamoro Organic Law), particularly the revenue provisions

[CONSTRAINTS]
- Do not fabricate committee proceedings that have not occurred
- Mark any claim you cannot verify with [UNVERIFIED]
- Use proper BARMM terminology (MFBM, not DBM; MILG, not DILG)

[QUALITY STANDARD] The briefer must be ready for supervisor review.
Write at the level of a senior analyst, not an intern summary.
```

**Five rules for government prompts:**

1. **Assign a role.** "You are a budget analyst for MFBM" produces better output than a generic request. The role activates the AI's relevant knowledge.

2. **Specify the format.** Name the exact document type. Reference templates if they exist. "Use the BB-coded budget briefer format" is better than "write me a budget analysis."

3. **Provide the source material.** Paste or upload the actual documents. Do not rely on the AI's memory of legislation — it may be outdated or incorrect.

4. **Set constraints explicitly.** Tell the AI what not to do. "Do not propose new institutional structures." "Do not include figures you cannot source."

5. **Define "done."** State what a successful output looks like. "The output should be 8-10 pages, suitable for a committee chair who has 30 minutes to read before session."

### 3.2.3 Step 3: Review Critically (Check Facts, Verify Citations, Assess Quality)

This is the step most people skip. And it is the step that separates useful AI adoption from dangerous AI dependence.

**AI makes confident-sounding errors.** It will cite a BAA number that does not exist. It will attribute a quote to the wrong official. It will state a budget figure with decimal-point precision — and the figure will be fabricated. The text reads fluently, and that fluency makes errors harder to catch.

**Your review checklist:**

- [ ] **Names and titles.** Is every official's name spelled correctly? Is every title current? The Chief Minister is **Ahod B. Ebrahim**, not "Ahmed." The Speaker is **Pangalian M. Balindong**, not "Pangalian Balindong."[^6]
- [ ] **Legislation references.** Does the BAA number cited actually exist? Does the section number match? Cross-check against the official index of 89 enacted BAAs.[^7]
- [ ] **Budget figures.** Are the amounts correct? Do they match the actual appropriations in the relevant BAA? AI regularly invents plausible-sounding numbers.
- [ ] **Legal provisions.** Are BOL provisions quoted verbatim or paraphrased? If quoted, verify the exact text against the source.
- [ ] **Institutional names.** Does the draft use correct BARMM ministry abbreviations? (MFBM, not DBM. MBHTE, not DepEd. MOH, not DOH. MILG, not DILG.)
- [ ] **Logic and coherence.** Does the analysis actually support the recommendation? Are the sections consistent with each other?

> **The 10-Minute Rule:** Allocate at least 10 minutes of focused review for every 2 pages of AI-generated output. This is non-negotiable. If you do not have time to review it, you do not have time to use it.

### 3.2.4 Step 4: Refine Iteratively (Improve Through Follow-Up Prompts, Don't Accept First Draft)

The first draft is never the final draft. This is true for human writing. It is equally true for AI output. The difference: AI can revise in seconds instead of hours.

**How to give effective feedback to AI:**

- **Be specific.** Not "make it better" but "Section III uses passive voice throughout — rewrite in active voice with the committee as the subject."
- **Point to the problem.** Not "the budget section is wrong" but "the figure in paragraph 3 says PHP 4.2 billion but the actual BAA 85 appropriation for MBHTE is PHP 5.1 billion — correct this."
- **Request one change at a time.** Stacking five requests in one prompt produces worse results than making five sequential requests.
- **Add missing context.** If the first draft missed a relevant BAA or stakeholder, provide that information and ask for a revision. "Also consider BAA 18 (Bangsamoro Education Code) which established the education governance framework."

**Common refinement patterns:**

| Problem | Refinement Prompt |
|---------|------------------|
| Too generic | "Add specific references to BAA provisions and BDP goals" |
| Too long | "Reduce to 5 pages while keeping all key findings" |
| Wrong terminology | "Replace all national government agency names with BARMM equivalents" |
| Missing stakeholders | "Add analysis of how this affects MAFAR and MENRE" |
| Weak recommendation | "Strengthen the recommendation section with cost-benefit data" |
| Inconsistent format | "Reformat to match the 13-section legislative briefer structure" |

**Know when to stop.** If you have refined three times and the output still does not meet your standard, the problem is likely in the context (Step 1) or the prompt (Step 2), not in the refinement. Go back to the beginning.

**The diminishing returns curve:** The first refinement typically captures 60% of the remaining issues. The second captures another 25%. By the third, you are polishing. If major problems persist after three rounds, rewrite your prompt. Four or more refinement rounds on the same prompt usually produce marginal improvement at significant time cost.

---

## 3.3 When to Use AI and When Not To

Not every government task benefits from AI. Some tasks are ideal. Others are inappropriate. The decision matrix below helps you choose.

### Decision Matrix: Government Tasks Ranked by AI Suitability

| Task | AI Suitability | Why | Human Role |
|------|---------------|-----|------------|
| **Drafting first-version memoranda and correspondence** | High | Routine format, clear templates | Review and sign |
| **Summarizing long documents (BAAs, committee reports)** | High | AI processes volume faster than any human reader | Verify accuracy of summary |
| **Comparing provisions across multiple BAAs** | High | Cross-referencing is labor-intensive for humans, fast for AI | Validate the comparison is correct |
| **Preparing legislative briefer first drafts** | High | Structured format, research-heavy | Expert review, policy judgment |
| **Translating documents between English, Filipino, and Arabic** | High | Speed and consistency | Verify nuance and cultural accuracy |
| **Formatting data into tables, charts, and visual aids** | High | Mechanical formatting task | Check data accuracy |
| **Budget analysis and comparison across fiscal years** | High | Number-heavy, pattern-finding | Verify all figures against source |
| **Generating meeting minutes from transcripts** | High | Transcription and summarization | Verify names, confirm action items |
| **Drafting training materials and workshop content** | High | Volume production, modular content | Subject-matter review |
| **Researching best practices from other jurisdictions** | Medium | Good for initial scan, needs human judgment for applicability | Evaluate relevance to BARMM |
| **Drafting policy recommendations** | Medium | AI structures well but may miss political context | Validate feasibility, add local knowledge |
| **Preparing interpellation questions** | Medium | AI generates thorough questions; human selects strategic ones | Strategic selection, political judgment |
| **Reviewing draft bills for legal consistency** | Medium | AI catches textual contradictions; misses intent and precedent | Legal judgment, interpretation |
| **Writing speeches and public statements** | Medium | AI produces drafts; speaker's voice needs human shaping | Voice, tone, political sensitivity |
| **Stakeholder analysis and mapping** | Medium | AI structures the analysis; human provides real relationships | Local knowledge, relationship context |
| **Final legal interpretation of BOL provisions** | Not appropriate | Requires authorized legal judgment with binding consequences | Full human responsibility |
| **Shari'ah rulings and Islamic legal opinions** | Not appropriate | Requires qualified religious scholarship and authority | Darul Ifta, Shari'ah scholars |
| **Political strategy and coalition decisions** | Not appropriate | Requires lived relationships, trust, and political instinct | Leadership judgment |
| **Personnel evaluation and disciplinary decisions** | Not appropriate | Requires fairness, personal observation, due process | Supervisor and HR responsibility |
| **Confidential and classified matters** | Not appropriate | Uploading sensitive data to AI tools creates security risks | Handle through secure channels |
| **Moral governance judgments** | Not appropriate | Requires accountability, ethical reasoning, and community values | Moral governance council, leadership |

**The rule of thumb:** If the task involves **volume, structure, or speed**, AI helps. If the task involves **judgment, authority, or accountability**, the human leads. Most tasks fall somewhere in between — and that is where the four-step workflow matters most.

### How to Read the Matrix

**High suitability** does not mean "hand it off to AI." It means AI can produce a useful first draft that saves significant time. You still review everything.

**Medium suitability** means AI provides a helpful starting point, but the output requires substantial human shaping. The AI contributes maybe 40-50% of the final product; your expertise fills the rest.

**Not appropriate** means the task should not involve AI at all — either because it requires human authority, involves sensitive information that should not be uploaded to AI tools, or depends on judgment that AI cannot provide. Feeding confidential personnel records or classified security briefings into an AI tool creates risks that no time savings can justify.

**When in doubt, ask this question:** "If someone discovered this document was AI-assisted, would that undermine its credibility or create a legal or ethical problem?" If the answer is yes, handle the task manually.

---

## 3.4 Quality Assurance: The "Trust but Verify" Protocol

Every AI output that enters an official government workflow must pass through verification. No exceptions. This is not skepticism about AI — it is the same standard you apply to any staff work product before it reaches a decision-maker.

### The "Trust but Verify" Checklist

Use this checklist for every AI-generated document before it leaves your desk:

**1. Source Verification**
- [ ] Every cited BAA number exists in the official index of enacted BAAs[^7]
- [ ] Every cited section and article number matches the actual text of the law
- [ ] Every cited RA (Republic Act) number is correct and the law is still in force
- [ ] Budget figures match the source document (BAA, BBM, or financial report)

**2. Name and Title Verification**
- [ ] Every person named holds the title attributed to them
- [ ] Names are spelled correctly (check against official directories)
- [ ] Organizational names use BARMM conventions, not national government equivalents
- [ ] Committee names match current BTA parliamentary assignments[^8]

**3. Logical Consistency**
- [ ] The analysis supports the conclusion
- [ ] Recommendations are consistent with the problem statement
- [ ] No internal contradictions between sections
- [ ] Cost estimates align with the scope of the proposal

**4. Format and Standards Compliance**
- [ ] The document follows the correct template (13-section briefer, BB-coded budget briefer, policy recommendation format)
- [ ] Citations follow the approved format[^9]
- [ ] All required sections are present and complete
- [ ] The executive summary accurately reflects the body

**5. Sensitivity Review**
- [ ] No Shari'ah or Islamic legal claims are made without proper scholarly authority
- [ ] Gender-responsive language is used throughout
- [ ] The document respects the moral governance framework[^10]
- [ ] No confidential information was exposed to the AI tool

**6. Attribution and Transparency**
- [ ] The document does not claim AI-generated analysis as original research
- [ ] If institutional policy requires AI disclosure, the disclosure is included
- [ ] The final document reflects the analyst's professional judgment, not raw AI output

> **Verification takes time — and it should.** A 10-page legislative briefer that took 2 hours to generate with AI should get at least 1 hour of verification. If you are not willing to invest that hour, produce the briefer manually instead. AI saves time only when verification is built into the workflow.

### When Verification Reveals a Pattern

Track the errors you find. After using AI on five or ten similar documents, you will notice patterns. Perhaps the AI consistently gets BARMM ministry names wrong. Perhaps it fabricates budget figures. Perhaps it misquotes BOL provisions. Each pattern becomes a **gotcha** — a specific instruction you add to future prompts.

For example, if you discover that AI regularly uses "Department of Education" instead of "MBHTE," add this to every education-related prompt: "Use BARMM ministry names throughout. Specifically: MBHTE (not DepEd), MFBM (not DBM), MILG (not DILG), MOH (not DOH), MOLE (not DOLE), MSSD (not DSWD), MENRE (not DENR), MAFAR (not DA)."

Over time, your prompts become more precise, your AI outputs improve, and your verification time decreases. This is the **compounding returns** of disciplined AI use: every error you catch today makes tomorrow's output better.

---

## 3.5 Document Management and AI Outputs

AI-generated drafts create a version control problem. Without clear naming conventions, you will lose track of which draft is AI-generated, which is human-reviewed, and which is final. These conventions prevent that.

### Naming Conventions

Use this pattern for all AI-assisted documents:

```
[TYPE]-[NUMBER]-[SUBJECT]-[VERSION].[ext]

Examples:
LA-PB245-Revenue-Code-v1-ai.md       ← AI first draft
LA-PB245-Revenue-Code-v2-reviewed.md  ← After human review
LA-PB245-Revenue-Code-v3-final.md     ← Approved for submission
BB-FY2026-MBHTE-v1-ai.md             ← AI-drafted budget briefer
BB-FY2026-MBHTE-v2-final.md          ← Final version
PR-ECCD-Framework-v1-ai.md           ← AI-drafted policy recommendation
```

**Document type codes:**

| Code | Document Type |
|------|--------------|
| LA | Legislative Analysis Briefer |
| BB | Budget Briefer |
| PR | Policy Recommendation |
| LO | Legal Opinion |
| PP | Project Proposal |
| PA | Personnel/Administrative Action |
| GN | General CSW |
| MO | Memorandum/Correspondence |
| SR | Summary/Research Report |

### Version Control Rules

1. **Never overwrite an AI draft with your edits.** Save your reviewed version as a new file (v2, v3). This lets you compare what the AI produced against what you submitted.

2. **Mark AI-generated versions clearly.** The `-ai` suffix on version 1 tells anyone looking at the file that it is unreviewed AI output.

3. **Keep final versions separate from drafts.** Only the `-final` version should be transmitted to a decision-maker or attached to a transmittal memo.

4. **Retain the AI conversation.** If your AI tool allows export of the conversation, save it alongside the document. This creates an audit trail showing how the document was produced and what instructions were given.

### Folder Structure for AI-Assisted Projects

For complex projects like legislative briefers or policy recommendations that require multiple AI sessions, maintain a project folder:

```
CSW-PB312-ECCD/
├── sources/                  ← Source documents used as AI context
│   ├── PB-312-full-text.pdf
│   ├── BAA-49-excerpts.md
│   └── BDP-Ch5-excerpts.md
├── drafts/
│   ├── LA-PB312-v1-ai.md    ← AI first draft
│   ├── LA-PB312-v2-reviewed.md
│   └── LA-PB312-v3-final.md
├── ai-logs/                  ← Exported AI conversations (optional)
│   └── session-2026-03-15.md
└── transmittal/
    └── TM-PB312-signed.pdf   ← Final transmittal memorandum
```

This structure ensures that anyone inheriting the file can see exactly what sources were used, how the document evolved, and what the AI contributed. It also protects you during audits or quality reviews.

### Attribution Practices

Your office should establish a clear policy on AI attribution. At minimum:

- **Internal documents:** Note in the file metadata or cover memo that AI tools assisted in drafting. Example: "Initial draft prepared with AI assistance; all content verified by [analyst name]."

- **Official submissions:** The human author is the author of record. AI is a tool, like a calculator or a database query. You do not credit your spreadsheet software in a budget proposal.

- **Published materials:** Follow whatever disclosure policy your office or the Chief Minister's Office adopts. When no policy exists, err toward transparency.

---

## 3.6 Building AI Into Existing Processes, Not Replacing Them

AI is a layer on top of ADDRESS IT. It is not a separate system. Every step in the seven-step CSW process can benefit from AI assistance — but the human remains responsible for every step.

### How ADDRESS IT Maps to AI

The table below shows exactly what AI does and what the human does at each step of the ADDRESS IT framework.[^1]

| ADDRESS IT Step | What AI Does | What Human Does | Quality Check |
|----------------|-------------|----------------|---------------|
| **Step 1: Analyze the Context** | Summarizes source documents. Identifies relevant BOL provisions. Lists stakeholders from similar past initiatives. Extracts key data from reports. | Defines the assignment. Clarifies ambiguities with the superior. Validates stakeholder list from personal knowledge. Confirms which laws apply. | Human verifies AI's document summaries are accurate. Human adds stakeholders AI missed. |
| **Step 2: Define and Deliberate** | Generates problem statement drafts. Identifies potential root causes from similar documented cases. Produces PESTEL analysis frameworks. | Engages stakeholders in actual deliberation. Selects the true root cause. Establishes SMART objectives. Validates problem statement. | Human confirms problem statement matches reality, not just what documents say. |
| **Step 3: Research** | Scans large document sets. Compiles comparative analyses. Identifies relevant provisions across multiple BAAs. Summarizes academic literature. | Designs the research plan. Evaluates source credibility. Conducts primary data collection (interviews, field visits). Validates findings. | Human verifies all AI-cited sources exist and say what AI claims they say. |
| **Step 4: Explore Options** | Generates option frameworks. Drafts pro/con comparisons. Produces cost-benefit analysis templates. Identifies precedents from other jurisdictions. | Evaluates feasibility from local knowledge. Conducts stakeholder consultations. Applies political and cultural judgment. Selects the best option. | Human validates that AI-generated options are actually implementable in BARMM. |
| **Step 5: Submit Proposal** | Drafts the full report. Formats according to template. Writes executive summary. Generates visual aids (tables, charts). | Reviews every page. Verifies all facts. Refines recommendations. Obtains supervisor clearance. Signs and submits. | Supervisor reviews the final product. "Trust but Verify" checklist is completed. |
| **Step 6: Sustain Implementation** | Tracks milestones against the implementation plan. Drafts progress reports. Generates monitoring dashboards. | Mobilizes resources. Coordinates with partners. Addresses political obstacles. Maintains stakeholder relationships. | Human confirms AI-tracked progress matches ground reality. |
| **Step 7: Iterate and Improve** | Analyzes performance data. Identifies trends. Compares outcomes against targets. Drafts evaluation reports. | Interprets what the data means. Decides what to change. Engages stakeholders in feedback. Documents lessons learned. | Human validates that AI-identified patterns are real, not statistical artifacts. |

### The Overlay Principle

Notice that AI never *replaces* a step. It augments each one. The ADDRESS IT process remains intact. The staff member still walks through all seven steps. The difference is that steps involving heavy reading, drafting, and data processing now take hours instead of days.

This is deliberate. If your office adopts AI today and the tools disappear tomorrow, your ADDRESS IT process still works. You just return to manual methods. AI is an accelerator, not a dependency.

**Why this matters for BARMM specifically:** The Bangsamoro government is in a transition period. Staff turnover is high. Institutional memory is thin. Processes that depend entirely on AI tools become fragile — if the subscription lapses, the internet goes down, or the tool changes its features, work stops. Processes that use AI as an overlay on ADDRESS IT are resilient. The seven steps provide the backbone. AI provides the speed.

**A practical test:** After completing any AI-assisted task, ask yourself: "Could I explain to my supervisor exactly how I arrived at this recommendation, step by step, without mentioning AI?" If the answer is yes, you used AI correctly — as a tool within a sound process. If the answer is no — if you cannot justify the analysis without saying "the AI told me" — then you relied on AI instead of overlaying it. Go back to the four-step workflow and add more of your own analysis.

### Cross-Reference to Other Guidebooks

The ADDRESS IT framework is covered in full in the *Complete Staff Work Guidebook for the Bangsamoro Autonomous Region*, Chapters 4-10.[^1] If you have not read that guidebook, start with the ADDRESS IT Quick Reference Card (Appendix A of the CSW guidebook) to understand each step before mapping AI onto it.

For specific document types that benefit from AI assistance:
- **Legislative briefers** — see this guidebook, Chapter 7 (AI for Legislative and Policy Work) and the CSW guidebook, Chapter 11 (CSW for Parliamentary Committees)
- **Budget briefers** — see this guidebook, Chapter 6 (AI for Budgeting and Financial Analysis) and the CSW guidebook, Chapter 12, Section 12.1
- **Policy recommendations** — see this guidebook, Chapter 7, Section 7.6 and the CSW guidebook, Chapter 3, Section 3.4
- **Project proposals** — see this guidebook, Chapter 8 (AI for Program Implementation) and the CSW guidebook, Chapter 12, Section 12.2

Appendix E of this guidebook provides a complete mapping of AI assistance to every ADDRESS IT step, with specific prompts for each.

---

## Case Study: Using AI to Prepare a Legislative Briefer

> **Scenario:** You are a legislative analyst assigned to the Committee on Basic, Higher, and Technical Education. The committee chair asks you to prepare a legislative briefer for Proposed Bill No. 312 (Bangsamoro Early Childhood Care and Development Act). You have three days before the committee session.

### Step 1: Prepare Context (Day 1 Morning — 2 Hours)

You gather the source materials:
- Full text of Proposed Bill No. 312
- BOL, Article IX (Education) and Article XIII, Section 4 (powers of the BTA)
- BAA 18 (Bangsamoro Education Code) — the existing education framework
- RA 8980 (ECCD Act, national law) — the law PB 312 aims to localize
- Committee records from previous hearings, if any
- BDP 2023-2028, Chapter 5 (Human Capital Development goals)

You upload or paste these documents into your AI tool. You note the boundaries: the briefer should analyze the bill, not recommend a vote.

### Step 2: Prompt Clearly (Day 1 Afternoon — 1 Hour)

You write:

```
You are a legislative analyst for the BTA Committee on Basic, Higher,
and Technical Education.

Draft a 13-section legislative briefer for Proposed Bill No. 312
(Bangsamoro ECCD Act). Use the standard legislative briefer format:

I. Overview
II. Brief Description of the Measure
III. Previous Proceedings and Committee Actions
IV. Summary of Key Provisions
V. Implementing Agencies and Institutional Framework
VI. Financial Implications
VII. Legal and Constitutional Analysis (BOL, RA 8980, BAA 49)
VIII. Comparative Analysis with National ECCD Framework
IX. Stakeholder Impact Assessment
X. Parliamentary Strategy and Expected Debates
XI. Proposed Committee Amendments
XII. Recommended Committee Position and Vote
XIII. Strategic Intelligence for the Committee Chair

Base your analysis on the documents I provided. Use BARMM
terminology (MBHTE, not DepEd). Mark any information you cannot
verify with [UNVERIFIED]. Do not fabricate committee proceedings.
```

The AI generates a 12-page first draft in approximately 3 minutes.

### Step 3: Review Critically (Day 2 — 3 Hours)

You read every section against the source documents:
- Section VII claims Article IX, Section 3 of the BOL grants explicit ECCD authority. You check: the actual BOL text does not mention ECCD specifically, only "basic education." You correct this.
- Section VI estimates a PHP 500 million annual implementation cost. No source is given. You mark this [UNVERIFIED] and search the bill's explanatory note for actual figures.
- Section V lists the "Department of Social Welfare" as a co-implementer. You correct this to MSSD (Ministry of Social Services and Development).
- The draft names a committee member incorrectly. You correct the name and title.

You run through the full "Trust but Verify" checklist from Section 3.4.

### Step 4: Refine Iteratively (Day 2 Afternoon — 2 Hours)

You provide three rounds of feedback:

**Round 1:** "Section VII needs to clarify that ECCD is implied but not explicit in the BOL's education provisions. Rewrite the constitutional analysis to reflect this gap."

**Round 2:** "Add a comparison table showing how PB 312 differs from RA 8980 in at least 8 specific provisions — service delivery structure, funding mechanism, quality standards, age coverage, curriculum authority, personnel requirements, coordination mechanism, and oversight framework."

**Round 3:** "The recommendation in Section XII is too vague. Draft three specific conditions the committee should attach to approval, based on the gaps identified in Sections VII and VIII."

### Result

**Time comparison:**

| Activity | Without AI | With AI |
|----------|-----------|---------|
| Gathering source documents | 3 hours | 2 hours (same research, slightly faster with AI-assisted search) |
| Reading and analyzing sources | 8 hours | 4 hours (AI summarizes, human verifies) |
| Drafting the briefer | 10 hours | 1 hour (AI drafts) + 3 hours (human reviews) |
| Revision and formatting | 3 hours | 2 hours (AI revises, human finalizes) |
| **Total** | **24 hours (3 full days)** | **12 hours (1.5 days)** |

The analyst saved approximately 50% of total time. More importantly, the quality of the comparative analysis in Section VIII was higher because the AI could systematically compare provisions across two laws — a task that is tedious and error-prone when done manually.

**What went wrong and how it was caught:**
- The AI fabricated a committee hearing date in Section III. The analyst caught this because no hearings had been conducted yet. **Lesson:** AI fills gaps with plausible-sounding fiction. Always verify procedural facts.
- The AI used "DepEd" four times instead of "MBHTE." The analyst corrected every instance. **Lesson:** AI defaults to national government terminology. Always search for incorrect agency names before submitting.
- The cost estimate in Section VI had no source. The analyst either found a source or marked it [UNVERIFIED] with a note explaining the estimate's basis. **Lesson:** Unsourced numbers are the most dangerous AI output. Every figure needs a citation.

The AI produced the structure and the first draft. The analyst produced the accuracy, the judgment, and the final product worthy of a committee chair's desk.

---

## Chapter Summary

The AI-augmented workflow rests on five principles:

1. **AI drafts, you decide.** The human-AI partnership mirrors CSW: the staff does the work, the decision-maker approves. AI is the staff; you are the decision-maker over AI's output.

2. **Four steps, every time.** Prepare Context, Prompt Clearly, Review Critically, Refine Iteratively. Skip the review step and you risk submitting fabricated information.

3. **Not every task needs AI.** Use the decision matrix. High-volume, structured, research-heavy tasks benefit most. Final legal interpretations, Shari'ah rulings, and political judgments stay fully human.

4. **Trust but verify — always.** The six-part checklist applies to every AI-generated document. Sources, names, logic, format, sensitivity, and attribution.

5. **Overlay, do not replace.** AI maps onto every ADDRESS IT step without changing the process. If the tools vanish, your workflow survives.

The next chapter shows you how to build the document foundation that makes AI useful: how to prepare government documents, structure a knowledge base, and manage the data that feeds every prompt.

---

## Footnotes

[^1]: The ADDRESS IT framework is a seven-step CSW methodology (Analyze, Define and Deliberate, Research, Explore Options, Submit Proposal, Sustain Efforts, Iterate and Improve) developed for BARMM governance. See the *Complete Staff Work Guidebook for the Bangsamoro Autonomous Region* (Mambayao, 2026), particularly the ADDRESS IT Quick Reference in Appendix A. The full framework is detailed in Chapters 4-10 of that guidebook.

[^2]: The principle that "the decision-maker should only need to approve or disapprove" is the foundational standard of Complete Staff Work as institutionalized in Philippine governance through Civil Service Commission Memorandum Circular No. 72, s. 2019 ("Institutionalization of the Practice of Complete Staff Work in Government") and Memorandum Circular No. 2, s. 2022 (superseding MC 72). See *Complete Staff Work Guidebook for the Bangsamoro Autonomous Region*, Chapter 1, Section 1.1.1.

[^3]: The four-step workflow synthesizes practitioner patterns from AI-augmented document production. The "Prepare, Prompt, Review, Refine" cycle is adapted from structured skill workflows documented by practitioners working with Claude Code and similar AI tools. See AI-Claude-Code GUIDE (2026), particularly the Five-Skill Workflow discussion.

[^4]: BAA 84 (Bangsamoro Budget System Act) establishes the legal framework for the BARMM budget cycle, including preparation, authorization, execution, and accountability. Budget Call Memoranda (BBMs) are issued annually by MFBM to guide budget preparation for the upcoming fiscal year.

[^5]: Republic Act No. 11054, or the Bangsamoro Organic Law (BOL), is the foundational law establishing the Bangsamoro Autonomous Region in Muslim Mindanao. Its 18 Articles define the powers, structure, and fiscal framework of the Bangsamoro government.

[^6]: Official names and titles of BARMM officials should always be verified against current official directories. Officials referenced in this guidebook reflect the BTA membership for the transition period as of 2025-2026. Names and positions change — always verify before finalizing any document.

[^7]: The Bangsamoro Parliament has enacted 89 Bangsamoro Autonomy Acts (BAAs) as of the current transition period. An index of all enacted BAAs is maintained and should be the authoritative reference for verifying BAA numbers and titles.

[^8]: BTA Parliamentary and Committee Assignments are published periodically. The most recent assignments should be verified against official Parliament records.

[^9]: Philippine Manual of Legal Citations (Feliciano, 10th Ed.) is the standard reference for citation format in Philippine legal and government documents.

[^10]: The moral governance framework is established under BAA 13 (Bangsamoro Moral Governance Act), which institutionalizes the 12 Pillars of Moral Governance for the BARMM. See *Complete Staff Work Guidebook for the Bangsamoro Autonomous Region*, Chapter 2, Section 2.3.
