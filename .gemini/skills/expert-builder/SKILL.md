---
name: expert-builder
description: |
  Build fully trained AI experts from NotebookLM research. Creates a permanent Gemini CLI
  skill grounded in real frameworks, methods, and domain knowledge — not generic instructions.
  Use when user says "expert builder", "build a expert", "create a consultant", "build an
  AI expert", "train an AI", "create a specialist", "build me a [role]", "I want an AI that
  thinks like a [profession]", or wants to create any kind of specialized AI assistant
  (consultant, writer, strategist, analyst, teacher, advisor, chef, etc.).
allowed-tools: Read, Glob, Grep, Bash, Write, Agent
---

# Persona Builder

Build the brain in NotebookLM (free). Give it a body as a Gemini CLI skill (permanent).

## Process

### Step 1: Define the Persona

Ask the user:
- **What role?** (business consultant, journalist, finance advisor, etc.)
- **What should it know?** (frameworks, methods, domain knowledge)
- **How should it behave?** (communication style, output format, thinking approach)
- **What's the skill name?** (used as the slash command, e.g., `/consultant`)

### Step 2: Build the Knowledge Base (NotebookLM — FREE)

Create a NotebookLM notebook and run deep research:

```bash
notebooklm create "Persona: [Role Name]"
notebooklm source add-research "[core frameworks, methods, and knowledge domains for this role]" --mode deep --import-all
```

If the user has existing sources (PDFs, URLs, books), add those too:
```bash
notebooklm source add "./path/to/source.pdf"
notebooklm source add "https://relevant-url.com"
```

Then synthesize the knowledge base:
```bash
notebooklm ask "Create a comprehensive knowledge base for an elite [role]. Include: core frameworks and when to use each, problem-solving methodology, communication style and output standards, decision-making heuristics, and common pitfalls to avoid."
```

Save the response to a temp file.

### Step 3: Review with User

Present the synthesized knowledge base to the user. Ask:
- Is anything missing from the knowledge domains?
- Should the expert emphasize certain frameworks over others?
- Any specific behavior rules or output preferences?

Iterate until the user approves the knowledge base.

### Step 4: Create the Skill

Create the skill directory and SKILL.md at `~/.gemini/skills/[expert-name]/SKILL.md`.

The generated skill should include:

```markdown
---
name: [expert-name]
description: |
  [Role description and trigger phrases]
allowed-tools: Read, Glob, Grep, Bash, Write
---

# [Role Name]

## Identity
[Who this expert is and how it thinks]

## Core Frameworks
[The specific frameworks from the research, with when to apply each]

## Problem-Solving Method
[Step-by-step approach this expert uses to break down problems]

## Communication Style
[How it speaks, what format it uses, level of formality]

## Output Guide
[What deliverables look like — structure, depth, format]

## Behavior Rules
[What it always does, what it never does, how it handles uncertainty]
```

The skill content must come from the NotebookLM research — not from generic knowledge. Every framework, method, and rule should trace back to the sources.

### Step 5: Install and Test

Confirm the skill is saved. Then do a quick test:
- Ask the expert a question in its domain
- Verify it applies the frameworks from the research automatically
- Verify the communication style matches expectations

### Step 6: Save to Vault

Create a research note at `~/Vault/research/yymmdd-expert-[name].md` documenting:
- What expert was built
- What sources/research went into it
- The skill location
- How to invoke it

## Examples

**User says:** "Build me a business consultant"
- NotebookLM researches: Porter's Five Forces, BCG Matrix, MECE thinking, financial literacy, client communication
- Skill created at `~/.gemini/skills/consultant/SKILL.md`
- User can now type `/consultant` and get framework-grounded analysis

**User says:** "I want an AI that writes like a seasoned journalist"
- NotebookLM researches: AP style, inverted pyramid, source attribution, narrative structure, editing principles
- Skill created at `~/.gemini/skills/journalist/SKILL.md`

**User says:** "Create a Bangsamoro policy analyst"
- NotebookLM researches: BOL, BDP 2023-2028, parliamentary procedures, fiscal governance, BARMM institutional framework
- Skill created at `~/.gemini/skills/policy-analyst/SKILL.md`
