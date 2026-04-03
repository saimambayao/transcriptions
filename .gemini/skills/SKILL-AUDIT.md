---
date: 2026-03-31
purpose: Audit of Gemini skills for this repo (transcriptions) — categorize by usage
total_skills: 145 (including 3 non-skill files)
---

# Gemini Skills Audit — Transcriptions Repo

This repo's primary tasks: guidebook writing, legal references, YouTube transcription,
PDF production, legal research, fact-checking, session management, and vault integration.

Skills are categorized into 3 tiers based on 9 days of session summaries (260323-260331).

---

## Tier 1: ACTIVELY USED (48 skills)

Skills confirmed used in session summaries. Keep in `.gemini/skills/`.

### Core Production (guidebooks, legal refs, PDFs)
| Skill | Usage Context |
|-------|--------------|
| `guidebook-writer` | All 13+ BARMM guidebooks |
| `pdf` | WeasyPrint PDF generation for all guidebooks + legal references |
| `citation` | Feliciano-format footnotes in every chapter |
| `fact-checker` | VALIDATE + verification on every deliverable |
| `legal-reviewer` | ACCURACY + QA-REVIEW on legal references |
| `legal-researcher` | 5-step methodology, REFERENCE mode for BOL powers |
| `legal-assistant` | REFERENCE mode, 9-theme Q&A production |
| `shariah` | 7 modes for Shari'ah guidebook + Islamic law checkpoint |
| `bangsamoro` | Domain context loaded before every BARMM content task |
| `humanizer` | Voice consistency passes on guidebooks |
| `visualize` | Infographics and data visualizations in guidebooks |
| `excalidraw` | Diagrams (framework flows, process diagrams) |
| `transcriber` | PDF/DOCX text extraction (source documents) |

### Legislative Skills
| Skill | Usage Context |
|-------|--------------|
| `bill-drafter` | Bill drafting workflow, ECCD bill, skill refinement |
| `resolution-drafter` | Parliamentary resolutions, Hijri dates, WHEREAS conventions |
| `legislative-briefer` | 13-section CSW briefers, forum briefing template |
| `speech-writer` | Tagalog/Taglish speeches, Matatag 5 pillars |
| `policy-recommendation` | Bardach's Eightfold Path, OOBC 10 policy recs |
| `policy-paper` | OOBC comprehensive policy paper (58 pages) |
| `csw` | ADDRESS IT methodology for BARMM entities |
| `mop` | Manual of Operations (Bill Drafting MOP, OOBC MOP) |
| `supervision` | Supervision system design for BARMM |

### Transcription & Research
| Skill | Usage Context |
|-------|--------------|
| `youtube-transcriber` | 40+ videos transcribed across 9 days |
| `guide-drafter` | GUIDE files updated after every transcription |
| `notebooklm` | Deep research, topic notebooks, Research→Vault mode |
| `deep-research` | Multi-phase research with validation |
| `research-pipeline` | Token-efficient NotebookLM + sub-agent pipeline |
| `expert-builder` | Domain experts from NotebookLM research |
| `scrape` | 12 registered scrapers (lawphil, quran, hadith) |
| `content-research-writer` | Research-backed content writing |

### Workflow & Meta
| Skill | Usage Context |
|-------|--------------|
| `prompter` | Prompt refinement before every major task |
| `skill-optimizer` | ANALYZE + OPTIMIZE on 10+ skills |
| `auto-research` | Template optimization, Karpathy loop |
| `session-summary` | End-of-session daily notes |
| `context` | Load full user context from vault |
| `obsidian` | Vault note creation |
| `vault-update` | Review vault, recommend CLAUDE.md improvements |
| `emerge` | Surface latent insights from vault |
| `connect` | Cross-domain pattern finding in vault |
| `gitops` | Git commit and push workflow |

### Superpowers (workflow discipline)
| Skill | Usage Context |
|-------|--------------|
| `sp-brainstorming` | Pre-creative-work exploration |
| `sp-writing-plans` | Implementation plans before coding |
| `sp-executing-plans` | Execute plans with checkpoints |
| `sp-subagent-driven-development` | Parallel task execution |
| `sp-verification-before-completion` | Verify before claiming done |
| `sp-dispatching-parallel-agents` | 2+ independent parallel tasks |
| `sp-using-superpowers` | Skill discovery and usage |
| `sp-writing-skills` | Create/edit/verify skills |

---

## Tier 2: RELATED — POTENTIALLY USEFUL (24 skills)

Not confirmed used in session summaries, but directly relevant to this repo's tasks.
Keep in `.gemini/skills/` — likely to be needed.

