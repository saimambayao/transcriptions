# Chapter 6 — AI for Budgeting and Financial Analysis

The Bangsamoro Government manages a budget exceeding PHP 114 billion for FY 2026.[^1] That budget flows through a four-phase cycle — preparation, authorization, execution, and accountability — codified in the Bangsamoro Budget System Act.[^2] Every phase generates documents: budget proposals, committee reports, allotment orders, disbursement authorities, financial accountability reports. Every document contains numbers that must be checked, compared, and explained.

This is where AI earns its place. AI does not make budget decisions. It does not sign allotment orders. But it can compare this year's appropriations against last year's in seconds. It can flag a ministry whose **Personnel Services** allocation exceeds the 45% ceiling. It can draft a budget briefer that would take a staff analyst two days in under two hours. You still verify every number. You still apply judgment. AI handles the volume.

This chapter walks you through the entire budget cycle and shows you exactly where AI enters, what prompts to use, and what to verify before you sign anything.

---

## 6.1 The Bangsamoro Budget Cycle and Where AI Enters

BAA 84 establishes a **planning-programming-budgeting continuum** that links the Bangsamoro Development Plan to annual budget allocations.[^3] The cycle has four distinct phases. Each phase has specific documents, deadlines, and decision points. AI can assist in every phase — but the nature of its assistance changes.

### The Budget Cycle at a Glance

| Phase | Key Activities | Key Documents | BAA 84 Sections | AI Entry Points |
|-------|---------------|---------------|-----------------|-----------------|
| **Preparation** | BBCC sets fiscal strategy; M/O/As submit proposals; MFBM evaluates | Budget Call, Budget Proposals, Budget Priorities Framework, BESF | Secs. 14-25 | Draft proposals, check BDP alignment, compare year-over-year figures |
| **Authorization** | Parliament deliberates GABB; committee reviews; plenary votes | General Appropriations Bill, Committee Reports, Amendments | Secs. 26-33 | Analyze bill provisions, prepare committee briefers, compare proposed vs. prior-year allocations |
| **Execution** | MFBM releases allotments; M/O/As obligate and disburse | GAABAO, SARO, BEDs, Financial Plans, Procurement Plans | Secs. 34-51 | Track obligation rates, flag under-spending, draft quarterly reports |
| **Accountability** | M/O/As submit BFARs; COA audits; Parliament reviews | BFARs, COA Reports, Annual Accomplishment Reports | Secs. 60-67 | Analyze audit findings, compare planned vs. actual performance, draft compliance reports |

The table above is your reference map. Whenever someone assigns you a budget task, locate it in one of these four phases first. The phase determines what documents you need and what kind of AI assistance is appropriate.

---

### 6.1.1 Budget Preparation

Budget preparation begins when the **Bangsamoro Budget Coordinating Committee (BBCC)** presents the Budget Priorities Framework to the Chief Minister and Cabinet in April of each year.[^4] The MFBM then issues the annual **Budget Call**, which prescribes the process, forms, and calendar for all M/O/As to follow.[^5]

**What happens in this phase:**

- The BBCC reviews macroeconomic targets, revenue projections, and expenditure priorities
- M/O/As prepare and submit budget proposals showing organizational outcomes, performance indicators, and cost estimates
- **Budget Endorsing Authorities** review and endorse proposals for compliance with technical standards
- The MFBM evaluates proposals against six criteria: alignment with the Chief Minister's priority agenda, past performance, implementation readiness, program convergence, available funding sources, and other MFBM criteria[^6]
- The Chief Minister submits the **Proposed Bangsamoro Budget** to Parliament by September 30[^7]

**Where AI enters:**

Use AI to **draft budget proposals** that link each program, activity, and project (P/A/P) to the Bangsamoro Development Plan. BAA 84 explicitly requires this linkage.[^8] Feed the AI your ministry's mandate, the BDP 2023-2028 goals, and your proposed P/A/Ps. Ask it to draft the narrative justification showing how each P/A/P advances specific BDP strategies.

Use AI to **compare your current proposal against prior-year budgets**. Paste your proposed figures alongside last year's enacted amounts. The AI can calculate percentage changes, flag items that increased or decreased by more than 20%, and draft explanations for significant variances.

Use AI to **check compliance with the Budget Priorities Framework**. The framework mandates that the highest budgetary priority go to education, health, and social services. It also requires that at least 5% of each M/O/A's appropriation be allocated for **gender-responsive programs**.[^9] Ask the AI to scan your proposal and verify these requirements are met.

> **Sample Prompt — Budget Proposal Drafting:**
>
> ```
> You are a budget analyst for [Ministry Name] in the Bangsamoro Government.
>
> Draft a budget proposal narrative for FY [Year] that covers:
> 1. Organizational outcomes and performance indicators
> 2. Linkage of each P/A/P to the BDP 2023-2028 (specify which
>    BDP goal and strategy each P/A/P supports)
> 3. Estimated expenditures by allotment class (PS, MOOE, CO)
>    with comparative data for the preceding and current fiscal years
> 4. Brief description of major thrusts and priority programs
>
> Use the following data:
> [Paste your ministry's proposed programs, prior-year figures, and
> relevant BDP goals]
>
> Follow BAA 84, Section 19 requirements for budget proposals.
> Do not fabricate figures. Mark any estimate without a source as
> [ESTIMATE - VERIFY].
> ```

