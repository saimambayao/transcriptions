---
name: appmanager
description: Orchestrates all skills throughout the application lifecycle (architecture, development, testing, deployment, maintenance). Provides skill discovery, workflow recommendations, state tracking, and lifecycle-aware task management. Use when unsure which skill to use, planning multi-step workflows, or managing complex tasks spanning multiple skills. Recommends skills and asks user permission before invoking.
argument-hint: "[topic]"
---

# AppManager

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's orchestration request                    ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Overview

AppManager is the central orchestration skill for Bangsamoro Development Platform development. It discovers all available skills in `.gemini/skills/`, recommends appropriate skills based on the current task or lifecycle phase, tracks workflow state across multi-step processes, and ensures skills are used effectively throughout the architecture, development, testing, deployment, and maintenance of CSEA.

**Core Philosophy**: AppManager **recommends and guides**, but the user **explicitly invokes** each skill. AppManager never auto-invokes skills without permission.

## Tech Stack

**Frontend:** Next.js 16+, React 19+, TypeScript, TanStack Query, Tailwind CSS v4, shadcn/ui

**Backend:** Django 6.0, Django Ninja APIs, PostgreSQL 18, Python 3.14

**Deployment:** Railway (Docker-based), GitHub Actions CI/CD

## Core Capabilities

### 1. Skill Discovery and Cataloging

AppManager uses a **hybrid discovery strategy**:

1. **Static Catalog**: Maintains a catalog of known CSEA skills in `references/skill-catalog.md` with their purposes, triggers, and integration points.
2. **Dynamic Detection**: Scans `.gemini/skills/` directory to detect new skills and parse YAML frontmatter metadata.

**When to Use**:
- Beginning of a conversation to understand available skills
- After new skills are added to `.gemini/skills/`
- When user asks "what skills are available?"
- When deciding which skill to recommend

**Workflow**:
1. Read static catalog from `references/skill-catalog.md`
2. Scan `.gemini/skills/` directory for all skill directories
3. For each skill, attempt to parse YAML frontmatter from SKILL.md
4. Compare static catalog with detected skills
5. Report any new skills or missing skills
6. Update understanding of available capabilities

### 2. Workflow Orchestration

AppManager recommends multi-skill workflows for common CSEA tasks. It provides **balanced detail** with clear decision points, allowing the user to understand the workflow while maintaining control.

**Workflow Patterns** (see `references/workflow-templates.md`):
- **New Feature Development**: safety-first → featuredev → frontend → backend → unit-tests → integration-tests → coditor → devops
- **Bug Fix**: investigator → debugger → unit-tests → coditor → devops
- **Deployment**: coditor → devops → (user performs deployment manually)
- **Security Enhancement**: security → coditor → unit-tests → devops
- **Database Migration**: database → safety-first → unit-tests → integration-tests → devops

**Recommendation Style**:
```
Based on your request to [task description], I recommend this workflow:

1. **Phase 1: Investigation** (10-15 min)
   - Invoke /investigator to research [specific issue]
   - Expected outcome: 3 solution alternatives with evidence

   Shall I invoke /investigator now? (y/n)

2. **Phase 2: Implementation** (after investigator completes)
   - Invoke /backend to implement [specific change]
   - Expected outcome: Updated models/APIs

3. **Phase 3: Verification** (after implementation)
   - Invoke /unit-tests to verify changes
   - Invoke /coditor for security audit

Would you like to proceed with Phase 1?
```

**Key Principle**: Ask permission before each major phase or skill invocation.

### 3. Workflow State Tracking (Mandatory)

AppManager **tracks where you are** in multi-step workflows, remembering completed steps and suggesting next steps.

**State Tracking Mechanism**:
- Uses conversation memory to track workflow progress
- Explicitly states current phase and completed steps
- Reminds user of next recommended step
- Allows resumption after interruptions

