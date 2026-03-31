# Cooperative Manager - MoroNegosyo

## Overview
Cooperative Managers are authenticated users who manage a registered cooperative's presence on MoroNegosyo. They access the Tenant Portal to manage their shop, products, orders, members, and ensure compliance with CSEA regulations including the FRAMES compliance framework. This role represents the primary business operator on the platform.

## Role Definition
**Type**: Authenticated Tenant User
**Portal Access**: Tenant Portal (`/portal`), Public Portal (`/`), Storefront (`/coop/[slug]`)
**Authentication**: Email/Password with optional 2FA (recommended for financial access)

## Capabilities

### Core Capabilities
| Capability | Description | Priority |
|------------|-------------|----------|
| Shop Management | Configure and customize coop storefront | P0 |
| Product Management | Create, edit, archive products | P0 |
| Order Management | Process, fulfill, track orders | P0 |
| Inventory Management | Track stock levels, alerts | P0 |
| Member Management | Add, remove, manage coop members | P1 |
| Compliance Tracking | Monitor FRAMES status, upload documents | P1 |
| Financial Dashboard | View sales, revenue, payouts | P1 |
| Storefront Customization | Brand colors, logo, banner, about | P1 |
| Promotion Management | Create discounts, sales, coupons | P2 |
| Analytics Dashboard | Sales trends, customer insights | P2 |
| Training Access | Enroll in MoroAcademy courses | P2 |
| Support Requests | Contact CSEA, resolve issues | P2 |
| Team Management | Add staff with role-based access | P3 |
| Payout Configuration | Manage bank details for payouts | P3 |

### Feature Access Matrix
| Feature | Access Level | Notes |
|---------|--------------|-------|
| Tenant Dashboard | Full | Primary workspace |
| Shop Settings | Full | All configuration options |
| Product Catalog | Full | CRUD operations |
| Order Processing | Full | All order actions |
| Inventory | Full | Stock management |
| Member Directory | Full | All member operations |
| FRAMES Compliance | Full | Document upload, status view |
| Financial Reports | Full | All reports, export capability |
| Analytics | Full | All metrics, date ranges |
| Storefront Editor | Full | All customization options |
| Promotions | Full | Create, edit, deactivate |
| MoroAcademy | Full | Enroll in any course |
| Public Portal | Full | Consumer capabilities retained |
| Admin Portal | None | CSEA staff only |

## User Journey Entry Points

1. **Daily Operations Login**
   - Manager logs in to check new orders
   - Lands on Tenant Dashboard
   - Path: Login > Dashboard > Orders > Process

2. **Order Notification**
   - Manager receives new order notification
   - Clicks through to order detail
   - Path: Email/SMS > Order Detail > Process > Ship

3. **Inventory Alert**
   - Low stock notification received
   - Reviews inventory, updates stock
   - Path: Alert > Inventory > Update > Reorder supplier

4. **Compliance Deadline**
   - CSEA sends compliance reminder
   - Manager uploads required documents
   - Path: Email > Compliance > Upload > Submit

5. **Performance Review**
   - Weekly sales report email
   - Manager reviews analytics
   - Path: Email > Analytics > Identify opportunities

6. **Customer Issue**
   - Customer support request received
   - Manager resolves issue
   - Path: Notification > Messages > Respond > Resolve

## Key Pages

### Tenant Portal Pages
| Page | Purpose | Route | Implementation |
|------|---------|-------|----------------|
| Dashboard | Overview, key metrics, alerts | `/portal` | Active |
| Shop Settings | Basic shop configuration | `/portal/settings` | Active |
| Products List | All products management | `/portal/products` | Active |
| Product Create | Add new product | `/portal/products/new` | Active |
| Product Edit | Modify product | `/portal/products/[id]` | Active |
| Orders List | All orders | `/portal/orders` | Active |
| Order Detail | Single order management | `/portal/orders/[id]` | Active |
| Inventory | Stock management | `/portal/inventory` | Planned |
| Members | Member management | `/portal/members` | Planned |
| Compliance | FRAMES status, documents | `/portal/compliance` | Active |
| Analytics | Sales, traffic reports | `/portal/analytics` | Planned |
| Storefront Editor | Customize storefront | `/portal/storefront` | Planned |
| Promotions | Discounts, coupons | `/portal/promotions` | Planned |
| Financial | Sales, payouts, reports | `/portal/financials` | Planned |
| Team | Staff management | `/portal/team` | Planned |
| Training | MoroAcademy access | `/portal/training` | Planned |
| Support | Help, contact CSEA | `/portal/support` | Planned |

