---
name: training-assistant
description: |
  Complete training package builder that generates all materials from a training design.
  Triggers on: training package, training materials, facilitator guide, facilitator manual,
  participant handout, participant workbook, participant worksheet, session plan,
  training session, training design, training evaluation, evaluation form, pre-test,
  post-test, satisfaction survey, certificate generation, training certificate,
  certificate of completion, training presentation, session slides, training slides,
  training deck, build training, generate training, create training materials,
  training output, training deliverables, course materials, course package,
  workshop materials, workshop package, seminar materials, training bundle,
  learning materials, instructional materials, trainer guide, trainer manual,
  session guide, activity guide, handout generation, workbook generation.
  Use this skill whenever the user wants to produce any combination of facilitator guides,
  participant handouts, evaluation forms, certificates, or presentations from a training
  design or training description. Also use when the user asks to build, generate, or
  create a complete or partial training package. This skill orchestrates the full pipeline
  from training design input to finished deliverables.
argument-hint: "[training-design-file-or-topic]"
allowed-tools: Read, Bash, Glob, Grep
---

# Training Package Builder

## Overview

Build complete training packages from a training design markdown file (or from a topic description when no design exists yet). A training package consists of up to five deliverables generated from a single training design source:

| # | Deliverable | Format | Skill Used |
|---|-------------|--------|------------|
| 1 | Facilitator Guide | .docx | /docx |
| 2 | Participant Handouts | .docx | /docx |
| 3 | Evaluation Form | .docx | /docx |
| 4 | Certificate | .pdf | /pdf |
| 5 | Presentation(s) | .pptx | /pptx |

## Verification Protocol

This skill follows the Universal Verification Framework (Prevent → Detect → Confirm).
Read `~/.gemini/skills/fact-checker/references/verification-framework.md` for the full protocol.
Read `~/.gemini/skills/fact-checker/references/source-preload-protocol.md` — MANDATORY: load source text BEFORE writing any citation. No claims from training data when local source exists.
If a claim cannot be verified against loaded source files, mark it `[UNVERIFIED]` — never guess or fabricate. See source-preload-protocol.md Section 4.

**Before writing (PREVENT):**
1. Invoke `/bangsamoro` to load domain context
2. Read the fact-check error log at `~/Vault/skill-outputs/fact-checker/fact-check-error-log.md`
3. Read authoritative reference files relevant to the topic

**After writing (DETECT):**
Invoke `/fact-checker` on the complete document.

**Before delivery (CONFIRM):**
Present the fact-check report to the user. Fix all errors before delivery.

## Context

- Organization: **CSEA-BARMM** (Cooperative and Social Enterprise Authority, Bangsamoro Autonomous Region in Muslim Mindanao)
- 41 training designs live in: `/Users/saidamenmambayao/Library/Mobile Documents/com~apple~CloudDocs/Business Development/Cooperatives/Training/Training Package/Training-Design/Training-Design-MD/`
- Each training design MD has structured sections: Course Info, Modular Block Architecture, Course Description, Rationale, Learning Objectives, Content Outline, Traceability Matrix, Methodology, Session Plan, Assessment Tools, Case Studies, Facilitation Notes, Active Learning Integration, References, Assessment Instruments
- Existing build script for training design docx: `convert-training-designs.py`

## Brand and Styling

- **Font**: Inter (all documents, all headings, all body text)
- **Body text**: 10pt, line spacing 1.0, single extra line between paragraphs
- **Primary accent**: Dark blue `#1B4F72`
- **Secondary accent**: Medium blue `#2E86C1`
- **Tertiary accent**: Light blue-gray `#D6EAF8`
- **Body text color**: Near-black `#1A1A1A`
- **Table header background**: `#1B4F72` with white text
- **Table alternating rows**: `#F8F9FA`
- **NEVER use purple colors**
- **Use icons (Unicode/symbol) instead of emojis**

## Workflow

### Step 0: Determine Input

**If the user provides a training design MD file path:**
- Read the full file to extract all structured sections
- Proceed to Step 1

**If the user provides a topic or description but no existing training design:**
- Ask the user: "No existing training design found. Shall I build a draft training design first for your approval before generating the package?"
- If yes, create a draft training design MD following the structure of existing designs, present it, and wait for approval
- If the user just wants specific deliverables (e.g., only a facilitator guide), proceed with whatever information is available

**If the user names a training by code (e.g., "A1", "B2", "H5"):**
- Search for the matching file in the Training-Design-MD directory using Glob
- Read the latest version (highest VerXX number)

### Step 1: Parse the Training Design

Extract these key elements from the training design:

