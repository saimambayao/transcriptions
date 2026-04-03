# Course Discovery to Enrollment Journey - MoroAcademy

## Overview
This journey maps the experience of a learner discovering courses on MoroAcademy, evaluating options across different training providers, and enrolling in a course that matches their professional development needs. The focus is on making course discovery intuitive and helping learners make informed enrollment decisions.

## Persona
**Name**: Fatima Salim
**Age**: 26
**Role**: Cooperative Member & Aspiring Manager
**Context**: Fatima is a member of a multi-purpose cooperative in Cotabato City. She has been involved in cooperative operations for 3 years and aspires to take on a management role. She heard about MoroAcademy from her cooperative's training officer and wants to find courses on cooperative management.
**Goals**:
- Find relevant courses on cooperative governance and management
- Compare courses from different training providers
- Enroll in a course that fits her schedule and budget
- Gain skills to qualify for a management position

## Journey Map

### Stage 1: Awareness & Entry
**User Goal**: Access MoroAcademy and understand what's available

**Actions**:
1. Receives recommendation from cooperative training officer
2. Visits MoroAcademy homepage (academy.negosyo.bangsamoro.site or /academy)
3. Scans homepage to understand the platform
4. Looks for course catalog or search functionality

**Touchpoints**:
- MoroAcademy landing page
- Hero section with value proposition
- Featured courses carousel
- Category navigation

**Emotions**: Curious, slightly uncertain about what to expect
**Pain Points**:
- May not know what specific courses exist
- Overwhelmed if too many options shown immediately
- Unclear navigation if categories aren't intuitive

**Opportunities**:
- Clear value proposition for cooperative members
- "Recommended for Coop Members" section
- Quick category filters visible above fold
- Search with autocomplete suggestions

### Stage 2: Course Discovery
**User Goal**: Find courses relevant to cooperative management

**Actions**:
1. Uses search bar to type "cooperative management"
2. Browses course catalog with filters applied
3. Filters by category: "Cooperative Development"
4. Filters by provider to see CSEA-certified courses
5. Sorts by rating or enrollment count

**Touchpoints**:
- Course catalog page (/academy/courses)
- Search bar with live suggestions
- Filter sidebar (category, provider, duration, difficulty)
- Sort dropdown
- Course cards with key information

**Emotions**: Engaged, focused on finding the right fit
**Pain Points**:
- Too many filters can be confusing
- Course titles may not clearly indicate content
- Hard to distinguish course quality
- Unclear which provider to trust

**Opportunities**:
- Smart search with course content matching
- Provider trust badges (CSEA-certified, Partner TSP)
- Quick preview on hover
- "Similar to what you viewed" suggestions
- Clear course duration and commitment indicators

### Stage 3: Course Evaluation
**User Goal**: Evaluate course details and compare options

**Actions**:
1. Clicks on "Fundamentals of Cooperative Management" course
2. Reviews course description and learning objectives
3. Checks course curriculum/module outline
4. Views instructor profile and credentials
5. Reads learner reviews and ratings
6. Checks course duration, schedule, and price
7. Opens 2-3 other courses in new tabs to compare

**Touchpoints**:
- Course detail page (/academy/courses/[slug])
- Course overview section
- Curriculum accordion
- Instructor card
- Reviews section
- Enrollment sidebar (price, duration, CTA)

**Emotions**: Analytical, comparing options, building confidence
**Pain Points**:
- Difficult to compare multiple courses side-by-side
- Reviews may be limited or absent
- Unclear what "certificate" means (is it recognized?)
- No preview of actual course content
- Price comparison across providers confusing

**Opportunities**:
- "Compare Courses" feature (select up to 3)
- Course preview video or lesson
- Certificate explanation tooltip
- Provider comparison table
- "Why learners choose this course" highlights
- Clear refund policy display

### Stage 4: Provider Comparison
**User Goal**: Decide which training provider to trust

**Actions**:
1. Clicks on provider name to view provider profile
2. Reviews provider credentials and accreditation
3. Sees other courses offered by provider
4. Compares CSEA vs. TSP vs. Cooperative-offered courses
5. Notes which courses have government recognition

**Touchpoints**:
- Provider profile page (/academy/providers/[slug])
- Provider badge/verification status
- Provider's course catalog
- Accreditation indicators

**Emotions**: Cautious, seeking validation and trust
**Pain Points**:
- Unclear difference between provider types
- Hard to verify provider legitimacy
- No clear hierarchy of course recognition

**Opportunities**:
- Provider verification badges with explanation
- "Government-Accredited" vs "Partner" vs "Community" tiers
- Provider success metrics (completion rates, satisfaction)
- Direct link to CSEA verification if applicable

### Stage 5: Enrollment Decision
**User Goal**: Complete enrollment in chosen course

**Actions**:
1. Returns to preferred course
2. Clicks "Enroll Now" button
3. If not logged in, prompted to sign in or register
4. Reviews enrollment summary (course, price, access period)
5. Selects payment method (if paid course)
6. Confirms enrollment
7. Receives confirmation and next steps

