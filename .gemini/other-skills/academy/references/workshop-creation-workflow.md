# Workshop Creation Workflow

Complete step-by-step workflow for creating live workshops and multi-day training programs in MoroAcademy.

---

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      WORKSHOP CREATION WORKFLOW                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  DECISION: Simple (1-4h) or Multi-Day (2-5 days)?                          │
│                                                                             │
│  STAGE 1      STAGE 2      STAGE 3       STAGE 4      STAGE 5             │
│  ANALYZE  →   DESIGN   →   DEVELOP   →  IMPLEMENT →  FACILITATE           │
│                                          & EVALUATE                        │
│  Workshop     Workshop     Workshop      Live         Workshop             │
│  Brief       Curriculum    Package      Workshop     Report                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## DECISION: Workshop Type

### Simple Workshop
- **Duration**: 1-4 hours
- **Format**: Single session, single topic
- **Structure**: No curriculum builder needed
- **Use when**: Orientation, demo, single skill training

### Multi-Day Workshop
- **Duration**: 2-5 days (8+ hours per day)
- **Format**: Multiple sessions across days
- **Structure**: Full Day → Module → Session hierarchy
- **Use when**: Comprehensive training, skill development program

```
IF duration <= 4 hours AND single topic:
    → SIMPLE workshop
ELSE IF duration > 4 hours OR multiple topics:
    → MULTI_DAY workshop
```

---

## STAGE 1: ANALYZE (Discovery)

**Goal**: Understand the training need and context

**Duration**: 1-2 days

### Step 1.1: Identify Training Need

Questions to answer:
- What problem are we solving?
- Is this a skills gap, compliance requirement, or certification need?
- What will participants DO differently after training?
- What is the organizational impact?

Output:
```
Training Need: [Enterprise development for cooperative managers]
Type: [Skills gap + certification]
Impact: [Improved business planning, sustainability]
Expected Change: [Create business plans, implement strategies]
```

### Step 1.2: Profile Participants

Questions to answer:
- Who are the participants? (role, level, organization)
- How many participants? (optimal: 15-30)
- What is their current knowledge?
- What motivates them to attend?

Output:
```
Participants: [Cooperative managers and board members]
Number: [25 participants (max 30)]
Current Level: [Mixed - some formal training, mostly experiential]
Motivation: [CDA compliance, business improvement, certification]
```

### Step 1.3: Determine Logistics

Questions to answer:
- Where will training be held? (venue capacity, equipment)
- What dates/times are available?
- What is the budget?
- What materials are needed?

Output:
```
Venue: [Hotel conference room, 50-person capacity]
Dates: [March 10-14, 2025]
Time: [8:00 AM - 5:00 PM daily]
Budget: [PHP 150,000]
Equipment: [Projector, flipcharts, breakout tables]
Materials: [Workbooks, templates, simulation materials]
```

### Step 1.4: Set Participant Limits

Recommendations:
- **Lecture-heavy**: Up to 50 participants
- **Interactive workshop**: 20-30 participants
- **Simulation/hands-on**: 15-25 participants
- **Coaching-intensive**: 10-15 participants

### Stage 1 Output: Workshop Brief

```markdown
# Workshop Brief: [Workshop Title]

## Training Need
- Problem: [What gap/need this addresses]
- Type: [Skills development / Compliance / Certification]
- Impact: [Expected organizational benefit]

## Participants
- Profile: [Role, organization type]
- Number: [X participants (max Y)]
- Current level: [Beginner/Intermediate/Mixed]
- Prerequisites: [What they should know before]

## Logistics
- Venue: [Location, capacity]
- Dates: [Start - End dates]
- Time: [Daily schedule]
- Budget: [Amount]

## Workshop Type
- [ ] SIMPLE (1-4 hours, single session)
- [x] MULTI_DAY (2+ days, structured curriculum)

## Success Criteria
- Attendance: 80%+ per session
- Assessment: 70%+ pass rate
- Satisfaction: 4/5+ rating
```

---

## STAGE 2: DESIGN (Blueprint)

**Goal**: Structure the curriculum and define outcomes

**Duration**: 2-5 days

