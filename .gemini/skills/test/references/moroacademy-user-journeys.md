# MoroAcademy User Journeys & Test Coverage

This document outlines the user journeys and workflows in MoroAcademy that should be tested using automated tests (unit, integration, E2E) and manual testing.

---

## Implementation Status Summary

| Category | Implemented | Partial | Not Implemented | Total |
|----------|-------------|---------|-----------------|-------|
| Learner Journeys | 28 | 5 | 2 | 35 |
| Provider Journeys | 2 | 0 | 14 | 16 |
| TSP Journeys | 0 | 0 | 17 | 17 |
| Government Agency Journeys | 0 | 0 | 12 | 12 |
| CSEA Provider Journeys | 0 | 0 | 8 | 8 |
| Cooperative/SE Provider | 0 | 0 | 12 | 12 |
| Facilitator Journeys | 10 | 0 | 4 | 14 |
| Platform Admin Journeys | 0 | 0 | 18 | 18 |
| Cross-Cutting Concerns | 3 | 3 | 11 | 17 |
| Simulation & Assessment | 4 | 2 | 2 | 8 |
| **TOTAL** | **47** | **10** | **100** | **157** |

**Overall Implementation: ~30% Implemented, ~6% Partial, ~64% Not Implemented**

### Legend
- ✅ Implemented - Frontend page exists and is functional
- 🚧 Partially Implemented - Page exists but features incomplete or backend integration pending
- ❌ Not Yet Implemented - Feature/page does not exist

---

## Platform Architecture

MoroAcademy is a **multi-provider learning platform** where different organizations can offer training content:

```
MoroAcademy Platform (operated by CSEA)
    |
    +-- Content Providers
        |
        +-- CSEA (Platform Operator + Provider)
        |   +-- Courses (e.g., Cooperative Management)
        |   +-- Workshops (e.g., EDP - Enterprise Development Program)
        |
        +-- Government Agencies
        |   +-- MAFAR (Agriculture training)
        |   +-- MTIT (Trade & Tourism training)
        |   +-- Other BARMM agencies
        |
        +-- Training Service Providers (TSPs)
        |   +-- Accredited external trainers/consultants
        |   +-- Private training organizations
        |
        +-- Cooperatives (as providers)
        |   +-- Peer-to-peer training
        |   +-- Best practice sharing
        |
        +-- Social Enterprises (as providers)
            +-- Industry-specific training
            +-- Mentorship programs
```

---

## User Roles

| Role | Access Level | Primary Actions |
| ---- | ------------ | --------------- |
| **Anonymous** | Public | Browse courses/workshops, view provider pages |
| **Learner** | Authenticated | Enroll, learn, track progress, get certificates |
| **Lightweight Learner** | Access Code | Phone-based registration, workshop participation |
| **Facilitator** | Provider-scoped | Generate codes, take attendance, manage registrations |
| **Provider Admin** | Provider-scoped | Manage own provider's courses, workshops, facilitators |
| **TSP Admin** | TSP-scoped | Manage TSP content, view analytics, manage accreditation |
| **Agency Admin** | Agency-scoped | Manage government agency training content |
| **Platform Admin (CSEA)** | Full | Manage all providers, content, platform settings |

---

## Provider Types

| Type | Code | Description | Example Organizations |
| ---- | ---- | ----------- | --------------------- |
| **CSEA** | `CSEA` | Platform operator and primary provider | CSEA itself |
| **Government Agency** | `GOVERNMENT_AGENCY` | BARMM government agencies | MAFAR, MTIT, MOH |
| **TSP** | `TSP` | Accredited Training Service Providers | External consultants, training firms |
| **Cooperative** | `COOPERATIVE` | Cooperatives offering peer training | NATCCO, regional federations |
| **Social Enterprise** | `SOCIAL_ENTERPRISE` | SEs offering industry training | Social enterprise networks |

---

## 1. Learner Journeys