## Shop Management

### Shop Profile
- Cooperative name (from CDA registration)
- Business description (rich text)
- Logo (recommended 500x500px)
- Banner image (recommended 1200x400px)
- Contact information (phone, email)
- Business hours
- Physical address
- Social media links

### Storefront Customization
- Primary brand color
- Secondary accent color
- Custom URL slug (`/coop/[your-slug]`)
- Custom domain support (e.g., `www.yourcoop.ph`)
- Featured products section
- About us section
- Team/members showcase
- Certifications display
- Impact metrics display

### Business Settings
- Shipping zones and rates
- Payment methods accepted
- Order processing SLA
- Return/refund policy
- Minimum order amount
- Maximum order amount
- Product categories

## Product Management

### Product Information
| Field | Required | Description |
|-------|----------|-------------|
| Product Name | Yes | Up to 200 characters |
| Description | Yes | Rich text, min 100 characters |
| SKU | Yes | Unique identifier |
| Category | Yes | From predefined categories |
| Price | Yes | Regular price in PHP |
| Compare-at Price | No | Original price for discounts |
| Cost | No | For profit calculation |
| Images | Yes | Min 1, max 10, primary image required |
| Weight | Conditional | Required if shipping by weight |
| Dimensions | No | For shipping calculation |
| Stock Quantity | Yes | Current available stock |
| Low Stock Threshold | No | Alert trigger level |
| Variants | No | Size, color, etc. |
| Tags | No | For search optimization |

### Product States
| State | Description | Visibility |
|-------|-------------|------------|
| Draft | Work in progress | Manager only |
| Pending Review | Awaiting CSEA approval | Manager + CSEA |
| Published | Live on marketplace | Public |
| Archived | Soft deleted | Manager only |
| Out of Stock | No inventory | Public (not purchasable) |

### Bulk Operations
- CSV import/export
- Bulk price updates
- Bulk stock updates
- Bulk archive/publish
- Category reassignment

## Order Management

### Order Processing Flow
```
New Order
    ├── Review order details
    ├── Check inventory
    ├── Confirm (or reject with reason)
    │
    ├── [If confirmed]
    │   ├── Prepare order
    │   ├── Add tracking info
    │   ├── Mark as shipped
    │   │
    │   ├── [Customer receives]
    │   ├── Customer confirms receipt
    │   └── Order completed
    │
    └── [If rejected]
        ├── Notify customer
        └── Refund processed
```

### Order Actions
| Action | When Available | Description |
|--------|----------------|-------------|
| Confirm | New orders | Accept order for processing |
| Reject | New orders | Decline with reason, auto-refund |
| Add Note | Any state | Internal notes for team |
| Message Customer | Any state | Direct customer communication |
| Update Tracking | Confirmed+ | Add/update shipment tracking |
| Mark Shipped | Confirmed | Record shipment |
| Request Return | Shipped/Delivered | Initiate return process |
| Refund | Various | Full or partial refund |
| Print Packing Slip | Confirmed+ | Generate packing document |
| Print Invoice | Any state | Generate invoice document |

### Shipping Integration
- Manual tracking entry
- J&T Express integration (planned)
- LBC Express integration (planned)
- Local delivery option
- Pickup option

## Member Management (Cooperative-Specific)

### Member Types
| Type | Description | Access |
|------|-------------|--------|
| Admin | Full management rights | All features |
| Manager | Shop operations | Products, orders, inventory |
| Staff | Limited operations | View products, process orders |
| Member | Basic member | View dashboard, member benefits |

### Member Features
- Member registration/invitation
- Role assignment
- Access permission configuration
- Member directory
- Member communication
- Patronage refund tracking (planned)
- Member voting (planned)

## FRAMES Compliance

