# Consumer to Tenant Manager Journey - MoroNegosyo

## Overview

This journey maps the transformation from a regular consumer account to a tenant manager (cooperative or social enterprise manager) on MoroNegosyo. This is a critical conversion journey that brings new sellers onto the platform while ensuring compliance with CSEA registration requirements.

## Persona

**Name**: Rosa Macaraya
**Age**: 45
**Role**: Cooperative Officer (Secretary/Treasurer)
**Location**: Lamitan City, Basilan
**Context**: Rosa is the secretary of the Lamitan Weavers Cooperative, a group of 50 women producing traditional Yakan textiles. The cooperative has been operating for 10 years and is registered with CDA. They currently sell through local markets and occasional trade fairs, but want to expand their reach through online sales. Rosa has basic computer skills and uses a smartphone daily.

**Goals**:
- Register her cooperative on MoroNegosyo to sell products online
- Complete the registration process with minimal back-and-forth
- Upload required compliance documents correctly the first time
- Get approved quickly to start listing products before the holiday season

**Tech Comfort**: Moderate - uses Facebook, GCash, basic document handling
**Connectivity**: 3G/4G depending on location, sometimes unstable
**Documentation**: Has most documents but may need to scan them

---

## Journey Map

### Stage 1: Discovery & Interest

**User Goal**: Understand if MoroNegosyo is right for our cooperative

**Actions**:
1. Rosa hears about MoroNegosyo from a CSEA field officer
2. Visits the homepage as a consumer
3. Browses existing cooperative storefronts
4. Looks for "Sell on MoroNegosyo" information
5. Reads benefits and requirements for sellers
6. Discusses with cooperative board

**Touchpoints**:
- Homepage with seller CTA
- "Sell on MoroNegosyo" landing page
- Benefits overview
- Requirements checklist
- FAQ section
- Contact/inquiry form

**Emotions**: Curious, cautiously optimistic, evaluating feasibility

**Pain Points**:
- Unclear if their cooperative type qualifies
- Requirements seem complex
- Uncertain about fees or costs
- Worried about technical skills needed

**Opportunities**:
- Clear eligibility checker
- Success stories from similar cooperatives
- No fees/commission structure clarity
- Testimonials from non-tech-savvy sellers

**Design Requirements**:
```
"Sell on MoroNegosyo" Landing Page:
- Hero: "Bring your cooperative online"
- Benefits cards: Reach customers, CSEA compliance, free to join
- Quick eligibility check: Cooperative/SE type selector
- Requirements preview with downloadable checklist
- Success stories with photos from real cooperatives
- FAQ accordion
- "Get Started" CTA + "Contact Us" alternative
```

---

### Stage 2: Pre-Application Preparation

**User Goal**: Gather all required documents before starting the application

**Actions**:
1. Rosa downloads the requirements checklist
2. Reviews what documents are needed
3. Gathers existing documents (CDA registration, permits)
4. Scans or photographs documents
5. Verifies document validity dates
6. Gets board approval to proceed

**Touchpoints**:
- Requirements checklist (downloadable PDF)
- Document preparation guide
- Sample document images
- Document scanner tips
- Board resolution template

**Emotions**: Organized, slightly overwhelmed, determined

**Pain Points**:
- Some documents are expired and need renewal
- Unsure of exact document format requirements
- No scanner, only phone camera
- Board resolution format unclear

**Opportunities**:
- Document validity checker tool
- Mobile-optimized document capture
- Template downloads for resolutions
- Allow partial application saves

**Design Requirements**:
```
Document Preparation Page:

Required Documents (with sample images):
1. CDA Certificate of Registration
   - Must be valid (check expiry)
   - Clear, readable scan
   - [View Sample] [Tips for Scanning]

2. Business Permit (current year)
   - From your LGU
   - [View Sample]

3. BIR Certificate of Registration
   - Form 2303
   - [View Sample]

4. Board Resolution to Register
   - Authorizing representative
   - [Download Template]

5. Valid ID of Authorized Representative
   - Government-issued ID
   - [Accepted IDs List]

Document Tips:
- Phone camera acceptable (ensure good lighting)
- PDF or JPG format
- Max 5MB per file
- Text must be readable
```