**Example**:
```
[Workflow State]
✓ Completed: /investigator (found 3 solutions)
✓ Completed: /backend (implemented Solution #2)
→ Current: /unit-tests (running tests)
⏭ Next: /coditor (security audit)
```

**When Resuming**:
```
I see we're in the middle of the Bug Fix workflow. We've completed:
- /investigator: Identified root cause (multi-tenant data leak)
- /backend: Implemented organization filter fix

Next recommended step: Run /unit-tests to verify the fix.

Shall I invoke /unit-tests now?
```

### 4. Lifecycle Phase Detection

AppManager detects the current Software Development Lifecycle (SDLC) phase and recommends phase-appropriate skills.

**SDLC Phases** (see `references/lifecycle-workflows.md`):

| Phase | Indicators | Recommended Skills |
|-------|-----------|-------------------|
| **Architecture** | "design", "plan", "architect", "structure" | architect, featuredev (planning mode), database |
| **Development** | "implement", "build", "create", "add feature" | featuredev, backend, frontend, database, ai-engineer |
| **Testing** | "test", "verify", "check", completed implementation | unit-tests, integration-tests, e2e-tests, component-tests |
| **Deployment** | "deploy", "release", "push to staging/production" | coditor (audit first!), devops, safety-first |
| **Maintenance** | "fix", "debug", "investigate", "error", "issue" | investigator, debugger, refactor, coditor |
| **Operations** | "monitor", "optimize", "performance", "scaling" | devops, apptimizer |

**Phase Detection Workflow**:
1. Analyze user's request for phase indicators
2. Check conversation history for context (e.g., just finished implementation → testing phase)
3. Identify current lifecycle phase
4. Recommend phase-appropriate skills
5. Suggest transition to next phase when appropriate

### 5. Skill Health Checks

AppManager verifies that skills are correctly structured and functional before recommending them.

**Health Check Criteria**:
- SKILL.md exists and has valid YAML frontmatter
- Required directories exist (scripts/, references/, assets/ as declared)
- Referenced files in SKILL.md exist
- No broken links to non-existent files

**Health Check Workflow**:
1. Read SKILL.md for the skill
2. Verify YAML frontmatter parses correctly
3. Check for referenced files (e.g., "See `references/foo.md`")
4. Report any issues: missing files, broken links, invalid structure
5. Mark skill as healthy ✓ or needs attention ⚠

**When to Run**:
- Before recommending a skill for the first time in a conversation
- When user asks "are skills working correctly?"
- After skill updates or modifications

### 6. Skill Selection and Recommendation

AppManager uses a decision tree approach to recommend the right skill(s) for the task at hand.

**Selection Criteria** (see `references/skill-selection-guide.md`):
- **Task Type**: Feature, bug, deployment, investigation, optimization
- **Domain**: Frontend (Next.js/React), Backend (Django Ninja), Database, AI, Security, DevOps
- **Lifecycle Phase**: Architecture, development, testing, deployment, maintenance
- **Urgency**: Critical (production issue), high (user-facing bug), normal, low
- **Complexity**: Simple (1 skill), moderate (2-3 skills), complex (full workflow)

**Recommendation Process**:
1. **Analyze Request**: Extract task type, domain, urgency, complexity
2. **Detect Phase**: Determine current SDLC phase
3. **Select Skills**: Use decision tree to identify 1-3 relevant skills
4. **Order Skills**: Sequence skills logically (e.g., safety-first before database migration)
5. **Present Recommendation**: Explain why each skill is relevant
6. **Ask Permission**: "Shall I invoke /[skill-name] now?"

**Example Decision Tree**:
```
User says: "The cooperative list isn't loading properly"

1. Task Type: Bug (maintenance phase)
2. Domain: Frontend (React/Next.js)
3. Urgency: High (user-facing)
4. Complexity: Moderate (might need backend check too)

Recommended Workflow:
- /investigator → Research TanStack Query patterns, identify issue
- /debugger → Systematic debugging workflow
- /frontend → Fix React component or query hook
- /unit-tests → Verify fix
- /coditor → Audit for similar issues

Presenting: "This appears to be a frontend data fetching issue. I recommend starting with /investigator to research the problem. Shall I invoke /investigator now?"
```

