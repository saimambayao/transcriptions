# OBCMS Workflow Templates

**Purpose**: Pre-built workflow templates for common OBCMS tasks.

**Use**: AppManager uses these templates to recommend complete workflows for standard development scenarios.

---

## Template Overview

Each template includes:
- **Trigger**: When to use this template
- **Workflow Steps**: Ordered sequence of skills
- **Decision Points**: Key decisions requiring user input
- **Success Criteria**: When the workflow is complete
- **Safety Checks**: Critical verifications
- **Estimated Timeline**: Rough time estimates

---

## Template 1: New Feature Development

### Trigger
- User requests a new feature or capability
- Keywords: "add", "create", "implement", "build feature"

### Full Workflow

```
[Workflow: New Feature Development]

Phase 1: Planning & Architecture (1-2 hours)
├─ 1. /safety-first
│   Purpose: Verify git status, database safety
│   Output: Safety clearance or blockers
│   Decision: Proceed or resolve blockers?
│
├─ 2. /featuredev (Planning Mode)
│   Purpose: Feature modeling and design (FDD methodology)
│   Output: Feature plan, user stories, acceptance criteria
│   Decision: User approves plan?
│
└─ If complex architecture needed:
    └─ 3. /architect (Optional)
        Purpose: Architectural planning
        Output: Architecture diagrams, technical decisions

Phase 2: Implementation (4-8 hours)
├─ 4. /database (if needed)
│   Purpose: Design database schema, create migrations
│   Output: Django migrations
│
├─ 5. /backend (if needed)
│   Purpose: Implement Django models, views, APIs
│   Output: Python code (models.py, views.py, serializers.py)
│
├─ 6. /frontend (if needed)
│   Purpose: Build UI components (HTMX + Tailwind)
│   Output: Django templates, HTMX interactions
│
└─ Critical: All code must be CSP-compliant (Rule 12)

Phase 3: Testing (1-2 hours)
├─ 7. /unit-tests
│   Purpose: Verify functionality
│   Output: Test results (must pass, coverage > 80%)
│   Decision: Tests pass? If not, debug before proceeding
│
└─ 8. /integration-tests
    Purpose: Verify cross-module workflows
    Output: Integration test results (must pass)

Phase 4: Quality Assurance (30-60 min)
└─ 9. /coditor
    Purpose: Comprehensive audit
    Output: Findings (Critical/High/Medium/Low)
    Decision: Any Critical/High findings? Fix before deployment

Phase 5: Deployment (30 min)
└─ 10. /devops
    Purpose: Deployment guidance
    Output: Deployment checklist, commands
    User Action: Execute git push origin staging (manually)
```

### Decision Points

**Decision Point 1** (After safety-first):
```
✅ safety-first completed.

Results:
- Git status: Clean (no uncommitted changes)
- Database: Safe (db.sqlite3 exists)
- Blockers: None

Proceed to /featuredev for feature planning?
```

**Decision Point 2** (After featuredev planning):
```
✅ /featuredev planning completed.

Feature Plan:
- Feature: Resource Booking Calendar
- Models: ResourceBooking, AvailabilitySlot
- Views: BookingListView, BookingCreateView, BookingUpdateView, BookingDeleteView
- Templates: booking_list.html, booking_form.html, booking_calendar.html
- API: /api/bookings/ (CRUD endpoints)

User approval required. Proceed with implementation?
```

**Decision Point 3** (After implementation):
```
✅ Implementation completed.

Changes:
- Models: ResourceBooking model created
- Migrations: 0025_resourcebooking.py
- Views: 4 views implemented
- Templates: 3 templates created (CSP-compliant)
- API: DRF endpoints created

Tests pass? Run /unit-tests now?
```

**Decision Point 4** (After coditor):
```
✅ /coditor audit completed.

Findings:
- Critical: 0
- High: 0
- Medium: 2 (documented, can fix later)
- Low: 5

Ready to deploy to staging?
```

### Success Criteria

- ✅ Feature plan approved by user
- ✅ All code implemented
- ✅ Migrations created and tested
- ✅ All tests pass (coverage > 80%)
- ✅ CSP compliance verified
- ✅ Coditor audit: Critical/High = 0
- ✅ UI tested in browser (3 times)
- ✅ Deployed to staging and verified

