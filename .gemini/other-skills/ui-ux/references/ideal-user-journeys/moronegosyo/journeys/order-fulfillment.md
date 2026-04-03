# Order Processing Journey - MoroNegosyo

## Overview

This journey maps the complete order fulfillment experience for tenant managers on MoroNegosyo, from receiving a new order notification through delivery confirmation. The journey emphasizes efficient mobile-first order management, clear customer communication, and reliable shipping processes tailored to BARMM logistics realities.

## Persona

**Name**: Ana Maguid
**Age**: 32
**Role**: Social Enterprise Manager
**Location**: Cotabato City, Maguindanao
**Context**: Ana runs Halal Delights, a social enterprise producing halal-certified food products. She manages orders daily, often while attending to other business activities. Her enterprise ships primarily within BARMM but also to Manila for the diaspora market. She relies heavily on her smartphone for order management.

**Goals**:
- Process orders quickly to maintain customer satisfaction
- Communicate clearly with customers about order status
- Manage shipping efficiently with reliable couriers
- Reduce order issues and returns
- Build customer loyalty through excellent service

**Tech Comfort**: High - uses multiple apps for business management
**Connectivity**: Good 4G in Cotabato City
**Order Volume**: 15-30 orders per week (growing)

---

## Journey Map

### Stage 1: Order Notification

**User Goal**: Be immediately aware of new orders to start processing

**Actions**:
1. Ana receives push notification for new order
2. Sees notification summary (order total, item count)
3. Taps notification to open order details
4. Reviews order information quickly
5. Decides to process now or later

**Touchpoints**:
- Push notification
- SMS notification (backup)
- Email notification
- In-app notification center
- Order detail quick view

**Emotions**: Alert, responsive, sometimes interrupted

**Pain Points**:
- Notifications delayed or missed
- Too many notification channels (overwhelming)
- Can't see enough detail in notification
- Notification doesn't deep-link to order

**Opportunities**:
- Configurable notification preferences
- Rich notification with key details
- Deep link directly to order action screen
- Aggregate notifications for bulk orders

**Design Requirements**:
```
Push Notification Content:
[MoroNegosyo logo]
New Order #12345
3 items - PHP 1,250
Maria S. - Cotabato City
[Tap to process]

Notification Preferences:
New Orders:
[x] Push notification
[x] SMS (for orders over PHP 1,000)
[x] Email

Order Updates:
[ ] Push for status changes
[x] Email for daily summary

Quiet Hours:
[10:00 PM] to [7:00 AM]
```

---

### Stage 2: Order Review

**User Goal**: Understand the order completely before processing

**Actions**:
1. Ana opens order details from dashboard
2. Reviews ordered items and quantities
3. Checks customer address and contact
4. Verifies payment status
5. Notes any customer instructions
6. Checks inventory availability
7. Decides to confirm or contact customer

**Touchpoints**:
- Order list view
- Order detail page
- Item details section
- Customer information section
- Payment status indicator
- Order notes/instructions
- Inventory check

**Emotions**: Reviewing, verifying, responsible

**Pain Points**:
- Have to scroll too much to see all info
- Customer address is unclear
- No way to verify inventory quickly
- Special instructions hidden

**Opportunities**:
- Compact order summary view
- Highlight special instructions
- Inline inventory status per item
- Quick customer contact buttons

**Design Requirements**:
```
Order Detail Layout:

[Header]
Order #12345 | New Order
Placed: Dec 20, 2025 3:45 PM
Payment: Paid via GCash ✓

[Special Instructions Banner - if any]
"Please include extra packaging for gift"

[Items]
| Product | Qty | Price | Stock |
|---------|-----|-------|-------|
| Halal Beef | 2 | PHP 400 | ✓ 15 |
| Chicken | 3 | PHP 450 | ✓ 22 |
| Sambal | 1 | PHP 100 | ✓ 8 |

Subtotal: PHP 950
Shipping: PHP 100
Total: PHP 1,050

[Customer]
Maria Santos
+63 912 345 6789 [Call] [SMS] [Chat]

Delivery Address:
123 Main Street, Brgy. Rosary Heights
Cotabato City, Maguindanao
Landmark: Near public market

[Actions]
[Confirm Order] [Contact Customer] [More ▼]
```

