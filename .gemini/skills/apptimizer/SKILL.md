---
name: apptimizer
description: Systematic performance optimization for Bangsamoro Development Platform. Orchestrates multiple skills (prompter, coditor, investigator, debugger, refactor) to analyze, plan, and implement performance improvements across Next.js frontend and Django Ninja backend. Requires user approval before implementing optimizations.
argument-hint: "[topic]"
---

# Apptimizer - CSEA Performance Optimizer

## Phase 0: Prompt Refinement (Mandatory)

**Before executing this skill's workflow, invoke `/prompter` first:**

1. Invoke `/prompter` with the user's optimization request
2. Present the refined prompt to the user
3. Wait for user confirmation:
   - "Yes, proceed" → Continue to Phase 1 (Clarification)
   - "No, adjust X" → Refine and re-confirm
   - "Let me rephrase" → Restart with new input

**Do not proceed without user confirmation.**

---

## Overview

Apptimizer is a specialized orchestration skill for optimizing Bangsamoro Development Platform performance. It follows a systematic workflow that combines multiple skills to identify performance bottlenecks, research best practices, plan optimizations, and implement improvements.

**Core Philosophy**: Apptimizer **analyzes first, plans second, implements third** - always with user approval before making changes.

## Tech Stack

**Frontend:**
- Next.js 16+ (SSR, SSG, ISR optimization)
- React 19+ (component optimization)
- TanStack Query (data fetching, caching)

**Backend:**
- Django 6.0 + Django Ninja (API optimization)
- PostgreSQL 18 (query optimization)

## When to Use This Skill

Invoke Apptimizer when:
- **Performance Issues**: "The marketplace is slow", "API responses are slow"
- **Optimization Requests**: "Optimize CSEA performance", "Improve load times"
- **Specific Bottlenecks**: "Optimize database queries", "Reduce bundle size"
- **Proactive Optimization**: "Audit and optimize CSEA"
- **Scaling Preparation**: "Prepare CSEA for more users"

**Keywords**: "optimize", "performance", "slow", "speed up", "improve response time", "bottleneck"

## Optimization Workflow

### Phase 1: Clarification (Prompter)

**Purpose**: Understand optimization goals and constraints

**Questions Asked**:
- What specific performance issue are you experiencing?
- Which areas need optimization? (Frontend, Backend, Database, All)
- What are your performance goals? (Response time, bundle size, query speed)
- Any constraints? (No breaking changes allowed?)

### Phase 2: Audit (Coditor)

**Purpose**: Identify performance issues in codebase

**Frontend Audit Focus**:
- Large bundle size
- Missing React.memo/useMemo optimizations
- Inefficient TanStack Query patterns
- Missing image optimization
- Unnecessary re-renders

**Backend Audit Focus**:
- N+1 queries
- Missing database indexes
- Slow API endpoints
- Missing pagination
- No response caching

**Output**: Performance audit report with severity-based findings

### Phase 3: Research (Investigator)

**Purpose**: Research best practices for identified issues

**Research Areas**:
- Next.js performance optimization
- TanStack Query caching strategies
- Django query optimization patterns
- PostgreSQL indexing strategies

**Output**: Evidence-based recommendations with sources

### Phase 4: Planning (Analysis & Approval)

**Purpose**: Present optimization plan and get user approval

**Plan Structure**:
1. Optimization Goals
2. Identified Issues (by severity)
3. Proposed Solutions (with evidence)
4. Implementation Plan
5. Expected Impact
6. Risk Assessment

**User Approval Required**: Apptimizer waits for explicit approval before implementing

### Phase 5: Implementation (Skill Orchestration)

**Skills Invoked** (based on plan):

- **Frontend Optimizations**: React component optimization, TanStack Query tuning
- **Backend Optimizations**: Django query optimization, API caching
- **Database Optimizations**: Indexing, query refactoring
- **Code Cleanup**: Refactoring, consolidation

### Phase 6: Verification

**Purpose**: Verify optimizations worked

**Actions**:
1. Run performance tests
2. Measure key metrics
3. Compare before/after results
4. Document improvements

## Optimization Domains

### 1. Frontend Optimization (Next.js + React)

**Common Issues**:
- Large bundle size
- Slow initial page load
- Unnecessary re-renders
- Unoptimized images

**Optimizations**:
```typescript
// Image optimization
import Image from 'next/image';
<Image src="/hero.jpg" width={800} height={600} priority />

// Dynamic imports for code splitting
const HeavyComponent = dynamic(() => import('./HeavyComponent'), {
  loading: () => <Skeleton />
});

// Memoization
const MemoizedCard = React.memo(CooperativeCard);

// TanStack Query optimization
const { data } = useQuery({
  queryKey: ['cooperatives'],
  queryFn: getCooperatives,
  staleTime: 5 * 60 * 1000, // 5 minutes
  cacheTime: 10 * 60 * 1000, // 10 minutes
});
```

