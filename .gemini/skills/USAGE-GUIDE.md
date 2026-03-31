---
tags: [gemini-cli, skills, guide, auto-update]
updated: 2026-03-28
total_skills: 135
---

# Skills Usage Guide

This guide tells you which skill to use for any task. Read it when you are unsure which skill to invoke. It is organized by what you want to accomplish, not alphabetically.

**Rule: When two skills could apply, use the more specific one.** `/bill-drafter` over `/bangsamoro` for drafting a bill. `/legislative-briefer` over `/csw` for a legislative briefer. The specific skill already invokes the general one internally.

---

## Quick Decision Tree

**"I need to draft legislation"**
- Bill (creates binding law) -> `/bill-drafter`
- Resolution (expresses parliamentary intent) -> `/resolution-drafter`
- Amendment to existing BAA -> `/bill-drafter` (amendment mode)

**"I need to prepare for a hearing"**
- Legislative briefer (bill analysis) -> `/legislative-briefer`
- Budget briefer (agency budget) -> `/csw` (budget briefer template)
- Interpellation questions -> `/bill-drafter` (Q&A mode)
- Speech or manifestation -> `/speech-writer`

**"I need to write a document"**
- Policy recommendation / brief / memo -> `/policy-recommendation`
- Policy paper (20+ pages, academic) -> `/policy-paper`
- Guidebook or manual (multi-chapter) -> `/guidebook-writer`
- Manual of Operations (MOP) -> `/mop`
- Complete Staff Work (any type) -> `/csw`
- Supervision system design -> `/supervision`

**"I need to research something"**
- Systematic legal research (4-step methodology, 7-tier hierarchy, Research Memorandum) -> `/legal-researcher`
- Legal analysis memo or comparison matrix -> `/legal-assistant`
- Deep multi-source research -> `/deep-research`
- Token-efficient research via NotebookLM -> `/research-pipeline`
- Bangsamoro domain context -> `/bangsamoro`

**"I need to verify or review"**
- Fact-check names, dates, legislation refs (Universal Verification Framework, P1-P10) -> `/fact-checker`
- Legal document review (accuracy, compliance, sufficiency, authority, currency) -> `/legal-reviewer`
- Comprehensive legal review (all modes combined) -> `/legal-reviewer` (FULL mode)
- Improve writing quality (remove AI slop) -> `/humanizer`
- Professional document tone -> `/writer`

**"I need to create a visual or document format"**
- PDF (professional, styled) -> `/pdf`
- Word document (.docx) -> `/docx`
- Excel spreadsheet -> `/xlsx`
- PowerPoint presentation -> `/pptx`
- Chart, infographic, data viz -> `/designer`

**"I need to work with video/audio"**
- Transcribe a video -> `/youtube-transcriber`
- Transcribe/extract from PDF -> `/transcriber`

**"I need to manage knowledge"**
- Save to Obsidian vault -> `/obsidian`
- Load vault context -> `/context`
- Surface hidden patterns in vault -> `/emerge`
- Connect two topics in vault -> `/connect`
- Update GUIDE files from transcripts -> `/guide-drafter`
- Review vault conventions -> `/vault-update`

**"I need to work with skills"**
- Create or modify a skill -> `/skill-creator`
- Analyze skill quality -> `/skill-optimizer` (ANALYZE mode)
- Optimize skill with auto-research -> `/skill-optimizer` (OPTIMIZE mode)
- Build an AI expert from research -> `/expert-builder`

---

## Bangsamoro Governance Skills

These skills form a connected ecosystem for parliamentary and government work. They share the `/bangsamoro` knowledge base and the local legislative archive (89 BAAs, 555 resolutions, 414 bills, BOL, BDP).

### The Legislative Pipeline

```
/bangsamoro (domain context)
    |
    v
/legal-researcher (FIND provisions)
    |
    v
/bill-drafter ---------> /resolution-drafter
    |                          |
    v                          v
/legal-reviewer (EVALUATE)  /speech-writer
    |                          |
    v                          v
/legal-assistant (PRODUCE)  /legislative-briefer
    |                          |
    v                          v
/fact-checker <--- /citation
    |
    v
Filed with Bills and Index Division
```

### Skill Relationships

| Skill | Invokes | Invoked By |
|-------|---------|------------|
| `/bangsamoro` | (foundation) | All Bangsamoro skills |
| `/legal-researcher` | `/bangsamoro`, `/transcriber` | `/legal-assistant`, `/legal-reviewer`, `/bill-drafter`, `/legislative-briefer`, `/resolution-drafter`, `/policy-recommendation`, `/fact-checker` |
| `/bill-drafter` | `/bangsamoro`, `/legal-assistant` | `/csw`, `/legislative-briefer` |
| `/resolution-drafter` | `/bangsamoro`, `/legal-assistant` | `/csw` |
| `/legislative-briefer` | `/bangsamoro`, `/bill-drafter` | `/csw` |
| `/speech-writer` | `/bangsamoro` | `/csw`, `/legislative-briefer` |
| `/csw` | `/legislative-briefer`, `/bill-drafter`, `/financial-analyst` | (orchestrator) |
| `/guidebook-writer` | `/bangsamoro`, composing skills | (standalone) |
| `/mop` | `/bangsamoro`, `/csw`, `/training-assistant` | (standalone) |
| `/supervision` | `/bangsamoro`, `/training-assistant` | (standalone) |
| `/policy-recommendation` | `/bangsamoro`, `/legal-assistant` | `/csw` |
| `/policy-paper` | `/bangsamoro`, `/deep-research` | (standalone) |
| `/fact-checker` | `/bangsamoro` officials ref, Universal Verification Framework (P1-P10 taxonomy) | All content skills (auto) |
| `/legal-reviewer` | `/legal-researcher`, `/bangsamoro` | All content skills (auto), `/legal-assistant` |
| `/legal-assistant` | `/legal-researcher`, `/legal-reviewer`, `/bangsamoro`, `/fact-checker`, `/docx` | `/bill-drafter`, `/policy-recommendation`, `/csw` |

