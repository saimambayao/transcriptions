# Workflow Selection Quick Reference

**Purpose:** Fast decision-making for Debugger skill workflow selection

## Decision Tree

```
Error reported
    ↓
    ├─ Production/Staging? ──→ YES ──→ ULTRATHINKING (99% of cases)
    │                                    ↓
    │                                    Exception: User explicitly says
    │                                    "quick hotfix only, skip agents"
    │                                    ↓
    │                                    → 7-STEP BASIC (rare)
    │
    └─ Development/Local? ──→ YES ──→ Check characteristics:
                                       ↓
                                       ├─ Root cause obvious? ──→ NO ──→ ULTRATHINKING
                                       ├─ Affects multiple layers? ──→ YES ──→ ULTRATHINKING
                                       ├─ Requires research? ──→ YES ──→ ULTRATHINKING
                                       ├─ User says "quick fix"? ──→ NO ──→ ULTRATHINKING
                                       │
                                       └─ ALL of:
                                          • Root cause obvious ──→ YES
                                          • Single layer only
                                          • No research needed
                                          • User wants speed
                                          ↓
                                          7-STEP BASIC
```

## Quick Lookup Table

### ULTRATHINKING (Multi-Agent) - DEFAULT

**Use when error has ANY of these characteristics:**

| Category | Indicators |
|----------|-----------|
| **Environment** | Production, Staging, Railway logs, Deployment context |
| **Complexity** | Multiple users affected, Multi-layer issue, Unclear root cause, Multi-tenancy involved |
| **Severity** | Critical, Blocking, Data loss risk, Security concern |
| **Type** | PermissionDenied, IntegrityError, Migration failure, HTMX issues in production |

**Keywords that trigger Ultrathinking:**
- "production", "staging", "Railway"
- "multiple users", "all organizations"
- "critical", "urgent", "blocking"
- "PermissionDenied", "DoesNotExist" (multi-tenancy)
- "migration", "deployment"
- "not sure what's causing"

### 7-STEP BASIC - Exceptions Only

**Use ONLY when ALL of these are true:**

| Requirement | Check |
|-------------|-------|
| Environment | Development/local only ✓ |
| Clarity | Root cause obvious from error message ✓ |
| Scope | Single user, single layer ✓ |
| Request | User explicitly wants "quick fix" or "hotfix" ✓ |
| Simplicity | Typo, import, or config error ✓ |

**Examples that qualify for 7-Step Basic:**
- NameError from typo in local development
- ModuleNotFoundError from missing import
- TemplateDoesNotExist (wrong path)
- KeyError in template variable
- User: "I made a typo, quick fix please"

**If ANY requirement is false → Use Ultrathinking instead**

## Concrete Examples

### Example 1: Production 403 Error
```
Error: PermissionDenied when approving budget
Environment: Production (Railway)
Affected: Admin users in Org #2
```
**Decision:** ULTRATHINKING
- Production ✓
- Affects users ✓
- Permission system (complex) ✓
- Multi-tenancy concern ✓

### Example 2: Development Import Error
```
Error: ModuleNotFoundError: No module named 'myapp.utils'
Environment: Local development
User: "I just renamed the module, quick fix"
```
**Decision:** 7-STEP BASIC (if ALL conditions met)
- Development ✓
- Root cause obvious (renamed module) ✓
- Single layer (import) ✓
- User wants quick fix ✓
- Simple error ✓

BUT if user didn't say "quick fix" → Still use Ultrathinking (safer)

### Example 3: Staging HTMX Swap Issue
```
Error: HTMX swap not working on task deletion
Environment: Staging
User: "The UI doesn't update when I delete a task"
```
**Decision:** ULTRATHINKING
- Staging environment ✓
- UI issue affecting users ✓
- Not obvious from description ✓

### Example 4: Development Database Error
```
Error: IntegrityError: duplicate key violates unique constraint
Environment: Local development
Context: After running migrations
```
**Decision:** ULTRATHINKING
- Database integrity (complex) ✓
- Migration context ✓
- Not a simple typo ✓
- Could have broader implications ✓

## Default Decision Logic

**When in doubt, follow this priority:**

1. **Is it production/staging?** → YES → **ULTRATHINKING**
2. **Is it development?** → Check if ALL Basic conditions met → If not → **ULTRATHINKING**
3. **Still uncertain?** → **ULTRATHINKING** (comprehensive > fast)

**Golden Rule:** Ultrathinking is the safe default. 7-Step Basic is the exception.

## User Request Keywords

### Keywords that trigger Ultrathinking:
- "investigate", "debug", "find root cause"
- "production error", "staging issue"
- "users affected", "multiple organizations"
- "not sure what's wrong"
- (No specific request = Ultrathinking default)

### Keywords that allow 7-Step Basic:
- "quick fix", "hotfix", "simple typo"
- "skip the agents", "fast fix needed"
- "just a configuration error"

**BUT:** Even with these keywords, if environment is production/staging → Still use Ultrathinking

## Integration with GEMINI.md

The Debugger skill's automatic workflow selection aligns with GEMINI.md's error documentation system:

**GEMINI.md specifies:**
> ALL errors must be systematically documented using the 3-agent sequential workflow (4 phases).

**Debugger skill implementation:**
- Production/staging errors → Automatically use Ultrathinking (3-agent workflow)
- Development errors → Use 7-Step Basic only if ALL conditions met
- Documents all errors regardless of workflow

**Result:** Automatic alignment with GEMINI.md requirements for production errors.

## Confidence Check

Before activating a workflow, verify:

**For Ultrathinking:**
- [ ] Error matches at least ONE Ultrathinking trigger?
- [ ] OR uncertain which workflow to use?
→ Activate Ultrathinking

**For 7-Step Basic:**
- [ ] Error matches ALL Basic requirements?
- [ ] User explicitly wants fast fix?
- [ ] Development environment only?
→ Activate 7-Step Basic

**If checklist incomplete → Default to Ultrathinking**

## Summary

**Simple rule:**
- **Production/Staging = Ultrathinking (always)**
- **Development = Ultrathinking (default), 7-Step Basic (exceptions only)**
- **Uncertain = Ultrathinking**

**Think of it as:**
- Ultrathinking = Standard operating procedure
- 7-Step Basic = Emergency bypass (rarely used)
