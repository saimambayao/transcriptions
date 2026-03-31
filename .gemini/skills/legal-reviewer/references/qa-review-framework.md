# Q&A Legal Review Framework

A 6-dimension review framework for evaluating Q&A legal analysis content — legal references, legal briefers, legislative briefers, and any document structured as questions and answers about law.

## When to Use

Apply this framework whenever reviewing:
- Legal reference files (BOL powers, legislative analyses)
- Legal briefer Q&A sections
- Legislative briefer Q&A sections
- Legal assistant MEMO/IRAC outputs
- Any Q&A-structured legal content

## The 6 Dimensions

### 1. RELEVANCE — "Is this the right question?"

| Check | What the Reviewer Asks |
|-------|----------------------|
| **Need** | Does this question address what a researcher, legislator, or consultant would actually need to know? |
| **Precision** | Is the question specific enough to have a definitive, citable answer — or is it so broad that the answer becomes vague? |
| **Redundancy** | Is this question already answered by another Q in the same document? Does it overlap with a different section/theme? |
| **Missing questions** | What question SHOULD be here that isn't? What would a parliamentary researcher ask that this document doesn't answer? |
| **Sequencing** | Is the question in the right section? Does it belong earlier or later in the logical flow? |

**Pass criteria:** The question addresses a real need, is specific enough to answer definitively, is not duplicated, and is in the right position.

### 2. EVIDENCE — "Is the answer backed by enacted law?"

| Check | What the Reviewer Asks |
|-------|----------------------|
| **Source identification** | Does the answer cite a specific provision (Article, Section, subsection) for every legal claim? |
| **Source type** | Is the source **enacted law** (Constitution, BOL, BAA, RA, EO, PD) — NOT a guidebook, commentary, training material, or academic text? |
| **Traceability** | Can a reader follow the citation back to the actual text of the law and verify the claim independently? |
| **Contradicting provisions** | Are there provisions in OTHER laws that contradict or qualify the answer — provisions the answer doesn't address? |
| **Unsupported conclusions** | Does the answer reach a legal conclusion (e.g., "BARMM can diverge") without citing the provision that supports it? Every legal conclusion needs a statutory basis. |

**Pass criteria:** Every legal claim cites a specific provision of enacted law. No conclusions without statutory basis. Contradicting provisions addressed.

### 3. VERBATIM — "Is the quoted text correct?"