---

### Stage 3: Application Initiation

**User Goal**: Start the registration process with my existing consumer account

**Actions**:
1. Rosa logs into her existing consumer account
2. Finds "Register as Seller" in account menu
3. Selects organization type (Cooperative)
4. Sees step-by-step application overview
5. Confirms she has required documents ready
6. Begins the application process

**Touchpoints**:
- Account dropdown menu
- "Register as Seller" entry point
- Organization type selection
- Application overview screen
- Document readiness check
- Application wizard start

**Emotions**: Committed, slightly nervous, focused

**Pain Points**:
- Can't find the registration option
- Unsure which organization type to select
- Worried about making mistakes
- Unclear how long it will take

**Opportunities**:
- Prominent seller registration CTA in account
- Clear organization type descriptions
- Progress estimation (time and steps)
- Auto-save to prevent data loss

**Design Requirements**:
```
Registration Entry Points:
1. Account dropdown: "Register as Seller" menu item
2. Footer link: "Sell on MoroNegosyo"
3. Header CTA (for logged-in users): "Start Selling"

Application Overview Screen:
- Step indicators: 1. Organization Info → 2. Documents → 3. Review
- Estimated time: "About 20 minutes"
- What you'll need (checklist)
- [ ] I have my documents ready
- [Start Application] button

Organization Type Selection:
[Cooperative] card
- Registered with CDA
- Member-owned organization
- [Select]

[Social Enterprise] card
- Registered with DTI/SEC
- Mission-driven business
- [Select]

[Not Sure?] link to comparison guide
```

---

### Stage 4: Organization Information

**User Goal**: Provide accurate information about our cooperative

**Actions**:
1. Rosa enters official cooperative name
2. Inputs CDA registration number and date
3. Selects primary sector (handicrafts/weaving)
4. Enters number of members
5. Provides cooperative address (BARMM location)
6. Adds contact person details
7. Writes brief description of cooperative

**Touchpoints**:
- Multi-step form wizard
- Progress indicator
- Field validation (inline)
- Help tooltips
- Save draft functionality
- Back/Next navigation

**Emotions**: Careful, referencing documents, wanting accuracy

**Pain Points**:
- Form is too long on one page
- Not sure what to write in description
- Address dropdowns don't match her location
- Loses progress if phone disconnects

**Opportunities**:
- Break form into logical steps
- Description templates/prompts
- BARMM-specific address hierarchy
- Auto-save every field change

**Design Requirements**:
```
Step 1: Basic Information (5-7 fields per step)
- Organization Name* (official registered name)
- Registration Number* (CDA/SEC/DTI)
- Registration Date* (date picker)
- Organization Type (auto-filled from selection)
- Primary Sector* (dropdown)
- Number of Members/Employees*

Step 2: Location & Contact
- Province* (BARMM provinces)
- Municipality* (cascading)
- Barangay* (cascading)
- Street Address*
- Contact Person Name*
- Position/Title*
- Email*
- Phone Number*

Step 3: Description
- Brief Description* (textarea with prompts)
  - "Describe your products, history, and impact..."
  - Character count: 0/500
- Year Established
- Website/Social Media (optional)

Auto-save indicator:
"Draft saved automatically" (shown on each change)

[Save & Continue Later] [Previous] [Next Step]
```

---

### Stage 5: Document Upload

**User Goal**: Upload all required documents correctly the first time

**Actions**:
1. Rosa sees list of required documents with status
2. Clicks to upload CDA registration
3. Takes photo or selects file from phone
4. Sees preview and confirms upload
5. System validates document (basic checks)
6. Repeats for each required document
7. Sees all documents uploaded successfully

**Touchpoints**:
- Document checklist with upload status
- File upload interface (camera/gallery)
- Document preview
- Validation feedback
- Upload progress indicator
- Completion status per document

**Emotions**: Focused, methodical, relieved when complete

**Pain Points**:
- Document photos are unclear/rejected
- Upload fails on slow connection
- Not sure if document is correct format
- Can't see what was uploaded after

**Opportunities**:
- Document photo quality tips
- Retry on connection failure
- Sample images for comparison
- Preview/replace uploaded documents

