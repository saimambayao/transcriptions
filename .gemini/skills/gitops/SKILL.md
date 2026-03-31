---
name: gitops
description: |
  Git workflow for committing and pushing changes. Handles pull, stage, commit, and push
  with smart defaults per repo type. Use when user says "gitops", "commit and push",
  "push changes", "deploy", or wants to commit their work and sync with remote.
  Adapts automatically based on whether the repo has a build system or is markdown-only.
allowed-tools: Read, Bash, Glob, Grep
---

# GitOps — Smart Git Workflow

Commit and push changes with the right workflow for the current repo.

## Process

### 1. Detect repo type

Check if the repo has a build system:
- If `package.json` exists → **code repo** (run lint/build/test before commit)
- If no `package.json` → **docs/markdown repo** (skip build checks)

### 2. Pull first

Always pull before committing to avoid divergence:
```
git pull --rebase
```
If there are conflicts, stop and ask the user to resolve them.

### 3. For code repos only — run checks

If this is a code repo with `package.json`:
- Run lint: `npm run lint` or `pnpm lint` (whichever exists)
- Run build: `npm run build` or `pnpm build`
- Run tests: `npm test` or `pnpm test`
- If any check fails, stop and fix before committing

### 4. Stage and review

- Run `git status` to show what changed
- Run `git diff --stat` to show the scope
- Present a summary to the user
- Ask for confirmation before committing

### 5. Commit

- Draft a concise commit message based on the changes
- Never include "Co-Authored-By" or AI attribution
- Commit with the drafted message

### 6. Push

- Push to the current branch
- Report success with the commit hash and branch name

## Rules

- Never force push
- Never push to main/master without user confirmation
- If the repo uses a development branch (like `nell`), push there first, then offer to merge to main
- Always pull --rebase before pushing to avoid merge conflicts
