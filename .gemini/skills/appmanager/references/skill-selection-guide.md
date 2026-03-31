# OBCMS Skill Selection Guide

**Purpose**: Decision trees and selection criteria for choosing the right skill(s) based on task type, domain, urgency, and complexity.

**Use**: AppManager uses this guide to recommend appropriate skills for user requests.

---

## Selection Framework

AppManager uses a multi-dimensional framework to select skills:

1. **Task Type**: What kind of work is being requested?
2. **Domain**: Which technical area does it involve?
3. **Lifecycle Phase**: Where are we in the SDLC?
4. **Urgency**: How quickly does it need to be done?
5. **Complexity**: How many skills/steps are needed?

---

## Dimension 1: Task Type

### Task Type Classification

| Task Type | Indicators | Primary Skill(s) |
|-----------|-----------|------------------|
| **New Feature** | "add", "create new", "implement feature", "build" | featuredev, architect |
| **Bug Fix** | "fix", "broken", "not working", "error", "bug" | investigator, debugger |
| **Investigation** | "why", "investigate", "research", "find out" | investigator |
| **Refactoring** | "refactor", "improve", "optimize code", "clean up" | refactor, coditor |
| **Deployment** | "deploy", "release", "push to", "go live" | devops, safety-first, coditor |
| **Database Change** | "migration", "schema", "database", "model change" | database, safety-first |
| **Security** | "security", "vulnerability", "CSP", "auth", "permissions" | security |
| **Testing** | "test", "verify", "check coverage" | unit-tests, integration-tests |
| **Performance** | "slow", "optimize", "performance", "speed up" | database, backend, frontend |
| **Documentation** | "document", "explain", "write docs" | (no specific skill) |

### Task Type Decision Tree

```
User Request
    │
    ├─ Contains "add", "create new", "implement", "build"?
    │   └─ YES → NEW FEATURE
    │       └─ Recommend: featuredev, architect (planning)
    │
    ├─ Contains "fix", "broken", "error", "bug"?
    │   └─ YES → BUG FIX
    │       └─ Recommend: investigator → debugger
    │
    ├─ Contains "deploy", "release", "push to"?
    │   └─ YES → DEPLOYMENT
    │       └─ Recommend: safety-first → coditor → devops
    │
    ├─ Contains "migration", "database", "schema"?
    │   └─ YES → DATABASE CHANGE
    │       └─ Recommend: database, safety-first
    │
    ├─ Contains "security", "CSP", "auth", "vulnerability"?
    │   └─ YES → SECURITY
    │       └─ Recommend: security, coditor
    │
    ├─ Contains "test", "verify", "coverage"?
    │   └─ YES → TESTING
    │       └─ Recommend: unit-tests, integration-tests
    │
    ├─ Contains "slow", "optimize", "performance"?
    │   └─ YES → PERFORMANCE
    │       └─ Recommend: (domain-specific) + coditor
    │
    └─ Contains "why", "investigate", "research"?
        └─ YES → INVESTIGATION
            └─ Recommend: investigator
```

---

## Dimension 2: Domain

### Domain Classification

| Domain | Indicators | Primary Skill(s) |
|--------|-----------|------------------|
| **Backend** | "models", "views", "API", "Django", "DRF", "Celery" | backend, database |
| **Frontend** | "UI", "template", "HTMX", "Tailwind", "Alpine.js" | frontend, frontend-component-scaffolder |
| **Database** | "query", "migration", "schema", "PostgreSQL", "ORM" | database, backend |
| **AI** | "AI", "obcAI", "LLM", "agent", "ADK" | obcai-engineer, ai-engineer |
| **Security** | "CSP", "auth", "permissions", "XSS", "multi-tenant" | security |
| **DevOps** | "deploy", "Railway", "infrastructure", "environment" | devops |
| **Testing** | "test", "coverage", "verify" | unit-tests, integration-tests, e2e-tests |
| **Full-Stack** | "feature", "end-to-end" | featuredev (coordinates all) |

### Domain Decision Tree

```
User Request
    │
    ├─ Contains "models", "views", "API", "serializers"?
    │   └─ YES → BACKEND DOMAIN
    │       └─ Recommend: backend, database
    │
    ├─ Contains "UI", "template", "HTMX", "Tailwind"?
    │   └─ YES → FRONTEND DOMAIN
    │       └─ Recommend: frontend, frontend-component-scaffolder
    │
    ├─ Contains "obcAI", "ADK", "agent", "specialist"?
    │   └─ YES → AI DOMAIN (obcAI)
    │       └─ Recommend: obcai-engineer, backend (integration)
    │
    ├─ Contains "AI", "LLM", "Claude", "prompt"?
    │   └─ YES → AI DOMAIN (General)
    │       └─ Recommend: ai-engineer, backend
    │
    ├─ Contains "CSP", "auth", "permissions", "security"?
    │   └─ YES → SECURITY DOMAIN
    │       └─ Recommend: security, (backend|frontend)
    │
    ├─ Contains "deploy", "Railway", "production", "staging"?
    │   └─ YES → DEVOPS DOMAIN
    │       └─ Recommend: devops, safety-first
    │
    └─ Contains "feature", "end-to-end", "full implementation"?
        └─ YES → FULL-STACK DOMAIN
            └─ Recommend: featuredev (orchestrates all domains)
```

