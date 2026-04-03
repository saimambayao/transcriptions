# Bug Documentation Reference

Documentation standards for tracking bugs in the Bangsamoro Development Platform.

## Directory Structure

```
docs/bugs/
├── 122025/           # December 2025
│   ├── 2025-12-01.md
│   ├── 2025-12-02.md
│   └── ...
├── 012026/           # January 2026
│   ├── 2026-01-01.md
│   └── ...
└── ...
```

## Daily Bug Log Template

**File naming**: `YYYY-MM-DD.md` (e.g., `2025-12-25.md`)

```markdown
# Bug Log - YYYY-MM-DD

## Bug: [Bug Name]

**Bug Brief**: [One sentence description of the bug]

**Status**: Identified | Fixing | Fixed

**Location**:
- File: `path/to/file.tsx`
- Component/Function: `ComponentName`
- Layer: Frontend / API / Database

**Root Cause**: [Identified after investigation]

**Fix Applied**: [Description of the fix]

**Lesson Learned**: [Pattern to recognize in future]

---

## Bug: [Another Bug Name]

...
```

## Status Definitions

| Status | Meaning | When to Set |
|--------|---------|-------------|
| **Identified** | Bug captured and documented | After Phase 2: Bug Brief |
| **Fixing** | Active investigation/fix in progress | After Phase 3: User Confirmation |
| **Fixed** | Bug resolved and verified | After Phase 5: Resolution |

## Bug Entry Template

Use this template when adding a new bug:

```markdown
## Bug: [Descriptive Name]

**Bug Brief**: [One sentence description]

**Status**: Identified

**Reported**: YYYY-MM-DD HH:MM

**Location**:
- File: `[file path]`
- Component/Function: `[name]`
- Layer: [Frontend / API / Database]

**Initial Hypothesis**: [From Bug Brief]

**Confidence**: [Low / Medium / High]

---
```

## Status Update Template

When updating status to **Fixing**:
```markdown
**Status**: Fixing

**Investigation Started**: YYYY-MM-DD HH:MM

**Findings**: [What was discovered during investigation]
```

When updating status to **Fixed**:
```markdown
**Status**: Fixed

**Fixed At**: YYYY-MM-DD HH:MM

**Root Cause**: [Actual root cause discovered]

**Fix Applied**: [Description of the fix]

**Files Changed**:
- `path/to/file1.tsx`
- `path/to/file2.py`

**Lesson Learned**: [Pattern to recognize in future]

**Bug Brief Revised**: [Yes/No - if initial hypothesis was wrong]
```

## Bug Audit Query Patterns

When auditing previous bugs, search for:

```bash
# Search by keyword
grep -r "keyword" docs/bugs/

# Search by component
grep -r "ComponentName" docs/bugs/

# Search by error message
grep -r "error message" docs/bugs/

# Search by file path
grep -r "path/to/file" docs/bugs/

# Search by status (find unfixed bugs)
grep -r "Status.*Identified\|Status.*Fixing" docs/bugs/
```

## Example Daily Bug Log

```markdown
# Bug Log - 2025-12-25

## Bug: Dashboard Blank After Save

**Bug Brief**: Dashboard fails to render after save action due to premature navigation.

**Status**: Fixed

**Reported**: 2025-12-25 09:30

**Location**:
- File: `frontend/src/app/(tenant)/portal/dashboard/page.tsx`
- Component/Function: `useSaveMutation` → `onSuccess`
- Layer: Frontend (TanStack Query)

**Initial Hypothesis**: Query invalidation too aggressive

**Confidence**: Medium

**Investigation Started**: 2025-12-25 09:45

**Findings**: Navigation happening before query invalidation completes

**Fixed At**: 2025-12-25 10:30

**Root Cause**: `router.push()` called before `await queryClient.invalidateQueries()`

**Fix Applied**: Added `await` before query invalidation and moved navigation after

**Files Changed**:
- `frontend/src/app/(tenant)/portal/dashboard/page.tsx`

**Lesson Learned**: Always await query invalidation before navigation in mutation callbacks

**Bug Brief Revised**: Yes - initial hypothesis was partially correct but missed navigation timing

---

## Bug: 401 Error on Product List

**Bug Brief**: Product list API returns 401 after 30 minutes of inactivity.

**Status**: Fixing

**Reported**: 2025-12-25 14:00

**Location**:
- File: `frontend/src/lib/services/api.ts`
- Component/Function: `apiClient` interceptor
- Layer: Frontend (Auth)

**Initial Hypothesis**: JWT refresh not triggered on 401

**Confidence**: Medium

**Investigation Started**: 2025-12-25 14:15

**Findings**: Investigating refresh token flow...
```

## Monthly Summary (Optional)

At the end of each month, create a summary file:

**File**: `MMYYYY/summary.md`

```markdown
# Bug Summary - December 2025

## Statistics
- Total Bugs: 15
- Fixed: 12
- Fixing: 2
- Identified: 1

## Most Common Issues
1. TanStack Query invalidation (4 bugs)
2. Authentication/JWT (3 bugs)
3. Hydration mismatch (2 bugs)

## Lessons Learned
- Always await query invalidation before navigation
- Add error boundaries to all data-fetching components
- Use proper TypeScript types for API responses
```


---

# Phase 6-7: Resolution & Bug Brief Revision

## Phase 6: Resolution

After implementing the fix:

1. Verify the fix resolves the original issue
2. Test edge cases
3. Run related tests
4. Check for regressions

**Update bug documentation to Fixed:**
```markdown
**Status**: Fixed

**Fixed At**: YYYY-MM-DD HH:MM

**Root Cause**: [Actual root cause discovered]

**Fix Applied**: [Description of the fix]

**Files Changed**:
- `path/to/file1.tsx`
- `path/to/file2.py`

**Lesson Learned**: [Pattern to recognize in future]
```
