# Legal Reference Template

This template defines the standard structure for each BOL power's legal reference entry. Every power from Article V, Section 2 (a-ccc) gets one file following this format.

---

## File and Folder Structure

Each power gets its own **folder** to accommodate multiple legal reference files per subject area (e.g., a main legal reference + sub-topic deep dives, comparative analyses, or legislative proposals).

```
legal-references/
  01-a-administration-of-justice/
    legal-reference.md          ← main legal reference (this template)
    shariah-court-jurisdiction.md   ← optional sub-topic
    traditional-justice-system.md   ← optional sub-topic
  02-b-administrative-organization/
    legal-reference.md
  ...
  11-k-cooperatives/
    legal-reference.md
    shariah-compliant-models.md     ← optional deep dive
  ...
  55-ccc-water-supply/
    legal-reference.md
```

**Folder naming**: `{NN}-{letter}-{short-slug}/` — numbered sequentially following Art. V, Sec. 2 order.
**Main file**: `legal-reference-{short-slug}.md` inside the folder (e.g., `legal-reference-cooperatives.md`, `legal-reference-administration-of-justice.md`).
**Additional files**: any sub-topic, comparative analysis, or legislative proposal relevant to this power.

Full numbering:
01-a, 02-b, 03-c, 04-d, 05-e, 06-f, 07-g, 08-h, 09-i, 10-j,
11-k, 12-l, 13-m, 14-n, 15-o, 16-p, 17-q, 18-r, 19-s, 20-t,
21-u, 22-v, 23-w, 24-x, 25-y, 26-z, 27-aa, 28-bb, 29-cc, 30-dd,
31-ee, 32-ff, 33-gg, 34-hh, 35-ii, 36-jj, 37-kk, 38-ll, 39-mm, 40-nn,
41-oo, 42-pp, 43-qq, 44-rr, 45-ss, 46-tt, 47-uu, 48-vv, 49-ww, 50-xx,
51-yy, 52-zz, 53-aaa, 54-bbb, 55-ccc

---

## Quick Conformance Check

Before submitting a power file, verify:

### Structure
- [ ] File named `legal-reference-{slug}.md` in folder `{NN}-{letter}-{slug}/`
- [ ] Legal Sources section has all 8 tables (BOL, BAAs, Resolutions, National Laws, Shari'ah Sources, Jurisprudence, Pending PBs, Development Alignment)
- [ ] Legal Briefer has 9 themes (A-I) with correct lettering
- [ ] Legislative Gaps table at the bottom (separate from Section G (Legislative Gaps))
- [ ] Footnotes in Feliciano format

### Content
- [ ] BOL Provisions: ALL provisions listed with ***bold italic*** verbatim text + explanation
- [ ] BAAs: PB No. column (not "Bill No." or "Enacted Bills")
- [ ] Resolutions: PR No. column
- [ ] National Laws: comprehensive scan of `national-laws/INDEX.md` + `executive-orders/INDEX.md` (not just BOL-cited laws)
- [ ] BAA 13 mandate: read from actual source file (Sec. XX-XX), enumerate ALL functions
- [ ] Zero instances of "Exclusive", "Shared", or "Concurrent"
- [ ] All BAA numbers verified against `legislation/baas/BAA-{N}.md`
- [ ] Em dashes use `—` (actual character), zero instances of `---` (triple hyphens) as em dashes

### Redundancy and Flow Checkpoint
After writing all 9 themes, re-read the entire Legal Briefer and verify:
- [ ] **No fact stated twice**: each fact (BOL limitation, constitutional provision, national law, Shari'ah principle, BAA function) appears in ONE theme only. Later themes cross-reference earlier ones using "As established in the relevant section..."
- [ ] **Logical flow**: A reader going A→B→C→D→E→F→G→H→I should build understanding progressively — each theme adds NEW information, not restated information
- [ ] **A (BOL)** does NOT describe implementation details (that's D)
- [ ] **B (Constitutional)** does NOT describe how BARMM implements (that's D) or how far it can diverge (that's F)
- [ ] **C (National Law)** does NOT describe what national agencies DO operationally (that's D.2) — only lists what laws/institutions exist
- [ ] **D (Implementation)** does NOT restate BOL provisions (that's A) or constitutional provisions (that's B)
- [ ] **E (Shari'ah)** does NOT list national laws (that's C) — only Shari'ah-specific sources and principles
- [ ] **F (Divergence)** does NOT restate BOL limitations (already in A) or constitutional floor (already in B) — synthesizes A-E and references them, including Shari'ah (E) as a basis for divergence
- [ ] **G (Gaps)** does NOT re-list unfulfilled mandates (already in A) or recommended legislation (already in the table) — only analyzes jurisdictional overlaps and pending PBs
- [ ] **I (Power-Specific)** does NOT re-explain Shari'ah models (already in E) — references E for Shari'ah detail

---

## Template Structure

```markdown
# (x) [Power Name as stated in BOL]

> **BOL Art. V, Sec. 2({letter})** — "[Verbatim text from BOL]"

## Power Overview

| Attribute | Value |
|-----------|-------|
| **BOL Basis** | Art. V, Sec. 2({letter}) — enumerated power |
| **National Law Consistency Required** | Yes (cite BOL provision) / No / Intergovernmental coordination (cite Art. VI body) |
| **Lead Ministry/Office** | [From BAA No. 85 and BAA No. 13] |
| **Supporting Agencies** | [Other BARMM bodies with jurisdiction] |
| **BDP Chapter(s)** | [BDP 2023-2028 chapter alignment] |
| **Priority Code** | [If covered by a priority code, e.g., Administrative Code, Education Code] |

## Legal Sources

The reference tables below present the raw legal data — BOL provisions, enacted legislation, national laws, jurisprudence, and pending bills. Read these first to see the legal landscape, then proceed to the Legal Briefer Q&A for analysis and interpretation.

### BOL Provisions

All BOL provisions relevant to this power — verbatim text with explanation of what each provision means in practice.

<table>
<colgroup>
  <col style="width:15%">
  <col style="width:40%">
  <col style="width:45%">
</colgroup>
<thead>
<tr><th>Provision</th><th>Verbatim Text</th><th>Explanation / Implication</th></tr>
</thead>
<tbody>
<tr>
  <td>Art. V, Sec. 2({letter})</td>
  <td><em><strong>"[Verbatim text of the enumerated power]"</strong></em></td>
  <td>[What this grant of authority means — scope, what it authorizes the Bangsamoro Government to do]</td>
</tr>
<tr>
  <td>Art. [X], Sec. [Y]</td>
  <td><em><strong>"[Verbatim excerpt from BOL]"</strong></em></td>
  <td>[What this provision means in practice — does it expand, limit, create a body, mandate legislation, require coordination? Plain language explanation.]</td>
</tr>
</tbody>
</table>

### Bangsamoro Legislation (BAAs)

Enacted legislation. A Parliament Bill (PB) becomes a BAA when enacted.

<table>
<colgroup>
  <col style="width:12%">
  <col style="width:13%">
  <col style="width:30%">
  <col style="width:30%">
  <col style="width:15%">
</colgroup>
<thead>
<tr><th>BAA</th><th>PB No.</th><th>Title</th><th>How It Implements This Power</th><th>Status</th></tr>
</thead>
<tbody>
<tr>
  <td>BAA No. [N]</td>
  <td>PB No. [N]</td>
  <td>[Full title]</td>
  <td>[Brief description of what the BAA does for this power area]</td>
  <td>In Force / Amended by BAA [N]</td>
</tr>
</tbody>
</table>

### Parliamentary Resolutions

Adopted resolutions. A Proposed Resolution (PR) becomes an enacted Resolution when adopted.

<table>
<colgroup>
  <col style="width:15%">
  <col style="width:12%">
  <col style="width:38%">
  <col style="width:35%">
</colgroup>
<thead>
<tr><th>Resolution No.</th><th>PR No.</th><th>Title / Subject</th><th>Relevance</th></tr>
</thead>
<tbody>
<tr>
  <td>Res. No. [N]</td>
  <td>PR No. [N]</td>
  <td>[Title]</td>
  <td>[How it relates to this power]</td>
</tr>
</tbody>
</table>

### National Laws

All Republic Acts, Executive Orders, and Presidential Decrees pertaining to this power area.

<table>
<colgroup>
  <col style="width:15%">
  <col style="width:25%">
  <col style="width:30%">
  <col style="width:30%">
</colgroup>
<thead>
<tr><th>Law</th><th>Title</th><th>Relationship to This Power</th><th>Application in BARMM</th></tr>
</thead>
<tbody>
<tr>
  <td>RA [N] / EO [N] / PD [N]</td>
  <td>[Full title]</td>
  <td>[BOL requires consistency (cite provision) / Suppletory (no BAA exists) / BOL explicitly references / Sets minimum standards / General framework]</td>
  <td>[How it interacts with Bangsamoro authority — does it apply directly, suppletorily, or is it superseded by a BAA?]</td>
</tr>
</tbody>
</table>

### Shari'ah Sources

Islamic legal principles, existing Shari'ah legislation, and scholarly opinions relevant to this power area.

<table>
<colgroup>
  <col style="width:20%">
  <col style="width:35%">
  <col style="width:45%">
</colgroup>
<thead>
<tr><th>Source</th><th>Provision / Principle</th><th>Application to This Power</th></tr>
</thead>
<tbody>
<tr>
  <td>[PD 1083 / BOL Art. X / *Maqasid al-Shari'ah* / *Fatwa* / Shari'ah court ruling]</td>
  <td>[Specific provision, principle, or ruling — verbatim where possible]</td>
  <td>[How it applies to this power area — what it requires, permits, or prohibits]</td>
</tr>
</tbody>
</table>

### Jurisprudence

Supreme Court decisions relevant to this power area — defining boundaries of autonomy, resolving jurisdiction questions, or interpreting related provisions.

<table>
<colgroup>
  <col style="width:20%">
  <col style="width:15%">
  <col style="width:40%">
  <col style="width:25%">
</colgroup>
<thead>
<tr><th>Case</th><th>Date</th><th>Holding / Relevance</th><th>Impact on This Power</th></tr>
</thead>
<tbody>
<tr>
  <td>[Case name, G.R. No.]</td>
  <td>[Date decided]</td>
  <td>[Key holding or ratio decidendi relevant to this power]</td>
  <td>[How this decision affects the exercise of this power by the Bangsamoro Government]</td>
</tr>
</tbody>
</table>

### Parliament Bills (Pending)

Filed Parliament Bills (PBs) that have NOT yet been enacted into BAAs. Shows legislative intent and pending proposals.

<table>
<colgroup>
  <col style="width:12%">
  <col style="width:40%">
  <col style="width:33%">
  <col style="width:15%">
</colgroup>
<thead>
<tr><th>PB No.</th><th>Title / Subject</th><th>Relevance to This Power</th><th>Status</th></tr>
</thead>
<tbody>
<tr>
  <td>PB No. [N]</td>
  <td>[Title]</td>
  <td>[What this bill would do for this power area]</td>
  <td>Filed / Committee / Plenary</td>
</tr>
</tbody>
</table>

### Development Plan and Policy Alignment

| Framework | Reference | Connection |
|-----------|-----------|------------|
| BDP 2023-2028 | Chapter [N]: [Topic] | [How this power enables BDP goal achievement] |
| Mas Matatag na Bangsamoro Agenda (2026-2028) | Pillar [N]: [Name] | [How this power supports the Matatag pillar] |

---

## Legal Briefer

A granular Q&A analysis. Answers stay as close as possible to the language of the law. All verbatim statutory text in ***bold italic***. Key terms in **bold**. Themes follow the legal hierarchy and analytical flow: BOL grant → constitutional floor → national law → implementation → Shari'ah dimension → divergence → gaps → development.

### A. BOL Grant and Scope

**Q. What power does the BOL grant the Bangsamoro Government in this area?**
A. [Answer using the verbatim Art. V, Sec. 2 text, then explain its scope.]

**Q. What specific BOL provisions elaborate on this power beyond Art. V, Sec. 2?**
A. [Walk through each elaborating provision with near-verbatim text. For each, state what it adds — does it define scope, create a body, mandate legislation, set limits, or grant fiscal authority? Cite as "Art. [X], Sec. [Y]."]

**Q. Does the BOL mandate the Parliament to enact specific legislation for this power?**
A. [If yes, quote the mandate verbatim. If no express mandate, state so.]

**Q. Does the BOL create any specific body, office, or institution for this power?**
A. [Name the body and cite the provision. If the BOL directs Parliament to create one, quote the directive.]

**Q. What conditions, limitations, or qualifications does the BOL place on this power?**
A. [Quote any limiting language — "subject to," "consistent with," "without prejudice to," "upon approval of." Cite each provision.]

### B. Constitutional Considerations

**Q. What constitutional provisions apply to this subject area?**
A. [Start with the universal constraint, then identify subject-specific provisions:
- **Universal (applies to ALL 55 powers)**: Art. X, Sec. 20 — autonomous regions operate ***"within the framework of this Constitution."***
- **Subject-specific articles**: Art. XII (National Economy), Art. XIII (Social Justice), Art. XIV (Education/Culture), Art. III (Bill of Rights) — as applicable.
- **State policies (Art. II)**: Declaration of Principles relevant to this power area.]

**Q. What rights and privileges does the Constitution guarantee in this area?**
A. [Identify specific constitutional rights: equal protection, due process, freedom of association, social and economic rights, rights of specific groups. For each, state what it guarantees and what it means for how BARMM must exercise this power.]

**Q. What constitutional mandates exist for legislation or institutions in this area?**
A. [Identify "Congress shall..." or "The State shall..." mandates. If a national law implements a constitutional mandate, it carries constitutional weight even without a BOL consistency requirement.]

### C. National Law Considerations

**Q. What does the current national legal framework provide for this subject area?**
A. [Describe comprehensively — protections, standards, institutions, regulatory mechanisms. This is the baseline against which BARMM legislation will be compared.]

**Q. What national laws currently apply in BARMM?**
A. [List each RA/EO/PD. Explain whether it applies **directly**, **suppletorily**, or is **superseded** by a BAA.]

**Q. What national institutions exercise authority in BARMM for this area?**
A. [Name national agencies. Explain: will authority transfer when a BAA is enacted, or do they retain concurrent jurisdiction?]

### D. Implementation

#### D.1 How the Bangsamoro Government Implements This Power

**Q. Which ministry or office is primarily responsible for exercising this power?**
A. [Name the lead ministry/office. Cite BAA 13 (specific Book/Title/Section) and BAA 85 (Chapter).]

**Q. What standalone legislation (BAAs) has the Parliament enacted for this power?**
A. [List each BAA by number, PB number, title, and what it does. If none, state so.]

**Q. What are the lead ministry's mandate and functions under BAA 13?**
A. [**MANDATORY**: Read the actual BAA 13 sections for this ministry/office — do NOT summarize from memory. Cite the specific Book, Title, Chapter, and Section numbers. Enumerate each function listed in the "Powers and Functions" section. Quote the mandate verbatim in ***bold italic***. Name the organizational divisions and their specific responsibilities. This answer must be a precise, citable account of what BAA 13 authorizes.]

**Q. What can the lead ministry NOT do without a standalone BAA beyond BAA 13?**
A. [Distinguish between what BAA 13 already provides (institutional existence, general functions, organizational structure) vs. what requires a dedicated code or act (comprehensive regulatory framework, detailed standards, penalty provisions, fiscal mechanisms, Shari'ah-compliant models, jurisdictional boundaries with national counterparts). BAA 13 creates the institution; the standalone BAA creates the regulatory code.]

**Q. Have any parliamentary resolutions signaled intent to legislate in this area?**
A. [List resolutions by number and subject. If none, state so.]

#### D.1.A Institutional Validation

**Q. Is the assigned lead MOA the correct one for this power?**
A. [Validate the MOA assignment. Some powers have obvious leads (MAFAR for agriculture, MBHTE for education). Others are less clear:
- Does the assigned MOA's BAA 13 mandate actually cover the FULL scope of this power — or only part of it?
- Is there a mismatch between the power's scope and the MOA's mandate? (e.g., "administration of justice" is broader than BAGO's prosecution/legal services mandate — it includes Shari'ah courts, traditional justice, ADR)
- Are there multiple MOAs that exercise parts of this power? If so, which is the primary coordinator?
- Does the BOL assign this power to a specific institution that is DIFFERENT from the BAA 13 assignment?]

**Q. What BARMM institutions currently exist for this power?**
A. [List ALL existing institutions — not just the lead MOA:
- **Lead ministry/office**: [name, BAA 13 section, BAA 85 chapter]
- **Supporting agencies**: [name, basis for involvement]
- **Commissions**: [BWC, BYC, BHRC, BSC, etc. — if relevant]
- **Special bodies**: [boards, councils, task forces created by BAA or EO]
- **Shari'ah institutions**: [courts, Darul Ifta', SLRB — if relevant]
- **LGU-level offices**: [mandated by BAA 49 or national law — if relevant]
For each, state: (a) what law created it, (b) whether it is operational, (c) what specific role it plays for this power.]

**Q. What institutions does the BOL mandate that have NOT been created yet?**
A. [Check whether the BOL directs Parliament to create specific bodies for this power that do not yet exist. Examples:
- Art. VII, Sec. 42: Parliament may create offices for youth, women, settler communities, DRRM, planning
- Art. X, Sec. 16: Parliament may create Shari'ah public assistance office, prosecution service, academy, Jurisconsult office
- Art. XIII, Sec. 28: Bangsamoro Economic Zone Authority (BEZA)
- Art. VI, Sec. 8: Bangsamoro Sustainable Development Board (created by BAA 31)
Quote the BOL provision. State whether the institution has been created (by BAA or EO) or remains unestablished.]

**Q. Does this power require creating NEW institutions that the BOL does not specifically name?**
A. [Beyond BOL-mandated bodies, analyze whether fully exercising this power requires institutions that don't exist:
- A regulatory body (e.g., CSEA for cooperatives — exists; a Bangsamoro FDA equivalent — doesn't)
- A dispute resolution mechanism (e.g., cooperative mediation — CSEA has this; environmental tribunal — doesn't exist)
- An interagency coordination body (e.g., DRRM Council exists; a maritime coordination body for inland waterways — doesn't)
- A specialized fund or financing institution
Name the proposed institution, what it would do, and what law would create it.]

#### D.2 How the National Government Implements This Power

**Q. How does the national government currently exercise authority in this area within BARMM?**
A. [Describe what national agencies do on the ground in BARMM for this subject — registration, regulation, enforcement, service delivery, program implementation. Name specific agencies and their functions.]

**Q. What national government programs and services operate in BARMM for this area?**
A. [List specific programs — e.g., DepEd school building program, DOH retained hospitals, DOLE employment facilitation, CDA cooperative registration. These are the national government's operational presence.]

**Q. What is the status of devolution for this power — has authority been transferred from national agencies to BARMM?**
A. [Explain: has the national agency's function been devolved to the BARMM ministry? Is devolution complete, partial, or pending? What still needs to be transferred? Cite any EO, MOA, or transition plan governing the devolution.]

**Q. Are there areas where both national and Bangsamoro agencies operate concurrently?**
A. [Identify overlapping jurisdictions — where both national and BARMM agencies exercise functions. Explain: is this by design (BOL requires it), by default (devolution incomplete), or by gap (no BAA clarifies the boundary)?]

#### D.3 BARMM Implementation

**Q. What has the BARMM accomplished so far in exercising this power?**
A. [Concrete achievements — not just "institution exists" but what it has actually done. Laws enacted, programs launched, entities registered, services delivered, standards enforced, institutions operationalized. Be specific with numbers and dates where possible.]

**Q. Where is the BARMM stronger than the national government in this area?**
A. [Identify BARMM's unique advantages — areas where the national system cannot match BARMM's approach:
- **Shari'ah integration** — does BARMM offer Shari'ah-compliant options the national system doesn't?
- **Cultural and linguistic fit** — does BARMM deliver in ways that resonate with the Bangsamoro population?
- **Conflict-sensitive design** — does BARMM's approach account for post-conflict realities (IDPs, ex-combatants, contested lands)?
- **Institutional innovation** — has BARMM designed something new that the national system never created?
If BARMM is not stronger in any area, state so and explain why.]

**Q. What is holding BARMM back from full implementation?**
A. [Identify the binding constraints — the specific things preventing BARMM from doing more:
- **Legal gap** — no standalone BAA, so the ministry cannot register, regulate, or enforce?
- **Institutional capacity** — ministry exists but understaffed, underfunded, or lacking expertise?
- **Devolution incomplete** — national agency hasn't transferred functions, data, or assets?
- **Coordination failure** — unclear jurisdictional boundary with national agencies?
Name the single biggest constraint and what would remove it.]

#### D.4 National Government Implementation

**Q. What has the national government built for this area that BARMM does not yet have?**
A. [Concrete national systems, infrastructure, and track record — what BARMM is working from behind on:
- **Legislative depth** — comprehensive codes with decades of amendments, IRRs, and jurisprudence
- **Institutional infrastructure** — established agencies with specialist staff, regional offices, enforcement arms
- **Regulatory systems** — registration databases, licensing frameworks, inspection regimes, adjudication mechanisms
- **IT and data** — online registration, national databases, monitoring dashboards
Be specific: name the agency, the system, and how long it has been operating.]

**Q. Where does the national system fall short for BARMM?**
A. [Identify where the national framework fails BARMM's needs — the one-size-fits-all problem:
- Does the national framework accommodate **Shari'ah-compliant** alternatives?
- Does it account for **conflict-affected** communities, **IDP** populations, or **post-conflict** realities?
- Does it deliver services in **local languages** and through **culturally appropriate** channels?
- Does the national agency's presence in BARMM match its presence elsewhere — or is BARMM **underserved**?
This is the case for why BARMM needs its own framework, not just the national one.]

**Q. What should BARMM replicate, adapt, or replace from the national system?**
A. [For each major element of the national framework:
- **Replicate** — adopt as-is because it works and context doesn't require changes (e.g., audit standards, financial reporting)
- **Adapt** — take the national model and modify for BARMM context (e.g., registration system with Shari'ah-compliant track)
- **Replace** — build something entirely different because the national approach doesn't fit (e.g., *mudarabah*-based cooperative models instead of interest-based)
This guidance directly informs what a standalone BAA should contain.]

### E. Shari'ah Considerations

**Q. Does this power have a Shari'ah dimension?**
A. [State whether Islamic law is relevant to this subject area. For some powers (Islamic banking, Hajj, administration of justice, cooperatives, customary laws, family-related matters) Shari'ah is central. For others (public works, cadastral survey, sports) it may be minimal or indirect. Even where indirect, consider whether Islamic principles (e.g., *maslahah* / public interest, *'adl* / justice, *amanah* / trust) inform how the power should be exercised.]

**Q. What does the BOL say about Shari'ah in relation to this power?**
A. [Cite any BOL provisions that reference Shari'ah, Islamic law, or Islamic institutions for this subject area. Key provisions: Art. X (entire — Shari'ah justice system), Art. X Sec. 4 (Parliament may enact Shari'ah laws on personal, family, property, commercial, and criminal matters), Art. IX Sec. 14 (*madaris* education). If the BOL is silent on Shari'ah for this specific power, state so.]

**Q. What Shari'ah principles are relevant to legislation in this area?**
A. [Identify the Islamic legal principles that should guide Bangsamoro legislation on this subject:
- ***Maslahah*** (public interest / welfare) — does legislation serve the common good?
- ***'Adl*** (justice / equity) — does it treat people fairly?
- ***Amanah*** (trust / stewardship) — does it impose accountability on those exercising authority?
- ***Shura*** (consultation) — does the legislative process include stakeholder participation?
- **Subject-specific**: for economic powers, consider prohibition of *riba* (interest/usury), *gharar* (excessive uncertainty), *maysir* (gambling); for cooperatives, consider *mudarabah*, *musharakah*, *murabaha*; for justice, consider *ta'zir* (discretionary punishment), *sulh* (mediation/settlement).
If no specific Shari'ah principles apply, state: "No specific Shari'ah principles beyond the general values of *maslahah*, *'adl*, and *amanah* directly govern this power area."]

**Q. What existing Shari'ah legislation or jurisprudence applies?**
A. [Identify:
- **PD 1083** (Code of Muslim Personal Laws, 1977) — does it cover any aspect of this power? PD 1083 governs personal status, marriage, divorce, succession, property for Muslims.
- **BOL Art. X, Sec. 4** — has Parliament enacted any Shari'ah law on this subject?
- **Shari'ah court jurisdiction** — do Shari'ah courts have jurisdiction over disputes arising from this power area (personal, family, property, commercial)?
- **Islamic scholarly opinions** (*fatawa*) — are there relevant opinions from the Bangsamoro *Darul Ifta'* or recognized *ulama* bodies?]

**Q. How should Shari'ah compliance be integrated into Bangsamoro legislation for this power?**
A. [For powers with a significant Shari'ah dimension: should compliance be mandatory (all entities must comply), optional (Shari'ah-compliant track available alongside conventional), or principled (legislation guided by Islamic values without mandating specific compliance)? What institutional mechanism ensures Shari'ah review — a Shari'ah Legislative Review Board (SLRB), *ulama* committee, or certification process?]

### F. Divergence Analysis

[NOTE: Do NOT repeat BOL consistency requirements or limitations already stated in Section A (BOL Grant and Scope). Do NOT restate the constitutional floor already established in Section B (Constitutional Considerations). Reference those themes instead. This theme synthesizes A-E — including the Shari'ah dimension from Section E (Shari'ah Considerations) as a unique basis for divergence.]

**Q. To what extent can the BARMM diverge from national law and policy in this area?**
A. [The critical analytical question. Synthesize from A (BOL limitations), B (constitutional floor), C (national framework), D (implementation reality), and E (Shari'ah dimension) to determine: what can BARMM do differently, and where are the limits? Four scenarios: BOL requires consistency → must conform; BOL is silent → constitutional floor applies; BOL expressly mandates different legislation → strongest basis for divergence; Shari'ah provides additional basis for distinctiveness → unique BARMM justification.]

**Q. If BARMM enacts different standards, what are the implications for rights holders and cross-boundary operations?**
A. [Do persons gain or lose rights? How do entities operating across BARMM/non-BARMM comply? What mutual recognition or comity provisions are needed?]

**Q. What happens to national law when the Parliament enacts a BAA on this subject?**
A. [BAA governs within BARMM; national law applies suppletorily where BAA is silent; constitutional provisions always apply.]

### G. Legislative Gaps and Recommended Legislation

[NOTE: Do NOT repeat the unfulfilled BOL mandates already listed in Section A (BOL Grant and Scope). Do NOT repeat the recommended legislation already listed in the Legislative Gaps table at the bottom. Focus on jurisdictional analysis and pending bills.]

**Q. Are there overlapping or unclear jurisdictions between Bangsamoro and national authority?**
A. [Identify specific overlaps. What legislative or intergovernmental action would resolve them?]

**Q. What pending Parliament Bills address the gaps?**
A. [List pending PBs. What would they accomplish? What gaps remain even if they pass?]

### H. Development and Policy Connection

**Q. Which BDP 2023-2028 goals and Mas Matatag na Bangsamoro Agenda pillars depend on this power?**
A. [Name BDP chapter, goals, Matatag pillar. Explain connection.]

**Q. What development outcomes are at risk if the legislative gaps remain unaddressed?**
A. [Practical consequences — what cannot happen without legislation that BAA 13 alone cannot deliver.]

### I. Power-Specific Questions

[Additional Q&A pairs unique to this power — nuances, complexities, and distinguishing features not covered by the universal questions above. No maximum. Examples:

- For **(a) Administration of Justice**: "What is the jurisdiction of each Shari'ah court level?"
- For **(f) Budgeting**: "What taxes can BARMM NOT impose?"
- For **(v) Education**: "What minimum national standards must BARMM conform to?"
- For **(d) Ancestral Domain**: "What resources require joint exercise with the National Government?"
- For **(i) Civil Service**: "Which law prevails when Bangsamoro and national civil service laws conflict?"

Add as many as the subject demands.]

### Legislative Gaps and Recommended Legislation

What laws should the Bangsamoro Parliament pass to fully exercise this power? Note: most powers are already exercised by MOAs through their BAA 13 (Administrative Code) mandates, but standalone legislation codifies standards, creates regulatory frameworks, and establishes institutional structures that a general mandate cannot.

| Gap Type | Gap | What Law / Institution Should Be Created | What It Would Cover | BOL Basis |
|----------|-----|------------------------------------------|---------------------|-----------|
| **Legislative** | [No standalone code/act] | [Proposed law title, e.g., "Bangsamoro Tourism Code"] | [Regulatory standards, institutional framework, funding, licensing, penalties, coordination] | [BOL provision] |
| **Institutional** | [No MOA exists for this function] | [Proposed institution, e.g., "Bangsamoro Economic Zone Authority (BEZA)"] | [Mandate, powers, functions, organizational structure, relationship with national counterpart] | [BOL provision mandating creation] |

## Footnotes

[^1]: Rep. Act No. 11054, sec. 2(x), art. V.
[^2]: BAA No. [N], sec. [S].
```

---

## Section-by-Section Guidance

### Power Overview
- **BOL Basis**: All 55 powers are enumerated in Art. V, Sec. 2 — this is the express grant of authority.
- **National Law Consistency**: Check whether any BOL provision requires this power to be exercised "consistent with national laws" (e.g., Art. VII Sec. 39 for civil service, Art. VII Sec. 28 for budget, Art. IV Sec. 4 for elections). If the BOL is silent on national law for this power, the Bangsamoro Government's authority is not constrained by national law (though national law applies suppletorily where no BAA exists). If an Art. VI intergovernmental body exists for this area, note it.
- **Lead Ministry**: Derive from BAA No. 85 (General Appropriations Act) which assigns staffing/budget by ministry. Cross-reference with BAA 13 (Administrative Code) for mandate assignments.
- **BDP Chapter**: Map to the 15 chapters of BDP 2023-2028.

### Legal Briefer (Q&A Reviewer Format)
- This is the PRIMARY content of each file — write it thoroughly. The tables are supporting data.
- Write AFTER completing all tables — the Q&A synthesizes the data.
- **Format**: Q&A reviewer style. Each question on its own line prefixed with **Q.**, each answer prefixed with **A.** and indented.
- **Answers must stay as close as possible to the language of the law.** Quote the BOL verbatim where possible. When explaining, use the statutory terms — don't substitute plain language for legal language.
- **Bold italic (`***text***`)** for all verbatim text of the law (BOL, BAA, RA, EO, PD). This visually distinguishes "what the law says" from "what it means." Regular text for explanations. Example: Art. XIII, Sec. 24 states: ***"It shall adopt and implement cooperative development policies and programs through the enactment of a Bangsamoro cooperative code."*** This names the specific legislation by title.
- **Em dash**: Use `—` (actual em dash character), NEVER `---` (triple hyphens). Triple hyphens render as horizontal rules in markdown. Always use the real em dash: `—`.
- **9 themes** following the legal hierarchy: A (BOL) → B (Shari'ah) → C (Constitutional) → D (National Law) → E (Implementation with E.1, E.1.A Institutional Validation, E.2, E.3, E.4) → F (Divergence) → G (Gaps) → H (Development) → I (Power-Specific).
- **Inline citations**: "Art. XIII, Sec. 24", "BAA No. 18", "RA 9520" — within the answer text.
- Target: someone studying this power should be able to look up any specific question and find a direct, law-grounded answer without reading the whole document.
- Total length: 2,000-4,000+ words (varies by power complexity).

### Redundancy Prevention Rules
Each fact should appear in ONE theme only. Later themes reference earlier ones instead of restating:
- **BOL limitations/conditions** → stated ONLY in Section A (BOL Grant and Scope). Themes F and G reference A, not restate.
- **Constitutional floor** (equal protection, due process, Art. XII provisions) → stated ONLY in Section B (Constitutional Considerations). Section F (Divergence Analysis) references B.
- **Unfulfilled BOL mandates** ("Parliament shall enact...") → stated ONLY in Section A (BOL Grant and Scope). Section G (Legislative Gaps) references A.
- **Recommended legislation** → stated ONLY in the Legislative Gaps table at the bottom. Section G (Legislative Gaps) analyzes jurisdictional overlaps and pending PBs, not the legislation itself.
- **National institutions** → listed in Section C (National Law Considerations) (what they are). Section D (Implementation).2 describes what they DO operationally (not what they are again).
- **Shari'ah-specific models/structures** → detailed in Section E (Shari'ah Considerations). Section F (Divergence Analysis) references E for Shari'ah as a basis for divergence, Section I (Power-Specific Questions) references E for Shari'ah questions — don't re-explain the models.
- **Lead ministry BAA 13 mandate** → detailed in Section D (Implementation).1. Section A (BOL Grant and Scope) names the ministry briefly, D.1 does the full enumeration.
- Cross-reference format: "As established in the **Constitutional Considerations** section (Section B), the constitutional floor is Art. XII, Sec. 15..."

### Guide Questions the Legal Briefer Must Answer

**Scope and Authority:**
1. What exactly does the BOL grant the Bangsamoro Government authority over in this area?
2. What specific BOL provisions (beyond Art. V Sec. 2) elaborate on this power?
3. Does the BOL mandate the Parliament to enact specific legislation for this power? If so, what?
4. Are there any conditions, limitations, or qualifications the BOL places on this power?
5. Does the BOL create any specific body, office, or institution for this power?

**Implementation:**
6. Which ministry or office is primarily responsible for exercising this power?
7. What standalone legislation (BAAs) has the Parliament enacted for this power?
8. If no standalone BAA exists, what does the lead ministry's BAA 13 mandate cover?
9. What can the ministry do under its current mandate, and what can it NOT do without standalone legislation?
10. Have any parliamentary resolutions signaled intent to legislate in this area?

**Constitutional Framework:**
11. What constitutional provisions (Art. II, III, X, XII, XIII, XIV) apply to this subject area?
12. What rights and privileges does the Constitution guarantee — and what do they mean for how BARMM must exercise this power?
13. What constitutional mandates for legislation or institutions exist (e.g., "Congress shall...")?

**National Legal Framework:**
14. What does the current national legal framework provide (protections, standards, institutions)?
15. What national laws apply in BARMM — directly, suppletorily, or superseded by BAA?
16. What national institutions exercise authority in BARMM for this area?

**Institutional Validation:**
17. Is the assigned lead MOA actually the correct one — does its BAA 13 mandate cover the FULL scope of this power?
18. What ALL institutions exist for this power (lead, supporting, commissions, Shari'ah, LGU-level)?
19. What institutions does the BOL mandate that haven't been created yet?
20. Does this power require NEW institutions beyond what the BOL names?

**BOL Positioning and Divergence:**
17. Does the BOL require consistency with national law? Presidential approval? Intergovernmental coordination?
18. To what extent can BARMM diverge from national law — and where are the constitutional limits?
19. If BARMM enacts different standards, what are the implications for rights holders and cross-boundary operations?

**Gaps and Opportunities:**
15. What unfulfilled BOL mandates exist — where the BOL says "The Parliament shall enact..." but no legislation has been passed?
16. What would a standalone BAA codify that BAA 13's general mandate doesn't cover (standards, regulatory framework, institutional structure, funding)?
17. Are there overlapping or unclear jurisdictions between Bangsamoro and national authority?
18. What specific bill concepts could address the gaps identified?

**Development and Policy Connection:**
19. Which BDP 2023-2028 goals and Mas Matatag na Bangsamoro Agenda (2026-2028) pillars depend on the full exercise of this power?
20. What development outcomes are at risk if the legislative gaps remain unaddressed?

### BOL Provisions
- Enumerate ALL BOL provisions related to this power — not just the obvious ones. Scan all 18 articles.
- Start with Art. V, Sec. 2({letter}) itself, then list every elaborating provision.
- **Verbatim Text** column: copy-paste from the local BOL transcription files. Never paraphrase.
- **Explanation / Implication** column: plain language explanation of what this provision means in practice. What does it authorize? What does it limit? What does it create? What does it require Parliament to do? This is where you teach the reader.

### Bangsamoro Legislation (BAAs)
- An enacted Parliament Bill (PB) becomes a BAA. List both numbers together.
- Check every BAA (1-89+) against this power area.
- Include BAAs that partially touch this power (note which sections are relevant).
- Status must reflect amendments: if BAA 70 amends BAA 54's provisions, note both.
- BAA 13 (Administrative Code) touches nearly every power — include the specific Book/Title/Section that assigns the mandate.

### National Laws
- Enumerate ALL national laws pertaining to this power — not just those cited in the BOL.
- **MANDATORY SEARCH**: For each power, run keyword searches against:
  - `legislation/national-laws/INDEX.md` (11,866 RAs) — search by subject keywords, agency names, and related terms
  - `legislation/executive-orders/*/INDEX.md` (2,572 EOs) — search per-year indexes, not just the master index
  - `legislation/national-laws/PD-1083.md` (Code of Muslim Personal Laws) — check for relevance
- **Do not rely on obvious matches alone.** The cooperatives example found 17 laws (13 RAs + 4 EOs) vs. the 5 originally listed — including EO 316 (1996) which devolved CDA functions to ARMM and is a critical precedent.
- Categories to search for: (1) laws explicitly referenced in BOL, (2) laws governing the subject area (codes, charters), (3) laws creating relevant national agencies, (4) MSME/enterprise framework laws, (5) ARMM-era devolution EOs, (6) laws that apply suppletorily, (7) related framework laws.
- Include **historical/superseded laws** when they are referenced in the BOL or provide institutional context (e.g., RA 6938 superseded by RA 9520 but still cited in BOL Art. XII, Sec. 9(k)).

### Jurisprudence
- Search `jurisprudence/` for Supreme Court decisions relevant to this power area.
- Focus on: (1) cases interpreting autonomous region powers, (2) cases on the specific subject matter, (3) cases defining national vs. regional authority boundaries.
- Include ARMM-era jurisprudence that may still apply to BARMM.
- If no relevant jurisprudence exists, state "No directly relevant Supreme Court decisions identified" rather than omitting the section.

### Parliament Bills (Pending)
- List filed PBs that have NOT been enacted — these show legislative intent.
- Search `legislation/bills/enacted/INDEX.md` and `legislation/bills/proposed/INDEX.md` by keyword.
- This section comes BEFORE Legislative Gaps so the reader sees what's pending before learning what's still missing.

### Legislative Gaps and Recommended Legislation
- This is the most actionable section — it tells legislators exactly what laws to pass.
- For each gap, name a **specific proposed law** (e.g., "Bangsamoro Cooperative Code", "Bangsamoro Tourism Act") and describe what it would cover.
- **What It Would Cover** column should be specific: regulatory standards, institutional framework, funding mechanisms, licensing/registration systems, penalties, coordination mechanisms, etc.
- **BOL Basis** column must cite the provision that authorizes or mandates the legislation — especially unfulfilled "The Parliament shall enact..." mandates.
- Consider what already exists (BAA 13 mandate, pending PBs, suppletory national law) and what the proposed law adds beyond those.
- If a pending PB already addresses the gap, note it but explain what additional legislation may still be needed.

### Footnotes
- Use Feliciano 10th Edition citation format throughout.
- Every provision cited must have a footnote with full citation.
- Format: `Rep. Act No. 11054, sec. 2(a), art. V.` / `BAA No. 13, sec. 5, bk. IV.`
