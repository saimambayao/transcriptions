---
name: coditor
description: Deep code auditing for Bangsamoro Development Platform. Systematically audits codebase for security vulnerabilities, TypeScript/React best practices, code quality (DRY, complexity), and architecture issues (multi-tenant, authentication). Use when auditing specific modules, performing pre-deployment audits, reviewing code quality, or checking standards compliance. Supports targeted (single module) and comprehensive (entire codebase) analysis with structured reports. Integrates with /security for vulnerability checks and /refactor for improvements.
argument-hint: "[topic]"
---

# Coditor - CSEA Code Auditor

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's code audit request                       ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

Deep, systematic code auditing for the Bangsamoro Development Platform.

## Overview

Performs comprehensive audits across:

- **Security**: Authentication, authorization, data exposure, XSS risks
- **TypeScript**: Type safety, proper typing, no `any` abuse
- **React/Next.js**: Component patterns, hooks usage, SSR/CSR boundaries
- **Code Quality**: DRY violations, complexity, test coverage
- **Architecture**: Multi-tenant isolation, portal separation, API design

## When to Use

### Manual Invocation
- "Audit the tenant portal for security issues"
- "Run comprehensive audit before deploying"
- "Check the cooperatives module for TypeScript issues"
- "Review code quality in the marketplace"

### Automatic Triggers
- "audit [module]"
- "check [app] for [security/quality]"
- "review code in [directory]"
- "pre-deployment check"

## Audit Scope Options

### Targeted Audit
Audit specific route group, component, or module.

**Examples:**
- "Audit the (tenant) portal routes"
- "Check the cooperatives service for issues"
- "Review the authentication flow"

### Comprehensive Audit
Audit entire codebase before deployment.

**Examples:**
- "Run comprehensive pre-deployment audit"
- "Audit entire frontend codebase"

## Audit Methodology

### Phase 1: Scope Identification

Determine what to audit:

| Scope | Location |
|-------|----------|
| Public Portal | `frontend/src/app/(public)/` |
| C/SE Portal | `frontend/src/app/(tenant)/` |
| CSEA Staff | `frontend/src/app/(admin)/` |
| Coop Storefronts | `frontend/src/app/(coop)/` |
| SE Storefronts | `frontend/src/app/(se)/` |
| Components | `frontend/src/components/` |
| Services | `frontend/src/lib/services/` |
| Hooks | `frontend/src/lib/hooks/` |
| Types | `frontend/src/lib/types/` |
| Backend API | `backend/apps/` |

### Phase 2: Pattern Detection

**Security Patterns (Critical/High):**

| Issue | Example | Fix |
|-------|---------|-----|
| Exposed secrets | API keys in code | Use environment variables |
| Missing auth check | Unprotected route | Add middleware auth |
| XSS vulnerability | `dangerouslySetInnerHTML` | Sanitize input |
| Data exposure | Logging sensitive data | Remove from logs |
| CORS misconfiguration | Allow all origins | Restrict origins |

**TypeScript Patterns (Medium/High):**

| Issue | Example | Fix |
|-------|---------|-----|
| `any` type abuse | `const data: any` | Define proper interface |
| Missing types | Function without return type | Add return type |
| Non-null assertion | `user!.name` | Proper null check |
| Type casting | `as unknown as Type` | Fix underlying type |

**React/Next.js Patterns (Medium/High):**

| Issue | Example | Fix |
|-------|---------|-----|
| Missing 'use client' | Client hook in server component | Add directive |
| Hydration mismatch | Date rendering in SSR | Use useEffect |
| Missing key prop | List without keys | Add unique keys |
| useEffect dependency | Missing dep in array | Add all dependencies |
| Prop drilling | Passing through 5+ levels | Use context |

**TanStack Query Patterns (Medium):**

| Issue | Example | Fix |
|-------|---------|-----|
| Missing error handling | No error state check | Add error handling |
| Incorrect query key | Dynamic value not in key | Include in key array |
| Missing invalidation | Mutation without invalidate | Add onSuccess |
| Stale closure | Old data in callback | Use fresh query data |

**Code Quality Patterns (Low/Medium):**

| Issue | Example | Fix |
|-------|---------|-----|
| DRY violation | Duplicate fetch logic | Extract to hook |
| Large component | 500+ lines | Split into smaller |
| Dead code | Unused imports | Remove |
| Magic numbers | `if (count > 10)` | Use named constant |
| Complex conditionals | Nested ternaries | Simplify or extract |

**Django Ninja Patterns (Backend):**

