---
name: security
description: Security implementation for Bangsamoro Development Platform (Next.js 16 + Django Ninja) including authentication, authorization, multi-tenant data isolation, input validation, CSRF/XSS prevention, and API security. Use when implementing security features, fixing vulnerabilities, handling sensitive data, or securing API endpoints. Integrates with /backend for auth patterns and /coditor for security audits.
argument-hint: "[topic]"
---

# Security Implementation - Bangsamoro Development Platform

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's security request                         ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

Comprehensive guidance for securing the Bangsamoro multi-portal system with Next.js frontend and Django Ninja backend.

## Tech Stack

**Frontend:**
- Next.js 16+ (App Router, Server/Client Components)
- React 19+
- TypeScript (type safety)
- TanStack Query (data fetching)

**Backend:**
- Django 6.0 + Django Ninja (API framework)
- PostgreSQL 18
- JWT authentication

**Architecture:**
- Three-portal system (Public, C/SE Portal, CSEA Staff)
- Multi-tenant (organization-scoped data)
- Role-based access control

## When to Use This Skill

- Implementing user authentication and login systems
- Designing role-based access control and permissions
- Ensuring multi-tenant data isolation
- Protecting sensitive business information
- Preventing XSS attacks in React components
- Handling CSRF protection for API calls
- Implementing API authentication (JWT)
- Securing file uploads
- Conducting security audits
- Meeting compliance requirements

## Reference Navigation

### Authentication

**JWT Authentication** - Token-based authentication for API access, token refresh, secure storage. See [references/jwt-auth.md](references/jwt-auth.md) when implementing API authentication.

**Session Security** - Next.js middleware for route protection, session management. See [references/session-security.md](references/session-security.md) when protecting routes or managing sessions.

**Password Security** - Password policies, strength validation, secure storage. See [references/passwords.md](references/passwords.md) when implementing password requirements.

### Authorization

**Role-Based Access Control** - User roles, permission checking, portal access. See [references/rbac.md](references/rbac.md) when implementing role-based permissions.

**API Permissions** - Django Ninja permission classes, endpoint protection. See [references/api-permissions.md](references/api-permissions.md) when securing API endpoints.

**Multi-Tenant Isolation** - Organization-scoped data, preventing cross-tenant access. See [references/multi-tenant.md](references/multi-tenant.md) when implementing tenant data isolation.

### Data Protection

**Input Validation** - Pydantic schemas, frontend validation, sanitization. See [references/input-validation.md](references/input-validation.md) when handling user input.

**XSS Prevention** - React security patterns, sanitizing content. See [references/xss-prevention.md](references/xss-prevention.md) when displaying user-generated content.

**CSRF Protection** - API token handling, secure requests. See [references/csrf-protection.md](references/csrf-protection.md) when making API requests.

### API Security

**Secure API Design** - Django Ninja security patterns, rate limiting. See [references/api-security.md](references/api-security.md) when designing secure APIs.

**File Upload Security** - Validation, storage, serving files securely. See [references/file-security.md](references/file-security.md) when handling file uploads.

## Quick Reference

### Authentication Flow

```
1. User submits credentials → Frontend
2. Frontend calls /api/auth/login → Django Ninja
3. Django Ninja validates → Returns JWT tokens
4. Frontend stores tokens → httpOnly cookies or secure storage
5. Frontend includes token in API requests → Authorization header
6. Django Ninja validates token → Processes request
```

### Frontend Security Patterns

**Protected Routes (Next.js Middleware):**
```typescript
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('access_token');
  const isAuthRoute = request.nextUrl.pathname.startsWith('/portal');

  if (isAuthRoute && !token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/portal/:path*', '/csea/:path*'],
};
```

**Secure API Calls:**
```typescript
// lib/api/client.ts
const apiClient = {
  async get(url: string) {
    const token = getAccessToken();
    const response = await fetch(`${API_BASE}${url}`, {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      credentials: 'include',
    });
    return response.json();
  },
};
```

**XSS Prevention in React:**
```typescript
// SAFE: React auto-escapes
<div>{userContent}</div>

// DANGEROUS: Only if absolutely necessary
<div dangerouslySetInnerHTML={{ __html: sanitizedContent }} />

// Use DOMPurify for sanitization
import DOMPurify from 'dompurify';
const clean = DOMPurify.sanitize(dirty);
```

### Backend Security Patterns

**JWT Authentication (Django Ninja):**
```python
# api.py
from ninja import Router
from ninja.security import HttpBearer

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        user = validate_jwt_token(token)
        if user:
            return user
        return None

router = Router()

@router.get('/protected', auth=AuthBearer())
def protected_endpoint(request):
    user = request.auth
    return {'user': user.email}
```