### FRAMES Components
| Component | Description | Documents |
|-----------|-------------|-----------|
| **F** - Financial | Financial health and transparency | Audited financial statements, annual reports |
| **R** - Regulatory | Regulatory compliance | CDA registration, tax clearances, permits |
| **A** - Administrative | Administrative capacity | Org structure, policies, meeting minutes |
| **M** - Membership | Membership management | Member list, share capital, education |
| **E** - Economic | Economic performance | Business plan, volume of business |
| **S** - Social | Social responsibility | Community projects, environmental initiatives |

### Compliance Dashboard
- Overall compliance score
- Component-wise scores
- Missing document alerts
- Upcoming deadline reminders
- Document upload interface
- Submission history
- CSEA feedback/comments

### Compliance Status
| Status | Description | Action |
|--------|-------------|--------|
| Compliant | All requirements met | Maintain |
| At Risk | Some documents pending | Upload soon |
| Non-Compliant | Critical issues | Immediate action |
| Under Review | Documents being verified | Wait for CSEA |

## Training Access (MoroAcademy)

### Available Training
- Cooperative management courses
- E-commerce best practices
- Product photography
- Customer service excellence
- Financial literacy
- Digital marketing
- Sustainable business practices

### Training Features
- Progress tracking
- Certificates upon completion
- Team training enrollment
- Training history
- Skill badges

## Role Progression

**From**: Consumer (after coop registration approval)
**To**:
- Multi-coop Manager (managing multiple coops)
- Federation Manager (future, for coop federations)

**Requirements to Become Coop Manager**:
- Valid CDA registration
- CSEA application submission
- Document verification
- CSEA approval
- Account activation

## Pain Points

1. **Complex Onboarding**
   - Many documents required for registration
   - Unclear requirements upfront
   - Impact: Delayed activation, frustration

2. **Inventory Sync Challenges**
   - Manual stock updates
   - No POS integration
   - Impact: Overselling, manual work

3. **Compliance Document Management**
   - Finding correct document versions
   - Understanding requirements
   - Impact: Non-compliance risks

4. **Limited Analytics**
   - Basic sales data only
   - No customer insights
   - Impact: Missed opportunities

5. **Order Fulfillment Bottlenecks**
   - Manual shipping process
   - No bulk order processing
   - Impact: Slow fulfillment

6. **Member Coordination**
   - No integrated communication tools
   - Separate systems for member management
   - Impact: Coordination overhead

## Improvement Opportunities

1. **Guided Onboarding**
   - Step-by-step registration wizard
   - Document checklist with progress
   - Sample documents as reference
   - Video tutorials per step

2. **Inventory Automation**
   - Low stock auto-alerts
   - Supplier reorder suggestions
   - Simple POS integration
   - Batch update tools

3. **Compliance Assistant**
   - AI document verification
   - Deadline prediction
   - Compliance score gamification
   - Peer benchmarking

4. **Advanced Analytics**
   - Customer demographics
   - Product performance
   - Sales forecasting
   - Competitor benchmarking

5. **Fulfillment Optimization**
   - Batch order processing
   - Shipping label printing
   - Carrier rate comparison
   - Delivery route optimization

6. **Member Portal**
   - Dedicated member app/portal
   - In-app communication
   - Member voting system
   - Patronage refund calculation

## Success Metrics

### Business Metrics
- **Monthly Gross Sales**: Total sales per month (target: growing MoM)
- **Order Count**: Total orders processed (target: 50+ monthly)
- **Average Order Value**: Mean order value (target: PHP 500+)
- **Order Fulfillment Time**: Hours from order to ship (target: < 48 hours)

### Operational Metrics
- **Inventory Accuracy**: Stock count accuracy (target: 98%+)
- **Order Acceptance Rate**: % orders accepted (target: 95%+)
- **Return Rate**: % orders returned (target: < 5%)
- **Customer Response Time**: Hours to respond (target: < 24 hours)

### Compliance Metrics
- **FRAMES Score**: Overall compliance percentage (target: 85%+)
- **Document Currency**: % documents up to date (target: 100%)
- **On-Time Submission**: % documents submitted before deadline (target: 100%)

### Growth Metrics
- **Product Catalog Growth**: New products per month (target: 5+)
- **Customer Acquisition**: New customers per month
- **Repeat Customer Rate**: % returning customers (target: 30%+)
- **Storefront Traffic**: Monthly unique visitors

