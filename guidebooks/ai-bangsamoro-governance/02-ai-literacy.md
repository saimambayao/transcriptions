# Chapter 2 — AI Literacy for Government Staff

You do not need a computer science degree to use AI. You need the same skill you already use every day: the ability to give clear instructions and evaluate what comes back. This chapter strips AI down to plain language, shows you exactly how these tools work, and walks you through your first government prompt. By the end, you will understand what AI can do, what it cannot do, and how to talk about it with confidence.

---

## 2.1 What Is AI, in Plain Language

**Artificial intelligence** is software that finds patterns in massive amounts of text and uses those patterns to generate new text. That is it. No magic, no consciousness, no thinking — just pattern matching at an enormous scale.

The specific type of AI you will use in government work is called a **large language model**, or LLM. An LLM is trained by reading billions of pages of text — books, articles, laws, reports, websites, and documents from every field. During training, the software learns which words tend to follow other words. It learns that "Bangsamoro Autonomous Region in Muslim Mindanao" is a real phrase. It learns that budget documents have specific structures. It learns that legal provisions follow particular patterns.

**Think of an LLM as a pattern machine.** It does not understand meaning the way you do. It predicts what text should come next based on patterns it learned during training.

Here is an analogy. You have a colleague who has read every government document ever produced in the Philippines. Every BAA, every Republic Act, every policy paper, every memorandum. This colleague has a perfect memory for phrases and structures. If you ask them to "draft a memorandum requesting budget realignment," they can produce something that looks exactly right — because they have seen thousands of similar documents.

But this colleague has a limitation. They do not actually understand budget policy. They cannot tell you whether a realignment is legal under BAA 84.[^1] They can produce text that *looks* correct, but you must verify whether it *is* correct. They are a drafting machine, not a policy expert.

That is what an LLM is. A very fast, very well-read drafting machine that needs a human expert — you — to verify its output.

### What Makes LLMs Different from Search Engines

A **search engine** finds existing documents that match your query. You type "BAA 13 Section 3," and Google shows you pages that contain those words.

An **LLM** generates new text based on your instructions. You type "Summarize the key principles in BAA 13 Section 3 as bullet points," and the AI writes a summary that did not exist before. The summary is not copied from a single source. It is assembled from patterns the AI learned during training.

This distinction matters. Search gives you what already exists. AI gives you something new — which means it can also give you something wrong. Every AI output requires human verification.

### Why "Artificial Intelligence" Is a Misleading Name

The word "intelligence" suggests thinking. LLMs do not think. They calculate probabilities. When you ask an AI to "explain the Bangsamoro Organic Law," it is not reasoning about constitutional law. It is predicting which sequence of words is most likely to follow that instruction, based on millions of documents it processed during training.

The practical consequence: **AI can produce confident-sounding text that is completely wrong.** It has no way to distinguish between true statements and plausible-sounding fabrications. Only you can do that.

---

## 2.2 How AI Reads, Writes, and Reasons

Understanding three concepts will make you a better AI user than 90% of people who use these tools daily.

### 2.2.1 Input and Output

Every AI interaction follows one pattern: **you provide input, and the AI returns output.**

**Input** is everything you give the AI before it generates a response:
- Your written instruction (called a **prompt**)
- Any documents you paste or upload
- Previous messages in the same conversation

**Output** is whatever the AI generates in response:
- A drafted document
- A summary of a long report
- A table comparing two pieces of legislation
- An answer to a question

**Government analogy:** Input is the assignment memo you give to a staff member — the task description, the background documents, the deadline, the format requirements. Output is the draft they hand back. The clearer your assignment memo, the better the draft. The same is true for AI.

### 2.2.2 Context Windows: The AI's Desk Space

Every AI tool has a **context window** — a maximum amount of text it can hold in a single conversation. Think of the context window as the AI's desk space.

A small desk holds one short document. A large desk holds dozens of files spread out side by side. When the desk is full, new documents push old ones off the edge. The AI can only work with what fits on its desk at that moment.

**Practical numbers as of 2026:**

| AI Tool | Context Window | Rough Equivalent |
|---------|---------------|-----------------|
| ChatGPT (free tier) | ~8,000 tokens | ~15 pages of text |
| Claude (standard) | ~200,000 tokens | ~400 pages of text |
| Claude (extended) | ~1,000,000 tokens | ~2,000 pages of text |
| Gemini (standard) | ~128,000 tokens | ~250 pages of text |

A **token** is roughly three-quarters of a word. The phrase "Bangsamoro Autonomous Region in Muslim Mindanao" is about 8 tokens.

**What this means for your work:**