**Multi-Tenant Data Isolation:**
```python
# CORRECT: Always filter by organization
@router.get('/cooperatives')
def list_cooperatives(request):
    return Cooperative.objects.filter(
        organization=request.auth.organization
    )

# WRONG: No organization filter (data leak!)
@router.get('/cooperatives')
def list_cooperatives(request):
    return Cooperative.objects.all()  # Exposes all orgs!
```

**Input Validation (Pydantic):**
```python
from ninja import Schema
from pydantic import validator

class CooperativeCreate(Schema):
    name: str
    registration_number: str

    @validator('name')
    def validate_name(cls, v):
        if len(v) < 3:
            raise ValueError('Name must be at least 3 characters')
        return v.strip()

    @validator('registration_number')
    def validate_registration(cls, v):
        # Sanitize and validate format
        return v.strip().upper()
```

**Permission Checking:**
```python
from functools import wraps
from ninja import Router

def require_role(*roles):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if request.auth.role not in roles:
                return {'error': 'Forbidden'}, 403
            return func(request, *args, **kwargs)
        return wrapper
    return decorator

@router.post('/admin/approve')
@require_role('csea_staff', 'admin')
def approve_registration(request, coop_id: int):
    # Only CSEA staff can approve
    pass
```

## Portal-Specific Security

### Public Portal (`/`)
- No authentication required
- Read-only public data
- Rate limiting on search endpoints
- No sensitive data exposure

### C/SE Portal (`/portal`)
- JWT authentication required
- Organization-scoped data only
- Role-based feature access
- Secure file uploads for documents

### CSEA Staff Portal (`/csea`)
- JWT authentication required
- Admin role verification
- Cross-organization data access (authorized)
- Audit logging for all actions

## Security Checklist

### Authentication
- [ ] JWT tokens with short expiry
- [ ] Refresh token rotation
- [ ] Secure token storage (httpOnly cookies)
- [ ] Password strength validation
- [ ] Account lockout after failed attempts

### Authorization
- [ ] Route protection middleware
- [ ] API endpoint permissions
- [ ] Role-based access control
- [ ] Multi-tenant data isolation

### Data Protection
- [ ] Input validation (Pydantic schemas)
- [ ] Output sanitization
- [ ] SQL injection prevention (ORM usage)
- [ ] XSS prevention (React escaping)

### API Security
- [ ] HTTPS only
- [ ] CORS configuration
- [ ] Rate limiting
- [ ] Request size limits
- [ ] Error message sanitization

### File Security
- [ ] File type validation
- [ ] Size limits
- [ ] Virus scanning (production)
- [ ] Secure storage paths

## Common Vulnerabilities to Prevent

| Vulnerability | Prevention |
|--------------|------------|
| XSS | React auto-escaping, DOMPurify |
| SQL Injection | Django ORM, parameterized queries |
| CSRF | Token-based auth, SameSite cookies |
| Data Leak | Organization filtering, permission checks |
| Auth Bypass | Middleware protection, token validation |
| File Upload | Type validation, size limits, secure paths |

## CSEA-Specific Considerations

### Multi-Tenant Isolation
Every API query must include organization filter:
```python
# All queries scoped to user's organization
Cooperative.objects.filter(organization=request.auth.organization)
```

### Portal Access Control
| Portal | Roles Allowed |
|--------|--------------|
| Public | Everyone |
| C/SE Portal | coop_manager, se_manager |
| CSEA Staff | csea_staff, admin |

### Sensitive Data
- Registration documents (encrypted storage)
- Financial reports (role-restricted)
- Member personal information (privacy compliance)

## Samples

Real-world security documentation examples from the CSEA project:

### Security Audit Report
A comprehensive security audit report covering authentication, authorization, multi-tenant isolation, input validation, API security, and more. Use this as a template for conducting security audits.

See [samples/SECURITY_AUDIT_REPORT.md](samples/SECURITY_AUDIT_REPORT.md)

### Remediation Checklist
A phased security remediation checklist tracking fixes from critical (Phase 1) through defense in depth (Phase 4). Use this format for tracking security improvements.

See [samples/REMEDIATION_CHECKLIST.md](samples/REMEDIATION_CHECKLIST.md)

**Checklist Phases:**
- Phase 1: Critical fixes (authentication, authorization, XSS, file uploads)
- Phase 2: High priority (JWT cookies, token blacklist, rate limiting, multi-tenant isolation)
- Phase 3: Security hardening (CORS, HSTS, CSP, password validation, account lockout)
- Phase 4: Defense in depth (RLS, cloud storage, monitoring, penetration testing)
