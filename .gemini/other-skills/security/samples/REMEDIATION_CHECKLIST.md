# CSEA Security Remediation Checklist

**Created:** December 13, 2025
**Status:** In Progress

Use this checklist to track security fixes. Check off items as they are completed.

---

## Phase 1: Critical Fixes (IMMEDIATE)

Must be completed before any production deployment.

### Authentication
- [x] Remove hardcoded test credentials from `frontend/src/lib/services/auth.service.ts` (lines 165-260) - **COMPLETED 2025-12-13**
- [x] Remove SECRET_KEY fallback from `backend/config/settings.py` (line 25) - **COMPLETED 2025-12-13**
- [x] Add cookie security flags to `backend/config/settings.py` - **COMPLETED 2025-12-13**
  - [x] `SESSION_COOKIE_HTTPONLY = True`
  - [x] `SESSION_COOKIE_SAMESITE = 'Lax'`
  - [x] `CSRF_COOKIE_HTTPONLY = True`
  - [x] `CSRF_COOKIE_SAMESITE = 'Lax'`

### Authorization
- [x] Add `auth=JWTAuth()` to admin router in `backend/apps/admin/api.py` (line 16) - **COMPLETED 2025-12-13**
- [x] Add admin role verification to admin endpoints - **COMPLETED 2025-12-13**
  - [x] Created `AdminAuth` class in `backend/apps/accounts/authentication.py`
  - [x] Created `TenantAuth` class for tenant-specific endpoints
  - [x] Updated admin router to use `AdminAuth`

### XSS Prevention
- [x] Install DOMPurify: `npm install dompurify @types/dompurify` - **COMPLETED 2025-12-13**
- [x] Sanitize HTML in: - **COMPLETED 2025-12-13**
  - [x] `frontend/src/app/(coop)/coop/[shortname]/profile/_components/AboutSection.tsx`
  - [x] `frontend/src/app/(se)/se/[shortname]/profile/_components/AboutSection.tsx`
  - [x] `frontend/src/app/(coop)/coop/[shortname]/product/[productId]/_components/ProductTabs.tsx`
  - [x] `frontend/src/app/(se)/se/[shortname]/product/[productId]/_components/ProductTabs.tsx`

### File Uploads
- [x] Add file type validation in `backend/apps/tenant/api/documents.py` - **COMPLETED 2025-12-13**
- [x] Add file size limits (10MB max) - **COMPLETED 2025-12-13**
- [x] Add filename sanitization (path traversal prevention) - **COMPLETED 2025-12-13**

---

## Phase 2: High Priority (Week 1)

### Authentication
- [x] Migrate JWT storage from localStorage to HttpOnly cookies - **COMPLETED 2025-12-13**
  - [x] Backend sets HttpOnly cookies on login/register
  - [x] Auth classes read tokens from cookies (with header fallback)
  - [x] Logout clears cookies and blacklists tokens
- [x] Fix token expiry mismatch - **COMPLETED 2025-12-13** (aligned to 1hr access / 7d refresh)
- [x] Implement token blacklist for logout - **COMPLETED 2025-12-13**
  - [x] Cache-based blacklist in `backend/apps/accounts/jwt_utils.py`
  - [x] Tokens checked against blacklist on every request
- [x] Add rate limiting to auth endpoints - **COMPLETED 2025-12-13**
  - [x] 5 attempts per 5 minutes per IP/email
  - [x] 15 minute lockout after max attempts

### Authorization
- [x] Create `AdminAuth` class with role verification - **COMPLETED 2025-12-13**
- [x] Create `TenantAuth` class with role verification - **COMPLETED 2025-12-13**
- [x] Add `role` claim to JWT payload in `backend/apps/accounts/jwt_utils.py` - **COMPLETED 2025-12-13**
  - [x] Added: role, is_staff, tenant_id claims
- [x] Update all admin endpoints to use `AdminAuth` - **COMPLETED 2025-12-13**
- [x] Update all tenant endpoints to use `TenantAuth` - **COMPLETED 2025-12-13**
  - [x] state.py, profile.py, products.py, members.py, storefront.py, documents.py