### 1.1 Registration & Authentication

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ✅ | Standard registration (`/academy/register`) | E2E + Unit | Form validation, email verification, account creation |
| ✅ | Standard login (`/academy/login`) | E2E + Unit | Credentials validation, session management |
| ✅ | Access code join (`/academy/join`) | E2E + Unit | Code validation, lightweight account creation |
| ✅ | Phone-only registration (`/academy/join/phone`) | E2E + Unit | Phone validation, OTP flow |
| ✅ | Access code redemption (`/academy/join/access-code`) | E2E + Unit | Code lookup, workshop auto-enrollment |
| ✅ | Account upgrade (`/academy/join/upgrade`) | E2E + Unit | Convert lightweight to full account |
| ✅ | Session persistence | E2E | Auth state across page navigations |

### 1.2 Course Learning

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ✅ | Browse courses (`/academy/courses`) | E2E + Unit | Listing, filtering by provider, search works |
| ✅ | Filter by provider | E2E | Provider filter shows only that provider's courses |
| ✅ | View course detail (`/academy/courses/[slug]`) | E2E | Course info, provider attribution, curriculum preview |
| 🚧 | Enroll in course | Integration | Enrollment record created, status "ENROLLED" |
| ✅ | Start learning (`/academy/courses/[slug]/learn`) | E2E | First lesson loads, progress initialized |
| 🚧 | Watch video lesson | E2E | Video plays, watch time tracked |
| ✅ | Read text lesson | E2E | Content displays, completion marking |
| 🚧 | Complete quiz | Integration | Quiz submission, score calculation, pass/fail |
| ✅ | View/download document lesson | E2E | PDF/PPTX renders, download works if enabled |
| 🚧 | Progress tracking | Integration | `LessonProgress` records, percentage updates |
| 🚧 | Course completion | Integration | 100% triggers `COMPLETED` status, `completed_at` set |
| 🚧 | Certificate generation | Integration | `Certificate` with provider branding |
| 🚧 | Leave course review | Integration | Rating + review saved, average recalculated |

### 1.3 Workshop Registration

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ✅ | Browse workshops (`/academy/workshops`) | E2E + Unit | Listing, date filtering, provider filtering |
| ✅ | View workshop detail (`/academy/workshops/[slug]`) | E2E | Schedule, trainer info, provider info, registration CTA |
| ✅ | Register for workshop | Integration | Registration created, slot count updated |
| ❌ | Waitlist flow | Integration | Full capacity triggers waitlist status |
| ❌ | Cancel registration | Integration | Status changed, slot freed |

### 1.4 Multi-Day Program Participation

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ✅ | View program detail (`/academy/programs/[slug]`) | E2E | Days, modules, provider info displayed |
| ✅ | Register for program | Integration | `ProgramEnrollment` created |
| ✅ | Attend live session (`/academy/programs/[slug]/live`) | E2E | Current session shown, day progress |
| ✅ | Access attendance view (`/academy/programs/[slug]/attend`) | E2E | Schedule, check-in info |
| ✅ | Fill template (`/academy/programs/[slug]/templates/[code]`) | E2E + Integration | Template loads, auto-save works |
| ✅ | Submit template | Integration | Status changes to `SUBMITTED` |
| ✅ | Take simulation (`/academy/programs/[slug]/simulation`) | E2E | Game loads, team assignment |
| ✅ | Complete pre/post assessment | Integration | Response saved, score calculated |

### 1.5 Provider Discovery

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ✅ | Browse providers (`/academy/providers`) | E2E | All verified providers listed |
| ✅ | Filter providers by type | E2E | TSP, Government, Cooperative filters work |
| ✅ | View provider detail (`/academy/providers/[slug]`) | E2E | Provider info, courses, workshops listed |
| ✅ | View provider courses | E2E | Only that provider's courses shown |
| ✅ | View provider workshops | E2E | Only that provider's workshops shown |
| 🚧 | View provider ratings | E2E | Aggregate rating across all courses |

### 1.6 Cross-Provider Learning

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| 🚧 | Enroll in courses from multiple providers | Integration | Separate enrollments per provider |
| ✅ | My Learning shows all providers | E2E | Courses from CSEA, TSPs, agencies all shown |
| 🚧 | Certificates show correct provider | E2E | Provider branding on each certificate |
| 🚧 | Learning stats aggregate across providers | Unit | Stats include all provider courses |

