# Product Discovery to Checkout Journey - MoroNegosyo

## Overview

This journey maps the complete shopping experience for consumers on the MoroNegosyo marketplace, from initial product discovery through successful checkout. The journey emphasizes trust-building for Bangsamoro cooperative and social enterprise products, accessibility for users with varying connectivity, and conversion optimization at each stage.

## Persona

**Name**: Maria Santos
**Age**: 35
**Role**: Small Business Owner (Sari-sari Store)
**Location**: Cotabato City, Maguindanao
**Context**: Maria runs a sari-sari store and is looking for wholesale supplies of local products to resell. She has a smartphone with mobile data and is moderately comfortable with online shopping. She values supporting local cooperatives but needs competitive pricing for her business.

**Goals**:
- Find quality local products at wholesale prices
- Discover reliable cooperative suppliers
- Complete purchases efficiently with clear delivery timelines
- Build ongoing relationships with trusted sellers

**Tech Comfort**: Moderate - uses Facebook Marketplace, GCash regularly
**Connectivity**: 4G mobile data, occasionally unstable
**Shopping Frequency**: Weekly for business supplies

---

## Journey Map

### Stage 1: Awareness & Entry

**User Goal**: Understand what MoroNegosyo offers and how it can help my business

**Actions**:
1. Maria hears about MoroNegosyo from a fellow store owner
2. Searches "MoroNegosyo" or "Bangsamoro products online"
3. Lands on the homepage
4. Scans the hero section and value proposition
5. Notices categories relevant to her needs

**Touchpoints**:
- Google search results / Social media link
- Homepage hero section
- Category navigation bar
- Featured products section
- Impact statistics banner

**Emotions**: Curious, slightly skeptical, hopeful

**Pain Points**:
- Unclear if wholesale pricing is available
- Uncertainty about seller legitimacy
- Wondering if delivery reaches her area
- Concerned about payment security

**Opportunities**:
- Display "Wholesale Available" badges prominently
- Show CSEA verification badges early
- Include Cotabato City in visible delivery areas
- Display secure payment icons in header

**Design Requirements**:
```
- Hero section loads within 3 seconds on 4G
- Value proposition visible without scrolling
- Category icons are large, touch-friendly (min 48px)
- "Shop Wholesale" CTA visible on homepage
- Trust signals (CSEA badge, secure payment) in header
```

---

### Stage 2: Product Discovery

**User Goal**: Find specific products that match my business needs

**Actions**:
1. Maria taps on "Food & Beverages" category
2. Uses filter to select "Wholesale Available"
3. Sorts by price (low to high)
4. Scrolls through product cards
5. Saves interesting products to wishlist
6. Taps on a promising product for details

**Touchpoints**:
- Category page with filters
- Sort/filter controls
- Product grid/cards
- Wishlist heart icon
- Product card quick actions

**Emotions**: Focused, comparing options, building mental shortlist

**Pain Points**:
- Too many products to browse efficiently
- Hard to compare prices across similar items
- Unclear minimum order quantities
- Filter reset when navigating back

**Opportunities**:
- Add "Minimum Order" filter option
- Show bulk pricing tiers on product cards
- Enable quick comparison view
- Persist filters in URL for back navigation
- Add "Recently Viewed" section

**Design Requirements**:
```
- Product cards show: name, price, seller, MOQ, wholesale badge
- Filters are sticky on scroll (mobile sheet, desktop sidebar)
- Infinite scroll or "Load More" (not pagination) for mobile
- Empty state with helpful suggestions if no results
- Quick add to wishlist without page reload
```

---

### Stage 3: Product Evaluation

**User Goal**: Determine if this product meets my quality and price requirements

**Actions**:
1. Maria views product images (zooms in on details)
2. Reads product description and specifications
3. Checks bulk pricing tiers
4. Reviews seller information and ratings
5. Reads customer reviews (filters for business buyers)
6. Checks delivery options and costs
7. Sends inquiry to seller via message

