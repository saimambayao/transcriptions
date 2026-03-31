# Root Cause Analysis (RCA)

Systematic techniques for identifying the true underlying cause of bugs, not just symptoms.

## What is Root Cause Analysis?

**Root Cause:** The fundamental reason a problem occurred - if eliminated, the problem won't recur.

**Symptom:** The visible manifestation of the problem - fixing symptoms without addressing root causes leads to recurring bugs.

### Example:

```
Symptom: "Users can see other organizations' data"
Surface Fix: Add organization filter to this one view
Root Cause: Missing organization scoping in base queryset
Permanent Fix: Add OrganizationScopedMixin to model
```

## The Five Whys Technique

**Developed by Sakichi Toyoda (Toyota Production System)**

Ask "Why?" five times to drill down from symptom to root cause.

### Example 1: Budget Approval Bug

```
Problem: Users cannot approve budget requests

Why #1: The approve button returns 403 Forbidden error
         → Look at server logs, confirm 403 status

Why #2: User doesn't have 'approve_budgetrequest' permission
         → Check user.get_all_permissions() in Django shell

Why #3: Permission wasn't added to the user's role during migration
         → Review migration files, permission not created

Why #4: Migration script didn't account for existing users
         → Migration only creates permission, doesn't assign it

Why #5: We didn't test the migration against staging data
         → No staging test in deployment checklist

ROOT CAUSE: Incomplete migration testing process
PERMANENT FIX:
1. Create data migration to assign permission to existing roles
2. Add "test migrations on staging" to deployment checklist
3. Add permission check to pre-deployment testing
```

### Example 2: HTMX Swap Failure

```
Problem: Delete button doesn't remove item from list

Why #1: HTMX request succeeds (200 OK) but DOM doesn't update
         → Check Network tab, request successful

Why #2: HTMX can't find target element with ID "item-list"
         → Check Elements tab, ID is actually "items-list" (plural)

Why #3: Template was refactored but HTMX attribute wasn't updated
         → Git blame shows ID changed 2 weeks ago

Why #4: No test caught the ID mismatch
         → UI tests don't check HTMX element targeting

Why #5: We don't have systematic UI testing for HTMX interactions
         → No UI testing checklist exists

ROOT CAUSE: Missing UI test coverage for HTMX interactions
PERMANENT FIX:
1. Fix ID mismatch: hx-target="#items-list"
2. Add UI test for delete functionality
3. Create HTMX testing checklist
4. Add HTMX attribute validation to code review process
```

## Fishbone (Ishikawa) Diagram

Visual method to categorize potential causes.

```
                                    Problem
                                       │
            ┌──────────────────────────┼──────────────────────────┐
            │                          │                          │
        People                     Process                   Technology
            │                          │                          │
    - Wrong permissions        - Skipped testing          - Django bug?
    - Misconfigured role       - No staging verify        - HTMX issue?
    - User error              - Missing checklist        - Browser compatibility
            │                          │                          │
            └──────────────────────────┴──────────────────────────┘
                                       │
                                  ROOT CAUSE
```

**How to use:**
1. Draw main problem on the right
2. Add major categories as "bones"
3. Brainstorm causes in each category
4. Investigate most likely causes
5. Test hypotheses systematically

### Categories for Software Bugs

**People:**
- Misunderstood requirements
- Lack of knowledge/experience
- Communication breakdown

**Process:**
- Skipped testing
- No code review
- Incomplete requirements
- Poor deployment process

**Technology:**
- Framework bugs
- Library incompatibilities
- Environment differences
- Browser issues

**Data:**
- Invalid data in database
- Missing test data
- Data corruption
- Schema mismatch

## Hypothesis-Driven RCA

Systematic approach to testing potential root causes.

### 1. List All Possible Causes

**For "403 Forbidden on Budget Approval":**

```
Hypothesis A: User doesn't have permission
Hypothesis B: CSRF token missing from request
Hypothesis C: User trying to approve own request (business rule)
Hypothesis D: Budget request is no longer in "pending" status
Hypothesis E: Organization mismatch (multi-tenancy issue)
Hypothesis F: View decorator checking wrong permission
```

### 2. Gather Supporting Evidence

**Hypothesis A: User doesn't have permission**

