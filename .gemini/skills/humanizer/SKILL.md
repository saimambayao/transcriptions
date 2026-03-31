---
name: humanizer
description: |
  This skill should be used when the user wants to eliminate AI slop, improve AI-generated
  output quality, humanize text, make writing sound natural, or avoid generic AI patterns.
  Use when the user says "humanize this", "make it sound human", "remove AI slop",
  "improve this writing", "make it less AI", "clean up this output", "this sounds robotic",
  "too generic", "sounds like ChatGPT", or when reviewing any AI-generated content for
  quality. Also trigger when drafting reports, research notes, knowledge documentation,
  organized notes, session summaries, policy documents, or any content that should read
  like a competent human wrote it. Works with all writing contexts — structured notes,
  bullet points, prose, legal documents, technical docs, and casual content.
argument-hint: "[text-or-file]"
---

# Humanizer — AI Output Quality Control

Eliminate AI slop. Make every output read like a sharp, competent human wrote it.

AI text fails in predictable ways: overused phrases, uniform rhythm, hollow transitions,
and a distinctive "helpful assistant" voice that readers recognize instantly. This skill
targets those patterns systematically across every writing context.

## How It Works

1. **Detect context** — what kind of content is this?
2. **Scan for AI patterns** — tiered by severity (see references/anti-patterns.md)
3. **Fix the problems** — replace, restructure, or delete
4. **Verify quality** — checklist pass before output

## Step 1: Detect Context

Identify the writing mode and apply appropriate standards:

| Mode | Tone | Key Focus |
|------|------|-----------|
| **Structured notes** (bullets, organized notes, transcripts) | Direct, scannable | Bold keywords, no filler, varied bullet lengths |
| **Research/knowledge docs** (vault notes, takeaways) | Authoritative, concise | Evidence over assertion, specific over vague |
| **Reports/policy** (formal documents, briefers) | Professional | Precision, citations, measured language |
| **Legal/legislative** (BAA, resolutions, laws) | Formal | Philippine citation standards (see references/) |
| **General content** (blog posts, emails, descriptions) | Natural, conversational | Reads like a real person talking to another |
| **Technical docs** (README, API docs, skill files) | Clear, imperative | Accuracy, brevity, zero fluff |

## Step 2: Scan and Fix AI Patterns

Apply the 4-tier anti-pattern scan. Full pattern library with 100+ phrases and frequency
data is in [references/anti-patterns.md](references/anti-patterns.md).

### Tier 1: Kill on Sight (100x+ AI frequency)

These phrases appear hundreds of times more often in AI text than human text. Delete or
rewrite every instance — no exceptions.

| Pattern | What to do |
|---------|------------|
| "valuable insights", "rich tapestry", "indelible mark" | Delete the whole sentence. Rewrite from scratch. |
| "plays a crucial role in shaping" | Say what it actually does. |
| "in today's fast-paced world" | Delete. Just start with the point. |
| "As an AI..." / "I don't have personal..." | Never appear. |
| Sentences starting with "By..." | Restructure: "By implementing X" becomes "X does Y" |

### Tier 2: Rewrite (10-100x frequency)

| Pattern | Fix |
|---------|-----|
| Dangling -ing clauses ("reflecting", "indicating", "showcasing") | Make it a new sentence or use a direct verb |
| "delves" (25x), "underscores" (9x), "landscape" (8x), "multifaceted" (7x) | Use plain words: examines, shows, field, complex |

### Tier 3: Minimize (formal connectors)

Replace "represents", "constitutes", "encompasses", "facilitates", "leverages", "utilizes"
with plain English: is, includes, helps, uses.

### Tier 4: Break Structural Patterns

| Pattern | Fix |
|---------|-----|
| Formulaic transitions (Moreover, Furthermore, Additionally) | Max 1 per 3-4 paragraphs. Use topic sentences instead. |
| Three-beat cadences ("fast, efficient, and reliable") | Vary list lengths. Drop to 2, or expand to 4-5. |
| Em-dash overuse | AI uses 3x human rate. Use commas or parentheses. |
| Uniform sentence length | Mix short (5-12), medium (13-20), long (21-30) words. |
| Uniform paragraph length | Vary. A one-sentence paragraph has impact. |

### Structured Content (Bullets & Lists)

Most AI output is bulleted/structured. These patterns are specific to that format:

| AI Pattern | Human Pattern |
|------------|---------------|
| Every bullet starts with bold keyword | Mix: some bold, some not, some start with verbs |
| Every bullet is the same length (15-20 words) | Vary: some 5 words, some 25 |
| Every bullet follows "**Keyword** — explanation" | Mix formats: questions, sentence fragments, bold mid-sentence |
| Nested bullets all at same depth | Use 2 levels max. Flatten when possible. |
| "Key takeaways:" followed by 5 perfectly parallel bullets | Break parallelism. Let some bullets be incomplete thoughts. |
| Numbered lists for everything | Numbers for sequences. Bullets for sets. |

