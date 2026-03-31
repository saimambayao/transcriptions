# Django Migrations

Migrations manage database schema changes in a version-controlled, team-friendly way.

## Table of Contents
- [Verification and Troubleshooting](#verification-and-troubleshooting)
- [Creating Migrations](#creating-migrations)
- [Running Migrations](#running-migrations)
- [Data Migrations](#data-migrations)
- [Squashing Migrations](#squashing-migrations)
- [Common Pitfalls](#common-pitfalls)
- [CSEA-Specific Patterns](#csea-specific-patterns)
- [Migration Best Practices](#migration-best-practices)
- [Related Patterns](#related-patterns)

## Verification and Troubleshooting

**Always verify migration chain before deploying:**

```bash
# Verify dependency chain
cd backend
python ../.gemini/skills/database/scripts/verify_migrations.py .

# Fix common issues (dry run first)
python ../.gemini/skills/database/scripts/fix_migrations.py . --dry-run
```

For detailed troubleshooting, see [migration-troubleshooting.md](migration-troubleshooting.md):
- Dependency chain issues (missing, circular, orphaned)
- Conflicting migrations
- Production migration strategies
- Railway deployment patterns
- Emergency recovery procedures

## Creating Migrations

```bash
# Detect model changes and create migrations
python manage.py makemigrations

# Create migration for specific app
python manage.py makemigrations myapp

# Create empty migration for custom operations
python manage.py makemigrations --empty myapp --name add_custom_index

# Show SQL for migration without running
python manage.py sqlmigrate myapp 0001
```

**Auto-detected changes:**
- Adding/removing models
- Adding/removing fields
- Changing field types
- Adding/removing indexes
- Adding/removing constraints

## Running Migrations

```bash
# Run all pending migrations
python manage.py migrate

# Run migrations for specific app
python manage.py migrate myapp

# Migrate to specific migration
python manage.py migrate myapp 0003

# Rollback to previous migration
python manage.py migrate myapp 0002

# Show migration status
python manage.py showmigrations

# Show unapplied migrations only
python manage.py showmigrations --plan
```

**Migration states:**
```
[X] communities.0001_initial       # Applied
[ ] communities.0002_add_field     # Not applied
```

## Data Migrations

Modify data while maintaining schema integrity.

```python
from django.db import migrations

def populate_regions(apps, schema_editor):
    """Add default regions."""
    Region = apps.get_model('common', 'Region')
    regions = [
        {'code': 'IX', 'name': 'Zamboanga Peninsula'},
        {'code': 'X', 'name': 'Northern Mindanao'},
        {'code': 'XI', 'name': 'Davao Region'},
        {'code': 'XII', 'name': 'SOCCSKSARGEN'},
    ]
    for region_data in regions:
        Region.objects.create(**region_data)

def reverse_populate_regions(apps, schema_editor):
    """Remove regions."""
    Region = apps.get_model('common', 'Region')
    Region.objects.filter(code__in=['IX', 'X', 'XI', 'XII']).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            populate_regions,
            reverse_code=reverse_populate_regions
        ),
    ]
```

**Updating existing data:**
```python
def update_community_status(apps, schema_editor):
    """Set default status for existing communities."""
    Community = apps.get_model('communities', 'Community')
    Community.objects.filter(status__isnull=True).update(status='active')

class Migration(migrations.Migration):
    dependencies = [
        ('communities', '0002_add_status_field'),
    ]

    operations = [
        migrations.RunPython(update_community_status, migrations.RunPython.noop),
    ]
```

## Squashing Migrations

Combine multiple migrations into one for performance and clarity.

```bash
# Squash migrations 0001 through 0005
python manage.py squashmigrations myapp 0001 0005

# Creates myapp/migrations/0001_squashed_0005.py
```

**When to squash:**
- Many small migrations accumulated
- Migration list is hard to navigate
- Fresh deployments are slow

**Important:** Don't squash migrations that have been deployed to production.

## Common Pitfalls

**Pitfall 1: Not creating migrations after model changes**
```python
# ❌ BAD - Changed model but didn't migrate
class Community(models.Model):
    name = models.CharField(max_length=200)
    # Added new field but forgot makemigrations
    region = models.ForeignKey('Region', on_delete=models.PROTECT)

# ✅ GOOD - Always create migration
# 1. Change model
# 2. python manage.py makemigrations
# 3. python manage.py migrate
```

**Pitfall 2: Editing applied migrations**
```python
# ❌ BAD - Editing migration that's already applied in production
# This causes migration conflicts

# ✅ GOOD - Create new migration to modify
python manage.py makemigrations --empty myapp --name fix_previous_migration
```

**Pitfall 3: Missing migration dependencies**
```python
# ❌ BAD - Migration depends on another app but not specified
class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0001_initial'),
        # Missing: ('otherapp', '0002_add_field')
    ]

# ✅ GOOD - Include all dependencies
class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0001_initial'),
        ('otherapp', '0002_add_field'),
    ]
```

**Pitfall 4: Non-reversible migrations**
```python
# ❌ BAD - Can't rollback
migrations.RunPython(forward_func)

# ✅ GOOD - Provide reverse operation
migrations.RunPython(forward_func, reverse_func)
```

## CSEA-Specific Patterns

**Organization data seeding:**
```python
def create_csea_organization(apps, schema_editor):
    """Create CSEA organization."""
    Organization = apps.get_model('tenant', 'Organization')
    User = apps.get_model('auth', 'User')

    # Create organization
    csea = Organization.objects.create(
        code='CSEA',
        name='Cooperative and Social Enterprise Authority',
        is_active=True
    )

    # Create admin user
    admin = User.objects.create_superuser(
        username='csea_admin',
        email='admin@csea.gov.ph',
        password='change_me_immediately'
    )

    # Link user to organization
    admin.profile.organization = csea
    admin.profile.save()

class Migration(migrations.Migration):
    dependencies = [
        ('tenant', '0001_initial'),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_csea_organization, migrations.RunPython.noop),
    ]
```

**Geographic data migration:**
```python
def populate_geographic_hierarchy(apps, schema_editor):
    """Populate regions, provinces, municipalities."""
    import json
    from pathlib import Path
    
    Region = apps.get_model('common', 'Region')
    Province = apps.get_model('common', 'Province')
    Municipality = apps.get_model('common', 'Municipality')
    
    # Load data file
    data_file = Path(__file__).parent / 'data' / 'geography.json'
    with open(data_file) as f:
        data = json.load(f)
    
    for region_data in data['regions']:
        region = Region.objects.create(
            code=region_data['code'],
            name=region_data['name']
        )
        
        for prov_data in region_data['provinces']:
            province = Province.objects.create(
                region=region,
                name=prov_data['name']
            )
            
            for mun_data in prov_data['municipalities']:
                Municipality.objects.create(
                    province=province,
                    name=mun_data['name']
                )

class Migration(migrations.Migration):
    operations = [
        migrations.RunPython(
            populate_geographic_hierarchy,
            migrations.RunPython.noop
        ),
    ]
```

**Fixing data inconsistencies:**
```python
def fix_orphaned_communities(apps, schema_editor):
    """Fix communities with deleted organizations."""
    Community = apps.get_model('communities', 'Community')
    Organization = apps.get_model('common', 'Organization')
    
    # Get default organization
    default_org = Organization.objects.filter(code='OOBC').first()
    if not default_org:
        return
    
    # Fix orphaned communities
    Community.objects.filter(organization__isnull=True).update(
        organization=default_org
    )

class Migration(migrations.Migration):
    operations = [
        migrations.RunPython(fix_orphaned_communities, migrations.RunPython.noop),
    ]
```

## Migration Best Practices

**1. Test migrations locally before deploying**
```bash
# Test forward migration
python manage.py migrate myapp

# Test rollback
python manage.py migrate myapp 0002  # Previous migration

# Test forward again
python manage.py migrate myapp
```

**2. Use atomic migrations for data changes**
```python
from django.db import migrations, transaction

def update_data(apps, schema_editor):
    with transaction.atomic():
        # All changes succeed or all fail
        Model.objects.filter(status='old').update(status='new')

class Migration(migrations.Migration):
    atomic = True  # Default, but explicit is better
    operations = [
        migrations.RunPython(update_data),
    ]
```

**3. Add indexes in separate migrations**
```python
# Migration 1: Add field (fast)
class Migration(migrations.Migration):
    operations = [
        migrations.AddField('community', 'status', models.CharField(max_length=20)),
    ]

# Migration 2: Add index (can be slow on large tables)
class Migration(migrations.Migration):
    operations = [
        migrations.AddIndex('community', models.Index(fields=['status'])),
    ]
```

**4. Handle nullable fields carefully**
```python
# Adding non-null field requires multiple steps

# Step 1: Add nullable field
migrations.AddField('community', 'region', models.ForeignKey(..., null=True))

# Step 2: Populate field (data migration)
migrations.RunPython(populate_region_field)

# Step 3: Make field non-nullable
migrations.AlterField('community', 'region', models.ForeignKey(..., null=False))
```

**5. Document complex migrations**
```python
class Migration(migrations.Migration):
    """
    This migration consolidates the community status field.
    
    Previous behavior: status stored in JSON field
    New behavior: status as dedicated CharField
    
    Data transformation: Extracts 'status' from JSON 'metadata' field
    and populates new 'status' field.
    """
    operations = [...]
```

## Related Patterns

- See [schema-design.md](schema-design.md) for model design decisions
- See [constraints.md](constraints.md) for adding database constraints
- See [indexes.md](indexes.md) for index strategies
- See [postgresql-features.md](postgresql-features.md) for PostgreSQL-specific migrations