**Touchpoints**:
- Product gallery with zoom
- Product details tabs (Description, Specs, Reviews)
- Pricing tier table
- Seller profile card
- Review section with filters
- Delivery calculator
- "Contact Seller" button

**Emotions**: Analytical, cautious, building trust, considering alternatives

**Pain Points**:
- Product photos don't show actual quality
- No way to verify reviews are genuine
- Bulk pricing unclear or hidden
- Can't estimate total cost with delivery
- Slow response from sellers

**Opportunities**:
- Require multiple product photos from sellers
- Add "Verified Purchase" badges on reviews
- Show bulk pricing prominently with calculator
- Display estimated delivery cost before cart
- Show seller response time metrics

**Design Requirements**:
```
- Image gallery supports pinch-to-zoom on mobile
- Bulk pricing table shows tiers: 10+, 50+, 100+ units
- "Estimated Total" calculator for quantity selection
- Seller card shows: rating, response time, member since, location
- Reviews filterable by "Business Buyers" tag
- Sticky "Add to Cart" bar on mobile scroll
```

---

### Stage 4: Cart Building

**User Goal**: Collect all needed products and understand total investment

**Actions**:
1. Maria adds product to cart with quantity
2. Continues browsing for related products
3. Adds multiple products from different sellers
4. Reviews cart summary periodically
5. Adjusts quantities based on budget
6. Removes items that don't fit budget
7. Checks if free shipping threshold is reachable

**Touchpoints**:
- Add to cart confirmation toast
- Cart icon with item count
- Mini cart preview dropdown
- Cart page with full details
- Quantity adjustment controls
- Free shipping progress bar

**Emotions**: Calculating, budget-conscious, optimizing

**Pain Points**:
- Cart from multiple sellers has multiple shipping costs
- Hard to track running total while browsing
- Minimum order quantities not enforced until checkout
- Items go out of stock while deciding

**Opportunities**:
- Show running total in header
- Group cart items by seller with subtotals
- Display shipping cost per seller
- Show "Add PHP X more for free shipping" message
- Real-time stock availability checking

**Design Requirements**:
```
- Toast confirmation shows: product name, quantity, new cart total
- Cart icon badge shows item count (max 99+)
- Cart page groups items by seller with subtotals
- Per-seller shipping costs visible
- Free shipping progress bar per seller
- Quantity input allows direct typing (not just +/- buttons)
- "Save for Later" option for undecided items
```

---

### Stage 5: Checkout Initiation

**User Goal**: Begin the purchase process with clear expectations

**Actions**:
1. Maria clicks "Proceed to Checkout"
2. Sees option to checkout as guest or sign in
3. Chooses to create account (for order tracking)
4. Enters email and basic information
5. Verifies email (if required)
6. Proceeds to address entry

**Touchpoints**:
- Checkout CTA button
- Guest vs. Account choice screen
- Registration form (minimal fields)
- Email verification screen
- Progress indicator (Step 1 of 3)

**Emotions**: Committed, slightly anxious, wanting efficiency

**Pain Points**:
- Forced registration feels intrusive
- Long registration forms cause abandonment
- Email verification breaks flow
- Progress feels unclear

**Opportunities**:
- Offer guest checkout prominently
- Minimize registration to 3 fields (name, email, password)
- Delay email verification until after purchase
- Show clear 3-step progress indicator
- Pre-fill from browser autofill

**Design Requirements**:
```
- Guest checkout option appears first/prominently
- Account creation: Name, Email, Password only
- Password requirements shown inline (not after error)
- "Sign in with Google" option for faster registration
- Progress indicator: Contact > Delivery > Payment
- Form validates inline, not on submit
```

---

### Stage 6: Delivery Information

**User Goal**: Specify where and how I want products delivered

**Actions**:
1. Maria selects delivery address or adds new one
2. Chooses province (Maguindanao) from dropdown
3. Selects municipality (Cotabato City)
4. Enters barangay and street address
5. Adds delivery instructions for her store
6. Selects delivery method/speed
7. Reviews delivery estimate

