# Consumer - MoroNegosyo

## Overview
Consumers are registered users who shop on MoroNegosyo for products from Bangsamoro cooperatives and social enterprises. They have full e-commerce capabilities including order management, saved preferences, loyalty points, and community participation through reviews. Consumers may also have multi-role potential, as they can later apply to become cooperative or SE managers.

## Role Definition
**Type**: Authenticated User
**Portal Access**: Public Portal (`/`), Personal Account Pages
**Authentication**: Email/Password or Social Login (Google, Facebook)

## Capabilities

### Core Capabilities
| Capability | Description | Priority |
|------------|-------------|----------|
| Full E-commerce | Complete purchase flow with saved data | P0 |
| Order Management | View, track, and manage orders | P0 |
| Profile Management | Update personal info, preferences | P0 |
| Address Book | Save multiple shipping addresses | P0 |
| Wishlist | Save products for later | P1 |
| Order History | Access all past orders and receipts | P1 |
| Submit Reviews | Rate and review purchased products | P1 |
| Loyalty Points | Earn and redeem reward points | P1 |
| Follow Sellers | Get updates from favorite coops/SEs | P2 |
| Saved Payment Methods | Store payment info securely | P2 |
| Reorder | Quick reorder from past purchases | P2 |
| Notifications | Order updates, promotions, followed seller news | P2 |
| Ask Questions | Q&A on product pages | P3 |

### Feature Access Matrix
| Feature | Access Level | Notes |
|---------|--------------|-------|
| Product Catalog | Full | All products visible |
| Product Search | Full | Plus personalized suggestions |
| Storefronts | Full | Can follow and get updates |
| Shopping Cart | Full | Persistent across devices |
| Wishlist | Full | Unlimited items, shareable |
| Order History | Full | All orders, downloadable receipts |
| Reviews/Ratings | Full | Can submit, edit, delete own reviews |
| Checkout | Full | Saved addresses, payment methods |
| Saved Addresses | Full | Multiple addresses supported |
| Loyalty Points | Full | Earn, view balance, redeem |
| Personalization | Full | Based on history and preferences |
| MoroAcademy | Full | Free and paid courses access |
| Coop/SE Portal | None | Requires tenant role |
| Admin Portal | None | Requires staff role |

## User Journey Entry Points

1. **Direct Login**
   - User logs in via header login button
   - Redirected to homepage or intended destination
   - Path: Login > Homepage > Browse > Purchase

2. **Email Campaign**
   - User clicks promotional email link
   - Auto-logged in via token, lands on promoted product
   - Path: Email > Product > Purchase

3. **Order Tracking**
   - User clicks tracking link from order email
   - Lands on order detail page
   - Path: Email > Order Detail > Related Products

4. **Reorder Flow**
   - User receives "Time to reorder?" notification
   - Clicks through to pre-filled cart
   - Path: Notification > Cart > Checkout

5. **Review Request**
   - User receives post-purchase review request
   - Lands on product with review form open
   - Path: Email > Product > Submit Review > Browse

6. **Loyalty Redemption**
   - User receives "Points expiring" notification
   - Lands on loyalty dashboard
   - Path: Notification > Loyalty > Redeem > Shop

## Key Pages

| Page | Purpose | Route | Implementation |
|------|---------|-------|----------------|
| Account Dashboard | Overview of account | `/account` | Active |
| Profile Settings | Edit personal info | `/account/profile` | Active |
| Address Book | Manage addresses | `/account/addresses` | Planned |
| Order History | List all orders | `/account/orders` | Active |
| Order Detail | Single order info | `/account/orders/[id]` | Active |
| Wishlist | Saved products | `/account/wishlist` | Planned |
| Reviews | My reviews | `/account/reviews` | Planned |
| Loyalty Points | Points balance, history | `/account/loyalty` | Planned |
| Notifications | Notification center | `/account/notifications` | Planned |
| Payment Methods | Saved payments | `/account/payments` | Planned |
| Security | Password, 2FA | `/account/security` | Planned |
| Preferences | Notification, privacy settings | `/account/preferences` | Planned |
| Following | Followed coops/SEs | `/account/following` | Planned |
| My MoroAcademy | Enrolled courses | `/academy/my-learning` | Active |

## Profile Management

### Personal Information
- Full name (required)
- Email address (required, verified)
- Phone number (optional, for SMS updates)
- Profile photo (optional)
- Birthday (optional, for birthday rewards)
- Gender (optional)
- Preferred language (English, Filipino, Arabic)

