# Ultrathinking Multi-Agent Debugging Workflow

Advanced error investigation using parallel agents and validation - the definitive OBCMS debugging methodology.

## Overview

**Ultrathinking** is a multi-agent collaborative debugging workflow that ensures:
- Comprehensive investigation from multiple angles
- Independent validation of findings
- User approval before implementation
- Systematic documentation

**When to use:**
- Complex production errors
- Critical bugs affecting multiple users
- Errors requiring deep investigation
- When basic debugging hasn't found root cause

## The 4-Phase Ultrathinking Workflow

### Step 0: Check Error History (Main Claude)

**ALWAYS check first** - avoid duplicate investigation.

```bash
# Search error log
grep -i "error_keyword" docs/error-logs/error_log.md

# Review recent errors
tail -50 docs/error-logs/error_log.md
```

**If exact same error found:**

1. **Review existing fix plan/report**
   - Check detailed error report in `docs/error-logs/{category}/`
   - Read proposed fix

2. **Validate the previous fix:**
   ```bash
   # Check if fix was committed
   git log --grep="error_name" --oneline -5

   # Verify fix in codebase
   grep -r "fixed_code_pattern" src/

   # Check Railway logs for recurrence
   railway logs --tail 100 | grep -i "error_keyword"
   ```

3. **Decision tree:**

   **If fix committed AND error still occurs:**
   - Previous fix didn't work
   - **Proceed to full investigation (Step 1)**

   **If fix NOT committed:**
   - Apply the previous fix
   - Mark as ⚠️ FIXED (uncommitted)
   - Test and commit

   **If fix committed AND error resolved:**
   - False alarm or different error
   - Document in error log
   - No further investigation needed

**If error is new or different:** Proceed to Step 1

---

### Step 1: Audit Logs (Main Claude)

**Main Claude gathers initial evidence** before launching agents.

**Required log captures:**

```bash
# Production/Staging errors - REQUIRED
railway logs --tail 200 > railway-logs-$(date +%Y%m%d-%H%M).txt
cat railway-logs.txt

# Local development logs
tail -100 src/logs/django.log

# System state
cd src && python manage.py showmigrations

# Git state
git status && git log --oneline -10
```

**Initial observations to document:**

1. **Error type:** Permission / Database / HTMX / Logic
2. **Frequency:** One-time / Intermittent / Consistent
3. **Affected scope:** Single user / Organization / All users
4. **Recent changes:** Recent commits/deployments
5. **Environment:** Development / Staging / Production

**Log immediately:**
```bash
DATE=$(date '+%Y-%m-%d %H:%M:%S')
echo "### [$DATE] | [ErrorName]
**Status:** 🔍 INVESTIGATING
**Category:** [deployment|migration|database|api|ui|etc]
**Severity:** [CRITICAL|HIGH|MEDIUM|LOW]
**Description:** [Brief description]
" >> docs/error-logs/error_log.md
```

**Output for agents:**
- Railway logs saved to file
- Log excerpts with timestamps
- Initial observations
- System state snapshot

---

### Phase 1: Parallel Investigation (Agents 1 & 2)

**Launch two agents in parallel** - each investigates from different angle.

**CRITICAL:** Both agents must complete before Phase 2.

#### Agent 1: Codebase Investigation

**Use:** `Explore` agent with "very thorough" setting

**Task:**
```
Investigate this error in the OBCMS codebase:

Error: [error description]
Logs: [paste relevant logs]
Environment: [dev/staging/production]

Investigation requirements:
1. Find root cause in codebase
2. Identify exact file/function/line causing error
3. Check for similar patterns elsewhere
4. Review git history for recent changes
5. Identify OBCMS-specific issues (org scoping, permissions, soft delete)

Deliverables:
- Root cause with evidence
- Affected code locations
- Similar patterns found
- Recent changes that may have introduced bug
```

**Agent 1 Tools:**
- Glob (find files by pattern)
- Grep (search code)
- Read (examine files)
- Bash (git history, file analysis)

**Expected output:**
- Root cause hypothesis with evidence
- Code snippets showing the issue
- Git commits that may have introduced bug
- Related code that needs fixing

#### Agent 2: Online Research

**Use:** `general-purpose` agent