### Member Metrics (Cooperative-Specific)
- **Active Members**: % of members active on platform
- **Member Participation**: Training completion rate
- **Member Transactions**: % of sales to members

---

## Implementation Plan

### Access Control
- **Authentication required**: All `/portal/*` routes require authenticated tenant user
- **Middleware**: `frontend/src/middleware.ts` - tenant auth guards for `(tenant)` route group
- **Tenant scoping**: All data operations scoped to user's assigned tenant (cooperative)
- **Permission checks**: User must have `coop_manager` or `coop_admin` role on tenant
- **2FA recommended**: Prompt for 2FA setup on first login, required for financial access

```typescript
// frontend/src/middleware.ts
const tenantRoutes = ['/portal'];
// Verify: authenticated + has tenant + role is coop_manager/coop_admin
// Inject tenant context into all API calls via X-Tenant-ID header
```

### Priority Pages

#### P0 - Core Operations
| Page | Route | File Path |
|------|-------|-----------|
| Dashboard | `/portal` | `frontend/src/app/(tenant)/portal/page.tsx` |
| Shop Settings | `/portal/settings` | `frontend/src/app/(tenant)/portal/settings/page.tsx` |
| Products List | `/portal/products` | `frontend/src/app/(tenant)/portal/products/page.tsx` |
| Product Create | `/portal/products/new` | `frontend/src/app/(tenant)/portal/products/new/page.tsx` |
| Product Edit | `/portal/products/[id]` | `frontend/src/app/(tenant)/portal/products/[id]/page.tsx` |
| Orders List | `/portal/orders` | `frontend/src/app/(tenant)/portal/orders/page.tsx` |
| Order Detail | `/portal/orders/[id]` | `frontend/src/app/(tenant)/portal/orders/[id]/page.tsx` |

#### P1 - Compliance & Members
| Page | Route | File Path |
|------|-------|-----------|
| Compliance Dashboard | `/portal/compliance` | `frontend/src/app/(tenant)/portal/compliance/page.tsx` |
| FRAMES Status | `/portal/compliance/frames` | `frontend/src/app/(tenant)/portal/compliance/frames/page.tsx` |
| Document Upload | `/portal/compliance/documents` | `frontend/src/app/(tenant)/portal/compliance/documents/page.tsx` |
| Members List | `/portal/members` | `frontend/src/app/(tenant)/portal/members/page.tsx` |
| Member Detail | `/portal/members/[id]` | `frontend/src/app/(tenant)/portal/members/[id]/page.tsx` |
| Inventory | `/portal/inventory` | `frontend/src/app/(tenant)/portal/inventory/page.tsx` |
| Financial Dashboard | `/portal/financials` | `frontend/src/app/(tenant)/portal/financials/page.tsx` |

#### P2 - Growth & Engagement
| Page | Route | File Path |
|------|-------|-----------|
| Analytics | `/portal/analytics` | `frontend/src/app/(tenant)/portal/analytics/page.tsx` |
| Storefront Editor | `/portal/storefront` | `frontend/src/app/(tenant)/portal/storefront/page.tsx` |
| Promotions | `/portal/promotions` | `frontend/src/app/(tenant)/portal/promotions/page.tsx` |
| Promotion Create | `/portal/promotions/new` | `frontend/src/app/(tenant)/portal/promotions/new/page.tsx` |
| Training | `/portal/training` | `frontend/src/app/(tenant)/portal/training/page.tsx` |
| Support | `/portal/support` | `frontend/src/app/(tenant)/portal/support/page.tsx` |

#### P3 - Team & Advanced
| Page | Route | File Path |
|------|-------|-----------|
| Team Management | `/portal/team` | `frontend/src/app/(tenant)/portal/team/page.tsx` |
| Payout Settings | `/portal/financials/payouts` | `frontend/src/app/(tenant)/portal/financials/payouts/page.tsx` |

### Role-Specific Components