| Issue | Example | Fix |
|-------|---------|-----|
| Missing auth | Endpoint without auth | Add authentication |
| No org filter | Query without tenant scope | Filter by organization |
| N+1 queries | Loop with individual queries | Use prefetch |
| Missing validation | No schema validation | Add input schema |

### Phase 3: Generate Report

```markdown
# Code Audit Report

## Audit Metadata
- **Date**: [date]
- **Scope**: [targeted/comprehensive]
- **Files Audited**: [count]

## Executive Summary
- **Critical**: [count] - Immediate action required
- **High**: [count] - Fix soon
- **Medium**: [count] - Plan to fix
- **Low**: [count] - Nice to have

## Critical Findings

### [Finding 1]
- **File**: `path/to/file.tsx:line`
- **Severity**: Critical
- **Category**: Security
- **Issue**: [description]
- **Impact**: [why it matters]
- **Fix**:
```typescript
// Before
[problematic code]

// After
[fixed code]
```

## High Priority Findings
[Similar structure]

## Medium Priority Findings
[Summary with examples]

## Low Priority Findings
[Summary with examples]

## Recommendations
1. [Priority action 1]
2. [Priority action 2]
3. [Priority action 3]
```

## Severity Levels

### Critical (Fix Immediately)
- Authentication bypass
- Data exposure across tenants
- Secrets in code
- XSS vulnerabilities

**SLA**: Fix before deployment

### High (Fix Soon)
- Missing authorization checks
- TypeScript `any` in critical paths
- Missing error boundaries
- Unhandled promise rejections

**SLA**: Fix within 1 sprint

### Medium (Plan to Fix)
- Code duplication
- Missing types
- Large files (>500 lines)
- Missing tests

**SLA**: Fix within 2-3 sprints

### Low (Nice to Have)
- Minor style issues
- Documentation improvements
- Unused code

**SLA**: Fix when convenient

## Audit Checklists

### Security Checklist

- [ ] No secrets in code (API keys, passwords)
- [ ] All routes have proper authentication
- [ ] Multi-tenant isolation enforced
- [ ] No `dangerouslySetInnerHTML` without sanitization
- [ ] CORS properly configured
- [ ] Environment variables used for config
- [ ] No sensitive data in logs

### TypeScript Checklist

- [ ] No `any` types (use `unknown` if needed)
- [ ] All functions have return types
- [ ] Interfaces defined for API responses
- [ ] Props properly typed
- [ ] Enums or unions for fixed values
- [ ] No non-null assertions without validation

### React/Next.js Checklist

- [ ] Proper 'use client' / 'use server' directives
- [ ] No hydration mismatch risks
- [ ] All lists have unique keys
- [ ] useEffect has proper dependencies
- [ ] Error boundaries in place
- [ ] Loading states handled
- [ ] Proper component composition

### TanStack Query Checklist

- [ ] Query keys include all dependencies
- [ ] Error states handled
- [ ] Loading states handled
- [ ] Mutations invalidate relevant queries
- [ ] Proper staleTime configuration
- [ ] No infinite refetching

### Code Quality Checklist

- [ ] Files under 1000 lines
- [ ] No duplicate code (DRY)
- [ ] Functions under 50 lines
- [ ] Meaningful variable names
- [ ] No magic numbers
- [ ] Comments for complex logic

## CSEA-Specific Checks

### Portal Isolation
- [ ] Tenant portal doesn't expose admin data
- [ ] Public portal has no auth-required data
- [ ] Storefronts only show their own data

### Multi-Tenancy
- [ ] API calls include organization context
- [ ] Queries filter by organization
- [ ] No cross-tenant data leakage

### UI Standards
- [ ] Negosyo Blue (#0056D2) used as primary
- [ ] No purple colors
- [ ] Icons instead of emojis
- [ ] shadcn/ui components used
- [ ] Tailwind for styling

## Quick Commands

```
"Audit the tenant portal"
"Check services for TypeScript issues"
"Audit entire codebase for security"
"Review components for React patterns"
"Pre-deployment comprehensive audit"
```

## Report Output

Reports saved to:
```
docs/coditor-audits/YYYY-MM-DD-[scope]-audit.md
```

## Limitations

Coditor performs **static analysis only**. Cannot detect:
- Runtime errors (use debugger skill)
- Performance issues (use profiling)
- Logic bugs (requires testing)
- API behavior (requires integration tests)

Use alongside:
- **debugger** - Fix runtime errors
- **investigator** - Research solutions
- **featuredev** - Implement fixes
