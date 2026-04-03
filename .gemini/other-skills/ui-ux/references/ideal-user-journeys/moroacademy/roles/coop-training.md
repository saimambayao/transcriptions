# CET (Committee on Education and Training) - User Journey on MoroAcademy

## Overview
The Committee on Education and Training (CET) manages training programs for their cooperative on MoroAcademy. Per RA 9520 (Philippine Cooperative Code), the Vice Chairperson of the Board of Directors serves as the Chairperson of this mandated committee. The CET coordinates member education, organizes peer training sessions, tracks member learning progress, and ensures cooperative-specific training requirements are met. They bridge the gap between MoroAcademy content and cooperative member development needs.

## Legal Basis
- **RA 9520** (Philippine Cooperative Code of 2008) mandates the Committee on Education and Training
- The Vice Chairperson of the BOD serves as CET Chairperson
- Committee members are appointed per cooperative bylaws
- Responsible for implementing the cooperative's education and training program

## Role Definition
**Type**: Provider (Cooperative)
**Portal Access**: Coop training dashboard (`/portal/training/*` and `/academy/coop/*`)
**Authentication**: Coop Portal linked account
**Provider Scope**: PROVIDER - limited to cooperative's training activities
**Committee Structure**: Chairperson (Vice Chair of BOD) + Committee Members

## Capabilities

### Core Capabilities
| Capability | Description | Priority |
|------------|-------------|----------|
| Manage Coop Courses | Create and manage cooperative-specific courses | P0 |
| Enroll Members | Bulk enroll cooperative members in courses | P0 |
| Track Member Progress | Monitor learning completion across membership | P0 |
| Facilitate Peer Training | Organize member-to-member training sessions | P0 |
| Schedule Workshops | Set up cooperative training workshops | P0 |
| Generate Access Codes | Create enrollment codes for exclusive content | P0 |
| Issue Certificates | Approve certificates for cooperative members | P1 |
| View Analytics | Track cooperative training metrics | P1 |
| Curate External Courses | Recommend TSP/CSEA courses to members | P1 |
| Take Attendance | Record workshop and training participation | P1 |
| Report to Management | Generate training reports for coop leadership | P2 |
| Manage Training Calendar | Coordinate training schedule | P2 |
| Track Compliance Training | Monitor required training completions | P1 |
| Budget Training | Manage training expenses and subsidies | P3 |

### Feature Access Matrix
| Feature | Access Level | Notes |
|---------|--------------|-------|
| Coop Course Creation | Full | For cooperative content |
| Member Enrollment | Full | Enroll coop members |
| External Courses | Partial | Recommend, cannot manage |
| Member Progress | Full | All coop members |
| Workshop Management | Full | Coop workshops |
| Access Codes | Full | Generate for coop courses |
| Certificates | Partial | Coop courses only |
| Analytics | Partial | Coop data only |
| Platform Courses | None | Cannot create platform-wide |
| Other Coops | None | Cannot access |
| TSP Management | None | Not a TSP admin |
| Financial Management | Partial | Training budget only |

## User Journey Entry Points
1. **Coop Portal** - Navigate from cooperative portal to training section
2. **Training Dashboard** - Direct access to training management
3. **Member Request** - Notification of training needs from members
4. **Compliance Alert** - Required training deadline approaching
5. **New Course Alert** - Relevant TSP/CSEA course published
6. **Board Report Request** - Need to prepare training report

## Key Pages
| Page | Purpose | Implementation |
|------|---------|----------------|
| Training Dashboard `/portal/training` | Overview of coop training | Planned |
| Member Progress `/portal/training/members` | All member learning status | Planned |
| Coop Courses `/portal/training/courses` | Cooperative course catalog | Planned |
| Create Course `/portal/training/courses/create` | Build coop-specific course | Planned |
| Course Builder `/portal/training/courses/[id]/edit` | Edit course content | Planned |
| Workshops `/portal/training/workshops` | Coop workshop management | Planned |
| Schedule Workshop `/portal/training/workshops/schedule` | Create new workshop | Planned |
| Peer Training `/portal/training/peer` | Member-to-member sessions | Planned |
| Access Codes `/portal/training/access-codes` | Enrollment code management | Planned |
| Attendance `/portal/training/attendance` | Training attendance records | Planned |
| Compliance `/portal/training/compliance` | Required training tracking | Planned |
| Analytics `/portal/training/analytics` | Training performance metrics | Planned |
| Reports `/portal/training/reports` | Generate training reports | Planned |
| Calendar `/portal/training/calendar` | Training schedule view | Planned |
| Course Catalog `/academy/courses` | Browse external courses | Existing |

