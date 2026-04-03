# CSEA Agency Staff - MoroNegosyo

## Overview
CSEA (Cooperative and Social Enterprise Authority) Staff are government employees who oversee cooperatives and social enterprises in the Bangsamoro region through MoroNegosyo. They access the Agency Admin Portal to manage registrations, review compliance, approve applications, monitor platform activity, and generate reports for CSEA leadership. This role represents the regulatory and oversight function of the platform.

## Role Definition
**Type**: Authenticated Admin User (Government Staff)
**Portal Access**: CSEA Admin Portal (`/csea`), Public Portal (`/`), limited Tenant Portal view
**Authentication**: Email/Password with mandatory 2FA, CSEA domain email required

## Capabilities

### Core Capabilities
| Capability | Description | Priority |
|------------|-------------|----------|
| Registration Oversight | Review and approve coop/SE applications | P0 |
| Compliance Monitoring | Track FRAMES compliance, SE verification | P0 |
| Document Verification | Review submitted compliance documents | P0 |
| Application Approval | Approve/reject manager applications | P0 |
| Tenant Management | View and manage all coop/SE tenants | P0 |
| Analytics Dashboard | Platform-wide metrics and insights | P1 |
| User Management | Manage consumer and tenant accounts | P1 |
| Report Generation | Create compliance and activity reports | P1 |
| Audit Trail | View all platform activity logs | P1 |
| Communication Tools | Send notifications to tenants | P2 |
| Content Moderation | Review flagged products, reviews | P2 |
| Custom Domain Config | Configure tenant custom domains | P2 |
| MoroAcademy Admin | Manage training content, enrollments | P2 |
| System Configuration | Platform settings, categories | P3 |
| Role Management | Assign staff roles and permissions | P3 |

### Feature Access Matrix
| Feature | Access Level | Notes |
|---------|--------------|-------|
| CSEA Dashboard | Full | Primary workspace |
| Tenant Directory | Full | All coop/SE records |
| Registration Queue | Full | Review and approve |
| Compliance Dashboard | Full | All compliance data |
| Document Repository | Full | All uploaded documents |
| User Management | Full | All platform users |
| Analytics | Full | All platform metrics |
| Report Builder | Full | All report types |
| Audit Logs | Full | Complete activity history |
| Communication Hub | Full | Notifications, announcements |
| Content Moderation | Full | Products, reviews, content |
| MoroAcademy Admin | Full | Courses, enrollments |
| System Settings | Varies | Based on staff role |
| Public Portal | Full | Consumer capabilities |
| Tenant Portal | View Only | Cannot modify tenant data |

## User Journey Entry Points

1. **Morning Dashboard Review**
   - Staff logs in at start of workday
   - Reviews pending applications, alerts
   - Path: Login > Dashboard > Review Queue

2. **Registration Review**
   - New coop/SE application notification
   - Reviews documents, makes decision
   - Path: Email > Application > Review > Approve/Reject

3. **Compliance Alert**
   - Non-compliant tenant flagged
   - Staff investigates, takes action
   - Path: Alert > Tenant Profile > Compliance > Action

4. **Report Request**
   - Leadership requests monthly report
   - Staff generates and exports report
   - Path: Dashboard > Reports > Generate > Export

5. **Support Escalation**
   - Tenant support request escalated
   - Staff reviews and resolves issue
   - Path: Support Queue > Ticket > Investigate > Resolve

6. **Audit Investigation**
   - Suspicious activity flagged
   - Staff reviews audit trail
   - Path: Audit Logs > Filter > Investigate > Document

## Key Pages

### CSEA Admin Portal Pages
| Page | Purpose | Route | Implementation |
|------|---------|-------|----------------|
| Dashboard | Overview, alerts, pending items | `/csea` | Active |
| Registration Queue | Pending coop/SE applications | `/csea/registrations` | Active |
| Application Detail | Review single application | `/csea/registrations/[id]` | Active |
| Tenant Directory | All registered coop/SEs | `/csea/tenants` | Active |
| Tenant Profile | Single tenant details | `/csea/tenants/[id]` | Active |
| Compliance Overview | All tenants compliance status | `/csea/compliance` | Active |
| FRAMES Dashboard | Cooperative compliance | `/csea/compliance/frames` | Planned |
| SE Verification | SE compliance | `/csea/compliance/se` | Planned |
| User Management | All platform users | `/csea/users` | Planned |
| Analytics | Platform metrics | `/csea/analytics` | Planned |
| Reports | Report generation | `/csea/reports` | Planned |
| Audit Logs | Activity history | `/csea/audit` | Planned |
| Communications | Notifications, announcements | `/csea/communications` | Planned |
| Content Moderation | Flagged content review | `/csea/moderation` | Planned |
| MoroAcademy Admin | Training management | `/csea/academy` | Planned |
| System Settings | Platform configuration | `/csea/settings` | Planned |
| Staff Management | CSEA team management | `/csea/staff` | Planned |

