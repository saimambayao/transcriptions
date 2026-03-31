# Anonymous User - MoroNegosyo

## Overview
Anonymous users are visitors who browse the MoroNegosyo marketplace without creating an account. They represent the largest potential user base and are the primary conversion targets for the platform. Their experience must be frictionless to encourage exploration while strategically guiding them toward registration.

## Role Definition
**Type**: Anonymous (Unauthenticated)
**Portal Access**: Public Portal only (`/`)
**Authentication**: None required; session-based tracking only

## Capabilities

### Core Capabilities
| Capability | Description | Priority |
|------------|-------------|----------|
| Browse Products | View all published products in the marketplace | P0 |
| Search Products | Full-text search with filters (category, price, location) | P0 |
| View Product Details | Access complete product information, images, specifications | P0 |
| Visit Storefronts | Browse individual coop/SE shop pages | P0 |
| View Directories | Access cooperative and social enterprise directories | P1 |
| Read Impact Stories | View published impact stories and success cases | P1 |
| Guest Checkout | Complete purchase without account creation | P1 |
| Contact Sellers | Submit inquiry forms (with email capture) | P2 |
| Share Products | Share product links to social media | P2 |
| Compare Products | Side-by-side product comparison (up to 4) | P3 |

### Feature Access Matrix
| Feature | Access Level | Notes |
|---------|--------------|-------|
| Product Catalog | Full | No restrictions on viewing |
| Product Search | Full | All filters available |
| Storefronts | Full | Can view all published storefronts |
| Shopping Cart | Full | Session-based, not persisted |
| Wishlist | None | Requires account |
| Order History | None | Requires account |
| Reviews/Ratings | View Only | Cannot submit reviews |
| Checkout | Partial | Guest checkout only |
| Saved Addresses | None | Must enter each time |
| Loyalty Points | None | Requires account |
| Personalized Recommendations | None | No user data to personalize |
| MoroAcademy | Browse Only | Can view course catalog |

## User Journey Entry Points

1. **Direct URL Access**
   - User types `negosyo.bangsamoro.site` directly
   - Lands on homepage with featured products and categories
   - Path: Homepage > Browse > Product > Guest Checkout

2. **Search Engine Discovery**
   - User finds product via Google/Bing search
   - Lands directly on product detail page
   - Path: Product Page > Add to Cart > Guest Checkout

3. **Social Media Referral**
   - User clicks shared product/storefront link
   - Lands on specific product or storefront page
   - Path: Shared Content > Explore > Guest Checkout

4. **Storefront Direct Access**
   - User visits coop/SE storefront via custom domain or direct link
   - Example: `www.bangsamorocrafts.ph` or `/coop/bangsamoro-crafts`
   - Path: Storefront > Browse Products > Guest Checkout

5. **Impact Story Engagement**
   - User discovers platform through news/impact story
   - Lands on impact story page
   - Path: Story > Related Products/Coops > Explore > Convert

## Key Pages

| Page | Purpose | Route | Implementation |
|------|---------|-------|----------------|
| Homepage | Discovery, featured products, categories | `/` | Active |
| Product Catalog | Browse all products | `/products` | Active |
| Product Detail | View product information | `/products/[id]` | Active |
| Category Browse | Filter by category | `/products?category=[slug]` | Active |
| Search Results | Search results display | `/search?q=[query]` | Active |
| Coop Directory | List all cooperatives | `/coops` | Active |
| SE Directory | List all social enterprises | `/social-enterprises` | Active |
| Coop Storefront | Individual coop shop | `/coop/[slug]` | Active |
| SE Storefront | Individual SE shop | `/se/[slug]` | Active |
| Impact Stories | Success stories listing | `/impact` | Active |
| Story Detail | Individual story | `/impact/[slug]` | Active |
| Cart | Shopping cart view | `/cart` | Active |
| Guest Checkout | Checkout without account | `/checkout` | Active |
| About | Platform information | `/about` | Active |
| Contact | Contact form | `/contact` | Planned |
| FAQ | Frequently asked questions | `/faq` | Planned |

