---
name: refactor
description: |
  Module/submodule refactoring workflow for e-Bangsamoro. Systematic approach to refactoring
  frontend modules based on wireframes, including cleanup of unused files after implementation.
  Use when: (1) implementing wireframes for a submodule, (2) restructuring tab-based components,
  (3) identifying and removing unused files after refactoring.
argument-hint: "[module]"
allowed-tools: Read, Grep, Glob
---

# Refactor Skill

Systematic module/submodule refactoring with cleanup recommendations.

## Use Cases

1. **Implement wireframes** - Convert wireframe specs to React components
2. **Restructure tabs** - Update tab-based navigation and content components
3. **Cleanup unused files** - Identify and remove obsolete components after refactoring

## Workflow

### Phase 1: Analysis

1. **Read wireframes** in `docs/architecture/Wireframes/`
2. **Review existing implementation** - understand current structure
3. **Identify gaps** - what needs to change (tabs, content, components)

### Phase 2: Implementation

1. **Update tab configuration** in `frontend/src/constants/modules/` (ministry.ts, parliament.ts, etc.)
2. **Create content components** for each tab following the pattern:
   - `{Module}{Tab}Content.tsx` (e.g., `BDPDashboardContent.tsx`)
3. **Update main component** to import and render new content components
4. **Update index.ts** exports

### Phase 3: Cleanup

After implementation, identify unused files:

```bash
# Search for component usage
grep -rn "ComponentName[^R]" frontend/src --include="*.tsx" --include="*.ts"

# Check if component is imported anywhere
grep -rn "import.*ComponentName" frontend/src
```

**Cleanup Checklist:**
- [ ] Remove unused component files
- [ ] Remove exports from index.ts
- [ ] Verify build passes: `npm run build`

## Module Structure

### Tab Configuration
Location: `frontend/src/constants/modules/{portal}.ts`

```typescript
{
  id: 'module-id',
  label: 'Module Name',
  icon: IconComponent,
  description: 'Description',
  tabs: [
    { id: 'tab-id', label: 'Tab Label', icon: IconComponent },
    // ...
  ]
}
```

### Content Components
Location: `frontend/src/features/{module}/components/{submodule}/`

Pattern:
```
{Submodule}/
├── {Submodule}.tsx           # Main container with tab routing
├── {Submodule}{Tab}Content.tsx  # Content for each tab
├── index.ts                  # Exports
└── ... (supporting components)
```

## Common Refactoring Scenarios

### Adding/Removing Tabs

1. Update tab config in `constants/modules/{portal}.ts`
2. Create/remove corresponding content component
3. Update main component's tab rendering
4. Update VALID_TABS constant in main component
5. Cleanup unused files

### Renaming Tabs

1. Update tab id and label in constants
2. Rename content component file
3. Update imports in main component
4. Update index.ts exports

## File Cleanup Commands

```bash
# Find files that might be unused after refactoring
grep -L "import.*from.*{filename}" frontend/src/**/*.tsx

# Verify no imports of a specific component
grep -rn "import.*{ComponentName}" frontend/src

# Check JSX usage
grep -rn "<{ComponentName}" frontend/src
```

## Example: BDP Alignment Refactoring

**Before:** 4 tabs (Dashboard, Goals, Targets, Matrix)
**After:** 5 tabs (Dashboard, Goals, Strategies, Indicators, Matrix)

**Files Created:**
- BDPDashboardContent.tsx
- BDPStrategiesContent.tsx
- BDPIndicatorsContent.tsx
- BDPAlignmentMatrixContent.tsx

**Files Deleted:**
- BDPAlignmentList.tsx (was used in old "Targets" tab)

**Config Updated:**
- ministry.ts - tab configuration
- index.ts - exports

## References

See `references/` for:
- [cleanup-checklist.md](references/cleanup-checklist.md) - Post-refactor cleanup steps