## Pre-Built Workflow Templates

AppManager includes ready-to-use workflow templates for common CSEA tasks (see `references/workflow-templates.md`).

**Available Templates**:

### Template 1: New Feature Development

**Trigger**: User requests a new feature or capability

**Workflow**:
1. `/safety-first` - Verify git status, database safety
2. `/featuredev` - Feature-Driven Development workflow (plan, model, build, test)
3. `/frontend` - Build Next.js/React UI components (frontend-first approach)
4. `/backend` - Implement Django Ninja APIs
5. `/unit-tests` - Verify unit tests pass
6. `/integration-tests` - Verify integration tests pass
7. `/coditor` - Comprehensive audit before deployment
8. `/devops` - Deployment guidance (user executes manually)

**Decision Points**:
- After safety-first: Proceed or resolve blockers?
- After featuredev planning: User approves plan?
- After implementation: Tests pass? If not, debug before proceeding
- After coditor: Any Critical/High findings? Fix before deployment
- Before devops: User ready to deploy?

### Template 2: Bug Fix

**Trigger**: User reports a bug, error, or issue

**Workflow**:
1. `/investigator` - Research issue, gather evidence, propose solutions
2. `/debugger` - Systematic debugging (7-Step methodology)
3. `/frontend` or `/backend` - Implement fix (depending on domain)
4. `/unit-tests` - Verify fix doesn't break existing tests
5. `/coditor` - Audit for related issues
6. `/devops` - Deployment guidance

**Decision Points**:
- After investigator: Which solution to implement?
- After implementation: Tests pass?
- After coditor: Any related issues found? Fix now or later?

### Template 3: Deployment (Staging/Production)

**Trigger**: User says "deploy to staging" or "deploy to production"

**Workflow**:
1. `/safety-first` - **MANDATORY** - Verify no uncommitted changes
2. `/coditor` - **MANDATORY** - Comprehensive audit (all Critical/High fixed)
3. `/unit-tests` - **MANDATORY** - All tests pass
4. `/integration-tests` - **MANDATORY** - Integration tests pass
5. `/devops` - Deployment guidance (user executes `git push` manually)

**Critical Safety Checks**:
- No uncommitted files
- All migrations tested
- Critical findings = 0
- High findings = 0
- Test coverage adequate

**Decision Point**: If ANY safety check fails, STOP and resolve before proceeding.

### Template 4: Database Migration

**Trigger**: User modifies Django models or requests database changes

**Workflow**:
1. `/safety-first` - Verify database safety, git status
2. `/database` - Review migration, check for data loss risks
3. `/backend` - Review model changes
4. `/unit-tests` - Test migration locally
5. `/integration-tests` - Test migration integration
6. `/coditor` - Audit migration for issues
7. `/devops` - Deployment guidance (test on staging first!)

**Critical Checks**:
- No data deletion (or explicit backup taken)
- Migrations tested locally
- Migrations tested on staging before production
- Auto-migration configured for Railway deployment

### Template 5: Security Enhancement

**Trigger**: User requests security feature or fix

**Workflow**:
1. `/security` - Security implementation patterns (JWT, multi-tenant, XSS, etc.)
2. `/backend` - Implement Django Ninja security changes
3. `/frontend` - Update Next.js middleware or components
4. `/unit-tests` - Security-focused tests
5. `/coditor` - Security audit
6. `/devops` - Deployment guidance

**Focus Areas**:
- JWT authentication
- Multi-tenant data isolation
- Input validation
- XSS prevention in React components

### Template 6: AI Feature

**Trigger**: User requests AI-powered feature