---

## Dimension 3: Lifecycle Phase

### Phase-Based Skill Selection

| Phase | Primary Skills | Supporting Skills |
|-------|---------------|-------------------|
| **Architecture** | architect, featuredev (planning) | database, prompter, investigator |
| **Development** | backend, frontend, database | featuredev, security, obcai-engineer |
| **Testing** | unit-tests, integration-tests | e2e-tests, component-tests, debugger |
| **Deployment** | safety-first, coditor, devops | unit-tests, integration-tests |
| **Maintenance** | investigator, debugger | backend, frontend, refactor |
| **Operations** | devops, database (optimization) | backend, frontend, coditor |

### Phase Detection → Skill Selection

**Example 1: Architecture Phase**
```
User: "Design a multi-stakeholder partnership tracking system"

Detection:
- Task Type: New Feature
- Domain: Full-Stack
- Phase: Architecture (keyword: "design")

Recommended Skills:
1. architect (primary) - Architectural planning
2. database (supporting) - Schema design
3. featuredev (supporting) - Feature modeling

Workflow: architect → database → featuredev (planning mode)
```

**Example 2: Maintenance Phase**
```
User: "Users are seeing tasks from other organizations"

Detection:
- Task Type: Bug Fix (Critical - security issue)
- Domain: Backend + Security
- Phase: Maintenance

Recommended Skills:
1. investigator (primary) - Research multi-tenant patterns
2. security (primary) - Multi-tenant security patterns
3. debugger (supporting) - Root cause analysis
4. backend (supporting) - Fix organization filtering

Workflow: investigator → security → debugger → backend
```

---

## Dimension 4: Urgency

### Urgency Levels

| Urgency | Criteria | Response | Workflow Adjustment |
|---------|----------|----------|---------------------|
| **Critical** | Production down, data leak, security breach | Immediate | Skip planning, go straight to fix |
| **High** | User-facing bug, broken feature | Same day | Shortened workflow, focus on fix |
| **Normal** | Non-critical bug, new feature | 1-2 sprints | Full workflow, proper testing |
| **Low** | Nice-to-have, optimization | When convenient | Can be batched, planned for later |

### Urgency-Based Skill Selection

**Critical Urgency**:
```
Indicators: "production down", "data leak", "security breach", "users can't"

Workflow Adjustment:
- SKIP: architect, featuredev planning
- PRIORITY: investigator (quick research), debugger (fast), immediate fix
- EXPEDITE: testing (focused), deployment (ASAP)

Example:
User: "Production is down! 500 errors everywhere!"

Workflow: investigator (quick) → debugger → fix → unit-tests (critical paths) → deploy ASAP
```

**High Urgency**:
```
Indicators: "broken feature", "users complaining", "not working"

Workflow Adjustment:
- REDUCE: Planning time (quick plan)
- PRIORITY: investigator, debugger, fix
- NORMAL: testing, deployment

Example:
User: "Task deletion isn't working"

Workflow: investigator → debugger → frontend fix → unit-tests → deploy (same day)
```

**Normal Urgency**:
```
Indicators: "add feature", "improve", regular development

Workflow: Full lifecycle, no shortcuts

Example:
User: "Add resource booking calendar"

Workflow: architect → featuredev → frontend → backend → tests → coditor → deploy
```

**Low Urgency**:
```
Indicators: "when you have time", "nice to have", "optimization"

Workflow: Can be batched, planned for later sprints

Example:
User: "Optimize the dashboard query when you get a chance"

Workflow: Add to backlog, plan optimization sprint, full workflow when scheduled
```

---

## Dimension 5: Complexity

### Complexity Classification

| Complexity | Skill Count | Decision |
|-----------|-------------|----------|
| **Simple** | 1 skill | Single skill invocation |
| **Moderate** | 2-3 skills | Short workflow |
| **Complex** | 4+ skills | Full workflow with state tracking |

### Complexity Decision Tree

