# Migration Troubleshooting Guide

Comprehensive guide for diagnosing and fixing Django migration issues in Bangsamoro Development Platform.

## Table of Contents
- [Verification Workflow](#verification-workflow)
- [Dependency Chain Issues](#dependency-chain-issues)
- [Conflicting Migrations](#conflicting-migrations)
- [Production Migration Issues](#production-migration-issues)
- [Railway Deployment](#railway-deployment)
- [Emergency Recovery](#emergency-recovery)
- [Common Error Messages](#common-error-messages)

## Verification Workflow

**Always verify migrations before deploying:**

```bash
# Run verification script
cd backend
python ../scripts/verify_migrations.py .

# Check migration status
python manage.py showmigrations --plan
```

**What the verification script checks:**
- Missing dependencies
- Circular dependencies
- Orphaned migrations
- Conflicting migrations (same number)
- Invalid dependency order

## Dependency Chain Issues

### Missing Dependencies

**Symptom:**
```
django.db.migrations.exceptions.NodeNotFoundError:
Migration accounts.0005_add_roles depends on nonexistent node ('core', '0003_missing')
```

**Diagnosis:**
```bash
# Find what migrations exist
python manage.py showmigrations core

# Check if the dependency was renamed or squashed
ls backend/apps/core/migrations/
```

**Fix - Update the dependency reference:**
```python
# In accounts/migrations/0005_add_roles.py
# Change:
dependencies = [
    ('accounts', '0004_previous'),
    ('core', '0003_missing'),  # This doesn't exist
]

# To:
dependencies = [
    ('accounts', '0004_previous'),
    ('core', '0003_actual_name'),  # Use correct name
]
```

**Fix - Using the fix script:**
```bash
python scripts/fix_migrations.py backend --dry-run
# Review changes, then apply
python scripts/fix_migrations.py backend
```

### Circular Dependencies

**Symptom:**
```
CircularDependencyError: accounts.0002 -> core.0003 -> accounts.0002
```

**Diagnosis:**
```bash
# Generate dependency graph
python scripts/fix_migrations.py backend --graph=migrations.dot
dot -Tpng migrations.dot -o migrations.png
```

**Fix - Break the cycle with intermediate migration:**
```python
# Step 1: Create migration without the problematic dependency
# accounts/migrations/0002_add_user_fields.py
class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
        # Removed: ('core', '0003_organization')
    ]
    operations = [
        migrations.AddField('user', 'temp_org_id', models.IntegerField(null=True)),
    ]

# Step 2: Create data migration to link after core is ready
# accounts/migrations/0003_link_organization.py
class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0002_add_user_fields'),
        ('core', '0003_organization'),  # Now safe
    ]
    operations = [
        migrations.AlterField(
            'user', 'organization',
            models.ForeignKey('core.Organization', on_delete=models.CASCADE)
        ),
    ]
```

### Orphaned Migrations

**Symptom:**
```
Migration accounts.0003_fix not in dependency chain
```

**Diagnosis:**
```bash
# Check if migration is being tracked
python manage.py showmigrations accounts

# Look for migrations not connected to initial
python scripts/verify_migrations.py backend
```

**Fix - Add proper dependency:**
```python
# In accounts/migrations/0003_fix.py
class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0002_previous'),  # Add this
    ]
```

## Conflicting Migrations

### Multiple Migrations with Same Number

**Symptom:**
```
CommandError: Conflicting migrations detected; multiple leaf nodes in the
migration graph: (0003_add_field, 0003_add_index in accounts)
```

**Diagnosis:**
```bash
ls backend/apps/accounts/migrations/0003*
# Shows: 0003_add_field.py, 0003_add_index.py
```

**Fix - Create merge migration:**
```bash
# Django's built-in merge
python manage.py makemigrations --merge accounts

# Or use fix script
python scripts/fix_migrations.py backend --dry-run
```

**Manual merge migration:**
```python
# accounts/migrations/0004_merge.py
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0003_add_field'),
        ('accounts', '0003_add_index'),
    ]
    operations = []
```

## Production Migration Issues

### Migrations Applied in Wrong Order

**Symptom:** Data corruption or missing fields in production.

**Diagnosis:**
```sql
-- Check django_migrations table
SELECT * FROM django_migrations WHERE app = 'accounts' ORDER BY applied;
```

**Fix - Fake migrations to correct state:**
```bash
# CAUTION: Only if you know the exact state
# Mark migrations as applied without running
python manage.py migrate accounts 0005 --fake
```

### Long-Running Migrations Timing Out

**Problem:** Adding index on large table times out.

**Fix - Use concurrent index creation:**
```python
from django.db import migrations
from django.contrib.postgres.operations import AddIndexConcurrently

class Migration(migrations.Migration):
    atomic = False  # Required for concurrent operations

    operations = [
        AddIndexConcurrently(
            model_name='order',
            index=models.Index(fields=['created_at'], name='order_created_idx'),
        ),
    ]
```

### Data Migration Failing in Production

**Problem:** Data migration works locally but fails with large dataset.

**Fix - Batch the operation:**
```python
def migrate_data_in_batches(apps, schema_editor):
    Model = apps.get_model('app', 'Model')
    batch_size = 1000

    # Process in batches
    total = Model.objects.count()
    for offset in range(0, total, batch_size):
        batch = Model.objects.all()[offset:offset + batch_size]
        for obj in batch:
            obj.new_field = compute_value(obj)
            obj.save(update_fields=['new_field'])
```

## Railway Deployment

### Automatic Migrations on Deploy

**Problem:** Cannot run `railway run` commands from Southeast Asia region.

**Solution - Use release command in railway.toml:**
```toml
# backend/railway.toml
[deploy]
startCommand = "python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT"
healthcheckPath = "/health/"
healthcheckTimeout = 100
```

**Alternative - Dockerfile entrypoint:**
```dockerfile
# backend/Dockerfile
COPY backend/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

```bash
#!/bin/bash
# backend/entrypoint.sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
```

### Pre-Deploy Migration Check

**Add to CI/CD pipeline:**
```yaml
# .github/workflows/deploy.yml
- name: Check migrations
  run: |
    cd backend
    python scripts/verify_migrations.py .
    python manage.py migrate --check
```

### Handling Migration Failures in Railway

**Problem:** Deploy fails due to migration error.

**Fix workflow:**
1. Check Railway deploy logs for specific error
2. Fix migration locally
3. Test migration: `python manage.py migrate --plan`
4. Commit and redeploy

**If migration partially applied:**
```python
# Create a fix migration that handles both states
def safe_forward(apps, schema_editor):
    Model = apps.get_model('app', 'Model')
    if not hasattr(Model, 'new_field'):
        # Field doesn't exist, migration not applied
        return
    # Apply fix
    Model.objects.filter(new_field__isnull=True).update(new_field='default')
```

## Emergency Recovery

### Rolling Back Migrations

**Local rollback:**
```bash
# Rollback to specific migration
python manage.py migrate accounts 0003

# Rollback all for an app
python manage.py migrate accounts zero
```

**Production rollback (Railway):**
1. Update code with reverse migration
2. Push to trigger redeploy with rollback

### Corrupted Migration State

**Symptom:** `django_migrations` table doesn't match actual schema.

**Recovery:**
```bash
# 1. Check actual table state
python manage.py dbshell
\d table_name

# 2. Fake migrations to match actual state
python manage.py migrate app_name migration_name --fake

# 3. Or reset migrations (DANGER - data loss possible)
python manage.py migrate app_name zero --fake
python manage.py migrate app_name
```

### Database Backup Before Migration

**Always backup before risky migrations:**
```bash
# Local
pg_dump -Fc csea_db > backup_$(date +%Y%m%d_%H%M).dump

# Restore
pg_restore -d csea_db backup.dump
```

## Common Error Messages

### "Table already exists"
```
django.db.utils.ProgrammingError: relation "accounts_user" already exists
```
**Fix:** Migration tracking out of sync
```bash
python manage.py migrate accounts --fake-initial
```

### "Column does not exist"
```
django.db.utils.ProgrammingError: column accounts_user.new_field does not exist
```
**Fix:** Missing migration or migration not applied
```bash
python manage.py showmigrations accounts
python manage.py migrate accounts
```

### "Dependency on app with no migrations"
```
ValueError: The field app.Model.field was declared with a lazy reference to
'other.Model', but app 'other' isn't installed or doesn't have migrations.
```
**Fix:** Ensure app is in INSTALLED_APPS and has migrations
```bash
python manage.py makemigrations other
```

### "Inconsistent migration history"
```
django.db.migrations.exceptions.InconsistentMigrationHistory
```
**Fix:** Clean up migration state
```bash
# Check what's applied
python manage.py showmigrations

# If migration was deleted but still in DB
DELETE FROM django_migrations WHERE name = '0005_deleted';
```

## Prevention Checklist

Before creating migrations:
- [ ] Run existing migrations successfully
- [ ] Make model changes
- [ ] Create migration: `makemigrations`
- [ ] Review migration file
- [ ] Test locally: `migrate`
- [ ] Test rollback: `migrate app previous_migration`
- [ ] Test forward again: `migrate`
- [ ] Verify with script: `verify_migrations.py`
- [ ] Commit migration file

Before deploying:
- [ ] All migrations committed
- [ ] No conflicting migrations
- [ ] Dependency chain verified
- [ ] Database backed up (for risky migrations)
