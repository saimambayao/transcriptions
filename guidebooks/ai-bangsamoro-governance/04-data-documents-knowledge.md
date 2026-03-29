# Chapter 4 — Data, Documents, and the BARMM Knowledge Base

Every AI tool you use is only as good as the documents you feed it. A brilliant analyst with an empty desk produces nothing. An AI assistant with no reference material produces hallucinations. This chapter teaches you how to organize the massive documentary output of BARMM governance into a structured knowledge base that makes AI dramatically more useful — and how to protect sensitive information while doing so.

---

## 4.1 The Document Universe of BARMM Governance

The Bangsamoro Government generates an extraordinary volume of documents. Consider what the BTA Parliament alone has produced since 2019:

- **89 Bangsamoro Autonomy Acts (BAAs)** spanning governance, budgeting, health, education, labor, local government creation, electoral reform, peace and security, and symbols of identity[^1]
- **570+ resolutions** — both proposed and adopted — covering everything from expressing condolences to directing executive action
- **424+ proposed bills** filed across three BTA compositions, with hundreds still pending deliberation
- The **Bangsamoro Organic Law (Republic Act No. 11054)**, the foundational 18-article charter that defines every power, right, and institution in BARMM[^2]
- The **2nd Bangsamoro Development Plan (BDP) 2023-2028**, a 15-chapter roadmap covering six development goals and eight strategies

That is the Parliament alone. Add the executive side:

- **Executive Orders** from the Office of the Chief Minister
- **Bangsamoro Budget Memoranda** governing the annual budget cycle
- **Manuals of Operations (MOPs)** for ministries, offices, and agencies
- **Committee reports** from 48 standing committees analyzing every bill before plenary
- **Implementing Rules and Regulations (IRRs)** for enacted legislation
- **Administrative orders, memorandum circulars, and special orders** governing daily operations across 27 ministries and offices

No single staff member can hold all of this in memory. No filing cabinet can make it searchable. But a well-organized digital collection combined with AI can.

### BARMM Document Types and Their AI Use Potential

| Document Type | Example | Volume | AI Use Potential | Caution |
|---------------|---------|--------|-----------------|---------|
| **Bangsamoro Autonomy Acts** | BAA 13 (Administrative Code) | 89 enacted | Cross-referencing, amendment tracking, gap analysis, summarization | AI may cite wrong section numbers; always verify against official text |
| **Proposed Bills** | PB-424 | 424+ filed | Legislative comparison, drafting assistance, policy analysis | Bills may have multiple versions; confirm which version is current |
| **Resolutions (Adopted)** | Resolution directing MFBM action | 300+ adopted | Pattern detection, tracking executive compliance | Distinguish between adopted and proposed resolutions |
| **Resolutions (Proposed)** | Proposed resolution on education | 270+ proposed | Identifying legislative priorities and trends | Many remain unfiled; status tracking is incomplete |
| **Bangsamoro Organic Law** | RA 11054, Art. XII (Fiscal Autonomy) | 1 (18 articles) | Constitutional analysis, power-mapping, jurisdictional questions | AI struggles with hierarchical interpretation between BOL and national law |
| **BDP 2023-2028** | Chapter 5 (Social Development) | 1 (15 chapters) | Planning alignment, gap analysis, performance benchmarking | BDP goals are aspirational; AI may treat targets as achievements |
| **Executive Orders** | EOs from the Office of the Chief Minister | 50+ | Policy tracking, executive-legislative alignment analysis | Not always publicly catalogued; collection may be incomplete |
| **Committee Reports** | Report on BAA 84 (Budget System Act) | Hundreds | Understanding legislative intent, tracking deliberations | Reports may not be digitized or publicly available |
| **IRRs** | IRR of BAA 35 (Electoral Code) | Varies per BAA | Implementation analysis, compliance checking | IRRs lag behind legislation; some BAAs have no IRR yet |
| **MOPs and Administrative Orders** | MOP of MBHTE | Per ministry | Process mapping, compliance verification, benchmarking | MOPs may be outdated; verify version currency |
| **Budget Documents** | GAA FY 2026 (BAA 85), BBM 2025-002 | Annual | Expenditure analysis, trend comparison, allocation tracking | Budget figures require careful context; AI may mix fiscal years |
| **Speeches and Statements** | Chief Minister's SOBA | Periodic | Sentiment analysis, commitment tracking, policy direction mapping | Distinguish between policy commitments and rhetorical emphasis |

