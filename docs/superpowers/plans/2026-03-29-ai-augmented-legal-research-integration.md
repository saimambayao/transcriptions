# AI-Augmented Legal Research Integration Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transcribe the SC's AI Governance Framework, integrate it as the legal spine of the AI and Bangsamoro Governance guidebook, then cascade AI-augmentation chapters into the Legal Research and Bill Drafting guidebooks.

**Architecture:** Three-phase pipeline. Phase 1 produces the source transcription. Phase 2 updates the universal AI guidebook with legal authority it currently lacks. Phase 3 adds domain-specific AI chapters to two guidebooks, each referencing both the SC Resolution and the universal guidebook. All content follows the `/guidebook-writer` skill and `/transcriber` skill conventions.

**Tech Stack:** Markdown content, `/transcriber` for PDF extraction, `/guidebook-writer` for chapter production, `/fact-checker` for verification, `/citation` for footnotes.

**Source prompt:** `~/Vault/Prompts/260329-1830-ai-augmented-legal-research-integration.md`

---

## File Structure

### Phase 1: Transcription
- **Create:** `jurisprudence/2026/AM-25-11-28-SC.md` — verbatim transcription of A.M. No. 25-11-28-SC (29 pages)

### Phase 2: Universal Guidebook Updates
- **Modify:** `guidebooks/ai-bangsamoro-governance/03-ai-augmented-workflow.md` — add SC's HITL/HOTL/HIC oversight mechanisms
- **Modify:** `guidebooks/ai-bangsamoro-governance/07-legislative-policy.md` — strengthen with SC's explicit AI authorization for legal research
- **Modify:** `guidebooks/ai-bangsamoro-governance/12-ethics-islamic-values.md` — ground in SC's 8 ethical principles + 4-tier risk classification
- **Modify:** `guidebooks/ai-bangsamoro-governance/17-appendices.md` — add SC disclosure template + risk classification matrix
- **Modify:** `guidebooks/ai-bangsamoro-governance/18-bibliography.md` — add A.M. No. 25-11-28-SC + key cited sources
- **Modify:** `guidebooks/ai-bangsamoro-governance/00-table-of-contents.md` — update if section headers change

### Phase 3: Domain Guidebook Chapters
- **Create:** `guidebooks/legal-research/14-chapter-14.md` — "AI-Augmented Legal Research"
- **Modify:** `guidebooks/legal-research/00-table-of-contents.md` — add Chapter 14
- **Create:** `guidebooks/bill-drafting/14-chapter-12.md` — "AI-Augmented Bill Drafting" [?confirm chapter number — current guidebook has 11 chapters, so this would be Chapter 12]
- **Modify:** `guidebooks/bill-drafting/00-table-of-contents.md` — add new chapter

---

## Phase 1: Transcribe A.M. No. 25-11-28-SC

### Task 1: Transcribe the SC Resolution

**Files:**
- Create: `jurisprudence/2026/AM-25-11-28-SC.md`

- [ ] **Step 1: Create the 2026 jurisprudence directory**

```bash
mkdir -p ~/apps/transcriptions/jurisprudence/2026
```

- [ ] **Step 2: Transcribe the PDF using /transcriber**

Invoke `/transcriber` on the source PDF:
```
Source: ~/Library/Mobile Documents/com~apple~CloudDocs/_Law/AM-NO-25-11-28-SC-AI-Augmented.pdf
Output: jurisprudence/2026/AM-25-11-28-SC.md
```

The transcription must include:
- **Metadata header:** case number (A.M. No. 25-11-28-SC), title, date (February 18, 2026), source URL (if available)
- **Notice page:** the cover letter with En Banc designation
- **WHEREAS clauses:** all 8 recitals verbatim
- **NOW THEREFORE clause** and adoption language
- **Working Group composition:** all names and positions (Chairperson through Consultants)
- **Signatories:** all 15 Supreme Court Justices
- **Part I (General Provisions):** Sections A-C (Purpose, Scope, Definitions — 10 definitions with footnotes)
- **Part II (Ethical Governance):** Sections 1-8 (Human-Centered, Human Rights, Transparency, Accountability/Oversight, Fairness, Privacy, Security, Sustainability)
- **Part III (Management Governance):** Sections 1-7 (Organizational Structure, Human Involvement Determination, AI Adoption Process, Stakeholder Consultation, Risk Management, Data Governance, International Cooperation)
- **All tables:** HITL/HOTL/HIC mechanisms table, AI roles table (Data Provider through AI User), risk classification (Prohibited/High/Limited/Minimal)
- **All footnotes:** 34 footnotes with full citations (ASEAN, UNESCO, EU, etc.)

