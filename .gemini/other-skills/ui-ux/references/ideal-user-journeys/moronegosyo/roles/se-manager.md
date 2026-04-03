# Social Enterprise Manager - MoroNegosyo

## Overview
Social Enterprise (SE) Managers are authenticated users who manage a registered social enterprise's presence on MoroNegosyo. They access the Tenant Portal to manage their shop, products, orders, and impact reporting while ensuring compliance with CSEA regulations. SE Managers focus on demonstrating social impact alongside commercial success, with specific emphasis on SDG alignment and triple-bottom-line reporting.

## Role Definition
**Type**: Authenticated Tenant User
**Portal Access**: Tenant Portal (`/portal`), Public Portal (`/`), Storefront (`/se/[slug]`)
**Authentication**: Email/Password with optional 2FA (recommended for financial access)

## Capabilities

### Core Capabilities
| Capability | Description | Priority |
|------------|-------------|----------|
| Shop Management | Configure and customize SE storefront | P0 |
| Product Management | Create, edit, archive products | P0 |
| Order Management | Process, fulfill, track orders | P0 |
| Impact Reporting | Track and report social impact metrics | P0 |
| Inventory Management | Track stock levels, alerts | P1 |
| Compliance Tracking | Monitor SE status, upload documents | P1 |
| Financial Dashboard | View sales, revenue, payouts | P1 |
| SDG Alignment | Map products/activities to SDGs | P1 |
| Storefront Customization | Brand, impact story, mission display | P1 |
| Promotion Management | Create discounts, sales, coupons | P2 |
| Analytics Dashboard | Sales, impact, customer insights | P2 |
| Training Access | Enroll in MoroAcademy courses | P2 |
| Beneficiary Management | Track impact beneficiaries | P2 |
| Support Requests | Contact CSEA, resolve issues | P2 |
| Team Management | Add staff with role-based access | P3 |

### Feature Access Matrix
| Feature | Access Level | Notes |
|---------|--------------|-------|
| Tenant Dashboard | Full | SE-specific widgets |
| Shop Settings | Full | All configuration options |
| Product Catalog | Full | CRUD with impact tags |
| Order Processing | Full | All order actions |
| Inventory | Full | Stock management |
| Impact Dashboard | Full | SE-exclusive feature |
| Beneficiary Tracking | Full | SE-exclusive feature |
| SDG Mapping | Full | SE-exclusive feature |
| Compliance | Full | SE-specific requirements |
| Financial Reports | Full | All reports, export capability |
| Analytics | Full | All metrics, date ranges |
| Storefront Editor | Full | Impact-focused templates |
| Promotions | Full | Create, edit, deactivate |
| MoroAcademy | Full | SE-focused courses available |
| Public Portal | Full | Consumer capabilities retained |
| Admin Portal | None | CSEA staff only |

## User Journey Entry Points

1. **Daily Operations Login**
   - Manager logs in to check new orders
   - Lands on Tenant Dashboard with impact summary
   - Path: Login > Dashboard > Orders > Process

2. **Impact Reporting Cycle**
   - Quarterly impact report due notification
   - Manager compiles and submits impact data
   - Path: Email > Impact Dashboard > Compile > Submit

3. **SDG Campaign**
   - Manager wants to highlight SDG alignment
   - Updates products with SDG tags
   - Path: Dashboard > Products > Edit > Add SDG tags

4. **Order Notification**
   - New order notification received
   - Clicks through to order detail
   - Path: Email/SMS > Order Detail > Process > Ship

5. **Compliance Deadline**
   - CSEA sends compliance reminder
   - Manager uploads required SE documents
   - Path: Email > Compliance > Upload > Submit

6. **Investor/Partner Inquiry**
   - Potential partner requests impact data
   - Manager exports impact report
   - Path: Dashboard > Impact > Export Report > Share

## Key Pages

