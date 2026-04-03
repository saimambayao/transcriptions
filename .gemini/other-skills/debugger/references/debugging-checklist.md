# Debugging Checklist

Quick reference checklist to ensure thorough debugging following the 7-step workflow.

## Pre-Debugging Checklist

Before starting any debugging investigation:

- [ ] Error message captured completely (full stack trace)
- [ ] Environment identified (dev / staging / production)
- [ ] User role and organization noted (multi-tenancy)
- [ ] Browser and version noted (for frontend issues)
- [ ] Reproduction steps documented
- [ ] Expected vs. actual behavior clear

## Step 1: Reproduce the Issue

- [ ] Bug reproduced successfully at least 3 times
- [ ] Exact steps documented
- [ ] All required conditions identified (user role, data state, etc.)
- [ ] Reproduction rate noted (e.g., 5/5 attempts = 100%)
- [ ] Screenshots or screen recording captured
- [ ] Error appears in logs (if applicable)
- [ ] Same error in different environments tested

**If you can't reproduce:**
- [ ] Tried with different users/organizations
- [ ] Checked if environment-specific (local vs. production)
- [ ] Verified database state matches reported issue
- [ ] Confirmed all dependencies installed
- [ ] Checked if timing-dependent (race condition)

## Step 2: Isolate the Problem

- [ ] Layer identified (model / view / template / API / frontend)
- [ ] Specific file and function identified
- [ ] Binary search performed (commented out code sections)
- [ ] Minimal reproduction case created
- [ ] Unrelated code eliminated from investigation
- [ ] Dependencies checked (framework bug vs. our code)

**Django-specific:**
- [ ] View function identified
- [ ] Model identified
- [ ] Template identified (if frontend)
- [ ] URL pattern verified

**HTMX-specific:**
- [ ] HTMX attribute identified (hx-get, hx-post, etc.)
- [ ] Target element verified exists
- [ ] Swap method checked (innerHTML, outerHTML, etc.)

## Step 3: Gather Evidence

- [ ] Django logs captured (`tail -f logs/django.log`)
- [ ] Railway logs saved (`railway logs --tail 200 > debug.log`)
- [ ] Browser console errors captured
- [ ] Network tab requests inspected
- [ ] Stack trace saved completely
- [ ] Database state checked (Django shell)
- [ ] HTMX events logged (`htmx.logAll()`)
- [ ] Environment variables verified

**For Production Issues:**
- [ ] Production logs saved with timestamp
- [ ] Recent deployments reviewed (`git log --oneline -10`)
- [ ] Database migrations status checked
- [ ] Environment variables compared (staging vs. production)

## Step 4: Formulate Hypotheses

- [ ] At least 3 hypotheses listed
- [ ] Evidence supporting each hypothesis noted
- [ ] Evidence contradicting each hypothesis noted
- [ ] Hypotheses ranked by likelihood
- [ ] Test plan for each hypothesis created
- [ ] Five Whys performed (if root cause unclear)

**Common hypotheses checked:**
- [ ] Organization scoping issue (multi-tenancy)
- [ ] Missing permission
- [ ] HTMX targeting issue
- [ ] CSRF token missing
- [ ] Migration not applied
- [ ] Soft-deleted record accessed
- [ ] Wrong environment variable

## Step 5: Test Hypotheses

- [ ] Most likely hypothesis tested first
- [ ] Debugging tool chosen (pdb / IDE debugger / Django shell)
- [ ] Breakpoints set at critical points
- [ ] Variables inspected at time of error
- [ ] Hypothesis confirmed or rejected with evidence
- [ ] Root cause identified definitively

**Testing tools used:**
- [ ] Python debugger (pdb) if code logic issue
- [ ] Django shell if database query issue
- [ ] Browser DevTools if frontend issue
- [ ] Network tab if AJAX/HTMX issue
- [ ] Django Debug Toolbar if performance issue

**Verification:**
- [ ] Root cause addresses the symptom
- [ ] Root cause explains all observed behavior
- [ ] No contradicting evidence exists

## Step 6: Implement Fix

