---
name: database
description: PostgreSQL database design and optimization for Bangsamoro Development Platform with Django ORM and Django Ninja. Covers schema design, migrations, migration verification, dependency chain validation, indexing, query optimization, transactions, and data management. Use when designing database schemas, writing migrations, verifying migration chains, fixing migration issues, optimizing queries, or managing PostgreSQL databases locally and in production (Railway).
argument-hint: "[topic]"
---

# Database Development - Bangsamoro Development Platform

Comprehensive guidance for PostgreSQL database design, Django migrations, migration verification, query optimization, and data management patterns for the Bangsamoro multi-portal system.

## Tech Stack

**Database:** PostgreSQL 18 as the primary relational database with advanced features like JSON fields, full-text search, and array types.

**ORM:** Django ORM for database abstraction, query building, and migrations. Django Ninja for API schema integration with Pydantic.

**Tools:** Railway PostgreSQL (managed), pgAdmin for database administration, Django Debug Toolbar for query analysis.

## When to Use This Skill

- Designing database schemas and entity relationships
- Creating or modifying Django migrations
- **Verifying migration dependency chains**
- **Fixing migration files and conflicts**
- **Troubleshooting production migration issues (Railway)**
- Optimizing slow database queries
- Adding indexes for performance
- Implementing data validation and constraints
- Handling database transactions
- Importing or exporting large datasets
- Designing multi-tenant data isolation
- Implementing soft deletes and audit trails
- Troubleshooting database performance issues

## Auto-Run After /build

**IMPORTANT:** When `/database` is invoked after `/build` has completed, automatically run the verification workflow without asking questions:

```bash
cd backend

# 1. Verify migration dependency chain
python3 ../.gemini/skills/database/scripts/verify_migrations.py .

# 2. Check migration status
python3 manage.py showmigrations --plan
```

**Expected results:**
- Migration chain: `[OK] No issues found`
- All migrations marked `[X]` (applied)

If issues are found, troubleshoot using the Migration Troubleshooting reference.

## Reference Navigation

### Schema and Structure

**Schema Design** - Database design, entity relationships, normalization. See [references/schema-design.md](references/schema-design.md) when designing database schemas.

**Migrations** - Django migrations, schema changes, data migrations. See [references/migrations.md](references/migrations.md) when creating or managing database migrations.

**Migration Troubleshooting** - Dependency chain issues, conflict resolution, production deployment, Railway patterns. See [references/migration-troubleshooting.md](references/migration-troubleshooting.md) when fixing migration issues or deploying to production.

### Performance

**Indexes** - Index strategies, performance optimization. See [references/indexes.md](references/indexes.md) when optimizing query performance.

**Queries** - Query optimization, N+1 problems, select_related/prefetch_related. See [references/queries.md](references/queries.md) when optimizing database access.

### Data Management

**Transactions** - Database transactions, ACID properties. See [references/transactions.md](references/transactions.md) when handling complex operations.

**Constraints** - Database constraints, validation. See [references/constraints.md](references/constraints.md) when implementing data validation.

## Quick Reference

### Migration Verification Workflow

**Before any migration work:**
```bash
cd backend

# Step 1: Verify current migration chain
python ../.gemini/skills/database/scripts/verify_migrations.py .

# Step 2: Check migration status
python manage.py showmigrations --plan
```

**After creating migrations:**
```bash
# Verify no issues introduced
python ../.gemini/skills/database/scripts/verify_migrations.py .

# Test locally
python manage.py migrate
python manage.py migrate app_name previous_migration  # Test rollback
python manage.py migrate  # Test forward again
```

**Fix common issues:**
```bash
# Dry run first
python ../.gemini/skills/database/scripts/fix_migrations.py . --dry-run

# Apply fixes
python ../.gemini/skills/database/scripts/fix_migrations.py .

# Generate dependency graph for analysis
python ../.gemini/skills/database/scripts/fix_migrations.py . --graph=migrations.dot
```

**Production deployment (Railway):**
Migrations run automatically on deploy via entrypoint. Ensure:
1. All migrations committed
2. Dependency chain verified
3. No conflicting migrations
4. Database backed up for risky changes

### Multi-Tenant Model Pattern

```python
# apps/cooperatives/models.py
from django.db import models
from apps.core.models import Organization

class Cooperative(models.Model):
    """Cooperative model with multi-tenant isolation."""

    # Multi-tenant field (required)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='cooperatives'
    )

    # Core fields
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

    # Audit fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'auth.User',
        on_delete=models.PROTECT,
        related_name='cooperatives_created'
    )

    # Soft delete
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['organization']),
            models.Index(fields=['status']),
            models.Index(fields=['shortname']),
        ]

    def __str__(self):
        return self.name
```

### Django Ninja Schema Integration

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
    created_at: datetime

