---
name: shariah
description: |
  Shari'ah legal research, court jurisdictional analysis, and Islamic law checkpoint for BARMM
  legislation and development work. Covers: BOL Art. X (Secs. 1-20) provisions, PD 1083
  (Code of Muslim Personal Laws), Shari'ah court jurisdiction (Circuit, District, High Court),
  Islamic finance instruments (mudarabah, musharakah, murabaha, waqf, zakat), and Shari'ah
  compliance review for BAA drafts and cooperative bylaws.
  Trigger on: "Shari'ah", "shariah", "sharia", "Islamic law", "Muslim personal law",
  "PD 1083", "Shari'ah court", "Circuit Court jurisdiction", "District Court jurisdiction",
  "Shari'ah High Court", "fiqh", "Islamic finance", "mudarabah", "musharakah", "murabaha",
  "waqf", "zakat", "halal", "ta'zir", "mahr", "dower", "Muslim marriage", "Muslim divorce",
  "Muslim inheritance", "Bangsamoro Darul-Ifta", "fatwa", "Shari'ah checkpoint",
  "Shari'ah compliance", "Shari'ah-compliant", "Islamic governance", "Maqasid al-Shari'ah",
  "does this have a Shari'ah dimension", "check for Shari'ah implications",
  or any question about Islamic law applicability in BARMM governance, legislation, or development.
  IMPORTANT: This skill assists with the LEGAL RESEARCH dimension of Shari'ah — locating
  enacted provisions, mapping court jurisdiction, and flagging questions that need fiqh expertise.
  It does NOT interpret Shari'ah. Interpretation requires qualified Islamic legal scholars
  and the Bangsamoro Darul-Ifta (BDI).
allowed-tools:
  - Read
  - Glob
  - Grep
  - WebSearch
  - WebFetch
argument-hint: "[Shari'ah question, provision lookup, jurisdiction check, or compliance review]"
---

# Shari'ah — Islamic Law Research and Checkpoint

Assists with the legal research dimension of Shari'ah in BARMM — locating enacted provisions, mapping court jurisdiction, checking legislative Shari'ah compliance, and researching Islamic finance frameworks. Does NOT interpret Shari'ah.

## The Fundamental Boundary

**AI cannot interpret Shari'ah.** This boundary is absolute and applies to every mode of this skill.

The Qur'an and Sunnah are the principal sources of Shari'ah (BOL Art. X, Sec. 3). Interpreting them requires *fiqh* — Islamic jurisprudential expertise developed through years of scholarly training. No AI tool possesses this expertise. When a question requires Shari'ah interpretation, this skill's job is to:

1. Identify that interpretation is needed
2. Document the specific question
3. Recommend referral to the **Bangsamoro Darul-Ifta (BDI)** — the region's Islamic religious authority for juristic opinions (*fatawa*)
4. Provide the enacted legal provisions (BOL, PD 1083) that frame the question

What this skill CAN do is search enacted law. BOL Art. X (20 sections), PD 1083 (190 articles), and enacted BAAs are law — they can be read, cited, and analyzed using the same legal research methodology as any other tier of the BARMM legal hierarchy.

## Sources

### Tier 1: Enacted Law (EXTRACTED — verbatim from source)

| Source | Path | What It Contains |
|--------|------|-----------------|
| **BOL Art. X** (Secs. 1-20) | `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` (chapter files 3-4) | Justice system, Shari'ah courts, sources of law, court jurisdiction, traditional justice, ADR |
| **PD 1083** | `~/apps/transcriptions/legislation/national-laws/PD-1083.md` (82K, 190 articles) | Code of Muslim Personal Laws — marriage, divorce, inheritance, family relations, property |
| **BAA 13** | `~/apps/transcriptions/legislation/BAAs/BAA-13.md` | Bangsamoro Darul-Ifta establishment, institutional framework |
| **Enacted BAAs** | `~/apps/transcriptions/legislation/BAAs/` | Any BAA with Shari'ah provisions |
| **Constitution** | Art. X, Sec. 15-21 | Autonomous region powers including justice system |

### Tier 2: Research Framework (INFERRED — Gemini deep-research, needs verification)

