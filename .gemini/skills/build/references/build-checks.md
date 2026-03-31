# Build Checks Reference

Pre-commit build verification commands and troubleshooting guide.

## Check Categories

### Frontend Checks

| Check | Command | Purpose |
|-------|---------|---------|
| Lint | `npm run lint` | TypeScript + ESLint validation |
| Build | `npm run build` | Production build compilation |
| Test | `npm run test` | Jest unit tests |

### Backend Checks

| Check | Command | Purpose |
|-------|---------|---------|
| Django Check | `python manage.py check` | Django system validation |
| Test | `pytest` | Pytest unit tests |

## Execution Order

```
1. Frontend Lint    (fast, catches most TS errors)
2. Frontend Build   (thorough, catches all build issues)
3. Frontend Test    (validates functionality)
4. Backend Check    (fast, Django validation)
5. Backend Test     (validates functionality)
```

## Common Errors and Fixes

### TypeScript Errors (Lint/Build)

**Type mismatch:**
```
Type 'string' is not assignable to type 'number'
```
Fix: Check variable types, add type assertions, or update interface.

**Missing property:**
```
Property 'x' does not exist on type 'Y'
```
Fix: Add property to interface or use optional chaining `?.`

**Import errors:**
```
Cannot find module '@/components/X'
```
Fix: Check file exists, verify path alias in tsconfig.json.

### ESLint Errors

**Unused variables:**
```
'x' is defined but never used
```
Fix: Remove unused variable or prefix with underscore `_x`.

**Missing dependencies in hooks:**
```
React Hook useEffect has a missing dependency
```
Fix: Add dependency to array or use `// eslint-disable-next-line`.

### Next.js Build Errors

**Server/Client boundary:**
```
'use client' directive required
```
Fix: Add `'use client'` at top of file using hooks or browser APIs.

**Static generation error:**
```
getServerSideProps cannot be used with 'use client'
```
Fix: Move data fetching to server component or API route.

### Django Check Errors

**Model issues:**
```
(models.E004) 'unique_together' refers to field 'x' not found
```
Fix: Verify field name in model, run makemigrations.

**URL configuration:**
```
(urls.E004) URL pattern has no route
```
Fix: Check urlpatterns in urls.py.

### Pytest Errors

**Import errors:**
```
ModuleNotFoundError: No module named 'apps.x'
```
Fix: Verify PYTHONPATH, check pytest.ini configuration.

**Database errors:**
```
django.db.utils.OperationalError: no such table
```
Fix: Run `pytest --create-db` or check migrations.

## Timeouts

| Check | Default Timeout | Notes |
|-------|-----------------|-------|
| Frontend Lint | 120s | Large codebases may need more |
| Frontend Build | 300s | Production builds are slow |
| Frontend Test | 300s | Depends on test count |
| Backend Check | 30s | Usually very fast |
| Backend Test | 300s | Depends on test count |

## Environment Requirements

### Frontend
- Node.js 22+
- npm installed
- Working directory: `frontend/`

### Backend
- Python 3.14+
- Virtual environment activated
- Django settings configured
- Working directory: `backend/`

## Integration with /debugger

When build verification fails:
1. Note the failing check and error message
2. Invoke `/debugger` skill with error details
3. Follow systematic debugging workflow
4. Re-run `/gitops` after fixes

## Check Commands Reference

### Run Individually

```bash
# Frontend
cd frontend && npm run lint
cd frontend && npm run build
cd frontend && npm run test

# Backend
cd backend && python manage.py check
cd backend && pytest
```

### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All checks passed |
| 1 | One or more checks failed |

## Skip Behavior

- If a check fails, subsequent checks in that category may be skipped
- This prevents running tests on broken builds
- All failures are reported before blocking commit