class CooperativeIn(Schema):
    name: str
    registration_number: str
    shortname: Optional[str] = None

# apps/cooperatives/api.py
from ninja import Router
from .models import Cooperative
from .schemas import CooperativeOut, CooperativeIn

router = Router()

@router.get('/', response=list[CooperativeOut])
def list_cooperatives(request):
    return Cooperative.objects.filter(
        organization=request.auth.organization,
        is_deleted=False
    ).select_related('organization')
```

### Query Optimization Patterns

**N+1 Query Prevention:**

```python
# BAD: N+1 queries
cooperatives = Cooperative.objects.all()
for coop in cooperatives:
    print(coop.organization.name)  # Query per cooperative!

# GOOD: Single query with join
cooperatives = Cooperative.objects.select_related('organization').all()
for coop in cooperatives:
    print(coop.organization.name)  # No additional query

# GOOD: For reverse relationships (ManyToMany, reverse FK)
cooperatives = Cooperative.objects.prefetch_related('members').all()
for coop in cooperatives:
    for member in coop.members.all():  # No additional query
        print(member.name)
```

**Index Strategy:**

```python
class Cooperative(models.Model):
    # Fields frequently filtered/ordered
    status = models.CharField(max_length=20, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    # Multi-tenant field (always indexed)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        db_index=True
    )

    class Meta:
        indexes = [
            # Composite index for common query pattern
            models.Index(fields=['organization', 'status']),
            # Index for ordering
            models.Index(fields=['-created_at']),
        ]
```

### Migration Best Practices

**Creating Migrations:**

```bash
# Generate migration
cd backend
python manage.py makemigrations cooperatives

# Review migration file
# backend/apps/cooperatives/migrations/0002_add_field.py

# Apply migration (local)
python manage.py migrate

# Check migration status
python manage.py showmigrations
```

**Safe Migration Patterns:**

```python
# migrations/0002_add_status_field.py
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('cooperatives', '0001_initial'),
    ]

    operations = [
        # Add nullable field first (safe)
        migrations.AddField(
            model_name='cooperative',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

# migrations/0003_populate_status.py
def populate_status(apps, schema_editor):
    Cooperative = apps.get_model('cooperatives', 'Cooperative')
    Cooperative.objects.filter(status__isnull=True).update(status='active')

class Migration(migrations.Migration):
    dependencies = [
        ('cooperatives', '0002_add_status_field'),
    ]

    operations = [
        migrations.RunPython(populate_status, migrations.RunPython.noop),
    ]

# migrations/0004_make_status_required.py
class Migration(migrations.Migration):
    dependencies = [
        ('cooperatives', '0003_populate_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperative',
            name='status',
            field=models.CharField(max_length=20, default='pending'),
        ),
    ]
```

### Transaction Patterns

```python
from django.db import transaction

# Atomic transaction
@transaction.atomic
def transfer_member(member_id, from_coop_id, to_coop_id):
    member = Member.objects.select_for_update().get(id=member_id)
    from_coop = Cooperative.objects.get(id=from_coop_id)
    to_coop = Cooperative.objects.get(id=to_coop_id)

    # These operations are atomic
    from_coop.members.remove(member)
    to_coop.members.add(member)
    member.transferred_at = timezone.now()
    member.save()
```

### Soft Delete Pattern

```python
from django.db import models
from django.utils import timezone

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True
```

## CSEA-Specific Patterns

### Organization-Scoped Queries

```python
# ALWAYS filter by organization in views
@router.get('/cooperatives')
def list_cooperatives(request):
    return Cooperative.objects.filter(
        organization=request.auth.organization
    )

# Include organization on create
@router.post('/cooperatives')
def create_cooperative(request, payload: CooperativeIn):
    return Cooperative.objects.create(
        **payload.dict(),
        organization=request.auth.organization,
        created_by=request.auth
    )
```

### Common Entity Relationships

```
Organization (Tenant)
    │
    ├── Cooperatives
    │       └── Members
    │       └── Products
    │       └── Documents
    │
    ├── Social Enterprises
    │       └── Beneficiaries
    │       └── Products
    │       └── Impact Metrics
    │
    └── Users
            └── Roles/Permissions
```

## Database Performance Checklist

- [ ] All foreign keys indexed
- [ ] Common filter fields indexed
- [ ] Composite indexes for common queries
- [ ] select_related for ForeignKey access
- [ ] prefetch_related for reverse/M2M access
- [ ] Pagination on list endpoints
- [ ] No N+1 queries in loops
- [ ] Transactions for multi-step operations

## Railway PostgreSQL

**Connection:**
```python
# settings.py
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}
```

**Backup:**
```bash
# Railway CLI
railway run pg_dump -Fc > backup.dump

# Restore
railway run pg_restore -d $DATABASE_URL backup.dump
```