### 1.7 My Learning Dashboard

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ✅ | View my learning (`/academy/my-learning`) | E2E | Enrolled courses from all providers shown |
| ✅ | Continue learning | E2E | Resumes from last lesson |
| 🚧 | View certificates | E2E | Certificates from all providers listed |
| 🚧 | View learning stats | Unit | Stats aggregate across all providers |

### 1.8 Profile Management

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ✅ | View profile (`/academy/profile`) | E2E | User info, learning history shown |
| ✅ | Update profile | Integration | Changes persisted |

---

## 2. Provider Journeys (All Provider Types)

### 2.1 Provider Onboarding & Registration

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | Apply as TSP | E2E + Integration | Application submitted, status `PENDING` |
| ❌ | Apply as Cooperative provider | E2E + Integration | Links to cooperative entity |
| ❌ | Apply as SE provider | E2E + Integration | Links to SE entity |
| ❌ | Submit accreditation documents | Integration | Documents stored, audit trail |
| ❌ | View application status | E2E | Pending/Approved/Rejected shown |

### 2.2 Provider Verification (Platform Admin)

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | Review provider application | E2E | Application details, documents visible |
| ❌ | Verify provider | Integration | `is_verified` = true, timestamp set |
| ❌ | Reject provider | Integration | Status updated, rejection reason saved |
| ❌ | Set accreditation details | Integration | Accreditation number, expiry saved |

### 2.3 Provider Content Management

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | Provider dashboard | E2E | Only own courses/workshops visible |
| ❌ | Create course (as provider) | E2E + Integration | Course linked to provider |
| ❌ | Edit own course | E2E | Updates persisted |
| ✅ | Cannot edit other provider's course | Integration | 403 Forbidden returned |
| ❌ | Create workshop (as provider) | E2E + Integration | Workshop linked to provider |
| ❌ | View own analytics | E2E | Enrollments, completion rates for own content |
| ✅ | Cannot view other provider's analytics | Integration | Data isolation enforced |

### 2.4 Provider Facilitator Management

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | Add facilitator to provider | Integration | `FacilitatorAuthorization` with PROVIDER scope |
| ❌ | Facilitator sees only provider's workshops | E2E | Workshop list filtered by provider |
| ❌ | Remove facilitator from provider | Integration | Authorization revoked |

---

## 3. TSP (Training Service Provider) Journeys

### 3.1 TSP Accreditation Lifecycle

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | TSP initial application | E2E + Integration | Provider type = TSP, status = PENDING |
| ❌ | Submit training portfolio | Integration | Portfolio documents stored |
| ❌ | Submit trainer credentials | Integration | Trainer qualifications stored |
| ❌ | Accreditation approval | Integration | `accreditation_status` = ACCREDITED |
| ❌ | Accreditation number assigned | Unit | Unique accreditation number generated |
| ❌ | Accreditation expiry set | Integration | `accreditation_expiry` date set |
| ❌ | Accreditation renewal | Integration | Expiry extended, renewal logged |
| ❌ | Accreditation suspension | Integration | Status = SUSPENDED, content hidden |
| ❌ | Accreditation expiry | Scheduled | Status = EXPIRED on expiry date |

### 3.2 TSP Content Creation

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | Create course as TSP | Integration | `provider_type` = TSP on course |
| ❌ | Set trainer info on course | E2E | Trainer name, bio, image saved |
| ❌ | Create workshop as TSP | Integration | Workshop linked to TSP provider |
| ❌ | Set workshop pricing | Integration | Price field saved (if applicable) |
| ❌ | Submit course for review | Integration | Status = PENDING_REVIEW |
| ❌ | Course published | Integration | Status = PUBLISHED after approval |

### 3.3 TSP Analytics & Reporting

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | View TSP dashboard | E2E | Own courses, workshops, enrollments |
| ❌ | View enrollment reports | E2E | Enrollments for own content only |
| ❌ | View completion reports | E2E | Completion rates for own content |
| ❌ | View revenue reports (if applicable) | E2E | Revenue for paid courses |
| ❌ | Export analytics | E2E | CSV/PDF export works |