### Multi-Tenant Isolation
- [x] Add tenant ownership verification to `backend/apps/core/api.py` - **COMPLETED 2025-12-13**
  - [x] `/compliance/status` endpoint - Added `verify_tenant_ownership()` check
  - [x] `/compliance/deadlines` endpoint - Added `verify_tenant_ownership()` check
  - [x] `/compliance/submissions` endpoint - Added `verify_tenant_ownership()` check
  - [x] `/compliance/steps/{year}` endpoint - Added `verify_tenant_ownership()` check
  - [x] `/compliance/pesos/{year}` endpoint - Added `verify_tenant_ownership()` check
  - [x] `/dashboard/metrics` endpoint - Added `verify_tenant_ownership()` check
  - [x] `/members` endpoint - Added `verify_tenant_ownership()` check
  - [x] `/members/metrics` endpoint - Added `verify_tenant_ownership()` check
  - [x] `/members/{member_id}` endpoints - Added tenant_id filter
  - [x] `/shop/products` endpoint - Added `verify_tenant_ownership()` check
  - [x] `/shop/products/{product_id}` endpoints - Added tenant_id filter
  - [x] `/shop/orders` endpoint - Added `verify_tenant_ownership()` check
  - [x] `/shop/orders/{order_id}` endpoints - Added tenant_id filter
  - [x] `/shop/metrics` endpoint - Added `verify_tenant_ownership()` check
  - [x] `/business/profile` endpoint - Added `verify_tenant_ownership()` check
- [x] Admin API `.all()` calls reviewed - **COMPLETED 2025-12-13**
  - Admin endpoints are protected by `AdminAuth` class (role verification)
  - `.all()` calls are intentional - admins need system-wide visibility
  - No changes needed - admin oversight requires access to all data

### Input Validation
- [x] Add Pydantic schemas to admin endpoints - **COMPLETED 2025-12-13**
  - [x] `review_submission` endpoint - Added `ReviewSubmissionInput` schema
  - [x] `issue_coc` endpoint - Added `IssueCOCInput` schema with COC number format validation
  - [x] `update_finding` endpoint - Added `UpdateFindingInput` schema
- [x] Add enum validation for status fields - **COMPLETED 2025-12-13**
  - [x] `SubmissionStatus` enum: pending, under_review, approved, rejected, needs_revision
  - [x] `FindingStatus` enum: open, in_progress, resolved, closed, deferred
  - [x] `COCStatus` enum: ACTIVE, EXPIRED, SUSPENDED, REVOKED
  - [x] Added business logic validation (COC expiry must be future date)

---

## Phase 3: Security Hardening (Week 2)

### API Security
- [x] Configure strict CORS origins in production - **COMPLETED 2025-12-13**
  - [x] Dev/prod separation for CORS_ALLOWED_ORIGINS
  - [x] Explicit CORS_ALLOW_HEADERS whitelist
  - [x] Explicit CORS_ALLOW_METHODS whitelist