**Task:**
```
Research solutions for this Django/HTMX error:

Error: [error description]
Tech stack: Django 5.2, HTMX, PostgreSQL, Railway
OBCMS context: Multi-tenant, org-scoped, RBAC

Research requirements:
1. Search Django documentation for error type
2. Find Stack Overflow solutions (2024-2025)
3. Check HTMX docs if frontend issue
4. Find best practices for this error
5. Identify common causes and solutions

Deliverables:
- Common causes of this error
- Recommended solutions from Django community
- Best practices to prevent recurrence
- Code examples of proper fixes
```

**Agent 2 Tools:**
- WebSearch (find recent solutions)
- WebFetch (read documentation)
- Read (review local docs)

**Expected output:**
- Common causes list
- Recommended solutions with sources
- Best practices
- Code examples from Django community

**⏸️ WAIT for both agents to complete**

---

### Phase 2: Fix Plan Synthesis (Main Claude)

**Main Claude synthesizes Agent 1 & 2 findings** into actionable fix plan.

**Inputs:**
- Agent 1 codebase investigation results
- Agent 2 online research results
- Initial log analysis (Step 1)
- Error history check (Step 0)

**Synthesis process:**

1. **Correlate findings**
   - Compare Agent 1's code findings with Agent 2's research
   - Identify agreements and contradictions
   - Prioritize most likely root cause

2. **Create concise fix plan** (1-2 pages MAX)

**Fix Plan Template:**

```markdown
# Fix Plan: [Error Name]

## Root Cause (from Agent 1 + Agent 2)
[Concise explanation of what's wrong and why]

## Evidence
- **Codebase:** [Agent 1 findings]
- **Research:** [Agent 2 findings]
- **Logs:** [Key log excerpts]

## Proposed Fix

### Changes Required
1. **File:** `path/to/file.py`
   **Change:** [What to change]
   **Why:** [How this fixes root cause]

2. **File:** `path/to/other/file.html`
   **Change:** [What to change]
   **Why:** [How this fixes root cause]

### Migration Required
- [ ] Yes: [migration details]
- [x] No

## Verification Steps
1. [How to test fix locally]
2. [How to verify in staging]
3. [How to confirm in production]

## Regression Tests
```python
# test_file.py - prevents recurrence
def test_[error_name]():
    """Ensure bug doesn't recur."""
    [test code]
```

## Prevention Measures
1. [Immediate prevention]
2. [Long-term prevention]
```

**Output:** Concise, actionable fix plan ready for validation

---

### Phase 3: Independent Validation (Agent 3)

**Launch Agent 3** for independent verification of the fix plan.

**Use:** `general-purpose` agent

**CRITICAL:** Agent 3 must **independently re-investigate** - not just review.

**Task:**
```
INDEPENDENT VALIDATION - Verify this fix plan:

Error: [error description]
Fix Plan: [paste entire fix plan from Phase 2]

Your mission: Re-investigate independently and validate:

1. ACCURACY: Is the root cause correct?
   - Re-read the logs yourself
   - Re-search the codebase yourself
   - Re-research online yourself
   - Do you reach the same conclusion?

2. COMPLETENESS: Does the fix address everything?
   - Are there edge cases missed?
   - Are there related issues not addressed?
   - Is the fix comprehensive enough?

3. ALIGNMENT: Does the fix follow best practices?
   - OBCMS standards (org scoping, soft delete, CSP)
   - Django best practices
   - HTMX patterns (if applicable)
   - Security considerations

Deliverables:
- Validation report (APPROVE / REVISE / REJECT)
- Issues found (if any)
- Additional recommendations
```

**Agent 3 Tools:**
- All tools (independent investigation)
- Grep, Read (re-examine code)
- WebSearch (verify solutions)

**Validation Criteria:**

**✅ APPROVE if:**
- Root cause is correct with evidence
- Fix addresses the root cause completely
- No critical issues or edge cases missed
- Follows OBCMS standards
- Includes proper testing

**⚠️ REVISE if:**
- Root cause mostly correct but incomplete
- Fix missing edge cases
- Needs additional changes
- Minor standards violations

**❌ REJECT if:**
- Root cause is wrong
- Fix doesn't address the issue
- Critical security/data issues
- Violates OBCMS architecture