---

## 4. Government Agency Provider Journeys

### 4.1 Agency Provider Setup

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | Create agency provider (CSEA admin) | Integration | `provider_type` = GOVERNMENT_AGENCY |
| ❌ | Link to existing agency entity | Integration | `entity_id` references agency record |
| ❌ | Assign agency admin | Integration | User linked to provider with admin role |
| ❌ | Agency admin login | E2E | Redirects to agency provider dashboard |

### 4.2 Agency Content Management

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | Create MAFAR course | Integration | Course linked to MAFAR provider |
| ❌ | Create MTIT workshop | Integration | Workshop linked to MTIT provider |
| ❌ | Agency branding on content | E2E | Agency logo, name displayed |
| ❌ | Cross-agency content visibility | E2E | All agency content visible on public listing |

### 4.3 Agency-Specific Programs

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | Create agency-specific program | Integration | Program linked to agency |
| ❌ | Target audience filtering | E2E | Programs can target specific audiences |
| ❌ | Agency staff enrollment | Integration | Internal staff can enroll |
| ❌ | Public enrollment for agency training | Integration | Public users can enroll if allowed |

---

## 5. CSEA as Provider Journeys

CSEA operates the platform AND is a content provider.

### 5.1 CSEA Platform Administration

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | Manage all providers | E2E | CSEA admin sees all providers |
| ❌ | Approve/reject provider applications | Integration | Status updates across providers |
| ❌ | Manage platform settings | E2E | Global settings configurable |
| ❌ | View platform-wide analytics | E2E | All providers' data aggregated |

### 5.2 CSEA as Content Provider

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | Create CSEA course | Integration | Course linked to CSEA provider |
| ❌ | Create CSEA workshop (EDP) | Integration | Workshop linked to CSEA provider |
| ❌ | CSEA content distinguished | E2E | CSEA badge/branding on content |
| ❌ | CSEA facilitators | Integration | Facilitators with GLOBAL scope |

---

## 6. Cooperative/SE as Provider Journeys

### 6.1 Cooperative Provider Setup

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | Cooperative applies as provider | E2E + Integration | Links to cooperative entity |
| ❌ | Cooperative verification | Integration | Verified cooperative can publish |
| ❌ | Cooperative branding | E2E | Coop logo, name on content |

### 6.2 Peer Training Programs

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | Create peer training course | Integration | Coop-to-coop training content |
| ❌ | Target other cooperatives | E2E | Target audience = COOPERATIVE |
| ❌ | Best practice sharing | E2E | Content visible to other coops |
| ❌ | Mentorship workshop | Integration | Workshop for coop mentorship |

### 6.3 SE Provider Programs

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | SE applies as provider | E2E + Integration | Links to SE entity |
| ❌ | Industry-specific training | Integration | SE creates industry content |
| ❌ | SE-to-SE knowledge sharing | E2E | Content available to other SEs |

---

## 7. Facilitator Journeys

### 7.1 Facilitator Authorization Scopes

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ✅ | WORKSHOP scope facilitator | Integration | Access only to specific workshop |
| ✅ | PROVIDER scope facilitator | Integration | Access to all provider's workshops |
| ✅ | GLOBAL scope facilitator (CSEA) | Integration | Access to all platform workshops |
| ✅ | Scope enforcement on code generation | Integration | Cannot generate for unauthorized workshops |

### 7.2 Access Code Management

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ✅ | View code dashboard (`/academy/admin/codes`) | E2E | Codes for authorized workshops only |
| ✅ | Generate single code | Integration | Code created with correct expiry, type |
| ✅ | Generate batch codes | Integration | Multiple codes, batch_id assigned |
| ✅ | Pre-register participant (`/academy/admin/codes/pre-register`) | E2E | Code with participant data created |
| ✅ | View audit log (`/academy/admin/codes/audit`) | E2E | Actions logged, filterable |
| ❌ | Revoke code | Integration | Status changed to `REVOKED` |
| ❌ | Rate limiting | Unit | Daily limit enforced per facilitator |

