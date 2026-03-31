# [Workflow Name] Checklist

**Date**: YYYY-MM-DD
**User**: Your Name
**Workflow Type**: [ ] New Feature [ ] Bug Fix [ ] Deployment [ ] Database Migration [ ] Security [ ] AI Feature
**Complexity**: [ ] Simple (1 skill) [ ] Moderate (2-3 skills) [ ] Complex (4+ skills)
**Urgency**: [ ] Critical [ ] High [ ] Normal [ ] Low

---

## Workflow Overview

**Objective**:
[Brief description of what this workflow aims to accomplish]

**Expected Outcome**:
[What should be achieved when this workflow is complete]

**Estimated Timeline**:
[Rough estimate: X hours or X days]

---

## Workflow Steps

### Phase 1: [Phase Name] (Estimated: X hours)

#### Step 1: /[skill-name]
- [ ] Skill invoked
- [ ] Expected output received
- [ ] Decision point addressed

**Purpose**: [Why this skill is being used]
**Expected Output**: [What this skill should produce]
**Decision Point**: [What decision needs to be made after this step]

**Notes**:
- [Any notes about this step]

---

#### Step 2: /[skill-name]
- [ ] Skill invoked
- [ ] Expected output received
- [ ] Decision point addressed

**Purpose**: [Why this skill is being used]
**Expected Output**: [What this skill should produce]
**Decision Point**: [What decision needs to be made after this step]

**Notes**:
- [Any notes about this step]

---

### Phase 2: [Phase Name] (Estimated: X hours)

#### Step 3: /[skill-name]
- [ ] Skill invoked
- [ ] Expected output received
- [ ] Decision point addressed

**Purpose**: [Why this skill is being used]
**Expected Output**: [What this skill should produce]
**Decision Point**: [What decision needs to be made after this step]

**Notes**:
- [Any notes about this step]

---

## Safety Checks

### Pre-Workflow Safety
- [ ] `/safety-first` invoked (if applicable)
- [ ] Git status clean (no uncommitted changes)
- [ ] Database safety verified
- [ ] No blockers identified

### During Workflow
- [ ] CSP compliance verified (if frontend changes)
- [ ] Multi-tenant data isolation verified (if backend changes)
- [ ] No temporary fixes or workarounds
- [ ] Root cause fixes only

### Pre-Deployment (if applicable)
- [ ] `/coditor` audit completed
- [ ] Critical findings = 0
- [ ] High findings = 0
- [ ] All unit tests pass
- [ ] All integration tests pass
- [ ] Test coverage > 80%
- [ ] UI tested in browser (3 times minimum, if applicable)

---

## Decision Log

Track all major decisions made during this workflow.

| Step | Decision Point | Decision Made | Rationale |
|------|---------------|---------------|-----------|
| 1 | [Decision point] | [Decision] | [Why this decision was made] |
| 2 | [Decision point] | [Decision] | [Why this decision was made] |
| 3 | [Decision point] | [Decision] | [Why this decision was made] |

---

## Workflow State Tracking

### Current State

**Current Phase**: [Phase name]
**Current Step**: [X/Y]
**Last Completed**: [Step name]
**Next Step**: [Step name]

### Progress Overview

```
✅ Phase 1: [Phase Name] - Completed
  ✅ Step 1: /[skill-name] - Completed
  ✅ Step 2: /[skill-name] - Completed

🔄 Phase 2: [Phase Name] - In Progress
  ✅ Step 3: /[skill-name] - Completed
  🔄 Step 4: /[skill-name] - In Progress
  ⏭️ Step 5: /[skill-name] - Pending

⏭️ Phase 3: [Phase Name] - Pending
  ⏭️ Step 6: /[skill-name] - Pending
  ⏭️ Step 7: /[skill-name] - Pending
```

---

## Issues Encountered

Track any issues, blockers, or deviations from the planned workflow.

| Step | Issue | Resolution | Time Impact |
|------|-------|------------|-------------|
| [Step] | [Description of issue] | [How it was resolved] | [+X hours] |

---

## Test Results

### Unit Tests
- [ ] All tests pass
- [ ] Coverage: [X%]
- [ ] New tests added: [Count]

**Test Command**: `pytest [args]`

**Results**:
```
[Paste test results here]
```

### Integration Tests
- [ ] All tests pass
- [ ] Cross-module workflows verified