**Touchpoints**:
- Address form with cascading dropdowns
- Saved addresses (for returning customers)
- Delivery instructions textarea
- Shipping method selection
- Delivery date/time estimate

**Emotions**: Focused, wanting accuracy, concerned about delivery reliability

**Pain Points**:
- Address forms not localized for BARMM geography
- Unclear if delivery reaches specific barangays
- No option for store/pickup location
- Delivery estimates are vague

**Opportunities**:
- Pre-populate BARMM provinces, municipalities, barangays
- Show "Delivery Available" confirmation per area
- Offer "Pickup from Cooperative" option
- Display specific delivery date range
- Allow multiple addresses (home vs. store)

**Design Requirements**:
```
- Province dropdown limited to BARMM regions
- Municipality dropdown filters based on province
- Barangay dropdown filters based on municipality
- "Delivery to this area: Yes/No" indicator after barangay
- Delivery instructions field with placeholder examples
- Shipping options show: method, price, estimated days
- "Same as billing" checkbox for matching addresses
```

---

### Stage 7: Payment Selection

**User Goal**: Pay securely using my preferred payment method

**Actions**:
1. Maria reviews order summary
2. Sees available payment methods
3. Selects GCash (her preferred method)
4. Enters or confirms GCash number
5. Reviews total amount
6. Clicks "Place Order"
7. Redirected to GCash for authorization
8. Completes payment authentication

**Touchpoints**:
- Order summary card
- Payment method selection
- Payment details form
- Security indicators
- "Place Order" CTA
- External payment gateway redirect

**Emotions**: Nervous about payment, wanting security confirmation, excited to complete

**Pain Points**:
- Preferred payment method not available
- Hidden fees revealed at last step
- Unclear what happens after clicking "Place Order"
- Payment gateway timeout or error

**Opportunities**:
- Support popular PH payment methods (GCash, Maya, bank transfer)
- Show all fees clearly before payment step
- Explain next steps before order placement
- Handle payment errors gracefully with retry option
- Save payment preferences for returning customers

**Design Requirements**:
```
- Payment methods shown as clickable cards with logos
- Order summary sticky/visible while selecting payment
- All fees itemized: subtotal, shipping, payment fee, total
- Security badges near payment form (SSL, GCash verified)
- "Place Order" button shows total amount
- Loading state during payment processing
- Error handling with clear retry instructions
```

---

### Stage 8: Order Confirmation

**User Goal**: Confirm my order was successful and understand next steps

**Actions**:
1. Maria sees success confirmation screen
2. Notes order number for reference
3. Reviews order summary
4. Checks estimated delivery date
5. Sees option to download/share receipt
6. Receives confirmation email
7. Accesses order tracking

**Touchpoints**:
- Success confirmation page
- Order number display
- Order summary
- Email confirmation
- Download/Share receipt buttons
- "Track Order" button
- "Continue Shopping" CTA

**Emotions**: Relieved, satisfied, anticipating delivery, may share experience

**Pain Points**:
- Confirmation page closes before saving details
- No SMS confirmation (email may be missed)
- Unclear when tracking will be available
- No way to contact about order issues

**Opportunities**:
- Keep confirmation accessible via account
- Send SMS + email confirmation
- Show when tracking will be active
- Provide direct link to contact seller
- Suggest related products for future orders

**Design Requirements**:
```
- Success icon animation for positive feedback
- Order number prominently displayed (copyable)
- "Order sent to [email]" confirmation message
- Delivery estimate: "Expected [date range]"
- "Track Order" and "Contact Seller" buttons
- Receipt download (PDF) and share (native share)
- "Continue Shopping" link below fold
```

---

### Stage 9: Post-Purchase Tracking

**User Goal**: Monitor my order status until delivery

