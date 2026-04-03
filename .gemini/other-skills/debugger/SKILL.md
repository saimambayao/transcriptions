---
name: debugger
description: Systematic debugging workflow for Bangsamoro Development Platform (Next.js + React + Django Ninja). Starts with Bug Brief -- capturing and confirming bug understanding before deep investigation. Use when investigating errors, tracking down bugs, analyzing production issues, or performing root cause analysis with permanent fixes. Accepts screenshots and error descriptions. Integrates with /investigator for research and /build for verification.
argument-hint: "[error message or bug description]"
---

# Debugger Skill - Bangsamoro Development Platform

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's debugging request                        ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

Systematic debugging workflow with Bug Brief confirmation for the Bangsamoro multi-portal architecture.

## Bug Documentation

Bugs are documented in `docs/bugs/MMYYYY/YYYY-MM-DD.md` (e.g., `docs/bugs/122025/2025-12-25.md`).

**See [references/bug-documentation.md](references/bug-documentation.md) for full documentation standards.**

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────┐
│  BUG BRIEF WORKFLOW WITH DOCUMENTATION                      │
│                                                             │
│  Phase 0: Bug Capture                                       │
│           ↓                                                 │
│  Phase 1: Bug Audit & Doc ──► Search docs/bugs/ + Document  │
│           ↓                                                 │
│  Phase 2: Initial Investigation                             │
│           ↓                                                 │
│  Phase 3: Bug Brief ──► Update: Status = Identified         │
│           ↓                                                 │
│  Phase 4: User Confirmation ◄── GATE                        │
│           ↓                                                 │
│  Phase 5: Deep Investigation ──► Update: Status = Fixing    │
│           ↓                                                 │
│  Phase 6: Resolution ──► Update: Status = Fixed             │
│           ↓                                                 │
│  Phase 7: Bug Brief Revision + Final Documentation          │
└─────────────────────────────────────────────────────────────┘
```

## Phase 0: Bug Capture

Accept bug report from user (screenshot, error message, description).

**Extract from input:**
- Error message or unexpected behavior
- Screenshot context (if provided)
- User's description of what went wrong
- When/where it occurs

**Example input:**
```
User: "The dashboard isn't loading after I click save"
[Screenshot showing blank page]
```

## Phase 1: Bug Audit & Documentation

**Before investigating, check if this bug was encountered before AND create initial documentation.**

### 1.1 Search for Similar Bugs

```bash
# Search for similar bugs in documentation
grep -ri "dashboard" docs/bugs/
grep -ri "blank page" docs/bugs/
grep -ri "save" docs/bugs/

# Check recent bug logs
ls -la docs/bugs/$(date +%m%Y)/
```

**If similar bug found:**
- Review previous root cause and fix
- Check if same fix applies
- Reference previous bug in new documentation

### 1.2 Create Bug Documentation Entry

```bash
# Create monthly directory if needed
mkdir -p docs/bugs/$(date +%m%Y)
```

Add entry to `docs/bugs/MMYYYY/YYYY-MM-DD.md`:

```markdown
## Bug: [Descriptive Name]

**Bug Brief**: [One sentence description - preliminary]

**Status**: Identified

**Reported**: YYYY-MM-DD HH:MM

**Location**: TBD (pending investigation)

**Initial Hypothesis**: TBD

**Confidence**: Low
```

## Phase 2: Initial Investigation

Quick codebase scan (2-3 minutes max) to locate probable bug area.

**Activities:**
1. Search for relevant files based on error/description
2. Identify likely component, page, or API endpoint
3. Check recent changes in git if applicable
4. Note any obvious error patterns

**Quick scan commands:**
```bash
# Find relevant files
grep -r "Dashboard" frontend/src/app/
grep -r "save" frontend/src/components/

# Check recent changes
git log --oneline -10
git diff HEAD~3 -- frontend/src/
```

## Phase 3: Bug Brief

Present concise bug definition for user validation AND update documentation.

**See [references/bug-brief.md](references/bug-brief.md) for full template and examples.**

**Bug Brief Structure:**
- **Summary**: One sentence describing the bug
- **Observed Behavior**: What actually happens
- **Expected Behavior**: What should happen
- **Probable Location**: File, Component/Function, Layer
- **Initial Hypothesis**: Best guess at root cause
- **Confidence**: Low / Medium / High

**Update bug documentation** with investigation findings:

```markdown
**Bug Brief**: [Updated one sentence description]