---

### 6.1.2 Budget Authorization

Authorization begins when the Chief Minister submits the Proposed Bangsamoro Budget to Parliament. The **General Appropriations Bill of the Bangsamoro (GABB)** must be filed and calendared for first reading within five calendar days. The committee must submit its report within 60 calendar days from referral. Plenary debate and amendments must conclude within 30 calendar days after that.[^10]

**What happens in this phase:**

- The Committee on Finance, Budget and Management (CFBM) conducts detailed review
- Members of Parliament examine ministry-by-ministry appropriations
- Committee hearings produce questions, amendments, and recommendations
- The plenary debates and votes on the GABB
- The enacted budget becomes the **General Appropriations Act of the Bangsamoro (GAAB)**

**Where AI enters:**

Use AI to **prepare committee briefers** for each ministry's budget. Feed the AI the ministry's proposed budget, its prior-year appropriations, and its accomplishment reports. Ask for a comparative analysis highlighting significant changes and questions for the committee to raise during hearings. Section 6.4 below gives you the full template.

Use AI to **analyze proposed amendments**. When a Member of Parliament proposes shifting PHP 50 million from one P/A/P to another, feed the amendment text and the original appropriation to the AI. Ask it to identify what programs would be affected, whether the amendment complies with BAA 84's prohibition against increasing total appropriations,[^11] and what downstream effects the shift would have.

Use AI to **draft committee reports**. After hearings conclude, the committee must submit a formal report. The AI can organize hearing notes, witness testimonies, and member concerns into a structured committee report with findings and recommendations.

---

### 6.1.3 Budget Execution

Once the GAAB takes effect, it serves as the **allotment order** (GAABAO) authorizing M/O/As to obligate Personnel Services and MOOE.[^12] Items requiring additional documentation are released through **Special Allotment Release Orders (SAROs)**. M/O/As must submit **Budget Execution Documents (BEDs)** before funds are released.[^13]

**What happens in this phase:**

- The GAABAO authorizes M/O/As to begin obligating funds
- M/O/As submit Financial Plans, Physical Plans, Monthly Disbursement Programs, and Annual Procurement Plans
- The MFBM issues Notices of Cash Allocation for disbursement
- M/O/As implement their programs, incur obligations, and make payments
- Quarterly allotment periods guide the release schedule (January, April, July, October)[^14]

**Where AI enters:**

Use AI to **track obligation and disbursement rates**. Feed the AI your monthly or quarterly financial data alongside your targets. Ask it to calculate absorption rates, identify under-spending patterns, and flag P/A/Ps at risk of reverting unobligated allotments at year-end.

Use AI to **draft allotment modification requests**. BAA 84 allows modifications within an activity or project (approved by the Minister or Head of Office) and between allotment classes or operating units (approved by MFBM).[^15] The AI can draft the justification memo explaining why the modification is needed and demonstrating compliance with the rules.

Use AI to **prepare the Budget Execution Documents**. The four required BEDs — Financial Plan, Physical Plan, Monthly Disbursement Program, and Annual Procurement Plan — follow standardized formats. Give the AI your P/A/P data and ask it to populate each template. Verify the figures before submission.

---

### 6.1.4 Budget Accountability

Accountability runs throughout the year but culminates in year-end reporting. M/O/As must submit **Budget and Financial Accountability Reports (BFARs)** showing the status of appropriations, allotments, obligations, disbursements, and unexpended balances.[^16] The COA conducts external audits. Parliament reviews performance through its committees.[^17]

**What happens in this phase:**

- M/O/As prepare and submit periodic BFARs to the MFBM
- The MFBM consolidates financial reports for the Chief Minister, Parliament, and COA
- The COA audits financial accounts of all M/O/As and BGOCCs
- M/O/As submit annual accomplishment reports to Parliament covering work and financial results
- Parliament holds M/O/As accountable for financial and non-financial performance

**Where AI enters:**

Use AI to **analyze BFARs for anomalies**. Feed the AI a ministry's quarterly BFAR data. Ask it to identify items where obligations significantly exceed or fall short of allotments, flag unusual disbursement patterns, and compare current-period performance against the same period in prior years.

Use AI to **summarize COA audit findings**. COA reports are dense and technical. The AI can extract the key findings, classify them by severity (material vs. immaterial, recurring vs. first-time), and draft management responses that address each finding point by point.

Use AI to **prepare annual accomplishment reports**. Feed the AI your ministry's physical and financial targets alongside actual accomplishments. Ask it to calculate performance rates, explain variances, and present the data in the format Parliament prescribes.

---

## 6.2 AI-Assisted Budget Proposal Development

A budget proposal under BAA 84 requires more than a table of numbers. Section 19 mandates that proposals include **organizational outcomes, performance indicators, linkage to the BDP and BDIP, estimated expenditures with comparative data, descriptions of priority programs, staffing patterns, and any other information the MFBM requires**.[^18]

Most budget analysts spend the bulk of their preparation time on two tasks: compiling comparative figures and writing narrative justifications. AI accelerates both.

### Building the Comparative Table

Start by organizing your data into three columns: **prior-year actual, current-year enacted, and proposed**. Break each column into the three standard allotment classes: Personnel Services (PS), Maintenance and Other Operating Expenses (MOOE), and Capital Outlays (CO).