## Conversion Points to Registered User

### High-Intent Conversion Triggers
1. **Checkout Flow**
   - Prompt: "Create an account to track your order and earn loyalty points"
   - Benefit highlight: Order history, faster future checkouts
   - Timing: After cart confirmation, before payment

2. **Wishlist Attempt**
   - Prompt: "Sign up to save items to your wishlist"
   - Show preview of wishlist feature
   - One-click signup option

3. **Review Submission**
   - Prompt: "Create an account to share your review"
   - Emphasize community contribution
   - Post-purchase email follow-up

### Low-Friction Conversion Opportunities
4. **Personalization Nudge**
   - After 3+ product views: "Get personalized recommendations"
   - Show sample of what recommendations look like
   - Progressive profiling approach

5. **Newsletter Signup**
   - Footer and exit-intent popup
   - "Get exclusive deals and new arrivals"
   - Email-first, account optional

6. **Social Login**
   - Prominent Google/Facebook login options
   - "Continue with..." for minimal friction
   - Auto-create account on first use

## Limitations

### Data Persistence
- Cart contents lost on session expiration (24 hours)
- No saved payment methods
- No saved shipping addresses
- No order history access
- Browse history not tracked for recommendations

### Feature Restrictions
- Cannot submit product reviews
- Cannot rate products or sellers
- Cannot save items to wishlist
- Cannot follow cooperatives or SEs
- Cannot access loyalty program
- Cannot receive personalized recommendations
- Cannot message sellers directly (form-based only)
- Cannot access MoroAcademy courses (browse catalog only)

### Checkout Limitations
- Must enter shipping information each time
- Must enter payment information each time
- Limited to credit card and COD payments
- No saved order templates
- No subscription or recurring orders

## Session Behavior

### Session Duration
- Active session: 24 hours of inactivity
- Cart persistence: Same as session
- Recently viewed: Stored in local storage (30 days)

### Tracking (Privacy-Compliant)
- Anonymous session ID for cart functionality
- Page views for analytics (aggregated only)
- No personal data collected without consent
- Cookie consent required for marketing cookies

## Pain Points

1. **Lost Cart Items**
   - Session expiration causes cart loss
   - No way to recover abandoned cart
   - Impact: Lost sales, frustrated users

2. **Repeated Information Entry**
   - Must re-enter shipping details every purchase
   - No saved payment methods
   - Impact: Higher checkout abandonment

3. **No Purchase History**
   - Cannot easily reorder previous purchases
   - No warranty/receipt access
   - Impact: Reduced repeat purchases

4. **Limited Engagement**
   - Cannot participate in community (reviews, Q&A)
   - Cannot follow favorite sellers
   - Impact: Lower platform stickiness

5. **No Personalization**
   - Generic homepage for all anonymous users
   - No relevant product suggestions
   - Impact: Lower conversion rates

## Improvement Opportunities

1. **Smart Cart Recovery**
   - Email capture at cart addition
   - Send cart recovery emails
   - Extend cart persistence with email link

2. **Progressive Profile Building**
   - Collect preferences through browse behavior
   - Offer personalization preview as conversion hook
   - Gradual data collection

3. **Guest Checkout Enhancement**
   - Post-purchase account creation prompt
   - Pre-fill account with checkout data
   - One-click account activation from order confirmation

4. **Social Proof for Conversion**
   - Show "X people bought this today"
   - Display reviews prominently to build trust
   - Highlight registered user benefits contextually

5. **Local Storage Optimization**
   - Persist more data in local storage
   - Sync to account on registration
   - Reduce friction of first-time user experience

## Success Metrics

### Engagement Metrics
- **Session Duration**: Average time spent on platform (target: 5+ minutes)
- **Pages per Session**: Number of pages viewed (target: 4+ pages)
- **Bounce Rate**: Single-page sessions (target: < 40%)
- **Product Views**: Average products viewed per session (target: 3+)

