# Tenant Product & Shop Journey - MoroNegosyo

## Overview

This journey maps the complete experience of a tenant manager setting up and managing their shop on MoroNegosyo, from creating their first product to customizing their storefront and managing ongoing inventory. The journey emphasizes progressive complexity, mobile-first management, and building a professional online presence.

## Persona

**Name**: Pedro Alonto
**Age**: 38
**Role**: Cooperative Manager
**Location**: Sultan Kudarat, Maguindanao
**Context**: Pedro manages a coffee cooperative with 120 farmer members. The cooperative has recently been approved on MoroNegosyo and needs to set up their online shop. Pedro is responsible for managing product listings, pricing, and storefront appearance. He often works from his phone while visiting member farms.

**Goals**:
- List all cooperative products with accurate information
- Set up competitive pricing including bulk/wholesale options
- Create an attractive storefront that tells their story
- Manage inventory efficiently across multiple products
- Keep product information current and accurate

**Tech Comfort**: Moderate - comfortable with basic apps, learns new tools
**Connectivity**: Variable - good in town, limited at farms
**Time Available**: Limited - manages shop between other responsibilities

---

## Journey Map

### Stage 1: Shop Profile Setup

**User Goal**: Create a compelling shop identity that builds trust

**Actions**:
1. Pedro navigates to Shop Settings
2. Uploads shop logo (cooperative logo)
3. Adds shop banner image
4. Writes shop description
5. Adds shop contact information
6. Sets operating hours
7. Previews public storefront

**Touchpoints**:
- Shop Settings page
- Image upload interfaces
- Rich text editor for description
- Contact form fields
- Operating hours selector
- Storefront preview

**Emotions**: Creative, building identity, proud of organization

**Pain Points**:
- Logo image requirements unclear
- Banner size/dimensions confusing
- Not sure what to write in description
- Preview doesn't match actual appearance

**Opportunities**:
- Clear image dimension guides
- Description templates and prompts
- Real-time preview updates
- Mobile-optimized image cropping

**Design Requirements**:
```
Shop Settings - Profile Tab:

[Shop Identity]
Logo*
- [Current logo or upload prompt]
- Recommended: 200x200px, PNG or JPG
- [Upload] [Remove]

Banner Image
- [Current banner or upload prompt]
- Recommended: 1200x300px
- [Upload] [Remove]

Shop Name: [Auto-filled from registration]
Tagline: [_______________________] (50 chars max)
"e.g., Fresh Arabica from Sultan Kudarat"

Description*
[Rich text editor]
- Placeholder: "Tell your story..."
- Character count: 0/1000
- Template suggestions dropdown

[Contact Information]
Email*: [___________]
Phone*: [___________]
WhatsApp: [___________]
Facebook: [___________]

[Operating Hours]
- Weekdays: [9:00 AM] to [5:00 PM]
- Saturday: [Closed / Custom]
- Sunday: [Closed / Custom]

[Preview Storefront] [Save Changes]
```

---

### Stage 2: First Product Creation

**User Goal**: List my first product correctly and completely

**Actions**:
1. Pedro clicks "Add Product" from dashboard
2. Enters product name and description
3. Selects appropriate category
4. Uploads product photos
5. Sets base price
6. Adds product variants (if applicable)
7. Sets inventory quantity
8. Publishes product

**Touchpoints**:
- Add Product button
- Product creation form (multi-step)
- Image upload gallery
- Category selector
- Price input
- Variant builder
- Inventory input
- Publish confirmation

**Emotions**: Careful, wanting to get it right, proud of products

**Pain Points**:
- Unsure which category fits best
- Photo upload is slow on mobile
- Variant setup is confusing
- Not sure what details matter

**Opportunities**:
- Category suggestion based on product name
- Compressed image upload for mobile
- Simplified variant interface
- Field importance indicators

