# Instructor/Facilitator - MoroAcademy

## Overview
Instructors are subject matter experts who create and deliver educational content on MoroAcademy. They develop online courses, facilitate live workshops, assess learner performance, and provide support. Instructors work under a provider (TSP, Cooperative, SE, or CSEA) and manage content within their assigned scope.

## Role Definition
**Type**: Provider
**Portal Access**: Academy instructor dashboard (`/academy/instructor/*`)
**Authentication**: Provider-linked account (email/password)
**Provider Scope**: PROVIDER - access limited to assigned provider's content

## Capabilities

### Core Capabilities
| Capability | Description | Priority |
|------------|-------------|----------|
| Create Courses | Build new courses with modules and lessons | P0 |
| Manage Content | Upload videos, documents, quizzes | P0 |
| Edit Courses | Modify existing course content | P0 |
| Facilitate Workshops | Lead live training sessions | P0 |
| Generate Access Codes | Create enrollment codes for exclusive courses | P0 |
| Track Learner Progress | View enrollment and completion data | P0 |
| Grade Assessments | Review and score assignments/quizzes | P0 |
| Issue Certificates | Approve certificate generation | P1 |
| Take Attendance | Record workshop participation | P1 |
| Answer Questions | Respond to learner inquiries | P1 |
| Moderate Discussions | Manage course forums | P1 |
| View Analytics | See course performance metrics | P1 |
| Schedule Workshops | Set dates and times for sessions | P2 |
| Create Quizzes | Build assessments with various question types | P0 |
| Manage Co-Instructors | Add/remove course collaborators | P2 |
| Export Data | Download learner data and reports | P3 |

### Feature Access Matrix
| Feature | Access Level | Notes |
|---------|--------------|-------|
| Course Creation | Full | Within assigned provider |
| Content Upload | Full | Videos, PDFs, resources |
| Workshop Management | Full | Create, schedule, facilitate |
| Access Code Generation | Full | For their courses |
| Learner Data | Partial | Own courses only |
| Certificate Issuance | Partial | Approve for own courses |
| Course Analytics | Partial | Own courses only |
| Platform Analytics | None | Provider-level only |
| Provider Settings | None | TSP/Coop/SE admin only |
| Course Publishing | Partial | Submit for approval |
| Platform Administration | None | CSEA admin only |
| Financial Reports | None | Provider admin only |

## User Journey Entry Points
1. **Instructor Dashboard** - Login to manage courses and workshops
2. **Notification Alert** - Learner question or assignment submission
3. **Calendar Reminder** - Upcoming workshop to facilitate
4. **Email Invitation** - Invited to co-instruct a course
5. **Course Builder** - Direct access to content creation tools
6. **Analytics Alert** - Course performance notification

## Key Pages
| Page | Purpose | Implementation |
|------|---------|----------------|
| Instructor Dashboard `/academy/instructor` | Overview of all teaching activities | Planned |
| My Courses `/academy/instructor/courses` | List of assigned/created courses | Planned |
| Course Builder `/academy/instructor/courses/[id]/edit` | Content creation interface | Planned |
| Lesson Editor `/academy/instructor/courses/[id]/lessons/[id]` | Edit individual lessons | Planned |
| Quiz Builder `/academy/instructor/courses/[id]/quizzes/[id]` | Create assessments | Planned |
| My Workshops `/academy/instructor/workshops` | Workshop management | Planned |
| Workshop Setup `/academy/instructor/workshops/[id]/setup` | Configure workshop | Planned |
| Workshop Room `/academy/instructor/workshops/[id]/live` | Facilitate live session | Planned |
| Attendance `/academy/instructor/workshops/[id]/attendance` | Take/view attendance | Planned |
| Access Codes `/academy/instructor/access-codes` | Manage enrollment codes | Planned |
| Learner Progress `/academy/instructor/courses/[id]/learners` | View enrolled learners | Planned |
| Submissions `/academy/instructor/submissions` | Review assignments/quizzes | Planned |
| Course Analytics `/academy/instructor/courses/[id]/analytics` | Course performance | Planned |
| Messages `/academy/instructor/messages` | Learner communications | Planned |

## Role Progression
**From**:
- Learner (invited by provider)
- External expert (direct invitation)

**To**:
- TSP Admin (if founding a TSP)
- Lead Instructor (senior role within provider)
- Curriculum Designer (specialized content role)

**Requirements**:
- Invitation from an accredited provider
- Verified expertise in subject area
- Completion of instructor orientation (if required)
- Background check (for certain content areas)