## Registration Oversight

### Application Review Process
```
New Application Received
    ├── Initial Screening (auto)
    │   ├── Document completeness check
    │   └── Basic validation
    │
    ├── Staff Review Assignment
    │   └── Based on region/type/workload
    │
    ├── Document Verification
    │   ├── CDA/SEC/DTI registration validation
    │   ├── Identity verification
    │   └── Business information check
    │
    ├── Decision
    │   ├── Approve → Tenant created, notification sent
    │   ├── Request More Info → Applicant notified
    │   └── Reject → Rejection reason, notification sent
    │
    └── Post-Approval
        ├── Welcome onboarding triggered
        ├── Training recommendations sent
        └── First compliance deadline set
```

### Application States
| State | Description | Staff Actions |
|-------|-------------|---------------|
| Submitted | New application received | Begin review |
| Under Review | Staff actively reviewing | Continue, request info |
| Info Requested | Awaiting applicant response | Wait, follow up |
| Approved | Application accepted | None (auto-processed) |
| Rejected | Application declined | Document reason |
| Withdrawn | Applicant cancelled | Archive |

### Application Review Checklist
| Item | Description | Verification |
|------|-------------|--------------|
| Legal Registration | CDA/SEC/DTI valid and current | Cross-reference database |
| Business Address | Valid Bangsamoro address | Location verification |
| Contact Information | Valid phone, email | Auto-verification |
| Key Officers | Identified and verified | ID check |
| Business Type | Matches registration | Category validation |
| Documents | All required docs submitted | Completeness check |
| Social Mission (SE) | Clear mission statement | Content review |

## Compliance Monitoring

### FRAMES Compliance (Cooperatives)
| Component | Staff Actions | Key Indicators |
|-----------|---------------|----------------|
| Financial | Review audited statements | Debt ratio, liquidity, reserves |
| Regulatory | Verify permits, clearances | Up-to-date registrations |
| Administrative | Check governance docs | Meeting minutes, policies |
| Membership | Review member records | Growth, share capital |
| Economic | Assess business performance | Revenue, volume, growth |
| Social | Review community activities | Projects, education, CSR |

### SE Verification
| Criterion | Staff Actions | Evidence |
|-----------|---------------|----------|
| Social Mission | Validate mission alignment | Statement, activities |
| Impact Tracking | Review impact reports | Metrics, beneficiaries |
| Reinvestment | Check financial allocation | Statements, records |
| Beneficiary Engagement | Verify beneficiary involvement | Testimonials, participation |
| Transparency | Assess disclosure practices | Reports, communications |

### Compliance Status Management
| Status | Staff Actions | Follow-up |
|--------|---------------|-----------|
| Compliant | Regular monitoring | None |
| At Risk | Issue warning, set deadline | 30-day follow-up |
| Non-Compliant | Issue notice, restrict features | Weekly follow-up |
| Suspended | Restrict marketplace access | Reactivation review |
| Revoked | Remove from platform | Appeal process |

## Analytics and Reporting

### Dashboard Metrics
| Metric Category | Metrics | Refresh |
|-----------------|---------|---------|
| Registrations | New apps, approved, rejected, pending | Real-time |
| Compliance | Overall rate, at-risk count, deadlines | Daily |
| Transactions | GMV, orders, active tenants | Daily |
| Users | New users, active users, by type | Daily |
| Products | Total, new, by category | Daily |
| Support | Open tickets, resolution time | Real-time |

