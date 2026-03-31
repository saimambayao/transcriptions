# Git Operation Rules

This document defines the workflow for all git operations.

## Pre-Commit Checklist

Before ANY commit, verify:

### 1. Current Branch
```bash
git branch --show-current
```

**Rule:** Confirm the current branch is correct before committing.

### 2. Staged Changes
```bash
git diff --staged
```

**Rule:** Review all staged changes. Only commit what you intend.

### 3. Unstaged Changes
```bash
git diff
```

**Rule:** Decide whether to stage, discard, or leave unstaged.

### 4. Excluded Files
Never commit:
- ✅ `.env` or `.env.local`
- ✅ `GEMINI.md`, `AGENTS.md`, `GEMINI.md`
- ✅ Secrets or credentials
- ✅ `db.sqlite3`
- ✅ Temporary files or build artifacts

### 5. Commit Message
- Clear and descriptive
- Explain the "why" not just the "what"
- Reference related issues if applicable

## Commit Workflow

### Step 1: User Initiates
```
"I want to commit my changes"
```

### Step 2: Show Git Status
```bash
git status
git diff
```

Output:
```
Branch: staging
Staged changes:
- src/models.py
- src/views.py

Unstaged changes:
- src/utils.py
```

### Step 3: Ask for Approval
```
Ready to commit?

Branch: staging
Staged files: 2 files
Message: "Add new feature for X"

Approve? (yes/no)
```

### Step 4: Execute (After Approval)
```bash
git add [files]
git commit -m "..."
```

## Push Workflow

### Step 1: User Initiates
```
"Push to staging"
```

### Step 2: Verify Branch
```bash
git branch --show-current
git log --oneline -5
```

Output:
```
Current branch: staging
Recent commits:
- abc1234 Last commit message
- def5678 Earlier commit
```

### Step 3: Ask for Confirmation
```
Ready to push to 'staging'?

Current branch: staging
Commits to push: 3
Destination: origin/staging

Approve? (yes/no)
```

### Step 4: Execute (After Approval)
```bash
git push origin staging
```

## Special Cases: Push to Main

**CRITICAL:** Main is production. Never push to main without explicit user instruction.

### Workflow:
1. User must explicitly say "push to main"
2. Verify at least 2 commits back:
   ```bash
   git log --oneline -5
   ```
3. Confirm branch:
   ```bash
   git branch --show-current
   ```
4. Ask THREE times:
   ```
   ⚠️ PUSH TO PRODUCTION (main)

   Are you absolutely sure?
   This will update production.

   Type: "yes, push to main" to confirm
   ```
5. Only after explicit confirmation, execute:
   ```bash
   git push origin main
   ```

## Force Push - ALWAYS REQUIRES EXPLICIT APPROVAL

Never use force push without:
1. User explicitly requesting it
2. Understanding the consequences
3. Getting specific token/approval code

```bash
# BLOCKED without explicit approval
git push --force
git push --force-with-lease
```

**Approval requirement:**
```
⚠️ FORCE PUSH DETECTED

Force push rewrites git history. This is dangerous.

Why: [reason provided by user]
Branch: [target branch]
Commits affected: [number]

User must type: "FORCE: [reason]" to approve
```

## Rollback Operations - ALWAYS REQUIRES EXPLICIT APPROVAL

Rollback operations modify git history and must have explicit approval:

```bash
# BLOCKED without explicit approval
git reset --hard
git revert
git reset HEAD~
```

**Approval requirement:**
```
⚠️ ROLLBACK OPERATION DETECTED

This will modify git history and revert commits.

Operation: [git reset/revert/etc]
Target: [commit hash or HEAD~N]
Files affected: [list]

User must approve by saying: "yes, rollback"
```

## Dangerous Patterns to Block

These patterns are always blocked:

### Merge Main Into Staging
```bash
# BLOCKED - requires review
git merge main
```

Reason: Could accidentally bring production changes into staging.

### Push to Wrong Branch
```bash
# BLOCKED - prevents mistakes
git push origin staging  # while on main
```

Verify current branch before every push.

### Amend Without Review
```bash
# BLOCKED - user must review what's being amended
git commit --amend
```

## Git State Before Every Operation

Before ANY git operation, show:

```bash
# Always show this
git status
git log --oneline -3
git branch --show-current
git diff [relevant files]
```

This prevents:
- Committing to wrong branch
- Committing unintended changes
- Force pushing important commits
- Losing work via reset