**Design Requirements**:
```
Add Product - Step by Step:

Step 1: Basic Information
Product Name*: [_______________________]
"e.g., Premium Arabica Coffee Beans"

Category*: [Search or select from tree]
- Food & Beverages
  - Coffee & Tea
    - Coffee Beans ✓
  - ...

Short Description*: [___________________] (150 chars)
"Appears in product cards and search"

Full Description:
[Rich text editor]
- Features, ingredients, story

Step 2: Photos
[+ Add Photos] (drag to reorder)
- Photo 1: [thumbnail] (Main) [x]
- Photo 2: [thumbnail] [x]
- [+ Add More]

Tips:
- First photo is the main image
- Add 3-5 photos from different angles
- Include packaging if applicable
- Max 5MB per photo

Step 3: Pricing & Inventory
Base Price*: PHP [________]

Bulk Pricing (optional):
[ ] Enable bulk/wholesale pricing
  - 10+ units: PHP [____] per unit
  - 50+ units: PHP [____] per unit
  - 100+ units: PHP [____] per unit

Cost Price (internal): PHP [________]
"Used for profit calculation, not shown to customers"

Stock Quantity*: [____] units
[ ] Track inventory
[ ] Allow backorders

SKU (optional): [________]

Step 4: Variants (optional)
[ ] This product has variants (size, color, etc.)

If enabled:
Option Name: [Size ▼]
Values: [Small] [Medium] [Large] [+ Add]

Variant Price Adjustments:
- Small: Base price
- Medium: +PHP 50
- Large: +PHP 100

Step 5: Review & Publish
[Product Preview]
- All details shown as customer will see

[Save as Draft] [Publish Product]
```

---

### Stage 3: Product Variants Management

**User Goal**: Offer product variations without creating separate listings

**Actions**:
1. Pedro edits an existing product
2. Enables variants for the product
3. Defines variant options (e.g., size, grind type)
4. Sets prices per variant
5. Manages inventory per variant
6. Saves and previews

**Touchpoints**:
- Product edit page
- Variant toggle
- Option builder
- Variant matrix editor
- Per-variant inventory
- Save/preview controls

**Emotions**: Organized, systematic, sometimes frustrated with complexity

**Pain Points**:
- Variant combinations explode quickly
- Price management across variants is tedious
- Inventory tracking per variant is complex
- Changes don't apply to all variants easily

**Opportunities**:
- Smart variant combination generation
- Bulk price adjustment tools
- Inventory alerts per variant
- "Apply to all variants" actions

**Design Requirements**:
```
Variant Management Interface:

Product: Premium Arabica Coffee
[x] This product has variants

Options:
Option 1: [Grind Type ▼]
Values: [Whole Bean] [Coarse] [Medium] [Fine] [+ Add]

Option 2: [+ Add Option]
[Size ▼]
Values: [250g] [500g] [1kg] [+ Add]

Generated Variants: (6 combinations)
[Use table view] / [Use list view]

| Grind | Size | Price | Stock | SKU |
|-------|------|-------|-------|-----|
| Whole Bean | 250g | PHP 180 | 50 | WB-250 |
| Whole Bean | 500g | PHP 350 | 30 | WB-500 |
| Whole Bean | 1kg | PHP 680 | 20 | WB-1K |
| Coarse | 250g | PHP 200 | 45 | CRS-250 |
... (collapsible)

Bulk Actions:
[Adjust all prices by %]
[Set all stock to...]
[Generate SKUs]
```

---

### Stage 4: Product Photo Management

**User Goal**: Showcase products with high-quality images

**Actions**:
1. Pedro adds photos during product creation
2. Takes new photos from phone camera
3. Reorders photos (first = main image)
4. Replaces low-quality images
5. Adds alt text for accessibility
6. Views how photos appear on storefront

**Touchpoints**:
- Photo upload interface
- Camera capture option
- Photo reorder (drag and drop)
- Photo editor (crop, rotate)
- Alt text input
- Gallery preview

**Emotions**: Visual, wanting professional appearance, sometimes frustrated with quality

**Pain Points**:
- Photos taken indoors look dark
- Image files too large to upload
- Can't crop photos in the system
- Reordering is difficult on mobile

**Opportunities**:
- Photo tips and lighting guide
- Automatic image compression
- In-app crop and rotate tools
- Touch-friendly reordering

**Design Requirements**:
```
Product Photos Section:

[Camera icon] [Gallery icon] Add Photos

Current Photos: (3 of 10 max)
[Main] [2] [3] [+ Add]

Drag to reorder. First photo is main image.

[Photo Actions on tap]
- Set as main
- Edit (crop/rotate)
- Add alt text
- Delete

Photo Guidelines:
- Use natural lighting when possible
- Show product from multiple angles
- Include size reference (e.g., hand, cup)
- Keep background clean and simple

[View Sample Photos] - link to examples

Mobile Camera Tips:
- Tap to focus on product
- Clean lens before shooting
- Use landscape orientation for banners
```