> **Sample Prompt — Year-Over-Year Budget Comparison:**
>
> ```
> I am preparing a budget proposal for [Ministry Name] for FY [Year].
>
> Here are the figures:
>
> FY 2025 Actual:
> - PS: [amount]
> - MOOE: [amount]
> - CO: [amount]
> - Total: [amount]
>
> FY 2026 Enacted (BAA 85):
> - PS: [amount]
> - MOOE: [amount]
> - CO: [amount]
> - Total: [amount]
>
> FY 2027 Proposed:
> - PS: [amount]
> - MOOE: [amount]
> - CO: [amount]
> - Total: [amount]
>
> Create a comparison table with:
> 1. Absolute amounts for all three years
> 2. Year-over-year change (amount and percentage)
> 3. PS as a percentage of total for each year
> 4. A flag for any line item that changed by more than 15%
> 5. A brief narrative explaining each significant change
>
> Use Philippine peso formatting. Do not round below thousands.
> ```

### Writing the BDP Linkage Narrative

BAA 84 requires all budget proposals to **explicitly state their linkage to the approved BDP and BDIP**.[^19] This means every P/A/P must trace back to a BDP goal, strategy, or program. The AI can draft this linkage if you provide both the P/A/P descriptions and the relevant BDP chapter.

Feed the AI your proposed P/A/Ps and the BDP 2023-2028 goal that your ministry serves. Ask it to map each P/A/P to a specific BDP strategy and output. Review the mapping carefully — the AI may link a program to a plausible but incorrect BDP strategy. Your professional knowledge of your ministry's mandate is the verification layer.

### Checking the 45% PS Ceiling

The BOL imposes a hard ceiling: **total appropriations for Personal Services shall not exceed 45% of the total revenue sources of the Bangsamoro Government**.[^20] This is a constitutional-level constraint. Feed the AI your ministry's PS figure and the total budget. Ask it to calculate the ratio and compare it against this ceiling. For the FY 2026 budget, the BTA Parliament's total PS across all M/O/As must stay within this limit as applied to the consolidated Bangsamoro revenue.

---

## 6.3 Budget Analysis and Comparison

Budget analysis is one of the most AI-ready tasks in government. The work is pattern-based: compare numbers, calculate changes, identify trends, and present findings. AI excels at all four.

### Year-Over-Year Analysis

The most common budget analysis compares the current year against prior years. For FY 2026, BAA 85 appropriated **PHP 114,077,644,141.90** across all M/O/As.[^21] A committee analyst examining this budget needs to know: How does this compare to FY 2025? Which ministries received the largest increases? Which programs were cut? Where did priorities shift?

Feed the AI both years' appropriation tables. Ask it to produce:

1. **A ranked list of M/O/As by budget increase** (both absolute and percentage)
2. **A ranked list of M/O/As by budget decrease**
3. **PS/MOOE/CO distribution** for each M/O/A across both years
4. **Special Purpose Fund changes** — particularly the Contingent Fund, SDF, and Quick Response Fund

> **Sample Prompt — GAA Comparative Analysis:**
>
> ```
> You are a budget analyst for the Bangsamoro Parliament's Committee
> on Finance, Budget and Management.
>
> I will provide you with two datasets:
> 1. BAA [Prior Year Number] - GAA for FY [Prior Year]
> 2. BAA 85 - GAA for FY 2026
>
> Produce a comparative analysis that includes:
>
> A. Total budget comparison (prior year vs. current year, absolute
>    and percentage change)
> B. Top 10 M/O/As by budget increase (amount and percentage)
> C. Top 10 M/O/As by budget decrease (amount and percentage)
> D. PS/MOOE/CO breakdown for each M/O/A, both years, with the PS
>    share highlighted if it exceeds 60% of the M/O/A's total
> E. Special Purpose Funds comparison (Contingent Fund, SDF, QRF,
>    IMPACT, and others)
> F. Key observations and questions for committee hearings
>
> Present findings in tables with Philippine peso formatting.
> Flag any ministry where PS growth exceeds overall budget growth
> by more than 10 percentage points.
> ```

### PS/MOOE/CO Breakdown Analysis

The three-way split between Personnel Services, Maintenance and Other Operating Expenses, and Capital Outlays reveals a ministry's spending priorities. A ministry with 80% PS and 5% CO is spending almost everything on salaries and almost nothing on infrastructure or equipment. This is not always wrong — a regulatory office may legitimately be staff-intensive — but it deserves scrutiny.

Ask the AI to calculate the **PS/MOOE/CO ratio** for every M/O/A and rank them. Look for:

- **Ministries where PS exceeds 70%** of total appropriation — these may need scrutiny for staffing efficiency
- **Ministries where CO dropped to zero or near-zero** — this signals possible capital investment gaps
- **Ministries where MOOE grew sharply** — check whether this reflects new programs or routine cost escalation

### Cross-Ministry Comparison

Use AI to compare ministries serving similar populations or mandates. How does MBHTE's budget per student compare to MOH's budget per health facility? These cross-ministry comparisons help Parliament assess whether resource allocation matches stated priorities.