### Standard Reports
| Report | Description | Frequency |
|--------|-------------|-----------|
| Registration Summary | Apps received, processed, outcomes | Weekly |
| Compliance Status | All tenants compliance summary | Monthly |
| Platform Performance | GMV, transactions, growth | Monthly |
| Sector Analysis | Performance by coop/SE type | Quarterly |
| FRAMES Summary | Cooperative compliance by component | Quarterly |
| SE Impact Summary | Aggregate SE impact metrics | Quarterly |
| Annual Review | Comprehensive yearly report | Annually |

### Custom Report Builder
- Date range selection
- Metric selection
- Filtering (region, type, status)
- Grouping options
- Export formats (PDF, Excel, CSV)
- Scheduled report delivery

## Staff Role Hierarchy

### Role Levels
| Role | Description | Access Level |
|------|-------------|--------------|
| Viewer | Read-only access | View dashboards, reports |
| Analyst | Analytics focus | Reports, analytics, no actions |
| Officer | Field operations | Registrations, compliance |
| Supervisor | Team lead | All operations, staff management |
| Administrator | System admin | Full access, settings |
| Director | Executive | Full access, strategic reports |

### Permission Matrix
| Function | Viewer | Analyst | Officer | Supervisor | Admin |
|----------|--------|---------|---------|------------|-------|
| View Dashboard | Yes | Yes | Yes | Yes | Yes |
| View Tenants | Yes | Yes | Yes | Yes | Yes |
| Review Applications | No | No | Yes | Yes | Yes |
| Approve/Reject Apps | No | No | Yes | Yes | Yes |
| Compliance Actions | No | No | Yes | Yes | Yes |
| Generate Reports | No | Yes | Yes | Yes | Yes |
| User Management | No | No | No | Yes | Yes |
| Staff Management | No | No | No | Yes | Yes |
| System Settings | No | No | No | No | Yes |

## Role Progression

**From**:
- External hire (CSEA employee)
- Promotion within CSEA

**To**:
- Higher staff role (Officer > Supervisor > Admin)
- Multi-agency admin (future, for MAFAR/MTIT)

**Requirements to Become CSEA Staff**:
- CSEA employment
- csea.gov.ph email domain
- Background verification
- Platform training completion
- Administrator account creation
- 2FA setup mandatory

## Audit and Accountability

### Audit Trail Tracking
| Action Type | Details Logged |
|-------------|----------------|
| Application Review | Staff ID, timestamp, decision, reason |
| Compliance Update | Staff ID, tenant, change, reason |
| User Action | Staff ID, user affected, action taken |
| Document Access | Staff ID, document, access type |
| Report Generation | Staff ID, report type, parameters |
| Setting Change | Staff ID, setting, old/new value |

### Accountability Features
- Action attribution to staff member
- Supervisor approval for sensitive actions
- Automatic escalation for delayed reviews
- Performance metrics per staff member
- Conflict of interest flagging

## Communication Tools

### Notification Types
| Type | Recipients | Trigger |
|------|------------|---------|
| Application Update | Applicant | Status change |
| Compliance Alert | Tenant manager | Approaching deadline, status change |
| Platform Announcement | All users | Admin-initiated |
| Document Request | Specific tenant | Staff-initiated |
| Training Reminder | Enrolled users | Course deadline |

### Communication Channels
- In-platform notifications
- Email notifications
- SMS for urgent alerts (planned)
- Bulk messaging for announcements

## Pain Points

1. **Manual Document Verification**
   - Time-consuming cross-referencing
   - No CDA database integration
   - Impact: Slow application processing

2. **Compliance Tracking Complexity**
   - Multiple compliance frameworks
   - Manual deadline tracking
   - Impact: Missed deadlines, inconsistent enforcement

3. **Limited Analytics**
   - Basic reporting only
   - No predictive insights
   - Impact: Reactive rather than proactive management

4. **Workload Imbalance**
   - No automatic assignment
   - Uneven review distribution
   - Impact: Bottlenecks, delays

5. **Communication Gaps**
   - No integrated messaging
   - Multiple systems for communication
   - Impact: Missed communications, delays

6. **Inter-Agency Coordination**
   - No integration with other agencies
   - Duplicate data entry
   - Impact: Inefficiency, inconsistency

## Improvement Opportunities

1. **Automated Document Verification**
   - CDA database integration
   - OCR for document extraction
   - AI-powered validation
   - Reduced manual work

2. **Smart Compliance Monitoring**
   - Automated deadline tracking
   - Predictive compliance risk scoring
   - Auto-escalation for at-risk tenants
   - Benchmarking and insights

