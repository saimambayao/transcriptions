# TSP Admin - MoroAcademy

## Overview
TSP (Training Service Provider) Admins manage accredited training organizations on MoroAcademy. They oversee instructor teams, manage course catalogs, handle accreditation compliance, and track organizational performance. TSPs are independent training entities that offer courses to learners across the Bangsamoro region.

## Role Definition
**Type**: Provider Admin
**Portal Access**: TSP admin dashboard (`/academy/tsp/*`)
**Authentication**: Provider admin account
**Provider Scope**: PROVIDER - full control over TSP's content and instructors

## Capabilities

### Core Capabilities
| Capability | Description | Priority |
|------------|-------------|----------|
| Manage TSP Profile | Update organization information and branding | P0 |
| Manage Instructors | Add, remove, assign instructors to courses | P0 |
| Oversee All Courses | View and manage all TSP courses | P0 |
| Publish Courses | Approve and publish instructor-created courses | P0 |
| Manage Workshops | Oversee all TSP workshops | P0 |
| Track Accreditation | Monitor and maintain accreditation status | P0 |
| View Analytics | Access comprehensive TSP performance data | P0 |
| Generate Access Codes | Create bulk enrollment codes | P1 |
| Manage Pricing | Set course fees and discounts | P1 |
| Issue Bulk Certificates | Batch certificate generation | P1 |
| View Financial Reports | Track revenue and transactions | P1 |
| Configure Settings | Customize TSP-specific configurations | P2 |
| Export Data | Download reports and learner data | P2 |
| Manage Partnerships | Coordinate with other providers | P3 |
| Submit Compliance Docs | Upload accreditation documentation | P1 |

### Feature Access Matrix
| Feature | Access Level | Notes |
|---------|--------------|-------|
| TSP Profile | Full | Complete control |
| Instructor Management | Full | Add, edit, remove |
| Course Catalog | Full | All TSP courses |
| Workshop Management | Full | All TSP workshops |
| Content Publishing | Full | Approve and publish |
| Access Codes | Full | Generate and manage |
| Learner Data | Full | All TSP enrollees |
| Certificates | Full | Issue and revoke |
| Financial Data | Full | TSP revenue only |
| Platform Settings | None | CSEA admin only |
| Other Providers | None | Cannot access |
| Accreditation | Partial | Submit, cannot approve |

## User Journey Entry Points
1. **TSP Dashboard** - Login to manage organization
2. **Accreditation Alert** - Notification about compliance requirements
3. **Course Approval Request** - Instructor submitted course for review
4. **Financial Report** - Monthly revenue summary notification
5. **Learner Milestone** - Achievement notification (e.g., 1000th enrollee)
6. **Instructor Application** - New instructor request to join TSP

## Key Pages
| Page | Purpose | Implementation |
|------|---------|----------------|
| TSP Dashboard `/academy/tsp` | Overview of all TSP activities | Planned |
| TSP Profile `/academy/tsp/profile` | Organization settings and branding | Planned |
| Instructor Management `/academy/tsp/instructors` | Team management | Planned |
| Add Instructor `/academy/tsp/instructors/add` | Invite new instructor | Planned |
| All Courses `/academy/tsp/courses` | Complete course catalog | Planned |
| Course Review `/academy/tsp/courses/[id]/review` | Approve course for publishing | Planned |
| All Workshops `/academy/tsp/workshops` | Workshop management | Planned |
| Accreditation `/academy/tsp/accreditation` | Compliance tracking | Planned |
| Analytics Dashboard `/academy/tsp/analytics` | Performance metrics | Planned |
| Financial Reports `/academy/tsp/finances` | Revenue and transactions | Planned |
| Access Codes `/academy/tsp/access-codes` | Bulk code management | Planned |
| Certificates `/academy/tsp/certificates` | Certificate management | Planned |
| Learner Data `/academy/tsp/learners` | All TSP learners | Planned |
| Settings `/academy/tsp/settings` | TSP configuration | Planned |
| Documents `/academy/tsp/documents` | Compliance documents | Planned |

## Role Progression
**From**:
- Instructor (promoted to admin)
- Founder (established new TSP)

**To**:
- Multi-TSP Admin (managing multiple training organizations)
- CSEA Training Consultant (advisory role)

**Requirements**:
- TSP registration approval from CSEA
- Valid accreditation status
- Completed TSP orientation program
- Background verification

