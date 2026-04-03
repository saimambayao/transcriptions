---
name: gemini-projects
description: |
  Audit, improve, and create Gemini Project instructions, then generate parallel Gemini CLI
  skills. Use this skill whenever the user mentions "claude project", "claude projects",
  "project instructions", "improve project", "audit project", "create project",
  "project designer", "optimize project instructions", "review my project",
  "project to skill", "convert project to skill", "update my project",
  "autoresearch project", "optimize project", "project evals",
  or wants to work with Gemini Projects in any way — reviewing them, improving their
  instructions, creating new ones, converting them into Gemini CLI skills, or optimizing
  instructions through automated evaluation loops.
  Also trigger when the user pastes a block of text that looks like Gemini project
  instructions (role definitions, behavioral rules, output format specs) and asks for
  feedback or improvement. This skill bridges the gap between Gemini's web-based
  Projects and Gemini CLI's skill system.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Agent
argument-hint: "[AUDIT|IMPROVE|CREATE|SKILL|DOCUMENT|OPTIMIZE] <project instructions or context>"
---

# Gemini Projects

Audit, improve, create, and convert Gemini Project instructions. Bridges Gemini Projects
(web interface) with Gemini CLI skills (terminal).

## Important Context

Gemini Projects are web-only workspaces. There is no API to create or modify them
programmatically. This skill works with pasted instructions and generates text output
that the user copies back into gemini.google.com manually.

Key constraints of Gemini Projects:
- **200K context window** on paid plans (Pro, Max, Team, Enterprise)
- **RAG auto-activates** when knowledge base exceeds context — Claude retrieves chunks, not full files
- **Context is NOT shared across chats** — only knowledge base + instructions carry over
- **Each chat starts fresh** — instructions must be self-contained
- **Instructions compete with knowledge base for context space** — shorter is better

Official documentation:
- What are Projects: support.claude.com/en/articles/9517075-what-are-projects
- Managing Projects: support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- Project examples: support.claude.com/en/articles/9529781-examples-of-projects-you-can-create

## Modes

The user may request a specific mode or describe what they want. Infer the right mode from context.

### Mode 1: AUDIT

Analyze existing project instructions the user has pasted.

**Steps:**

1. Read `references/evaluation-criteria.md` for the scoring rubric and anti-pattern catalog
2. Score the instructions on five dimensions (1-5 each):
   - **Clarity** — Could someone unfamiliar follow these?
   - **Completeness** — Role, task, format, constraints, edge cases, examples?
   - **Structure** — Organized with hierarchy, XML tags, logical flow?
   - **Effectiveness** — Leverages Claude's strengths (examples, roles, context)?
   - **RAG-Readiness** — Works when Claude only retrieves chunks?
3. Calculate overall score (average of 5 dimensions, out of 5)
4. Identify specific anti-patterns from the catalog
5. List concrete improvement recommendations, prioritized by impact

**Output format:**

```
## Project Audit: [Project Name]

### Scores
| Dimension | Score | Notes |
|-----------|-------|-------|
| Clarity | X/5 | ... |
| Completeness | X/5 | ... |
| Structure | X/5 | ... |
| Effectiveness | X/5 | ... |
| RAG-Readiness | X/5 | ... |
| **Overall** | **X/5** | |

### Anti-Patterns Found
1. [Pattern name] — [where it appears] — [why it's a problem]

### Recommendations (by priority)
1. [Highest impact change]
2. ...
```

### Mode 2: IMPROVE

Rewrite project instructions based on audit findings.

**Steps:**

1. If no audit exists yet, run AUDIT first
2. Rewrite the instructions applying these Anthropic best practices:
   - **Clear role definition** — specific domain expert, not "helpful assistant"
   - **Positive framing** — tell Gemini what TO do, not what to avoid
   - **Context for instructions** — explain WHY each rule matters
   - **Examples** — include 2-3 output examples using `<example>` tags
   - **XML structure** — use tags to separate instructions, context, format specs
   - **Concise** — aim for under 800 words; every token competes with knowledge base
   - **RAG-aware** — describe uploaded files and their purposes so Gemini knows what to search for
   - **Self-contained** — each chat starts fresh, so instructions can't assume prior context
3. Present the improved instructions in a copy-paste-ready format
4. Show a before/after comparison of key changes