## Role Progression
**From**:
- Coop Member/Learner (elected/appointed to committee)
- Coop Officer (Vice Chairperson of BOD automatically becomes CET Chairperson)

**To**:
- Federation/Union CET Chairperson (multi-coop training coordination)
- TSP Admin (if coop becomes TSP)
- CSEA/CRITS Consultant (government liaison role)

**Requirements**:
- Active cooperative membership
- Election as Vice Chairperson of BOD (for CET Chairperson) or appointment as committee member
- Completion of CET orientation training
- Understanding of cooperative education principles per RA 9520

## Pain Points
1. **Dual Portal Navigation** - Switching between Coop Portal and Academy
2. **Limited Course Templates** - No coop-specific course frameworks
3. **Member Enrollment Friction** - Complex process to add members to courses
4. **No Peer Training Tools** - Informal training not well supported
5. **Compliance Tracking Manual** - Required training not automated
6. **Report Generation Difficult** - Time-consuming to prepare board reports
7. **No Training Needs Assessment** - Difficult to identify skill gaps
8. **Budget Constraints Invisible** - No clear training budget tracking
9. **External Course Discovery** - Hard to find relevant TSP/CSEA courses
10. **Member Engagement Low** - Difficulty motivating members to learn

## Improvement Opportunities
1. **Unified Training Hub** - Single interface for all training activities
2. **Coop Course Templates** - Pre-built courses for common coop training
3. **One-Click Enrollment** - Easy member enrollment from member list
4. **Peer Training Module** - Formal support for member-led sessions
5. **Compliance Dashboard** - Automated tracking with reminders
6. **Auto-Generated Reports** - One-click board report generation
7. **Skills Gap Analysis** - Assessment tool to identify training needs
8. **Training Budget Tracker** - Expense management and subsidy tracking
9. **Course Recommendations** - AI-suggested courses based on coop needs
10. **Gamification** - Points and badges to encourage member learning
11. **Learning Paths** - Curated course sequences for member development
12. **Mobile Notifications** - Push alerts for members about training

## Success Metrics
- **Member Enrollment Rate**: Percentage of members enrolled in at least one course
- **Course Completion Rate**: Average completion rate across members
- **Training Hours**: Total learning hours logged by members
- **Compliance Rate**: Percentage completing required training on time
- **Workshop Attendance**: Average attendance at coop workshops
- **Peer Training Sessions**: Number of member-led training events
- **Member Satisfaction**: Training program satisfaction scores
- **Skills Improvement**: Pre/post assessment score changes

## Cooperative Training Types
| Training Type | Description | Example |
|---------------|-------------|---------|
| Mandatory Compliance | Required by CSEA or law | Cooperative principles, governance |
| Skill Development | Practical member skills | Financial literacy, product handling |
| Leadership | Officer and board training | Strategic planning, meeting management |
| Peer Training | Member-to-member knowledge | Best practices sharing, mentorship |
| External Programs | TSP/CSEA offered courses | Business development, digital skills |

## Training Calendar Workflow
```
Assess Needs -> Plan Training Year -> Schedule Workshops ->
Promote to Members -> Conduct Training -> Track Attendance ->
Evaluate -> Report to Board -> Iterate
```

## UI/UX Considerations
- Integration with Coop Portal for seamless navigation
- Member roster integration for easy enrollment
- Calendar view with drag-and-drop scheduling
- Progress visualization for member learning
- Compliance status indicators (red/yellow/green)
- Quick access to frequently used functions
- Mobile-friendly for field coordinators
- Printable attendance sheets and reports
- Notification preferences for training updates
- Collaborative planning with other coop officers

---

## Implementation Plan

### Access Control
- Authentication required with `coop_cet_member` or `coop_cet_chairperson` role
- **Tenant scoping is CRITICAL** - CET members only see their cooperative's data
- Middleware: `withTenantAccess` checking `user.tenant_id` (cooperative)
- Integration with Coop Portal authentication
- Access to both `/portal/training/*` (tenant) and public `/academy/*` for course discovery
- Cannot access other cooperatives' training data
- CET Chairperson (Vice Chair of BOD) has approval authority for training decisions

