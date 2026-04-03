# Database Migration Best Practices

Safe database migration patterns for OBCMS (GEMINI.md Rule 13).

## Migration Safety Checklist

Before running ANY migration in production:

- [ ] **Backup Completed**: Database backup exists and verified
- [ ] **Tested on Staging**: Migration ran successfully on staging
- [ ] **Reviewed Migration File**: Manually reviewed generated migration
- [ ] **No Data Loss**: Confirmed no data deletion without explicit backup
- [ ] **Reversible**: Can rollback if needed
- [ ] **Team Notified**: Team knows deployment is happening
- [ ] **Off-Peak Hours**: Deploying during low-traffic period

---

## Safe Migration Patterns

### ✅ SAFE: Adding New Fields

```python
# ✅ Safe - adding nullable field
class Migration(migrations.Migration):
    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
```

### ✅ SAFE: Adding New Models

```python
# ✅ Safe - new model, no dependencies on existing data
class Migration(migrations.Migration):
    operations = [
        migrations.CreateModel(
            name='TaskComment',
            fields=[...],
        ),
    ]
```

### ⚠️ CAUTION: Renaming Fields

```python
# ⚠️ Requires data migration
# Step 1: Add new field
# Step 2: Copy data (data migration)
# Step 3: Remove old field (separate deployment)
```

### ❌ DANGEROUS: Deleting Fields with Data

```python
# ❌ DANGEROUS - backup required before running
class Migration(migrations.Migration):
    operations = [
        migrations.RemoveField(
            model_name='task',
            name='old_field',  # ⚠️ Data will be lost!
        ),
    ]
```

---

## Testing Migrations

### Local Testing

```bash
# 1. Create migration
python manage.py makemigrations

# 2. Review generated file
cat src/app_name/migrations/0XXX_migration.py

# 3. Test migration
python manage.py migrate

# 4. Test rollback (if reversible)
python manage.py migrate app_name 0XXX  # Previous migration number

# 5. Re-apply
python manage.py migrate
```

### Staging Testing

```bash
# 1. Deploy to staging
git push origin staging

# 2. Monitor migration execution
railway environment staging
railway logs --tail

# 3. Verify migration applied
railway run python manage.py showmigrations

# 4. Test application functionality
# Visit staging URL, test features
```

---

## Data Migrations

### When to Use Data Migrations

- Renaming fields (copy old → new)
- Changing field types
- Populating default values
- Complex data transformations

### Example: Renaming Field

```python
# Migration 0002_rename_field_step1.py
# Step 1: Add new field
class Migration(migrations.Migration):
    operations = [
        migrations.AddField(
            model_name='task',
            name='new_status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

# Migration 0003_copy_data.py
# Step 2: Copy data
from django.db import migrations

def copy_status(apps, schema_editor):
    Task = apps.get_model('tasks', 'Task')
    for task in Task.objects.all():
        task.new_status = task.old_status
        task.save()

class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0002_rename_field_step1'),
    ]
    operations = [
        migrations.RunPython(copy_status, reverse_code=migrations.RunPython.noop),
    ]

# Migration 0004_rename_field_step3.py
# Step 3: Remove old field (separate deployment!)
class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0003_copy_data'),
    ]
    operations = [
        migrations.RemoveField(
            model_name='task',
            name='old_status',
        ),
    ]
```

**Deploy each step separately!**

---

## Migration Rollback

### Reversible Migrations

```bash
# Rollback to specific migration
railway run python manage.py migrate app_name 0XXX

# Example: Rollback last migration
railway run python manage.py migrate tasks 0002
```

### Non-Reversible Migrations

If migration deletes data, rollback requires database restore:

```bash
# Restore from backup
railway run psql < backup-file.sql
```

---

## Migration Dependencies

### Correct Dependency Order

```python
# ❌ WRONG - order matters!
class Migration(migrations.Migration):
    dependencies = [
        ('app1', '0003_later'),
        ('app2', '0001_first'),  # Should run before app1's 0003
    ]

# ✅ CORRECT
class Migration(migrations.Migration):
    dependencies = [
        ('app1', '0002_earlier'),  # Correct order
        ('app2', '0001_first'),
    ]
```

---

## Common Migration Errors

### "relation already exists"

**Cause**: Migration already applied but not recorded

**Fix**:
```bash
railway run python manage.py migrate app_name 0XXX --fake
```

### "cannot drop table - still referenced"

**Cause**: Foreign key constraint

**Fix**: Remove foreign keys first, then drop table

---

## Evidence

🟢 High Confidence
- [Django Migrations](https://docs.djangoproject.com/en/5.2/topics/migrations/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)
- GEMINI.md Rule 13