This table is not exhaustive. Every provincial government, city, and municipality within BARMM generates its own layer of documentation. The point is this: **the raw material for AI-assisted governance work already exists**. The challenge is making it accessible.

---

## 4.2 Preparing Government Documents for AI Analysis

Most AI tools work best with clean, structured text. A scanned PDF of a resolution — tilted, blurry, with handwritten marginal notes — is nearly useless to an AI system. A well-formatted markdown file of the same resolution is instantly searchable, quotable, and cross-referenceable.

### The Document Preparation Pipeline

Preparing a government document for AI analysis follows four steps:

**Step 1: Obtain the digital source.** Start with the best available version. A Word document is better than a PDF. A PDF generated from a Word document (a "native PDF") is better than a scanned image PDF. If the only version is a physical paper copy, scan it at 300 DPI minimum, in black and white, with the pages straight and well-lit.

**Step 2: Extract the text.** For native PDFs, copy-paste works. For scanned documents, you need **Optical Character Recognition (OCR)** — software that reads images and converts them to editable text. Free OCR tools include Adobe Acrobat's built-in OCR, Google Drive's automatic OCR (upload the PDF and open it as a Google Doc), and open-source tools like Tesseract. OCR output always contains errors. Expect misspelled words, merged paragraphs, and garbled tables.

**Step 3: Clean and structure the text.** This is the most labor-intensive step — and the one that pays the highest dividends. Clean the OCR output:

- Fix spelling errors, especially proper nouns (**BARMM**, **Maguindanao del Norte**, **Bangsamoro**)
- Restore paragraph breaks and section numbering
- Recreate tables that OCR flattened into jumbled text
- Remove headers, footers, and page numbers that OCR captured as body text
- Add **markdown formatting**: headings (`#`, `##`, `###`), bold for key terms, numbered lists for enumerated provisions

**Step 4: Apply a consistent file naming convention.** Every document needs a predictable filename. A naming convention allows both humans and AI to locate documents quickly. Use this pattern:

```
[TYPE]-[NUMBER].[extension]
```

Examples:
- `BAA-13.md` (Bangsamoro Administrative Code)
- `BAA-85.md` (GAA FY 2026)
- `PB-424.md` (Proposed Bill No. 424)
- `Resolution-150.md` (Resolution No. 150)

For documents without official numbers, use a date-based convention:

```
[TYPE]-[YYYY-MM-DD]-[short-description].[extension]
```

Examples:
- `EO-2025-07-30-sulu-realignment.md`
- `BBM-2025-002-budget-call-fy2026.md`

### Why Markdown?

**Markdown** is a lightweight text format that uses simple symbols for formatting. It is human-readable, machine-readable, and works with every AI tool. A markdown file is just a text file — it opens in any text editor, on any device, with no special software. Yet it preserves structure: headings, lists, tables, bold text, links.

Compare these two versions of the same provision:

**Scanned PDF (after OCR):**
> SEC. 9. Seat of Government. — The seat of government of the Bangsamoro Autonomous Region shall be in the Municipality of Parang, Province of Maguindanao del Norte. (As amended by BAA No. 37)

**Structured markdown:**
```markdown
### Section 9. Seat of Government

The seat of government of the Bangsamoro Autonomous Region shall be in the
Municipality of Parang, Province of Maguindanao del Norte.

*As amended by [BAA 37](BAA-37.md)*
```

The markdown version tells AI exactly what is a heading, what is body text, and where to find the amending legislation. This structure makes AI responses more accurate because the AI can navigate the document the same way you do — by section, by heading, by cross-reference.