```
User Request
    │
    ├─ Single domain, clear solution?
    │   └─ YES → SIMPLE (1 skill)
    │       Example: "Run tests" → unit-tests only
    │
    ├─ 2-3 domains, known pattern?
    │   └─ YES → MODERATE (2-3 skills)
    │       Example: "Fix the delete button" → investigator → frontend → unit-tests
    │
    └─ Multi-domain, new feature, or deployment?
        └─ YES → COMPLEX (4+ skills, full workflow)
            Example: "Add booking calendar" → featuredev → frontend → backend → tests → coditor → devops
```

### Complexity-Based Examples

**Simple (1 skill)**:
```
User: "Run tests"
Complexity: Simple
Skills: unit-tests
Workflow: unit-tests → done
```

**Moderate (2-3 skills)**:
```
User: "Fix the task deletion button in kanban view"
Complexity: Moderate
Skills: investigator → frontend → unit-tests
Workflow:
1. investigator - Research HTMX deletion patterns
2. frontend - Fix HTMX targeting
3. unit-tests - Verify fix
```

**Complex (4+ skills, full workflow)**:
```
User: "Add resource booking calendar to coordination module"
Complexity: Complex
Skills: featuredev → frontend → backend → unit-tests → integration-tests → coditor → devops
Workflow:
1. featuredev - Plan feature (FDD)
2. frontend - Build FullCalendar UI
3. backend - Implement booking models/API
4. unit-tests - Test functionality
5. integration-tests - Test workflow
6. coditor - Pre-deployment audit
7. devops - Deployment guidance
```

---

## Multi-Dimensional Selection Examples

### Example 1: Critical Bug Fix

**User**: "Production is broken! Users are seeing other organizations' data!"

**Analysis**:
- **Task Type**: Bug Fix
- **Domain**: Backend + Security
- **Lifecycle Phase**: Maintenance
- **Urgency**: Critical (data leak, security breach)
- **Complexity**: Moderate (2-3 skills, expedited)

**Skill Selection**:
1. **investigator** (quick research on multi-tenant leaks)
2. **security** (multi-tenant security patterns)
3. **backend** (fix organization filtering)
4. **unit-tests** (verify fix, critical paths only)
5. **coditor** (audit entire codebase for similar leaks)
6. **devops** (deploy ASAP)

**Workflow**:
```
🚨 CRITICAL: Multi-tenant data leak

Immediate workflow:
1. /investigator (15 min) - Research multi-tenant patterns, identify leak locations
2. /security (review patterns) - Multi-tenant security reference
3. /backend (30 min) - Fix organization filters in all affected queries
4. /unit-tests (15 min) - Test organization isolation
5. /coditor (30 min) - Audit entire codebase for similar leaks
6. /devops - Deploy fix ASAP

Shall I invoke /investigator now?
```

### Example 2: New Feature (Normal Urgency)

**User**: "Add a resource booking calendar to the coordination module"

**Analysis**:
- **Task Type**: New Feature
- **Domain**: Full-Stack
- **Lifecycle Phase**: Architecture → Development
- **Urgency**: Normal
- **Complexity**: Complex (full workflow)

**Skill Selection**:
1. **featuredev** (planning, modeling, building, testing)
2. **frontend** (FullCalendar + HTMX UI)
3. **backend** (Django models, API endpoints)
4. **database** (migrations)
5. **unit-tests** (functionality tests)
6. **integration-tests** (workflow tests)
7. **coditor** (pre-deployment audit)
8. **devops** (deployment guidance)

**Workflow**:
```
New Feature Development: Resource Booking Calendar

Full workflow:
1. /featuredev - Plan and model the feature (FDD methodology)
2. /frontend - Build FullCalendar UI with HTMX
3. /backend - Implement ResourceBooking model and API
4. /database - Review and apply migrations
5. /unit-tests - Test booking functionality
6. /integration-tests - Test booking workflow
7. /coditor - Comprehensive audit
8. /devops - Deployment guidance

Let's start with feature planning. Shall I invoke /featuredev now?
```

### Example 3: Deployment Request

**User**: "Deploy to staging"

**Analysis**:
- **Task Type**: Deployment
- **Domain**: DevOps
- **Lifecycle Phase**: Deployment
- **Urgency**: Normal (user-requested)
- **Complexity**: Moderate (safety checks + deployment)

**Skill Selection**:
1. **safety-first** (MANDATORY - verify safety)
2. **coditor** (MANDATORY - audit)
3. **unit-tests** (MANDATORY - verify tests)
4. **integration-tests** (MANDATORY - verify integration)
5. **devops** (deployment guidance)

**Workflow**:
```
Deployment to Staging

Mandatory pre-deployment workflow:
1. /safety-first - Verify no uncommitted changes, database safe
2. /coditor - Comprehensive audit (all Critical/High must be fixed)
3. /unit-tests - Verify all tests pass
4. /integration-tests - Verify integration tests pass
5. /devops - Deployment guidance (you execute: git push origin staging)

Shall I invoke /safety-first now?
```

