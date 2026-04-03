# CRITS (Cooperative Research Information and Training Section) - User Journey on MoroAcademy

## Overview
The Cooperative Research Information and Training Section (CRITS) is CSEA's unit responsible for cooperative education, training, and research - equivalent to CDA's Cooperative Research Information and Training Division (CRITD). CRITS staff exercise **regulatory oversight** on MoroAcademy, approving training service providers, monitoring content quality, and ensuring regulatory compliance.

**Important**: MoroAcademy is an **independent platform** - it is NOT owned or managed by CSEA. CRITS performs regulatory functions on the platform but does not manage platform settings, users, or technical administration. Platform management is handled by the **MoroAcademy Admin** (not a CSEA staff) and **Django Superuser**.

## Platform Independence
| Aspect | CSEA/CRITS | MoroAcademy Platform |
|--------|------------|---------------------|
| **Authority** | Full regulatory authority over cooperatives | Independent platform |
| **Ownership** | Government agency | NOT owned by CSEA or CDA |
| **Role on Platform** | Regulatory functions only | Managed by MoroAcademy Admin |
| **Platform Management** | NO access | MoroAcademy Admin + Django Superuser |

## Role Definition
**Type**: Regulator (Government)
**Portal Access**: CSEA regulatory dashboard (`/csea/training/*`)
**Authentication**: CSEA staff account (government credentials)
**Regulatory Scope**: Oversight of TSPs, content quality, and compliance on MoroAcademy

## Capabilities

### Core Capabilities (Regulatory Functions)
| Capability | Description | Priority |
|------------|-------------|----------|
| Approve TSPs | Review and approve training service providers | P0 |
| Monitor All Providers | Oversee TSPs, Coops, SEs training activities | P0 |
| Review Content | Quality assurance for published courses | P0 |
| Manage CSEA Courses | Create and manage CSEA official training | P0 |
| View Regulatory Analytics | Training metrics for regulatory oversight | P0 |
| Manage Accreditation | TSP accreditation approval and renewal | P0 |
| Issue CSEA Certificates | Official CSEA certifications | P1 |
| Handle Regulatory Appeals | Review content and provider compliance appeals | P2 |
| Generate Compliance Reports | Regulatory reporting | P1 |
| Define Compliance Requirements | Training compliance standards | P1 |
| Audit Provider Compliance | Review provider activity for compliance | P2 |

### Feature Access Matrix
| Feature | Access Level | Notes |
|---------|--------------|-------|
| Platform Settings | NONE | Managed by MoroAcademy Admin |
| TSP Management | Regulatory | Approve, suspend, revoke accreditation |
| All Courses | Review | View, review quality, flag for compliance |
| All Workshops | View | Monitor for compliance |
| All Learners | View | Aggregate data for regulatory reporting |
| CSEA Certificates | Full | Issue CSEA-specific certifications |
| Regulatory Analytics | Full | Compliance and oversight metrics |
| Financial Data | NONE | Platform revenue managed by MoroAcademy Admin |
| User Management | NONE | Managed by MoroAcademy Admin |
| CSEA Courses | Full | Create/manage official CSEA training |
| Content Moderation | Regulatory | Flag non-compliant content |
| Compliance Standards | Full | Define regulatory requirements |

## User Journey Entry Points
1. **CSEA Portal** - Navigate from CSEA portal to training regulatory oversight
2. **Regulatory Dashboard** - Direct access to CRITS oversight functions
3. **TSP Approval Queue** - TSP accreditation pending approval notification
4. **Compliance Alert** - Provider compliance issue detected
5. **Executive Report Request** - Prepare briefing for CSEA leadership
6. **Compliance Escalation** - Provider or content compliance issue

## Key Pages
| Page | Purpose | Implementation |
|------|---------|----------------|
| Regulatory Dashboard `/csea/training` | CRITS oversight overview | Planned |
| TSP Management `/csea/training/tsps` | TSP accreditation oversight | Planned |
| TSP Approval `/csea/training/tsps/pending` | Pending accreditation applications | Planned |
| TSP Detail `/csea/training/tsps/[id]` | Individual TSP compliance view | Planned |
| Course Review `/csea/training/courses` | Content quality monitoring | Planned |
| Course Quality Review `/csea/training/courses/[id]/review` | Individual course compliance review | Planned |
| CSEA Courses `/csea/training/csea-courses` | Official CSEA training management | Planned |
| Workshop Monitoring `/csea/training/workshops` | Workshop compliance oversight | Planned |
| CSEA Certificates `/csea/training/certificates` | CSEA certificate issuance | Planned |
| Certificate Verification `/csea/training/certificates/verify` | Public verification | Planned |
| Regulatory Analytics `/csea/training/analytics` | Compliance metrics | Planned |
| Compliance Standards `/csea/training/compliance` | Define compliance requirements | Planned |
| Compliance Reports `/csea/training/reports` | Regulatory report generation | Planned |
| Compliance Appeals `/csea/training/appeals` | Handle compliance appeals | Planned |

