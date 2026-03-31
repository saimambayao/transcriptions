# Web-to-Mobile Audit Guide

Complete guide for auditing web applications and planning mobile equivalents.

## Overview

Before starting mobile development, complete these three phases:
1. **Web App Audit** - Inventory all existing web pages
2. **Page Mapping** - Plan mobile screen equivalents
3. **Architecture Design** - Document the mobile app structure

---

## Phase 1: Web App Audit

### Purpose
Create a comprehensive inventory of all web app pages to understand scope.

### Audit Commands

```bash
# List all frontend routes
find frontend/src/app -name "page.tsx" | sort

# Count pages per route group
find frontend/src/app -name "page.tsx" | grep -c "(public)"
find frontend/src/app -name "page.tsx" | grep -c "(tenant)"
find frontend/src/app -name "page.tsx" | grep -c "(admin)"

# List route groups
ls -la frontend/src/app/

# Find all dynamic routes
find frontend/src/app -type d -name "\[*\]"
```

### Audit Template

Create `docs/architecture/mobile/web-audit.md`:

```markdown
# MoroMarket Web App Audit

Date: [DATE]
Auditor: [NAME]

## Summary
- Total pages: [COUNT]
- Public pages: [COUNT]
- Consumer pages: [COUNT]
- Seller pages: [COUNT]

## Public Portal (/)

| Page | Route | Components | API Calls | Priority | Mobile? |
|------|-------|------------|-----------|----------|---------|
| Home | / | Hero, ProductGrid, Categories | products, categories | High | Yes |
| Marketplace | /marketplace | ProductGrid, Filters, Pagination | products | High | Yes |
| Product Detail | /product/[slug] | ProductImages, Details, AddToCart | product/:slug | High | Yes |
| Coop Directory | /directory/cooperatives | CoopGrid, Filters | cooperatives | Medium | Yes |
| SE Directory | /directory/social-enterprises | SEGrid, Filters | social-enterprises | Medium | Yes |
| Coop Storefront | /coop/[shortname] | CoopHeader, ProductGrid | coop/:shortname | High | Yes |
| SE Storefront | /se/[shortname] | SEHeader, ProductGrid | se/:shortname | High | Yes |

## Consumer Portal (/consumer)

| Page | Route | Components | API Calls | Priority | Mobile? |
|------|-------|------------|-----------|----------|---------|
| Dashboard | /consumer | QuickStats, RecentOrders | consumer/dashboard | High | Yes |
| Orders | /consumer/orders | OrderList, OrderFilters | consumer/orders | High | Yes |
| Order Detail | /consumer/orders/[id] | OrderHeader, OrderItems, Timeline | consumer/orders/:id | High | Yes |
| Saved Items | /consumer/saved-items | SavedItemsGrid | consumer/saved-items | Medium | Yes |
| Profile | /consumer/profile | ProfileForm, AddressBook | consumer/profile | High | Yes |

## Seller Portal (/portal)

| Page | Route | Components | API Calls | Priority | Mobile? |
|------|-------|------------|-----------|----------|---------|
| Dashboard | /portal | SalesStats, OrderQueue, LowStock | tenant/dashboard | High | Yes |
| Products | /portal/products | ProductTable, Actions | tenant/products | High | Yes |
| Add Product | /portal/products/new | ProductForm | POST tenant/products | High | Yes |
| Edit Product | /portal/products/[id] | ProductForm | tenant/products/:id | High | Yes |
| Orders | /portal/orders | OrderTable, StatusFilters | tenant/orders | High | Yes |
| Order Detail | /portal/orders/[id] | OrderHeader, Actions | tenant/orders/:id | High | Yes |
| Inventory | /portal/inventory | InventoryTable, StockAlerts | tenant/inventory | Medium | Yes |
| Business | /portal/business | BusinessForm, Documents | tenant/business | Medium | Yes |

## Auth Pages (/auth)

| Page | Route | Components | API Calls | Priority | Mobile? |
|------|-------|------------|-----------|----------|---------|
| Login | /login | LoginForm | POST auth/login | High | Yes |
| Register | /register | RegisterForm | POST auth/register | High | Yes |
| Forgot Password | /forgot-password | ForgotForm | POST auth/forgot | Medium | Yes |
| Reset Password | /reset-password | ResetForm | POST auth/reset | Medium | Yes |

## Pages NOT Needed for Mobile

| Page | Route | Reason |
|------|-------|--------|
| CSEA Admin | /csea/* | Staff-only, desktop required |
| Academy | /academy/* | Separate app consideration |
| Dev Pages | /dev/* | Development only |
```

### Audit Checklist

- [ ] Listed all page.tsx files
- [ ] Documented route groups
- [ ] Identified dynamic routes
- [ ] Noted API dependencies
- [ ] Assigned priorities
- [ ] Marked mobile requirements
- [ ] Identified exclusions

---

## Phase 2: Page Mapping

### Purpose
Map each web page to a mobile screen with navigation structure.