Evidence FOR:
- ✅ Error code is 403 (permission-related)
- ✅ Django shell shows user lacks permission
- ✅ Log shows PermissionDenied exception

Evidence AGAINST:
- ❌ User has "Admin" role which should have all permissions
- ❌ Same user can perform other admin actions

**Verdict:** Partially supported - permission missing but shouldn't be

---

**Hypothesis B: CSRF token missing**

Evidence FOR:
- ❓ Request is POST (CSRF required)

Evidence AGAINST:
- ❌ Error is 403 not 403 CSRF
- ❌ Network tab shows CSRF token in request
- ❌ Other POST requests work fine

**Verdict:** Not supported - CSRF token present

---

**Hypothesis C: Business rule violation**

Evidence FOR:
- ❓ User created the request themselves

Evidence AGAINST:
- ❌ Business logic check would return 400, not 403
- ❌ Error message doesn't mention business rule

**Verdict:** Not supported

### 3. Test Most Likely Hypothesis

**Test Hypothesis A:**

```python
# Django shell
from common.models import User
from django.contrib.auth.models import Permission

user = User.objects.get(username='testadmin')

# Check permission
has_perm = user.has_perm('myapp.approve_budgetrequest')
print(f"Has approve permission: {has_perm}")  # False

# Check if permission exists
perm = Permission.objects.filter(codename='approve_budgetrequest')
print(f"Permission exists: {perm.exists()}")  # True

# Check role permissions
role = user.role
role_perms = role.permissions.all()
print(f"Role permissions: {list(role_perms)}")
# ['view_budgetrequest', 'add_budgetrequest'] - missing approve!

# ROOT CAUSE CONFIRMED: Permission exists but not assigned to role
```

## Trace Analysis

Follow the execution path to find where things go wrong.

### Request Flow Tracing

**Django Request Flow:**
```
1. Browser → POST /budget/requests/123/approve/
2. Django URLs → Match to view: budget_approval_approve
3. Middleware → Check CSRF token ✅
4. Middleware → Check authentication ✅
5. View Decorator → @require_permission('myapp.approve_budgetrequest') ❌
                    → User doesn't have permission
                    → Raise PermissionDenied (403)
6. Exception Handler → Return 403 Forbidden page

ROOT CAUSE: Permission check fails at step 5
```

### Code Path Tracing

**Using logging:**

```python
import logging
logger = logging.getLogger(__name__)

@login_required
@require_permission('myapp.approve_budgetrequest')
def budget_approval_approve(request, pk):
    logger.debug(f"Step 1: View called by user {request.user}")

    approval = get_object_or_404(BudgetApproval, pk=pk)
    logger.debug(f"Step 2: Found approval {approval.id}")

    logger.debug(f"Step 3: Checking permissions")
    if not request.user.has_perm('myapp.approve_budgetrequest'):
        logger.error(f"Step 3 FAILED: User lacks permission")
        return HttpResponseForbidden()

    logger.debug(f"Step 4: Permissions OK, approving")
    approval.approve(request.user)

    logger.debug(f"Step 5: Approval complete")
    return redirect('budget_list')
```

**Log output reveals:**
```
DEBUG Step 1: View called by user testadmin
DEBUG Step 2: Found approval 123
DEBUG Step 3: Checking permissions
ERROR Step 3 FAILED: User lacks permission
```

## Comparative Analysis

Compare working vs. broken cases to find the difference.

### Example: Why does it work for User A but not User B?

**User A (works):**
```python
user_a = User.objects.get(username='admin1')
print(f"Organization: {user_a.organization.id}")  # Org 1
print(f"Role: {user_a.role.name}")  # Admin
print(f"Permissions: {list(user_a.get_all_permissions())}")
# ['myapp.approve_budgetrequest', 'myapp.view_budgetrequest', ...]
```

**User B (broken):**
```python
user_b = User.objects.get(username='admin2')
print(f"Organization: {user_b.organization.id}")  # Org 2
print(f"Role: {user_b.role.name}")  # Admin
print(f"Permissions: {list(user_b.get_all_permissions())}")
# ['myapp.view_budgetrequest', 'myapp.add_budgetrequest']
# Missing: approve_budgetrequest
```