### Tenant Portal Pages
| Page | Purpose | Route | Implementation |
|------|---------|-------|----------------|
| Dashboard | Overview, impact metrics, alerts | `/portal` | Active |
| Shop Settings | Basic shop configuration | `/portal/settings` | Active |
| Products List | All products management | `/portal/products` | Active |
| Product Create | Add new product with impact tags | `/portal/products/new` | Active |
| Product Edit | Modify product | `/portal/products/[id]` | Active |
| Orders List | All orders | `/portal/orders` | Active |
| Order Detail | Single order management | `/portal/orders/[id]` | Active |
| Inventory | Stock management | `/portal/inventory` | Planned |
| Impact Dashboard | Social impact tracking | `/portal/impact` | Planned |
| SDG Alignment | SDG mapping and progress | `/portal/impact/sdg` | Planned |
| Beneficiaries | Beneficiary management | `/portal/impact/beneficiaries` | Planned |
| Compliance | SE status, documents | `/portal/compliance` | Active |
| Analytics | Sales, impact reports | `/portal/analytics` | Planned |
| Storefront Editor | Customize storefront | `/portal/storefront` | Planned |
| Promotions | Discounts, coupons | `/portal/promotions` | Planned |
| Financial | Sales, payouts, reports | `/portal/financials` | Planned |
| Team | Staff management | `/portal/team` | Planned |
| Training | MoroAcademy access | `/portal/training` | Planned |
| Support | Help, contact CSEA | `/portal/support` | Planned |

## Shop Management

### Shop Profile (SE-Specific)
- Social Enterprise name (from SEC/DTI registration)
- Mission statement (required, prominent display)
- Vision statement (recommended)
- Business description (rich text with impact focus)
- Logo (recommended 500x500px)
- Banner image with impact imagery (recommended 1200x400px)
- Founder/leadership story
- Contact information
- Business hours
- Physical address
- Social media links

### Storefront Customization (SE-Focused)
- Primary brand color
- Secondary accent color
- Custom URL slug (`/se/[your-slug]`)
- Custom domain support
- Featured products section
- **Impact story section** (SE-exclusive)
- **Beneficiary testimonials** (SE-exclusive)
- **SDG badges display** (SE-exclusive)
- Team showcase
- Partner logos
- Awards and recognitions

### Business Settings
- Shipping zones and rates
- Payment methods accepted
- Order processing SLA
- Return/refund policy
- Minimum order amount
- Impact contribution display per product
- Cause-linked promotions

## Product Management (SE-Specific Extensions)

### Product Information
| Field | Required | Description |
|-------|----------|-------------|
| Product Name | Yes | Up to 200 characters |
| Description | Yes | Rich text with impact story |
| SKU | Yes | Unique identifier |
| Category | Yes | From predefined categories |
| Price | Yes | Regular price in PHP |
| Compare-at Price | No | Original price for discounts |
| Cost | No | For profit calculation |
| **Impact Contribution** | No | Amount/% going to cause |
| Images | Yes | Min 1, show impact context |
| Weight | Conditional | Required if shipping by weight |
| Stock Quantity | Yes | Current available stock |
| **SDG Tags** | Recommended | Linked SDGs for this product |
| **Beneficiary Group** | No | Who benefits from purchase |
| Tags | No | For search optimization |

### Impact Product Tags
| Tag | SDG Link | Description |
|-----|----------|-------------|
| Livelihood Support | SDG 8 | Supports artisan livelihoods |
| Women Empowerment | SDG 5 | Made by women-led groups |
| Environmental | SDG 12, 13 | Eco-friendly, sustainable |
| Education Fund | SDG 4 | Proceeds support education |
| Health Support | SDG 3 | Proceeds support health initiatives |
| Indigenous Craft | SDG 10 | Preserves indigenous traditions |
| Zero Waste | SDG 12 | Zero-waste production/packaging |

## Impact Dashboard (SE-Exclusive)

### Impact Metrics
| Metric | Description | Frequency |
|--------|-------------|-----------|
| Beneficiaries Reached | Number of individuals impacted | Monthly |
| Jobs Created | Employment generated | Quarterly |
| Artisans Supported | Craftspeople earning income | Monthly |
| Women Employed | Female employment | Monthly |
| Environmental Impact | CO2 saved, plastic reduced, etc. | Quarterly |
| Community Investment | PHP invested in community | Quarterly |
| Training Hours | Skills training provided | Quarterly |
| Lives Improved | Aggregate impact stories | Ongoing |

### SDG Progress Tracking
- SDG goal selection (primary and secondary)
- Indicator mapping per SDG
- Progress visualization
- Year-over-year comparison
- SDG badge requirements
- Impact verification status

### Impact Reporting
| Report Type | Frequency | Purpose |
|-------------|-----------|---------|
| Monthly Summary | Monthly | Quick metrics snapshot |
| Quarterly Report | Quarterly | Detailed impact analysis |
| Annual Impact Report | Yearly | Comprehensive review |
| Custom Report | On-demand | For partners/investors |

