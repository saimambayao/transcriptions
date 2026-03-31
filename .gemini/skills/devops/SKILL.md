---
name: devops
description: DevOps expert for Bangsamoro Development Platform deployment workflows. Railway deployment specialist (current platform) with troubleshooting, documentation research, and best practices. Evidence-based recommendations with source citations and confidence ratings. Use for Railway deployment issues, pre-deployment workflows, environment configuration, Docker configuration, and infrastructure optimization. Integrates with /build for pre-deploy checks and /database for migration workflows.
argument-hint: "[topic]"
---

# DevOps - CSEA Deployment Expert

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's DevOps request                           ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

Comprehensive DevOps guidance for Bangsamoro Development Platform deployment workflows with Railway expertise.

## Overview

The DevOps skill provides:

- **Railway Deployment Expertise**: Troubleshooting, optimization, best practices
- **Live Documentation Research**: Real-time Railway docs, GitHub issues, community solutions
- **CSEA Integration**: Pre-deployment checklists, environment configuration
- **Evidence-Based Recommendations**: All advice cites authoritative sources with confidence ratings

## CRITICAL: Guidance Only, No Auto-Deployment

**This skill provides GUIDANCE and RECOMMENDATIONS only. It will NEVER**:

- Automatically commit code to git
- Automatically push to GitHub/Railway
- Automatically deploy to staging or production
- Execute deployment scripts without explicit instruction

**This skill WILL**:

- Explain deployment procedures step-by-step
- Provide helper scripts for YOU to review and run manually
- Research Railway issues and provide solutions
- Guide you through pre-deployment checklists
- Recommend best practices with evidence

## Tech Stack

**Frontend Deployment:**
- Next.js 16+ (Docker container)
- Static assets via Next.js build

**Backend Deployment:**
- Django 6.0 + Django Ninja (Docker container)
- PostgreSQL 18 (Railway managed)

**Platform:**
- Railway (Docker-based deployment)
- GitHub Actions (CI/CD)

## When to Use DevOps

### Railway Deployment

- "Railway deployment failed"
- "Next.js build error on Railway"
- "Database migration error on Railway"
- "503 errors after deploying"
- "Environment variables not working"
- "How to rollback Railway deployment"

### Pre-Deployment Workflow

- "Ready to deploy to staging"
- "Deploy to production"
- "Run pre-deployment checklist"
- "Verify environment configuration"

### Infrastructure Issues

- "Database backup before migration"
- "Slow query performance in production"
- "Static file serving issues"

## Evidence-Based Recommendations

### Confidence Rating System

| Rating | Criteria | Example Source |
|--------|----------|----------------|
| **High** | Official documentation | Railway docs, Next.js docs, Django docs |
| **Medium** | Verified community solutions | Railway GitHub issues, Stack Overflow |
| **Low** | Experimental approaches | Blog posts, forum discussions |

## Railway Deployment Workflows

### Workflow 1: Frontend Deployment (Next.js)

**Dockerfile Configuration:**
```dockerfile
# frontend/Dockerfile
FROM node:22-alpine AS builder
WORKDIR /app
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ .
RUN npm run build

FROM node:22-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static
COPY --from=builder /app/public ./public
EXPOSE 8080
CMD ["node", "server.js"]
```

**Environment Variables (Railway):**
```env
NODE_ENV=production
NEXT_PUBLIC_API_URL=https://api.csea.bangsamoro.site
PORT=8080
```

### Workflow 2: Backend Deployment (Django Ninja)

**Dockerfile Configuration:**
```dockerfile
# backend/Dockerfile
FROM python:3.14-slim
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ .
RUN python manage.py collectstatic --noinput
EXPOSE 8080
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8080"]
```

**Environment Variables (Railway):**
```env
DATABASE_URL=${{Postgres.DATABASE_URL}}
SECRET_KEY=<generated-secret>
ALLOWED_HOSTS=api.csea.bangsamoro.site
DJANGO_SETTINGS_MODULE=config.settings
```

**Auto-Migration on Deploy:**
```dockerfile
# Add to Dockerfile CMD
CMD python manage.py migrate --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:8080
```

### Workflow 3: Pre-Deployment Checklist

**Before deploying:**