3. **Enhanced Analytics**
   - Real-time dashboards
   - Trend analysis
   - Predictive modeling
   - Custom visualization

4. **Workload Management**
   - Auto-assignment based on capacity
   - SLA tracking
   - Performance dashboards
   - Load balancing

5. **Unified Communication Hub**
   - Integrated messaging
   - Template library
   - Communication history
   - Multi-channel delivery

6. **Inter-Agency Integration**
   - Shared authentication
   - Data sharing protocols
   - Cross-agency dashboards
   - Unified reporting

7. **Mobile Admin App**
   - Field verification
   - Mobile approvals
   - Push notifications
   - Offline capability

## Success Metrics

### Efficiency Metrics
- **Application Processing Time**: Days from submission to decision (target: < 5 days)
- **First Response Time**: Hours to first staff action (target: < 24 hours)
- **Backlog Size**: Pending applications (target: < 20)
- **Staff Utilization**: Active workload per staff (target: balanced)

### Quality Metrics
- **Decision Accuracy**: % decisions upheld on appeal (target: 95%+)
- **Compliance Detection Rate**: % at-risk tenants identified early (target: 90%+)
- **Document Verification Accuracy**: % correct verifications (target: 99%+)
- **Appeal Rate**: % decisions appealed (target: < 5%)

### Compliance Metrics
- **Overall Compliance Rate**: % tenants compliant (target: 85%+)
- **Deadline Adherence**: % documents submitted on time (target: 90%+)
- **Resolution Time**: Days to resolve non-compliance (target: < 30 days)
- **Recurring Non-Compliance**: % repeat offenders (target: < 10%)

### Platform Health Metrics
- **Active Tenants**: % of registered tenants with sales (target: 70%+)
- **Platform GMV Growth**: Month-over-month growth (target: 10%+)
- **User Satisfaction**: NPS from tenants (target: 40+)
- **Support Resolution Time**: Hours to resolve tickets (target: < 48 hours)

### Accountability Metrics
- **Audit Completeness**: % actions with full trail (target: 100%)
- **Policy Compliance**: % staff following procedures (target: 100%)
- **Training Completion**: % staff completing required training (target: 100%)

---

## Implementation Plan

### Access Control
- **Authentication required**: All `/csea/*` routes require authenticated admin user
- **Middleware**: `frontend/src/middleware.ts` - admin auth guards for `(admin)` route group
- **Domain restriction**: User email must end with `@csea.gov.ph` or approved domain
- **Mandatory 2FA**: Two-factor authentication required for all CSEA staff
- **Role-based permissions**: Access varies by staff role (Viewer, Analyst, Officer, Supervisor, Admin)
- **Platform-wide access**: Can view (but not modify) all tenant data
- **Audit logging**: All actions logged with staff ID, timestamp, and details

```typescript
// frontend/src/middleware.ts
const adminRoutes = ['/csea'];
// Verify: authenticated + email domain + 2FA enabled
// Check role permissions for specific actions
// Log all access and actions to audit trail
```

### Priority Pages

#### P0 - Core Oversight
| Page | Route | File Path |
|------|-------|-----------|
| Dashboard | `/csea` | `frontend/src/app/(admin)/csea/page.tsx` |
| Registration Queue | `/csea/registrations` | `frontend/src/app/(admin)/csea/registrations/page.tsx` |
| Application Detail | `/csea/registrations/[id]` | `frontend/src/app/(admin)/csea/registrations/[id]/page.tsx` |
| Tenant Directory | `/csea/tenants` | `frontend/src/app/(admin)/csea/tenants/page.tsx` |
| Tenant Profile | `/csea/tenants/[id]` | `frontend/src/app/(admin)/csea/tenants/[id]/page.tsx` |
| Compliance Overview | `/csea/compliance` | `frontend/src/app/(admin)/csea/compliance/page.tsx` |