**Design Requirements**:
```
Document Upload Screen:

[Document Checklist]
- [x] CDA Certificate of Registration [View] [Replace]
- [ ] Business Permit (current year) [Upload]
- [ ] BIR Registration (Form 2303) [Upload]
- [ ] Board Resolution [Upload]
- [ ] Valid ID (Authorized Rep) [Upload]

Upload Interface:
[Take Photo] [Choose File]
- Preview window
- "Make sure text is readable"
- [Confirm] [Retake]

Validation Feedback:
[check] File uploaded successfully
[!] Image quality may be low - text should be readable
[x] File too large (max 5MB) - please resize

Progress: 3 of 5 documents uploaded
```

---

### Stage 6: Application Review & Submission

**User Goal**: Review my application before submitting for approval

**Actions**:
1. Rosa sees complete application summary
2. Reviews organization information
3. Verifies uploaded documents
4. Makes corrections if needed
5. Reads and accepts terms and conditions
6. Submits application for review
7. Sees confirmation with next steps

**Touchpoints**:
- Application summary page
- Edit links per section
- Document thumbnails with view option
- Terms and conditions
- Submit button
- Confirmation screen with timeline

**Emotions**: Careful review, slight anxiety, relief upon submission

**Pain Points**:
- Summary is too long to review on mobile
- Can't edit without losing progress
- Terms are too long to read
- Unclear what happens next

**Opportunities**:
- Collapsible summary sections
- Section-by-section edit capability
- Terms summary with full link
- Clear timeline and expectations

**Design Requirements**:
```
Review Screen Layout:

[Application Summary]
Organization Information [Edit]
- Name: Lamitan Weavers Cooperative
- Registration: CDA-12345
- Sector: Handicrafts
- Members: 50
(collapsible for all details)

Uploaded Documents [Edit]
- [thumbnail] CDA Certificate ✓
- [thumbnail] Business Permit ✓
- [thumbnail] BIR Registration ✓
- [thumbnail] Board Resolution ✓
- [thumbnail] Valid ID ✓

[Agreement]
By submitting, I confirm that:
- Information provided is accurate
- I am authorized to register this organization
- I agree to Terms of Service [link]

[Submit Application]

Confirmation Screen:
[Check icon] Application Submitted!
Application ID: APP-2025-001234

What happens next:
1. CSEA reviews your application (3-5 business days)
2. You'll receive email notification
3. If approved, you can start adding products

[Track Application Status] [Return to Homepage]
```

---

### Stage 7: Application Review Period

**User Goal**: Track my application status and respond to any requests

**Actions**:
1. Rosa waits for review (checks status periodically)
2. Receives email about status update
3. Logs in to check application status
4. Sees request for additional information (if any)
5. Responds with requested clarification
6. Continues waiting for final decision

**Touchpoints**:
- Application status page
- Email notifications
- Request for information interface
- Document replacement upload
- Chat/message with CSEA reviewer

**Emotions**: Waiting, anxious, sometimes frustrated, hopeful

**Pain Points**:
- No visibility into review progress
- Generic status messages
- Unclear why additional info needed
- No direct communication with reviewer

**Opportunities**:
- Detailed status timeline
- Estimated completion date
- Clear explanation for requests
- In-app messaging with reviewer

**Design Requirements**:
```
Application Status Page:

Status: Under Review
Application ID: APP-2025-001234
Submitted: Dec 15, 2025

Timeline:
[x] Submitted - Dec 15, 2025
[x] Documents Received - Dec 15, 2025
[>] Under Review - Started Dec 16, 2025
    Estimated completion: Dec 20, 2025
[ ] Decision

[Action Required]
Additional Information Requested

The reviewer has requested clarification:
"Please provide a clearer copy of the Business Permit.
The expiry date is not readable."

[Upload New Document] [Message Reviewer]

Notification Preferences:
[x] Email me on status changes
[x] SMS on approval/rejection
```

---

### Stage 8: Approval & Role Upgrade

**User Goal**: Get approved and access my new seller capabilities

**Actions**:
1. Rosa receives approval notification
2. Logs in to see congratulations message
3. Sees her account now has "Manager" role
4. Accesses new Seller Portal dashboard
5. Takes brief orientation tour
6. Understands key features available
7. Ready to start adding products