| Source | Path | Status |
|--------|------|--------|
| **BARMM Shari'ah Legislation Framework** | `~/apps/transcriptions/source-pdfs/other/BARMM Shari'ah Legislation Framework.pdf` | Gemini deep-research output (29 pages). Treat ALL claims as INFERRED. Verify every BOL/PD 1083 citation against Tier 1 sources before using. Useful for structure and framework concepts, NOT as a source of legal authority. |

**Rule:** When the Gemini framework and the enacted law disagree, the enacted law wins. Always.

## Modes

### Mode 1: Shari'ah Checkpoint

**Invoke with:** Any question from another skill — "Does this have a Shari'ah dimension?"

This is the lightweight mode. It answers one question: does the research topic, bill, or policy have a Shari'ah dimension that requires deeper investigation?

**A Shari'ah dimension exists when:**
- The subject involves personal law (marriage, divorce, inheritance, custody) for Muslims
- The subject involves property relations between Muslims
- The subject involves minor criminal offenses under Shari'ah court jurisdiction (*ta'zir*)
- The subject intersects with Islamic finance, halal certification, waqf (endowment), or zakat (alms)
- A found provision references "Shari'ah," "Islamic law," or "Muslim personal law"
- The subject involves Madaris education or Islamic educational institutions
- The subject involves the Bangsamoro Darul-Ifta or religious authorities

**Output:** One of:
- **"Shari'ah dimension: None identified"** — with brief explanation
- **"Shari'ah dimension: YES"** — with specific BOL/PD 1083 provisions triggered, and recommendation for which mode to use next

**Worked Example:**

> **Input:** "Does the Cooperative Development Guidebook need Shari'ah review?"
>
> **Checkpoint:** Shari'ah dimension: **YES**
> - BOL Art. X, Sec. 4 authorizes Parliament to legislate on commercial matters including Shari'ah-compliant financing
> - Cooperative bylaws may require Shari'ah-compliant investment provisions (mudarabah, musharakah) — these are fiqh concepts, not yet codified by BAA
> - Chapter 7 (Islamic Finance Instruments for Cooperatives) directly addresses Shari'ah-compliant capital structures
> - **Recommend:** Mode 5 (Islamic Finance Research) for the legal framework; Mode 4 (Compliance Review) for any draft bylaws

> **Input:** "Does BAA 84 (Budget System Act) have a Shari'ah dimension?"
>
> **Checkpoint:** Shari'ah dimension: **None identified**
> - BAA 84 governs the Bangsamoro budget system — appropriations, fund management, fiscal procedures
> - No provisions reference Shari'ah, Islamic law, or Muslim personal law
> - Zakat (obligatory alms) is a potential intersection but BAA 84 does not address it — zakat legislation would be a separate BAA under Art. X, Sec. 4

### Mode 2: Jurisdictional Analysis

**Invoke with:** "Which Shari'ah court has jurisdiction?" or jurisdiction questions

Determines which Shari'ah court (Circuit, District, or High Court) has authority over a specific case or subject matter. Uses the jurisdictional matrix from BOL Art. X, Secs. 5-7.

**The Three-Tiered Court System:**

| Court | BOL Provision | Exclusive Original Jurisdiction | Appellate | Special Powers |
|-------|-------------|-------------------------------|-----------|---------------|
| **Shari'ah Circuit Court** | Art. X, Sec. 5 | PD 1083 offenses; marriage/divorce/dower/property; communal property disputes; *ta'zir* (arresto menor); civil actions (real ≤ P400K, other ≤ P200K) | None | None |
| **Shari'ah District Court** | Art. X, Sec. 6 | Custody/guardianship/legitimacy; estate settlement; Muslim Registry corrections; customary/Shari'ah contracts; civil actions (real > P400K, other > P200K) | All Circuit Court cases | Mandamus, prohibition, injunction, certiorari, habeas corpus |
| **Shari'ah High Court** | Art. X, Sec. 7 | Annulment of District Court judgments; auxiliary writs | All District Court cases | Mandamus, prohibition, injunction, certiorari, habeas corpus |

**Appellate pathway:** Circuit Court → District Court → High Court → Supreme Court (questions of law only)

**Critical limitation:** Shari'ah applies "exclusively to cases involving Muslims" (Art. X, Sec. 1). Non-Muslims may voluntarily submit. Confirm Muslim identity of parties before proceeding.

**Pending:** Verify operational status of the Shari'ah High Court — the BOL provides that until fully organized, District Court decisions are appealable to the Court of Appeals.

**Output Template:**

```markdown
## Jurisdictional Determination

