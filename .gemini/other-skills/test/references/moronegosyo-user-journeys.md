# MoroNegosyo E-Commerce Platform - User Journeys & Test Coverage

## Implementation Status Summary

**Last Updated:** December 30, 2025

### Overall Progress

| Portal | Status | Progress |
|--------|--------|----------|
| **Public Portal** | Fully Implemented | 100% |
| **Tenant Portal** | Mostly Implemented | ~85% |
| **Agency Admin Portal** | Mostly Implemented | ~90% |
| **Cooperative Storefronts** | Fully Implemented | 100% |
| **SE Storefronts** | Fully Implemented | 100% |
| **Registration Flows** | Fully Implemented | 100% |

### Status Legend

| Marker | Meaning |
|--------|---------|
| Done | Feature is fully implemented and functional |
| Partial | Feature exists but is incomplete or has limited functionality |
| Pending | Feature is not yet implemented |

### Key Outstanding Items

| Feature | Status | Notes |
|---------|--------|-------|
| Wishlist | Pending | No UI implementation |
| Loyalty Points Display/Usage | Pending | Backend schema may exist, no UI |
| Product Reviews System | Partial | Schema exists, UI partial |
| PayMongo Payment Gateway | Partial | COD works, e-wallet partial |
| Email Notifications | Partial | Basic notifications work |
| Certificate Generation (Coops) | Pending | Not implemented |
| Platform Fees/Commission Tracking | Pending | Not implemented |
| Storefront Live Preview | Partial | Settings exist, preview limited |
| Product Variants UI | Partial | Backend exists, UI incomplete |
| Order Status Updates | Partial | List exists, full workflow partial |
| Compliance Review Workflow | Partial | Basic review exists |

---

## Platform Architecture

```text
MoroNegosyo Platform
├── Public Portal (/)
│   ├── Marketplace (products from all coops/SEs)
│   ├── Cooperative Directory
│   ├── Social Enterprise Directory
│   ├── Product Detail Pages
│   ├── Cart & Checkout
│   └── User Registration/Login
│
├── Tenant Portal (/tenant)
│   ├── Dashboard (metrics, compliance banner)
│   ├── Shop Management (products, orders, storefront)
│   ├── Business Profile
│   ├── Compliance Tracking (STEPS/PESOS)
│   ├── Member Management
│   ├── Impact Stories
│   └── Settings
│
├── Agency Admin Portal (/agency)
│   ├── Dashboard (alerts, pending items)
│   ├── Registration Oversight
│   ├── Formation Tracking
│   ├── Auditing & Compliance
│   ├── Monitoring & Analytics
│   ├── Manager Applications
│   └── Sustainability Programs
│
├── Cooperative Storefronts (/coop/[shortname])
│   ├── Homepage with Hero
│   ├── Shop/Product Catalog
│   ├── Product Detail
│   ├── Cart & Checkout
│   ├── Business Info
│   ├── Profile (About)
│   └── Impact Stories
│
└── SE Storefronts (/se/[shortname])
    └── (Same structure as Cooperative Storefronts)
```

---

## Section 1: User Roles

| Role | Description | Primary Portal | Authentication |
|------|-------------|----------------|----------------|
| **Anonymous User** | Public visitor, no account | Public, Storefronts | None |
| **Consumer** | Registered marketplace user | Public, Storefronts | Email/Password |
| **Tenant Manager** | Coop/SE organization manager | Tenant Portal | Email/Password + Tenant Link |
| **CSEA Staff** | Agency staff member | Agency Admin | Email/Password + Admin Role |
| **CSEA Approver** | Staff with approval authority | Agency Admin | Email/Password + Approval Authority |
| **Django Superuser** | System administrator | All Portals + Django Admin | Superuser Flag |

### Role Progression

```text
Anonymous → Consumer (Register)
Consumer → Tenant Manager (Manager Application Approved)
Consumer → CSEA Staff (Admin Onboarding)
Tenant Manager can also be Consumer (multi-role)
```

---

## Section 2: Anonymous User Journeys

### 2.1 Browse Public Marketplace - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to `/` | Homepage loads with featured products | E2E, Integration | Done |
| 2 | Click "Marketplace" | Browse page shows products from all vendors | E2E | Done |
| 3 | Filter by category | Product list filters correctly | E2E, Unit | Done |
| 4 | Filter by vendor type (Coop/SE) | Only matching products shown | E2E, Unit | Done |
| 5 | Search for product | Search results relevant | E2E, Integration | Done |
| 6 | Sort by price/date | Products reorder correctly | E2E, Unit | Done |
| 7 | Click product card | Product detail page opens | E2E | Done |
| 8 | View product images | Image gallery works | E2E | Done |
| 9 | See vendor info | Links to storefront | E2E | Done |