### Navigation Concepts

| Web Concept | Mobile Equivalent |
|-------------|-------------------|
| Header nav links | Tab bar |
| Sidebar menu | Drawer or tabs |
| Breadcrumbs | Back button + header title |
| Modal/Dialog | Full screen or bottom sheet |
| Pagination | Infinite scroll |
| Hover states | Press states |
| Desktop tables | Card lists |

### Mapping Template

Create `docs/architecture/mobile/page-mapping.md`:

```markdown
# MoroMarket Mobile Page Mapping

## Navigation Structure

### Consumer App
```
(auth)
├── login.tsx
├── register.tsx
└── forgot-password.tsx

(consumer)
├── _layout.tsx (tabs)
└── (tabs)
    ├── home.tsx          ← / (marketplace)
    ├── search.tsx        ← /marketplace (with filters)
    ├── cart.tsx          ← /cart
    ├── orders.tsx        ← /consumer/orders
    └── profile.tsx       ← /consumer/profile

# Stack screens (pushed from tabs)
├── product/[slug].tsx    ← /product/[slug]
├── order/[id].tsx        ← /consumer/orders/[id]
├── saved-items.tsx       ← /consumer/saved-items
├── checkout.tsx          ← /checkout
└── coop/[shortname].tsx  ← /coop/[shortname]
```

### Seller App
```
(auth)
├── login.tsx
├── register.tsx
└── forgot-password.tsx

(seller)
├── _layout.tsx (tabs)
└── (tabs)
    ├── dashboard.tsx     ← /portal
    ├── products.tsx      ← /portal/products
    ├── orders.tsx        ← /portal/orders
    ├── inventory.tsx     ← /portal/inventory
    └── profile.tsx       ← /portal/business

# Stack screens (pushed from tabs)
├── product/new.tsx       ← /portal/products/new
├── product/[id].tsx      ← /portal/products/[id]
├── order/[id].tsx        ← /portal/orders/[id]
└── settings.tsx          ← Account settings
```

## Screen-by-Screen Mapping

### Consumer Screens

| Mobile Screen | Web Page | Tab | Stack From | Offline |
|---------------|----------|-----|------------|---------|
| Home | / | home | - | Cached products |
| Search | /marketplace | search | - | Cached results |
| ProductDetail | /product/[slug] | - | home, search | Cached |
| Cart | /cart | cart | - | Local storage |
| Checkout | /checkout | - | cart | Online only |
| Orders | /consumer/orders | orders | - | Cached list |
| OrderDetail | /consumer/orders/[id] | - | orders | Cached |
| SavedItems | /consumer/saved-items | - | profile | Cached |
| Profile | /consumer/profile | profile | - | Cached |
| CoopStore | /coop/[shortname] | - | home, search | Cached |

### Seller Screens

| Mobile Screen | Web Page | Tab | Stack From | Offline |
|---------------|----------|-----|------------|---------|
| Dashboard | /portal | dashboard | - | Limited |
| Products | /portal/products | products | - | Cached list |
| AddProduct | /portal/products/new | - | products | Queue |
| EditProduct | /portal/products/[id] | - | products | Queue |
| Orders | /portal/orders | orders | - | Cached list |
| OrderDetail | /portal/orders/[id] | - | orders | Cached |
| Inventory | /portal/inventory | inventory | - | Limited |
| Business | /portal/business | - | profile | Online |

## Component Mapping

| Web Component | Mobile Component | Notes |
|---------------|------------------|-------|
| DataTable | FlatList + Card | Touch-friendly |
| Modal/Dialog | Screen or BottomSheet | Full interaction |
| Form (complex) | Multi-screen wizard | Step by step |
| Sidebar | Drawer or Tabs | Platform native |
| Dropdown | ActionSheet or Picker | Platform native |
| Toast | Toast (react-native-toast) | Native feel |
| Tabs | Tabs or SegmentedControl | Simplified |
```

### Mapping Checklist

- [ ] Mapped all high-priority pages
- [ ] Defined tab structure
- [ ] Identified stack screens
- [ ] Noted offline requirements
- [ ] Planned component adaptations
- [ ] Considered platform patterns

---

## Phase 3: Architecture Design

### Purpose
Document the complete mobile app architecture before coding.

### Architecture Template

Create `docs/architecture/mobile/architecture.md`:

```markdown
# MoroMarket Mobile Architecture

## 1. Overview

### Purpose
Mobile application for the MoroMarket marketplace platform, serving:
- **Consumers**: Browse products, manage cart, place orders, track deliveries
- **Sellers**: Manage products, process orders, track inventory

### Scope
- iOS and Android platforms
- Consumer and Seller experiences
- Offline-first for BARMM connectivity
- Shared backend with web application

## 2. Tech Stack

| Layer | Technology | Version | Purpose |
|-------|------------|---------|---------|
| Framework | React Native | 0.76+ | Cross-platform |
| Build | Expo | SDK 52+ | Development & deployment |
| Language | TypeScript | 5.x | Type safety |
| Navigation | Expo Router | 4.x | File-based routing |
| Server State | TanStack Query | 5.x | Data fetching & caching |
| Local State | React Context | - | Auth, theme |
| Offline Storage | MMKV | 3.x | Fast key-value store |
| Secure Storage | Expo SecureStore | - | Tokens, credentials |
| Network | NetInfo | - | Connectivity detection |

## 3. App Structure

### Directory Layout
```
mobile/
├── app/
│   ├── (auth)/
│   │   ├── _layout.tsx
│   │   ├── login.tsx
│   │   ├── register.tsx
│   │   └── forgot-password.tsx
│   ├── (consumer)/
│   │   ├── _layout.tsx
│   │   ├── (tabs)/
│   │   │   ├── _layout.tsx
│   │   │   ├── home.tsx
│   │   │   ├── search.tsx
│   │   │   ├── cart.tsx
│   │   │   ├── orders.tsx
│   │   │   └── profile.tsx
│   │   ├── product/[slug].tsx
│   │   ├── order/[id].tsx
│   │   └── ...
│   ├── (seller)/
│   │   ├── _layout.tsx
│   │   ├── (tabs)/
│   │   │   ├── _layout.tsx
│   │   │   ├── dashboard.tsx
│   │   │   ├── products.tsx
│   │   │   ├── orders.tsx
│   │   │   ├── inventory.tsx
│   │   │   └── profile.tsx
│   │   ├── product/[id].tsx
│   │   ├── product/new.tsx
│   │   └── ...
│   └── _layout.tsx
├── components/
│   ├── ui/           # Base UI components
│   ├── consumer/     # Consumer-specific
│   └── seller/       # Seller-specific
├── lib/
│   ├── api/          # API client
│   ├── hooks/        # Custom hooks
│   ├── services/     # Business logic
│   └── storage/      # MMKV utilities
├── constants/
│   └── Colors.ts     # Design tokens
└── types/
    └── index.ts      # TypeScript types
```

## 4. State Architecture

### State Layers
```
┌─────────────────────────────────────────┐
│         React Context (Global)          │
│  - AuthContext (user, tokens, role)     │
│  - ThemeContext (dark/light mode)       │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│      TanStack Query (Server State)      │
│  - Products, Orders, Profile            │
│  - Cached, synced, invalidated          │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│          MMKV (Local Storage)           │
│  - Query cache persistence              │
│  - Cart items                           │
│  - Pending operations queue             │
└─────────────────────────────────────────┘
```

## 5. Offline Strategy

### Data Classification
| Data Type | Strategy | Offline | Sync |
|-----------|----------|---------|------|
| Products (catalog) | Cache-first | Yes | Background refresh |
| Product detail | Cache-first | Yes | On access |
| Cart | Local-first | Yes | On checkout |
| Orders (list) | Cache-first | Yes | Pull-to-refresh |
| Order detail | Cache-first | Yes | On access |
| Create order | Queue | Queued | When online |
| Profile | Network-first | Cached | On demand |
| Products (seller) | Cache-first | Yes | Background |
| Create product | Queue | Queued | When online |
| Update product | Queue | Queued | When online |

### Offline Components
1. **Network detection**: NetInfo hook monitors connectivity
2. **Offline banner**: Visual indicator when offline
3. **Pending queue**: MMKV stores operations for sync
4. **Background sync**: Processes queue when online

## 6. Security

### Authentication
- JWT access tokens (short-lived)
- Refresh tokens (long-lived)
- Stored in Expo SecureStore (encrypted)
- Auto-refresh on 401 response

### Data Protection
- No sensitive data in MMKV
- Certificate pinning (production)
- Biometric unlock (optional)

## 7. Performance Targets

| Metric | Target |
|--------|--------|
| Cold start | < 3s |
| Warm start | < 1s |
| Screen transition | < 300ms |
| API (cached) | < 100ms |
| API (network) | < 2s |
| Offline mode entry | Immediate |

## 8. Deployment

### Build Profiles
- **Development**: Local builds, hot reload
- **Preview**: Internal testing (APK/TestFlight)
- **Production**: App Store / Play Store

### OTA Updates
- EAS Update for JS-only changes
- Bypass store review for bug fixes
```

### Architecture Checklist

- [ ] Defined tech stack
- [ ] Documented directory structure
- [ ] Designed state architecture
- [ ] Planned offline strategy
- [ ] Specified security measures
- [ ] Set performance targets
- [ ] Outlined deployment strategy

---

## Output Checklist

Before starting Phase 4 (Project Setup), ensure you have:

- [ ] `docs/architecture/mobile/web-audit.md` - Complete web app audit
- [ ] `docs/architecture/mobile/page-mapping.md` - Web-to-mobile page mapping
- [ ] `docs/architecture/mobile/architecture.md` - Mobile app architecture document

These documents serve as the blueprint for mobile development.