**Expected output:**
```markdown
# Validation Report: [Error Name]

## Overall Assessment: APPROVE / REVISE / REJECT

## Accuracy Validation
[Re-investigation findings - do they match?]

## Completeness Check
- Missing edge cases: [list if any]
- Related issues: [list if found]

## Standards Alignment
- ✅ Organization scoping: [OK / Issues found]
- ✅ Soft delete: [OK / Issues found]
- ✅ CSP compliance: [OK / Issues found]
- ✅ RBAC: [OK / Issues found]

## Recommendations
1. [Additional change 1]
2. [Additional change 2]

## Verdict
[APPROVE and implement / REVISE with changes / REJECT and re-investigate]
```

**⏸️ WAIT for Agent 3 validation**

---

### Phase 4: Finalization & Approval (Main Claude)

**Main Claude reviews Agent 3 validation** and finalizes plan.

**Review Agent 3 feedback:**

**If APPROVED:**
- Fix plan is sound
- Proceed to user presentation

**If REVISE:**
- Incorporate Agent 3's recommendations
- Update fix plan
- May need to re-run Agent 3 validation

**If REJECTED:**
- Root cause is wrong
- Return to Phase 1 with new investigation focus

**Create user-facing summary** (1 page MAX):

```markdown
# Error Fix Summary: [Error Name]

## Problem
[1-2 sentence description of the bug]

## Root Cause
[1 paragraph explanation]

## Proposed Solution
1. [Change 1]
2. [Change 2]
3. [Change 3]

## Testing Plan
- Unit tests: [brief]
- Integration tests: [brief]
- Staging verification: [brief]

## Risk Assessment
- Risk level: LOW / MEDIUM / HIGH
- Rollback plan: [brief]

## Approval Needed
Do you approve implementing this fix?
```

**Present to user and WAIT for approval**

**CRITICAL:** Do NOT implement until user approves

**After user approval:**
1. Implement the fix
2. Run tests
3. Deploy to staging
4. Verify in staging
5. Deploy to production (if staging OK)
6. Document final results

---

## Workflow Summary

```
Step 0: Check History
         ↓
Step 1: Audit Logs (Main Claude)
         ↓
Phase 1: Launch Agents 1 & 2 (Parallel)
         ├─ Agent 1: Codebase
         └─ Agent 2: Research
         ↓ (WAIT for both)
Phase 2: Main Claude Synthesizes Fix Plan
         ↓
Phase 3: Agent 3 Validates
         ↓ (WAIT for validation)
Phase 4: Main Claude Finalizes
         ↓
    Present to User
         ↓ (WAIT for approval)
    Implement Fix
```

## When to Use Each Workflow

**Use Ultrathinking (this workflow) when:**
- ✅ Complex production errors
- ✅ Root cause unclear after basic debugging
- ✅ Error affects multiple users/organizations
- ✅ Critical bug requiring thorough investigation
- ✅ Time permits comprehensive investigation
- ✅ Error might have multiple causes

**Use Basic 7-Step Workflow when:**
- Simple, obvious errors
- Time-sensitive hotfixes
- Local development issues
- Clear reproduction and cause
- Low-risk bugs

## Benefits of Ultrathinking

1. **Multi-perspective investigation** - Codebase + Research + Validation
2. **Higher accuracy** - Independent validation catches mistakes
3. **User approval** - No surprises, user controls implementation
4. **Comprehensive** - Less likely to miss edge cases
5. **Better documentation** - Thorough investigation produces better docs
6. **Knowledge sharing** - Agents learn from each other

## Integration with Basic Workflow

Ultrathinking **enhances** the 7-step workflow:

**Steps 1-3 (Reproduce, Isolate, Evidence)** → **Step 0-1 (History, Logs)**
- Same initial investigation

**Step 4 (Hypotheses)** → **Phase 1 (Agents 1 & 2)**
- Multi-agent investigation instead of solo

**Step 5 (Test Hypotheses)** → **Phase 2-3 (Synthesis & Validation)**
- Validated fix plan instead of trial-and-error

**Steps 6-7 (Fix, Document)** → **Phase 4 (Approval & Implementation)**
- User approval before implementation

## Tips for Effective Ultrathinking

1. **Don't skip Step 0** - Checking history saves massive time
2. **Give agents context** - Include logs, environment, OBCMS details
3. **Wait for completion** - Don't rush agents, let them investigate thoroughly
4. **Trust Agent 3** - If validation fails, there's likely an issue
5. **Keep plans concise** - 1-2 pages, not novels
6. **Always get user approval** - Never implement without confirmation

## Example: Complete Ultrathinking Session

See `assets/ultrathinking-example.md` for a full walkthrough of the workflow in action.