> **Sample Prompt — Cross-Ministry Budget Comparison:**
>
> ```
> You are a budget analyst for the Bangsamoro Parliament.
>
> I will provide the FY 2026 appropriations for:
> 1. Ministry of Health (MOH)
> 2. Ministry of Social Services and Development (MSSD)
> 3. Ministry of Basic, Higher and Technical Education (MBHTE)
>
> These three ministries serve the "highest budgetary priority" areas
> under BAA 84, Section 17 (education, health, social services).
>
> Produce a comparison that includes:
> A. Total appropriation for each ministry
> B. Combined share of total GAAB (are education, health, and social
>    services actually receiving the highest priority?)
> C. Per-capita spending estimate (use BARMM population of approximately
>    4.4 million)
> D. PS/MOOE/CO ratio for each ministry
> E. Year-over-year growth rate for each ministry vs. the overall
>    budget growth rate
> F. Key observation: Does the budget allocation pattern reflect the
>    "highest budgetary priority" mandate?
>
> Present findings in a single comparison table plus 5 bullet-point
> observations. Philippine peso formatting.
> ```

### Special Purpose Fund Analysis

The GAAB contains several **Special Purpose Funds** that fall outside individual ministry budgets. Under BAA 84, these include the Contingent Fund, the Special Development Fund, Statutory Shares of Constituent LGUs, the Local Government Support Fund, and others approved by Parliament.[^31] The FY 2026 GAAB also includes the Personnel Gratuity Fund, Miscellaneous Personnel Benefits Fund, Quick Response Fund, IMPACT (Infrastructure Modernization and Public Asset Construction and Transformation), and the Sustainable Assistance Mechanism for Local Moral Governance.[^32]

Use AI to track SPF allocations across fiscal years. Ask it to calculate each SPF as a percentage of the total GAAB and flag any fund that grew or shrank disproportionately. Pay special attention to the **Contingent Fund**, which BAA 84 caps at 10% of total GAAB.[^33] Verify that the enacted GAAB respects this ceiling.

---

## 6.4 Preparing Budget Briefers with AI

A **budget briefer** is the primary decision-support document during budget authorization. Committee chairs, Members of Parliament, and senior staff rely on it to understand a ministry's budget request, challenge questionable items, and propose amendments.

The structure below follows the CSW format adapted for budget work. See the *Bill Drafting Manual for the Bangsamoro Parliament*, Chapter 9, for the full legislative process context that budget briefers support.[^22]

### Budget Briefer Structure

| Section | Content | AI Role |
|---------|---------|---------|
| I. Overview | Ministry mandate, organizational structure, key functions | Draft from ministry charter and enabling law |
| II. Budget Summary | Total appropriation by PS/MOOE/CO with year-over-year comparison | Calculate and format from raw data |
| III. Major Programs | Description and cost of top P/A/Ps with BDP linkage | Draft descriptions, verify BDP alignment |
| IV. Personnel Profile | Filled vs. unfilled positions, PS growth trends, average salary levels | Analyze plantilla data, calculate ratios |
| V. Performance Assessment | Prior-year targets vs. accomplishments, obligation rates, disbursement rates | Calculate performance rates from BFARs |
| VI. Key Issues | Under-spending, audit findings, delayed projects, unfunded mandates | Synthesize COA reports and BFAR data |
| VII. Questions for Hearings | Specific questions for the committee to raise with ministry officials | Generate from analysis of Sections II-VI |
| VIII. Recommended Actions | Suggested committee position — approve, reduce, or amend | Draft options with supporting rationale |

> **Sample Prompt — Full Budget Briefer:**
>
> ```
> You are a senior legislative analyst preparing a budget briefer for
> the Committee on Finance, Budget and Management of the Bangsamoro
> Parliament.
>
> Ministry: [Name]
> Fiscal Year: [Year]
>
> I am providing:
> 1. The ministry's proposed budget for FY [Year] (by P/A/P and
>    allotment class)
> 2. The enacted budget for FY [Prior Year] (same breakdown)
> 3. The ministry's most recent BFAR (showing obligations and
>    disbursements against the current-year budget)
> 4. Key COA audit findings from the most recent audit report
>
> Draft a budget briefer with eight sections:
> I. Overview — ministry mandate and key functions (2 paragraphs)
> II. Budget Summary — table showing PS/MOOE/CO for both years,
>     with absolute and percentage changes
> III. Major Programs — top 5 P/A/Ps by appropriation size, with
>      BDP linkage and year-over-year comparison
> IV. Personnel Profile — filled vs. unfilled positions, PS share
>     of total budget, PS growth rate vs. total budget growth rate
> V. Performance Assessment — obligation rate, disbursement rate,
>    key physical targets vs. accomplishments
> VI. Key Issues — list the top 5 budget concerns based on the data
> VII. Questions for Hearings — draft 10 specific questions the
>      committee chair should ask the minister
> VIII. Recommended Actions — 3 options (approve as proposed,
>       approve with specific reductions, approve with conditions)
>
> Use formal but clear language. Philippine peso formatting.
> Mark any figure you cannot verify as [UNVERIFIED].
> ```

### Verifying the Briefer

After the AI generates the briefer, apply these checks:

1. **Verify every number** against the source documents. The AI may transpose digits, misread allotment classes, or calculate percentages incorrectly.
2. **Check the PS ceiling** — confirm the ministry's PS does not push the consolidated BARMM PS above 45% of total revenue sources.
3. **Verify BDP linkages** — confirm the AI mapped programs to the correct BDP goals. Cross-check against the BDP 2023-2028 text.
4. **Review hearing questions** — remove questions that are politically sensitive, already answered in the budget documents, or based on AI assumptions rather than data.
5. **Test the recommendations** — each recommended action should follow logically from the analysis. If the briefer identifies chronic under-spending but recommends approval without conditions, the logic is broken.