**Test Command**: `pytest [args]`

**Results**:
```
[Paste test results here]
```

### E2E Tests (if applicable)
- [ ] All tests pass
- [ ] User journeys verified

**Test Command**: `pytest [args]`

**Results**:
```
[Paste test results here]
```

### Browser Testing (if UI changes)
- [ ] Tested in Chrome (3 times)
- [ ] No console errors
- [ ] HTMX interactions working
- [ ] CSP compliance verified (no CSP violations)

**Issues Found**:
- [List any issues]

---

## Coditor Audit Results

### Audit Summary
- [ ] Audit completed
- [ ] Critical: [Count]
- [ ] High: [Count]
- [ ] Medium: [Count]
- [ ] Low: [Count]

### Critical Findings (MUST FIX)
1. [Finding description]
   - Location: [File:line]
   - Fix: [How it was fixed]
   - Status: [ ] Fixed [ ] In Progress [ ] Pending

### High Findings (MUST FIX)
1. [Finding description]
   - Location: [File:line]
   - Fix: [How it was fixed]
   - Status: [ ] Fixed [ ] In Progress [ ] Pending

### Medium/Low Findings (Document)
- [List findings that can be fixed later]

---

## Deployment Information

### Deployment Checklist
- [ ] All safety checks passed
- [ ] All tests passed
- [ ] Coditor audit passed (Critical/High = 0)
- [ ] Database backup completed (production only)
- [ ] Migrations tested (locally, and on staging if deploying to production)
- [ ] Team notified (production only)

### Deployment Details

**Target Environment**: [ ] Local [ ] Staging [ ] Production

**Deployment Date**: YYYY-MM-DD HH:MM

**Deployed By**: [Name]

**Git Branch**: [branch-name]

**Git Commit**: [commit-hash]

**Deployment Command**: `[command used]`

### Post-Deployment Verification

#### Immediate (First 10 Minutes)
- [ ] Application responding (200 OK)
- [ ] Health check passing
- [ ] Database migrations applied
- [ ] Static files served correctly
- [ ] Critical endpoints tested
- [ ] No error spikes in logs

#### First Hour
- [ ] Error rates normal
- [ ] Response times acceptable
- [ ] Database performance normal
- [ ] Celery tasks running (if applicable)
- [ ] No user-reported issues

#### First 24 Hours
- [ ] Overall system health good
- [ ] Metrics compared to baseline
- [ ] No gradual degradation observed

---

## Time Tracking

| Phase | Estimated | Actual | Variance |
|-------|-----------|--------|----------|
| Planning | [X hours] | [X hours] | [+/- X hours] |
| Implementation | [X hours] | [X hours] | [+/- X hours] |
| Testing | [X hours] | [X hours] | [+/- X hours] |
| Audit | [X hours] | [X hours] | [+/- X hours] |
| Deployment | [X hours] | [X hours] | [+/- X hours] |
| **Total** | [X hours] | [X hours] | [+/- X hours] |

---

## Lessons Learned

### What Went Well
- [Positive outcomes or smooth processes]

### What Could Be Improved
- [Areas for improvement]

### Recommendations for Future
- [Suggestions for similar workflows]

---

## Final Summary

**Workflow Status**: [ ] Success [ ] Partial [ ] Failed [ ] Rolled Back

**Final Outcome**:
[Brief summary of what was accomplished]

**Critical Metrics**:
- Test Coverage: [X%]
- Coditor Findings Fixed: [Critical: X, High: X]
- Deployment Status: [Success/Failed/Rolled Back]
- Total Time: [X hours]

**Deployment URL** (if applicable):
[Staging URL or Production URL]

**Sign-off**: ___________________________  Date: ___________

---

## Appendix

### Files Modified
```
[List all files that were created, modified, or deleted]
```

### Dependencies Added
```
[List any new dependencies added to requirements.txt or package.json]
```

### Configuration Changes
```
[List any environment variables or configuration changes]
```

### Database Changes
```
[List migrations created and applied]
```

### Rollback Plan (if needed)

**Rollback Trigger**:
[What conditions would trigger a rollback]

**Rollback Procedure**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Rollback Verification**:
- [ ] [Verification step 1]
- [ ] [Verification step 2]

---

## Notes

[Any additional notes, observations, or important information]
