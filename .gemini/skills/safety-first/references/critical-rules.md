# Critical Rules from GEMINI.md

These rules are non-negotiable. Violating them can cause data loss, git corruption, or incorrect commits.

## Rule 1: ALWAYS Ask Permission Before Committing

**🚨 CRITICAL: NEVER auto-commit. ALWAYS ask user for permission first.**

### Workflow
1. Make code changes
2. Show user what changed: `git status` and `git diff`
3. **WAIT for user to say "commit" or "go ahead" or "push to [branch]"**
4. Only then run `git add` and `git commit`
5. **VERIFY branch BEFORE pushing** - Always confirm target branch with user

### Critical Branch Rule
- ✅ **Staging is for testing** - Push development changes to staging first
- ✅ **Main is for production** - Only push to main after staging verification
- ❌ **NEVER push to main without explicit user approval**
- ❌ **NEVER assume which branch to push to** - ALWAYS ask or wait for instruction

### Checklist Before Every Commit
- [ ] User explicitly approved the commit (not assumed)?
- [ ] Files to be committed are correct?
- [ ] No GEMINI.md, AGENTS.md, GEMINI.md, .env, or secrets included?
- [ ] Branch is correct (staging vs main)?
- [ ] Commit message is clear and descriptive?

### If you accidentally committed to wrong branch
1. Revert immediately: `git reset --hard [previous-commit]`
2. Force push to correct branch: `git push origin [branch] --force`
3. Push correct changes to intended branch
4. Inform user immediately

## Rule 2: NEVER Assume - Follow Instructions Exactly

**🚨 CRITICAL: Do NOT make assumptions about what the user wants. Follow their instructions EXACTLY.**

### Rules
- If user says "test using mcp" → Just test using MCP. Do NOT ask about commits, deployments, or other steps
- If user says "check the git tree" → Just show the git tree. Do NOT suggest next steps
- If user says "run the command" → Just run the command. Do NOT explain why or suggest alternatives
- **Let the user see the results FIRST, then they will tell you what to do next**

### Examples of BAD behavior (DO NOT DO THIS)

❌ User: "Test using mcp"
❌ Claude: "I need to commit and deploy first before testing..."
**WRONG:** User gave a direct instruction. Just test with MCP.

❌ User: "Check if it works"
❌ Claude: "Let me explain the architecture first and then suggest fixes..."
**WRONG:** User asked to check. Just check and report findings.

### Examples of GOOD behavior (DO THIS)

✅ User: "Test using mcp"
✅ Claude: *Immediately launches MCP and tests, then reports findings*

✅ User: "Check the database"
✅ Claude: *Runs query, shows results, waits for user's next instruction*

## Rule 3: NEVER Delete Local Database - CRITICAL

**🚨 CRITICAL: `db.sqlite3` IS OFF-LIMITS - IT CONTAINS USER'S DEVELOPMENT DATA**

### Rules
- ❌ **NEVER delete `db.sqlite3`** for any reason
- ❌ **NEVER recreate database** to fix migration/schema issues
- ✅ **ALWAYS ask permission first** before any database-altering operation
- ✅ **ALWAYS explore alternatives** that preserve existing data

### If database issues occur:
1. **First:** Try to fix with migrations (apply, rollback, reconcile)
2. **Second:** Ask user if database can be reset
3. **NEVER:** Silently delete the database without permission

This is not a temp file. It is your development database with real data.

## Rule 4: File Cleanup - Stay Within Scope

**CRITICAL: Only remove files that are temporary/build artifacts.**

### When cleaning up files:
- ✅ **DO remove:** Temporary build files, duplicate exports, cache files
- ❌ **DO NOT remove:** `db.sqlite3`, Documentation (*.md), UI components (*.html), project source files

### Rule: If you're unsure whether a file belongs to the project, **ASK FIRST - DO NOT DELETE.**

### Scope principle
Only delete files explicitly confirmed as temporary/build artifacts. Never assume UI components, documentation, or code files are "temporary" without user confirmation.

