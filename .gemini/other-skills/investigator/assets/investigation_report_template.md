# Investigation Report: [Error/Issue Title]

**Date**: [YYYY-MM-DD]
**Investigated by**: Claude Investigator
**Error Type**: [HTMX/Django ORM/Celery/Railway/PostgreSQL/Auth/Frontend/API]
**Environment**: [Local/Staging/Production]

---

## Executive Summary

[2-3 sentence summary of the issue and recommended solution]

---

## Issue Details

### Error Description

**What happened**:
[Detailed description of the error or issue]

**When it occurs**:
[Triggers, frequency, patterns]

**Impact**:
[Who/what is affected, severity level]

### Evidence Collected

**Error Messages**:
```
[Exact error message(s) from logs]
```

**Stack Trace** (if applicable):
```
[Relevant portions of stack trace]
```

**Related Logs**:
```
[Relevant log excerpts showing context before/after error]
```

**Code Context**:
[File paths and line numbers where issue manifests]

**Recent Changes**:
- [What changed before the error appeared]

---

## Investigation Summary

### Investigation Steps Performed

1. [Step 1: What was investigated]
   - Finding: [What was discovered]

2. [Step 2: What was investigated]
   - Finding: [What was discovered]

3. [Step 3: What was investigated]
   - Finding: [What was discovered]

### Root Cause Analysis