**Note**: Platform administration pages (Settings, User Management, Audit Log) are managed by MoroAcademy Admin, not CRITS.

## Role Progression
**From**:
- CSEA Staff (assigned to CRITS)
- Cooperative Development Specialist (transitioned to CRITS)

**To**:
- CRITS Section Chief (senior oversight role)
- Cross-Agency Training Lead (multi-ministry coordination)
- Policy Development (training policy formulation)

**Requirements**:
- CSEA employment or official designation
- Government security clearance
- Training in cooperative education and regulatory oversight
- Understanding of cooperative and SE sector per RA 9520

## Pain Points
1. **High Approval Volume** - Too many TSP accreditation applications pending
2. **Quality Assurance Difficult** - Hard to review all content for compliance
3. **Multi-Provider Coordination** - Complex provider landscape across TSPs, Coops, SEs
4. **Compliance Monitoring Manual** - No automated compliance checking
5. **Report Generation Time-Consuming** - Manual data compilation for regulatory reports
6. **Limited Compliance Visibility** - Cannot see real-time compliance status
7. **No Predictive Analytics** - Cannot anticipate compliance issues
8. **Integration Gaps** - Not connected to other CSEA regulatory systems
9. **Policy Implementation Lag** - Slow to implement new training requirements
10. **Coordination with Platform Admin** - Need to coordinate with MoroAcademy Admin for platform-level issues

## Improvement Opportunities
1. **Accreditation Workflow Automation** - Auto-checks before manual TSP review
2. **AI Content Compliance Review** - Automated compliance screening
3. **Provider Compliance Dashboard** - Real-time provider compliance monitoring
4. **Compliance Automation** - Automatic requirement tracking
5. **One-Click Regulatory Reports** - Pre-configured compliance reports
6. **Real-Time Compliance Dashboard** - Live compliance status view
7. **Predictive Compliance Analytics** - ML-based compliance issue prediction
8. **CSEA System Integration** - Connect to other CSEA regulatory systems
9. **Policy Templates** - Quick implementation of new training requirements
10. **Bulk Compliance Actions** - Mass compliance reviews for efficiency
11. **Compliance Alerts** - Smart alerts for compliance issues

## Success Metrics
- **TSP Accreditation Rate**: TSPs approved vs rejected
- **Accreditation Turnaround**: Average days to process TSP applications
- **Content Compliance Rate**: Percentage of courses meeting quality standards
- **Provider Compliance Rate**: Percentage of providers in good standing
- **CSEA Certificate Issuance**: CSEA certificates issued per month
- **Compliance Issue Resolution**: Average time to resolve compliance issues
- **Accreditation Renewals**: On-time renewal rate
- **Training Coverage**: Percentage of coops/SEs with active training programs
- **Regulatory Report Timeliness**: Reports submitted on schedule

## CRITS Regulatory Dashboard
```
┌─────────────────────────────────────────────────────────┐
│ CRITS Regulatory Oversight Dashboard                    │
├─────────────────────────────────────────────────────────┤
│ Accredited TSPs: 34              │ Pending TSPs: 8       │
│ Compliant Providers: 89%         │ Compliance Issues: 3  │
│ Courses Reviewed: 245            │ Pending Reviews: 23   │
│ CSEA Certificates Issued: 1,230  │ Appeals: 2            │
├─────────────────────────────────────────────────────────┤
│ Quick Actions: [Approve TSP] [Review Course] [Report]   │
└─────────────────────────────────────────────────────────┘
```

## Accreditation & Compliance Workflows
| Item | Workflow | SLA |
|------|----------|-----|
| TSP Accreditation | Submit -> Document Review -> Interview -> Accreditation/Reject | 14 days |
| Course Compliance Review | Flag -> Compliance Check -> Review -> Approve/Require Revision | 5 days |
| CSEA Certificate Design | Submit -> Compliance Check -> Design Review -> Approve | 3 days |
| Compliance Appeal | Submit -> Initial Review -> Investigation -> Decision | 7 days |
| Accreditation Renewal | Notice -> Document Update -> Review -> Renew/Suspend | 30 days |