**Status**: Identified

**Location**:
- File: `[file path]`
- Component/Function: `[name]`
- Layer: [Frontend / API / Database]

**Initial Hypothesis**: [From Bug Brief]

**Confidence**: [Low / Medium / High]
```

## Phase 4: User Confirmation

**GATE: Do not proceed without user confirmation.**

Present Bug Brief and ask:

```
Does this Bug Brief capture the issue correctly?

1. "Yes, proceed with deep investigation"
2. "No, the issue is actually [correction]"
3. "Let me provide more context: [details]"
```

**If user corrects:**
- Update Bug Brief with corrections
- Re-confirm before proceeding

**If user confirms:**
- Proceed to Phase 5 (Deep Investigation)

## Phase 5: Deep Investigation

After user confirms Bug Brief, proceed with the 7-Step Debugging workflow.

**Update bug documentation status:**
```markdown
**Status**: Fixing

**Investigation Started**: YYYY-MM-DD HH:MM
```

---

## Tech Stack Coverage

**Frontend:**
- Next.js 16+ (App Router, Server/Client Components)
- React 19+ (Hooks, State, Effects)
- TypeScript
- TanStack Query
- Tailwind CSS v4

**Backend:**
- Django 6.0 + Django Ninja
- PostgreSQL 18

**Infrastructure:**
- Railway deployment
- Docker containers

## When to Use

- Encountering errors in development or production
- Investigating unexpected behavior or bugs
- Analyzing failed tests or broken features
- Debugging React/Next.js rendering issues
- Troubleshooting API integration problems
- Investigating deployment or build failures

## Workflow Selection

Use **Comprehensive Debugging** for production issues, multi-layer errors, and when root cause is unclear. Use **Quick-Fix** for obvious typos/missing imports in dev only. Default: Comprehensive.

## Comprehensive 7-Step Debugging

See [comprehensive-debugging.md](references/comprehensive-debugging.md) for the full 7-step debugging workflow with reproduction, isolation, evidence gathering, hypothesis testing, fix implementation, and documentation.

# Local
python manage.py runserver  # Watch output

# Production
railway logs --tail 200 > debug-logs.txt

# Use bundled log analyzer
python scripts/analyze_logs.py --file debug-logs.txt
```

**See [debugging-checklist.md](references/debugging-checklist.md) for comprehensive checklist.**

### Step 4: Formulate Hypotheses

**Common CSEA Hypotheses:**

| Symptom | Likely Cause |
|---------|--------------|
| "Hydration mismatch" | Server/Client component boundary issue |
| "undefined is not a function" | Missing import or null check |
| Stale data after mutation | Missing query invalidation |
| 401 Unauthorized | JWT expired or missing |
| 422 Validation Error | Schema mismatch (frontend types vs backend) |
| 500 Internal Server Error | Backend exception, check Django logs |
| Component not rendering | Conditional rendering issue, bad state |
| Data not updating | TanStack Query cache, missing refetch |

**Five Whys Example:**
```
Bug: Dashboard shows stale data after creating a new product

Why? → TanStack Query cache not invalidated
Why? → Mutation doesn't call queryClient.invalidateQueries
Why? → useMutation hook missing onSuccess callback
Why? → Copy-pasted from another hook without customization
Why? → No mutation template/pattern documented

Root Cause: Missing query invalidation in mutation hook
```

**See [root-cause-analysis.md](references/root-cause-analysis.md) for Five Whys technique.**

### Step 5: Test Hypotheses

**Frontend Testing:**

```typescript
// Test with isolated component
function DebugComponent() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['test'],
    queryFn: async () => {
      console.log('Fetching...');
      const result = await fetch('/api/test');
      console.log('Response:', result);
      return result.json();
    },
  });

  console.log('Render state:', { data, isLoading, error });
  return <pre>{JSON.stringify({ data, isLoading, error }, null, 2)}</pre>;
}
```

