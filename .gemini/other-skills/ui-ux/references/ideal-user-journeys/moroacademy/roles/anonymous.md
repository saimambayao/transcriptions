# Anonymous User - MoroAcademy

## Overview
Anonymous users are visitors who browse MoroAcademy without logging in. They can explore the course catalog, view workshop schedules, and learn about training providers, but cannot enroll or track progress. The primary goal is to convert them into registered learners.

## Role Definition
**Type**: Anonymous
**Portal Access**: Public-facing academy pages only (`/academy`)
**Authentication**: None required
**Provider Scope**: N/A - read-only access

## Capabilities

### Core Capabilities
| Capability | Description | Priority |
|------------|-------------|----------|
| Browse Course Catalog | View all published courses with filters | P0 |
| View Course Details | See course overview, curriculum, requirements | P0 |
| Browse Workshop Schedule | View upcoming workshops and events | P0 |
| View Provider Profiles | Explore TSPs, Coops, SEs offering training | P0 |
| Search Content | Search courses, workshops, providers | P0 |
| View Pricing | See course/workshop fees if applicable | P1 |
| Preview Course Content | Watch sample videos or lessons | P1 |
| View Provider Ratings | See reviews and ratings from learners | P2 |
| Compare Courses | Side-by-side course comparison | P3 |

### Feature Access Matrix
| Feature | Access Level | Notes |
|---------|--------------|-------|
| Course Catalog | Full | Can browse all published courses |
| Course Details | Partial | Overview only, no lesson content |
| Workshop Listings | Full | Can view all upcoming workshops |
| Provider Directory | Full | Can browse all accredited providers |
| Enrollment | None | Redirects to login/register |
| Progress Tracking | None | Requires authentication |
| Certificates | None | Requires authentication |
| My Learning Dashboard | None | Requires authentication |
| Course Reviews | Partial | Can read, cannot write |
| Discussion Forums | None | Requires authentication |

## User Journey Entry Points
1. **Search Engine** - Discovers MoroAcademy through Google search for Bangsamoro training
2. **Negosyo Marketplace** - Clicks "Learn More" link from cooperative/SE product page
3. **Direct URL** - Navigates directly to moroacademy.ph or negosyo.bangsamoro.site/academy
4. **Social Media** - Follows link from CSEA social media posts about training programs
5. **Referral** - Receives shared course link from existing learner

## Key Pages
| Page | Purpose | Implementation |
|------|---------|----------------|
| Academy Home `/academy` | Landing page with featured courses | Planned |
| Course Catalog `/academy/courses` | Browse all courses | Planned |
| Course Detail `/academy/courses/[slug]` | View course information | Planned |
| Workshop Listings `/academy/workshops` | Browse upcoming workshops | Planned |
| Workshop Detail `/academy/workshops/[id]` | View workshop information | Planned |
| Provider Directory `/academy/providers` | Browse training providers | Planned |
| Provider Profile `/academy/providers/[slug]` | View provider details | Planned |
| Search Results `/academy/search` | Search results page | Planned |
| Login `/academy/login` | Authentication entry point | Planned |
| Register `/academy/register` | New learner registration | Planned |

## Role Progression
**From**: N/A (entry point)
**To**: Learner (primary), Instructor, TSP Admin, Coop Training Coordinator, SE Training Coordinator
**Requirements**:
- **To Learner**: Complete registration with email verification
- **To Provider Roles**: Register as learner first, then apply for provider role

## Pain Points
1. **No Quick Preview** - Cannot sample course content without registering
2. **Limited Information** - Course details may not fully convey value proposition
3. **Registration Friction** - Multiple steps to become a learner
4. **No Wishlist** - Cannot save courses of interest without account
5. **Provider Discovery** - Difficult to find the right training provider
6. **No Recommendations** - Cannot receive personalized course suggestions

## Improvement Opportunities
1. **Guest Preview** - Allow preview of first lesson without registration
2. **One-Click Registration** - Simplify signup with social login options
3. **Course Comparison Tool** - Enable side-by-side course evaluation
4. **Interest Tracking** - Allow anonymous wishlisting with local storage
5. **Smart Search** - AI-powered search with natural language queries
6. **Provider Matching** - Quiz to match anonymous users with suitable providers
7. **Exit Intent Capture** - Offer value (e.g., free course) before leaving
8. **Social Proof** - Display learner testimonials and success stories prominently

