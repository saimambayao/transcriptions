# Database Optimization Guide

Django ORM optimization, indexing, query optimization, connection pooling.

## Query Optimization

### 1. Identify N+1 Queries

**Django Debug Toolbar** (development):
```python
# settings/development.py
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
```

**Logging Queries** (production):
```python
# Count queries in view
from django.db import connection
def my_view(request):
    queries_before = len(connection.queries)
    # ... view logic ...
    queries_after = len(connection.queries)
    print(f"Queries: {queries_after - queries_before}")
```

### 2. Use select_related() for ForeignKey

**When**: Accessing ForeignKey relationships

```python
# ❌ N+1 queries (1 + N where N = number of communities)
communities = Community.objects.all()
for community in communities:
    print(community.municipality.name)  # New query for each!

# ✅ 1 query with JOIN
communities = Community.objects.select_related('municipality', 'barangay')
for community in communities:
    print(community.municipality.name)  # No query
```

### 3. Use prefetch_related() for Reverse FK/M2M

**When**: Accessing reverse ForeignKey or ManyToMany

```python
# ❌ N+1 queries
communities = Community.objects.all()
for community in communities:
    households = community.households.all()  # New query!

# ✅ 2 queries total (one for communities, one for all households)
communities = Community.objects.prefetch_related('households')
for community in communities:
    households = community.households.all()  # From prefetch cache
```

### 4. Combined Optimization

```python
# Complex query with both
communities = Community.objects.select_related(
    'municipality',
    'barangay',
    'organization'
).prefetch_related(
    'households',
    'assessments'
).filter(
    organization=request.user.organization
)
```

## Database Indexing

### 1. Add Indexes to Frequently Filtered Fields

```python
class Task(BaseModel):
    # Fields used in WHERE clauses should have db_index=True
    organization = models.ForeignKey(Organization, on_delete=CASCADE, db_index=True)
    status = models.CharField(max_length=50, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    assigned_to = models.ForeignKey(User, on_delete=SET_NULL, null=True, db_index=True)
```

### 2. Composite Indexes

```python
class Task(BaseModel):
    class Meta:
        indexes = [
            models.Index(fields=['organization', 'status']),  # Common filter combination
            models.Index(fields=['organization', '-created_at']),  # List views
        ]
```

### 3. Verify Index Usage (PostgreSQL)

```sql
EXPLAIN ANALYZE SELECT * FROM tasks_task WHERE organization_id = 1 AND status = 'open';
```

## Query Result Caching

### 1. QuerySet Caching (Redis)

```python
from django.core.cache import cache

def get_communities(organization):
    cache_key = f"communities:{organization.id}"
    communities = cache.get(cache_key)
    if not communities:
        communities = list(Community.objects.filter(organization=organization).select_related('municipality'))
        cache.set(cache_key, communities, 300)  # 5 min
    return communities
```

### 2. Cache Invalidation

```python
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver([post_save, post_delete], sender=Community)
def invalidate_community_cache(sender, instance, **kwargs):
    cache_key = f"communities:{instance.organization.id}"
    cache.delete(cache_key)
```

## Connection Pooling

```python
# settings/production.py
DATABASES = {
    'default': {
        ...
        'CONN_MAX_AGE': 600,  # Reuse connections for 10 minutes
        'CONN_HEALTH_CHECKS': True,  # Check connection health
    }
}
```

## Query Optimization Checklist

- [ ] Use select_related() for FK
- [ ] Use prefetch_related() for reverse FK/M2M
- [ ] Add db_index=True to filtered fields
- [ ] Add composite indexes for common filter combinations
- [ ] Cache expensive query results
- [ ] Enable connection pooling
- [ ] Use only() to limit fields
- [ ] Use values() for dict results (faster than objects)
