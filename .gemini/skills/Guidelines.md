---
tags: [gemini-cli, skills, guidelines, reference]
updated: 2026-03-23
sources: 7 official Anthropic docs + 14 web sources
method: research-pipeline (local docs + web research + NotebookLM)
---

# Skill Creation Guidelines

Authoritative reference for creating, testing, and optimizing Gemini CLI skills. Use this document when running `/skill-creator` or building skills manually.

> **Skills are an open standard** maintained at [agentskills.io](https://agentskills.io), adopted by 30+ tools including Gemini CLI, Cursor, Gemini CLI, OpenAI Codex, GitHub Copilot, VS Code, JetBrains Junie, Goose, Roo Code, and others.

---

## 1. Directory Structure

```
skill-name/
├── SKILL.md              # Required — YAML frontmatter + markdown body
├── references/           # Optional — detailed docs loaded on demand
├── scripts/              # Optional — executable code (deterministic tasks)
├── examples/             # Optional — working code examples
└── assets/               # Optional — templates, images, fonts for output
```

**Naming**: kebab-case directories. Verb-first, active voice. Gerunds work for processes.
- Good: `condition-based-waiting`, `creating-skills`
- Bad: `skill-creation`, `async-test-helpers`

---

## 2. YAML Frontmatter

### Required Fields (Open Standard)

| Field | Constraints | Notes |
|-------|-------------|-------|
| `name` | Max 64 chars, lowercase + hyphens, must match directory name | Letters, numbers, hyphens only |
| `description` | Max 1024 chars | **The sole triggering mechanism** — most critical field |

### Optional Fields (Open Standard)

| Field | Purpose |
|-------|---------|
| `license` | License name or reference |
| `compatibility` | Max 500 chars, environment requirements |
| `metadata` | Arbitrary key-value map |

### Gemini CLI Extensions

| Field | Purpose | Example |
|-------|---------|---------|
| `argument-hint` | Autocomplete hint | `[issue-number]` |
| `disable-model-invocation` | Manual `/name` only, no auto-trigger | `true` |
| `user-invocable` | Hide from `/` menu | `false` |
| `model` | Override model | `sonnet`, `opus`, `haiku` |
| `effort` | Reasoning effort (Opus 4.6 only) | `low`, `medium`, `high`, `max` |
| `context` | Isolation mode | `fork` for subagent isolation |
| `agent` | Subagent type | `Explore`, `Plan`, `general-purpose` |
| `hooks` | Skill-scoped lifecycle hooks | JSON hooks config |
| `allowed-tools` | Restrict available tools | Space-delimited list |

### String Substitutions

| Variable | Resolves To |
|----------|-------------|
| `$ARGUMENTS` | All user arguments after `/skill-name` |
| `$ARGUMENTS[N]` or `$N` | Positional argument |
| `${GEMINI_SKILL_DIR}` | Skill directory path (replaces deprecated `{baseDir}`) |
| `${GEMINI_SESSION_ID}` | Current session ID |

### Dynamic Context Injection

`` !`<shell-command>` `` runs the command before skill content reaches Gemini. Output replaces the placeholder inline.

### Extended Thinking

Include "ultrathink" anywhere in skill content to enable extended thinking.

---

## 3. Description — The Most Critical Field

The description is the **sole mechanism** determining whether Gemini invokes a skill. Get this wrong and the skill never fires.

### Rules

1. **Third person** for skills: `"This skill should be used when the user asks to..."`
2. **Include specific trigger phrases** in quotes: `"create a hook"`, `"add a PreToolUse hook"`
3. **Be "pushy"** — Gemini tends to under-trigger. Cast a wide net.
4. **Include near-miss contexts** — when it should AND should not fire.
5. **NEVER summarize the workflow** in the description.

### Why Never Summarize Workflow

> "Testing revealed that when a description summarizes the skill's workflow, Gemini may follow the description instead of reading the full skill content. A description saying 'code review between tasks' caused Gemini to do ONE review, even though the skill's flowchart clearly showed TWO reviews."

The description tells Gemini **WHEN** to fire, not **WHAT** to do.

```yaml
# BAD: Summarizes workflow
description: Use when executing plans - dispatches subagent per task with code review between tasks

# GOOD: Just triggering conditions
description: Use when executing implementation plans with independent tasks in the current session
```

### Bad vs Good Examples

```yaml
# BAD
description: Provides guidance for working with hooks.  # Vague, no triggers
description: Load when user needs hook help.            # Wrong person
description: For async testing                          # Too abstract
description: I can help you with async tests            # First person

# GOOD
description: This skill should be used when the user asks to "create a hook",
  "add a PreToolUse hook", "validate tool use", "implement prompt-based hooks"
description: Use when tests have race conditions, timing dependencies,
  or pass/fail inconsistently
```

---

## 4. Progressive Disclosure

Three-level loading system to manage token budget:

| Level | When Loaded | Size Target | Content |
|-------|-------------|-------------|---------|
| **Metadata** | Always in context | ~100 words | `name` + `description` |
| **SKILL.md body** | When skill triggers | 1,500-2,000 words (max 5,000) | Core workflow, quick reference |
| **Bundled resources** | On demand | Unlimited | Detailed patterns, APIs, edge cases |

**Token budget**: 2% of context window allocated to skill descriptions (fallback: 16,000 chars).

### What Goes Where

**In SKILL.md (loaded on trigger):**
- Core concepts and overview
- Essential procedures and workflows
- Quick reference tables
- Pointers to references/scripts (so Gemini knows they exist)
- Most common use cases

**In references/ (loaded as needed):**
- Detailed patterns and advanced techniques
- Comprehensive API docs
- Migration guides, edge cases, troubleshooting
- Each file can be 2,000-5,000+ words

**In scripts/ (executed, not read into context):**
- Deterministic/repetitive tasks
- Validation utilities
- Code that would be rewritten every invocation

**In assets/ (used in output, never loaded):**
- Templates, images, fonts, boilerplate

### Key Rule

> "Information should live in either SKILL.md or references files, not both."

If reference files are large (>10k words), include grep search patterns in SKILL.md so Gemini can find what it needs.

---

## 5. Writing Style

### Imperative/Infinitive Form (Skills & Commands)

```
CORRECT: "Start by reading the configuration file."
INCORRECT: "You should start by reading the configuration file."
```

### Explain the Why, Not Rigid Rules

> "Try hard to explain the **why** behind everything. Today's LLMs are smart. If you find yourself writing ALWAYS or NEVER in all caps, that's a yellow flag — reframe and explain the reasoning."

### Word Limits

- SKILL.md body: **1,500-2,000 words** ideal, max 5,000
- Under **500 lines** for the full SKILL.md file
- Frequently-loaded skills: under **150-200 words**

### Token Efficiency Techniques

- Move details to `references/`
- Use cross-references instead of repeating content
- Compress examples — one excellent example beats many mediocre ones
- Eliminate redundancy

---

## 6. SKILL.md Body Template

```markdown
---
name: skill-name
description: This skill should be used when the user asks to "phrase 1",
  "phrase 2", "phrase 3". Provides [capability] for [context].
---

# Skill Name

## Overview
What is this? Core principle in 1-2 sentences.

## When to Use
Bullet list with SYMPTOMS and use cases. When NOT to use.

## Core Pattern
Before/after code comparison or workflow steps.

## Quick Reference
Table or bullets for scanning.

## Implementation
Inline code for simple patterns; link to references/ for heavy content.

## Common Mistakes
What goes wrong + fixes. Highest-signal content here.
```

---

## 7. Eval & Testing Workflow (/skill-creator)

### The TDD Rule

> "NO SKILL WITHOUT A FAILING TEST FIRST"

- **RED**: Run scenario WITHOUT skill. Document baseline behavior.
- **GREEN**: Write minimal skill addressing failures. Verify compliance.
- **REFACTOR**: Find rationalizations, add counters, re-test until bulletproof.

### /skill-creator Pipeline

1. **Draft skill** and create 2-3 realistic test prompts
2. **Save test cases** to `evals/evals.json`
3. **Spawn parallel runs**: with-skill AND baseline (without-skill) for each test
4. **Draft quantitative assertions** with descriptive names while runs execute
5. **Capture timing data** (`total_tokens`, `duration_ms`)
6. **Grade** each run → `grading.json`
7. **Aggregate** → `benchmark.json` (pass_rate, time, tokens — mean +/- stddev)
8. **Analyst pass** — surface patterns hidden by aggregate stats
9. **Launch viewer** using `generate_review.py` (never write custom HTML)
10. **Collect feedback** from user via `feedback.json`
11. **Iterate** — improve skill, rerun into `iteration-<N+1>/`

### Description Optimization (Automated)

1. Generate **20 eval queries** (8-10 should-trigger, 8-10 should-not-trigger)
2. Queries must be realistic (personal context, file paths, company names)
3. Should-not-trigger queries must be **near-misses**, not obviously irrelevant
4. Run `scripts.run_loop` — 60/40 train/test split, 3x per query, extended thinking
5. Select best by **test score** (not train) to avoid overfitting
6. Apply `best_description` to frontmatter

### Testing by Skill Type

| Type | Test With |
|------|-----------|
| Discipline-enforcing | Academic questions + pressure scenarios (time, sunk cost, authority) |
| Technique | Application scenarios + edge cases + missing info |
| Pattern | Recognition + application + counter-examples |
| Reference | Retrieval + application + gap testing |

---

## 8. Agent-Specific Guidelines

### Required Frontmatter
`name`, `description` (with `<example>` blocks), `model` (usually `inherit`), `color` (blue/cyan/green/yellow/magenta/red)

### Description Must Include Examples

```yaml
description: Use this agent when [conditions]. Examples:

<example>
Context: [Scenario]
user: "[Request]"
assistant: "[Response]"
<commentary>[Why this triggers]</commentary>
</example>
```

2-4 concrete examples covering proactive and reactive triggering.

### System Prompt
- Written in **second person** ("You are [role]...")
- 500-3,000 characters ideal, max 10,000
- Must include: role, responsibilities, step-by-step process, output format, quality standards, edge cases

### Agent Name Rules
3-50 characters, lowercase letters + numbers + hyphens. Must start/end with alphanumeric.

---

## 9. Anti-Patterns

| Anti-Pattern | Why It's Bad | Fix |
|-------------|-------------|-----|
| Vague description | Never triggers | Add specific trigger phrases in quotes |
| Workflow in description | Gemini follows description, skips body | Description = WHEN to fire, not WHAT to do |
| Everything in one file | Blows token budget, slow loading | Move details to `references/` |
| Second person in skills | Wrong convention | Use imperative form |
| Unreferenced resources | Gemini doesn't know they exist | Mention all bundled files in SKILL.md |
| Multi-language dilution | 5+ language examples | One excellent example beats many mediocre |
| ALWAYS/NEVER in caps | Rigid, overfitting | Explain the why instead |
| Force-loading with `@` | Consumes 200k+ context | Use skill name references |
| Skipping baseline test | Can't measure improvement | Always test without skill first |
| Overfitting iterations | Diminishing returns | Try different metaphors instead of fiddly constraints |
| Hardcoded paths | Breaks portability | Use `${GEMINI_SKILL_DIR}` |
| Narrative storytelling | Not reusable | State rules, not session history |

---

## 10. Validation & Distribution

### Validate Skills

```bash
skills-ref validate ./my-skill
```

Available at [github.com/agentskills/agentskills](https://github.com/agentskills/agentskills)

### Package as .skill File

```bash
# Via /skill-creator
scripts/package_skill.py
```

### Install via Plugin Marketplace

```bash
/plugin marketplace add anthropics/skills
/plugin install
```

---

## 11. Portability Checklist

When creating skills intended for multiple AI agents (Gemini, Codex, etc.):

- [ ] Use `${GEMINI_SKILL_DIR}` for paths (or make path-agnostic)
- [ ] Never hardcode absolute paths or `~/` shortcuts
- [ ] Standard YAML frontmatter only (`name`, `description`)
- [ ] Test on multiple systems
- [ ] Use portable bash/Python constructs in scripts
- [ ] One skill per purpose — no overlap with existing skills
- [ ] Check ~/Vault/Gemini-Skills/index.md before creating

---

## 12. Quick Checklist — Before Shipping a Skill

- [ ] `name` is kebab-case, matches directory name
- [ ] `description` is under 1024 chars, third person, includes trigger phrases
- [ ] Description does NOT summarize the workflow
- [ ] SKILL.md body is under 2,000 words (max 5,000)
- [ ] All bundled resources (references/, scripts/) are mentioned in SKILL.md
- [ ] No duplicate info between SKILL.md and references/
- [ ] Imperative form throughout (no "you should")
- [ ] Explains WHY, not just WHAT
- [ ] Tested with /skill-creator eval pipeline (baseline + with-skill)
- [ ] Description optimized with train/test split
- [ ] No overlap with existing skills (checked index.md)
- [ ] Synced to ~/Vault/Gemini-Skills/ AND ~/apps/skills-bucket/

---

## Sources

### Official Anthropic Documentation
- [Agent Skills Open Standard](https://agentskills.io) — specification adopted by 30+ tools
- [Agent Skills Specification](https://agentskills.io/specification) — frontmatter fields and format
- [Gemini CLI Skills Docs](https://code.claude.com/docs/en/skills) — official Gemini CLI guide
- [Anthropic Skills Repository](https://github.com/anthropics/skills) — official skills collection
- [Gemini Plugins Official](https://github.com/anthropics/claude-plugins-official) — plugin-dev, skill-creator, figma, etc.

### Local Sources (read in full)
- `official-skill-creator/skill.md` — eval pipeline, description optimization, iteration workflow
- `plugin-skill-development/skill.md` — progressive disclosure, writing style, resource organization
- `plugin-structure/skill.md` — plugin directory layout, auto-discovery, namespacing
- `plugin-command-development/skill.md` — commands as agent instructions, dynamic arguments
- `plugin-agent-development/skill.md` — agent frontmatter, example blocks, system prompts
- `plugin-hook-development/skill.md` — prompt-based hooks, security requirements
- `sp-writing-skills/skill.md` — TDD for skills, description traps, token efficiency

### Community Resources
- [Gemini Skills Deep Dive](https://leehanchung.github.io/blogs/2025/10/26/gemini-skills-deep-dive/) — first principles analysis
- [Progressive Disclosure for AI Tools](https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/)
- [Gemini CLI Customization Guide](https://alexop.dev/posts/gemini-cli-customization-guide-claudemd-skills-subagents/)
- [awesome-gemini-skills](https://github.com/travisvn/awesome-gemini-skills) — curated skill list
- [SkillsMP Marketplace](https://skillsmp.com/) — community skill distribution