### Example - WRONG
```bash
# ❌ WRONG - Deletes potentially important UI files
rm src/templates/components/dynamic_width_style.html
rm src/templates/CSP_INLINE_STYLES_FIX.md
```

### Example - RIGHT
```bash
# ✅ RIGHT - Removes only confirmed temporary build files
rm src/db_restore_oct24.sqlite3  # Temp SQLite restore file
rm backup_data.sql               # Duplicate export (src/backup_data.sql exists)
```

## Rule 5: No Temporary Fixes

**ALWAYS fix root causes, never use workarounds:**

```python
# ❌ WRONG - Temporary workaround
# @require_permission('manage_users')  # Commented out temporarily
def manage_users(request):
    pass

# ✅ RIGHT - Fix root cause
# Create migration to add missing permission
@require_permission('manage_users')
def manage_users(request):
    pass
```

## Rule 6: No Assumptions - Research When Unsure

Never guess. Always verify:
- Use WebSearch for current documentation
- Use parallel agents for multi-faceted investigations
- Read actual code instead of assuming behavior
- State explicitly when you don't know something

## Rule 7: Verify Outcomes with Evidence

Never claim success without proof:

```markdown
# ❌ WRONG
"The deployment succeeded. I saw a checkmark."

# ✅ RIGHT
"I navigated to deployment logs. The logs show:
[specific output]. Status: SUCCESS. Last entry at 14:30 UTC."
```

When challenged, re-verify with actual evidence.

## Rule 8: CSP Compliance is Mandatory

**🚨 CRITICAL: All code changes MUST be Content Security Policy (CSP) compliant.**

### Rules:
- **NEVER use inline styles** - Use `<style nonce="{{ request.csp_nonce }}">` blocks
- **NEVER use inline scripts** - Use `<script nonce="{{ request.csp_nonce }}">` blocks
- **NEVER use inline event handlers** - Use HTMX attributes or proper event listeners
- **ALWAYS verify nonce attributes** are present on `<style>` and `<script>` tags

### Examples

```html
<!-- ❌ WRONG - CSP Violation -->
<div style="color: red;">Text</div>
<button onclick="doSomething()">Click</button>
<script>console.log('hello');</script>

<!-- ✅ RIGHT - CSP Compliant -->
<style nonce="{{ request.csp_nonce }}">
.red-text { color: red; }
</style>
<div class="red-text">Text</div>

<button id="myButton">Click</button>
<script nonce="{{ request.csp_nonce }}">
document.getElementById('myButton').addEventListener('click', doSomething);
</script>
```

### HTMX is CSP-safe:
```html
<!-- ✅ HTMX attributes are CSP-safe -->
<button hx-get="/api/data" hx-target="#result">Load</button>
```

### Before committing ANY code:
1. Search for inline `style=` attributes → Move to `<style nonce>` block
2. Search for inline `onclick=`, `onload=`, etc. → Use event listeners or HTMX
3. Search for `<script>` tags → Verify `nonce="{{ request.csp_nonce }}"` present
4. Search for `<style>` tags → Verify `nonce="{{ request.csp_nonce }}"` present

## Rule 9: Migration Management - CRITICAL

**🚨 CRITICAL: NEVER DELETE `db.sqlite3` WHEN RUNNING OR FIXING MIGRATION ISSUES**

This is the user's development data. It is NOT a temporary file. ALWAYS ask permission before any operation that would modify or delete the database.

### Database Operations
- ✅ **DO:** Apply migrations to existing database
- ✅ **DO:** Create new migrations for model changes
- ✅ **DO:** Use `sync_migrations` for production databases with existing tables
- ✅ **DO:** Ask user permission before ANY database-altering operation

### Database Operations - NEVER DO
- ❌ Delete db.sqlite3 (EVER - it contains user's development data)
- ❌ Manually edit migration files (except dependencies)
- ❌ Skip migrations
- ❌ Perform database operations without asking first