---

### Stage 5: Inventory Management

**User Goal**: Keep stock levels accurate and avoid overselling

**Actions**:
1. Pedro views inventory dashboard
2. Sees low stock alerts
3. Updates stock quantities
4. Sets low stock threshold
5. Enables/disables products based on availability
6. Views inventory history

**Touchpoints**:
- Inventory dashboard
- Low stock alerts
- Inline stock editing
- Threshold settings
- Product status toggle
- Inventory log

**Emotions**: Managing, responsible, sometimes stressed about stockouts

**Pain Points**:
- Stock updates require opening each product
- No warning before stockout
- Can't update multiple products at once
- Inventory doesn't sync with actual stock

**Opportunities**:
- Quick inline stock editing
- Configurable low stock alerts
- Bulk inventory update tools
- Simple inventory import/export

**Design Requirements**:
```
Inventory Dashboard:

[Alerts Banner]
3 products low on stock! [View]

Quick Filters: [All] [Low Stock] [Out of Stock] [In Stock]

Product Inventory Table:
| Product | Variants | Stock | Threshold | Status |
|---------|----------|-------|-----------|--------|
| Arabica Coffee | 6 | 195 | 20 | In Stock |
| Robusta Coffee | 3 | 12 | 20 | Low Stock ⚠ |
| Coffee Sampler | - | 0 | 5 | Out of Stock [Restock] |

Click stock number to edit inline:
[Product Row]
Stock: [12] [Update]

Bulk Actions:
[ ] Select all
[Update Stock] [Set Thresholds] [Export]

Inventory Settings:
Low Stock Threshold (default): [20] units
[ ] Email me when products are low stock
[ ] Automatically hide out-of-stock products
```

---

### Stage 6: Pricing & Promotions

**User Goal**: Set competitive prices and run occasional promotions

**Actions**:
1. Pedro reviews current pricing
2. Adjusts prices based on costs
3. Sets up bulk/wholesale pricing tiers
4. Creates a promotional discount
5. Sets promotion duration
6. Monitors promotion performance

**Touchpoints**:
- Pricing overview
- Price edit interface
- Bulk pricing tiers
- Promotion creation
- Discount settings
- Promotion analytics

**Emotions**: Strategic, competitive, wanting to drive sales

**Pain Points**:
- No easy way to see all prices at once
- Bulk pricing setup is confusing
- Promotions are hard to set up
- Can't compare with competitor pricing

**Opportunities**:
- Pricing overview dashboard
- Guided bulk pricing setup
- Simple promotion wizard
- Price suggestion tools

**Design Requirements**:
```
Pricing Overview:

Price List View:
| Product | Base Price | Bulk 10+ | Bulk 50+ | Status |
|---------|------------|----------|----------|--------|
| Arabica | PHP 180 | PHP 170 | PHP 160 | Active |
| Robusta | PHP 150 | PHP 140 | PHP 130 | Active |

[Edit] opens inline or modal

Create Promotion:
Promotion Name: [_____________]
"e.g., Holiday Sale"

Discount Type:
( ) Percentage off: [__]%
( ) Fixed amount: PHP [____]
( ) Buy X Get Y

Apply To:
( ) All products
( ) Selected products [Choose]
( ) Specific category

Duration:
Start: [Date picker] at [Time]
End: [Date picker] at [Time]

[ ] Show countdown on products
[ ] Feature on storefront

[Preview] [Create Promotion]

Active Promotions:
| Name | Discount | Products | Ends | Orders |
|------|----------|----------|------|--------|
| Holiday Sale | 15% off | All | Dec 31 | 23 |
[Pause] [Edit] [End]
```

---

### Stage 7: Storefront Customization

**User Goal**: Create an attractive, branded online shop

**Actions**:
1. Pedro accesses storefront settings
2. Customizes color theme
3. Arranges featured products
4. Adds "About Us" content
5. Sets up product collections
6. Configures policies (shipping, returns)
7. Previews and publishes changes

**Touchpoints**:
- Storefront editor
- Theme customization
- Featured products selector
- About/Story page editor
- Collections manager
- Policy templates
- Live preview