- If you paste a 50-page bill into an AI tool with a small context window, the AI might lose track of early sections by the time it reaches the end.
- If you are working with a large context window, you can paste the full text of BAA 13 (the Bangsamoro Administrative Code) alongside three other BAAs and ask the AI to compare them.
- When a conversation gets very long, the AI may "forget" instructions you gave at the beginning. Start a new conversation when this happens.

**Government analogy:** The context window is like the physical desk of a government employee. A provincial office clerk with a small desk can only work on one file at a time. A legislative analyst with a large conference table can spread out multiple bills, committee reports, and reference documents simultaneously. The more desk space, the more the worker can cross-reference.

### How Context Windows Affect Your BARMM Work

Here are practical scenarios showing why context window size matters:

**Scenario A — Small context window (15 pages).** You paste Section 3 of BAA 13 and ask the AI to explain each principle. This works. The text fits easily on the desk.

**Scenario B — Medium context window (250 pages).** You paste the full text of BAA 49 (Bangsamoro Local Governance Code), BAA 13 (Bangsamoro Administrative Code), and the relevant BOL articles. You ask the AI to identify where the two codes overlap or contradict each other. This works because all three documents fit on the desk simultaneously.

**Scenario C — Large context window (2,000 pages).** You paste fifteen BAAs covering health infrastructure (BAAs 21, 25-30, 73-74, 76, 78-80), the BDP health chapter, and the MOH organizational structure.[^1] You ask the AI to map every hospital upgrade authorized by law, its province, its bed capacity, and its current Level designation. This works because the entire reference set fits on the desk.

**Scenario D — Overloaded.** You try to paste all 89 BAAs into a tool with a 15-page context window. The tool cannot hold them. It either rejects the input, silently drops the older content, or processes only the last few pages. The output will be incomplete and unreliable.

**The practical rule:** Before you paste documents into an AI tool, estimate the total page count. Match it to the tool's capacity. If the documents do not fit, narrow your selection to the most relevant sections.

### 2.2.3 Hallucinations: When AI Makes Things Up

**Hallucination** is the technical term for when an AI generates information that sounds correct but is fabricated. This is the single most dangerous behavior of AI tools for government work.

Examples of AI hallucinations in a BARMM context:

- The AI cites "BAA 91, Section 14" — but only 89 BAAs have been enacted.[^2]
- The AI names a "Deputy Minister Rashid Adiong of MFBM" — but that person does not hold that position.[^3]
- The AI quotes "Article XII, Section 5 of the BOL" and provides text that looks real but does not match the actual provision.
- The AI states that a specific budget allocation "amounted to PHP 2.3 billion" with no source — and the real figure is different.

**Why does this happen?** The AI does not access a database of facts. It predicts plausible text. If the pattern of "BAA [number], Section [number]" appears frequently in its training data, it will generate new combinations that fit the pattern — even if those combinations do not correspond to real laws.

**The rule:** Treat every AI output the way you treat an unverified intelligence report. It might be accurate. It might be partially accurate. It might be entirely fabricated. You verify before you use it.

Three verification habits that prevent hallucination damage:

1. **Cross-check every citation.** If the AI cites a BAA, open the actual BAA text and confirm the section exists and says what the AI claims.
2. **Verify every name and title.** If the AI mentions an official, check the current BARMM officials directory.[^3]
3. **Question confident specifics.** When the AI provides exact numbers, dates, or budget figures without you providing a source, treat those as suspect until verified.

---

## 2.3 Types of AI Tools for Government Work

AI is not a single tool. It is a category of tools, each suited to different tasks. This section maps the four categories most relevant to BARMM government operations.

### AI Tool Categories for BARMM Government Work

| Category | What It Does | Government Application | Example Tools (2026) |
|----------|-------------|----------------------|---------------------|
| **Text Generation** | Writes new text based on instructions | Drafting memoranda, legislative briefers, policy papers, correspondence | Claude, ChatGPT, Gemini |
| **Document Analysis** | Reads and summarizes long documents | Reviewing proposed bills, comparing BAA provisions, extracting key points from BDP chapters | Claude, NotebookLM, ChatGPT |
| **Research Synthesis** | Combines information from multiple sources into structured findings | Legislative research, policy comparison across jurisdictions, preparing background papers for committee hearings | NotebookLM, Gemini Deep Research, Claude |
| **Translation** | Converts text between languages | English-to-Filipino correspondence, Filipino-to-English reports, Arabic protocol greetings | Claude, Google Translate, ChatGPT |

### 2.3.1 Text Generation

**Text generation** is the most common AI use case for government staff. You describe what you need, and the AI writes a first draft.

**BARMM examples:**

