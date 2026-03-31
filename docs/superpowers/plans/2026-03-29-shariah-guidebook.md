# Shari'ah Guidebook Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create an independently-authored guidebook on Shari'ah and its application in Bangsamoro governance, legislation, and development — a practitioner's guide, not a fiqh treatise.

**Architecture:** The guidebook teaches governance practitioners (legislative staff, MOA legal officers, planners, cooperative organizers, consultants) how to legislate Shari'ah in BARMM — whether as standalone legislation or as a mainstreaming approach — research the enacted and scriptural legal framework, navigate court jurisdiction, produce Shari'ah legal analysis, handle Islamic finance instruments, and know when to refer to the BDI for binding rulings. Grounded in the complete local Islamic source library (Qur'an + Kutub al-Sittah + BOL + PD 1083).

**Tech Stack:** Markdown content, `/guidebook-writer` for production, `/shariah` skill for research, `/legal-researcher` for provision extraction, `/fact-checker` for verification, `/citation` for footnotes.

**Author:** Saidamen R. Mambayao (independent governance practitioner)

**Source prompt:** `~/Vault/Prompts/260329-2200-shariah-guidebook-plan.md`

---

## Approved Structure (2026-03-31)

### Front Matter
- About This Guidebook (Purpose, Audience, How to Use, AI Declaration)
- About the Author

### Part I — Foundations

**Chapter 1 — Why Shari'ah Matters in Bangsamoro Governance**
- 1.1 What This Guidebook Is — and What It Is Not
- 1.2 The Bangsamoro Identity and Islamic Governance
- 1.3 Who This Guidebook Is For
- 1.4 The Institutional Boundary: Legal Analysis vs. Binding Religious Rulings
- 1.5 How to Use This Guidebook

**Chapter 2 — The Constitutional and Legal Framework**
- 2.1 The 1987 Constitution and Autonomous Regions (Art. X)
- 2.2 The BOL as Social Compact — Nested Sovereignty
- 2.3 BOL Article X: The 20 Sections (complete walkthrough)
- 2.4 Sources of Shari'ah Recognized by the BOL (Qur'an, Sunnah, Ijma', Qiyas)
- 2.5 The "Exclusively Muslim" Scope and Voluntary Submission
- 2.6 Constitutional Constraints on Shari'ah Legislation (Bill of Rights, due process, equal protection)
- 2.7 Worked Example, Common Pitfalls, Quality Checklist

**Chapter 3 — PD 1083: The Code of Muslim Personal Laws**
- 3.1 What PD 1083 Covers (4 Books, 190 Articles)
- 3.2 PD 1083 and the BOL: The Supplementary Relationship
- 3.3 Navigating PD 1083 by Subject (marriage, divorce, inheritance, family relations, property)
- 3.4 When PD 1083 Governs vs. When Parliament Can Legislate
- 3.5 Worked Example, Common Pitfalls, Quality Checklist

**Chapter 4 — The Shari'ah Court System**
- 4.1 Shari'ah Circuit Courts (Art. X, Sec. 5)
- 4.2 Shari'ah District Courts (Art. X, Sec. 6)
- 4.3 The Shari'ah High Court (Art. X, Sec. 7)
- 4.4 The Jurisdictional Matrix (subject matter + monetary thresholds)
- 4.5 Appellate Pathway (Circuit → District → High Court → Supreme Court)
- 4.6 Qualifications of Judges (Art. X, Secs. 8-10)
- 4.7 Traditional and Tribal Justice (Art. X, Secs. 17-18)
- 4.8 Alternative Dispute Resolution (Art. X, Secs. 19-20)
- 4.9 The Interim Pathway (pending High Court organization)
- 4.10 Worked Example: Determining Court Jurisdiction
- 4.11 Common Pitfalls, Quality Checklist

**Chapter 5 — Maqasid al-Shari'ah as a Policy Framework**
- 5.1 The Five Objectives (Faith, Life, Intellect, Lineage, Property)
- 5.2 Maqasid as a Legislative Lens — Scholarly Framework Informing Legislation
- 5.3 How Maqasid Aligns with the BDP and Mas Matatag Agenda
- 5.4 Application in Program Design and Policy Analysis
- 5.5 When Maqasid Analysis Needs BDI Consultation
- 5.6 Worked Example, Common Pitfalls, Quality Checklist

### Part II — Researching Shari'ah

**Chapter 6 — Using Primary Islamic Sources**
- 6.1 Why Practitioners Need Access to Primary Sources
- 6.2 Building Your Own Islamic Source Library
  - The Qur'an: recommended translations (Sahih International, Muhammad Muhsin Khan), digital sources (quran.com API, Tanzil.net)
  - The Kutub al-Sittah (Six Major Hadith Collections): what they are, which to prioritize, digital sources (sunnah.com, hadith-api)
  - Tafsir: Ibn Kathir (Abridged) as the standard reference, how to access
  - Organizing sources for searchability: per-book files, consistent formatting, keyword-searchable text
- 6.3 Hierarchy of Authority: Qur'an → Bukhari/Muslim → Sunan Collections
- 6.4 Research Methodology: Finding Relevant Scriptural Sources
- 6.5 Cross-Collection Verification and *Muttafaq 'Alayh*
- 6.6 The Madhhab Dimension: Shafi'i/Hanafi Practice in the Philippines
- 6.7 Worked Example: Researching a Shari'ah Topic from Scratch

**Chapter 7 — Producing Shari'ah Legal Analysis**
- 7.1 Citing Scriptural Sources in Official Documents (the footnote protocol)
- 7.2 Shari'ah Legal Opinions: IRAC Methodology with Islamic Sources
- 7.3 When Scholarly Disagreement (*Ikhtilaf*) Affects Your Work
- 7.4 The BDI Referral: When Analysis Reaches Its Limit
- 7.5 Worked Example: From Research to Legal Opinion
- 7.6 Common Pitfalls, Quality Checklist

### Part III — Legislating Shari'ah

**Chapter 8 — Legislative Strategy: Standalone vs. Mainstreaming**
- 8.1 The Strategic Question: How Should Parliament Legislate Shari'ah?
- 8.2 Standalone Approach — Dedicated Shari'ah BAAs
- 8.3 Mainstreaming Approach — Shari'ah Provisions in Every BAA
- 8.4 Hybrid Approach — Foundational Code + Mainstreaming Checklist
- 8.5 Analysis: Which Approach Fits BARMM's Legislative Reality?
- 8.6 Recommendation: A Phased Hybrid Strategy
- 8.7 Worked Example: Mapping a Legislative Agenda for Shari'ah
- 8.8 Common Pitfalls, Quality Checklist

**Chapter 9 — The Shari'ah Checkpoint for Bill Drafting**
- 9.1 When a Bill Has a Shari'ah Dimension
- 9.2 The Shari'ah Compliance Review Process
- 9.3 Drafting Shari'ah-Consistent Legislation
- 9.4 The Role of the BDI in Legislative Review (BAA 13, Secs. 52-56)
- 9.5 Worked Example: Reviewing a Draft BAA
- 9.6 Common Pitfalls, Quality Checklist

**Chapter 10 — The Current Legislative Landscape**
- 10.1 Foundational Codes with Embedded Islamic Principles
- 10.2 Bills with Explicit Shari'ah Integration
- 10.3 Bills with Implicit Shari'ah Alignment
- 10.4 Legislative Gaps: Where Parliament Has Not Yet Acted
- 10.5 Comparative: How Other Autonomous Muslim Regions Legislate Shari'ah

### Part IV — Applying Shari'ah in Development

**Chapter 11 — Islamic Finance for Cooperatives and Social Enterprises**
- 11.1 The Legal Framework (BOL Art. X, Sec. 4 + RA 9520)
- 11.2 Key Instruments: Mudarabah, Musharakah, Murabaha
- 11.3 Waqf and Zakat
- 11.4 Shari'ah-Compliant Cooperative Bylaws
- 11.5 The Dual Compliance Challenge: RA 9520 + Islamic Finance Principles
- 11.6 Worked Example: Structuring a Shari'ah-Compliant Cooperative
- 11.7 Common Pitfalls, Quality Checklist

**Chapter 12 — Halal Economy and Regulatory Framework**
- 12.1 Halal Certification in BARMM
- 12.2 The Mas Matatag Agenda and Halal Economy
- 12.3 BOL Provisions for Halal Regulation
- 12.4 National Halal Framework and BARMM's Role
- 12.5 Opportunities for Development Practitioners

### Part V — Practical Tools

**Chapter 13 — The Practitioner's Toolkit**
- 13.1 Shari'ah Checkpoint Checklist (detachable)
- 13.2 Jurisdictional Determination Worksheet (detachable)
- 13.3 Shari'ah Compliance Flags Template (detachable)
- 13.4 Islamic Finance Instrument Quick Reference (detachable)
- 13.5 PD 1083 Subject Index
- 13.6 BOL Art. X Section-by-Section Quick Reference
- 13.7 Kutub al-Sittah Quick Reference (6 collections, book counts, recommended digital sources)
- 13.8 Qur'an and Hadith Citation Format Quick Reference (with examples)
- 13.9 When to Refer to BDI (decision tree)
- 13.10 AI in Practice: AI-Assisted Shari'ah Legal Analysis

**Glossary of Shari'ah and Islamic Legal Terms**

**Bibliography and References**

**Appendices**
- A. BOL Article X — Verbatim Text (all 20 sections)
- B. PD 1083 Table of Contents with Article Index
- C. Shari'ah-Relevant BAAs and Bills Index
- D. Kutub al-Sittah Collection Summary (6 collections, book counts, recommended digital sources)
- E. BAA 13 Secs. 52-56 — Bangsamoro Darul-Ifta Verbatim Text
- F. AI Declaration

---

## Key Design Decisions

1. **Practitioner AND analyst.** The guidebook teaches both WHERE Shari'ah intersects your work AND HOW to produce Shari'ah legal analysis — same standard as secular legal work. Binding religious rulings (*fatawa*) are the BDI's mandate, but legal analysis, research, and opinion-writing are practitioner skills.

2. **Legislative strategy is the core question.** Chapter 6 (standalone vs. mainstreaming) is the most important chapter. The answer to "how should we legislate Shari'ah?" drives everything else. This is the question the Bangsamoro Parliament needs answered.

3. **Constitutional framework first.** Chapter 2 establishes that Shari'ah in BARMM operates within the Philippine constitutional system. This is the legal reality that enables — not limits — Shari'ah legislation.

4. **Primary sources guide.** Chapter 12 teaches practitioners how to build their own searchable Islamic source library (Qur'an + Kutub al-Sittah) using publicly available digital sources (quran.com, sunnah.com, hadith-api). The guidebook does NOT assume any specific local setup — it provides the methodology and recommended sources. Scriptural citations in the guidebook itself will follow the footnote protocol in Ch. 12.5.

5. **Gemini framework as INFERRED source.** The BARMM Shari'ah Legislation Framework PDF (29 pages) informs the structure but every claim must be verified against BOL and PD 1083. The SLRB proposal in the Gemini PDF was verified as fabricated — it does not exist in any enacted law and has been removed from the plan.

6. **AI Declaration.** Follows the "Both + AI Declaration" pattern — AI in Practice callouts in relevant chapters plus the standard disclosure in the About section.

7. **Each guidebook is independent.** This is NOT part of a "series." It stands alone. It cross-references the Legal Research Guidebook (Ch. 9) and the Cooperative Development Guidebook (Ch. 9) by title.

8. **Madhhab-aware.** PD 1083 follows Hanafi/Shafi'i traditions as practiced in the Philippines. When fiqh analysis is required, the guidebook presents relevant school positions with evidence, defaulting to Shafi'i/Hanafi context unless broader analysis is needed.

---

## Prerequisites Before Writing

- [ ] Transcribe A.M. No. 25-11-28-SC to `jurisprudence/2026/AM-25-11-28-SC.md` (for AI Declaration)
- [ ] Verify key claims in the Gemini Shari'ah framework PDF against BOL Art. X and PD 1083
- [ ] Read the full PD 1083 transcription at `legislation/national-laws/PD-1083.md`
- [ ] Search `legislation/bills/` for all Shari'ah-relevant filed bills
- [ ] Search `legislation/BAAs/` for all BAAs with Shari'ah provisions
- [ ] Create `references/pd-1083-index.md` for the /shariah skill (deep investment from analysis)

## Estimated Scope

- 13 chapters (6 Parts) + front matter + glossary + bibliography + 6 appendices
- Comparable to Legal Research Guidebook (~350-450 pages as PDF)
- Production pipeline: `/guidebook-writer` → `/shariah` (Modes 3, 6, 7) → `/legal-researcher` → `/fact-checker` → `/citation` → PDF generation
- Key new capability: Ch. 6 (legislative strategy) and Ch. 12 (scriptural research) leverage the complete local Islamic source library built 2026-03-30/31

## Status: PLANNED — Ready for execution

### Updates Log
- 2026-03-29: Initial plan created
- 2026-03-31: Major revision — removed fabricated SLRB, updated institutional boundary (AI produces legal analysis, BDI issues fatawa), added Ch. 6 (standalone vs. mainstreaming legislative strategy), added Ch. 12 (scriptural research using local Qur'an + Kutub al-Sittah), added Part V, renumbered chapters 6-13, updated key design decisions 1-8