---

## 6.5 Revenue Analysis and Fiscal Forecasting

The Bangsamoro Government draws revenue from multiple sources defined in the Bangsamoro Organic Law. Understanding these sources — their legal basis, relative size, and growth trajectory — is essential for any analyst working on budget policy, fiscal strategy, or development planning.

### Revenue Sources Under the BOL

Article XII of the Bangsamoro Organic Law enumerates twelve categories of revenue sources.[^23] The table below organizes them with their legal basis and relevance to AI-assisted analysis:

| Revenue Source | BOL Provision | Description | AI Analysis Potential |
|---------------|--------------|-------------|----------------------|
| **Taxes** | Art. XII, Sec. 6(a) | Regional taxes levied by Parliament | Trend analysis of collection rates |
| **Fees and Charges** | Art. XII, Sec. 6(b) | Regulatory and service fees | Revenue forecasting from historical data |
| **Annual Block Grant** | Art. XII, Secs. 6(c), 15-18 | 5% of net national internal revenue (BIR + BOC) | Projection based on national revenue trends |
| **Natural Resource Revenues** | Art. XII, Sec. 6(d) | Shares from exploration, development, utilization | Commodity price correlation analysis |
| **75% Tax Share** | Art. XII, Secs. 6(e), 10-13 | National taxes collected within BARMM | Collection efficiency analysis |
| **GOCC Dividends** | Art. XII, Sec. 6(f) | Dividends from government-owned corporations | Portfolio performance tracking |
| **Economic Convention Grants** | Art. XII, Sec. 6(g) | Revenues from economic agreements | Agreement term analysis |
| **Grants and Foreign Assistance** | Art. XII, Sec. 6(h) | ODA, donations, endowments | Grant pipeline tracking |
| **Loans and ODA** | Art. XII, Sec. 6(i) | Official development assistance | Debt service ratio monitoring |
| **Public Utility Revenues** | Art. XII, Sec. 6(j) | Shares from utilities in BARMM | Utility performance benchmarking |
| **National Government Allocations** | Art. XII, Sec. 6(k) | Appropriations beyond the block grant | Historical allocation tracking |
| **Quarry Resource Tax** | Art. XII, Sec. 6(l) | Up to 10% of fair market value per cubic meter | Volume and pricing analysis |

In addition to these recurring sources, the **Special Development Fund** provides PHP 5 billion per year for ten years (PHP 50 billion total) for rebuilding, rehabilitation, and development of conflict-affected communities.[^24] The SDF is established under Article XIV, Section 2 of the BOL — not Article XII.

### The Block Grant: The Dominant Revenue Source

The **annual block grant** is the single largest revenue source for the Bangsamoro Government. It equals 5% of the net national internal revenue tax collection of the Bureau of Internal Revenue and the net collection of the Bureau of Customs, calculated from the third fiscal year preceding the current budget year.[^25]

For AI-assisted fiscal forecasting, this formula matters. The block grant for any given year depends on national revenue performance three years prior. Feed the AI the BIR and BOC collection data from the relevant base years. Ask it to:

1. **Calculate the expected block grant** using the BOL formula
2. **Project future block grants** based on historical national revenue growth rates
3. **Assess risk scenarios** — what happens to the Bangsamoro budget if national revenue collections decline by 5%, 10%, or 15%?
4. **Track the gap** between the block grant formula amount and actual appropriations in the national GAA

> **Sample Prompt — Block Grant Projection:**
>
> ```
> You are a fiscal analyst for the Bangsamoro Planning and
> Development Authority.
>
> The BOL (RA 11054, Art. XII, Sec. 16) provides that the annual
> block grant equals 5% of the net national internal revenue tax
> collection of the BIR plus the net collection of the BOC from the
> third fiscal year preceding the current budget year.
>
> Here are the national revenue figures:
> [Paste BIR and BOC net collection data for relevant years]
>
> Calculate:
> 1. The formula-based block grant for FY [Year]
> 2. Block grant projections for the next 3 fiscal years using
>    [X]% annual revenue growth
> 3. Three scenarios: base case ([X]% growth), optimistic
>    ([X+2]% growth), pessimistic ([X-3]% growth)
> 4. The PS ceiling (45% of total revenue sources) under each
>    scenario
>
> Present results in a table with Philippine peso formatting.
> Show your calculations. Note any assumptions.
> ```

### Revenue Diversification Analysis

The BOL grants the Bangsamoro Government the **power to create its own sources of revenue** and levy taxes, fees, and charges.[^26] But the Revenue Code — one of the seven priority codes mandated by the BOL — remains unenacted.[^27] This means the BARMM currently relies heavily on the block grant and national transfers rather than own-source revenue.

Use AI to analyze the **revenue mix** over time. Feed the AI multi-year revenue data (if available from BFARs or the BESF). Ask it to calculate:

- **Block grant dependency ratio** — block grant as a percentage of total revenue
- **Own-source revenue growth rate** — are regional taxes and fees growing faster or slower than the block grant?
- **Comparison with other autonomous or subnational governments** — how does BARMM's revenue mix compare to ARMM's historical revenue mix or to other subnational entities in the Philippines?

