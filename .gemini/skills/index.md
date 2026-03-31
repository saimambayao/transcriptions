---
tags: [gemini-cli, skills, index]
updated: 2026-03-28
total_skills: 135
---

# Gemini CLI Skills Library

Complete reference of all Gemini CLI skills — deduplicated, with clear boundaries. One subfolder per unique skill containing `skill.md` plus references and scripts.

**Purpose**: Portable skill archive for replication to other AI agents (Gemini, Codex, etc.) and as an Obsidian-searchable knowledge base.

---

## Global Skills (37)

Available in every Gemini CLI session via `~/.gemini/skills/`.

### Knowledge & Research
- [[brand-guidelines]] — Anthropic brand colors and typography
- [[gemini-projects]] — Audit/improve Gemini Project instructions
- [[content-research-writer]] — Research-backed content writing with citations
- [[deep-research]] — Multi-phase research with validation and confidence scoring
- [[expert-builder]] — Build AI experts from NotebookLM research
- [[notebooklm]] — Google NotebookLM CLI integration
- [[research-pipeline]] — Token-efficient research (NotebookLM + validation)
- [[auto-research]] — Universal autonomous optimization loop (Karpathy methodology)
- [[skill-optimizer]] — Analyze and optimize skill quality with evals

### Vault & Session
- [[connect]] — Find cross-domain connections in Obsidian vault
- [[context]] — Load full user context from Obsidian vault
- [[emerge]] — Surface latent insights from vault notes
- [[obsidian]] — Obsidian vault note creator
- [[session-summary]] — End-of-session daily note capture
- [[vault-update]] — Review vault and recommend GEMINI.md improvements

### Document Creation
- [[csw]] — Universal Complete Staff Work engine (ADDRESS IT methodology) for any BARMM entity
- [[guidebook-writer]] — Professional multi-chapter guidebooks for BARMM (Parliament + MOAs)
- [[mop]] — Manual of Operations (MOP) production for specific BARMM offices and divisions
- [[supervision]] — Supervision system design and supervisory development for BARMM entity heads/chiefs
- [[visualizer]] — Charts, infographics, and data visualizations *(renamed from designer)*
- [[docx]] — Word document creation, editing, tracked changes
- [[humanizer]] — Transform AI content to natural prose (generic)
- [[pdf]] — Professional PDF creation and manipulation
- [[pptx]] — Presentation creation and editing
- [[stitch-design]] — Visual design exploration with Google Stitch
- [[training-assistant]] — Complete training package builder
- [[xlsx]] — Excel spreadsheet creation, analysis, visualization

### Development Workflow
- [[gitops]] — Git commit and push workflow (agnostic)
- [[grill-me]] — Stress-test plans through relentless interview
- [[improve-codebase-architecture]] — Find architectural improvement opportunities
- [[prd-to-issues]] — Break PRDs into GitHub issues (vertical slices)
- [[prompter]] — Intelligent prompt refinement before execution
- [[refactor]] — Module refactoring workflow
- [[tdd]] — Test-driven development (red-green-refactor)
- [[webapp-testing]] — Browser automation testing with Playwright
- [[write-a-prd]] — Product requirements document creation

### Transcription & Legal
- [[fact-checker]] — Document accuracy verification (names, titles, dates, legislation)
- [[legal-assistant]] — Philippine legal and regulatory analyzer
- [[legal-researcher]] — Find and extract legal provisions from the Bangsamoro legislative archive (SEARCH, EXTRACT, SURVEY)
- [[meeting-insights-analyzer]] — Meeting transcript behavioral analysis
- [[transcriber]] — PDF OCR extraction and transcription verification *(Word scope removed — use [[docx]])*
- [[video-downloader]] — Video download utility
- [[youtube-transcriber]] — YouTube video transcription to markdown

### Utility
- [[file-organizer]] — File organization utility

---

## Cross-Project Skills (41)

Shared across e-Bangsamoro, e-Negosyo, bangsamorohr. Stack-agnostic where possible.

