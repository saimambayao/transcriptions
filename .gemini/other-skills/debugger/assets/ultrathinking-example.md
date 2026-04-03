# Ultrathinking Workflow Example

Real-world walkthrough of the multi-agent debugging process.

## Scenario: Budget Approval 403 Error

**Initial Report:**
```
Error: Users cannot approve budget requests
Status: 403 Forbidden
Environment: Production
Affected: All admin users in Organization #2
First Occurrence: 2025-10-31 14:30 UTC
```

---

## Step 0: Check Error History

**Main Claude checks error log:**

```bash
grep -i "budget.*403\|permission.*budget" docs/error-logs/error_log.md
```

**Result:** No matching errors found in history

**Decision:** This is a new error → Proceed to Step 1

---

## Step 1: Audit Logs

**Main Claude gathers initial evidence:**

```bash
# Capture Railway logs
railway logs --tail 200 > railway-logs-20251031-1430.txt

# Review logs
grep -i "403\|forbidden\|permission" railway-logs-20251031-1430.txt
```

**Key findings from logs:**
```
[2025-10-31 14:30:15] ERROR PermissionDenied at /budget/requests/123/approve/
[2025-10-31 14:30:15] User: admin@org2.com (ID: 45, Org: 2)
[2025-10-31 14:30:15] Required permission: myapp.approve_budgetrequest
[2025-10-31 14:30:15] User permissions: ['myapp.view_budgetrequest', 'myapp.add_budgetrequest']
```

**Initial observations:**
- Error: Permission-related (403 PermissionDenied)
- Frequency: Consistent (all attempts fail)
- Scope: Organization #2 only
- Pattern: Admin users missing 'approve_budgetrequest' permission

**Log error:**
```bash
echo "### [2025-10-31 14:30] | BudgetApprovalPermissionError
**Status:** 🔍 INVESTIGATING
**Category:** permissions
**Severity:** HIGH
**Description:** Admin users in Org #2 cannot approve budget requests - 403 Forbidden
" >> docs/error-logs/error_log.md
```

---

## Phase 1: Parallel Investigation

### Launch Agent 1: Codebase Investigation

**Task given to Explore agent:**
```
Investigate this permission error in OBCMS:

Error: 403 Forbidden when admin tries to approve budget requests
Logs show: User missing 'myapp.approve_budgetrequest' permission
Environment: Production, Organization #2 only
User role: Admin (should have all permissions)

Investigation requirements:
1. Find where 'approve_budgetrequest' permission is created
2. Check how permissions are assigned to Admin role
3. Review recent migrations that may have added this permission
4. Check if Organization #1 admins have this permission (comparison)
5. Identify OBCMS permission assignment patterns

Tools: Glob, Grep, Read, Bash (git history)
```

**Agent 1 Investigation Results:**

```markdown
# Agent 1: Codebase Investigation Report

## Permission Creation
Found in: `src/myapp/models.py:45`
```python
class BudgetApproval(models.Model):
    class Meta:
        permissions = [
            ('approve_budgetrequest', 'Can approve budget requests'),
        ]
```

## Migration History
- Permission added in migration: `0015_budgetapproval_permissions.py` (Oct 20)
- Migration creates permission but doesn't assign to roles
- No data migration to assign to existing roles

## Git Blame
```
git log --oneline --grep="approve" -- src/myapp/
abc123d Add budget approval feature (Oct 20)
```

## Comparison: Org #1 vs Org #2
Using Django shell simulation:
- Org #1 created: Oct 15 (before migration)
- Org #2 created: Oct 25 (after migration)
- Org #1 admin role has permission (manually added)
- Org #2 admin role missing permission

## Root Cause Hypothesis
Migration creates permission but doesn't assign it to existing or new admin roles.
Org #1 had permission manually added later, Org #2 was never updated.
```

### Launch Agent 2: Online Research

**Task given to general-purpose agent:**
```
Research Django permission management best practices:

Context: Permission added via migration but not assigned to roles
Error: New organizations don't have permission on admin role
Tech: Django 5.2, multi-tenant with role-based permissions

Research requirements:
1. Django best practices for permission management
2. How to assign permissions to roles in migrations
3. Common pitfalls with permission migrations
4. Multi-tenant permission patterns

Use WebSearch for 2024-2025 Django docs and Stack Overflow
```

**Agent 2 Research Results:**

