---
name: investigator
description: Deep investigation of errors and issues in Bangsamoro Development Platform. Researches online for at least 5 credible sources per solution, reads official documentation, and presents 3 evidence-based solution alternatives ranked by effectiveness. Use when investigating Next.js/React errors, TanStack Query issues, Django Ninja API failures, Railway deployment problems, PostgreSQL issues, authentication errors, or frontend TypeScript errors. This skill performs research and analysis only -- it does NOT implement solutions. Integrates with /debugger for fix implementation.
argument-hint: "[error or issue to investigate]"
context: fork
agent: Explore
---

# Investigator - Bangsamoro Development Platform

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's investigation request                    ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

Systematic, evidence-based investigation for CSEA's Next.js + Django Ninja architecture.

## Overview

**What This Skill Does:**
- Investigates errors using logs, codebase analysis, and official documentation
- Researches at least 5 credible sources per proposed solution
- Presents 3 solution alternatives ranked by effectiveness
- Provides evidence-based recommendations with trade-off analysis

**What This Skill Does NOT Do:**
- Implement solutions (investigation only)
- Make code changes
- Commit fixes

## When to Use

### Error Investigation Scenarios

- **Next.js errors**: Server/Client component issues, hydration mismatches, routing problems
- **React errors**: Hook violations, state issues, rendering problems
- **TanStack Query issues**: Cache problems, refetch failures, mutation errors
- **Django Ninja failures**: API errors, serialization issues, authentication problems
- **Railway deployment**: Build failures, startup errors, environment issues
- **PostgreSQL problems**: Connection issues, query failures, migration errors
- **TypeScript errors**: Type mismatches, module resolution, compilation failures
- **Authentication errors**: JWT issues, session problems, permission denied

### When NOT to Use

- Fix is obvious and well-understood
- Simple syntax errors or typos
- Need to implement (use debugger skill instead)

## Investigation Workflow

### Step 1: Define Scope

```markdown
**Error/Issue**: [One-sentence description]
**Environment**: Local / Staging / Production (Railway)
**Portal**: Public / C/SE Portal / CSEA Staff
**Frequency**: Consistent / Intermittent / One-time
**Recent Changes**: [What changed before error appeared]
```

### Step 2: Gather Evidence

**For Frontend (Next.js/React):**
- Browser console errors
- Network tab (API requests/responses)
- React DevTools state
- Next.js server logs (`npm run dev` output)

**For Backend (Django Ninja):**
- Django server logs
- API response bodies
- Database query errors

**For Production (Railway):**
```bash
railway logs --tail 200
```

### Step 3: Consult Error-Specific Workflow

| Error Type | Investigation Focus |
|------------|---------------------|
| Next.js Hydration | Server vs Client component boundaries, useEffect timing |
| TanStack Query | Query keys, stale time, cache invalidation |
| Django Ninja 4xx | Schema validation, authentication, permissions |
| Django Ninja 5xx | Exception handling, database queries, serialization |
| TypeScript | Type definitions, module resolution, tsconfig |
| Railway Deploy | Dockerfile, environment variables, build process |

### Step 4: Systematic Research

**Source Priority:**

1. **Tier 1: Official Documentation**
   - Next.js docs, React docs, TanStack Query docs
   - Django Ninja docs, Django docs
   - TypeScript handbook

2. **Tier 2: Official GitHub Issues**
   - nextjs/next.js issues
   - TanStack/query issues
   - vitalik/django-ninja issues

3. **Tier 3: Technical Communities**
   - Stack Overflow (filter by votes)
   - Reddit (r/nextjs, r/reactjs, r/django)
   - Discord communities

4. **Tier 4: Technical Blogs**
   - Vercel blog, React blog
   - Real Python, Django Stars

**Requirements:**
- At least 3 distinct solution approaches
- At least 5 credible sources per solution (15 total minimum)
- At least 2 Tier 1 sources per solution
- Sources within 2 years or verified applicable

### Step 5: Rank Solutions

**Criteria:**

| Factor | High | Medium | Low |
|--------|------|--------|-----|
| Effectiveness | Root cause fix, official approach | Symptom fix, community-validated | Workaround, single source |
| Risk | Easy to revert, backward compatible | Requires testing | Breaking changes |
| Effort | Config change, single file | Multiple files | Architectural change |

### Step 6: Present Report

```markdown
# Investigation Report

## Executive Summary
[2-3 sentence overview]

## Issue Details
- **Error**: [exact message]
- **Location**: [file:line or route]
- **Evidence**: [logs, screenshots, stack trace]

## Root Cause Analysis
[Technical explanation]

## Proposed Solutions

### Solution 1: [Name] ⭐ RECOMMENDED
**Approach**: [Description]
**Effectiveness**: High | **Risk**: Low | **Effort**: Low

**Evidence Sources:**
1. [URL] - [Key finding]
2. [URL] - [Key finding]
3. [URL] - [Key finding]
4. [URL] - [Key finding]
5. [URL] - [Key finding]

**Pros**: [List]
**Cons**: [List]

### Solution 2: [Name]
[Same structure]

### Solution 3: [Name]
[Same structure]

## Comparison Matrix

| Criteria | Solution 1 | Solution 2 | Solution 3 |
|----------|------------|------------|------------|
| Effectiveness | High | Medium | Low |
| Risk | Low | Medium | High |
| Effort | Low | Medium | High |

## Recommendation
[Which solution and why]

---
⚠️ **No changes implemented - user approval required**
```

## Common CSEA Error Patterns

### Next.js Hydration Mismatch
**Symptoms**: "Hydration failed" or "Text content does not match"
**Common Causes**:
- Using browser-only APIs in Server Components
- Date/time rendering differences
- Random values during SSR

**Research Focus**: Next.js App Router docs, React hydration docs

### TanStack Query Cache Issues
**Symptoms**: Stale data, missing updates, infinite refetching
**Common Causes**:
- Incorrect query keys
- Missing cache invalidation after mutations
- Stale time configuration

**Research Focus**: TanStack Query docs, cache strategies

### Django Ninja 422 Errors
**Symptoms**: Validation errors from API
**Common Causes**:
- Schema mismatch between frontend types and backend
- Missing required fields
- Type coercion issues

**Research Focus**: Django Ninja schema docs, Pydantic validation

### Railway Deployment Failures
**Symptoms**: Build fails, app won't start
**Common Causes**:
- Missing environment variables
- Dockerfile configuration issues
- Memory/resource limits

**Research Focus**: Railway docs, Next.js production docs

## CSEA-Specific Considerations

### Multi-Tenant Context
- Does error affect tenant data isolation?
- Is organization context being passed correctly?
- Are API endpoints properly scoped?

### Portal-Specific Issues
- Which portal is affected? (Public, C/SE, CSEA Staff)
- Is authentication/authorization working correctly?
- Are role-based permissions enforced?

### Frontend-Backend Integration
- Are TypeScript types matching Django Ninja schemas?
- Is TanStack Query configured correctly for the API?
- Are error boundaries handling API failures?

## Quality Standards

Every investigation MUST include:
- [ ] Minimum 15 sources (5 per solution × 3 solutions)
- [ ] At least 6 Tier 1 sources (official docs)
- [ ] 3 distinct solutions ranked by effectiveness
- [ ] Root cause identified with technical explanation
- [ ] CSEA-specific considerations addressed
- [ ] Clear recommendation marked
- [ ] Warning: "No changes implemented"

## Remember

**This skill investigates - it does NOT implement.**

After presenting the report:
1. Wait for user review
2. User decides which solution to pursue
3. User may ask to implement (switch to debugger skill)
4. User may request more research