### 2. Backend Optimization (Django Ninja)

**Common Issues**:
- N+1 queries
- Slow API responses
- No pagination
- Missing caching

**Optimizations**:
```python
# select_related for ForeignKey
@router.get('/cooperatives')
def list_cooperatives(request):
    return Cooperative.objects.select_related(
        'organization'
    ).filter(organization=request.auth.organization)

# prefetch_related for reverse/M2M
@router.get('/cooperatives')
def list_with_products(request):
    return Cooperative.objects.prefetch_related(
        'products'
    ).filter(organization=request.auth.organization)

# Pagination
from ninja.pagination import paginate, PageNumberPagination

@router.get('/cooperatives')
@paginate(PageNumberPagination)
def list_cooperatives(request):
    return Cooperative.objects.filter(
        organization=request.auth.organization
    )
```

### 3. Database Optimization (PostgreSQL)

**Common Issues**:
- Missing indexes
- Slow queries
- Inefficient joins

**Optimizations**:
```python
# Add indexes for frequently filtered fields
class Cooperative(models.Model):
    status = models.CharField(max_length=20, db_index=True)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        db_index=True
    )

    class Meta:
        indexes = [
            models.Index(fields=['organization', 'status']),
            models.Index(fields=['-created_at']),
        ]
```

### 4. TanStack Query Optimization

**Common Issues**:
- Over-fetching
- Missing cache invalidation
- Stale data

**Optimizations**:
```typescript
// Optimized query configuration
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 5 * 60 * 1000,
      cacheTime: 10 * 60 * 1000,
      refetchOnWindowFocus: false,
      retry: 1,
    },
  },
});

// Selective invalidation
const mutation = useMutation({
  mutationFn: createCooperative,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['cooperatives'] });
  },
});

// Prefetching
const prefetchCooperative = async (id: string) => {
  await queryClient.prefetchQuery({
    queryKey: ['cooperative', id],
    queryFn: () => getCooperative(id),
  });
};
```

## Example Optimization Plan

```markdown
# CSEA Performance Optimization Plan

## Optimization Goals
- Reduce marketplace page load from 3s to <1s
- Reduce API response time by 50%
- Reduce database query count by 80%

## Issues Identified

### Critical
1. N+1 queries in cooperative list endpoint (100+ queries → 1)
2. Missing pagination on marketplace (1000+ products rendered)

### High
3. Large bundle size (no code splitting)
4. No TanStack Query caching configured

### Medium
5. Missing database indexes on frequently filtered columns
6. Images not optimized

## Proposed Solutions

### Solution 1: Database Query Optimization
- Add select_related() to API endpoints
- Add database indexes
- Expected: 100 queries → 2 queries

### Solution 2: Pagination
- Add pagination to list endpoints
- Limit to 25 items per page
- Expected: Page load 3s → 0.5s

### Solution 3: Code Splitting
- Dynamic imports for heavy components
- Expected: Bundle size -40%

### Solution 4: TanStack Query Caching
- Configure staleTime and cacheTime
- Add selective invalidation
- Expected: API calls -60%

## Approval Required

Do you approve this optimization plan? (y/n)
```

## Safety Considerations

### 1. Always Get Approval

**Rule**: NEVER implement optimizations without user approval

### 2. Test Before Deploy

**Rule**: All optimizations must be verified locally

### 3. Measure Impact

**Rule**: Always measure before/after metrics

### 4. No Breaking Changes (Unless Approved)

**Rule**: Avoid breaking changes unless explicitly approved

## Integration with Other Skills

```
User Request: "Optimize CSEA"

Apptimizer Workflow:
1. /prompter → Clarify requirements
2. /coditor → Audit for performance issues
3. /investigator → Research solutions
4. [Apptimizer creates plan]
5. [User approves plan]
6. /refactor → Implement optimizations
7. /debugger → Fix any issues
8. [Apptimizer measures results]
```

## Quick Start Examples

### Example 1: General Performance

**User**: "Optimize CSEA performance"

**Apptimizer**:
1. Clarifies scope with /prompter
2. Audits codebase with /coditor
3. Researches solutions with /investigator
4. Creates comprehensive plan
5. Waits for approval
6. Implements optimizations

### Example 2: Slow API

**User**: "API responses are slow"

**Apptimizer**:
1. Audits Django Ninja endpoints
2. Finds N+1 queries, missing pagination
3. Plans select_related, indexing, pagination
4. Waits for approval
5. Implements backend optimizations

### Example 3: Slow Page Load

**User**: "Marketplace loads slowly"

**Apptimizer**:
1. Audits Next.js bundle and rendering
2. Finds large bundle, unoptimized images
3. Plans code splitting, image optimization
4. Waits for approval
5. Implements frontend optimizations

---

**Remember**: Apptimizer **analyzes, plans, then implements** - always with your approval. It orchestrates multiple skills to deliver comprehensive, evidence-based performance optimizations.