**API Testing:**

```bash
# Test endpoint directly
curl -X GET http://localhost:8090/api/endpoint/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
```

**Django Shell:**

```python
python manage.py shell

from apps.myapp.models import MyModel
MyModel.objects.filter(organization_id=1).values()
```

**Use bundled Django debugger:**
```bash
python scripts/debug_django.py --model MyModel --org 1
```

### Step 6: Implement Permanent Fix

**Fix Principles:**

**Do:**
- Fix root cause, not symptoms
- Add error handling
- Update types if needed
- Test the fix
- Consider similar patterns elsewhere

**Don't:**
- Comment out failing code
- Add temporary hacks
- Skip testing
- Ignore TypeScript errors

**Common Fixes:**

**Hydration Mismatch:**
```typescript
// Move browser-only code to useEffect
'use client';

import { useState, useEffect } from 'react';

export function DateDisplay() {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) return null;

  return <span>{new Date().toLocaleDateString()}</span>;
}
```

**TanStack Query Invalidation:**
```typescript
const mutation = useMutation({
  mutationFn: createProduct,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['products'] });
  },
});
```

**Missing Null Check:**
```typescript
// Before
const name = user.organization.name;

// After
const name = user?.organization?.name ?? 'Unknown';
```

**API Error Handling:**
```typescript
const { data, error, isLoading } = useQuery({
  queryKey: ['data'],
  queryFn: fetchData,
});

if (error) {
  return <ErrorDisplay message={error.message} />;
}
```

### Step 7: Document & Prevent

**Add Error Handling:**
```typescript
// Add error boundary for component
import { ErrorBoundary } from 'react-error-boundary';

<ErrorBoundary fallback={<ErrorFallback />}>
  <MyComponent />
</ErrorBoundary>
```

**Add TypeScript Types:**
```typescript
// Ensure types match API response
interface ApiResponse {
  id: number;
  name: string;
  status: 'active' | 'inactive';
}
```

**Add Tests:**
```typescript
test('should handle API error gracefully', async () => {
  server.use(
    http.get('/api/data', () => {
      return HttpResponse.json({ error: 'Not found' }, { status: 404 });
    })
  );

  render(<MyComponent />);

  expect(await screen.findByText('Error loading data')).toBeInTheDocument();
});
```

---

## Phase 6: Resolution

Verify fix, test edge cases, check regressions. Update bug doc to "Fixed" with root cause and files changed.

## Phase 7: Bug Brief Revision

Revise Bug Brief if root cause differed from initial hypothesis. See [bug-brief.md](references/bug-brief.md) for revision template.

## Quick Reference: Debugging by Error Type

See [debugging-checklist.md](references/debugging-checklist.md) for Next.js, React, TanStack Query, and Django Ninja error reference tables.

## CSEA-Specific Debugging

See [debugging-checklist.md](references/debugging-checklist.md) for multi-portal context, multi-tenant issues, and authentication debugging.

## Tools Reference

See [debugging-checklist.md](references/debugging-checklist.md) for browser DevTools, command line, and VS Code debugging tools.

# Frontend dev server with verbose logging
npm run dev

# Backend dev server
python manage.py runserver

# Production logs
railway logs --tail 200

# Test API endpoints
curl -X GET http://localhost:8090/api/docs
```

### VS Code
- Breakpoints in TypeScript/Python
- Debug console
- Watch variables

## Resources Index

| Type | Files |
|------|-------|
| References | bug-brief.md, bug-documentation.md, debugging-checklist.md, production-debugging.md, reproduction-techniques.md, root-cause-analysis.md, ultrathinking-workflow.md |
| Assets | debugging_quick_reference.md, error_report_template.md, ultrathinking-example.md, workflow_selection_guide.md |
| Scripts | analyze_logs.py, debug_django.py |

## Anti-Patterns

**Don't:** Skip Bug Brief, skip reproduction, guess at fixes, comment out code, deploy untested fixes.
**Do:** Present Bug Brief first, get user confirmation, follow 7-step workflow, gather evidence, write tests.