| Component | Path | Purpose |
|-----------|------|---------|
| TenantSidebar | `frontend/src/components/portal/tenant-sidebar.tsx` | Portal navigation |
| DashboardStats | `frontend/src/components/portal/dashboard-stats.tsx` | Key metrics cards |
| RecentOrders | `frontend/src/components/portal/recent-orders.tsx` | Dashboard order list |
| ComplianceAlert | `frontend/src/components/portal/compliance-alert.tsx` | Compliance warnings |
| ProductForm | `frontend/src/components/portal/products/product-form.tsx` | Add/edit product |
| ProductTable | `frontend/src/components/portal/products/product-table.tsx` | Product data table |
| ProductImageUpload | `frontend/src/components/portal/products/product-image-upload.tsx` | Multi-image upload |
| VariantEditor | `frontend/src/components/portal/products/variant-editor.tsx` | Product variants |
| OrderTable | `frontend/src/components/portal/orders/order-table.tsx` | Orders data table |
| OrderActions | `frontend/src/components/portal/orders/order-actions.tsx` | Confirm/ship/cancel |
| OrderTimeline | `frontend/src/components/portal/orders/order-timeline.tsx` | Processing timeline |
| ShippingForm | `frontend/src/components/portal/orders/shipping-form.tsx` | Add tracking info |
| FRAMESCard | `frontend/src/components/portal/compliance/frames-card.tsx` | FRAMES component score |
| FRAMESProgress | `frontend/src/components/portal/compliance/frames-progress.tsx` | Overall compliance |
| DocumentUploader | `frontend/src/components/portal/compliance/document-uploader.tsx` | Document upload |
| DocumentList | `frontend/src/components/portal/compliance/document-list.tsx` | Submitted docs |
| MemberTable | `frontend/src/components/portal/members/member-table.tsx` | Member directory |
| MemberInviteForm | `frontend/src/components/portal/members/member-invite-form.tsx` | Invite member |
| InventoryTable | `frontend/src/components/portal/inventory/inventory-table.tsx` | Stock levels |
| LowStockAlert | `frontend/src/components/portal/inventory/low-stock-alert.tsx` | Stock warnings |
| SalesChart | `frontend/src/components/portal/analytics/sales-chart.tsx` | Sales over time |
| RevenueCard | `frontend/src/components/portal/financials/revenue-card.tsx` | Revenue summary |
| StorefrontPreview | `frontend/src/components/portal/storefront/storefront-preview.tsx` | Live preview |
| BannerUpload | `frontend/src/components/portal/storefront/banner-upload.tsx` | Storefront banner |
| PromotionForm | `frontend/src/components/portal/promotions/promotion-form.tsx` | Create discount |
| CouponGenerator | `frontend/src/components/portal/promotions/coupon-generator.tsx` | Generate codes |

### API Endpoints Required

| Endpoint | Method | Location | Purpose |
|----------|--------|----------|---------|
| `/api/tenant/profile` | GET/PATCH | `backend/apps/tenant/api.py` | Tenant profile |
| `/api/tenant/settings` | GET/PATCH | `backend/apps/tenant/api.py` | Business settings |
| `/api/tenant/products` | GET/POST | `backend/apps/products/api.py` | Product management |
| `/api/tenant/products/{id}` | GET/PATCH/DELETE | `backend/apps/products/api.py` | Single product ops |
| `/api/tenant/products/bulk` | POST | `backend/apps/products/api.py` | Bulk operations |
| `/api/tenant/products/import` | POST | `backend/apps/products/api.py` | CSV import |
| `/api/tenant/orders` | GET | `backend/apps/orders/api.py` | Tenant orders |
| `/api/tenant/orders/{id}` | GET/PATCH | `backend/apps/orders/api.py` | Order detail/update |
| `/api/tenant/orders/{id}/confirm` | POST | `backend/apps/orders/api.py` | Confirm order |
| `/api/tenant/orders/{id}/ship` | POST | `backend/apps/orders/api.py` | Mark shipped |
| `/api/tenant/orders/{id}/cancel` | POST | `backend/apps/orders/api.py` | Cancel order |
| `/api/tenant/inventory` | GET/PATCH | `backend/apps/products/api.py` | Stock management |
| `/api/tenant/compliance` | GET | `backend/apps/compliance/api.py` | Compliance status |
| `/api/tenant/compliance/frames` | GET | `backend/apps/compliance/api.py` | FRAMES breakdown |
| `/api/tenant/compliance/documents` | GET/POST | `backend/apps/compliance/api.py` | Document management |
| `/api/tenant/members` | GET/POST | `backend/apps/tenant/api.py` | Member management |
| `/api/tenant/members/{id}` | GET/PATCH/DELETE | `backend/apps/tenant/api.py` | Single member ops |
| `/api/tenant/members/invite` | POST | `backend/apps/tenant/api.py` | Invite member |
| `/api/tenant/analytics` | GET | `backend/apps/analytics/api.py` | Sales analytics |
| `/api/tenant/financials` | GET | `backend/apps/financials/api.py` | Financial reports |
| `/api/tenant/financials/payouts` | GET/PATCH | `backend/apps/financials/api.py` | Payout config |
| `/api/tenant/storefront` | GET/PATCH | `backend/apps/tenant/api.py` | Storefront settings |
| `/api/tenant/promotions` | GET/POST | `backend/apps/promotions/api.py` | Promotions |
| `/api/tenant/promotions/{id}` | GET/PATCH/DELETE | `backend/apps/promotions/api.py` | Single promotion |
| `/api/tenant/team` | GET/POST | `backend/apps/tenant/api.py` | Team members |
| `/api/tenant/team/{id}` | PATCH/DELETE | `backend/apps/tenant/api.py` | Team member ops |
| `/api/tenant/support` | GET/POST | `backend/apps/support/api.py` | Support tickets |

