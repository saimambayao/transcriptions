# Social Enterprise Training Coordinator - MoroAcademy

## Overview
Social Enterprise Training Coordinators manage training programs for their social enterprise on MoroAcademy. They coordinate employee and stakeholder education, organize industry-specific training, track learning progress aligned with social impact goals, and ensure training supports the enterprise's social mission. They connect MoroAcademy resources with the social enterprise's development needs.

## Role Definition
**Type**: Provider (Social Enterprise)
**Portal Access**: SE training dashboard (`/portal/training/*` and `/academy/se/*`)
**Authentication**: SE Portal linked account
**Provider Scope**: PROVIDER - limited to social enterprise's training activities

## Capabilities

### Core Capabilities
| Capability | Description | Priority |
|------------|-------------|----------|
| Manage SE Courses | Create and manage enterprise-specific courses | P0 |
| Enroll Team Members | Add employees and stakeholders to courses | P0 |
| Track Team Progress | Monitor learning completion across team | P0 |
| Schedule Workshops | Set up enterprise training workshops | P0 |
| Generate Access Codes | Create enrollment codes for exclusive content | P0 |
| Issue Certificates | Approve certificates for team members | P1 |
| View Analytics | Track enterprise training metrics | P1 |
| Curate External Courses | Recommend TSP/CSEA courses to team | P1 |
| Map Impact Training | Align training with social impact goals | P0 |
| Take Attendance | Record workshop and training participation | P1 |
| Report to Leadership | Generate training reports for SE management | P2 |
| Manage Training Calendar | Coordinate training schedule | P2 |
| Industry Training | Organize sector-specific training | P1 |
| Beneficiary Training | Coordinate training for beneficiaries | P2 |

### Feature Access Matrix
| Feature | Access Level | Notes |
|---------|--------------|-------|
| SE Course Creation | Full | For enterprise content |
| Team Enrollment | Full | Enroll SE team members |
| External Courses | Partial | Recommend, cannot manage |
| Team Progress | Full | All SE team members |
| Workshop Management | Full | SE workshops |
| Access Codes | Full | Generate for SE courses |
| Certificates | Partial | SE courses only |
| Analytics | Partial | SE data only |
| Platform Courses | None | Cannot create platform-wide |
| Other SEs | None | Cannot access |
| TSP Management | None | Not a TSP admin |
| Impact Metrics | Partial | Training-related only |

## User Journey Entry Points
1. **SE Portal** - Navigate from social enterprise portal to training section
2. **Training Dashboard** - Direct access to training management
3. **Team Request** - Training needs from employees or stakeholders
4. **Impact Goal Review** - Align training with social mission objectives
5. **New Course Alert** - Relevant TSP/CSEA course published
6. **Board/Investor Report** - Need to prepare training impact report

## Key Pages
| Page | Purpose | Implementation |
|------|---------|----------------|
| Training Dashboard `/portal/training` | Overview of SE training | Planned |
| Team Progress `/portal/training/team` | All team learning status | Planned |
| SE Courses `/portal/training/courses` | Enterprise course catalog | Planned |
| Create Course `/portal/training/courses/create` | Build SE-specific course | Planned |
| Course Builder `/portal/training/courses/[id]/edit` | Edit course content | Planned |
| Workshops `/portal/training/workshops` | SE workshop management | Planned |
| Schedule Workshop `/portal/training/workshops/schedule` | Create new workshop | Planned |
| Industry Training `/portal/training/industry` | Sector-specific training | Planned |
| Beneficiary Training `/portal/training/beneficiaries` | Beneficiary programs | Planned |
| Access Codes `/portal/training/access-codes` | Enrollment code management | Planned |
| Attendance `/portal/training/attendance` | Training attendance records | Planned |
| Impact Alignment `/portal/training/impact` | Training-impact mapping | Planned |
| Analytics `/portal/training/analytics` | Training performance metrics | Planned |
| Reports `/portal/training/reports` | Generate training reports | Planned |
| Calendar `/portal/training/calendar` | Training schedule view | Planned |

## Role Progression
**From**:
- SE Team Member/Learner (appointed by SE management)
- HR or Operations lead (additional responsibility)

**To**:
- Lead Training Coordinator (multi-SE training)
- TSP Admin (if SE becomes accredited TSP)
- CSEA Training Consultant (government liaison role)

**Requirements**:
- Active social enterprise team membership
- Appointment by SE management or board
- Completion of Training Coordinator orientation
- Understanding of social enterprise principles and impact measurement

