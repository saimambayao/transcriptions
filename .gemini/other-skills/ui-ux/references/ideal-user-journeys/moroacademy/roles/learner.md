# Learner - MoroAcademy

## Overview
Learners are authenticated users who actively engage with MoroAcademy's educational content. They can enroll in courses, attend workshops, track their progress, earn certificates, and interact with instructors and peers. Learners may learn from multiple providers across the platform.

## Role Definition
**Type**: Learner
**Portal Access**: Full academy access (`/academy/*`)
**Authentication**: Email/password or social login
**Provider Scope**: GLOBAL - can enroll with any accredited provider

## Capabilities

### Core Capabilities
| Capability | Description | Priority |
|------------|-------------|----------|
| Enroll in Courses | Join any published course (free or paid) | P0 |
| Access Course Content | View lessons, videos, downloads | P0 |
| Track Progress | See completion status across all courses | P0 |
| Complete Assessments | Take quizzes and submit assignments | P0 |
| Earn Certificates | Receive certificates upon completion | P0 |
| Register for Workshops | Sign up for live training sessions | P0 |
| Attend Workshops | Join virtual or in-person sessions | P0 |
| Access My Learning | Personal dashboard for all enrollments | P0 |
| Leave Reviews | Rate and review completed courses | P1 |
| Join Discussions | Participate in course forums | P1 |
| Download Resources | Access course materials offline | P1 |
| Bookmark Content | Save courses and lessons for later | P1 |
| Receive Notifications | Get updates on courses and deadlines | P1 |
| View Certificate Portfolio | Manage earned credentials | P2 |
| Share Achievements | Post certificates to social media | P2 |
| Request Access Codes | Apply for exclusive course access | P2 |
| Provide Feedback | Submit course improvement suggestions | P3 |

### Feature Access Matrix
| Feature | Access Level | Notes |
|---------|--------------|-------|
| Course Catalog | Full | Browse and enroll |
| Course Content | Full | Access enrolled courses only |
| Workshop Registration | Full | Register for available workshops |
| My Learning Dashboard | Full | Personal learning hub |
| Progress Tracking | Full | All enrollments tracked |
| Certificates | Full | Earn and download |
| Course Reviews | Full | Read and write for completed courses |
| Discussion Forums | Full | Participate in enrolled courses |
| Instructor Messaging | Partial | Q&A through platform, no direct DM |
| Course Creation | None | Learner only |
| Analytics | Partial | Personal stats only |
| Admin Functions | None | No platform administration |

## User Journey Entry Points
1. **Login** - Returning learner accessing their dashboard
2. **Email Notification** - Course update or deadline reminder
3. **Enrollment Completion** - Redirect after successful enrollment
4. **Shared Link** - Course link shared by peer or instructor
5. **Search Result** - Finding course through internal search
6. **Provider Recommendation** - Course suggested by their cooperative/SE

## Key Pages
| Page | Purpose | Implementation |
|------|---------|----------------|
| My Learning `/academy/my-learning` | Dashboard with enrolled courses | Planned |
| Course Player `/academy/learn/[slug]` | Main learning interface | Planned |
| Lesson View `/academy/learn/[slug]/[lesson]` | Individual lesson content | Planned |
| Assessment `/academy/learn/[slug]/quiz/[id]` | Quiz/assessment interface | Planned |
| My Workshops `/academy/my-workshops` | Enrolled workshops list | Planned |
| Workshop Room `/academy/workshop/[id]/live` | Live session interface | Planned |
| My Certificates `/academy/certificates` | Certificate portfolio | Planned |
| Certificate View `/academy/certificates/[id]` | Individual certificate | Planned |
| Profile `/academy/profile` | Learner profile settings | Planned |
| Course Discussion `/academy/learn/[slug]/discussion` | Forum for course | Planned |
| Bookmarks `/academy/bookmarks` | Saved content | Planned |
| Notifications `/academy/notifications` | Alert center | Planned |

## Role Progression
**From**: Anonymous User (via registration)
**To**:
- Instructor (if invited by provider)
- Coop Training Coordinator (if appointed by cooperative)
- SE Training Coordinator (if appointed by social enterprise)
- TSP Admin (if establishing training service provider)

**Requirements**:
- **To Instructor**: Invitation from existing provider + expertise verification
- **To Coordinator**: Appointment by cooperative/SE management
- **To TSP Admin**: TSP registration and accreditation approval