**Touchpoints**:
- Course detail page enrollment CTA
- Login/Register modal or page
- Enrollment confirmation page
- Payment gateway (if applicable)
- Confirmation email

**Emotions**: Committed, excited to start learning, slight anxiety about payment
**Pain Points**:
- Forced to register before seeing full enrollment details
- Payment process friction
- Unclear what happens after enrollment
- No option to "save for later" if not ready

**Opportunities**:
- Guest preview of enrollment flow
- Multiple payment options (GCash, bank transfer)
- Clear "What's Next" section after enrollment
- "Save to Wishlist" for later consideration
- Scholarship/subsidy indicator if applicable
- Immediate course access confirmation

### Stage 6: Post-Enrollment Onboarding
**User Goal**: Start learning immediately and know what to expect

**Actions**:
1. Directed to course dashboard or first lesson
2. Views welcome message from instructor
3. Understands course structure and timeline
4. Sets personal learning schedule/reminders
5. Bookmarks course for easy access

**Touchpoints**:
- Course player/learning page
- Welcome module or video
- Progress dashboard
- Notification preferences
- My Courses section

**Emotions**: Excited, motivated, ready to learn
**Pain Points**:
- Not knowing where to start
- Overwhelming amount of content
- No clear timeline or milestones
- Feeling alone in the learning journey

**Opportunities**:
- Guided first-time experience
- Quick start guide overlay
- Suggested learning schedule
- Community/cohort introduction
- "Start First Lesson" prominent CTA

## Success Metrics
- **Discovery to Enrollment Conversion Rate**: % of visitors who enroll in a course
- **Search Success Rate**: % of searches that lead to course view
- **Course View to Enrollment Rate**: % of course views that convert to enrollment
- **Time to Enrollment**: Average time from first visit to enrollment
- **Provider Trust Score**: Rating of provider clarity in user surveys
- **Wishlist Usage**: Number of courses saved for later consideration

## Implementation Status (Legacy)
| Feature | Status |
|---------|--------|
| Course catalog page | 🚧 In Progress |
| Course search with filters | 🚧 In Progress |
| Course detail page | 🚧 In Progress |
| Provider profile page | ❌ Not Started |
| Course comparison tool | ❌ Not Started |
| Wishlist/Save for later | ❌ Not Started |
| Provider verification badges | ❌ Not Started |
| Course preview/sample content | ❌ Not Started |
| Enrollment flow | 🚧 In Progress |
| Post-enrollment onboarding | ❌ Not Started |

## Implementation Status

*Audited: December 30, 2025*

### Frontend Pages
| Page | Status | Path | Notes |
|------|--------|------|-------|
| MoroAcademy Landing | ✅ Exists | `frontend/src/app/(academy)/academy/page.tsx` | Homepage with featured courses |
| Course Catalog | ✅ Exists | `frontend/src/app/(academy)/academy/courses/page.tsx` | Course listing page |
| Course Detail | ✅ Exists | `frontend/src/app/(academy)/academy/courses/[slug]/page.tsx` | Individual course view |
| Provider Directory | ✅ Exists | `frontend/src/app/(academy)/academy/providers/page.tsx` | Provider listing |
| Provider Profile | ✅ Exists | `frontend/src/app/(academy)/academy/providers/[slug]/page.tsx` | Individual provider view |
| Login Page | ✅ Exists | `frontend/src/app/(academy)/academy/login/page.tsx` | Academy authentication |
| Register Page | ✅ Exists | `frontend/src/app/(academy)/academy/register/page.tsx` | Academy registration |
| My Learning | ✅ Exists | `frontend/src/app/(academy)/academy/my-learning/page.tsx` | Enrolled courses dashboard |

### Components
| Component | Status | Path | Notes |
|-----------|--------|------|-------|
| Course Card | 🚧 Partial | `frontend/src/components/academy/` | Needs audit for implementation |
| Course Filters | 🚧 Partial | `frontend/src/components/academy/` | Needs audit for implementation |
| Provider Badge | ❌ Missing | - | Trust badges not implemented |
| Wishlist Button | ❌ Missing | - | Save for later not implemented |
| Enrollment Sidebar | 🚧 Partial | - | Needs audit for implementation |

### Backend APIs
| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| GET /training/public/courses | ✅ Exists | `backend/apps/training/api.py` | Course listing |
| GET /training/public/courses/{slug} | ✅ Exists | `backend/apps/training/api.py` | Course detail |
| GET /training/public/categories | ✅ Exists | `backend/apps/training/api.py` | Course categories |
| GET /training/tenant/enrollments | ✅ Exists | `backend/apps/training/api.py` | User enrollments |
| POST /training/tenant/enrollments | 🚧 Partial | `backend/apps/training/api.py` | Enrollment creation |
| GET /training/public/courses/{id}/reviews | ✅ Exists | `backend/apps/training/api.py` | Course reviews |
| Wishlist endpoints | ❌ Missing | - | Save for later not implemented |

### Overall Progress
- **Frontend**: 8/10 core pages (80%)
- **Backend**: 5/7 core endpoints (71%)
- **Key Missing**: Wishlist, Provider trust badges, Course comparison tool

## Recommendations