---

### Stage 3: Order Confirmation

**User Goal**: Confirm the order and commit to fulfilling it

**Actions**:
1. Ana clicks "Confirm Order"
2. Sees confirmation dialog with estimated processing time
3. Selects when order will be ready
4. Confirms order processing
5. Customer receives confirmation notification
6. Order moves to "Processing" status

**Touchpoints**:
- Confirm order button
- Confirmation dialog
- Processing time selector
- Customer notification trigger
- Status update

**Emotions**: Committed, professional, time-conscious

**Pain Points**:
- Accidental confirmation without checking
- No way to set expected processing time
- Customer not notified automatically
- Can't easily undo confirmation

**Opportunities**:
- Review checklist before confirmation
- Processing time commitment
- Automated customer notification
- Grace period for changes

**Design Requirements**:
```
Confirm Order Dialog:

"Confirm Order #12345?"

By confirming, you commit to:
[x] Items are in stock
[x] Order will be prepared by selected time

When will this order be ready?
( ) Within 1 hour
(x) Within 4 hours
( ) Next business day
( ) Custom: [Date/Time picker]

Customer will be notified:
"Your order is being prepared and will be ready by [time]"

[Cancel] [Confirm Order]

---

After Confirmation:
Order Status: Processing
Customer notified via SMS and Email

[Prepare Packing Slip] [Mark as Ready]
```

---

### Stage 4: Order Preparation

**User Goal**: Prepare the order accurately for shipping

**Actions**:
1. Ana prints or views packing slip
2. Gathers items according to list
3. Checks items against order
4. Packages items appropriately
5. Adds any gift packaging if requested
6. Marks order as "Ready to Ship"

**Touchpoints**:
- Packing slip (printable/viewable)
- Item checklist
- Packaging guidelines
- Ready to ship button
- Photo capture (optional)

**Emotions**: Focused, careful, quality-conscious

**Pain Points**:
- No packing slip printer access
- Checklist not available on mobile
- Easy to miss items in large orders
- No record of what was packed

**Opportunities**:
- Mobile-friendly packing checklist
- Item scanning for verification
- Photo documentation option
- Packaging recommendation tips

**Design Requirements**:
```
Packing Slip View (Mobile-optimized):

Order #12345 | Pack by: 6:00 PM

Checklist:
[ ] Halal Beef Rendang x2
[ ] Chicken Adobo x3
[ ] Sambal Sauce x1

Special Instructions:
- Gift packaging requested

Packaging Guidelines:
- Use insulated packaging for meat
- Include reheating instructions
- Add ice pack if transit > 4 hours

[Capture Photo of Package]
Optional: Document packed items

[All Items Packed - Ready to Ship]

---

Ready to Ship Confirmation:
Order #12345 is ready to ship
Package weight: [____] kg
Package dimensions: [LxWxH] cm

[Proceed to Shipping]
```

---

### Stage 5: Shipping Arrangement

**User Goal**: Arrange reliable shipping that reaches the customer

**Actions**:
1. Ana views shipping options
2. Selects courier based on destination
3. Enters package dimensions and weight
4. Sees shipping cost calculation
5. Books shipping pickup or drop-off
6. Prints or receives shipping label
7. Hands off to courier

**Touchpoints**:
- Shipping options selector
- Courier comparison
- Package details form
- Shipping cost calculator
- Booking interface
- Shipping label generation
- Pickup scheduling

**Emotions**: Logistics-focused, cost-conscious, time-sensitive

**Pain Points**:
- Limited courier options in BARMM
- Shipping costs vary significantly
- Booking is complicated
- Label printing requires equipment

**Opportunities**:
- Pre-integrated courier options
- Shipping cost in order total
- Simplified booking flow
- QR code labels for phone scanning

