---
name: academy
description: Course and workshop design specialist for MoroAcademy LMS with research capability. Use when designing, creating, structuring, or managing online courses and live workshops. Covers curriculum design and development using ADDIE, UbD (Understanding by Design), and SAM frameworks, competency-based curriculum development, training needs assessment (TNA), learning objectives with Bloom's Taxonomy, curriculum mapping, lesson planning, assessment design, Kirkpatrick evaluation model, workshop facilitation, multi-day training programs, and presentation-style UI for live workshops and video content. Includes research capability to find best practices, industry standards, subject matter expertise, and pedagogical approaches. For storytelling and narrative design, invoke /storyteller. For gamification and simulations, invoke /gamifier.
argument-hint: "[course or workshop topic]"
---

# Academy - MoroAcademy Course & Workshop Design

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's academy/training request                 ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

## Overview

Academy is the instructional design specialist for MoroAcademy, the learning management system of the Negosyo Bangsamoro Digital Platform. It provides expertise in designing effective courses and workshops that transform cooperative/SE members into competent practitioners.

**Core Purpose**: Design and create pedagogically sound courses and workshops that achieve measurable learning outcomes.

**Deep Research**: Academy performs **Deep Research** when starting any new course or workshop. This is mandatory, not optional. Deep Research follows the **Plan → Search → Read → Iterate → Output** cycle (inspired by [Gemini Deep Research](https://blog.google/products/gemini/google-gemini-deep-research/)) to systematically explore topics through iterative web searching and synthesis.

See: [references/deep-research.md](references/deep-research.md) for complete methodology.

## When to Use This Skill

Invoke Academy when:
- **Curriculum Development**: "Design a curriculum for cooperative leadership development"
- **Course Design**: "Design a course on cooperative financial management"
- **Curriculum Structure**: "How should I structure this 5-module course?"
- **Learning Objectives**: "Write learning objectives for bookkeeping basics"
- **Lesson Planning**: "Plan lessons for a video course on marketing"
- **Workshop Design**: "Create a 3-day workshop curriculum"
- **Assessment Creation**: "Design quizzes for the governance module"
- **Content Organization**: "How do I break this topic into modules?"
- **Training Needs Assessment**: "Conduct a TNA for cooperative board members"
- **Competency Mapping**: "Map competencies for financial management certification"
- **Evaluation Planning**: "Design evaluation using Kirkpatrick model"
- **Facilitation Guide**: "Create facilitator notes for this workshop"
- **Presentation Design**: "Create presentation slides for the workshop session"
- **Video Recording**: "Build slides for recording a video course"
- **Research Best Practices**: "Research best practices for cooperative governance training"
- **Subject Matter Research**: "Research current financial literacy frameworks for coops"
- **Industry Standards**: "Find CDA requirements for cooperative officer training"
- **Pedagogical Research**: "Research effective methods for adult financial education"
- **BARMM Context**: "Align this curriculum with BDP 2023-2028 priorities"
- **Islamic Education**: "Integrate Islamic principles into this governance course"
- **Workforce Development**: "Design training for BDP workforce needs"

**Keywords**: "course", "workshop", "curriculum", "curriculum design", "curriculum development", "lesson", "learning objectives", "module", "session", "training", "assessment", "quiz", "certificate", "presentation", "slides", "PowerPoint", "ADDIE", "UbD", "backward design", "SAM", "competency-based", "TNA", "training needs assessment", "Kirkpatrick", "evaluation", "research", "best practices", "industry standards", "pedagogical", "BARMM", "BDP", "Bangsamoro", "moral governance", "Islamic education", "Islamic finance"

**For storytelling, narrative design, learner personas, and journey mapping** → Invoke `/storyteller`

**For gamification, simulations, points/badges, and learning games** → Invoke `/gamifier`

### BARMM Development Plan Context

When designing courses for BARMM audiences or aligning with regional development priorities, consult [references/barmm-bdp-alignment.md](references/barmm-bdp-alignment.md) for:
- BDP 2023-2028 six development goals and strategies
- Moral Governance 12 pillars for integration into courses
- Workforce development priorities by economic sector
- Islamic education integration opportunities
- BARMM-specific education and skills gaps
- Macroeconomic targets affecting training needs
- Curriculum alignment examples for all core courses

---

## Quick Start Workflows

### Create a Course (Self-Paced)

```
STAGE 0: DEEP RESEARCH (MANDATORY) → Output: Validated Research Brief
│
├── LAYER 1: Invoke /deep-research skill
│   ├── Workflow 1: Initial Deep Research (10+ searches, 5+ fetches)
│   ├── Workflow 2: Research Validation (re-fetch top sources)
│   ├── Workflow 3: Factual Accuracy Verification (dates, numbers, names)
│   ├── Workflow 4: Refinement (corrections, strengthened citations)
│   └── OUTPUT: Research Brief with Works Cited
│
└── LAYER 2: Academy Curriculum Validation
    ├── Review for curriculum applicability
    ├── Cross-reference with domain-specific sources (CDA, ICA, etc.)
    ├── Validate against regulatory requirements
    ├── Ensure pedagogical alignment (adult learning, Bloom's taxonomy)
    └── OUTPUT: Validated Research Brief for curriculum design

STAGE 1: ANALYZE → Output: Course Brief
├── Identify target audience
├── Define learning problem/gap
├── Assess prerequisites
└── Determine constraints (time, device, language)

STAGE 2: DESIGN → Output: Course Outline
├── Write learning objectives (Bloom's verbs)
├── Structure modules (3-7 modules)
├── Plan lesson sequence
└── Design assessment strategy

STAGE 3: DEVELOP → Output: Course Content
├── Create VIDEO/TEXT/QUIZ lessons
├── Videos: max 15 min, purposeful durations (see guidelines below)
├── Text: 500-1000 words, Grade 8 reading level
├── Quizzes: 5-10 questions with feedback
└── Scripts: English + Filipino (bilingual)

STAGE 4: IMPLEMENT → Output: Live Course
├── Invoke /presentation → Build session/slide pages (if presentation-style)
├── Invoke /frontend → Build course pages
├── Invoke /backend → API integration (if needed)
├── Configure enrollment and pricing
└── Publish to MoroAcademy

STAGE 5: EVALUATE → Output: Course Analytics
├── Monitor completion rates (target: 60%+)
├── Analyze quiz scores (target: 70%+ pass)
└── Iterate based on feedback
```

**Full workflow details**: [references/course-creation-workflow.md](references/course-creation-workflow.md)

### Create a Workshop (Live Training)

```
DECISION: Simple (1-4h) or Multi-day (2-5 days)?

STAGE 0: DEEP RESEARCH (MANDATORY) → Output: Validated Research Brief
│
├── LAYER 1: Invoke /deep-research skill
│   ├── Workflow 1: Initial Deep Research (10+ searches, 5+ fetches)
│   ├── Workflow 2: Research Validation (re-fetch top sources)
│   ├── Workflow 3: Factual Accuracy Verification (dates, numbers, names)
│   ├── Workflow 4: Refinement (corrections, strengthened citations)
│   └── OUTPUT: Research Brief with Works Cited
│
└── LAYER 2: Academy Curriculum Validation
    ├── Review for curriculum applicability
    ├── Cross-reference with domain-specific sources (CDA, ICA, etc.)
    ├── Validate against regulatory requirements
    ├── Ensure pedagogical alignment (adult learning, Bloom's taxonomy)
    ├── Verify facilitation best practices & methodologies
    └── OUTPUT: Validated Research Brief for workshop design

STAGE 1: ANALYZE → Output: Workshop Brief
├── Identify training need
├── Profile participants (15-30 optimal)
├── Determine logistics (venue, dates, budget)
└── Set participant limits

STAGE 2: DESIGN → Output: Workshop Curriculum
├── Define learning outcomes (3-5 max)
├── Select methodologies (30% lecture / 70% active)
├── Structure: Days → Modules → Sessions
└── Plan major outputs (templates participants complete)

STAGE 3: DEVELOP → Output: Workshop Package
├── Create session content blocks
├── Write facilitator guides
├── Design templates for outputs
└── Prepare materials checklist

STAGE 4: IMPLEMENT → Output: Live Workshop
├── Invoke /presentation → Build session/slide pages for facilitation
├── Invoke /frontend → Build curriculum pages
├── Set up registration (access codes, pre-registration)
├── Schedule sessions and generate QR codes
└── Publish workshop

STAGE 5: FACILITATE & EVALUATE → Output: Workshop Report
├── Take attendance per session (80% required for cert)
├── Collect output submissions
├── Run pre/post assessments
└── Issue certificates
```

**Full workflow details**: [references/workshop-creation-workflow.md](references/workshop-creation-workflow.md)

---

## Decision Trees

### Course vs Workshop?

| Choose COURSE when... | Choose WORKSHOP when... |
|----------------------|------------------------|
| Self-paced, always available | Live instruction needed |
| Certification/knowledge focus | Hands-on practice focus |
| Scale to many learners | Intensive skill building |
| Limited facilitator resources | Facilitator available |
| Under 10 hours total | 1-5 days intensive |

**Quick rule**: Can they learn it from video/text? → COURSE. Need coaching/practice? → WORKSHOP.

### Simple vs Multi-day Workshop?

| Choose SIMPLE when... | Choose MULTI_DAY when... |
|----------------------|-------------------------|
| Single topic, 1-4 hours | Multiple topics, 2+ days |
| Lecture/demo format | Simulation/games needed |
| No output templates | Multiple output deliverables |
| Orientation/intro | Comprehensive skill building |
| No pre/post assessment | Full assessment required |

---

## Research Capability

See [references/extracted-content.md](references/extracted-content.md) for details.

## Research Questions
1. [Question 1]
2. [Question 2]

## Key Findings

### Subject Matter
- [Key concept 1]
- [Key concept 2]

### Industry Standards
- [Requirement 1]
- [Requirement 2]

### Best Practices
- [Best practice 1]
- [Best practice 2]

### Recommended Approach
[Summary of recommended curriculum approach based on research]

## Sources
1. [Source 1 with URL]
2. [Source 2 with URL]
```

**Full research guide**: [references/research-capability.md](references/research-capability.md)

---

## Essential Courses & Workshops

See [references/extracted-content.md](references/extracted-content.md) for details.

## Government Training

See [references/extracted-content.md](references/extracted-content.md) for details.

## Presentation UI (Web-Based Slides)

When building presentation pages for courses or workshops, invoke the `/presentation` skill.

**Invoke `/presentation`** for:
- Building session/slide pages with `PresentationMode`
- Creating projector-ready web presentations
- Adding Framer Motion animations
- Implementing facilitator content locking
- Optimizing for video recording

### Font Standard

**Official Font: Inter Only** - All MoroAcademy presentations MUST use Inter as the sole font family.

```tsx
<div className="font-[family-name:var(--font-inter)]">
  {/* All presentation slides use Inter */}
</div>
```

**Font Reference Implementation**: `/frontend/src/app/(academy)/academy/model-presentation/`

**Reference Implementation**: `/frontend/src/app/(academy)/academy/edp/`

**Full documentation**: See [references/presentation-ui-standards.md](references/presentation-ui-standards.md) for components, typography, font standard, layout patterns, and animations.

---

## Use Templates

See [references/extracted-content.md](references/extracted-content.md) for details.

## MoroAcademy Content Structure

See [references/extracted-content.md](references/extracted-content.md) for details.

## Curriculum Design Frameworks

Choose the right framework for your instructional design approach:

| Framework | Best For | Key Principle |
|-----------|----------|---------------|
| **ADDIE** | Traditional, structured programs | Sequential phases: Analyze → Design → Develop → Implement → Evaluate |
| **UbD (Backward Design)** | Competency-based, outcome-focused | Start with desired results, work backward to activities |
| **SAM** | Digital courses, rapid development | Iterative cycles: Design → Prototype → Review → Repeat |

**Quick Selection**:
- Government/compliance training → **ADDIE**
- Professional skill building → **UbD (Backward Design)**
- Digital courses needing iteration → **SAM**

**Full framework details**: [references/curriculum-design.md](references/curriculum-design.md)

---

## General → BARMM Contextualization Standard

See [references/extracted-content.md](references/extracted-content.md) for details.

## ADDIE Framework for Course Design

See [references/extracted-content.md](references/extracted-content.md) for details.

## Writing Learning Objectives

Use Bloom's Taxonomy verbs for measurable objectives:

| Level | Verbs | Example |
|-------|-------|---------|
| Remember | List, Define, Identify | "List the 7 cooperative principles" |
| Understand | Explain, Summarize, Describe | "Explain the purpose of member equity" |
| Apply | Calculate, Demonstrate, Use | "Calculate patronage refund distribution" |
| Analyze | Compare, Differentiate, Examine | "Compare cooperative vs corporate governance" |
| Evaluate | Assess, Justify, Recommend | "Evaluate financial health using PEARLS ratios" |
| Create | Design, Develop, Formulate | "Design a marketing plan for the cooperative" |

**SMART Objectives Format**:

```
By the end of this [lesson/module/course], learners will be able to
[action verb] + [specific content] + [condition/context].
```

**Examples**:
- "Calculate patronage refunds using the contribution method"
- "Prepare a simplified cash flow statement for a small cooperative"
- "Identify compliance requirements under RA 11524"

## Module Structure Patterns

See [references/extracted-content.md](references/extracted-content.md) for details.

## Lesson Design (Courses)

See [references/extracted-content.md](references/extracted-content.md) for details.

## Session Design (Workshops)

See [references/extracted-content.md](references/extracted-content.md) for details.

## Multi-Day Workshop Design

See [references/extracted-content.md](references/extracted-content.md) for details.

## Assessment Strategies

See [references/extracted-content.md](references/extracted-content.md) for details.

## MoroAcademy Data Structures

See [references/extracted-content.md](references/extracted-content.md) for details.

## Quick Reference

### Course Checklist

- [ ] Clear, descriptive title
- [ ] 3-5 measurable learning objectives
- [ ] Logical module structure (Module -> Lesson)
- [ ] Mix of lesson types (video, text, quiz)
- [ ] Assessment aligned to objectives
- [ ] Estimated duration accurate
- [ ] Prerequisites stated
- [ ] Certificate criteria defined

### Workshop Checklist

- [ ] Target audience defined
- [ ] Day/Module/Session structure planned
- [ ] Session timing realistic
- [ ] Breaks scheduled (every 90 min)
- [ ] Materials list complete
- [ ] Facilitator guide prepared
- [ ] Venue requirements specified
- [ ] Registration deadline set

## Additional References

See [references/extracted-content.md](references/extracted-content.md) for details.

## Cooperative Training Programs

See [references/cooperative-integration.md](references/cooperative-integration.md) for detailed cooperative training guidance including:
- Pre-Registration Seminar (PRS) requirements and curriculum
- Cooperative officer training pathway (PRS -> COOP-101 -> COOP-201 -> COOP-301 -> Specialized)
- CDA MC 2015-09 compliance: training requirements by coop size, timelines, consequences
- ETF utilization for training (Art. 59, RA 9520): eligible expenses, documentation, reporting
- Training delivery modes (online, blended, live, TSP-delivered)
- Member education programs beyond officer training

## Skill Integration

When to invoke other skills:

| Task | Skill | Purpose |
|------|-------|---------|
| Add storytelling/narrative | `/storyteller` | Hero's Journey, 3-Act, personas, journey mapping |
| Add gamification/simulations | `/gamifier` | Points, badges, simulations, debriefing |
| Build presentation slides | `/presentation` | Session pages, Framer Motion, facilitator control |
| Build course/workshop UI | `/frontend` | Create pages, components |
| Create API endpoints | `/backend` | Enrollment, progress APIs |
| Full-stack features | `/featuredev` | Complete feature implementation |
| UX improvements | `/ui-ux` | Learner experience design |
| Debug issues | `/debugger` | Fix errors and bugs |
| Validate changes | `/build` + `/test` | Quality assurance |

### /storyteller Integration

Invoke `/storyteller` when designing narrative elements:

| Trigger | /storyteller Output |
|---------|---------------------|
| "Add narrative to this course" | Story arc + character profiles |
| "Create learner personas" | 2-3 detailed personas with empathy maps |
| "Map the learner journey" | Journey map with touchpoints and emotions |
| "Design engaging video lessons" | 3-Act structure + script outline |
| "Make this workshop memorable" | Story template + emotional design |

**Handoff Pattern**:
```
/academy (Research + Design)
    │
    ├─► Invoke /storyteller for narrative design
    │       └─► Returns: Personas, journey map, story arc
    │
    └─► Continue with ADDIE (Develop → Implement → Evaluate)
```

### /gamifier Integration

Invoke `/gamifier` when designing game elements:

| Trigger | /gamifier Output |
|---------|------------------|
| "Add gamification to this course" | Points system, badges, progress design |
| "Design a business simulation" | Simulation structure, economy, materials |
| "Make this workshop engaging with games" | Game selection, facilitation guide |
| "Add leaderboards and achievements" | Leaderboard design, badge hierarchy |
| "Create a trading simulation" | Team roles, round structure, debrief |

**Handoff Pattern**:
```
/academy (Research + Design)
    │
    ├─► Invoke /gamifier for gamification design
    │       └─► Returns: Game design, points system, simulation plan
    │
    └─► Continue with ADDIE (Develop → Implement → Evaluate)
```

See [references/skill-integration.md](references/skill-integration.md) for detailed handoff patterns.

---

## Cooperative Integration

See [references/extracted-content.md](references/extracted-content.md) for details.
