---
name: writer
description: Document humanization and technical writing skill for e-Bangsamoro. Transforms AI-generated content into natural, human-sounding prose while adhering to technical writing standards. Use when drafting reports, policy documents, legislative text, or any content requiring professional, authentic voice. Removes AI detection patterns, applies Philippine legal citation standards, and maintains formal yet natural tone.
---

# Writer Skill - Document Humanization

Transform AI-generated content into authentic, professionally-written documents that read naturally while meeting technical writing standards.

## Purpose

Ensures all written outputs:
1. Sound natural and human-authored
2. Follow technical writing conventions
3. Include proper legal/legislative citations (Philippine context)
4. Avoid patterns that trigger AI detection tools
5. Maintain professional, formal tone without artificial stiffness

## Core Workflow

### Phase 1: Content Analysis

Identify the document type and apply appropriate standards:

| Document Type | Tone | Citation Style | Key Focus |
|---------------|------|----------------|-----------|
| Legislative (BAA, resolutions) | Formal | Philippine legal | Precision, clarity |
| Policy/Reports | Professional | Academic/gov't | Evidence-based, direct |
| Technical docs | Clear/Direct | Inline/footnote | Accuracy, brevity |
| Correspondence | Professional | Minimal | Clarity, respect |
| Academic/Research | Scholarly | Philippine Manual | Rigorous citations |

### Phase 2: Anti-Pattern Scan

**CRITICAL: Scan and eliminate AI-detection triggers by risk level.**

#### Tier 1: Extreme Risk (Fix Immediately)

These patterns appear 100-900x more frequently in AI text. **Eliminate completely.**

**High-Frequency Phrases (902x+ ratio):**
- "provide/gain valuable insights" (902x)
- "casting long shadows" (561x)
- "left an indelible mark" (319x)
- "a rich tapestry" (227x)
- "plays a crucial role in shaping" (182x)
- "in today's fast-paced world" (107x)

**Self-Reference Patterns (294,000x ratio):**
- "As an AI language model..."
- "I do not have personal..."
- "As an AI, I..."

**"By..." Sentence Starters:**

| Problematic | Rewrite |
|-------------|---------|
| "By implementing this policy..." | "Implementing this policy..." |
| "By incorporating these changes..." | "These changes incorporate..." |
| "By leveraging technology..." | "Technology enables..." |

#### Tier 2: High Risk (10-100x frequency)

**Dangling -ing Dependent Clauses:**

Avoid: reflecting, indicating, suggesting, resulting, emphasizing, underscoring, demonstrating, highlighting, signifying, illustrating, showcasing, revealing.

| Problematic | Rewrite |
|-------------|---------|
| "The budget increased, reflecting growth." | "The budget increase reflects growth." |
| "Revenue declined, indicating weak demand." | "Revenue declined. This indicates weak demand." |
| "The policy succeeded, resulting in..." | "The policy succeeded and produced..." |

**High-Detection Words:**

| Word | Ratio | Use Instead |
|------|-------|-------------|
| delves | 25.2x | examines, explores |
| showcasing | 9.2x | showing, displaying |
| underscores | 9.1x | emphasizes, shows |
| landscape | 8x+ | field, area |
| multifaceted | 7x+ | complex, varied |

#### Tier 3: Moderate Risk (Formal Connectors)

| Overused | Alternatives |
|----------|--------------|
| represents | is, serves as, shows |
| constitutes | is, makes up, forms |
| comprises | includes, contains, has |
| encompasses | includes, covers, spans |
| facilitates | helps, enables, supports |
| leverages | uses, applies, employs |
| utilizes | uses |

#### Tier 4: Structural Patterns

**Formulaic Transitions:** Avoid Moreover, Furthermore, Additionally, Consequently, Subsequently, Hence, Thus, Therefore at sentence start. Use sparingly (max 1 per 3-4 paragraphs).

**Three-Beat Cadences:** Avoid "Fast, efficient, and reliable" rhythms. Vary list lengths.

**Em-Dash Overuse:** AI uses em-dashes at 3x human rate. Use commas or parentheses instead.

**Uniform Sentence Length:** Mix short (5-12 words), medium (13-20), and longer (21-30) sentences to increase burstiness.

See [references/humanization-patterns.md](references/humanization-patterns.md) for comprehensive pattern library with 100+ AI slop words and frequency data.

### Phase 3: Voice and Tone Adjustments

#### Active Voice Priority

Convert passive to active where clarity improves:
- Before: "The report was submitted by the committee."
- After: "The committee submitted the report."

**Exception:** Passive voice is appropriate when the actor is unknown, unimportant, or when emphasizing the action's recipient (common in legal writing).

#### Sentence Variety

Mix sentence lengths:
- Short sentences for impact (10-15 words)
- Medium sentences for explanation (15-25 words)
- Occasional longer sentences for complex ideas (25-35 words)

**Avoid:** Uniform sentence lengths (AI pattern).

#### Natural Rhythm

Read aloud mentally. Adjust anything that sounds:
- Stilted or mechanical
- Overly formal for context
- Repetitive in structure

### Phase 4: Technical Writing Standards

See [references/technical-writing-standards.md](references/technical-writing-standards.md) for complete guide.

#### Clarity Principles