## Success Metrics
- **Conversion Rate**: Percentage of anonymous visitors who register as learners
- **Bounce Rate**: Percentage leaving without exploring multiple pages
- **Pages per Session**: Average pages viewed before leaving or registering
- **Time on Site**: Average duration of anonymous browsing session
- **Search Engagement**: Percentage using search functionality
- **Course Detail Views**: Average course pages viewed per session
- **Registration Start Rate**: Percentage who begin but may not complete registration

## Conversion Triggers
1. **Enrollment CTA** - "Enroll Now" button on course detail prompts login
2. **Workshop Registration** - Attempting to register for workshop triggers signup
3. **Content Gate** - Premium content requires authentication
4. **Progress Saving** - Prompt to save progress requires account
5. **Certificate Interest** - Viewing certificate examples encourages registration
6. **Community Access** - Discussion forum participation requires login

## UI/UX Considerations
- Clear value proposition on landing page
- Prominent but non-intrusive registration CTAs
- Mobile-first responsive design
- Fast page loads for browsing experience
- Trust signals (accreditation badges, learner count)
- Clear navigation between catalog, workshops, and providers
- Accessibility compliance for all users

---

## Implementation Plan

### Access Control
- No authentication required - public routes only
- No middleware needed for anonymous access
- Rate limiting on search endpoints to prevent abuse
- Analytics tracking for conversion optimization

### Priority Pages
| Priority | Page | Route | File Path |
|----------|------|-------|-----------|
| P0 | Academy Home | `/academy` | `frontend/src/app/(academy)/academy/page.tsx` |
| P0 | Course Catalog | `/academy/courses` | `frontend/src/app/(academy)/academy/courses/page.tsx` |
| P0 | Course Detail | `/academy/courses/[slug]` | `frontend/src/app/(academy)/academy/courses/[slug]/page.tsx` |
| P0 | Workshop Listings | `/academy/workshops` | `frontend/src/app/(academy)/academy/workshops/page.tsx` |
| P0 | Workshop Detail | `/academy/workshops/[id]` | `frontend/src/app/(academy)/academy/workshops/[id]/page.tsx` |
| P0 | Provider Directory | `/academy/providers` | `frontend/src/app/(academy)/academy/providers/page.tsx` |
| P0 | Provider Profile | `/academy/providers/[slug]` | `frontend/src/app/(academy)/academy/providers/[slug]/page.tsx` |
| P1 | Search Results | `/academy/search` | `frontend/src/app/(academy)/academy/search/page.tsx` |
| P1 | Login | `/academy/login` | `frontend/src/app/(academy)/academy/login/page.tsx` |
| P1 | Register | `/academy/register` | `frontend/src/app/(academy)/academy/register/page.tsx` |

### Role-Specific Components
| Component | Purpose | File Path |
|-----------|---------|-----------|
| `AcademyHero` | Landing page hero with value proposition | `frontend/src/components/academy/AcademyHero.tsx` |
| `FeaturedCourses` | Carousel of featured/popular courses | `frontend/src/components/academy/FeaturedCourses.tsx` |
| `CourseCard` | Course preview card for catalog | `frontend/src/components/academy/CourseCard.tsx` |
| `WorkshopCard` | Workshop preview card | `frontend/src/components/academy/WorkshopCard.tsx` |
| `ProviderCard` | Provider preview card | `frontend/src/components/academy/ProviderCard.tsx` |
| `CourseFilters` | Filter panel for course catalog | `frontend/src/components/academy/CourseFilters.tsx` |
| `SearchBar` | Global academy search component | `frontend/src/components/academy/SearchBar.tsx` |
| `CTABanner` | Registration call-to-action banner | `frontend/src/components/academy/CTABanner.tsx` |
| `TrustSignals` | Accreditation badges and stats | `frontend/src/components/academy/TrustSignals.tsx` |
| `CoursePreview` | Limited course content preview | `frontend/src/components/academy/CoursePreview.tsx` |