## Pain Points
1. **Complex Course Builder** - Steep learning curve for content creation
2. **Video Upload Limits** - Slow uploads, file size restrictions
3. **Limited Collaboration** - Difficult to work with co-instructors
4. **Manual Grading** - Time-consuming assessment review
5. **Workshop Tech Issues** - Connectivity problems during live sessions
6. **No Template Library** - Starting from scratch each time
7. **Fragmented Communications** - Learner questions across multiple channels
8. **Certificate Delays** - Manual approval process for each certificate
9. **Limited Analytics** - Insufficient data on learner engagement
10. **No Mobile Access** - Cannot manage courses on mobile

## Improvement Opportunities
1. **Simplified Course Builder** - Drag-and-drop interface with templates
2. **Bulk Upload** - Upload multiple videos/files at once
3. **Real-time Collaboration** - Co-edit courses with other instructors
4. **Auto-Grading** - AI-assisted quiz grading with feedback
5. **Workshop Platform** - Integrated video conferencing (no third-party)
6. **Template Library** - Pre-built course structures and lesson formats
7. **Unified Inbox** - Single location for all learner communications
8. **Batch Certificates** - Bulk issuance for completed learners
9. **Enhanced Analytics** - Engagement heatmaps, drop-off analysis
10. **Mobile Instructor App** - Manage courses and workshops on-the-go
11. **Content Versioning** - Track changes and rollback if needed
12. **Accessibility Checker** - Ensure content meets accessibility standards

## Success Metrics
- **Courses Published**: Number of courses successfully launched
- **Learner Satisfaction**: Average rating from course reviews
- **Completion Rate**: Percentage of enrollees who complete courses
- **Assessment Scores**: Average learner quiz/assignment performance
- **Response Time**: Average time to answer learner questions
- **Workshop Attendance**: Percentage of registered learners attending
- **Content Quality Score**: Composite of reviews, completions, engagement
- **Re-enrollment Rate**: Learners taking additional courses from instructor

## Content Creation Workflow
```
Outline Course -> Create Modules -> Add Lessons -> Upload Media ->
Build Assessments -> Set Access Rules -> Submit for Review ->
Publish -> Monitor & Iterate
```

## Workshop Facilitation Flow
```
Create Workshop -> Set Schedule -> Configure Access -> Promote ->
Prepare Materials -> Open Room -> Facilitate -> Take Attendance ->
Issue Certificates -> Collect Feedback -> Analyze
```

## UI/UX Considerations
- Intuitive drag-and-drop course builder
- Real-time preview of course content
- Progress indicators for course setup completion
- Easy media management (video, images, files)
- Clear distinction between draft and published content
- Accessible analytics dashboard
- Quick actions for common tasks
- Notification badges for pending items
- Calendar view for workshop scheduling
- Responsive design for tablet use during workshops

---

## Implementation Plan

### Access Control
- Authentication required with `instructor` role verification
- **Provider scoping is CRITICAL** - instructors only see their assigned provider's content
- Middleware: `withProviderAccess` checking `user.provider_id` against resource ownership
- Course/workshop access limited to instructor's assigned provider
- Cannot access other providers' courses, learners, or analytics

### Priority Pages
| Priority | Page | Route | File Path |
|----------|------|-------|-----------|
| P0 | Instructor Dashboard | `/academy/instructor` | `frontend/src/app/(academy)/academy/instructor/page.tsx` |
| P0 | My Courses | `/academy/instructor/courses` | `frontend/src/app/(academy)/academy/instructor/courses/page.tsx` |
| P0 | Course Builder | `/academy/instructor/courses/[id]/edit` | `frontend/src/app/(academy)/academy/instructor/courses/[id]/edit/page.tsx` |
| P0 | Lesson Editor | `/academy/instructor/courses/[id]/lessons/[lessonId]` | `frontend/src/app/(academy)/academy/instructor/courses/[id]/lessons/[lessonId]/page.tsx` |
| P0 | Quiz Builder | `/academy/instructor/courses/[id]/quizzes/[quizId]` | `frontend/src/app/(academy)/academy/instructor/courses/[id]/quizzes/[quizId]/page.tsx` |
| P0 | My Workshops | `/academy/instructor/workshops` | `frontend/src/app/(academy)/academy/instructor/workshops/page.tsx` |
| P1 | Workshop Setup | `/academy/instructor/workshops/[id]/setup` | `frontend/src/app/(academy)/academy/instructor/workshops/[id]/setup/page.tsx` |
| P1 | Workshop Room | `/academy/instructor/workshops/[id]/live` | `frontend/src/app/(academy)/academy/instructor/workshops/[id]/live/page.tsx` |
| P1 | Attendance | `/academy/instructor/workshops/[id]/attendance` | `frontend/src/app/(academy)/academy/instructor/workshops/[id]/attendance/page.tsx` |
| P1 | Access Codes | `/academy/instructor/access-codes` | `frontend/src/app/(academy)/academy/instructor/access-codes/page.tsx` |
| P1 | Learner Progress | `/academy/instructor/courses/[id]/learners` | `frontend/src/app/(academy)/academy/instructor/courses/[id]/learners/page.tsx` |
| P1 | Submissions | `/academy/instructor/submissions` | `frontend/src/app/(academy)/academy/instructor/submissions/page.tsx` |
| P2 | Course Analytics | `/academy/instructor/courses/[id]/analytics` | `frontend/src/app/(academy)/academy/instructor/courses/[id]/analytics/page.tsx` |
| P2 | Messages | `/academy/instructor/messages` | `frontend/src/app/(academy)/academy/instructor/messages/page.tsx` |

