---
name: jurisprudence
description: |
  Case analysis, jurisprudential research, litigation strategy, and judicial simulation
  for Philippine litigation and legislation. Eight modes: (1) CASE — neutral analysis of
  a specific factual case, (2) PROSECUTION — build the prosecution's case (charge strategy,
  Information drafting, evidence plan, witness sequence, defense anticipation),
  (3) DEFENSE — build the defense (rights inventory, Information analysis, affirmative
  defenses, reasonable doubt map, impeachment plan, testimony decision),
  (4) DOCTRINE — survey Supreme Court doctrines for legislation or policy,
  (5) JUDGE RTC — simulate a Regional Trial Court decision,
  (6) JUDGE CA — simulate a Court of Appeals decision,
  (7) JUDGE SC — simulate a Supreme Court decision,
  (8) JUDGE SHARIAH — simulate a Shari'ah Court decision.
  Hybrid architecture: own jurisprudence search protocol for the 39,957+ SC decisions
  in the local archive, calls /legal-researcher for statute search and /shariah when
  Muslim personal law (PD 1083) is involved.
  Trigger on: "case analysis", "analyze this case", "defense analysis", "prosecution
  analysis", "what are the elements of", "is this evidence admissible", "admissibility",
  "jurisprudential analysis", "what has the SC said about", "doctrine on", "controlling
  jurisprudence", "case law on", "leading cases on", "verdict assessment", "elements
  mapping", "criminal case", "civil case", "VAWC case", "RA 9262", "defense strategy",
  "prosecution strategy", "build the prosecution's case", "draft an Information",
  "what should the prosecutor charge", "defense strategy", "build the defense",
  "motion to quash", "affirmative defense", "reasonable doubt", "cross-examination",
  "impeachment plan", "case review", "litigation analysis", "breach of contract",
  "damages", "specific performance", "injunction", "ejectment", "forcible entry",
  "civil case", "collection of sum of money", "annulment", "partition",
  "quieting of title", "if you were the judge",
  "simulate a decision", "write a decision", "RTC decision", "court decision",
  "Shari'ah court", "how would the court rule", or any request to analyze a court case,
  build a prosecution or defense strategy, assess evidence admissibility, map statutory
  elements to facts, survey Supreme Court doctrines, or simulate a judicial decision.
  Use this skill even when the user just provides case facts and asks "what do you
  think?" — that is a CASE analysis.
allowed-tools:
  - Read
  - Glob
  - Grep
  - Agent
  - WebSearch
  - WebFetch
argument-hint: "[CASE|PROSECUTION|DEFENSE|DOCTRINE|JUDGE RTC|JUDGE CA|JUDGE SC|JUDGE SHARIAH] [case or concept]"
---

# Jurisprudence — Case Analysis & Doctrinal Research

Analyzes specific court cases against the full legal landscape, surveys Supreme Court doctrines for legislative purposes, or simulates judicial decisions at any court level. Every legal claim is verified against local source files — Constitution, statutes, Rules of Court, and the 39,957+ SC decisions in the jurisprudence archive.

## Mode Selection

| Mode | Input | Output | Use When |
|------|-------|--------|----------|
| **CASE** | Facts, charges, evidence | Issue analysis, elements map, admissibility scan, verdict assessment | Analyzing a specific litigation matter (neutral, both sides) |
| **PROSECUTION** | Complainant's facts, evidence | Charge strategy, Information draft, evidence plan, witness sequence, defense anticipation | Building the prosecution's case |
| **DEFENSE** | Accused's facts, charges faced | Defense strategy, Motion to Quash analysis, cross-examination plan, affirmative defenses, reasonable doubt map | Building the defense |
| **DOCTRINE** | Legal concept or question | Doctrinal survey, evolution timeline, current standard | Researching case law for legislation or policy |
| **JUDGE RTC** | Complete case record | RTC Decision (findings of fact, findings of law, dispositive portion) | Simulating a trial court ruling |
| **JUDGE CA** | RTC decision + appeal brief | CA Decision (errors assigned, review of facts/law, disposition) | Simulating an appellate review |
| **JUDGE SC** | CA decision or petition | SC Decision (constitutional/doctrinal analysis, vote) | Simulating a Supreme Court ruling |
| **JUDGE SHARIAH** | Case involving Muslim personal law | Shari'ah Court Decision (PD 1083, Islamic jurisprudence) | Cases under Muslim personal law jurisdiction |

Default to CASE if the user provides facts about a specific dispute. Default to DOCTRINE if the user asks about a legal concept abstractly. JUDGE modes require the user to specify the court level. PROSECUTION mode when the user is building a case, not analyzing one.

## Complexity Scaling

Adapt the depth of analysis to the case complexity. Not every case needs 3 sweep passes.

| Complexity | Indicators | Approach |
|-----------|-----------|----------|
| **Simple** | 1 charge, 1-2 witnesses, no constitutional/PD 1083 issues, clear applicable law | Abbreviated: skip sweeps, single-pass research, condensed output |
| **Medium** | 1-3 charges, 3-6 witnesses, 1-2 special law issues (RA 9262, RA 10175, etc.) | Full protocol: all 4 phases + 3 sweeps |
| **Complex** | 4+ charges, 7+ witnesses, constitutional + PD 1083 + multiple statutory schemes, doctrinal conflicts | Full protocol + dispatch parallel subagents for separate issue clusters |

## Criminal vs. Civil Gate

At the start of CASE, PROSECUTION, DEFENSE, and JUDGE modes, determine whether the case is **criminal** or **civil**. This affects terminology, rules, standard of proof, and output format.

| Aspect | Criminal | Civil |
|--------|----------|-------|
| Parties | People of the Philippines vs. Accused | Plaintiff vs. Defendant |
| Charging document | Information (Rule 110) | Complaint (Rule 6) |
| Standard of proof | Beyond reasonable doubt (Rule 133, Sec. 2) | Preponderance of evidence (Rule 133, Sec. 1) |
| Applicable Rules | Rules 110-127 (Criminal Procedure) | Rules 1-71 (Civil Procedure) |
| Testimony | Judicial Affidavit Rule (AM No. 12-8-8-SC) applies to both | Same |
| Trial | Continuous Trial (AM No. 15-06-10-SC) applies to both | Same |