### Implementation Sequence

#### Phase 1: Dashboard & Products (Week 1-3)
1. Tenant authentication and context injection
2. Dashboard with key metrics (orders, revenue, compliance)
3. Product list with search, filter, pagination
4. Product create/edit forms with image upload
5. Product state management (draft, published, archived)
6. Basic shop settings page

#### Phase 2: Order Management (Week 4-5)
1. Order list with status filters
2. Order detail with customer info, items, totals
3. Order actions (confirm, reject with reason)
4. Shipping/tracking info entry
5. Order state transitions and notifications
6. Packing slip and invoice generation

#### Phase 3: Compliance & FRAMES (Week 6-7)
1. Compliance dashboard with overall status
2. FRAMES component breakdown cards
3. Document upload with categorization
4. Document list with status tracking
5. Deadline alerts and reminders
6. Compliance history view

#### Phase 4: Members & Inventory (Week 8-9)
1. Member directory with search
2. Member invite flow
3. Member role assignment
4. Inventory management table
5. Low stock alerts
6. Bulk stock updates

#### Phase 5: Analytics & Financials (Week 10-11)
1. Sales analytics with charts
2. Revenue and payout summaries
3. Date range filtering
4. Export to CSV/Excel
5. Basic financial reports
6. Payout configuration

#### Phase 6: Storefront & Growth (Week 12-14)
1. Storefront editor (logo, banner, colors)
2. Storefront preview
3. Custom domain configuration
4. Promotion creation (discounts, coupons)
5. Training/MoroAcademy integration
6. Team management with role-based access

---

## Implementation Status

*Audited: December 30, 2025*

### Key Pages Status