### Step 2.1: Define Learning Outcomes

For workshops, focus on APPLICATION-level outcomes:

```
By the end of this workshop, participants will be able to:
1. [Create/Design/Develop] + [deliverable] + [using method]
2. [Apply/Implement/Demonstrate] + [skill] + [in context]
3. [Analyze/Evaluate] + [situation] + [to achieve goal]
```

Example:
```
1. Create a Lean Canvas business model for their enterprise
2. Apply pricing strategies based on cost and market analysis
3. Develop a 90-day action plan with measurable milestones
```

### Step 2.2: Select Methodologies

Choose from:

| Methodology | Best For | Duration |
|-------------|----------|----------|
| LECTURE | Concepts, theory | 20-30 min |
| WORKSHOP | Hands-on practice | 45-90 min |
| SIMULATION | Experiential learning | 60-120 min |
| GROUP_DISCUSSION | Sharing, synthesis | 15-30 min |
| GALLERY_WALK | Peer feedback | 30-45 min |
| CASE_STUDY | Problem analysis | 45-60 min |
| TEAM_ACTIVITY | Collaboration | 30-60 min |

Balance: 30% lecture / 70% active learning

### Step 2.3: Structure Days → Modules → Sessions

**Multi-Day Structure:**
```
Workshop: [Title]
├── Day 1: [Theme]
│   ├── Module 1: [Topic]
│   │   ├── Session: [Activity] (TYPE - duration)
│   │   └── Session: [Activity] (TYPE - duration)
│   └── Module 2: [Topic]
│       └── Session: [Activity] (TYPE - duration)
├── Day 2: [Theme]
│   └── [Modules and sessions...]
└── Day N: [Theme]
    └── [Modules and sessions...]
```

**Simple Workshop Structure:**
```
Workshop: [Title]
└── Day 1: [Theme]
    └── Module 1: [Topic]
        ├── Session: Introduction (LECTURE - 15 min)
        ├── Session: Main Content (LECTURE - 30 min)
        ├── Session: Activity (WORKSHOP - 60 min)
        └── Session: Wrap-up (GROUP_DISCUSSION - 15 min)
```

### Step 2.4: Plan Major Outputs

What will participants CREATE during the workshop?

Examples:
- SWOT Analysis document
- Lean Canvas
- Financial projection
- Marketing plan
- 90-Day Action Plan

Output deliverables should:
- Be practical and immediately useful
- Build on each other across days
- Have clear templates provided
- Include peer review component

### Step 2.5: Design Assessments

**Pre-Assessment**: Baseline knowledge (10-15 questions)
**Post-Assessment**: Learning validation (same questions + application)
**Session Assessments**: Template completion quality

### Stage 2 Output: Workshop Curriculum

```markdown
# Workshop Curriculum: [Workshop Title]

## Overview
- Duration: [X days]
- Participants: [X (max Y)]
- Type: [SIMPLE / MULTI_DAY]

## Learning Outcomes
1. [Outcome 1]
2. [Outcome 2]
3. [Outcome 3]

## Methodologies
- Lecture (30%)
- Workshop activities (40%)
- Simulation (15%)
- Group discussion (15%)

## Daily Structure

### Day 1: [Theme]
| Time | Module/Session | Type | Duration |
|------|----------------|------|----------|
| 8:00 | Opening | CEREMONY | 30 min |
| 8:30 | Module 1: [Topic] | | |
| | Session: [Title] | LECTURE | 45 min |
| | Session: [Title] | WORKSHOP | 60 min |
| 10:15 | Break | BREAK | 15 min |
| [Continue...] | | | |

[Repeat for each day]

## Major Outputs
1. [Output 1] - Template provided
2. [Output 2] - Template provided
3. [Output 3] - Template provided

## Assessment Plan
- Pre-assessment: [Description]
- Post-assessment: [Description]
- Passing criteria: [70% + completed outputs]
```

---

## STAGE 3: DEVELOP (Build Content)

**Goal**: Create all workshop materials

**Duration**: 1-3 weeks

### Step 3.1: Create Session Content Blocks

For each session, define content blocks:

```json
{
  "session_title": "Value Proposition Canvas Workshop",
  "type": "WORKSHOP",
  "duration_minutes": 90,
  "content_blocks": [
    {
      "type": "text",
      "title": "Introduction",
      "content": "Overview of the value proposition canvas...",
      "duration": 10
    },
    {
      "type": "activity",
      "title": "Complete Your Canvas",
      "instructions": "Using the template provided...",
      "duration": 50
    },
    {
      "type": "discussion",
      "title": "Share and Feedback",
      "prompts": ["What was your key insight?"],
      "duration": 30
    }
  ]
}
```

### Step 3.2: Write Facilitator Guides

For each session:

```markdown
# Facilitator Guide: [Session Title]

## Overview
- Duration: [X minutes]
- Type: [SESSION_TYPE]
- Module: [Parent module]

## Preparation
- [ ] [Material 1 ready]
- [ ] [Equipment set up]
- [ ] [Handouts printed]

## Script

### Opening (X min)
"Welcome to [session]. Today we will..."

### Main Activity (X min)
1. Explain the task: "[Instructions]"
2. Distribute materials
3. Allow [X] minutes for completion
4. Circulate and provide guidance

### Common Questions
- Q: [Anticipated question]
  A: [Response]

### Troubleshooting
- If participants struggle: [Alternative approach]
- If running behind: [What to cut]
- If running ahead: [Extension activity]

### Transition
"Now that we've completed [this], we'll move to..."
```

### Step 3.3: Design Templates

Create fillable templates for each output:

Template requirements:
- Clear instructions
- Structured sections
- Example content (if helpful)
- Space for participant notes
- Printable format (A4)

### Step 3.4: Configure Simulations (if applicable)

Simulation setup:
- Team structure
- Starting resources
- Round mechanics
- Scoring system
- Debrief questions

### Step 3.5: Prepare Materials List

```markdown
## Materials Checklist

### Per Participant
- [ ] Workbook/handout packet
- [ ] Name tag
- [ ] Pen and notebook
- [ ] Certificate folder

### Room Setup
- [ ] Projector and screen
- [ ] Flipcharts (X) with markers
- [ ] Tables in cluster arrangement
- [ ] Breakout areas marked

### Activity Materials
- [ ] [Simulation materials]
- [ ] [Template printouts]
- [ ] [Case study handouts]

### Digital
- [ ] Presentation slides
- [ ] Timer visible
- [ ] Attendance sheet
- [ ] Evaluation forms
```

### Stage 3 Output: Complete Workshop Package

```
Deliverables:
□ Session content blocks for all sessions
□ Facilitator guides written
□ Templates designed and printed
□ Simulation configured (if applicable)
□ Presentation slides created
□ Materials checklist complete
□ Pre/post assessments ready
□ Certificates prepared
```

---

## STAGE 4: IMPLEMENT (Launch)

**Goal**: Set up workshop and enable registration

**Duration**: 1-2 days

### Step 4.1: Build Curriculum in MoroAcademy

Invoke `/frontend` skill:
```
"Build the workshop curriculum pages for [Workshop Title] with:
- Day/Module/Session navigation
- Session content display
- Facilitator guide access
- Template downloads"
```

### Step 4.2: Set Up Registration

Options:
- **Open registration**: Anyone can register
- **Access code**: Requires code to register
- **Pre-registration**: Batch create from participant list

Configure:
- Registration deadline
- Max participants (with waitlist)
- Required information
- Confirmation email

### Step 4.3: Schedule Sessions

In MoroAcademy:
- Create schedule entries
- Set dates and times
- Assign venue/location
- Generate QR codes for attendance

### Step 4.4: Publish Workshop

- Set status to PUBLISHED
- Send invitations
- Share registration link
- Confirm logistics with venue

### Stage 4 Output: Live Workshop

```
Launch Checklist:
□ Curriculum uploaded
□ Registration configured
□ Schedule set
□ QR codes generated
□ Status: PUBLISHED
□ Invitations sent
□ Venue confirmed
□ Materials prepared
```

---

## STAGE 5: FACILITATE & EVALUATE

**Goal**: Deliver training and assess results

