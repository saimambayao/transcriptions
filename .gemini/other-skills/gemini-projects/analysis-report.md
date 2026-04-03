# Skill Analysis Report: gemini-projects

**Analyzed:** 2026-03-23 (round 2, post-optimization)
**Lines:** 411 (SKILL.md) + 524 (3 references) = 935 total
**Tier:** 1 — Production Ready
**References:** 3 files (evaluation-criteria.md, autoresearch-methodology.md, improve-examples.md)
**Previous Tier:** 2 — Usable (pre-optimization)

## Score Card (Post-Optimization)

| Dimension                    | Before   | After    | Key Change                                            |
|------------------------------|----------|----------|-------------------------------------------------------|
| YAML Frontmatter             | Adequate | Strong   | Added allowed-tools, argument-hint, 3 new triggers    |
| Phase Architecture           | Strong   | Strong   | Added Mode Dependencies table with explicit data flow  |
| Output Specification         | Adequate | Strong   | improve-examples.md: 3 complete before/after examples  |
| Constraint Density           | Strong   | Strong   | CREATE mode now has 5 specific constraints              |
| Error Handling               | Weak     | Adequate | 6-row error table covering real-world failures          |
| Examples & Demonstration     | Adequate | Strong   | 3 domain-specific transformation examples               |
| Scaling & Complexity Mgmt    | Weak     | Adequate | Simple/Medium/Complex table with approaches              |

## Detailed Findings

### YAML Frontmatter (Adequate)
- `name`: present, matches directory ✓
- `description`: 13 trigger phrases covering core use cases ✓
- `allowed-tools`: ABSENT — skill uses Read, Write, Edit, Glob, Grep, WebSearch, Agent
- `argument-hint`: ABSENT — skill accepts mode arguments (AUDIT, IMPROVE, etc.)
- Missing trigger: "optimize project instructions" despite Mode 6 addition
- Missing trigger: "autoresearch" despite OPTIMIZE mode's methodology

### Phase Architecture (Strong)
- 6 named modes with numbered steps (lines 44-270) ✓
- Self-Review Protocol as quality gate (lines 272-319) ✓
- Workflow section defines natural progression (lines 322-330) ✓
- Gaps: No explicit actor roles (evaluator vs generator). No formal handoff contracts
  between modes — what AUDIT outputs that IMPROVE consumes is implicit. CREATE mode
  is the only one with an information-gathering step (Step 1: "Ask the user").

### Output Specification (Adequate)
- AUDIT: Full table template (lines 63-82) ✓
- DOCUMENT: README.md + attachment-list.md templates (lines 182-228) ✓
- IMPROVE: "copy-paste-ready format" — no template shown
- CREATE: "structured format" — completely vague
- SKILL: References skill format but no conversion example
- OPTIMIZE: Describes report contents, no template

### Constraint Density (Strong)
- Self-Review: "Line count > 50", "Word count within 20%", "Has XML tags" (lines 278-315) ✓
- IMPROVE: "under 800 words" target ✓
- Anti-pattern catalog: 7 patterns with BAD/WHY/FIX ✓
- Weak spot: CREATE mode has zero specific constraints (line 126: "structured format")
- OPTIMIZE mode says "5-10 evals" and "3-5 test prompts" — good bounds

