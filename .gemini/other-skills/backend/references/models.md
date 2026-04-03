# Django Models and ORM

Comprehensive guide for Django model design, relationships, migrations, and query optimization for OBCMS.

## Table of Contents

- [Model Design Principles](#model-design-principles)
- [Field Types and Options](#field-types-and-options)
- [Relationships](#relationships)
- [Model Mixins](#model-mixins)
- [Custom Managers and QuerySets](#custom-managers-and-querysets)
- [Model Methods](#model-methods)
- [Migrations](#migrations)
- [Query Optimization](#query-optimization)

## Model Design Principles

### Organization-Scoped Models

OBCMS is multi-organizational. Most models should be scoped to an organization:

```python
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Organization(models.Model):
    """Government organization or ministry."""
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)
    org_type = models.CharField(max_length=50, choices=[
        ('OOBC', 'Office for Other Bangsamoro Communities'),
        ('MINISTRY', 'Partner Ministry'),
        ('LGU', 'Local Government Unit'),
    ])

    class Meta:
        db_table = 'organizations'
        ordering = ['name']

    def __str__(self):
        return self.name


class Community(models.Model):
    """OBC community managed by an organization."""
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    region = models.ForeignKey('geography.Region', on_delete=models.PROTECT)
    municipality = models.ForeignKey('geography.Municipality', on_delete=models.PROTECT)
    barangay = models.ForeignKey('geography.Barangay', on_delete=models.PROTECT)
    population = models.IntegerField(null=True, blank=True)

    # Audit fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='communities_created')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='communities_updated')

    class Meta:
        db_table = 'communities'
        ordering = ['name']
        unique_together = [['organization', 'name', 'barangay']]
        indexes = [
            models.Index(fields=['organization', 'region']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.name}, {self.barangay.name}"
```

### Audit Trail Pattern

Track who created and modified records:

```python
class AuditMixin(models.Model):
    """Mixin providing audit fields for tracking record changes."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_created'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_updated'
    )

    class Meta:
        abstract = True


class Program(AuditMixin):
    """Government program or intervention."""
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=50, choices=[
        ('PLANNING', 'Planning'),
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ])

    class Meta:
        db_table = 'programs'
        ordering = ['-created_at']
```

### Soft Delete Pattern

Don't hard-delete records - use soft deletes:

```python
class SoftDeleteManager(models.Manager):
    """Manager that filters out soft-deleted records."""

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class SoftDeleteModel(models.Model):
    """Mixin for soft delete functionality."""
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)
    deleted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(app_label)s_%(class)s_deleted'
    )

    objects = SoftDeleteManager()
    all_objects = models.Manager()  # Access all records including deleted

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False, user=None):
        """Soft delete the record."""
        from django.utils import timezone
        self.deleted_at = timezone.now()
        if user:
            self.deleted_by = user
        self.save()

    def hard_delete(self):
        """Permanently delete the record."""
        super().delete()

    def restore(self):
        """Restore a soft-deleted record."""
        self.deleted_at = None
        self.deleted_by = None
        self.save()


class Assessment(AuditMixin, SoftDeleteModel):
    """MANA community assessment."""
    community = models.ForeignKey(Community, on_delete=models.PROTECT)
    assessment_date = models.DateField()
    status = models.CharField(max_length=50, default='DRAFT')

    class Meta:
        db_table = 'assessments'
```

## Field Types and Options

### Common Field Patterns

```python
class Beneficiary(models.Model):
    """Individual beneficiary of programs."""

    # Text fields
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    suffix = models.CharField(max_length=10, blank=True)  # Jr., Sr., III

    # Choices field
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'Prefer not to say'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    # Date fields
    birth_date = models.DateField()
    registration_date = models.DateField(auto_now_add=True)

    # Email and phone
    email = models.EmailField(blank=True)
    mobile = models.CharField(max_length=20)

    # Address components
    house_number = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=200, blank=True)
    barangay = models.ForeignKey('geography.Barangay', on_delete=models.PROTECT)

    # Boolean flags
    is_indigenous = models.BooleanField(default=False)
    is_senior = models.BooleanField(default=False)
    is_pwd = models.BooleanField(default=False)  # Person with Disability

    # Integer fields
    household_size = models.IntegerField(default=1)

    # Decimal fields
    monthly_income = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    # Text area
    special_needs = models.TextField(blank=True)

    # JSON field for flexible data
    metadata = models.JSONField(default=dict, blank=True)

    class Meta:
        db_table = 'beneficiaries'
        ordering = ['last_name', 'first_name']
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['barangay', 'registration_date']),
        ]

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        """Return full name with suffix."""
        parts = [self.first_name, self.middle_name, self.last_name]
        name = ' '.join(p for p in parts if p)
        if self.suffix:
            name = f"{name} {self.suffix}"
        return name

    @property
    def age(self):
        """Calculate age from birth date."""
        from datetime import date
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
```

### Geographic Fields (without PostGIS)

OBCMS stores geographic data as GeoJSON in JSONField:

```python
class GeographicArea(models.Model):
    """Base model for geographic entities."""
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)

    # Store GeoJSON in JSONField
    geometry = models.JSONField(
        null=True,
        blank=True,
        help_text="GeoJSON geometry for boundary"
    )

    class Meta:
        abstract = True

    def get_center_coordinates(self):
        """Extract center point from GeoJSON."""
        if not self.geometry:
            return None

        if self.geometry.get('type') == 'Point':
            return self.geometry['coordinates']
        elif self.geometry.get('type') == 'Polygon':
            # Calculate centroid (simple average)
            coords = self.geometry['coordinates'][0]
            lon = sum(c[0] for c in coords) / len(coords)
            lat = sum(c[1] for c in coords) / len(coords)
            return [lon, lat]

        return None


class Region(GeographicArea):
    """Philippine region (e.g., Region IX, X, XI, XII)."""

    class Meta:
        db_table = 'geography_regions'
        ordering = ['code']


class Province(GeographicArea):
    """Province within a region."""
    region = models.ForeignKey(Region, on_delete=models.PROTECT)

    class Meta:
        db_table = 'geography_provinces'
        ordering = ['name']


class Municipality(GeographicArea):
    """Municipality or City."""
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    city = models.BooleanField(default=False)

    class Meta:
        db_table = 'geography_municipalities'
        ordering = ['name']


class Barangay(GeographicArea):
    """Barangay (smallest administrative unit)."""
    municipality = models.ForeignKey(Municipality, on_delete=models.PROTECT)
    population = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'geography_barangays'
        ordering = ['name']
```

## Relationships

### One-to-Many (ForeignKey)

```python
class Project(models.Model):
    """Development project."""
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    program = models.ForeignKey(Program, on_delete=models.PROTECT, related_name='projects')

    class Meta:
        db_table = 'projects'


class Activity(models.Model):
    """Project activity."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='activities')
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'activities'

# Usage:
project = Project.objects.get(pk=1)
activities = project.activities.all()  # Related name
```

### Many-to-Many

```python
class Sector(models.Model):
    """Development sector (Health, Education, etc.)."""
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'sectors'


class Need(models.Model):
    """Community need from MANA assessment."""
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    description = models.TextField()
    priority = models.IntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')])

    # Many-to-many: A need can span multiple sectors
    sectors = models.ManyToManyField(Sector, related_name='needs')

    class Meta:
        db_table = 'needs'

# Usage:
need = Need.objects.get(pk=1)
need.sectors.add(health_sector, education_sector)
need.sectors.all()  # QuerySet of sectors
```

### Many-to-Many with Through Model

When you need extra fields on the relationship:

```python
class ProgramBeneficiary(models.Model):
    """Through model for program-beneficiary relationship."""
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)

    # Extra fields on the relationship
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('ENROLLED', 'Enrolled'),
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('DROPPED', 'Dropped Out'),
    ])
    completion_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'program_beneficiaries'
        unique_together = [['program', 'beneficiary']]


class Program(models.Model):
    # ... other fields ...
    beneficiaries = models.ManyToManyField(
        Beneficiary,
        through='ProgramBeneficiary',
        related_name='programs'
    )

# Usage:
program.beneficiaries.add(
    beneficiary,
    through_defaults={'status': 'ENROLLED'}
)

# Or create directly:
ProgramBeneficiary.objects.create(
    program=program,
    beneficiary=beneficiary,
    status='ENROLLED'
)
```

### Self-Referential Relationships

```python
class WorkItem(models.Model):
    """Task or work item with parent-child hierarchy."""
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        db_table = 'work_items'

    def get_ancestors(self):
        """Get all parent work items."""
        ancestors = []
        current = self.parent
        while current:
            ancestors.append(current)
            current = current.parent
        return ancestors

    def get_descendants(self):
        """Get all child work items recursively."""
        descendants = list(self.children.all())
        for child in self.children.all():
            descendants.extend(child.get_descendants())
        return descendants
```

## Model Mixins

### Timestamped Mixin

```python
class TimestampedModel(models.Model):
    """Mixin for timestamp fields."""
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```

### Status Mixin

```python
class StatusMixin(models.Model):
    """Mixin for status tracking."""
    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='DRAFT')
    status_changed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """Track when status changes."""
        if self.pk:
            old = self.__class__.objects.get(pk=self.pk)
            if old.status != self.status:
                from django.utils import timezone
                self.status_changed_at = timezone.now()
        super().save(*args, **kwargs)
```

## Custom Managers and QuerySets

### Custom QuerySet

```python
class CommunityQuerySet(models.QuerySet):
    """Custom queryset for Community model."""

    def for_organization(self, organization):
        """Filter communities by organization."""
        return self.filter(organization=organization)

    def in_region(self, region):
        """Filter communities in a specific region."""
        return self.filter(region=region)

    def active(self):
        """Filter active communities only."""
        return self.filter(deleted_at__isnull=True)

    def with_assessment_count(self):
        """Annotate with count of assessments."""
        return self.annotate(
            assessment_count=models.Count('assessment')
        )

    def with_latest_assessment(self):
        """Annotate with latest assessment date."""
        from django.db.models import Max
        return self.annotate(
            latest_assessment=Max('assessment__assessment_date')
        )


class Community(models.Model):
    # ... fields ...

    objects = CommunityQuerySet.as_manager()

    class Meta:
        db_table = 'communities'

# Usage:
communities = Community.objects.for_organization(org).in_region(region).with_assessment_count()
```

### Custom Manager

```python
class OrganizationScopedManager(models.Manager):
    """Manager that auto-filters by organization."""

    def __init__(self, *args, **kwargs):
        self.organization_field = kwargs.pop('organization_field', 'organization')
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        """Override to add organization filter."""
        qs = super().get_queryset()
        if hasattr(self, '_organization'):
            filter_kwargs = {self.organization_field: self._organization}
            return qs.filter(**filter_kwargs)
        return qs

    def for_organization(self, organization):
        """Set organization for this manager instance."""
        manager = self.__class__(organization_field=self.organization_field)
        manager._organization = organization
        manager.model = self.model
        return manager
```

## Model Methods

### Common Methods

```python
class Program(models.Model):
    # ... fields ...

    def __str__(self):
        """String representation."""
        return self.name

    def get_absolute_url(self):
        """URL for this program."""
        from django.urls import reverse
        return reverse('programs:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        """Override save for custom logic."""
        # Uppercase the code
        if self.code:
            self.code = self.code.upper()

        # Validate before saving
        self.full_clean()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Override delete for custom logic."""
        # Don't allow deletion if has active projects
        if self.projects.filter(status='ACTIVE').exists():
            raise ValueError("Cannot delete program with active projects")

        super().delete(*args, **kwargs)

    def clean(self):
        """Model validation."""
        from django.core.exceptions import ValidationError

        if self.budget and self.budget < 0:
            raise ValidationError({'budget': 'Budget cannot be negative'})

        if self.end_date and self.start_date and self.end_date < self.start_date:
            raise ValidationError({'end_date': 'End date must be after start date'})
```

### Property Methods

```python
class Assessment(models.Model):
    # ... fields ...

    @property
    def is_complete(self):
        """Check if assessment is complete."""
        return self.status == 'COMPLETED'

    @property
    def days_since_assessment(self):
        """Days since assessment date."""
        from datetime import date
        return (date.today() - self.assessment_date).days

    @property
    def completion_percentage(self):
        """Calculate completion percentage."""
        total_sections = 10
        completed = self.sections.filter(status='COMPLETED').count()
        return (completed / total_sections) * 100 if total_sections > 0 else 0
```

## Migrations

### Creating Migrations

```bash
# Create migrations for all changes
python manage.py makemigrations

# Create migration for specific app
python manage.py makemigrations communities

# Create empty migration
python manage.py makemigrations --empty communities
```

### Data Migration Example

```python
# migrations/0005_populate_regions.py
from django.db import migrations

def populate_regions(apps, schema_editor):
    """Populate initial regions."""
    Region = apps.get_model('geography', 'Region')
    regions = [
        {'code': 'IX', 'name': 'Region IX - Zamboanga Peninsula'},
        {'code': 'X', 'name': 'Region X - Northern Mindanao'},
        {'code': 'XI', 'name': 'Region XI - Davao Region'},
        {'code': 'XII', 'name': 'Region XII - SOCCSKSARGEN'},
    ]
    for region_data in regions:
        Region.objects.get_or_create(
            code=region_data['code'],
            defaults={'name': region_data['name']}
        )

def reverse_populate(apps, schema_editor):
    """Reverse the migration."""
    Region = apps.get_model('geography', 'Region')
    Region.objects.filter(code__in=['IX', 'X', 'XI', 'XII']).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('geography', '0004_previous_migration'),
    ]

    operations = [
        migrations.RunPython(populate_regions, reverse_populate),
    ]
```

### Migration Best Practices

1. **Always review generated migrations**
2. **Add database indexes for foreign keys and commonly queried fields**
3. **Use `db_index=True` in model definitions**
4. **Test migrations on staging database first**
5. **Keep migrations small and focused**
6. **Never edit applied migrations**

## Query Optimization

### Select Related (One-to-One, ForeignKey)

```python
# Bad - N+1 queries
communities = Community.objects.all()
for community in communities:
    print(community.region.name)  # Extra query per iteration

# Good - 1 query with JOIN
communities = Community.objects.select_related('region', 'municipality', 'barangay')
for community in communities:
    print(community.region.name)  # No extra query
```

### Prefetch Related (Many-to-Many, Reverse ForeignKey)

```python
# Bad - N+1 queries
programs = Program.objects.all()
for program in programs:
    print(program.projects.count())  # Extra query per iteration

# Good - 2 queries total
programs = Program.objects.prefetch_related('projects')
for program in programs:
    print(program.projects.count())  # No extra query
```

### Combining Select and Prefetch

```python
# Efficient: 3 queries total
assessments = Assessment.objects.select_related(
    'community',
    'community__region',
    'community__barangay'
).prefetch_related(
    'needs',
    'needs__sectors'
)
```

### Only and Defer

```python
# Only load specific fields
beneficiaries = Beneficiary.objects.only('first_name', 'last_name', 'email')

# Load all except specific fields
beneficiaries = Beneficiary.objects.defer('metadata', 'special_needs')
```

### Aggregation

```python
from django.db.models import Count, Sum, Avg, Max, Min

# Count by status
Program.objects.values('status').annotate(count=Count('id'))

# Total budget by organization
Program.objects.values('organization__name').annotate(
    total_budget=Sum('budget')
)

# Average household size by barangay
Beneficiary.objects.values('barangay__name').annotate(
    avg_household=Avg('household_size')
)
```

### Bulk Operations

```python
# Bulk create (efficient for many records)
beneficiaries = [
    Beneficiary(first_name=f'John{i}', last_name='Doe')
    for i in range(1000)
]
Beneficiary.objects.bulk_create(beneficiaries, batch_size=500)

# Bulk update
Beneficiary.objects.filter(barangay=old_barangay).update(
    barangay=new_barangay,
    updated_at=timezone.now()
)

# Bulk delete
Beneficiary.objects.filter(registration_date__lt='2020-01-01').delete()
```

This covers the essential Django model patterns for OBCMS. For API serialization of these models, see [serializers.md](serializers.md).
