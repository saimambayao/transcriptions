---
name: prompter
description: |
  Intelligent prompt refinement that works in any project. Analyzes raw prompts, audits codebase
  context dynamically, extracts intent, and produces structured redescriptions for clarity before
  execution. Prevents incorrect implementations from ambiguous or incomplete prompts.
  Use when: entering complex prompts, phrasing multi-step tasks, disambiguating requirements,
  confirming system understanding before action, or when any other skill says "invoke /prompter first".
  Triggers on: "prompter", "refine this prompt", "clarify my intent", "what do I mean",
  "rephrase this", "help me prompt", "prompt check".
argument-hint: "<raw prompt to refine>"
allowed-tools:
  - Read
  - Glob
  - Grep
  - Agent
---

# Prompter — Intelligent Prompt Refinement

Ensures prompts are clear, context-aware, and accurately capture intent before execution.
Works in any project by dynamically detecting the stack, structure, and conventions.

## Phase 1: Prompt Capture & Triage

Accept the raw prompt and **triage** it before doing full analysis:

### Fast-Path Check

If the prompt already contains **4+ of these signals**, it's already well-structured — skip to Phase 5 (Confirm):
- Explicit task statement ("Add X to Y", "Fix the Z bug in W")
- Named files or modules
- Specific constraints or requirements listed
- Clear success criteria
- Defined scope (in/out)

If fast-path triggers, say:
```
Your prompt is already well-structured. Proceeding as-is.
[Show the prompt back for confirmation]
```

### Standard Path

