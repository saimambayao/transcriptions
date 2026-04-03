---
name: backend
description: Django backend development patterns for Bangsamoro Development Platform including models, Django Ninja APIs, authentication, authorization, and testing. Use when working with Django, creating REST APIs with Django Ninja, designing database models, implementing authentication/authorization, or any Django backend development tasks. Integrates with /database for schema design and /security for auth patterns.
argument-hint: "[topic]"
---

# Backend Development - Bangsamoro Development Platform

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's backend development request              ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

Comprehensive guidance for Django backend development with Django Ninja API framework for the Bangsamoro multi-portal system.

## Tech Stack

**Framework:** Django 6.0 web framework providing the foundation for backend development.

**API Framework:** Django Ninja for building fast RESTful APIs with automatic OpenAPI documentation and Pydantic schema validation.

**Database:** PostgreSQL 18 as the primary relational database.

**Authentication:** JWT-based authentication for API access.

## When to Use This Skill

- Creating or modifying Django models
- Building REST API endpoints with Django Ninja
- Implementing authentication and authorization
- Designing service layers and business logic
- Writing backend tests
- Handling file uploads
- Implementing audit logging
- **Migrating mock data to real API endpoints**
- **Connecting frontend services to backend APIs**

## Reference Navigation

### Core Django Patterns

**Models and ORM** - Django model design patterns, field types, relationships, migrations. See [references/models.md](references/models.md) when creating models or optimizing queries.

**Django Ninja APIs** - Router patterns, schemas, responses, authentication. See [references/ninja-apis.md](references/ninja-apis.md) when building API endpoints.

### Security

**Authentication** - JWT authentication, token management. See [references/authentication.md](references/authentication.md) when implementing auth systems.

**Authorization** - Permission patterns, role-based access. See [references/authorization.md](references/authorization.md) when implementing access control.

### Testing

**Testing Patterns** - Django test patterns, fixtures, factories. See [references/testing.md](references/testing.md) when writing tests.

### Frontend Integration

**Mock to API Migration** - Complete workflow for replacing frontend mock data with real API endpoints. See [references/mock-to-api-migration.md](references/mock-to-api-migration.md) when migrating mock data to database-backed APIs.

## Quick Reference

### Project Structure

```
backend/
├── config/
│   ├── settings.py      # Django settings
│   ├── urls.py          # Root URL configuration
│   └── wsgi.py          # WSGI application
├── apps/
│   ├── core/            # Core app (Organization, User)
│   │   ├── models.py
│   │   ├── api.py
│   │   └── schemas.py
│   ├── cooperatives/    # Cooperatives management
│   ├── social_enterprises/
│   ├── products/
│   └── compliance/
├── requirements.txt
└── manage.py
```

### Django Ninja API Pattern

```python
# apps/cooperatives/api.py
from ninja import Router, Schema
from ninja.security import HttpBearer
from typing import List
from .models import Cooperative
from .schemas import CooperativeOut, CooperativeIn, CooperativeUpdate

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        from apps.core.services import validate_jwt_token
        user = validate_jwt_token(token)
        if user:
            return user
        return None

router = Router(auth=AuthBearer())

@router.get('/', response=List[CooperativeOut])
def list_cooperatives(request):
    """List all cooperatives for the current organization."""
    return Cooperative.objects.filter(
        organization=request.auth.organization,
        is_deleted=False
    ).select_related('organization')

@router.get('/{coop_id}', response=CooperativeOut)
def get_cooperative(request, coop_id: int):
    """Get a specific cooperative."""
    return Cooperative.objects.get(
        id=coop_id,
        organization=request.auth.organization,
        is_deleted=False
    )

@router.post('/', response=CooperativeOut)
def create_cooperative(request, payload: CooperativeIn):
    """Create a new cooperative."""
    return Cooperative.objects.create(
        **payload.dict(),
        organization=request.auth.organization,
        created_by=request.auth
    )

@router.put('/{coop_id}', response=CooperativeOut)
def update_cooperative(request, coop_id: int, payload: CooperativeUpdate):
    """Update a cooperative."""
    coop = Cooperative.objects.get(
        id=coop_id,
        organization=request.auth.organization
    )
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(coop, attr, value)
    coop.save()
    return coop

@router.delete('/{coop_id}')
def delete_cooperative(request, coop_id: int):
    """Soft delete a cooperative."""
    coop = Cooperative.objects.get(
        id=coop_id,
        organization=request.auth.organization
    )
    coop.soft_delete()
    return {'success': True}
```

### Pydantic Schema Pattern

```python
# apps/cooperatives/schemas.py
from ninja import Schema
from datetime import datetime
from typing import Optional

class CooperativeOut(Schema):
    id: int
    name: str
    shortname: str
    registration_number: str
    status: str
    address: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

class CooperativeIn(Schema):
    name: str
    registration_number: str
    shortname: Optional[str] = None
    address: Optional[str] = None

class CooperativeUpdate(Schema):
    name: Optional[str] = None
    address: Optional[str] = None
    status: Optional[str] = None
```

### Model with Audit Fields

```python
# apps/cooperatives/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class BaseModel(models.Model):
    """Base model with audit and soft delete fields."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(class)s_created',
        null=True
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(class)s_updated',
        null=True
    )

    # Soft delete
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

class Cooperative(BaseModel):
    """Cooperative entity with multi-tenant support."""

    organization = models.ForeignKey(
        'core.Organization',
        on_delete=models.CASCADE,
        related_name='cooperatives'
    )
    name = models.CharField(max_length=255)
    shortname = models.SlugField(max_length=50, unique=True)
    registration_number = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('active', 'Active'),
            ('suspended', 'Suspended'),
        ],
        default='pending'
    )
    address = models.TextField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['organization']),
            models.Index(fields=['status']),
            models.Index(fields=['shortname']),
        ]

    def __str__(self):
        return self.name
```