### Address Management
- Multiple saved addresses (no limit)
- Default shipping address
- Default billing address
- Address labels (Home, Work, etc.)
- Philippine address format support
- Barangay-level specificity

### Communication Preferences
- Order updates (email/SMS/push)
- Promotional emails
- Followed seller updates
- Price drop alerts
- Back in stock notifications
- Review reminders

## Loyalty Program

### Point Earning
| Action | Points Earned |
|--------|---------------|
| Purchase | 1 point per PHP 100 spent |
| First Purchase | 100 bonus points |
| Submit Review | 20 points per review |
| Refer Friend | 200 points per successful referral |
| Birthday | 50 bonus points |
| Complete Profile | 50 points |

### Point Redemption
| Tier | Points Required | Discount Value |
|------|-----------------|----------------|
| Bronze | 500 points | PHP 50 off |
| Silver | 1,000 points | PHP 100 off |
| Gold | 2,500 points | PHP 250 off |
| Platinum | 5,000 points | PHP 500 off |

### Loyalty Tiers
| Tier | Annual Spend | Benefits |
|------|--------------|----------|
| Member | PHP 0+ | Base earning rate |
| Silver | PHP 5,000+ | 1.25x earning rate, early sale access |
| Gold | PHP 15,000+ | 1.5x earning rate, free shipping (1/month) |
| Platinum | PHP 50,000+ | 2x earning rate, free shipping, priority support |

## Order Management

### Order States
| State | Description | Consumer Actions |
|-------|-------------|------------------|
| Pending | Awaiting payment confirmation | Cancel, Retry payment |
| Confirmed | Payment received, processing | Cancel (limited time) |
| Preparing | Seller preparing order | View status |
| Shipped | In transit | Track shipment |
| Delivered | Order received | Confirm receipt, Review |
| Completed | Order finalized | Review, Reorder |
| Cancelled | Order cancelled | View reason |
| Refund Requested | Return/refund in process | Track refund |

### Order Features
- Real-time tracking integration
- Delivery photo proof
- Split shipments supported
- Order notes to seller
- Gift wrapping option
- Digital receipts (downloadable)
- Order invoice for business purchases

## Multi-Role Potential

### Role Progression Paths

**Path 1: Consumer to Coop Manager**
1. User is member of a registered cooperative
2. Applies via "Register Your Coop" flow
3. Submits required documents (CDA registration, etc.)
4. CSEA reviews and approves
5. User gains Coop Manager role
6. Retains Consumer role for personal shopping

**Path 2: Consumer to SE Manager**
1. User owns/manages a social enterprise
2. Applies via "Register Your SE" flow
3. Submits required documents (SEC/DTI, impact proof)
4. CSEA reviews and approves
5. User gains SE Manager role
6. Retains Consumer role for personal shopping

### Role Coexistence
- Users can hold multiple roles simultaneously
- Role context switch via account menu
- Each role has separate dashboard
- Unified notifications across roles
- Single login for all roles

## Role Progression

**From**: Anonymous User
**To**:
- Coop Manager (via coop registration)
- SE Manager (via SE registration)
- CSEA Staff (via employment/invitation)

**Requirements to Become Consumer**:
- Valid email address
- Email verification
- Acceptance of Terms of Service
- Basic profile completion

## Pain Points

1. **Complex Checkout for First-Time**
   - Too many steps for returning users
   - Saved data not auto-applied
   - Impact: Cart abandonment

2. **Limited Payment Options**
   - No GCash/Maya integration yet
   - No installment options
   - Impact: Lost sales from unbanked users

3. **Order Tracking Gaps**
   - Inconsistent tracking updates
   - No unified tracking across sellers
   - Impact: Support inquiries, anxiety

4. **Review Process Friction**
   - Must navigate to product to review
   - No photo upload for reviews
   - Impact: Low review submission rate

5. **Loyalty Program Visibility**
   - Points balance not prominent
   - Redemption options unclear
   - Impact: Low engagement with program

6. **Mobile App Absence**
   - No native app experience
   - PWA has limitations
   - Impact: Lower engagement vs. competitors

## Improvement Opportunities

1. **One-Click Checkout**
   - For repeat purchases from same seller
   - Default everything for speed
   - Confirmation-only flow

2. **E-Wallet Integration**
   - GCash, Maya, GrabPay support
   - QR code payments
   - Wallet balance display

3. **Smart Reorder**
   - Subscription-style recurring orders
   - AI-suggested reorder timing
   - Pre-filled cart from patterns