**Actions**:
1. Maria receives shipping notification
2. Clicks tracking link in SMS/email
3. Views order status timeline
4. Checks current location/status
5. Sees estimated delivery update
6. Receives delivery notification
7. Confirms receipt

**Touchpoints**:
- Email/SMS notifications
- Order tracking page
- Status timeline visualization
- Delivery confirmation prompt
- Receipt/delivery confirmation

**Emotions**: Anticipating, occasionally anxious, satisfied upon delivery

**Pain Points**:
- Tracking information delayed or unavailable
- Status updates are vague
- No proactive delay notifications
- Can't contact driver/seller easily

**Opportunities**:
- Real-time tracking integration with couriers
- Proactive delay notifications
- Direct messaging with seller
- "Confirm Receipt" prompt to close order
- Review prompt after delivery confirmation

**Design Requirements**:
```
- Order timeline: Placed > Processing > Shipped > Delivered
- Current status highlighted with estimated time
- Courier tracking number clickable to external tracking
- Push notifications for status changes (opt-in)
- "Report Issue" button visible throughout
- "Confirm Receipt" button when marked delivered
- Auto-completion after 7 days if not disputed
```

---

## Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Homepage to Product View | > 60% | Analytics funnel |
| Product View to Add to Cart | > 15% | Analytics events |
| Cart to Checkout Start | > 65% | Funnel conversion |
| Checkout Completion Rate | > 75% | Funnel conversion |
| Overall Conversion Rate | > 3.5% | Order/Visit ratio |
| Average Order Value | > PHP 1,500 | Order analytics |
| Cart Abandonment Rate | < 60% | Funnel drop-off |
| Mobile Conversion Rate | > 3% | Device segmentation |
| Time to First Purchase | < 10 min | Session analytics |
| Repeat Purchase Rate | > 25% (90 days) | Customer cohorts |

---

## Implementation Status

| Feature | Status | Notes |
|---------|--------|-------|
| Homepage hero section | TBD | Design needed |
| Category navigation | TBD | Need product categories |
| Product listing with filters | TBD | Backend filters needed |
| Product detail page | TBD | Gallery, reviews structure |
| Wishlist functionality | TBD | User authentication req |
| Shopping cart | TBD | Multi-seller handling |
| Guest checkout | TBD | Balance with account creation |
| Address form (BARMM) | TBD | Need location data |
| Payment integration | TBD | GCash, Maya, bank transfer |
| Order confirmation | TBD | Email/SMS templates |
| Order tracking | TBD | Courier integration |

---

## Recommendations

### Priority 1: Trust & Credibility
1. Implement CSEA verification badges prominently on seller cards and product pages
2. Display "Wholesale Available" and bulk pricing clearly on product cards
3. Add "Verified Purchase" badges to genuine customer reviews
4. Show seller response time and order fulfillment metrics

### Priority 2: Mobile Optimization
1. Ensure all touchpoints work on 4G with < 3 second load times
2. Implement sticky Add to Cart on product pages
3. Use native share for receipts and product sharing
4. Optimize image loading with lazy loading and WebP format

### Priority 3: Conversion Optimization
1. Simplify checkout to 3 clear steps maximum
2. Offer guest checkout as the default option
3. Show free shipping threshold progress bar
4. Implement cart recovery emails for abandoned carts

### Priority 4: Local Context
1. Pre-populate BARMM-specific address dropdowns
2. Support GCash and Maya as primary payment methods
3. Show delivery availability confirmation per barangay
4. Enable "Pickup from Cooperative" option for local buyers

### Priority 5: Post-Purchase Experience
1. Send SMS confirmations (not just email)
2. Integrate courier tracking for real-time updates
3. Implement "Confirm Receipt" flow with review prompt
4. Create automated follow-up for repeat purchases

---

## Implementation Plan

### Phase 1: Frontend Foundation

