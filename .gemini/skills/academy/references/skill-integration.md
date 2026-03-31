# Academy Skill Integration Guide

How to integrate the `/academy` skill with other skills in the CSEA skill ecosystem.

---

## Integration Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        SKILL INTEGRATION MAP                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│                          /academy                                       │
│                    (Instructional Design)                               │
│                             │                                           │
│         ┌───────────────────┼───────────────────┐                       │
│         │                   │                   │                       │
│         ▼                   ▼                   ▼                       │
│    /frontend           /backend           /featuredev                   │
│    (Build UI)         (Build API)        (Full Stack)                   │
│         │                   │                   │                       │
│         └───────────────────┴───────────────────┘                       │
│                             │                                           │
│         ┌───────────────────┼───────────────────┐                       │
│         ▼                   ▼                   ▼                       │
│      /ui-ux            /debugger          /build + /test                │
│    (UX Review)        (Fix Issues)       (Validate)                     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Skill Handoff Points

### /frontend

**When to invoke:**
- Building course/workshop detail pages
- Creating curriculum navigation UI
- Implementing enrollment flows
- Designing learner dashboards

**Trigger phrases:**
- "Build the course detail page"
- "Create workshop curriculum UI"
- "Implement lesson player"
- "Design progress tracker"

**Handoff information:**
```markdown
Invoke /frontend to build [component/page]:

## Context
- Building: [Course detail page / Workshop curriculum / etc.]
- Location: /academy/[path]
- Related models: Course, CourseModule, Lesson

## Requirements
- [Feature requirement 1]
- [Feature requirement 2]
- [Feature requirement 3]

## Data Structure
[Provide TypeScript interface or sample data]

## UI Components Needed
- [Component 1]
- [Component 2]
- [Component 3]

## Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
```

---

### /backend

**When to invoke:**
- Creating new API endpoints
- Modifying database models
- Implementing business logic
- Setting up authentication/authorization

**Trigger phrases:**
- "Create enrollment API"
- "Add assessment submission endpoint"
- "Implement certificate generation"
- "Build progress tracking API"

**Handoff information:**
```markdown
Invoke /backend to implement [feature]:

## Context
- Feature: [Enrollment API / Assessment endpoint / etc.]
- App: training
- Related models: [Model names]

## API Endpoints Needed
| Method | Path | Description |
|--------|------|-------------|
| POST | /api/training/[path] | [Purpose] |
| GET | /api/training/[path] | [Purpose] |

## Business Logic
- [Logic requirement 1]
- [Logic requirement 2]

## Data Validation
- [Validation rule 1]
- [Validation rule 2]

## Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
```

---

### /featuredev

**When to invoke:**
- Implementing complete features (frontend + backend)
- Building new capabilities from scratch
- Major enhancements to existing features

**Trigger phrases:**
- "Implement complete enrollment flow"
- "Build simulation game feature"
- "Add certificate generation end-to-end"
- "Create workshop attendance system"

**Handoff information:**
```markdown
Invoke /featuredev to implement [feature]:

## User Story
As a [user type], I want to [action] so that [benefit].

## Context
- Feature: [Feature name]
- Affects: [Frontend / Backend / Both]
- Related: [Existing features it integrates with]

## Requirements
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

## Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

## Technical Notes
- [Consideration 1]
- [Consideration 2]
```

---

### /ui-ux

**When to invoke:**
- Designing user journeys
- Improving learner experience
- Reviewing accessibility
- Optimizing conversion flows

**Trigger phrases:**
- "Design course discovery flow"
- "Optimize enrollment experience"
- "Review learner dashboard UX"
- "Improve workshop registration"

**Handoff information:**
```markdown
Invoke /ui-ux to design/review [journey]:

## Context
- Journey: [Course discovery / Enrollment / etc.]
- Users: [Learner / Trainer / Admin]
- Current state: [Description or screenshots]

## Pain Points
- [Issue 1]
- [Issue 2]

## Goals
- [Goal 1: e.g., reduce time to enroll]
- [Goal 2: e.g., improve completion rate]

## Constraints
- [Constraint 1]
- [Constraint 2]

## Success Metrics
- [Metric 1]
- [Metric 2]
```

