---
name: oversight
description: Oversight work domain skill for e-Bangsamoro. Covers MOA budget tracking, program monitoring, ministry oversight, and accountability procedures. Use when implementing oversight dashboards, MOA management, or program tracking features.
argument-hint: "[topic]"
---

# Oversight Work - e-Bangsamoro

## Purpose
Provides domain expertise for the Oversight Work module of e-Bangsamoro, covering monitoring of Ministry of the Bangsamoro (MOA) budgets, programs, and accountability.

## When to Use
- Implementing MOA budget tracking features
- Building program monitoring dashboards
- Creating oversight report systems
- Implementing audit trail features
- Designing accountability tracking

## Key Entities
- **MOA**: Ministry of the Bangsamoro agencies
- **ProgramMonitor**: Tracked programs and their status
- **BudgetAllocation**: Ministry budget allocations
- **OversightReport**: Parliamentary oversight reports
- **Finding**: Audit/oversight findings
- **Recommendation**: Improvement recommendations

## Oversight Areas
1. Budget Utilization Monitoring
2. Program Implementation Tracking
3. Performance Assessment
4. Compliance Verification
5. Audit Follow-up

## Reference Files
- [moa-tracking.md](references/moa-tracking.md) - Ministry tracking procedures
- [program-monitoring.md](references/program-monitoring.md) - Program oversight methods
- [audit-procedures.md](references/audit-procedures.md) - Audit and accountability procedures

## BARMM Oversight Context

### Parliamentary Oversight Authority
The Bangsamoro Parliament exercises oversight powers over all ministries, agencies, and instrumentalities of the Bangsamoro Government. This includes:
- Review of budget execution and utilization
- Monitoring of program implementation
- Investigation of irregularities
- Performance evaluation of government agencies

### Key Oversight Committees
1. **Committee on Appropriations** - Budget oversight
2. **Committee on Audit and Accounts** - Financial accountability
3. **Committee on Good Governance** - Anti-corruption and transparency
4. **Sectoral Committees** - Ministry-specific oversight

### Oversight Mechanisms
1. **Regular Reporting** - Quarterly and annual reports from ministries
2. **Committee Hearings** - Inquiry sessions on specific matters
3. **Field Inspections** - On-site verification of projects
4. **Audit Reviews** - COA coordination and follow-up
5. **Performance Reviews** - Assessment against targets

## Implementation Guidelines

### Dashboard Components
- Ministry budget utilization cards
- Program status tracking tables
- Finding/recommendation trackers
- Compliance status indicators
- Timeline visualizations for audits

### Data Models
```
Ministry (MOA)
+-- BudgetAllocation
|   +-- amount
|   +-- fiscal_year
|   +-- utilization_rate
|   +-- status
+-- Programs
|   +-- name
|   +-- budget
|   +-- target_beneficiaries
|   +-- actual_beneficiaries
|   +-- implementation_status
+-- OversightReports
    +-- type (regular/special)
    +-- period
    +-- findings[]
    +-- recommendations[]
```

### API Endpoints Pattern
- `GET /api/oversight/ministries/` - List all ministries with overview stats
- `GET /api/oversight/ministries/{id}/budget/` - Ministry budget details
- `GET /api/oversight/ministries/{id}/programs/` - Ministry programs
- `GET /api/oversight/reports/` - Oversight reports
- `POST /api/oversight/findings/` - Record new findings
- `PATCH /api/oversight/recommendations/{id}/status/` - Update recommendation status

### Status Tracking
- **Budget Status**: On Track, At Risk, Behind, Completed
- **Program Status**: Planning, Implementation, Monitoring, Completed, Suspended
- **Finding Status**: Open, In Progress, Resolved, Closed
- **Recommendation Status**: Pending, Accepted, In Progress, Implemented, Rejected
