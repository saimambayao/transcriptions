# Registration to Profile Management Journey - MoroNegosyo

## Overview

This journey maps the complete account lifecycle for consumers on MoroNegosyo, from first-time registration through ongoing profile management. The journey emphasizes progressive profile building, minimal friction during registration, and value delivery before requiring account creation.

## Persona

**Name**: Juan Dela Cruz
**Age**: 28
**Role**: First-time Online Shopper
**Location**: Marawi City, Lanao del Sur
**Context**: Juan is a young professional who has recently started ordering products online. He's comfortable with social media and mobile apps but is cautious about creating accounts on unfamiliar websites. He values convenience and is interested in supporting local Bangsamoro businesses.

**Goals**:
- Create an account quickly without too much personal information required
- Manage his delivery addresses for home and office
- Track his orders and order history easily
- Save favorite products for future purchases
- Earn and track loyalty rewards

**Tech Comfort**: High - daily smartphone user, uses multiple apps
**Connectivity**: Good 4G/LTE in urban area
**Privacy Concern**: Moderate - wants to know why data is needed

---

## Journey Map

### Stage 1: Pre-Registration (Guest Browsing)

**User Goal**: Explore the platform before committing to an account

**Actions**:
1. Juan browses products without logging in
2. Adds items to cart as a guest
3. Saves items to a local wishlist (cookie-based)
4. Attempts to checkout
5. Is prompted to create account or continue as guest

**Touchpoints**:
- Guest browsing experience
- Guest cart functionality
- "Save for Later" prompt
- Checkout entry point
- Account creation prompt

**Emotions**: Curious, non-committal, evaluating the platform

**Pain Points**:
- Losing cart items when closing browser
- Can't access wishlist across devices
- Forced registration feels pushy
- Unclear benefits of having an account

**Opportunities**:
- Persist guest cart via local storage (longer duration)
- Show clear benefits of account creation at key moments
- Allow guest checkout but highlight account benefits
- Offer social login for faster registration

**Design Requirements**:
```
- Guest can browse, add to cart, and checkout without account
- Cart persists for 30 days via local storage
- Benefits banner: "Create account to track orders, save favorites, earn rewards"
- Registration prompt appears at checkout, not before
- "Continue as Guest" is a visible, valid option
```

---

### Stage 2: Account Registration

**User Goal**: Create an account quickly with minimal friction

**Actions**:
1. Juan chooses to create an account (from checkout or header)
2. Sees registration options: email or social login
3. Selects "Sign up with Google" for speed
4. Reviews and accepts permissions
5. Is redirected back with account created
6. OR: Fills in email registration form
7. Creates password meeting requirements
8. Submits and sees success confirmation

**Touchpoints**:
- Registration page/modal
- Social login buttons (Google, Facebook)
- Email registration form
- Password strength indicator
- Terms acceptance checkbox
- Success confirmation screen

**Emotions**: Slightly reluctant, wanting speed, cautious about privacy

**Pain Points**:
- Long registration forms cause abandonment
- Password requirements unclear until error
- Forced email verification interrupts flow
- Social login permissions seem invasive

**Opportunities**:
- Minimize required fields to essential only
- Show password requirements inline as user types
- Delay email verification until after first purchase
- Clearly explain social login data access
- Transfer guest cart to new account automatically

**Design Requirements**:
```
- Required fields only: Name, Email, Password (for email signup)
- Social login options: Google (primary), Facebook (secondary)
- Password requirements shown inline: 8+ chars, 1 number, 1 uppercase
- Password visibility toggle icon
- Terms link opens in new tab (doesn't lose form data)
- Guest cart automatically merges with new account
- No email verification required for first purchase
```

### Registration Form Pattern

```
[Social Login Section]
- Continue with Google (primary, full-width button)
- Continue with Facebook (secondary, full-width button)

[Divider]
- "or create account with email"

[Email Registration Form]
- Full Name* [_______________]
- Email Address* [_______________]
- Password* [_______________] [eye icon]
  - Requirements shown inline as checkmarks
- [ ] I agree to Terms of Service and Privacy Policy
- [Create Account] button

[Footer]
- Already have an account? Sign in
```

---

### Stage 3: Email Verification (Deferred)

**User Goal**: Verify my email when convenient without blocking my activity