### Priority Pages
| Priority | Page | Route | File Path |
|----------|------|-------|-----------|
| P0 | Training Dashboard | `/portal/training` | `frontend/src/app/(tenant)/portal/training/page.tsx` |
| P0 | Member Progress | `/portal/training/members` | `frontend/src/app/(tenant)/portal/training/members/page.tsx` |
| P0 | Coop Courses | `/portal/training/courses` | `frontend/src/app/(tenant)/portal/training/courses/page.tsx` |
| P0 | Create Course | `/portal/training/courses/create` | `frontend/src/app/(tenant)/portal/training/courses/create/page.tsx` |
| P0 | Course Builder | `/portal/training/courses/[id]/edit` | `frontend/src/app/(tenant)/portal/training/courses/[id]/edit/page.tsx` |
| P0 | Workshops | `/portal/training/workshops` | `frontend/src/app/(tenant)/portal/training/workshops/page.tsx` |
| P1 | Schedule Workshop | `/portal/training/workshops/schedule` | `frontend/src/app/(tenant)/portal/training/workshops/schedule/page.tsx` |
| P1 | Peer Training | `/portal/training/peer` | `frontend/src/app/(tenant)/portal/training/peer/page.tsx` |
| P1 | Compliance | `/portal/training/compliance` | `frontend/src/app/(tenant)/portal/training/compliance/page.tsx` |
| P1 | Access Codes | `/portal/training/access-codes` | `frontend/src/app/(tenant)/portal/training/access-codes/page.tsx` |
| P1 | Attendance | `/portal/training/attendance` | `frontend/src/app/(tenant)/portal/training/attendance/page.tsx` |
| P2 | Analytics | `/portal/training/analytics` | `frontend/src/app/(tenant)/portal/training/analytics/page.tsx` |
| P2 | Reports | `/portal/training/reports` | `frontend/src/app/(tenant)/portal/training/reports/page.tsx` |
| P2 | Calendar | `/portal/training/calendar` | `frontend/src/app/(tenant)/portal/training/calendar/page.tsx` |

### Role-Specific Components
| Component | Purpose | File Path |
|-----------|---------|-----------|
| `CoopTrainingDashboard` | Training overview for coop | `frontend/src/components/portal/training/CoopTrainingDashboard.tsx` |
| `MemberProgressTable` | Member learning progress | `frontend/src/components/portal/training/MemberProgressTable.tsx` |
| `MemberEnrollment` | Bulk member enrollment | `frontend/src/components/portal/training/MemberEnrollment.tsx` |
| `CoopCourseBuilder` | Coop-specific course builder | `frontend/src/components/portal/training/CoopCourseBuilder.tsx` |
| `CoopCourseTemplates` | Pre-built coop course templates | `frontend/src/components/portal/training/CoopCourseTemplates.tsx` |
| `WorkshopScheduler` | Workshop creation/scheduling | `frontend/src/components/portal/training/WorkshopScheduler.tsx` |
| `PeerTrainingManager` | Member-to-member session tracking | `frontend/src/components/portal/training/PeerTrainingManager.tsx` |
| `ComplianceTracker` | Required training status | `frontend/src/components/portal/training/ComplianceTracker.tsx` |
| `AttendanceRecorder` | Workshop attendance interface | `frontend/src/components/portal/training/AttendanceRecorder.tsx` |
| `CoopTrainingAnalytics` | Training metrics charts | `frontend/src/components/portal/training/CoopTrainingAnalytics.tsx` |
| `BoardReportGenerator` | Training report for board | `frontend/src/components/portal/training/BoardReportGenerator.tsx` |
| `TrainingCalendar` | Calendar view of training | `frontend/src/components/portal/training/TrainingCalendar.tsx` |
| `ExternalCourseRecommender` | Browse/recommend TSP courses | `frontend/src/components/portal/training/ExternalCourseRecommender.tsx` |