### 7.3 Workshop Facilitation

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | View registrations | E2E | Participant list for authorized workshop |
| ❌ | Take attendance | Integration | `WorkshopAttendance` created |
| 🚧 | Issue certificate | Integration | Certificate for eligible participants |
| ✅ | View attendance rate | Unit | Rate calculation accurate |

---

## 8. Platform Admin (CSEA) Journeys

### 8.1 Provider Management

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | List all providers | E2E | All provider types listed |
| ❌ | Filter by provider type | E2E | TSP, Agency, Coop, SE filters |
| ❌ | Create provider | Integration | Provider created with type |
| ❌ | Edit provider | E2E | Updates persisted |
| ❌ | Verify provider | Integration | `is_verified` set |
| ❌ | Suspend provider | Integration | Content hidden from public |
| ❌ | Manage accreditation | Integration | Accreditation details updated |

### 8.2 Course Management (Platform-wide)

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | List all courses | E2E | Courses from all providers |
| ❌ | Filter by provider | E2E | Show only specific provider's courses |
| ❌ | Review pending courses | E2E | Courses pending approval listed |
| ❌ | Approve course | Integration | Status = PUBLISHED |
| ❌ | Reject course | Integration | Status = REJECTED, reason saved |
| ❌ | Feature course | Integration | `is_featured` = true |

### 8.3 Workshop Management (Platform-wide)

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | List all workshops | E2E | Workshops from all providers |
| ❌ | Import curriculum | E2E | Curriculum parsed and created |
| ❌ | Manage workshop templates | E2E | Template assignments work |

### 8.4 Platform Settings

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ❌ | Academy settings | E2E | Settings configurable |
| ❌ | Custom domains | E2E | Domain configuration works |
| ❌ | Branding settings | E2E | Logo, colors configurable |

---

## 9. Cross-Cutting Concerns

### 9.1 Data Isolation by Provider

| Status | Test | Type | Assertions |
| ------ | ---- | ---- | ---------- |
| ✅ | Provider content isolation | Integration | Each provider sees only their content |
| 🚧 | Provider analytics isolation | Integration | Analytics scoped to provider |
| ✅ | Facilitator scope enforcement | Unit | WORKSHOP/PROVIDER/GLOBAL respected |
| ✅ | Learner sees all providers | E2E | Public content from all providers visible |

### 9.2 Multi-Provider Data Integrity

| Status | Test | Type | Assertions |
| ------ | ---- | ---- | ---------- |
| ❌ | Course-provider relationship | Unit | Course always has provider |
| ❌ | Workshop-provider relationship | Unit | Workshop always has provider |
| ❌ | Enrollment tracks provider | Integration | Provider info in enrollment |
| 🚧 | Certificate shows provider | Integration | Provider branding on certificate |

### 9.3 Security

| Status | Test | Type | Assertions |
| ------ | ---- | ---- | ---------- |
| ✅ | Access code hashing | Unit | Codes stored as SHA-256 hash |
| ❌ | Rate limiting | Unit | Redemption attempts limited |
| ✅ | Audit logging | Integration | All sensitive actions logged |
| ✅ | Permission checks | Integration | Unauthorized access denied |
| ✅ | Provider admin cannot access other providers | Integration | 403 on cross-provider access |

### 9.4 Progress & Completion

| Status | Test | Type | Assertions |
| ------ | ---- | ---- | ---------- |
| 🚧 | Progress calculation | Unit | `progress_percent` formula accurate |
| 🚧 | Status transitions | Unit | ENROLLED -> IN_PROGRESS -> COMPLETED |
| 🚧 | Completion triggers | Integration | 100% triggers certificate generation |
| 🚧 | Provider-branded certificate | Integration | Certificate shows provider info |

### 9.5 Gamification

| Status | Test | Type | Assertions |
| ------ | ---- | ---- | ---------- |
| ❌ | Badge awarding | Integration | Correct badges for achievements |
| ❌ | Badge uniqueness | Unit | No duplicate badge awards |
| ❌ | Cross-provider badges | Integration | Badges from any provider's content |

---

## 10. Simulation & Assessment Flows

