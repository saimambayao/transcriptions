# Bug Brief Reference

Quick-reference for creating and managing Bug Briefs during debugging.

## Bug Brief Template

```markdown
## Bug Brief

**Summary**: [One sentence describing the bug]

**Observed Behavior**: [What actually happens]

**Expected Behavior**: [What should happen]

**Probable Location**:
- File: `path/to/file.tsx`
- Component/Function: `ComponentName` / `functionName()`
- Layer: Frontend / API / Database

**Initial Hypothesis**: [Best guess at root cause]

**Confidence**: Low / Medium / High
```

## Confidence Levels

| Level | Meaning | When to Use |
|-------|---------|-------------|
| **High** | Strong evidence points to cause | Clear error message, stack trace points to exact line |
| **Medium** | Reasonable guess based on patterns | Similar bugs seen before, likely area identified |
| **Low** | Limited information, multiple possibilities | Vague symptoms, no clear error, needs investigation |

## Examples by Bug Type

### Frontend State Bug

```markdown
## Bug Brief

**Summary**: Dashboard fails to render after save action due to state reset.

**Observed Behavior**: Clicking "Save" causes the dashboard to show a blank page.

**Expected Behavior**: Dashboard should persist data and remain visible after save.

**Probable Location**:
- File: `frontend/src/app/(tenant)/portal/dashboard/page.tsx`
- Component/Function: `useSaveMutation` → `onSuccess` callback
- Layer: Frontend (TanStack Query state)

**Initial Hypothesis**: The save mutation's `onSuccess` is invalidating queries too aggressively, causing a flash of empty state before refetch completes.

**Confidence**: Medium
```

### API Integration Bug

```markdown
## Bug Brief

**Summary**: Product list returns 401 Unauthorized after session timeout.

**Observed Behavior**: After ~30 minutes of inactivity, product list API returns 401 and page shows "Unauthorized" error.

**Expected Behavior**: Token should auto-refresh, or user should be redirected to login.

**Probable Location**:
- File: `frontend/src/lib/services/api.ts`
- Component/Function: `apiClient` interceptor / token refresh logic
- Layer: Frontend (Auth handling)

**Initial Hypothesis**: JWT refresh token logic is not being triggered on 401 responses, or refresh endpoint is failing silently.

**Confidence**: Medium
```

### Hydration Bug

```markdown
## Bug Brief

**Summary**: Hydration mismatch on date display component.

**Observed Behavior**: Console shows "Text content does not match server-rendered HTML" warning. Date flickers on page load.

**Expected Behavior**: Date should render consistently without hydration warnings.

**Probable Location**:
- File: `frontend/src/components/DateDisplay.tsx`
- Component/Function: `DateDisplay` component
- Layer: Frontend (Next.js SSR/CSR boundary)

**Initial Hypothesis**: Date is being formatted during SSR with server timezone, then re-rendered on client with browser timezone, causing mismatch.

**Confidence**: High
```

### Database/Query Bug

```markdown
## Bug Brief

**Summary**: Cooperative members list shows members from other organizations.

**Observed Behavior**: Admin for Coop A sees members belonging to Coop B in their member list.

**Expected Behavior**: Each organization should only see their own members (multi-tenant isolation).

**Probable Location**:
- File: `backend/apps/tenant/api.py`
- Component/Function: `list_members` endpoint / queryset filter
- Layer: Backend (Django ORM query)

**Initial Hypothesis**: The queryset is missing `.filter(organization=request.user.organization)` or the organization context is not being passed correctly.

**Confidence**: High
```

### Build/Deployment Bug

```markdown
## Bug Brief

**Summary**: Production build fails with "Module not found" for @/components/ui.

**Observed Behavior**: `npm run build` fails in CI with error: "Cannot find module '@/components/ui/button'".

**Expected Behavior**: Build should complete successfully. Works in development.

**Probable Location**:
- File: `frontend/tsconfig.json` or `frontend/next.config.ts`
- Component/Function: Path alias configuration
- Layer: Build configuration

**Initial Hypothesis**: Path aliases are configured for dev but not resolving correctly in production build. May need to check `baseUrl` and `paths` in tsconfig.

**Confidence**: Medium
```

## Bug Brief Revision Template

Use when initial hypothesis was incorrect:

```markdown
## Bug Brief - REVISED

**Original Hypothesis**: [What we initially thought]

**Actual Root Cause**: [What we discovered]

**Key Finding**: [The insight that led to the real cause]

**Lesson Learned**: [Pattern to recognize in future debugging]
```

### Revision Example

```markdown
## Bug Brief - REVISED

**Original Hypothesis**: Save mutation invalidating queries too aggressively.

**Actual Root Cause**: The `onSuccess` callback was calling `router.push()`
before the query refetch completed, causing an unmounted component state
update that silently failed.

**Key Finding**: The navigation was happening in a `setTimeout` with 0ms delay,
which still executed before the async invalidation completed.

**Lesson Learned**: When debugging blank page after mutation, check for:
1. Navigation side effects in mutation callbacks
2. Async timing issues between invalidation and navigation
3. Use `await queryClient.invalidateQueries()` before navigation
```

## Quick Checklist

Before presenting Bug Brief to user:

- [ ] Summary is one clear sentence
- [ ] Observed vs Expected is specific (not vague)
- [ ] File path is as specific as possible
- [ ] Layer is identified (Frontend/API/Database)
- [ ] Hypothesis is testable
- [ ] Confidence level is honest

After fix is complete:

- [ ] Was initial hypothesis correct?
- [ ] If not, document revision
- [ ] Capture lesson learned for future debugging