**Pages:**
- `frontend/src/app/(public)/page.tsx` - Homepage with hero, categories, featured products
- `frontend/src/app/(public)/products/page.tsx` - Product listing with filters/sort
- `frontend/src/app/(public)/products/[slug]/page.tsx` - Product detail page
- `frontend/src/app/(public)/cart/page.tsx` - Shopping cart with multi-seller grouping
- `frontend/src/app/(public)/checkout/page.tsx` - Multi-step checkout flow
- `frontend/src/app/(public)/checkout/success/page.tsx` - Order confirmation
- `frontend/src/app/(public)/orders/[id]/page.tsx` - Order tracking page

**Components:**
- `frontend/src/components/products/ProductCard.tsx` - Product card with wholesale badge, MOQ, price
- `frontend/src/components/products/ProductGallery.tsx` - Image gallery with pinch-to-zoom
- `frontend/src/components/products/ProductFilters.tsx` - Sticky filter sidebar/sheet
- `frontend/src/components/products/BulkPricingTable.tsx` - Tier pricing display
- `frontend/src/components/products/SellerCard.tsx` - Seller info with CSEA badge, ratings
- `frontend/src/components/cart/CartItem.tsx` - Cart item with quantity controls
- `frontend/src/components/cart/CartSummary.tsx` - Grouped by seller with subtotals
- `frontend/src/components/cart/FreeShippingProgress.tsx` - Progress bar per seller
- `frontend/src/components/checkout/AddressForm.tsx` - BARMM cascading dropdowns
- `frontend/src/components/checkout/PaymentMethodSelector.tsx` - GCash, Maya, bank transfer
- `frontend/src/components/checkout/OrderTimeline.tsx` - Visual status timeline
- `frontend/src/components/ui/CategoryNav.tsx` - Touch-friendly category navigation

**shadcn/ui Components Used:**
- Card, Button, Badge, Skeleton for product cards
- Sheet for mobile filters
- Select for dropdowns and sorting
- Dialog for quick view modals
- Form, Input for checkout forms
- Tabs for product details sections
- Toast for add-to-cart confirmations

### Phase 2: State & Services

**Hooks:**
- `frontend/src/lib/hooks/useProducts.ts` - Product listing with filters, pagination
- `frontend/src/lib/hooks/useProduct.ts` - Single product detail
- `frontend/src/lib/hooks/useCart.ts` - Cart state management with local storage
- `frontend/src/lib/hooks/useCheckout.ts` - Checkout flow state
- `frontend/src/lib/hooks/useWishlist.ts` - Wishlist management
- `frontend/src/lib/hooks/useOrderTracking.ts` - Real-time order status
- `frontend/src/lib/hooks/useBARMMLocations.ts` - Province/municipality/barangay cascade

**Services:**
- `frontend/src/lib/services/products.ts` - Product API calls
- `frontend/src/lib/services/cart.ts` - Cart persistence and sync
- `frontend/src/lib/services/checkout.ts` - Order creation, payment initiation
- `frontend/src/lib/services/orders.ts` - Order history and tracking
- `frontend/src/lib/services/shipping.ts` - Delivery cost calculation

**Types:**
- `frontend/src/lib/types/product.ts` - Product, Variant, Category types
- `frontend/src/lib/types/cart.ts` - CartItem, CartSummary types
- `frontend/src/lib/types/checkout.ts` - Address, PaymentMethod, Order types
- `frontend/src/lib/types/shipping.ts` - ShippingOption, DeliveryEstimate types

### Phase 3: Backend Integration

**Endpoints (`backend/apps/products/api.py`):**
- `GET /api/products` - List products with filters, pagination
- `GET /api/products/{slug}` - Product detail with variants
- `GET /api/products/{id}/reviews` - Product reviews with business buyer filter
- `GET /api/categories` - Category tree

**Endpoints (`backend/apps/orders/api.py`):**
- `POST /api/cart` - Sync cart with backend
- `POST /api/orders` - Create order
- `GET /api/orders/{id}` - Order detail
- `GET /api/orders/{id}/tracking` - Tracking status
- `POST /api/orders/{id}/confirm-receipt` - Confirm delivery

