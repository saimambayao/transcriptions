# Post-Refactoring Cleanup Checklist

Use this checklist after completing a module/submodule refactoring to ensure no unused files remain.

## Step 1: Identify Potentially Unused Files

List all files in the refactored directory:
```bash
ls -la frontend/src/features/{module}/components/{submodule}/
```

## Step 2: Check Each File's Usage

For each file, verify it's still needed:

### Check Imports
```bash
# Search for imports of the component
grep -rn "import.*{ComponentName}" frontend/src --include="*.tsx" --include="*.ts"
```

### Check JSX Usage
```bash
# Search for component usage in JSX
grep -rn "<{ComponentName}" frontend/src --include="*.tsx"
```

### Check Type References
```bash
# Search for type/interface usage
grep -rn "{TypeName}" frontend/src --include="*.tsx" --include="*.ts"
```

## Step 3: Document Findings

Create a table of findings:

| File | Status | Reason |
|------|--------|--------|
| Component.tsx | KEEP | Used in MainComponent.tsx |
| OldComponent.tsx | DELETE | No imports found |
| SharedUtil.ts | KEEP | Used by multiple components |

## Step 4: Remove Unused Files

After confirming files are unused:

1. Delete the file:
```bash
rm frontend/src/features/{module}/components/{submodule}/{UnusedFile}.tsx
```

2. Remove from index.ts exports:
```typescript
// Remove this line
export { default as UnusedComponent } from './UnusedComponent';
```

## Step 5: Verify Build

Always verify the build passes after cleanup:
```bash
cd frontend && npm run build
```

## Common Files to Check After Refactoring

### After Tab Restructuring
- Old tab content components that were replaced
- List components that were merged into new tab content
- Form components that may no longer be needed

### After Component Consolidation
- Helper components absorbed into larger components
- Utility functions that were inlined
- Types/interfaces that were moved or renamed

## Red Flags (Don't Delete)

- Files exported from index.ts may be used externally
- Shared components used across multiple modules
- Type definitions used by API/hooks
- Test files (check if tests still pass)

## Cleanup Report Template

After cleanup, document what was removed:

```markdown
## Refactoring Cleanup: {Module}/{Submodule}

**Date:** YYYY-MM-DD

### Files Deleted
| File | Reason |
|------|--------|
| OldComponent.tsx | Replaced by NewContent.tsx |

### Exports Removed
- `export { default as OldComponent } from './OldComponent'`

### Build Status
- [ ] Build passes
- [ ] No TypeScript errors
- [ ] UI functions correctly
```
