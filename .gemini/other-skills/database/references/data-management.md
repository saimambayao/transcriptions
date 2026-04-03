# Data Management

Bulk operations, imports, exports, and data maintenance for Django applications.

## Table of Contents
- [Bulk Operations](#bulk-operations)
- [Data Import](#data-import)
- [Data Export](#data-export)
- [Data Seeding](#data-seeding)
- [Common Pitfalls](#common-pitfalls)
- [OBCMS-Specific Patterns](#obcms-specific-patterns)
- [Related Patterns](#related-patterns)

## Bulk Operations

**Bulk Create:**
```python
# ❌ SLOW - Individual creates
for data in large_dataset:
    Community.objects.create(**data)

# ✅ FAST - Bulk create
communities = [Community(**data) for data in large_dataset]
Community.objects.bulk_create(communities, batch_size=1000)
```

**Bulk Update:**
```python
# Update multiple records efficiently
communities = Community.objects.filter(region__code='IX')
communities.update(status='verified')

# Bulk update with different values
from django.db.models import F

WorkItem.objects.filter(fiscal_year=2024).update(
    allocated_budget=F('allocated_budget') * 1.1
)
```

**Bulk Delete:**
```python
# Delete in batches to avoid locking
batch_size = 1000
while True:
    deleted = Community.objects.filter(
        is_active=False,
        deleted_at__lt=one_year_ago
    )[:batch_size].delete()
    
    if deleted[0] == 0:
        break
```

## Data Import

**CSV Import:**
```python
import csv
from django.db import transaction

@transaction.atomic
def import_communities(csv_file):
    reader = csv.DictReader(csv_file)
    communities = []
    
    for row in reader:
        community = Community(
            name=row['name'],
            municipality_id=row['municipality_id'],
            population=int(row['population'])
        )
        communities.append(community)
        
        if len(communities) >= 1000:
            Community.objects.bulk_create(communities)
            communities = []
    
    if communities:
        Community.objects.bulk_create(communities)
```

## Data Export

**CSV Export:**
```python
import csv
from django.http import HttpResponse

def export_communities(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="communities.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Name', 'Municipality', 'Population'])
    
    for community in Community.objects.select_related('municipality'):
        writer.writerow([
            community.name,
            community.municipality.name,
            community.population
        ])
    
    return response
```

## Data Seeding

**Management command for seeding:**
```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Seed regions
        regions = [
            {'code': 'IX', 'name': 'Zamboanga Peninsula'},
            {'code': 'X', 'name': 'Northern Mindanao'},
        ]
        for region_data in regions:
            Region.objects.get_or_create(**region_data)
```

## Common Pitfalls

**Pitfall 1: Not using transactions for imports**
```python
# ❌ BAD - Partial import on error
for row in data:
    Model.objects.create(**row)

# ✅ GOOD - All or nothing
with transaction.atomic():
    for row in data:
        Model.objects.create(**row)
```

## OBCMS-Specific Patterns

**Import geographic data:**
```python
@transaction.atomic
def import_geography(json_file):
    data = json.load(json_file)
    
    for region_data in data['regions']:
        region = Region.objects.create(**region_data)
        
        for prov_data in region_data['provinces']:
            province = Province.objects.create(
                region=region,
                **prov_data
            )
```

## Related Patterns

- See [transactions.md](transactions.md) for atomic operations
- See [queries.md](queries.md) for efficient querying