### The Legislative Archive

All Bangsamoro legislative skills share these local archives. Check here BEFORE web searching.

| Archive | Count | Path | Used By |
|---------|-------|------|---------|
| Enacted BAAs | 89 | `~/Vault/bangsamoro/bangsamoro-laws/BAA-{N}.md` | `/bill-drafter`, `/resolution-drafter`, `/legal-reviewer` |
| Adopted Resolutions | 555 | `~/Vault/bangsamoro/bangsamoro-resolutions/resolution{N}.md` | `/resolution-drafter`, `/legislative-briefer` |
| Filed Bills | 414 | `docs/Bills/` | `/bill-drafter` |
| BOL (RA 11054) | 5 files | `~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/` | All |
| BDP 2023-2028 | 15 ch. | `~/Vault/bangsamoro/bangsamoro-development/bdp-2023-2028/` | All |
| BAA Quick Ref | 1 file | `~/Vault/bangsamoro/bangsamoro-laws/baa-quick-reference.md` | `/bangsamoro` Workflow A |
| Resolution Classification | 1 file | `~/Vault/bangsamoro/bangsamoro-resolutions/resolution-classification.md` | `/bangsamoro` Workflow B |

### MP Office Roles in the Workflow

Every document produced by these skills enters the MP office review chain:

1. **Legislative Staff Officers** prepare initial work
2. **Legislative Chief (SLSO I)** reviews, revises, manages legislative operations
3. **Chief of Staff (SPAO III/PAO VI)** clears for MP (overall supervision)
4. **MP** approves, modifies, or returns

Skills produce output at the Legislative Chief level — complete enough to clear the chain with minimal revision.

---

## Document Production Skills

| Need | Skill | Output |
|------|-------|--------|
| Professional PDF | `/pdf` | Styled PDF with headers, footers, cover page |
| Word document | `/docx` | .docx with formatting, tracked changes |
| Excel spreadsheet | `/xlsx` | .xlsx with formulas, charts, pivot tables |
| PowerPoint | `/pptx` | .pptx with layouts, speaker notes |
| Charts and infographics | `/designer` | PNG/SVG/PDF visualizations |

---

## Writing Quality Skills

Use these AFTER producing content, BEFORE delivering:

1. `/fact-checker` — Universal Verification Framework with P1-P10 taxonomy: verify names, titles, dates, legislation references, institutions, statistics (run FIRST)
2. `/legal-reviewer` — verify verbatim legal provisions (if citing BOL/BAAs)
3. `/humanizer` — remove AI patterns, make writing sound natural
4. `/writer` — professional document tone for BARMM context

---

## Common Multi-Skill Workflows

### Draft a Bill
```
/bangsamoro -> /legal-researcher -> /bill-drafter -> /legal-reviewer (ACCURACY) -> /fact-checker
```

### Prepare a Legislative Briefer
```
/bangsamoro -> /legal-researcher -> /legislative-briefer -> /legal-reviewer (ACCURACY) -> /fact-checker
```

### Legal Mandate Matrix for Strategic Planning
```
/legal-researcher -> /legal-assistant (MANDATE) -> /legal-reviewer (FULL)
```

### Write a Policy Recommendation
```
/bangsamoro -> /policy-recommendation -> /fact-checker -> /pdf
```

### Create a Guidebook
```
/bangsamoro -> /guidebook-writer (multi-chapter) -> /fact-checker -> /legal-reviewer -> generate-pdf.py
```

### Produce a MOP
```
/bangsamoro -> /mop (6-9 chapters) -> /fact-checker -> /pdf or /docx
```

### Prepare a Budget Briefer
```
/bangsamoro -> /csw (budget briefer template BB01-BB13) -> /fact-checker -> /financial-analyst
```

### Design a Training Program
```
/csw (training mode) or /training-assistant -> /pptx (slides) -> /docx (handouts)
```

---

## Auto-Update Convention

This guide must be updated whenever:
- A new skill is created
- An existing skill's scope or workflow changes
- Skills are merged, split, or deprecated
- Archive counts change (new BAAs enacted, new resolutions adopted)

**Who updates**: The session that creates or modifies a skill updates this guide as the final step.

**What to update**:
1. Decision tree entries (if a new "I need to..." is covered)
2. Skill relationships table (if composition changes)
3. Archive counts (if legislative archive grows)
4. Frontmatter `total_skills` count and `updated` date

---

*Last verified: 2026-03-28. 135 skills across global, project, and plugin scopes.*