- [ ] Fix addresses root cause (not just symptoms)
- [ ] Code follows OBCMS standards
- [ ] Multi-tenancy preserved (organization scoping)
- [ ] CSRF protection maintained
- [ ] CSP compliance verified (no inline styles/scripts)
- [ ] Soft delete behavior preserved
- [ ] Fix tested locally
- [ ] Original bug verified as fixed
- [ ] No regressions introduced

**For Schema Changes:**
- [ ] Migration created (`makemigrations`)
- [ ] Migration tested locally (`migrate`)
- [ ] Migration reversible (`migrate app zero`)
- [ ] Migration tested on staging data

**For Permission Changes:**
- [ ] Permission created in database
- [ ] Permission assigned to correct roles
- [ ] All affected users verified

**For HTMX Changes:**
- [ ] Target element verified exists
- [ ] HTMX attributes correct
- [ ] Response format correct
- [ ] Loading states added
- [ ] Error handling added

## Step 7: Document & Prevent

- [ ] Error logged in `docs/error-logs/error_log.md`
- [ ] Detailed error report created
- [ ] Root cause documented
- [ ] Fix documented
- [ ] Prevention measures identified
- [ ] Tests added to prevent regression
- [ ] Deployment checklist updated (if needed)
- [ ] Team notified (if applicable)

**Regression Prevention:**
- [ ] Unit test added for the bug
- [ ] Integration test added (if workflow bug)
- [ ] UI test added (if frontend bug)
- [ ] Test verifies fix works
- [ ] Test would catch similar bugs

**Documentation:**
- [ ] Error log entry complete
- [ ] Detailed report saved in correct category
- [ ] Code comments added (if complex fix)
- [ ] Internal wiki updated (if applicable)

## Testing Checklist

Before declaring bug fixed:

- [ ] Original reproduction steps no longer cause error
- [ ] Test suite passes (`pytest --cov`)
- [ ] Coverage not decreased
- [ ] Fix tested in staging environment
- [ ] No new console errors
- [ ] No new warnings in logs
- [ ] Related features still work
- [ ] Multi-tenant isolation verified
- [ ] Performance not degraded

**HTMX-specific testing:**
- [ ] HTMX swap works correctly
- [ ] Loading indicator shows
- [ ] Error handling works
- [ ] Tested 3 times to ensure consistency
- [ ] No console errors

**Permission testing:**
- [ ] Authorized users can perform action
- [ ] Unauthorized users get proper error
- [ ] Organization isolation maintained

## Deployment Checklist

Before deploying fix to production:

- [ ] All tests passing
- [ ] Code reviewed (if team)
- [ ] Staging deployment successful
- [ ] Staging testing complete
- [ ] No errors in staging logs
- [ ] Migration tested (if schema change)
- [ ] Rollback plan prepared
- [ ] Monitoring plan prepared

**Post-Deployment:**
- [ ] Production deployment successful
- [ ] Smoke test passed
- [ ] Original bug verified as fixed in production
- [ ] No new errors in production logs
- [ ] Monitored for 30 minutes after deploy

## Common Pitfalls to Avoid

- [ ] Not skipping step 1 (reproduction)
- [ ] Not guessing at fixes without evidence
- [ ] Not commenting out failing tests
- [ ] Not deploying without testing
- [ ] Not ignoring error messages
- [ ] Not adding workarounds instead of real fixes
- [ ] Not forgetting to document the fix
- [ ] Not skipping regression tests

## Emergency Production Checklist

For P0/P1 production incidents:

**Immediate (0-5 min):**
- [ ] Severity assessed (P0/P1/P2/P3)
- [ ] Impact quantified (users affected)
- [ ] Team notified
- [ ] Incident channel created (if applicable)

**Triage (5-15 min):**
- [ ] Production logs captured and saved
- [ ] Recent deployments reviewed
- [ ] Rollback option evaluated
- [ ] Hotfix vs. rollback decision made

**If Rollback (15-20 min):**
- [ ] Previous working commit identified
- [ ] Rollback executed (`railway rollback`)
- [ ] Rollback verified successful
- [ ] Users notified
- [ ] Investigation continues offline

**If Hotfix (20-60 min):**
- [ ] Hotfix branch created
- [ ] Minimal fix implemented
- [ ] Fix tested locally
- [ ] Fix deployed to staging
- [ ] Staging verification complete
- [ ] Fix deployed to production
- [ ] Production verification complete
- [ ] Monitoring active