## Key Procedural Rules (All Modes)

These rules affect current Philippine court practice and must be considered:

1. **Judicial Affidavit Rule (AM No. 12-8-8-SC)** — direct testimony is submitted via judicial affidavit, not live examination. The affidavit replaces the witness's direct testimony on the stand. Cross-examination is still live. PROSECUTION and DEFENSE witness planning must account for this: direct examination questions become the judicial affidavit's content.

2. **Continuous Trial Guidelines (AM No. 15-06-10-SC)** — trial dates are scheduled continuously, not case-to-case. Motions for postponement are strictly limited. Both sides must have witnesses and evidence ready on scheduled dates. Strategic delays are harder to achieve.

3. **Demurrer to Evidence (Rule 119, Sec. 23)** — after the prosecution rests its case, the defense may file a demurrer (motion to dismiss for insufficiency of evidence) without presenting its own evidence. If granted, the accused is acquitted. If denied without leave of court, the accused waives the right to present evidence. DEFENSE mode must assess whether a demurrer is viable after mapping prosecution evidence to elements.

4. **Rules on Electronic Evidence (AM No. 01-7-01-SC)** — governs admissibility of electronic documents, emails, text messages, social media posts, CCTV footage, digital photographs. Requires authentication (Sec. 2), establishes the ephemeral electronic communications rule (Sec. 1(k)), and defines the business records exception for electronic evidence. Both PROSECUTION and DEFENSE evidence plans must account for electronic evidence authentication requirements.

5. **Plea Bargaining Framework** — governed by DOJ DC No. 18, s. 2018 and SC guidelines. In drug cases, RA 9165 Sec. 23 as amended by RA 10640. PROSECUTION vulnerability assessment should consider whether plea bargaining is strategically advantageous.

---

## CASE Mode

### Phase 1: Issue Identification

Read the case facts, the Information/complaint, and all available evidence. Then identify every legal issue:

1. **Substantive issues** — What are the elements of the offense/cause of action? Which elements are contested?
2. **Procedural issues** — Jurisdiction, venue, prescription, due process, scope of the Information
3. **Evidentiary issues** — Admissibility of each piece of evidence, burden of proof, sufficiency
4. **Affirmative defenses** — What defenses are available? (e.g., talaq under PD 1083, self-defense, prescription)
5. **Constitutional issues** — Any fundamental rights implicated? (privacy, due process, equal protection, right to silence)

Present the issue list to the user before proceeding. This is the roadmap — missed issues cannot be caught until the sweep pass.

### Phase 2: Per-Issue Research Protocol

For EACH issue identified in Phase 1, run this 6-step sequence. The depth adapts to the issue — a constitutional issue gets deeper Constitution search; an admissibility issue gets deeper jurisprudence search. But every step runs for every issue.

#### Step 1: Constitution Check
Search `legislation/Constitution/1987-constitution.md` for relevant provisions.
- Art. III (Bill of Rights) — for privacy, due process, right to silence, search and seizure
- Art. X (Autonomous Regions) — if BARMM jurisdiction is relevant
- Art. XII-XIV — if economic, social justice, or education rights are implicated
- Extract verbatim text. Never paraphrase constitutional provisions from memory.

#### Step 2: Statute Elements
Invoke `/legal-researcher` to find the governing statute and extract:
- The verbatim text of the provision creating the offense/right
- Every element the prosecution/plaintiff must prove
- Penalties or remedies
- Related provisions (definitions, qualifying circumstances, exemptions)

If the statute is already known (e.g., RA 9262 Sec. 5(i)), read it directly from `legislation/national-laws/` instead of invoking the full researcher workflow.

#### Step 3: PD 1083 / Shari'ah Check
**MANDATORY if any party is Muslim or the case involves Muslim personal law** (marriage, divorce, inheritance, custody, property relations).

