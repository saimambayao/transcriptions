# OBCMS Common Conventions

**Purpose**: Naming conventions, file organization, code style, and project standards.

---

## Naming Conventions

### Apps
- **Format**: Lowercase, singular
- **Examples**: `community` (not `communities`), `planning`, `coordination`

### Models
- **Format**: PascalCase, singular
- **Examples**: `Task`, `Community`, `ResourceBooking`

### Views
- **Format**: snake_case, descriptive
- **Examples**: `list_tasks`, `create_booking`, `delete_community`

### Templates
- **Format**: snake_case
- **Examples**: `task_list.html`, `booking_form.html`, `community_detail.html`

### URLs
- **Format**: kebab-case
- **Examples**: `/resource-bookings/`, `/mana-assessments/`, `/coordination-meetings/`

### Variables
- **Format**: snake_case
- **Examples**: `community_count`, `user_organization`, `assessment_score`

### Constants
- **Format**: UPPER_SNAKE_CASE
- **Examples**: `MAX_UPLOAD_SIZE`, `DEFAULT_PAGINATION`, `MANA_SECTORS`

---

## File Organization

### Django App Structure
```
my_app/
├── __init__.py
├── models.py              # All models
├── views.py               # Views (or views/ for large apps)
├── serializers.py         # DRF serializers
├── urls.py                # URL patterns
├── admin.py               # Django admin
├── forms.py               # Django forms
├── tasks.py               # Celery tasks
├── permissions.py         # Custom permissions
├── managers.py            # Custom model managers
├── tests/                 # All tests
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_views.py
│   └── test_api.py
├── templates/my_app/      # App templates
└── migrations/            # Database migrations
```

### Template Organization
```
templates/
├── base.html              # Base template
├── my_app/                # App-specific templates
│   ├── my_model_list.html
│   ├── my_model_form.html
│   └── my_model_detail.html
├── common/                # Shared components
│   ├── navbar.html
│   └── footer.html
└── components/            # Reusable UI components
    ├── stat_card.html
    └── modal.html
```

---

## Code Style

### Formatting
- **Tool**: Black
- **Line Length**: 88 characters
- **Run**: `black src/`

### Import Sorting
- **Tool**: isort
- **Run**: `isort src/`

### Import Order
```python
# 1. Standard library
import os
from datetime import datetime

# 2. Third-party
from django.db import models
from rest_framework import viewsets

# 3. Local
from common.models import BaseModel
from .serializers import TaskSerializer
```

### Docstrings
- **Style**: Google format
```python
def list_tasks(request):
    """List all tasks for the current user's organization.

    Args:
        request: Django HTTP request object

    Returns:
        HttpResponse with rendered task list template
    """
    tasks = Task.objects.filter(organization=request.user.organization)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
```

### Type Hints (Encouraged)
```python
from typing import List
from django.http import HttpRequest, HttpResponse

def list_tasks(request: HttpRequest) -> HttpResponse:
    ...
```

---

## Django Conventions

### Model Fields
```python
class Community(BaseModel):
    # CharField: Always specify max_length
    name = models.CharField(max_length=255)

    # ForeignKey: Use on_delete
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)

    # DateTimeField: Use auto_now_add for created, auto_now for modified
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # BooleanField: Provide default
    is_active = models.BooleanField(default=True)
```

### View Patterns
```python
# Function-Based View
def list_items(request):
    items = Item.objects.filter(organization=request.user.organization)
    return render(request, 'app/list.html', {'items': items})

# Class-Based View
class ItemListView(ListView):
    model = Item
    template_name = 'app/list.html'

    def get_queryset(self):
        return Item.objects.filter(organization=self.request.user.organization)
```

---

## Git Conventions

### Branch Names
- `main`: Production
- `staging`: Staging environment
- `feature/feature-name`: Feature branches
- `bugfix/bug-description`: Bug fixes

### Commit Messages
```
Feature: Add resource booking calendar

- Implement ResourceBooking model
- Create booking API endpoints
- Build FullCalendar UI
- Add organization filtering

🤖 Generated with Gemini CLI
Co-Authored-By: Claude <noreply@anthropic.com>
```

---

## Testing Conventions

### Test File Names
```
tests/
├── test_models.py         # Model tests
├── test_views.py          # View tests
├── test_api.py            # API tests
└── test_permissions.py    # Permission tests
```

### Test Method Names
```python
def test_community_creation(self):
    """Test creating a community"""

def test_organization_isolation(self):
    """Test users can't see other organizations' data"""

def test_permission_required(self):
    """Test view requires proper permission"""
```

---

**Remember**: Consistency matters. Follow these conventions to maintain codebase quality.