## Compliance Framework
| Requirement | Frequency | Monitored By |
|-------------|-----------|--------------|
| TSP Accreditation | Annual | CRITS Manual Review |
| Course Quality Standards | Continuous | AI + CRITS Review |
| Instructor Credentials | Initial + Annual | CRITS Document verification |
| Content Accuracy | Continuous | Community Reports + CRITS Review |
| Provider Compliance | Quarterly | CRITS Automated Reports |
| Regulatory Reporting | Quarterly | CRITS |

**Note**: Platform-level audits (data privacy, system security) are managed by MoroAcademy Admin.

## UI/UX Considerations
- Regulatory dashboard with compliance KPIs at a glance
- Clear accreditation approval queues with priority indicators
- One-click actions for common regulatory tasks
- Drill-down capability from aggregate compliance to provider detail
- Visual compliance status across all providers
- Regulatory report builder
- Alert configuration for compliance issues
- Compliance history with search and filter
- Mobile access for urgent accreditation approvals
- Export capabilities for regulatory reports

---

## Implementation Plan

### Access Control
- Authentication required with `crits_staff` or `crits_chief` role
- **Regulatory oversight access** - VIEW/REVIEW scope across all providers for compliance
- Middleware: `withCRITSAccess` verifying CSEA/CRITS staff credentials
- View access to all TSPs, Coops, SEs, courses for compliance monitoring
- Full control only for: TSP accreditation, compliance standards, CSEA courses/certificates
- NO access to: Platform settings, user management, financial data (managed by MoroAcademy Admin)
- Integration with CSEA Portal authentication (government credentials)
- Audit logging for all regulatory actions

### Priority Pages
| Priority | Page | Route | File Path |
|----------|------|-------|-----------|
| P0 | Regulatory Dashboard | `/csea/training` | `frontend/src/app/(admin)/csea/training/page.tsx` |
| P0 | TSP Accreditation | `/csea/training/tsps` | `frontend/src/app/(admin)/csea/training/tsps/page.tsx` |
| P0 | TSP Approval Queue | `/csea/training/tsps/pending` | `frontend/src/app/(admin)/csea/training/tsps/pending/page.tsx` |
| P0 | TSP Compliance Detail | `/csea/training/tsps/[id]` | `frontend/src/app/(admin)/csea/training/tsps/[id]/page.tsx` |
| P0 | Course Compliance Review | `/csea/training/courses` | `frontend/src/app/(admin)/csea/training/courses/page.tsx` |
| P0 | Course Quality Review | `/csea/training/courses/[id]/review` | `frontend/src/app/(admin)/csea/training/courses/[id]/review/page.tsx` |
| P0 | CSEA Official Courses | `/csea/training/csea-courses` | `frontend/src/app/(admin)/csea/training/csea-courses/page.tsx` |
| P1 | Workshop Compliance | `/csea/training/workshops` | `frontend/src/app/(admin)/csea/training/workshops/page.tsx` |
| P1 | CSEA Certificates | `/csea/training/certificates` | `frontend/src/app/(admin)/csea/training/certificates/page.tsx` |
| P1 | Certificate Verification | `/csea/training/certificates/verify` | `frontend/src/app/(admin)/csea/training/certificates/verify/page.tsx` |
| P1 | Regulatory Analytics | `/csea/training/analytics` | `frontend/src/app/(admin)/csea/training/analytics/page.tsx` |
| P1 | Compliance Standards | `/csea/training/compliance` | `frontend/src/app/(admin)/csea/training/compliance/page.tsx` |
| P2 | Regulatory Reports | `/csea/training/reports` | `frontend/src/app/(admin)/csea/training/reports/page.tsx` |
| P2 | Compliance Appeals | `/csea/training/appeals` | `frontend/src/app/(admin)/csea/training/appeals/page.tsx` |

**Note**: Platform admin pages (User Management, Settings, Audit Log) are NOT part of CRITS scope - managed by MoroAcademy Admin.