---

### /debugger

**When to invoke:**
- Fixing bugs in academy features
- Investigating errors
- Troubleshooting issues

**Trigger phrases:**
- "Debug enrollment failure"
- "Fix certificate generation error"
- "Investigate progress tracking issue"
- "Troubleshoot quiz submission"

**Handoff information:**
```markdown
Invoke /debugger to investigate [issue]:

## Issue Description
[What's happening vs what should happen]

## Error Details
- Error message: [If any]
- Location: [File/endpoint]
- Frequency: [Always / Sometimes / Once]

## Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Expected Behavior
[What should happen]

## Actual Behavior
[What's happening]

## Environment
- Browser: [If applicable]
- User type: [Learner / Admin]
- Test data: [If applicable]
```

---

### /build + /test

**When to invoke:**
- Before deploying new features
- After making changes
- For quality validation

**Trigger phrases:**
- "Run tests for training app"
- "Validate enrollment feature"
- "Check for regressions"
- "Build and test"

**Handoff information:**
```markdown
Invoke /build and /test to validate:

## Scope
- Feature: [Feature name]
- Files changed: [List of files]
- App: training

## Test Scenarios
- [ ] [Scenario 1]
- [ ] [Scenario 2]
- [ ] [Scenario 3]

## Expected Outcomes
- All tests pass
- No type errors
- Build succeeds
```

---

## Integration Workflow Examples

### Example 1: Create New Course Type

```
Step 1: /academy (Design)
"Design curriculum structure for a micro-course format (30 min total)"
Output: Course outline, lesson structure

Step 2: /backend (API)
"Create API endpoints for micro-course with time-boxed lessons"
Output: New endpoints, model updates

Step 3: /frontend (UI)
"Build micro-course player with countdown timer"
Output: Course player UI

Step 4: /build + /test (Validate)
"Test micro-course end-to-end"
Output: Validated feature

Step 5: /academy (Evaluate)
"Review micro-course design based on initial testing"
Output: Refinements
```

### Example 2: Add Workshop Simulation

```
Step 1: /academy (Design)
"Design simulation game for supply chain workshop"
Output: Game mechanics, rules, scoring

Step 2: /featuredev (Full Implementation)
"Implement supply chain simulation with team management and rounds"
Output: Complete simulation feature

Step 3: /ui-ux (Review)
"Review simulation UX for mobile participants"
Output: UX improvements

Step 4: /test (Validate)
"Test simulation with multiple concurrent teams"
Output: Performance validation
```

### Example 3: Fix Enrollment Issue

```
Step 1: /debugger (Investigate)
"Debug: Users getting error when enrolling in paid courses"
Output: Root cause identified

Step 2: /backend (Fix)
"Fix payment validation in enrollment endpoint"
Output: Bug fix

Step 3: /test (Validate)
"Test enrollment flow for paid courses"
Output: Fix confirmed
```

---

## Quick Reference

| Task | Primary Skill | Supporting Skills |
|------|---------------|-------------------|
| Design course | /academy | - |
| Design workshop | /academy | - |
| Build UI | /frontend | /ui-ux |
| Build API | /backend | - |
| Full feature | /featuredev | /frontend, /backend |
| Fix bugs | /debugger | /backend, /frontend |
| Validate | /build + /test | - |
| UX review | /ui-ux | /academy |

---

## Best Practices

### 1. Always Start with Design
- Use /academy to design before building
- Have clear learning objectives
- Define assessment strategy

### 2. Provide Context
- Always include relevant context when handing off
- Reference data structures and models
- Specify acceptance criteria

### 3. Validate Before Deploy
- Always run /build + /test after changes
- Check for regressions
- Test on mobile if applicable

### 4. Iterate Based on Data
- Use /academy to evaluate after launch
- Track completion and engagement metrics
- Refine based on learner feedback

---

## Related Files

- [course-creation-workflow.md](course-creation-workflow.md) - Course workflow
- [workshop-creation-workflow.md](workshop-creation-workflow.md) - Workshop workflow
- [templates/](templates/) - Content templates