**Workflow**:
1. `/ai-engineer` - LLM integration, RAG patterns, prompt engineering
2. `/backend` - Django Ninja API for AI features
3. `/frontend` - React UI for AI chat/features
4. `/unit-tests` - Test AI functions
5. `/coditor` - Audit AI implementation
6. `/devops` - Deployment guidance

**Considerations**:
- Multi-tenant isolation for AI features
- Token usage optimization
- Gemini API integration patterns

## Workflow State Tracking System

AppManager maintains workflow state using structured tracking in conversation memory.

**State Structure**:
```markdown
[Workflow: New Feature Development]
Current Step: 3/8

✓ 1. /safety-first - Completed (no blockers)
✓ 2. /featuredev - Completed (feature plan approved)
→ 3. /frontend - In Progress (building React components)
⏭ 4. /backend - Pending
⏭ 5. /unit-tests - Pending
⏭ 6. /integration-tests - Pending
⏭ 7. /coditor - Pending
⏭ 8. /devops - Pending

Next Action: Complete frontend implementation, then invoke /backend
```

**State Updates**:
- After each skill completes: Update status to ✓
- When user approves next step: Update status to →
- Explicitly state next action

**Resumption Example**:
```
I see we were working on the New Feature Development workflow. Here's where we are:

✓ Completed: /safety-first, /featuredev (plan approved), /frontend (components built)
→ Last step: /backend (API implementation started)

We have the React components ready. Next, we need to complete the Django Ninja API endpoints.

Would you like to continue with the backend implementation?
```

## Skill Invocation Pattern

AppManager follows this pattern when recommending skills:

**Step 1: Analyze and Recommend**
```
Based on your request to [task], I detect we're in the [SDLC Phase] phase.

I recommend this approach:
- /[skill-name]: [Why this skill is relevant, what it will do]
- Expected outcome: [What user can expect]
```

**Step 2: Ask Permission**
```
Shall I invoke /[skill-name] now? (y/n)
```

**Step 3: Track State**
```
[After skill completes]
✓ /[skill-name] completed: [Brief summary of outcome]

Next recommended step: /[next-skill]
Would you like to proceed?
```

**Step 4: Repeat for Each Skill**

**Never**:
- Auto-invoke multiple skills in sequence
- Assume user approval
- Skip permission for skill invocation

## Integration with CSEA Workflows

AppManager integrates with CSEA-specific workflows and rules:

### Integration 1: GEMINI.md Critical Rules

AppManager enforces GEMINI.md rules through skill recommendations:

- **Rule**: Ask permission before committing → AppManager never auto-invokes skills without permission
- **Rule**: Frontend-first development → Workflow templates prioritize frontend implementation
- **Rule**: No purple colors → Skills enforce Negosyo Blue (#0056D2) usage
- **Rule**: Files under 1000 lines → Skills check file length

### Integration 2: Three-Portal Architecture

AppManager understands CSEA's three-portal structure:

| Portal | Route | Skills |
|--------|-------|--------|
| Public Portal | `/` | frontend, backend (public APIs) |
| C/SE Portal | `/portal` | frontend, backend, compliance |
| CSEA Staff Portal | `/csea` | frontend, backend, admin features |

### Integration 3: Railway Deployment

AppManager integrates with Railway deployment workflow:

- Auto-migration on deploy (configured in Dockerfile)
- Docker-based deployment for both frontend and backend
- Environment variable verification

## Resources

### references/

**skill-catalog.md**: Static catalog of all known CSEA skills with purposes, triggers, and integration points.

**lifecycle-workflows.md**: Detailed SDLC phase mapping with indicators, recommended skills per phase, and transition criteria.

**skill-selection-guide.md**: Decision trees and selection criteria for choosing the right skill(s).

**workflow-templates.md**: Pre-built workflow templates for common CSEA tasks.

---

## Quick Start Examples

See [workflow-templates.md](references/workflow-templates.md) for examples of new feature, bug fix, and deployment workflows.