## Pain Points
1. **Dual Portal Navigation** - Switching between SE Portal and Academy
2. **No SE-Specific Templates** - Courses don't reflect SE context
3. **Impact Alignment Complex** - Difficult to connect training to social goals
4. **Beneficiary Training Separate** - Not integrated with team training
5. **Industry Training Fragmented** - Hard to find sector-specific content
6. **Report Generation Manual** - Time-consuming for investor reports
7. **No Skills Assessment** - Difficult to identify team skill gaps
8. **Limited Stakeholder Access** - External stakeholders hard to include
9. **Training ROI Unclear** - Cannot measure training impact on mission
10. **Resource Constraints** - Limited budget for training

## Improvement Opportunities
1. **Unified Training Hub** - Single interface for all training activities
2. **SE Course Templates** - Pre-built courses for social enterprise contexts
3. **Impact Dashboard** - Visual connection of training to social outcomes
4. **Integrated Beneficiary Training** - Same platform for all audiences
5. **Industry Course Library** - Curated sector-specific content
6. **Impact Reports** - Auto-generated training impact reports for investors
7. **Skills Gap Analysis** - Assessment tool to identify training needs
8. **Stakeholder Portal** - External access for partners and beneficiaries
9. **Training ROI Calculator** - Measure training contribution to impact
10. **Scholarship Management** - Training subsidies for beneficiaries
11. **Learning Paths by Role** - Curated sequences for different SE roles
12. **Mobile Learning** - Offline access for field-based team members

## Success Metrics
- **Team Enrollment Rate**: Percentage of team enrolled in training
- **Course Completion Rate**: Average completion rate across team
- **Training Hours**: Total learning hours logged by team
- **Impact Alignment Score**: Training programs linked to impact goals
- **Workshop Attendance**: Average attendance at SE workshops
- **Beneficiary Training**: Beneficiaries trained per quarter
- **Stakeholder Satisfaction**: Training program satisfaction scores
- **Skills Improvement**: Pre/post assessment score changes
- **Training-Impact Correlation**: Impact improvements linked to training

## Social Enterprise Training Types
| Training Type | Description | Example |
|---------------|-------------|---------|
| Core Team Development | Employee skills and knowledge | Operations, customer service |
| Leadership | Management and governance training | Strategic planning, impact measurement |
| Beneficiary Empowerment | Training for beneficiaries | Livelihood skills, financial literacy |
| Industry-Specific | Sector knowledge and skills | Agriculture, crafts, food processing |
| Impact Measurement | Understanding and tracking impact | Theory of change, M&E |
| Stakeholder Engagement | Partner and investor relations | Reporting, communication |

## Impact-Aligned Training Framework
```
Identify Impact Goals -> Map Required Skills -> Design Training ->
Deliver Training -> Measure Learning -> Track Impact Outcomes ->
Report to Stakeholders -> Iterate
```

## Training for Different SE Audiences
| Audience | Training Focus | Access Method |
|----------|----------------|---------------|
| Employees | Core skills, operations | Team enrollment |
| Management | Leadership, strategy | Priority access |
| Beneficiaries | Empowerment, livelihood | Access codes |
| Partners | Collaboration, processes | Guest access |
| Board Members | Governance, oversight | Executive access |

## UI/UX Considerations
- Integration with SE Portal for seamless navigation
- Team roster integration for easy enrollment
- Impact goal visualization with training connections
- Calendar view with drag-and-drop scheduling
- Progress visualization for team learning
- Beneficiary training tracking dashboard
- Quick access to frequently used functions
- Mobile-friendly for field coordinators
- Impact-ready reports for stakeholders
- Collaborative planning with SE leadership
- Industry-specific content recommendations
- Visual distinction between team and beneficiary training

---

## Implementation Plan

### Access Control
- Authentication required with `se_training_coordinator` role
- **Tenant scoping is CRITICAL** - coordinator only sees their social enterprise's data
- Middleware: `withTenantAccess` checking `user.tenant_id` (social enterprise)
- Integration with SE Portal authentication
- Access to both `/portal/training/*` (tenant) and public `/academy/*` for course discovery
- Cannot access other social enterprises' training data