### 2.2 Browse Directories - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to `/cooperatives` | Cooperative directory loads | E2E | Done |
| 2 | Filter by province/municipality | Results filter geographically | E2E, Unit | Done |
| 3 | Filter by cooperative type | Results filter by type | E2E, Unit | Done |
| 4 | Click cooperative card | Detail page shows profile | E2E | Done |
| 5 | Navigate to `/social-enterprises` | SE directory loads | E2E | Done |
| 6 | Filter by sector | Results filter by sector | E2E, Unit | Done |
| 7 | Filter by SDG alignment | Results filter by SDGs | E2E, Unit | Done |
| 8 | Click SE card | Detail page shows profile | E2E | Done |

### 2.3 Visit Individual Storefront - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to `/coop/[shortname]` | Storefront homepage loads | E2E | Done |
| 2 | See hero banner | Custom hero displays | E2E | Done |
| 3 | See featured products | Featured products section | E2E | Done |
| 4 | Navigate to shop | Product catalog displays | E2E | Done |
| 5 | Filter products | Store-specific filters work | E2E, Unit | Done |
| 6 | View product detail | Product page with add to cart | E2E | Done |
| 7 | Add to cart | Item added to storefront cart | E2E, Integration | Done |
| 8 | View cart | Cart shows items, totals | E2E | Done |
| 9 | Navigate to business info | Contact, hours, location shown | E2E | Done |
| 10 | View impact stories | Impact carousel/grid displays | E2E | Done |

### 2.4 Guest Checkout (Storefront) - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Add items to cart | Cart updates | E2E, Integration | Done |
| 2 | Click checkout | Checkout page loads | E2E | Done |
| 3 | Enter customer info | Form validates fields | E2E, Unit | Done |
| 4 | Enter shipping address | Address form validates | E2E, Unit | Done |
| 5 | Select shipping method | Options show with pricing | E2E | Done |
| 6 | Select payment method | COD, GCash, etc. options | E2E | Partial |
| 7 | Review order | Summary shows all details | E2E | Done |
| 8 | Place order | Order created, confirmation shown | E2E, Integration | Done |
| 9 | Receive order number | Unique order number generated | Integration | Done |
| 10 | Order appears in tenant dashboard | Vendor sees new order | Integration | Done |

---

## Section 3: Consumer Journeys

### 3.1 Registration - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to `/register` | Registration form loads | E2E | Done |
| 2 | Enter email | Email validated | E2E, Unit | Done |
| 3 | Enter password | Password strength validated | E2E, Unit | Done |
| 4 | Enter name | Name fields validated | E2E, Unit | Done |
| 5 | Submit form | Account created | E2E, Integration | Done |
| 6 | Verification email sent | Email queued | Integration | Partial |
| 7 | Click verification link | Email verified | Integration | Partial |
| 8 | Login with credentials | Successfully authenticated | E2E, Integration | Done |

### 3.2 Login - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to `/login` | Login form loads | E2E | Done |
| 2 | Enter credentials | Form validates | E2E, Unit | Done |
| 3 | Click login | JWT issued, user authenticated | E2E, Integration | Done |
| 4 | Access protected routes | Consumer routes accessible | Integration | Done |
| 5 | Invalid credentials | Error message shown | E2E, Unit | Done |
| 6 | Account lockout (5 attempts) | Account locked temporarily | Integration, Unit | Done |

### 3.3 Customer Profile Management - Partial

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Access profile section | Profile loads | E2E | Done |
| 2 | Update name | Changes saved | E2E, Integration | Done |
| 3 | Update phone number | Phone validated, saved | E2E, Unit | Done |
| 4 | Add shipping address | Address added to list | E2E, Integration | Done |
| 5 | Set default address | Default flag updated | E2E, Integration | Done |
| 6 | Delete address | Address removed | E2E, Integration | Done |
| 7 | View wishlist | Saved products shown | E2E | Pending |
| 8 | Add to wishlist | Product added | E2E, Integration | Pending |
| 9 | Remove from wishlist | Product removed | E2E, Integration | Pending |
| 10 | View loyalty points | Points balance shown | E2E | Pending |

### 3.4 Authenticated Checkout - Partial

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Add items to cart | Cart syncs with account | E2E, Integration | Done |
| 2 | Start checkout | Saved addresses pre-filled | E2E | Done |
| 3 | Select saved address | Address selected | E2E | Done |
| 4 | Complete order | Order linked to account | E2E, Integration | Done |
| 5 | View order history | Order appears in history | E2E, Integration | Done |
| 6 | Track order status | Status updates shown | E2E, Integration | Done |
| 7 | Earn loyalty points | Points credited | Integration | Pending |

### 3.5 Product Reviews - Partial

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to purchased product | Review option available | E2E | Partial |
| 2 | Click "Write Review" | Review form opens | E2E | Partial |
| 3 | Select rating (1-5 stars) | Stars selected | E2E | Partial |
| 4 | Enter review title | Title validated | E2E, Unit | Partial |
| 5 | Enter review content | Content validated | E2E, Unit | Partial |
| 6 | Upload images (optional) | Images uploaded | E2E, Integration | Partial |
| 7 | Submit review | Review created (pending) | E2E, Integration | Partial |
| 8 | Review approved by vendor | Review becomes visible | Integration | Pending |
| 9 | Verified purchase badge | Badge shown if order linked | Integration | Pending |
| 10 | Owner responds | Response shown under review | Integration | Pending |