- [ ] **Step 3: Verify transcription against source PDF**

Read the transcribed markdown and spot-check:
- All 15 Justice signatures present with correct names
- All 10 definitions in Part I.C match the PDF
- All 8 ethical principles in Part II have correct section numbers
- The HITL/HOTL/HIC table has 3 rows with complete definitions
- The 4-tier risk classification (Prohibited/High/Limited/Minimal) has all 4 categories with examples
- Footnote count matches (34 footnotes)

- [ ] **Step 4: Update jurisprudence INDEX**

Add entry to `jurisprudence/INDEX.md` under 2026 (create 2026 section if needed):
```markdown
### 2026
| File | Case No. | Title | Date |
|------|----------|-------|------|
| [AM-25-11-28-SC](2026/AM-25-11-28-SC.md) | A.M. No. 25-11-28-SC | Governance Framework on the Use of Human-Centered Augmented Intelligence in the Philippine Judiciary | February 18, 2026 |
```

---

## Phase 2: Update the Universal AI Guidebook

### Task 2: Update Chapter 3 — AI-Augmented Workflow (HITL/HOTL/HIC)

**Files:**
- Modify: `guidebooks/ai-bangsamoro-governance/03-ai-augmented-workflow.md`

- [ ] **Step 1: Read Chapter 3 to identify insertion points**

Read the full chapter. Identify:
- Section 3.1 (Human-AI Partnership Model) — this is where the SC's oversight mechanisms should be grounded
- Section 3.4 (Quality Assurance: Trust but Verify) — this is where the SC's accountability and disclosure requirements map

- [ ] **Step 2: Add SC-mandated oversight mechanisms to Section 3.1**

After the existing Human-AI Partnership Model content, add a new subsection:

**3.1.1 The Supreme Court's Human Oversight Framework**

Content must include:
- Citation: A.M. No. 25-11-28-SC, Part III, Sec. 2
- The three mechanisms table (verbatim from the SC Resolution):
  - **Human-in-the-loop (HITL):** AI output treated as recommendations for human decision-maker
  - **Human-on-the-loop (HOTL):** Human control during design/development, shifts to monitoring post-deployment
  - **Human-in-command (HIC):** Human control extends beyond immediate functioning to external impact
- The principle: "Under no circumstance should AI tools or their output serve as the sole, primary or determinative basis of any adjudicatory outcome" (Part II, Sec. 4)
- Application to BARMM: for legal research, the researcher is always HITL — AI produces a Research Memorandum draft, the researcher verifies every provision

- [ ] **Step 3: Add SC disclosure requirements to Section 3.4 or new Section 3.7**

Add the SC's 6-point disclosure framework (Part II, Sec. 3):
1. AI tool used (name, version)
2. Extent/degree of use for the specific work
3. Extent of human control and oversight
4. Statement that output was preserved upon inquiry
5. Compliance with Framework principles
6. Statement that user bears ultimate responsibility

Include a **BARMM AI Disclosure Template** adapted from the SC's requirements.

- [ ] **Step 4: Verify edits are consistent with chapter voice**

Read the modified chapter beginning-to-end. Confirm new sections use the same tone, formatting, and pedagogical approach as existing content.

### Task 3: Update Chapter 7 — Legislative and Policy Work

**Files:**
- Modify: `guidebooks/ai-bangsamoro-governance/07-legislative-policy.md`

- [ ] **Step 1: Read Chapter 7, focusing on Section 7.2 (Legislative Research with AI)**

Identify where the SC Resolution's explicit authorization of AI for legal research should be cited.

- [ ] **Step 2: Add SC legal authority for AI-assisted legal research**

