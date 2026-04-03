# Database Constraints

Database constraints enforce data integrity rules at the database level, providing stronger guarantees than application-level validation.

## Table of Contents
- [Check Constraints](#check-constraints)
- [Unique Constraints](#unique-constraints)
- [Foreign Key Constraints](#foreign-key-constraints)
- [Django Meta Constraints](#django-meta-constraints)
- [Common Pitfalls](#common-pitfalls)
- [OBCMS-Specific Patterns](#obcms-specific-patterns)
- [Migration Examples](#migration-examples)
- [Related Patterns](#related-patterns)

## Check Constraints

Validate field values match specific conditions at the database level.

```python
from django.db import models
from django.db.models import Q, CheckConstraint

class Budget(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    year = models.IntegerField()
    status = models.CharField(max_length=20)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(amount__gte=0),
                name='budget_amount_positive'
            ),
            CheckConstraint(
                check=Q(year__gte=2020) & Q(year__lte=2050),
                name='budget_year_valid'
            ),
            CheckConstraint(
                check=Q(status__in=['draft', 'approved', 'executed']),
                name='budget_status_valid'
            ),
        ]
```

**When to use:** Enforce business rules that must hold at database level, such as positive amounts, valid date ranges, or enum-like status values.

**Why database-level:** Application validation can be bypassed with bulk operations or direct database access. Constraints are always enforced.

## Unique Constraints

Ensure combinations of fields are unique across the table.

```python
class WorkItem(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    fiscal_year = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            # Unique code per organization per year
            models.UniqueConstraint(
                fields=['organization', 'code', 'fiscal_year'],
                name='unique_workitem_per_org_year'
            ),
            # Unique code among active items only
            models.UniqueConstraint(
                fields=['organization', 'code'],
                condition=Q(is_active=True),
                name='unique_active_workitem_code'
            ),
        ]
```

**Partial unique constraints:** Use `condition` parameter to enforce uniqueness only on subset of rows (e.g., only active records).

## Foreign Key Constraints

Control referential integrity and deletion behavior.

```python
class Assessment(models.Model):
    community = models.ForeignKey(
        'communities.Community',
        on_delete=models.PROTECT,  # Prevent deletion if assessments exist
        related_name='assessments'
    )
    created_by = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,  # Keep assessment if user deleted
        null=True,
        related_name='created_assessments'
    )
    parent_assessment = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,  # Delete children when parent deleted
        null=True,
        blank=True,
        related_name='children'
    )
```

**on_delete options:**

| Option | Behavior | Use Case |
|--------|----------|----------|
| `CASCADE` | Delete related objects | Child records that don't make sense without parent |
| `PROTECT` | Prevent deletion | Referenced data that should never be orphaned |
| `SET_NULL` | Set to NULL | Audit fields where user might be deleted |
| `SET_DEFAULT` | Set to default value | Fallback to default when reference deleted |
| `DO_NOTHING` | Database handles it | Avoid in Django - use database triggers instead |
| `SET()` | Set to specific value/function | Custom logic when reference deleted |

## Django Meta Constraints

Complex multi-field constraints using F expressions and Q objects.

```python
from django.db.models import F

class Meeting(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_participants = models.IntegerField()
    min_participants = models.IntegerField()

    class Meta:
        constraints = [
            # End must be after start
            CheckConstraint(
                check=Q(end_time__gt=F('start_time')),
                name='meeting_end_after_start'
            ),
            # Max must be >= Min
            CheckConstraint(
                check=Q(max_participants__gte=F('min_participants')),
                name='meeting_max_gte_min'
            ),
        ]
```

**Complex conditions:**
```python
class BudgetAllocation(models.Model):
    budget = models.ForeignKey('Budget', on_delete=models.CASCADE)
    allocated_amount = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        constraints = [
            # Allocated cannot exceed total budget
            CheckConstraint(
                check=Q(allocated_amount__lte=F('budget__total_amount')),
                name='allocation_within_budget'
            ),
        ]
```

## Common Pitfalls

**Pitfall 1: Not naming constraints**
```python
# ❌ BAD - Django auto-generates hard-to-debug names
CheckConstraint(check=Q(amount__gte=0))

# ✅ GOOD - Explicit, descriptive name
CheckConstraint(
    check=Q(amount__gte=0),
    name='budget_amount_positive'
)
```

**Pitfall 2: Forgetting to create migrations**
```bash
# Constraints are schema changes - always create migration
python manage.py makemigrations
python manage.py migrate
```

**Pitfall 3: Using validators instead of constraints**
```python
# ❌ WEAK - Validators can be bypassed
class Budget(models.Model):
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]  # Only runs in forms/serializers
    )

# ✅ STRONG - Database enforces it
class Budget(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        constraints = [
            CheckConstraint(check=Q(amount__gte=0), name='budget_amount_positive')
        ]
```

**Pitfall 4: Constraint violations without user-friendly messages**
```python
# Handle constraint violations gracefully
from django.db import IntegrityError

try:
    work_item.save()
except IntegrityError as e:
    if 'unique_workitem_per_org_year' in str(e):
        raise ValidationError('Work item code already exists for this year')
    elif 'budget_amount_positive' in str(e):
        raise ValidationError('Budget amount must be positive')
    raise
```

## OBCMS-Specific Patterns

**Organization-Scoped Uniqueness:**
```python
class Community(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    region = models.ForeignKey('Region', on_delete=models.PROTECT)
    municipality = models.ForeignKey('Municipality', on_delete=models.PROTECT)

    class Meta:
        constraints = [
            # Community name unique per organization and region
            models.UniqueConstraint(
                fields=['organization', 'name', 'region'],
                name='unique_community_per_org_region'
            ),
        ]
```

**Soft Delete with Unique Constraints:**
```python
class Program(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            # Only active programs need unique codes
            models.UniqueConstraint(
                fields=['organization', 'code'],
                condition=Q(is_active=True),
                name='unique_active_program_code'
            ),
        ]
```

**Multi-Organizational Data Isolation:**
```python
class ResourceBooking(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    resource = models.ForeignKey('Resource', on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        constraints = [
            # No overlapping bookings per organization
            CheckConstraint(
                check=Q(end_date__gte=F('start_date')),
                name='booking_end_after_start'
            ),
            # TODO: Overlapping bookings need database trigger or app logic
        ]
```

## Migration Examples

**Adding constraint:**
```python
from django.db import migrations, models
from django.db.models import Q

class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='budget',
            constraint=models.CheckConstraint(
                check=Q(amount__gte=0),
                name='budget_amount_positive'
            ),
        ),
    ]
```

**Removing constraint:**
```python
class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0002_add_budget_constraint'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='budget',
            name='budget_amount_positive',
        ),
    ]
```

**Modifying constraint (remove + add):**
```python
class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0003_remove_budget_constraint'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='budget',
            name='budget_amount_positive',
        ),
        migrations.AddConstraint(
            model_name='budget',
            constraint=models.CheckConstraint(
                check=Q(amount__gte=0) & Q(amount__lte=1000000000),
                name='budget_amount_valid_range'
            ),
        ),
    ]
```

## Related Patterns

- See [migrations.md](migrations.md) for applying constraint changes safely
- See [schema-design.md](schema-design.md) for overall data modeling strategy
- See [indexes.md](indexes.md) for performance optimization with unique constraints