---

## Section 4: Consumer -> Tenant Manager Journey

### 4.1 Manager Application - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to manager application | Application form loads | E2E | Done |
| 2 | Search for organization | Registered coops/SEs shown | E2E, Integration | Done |
| 3 | Select organization | Org details displayed | E2E | Done |
| 4 | Enter position title | Title validated | E2E, Unit | Done |
| 5 | Enter position description | Description validated | E2E, Unit | Done |
| 6 | Upload Board Resolution | Document uploaded | E2E, Integration | Done |
| 7 | Upload Government ID | Document uploaded | E2E, Integration | Done |
| 8 | Upload additional docs | Documents uploaded | E2E, Integration | Done |
| 9 | Save as draft | Draft saved | E2E, Integration | Done |
| 10 | Submit application | Status -> PENDING | E2E, Integration | Done |
| 11 | View application status | Status page shows progress | E2E | Done |
| 12 | Respond to info request | Additional info submitted | E2E, Integration | Done |

### 4.2 Manager Application Admin Review - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | CSEA Approver views inbox | Application appears | E2E | Done |
| 2 | Click to review | Application details shown | E2E | Done |
| 3 | Verify documents | Each document reviewed | E2E | Done |
| 4 | Request more info | Status -> INFO_REQUESTED | E2E, Integration | Done |
| 5 | Approve application | Status -> APPROVED | E2E, Integration | Done |
| 6 | User upgraded to tenant role | Role added to user | Integration | Done |
| 7 | OrganizationManager created | Manager record created | Integration | Done |
| 8 | Reject application | Status -> REJECTED, reason provided | E2E, Integration | Done |

---

## Section 5: Tenant Manager Journeys

### 5.1 Dashboard - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Login as tenant | Redirect to `/tenant/dashboard` | E2E | Done |
| 2 | View metrics grid | Key metrics displayed | E2E | Done |
| 3 | See compliance banner | Compliance status shown | E2E | Done |
| 4 | View quick actions | Action buttons available | E2E | Done |
| 5 | See recent activity | Activity feed shown | E2E | Done |
| 6 | Data scoped to tenant | Only own organization's data | Integration, Security | Done |

### 5.2 Product Management - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to Shop | Products tab shown | E2E | Done |
| 2 | View products table | Products listed with pagination | E2E | Done |
| 3 | Click "Add Product" | Product form opens | E2E | Done |
| 4 | Enter product name | Name validated | E2E, Unit | Done |
| 5 | Enter description | Description saved | E2E | Done |
| 6 | Set price | Price validated (positive number) | E2E, Unit | Done |
| 7 | Set compare-at price | Optional sale price | E2E | Done |
| 8 | Select category | Category dropdown | E2E | Done |
| 9 | Enter SKU | SKU validated (unique) | E2E, Unit | Done |
| 10 | Set stock quantity | Stock validated | E2E, Unit | Done |
| 11 | Set low stock threshold | Threshold saved | E2E | Done |
| 12 | Upload product images | Images uploaded to storage | E2E, Integration | Done |
| 13 | Set featured flag | Featured products highlighted | E2E | Done |
| 14 | Save product | Product created | E2E, Integration | Done |
| 15 | Edit product | Changes saved | E2E, Integration | Done |
| 16 | Delete product | Soft delete/confirmation | E2E, Integration | Done |

### 5.3 Product Variants - Partial

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Edit product | Variants tab shown | E2E | Partial |
| 2 | Add variant option (Size) | Option created | E2E, Integration | Partial |
| 3 | Add values (S, M, L) | Values saved | E2E, Integration | Partial |
| 4 | Add variant option (Color) | Second option created | E2E, Integration | Partial |
| 5 | Generate variants | Matrix of variants created | E2E, Integration | Partial |
| 6 | Set variant prices | Individual pricing | E2E | Partial |
| 7 | Set variant stock | Individual inventory | E2E | Partial |
| 8 | Upload variant images | Per-variant images | E2E, Integration | Pending |

### 5.4 Order Management - Partial

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to Orders tab | Orders table loads | E2E | Done |
| 2 | Filter by status | Orders filtered | E2E, Unit | Done |
| 3 | Search by order number | Search works | E2E | Done |
| 4 | Click order row | Order detail opens | E2E | Done |
| 5 | View order items | Items with quantities | E2E | Done |
| 6 | View customer info | Contact details shown | E2E | Done |
| 7 | View shipping address | Address shown | E2E | Done |
| 8 | Update status -> Processing | Status updated, timeline entry | E2E, Integration | Partial |
| 9 | Update status -> Shipped | Status updated | E2E, Integration | Partial |
| 10 | Update status -> Delivered | Status updated | E2E, Integration | Partial |
| 11 | Cancel order | Status -> Cancelled | E2E, Integration | Partial |
| 12 | Add order notes | Notes saved | E2E, Integration | Partial |
| 13 | View order timeline | All status changes shown | E2E | Partial |