#### P1 - Compliance & Analytics
| Page | Route | File Path |
|------|-------|-----------|
| FRAMES Dashboard | `/csea/compliance/frames` | `frontend/src/app/(admin)/csea/compliance/frames/page.tsx` |
| SE Verification | `/csea/compliance/se` | `frontend/src/app/(admin)/csea/compliance/se/page.tsx` |
| Tenant Compliance | `/csea/compliance/[tenantId]` | `frontend/src/app/(admin)/csea/compliance/[tenantId]/page.tsx` |
| User Management | `/csea/users` | `frontend/src/app/(admin)/csea/users/page.tsx` |
| User Detail | `/csea/users/[id]` | `frontend/src/app/(admin)/csea/users/[id]/page.tsx` |
| Analytics | `/csea/analytics` | `frontend/src/app/(admin)/csea/analytics/page.tsx` |
| Reports | `/csea/reports` | `frontend/src/app/(admin)/csea/reports/page.tsx` |
| Audit Logs | `/csea/audit` | `frontend/src/app/(admin)/csea/audit/page.tsx` |

#### P2 - Communication & Content
| Page | Route | File Path |
|------|-------|-----------|
| Communications | `/csea/communications` | `frontend/src/app/(admin)/csea/communications/page.tsx` |
| Content Moderation | `/csea/moderation` | `frontend/src/app/(admin)/csea/moderation/page.tsx` |
| MoroAcademy Admin | `/csea/academy` | `frontend/src/app/(admin)/csea/academy/page.tsx` |
| Custom Domains | `/csea/domains` | `frontend/src/app/(admin)/csea/domains/page.tsx` |

#### P3 - System Administration
| Page | Route | File Path |
|------|-------|-----------|
| System Settings | `/csea/settings` | `frontend/src/app/(admin)/csea/settings/page.tsx` |
| Staff Management | `/csea/staff` | `frontend/src/app/(admin)/csea/staff/page.tsx` |
| Categories | `/csea/settings/categories` | `frontend/src/app/(admin)/csea/settings/categories/page.tsx` |
| Platform Config | `/csea/settings/platform` | `frontend/src/app/(admin)/csea/settings/platform/page.tsx` |

### Role-Specific Components

| Component | Path | Purpose |
|-----------|------|---------|
| AdminSidebar | `frontend/src/components/admin/admin-sidebar.tsx` | Admin navigation |
| AdminDashboardStats | `frontend/src/components/admin/dashboard-stats.tsx` | Platform metrics |
| PendingAlerts | `frontend/src/components/admin/pending-alerts.tsx` | Action items |
| RegistrationQueue | `frontend/src/components/admin/registrations/registration-queue.tsx` | App queue list |
| ApplicationReview | `frontend/src/components/admin/registrations/application-review.tsx` | Review form |
| DocumentVerifier | `frontend/src/components/admin/registrations/document-verifier.tsx` | Doc verification |
| ApprovalActions | `frontend/src/components/admin/registrations/approval-actions.tsx` | Approve/reject |
| RejectionReasonForm | `frontend/src/components/admin/registrations/rejection-reason-form.tsx` | Rejection modal |
| TenantTable | `frontend/src/components/admin/tenants/tenant-table.tsx` | Tenant directory |
| TenantProfile | `frontend/src/components/admin/tenants/tenant-profile.tsx` | Full tenant view |
| TenantActions | `frontend/src/components/admin/tenants/tenant-actions.tsx` | Suspend/activate |
| ComplianceOverview | `frontend/src/components/admin/compliance/compliance-overview.tsx` | All tenants status |
| FRAMESDashboard | `frontend/src/components/admin/compliance/frames-dashboard.tsx` | FRAMES summary |
| SEVerificationDashboard | `frontend/src/components/admin/compliance/se-verification-dashboard.tsx` | SE summary |
| ComplianceActions | `frontend/src/components/admin/compliance/compliance-actions.tsx` | Status changes |
| ComplianceHistory | `frontend/src/components/admin/compliance/compliance-history.tsx` | Audit trail |
| UserTable | `frontend/src/components/admin/users/user-table.tsx` | User directory |
| UserProfile | `frontend/src/components/admin/users/user-profile.tsx` | User detail view |
| UserActions | `frontend/src/components/admin/users/user-actions.tsx` | Ban/activate |
| AnalyticsDashboard | `frontend/src/components/admin/analytics/analytics-dashboard.tsx` | Platform metrics |
| GMVChart | `frontend/src/components/admin/analytics/gmv-chart.tsx` | GMV over time |
| RegistrationChart | `frontend/src/components/admin/analytics/registration-chart.tsx` | Registration trend |
| SectorBreakdown | `frontend/src/components/admin/analytics/sector-breakdown.tsx` | By coop/SE type |
| ReportBuilder | `frontend/src/components/admin/reports/report-builder.tsx` | Custom reports |
| ReportExporter | `frontend/src/components/admin/reports/report-exporter.tsx` | Export to PDF/Excel |
| AuditLogTable | `frontend/src/components/admin/audit/audit-log-table.tsx` | Activity log |
| AuditFilters | `frontend/src/components/admin/audit/audit-filters.tsx` | Log filtering |
| AnnouncementForm | `frontend/src/components/admin/communications/announcement-form.tsx` | Bulk messaging |
| NotificationSender | `frontend/src/components/admin/communications/notification-sender.tsx` | Send notification |
| ContentModerationQueue | `frontend/src/components/admin/moderation/moderation-queue.tsx` | Flagged items |
| ModerationActions | `frontend/src/components/admin/moderation/moderation-actions.tsx` | Approve/remove |
| StaffTable | `frontend/src/components/admin/staff/staff-table.tsx` | Staff directory |
| StaffRoleAssignment | `frontend/src/components/admin/staff/staff-role-assignment.tsx` | Role management |
| DomainConfigForm | `frontend/src/components/admin/domains/domain-config-form.tsx` | Custom domain setup |

