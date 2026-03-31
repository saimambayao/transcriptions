---
name: build
description: Build verification and TypeScript error fixing for Bangsamoro Development Platform. Runs lint, build, and test checks, identifies TypeScript errors, and fixes them systematically. Use when preparing code for commit, fixing build errors, resolving TypeScript issues, or validating changes before git operations. Integrates with /debugger for complex issues and /gitops for commit workflow.
disable-model-invocation: true
argument-hint: "[topic]"
---

# Build - Verification & TypeScript Error Fixing

Build verification and error fixing workflow for frontend (Next.js/TypeScript) and backend (Django/Python).

## When to Use

- Before committing code (run `/build` before `/gitops`)
- Fixing TypeScript or ESLint errors
- Resolving build failures
- Validating changes work correctly
- After significant code changes

## Workflow

**Complete /build workflow:**
1. Run lint checks (TypeScript + ESLint)
2. Run production build
3. Fix any errors found
4. Verify all checks pass
5. **Run /database verification** (migration chains + status)

### Step 1: Run Build Verification

Execute verification script or run checks manually:

```bash
# Full verification (frontend + backend)
python3 .gemini/skills/build/scripts/build_verify.py

# Frontend only
python3 .gemini/skills/build/scripts/build_verify.py --frontend-only

# Backend only
python3 .gemini/skills/build/scripts/build_verify.py --backend-only
```

**Manual commands:**
```bash
# Frontend (in order)
cd frontend && npm run lint     # TypeScript + ESLint
cd frontend && npm run build    # Production build
cd frontend && npm run test     # Jest unit tests

# Backend (in order)
cd backend && python manage.py check   # Django system check
cd backend && pytest                    # Unit tests
```

### Step 2: Analyze Failures

When checks fail, analyze the output:

**Output format:**
```
BUILD VERIFICATION RESULTS
==================================================

Frontend:
----------------------------------------
  [PASS] Lint (12.3s)
  [FAIL] Build (45.2s)
    Type 'string' is not assignable to type 'number'
    src/components/Dashboard.tsx:42

Backend:
----------------------------------------
  [PASS] Django Check (2.1s)
  [PASS] Test (15.4s)

==================================================
BUILD BLOCKED: 1 check(s) failed
```

### Step 3: Fix Errors

For each error, apply the appropriate fix pattern. See `references/typescript-errors.md` for common patterns.

**TypeScript error fixing approach:**
1. Read the file containing the error
2. Understand the error context
3. Apply the correct fix (type annotation, interface update, etc.)
4. Re-run the failing check to verify

### Step 4: Verify All Checks Pass

Re-run verification until all checks pass:

```
BUILD PASSED: 5 check(s) passed
```

### Step 5: Run Database Verification

After build passes, run `/database` workflow to verify migrations:

```bash
cd backend

# Verify migration dependency chain
python3 ../.gemini/skills/database/scripts/verify_migrations.py .

# Check migration status
python3 manage.py showmigrations --plan
```

**Expected output:**
```
MIGRATION DEPENDENCY VERIFICATION REPORT
============================================================
Scanned: X apps, Y migrations
[OK] No issues found. Migration dependency chain is valid.
```

All migrations should be marked `[X]` (applied). If issues found, see `/database` skill for troubleshooting.

## Common Error Patterns

### TypeScript Type Errors

**Type mismatch:**
```
Type 'string' is not assignable to type 'number'
```
Fix: Check variable types, add type assertions, update interface.

**Missing property:**
```
Property 'x' does not exist on type 'Y'
```
Fix: Add property to interface or use optional chaining `?.`

**Null/undefined errors:**
```
Object is possibly 'undefined'
```
Fix: Add null check, use optional chaining, or non-null assertion.

### ESLint Errors

**Unused variables:**
```
'x' is defined but never used
```
Fix: Remove variable or prefix with underscore `_x`.

**Missing hook dependencies:**
```
React Hook useEffect has a missing dependency
```
Fix: Add dependency to array or use `// eslint-disable-next-line`.

### Next.js Build Errors

**Client/Server boundary:**
```
'use client' directive required
```
Fix: Add `'use client'` at top of file using hooks or browser APIs.

**Import errors:**
```
Cannot find module '@/components/X'
```
Fix: Check file exists, verify path alias in tsconfig.json.

### Django Errors

**Model issues:**
```
(models.E004) 'unique_together' refers to field 'x' not found
```
Fix: Verify field name in model, run makemigrations.

**Import errors:**
```
ModuleNotFoundError: No module named 'apps.x'
```
Fix: Verify PYTHONPATH, check conftest.py configuration.

## Integration

### With /database

After build checks pass, database verification runs automatically:
1. Migration dependency chain is verified
2. Migration status is checked (all should be applied)
3. If issues found, `/database` skill provides troubleshooting guidance

### With /debugger

For complex errors that aren't straightforward fixes:
1. Note the error message and file location
2. Invoke `/debugger` skill with error details
3. Follow systematic debugging workflow
4. Return to `/build` to verify fix

### With /gitops

After all checks pass (including database verification):
1. Run `/gitops` to commit and push
2. Build verification is NOT repeated in gitops (assumes `/build` passed)

## Quick Reference

### Check Commands
```bash
cd frontend && npm run lint      # TypeScript + ESLint
cd frontend && npm run build     # Production build
cd frontend && npm run test      # Jest tests
cd backend && python manage.py check  # Django check
cd backend && pytest             # Pytest
```

### Timeouts
| Check | Timeout |
|-------|---------|
| Frontend Lint | 120s |
| Frontend Build | 300s |
| Frontend Test | 300s |
| Backend Check | 30s |
| Backend Test | 300s |

## Constraints

- Fix all errors before committing (no bypass)
- Lint must pass before build
- Build must pass before tests
- For complex errors, use /debugger skill
- Always verify fix by re-running the check
