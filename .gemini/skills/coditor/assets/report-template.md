# OBCMS Code Audit Report

**Audit Date**: {AUDIT_DATE}
**Scope**: {AUDIT_SCOPE}
**Focus Areas**: {FOCUS_AREAS}
**Auditor**: Coditor v1.0.0
**Duration**: {DURATION}

---

## Executive Summary

### Overall Health Score: {HEALTH_SCORE}/100

### Findings Summary

| Severity | Count | Status |
|----------|-------|--------|
| 🔴 Critical | {CRITICAL_COUNT} | {CRITICAL_STATUS} |
| 🟠 High | {HIGH_COUNT} | {HIGH_STATUS} |
| 🟡 Medium | {MEDIUM_COUNT} | {MEDIUM_STATUS} |
| 🟢 Low | {LOW_COUNT} | {LOW_STATUS} |
| **Total** | **{TOTAL_COUNT}** | |

### Key Concerns

{KEY_CONCERNS_LIST}

### Positive Highlights

{POSITIVE_HIGHLIGHTS_LIST}

---

## Critical Findings

**Action Required**: Fix before next deployment

{CRITICAL_FINDINGS}

### Example Critical Finding

**Finding ID**: {FINDING_ID}
**Severity**: Critical
**Category**: {CATEGORY}
**File**: {FILE_PATH}:{LINE_NUMBER}

**Description**: {DESCRIPTION}

**Code**:
```python
{CODE_SNIPPET}
```

**Impact**: {IMPACT_DESCRIPTION}

**Remediation**:
```python
{REMEDIATION_CODE}
```

**Explanation**: {REMEDIATION_EXPLANATION}

---

## High Priority Findings

**Action Required**: Fix within 1 sprint

{HIGH_FINDINGS}

---

## Medium Priority Findings

**Action Required**: Plan to fix within 2-3 sprints

{MEDIUM_FINDINGS_SUMMARY}

### Top 5 Medium Priority Issues

1. **{MEDIUM_ISSUE_1}** - {FILE_COUNT} occurrences
2. **{MEDIUM_ISSUE_2}** - {FILE_COUNT} occurrences
3. **{MEDIUM_ISSUE_3}** - {FILE_COUNT} occurrences
4. **{MEDIUM_ISSUE_4}** - {FILE_COUNT} occurrences
5. **{MEDIUM_ISSUE_5}** - {FILE_COUNT} occurrences

---

## Low Priority Findings

**Action Required**: Fix when convenient

{LOW_FINDINGS_SUMMARY}

---

## Findings by Category

### Security ({SECURITY_COUNT} findings)

{SECURITY_FINDINGS_SUMMARY}

### Architecture ({ARCHITECTURE_COUNT} findings)

{ARCHITECTURE_FINDINGS_SUMMARY}

### Code Quality ({QUALITY_COUNT} findings)

{QUALITY_FINDINGS_SUMMARY}

### Frontend ({FRONTEND_COUNT} findings)

{FRONTEND_FINDINGS_SUMMARY}

---

## Findings by Django App

{FINDINGS_BY_APP}

### Example App Breakdown

**App**: communities
**Findings**: 12 (3 Critical, 4 High, 3 Medium, 2 Low)

- Critical: Missing organization filters in views.py (lines 45, 67, 89)
- High: CSP violations in templates (3 files)
- Medium: Duplicate code in forms.py
- Low: Missing docstrings in utils.py

---

## Recommendations

### Immediate Actions (This Week)

1. **Fix Critical Security Issues**
   - [ ] Add organization filters to all queries in {APP_NAMES}
   - [ ] Add CSP nonces to inline scripts in {TEMPLATE_NAMES}
   - [ ] Fix SQL injection in {FILE_NAMES}

2. **Fix High Priority Issues**
   - [ ] Add RBAC decorators to sensitive views
   - [ ] Implement soft delete where needed
   - [ ] Fix CSRF protection issues

### Short-Term Actions (1-2 Sprints)

1. **Code Quality Improvements**
   - [ ] Refactor duplicate code
   - [ ] Add docstrings to public functions
   - [ ] Reduce complexity in {COMPLEX_FUNCTIONS}

2. **Testing Gaps**
   - [ ] Add tests for multi-tenant isolation
   - [ ] Add tests for permission checks
   - [ ] Increase coverage to >80%

### Long-Term Actions (Quarterly)

1. **Architecture Improvements**
   - [ ] Extract common patterns to mixins
   - [ ] Standardize RBAC usage across apps
   - [ ] Optimize database indexes

2. **Documentation**
   - [ ] Document all public APIs
   - [ ] Create architecture decision records
   - [ ] Update GEMINI.md with new patterns

---

## Trend Analysis

{TREND_ANALYSIS}

### Comparison with Previous Audit

| Metric | Previous | Current | Change |
|--------|----------|---------|--------|
| Critical | {PREV_CRITICAL} | {CURR_CRITICAL} | {CHANGE_CRITICAL} |
| High | {PREV_HIGH} | {CURR_HIGH} | {CHANGE_HIGH} |
| Medium | {PREV_MEDIUM} | {CURR_MEDIUM} | {CHANGE_MEDIUM} |
| Low | {PREV_LOW} | {CURR_LOW} | {CHANGE_LOW} |
| Health Score | {PREV_SCORE}/100 | {CURR_SCORE}/100 | {CHANGE_SCORE} |

---

## Appendices

### Appendix A: Files Audited

{FILES_AUDITED_LIST}

### Appendix B: Pattern Detection Rules Used

{PATTERNS_USED_LIST}

### Appendix C: GEMINI.md Rules Checked

{CLAUDE_RULES_CHECKED_LIST}

### Appendix D: Full Findings List

{FULL_FINDINGS_DUMP}

---

## Audit Methodology

**Tools Used**:
- Coditor skill v1.0.0
- Pattern detection from references/
- OBCMS standards from GEMINI.md

**Scope**:
- Django apps: {APPS_AUDITED}
- File types: Python (.py), Templates (.html), JavaScript (.js)
- Exclusions: migrations/, node_modules/, venv/

**Pattern Detection**:
- Security patterns (CSP, multi-tenant, XSS, SQL injection)
- Architecture patterns (RBAC, soft delete, organization scoping)
- Code quality patterns (DRY, complexity, documentation)
- Frontend patterns (HTMX, Alpine.js, Tailwind, accessibility)

---

**Report Generated**: {TIMESTAMP}
**Next Recommended Audit**: {NEXT_AUDIT_DATE}

---

## Notes

{ADDITIONAL_NOTES}