### Role-Specific Components
| Component | Purpose | File Path |
|-----------|---------|-----------|
| `InstructorDashboard` | Overview with pending items and stats | `frontend/src/components/academy/instructor/InstructorDashboard.tsx` |
| `CourseList` | List of instructor's courses | `frontend/src/components/academy/instructor/CourseList.tsx` |
| `CourseBuilder` | Drag-and-drop course structure builder | `frontend/src/components/academy/instructor/CourseBuilder.tsx` |
| `ModuleEditor` | Module management within course | `frontend/src/components/academy/instructor/ModuleEditor.tsx` |
| `LessonEditor` | Rich lesson content editor | `frontend/src/components/academy/instructor/LessonEditor.tsx` |
| `MediaUploader` | Video/file upload component | `frontend/src/components/academy/instructor/MediaUploader.tsx` |
| `QuizBuilder` | Quiz question builder | `frontend/src/components/academy/instructor/QuizBuilder.tsx` |
| `QuestionEditor` | Individual question editor | `frontend/src/components/academy/instructor/QuestionEditor.tsx` |
| `WorkshopScheduler` | Workshop creation and scheduling | `frontend/src/components/academy/instructor/WorkshopScheduler.tsx` |
| `AttendanceSheet` | Workshop attendance management | `frontend/src/components/academy/instructor/AttendanceSheet.tsx` |
| `AccessCodeGenerator` | Generate and manage access codes | `frontend/src/components/academy/instructor/AccessCodeGenerator.tsx` |
| `LearnerProgressTable` | View enrolled learners' progress | `frontend/src/components/academy/instructor/LearnerProgressTable.tsx` |
| `SubmissionReviewer` | Review and grade submissions | `frontend/src/components/academy/instructor/SubmissionReviewer.tsx` |
| `CourseAnalytics` | Course performance charts | `frontend/src/components/academy/instructor/CourseAnalytics.tsx` |