**Actions**:
1. Juan completes first purchase successfully
2. Receives email with verification link
3. Sees in-app banner prompting verification
4. Clicks verification link when ready
5. Email is verified, banner dismissed
6. Full account features unlocked

**Touchpoints**:
- Verification email
- In-app verification banner (non-blocking)
- Verification success page
- Feature unlock notifications

**Emotions**: Slightly annoyed by reminders, but understands necessity

**Pain Points**:
- Verification email goes to spam
- Link expires too quickly
- Can't resend verification easily
- Blocked from critical features before verifying

**Opportunities**:
- Allow purchases without verification (limited to 3)
- Make banner dismissible but persistent
- Easy resend with cooldown
- Clear explanation of what's unlocked after verification

**Design Requirements**:
```
- User can place up to 3 orders before verification required
- Banner: "Verify your email to unlock all features" [Verify Now] [X]
- Banner persists across sessions until verified
- Verification link valid for 7 days
- "Resend Email" available with 60-second cooldown
- Email includes: verification link, 6-digit code option
- Code entry available for users who can't click links
```

---

### Stage 4: Profile Setup (Progressive)

**User Goal**: Complete my profile at my own pace with clear benefits

**Actions**:
1. Juan accesses account/profile section
2. Sees profile completion meter (e.g., 40% complete)
3. Views suggested next steps with incentives
4. Adds phone number (for order updates)
5. Uploads profile photo (optional)
6. Completes profile to unlock rewards

**Touchpoints**:
- Account dashboard
- Profile completion progress bar
- Profile edit form
- Incentive notifications
- Reward unlock confirmations

**Emotions**: Willing if value is clear, resistant to unnecessary data collection

**Pain Points**:
- Unclear why information is needed
- No benefit to completing profile
- Too many required fields
- Photo upload is cumbersome

**Opportunities**:
- Tie profile completion to tangible rewards (discount, points)
- Explain data use next to each field
- Make most fields optional
- Allow camera capture or file upload for photo

**Design Requirements**:
```
Profile Completion Rewards:
- 50% complete: Unlock order tracking SMS
- 75% complete: 50 bonus loyalty points
- 100% complete: PHP 50 discount on next order

Fields by Priority:
- Required: Name, Email (from registration)
- Recommended: Phone (for SMS updates)
- Optional: Profile photo, Birthday, Gender

Each field shows: why it's needed, what it unlocks
"Add phone number to receive SMS order updates"
```

### Profile Dashboard Layout

```
[Profile Header]
- Photo/Avatar | Name | Edit Profile button
- Verified badge (if email verified)
- Member since date

[Profile Completion Card]
- Progress bar: 60% complete
- "Complete your profile for rewards"
- Next step: "Add phone number" [Add]

[Quick Stats]
- Orders: 5 | Wishlist: 12 | Reviews: 3

[Account Navigation]
- My Orders
- Addresses
- Wishlist
- Loyalty Points
- Reviews
- Settings
```

---

### Stage 5: Address Management

**User Goal**: Save and manage multiple delivery addresses for convenience

**Actions**:
1. Juan navigates to Address section
2. Sees existing addresses (if any)
3. Clicks "Add New Address"
4. Fills in address form with BARMM locations
5. Labels address (Home/Office/Other)
6. Sets as default address
7. Saves and returns to address list
8. Can edit or delete addresses later

**Touchpoints**:
- Address list page
- Add/Edit address form
- Address label selector
- Default address toggle
- Delete confirmation dialog

**Emotions**: Focused, wanting organization, slightly tedious task

**Pain Points**:
- Address form doesn't know BARMM geography
- Can't easily duplicate/modify existing address
- Unclear which address is default
- Deleting address is scary (what if needed later?)

**Opportunities**:
- Pre-populate BARMM provinces, municipalities, barangays
- "Copy from existing" option for similar addresses
- Clear default indicator with easy change
- Soft delete: "Archived addresses" recoverable

**Design Requirements**:
```
Address Form Fields:
- Label: [Home] [Office] [Other: ___]
- Full Name*
- Phone Number*
- Province* (dropdown: BARMM provinces)
- Municipality* (cascading dropdown)
- Barangay* (cascading dropdown)
- Street Address / Building*
- Landmark (optional)
- Delivery Instructions (optional)
- [ ] Set as default address

Address Card Display:
- Label badge (Home/Office)
- Default indicator
- Full address formatted
- Phone number
- [Edit] [Delete] actions
```