**Endpoints (`backend/apps/core/api.py`):**
- `GET /api/locations/provinces` - BARMM provinces
- `GET /api/locations/municipalities/{province}` - Municipalities
- `GET /api/locations/barangays/{municipality}` - Barangays
- `GET /api/shipping/calculate` - Shipping cost calculation

**Schemas (`backend/apps/*/schemas.py`):**
- `ProductListSchema`, `ProductDetailSchema` with bulk pricing
- `CartSchema`, `CartItemSchema`
- `OrderCreateSchema`, `OrderDetailSchema`
- `AddressSchema` with BARMM fields
- `ShippingCalculationSchema`

### Phase 4: Polish & UX

**Loading States:**
- Skeleton loaders for product cards, product detail sections
- Skeleton for cart items during quantity updates
- Checkout step transition animations
- Order timeline skeleton during status fetch

**Error Handling:**
- Empty state for no search results with suggestions
- Out of stock handling with alternatives
- Payment failure with retry option
- Network error with offline indicator

**Animations:**
- Add to cart confirmation toast slide-in
- Wishlist heart animation on toggle
- Checkout step progress transitions
- Success confetti on order confirmation

**Accessibility:**
- Focus management in checkout flow
- Screen reader announcements for cart updates
- Keyboard navigation for product filters
- Alt text for all product images

**Mobile Optimization:**
- Sticky add-to-cart bar on product page
- Bottom sheet filters on mobile
- Swipe gestures for product gallery
- Native share for receipts

### Implementation Sequence

**Week 1-2: Core Browsing**
1. Homepage with hero and category navigation
2. Product listing page with basic filters
3. Product card component with essential info
4. Category page routing