**Touchpoints**:
- Approval email with celebration
- Login redirect to new dashboard
- Role upgrade confirmation
- Portal orientation tour
- Dashboard with quick actions
- Getting started checklist

**Emotions**: Excited, accomplished, slightly overwhelmed, eager to start

**Pain Points**:
- Dashboard is unfamiliar and complex
- Not sure where to start
- Features are overwhelming
- Worried about making mistakes

**Opportunities**:
- Guided orientation tour
- Progressive feature disclosure
- Clear getting started checklist
- Contextual help tooltips

**Design Requirements**:
```
Approval Email:
Subject: Congratulations! Your cooperative is approved

[Cooperative Logo]
Welcome to MoroNegosyo!

Lamitan Weavers Cooperative has been approved.
You can now start selling on the platform.

[Go to Your Dashboard]

First Login Experience:
[Celebration animation/confetti]
"Welcome, Rosa!"
"Your cooperative is now registered on MoroNegosyo"

[Start Orientation Tour] [Skip for now]

Orientation Tour (5 steps):
1. Dashboard Overview - Your home base
2. Shop Settings - Customize your storefront
3. Add Products - List your first item
4. Orders - Manage customer orders
5. Compliance - Track your FRAMES status

Getting Started Checklist (persistent):
[ ] Complete shop profile
[ ] Add shop logo
[ ] Add your first product
[ ] Set up payment preferences
[ ] Preview your storefront

Progress: 0% complete
```

---

### Stage 9: First Login to Tenant Portal

**User Goal**: Navigate the new seller portal and understand my capabilities

**Actions**:
1. Rosa explores the dashboard
2. Sees shop completion checklist
3. Starts with shop profile setup
4. Uploads shop logo and banner
5. Writes shop description
6. Previews public storefront
7. Proceeds to add first product

**Touchpoints**:
- Seller dashboard
- Shop settings/profile page
- Image upload interfaces
- Shop preview (public view)
- Navigation sidebar
- Product management entry

**Emotions**: Exploring, learning, accomplishing small wins

**Pain Points**:
- Too many options to understand
- Not sure what's required vs optional
- Shop preview doesn't work well on mobile
- Overwhelmed by settings

**Opportunities**:
- Highlight recommended next steps
- Show required vs optional clearly
- Mobile-responsive preview
- Contextual explanations

**Design Requirements**:
```
Seller Dashboard Layout:

[Header]
- Organization name + logo
- Role: Manager
- [View Shop] [Quick Add Product]

[Sidebar Navigation]
- Dashboard (home icon)
- Products
- Orders
- Shop Settings
- Compliance (FRAMES)
- Messages
- Reports

[Main Content - Dashboard]
Getting Started (prominent if incomplete)
- Complete shop profile [60%]
- Add your first product [0]
- Set up payment [Pending]

Quick Stats (once active)
- Today's orders: 0
- Pending orders: 0
- Products listed: 0
- Shop views: 0

[Tips & Help]
- "Add at least 5 products to rank higher"
- "Complete your shop profile for better visibility"
```

---

## Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Application Start Rate | > 60% of info page visitors | Funnel conversion |
| Application Completion Rate | > 80% of started | Funnel conversion |
| Document Upload Success | > 90% first attempt | Error tracking |
| Average Application Time | < 25 minutes | Session analytics |
| Revision Request Rate | < 30% | Review data |
| Approval Rate | > 85% | Application outcomes |
| Time to Approval | < 5 business days | Processing analytics |
| First Product Listed | > 80% within 7 days | Post-approval funnel |
| Onboarding Completion | > 70% complete checklist | Feature tracking |
| 30-Day Retention | > 90% active | Login activity |

---

## Implementation Status