---

### Stage 6: Wishlist Management

**User Goal**: Save and organize products I want to buy later

**Actions**:
1. Juan browses products and clicks heart icon
2. Receives confirmation toast
3. Navigates to Wishlist from account
4. Views saved products with current prices
5. Sees "Price Drop" notification on discounted items
6. Moves items to cart directly
7. Removes items no longer interested in
8. Shares wishlist with family (optional)

**Touchpoints**:
- Heart icon on product cards/pages
- Add to wishlist confirmation
- Wishlist page
- Price change notifications
- Move to cart action
- Share wishlist feature

**Emotions**: Collecting, anticipating, bargain-hunting

**Pain Points**:
- Wishlist gets cluttered over time
- No notification when prices drop
- Items go out of stock without warning
- Can't organize into categories

**Opportunities**:
- Price drop alerts via email/push
- "Back in Stock" notifications
- Wishlist organization (folders/categories)
- Shareable wishlist for gifts

**Design Requirements**:
```
Wishlist Features:
- Grid view of saved products (consistent with catalog)
- Current price with "Was PHP X" if price dropped
- "Price Drop!" badge on discounted items
- Stock status indicator
- [Add to Cart] quick action
- [Remove] icon action

Wishlist Organization:
- All Items (default)
- Create folder option: "Birthday", "For the Store", etc.
- Move item between folders

Notifications (opt-in):
- [ ] Email me when prices drop
- [ ] Notify when items back in stock
```

---

### Stage 7: Order History & Tracking

**User Goal**: View my past orders and track current ones

**Actions**:
1. Juan navigates to "My Orders" section
2. Sees list of orders with status indicators
3. Filters by status (All/Processing/Shipped/Delivered)
4. Clicks on specific order for details
5. Views order timeline and tracking
6. Downloads invoice/receipt
7. Initiates return/refund if needed
8. Reorders items from past order

**Touchpoints**:
- Order list page
- Order status badges
- Filter/search controls
- Order detail page
- Tracking timeline
- Invoice download
- Return/Refund initiation
- Reorder button

**Emotions**: Checking, following up, sometimes frustrated (if issues)

**Pain Points**:
- Can't find specific past order
- Tracking information is outdated
- No easy way to reorder same items
- Return process is unclear

**Opportunities**:
- Search orders by product name or order ID
- Real-time tracking integration
- One-click reorder for entire order
- Clear return/refund timeline

**Design Requirements**:
```
Order List Card:
- Order #12345 | Dec 15, 2025
- [Delivered] status badge
- Item thumbnails (up to 3 + "+X more")
- Total: PHP 1,250
- [View Details] [Reorder] buttons

Order Detail Page:
- Order header with status
- Tracking timeline (visual steps)
- Items ordered (images, quantities, prices)
- Payment summary
- Delivery address
- Seller information
- [Download Invoice] [Contact Seller] [Request Return]

Reorder Flow:
- Click "Reorder" on past order
- Items added to cart (with stock check)
- Unavailable items flagged with alternatives
```

---

### Stage 8: Loyalty Points & Rewards

**User Goal**: Earn and redeem rewards for my purchases

**Actions**:
1. Juan sees loyalty points balance in dashboard
2. Navigates to Loyalty section
3. Views points earning history
4. Sees available rewards to redeem
5. Checks points expiry dates
6. Redeems points for discount voucher
7. Uses voucher on next purchase

**Touchpoints**:
- Points balance display (header/dashboard)
- Loyalty program page
- Points history timeline
- Rewards catalog
- Redemption flow
- Voucher application at checkout

**Emotions**: Rewarded, motivated to buy more, tracking progress

**Pain Points**:
- Unclear how points are earned
- Points expire without warning
- Redemption options are limited
- Voucher application confusing

**Opportunities**:
- Clear points earning rules displayed
- Expiry reminders 7 days before
- Variety of redemption options
- Auto-apply vouchers at checkout