- **Routine correspondence.** "Draft a transmittal letter from the Office of the Chief Minister to the Speaker of the Parliament, forwarding the proposed budget for FY 2027 for parliamentary consideration."
- **Meeting summaries.** Paste raw meeting notes and ask the AI to organize them into a structured summary with action items, responsible offices, and deadlines.
- **First-draft memoranda.** "Draft a memorandum from MFBM to all ministry budget officers, reminding them of the FY 2027 budget submission deadline and listing the required attachments per BAA 84."[^1]
- **Speech preparation.** "Prepare a 5-minute opening statement for a committee hearing on the proposed education amendments, highlighting three key issues."

**What text generation does well:** Produces structured documents quickly, follows templates, maintains consistent tone and formatting, and handles high-volume drafting tasks.

**What text generation does poorly:** Verifying facts, making policy judgments, understanding local political context, and knowing which information is current versus outdated.

**Time savings:** A routine transmittal letter that takes 30 minutes to draft manually takes 3 minutes with AI — plus 5 minutes for your review and corrections. A first-draft legislative briefer that takes a full day drops to 2-3 hours. The time savings come from drafting speed, not from skipping review.

### 2.3.2 Document Analysis

**Document analysis** is the second most valuable AI capability for government operations. You give the AI a document — or several documents — and ask it to extract, compare, or summarize information.

**BARMM examples:**

- **Bill review.** Upload a proposed bill and ask: "Identify every section that creates a new government body. For each body, list its name, composition, and functions."
- **Legal comparison.** Paste two versions of an amendment and ask: "List every difference between Version A and Version B, organized by section number."
- **Budget analysis.** Upload the GAA and ask: "Create a table showing the appropriation for each ministry, sorted from highest to lowest."
- **Provision extraction.** Paste BAA 13 Section 3 and ask: "List each declared principle and policy as a separate bullet point, with a one-sentence explanation in plain language."

**Why this matters for BARMM:** The Bangsamoro Transition Authority has enacted 89 BAAs, many of which cross-reference and amend each other.[^2] BAA 14 amends BAA 3. BAA 33 amends BAA 23. BAA 37 amends BAA 13. BAA 70 amends BAA 54. BAA 77 amends BAA 58. Manually tracking these amendment chains across hundreds of pages is time-consuming and error-prone. AI can scan multiple documents simultaneously and flag connections a human reader might miss.

**Practical tip:** When analyzing a bill or BAA, always paste the **full text** of the document, not just the section you are interested in. AI performs better when it can see the complete structure — definitions, scope, implementing provisions, and repealing clauses — rather than a fragment.

### 2.3.3 Research Synthesis

**Research synthesis** goes beyond single-document analysis. It combines findings from multiple sources into a coherent summary with citations.

**BARMM examples:**

- **Committee hearing preparation.** Load the proposed bill, relevant existing BAAs, the BOL provisions on the subject, and the BDP chapter on the sector. Ask the AI to produce a briefing paper that maps the proposal against existing law and development goals.
- **Cross-jurisdictional comparison.** Ask the AI to compare how BARMM, ARMM, and the Cordillera Administrative Region handle a specific governance issue.
- **Development tracking.** Load multiple quarterly reports and ask the AI to identify trends, gaps, and progress against BDP 2023-2028 targets.[^4]

**Key limitation:** Research synthesis is only as good as the sources you provide. If you give the AI incomplete documents, its synthesis will have gaps. If you give it outdated documents, its findings will be outdated. **The AI does not know what it does not have.** You must ensure the source documents are complete and current.

**A tool worth knowing: NotebookLM.** Google's NotebookLM is a free research synthesis tool that excels when you have specific source documents and need the AI to stay strictly within those sources.[^8] You upload your PDFs, and NotebookLM only draws from what you uploaded — reducing hallucination risk. For BARMM staff preparing committee hearing briefers, this means uploading the proposed bill, the relevant BAAs, and the BOL chapters, then asking NotebookLM to synthesize findings. The outputs still need human review, but the source-grounded approach produces more reliable first drafts than general-purpose AI tools.

### 2.3.4 Translation

**Translation** serves a practical need across BARMM, where government operations use English, Filipino, and Arabic.

**BARMM examples:**

- **Official correspondence.** Translate a Filipino memorandum into English for national agency submission, or translate English committee reports into Filipino for broader distribution.
- **Islamic greetings and protocols.** Generate proper Arabic greetings for official documents, with transliteration and English translation.
- **Public communications.** Translate policy announcements from English into Filipino to reach a wider audience.

**Limitations:** AI translation handles standard Filipino and English well. It struggles with regional languages (Tausug, Maguindanaon, Maranao), colloquial expressions, and specialized Islamic legal terminology. For sensitive translations involving Shari'ah concepts or indigenous people's rights, always have a qualified human translator review the AI output.

