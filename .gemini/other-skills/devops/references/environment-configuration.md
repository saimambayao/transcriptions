# Environment Configuration

Managing environment variables and secrets for OBCMS deployment.

## Required Environment Variables

### Django Core

```bash
# Settings module
DJANGO_SETTINGS_MODULE=obc_management.settings.production

# Secret key (generate with: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
SECRET_KEY=your-secret-key-here

# Debug mode (NEVER True in production!)
DEBUG=False

# Allowed hosts (comma-separated)
ALLOWED_HOSTS=your-app.railway.app,your-domain.com
```

### Database (Auto-set by Railway)

```bash
DATABASE_URL=postgresql://user:password@host:port/database
PGDATABASE=railway
PGUSER=postgres
PGPASSWORD=***
PGHOST=containers-us-west-xxx.railway.app
PGPORT=5432
```

### Redis (Auto-set by Railway)

```bash
REDIS_URL=redis://default:***@containers-us-west-xxx.railway.app:6379
```

### Media & Static Files

```bash
MEDIA_ROOT=/app/media
STATIC_ROOT=/app/staticfiles
STATIC_URL=/static/
MEDIA_URL=/media/
```

### Email Configuration

```bash
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password  # Not your Gmail password!
DEFAULT_FROM_EMAIL=noreply@your-domain.com
```

### Celery

```bash
CELERY_BROKER_URL=${REDIS_URL}
CELERY_RESULT_BACKEND=${REDIS_URL}
```

### AI Services (if using obcAI)

```bash
GEMINI_API_KEY=your-gemini-api-key
ZHIPU_API_KEY=your-zhipu-api-key  # Fallback
```

---

## Secret Management

### ❌ NEVER Do This

```python
# ❌ Hardcoded in settings.py
SECRET_KEY = 'hardcoded-secret-12345'
GEMINI_API_KEY = 'AIzaSy...'  # EXPOSED IN VERSION CONTROL!
```

### ✅ Always Do This

```python
# ✅ Load from environment
import os
from django.core.exceptions import ImproperlyConfigured

SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    raise ImproperlyConfigured("SECRET_KEY environment variable is required")

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
```

---

## Setting Environment Variables in Railway

### Via Dashboard

1. Go to your Railway project
2. Click on the service (e.g., "web")
3. Go to "Variables" tab
4. Click "New Variable"
5. Enter variable name and value
6. **Important**: Redeploy for changes to take effect

### Via Railway CLI

```bash
# Set single variable
railway variables set SECRET_KEY="your-secret-key"

# Set multiple variables from file
# Create .env.production (DO NOT COMMIT THIS FILE!)
railway variables set -f .env.production

# List all variables
railway variables
```

---

## Environment-Specific Settings

### Development

```python
# settings/development.py
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Staging

```python
# settings/production.py (used by staging too)
DEBUG = False
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
DATABASES = {'default': dj_database_url.config()}

# Staging-specific overrides (optional)
if os.environ.get('RAILWAY_ENVIRONMENT') == 'staging':
    # Less strict security for staging
    SECURE_SSL_REDIRECT = False
```

### Production

```python
# settings/production.py
DEBUG = False
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
DATABASES = {'default': dj_database_url.config()}

# Strict security for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

---

## Security Best Practices

### 1. Never Commit Secrets

```bash
# .gitignore
.env
.env.local
.env.production
*.key
secrets/
```

### 2. Rotate Secrets Regularly

- Change `SECRET_KEY` annually
- Rotate API keys when team members leave
- Use different keys for staging and production

### 3. Minimum Permissions

- Database users should have minimum required permissions
- API keys should have scoped permissions (not admin)

### 4. Audit Access

- Review who has access to Railway dashboard
- Log secret access (if using secret management service)

---

## Common Issues

### Missing Environment Variable

**Error**: `KeyError: 'SECRET_KEY'` or `None` value

**Fix**:
```bash
# Check variable is set
railway variables

# If missing, set it
railway variables set SECRET_KEY="your-secret"

# Redeploy
railway redeploy
```

### Wrong Variable Value

**Symptoms**: Application behaves incorrectly

**Fix**:
```bash
# Update variable
railway variables set VAR_NAME="new-value"

# Redeploy (required!)
railway redeploy
```

### Typo in Variable Name

**Symptoms**: Variable not found despite being set

**Fix**: Variables are case-sensitive!
```bash
# ❌ Wrong
railway variables set secret_key="..."  # lowercase

# ✅ Correct
railway variables set SECRET_KEY="..."  # match your code
```

---

## Environment Variable Checklist

Before deploying:

- [ ] All required variables set in Railway
- [ ] No secrets in git repository (check with `git log -S "SECRET"`)
- [ ] Different secrets for staging and production
- [ ] `DEBUG=False` in production
- [ ] `ALLOWED_HOSTS` includes Railway domain
- [ ] Email settings correct (test with: `python manage.py sendtestemail`)
- [ ] API keys valid and have required permissions
- [ ] Database URL correct (auto-set by Railway)
- [ ] Redis URL correct (auto-set by Railway)

---

## Evidence

🟢 High Confidence
- [Django Settings](https://docs.djangoproject.com/en/5.2/topics/settings/)
- [Railway Environment Variables](https://docs.railway.app/develop/variables)
- [12-Factor App Config](https://12factor.net/config)
