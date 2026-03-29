# Chapter 13 — Getting Started: An Implementation Roadmap

You have read eleven chapters on what AI can do across the governance cycle. You have seen prompts, examples, and BARMM-specific applications. The question now is: **where do you start?**

The answer depends on where you are. A staff member opening Claude for the first time faces a different challenge than a ministry director drafting an AI adoption policy. A lone researcher experimenting with NotebookLM operates in a different reality than a Parliament committee secretariat standardizing AI-assisted briefers across twelve standing committees.

This chapter gives you the roadmap. It maps three maturity levels — individual, team, institutional — and provides concrete actions for each. It ends with a 90-day plan that any BARMM office can adapt, and a change management framework that addresses the specific resistance patterns you will encounter in Bangsamoro government settings.

Start where you are. Move at the speed your context allows. But start.

---

## 13.1 The Three Maturity Levels

AI adoption does not happen all at once. It follows a predictable progression. Understanding where you fall on this progression prevents two common mistakes: **trying to do too much too fast** (which creates backlash and abandoned tools) and **staying at the individual level forever** (which limits AI's impact to personal productivity rather than institutional improvement).

### 13.1.1 Level 1: Individual Use and Personal Productivity

**Level 1 is one person using AI to do their own work faster.** No policy exists. No team agreement governs usage. The staff member experiments on their own initiative, learns through trial and error, and applies AI to tasks within their personal control.

**Characteristics of Level 1:**

- **One user, one tool.** A legislative researcher uses Claude to summarize committee reports. A budget analyst uses NotebookLM to analyze COA findings. Each person works independently.
- **No shared prompts or standards.** Two staff members doing the same task may prompt differently and get inconsistent outputs.
- **No institutional knowledge capture.** When a staff member discovers an effective prompt for drafting BAA summaries, that knowledge stays in their head or their personal files.
- **No quality assurance beyond the individual.** The staff member decides what to verify and how. There is no shared protocol for checking AI outputs.
- **No budget allocation.** The staff member uses free tools or pays for subscriptions personally.

**Level 1 is where every AI adoption starts.** It is valuable. It is necessary. But it is not sufficient. If your office stays at Level 1 indefinitely, you have individual efficiency gains without institutional transformation.

### 13.1.2 Level 2: Team Integration and Shared Workflows

**Level 2 is a team agreeing on how to use AI together.** The unit shares prompts. It maintains a common knowledge base. It establishes basic quality standards. AI becomes part of the team's workflow rather than an individual's side experiment.

**Characteristics of Level 2:**

- **Shared prompt libraries.** The committee secretariat maintains a set of tested prompts for legislative briefers, committee reports, and plenary preparation. New staff inherit them.
- **Common knowledge bases.** The team maintains an Obsidian vault or NotebookLM notebook that everyone contributes to and draws from. The vault contains enacted BAAs, committee records, and reference documents that give AI the context it needs.
- **Basic SOPs.** The team has written agreements: "All AI-drafted briefers go through the Senior Legislative Officer before submission." "All budget analysis outputs are verified against original GAA figures." "No confidential documents are uploaded to cloud-based AI tools."
- **Designated AI champions.** At least one team member stays current on AI capabilities and trains colleagues on new techniques.
- **Some budget awareness.** The team lead has justified subscription costs in the office budget, or the agency has secured a team-level plan.

**Level 2 is where AI begins to multiply its impact.** Instead of one person working faster, an entire unit produces higher-quality outputs with greater consistency.

### 13.1.3 Level 3: Institutional Adoption and Policy-Backed Deployment

**Level 3 is the organization making AI a formal part of how it operates.** Executive leadership has approved an AI use policy. Training programs exist. Budget lines fund subscriptions and capacity building. AI-assisted processes are documented in the office's manual of operations. Performance metrics track AI impact.

**Characteristics of Level 3:**

- **Formal AI use policy.** The office has issued a written policy governing acceptable uses, prohibited uses, data classification rules, quality assurance requirements, and accountability structures.[^1]
- **Institutional training program.** New staff receive AI orientation. Existing staff receive periodic skills updates. The training covers both technical competency and ethical guidelines.
- **Budget allocation.** AI subscriptions and training costs appear as line items in the office's annual work and financial plan.
- **Process integration.** The office's standard operating procedures explicitly incorporate AI at defined steps — with human review checkpoints built in.
- **Performance measurement.** The office tracks AI impact: time saved on routine tasks, output quality improvements, staff satisfaction, and cost-effectiveness.
- **Knowledge management infrastructure.** The institutional knowledge base is maintained, updated, and accessible to all authorized staff.

**Level 3 is the target.** Not every office will reach it in the first year. But every office should move toward it deliberately.

### Table 13.1: Maturity Level Comparison

| Dimension | Level 1: Individual | Level 2: Team | Level 3: Institutional |
|---|---|---|---|
| **Who uses AI** | Individual staff members | Defined teams or units | The entire office or ministry |
| **Governance** | None | Informal team agreements | Formal AI use policy |
| **Prompts** | Personal, ad hoc | Shared prompt library | Standardized, version-controlled |
| **Knowledge base** | Personal files | Shared team vault or notebook | Institutional knowledge management system |
| **Quality assurance** | Self-review | Peer review within team | Defined QA process with assigned reviewers |
| **Training** | Self-taught | Peer coaching and mentoring | Formal training program |
| **Budget** | Personal or unfunded | Team-level justification | Dedicated budget line |
| **Measurement** | Anecdotal | Basic team tracking | Institutional KPIs |

---

## 13.2 Level 1 — Individual Quick Wins

**You do not need permission to start using AI.** You need a free account, a clear task, and twenty minutes. Level 1 is about building your own confidence and competence before you try to convince anyone else.

### What Any Staff Member Can Do Tomorrow

Start with tasks you already do. Do not invent new tasks for AI. Take the work sitting on your desk right now and ask: **which part of this task is information processing that AI could help with?**

The table below maps eight common BARMM roles to their highest-value first AI tasks. Each entry includes the role, the task, the estimated time savings, the recommended tool, and a sample prompt opening. Use this as your starting point.

### Table 13.2: Quick Wins by Role

| Role | First AI Task | Time Saved | Tool | Sample Prompt Start |
|---|---|---|---|---|
| **Legislative Researcher** | Summarize a 50-page committee hearing transcript into a 2-page briefer | 3-4 hours per transcript | Claude | "Summarize this committee hearing transcript. Extract: key issues discussed, positions taken by each speaker, decisions made, action items assigned..." |
| **Budget Analyst** | Compare two fiscal years of ministry budget allocations and flag variances above 10% | 2-3 hours per comparison | Claude or NotebookLM | "Compare the FY 2025 and FY 2026 budget allocations for [Ministry]. For each program, show the year-over-year change..." |
| **Legal/Bill Drafter** | Cross-reference a draft bill against existing BAAs for conflicts or redundancies | 4-6 hours per bill | Claude with BAA knowledge base | "Review this draft bill against the following enacted BAAs. Identify any provision in the draft that conflicts with, duplicates, or amends an existing provision..." |
| **Administrative Officer** | Draft routine correspondence (invitations, transmittal letters, acknowledgments) | 30-60 minutes per batch | Claude | "Draft a formal transmittal letter from [Office] to [Recipient] transmitting the attached [document]. Follow Philippine government correspondence format..." |
| **Planning Officer** | Extract BDP alignment indicators for a ministry's annual work plan | 2-3 hours per plan | Claude with BDP chapters | "Review this ministry work plan and map each program/activity/project to the relevant BDP 2023-2028 goal and strategy. Flag any PPA that does not align..." |
| **M&E Officer** | Generate a quarterly accomplishment report template from the ministry's targets | 1-2 hours per report cycle | Claude | "Based on these annual performance targets, create a quarterly accomplishment report template with columns for: target, Q1-Q4 actual, variance, remarks..." |
| **HR/Personnel Officer** | Summarize and compare applicant qualifications against position requirements | 1-2 hours per screening batch | Claude | "Compare the following applicant profiles against the qualification standards for [Position]. For each applicant, list: met requirements, unmet requirements..." |
| **Communications Officer** | Draft press releases and social media summaries of parliamentary actions | 1-2 hours per release | Claude | "Write a press release announcing that the BTA Parliament enacted [BAA number and title]. Include: what the law does, who benefits, key provisions..." |

### The Five Rules for Level 1 Success

1. **Start with your own work, not someone else's.** Do not volunteer to AI-optimize a colleague's process before you have optimized your own. Your credibility comes from demonstrated results.
2. **Begin with low-stakes tasks.** Draft correspondence, not position papers. Summarize documents, not make policy recommendations. Build confidence before raising the stakes.
3. **Verify everything.** At Level 1, you are the only quality control. Check every fact, every number, every citation. AI will occasionally produce plausible but incorrect outputs. Your reputation depends on catching those errors before they reach your supervisor.[^2]
4. **Save your best prompts.** When you find a prompt that consistently produces good results, save it in a file. Label it with the task it serves. You will need this library when you move to Level 2.
5. **Track your time savings.** Note how long a task took before AI and how long it takes now. You will need this data to justify AI adoption to your supervisor and budget officer.

### The First Week: A Day-by-Day Guide

Some staff members read "start tomorrow" and still do not know what to do on Tuesday. This section removes that ambiguity.

**Day 1 (Monday): Set up.** Create a free Claude account at claude.ai. Spend fifteen minutes exploring the interface. Type a simple prompt: "Explain the structure of the Bangsamoro Autonomous Region in Muslim Mindanao." Read the output. Notice what it gets right. Notice what it gets wrong. You have just completed your first AI interaction as a government employee.

**Day 2 (Tuesday): Choose your task.** Look at your work plan for the week. Identify the most time-consuming document-based task. This is your pilot. Write down how long that task normally takes you.

**Day 3 (Wednesday): Write your first work prompt.** Open Claude. Provide context: your role, the document you need, the format required, the audience. Be specific. Run the prompt. Evaluate the output honestly — what is usable, what needs revision, what is wrong.

**Day 4 (Thursday): Iterate.** Take the same task. Revise your prompt based on yesterday's results. Add more context. Specify the format more precisely. Include a reference document if you have one. Run it again. Compare.

**Day 5 (Friday): Document.** Write down: (1) the task, (2) your final prompt, (3) the time it took with AI versus without, (4) what you learned. Save this file. This is the first entry in your personal prompt library.

### Getting Started Checklist

- [ ] Create a free Claude account (claude.ai)
- [ ] Identify three recurring tasks from your current workload
- [ ] Write your first prompt for the simplest of those three tasks
- [ ] Run the prompt and compare the output against what you would have produced manually
- [ ] Revise the prompt based on what worked and what did not
- [ ] Save the revised prompt in a personal prompt library file
- [ ] Track the time you spent (prompt time + review time) versus your manual baseline

---

## 13.3 Level 2 — Team-Level Integration

**Level 2 begins when one person's success becomes the team's opportunity.** Someone on your team has been using AI effectively. Their outputs are noticeably faster, their drafts need fewer revisions, and their research is more thorough. The question shifts from "Should I try AI?" to "How do we all use it consistently?"

### Moving from Individual to Team

The transition from Level 1 to Level 2 requires three things:

1. **A team lead who supports experimentation.** The division chief, section head, or committee chairperson must explicitly authorize AI use and signal that they value the results. Without leadership support, individual AI users stay isolated.
2. **At least two people who have Level 1 experience.** You cannot build a shared practice from zero. You need at least two team members who have used AI successfully so they can compare approaches and develop shared standards.
3. **A specific workflow to standardize.** Do not try to AI-enable everything at once. Pick one recurring team process — the weekly committee briefer, the monthly budget report, the quarterly accomplishment review — and standardize AI use for that single process first.

### Shared Prompt Libraries

A **shared prompt library** is a document or folder that contains tested prompts for the team's recurring tasks. Every prompt includes:

- **The task it serves** (e.g., "Draft a committee hearing briefer for a standing committee chairperson")
- **The prompt text** (the exact wording that produces consistently good results)
- **Required inputs** (what documents or data the user needs to provide)
- **Expected output format** (what the AI should produce)
- **Quality checkpoints** (what the reviewer should verify before the output is used)

Store the prompt library where the whole team can access it. An Obsidian vault works well. A shared folder works. A Google Doc works. The format matters less than the discipline of maintaining it.

> **Example — Parliamentary Committee Secretariat Prompt Library:**
>
> A standing committee secretariat maintains prompts for:
> - Pre-hearing briefer (summarizes the agenda item, relevant BAAs, and ministry responses)
> - Post-hearing minutes (converts raw hearing transcript into structured minutes)
> - Committee report draft (synthesizes findings from multiple hearings into a committee report)
> - Follow-up tracker (generates a list of commitments made by ministry officials during hearings)
>
> Each prompt was developed by the committee's legislative officers, tested across multiple hearings, and revised based on what worked. New staff receive the prompt library on their first day.[^3]

### Building a Team Knowledge Base

A **knowledge base** is the collection of documents that gives AI the context it needs to produce BARMM-specific outputs. Without a knowledge base, AI produces generic responses. With one, it produces outputs grounded in Bangsamoro law, policy, and institutional practice.

**What goes in a team knowledge base:**

| Category | Examples | Purpose |
|---|---|---|
| **Legal texts** | BAAs relevant to the team's mandate, BOL provisions, IRRs | Ensures AI references actual Bangsamoro law |
| **Policy documents** | BDP 2023-2028 chapters, ministerial development plans, executive orders | Grounds AI outputs in current BARMM policy |
| **Templates** | Standard briefer format, committee report format, correspondence templates | Ensures AI outputs match institutional formatting |
| **Historical records** | Previous committee reports, past budget analyses, prior accomplishment reports | Gives AI context for continuity and trend analysis |
| **Reference data** | Organizational structure, staff directory, committee assignments, budget allocations | Enables AI to produce outputs with correct names, titles, and numbers |

**How to build it:**

1. **Assign one person** to collect and organize the team's reference documents. This person does not need to be the most senior — they need to be the most organized.
2. **Start with the documents the team uses most frequently.** If your team produces legislative briefers, start with the enacted BAAs, the committee's past reports, and the standard briefer template.
3. **Upload to your AI tool.** Claude Projects allows you to attach reference documents. NotebookLM allows you to add multiple sources per notebook. Obsidian provides a local knowledge base that works with Claude Desktop.
4. **Update regularly.** A knowledge base that was built six months ago and never updated will produce outputs based on outdated information. Assign a monthly review.

### Prompt Versioning and Quality Control

Prompts degrade over time. AI tools update their models. Team requirements evolve. A prompt that produced excellent legislative briefers in January may produce mediocre ones by June if the model's behavior has shifted or the team's standards have changed.

**Implement basic version control:**

- **Number your prompts.** Start with v1.0. When you make significant changes, increment to v2.0. Minor tweaks become v1.1, v1.2.
- **Date every revision.** Record when the prompt was last tested and who tested it.
- **Retire outdated prompts.** When a prompt no longer produces acceptable output, mark it as deprecated and replace it. Do not leave broken prompts in the library for new staff to discover.
- **Test after AI tool updates.** When Claude, NotebookLM, or any other tool announces a major update, test your top five prompts within the first week. Flag any that produce noticeably different outputs.

### Standard Operating Procedures for AI Use

At Level 2, the team develops basic SOPs. These do not need to be elaborate. Three to five rules will cover most situations.

**Sample Team AI SOP:**

1. **All AI-assisted outputs are reviewed by at least one person before submission.** The person who generated the output cannot be the sole reviewer.
2. **Legal citations in AI-generated drafts are verified against the original text.** Do not trust AI to quote a BAA provision correctly — check it.
3. **Confidential documents are not uploaded to cloud-based AI tools.** Use Claude Desktop (local processing) for documents classified as confidential or above.
4. **The team prompt library is the starting point for recurring tasks.** Individual modifications are allowed, but the base prompt should be used for consistency.
5. **Time savings and quality improvements are logged in the team's weekly report.** This data supports future budget requests for AI subscriptions and training.

### The Level 2 Transition Checklist

- [ ] Identify at least two staff members with Level 1 AI experience
- [ ] Select one recurring team process for AI standardization
- [ ] Create an initial shared prompt library with tested prompts for that process
- [ ] Build a starter knowledge base with the team's most-used documents
- [ ] Draft a team AI SOP (3-5 rules, 1-2 pages)
- [ ] Conduct a team orientation session on the shared tools and standards
- [ ] Assign an AI Champion to maintain the prompt library and knowledge base
- [ ] Begin tracking team-level time savings and quality improvements

---

## 13.4 Level 3 — Institutional Adoption

**Level 3 is where AI stops being a team experiment and becomes an organizational commitment.** This requires executive leadership, formal policy, dedicated budget, and integration into the office's standard processes.

### What Institutional Adoption Requires

**1. Executive Sponsorship**

The ministry head, chief of staff, or office director must champion AI adoption. This is not optional. Without executive sponsorship, AI initiatives remain at the team level because they lack the authority to change office-wide processes, allocate budget, or require participation.

The executive sponsor does not need to be an AI expert. They need to understand the value proposition: **AI-augmented staff produce more, higher-quality work with the same headcount.**[^4] In BARMM's context — where many offices are still filling plantilla positions and staff carry multiple portfolios — this proposition is compelling.

**2. A Formal AI Use Policy**

The policy establishes what is allowed, what is required, and what is prohibited. At minimum, it covers:

- **Scope.** Which staff and which functions are covered.
- **Approved tools.** Which AI platforms are authorized for use with government work.
- **Data classification.** Which documents can be processed by cloud-based AI tools and which require local processing only.
- **Quality assurance.** The review process for AI-assisted outputs before they are submitted externally.
- **Accountability.** The human who submits an AI-assisted output takes full responsibility for its accuracy. AI does not sign documents. People do.[^5]
- **Ethical guidelines.** Alignment with the Twelve Pillars of Moral Governance and the Islamic principles discussed in Chapter 12.

See Appendix D for a complete sample AI policy adapted for a BARMM office.

**3. Training Infrastructure**

Institutional adoption requires more than one orientation session. It requires an ongoing training program that covers new staff, skill updates, and specialized applications. Chapter 14 covers training program design in detail.

**4. Budget Allocation**

AI is not free at scale. Team-level subscriptions (Claude Pro, NotebookLM Plus, Obsidian Sync) cost money. Training workshops require facilitator time and logistics. Knowledge base maintenance requires staff time. These costs must appear in the office's annual work and financial plan.

**Budget Items to Plan For:**

| Item | Estimated Annual Cost | Justification |
|---|---|---|
| **AI tool subscriptions** (5-10 users) | PhP 120,000 - 300,000 | Enables staff access to professional-grade AI tools |
| **Training workshops** (2 per year) | PhP 50,000 - 100,000 per workshop | Builds and maintains staff AI competency |
| **Knowledge base maintenance** (staff time) | 2-4 hours/month per assigned staff | Keeps AI reference materials current and accurate |
| **External technical support** (as needed) | PhP 50,000 - 150,000 | Setup assistance, troubleshooting, advanced configuration |

These are modest investments compared to the alternative: hiring additional staff to handle increasing workloads. A single Claude Pro subscription costs roughly PhP 12,000 per year. A single additional staff member costs PhP 300,000-500,000 per year in salary alone.[^6]

**5. Process Integration**

AI must be written into the office's existing workflows, not bolted on as an afterthought. This means revising standard operating procedures to include AI-assisted steps with defined human review checkpoints.

> **Example — Integrating AI into the Budget Preparation Cycle:**
>
> The MFBM planning division revises its budget preparation SOP:
> - Step 1: Receive Budget Call from the Chief Minister (human)
> - Step 2: Compile prior year's budget execution data (human, with AI-assisted data extraction)
> - Step 3: Generate variance analysis between planned and actual expenditures (AI-assisted, reviewed by Senior Budget Analyst)
> - Step 4: Draft budget narrative for each program (AI-assisted, reviewed by Division Chief)
> - Step 5: Present to Ministry Head for approval (human)
> - Step 6: Submit to MFBM Budget Bureau (human)
>
> AI appears at Steps 2, 3, and 4. Human review gates appear at Steps 3 and 4. No step is fully automated.[^7]

**6. Knowledge Management as Infrastructure**

At Level 3, the knowledge base is no longer a team folder. It is institutional infrastructure. Treat it like you treat your office's filing system — with assigned custodians, update schedules, access controls, and retention policies.

**Institutional knowledge management requirements:**

- **Custodian assignment.** Name a staff member responsible for each knowledge base domain (legislative, budgetary, administrative, HR).
- **Update schedule.** Define when new documents are added. After every parliamentary session? After every budget cycle? After every new BAA is enacted?
- **Access controls.** Define who can read, who can add, and who can modify. Not every staff member needs write access. But every staff member needs read access.
- **Retention policy.** Define what stays and what gets archived. A knowledge base cluttered with five-year-old drafts is harder for AI to work with than a curated collection of current documents.
- **Backup.** If the knowledge base lives on a local machine, back it up. If it lives in the cloud, ensure you have a local copy. Government data should never exist in only one place.

---

## 13.5 The 90-Day AI Adoption Plan for a BARMM Office

The plan below is designed for a BARMM ministry division, parliamentary committee secretariat, or attached agency office with 5-15 staff. Adapt the timeline to your context. Some offices will move faster. Some will need more time at each phase. The sequence matters more than the speed.

### Table 13.3: 90-Day AI Adoption Plan

| Week | Phase | Activities | Responsible | Deliverable |
|---|---|---|---|---|
| **1** | **Assess** | Survey staff AI familiarity. Identify who has Level 1 experience. Map the team's top 10 recurring tasks by time spent. | Team Lead + AI Champion | Staff AI readiness survey results; Task inventory ranked by hours/week |
| **2** | **Assess** | Select three pilot tasks for AI integration. Choose tasks that are: recurring, time-consuming, document-heavy, and low-risk if errors occur. | Team Lead | List of three pilot tasks with baseline time measurements |
| **3** | **Pilot** | Set up AI tools. Create accounts. Assign one AI Champion to coordinate. Build a starter prompt for each of the three pilot tasks. | AI Champion | Tool access confirmed; Three draft prompts tested |
| **4** | **Pilot** | Run the three pilot tasks using AI. Each pilot task owner runs AI-assisted and manual versions side by side. Document time, quality, and issues. | Pilot Task Owners | Pilot results log: time comparison, quality notes, issues encountered |
| **5** | **Pilot** | Review pilot results with the full team. Discuss what worked, what failed, and what needs adjustment. Revise prompts based on findings. | Team Lead + All Staff | Revised prompts; Lessons learned document |
| **6** | **Build** | Create the team's shared prompt library. Include the three pilot prompts plus any others that team members have developed individually. | AI Champion | Shared prompt library (v1) |
| **7** | **Build** | Build the team knowledge base. Collect legal texts, policy documents, templates, and reference data relevant to the team's mandate. | Assigned Staff + AI Champion | Knowledge base with initial document set |
| **8** | **Build** | Draft team AI SOPs. Cover: review requirements, data handling rules, prompt library usage, and quality checkpoints. | Team Lead + AI Champion | Team AI SOP (v1, 1-2 pages) |
| **9** | **Train** | Conduct a half-day AI workshop for the full team. Cover: basic prompting, the team's prompt library, the knowledge base, and the SOPs. | AI Champion | Workshop completed; All staff trained on team tools |
| **10** | **Expand** | Expand AI use to additional tasks beyond the original three pilots. Each staff member identifies one new task from their workload. | All Staff | Expanded task list with new prompts added to library |
| **11** | **Expand** | Test expanded tasks. Review outputs. Update prompts and SOPs based on new use cases. | Team Lead + AI Champion | Updated prompt library (v2); Updated SOPs |
| **12** | **Measure** | Compile 90-day results. Calculate total time saved, tasks AI-enabled, staff confidence levels, and quality observations. Draft a brief report for the office head. | AI Champion + Team Lead | 90-Day AI Adoption Report |
| **13** | **Decide** | Present results to the office head. Recommend next steps: continue at Level 2, prepare for Level 3, or adjust approach. Request budget for Year 2 if results justify it. | Team Lead | Presentation to office head; Level 3 readiness assessment |

### Critical Success Factors for the 90-Day Plan

The plan above looks straightforward on paper. In practice, five factors determine whether it succeeds or stalls:

1. **The AI Champion must have protected time.** If the champion's regular workload does not decrease, the AI adoption work becomes unpaid overtime. That is not sustainable. The team lead must explicitly reallocate at least 4-6 hours per week during the 90-day period.
2. **Week 5 is the make-or-break moment.** The team reviews pilot results and decides whether to continue. If the pilot tasks were poorly chosen (too complex, too politically sensitive, too dependent on judgment), the results will be underwhelming and momentum will die. Choose your three pilot tasks carefully. Pick tasks where AI can clearly demonstrate value.
3. **The knowledge base requires upfront effort.** Building a knowledge base is not glamorous work. It means collecting, organizing, and formatting documents. The staff member assigned to this task must understand that this foundational work enables everything that follows.
4. **The team lead must attend the Week 5 and Week 9 sessions.** If the team lead delegates these to the AI Champion, the rest of the team interprets this as a signal that AI adoption is not a leadership priority.
5. **The 90-day report must contain numbers.** "We saved time" is not a finding. "We reduced average briefer preparation time from 6 hours to 2.5 hours across 12 briefers" is a finding. Numbers sustain executive support. Impressions do not.

### Adapting the 90-Day Plan

**For smaller offices (under 5 staff):** Compress the Assess phase to one week. Combine the Build and Train phases. Your AI Champion is likely also the Team Lead.

**For larger offices (over 15 staff):** Start with one division as the pilot group. Do not try to onboard the entire ministry at once. Use the pilot division's results to justify and design the ministry-wide rollout.

**For parliamentary committee secretariats:** Align the plan with the parliamentary calendar. Start the Assess phase during recess periods when staff have more capacity. Schedule the Train phase before the next session opens so staff can apply new skills immediately.

**For island province offices (Tawi-Tawi, Sulu, Basilan):** Account for intermittent internet connectivity. Prioritize tools that work offline or with minimal bandwidth. Claude Desktop with a local knowledge base functions without a constant internet connection for many tasks. Build your knowledge base on local storage, not exclusively on cloud platforms.

**For BPDA, DAB, and other attached agencies:** Your mandates are cross-cutting. Build your knowledge base with documents from multiple ministries, not just your own. Your AI-assisted analyses will be more valuable if they draw on the full policy landscape.

See Appendix H for a printable template version of this plan.

---

## 13.6 Change Management: Addressing Resistance and Building Champions

AI adoption fails more often from resistance than from technology. The tools work. The prompts produce results. But people hesitate, resist, or actively undermine adoption for reasons that are entirely human and entirely predictable.

Understanding these resistance patterns — and having ready responses — is the difference between an AI initiative that stalls and one that scales.

### The Six Resistance Patterns in BARMM Government

| Resistance Pattern | What You Hear | Root Cause | Effective Response |
|---|---|---|---|
| **"This will replace my job"** | "AI is going to make us all redundant." "They will use this to cut staff." | Fear of displacement. This is the deepest and most legitimate concern. | Demonstrate that AI handles the tedious parts of the job, not the judgment parts. Show how AI-augmented staff become more valuable, not less. Point to the plantilla vacancies — BARMM has too few staff, not too many.[^8] |
| **"I am too old/not tech-savvy enough"** | "That is for young people." "I cannot even use Excel properly." | Fear of incompetence. Senior staff who have built careers on manual expertise feel threatened by a skill they do not have. | Start them with voice-to-text prompting. Show them that prompting is closer to giving instructions to a staff member than to programming. Pair them with a younger colleague for their first session. |
| **"This is haram/against our values"** | "AI is deception." "Using AI means we are lying about who did the work." | Ethical and religious concern. This is sincere and must be treated with respect. | Refer to Chapter 12 on Islamic principles. Emphasize transparency — disclosing AI use, not hiding it. Frame AI as a tool like a calculator or a search engine. Cite the principle of *maslahah* (public interest): if AI helps serve the Bangsamoro people better, using it responsibly is consistent with Islamic governance values.[^9] |
| **"My supervisor does not support this"** | "My boss does not believe in AI." "They will think I am wasting time." | Lack of institutional permission. The staff member wants to use AI but fears negative consequences from a supervisor who is skeptical or uninformed. | Provide the staff member with data from the pilot results. Offer to brief the supervisor. Frame AI as a tool that makes the supervisor's unit look more productive. See the Supervision Guidebook, Chapter 4, on coaching for development — the supervisor's resistance may signal a coaching opportunity, not a dead end.[^10] |
| **"The output is not good enough"** | "I tried it and it gave me garbage." "AI cannot write like a government employee." | Bad first experience. Usually caused by vague prompts, no context provided, or unrealistic expectations. | Review their prompt. Most bad outputs come from bad prompts. Teach the Four-Step Workflow (Chapter 3). Show them the difference between a one-line prompt and a structured prompt with role, context, task, and format. |
| **"We have more pressing problems"** | "We do not even have enough computers." "Our internet connection cannot handle this." | Infrastructure and resource constraints. This is sometimes a legitimate barrier and sometimes a deflection. | Acknowledge the constraint honestly. Then show that AI works on phones (Claude's mobile interface). Show that prompting requires minimal bandwidth. Identify which tasks can be done offline and which require connectivity. Solve the infrastructure problem separately — do not let it block all progress. |

### The Hidden Seventh Pattern: Passive Compliance

The six patterns above are visible. You hear the resistance. You can respond to it. The seventh pattern is silent and more dangerous: **staff who attend the training, nod along, and never use AI.**

Passive compliance looks like adoption but produces none of the results. The staff member has an account but has not logged in since the workshop. They have access to the prompt library but have not opened it. Their weekly reports contain no mention of AI-assisted tasks.

**How to address passive compliance:**

- **Do not call it out publicly.** Shaming does not produce adoption. It produces resentment.
- **Create low-pressure opportunities.** A "prompt of the week" exercise where every staff member tries one prompt and shares their result in the team chat. No grading. No evaluation. Just practice.
- **Make it practical, not theoretical.** Give the passively compliant staff member a specific task and a specific prompt. "Try this prompt on the report you are working on today. Tell me tomorrow if the output was useful." Remove the friction of figuring out what to try.
- **Track usage, not attitudes.** You cannot measure enthusiasm. You can measure whether someone used AI this week. Focus on the behavior, not the sentiment.

### Building AI Champions

**An AI Champion is a staff member who actively promotes, supports, and teaches AI use within their team.** Every successful AI adoption has at least one. Most successful adoptions have two to three per office.

**Who makes a good AI Champion:**

- **Curious, not necessarily technical.** The best champions are people who like learning new things, not necessarily people with IT backgrounds.
- **Respected by peers.** A champion must be someone whose colleagues trust. If the most technically capable person is also the least collaborative, they are the wrong choice.
- **Positioned in the workflow.** The champion should work on the team's core tasks, not on peripheral functions. When the champion demonstrates AI on the team's bread-and-butter work, the impact is visible to everyone.
- **Willing to teach.** A champion who hoards knowledge is not a champion. They must be willing to sit with a colleague, walk through a prompt, and troubleshoot a bad output.

**What AI Champions do:**

1. **Maintain the team's prompt library.** They add new prompts, retire outdated ones, and version-control changes.
2. **Conduct informal training.** Brown-bag sessions, desk-side coaching, and Viber group tips.
3. **Troubleshoot failures.** When a colleague's AI output fails, the champion reviews the prompt and suggests improvements.
4. **Report results to leadership.** The champion compiles data on time saved, tasks enabled, and quality improvements. This data sustains executive sponsorship.
5. **Stay current.** The champion tracks AI tool updates, new features, and emerging best practices. They bring relevant updates to the team.
6. **Connect with champions in other offices.** AI adoption is happening across BARMM. A champion in MFBM's budget division can learn from a champion in MAFAR's planning division. Encourage cross-office connections. Chapter 14, Section 14.4 covers how to formalize these connections into a community of practice.

### The Executive Sponsor's Role

**The executive sponsor — the ministry head, director, or committee chairperson — does not need to use AI daily.** They need to do four things:

1. **Authorize experimentation.** Say publicly: "I encourage our staff to explore AI tools for their work." This single statement removes the permission barrier for dozens of staff members.
2. **Protect early adopters.** When a staff member's first AI attempt produces a subpar output, the sponsor ensures they are coached, not punished. Innovation requires tolerance for early failures. The Supervision Guidebook calls this the difference between a learning culture and a blame culture.[^11]
3. **Allocate resources.** Approve subscription costs. Allocate staff time for training. Include AI-related expenses in the annual work plan.
4. **Demand results.** After the first 90 days, ask for data. What tasks are faster? What outputs are better? What is the return on the investment? This accountability keeps the initiative focused and credible.

### The Change Management Sequence

The sequence matters. Do not skip steps.

1. **Demonstrate, do not argue.** Show a real BARMM task done with AI and without AI. Side-by-side comparison is more persuasive than any presentation.
2. **Start with the willing.** Do not waste energy converting the most resistant staff member first. Start with the curious ones. Build momentum with early adopters. The resistant will follow when they see results.
3. **Solve a real pain point.** Find the task everyone hates — the one that eats four hours every week and produces no satisfaction. Make that your first AI pilot. When AI eliminates a pain point, resistance drops sharply.
4. **Make it visible.** When the pilot produces results, share them. Post the time saved. Show the before-and-after outputs. Celebrate the team member who had the best prompt this month.
5. **Institutionalize gradually.** Do not mandate AI use on Day 1. Mandate it after the pilot has proven value, the SOPs are written, and the training has been delivered.
6. **Sustain with data.** Every quarter, compile the numbers: hours saved, tasks AI-enabled, quality improvements. Present them to leadership. Data is what keeps the budget flowing and the initiative alive.

### When AI Adoption Fails — and How to Recover

Not every 90-day plan succeeds. Some offices will reach Week 8 and realize they have stalled. The prompt library has three prompts that nobody uses. The knowledge base was built but never updated. The AI Champion was reassigned to a different priority. The team lead stopped attending review sessions.

**Diagnose before you restart.** Ask three questions:

1. **Was the pilot task well chosen?** If the team tried to AI-enable a task that requires deep institutional judgment (e.g., negotiating with stakeholders, resolving inter-agency disputes), the pilot was doomed from the start. Choose a different task — one that is more document-heavy and less judgment-heavy.
2. **Did the AI Champion have protected time?** If the champion was expected to do AI work on top of a full existing workload, burnout is the predictable result. Reallocate time before restarting.
3. **Did leadership show up?** If the team lead did not attend the review sessions, did not ask about results, and did not mention AI in any team meeting, the rest of the staff correctly concluded that this was not a real priority. Fix the leadership signal before fixing the technology.

**To recover:** Do not restart the full 90-day plan. Go back to Week 3 (pilot) with a better-chosen task, a protected champion, and visible leadership engagement. A fresh pilot that succeeds is worth more than a completed plan that produced nothing.

### What This Chapter Has Given You

You now have three maturity levels to assess where you stand. You have quick wins for eight common BARMM roles. You have a day-by-day guide for your first week. You have a team integration framework with shared prompts, knowledge bases, and SOPs. You have an institutional adoption checklist with policy, budget, process integration, and knowledge management requirements. You have a 90-day plan you can start tomorrow. You have a change management playbook that addresses six visible resistance patterns and one hidden one. And you have a recovery protocol for when plans stall.

The tools and prompts from Chapters 1-12 are your arsenal. This chapter is your battle plan.

Chapter 14 addresses the next requirement: building and sustaining the human capacity to make this plan work over time.

---

## Footnotes

[^1]: A formal AI use policy is consistent with the principle of *shura* (consultation) discussed in Chapter 12. The policy should be developed through consultation with staff, not imposed unilaterally. See Section 12.2.3 for the *shura* framework applied to AI deployment decisions.

[^2]: The "Trust but Verify" Protocol is introduced in Chapter 3, Section 3.4. At Level 1, this protocol is entirely self-directed. At Level 2, it becomes a shared team practice.

[^3]: For a detailed prompt library covering the full range of government tasks, see Appendix A (Prompt Library for Common Government Tasks).

[^4]: The Bangsamoro Development Plan 2023-2028 identifies "improving and strengthening governance" as one of six overarching development goals. AI-augmented staff capacity directly supports BDP Goal 5 by enabling existing staff to deliver more effective governance outputs. See Bangsamoro Development Plan 2023-2028, Chapter 5.

[^5]: Republic Act No. 11054 (Bangsamoro Organic Law), Art. VII, Sec. 41. "Public office is a public trust. Public officers and employees shall at all times be accountable to the people." Accountability does not transfer to an AI tool. The officer who submits the work bears full responsibility for its content.

[^6]: These cost estimates are based on published subscription prices for Claude Pro (approximately USD 20/month) and typical Salary Grade 11-15 compensation for BARMM government staff as of 2026. Actual costs vary by office and position.

[^7]: For a full discussion of AI integration into the Bangsamoro budget cycle, see Chapter 6 (AI for Budgeting and Financial Analysis), Section 6.1.

[^8]: As of 2026, many BARMM ministries and offices continue to fill plantilla positions authorized under BAA 13 (Bangsamoro Administrative Code) and BAA 85 (General Appropriations Act, FY 2026). The workforce challenge in BARMM is understaffing, not overstaffing.

[^9]: See Chapter 12, Section 12.2.4 for the *maslahah* (public interest) principle applied to AI adoption. The principle holds that actions which serve the common good and do not contradict Shari'ah are permissible. AI tools that improve government service delivery and transparency serve the public interest.

[^10]: Supervision and Supervisory Development Guidebook for the Bangsamoro Autonomous Region, Chapter 4 (Coaching for Performance and Development). The guidebook provides frameworks for supervisors to develop staff competencies through structured coaching conversations rather than directive mandates.

[^11]: Supervision and Supervisory Development Guidebook for the Bangsamoro Autonomous Region, Chapter 1, Section 1.1. The guidebook frames supervision as service (*amanah*) and establishes that supervisors who create environments where staff can learn from mistakes — rather than fear them — produce higher-performing teams over time.