**Key rewriting principles (from Anthropic docs):**
- Replace "NEVER do X" with "Do Y instead" — positive framing is more effective
- Replace ALL-CAPS directives with normal language — Claude 4.6 is responsive enough
- Add WHY behind each instruction — Claude generalizes better from explanations
- Include examples of desired output — "one of the most reliable ways to steer Claude"
- Use XML tags for structure — reduces misinterpretation in complex prompts

Read `references/improve-examples.md` for 3 complete before/after transformation examples (legislative, research, content creation).

### Mode 3: CREATE

Design a new Gemini Project from scratch.

**Steps:**

1. Ask the user what the project should accomplish
2. Identify the three components (from official docs):
   - **Knowledge Base** — what reference materials to upload
   - **Instructions** — the system prompt
   - **Expected Artifacts** — what outputs users will create in chats
3. Generate:
   - Project name and description
   - Complete project instructions (following all best practices from Mode 2)
   - Recommended file inventory with descriptions of what each file provides
   - 3-5 example prompts users would type in the project
4. Present everything in a structured format

**CREATE constraints:**
- Instructions must be under 800 words — every token competes with knowledge base
- Include 2-3 concrete output examples using `<example>` tags
- Knowledge base inventory must list each file with type, purpose, and what to search for
- Role definition must be a specific domain expert, not "helpful assistant"
- Include at least one edge case instruction (what to do when information isn't available)

### Mode 4: SKILL

Convert project instructions into a Gemini CLI skill.

Gemini CLI skills differ from Gemini Projects in important ways. The conversion must adapt for:

| Gemini Projects | Gemini CLI Skills |
|---|---|
| 200K context window | 1M context window |
| RAG for large knowledge bases | Direct filesystem access to all files |
| Web-only, manual interaction | Terminal + IDE, tool access |
| Instructions are the only customization | Skills can reference other skills, use tools, run scripts |
| Each chat is isolated | Persistent session with full conversation history |

**Steps:**

1. Extract the core capability from the project instructions
2. Identify which parts translate directly vs need adaptation:
   - File references → filesystem `Read` calls
   - "Search the knowledge base" → `Grep`/`Glob` commands
   - Output format rules → preserve as-is
   - Domain expertise → preserve as-is
   - Anti-patterns that were project-specific → remove
3. Check for existing Gemini CLI skills that overlap (scan `~/.gemini/skills/`)
4. Write the skill with proper frontmatter:
   - `name`: skill identifier
   - `description`: triggering description (specific, slightly pushy for reliable activation)
5. Add composition hints — which other skills to invoke alongside
6. Save to `~/.gemini/skills/[skill-name]/SKILL.md`

### Mode 5: DOCUMENT

Save project documentation to the Obsidian vault as a **subfolder** (one project = one subfolder).

**Steps:**

1. Create `~/Vault/Claude-Projects/[project-name]/` subfolder
2. Generate these standard files:

| File | Purpose | Required |
|------|---------|----------|
| `README.md` | Project overview, audit results, purpose, notes | Always |
| `original-instructions.md` | Original project instructions — COMPLETE, VERBATIM, NEVER TRUNCATED | Always |
| `improved-instructions.md` | Rewritten instructions (copy-paste ready) | After IMPROVE |
| `attachment-list.md` | Inventory of all files uploaded to the project | Always |
| Other reference files (e.g., `barmm-agencies.md`) | Extracted reference data from the instructions | When applicable |

**Critical rule for `original-instructions.md`:** The original instructions must be preserved in full — every word, every section, every detail. The purpose of this file is to enable the user to recreate the gemini.google.com Project from scratch. A truncated or summarized version is useless for that purpose. If the instructions are 4000 words, the file is 4000 words. No summaries, no "[... rest follows ...]", no "see above for details." Complete and verbatim.

3. Use Obsidian conventions:
   - `[[double bracket links]]` for cross-references
   - Frontmatter with metadata
   - Tags for categorization

**README.md template:**

```markdown
---
project: [Project Name]
platform: gemini.google.com
status: [active/archived/needs-update]
last_reviewed: [YYYY-MM-DD]
claude_code_skill: [skill name or "none"]
tags: [relevant tags]
---

# [Project Name]

**Description:** [one-line description]
**Created:** [date if known]
**Last Updated:** [date if known]

## Purpose
[What this project does and who it serves]

## Audit Results
[If audit was performed, include scores and key findings]

## Linked Skill
[If a Gemini CLI skill was created, link it: [[skill-name]]]

## Notes
[Any additional context about this project]
```

**attachment-list.md template:**

```markdown
---
type: attachment-list
project: [Project Name]
captured: [YYYY-MM-DD]
storage_used: [X%]
---

# Project Attachments — [Project Name]

| # | Filename | Type | Lines | Category |
|---|----------|------|-------|----------|
| 1 | [filename] | [PDF/TEXT/HTML/DOCX] | [lines] | [category] |
```

The attachment list captures the file inventory from the gemini.google.com Project's knowledge base panel. Record filename, file type, line count, and a category grouping. This serves as a reference for what the project has access to and helps when converting to a Gemini CLI skill (to know what reference files to bundle).

### Mode 6: OPTIMIZE

Systematically improve project instructions using the autoresearch methodology — automated evaluation loops that find improvements humans miss.

This mode applies Andrej Karpathy's autoresearch concept to gemini.google.com Project instructions: define binary evals, run test prompts, score outputs, mutate the instructions, keep the winner, repeat.

**When to use:** After IMPROVE mode, when the user wants to push instruction quality beyond what manual rewriting achieves. Especially valuable for high-use projects where a 5% reliability improvement compounds across hundreds of sessions.

**Steps:**

1. Read `references/autoresearch-methodology.md` for the full methodology
2. **Define binary evals** (5-10 yes/no questions) based on:
   - The 5 audit dimensions (one eval minimum per dimension)
   - Project-specific requirements (format compliance, citation rules, domain constraints)
   - Known failure modes from the audit

   Example evals for a bill drafter:
   - "Does the output use the correct SECTION format (number, title, em dash, continuous text)?"
   - "Are only BAA No. 13 agencies cited?"
   - "Is the Qur'an/Hadith footnote protocol followed (general text + exact source in footnote)?"

3. **Create 3-5 test prompts** — realistic requests a user would type into the project
4. **Run the auto loop:**
   - Use the improved instructions as the system prompt
   - For each test prompt: generate output → evaluate against binary evals → score
   - Run each prompt 3x minimum (outputs are distributions, not deterministic)
   - Calculate baseline pass rate
   - Mutate the instructions (one targeted change per iteration)
   - Re-run and compare — keep the winner
   - Repeat until no improvement or 5 iterations
5. **Report results:**
   - Before/after pass rates
   - Which mutations helped vs didn't
   - The winning instruction set (copy-paste ready)
   - Save optimization log to the project's vault subfolder

**Important:** Apply only one mutation per iteration so improvements can be attributed to specific changes. Binary evals only — Likert scales compound variability and produce unreliable results.

**For deeper optimization** of the parallel Gemini CLI skill, use `/skill-optimizer` which has the full eval viewer, benchmarking infrastructure, and blind comparison capabilities.

## Self-Review Protocol

Every mode produces outputs. Every output gets verified before presenting to the user. This is not optional — it runs automatically after each mode completes.

### After DOCUMENT mode — verify all generated files:

**For `original-instructions.md`:**
- [ ] Line count > 50 (anything shorter is likely truncated)
- [ ] Contains the complete BARMM agency list if the original had one (check for "MAFAR", "MBHTE" as markers)
- [ ] Contains all section headers from the original (count them)
- [ ] No placeholder text like "[... rest follows ...]", "see above", or "[truncated]"
- [ ] Word count within 20% of the pasted original

**For `improved-instructions.md`:**
- [ ] Has XML tags (`<role>`, `<style_rules>`, etc.)
- [ ] Has full BARMM agency list with complete names (not just abbreviations) if the original had one
- [ ] Has `<knowledge_base>` section listing all uploaded files by name if screenshots were provided
- [ ] Template/structure sections preserve the detail level from the original — don't strip field descriptions to bare headers
- [ ] Is self-sufficient: someone could recreate the project from this file alone without needing the original

**For `attachment-list.md`:**
- [ ] Every file visible in the screenshot is listed
- [ ] Each file has: filename, type, line count, category

**For README.md:**
- [ ] Has audit scores if AUDIT was run
- [ ] Has linked skill name if SKILL was run
- [ ] Chat history captured from screenshot

### After IMPROVE mode — verify improved instructions quality:

Compare the improved version against the original on these checks:
- [ ] **No content loss** — every major section/template from the original is represented in the improved version (possibly restructured, but not deleted)
- [ ] **No detail stripping** — if the original had 10 detailed guide points for a section, the improved version doesn't reduce them to 1 header
- [ ] **Agency list complete** — if original had full agency names, improved has full agency names (not compressed to abbreviations)
- [ ] **Examples preserved** — if the original had sample text (e.g., Tagalog salutation, section format example), the improved version includes them
- [ ] **Self-sufficient** — the improved instructions work without needing the original as reference

### After SKILL mode — verify skill quality:

- [ ] SKILL.md has proper frontmatter (name, description with trigger phrases)
- [ ] References directory contains all extracted reference data
- [ ] Skill composition section lists relevant existing skills
- [ ] The skill is functionally distinct from existing skills (not a duplicate)

### If any check fails:

Fix it immediately before presenting to the user. Don't present partial or degraded output and ask if it's OK. The user has explicitly stated: truncation and lazy shortcuts are unacceptable. Do the work right the first time.

## Error Handling

| Failure | Detection | Recovery |
|---------|-----------|----------|
| **User pastes partial instructions** | Instructions end mid-sentence, or obvious sections missing | Ask: "This appears to be partial — are there more sections? I see [X] but expected [Y]." |
| **OneDrive/cloud-only files** | pandoc/extraction returns empty or "couldn't unpack" error | Tell user: "This file is a cloud placeholder. Please paste the content directly or download it first." |
| **Screenshot unreadable** | Can't identify file names, chat history, or storage info | Ask for a higher-resolution screenshot or request the user list files manually |
| **Ambiguous mode request** | User says "review my project" without specifying mode | Default to AUDIT. If instructions are already good (score > 4), suggest OPTIMIZE instead |
| **Existing skill overlap** | `Glob ~/.gemini/skills/*/SKILL.md` finds a skill with similar triggers | Warn user, show the overlap, and ask whether to merge, replace, or create distinct |
| **Self-review finds unfixable issue** | Original source unavailable to verify verbatim text | Flag the specific gap to the user rather than guessing. Never fabricate missing content |

## Mode Dependencies

Each mode produces outputs that feed into the next. When running the full pipeline:

| Mode | Consumes | Produces |
|------|----------|----------|
| **AUDIT** | Pasted instructions | Scores, anti-patterns, recommendations |
| **IMPROVE** | AUDIT scores + anti-patterns + original instructions | Rewritten instructions (copy-paste ready) |
| **SKILL** | Improved instructions + file inventory | SKILL.md + references/ directory |
| **DOCUMENT** | All prior outputs + screenshots | Vault subfolder with 4-5 files |
| **OPTIMIZE** | Improved instructions + audit findings | Binary evals, test prompts, winning instruction set |

When entering mid-pipeline (e.g., user jumps to SKILL without AUDIT), ask for the missing inputs rather than guessing.

## Workflow

When the user brings a project, the natural flow is:

1. **AUDIT** — understand what exists and where it falls short
2. **IMPROVE** — rewrite the instructions → **self-review improved instructions**
3. **SKILL** — create a parallel Gemini CLI skill → **self-review skill**
4. **DOCUMENT** — save everything to the vault → **self-review all files**
5. **OPTIMIZE** — (optional) run autoresearch loop to push quality beyond manual improvement

The user can enter at any point or skip steps. Ask which mode they want if unclear.

## Complexity Scaling

Adapt the approach based on project size:

| Complexity | Instructions | Files | Approach |
|------------|-------------|-------|----------|
| **Simple** | < 200 words, < 5 files | Quick audit, lightweight improve, skip OPTIMIZE |
| **Medium** | 200-800 words, 5-20 files | Full pipeline (AUDIT → IMPROVE → SKILL → DOCUMENT) |
| **Complex** | 800+ words, 20+ files | Full pipeline + multi-pass IMPROVE + OPTIMIZE recommended |

For **simple** projects: AUDIT can be abbreviated (scores + 2-3 key recommendations). IMPROVE focuses on adding structure and examples. SKILL may not be needed if the project is rarely used.

For **complex** projects: IMPROVE may require multiple passes — first pass restructures, second pass adds examples and RAG guidance. OPTIMIZE is strongly recommended to catch issues manual review misses. DOCUMENT should extract large reference data (agency lists, templates) into separate files.

## Common Patterns

### Legislative/Government Projects
These projects (like the user's Bangsamoro bill drafter) typically need:
- Precise formatting rules with examples
- Reference to specific legal frameworks (Constitution, organic laws)
- Agency/ministry reference lists
- Citation standards
- Output templates (bill structure, resolution format)

For these, the SKILL conversion should reference `/legal-assistant` and `/bangsamoro` skills.

### Research/Analysis Projects
- Clear methodology instructions
- Source verification requirements
- Output structure (sections, citations)

### Content Creation Projects
- Style guide integration
- Tone/voice examples
- Platform-specific formatting
