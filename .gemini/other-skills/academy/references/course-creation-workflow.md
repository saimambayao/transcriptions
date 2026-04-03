# Course Creation Workflow

Complete step-by-step workflow for creating self-paced online courses in MoroAcademy.

---

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    COURSE CREATION WORKFLOW                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  STAGE 1         STAGE 2         STAGE 3         STAGE 4   STAGE 5│
│  ANALYZE    →    DESIGN    →    DEVELOP    →   IMPLEMENT → EVALUATE│
│                                                                     │
│  Course Brief    Course          Course          Live       Course │
│  Document        Outline         Content         Course     Report │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## STAGE 1: ANALYZE (Discovery)

**Goal**: Understand the learning problem and context

**Duration**: 1-2 days

### Step 1.1: Identify Target Audience

Questions to answer:
- Who are the learners? (Cooperative managers, SE staff, government workers)
- What is their current knowledge level?
- What are their learning preferences?
- What constraints do they have? (time, internet, device)

Output:
```
Target Audience: [Cooperative managers in BARMM]
Current Level: [Beginner - limited formal business training]
Preferences: [Mobile-friendly, video content, local language]
Constraints: [Limited bandwidth, time available: 30 min/day]
```

### Step 1.2: Define Learning Problem/Gap

Questions to answer:
- What can they NOT do that they need to do?
- What skills/knowledge are missing?
- What is the business/organizational impact?
- Why does this matter?

Output:
```
Problem: [Cooperative managers lack basic financial management skills]
Impact: [Poor financial records, audit findings, compliance issues]
Gap: [Need to know: bookkeeping, financial statements, audit prep]
```

### Step 1.3: Assess Prerequisites

Questions to answer:
- What must learners already know?
- What skills are assumed?
- What technology access is required?

Output:
```
Prerequisites:
- Basic computer/smartphone skills
- Can read and write in English or Filipino
- Basic math (addition, subtraction, percentages)
- No prior accounting knowledge required
```

### Step 1.4: Determine Constraints

Questions to answer:
- How much time do learners have?
- What devices will they use?
- What bandwidth is available?
- What language(s) are needed?

Output:
```
Duration: 6-10 hours total (30 min sessions)
Device: Primarily mobile (Android)
Bandwidth: Variable (need offline-friendly options)
Language: Bilingual (English with Filipino explanations)
```

### Stage 1 Output: Course Brief Document

```markdown
# Course Brief: [Course Title]

## Target Audience
- Primary: [Description]
- Secondary: [Description]
- Estimated learners: [Number]

## Learning Problem
- Current state: [What learners cannot do]
- Desired state: [What learners will be able to do]
- Impact: [Business/organizational benefit]

## Prerequisites
- [Prerequisite 1]
- [Prerequisite 2]

## Constraints
- Duration: [X hours]
- Device: [Mobile/Desktop]
- Bandwidth: [High/Low]
- Language: [Language]

## Success Criteria
- Completion rate target: [60%+]
- Assessment pass rate: [70%+]
- Learner satisfaction: [4/5 stars]
```

---

## STAGE 2: DESIGN (Blueprint)

**Goal**: Structure the course and define learning outcomes

**Duration**: 2-3 days

### Step 2.1: Write Learning Objectives

Use Bloom's Taxonomy verbs:

| Level | Verbs | Example |
|-------|-------|---------|
| Remember | List, Define, Identify | "List the 7 cooperative principles" |
| Understand | Explain, Summarize | "Explain the purpose of member equity" |
| Apply | Calculate, Demonstrate | "Calculate patronage refund distribution" |
| Analyze | Compare, Differentiate | "Compare cooperative vs corporate governance" |
| Evaluate | Assess, Justify | "Evaluate financial health using ratios" |
| Create | Design, Develop | "Design a marketing plan" |

Format:
```
By the end of this course, learners will be able to:
1. [Action verb] + [specific content] + [condition]
2. [Action verb] + [specific content] + [condition]
3. [Action verb] + [specific content] + [condition]
```

### Step 2.2: Structure Modules

Recommended: 3-7 modules per course

Patterns:
- **Concept-to-Application**: What → Why → How → Apply
- **Progressive Complexity**: Basic → Intermediate → Advanced
- **Problem-Solution**: Problem → Analysis → Solutions → Implementation