### 5.5 Storefront Customization - Partial

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to Storefront tab | Builder loads | E2E | Done |
| 2 | Configure theme colors | Primary/secondary colors | E2E | Done |
| 3 | Upload hero image | Image uploaded | E2E, Integration | Done |
| 4 | Set hero text | Title/subtitle saved | E2E | Done |
| 5 | Configure CTA button | Text and link saved | E2E | Done |
| 6 | Select featured products | Products selected | E2E | Done |
| 7 | Preview changes | Live preview updates | E2E | Partial |
| 8 | Toggle device preview | Mobile/desktop views | E2E | Partial |
| 9 | Save settings | StorefrontSettings updated | E2E, Integration | Done |
| 10 | Publish changes | Changes live on storefront | E2E, Integration | Done |

### 5.6 Business Profile Management - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to Business | Business page loads | E2E | Done |
| 2 | Edit basic info | Name, description editable | E2E | Done |
| 3 | Update contact info | Email, phone, address | E2E | Done |
| 4 | Set operating hours | Hours editor works | E2E | Done |
| 5 | Upload documents | Documents uploaded | E2E, Integration | Done |
| 6 | View document status | PENDING/VERIFIED shown | E2E | Done |
| 7 | Save changes | TenantDraftState updated | E2E, Integration | Done |
| 8 | Publish profile | Changes go live | E2E, Integration | Done |

### 5.7 Member Management (Cooperatives) - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to Members | Members page loads | E2E | Done |
| 2 | View members table | Members listed | E2E | Done |
| 3 | Add new member | Form opens | E2E | Done |
| 4 | Enter member details | All fields validated | E2E, Unit | Done |
| 5 | Assign role | OWNER/MANAGER/MEMBER/SALES/EDITOR | E2E | Done |
| 6 | Set portal access | Toggle access flag | E2E | Done |
| 7 | Save member | Member created | E2E, Integration | Done |
| 8 | Edit member | Changes saved | E2E, Integration | Done |
| 9 | View member metrics | Member count, share capital totals | E2E | Done |

### 5.8 Compliance Tracking - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to Compliance | Compliance page loads | E2E | Done |
| 2 | View STEPS indicators | Performance metrics shown | E2E | Done |
| 3 | View PESOS indicators | Lending metrics shown (if applicable) | E2E | Done |
| 4 | View submission history | Past submissions listed | E2E | Done |
| 5 | Submit new report | Upload form opens | E2E | Done |
| 6 | Select submission type | CAFS/PAR/SAR/etc. | E2E | Done |
| 7 | Upload file | File uploaded | E2E, Integration | Done |
| 8 | Submit for review | Status -> PENDING | E2E, Integration | Done |
| 9 | View deadline tracker | Upcoming deadlines shown | E2E | Done |
| 10 | Compliance score updates | Score reflects submissions | Integration | Done |

### 5.9 Impact Stories - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to Impact | Impact page loads | E2E | Done |
| 2 | View existing stories | Stories listed | E2E | Done |
| 3 | Click "New Story" | Story form opens | E2E | Done |
| 4 | Enter title | Title validated | E2E, Unit | Done |
| 5 | Enter content | Rich text editor works | E2E | Done |
| 6 | Select category | Category selected | E2E | Done |
| 7 | Select SDG alignment | SDGs selected | E2E | Done |
| 8 | Upload media | Images/videos uploaded | E2E, Integration | Done |
| 9 | Set featured image | Image marked featured | E2E | Done |
| 10 | Save as draft | Story saved with DRAFT status | E2E, Integration | Done |
| 11 | Publish story | Status -> PUBLISHED | E2E, Integration | Done |
| 12 | Story appears on storefront | Public can view | Integration | Done |

### 5.10 Delivery Settings - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to Settings -> Delivery | Delivery section loads | E2E | Done |
| 2 | Enable vendor delivery | Toggle on | E2E | Done |
| 3 | Set delivery estimate | Text saved | E2E | Done |
| 4 | Set delivery fee | Fee validated | E2E, Unit | Done |
| 5 | Enable pickup | Toggle on | E2E | Done |
| 6 | Set pickup address | Address saved | E2E | Done |
| 7 | Set pickup instructions | Instructions saved | E2E | Done |
| 8 | Enable meetup | Toggle on | E2E | Done |
| 9 | Set meetup instructions | Instructions saved | E2E | Done |
| 10 | Save settings | StorefrontSettings updated | E2E, Integration | Done |
| 11 | Options appear at checkout | Customer sees options | Integration | Done |

---

## Section 6: CSEA Agency Admin Journeys

