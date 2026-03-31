# OBCMS Lifecycle Workflows

**Purpose**: Detailed SDLC phase mapping with indicators, recommended skills per phase, and transition criteria for OBCMS development.

**Use**: AppManager uses this reference to detect current lifecycle phase and recommend phase-appropriate skills.

---

## SDLC Phase Overview

OBCMS development follows a standard Software Development Lifecycle (SDLC) with these phases:

1. **Architecture** - System design, planning, technical decisions
2. **Development** - Implementation of features and functionality
3. **Testing** - Verification and validation
4. **Deployment** - Release to staging or production
5. **Maintenance** - Bug fixes, optimization, monitoring
6. **Operations** - Ongoing monitoring, performance, scaling

Each phase has specific indicators, recommended skills, inputs, outputs, and transition criteria.

---

## Phase 1: Architecture

### Phase Indicators

**User Language**:
- "design", "plan", "architect", "structure"
- "how should we", "what's the best way to"
- "database schema", "API design"
- "should we use", "which approach"

**Context Clues**:
- No existing implementation yet
- Planning new major features
- Discussing technical approaches
- Architectural questions

**Examples**:
- "Design a multi-stakeholder partnership tracking feature"
- "Plan the database schema for resource booking"
- "What's the best architecture for the calendar component?"

### Recommended Skills

| Priority | Skill | Purpose |
|----------|-------|---------|
| **Primary** | `architect` | Architectural evaluation and planning |
| **Primary** | `featuredev` (planning mode) | Feature modeling and design |
| Supporting | `database` | Database schema design |
| Supporting | `prompter` | Clarify requirements |
| Supporting | `investigator` | Research architectural patterns |

### Phase Inputs
- User requirements (functional, non-functional)
- Business objectives
- Existing system constraints
- OBCMS architectural patterns

### Phase Outputs
- Architecture diagrams
- Database schemas (ERD)
- API endpoint designs
- Technical decisions documented
- Feature plans (from featuredev)

### Transition Criteria

**Ready to Move to Development** when:
- ✅ Architecture design approved by user
- ✅ Database schema designed
- ✅ API endpoints defined
- ✅ Technical decisions made and documented
- ✅ Feature plan approved (if using featuredev)

**Transition Statement**:
```
Architecture phase complete. We have:
- Designed the database schema (ResourceBooking model)
- Defined API endpoints (list, create, update, delete, availability check)
- Selected FullCalendar for UI

Ready to move to Development phase?
```

---

## Phase 2: Development

### Phase Indicators

**User Language**:
- "implement", "build", "create", "add feature"
- "write code for", "develop"
- "make it work", "code the"

**Context Clues**:
- Architecture/planning phase completed
- Ready to write code
- Feature requirements are clear
- User approves design

**Examples**:
- "Implement the resource booking models"
- "Build the calendar UI with FullCalendar"
- "Create the HTMX form for task deletion"

### Recommended Skills

| Priority | Skill | Purpose |
|----------|-------|---------|
| **Primary** | `featuredev` | Full-stack feature development (FDD) |
| **Primary** | `backend` | Django models, views, APIs |
| **Primary** | `frontend` | HTMX, Alpine.js, Tailwind UI |
| **Primary** | `database` | Django migrations |
| Supporting | `frontend-component-scaffolder` | Generate UI components |
| Supporting | `security` | Ensure CSP compliance, multi-tenant isolation |
| Supporting | `obcai-engineer` | AI features (if applicable) |
| Supporting | `ai-engineer` | General AI features (if applicable) |

### Sub-Phases

**2.1 Backend Development**:
- Models: `backend` + `database`
- Views: `backend` + `security` (RBAC, multi-tenant)
- APIs: `backend` (DRF serializers, viewsets)
- Background tasks: `backend` (Celery)

**2.2 Frontend Development**:
- Templates: `frontend` + `frontend-component-scaffolder`
- HTMX interactions: `frontend`
- Alpine.js state: `frontend`
- Tailwind styling: `frontend`
- CSP compliance: `security` (mandatory!)