**Before (AI slop):**
- **Comprehensive framework** — provides a robust and multifaceted approach to governance
- **Stakeholder engagement** — facilitates meaningful dialogue with key stakeholders
- **Sustainable development** — ensures long-term sustainability of initiatives

**After (human):**
- Governance framework covering the 5 provinces and Cotabato City
- Stakeholders get a seat at the table through quarterly forums
- Built to last — the 2028 sunset clause forces a sustainability plan

## Step 3: Voice and Tone

### Active Over Passive
- Before: "The report was submitted by the committee."
- After: "The committee submitted the report."

Exception: passive is fine when the actor is unknown or unimportant.

### Specific Over Vague
- Before: "Several barangays were affected."
- After: "15 barangays in Maguindanao del Sur were affected."
- Before: "Cooperatives have grown significantly."
- After: "12,058 registered cooperatives operate in BARMM as of 2025."

When you know the real number, use it. When you don't, insert `[X]` as a placeholder
so the author fills it in. Never leave "several", "various", or "many" standing when
a count exists somewhere.

### Bullet Length Variation
Deliberately make at least one bullet under 8 words and one over 20. A 5-word bullet
hits harder than a 15-word one saying the same thing. Example:
- CSEA audits everything. (4 words)
- The cooperative governance model requires quarterly financial reporting to CSEA with independent audit verification for any cooperative managing over PHP 1 million in assets. (26 words)

### Concrete Over Aspirational
- Before: "The initiative will create transformative impact."
- After: "The initiative trained 200 cooperative officers in 2025."

### Concision
Delete: "It is important to note that", "in order to" (just "to"), "advance planning"
(just "planning"), unnecessary hedging ("perhaps", "somewhat").

## Step 4: Final Checklist

Before delivering output, verify:

```
TIER 1: [ ] Zero 100x+ frequency phrases
TIER 2: [ ] No -ing dangling clauses, no "delves/underscores/landscape"
TIER 3: [ ] Formal connectors minimized
TIER 4: [ ] Varied sentence lengths, no three-beat cadences, minimal em-dashes

STRUCTURED CONTENT:
[ ] Bullet lengths vary (not all 15-20 words)
[ ] Bullet formats vary (not all "**Bold** — explanation")
[ ] No more than 2 nesting levels

VOICE:
[ ] Active voice predominant
[ ] Specific numbers and names over vague references
[ ] Concrete outcomes over aspirational language
[ ] No throat-clearing phrases
[ ] Reads naturally spoken aloud
```

## When NOT to Humanize

Skip or tread lightly in these cases:
- **Code blocks** — never modify code syntax, variable names, or comments for "humanization"
- **Direct quotes** — preserve the speaker's exact words even if they contain AI-like patterns
- **Already-human text** — if the input reads naturally, say so and make minimal changes
- **Very short input** (1-2 sentences) — use Mode 2 Quick Scan, don't over-process
- **Intentional style** — if the user deliberately chose formal/academic tone, respect it

## Proactive Application

The best humanization is never producing slop in the first place. When generating content
(not just editing), apply the checklist mentally BEFORE delivering output. Catch yourself
reaching for "valuable insights" or "rich tapestry" and replace in real-time. This skill
applies to your own output as much as it does to text you're editing.

For long documents (10+ pages): do a Tier 1 sweep first (fastest, highest impact), then
Tier 2-4 in a second pass. Prioritize the opening and closing — readers notice those most.

## Modes

### Mode 1: Full Humanization
Transform entire document or long text. Apply all steps sequentially.

### Mode 2: Quick Scan
For shorter text or inline output. Focus on Tier 1-2 patterns and structural fixes.
Skip legal citations unless content is legislative.

### Mode 3: Legal/Policy Mode
Apply all steps plus Philippine legal citation standards.
See [references/legal-citation-guide.md](references/legal-citation-guide.md) for formats.

Quick reference:
| Source | Format |
|--------|--------|
| Constitution | CONST. art. [No.], SS [No.] |
| Republic Act | Rep. Act No. [No.], SS [No.] ([Year]) |
| BAA | BAA No. [No.], SS [No.] ([Year]) |
| Supreme Court | [Case], G.R. No. [No.], [Date] |

## Why This Matters

AI detectors measure two things:
- **Perplexity** — how predictable word choices are (low = AI, high = human)
- **Burstiness** — variation in sentence length (low = AI, high = human)

Every fix in this skill increases perplexity (less predictable words) and burstiness
(varied rhythm). The goal is not to "trick" detectors — it's to write better.
Text that reads like a human wrote it IS better writing.

## References

| File | Purpose |
|------|---------|
| [anti-patterns.md](references/anti-patterns.md) | Full 100+ phrase library with frequency data |
| [technical-writing-standards.md](references/technical-writing-standards.md) | Government/professional writing standards |
| [legal-citation-guide.md](references/legal-citation-guide.md) | Philippine legal citation formats |