| Check | What the Reviewer Asks |
|-------|----------------------|
| **Word-for-word match** | Does every ***bold italic*** quote match the actual source text character-by-character? |
| **Citation accuracy** | Do article/section numbers point to the correct provision? (The #1 fabrication pattern in AI-generated legal content) |
| **Ellipsis integrity** | When quotes use "..." to compress, does the omission change the meaning? |
| **Context fidelity** | Is the quote used in a way that accurately represents its context in the law — or is it taken out of context to support a point the provision doesn't actually make? |

**Pass criteria:** Every quote matches source text. Every citation points to the correct provision. No meaning-altering omissions or out-of-context usage.

### 4. INCLUSIVENESS — "What's missing?"

| Check | What the Reviewer Asks |
|-------|----------------------|
| **BOL coverage** | Did the answer scan ALL 18 BOL articles — or only the obvious one? Are there provisions in other articles that elaborate, limit, or qualify? |
| **National law coverage** | Did the answer scan the full RA index (11,866 RAs) and EO index (2,572 EOs) — or only list the obvious laws? |
| **Constitutional coverage** | Are all applicable constitutional provisions identified — equal protection, due process, subject-specific articles, state policies (Art. II)? |
| **Shari'ah coverage** | Is there a Shari'ah dimension the answer missed? PD 1083 relevance? BOL Art. X Sec. 4 commercial authority? Islamic principles? |
| **Jurisprudence** | Are there Supreme Court decisions that define boundaries, resolve jurisdiction questions, or interpret related provisions? |
| **Alternative answers** | Are there other legally defensible answers to this question? If the answer presents one interpretation, are there others the reader should know about? Multiple valid readings of the same provision should be acknowledged. |

**Pass criteria:** All relevant legal sources scanned (not just obvious ones). Alternative interpretations acknowledged where they exist.

### 5. ASSUMPTIONS — "What's assumed and is it valid?"

| Check | What the Reviewer Asks |
|-------|----------------------|
| **Hidden assumptions** | What legal assumptions does the answer make that are NOT stated explicitly? Common hidden assumptions: "BOL silence = BARMM can legislate freely" (assumes silence is permissive); "suppletory national law ceases when BAA is enacted" (assumes clean substitution); "the BOL authorizes divergence because it's a congressional act" (assumes congressional intent from the act's existence) |
| **Assumption validity** | Is each assumption supported by legal doctrine, jurisprudence, or explicit statutory language — or is it the writer's interpretation presented as established law? |
| **Counterarguments** | What would the opposing argument be? If a national agency challenged BARMM's authority, what would they cite? If a cooperative member challenged BARMM's different standards, what constitutional argument would they make? |
| **Doctrinal grounding** | Does the answer rest on established Philippine legal doctrine (e.g., *ejusdem generis*, *expressio unius*, police power doctrine, *dura lex sed lex*) — and if so, is the doctrine correctly stated and applied? |
| **Temporal assumptions** | Does the answer assume current conditions (e.g., "no BAA exists," "as of BAA 89") that will change? Is the answer structured to remain useful when conditions change, or will it become misleading? |

**Pass criteria:** All assumptions stated explicitly. Each assumption validated against enacted law or established doctrine. Counterarguments presented for contested positions.

### 6. EFFECTIVENESS — "How should the answer be delivered?"

| Check | What the Reviewer Asks |
|-------|----------------------|
| **Statutory language** | Does the answer use the language of the law — or does it substitute generic paraphrases? The law says ***"shall exercise its authority over"*** — the answer should use that phrase, not "the BOL allows" or "BARMM has the power to." |
| **Directness** | Does the answer address the SPECIFIC question asked — or does it answer a related but different question? If Q asks "Does the BOL require consistency?" the A should start with "Yes" or "No" — not with background. |
| **Audience calibration** | Would a parliamentary staff member (not a lawyer) understand this? Are legal terms defined or explained on first use? Is jargon avoided where plain language suffices? |
| **Actionability** | Can the reader DO something with this answer — cite it in a bill concept note, use it in a policy brief, make a governance decision? Or is it purely informational with no practical application? |
| **Proportionality** | Is the length appropriate? Simple yes/no questions need a direct answer + citation (2-3 sentences). Complex analytical questions (divergence, constitutional implications) warrant thorough treatment (2-3 paragraphs). |

**Pass criteria:** Answers use statutory language. Direct response before elaboration. Accessible to non-lawyers. Actionable. Length proportional to complexity.

## Review Report Format

For each Q&A pair reviewed:

```markdown
### Q[N]: [Question text]

| Dimension | Score | Finding |
|-----------|-------|---------|
| Relevance | PASS / FAIL / IMPROVE | [Details] |
| Evidence | PASS / FAIL / IMPROVE | [Details — cite missing sources] |
| Verbatim | PASS / FAIL / IMPROVE | [Details — cite mismatches] |
| Inclusiveness | PASS / FAIL / IMPROVE | [Details — cite missing provisions] |
| Assumptions | PASS / FAIL / IMPROVE | [Details — list hidden assumptions] |
| Effectiveness | PASS / FAIL / IMPROVE | [Details — suggest improvements] |

**Action:** [KEEP / REVISE / MERGE / REMOVE / ADD NEW Q]
**Suggested revision:** [If REVISE, provide the improved Q and/or A]
```

## Scoring

- **PASS** — meets all checks for this dimension
- **IMPROVE** — meets most checks but has specific weaknesses that should be addressed
- **FAIL** — does not meet the dimension's pass criteria; must be fixed before the document ships

## Relationship to Existing /legal-reviewer Modes

| Existing Mode | Relationship to Q&A Review |
|--------------|---------------------------|
| ACCURACY | Dimension 3 (Verbatim) is a subset of ACCURACY mode |
| COMPLIANCE | Dimensions 2 (Evidence) and 4 (Inclusiveness) overlap with hierarchy compliance |
| AUTHORITY | Dimension 5 (Assumptions) covers authority analysis |
| SUFFICIENCY | Dimension 4 (Inclusiveness) covers sufficiency |
| CURRENCY | Dimension 5 temporal assumptions covers currency |
| FULL | Q&A Review is complementary — FULL reviews documents, Q&A Review reviews Q&A-structured content |

## New Mode: QA-REVIEW

Invoke with: `/legal-reviewer QA-REVIEW [file]`

Applies all 6 dimensions to every Q&A pair in the document. Produces the review report above. Corrections are applied via Edit tool. The review iterates until all FAILs are resolved (Legal QA Loop — max 5 iterations).