**Design Requirements**:
```
Shipping Arrangement:

Destination: Cotabato City, Maguindanao
Distance: Local (same city)

Recommended Couriers:
| Courier | Est. Days | Cost | Rating |
|---------|-----------|------|--------|
| Grab Express | Same day | PHP 80 | 4.5 |
| J&T Express | 1-2 days | PHP 100 | 4.2 |
| LBC | 2-3 days | PHP 120 | 4.4 |

Package Details:
Weight: [___] kg
Dimensions: [__] x [__] x [__] cm

Shipping Cost: PHP 80
[Already included in order] or [Add to order]

Pickup/Drop-off:
( ) Schedule pickup: [Today] [Time slot]
( ) I'll drop off at: [Nearest branch]

[Book Shipping]

---

Booking Confirmed:
Courier: Grab Express
Tracking #: GRB123456789
Pickup: Today, 4:00-5:00 PM

[View Label] [Send to Customer]

Shipping Label Options:
[Print Label] [Show QR Code] [Send via Email]
```

---

### Stage 6: Tracking & Status Updates

**User Goal**: Monitor shipment progress and keep customer informed

**Actions**:
1. Ana enters tracking number (if not auto-generated)
2. Updates order status to "Shipped"
3. Customer receives shipping notification
4. Monitors tracking updates
5. Sees delivery status change
6. Follows up if delays occur

**Touchpoints**:
- Tracking number input
- Status update trigger
- Customer notification
- Tracking integration
- Delay alerts
- Follow-up actions

**Emotions**: Monitoring, hopeful, sometimes anxious about delays

**Pain Points**:
- Tracking info not integrated
- Customer asks for updates constantly
- No proactive delay notifications
- Can't intervene when issues occur

**Opportunities**:
- Integrated tracking from couriers
- Automated customer updates
- Delay detection and alerts
- Direct courier communication

**Design Requirements**:
```
Shipped Status Update:

Order #12345 - Shipping

Tracking Number*: [GRB123456789]
Courier: [Grab Express ▼]
Shipped Date: [Today's date]

[Update to Shipped]

---

Customer Notification Preview:
"Your order #12345 has been shipped!
Track: GRB123456789
Est. delivery: Dec 21, 2025"

[Send Notification]

---

Tracking Integration:

Order #12345 - In Transit
Tracking: GRB123456789

Timeline:
[x] Dec 20, 4:30 PM - Picked up
[x] Dec 20, 5:15 PM - In transit to hub
[>] Dec 20, 7:00 PM - At sorting facility
[ ] Dec 21 - Out for delivery
[ ] Dec 21 - Delivered

[View on Courier Site]

---

Delay Alert:
"Shipment delayed at sorting facility"
Est. new delivery: Dec 22

[Notify Customer] [Contact Courier]
```

---

### Stage 7: Delivery Confirmation

**User Goal**: Confirm successful delivery and close the order

**Actions**:
1. Ana receives delivery notification
2. Verifies delivery through tracking
3. Order auto-updates to "Delivered"
4. Customer receives delivery confirmation
5. Review request sent to customer
6. Order marked as complete

**Touchpoints**:
- Delivery notification
- Tracking status sync
- Auto-status update
- Customer notification
- Review request trigger
- Order completion status

**Emotions**: Satisfied, accomplished, ready for next order

**Pain Points**:
- Delivery confirmation delayed
- Customer disputes delivery
- No proof of delivery
- Review requests not sent

**Opportunities**:
- Real-time delivery sync
- Delivery photo from courier
- Automatic review request
- Dispute resolution flow