**Design Requirements**:
```
Loyalty Dashboard:
- Current Balance: 1,250 points
- Points expiring soon: 100 (expires Dec 31)
- "Earn 10 points per PHP 100 spent"
- [View History] [Redeem Rewards]

Earning Rules:
- PHP 100 spent = 10 points
- First purchase = 50 bonus points
- Complete profile = 50 bonus points
- Leave review = 20 points
- Refer a friend = 100 points

Rewards Catalog:
- PHP 50 off (500 points)
- PHP 100 off (900 points)
- Free Shipping (300 points)
- Featured Product discount (varies)

Redemption Flow:
1. Select reward
2. Confirm redemption
3. Voucher added to "My Vouchers"
4. Auto-suggest at checkout
```

---

### Stage 9: Account Settings & Security

**User Goal**: Manage my account preferences and security settings

**Actions**:
1. Juan accesses Settings from account menu
2. Updates notification preferences
3. Changes password
4. Reviews login activity
5. Manages connected accounts (social logins)
6. Reviews privacy settings
7. Downloads account data (GDPR compliance)
8. Considers account deletion (last resort)

**Touchpoints**:
- Settings page
- Notification preferences toggles
- Password change form
- Login activity log
- Connected accounts management
- Privacy settings
- Data download request
- Account deletion flow

**Emotions**: Security-conscious, wanting control, sometimes frustrated

**Pain Points**:
- Too many notification types
- Password change requires re-login everywhere
- Can't see who has access to account
- Deleting account seems permanent and scary

**Opportunities**:
- Grouped notification settings
- Device management (see all logged-in devices)
- Clear privacy controls
- Account deletion grace period

**Design Requirements**:
```
Settings Sections:

[Notifications]
- Order updates: [Email] [SMS] [Push]
- Promotions: [Email] [Push]
- Price drop alerts: [Email] [Push]
- Newsletter: [Email]

[Security]
- Change password (link to form)
- Login activity (last 10 logins with device/location)
- Two-factor authentication (optional)
- Connected accounts: Google, Facebook

[Privacy]
- Data sharing preferences
- Marketing consent
- Download my data
- Delete my account

[Account Deletion]
- 30-day grace period to reactivate
- Clear explanation of what's deleted
- Confirm with password
```

---

## Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Registration Completion Rate | > 80% | Started / Completed |
| Social Login Adoption | > 50% | Login method tracking |
| Email Verification Rate | > 70% (7 days) | Verification funnel |
| Profile Completion Rate | > 60% | Profile field fill rate |
| Address Book Usage | > 40% have 2+ addresses | Account data |
| Wishlist Engagement | > 30% use wishlist | Feature tracking |
| Order History Access | > 60% visit post-purchase | Page analytics |
| Loyalty Redemption Rate | > 40% redeem points | Redemption tracking |
| Account Retention (90 days) | > 70% | Login activity |
| Account Deletion Rate | < 2% | Deletion requests |

---

## Implementation Status

| Feature | Status | Notes |
|---------|--------|-------|
| Email registration | TBD | Basic form needed |
| Social login (Google) | TBD | OAuth integration |
| Social login (Facebook) | TBD | OAuth integration |
| Email verification | TBD | Deferred pattern |
| Profile management | TBD | Progressive completion |
| Address management | TBD | BARMM geo data needed |
| Wishlist | TBD | Cart integration |
| Order history | TBD | Order tracking integration |
| Loyalty program | TBD | Points system design |
| Account settings | TBD | Notification system |
| Account deletion | TBD | Grace period logic |

---

## Recommendations

### Priority 1: Frictionless Registration
1. Implement social login (Google first, then Facebook) as primary option
2. Reduce email registration to 3 fields only
3. Allow purchases before email verification (up to 3)
4. Auto-merge guest cart with new account

### Priority 2: Progressive Profile Building
1. Tie profile completion to tangible rewards
2. Explain data usage next to each optional field
3. Implement profile completion progress indicator
4. Make phone number high-priority for SMS updates

### Priority 3: Address Convenience
1. Build BARMM-specific address dropdowns
2. Allow multiple addresses with clear default indicator
3. Enable address duplication for similar locations
4. Include landmark field for delivery accuracy

### Priority 4: Engagement Features
1. Implement price drop notifications for wishlist items
2. Create easy reorder flow from order history
3. Design loyalty program with clear earning/redemption rules
4. Send expiry reminders for points

### Priority 5: Trust & Security
1. Display login activity for transparency
2. Implement password change with device management
3. Provide data download option (GDPR)
4. Create account deletion with 30-day grace period

---

## Implementation Plan