| Feature | Status | Notes |
|---------|--------|-------|
| Sell on MoroNegosyo landing | TBD | Marketing content needed |
| Requirements checklist | TBD | Document templates |
| Organization type selection | TBD | Coop vs SE logic |
| Multi-step application form | TBD | Form wizard component |
| BARMM address dropdowns | TBD | Location data required |
| Document upload interface | TBD | Mobile camera capture |
| Application review screen | TBD | Edit capability |
| Application status tracking | TBD | CSEA workflow |
| Approval notification | TBD | Email templates |
| Role upgrade mechanism | TBD | User role system |
| Seller portal dashboard | TBD | New portal layout |
| Onboarding tour | TBD | Product tour library |
| Getting started checklist | TBD | Progress tracking |

---

## Recommendations

### Priority 1: Reduce Application Friction
1. Break application into 3-4 digestible steps
2. Implement auto-save on every field change
3. Allow partial save and continue later
4. Provide clear document requirements with samples

### Priority 2: Document Upload Experience
1. Optimize for mobile camera capture
2. Provide real-time quality feedback
3. Allow document replacement without restarting
4. Support multiple file formats (PDF, JPG, PNG)

### Priority 3: Transparency During Review
1. Show detailed status timeline
2. Provide estimated completion dates
3. Enable direct messaging with reviewer
4. Send proactive status update notifications

### Priority 4: Smooth Role Transition
1. Create guided orientation tour
2. Implement getting started checklist
3. Provide contextual help throughout portal
4. Celebrate small wins (first product, first order)

### Priority 5: Ongoing Support
1. Create video tutorials for common tasks
2. Enable chat support for new sellers
3. Build community forum for peer learning
4. Schedule follow-up check-ins for new sellers

---

## Implementation Plan

### Phase 1: Frontend Foundation

**Pages:**
- `frontend/src/app/(public)/sell/page.tsx` - "Sell on MoroNegosyo" landing page
- `frontend/src/app/(public)/sell/requirements/page.tsx` - Requirements checklist
- `frontend/src/app/(public)/sell/eligibility/page.tsx` - Eligibility checker
- `frontend/src/app/(tenant)/register/page.tsx` - Application start (org type selection)
- `frontend/src/app/(tenant)/register/[step]/page.tsx` - Multi-step wizard
- `frontend/src/app/(tenant)/register/status/page.tsx` - Application status tracking
- `frontend/src/app/(tenant)/portal/page.tsx` - Seller dashboard (post-approval)
- `frontend/src/app/(tenant)/portal/getting-started/page.tsx` - Onboarding checklist

**Components:**
- `frontend/src/components/sell/HeroSection.tsx` - Landing page hero
- `frontend/src/components/sell/BenefitsCards.tsx` - Seller benefits display
- `frontend/src/components/sell/EligibilityChecker.tsx` - Quick eligibility quiz
- `frontend/src/components/sell/RequirementsChecklist.tsx` - Downloadable checklist
- `frontend/src/components/sell/SuccessStories.tsx` - Cooperative testimonials
- `frontend/src/components/register/OrgTypeSelector.tsx` - Coop vs SE selection
- `frontend/src/components/register/ApplicationWizard.tsx` - Multi-step form container
- `frontend/src/components/register/OrgInfoForm.tsx` - Organization details form
- `frontend/src/components/register/DocumentUpload.tsx` - Document upload interface
- `frontend/src/components/register/DocumentPreview.tsx` - Uploaded document preview
- `frontend/src/components/register/ApplicationReview.tsx` - Submission summary
- `frontend/src/components/register/ApplicationTimeline.tsx` - Status timeline
- `frontend/src/components/portal/OnboardingTour.tsx` - Guided product tour
- `frontend/src/components/portal/GettingStartedChecklist.tsx` - Progress checklist

**shadcn/ui Components Used:**
- Card, Button, Badge for landing page sections
- Form, Input, Select, Textarea for application forms
- Progress for wizard and completion indicators
- Dialog for document preview
- Alert for status updates and action requests
- Tabs for application sections
- Skeleton for loading states
- Toast for upload confirmations

### Phase 2: State & Services

**Hooks:**
- `frontend/src/lib/hooks/useApplication.ts` - Application state and submission
- `frontend/src/lib/hooks/useApplicationStatus.ts` - Status polling/websocket
- `frontend/src/lib/hooks/useDocumentUpload.ts` - File upload with progress
- `frontend/src/lib/hooks/useOnboarding.ts` - Onboarding checklist state
- `frontend/src/lib/hooks/useBARMMLocations.ts` - Province/municipality/barangay
- `frontend/src/lib/hooks/useAutoSave.ts` - Form auto-save functionality