### 6.1 Admin Dashboard - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Login as admin | Redirect to `/agency` | E2E | Done |
| 2 | View stats cards | Summary metrics shown | E2E | Done |
| 3 | View compliance overview | Compliance distribution | E2E | Done |
| 4 | View pending items | Action items listed | E2E | Done |
| 5 | View recent activity | Activity feed | E2E | Done |
| 6 | View regional overview | Geographic breakdown | E2E | Done |
| 7 | See all organizations | Not scoped to single tenant | Security | Done |

### 6.2 Registration Oversight - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to Registration | Registration page loads | E2E | Done |
| 2 | View applications inbox | Pending applications listed | E2E | Done |
| 3 | Filter by status | Filtering works | E2E, Unit | Done |
| 4 | Click application | Review panel opens | E2E | Done |
| 5 | Verify documents | Document checklist | E2E | Done |
| 6 | Approve application | Status -> Approved | E2E, Integration | Done |
| 7 | Issue certificate | Certificate generated | E2E, Integration | Pending |
| 8 | Reject application | Status -> Rejected, reason | E2E, Integration | Done |
| 9 | View amendments | Amendment requests listed | E2E | Done |
| 10 | Process amendments | Changes applied | E2E, Integration | Done |

### 6.3 Formation Tracking - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to Formation | Formation page loads | E2E | Done |
| 2 | View name reservations | Reservations listed | E2E | Done |
| 3 | Review reservation | Details shown | E2E | Done |
| 4 | Approve/reject reservation | Status updated | E2E, Integration | Done |
| 5 | View PRS schedule | Training schedule | E2E | Done |
| 6 | Enroll participants | Enrollment processed | E2E, Integration | Done |
| 7 | View economic surveys | Surveys listed | E2E | Done |
| 8 | Review survey | Survey details | E2E | Done |
| 9 | Provide feedback | Feedback saved | E2E, Integration | Done |

### 6.4 Auditing & Compliance - Partial

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to Auditing | Auditing page loads | E2E | Done |
| 2 | View submissions inbox | Submissions listed | E2E | Done |
| 3 | Filter by type/priority | Filtering works | E2E, Unit | Done |
| 4 | Review submission | Document viewer opens | E2E | Done |
| 5 | Approve submission | Status -> Approved | E2E, Integration | Partial |
| 6 | Reject/return submission | Status updated, notes | E2E, Integration | Partial |
| 7 | Record audit finding | Finding recorded | E2E, Integration | Partial |
| 8 | Issue COC | Certificate issued | E2E, Integration | Pending |
| 9 | Schedule field inspection | Inspection scheduled | E2E, Integration | Partial |
| 10 | View performance metrics | STEPS/PESOS displayed | E2E | Done |

### 6.5 Monitoring & Analytics - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to Monitoring | Monitoring page loads | E2E | Done |
| 2 | View analytics dashboard | Charts and metrics | E2E | Done |
| 3 | Filter by date range | Data refreshes | E2E | Done |
| 4 | View sectoral reports | Sector breakdown | E2E | Done |
| 5 | View impact assessment | Impact metrics | E2E | Done |
| 6 | Generate report | Report PDF generated | E2E, Integration | Partial |
| 7 | Export data | Data exported | E2E, Integration | Partial |

### 6.6 Manager Applications (Admin View) - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to Manager Applications | Applications listed | E2E | Done |
| 2 | Filter by status | Filtering works | E2E, Unit | Done |
| 3 | View application details | Full details shown | E2E | Done |
| 4 | Verify documents | Document verification | E2E | Done |
| 5 | Request more information | Status -> INFO_REQUESTED | E2E, Integration | Done |
| 6 | Approve application | User upgraded to tenant | E2E, Integration | Done |
| 7 | Reject application | Rejection reason recorded | E2E, Integration | Done |

### 6.7 Cooperatives/SE Registry Management - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to Cooperatives | Cooperatives table loads | E2E | Done |
| 2 | Filter by status/type/location | Filtering works | E2E, Unit | Done |
| 3 | View cooperative details | Detail panel opens | E2E | Done |
| 4 | Edit cooperative info | Changes saved | E2E, Integration | Done |
| 5 | Update compliance status | Status updated | E2E, Integration | Done |
| 6 | Archive cooperative | Archived, hidden from public | E2E, Integration | Done |
| 7 | Navigate to Social Enterprises | SE table loads | E2E | Done |
| 8 | Same filtering/editing | Works for SEs | E2E | Done |

### 6.8 SE-Specific Admin Functions - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | View SE accreditation applications | Applications listed | E2E | Done |
| 2 | Review impact statement | Statement displayed | E2E | Done |
| 3 | Assess IMPACT score | Score calculated | E2E, Unit | Done |
| 4 | Review self-certification | Certification shown | E2E | Done |
| 5 | Track SDG contributions | SDG metrics shown | E2E | Done |
| 6 | Review impact assessment | Assessment displayed | E2E | Done |
| 7 | Approve accreditation renewal | Status updated | E2E, Integration | Done |

---