In Section 7.2, add a subsection citing:
- A.M. No. 25-11-28-SC, Part I.C.6 — definition of "Use of human-centered augmented intelligence" includes "legal research" and "automated compilation or generation of structured authorities, citations, or other paratext" (items d and c from the permitted uses list)
- This is Tier 7 authority (SC rule-making power under Constitution Art. VIII, Sec. 5(5)) that explicitly authorizes AI for legal research
- Cross-reference to the Legal Research Guidebook, Chapter 14 (AI-Augmented Legal Research) for the domain-specific methodology

- [ ] **Step 3: Add SC risk classification for legal research**

Note that the SC classifies AI for legal research as **limited-risk** (Part III, Sec. 5, Category 3: "customer-service chatbots, transcription" — legal research falls in this category, not the high-risk adjudicatory category). This means:
- HITL oversight is required but not the same level as adjudicatory AI
- Disclosure is required
- Verification against source documents is mandatory (the guidebook's existing anti-fabrication protocol satisfies this)

### Task 4: Update Chapter 12 — Ethics, Islamic Values, and Responsible AI

**Files:**
- Modify: `guidebooks/ai-bangsamoro-governance/12-ethics-islamic-values.md`

- [ ] **Step 1: Read Chapter 12, focusing on Section 12.5 (Bangsamoro AI Ethics Framework)**

Identify how the existing framework maps to the SC's 8 ethical principles.

- [ ] **Step 2: Ground the Bangsamoro AI Ethics Framework in the SC Resolution**

Add a mapping table showing alignment:

| SC Principle (A.M. No. 25-11-28-SC) | Bangsamoro Framework Equivalent | Islamic Principle |
|--------------------------------------|--------------------------------|-------------------|
| 1. Human-Centered | Human-AI Partnership (Ch. 3) | Khalifah (stewardship) |
| 2. Human Rights & Harm Avoidance | Rights Protection | Adl (justice) |
| 3. Transparency | Trust but Verify Protocol | Amanah (trustworthiness) |
| 4. Accountability & Human Oversight | HITL/HOTL/HIC | Hisbah (accountability) |
| 5. Fairness & Non-Discrimination | Inclusive Governance | Adl + Ihsan |
| 6. Privacy & Data Protection | Data Privacy (RA 10173) | Sitr (privacy in Islam) |
| 7. Security, Safety & Robustness | Risk Management | Maslahah (public interest) |
| 8. Sustainability & Environmental Impact | Resource Stewardship | Khalifah + Amanah |

- [ ] **Step 3: Add the SC's 4-tier risk classification**

Add a new subsection under 12.4 (Risks and Safeguards) with the SC's risk classification:
1. **Prohibited AI systems** — cognitive manipulation, biometrics-based categorization, real-time tracking
2. **High-risk AI systems** — directly affect fundamental rights, law enforcement
3. **Limited-risk AI systems** — chatbots, transcription, legal research, document processing
4. **Minimal-risk AI systems** — spam filters, basic automation

Map each category to BARMM governance activities.

### Task 5: Update Appendices and Bibliography

**Files:**
- Modify: `guidebooks/ai-bangsamoro-governance/17-appendices.md`
- Modify: `guidebooks/ai-bangsamoro-governance/18-bibliography.md`

- [ ] **Step 1: Add AI Disclosure Template to Appendices**

Create a new appendix: **Appendix [next letter]: AI Use Disclosure Template**

Based on the SC's 6-point disclosure requirement, create a fill-in template:

```markdown
## AI Use Disclosure

**Document:** [title of the document that used AI assistance]
**Date:** [date]
**Prepared by:** [name and position]

1. **AI Tool(s) Used:** [name, version — e.g., "Claude Code (Anthropic Claude Opus 4.6)"]
2. **Purpose and Extent of AI Use:** [what the AI was used for — e.g., "legal research compilation, provision extraction, comparative matrix generation"]
3. **Human Control and Oversight:** [HITL/HOTL/HIC — e.g., "Human-in-the-loop: all AI-generated provisions were verified against source documents by the researcher"]
4. **Output Preservation:** [statement — "AI outputs have been preserved and are available upon request"]
5. **Framework Compliance:** [statement — "This use of AI complies with the principles set forth in A.M. No. 25-11-28-SC and the AI and Bangsamoro Governance Guidebook"]
6. **Responsibility:** [statement — "The undersigned bears ultimate responsibility for the accuracy and completeness of this document"]

**Signature:** _______________
```

- [ ] **Step 2: Add SC Risk Classification Quick Reference to Appendices**

Create a one-page risk classification reference card showing the 4 tiers with BARMM-specific examples.

- [ ] **Step 3: Update Bibliography**

Add to Section A (Primary Legal Sources) under a new "Supreme Court Administrative Matters" heading:

```markdown
### Supreme Court Administrative Matters

Supreme Court of the Philippines, A.M. No. 25-11-28-SC, Governance Framework on the Use of Human-Centered Augmented Intelligence in the Philippine Judiciary (February 18, 2026).
```

Add to a new Section (International and Regional AI Governance Sources) the key sources cited by the SC Resolution:
- ASEAN Guide on AI Governance and Ethics (2024)
- UNESCO Recommendation on the Ethics of Artificial Intelligence (2021)
- UNESCO Guidelines for the Use of AI Systems in Courts and Tribunals (2023)
- European Commission High-Level Expert Group, Ethics Guidelines for Trustworthy AI (2019)
- Council of ASEAN Chief Justices, Governance Framework on the Use of AI for ASEAN Judiciaries
- EU Artificial Intelligence Act
- OECD AI Principles
- Inter-Parliamentary Union, Guidelines for AI in Parliaments — Ethical Principles

### Task 6: Update Universal Guidebook TOC

**Files:**
- Modify: `guidebooks/ai-bangsamoro-governance/00-table-of-contents.md`

- [ ] **Step 1: Add new subsection headers to TOC**

Update the TOC to reflect new subsections added in Tasks 2-5:
- Under Chapter 3: add "3.1.1 The Supreme Court's Human Oversight Framework"
- Under Chapter 7: add SC authorization subsection
- Under Chapter 12: add risk classification subsection
- Under Appendices: add AI Disclosure Template and Risk Classification Quick Reference

---

## Phase 3: Domain Guidebook AI Chapters

### Task 7: Write Chapter 14 — AI-Augmented Legal Research (Legal Research Guidebook)

**Files:**
- Create: `guidebooks/legal-research/14-chapter-14.md`

- [ ] **Step 1: Draft the chapter using /guidebook-writer conventions**

The chapter must follow the same structure as Chapters 1-13: introduction, numbered sections, worked example, common pitfalls, template, quality checklist.

**Chapter outline:**

```markdown
# Chapter 14 — AI-Augmented Legal Research

## 14.1 Purpose
[Why this chapter exists — SC Resolution now explicitly authorizes AI for legal research]

## 14.2 The Legal Authority for AI in Legal Research
[Cite A.M. No. 25-11-28-SC verbatim:
- Part I.C.6: "legal research" is an authorized use
- Part I.C.6.c: "automated compilation or generation of structured authorities, citations, or other paratext"
- Part II, Sec. 4: "Under no circumstance should AI tools or their output serve as the sole, primary or determinative basis"
- Constitutional basis: Art. VIII, Sec. 5(5)]

## 14.3 The Human-in-the-Loop Model for Legal Research
[Map SC's HITL/HOTL/HIC to the 5-step methodology:
- Step 1 (Issue Analysis): AI can help formulate research questions — HITL
- Step 2 (Landscape Review): AI can scan secondary sources — HITL
- Step 3 (Systematic Source Search): AI searches archives, extracts provisions — HITL with mandatory human verification
- Step 4 (Provision Chain Trace): AI traces chains, human verifies each link — HITL
- Step 5 (Verification): Human-only — this step cannot be delegated to AI]

## 14.4 What AI Can and Cannot Do in Legal Research
[Two-column table: CAN (search, extract, compare, draft) vs. CANNOT (determine legal conclusions, replace verification, substitute for professional judgment)]

## 14.5 The AI-Augmented Research Pipeline
[Map to the existing 6-step Legal Reference Pipeline:
1. /prompter → AI helps refine the question
2. /plan → AI helps design research strategy
3. /legal-researcher → AI executes systematic search with HITL oversight
4. /legal-assistant → AI drafts document, human verifies every claim
5. /legal-reviewer → AI assists review, human makes final judgment
6. /fact-checker → AI assists verification, human confirms
Show how each step implements HITL]

## 14.6 Anti-Fabrication: The SC-Compliant Verification Method
[Connect the guidebook's existing EXTRACTED/INFERRED/UNVERIFIED framework to SC requirements:
- SC requires transparency about AI limitations (Part II, Sec. 3)
- The tagging system (EXTRACTED/INFERRED/UNVERIFIED) IS the transparency mechanism
- Every AI-generated provision must be verified against the source document
- Any claim that cannot be verified must be marked [UNVERIFIED]]

## 14.7 Disclosure Requirements for AI-Assisted Research
[The 6-point disclosure from SC, adapted for legal research outputs:
- When disclosure is required (always, for any AI-assisted research product)
- Where to place the disclosure (appendix of Research Memorandum)
- Template (cross-reference to AI and Bangsamoro Governance Guidebook appendix)]

## 14.8 BARMM-Specific Considerations
[Address unique BARMM context:
- Shari'ah content: AI tools may not have adequate training data for Islamic jurisprudence — higher verification burden
- Multilingual content: Filipino, English, Arabic — AI performance varies by language
- Local legislation: AI may not have current BAA texts — local archive is the authoritative source
- Data privacy: RA 10173 applies to any personal data in research queries]

## 14.9 Worked Example: AI-Augmented vs. Manual Research
[Side-by-side comparison on the same question: "What is the legal basis for the Bangsamoro Budget System Act?"
- Manual path: time, steps, sources consulted
- AI-augmented path: same steps with AI assistance, time saved, additional sources found
- Both produce the same Research Memorandum — AI found 3 additional national laws the manual researcher missed
- Disclosure statement appended to the AI-augmented version]

## 14.10 Common Pitfalls
[8-10 pitfalls specific to AI-augmented legal research:
1. Accepting AI-generated provision text without reading the source
2. Treating AI confidence as accuracy
3. Not disclosing AI use
4. Using AI for Shari'ah interpretation without Islamic jurisprudential expertise
5. Feeding confidential case data into external AI tools
6. Skipping the National Law Relationship Test because AI "figured it out"
7. Over-relying on AI for verification (Step 5 must be human)
8. Assuming AI has current BAA texts — local archive is authoritative]

## 14.11 Template: AI-Augmented Research Memorandum
[Same template as Chapter 12's Research Memorandum but with:
- "AI Assistance" field in the header
- AI Disclosure appendix at the end]

## 14.12 Quality Checklist
[Extends Chapter 2's quality checklist with AI-specific items:
- [ ] AI use disclosed in the document
- [ ] Every AI-extracted provision verified against source text
- [ ] EXTRACTED/INFERRED/UNVERIFIED tags applied to all AI-generated findings
- [ ] No confidential or personal data sent to external AI tools without authorization
- [ ] Shari'ah content reviewed by Islamic jurisprudential expert (if applicable)
- [ ] Human researcher independently formed legal conclusions
- [ ] Disclosure template completed and appended]
```

- [ ] **Step 2: Write the full chapter content**

Use `/guidebook-writer` to produce the complete chapter, following the outline above. Each section must:
- Cite A.M. No. 25-11-28-SC verbatim for all governance principles
- Reference the AI and Bangsamoro Governance Guidebook for universal principles
- Use the Legal Research Guidebook's existing terminology (5-step methodology, 7-tier hierarchy, etc.)
- Include footnotes in Feliciano 10th Edition format

- [ ] **Step 3: Run /fact-checker on the chapter**

Verify all citations to A.M. No. 25-11-28-SC against the transcription (Task 1 output).
Verify all cross-references to existing guidebook chapters.

- [ ] **Step 4: Run /citation on the chapter**

Apply proper citation format to all references.

### Task 8: Update Legal Research Guidebook TOC

**Files:**
- Modify: `guidebooks/legal-research/00-table-of-contents.md`

- [ ] **Step 1: Add Chapter 14 to the TOC**

After Chapter 13's entry, add:

```markdown
**Chapter 14 — AI-Augmented Legal Research**

&emsp;14.1 Purpose
&emsp;14.2 The Legal Authority for AI in Legal Research
&emsp;14.3 The Human-in-the-Loop Model for Legal Research
&emsp;14.4 What AI Can and Cannot Do in Legal Research
&emsp;14.5 The AI-Augmented Research Pipeline
&emsp;14.6 Anti-Fabrication: The SC-Compliant Verification Method
&emsp;14.7 Disclosure Requirements for AI-Assisted Research
&emsp;14.8 BARMM-Specific Considerations
&emsp;14.9 Worked Example: AI-Augmented vs. Manual Research
&emsp;14.10 Common Pitfalls
&emsp;14.11 Template: AI-Augmented Research Memorandum
&emsp;14.12 Quality Checklist
```

### Task 9: Write AI-Augmented Bill Drafting Chapter (Bill Drafting Guidebook)

**Files:**
- Create: `guidebooks/bill-drafting/14-chapter-12.md` [confirm filename matches existing pattern]

- [ ] **Step 1: Read the Bill Drafting Guidebook TOC and identify the insertion point**

Read `guidebooks/bill-drafting/00-table-of-contents.md` fully. Determine:
- Current last chapter number
- The correct filename convention (e.g., `12-chapter-11.md` means file `12` = chapter `11`)
- Where AI content naturally fits in the bill drafting workflow

- [ ] **Step 2: Draft the chapter outline**

Follow the same pattern as Task 7 but adapted for bill drafting:

```markdown
# Chapter 12 — AI-Augmented Bill Drafting

## 12.1 Purpose
## 12.2 The Legal Authority for AI in Legislative Work
## 12.3 The Human-in-the-Loop Model for Bill Drafting
## 12.4 What AI Can and Cannot Do in Bill Drafting
[CAN: research, draft structure, comparative analysis, consistency checking, citation generation
CANNOT: make policy decisions, determine legislative intent, replace committee deliberation]
## 12.5 The AI-Augmented Bill Drafting Process
[Map to the Bill Drafting Guidebook's existing stages:
Stage 1 (Policy Direction) → AI assists environmental scanning
Stage 2 (Legislative Research) → AI executes /legal-researcher pipeline
Stage 3 (Drafting) → AI assists with structure, cross-references
Stage 4 (Review) → AI assists /legal-reviewer, human decides
Stage 5 (Filing) → human only]
## 12.6 Anti-Fabrication in AI-Assisted Drafting
## 12.7 Disclosure Requirements
## 12.8 Worked Example: AI-Augmented vs. Manual Bill Drafting
## 12.9 Common Pitfalls
## 12.10 Template: AI Disclosure for Legislative Documents
## 12.11 Quality Checklist
```

- [ ] **Step 3: Write the full chapter content**

Use `/guidebook-writer` conventions. Follow the same quality standards as Task 7.

- [ ] **Step 4: Run /fact-checker and /citation**

- [ ] **Step 5: Update Bill Drafting Guidebook TOC**

---

## Verification Checklist (run after all tasks complete)

- [ ] A.M. No. 25-11-28-SC transcription is complete and verified at `jurisprudence/2026/AM-25-11-28-SC.md`
- [ ] AI and Bangsamoro Governance guidebook cites A.M. No. 25-11-28-SC in Chapters 3, 7, 12, 17, and 18
- [ ] Legal Research Guidebook Chapter 14 exists and follows guidebook conventions
- [ ] Bill Drafting Guidebook AI chapter exists and follows guidebook conventions
- [ ] All A.M. No. 25-11-28-SC citations verified against the transcription
- [ ] All cross-references between guidebooks are bidirectional and accurate
- [ ] Authority chain works: domain chapter -> universal guidebook -> A.M. No. 25-11-28-SC -> Constitution Art. VIII, Sec. 5(5)
- [ ] No guidebook cited as a primary source for legal claims
- [ ] AI Disclosure Template is consistent across all three guidebooks

## Execution Notes

- **Task dependencies:** Task 1 must complete before Tasks 2-9 (they cite the transcription)
- **Tasks 2-6 are independent** of each other and can run in parallel
- **Tasks 7-9 depend on Task 6** (they reference the updated universal guidebook)
- **Estimated scope:** 9 tasks, ~3-4 sessions
- **Phase 1 alone** (Task 1) is a clean deliverable — can be committed independently
- **Phase 2** (Tasks 2-6) is a clean deliverable — can be committed as one batch
- **Phase 3** (Tasks 7-9) is a clean deliverable — each guidebook chapter can be committed independently