### Platform Development
- [[academy]] — Course and workshop builder for cooperatives/SEs
- [[ai-engineer]] — AI engineering patterns and workflows
- [[appmanager]] — Application lifecycle orchestrator (meta-skill/router)
- [[apptimizer]] — Systematic performance optimization
- [[backend]] — Backend development (Django)
- [[build]] — Build verification and error fixing
- [[coditor]] — Deep code auditing (security, best practices, architecture)
- [[database]] — PostgreSQL design, migrations, pgvector
- [[debugger]] — Professional debugging and issue resolution
- [[devops]] — Railway deployment and infrastructure
- [[devwork]] — Feature development (frontend-first, stack-agnostic) *(merged from devwork + featuredev)*
- [[explainer]] — Tech stack knowledge expert
- [[frontend]] — Frontend development (React 19, Next.js)
- [[investigator]] — Deep error investigation with online research
- [[mobile]] — React Native development
- [[presentation]] — Web-based presentation builder (React slides)
- [[push]] — Push to remote + optional merge (branch-agnostic) *(merged from push + csea-push + gitops-man)*
- [[safety-first]] — Pre-task safety verification
- [[security]] — Security implementation (auth, CSRF, XSS)
- [[shared]] — Shared utilities and references
- [[data-sync]] — Portal-storefront data sync verification *(renamed from sync)*
- [[test]] — Comprehensive testing framework
- [[ui-ux]] — UI/UX design patterns

### Bangsamoro & Governance
- [[bangsamoro]] — Domain expert in Bangsamoro affairs
- [[design-thinking]] — Human-centered design (Stanford d.school, IDEO)
- [[finance]] — Organizational financial management for cooperatives/SEs
- [[financial-analyst]] — Technical financial analysis (CFA-level)
- [[governance]] — Board governance and parliamentary operations
- [[lean-canvas]] — Lean Canvas business modeling (Ash Maurya)
- [[toc]] — Theory of Change planning and evaluation

### Business & Cooperative
- [[branding]] — Brand strategy and identity (Aaker, Keller, Kapferer)
- [[cofounder]] — Founder development and team dynamics
- [[cooperative]] — Cooperative development (RA 9520)
- [[enterprise-dev]] — Enterprise growth and scaling frameworks
- [[gamifier]] — Gamification design for learning platforms
- [[investor]] — Investment banking perspective (valuation, M&A, deals)
- [[leadership]] — Leadership development (transformational, servant, situational)
- [[management]] — Management frameworks (POLC, Mintzberg, Katz)
- [[marketer]] — Marketing strategy (4Ps, STP, AIDA, digital)
- [[product]] — Product management (roadmaps, prioritization, PMF)
- [[social-enterprise]] — Social enterprise 4D development journey
- [[social-media]] — Social media strategy and management
- [[startup]] — Startup strategy and execution (Lean Startup)
- [[storyteller]] — Narrative design and storytelling

---

## Project-Specific Skills (16)

### Parliamentarian (8)
- [[bill-drafter]] — Draft bills and enacted legislation for BTA Parliament
- [[resolution-drafter]] — Draft parliamentary resolutions (WHEREAS/operative clauses) for BTA Parliament
- [[legislative-briefer]] — 13-section CSW Legislative Analysis Briefer for any MP
- [[speech-writer]] — Speeches, messages, manifestations in Tagalog/Taglish for MPs and executives
- [[policy-recommendation]] — Standards-based policy recommendations, briefs, and memos for any BARMM agency (Bardach methodology)
- [[policy-paper]] — Comprehensive 20+ page policy papers with rear-loaded evidence-heavy structure
- [[legal-reviewer]] — Post-drafting legal fact-checking and validation
- [[resolution-writer]] — Draft parliamentary resolutions (general purpose)

