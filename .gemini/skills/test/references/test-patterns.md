# Test Patterns Reference - Bangsamoro Development Platform

Comprehensive testing patterns, templates, and best practices for the Bangsamoro multi-portal system.

## Table of Contents

1. [Frontend Testing Patterns](#frontend-testing-patterns)
2. [Backend Testing Patterns](#backend-testing-patterns)
3. [E2E Testing Patterns](#e2e-testing-patterns)
4. [Mocking Patterns](#mocking-patterns)
5. [Fixtures and Test Data](#fixtures-and-test-data)
6. [Coverage Configuration](#coverage-configuration)

## Frontend Testing Patterns

### React Component Tests

```typescript
// Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Button } from './Button';

describe('Button', () => {
  it('renders with correct text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole('button', { name: /click me/i })).toBeInTheDocument();
  });

  it('calls onClick when clicked', async () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Submit</Button>);

    await userEvent.click(screen.getByRole('button'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('is disabled when disabled prop is true', () => {
    render(<Button disabled>Disabled</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
  });

  it('shows loading state', () => {
    render(<Button loading>Loading</Button>);
    expect(screen.getByRole('button')).toHaveAttribute('aria-busy', 'true');
  });
});
```

### Hook Tests

```typescript
// useCounter.test.ts
import { renderHook, act } from '@testing-library/react';
import { useCounter } from './useCounter';

describe('useCounter', () => {
  it('starts with initial value', () => {
    const { result } = renderHook(() => useCounter(5));
    expect(result.current.count).toBe(5);
  });

  it('increments count', () => {
    const { result } = renderHook(() => useCounter(0));

    act(() => {
      result.current.increment();
    });

    expect(result.current.count).toBe(1);
  });

  it('decrements count', () => {
    const { result } = renderHook(() => useCounter(5));

    act(() => {
      result.current.decrement();
    });

    expect(result.current.count).toBe(4);
  });
});
```

### TanStack Query Hook Tests

```typescript
// useCourses.test.ts
import { renderHook, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { useCourses } from './useCourses';

const createWrapper = () => {
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: { retry: false },
    },
  });
  return ({ children }: { children: React.ReactNode }) => (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  );
};

describe('useCourses', () => {
  it('fetches courses successfully', async () => {
    const { result } = renderHook(() => useCourses(), {
      wrapper: createWrapper(),
    });

    await waitFor(() => {
      expect(result.current.isSuccess).toBe(true);
    });

    expect(result.current.data).toBeDefined();
    expect(result.current.data?.items).toBeInstanceOf(Array);
  });
});
```

### Service Layer Tests

```typescript
// academy.service.test.ts
import { academyService } from './academy.service';

// Mock fetch globally
global.fetch = jest.fn();

describe('academyService', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('getCourses', () => {
    it('fetches courses with correct URL', async () => {
      (fetch as jest.Mock).mockResolvedValueOnce({
        ok: true,
        json: () => Promise.resolve({ items: [], total: 0 }),
      });

      await academyService.getCourses({ page: 1, limit: 10 });

      expect(fetch).toHaveBeenCalledWith(
        expect.stringContaining('/api/academy/courses'),
        expect.any(Object)
      );
    });

    it('throws error on failed request', async () => {
      (fetch as jest.Mock).mockResolvedValueOnce({
        ok: false,
        status: 500,
      });

      await expect(academyService.getCourses({})).rejects.toThrow();
    });
  });
});
```

## Backend Testing Patterns

### Model Tests

```python
# tests/test_models.py
import pytest
from django.utils import timezone
from apps.academy.models import Course, Category

@pytest.mark.django_db
class TestCourseModel:
    def test_create_course(self, organization):
        """Test course creation with required fields."""
        course = Course.objects.create(
            organization=organization,
            title="Test Course",
            slug="test-course",
            description="A test course",
            status="draft"
        )
        assert course.id is not None
        assert course.title == "Test Course"
        assert course.created_at is not None

    def test_course_str(self, organization):
        """Test course string representation."""
        course = Course.objects.create(
            organization=organization,
            title="Test Course",
            slug="test-course"
        )
        assert str(course) == "Test Course"

    def test_course_soft_delete(self, organization):
        """Test soft delete functionality."""
        course = Course.objects.create(
            organization=organization,
            title="Test Course",
            slug="test-course"
        )
        course.soft_delete()

        assert course.is_deleted is True
        assert course.deleted_at is not None

        # Should not appear in default queryset
        assert Course.objects.filter(id=course.id).count() == 0
        # Should appear in all_objects
        assert Course.all_objects.filter(id=course.id).count() == 1
```

### API Tests with Django Ninja

```python
# tests/test_api.py
import pytest
from django.test import Client
from apps.academy.models import Course

@pytest.fixture
def auth_headers(user_token):
    return {"HTTP_AUTHORIZATION": f"Bearer {user_token}"}

@pytest.fixture
def course_data():
    return {
        "title": "New Course",
        "slug": "new-course",
        "description": "Course description",
        "category_id": 1,
        "difficulty": "beginner",
        "duration_hours": 10
    }

@pytest.mark.django_db
class TestCourseAPI:
    def test_list_courses(self, client: Client, auth_headers, organization):
        """Test listing courses returns organization-scoped results."""
        # Create courses
        Course.objects.create(
            organization=organization,
            title="Course 1",
            slug="course-1"
        )
        Course.objects.create(
            organization=organization,
            title="Course 2",
            slug="course-2"
        )

        response = client.get("/api/academy/courses/", **auth_headers)

        assert response.status_code == 200
        data = response.json()
        assert "items" in data
        assert len(data["items"]) == 2

    def test_create_course(self, client: Client, auth_headers, course_data, category):
        """Test creating a new course."""
        course_data["category_id"] = category.id

        response = client.post(
            "/api/academy/courses/",
            data=course_data,
            content_type="application/json",
            **auth_headers
        )

        assert response.status_code == 201
        assert Course.objects.filter(title="New Course").exists()

    def test_update_course(self, client: Client, auth_headers, course):
        """Test updating an existing course."""
        response = client.patch(
            f"/api/academy/courses/{course.id}/",
            data={"title": "Updated Course"},
            content_type="application/json",
            **auth_headers
        )

        assert response.status_code == 200
        course.refresh_from_db()
        assert course.title == "Updated Course"

    def test_delete_course(self, client: Client, auth_headers, course):
        """Test deleting (soft delete) a course."""
        response = client.delete(
            f"/api/academy/courses/{course.id}/",
            **auth_headers
        )

        assert response.status_code == 204
        course.refresh_from_db()
        assert course.is_deleted is True

    def test_unauthorized_access(self, client: Client):
        """Test API requires authentication."""
        response = client.get("/api/academy/courses/")
        assert response.status_code == 401
```

### Fixture Examples (conftest.py)

```python
# conftest.py
import pytest
from django.contrib.auth import get_user_model
from apps.core.models import Organization
from apps.academy.models import Course, Category

User = get_user_model()

@pytest.fixture
def organization():
    """Create a test organization."""
    return Organization.objects.create(
        name="Test Organization",
        slug="test-org",
        type="cooperative"
    )

@pytest.fixture
def user(organization):
    """Create a test user with organization."""
    user = User.objects.create_user(
        email="test@example.com",
        password="testpass123"
    )
    user.organization = organization
    user.save()
    return user

@pytest.fixture
def admin_user(organization):
    """Create a test admin user."""
    return User.objects.create_superuser(
        email="admin@example.com",
        password="adminpass123"
    )

@pytest.fixture
def user_token(user):
    """Generate JWT token for test user."""
    from rest_framework_simplejwt.tokens import RefreshToken
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)

@pytest.fixture
def category(organization):
    """Create a test category."""
    return Category.objects.create(
        organization=organization,
        name="Test Category",
        slug="test-category"
    )

@pytest.fixture
def course(organization, category, user):
    """Create a test course."""
    return Course.objects.create(
        organization=organization,
        title="Test Course",
        slug="test-course",
        description="A test course",
        category=category,
        created_by=user
    )
```

## E2E Testing Patterns

### Page Object Pattern

```typescript
// e2e/pages/LoginPage.ts
import { Page } from '@playwright/test';

export class LoginPage {
  constructor(private page: Page) {}

  async goto() {
    await this.page.goto('/login');
  }

  async login(email: string, password: string) {
    await this.page.fill('input[name="email"]', email);
    await this.page.fill('input[name="password"]', password);
    await this.page.click('button[type="submit"]');
  }

  async expectError(message: string) {
    await expect(this.page.getByText(message)).toBeVisible();
  }
}
```

### Complete E2E Test

```typescript
// e2e/course-management.spec.ts
import { test, expect } from '@playwright/test';
import { LoginPage } from './pages/LoginPage';

test.describe('Course Management', () => {
  test.beforeEach(async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login('admin@example.com', 'password');
    await page.waitForURL('/academy/admin/dashboard');
  });

  test('admin can view course list', async ({ page }) => {
    await page.goto('/academy/admin/courses');

    await expect(page.getByRole('heading', { name: 'Courses' })).toBeVisible();
    await expect(page.getByRole('table')).toBeVisible();
  });

  test('admin can create a new course', async ({ page }) => {
    await page.goto('/academy/admin/courses');

    // Click new course button
    await page.click('button:has-text("New Course")');

    // Fill form
    await page.fill('input[name="title"]', 'E2E Test Course');
    await page.fill('textarea[name="description"]', 'Test description');
    await page.selectOption('select[name="category"]', 'business');
    await page.selectOption('select[name="difficulty"]', 'beginner');

    // Submit
    await page.click('button:has-text("Save")');

    // Verify success
    await expect(page.getByText('Course created successfully')).toBeVisible();
    await expect(page.getByText('E2E Test Course')).toBeVisible();
  });

  test('admin can edit a course', async ({ page }) => {
    await page.goto('/academy/admin/courses');

    // Click edit on first course
    await page.click('table tbody tr:first-child button[aria-label="Edit"]');

    // Modify title
    await page.fill('input[name="title"]', 'Updated Course Title');
    await page.click('button:has-text("Save")');

    // Verify update
    await expect(page.getByText('Course updated successfully')).toBeVisible();
    await expect(page.getByText('Updated Course Title')).toBeVisible();
  });

  test('admin can delete a course', async ({ page }) => {
    await page.goto('/academy/admin/courses');

    const courseName = await page.locator('table tbody tr:first-child td:first-child').textContent();

    // Click delete
    await page.click('table tbody tr:first-child button[aria-label="Delete"]');

    // Confirm deletion
    await page.click('button:has-text("Confirm")');

    // Verify deletion
    await expect(page.getByText('Course deleted successfully')).toBeVisible();
    await expect(page.getByText(courseName!)).not.toBeVisible();
  });
});
```

## Mocking Patterns

### MSW (Mock Service Worker) Setup

```typescript
// mocks/handlers.ts
import { rest } from 'msw';

export const handlers = [
  rest.get('/api/academy/courses', (req, res, ctx) => {
    return res(
      ctx.json({
        items: [
          { id: 1, title: 'Course 1', status: 'published' },
          { id: 2, title: 'Course 2', status: 'draft' },
        ],
        total: 2,
        page: 1,
        limit: 10,
      })
    );
  }),

  rest.post('/api/academy/courses', async (req, res, ctx) => {
    const body = await req.json();
    return res(
      ctx.status(201),
      ctx.json({ id: 3, ...body })
    );
  }),
];
```

### Django Test Mocking

```python
# tests/test_services.py
from unittest.mock import patch, MagicMock
import pytest

@pytest.mark.django_db
class TestExternalServiceIntegration:
    @patch('apps.academy.services.external_api.send_notification')
    def test_course_publish_sends_notification(self, mock_notify, course):
        """Test that publishing a course sends notification."""
        mock_notify.return_value = {"success": True}

        course.publish()

        mock_notify.assert_called_once_with(
            type="course_published",
            course_id=course.id
        )

    @patch('apps.academy.services.storage.upload_file')
    def test_upload_course_material(self, mock_upload, course):
        """Test uploading course material."""
        mock_upload.return_value = "https://storage.example.com/file.pdf"

        result = course.add_material(
            file=b"content",
            filename="lesson.pdf"
        )

        assert result.url == "https://storage.example.com/file.pdf"
        mock_upload.assert_called_once()
```

## Coverage Configuration

### Jest Coverage (frontend)

```javascript
// jest.config.js
module.exports = {
  collectCoverageFrom: [
    'src/**/*.{ts,tsx}',
    '!src/**/*.d.ts',
    '!src/**/*.test.{ts,tsx}',
    '!src/**/index.ts',
  ],
  coverageThreshold: {
    global: {
      branches: 70,
      functions: 70,
      lines: 70,
      statements: 70,
    },
  },
  coverageReporters: ['text', 'lcov', 'html'],
};
```

### Pytest Coverage (backend)

```ini
# pytest.ini
[pytest]
testpaths = apps
python_files = test_*.py
python_functions = test_*
addopts = --strict-markers -v

markers =
    integration: Integration tests
    slow: Slow running tests

# Coverage settings
[coverage:run]
source = apps
omit =
    */migrations/*
    */tests/*
    */__init__.py

[coverage:report]
fail_under = 80
show_missing = true
exclude_lines =
    pragma: no cover
    def __repr__
    raise NotImplementedError
```

### Playwright Configuration

```typescript
// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  timeout: 30000,
  retries: 2,
  workers: 4,
  reporter: [
    ['html', { outputFolder: 'playwright-report' }],
    ['junit', { outputFile: 'results.xml' }],
  ],
  use: {
    baseURL: 'http://localhost:3090',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { browserName: 'chromium' },
    },
  ],
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3090',
    reuseExistingServer: !process.env.CI,
  },
});
```