**Identified Root Cause**:
[Clear explanation of what's causing the issue]

**Why This Happens**:
[Technical explanation of the mechanism]

**Contributing Factors**:
- [Factor 1]
- [Factor 2]

---

## Proposed Solutions

**Solutions ranked by effectiveness (most effective first)**

---

### Solution 1: [Descriptive Name] ⭐ RECOMMENDED

**Approach**:
[1-2 sentence summary of the solution approach]

**Why This Solution**:
[Explain why this is the most effective approach]

#### Assessment

| Criteria | Rating | Notes |
|----------|--------|-------|
| **Effectiveness** | High/Medium/Low | [Brief explanation] |
| **Risk** | Low/Medium/High | [Brief explanation] |
| **Implementation Effort** | Low/Medium/High | [Brief explanation] |
| **Maintenance Burden** | Low/Medium/High | [Brief explanation] |

#### Evidence Sources

1. **Official Documentation**: [Title]
   - **URL**: [Link]
   - **Key Finding**: "[Quote or summary of relevant information]"
   - **Relevance**: [Why this source matters for this solution]
   - **Date**: [Publication/last updated date]

2. **GitHub Issue/PR**: [Title]
   - **URL**: [Link]
   - **Key Finding**: "[Quote or summary]"
   - **Relevance**: [Why this matters]
   - **Status**: [Open/Closed/Merged]

3. **Stack Overflow/Community**: [Title]
   - **URL**: [Link]
   - **Key Finding**: "[Quote or summary]"
   - **Relevance**: [Why this matters]
   - **Votes/Acceptance**: [Community validation]

4. **Technical Blog/Article**: [Title]
   - **URL**: [Link]
   - **Key Finding**: "[Quote or summary]"
   - **Relevance**: [Why this matters]
   - **Author Credentials**: [Why this source is trustworthy]

5. **Additional Source**: [Title]
   - **URL**: [Link]
   - **Key Finding**: "[Quote or summary]"
   - **Relevance**: [Why this matters]

#### Implementation Overview

**What needs to change**:
[High-level description of implementation steps]

**Files affected**:
- `path/to/file1.py` - [What changes]
- `path/to/file2.py` - [What changes]

**Configuration changes**:
- [Setting/variable to change]

**Dependencies** (if any):
- [New packages to install]

#### Trade-offs

**Pros**:
- ✅ [Benefit 1]
- ✅ [Benefit 2]
- ✅ [Benefit 3]

**Cons**:
- ❌ [Limitation 1]
- ❌ [Limitation 2]

#### Validation Steps

1. **Pre-implementation verification**:
   - [ ] [Check prerequisite 1]
   - [ ] [Check prerequisite 2]

2. **Post-implementation testing**:
   - [ ] [Test step 1]
   - [ ] [Test step 2]
   - [ ] [Test step 3]

3. **Regression testing**:
   - [ ] [Feature to verify still works]
   - [ ] [Feature to verify still works]

4. **Production monitoring**:
   - [ ] [Metric to monitor]
   - [ ] [Log to watch]

---

### Solution 2: [Descriptive Name]

**Approach**:
[1-2 sentence summary of the solution approach]

**Why Consider This**:
[When/why this might be preferred over Solution 1]

#### Assessment

| Criteria | Rating | Notes |
|----------|--------|-------|
| **Effectiveness** | High/Medium/Low | [Brief explanation] |
| **Risk** | Low/Medium/High | [Brief explanation] |
| **Implementation Effort** | Low/Medium/High | [Brief explanation] |
| **Maintenance Burden** | Low/Medium/High | [Brief explanation] |

#### Evidence Sources

1. **[Source Type]**: [Title]
   - **URL**: [Link]
   - **Key Finding**: "[Quote or summary]"
   - **Relevance**: [Why this matters]

2. **[Source Type]**: [Title]
   - **URL**: [Link]
   - **Key Finding**: "[Quote or summary]"
   - **Relevance**: [Why this matters]

3. **[Source Type]**: [Title]
   - **URL**: [Link]
   - **Key Finding**: "[Quote or summary]"
   - **Relevance**: [Why this matters]

4. **[Source Type]**: [Title]
   - **URL**: [Link]
   - **Key Finding**: "[Quote or summary]"
   - **Relevance**: [Why this matters]

5. **[Source Type]**: [Title]
   - **URL**: [Link]
   - **Key Finding**: "[Quote or summary]"
   - **Relevance**: [Why this matters]

#### Implementation Overview

[Same structure as Solution 1]

#### Trade-offs

**Pros**:
- ✅ [Benefit 1]
- ✅ [Benefit 2]

**Cons**:
- ❌ [Limitation 1]
- ❌ [Limitation 2]

#### Validation Steps

[Same structure as Solution 1]

---

### Solution 3: [Descriptive Name]

**Approach**:
[1-2 sentence summary of the solution approach]

**Why Consider This**:
[When/why this might be preferred - likely special circumstances]

#### Assessment

| Criteria | Rating | Notes |
|----------|--------|-------|
| **Effectiveness** | High/Medium/Low | [Brief explanation] |
| **Risk** | Low/Medium/High | [Brief explanation] |
| **Implementation Effort** | Low/Medium/High | [Brief explanation] |
| **Maintenance Burden** | Low/Medium/High | [Brief explanation] |

#### Evidence Sources

[Same structure as Solutions 1 & 2 - 5 sources each]

#### Implementation Overview

[Same structure as Solutions 1 & 2]

#### Trade-offs

[Same structure as Solutions 1 & 2]

#### Validation Steps

[Same structure as Solutions 1 & 2]

---

## Comparison Matrix

| Criteria | Solution 1 | Solution 2 | Solution 3 |
|----------|-----------|-----------|-----------|
| **Effectiveness** | [Rating] | [Rating] | [Rating] |
| **Risk** | [Rating] | [Rating] | [Rating] |
| **Effort** | [Rating] | [Rating] | [Rating] |
| **Maintenance** | [Rating] | [Rating] | [Rating] |
| **Time to Implement** | [Estimate] | [Estimate] | [Estimate] |
| **Best For** | [Scenario] | [Scenario] | [Scenario] |

---

## OBCMS-Specific Considerations

### Multi-Tenant Impact
[How does each solution affect multi-tenant data isolation?]

### CSP Compliance
[Are all solutions CSP-compliant? Any inline scripts to address?]

### Performance Impact
[Expected performance implications for each solution]

### Security Implications
[Any security considerations for each approach?]

### Migration Requirements
[Do any solutions require database migrations?]

---

## Recommendations

### Immediate Actions

1. **[Highest priority action]**
   - Why: [Justification]
   - Who: [Role/person responsible]
   - When: [Timeframe]

2. **[Second priority action]**
   - Why: [Justification]
   - Who: [Role/person responsible]
   - When: [Timeframe]

### Long-term Improvements

1. **[Preventive measure or improvement]**
   - Why: [Justification]
   - Impact: [Expected benefit]

2. **[Preventive measure or improvement]**
   - Why: [Justification]
   - Impact: [Expected benefit]

### Monitoring & Prevention

**What to monitor**:
- [Metric/log to watch]
- [Threshold/alert condition]

**How to prevent recurrence**:
- [Preventive measure 1]
- [Preventive measure 2]

---

## Related Issues

**Similar past issues**:
- [Link or reference to similar issue]
- [What was learned]

**Related GitHub issues**:
- [Link to relevant GitHub issue]

**Documentation to update**:
- [Documentation that should be updated based on this investigation]

---

## Appendix

### Useful Commands

```bash
# Commands used during investigation
[Command 1]
[Command 2]
```

### References

All sources cited above, organized by category:

**Official Documentation**:
- [Source 1]
- [Source 2]

**GitHub Issues/PRs**:
- [Source 1]
- [Source 2]

**Community Resources**:
- [Source 1]
- [Source 2]

**Technical Articles**:
- [Source 1]
- [Source 2]

### Investigation Notes

[Any additional observations, patterns noticed, or context that might be useful for future reference]

---

**Next Steps**: User should review the recommended solution and decide whether to proceed with implementation.

**⚠️ Important**: This investigation report presents research and recommendations only. No changes have been implemented. User approval is required before proceeding with any solution.