### Safety Checks

- No uncommitted changes before starting
- Database safety verified
- CSP compliance mandatory (GEMINI.md Rule 12)
- Multi-tenant data isolation verified
- All tests pass before deployment
- Coditor audit before deployment

### Estimated Timeline

- **Planning**: 1-2 hours
- **Implementation**: 4-8 hours (depends on complexity)
- **Testing**: 1-2 hours
- **Audit**: 30-60 min
- **Deployment**: 30 min
- **Total**: 7-13 hours (1-2 days)

---

## Template 2: Bug Fix

### Trigger
- User reports a bug, error, or issue
- Keywords: "fix", "broken", "not working", "error", "bug"

### Full Workflow

```
[Workflow: Bug Fix]

Phase 1: Investigation (30-60 min)
├─ 1. /investigator
│   Purpose: Research issue, gather evidence, propose solutions
│   Output: 3 solution alternatives (ranked by effectiveness)
│   Decision: Which solution to implement?
│
└─ 2. /debugger (if needed)
    Purpose: Systematic debugging, root cause analysis
    Output: Root cause identified, fix plan

Phase 2: Implementation (30 min - 2 hours)
├─ 3. /backend (if backend bug)
│   Purpose: Implement fix
│   Output: Fixed code
│
├─ 3. /frontend (if frontend bug)
│   Purpose: Implement fix
│   Output: Fixed templates/HTMX
│
└─ Critical: Fix root cause, not symptoms (GEMINI.md Rule 5)

Phase 3: Verification (30 min)
├─ 4. /unit-tests
│   Purpose: Verify fix, add test case to prevent regression
│   Output: Tests pass (including new test case)
│
└─ 5. /coditor (Optional but recommended)
    Purpose: Audit for related issues
    Output: Similar issues identified and fixed

Phase 4: Deployment (30 min)
└─ 6. /devops
    Purpose: Deploy fix
    User Action: git push origin staging (or main for hotfix)
```

### Decision Points

**Decision Point 1** (After investigator):
```
✅ /investigator completed.

Issue: Task deletion not working in kanban view
Root Cause: HTMX targeting mismatch

3 Solution Alternatives:
1. Fix HTMX hx-target to match kanban card ID (🟢 High confidence)
2. Use hx-swap="outerHTML" on parent container (🟡 Medium confidence)
3. Reload entire kanban board after deletion (🟠 Low confidence, not ideal)

Recommendation: Solution #1 (fix targeting)

Proceed with Solution #1?
```

**Decision Point 2** (After implementation):
```
✅ Fix implemented.

Changes:
- Updated hx-target in task_kanban_card.html
- Changed from "#task-list" to "#task-{{ task.id }}"

Run /unit-tests to verify fix?
```

**Decision Point 3** (After coditor audit):
```
✅ /coditor audit completed.

Related Issues Found:
- Similar HTMX targeting issue in 2 other templates (fixed)
- Missing hx-confirm on 1 delete button (fixed)

Ready to deploy fix?
```

### Urgency-Based Variations

**Critical Urgency** (Production down, data leak):
```
EXPEDITED WORKFLOW:
1. /investigator (quick, 15 min)
2. /debugger (fast, 30 min)
3. Fix implementation (immediate)
4. /unit-tests (critical paths only)
5. Deploy ASAP

Skip: coditor audit (do after deployment)
```

**High Urgency** (User-facing bug):
```
SHORTENED WORKFLOW:
1. /investigator (30 min)
2. Fix implementation
3. /unit-tests (focused)
4. Deploy same day

Coditor audit: Optional
```

**Normal Urgency**:
```
FULL WORKFLOW:
Use standard bug fix workflow above
```

### Success Criteria

- ✅ Root cause identified and fixed
- ✅ Tests pass (including new regression test)
- ✅ No temporary fixes or workarounds
- ✅ Related issues found and fixed (via coditor)
- ✅ Fix deployed and verified

### Safety Checks

