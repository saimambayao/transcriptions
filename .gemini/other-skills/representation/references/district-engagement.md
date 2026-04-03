---
description: Django backend development with Django REST Framework APIs for e-Bangsamoro
---

# Backend Development Workflow

## Tech Stack
- Django 6.0 + Django REST Framework 3.16+ (API framework)
- PostgreSQL 18
- JWT authentication
- Celery 5.4+ (background tasks)
- Redis 8.4 (cache, sessions)

## When to Use
- Creating or modifying Django models
- Building REST API endpoints with DRF
- Implementing authentication and authorization
- Writing backend tests

## Project Structure
```
backend/
├── config/              # Django settings
│   └── settings/        # base.py, development.py, production.py
├── apps/
│   ├── accounts/        # User authentication, RBAC
│   ├── tenants/         # Multi-tenant management
│   ├── core/            # Shared utilities, mixins
│   ├── legislative/     # Bills, resolutions, committees
│   ├── oversight/       # MOA tracking, program monitoring
│   ├── representation/  # Constituent services
│   ├── ministerial/     # Strategic planning
│   ├── budget/          # BBSA (BAA No. 84)-compliant budgeting
│   ├── office/          # Staff, tasks, calendar
│   ├── ai/              # AI agent system (Google ADK)
│   └── realtime/        # WebSocket handlers
├── api/v1/              # API endpoints
└── manage.py
```

## Quick Reference

### DRF ViewSet Pattern
```python
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

class CommitteeViewSet(viewsets.ModelViewSet):
    serializer_class = CommitteeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Committee.objects.filter(
            tenant=self.request.user.tenant,  # REQUIRED
            is_deleted=False
        )

    def perform_create(self, serializer):
        serializer.save(
            tenant=self.request.user.tenant,  # REQUIRED
            created_by=self.request.user
        )

    @action(detail=True, methods=['post'])
    def assign_members(self, request, pk=None):
        committee = self.get_object()
        # Custom action logic
        return Response({'status': 'members assigned'})
```

### DRF Serializer Pattern
```python
from rest_framework import serializers

class CommitteeSerializer(serializers.ModelSerializer):
    chairperson_name = serializers.CharField(source='chairperson.full_name', read_only=True)

    class Meta:
        model = Committee
        fields = ['id', 'name', 'jurisdiction', 'chairperson', 'chairperson_name', 'status']
        read_only_fields = ['id']
```

### Permission Classes
```python
from rest_framework import permissions

class IsMemberOfParliament(permissions.BasePermission):
    """Allow access only to MPs"""
    def has_permission(self, request, view):
        return request.user.role == 'mp'

class IsMinister(permissions.BasePermission):
    """Allow access only to Ministers"""
    def has_permission(self, request, view):
        return request.user.role == 'minister'

class IsCommitteeMember(permissions.BasePermission):
    """Allow access to committee members"""
    def has_object_permission(self, request, view, obj):
        return request.user in obj.members.all()
```

## Multi-Tenant Enforcement
```python
# ALWAYS include tenant filter
def get_queryset(self):
    return Bill.objects.filter(
        tenant=self.request.user.tenant  # REQUIRED
    )
```

## e-Bangsamoro-Specific Models

### Legislative Module
- Bill, Resolution, Amendment
- Committee, CommitteeMembership
- Session, Vote, VoteRecord

### Oversight Module
- MOA, MOABudget, MOAProgram
- OversightReport, Finding

### Representation Module
- Constituent, Case, ServiceRequest
- District, Engagement

### Budget Module
- Appropriation, Allotment, Obligation
- Disbursement, BudgetReport

## Reference Files
See `.gemini/skills/backend/references/` for detailed patterns:
- `models.md` - Django model patterns
- `drf-apis.md` - DRF endpoint patterns
- `authentication.md` - JWT auth
- `authorization.md` - Permission patterns