---

## 2.4 The Prompt as a Government Instruction

A **prompt** is the instruction you type into an AI tool. Prompting is not a technical skill. It is the same skill you use when you write an assignment memo, a terms of reference, or a CSW tasking order.

**Government analogy:** A prompt is an assignment memo for AI.

Compare these two assignment memos:

**Vague memo (bad):**
> "Please prepare something about the budget."

**Clear memo (good):**
> "Prepare a 3-page summary of BAA 85 (GAA FY 2026) showing the total appropriation per ministry. Present the data in a table sorted from highest to lowest allocation. Include a paragraph comparing the top 3 ministries' allocations to FY 2025 levels. Submit by Friday. The audience is the Committee on Appropriations."

The second memo produces better work because it specifies **what** to produce, **how** to format it, **who** the audience is, and **what** scope to cover. AI prompts work exactly the same way.

### The Five Elements of a Good Government Prompt

Every effective prompt contains most or all of these five elements:

| Element | What It Does | Example |
|---------|-------------|---------|
| **Role** | Tells the AI what perspective to adopt | "You are a legislative analyst for the Bangsamoro Parliament" |
| **Task** | Describes exactly what you need | "Summarize the key provisions of this bill" |
| **Format** | Specifies the output structure | "Present as numbered bullet points, one per section" |
| **Context** | Provides background information | "This bill amends BAA 49 (Bangsamoro Local Governance Code)" |
| **Constraints** | Sets boundaries on what the AI should not do | "Do not add information beyond what is in the bill text. Mark any gaps as [INFORMATION NEEDED]" |

You do not need all five elements for every prompt. A simple request — "Summarize this document in 10 bullet points" — only needs Task and Format. But complex government tasks benefit from all five.

### Common Government Tasks Mapped to Prompt Elements

| Government Task | Key Prompt Elements | Example Prompt Opening |
|----------------|--------------------|-----------------------|
| Draft a transmittal letter | Role + Task + Format | "You are an executive assistant in the Office of the Chief Minister. Draft a transmittal letter..." |
| Summarize a proposed bill | Task + Format + Constraints | "Summarize this proposed bill in 10 bullet points. One bullet per section. Do not add analysis..." |
| Compare two BAA versions | Task + Context + Format | "I am providing two versions of an amendment to BAA 49. Create a comparison table showing every difference..." |
| Prepare talking points | Role + Task + Context + Format | "You are a legislative staff member preparing the committee chair for a hearing on PB 312. Draft 5 talking points..." |
| Simplify legal text | Role + Task + Constraints | "You are a government trainer. Rewrite this BOL provision in plain language a high school graduate can understand. Do not change the legal meaning." |

### The Iterative Prompting Method

One prompt rarely produces a perfect output. Experienced AI users follow an iterative method:

1. **First prompt:** Give the AI the task with your source documents. Accept that the first output will be 60-70% of what you need.
2. **Second prompt:** Point out specific problems. "The third bullet point is wrong — BAA 49 does not cover barangay elections. Correct this." Specific feedback produces better revisions than vague feedback like "make it better."
3. **Third prompt:** Request final formatting adjustments. "Add the section numbers in parentheses after each bullet. Change the heading to match our standard memo format."

This iterative approach mirrors how you already work with staff. You assign a task, review the draft, provide corrections, and receive a revised version. The difference is speed: each AI revision cycle takes seconds, not days.

### Before and After: A BOL Provision Example

Suppose you need to explain Article V, Section 2 of the Bangsamoro Organic Law to a non-lawyer colleague. Here is the actual BOL text:

> **Section 2.** *Powers of Government.* — The Bangsamoro Government shall have the authority to exercise its powers over its internal affairs and territorial jurisdiction as provided in this Organic Law. The Bangsamoro Government shall have the power to create its own sources of revenue and to levy taxes, fees, and charges that shall accrue exclusively to the Bangsamoro Government, in accordance with this Organic Law.[^5]

**Before (weak prompt):**

> "Explain this section."

**AI output from weak prompt:**
> "This section provides that the Bangsamoro Government has authority over internal affairs and territorial jurisdiction as established by the Organic Law. It also has the power to create revenue sources and levy taxes."

This output is technically accurate but useless — it restates the provision without simplifying it.

**After (strong prompt):**

> "You are a government trainer explaining the BOL to new BARMM employees who have no legal background. Rewrite this provision in plain Filipino-English (Taglish), using a concrete example. Maximum 5 sentences. Do not change the legal meaning."

