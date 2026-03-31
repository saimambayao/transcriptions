## Comprehensive 7-Step Debugging

### Step 1: Reproduce the Issue

**Never skip this step.** Consistent reproduction is critical.

**Activities:**
1. Document exact steps that trigger the bug
2. Identify environment (dev, staging, production)
3. Capture error message and stack trace
4. Note conditions (user role, portal, data state)
5. Verify bug occurs consistently (3+ times)

**Frontend Tools:**
- Browser DevTools Console
- React DevTools
- Network tab

**Backend Tools:**
- Django server logs
- Railway logs: `railway logs --tail 200`

### Step 2: Isolate the Problem

Narrow down using binary search approach.

**Layer Identification:**

| Layer | Symptoms | Tools |
|-------|----------|-------|
| React Component | UI doesn't render, state issues | React DevTools, console.log |
| Next.js | Routing, SSR/CSR mismatch, hydration | Next.js dev overlay, server logs |
| TanStack Query | Stale data, refetch issues | React Query DevTools |
| API Call | Network errors, wrong data | Network tab, API response |
| Django Ninja | 4xx/5xx errors | Django logs, API docs |
| Database | Missing data, query errors | Django shell, SQL logs |

**Isolation Techniques:**

```typescript
// Add strategic logging
console.log('Step 1: Component mounted');
console.log('Step 2: Query data:', data);
console.log('Step 3: Rendering with:', props);
```

### Step 3: Gather Evidence

**Browser Console:**
```javascript
// Check for errors
// Red errors = JavaScript/React issues
// Yellow warnings = potential issues
```

**Network Tab:**
- Check request URL, method, headers
- Verify response status code
- Inspect response body
- Check timing

**React DevTools:**
- Component tree
- Props and state values
- Hooks state

**TanStack Query DevTools:**
- Query status (loading, error, success)
- Cache state
- Query key

**Django Logs:**
```bash