## Section 7: Cooperative Registration Flow

### 7.1 Multi-Step Cooperative Registration - Done

| Step | Page | Actions | Test Type | Status |
|------|------|---------|-----------|--------|
| 1 | `/coop/register` | Start registration, enter basic info | E2E | Done |
| 2 | `/coop/register/cooperators` | Add minimum 15 cooperators | E2E, Unit | Done |
| 3 | `/coop/register/purposes` | Define cooperative purposes | E2E | Done |
| 4 | `/coop/register/articles` | Review articles of cooperation | E2E | Done |
| 5 | `/coop/register/bylaws` | Review by-laws | E2E | Done |
| 6 | `/coop/register/committees` | Set up committees | E2E | Done |
| 7 | `/coop/register/capitalization` | Enter capital structure | E2E | Done |
| 8 | `/coop/register/economic-survey` | Complete economic survey | E2E | Done |
| 9 | `/coop/register/staff` | Add staff information | E2E | Done |
| 10 | `/coop/register/manager` | Designate manager | E2E | Done |
| 11 | `/coop/register/documents` | Upload required documents | E2E, Integration | Done |
| 12 | `/coop/register/review` | Review and submit | E2E, Integration | Done |

### 7.2 Social Enterprise Registration Flow - Done

| Step | Page | Actions | Test Type | Status |
|------|------|---------|-----------|--------|
| 1 | `/se/register` | Start registration, enter basic info | E2E | Done |
| 2 | `/se/register/impact` | Define impact areas, SDGs | E2E | Done |
| 3 | `/se/register/manager` | Designate manager | E2E | Done |
| 4 | `/se/register/documents` | Upload required documents | E2E, Integration | Done |
| 5 | `/se/register/review` | Review and submit | E2E, Integration | Done |

---

## Section 8: Payment & Transaction Flows

### 8.1 Order Payment Processing - Partial

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Select payment method | Options: COD, GCash, PayMongo | E2E | Partial |
| 2 | COD selected | Order placed, status unpaid | E2E, Integration | Done |
| 3 | E-wallet selected | Redirect to payment gateway | E2E, Integration | Partial |
| 4 | Payment completed | Webhook updates order | Integration | Partial |
| 5 | Payment failed | Error shown, order pending | E2E, Integration | Partial |
| 6 | Retry payment | New transaction created | E2E, Integration | Pending |
| 7 | View transaction history | Transactions listed | E2E | Pending |

### 8.2 Platform Fees & Commission - Pending

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Order completed | Platform fee calculated | Integration | Pending |
| 2 | Net amount calculated | Fee deducted from total | Integration | Pending |
| 3 | View in order details | Fee breakdown shown | E2E | Pending |
| 4 | Admin reports | Commission tracked | Integration | Pending |

---

## Section 9: Custom Domain Journeys

### 9.1 Storefront Custom Domain - Done

| Step | Action | Expected Result | Test Type | Status |
|------|--------|-----------------|-----------|--------|
| 1 | Navigate to Settings -> Domains | Domain settings load | E2E | Done |
| 2 | Add custom domain | Domain entered | E2E | Done |
| 3 | View DNS instructions | CNAME target shown | E2E | Done |
| 4 | View verification token | TXT record shown | E2E | Done |
| 5 | Request verification | DNS lookup performed | Integration | Done |
| 6 | Verification succeeds | Status -> verified | Integration | Done |
| 7 | SSL provisioning | Certificate requested | Integration | Done |
| 8 | Domain active | Storefront accessible via domain | Integration | Done |
| 9 | Set as primary | Primary flag updated | E2E, Integration | Done |

---

## Section 10: Cross-Cutting Concerns

### 10.1 Authentication & Authorization - Done

| Test Case | Description | Test Type | Status |
|-----------|-------------|-----------|--------|
| JWT Token Validation | Valid tokens grant access | Unit, Integration | Done |
| Token Expiration | Expired tokens rejected | Unit, Integration | Done |
| Role-Based Access | Wrong role = 403 | Integration, Security | Done |
| Tenant Isolation | Tenant A can't access Tenant B data | Integration, Security | Done |
| Multi-Role Support | User with multiple roles can switch context | Integration | Done |
| Session Invalidation | Logout invalidates token | Integration | Done |

### 10.2 Data Isolation (Multi-Tenant) - Done

| Test Case | Description | Test Type | Status |
|-----------|-------------|-----------|--------|
| Product Isolation | Tenant only sees own products | Integration, Security | Done |
| Order Isolation | Tenant only sees own orders | Integration, Security | Done |
| Member Isolation | Tenant only sees own members | Integration, Security | Done |
| Document Isolation | Tenant only sees own documents | Integration, Security | Done |
| Analytics Isolation | Dashboard shows only own metrics | Integration, Security | Done |
| API Scoping | All API endpoints filter by tenant | Integration, Security | Done |

### 10.3 File Upload Security - Done