| Page | Status | Path | Notes |
|------|--------|------|-------|
| Dashboard | ✅ Implemented | `frontend/src/app/(tenant)/dashboard/page.tsx` | Route is `/dashboard` not `/portal` |
| Login | ✅ Implemented | `frontend/src/app/(tenant)/login/page.tsx` | Tenant login |
| Register | ✅ Implemented | `frontend/src/app/(tenant)/register/page.tsx` | Tenant registration |
| Profile | ✅ Implemented | `frontend/src/app/(tenant)/profile/page.tsx` | Manager profile |
| Shop Overview | ✅ Implemented | `frontend/src/app/(tenant)/shop/page.tsx` | Shop management |
| Products List | ✅ Implemented | `frontend/src/app/(tenant)/shop/products/page.tsx` | Route is `/shop/products` |
| Business Profile | ✅ Implemented | `frontend/src/app/(tenant)/business/page.tsx` | Business info |
| Business Documents | ✅ Implemented | `frontend/src/app/(tenant)/business/documents/page.tsx` | Document management |
| Compliance | ✅ Implemented | `frontend/src/app/(tenant)/compliance/page.tsx` | FRAMES compliance |
| Finances | ✅ Implemented | `frontend/src/app/(tenant)/finances/page.tsx` | Financial dashboard |
| Impact Dashboard | ✅ Implemented | `frontend/src/app/(tenant)/impact/page.tsx` | Impact tracking |
| Impact Create | ✅ Implemented | `frontend/src/app/(tenant)/impact/new/page.tsx` | New impact story |
| Impact Detail | ✅ Implemented | `frontend/src/app/(tenant)/impact/[id]/page.tsx` | Single impact story |
| Members List | ✅ Implemented | `frontend/src/app/(tenant)/members/page.tsx` | Member management |
| Member Create | ✅ Implemented | `frontend/src/app/(tenant)/members/new/page.tsx` | Add member |
| Training | ✅ Implemented | `frontend/src/app/(tenant)/training/page.tsx` | MoroAcademy access |
| Training Courses | ✅ Implemented | `frontend/src/app/(tenant)/training/courses/page.tsx` | Course catalog |
| Training Workshops | ✅ Implemented | `frontend/src/app/(tenant)/training/workshops/page.tsx` | Workshop catalog |
| Settings | ✅ Implemented | `frontend/src/app/(tenant)/settings/page.tsx` | General settings |
| Domain Settings | ✅ Implemented | `frontend/src/app/(tenant)/settings/domains/page.tsx` | Custom domains |
| Product Create | ❌ Not Found | - | No `/shop/products/new` page |
| Product Edit | ❌ Not Found | - | No `/shop/products/[id]` page |
| Orders List | ❌ Not Found | - | No orders management page |
| Order Detail | ❌ Not Found | - | No single order page |
| Inventory | ❌ Not Found | - | No inventory page |
| Analytics | ❌ Not Found | - | No analytics page |
| Storefront Editor | ❌ Not Found | - | No storefront customization |
| Promotions | ❌ Not Found | - | No promotions page |
| Team | ❌ Not Found | - | No team management |
| Support | ❌ Not Found | - | No support page |

### API Endpoints Status

| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| Tenant Profile | ✅ Implemented | `/tenant/profile` | Business profile |
| Tenant Products | ✅ Implemented | `/tenant/products` | Product CRUD |
| Tenant Orders | ✅ Implemented | `/tenant/orders` | Order management |
| Tenant Analytics | ✅ Implemented | `/tenant/analytics` | Sales analytics |
| Tenant Reviews | ✅ Implemented | `/tenant/reviews` | Product reviews |
| Tenant Storefront | ✅ Implemented | `/tenant/storefront` | Storefront config |
| Tenant Impact | ✅ Implemented | `/tenant/impact` | Impact stories |
| Tenant Members | ✅ Implemented | `/tenant/members` | Member management |
| Tenant Documents | ✅ Implemented | `/tenant/documents` | Document upload |
| Core Compliance | ✅ Implemented | `/core/compliance` | FRAMES status |
| Core Dashboard Metrics | ✅ Implemented | `/core/dashboard/metrics` | Dashboard stats |
| Core Members | ✅ Implemented | `/core/members` | Member operations |
| Shop Products | ✅ Implemented | `/core/shop/products` | Shop products |
| Shop Orders | ✅ Implemented | `/core/shop/orders` | Shop orders |
| Inventory | ❌ Not Found | - | No dedicated inventory API |
| Promotions | ❌ Not Found | - | No promotions API |
| Team Management | ❌ Not Found | - | No team API |
| Support Tickets | ❌ Not Found | - | No support API |

### Overall Progress

- **Pages**: 20/30 implemented (67%)
- **APIs**: 14/18 implemented (78%)

### Notes

1. **Route Structure**: Uses `/dashboard` instead of `/portal` as main tenant area
2. **Product CRUD**: Product list exists but create/edit pages not found
3. **Orders Missing**: No order management pages despite API existing
4. **Members Complete**: Full member management flow implemented
5. **Compliance Ready**: FRAMES compliance dashboard implemented
6. **Impact Tracking**: Impact stories CRUD fully implemented
7. **Training Integration**: MoroAcademy integration with courses and workshops
8. **Custom Domains**: Domain configuration available in settings
9. **Missing Features**: Inventory, analytics pages, promotions, team management, storefront editor