**Emotions**: Creative, building brand, wanting professional appearance

**Pain Points**:
- Limited customization options
- Preview doesn't match live site
- Collections are confusing to set up
- Mobile storefront looks different

**Opportunities**:
- Simple theme presets
- Real-time preview
- Smart collection suggestions
- Mobile/desktop preview toggle

**Design Requirements**:
```
Storefront Customization:

[Theme]
Primary Color: [#0056D2 picker]
Accent Color: [picker]
Theme Style: [Light / Dark]

[Layout]
Header Style: [Logo Left / Logo Center]
Product Grid: [3 columns / 4 columns]

[Featured Section]
Title: "Featured Products"
Products: (drag to reorder)
- [Product 1] [x]
- [Product 2] [x]
- [+ Add Product]

[Collections]
Create collection:
Name: [Best Sellers]
Products: [Select products]
Display on homepage: [Yes/No]

[About/Story]
[Rich text editor]
- Our cooperative was founded in...
- Farmer photos gallery

[Policies]
Shipping Policy: [Use template] or [Custom]
Return Policy: [Use template] or [Custom]
Payment Terms: [Use template] or [Custom]

[Preview] - Toggle: [Mobile] [Desktop]
[Publish Changes]
```

---

### Stage 8: Product Organization

**User Goal**: Organize products so customers can find what they need

**Actions**:
1. Pedro creates product collections
2. Assigns products to collections
3. Sets collection display order
4. Creates featured/seasonal collections
5. Archives discontinued products
6. Manages product visibility

**Touchpoints**:
- Collections management
- Product assignment
- Display order controls
- Featured collection settings
- Archive functionality
- Visibility toggles

**Emotions**: Organizing, planning, seasonal thinking

**Pain Points**:
- Products can only be in one collection
- No way to schedule collection changes
- Archived products are hard to find
- Bulk assignment is tedious

**Opportunities**:
- Multi-collection assignment
- Scheduled collection activation
- Archive management view
- Bulk product actions

**Design Requirements**:
```
Collections Management:

Collections List:
| Collection | Products | Visibility | Order |
|------------|----------|------------|-------|
| Coffee Beans | 5 | Visible | 1 [↑↓] |
| Ground Coffee | 4 | Visible | 2 [↑↓] |
| Gift Sets | 3 | Visible | 3 [↑↓] |
| Seasonal (Holiday) | 2 | Hidden | - |

[+ Create Collection]

Edit Collection:
Name: [Gift Sets]
Description: [____________]
Image: [Upload]

Products in this collection:
[Search to add products]
- Coffee Sampler Pack [x]
- Premium Duo Set [x]
- Corporate Gift Box [x]

Display:
[x] Show on storefront navigation
[x] Show on homepage

Scheduling (optional):
Show from: [Date] to [Date]

[Save Collection]

Product Visibility:
| Product | Visibility | Collections |
|---------|------------|-------------|
| Arabica | Visible | Coffee Beans, Featured |
| Old Product | Archived | - [Restore] |
```

---

### Stage 9: Ongoing Product Management

**User Goal**: Keep my product catalog current and optimized

**Actions**:
1. Pedro reviews product performance
2. Updates underperforming product descriptions
3. Adds new products as available
4. Deactivates seasonal products
5. Responds to customer questions about products
6. Monitors competitor offerings

**Touchpoints**:
- Product performance analytics
- Product edit interface
- Quick actions (activate/deactivate)
- Customer questions queue
- Market comparison tools

**Emotions**: Optimizing, responsive, competitive

**Pain Points**:
- No insight into what's working
- Editing is time-consuming
- Customer questions scattered
- Manual competitive research

**Opportunities**:
- Product performance dashboard
- Quick edit capabilities
- Centralized Q&A management
- Performance recommendations

**Design Requirements**:
```
Product Performance Dashboard:

Top Performers (Last 30 days):
1. Premium Arabica - 45 orders, PHP 12,500
2. Coffee Sampler - 28 orders, PHP 5,600
3. Robusta Blend - 22 orders, PHP 4,400

Low Performers:
- Decaf Coffee - 2 orders (Consider: lower price, better photos)
- Instant Pack - 0 orders (Consider: archive or promote)

Quick Actions:
[Boost with promotion] [Improve listing]

Customer Questions:
3 unanswered questions
| Product | Question | Date |
|---------|----------|------|
| Arabica | "Is this organic?" | 2 days ago |
[Answer] opens quick response

Recommendations:
- Add 3 more products to improve discoverability
- Update seasonal products for upcoming holiday
- Respond to pending questions (avg response: 2.5 days)
```