4. **Enhanced Reviews**
   - Photo and video reviews
   - Review from order history page
   - Incentivized review program

5. **Loyalty Gamification**
   - Progress bars toward next tier
   - Monthly challenges for bonus points
   - Point multiplier events

6. **Social Features**
   - Share wishlist with friends
   - Social shopping lists
   - Gift recommendations

7. **Mobile App Development**
   - Native iOS/Android apps
   - Push notifications
   - Offline catalog browsing

## Success Metrics

### Engagement Metrics
- **Monthly Active Users**: Unique logged-in users per month
- **Session Frequency**: Average sessions per user per month (target: 4+)
- **Wishlist Items**: Average items in wishlist (target: 5+)
- **Followed Sellers**: Average sellers followed (target: 2+)

### Transaction Metrics
- **Repeat Purchase Rate**: % making 2+ purchases (target: 40%+)
- **Average Order Value**: Mean order value (target: PHP 500+)
- **Customer Lifetime Value**: Total revenue per customer (target: PHP 5,000+)
- **Checkout Conversion**: Cart to purchase rate (target: 75%+)

### Loyalty Metrics
- **Points Earned per User**: Average monthly points earned
- **Redemption Rate**: % of points redeemed (target: 60%+)
- **Tier Distribution**: % at each loyalty tier
- **Tier Upgrade Rate**: % moving up tiers annually

### Community Metrics
- **Review Submission Rate**: % of orders reviewed (target: 20%+)
- **Review Helpfulness**: % of reviews marked helpful
- **Q&A Participation**: Questions asked/answered per user
- **Referral Rate**: % referring new users (target: 10%+)

---

## Implementation Plan

### Access Control
- **Authentication required**: All `/account/*` routes require authenticated user
- **Middleware**: `frontend/src/middleware.ts` - auth guards for `(account)` route group
- **Session management**: JWT tokens with refresh, stored in httpOnly cookies
- **Permission checks**: User role must include "consumer" or higher
- **Cart sync**: On login, merge session cart with persisted user cart

```typescript
// frontend/src/middleware.ts
const protectedRoutes = ['/account', '/checkout/authenticated'];
// Redirect to /login if not authenticated
```

### Priority Pages

#### P0 - Core Account & Orders
| Page | Route | File Path |
|------|-------|-----------|
| Account Dashboard | `/account` | `frontend/src/app/(account)/account/page.tsx` |
| Profile Settings | `/account/profile` | `frontend/src/app/(account)/account/profile/page.tsx` |
| Order History | `/account/orders` | `frontend/src/app/(account)/account/orders/page.tsx` |
| Order Detail | `/account/orders/[id]` | `frontend/src/app/(account)/account/orders/[id]/page.tsx` |
| Authenticated Checkout | `/checkout` | `frontend/src/app/(public)/checkout/page.tsx` (enhanced) |

#### P1 - Personalization & Loyalty
| Page | Route | File Path |
|------|-------|-----------|
| Address Book | `/account/addresses` | `frontend/src/app/(account)/account/addresses/page.tsx` |
| Wishlist | `/account/wishlist` | `frontend/src/app/(account)/account/wishlist/page.tsx` |
| Loyalty Points | `/account/loyalty` | `frontend/src/app/(account)/account/loyalty/page.tsx` |
| My Reviews | `/account/reviews` | `frontend/src/app/(account)/account/reviews/page.tsx` |

#### P2 - Engagement & Settings
| Page | Route | File Path |
|------|-------|-----------|
| Following | `/account/following` | `frontend/src/app/(account)/account/following/page.tsx` |
| Notifications | `/account/notifications` | `frontend/src/app/(account)/account/notifications/page.tsx` |
| Preferences | `/account/preferences` | `frontend/src/app/(account)/account/preferences/page.tsx` |
| Security | `/account/security` | `frontend/src/app/(account)/account/security/page.tsx` |
| Payment Methods | `/account/payments` | `frontend/src/app/(account)/account/payments/page.tsx` |

#### P3 - MoroAcademy Integration
| Page | Route | File Path |
|------|-------|-----------|
| My Learning | `/academy/my-learning` | `frontend/src/app/(academy)/academy/my-learning/page.tsx` |

### Role-Specific Components