### Role-Specific Components
| Component | Purpose | File Path |
|-----------|---------|-----------|
| `CRITSDashboard` | Regulatory KPI dashboard | `frontend/src/components/csea/training/CRITSDashboard.tsx` |
| `TSPAccreditationTable` | TSP accreditation management | `frontend/src/components/csea/training/TSPAccreditationTable.tsx` |
| `TSPApprovalQueue` | Pending TSP accreditation applications | `frontend/src/components/csea/training/TSPApprovalQueue.tsx` |
| `TSPComplianceView` | Individual TSP compliance view | `frontend/src/components/csea/training/TSPComplianceView.tsx` |
| `CourseComplianceTable` | Course compliance review list | `frontend/src/components/csea/training/CourseComplianceTable.tsx` |
| `CourseQualityReview` | Course quality compliance review | `frontend/src/components/csea/training/CourseQualityReview.tsx` |
| `CSEACourseManager` | Official CSEA training management | `frontend/src/components/csea/training/CSEACourseManager.tsx` |
| `RegulatoryAnalytics` | Compliance analytics | `frontend/src/components/csea/training/RegulatoryAnalytics.tsx` |
| `ComplianceMonitor` | Provider compliance monitoring | `frontend/src/components/csea/training/ComplianceMonitor.tsx` |
| `CSEACertificateManager` | CSEA certificate issuance | `frontend/src/components/csea/training/CSEACertificateManager.tsx` |
| `CertificateVerifier` | Certificate verification tool | `frontend/src/components/csea/training/CertificateVerifier.tsx` |
| `RegulatoryReportBuilder` | Compliance report generator | `frontend/src/components/csea/training/RegulatoryReportBuilder.tsx` |
| `ComplianceAppealHandler` | Compliance appeals | `frontend/src/components/csea/training/ComplianceAppealHandler.tsx` |