Example:
```
Module 1: Introduction to Financial Management (1 hour)
Module 2: Basic Bookkeeping (2 hours)
Module 3: Financial Statements (2 hours)
Module 4: Analysis and Reporting (1.5 hours)
Module 5: Practical Application (1.5 hours)
```

### Step 2.3: Plan Lesson Sequence

For each module, plan lessons (4-6 lessons per module):

```
Module X: [Title]
├── Lesson X.1: [Topic] (VIDEO - 10 min)
├── Lesson X.2: [Topic] (TEXT - 10 min)
├── Lesson X.3: [Topic] (VIDEO - 8 min)
├── Lesson X.4: [Practice] (TEXT - 15 min)
└── Quiz X: [Assessment] (10 questions)
```

### Step 2.4: Design Assessment Strategy

**Formative (during learning):**
- End-of-module quizzes (5-10 questions)
- Reflection prompts
- Practice exercises

**Summative (end of course):**
- Final assessment (15-25 questions)
- Project/assignment (if applicable)
- Certificate criteria

### Step 2.5: Define Completion Criteria

```
Certificate Requirements:
- Complete 100% of lessons
- Pass all module quizzes (70% minimum)
- Pass final assessment (70% minimum)
- Total time: X hours
```

### Stage 2 Output: Course Outline

```markdown
# Course Outline: [Course Title]

## Course Overview
- Duration: [X hours]
- Modules: [X modules]
- Target Audience: [Description]
- Difficulty: [Beginner/Intermediate/Advanced]

## Learning Objectives
By the end of this course, learners will be able to:
1. [Objective 1]
2. [Objective 2]
3. [Objective 3]

## Module Structure

### Module 1: [Title] (X hours)
**Objective**: [Module objective]

| Lesson | Type | Duration | Topic |
|--------|------|----------|-------|
| 1.1 | VIDEO | 10 min | [Topic] |
| 1.2 | TEXT | 10 min | [Topic] |
| 1.3 | QUIZ | 10 min | Assessment |

[Repeat for each module]

## Assessment Plan
- Module quizzes: X questions each, 70% pass
- Final assessment: X questions, 70% pass
- Certificate: Requires 100% completion + passing scores
```

---

## STAGE 3: DEVELOP (Build Content)

**Goal**: Create all course content

**Duration**: 1-3 weeks (depending on course length)

### Step 3.1: Create Lesson Content

**VIDEO Lessons:**
- **Maximum duration: 15 minutes** (optimal: 8-12 minutes)
- One concept per video
- Include visuals, examples
- End with key takeaways
- Add captions

Script template:
```
VIDEO: [Lesson Title]
Duration: [X minutes]

INTRO (30 sec):
- Hook/attention grabber
- Learning objective for this lesson

CONTENT (X min):
- Point 1: [Explanation + Example]
- Point 2: [Explanation + Example]
- Point 3: [Explanation + Example]

SUMMARY (30 sec):
- Key takeaways (3 bullet points)
- Preview next lesson
```

**TEXT Lessons:**
- Length: 500-1000 words
- Reading level: Grade 8
- Use headers, bullets, short paragraphs
- Include images/diagrams
- Add practical examples

Template:
```markdown
# [Lesson Title]

## Introduction
[1-2 sentences on what this lesson covers]

## [Main Topic 1]
[Explanation with examples]

### Key Point
[Important concept to remember]

## [Main Topic 2]
[Explanation with examples]

## Practical Tip
[Real-world application advice]

## Summary
- [Key point 1]
- [Key point 2]
- [Key point 3]

## Next Steps
[What to do next / preview next lesson]
```

### Step 3.2: Create Quiz Questions

Question types:
- **Multiple Choice** (conceptual understanding)
- **True/False** (factual knowledge)
- **Fill in the Blank** (terminology)
- **Short Answer** (application - for assignments)

Per quiz:
- 5-10 questions
- 60% easy, 30% medium, 10% hard
- Include feedback for each answer

Template:
```
Question 1 (Easy):
[Question text]
A. [Option A]
B. [Option B] ← Correct
C. [Option C]
D. [Option D]

Feedback (Correct): [Explanation why B is correct]
Feedback (Incorrect): [Explanation of the correct answer]
```

### Step 3.3: Build Final Assessment

- 15-25 questions
- Cover all modules proportionally
- Mix of difficulty levels
- Time limit optional (recommend 1 hour)

### Step 3.4: Prepare Supporting Materials

- Downloadable templates/worksheets
- Reference documents
- Glossary of terms
- Additional resources list