Invoke `/shariah` to determine:
- Whether PD 1083 applies and which provisions
- PD 1083 Art. 3(1) hierarchy: "In case of conflict between any provision of this Code and laws of general application, the former shall prevail"
- Whether the Shari'ah courts have jurisdiction
- Whether Islamic legal concepts are relevant (talaq, 'idda, ruju, mahr, etc.)

If no Muslim party and no Muslim personal law issue, note "PD 1083: Not applicable" and move on.

#### Step 4: Jurisprudence Search
Search the local archive (`jurisprudence/`) for controlling SC decisions. This is the core competency of this skill — search systematically, not by keyword alone.

**Search strategy (use ALL of these, not just one):**

1. **By statute section** — grep for the specific section number (e.g., `Section 5.*9262`, `Art. 46.*1083`)
2. **By legal doctrine keyword** — grep for the legal concept (e.g., `psychological violence`, `marital infidelity`, `illegal access`, `exclusionary rule`, `talaq`)
3. **By constitutional provision** — grep for the constitutional article identified in Step 1 (e.g., `Art. III.*Sec. 3`, `privacy of communication`)
4. **By G.R. number** — if a known leading case exists, read it directly
5. **By year range** — for recent doctrinal developments, focus on `jurisprudence/2020/` through `jurisprudence/2026/`

**For each case found, extract:**
- G.R. number, title, date, ponente, division (En Banc vs. Division)
- The holding relevant to the issue
- Whether it supports or undermines the position being analyzed
- Whether it is still good law (check for overruling, modification, or supersession)

**Hierarchy of authority:**
- En Banc > Division
- Later decision > Earlier decision (on the same issue)
- But: a Division decision does NOT overturn an En Banc decision (it may signal a shift, but the En Banc ruling controls until expressly reversed)

#### Step 5: Evidence Admissibility Scan
For EACH piece of evidence in the case, assess:

| Question | Source to Check |
|----------|----------------|
| Was it lawfully obtained? | Constitution Art. III Sec. 2 (search/seizure), Sec. 3 (privacy of communication); RA 10175 (Cybercrime — illegal access); RA 4200 (Anti-Wiretapping); RA 10173 (Data Privacy) |
| Does an exclusionary rule apply? | Art. III Sec. 3(2): evidence obtained in violation is "inadmissible for any purpose in any proceeding"; Zulueta v. CA (GR 107383) for private parties |
| Is it relevant? | Rules of Evidence, Rule 128 Sec. 4 |
| Is it hearsay? | Rule 130 |
| Is it privileged? | Marital privilege (Rule 130 Sec. 22); attorney-client; physician-patient |
| Can it be authenticated? | Rule 132 (electronic evidence: Rules on Electronic Evidence, AM 01-7-01-SC) |

Search `jurisprudence/` for admissibility rulings on similar evidence types. The Zulueta lesson: never assume evidence is admissible just because it helps the case.

#### Step 6: Elements Mapping
Map every statutory element to the available facts and evidence:

```
| # | Element | Prosecution Evidence | Defense Counter | Assessment |
|---|---------|---------------------|-----------------|------------|
| 1 | [element text] | [what proves it] | [what negates it] | Proven / Contested / Not proven |
```

Flag elements where the prosecution's evidence is weak or missing. Flag elements where the defense has strong counter-evidence.

### Phase 3: Mandatory Sweep Pass

After completing per-issue research, run these three sweeps across the ENTIRE case. The sweep catches issues the per-issue analysis missed — this is the safety net.

#### Sweep 1: Constitution Sweep
Re-read `legislation/Constitution/1987-constitution.md` Art. III (Bill of Rights) in full. For each right, ask: "Is this right implicated anywhere in this case?" This catches constitutional issues that weren't obvious from the facts alone.

#### Sweep 2: PD 1083 Sweep (if Muslim party)
If any party is Muslim, re-read PD 1083 provisions on:
- Marriage (Arts. 14-34)
- Divorce (Arts. 45-55)
- 'Idda (Arts. 56-59)
- Property relations (Arts. 37-44)
- Succession (Arts. 89-109)
Ask: "Does any PD 1083 provision affect any aspect of this case that wasn't already identified?"

#### Sweep 3: Evidence Admissibility Sweep
List ALL evidence from both sides. For any piece not already assessed in Step 5, run the admissibility checklist. For pieces already assessed, verify the assessment holds in light of the full case picture.

### Phase 4: Verdict Assessment

Synthesize everything into a judicial assessment:

1. **Per-charge/cause of action verdict** — For each charge: Acquittal/Dismissal (and why) or Conviction/Liability (and why)
2. **Strength assessment** — Rate each side's position using this scale:
   - **Strong** — all elements provable/defensible, controlling jurisprudence favorable, no viable counter-argument
   - **Moderate** — most elements covered but 1-2 contested, jurisprudence mixed or evolving, outcome depends on credibility findings
   - **Weak** — key element unprovable/undefendable, controlling jurisprudence adverse, or fatal procedural defect
3. **Worst-case scenario** — What is the most unfavorable realistic outcome? What facts or legal developments would trigger it?
4. **Strategic observations** — Procedural advantages, timing considerations, settlement leverage, appeal prospects

### CASE Mode Output

**MANDATORY QA before delivery** — run both `/legal-reviewer ACCURACY` and `/fact-checker VALIDATE` on the written analysis. Fix all CRITICAL errors before presenting to the user. A case analysis with fabricated citations is worse than no analysis.

Write the analysis to `jurisprudence/cases/` (user can override path).

Filename: `crim-{year}-{case-no}-{short-description}.md` or `civil-{year}-{case-no}-{short-description}.md`

```markdown
# [Case Title]
## [Case Number] — [Court]
## Charge/Cause of Action: [Description]

---

**Date of Analysis:** [date]

---

## I. Issues Identified
[Numbered list of all legal issues]

## II. Per-Issue Analysis

### Issue 1: [Issue Name]
**Constitution:** [relevant provisions with verbatim text]
**Statute:** [governing law with elements]
**PD 1083:** [if applicable]
**Controlling Jurisprudence:**
| Case | Date | Holding | Impact |
**Evidence:** [admissibility assessment for evidence relevant to this issue]
**Elements Map:**
| # | Element | Evidence | Counter | Assessment |

[Repeat for each issue]

## III. Sweep Findings
[Any additional issues or corrections from the three sweeps]

## IV. Verdict Assessment
### Per-Charge Analysis
### Strength Assessment
### Worst-Case Scenario
### Strategic Observations

## V. Authorities Cited
[Full list of all cases, statutes, and constitutional provisions cited]

## VI. Search Record
[Keywords, archive paths searched, what was found vs. not found — for audit]
```

---

## DOCTRINE Mode

### Process

1. **Define the doctrine** — What legal concept? Which statute or constitutional provision? What is the specific question?

2. **Statute foundation** — Invoke `/legal-researcher` to find the statutory text that the doctrine interprets. Read the verbatim provision.

3. **Jurisprudence survey** — Search `jurisprudence/` systematically:
   - Grep by statute section number
   - Grep by doctrine name/keyword
   - Grep by constitutional provision
   - Focus on En Banc decisions (they set binding doctrine)
   - Trace the evolution: earliest case → development → current standard

4. **Doctrinal synthesis** — Organize findings chronologically and identify:
   - The **current controlling standard** (most recent En Banc, or most recent Division if no En Banc)
   - **Doctrinal evolution** — how has the interpretation changed over time?
   - **Concurrences and dissents** — what alternative positions exist within the Court?
   - **Open questions** — what hasn't the SC decided yet?

5. **Legislative implications** — How does this doctrine affect pending or proposed legislation? What does the SC's interpretation mean for legislative drafting?

### DOCTRINE Mode Output

Write to `jurisprudence/doctrines/` (user can override path).

Filename: `doctrine-{statute-or-concept}-{date}.md`

```markdown
# Doctrinal Survey: [Legal Concept]
## Governing Provision: [Statute/Constitutional provision]

**Date:** [date]
**Purpose:** [legislative analysis / policy review / litigation preparation]

---

## I. Statutory Foundation
[Verbatim text of the governing provision]

## II. Doctrinal Evolution

| # | Case | Date | Division | Ponente | Holding | Significance |
|---|------|------|----------|---------|---------|--------------|
[Chronological survey of all relevant SC decisions]

## III. Current Controlling Standard
[The doctrine as it stands today, with citation to the controlling case]

## IV. Concurrences and Dissents
[Alternative positions within the Court — these signal potential doctrinal shifts]

## V. Open Questions
[What the SC hasn't decided; areas of ambiguity]

## VI. Legislative Implications
[How this doctrine affects legislative drafting, pending bills, or policy]

## VII. Authorities Cited
## VIII. Search Record
```

---

## PROSECUTION Mode

Builds the strongest possible case from the complainant/State's perspective. This mode thinks like a prosecutor — identifying what to charge, how to draft the Information, what evidence to present and in what order, which witnesses to call, and how to anticipate and counter defense arguments.

**Read before starting:** `legislation/rules-of-court/criminal-procedure-rules-110-127.md` — particularly Rule 110 (Prosecution of Offenses), Rule 112 (Preliminary Investigation), Rule 119 (Trial).

### Phase 1: Charge Strategy

1. **Identify all possible charges** — read the facts from the complainant's perspective. What laws were violated? What provisions apply? Search the governing statute for ALL applicable sections, not just the obvious one.
2. **Elements analysis per charge** — for each potential charge, extract every element from the statute. Map available evidence to each element. Flag elements where evidence is thin.
3. **Select the optimal charge(s)** — choose the charge(s) with the strongest evidentiary support. Consider:
   - Which charge has the fewest unprovable elements?
   - Which charge carries the most favorable jurisprudential standard? (e.g., GR 252739's presumption of intent for marital infidelity)
   - Can charges be combined or are they mutually exclusive?
   - Is a lesser included offense available as a fallback?
4. **Temporal scope** — what dates should the Information cover? This is a strategic decision. Broader scope captures more conduct but may dilute focus. Narrower scope concentrates the case but risks missing relevant acts.
   - **Lesson from Andy/Boony:** The prosecution charged "on or about February 12, 2025" — post-talaq. If they had charged "from September 2024 through February 2025," the marital infidelity presumption under GR 252739 would have been available. Temporal scope is not a drafting detail — it determines which legal standards apply.

### Phase 2: Draft the Information

Draft the Information following Rule 110, Sec. 6-9:
- Name of accused, offense, acts/omissions constituting the offense
- Approximate date and place
- Name of offended party
- Ensure every element of the offense appears in the allegations

**Self-check:** Read the draft Information against the elements. Does every element have a corresponding allegation? If not, the Information is defective and vulnerable to a Motion to Quash (Rule 117).

### Phase 3: Evidence Plan

For each element of the offense:

| # | Element | Evidence Available | Type | Witness | Admissibility Risk |
|---|---------|-------------------|------|---------|-------------------|
| 1 | [element] | [description] | Documentary/Testimonial/Object | [who presents it] | [any exclusionary rule concern] |

**Presentation order** — plan the sequence of evidence presentation following Rule 119, Sec. 11:
1. Lead with the strongest evidence that establishes the core narrative
2. Build the elements systematically — the court should feel the case is proven element-by-element
3. Anticipate the defense's cross-examination strategy and prepare re-direct questions
4. Reserve rebuttal evidence for defense claims you can anticipate

**Evidence admissibility pre-screen** — run the admissibility scan (CASE mode Step 5) on EVERY piece of prosecution evidence. An inadmissible key exhibit discovered at trial is a catastrophic failure. Better to discover it now and adjust the strategy.

### Phase 4: Witness Sequence

For each witness:
- **Purpose:** What elements does this witness prove?
- **Direct examination outline:** Key questions that establish the elements
- **Anticipated cross-examination:** What will the defense attack?
- **Rehabilitation strategy:** How to recover on re-direct if cross-examination damages the witness?
- **Corroboration:** Which other witnesses or documents support this witness?

**Witness order matters.** Lead with the complainant (establishes the narrative and emotional weight), follow with corroborating witnesses, then expert witnesses if needed, close with documentary/forensic evidence.

### Phase 5: Defense Anticipation

Think adversarially. For each likely defense:

| Defense | Likelihood | Prosecution Counter | Jurisprudential Support |
|---------|-----------|--------------------|-----------------------|
| [e.g., talaq defense] | High/Medium/Low | [how to rebut] | [case law supporting rebuttal] |

**Key questions:**
- What Motions to Quash might the defense file? (Rule 117) How do you oppose?
- What affirmative defenses are available? How do you negate them?
- Will the accused testify? If yes, what cross-examination questions are ready? If no, how does that affect your burden?
- What pre-trial issues should you raise? (Rule 118)

### Phase 6: Vulnerability Assessment

Honestly assess the case's weaknesses:
- Which elements are hardest to prove beyond reasonable doubt?
- What evidence is most vulnerable to exclusion?
- What facts favor the defense?
- What is the realistic probability of conviction?
- Should a plea bargain be considered?

### PROSECUTION Mode Output

Write to `jurisprudence/cases/` (user can override). Filename: `pros-{year}-{case-no}-{short-description}.md`

```markdown
# Prosecution Strategy: [Case Title]
## [Case Number]

**Date:** [date]
**Charge:** [offense]

## I. Charge Strategy
[Selected charge(s) with reasoning]

## II. Draft Information
[Full text of the Information]

## III. Elements Map
| # | Element | Evidence | Witness | Admissibility |

## IV. Evidence Presentation Plan
[Ordered sequence with rationale]

## V. Witness Sequence
[Per-witness outline]

## VI. Defense Anticipation
| Defense | Counter | Case Law |

## VII. Vulnerability Assessment
[Honest weaknesses + mitigation]

## VIII. Authorities Cited
## IX. Search Record
```

---

## DEFENSE Mode

Builds the strongest possible defense from the accused's perspective. This mode thinks like a defense attorney — finding every procedural defect, every unprovable element, every constitutional violation, every credibility gap, and every affirmative defense available.

**Read before starting:** `legislation/rules-of-court/criminal-procedure-rules-110-127.md` — particularly Rule 115 (Rights of Accused), Rule 117 (Motion to Quash), Rule 119 (Trial), Rule 120 (Judgment).

### Phase 1: Rights Inventory

Before anything else, verify the accused's rights were respected at every stage:

1. **Right to preliminary investigation** (Rule 112) — was it conducted? Did the accused receive the subpoena? Was there an opportunity to submit counter-affidavit?
2. **Right to be informed** (Constitution Art. III, Sec. 14(2); Rule 110) — does the Information clearly state all elements? Can the accused prepare a defense based on what's charged?
3. **Right to bail** (Rule 114) — if detained, was bail set? Is the offense bailable?
4. **Right to counsel** (Constitution Art. III, Sec. 14(2)) — at every stage
5. **Right against unreasonable search and seizure** (Art. III, Sec. 2) — was any evidence obtained through an illegal search?
6. **Right to privacy of communication** (Art. III, Sec. 3) — was any electronic evidence obtained without authorization? (Zulueta, RA 10175)
7. **Right to remain silent** (Art. III, Sec. 17) — was the accused pressured to make statements?
8. **Due process** (Art. III, Sec. 1) — any procedural irregularities?

Any violation is a potential ground for exclusion of evidence, quashal of the Information, or appeal.

### Phase 2: Information Analysis

Dissect the Information line by line:

1. **Sufficiency** — does it allege every element of the offense? If any element is missing, the Information is defective (Rule 117, Sec. 3(a): "the facts charged do not constitute an offense").
2. **Temporal scope** — what period is covered? Can the prosecution prove acts within this window? Does the timeframe inadvertently help the defense? (Andy/Boony lesson: "on or about Feb 12" locked the prosecution into the post-talaq period.)
3. **Venue** — is the case filed in the correct court? (Rule 110, Sec. 15)
4. **Prescription** — has the offense prescribed? (Rule 117, Sec. 3(j))
5. **Double jeopardy** — has the accused been previously charged for the same offense? (Rule 117, Sec. 3(i))

**Strategic decision: file a Motion to Quash, or let it proceed?**
- Filing a MTQ alerts the prosecution to defects they can fix (by amending the Information pre-arraignment under Rule 110, Sec. 14)
- Letting a defective Information proceed to arraignment LOCKS IT — the prosecution needs leave of court and accused's consent to amend substantively after arraignment
- Sometimes the smartest defense move is silence

### Phase 3: Affirmative Defenses

Identify every available affirmative defense:

| Defense | Legal Basis | Facts Supporting | Strength |
|---------|-----------|-----------------|----------|
| [e.g., talaq — no marriage existed] | PD 1083, Art. 46 | Talaq pronounced Jan 23, accepted by complainant | Strong |
| [e.g., Acharon — no willful denial] | GR 224946 | Remittances on Feb 8 and Feb 23 | Strong |
| [e.g., GR 264870 — no domination pattern] | GR 264870 | Complainant directed accused to Charlie's apartment | Strong |

For each defense, trace the full legal chain: statute → elements → jurisprudence → application to facts.

### Phase 4: Reasonable Doubt Map

For each element the prosecution must prove, identify where reasonable doubt exists:

| # | Element | Prosecution's Likely Evidence | Reasonable Doubt Source | How to Exploit |
|---|---------|------------------------------|----------------------|---------------|
| 1 | [element] | [their evidence] | [gap, contradiction, or alternative explanation] | [cross-examination question or defense evidence] |

The prosecution must prove EVERY element beyond reasonable doubt. The defense only needs to create reasonable doubt on ONE element.

### Phase 5: Impeachment and Credibility

For each prosecution witness:
- **Prior inconsistent statements** — any sworn statement that contradicts what they'll testify? (Rule 132, Sec. 11)
- **Bias or motive** — does the witness have a reason to lie or exaggerate?
- **Perception issues** — was the witness in a position to observe what they claim?
- **Character for truthfulness** — any evidence of dishonesty? (Rule 132, Sec. 11; Rule 133, Sec. 1)

**The Andy/Boony lesson:** Boony's judicial affidavit claims she "slipped in" to the apartment — but she didn't enter. This is a provably false statement in a sworn document. Impeachment on this point destroys her credibility on all material facts. Save it for cross-examination — don't reveal it in pre-trial filings.

### Phase 6: Evidence Exclusion Strategy

For each piece of prosecution evidence, assess whether a motion to exclude is viable:
- **Constitutional exclusion** — Art. III, Sec. 3(2) (privacy of communication), Sec. 2 (search and seizure)
- **Statutory exclusion** — RA 10175 (illegal access), RA 4200 (anti-wiretapping)
- **Hearsay** — Rule 130
- **Best evidence rule** — Rule 130, Sec. 3
- **Fruit of the poisonous tree** — evidence derived from illegally obtained evidence

### Phase 7: Whether the Accused Should Testify

This is the most consequential strategic decision. Analyze both scenarios:

**Testify:**
- Pros: Can present affirmative defense narrative, humanize the accused, explain context
- Cons: Opens to cross-examination on EVERYTHING. Any inconsistency destroys credibility on all facts. Prosecution can introduce evidence that would otherwise be inadmissible.

**Do not testify (invoke right to silence, Art. III, Sec. 17):**
- Pros: No cross-examination risk. Prosecution must carry its entire burden without any help from the accused.
- Cons: Judge doesn't hear the accused's version. Some defenses (like alibi) are weaker without testimony.

**Default recommendation:** Do NOT testify unless the defense absolutely requires the accused's testimony to establish an element that no other witness or document can prove. The risk of cross-examination almost always outweighs the benefit.

### DEFENSE Mode Output

Write to `jurisprudence/cases/` (user can override). Filename: `def-{year}-{case-no}-{short-description}.md`

```markdown
# Defense Strategy: [Case Title]
## [Case Number]

**Date:** [date]
**Charge:** [offense]
**Accused:** [name]

## I. Rights Inventory
[Any violations found]

## II. Information Analysis
[Defects, temporal scope, strategic implications]

## III. Affirmative Defenses
| Defense | Basis | Facts | Strength |

## IV. Reasonable Doubt Map
| Element | Prosecution Evidence | Doubt Source | Exploitation |

## V. Impeachment Plan
[Per-witness credibility attacks]

## VI. Evidence Exclusion
[Motions to exclude with legal basis]

## VII. Testimony Decision
[Testify / Do not testify — with reasoning]

## VIII. Worst-Case Scenario
[If everything goes wrong, what's the outcome?]

## IX. Authorities Cited
## X. Search Record
```

---

## JUDGE Modes — Judicial Simulation

JUDGE modes simulate a court issuing a decision. The skill first runs the full CASE mode analysis (Phases 1-3), then writes the decision in the court's actual format using the applicable Rules of Court.

**Prerequisite for all JUDGE modes:** Read the applicable Rules of Court from the local archive before writing the decision. The decision must follow procedural rules — not just get the law right, but follow the court's own format and standards.

### Common Process (All JUDGE Modes)

1. **Run CASE mode Phases 1-3** — issue identification, per-issue research, sweep passes
2. **Read applicable Rules of Court** from `legislation/rules-of-court/`
3. **Determine standard of proof** — beyond reasonable doubt (criminal), preponderance of evidence (civil), substantial evidence (administrative)
4. **Weigh the evidence** — assess credibility, resolve conflicting testimonies, apply presumptions from the Rules on Evidence (`legislation/rules-of-court/evidence-rules-128-133.md`)
5. **Write the decision** in the court-specific format (see below)
6. **MANDATORY QA before delivery** — run BOTH of these on the written decision:
   - `/legal-reviewer ACCURACY` — verify every quoted provision is verbatim, every case citation has correct GR number/date/ponente/division, every elements enumeration matches the source decision. Fix all errors before proceeding.
   - `/fact-checker VALIDATE` — classify every factual assertion (SOURCED/INFERENTIAL/UNSOURCED), verify integrity (IC-1 through IC-5), flag any hallucinated citations. Fix all CRITICAL and HIGH errors before proceeding.
   - **The decision is NOT ready for delivery until both pass with 0 CRITICAL errors.** No exceptions — a simulated decision with fabricated citations is worse than no decision.
7. **Output** to `jurisprudence/cases/` with prefix `simulated-` and the court level (e.g., `crim-YYYY-NNNNN-simulated-rtc-decision.md`)

### JUDGE RTC — Regional Trial Court

**Title:** Judge | **Applicable Rules:** Criminal Procedure (Rules 110-127), Civil Procedure (Rules 1-71), Evidence (Rules 128-134)

**Read before writing:**
- `legislation/rules-of-court/criminal-procedure-rules-110-127.md` (criminal cases)
- `legislation/rules-of-court/civil-procedure-rules-1-35.md` + `civil-procedure-rules-36-71.md` (civil cases)
- `legislation/rules-of-court/evidence-rules-128-133.md` (all cases)

**Decision format (Rule 120, Sec. 2 for criminal; Rule 36 for civil):**

```markdown
Republic of the Philippines
REGIONAL TRIAL COURT, [Judicial Region]
Branch ___, [City]

[PLAINTIFF/PEOPLE],
[Party designation],

— versus —

[DEFENDANT/ACCUSED],
[Party designation].

[Case Type] Case No. [Number]
For: [Charge/Cause of Action]

---

D E C I S I O N

[JUDGE NAME], J.:

## Statement of the Case
[Nature of the action, parties, what is being sought]

## Statement of Facts
### Prosecution/Plaintiff's Version
[Narrative of evidence presented]

### Defense Version
[Narrative of evidence presented]

## Issues
[Enumerated legal issues to resolve]

## Discussion

### [Issue 1]
[Analysis: applicable law + evidence + jurisprudence → finding]

### [Issue 2]
[Same pattern]

[Continue for each issue]

## Dispositive Portion

WHEREFORE, premises considered, [judgment is hereby rendered as follows:]

[For criminal: ACQUITTING/CONVICTING the accused...]
[For civil: ordering the defendant to... / dismissing the complaint...]

SO ORDERED.

[City], Philippines, [Date].

[JUDGE NAME]
Presiding Judge
```

**Key rules the RTC must follow:**
- Rule 120, Sec. 1: Judgment must be in writing, personally and directly prepared by the judge, with a statement of facts and law
- Rule 120, Sec. 2: Must contain clearly and distinctly a statement of the facts and the law upon which it is based
- Rule 133, Sec. 1: Preponderance of evidence in civil; proof beyond reasonable doubt in criminal
- The decision must address EVERY issue raised by the parties

### JUDGE CA — Court of Appeals

**Title:** Justice | **Scope:** Reviews errors of law and fact from RTC decisions

**Additional reading:** Rule 44 (ordinary appeal), Rule 46 (certiorari to CA)

**Decision format:**

```markdown
Republic of the Philippines
COURT OF APPEALS
[Division]

[APPELLANT],
[Party]-Appellant,

— versus —

[APPELLEE],
[Party]-Appellee.

CA-G.R. [CR/CV/SP] No. [Number]

---

D E C I S I O N

[JUSTICE NAME], J.:

## Nature of the Case
[Appeal from RTC Branch ___, [City], [Case No.], [Date of RTC Decision]]

## Statement of Facts
[Summary of RTC findings — adopt or modify as needed]

## Errors Assigned
[Enumerate errors claimed by appellant]

## Discussion

### [Error 1]
[Review standard: questions of fact (clearly erroneous) vs. questions of law (de novo)]
[Analysis: was the RTC correct?]

### [Error 2]
[Same pattern]

## Dispositive Portion

WHEREFORE, the appeal is [GRANTED/DENIED]. The Decision dated [date] of the RTC, Branch ___, [City] in [Case No.] is hereby [AFFIRMED/REVERSED/MODIFIED] [specify modifications if any].

SO ORDERED.

[JUSTICE NAME]
Associate Justice

WE CONCUR:
[JUSTICE 2] — Associate Justice
[JUSTICE 3] — Associate Justice
```

### JUDGE SC — Supreme Court

**Title:** Justice | **Scope:** Constitutional questions, doctrinal pronouncements, certiorari, appeals from CA

**Additional reading:** Rule 45 (appeal by certiorari to SC), Rule 65 (certiorari, prohibition, mandamus)

**SC-specific analysis requirements:**
1. **Determine composition** — En Banc (15 Justices, required for constitutional questions and doctrinal reversals) or Division (First, Second, or Third Division, 5 Justices each)
2. **Identify the ratio decidendi** — the legal principle that is binding precedent. Distinguish from obiter dictum (statements not necessary to the decision — persuasive but not binding)
3. **Apply stare decisis** — check whether the issue has been decided before. If following precedent, cite the controlling case. If departing from precedent, explain why (doctrinal evolution, changed circumstances, prior error)
4. **Address constitutional dimensions** — if constitutional rights are implicated, apply the strict scrutiny / rational basis / intermediate scrutiny framework as appropriate
5. **Consider concurrences and dissents** — if the legal question is genuinely debatable, write a concurring or dissenting opinion that articulates the alternative position. This is valuable for anticipating future doctrinal shifts.

**Decision format:**

```markdown
Republic of the Philippines
SUPREME COURT
Manila

[EN BANC / FIRST DIVISION / SECOND DIVISION / THIRD DIVISION]

[PETITIONER],
Petitioner,

— versus —

[RESPONDENT],
Respondent.

G.R. No. [Number]

---

D E C I S I O N

[JUSTICE NAME], J.:

## Nature of the Case
[Petition for review on certiorari / certiorari under Rule 65 / appeal from CA]

## Statement of Facts
[Undisputed facts as found by the lower courts]

## Issues
[Constitutional/doctrinal questions presented]

## Discussion

### [Issue 1]
[Ratio decidendi: the binding legal principle]
[Stare decisis analysis: prior rulings on this issue]
[Application to the facts]

### [Issue 2]
[Same pattern]

## Dispositive Portion

WHEREFORE, the petition is [GRANTED/DENIED]. The Decision dated [date] of the Court of Appeals in [CA Case No.] is hereby [AFFIRMED/REVERSED/MODIFIED].

[If establishing new doctrine: "This Court hereby holds that [doctrinal pronouncement]."]

SO ORDERED.

[PONENTE NAME]
Associate Justice

WE CONCUR:

[For En Banc: list all 15 Justices]
[CHIEF JUSTICE NAME] — Chief Justice
[JUSTICE 2] — Associate Justice (concur / dissent / on leave)
[Continue for all Justices]

[For Division: list 5 Justices]
```

**If writing a concurring opinion:**
```markdown
CONCURRING OPINION

[JUSTICE NAME], J.:

I concur in the result but write separately to [state the reason — e.g., "articulate a narrower ground" or "address an issue the ponencia did not reach"].

[Analysis]
```

**If writing a dissenting opinion:**
```markdown
DISSENTING OPINION

[JUSTICE NAME], J.:

[State the disagreement clearly, then analyze why the majority erred. Dissents often become the basis for future doctrinal reversals — write it to be persuasive to future courts, not just to the current one.]
```

### JUDGE SHARIAH — Shari'ah Circuit/District Court

**Title:** Judge | **Applicable law:** PD 1083 (Code of Muslim Personal Laws), Shari'ah Court Special Rules of Procedure

**Mandatory:** Invoke `/shariah` for PD 1083 analysis before writing the decision.

**Read before writing:**
- `legislation/national-laws/PD-1083.md` — the primary governing law
- Relevant provisions on marriage (Arts. 14-34), divorce (Arts. 45-55), 'idda (Arts. 56-59), property (Arts. 37-44), succession (Arts. 89-109)

**Jurisdiction (PD 1083, Art. 143):**
- **Shari'ah Circuit Court:** original jurisdiction over disputes on marriage, divorce, customary contracts, support, betrothal
- **Shari'ah District Court:** original jurisdiction over cases involving custody, guardianship, legitimacy, paternity; appellate jurisdiction over Circuit Court decisions

**Decision format:**

```markdown
Republic of the Philippines
SHARI'AH [CIRCUIT/DISTRICT] COURT
[Judicial District], [City/Province]

[PETITIONER/PLAINTIFF],
[Party designation],

— versus —

[RESPONDENT/DEFENDANT],
[Party designation].

Shari'ah Case No. [Number]
For: [Nature of case — e.g., Declaration of Divorce, Custody, Support]

---

D E C I S I O N

[JUDGE NAME], J.:

## Statement of the Case
[Nature: petition for declaration of talaq / custody / support / etc.]

## Antecedent Facts
[Marriage, events, Islamic law context]

## Issues
[Legal questions under PD 1083 and Islamic jurisprudence]

## Discussion

### [Issue 1]
[PD 1083 provision + Islamic legal principle + facts → finding]
[When citing Islamic jurisprudence, distinguish between PD 1083 (enacted law) and fiqh (scholarly opinion)]

## Dispositive Portion

WHEREFORE, [the Court finds/declares/orders...]

SO ORDERED.

[City], Philippines, [Date].

[JUDGE NAME]
Presiding Judge
```

**Key Shari'ah Court rules:**
- PD 1083 Art. 3(1): PD 1083 prevails over laws of general application in case of conflict
- Art. 161: Talaq notice filing requirements
- Art. 162-166: Agama Arbitration Council procedures
- The court may reference Islamic jurisprudence (fiqh) but must ground its decision in PD 1083

---

## Anti-Fabrication Rules

These apply to BOTH modes. Fabricated case citations are catastrophic in litigation.

1. **NEVER cite a case without reading it.** If you find a G.R. number via grep, READ the actual file before citing the holding. Grep matches are not holdings.
2. **NEVER invent G.R. numbers.** If you cannot find a case in the local archive, mark it `[UNVERIFIED — not found in local archive]`.
3. **NEVER paraphrase holdings from memory.** Read the decision, extract the relevant passage, quote it.
4. **Verify case metadata.** After reading, confirm: G.R. number, date, ponente, division. Mis-attributed cases destroy credibility.
5. **Check if still good law.** Search for subsequent cases that cite the same G.R. number — look for "overruled", "modified", "abandoned", or "superseded".
6. **En Banc vs. Division matters.** Always note the composition. A Division decision cannot overturn an En Banc decision.

## Local Archive Reference

| Resource | Path | Contents |
|----------|------|----------|
| Constitution | `legislation/Constitution/1987-constitution.md` | Full 1987 Constitution |
| National laws | `legislation/national-laws/` | 11,866 RAs (search INDEX.md first) |
| Executive orders | `legislation/executive-orders/` | 2,572 EOs (1987-2025) |
| Jurisprudence | `jurisprudence/` | ~39,957 SC decisions (1987-2026) |
| Jurisprudence INDEX | `jurisprudence/INDEX.md` | Master index with year-by-year counts |
| Per-year INDEX | `jurisprudence/{year}/INDEX.md` | Year index with case titles |
| PD 1083 | `legislation/national-laws/PD-1083.md` | Code of Muslim Personal Laws |
| RA 10175 | `legislation/national-laws/RA-10000-10499/RA-10175.md` | Cybercrime Prevention Act |
| BOL | `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` | Bangsamoro Organic Law (5 files) |
| BAAs | `legislation/BAAs/` | 89+ Bangsamoro Autonomy Acts |
| DOJ issuances | `legislation/issuances/doj/` | 359 DOJ Department Circulars |
| **Rules of Court** | `legislation/rules-of-court/` | **INDEX + 5 files (756 KB total)** |
| Civil Procedure (1-35) | `legislation/rules-of-court/civil-procedure-rules-1-35.md` | 2019 Amendments (AM No. 19-10-20-SC) |
| Civil Procedure (36-71) | `legislation/rules-of-court/civil-procedure-rules-36-71.md` | Rules 36-71 |
| Criminal Procedure | `legislation/rules-of-court/criminal-procedure-rules-110-127.md` | Revised Rules (Rules 110-127) |
| Evidence (128-133) | `legislation/rules-of-court/evidence-rules-128-133.md` | 2019 Amendments (AM No. 19-08-15-SC) |
| Evidence (134) | `legislation/rules-of-court/evidence-rule-134.md` | Rule 134 — Perpetuation of Testimony |

## Jurisprudence Search Strategy

The archive has ~39,957 decisions across 40 year-folders. Searching effectively requires strategy, not brute force.

**For known cases:** Read directly — `jurisprudence/{year}/GR-{number}.md`

**For unknown cases by legal concept:**
1. Start with `jurisprudence/INDEX.md` — scan year-by-year counts to understand coverage
2. Grep across the full archive by statute section: `grep -r "Section 5.*9262" jurisprudence/`
3. Grep by doctrine keyword: `grep -r "psychological violence" jurisprudence/`
4. Grep by constitutional provision: `grep -r "Art. III.*Sec. 3" jurisprudence/`
5. For recent developments, focus on 2020-2026 year folders
6. Read per-year INDEX files for case titles that suggest relevance

**For doctrinal evolution:**
1. Find the earliest case on the issue
2. Search for cases that CITE that case: `grep -r "GR.*{number}" jurisprudence/`
3. Follow the citation chain forward to the most recent pronouncement
4. Note En Banc vs. Division composition at each step

## Skill Composition

- **Calls /legal-researcher** — for statute search (7-Tier hierarchy), provision text extraction
- **Calls /shariah** — when Muslim personal law (PD 1083) is involved
- **Calls /bangsamoro** — when BARMM governance context is needed
- **Called by** — /legal-assistant, /bill-drafter, /legislative-briefer (when they need jurisprudential analysis)

## Error Handling

| Situation | Mode | Action |
|-----------|------|--------|
| Case not found in local archive | All | Search web (SC E-Library, LawPhil, ChanRobles). Label as `[Source: web — verify]`. |
| G.R. number uncertain | All | Mark `[UNVERIFIED]`. Never guess. |
| Conflicting holdings (En Banc vs. Division) | All | Note both. Flag the conflict. En Banc controls unless expressly reversed. |
| Case appears overruled | All | Note the overruling case. Mark original as `[SUPERSEDED by GR {number}]`. |
| Evidence type not covered by known rules | All | Note the gap. Search for analogous admissibility rulings. |
| PD 1083 applicability unclear | All | Invoke /shariah for jurisdictional analysis. |
| Complainant's facts insufficient for probable cause | PROSECUTION | Flag to user. Identify which elements lack evidentiary support. Suggest what additional evidence is needed. |
| No applicable statute found for alleged conduct | PROSECUTION | Report the gap. Consider whether the conduct may be non-criminal. Check related statutes. |
| Information unavailable or incomplete | DEFENSE | Request from user. If unavailable, analyze based on the charges described and flag assumptions. |
| Accused provides contradictory facts | DEFENSE | Flag the contradictions. Analyze both versions. Recommend which version to present and why. |
| Both parties' evidence equally credible | JUDGE | Apply the standard of proof: in criminal cases, tie goes to the accused (proof beyond reasonable doubt not met). In civil cases, weigh the preponderance. |
| Applicable law is ambiguous or has no controlling jurisprudence | JUDGE | Note the ambiguity. Apply statutory construction rules (plain meaning, legislative intent, ejusdem generis). Flag as a potential appeal issue. |