**Design Requirements**:
```
Delivery Confirmation:

Order #12345 - Delivered!
Delivered: Dec 21, 2025 2:30 PM
Received by: Maria Santos

[Proof of Delivery Photo - if available]

Customer Notified:
"Your order has been delivered!
Enjoy your Halal Delights!"

Review Request:
Sent after 2 hours to allow product use
"How was your order? Leave a review!"

[View Order Details] [Contact Customer]

---

Order Complete Summary:
Order #12345

Timeline:
- Placed: Dec 20, 3:45 PM
- Confirmed: Dec 20, 3:50 PM
- Ready: Dec 20, 5:30 PM
- Shipped: Dec 20, 6:00 PM
- Delivered: Dec 21, 2:30 PM

Total Processing Time: 22h 45m
(Your average: 24h)

[Close Order] [Request Review]
```

---

### Stage 8: Customer Communication

**User Goal**: Maintain clear communication throughout the order lifecycle

**Actions**:
1. Ana responds to customer inquiries
2. Sends proactive updates when needed
3. Handles customer concerns
4. Provides estimated times
5. Follows up after delivery

**Touchpoints**:
- In-app messaging
- Quick response templates
- Proactive update triggers
- Customer inquiry inbox
- Post-delivery follow-up

**Emotions**: Service-oriented, responsive, sometimes stressed

**Pain Points**:
- Messages scattered across channels
- No template for common questions
- Can't respond quickly on mobile
- Customer expectations unclear

**Opportunities**:
- Unified messaging inbox
- Quick reply templates
- Mobile-optimized messaging
- Automated response for common queries

**Design Requirements**:
```
Messaging Interface:

Order #12345 - Chat with Maria

[Customer avatar] Maria Santos
"Hi, when will my order be delivered?"
3:45 PM

[Quick Replies]
[Preparing now] [Shipping today] [Will update soon]

Or type: [________________________] [Send]

---

Quick Reply Templates:
- Order Confirmation:
  "Hi [Name], your order is confirmed!
   We're preparing it now."

- Shipping Update:
  "Your order has been shipped with [Courier].
   Track: [Tracking#]. Est: [Date]"

- Delay Notice:
  "Apologies for the delay. Your order
   will arrive by [New Date]. Thank you!"

- Delivery Confirmation:
  "Your order has been delivered!
   Thank you for shopping with us."

[Manage Templates]

---

Message Inbox:
| Order | Customer | Last Message | Time |
|-------|----------|--------------|------|
| #12345 | Maria | When will... | 5m |
| #12340 | Juan | Thanks! | 2h |
| #12338 | Rosa | Is it halal? | 1d |

Unread: 1 | All Messages: 15
```

---

### Stage 9: Issue Resolution

**User Goal**: Handle order issues professionally and efficiently

**Actions**:
1. Ana receives issue report from customer
2. Reviews the issue details
3. Investigates the problem
4. Decides on resolution (refund/replacement/etc.)
5. Communicates resolution to customer
6. Processes refund or ships replacement
7. Documents issue for improvement

**Touchpoints**:
- Issue notification
- Issue detail view
- Investigation tools
- Resolution options
- Customer communication
- Refund/replacement processing
- Issue documentation

**Emotions**: Concerned, problem-solving, wanting to satisfy customer

**Pain Points**:
- Issue details unclear
- No standard resolution process
- Refunds are complicated
- No way to prevent future issues

**Opportunities**:
- Structured issue reporting
- Resolution workflow guidance
- Streamlined refund process
- Issue pattern analytics

**Design Requirements**:
```
Issue Report View:

Order #12340 - Issue Reported
Type: Damaged Product
Reported: Dec 22, 2025

Customer Message:
"The sambal sauce bottle was broken
when I received the package.
The other items are okay."

[Customer Photo - broken bottle]

Order Items:
- Halal Beef Rendang x2 ✓
- Sambal Sauce x1 - ISSUE
- Chicken Adobo x3 ✓

---

Resolution Options:

( ) Full Refund - PHP 100
    Refund amount for sambal sauce

( ) Partial Refund - PHP [___]
    Custom amount

(x) Replacement
    Ship new sambal sauce

( ) Store Credit - PHP 100
    Add to customer account

Resolution Message:
[We're sorry about the broken item.
We're sending a replacement right away.
It will arrive by [Date].]

[Apply Resolution]

---

Resolution Applied:
Replacement order created: #12345-R
Shipping same-day via Grab Express

Customer Notified:
"We apologize for the inconvenience.
A replacement is on its way!"

[Track Replacement] [Close Issue]
```