- Root cause fix, not symptom fix (GEMINI.md Rule 5)
- Add test case to prevent regression
- No breaking changes to existing functionality
- UI tested in browser (if UI bug)

### Estimated Timeline

- **Investigation**: 30-60 min
- **Implementation**: 30 min - 2 hours
- **Testing**: 30 min
- **Audit**: 30 min (optional)
- **Deployment**: 30 min
- **Total**: 2-4 hours

---

## Template 3: Deployment (Staging/Production)

### Trigger
- User says "deploy to staging" or "deploy to production"
- Keywords: "deploy", "release", "push to"

### Full Workflow (MANDATORY Safety Checks)

```
[Workflow: Deployment]

Phase 1: Safety Verification (15 min) **MANDATORY**
└─ 1. /safety-first
    Purpose: Verify no uncommitted changes, database safe
    Output: Safety clearance or STOP
    Critical: If ANY check fails, STOP deployment

Phase 2: Code Quality Audit (30-60 min) **MANDATORY**
└─ 2. /coditor
    Purpose: Comprehensive audit
    Output: Findings (must fix Critical/High)
    Critical: Critical findings = 0, High findings = 0

Phase 3: Test Verification (30-60 min) **MANDATORY**
├─ 3. /unit-tests
│   Purpose: Verify all tests pass
│   Output: All tests passing, coverage > 80%
│
└─ 4. /integration-tests
    Purpose: Verify integration tests pass
    Output: All integration tests passing

Phase 4: Deployment Guidance (30 min)
└─ 5. /devops
    Purpose: Deployment guidance, post-deployment verification
    Output: Deployment checklist, commands
    User Action: git push origin staging (or git push origin main)
```

### Critical Safety Checks (MANDATORY)

**Pre-Deployment Checklist**:
- ✅ safety-first: No uncommitted changes
- ✅ safety-first: Database safety verified
- ✅ coditor: Critical findings = 0
- ✅ coditor: High findings = 0
- ✅ unit-tests: All tests pass
- ✅ integration-tests: All tests pass
- ✅ Test coverage > 80%
- ✅ Migrations tested (locally, or on staging if deploying to production)
- ✅ Database backup completed (production only)
- ✅ No secrets in codebase
- ✅ UI tested in browser (3 times minimum)

**If ANY Check Fails**: STOP deployment and resolve.

### Decision Points

**Decision Point 1** (After safety-first):
```
✅ /safety-first completed.

Results:
- Git status: Clean ✅
- Database: Safe ✅
- Blockers: None ✅

Proceed to /coditor for code audit?
```

**Decision Point 2** (After coditor):
```
❌ /coditor audit FAILED.

Findings:
- Critical: 2 (MUST FIX)
  1. Multi-tenant data leak in BookingListView (missing organization filter)
  2. CSP violation in booking_calendar.html (inline script without nonce)
- High: 1 (MUST FIX)
  1. Missing permission check on BookingDeleteView

DEPLOYMENT BLOCKED. Fix Critical/High findings before proceeding.

Would you like me to help fix these issues?
```

**Decision Point 3** (After fixing issues and re-auditing):
```
✅ /coditor audit PASSED.

Findings:
- Critical: 0 ✅
- High: 0 ✅
- Medium: 2 (documented)
- Low: 5

Proceed to test verification?
```

**Decision Point 4** (After all checks pass):
```
✅ All pre-deployment checks passed:
- safety-first: ✅
- coditor: ✅ (Critical/High = 0)
- unit-tests: ✅ (52/52 passed, coverage: 89%)
- integration-tests: ✅ (15/15 passed)

Ready to deploy to staging.

Shall I invoke /devops for deployment guidance?
```

### Staging vs Production Differences

**Staging Deployment**:
```
Workflow: safety-first → coditor → tests → devops

User Action: git push origin staging

Post-Deployment:
- Verify deployment successful
- Test critical features on staging
- Monitor for 10-30 minutes
```