- [x] Add HSTS headers - **COMPLETED 2025-12-13**
  - [x] `SECURE_HSTS_SECONDS = 31536000` (1 year)
  - [x] `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
  - [x] `SECURE_HSTS_PRELOAD = True`
- [x] Add `X_FRAME_OPTIONS = 'DENY'` - **COMPLETED 2025-12-13**
- [x] Production security settings - **COMPLETED 2025-12-13**
  - [x] `SECURE_PROXY_SSL_HEADER` for Railway
  - [x] `SESSION_COOKIE_SECURE = True`
  - [x] `CSRF_COOKIE_SECURE = True`
  - [x] `SECURE_BROWSER_XSS_FILTER = True`
  - [x] `SECURE_CONTENT_TYPE_NOSNIFF = True`

### Frontend Security
- [x] Add Content Security Policy headers in `next.config.ts` - **COMPLETED 2025-12-13**
  - [x] `default-src 'self'`
  - [x] `script-src` with necessary directives for Next.js
  - [x] `style-src` for Tailwind inline styles
  - [x] `connect-src` whitelist for API endpoints
  - [x] `frame-ancestors 'none'`
- [x] Add X-Frame-Options header - **COMPLETED 2025-12-13**
- [x] Add X-Content-Type-Options header - **COMPLETED 2025-12-13**
- [x] Add Referrer-Policy header - **COMPLETED 2025-12-13**
- [x] Add X-XSS-Protection header - **COMPLETED 2025-12-13**
- [x] Add Permissions-Policy header - **COMPLETED 2025-12-13**
- [x] Disable `poweredByHeader` - **COMPLETED 2025-12-13**
- [x] Enable `reactStrictMode` - **COMPLETED 2025-12-13**

### Authentication Hardening
- [x] Strengthen password validation (12+ chars, complexity) - **COMPLETED 2025-12-13**
  - [x] Created `apps/accounts/validators.py` with custom validators:
    - `MinimumLengthValidator` (12 chars)
    - `UppercaseValidator`
    - `LowercaseValidator`
    - `DigitValidator`
    - `SpecialCharacterValidator`
    - `NoCommonPatternsValidator`
  - [x] Updated `settings.py` AUTH_PASSWORD_VALIDATORS
- [x] Add account lockout after failed attempts - **COMPLETED 2025-12-13**
  - [x] Created `apps/accounts/lockout.py` with `AccountLockout` class
  - [x] 5 failed attempts triggers 30-minute lockout
  - [x] Per-account tracking (in addition to IP-based rate limiting)
  - [x] Shows remaining attempts before lockout
- [x] Use crypto.getRandomValues() for token generation - **COMPLETED 2025-12-13**
  - [x] Created `frontend/src/lib/utils/crypto.ts` utility
  - [x] Updated `auth.service.ts` verification tokens
  - [x] Updated `auth.service.ts` user ID generation
  - [x] Updated checkout pages (coop/se) order ID generation
  - [x] Updated `CertificateIssuanceForm.tsx`
  - [x] Updated `COCIssuanceForm.tsx`

### File Upload Hardening
- [x] Validate file magic bytes (actual content) - **COMPLETED 2025-12-13**
  - [x] Created `apps/tenant/utils/file_security.py`
  - [x] Magic byte signatures for PDF, images, Office docs
  - [x] `validate_file_content()` checks actual file bytes
  - [x] Integrated into `documents.py` upload validation
- [x] Sanitize filenames properly - **COMPLETED 2025-12-13**
  - [x] `sanitize_filename_secure()` with UUID-based naming
  - [x] Dangerous character removal
  - [x] Reserved filename protection
  - [x] Path traversal prevention
  - [x] Length limits enforced
- [x] ClamAV virus scanning integration - **COMPLETED 2025-12-13**
  - [x] `ClamAVScanner` class in `file_security.py`
  - [x] Configurable via `CLAMAV_ENABLED` environment variable
  - [x] Auto-detects clamscan binary path
  - [x] Integrated into document upload flow

---

## Phase 4: Defense in Depth (Week 3-4)

### Database Security
- [ ] Implement PostgreSQL Row Level Security
- [ ] Add database-level tenant isolation

### Infrastructure
- [ ] Migrate file storage to cloud (S3/GCS)
- [ ] Enable server-side encryption for files
- [ ] Implement signed URLs for file access

### Monitoring & Auditing
- [ ] Implement security audit logging
- [ ] Set up alerting for suspicious activity
- [ ] Configure log retention policies

### Testing
- [ ] Conduct penetration testing
- [ ] Add security integration tests
- [ ] Test cross-tenant isolation

---

## Quick Commands

### Install Security Dependencies

```bash
# Frontend
cd frontend
npm install dompurify @types/dompurify

# Backend
cd backend
pip install django-ratelimit python-magic
```

### Critical Code Fixes

**1. Fix Admin Router (backend/apps/admin/api.py:16)**
```python
# Change:
router = Router(tags=['Admin'])
# To:
router = Router(tags=['Admin'], auth=JWTAuth())
```

**2. Remove SECRET_KEY Fallback (backend/config/settings.py:25)**
```python
# Change:
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-...')
# To:
SECRET_KEY = os.environ['SECRET_KEY']  # Will fail if not set
```

**3. Add Cookie Security (backend/config/settings.py)**
```python
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = 'Lax'
```

**4. Sanitize HTML (frontend components)**
```typescript
import DOMPurify from 'dompurify';

// Before:
<div dangerouslySetInnerHTML={{ __html: content }} />

// After:
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(content) }} />
```

---

## Sign-Off

| Phase | Completed By | Date | Verified By |
|-------|--------------|------|-------------|
| Phase 1 | Gemini CLI | 2025-12-13 | Pending |
| Phase 2 (Auth) | Gemini CLI | 2025-12-13 | Pending |
| Phase 2 (Multi-Tenant) | Gemini CLI | 2025-12-13 | Pending |
| Phase 2 (Input Validation) | Gemini CLI | 2025-12-13 | Pending |
| Phase 3 (API Security) | Gemini CLI | 2025-12-13 | Pending |
| Phase 3 (Frontend Security) | Gemini CLI | 2025-12-13 | Pending |
| Phase 3 (Auth Hardening) | Gemini CLI | 2025-12-13 | Pending |
| Phase 3 (File Upload) | Gemini CLI | 2025-12-13 | Pending |
| Phase 4 | | | |

**Final Security Review:** _________________ Date: _______
