# Code Quality

Guide for code organization, design patterns, and best practices.

## Service Layer Pattern

```python
# services/community_service.py
from django.db import transaction
from communities.models import Community
from mana.models import Assessment

class CommunityService:
    """Business logic for communities."""

    @staticmethod
    @transaction.atomic
    def create_community_with_assessment(community_data, user):
        """Create community and initial assessment."""
        community = Community.objects.create(
            **community_data,
            created_by=user,
            updated_by=user,
            organization=user.organization
        )
        
        # Create initial assessment
        assessment = Assessment.objects.create(
            community=community,
            status='PENDING',
            created_by=user,
            updated_by=user
        )
        
        return community, assessment

    @staticmethod
    def get_community_statistics(organization):
        """Get statistics for an organization's communities."""
        from django.db.models import Count, Sum, Avg
        
        communities = Community.objects.filter(organization=organization)
        return {
            'total_communities': communities.count(),
            'total_population': communities.aggregate(Sum('population'))['population__sum'],
            'avg_population': communities.aggregate(Avg('population'))['population__avg'],
            'by_region': communities.values('region__name').annotate(count=Count('id')),
        }

# Usage in views
from services.community_service import CommunityService

def create_community_view(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community, assessment = CommunityService.create_community_with_assessment(
                form.cleaned_data,
                request.user
            )
            return redirect('communities:detail', pk=community.pk)
```

## Repository Pattern

```python
# repositories/community_repository.py
from django.db.models import Q

class CommunityRepository:
    """Data access layer for communities."""

    @staticmethod
    def get_by_organization(organization):
        """Get all communities for an organization."""
        return Community.objects.filter(
            organization=organization
        ).select_related('region', 'municipality', 'barangay')

    @staticmethod
    def search(query, organization):
        """Search communities by name or location."""
        return Community.objects.filter(
            Q(name__icontains=query) |
            Q(barangay__name__icontains=query) |
            Q(municipality__name__icontains=query),
            organization=organization
        )

    @staticmethod
    def get_with_assessment_count(organization):
        """Get communities with assessment count."""
        from django.db.models import Count
        return Community.objects.filter(
            organization=organization
        ).annotate(
            assessment_count=Count('assessment')
        )
```

## Code Organization

```
app/
├── models.py                   # Database models
├── views.py or views/         # View logic
├── forms.py                    # Django forms
├── serializers.py              # DRF serializers
├── services/                   # Business logic
│   ├── community_service.py
│   └── assessment_service.py
├── repositories/               # Data access
│   └── community_repository.py
├── managers.py                 # Custom model managers
├── admin.py                    # Django admin
├── urls.py                     # URL routing
├── tests/                      # Tests
│   ├── test_models.py
│   ├── test_views.py
│   └── test_services.py
└── templatetags/               # Custom template tags
    └── community_tags.py
```

## Best Practices

### 1. Use timezone-aware datetimes
```python
from django.utils import timezone

# Good
created_at = models.DateTimeField(default=timezone.now)
now = timezone.now()

# Bad
from datetime import datetime
now = datetime.now()  # Naive datetime
```

### 2. Use select_related and prefetch_related
```python
# Good
communities = Community.objects.select_related('region', 'municipality').all()

# Bad
communities = Community.objects.all()
for community in communities:
    print(community.region.name)  # N+1 query problem
```

### 3. Use transactions for multiple operations
```python
from django.db import transaction

# Good
@transaction.atomic
def create_program_with_projects(program_data, projects_data):
    program = Program.objects.create(**program_data)
    for project_data in projects_data:
        Project.objects.create(program=program, **project_data)
    return program
```

### 4. Validate in models and forms
```python
class Community(models.Model):
    def clean(self):
        if self.population and self.population < 0:
            raise ValidationError({'population': 'Population cannot be negative'})
    
    def save(self, *args, **kwargs):
        self.full_clean()  # Run validation
        super().save(*args, **kwargs)
```

### 5. Use constants for choices
```python
class Program(models.Model):
    STATUS_DRAFT = 'DRAFT'
    STATUS_ACTIVE = 'ACTIVE'
    STATUS_COMPLETED = 'COMPLETED'
    
    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_ACTIVE, 'Active'),
        (STATUS_COMPLETED, 'Completed'),
    ]
    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_DRAFT)
```

## Code Style

Follow PEP 8 and Django coding style:

```bash
# Install tools
pip install black isort flake8

# Format code
black .
isort .

# Check style
flake8 .
```

This completes the backend skill reference documentation.