### Conversion Metrics
- **Guest Checkout Rate**: % completing purchase as guest (target: 60%+)
- **Cart Abandonment Rate**: % abandoning before checkout (target: < 70%)
- **Registration Conversion**: % converting to registered user (target: 15%+)
- **Newsletter Signup Rate**: % signing up for newsletter (target: 5%+)

### Quality Metrics
- **Search Success Rate**: % finding products via search (target: 80%+)
- **Zero Results Rate**: % searches with no results (target: < 5%)
- **Mobile Usability Score**: Google mobile-friendly score (target: 90+)

---

## Implementation Plan

### Access Control
- **No authentication required** - all routes are publicly accessible
- **Middleware**: `frontend/src/middleware.ts` - no auth guards for `(public)` routes
- **Session-based cart**: Use browser localStorage/sessionStorage for cart persistence
- **Cookie consent**: Implement cookie banner for analytics tracking compliance

### Priority Pages

#### P0 - Core Shopping Experience
| Page | Route | File Path |
|------|-------|-----------|
| Homepage | `/` | `frontend/src/app/(public)/page.tsx` |
| Product Catalog | `/products` | `frontend/src/app/(public)/products/page.tsx` |
| Product Detail | `/products/[id]` | `frontend/src/app/(public)/products/[id]/page.tsx` |
| Search Results | `/search` | `frontend/src/app/(public)/search/page.tsx` |
| Cart | `/cart` | `frontend/src/app/(public)/cart/page.tsx` |
| Guest Checkout | `/checkout` | `frontend/src/app/(public)/checkout/page.tsx` |

#### P1 - Discovery & Trust
| Page | Route | File Path |
|------|-------|-----------|
| Coop Directory | `/coops` | `frontend/src/app/(public)/coops/page.tsx` |
| SE Directory | `/social-enterprises` | `frontend/src/app/(public)/social-enterprises/page.tsx` |
| Coop Storefront | `/coop/[slug]` | `frontend/src/app/(storefront)/coop/[slug]/page.tsx` |
| SE Storefront | `/se/[slug]` | `frontend/src/app/(storefront)/se/[slug]/page.tsx` |
| Impact Stories | `/impact` | `frontend/src/app/(public)/impact/page.tsx` |
| Story Detail | `/impact/[slug]` | `frontend/src/app/(public)/impact/[slug]/page.tsx` |

#### P2 - Supporting Pages
| Page | Route | File Path |
|------|-------|-----------|
| About | `/about` | `frontend/src/app/(public)/about/page.tsx` |
| Contact | `/contact` | `frontend/src/app/(public)/contact/page.tsx` |
| FAQ | `/faq` | `frontend/src/app/(public)/faq/page.tsx` |
| Category Browse | `/products?category=[slug]` | Uses `/products` with query params |

### Role-Specific Components

| Component | Path | Purpose |
|-----------|------|---------|
| ProductCard | `frontend/src/components/products/product-card.tsx` | Product display in grids |
| ProductGrid | `frontend/src/components/products/product-grid.tsx` | Responsive product grid |
| ProductFilters | `frontend/src/components/products/product-filters.tsx` | Search filters sidebar |
| SearchBar | `frontend/src/components/search/search-bar.tsx` | Global search input |
| CartDrawer | `frontend/src/components/cart/cart-drawer.tsx` | Slide-out cart preview |
| CartItem | `frontend/src/components/cart/cart-item.tsx` | Individual cart line item |
| GuestCheckoutForm | `frontend/src/components/checkout/guest-checkout-form.tsx` | Checkout form for guests |
| StorefrontHeader | `frontend/src/components/storefront/storefront-header.tsx` | Coop/SE storefront banner |
| ImpactStoryCard | `frontend/src/components/impact/impact-story-card.tsx` | Story preview card |
| DirectoryCard | `frontend/src/components/directory/directory-card.tsx` | Coop/SE directory listing |
| ConversionPrompt | `frontend/src/components/auth/conversion-prompt.tsx` | Registration nudge modal |
| CookieConsent | `frontend/src/components/common/cookie-consent.tsx` | GDPR cookie banner |

### API Endpoints Required