**Difference found:**
```
User A's role has approve permission
User B's role doesn't have approve permission

Why? Check role creation:
- Org 1: Role created after migration (has permission)
- Org 2: Role created before migration (missing permission)

ROOT CAUSE: Migration adds permission but doesn't assign to existing roles
```

## Timeline Analysis

Identify when the bug started to find the cause.

### Example Timeline:

```
Oct 20: Feature deployed to production
Oct 20-25: No errors reported
Oct 26: First error report (User from Org 2)
Oct 27: 3 more errors (all from Org 2)
Oct 28: Error investigation begins

What changed?
- Oct 25: Added new organization (Org 2)
- Org 2 created with admin role
- Migration had already run (Oct 20)
- Org 2's admin role missing new permission

ROOT CAUSE: Timing issue - role created after migration
FIX: Migrations must handle both new and existing roles
```

## Dependency Analysis

Trace dependencies to find interconnected causes.

```
Budget Approval depends on:
├── User
│   ├── Organization (multi-tenant scope)
│   ├── Role
│   │   └── Permissions ← MISSING
│   └── is_active status
├── BudgetRequest
│   ├── status = 'pending'
│   ├── organization matches user
│   └── not soft-deleted
└── Permission
    └── approve_budgetrequest exists in DB

Dependency check reveals:
✅ User exists and active
✅ Organization matches
✅ Role exists
❌ Permission not in role.permissions
✅ BudgetRequest valid
✅ Permission exists in Permission table

ROOT CAUSE: Missing link between Role and Permission
```

## Anti-Patterns to Avoid

### ❌ Stopping at Symptoms

```
Problem: App crashes with "NoneType has no attribute 'organization'"
Bad Fix: Add if statement to check for None
Good RCA: Why is the object None? Should it ever be None?
```

### ❌ Blaming External Factors Too Quickly

```
Problem: Query is slow
Bad conclusion: "PostgreSQL is slow"
Good RCA: Check query structure, indexes, N+1 queries first
```

### ❌ Accepting First Explanation

```
Problem: User can't login
First Why: Password is wrong
Stop? NO - keep asking why
Why is password wrong? User forgot it
Why did they forget? Too complex
Why is it complex? Password policy changed
Why changed? Security requirement added
ROOT CAUSE: New policy wasn't communicated to users
```

## RCA Documentation Template

```markdown
# Root Cause Analysis: [Bug Title]

## Problem Statement
[Clear description of the observable bug]

## Impact
- Affected users: [number/role/organization]
- Severity: CRITICAL / HIGH / MEDIUM / LOW
- First occurrence: [date/time]
- Frequency: [always / intermittent]

## Investigation Timeline
- [Date]: Bug reported
- [Date]: Reproduction confirmed
- [Date]: Root cause identified
- [Date]: Fix implemented

## Root Cause Analysis

### Five Whys
1. Why? [Answer]
2. Why? [Answer]
3. Why? [Answer]
4. Why? [Answer]
5. Why? [Answer]

**Root Cause:** [Fundamental underlying issue]

### Supporting Evidence
- [Evidence item 1]
- [Evidence item 2]
- [Evidence item 3]

### Contributing Factors
1. [Factor 1 - e.g., missing test coverage]
2. [Factor 2 - e.g., unclear requirements]

## Solution

### Immediate Fix
[What was changed to fix the bug]

### Long-term Prevention
1. [Prevention measure 1]
2. [Prevention measure 2]
3. [Prevention measure 3]

### Tests Added
- [Test 1 to prevent regression]
- [Test 2 to catch similar issues]

## Lessons Learned
[What was learned from this incident]

## Action Items
- [ ] [Action 1]
- [ ] [Action 2]
- [ ] [Action 3]
```

## Summary

**Effective RCA Process:**
1. Identify the symptom clearly
2. Use Five Whys to dig deeper
3. Gather evidence for each hypothesis
4. Test hypotheses systematically
5. Trace execution paths
6. Compare working vs. broken cases
7. Analyze timeline and dependencies
8. Document root cause thoroughly
9. Implement both fix and prevention

**Key Principle:** Keep asking "Why?" until you reach a cause that, if fixed, prevents the problem from recurring.
