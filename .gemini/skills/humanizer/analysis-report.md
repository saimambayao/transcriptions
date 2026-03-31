# Skill Analysis Report: humanizer

**Analyzed:** 2026-03-23
**Lines:** 187 (SKILL.md) + 189 (anti-patterns.md) + 285 (technical-writing-standards.md) + legal-citation-guide.md
**Tier:** Tier 2 — Usable
**References:** 3 files

## Score Card

| Dimension | Rating | Key Finding |
|-----------|--------|-------------|
| YAML Frontmatter | **Strong** | Rich description with 12+ trigger phrases, pushy, third person. Missing `allowed-tools`. |
| Phase Architecture | **Adequate** | 4 clear steps but no actor roles, no explicit input/output per step. |
| Output Specification | **Weak** | Has before/after examples but no complete output template showing a full humanized document. |
| Constraint Density | **Strong** | Data-backed frequency ratios (902x, 25x), specific word lists, measurable rules (max 1 per 3-4 paragraphs). |
| Error Handling | **Absent** | No guidance for: input is already human-quality, input is code (not prose), input is too short to humanize, conflicting mode signals. |
| Examples & Demonstration | **Adequate** | 1 good before/after for bullets (lines 97-105), 3 voice examples. No complete document transformation. |
| Scaling & Complexity | **Adequate** | 3 modes (Full, Quick, Legal) handle different scales. No guidance on very long documents (10+ pages). |

## Detailed Findings

### YAML Frontmatter — Strong
The description (lines 3-12) is well-crafted: third person, 12+ trigger phrases in quotes, covers multiple contexts (structured notes, bullets, prose, legal, technical, casual). The `argument-hint` is present. **Gap:** No `allowed-tools` field — this skill primarily uses Read and Edit tools but doesn't declare them. Not critical since it's mostly a behavioral/writing-style skill.

### Phase Architecture — Adequate
Four steps (Detect Context → Scan Patterns → Voice/Tone → Checklist) with a clear flow. **Gap:** No explicit actor role (is Claude applying this to its OWN output, or transforming a user-provided document?). No input/output contract per step. Step 2 and Step 2b could be a single step — the "2b" numbering suggests it was added later and not fully integrated.

### Output Specification — Weak
The skill tells Claude WHAT to fix but not WHAT the final output should look like structurally. For Mode 1 (Full Humanization), there's no template showing: "Given this AI document, produce this humanized version." The before/after example on lines 97-105 is excellent but only covers 3 bullet points — not a full document transformation.

### Constraint Density — Strong
This is the skill's standout feature. Frequency ratios (902x, 561x, 25.2x) are concrete and data-backed. The 4-tier system with escalating severity is well-designed. Measurable rules: "max 1 transition per 3-4 paragraphs", "mix 5-12, 13-20, 21-30 word sentences". The structured content patterns table (lines 88-95) is specific and actionable.