| Component | Path | Purpose |
|-----------|------|---------|
| AccountSidebar | `frontend/src/components/account/account-sidebar.tsx` | Account navigation menu |
| OrderCard | `frontend/src/components/orders/order-card.tsx` | Order summary card |
| OrderTimeline | `frontend/src/components/orders/order-timeline.tsx` | Order status timeline |
| OrderTracking | `frontend/src/components/orders/order-tracking.tsx` | Shipment tracking display |
| AddressCard | `frontend/src/components/account/address-card.tsx` | Saved address display |
| AddressForm | `frontend/src/components/account/address-form.tsx` | Add/edit address form |
| WishlistButton | `frontend/src/components/products/wishlist-button.tsx` | Add to wishlist toggle |
| WishlistGrid | `frontend/src/components/account/wishlist-grid.tsx` | Wishlist product grid |
| LoyaltyCard | `frontend/src/components/loyalty/loyalty-card.tsx` | Points balance display |
| LoyaltyTierBadge | `frontend/src/components/loyalty/loyalty-tier-badge.tsx` | User tier indicator |
| PointsHistory | `frontend/src/components/loyalty/points-history.tsx` | Points transaction log |
| ReviewForm | `frontend/src/components/reviews/review-form.tsx` | Submit/edit review |
| ReviewCard | `frontend/src/components/reviews/review-card.tsx` | Display user review |
| FollowButton | `frontend/src/components/storefront/follow-button.tsx` | Follow coop/SE toggle |
| NotificationItem | `frontend/src/components/notifications/notification-item.tsx` | Single notification |
| PreferencesForm | `frontend/src/components/account/preferences-form.tsx` | Notification settings |
| ReorderButton | `frontend/src/components/orders/reorder-button.tsx` | Quick reorder action |

### API Endpoints Required

| Endpoint | Method | Location | Purpose |
|----------|--------|----------|---------|
| `/api/auth/login` | POST | `backend/apps/users/api.py` | User authentication |
| `/api/auth/register` | POST | `backend/apps/users/api.py` | User registration |
| `/api/auth/refresh` | POST | `backend/apps/users/api.py` | Token refresh |
| `/api/users/me` | GET/PATCH | `backend/apps/users/api.py` | Profile get/update |
| `/api/users/me/addresses` | GET/POST | `backend/apps/users/api.py` | Address management |
| `/api/users/me/addresses/{id}` | PATCH/DELETE | `backend/apps/users/api.py` | Single address ops |
| `/api/orders` | GET/POST | `backend/apps/orders/api.py` | Order list/create |
| `/api/orders/{id}` | GET | `backend/apps/orders/api.py` | Order detail |
| `/api/orders/{id}/tracking` | GET | `backend/apps/orders/api.py` | Tracking info |
| `/api/orders/{id}/reorder` | POST | `backend/apps/orders/api.py` | Create reorder cart |
| `/api/wishlist` | GET/POST/DELETE | `backend/apps/products/api.py` | Wishlist operations |
| `/api/reviews` | GET/POST | `backend/apps/reviews/api.py` | User reviews |
| `/api/reviews/{id}` | PATCH/DELETE | `backend/apps/reviews/api.py` | Review update/delete |
| `/api/loyalty/balance` | GET | `backend/apps/loyalty/api.py` | Points balance |
| `/api/loyalty/history` | GET | `backend/apps/loyalty/api.py` | Points history |
| `/api/loyalty/redeem` | POST | `backend/apps/loyalty/api.py` | Redeem points |
| `/api/following` | GET/POST/DELETE | `backend/apps/tenant/api.py` | Follow/unfollow coops/SEs |
| `/api/notifications` | GET/PATCH | `backend/apps/notifications/api.py` | Notification management |
| `/api/preferences` | GET/PATCH | `backend/apps/users/api.py` | User preferences |
| `/api/cart` | GET/POST/PATCH/DELETE | `backend/apps/orders/api.py` | Authenticated cart |
| `/api/checkout` | POST | `backend/apps/orders/api.py` | Authenticated checkout |

### Implementation Sequence

#### Phase 1: Authentication & Profile (Week 1-2)
1. Login/Register pages with email + social auth (Google)
2. JWT authentication flow with refresh tokens
3. Account dashboard with overview widgets
4. Profile settings page (name, email, phone, photo)
5. Session cart to user cart sync on login

#### Phase 2: Orders & Checkout (Week 3-4)
1. Enhanced checkout with saved addresses
2. Order history listing with filters (status, date)
3. Order detail with timeline and tracking
4. Digital receipt download
5. Reorder functionality

#### Phase 3: Wishlist & Reviews (Week 5-6)
1. Wishlist functionality (add/remove/list)
2. Wishlist page with product grid
3. Review submission on product pages
4. My reviews page with edit/delete
5. Review from order history

