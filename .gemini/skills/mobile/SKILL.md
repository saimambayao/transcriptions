---
name: mobile
description: React Native mobile development for MoroMarket (Bangsamoro Digital Platform). Use when building mobile app features for consumers (shopping, orders, wishlist) or sellers (product management, inventory, orders). Covers React Native + Expo setup, navigation, API integration with Django Ninja backend, offline-first patterns for BARMM connectivity, and app store deployment. Includes project-specific design tokens (Negosyo Blue #0056D2) and shared TypeScript types.
argument-hint: "[topic]"
---

# Mobile Development

React Native + Expo mobile app development for the Bangsamoro Digital Platform (MoroMarket).

## When to Use

- Building mobile app screens for MoroMarket
- Setting up React Native + Expo project
- Implementing navigation (tabs, stacks, deep linking)
- Integrating with Django Ninja backend APIs
- Implementing offline-first patterns for BARMM connectivity
- Deploying to App Store / Play Store
- Creating mobile-specific UI components

## Tech Stack

| Layer | Technology |
|-------|------------|
| Framework | React Native + Expo |
| Language | TypeScript |
| Navigation | Expo Router (file-based) |
| State | TanStack Query |
| Storage | MMKV, SecureStore |
| API | Django Ninja (shared backend) |

## Development Phases

Complete these phases in order:

| Phase | Purpose | Output |
|-------|---------|--------|
| 1. Web App Audit | Inventory existing web pages | Audit spreadsheet |
| 2. Page Mapping | Plan mobile equivalents | Page mapping document |
| 3. Architecture Design | Define mobile app structure | Architecture document |
| 4. Project Setup | Initialize Expo project | Working project |
| 5. Implementation | Build screens and features | Mobile app |
| 6. Deployment | Submit to app stores | Published app |

---

## Phase 1: Web App Audit

Audit existing MoroMarket web application to understand what needs mobile equivalents.

### Audit Checklist

```markdown
## Web App Pages Audit

### Public Portal (/)
| Page | Route | Priority | Mobile Needed | Notes |
|------|-------|----------|---------------|-------|
| Home | / | High | Yes | Marketplace landing |
| Product List | /marketplace | High | Yes | Browse products |
| Product Detail | /product/[slug] | High | Yes | View product |
| Coop Directory | /directory/cooperatives | Medium | Yes | List coops |
| SE Directory | /directory/social-enterprises | Medium | Yes | List SEs |
| Coop Storefront | /coop/[shortname] | High | Yes | Individual shop |
| SE Storefront | /se/[shortname] | High | Yes | Individual shop |

### Consumer Portal (/consumer)
| Page | Route | Priority | Mobile Needed | Notes |
|------|-------|----------|---------------|-------|
| Dashboard | /consumer | High | Yes | Consumer home |
| Orders | /consumer/orders | High | Yes | Order history |
| Order Detail | /consumer/orders/[id] | High | Yes | Track order |
| Saved Items | /consumer/saved-items | Medium | Yes | Wishlist |
| Profile | /consumer/profile | High | Yes | Account settings |

### Seller Portal (/portal)
| Page | Route | Priority | Mobile Needed | Notes |
|------|-------|----------|---------------|-------|
| Dashboard | /portal | High | Yes | Business overview |
| Products | /portal/products | High | Yes | Product management |
| Add Product | /portal/products/new | High | Yes | Create product |
| Edit Product | /portal/products/[id] | High | Yes | Update product |
| Orders | /portal/orders | High | Yes | Order management |
| Inventory | /portal/inventory | Medium | Yes | Stock management |
| Business Profile | /portal/business | Medium | Yes | Business settings |
```

### Audit Commands

```bash
# List all frontend routes
find frontend/src/app -name "page.tsx" | sort

# Count pages per route group
find frontend/src/app -name "page.tsx" | grep -c "(public)"
find frontend/src/app -name "page.tsx" | grep -c "(tenant)"
```

---

## Phase 2: Page Mapping

Map web pages to mobile app screens with navigation structure.

### Mapping Template

```markdown
## Web-to-Mobile Page Mapping

### Consumer App Screens

| Web Page | Mobile Screen | Route Group | Tab/Stack | Notes |
|----------|---------------|-------------|-----------|-------|
| / (home) | Home | (consumer) | Tab | Marketplace home |
| /marketplace | Search | (consumer) | Tab | Product search |
| /product/[slug] | ProductDetail | (consumer) | Stack | From home/search |
| /cart | Cart | (consumer) | Tab | Shopping cart |
| /checkout | Checkout | (consumer) | Stack | From cart |
| /consumer/orders | Orders | (consumer) | Tab | Order history |
| /consumer/orders/[id] | OrderDetail | (consumer) | Stack | From orders |
| /consumer/saved-items | SavedItems | (consumer) | Stack | From profile |
| /consumer/profile | Profile | (consumer) | Tab | Account |

### Seller App Screens

| Web Page | Mobile Screen | Route Group | Tab/Stack | Notes |
|----------|---------------|-------------|-----------|-------|
| /portal | Dashboard | (seller) | Tab | Business home |
| /portal/products | Products | (seller) | Tab | Product list |
| /portal/products/new | AddProduct | (seller) | Stack | From products |
| /portal/products/[id] | EditProduct | (seller) | Stack | From products |
| /portal/orders | Orders | (seller) | Tab | Order management |
| /portal/orders/[id] | OrderDetail | (seller) | Stack | From orders |
| /portal/inventory | Inventory | (seller) | Tab | Stock mgmt |
| /portal/business | Business | (seller) | Stack | From profile |

### Auth Screens (shared)

| Web Page | Mobile Screen | Route Group | Notes |
|----------|---------------|-------------|-------|
| /login | Login | (auth) | Email/password |
| /register | Register | (auth) | Consumer signup |
| /register/seller | SellerRegister | (auth) | Business signup |
| /forgot-password | ForgotPassword | (auth) | Password reset |
```

### Mapping Considerations

- **Simplify for mobile**: Combine related pages where appropriate
- **Prioritize touch**: Consider thumb zones and gesture navigation
- **Offline-first**: Mark screens that need offline support
- **Platform patterns**: Use native iOS/Android patterns (tabs, back navigation)

---

## Phase 3: Architecture Design

Document the mobile app architecture before starting development.

### Architecture Document Template

```markdown
# MoroMarket Mobile Architecture

## Overview
Mobile application for MoroMarket marketplace serving:
- Consumers: Browse, purchase, track orders
- Sellers: Manage products, process orders, track inventory

## Tech Stack
- **Framework**: React Native + Expo (SDK 52+)
- **Language**: TypeScript
- **Navigation**: Expo Router
- **State**: TanStack Query + React Context
- **Storage**: MMKV (offline), SecureStore (tokens)
- **API**: Django Ninja (shared backend)

## App Structure

### Route Groups
```
app/
├── (auth)/           # Authentication flow
├── (consumer)/       # Consumer experience
│   └── (tabs)/       # Consumer tab navigation
├── (seller)/         # Seller experience
│   └── (tabs)/       # Seller tab navigation
└── _layout.tsx       # Root: auth check + providers
```

### State Architecture
```
AuthContext (user, tokens, role)
    └── QueryClientProvider (TanStack Query)
        └── Role-based navigation
            ├── Consumer tabs
            └── Seller tabs
```

### Data Flow
```
API (Django Ninja)
    ↓
TanStack Query (cache, sync)
    ↓
MMKV (offline persistence)
    ↓
Components (UI)
```

## Offline Strategy

| Data Type | Strategy | Sync |
|-----------|----------|------|
| Products catalog | Cache-first | Background |
| Cart | Local-first | On checkout |
| Orders (read) | Cache-first | On pull |
| Orders (create) | Queue | When online |
| Profile | Network-first | On demand |

## Security

- JWT tokens in SecureStore
- Token refresh on 401
- Biometric unlock (optional)
- Certificate pinning (production)

## Performance Targets

| Metric | Target |
|--------|--------|
| App launch | < 2s |
| Screen transition | < 300ms |
| API response (cached) | < 100ms |
| Offline mode entry | Immediate |
```

Save architecture document to `docs/architecture/mobile/` before proceeding.

See [references/web-to-mobile-audit.md](references/web-to-mobile-audit.md) for detailed audit process.

---

## Phase 4: Project Setup

### Initialize Expo Project

```bash
# Create Expo project
npx create-expo-app@latest MoroMarketMobile --template expo-template-blank-typescript
cd MoroMarketMobile

# Install core dependencies
npx expo install @react-navigation/native @react-navigation/native-stack
npx expo install @tanstack/react-query expo-secure-store
npx expo install react-native-mmkv @react-native-community/netinfo
```

Copy design tokens from `assets/design-tokens.ts` to your project.

See [references/setup.md](references/setup.md) for complete setup guide.

## App Architecture

### Role-Based Navigation

```
(auth)           → Login, Register, Forgot Password
(consumer)       → Home, Search, Cart, Orders, Profile
(seller)         → Dashboard, Products, Orders, Inventory, Business
```

### Feature Matrix

| Feature | Consumer | Seller |
|---------|----------|--------|
| Browse products | Yes | - |
| Shopping cart | Yes | - |
| Place orders | Yes | - |
| Track orders | Yes | Yes |
| Manage products | - | Yes |
| Manage inventory | - | Yes |
| View analytics | - | Yes |
| Push notifications | Yes | Yes |
| Offline browsing | Yes | Limited |

See [references/navigation.md](references/navigation.md) for navigation patterns.

## API Integration

### API Client Pattern

```typescript
// lib/api/client.ts
import * as SecureStore from 'expo-secure-store'

const API_URL = 'https://api.moromarket.bangsamoro.site'

export const apiClient = {
  async get<T>(endpoint: string, params?: Record<string, unknown>): Promise<T> {
    const token = await SecureStore.getItemAsync('accessToken')
    const url = new URL(`${API_URL}${endpoint}`)
    if (params) {
      Object.entries(params).forEach(([k, v]) =>
        v !== undefined && url.searchParams.set(k, String(v))
      )
    }
    const res = await fetch(url.toString(), {
      headers: {
        'Content-Type': 'application/json',
        ...(token && { Authorization: `Bearer ${token}` }),
      },
    })
    if (!res.ok) throw new Error(`API error: ${res.status}`)
    return res.json()
  },
  // post, patch, delete similar...
}
```

### TanStack Query Hook

```typescript
// lib/hooks/useProducts.ts
import { useQuery } from '@tanstack/react-query'

export function useProducts(filters?: ProductFilters) {
  return useQuery({
    queryKey: ['products', filters],
    queryFn: () => apiClient.get<Product[]>('/public/products', filters),
    staleTime: 1000 * 60 * 5,
  })
}
```

See [references/api-integration.md](references/api-integration.md) for:
- Full API client implementation
- Authentication service
- All API endpoints
- Error handling

## Offline Support

BARMM areas may have limited connectivity. Implement offline-first patterns:

### Network Detection

```typescript
import { useNetworkStatus } from '@/lib/hooks/useNetworkStatus'

function ProductList() {
  const { isConnected } = useNetworkStatus()

  if (!isConnected) {
    return <OfflineBanner />
  }
  // ...
}
```

### Cache Strategy

| Data | Strategy | Offline |
|------|----------|---------|
| Products | Cache-first | Yes (stale OK) |
| Cart | Local-first | Yes |
| Orders | Network-first | Read-only |
| Profile | Network-first | Cached |

See [references/offline-first.md](references/offline-first.md) for:
- MMKV storage setup
- TanStack Query persistence
- Background sync patterns
- Optimistic updates

## Design System

### Colors (Negosyo Blue)

```typescript
import { Colors } from '@/constants/Colors'

// Primary
Colors.primary       // #0056D2 (Negosyo Blue)
Colors.primaryLight  // #3378DB
Colors.primaryDark   // #004BB5

// Accent (hero/promo)
Colors.accent        // #D30A28 (Negosyo Red)

// Semantic
Colors.success       // #22C55E
Colors.warning       // #F59E0B
Colors.error         // #EF4444
```

See `assets/design-tokens.ts` for complete tokens:
- Colors
- Typography
- Spacing
- Border radius
- Shadows
- Icon sizes

## Deployment

### Build Commands

```bash
# Development
npx expo start

# Preview APK
eas build --platform android --profile preview

# Production
eas build --platform ios --profile production
eas build --platform android --profile production

# Submit to stores
eas submit --platform ios --latest
eas submit --platform android --latest
```

### OTA Updates

```bash
# Push JS-only updates
eas update --branch production --message "Bug fix"
```

See [references/deployment.md](references/deployment.md) for:
- EAS configuration
- App Store metadata
- Play Store setup
- CI/CD with GitHub Actions

## Project-Specific Context

### Shared Types

Reuse types from web frontend where applicable:

```typescript
// Types from frontend/src/lib/types/
- auth.ts     → User, LoginCredentials, AuthResponse
- consumer.ts → ConsumerProfile, SavedItem, ConsumerOrder
- storefront.ts → Product, ProductFilters
- tenant.ts   → Tenant, TenantType
```

### API Endpoints

Backend API is shared with web:
- Auth: `/auth/login`, `/auth/register`, `/auth/refresh`
- Consumer: `/consumer/profile`, `/consumer/orders`, `/consumer/saved-items`
- Public: `/public/products`, `/public/cooperatives`
- Tenant: `/tenant/products`, `/tenant/orders`, `/tenant/inventory`

### Conventions

- Primary color: Negosyo Blue (#0056D2)
- No purple colors
- Icons instead of emojis
- Offline-first for BARMM connectivity
- TypeScript for all code

## Resources

### References
- [web-to-mobile-audit.md](references/web-to-mobile-audit.md) - Web app audit and page mapping
- [setup.md](references/setup.md) - Project setup and configuration
- [navigation.md](references/navigation.md) - Navigation patterns
- [api-integration.md](references/api-integration.md) - API integration
- [offline-first.md](references/offline-first.md) - Offline support
- [deployment.md](references/deployment.md) - App store deployment

### Assets
- [design-tokens.ts](assets/design-tokens.ts) - Colors, typography, spacing
- [app.config.template.ts](assets/app.config.template.ts) - Expo configuration template
