---
name: stitch-design
description: |
  Visual design exploration and planning with Google Stitch. Generates design directions,
  extracts design systems, and produces design.md blueprints that feed into /frontend-design
  for implementation. Use for greenfield projects and existing app redesigns.
  Triggers on: "stitch design", "stitch explore", "design direction", "visual exploration",
  "design planning", "design.md", "design system from URL", "redesign this section",
  "show me mockups", "explore visual directions", "stitch ideate".
  Invoke BEFORE /frontend-design when you want visual exploration before coding.
argument-hint: "[design brief or URL reference]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
---

# Stitch Design — Visual Exploration & Design System Extraction

Explore visual directions, generate design mockups, and extract design.md blueprints
using Google Stitch. This skill is a **companion to /frontend-design** — use it before
/frontend-design when you want to explore what something should look like before coding it.

## Prerequisites

- **Stitch MCP installed** in Gemini CLI or Antigravity
- **Stitch API key** from stitch.withgoogle.com
- 15 redesign credits per day (Stitch rate limit)

### Installation

**Gemini CLI:**
```bash
claude mcp add stitch --transport <stitch-transport-config>
# Then provide your API key when prompted
```

**Antigravity:**
Settings → MCP Service → search "Stitch" → Install → paste API key

### Verify Connection
Ask: "What was the latest design I created in Stitch?"
If it returns a project ID and timestamp, you're connected.

## When to Use This Skill

| Situation | Use /stitch-design? |
|---|---|
| "I don't know what this should look like" | Yes — explore 2-3 directions |
| "Redesign this section of my app" | Yes — feed current URL/screenshot into Stitch |
| "Compare visual directions before coding" | Yes — generate variants |
| "I need stakeholder buy-in before building" | Yes — quick mockups for approval |
| "I already know exactly what I want, just build it" | No — go straight to /frontend-design |
| "Fix this CSS bug" or "tweak this component" | No — too small for Stitch |

## Phase 1: Gather Inputs

### For new/greenfield projects
Ask the user for:
- What the product/page is about (1-2 sentences)
- Target audience
- Any reference URLs, screenshots, or design inspiration (Pinterest, Dribbble, Godly.website)

### For existing projects
- Take a screenshot or get the URL of the current app/page
- Ask what sections or aspects the user wants to explore redesigning
- Read existing design tokens/styles from the project if available

## Phase 2: Ideate in Stitch

### Option A: Ideation Mode (no reference)
Use Stitch's ideate feature to research and generate design directions:

```
Tell Stitch: "I'm building [product description]. Find the top 3 [industry] websites
and generate 3 different design directions based on what's working for them."
```

Stitch will:
1. Research existing sites in the niche
2. Produce strategy docs (typography, color palette, design tokens, interactions)
3. Generate 3 visual directions to choose from

### Option B: Redesign Mode (with reference)
Feed a URL or screenshot into Stitch's redesign feature:

```
Tell Stitch: "Redesign this [URL/screenshot] for [product]. Keep [what to preserve],
change [what to improve]. Include: [sections needed]."
```

Stitch uses Nano Banana 2 to generate concept art images first (not code) — this
produces better quality references than code-first approaches.

### Option C: Section-Level Exploration
For existing apps, don't redesign everything — focus on one section:

```
Tell Stitch: "Here's my current [dashboard/landing page]. Generate 3 variants
for just the [hero section / pricing table / navigation] in the same style."
```

## Phase 3: Iterate & Refine

- **Generate variants**: right-click any design → Regenerate or Variants (layout, color, images, custom)
- **Edit directly**: click Edit to modify text, colors, individual components inline
- **Annotate**: draw on the canvas, leave notes for specific changes
- **Multiple queries**: Stitch can process multiple design requests in parallel

Keep iterating until the user approves a direction. This is the cheap part —
visual iteration in Stitch is free and fast compared to coding alternatives.

## Phase 4: Extract design.md

Once the user picks a direction, extract the design blueprint:

```
Ask Gemini CLI: "Create a design.md based on my latest Stitch designs."
```

Gemini calls Stitch MCP → lists screens → fetches HTML → extracts design tokens + metadata.

The design.md contains:
- **Visual theme and atmosphere** (creative northstar)
- **Color palette** with hex values and roles (primary, secondary, accent, neutral)
- **Typography** (font families, sizes, weights, hierarchy)
- **Spacing and layout** rules
- **Component patterns** identified in the design
- **Anti-slop language** — how this design breaks away from generic templates

### Save the design.md

Save to the project directory so /frontend-design can reference it:
```
<project-root>/design.md
```

Or for multiple design systems:
```
<project-root>/design/design.md
<project-root>/design/stitch-screens/  (exported screenshots for reference)
```

## Phase 5: Hand Off to /frontend-design

After extracting design.md, tell the user:

```
Design direction locked. design.md saved to [path].

To implement, invoke /frontend-design with your design brief.
The skill will use the design.md as its aesthetic foundation.
```

The user then invokes `/frontend-design` separately — this skill does NOT auto-invoke it.

## Stitch MCP Commands Reference

```bash
# List your Stitch projects
# (via MCP — Gemini calls these automatically)
stitch.list_projects
stitch.get_project <project_id>
stitch.list_screens <project_id>
stitch.get_screen_html <screen_id>
stitch.get_project_metadata <project_id>
```

## Stitch Loop (Autonomous Multi-Page)

For multi-page designs, use the Stitch Loop pattern:
1. Build one screen with full art direction
2. Extract design.md from that screen
3. Gemini passes a "baton file" (the design.md) to itself
4. Generates remaining pages autonomously, matching the design system

Tell Gemini: "Use the Stitch Loop to generate all pages for this app based on the
design system from the first screen."

## Error Handling

| Situation | Response |
|---|---|
| Stitch MCP not installed | Tell user how to install (see Prerequisites) |
| API key expired or missing | Direct user to stitch.withgoogle.com for a new key |
| Redesign credits exhausted (15/day) | Suggest continuing tomorrow or using ideation mode (unlimited) |
| Design looks generic despite prompting | Sharpen the brief — add a reference URL/screenshot for Stitch to work from |
| User wants to go straight to code | Skip this skill — direct them to /frontend-design |

## Tips

- **Always provide reference images** — Stitch produces dramatically better output with visual references than text-only prompts
- **Use Pinterest for inspiration** — great for finding landing page designs and related styles
- **Nano Banana 2 generates concept art first** — think of outputs as "concept art that captures the essence", not final code
- **design.md is portable** — once extracted, use it across multiple projects for consistent branding
- **15 redesign credits/day** — ideation mode is unlimited, redesign mode is capped