### Priority Pages
| Priority | Page | Route | File Path |
|----------|------|-------|-----------|
| P0 | Training Dashboard | `/portal/training` | `frontend/src/app/(tenant)/portal/training/page.tsx` |
| P0 | Team Progress | `/portal/training/team` | `frontend/src/app/(tenant)/portal/training/team/page.tsx` |
| P0 | SE Courses | `/portal/training/courses` | `frontend/src/app/(tenant)/portal/training/courses/page.tsx` |
| P0 | Create Course | `/portal/training/courses/create` | `frontend/src/app/(tenant)/portal/training/courses/create/page.tsx` |
| P0 | Course Builder | `/portal/training/courses/[id]/edit` | `frontend/src/app/(tenant)/portal/training/courses/[id]/edit/page.tsx` |
| P0 | Workshops | `/portal/training/workshops` | `frontend/src/app/(tenant)/portal/training/workshops/page.tsx` |
| P0 | Impact Alignment | `/portal/training/impact` | `frontend/src/app/(tenant)/portal/training/impact/page.tsx` |
| P1 | Schedule Workshop | `/portal/training/workshops/schedule` | `frontend/src/app/(tenant)/portal/training/workshops/schedule/page.tsx` |
| P1 | Industry Training | `/portal/training/industry` | `frontend/src/app/(tenant)/portal/training/industry/page.tsx` |
| P1 | Beneficiary Training | `/portal/training/beneficiaries` | `frontend/src/app/(tenant)/portal/training/beneficiaries/page.tsx` |
| P1 | Access Codes | `/portal/training/access-codes` | `frontend/src/app/(tenant)/portal/training/access-codes/page.tsx` |
| P1 | Attendance | `/portal/training/attendance` | `frontend/src/app/(tenant)/portal/training/attendance/page.tsx` |
| P2 | Analytics | `/portal/training/analytics` | `frontend/src/app/(tenant)/portal/training/analytics/page.tsx` |
| P2 | Reports | `/portal/training/reports` | `frontend/src/app/(tenant)/portal/training/reports/page.tsx` |
| P2 | Calendar | `/portal/training/calendar` | `frontend/src/app/(tenant)/portal/training/calendar/page.tsx` |

### Role-Specific Components
| Component | Purpose | File Path |
|-----------|---------|-----------|
| `SETrainingDashboard` | Training overview for SE | `frontend/src/components/portal/training/SETrainingDashboard.tsx` |
| `TeamProgressTable` | Team learning progress | `frontend/src/components/portal/training/TeamProgressTable.tsx` |
| `TeamEnrollment` | Bulk team enrollment | `frontend/src/components/portal/training/TeamEnrollment.tsx` |
| `SECourseBuilder` | SE-specific course builder | `frontend/src/components/portal/training/SECourseBuilder.tsx` |
| `SECourseTemplates` | Pre-built SE course templates | `frontend/src/components/portal/training/SECourseTemplates.tsx` |
| `ImpactAlignmentMapper` | Map training to impact goals | `frontend/src/components/portal/training/ImpactAlignmentMapper.tsx` |
| `ImpactDashboard` | Training-impact visualization | `frontend/src/components/portal/training/ImpactDashboard.tsx` |
| `BeneficiaryTrainingManager` | Beneficiary program management | `frontend/src/components/portal/training/BeneficiaryTrainingManager.tsx` |
| `IndustryTrainingBrowser` | Sector-specific course discovery | `frontend/src/components/portal/training/IndustryTrainingBrowser.tsx` |
| `WorkshopScheduler` | Workshop creation/scheduling | `frontend/src/components/portal/training/WorkshopScheduler.tsx` |
| `AttendanceRecorder` | Workshop attendance interface | `frontend/src/components/portal/training/AttendanceRecorder.tsx` |
| `SETrainingAnalytics` | Training metrics charts | `frontend/src/components/portal/training/SETrainingAnalytics.tsx` |
| `ImpactReportGenerator` | Impact-ready training report | `frontend/src/components/portal/training/ImpactReportGenerator.tsx` |
| `TrainingCalendar` | Calendar view of training | `frontend/src/components/portal/training/TrainingCalendar.tsx` |