---

## 4.3 Building an Institutional Knowledge Base

A scattered collection of files on a shared drive is not a knowledge base. A knowledge base is an **organized, searchable, interlinked collection** designed for rapid retrieval. The principle is simple: **organized documents make AI dramatically more useful**.

This is the "second brain" principle adapted for government offices. Your personal memory is limited. Your office's institutional memory is fragile — staff transfer, hard drives crash, email accounts expire. A knowledge base survives all of these because the knowledge lives in the structure, not in any individual's head.

### The Three-Tier Architecture

Build your knowledge base in three tiers:

**Tier 1: Legislation and Legal References (read-only)**
These are your authoritative sources. They change only when Parliament enacts new laws or the Supreme Court issues a ruling.

```
knowledge-base/
  legislation/
    bol/
      RA-11054-Article-I.md
      RA-11054-Article-II.md
      ...
      RA-11054-Article-XVIII.md
    baas/
      BAA-1.md through BAA-89.md
    resolutions/
      adopted/
        Resolution-1.md through Resolution-350.md
      proposed/
    bills/
      enacted/
      proposed/
    national-laws/
      RA-10173-data-privacy-act.md
      RA-9485-anti-red-tape-act.md
      ...
```

**Tier 2: Policy and Planning Documents (periodic updates)**
These are your operational references. They change with each planning cycle or budget year.

```
knowledge-base/
  policy/
    bdp-2023-2028/
      chapter-01.md through chapter-15.md
    executive-orders/
    budget/
      gaa-fy-2026.md
      bbm-2025-002.md
    mops/
      mbhte-mop.md
      milg-mop.md
      ...
```

**Tier 3: Working Documents (active, daily use)**
These are your current drafts, analyses, and briefers. They change frequently.

```
knowledge-base/
  working/
    bill-drafts/
    committee-reports/
    briefers/
    correspondence/
```

### Making It Searchable

Structure alone is not enough. Three practices make your knowledge base genuinely searchable:

**1. Consistent headings.** Every BAA file should follow the same heading structure: title, preamble, sections. Every resolution should follow the same structure: whereas clauses, resolving clauses. Consistent structure lets AI find equivalent sections across hundreds of documents.

**2. Index files.** Create an index file at the top of each major folder. The BAA index should list every BAA with its number, short title, category, and date of enactment. The resolution index should list every resolution with its status (adopted, proposed, withdrawn). Index files give AI a map of your collection before it reads any individual document.

**3. Cross-references.** When BAA 37 amends BAA 13, the markdown file for BAA 37 should contain a link to BAA 13, and vice versa. When a committee report analyzes PB-200, the report should link to the bill. Cross-references create a web of connections that AI can navigate — surfacing relationships you might miss when reading documents in isolation.

> **Case Study: Building a Searchable BAA Library**
>
> The BTA Parliament has enacted 89 BAAs across 13 categories: Budget and Appropriations (18), Local Government (14), Health (13), Electoral (6), Symbols and Identity (6), Social Welfare and Human Rights (6), Governance and Administration (5), Education and Culture (5), Economy and Labor (5), Peace and Security (3), Environment and Development (2), Human Rights (1), and Miscellaneous (5).[^1]
>
> When all 89 BAAs are transcribed into structured markdown files with consistent headings, an index file, and cross-references for amendment chains, AI can instantly answer questions that would take a researcher hours:
>
> - *"Which BAAs have been amended, and by what?"* — The amendment chain shows 12 BAAs that amend or extend other BAAs. BAA 87 and BAA 88 both amend BAA 35 (Electoral Code). BAA 37 amends BAA 13 (Administrative Code). BAA 70 and BAA 71 amend the municipality creation acts BAA 54 and BAA 55.
> - *"How many hospital upgrade bills has the Parliament passed?"* — Thirteen health-related BAAs, including nine hospital upgrades across Maguindanao, Lanao del Sur, Sulu, Basilan, and Tawi-Tawi.
> - *"What municipalities has the BTA created?"* — Twelve new municipalities: Pahamuddin, Kadayangan, Nabalawag, Old Kaabakan, Kapalawan, Malidegao, Tugunan, Ligawasan, Nuling, Datu Sinsuat Balabaran, Sheik Abas Hamza (all in Maguindanao del Norte), plus others.
> - *"Which priority codes remain unenacted?"* — Four of seven priority codes are enacted (Administrative Code, Civil Service Code, Education Code, Electoral Code). Three remain: Revenue Code, Local Government Code, and Investment Code.[^2]
>
> None of these answers require AI to "know" Bangsamoro legislation from its training data. The AI reads your organized collection and synthesizes. **The quality of your knowledge base determines the quality of the AI's answers.**