### 10.1 Simulation (EDP-style)

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| ✅ | Team assignment | Integration | Participants assigned to teams |
| ✅ | Round progression | E2E | Rounds advance correctly |
| ✅ | Transaction recording | Integration | Purchases, loans tracked |
| ✅ | Score calculation | Unit | Winning criteria applied |

### 10.2 Assessments

| Status | Journey | Test Type | Key Assertions |
| ------ | ------- | --------- | -------------- |
| 🚧 | Pre-assessment | E2E | Questions display, responses saved |
| 🚧 | Post-assessment | E2E + Integration | Score calculated, pass/fail determined |
| ❌ | Quiz attempt tracking | Unit | Attempt count incremented |

---

## 11. Test Priority Matrix

| Priority | Workflow | Status | Reason |
| -------- | -------- | ------ | ------ |
| **P0 (Critical)** | Registration/Login, Course Enrollment, Access Code Redemption | ✅ | Core user acquisition |
| **P0 (Critical)** | Lesson Completion, Progress Tracking | 🚧 | Core learning experience |
| **P0 (Critical)** | Provider content isolation | ✅ | Data security |
| **P1 (High)** | Certificate Generation, Workshop Registration | 🚧 | Key outcomes |
| **P1 (High)** | Provider onboarding, TSP accreditation | ❌ | Provider ecosystem |
| **P1 (High)** | Code Generation (Facilitator), Provider Admin CRUD | 🚧 | Operational workflows |
| **P2 (Medium)** | Simulation, Multi-day Programs | ✅ | Advanced features |
| **P2 (Medium)** | Reviews, Comments, Badges | ❌ | Engagement features |
| **P2 (Medium)** | Cross-provider analytics | ❌ | Reporting features |
| **P3 (Low)** | Platform settings, Domain Config | ❌ | Admin-only, infrequent |

---

## 12. Manual Testing Checklist

### Core Functionality

- [x] **Video playback** - YouTube embeds, watch time tracking accuracy ✅
- [x] **PDF/PPTX rendering** - Document viewer across browsers ✅
- [ ] **Mobile responsiveness** - All pages on mobile viewports 🚧
- [ ] **Email notifications** - Registration, certificates, reminders ❌
- [x] **QR code generation** - Access code QR codes scannable ✅
- [x] **Live session UX** - Real-time session indicators during workshop ✅

### Provider-Specific

- [x] **Provider branding** - Logos, colors display correctly ✅
- [ ] **TSP accreditation badge** - Displayed on TSP content ❌
- [ ] **Government agency branding** - Agency logos on content ❌
- [ ] **Certificate provider attribution** - Correct provider on certificate 🚧
- [x] **Cross-provider navigation** - Smooth switching between providers ✅

### Edge Cases

- [ ] **Offline behavior** - What happens when connection drops ❌
- [ ] **Performance under load** - Multiple concurrent enrollments ❌
- [ ] **Accreditation expiry** - TSP content hidden after expiry ❌
- [ ] **Provider suspension** - Content hidden when provider suspended ❌

---

## 13. Related Models

### Provider Model (backend/apps/training/models.py)

```python
class ContentProvider(models.Model):
    PROVIDER_TYPE_CHOICES = [
        ('CSEA', 'CSEA'),
        ('COOPERATIVE', 'Cooperative'),
        ('SOCIAL_ENTERPRISE', 'Social Enterprise'),
        ('TSP', 'Training Service Provider'),
        ('GOVERNMENT_AGENCY', 'Government Agency'),
    ]

    ACCREDITATION_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCREDITED', 'Accredited'),
        ('SUSPENDED', 'Suspended'),
        ('EXPIRED', 'Expired'),
    ]
```

### Facilitator Authorization Model

```python
class FacilitatorAuthorizationType(models.TextChoices):
    WORKSHOP = 'WORKSHOP', 'Specific Workshop Only'
    PROVIDER = 'PROVIDER', 'All Provider Workshops'
    GLOBAL = 'GLOBAL', 'All Workshops (Admin Only)'
```

### Core Models (backend/apps/training/models.py)