---

## Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Shop Profile Completion | > 90% | Field completion rate |
| First Product Published | < 30 min from approval | Time tracking |
| Average Products per Shop | > 10 | Product count |
| Products with 3+ Photos | > 70% | Photo count |
| Bulk Pricing Adoption | > 50% | Feature usage |
| Collection Usage | > 40% create collections | Feature usage |
| Storefront Customization | > 60% customize | Setting changes |
| Inventory Accuracy | > 95% | Stockout incidents |
| Product Update Frequency | Monthly average | Edit tracking |
| Question Response Time | < 24 hours | Response analytics |

---

## Implementation Status

| Feature | Status | Notes |
|---------|--------|-------|
| Shop profile settings | TBD | Logo, banner, description |
| Product creation wizard | TBD | Multi-step form |
| Product photo upload | TBD | Mobile optimization |
| Variant management | TBD | Matrix editor |
| Inventory dashboard | TBD | Inline editing |
| Bulk pricing tiers | TBD | Tier configuration |
| Promotions system | TBD | Discount engine |
| Storefront customization | TBD | Theme settings |
| Collections management | TBD | Product grouping |
| Performance analytics | TBD | Dashboard stats |
| Customer questions | TBD | Q&A management |

---

## Recommendations

### Priority 1: Streamlined Product Creation
1. Implement wizard-style product creation with clear steps
2. Enable camera capture directly from product form
3. Auto-compress images on upload for mobile
4. Provide category suggestions based on product name

### Priority 2: Mobile-First Management
1. Design all interfaces for thumb-friendly interaction
2. Enable offline product drafts that sync when connected
3. Implement quick actions for common tasks
4. Use bottom sheets instead of full-page navigations

### Priority 3: Inventory Simplification
1. Create inline editing for stock quantities
2. Implement configurable low stock alerts
3. Add bulk update tools for multiple products
4. Show inventory health score on dashboard

### Priority 4: Storefront Quality
1. Provide theme presets for quick setup
2. Create guided storefront improvement tips
3. Enable mobile/desktop preview toggle
4. Add policy templates specific to BARMM context

### Priority 5: Performance Optimization
1. Build product performance dashboard
2. Show actionable recommendations
3. Track and surface customer questions
4. Provide competitive benchmarking tools

---

## Implementation Plan

### Phase 1: Frontend Foundation

**Pages:**
- `frontend/src/app/(tenant)/portal/shop/page.tsx` - Shop settings overview
- `frontend/src/app/(tenant)/portal/shop/profile/page.tsx` - Shop profile edit
- `frontend/src/app/(tenant)/portal/shop/storefront/page.tsx` - Storefront customization
- `frontend/src/app/(tenant)/portal/products/page.tsx` - Product list/inventory
- `frontend/src/app/(tenant)/portal/products/new/page.tsx` - Add product wizard
- `frontend/src/app/(tenant)/portal/products/[id]/page.tsx` - Edit product
- `frontend/src/app/(tenant)/portal/products/collections/page.tsx` - Collections management
- `frontend/src/app/(tenant)/portal/products/inventory/page.tsx` - Inventory dashboard
- `frontend/src/app/(tenant)/portal/promotions/page.tsx` - Promotions management
- `frontend/src/app/(tenant)/portal/performance/page.tsx` - Product performance

**Components:**
- `frontend/src/components/shop/ShopProfileForm.tsx` - Logo, banner, description
- `frontend/src/components/shop/ImageUploader.tsx` - With crop and guidelines
- `frontend/src/components/shop/StorefrontPreview.tsx` - Mobile/desktop toggle
- `frontend/src/components/shop/ThemeCustomizer.tsx` - Color and layout options
- `frontend/src/components/products/ProductWizard.tsx` - Multi-step creation
- `frontend/src/components/products/ProductBasicInfo.tsx` - Name, category, description
- `frontend/src/components/products/ProductPhotos.tsx` - Gallery with reorder
- `frontend/src/components/products/ProductPricing.tsx` - Base and bulk pricing
- `frontend/src/components/products/ProductVariants.tsx` - Variant matrix editor
- `frontend/src/components/products/ProductInventory.tsx` - Stock and thresholds
- `frontend/src/components/products/ProductTable.tsx` - List with inline editing
- `frontend/src/components/products/CollectionCard.tsx` - Collection display
- `frontend/src/components/products/CollectionForm.tsx` - Create/edit collection
- `frontend/src/components/promotions/PromotionForm.tsx` - Discount creation
- `frontend/src/components/promotions/PromotionCard.tsx` - Active promotion display
- `frontend/src/components/performance/ProductPerformanceCard.tsx` - Stats display
- `frontend/src/components/performance/RecommendationsPanel.tsx` - Action items