---

## Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Order Confirmation Time | < 30 min | Time to first status change |
| Processing to Ship Time | < 24 hours | Status timestamp difference |
| Delivery Success Rate | > 98% | Successful deliveries |
| First Response Time | < 2 hours | Customer message response |
| Issue Rate | < 3% | Issues per order |
| Issue Resolution Time | < 24 hours | Issue to resolution |
| Customer Satisfaction | > 4.5/5 | Post-order ratings |
| Return Rate | < 2% | Returns per order |
| Tracking Accuracy | > 95% | Delivery match |
| Review Request Conversion | > 30% | Reviews per delivered order |

---

## Implementation Status

| Feature | Status | Notes |
|---------|--------|-------|
| Push notifications | TBD | FCM integration |
| Order list dashboard | TBD | Status filtering |
| Order detail view | TBD | Compact layout |
| Order confirmation flow | TBD | Processing time |
| Packing slip | TBD | Mobile-optimized |
| Shipping integration | TBD | Courier APIs |
| Tracking integration | TBD | Multi-courier |
| Customer messaging | TBD | In-app chat |
| Quick reply templates | TBD | Template manager |
| Issue resolution | TBD | Workflow engine |
| Refund processing | TBD | Payment reversal |
| Order analytics | TBD | Performance dashboard |

---

## Recommendations

### Priority 1: Mobile-First Order Management
1. Design all order workflows for one-handed phone use
2. Implement rich push notifications with quick actions
3. Create mobile-optimized packing checklists
4. Enable QR code shipping labels for phone scanning

### Priority 2: Shipping Simplification
1. Integrate 3-4 major couriers serving BARMM
2. Auto-calculate shipping costs at order time
3. Enable one-click booking for common routes
4. Provide pickup scheduling within the app

### Priority 3: Customer Communication
1. Build unified messaging inbox across all orders
2. Create quick reply template library
3. Implement proactive status notifications
4. Enable automated delay notifications

### Priority 4: Tracking Integration
1. Connect real-time tracking from major couriers
2. Auto-update order status based on tracking
3. Display tracking timeline in order view
4. Alert sellers on delivery exceptions

### Priority 5: Issue Management
1. Create structured issue reporting form
2. Guide resolution with recommended actions
3. Streamline refund processing
4. Track issue patterns for prevention

---

## Implementation Plan

### Phase 1: Frontend Foundation

**Pages:**
- `frontend/src/app/(tenant)/portal/orders/page.tsx` - Order list dashboard
- `frontend/src/app/(tenant)/portal/orders/[id]/page.tsx` - Order detail view
- `frontend/src/app/(tenant)/portal/orders/[id]/packing/page.tsx` - Packing slip view
- `frontend/src/app/(tenant)/portal/orders/[id]/shipping/page.tsx` - Shipping arrangement
- `frontend/src/app/(tenant)/portal/messages/page.tsx` - Customer messaging inbox
- `frontend/src/app/(tenant)/portal/issues/page.tsx` - Issue management
- `frontend/src/app/(tenant)/portal/issues/[id]/page.tsx` - Issue resolution

**Components:**
- `frontend/src/components/orders/OrderTable.tsx` - Order list with filters
- `frontend/src/components/orders/OrderCard.tsx` - Order summary card
- `frontend/src/components/orders/OrderDetail.tsx` - Full order information
- `frontend/src/components/orders/OrderTimeline.tsx` - Visual status timeline
- `frontend/src/components/orders/OrderActions.tsx` - Confirm, ship, etc.
- `frontend/src/components/orders/PackingChecklist.tsx` - Item checklist
- `frontend/src/components/orders/PackagePhotoCapture.tsx` - Document packing
- `frontend/src/components/shipping/CourierSelector.tsx` - Courier comparison
- `frontend/src/components/shipping/ShippingForm.tsx` - Package details
- `frontend/src/components/shipping/ShippingLabel.tsx` - Print/QR display
- `frontend/src/components/shipping/TrackingTimeline.tsx` - Courier updates
- `frontend/src/components/messages/MessageInbox.tsx` - Conversation list
- `frontend/src/components/messages/MessageThread.tsx` - Chat interface
- `frontend/src/components/messages/QuickReplyTemplates.tsx` - Template selector
- `frontend/src/components/issues/IssueCard.tsx` - Issue summary
- `frontend/src/components/issues/IssueDetail.tsx` - Issue with photos
- `frontend/src/components/issues/ResolutionOptions.tsx` - Refund/replace/credit