## Pain Points
1. **Complex Accreditation** - Confusing compliance requirements and deadlines
2. **Limited Branding** - Cannot fully customize TSP appearance on platform
3. **Manual Instructor Onboarding** - Time-consuming process to add instructors
4. **Fragmented Analytics** - Data scattered across multiple reports
5. **Revenue Tracking** - Delayed financial reporting
6. **Course Approval Bottleneck** - Too many courses pending review
7. **No Bulk Operations** - Cannot perform batch actions efficiently
8. **Limited Integrations** - No connection to external systems
9. **Compliance Document Management** - Difficult to organize required documents
10. **Instructor Performance Tracking** - Limited visibility into individual instructor metrics

## Improvement Opportunities
1. **Accreditation Dashboard** - Clear timeline and checklist for compliance
2. **Custom Branding** - White-label TSP presence with logo, colors
3. **Self-Service Instructor Onboarding** - Streamlined invitation and setup
4. **Unified Analytics** - Single dashboard with all key metrics
5. **Real-Time Revenue** - Live financial tracking and reporting
6. **Course Workflow Automation** - Automatic quality checks before review
7. **Bulk Actions** - Multi-select for courses, learners, certificates
8. **API Access** - Integration with external LMS and CRM systems
9. **Document Vault** - Organized storage with expiry reminders
10. **Instructor Scorecards** - Performance metrics per instructor
11. **Automated Renewals** - Accreditation renewal reminders and workflows
12. **Comparative Analytics** - Benchmark against platform averages

## Success Metrics
- **Active Courses**: Number of published, active courses
- **Total Enrollments**: Cumulative learners across all courses
- **Completion Rate**: Average course completion rate
- **Learner Satisfaction**: Average rating across all courses
- **Revenue Growth**: Month-over-month revenue change
- **Instructor Productivity**: Courses produced per instructor
- **Accreditation Status**: Continuous compliance maintenance
- **Time to Publish**: Average days from course submission to publication

## TSP Lifecycle
```
Registration -> CSEA Approval -> Onboarding -> Add Instructors ->
Create Courses -> Publish -> Enroll Learners -> Monitor & Grow ->
Renew Accreditation -> Expand
```

## Accreditation Workflow
```
Submit Application -> Document Upload -> CSEA Review ->
Site Visit (if required) -> Approval -> Ongoing Compliance ->
Annual Review -> Renewal
```

## UI/UX Considerations
- Executive-level dashboard with KPIs at a glance
- Clear accreditation status indicators (traffic lights)
- Quick actions for common administrative tasks
- Searchable instructor and course management
- Visual financial reports with charts
- Document management with version history
- Notification center for important alerts
- Role-based access for TSP team members
- Mobile-responsive for management on-the-go
- Audit trail for compliance activities

---

## Implementation Plan

### Access Control
- Authentication required with `tsp_admin` role verification
- **Provider scoping is CRITICAL** - TSP admins only manage their own TSP
- Middleware: `withTSPAccess` checking `user.tsp_id` against resource ownership
- Full control over TSP's instructors, courses, and learner data
- Cannot access other TSPs, Coops, or SEs

### Priority Pages
| Priority | Page | Route | File Path |
|----------|------|-------|-----------|
| P0 | TSP Dashboard | `/academy/tsp` | `frontend/src/app/(academy)/academy/tsp/page.tsx` |
| P0 | TSP Profile | `/academy/tsp/profile` | `frontend/src/app/(academy)/academy/tsp/profile/page.tsx` |
| P0 | Instructor Management | `/academy/tsp/instructors` | `frontend/src/app/(academy)/academy/tsp/instructors/page.tsx` |
| P0 | Add Instructor | `/academy/tsp/instructors/add` | `frontend/src/app/(academy)/academy/tsp/instructors/add/page.tsx` |
| P0 | All Courses | `/academy/tsp/courses` | `frontend/src/app/(academy)/academy/tsp/courses/page.tsx` |
| P0 | Course Review | `/academy/tsp/courses/[id]/review` | `frontend/src/app/(academy)/academy/tsp/courses/[id]/review/page.tsx` |
| P0 | Accreditation | `/academy/tsp/accreditation` | `frontend/src/app/(academy)/academy/tsp/accreditation/page.tsx` |
| P1 | All Workshops | `/academy/tsp/workshops` | `frontend/src/app/(academy)/academy/tsp/workshops/page.tsx` |
| P1 | Analytics Dashboard | `/academy/tsp/analytics` | `frontend/src/app/(academy)/academy/tsp/analytics/page.tsx` |
| P1 | Financial Reports | `/academy/tsp/finances` | `frontend/src/app/(academy)/academy/tsp/finances/page.tsx` |
| P1 | Access Codes | `/academy/tsp/access-codes` | `frontend/src/app/(academy)/academy/tsp/access-codes/page.tsx` |
| P1 | Certificates | `/academy/tsp/certificates` | `frontend/src/app/(academy)/academy/tsp/certificates/page.tsx` |
| P2 | Learner Data | `/academy/tsp/learners` | `frontend/src/app/(academy)/academy/tsp/learners/page.tsx` |
| P2 | Settings | `/academy/tsp/settings` | `frontend/src/app/(academy)/academy/tsp/settings/page.tsx` |
| P2 | Documents | `/academy/tsp/documents` | `frontend/src/app/(academy)/academy/tsp/documents/page.tsx` |