**Services:**
- `frontend/src/lib/services/application.ts` - Application CRUD and submission
- `frontend/src/lib/services/documents.ts` - Document upload and validation
- `frontend/src/lib/services/onboarding.ts` - Checklist progress tracking
- `frontend/src/lib/services/templates.ts` - Template download URLs

**Types:**
- `frontend/src/lib/types/application.ts` - Application, OrgType, ApplicationStatus
- `frontend/src/lib/types/document.ts` - Document, DocumentType, UploadProgress
- `frontend/src/lib/types/onboarding.ts` - OnboardingStep, ChecklistItem

### Phase 3: Backend Integration

**Endpoints (`backend/apps/tenant/api.py`):**
- `POST /api/applications` - Create application
- `GET /api/applications/{id}` - Get application detail
- `PATCH /api/applications/{id}` - Update application (draft save)
- `POST /api/applications/{id}/submit` - Submit for review
- `GET /api/applications/{id}/status` - Get review status
- `POST /api/applications/{id}/documents` - Upload document
- `DELETE /api/applications/{id}/documents/{doc_id}` - Remove document
- `POST /api/applications/{id}/respond` - Respond to reviewer request

**Endpoints (`backend/apps/tenant/api.py`):**
- `GET /api/onboarding/checklist` - Get onboarding steps
- `PATCH /api/onboarding/checklist/{step}` - Mark step complete
- `GET /api/templates/{type}` - Download document template

**Endpoints (`backend/apps/core/api.py`):**
- `GET /api/sectors` - List business sectors
- `GET /api/org-types` - Organization types (Coop/SE)

**Schemas (`backend/apps/*/schemas.py`):**
- `ApplicationCreateSchema`, `ApplicationUpdateSchema`
- `ApplicationDetailSchema` with status timeline
- `DocumentUploadSchema`, `DocumentSchema`
- `ReviewerCommentSchema`, `ResponseSchema`
- `OnboardingChecklistSchema`, `OnboardingStepSchema`

### Phase 4: Polish & UX

**Loading States:**
- Skeleton for application status page
- Upload progress indicator per document
- Submission processing overlay
- Onboarding checklist skeleton

**Error Handling:**
- Document upload failure with retry
- File size/format validation errors
- Network interruption during upload
- Application save failure recovery

**Animations:**
- Wizard step transitions
- Document upload success animation
- Status timeline updates
- Onboarding tour spotlight effects
- Celebration confetti on approval

**Accessibility:**
- Form field focus management
- Screen reader announcements for upload status
- Keyboard navigation in document list
- Alt text for sample document images

**Mobile Optimization:**
- Camera capture for document upload
- Touch-friendly document reordering
- Swipe between wizard steps
- Responsive timeline display

### Implementation Sequence

**Week 1-2: Landing & Discovery**
1. "Sell on MoroNegosyo" landing page
2. Benefits cards and success stories
3. Eligibility checker component
4. Requirements checklist (downloadable)
5. FAQ accordion

