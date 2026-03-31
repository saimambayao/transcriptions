# Multi-Tenant Data Isolation

**Critical for OBCMS: Preventing Cross-Organization Data Leaks**

OBCMS is a multi-organizational system supporting OOBC and partner ministries. All data must be strictly isolated by organization to prevent unauthorized cross-organization access.

## Table of Contents

1. [Organization-Based Architecture](#organization-based-architecture)
2. [QuerySet Filtering Patterns](#queryset-filtering-patterns)
3. [View-Level Isolation](#view-level-isolation)
4. [API Endpoint Isolation](#api-endpoint-isolation)
5. [Form Validation](#form-validation)
6. [Common Pitfalls](#common-pitfalls)
7. [Testing Data Isolation](#testing-data-isolation)

## Organization-Based Architecture

### User-Organization Relationship

Every user belongs to one organization:

```python
# common/models.py
class User(AbstractUser):
    organization = models.ForeignKey(
        'Organization',
        on_delete=models.PROTECT,
        related_name='users'
    )
```

### Organization-Scoped Models

Most models in OBCMS are organization-scoped:

```python
# Example: Task model
class Task(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_tasks')
```

### Organization Model

```python
# common/models.py
class Organization(models.Model):
    name = models.CharField(max_length=200)
    org_type = models.CharField(max_length=50)  # 'oobc', 'ministry', etc.
    is_active = models.BooleanField(default=True)
```

## QuerySet Filtering Patterns

**Golden Rule:** Always filter by `request.user.organization` unless explicitly working with cross-organization data (rare cases that require special approval).

### Basic Filtering

```python
# ✅ CORRECT - Filter by user's organization
def list_tasks(request):
    tasks = Task.objects.filter(organization=request.user.organization)
    return render(request, 'tasks/list.html', {'tasks': tasks})

# ❌ WRONG - No organization filter
def list_tasks_bad(request):
    tasks = Task.objects.all()  # LEAKS DATA FROM ALL ORGANIZATIONS!
    return render(request, 'tasks/list.html', {'tasks': tasks})
```

### Related Object Filtering

```python
# ✅ CORRECT - Filter through relationships
def list_community_assessments(request):
    assessments = Assessment.objects.filter(
        community__organization=request.user.organization
    )
    return render(request, 'assessments/list.html', {'assessments': assessments})

# ✅ CORRECT - Multiple related filters
def list_task_comments(request):
    comments = Comment.objects.filter(
        task__organization=request.user.organization
    )
```

### Aggregation Queries

```python
from django.db.models import Count, Sum

# ✅ CORRECT - Aggregation with organization filter
def dashboard_stats(request):
    org = request.user.organization

    stats = {
        'total_tasks': Task.objects.filter(organization=org).count(),
        'completed_tasks': Task.objects.filter(
            organization=org,
            status='completed'
        ).count(),
        'total_budget': BudgetItem.objects.filter(
            organization=org
        ).aggregate(total=Sum('amount'))['total']
    }
    return render(request, 'dashboard.html', stats)
```

### Custom Managers for Organization Filtering

```python
# ✅ BEST PRACTICE - Custom manager for automatic filtering
class OrganizationQuerySet(models.QuerySet):
    def for_organization(self, organization):
        return self.filter(organization=organization)

class TaskManager(models.Manager):
    def get_queryset(self):
        return OrganizationQuerySet(self.model, using=self._db)

class Task(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    # ... other fields ...

    objects = TaskManager()

# Usage in views
def list_tasks(request):
    tasks = Task.objects.for_organization(request.user.organization)
```

## View-Level Isolation

### Function-Based Views

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def task_detail(request, task_id):
    # ✅ CORRECT - Verify task belongs to user's organization
    task = get_object_or_404(
        Task,
        id=task_id,
        organization=request.user.organization
    )
    return render(request, 'tasks/detail.html', {'task': task})

# ❌ WRONG - No organization check
@login_required
def task_detail_bad(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # DATA LEAK!
    return render(request, 'tasks/detail.html', {'task': task})
```

### Class-Based Views

```python
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/list.html'

    def get_queryset(self):
        # ✅ CORRECT - Filter by organization
        return Task.objects.filter(
            organization=self.request.user.organization
        )

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'

    def get_queryset(self):
        # ✅ CORRECT - Filter by organization
        return Task.objects.filter(
            organization=self.request.user.organization
        )
```

### Create Views with Auto-Assignment

```python
from django.views.generic.edit import CreateView

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'assigned_to']
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        # ✅ CORRECT - Auto-assign organization
        form.instance.organization = self.request.user.organization
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # ✅ CORRECT - Limit assigned_to to users in same organization
        form.fields['assigned_to'].queryset = User.objects.filter(
            organization=self.request.user.organization
        )
        return form
```

## API Endpoint Isolation

### Django REST Framework ViewSets

```python
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # ✅ CORRECT - Filter by organization
        return Task.objects.filter(
            organization=self.request.user.organization
        )

    def perform_create(self, serializer):
        # ✅ CORRECT - Auto-assign organization
        serializer.save(
            organization=self.request.user.organization,
            created_by=self.request.user
        )
```

### API Views with Manual Filtering

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_task_list(request):
    # ✅ CORRECT - Filter by organization
    tasks = Task.objects.filter(organization=request.user.organization)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_task_detail(request, task_id):
    # ✅ CORRECT - Verify organization ownership
    try:
        task = Task.objects.get(
            id=task_id,
            organization=request.user.organization
        )
    except Task.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    serializer = TaskSerializer(task)
    return Response(serializer.data)
```

### Serializer Validation

```python
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_to']

    def validate_assigned_to(self, value):
        # ✅ CORRECT - Ensure assigned user is in same organization
        request = self.context.get('request')
        if value and value.organization != request.user.organization:
            raise serializers.ValidationError(
                "Cannot assign task to user from different organization"
            )
        return value
```

## Form Validation

### ModelForm with Organization Validation

```python
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ✅ CORRECT - Limit choices to same organization
        self.fields['assigned_to'].queryset = User.objects.filter(
            organization=user.organization
        )
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit=False)
        # ✅ CORRECT - Auto-assign organization
        instance.organization = self.user.organization
        if commit:
            instance.save()
        return instance

# Usage in view
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:list')
    else:
        form = TaskForm(user=request.user)
    return render(request, 'tasks/create.html', {'form': form})
```

### ForeignKey Choice Validation

```python
class AssignmentForm(forms.Form):
    task = forms.ModelChoiceField(queryset=Task.objects.none())
    assigned_to = forms.ModelChoiceField(queryset=User.objects.none())

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ✅ CORRECT - Limit all choices to user's organization
        self.fields['task'].queryset = Task.objects.filter(
            organization=user.organization
        )
        self.fields['assigned_to'].queryset = User.objects.filter(
            organization=user.organization
        )
```

## Common Pitfalls

### Pitfall 1: Global Queries

```python
# ❌ WRONG - Queries all organizations
tasks = Task.objects.all()

# ✅ CORRECT
tasks = Task.objects.filter(organization=request.user.organization)
```

### Pitfall 2: Missing Organization Filter in get_object_or_404

```python
# ❌ WRONG - No organization check
task = get_object_or_404(Task, id=task_id)

# ✅ CORRECT
task = get_object_or_404(Task, id=task_id, organization=request.user.organization)
```

### Pitfall 3: Related Object Access Without Verification

```python
# ❌ WRONG - Accessing related object without org check
def view_task_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    # If comment.task is from another org, DATA LEAK!
    return render(request, 'comment.html', {'comment': comment})

# ✅ CORRECT - Verify through relationship
def view_task_comment(request, comment_id):
    comment = get_object_or_404(
        Comment,
        id=comment_id,
        task__organization=request.user.organization
    )
    return render(request, 'comment.html', {'comment': comment})
```

### Pitfall 4: Foreign Key Choices Not Limited

```python
# ❌ WRONG - Shows all users across all organizations
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['assigned_to']
    # No __init__ to filter queryset - LEAKS USER LIST!

# ✅ CORRECT - Limit to same organization
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['assigned_to']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(
            organization=user.organization
        )
```

### Pitfall 5: Admin Interface Without Organization Filter

```python
# ❌ WRONG - Shows all tasks to all users
from django.contrib import admin

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization']
    # No get_queryset override - SHOWS ALL ORGS!

# ✅ CORRECT - Filter by user's organization
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(organization=request.user.organization)
```

### Pitfall 6: Raw SQL Queries

```python
# ❌ WRONG - Raw SQL without org filter
from django.db import connection

def get_tasks_raw():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM tasks")
        return cursor.fetchall()
    # LEAKS DATA FROM ALL ORGANIZATIONS!

# ✅ CORRECT - Parameterized query with org filter
def get_tasks_raw(organization_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM tasks WHERE organization_id = %s",
            [organization_id]
        )
        return cursor.fetchall()
```

## Testing Data Isolation

### Unit Tests for Data Isolation

```python
from django.test import TestCase, Client
from common.models import Organization, User
from tasks.models import Task

class DataIsolationTest(TestCase):
    def setUp(self):
        # Create two organizations
        self.org1 = Organization.objects.create(name="OOBC")
        self.org2 = Organization.objects.create(name="Ministry of Health")

        # Create users in different organizations
        self.user1 = User.objects.create_user(
            username='user1',
            password='pass',
            organization=self.org1
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='pass',
            organization=self.org2
        )

        # Create tasks for different organizations
        self.task1 = Task.objects.create(
            title="Task 1",
            organization=self.org1
        )
        self.task2 = Task.objects.create(
            title="Task 2",
            organization=self.org2
        )

    def test_user_cannot_view_other_org_tasks(self):
        """User from org1 should not see org2 tasks"""
        self.client.login(username='user1', password='pass')
        response = self.client.get('/tasks/')

        # Should see own organization's task
        self.assertContains(response, "Task 1")
        # Should NOT see other organization's task
        self.assertNotContains(response, "Task 2")

    def test_user_cannot_access_other_org_task_detail(self):
        """User from org1 should not access org2 task detail"""
        self.client.login(username='user1', password='pass')
        response = self.client.get(f'/tasks/{self.task2.id}/')

        # Should return 404, not the task
        self.assertEqual(response.status_code, 404)

    def test_api_filters_by_organization(self):
        """API should only return tasks from user's organization"""
        self.client.login(username='user1', password='pass')
        response = self.client.get('/api/tasks/')

        self.assertEqual(response.status_code, 200)
        data = response.json()

        # Should only have 1 task (from org1)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], "Task 1")

    def test_form_limits_choices_to_organization(self):
        """Form choices should be limited to same organization"""
        from tasks.forms import TaskForm

        # User1's form should only show org1 users
        form = TaskForm(user=self.user1)
        assigned_to_choices = list(form.fields['assigned_to'].queryset)

        self.assertIn(self.user1, assigned_to_choices)
        self.assertNotIn(self.user2, assigned_to_choices)
```

### Integration Tests

```python
class CrossOrganizationAccessTest(TestCase):
    """Test that cross-organization access is properly blocked"""

    def test_cannot_update_other_org_task(self):
        """User cannot update task from different organization"""
        # Setup (same as above)
        self.client.login(username='user1', password='pass')

        response = self.client.post(f'/tasks/{self.task2.id}/edit/', {
            'title': 'Hacked Task',
            'description': 'Should not work'
        })

        # Should be 404 or 403
        self.assertIn(response.status_code, [403, 404])

        # Task should remain unchanged
        self.task2.refresh_from_db()
        self.assertEqual(self.task2.title, "Task 2")

    def test_cannot_delete_other_org_task(self):
        """User cannot delete task from different organization"""
        self.client.login(username='user1', password='pass')

        response = self.client.post(f'/tasks/{self.task2.id}/delete/')

        # Should be 404 or 403
        self.assertIn(response.status_code, [403, 404])

        # Task should still exist
        self.assertTrue(Task.objects.filter(id=self.task2.id).exists())
```

## Data Isolation Checklist

Use this checklist when implementing any view, API endpoint, or form:

- [ ] All queries filter by `request.user.organization`
- [ ] `get_object_or_404()` includes `organization=request.user.organization`
- [ ] Class-based views override `get_queryset()` with organization filter
- [ ] Create views auto-assign `organization=request.user.organization`
- [ ] Forms limit `ForeignKey` choices to same organization
- [ ] API ViewSets filter `get_queryset()` by organization
- [ ] Serializers validate related objects are from same organization
- [ ] Admin interface filters by organization (unless superuser)
- [ ] Raw SQL queries include organization_id filter
- [ ] Related object access verifies organization through relationships
- [ ] Tests verify cross-organization access is blocked
- [ ] Tests verify queries return only same-organization data

## Organization-Scoped Utilities

```python
# common/utils.py

def get_organization_queryset(model, organization):
    """
    Get queryset filtered by organization.

    Args:
        model: Django model class
        organization: Organization instance

    Returns:
        QuerySet filtered by organization
    """
    return model.objects.filter(organization=organization)

def verify_organization_access(obj, user):
    """
    Verify user has access to object based on organization.

    Args:
        obj: Model instance with organization field
        user: User instance

    Returns:
        bool: True if user can access object

    Raises:
        PermissionDenied: If user cannot access object
    """
    from django.core.exceptions import PermissionDenied

    if not hasattr(obj, 'organization'):
        raise ValueError(f"{obj.__class__.__name__} has no organization field")

    if obj.organization != user.organization:
        raise PermissionDenied("Cannot access resource from different organization")

    return True
```

## Resources

- OBCMS GEMINI.md: Database rules and multi-tenant patterns
- Django QuerySet API: https://docs.djangoproject.com/en/5.2/ref/models/querysets/
- Django Row-Level Security: https://docs.djangoproject.com/en/5.2/topics/db/queries/#complex-queries