**shadcn/ui Components Used:**
- Table for order list with sorting
- Card, Badge for order cards and status
- Dialog for order confirmations
- Sheet for mobile order details
- Form, Input, Select for shipping forms
- Textarea for customer messages
- Checkbox for packing checklist
- Tabs for order detail sections
- Alert for action required items

### Phase 2: State & Services

**Hooks:**
- `frontend/src/lib/hooks/useOrders.ts` - Order list with filters
- `frontend/src/lib/hooks/useOrder.ts` - Single order state
- `frontend/src/lib/hooks/useOrderActions.ts` - Confirm, ship, complete
- `frontend/src/lib/hooks/useShipping.ts` - Courier and booking
- `frontend/src/lib/hooks/useTracking.ts` - Real-time tracking
- `frontend/src/lib/hooks/useMessages.ts` - Customer messaging
- `frontend/src/lib/hooks/useMessageThread.ts` - Individual conversation
- `frontend/src/lib/hooks/useIssues.ts` - Issue list and management
- `frontend/src/lib/hooks/useIssueResolution.ts` - Resolution workflow
- `frontend/src/lib/hooks/useNotifications.ts` - Push notification handling

**Services:**
- `frontend/src/lib/services/orders.ts` - Order operations
- `frontend/src/lib/services/shipping.ts` - Courier API integration
- `frontend/src/lib/services/tracking.ts` - Tracking data
- `frontend/src/lib/services/messages.ts` - Messaging API
- `frontend/src/lib/services/issues.ts` - Issue management
- `frontend/src/lib/services/refunds.ts` - Refund processing

**Types:**
- `frontend/src/lib/types/order.ts` - Order, OrderItem, OrderStatus
- `frontend/src/lib/types/shipping.ts` - Courier, ShippingBooking, Label
- `frontend/src/lib/types/tracking.ts` - TrackingEvent, DeliveryStatus
- `frontend/src/lib/types/message.ts` - Message, Thread, Template
- `frontend/src/lib/types/issue.ts` - Issue, IssueType, Resolution

### Phase 3: Backend Integration

**Endpoints (`backend/apps/orders/api.py`):**
- `GET /api/tenant/orders` - List orders with filters
- `GET /api/tenant/orders/{id}` - Order detail
- `POST /api/tenant/orders/{id}/confirm` - Confirm order
- `POST /api/tenant/orders/{id}/ready` - Mark ready to ship
- `POST /api/tenant/orders/{id}/ship` - Add shipping info
- `POST /api/tenant/orders/{id}/complete` - Mark delivered
- `GET /api/tenant/orders/{id}/packing-slip` - Packing slip data

**Endpoints (`backend/apps/shipping/api.py`):**
- `GET /api/couriers` - Available couriers
- `POST /api/shipping/calculate` - Calculate shipping cost
- `POST /api/shipping/book` - Book courier pickup
- `GET /api/shipping/tracking/{tracking_number}` - Get tracking
- `POST /api/shipping/labels` - Generate label

**Endpoints (`backend/apps/messages/api.py`):**
- `GET /api/tenant/messages` - List conversations
- `GET /api/tenant/messages/{thread_id}` - Get thread
- `POST /api/tenant/messages/{thread_id}` - Send message
- `GET /api/tenant/messages/templates` - Quick reply templates
- `POST /api/tenant/messages/templates` - Create template