**AI output from strong prompt:**
> "Ang BARMM ay may sariling kapangyarihang mamahala sa loob ng kanyang teritoryo — hindi na kailangan humingi ng permission sa national government para sa internal affairs. Kasama rito ang power na gumawa ng sariling sources of revenue. For example, the Bangsamoro Parliament can pass a law creating a regional business tax na mapupunta directly sa BARMM coffers, hindi sa national treasury. This is different from ordinary regions na umaasa lang sa IRA o national tax share. The legal basis is the BOL itself — Republic Act 11054."

The strong prompt produced a practical explanation with a concrete example. The difference was not AI capability — it was prompt quality.

---

## 2.5 Hands-On: Your First Government Prompt

This section walks you through a real exercise. You will use AI to summarize BAA 13, Section 3 — the Declaration of Principles and Policies of the Bangsamoro Administrative Code.[^6]

### What You Need

- Access to any AI text tool (Claude, ChatGPT, or Gemini — all will work)
- The text of BAA 13, Section 3 (provided below)
- 10 minutes

### The Source Text

BAA 13, Section 3 declares eleven principles and policies that serve as the foundation of the Bangsamoro Administrative Code. The full text reads:

> **Sec. 3. Declaration of Principles and Policies.** — The Bangsamoro Government hereby declares the following principles and policies as the basic foundation of the Code:
>
> a. The Bangsamoro Autonomous Region in Muslim Mindanao is an autonomous regional government with asymmetrical relationship with the Republic of the Philippines and shall be parliamentary in form. Its political system is democratic, and all government authority resides in the people...
>
> b. The Bangsamoro Government recognizes and protects the customs and traditions, beliefs, and cultures of its indigenous inhabitants...
>
> c. The Bangsamoro Government recognizes the vital role of women and youth, and the valuable contributions of differently abled persons in nation-building...
>
> d. The Bangsamoro Government shall ensure every citizen in its territorial jurisdiction the provision of the basic necessities and equal opportunities in life...
>
> e. The Bangsamoro Government shall promote unity, peace, justice, and goodwill among all peoples...
>
> f. The Bangsamoro Government, its offices, agencies, including GOCCs shall ensure full respect for human rights...
>
> g. The Bangsamoro Government shall ensure the autonomy of its constituent local government units (LGUs)...
>
> h. The Bangsamoro Government shall develop a self-reliant and independent regional economy...
>
> i. The Bangsamoro Government shall encourage the participation of non-governmental, community-based, and sectoral organizations in government affairs...
>
> j. The Bangsamoro Government, in pursuit of moral governance, shall maintain honesty, integrity, transparency and accountability...
>
> k. Subject to reasonable conditions prescribed by law, the Bangsamoro Government adopts and implements a policy of full public disclosure of all its transactions involving public interest.

*(The full verbatim text of each principle is in the enacted BAA 13. The above excerpts show the opening clause of each.)*

### Step-by-Step Walkthrough

**Step 1: Open your AI tool.**

Open Claude (claude.ai), ChatGPT (chat.openai.com), or Gemini (gemini.google.com) in your browser. Create a new conversation.

**Step 2: Paste the source text.**

Copy the full text of BAA 13, Section 3 from your reference copy. Paste it into the chat. (If you have the full BAA 13 document, paste the entire Section 3 — all eleven principles with their complete text.)

**Step 3: Write your prompt.**

Type the following prompt after the pasted text:

```
You are a BARMM government trainer preparing a handout for new employees.

Task: Summarize each of the 11 principles in BAA 13, Section 3
in one sentence of plain language. No legal jargon.

Format:
- Numbered list (1-11)
- Each item: [Letter] — [One-sentence plain language summary]
- Add a short label for each principle (e.g., "Democratic Governance",
  "Indigenous Peoples' Rights")

Constraints:
- Do not add principles that are not in the source text
- Do not change the legal meaning
- Use language a high school graduate can understand
```

**Step 4: Review the output.**

The AI will generate something like this:

> 1. **(a) Democratic Governance** — BARMM is a self-governing region within the Philippines, with a parliamentary system where power comes from the people.
> 2. **(b) Indigenous Peoples' Rights** — The government protects the customs, traditions, and cultures of indigenous communities and shields them from discrimination.
> 3. **(c) Women, Youth, and PWD Participation** — Women, youth, and persons with disabilities play vital roles in building the region and the government supports their well-being.
> 4. **(d) Social Justice** — Every citizen deserves basic necessities and equal opportunities, with social justice applied across all aspects of life.
> 5. **(e) Peace and Unity** — The government promotes peace, justice, and goodwill, and supports the peaceful resolution of disputes.
> 6. **(f) Human Rights** — All government offices, agencies, and GOCCs must respect human rights in every plan, program, and activity they carry out.
> 7. **(g) Local Government Autonomy** — Provinces, cities, municipalities, and barangays keep their autonomy, and their existing privileges under the Local Government Code are not reduced.
> 8. **(h) Economic Self-Reliance** — The government develops a regional economy that is self-reliant and serves the needs of the Bangsamoro people.
> 9. **(i) Civil Society Participation** — NGOs, community organizations, and sectoral groups are encouraged to participate in government affairs.
> 10. **(j) Moral Governance** — The government commits to honesty, integrity, transparency, accountability, and active measures against corruption.
> 11. **(k) Full Public Disclosure** — All government transactions involving public interest are subject to full public disclosure.

