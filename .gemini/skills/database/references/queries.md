# Query Optimization

Optimize Django ORM queries for performance and efficiency.

## Table of Contents
- [N+1 Query Problem](#n1-query-problem)
- [Select Related](#select-related)
- [Prefetch Related](#prefetch-related)
- [Query Analysis](#query-analysis)
- [Indexing for Queries](#indexing-for-queries)
- [Common Pitfalls](#common-pitfalls)
- [OBCMS-Specific Patterns](#obcms-specific-patterns)
- [Related Patterns](#related-patterns)

## N+1 Query Problem

The most common Django performance issue.

```python
# ❌ BAD - N+1 queries (1 + N where N = number of communities)
communities = Community.objects.all()
for community in communities:
    print(community.municipality.name)  # Queries database each iteration!

# ✅ GOOD - 2 queries total
communities = Community.objects.select_related('municipality').all()
for community in communities:
    print(community.municipality.name)  # No extra query
```

**Detecting N+1:**
```python
from django.db import connection
from django.test.utils import override_settings

@override_settings(DEBUG=True)
def test_queries():
    with connection.cursor() as cursor:
        # Your code here
        pass
    print(f"Queries executed: {len(connection.queries)}")
    for query in connection.queries:
        print(query['sql'])
```

## Select Related

Use for ForeignKey and OneToOne relationships (forward lookups).

```python
# Single level
communities = Community.objects.select_related('municipality')

# Multiple fields
communities = Community.objects.select_related(
    'municipality',
    'province',
    'region'
)

# Nested relationships
work_items = WorkItem.objects.select_related(
    'organization',
    'created_by__profile',  # User -> Profile
    'parent__organization'   # Parent WorkItem -> Organization
)

# All relationships (use carefully)
communities = Community.objects.select_related()  # All ForeignKey/OneToOne
```

**When to use:**
- Forward ForeignKey lookups
- OneToOne relationships
- When you need the related object for each result

## Prefetch Related

Use for reverse ForeignKey, ManyToMany, and reverse OneToOne.

```python
# Reverse ForeignKey
organizations = Organization.objects.prefetch_related('workitem_set')
for org in organizations:
    for work_item in org.workitem_set.all():  # No extra queries
        print(work_item.name)

# ManyToMany
programs = Program.objects.prefetch_related('communities')
for program in programs:
    for community in program.communities.all():  # No extra queries
        print(community.name)

# Multiple prefetches
assessments = Assessment.objects.prefetch_related(
    'responses',
    'comments',
    'attachments'
)
```

**Custom prefetch with filtering:**
```python
from django.db.models import Prefetch

# Prefetch only active work items
organizations = Organization.objects.prefetch_related(
    Prefetch(
        'workitem_set',
        queryset=WorkItem.objects.filter(is_active=True).order_by('created_at')
    )
)

# Prefetch with select_related nested
organizations = Organization.objects.prefetch_related(
    Prefetch(
        'workitem_set',
        queryset=WorkItem.objects.select_related('created_by')
    )
)
```

## Query Analysis

**Django Debug Toolbar (Development):**
```python
# settings.py
INSTALLED_APPS = [
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']
```

**Manual query logging:**
```python
import logging

# Enable query logging
logging.basicConfig()
logging.getLogger('django.db.backends').setLevel(logging.DEBUG)

# Or in settings.py
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'}
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    }
}
```

**Explain queries:**
```python
# See query execution plan
queryset = Community.objects.filter(region__code='IX')
print(queryset.explain())

# Detailed analysis
print(queryset.explain(analyze=True, verbose=True))
```

## Indexing for Queries

```python
# Add indexes for frequently queried fields
class Community(models.Model):
    name = models.CharField(max_length=200)
    region = models.ForeignKey('Region', on_delete=models.PROTECT)
    status = models.CharField(max_length=20)
    
    class Meta:
        indexes = [
            models.Index(fields=['region', 'status']),  # Composite index
            models.Index(fields=['name']),
            models.Index(fields=['-created_at']),  # Descending order
        ]
```

**Check missing indexes:**
```python
# Find slow queries without indexes
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("""
        SELECT schemaname, tablename, attname, n_distinct, correlation
        FROM pg_stats
        WHERE schemaname = 'public'
        AND tablename LIKE 'myapp_%'
        ORDER BY abs(correlation) DESC
    """)
    print(cursor.fetchall())
```

## Common Pitfalls

**Pitfall 1: Counting with len() instead of count()**
```python
# ❌ BAD - Fetches all records
communities = Community.objects.all()
total = len(communities)  # Loads all records into memory

# ✅ GOOD - Database count
total = Community.objects.count()  # Single COUNT query
```

**Pitfall 2: Checking existence with count()**
```python
# ❌ BAD - Counts all records
if Community.objects.filter(name='Test').count() > 0:
    pass

# ✅ GOOD - Stops at first match
if Community.objects.filter(name='Test').exists():
    pass
```

**Pitfall 3: Accessing related objects in templates without prefetch**
```python
# ❌ BAD - Template causes N+1 queries
# views.py
organizations = Organization.objects.all()

# template.html
{% for org in organizations %}
    {% for item in org.workitem_set.all %}  # N+1!
        {{ item.name }}
    {% endfor %}
{% endfor %}

# ✅ GOOD - Prefetch in view
organizations = Organization.objects.prefetch_related('workitem_set')
```

**Pitfall 4: Not using only() or defer() for large objects**
```python
# ❌ BAD - Loads large content field
documents = Document.objects.all()
for doc in documents:
    print(doc.title)  # But loaded entire content field too

# ✅ GOOD - Only load what you need
documents = Document.objects.only('id', 'title')

# Or defer large fields
documents = Document.objects.defer('content', 'attachments')
```

**Pitfall 5: Iterating querysets multiple times**
```python
# ❌ BAD - Queries database twice
communities = Community.objects.filter(region__code='IX')
count = communities.count()  # Query 1
for community in communities:  # Query 2
    print(community.name)

# ✅ GOOD - Evaluate once
communities = list(Community.objects.filter(region__code='IX'))
count = len(communities)  # No query
for community in communities:  # No query
    print(community.name)
```

## OBCMS-Specific Patterns

**Organization-scoped queries with prefetch:**
```python
# Get all work items with related data for organization
work_items = WorkItem.objects.filter(
    organization=request.user.organization
).select_related(
    'created_by',
    'parent'
).prefetch_related(
    'budget_set',
    'attachments',
    Prefetch(
        'children',
        queryset=WorkItem.objects.filter(is_active=True)
    )
)
```

**Geographic hierarchy queries:**
```python
# Efficient loading of geographic hierarchy
communities = Community.objects.select_related(
    'barangay__municipality__province__region'
).filter(
    barangay__municipality__province__region__code='IX'
)

# Prefetch all communities per region
regions = Region.objects.prefetch_related(
    Prefetch(
        'province_set__municipality_set__barangay_set__community_set',
        queryset=Community.objects.filter(is_active=True)
    )
)
```

**Assessment queries with responses:**
```python
# Load assessments with all related data
assessments = Assessment.objects.filter(
    community__organization=org
).select_related(
    'community__municipality__province',
    'created_by'
).prefetch_related(
    'assessmentresponse_set',
    'comments',
    'attachments'
).order_by('-created_at')
```

**Dashboard aggregation queries:**
```python
from django.db.models import Count, Sum, Avg

# Efficient stats query
stats = WorkItem.objects.filter(
    organization=org,
    fiscal_year=2025
).aggregate(
    total_items=Count('id'),
    total_budget=Sum('budget__amount'),
    avg_budget=Avg('budget__amount')
)

# Group by status
status_counts = WorkItem.objects.filter(
    organization=org
).values('status').annotate(
    count=Count('id'),
    total_budget=Sum('budget__amount')
).order_by('status')
```

## Related Patterns

- See [indexes.md](indexes.md) for indexing strategies
- See [transactions.md](transactions.md) for select_for_update
- See [postgresql-features.md](postgresql-features.md) for advanced queries