#### Phase 4: Loyalty Program (Week 7-8)
1. Loyalty dashboard with balance and tier
2. Points earning on purchases
3. Points history and transaction log
4. Point redemption at checkout
5. Tier progress visualization

#### Phase 5: Engagement Features (Week 9-10)
1. Follow coop/SE functionality
2. Following feed/page
3. Notification center
4. Notification preferences
5. Communication preferences (email/SMS/push)

#### Phase 6: Advanced Features (Week 11-12)
1. Payment methods management
2. Security settings (password change, 2FA)
3. Address book with multiple addresses
4. One-click checkout (default everything)
5. MoroAcademy integration (enrolled courses)

---

## Implementation Status

*Audited: December 30, 2025*

### Key Pages Status

| Page | Status | Path | Notes |
|------|--------|------|-------|
| Account Dashboard | ✅ Implemented | `frontend/src/app/(account)/account/page.tsx` | Overview page |
| Profile Settings | ✅ Implemented | `frontend/src/app/(account)/profile/page.tsx` | Route is `/profile` not `/account/profile` |
| Address Book | ✅ Implemented | `frontend/src/app/(account)/addresses/page.tsx` | Route is `/addresses` |
| Order History | ✅ Implemented | `frontend/src/app/(account)/orders/page.tsx` | Route is `/orders` |
| Order Detail | ✅ Implemented | `frontend/src/app/(account)/orders/[id]/page.tsx` | Single order view |
| Wishlist/Saved | ✅ Implemented | `frontend/src/app/(account)/saved/page.tsx` | Route is `/saved` |
| My Reviews | ❌ Not Found | - | No `/account/reviews` page |
| Loyalty Points | ❌ Not Found | - | No loyalty program pages |
| Notifications | ❌ Not Found | - | No notification center |
| Payment Methods | ❌ Not Found | - | No saved payments page |
| Security | ❌ Not Found | - | No security settings page |
| Preferences | ❌ Not Found | - | No preferences page |
| Following | ❌ Not Found | - | No following page |
| Membership | ✅ Implemented | `frontend/src/app/(account)/membership/page.tsx` | Coop/SE membership |
| Training | ✅ Implemented | `frontend/src/app/(account)/training/page.tsx` | MoroAcademy courses |
| Become Manager | ✅ Implemented | `frontend/src/app/(account)/become-manager/page.tsx` | Role upgrade flow |
| Manager Application | ✅ Implemented | `frontend/src/app/(account)/manager-application/page.tsx` | Application status |

### API Endpoints Status

| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| Login | ✅ Implemented | `/accounts/login` | Authentication |
| Register | ✅ Implemented | `/accounts/register` | User registration |
| Get Profile | ✅ Implemented | `/accounts/me` | Current user |
| Update Profile | ✅ Implemented | `/accounts/profile` | Profile updates |
| Consumer Dashboard Stats | ✅ Implemented | `/public/consumer/dashboard/stats` | Dashboard metrics |
| Consumer Orders | ✅ Implemented | `/public/consumer/orders` | Order history |
| Saved Items | ✅ Implemented | `/public/consumer/saved-items` | Wishlist |
| Memberships | ✅ Implemented | `/public/consumer/memberships` | Coop/SE memberships |
| Consumer Training | ✅ Implemented | `/public/consumer/training` | Enrolled courses |
| Manager Application | ✅ Implemented | `/accounts/manager-application` | Apply for manager role |
| Addresses | 🚧 Partial | - | Not found in audit; may be under profile |
| Reviews | ❌ Not Found | - | No user reviews endpoint |
| Loyalty Balance | ❌ Not Found | - | No loyalty program API |
| Loyalty History | ❌ Not Found | - | No loyalty program API |
| Following | ❌ Not Found | - | No following/unfollow API |
| Notifications | ❌ Not Found | - | No notifications API |
| Preferences | ❌ Not Found | - | No preferences API |
| Cart (Authenticated) | ❌ Not Found | - | May use session-based cart |

### Overall Progress

- **Pages**: 10/17 implemented (59%)
- **APIs**: 10/18 implemented (56%)

### Notes

1. **Route Structure**: Account pages use flat routes (`/profile`, `/orders`) instead of nested (`/account/profile`)
2. **Missing Features**: Loyalty program, notifications, preferences, reviews management not implemented
3. **Manager Flow**: Complete flow for consumers to apply as coop/SE managers
4. **Training Integration**: MoroAcademy integration exists for enrolled courses
5. **No Loyalty Program**: Points, tiers, and redemption features not yet implemented