## Beneficiary Management (SE-Exclusive)

### Beneficiary Tracking
- Beneficiary registration
- Category assignment (artisan, farmer, community, etc.)
- Demographics tracking
- Income impact tracking
- Story collection
- Photo consent management
- Testimonial gathering

### Beneficiary Categories
| Category | Description | Key Metrics |
|----------|-------------|-------------|
| Artisans | Crafts producers | Income, orders, skills |
| Farmers | Agricultural producers | Income, yield, practices |
| Women | Women beneficiaries | Employment, income, empowerment |
| Youth | Young people supported | Education, employment, training |
| Community | General community | Projects, investments, reach |
| Environment | Environmental beneficiaries | Trees, CO2, waste reduced |

## SE Compliance Requirements

### SE-Specific Documents
| Document | Description | Frequency |
|----------|-------------|-----------|
| SEC/DTI Registration | Legal registration | Annual renewal |
| Impact Report | Social impact documentation | Quarterly |
| Financial Statements | Audited financials | Annual |
| Social Mission Statement | Documented mission | Initial + changes |
| Beneficiary List | Active beneficiaries | Quarterly |
| Partner Agreements | Third-party partnerships | As needed |
| Environmental Certifications | If applicable | Per certification |

### SE Validation Criteria
| Criterion | Description | Evidence Required |
|-----------|-------------|-------------------|
| Social Mission | Clear social/environmental purpose | Mission statement, activities |
| Impact Measurement | Tracks and reports impact | Impact reports, metrics |
| Profit Reinvestment | Majority reinvested in mission | Financial statements |
| Stakeholder Engagement | Beneficiary involvement | Testimonials, participation |
| Transparency | Open about operations | Reports, disclosures |

### Compliance Status
| Status | Description | Action |
|--------|-------------|--------|
| Verified SE | Full compliance, impact verified | Maintain |
| Pending Verification | Documents under review | Wait for CSEA |
| Conditional | Minor issues to address | Resolve within 30 days |
| Non-Compliant | Significant issues | Immediate action required |

## Training Access (MoroAcademy) - SE Focus

### SE-Specific Training
- Social entrepreneurship fundamentals
- Impact measurement and management
- SDG integration in business
- Beneficiary-centered design
- Sustainable business models
- Impact storytelling
- Social enterprise financing
- Theory of Change development

### General Training
- E-commerce best practices
- Product photography
- Customer service excellence
- Financial literacy
- Digital marketing

## Role Progression

**From**: Consumer (after SE registration approval)
**To**:
- Multi-SE Manager (managing multiple SEs)
- SE Network Manager (future, for SE networks)

**Requirements to Become SE Manager**:
- Valid SEC/DTI registration
- Documented social mission
- Initial impact evidence
- CSEA application submission
- Document verification
- CSEA approval
- Account activation

## Differences from Coop Manager

| Aspect | Coop Manager | SE Manager |
|--------|--------------|------------|
| Entity Type | Cooperative (CDA registered) | Social Enterprise (SEC/DTI) |
| Compliance | FRAMES framework | SE verification criteria |
| Member Management | Coop member features | Not applicable |
| Impact Focus | Community through patronage | Explicit impact tracking |
| SDG Alignment | Optional | Required |
| Beneficiary Tracking | Not explicit | Core feature |
| Profit Distribution | Patronage refund | Mission reinvestment |
| Governance | Member voting | Varies by structure |

## Pain Points

1. **Impact Measurement Complexity**
   - Defining right metrics is hard
   - Data collection burden
   - Impact: Incomplete reporting, undervalued impact

2. **SDG Alignment Confusion**
   - Too many goals to choose from
   - Unclear indicator requirements
   - Impact: Poor SDG representation

3. **Beneficiary Data Management**
   - Manual tracking processes
   - Privacy/consent concerns
   - Impact: Incomplete beneficiary records

4. **Storytelling for Impact**
   - Difficulty conveying impact compellingly
   - No templates or guidance
   - Impact: Missed connection with consumers

5. **Verification Process**
   - Lengthy verification timeline
   - Unclear requirements
   - Impact: Delayed marketplace access

6. **Balancing Commerce and Impact**
   - Pressure to prioritize sales
   - Impact work seen as overhead
   - Impact: Mission drift

