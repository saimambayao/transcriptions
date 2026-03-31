# PostgreSQL-Specific Features

Django + PostgreSQL provides advanced features beyond standard SQL for efficient data handling.

## Table of Contents
- [JSON Fields](#json-fields)
- [Array Fields](#array-fields)
- [Full-Text Search](#full-text-search)
- [PostgreSQL Indexes](#postgresql-indexes)
- [Database Functions](#database-functions)
- [Common Pitfalls](#common-pitfalls)
- [OBCMS-Specific Patterns](#obcms-specific-patterns)
- [Performance Tips](#performance-tips)
- [Related Patterns](#related-patterns)

## JSON Fields

Store and query JSON data efficiently without separate tables.

```python
from django.db import models

class AssessmentResponse(models.Model):
    assessment = models.ForeignKey('Assessment', on_delete=models.CASCADE)
    responses = models.JSONField(default=dict)
    metadata = models.JSONField(default=dict)

# Store JSON data
assessment_response = AssessmentResponse.objects.create(
    assessment=assessment,
    responses={
        'health': {
            'hospitals': 2,
            'health_workers': 15,
            'rating': 'poor'
        },
        'education': {
            'schools': 5,
            'teachers': 30,
            'rating': 'fair'
        }
    },
    metadata={
        'surveyor': 'John Doe',
        'date': '2025-10-31'
    }
)
```

**Query JSON fields:**
```python
# Query by nested key
responses = AssessmentResponse.objects.filter(
    responses__health__rating='poor'
)

# Numeric comparisons
responses = AssessmentResponse.objects.filter(
    responses__health__hospitals__gte=2
)

# Check key existence
responses = AssessmentResponse.objects.filter(
    responses__has_key='health'
)

# Multiple keys exist
responses = AssessmentResponse.objects.filter(
    responses__has_keys=['health', 'education']
)

# Any key exists
responses = AssessmentResponse.objects.filter(
    responses__has_any_keys=['health', 'infrastructure']
)
```

**Update JSON fields:**
```python
# Update entire field
assessment_response.responses['health']['hospitals'] = 3
assessment_response.save()

# JSONField update with F expression (Django 3.1+)
from django.db.models.functions import JSONObject

AssessmentResponse.objects.filter(id=response_id).update(
    metadata=JSONObject(processed=True)
)
```

## Array Fields

Store lists of values in a single column.

```python
from django.contrib.postgres.fields import ArrayField

class Community(models.Model):
    name = models.CharField(max_length=200)
    languages = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        default=list
    )
    contact_numbers = ArrayField(
        models.CharField(max_length=20),
        size=5,  # Max 5 phone numbers
        default=list
    )
    indigenous_groups = ArrayField(
        models.CharField(max_length=100),
        default=list
    )

# Create with array values
community = Community.objects.create(
    name="Marawi Community",
    languages=['Maranao', 'Tagalog', 'English'],
    contact_numbers=['+63123456789', '+63987654321'],
    indigenous_groups=['Maranao', 'Iranun']
)
```

**Query arrays:**
```python
# Contains specific value
communities = Community.objects.filter(
    languages__contains=['Maranao']
)

# Contains any of these values (overlap)
communities = Community.objects.filter(
    languages__overlap=['Maranao', 'Tausug']
)

# Array length
from django.contrib.postgres.fields import ArrayField
from django.db.models import Func

communities = Community.objects.annotate(
    lang_count=Func('languages', function='cardinality')
).filter(lang_count__gte=3)

# Index into array (0-based)
communities = Community.objects.filter(
    languages__0='Maranao'  # First language
)

# Contained by (subset check)
communities = Community.objects.filter(
    languages__contained_by=['Maranao', 'Tagalog', 'English', 'Cebuano']
)
```

**Array aggregations:**
```python
from django.contrib.postgres.aggregates import ArrayAgg

# Collect all languages used
all_languages = Community.objects.aggregate(
    all_langs=ArrayAgg('languages', distinct=True)
)
```

## Full-Text Search

Efficient text search using PostgreSQL's built-in capabilities.

```python
from django.contrib.postgres.search import (
    SearchVector, SearchQuery, SearchRank, SearchHeadline
)

class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.CharField(max_length=500)

# Simple search in single field
results = Document.objects.filter(title__search='community assessment')

# Multi-field search
results = Document.objects.annotate(
    search=SearchVector('title', 'content', 'tags')
).filter(search='community assessment')

# Weighted search (title more important)
results = Document.objects.annotate(
    search=SearchVector('title', weight='A') +
           SearchVector('content', weight='B') +
           SearchVector('tags', weight='C')
).filter(search='community')

# Ranked search results
query = SearchQuery('community assessment')
vector = SearchVector('title', weight='A') + SearchVector('content', weight='B')

results = Document.objects.annotate(
    rank=SearchRank(vector, query)
).filter(rank__gte=0.3).order_by('-rank')

# Search with headlines (snippets)
results = Document.objects.annotate(
    search=SearchVector('content'),
    headline=SearchHeadline('content', query)
).filter(search=query)
```

**Precomputed search vectors:**
```python
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex

class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector'])
        ]

# Update search vector in save method
def save(self, *args, **kwargs):
    self.search_vector = (
        SearchVector('title', weight='A') +
        SearchVector('content', weight='B')
    )
    super().save(*args, **kwargs)
```

## PostgreSQL Indexes

Advanced indexing for performance.

**GIN Index (Generalized Inverted Index):**
```python
from django.contrib.postgres.indexes import GinIndex

class AssessmentResponse(models.Model):
    responses = models.JSONField()
    languages = ArrayField(models.CharField(max_length=50), default=list)

    class Meta:
        indexes = [
            GinIndex(fields=['responses']),
            GinIndex(fields=['languages']),
        ]
```

**GiST Index (Generalized Search Tree):**
```python
from django.contrib.postgres.indexes import GistIndex
from django.contrib.postgres.fields import DateRangeField

class Event(models.Model):
    name = models.CharField(max_length=200)
    date_range = DateRangeField()

    class Meta:
        indexes = [
            GistIndex(fields=['date_range'])
        ]
```

**Partial Indexes:**
```python
class WorkItem(models.Model):
    status = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [
            # Only index active records
            models.Index(
                fields=['status'],
                name='active_status_idx',
                condition=models.Q(is_active=True)
            )
        ]
```

**Expression Indexes:**
```python
from django.db.models import Index, F
from django.db.models.functions import Upper

class Community(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        indexes = [
            # Index on uppercase name for case-insensitive search
            Index(Upper('name'), name='name_upper_idx')
        ]
```

## Database Functions

PostgreSQL-specific functions in queries.

**String functions:**
```python
from django.db.models import F, Value
from django.db.models.functions import (
    Concat, Upper, Lower, Length, Substr, Replace
)

# Concatenate fields
communities = Community.objects.annotate(
    full_address=Concat(
        'barangay__name', Value(', '),
        'municipality__name', Value(', '),
        'province__name'
    )
)

# String manipulation
communities = Community.objects.annotate(
    name_upper=Upper('name'),
    name_length=Length('name')
).filter(name_length__gte=20)
```

**Date/time functions:**
```python
from django.db.models.functions import (
    ExtractYear, ExtractMonth, TruncMonth, TruncDate
)

# Extract year and month
assessments = Assessment.objects.annotate(
    year=ExtractYear('created_at'),
    month=ExtractMonth('created_at')
).values('year', 'month').annotate(count=Count('id'))

# Truncate to month for grouping
monthly_stats = Assessment.objects.annotate(
    month=TruncMonth('created_at')
).values('month').annotate(count=Count('id'))
```

**Mathematical functions:**
```python
from django.db.models import F
from django.db.models.functions import Round, Ceil, Floor

# Calculate percentages
budgets = Budget.objects.annotate(
    percent_used=Round(
        F('allocated_amount') * 100.0 / F('total_amount'),
        2
    )
)
```

## Common Pitfalls

**Pitfall 1: Not indexing JSON fields you query**
```python
# ❌ SLOW - No index on JSON field
class Model(models.Model):
    data = models.JSONField()

# Query is slow
Model.objects.filter(data__status='active')

# ✅ FAST - Add GIN index
class Model(models.Model):
    data = models.JSONField()

    class Meta:
        indexes = [GinIndex(fields=['data'])]
```

**Pitfall 2: Using JSON for frequently-queried structured data**
```python
# ❌ BAD - Status is queried frequently
class Assessment(models.Model):
    data = models.JSONField()  # Contains 'status'

# ✅ GOOD - Make it a real column
class Assessment(models.Model):
    status = models.CharField(max_length=20)
    data = models.JSONField()  # For variable/semi-structured data
```

**Pitfall 3: Not setting default=dict/list for JSON/Array fields**
```python
# ❌ BAD - Can cause None errors
metadata = models.JSONField()
languages = ArrayField(models.CharField(max_length=50))

# ✅ GOOD - Safe defaults
metadata = models.JSONField(default=dict)
languages = ArrayField(models.CharField(max_length=50), default=list)
```

**Pitfall 4: Full table scan with array contains**
```python
# Without GIN index, array operations are slow
# Always add GIN index for arrays you query

class Community(models.Model):
    languages = ArrayField(models.CharField(max_length=50), default=list)

    class Meta:
        indexes = [GinIndex(fields=['languages'])]
```

## OBCMS-Specific Patterns

**Geographic data with GeoJSON (no PostGIS):**
```python
class Barangay(models.Model):
    name = models.CharField(max_length=200)
    boundary = models.JSONField(
        help_text="GeoJSON boundary data",
        default=dict
    )

    class Meta:
        indexes = [GinIndex(fields=['boundary'])]

# Store GeoJSON
barangay = Barangay.objects.create(
    name="Barangay Example",
    boundary={
        "type": "Polygon",
        "coordinates": [[[120.123, 7.456], [120.124, 7.457], ...]]
    }
)

# Query by geometry type
barangays = Barangay.objects.filter(boundary__type='Polygon')
```

**Multi-language support:**
```python
class Program(models.Model):
    name_translations = models.JSONField(default=dict)
    description_translations = models.JSONField(default=dict)

# Store translations
program = Program.objects.create(
    name_translations={
        'en': 'Community Development Program',
        'fil': 'Programa sa Pag-unlad ng Komunidad',
        'mrw': 'Programa sa Pag-uswag sa Ingud'
    }
)

# Query by language
programs = Program.objects.filter(
    name_translations__en__icontains='development'
)
```

**Dynamic form responses:**
```python
class FormResponse(models.Model):
    form_template = models.ForeignKey('FormTemplate', on_delete=models.CASCADE)
    responses = models.JSONField(default=dict)

    class Meta:
        indexes = [GinIndex(fields=['responses'])]

# Flexible form responses
response = FormResponse.objects.create(
    form_template=template,
    responses={
        'question_1': 'Answer text',
        'question_2': ['option1', 'option2'],
        'question_3': 5,  # Rating
        'nested': {
            'sub_question': 'Value'
        }
    }
)
```

## Performance Tips

**Index JSON paths you query frequently:**
```python
# Create index on specific JSON path (raw SQL in migration)
from django.db import migrations

class Migration(migrations.Migration):
    operations = [
        migrations.RunSQL(
            "CREATE INDEX responses_status_idx ON myapp_assessment "
            "((responses->'status'));"
        )
    ]
```

**Batch JSON updates:**
```python
# ❌ SLOW - Individual updates
for response in responses:
    response.metadata['processed'] = True
    response.save()

# ✅ FAST - Bulk update
from django.db.models import Value
from django.db.models.functions import JSONObject

AssessmentResponse.objects.all().update(
    metadata=JSONObject(processed=Value(True))
)
```

**Use array operations wisely:**
```python
# Array contains with index is fast
communities = Community.objects.filter(
    languages__contains=['Maranao']
)  # Fast with GIN index

# Array element access is fast
communities = Community.objects.filter(
    languages__0='Maranao'
)  # Fast
```

## Related Patterns

- See [indexes.md](indexes.md) for index strategies
- See [queries.md](queries.md) for query optimization
- See [schema-design.md](schema-design.md) for when to use JSON vs columns
- See [migrations.md](migrations.md) for adding PostgreSQL features