**shadcn/ui Components Used:**
- Card, Button, Badge for product cards
- Form, Input, Textarea, Select for forms
- Table for product and inventory lists
- Dialog for quick actions and confirmations
- Sheet for mobile filters and editors
- Tabs for product detail sections
- Switch for toggles (visibility, tracking)
- Slider for bulk pricing tiers
- Calendar for promotion scheduling

### Phase 2: State & Services

**Hooks:**
- `frontend/src/lib/hooks/useShopProfile.ts` - Shop settings state
- `frontend/src/lib/hooks/useProducts.ts` - Product list with filters
- `frontend/src/lib/hooks/useProduct.ts` - Single product CRUD
- `frontend/src/lib/hooks/useProductWizard.ts` - Wizard step state
- `frontend/src/lib/hooks/useVariants.ts` - Variant management
- `frontend/src/lib/hooks/useInventory.ts` - Inventory updates
- `frontend/src/lib/hooks/useCollections.ts` - Collection CRUD
- `frontend/src/lib/hooks/usePromotions.ts` - Promotion management
- `frontend/src/lib/hooks/useProductPerformance.ts` - Analytics data
- `frontend/src/lib/hooks/useImageUpload.ts` - Image upload with compression

**Services:**
- `frontend/src/lib/services/shop.ts` - Shop profile API
- `frontend/src/lib/services/products.ts` - Product CRUD
- `frontend/src/lib/services/variants.ts` - Variant operations
- `frontend/src/lib/services/inventory.ts` - Stock management
- `frontend/src/lib/services/collections.ts` - Collection operations
- `frontend/src/lib/services/promotions.ts` - Promotion API
- `frontend/src/lib/services/analytics.ts` - Performance data

**Types:**
- `frontend/src/lib/types/shop.ts` - ShopProfile, StorefrontSettings
- `frontend/src/lib/types/product.ts` - Product, Variant, Category
- `frontend/src/lib/types/inventory.ts` - StockItem, StockThreshold
- `frontend/src/lib/types/collection.ts` - Collection, CollectionProduct
- `frontend/src/lib/types/promotion.ts` - Promotion, DiscountType
- `frontend/src/lib/types/analytics.ts` - ProductStats, PerformanceData

### Phase 3: Backend Integration

**Endpoints (`backend/apps/tenant/api.py`):**
- `GET /api/shop` - Get shop profile
- `PATCH /api/shop` - Update shop profile
- `POST /api/shop/logo` - Upload shop logo
- `POST /api/shop/banner` - Upload shop banner
- `GET /api/shop/storefront` - Get storefront settings
- `PATCH /api/shop/storefront` - Update storefront settings

**Endpoints (`backend/apps/products/api.py`):**
- `GET /api/tenant/products` - List tenant products
- `POST /api/tenant/products` - Create product
- `GET /api/tenant/products/{id}` - Get product detail
- `PATCH /api/tenant/products/{id}` - Update product
- `DELETE /api/tenant/products/{id}` - Delete product
- `POST /api/tenant/products/{id}/photos` - Add photos
- `PATCH /api/tenant/products/{id}/photos/reorder` - Reorder photos
- `POST /api/tenant/products/{id}/variants` - Add variants
- `PATCH /api/tenant/products/{id}/inventory` - Update stock

**Endpoints (`backend/apps/products/api.py`):**
- `GET /api/tenant/collections` - List collections
- `POST /api/tenant/collections` - Create collection
- `PATCH /api/tenant/collections/{id}` - Update collection
- `DELETE /api/tenant/collections/{id}` - Delete collection
- `POST /api/tenant/collections/{id}/products` - Add products

