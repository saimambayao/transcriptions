---
name: push
description: Pushes the current branch to remote with optional build verification and merge-to-main. The user triggers this skill by saying "push", "push to remote", "push my changes", or "/push". Works with any branch and any tech stack.
---

# Push - Push to Remote + Optional Merge

Pushes the current branch to its remote counterpart. Optionally runs build verification (auto-detected) and merges to main. This is for when changes are already committed -- use `/gitops` for the full stage-commit-push workflow.

**IMPORTANT:** When the user invokes `/push`, immediately execute the workflow. Do not ask for confirmation to start.

## Arguments

- `--merge` or `--merge-to-main` -- after pushing, merge the current branch into main and push main
- `--build` -- run build verification before pushing
- `--no-build` -- skip build verification even if a build system is detected
- If no flags given, auto-detect build system and ask once whether to run it

---

## Step 1: Pre-flight Check

```bash
git status
git branch --show-current
git log --oneline -3
```

Capture:
- `BRANCH` = current branch name
- Confirm there are committed changes ahead of remote (or at least no uncommitted changes blocking a push)

If there are uncommitted changes, warn the user and stop. Suggest `/gitops` or manual commit first.

---

## Step 2: Build Verification (Optional)

**Skip this step if `--no-build` was passed.**

Auto-detect the project's build system by checking for these files in the repo root (or common subdirectories):

| Indicator File | Stack | Verification Command |
|---|---|---|
| `package.json` (with `lint`/`build` scripts) | Node/JS/TS | `npm run lint && npm run build` |
| `Cargo.toml` | Rust | `cargo check && cargo test` |
| `go.mod` | Go | `go vet ./... && go test ./...` |
| `pyproject.toml` or `setup.py` or `manage.py` | Python | `python -m pytest` (or `python manage.py check && pytest` for Django) |
| `Makefile` (with `check`/`test` targets) | Make-based | `make check && make test` |
| `build.gradle` or `pom.xml` | Java/Kotlin | `./gradlew check` or `mvn verify` |

**For monorepos** (e.g., `frontend/` + `backend/` subdirectories), run checks for each detected stack.

If `--build` was passed, run verification automatically.
If no flag was passed and a build system is detected, ask the user once: "Build system detected (`<stack>`). Run verification before pushing? (yes/no)"

**On failure:** Fix errors and re-run. Do not proceed until checks pass.

---

## Step 3: Push to Remote

```bash
git push origin $BRANCH
```

If the branch has no upstream yet:

```bash
git push -u origin $BRANCH
```

If push is rejected (remote has new commits):

```bash
git pull --rebase origin $BRANCH
git push origin $BRANCH
```

Report success before proceeding.

---

## Step 4: Merge to Main (Optional)

**Only execute this step if `--merge` was passed or the user explicitly requested it.**

```bash
git checkout main
git pull origin main
git merge $BRANCH -m "Merge branch '$BRANCH' into main"
git push origin main
git checkout $BRANCH
```

**On merge conflict:**
1. List conflicting files: `git diff --name-only --diff-filter=U`
2. Resolve each conflict
3. Stage resolved files: `git add <file>`
4. Complete merge: `git commit -m "Merge branch '$BRANCH' into main"`
5. Continue with push and branch switch

---

## Step 5: Success Report

```
Push Complete

Branch: $BRANCH
Pushed to: origin/$BRANCH
Merged to main: yes/no
Current branch: $BRANCH
```

---

## Constraints

- NEVER include AI references, Co-Authored-By, or any indication of AI assistance in commits
- If uncommitted changes exist, stop and suggest committing first -- do not auto-commit (that is `/gitops` territory)
- Always end on the original working branch
- Build verification failures block the push (no bypass unless `--no-build`)
- When merge conflicts arise, resolve them properly before completing