| Test Case | Description | Test Type | Status |
|-----------|-------------|-----------|--------|
| File Type Validation | Only allowed MIME types | Unit, Integration | Done |
| File Size Limits | Reject oversized files | Unit, Integration | Done |
| Malware Scanning | Files scanned before storage | Integration | Partial |
| Secure Storage | Files stored in tenant-isolated paths | Integration, Security | Done |
| Signed URLs | Temporary access URLs generated | Integration | Done |

### 10.4 Input Validation - Done

| Test Case | Description | Test Type | Status |
|-----------|-------------|-----------|--------|
| Email Format | Valid email required | Unit | Done |
| Phone Format | Valid PH phone format | Unit | Done |
| Price Validation | Positive numbers only | Unit | Done |
| SKU Uniqueness | Unique within tenant | Unit, Integration | Done |
| XSS Prevention | HTML stripped/escaped | Unit, Security | Done |
| SQL Injection | Parameterized queries | Security | Done |

### 10.5 Error Handling - Done

| Test Case | Description | Test Type | Status |
|-----------|-------------|-----------|--------|
| 404 Pages | Custom not found pages | E2E | Done |
| 500 Errors | Graceful error handling | E2E, Integration | Done |
| Form Errors | Inline validation messages | E2E | Done |
| Network Errors | Retry mechanisms, offline handling | E2E | Done |
| Payment Errors | Clear error messages | E2E | Partial |

---

## Section 11: Test Priority Matrix

### P0 (Critical) - Must Pass for Release

| Category | Tests | Status |
|----------|-------|--------|
| Authentication | Login, logout, session management | Done |
| Order Flow | Cart -> checkout -> order creation | Done |
| Payment Processing | All payment methods functional | Partial |
| Data Isolation | Tenant cannot access other tenant data | Done |
| Product Management | CRUD operations work correctly | Done |
| Registration | Coop/SE registration completes | Done |

### P1 (High) - Important Functionality

| Category | Tests | Status |
|----------|-------|--------|
| Manager Application | Application -> approval -> tenant upgrade | Done |
| Compliance Submission | Upload and submission workflow | Done |
| Storefront Customization | Theme and settings save correctly | Done |
| Order Status Updates | Status transitions work | Partial |
| Admin Review Workflows | Approval/rejection workflows | Partial |

### P2 (Medium) - Enhanced Features

| Category | Tests | Status |
|----------|-------|--------|
| Product Variants | Variant matrix generation | Partial |
| Impact Stories | Publishing workflow | Done |
| Custom Domains | DNS verification | Done |
| Analytics | Dashboard metrics accuracy | Done |
| Member Management | CRUD operations | Done |

### P3 (Low) - Nice to Have

| Category | Tests | Status |
|----------|-------|--------|
| Loyalty Points | Points calculation | Pending |
| Wishlist | Add/remove functionality | Pending |
| Report Export | PDF/Excel generation | Partial |
| UI Polish | Animations, transitions | Done |
| Notifications | Email delivery | Partial |

---

## Section 12: Manual Testing Checklist

### Pre-Release Checklist

**Public Portal:** Done
- [x] Homepage loads with all sections
- [x] Product search works
- [x] Category filtering works
- [x] Product detail pages display correctly
- [x] Add to cart works
- [x] Guest checkout completes
- [x] Mobile responsive layout

**Storefronts:** Done
- [x] Coop storefront accessible via `/coop/[slug]`
- [x] SE storefront accessible via `/se/[slug]`
- [x] Custom theme colors applied
- [x] Hero banner displays
- [x] Products load correctly
- [x] Cart and checkout work

**Tenant Portal:** Partial
- [x] Dashboard loads for tenant
- [x] Only own organization data shown
- [x] Product CRUD works
- [ ] Order management works (partial - status updates incomplete)
- [x] Storefront customization works
- [x] Document upload works

**Agency Admin:** Partial
- [x] Dashboard shows aggregate data
- [x] Registration review works
- [ ] Compliance submission review works (partial - workflow incomplete)
- [x] Manager application approval works
- [x] All tenants visible (not isolated)

**Cross-Browser:**
- [x] Chrome (latest)
- [x] Firefox (latest)
- [x] Safari (latest)
- [x] Edge (latest)
- [x] Mobile Safari (iOS)
- [x] Mobile Chrome (Android)

---

## Section 13: API Endpoint Testing

### Public API Endpoints - Done

| Endpoint | Method | Test Cases | Status |
|----------|--------|------------|--------|
| `/api/public/products` | GET | Pagination, filtering, search | Done |
| `/api/public/products/{id}` | GET | Valid ID, invalid ID, inactive product | Done |
| `/api/public/cooperatives` | GET | Pagination, filtering by type/location | Done |
| `/api/public/cooperatives/{slug}` | GET | Valid slug, invalid slug | Done |
| `/api/public/social-enterprises` | GET | Pagination, filtering by sector | Done |
| `/api/public/orders` | POST | Valid order, validation errors | Done |
| `/api/public/reviews` | POST | Valid review, duplicate prevention | Partial |

