---
name: test
description: Full-suite testing for Bangsamoro Development Platform. Runs unit tests, integration tests, and E2E tests on newly implemented features before commit. Integrates with /build (runs after) and /gitops, /csea-push (runs before). Use when testing new features, validating changes, or as part of the pre-commit workflow.
disable-model-invocation: true
argument-hint: "[topic]"
---

# Test - Full-Suite Feature Testing

## Phase 0: Prompt Refinement (Mandatory)

**Before executing this skill's workflow, invoke `/prompter` first:**

1. Invoke `/prompter` with the user's testing request
2. Present the refined prompt to the user
3. Wait for user confirmation:
   - "Yes, proceed" → Continue to Step 1 (Detect Changed Features)
   - "No, adjust X" → Refine and re-confirm
   - "Let me rephrase" → Restart with new input

**Do not proceed without user confirmation.**

---

Comprehensive testing workflow for newly implemented features in Bangsamoro Development Platform (Next.js + Django Ninja).

## When to Use

- After implementing a new feature (before committing)
- Testing specific components, pages, or API endpoints
- Validating database migrations work correctly
- Running E2E tests on user workflows
- As part of pre-commit workflow: `/build` -> `/test` -> `/gitops`

## Workflow Position

```
Development Flow:
  Code Changes -> /build -> /test -> /gitops -> /csea-push
                     |         |         |           |
                     v         v         v           v
                  Lint     Tests    Commit      Deploy
                  Build   Unit/E2E   Push       Merge
```

## Workflow

### Step 1: Detect Changed Features

Analyze git diff to identify what needs testing:

```bash
git diff --name-only HEAD~1           # Last commit
git diff --name-only origin/main      # Against main
git status --short                    # Current changes
```

**Classify changes by category:**

| Path Pattern | Test Type | Command |
|--------------|-----------|---------|
| `frontend/src/components/**` | Unit + Component | Jest |
| `frontend/src/app/**` | Unit + E2E | Jest + Playwright |
| `frontend/src/lib/hooks/**` | Unit | Jest |
| `frontend/src/lib/services/**` | Unit + Integration | Jest |
| `backend/apps/**/api.py` | Integration | Pytest |
| `backend/apps/**/models.py` | Unit + Migration | Pytest |
| `backend/apps/**/migrations/**` | Migration | verify_migrations.py |

### Step 2: Run Unit Tests

#### Frontend (Jest)

```bash
# Run all frontend tests
cd frontend && npm run test

# Run tests for specific file/pattern
cd frontend && npm run test -- --testPathPattern="ComponentName"

# Run tests with coverage
cd frontend && npm run test -- --coverage
```

**Test file conventions:**
- Component: `ComponentName.test.tsx`
- Hook: `useHookName.test.ts`
- Service: `serviceName.test.ts`
- Utility: `utilName.test.ts`

#### Backend (Pytest)

```bash
# Run all backend tests
cd backend && pytest

# Run tests for specific app
cd backend && pytest apps/academy/

# Run specific test file
cd backend && pytest apps/academy/tests/test_api.py

# Run with coverage
cd backend && pytest --cov=apps --cov-report=term-missing
```

**Test file conventions:**
- API tests: `tests/test_api.py`
- Model tests: `tests/test_models.py`
- Service tests: `tests/test_services.py`

### Step 3: Run Integration Tests

Integration tests verify components work together across boundaries.

#### Frontend Integration

Test service layer and API integration:

```bash
cd frontend && npm run test -- --testPathPattern="integration"
```

#### Backend Integration

Test API endpoints with database:

```bash
cd backend && pytest -m integration
```

### Step 4: Run E2E Tests (When Applicable)

E2E tests verify complete user workflows through the browser.

**Run E2E tests:**
```bash
cd frontend && npm run test:e2e
# OR
cd frontend && npx playwright test
```

**Common E2E scenarios:**
- Login/logout flow
- Form submission and validation
- Data CRUD operations
- Navigation and routing
- Error handling and feedback

### Step 5: Verify Database Migrations

When model changes are detected:

```bash
cd backend

# Verify migration chain
python ../.gemini/skills/database/scripts/verify_migrations.py .

# Check for pending migrations
python manage.py makemigrations --check --dry-run

# Test migration forward/backward
python manage.py migrate
python manage.py migrate app_name previous_migration
python manage.py migrate
```

### Step 6: Generate Test Report

**Report format:**
```
TEST RESULTS
==================================================

Frontend:
----------------------------------------
  [PASS] Unit Tests (15 passed, 0 failed) - 12.3s
  [PASS] Integration Tests (5 passed, 0 failed) - 8.1s
  [SKIP] E2E Tests (no changes to pages)

Backend:
----------------------------------------
  [PASS] Unit Tests (22 passed, 0 failed) - 5.2s
  [PASS] Integration Tests (8 passed, 0 failed) - 4.8s
  [PASS] Migration Verification - 2.1s

Coverage:
----------------------------------------
  Frontend: 78% (statements)
  Backend: 85% (statements)

==================================================
ALL TESTS PASSED - Ready for /gitops
```

## Quick Commands

### Run All Tests

```bash
# Frontend
cd frontend && npm run test

# Backend
cd backend && pytest

# E2E
cd frontend && npm run test:e2e
```

### Run Specific Tests

```bash
# Frontend component
cd frontend && npm run test -- --testPathPattern="Button"

# Backend app
cd backend && pytest apps/academy/

# Single E2E test
cd frontend && npx playwright test login.spec.ts
```

### Coverage Reports

```bash
# Frontend
cd frontend && npm run test -- --coverage

# Backend
cd backend && pytest --cov=apps --cov-report=html
```

## Integration with Other Skills

### /build (Runs Before /test)

/build runs lint and compilation checks. /test assumes these pass:
1. Run `/build` - Verify code compiles
2. Run `/test` - Verify behavior is correct
3. Proceed to `/gitops` or `/csea-push`

### /database (For Migration Testing)

When models change, use database skill tools:
```bash
python ../.gemini/skills/database/scripts/verify_migrations.py .
```

### /gitops and /csea-push (Run After /test)

After all tests pass:
- `/gitops` - Commit and push changes
- `/csea-push` - Full deployment workflow

## Test Writing Guidelines

### Frontend Unit Tests

```typescript
// ComponentName.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { ComponentName } from './ComponentName';

describe('ComponentName', () => {
  it('renders correctly', () => {
    render(<ComponentName />);
    expect(screen.getByText('Expected Text')).toBeInTheDocument();
  });

  it('handles user interaction', async () => {
    render(<ComponentName />);
    await fireEvent.click(screen.getByRole('button'));
    expect(screen.getByText('Updated Text')).toBeInTheDocument();
  });
});
```

### Backend API Tests

```python
# tests/test_api.py
import pytest
from django.test import Client
from apps.academy.models import Course

@pytest.mark.django_db
class TestCourseAPI:
    def test_list_courses(self, client: Client, auth_headers):
        response = client.get('/api/courses/', **auth_headers)
        assert response.status_code == 200
        assert 'items' in response.json()

    def test_create_course(self, client: Client, auth_headers, course_data):
        response = client.post('/api/courses/', course_data, **auth_headers)
        assert response.status_code == 201
        assert Course.objects.filter(title=course_data['title']).exists()
```

### E2E Tests

```typescript
// e2e/course-management.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Course Management', () => {
  test('admin can create a course', async ({ page }) => {
    await page.goto('/academy/admin/courses');
    await page.click('button:has-text("New Course")');
    await page.fill('input[name="title"]', 'Test Course');
    await page.click('button:has-text("Save")');
    await expect(page.getByText('Test Course')).toBeVisible();
  });
});
```

## References

See [references/test-patterns.md](references/test-patterns.md) for:
- Complete test file templates
- Mocking patterns
- Fixture examples
- Coverage configuration

## Constraints

- All tests must pass before `/gitops`
- Never skip failing tests (fix them first)
- Use `/debugger` for complex test failures
- E2E tests require dev server running
- Migration tests should verify both forward and backward
- Coverage thresholds: Frontend 70%, Backend 80%
