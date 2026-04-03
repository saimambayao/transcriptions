# Code Quality Pattern Detection

Pattern detection rules for code quality issues in OBCMS.

## DRY Violations

**Severity**: Medium

### Pattern: Duplicate Code Blocks

**Detection**: Look for identical or near-identical code blocks (>5 lines) in multiple locations.

**Example Violation**:
```python
# File1
def list_tasks(request):
    tasks = Task.objects.filter(organization=request.user.organization)
    return render(request, 'tasks.html', {'tasks': tasks})

# File2
def list_assignments(request):
    assignments = Assignment.objects.filter(organization=request.user.organization)
    return render(request, 'assignments.html', {'assignments': assignments})
```

**Remediation**: Extract to shared utility or mixin:
```python
class OrganizationScopedMixin:
    def get_queryset(self):
        return super().get_queryset().filter(
            organization=self.request.user.organization
        )
```

---

## Complexity Issues

**Severity**: Medium

### Pattern: High Cyclomatic Complexity

**Detection**: Functions with >10 decision points (if/for/while/and/or).

**Threshold**: Complexity > 10 warrants refactoring.

**Example Violation**:
```python
def complex_function(data):
    if data:
        if data.type == 'A':
            if data.status == 'active':
                # ... 20 more nested ifs
```

**Remediation**: Break into smaller functions, use early returns, extract validators.

---

## Naming Conventions

**Severity**: Low

### OBCMS Naming Standards

- **Models**: PascalCase (`Task`, `Community`)
- **Functions/variables**: snake_case (`get_tasks`, `user_role`)
- **Constants**: UPPER_SNAKE_CASE (`MAX_UPLOAD_SIZE`)
- **Classes**: PascalCase (`TaskManager`, `OrganizationMixin`)
- **Template files**: snake_case.html (`task_list.html`)

**Detection Pattern**:
```python
# ❌ Wrong
def GetTasks():  # Should be snake_case
    pass

taskList = []  # Should be snake_case

# ✅ Correct
def get_tasks():
    pass

task_list = []
```

---

## Documentation Requirements

**Severity**: Medium

### Pattern: Missing Docstrings

**Detection**: Public functions/classes without docstrings.

**Example Violation**:
```python
# ❌ Missing docstring
def calculate_budget_total(items):
    return sum(item.amount for item in items)
```

**Remediation**:
```python
# ✅ Has docstring
def calculate_budget_total(items):
    """
    Calculate total budget amount from budget items.

    Args:
        items: QuerySet of BudgetItem instances

    Returns:
        Decimal: Total budget amount
    """
    return sum(item.amount for item in items)
```

---

## Dead Code Detection

**Severity**: Low

### Pattern 1: Unused Imports

**Detection**:
```python
import os  # Never used in file
from django.db import models
```

### Pattern 2: Unreachable Code

**Detection**:
```python
def process():
    return True
    print("Never executes")  # Dead code
```

### Pattern 3: Commented Out Code

**Detection**: Large blocks of commented code (>10 lines) without explanation.

---

## Testing Standards

**Severity**: Medium

### Pattern: Low Test Coverage

**Detection**: Files with <80% test coverage.

**Required Tests**:
- Models: Field validation, methods, managers
- Views: GET/POST, permissions, org filtering
- APIs: CRUD operations, authentication, serialization
- Forms: Validation, org-scoped querysets

**Example**:
```python
# tests/test_models.py
class TaskModelTest(TestCase):
    def test_organization_scoped_manager(self):
        """Verify tasks are filtered by organization"""
        org1_task = Task.objects.create(organization=self.org1)
        org2_task = Task.objects.create(organization=self.org2)

        org1_tasks = Task.objects.filter(organization=self.org1)
        self.assertIn(org1_task, org1_tasks)
        self.assertNotIn(org2_task, org1_tasks)
```

---

## Audit Checklist

- [ ] No duplicate code blocks (>5 lines)
- [ ] Function complexity < 10
- [ ] Consistent naming conventions
- [ ] Public functions have docstrings
- [ ] No unused imports
- [ ] No unreachable code
- [ ] Test coverage > 80%
- [ ] All models tested
- [ ] All views tested
- [ ] All APIs tested