1. **One idea per sentence** - Split complex sentences
2. **Specific over vague** - "15 barangays" not "several localities"
3. **Concrete over abstract** - Measurable outcomes, not aspirational language
4. **Action verbs** - "The ministry will implement" not "implementation will occur"

#### Concision Rules

Remove:
- Redundant words ("advance planning" → "planning")
- Empty phrases ("in order to" → "to")
- Throat-clearing ("It is important to note that" → delete)
- Unnecessary hedging ("perhaps," "somewhat" — unless precision requires)

### Phase 5: Legal/Legislative Citations

**For Philippine legal documents, cite properly.**

See [references/legal-citation-guide.md](references/legal-citation-guide.md) for complete formats.

#### Quick Reference

| Source | Format |
|--------|--------|
| Constitution | CONST. art. [No.], § [No.] |
| Republic Act | Rep. Act No. [No.], § [No.] ([Year]) |
| Bangsamoro Autonomy Act | BAA No. [No.], § [No.] ([Year]) |
| Supreme Court Decision | [Case], G.R. No. [No.], [Date] |
| Administrative Order | [Agency] A.O. No. [No.], § [No.] ([Year]) |

**Requirements:**
- Cite the specific provision, section, or article
- Include relevant text in block quotes for substantive references
- **Embolden** the portion directly relevant to the discussion

#### Example:

> Section 3, Article X of the 1987 Constitution provides: "The Congress shall enact a law providing for the creation of the Bangsamoro Autonomous Region, **subject to a plebiscite to be called for the purpose**..."

### Phase 6: Final Review Checklist

Before output, verify:

```
TIER 1 - EXTREME RISK (Must Fix):
[ ] No 100x+ frequency phrases ("valuable insights", "rich tapestry", etc.)
[ ] No AI self-reference patterns
[ ] No sentences start with "By..."

TIER 2 - HIGH RISK:
[ ] No -ing dangling clauses (reflecting, indicating, showcasing, etc.)
[ ] No high-detection words (delves, underscores, landscape, etc.)

TIER 3 - MODERATE RISK:
[ ] Formal connectors minimized (represents, constitutes, encompasses)
[ ] Transitions used sparingly (max 1 per 3-4 paragraphs)

TIER 4 - STRUCTURAL:
[ ] Varied sentence lengths (burstiness check)
[ ] No three-beat cadences throughout
[ ] Em-dashes used sparingly
[ ] Paragraph lengths vary

QUALITY:
[ ] Active voice predominant
[ ] All legal/policy claims properly cited
[ ] Terminology consistent throughout
[ ] No throat-clearing phrases ("It is important to note...")
[ ] Reads naturally when spoken aloud
[ ] Matches intended document type tone
```

## Usage Modes

### Mode 1: Full Document Humanization

Transform entire AI-generated document:
1. Apply all phases sequentially
2. Preserve meaning while improving naturalness
3. Ensure citation compliance

### Mode 2: Quick Edit

For shorter text or specific passages:
1. Focus on Pattern elimination (Phase 2)
2. Apply voice adjustments (Phase 3)
3. Skip full citation review if not legal content

### Mode 3: Citation Enhancement

For documents needing legal/policy citations:
1. Identify claims requiring citation
2. Apply Philippine citation standards
3. Format block quotes with emboldened relevant text

## Output Quality Markers

**Well-humanized text:**
- Reads like a competent professional wrote it
- No repetitive structural patterns
- Varied vocabulary (not thesaurus abuse)
- Clear, direct statements
- Proper citations where needed
- Natural flow between paragraphs
- High burstiness (varied sentence lengths)
- Zero extreme-risk phrases (902x+ frequency)

**Still needs work:**
- Multiple sentences starting the same way
- Heavy use of "represents," "constitutes," "encompasses"
- Long strings of -ing dependent clauses
- Uniform sentence length (low burstiness)
- Missing citations for claims
- Robotic, stilted rhythm
- Em-dash overuse (3x human rate)
- Three-beat cadences throughout
- Contains any 100x+ frequency phrases

## Detection Methodology Understanding

AI detectors analyze two primary metrics:

**Perplexity:** How predictable word choices are
- Low perplexity = AI likely (statistically optimal word selection)
- High perplexity = Human likely (unexpected, varied choices)

**Burstiness:** Variation in sentence length and complexity
- Low burstiness = AI likely (uniform sentences)
- High burstiness = Human likely (varied rhythm, mixed lengths)

Human writing has natural irregularities. AI writing tends toward statistical uniformity. The /writer skill targets these metrics by:
1. Replacing high-frequency AI phrases with less predictable alternatives
2. Varying sentence lengths deliberately
3. Breaking structural patterns (three-beat, uniform paragraphs)

## References

| Reference | Purpose |
|-----------|---------|
| [humanization-patterns.md](references/humanization-patterns.md) | Comprehensive AI pattern avoidance |
| [technical-writing-standards.md](references/technical-writing-standards.md) | Government/professional writing standards |
| [legal-citation-guide.md](references/legal-citation-guide.md) | Philippine legal citation formats |

## Context

Research and examples are contextualized for the Philippines and BARMM governance. All legal citations follow Philippine standards (Philippine Manual of Legal Citations, Supreme Court Manual of Judicial Writing, Ombudsman Stylebook).