### Phase 1: Frontend Foundation

**Pages:**
- `frontend/src/app/(public)/auth/login/page.tsx` - Login with social options
- `frontend/src/app/(public)/auth/register/page.tsx` - Registration form
- `frontend/src/app/(public)/auth/verify-email/page.tsx` - Email verification
- `frontend/src/app/(public)/auth/forgot-password/page.tsx` - Password reset request
- `frontend/src/app/(public)/auth/reset-password/page.tsx` - Password reset form
- `frontend/src/app/(public)/account/page.tsx` - Account dashboard
- `frontend/src/app/(public)/account/profile/page.tsx` - Profile management
- `frontend/src/app/(public)/account/addresses/page.tsx` - Address book
- `frontend/src/app/(public)/account/wishlist/page.tsx` - Saved products
- `frontend/src/app/(public)/account/orders/page.tsx` - Order history
- `frontend/src/app/(public)/account/loyalty/page.tsx` - Points and rewards
- `frontend/src/app/(public)/account/settings/page.tsx` - Account settings

**Components:**
- `frontend/src/components/auth/LoginForm.tsx` - Email/password with social login
- `frontend/src/components/auth/RegisterForm.tsx` - Minimal registration form
- `frontend/src/components/auth/SocialLoginButtons.tsx` - Google, Facebook OAuth
- `frontend/src/components/auth/PasswordStrengthIndicator.tsx` - Inline requirements
- `frontend/src/components/account/ProfileHeader.tsx` - Avatar, name, verified badge
- `frontend/src/components/account/ProfileCompletion.tsx` - Progress bar with rewards
- `frontend/src/components/account/AddressCard.tsx` - Address with label, default badge
- `frontend/src/components/account/AddressForm.tsx` - BARMM cascading dropdowns
- `frontend/src/components/account/WishlistItem.tsx` - Product with price drop badge
- `frontend/src/components/account/OrderCard.tsx` - Order summary with reorder
- `frontend/src/components/account/LoyaltyBalance.tsx` - Points with expiry warning
- `frontend/src/components/account/RewardsGrid.tsx` - Redeemable rewards
- `frontend/src/components/account/NotificationSettings.tsx` - Toggle preferences
- `frontend/src/components/account/SecuritySettings.tsx` - Password, login activity

**shadcn/ui Components Used:**
- Card, Button, Badge for profile sections
- Form, Input, Select for forms
- Switch for notification toggles
- Dialog for confirmations (delete address, redeem points)
- Avatar for profile photo
- Progress for completion meter
- Tabs for settings sections
- Alert for verification banner

### Phase 2: State & Services

**Hooks:**
- `frontend/src/lib/hooks/useAuth.ts` - Authentication state, login/logout
- `frontend/src/lib/hooks/useProfile.ts` - Profile data and updates
- `frontend/src/lib/hooks/useAddresses.ts` - Address CRUD operations
- `frontend/src/lib/hooks/useWishlist.ts` - Wishlist management with notifications
- `frontend/src/lib/hooks/useOrders.ts` - Order history with filters
- `frontend/src/lib/hooks/useLoyalty.ts` - Points balance, history, redemption
- `frontend/src/lib/hooks/useNotificationPreferences.ts` - Settings management
- `frontend/src/lib/hooks/useLoginActivity.ts` - Session history

**Services:**
- `frontend/src/lib/services/auth.ts` - Login, register, OAuth, password reset
- `frontend/src/lib/services/profile.ts` - Profile CRUD
- `frontend/src/lib/services/addresses.ts` - Address management
- `frontend/src/lib/services/wishlist.ts` - Wishlist operations
- `frontend/src/lib/services/loyalty.ts` - Points and rewards API
- `frontend/src/lib/services/account.ts` - Settings, data export, deletion

**Types:**
- `frontend/src/lib/types/auth.ts` - User, Session, LoginCredentials types
- `frontend/src/lib/types/profile.ts` - Profile, ProfileCompletion types
- `frontend/src/lib/types/address.ts` - Address, AddressLabel types
- `frontend/src/lib/types/loyalty.ts` - Points, Reward, Redemption types

### Phase 3: Backend Integration