### e-Bangsamoro Only (12)
- [[bill-obc]] — Bill drafting for OBC communities *(renamed from bill)*
- [[budget]] — Government budget management (BBSA compliance)
- [[documenter]] — Markdown-to-React component conversion *(PDF OCR → use [[transcriber]])*
- [[e-bangsamoro-investor]] — Investor outreach for e-Bangsamoro platform
- [[legislative]] — Legislative tracking module
- [[ministerial]] — Ministerial coordination module
- [[office]] — Office management module
- [[oversight]] — Parliamentary oversight module
- [[remotion-best-practices]] — Remotion video rendering rules
- [[representation]] — Constituency representation module
- [[resolution-obc]] — Resolution drafting for OBC communities *(renamed from resolution)*
- [[writer]] — Technical writing (e-Bangsamoro style, Philippine legal citations)

---

## Official Anthropic Plugin Skills (12)

Maintained by Anthropic. Included here for portability to other AI agents.

### Plugin Development (7)
- [[plugin-agent-development]] — Create subagents for Gemini CLI plugins
- [[plugin-command-development]] — Build slash commands
- [[plugin-hook-development]] — Event-driven hooks (PreToolUse, PostToolUse, etc.)
- [[plugin-mcp-integration]] — Integrate MCP servers into plugins
- [[plugin-settings]] — Plugin configuration with .local.md
- [[plugin-skill-development]] — Skill creation best practices
- [[plugin-structure]] — Plugin directory layout and manifest

### Design & Setup (3)
- [[gemini-automation-recommender]] — Recommend Gemini CLI automations for a codebase
- [[figma-code-connect]] — Connect Figma components to code
- [[figma-design-system-rules]] — Generate design system rules
- [[figma-implement-design]] — Translate Figma designs to code

### Meta (2)
- [[official-frontend-design]] — Anthropic's frontend-design skill (base version)
- [[official-skill-creator]] — Create, test, and iterate skills with evals

---

## Superpowers Skills (14)

Third-party plugin providing development workflow discipline.

### Planning & Architecture
- [[sp-brainstorming]] — Pre-creative-work intent and requirements exploration
- [[sp-writing-plans]] — Write implementation plans from specs before coding
- [[sp-executing-plans]] — Execute plans with review checkpoints
- [[sp-subagent-driven-development]] — Execute plans with parallel independent tasks

### Development Workflow
- [[sp-test-driven-development]] — TDD red-green-refactor loop
- [[sp-systematic-debugging]] — Debug methodically before proposing fixes
- [[sp-using-git-worktrees]] — Isolated worktrees for feature work
- [[sp-dispatching-parallel-agents]] — Dispatch 2+ independent parallel tasks

### Quality & Review
- [[sp-requesting-code-review]] — Verify work meets requirements
- [[sp-receiving-code-review]] — Process code review feedback with rigor
- [[sp-verification-before-completion]] — Verify before claiming work is done
- [[sp-finishing-a-development-branch]] — Guide branch completion (merge/PR/cleanup)

### Meta
- [[sp-using-superpowers]] — Discover and use superpowers skills
- [[sp-writing-skills]] — Create, edit, and verify skills

---

## Dedup Rules

To prevent future duplicates:
- **One skill per purpose** — before creating a new skill, check this index for overlap
- **Generic > specific** — prefer stack-agnostic skills with auto-detection over hardcoded platform versions
- **Clear ownership** — each capability has ONE owning skill (e.g., PDF OCR → `transcriber`, Word docs → `docx`, data viz → `visualizer`)
- **Naming** — use descriptive slugs; suffix with `-obc` for OBC-specific variants

## Skills 2.0 Format

```
skill-name/
├── skill.md              (required — YAML frontmatter + markdown body)
├── references/           (optional — detailed docs loaded on demand)
├── scripts/              (optional — executable code)
├── examples/             (optional — working code examples)
└── assets/               (optional — templates, fonts, images)
```

**Key rules:**
- YAML frontmatter with `name` and `description` required
- Description uses **third person** with specific trigger phrases
- Body **under 2,000 words** (max 5,000); details go in `references/`
- Use [[official-skill-creator]] to create, test, benchmark, and iterate skills