**Endpoints (`backend/apps/issues/api.py`):**
- `GET /api/tenant/issues` - List issues
- `GET /api/tenant/issues/{id}` - Issue detail
- `POST /api/tenant/issues/{id}/resolve` - Apply resolution
- `POST /api/tenant/issues/{id}/refund` - Process refund
- `POST /api/tenant/issues/{id}/replace` - Create replacement

**Schemas (`backend/apps/*/schemas.py`):**
- `OrderListSchema`, `OrderDetailSchema`
- `OrderConfirmSchema`, `ShipmentSchema`
- `CourierSchema`, `ShippingBookingSchema`
- `TrackingSchema`, `TrackingEventSchema`
- `MessageSchema`, `ThreadSchema`, `TemplateSchema`
- `IssueSchema`, `ResolutionSchema`, `RefundSchema`

### Phase 4: Polish & UX

**Loading States:**
- Skeleton for order list table
- Skeleton for order detail sections
- Tracking timeline loading animation
- Message thread loading

**Error Handling:**
- Shipping booking failure with alternatives
- Tracking data unavailable fallback
- Message send failure with retry
- Refund processing error handling

**Animations:**
- Order status badge transitions
- Packing checklist check animations
- Message send/receive animations
- Issue resolution success feedback

**Accessibility:**
- Order table keyboard navigation
- Packing checklist focus management
- Message thread screen reader support
- Status update announcements

**Mobile Optimization:**
- Rich push notifications with quick actions
- Swipe actions on order list
- QR code label for phone scanning
- Touch-friendly packing checklist
- Voice input for customer messages

### Implementation Sequence

**Week 1-2: Order Dashboard**
1. Order list table with status filters
2. Order card component
3. Order detail page layout
4. Order timeline component
5. Order confirmation flow