### Role-Specific Components
| Component | Purpose | File Path |
|-----------|---------|-----------|
| `TSPDashboard` | Executive KPI dashboard | `frontend/src/components/academy/tsp/TSPDashboard.tsx` |
| `TSPProfileForm` | Organization profile editor | `frontend/src/components/academy/tsp/TSPProfileForm.tsx` |
| `InstructorTable` | Instructor management table | `frontend/src/components/academy/tsp/InstructorTable.tsx` |
| `InstructorInviteForm` | Invite new instructor form | `frontend/src/components/academy/tsp/InstructorInviteForm.tsx` |
| `CourseApprovalQueue` | Pending courses for review | `frontend/src/components/academy/tsp/CourseApprovalQueue.tsx` |
| `CourseReviewer` | Course review interface | `frontend/src/components/academy/tsp/CourseReviewer.tsx` |
| `AccreditationStatus` | Accreditation status display | `frontend/src/components/academy/tsp/AccreditationStatus.tsx` |
| `AccreditationChecklist` | Compliance requirements | `frontend/src/components/academy/tsp/AccreditationChecklist.tsx` |
| `TSPAnalytics` | Performance analytics charts | `frontend/src/components/academy/tsp/TSPAnalytics.tsx` |
| `FinancialReport` | Revenue and transaction reports | `frontend/src/components/academy/tsp/FinancialReport.tsx` |
| `BulkAccessCodes` | Bulk access code generator | `frontend/src/components/academy/tsp/BulkAccessCodes.tsx` |
| `CertificateManager` | Bulk certificate operations | `frontend/src/components/academy/tsp/CertificateManager.tsx` |
| `LearnerDataTable` | TSP learner management | `frontend/src/components/academy/tsp/LearnerDataTable.tsx` |
| `DocumentVault` | Compliance document storage | `frontend/src/components/academy/tsp/DocumentVault.tsx` |

