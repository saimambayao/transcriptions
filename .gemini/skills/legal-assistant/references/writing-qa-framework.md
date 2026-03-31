# Writing QA Framework

Quality assurance rules that apply DURING legal document production — not after. Every answer must cite its evidence at the moment it's written.

## The Core Rule: Local Source or Verified Online Source — NEVER Training Data

Every legal claim must come from:
1. **Local source file** (BOL transcription, BAA file, RA file, Constitution file) — READ the file, cite the path and line
2. **Verified online source** (lawphil.net, officialgazette.gov.ph, SC E-Library) — cite the URL
3. **[UNVERIFIED]** — if neither local nor online source confirms the claim

**NEVER from training data.** Training data is what produces hallucinations — fabricated BAA numbers, fiqh terms presented as enacted law, wrong article numbers. If you "know" something but can't point to a local file or verified URL, it's training data and it's unreliable.

The reader should never have to ask "where did this come from?"

### Three Evidence Tiers in Every Answer

| Tier | What It Is | How to Present | Example |
|------|-----------|---------------|---------|
| **Enacted law** | BOL, BAA, RA, EO, PD, Constitution — verbatim or near-verbatim | ***Bold italic*** with Article/Section citation | ***"through the enactment of a Bangsamoro cooperative code"*** (Art. XIII, Sec. 24) |
| **Jurisprudence / doctrine** | SC decisions, established legal tests | **Bold** with case name or doctrine name | The **equal protection test** from *People v. Cayat* (1939) requires... |
| **Scholarship / analysis** | Islamic jurisprudence (fiqh), academic frameworks, guidebook concepts, the writer's own analysis | Regular text, explicitly labeled as analytical | This principle is from Islamic jurisprudence (*fiqh*) — it is not codified in BARMM law but provides an analytical framework for... |

### The Critical Distinction

**WRONG** (presents fiqh as if it has legal force):
> ***'Adl*** (justice/equity) — the foundational Shari'ah principle governing the justice system.

**RIGHT** (distinguishes enacted law from scholarship):
> ***'Adl*** (justice/equity) — an Islamic jurisprudential principle meaning fairness and balance. The BOL does not use this Arabic term, but the concept is reflected in Art. X, Sec. 1: ***"Justice shall be dispensed in the Bangsamoro Autonomous Region in consonance with the Constitution."*** A Bangsamoro justice framework could codify *'adl* as a guiding principle — but as of today, it is a *fiqh* concept, not an enacted standard.

## Rules for Each Theme

### Theme A (BOL Grant) — EXTRACTED only
Every claim must cite a specific BOL Article and Section. If the claim is about what the BOL "implies," label it explicitly as an inference.

### Theme B (Shari'ah) — MIXED, must distinguish
- **What the BOL says about Shari'ah**: EXTRACTED (Art. X, PD 1083 — cite section)
- **Arabic legal terms and principles**: Label as ***fiqh*** (Islamic jurisprudence) — not enacted BARMM law
- **How Shari'ah compliance should be integrated**: Writer's ANALYSIS — label as recommendation
- **Never present fiqh concepts as if they have the same authority as BOL provisions**

### Theme C (Constitutional) — EXTRACTED + DOCTRINE
- **Constitutional text**: EXTRACTED (cite Article and Section)
- **Constitutional doctrines**: Cite the SC case establishing the doctrine
- **"Constitutional floor" concept**: Label as analytical framework from the Legal Research Guidebook Ch. 4 — not a term in enacted law

### Theme D (National Law) — EXTRACTED
Every national law claim must cite a specific RA/EO number. "Suppletory application" is a doctrinal concept — label it as such when first used.

### Theme E (Implementation) — EXTRACTED from BAA 13
- BAA 13 mandates and functions: MUST be read from the actual file, not from memory
- Implementation status claims ("CSEA has begun processing registrations"): Label source — is this from an official report, from BAA 85 budget data, or INFERRED?
- "What the ministry can/cannot do": Distinguish between what BAA 13 authorizes (EXTRACTED) and what the writer believes requires standalone legislation (ANALYSIS)

### Theme E.1.A (Institutional Validation) — EXTRACTED + ANALYSIS
- Existing institutions: EXTRACTED from BAA 13, BAA 85, specific BAAs
- Whether the lead MOA is "correct": ANALYSIS — state the reasoning
- New institutions needed: RECOMMENDATION — label as such

### Theme F (Divergence) — ANALYSIS
This is inherently analytical. Label it as such. Cross-reference the enacted law provisions from Themes A, C, D that the analysis is based on.

### Theme I (Power-Specific) — MIXED
Tag each answer: is it from enacted law, from jurisprudence, from fiqh, or from the writer's analysis?

## Inline Evidence Format for Q&A

When writing an answer, lead with the source:

**Pattern 1 — Answer from enacted law:**
> A. Art. XIII, Sec. 24 states: ***"It shall adopt and implement cooperative development policies and programs through the enactment of a Bangsamoro cooperative code."*** This provision...

**Pattern 2 — Answer from doctrine:**
> A. Under the equal protection test established by the Supreme Court in *People v. Cayat* (G.R. No. 45987, 1939), a classification is valid if...

**Pattern 3 — Answer from analysis/fiqh:**
> A. *Mudarabah* (trust financing/profit-sharing) is an Islamic jurisprudential concept — not codified in BARMM law — that could serve as the basis for Shari'ah-compliant cooperative lending. Under *mudarabah*, the cooperative would act as...

**Pattern 4 — Mixed:**
> A. BOL Art. X, Sec. 20 mandates ***"an alternative dispute resolution mechanism"*** for the Bangsamoro. In Islamic jurisprudence, this function is served by ***sulh*** (mediation/settlement) — a concept from *fiqh* that is not named in the BOL but maps to the Art. X Sec. 20 mandate. PD 1083 addresses arbitration of Muslim disputes (Art. 155-168) but does not use the term *sulh*.

## Quality Gates During Writing

Before completing ANY Q&A pair:

1. **Evidence gate**: Does the answer cite a specific provision for every legal claim?
2. **Source tier gate**: Is enacted law distinguished from doctrine and scholarship?
3. **Shari'ah gate**: Are Arabic terms labeled as fiqh (not presented as enacted law)?
4. **Inference gate**: Are analytical conclusions ("BARMM can diverge") labeled as analysis with reasoning?
5. **BAA 13 gate**: Were functions quoted from the actual file, not summarized?
6. **Em dash gate**: Uses `—` not `---`?

## What to Do When You Don't Know the Source

- **If you think it's from the BOL but can't find the section**: Write `[UNVERIFIED: believed to be in BOL Art. X but section not confirmed — verify before publication]`
- **If it's general knowledge about Islamic law**: Write "In Islamic jurisprudence (*fiqh*)..." — never present it as enacted BARMM law
- **If it's about what a ministry does in practice**: Write `[UNVERIFIED: operational status not confirmed from official source]`
- **Never fabricate a citation.** A blank is better than a wrong citation. A wrong BAA number or BOL article is 3x worse than `[UNVERIFIED]`.