### Stage 3 Output: Complete Course Content

```
Deliverables:
□ All video scripts written
□ All videos recorded/sourced
□ All text lessons written
□ All quiz questions created
□ Final assessment ready
□ Supporting materials prepared
□ Course thumbnail designed
□ Course description written
```

---

## STAGE 4: IMPLEMENT (Launch)

**Goal**: Publish course and enable enrollment

**Duration**: 1-2 days

### Step 4.1: Build Course in MoroAcademy

Invoke `/frontend` skill:
```
"Build the course detail page for [Course Title] with:
- Course overview section
- Module/lesson navigation
- Progress tracking
- Assessment integration"
```

### Step 4.2: Configure Settings

In MoroAcademy admin:
- Course visibility (PUBLIC/MEMBERS_ONLY/PRIVATE)
- Pricing (FREE or set price)
- Certificate settings
- Enrollment options

### Step 4.3: Test the Course

Before launch:
- [ ] All videos play correctly
- [ ] All text renders properly
- [ ] All quizzes function
- [ ] Progress tracking works
- [ ] Certificate generates correctly
- [ ] Mobile experience tested

### Step 4.4: Publish and Announce

- Set status to PUBLISHED
- Announce via appropriate channels
- Send invitations to target audience

### Stage 4 Output: Live Course

```
Launch Checklist:
□ Course content uploaded
□ Settings configured
□ Testing completed
□ Status: PUBLISHED
□ Announcement sent
□ Enrollment open
```

---

## STAGE 5: EVALUATE (Improve)

**Goal**: Monitor performance and iterate

**Duration**: Ongoing

### Step 5.1: Monitor Metrics

Key metrics to track:

| Metric | Target | Action if Below |
|--------|--------|-----------------|
| Enrollment rate | Growing | Improve marketing |
| Completion rate | 60%+ | Review drop-off points |
| Quiz pass rate | 70%+ | Clarify content |
| Assessment pass rate | 70%+ | Review difficulty |
| Ratings | 4/5+ | Address feedback |

### Step 5.2: Collect Feedback

Sources:
- Course ratings and reviews
- Learner comments
- Support questions
- Post-course surveys

### Step 5.3: Identify Improvements

Common issues:
- High drop-off at specific lessons → Improve content
- Low quiz scores → Clarify teaching
- Negative feedback → Address concerns
- Technical issues → Fix bugs

### Step 5.4: Iterate

Improvement cycle:
1. Analyze data monthly
2. Prioritize issues
3. Make updates
4. Track impact

### Stage 5 Output: Course Analytics Report

```markdown
# Course Analytics Report: [Course Title]

## Period: [Month/Quarter]

## Enrollment
- Total enrolled: [X]
- New this period: [X]
- Trend: [Up/Down/Stable]

## Completion
- Completed: [X] ([X%])
- In progress: [X]
- Dropped: [X]

## Performance
- Average quiz score: [X%]
- Assessment pass rate: [X%]
- Average rating: [X/5]

## Top Feedback Themes
1. [Theme 1]
2. [Theme 2]
3. [Theme 3]

## Actions Taken
- [Action 1]
- [Action 2]

## Next Steps
- [Improvement 1]
- [Improvement 2]
```

---

## Quick Reference Checklist

### Before You Start
- [ ] Clear learning problem identified
- [ ] Target audience defined
- [ ] Constraints understood
- [ ] Resources available

### During Design
- [ ] 3-5 measurable learning objectives
- [ ] 3-7 logical modules
- [ ] Mix of lesson types
- [ ] Assessment aligned to objectives

### During Development
- [ ] Videos maximum 15 minutes each (optimal: 8-12 minutes)
- [ ] Text at Grade 8 level
- [ ] Quizzes with feedback
- [ ] Mobile-friendly content

### At Launch
- [ ] Full testing completed
- [ ] Settings configured
- [ ] Announcement ready
- [ ] Support plan in place

### After Launch
- [ ] Monitoring dashboard set up
- [ ] Feedback collection active
- [ ] Improvement cycle scheduled

---

## Skill Integration Points

| When | Invoke | Purpose |
|------|--------|---------|
| Build UI | `/frontend` | Create course pages |
| Create API | `/backend` | Add endpoints |
| Full feature | `/featuredev` | End-to-end implementation |
| UX review | `/ui-ux` | Improve learner experience |
| Debug | `/debugger` | Fix issues |
| Validate | `/build` + `/test` | Ensure quality |