**Step 5: Verify the output.**

Go through each summary and check it against the original text:

- Does summary (a) accurately capture the "asymmetrical relationship" concept? If the AI omitted this detail, you can ask it to add it.
- Does summary (g) correctly state that LGU privileges "shall not be diminished"? If the AI softened this language, you can request a correction.
- Did the AI add a 12th principle that does not exist in the source? If yes, delete it.

**Step 6: Refine.**

Give the AI specific feedback:

```
Good draft. Two corrections:
1. Item (a) should mention the "asymmetrical relationship" with the
   national government — this is a defining feature of BARMM.
2. Item (g) should explicitly state that privileges under RA 7160
   "shall not be diminished" — this is stronger than "are not reduced."

Please revise only these two items.
```

The AI will revise only those items and keep the rest unchanged.

### What You Just Learned

In 10 minutes, you:

1. **Prepared context** by gathering the source text
2. **Wrote a clear prompt** using Role, Task, Format, and Constraints
3. **Reviewed the output** against the source document
4. **Refined with specific feedback** instead of starting over

This is the same four-step cycle used for every AI task in government — from simple summaries to complex legislative briefers. The complexity of the prompt changes. The process does not.

### Variations to Try

Once you complete the basic exercise, try these variations to build your prompting skills:

**Variation 1 — Different audience.** Change the Role line to: "You are a barangay captain explaining BARMM governance to community members." Notice how the AI adjusts its language and examples.

**Variation 2 — Different format.** Change the Format to: "Create a two-column table. Column 1: Principle letter and label. Column 2: Plain language explanation in one sentence." Notice how format instructions change the output structure.

**Variation 3 — Comparative analysis.** Paste BAA 13, Section 3 alongside Article II, Section 1 of the 1987 Philippine Constitution (Declaration of Principles and State Policies). Add this prompt: "Compare the BARMM principles in BAA 13, Section 3 with the national principles in Article II of the Constitution. Identify which BARMM principles mirror national principles and which are unique to the Bangsamoro." This introduces multi-document analysis — a skill you will use frequently in legislative work.

**Variation 4 — Translation.** Take the AI's output from the basic exercise and add: "Translate this summary into Filipino. Keep the principle labels in English." This tests the AI's bilingual capability and shows you the translation quality you can expect.

Each variation takes 5 minutes. After completing all four, you will have practiced single-document analysis, format control, comparative analysis, and translation — the four most common AI tasks in government work.

### Choosing the Right Tool for the Task

You now know four AI tool categories. The question is: which one should you use for a given task? Here is a decision guide:

**Use Text Generation when:**
- You need a first draft of a document (memo, letter, briefer, speech)
- You have a clear template or format in mind
- The task is primarily about writing, not analysis

**Use Document Analysis when:**
- You have a long document and need specific information extracted
- You need to identify patterns, gaps, or inconsistencies in a single document
- You want to convert unstructured text into a structured format (tables, bullet lists)

**Use Research Synthesis when:**
- You need to combine findings from multiple documents
- You are preparing background research for a committee hearing or policy decision
- You need to compare provisions across different laws or BAAs

**Use Translation when:**
- You need to convert between English, Filipino, or Arabic
- You want to produce bilingual versions of official documents
- You need to simplify technical language into accessible explanations

Many tasks combine categories. A legislative briefer, for example, requires document analysis (reading the proposed bill), research synthesis (comparing it to existing law), and text generation (writing the briefer). You can do all three in a single AI conversation by working through each stage sequentially.

---

## 2.6 Common Misconceptions and How to Address Them

Every new technology carries misconceptions. AI has more than most because the name itself — "artificial intelligence" — implies capabilities the technology does not have. Here are the six most common misconceptions among government staff, what the reality actually is, and how to respond when colleagues raise them.

### Misconceptions vs. Reality