**Endpoints (`backend/apps/promotions/api.py`):**
- `GET /api/tenant/promotions` - List promotions
- `POST /api/tenant/promotions` - Create promotion
- `PATCH /api/tenant/promotions/{id}` - Update promotion
- `POST /api/tenant/promotions/{id}/pause` - Pause promotion
- `POST /api/tenant/promotions/{id}/end` - End promotion

**Endpoints (`backend/apps/analytics/api.py`):**
- `GET /api/tenant/analytics/products` - Product performance
- `GET /api/tenant/analytics/inventory` - Inventory health
- `GET /api/tenant/analytics/recommendations` - Action items

**Schemas (`backend/apps/*/schemas.py`):**
- `ShopProfileSchema`, `StorefrontSettingsSchema`
- `ProductCreateSchema`, `ProductUpdateSchema`
- `VariantSchema`, `VariantMatrixSchema`
- `CollectionSchema`, `CollectionCreateSchema`
- `PromotionSchema`, `PromotionCreateSchema`
- `ProductPerformanceSchema`, `InventoryHealthSchema`

### Phase 4: Polish & UX

**Loading States:**
- Skeleton for product list table
- Skeleton for shop profile form
- Image upload progress indicators
- Product wizard step transitions

**Error Handling:**
- Image upload failure with retry
- Stock update validation errors
- Variant conflict handling
- Promotion overlap warnings

**Animations:**
- Image reorder drag feedback
- Variant matrix generation
- Stock update confirmation
- Promotion activation pulse

**Accessibility:**
- Drag-and-drop keyboard alternatives
- Image alt text prompts
- Form validation announcements
- Table keyboard navigation

**Mobile Optimization:**
- Bottom sheet for product quick edit
- Swipe actions on product list
- Touch-friendly image reordering
- Camera capture for product photos

### Implementation Sequence

**Week 1-2: Shop Profile**
1. Shop profile form with logo/banner
2. Image uploader with crop tool
3. Description editor with templates
4. Contact and operating hours
5. Shop preview component

**Week 3-4: Product Creation**
6. Product list table (depends on shop setup)
7. Product wizard container
8. Basic info form (step 1)
9. Photo gallery with reorder (step 2)
10. Pricing and bulk tiers (step 3)