**Endpoints (`backend/apps/users/api.py`):**
- `POST /api/auth/register` - Email registration
- `POST /api/auth/login` - Email/password login
- `POST /api/auth/social/{provider}` - OAuth callback
- `POST /api/auth/verify-email` - Email verification
- `POST /api/auth/forgot-password` - Password reset request
- `POST /api/auth/reset-password` - Password reset
- `GET /api/auth/me` - Current user profile
- `PATCH /api/auth/me` - Update profile
- `GET /api/auth/login-activity` - Login history
- `POST /api/auth/logout` - Logout
- `DELETE /api/auth/account` - Account deletion

**Endpoints (`backend/apps/users/api.py`):**
- `GET /api/addresses` - List addresses
- `POST /api/addresses` - Create address
- `PATCH /api/addresses/{id}` - Update address
- `DELETE /api/addresses/{id}` - Delete address
- `POST /api/addresses/{id}/set-default` - Set default

**Endpoints (`backend/apps/loyalty/api.py`):**
- `GET /api/loyalty/balance` - Current points
- `GET /api/loyalty/history` - Points history
- `GET /api/loyalty/rewards` - Available rewards
- `POST /api/loyalty/redeem` - Redeem reward
- `GET /api/loyalty/vouchers` - User vouchers

**Endpoints (`backend/apps/wishlist/api.py`):**
- `GET /api/wishlist` - List wishlist items
- `POST /api/wishlist/{product_id}` - Add to wishlist
- `DELETE /api/wishlist/{product_id}` - Remove from wishlist
- `GET /api/wishlist/price-drops` - Items with price changes

**Schemas (`backend/apps/*/schemas.py`):**
- `UserSchema`, `UserCreateSchema`, `UserUpdateSchema`
- `LoginSchema`, `RegisterSchema`, `PasswordResetSchema`
- `AddressSchema`, `AddressCreateSchema`
- `LoyaltyBalanceSchema`, `RewardSchema`, `RedemptionSchema`
- `WishlistItemSchema` with price drop indicator

### Phase 4: Polish & UX

**Loading States:**
- Skeleton for profile sections
- Skeleton for address cards
- Skeleton for order list items
- Skeleton for loyalty balance

**Error Handling:**
- Invalid credentials with retry
- Email already exists during registration
- Address validation errors
- Failed redemption with reason

**Animations:**
- Password strength indicator transitions
- Profile completion progress animation
- Wishlist heart toggle animation
- Points balance update animation

**Accessibility:**
- Form field error announcements
- Focus management after form submission
- Keyboard navigation for address selection
- Screen reader support for verification status

**Mobile Optimization:**
- Touch-friendly toggle switches
- Swipe to delete address
- Pull to refresh for order history
- Native share for wishlist

### Implementation Sequence

**Week 1-2: Authentication Foundation**
1. Login page with email/password
2. Registration form with password strength
3. Social login integration (Google first)
4. Password reset flow
5. Email verification (deferred pattern)