### The Compounding Effect

A knowledge base produces returns that compound over time. On day one, you have 10 documents and AI can answer basic questions. By month three, you have 200 documents and AI can cross-reference legislation against policy against implementation reports. By year one, you have a comprehensive institutional archive that survives staff turnover, office reorganization, and political transitions.

The BTA has operated under three compositions since 2019. Each transition brought new members, new priorities, and new staff. The institutional knowledge that was not written down was lost. A knowledge base prevents this. When the first regular Bangsamoro Government takes office after the 2028 elections, the offices with organized knowledge bases will transition smoothly. Those without them will start from scratch — again.

Start small. Pick one category of documents your office handles daily. Convert them to structured markdown. Build the index. Add metadata headers. Then expand.

### Folder Structures for Different Offices

Not every office needs the same knowledge base. Adapt the three-tier structure to your function:

- **Committee Secretariat**: Prioritize Tier 1 (all BAAs and bills assigned to your committee) and Tier 3 (active committee reports, hearing schedules, witness testimonies)
- **Budget Office (MFBM)**: Prioritize Tier 2 (all GAAs, budget memoranda, SDF allocation documents) and Tier 1 (BAA 84 Budget System Act, BOL Art. XII on fiscal autonomy)
- **Ministry Planning Division**: Prioritize Tier 2 (BDP chapters relevant to your ministry, AIP templates) and Tier 3 (current plans, M&E reports)
- **Office of the Chief Minister**: All three tiers, with emphasis on cross-cutting documents that span multiple ministries

### Tagging and Metadata

Add a **metadata header** to every document in your knowledge base. This header tells AI what the document is, when it was produced, and how to classify it:

```markdown
---
type: BAA
number: 84
title: Bangsamoro Budget System Act of 2025
category: Budget & Appropriations
date_enacted: 2025
status: enacted
amends: null
amended_by: null
classification: public
---
```

Metadata headers enable AI to filter, sort, and compare documents without reading their full text. Ask "list all BAAs in the Health category enacted after 2023" and the AI scans metadata headers, not 89 full documents.

---

## 4.4 Data Privacy and Information Classification

Not every government document belongs in an AI tool. The **Data Privacy Act of 2012 (Republic Act No. 10173)** governs how personal information must be collected, processed, and stored — and it applies fully to BARMM government offices.[^3]

### What RA 10173 Requires

The Data Privacy Act establishes three key principles for government data handling:

**Transparency.** Data subjects (citizens, employees, constituents) must know that their personal information is being collected and how it will be used.[^4]

**Legitimate purpose.** Personal information must be processed only for purposes that are declared, specified, and legitimate.[^5]

**Proportionality.** The processing of personal information must be adequate, relevant, and not excessive in relation to the purpose.[^6]

When you paste a document containing personal information into an AI tool, you are **processing** that data. The AI tool's servers receive, store (temporarily or otherwise), and analyze the information. This triggers RA 10173 obligations.

### The Information Classification Framework

Every BARMM office should classify its documents into four categories before deciding what can be shared with AI tools:

| Classification | Definition | Examples | AI Use Guidance |
|---------------|------------|----------|----------------|
| **Public** | Published or intended for public access; no restriction on sharing | Enacted BAAs, adopted resolutions, official speeches, published BDP chapters, press releases, public budget documents (GAA) | Safe for any AI tool. These documents are already in the public domain. |
| **Internal** | For government use; not classified but not published | Draft MOPs, internal memoranda, committee meeting minutes, interoffice correspondence, draft IRRs | Use with caution. Remove any personal identifiers before sharing. Avoid cloud-based AI tools unless your office has a data processing agreement. |
| **Confidential** | Contains sensitive personal or institutional information | Personnel records (201 files), medical records, disciplinary proceedings, salary details, employee evaluations, tax records, bid proposals before opening | **Do not share with AI tools.** Process these documents manually or use only on-premise, air-gapped AI systems. |
| **Restricted** | National security, peace process, or classified government intelligence | Intelligence reports, peace negotiation documents, military coordination records, decommissioning lists, witness protection information | **Never share with any AI tool under any circumstance.** Handle through classified channels only. |

### Practical Rules for AI Data Handling

Follow these rules when deciding whether to use a document with AI:

**Rule 1: Strip personal identifiers.** Before feeding any internal document to an AI tool, remove names, addresses, phone numbers, ID numbers, and other personally identifiable information (PII). Replace them with placeholders: `[Employee Name]`, `[Address]`, `[ID Number]`.

**Rule 2: Use the "newspaper test."** If the document appeared on the front page of a newspaper tomorrow, would anyone be harmed? If yes, do not share it with a cloud-based AI tool.

**Rule 3: Distinguish between the document and the pattern.** You cannot share a specific employee's performance evaluation with AI. But you can share the **template** for performance evaluations and ask AI to help you improve the format, scoring criteria, or instructions.

**Rule 4: Check your AI tool's data policy.** Different AI tools handle your data differently. Some tools use your inputs to train their models. Others do not. Read the terms of service. As of 2026, Claude (Anthropic) does not use conversation data for training when accessed through the API or Team/Enterprise plans.[^7] Google's NotebookLM processes documents on Google's servers but does not train its models on uploaded content.[^8] Policies change. Verify before you share.

**Rule 5: When in doubt, ask your Data Protection Officer.** RA 10173 requires government agencies to designate a Data Protection Officer (DPO).[^9] If you are unsure whether a document can be shared with an AI tool, ask your DPO. The cost of asking is a few minutes. The cost of a data breach is a compliance investigation.

### Common Scenarios and How to Handle Them

**Scenario: You need AI to draft a committee report.** The committee report references testimony from named witnesses, their positions, and their statements. Strip the names and replace with role descriptions: "[Witness 1, Municipal Mayor]" instead of the actual name. Keep the substance. Remove the identifiers.

**Scenario: You need AI to analyze budget utilization by office.** The budget data itself (allocation amounts, utilization rates, program expenditures) is generally Public or Internal. But if the analysis involves specific personnel costs tied to named employees, remove the names. Aggregate where possible: "Division X has 15 positions with a total PS allocation of PHP 12M" rather than listing each employee's salary.

**Scenario: You need AI to help draft a disciplinary resolution.** Stop. Disciplinary proceedings involve Confidential personnel information. Do not share the specifics with any cloud-based AI tool. You may ask AI for help with the **format and structure** of a disciplinary resolution using a blank template, but never include case-specific details.

**Scenario: You need AI to cross-reference a peace process document.** If the document is a published peace agreement (like the Comprehensive Agreement on the Bangsamoro), it is Public. If it is an internal negotiation brief, intelligence assessment, or decommissioning schedule, it is Restricted. Know the difference before you type.

### The BOL's Transparency Mandate

The Bangsamoro Organic Law contains its own transparency provisions. Article IX recognizes the right of the people to information on matters of public concern.[^10] Article VII provides for an open and transparent government through the Parliament's proceedings.[^11] These provisions create a **presumption of openness** for legislative documents — enacted laws, resolutions, committee reports, and plenary proceedings are public by nature.