## Improvement Opportunities

1. **Impact Measurement Framework**
   - Pre-built indicator library
   - SDG-linked templates
   - Automated calculation where possible
   - Benchmarking against peers

2. **SDG Wizard**
   - Guided SDG selection
   - Indicator suggestions per goal
   - Progress tracking templates
   - SDG badge auto-assignment

3. **Beneficiary Management System**
   - Mobile app for field data collection
   - Consent management
   - Story capture tools
   - Impact aggregation

4. **Impact Storytelling Tools**
   - Story templates
   - Impact visualization widgets
   - Testimonial collection workflow
   - Social media integration

5. **Streamlined Verification**
   - Clear checklist upfront
   - Document pre-validation
   - Progress tracker
   - Expedited review for renewals

6. **Impact-Commerce Integration**
   - "Impact per purchase" display
   - Cause-linked campaigns
   - Consumer impact dashboards
   - Impact NFTs/certificates (future)

## Success Metrics

### Business Metrics
- **Monthly Gross Sales**: Total sales per month (target: growing MoM)
- **Order Count**: Total orders processed (target: 30+ monthly)
- **Average Order Value**: Mean order value (target: PHP 600+)
- **Order Fulfillment Time**: Hours from order to ship (target: < 48 hours)

### Impact Metrics (SE-Specific)
- **Beneficiaries Reached**: Monthly unique beneficiaries (target: growing)
- **Impact per Sale**: Average impact contribution per order
- **SDG Goals Tracked**: Number of SDGs with active metrics (target: 2-3)
- **Impact Report Completion**: % of required reports submitted (target: 100%)

### Operational Metrics
- **Inventory Accuracy**: Stock count accuracy (target: 98%+)
- **Order Acceptance Rate**: % orders accepted (target: 95%+)
- **Return Rate**: % orders returned (target: < 5%)
- **Customer Response Time**: Hours to respond (target: < 24 hours)

### Compliance Metrics
- **Verification Status**: Active SE verification (target: Verified)
- **Document Currency**: % documents up to date (target: 100%)
- **On-Time Submission**: % reports submitted before deadline (target: 100%)
- **Impact Verification**: % of impact claims verified (target: 80%+)

### Growth Metrics
- **Product Catalog Growth**: New products per month (target: 5+)
- **Customer Acquisition**: New customers per month
- **Impact-Motivated Purchases**: % citing impact as reason (target: 40%+)
- **Storefront Traffic**: Monthly unique visitors

### Storytelling Metrics
- **Beneficiary Stories Published**: Stories per quarter (target: 3+)
- **Story Engagement**: Views, shares, reactions
- **Media Mentions**: External coverage of SE impact

---

## Implementation Plan

### Access Control
- **Authentication required**: All `/portal/*` routes require authenticated tenant user
- **Middleware**: `frontend/src/middleware.ts` - tenant auth guards for `(tenant)` route group
- **Tenant scoping**: All data operations scoped to user's assigned tenant (social enterprise)
- **Permission checks**: User must have `se_manager` or `se_admin` role on tenant
- **2FA recommended**: Prompt for 2FA setup on first login, required for financial access
- **Entity type check**: Tenant must be of type `social_enterprise` for SE-specific features