**Production Deployment** (Extra Safety):
```
Workflow: safety-first → coditor → tests → devops

Additional Requirements:
- Staging verification completed ✅
- Production database backup ✅
- Team notified ✅
- Low-traffic deployment window ✅

User Action: git push origin main

Extra Confirmation:
"⚠️⚠️⚠️ PRODUCTION DEPLOYMENT ⚠️⚠️⚠️
Are you ABSOLUTELY SURE? (type 'yes')"

Post-Deployment:
- Monitor for 1 hour minimum
- Verify health check
- Check error rates
- Test critical user journeys
```

### Success Criteria

- ✅ All pre-deployment checks passed
- ✅ Deployment successful (200 OK, health check passing)
- ✅ Migrations applied successfully
- ✅ Static files served correctly
- ✅ No error spikes in logs
- ✅ Critical endpoints tested
- ✅ Post-deployment verification completed

### Rollback Plan

**If Deployment Fails**:
```
1. Identify issue from logs (railway logs)
2. Decide: Fix forward or rollback?
3. If rollback needed:
   - Railway dashboard: Redeploy previous successful deployment
   - OR git: git revert HEAD && git push
4. Verify rollback successful
5. Investigate issue offline
```

### Estimated Timeline

- **Safety verification**: 15 min
- **Coditor audit**: 30-60 min
- **Test verification**: 30-60 min
- **Deployment**: 30 min
- **Post-deployment verification**: 30-60 min
- **Total**: 2-3 hours

---

## Template 4: Database Migration

### Trigger
- User modifies Django models or requests database changes
- Keywords: "migration", "database", "schema change", "model change"

### Full Workflow (CRITICAL SAFETY)

```
[Workflow: Database Migration]

Phase 1: Safety Verification (15 min) **MANDATORY**
└─ 1. /safety-first
    Purpose: Verify database safety, git status
    Output: Safety clearance
    Critical: Verify db.sqlite3 exists (NEVER DELETE - Rule 3)

Phase 2: Migration Planning (30 min)
├─ 2. /database
│   Purpose: Review migration, check for data loss risks
│   Output: Migration analysis, safety recommendations
│
└─ 3. /backend
    Purpose: Review model changes
    Output: Model code review

Phase 3: Migration Creation (15 min)
└─ Create migrations: python manage.py makemigrations
    Output: Migration files (migrations/*.py)
    Action: Review migration file carefully

Phase 4: Testing (30-60 min)
├─ 4. /unit-tests
│   Purpose: Test migration locally
│   Output: Migration applied successfully locally
│
└─ 5. /integration-tests
    Purpose: Test migration integration with existing code
    Output: All tests pass with new migrations

Phase 5: Quality Check (30 min)
└─ 6. /coditor
    Purpose: Audit migration for issues
    Output: Migration safety report

Phase 6: Deployment (staged)
└─ 7. /devops
    Purpose: Deployment guidance
    Output: Staged migration plan
    Critical: Test on staging FIRST (Rule 13)
```

### Critical Checks (GEMINI.md Rule 13)

**Pre-Migration Checklist**:
- ✅ No data deletion (or explicit backup taken)
- ✅ Migrations tested locally (manage.py migrate)
- ✅ No reverse migration issues
- ✅ Database backup completed (production)
- ✅ Migration file reviewed manually
- ✅ No destructive operations without approval

**Data Loss Prevention**:
```
⚠️ ALERT: Migration includes data deletion

Migration: Remove field 'old_field' from model 'MyModel'
Risk: Data in 'old_field' will be lost

Actions Required:
1. Backup data from 'old_field' first
2. Confirm data is no longer needed
3. User explicit approval required

Proceed with data deletion? (explicit approval needed)
```

### Decision Points

**Decision Point 1** (After migration creation):
```
✅ Migrations created.

Migration: 0026_resourcebooking_availability_slot.py

Changes:
- Add field 'availability_slot' to ResourceBooking
- Add field 'capacity' to AvailabilitySlot
- No data deletion ✅

Migration looks safe. Proceed to testing?
```

**Decision Point 2** (After local testing):
```
✅ Migration tested locally.

Results:
- Migration applied successfully ✅
- No errors ✅
- Data integrity maintained ✅

Proceed to /unit-tests for full test suite?
```