| Endpoint | Method | Location | Purpose |
|----------|--------|----------|---------|
| `/api/products` | GET | `backend/apps/products/api.py` | List products with filters |
| `/api/products/{id}` | GET | `backend/apps/products/api.py` | Product detail |
| `/api/products/search` | GET | `backend/apps/products/api.py` | Full-text search |
| `/api/categories` | GET | `backend/apps/products/api.py` | Category list |
| `/api/tenants/coops` | GET | `backend/apps/tenant/api.py` | Coop directory listing |
| `/api/tenants/social-enterprises` | GET | `backend/apps/tenant/api.py` | SE directory listing |
| `/api/tenants/{slug}` | GET | `backend/apps/tenant/api.py` | Storefront data |
| `/api/tenants/{slug}/products` | GET | `backend/apps/tenant/api.py` | Storefront products |
| `/api/impact-stories` | GET | `backend/apps/content/api.py` | Impact stories list |
| `/api/impact-stories/{slug}` | GET | `backend/apps/content/api.py` | Single story detail |
| `/api/cart/guest` | POST | `backend/apps/orders/api.py` | Guest cart operations |
| `/api/checkout/guest` | POST | `backend/apps/orders/api.py` | Guest checkout submission |
| `/api/contact` | POST | `backend/apps/core/api.py` | Contact form submission |

### Implementation Sequence

#### Phase 1: Core Shopping (Week 1-2)
1. Homepage with featured products and categories
2. Product catalog with grid view and basic filters
3. Product detail page with images, description, pricing
4. Search functionality with results page
5. Session-based cart (localStorage)

#### Phase 2: Storefronts & Discovery (Week 3-4)
1. Coop directory listing page
2. SE directory listing page
3. Individual storefront pages (`/coop/[slug]`, `/se/[slug]`)
4. Storefront product listings
5. Category filtering on product pages

#### Phase 3: Checkout & Trust (Week 5-6)
1. Guest checkout flow (shipping, payment selection)
2. Order confirmation page
3. Impact stories listing and detail pages
4. About, Contact, FAQ pages

#### Phase 4: Conversion & Polish (Week 7-8)
1. Registration conversion prompts (at checkout, wishlist attempt)
2. Cookie consent banner
3. Social sharing functionality
4. Product comparison feature (P3)
5. Newsletter signup integration
6. SEO optimization (meta tags, structured data)

---

## Implementation Status

*Audited: December 30, 2025*

### Key Pages Status

| Page | Status | Path | Notes |
|------|--------|------|-------|
| Homepage | ✅ Implemented | `frontend/src/app/(public)/page.tsx` | Active with featured products |
| Product Catalog | ✅ Implemented | `frontend/src/app/(public)/marketplace/browse/page.tsx` | Route is `/marketplace/browse` |
| Product Detail | ✅ Implemented | `frontend/src/app/(public)/marketplace/products/[slug]/page.tsx` | Using slug instead of id |
| Search Results | ❌ Not Found | - | No dedicated `/search` page found |
| Cart | ✅ Implemented | `frontend/src/app/(public)/marketplace/cart/page.tsx` | Under marketplace route |
| Guest Checkout | ✅ Implemented | `frontend/src/app/(public)/marketplace/checkout/page.tsx` | Under marketplace route |
| Coop Directory | ✅ Implemented | `frontend/src/app/(public)/cooperatives/browse/page.tsx` | Route is `/cooperatives/browse` |
| SE Directory | ✅ Implemented | `frontend/src/app/(public)/social-enterprises/browse/page.tsx` | Route is `/social-enterprises/browse` |
| Coop Storefront | ✅ Implemented | `frontend/src/app/(coop)/coop/[shortname]/page.tsx` | Uses `shortname` param |
| SE Storefront | ✅ Implemented | `frontend/src/app/(se)/se/[shortname]/page.tsx` | Uses `shortname` param |
| Impact Stories | ❌ Not Found | - | No `/impact` public page found |
| Story Detail | ❌ Not Found | - | No `/impact/[slug]` page found |
| About | ❌ Not Found | - | No `/about` page found |
| Contact | ❌ Not Found | - | No `/contact` page found |
| FAQ | ❌ Not Found | - | No `/faq` page found |
| Login | ✅ Implemented | `frontend/src/app/(public)/login/page.tsx` | Public login page |
| Register | ✅ Implemented | `frontend/src/app/(public)/register/page.tsx` | Public registration page |
| Training Browse | ✅ Implemented | `frontend/src/app/(public)/training/page.tsx` | MoroAcademy catalog |