**Week 3-4: Application Wizard**
6. Organization type selection (depends on #1)
7. Application wizard container with progress
8. Organization info form (step 1)
9. BARMM location dropdowns (depends on #8)
10. Auto-save functionality

**Week 5-6: Document Upload**
11. Document checklist display
12. Document upload interface with camera
13. Upload progress and validation
14. Document preview modal
15. Document replacement flow

**Week 7-8: Review & Submission**
16. Application review summary page (depends on #15)
17. Declaration and terms acceptance
18. Submission confirmation
19. Application status tracking page
20. Reviewer comment response interface

**Week 9-10: Post-Approval**
21. Approval notification and celebration
22. Seller dashboard layout
23. Onboarding tour component
24. Getting started checklist
25. Shop profile setup guidance

---

## Implementation Status

*Audited: December 30, 2025*

### Frontend Pages
| Page | Status | Path | Notes |
|------|--------|------|-------|
| Sell on MoroNegosyo Landing | ❌ Missing | `frontend/src/app/(public)/sell/page.tsx` | Marketing landing page |
| Requirements Checklist | ❌ Missing | `frontend/src/app/(public)/sell/requirements/page.tsx` | Document checklist |
| Eligibility Checker | ❌ Missing | `frontend/src/app/(public)/sell/eligibility/page.tsx` | Quick eligibility quiz |
| Tenant Login | ✅ Exists | `frontend/src/app/(tenant)/login/page.tsx` | Manager login |
| Tenant Register | ✅ Exists | `frontend/src/app/(tenant)/register/page.tsx` | Multi-page registration |
| Coop Registration | ✅ Exists | `frontend/src/app/(coop)/coop/register/` | Multiple pages for coop |
| SE Registration | ✅ Exists | `frontend/src/app/(se)/se/register/` | Multiple pages for SE |
| Tenant Dashboard | ✅ Exists | `frontend/src/app/(tenant)/dashboard/page.tsx` | Post-approval dashboard |
| Application Status | ❌ Missing | `frontend/src/app/(tenant)/register/status/page.tsx` | Track application |
| Getting Started | ❌ Missing | `frontend/src/app/(tenant)/portal/getting-started/page.tsx` | Onboarding checklist |

### Components
| Component | Status | Path | Notes |
|-----------|--------|------|-------|
| HeroSection (Sell) | ❌ Missing | `frontend/src/components/sell/` | Landing page hero |
| BenefitsCards | ❌ Missing | `frontend/src/components/sell/` | Seller benefits |
| EligibilityChecker | ❌ Missing | `frontend/src/components/sell/` | Quick eligibility quiz |
| RequirementsChecklist | ❌ Missing | `frontend/src/components/sell/` | Downloadable checklist |
| SuccessStories | ❌ Missing | `frontend/src/components/sell/` | Cooperative testimonials |
| OrgTypeSelector | 🚧 Needs Audit | `frontend/src/components/register/` | Coop vs SE selection |
| ApplicationWizard | 🚧 Needs Audit | `frontend/src/components/register/` | Multi-step form |
| OrgInfoForm | 🚧 Needs Audit | `frontend/src/components/register/` | Organization details |
| DocumentUpload | 🚧 Needs Audit | `frontend/src/components/register/` | Document upload interface |
| DocumentPreview | 🚧 Needs Audit | `frontend/src/components/register/` | Preview modal |
| ApplicationReview | 🚧 Needs Audit | `frontend/src/components/register/` | Submission summary |
| ApplicationTimeline | ❌ Missing | `frontend/src/components/register/` | Status timeline |
| OnboardingTour | ❌ Missing | `frontend/src/components/portal/` | Guided product tour |
| GettingStartedChecklist | ❌ Missing | `frontend/src/components/portal/` | Progress checklist |

### Backend APIs
| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| POST /api/registration/cooperative | ✅ Exists | `backend/apps/registration/api.py` | Coop registration |
| POST /api/registration/social-enterprise | ✅ Exists | `backend/apps/registration/api.py` | SE registration |
| GET /api/tenant/state | ✅ Exists | `backend/apps/tenant/api.py` | Tenant state |
| GET /api/tenant/profile | ✅ Exists | `backend/apps/tenant/api.py` | Tenant profile |
| POST /api/applications | ❌ Missing | `backend/apps/tenant/api.py` | Create application |
| GET /api/applications/{id} | ❌ Missing | `backend/apps/tenant/api.py` | Application detail |
| GET /api/applications/{id}/status | ❌ Missing | `backend/apps/tenant/api.py` | Review status |
| POST /api/applications/{id}/documents | ❌ Missing | `backend/apps/tenant/api.py` | Upload document |
| GET /api/onboarding/checklist | ❌ Missing | `backend/apps/tenant/api.py` | Onboarding steps |
| GET /api/sectors | ❌ Missing | `backend/apps/core/api.py` | Business sectors |
| GET /api/org-types | ❌ Missing | `backend/apps/core/api.py` | Organization types |

### Overall Progress
- **Frontend**: 5/10 pages (50%)
- **Components**: 6/14 need audit (43%)
- **Backend**: 4/11 endpoints (36%)