**Decision Point 3** (Before deployment):
```
✅ All checks passed:
- Migration tested locally ✅
- Unit tests pass ✅
- Integration tests pass ✅
- Coditor audit: No issues ✅

Deployment Plan (STAGED):
1. Deploy to staging FIRST
2. Test migration on staging
3. Verify data integrity on staging
4. ONLY THEN deploy to production

Proceed with staging deployment?
```

### Deployment Staging (MANDATORY)

**Stage 1: Staging**:
```
1. git push origin staging
2. Verify migration applied on staging
3. Test data integrity
4. Test affected features
5. Monitor for issues (30 min minimum)
```

**Stage 2: Production** (Only after staging success):
```
1. Backup production database (MANDATORY)
2. git push origin main
3. Monitor migration application
4. Verify data integrity
5. Test critical features
6. Monitor for 1 hour
```

### Success Criteria

- ✅ Migration file reviewed and safe
- ✅ No data deletion (or explicit backup + approval)
- ✅ Migration tested locally
- ✅ Migration tested on staging
- ✅ All tests pass
- ✅ Data integrity verified
- ✅ Production migration successful

### Safety Checks

- NEVER delete db.sqlite3 (GEMINI.md Rule 3)
- Always test migrations on staging first (GEMINI.md Rule 13)
- Backup production database before migration
- No destructive operations without explicit approval
- Review migration files manually

### Estimated Timeline

- **Planning**: 30 min
- **Creation**: 15 min
- **Testing**: 30-60 min
- **Audit**: 30 min
- **Staging deployment**: 30 min
- **Production deployment**: 30 min
- **Total**: 2.5-3.5 hours

---

## Template 5: Security Enhancement

### Trigger
- User requests security feature or fix
- Keywords: "security", "auth", "permissions", "CSP", "vulnerability"

### Full Workflow

```
[Workflow: Security Enhancement]

Phase 1: Security Planning (30-60 min)
└─ 1. /security
    Purpose: Security implementation patterns
    Output: Security patterns, best practices
    Focus: CSP, multi-tenant, XSS, authentication, authorization

Phase 2: Implementation (2-4 hours)
├─ 2. /backend
│   Purpose: Implement security changes
│   Output: Updated models, views, middleware
│   Critical: Multi-tenant data isolation, RBAC
│
└─ 3. /frontend (if applicable)
    Purpose: Update UI for CSP compliance
    Output: CSP-compliant templates
    Critical: CSP compliance mandatory (GEMINI.md Rule 12)

Phase 3: Security Testing (1 hour)
├─ 4. /unit-tests
│   Purpose: Security-focused tests
│   Output: Security test results
│   Tests: Authentication, authorization, data isolation
│
└─ 5. /coditor
    Purpose: Comprehensive security audit
    Output: Security findings (must fix Critical/High)

Phase 4: Deployment (30 min)
└─ 6. /devops
    Purpose: Deployment guidance
    User Action: Deploy to staging, then production
```

### Focus Areas

**CSP Compliance** (GEMINI.md Rule 12):
- Nonce-based script/style loading
- No inline scripts without nonces
- HTMX-compatible CSP patterns
- Alpine.js CSP patterns

**Multi-Tenant Security**:
- Organization-scoped queries
- Prevent cross-organization data leaks
- Organization field on all models
- QuerySet filtering: `.filter(organization=request.user.organization)`

**Authentication/Authorization**:
- Django authentication
- RBAC permissions
- Permission decorators on views
- API permission classes

**Input Validation**:
- XSS prevention (Django auto-escaping)
- CSRF protection (Django middleware)
- SQL injection prevention (ORM, parameterized queries)

### Critical Security Checks

**Pre-Deployment**:
- ✅ CSP compliance verified (no inline scripts without nonces)
- ✅ Multi-tenant data isolation verified
- ✅ Permission checks on all views
- ✅ Input validation on all forms
- ✅ Coditor security audit: Critical/High = 0

### Decision Points

**Decision Point 1** (After security planning):
```
✅ /security planning completed.

Security Requirements:
- Implement RBAC permissions for resource booking
- Add CSP-compliant delete confirmation modal
- Verify multi-tenant data isolation

Proceed with implementation?
```