**2.3 Database Migrations**:
- Create migrations: `database`
- Review migrations: `safety-first`
- Test migrations: `unit-tests`

### Phase Inputs
- Architecture designs from Phase 1
- Feature plans (from featuredev)
- OBCMS design standards
- GEMINI.md rules (especially Rule 12: CSP compliance)

### Phase Outputs
- Django models (models.py)
- Views (views.py, viewsets)
- Serializers (serializers.py)
- Templates (*.html with HTMX)
- Migrations (migrations/*.py)
- Background tasks (tasks.py)

### Transition Criteria

**Ready to Move to Testing** when:
- ✅ All code implemented
- ✅ No syntax errors
- ✅ Migrations created and applied locally
- ✅ CSP compliance verified (Rule 12)
- ✅ Multi-tenant data isolation verified
- ✅ Code follows OBCMS standards

**Transition Statement**:
```
Development phase complete. We have:
- Implemented ResourceBooking model with organization field
- Created booking API endpoints (DRF)
- Built FullCalendar UI with HTMX
- Migrations created and applied locally
- All code is CSP-compliant

Ready to move to Testing phase?
```

---

## Phase 3: Testing

### Phase Indicators

**User Language**:
- "test", "verify", "check", "run tests"
- "does it work", "make sure"
- "test coverage", "validate"

**Context Clues**:
- Development completed
- Code implementation finished
- Ready to verify functionality
- Before committing or deploying

**Examples**:
- "Run tests to verify the booking feature"
- "Check if the task deletion works"
- "Verify test coverage is above 80%"

### Recommended Skills

| Priority | Skill | Purpose |
|----------|-------|---------|
| **Primary** | `unit-tests` | Run unit tests, verify functionality |
| **Primary** | `integration-tests` | Test cross-module workflows |
| Supporting | `e2e-tests` | Test complete user journeys |
| Supporting | `component-tests` | Test UI components |
| Supporting | `debugger` | Fix test failures (root cause) |
| Supporting | `coditor` | Pre-deployment audit |

### Testing Hierarchy

**3.1 Unit Tests** (Always run first):
- Test individual functions/methods
- Test models, serializers, utilities
- Verify business logic
- **Requirement**: Coverage > 80%

**3.2 Integration Tests** (After unit tests pass):
- Test cross-module workflows
- Test API endpoints (full HTTP stack)
- Test Django views with request/response
- Verify database interactions

**3.3 E2E Tests** (After integration tests pass):
- Test complete user workflows (browser)
- Verify UI interactions
- Test HTMX swaps and updates
- Verify user journey from UI to database

**3.4 Component Tests** (If applicable):
- Test individual UI components
- Verify component behavior

### Phase Inputs
- Implemented code from Phase 2
- Test cases (existing + new)
- Test data

### Phase Outputs
- Test results (pass/fail)
- Test coverage reports
- Bug fixes (if tests fail)
- Root cause analysis (if failures)

### Critical Rules

**NEVER**:
- Bypass failing tests
- Skip tests before committing
- Deploy with failing tests
- Use temporary fixes for test failures

**ALWAYS**:
- Fix root causes of test failures
- Achieve > 80% test coverage
- Run all test types (unit, integration, e2e)
- Test in browser (3 times minimum for UI changes)

### Transition Criteria

**Ready to Move to Deployment** when:
- ✅ All unit tests pass
- ✅ All integration tests pass
- ✅ All e2e tests pass (if UI changes)
- ✅ Test coverage > 80%
- ✅ UI tested in browser (3 times minimum)
- ✅ No failing tests or skipped tests
- ✅ Coditor audit completed (no Critical/High findings)

**Transition Statement**:
```
Testing phase complete. Results:
- Unit tests: 45/45 passed (coverage: 87%)
- Integration tests: 12/12 passed
- E2E tests: 5/5 passed
- Coditor audit: 0 Critical, 0 High, 2 Medium findings
- UI tested in browser: 3 times (Chrome DevTools)

Ready to move to Deployment phase?
```

**If Tests Fail**:
```
Testing phase BLOCKED. Issues:
- Unit tests: 2 failures (test_booking_availability, test_organization_filter)
- Integration tests: Not run (waiting for unit tests)

Recommended next step: Invoke /debugger to fix failing tests.

Would you like to proceed with debugging?
```

---

## Phase 4: Deployment

### Phase Indicators

**User Language**:
- "deploy", "release", "push to staging/production"
- "deploy to staging", "ready to deploy"
- "push to Railway"

**Context Clues**:
- Testing phase completed (all tests pass)
- User explicitly requests deployment
- Code ready for staging/production
- All critical issues resolved

**Examples**:
- "Deploy to staging"
- "Ready to push to production"
- "Release this feature"

### Recommended Skills

| Priority | Skill | Purpose |
|----------|-------|---------|
| **PRIMARY** | `safety-first` | **MANDATORY** safety verification |
| **PRIMARY** | `coditor` | **MANDATORY** comprehensive audit |
| **PRIMARY** | `unit-tests` | **MANDATORY** verify tests pass |
| **PRIMARY** | `integration-tests` | **MANDATORY** verify integration |
| **PRIMARY** | `devops` | Deployment guidance (manual execution) |

### Deployment Workflow (Mandatory Sequence)

**Step 1: Safety Verification** (`safety-first`)
```
MANDATORY checks:
- No uncommitted changes (git status clean)
- Database safety (db.sqlite3 exists, no destructive operations)
- No risky operations pending
```

**Step 2: Code Audit** (`coditor`)
```
MANDATORY audit:
- Comprehensive codebase audit
- All Critical findings fixed
- All High findings fixed
- Medium/Low findings documented
```

**Step 3: Test Verification** (`unit-tests`, `integration-tests`)
```
MANDATORY test runs:
- All unit tests pass
- All integration tests pass
- Test coverage > 80%
```

**Step 4: Deployment Guidance** (`devops`)
```
GUIDANCE ONLY (user executes manually):
- Review deployment checklist
- Execute: git push origin staging  (or git push origin main)
- Monitor deployment logs
- Run post-deployment verification
```

### Phase Inputs
- Tested code from Phase 3
- Pre-deployment checklist (`docs/claude/checklists/pre-deployment.md`)
- Railway environment configuration

### Phase Outputs
- Deployed application (staging or production)
- Deployment logs
- Post-deployment verification results

### Critical Safety Checks

**Pre-Deployment (MANDATORY)**:
- ✅ safety-first completed (no blockers)
- ✅ coditor audit completed (Critical/High = 0)
- ✅ All tests pass
- ✅ Migrations tested on staging (if deploying to production)
- ✅ Database backup completed (production only)
- ✅ No uncommitted changes
- ✅ No secrets in codebase

**If ANY Check Fails**: STOP deployment and resolve issues.

### Deployment Types

**Staging Deployment**:
```
Workflow: safety-first → coditor → unit-tests → integration-tests → devops

User executes: git push origin staging

Post-deployment: Verify on staging, test critical features
```

**Production Deployment** (Extra Safety):
```
Workflow: safety-first → coditor → unit-tests → integration-tests → devops

Additional requirements:
- Staging verification completed
- Production database backup
- Team notified
- Low-traffic deployment window

User executes: git push origin main

Post-deployment: Monitor for 10 min, verify health, check error rates
```

### Transition Criteria

**Deployment Successful** when:
- ✅ Application responding (200 OK)
- ✅ Health check passing
- ✅ Migrations applied successfully
- ✅ Static files served
- ✅ No error spikes in logs
- ✅ Critical endpoints tested

**Transition Statement**:
```
Deployment phase complete:
- Deployed to: staging
- Deployment status: Success
- Health check: ✅ Passing
- Migrations: ✅ Applied
- Error rate: Normal
- Critical features: ✅ Tested

Application is live and healthy. Monitor for next hour.
```

**If Deployment Fails**:
```
Deployment phase FAILED:
- Error: 503 Service Unavailable
- Health check: ❌ Failed

Recommended next step: Invoke /devops for troubleshooting, consider rollback.

Would you like to proceed with troubleshooting or rollback?
```

---

## Phase 5: Maintenance

### Phase Indicators

**User Language**:
- "fix", "debug", "investigate", "error", "issue"
- "not working", "broken", "bug"
- "users reporting", "production issue"

**Context Clues**:
- Application already deployed
- Error or bug reported
- Feature not working as expected
- User feedback about issues

**Examples**:
- "Task deletion isn't working in kanban view"
- "Users are seeing other organizations' data"
- "500 error on the booking endpoint"

### Recommended Skills

| Priority | Skill | Purpose |
|----------|-------|---------|
| **Primary** | `investigator` | Research issue, gather evidence |
| **Primary** | `debugger` | Systematic debugging |
| Supporting | `backend` | Implement backend fixes |
| Supporting | `frontend` | Implement frontend fixes |
| Supporting | `security` | Fix security issues |
| Supporting | `refactor` | Optimize or refactor code |
| Supporting | `unit-tests` | Verify fixes |
| Supporting | `coditor` | Audit for related issues |

### Maintenance Workflow

**Bug Fix Workflow**:
```
1. investigator → Research issue, propose 3 solutions
2. debugger → Systematic debugging (root cause analysis)
3. (backend|frontend) → Implement fix
4. unit-tests → Verify fix
5. coditor → Audit for related issues
6. devops → Deploy fix
```

**Urgency Levels**:

| Urgency | Criteria | Response Time | Workflow |
|---------|----------|---------------|----------|
| **Critical** | Production down, data leak, security breach | Immediate | investigator → debugger → fix → deploy ASAP |
| **High** | User-facing bug, broken feature | Same day | investigator → debugger → fix → tests → deploy |
| **Normal** | Non-critical bug, minor issue | 1-2 sprints | investigator → plan fix → implement → tests → deploy |
| **Low** | Nice-to-have, optimization | When convenient | refactor → optimize → tests → deploy |

### Phase Inputs
- Bug reports / error messages
- User feedback
- Production logs
- Monitoring data

### Phase Outputs
- Root cause analysis
- Bug fixes (permanent, not temporary)
- Test cases (to prevent regression)
- Updated code

### Critical Rules

**NEVER** (GEMINI.md Rule 5):
- Use temporary fixes
- Bypass errors
- Apply quick hacks
- Deploy without testing

**ALWAYS**:
- Fix root causes
- Add test cases
- Verify no regressions
- Audit for related issues

### Transition Criteria

**Fix Complete** when:
- ✅ Root cause identified and fixed
- ✅ Tests pass (including new test cases)
- ✅ No regressions introduced
- ✅ Coditor audit complete (no new issues)
- ✅ Ready to deploy fix

**Transition Statement**:
```
Maintenance phase complete. Bug fix summary:
- Issue: Multi-tenant data leak in Task.objects.all()
- Root cause: Missing organization filter
- Fix: Added organization=request.user.organization filter
- Tests: Added test_organization_isolation test case
- Coditor audit: Found 3 similar issues (fixed)

Ready to deploy fix to staging?
```

---

## Phase 6: Operations

### Phase Indicators

**User Language**:
- "monitor", "optimize", "performance", "scaling"
- "slow response", "database performance"
- "cost optimization", "resource usage"

**Context Clues**:
- Application running in production
- Performance issues
- Scaling needs
- Operational concerns

**Examples**:
- "Optimize the database queries for the dashboard"
- "The map is loading slowly"
- "How can we reduce Railway costs?"

### Recommended Skills

| Priority | Skill | Purpose |
|----------|-------|---------|
| **Primary** | `devops` | Infrastructure optimization, monitoring |
| Supporting | `database` | Query optimization |
| Supporting | `backend` | Code optimization |
| Supporting | `frontend` | UI performance optimization |
| Supporting | `obcai-engineer` | AI cost optimization |
| Supporting | `coditor` | Performance audit |

### Operations Focus Areas

**6.1 Performance Optimization**:
- Database query optimization (select_related, prefetch_related)
- Caching strategies (Redis)
- Frontend optimization (lazy loading, pagination)
- API response time optimization

**6.2 Monitoring**:
- Railway logs monitoring
- Error rate tracking
- Response time monitoring
- Database performance monitoring

**6.3 Cost Optimization**:
- Railway resource usage
- Database connection pooling
- obcAI token usage (Gemini + Zhipu GLM 4.6)
- Redis memory optimization

**6.4 Scaling**:
- Horizontal scaling (Railway replicas)
- Database optimization (indexing, query optimization)
- Multi-cloud migration planning (GCP, AWS, Azure)

### Phase Inputs
- Production metrics
- Railway logs
- Database performance data
- User feedback (performance)

### Phase Outputs
- Optimized code
- Performance improvements
- Monitoring dashboards
- Scaling recommendations

### Transition Criteria

**Optimization Complete** when:
- ✅ Performance issue resolved
- ✅ Metrics improved (response time, query time, etc.)
- ✅ Tests pass
- ✅ No regressions
- ✅ Deployed and verified

---

## Phase Transitions

### Common Transition Patterns

**Linear Progression** (New Feature):
```
Architecture → Development → Testing → Deployment → Operations
```

**Bug Fix Cycle** (Maintenance):
```
Maintenance (identify bug) → Development (fix) → Testing → Deployment
```

**Performance Optimization** (Operations):
```
Operations (identify issue) → Development (optimize) → Testing → Deployment → Operations (verify)
```

**Security Enhancement**:
```
Architecture (plan) → Development (implement) → Testing (security tests) → Deployment
```

### Phase Overlap

Some phases can overlap:
- **Architecture + Development**: Iterative design while implementing
- **Development + Testing**: Test-driven development (TDD)
- **Testing + Deployment**: Continuous deployment (CD)
- **Deployment + Operations**: Continuous monitoring

### Resuming After Interruption

**AppManager tracks phase transitions**:
```
[Workflow State]
Current Phase: Testing
Previous Phases:
✅ Architecture - Complete (feature designed)
✅ Development - Complete (implemented ResourceBooking)
🔄 Testing - In Progress (2/3 test types pass)

Next Step: Fix 2 failing unit tests before proceeding to Deployment.
```

---

## Integration with GEMINI.md Rules

Each phase enforces GEMINI.md critical rules:

| Phase | Critical Rules Enforced |
|-------|------------------------|
| Architecture | Rule 6 (No assumptions - research when unsure) |
| Development | Rule 12 (CSP compliance), Rule 8 (Keep src/ clean) |
| Testing | Rule 11 (UI testing mandatory), Rule 7 (Verify with evidence) |
| Deployment | Rule 1 (Ask permission before committing), Rule 13 (Migration management) |
| Maintenance | Rule 5 (No temporary fixes - fix root causes) |
| Operations | Rule 7 (Verify outcomes with evidence) |

---

## Quick Reference: Lifecycle Detection

| User Says | Detected Phase | Recommended Skills |
|-----------|---------------|-------------------|
| "Design the booking system" | Architecture | architect, database, featuredev |
| "Implement the booking models" | Development | backend, database |
| "Build the calendar UI" | Development | frontend, frontend-component-scaffolder |
| "Run tests" | Testing | unit-tests, integration-tests |
| "Deploy to staging" | Deployment | safety-first, coditor, devops |
| "Task deletion is broken" | Maintenance | investigator, debugger |
| "Optimize the dashboard query" | Operations | database, backend, devops |

---

**Remember**: Lifecycle phase detection is dynamic. AppManager analyzes user language, conversation context, and previous phase completions to determine the current phase and recommend appropriate skills.