### API Endpoints Required
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/csea/training/dashboard` | Regulatory KPIs |
| GET | `/api/v1/csea/training/tsps` | List all TSPs for accreditation |
| GET | `/api/v1/csea/training/tsps/pending` | Pending TSP accreditation applications |
| GET | `/api/v1/csea/training/tsps/{id}` | TSP compliance details |
| PUT | `/api/v1/csea/training/tsps/{id}/accredit` | Accredit TSP |
| PUT | `/api/v1/csea/training/tsps/{id}/reject` | Reject TSP accreditation |
| PUT | `/api/v1/csea/training/tsps/{id}/suspend` | Suspend TSP accreditation |
| GET | `/api/v1/csea/training/courses` | Courses for compliance review |
| GET | `/api/v1/csea/training/courses/flagged` | Courses flagged for compliance |
| PUT | `/api/v1/csea/training/courses/{id}/compliance-approve` | Approve course compliance |
| PUT | `/api/v1/csea/training/courses/{id}/compliance-flag` | Flag course for compliance issue |
| GET | `/api/v1/csea/training/csea-courses` | CSEA official courses |
| POST | `/api/v1/csea/training/csea-courses` | Create CSEA course |
| GET | `/api/v1/csea/training/workshops` | Workshops for compliance monitoring |
| GET | `/api/v1/csea/training/certificates` | CSEA certificates |
| POST | `/api/v1/csea/training/certificates` | Issue CSEA certificate |
| GET | `/api/v1/csea/training/certificates/verify/{code}` | Verify certificate |
| GET | `/api/v1/csea/training/analytics` | Regulatory analytics |
| GET | `/api/v1/csea/training/compliance` | Compliance standards |
| POST | `/api/v1/csea/training/compliance` | Define compliance requirement |
| GET | `/api/v1/csea/training/reports` | Generate regulatory reports |
| GET | `/api/v1/csea/training/appeals` | List compliance appeals |
| PUT | `/api/v1/csea/training/appeals/{id}/resolve` | Resolve compliance appeal |

**Note**: Platform management endpoints (users, settings, audit) are NOT exposed to CRITS - managed by MoroAcademy Admin.

### Implementation Sequence
1. **Phase 1: Regulatory Dashboard**
   - CRITS dashboard with regulatory KPIs
   - Quick actions for pending accreditations
   - Compliance alert notifications

2. **Phase 2: TSP Accreditation**
   - TSP accreditation list with status filtering
   - TSP accreditation approval workflow
   - Individual TSP compliance view

3. **Phase 3: Course Compliance**
   - Course compliance review list
   - Course quality review workflow
   - CSEA official course creation

4. **Phase 4: Compliance Standards**
   - Define compliance requirements
   - Provider compliance monitoring
   - Accreditation tracking

5. **Phase 5: Regulatory Reporting**
   - Regulatory analytics dashboard
   - Compliance report builder
   - Export capabilities

6. **Phase 6: Certificates & Appeals**
   - CSEA certificate issuance
   - Certificate verification
   - Compliance appeal handling

---

## Implementation Status

*Audited: December 30, 2025*

**Note**: The pages below under `(academy-admin)` are **MoroAcademy Admin** pages, NOT CRITS pages. CRITS regulatory pages are under `(admin)/csea/training/`.

### MoroAcademy Admin Pages (NOT CRITS - for reference only)
| Page | Status | Path | Notes |
|------|--------|------|-------|
| Admin Dashboard | ✅ Implemented | `frontend/src/app/(academy-admin)/academy/admin/page.tsx` | Platform admin (not CRITS) |
| Admin Login | ✅ Implemented | `frontend/src/app/(academy-admin)/academy/admin/login/page.tsx` | Platform authentication |
| All Courses | ✅ Implemented | `frontend/src/app/(academy-admin)/academy/admin/courses/page.tsx` | Platform course management |
| All Providers | ✅ Implemented | `frontend/src/app/(academy-admin)/academy/admin/providers/page.tsx` | Platform provider list |
| Provider Detail | ✅ Implemented | `frontend/src/app/(academy-admin)/academy/admin/providers/[id]/page.tsx` | Platform provider detail |
| All Workshops | ✅ Implemented | `frontend/src/app/(academy-admin)/academy/admin/workshops/page.tsx` | Platform workshop management |
| Settings | ✅ Implemented | `frontend/src/app/(academy-admin)/academy/admin/settings/page.tsx` | Platform settings |
| Domain Settings | ✅ Implemented | `frontend/src/app/(academy-admin)/academy/admin/settings/domains/page.tsx` | Custom domains |

### CRITS Regulatory Pages Status
| Page | Status | Path | Notes |
|------|--------|------|-------|
| Regulatory Dashboard | ❌ Not Implemented | `frontend/src/app/(admin)/csea/training/page.tsx` | CRITS dashboard missing |
| TSP Accreditation | ❌ Not Implemented | `frontend/src/app/(admin)/csea/training/tsps/page.tsx` | TSP accreditation missing |
| TSP Approval Queue | ❌ Not Implemented | `frontend/src/app/(admin)/csea/training/tsps/pending/page.tsx` | Approval queue missing |
| Course Compliance | ❌ Not Implemented | `frontend/src/app/(admin)/csea/training/courses/page.tsx` | Compliance review missing |
| CSEA Certificates | ❌ Not Implemented | `frontend/src/app/(admin)/csea/training/certificates/page.tsx` | CSEA certificate issuance missing |
| Regulatory Analytics | ❌ Not Implemented | `frontend/src/app/(admin)/csea/training/analytics/page.tsx` | Compliance analytics missing |
| Compliance Standards | ❌ Not Implemented | `frontend/src/app/(admin)/csea/training/compliance/page.tsx` | Standards management missing |
| Regulatory Reports | ❌ Not Implemented | `frontend/src/app/(admin)/csea/training/reports/page.tsx` | Report generation missing |
| Compliance Appeals | ❌ Not Implemented | `frontend/src/app/(admin)/csea/training/appeals/page.tsx` | Appeal handling missing |

### CRITS API Endpoints Status
| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| GET `/api/v1/csea/training/dashboard` | ❌ Not Implemented | - | Regulatory KPIs |
| GET `/api/v1/csea/training/tsps` | ❌ Not Implemented | - | TSP accreditation list |
| GET `/api/v1/csea/training/tsps/pending` | ❌ Not Implemented | - | Pending accreditations |
| PUT `/api/v1/csea/training/tsps/{id}/accredit` | ❌ Not Implemented | - | TSP accreditation |
| GET `/api/v1/csea/training/courses` | ❌ Not Implemented | - | Compliance review list |
| GET `/api/v1/csea/training/compliance` | ❌ Not Implemented | - | Compliance standards |
| GET `/api/v1/csea/training/certificates` | ❌ Not Implemented | - | CSEA certificates |
| GET `/api/v1/csea/training/appeals` | ❌ Not Implemented | - | Compliance appeals |

### Overall CRITS Progress
- **Pages**: 0/9 implemented (0%)
- **APIs**: 0/8 implemented (0%)
