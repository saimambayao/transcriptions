---
name: sync
description: Portal-Storefront data sync verification skill for Bangsamoro Development Platform. Ensures data integrity and API connection between the C/SE Portal (management interface) and public Storefront (customer-facing). Use when making portal changes, debugging data sync issues, verifying API integration, or troubleshooting why changes aren't reflecting on storefronts.
argument-hint: "[topic]"
---

# Sync - Portal-Storefront Data Integrity

## Phase 0: Prompt Refinement (Mandatory)

**Before executing this skill's workflow, invoke `/prompter` first:**

1. Invoke `/prompter` with the user's data sync verification request
2. Present the refined prompt to the user
3. Wait for user confirmation:
   - "Yes, proceed" → Continue to Phase 1 (Identify Sync Scope)
   - "No, adjust X" → Refine and re-confirm
   - "Let me rephrase" → Restart with new input

**Do not proceed without user confirmation.**

---

## Overview

The Sync skill ensures data integrity between the **C/SE Portal** (where cooperatives and social enterprises manage their data) and the **Storefront** (public-facing shop pages that customers see). When changes are made in the portal, this skill verifies they properly reflect on the storefront through correct API integration and publishing workflows.

**Core Concern**: Changes in `/tenant/*` portal pages must sync correctly to `/coop/[shortname]` or `/se/[shortname]` storefronts.

## When to Use This Skill

Invoke `/sync` when:
- Making changes to portal data management features
- Debugging why portal changes aren't showing on storefronts
- Implementing new portal features that affect storefront display
- Verifying API endpoints connect portal and storefront correctly
- Testing the publish/draft workflow
- Auditing data flow between management and public views

**Keywords**: "not showing", "not reflecting", "sync", "portal changes", "storefront data", "publish", "draft", "API connection"