```typescript
// frontend/src/middleware.ts
const tenantRoutes = ['/portal'];
// Verify: authenticated + has tenant + role is se_manager/se_admin
// Verify tenant.entity_type === 'social_enterprise' for SE features
// Inject tenant context via X-Tenant-ID header
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
| Impact Dashboard | `/portal/impact` | `frontend/src/app/(tenant)/portal/impact/page.tsx` |

#### P1 - Impact & Compliance
| Page | Route | File Path |
|------|-------|-----------|
| SDG Alignment | `/portal/impact/sdg` | `frontend/src/app/(tenant)/portal/impact/sdg/page.tsx` |
| Beneficiaries | `/portal/impact/beneficiaries` | `frontend/src/app/(tenant)/portal/impact/beneficiaries/page.tsx` |
| Beneficiary Detail | `/portal/impact/beneficiaries/[id]` | `frontend/src/app/(tenant)/portal/impact/beneficiaries/[id]/page.tsx` |
| Impact Reports | `/portal/impact/reports` | `frontend/src/app/(tenant)/portal/impact/reports/page.tsx` |
| Compliance Dashboard | `/portal/compliance` | `frontend/src/app/(tenant)/portal/compliance/page.tsx` |
| Document Upload | `/portal/compliance/documents` | `frontend/src/app/(tenant)/portal/compliance/documents/page.tsx` |
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
| TenantSidebar | `frontend/src/components/portal/tenant-sidebar.tsx` | Portal navigation (shared) |
| DashboardStats | `frontend/src/components/portal/dashboard-stats.tsx` | Key metrics cards (shared) |
| ImpactSummaryCard | `frontend/src/components/portal/impact/impact-summary-card.tsx` | Impact overview |
| SDGSelector | `frontend/src/components/portal/impact/sdg-selector.tsx` | SDG goal picker |
| SDGProgressCard | `frontend/src/components/portal/impact/sdg-progress-card.tsx` | SDG goal progress |
| SDGBadge | `frontend/src/components/portal/impact/sdg-badge.tsx` | SDG badge display |
| ImpactMetricForm | `frontend/src/components/portal/impact/impact-metric-form.tsx` | Log impact data |
| ImpactChart | `frontend/src/components/portal/impact/impact-chart.tsx` | Impact visualization |
| BeneficiaryTable | `frontend/src/components/portal/impact/beneficiary-table.tsx` | Beneficiary list |
| BeneficiaryForm | `frontend/src/components/portal/impact/beneficiary-form.tsx` | Add/edit beneficiary |
| BeneficiaryStoryForm | `frontend/src/components/portal/impact/beneficiary-story-form.tsx` | Capture testimonial |
| ImpactReportGenerator | `frontend/src/components/portal/impact/impact-report-generator.tsx` | Generate reports |
| ProductForm | `frontend/src/components/portal/products/product-form.tsx` | Product form (extended) |
| ImpactTagSelector | `frontend/src/components/portal/products/impact-tag-selector.tsx` | Impact tags picker |
| ProductSDGMapping | `frontend/src/components/portal/products/product-sdg-mapping.tsx` | Link product to SDGs |
| ImpactContributionInput | `frontend/src/components/portal/products/impact-contribution-input.tsx` | Set impact amount |
| SEComplianceCard | `frontend/src/components/portal/compliance/se-compliance-card.tsx` | SE verification status |
| MissionStatementEditor | `frontend/src/components/portal/settings/mission-statement-editor.tsx` | Mission/vision edit |
| StorefrontImpactSection | `frontend/src/components/portal/storefront/storefront-impact-section.tsx` | Impact story section |
| TestimonialEditor | `frontend/src/components/portal/storefront/testimonial-editor.tsx` | Beneficiary quotes |

### API Endpoints Required

| Endpoint | Method | Location | Purpose |
|----------|--------|----------|---------|
| `/api/tenant/profile` | GET/PATCH | `backend/apps/tenant/api.py` | Tenant profile (shared) |
| `/api/tenant/settings` | GET/PATCH | `backend/apps/tenant/api.py` | Business settings (shared) |
| `/api/tenant/products` | GET/POST | `backend/apps/products/api.py` | Product management (shared) |
| `/api/tenant/products/{id}` | GET/PATCH/DELETE | `backend/apps/products/api.py` | Single product (shared) |
| `/api/tenant/products/{id}/impact` | GET/PATCH | `backend/apps/products/api.py` | Product impact data |
| `/api/tenant/products/{id}/sdg` | GET/PATCH | `backend/apps/products/api.py` | Product SDG mapping |
| `/api/tenant/orders` | GET | `backend/apps/orders/api.py` | Tenant orders (shared) |
| `/api/tenant/orders/{id}` | GET/PATCH | `backend/apps/orders/api.py` | Order detail (shared) |
| `/api/tenant/impact` | GET | `backend/apps/impact/api.py` | Impact summary |
| `/api/tenant/impact/metrics` | GET/POST | `backend/apps/impact/api.py` | Log impact metrics |
| `/api/tenant/impact/sdg` | GET/PATCH | `backend/apps/impact/api.py` | SDG alignment config |
| `/api/tenant/impact/sdg/{goal}` | GET/PATCH | `backend/apps/impact/api.py` | Single SDG progress |
| `/api/tenant/beneficiaries` | GET/POST | `backend/apps/impact/api.py` | Beneficiary management |
| `/api/tenant/beneficiaries/{id}` | GET/PATCH/DELETE | `backend/apps/impact/api.py` | Single beneficiary |
| `/api/tenant/beneficiaries/{id}/story` | GET/POST | `backend/apps/impact/api.py` | Beneficiary story |
| `/api/tenant/impact/reports` | GET/POST | `backend/apps/impact/api.py` | Impact reports |
| `/api/tenant/impact/reports/{id}` | GET | `backend/apps/impact/api.py` | Single report |
| `/api/tenant/impact/export` | GET | `backend/apps/impact/api.py` | Export impact data |
| `/api/tenant/compliance` | GET | `backend/apps/compliance/api.py` | SE verification status |
| `/api/tenant/compliance/documents` | GET/POST | `backend/apps/compliance/api.py` | Document management |
| `/api/tenant/analytics` | GET | `backend/apps/analytics/api.py` | Sales + impact analytics |
| `/api/tenant/storefront` | GET/PATCH | `backend/apps/tenant/api.py` | Storefront with impact |
| `/api/sdg/goals` | GET | `backend/apps/impact/api.py` | SDG reference data |
| `/api/sdg/indicators` | GET | `backend/apps/impact/api.py` | SDG indicators |
| `/api/impact-tags` | GET | `backend/apps/impact/api.py` | Available impact tags |

### Implementation Sequence

#### Phase 1: Core Operations (Week 1-3)
*Shared with Coop Manager - see coop-manager.md*
1. Tenant authentication with SE type detection
2. Dashboard with key metrics + impact summary widget
3. Product list/create/edit with impact fields (SDG tags, contribution)
4. Order management (confirm, ship, cancel)
5. Basic shop settings with mission statement

#### Phase 2: Impact Dashboard (Week 4-6)
1. Impact dashboard overview
2. Impact metric logging forms
3. Impact visualization charts
4. SDG goal selection wizard
5. SDG progress tracking per goal
6. SDG badge auto-assignment

#### Phase 3: Beneficiary Management (Week 7-8)
1. Beneficiary directory table
2. Beneficiary registration form
3. Beneficiary profile pages
4. Category assignment (artisan, farmer, women, etc.)
5. Story/testimonial capture
6. Photo consent management

#### Phase 4: Compliance & Verification (Week 9-10)
1. SE compliance dashboard
2. Verification criteria checklist
3. Document upload with SE-specific categories
4. Verification status tracking
5. Deadline and reminder system
6. CSEA feedback display

#### Phase 5: Reporting & Export (Week 11-12)
1. Monthly impact summary generator
2. Quarterly report builder
3. Annual report template
4. Custom report with date/metric selection
5. PDF/Excel export
6. Shareable impact report links

#### Phase 6: Storefront & Growth (Week 13-14)
1. Storefront editor with impact section
2. Beneficiary testimonial display
3. SDG badges on storefront
4. "Impact per purchase" display
5. Cause-linked promotions
6. Training/MoroAcademy integration

#### Phase 7: Advanced Features (Week 15-16)
1. Impact-commerce analytics
2. Impact-motivated purchase tracking
3. Beneficiary income tracking
4. Partner/investor report sharing
5. Team management
6. Integration with external impact platforms (planned)

---

## Implementation Status

*Audited: December 30, 2025*

### Key Pages Status

| Page | Status | Path | Notes |
|------|--------|------|-------|
| Dashboard | ✅ Implemented | `frontend/src/app/(tenant)/dashboard/page.tsx` | Shared with coop (entity type detection) |
| Login | ✅ Implemented | `frontend/src/app/(tenant)/login/page.tsx` | Tenant login |
| Register | ✅ Implemented | `frontend/src/app/(tenant)/register/page.tsx` | Tenant registration |
| Profile | ✅ Implemented | `frontend/src/app/(tenant)/profile/page.tsx` | Manager profile |
| Shop Overview | ✅ Implemented | `frontend/src/app/(tenant)/shop/page.tsx` | Shop management |
| Products List | ✅ Implemented | `frontend/src/app/(tenant)/shop/products/page.tsx` | Product catalog |
| Business Profile | ✅ Implemented | `frontend/src/app/(tenant)/business/page.tsx` | SE info + mission |
| Business Documents | ✅ Implemented | `frontend/src/app/(tenant)/business/documents/page.tsx` | SE documents |
| Compliance | ✅ Implemented | `frontend/src/app/(tenant)/compliance/page.tsx` | SE verification |
| Finances | ✅ Implemented | `frontend/src/app/(tenant)/finances/page.tsx` | Financial dashboard |
| Impact Dashboard | ✅ Implemented | `frontend/src/app/(tenant)/impact/page.tsx` | SE-focused impact |
| Impact Create | ✅ Implemented | `frontend/src/app/(tenant)/impact/new/page.tsx` | New impact story |
| Impact Detail | ✅ Implemented | `frontend/src/app/(tenant)/impact/[id]/page.tsx` | Single impact story |
| Training | ✅ Implemented | `frontend/src/app/(tenant)/training/page.tsx` | MoroAcademy access |
| Training Courses | ✅ Implemented | `frontend/src/app/(tenant)/training/courses/page.tsx` | SE-focused courses |
| Training Workshops | ✅ Implemented | `frontend/src/app/(tenant)/training/workshops/page.tsx` | Workshop catalog |
| Settings | ✅ Implemented | `frontend/src/app/(tenant)/settings/page.tsx` | General settings |
| Domain Settings | ✅ Implemented | `frontend/src/app/(tenant)/settings/domains/page.tsx` | Custom domains |
| SDG Alignment | ❌ Not Found | - | No `/impact/sdg` page |
| Beneficiaries | ❌ Not Found | - | No beneficiary management pages |
| Impact Reports | ❌ Not Found | - | No report generator page |
| Product Create | ❌ Not Found | - | No product create page |
| Product Edit | ❌ Not Found | - | No product edit page |
| Orders List | ❌ Not Found | - | No orders page |
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
| Tenant Profile | ✅ Implemented | `/tenant/profile` | SE profile |
| Tenant Products | ✅ Implemented | `/tenant/products` | Product CRUD |
| Tenant Orders | ✅ Implemented | `/tenant/orders` | Order management |
| Tenant Analytics | ✅ Implemented | `/tenant/analytics` | Sales + impact analytics |
| Tenant Reviews | ✅ Implemented | `/tenant/reviews` | Product reviews |
| Tenant Storefront | ✅ Implemented | `/tenant/storefront` | Storefront config |
| Tenant Impact | ✅ Implemented | `/tenant/impact` | Impact stories |
| Tenant Documents | ✅ Implemented | `/tenant/documents` | SE documents |
| Core Compliance | ✅ Implemented | `/core/compliance` | SE verification status |
| Core Dashboard Metrics | ✅ Implemented | `/core/dashboard/metrics` | Dashboard stats |
| Shop Products | ✅ Implemented | `/core/shop/products` | Shop products |
| Shop Orders | ✅ Implemented | `/core/shop/orders` | Shop orders |
| Impact Metrics | ❌ Not Found | - | No dedicated metrics logging API |
| SDG Alignment | ❌ Not Found | - | No SDG-specific API |
| Beneficiaries | ❌ Not Found | - | No beneficiary management API |
| Impact Reports Export | ❌ Not Found | - | No report export API |
| Promotions | ❌ Not Found | - | No promotions API |
| Team Management | ❌ Not Found | - | No team API |

### SE-Specific Features Status

| Feature | Status | Notes |
|---------|--------|-------|
| Mission Statement Display | 🚧 Partial | In business profile, needs prominence |
| SDG Badge Display | ❌ Not Found | No SDG integration |
| Beneficiary Tracking | ❌ Not Found | No beneficiary management |
| Impact Per Purchase | ❌ Not Found | No product-level impact |
| Beneficiary Testimonials | ❌ Not Found | No testimonial system |
| Impact Report Generator | ❌ Not Found | No automated reports |

### Overall Progress

- **Pages**: 18/31 implemented (58%)
- **APIs**: 12/18 implemented (67%)
- **SE-Specific Features**: 1/6 implemented (17%)

### Notes

1. **Shared Infrastructure**: SE manager uses same tenant portal as coop manager
2. **Entity Type Detection**: Differences should be handled via `tenant.entity_type === 'social_enterprise'`
3. **Impact Dashboard**: Basic impact tracking exists but lacks SE-specific depth
4. **Missing SDG Features**: No SDG alignment, tracking, or badge system
5. **No Beneficiary Management**: Core SE differentiator not yet implemented
6. **Impact Reporting**: Manual impact stories exist, no automated reporting
7. **Product Impact Tags**: No implementation for linking products to SDGs or impact
8. **Verification vs FRAMES**: Uses compliance page but needs SE-specific verification criteria