This means most Tier 1 legislative documents are safe for AI analysis. The privacy risk concentrates in Tier 3 working documents and personnel-related materials.

---

## 4.5 Working with Philippine and Bangsamoro Legal Texts

Legal texts are where AI is simultaneously most useful and most dangerous. The usefulness comes from AI's ability to read and cross-reference hundreds of documents in seconds. The danger comes from AI's tendency to fabricate details that sound authoritative.

### What AI Does Well with Legal Texts

**Cross-referencing.** Ask AI to identify every BAA that amends another BAA. With a structured knowledge base, AI produces the complete amendment chain in seconds: BAA 14 extends BAA 3. BAA 33 amends BAA 23. BAA 37 amends BAA 13. BAA 87 and BAA 88 both amend BAA 35. Twelve amendment relationships across 89 BAAs — a task that would take a researcher an hour of manual checking.[^1]

**Summarization.** Ask AI to summarize BAA 85 (GAA FY 2026) into a one-page briefer for a Member of Parliament. AI excels at condensing long, repetitive legislative text into structured summaries with clear headings.

**Pattern detection.** Ask AI to categorize all 89 BAAs by domain. AI identifies that Budget and Appropriations dominates with 18 BAAs, followed by Local Government (14) and Health (13). Ask AI to identify trends: hospital upgrade legislation has accelerated since 2023, with nine health infrastructure BAAs covering hospitals across five provinces.

**Gap analysis.** Ask AI which of the seven priority codes mandated by the BOL's transition provisions remain unenacted. AI compares the list against the 89 enacted BAAs and identifies Revenue Code, Local Government Code, and Investment Code as outstanding.[^2]

**Comparative analysis.** Ask AI to compare a proposed bill against existing BAAs to identify conflicts, overlaps, or gaps. Feed it PB-200 and BAA 49 (Local Governance Code) and ask: "Does this proposed bill create any entity that already exists under BAA 49?"

### What AI Gets Wrong with Legal Texts

AI makes specific, predictable errors with legal texts. Learn these patterns and you can catch them before they reach an official document.

| AI Pitfall | What Happens | Real Example | How to Catch It |
|-----------|-------------|--------------|----------------|
| **Wrong BAA number** | AI cites the correct content but assigns it to the wrong BAA | "BAA 35 creates the Bangsamoro Human Rights Commission" (actually BAA 4; BAA 35 is the Electoral Code) | Cross-check every BAA number against the BAA index |
| **Fabricated section** | AI invents a section number that does not exist in the cited law | "Section 42 of the BOL provides for AI governance" (no such section exists) | Verify every section citation against the source document |
| **Misquoted provision** | AI paraphrases a provision and presents the paraphrase as a direct quote | "The BOL states that the annual block grant shall be 7% of national revenue" (the actual figure is 5% per Art. XII, Sec. 15) | Never trust AI-generated "quotations" of legal text; verify verbatim wording |
| **Conflated provisions** | AI merges provisions from different articles or different laws into one statement | "The BOL's Special Development Fund of PHP 5B annually is found in Article XII" (SDF is in Art. XIV, Sec. 2, not Art. XII)[^2] | Check not just the content but the specific article and section |
| **Outdated information** | AI references provisions that have been amended or superseded | "BAA 58 establishes the parliamentary districts of BARMM" (BAA 58 was declared unconstitutional; BAA 86 now governs redistricting)[^12] | Check the amendment chain for any cited BAA |
| **Hierarchical confusion** | AI treats a BAA provision as overriding national law, or vice versa | "BARMM can unilaterally establish its own labor standards" (labor is an overlapping jurisdiction requiring harmonization per BOL Art. V) | Verify jurisdictional scope through Art. V enumerated powers |
| **False consensus** | AI states that a bill "was enacted" when it was only proposed | "The Revenue Code was enacted as BAA 90" (the Revenue Code has not been enacted as of March 2026) | Verify enactment status against the BAA index and parliamentary records |