### API Endpoints Required

| Endpoint | Method | Location | Purpose |
|----------|--------|----------|---------|
| `/api/admin/dashboard` | GET | `backend/apps/admin/api.py` | Dashboard metrics |
| `/api/admin/registrations` | GET | `backend/apps/admin/api.py` | Registration queue |
| `/api/admin/registrations/{id}` | GET/PATCH | `backend/apps/admin/api.py` | Application detail |
| `/api/admin/registrations/{id}/approve` | POST | `backend/apps/admin/api.py` | Approve application |
| `/api/admin/registrations/{id}/reject` | POST | `backend/apps/admin/api.py` | Reject application |
| `/api/admin/registrations/{id}/request-info` | POST | `backend/apps/admin/api.py` | Request more info |
| `/api/admin/tenants` | GET | `backend/apps/admin/api.py` | All tenants |
| `/api/admin/tenants/{id}` | GET/PATCH | `backend/apps/admin/api.py` | Tenant detail |
| `/api/admin/tenants/{id}/suspend` | POST | `backend/apps/admin/api.py` | Suspend tenant |
| `/api/admin/tenants/{id}/activate` | POST | `backend/apps/admin/api.py` | Activate tenant |
| `/api/admin/compliance` | GET | `backend/apps/admin/api.py` | Compliance overview |
| `/api/admin/compliance/frames` | GET | `backend/apps/admin/api.py` | FRAMES summary |
| `/api/admin/compliance/se` | GET | `backend/apps/admin/api.py` | SE verification summary |
| `/api/admin/compliance/{tenantId}` | GET/PATCH | `backend/apps/admin/api.py` | Tenant compliance |
| `/api/admin/compliance/{tenantId}/status` | PATCH | `backend/apps/admin/api.py` | Update status |
| `/api/admin/users` | GET | `backend/apps/admin/api.py` | All users |
| `/api/admin/users/{id}` | GET/PATCH | `backend/apps/admin/api.py` | User detail |
| `/api/admin/users/{id}/ban` | POST | `backend/apps/admin/api.py` | Ban user |
| `/api/admin/analytics` | GET | `backend/apps/admin/api.py` | Platform analytics |
| `/api/admin/analytics/gmv` | GET | `backend/apps/admin/api.py` | GMV metrics |
| `/api/admin/analytics/registrations` | GET | `backend/apps/admin/api.py` | Registration metrics |
| `/api/admin/analytics/sector` | GET | `backend/apps/admin/api.py` | Sector breakdown |
| `/api/admin/reports` | GET/POST | `backend/apps/admin/api.py` | Report generation |
| `/api/admin/reports/{id}` | GET | `backend/apps/admin/api.py` | Single report |
| `/api/admin/reports/export` | POST | `backend/apps/admin/api.py` | Export report |
| `/api/admin/audit` | GET | `backend/apps/admin/api.py` | Audit logs |
| `/api/admin/communications` | GET/POST | `backend/apps/admin/api.py` | Announcements |
| `/api/admin/notifications/send` | POST | `backend/apps/admin/api.py` | Send notification |
| `/api/admin/moderation` | GET | `backend/apps/admin/api.py` | Moderation queue |
| `/api/admin/moderation/{id}` | PATCH | `backend/apps/admin/api.py` | Moderation action |
| `/api/admin/staff` | GET/POST | `backend/apps/admin/api.py` | Staff management |
| `/api/admin/staff/{id}` | GET/PATCH/DELETE | `backend/apps/admin/api.py` | Staff detail |
| `/api/admin/staff/{id}/role` | PATCH | `backend/apps/admin/api.py` | Role assignment |
| `/api/admin/domains` | GET/POST | `backend/apps/admin/api.py` | Custom domains |
| `/api/admin/domains/{id}` | GET/PATCH/DELETE | `backend/apps/admin/api.py` | Domain config |
| `/api/admin/settings` | GET/PATCH | `backend/apps/admin/api.py` | Platform settings |
| `/api/admin/categories` | GET/POST/PATCH/DELETE | `backend/apps/admin/api.py` | Category management |