| Skill | Why Relevant |
|-------|-------------|
| `training-assistant` | Training packages from guidebook content |
| `docx` | Word doc creation (deliverable format for BARMM) |
| `pptx` | Presentation creation from guidebook content |
| `xlsx` | Spreadsheet analysis (budget data, cooperative data) |
| `grill-me` | Stress-test plans before guidebook execution |
| `write-a-prd` | PRD creation for feature planning |
| `stitch-design` | Visual design exploration for guidebook covers |
| `brand-guidelines` | Anthropic brand application (if needed) |
| `lean-canvas` | Business model work (MoroTech, cooperatives) |
| `toc` | Theory of Change (evaluation, legislative programs) |
| `design-thinking` | Human-centered design for BARMM platforms |
| `financial-analyst` | Government financial analysis |
| `cooperative` | Cooperative development (RA 9520) |
| `governance` | Board governance, parliamentary operations |
| `file-organizer` | File organization utility |
| `meeting-insights-analyzer` | Meeting transcript analysis |
| `sp-requesting-code-review` | Verify work meets requirements |
| `sp-receiving-code-review` | Process code review feedback |
| `sp-systematic-debugging` | Debug methodically |
| `sp-finishing-a-development-branch` | Guide branch completion |
| `sp-using-git-worktrees` | Isolated worktrees |
| `sp-test-driven-development` | TDD workflow |
| `video-downloader` | Download videos for transcription |
| `image` | Image handling |

---

## Tier 3: NOT NEEDED — MOVE TO `other-skills/` (70 skills)

These are e-Bangsamoro platform-specific, mobile dev, startup/business, or otherwise
irrelevant to this repo's guidebook/transcription/legal work.

### e-Bangsamoro Platform-Specific (not this repo)
- `academy` — Course builder for e-Bangsamoro
- `appmanager` — App lifecycle orchestrator
- `apptimizer` — Performance optimization
- `backend` — Django backend development
- `build` — TypeScript build verification
- `coditor` — Deep code auditing
- `database` — PostgreSQL/Django ORM
- `debugger` — Professional debugging
- `devops` — Railway deployment
- `devwork` — Feature development (frontend-first)
- `documenter` — Markdown-to-React conversion
- `explainer` — Tech stack knowledge expert
- `frontend` — React 19 / Next.js frontend
- `investigator` — Deep error investigation
- `legislative` — Legislative tracking module
- `ministerial` — Ministerial coordination module
- `mobile` — React Native development
- `office` — Office management module
- `oversight` — Parliamentary oversight module
- `presentation` — Web-based React slides
- `push` — Push to remote + merge
- `refactor` — Module refactoring workflow
- `remotion-best-practices` — Remotion video rendering
- `representation` — Constituency representation module
- `safety-first` — Pre-task safety verification
- `security` — Auth, CSRF, XSS implementation
- `data-sync` — Portal-storefront sync
- `shared` — Shared utilities
- `test` — Comprehensive testing framework
- `tdd` — Test-driven development (code-specific)
- `ui-ux` — UI/UX design patterns
- `webapp-testing` — Playwright browser testing
- `writer` — e-Bangsamoro technical writing
- `improve-codebase-architecture` — Codebase architecture improvement
- `prd-to-issues` — PRD to GitHub issues

### Business/Startup (not this repo's domain)
- `branding` — Brand strategy (Aaker, Keller)
- `cofounder` — Founder development
- `enterprise-dev` — Enterprise growth frameworks
- `e-bangsamoro-investor` — Investor outreach
- `finance` — Organizational financial management
- `gamifier` — Gamification design
- `investor` — Investment banking perspective
- `leadership` — Leadership development
- `management` — Management frameworks (POLC)
- `marketer` — Marketing strategy (4Ps, STP)
- `product` — Product management (roadmaps, PMF)
- `social-enterprise` — SE 4D development
- `social-media` — Social media strategy
- `startup` — Startup strategy (Lean Startup)
- `storyteller` — Narrative design

### OBC-Specific Bill/Resolution Variants
- `bill-obc` — OBC-specific bill drafting
- `budget` — Government budget (BBSA)
- `resolution-obc` — OBC-specific resolution drafting
- `resolution-writer` — General purpose resolution writer

### Plugin Development (Anthropic plugin system)
- `plugin-agent-development`
- `plugin-command-development`
- `plugin-hook-development`
- `plugin-mcp-integration`
- `plugin-settings`
- `plugin-skill-development`
- `plugin-structure`

### Other Non-Relevant
- `ai-engineer` — AI engineering patterns
- `claude-api` — Claude API/SDK usage
- `gemini-automation-recommender` — Gemini automation setup
- `gemini-projects` — Gemini project instructions
- `figma-code-connect` — Figma component mapping
- `figma-design-system-rules` — Design system rules
- `figma-implement-design` — Figma to code
- `official-frontend-design` — Anthropic's frontend-design
- `official-skill-creator` — Anthropic's skill creator
- `frontend-design` — (duplicate of official)

### Non-Skill Files (keep in place)
- `Guidelines.md` — Skill format guidelines
- `USAGE-GUIDE.md` — Decision tree and skill relationships
- `index.md` — Skill index
- `auto-research-guidelines.md` — Auto research methodology

---

## Summary

| Tier | Count | Action |
|------|-------|--------|
| Tier 1: Actively Used | 48 | Keep in `.gemini/skills/` |
| Tier 2: Related/Useful | 24 | Keep in `.gemini/skills/` |
| Tier 3: Not Needed | 70 | Move to `.gemini/other-skills/` |
| Non-skill files | 4 | Keep in `.gemini/skills/` |
| **Total** | **146** | |

After reorganization: 76 skills + 4 files in `skills/`, 70 skills in `other-skills/`.