| Element | Used In |
|---------|---------|
| Course title, code, hours | All deliverables |
| Target participants | Facilitator Guide, Handouts, Certificate |
| Learning objectives | Facilitator Guide, Handouts, Evaluation |
| Content outline (topics) | Facilitator Guide, Handouts, Presentations |
| Session plan (time blocks) | Facilitator Guide, Presentations |
| Methodology | Facilitator Guide |
| Assessment instruments | Evaluation Form |
| Case studies | Facilitator Guide, Handouts |
| Facilitation notes | Facilitator Guide |
| Active learning activities | Facilitator Guide, Handouts |
| Materials/tools listed | Facilitator Guide, Handouts |

### Step 2: Confirm Scope with User

Present the parsed summary and ask:
- "Which deliverables do you want generated?" (default: all five)
- "Any customizations?" (date, venue, specific participant names for certificates, etc.)
- If generating certificates, collect: participant names, date, venue, signatory names/titles

### Step 3: Generate Deliverables

Generate each requested deliverable by invoking the appropriate skill. Process them in parallel where possible (facilitator guide + handouts + evaluation can run simultaneously; presentations may depend on finalized content).

---

## Deliverable Specifications

### 1. Facilitator Guide (.docx)

**Reference template**: Read `references/facilitator-guide-template.md` for the full structural template.

**Key sections to generate:**
- Cover page (course title, code, organization, date, version)
- Course overview (description, rationale, objectives, methodology)
- Preparation checklist (materials, room setup, tech requirements)
- Detailed session-by-session guide:
  - For EACH time block in the session plan, generate:
    - Time and duration
    - Topic/activity title
    - Facilitator instructions (step-by-step what to do and say)
    - Discussion prompts and expected participant responses
    - Transition cues to next segment
    - Materials needed for that segment
    - Tips and common pitfalls
- Assessment administration guide (how to administer pre/post tests)
- Appendices: answer keys, rubrics, handout masters

**Content generation rules:**
- Write facilitator instructions in second person ("You will..." / "Ask participants to...")
- Include time cues: [icon:clock] markers for pacing
- Include discussion prompts with 2-3 expected response directions
- Flag activities that need advance preparation with [icon:warning]
- Mark optional/alternative activities clearly

**Invoke**: `/docx` skill to create the .docx file

### 2. Participant Handouts (.docx)

**Reference template**: Read `references/participant-handout-template.md` for the full structural template.

**Key sections to generate:**
- Cover page (course title, participant name field, date field)
- Course overview (simplified: what you will learn, schedule at a glance)
- For EACH topic/session:
  - Key concepts summary (1-2 paragraphs)
  - Vocabulary/key terms box
  - Activity worksheets (fill-in, matching, tables to complete)
  - Notes space (lined or boxed areas)
  - Reflection prompts
- Reference sheets (frameworks, matrices, checklists used in the course)
- Personal action plan template (end of course)
- Evaluation form (if bundled)

**Content generation rules:**
- Write in participant-friendly language (accessible, Grade 6-8 reading level for BARMM context)
- Include clear instructions for each worksheet
- Leave adequate blank space for writing
- Use tables, checkboxes, and structured formats over free-form text

**Invoke**: `/docx` skill to create the .docx file

### 3. Evaluation Form (.docx)

**Reference guide**: Read `references/evaluation-form-guide.md` for guidelines on choosing the right evaluation approach.

**Determine the best evaluation approach based on the training design:**

| Training Type | Recommended Evaluation |
|---------------|----------------------|
| Knowledge-focused (Category A basics) | Pre/post test + satisfaction survey |
| Skill-focused (workshops, hands-on) | Pre/post test + skills demonstration rubric + satisfaction |
| Short training (2-4 hours) | Combined: 5-item knowledge check + satisfaction |
| Full-day or multi-day | Separate pre-test, post-test, and satisfaction survey |

**If the training design already includes assessment instruments (Section 15):**
- Use those items directly in the pre/post test
- Add a satisfaction survey section

**If no assessment instruments exist:**
- Generate 10-item pre/post test aligned to learning objectives
- Item types: True/False, Multiple Choice, Short Answer (mix based on proficiency level)
- Add a satisfaction/reaction survey (Kirkpatrick Level 1)

**Satisfaction survey standard items:**
1. Overall training rating (1-5 scale)
2. Relevance to work/role (1-5)
3. Quality of facilitation (1-5)
4. Quality of materials (1-5)
5. Adequacy of time allocation (1-5)
6. Most useful topic (open)
7. Suggestions for improvement (open)
8. Would recommend to colleagues (Yes/No)

**Invoke**: `/docx` skill to create the .docx file

### 4. Certificate (.pdf)

**Layout**: Landscape orientation, letter size (11" x 8.5")

**Design elements:**
- Decorative border (dark blue `#1B4F72` accent line, subtle)
- Organization header: "COOPERATIVE AND SOCIAL ENTERPRISE AUTHORITY" / "Bangsamoro Autonomous Region in Muslim Mindanao"
- Title: "CERTIFICATE OF COMPLETION" or "CERTIFICATE OF TRAINING"
- Body text: "{Participant Name} has successfully completed the training on {Course Title} ({Course Code}) consisting of {Hours} hours conducted on {Date} at {Venue}."
- Signature lines (2-3): Facilitator, Division Chief, Executive Director (or as specified)
- Certificate number field (optional)
- No background images unless user provides one