### Storefront Pages Status

| Page | Status | Path | Notes |
|------|--------|------|-------|
| Coop Storefront Home | ✅ Implemented | `frontend/src/app/(coop)/coop/[shortname]/page.tsx` | Main storefront |
| Coop Shop | ✅ Implemented | `frontend/src/app/(coop)/coop/[shortname]/shop/page.tsx` | Product listing |
| Coop Product Detail | ✅ Implemented | `frontend/src/app/(coop)/coop/[shortname]/product/[id]/page.tsx` | Single product |
| Coop Cart | ✅ Implemented | `frontend/src/app/(coop)/coop/[shortname]/cart/page.tsx` | Storefront cart |
| Coop Checkout | ✅ Implemented | `frontend/src/app/(coop)/coop/[shortname]/checkout/page.tsx` | Storefront checkout |
| Coop Business Info | ✅ Implemented | `frontend/src/app/(coop)/coop/[shortname]/business/page.tsx` | About the coop |
| Coop Impact | ✅ Implemented | `frontend/src/app/(coop)/coop/[shortname]/impact/page.tsx` | Impact stories |
| SE Storefront Home | ✅ Implemented | `frontend/src/app/(se)/se/[shortname]/page.tsx` | Main storefront |
| SE Shop | ✅ Implemented | `frontend/src/app/(se)/se/[shortname]/shop/page.tsx` | Product listing |
| SE Product Detail | ✅ Implemented | `frontend/src/app/(se)/se/[shortname]/product/[id]/page.tsx` | Single product |
| SE Cart | ✅ Implemented | `frontend/src/app/(se)/se/[shortname]/cart/page.tsx` | Storefront cart |
| SE Checkout | ✅ Implemented | `frontend/src/app/(se)/se/[shortname]/checkout/page.tsx` | Storefront checkout |
| SE Business Info | ✅ Implemented | `frontend/src/app/(se)/se/[shortname]/business/page.tsx` | About the SE |
| SE Impact | ✅ Implemented | `frontend/src/app/(se)/se/[shortname]/impact/page.tsx` | Impact stories |

### API Endpoints Status

| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| Products List | ✅ Implemented | `/public/products` | With filters |
| Product Detail | ✅ Implemented | `/public/products/{id}` | Single product |
| Categories | ✅ Implemented | `/public/categories` | Category list |
| Cooperatives List | ✅ Implemented | `/public/cooperatives` | Directory listing |
| Social Enterprises List | ✅ Implemented | `/public/social-enterprises` | Directory listing |
| Impact Stories | ✅ Implemented | `/public/impact-stories` | Stories list |
| Orders (Guest) | ✅ Implemented | `/public/orders` | Guest checkout |
| Reviews | ✅ Implemented | `/public/reviews` | Product reviews |
| Stats | ✅ Implemented | `/public/stats` | Platform statistics |
| Search | 🚧 Partial | - | Integrated with products endpoint |
| Contact Form | ❌ Not Found | - | No contact endpoint |

### Overall Progress

- **Pages**: 12/19 implemented (63%)
- **Storefront Pages**: 14/14 implemented (100%)
- **APIs**: 9/11 implemented (82%)

### Notes

1. **Route Structure Differences**: Actual routes differ from planned (`/marketplace/browse` vs `/products`)
2. **Missing Public Pages**: About, Contact, FAQ, Impact Stories, Search results pages not found
3. **Storefronts Complete**: Both coop and SE storefronts are fully implemented
4. **Search Functionality**: No dedicated search page; search likely integrated into browse pages