## Pain Points
1. **Multi-Provider Confusion** - Difficulty managing courses from different providers
2. **Progress Not Syncing** - Progress sometimes doesn't save properly
3. **Certificate Delays** - Waiting for manual certificate issuance
4. **Workshop Scheduling** - Conflicts with work or personal schedule
5. **Content Accessibility** - Videos without captions, poor mobile experience
6. **Limited Offline Access** - Cannot learn without internet connection
7. **No Learning Path** - Unclear what to learn next after completing a course
8. **Assessment Feedback** - Insufficient explanation for wrong answers
9. **Expired Access** - Losing access to course content after completion

## Improvement Opportunities
1. **Unified Dashboard** - Single view of all enrollments regardless of provider
2. **Offline Mode** - Download content for offline learning
3. **Learning Paths** - Curated sequences of courses by skill/career goal
4. **Auto-Certificates** - Immediate issuance upon completion
5. **Mobile App** - Native app for better mobile learning experience
6. **Smart Notifications** - AI-driven reminders based on learning patterns
7. **Peer Study Groups** - Connect learners in same course
8. **Skill Badges** - Micro-credentials for specific competencies
9. **Calendar Integration** - Sync workshop schedules with personal calendar
10. **Accessibility Features** - Captions, transcripts, screen reader support

## Success Metrics
- **Course Completion Rate**: Percentage of enrolled courses completed
- **Time to Completion**: Average days from enrollment to certificate
- **Workshop Attendance Rate**: Percentage of registered workshops attended
- **Certificate Earn Rate**: Certificates earned per learner per year
- **Engagement Score**: Composite of logins, time spent, interactions
- **Re-enrollment Rate**: Percentage taking additional courses
- **Net Promoter Score**: Likelihood to recommend platform
- **Content Consumption**: Lessons viewed, videos watched, resources downloaded

## Learning Experience Flow
```
Enrollment -> Welcome -> First Lesson -> Progress -> Assessment ->
Completion -> Certificate -> Review -> Recommend/Re-enroll
```

## UI/UX Considerations
- Clean, distraction-free learning interface
- Clear progress indicators (progress bars, checkmarks)
- Easy navigation between lessons
- Responsive design for mobile learning
- Dark mode option for extended reading
- Keyboard navigation support
- Quick access to help/support
- Celebration animations for achievements
- Persistent video player position
- Note-taking functionality within courses

---

## Implementation Plan

### Access Control
- Authentication required for all `/academy/my-*` and `/academy/learn/*` routes
- Middleware: `withAuth` HOC or route middleware checking session
- Enrollment verification for course content access
- Global access - learners can enroll with ANY provider's courses
- No tenant/provider scoping - learner sees all their enrollments across providers

### Priority Pages
| Priority | Page | Route | File Path |
|----------|------|-------|-----------|
| P0 | My Learning | `/academy/my-learning` | `frontend/src/app/(academy)/academy/my-learning/page.tsx` |
| P0 | Course Player | `/academy/learn/[slug]` | `frontend/src/app/(academy)/academy/learn/[slug]/page.tsx` |
| P0 | Lesson View | `/academy/learn/[slug]/[lesson]` | `frontend/src/app/(academy)/academy/learn/[slug]/[lesson]/page.tsx` |
| P0 | Assessment | `/academy/learn/[slug]/quiz/[id]` | `frontend/src/app/(academy)/academy/learn/[slug]/quiz/[id]/page.tsx` |
| P0 | My Workshops | `/academy/my-workshops` | `frontend/src/app/(academy)/academy/my-workshops/page.tsx` |
| P1 | Workshop Room | `/academy/workshop/[id]/live` | `frontend/src/app/(academy)/academy/workshop/[id]/live/page.tsx` |
| P1 | My Certificates | `/academy/certificates` | `frontend/src/app/(academy)/academy/certificates/page.tsx` |
| P1 | Certificate View | `/academy/certificates/[id]` | `frontend/src/app/(academy)/academy/certificates/[id]/page.tsx` |
| P1 | Course Discussion | `/academy/learn/[slug]/discussion` | `frontend/src/app/(academy)/academy/learn/[slug]/discussion/page.tsx` |
| P2 | Learner Profile | `/academy/profile` | `frontend/src/app/(academy)/academy/profile/page.tsx` |
| P2 | Bookmarks | `/academy/bookmarks` | `frontend/src/app/(academy)/academy/bookmarks/page.tsx` |
| P2 | Notifications | `/academy/notifications` | `frontend/src/app/(academy)/academy/notifications/page.tsx` |

