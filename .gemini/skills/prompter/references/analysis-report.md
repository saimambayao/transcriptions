# Skill Analysis Report: prompter

**Analyzed:** 2026-03-23
**Lines:** 464
**Tier:** 2 — Usable but not portable
**References:** none

## Score Card

| Dimension                    | Rating   | Key Finding                                              |
|------------------------------|----------|----------------------------------------------------------|
| YAML Frontmatter             | Weak     | Missing `allowed-tools` and `argument-hint`; description hardcoded to e-Bangsamoro |
| Phase Architecture           | Adequate | 6 phases well-named, but Phase 6 (Ralph Loop) is 60% of the skill |
| Output Specification         | Strong   | Full markdown template in Phase 4, detailed ralph loop template in Phase 6 |
| Constraint Density           | Adequate | Good decision criteria for ralph loop, but core Phases 1-5 rely on hardcoding |
| Error Handling               | Absent   | No handling for: already-clear prompts, unknown project type, missing skills |
| Examples & Demonstration     | Strong   | Two complete end-to-end examples (bill amendments + TypeScript types) |
| Scaling & Complexity Mgmt    | Adequate | Ralph loop has complexity table, but Phases 1-5 treat all prompts the same |

## Detailed Findings

**YAML Frontmatter (Weak):** No `allowed-tools` field — skill needs Read, Glob, Grep at minimum for codebase context audits. No `argument-hint`. Description is hardcoded to "React 19, Vite 6.0+, TypeScript, Django REST Framework" — won't trigger correctly in non-e-Bangsamoro projects.

**Phase Architecture (Adequate):** Phases 1-5 (Capture → Audit → Extract → Redescribe → Confirm) are clean and logical. Phase 6 (Ralph Loop Construction) is 170 lines — 37% of the entire skill — and is functionally a separate orchestration concern. It couples the prompter to `ralph-loop` skill existence.

**Output Specification (Strong):** Phase 4 provides a complete 7-section markdown template (Task Intent, Module Context, Tech Context, Requirements, Constraints, Success Criteria, Scope). Phase 6 provides a complete ralph loop prompt template. Both are concrete and reproducible.

**Constraint Density (Adequate):** Module architecture table (line 281-289) and user types table (line 307-315) provide specific constraints. Key conventions listed (line 299-305). But all of these are e-Bangsamoro-specific — the skill has zero generic constraints.

**Error Handling (Absent):** No fast-path for already-clear prompts. No handling for unknown project structures. No fallback if ralph-loop skill isn't installed. No guidance on what to do if user rejects redescription multiple times.

**Examples (Strong):** Two complete examples showing raw prompt → redescription → confirmation → ralph loop. Both are realistic and demonstrate the full workflow.

**Scaling (Adequate):** Ralph loop has a 4-tier complexity table (Simple/Medium/Complex/Large → iterations). But core Phase 1-5 workflow applies identical treatment to "fix a typo" and "rebuild the entire module."

## Recommended Evals

1. **Does the redescription contain all 7 template sections?** — Critical, Low gaming risk
2. **Is the redescription shorter than the raw prompt while preserving all requirements?** — Important, Medium gaming risk
3. **Does the skill ask for confirmation before proceeding?** — Critical, Low gaming risk
4. **Does Phase 2 reference actual files/patterns from the current project?** — Critical, Medium gaming risk
5. **Does the skill correctly identify when a prompt is already clear enough?** — Important, High gaming risk

## Optimization Recommendations

### Quick Wins
1. Add `allowed-tools: Read, Glob, Grep, Agent` to YAML
2. Add `argument-hint` field
3. Remove stack-specific language from description

### Structural Improvements
4. Make Phase 2 dynamic — scan project structure instead of hardcoding
5. Add fast-path at Phase 1 for already-structured prompts
6. Extract Ralph Loop into conditional section or reference file

### Deep Investments
7. Project profile system — auto-generate context on first run
8. Add error handling for all failure modes

## Next Steps

- [x] Apply analysis
- [ ] Rebuild as global skill with dynamic Phase 2
- [ ] Extract Ralph Loop to references/ or separate skill
- [ ] Add error handling and fast-path
