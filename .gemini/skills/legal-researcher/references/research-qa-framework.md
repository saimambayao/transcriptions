# Research QA Framework

Quality assurance rules that apply DURING legal research — not after. Every finding must be sourced at the moment it's recorded.

## The Absolute Rule: LOCAL SOURCE or VERIFIED ONLINE SOURCE — NEVER TRAINING DATA

Training data is the #1 source of hallucination. It produces fabricated BAA numbers, wrong article citations, fiqh terms presented as enacted law, and "facts" that sound authoritative but have no basis in any enacted legislation.

**The hierarchy:**
1. **Local source file** — read it, cite file path + line number. This is the gold standard.
2. **Verified online source** — lawphil.net, officialgazette.gov.ph, SC E-Library. Cite the URL.
3. **[UNVERIFIED]** — if neither local nor online confirms the claim. Mark it and move on.
4. **Training data** — NEVER for legal claims. If you "know" something but can't point to a file or URL, it's training data and it's unreliable. Do not use it.

## The Tagging Rule: EXTRACTED vs INFERRED

Every factual claim in a Research Memorandum must be tagged:

- **EXTRACTED** — directly stated in an enacted law, with source file path and line number
  - Example: `Art. V, Sec. 2(k) — "Cooperatives and social entrepreneurship" [EXTRACTED: bol-ra-11054/01-articles-I-to-V.md:156]`
- **INFERRED** — reasoned from a provision or derived from doctrine/scholarship, with reasoning chain
  - Example: `Mudarabah-based cooperative financing is relevant [INFERRED: Islamic jurisprudence (fiqh); BOL Art. X Sec. 4 authorizes commercial Shari'ah but doesn't name mudarabah; no enacted BARMM law codifies this term]`

### Why This Matters

The cooperatives example found that CSEA was described as "cannot register cooperatives" — wrong, because BAA 13 Sec. 57 says the opposite. This happened because the claim was INFERRED from assumption, not EXTRACTED from the source. Tagging forces the researcher to READ the source before claiming.

## Source Hierarchy for Tagging

| Tag | Source Type | Authority Level | Example |
|-----|-----------|----------------|---------|
| **EXTRACTED: enacted law** | BOL, BAA, RA, EO, PD, Constitution | Highest — verbatim from enacted legislation | Art. XIII, Sec. 24: "through the enactment of a Bangsamoro cooperative code" |
| **EXTRACTED: official document** | BAA 85 budget tables, Parliament records, official gazette | High — from government publications | BAA 85, Ch. XXVI allocates PhP X to CSEA |
| **INFERRED: from enacted law** | Logical implication of a provision | Medium — the provision exists, the inference is the researcher's | Art. V, Sec. 2(k) implies BARMM can register cooperatives (inferring from enumerated power) |
| **INFERRED: from doctrine** | Philippine legal doctrine, SC rulings | Medium — established but not in BARMM-specific law | Equal protection test from *People v. Cayat* applies to BARMM legislation |
| **INFERRED: from scholarship** | Islamic jurisprudence (fiqh), academic literature, guidebooks | Low — not enacted law; may inform legislation but has no legal force | *Mudarabah* is a valid cooperative financing model in Islamic finance theory |
| **UNVERIFIED** | Cannot be traced to any source | Lowest — flag and do not present as fact | [UNVERIFIED: could not confirm whether CDA has a regional office in BARMM]

## Rules for Shari'ah Content

Shari'ah content is the highest-risk area for presenting scholarship as enacted law. Apply these rules:

1. **BOL Art. X provisions** — EXTRACTED. These are enacted law. Quote verbatim.
2. **PD 1083 provisions** — EXTRACTED. This is enacted law. Quote with section numbers.
3. **Arabic legal terms** (*mudarabah*, *sulh*, *ta'zir*, *'adl*, *shura*) — **INFERRED from fiqh** unless a specific BARMM law uses the term. The BOL does NOT use most Arabic legal terms. PD 1083 uses some.
4. **Maqasid al-Shari'ah** (objectives of Shari'ah) — INFERRED from Islamic legal philosophy. Not codified in BARMM law.
5. **Shari'ah court jurisdiction** — EXTRACTED from BOL Art. X, Sec. 5-9 (specific jurisdictional boundaries are enacted law).

**The key distinction:** "The BOL authorizes Shari'ah-based commercial legislation" is EXTRACTED (Art. X, Sec. 4). "Mudarabah is a relevant Shari'ah-compliant cooperative model" is INFERRED (fiqh concept, not in any enacted BARMM law).

## Rules for Constitutional Content

1. **Constitutional text** — EXTRACTED from the 1987 Constitution. Always cite Article and Section.
2. **Constitutional doctrines** (equal protection test, due process requirements) — INFERRED from jurisprudence (*People v. Cayat*, *Ang Tibay v. CIR*). These are established but not in the Constitution's text.
3. **"Constitutional floor" concept** — INFERRED. This analytical framework was developed in the legal references project. It's useful but not a term in enacted law.

## Rules for National Law Content

1. **RA/EO provisions** — EXTRACTED. Cite the specific section.
2. **"Suppletory application"** — INFERRED from legal doctrine. The concept that national law fills gaps where no BAA exists is reasoned, not stated in any single provision.
3. **Whether a national law applies in BARMM** — requires analysis (INFERRED) unless the BOL specifically names the law.

## Inline Sourcing Format

When recording findings in the Research Memorandum, use this format:

```
| Finding | Source | Tag | File:Line |
|---------|--------|-----|-----------|
| BARMM has authority over cooperatives | Art. V, Sec. 2(k) | EXTRACTED | bol/01-articles-I-to-V.md:156 |
| Cooperative code is mandated | Art. XIII, Sec. 24 | EXTRACTED | bol/04-articles-XIII-to-XV.md:174 |
| Mudarabah is relevant to cooperatives | Islamic jurisprudence (fiqh) | INFERRED | No enacted BARMM law uses this term |
| CSEA can register cooperatives | BAA 13, Sec. 57 | EXTRACTED | baas/BAA-13.md:1443 |
```

## Quality Gates During Research

Before finalizing ANY section of the Research Memorandum:

1. **Source check**: Does every EXTRACTED claim have a file:line reference?
2. **Inference check**: Is every INFERRED claim clearly labeled with the reasoning chain?
3. **Shari'ah check**: Are Arabic legal terms tagged as fiqh (not presented as enacted law)?
4. **Constitutional check**: Are doctrinal tests (equal protection, due process) tagged as jurisprudence?
5. **National law check**: Were INDEX files actually scanned (record search terms)?
6. **BAA 13 check**: Were the actual BAA 13 sections read (not summarized from memory)?

## What Happens If a Finding Can't Be Sourced

- **If it's a legal claim** (e.g., "BARMM can diverge"): Mark as [INFERRED] with reasoning. The /legal-assistant must present it as analysis, not as law.
- **If it's a factual claim** (e.g., "CDA has 73,000 registered cooperatives"): Mark as [UNVERIFIED] unless you can cite a specific source.
- **If it's a Shari'ah concept**: Mark as [INFERRED: Islamic jurisprudence] and note that it requires enactment to have legal force in BARMM.
- **Never present unsourced claims as EXTRACTED.** A wrong citation is 3x worse than [UNVERIFIED].