### Priority 1: Foundation
1. **Complete Course Catalog with Search**: Implement full-text search with category and provider filters
2. **Course Detail Page Polish**: Ensure curriculum, instructor, and reviews sections are complete
3. **Clear Provider Indicators**: Add badges distinguishing CSEA, TSP, and Cooperative providers

### Priority 2: Trust Building
4. **Provider Profiles**: Create dedicated pages for training providers with credentials
5. **Learner Reviews**: Enable and display authentic course reviews with ratings
6. **Certificate Clarity**: Explain what certificates mean and their recognition

### Priority 3: Conversion Optimization
7. **Course Preview**: Allow preview of first lesson or intro video before enrollment
8. **Wishlist Feature**: Let users save courses for later consideration
9. **Comparison Tool**: Enable side-by-side course comparison

### Priority 4: Engagement
10. **Post-Enrollment Onboarding**: Guide new enrollees to start learning immediately
11. **Personalized Recommendations**: Suggest courses based on interests and history
12. **Learning Path Suggestions**: Group courses into recommended sequences

---

## Implementation Plan

### Phase 1: Frontend Foundation
**Pages** (under `frontend/src/app/(academy)/...`):
- `academy/page.tsx` - MoroAcademy landing page with hero, featured courses, categories
- `academy/courses/page.tsx` - Course catalog with search, filters, and pagination
- `academy/courses/[slug]/page.tsx` - Course detail page with curriculum, instructor, reviews
- `academy/providers/page.tsx` - Training providers directory
- `academy/providers/[slug]/page.tsx` - Provider profile with credentials and courses

**Components** (under `frontend/src/components/academy/...`):
- `course-card.tsx` - Course preview card with thumbnail, title, provider, rating
- `course-filters.tsx` - Filter sidebar (category, provider, level, duration)
- `course-search.tsx` - Search bar with autocomplete suggestions
- `provider-badge.tsx` - Trust badge component (CSEA-certified, Partner TSP)
- `curriculum-accordion.tsx` - Expandable course curriculum display
- `instructor-card.tsx` - Instructor profile card with credentials
- `review-list.tsx` - Course reviews and ratings display
- `enrollment-sidebar.tsx` - Sticky sidebar with price, duration, enroll CTA
- `wishlist-button.tsx` - Save course for later functionality

### Phase 2: State & Services
**Hooks** (under `frontend/src/lib/hooks/academy/...`):
- `use-courses.ts` - TanStack Query hook for fetching course list with filters
- `use-course-detail.ts` - Hook for single course data with curriculum
- `use-providers.ts` - Hook for provider list and details
- `use-course-search.ts` - Hook for search with debounce and suggestions
- `use-wishlist.ts` - Hook for managing saved courses
- `use-enrollment.ts` - Hook for enrollment flow and status

**Services** (under `frontend/src/lib/services/academy/...`):
- `course-service.ts` - API calls for courses (list, detail, search)
- `provider-service.ts` - API calls for providers
- `enrollment-service.ts` - API calls for enrollment actions
- `wishlist-service.ts` - API calls for wishlist management

**Types** (under `frontend/src/lib/types/academy/...`):
- `course.ts` - Course, Module, Lesson, Review types
- `provider.ts` - Provider, Instructor types
- `enrollment.ts` - Enrollment status, payment types

### Phase 3: Backend Integration
**Django Ninja Endpoints** (in `backend/apps/training/api.py`):
- `GET /api/training/courses` - List courses with filters (category, provider, level)
- `GET /api/training/courses/{slug}` - Course detail with curriculum and reviews
- `GET /api/training/courses/search` - Full-text search with suggestions
- `GET /api/training/providers` - List verified providers
- `GET /api/training/providers/{slug}` - Provider profile with courses
- `POST /api/training/enrollments` - Create enrollment
- `GET /api/training/wishlist` - Get user's saved courses
- `POST /api/training/wishlist/{course_id}` - Add to wishlist
- `DELETE /api/training/wishlist/{course_id}` - Remove from wishlist

**Schemas** (in `backend/apps/training/schemas.py`):
- `CourseListSchema` - Course summary for catalog
- `CourseDetailSchema` - Full course with curriculum, instructor, reviews
- `ProviderSchema` - Provider profile with verification status
- `EnrollmentCreateSchema` - Enrollment request payload
- `ReviewSchema` - Course review with rating

### Phase 4: Polish & UX
- Loading skeletons for course cards and detail page
- Empty states for no search results, empty wishlist
- Error boundaries for failed API calls
- Optimistic updates for wishlist actions
- Smooth transitions between catalog and detail views
- Responsive design for mobile course browsing
- Accessibility: proper ARIA labels, keyboard navigation

### Implementation Sequence
1. Course catalog page with static data (frontend structure)
2. Course card component and filter sidebar
3. Course detail page layout with curriculum accordion
4. Backend API endpoints for courses and providers
5. Connect frontend to backend with TanStack Query
6. Search functionality with autocomplete
7. Provider profile pages
8. Enrollment flow with authentication check
9. Wishlist feature (save for later)
10. Reviews display and submission
11. Polish: loading states, error handling, animations