### API Endpoints Required
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/academy/instructor/dashboard` | Dashboard stats (provider-scoped) |
| GET | `/api/v1/academy/instructor/courses` | List instructor's courses |
| POST | `/api/v1/academy/instructor/courses` | Create new course |
| GET | `/api/v1/academy/instructor/courses/{id}` | Get course details |
| PUT | `/api/v1/academy/instructor/courses/{id}` | Update course |
| DELETE | `/api/v1/academy/instructor/courses/{id}` | Delete course (draft only) |
| POST | `/api/v1/academy/instructor/courses/{id}/publish` | Submit for publishing |
| POST | `/api/v1/academy/instructor/courses/{id}/modules` | Add module |
| PUT | `/api/v1/academy/instructor/courses/{id}/modules/{moduleId}` | Update module |
| POST | `/api/v1/academy/instructor/courses/{id}/lessons` | Create lesson |
| PUT | `/api/v1/academy/instructor/lessons/{id}` | Update lesson |
| POST | `/api/v1/academy/instructor/media/upload` | Upload media files |
| POST | `/api/v1/academy/instructor/courses/{id}/quizzes` | Create quiz |
| PUT | `/api/v1/academy/instructor/quizzes/{id}` | Update quiz |
| GET | `/api/v1/academy/instructor/workshops` | List instructor's workshops |
| POST | `/api/v1/academy/instructor/workshops` | Create workshop |
| PUT | `/api/v1/academy/instructor/workshops/{id}` | Update workshop |
| POST | `/api/v1/academy/instructor/workshops/{id}/attendance` | Record attendance |
| GET | `/api/v1/academy/instructor/access-codes` | List access codes |
| POST | `/api/v1/academy/instructor/access-codes` | Generate access codes |
| GET | `/api/v1/academy/instructor/courses/{id}/learners` | Get course enrollees |
| GET | `/api/v1/academy/instructor/submissions` | List pending submissions |
| PUT | `/api/v1/academy/instructor/submissions/{id}/grade` | Grade submission |
| GET | `/api/v1/academy/instructor/courses/{id}/analytics` | Course analytics |

### Implementation Sequence
1. **Phase 1: Instructor Dashboard**
   - Dashboard page with stats and quick actions
   - Provider-scoped data fetching
   - Pending items display (submissions, questions)

2. **Phase 2: Course Management**
   - Course list with CRUD operations
   - Course builder with module/lesson structure
   - Draft/publish workflow

3. **Phase 3: Content Creation**
   - Lesson editor with rich text
   - Media upload (video, images, files)
   - Content preview functionality

4. **Phase 4: Assessments**
   - Quiz builder with question types
   - Quiz settings (passing score, attempts)
   - Submission review interface

5. **Phase 5: Workshop Management**
   - Workshop scheduling interface
   - Workshop setup and configuration
   - Live workshop facilitation tools
   - Attendance tracking

6. **Phase 6: Access & Analytics**
   - Access code generation
   - Learner progress monitoring
   - Course analytics dashboard
   - Messaging/Q&A interface

---

## Implementation Status

*Audited: December 30, 2025*

### Key Pages Status
| Page | Status | Path | Notes |
|------|--------|------|-------|
| Instructor Dashboard | ❌ Not Implemented | `frontend/src/app/(academy)/academy/instructor/page.tsx` | Overview page missing |
| My Courses | ❌ Not Implemented | `frontend/src/app/(academy)/academy/instructor/courses/page.tsx` | Course list missing |
| Course Builder | ❌ Not Implemented | `frontend/src/app/(academy)/academy/instructor/courses/[id]/edit/page.tsx` | Course builder missing |
| Lesson Editor | ❌ Not Implemented | `frontend/src/app/(academy)/academy/instructor/courses/[id]/lessons/[lessonId]/page.tsx` | Lesson editor missing |
| Quiz Builder | ❌ Not Implemented | `frontend/src/app/(academy)/academy/instructor/courses/[id]/quizzes/[quizId]/page.tsx` | Quiz builder missing |
| My Workshops | ❌ Not Implemented | `frontend/src/app/(academy)/academy/instructor/workshops/page.tsx` | Workshop list missing |
| Workshop Setup | ❌ Not Implemented | `frontend/src/app/(academy)/academy/instructor/workshops/[id]/setup/page.tsx` | Setup page missing |
| Workshop Room | ❌ Not Implemented | `frontend/src/app/(academy)/academy/instructor/workshops/[id]/live/page.tsx` | Facilitator room missing |
| Attendance | ❌ Not Implemented | `frontend/src/app/(academy)/academy/instructor/workshops/[id]/attendance/page.tsx` | Attendance tracking missing |
| Access Codes | ❌ Not Implemented | `frontend/src/app/(academy)/academy/instructor/access-codes/page.tsx` | Code management missing |
| Learner Progress | ❌ Not Implemented | `frontend/src/app/(academy)/academy/instructor/courses/[id]/learners/page.tsx` | Learner tracking missing |
| Submissions | ❌ Not Implemented | `frontend/src/app/(academy)/academy/instructor/submissions/page.tsx` | Grading interface missing |
| Course Analytics | ❌ Not Implemented | `frontend/src/app/(academy)/academy/instructor/courses/[id]/analytics/page.tsx` | Analytics missing |
| Messages | ❌ Not Implemented | `frontend/src/app/(academy)/academy/instructor/messages/page.tsx` | Communications missing |

### API Endpoints Status
| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| POST `/training/facilitator/grant` | ✅ Implemented | `backend/apps/training/api.py` | Grant facilitator role |
| GET `/training/facilitator/list` | ✅ Implemented | `backend/apps/training/api.py` | List facilitators |
| PUT `/training/facilitator/update` | ✅ Implemented | `backend/apps/training/api.py` | Update facilitator |
| DELETE `/training/facilitator/revoke` | ✅ Implemented | `backend/apps/training/api.py` | Revoke access |
| GET `/training/facilitator/my-permissions` | ✅ Implemented | `backend/apps/training/api.py` | My permissions |
| POST `/training/access-code/generate` | ✅ Implemented | `backend/apps/training/api.py` | Generate codes |
| GET `/training/access-code/list` | ✅ Implemented | `backend/apps/training/api.py` | List codes |
| GET `/training/access-code/stats` | ✅ Implemented | `backend/apps/training/api.py` | Code statistics |
| POST `/training/access-code/revoke` | ✅ Implemented | `backend/apps/training/api.py` | Revoke code |
| GET `/training/access-code/audit` | ✅ Implemented | `backend/apps/training/api.py` | Code audit trail |
| GET `/api/v1/academy/instructor/dashboard` | ❌ Not Implemented | - | Dashboard stats |
| POST `/api/v1/academy/instructor/courses` | ❌ Not Implemented | - | Create course |
| POST `/api/v1/academy/instructor/media/upload` | ❌ Not Implemented | - | Media upload |
| POST `/api/v1/academy/instructor/workshops/{id}/attendance` | ❌ Not Implemented | - | Record attendance |

### Overall Progress
- **Pages**: 0/14 implemented (0%)
- **APIs**: 10/14 implemented (71%)
