# Database Operation Rules

## Critical Rule: NEVER Delete db.sqlite3

**This is the user's development database. It contains real data.**

### Blocked Operations

These operations are ALWAYS blocked:

```bash
# 🚫 BLOCKED
rm db.sqlite3
rm src/db.sqlite3
rm -f db.sqlite3
rm -rf db.sqlite3
python manage.py flush         # Clears all data
python manage.py reset_db      # Custom command that deletes
```

### Why
- `db.sqlite3` is development data, not a temporary file
- User may have spent hours populating test data
- Silent deletion causes data loss
- Recovery is difficult or impossible

### If User Wants to Reset Database

User must:
1. Explicitly request reset: "I want to reset the database"
2. Confirm understanding: "Yes, I understand I will lose all data"
3. Provide reason: "Because [specific reason]"

Only after explicit approval, offer alternatives:
1. **First choice:** Fix with migrations (preserve data)
2. **Second choice:** Backup and reset (preserve old data)
3. **Last resort:** Delete and recreate (only with user approval)

## Database Operations Workflow

### Check Database Health
```bash
ls -la src/db.sqlite3
git status src/db.sqlite3
```

Report:
- File exists: ✅ or ❌
- File size
- Last modified
- Git status

### Apply Migrations
```bash
cd src
python manage.py migrate
```

After migrations:
```bash
python manage.py showmigrations
```

Report:
- Number of migrations applied
- Any migrations pending
- Any migration errors

### Create New Migrations
```bash
cd src
python manage.py makemigrations [app_name]
```

Rules:
1. Review generated migration before applying
2. Check for data loss (dropping columns, deleting fields)
3. If data loss detected:
   - Ask user before applying
   - Suggest data migration if needed
   - Provide rollback plan

### Rollback Migrations

If a migration fails:

```bash
# Show migration history
python manage.py showmigrations [app]

# Rollback specific migration
python manage.py migrate [app] [previous_migration]
```

Rules:
1. Never rollback without user permission
2. Warn about potential data issues
3. Provide recovery plan if data is at risk
4. Never delete migration files (create new ones instead)

## Pre-Migration Checklist

Before ANY migration operation:

- [ ] Backup database (optional but recommended)
- [ ] Review migration file for data impact
- [ ] Understand changes to schema
- [ ] Confirm user approval
- [ ] Run in development first
- [ ] Verify no data loss
- [ ] Document changes

## Migration Safety Patterns

### ✅ Safe Migrations
```python
# Safe: Adding optional field
field = models.CharField(null=True, blank=True)

# Safe: Adding field with default
field = models.CharField(default="value")

# Safe: Renaming field (Django handles automatically)
# field = models.CharField(name="new_name")
```

### ⚠️ Requires User Approval
```python
# Risk: Removing field (data loss)
# field = models.CharField()  # Removed

# Risk: Changing field type
# field = models.IntegerField()  # Was CharField

# Risk: Adding NOT NULL field (requires default or migration data step)
field = models.CharField(null=False)
```

### 🚫 Blocked Without Explicit Approval
```python
# Blocked: Deleting model
# class User(models.Model):  # Deleted

# Blocked: Bulk operations that modify data
# User.objects.all().delete()
# User.objects.all().update(is_active=False)
```

## Database Inspection

Before making changes, inspect current state:

```bash
# Show all tables
sqlite3 src/db.sqlite3 ".tables"

# Show schema of table
sqlite3 src/db.sqlite3 ".schema users_user"

# Show row count
sqlite3 src/db.sqlite3 "SELECT COUNT(*) FROM users_user;"

# Show recent changes
ls -la src/db.sqlite3
git log --oneline -5 -- src/db.sqlite3
```

## Backup Procedures

When user approves database changes:

1. Create backup:
   ```bash
   cp src/db.sqlite3 "backups/db-$(date +%Y%m%d-%H%M%S).sqlite3"
   ```

2. Run operation
3. Verify success
4. Keep backup for 7 days

## Error Recovery

### Migration Failed

```bash
# Show error
python manage.py showmigrations [app]

# Rollback
python manage.py migrate [app] [previous]

# Investigate
git log --oneline -5 -- src/[app]/migrations/
cat src/[app]/migrations/[failing_migration].py
```

### Database Corrupted

User options:
1. Rollback migrations
2. Restore from backup
3. Reset database (with explicit approval)

## Production Database (PostgreSQL)

For staging/production databases:

- ✅ **DO:** Use `sync_migrations` command
- ✅ **DO:** Test migrations locally first
- ✅ **DO:** Backup database before migrations
- ✅ **DO:** Have rollback plan ready
- ❌ **NEVER:** Delete production database
- ❌ **NEVER:** Run destructive commands without backup
- ❌ **NEVER:** Skip migration testing

### Production Migration Process

1. **Local Test**
   ```bash
   cd src
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Code Review**
   - Review migration file
   - Check for data impacts
   - Get user approval

3. **Commit & Deploy**
   - Commit migration
   - Deploy to staging first
   - Test in staging
   - Deploy to production

4. **Monitor**
   - Watch logs for errors
   - Have rollback plan ready
   - Verify data integrity