### API Endpoints Required
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/portal/training/dashboard` | SE training dashboard stats |
| GET | `/api/v1/portal/training/team` | List team with learning status |
| POST | `/api/v1/portal/training/team/enroll` | Bulk enroll team members |
| GET | `/api/v1/portal/training/team/{id}/progress` | Team member's learning progress |
| GET | `/api/v1/portal/training/courses` | List SE courses |
| POST | `/api/v1/portal/training/courses` | Create SE course |
| PUT | `/api/v1/portal/training/courses/{id}` | Update SE course |
| GET | `/api/v1/portal/training/courses/templates` | Get SE course templates |
| GET | `/api/v1/portal/training/impact` | Impact goal mapping |
| POST | `/api/v1/portal/training/impact/link` | Link training to impact goal |
| GET | `/api/v1/portal/training/workshops` | List SE workshops |
| POST | `/api/v1/portal/training/workshops` | Schedule workshop |
| PUT | `/api/v1/portal/training/workshops/{id}` | Update workshop |
| GET | `/api/v1/portal/training/beneficiaries` | Beneficiary training programs |
| POST | `/api/v1/portal/training/beneficiaries/enroll` | Enroll beneficiaries |
| GET | `/api/v1/portal/training/industry` | Industry-specific courses |
| GET | `/api/v1/portal/training/attendance` | Attendance records |
| POST | `/api/v1/portal/training/attendance` | Record attendance |
| GET | `/api/v1/portal/training/access-codes` | List access codes |
| POST | `/api/v1/portal/training/access-codes` | Generate access codes |
| GET | `/api/v1/portal/training/analytics` | Training analytics |
| GET | `/api/v1/portal/training/reports/impact` | Generate impact report |
| GET | `/api/v1/portal/training/calendar` | Training calendar events |

### Implementation Sequence
1. **Phase 1: Training Dashboard**
   - Dashboard with SE training overview
   - Integration with SE Portal navigation
   - Quick stats and pending items

2. **Phase 2: Team Management**
   - Team progress tracking
   - Bulk enrollment from team roster
   - Individual team member learning status

3. **Phase 3: Impact Alignment**
   - Impact goal mapping interface
   - Training-to-impact connections
   - Impact visualization dashboard

4. **Phase 4: Course Management**
   - SE course creation
   - Course templates for SE contexts
   - Industry-specific course discovery

5. **Phase 5: Workshop & Beneficiary Training**
   - Workshop scheduling
   - Beneficiary training programs
   - Attendance recording

6. **Phase 6: Analytics & Reporting**
   - Training analytics dashboard
   - Impact report generation for stakeholders
   - Calendar view
   - External course recommendations

---

## Implementation Status

*Audited: December 30, 2025*

### Key Pages Status
| Page | Status | Path | Notes |
|------|--------|------|-------|
| Training Dashboard | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/page.tsx` | Overview missing |
| Team Progress | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/team/page.tsx` | Team tracking missing |
| SE Courses | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/courses/page.tsx` | Course catalog missing |
| Create Course | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/courses/create/page.tsx` | Course creation missing |
| Course Builder | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/courses/[id]/edit/page.tsx` | Builder missing |
| Workshops | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/workshops/page.tsx` | Workshop management missing |
| Impact Alignment | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/impact/page.tsx` | Impact mapping missing |
| Schedule Workshop | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/workshops/schedule/page.tsx` | Scheduling missing |
| Industry Training | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/industry/page.tsx` | Sector training missing |
| Beneficiary Training | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/beneficiaries/page.tsx` | Beneficiary programs missing |
| Access Codes | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/access-codes/page.tsx` | Code management missing |
| Attendance | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/attendance/page.tsx` | Attendance records missing |
| Analytics | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/analytics/page.tsx` | Training metrics missing |
| Reports | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/reports/page.tsx` | Impact reports missing |
| Calendar | ❌ Not Implemented | `frontend/src/app/(tenant)/portal/training/calendar/page.tsx` | Schedule view missing |
| Course Catalog (Browse) | ✅ Implemented | `frontend/src/app/(academy)/academy/courses/page.tsx` | External course discovery |

### API Endpoints Status
| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| GET `/api/v1/portal/training/dashboard` | ❌ Not Implemented | - | Training dashboard stats |
| GET `/api/v1/portal/training/team` | ❌ Not Implemented | - | Team learning status |
| POST `/api/v1/portal/training/team/enroll` | ❌ Not Implemented | - | Bulk enrollment |
| GET `/api/v1/portal/training/courses` | ❌ Not Implemented | - | SE courses |
| GET `/api/v1/portal/training/impact` | ❌ Not Implemented | - | Impact goal mapping |
| POST `/api/v1/portal/training/impact/link` | ❌ Not Implemented | - | Link training to impact |
| GET `/api/v1/portal/training/beneficiaries` | ❌ Not Implemented | - | Beneficiary programs |
| GET `/api/v1/portal/training/industry` | ❌ Not Implemented | - | Industry courses |
| GET `/api/v1/portal/training/analytics` | ❌ Not Implemented | - | Training analytics |
| GET `/api/v1/portal/training/reports/impact` | ❌ Not Implemented | - | Impact reports |

### Overall Progress
- **Pages**: 1/16 implemented (6%)
- **APIs**: 0/10 implemented (0%)