### API Endpoints Required
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/academy/courses` | List published courses with filters |
| GET | `/api/v1/academy/courses/{slug}` | Get course detail (public view) |
| GET | `/api/v1/academy/workshops` | List upcoming workshops |
| GET | `/api/v1/academy/workshops/{id}` | Get workshop detail |
| GET | `/api/v1/academy/providers` | List accredited providers |
| GET | `/api/v1/academy/providers/{slug}` | Get provider profile |
| GET | `/api/v1/academy/search` | Global search across courses, workshops, providers |
| GET | `/api/v1/academy/categories` | Get course categories |
| GET | `/api/v1/academy/stats` | Platform statistics for trust signals |

### Implementation Sequence
1. **Phase 1: Core Infrastructure**
   - Set up academy route group `(academy)`
   - Create academy layout with navigation
   - Implement base components (CourseCard, WorkshopCard, ProviderCard)

2. **Phase 2: Catalog Pages**
   - Academy home page with featured content
   - Course catalog with filters and pagination
   - Workshop listings with date filtering
   - Provider directory

3. **Phase 3: Detail Pages**
   - Course detail page (overview, curriculum, requirements)
   - Workshop detail page (schedule, instructor, registration CTA)
   - Provider profile page (courses, workshops, about)

4. **Phase 4: Search & Discovery**
   - Global search functionality
   - Search results page with filtering
   - Category navigation

5. **Phase 5: Conversion Optimization**
   - Registration/login pages
   - CTA banners and enrollment prompts
   - Trust signals and social proof elements

---

## Implementation Status

*Audited: December 30, 2025*

### Key Pages Status
| Page | Status | Path | Notes |
|------|--------|------|-------|
| Academy Home | ✅ Implemented | `frontend/src/app/(academy)/academy/page.tsx` | Landing page exists |
| Course Catalog | ✅ Implemented | `frontend/src/app/(academy)/academy/courses/page.tsx` | Browse all courses |
| Course Detail | ✅ Implemented | `frontend/src/app/(academy)/academy/courses/[slug]/page.tsx` | Individual course view |
| Workshop Listings | ✅ Implemented | `frontend/src/app/(academy)/academy/workshops/page.tsx` | Browse workshops |
| Workshop Detail | ✅ Implemented | `frontend/src/app/(academy)/academy/workshops/[slug]/page.tsx` | Individual workshop view |
| Provider Directory | ✅ Implemented | `frontend/src/app/(academy)/academy/providers/page.tsx` | Browse providers |
| Provider Profile | ✅ Implemented | `frontend/src/app/(academy)/academy/providers/[slug]/page.tsx` | Individual provider view |
| Search Results | ❌ Not Implemented | `frontend/src/app/(academy)/academy/search/page.tsx` | Global search page missing |
| Login | ✅ Implemented | `frontend/src/app/(academy)/academy/login/page.tsx` | Authentication entry |
| Register | ✅ Implemented | `frontend/src/app/(academy)/academy/register/page.tsx` | New learner registration |

### API Endpoints Status
| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| GET `/training/public/courses` | ✅ Implemented | `backend/apps/training/api.py` | List published courses |
| GET `/training/public/courses/{slug}` | ✅ Implemented | `backend/apps/training/api.py` | Course detail |
| GET `/training/public/categories` | ✅ Implemented | `backend/apps/training/api.py` | Course categories |
| GET `/training/public/courses/{id}/reviews` | ✅ Implemented | `backend/apps/training/api.py` | Course reviews |
| GET `/api/v1/academy/workshops` | 🚧 Partial | - | May need public workshops endpoint |
| GET `/api/v1/academy/providers` | 🚧 Partial | - | May need public providers endpoint |
| GET `/api/v1/academy/search` | ❌ Not Implemented | - | Global search missing |
| GET `/api/v1/academy/stats` | ❌ Not Implemented | - | Platform stats for trust signals |

### Overall Progress
- **Pages**: 8/10 implemented (80%)
- **APIs**: 4/8 implemented (50%)