### Error Handling — Absent
No guidance for edge cases:
- What if the input text is already well-written? (Don't over-correct)
- What if the input is code, not prose? (Skip or handle differently)
- What if the input is very short (1-2 sentences)? (Quick Scan mode, but not stated)
- What if Mode detection is ambiguous? (Research note that's also policy-adjacent)
- What if the user wants to keep a specific AI-ish phrase for emphasis?

### Examples — Adequate
The bullet before/after (lines 97-105) is the strongest part — concrete, contextual (BARMM governance), shows the transformation clearly. The voice examples (lines 109-121) are good but standard. **Gap:** No full-document before/after. No edge case examples. No example showing structured notes transformation (the user's most common output).

### Scaling — Adequate
Three modes handle different scales (Full, Quick, Legal). **Gap:** No guidance for very long documents (what to prioritize in a 20-page report vs a 3-bullet list). No mention of processing strategy — do you do one pass or multiple passes?

## Recommended Evals

### Recommended Eval 1
**Question:** Does the output contain zero Tier 1 phrases (valuable insights, rich tapestry, indelible mark, crucial role in shaping, fast-paced world)?
**Tests dimension:** Constraint Density
**Why this matters:** Tier 1 phrases are the most detectable AI signals. If even one survives, the skill failed its primary job.
**Risk of gaming:** Low — these are specific strings that can be checked programmatically.
**Priority:** Critical

PASS: Zero matches for any Tier 1 phrase in the output.
FAIL: One or more Tier 1 phrases present.

### Recommended Eval 2
**Question:** Do bullet point lengths vary by at least 2x (shortest vs longest bullet)?
**Tests dimension:** Output Specification (structural patterns)
**Why this matters:** Uniform bullet length is one of the strongest AI signals in structured content — the user's most common output format.
**Risk of gaming:** Medium — model could artificially pad/trim bullets without improving quality.
**Priority:** Critical

PASS: Shortest bullet is under 10 words AND longest is over 20 words.
FAIL: All bullets within 5-word range of each other.

### Recommended Eval 3
**Question:** Does the output use active voice in at least 70% of sentences?
**Tests dimension:** Voice and Tone (Step 3)
**Why this matters:** Passive voice at scale is an AI signal. Active voice is also just better writing.
**Risk of gaming:** Low — requires genuine sentence restructuring.
**Priority:** Important

PASS: 70%+ of sentences use active voice constructions.
FAIL: Less than 70% active voice.

### Recommended Eval 4
**Question:** Does the output contain zero formulaic transitions (Moreover, Furthermore, Additionally, Consequently, Subsequently) at sentence start?
**Tests dimension:** Constraint Density (Tier 4)
**Why this matters:** These transitions are the most common "tell" in paragraph-level AI text.
**Risk of gaming:** Low — specific strings at sentence start, easily checked.
**Priority:** Important

PASS: No sentences begin with these transition words.
FAIL: One or more sentences start with formulaic transitions.

### Recommended Eval 5
**Question:** Does the output avoid the "**Bold** — explanation" bullet format monotony (not all bullets follow the same format)?
**Tests dimension:** Structured Content (Step 2b)
**Why this matters:** The most common AI bullet pattern. The user's organized notes should break this.
**Risk of gaming:** Medium — model could vary format artificially.
**Priority:** Important

PASS: At least 2 different bullet formats used (e.g., some bold-start, some plain, some with numbers).
FAIL: All bullets follow identical "**Bold** — explanation" format.

### Recommended Eval 6
**Question:** Are concrete numbers, names, or specific references used instead of vague quantifiers ("several", "many", "various")?
**Tests dimension:** Voice and Tone (Specific Over Vague)
**Why this matters:** Vague quantifiers are an AI crutch. Specific details signal human authorship.
**Risk of gaming:** Medium — model could insert arbitrary numbers.
**Priority:** Nice-to-have

PASS: Output uses specific numbers/names in 80%+ of factual claims.
FAIL: Multiple uses of "several", "various", "numerous" without specifics.

## Optimization Recommendations

### Quick Wins (high impact, low effort)

1. **Fix `technical-writing-standards.md` reference** — addresses Output Specification
   WHY: The file currently contains a copy of the OLD humanizer skill (the writer skill), not actual technical writing standards. It's 285 lines of duplicated content that wastes context.
   HOW: Replace with actual technical writing standards (plain language principles, government writing guides, readability rules).

2. **Add `allowed-tools` to frontmatter** — addresses YAML Frontmatter
   WHY: Follows Skills 2.0 best practices from Guidelines.md.
   HOW: Add `allowed-tools: Read, Edit, Write, Grep` since the skill may need to read files and edit them.

3. **Merge Step 2 and Step 2b** — addresses Phase Architecture
   WHY: "Step 2b" naming suggests a bolt-on. Integrating structured content patterns into Step 2 makes the flow cleaner.
   HOW: Rename to "Step 2: Scan AI Patterns" with subsections for prose and structured content.

### Structural Improvements (high impact, medium effort)

4. **Add error handling for edge cases** — addresses Error Handling (Absent)
   WHY: Without guidance, the skill will over-correct human text, try to humanize code, or fail on ambiguous content.
   HOW: Add a "When NOT to humanize" section: already-human text, code blocks, quoted speech, intentional stylistic choices.

5. **Add a complete before/after example for organized notes** — addresses Examples
   WHY: Structured notes are the user's most common output. The current before/after only shows 3 bullets.
   HOW: Add a 10-15 line example showing a full organized notes section (from youtube-transcriber output) before and after humanization.

6. **Add processing strategy for long documents** — addresses Scaling
   WHY: A 20-page policy document needs a different approach than 5 bullet points.
   HOW: Add guidance: "For documents over 2 pages, do a Tier 1 sweep first (fastest, highest impact), then Tier 2-4 in a second pass."

### Deep Investments (high impact, high effort)

7. **Create a `references/humanization-examples.md`** — addresses Examples
   WHY: The SKILL.md is lean (187 lines, good). But it could benefit from a comprehensive examples reference showing full-document transformations across all 6 modes.
   HOW: Create 6 examples (one per mode) showing 200-300 words of AI text transformed to human text, with annotations explaining each change.

8. **Add self-monitoring guidance** — addresses Scaling
   WHY: The skill should also apply to Gemini's OWN output, not just user-provided text. Currently it reads as a post-processing tool, but the user wants it to prevent AI slop proactively.
   HOW: Add a section: "When generating content (not just editing), apply the checklist BEFORE delivering output. The best humanization is never producing slop in the first place."

## Next Steps

- [ ] Apply quick wins 1-3 (fix reference file, add allowed-tools, merge steps)
- [ ] Apply structural improvements 4-6 (error handling, examples, scaling)
- [ ] Run `/skill-optimizer optimize humanizer` with the recommended evals
- [ ] Consider deep investments 7-8 after optimization confirms baseline quality