| # | Misconception | Reality | How to Respond |
|---|--------------|---------|---------------|
| 1 | "AI understands what I mean" | AI predicts the next most probable word based on patterns. It does not understand meaning, context, or intent. It processes text — it does not comprehend it. | "AI is a pattern machine, not a thinking machine. It predicts words, like autocomplete on your phone — just far more sophisticated. We must still tell it exactly what we need." |
| 2 | "AI will replace government employees" | AI replaces *tasks*, not *people*. A legislative analyst who uses AI does not become unnecessary — they become faster. The analyst still makes judgments, verifies facts, and applies professional expertise the AI lacks. No AI can attend a committee hearing, build relationships with stakeholders, or navigate political realities. | "AI replaces the drafting, not the drafter. You still decide, verify, and sign. AI handles the typing. You handle the thinking." |
| 3 | "AI output is always accurate" | AI regularly fabricates information — fake citations, wrong names, non-existent laws, and invented statistics. The technical term is **hallucination**. Every AI output must be verified against source documents before use in any official capacity. | "AI is like a very confident intern who never says 'I don't know.' Always check the output against the actual documents." |
| 4 | "Using AI is cheating" | AI is a tool, like a calculator or a word processor. A budget officer who uses a spreadsheet formula is not "cheating" at math. A legislative analyst who uses AI to draft a first version of a briefer is not "cheating" at analysis — they are working more efficiently. What matters is the quality and accuracy of the final product, not which tool produced the first draft. | "We do not say a carpenter is cheating because they use a power saw instead of a handsaw. AI is a power tool for knowledge work." |
| 5 | "AI is too complicated for me" | If you can write a clear assignment memo, you can use AI. Prompting requires the same skills as writing a CSW tasking order: state what you need, provide background documents, specify the format, and set boundaries. You already practice these skills daily. | "You write assignment memos every week. A prompt is the same thing — just addressed to software instead of a staff member." |
| 6 | "Whatever AI produces can be submitted as-is" | No AI output should go directly from the tool to a decision-maker without human review. AI drafts contain errors, uses generic language, misses BARMM-specific terminology (writing "DSWD" instead of "MSSD," "DepEd" instead of "MBHTE"), and may fabricate citations.[^7] The **Rule of Signature** applies: if your name goes on the document, you verified every line. | "Would you sign a letter written by a new staff member without reading it? Treat AI output the same way." |
| 7 | "I need to learn programming to use AI" | Text-based AI tools like Claude, ChatGPT, and Gemini work through natural language — plain English or Filipino. You type instructions in the same language you use for emails and memoranda. There is no code, no command line, and no technical syntax required. | "If you can type an email, you can use AI. You write instructions in plain language. The AI reads them and responds." |
| 8 | "AI has access to our internal files" | Standard AI tools (Claude, ChatGPT, Gemini) do not have access to your computer, your email, your internal databases, or any BARMM systems. They only process what you paste or upload into the conversation. They cannot search government servers or access classified information unless you provide it. | "AI only sees what you show it. It cannot access iGovPhil, your email, or internal files. You control what goes in." |

### A Note on Data Sensitivity

Misconception #8 deserves special attention. While AI tools do not access your internal files, the reverse is also true: **anything you paste into an AI tool leaves your computer.** When you paste the text of a draft bill into ChatGPT or Claude, that text is transmitted to external servers for processing.

**What this means for BARMM staff:**

- **Public documents** (enacted BAAs, published BOL text, official budget documents) can be safely pasted into AI tools. These are already public.
- **Draft documents** (unreleased bills, internal memoranda, pre-decisional policy papers) require caution. Check your office policy before pasting confidential drafts into external AI tools.
- **Personnel data** (employee records, performance evaluations, disciplinary actions) should never be pasted into external AI tools.
- **Security-sensitive information** (peace process negotiations, security assessments, intelligence reports) must never be processed through external AI tools.

When in doubt, ask: "Would I email this document to someone outside the Bangsamoro Government?" If the answer is no, do not paste it into an AI tool. Chapter 12 of this guidebook covers data governance and ethical considerations in full detail.

### Addressing Misconceptions in the Workplace

When colleagues express these misconceptions, respond with the **concrete example method** rather than theoretical explanations:

- **Do not say:** "AI uses transformer architecture with attention mechanisms to predict token sequences." Nobody cares.
- **Do say:** "Let me show you. Give me a task you are working on right now. I will use AI to draft a first version in 3 minutes. Then you tell me what it got right and what it got wrong."

A live demonstration converts skeptics faster than any explanation. The most effective way to address misconceptions is to let colleagues watch AI produce useful output — and then watch you catch and correct its mistakes. Both parts matter. They see the speed. They also see that human review is non-negotiable.

### The Three-Sentence Explanation

When a senior official or a colleague asks "What is AI?", use this three-sentence explanation:

