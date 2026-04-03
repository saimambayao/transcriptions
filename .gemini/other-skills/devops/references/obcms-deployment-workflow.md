# OBCMS Deployment Workflow

Step-by-step deployment guide for OBCMS on Railway.

**IMPORTANT**: This is GUIDANCE ONLY. You execute all commands manually.

## Pre-Deployment Checklist

Reference: `docs/claude/checklists/pre-deployment.md` (50+ items)

### Critical Items

1. **Code Quality**
   - [ ] Run `coditor` comprehensive audit
   - [ ] Fix all Critical findings
   - [ ] Fix all High findings
   - [ ] Document Medium/Low findings

2. **Tests**
   - [ ] All unit tests passing (`pytest`)
   - [ ] All integration tests passing
   - [ ] Test coverage > 80%
   - [ ] No test warnings

3. **Database Safety** (GEMINI.md Rule 13)
   - [ ] Backup production database
   - [ ] Review all migration files
   - [ ] No data deletion without explicit backup
   - [ ] Test migrations on staging first

4. **Environment Variables**
   - [ ] All required env vars set in Railway
   - [ ] No secrets in codebase (coditor checks this)
   - [ ] `DJANGO_SETTINGS_MODULE` correct
   - [ ] `ALLOWED_HOSTS` includes Railway domain

5. **Static Files**
   - [ ] `python manage.py collectstatic` runs without errors
   - [ ] WhiteNoise configured correctly

6. **Git Status**
   - [ ] All changes committed
   - [ ] No uncommitted files
   - [ ] Branch is up to date

---

## Deployment to Staging

**Purpose**: Test changes in production-like environment before production deployment.

### Steps

1. **Verify Staging Environment**
   ```bash
   # Check Railway project
   railway status

   # Verify you're on staging environment
   railway environment
   # Should show: staging
   ```

2. **Push to Staging Branch**
   ```bash
   # Commit your changes (if not already)
   git add .
   git commit -m "Your commit message"

   # Push to staging
   git push origin staging
   ```

3. **Monitor Deployment**
   ```bash
   # Watch logs during deployment
   railway logs --tail

   # Look for:
   # - Build completion
   # - Migration execution
   # - Server start
   ```

4. **Verify Deployment Success**
   - Visit staging URL: `https://your-app-staging.railway.app`
   - Check health endpoint: `/health/`
   - Test critical user flows
   - Verify migrations applied: `railway run python manage.py showmigrations`

5. **Test Thoroughly**
   - Test new features
   - Test existing features (regression)
   - Check database changes
   - Monitor logs for errors

---

## Deployment to Production

**⚠️ CRITICAL**: Only deploy after staging verification.

### Steps

1. **Final Pre-Deployment Checks**
   ```bash
   # Verify staging is working
   # Verify all tests pass on staging
   # Verify database backup exists
   ```

2. **Backup Production Database**
   ```bash
   # Use helper script (review before running)
   ./scripts/backup-database.sh production

   # Or manually:
   railway environment production
   railway run pg_dump > prod-backup-$(date +%Y%m%d-%H%M%S).sql
   ```

3. **Switch to Production Environment**
   ```bash
   railway environment production
   railway status
   ```

4. **Deploy to Production**
   ```bash
   # Push to main branch (triggers Railway deployment)
   git push origin main
   ```

5. **Monitor Deployment Closely**
   ```bash
   # Watch logs
   railway logs --tail

   # Monitor for:
   # - Build errors
   # - Migration errors
   # - Application start errors
   # - Runtime errors (first 10 minutes)
   ```

6. **Post-Deployment Verification**
   ```bash
   # Use verification script (review before running)
   ./scripts/verify-deployment.sh production

   # Or manually verify:
   # - Visit production URL
   # - Check health endpoint
   # - Test critical flows
   # - Monitor error rates
   # - Check database migrations applied
   ```

7. **Monitor for 10 Minutes**
   - Watch error rates in logs
   - Test critical endpoints
   - Monitor database connections
   - Check Celery tasks (if applicable)

---

## Rollback Procedures

**When to Rollback**:
- Application not starting
- Critical errors in production
- Database migration failed
- Unexpected behavior

### Method 1: Railway Dashboard Rollback

1. Go to Railway Dashboard → Deployments
2. Find previous successful deployment
3. Click "Redeploy"
4. Monitor logs

### Method 2: Git Rollback

```bash
# Revert last commit
git revert HEAD
git push origin main

# Or reset to specific commit (⚠️ DANGEROUS)
git reset --hard <previous-commit-sha>
git push --force origin main  # Use with extreme caution
```

### Method 3: Database Rollback (if needed)

```bash
# Only if migrations ran and failed
railway environment production
railway run psql < prod-backup-YYYYMMDD-HHMMSS.sql
```

**Evidence**: 🟢 High Confidence
- [Railway Deployments](https://docs.railway.app/guides/deployments)

---

## Environment-Specific Configurations

### Development (Local)

```bash
# Use local SQLite database
DJANGO_SETTINGS_MODULE=obc_management.settings.development
DEBUG=True
```

### Staging (Railway)

```bash
# Railway environment: staging
DJANGO_SETTINGS_MODULE=obc_management.settings.production
DEBUG=False
ALLOWED_HOSTS=your-app-staging.railway.app
```

### Production (Railway)

```bash
# Railway environment: production
DJANGO_SETTINGS_MODULE=obc_management.settings.production
DEBUG=False
ALLOWED_HOSTS=your-app.railway.app,your-custom-domain.com
```

---

## Deployment Frequency

**Recommended**:
- **Staging**: Deploy daily or per feature completion
- **Production**: Deploy weekly or bi-weekly

**Best Practices**:
- Small, incremental deployments
- Deploy during low-traffic hours
- Have team available during production deploys
- Never deploy on Fridays (avoid weekend emergencies)

**Evidence**: 🟡 Medium Confidence
- Industry best practice
- DevOps community recommendations

---

## Monitoring Post-Deployment

### First 10 Minutes (Critical)

```bash
# Watch logs continuously
railway logs --tail

# Look for:
# - Error rate spikes
# - Database connection errors
# - 500/503 errors
# - Slow response times
```

### First Hour

- Check error rates in Railway metrics
- Verify user reports (if any)
- Monitor database performance
- Check Celery task execution

### First 24 Hours

- Monitor overall health
- Compare metrics to pre-deployment baseline
- Watch for gradual degradation

---

## Emergency Contacts

**If deployment fails**:

1. **Check Railway Status**: https://status.railway.app/
2. **Check Logs**: `railway logs --tail`
3. **Rollback if Critical**: Use procedures above
4. **Get Help**: Railway Discord or GitHub issues

---

**Remember**: This workflow provides GUIDANCE. You execute all commands manually after reviewing them.