**Question:** [the jurisdictional question]
**Parties:** [Muslim / Non-Muslim / Mixed — if mixed, voluntary submission confirmed?]
**Subject Matter:** [category — personal law, property, criminal, commercial, estate]

### Determination

| Field | Value |
|-------|-------|
| **Court** | [Shari'ah Circuit Court / District Court / High Court] |
| **BOL Provision** | [Art. X, Sec. 5/6/7] |
| **Basis** | [which jurisdictional category and monetary threshold if applicable] |
| **Appellate Path** | [next court in the chain] |

### Reasoning
[2-3 sentences explaining why this court, not the others]

### Caveats
[Any uncertainties — e.g., High Court operational status, borderline monetary threshold]
```

**Worked Example:**

> **Input:** "A Muslim couple in Cotabato City is divorcing. The wife claims mahr (dower) of P150,000 and wants custody of their two children. Which court?"
>
> **Parties:** Both Muslim — Shari'ah jurisdiction applies (Art. X, Sec. 1)
>
> **Determination:**
> - **Divorce and mahr (P150,000):** Shari'ah Circuit Court — Art. X, Sec. 5 (marriage, divorce, dower, property upon divorce; civil claim ≤ P200,000)
> - **Custody of children:** Shari'ah District Court — Art. X, Sec. 6 (custody, guardianship, legitimacy under PD 1083)
>
> **Result:** Two courts are involved. The divorce and mahr go to Circuit Court. Custody goes to District Court. The District Court also has appellate jurisdiction over the Circuit Court's decision on divorce/mahr.
>
> **Caveat:** Verify whether the cases can be consolidated at the District Court level for judicial economy — the BOL does not explicitly address consolidation of related Shari'ah cases across court levels.

### Mode 3: Shari'ah Legal Research

**Invoke with:** Research questions about Islamic law provisions in BARMM

Full legal research on Shari'ah topics using the same 5-step methodology as `/legal-researcher`, but with Shari'ah-specific sources and verification requirements.

**Process:**
1. **Issue Analysis** — frame the question; confirm it involves Muslims or Shari'ah subject matter
2. **Landscape Review** — understand the Shari'ah dimension; consult BOL Art. X, PD 1083
3. **Systematic Search** — search enacted Shari'ah sources:
   - BOL Art. X, Secs. 1-20 (read ALL 20 sections, not just keyword matches)
   - PD 1083 (search by Book/Title/Chapter for the relevant subject)
   - BAAs with Shari'ah provisions
   - Bills with explicit Shari'ah integration (search `legislation/bills/`)
4. **Provision Chain Trace** — follow Shari'ah references across sources
5. **Verification** — verify every provision against source text

**Additional Shari'ah-specific steps:**
- Identify whether Parliament has legislated on the subject (BOL Art. X, Sec. 4 grants power to legislate on matters "not provided for" under PD 1083)
- If PD 1083 covers the subject, it remains governing law — Parliament's power is supplementary
- Flag questions that require fiqh expertise and recommend BDI referral

**Output:** Research Memorandum with a Shari'ah Sources section:

| Source | Provision | Type | Application |
|--------|-----------|------|-------------|
| BOL Art. X, Sec. 5 | Circuit Court jurisdiction | EXTRACTED | Defines court authority |
| PD 1083, Art. 13 | Marriage requirements | EXTRACTED | Governs Muslim marriage |
| Maqasid al-Shari'ah | Protection of faith | INFERRED: fiqh | Framework concept — not enacted law |

### Mode 4: Shari'ah Compliance Review

**Invoke with:** "Check this BAA/bill for Shari'ah compliance" or compliance questions

Reviews a draft BAA, bill, cooperative bylaw, or policy document for Shari'ah implications. Does NOT determine whether the document IS Shari'ah-compliant (that requires fiqh expertise) — it identifies provisions that HAVE Shari'ah implications and flags them for expert review.

**What this mode does:**
1. Scans the document for terms and subjects with Shari'ah dimensions
2. Maps each flagged provision to the relevant BOL Art. X section or PD 1083 article
3. Identifies whether the provision falls within Shari'ah court jurisdiction
4. Flags provisions that require BDI review
5. Checks whether the document respects the "exclusively Muslim" boundary (Art. X, Sec. 1)

**What this mode does NOT do:**
- Determine whether a provision is consistent with the Qur'an or Sunnah
- Interpret Ijma (scholarly consensus) or Qiyas (analogical reasoning)
- Issue opinions on whether Islamic principles are correctly applied
- Replace the proposed Shari'ah Legislative Review Board (SLRB) function

**Output Template:**

```markdown
## Shari'ah Compliance Flags

**Document reviewed:** [title, type — BAA draft / bill / bylaw / policy]
**Date:** [date]

### Flagged Provisions

| # | Section/Provision | Shari'ah Dimension | BOL/PD 1083 Reference | Action Required |
|---|-------------------|-------------------|----------------------|-----------------|
| 1 | [section number] | [what Shari'ah subject it touches] | [enacted provision] | [BDI review / jurisdiction check / fiqh consultation] |

### Muslim Exclusivity Check
[Does the document apply Shari'ah to non-Muslims without voluntary submission? If yes, flag as constitutional violation of Art. X, Sec. 1]

### Provisions Requiring BDI Review
[List provisions where Shari'ah interpretation — not just legal research — is needed]

### Provisions Clear Under Enacted Law
[List provisions that can be resolved by reading BOL Art. X or PD 1083 — no interpretation needed]
```

### Mode 5: Islamic Finance Research

**Invoke with:** Questions about Islamic finance instruments, Shari'ah-compliant financing, cooperative finance

Researches the legal framework for Islamic finance in BARMM — for cooperatives, social enterprises, and government financial instruments.

**Key instruments:**

| Instrument | Arabic | Description | BOL/Legal Basis |
|-----------|--------|-------------|----------------|
| **Mudarabah** | مضاربة | Profit-sharing partnership — one party provides capital, other provides labor | BOL Art. X, Sec. 4 (Parliament can legislate); no enacted BAA yet |
| **Musharakah** | مشاركة | Joint venture — all parties contribute capital and share profit/loss | Same as above |
| **Murabaha** | مرابحة | Cost-plus financing — seller discloses cost and adds agreed markup | Same as above |
| **Waqf** | وقف | Islamic endowment — property held in trust for charitable purposes | BOL Art. X, Sec. 4; PD 1083 provisions |
| **Zakat** | زكاة | Obligatory alms — one of the Five Pillars of Islam | BOL Art. X, Sec. 4 |
| **Tabarru'** | تبرع | Charitable donation — used in Islamic social finance | Referenced in PB 379 |

**CRITICAL:** These instruments are fiqh concepts. No BARMM BAA has codified any of them. When writing about Islamic finance, label each instrument as:
- **EXTRACTED** if citing a BOL/PD 1083 provision that names it
- **INFERRED: fiqh** if describing the instrument's characteristics from Islamic finance scholarship
- **INFERRED: pending legislation** if referencing a filed but unenacted bill

**For cooperative development:** Cross-reference with RA 9520 (Philippine Cooperative Code) and the Cooperative Development Guidebook. Shari'ah-compliant cooperative bylaws must satisfy both RA 9520 requirements AND Islamic finance principles — but the Islamic finance principles are not yet codified in BARMM law.

## Constitutional Checkpoint (Cross-Cutting — Applies to All Modes)

Every Shari'ah research output must pass through a constitutional checkpoint. Shari'ah legislation in BARMM operates within the Philippine constitutional framework — this is the "nested sovereignty" principle. The BOL itself states that BARMM is "an integral, indivisible, and inseparable part of the territory of the Republic of the Philippines."

**Three constitutional constraints on Shari'ah legislation:**

### 1. Bill of Rights (Art. III)

All BARMM legislation — including Shari'ah-based BAAs — must comply with the Bill of Rights. Key provisions:

| Right | Application to Shari'ah Legislation |
|-------|-------------------------------------|
| **Due process** (Sec. 1) | *Ta'zir* penalties must satisfy procedural due process (*Ang Tibay v. CIR* requirements). A BAA imposing penalties must provide notice, hearing, and proportionality. |
| **Equal protection** (Sec. 1) | Shari'ah provisions that treat Muslims differently from non-Muslims are constitutionally permissible BECAUSE the BOL explicitly authorizes them AND the "exclusively Muslim" boundary (Art. X, Sec. 1) ensures non-Muslims are not subjected without consent. |
| **Freedom of religion** (Sec. 5) | Shari'ah applies exclusively to cases involving Muslims — but a non-Muslim may voluntarily submit to Shari'ah court jurisdiction (Art. X, Sec. 1). The constitutional requirement is that submission be genuinely voluntary, not coerced. |
| **Right against unreasonable searches** (Sec. 2) | Shari'ah enforcement mechanisms (e.g., halal compliance inspection) must satisfy constitutional search and seizure standards. |

### 2. Autonomous Region Limits (Art. X, Sec. 15-21)

| Constraint | What It Means |
|-----------|---------------|
| Art. X, Sec. 18 | Autonomous regions created "within the framework of this Constitution" — not outside it |
| Art. X, Sec. 20 | Organic act defines legislative powers "subject to the provisions of this Constitution and national laws" |
| SC supervision | All Shari'ah courts are part of the Philippine judicial system under Supreme Court supervision (BOL Art. X, Sec. 2). SC has final say on questions of law. |

### 3. The "Exclusively Muslim" Boundary as Constitutional Compliance

BOL Art. X, Sec. 1 establishes the scope: Shari'ah applies "exclusively to cases involving Muslims" — with the important provision that "where a case involves a non-Muslim, Shari'ah law may apply only if the non-Muslim voluntarily submits to the jurisdiction of the Shari'ah court." This voluntary submission mechanism is itself the constitutional safeguard — it preserves religious freedom while allowing non-Muslims to choose Shari'ah jurisdiction when they wish. If a BAA removes the voluntariness of that submission, it risks unconstitutionality.

**How to apply this checkpoint:**

After completing any mode (1-5), ask:
1. Does this output involve legislation that imposes obligations or penalties? → Check due process
2. Does this output apply Shari'ah to non-Muslims? → Confirm voluntary submission (Art. X, Sec. 1) — not coerced, not presumed
3. Does this output affect the jurisdiction of Shari'ah courts? → Confirm SC supervisory authority is preserved
4. Does this output affect non-Muslim rights? → Confirm Art. III protections are not diminished

If any constitutional issue is identified, flag it in the output with: **"Constitutional consideration: [specific issue]. See Legal Research Guidebook, Chapter 4 (Constitutional Analysis) for the full framework."**

**Cross-reference:** The Legal Research Guidebook's Chapter 4 provides the complete constitutional analysis framework — constitutional floor, equal protection test (*People v. Cayat*), due process (*Ang Tibay v. CIR*), and unconstitutionality risk assessment. Use that framework for deep constitutional analysis; this checkpoint is the quick gate.

## Complexity Scaling

| Complexity | Mode(s) | Time | When to Use |
|-----------|---------|------|-------------|
| **Simple** | Mode 1 (Checkpoint) | < 1 min | Quick gate — "does this topic have a Shari'ah dimension?" Called by /legal-researcher at Step 3. |
| **Focused** | Mode 2 (Jurisdiction) | 5-10 min | Specific court jurisdiction question. Identify parties, subject, monetary value → determine court. |
| **Medium** | Mode 4 (Compliance) or Mode 5 (Islamic Finance) | 15-30 min | Review a specific document for Shari'ah flags, or research the legal framework for one Islamic finance instrument. |
| **Complex** | Mode 3 (Full Research) + Mode 5 | 30-60 min | Comprehensive Shari'ah legal research — read all 20 BOL Art. X sections, search PD 1083, trace provision chains, identify legislative gaps. |
| **Requires BDI** | Any mode → escalation | N/A | When the question requires interpretation of Qur'an, Sunnah, Ijma, or Qiyas. Document the question and the enacted provisions that frame it, then refer to the Bangsamoro Darul-Ifta. |

## Gotchas

- **"Shari'ah Appellate Court"** — WRONG. The correct name is **Shari'ah High Court** (BOL Art. X, Sec. 7). This is the #1 nomenclature error.
- **Presenting fiqh as enacted law** — Arabic terms (mudarabah, sulh, ta'zir as a concept beyond arresto menor) are fiqh concepts. The BOL authorizes them but does NOT codify most of them. Only cite as enacted law what is actually in the BOL or PD 1083 text.
- **Ignoring the "exclusively Muslim" boundary** — Shari'ah applies only to cases involving Muslims (Art. X, Sec. 1). Non-Muslims must voluntarily submit. This is a hard constitutional limit.
- **Confusing PD 1083 subjects with Parliament's legislative power** — Parliament can legislate on matters "not provided for" under PD 1083. If PD 1083 already covers it, PD 1083 governs. Parliament's power is supplementary, not overriding.
- **The Gemini framework PDF is NOT an authoritative source** — it's an AI-generated research output that needs verification. Treat every claim in it as INFERRED. Verify against BOL and PD 1083 before citing.
- **Maqasid al-Shari'ah is a scholarly framework, not enacted law** — The five objectives (faith, life, intellect, lineage, property) are from Islamic jurisprudence. They inform legislation but have no legal force until enacted by Parliament.

## Skill Composition

**This skill is called by:**
- `/legal-researcher` — when the Shari'ah Checkpoint in Step 3 triggers
- `/bill-drafter` — when drafting legislation with Shari'ah implications
- `/legal-assistant` — when producing legal analysis with Shari'ah dimensions
- `/legal-reviewer` — when reviewing documents for Shari'ah compliance

**This skill calls:**
- `/bangsamoro` — for governance context, institutional relationships
- `/legal-researcher` — for provision chain tracing across the 7-tier hierarchy

## Subagent Honesty Rules

Every subagent prompt dispatched by this skill MUST include:

> HONESTY RULES:
> 1. Only extract values explicitly stated in BOL Art. X, PD 1083, or enacted BAAs. If a claim comes from fiqh scholarship (not enacted law), tag it as INFERRED: fiqh.
> 2. A wrong Shari'ah citation is 3x worse than a blank answer. When in doubt, leave it blank.
> 3. Tag every claim as EXTRACTED (from enacted law with source), INFERRED: fiqh (from Islamic jurisprudence), or INFERRED: pending legislation (from filed but unenacted bills).
> 4. NEVER present fiqh concepts as enacted BARMM law. The BOL authorizes Shari'ah legislation but most Arabic legal terms have NOT been codified by any BAA.

## Error Handling

| Situation | Action |
|-----------|--------|
| Question requires Shari'ah interpretation | Flag for BDI referral. Document the specific question. Provide the enacted provisions that frame it. |
| PD 1083 and BOL Art. X appear to conflict | PD 1083 continues for subjects it covers. BOL Art. X, Sec. 4 grants Parliament power to legislate on matters "not provided for" by PD 1083. If the conflict is genuine, note both provisions and flag for legal analysis by /legal-assistant. |
| Non-Muslim parties involved | Shari'ah does not apply unless the non-Muslim voluntarily submits (Art. X, Sec. 1). Note this boundary in the output. |
| No enacted BAA covers the Islamic finance instrument | Label as INFERRED: fiqh. Note that BOL Art. X, Sec. 4 authorizes future legislation but no BAA has been enacted. Search `legislation/bills/` for pending bills. |
| Gemini framework PDF cited as authority | Reject. It is a research output, not enacted law. Verify every claim against Tier 1 sources. |
| Shari'ah High Court operational status unclear | Note the uncertainty. The BOL provides an interim pathway (Court of Appeals) until the High Court is fully organized. |