### Role-Specific Components
| Component | Purpose | File Path |
|-----------|---------|-----------|
| `LearnerDashboard` | My Learning overview with progress | `frontend/src/components/academy/learner/LearnerDashboard.tsx` |
| `EnrolledCourseCard` | Course card with progress indicator | `frontend/src/components/academy/learner/EnrolledCourseCard.tsx` |
| `CoursePlayer` | Main learning interface wrapper | `frontend/src/components/academy/learner/CoursePlayer.tsx` |
| `LessonContent` | Lesson display (video, text, etc.) | `frontend/src/components/academy/learner/LessonContent.tsx` |
| `VideoPlayer` | Video player with progress tracking | `frontend/src/components/academy/learner/VideoPlayer.tsx` |
| `LessonSidebar` | Course navigation sidebar | `frontend/src/components/academy/learner/LessonSidebar.tsx` |
| `ProgressBar` | Course completion progress | `frontend/src/components/academy/learner/ProgressBar.tsx` |
| `QuizInterface` | Quiz taking interface | `frontend/src/components/academy/learner/QuizInterface.tsx` |
| `CertificateCard` | Certificate display card | `frontend/src/components/academy/learner/CertificateCard.tsx` |
| `CertificateViewer` | Full certificate view with download | `frontend/src/components/academy/learner/CertificateViewer.tsx` |
| `WorkshopEnrollmentCard` | Enrolled workshop card | `frontend/src/components/academy/learner/WorkshopEnrollmentCard.tsx` |
| `DiscussionThread` | Course discussion interface | `frontend/src/components/academy/learner/DiscussionThread.tsx` |
| `NoteTaker` | In-lesson note-taking | `frontend/src/components/academy/learner/NoteTaker.tsx` |