**Post-Incident (within 24 hours):**
- [ ] Incident report created
- [ ] Root cause documented
- [ ] Prevention measures identified
- [ ] Action items assigned
- [ ] Postmortem scheduled (if P0/P1)

## Quick Reference: By Issue Type

### Permission Issues (403 Forbidden)
- [ ] User permissions checked (`user.get_all_permissions()`)
- [ ] Required permission identified
- [ ] Permission exists in database
- [ ] Permission assigned to user's role
- [ ] View decorator verified
- [ ] Organization scoping checked

### HTMX Issues (UI Not Updating)
- [ ] Network request successful (200 OK)
- [ ] Target element exists in DOM
- [ ] Target ID matches hx-target
- [ ] Response content verified
- [ ] Swap method appropriate
- [ ] HTMX events logged (`htmx.logAll()`)

### Database Issues
- [ ] Migrations applied (`showmigrations`)
- [ ] Query tested in Django shell
- [ ] SQL printed (`print(queryset.query)`)
- [ ] Indexes exist for filtered fields
- [ ] N+1 queries checked
- [ ] Organization scoping present

### Multi-Tenancy Issues
- [ ] Query filtered by organization
- [ ] User organization verified
- [ ] Foreign keys have organization
- [ ] Data leakage tested (different org)
- [ ] Organization-scoped base queryset used

### Soft Delete Issues
- [ ] `is_active=True` filter present
- [ ] Soft-deleted records excluded
- [ ] Related queries respect soft delete
- [ ] Foreign key constraints safe

## Summary

Use this checklist to ensure:
1. ✅ Systematic investigation (not random guessing)
2. ✅ Thorough evidence gathering
3. ✅ Root cause identification (not symptom fixing)
4. ✅ Proper testing before deployment
5. ✅ Complete documentation for future reference

**Remember:** Skipping steps leads to recurring bugs and wasted time. Follow the process methodically.


---

# Quick Reference: Debugging by Error Type

## Quick Reference: Debugging by Error Type

### Next.js Errors

| Error | Cause | Fix |
|-------|-------|-----|
| Hydration mismatch | Server/Client difference | Use useEffect for client-only code |
| Module not found | Wrong import path | Check paths in tsconfig |
| Build error | TypeScript/syntax issue | Fix type errors |

### React Errors

| Error | Cause | Fix |
|-------|-------|-----|
| Too many re-renders | Infinite loop in useEffect | Add proper dependencies |
| Invalid hook call | Hook outside component | Move inside function component |
| Cannot update during render | setState in render | Move to useEffect |

### TanStack Query Errors

| Error | Cause | Fix |
|-------|-------|-----|
| Stale data | Missing invalidation | Add onSuccess invalidation |
| Infinite refetching | refetchInterval too low | Adjust or remove |
| Data undefined | Query not ready | Check isLoading |

### Django Ninja Errors

| Error | Cause | Fix |
|-------|-------|-----|
| 401 | Auth required | Check JWT token |
| 403 | Permission denied | Check user permissions |
| 404 | Resource not found | Check URL and ID |
| 422 | Validation error | Check schema match |
| 500 | Server exception | Check Django logs |


---

## CSEA-Specific Debugging

### Multi-Portal Context

When debugging, identify which portal:
- **Public Portal**: Unauthenticated, public data only
- **C/SE Portal**: Tenant-scoped, authenticated
- **CSEA Staff**: Admin access, all organizations

### Multi-Tenant Issues

```typescript
// Check organization context
console.log('Current org:', organization);
console.log('API URL:', `/api/v1/org/${organization.id}/data`);
```

### Authentication Issues

```typescript
// Check auth state
const { user, isAuthenticated, token } = useAuth();
console.log('Auth state:', { user, isAuthenticated, hasToken: !!token });
```


---

## Tools Reference

### Browser DevTools
- **Console**: JavaScript errors, logs
- **Network**: API requests/responses
- **Elements**: DOM inspection
- **React DevTools**: Component state
- **Query DevTools**: TanStack Query state

### Command Line
```bash