### URL Configuration

```python
# config/urls.py
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from apps.core.api import router as core_router
from apps.cooperatives.api import router as cooperatives_router
from apps.social_enterprises.api import router as se_router
from apps.products.api import router as products_router

api = NinjaAPI(
    title="CSEA API",
    version="1.0.0",
    description="API for Bangsamoro Development Platform"
)

api.add_router('/auth/', core_router, tags=['Authentication'])
api.add_router('/cooperatives/', cooperatives_router, tags=['Cooperatives'])
api.add_router('/social-enterprises/', se_router, tags=['Social Enterprises'])
api.add_router('/products/', products_router, tags=['Products'])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
```

### Permission Checking

```python
# apps/core/permissions.py
from functools import wraps
from ninja.errors import HttpError

def require_role(*roles):
    """Decorator to require specific roles."""
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if not hasattr(request, 'auth') or not request.auth:
                raise HttpError(401, "Authentication required")
            if request.auth.role not in roles:
                raise HttpError(403, "Permission denied")
            return func(request, *args, **kwargs)
        return wrapper
    return decorator

# Usage in api.py
@router.post('/approve/{coop_id}')
@require_role('csea_staff', 'admin')
def approve_cooperative(request, coop_id: int):
    """Approve a cooperative registration (CSEA staff only)."""
    coop = Cooperative.objects.get(id=coop_id)
    coop.status = 'active'
    coop.save()
    return {'success': True}
```

### Service Layer Pattern

```python
# apps/cooperatives/services.py
from django.db import transaction
from .models import Cooperative, Member

class CooperativeService:
    @staticmethod
    @transaction.atomic
    def register_cooperative(data: dict, user) -> Cooperative:
        """Register a new cooperative with initial setup."""
        coop = Cooperative.objects.create(
            **data,
            organization=user.organization,
            created_by=user,
            status='pending'
        )

        # Create initial admin member
        Member.objects.create(
            cooperative=coop,
            user=user,
            role='admin',
            created_by=user
        )

        return coop

    @staticmethod
    def get_cooperative_stats(coop: Cooperative) -> dict:
        """Get statistics for a cooperative."""
        return {
            'total_members': coop.members.count(),
            'active_products': coop.products.filter(is_active=True).count(),
            'total_orders': coop.orders.count(),
        }
```

### Testing Pattern

```python
# apps/cooperatives/tests/test_api.py
from django.test import TestCase
from ninja.testing import TestClient
from apps.cooperatives.api import router
from apps.core.models import Organization, User

class CooperativeAPITests(TestCase):
    def setUp(self):
        self.client = TestClient(router)
        self.org = Organization.objects.create(name='Test Org')
        self.user = User.objects.create_user(
            username='test',
            organization=self.org
        )

    def test_list_cooperatives(self):
        response = self.client.get('/', user=self.user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_create_cooperative(self):
        response = self.client.post('/', json={
            'name': 'Test Coop',
            'registration_number': 'REG-001'
        }, user=self.user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Test Coop')

    def test_organization_isolation(self):
        """Test that users can't see other organizations' data."""
        other_org = Organization.objects.create(name='Other Org')
        Cooperative.objects.create(
            name='Other Coop',
            organization=other_org,
            registration_number='REG-002'
        )

        response = self.client.get('/', user=self.user)
        self.assertEqual(len(response.json()), 0)  # Can't see other org's coop
```

## CSEA-Specific Patterns

### Portal-Specific Endpoints

```python
# Public endpoints (no auth)
@router.get('/public/cooperatives', auth=None)
def list_public_cooperatives(request):
    """Public directory of active cooperatives."""
    return Cooperative.objects.filter(
        status='active',
        is_deleted=False
    ).values('id', 'name', 'shortname')

# Tenant endpoints (auth required)
@router.get('/cooperatives', auth=AuthBearer())
def list_my_cooperatives(request):
    """List cooperatives for current organization."""
    return Cooperative.objects.filter(
        organization=request.auth.organization
    )

# Admin endpoints (role required)
@router.get('/admin/cooperatives', auth=AuthBearer())
@require_role('csea_staff', 'admin')
def list_all_cooperatives(request):
    """Admin view of all cooperatives."""
    return Cooperative.objects.all()
```

### Multi-Tenant Enforcement

```python
# ALWAYS include organization filter
def list_cooperatives(request):
    return Cooperative.objects.filter(
        organization=request.auth.organization  # REQUIRED
    )

# ALWAYS set organization on create
def create_cooperative(request, payload):
    return Cooperative.objects.create(
        **payload.dict(),
        organization=request.auth.organization  # REQUIRED
    )
```

## Common Patterns

| Pattern | When to Use |
|---------|-------------|
| Service Layer | Complex business logic |
| Soft Delete | Audit trail, data recovery |
| Pydantic Schemas | API request/response validation |
| Permission Decorators | Role-based access control |
| Transaction Atomic | Multi-step operations |

## Development Workflow

1. **Design model** with multi-tenant support
2. **Create migration** and test locally
3. **Define schemas** (In/Out/Update)
4. **Implement API router** with CRUD operations
5. **Add permissions** as needed
6. **Write tests** for API and business logic
7. **Document** API (auto-generated by Django Ninja)

## Mock to API Migration Workflow

See [mock-to-api-migration.md](references/mock-to-api-migration.md) for the complete migration guide with quick steps, patterns, type alignment, seed data, and testing connection.