### How to Prompt AI for Legal Research

The way you frame a legal question determines the quality of the answer. Follow these prompting principles:

**Specify the source.** Do not ask "What does the law say about fiscal autonomy?" Ask "What does Article XII of RA 11054 say about the annual block grant?" The more specific your reference, the less room AI has to fabricate.

**Provide the documents.** Do not rely on AI's training data for legal text. Paste or attach the actual BAA, resolution, or BOL article. When AI reads your document rather than recalling from memory, accuracy improves dramatically.

**Ask for citations.** End every legal prompt with: "Cite the specific section, article, and law for every claim." This forces AI to ground its response in identifiable sources you can verify.

**Request uncertainty flags.** Add: "If you are not certain about any fact, say so explicitly." AI tools are capable of expressing uncertainty — but they default to confident-sounding answers unless you ask them to flag doubts.

### The Verification Protocol for Legal AI Outputs

Every time AI produces a legal citation, run this five-point check:

1. **Number check.** Is the BAA/RA/resolution number correct? Cross-reference against your index.
2. **Section check.** Does the cited section actually exist in that law? Open the source document.
3. **Verbatim check.** If AI presents text as a quotation, compare it word-for-word against the source.
4. **Currency check.** Has the cited provision been amended or repealed? Check the amendment chain.
5. **Jurisdiction check.** Is the matter within BARMM's enumerated powers (BOL Art. V, Sec. 2), shared jurisdiction, or exclusive national government authority?[^13]

This protocol takes two to five minutes per citation. It is not optional. A single wrong BAA number in an official briefer undermines the credibility of every other fact in the document.

### Working with the BOL's Unique Structure

The Bangsamoro Organic Law has structural features that trip up AI tools:

**The enumerated powers list.** Article V, Section 2 lists 55 subject areas from (a) to (ccc). AI tools frequently miscount items in long enumerated lists or assign the wrong letter to a subject area. When citing a specific power, provide the letter designation and verify it.[^13]

**Overlapping jurisdiction.** Some BOL enumerated powers overlap with national legislation — education, labor, disaster management, environmental protection. AI may state definitively that BARMM "has authority over" a matter when the reality is shared jurisdiction requiring harmonization through the intergovernmental relations mechanisms in Article VI.[^13]

**The transition provisions.** Article XVI governs the BTA's mandate, which has been extended twice (RA 11593 to 2025, RA 12064 to 2028). AI training data may reflect earlier timelines. Always specify the current transition status when prompting AI about BTA-related questions.[^2]

**The Sulu exclusion.** The Supreme Court ruled in *Province of Sulu v. Medialdea* (G.R. Nos. 242255, 243246, 243693; September 9, 2024, finalized November 26, 2024) that Sulu is not part of BARMM. EO 91 (July 30, 2025) realigned Sulu under Region IX.[^2] AI trained on data before late 2024 may still include Sulu in BARMM's territorial scope. Correct this explicitly in your prompts.

---

## Key Takeaways

1. **The raw material already exists.** BARMM's 89 BAAs, 570+ resolutions, 424+ proposed bills, and hundreds of policy documents contain the institutional knowledge your office needs. The bottleneck is organization, not creation.

2. **Structure determines AI quality.** A well-formatted markdown file with consistent headings, metadata, and cross-references produces dramatically better AI outputs than a scanned PDF or unstructured Word document.

3. **Build your knowledge base in three tiers.** Legislation and legal references (read-only), policy and planning documents (periodic updates), and working documents (active use). Start with whatever your office produces most.

4. **Classify before you share.** Use the four-level classification framework (Public, Internal, Confidential, Restricted) and never share Confidential or Restricted documents with cloud-based AI tools.

5. **Trust AI for pattern work, not precision work.** AI excels at cross-referencing, summarizing, and detecting patterns across large document collections. It fails at verbatim accuracy, section numbering, and jurisdictional interpretation. Always verify.

---

## Chapter 4 Checklist