**Week 5-6: Variants & Inventory**
11. Variant option builder (depends on #10)
12. Variant matrix editor
13. Inventory dashboard
14. Inline stock editing
15. Low stock alerts

**Week 7-8: Collections & Organization**
16. Collections list page
17. Collection create/edit form
18. Product assignment to collections
19. Collection visibility and scheduling
20. Storefront customization

**Week 9-10: Promotions & Performance**
21. Promotions list page
22. Promotion creation wizard
23. Promotion scheduling
24. Product performance dashboard
25. Recommendations and Q&A panel

---

## Implementation Status

*Audited: December 30, 2025*

### Frontend Pages
| Page | Status | Path | Notes |
|------|--------|------|-------|
| Tenant Dashboard | ✅ Exists | `frontend/src/app/(tenant)/dashboard/page.tsx` | Main dashboard |
| Shop Overview | ✅ Exists | `frontend/src/app/(tenant)/shop/page.tsx` | Shop settings |
| Shop Products | ✅ Exists | `frontend/src/app/(tenant)/shop/products/page.tsx` | Product list |
| Business Profile | ✅ Exists | `frontend/src/app/(tenant)/business/page.tsx` | Business info |
| Business Documents | ✅ Exists | `frontend/src/app/(tenant)/business/documents/page.tsx` | Document management |
| Impact Stories | ✅ Exists | `frontend/src/app/(tenant)/impact/page.tsx` | Impact listing |
| New Impact Story | ✅ Exists | `frontend/src/app/(tenant)/impact/new/page.tsx` | Create story |
| Settings | ✅ Exists | `frontend/src/app/(tenant)/settings/page.tsx` | Tenant settings |
| Domain Settings | ✅ Exists | `frontend/src/app/(tenant)/settings/domains/page.tsx` | Custom domains |
| Shop Profile Edit | ❌ Missing | `frontend/src/app/(tenant)/portal/shop/profile/page.tsx` | Logo, banner edit |
| Storefront Customization | ❌ Missing | `frontend/src/app/(tenant)/portal/shop/storefront/page.tsx` | Theme settings |
| Add Product | ❌ Missing | `frontend/src/app/(tenant)/portal/products/new/page.tsx` | Product wizard |
| Edit Product | ❌ Missing | `frontend/src/app/(tenant)/portal/products/[id]/page.tsx` | Product edit |
| Collections | ❌ Missing | `frontend/src/app/(tenant)/portal/products/collections/page.tsx` | Product grouping |
| Inventory Dashboard | ❌ Missing | `frontend/src/app/(tenant)/portal/products/inventory/page.tsx` | Stock management |
| Promotions | ❌ Missing | `frontend/src/app/(tenant)/portal/promotions/page.tsx` | Discount management |
| Performance | ❌ Missing | `frontend/src/app/(tenant)/portal/performance/page.tsx` | Product analytics |

### Components
| Component | Status | Path | Notes |
|-----------|--------|------|-------|
| ShopProfileForm | 🚧 Needs Audit | `frontend/src/components/shop/` | Logo, banner, description |
| ImageUploader | 🚧 Needs Audit | `frontend/src/components/shop/` | With crop guidelines |
| StorefrontPreview | ❌ Missing | `frontend/src/components/shop/` | Mobile/desktop toggle |
| ThemeCustomizer | ❌ Missing | `frontend/src/components/shop/` | Color and layout |
| ProductWizard | ❌ Missing | `frontend/src/components/products/` | Multi-step creation |
| ProductBasicInfo | 🚧 Needs Audit | `frontend/src/components/products/` | Name, category, desc |
| ProductPhotos | 🚧 Needs Audit | `frontend/src/components/products/` | Gallery with reorder |
| ProductPricing | ❌ Missing | `frontend/src/components/products/` | Base and bulk pricing |
| ProductVariants | ❌ Missing | `frontend/src/components/products/` | Variant matrix editor |
| ProductInventory | ❌ Missing | `frontend/src/components/products/` | Stock and thresholds |
| ProductTable | 🚧 Needs Audit | `frontend/src/components/products/` | List with inline edit |
| CollectionCard | ❌ Missing | `frontend/src/components/products/` | Collection display |
| CollectionForm | ❌ Missing | `frontend/src/components/products/` | Create/edit collection |
| PromotionForm | ❌ Missing | `frontend/src/components/promotions/` | Discount creation |
| ProductPerformanceCard | ❌ Missing | `frontend/src/components/performance/` | Stats display |

### Backend APIs
| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| GET /api/tenant/products | ✅ Exists | `backend/apps/tenant/api.py` | List products |
| GET /api/tenant/storefront | ✅ Exists | `backend/apps/tenant/api.py` | Storefront data |
| GET /api/tenant/profile | ✅ Exists | `backend/apps/tenant/api.py` | Business profile |
| GET /api/tenant/impact | ✅ Exists | `backend/apps/tenant/api.py` | Impact stories |
| GET /api/tenant/documents | ✅ Exists | `backend/apps/tenant/api.py` | Documents list |
| GET /api/tenant/analytics | ✅ Exists | `backend/apps/tenant/api.py` | Basic analytics |
| POST /api/tenant/products | ❌ Missing | `backend/apps/tenant/api.py` | Create product |
| PATCH /api/tenant/products/{id} | ❌ Missing | `backend/apps/tenant/api.py` | Update product |
| POST /api/tenant/products/{id}/photos | ❌ Missing | `backend/apps/tenant/api.py` | Add photos |
| PATCH /api/tenant/products/{id}/inventory | ❌ Missing | `backend/apps/tenant/api.py` | Update stock |
| GET /api/tenant/collections | ❌ Missing | `backend/apps/tenant/api.py` | List collections |
| POST /api/tenant/collections | ❌ Missing | `backend/apps/tenant/api.py` | Create collection |
| GET /api/tenant/promotions | ❌ Missing | `backend/apps/tenant/api.py` | List promotions |
| POST /api/tenant/promotions | ❌ Missing | `backend/apps/tenant/api.py` | Create promotion |
| GET /api/tenant/analytics/products | ❌ Missing | `backend/apps/tenant/api.py` | Product performance |

### Overall Progress
- **Frontend**: 9/17 pages (53%)
- **Components**: 5/15 need audit (33%)
- **Backend**: 6/15 endpoints (40%)