```markdown
# Agent 2: Online Research Report

## Django Permission Best Practices (2025)

Source: Django 5.2 Documentation
- Permissions should be assigned in data migrations
- Create permission → Assign to groups/roles in same migration
- Never rely on manual permission assignment

## Common Pattern
```python
def assign_permissions(apps, schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    Group = apps.get_model('auth', 'Group')

    # Get permission
    perm = Permission.objects.get(codename='approve_budgetrequest')

    # Assign to admin group/role
    admin_role = Group.objects.get(name='Admin')
    admin_role.permissions.add(perm)
```

## Multi-Tenant Considerations
From Stack Overflow (2025):
- In multi-tenant apps, permissions should be assigned to roles per organization
- Data migrations must handle existing AND future organizations
- Use signals or override role creation to auto-assign

## Common Pitfall (Exact Issue!)
"Permission created but not assigned to roles" - top Django issue
- Solution: Always use data migration to assign permissions
- Reference: https://stackoverflow.com/questions/12345678/ (1,234 votes)

## Recommendation
Create data migration that:
1. Gets or creates permission
2. Loops through all organizations
3. Assigns permission to admin role for each org
```

**⏸️ WAIT for both agents**

---

## Phase 2: Fix Plan Synthesis

**Main Claude synthesizes findings:**

```markdown
# Fix Plan: Budget Approval Permission Error

## Root Cause
Migration `0015_budgetapproval_permissions.py` created the
'approve_budgetrequest' permission but didn't assign it to existing
admin roles. Organizations created after the migration also don't get
this permission assigned automatically.

**Evidence:**
- **Codebase (Agent 1):** Permission defined but no assignment logic
- **Research (Agent 2):** Django best practice requires data migration
- **Logs:** User has Admin role but missing specific permission

## Proposed Fix

### 1. Create Data Migration
**File:** `src/myapp/migrations/0016_assign_approve_permission.py`

```python
from django.db import migrations

def assign_approve_permission(apps, schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    Organization = apps.get_model('common', 'Organization')
    Role = apps.get_model('common', 'Role')

    # Get the permission
    try:
        perm = Permission.objects.get(
            content_type__app_label='myapp',
            codename='approve_budgetrequest'
        )
    except Permission.DoesNotExist:
        return  # Permission doesn't exist yet

    # Assign to admin role for all organizations
    for org in Organization.objects.all():
        admin_role = Role.objects.filter(
            organization=org,
            name='Admin'
        ).first()

        if admin_role:
            admin_role.permissions.add(perm)

class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0015_budgetapproval_permissions'),
    ]

    operations = [
        migrations.RunPython(
            assign_approve_permission,
            reverse_code=migrations.RunPython.noop
        ),
    ]
```

### 2. Update Role Creation
**File:** `src/common/models/roles.py`

Ensure new admin roles get this permission automatically:
```python
# In Role.create_default_roles() method
admin_permissions.append('myapp.approve_budgetrequest')
```

## Verification Steps
1. Run migration locally
2. Check Org #2 admin has permission: `user.has_perm('myapp.approve_budgetrequest')`
3. Create new org, verify admin role has permission
4. Test in staging
5. Deploy to production

## Regression Test
```python
# test_permissions.py
def test_admin_has_approve_permission(admin_user):
    """Ensure all admin users can approve budget requests."""
    assert admin_user.has_perm('myapp.approve_budgetrequest')

def test_new_org_admin_has_permission(db):
    """New organizations' admins should have permission."""
    org = Organization.objects.create(name="New Org")
    Role.create_default_roles(org)
    admin_role = Role.objects.get(organization=org, name='Admin')
    assert admin_role.permissions.filter(
        codename='approve_budgetrequest'
    ).exists()
```

## Prevention
1. Update deployment checklist: "Verify all permissions assigned in migrations"
2. Add CI check: Test that default roles have expected permissions
3. Document: All new permissions must include data migration for assignment
```

---

## Phase 3: Validation

**Launch Agent 3 for independent validation:**

**Task:**
```
INDEPENDENT VALIDATION

Fix Plan: [paste entire fix plan above]

Re-investigate independently:
1. ACCURACY: Re-read logs, re-search codebase - is root cause correct?
2. COMPLETENESS: Are there edge cases? Related issues?
3. ALIGNMENT: Does fix follow OBCMS/Django best practices?

Do NOT just review - actually investigate again yourself.
```

**Agent 3 Validation Report:**

```markdown
# Validation Report: Budget Approval Permission Error

## Overall Assessment: ✅ APPROVE WITH MINOR RECOMMENDATIONS

## Accuracy Validation ✅
Re-investigated independently:
- ✅ Confirmed permission exists but not assigned
- ✅ Verified Org #2 admin missing permission
- ✅ Checked migration history - matches findings
- ✅ Root cause is accurate

## Completeness Check ⚠️
Missing considerations:
1. **Edge case:** What about Manager role? Should they also have permission?
   - Current fix only handles Admin role
   - Recommend checking if Manager needs this permission too

2. **Related issue:** Other permissions may have same problem
   - Grep search found 3 other permissions added without assignment
   - Recommend: Fix all similar permission issues in same migration

3. **Future prevention:** No automatic check
   - Recommend: Add test to CI that validates default permissions

## Standards Alignment ✅
- ✅ Django best practice (data migration for permissions)
- ✅ OBCMS multi-tenant pattern (per-organization roles)
- ✅ Proper migration reversibility (noop reverse)
- ✅ Test coverage included

## Additional Recommendations
1. **Extend migration to handle Manager role if needed**
   ```python
   for role_name in ['Admin', 'Manager']:
       role = Role.objects.filter(org=org, name=role_name).first()
       if role:
           role.permissions.add(perm)
   ```

2. **Add permission matrix documentation**
   - Document which roles should have which permissions
   - Reference: docs/permissions/role-permission-matrix.md

3. **Add monitoring**
   - Alert if admin user lacks expected permission
   - Periodic check: All admins have core permissions

## Verdict
✅ APPROVE - Root cause correct, fix is sound

Implement with minor enhancements:
- Extend to Manager role (confirm with user first)
- Add permission matrix documentation
- Consider fixing similar permission issues
```

**⏸️ WAIT for validation**

---

## Phase 4: Finalization & User Presentation

**Main Claude reviews Agent 3 feedback:**
- Validation: APPROVED
- Good point about Manager role
- Good point about documenting permission matrix

**Main Claude creates user summary:**

```markdown
# Budget Approval Permission Error - Fix Summary

## Problem
Admin users in Organization #2 cannot approve budget requests (403 Forbidden).

## Root Cause
Migration created 'approve_budgetrequest' permission on Oct 20 but didn't
assign it to existing admin roles. Org #2 was created on Oct 25 (after
migration) and never received the permission.

## Proposed Solution
1. Create data migration to assign permission to all existing admin roles
2. Update role creation to include permission for new organizations
3. Add regression tests to prevent recurrence

## Code Changes
- New migration: `0016_assign_approve_permission.py` (28 lines)
- Update: `common/models/roles.py` (1 line)
- New tests: `test_permissions.py` (15 lines)

## Testing Plan
- Unit tests: Verify permission assigned to all admins
- Integration test: Test approval workflow end-to-end
- Staging: Test with Org #2 admin user

## Additional Question
Agent 3 validation suggests: Should Manager role also have this permission?
(Currently fixing for Admin only)

## Risk Assessment
- Risk: LOW (permission assignment only, no schema change)
- Rollback: Migration is reversible
- Impact: Fixes issue for all affected organizations

---

**Approval Needed:**
1. Proceed with fix as proposed?
2. Should Manager role also get approve permission? (yes/no)
```

**🛑 WAIT FOR USER APPROVAL**

---

## User Response

**User:** "Yes, proceed. Yes, Manager should also have approve permission."

---

## Implementation

**Main Claude implements approved fix:**

1. **Create migration** (with Manager role added per user feedback)
2. **Update role creation**
3. **Add tests**
4. **Run tests locally** - All pass ✅
5. **Deploy to staging**
6. **Verify in staging** - Org #2 admin can now approve ✅
7. **Deploy to production**
8. **Verify in production** - Issue resolved ✅

**Final documentation:**

```bash
# Update error log
sed -i '' 's/🔍 INVESTIGATING/✅ FIXED/' docs/error-logs/error_log.md

# Create detailed report
cat > docs/error-logs/permissions/20251031-1430-budget-approval-403.md <<EOF
[Complete error report with all investigation details,
 agent findings, validation results, and final implementation]
EOF
```

---

## Outcome

**Error resolved:** ✅ All admin and manager users can approve budget requests

**Investigation quality:**
- Root cause: Accurately identified by Agent 1
- Solution: Validated best practice from Agent 2
- Validation: Agent 3 caught missing edge case (Manager role)
- User input: Incorporated into final fix

**Time:**
- Traditional debugging: Estimated 2-3 hours (trial and error)
- Ultrathinking: 45 minutes (comprehensive, validated, documented)

**Prevention:**
- Tests added to prevent regression
- Documentation updated
- Process improved (permission assignment checklist)

---

## Lessons Learned

**What worked well:**
1. Parallel investigation (Agent 1 + Agent 2) was faster than sequential
2. Agent 3 validation caught edge case we missed (Manager role)
3. User approval prevented implementing incomplete fix
4. Comprehensive documentation from agent reports

**What could improve:**
1. Could have caught Manager role issue in Phase 2 (before validation)
2. Could have checked for similar permission issues proactively

**Key takeaway:** Multi-agent validation prevented shipping incomplete fix!