- [ ] Identify the top 20 documents your office uses most frequently
- [ ] Convert at least 5 key documents from PDF to structured markdown
- [ ] Establish a file naming convention for your office's knowledge base
- [ ] Create an index file listing all documents in your collection
- [ ] Classify your document collection using the four-level framework
- [ ] Identify your office's Data Protection Officer
- [ ] Test AI with a known legal question and verify the answer against source documents

---

[^1]: Based on the BAA Quick-Reference Index maintained from BTA Parliamentary records. The 89 BAAs are categorized across 13 domains: Budget & Appropriations (18), Local Government (14), Health (13), Electoral (6), Symbols & Identity (6), Social Welfare & Human Rights (6), Governance & Administration (5), Education & Culture (5), Economy & Labor (5), Miscellaneous (5), Peace & Security (3), Environment & Development (2), Human Rights (1).

[^2]: Republic Act No. 11054, "An Act Providing for the Organic Law for the Bangsamoro Autonomous Region in Muslim Mindanao" (2018). Key provisions referenced: Art. V, Sec. 1-3 (Powers of Government); Art. XII, Sec. 15-16 (Annual Block Grant); Art. XIV, Sec. 2 (Special Development Fund); Art. XVI (Transition Provisions). Transition timeline: original 2022 deadline extended by RA 11593 (to 2025) and RA 12064 (to 2028). Priority codes status as of March 2026: four enacted (Administrative Code/BAA 13, Civil Service Code/BAA 17, Education Code/BAA 18, Electoral Code/BAA 35), three remaining (Revenue Code, Local Government Code, Investment Code). Sulu exclusion per *Province of Sulu v. Medialdea*, G.R. Nos. 242255, 243246, 243693 (Sept. 9, 2024; finalized Nov. 26, 2024).

[^3]: Republic Act No. 10173, "An Act Protecting Individual Personal Information in Information and Communications Systems in the Government and the Private Sector, Creating for this Purpose a National Privacy Commission, and for Other Purposes" (2012), otherwise known as the Data Privacy Act of 2012.

[^4]: RA 10173, Sec. 11(a) (Transparency principle for processing of personal information).

[^5]: RA 10173, Sec. 11(b) (Legitimate purpose principle).

[^6]: RA 10173, Sec. 11(c) (Proportionality principle).

[^7]: Anthropic, "Privacy Policy" and "Commercial Terms of Service." As of 2026, Anthropic states that customer data submitted through the API and Team/Enterprise plans is not used for model training. Verify current terms at anthropic.com/privacy.

[^8]: Google, "NotebookLM Privacy and Data Handling." As of 2026, Google states that NotebookLM does not use uploaded sources to train its AI models. Verify current terms at notebooklm.google.com.

[^9]: RA 10173, Sec. 21 (Designation of Data Protection Officer by personal information controllers and processors, including government agencies).

[^10]: Republic Act No. 11054, Art. IX (Basic Rights). The right to information on matters of public concern is a fundamental right recognized under both the BOL and the 1987 Philippine Constitution, Art. III, Sec. 7.

[^11]: Republic Act No. 11054, Art. VII (Bangsamoro Government), provisions on parliamentary transparency and open proceedings.

[^12]: BAA 58 (Parliamentary Districts Creation) and BAA 77 (Reconstituted Parliamentary Districts) were declared unconstitutional by the Supreme Court in *Ali et al. v. BTA* (G.R. No. E-02219) and *Macapaar et al. v. COMELEC* (G.R. No. E-02235; Sept. 30, 2025). BAA 86 (Parliamentary District Act, Jan. 20, 2026) was subsequently enacted, establishing 32 parliamentary districts.

[^13]: Republic Act No. 11054, Art. V, Sec. 2 enumerates 55 subject areas of Bangsamoro government power from (a) administration of justice to (ccc) water supply. Art. V, Sec. 1 contains the residual clause: powers not granted to BARMM vest in the National Government. Art. VI governs intergovernmental relations mechanisms for areas of overlapping authority.