**Duration**: Workshop duration + 1 week follow-up

### Step 5.1: Pre-Workshop

Day before:
- [ ] Venue setup complete
- [ ] Materials in place
- [ ] Tech tested
- [ ] Team briefed

### Step 5.2: During Workshop

Daily:
- [ ] Attendance taken (QR code scan)
- [ ] Sessions delivered per guide
- [ ] Templates collected
- [ ] Adjustments noted

### Step 5.3: Attendance Management

Requirement: 80% attendance for certificate

Track:
- Per-session attendance
- Late arrivals/early departures
- Make-up arrangements (if applicable)

### Step 5.4: Collect Outputs

- Gather completed templates
- Review for quality
- Provide feedback
- Store for records

### Step 5.5: Run Assessments

- Pre-assessment (Day 1 morning)
- Post-assessment (Final day)
- Compare scores for learning gain

Learning Gain Formula:
```
Learning Gain = (Post - Pre) / (100 - Pre) × 100%
Target: 30%+ learning gain
```

### Step 5.6: Issue Certificates

Requirements:
- 80%+ attendance
- Completed major outputs
- Passed post-assessment (70%+)

Certificate data:
- Participant name
- Workshop title
- Date(s)
- Certificate number (auto-generated)

### Step 5.7: Gather Feedback

Evaluation form:
- Content relevance (1-5)
- Facilitator effectiveness (1-5)
- Materials quality (1-5)
- Venue/logistics (1-5)
- Overall satisfaction (1-5)
- Open comments

### Stage 5 Output: Workshop Report

```markdown
# Workshop Report: [Workshop Title]

## Overview
- Dates: [Start - End]
- Venue: [Location]
- Facilitators: [Names]

## Participation
- Registered: [X]
- Attended: [X] ([X%] attendance rate)
- Completed: [X] ([X%] completion rate)
- Certificates issued: [X]

## Learning Outcomes
- Pre-assessment average: [X%]
- Post-assessment average: [X%]
- Learning gain: [X%]

## Outputs Submitted
- [Output 1]: [X] submitted
- [Output 2]: [X] submitted
- [Output 3]: [X] submitted

## Evaluation Results
- Content: [X/5]
- Facilitator: [X/5]
- Materials: [X/5]
- Logistics: [X/5]
- Overall: [X/5]

## Key Feedback Themes
1. [Positive feedback theme]
2. [Improvement suggestion]
3. [Other observation]

## Lessons Learned
1. [What worked well]
2. [What to improve]
3. [Recommendations for future]

## Follow-up Actions
- [ ] Send certificates to absentees who qualify
- [ ] Share resources/materials
- [ ] Schedule follow-up check-in
- [ ] Update curriculum based on feedback
```

---

## Quick Reference Checklist

### Before You Start
- [ ] Training need clearly identified
- [ ] Workshop type decided (SIMPLE/MULTI_DAY)
- [ ] Participants defined
- [ ] Logistics confirmed

### During Design
- [ ] 3-5 application-level outcomes
- [ ] Mix of methodologies (30% lecture / 70% active)
- [ ] Major outputs defined
- [ ] Assessment plan set

### During Development
- [ ] All session content created
- [ ] Facilitator guides written
- [ ] Templates designed
- [ ] Materials checklist complete

### At Launch
- [ ] Registration open
- [ ] Schedule published
- [ ] Venue confirmed
- [ ] Team briefed

### During Delivery
- [ ] Attendance tracked
- [ ] Outputs collected
- [ ] Assessments administered
- [ ] Feedback gathered

### After Workshop
- [ ] Certificates issued
- [ ] Report compiled
- [ ] Follow-up scheduled
- [ ] Improvements noted

---

## Skill Integration Points

| When | Invoke | Purpose |
|------|--------|---------|
| Build UI | `/frontend` | Create curriculum pages |
| Create API | `/backend` | Add registration/attendance endpoints |
| Full feature | `/featuredev` | End-to-end implementation |
| UX review | `/ui-ux` | Improve participant experience |
| Debug | `/debugger` | Fix issues |
| Validate | `/build` + `/test` | Ensure quality |
