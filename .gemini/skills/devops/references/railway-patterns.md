# Railway Deployment Patterns

Common Railway deployment configurations and patterns for OBCMS.

## Database Configuration

### PostgreSQL Connection Pooling

**Pattern**: Optimize database connections for Django on Railway

```python
# settings/production.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGDATABASE'),
        'USER': os.environ.get('PGUSER'),
        'PASSWORD': os.environ.get('PGPASSWORD'),
        'HOST': os.environ.get('PGHOST'),
        'PORT': os.environ.get('PGPORT', 5432),
        'CONN_MAX_AGE': 600,  # 10 minutes - reuse connections
        'CONN_HEALTH_CHECKS': True,  # Verify connections are alive
    }
}
```

**Evidence**: 🟢 High Confidence
- [Railway PostgreSQL Docs](https://docs.railway.app/databases/postgresql)
- [Django Database Docs](https://docs.djangoproject.com/en/5.2/ref/databases/#persistent-connections)

---

## Environment Variables

### Required OBCMS Variables

```bash
# Django Core
DJANGO_SETTINGS_MODULE=obc_management.settings.production
SECRET_KEY=<generated-secret-key>
DEBUG=False
ALLOWED_HOSTS=<your-railway-domain>.railway.app

# Database (Auto-set by Railway PostgreSQL)
DATABASE_URL=postgresql://...
PGDATABASE=railway
PGUSER=postgres
PGPASSWORD=...
PGHOST=...
PGPORT=5432

# Redis (Auto-set by Railway Redis)
REDIS_URL=redis://...

# Media/Static Files
MEDIA_ROOT=/app/media
STATIC_ROOT=/app/staticfiles

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=<your-email>
EMAIL_HOST_PASSWORD=<app-password>

# Celery
CELERY_BROKER_URL=${REDIS_URL}
CELERY_RESULT_BACKEND=${REDIS_URL}

# AI (if using obcAI)
GEMINI_API_KEY=<your-gemini-key>
```

**Set in Railway**:
1. Go to project → Variables
2. Add each variable
3. Redeploy to apply

---

## Build Optimization

### Railway nixpacks Configuration

Create `railway.toml`:

```toml
[build]
builder = "nixpacks"

[deploy]
startCommand = "gunicorn obc_management.wsgi:application --bind 0.0.0.0:$PORT --workers 3"
healthcheckPath = "/health/"
healthcheckTimeout = 300
restartPolicyType = "on_failure"
restartPolicyMaxRetries = 3
```

**Build Performance**:
- Use `.dockerignore` to exclude unnecessary files
- Cache Python dependencies
- Minimize installed packages

---

## Static Files

### collectstatic on Deploy

Railway automatically runs collectstatic if configured:

```python
# settings/production.py
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# WhiteNoise for serving static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # After SecurityMiddleware
    # ... other middleware
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

**Evidence**: 🟢 High Confidence
- [WhiteNoise Docs](http://whitenoise.evans.io/en/stable/)
- Railway automatically runs `python manage.py collectstatic --noinput`

---

## Gunicorn Configuration

### Production WSGI Server

```python
# gunicorn.conf.py
import multiprocessing

bind = f"0.0.0.0:{os.environ.get('PORT', 8000)}"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
max_requests = 1000  # Restart workers after 1000 requests
max_requests_jitter = 50
timeout = 30
keepalive = 2
```

**Start Command** (in railway.toml):
```toml
startCommand = "gunicorn obc_management.wsgi:application --config gunicorn.conf.py"
```

---

## Cost Optimization

### Railway Hobby Tier Limits

- **App**: $5/month base, then usage
- **PostgreSQL**: $5/month base, then usage
- **Redis**: $5/month base, then usage
- **Storage**: $0.25/GB/month
- **Bandwidth**: Included up to limits

**Optimization Strategies**:
1. Use connection pooling (reduce DB connections)
2. Enable WhiteNoise (reduce static file requests)
3. Optimize queries (reduce DB load)
4. Cache frequently accessed data (use Redis)
5. Monitor usage in Railway dashboard

**Evidence**: 🟢 High Confidence
- [Railway Pricing](https://railway.app/pricing)

---

## Monitoring

### Railway Logs

Access logs via Railway CLI:

```bash
# Install CLI
npm install -g @railway/cli

# Login
railway login

# View logs
railway logs

# Follow logs (tail -f)
railway logs --tail
```

### Application Logging

```python
# settings/production.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
```

**Evidence**: 🟢 High Confidence
- [Django Logging](https://docs.djangoproject.com/en/5.2/topics/logging/)
- Railway captures stdout/stderr

---

## Security

### HTTPS/SSL

Railway provides automatic HTTPS for all deployments.

**Configure Django**:
```python
# settings/production.py
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

**Evidence**: 🟢 High Confidence
- [Railway HTTPS Docs](https://docs.railway.app/deploy/exposing-your-app#https)
- [Django Security Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)

---

## Backup Strategy

### Automated Database Backups

Railway Pro includes automated backups. For Hobby tier, use cron jobs:

```bash
# Create backup script (scripts/backup-database.sh)
# Run via Cron job service or manually
```

**Manual Backup**:
```bash
railway run pg_dump > backup-$(date +%Y%m%d-%H%M%S).sql
```

**Evidence**: 🟡 Medium Confidence
- Railway Pro feature
- Community recommendation for Hobby tier

---

## Migration Best Practices

### Safe Migration Workflow

1. **Test Locally**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   # Test thoroughly
   ```

2. **Deploy to Staging First**:
   ```bash
   git push origin staging
   # Railway auto-deploys staging
   # Verify migrations applied successfully
   ```

3. **Backup Production DB**:
   ```bash
   railway run pg_dump > prod-backup-$(date +%Y%m%d).sql
   ```

4. **Deploy to Production**:
   ```bash
   git push origin main
   # Railway auto-deploys production
   # Monitor logs during migration
   ```

**Evidence**: 🟢 High Confidence
- Django best practices
- GEMINI.md Rule 13

---

## Common Configurations

### Multi-Environment Setup

Use Railway environments:
- **development**: Local development
- **staging**: Testing environment
- **production**: Live environment

**Environment-Specific Variables**:
- Set different `DATABASE_URL` for each environment
- Use different `SECRET_KEY` for each
- Different `ALLOWED_HOSTS` for each

**Evidence**: 🟢 High Confidence
- [Railway Environments](https://docs.railway.app/develop/environments)