**Decision Point 2** (After implementation):
```
✅ Implementation completed.

Security Changes:
- Added @permission_required('coordination.delete_resourcebooking')
- Implemented organization filtering on all queries
- Updated delete modal with nonce-based script
- CSP compliance verified ✅

Run /coditor security audit?
```

**Decision Point 3** (After coditor):
```
✅ /coditor security audit completed.

Findings:
- Critical: 0 ✅
- High: 0 ✅
- Medium: 1 (documentation improvement)

Security implementation approved. Ready to deploy?
```

### Success Criteria

- ✅ CSP compliance verified (GEMINI.md Rule 12)
- ✅ Multi-tenant data isolation verified
- ✅ Authentication/authorization implemented
- ✅ Input validation implemented
- ✅ Security tests pass
- ✅ Coditor security audit: Critical/High = 0

### Estimated Timeline

- **Planning**: 30-60 min
- **Implementation**: 2-4 hours
- **Testing**: 1 hour
- **Audit**: 30-60 min
- **Deployment**: 30 min
- **Total**: 4.5-7 hours

---

## Template 6: AI Feature (obcAI)

### Trigger
- User requests AI-powered feature using obcAI
- Keywords: "obcAI", "AI", "agent", "specialist", "ADK"

### Full Workflow

```
[Workflow: AI Feature Development]

Phase 1: AI Planning (1-2 hours)
└─ 1. /obcai-engineer
    Purpose: ADK implementation patterns, specialist agent design
    Output: Agent design, function tools specification
    Focus: Gemini (primary), Zhipu GLM 4.6 (fallback), multi-tenant isolation

Phase 2: Implementation (3-5 hours)
├─ 2. /backend
│   Purpose: Django integration with ADK agents
│   Output: Function tools, coordinator integration, Django views/APIs
│
└─ 3. /frontend (if needed)
    Purpose: UI for AI chat/features
    Output: AI chat widget, HTMX interactions
    Critical: CSP compliance for AI UI

Phase 3: Testing (1-2 hours)
├─ 4. /unit-tests
│   Purpose: Test AI functions
│   Output: Function tool tests, agent tests
│
└─ 5. /coditor
    Purpose: Audit AI implementation
    Output: AI audit (multi-tenant isolation, token optimization)

Phase 4: Deployment (30 min)
└─ 6. /devops
    Purpose: Deployment guidance
    User Action: Deploy AI feature
```

### AI-Specific Considerations

**Multi-Tenant Isolation**:
- Organization-scoped function tools
- Filter data by organization in all queries
- User context passed to all agents

**Token Optimization**:
- Use Gemini (primary, cost-effective)
- Fallback to Zhipu GLM 4.6 (if Gemini fails)
- Caching for common queries
- Minimize token usage in prompts

**ADK Patterns**:
- Specialist agents (Geographic, Community, MANA, etc.)
- Function tools (wrapped functions)
- Coordinator routing (intent detection)

### Decision Points

**Decision Point 1** (After AI planning):
```
✅ /obcai-engineer planning completed.

AI Feature Plan:
- Specialist: Policy Recommendation Agent
- Function Tools:
  1. query_policies(organization, domain)
  2. analyze_policy_impact(policy_id, community_ids)
  3. generate_recommendations(context)
- Coordinator Routing: "policy" intent → Policy Specialist

Proceed with implementation?
```

**Decision Point 2** (After implementation):
```
✅ Implementation completed.

AI Components:
- Policy Specialist agent created
- 3 function tools implemented (with organization filtering)
- Coordinator routing updated
- Django API endpoints: /api/ai/policy/recommend/

Run /unit-tests for AI functions?
```

**Decision Point 3** (After testing):
```
✅ AI tests completed.

Results:
- Function tools: All tests pass ✅
- Multi-tenant isolation: Verified ✅
- Token usage: Average 1,200 tokens/query
- Gemini API: Working ✅
- Fallback to Zhipu GLM 4.6: Tested ✅

Run /coditor audit?
```

### Success Criteria