**Week 3-4: Profile & Addresses**
6. Account dashboard layout (depends on #1)
7. Profile management page
8. Profile completion indicator with rewards
9. Address book with CRUD
10. BARMM cascading address form (depends on #9)

**Week 5-6: Wishlist & Orders**
11. Wishlist page with product cards
12. Price drop notification badges
13. Order history with filters
14. Order detail view
15. Reorder functionality (depends on #14)

**Week 7-8: Loyalty Program**
16. Loyalty balance display
17. Points history timeline
18. Rewards catalog grid
19. Redemption flow with confirmation
20. Voucher application at checkout

**Week 9-10: Settings & Security**
21. Notification preferences page
22. Password change form
23. Login activity display
24. Account data export
25. Account deletion with grace period

---

## Implementation Status

*Audited: December 30, 2025*

### Frontend Pages
| Page | Status | Path | Notes |
|------|--------|------|-------|
| Login | ✅ Exists | `frontend/src/app/(public)/login/page.tsx` | Email/password login |
| Register | ✅ Exists | `frontend/src/app/(public)/register/page.tsx` | Registration form |
| Account Dashboard | ✅ Exists | `frontend/src/app/(account)/account/page.tsx` | Account overview |
| Profile Management | ✅ Exists | `frontend/src/app/(account)/profile/page.tsx` | Edit profile |
| Address Book | ✅ Exists | `frontend/src/app/(account)/addresses/page.tsx` | Manage addresses |
| Order History | ✅ Exists | `frontend/src/app/(account)/orders/page.tsx` | List orders |
| Order Detail | ✅ Exists | `frontend/src/app/(account)/orders/[id]/page.tsx` | Single order view |
| Saved Items | ✅ Exists | `frontend/src/app/(account)/saved/page.tsx` | Wishlist functionality |
| Training/Courses | ✅ Exists | `frontend/src/app/(account)/training/page.tsx` | User's training |
| Membership | ✅ Exists | `frontend/src/app/(account)/membership/page.tsx` | Membership status |
| Become Manager | ✅ Exists | `frontend/src/app/(account)/become-manager/page.tsx` | Upgrade path |
| Verify Email | ❌ Missing | `frontend/src/app/(public)/auth/verify-email/page.tsx` | Email verification |
| Forgot Password | ❌ Missing | `frontend/src/app/(public)/auth/forgot-password/page.tsx` | Password reset request |
| Reset Password | ❌ Missing | `frontend/src/app/(public)/auth/reset-password/page.tsx` | Password reset form |
| Loyalty Points | ❌ Missing | `frontend/src/app/(account)/loyalty/page.tsx` | Points and rewards |
| Account Settings | ❌ Missing | `frontend/src/app/(account)/settings/page.tsx` | Notification/security settings |

### Components
| Component | Status | Path | Notes |
|-----------|--------|------|-------|
| LoginForm | 🚧 Needs Audit | `frontend/src/components/auth/` | Check social login support |
| RegisterForm | 🚧 Needs Audit | `frontend/src/components/auth/` | Minimal fields check |
| SocialLoginButtons | ❌ Missing | `frontend/src/components/auth/` | Google, Facebook OAuth |
| PasswordStrengthIndicator | ❌ Missing | `frontend/src/components/auth/` | Inline requirements |
| ProfileHeader | 🚧 Needs Audit | `frontend/src/components/account/` | Avatar, verified badge |
| ProfileCompletion | ❌ Missing | `frontend/src/components/account/` | Progress bar with rewards |
| AddressCard | 🚧 Needs Audit | `frontend/src/components/account/` | Label, default badge |
| AddressForm | 🚧 Needs Audit | `frontend/src/components/account/` | BARMM cascading dropdowns |
| WishlistItem | 🚧 Needs Audit | `frontend/src/components/account/` | Price drop badge |
| OrderCard | 🚧 Needs Audit | `frontend/src/components/account/` | Reorder functionality |
| LoyaltyBalance | ❌ Missing | `frontend/src/components/account/` | Points with expiry |
| NotificationSettings | ❌ Missing | `frontend/src/components/account/` | Toggle preferences |
| SecuritySettings | ❌ Missing | `frontend/src/components/account/` | Password, login activity |

### Backend APIs
| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| POST /api/accounts/login | ✅ Exists | `backend/apps/accounts/api.py` | Email/password login |
| POST /api/accounts/register | ✅ Exists | `backend/apps/accounts/api.py` | User registration |
| GET /api/accounts/me | ✅ Exists | `backend/apps/accounts/api.py` | Current user |
| PATCH /api/accounts/profile | ✅ Exists | `backend/apps/accounts/api.py` | Update profile |
| POST /api/auth/social/{provider} | ❌ Missing | `backend/apps/accounts/api.py` | OAuth callback |
| POST /api/auth/verify-email | ❌ Missing | `backend/apps/accounts/api.py` | Email verification |
| POST /api/auth/forgot-password | ❌ Missing | `backend/apps/accounts/api.py` | Password reset request |
| POST /api/auth/reset-password | ❌ Missing | `backend/apps/accounts/api.py` | Password reset |
| GET /api/auth/login-activity | ❌ Missing | `backend/apps/accounts/api.py` | Login history |
| GET /api/addresses | ❌ Missing | `backend/apps/*/api.py` | List addresses |
| POST /api/addresses | ❌ Missing | `backend/apps/*/api.py` | Create address |
| GET /api/loyalty/balance | ❌ Missing | `backend/apps/*/api.py` | Points balance |
| GET /api/wishlist | ❌ Missing | `backend/apps/*/api.py` | Wishlist items |

### Overall Progress
- **Frontend**: 11/16 pages (69%)
- **Components**: 5/13 need audit (38%)
- **Backend**: 4/13 endpoints (31%)
