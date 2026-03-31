---
name: Safety First
description: Pre-task safety verification for Bangsamoro Development Platform development. Enforces GEMINI.md critical rules, prevents dangerous operations (unauthorized git commits, destructive database operations), verifies git status, confirms database safety, and obtains explicit approval for risky operations before execution.
disable-model-invocation: true
argument-hint: "[topic]"
---

# Safety First

**Invoke this skill at the start of EVERY task.** It prevents critical mistakes: unauthorized git commits, database destruction, and rule violations.

## Quick Start

Before starting ANY task, run this safety workflow:

```
/csea-safety
```

The workflow will:
1. Ask what you're trying to do
2. Identify risky operations in your plan
3. Verify current git/database state
4. Get explicit approvals for dangerous operations
5. Grant an approval token you can use
6. Block any unsafe command execution

## How It Works

### Phase 1: Pre-Task Confirmation

When you invoke the skill or start a task, I will:

1. **Ask what you're doing** - Understand your intent clearly
2. **Identify risky operations** - Check if your task involves:
   - Git operations (commit, push, reset)
   - Database operations (migrations, deletions, schema changes)
   - File deletions (especially source files, migrations, documentation)
   - Production deployments

### Phase 2: Git Status Check

I will run:
```bash
git status && git diff --stat && git log --oneline -5
```

And report:
- Current branch
- Staged/unstaged changes
- Recent commits
- Any uncommitted work

**Why:** Prevent accidental commits to wrong branch or on top of unintended changes.

### Phase 3: Database Safety Verification

I will check:
- Migration file status
- Pending migrations
- Railway PostgreSQL connection (if deploying)

And confirm:
- No destructive migrations pending
- Migrations tested locally before production
- Auto-migration configured for Railway deployment

**Why:** PostgreSQL database contains production data and must be protected from accidental destruction.

### Phase 4: GEMINI.md Review

I will remind you of the critical rules relevant to your task:

**CRITICAL RULES (always apply):**
- ALWAYS ask permission before committing
- NEVER push without explicit permission
- NEVER assume - follow instructions exactly
- Use icons instead of emojis
- No purple colors (use Negosyo Blue #0056D2)
- Frontend-first development approach
- Files under 1000 lines

**Task-Specific Rules:**
- If task involves **git operations** → Review git commit rules
- If task involves **database** → Review migration safety rules
- If task involves **UI changes** → Review color and styling rules
- If task involves **migrations** → Ensure auto-migration for Railway

### Phase 5: Risk Assessment & Approval

For each risky operation identified, I will ask:

**For Git Operations:**
```
This task involves: git commit
Target branch: [branch]
Changes to commit: [summary]
Do you approve? (yes/no)
```

**For Database Operations:**
```
This task involves: database migration
Action: [description]
Data impact: [preserved/modified/at-risk]
Do you approve? (yes/no)
```

**For File Deletions:**
```
This task involves: file deletion
File: [path]
Type: [source/documentation/temporary]
Reason for deletion: [must be approved explicitly]
Do you approve? (yes/no)
```

I will **NOT proceed** without explicit approval.

### Phase 6: Approval Token

Once all approvals are obtained, I will create an **approval token**:

```
APPROVED: task-name [timestamp] | operations: [list]
Token: [uuid]
```

This token proves you explicitly approved the operations. I will reference this token when executing approved operations.

## Blocked Operations

These operations are **ALWAYS BLOCKED** unless you provide explicit approval AND the approval token:

### Unauthorized Git Operations
```bash
# BLOCKED - requires explicit approval + token
git commit              # Without your "commit this" instruction
git push origin main    # Without explicit branch confirmation
git push --force        # Force push to any branch
git reset --hard        # Hard reset without approval
```

### Destructive Database Operations
```bash
# BLOCKED - requires explicit approval + token
python manage.py flush          # Wipe database
python manage.py reset_db       # Reset database
DROP TABLE ...                  # Direct SQL drops
```

### Mass File Deletion
```bash
# BLOCKED - requires listing files and explicit approval
rm -r frontend/src/     # Multiple source files
rm -r backend/apps/     # Multiple app files
rm backend/*/migrations/  # Migration files
```

### Critical Config Deletion
```bash
# BLOCKED - critical configuration
rm GEMINI.md
rm .env
rm .env.example
rm railway.toml
rm Dockerfile
```

## Approval Workflow

### Step 1: You Give Instruction

```
"I need to commit my changes to the compliance feature"
```

### Step 2: I Invoke Safety Skill

1. Identify operation: `git commit`
2. Check git status: Show what will be committed
3. Verify with GEMINI.md: Confirm you own this branch
4. **Ask for approval:**
   ```
   Files to commit:
   - frontend/src/app/(tenant)/portal/compliance/page.tsx
   - backend/apps/compliance/api.py

   Branch: staging

   Do you approve this commit? (yes/no)
   ```

### Step 3: You Approve

```
"yes, commit these changes"
```

### Step 4: I Create Token & Execute

```
APPROVED: compliance-feature-commit [2025-12-13 10:30] | git commit
Token: 550e8400-e29b-41d4-a716-446655440000

Executing: git commit -m "..."
```

## When to Invoke

**Manual invocation:**
```
/csea-safety
```

**Or explicitly before tasks:**
- Before ANY git operation
- Before ANY database migration
- Before ANY file deletion
- Before ANY production deployment to Railway

**Automatic triggers** (I should catch these):
- Detecting `git commit` in my plan
- Detecting destructive database commands
- Detecting migrations without approval
- Detecting force push attempts

## CSEA-Specific Safety Rules

### Railway Deployment Safety

1. **Auto-Migration**: Migrations run automatically on Railway deploy via Dockerfile CMD
2. **Pre-Deploy Check**: Always test migrations locally before pushing
3. **No Manual Migration**: Don't attempt `railway run python manage.py migrate` - it's automatic

### Three-Portal Architecture Safety

When modifying code, verify changes are scoped to correct portal:

| Portal | Route Group | Verify |
|--------|-------------|--------|
| Public | `(public)` | No auth-only features leaked |
| C/SE Portal | `(tenant)` | Organization-scoped data |
| CSEA Staff | `(admin)` | Admin-only features protected |

### Multi-Tenant Data Safety

When writing queries:
```python
# SAFE - Organization-scoped
Cooperative.objects.filter(organization=request.auth.organization)

# DANGEROUS - All data exposed
Cooperative.objects.all()  # BLOCKED without approval
```

### Color Safety

When writing styles:
```typescript
// SAFE - Negosyo Blue
className="bg-negosyo-blue"

// BLOCKED - Purple (check GEMINI.md)
className="bg-purple-600"  // NOT ALLOWED
```

## Reference

For the complete critical rules and detailed guidance, see:
- [Critical Rules](references/critical-rules.md) - Full GEMINI.md critical rules
- [Git Rules](references/git-rules.md) - Commit and push workflow
- [Database Rules](references/database-rules.md) - Database protection and migration rules

## Key Principles

1. **No assumptions** - Follow your instructions exactly, ask when unsure
2. **Explicit approval** - Never skip asking for permission
3. **Database protection** - PostgreSQL production data is sacred
4. **Frontend-first** - Build UI before backend integration
5. **Evidence-based** - Verify outcomes with actual evidence before claiming success
6. **No purple** - Use Negosyo Blue (#0056D2) for primary colors
7. **File size limit** - Keep files under 1000 lines

---

**Remember:** This skill blocks unsafe operations. If you can't execute something you need to do, the safety workflow will ask for explicit approval first. This is a feature, not a bug - it keeps your data and git history safe.
