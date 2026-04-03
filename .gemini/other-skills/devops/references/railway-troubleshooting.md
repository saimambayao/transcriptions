# Railway Troubleshooting Guide

Common Railway deployment errors and evidence-based solutions.

## Build Failures

### Error: "Python version not found"

**Symptoms**: Build fails with "Python 3.12 not found" or similar

**Solution**: 🟢 High Confidence

Create `runtime.txt` in project root:
```
python-3.12
```

**Source**: [Railway Python Docs](https://docs.railway.app/languages/python)

---

### Error: "Requirements installation failed"

**Symptoms**: `pip install -r requirements.txt` fails

**Common Causes**:
1. Conflicting dependencies
2. Missing system libraries
3. Outdated pip/setuptools

**Solution**: 🟢 High Confidence

```bash
# Locally, regenerate requirements
pip freeze > requirements/production.txt

# Or use requirements/base.txt + production.txt pattern
# Ensure all dependencies have version pins
```

**Source**: [Python Packaging](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

---

### Error: "collectstatic failed"

**Symptoms**: Static files collection fails during build

**Solution**: 🟢 High Confidence

1. Verify `STATIC_ROOT` is set:
   ```python
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   ```

2. Check `whitenoise` is installed:
   ```bash
   pip install whitenoise
   ```

3. Ensure middleware is configured:
   ```python
   MIDDLEWARE = [
       'whitenoise.middleware.WhiteNoiseMiddleware',  # After SecurityMiddleware
   ]
   ```

**Source**: [WhiteNoise Docs](http://whitenoise.evans.io/)

---

## Migration Errors

### Error: "relation already exists"

**Symptoms**: Migration fails with "relation already exists" or "duplicate column"

**Root Cause**: Migration already applied but not recorded in `django_migrations` table

**Solution**: 🟢 High Confidence

```bash
# 1. Connect to Railway PostgreSQL
railway run psql

# 2. Check applied migrations
SELECT * FROM django_migrations WHERE app = 'your_app';

# 3. Fake the migration (if it was already applied manually)
railway run python manage.py migrate your_app 0003 --fake

# 4. Redeploy
git push
```

**Source**: [Django Migrations Troubleshooting](https://docs.djangoproject.com/en/5.2/topics/migrations/#troubleshooting)

---

### Error: "Cannot add foreign key constraint"

**Symptoms**: Migration fails with foreign key constraint error

**Root Cause**: Referenced table/column doesn't exist or data integrity issue

**Solution**: 🟢 High Confidence

1. Check migration order (dependencies)
2. Verify referenced model exists
3. Check for data that violates constraint

```python
# In migration file, ensure proper dependencies:
class Migration(migrations.Migration):
    dependencies = [
        ('app1', '0002_previous_migration'),
        ('app2', '0003_referenced_model'),  # Must exist first
    ]
```

**Source**: [Django Migration Dependencies](https://docs.djangoproject.com/en/5.2/topics/migrations/#migration-files)

---

## Runtime Errors

### Error: "503 Service Unavailable"

**Symptoms**: Application returns 503 errors after deployment

**Common Causes**:
1. Application not starting (check logs)
2. Health check timeout
3. Port binding issue
4. Database connection failure

**Solution**: 🟢 High Confidence

```bash
# 1. Check Railway logs
railway logs

# 2. Common fixes:

# Fix 1: Verify PORT binding
# In gunicorn command:
gunicorn obc_management.wsgi:application --bind 0.0.0.0:$PORT

# Fix 2: Increase health check timeout
# In railway.toml:
[deploy]
healthcheckTimeout = 300  # 5 minutes

# Fix 3: Check DATABASE_URL
# Verify Railway set it automatically
railway variables
```

**Source**: [Railway Deployments](https://docs.railway.app/guides/deployments)

---

### Error: "OperationalError: FATAL: remaining connection slots are reserved"

**Symptoms**: Database connection limit exceeded

**Solution**: 🟢 High Confidence

```python
# settings/production.py

# Reduce max connections per app instance
DATABASES['default']['CONN_MAX_AGE'] = 60  # Reduce from 600

# Or upgrade PostgreSQL plan for more connections
# Railway PostgreSQL: 100 connections on Hobby tier
```

**Alternative**: Use connection pooling service (PgBouncer)

**Source**: [Railway PostgreSQL Limits](https://docs.railway.app/databases/postgresql#connection-limits)

---

### Error: "DisallowedHost at /"

**Symptoms**: 400 Bad Request with "DisallowedHost" error

**Solution**: 🟢 High Confidence

```python
# settings/production.py
ALLOWED_HOSTS = [
    'your-app.railway.app',
    'your-custom-domain.com',
    # For development with ngrok:
    '.ngrok.io',
]

# Or use environment variable
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
```

**Set in Railway**:
```bash
railway variables set ALLOWED_HOSTS=your-app.railway.app,your-domain.com
```

**Source**: [Django ALLOWED_HOSTS](https://docs.djangoproject.com/en/5.2/ref/settings/#allowed-hosts)

---

## Environment Variable Issues

### Error: Environment variable not found

**Symptoms**: KeyError or None value for environment variable

**Solution**: 🟢 High Confidence

1. **Verify in Railway Dashboard**:
   - Go to project → Variables
   - Check variable is set
   - Check spelling (case-sensitive)

2. **Use Fallbacks in Code**:
   ```python
   # Bad (crashes if not set)
   API_KEY = os.environ['API_KEY']

   # Good (provides default or raises helpful error)
   API_KEY = os.environ.get('API_KEY')
   if not API_KEY:
       raise ImproperlyConfigured("API_KEY environment variable is required")
   ```

3. **Redeploy After Setting**:
   ```bash
   # Setting env var requires redeploy
   railway redeploy
   ```

**Source**: [Railway Environment Variables](https://docs.railway.app/develop/variables)

---

## Performance Issues

### Slow Build Times

**Symptoms**: Railway build takes >5 minutes

**Solutions**: 🟡 Medium Confidence

1. **Use `.dockerignore`**:
   ```
   # .dockerignore
   venv/
   __pycache__/
   *.pyc
   .git/
   node_modules/
   db.sqlite3
   ```

2. **Minimize Dependencies**:
   - Only include production requirements
   - Remove dev dependencies from production builds

3. **Use Railway Build Cache**:
   - Railway automatically caches Python packages
   - Pinned versions cache better than ranges

**Source**: Railway community best practices

---

### Slow Application Response

**Symptoms**: Application responds slowly in production

**Common Causes**:
1. N+1 database queries
2. Missing database indexes
3. Slow external API calls
4. Insufficient workers

**Solutions**: 🟢 High Confidence

1. **Optimize Database Queries**:
   ```python
   # Use select_related for foreign keys
   tasks = Task.objects.select_related('assigned_to', 'organization')

   # Use prefetch_related for reverse foreign keys
   orgs = Organization.objects.prefetch_related('users', 'tasks')
   ```

2. **Add Database Indexes**:
   ```python
   class Task(models.Model):
       status = models.CharField(max_length=20, db_index=True)
       organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

       class Meta:
           indexes = [
               models.Index(fields=['organization', 'status']),
           ]
   ```

3. **Scale Gunicorn Workers**:
   ```toml
   # railway.toml
   [deploy]
   startCommand = "gunicorn obc_management.wsgi:application --workers 4"
   ```

**Source**: [Django Performance](https://docs.djangoproject.com/en/5.2/topics/performance/)

---

## Database Connection Issues

### Error: "connection refused" or "could not connect to server"

**Symptoms**: Application cannot connect to PostgreSQL

**Solution**: 🟢 High Confidence

1. **Verify Railway PostgreSQL is running**:
   ```bash
   railway status
   ```

2. **Check DATABASE_URL**:
   ```bash
   railway variables
   # Verify DATABASE_URL is set
   ```

3. **Test Connection Manually**:
   ```bash
   railway run psql
   # If this works, connection is fine
   ```

4. **Check Database Settings**:
   ```python
   # settings/production.py
   import dj_database_url

   DATABASES = {
       'default': dj_database_url.config(
           default=os.environ.get('DATABASE_URL'),
           conn_max_age=600,
       )
   }
   ```

**Source**: [dj-database-url](https://github.com/jazzband/dj-database-url)

---

## Redis Issues

### Error: "Connection to Redis lost"

**Symptoms**: Celery tasks fail, cache unavailable

**Solution**: 🟢 High Confidence

1. **Verify Railway Redis is running**:
   ```bash
   railway status
   ```

2. **Check REDIS_URL**:
   ```bash
   railway variables
   ```

3. **Configure Celery Properly**:
   ```python
   # settings/production.py
   CELERY_BROKER_URL = os.environ.get('REDIS_URL')
   CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL')

   # Add retry logic
   CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
   CELERY_BROKER_CONNECTION_MAX_RETRIES = 10
   ```

**Source**: [Celery Configuration](https://docs.celeryproject.org/en/stable/userguide/configuration.html)

---

## Rollback Procedures

### How to Rollback a Failed Deployment

**Steps**: 🟢 High Confidence

1. **Via Railway Dashboard**:
   - Go to Deployments tab
   - Find previous successful deployment
   - Click "Redeploy"

2. **Via Git**:
   ```bash
   # Revert to previous commit
   git revert HEAD
   git push

   # Or reset to specific commit
   git reset --hard <previous-commit-sha>
   git push --force  # ⚠️ Dangerous, use with caution
   ```

3. **Restore Database** (if migrations ran):
   ```bash
   # Restore from backup
   railway run psql < backup-file.sql
   ```

**Source**: [Railway Deployments](https://docs.railway.app/guides/deployments#rollback)

---

## Getting Help

### Where to Find Solutions

1. **Railway Docs**: https://docs.railway.app/
2. **Railway GitHub Issues**: https://github.com/railwayapp/railway/issues
3. **Railway Discord**: https://discord.gg/railway
4. **Stack Overflow**: Tag `railway` + `django`
5. **OBCMS Docs**: `docs/deployment/railway-deployment.md`

### How to Report Railway Issues

Include:
- Build/deployment logs
- Error messages (full stack trace)
- Railway project ID
- Reproduction steps
- Expected vs actual behavior

**Template**:
```
**Issue**: [Brief description]

**Environment**: Production/Staging

**Error**:
[Full error message from logs]

**Steps to Reproduce**:
1. ...
2. ...

**Expected**: [What should happen]
**Actual**: [What actually happened]

**Logs**: [Paste relevant Railway logs]
```