### API Endpoints Required
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/portal/training/dashboard` | Coop training dashboard stats |
| GET | `/api/v1/portal/training/members` | List members with learning status |
| POST | `/api/v1/portal/training/members/enroll` | Bulk enroll members |
| GET | `/api/v1/portal/training/members/{id}/progress` | Member's learning progress |
| GET | `/api/v1/portal/training/courses` | List coop courses |
| POST | `/api/v1/portal/training/courses` | Create coop course |
| PUT | `/api/v1/portal/training/courses/{id}` | Update coop course |
| GET | `/api/v1/portal/training/courses/templates` | Get coop course templates |
| GET | `/api/v1/portal/training/workshops` | List coop workshops |
| POST | `/api/v1/portal/training/workshops` | Schedule workshop |
| PUT | `/api/v1/portal/training/workshops/{id}` | Update workshop |
| GET | `/api/v1/portal/training/peer-sessions` | List peer training sessions |
| POST | `/api/v1/portal/training/peer-sessions` | Record peer training |
| GET | `/api/v1/portal/training/compliance` | Compliance requirements status |
| GET | `/api/v1/portal/training/attendance` | Attendance records |
| POST | `/api/v1/portal/training/attendance` | Record attendance |
| GET | `/api/v1/portal/training/access-codes` | List access codes |
| POST | `/api/v1/portal/training/access-codes` | Generate access codes |
| GET | `/api/v1/portal/training/analytics` | Training analytics |
| GET | `/api/v1/portal/training/reports` | Generate training report |
| GET | `/api/v1/portal/training/calendar` | Training calendar events |

### Implementation Sequence
1. **Phase 1: Training Dashboard**
   - Dashboard with coop training overview
   - Integration with Coop Portal navigation
   - Quick stats and pending items

2. **Phase 2: Member Management**
   - Member progress tracking
   - Bulk enrollment from member roster
   - Individual member learning status

3. **Phase 3: Course Management**
   - Coop course creation
   - Course templates for common coop training
   - Course editing and management

4. **Phase 4: Workshop & Peer Training**
   - Workshop scheduling
   - Peer training session tracking
   - Attendance recording

5. **Phase 5: Compliance**
   - Compliance requirement tracking
   - Required training status
   - Compliance alerts and reminders

6. **Phase 6: Analytics & Reporting**
   - Training analytics dashboard
   - Board report generation
   - Calendar view
   - External course recommendations

---

## Implementation Status

*Audited: December 30, 2025*

### Key Pages Status
| Page | Status | Path | Notes |
|------|--------|------|-------|
| Training Dashboard | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/page.tsx` | Overview missing |
| Member Progress | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/members/page.tsx` | Member tracking missing |
| Coop Courses | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/courses/page.tsx` | Course catalog missing |
| Create Course | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/courses/create/page.tsx` | Course creation missing |
| Course Builder | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/courses/[id]/edit/page.tsx` | Builder missing |
| Workshops | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/workshops/page.tsx` | Workshop management missing |
| Schedule Workshop | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/workshops/schedule/page.tsx` | Scheduling missing |
| Peer Training | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/peer/page.tsx` | Peer sessions missing |
| Compliance | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/compliance/page.tsx` | Compliance tracking missing |
| Access Codes | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/access-codes/page.tsx` | Code management missing |
| Attendance | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/attendance/page.tsx` | Attendance records missing |
| Analytics | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/analytics/page.tsx` | Training metrics missing |
| Reports | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/reports/page.tsx` | Report generation missing |
| Calendar | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/calendar/page.tsx` | Schedule view missing |
| Course Catalog (Browse) | ✅ Implemented | `frontend/src/app/(academy)/academy/courses/page.tsx` | External course discovery |

### API Endpoints Status
| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| GET `/api/v1/portal/training/dashboard` | ❌ Not Implemented | - | Training dashboard stats |
| GET `/api/v1/portal/training/members` | ❌ Not Implemented | - | Member learning status |
| POST `/api/v1/portal/training/members/enroll` | ❌ Not Implemented | - | Bulk enrollment |
| GET `/api/v1/portal/training/courses` | ❌ Not Implemented | - | Coop courses |
| POST `/api/v1/portal/training/courses` | ❌ Not Implemented | - | Create course |
| GET `/api/v1/portal/training/workshops` | ❌ Not Implemented | - | List workshops |
| GET `/api/v1/portal/training/peer-sessions` | ❌ Not Implemented | - | Peer training |
| GET `/api/v1/portal/training/compliance` | ❌ Not Implemented | - | Compliance status |
| POST `/api/v1/portal/training/attendance` | ❌ Not Implemented | - | Record attendance |
| GET `/api/v1/portal/training/analytics` | ❌ Not Implemented | - | Training analytics |

### Overall Progress
- **Pages**: 1/15 implemented (7%)
- **APIs**: 0/10 implemented (0%)
