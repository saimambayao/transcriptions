# TypeScript Error Patterns Reference

Common TypeScript errors in Bangsamoro Development Platform and their fixes.

## Table of Contents

1. [Type Assignment Errors](#type-assignment-errors)
2. [Property/Method Errors](#propertymethod-errors)
3. [Null/Undefined Errors](#nullundefined-errors)
4. [Import/Module Errors](#importmodule-errors)
5. [React/Next.js Specific](#reactnextjs-specific)
6. [TanStack Query Errors](#tanstack-query-errors)
7. [ESLint Errors](#eslint-errors)

## Type Assignment Errors

### TS2322: Type 'X' is not assignable to type 'Y'

**Pattern:**
```typescript
Type 'string' is not assignable to type 'number'
```

**Fix approaches:**
```typescript
// 1. Update the variable type
const value: string = getData(); // Change from number to string

// 2. Convert the value
const value: number = parseInt(stringValue, 10);

// 3. Update the interface/type
interface Props {
  count: string; // Change from number to string
}

// 4. Type assertion (use sparingly)
const value = getData() as number;
```

### TS2345: Argument type mismatch

**Pattern:**
```typescript
Argument of type 'string' is not assignable to parameter of type 'number'
```

**Fix:**
```typescript
// Check function signature and pass correct type
function calculate(value: number): number { ... }
calculate(Number(stringValue)); // Convert before passing
```

### TS2741: Property missing in type

**Pattern:**
```typescript
Property 'name' is missing in type '{ id: number }' but required in type 'User'
```

**Fix:**
```typescript
// Add missing property
const user: User = { id: 1, name: "John" };

// Or make property optional in interface
interface User {
  id: number;
  name?: string; // Optional
}
```

## Property/Method Errors

### TS2339: Property does not exist

**Pattern:**
```typescript
Property 'x' does not exist on type 'Y'
```

**Fixes:**
```typescript
// 1. Add to interface
interface User {
  id: number;
  name: string;
  x: string; // Add missing property
}

// 2. Use optional chaining if property may not exist
const value = user?.x;

// 3. Type guard
if ('x' in user) {
  console.log(user.x);
}

// 4. Extend type
type ExtendedUser = User & { x: string };
```

### TS2551: Property typo suggestion

**Pattern:**
```typescript
Property 'nmae' does not exist. Did you mean 'name'?
```

**Fix:** Correct the typo.

## Null/Undefined Errors

### TS2531: Object is possibly 'null'

**Pattern:**
```typescript
Object is possibly 'null'
```

**Fixes:**
```typescript
// 1. Optional chaining
const name = user?.name;

// 2. Nullish coalescing
const name = user?.name ?? 'Default';

// 3. Type guard
if (user !== null) {
  console.log(user.name);
}

// 4. Non-null assertion (use when certain)
const name = user!.name;
```

### TS2532: Object is possibly 'undefined'

**Pattern:**
```typescript
Object is possibly 'undefined'
```

**Same fixes as null, plus:**
```typescript
// Default parameter
function greet(name: string = 'Guest') { ... }

// Destructuring with default
const { name = 'Guest' } = user ?? {};
```

### TS18048: Variable possibly undefined after assignment

**Pattern:**
```typescript
'x' is possibly 'undefined'
```

**Fix:**
```typescript
// Early return pattern
const item = items.find(i => i.id === id);
if (!item) return null;
// item is now guaranteed to be defined
console.log(item.name);
```

## Import/Module Errors

### TS2307: Cannot find module

**Pattern:**
```typescript
Cannot find module '@/components/Button' or its corresponding type declarations
```

**Fixes:**
1. Check file exists at the path
2. Verify tsconfig.json path aliases:
```json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```
3. Check file extension (.ts vs .tsx)
4. Restart TypeScript server

### TS2305: Module has no exported member

**Pattern:**
```typescript
Module '"@/lib/utils"' has no exported member 'formatDate'
```

**Fixes:**
```typescript
// 1. Check export exists
export function formatDate() { ... } // Must be exported

// 2. Use correct export type
export { formatDate }; // Named export
export default formatDate; // Default export

// 3. Import correctly
import { formatDate } from '@/lib/utils'; // Named
import formatDate from '@/lib/utils'; // Default
```

## React/Next.js Specific

### Client/Server Component Errors

**Pattern:**
```typescript
You're importing a component that needs 'useState'. This only works in a Client Component.
```

**Fix:**
```typescript
// Add directive at top of file
'use client';

import { useState } from 'react';
```

### TS2786: Component cannot be used as JSX

**Pattern:**
```typescript
'Component' cannot be used as a JSX component. Its return type is not a valid JSX element.
```

**Fix:**
```typescript
// Ensure component returns valid JSX
export function Component(): JSX.Element {
  return <div>Content</div>; // Not null or undefined at top level
}

// Or use ReactNode for flexibility
export function Component(): React.ReactNode {
  return condition ? <div>Content</div> : null;
}
```

### Event Handler Types

**Pattern:**
```typescript
Type '(e: MouseEvent) => void' is not assignable to type 'MouseEventHandler<HTMLButtonElement>'
```

**Fix:**
```typescript
// Use React's event types
const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
  // ...
};

// Or let TypeScript infer
<button onClick={(e) => console.log(e.currentTarget)}>Click</button>
```

## TanStack Query Errors

### Query Key Type Errors

**Pattern:**
```typescript
Type 'string' is not assignable to type 'readonly unknown[]'
```

**Fix:**
```typescript
// Query keys must be arrays
const { data } = useQuery({
  queryKey: ['users', userId], // Array, not string
  queryFn: () => fetchUser(userId),
});
```

### Return Type Mismatches

**Pattern:**
```typescript
Type 'undefined' is not assignable to type 'User[]'
```

**Fix:**
```typescript
// Handle loading/error states
const { data, isLoading, error } = useQuery<User[]>({...});

if (isLoading) return <Loading />;
if (error) return <Error />;

// data is now guaranteed to be User[]
return <UserList users={data} />;
```

## ESLint Errors

### Unused Variables

**Pattern:**
```typescript
'x' is defined but never used @typescript-eslint/no-unused-vars
```

**Fixes:**
```typescript
// 1. Remove if truly unused
// 2. Prefix with underscore
const _unusedVar = getValue();
const { used, _unused } = object;

// 3. Disable for specific line
// eslint-disable-next-line @typescript-eslint/no-unused-vars
const tempVar = debug();
```

### Missing Dependencies in Hooks

**Pattern:**
```typescript
React Hook useEffect has missing dependencies: 'value'. eslint(react-hooks/exhaustive-deps)
```

**Fixes:**
```typescript
// 1. Add missing dependency
useEffect(() => {
  doSomething(value);
}, [value]); // Add value to deps

// 2. Use useCallback for functions
const memoizedFn = useCallback(() => {
  doSomething(value);
}, [value]);

useEffect(() => {
  memoizedFn();
}, [memoizedFn]);

// 3. Intentionally skip (document why)
useEffect(() => {
  // Only run on mount
  initializeOnce();
  // eslint-disable-next-line react-hooks/exhaustive-deps
}, []);
```

### Prefer const

**Pattern:**
```typescript
'x' is never reassigned. Use 'const' instead. eslint(prefer-const)
```

**Fix:**
```typescript
// Change let to const
const value = 'fixed'; // Not let
```

## Quick Diagnostic Commands

```bash
# Run TypeScript compiler for diagnostics only
cd frontend && npx tsc --noEmit

# Show all errors with context
cd frontend && npx tsc --noEmit --pretty

# Check specific file
cd frontend && npx tsc --noEmit src/components/MyComponent.tsx
```