### Tenant API Endpoints - Done

| Endpoint | Method | Test Cases | Status |
|----------|--------|------------|--------|
| `/api/tenant/products` | GET, POST | CRUD, tenant isolation | Done |
| `/api/tenant/products/{id}` | GET, PUT, DELETE | CRUD, tenant isolation | Done |
| `/api/tenant/orders` | GET | List, filter, tenant isolation | Done |
| `/api/tenant/orders/{id}` | GET, PUT | Detail, status update | Partial |
| `/api/tenant/storefront` | GET, PUT | Settings CRUD | Done |
| `/api/tenant/documents` | GET, POST | Upload, list | Done |
| `/api/tenant/members` | GET, POST | CRUD | Done |

### Admin API Endpoints - Done

| Endpoint | Method | Test Cases | Status |
|----------|--------|------------|--------|
| `/api/agency/cooperatives` | GET | List all (not scoped) | Done |
| `/api/agency/applications` | GET | Manager applications list | Done |
| `/api/agency/applications/{id}` | PUT | Approve/reject | Done |
| `/api/agency/submissions` | GET | Compliance submissions | Done |
| `/api/agency/submissions/{id}` | PUT | Review actions | Partial |

---

## Section 14: Performance Testing

### Page Load Targets - Done

| Page | Target (LCP) | Test Method | Status |
|------|--------------|-------------|--------|
| Homepage | < 2.5s | Lighthouse | Done |
| Product Listing | < 2.5s | Lighthouse | Done |
| Product Detail | < 2.0s | Lighthouse | Done |
| Tenant Dashboard | < 3.0s | Lighthouse | Done |
| Admin Dashboard | < 3.0s | Lighthouse | Done |

### API Response Targets - Done

| Endpoint Type | Target (p95) | Status |
|---------------|--------------|--------|
| List (paginated) | < 500ms | Done |
| Detail | < 200ms | Done |
| Create/Update | < 1000ms | Done |
| File Upload | < 5000ms | Done |

### Load Testing Scenarios - Partial

| Scenario | Concurrent Users | Duration | Status |
|----------|------------------|----------|--------|
| Normal Load | 100 | 10 min | Partial |
| Peak Load | 500 | 5 min | Pending |
| Stress Test | 1000 | 2 min | Pending |

---

## Appendix: Entity Relationship Summary

```text
User ──────────────────────────────────────────────────────────────┐
 │                                                                  │
 ├── CustomerProfile (1:1)                                         │
 │    ├── shipping_addresses[]                                     │
 │    ├── wishlist[]                                               │
 │    └── loyalty_points                                           │
 │                                                                  │
 ├── ManagerApplication (1:N)                                      │
 │    ├── documents[]                                              │
 │    └── → OrganizationManager (upon approval)                    │
 │                                                                  │
 └── OrganizationManager (1:N)                                     │
      └── Cooperative | SocialEnterprise                           │
                                                                    │
Cooperative ────────────────────────────────────────────────────────┤
 ├── CooperativeProduct (1:N)                                      │
 │    ├── ProductVariant (1:N)                                     │
 │    └── ProductReview (1:N)                                      │
 │                                                                  │
 ├── CooperativeOrder (1:N)                                        │
 │    └── PaymentTransaction (1:N)                                 │
 │                                                                  │
 ├── CooperativeMember (1:N)                                       │
 ├── CooperativeOfficer (1:N)                                      │
 ├── ComplianceSubmission (1:N)                                    │
 ├── STEPSData (1:N per fiscal year)                               │
 ├── PESOSData (1:N per fiscal year)                               │
 └── CustomDomain (1:N)                                            │
                                                                    │
SocialEnterprise ───────────────────────────────────────────────────┤
 ├── SocialEnterpriseProduct (1:N)                                 │
 │    ├── ProductVariant (1:N)                                     │
 │    └── ProductReview (1:N)                                      │
 │                                                                  │
 ├── SocialEnterpriseOrder (1:N)                                   │
 │    └── PaymentTransaction (1:N)                                 │
 │                                                                  │
 ├── SEBoardMember (1:N)                                           │
 ├── SEComplianceSubmission (1:N)                                  │
 ├── SEImpactAssessment (1:N per fiscal year)                      │
 └── CustomDomain (1:N)                                            │
                                                                    │
Tenant-Scoped Models ───────────────────────────────────────────────┤
 ├── TenantDraftState (1:1 per entity)                             │
 ├── TenantDocument (1:N)                                          │
 ├── StorefrontSettings (1:1 per entity)                           │
 └── ImpactStory (1:N)                                             │
      └── ImpactStoryMedia (1:N)                                   │
                                                                    │
Reference Models ───────────────────────────────────────────────────┘
 ├── Region → Province → Municipality
 ├── CooperativeType
 ├── SESector
 ├── ProductCategory
 ├── DocumentType
 ├── ImpactArea
 └── SDGGoal
```