### Implementation Sequence

#### Phase 1: Authentication & Dashboard (Week 1-2)
1. CSEA staff authentication with domain validation
2. Mandatory 2FA setup flow
3. Role-based route protection
4. Dashboard with key metrics and alerts
5. Basic navigation sidebar

#### Phase 2: Registration Management (Week 3-5)
1. Registration queue with filters (status, date, type)
2. Application detail view with all documents
3. Document verification interface
4. Approve/reject workflow with reason capture
5. Request more info flow
6. Notification on status change
7. Application assignment to staff

#### Phase 3: Tenant Management (Week 6-7)
1. Tenant directory with search and filters
2. Tenant profile view (read-only details)
3. Tenant status actions (suspend, activate)
4. Tenant compliance summary view
5. Tenant order/sales overview

#### Phase 4: Compliance Monitoring (Week 8-10)
1. Compliance overview dashboard
2. FRAMES dashboard for cooperatives
3. SE verification dashboard
4. Individual tenant compliance detail
5. Compliance status update workflow
6. Document review and verification
7. Deadline tracking and alerts
8. Compliance action history

#### Phase 5: Analytics & Reporting (Week 11-13)
1. Platform analytics dashboard
2. GMV and transaction metrics
3. Registration trend charts
4. Sector breakdown analysis
5. Report builder with filters
6. Standard report templates
7. Export to PDF/Excel/CSV
8. Scheduled report delivery

#### Phase 6: User & Audit (Week 14-15)
1. User directory with search
2. User profile view
3. User status actions (ban, activate)
4. Audit log viewer with filters
5. Action attribution display
6. Export audit logs

#### Phase 7: Communication & Moderation (Week 16-17)
1. Announcement creation
2. Targeted notification sending
3. Communication history
4. Content moderation queue
5. Moderation actions (approve, remove)
6. Moderation reason capture

#### Phase 8: System Administration (Week 18-20)
1. Staff management interface
2. Role assignment workflow
3. Permission configuration
4. Category management
5. Platform settings
6. Custom domain configuration
7. MoroAcademy admin integration

---

## Implementation Status

*Audited: December 30, 2025*

### Key Pages Status