If the prompt needs refinement:
1. Identify key components (task, constraints, context)
2. Extract implicit requirements (what's assumed but not stated)
3. Flag ambiguities (words that could mean multiple things)

## Phase 2: Dynamic Context Audit

**Do NOT hardcode project knowledge.** Instead, dynamically discover the project:

### Step 2a: Detect Project Type

Use Glob and Grep to identify the project:

```
Check for these patterns (in parallel where possible):
- package.json → Node/JS project → read for framework (React, Vue, Next, etc.)
- requirements.txt / pyproject.toml / Pipfile → Python project → read for framework (Django, Flask, FastAPI)
- Cargo.toml → Rust project
- go.mod → Go project
- *.csproj → .NET project
- CLAUDE.md → read for project-specific conventions
- .claude/skills/ → check for project-level skills that might be relevant
```

### Step 2b: Discover Structure

Based on project type, scan for:
- **Directory structure**: top-level folders (src/, frontend/, backend/, apps/, lib/, etc.)
- **Module organization**: how features/domains are grouped
- **Existing patterns**: similar components, hooks, utilities, API routes near the task area
- **Test structure**: where tests live, what framework (jest, pytest, vitest, etc.)

### Step 2c: Read CLAUDE.md

If a CLAUDE.md exists (project-level or global), extract:
- Code conventions
- Architectural patterns
- Naming conventions
- Constraints ("no purple", "icons not emojis", etc.)

### Step 2d: Build Context Summary

Compile what you found into a brief internal context (not shown to user yet):
- Stack: [detected]
- Structure: [key directories]
- Conventions: [from CLAUDE.md]
- Relevant existing code: [files/patterns near the task area]

## Phase 3: Intent Extraction

From the raw prompt + discovered context, extract:

- **Primary goal** — what the user actually wants to accomplish
- **Success criteria** — how we'll know it's done
- **Constraints** — explicit and implicit (from CLAUDE.md, conventions, etc.)
- **Scope** — what's in and what's out
- **Ambiguities** — anything that could be interpreted multiple ways (flag these)

### Change Discipline Gate

Before proceeding to redescription, apply the gate from
[references/change-discipline-gate.md](references/change-discipline-gate.md):

1. Parse the user's action words — "remove," "rewrite," "fix," "add," "check" — and match
   them to their exact definitions. Do not interpret "remove" as "replace" or "rewrite" as
   "restructure from scratch."
2. List what the user asked for. List what they did NOT ask for. Include the second list
   in the Scope section as **Out of Scope**.
3. If the task is "rewrite" or "review": list the specific problems to fix BEFORE proposing
   any changes. Present the problem list to the user for confirmation.

### Behavioral Rules Check

Read [references/behavioral-rules.md](references/behavioral-rules.md) and identify which
rule categories apply to this task:

- Does the task involve **editing existing content**? → Apply editing rules (remove=delete, rewrite=fix broken)
- Does the task involve **BARMM content**? → Flag: read error log, verify BOL/BAA/ministry names, no "Islamic governance"
- Is the output an **external document**? → Flag: pre-delivery scan required before delivery
- Does the task involve **PDF generation**? → Flag: visual verification loop required
- Does the task involve **legal work**? → Flag: 7-step pipeline, verify-references before citation
- Does the task involve **citations**? → Flag: verify BAA/BOL numbers, no guidebooks as sources

Include all applicable rules in the **Constraints** section of the redescription.

## Phase 4: Redescription

Generate a concise, structured redescription:

```markdown
## Task Intent
[One sentence: What to accomplish]

## Project Context
- **Stack**: [detected stack — e.g., React 19 + Django REST, Next.js + Prisma, etc.]
- **Module/Area**: [which part of the codebase this touches]
- **User Type**: [who this feature is for, if applicable]

## Technical Context
- **Files involved**: [specific files or patterns discovered in Phase 2]
- **Related code**: [existing components, hooks, utilities, or API endpoints nearby]
- **Conventions**: [relevant rules from CLAUDE.md or detected patterns]

## Primary Requirements
1. [Specific requirement]
2. [Specific requirement]

## Constraints
- [Constraint from CLAUDE.md or conventions]
- [Constraint from the prompt itself]

## Success Criteria
- [How will we know it's done?]

## Scope
- **In Scope**: [What's included]
- **Out of Scope**: [What's explicitly excluded]
```

### Redescription Rules

- **Shorter than the raw prompt** while preserving all requirements
- **No invented requirements** — only what was stated or directly implied
- **Flag ambiguities** with [?] markers: "Amendment status workflow [?draft→review→adopted or draft→vote→adopted?]"
- **Reference real files** discovered in Phase 2, not hypothetical paths
- **Use the project's terminology** — if the codebase calls them "modules", don't say "features"

## Phase 5: Confirmation

Present the redescription and ask:

```
Does this capture your intent?

1. Yes, proceed
2. No, adjust [specify what]
3. Let me rephrase entirely
```

**If the user says "Yes, proceed":** The refined prompt is now the authoritative task description. Other skills or Claude Code itself should use this redescription as the task spec.

**If the user says "No, adjust X":** Apply the adjustment, re-present, and confirm again.

**If the user says "Let me rephrase":** Go back to Phase 1 with the new prompt.

## Error Handling

| Situation | Response |
|-----------|----------|
| Prompt is already clear (fast-path) | Show it back, confirm, proceed |
| Can't detect project type | Ask the user: "What stack/framework is this project?" |
| No CLAUDE.md found | Proceed without conventions — note this in the redescription |
| Prompt is too vague to extract intent | Ask 1-2 targeted clarifying questions before Phase 3 |
| User rejects redescription 2+ times | Ask: "What am I misunderstanding? Can you give me an example of what you want?" |
| Prompt spans multiple unrelated tasks | Split into separate redescriptions, confirm each independently |

## Scaling by Complexity

| Prompt Complexity | Approach |
|-------------------|----------|
| **Simple** (single file, clear task) | Fast-path or minimal redescription — don't over-engineer |
| **Medium** (multi-file, one feature) | Full Phase 1-5 workflow |
| **Complex** (cross-module, architectural) | Full workflow + suggest breaking into subtasks |
| **Ambiguous** (vague, open-ended) | Ask clarifying questions first, then workflow |

## Phase 6: Save to Vault

After the user confirms the redescription (Phase 5 → "Yes, proceed"), save the output:

1. **Generate filename**: `YYMMDD-HHMM-short-slug.md` (e.g., `260326-1430-oobc-v3-review.md`)
2. **Save to**: `~/Vault/Prompts/YYMMDD-HHMM-short-slug.md`
3. **Format**: Include the full redescription with a YAML frontmatter header:
   ```yaml
   ---
   date: YYYY-MM-DD
   tags: [prompt, <project-tag>]
   project: <project or repo name>
   status: confirmed
   ---
   ```
4. **Update index**: Append a `- [[YYMMDD-HHMM-short-slug]] — one-line description` entry to `~/Vault/Prompts/index.md` under the `## Prompts` heading.

If the user says "No, adjust" or "Let me rephrase", do NOT save until a confirmed version exists.

## What This Skill Does NOT Do

- Does not execute the task — it only refines the prompt
- Does not write code — it produces a structured task spec
- Does not make architectural decisions — it surfaces them for the user to decide
- Does not replace project-specific skills — it feeds into them (e.g., /devwork, /tdd)