### API Endpoints Required
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/academy/tsp/dashboard` | Dashboard KPIs |
| GET | `/api/v1/academy/tsp/profile` | Get TSP profile |
| PUT | `/api/v1/academy/tsp/profile` | Update TSP profile |
| GET | `/api/v1/academy/tsp/instructors` | List TSP instructors |
| POST | `/api/v1/academy/tsp/instructors/invite` | Invite instructor |
| DELETE | `/api/v1/academy/tsp/instructors/{id}` | Remove instructor |
| PUT | `/api/v1/academy/tsp/instructors/{id}/courses` | Assign courses |
| GET | `/api/v1/academy/tsp/courses` | List all TSP courses |
| GET | `/api/v1/academy/tsp/courses/pending` | Pending course approvals |
| PUT | `/api/v1/academy/tsp/courses/{id}/publish` | Approve and publish course |
| PUT | `/api/v1/academy/tsp/courses/{id}/reject` | Reject course with feedback |
| GET | `/api/v1/academy/tsp/workshops` | List all TSP workshops |
| GET | `/api/v1/academy/tsp/accreditation` | Get accreditation status |
| POST | `/api/v1/academy/tsp/accreditation/documents` | Upload compliance docs |
| GET | `/api/v1/academy/tsp/analytics` | TSP performance analytics |
| GET | `/api/v1/academy/tsp/finances` | Financial reports |
| GET | `/api/v1/academy/tsp/access-codes` | List all access codes |
| POST | `/api/v1/academy/tsp/access-codes/bulk` | Generate bulk codes |
| GET | `/api/v1/academy/tsp/certificates` | List issued certificates |
| POST | `/api/v1/academy/tsp/certificates/bulk` | Bulk issue certificates |
| GET | `/api/v1/academy/tsp/learners` | List TSP learners |
| GET | `/api/v1/academy/tsp/learners/{id}` | Learner details |
| GET | `/api/v1/academy/tsp/documents` | List compliance documents |

### Implementation Sequence
1. **Phase 1: TSP Dashboard & Profile**
   - Dashboard with KPIs and quick actions
   - TSP profile management
   - Branding configuration

2. **Phase 2: Instructor Management**
   - Instructor list with CRUD
   - Invitation workflow
   - Course assignment

3. **Phase 3: Course Oversight**
   - All courses list view
   - Course approval workflow
   - Publishing controls

4. **Phase 4: Accreditation**
   - Accreditation status display
   - Compliance checklist
   - Document upload and management

5. **Phase 5: Analytics & Finance**
   - Performance analytics dashboard
   - Financial reporting
   - Export capabilities

6. **Phase 6: Operations**
   - Bulk access code generation
   - Certificate management
   - Learner data management
   - Settings configuration

---

## Implementation Status

*Audited: December 30, 2025*

### Key Pages Status
| Page | Status | Path | Notes |
|------|--------|------|-------|
| TSP Dashboard | ✅ Implemented | `frontend/src/app/(tsp)/dashboard/page.tsx` | Main dashboard |
| TSP Login | ✅ Implemented | `frontend/src/app/(tsp)/login/page.tsx` | Authentication |
| TSP Register | ✅ Implemented | `frontend/src/app/(tsp)/register/page.tsx` | Registration |
| TSP Profile | ❌ Not Implemented | `frontend/src/app/(tsp)/profile/page.tsx` | Organization settings missing |
| Instructor Management | ❌ Not Implemented | `frontend/src/app/(tsp)/instructors/page.tsx` | Team management missing |
| Add Instructor | ❌ Not Implemented | `frontend/src/app/(tsp)/instructors/add/page.tsx` | Invite form missing |
| All Courses | ❌ Not Implemented | `frontend/src/app/(tsp)/courses/page.tsx` | Course catalog missing |
| Course Review | ❌ Not Implemented | `frontend/src/app/(tsp)/courses/[id]/review/page.tsx` | Approval workflow missing |
| All Workshops | ❌ Not Implemented | `frontend/src/app/(tsp)/workshops/page.tsx` | Workshop management missing |
| Accreditation | ❌ Not Implemented | `frontend/src/app/(tsp)/accreditation/page.tsx` | Compliance tracking missing |
| Analytics Dashboard | ❌ Not Implemented | `frontend/src/app/(tsp)/analytics/page.tsx` | Performance metrics missing |
| Financial Reports | ❌ Not Implemented | `frontend/src/app/(tsp)/finances/page.tsx` | Revenue tracking missing |
| Access Codes | ❌ Not Implemented | `frontend/src/app/(tsp)/access-codes/page.tsx` | Bulk codes missing |
| Certificates | ❌ Not Implemented | `frontend/src/app/(tsp)/certificates/page.tsx` | Certificate management missing |
| Learner Data | ❌ Not Implemented | `frontend/src/app/(tsp)/learners/page.tsx` | Learner management missing |
| Settings | ❌ Not Implemented | `frontend/src/app/(tsp)/settings/page.tsx` | TSP config missing |
| Documents | ❌ Not Implemented | `frontend/src/app/(tsp)/documents/page.tsx` | Compliance docs missing |

### API Endpoints Status
| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| GET `/api/v1/academy/tsp/dashboard` | ❌ Not Implemented | - | Dashboard KPIs |
| GET `/api/v1/academy/tsp/profile` | ❌ Not Implemented | - | TSP profile |
| GET `/api/v1/academy/tsp/instructors` | ❌ Not Implemented | - | List instructors |
| POST `/api/v1/academy/tsp/instructors/invite` | ❌ Not Implemented | - | Invite instructor |
| GET `/api/v1/academy/tsp/courses` | ❌ Not Implemented | - | List courses |
| PUT `/api/v1/academy/tsp/courses/{id}/publish` | ❌ Not Implemented | - | Publish course |
| GET `/api/v1/academy/tsp/accreditation` | ❌ Not Implemented | - | Accreditation status |
| GET `/api/v1/academy/tsp/analytics` | ❌ Not Implemented | - | Analytics |
| GET `/api/v1/academy/tsp/finances` | ❌ Not Implemented | - | Financial reports |
| POST `/api/v1/academy/tsp/access-codes/bulk` | ❌ Not Implemented | - | Bulk codes |

### Overall Progress
- **Pages**: 3/17 implemented (18%)
- **APIs**: 0/10 implemented (0%)