- `Course`, `CourseModule`, `Lesson`, `LessonProgress`
- `Enrollment`, `Certificate`, `CourseReview`
- `Workshop`, `WorkshopSchedule`, `WorkshopRegistration`, `WorkshopAttendance`
- `ContentProvider`
- `LearnerBadge`, `LessonComment`

### Program Models (backend/apps/training/models_program.py)

- `WorkshopProgram`, `ProgramDay`, `ProgramModule`, `ModuleSession`
- `WorkshopTemplate`, `SimulationConfig`, `ProgramAssessment`

### Participant Models (backend/apps/training/models_participant.py)

- `ProgramEnrollment`, `TemplateSubmission`, `AssessmentResponse`
- `OutputReview`, `SessionAttendance`, `ProgramTemplateAssignment`

### Access Models (backend/apps/training/models_access.py)

- `AccessCode`, `FacilitatorAuthorization`, `AccessCodeAuditLog`

### Simulation Models (backend/apps/training/models_simulation.py)

- `SimulationSession`, `SimulationTeam`, `SimulationTeamMember`
- `SimulationInventoryItem`, `SimulationLoan`, `SimulationTransaction`

---

## 14. Frontend Routes Reference

### Public Academy Routes (`/academy/...`)

| Status | Route | Description |
| ------ | ----- | ----------- |
| ✅ | `/academy` | Homepage |
| ✅ | `/academy/courses` | Course listing (all providers) |
| ✅ | `/academy/courses/[slug]` | Course detail |
| ✅ | `/academy/courses/[slug]/learn` | Learning interface |
| ✅ | `/academy/workshops` | Workshop listing (all providers) |
| ✅ | `/academy/workshops/[slug]` | Workshop detail |
| ✅ | `/academy/programs/[slug]` | Program detail |
| ✅ | `/academy/programs/[slug]/live` | Live session view |
| ✅ | `/academy/programs/[slug]/attend` | Attendance view |
| ✅ | `/academy/programs/[slug]/templates/[code]` | Template filling |
| ✅ | `/academy/programs/[slug]/simulation` | Simulation game |
| ✅ | `/academy/providers` | Provider directory |
| ✅ | `/academy/providers/[slug]` | Provider detail |
| ✅ | `/academy/my-learning` | Learner dashboard |
| ✅ | `/academy/profile` | User profile |
| ✅ | `/academy/login` | Login |
| ✅ | `/academy/register` | Registration |
| ✅ | `/academy/join` | Lightweight join flow |
| ✅ | `/academy/join/phone` | Phone registration |
| ✅ | `/academy/join/access-code` | Code redemption |
| ✅ | `/academy/join/upgrade` | Account upgrade |
| ✅ | `/academy/join/complete` | Join completion |
| ✅ | `/academy/edp/*` | EDP modules |

### Admin Routes (`/academy/admin/...`)

| Status | Route | Description |
| ------ | ----- | ----------- |
| ❌ | `/academy/admin` | Admin dashboard |
| ❌ | `/academy/admin/courses` | Course management |
| ❌ | `/academy/admin/courses/new` | Create course |
| ❌ | `/academy/admin/courses/[id]` | Edit course |
| ❌ | `/academy/admin/courses/[id]/curriculum` | Manage curriculum |
| ❌ | `/academy/admin/workshops` | Workshop management |
| ❌ | `/academy/admin/workshops/new` | Create workshop |
| ❌ | `/academy/admin/workshops/[id]` | Edit workshop |
| ❌ | `/academy/admin/workshops/[id]/curriculum` | Manage curriculum |
| ❌ | `/academy/admin/providers` | Provider management |
| ❌ | `/academy/admin/providers/[id]` | Edit provider |
| ❌ | `/academy/admin/settings` | Academy settings |
| ❌ | `/academy/admin/settings/domains` | Custom domains |

### Facilitator Routes (`/academy/admin/codes/...`)

| Status | Route | Description |
| ------ | ----- | ----------- |
| ✅ | `/academy/admin/codes` | Code dashboard |
| ✅ | `/academy/admin/codes/pre-register` | Pre-registration |
| ✅ | `/academy/admin/codes/audit` | Audit log |