**Week 3-4: Packing & Preparation**
6. Packing slip view (depends on #4)
7. Packing checklist with checkboxes
8. Package photo capture
9. Mark ready to ship flow
10. Processing time commitment

**Week 5-6: Shipping Integration**
11. Courier selector with comparison
12. Shipping form (weight, dimensions)
13. Shipping cost calculation
14. Courier booking interface
15. Shipping label generation

**Week 7-8: Tracking & Communication**
16. Tracking timeline integration
17. Auto-status updates from courier
18. Message inbox page
19. Message thread interface
20. Quick reply templates

**Week 9-10: Issues & Resolution**
21. Issue list and filtering
22. Issue detail with photos
23. Resolution options interface
24. Refund processing flow
25. Replacement order creation

---

## Implementation Status

*Audited: December 30, 2025*

### Frontend Pages
| Page | Status | Path | Notes |
|------|--------|------|-------|
| Tenant Dashboard | ✅ Exists | `frontend/src/app/(tenant)/dashboard/page.tsx` | Overview with orders |
| Finances Overview | ✅ Exists | `frontend/src/app/(tenant)/finances/page.tsx` | Financial summary |
| Coop Order View | ✅ Exists | `frontend/src/app/(coop)/coop/[shortname]/order/[orderId]/page.tsx` | Order from storefront |
| SE Order View | ✅ Exists | `frontend/src/app/(se)/se/[shortname]/order/[orderId]/page.tsx` | Order from storefront |
| Orders List | ❌ Missing | `frontend/src/app/(tenant)/portal/orders/page.tsx` | Order list dashboard |
| Order Detail | ❌ Missing | `frontend/src/app/(tenant)/portal/orders/[id]/page.tsx` | Full order view |
| Packing Slip | ❌ Missing | `frontend/src/app/(tenant)/portal/orders/[id]/packing/page.tsx` | Mobile packing view |
| Shipping Arrangement | ❌ Missing | `frontend/src/app/(tenant)/portal/orders/[id]/shipping/page.tsx` | Courier booking |
| Messages Inbox | ❌ Missing | `frontend/src/app/(tenant)/portal/messages/page.tsx` | Customer messaging |
| Issues List | ❌ Missing | `frontend/src/app/(tenant)/portal/issues/page.tsx` | Issue management |
| Issue Resolution | ❌ Missing | `frontend/src/app/(tenant)/portal/issues/[id]/page.tsx` | Resolve issues |

### Components
| Component | Status | Path | Notes |
|-----------|--------|------|-------|
| OrderTable | 🚧 Needs Audit | `frontend/src/components/orders/` | Order list with filters |
| OrderCard | 🚧 Needs Audit | `frontend/src/components/orders/` | Order summary card |
| OrderDetail | 🚧 Needs Audit | `frontend/src/components/orders/` | Full order info |
| OrderTimeline | 🚧 Needs Audit | `frontend/src/components/orders/` | Visual status |
| OrderActions | ❌ Missing | `frontend/src/components/orders/` | Confirm, ship, etc. |
| PackingChecklist | ❌ Missing | `frontend/src/components/orders/` | Item checklist |
| PackagePhotoCapture | ❌ Missing | `frontend/src/components/orders/` | Document packing |
| CourierSelector | ❌ Missing | `frontend/src/components/shipping/` | Courier comparison |
| ShippingForm | ❌ Missing | `frontend/src/components/shipping/` | Package details |
| ShippingLabel | ❌ Missing | `frontend/src/components/shipping/` | Print/QR display |
| TrackingTimeline | ❌ Missing | `frontend/src/components/shipping/` | Courier updates |
| MessageInbox | ❌ Missing | `frontend/src/components/messages/` | Conversation list |
| MessageThread | ❌ Missing | `frontend/src/components/messages/` | Chat interface |
| QuickReplyTemplates | ❌ Missing | `frontend/src/components/messages/` | Template selector |
| IssueCard | ❌ Missing | `frontend/src/components/issues/` | Issue summary |
| ResolutionOptions | ❌ Missing | `frontend/src/components/issues/` | Refund/replace/credit |

### Backend APIs
| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| GET /api/tenant/orders | ✅ Exists | `backend/apps/tenant/api.py` | List orders |
| GET /api/core/shop/orders | ✅ Exists | `backend/apps/core/api.py` | Shop orders |
| GET /api/public/orders | ✅ Exists | `backend/apps/*/api.py` | Public order data |
| GET /api/tenant/orders/{id} | ❌ Missing | `backend/apps/tenant/api.py` | Order detail |
| POST /api/tenant/orders/{id}/confirm | ❌ Missing | `backend/apps/tenant/api.py` | Confirm order |
| POST /api/tenant/orders/{id}/ready | ❌ Missing | `backend/apps/tenant/api.py` | Mark ready |
| POST /api/tenant/orders/{id}/ship | ❌ Missing | `backend/apps/tenant/api.py` | Add shipping |
| GET /api/tenant/orders/{id}/packing-slip | ❌ Missing | `backend/apps/tenant/api.py` | Packing slip |
| GET /api/couriers | ❌ Missing | `backend/apps/shipping/api.py` | Available couriers |
| POST /api/shipping/calculate | ❌ Missing | `backend/apps/shipping/api.py` | Calculate cost |
| POST /api/shipping/book | ❌ Missing | `backend/apps/shipping/api.py` | Book courier |
| GET /api/shipping/tracking/{number} | ❌ Missing | `backend/apps/shipping/api.py` | Get tracking |
| GET /api/tenant/messages | ❌ Missing | `backend/apps/messages/api.py` | List conversations |
| POST /api/tenant/messages/{thread_id} | ❌ Missing | `backend/apps/messages/api.py` | Send message |
| GET /api/tenant/issues | ❌ Missing | `backend/apps/issues/api.py` | List issues |
| POST /api/tenant/issues/{id}/resolve | ❌ Missing | `backend/apps/issues/api.py` | Apply resolution |

### Overall Progress
- **Frontend**: 4/11 pages (36%)
- **Components**: 4/16 need audit (25%)
- **Backend**: 3/16 endpoints (19%)