> **"AI is software that reads massive amounts of text and learns patterns. When you give it instructions, it generates new text based on those patterns — like a very fast drafter who has read every document ever written. But it does not understand what it writes, so we always verify the output before using it."**

This explanation is accurate, jargon-free, and honest about the limitation. Memorize it. You will use it often.

---

## Key Takeaways

1. **AI is a pattern machine.** Large language models predict text based on patterns learned from billions of pages. They do not understand, think, or reason. They generate plausible text.

2. **Context windows are desk space.** The more documents you can fit in the AI's context window, the better it can cross-reference and compare. But every tool has a limit.

3. **Hallucinations are real and dangerous.** AI fabricates citations, names, and statistics. Every output must be verified against source documents before use in any official document.

4. **Four tool categories serve government work.** Text generation, document analysis, research synthesis, and translation each serve different needs. Match the tool to the task.

5. **A prompt is an assignment memo.** The same skills you use to write clear CSW tasking orders — Role, Task, Format, Context, Constraints — produce effective AI prompts.

6. **Misconceptions block adoption.** Address them with live demonstrations, not lectures. Show colleagues what AI can do, then show them how you catch its mistakes.

7. **Data sensitivity requires judgment.** Public documents can be safely processed through AI tools. Draft documents, personnel data, and security-sensitive information require caution or should never be entered into external AI tools. When in doubt, apply the email test: if you would not email it outside the Bangsamoro Government, do not paste it into an AI tool.

8. **Start simple, build gradually.** Your first AI task should be a basic summary or document extraction — not a 13-section legislative briefer. Master the four-step cycle (Prepare, Prompt, Review, Refine) on simple tasks before applying it to complex ones.

The next chapter takes these foundations and puts them to work. You will learn a repeatable four-step workflow for using AI in any government task, directly connected to the ADDRESS IT framework for Complete Staff Work.

---

## Footnotes

[^1]: Bangsamoro Autonomy Act No. 84, "Bangsamoro Budget System Act of 2025," establishes the legal framework for the BARMM budget cycle, including preparation, authorization, execution, and accountability. MFBM (Ministry of Finance, Budget, and Management) serves as the primary fiscal authority for the Bangsamoro Government.

[^2]: As of March 2026, the Bangsamoro Transition Authority Parliament has enacted 89 Bangsamoro Autonomy Acts (BAAs). BAA numbers cited in any document should be verified against the official BAA index maintained by the Bangsamoro Parliament Secretariat. See the BAA Quick-Reference Index in the reference materials of this guidebook.

[^3]: Official names and titles of BARMM officials should always be verified against current official directories. The BTA membership and ministerial appointments are updated periodically. A verified BARMM officials reference is maintained separately and should be consulted before finalizing any document that names government personnel.

[^4]: The 2nd Bangsamoro Development Plan (BDP) 2023-2028 establishes six development goals, eight strategies, and sector-specific targets for the Bangsamoro Autonomous Region. The BDP is the authoritative reference for development planning, program design, and budget alignment in BARMM.

[^5]: Republic Act No. 11054, "An Act Providing for the Organic Law for the Bangsamoro Autonomous Region in Muslim Mindanao," Article V, Section 2. The BOL's 18 Articles define the full powers, structure, and fiscal framework of the Bangsamoro Government.

[^6]: Bangsamoro Autonomy Act No. 13, "An Act Providing for the Bangsamoro Administrative Code and for Other Related Purposes," Section 3 (Declaration of Principles and Policies). BAA 13 serves as the comprehensive administrative code governing the structure, functions, and procedures of the Bangsamoro Government.

[^8]: Google NotebookLM is a free AI research tool that constrains its outputs to user-uploaded sources. Unlike general-purpose AI tools, NotebookLM does not draw on its broader training data when answering questions — it only references the specific documents in the user's notebook. This source-grounded approach significantly reduces hallucination risk for document-heavy government work. See Jeff Su, "NotebookLM Changed Completely: Here's What Matters (in 2026)," YouTube, March 2026.

[^7]: BARMM uses distinct ministry names that differ from their national government counterparts. Common errors include: writing "DSWD" instead of "MSSD" (Ministry of Social Services and Development), "DepEd" instead of "MBHTE" (Ministry of Basic, Higher, and Technical Education), "DOLE" instead of "MOLE" (Ministry of Labor and Employment), "DBM" instead of "MFBM" (Ministry of Finance, Budget, and Management), and "DOH" instead of "MOH" (Ministry of Health). AI tools trained primarily on national government documents frequently produce national agency names rather than BARMM ministry names. See the full ministry name mapping in Appendix C of this guidebook.
