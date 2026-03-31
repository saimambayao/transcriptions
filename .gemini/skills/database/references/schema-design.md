# Schema Design

Database schema design principles for scalable, maintainable Django applications.

## Table of Contents
- [Normalization](#normalization)
- [Denormalization](#denormalization)
- [Lookup Tables](#lookup-tables)
- [Audit Fields](#audit-fields)
- [Soft Deletes](#soft-deletes)
- [Multi-Tenancy](#multi-tenancy)
- [Common Pitfalls](#common-pitfalls)
- [OBCMS-Specific Patterns](#obcms-specific-patterns)
- [Related Patterns](#related-patterns)

## Normalization

Organize data to minimize redundancy.

**Third Normal Form (3NF) Example:**
```python
# ❌ BAD - Redundant data
class Order(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    # Customer data repeated for every order

# ✅ GOOD - Normalized
class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
```

## Denormalization

Sometimes duplication improves performance.

```python
# Denormalize for read-heavy workloads
class WorkItem(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    total_budget = models.DecimalField(max_digits=12, decimal_places=2)
    allocated_budget = models.DecimalField(max_digits=12, decimal_places=2)
    # Could calculate from budget_set, but denormalized for performance
    
    def update_budget_totals(self):
        """Update denormalized fields."""
        self.total_budget = self.budget_set.aggregate(
            total=Sum('amount')
        )['total'] or 0
        self.save(update_fields=['total_budget'])
```

## Lookup Tables

Reference data that rarely changes.

```python
class Region(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['code']

class Province(models.Model):
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
```

**Choices vs Foreign Keys:**
```python
# Use choices for small, stable lists
class WorkItem(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

# Use ForeignKey for dynamic/growing lists
class WorkItem(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
```

## Audit Fields

Track who created/modified records.

```python
class AuditMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(class)s_created'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(class)s_updated'
    )
    
    class Meta:
        abstract = True

class WorkItem(AuditMixin):
    name = models.CharField(max_length=200)
```

## Soft Deletes

Keep deleted records for audit trails.

```python
class SoftDeleteMixin(models.Model):
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='%(class)s_deleted'
    )
    
    class Meta:
        abstract = True
    
    def soft_delete(self, user):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.deleted_by = user
        self.save()
```

## Multi-Tenancy

Isolate data by organization.

```python
class OrganizationScopedMixin(models.Model):
    organization = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE
    )
    
    class Meta:
        abstract = True

# All organization-scoped models
class Community(OrganizationScopedMixin):
    name = models.CharField(max_length=200)
```

## Common Pitfalls

**Pitfall 1: Too many NULL fields**
```python
# ❌ BAD - Most fields optional
class Assessment(models.Model):
    field1 = models.CharField(max_length=100, null=True, blank=True)
    field2 = models.CharField(max_length=100, null=True, blank=True)
    # 20 more optional fields...

# ✅ GOOD - Use JSONField for variable data
class Assessment(models.Model):
    community = models.ForeignKey('Community', on_delete=models.CASCADE)
    responses = models.JSONField(default=dict)
```

**Pitfall 2: Circular dependencies**
```python
# ❌ BAD - Circular ForeignKey
class A(models.Model):
    b = models.ForeignKey('B', on_delete=models.CASCADE)

class B(models.Model):
    a = models.ForeignKey('A', on_delete=models.CASCADE)

# ✅ GOOD - Use intermediate table
class A(models.Model):
    pass

class B(models.Model):
    pass

class AB(models.Model):
    a = models.ForeignKey(A, on_delete=models.CASCADE)
    b = models.ForeignKey(B, on_delete=models.CASCADE)
```

## OBCMS-Specific Patterns

**Geographic hierarchy:**
```python
class Region(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)

class Province(models.Model):
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)

class Municipality(models.Model):
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)

class Barangay(models.Model):
    municipality = models.ForeignKey(Municipality, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
```

**Work item hierarchy:**
```python
class WorkItem(OrganizationScopedMixin, AuditMixin, SoftDeleteMixin):
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=500)
    
    class Meta:
        unique_together = [['organization', 'code']]
```

## Related Patterns

- See [constraints.md](constraints.md) for enforcing rules
- See [indexes.md](indexes.md) for performance
- See [migrations.md](migrations.md) for schema changes
