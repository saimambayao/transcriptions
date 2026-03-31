# Database Indexes

Indexes dramatically improve query performance but require careful planning.

## Table of Contents
- [Index Types](#index-types)
- [When to Add Indexes](#when-to-add-indexes)
- [Composite Indexes](#composite-indexes)
- [Index Maintenance](#index-maintenance)
- [Common Pitfalls](#common-pitfalls)
- [OBCMS-Specific Patterns](#obcms-specific-patterns)
- [Related Patterns](#related-patterns)

## Index Types

**B-Tree Index (Default):**
```python
class Community(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        indexes = [
            models.Index(fields=['name']),  # B-tree index
        ]
```

**GIN Index (for JSON, arrays, full-text):**
```python
from django.contrib.postgres.indexes import GinIndex

class Assessment(models.Model):
    responses = models.JSONField()
    
    class Meta:
        indexes = [
            GinIndex(fields=['responses']),
        ]
```

**Partial Index (conditional):**
```python
class WorkItem(models.Model):
    status = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        indexes = [
            models.Index(
                fields=['status'],
                name='active_status_idx',
                condition=models.Q(is_active=True)
            )
        ]
```

## When to Add Indexes

**Add indexes for:**
- ForeignKey fields (Django adds automatically)
- Fields in WHERE clauses
- Fields in ORDER BY clauses
- Fields in JOIN conditions
- Fields used in filtering/searching

**Don't index:**
- Small tables (<1000 rows)
- Fields that are rarely queried
- Fields with low cardinality (few unique values) unless using partial index
- Write-heavy tables (indexes slow down writes)

## Composite Indexes

Index multiple fields together for specific queries.

```python
class WorkItem(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    fiscal_year = models.IntegerField()
    status = models.CharField(max_length=20)
    
    class Meta:
        indexes = [
            # Composite index - order matters!
            models.Index(fields=['organization', 'fiscal_year', 'status']),
        ]

# This query uses the index
WorkItem.objects.filter(
    organization=org,
    fiscal_year=2025,
    status='active'
)

# This query also uses the index (left-prefix rule)
WorkItem.objects.filter(organization=org, fiscal_year=2025)

# This query does NOT use the index (missing left-most field)
WorkItem.objects.filter(fiscal_year=2025, status='active')
```

**Descending indexes:**
```python
class Activity(models.Model):
    created_at = models.DateTimeField()
    
    class Meta:
        indexes = [
            models.Index(fields=['-created_at']),  # Descending
        ]

# Efficient for ORDER BY -created_at
Activity.objects.order_by('-created_at')[:10]
```

## Index Maintenance

**Check index usage:**
```sql
-- PostgreSQL: Check index statistics
SELECT
    schemaname,
    tablename,
    indexname,
    idx_scan,
    idx_tup_read,
    idx_tup_fetch
FROM pg_stat_user_indexes
WHERE schemaname = 'public'
ORDER BY idx_scan;
```

**Find unused indexes:**
```sql
-- Indexes never used
SELECT
    schemaname,
    tablename,
    indexname
FROM pg_stat_user_indexes
WHERE idx_scan = 0
AND schemaname = 'public';
```

**Index size:**
```sql
-- Check index sizes
SELECT
    tablename,
    indexname,
    pg_size_pretty(pg_relation_size(indexrelid)) as size
FROM pg_stat_user_indexes
WHERE schemaname = 'public'
ORDER BY pg_relation_size(indexrelid) DESC;
```

## Common Pitfalls

**Pitfall 1: Over-indexing**
```python
# ❌ BAD - Too many indexes slow down writes
class Model(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    field3 = models.CharField(max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['field1']),
            models.Index(fields=['field2']),
            models.Index(fields=['field3']),
            models.Index(fields=['field1', 'field2']),
            models.Index(fields=['field2', 'field3']),
            models.Index(fields=['field1', 'field2', 'field3']),
        ]

# ✅ GOOD - Only index what you actually query
class Model(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['field1', 'field2']),  # Most common query
        ]
```

**Pitfall 2: Wrong index order**
```python
# Query: organization + status
WorkItem.objects.filter(organization=org, status='active')

# ❌ BAD - Wrong order
indexes = [models.Index(fields=['status', 'organization'])]

# ✅ GOOD - High cardinality field first
indexes = [models.Index(fields=['organization', 'status'])]
```

**Pitfall 3: Not using db_index=True for frequently filtered fields**
```python
# ❌ BAD - Frequently filtered but not indexed
class Community(models.Model):
    status = models.CharField(max_length=20)

# ✅ GOOD - Add index
class Community(models.Model):
    status = models.CharField(max_length=20, db_index=True)
```

## OBCMS-Specific Patterns

**Organization-scoped indexes:**
```python
class WorkItem(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    fiscal_year = models.IntegerField()
    status = models.CharField(max_length=20)
    
    class Meta:
        indexes = [
            # Most queries filter by organization first
            models.Index(fields=['organization', 'fiscal_year']),
            models.Index(fields=['organization', 'status']),
            models.Index(fields=['organization', 'code']),
        ]
```

**Time-based queries:**
```python
class Assessment(models.Model):
    created_at = models.DateTimeField()
    community = models.ForeignKey('Community', on_delete=models.CASCADE)
    
    class Meta:
        indexes = [
            # Dashboard: recent assessments
            models.Index(fields=['-created_at']),
            # Community assessment history
            models.Index(fields=['community', '-created_at']),
        ]
```

**Search optimization:**
```python
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField

class Document(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    search_vector = SearchVectorField(null=True)
    
    class Meta:
        indexes = [
            GinIndex(fields=['search_vector']),
        ]
```

## Related Patterns

- See [queries.md](queries.md) for query optimization
- See [postgresql-features.md](postgresql-features.md) for GIN/GiST indexes
- See [migrations.md](migrations.md) for adding indexes safely