This analysis supports the BBCC's fiscal policy work and informs Parliament's deliberations on revenue legislation.

### Fiscal Risk Scenario Modeling

BAA 84 allows the Bangsamoro Government to **deviate from medium-term fiscal objectives** in cases of major natural disaster, severe economic shock, or other significant unforeseeable events.[^30] The BBCC must disclose deviations and corrective measures in the Annual Fiscal Report.

AI can help you prepare for these scenarios before they happen. Feed the AI your current fiscal position — total revenue by source, total expenditure by allotment class, outstanding obligations, and cash reserves. Then ask it to model:

- **Revenue shortfall scenario:** What happens if the block grant is delayed by one quarter? Which M/O/As would need to reduce spending first?
- **Emergency expenditure scenario:** A major natural disaster requires PHP 2 billion in immediate response. Where do funds come from? How much can the Contingent Fund and Quick Response Fund cover?
- **Personnel cost escalation scenario:** If a new compensation law increases PS by 15%, how does this affect the 45% PS ceiling? What MOOE and CO programs would need to be cut?

These scenarios do not predict the future. They prepare your office to respond faster when fiscal disruptions occur. The AI drafts the scenario analysis; your team validates the assumptions and presents the options to the BBCC.

> **Sample Prompt — Fiscal Risk Scenario:**
>
> ```
> You are a fiscal risk analyst for the MFBM.
>
> Current fiscal position:
> - Total GAAB: PHP [amount]
> - Block grant component: PHP [amount] ([X]% of total)
> - Own-source revenue: PHP [amount] ([X]% of total)
> - Contingent Fund: PHP [amount]
> - Quick Response Fund: PHP [amount]
>
> Model three scenarios:
>
> Scenario 1 — Block Grant Delay: The national government delays
> Q3 block grant release by 60 days. Identify which M/O/As face
> immediate cash flow problems based on their Monthly Disbursement
> Programs. Propose a cash rationing plan.
>
> Scenario 2 — Major Disaster: An earthquake requires PHP 2 billion
> in emergency response. Calculate how much the Contingent Fund
> and QRF can cover. Identify which P/A/Ps could be suspended to
> declare savings under BAA 84, Sec. 46.
>
> Scenario 3 — PS Ceiling Breach: A 15% PS increase is legislated.
> Calculate the new PS total. Determine if it breaches the 45%
> ceiling under BOL Art. XII, Sec. 20(a). Propose adjustments.
>
> Present each scenario with: trigger, immediate impact, available
> fiscal tools, recommended actions, and legal basis under BAA 84.
> ```

---

## 6.6 Audit Preparation and COA Compliance

The Commission on Audit is the **exclusive external auditor** of the Bangsamoro Government.[^28] Every M/O/A and BGOCC must have its financial accounts audited by the COA. The audit findings carry legal weight — they can trigger disallowances, suspensions, and charges against responsible officials.

### Understanding COA Audit Reports

COA audit reports follow a standard structure: management letter, audit observations, recommendations, and the status of prior-year findings. Each observation is classified by severity and nature (financial, compliance, or performance). The most common findings in government agencies involve:

- **Unliquidated obligations** — obligations incurred but not settled within the prescribed period
- **Cash advances** not liquidated within the reglementary period
- **Procurement irregularities** — failure to follow RA 12009 (New Government Procurement Act) procedures
- **Unreconciled accounts** — differences between agency records and COA records
- **Non-submission of reports** — failure to submit BFARs or other required reports on time

### Using AI for COA Audit Preparation

**Before the audit**, use AI to conduct a **pre-audit self-assessment**. Feed the AI your financial records, obligation registers, and disbursement journals. Ask it to identify potential audit findings before the COA examiner arrives.

> **Sample Prompt — Pre-Audit Self-Assessment:**
>
> ```
> You are an internal auditor for [M/O/A Name] in the Bangsamoro
> Government.
>
> I am providing the following data for FY [Year]:
> 1. Summary of obligations incurred by quarter
> 2. Summary of disbursements by quarter
> 3. List of cash advances and their liquidation status
> 4. List of procurement transactions over PHP 1 million
> 5. Prior-year COA audit findings and our management responses
>
> Conduct a pre-audit assessment:
> A. Identify obligations that remain unliquidated beyond the
>    Extended Payment Period
> B. Flag cash advances not liquidated within the reglementary
>    period
> C. Check if prior-year audit findings have been fully addressed
>    (compare our management responses against actual actions taken)
> D. Identify potential compliance issues based on the data patterns
> E. Draft a management action plan addressing each identified risk
>
> Use BAA 84 provisions on budget execution (Secs. 34-51) and
> accountability (Secs. 60-67) as the compliance framework.
> Flag any item requiring immediate attention as [URGENT].
> ```

### Responding to COA Findings

After receiving COA audit observations, M/O/As must submit **management comments** addressing each finding. AI can draft these responses, but you must verify every factual claim. A management response that misrepresents the status of corrective actions creates more problems than the original finding.

Feed the AI the specific COA observation and your supporting documents (e.g., evidence that the finding has been corrected, timeline for pending corrections, or justification for why the finding is not applicable). Ask it to draft a response that:

1. **Acknowledges** the finding (never argue with a COA observation unless you have clear legal basis)
2. **Explains** the root cause
3. **Details** corrective actions already taken
4. **Commits** to a timeline for completing remaining actions
5. **Provides** supporting documentation references

