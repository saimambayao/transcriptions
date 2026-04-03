---
name: office
description: Office management domain skill for e-Bangsamoro. Covers staff management, task tracking, calendar scheduling, document management, and office operations. Use when implementing office productivity features, staff coordination, or document handling systems.
argument-hint: "[topic]"
---

# Office Management - e-Bangsamoro

## Purpose

Provides domain expertise for the Office Management module of e-Bangsamoro, covering day-to-day operations of parliamentary and ministerial offices.

## When to Use

- Implementing staff management features
- Building task tracking systems
- Creating calendar and scheduling features
- Implementing document management
- Designing office workflow automation

## Key Entities

- **Staff**: Office staff members with roles and permissions
- **Task**: Work tasks and assignments with deadlines
- **Event**: Calendar events, meetings, and schedules
- **Document**: Office documents with version control
- **Workflow**: Automated office workflows and approvals
- **Notification**: Staff notifications and alerts

## Task States

```
Created --> Assigned --> In Progress --> Review --> Completed
    |           |             |            |
    v           v             v            v
  Cancelled  Reassigned   On Hold     Rejected
```

1. **Created** - Task has been created but not yet assigned
2. **Assigned** - Task has been assigned to a staff member
3. **In Progress** - Staff member is actively working on the task
4. **Review** - Task completed and awaiting supervisor review
5. **Completed** - Task approved and closed
6. **Cancelled** - Task was cancelled before completion
7. **On Hold** - Task temporarily paused
8. **Rejected** - Task returned for revision during review

## Document Types

| Type | Description | Retention Period |
|------|-------------|------------------|
| Internal Memos | Staff communications | 2 years |
| Official Correspondence | External letters and communications | 5 years |
| Reports | Analytical and status reports | 5 years |
| Meeting Minutes | Records of meetings | Permanent |
| Policy Documents | Office policies and procedures | Permanent |
| Administrative Orders | Directives and instructions | 5 years |
| Endorsements | Recommendations and approvals | 3 years |

## Staff Roles in Parliamentary Offices

| Role | Description |
|------|-------------|
| Chief of Staff | Head of office operations |
| Executive Assistant | Direct support to MP/Minister |
| Legislative Aide | Bill research and drafting support |
| Constituent Liaison | Public relations and constituent services |
| Administrative Officer | General administration |
| Records Officer | Document management |
| Finance Officer | Budget and financial matters |

## Calendar Event Types

- **Plenary Sessions** - Parliament sessions
- **Committee Hearings** - Standing/special committee meetings
- **Consultations** - Stakeholder and public consultations
- **Staff Meetings** - Internal team meetings
- **Official Travel** - Official trips and visits
- **Deadlines** - Important submission deadlines
- **Appointments** - Scheduled meetings with constituents

## Office Workflow Patterns

### Document Approval Workflow
```
Draft --> Supervisor Review --> Chief of Staff --> MP/Minister --> Filed
```

### Leave Request Workflow
```
Request --> Supervisor Approval --> HR Processing --> Approved/Denied
```

### Procurement Request Workflow
```
Request --> Budget Check --> Approval --> Procurement --> Received
```

## Integration Points

- **Legislative Work**: Tasks related to bill processing
- **Oversight Work**: Document management for oversight activities
- **Representation Work**: Constituent appointment scheduling
- **Budget Management**: Office budget tracking
- **Ministerial Planning**: Planning-related document management

## Reference Files

- [staff-management.md](references/staff-management.md) - Staff organization and roles
- [task-workflows.md](references/task-workflows.md) - Task assignment and tracking
- [document-management.md](references/document-management.md) - Document handling procedures

## Tech Implementation Notes

### Backend (Django)
- App location: `backend/apps/office/`
- Models: Staff, Task, Event, Document, Workflow
- Use Django REST Framework for API endpoints
- Implement Celery tasks for notifications and reminders

### Frontend (React)
- Feature location: `frontend/src/features/office/`
- Route pattern: `/office/*`
- Use TanStack Query for data fetching
- Calendar component with Recharts for analytics

### Database Considerations
- PostgreSQL with proper indexing for task queries
- Use Django's FileField with Cloudflare R2 for documents
- Implement soft delete for compliance with retention policies