## Data Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        C/SE PORTAL                              │
│                   /tenant/[shortname]/*                         │
│                                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │Dashboard │  │ Profile  │  │   Shop   │  │Compliance│        │
│  │          │  │ Editor   │  │ Manager  │  │  Status  │        │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘        │
│       │             │             │             │               │
│       └─────────────┴─────────────┴─────────────┘               │
│                           │                                     │
│                    ┌──────┴──────┐                              │
│                    │   PUBLISH   │ ◄── Draft vs Published       │
│                    │   WORKFLOW  │                              │
│                    └──────┬──────┘                              │
└───────────────────────────┼─────────────────────────────────────┘
                            │
                     ┌──────▼──────┐
                     │   API/DB    │
                     │  Backend    │
                     └──────┬──────┘
                            │
┌───────────────────────────┼─────────────────────────────────────┐
│                           │                                     │
│                    ┌──────▼──────┐                              │
│                    │   PUBLIC    │                              │
│                    │   QUERY     │                              │
│                    └──────┬──────┘                              │
│                           │                                     │
│       ┌───────────────────┼───────────────────┐                 │
│       │                   │                   │                 │
│  ┌────▼─────┐       ┌─────▼────┐       ┌──────▼─────┐          │
│  │   Hero   │       │ Products │       │   About    │          │
│  │  Banner  │       │   Grid   │       │   Info     │          │
│  └──────────┘       └──────────┘       └────────────┘          │
│                                                                 │
│                        STOREFRONT                               │
│              /coop/[shortname] or /se/[shortname]               │
└─────────────────────────────────────────────────────────────────┘
```

## Data Sync Points

The following data must sync from Portal to Storefront:

| Portal Section | Storefront Display | Data Points |
|----------------|-------------------|-------------|
| **Profile** | Hero Banner, About | name, tagline, description, logo, colors |
| **Business** | About Page | address, contact, operating hours, documents |
| **Shop/Products** | Product Grid | products, prices, images, categories, availability |
| **Storefront Settings** | Theme/Layout | primaryColor, layout, featured products |

## Verification Workflow

### Phase 1: Identify Sync Scope

When a sync issue is reported or a feature is implemented, identify:

1. **Source**: Which portal section is the data coming from?
2. **Target**: Which storefront component should display it?
3. **API**: Which endpoint connects them?
4. **State**: Is it a draft or published data issue?

### Phase 2: Trace Data Path

```
1. Portal Form/Editor
   └── Check: Form state management (React useState/useForm)
       └── Check: Form submission handler
           └── Check: API mutation call (TanStack Query)
               └── Check: API endpoint (Django Ninja)
                   └── Check: Database write
                       └── Check: Storefront query
                           └── Check: Component render
```

### Phase 3: Verification Checklist

Run this checklist for any portal-storefront sync:

```markdown
## Sync Verification Checklist

### 1. Portal Side
- [ ] Form data captures user input correctly
- [ ] Form submission triggers API call
- [ ] API call includes correct payload
- [ ] Success response received from backend
- [ ] UI updates to reflect saved state (optimistic or refetch)

### 2. API/Backend
- [ ] Endpoint receives correct data
- [ ] Data validated by Pydantic schema
- [ ] Database transaction completes
- [ ] Response includes updated data
- [ ] Multi-tenant scoping applied (organization filter)

### 3. Storefront Side
- [ ] Query fetches from correct endpoint
- [ ] Query includes correct filters (shortname, status)
- [ ] Data matches what was saved in portal
- [ ] Component receives data via props
- [ ] Component renders data correctly

### 4. Publishing Workflow
- [ ] Draft changes stay in draft state
- [ ] Publish action updates published status
- [ ] Storefront only shows published data
- [ ] Preview mode shows draft data
```

## Common Sync Issues

### Issue 1: Changes Not Appearing on Storefront

**Symptoms**: User saves in portal, but storefront shows old data

**Debug Steps**:
```typescript
// 1. Check TanStack Query cache invalidation
const mutation = useMutation({
  mutationFn: updateProfile,
  onSuccess: () => {
    // Is this invalidating the right query?
    queryClient.invalidateQueries({
      queryKey: ['cooperative', shortname]
    });
  },
});

// 2. Check storefront query key matches
const { data } = useQuery({
  queryKey: ['cooperative', shortname], // Must match invalidation
  queryFn: () => getCooperative(shortname),
});
```

**Common Fixes**:
- Ensure query keys match between portal mutation and storefront query
- Add staleTime: 0 for real-time data
- Verify cache invalidation on mutation success

### Issue 2: API Returns Stale Data

**Symptoms**: API call succeeds but returns old data

**Debug Steps**:
```python
# Check Django view is reading from database, not cache
@router.get('/cooperatives/{shortname}')
def get_cooperative(request, shortname: str):
    # Force database read
    return Cooperative.objects.select_related(
        'organization'
    ).get(
        shortname=shortname,
        status='active'  # Is status filter correct?
    )
```

**Common Fixes**:
- Disable or invalidate server-side cache
- Check database transaction isolation
- Verify status filters include updated records

### Issue 3: Published vs Draft State

**Symptoms**: Changes appear in preview but not public storefront

**Debug Steps**:
```typescript
// Portal: Check publish state
const { publishedAt, isDraft } = useStorefrontState();

// Storefront: Check query filters
const { data } = useQuery({
  queryKey: ['cooperative', shortname],
  queryFn: () => getPublicCooperative(shortname), // Only published
});
```

**Common Fixes**:
- Ensure publish action updates `publishedAt` timestamp
- Verify storefront query filters for `status='active'` or `publishedAt IS NOT NULL`
- Check preview mode uses different query (includes drafts)

### Issue 4: Multi-Tenant Data Leak

**Symptoms**: Storefront shows data from wrong organization

**Debug Steps**:
```python
# CRITICAL: Verify organization scoping
@router.get('/cooperatives/{shortname}')
def get_cooperative(request, shortname: str):
    return Cooperative.objects.get(
        shortname=shortname,
        organization=request.auth.organization  # REQUIRED for portal
        # But storefront is public - uses shortname only
    )
```

**Common Fixes**:
- Portal endpoints MUST include organization filter
- Storefront endpoints use shortname (public data only)
- Never expose internal IDs on public endpoints

## API Integration Patterns

### Portal Mutation Pattern

```typescript
// frontend/src/lib/hooks/tenant/useProfile.ts

export function useUpdateProfile() {
  const queryClient = useQueryClient();
  const { shortname } = useTenant();

  return useMutation({
    mutationFn: async (data: ProfileUpdate) => {
      const response = await api.put(`/tenant/${shortname}/profile`, data);
      return response.data;
    },
    onSuccess: (updatedProfile) => {
      // Invalidate both portal and storefront caches
      queryClient.invalidateQueries({ queryKey: ['tenant', 'profile'] });
      queryClient.invalidateQueries({ queryKey: ['cooperative', shortname] });
    },
    onError: (error) => {
      toast.error('Failed to update profile');
    },
  });
}
```

### Storefront Query Pattern

```typescript
// frontend/src/lib/hooks/public/useCooperative.ts

export function useCooperative(shortname: string) {
  return useQuery({
    queryKey: ['cooperative', shortname],
    queryFn: async () => {
      const response = await api.get(`/public/cooperatives/${shortname}`);
      return response.data;
    },
    staleTime: 5 * 60 * 1000, // 5 minutes for public data
    enabled: !!shortname,
  });
}
```

### Backend Endpoint Pattern

```python
# backend/apps/cooperatives/api.py

# Portal endpoint (authenticated, organization-scoped)
@router.put('/tenant/{shortname}/profile')
def update_profile(request, shortname: str, payload: ProfileUpdate):
    coop = Cooperative.objects.get(
        shortname=shortname,
        organization=request.auth.organization  # REQUIRED
    )
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(coop, attr, value)
    coop.updated_by = request.auth
    coop.save()
    return coop

# Storefront endpoint (public, no auth)
@router.get('/public/cooperatives/{shortname}', auth=None)
def get_public_cooperative(request, shortname: str):
    return Cooperative.objects.filter(
        shortname=shortname,
        status='active',
        is_deleted=False
    ).values(
        'name', 'shortname', 'tagline', 'description',
        'logo', 'primaryColor', 'address', 'phone', 'email'
    ).first()
```

## File Locations Reference

### Portal Files
```
frontend/src/app/(tenant)/
├── tenant/[shortname]/
│   ├── dashboard/page.tsx       # Dashboard metrics
│   ├── profile/page.tsx         # Profile editor
│   ├── business/page.tsx        # Business info
│   ├── shop/page.tsx            # Product management
│   ├── compliance/page.tsx      # Compliance status
│   └── settings/page.tsx        # Storefront settings
```

### Storefront Files
```
frontend/src/app/(coop)/
├── coop/[shortname]/
│   ├── layout.tsx               # Storefront layout
│   ├── page.tsx                 # Homepage
│   ├── _components/
│   │   ├── HeroBanner.tsx       # Hero with profile data
│   │   ├── ProductCard.tsx      # Product display
│   │   ├── TenantHeader.tsx     # Navigation
│   │   └── StorefrontShell.tsx  # Main wrapper
│   ├── shop/page.tsx            # All products
│   ├── about/page.tsx           # About page
│   └── profile/page.tsx         # Business profile
```

### API/Service Files
```
frontend/src/lib/
├── services/
│   ├── tenant/                  # Portal API calls
│   └── public/                  # Storefront API calls
├── hooks/
│   ├── tenant/                  # Portal hooks
│   └── public/                  # Storefront hooks
```

## Testing Sync

### Manual Test Workflow

1. **Open Portal** at `/tenant/[shortname]/profile`
2. **Open Storefront** at `/coop/[shortname]` in another tab
3. **Make change** in Portal (e.g., update tagline)
4. **Save** the change
5. **Refresh** Storefront tab
6. **Verify** the change appears

### Automated Test Pattern

```typescript
// e2e/sync.spec.ts
import { test, expect } from '@playwright/test';

test('profile changes sync to storefront', async ({ page, context }) => {
  const shortname = 'cowocco';

  // Login to portal
  await page.goto('/tenant/login');
  await page.fill('[name="email"]', 'admin@cowocco.coop');
  await page.fill('[name="password"]', 'password');
  await page.click('button[type="submit"]');

  // Update profile
  await page.goto(`/tenant/${shortname}/profile`);
  const newTagline = `Updated at ${Date.now()}`;
  await page.fill('[name="tagline"]', newTagline);
  await page.click('button:has-text("Save")');
  await expect(page.locator('.toast-success')).toBeVisible();

  // Verify on storefront
  const storefrontPage = await context.newPage();
  await storefrontPage.goto(`/coop/${shortname}`);
  await expect(storefrontPage.locator('.hero-tagline')).toContainText(newTagline);
});
```

## Quick Debugging Commands

```bash
# Check database state
cd backend && python manage.py shell
>>> from apps.cooperatives.models import Cooperative
>>> c = Cooperative.objects.get(shortname='cowocco')
>>> print(c.tagline, c.updated_at)

# Check API response
curl http://localhost:8090/api/public/cooperatives/cowocco

# Check frontend query cache (browser console)
window.__REACT_QUERY_DEVTOOLS__.getQueryCache().getAll()
```

## Integration with Other Skills

| Skill | When to Use Together |
|-------|---------------------|
| `/debugger` | When sync issue requires deep investigation |
| `/frontend` | When building new portal-storefront features |
| `/backend` | When implementing API endpoints for sync |
| `/investigator` | When researching TanStack Query patterns |
| `/coditor` | When auditing for data leak vulnerabilities |

---

**Remember**: The `/sync` skill focuses on data integrity between Portal and Storefront. Always trace the full data path: Form → API → Database → Query → Component.