**Week 3-4: Product Detail**
5. Product detail page layout
6. Image gallery with zoom (depends on #3)
7. Bulk pricing table component
8. Seller card with CSEA badge
9. Add to cart functionality

**Week 5-6: Cart & Wishlist**
10. Cart page with multi-seller grouping (depends on #9)
11. Cart item quantity controls
12. Free shipping progress indicator
13. Wishlist toggle and page
14. Save for later functionality

**Week 7-8: Checkout Flow**
15. Guest vs account checkout selection
16. BARMM address form with cascading dropdowns
17. Shipping method selection (depends on #16)
18. Payment method selection (GCash, Maya)
19. Order review and placement

**Week 9-10: Post-Purchase**
20. Order confirmation page (depends on #19)
21. Order tracking page with timeline
22. Order history page
23. Email/SMS notification integration
24. Review prompt after delivery

---

## Implementation Status

*Audited: December 30, 2025*

### Frontend Pages
| Page | Status | Path | Notes |
|------|--------|------|-------|
| Homepage | ✅ Exists | `frontend/src/app/(public)/page.tsx` | Hero, categories, featured products |
| Marketplace Browse | ✅ Exists | `frontend/src/app/(public)/marketplace/browse/page.tsx` | Product listing with filters |
| Product Detail | ✅ Exists | `frontend/src/app/(public)/marketplace/products/[slug]/page.tsx` | Product details |
| Shopping Cart | ✅ Exists | `frontend/src/app/(public)/marketplace/cart/page.tsx` | Cart with multi-seller grouping |
| Checkout | ✅ Exists | `frontend/src/app/(public)/marketplace/checkout/page.tsx` | Multi-step checkout flow |
| Storefronts List | ✅ Exists | `frontend/src/app/(public)/marketplace/storefronts/page.tsx` | Browse storefronts |
| Coop Storefront | ✅ Exists | `frontend/src/app/(coop)/coop/[shortname]/shop/page.tsx` | Individual coop shop |
| SE Storefront | ✅ Exists | `frontend/src/app/(se)/se/[shortname]/shop/page.tsx` | Individual SE shop |
| Coop Product Detail | ✅ Exists | `frontend/src/app/(coop)/coop/[shortname]/product/[id]/page.tsx` | Storefront product view |
| SE Product Detail | ✅ Exists | `frontend/src/app/(se)/se/[shortname]/product/[id]/page.tsx` | Storefront product view |
| Coop Cart | ✅ Exists | `frontend/src/app/(coop)/coop/[shortname]/cart/page.tsx` | Storefront cart |
| Coop Checkout | ✅ Exists | `frontend/src/app/(coop)/coop/[shortname]/checkout/page.tsx` | Storefront checkout |
| Order Tracking | ✅ Exists | `frontend/src/app/(account)/orders/[id]/page.tsx` | Order detail/tracking |
| Checkout Success | ❌ Missing | `frontend/src/app/(public)/marketplace/checkout/success/page.tsx` | Order confirmation page |
| Wishlist Page | ✅ Exists | `frontend/src/app/(account)/saved/page.tsx` | Saved/wishlist items |

### Components
| Component | Status | Path | Notes |
|-----------|--------|------|-------|
| ProductCard | 🚧 Needs Audit | `frontend/src/components/products/` | Check for wholesale badge, MOQ |
| ProductGallery | 🚧 Needs Audit | `frontend/src/components/products/` | Verify pinch-to-zoom |
| ProductFilters | 🚧 Needs Audit | `frontend/src/components/products/` | Check sticky behavior |
| BulkPricingTable | ❌ Missing | `frontend/src/components/products/` | Tier pricing display |
| SellerCard | 🚧 Needs Audit | `frontend/src/components/products/` | CSEA badge, ratings |
| CartItem | 🚧 Needs Audit | `frontend/src/components/cart/` | Quantity controls |
| CartSummary | 🚧 Needs Audit | `frontend/src/components/cart/` | Multi-seller grouping |
| FreeShippingProgress | ❌ Missing | `frontend/src/components/cart/` | Progress bar per seller |
| AddressForm | 🚧 Needs Audit | `frontend/src/components/checkout/` | BARMM dropdowns |
| PaymentMethodSelector | 🚧 Needs Audit | `frontend/src/components/checkout/` | GCash, Maya support |
| OrderTimeline | 🚧 Needs Audit | `frontend/src/components/orders/` | Visual status timeline |
| CategoryNav | 🚧 Needs Audit | `frontend/src/components/ui/` | Touch-friendly navigation |

### Backend APIs
| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| GET /api/public/products | ✅ Exists | `backend/apps/*/api.py` | Product listing |
| GET /api/public/categories | ✅ Exists | `backend/apps/*/api.py` | Category tree |
| GET /api/public/cooperatives | ✅ Exists | `backend/apps/*/api.py` | Cooperative directory |
| GET /api/public/social-enterprises | ✅ Exists | `backend/apps/*/api.py` | SE directory |
| POST /api/public/orders | ✅ Exists | `backend/apps/*/api.py` | Create order |
| GET /api/public/reviews | ✅ Exists | `backend/apps/*/api.py` | Product reviews |
| GET /api/core/shop/products | ✅ Exists | `backend/apps/core/api.py` | Shop products |
| GET /api/core/shop/orders | ✅ Exists | `backend/apps/core/api.py` | Shop orders |
| GET /api/locations/provinces | ❌ Missing | `backend/apps/core/api.py` | BARMM provinces |
| GET /api/locations/municipalities | ❌ Missing | `backend/apps/core/api.py` | Cascading municipalities |
| GET /api/locations/barangays | ❌ Missing | `backend/apps/core/api.py` | Cascading barangays |
| GET /api/shipping/calculate | ❌ Missing | `backend/apps/*/api.py` | Shipping cost calculation |

### Overall Progress
- **Frontend**: 14/15 pages (93%)
- **Components**: 4/12 confirmed (33% - needs deeper audit)
- **Backend**: 8/12 endpoints (67%)