### BAA 84 Enforcement Provisions

Budget staff should know the enforcement provisions because they define the consequences of non-compliance. BAA 84 establishes five categories of liability:[^29]

| Violation | BAA 84 Section | Consequence |
|-----------|---------------|-------------|
| **Illegal certification of fund availability** | Sec. 71 | Grave offense; joint and several liability for full amount |
| **Illegal expenditures** | Sec. 72 | Null and void; grave offense; joint and several liability |
| **Incurrence of overdraft** | Sec. 73 | Less grave offense; personal liability |
| **Fraudulent accountability reports** | Sec. 74 | Administrative and criminal sanctions |
| **Failure to submit reports or comply with transparency** | Sec. 75 | Automatic salary suspension; withholding of allotments |

AI cannot protect you from these consequences. But it can help you **identify compliance risks before they become audit findings**. Build a compliance checklist based on these provisions and run it against your financial data quarterly.

---

> ### Case Study: AI-Assisted Analysis of BAA 85 (FY 2026 GAA)
>
> **The task:** A committee analyst is assigned to prepare a comparative budget briefer for the Committee on Finance, Budget and Management before plenary deliberation of the FY 2026 budget.
>
> **The approach:**
>
> 1. **Context preparation** (30 minutes): The analyst gathers the full text of BAA 85, the prior-year GAA, each ministry's accomplishment report, and the most recent BFARs. She uploads these to her AI tool.
>
> 2. **First prompt** (5 minutes): She asks the AI to produce a ministry-by-ministry comparison table showing FY 2025 vs. FY 2026 appropriations by PS/MOOE/CO, with percentage changes and flags for items exceeding 20% change.
>
> 3. **AI output** (3 minutes): The AI generates a 15-page comparative table. The total FY 2026 appropriation is PHP 114,077,644,141.90. The BTA Parliament receives PHP 7,257,475,847.00. The Ministry of Health receives the largest operational budget among line ministries. Capital Outlays for the Ministry of Public Works dominate the CO category.
>
> 4. **Verification** (2 hours): The analyst checks every figure against the source documents. She catches two transposition errors in the MOOE figures for MILG. She corrects the AI's classification of the Special Development Fund — the AI had placed it under the OCM budget rather than as a Special Purpose Fund.
>
> 5. **Second prompt** (5 minutes): She asks the AI to generate 10 hearing questions for each of the top 5 ministries by budget size, focusing on under-spending patterns, unfilled positions, and unresolved COA findings.
>
> 6. **Third prompt** (5 minutes): She asks the AI to draft the "Key Issues" section, highlighting ministries with obligation rates below 70% in the prior year and programs with no capital outlay allocation despite infrastructure mandates.
>
> 7. **Final output** (1 hour to finalize): The analyst reviews, corrects, and finalizes a 25-page budget briefer. Total time: approximately 4 hours. Without AI, this analysis would have taken 3-4 working days.
>
> **Lessons:**
>
> - **AI saved 70% of the drafting time** but required 2 hours of verification
> - **The AI made two factual errors** — both caught during verification
> - **The hearing questions were the highest-value output** — the AI generated questions the analyst had not considered, based on patterns in the data
> - **The analyst's domain knowledge was indispensable** for correcting the SDF classification error — the AI did not know the GAAB's internal structure well enough to distinguish SPFs from ministry budgets

---

## Chapter Summary

The Bangsamoro budget cycle generates an enormous volume of documents at every phase — from budget proposals in April to COA audit responses the following year. AI does not change the cycle. It accelerates the document work that drives each phase.

Here is what you can do immediately:

- **During preparation:** Use AI to draft budget proposals that comply with BAA 84, Section 19 requirements and link every P/A/P to the BDP
- **During authorization:** Use AI to prepare eight-section budget briefers that give committee chairs the analysis they need for hearings
- **During execution:** Use AI to track obligation rates, flag under-spending, and draft allotment modification justifications
- **During accountability:** Use AI to conduct pre-audit self-assessments and draft management responses to COA findings
- **For revenue analysis:** Use AI to project block grant levels, analyze revenue diversification, and model fiscal scenarios

Every output requires human verification. The Rule of Signature from Chapter 3 applies here with full force: if your name goes on the budget briefer, you verify every number.

The next chapter takes you into the legislative process — where the budget becomes law and where AI assists in drafting, analyzing, and tracking the bills that shape Bangsamoro governance.

---

## Footnotes

[^1]: BAA 85, Sec. 1. The total appropriation for FY 2026 is PHP 114,077,644,141.90, drawn from the annual block grant, other subsidies, national tax shares, regional collections, and prior-year appropriations.

[^2]: Bangsamoro Autonomy Act No. 84, "An Act Prescribing a Budget System for the Bangsamoro Government" (Bangsamoro Budget System Act of 2025), enacted December 9, 2025. BAA 84 governs the preparation, authorization, execution, and accountability of the Bangsamoro budget.

[^3]: BAA 84, Sec. 16 (Planning-Investment-Programming-Budgeting Continuum). Budget priorities shall be based on regional development strategies in the approved BDP.

[^4]: BAA 84, Sec. 17 (Budget Priorities Framework). The BBCC shall present the framework to the Chief Minister and Cabinet in April of each year.