| Page | Status | Path | Notes |
|------|--------|------|-------|
| Dashboard | ✅ Implemented | `frontend/src/app/(admin)/agency/dashboard/page.tsx` | Route is `/agency/dashboard` |
| Login | ✅ Implemented | `frontend/src/app/(admin)/agency/login/page.tsx` | Admin login |
| Profile | ✅ Implemented | `frontend/src/app/(admin)/agency/profile/page.tsx` | Staff profile |
| Registration Queue | ✅ Implemented | `frontend/src/app/(admin)/agency/registration/page.tsx` | Route is `/registration` |
| Cooperatives List | ✅ Implemented | `frontend/src/app/(admin)/agency/cooperatives/page.tsx` | Coop directory |
| Cooperatives Create | ✅ Implemented | `frontend/src/app/(admin)/agency/cooperatives/new/page.tsx` | Add cooperative |
| Social Enterprises | ✅ Implemented | `frontend/src/app/(admin)/agency/social-enterprises/page.tsx` | SE directory |
| SE Create | ✅ Implemented | `frontend/src/app/(admin)/agency/social-enterprises/new/page.tsx` | Add SE |
| Formation | ✅ Implemented | `frontend/src/app/(admin)/agency/formation/page.tsx` | Formation tracking |
| Monitoring | ✅ Implemented | `frontend/src/app/(admin)/agency/monitoring/page.tsx` | Platform monitoring |
| Auditing | ✅ Implemented | `frontend/src/app/(admin)/agency/auditing/page.tsx` | Audit functions |
| Analytics | ✅ Implemented | `frontend/src/app/(admin)/agency/analytics/page.tsx` | Platform metrics |
| Sustainability | ✅ Implemented | `frontend/src/app/(admin)/agency/sustainability/page.tsx` | Sustainability tracking |
| Training Admin | ✅ Implemented | `frontend/src/app/(admin)/agency/training/page.tsx` | MoroAcademy admin |
| Manager Applications | ✅ Implemented | `frontend/src/app/(admin)/agency/manager-applications/page.tsx` | Application review |
| Application Detail | ❌ Not Found | - | No `/registrations/[id]` page |
| Tenant Profile | ❌ Not Found | - | No `/tenants/[id]` detail page |
| Compliance Overview | ❌ Not Found | - | No compliance dashboard |
| FRAMES Dashboard | ❌ Not Found | - | No FRAMES summary page |
| SE Verification | ❌ Not Found | - | No SE verification page |
| User Management | ❌ Not Found | - | No user management page |
| Reports | ❌ Not Found | - | No report builder page |
| Audit Logs | ❌ Not Found | - | No audit log viewer |
| Communications | ❌ Not Found | - | No communications hub |
| Content Moderation | ❌ Not Found | - | No moderation queue |
| System Settings | ❌ Not Found | - | No platform settings |
| Staff Management | ❌ Not Found | - | No staff management |
| Custom Domains | ❌ Not Found | - | No domain config page |

### API Endpoints Status

| Endpoint | Status | Path | Notes |
|----------|--------|------|-------|
| Admin Dashboard | ✅ Implemented | `/admin/dashboard` | Dashboard metrics |
| Admin Submissions | ✅ Implemented | `/admin/submissions` | Registration queue |
| Admin COC | ✅ Implemented | `/admin/coc` | Certificate of Compliance |
| Admin Findings | ✅ Implemented | `/admin/findings` | Audit findings |
| Admin Inspections | ✅ Implemented | `/admin/inspections` | Inspection management |
| Admin Formations | ✅ Implemented | `/admin/formations` | Formation tracking |
| Admin Analytics | ✅ Implemented | `/admin/analytics` | Platform analytics |
| Admin Monitoring | ✅ Implemented | `/admin/monitoring` | Monitoring data |
| Admin Users | ✅ Implemented | `/admin/users` | User management |
| Registration Coop | ✅ Implemented | `/registration/cooperative` | Coop registration |
| Registration SE | ✅ Implemented | `/registration/social-enterprise` | SE registration |
| Registration Approvals | ✅ Implemented | `/admin/approvals` (inferred) | Application approvals |
| Compliance Overview | ❌ Not Found | - | No compliance summary API |
| FRAMES Summary | ❌ Not Found | - | No FRAMES aggregate API |
| SE Verification Summary | ❌ Not Found | - | No SE verification API |
| Audit Logs | ❌ Not Found | - | No audit log API |
| Communications | ❌ Not Found | - | No announcements API |
| Content Moderation | ❌ Not Found | - | No moderation API |
| Staff Management | ❌ Not Found | - | No staff CRUD API |
| Report Generation | ❌ Not Found | - | No report builder API |

### Overall Progress

- **Pages**: 15/28 implemented (54%)
- **APIs**: 12/20 implemented (60%)

### Notes

1. **Route Structure**: Uses `/agency/` prefix instead of `/csea/` for admin routes
2. **Core Admin Functions**: Dashboard, registration, tenant directories implemented
3. **Missing Compliance Views**: No dedicated compliance dashboards for FRAMES or SE verification
4. **No Application Detail**: Registration queue exists but no individual application review page
5. **Audit Functions**: Auditing page exists but no audit log viewer
6. **Formation Tracking**: Unique feature for coop/SE formation process
7. **Manager Applications**: Separate flow for reviewing consumer-to-manager applications
8. **Missing Infrastructure**: User management, reports, settings, staff management pages not found
9. **No Communication Hub**: No integrated announcement or notification system
10. **Analytics Available**: Basic analytics page exists for platform metrics