### Example 4: Performance Investigation

**User**: "The dashboard is loading very slowly"

**Analysis**:
- **Task Type**: Performance (Investigation + Optimization)
- **Domain**: Backend (likely query optimization)
- **Lifecycle Phase**: Operations
- **Urgency**: Normal
- **Complexity**: Moderate (2-3 skills)

**Skill Selection**:
1. **investigator** (research slow query patterns)
2. **database** (query optimization)
3. **backend** (code optimization)
4. **unit-tests** (verify optimization)
5. **coditor** (performance audit)

**Workflow**:
```
Performance Investigation: Slow Dashboard

Workflow:
1. /investigator - Research Django query optimization patterns
2. /database - Optimize queries (select_related, prefetch_related, indexing)
3. /backend - Implement optimizations
4. /unit-tests - Verify no regressions
5. /coditor - Performance audit

Shall I invoke /investigator now to identify bottlenecks?
```

---

## Special Cases

### Case 1: Ambiguous Request

**User**: "Make it better"

**Action**: Use **prompter** skill to clarify

**Workflow**:
```
Your request is ambiguous. I'll use /prompter to clarify requirements.

Questions I need answered:
1. What specifically should be improved? (UI, performance, code quality, security)
2. Which component/feature are you referring to?
3. What problem are you experiencing?

Shall I invoke /prompter now to gather requirements?
```

### Case 2: Multi-Domain Complex Request

**User**: "Add AI-powered recommendations to the planning module with a nice UI"

**Analysis**:
- **Domains**: AI + Backend + Frontend (multi-domain)
- **Complexity**: Complex

**Skill Selection**:
1. **featuredev** (orchestrate full feature)
2. **obcai-engineer** (AI specialist agent)
3. **backend** (Django integration)
4. **frontend** (UI with HTMX)
5. Full testing + deployment workflow

**Workflow**:
```
Complex Multi-Domain Feature: AI-Powered Planning Recommendations

This requires AI, backend, and frontend work. I recommend the full workflow:

1. /featuredev - Plan the feature (FDD)
2. /obcai-engineer - Design AI recommendation agent (ADK)
3. /backend - Integrate agent with Django
4. /frontend - Build recommendation UI
5. /unit-tests - Test AI functions and integration
6. /coditor - Audit before deployment
7. /devops - Deployment guidance

Shall I invoke /featuredev now to start planning?
```

### Case 3: Security-Critical Request

**User**: "Implement login functionality"

**Analysis**:
- **Domain**: Backend + Security (security-critical)
- **Critical Requirement**: CSP compliance, secure authentication

**Skill Selection**:
1. **security** (authentication patterns)
2. **backend** (implement auth)
3. **frontend** (login UI, CSP-compliant)
4. **unit-tests** (security tests)
5. **coditor** (security audit)

**Workflow**:
```
Security-Critical Feature: Login Functionality

This requires security-first approach:

1. /security - Review Django authentication patterns, CSP requirements
2. /backend - Implement authentication (Django auth + RBAC)
3. /frontend - Build login UI (CSP-compliant)
4. /unit-tests - Test authentication flow
5. /coditor - Security audit (mandatory for auth features)
6. /devops - Deployment guidance

Shall I invoke /security now to review authentication patterns?
```

---

## Quick Reference Decision Table

| User Request | Task Type | Domain | Urgency | Complexity | First Skill to Recommend |
|--------------|-----------|--------|---------|-----------|-------------------------|
| "Add booking calendar" | Feature | Full-Stack | Normal | Complex | featuredev |
| "Task deletion is broken" | Bug | Frontend | High | Moderate | investigator |
| "Deploy to staging" | Deployment | DevOps | Normal | Moderate | safety-first |
| "Users see other orgs' data" | Bug | Security | Critical | Moderate | investigator (urgent) |
| "Optimize dashboard query" | Performance | Database | Normal | Moderate | investigator |
| "Implement login" | Feature | Security | Normal | Complex | security |
| "Run tests" | Testing | Testing | Normal | Simple | unit-tests |
| "Why is this slow?" | Investigation | Unknown | Normal | Simple | investigator |

---

## Integration with Workflow Templates

After skill selection, AppManager maps selected skills to **workflow templates** (see `workflow-templates.md`):

- **New Feature** → New Feature Development Template
- **Bug Fix** → Bug Fix Template
- **Deployment** → Deployment Template
- **Database Change** → Database Migration Template
- **Security** → Security Enhancement Template
- **AI Feature** → AI Feature Template

---

**Remember**: Skill selection is multi-dimensional. AppManager analyzes task type, domain, lifecycle phase, urgency, and complexity together to recommend the most appropriate skills and workflow.