**Invoke**: `/pdf` skill to create the .pdf file using HTML-to-PDF workflow

### 5. Presentation(s) (.pptx)

**Generate one presentation per major session block or topic**, based on the Modular Block Architecture.

**For each presentation:**
- Title slide: Course title, block/topic title, CSEA-BARMM
- Objectives slide: Learning objectives for that block
- Content slides: Key concepts, frameworks, definitions (from Content Outline)
- Activity slides: Instructions for workshop/activity segments
- Discussion slides: Prompts and questions
- Summary/recap slide
- Transition slide (to next block if applicable)

**Design approach:**
- Use dark blue `#1B4F72` as primary color
- Clean, minimal slides (not text-heavy)
- Max 6-7 bullet points per slide, prefer 4-5
- Use visual frameworks (tables, diagrams described in text) where the training design references them
- Speaker notes: Include facilitator talking points and time cues

For training diagrams (process flows, frameworks, models), use `/excalidraw` to generate PNGs for embedding in presentations and handouts. For training material visuals, dashboards, and one-page visual summaries, use `/visualize` to generate self-contained HTML visualizations that can be converted to PNG for embedding.

**Invoke**: `/pptx` skill to create the .pptx file(s)

---

## Output Organization

Save all generated files in a directory structure:

```
{output-directory}/
  {CourseCode}-Facilitator-Guide.docx
  {CourseCode}-Participant-Handouts.docx
  {CourseCode}-Evaluation-Form.docx
  {CourseCode}-Certificate.pdf
  {CourseCode}-Presentation-Block-{BlockID}.pptx
  ...
```

Default output directory: same directory as the source training design file, in a subfolder named `{CourseCode}-Training-Package/`

## File Lookup

To find a training design by code:
```bash
ls "/Users/saidamenmambayao/Library/Mobile Documents/com~apple~CloudDocs/Business Development/Cooperatives/Training/Training Package/Training-Design/Training-Design-MD/" | grep -i "{code}"
```

To find the latest version of a training design:
```bash
ls -t "/Users/saidamenmambayao/Library/Mobile Documents/com~apple~CloudDocs/Business Development/Cooperatives/Training/Training Package/Training-Design/Training-Design-MD/Training-Design-{code}*" | head -1
```

## Important Notes

- All docx output must use Inter font, 10pt body, line spacing 1.0 per GEMINI.md
- Never use purple in any deliverable
- Use Unicode icons/symbols, never emojis
- When generating certificates in batch, prompt for the list of participant names
- If a training design references activities from a separate Activity Catalog, note the reference but generate reasonable activity instructions based on what is described in the training design itself
- Respect the Kolb Experiential Learning Cycle structure when writing facilitator instructions: concrete experience before abstract conceptualization
- For BARMM context: note multilingual facilitation needs, functional literacy considerations, and local cooperative examples

## Fact-Check Before Delivery

Before delivering the final training package, run `/fact-checker` on content-heavy deliverables
(facilitator guide, participant handouts). Training materials cite legislation, statistics,
official names, and institutional facts — errors in training materials get multiplied across
every participant who receives them.

## Gotchas

- BOL article numbers are the #1 fabrication target — always verify against ~/Vault/bangsamoro/bangsamoro-laws/bol-ra-11054/
- BAA numbers are the #2 fabrication target — verify against ~/Vault/bangsamoro/bangsamoro-laws/index.md
- Use BARMM ministry abbreviations (MFBM not DBM, MOLE not DOLE, MBHTE not DepEd, MILG not DILG) — never national equivalents
- Mas Matatag na Bangsamoro Agenda (2026-2028) replaces 12-Point Priority Agenda — update all references
- Never cite guidebooks as primary sources — trace back to enacted law (BAA, RA, BOL)
- A wrong BAA number, BOL article, or official title is 3x worse than writing [UNVERIFIED]. When in doubt, mark it.
- Training content for BARMM staff must reference BARMM-specific legislation, not national equivalents
- Facilitator guides must include correct titles and positions of officials who may attend
- Session timings in training designs must account for prayer breaks (Dhuhr, Asr)

## Subagent Honesty Rules

Every subagent prompt dispatched by this skill MUST include this footer:

> HONESTY RULES:
> 1. Only extract values explicitly stated in source documents. If ambiguous or missing, leave blank with a one-line reason.
> 2. A wrong answer is 3x worse than a blank answer. When in doubt, leave it blank.
> 3. Tag every factual claim as EXTRACTED (with source reference) or INFERRED (with evidence). Inferred claims will be verified first.