- ✅ Specialist agent designed and implemented
- ✅ Function tools with multi-tenant isolation
- ✅ Coordinator routing configured
- ✅ Django integration complete
- ✅ UI implemented (if needed, CSP-compliant)
- ✅ Tests pass
- ✅ Token optimization implemented
- ✅ Coditor audit passed

### Estimated Timeline

- **Planning**: 1-2 hours
- **Implementation**: 3-5 hours
- **Testing**: 1-2 hours
- **Audit**: 30-60 min
- **Deployment**: 30 min
- **Total**: 6-10 hours

---

## Using Workflow Templates

### How AppManager Uses Templates

1. **Detect Request** → Match to template trigger
2. **Select Template** → Choose appropriate template
3. **Present Workflow** → Show full workflow to user
4. **Track State** → Track progress through workflow steps
5. **Guide User** → Ask permission at each decision point

### Example: Template Selection

```
User: "Add resource booking calendar"

AppManager Analysis:
- Keywords: "add" (new feature)
- Domain: Full-stack (calendar UI + booking logic)
- Complexity: Complex

Template Selected: Template 1 (New Feature Development)

Recommendation:
"I detect this is a New Feature Development request. I recommend the full feature development workflow:

1. /featuredev - Plan feature
2. /frontend - Build FullCalendar UI
3. /backend - Implement booking models/API
4. /unit-tests - Test functionality
5. /integration-tests - Test workflow
6. /coditor - Pre-deployment audit
7. /devops - Deployment guidance

This will take approximately 7-13 hours (1-2 days).

Shall I invoke /featuredev now to start planning?"
```

---

## Template Customization

Templates can be customized based on:
- **Urgency**: Expedited workflows for critical issues
- **Complexity**: Simplified workflows for simple tasks
- **Domain**: Domain-specific skill substitutions
- **Phase**: Resume from current phase if interrupted

### Example: Expedited Bug Fix (Critical)

```
Standard Bug Fix Template: 6 steps, 2-4 hours

Expedited (Critical):
1. /investigator (15 min, quick research)
2. /debugger (30 min, fast)
3. Fix (immediate)
4. /unit-tests (critical paths only)
5. Deploy ASAP
Total: 1-1.5 hours

Skip: /coditor (do after deployment)
```

---

**Remember**: Workflow templates are guides, not rigid rules. AppManager adapts templates based on context, urgency, and user feedback.


---

# Quick Start Examples (from SKILL.md)

## Quick Start Examples

### Example 1: User Asks for New Feature

**User**: "I need to add a product catalog filter to the marketplace"

**AppManager Response**:
```
I detect this is a **New Feature Development** request in the **Architecture** phase.

Recommended workflow:
1. /featuredev - Plan the filter feature (FDD methodology)
2. /frontend - Build filter UI (React + TanStack Query)
3. /backend - Implement Django Ninja filter endpoints
4. /unit-tests - Verify functionality
5. /coditor - Audit before deployment

Let's start with feature planning. Shall I invoke /featuredev now?
```

### Example 2: User Reports Bug

**User**: "Users are seeing products from other organizations!"

**AppManager Response**:
```
This is a **Critical** multi-tenant data leak issue!

Recommended immediate workflow:
1. /investigator - Research multi-tenant data leak patterns (URGENT)
2. /security - Review multi-tenant security patterns
3. /backend - Fix organization filtering in Django Ninja
4. /unit-tests - Verify fix
5. /coditor - Audit entire codebase for similar leaks

This is high-priority. Shall I invoke /investigator now to identify the root cause?
```

### Example 3: User Wants to Deploy

**User**: "Deploy to staging"

**AppManager Response**:
```
Before deploying to staging, I recommend the **Deployment Workflow**:

1. /safety-first - Verify no uncommitted changes
2. /coditor - Comprehensive audit (all Critical/High findings must be fixed)
3. /unit-tests - Verify all tests pass
4. /devops - Deployment guidance (you'll execute git push manually)

This ensures safe deployment. Shall I invoke /safety-first now?
```

---

**Remember**: AppManager recommends and guides, but **you control all skill invocations**. AppManager will never invoke a skill without your explicit permission.