[^5]: BAA 84, Sec. 18 (Annual Budget Preparation Process). The MFBM, through the Bangsamoro Budget Office, prescribes the budget preparation process and calendar in the annual Budget Call.

[^6]: BAA 84, Sec. 21 (Budget Evaluation). The six evaluation criteria are: (a) relationship with the Chief Minister's priority agenda; (b) past performance vis-a-vis target spending; (c) implementation readiness; (d) program convergence; (e) all sources and authorized uses of funds; and (f) other criteria as determined by the MFBM.

[^7]: BAA 84, Sec. 23 (The Proposed Bangsamoro Budget). The Chief Minister shall submit the Proposed Bangsamoro Budget to Parliament as far as practicable not later than the 30th of September of each year.

[^8]: BAA 84, Sec. 16, par. 2: "All budget proposals for P/A/Ps shall explicitly state their linkage to the approved BDP and BDIP."

[^9]: BAA 84, Sec. 17, par. 2. The highest budgetary priority shall be given to education, health, and social services. At least 5% of each M/O/A and BGOCC's total appropriation shall be set aside for gender-responsive programs following a gender and development plan.

[^10]: BAA 84, Sec. 26 (Schedule of Budget Consideration). The GABB shall be filed and calendared for first reading within 5 calendar days from budget submission. The committee report is due within 60 calendar days from referral. Plenary debate and amendments must conclude within 30 calendar days from submission of the committee report.

[^11]: BAA 84, Sec. 31 (Prohibition Against the Increase of Appropriations): "The Parliament shall, in no case, increase the total budget appropriations proposed by the Chief Minister."

[^12]: BAA 84, Sec. 36 (GAABAO). Upon effectivity, the GAAB serves as the allotment order authorizing M/O/As and BGOCCs to obligate PS and MOOE, subject to certain exceptions.

[^13]: BAA 84, Sec. 38 (Budget Execution Documents). M/O/As must submit BEDs at the onset of each budget execution phase: Financial Plan, Physical Plan, Monthly Disbursement Program, and Annual Procurement Plan.

[^14]: BAA 84, Sec. 37(b). Each calendar year is divided into four quarterly allotment periods beginning on the 1st day of January, April, July, and October.

[^15]: BAA 84, Sec. 49 (Rules on Modification of Allotments). Ministers or Heads of Office may approve changes within an activity or project. The MFBM approves transfers between allotment classes, between operating units, modifications within SPFs, and Magna Carta benefit payments.

[^16]: BAA 84, Sec. 61 (Submission of BFARs). Each M/O/A shall report the status of appropriations, allotments, obligations, disbursements, unliquidated obligations, and unexpended balances.

[^17]: BAA 84, Sec. 65 (Annual Report on Accomplishments to the Parliament). M/O/As and BGOCCs shall submit annual reports covering work and financial results. Parliament monitors efficiency and effectiveness through its committees.

[^18]: BAA 84, Sec. 19 (Budget Proposal). The required contents include: organizational outcomes, performance indicators, BDP/BDIP linkage, estimated expenditures with comparative data, program descriptions, staffing patterns, and other MFBM-required information.

[^19]: BAA 84, Sec. 16, par. 2.

[^20]: Republic Act No. 11054 (BOL), Art. XII, Sec. 20(a). Total PS appropriations for one fiscal year shall not exceed 45% of total revenue sources. Salaries for public utility and economic enterprise employees are excluded from this computation.

[^21]: BAA 85, Sec. 1.

[^22]: The *Bill Drafting Manual for the Bangsamoro Parliament* (Mambayao, 2026), Chapter 9 (The Budget Process), provides the legislative process context within which budget briefers operate.

[^23]: Republic Act No. 11054 (BOL), Art. XII, Sec. 6 (Sources of Revenues). Twelve categories enumerated from (a) through (l).

[^24]: Republic Act No. 11054 (BOL), Art. XIV, Sec. 2 (Special Development Fund). PHP 50 billion at PHP 5 billion per year for 10 years from ratification.

[^25]: Republic Act No. 11054 (BOL), Art. XII, Sec. 16 (Block Grant Amount). The base year is the third fiscal year immediately preceding the current fiscal year.

[^26]: Republic Act No. 11054 (BOL), Art. XII, Sec. 6.

[^27]: Republic Act No. 11054 (BOL), Art. XII, Sec. 14 (Bangsamoro Tax and Revenue Code). The Parliament is mandated to enact this code. As of the current transition period, it remains pending.

[^28]: BAA 84, Sec. 67 (Exclusive External Auditor): "The financial accounts of M/O/As and BGOCCs shall continue to be audited by the COA, which shall serve as the exclusive external auditor of the Bangsamoro Government."

[^29]: BAA 84, Secs. 71-75 (Enforcement provisions under Title VII).

[^30]: BAA 84, Sec. 11 (Deviations from Fiscal Objectives).

[^31]: BAA 84, Sec. 28 (Special Purpose Funds).

[^32]: BAA 85, Table of Contents (Special Purpose Funds section): Personnel Gratuity Funds, Miscellaneous Personnel Benefits Fund, Contingent Fund, Special Development Fund, Sustainable Assistance Mechanism for Local Moral Governance, Bangsamoro Support Fund to Judiciary, Quick Response Fund, and IMPACT.

[^33]: BAA 84, Sec. 29, par. 3: "In no case shall the Contingent Fund exceed ten percent (10%) of the total GAAB."