### API Endpoints Required
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/academy/my/enrollments` | List learner's enrolled courses |
| POST | `/api/v1/academy/courses/{slug}/enroll` | Enroll in a course |
| GET | `/api/v1/academy/learn/{slug}` | Get course content for enrolled learner |
| GET | `/api/v1/academy/learn/{slug}/lessons/{id}` | Get specific lesson content |
| POST | `/api/v1/academy/learn/{slug}/lessons/{id}/complete` | Mark lesson complete |
| GET | `/api/v1/academy/learn/{slug}/progress` | Get learner's course progress |
| GET | `/api/v1/academy/learn/{slug}/quiz/{id}` | Get quiz questions |
| POST | `/api/v1/academy/learn/{slug}/quiz/{id}/submit` | Submit quiz answers |
| GET | `/api/v1/academy/my/workshops` | List enrolled workshops |
| POST | `/api/v1/academy/workshops/{id}/register` | Register for workshop |
| GET | `/api/v1/academy/my/certificates` | List earned certificates |
| GET | `/api/v1/academy/certificates/{id}` | Get certificate details |
| GET | `/api/v1/academy/certificates/{id}/download` | Download certificate PDF |
| GET | `/api/v1/academy/learn/{slug}/discussions` | Get course discussions |
| POST | `/api/v1/academy/learn/{slug}/discussions` | Post to discussion |
| GET | `/api/v1/academy/my/bookmarks` | Get bookmarked courses |
| POST | `/api/v1/academy/courses/{slug}/bookmark` | Bookmark a course |
| GET | `/api/v1/academy/my/notifications` | Get learner notifications |

### Implementation Sequence
1. **Phase 1: Learning Dashboard**
   - My Learning page with enrolled courses
   - Enrollment API integration
   - Progress tracking display

2. **Phase 2: Course Player**
   - Course player layout with sidebar navigation
   - Lesson content display (text, video)
   - Video player with progress tracking
   - Lesson completion marking

3. **Phase 3: Assessments**
   - Quiz interface with question types
   - Quiz submission and grading
   - Results display with feedback

4. **Phase 4: Workshops**
   - My Workshops page
   - Workshop registration flow
   - Live workshop room integration

5. **Phase 5: Certificates**
   - My Certificates page
   - Certificate viewing and download
   - Certificate sharing functionality

6. **Phase 6: Engagement Features**
   - Course discussions/forums
   - Bookmarks functionality
   - Notifications system
   - Note-taking feature

---

## Implementation Status

*Audited: December 30, 2025*

### Key Pages Status
| Page | Status | Path | Notes |
|------|--------|------|-------|
| My Learning | ✅ Implemented | `frontend/src/app/(academy)/academy/my-learning/page.tsx` | Learner dashboard |
| Course Player | ❌ Not Implemented | `frontend/src/app/(academy)/academy/learn/[slug]/page.tsx` | Main learning interface missing |
| Lesson View | ❌ Not Implemented | `frontend/src/app/(academy)/academy/learn/[slug]/[lesson]/page.tsx` | Lesson content missing |
| Assessment | ❌ Not Implemented | `frontend/src/app/(academy)/academy/learn/[slug]/quiz/[id]/page.tsx` | Quiz interface missing |
| My Workshops | ❌ Not Implemented | `frontend/src/app/(academy)/academy/my-workshops/page.tsx` | Enrolled workshops missing |
| Workshop Room | ✅ Implemented | `frontend/src/app/(academy)/academy/programs/[slug]/live/page.tsx` | Live session via programs |
| Workshop Attend | ✅ Implemented | `frontend/src/app/(academy)/academy/programs/[slug]/attend/page.tsx` | Attendance page |
| Workshop Simulation | ✅ Implemented | `frontend/src/app/(academy)/academy/programs/[slug]/simulation/page.tsx` | Simulation mode |
| My Certificates | ❌ Not Implemented | `frontend/src/app/(academy)/academy/certificates/page.tsx` | Certificate portfolio missing |
| Profile | ✅ Implemented | `frontend/src/app/(academy)/academy/profile/page.tsx` | Learner profile |
| Join (Access Code) | ✅ Implemented | `frontend/src/app/(academy)/academy/join/page.tsx` | Access code entry |
| Join Phone | ✅ Implemented | `frontend/src/app/(academy)/academy/join/phone/page.tsx` | Phone verification |
| Join Complete | ✅ Implemented | `frontend/src/app/(academy)/academy/join/complete/page.tsx` | Registration complete |
| Join Upgrade | ✅ Implemented | `frontend/src/app/(academy)/academy/join/upgrade/page.tsx` | Account upgrade |

### API Endpoints Status
| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| GET `/training/tenant/enrollments` | ✅ Implemented | `backend/apps/training/api.py` | List enrollments |
| GET `/training/tenant/progress` | ✅ Implemented | `backend/apps/training/api.py` | Learning progress |
| GET `/training/tenant/certificates` | ✅ Implemented | `backend/apps/training/api.py` | Certificates |
| GET `/training/tenant/badges` | ✅ Implemented | `backend/apps/training/api.py` | Earned badges |
| POST `/training/tenant/reviews` | ✅ Implemented | `backend/apps/training/api.py` | Submit reviews |
| GET `/training/tenant/lessons/comments` | ✅ Implemented | `backend/apps/training/api.py` | Lesson comments |
| GET `/training/academy/my-learning` | ✅ Implemented | `backend/apps/training/api.py` | My learning data |
| GET `/accounts/access/validate-code` | ✅ Implemented | `backend/apps/accounts/api.py` | Validate access code |
| POST `/accounts/access/redeem-code` | ✅ Implemented | `backend/apps/accounts/api.py` | Redeem access code |
| POST `/accounts/access/phone-otp` | ✅ Implemented | `backend/apps/accounts/api.py` | Phone OTP |
| POST `/accounts/access/upgrade-account` | ✅ Implemented | `backend/apps/accounts/api.py` | Account upgrade |
| POST `/api/v1/academy/courses/{slug}/enroll` | ❌ Not Implemented | - | Course enrollment action |
| GET `/api/v1/academy/learn/{slug}/lessons/{id}` | ❌ Not Implemented | - | Lesson content |
| POST `/api/v1/academy/learn/{slug}/lessons/{id}/complete` | ❌ Not Implemented | - | Mark lesson complete |

### Overall Progress
- **Pages**: 10/14 implemented (71%)
- **APIs**: 11/14 implemented (79%)
