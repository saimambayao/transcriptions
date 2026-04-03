# Error Report: [Bug Title]

**Date:** [YYYY-MM-DD]
**Reported By:** [Name/Email]
**Severity:** CRITICAL / HIGH / MEDIUM / LOW
**Status:** 🔍 INVESTIGATING / ✅ FIXED / ⚠️ FIXED (uncommitted) / 📋 DOCUMENTED

---

## Summary

Brief description of the bug in 1-2 sentences.

---

## Environment

- **Where:** Development / Staging / Production
- **URL:** [Affected URL or feature]
- **Django Version:** 5.2
- **Database:** PostgreSQL / SQLite
- **Browser:** Chrome / Firefox / Safari (version)
- **User Role:** Admin / Manager / Staff
- **Organization:** [Org name or ID]

---

## Reproduction Steps

### Prerequisites
1. [Any required setup or data state]
2. [User permissions needed]
3. [Specific conditions]

### Steps to Reproduce
1. [First action]
2. [Second action]
3. [Third action]
4. [Action that triggers bug]

### Expected Result
[What should happen]

### Actual Result
[What actually happens]

**Reproduction Rate:** X/Y attempts (Z% consistent)

---

## Evidence

### Error Messages
```
[Paste full error message and stack trace]
```

### Django Logs
```
[Relevant log entries]
```

### Browser Console (if frontend issue)
```
[JavaScript errors, HTMX events]
```

### Screenshots
[Attach screenshots showing the error]

### Network Requests (if HTMX/API issue)
- **Request URL:** [URL]
- **Request Method:** GET / POST / PUT / DELETE
- **Status Code:** [200 / 403 / 404 / 500]
- **Request Payload:** [JSON/Form data]
- **Response:** [Response body]

---

## Investigation

### Step 1: Reproduction
- [x] Bug reproduced consistently
- [x] Environment conditions documented
- [x] Error captured in logs

### Step 2: Isolation
**Layer Identified:** Model / View / Template / API / Frontend

**Specific Location:**
- File: `[path/to/file.py]`
- Function/Class: `[function_name]`
- Line Number: [line number]

### Step 3: Evidence Gathered
- [x] Django logs reviewed
- [x] Database state checked
- [x] Browser DevTools inspected
- [x] Stack trace analyzed

### Step 4: Root Cause Analysis

**Five Whys:**
1. **Why?** [First why answer]
2. **Why?** [Second why answer]
3. **Why?** [Third why answer]
4. **Why?** [Fourth why answer]
5. **Why?** [Fifth why answer]

**Root Cause:** [Fundamental underlying issue]

**Contributing Factors:**
1. [Factor 1]
2. [Factor 2]

### Step 5: Hypothesis Testing

**Hypothesis:** [What we thought was wrong]

**Evidence Supporting:**
- [Supporting evidence 1]
- [Supporting evidence 2]

**Evidence Against:**
- [Contradicting evidence, if any]

**Verification:** [How hypothesis was tested]

**Result:** ✅ Confirmed / ❌ Rejected

---

## Solution

### Fix Implementation

**File(s) Changed:**
- `[path/to/file1.py]`
- `[path/to/file2.html]`

**Changes Made:**
```python
# Before (broken code)
[paste original code]

# After (fixed code)
[paste fixed code]
```

**Why This Fixes It:**
[Explanation of how the fix addresses the root cause]

### Migration Required
- [ ] Yes - Migration file: `[migration_name]`
- [x] No

### Configuration Changes
- [ ] Environment variables updated
- [ ] Settings changed
- [ ] Permissions added

---

## Testing

### Test Results
- [x] Original bug no longer reproduces
- [x] Unit tests added
- [x] Integration tests added
- [x] Tested in staging
- [x] All tests passing

### Tests Added
```python
# test_file.py
def test_[bug_name](self):
    """Test that bug is fixed."""
    [test code]
```

### Regression Check
- [x] Related features still work
- [x] Multi-tenant isolation maintained
- [x] No performance degradation
- [x] No new console errors

---

## Prevention Measures

### Immediate Prevention
1. [Test added to prevent regression]
2. [Code review checklist updated]

### Long-term Prevention
1. [Process improvement]
2. [Documentation update]
3. [Training/awareness]

### Monitoring
- [ ] Alert added for similar errors
- [ ] Dashboard metric added
- [ ] Periodic check scheduled

---

## Deployment

### Deployment Plan
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Deployed To
- [ ] Staging - [Date/Time]
- [ ] Production - [Date/Time]

### Verification
- [x] Tested in staging
- [x] Tested in production
- [x] No new errors in logs
- [x] Feature works as expected

### Rollback Plan
- **Revert Commit:** `[commit hash]`
- **Railway Rollback:** Available
- **Estimated Rollback Time:** [X minutes]

---

## Post-Mortem (for P0/P1 incidents)

### What Went Well
1. [What worked in our response]
2. [Effective processes]

### What Could Be Improved
1. [Areas for improvement]
2. [Process gaps]

### Action Items
- [ ] [Action 1] - Owner: [Name]
- [ ] [Action 2] - Owner: [Name]
- [ ] [Action 3] - Owner: [Name]

### Lessons Learned
[Key takeaways from this incident]

---

## Related Issues

- Related Bug: [Link to related issue]
- Similar Pattern: [docs/error-logs/category/similar-bug.md]
- Documentation: [Link to relevant docs]

---

## Additional Notes

[Any other relevant information, context, or observations]

---

**Report Created:** [YYYY-MM-DD HH:MM]
**Report Updated:** [YYYY-MM-DD HH:MM]
**Resolved:** [YYYY-MM-DD HH:MM]