1. **Code Quality**
   - [ ] All tests passing
   - [ ] No TypeScript errors (`npm run build`)
   - [ ] No lint errors
   - [ ] Code reviewed

2. **Environment Configuration**
   - [ ] All env vars set in Railway
   - [ ] No secrets in codebase
   - [ ] API URLs correct

3. **Database**
   - [ ] Migrations created (`makemigrations`)
   - [ ] Migrations tested locally
   - [ ] Database backup taken

4. **Frontend Build**
   - [ ] `npm run build` succeeds
   - [ ] No build warnings
   - [ ] Static assets generated

5. **Deployment**
   - [ ] Git changes committed
   - [ ] Branch pushed to GitHub
   - [ ] Railway auto-deploy triggered

### Workflow 4: Railway Troubleshooting

**Build Failures:**

| Error | Cause | Fix |
|-------|-------|-----|
| `npm ci` fails | Package lock mismatch | Delete `node_modules`, run `npm install` |
| TypeScript errors | Type issues | Fix types locally first |
| Python deps fail | Version conflict | Check `requirements.txt` versions |

**Runtime Errors:**

| Error | Cause | Fix |
|-------|-------|-----|
| 503 Service Unavailable | App crashed | Check Railway logs |
| 502 Bad Gateway | App not starting | Check PORT and CMD |
| Database connection error | Wrong DATABASE_URL | Verify Railway Postgres URL |

**Common Fixes:**

```bash
# Check Railway logs
railway logs --tail 200

# Restart service
railway service restart

# Force redeploy
railway up --detach
```

## CSEA Deployment Architecture

```
GitHub Repository
       │
       ▼
┌──────────────────┐
│   GitHub Push    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Railway Auto-   │
│    Deploy        │
└────────┬─────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌────────┐ ┌────────┐
│Frontend│ │Backend │
│Next.js │ │Django  │
│:8080   │ │:8080   │
└───┬────┘ └───┬────┘
    │          │
    │          ▼
    │     ┌────────┐
    │     │Postgres│
    │     │Database│
    │     └────────┘
    │
    ▼
┌────────────────────┐
│csea.bangsamoro.site│
└────────────────────┘
```

## Environment Variables Reference

### Frontend (Next.js)

| Variable | Required | Description |
|----------|----------|-------------|
| `NODE_ENV` | Yes | `production` |
| `NEXT_PUBLIC_API_URL` | Yes | Backend API URL |
| `PORT` | Yes | `8080` (Railway default) |

### Backend (Django)

| Variable | Required | Description |
|----------|----------|-------------|
| `DATABASE_URL` | Yes | PostgreSQL connection string |
| `SECRET_KEY` | Yes | Django secret key |
| `ALLOWED_HOSTS` | Yes | Comma-separated domains |
| `DJANGO_SETTINGS_MODULE` | Yes | `config.settings` |
| `DEBUG` | No | `False` in production |

## Best Practices

### 1. Always Backup Before Migrations

Never run migrations in production without a database backup.

**Evidence**: High Confidence
- Source: Django Deployment Checklist

### 2. Test Builds Locally First

Always run `npm run build` and `python manage.py check` before pushing.

**Evidence**: High Confidence
- Source: Best practice

### 3. Monitor First 10 Minutes After Deployment

Watch for error spikes, connection issues, or performance degradation.

**Evidence**: Medium Confidence
- Source: Industry best practice

### 4. Use Environment Variables for Secrets

Never hardcode secrets, API keys, or credentials in codebase.

**Evidence**: High Confidence
- Source: 12-Factor App methodology

## Troubleshooting Quick Reference

| Issue | Quick Fix |
|-------|-----------|
| Build failure | Check `railway logs`, fix locally first |
| Migration error | Verify migration files, test on staging |
| 503 errors | Check app logs, verify PORT config |
| Env var missing | Verify Railway dashboard settings |
| Database connection | Check DATABASE_URL format |
| Static files 404 | Verify collectstatic ran, check paths |

## Limitations

DevOps skill provides:
- Railway troubleshooting and optimization
- CSEA deployment workflow guidance
- Evidence-based recommendations

DevOps skill does NOT provide:
- Automatic deployments
- Full CI/CD pipeline implementation
- Terraform/IaC templates
- Security compliance certifications