### Error Handling (Weak)
- Single line of error guidance (line 319): "Fix it immediately"
- No error table mapping failure types to recovery actions
- Known real-world failures NOT addressed:
  - OneDrive cloud-only placeholders (pandoc can't unpack)
  - User pastes partial/truncated instructions
  - Screenshots unreadable or ambiguous
  - File extraction fails
  - User provides instructions in non-English
- No bounded retries for OPTIMIZE mode
- No escalation path when self-review finds unfixable issues

### Examples & Demonstration (Adequate)
- References: 7 anti-pattern examples with BAD/WHY/FIX structure ✓
- OPTIMIZE: 3 example evals for bill drafter ✓
- DOCUMENT: Template examples ✓
- Missing: No before/after example for IMPROVE mode (the core mode)
- Missing: No CREATE output example
- Missing: No SKILL conversion example (project instructions → SKILL.md)
- Missing: No good-vs-bad output comparison for any mode

### Scaling & Complexity Management (Weak)
- Common Patterns section differentiates by project type ✓
- Self-Review adapts checks by output type ✓
- No scaling table for instruction length (100 vs 2000 words)
- No guidance for knowledge base size (0 vs 50 files)
- No time/token estimates for different complexity levels
- OPTIMIZE mode has no iteration cost limits or complexity-based bounds

## Recommended Evals

### Eval 1: IMPROVE Output Self-Sufficiency
**Question:** Can someone recreate the Gemini Project from improved-instructions.md alone?
**Tests dimension:** Output Specification / Constraint Density
**Why this matters:** User's #1 complaint was stripped/truncated outputs that couldn't recreate the project.
**Risk of gaming:** Medium
**Priority:** Critical

PASS: Contains role definition, output template with field descriptions, file inventory, all domain rules
FAIL: Missing sections, bare headers without guidance, compressed agency lists

### Eval 2: DOCUMENT Verbatim Preservation
**Question:** Does original-instructions.md contain complete, untruncated text?
**Tests dimension:** Constraint Density (Self-Review enforcement)
**Why this matters:** 3 of 6 projects had truncated originals in the prior session.
**Risk of gaming:** Low
**Priority:** Critical

PASS: Line count within 20% of source, no placeholder text, all section headers present
FAIL: Summarized, truncated, or contains "[... rest follows ...]"

### Eval 3: SKILL Functional Distinction
**Question:** Is the generated skill functionally distinct from existing skills?
**Tests dimension:** Phase Architecture (SKILL conversion logic)
**Why this matters:** Bill-drafter and resolution-drafter were initially merged incorrectly.
**Risk of gaming:** Medium
**Priority:** Important

PASS: Explicitly references which skills it differs from, adapts file refs to filesystem, adds composition
FAIL: Duplicates an existing skill's triggers or core functionality

### Eval 4: AUDIT Score Justification
**Question:** Does every audit score have a specific finding (not just a generic adjective)?
**Tests dimension:** Examples & Demonstration
**Why this matters:** Vague notes like "adequate" don't help the user improve.
**Risk of gaming:** Low
**Priority:** Important

PASS: Each note references a specific part of the instructions
FAIL: Generic notes like "needs improvement" without specifics

### Eval 5: Error Recovery on Partial Input
**Question:** When given incomplete instructions, does the skill ask for clarification?
**Tests dimension:** Error Handling
**Why this matters:** Real users paste fragments or provide screenshots.
**Risk of gaming:** High
**Priority:** Nice-to-have

PASS: Identifies what's missing and asks targeted questions
FAIL: Silently fills in assumed content

## Optimization Recommendations

### Quick Wins (high impact, low effort)
1. **Add `allowed-tools` to frontmatter** — D1
   WHY: Missing tool declarations prevent proper sandboxing
   HOW: Add `allowed-tools: [Read, Write, Edit, Glob, Grep, WebSearch, Agent]`

2. **Add "optimize" trigger to description** — D1
   WHY: Mode 6 exists but description doesn't trigger on "optimize project"
   HOW: Add "optimize project instructions", "autoresearch project" to triggers

3. **Add error table** — D5
   WHY: OneDrive failures, truncated pastes, unreadable screenshots all occurred
   HOW: 6-row error table after Self-Review section

### Structural Improvements (high impact, medium effort)
4. **Add IMPROVE mode before/after example** — D3, D6
   WHY: IMPROVE is the most-used mode with no concrete transformation example
   HOW: 30-line before/after in references/improve-examples.md

5. **Define inter-mode handoff contracts** — D2
   WHY: What AUDIT outputs that IMPROVE consumes is implicit
   HOW: Add "Mode Dependencies" subsection with explicit data flow

6. **Add CREATE mode constraints** — D4
   WHY: CREATE has weakest constraints — "structured format" is insufficient
   HOW: Add word limit, example count, file inventory requirements

### Deep Investments (high impact, high effort)
7. **Add complexity scaling table** — D7
   WHY: 100-word project needs different treatment than 2000-word project
   HOW: Simple/Medium/Complex table with different mode recommendations

8. **Add references/improve-examples.md** — D6
   WHY: 2-3 complete before/after transformations would anchor the IMPROVE mode
   HOW: Legislative, research, content creation examples (50 lines each)

## Next Steps

- [ ] Apply quick wins (1-3) — immediate frontmatter + error table fixes
- [ ] Create references/improve-examples.md (recommendation 4+8 combined)
- [ ] Add CREATE mode constraints and inter-mode handoffs (5+6)
- [ ] Add complexity scaling table (7)
- [ ] Re-analyze after changes to verify tier improvement
