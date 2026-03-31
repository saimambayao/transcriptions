# e-Bangsamoro Platform Architecture: Three-Portal System

## Architecture Document

**Version**: 1.8
**Date**: 2026-01-04
**Status**: Draft - Architecture Planning

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Platform Overview](#2-platform-overview)
3. [Portal Definitions](#3-portal-definitions)
4. [Module-to-Portal Mapping](#4-module-to-portal-mapping)
5. [Cross-Portal Data Flows](#5-cross-portal-data-flows)
6. [Authentication, Authorization & Multi-Tenancy](#6-authentication-authorization--multi-tenancy)
   - 6.1 [Unified Authentication Flow](#61-unified-authentication-flow)
   - 6.2 [Multi-Tenancy Architecture](#62-multi-tenancy-architecture)
   - 6.3 [Role-Based Access Control (RBAC)](#63-role-based-access-control-rbac)
   - 6.4 [Permission Matrix](#64-permission-matrix)
   - 6.5 [Portal Access by Role](#65-portal-access-by-role)
   - 6.6 [DRF Permission Classes](#66-drf-permission-classes)
   - 6.7 [JWT Token Structure](#67-jwt-token-structure)
   - 6.8 [Cross-Portal Access Patterns](#68-cross-portal-access-patterns)
7. [Navigation Architecture](#7-navigation-architecture)
8. [Shared Infrastructure](#8-shared-infrastructure)
9. [Deployment Architecture](#9-deployment-architecture)
10. [Implementation Strategy](#10-implementation-strategy)

---

## 1. Executive Summary

The Bangsamoro Parliamentary and Ministerial Platform (BPMP) is being restructured from a unified 7-module application into **3 specialized portals**, each serving distinct user groups with focused functionality:

| Portal | Domain | Primary Users |
|--------|--------|---------------|
| **Parliamentary Portal** | Legislative operations, oversight, representation | MPs, MP Staff, Committee Secretariat/Staff |
| **Ministerial Portal** | Strategic planning, PPA management | Ministers, Directors, Planning/Program/Budget/M&E Officers |
| **Budget Portal** | Budget lifecycle (BBSA-compliant) | MFBM Staff, MOA Budget/Finance/Accounting Staff |

### Benefits of Portal Separation

1. **Focused User Experience** - Each portal is optimized for its primary users
2. **Simplified Navigation** - Reduced cognitive load with domain-specific menus
3. **Role-Based Access** - Natural permission boundaries at portal level
4. **Independent Scaling** - Portals can scale based on usage patterns
5. **Modular Development** - Teams can work on portals independently

---

## 2. Platform Overview

### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           BPMP PLATFORM                                      │
│                      e-governance.bangsamoro.site                            │
│                                                                              │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐          │
│  │   PARLIAMENTARY  │  │    MINISTERIAL   │  │     BUDGET       │          │
│  │      PORTAL      │  │      PORTAL      │  │     PORTAL       │          │
│  │                  │  │                  │  │                  │          │
│  │  /parliament     │  │  /ministry       │  │  /budget         │          │
│  │                  │  │                  │  │                  │          │
│  │  - Legislative   │  │  - Ministerial   │  │  - Budget Prep   │          │
│  │  - Oversight     │  │    Planning      │  │  - Authorization │          │
│  │  - Representation│  │  - PPA Mgmt      │  │  - Execution     │          │
│  │  - Office Mgmt   │  │  - Office Mgmt   │  │  - Accountability│          │
│  │  - Dashboard     │  │  - Dashboard     │  │  - Dashboard     │          │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘          │
│           │                     │                     │                     │
│           └─────────────────────┼─────────────────────┘                     │
│                                 │                                            │
│  ┌──────────────────────────────┴──────────────────────────────────────┐    │
│  │                    SHARED API GATEWAY                                │    │
│  │              e-governance.bangsamoro.site/api                        │    │
│  └──────────────────────────────┬──────────────────────────────────────┘    │
│                                 │                                            │
│  ┌──────────────────────────────┴──────────────────────────────────────┐    │
│  │                    DJANGO REST FRAMEWORK BACKEND                     │    │
│  │                                                                      │    │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐       │    │
│  │  │accounts │ │legislat.│ │oversight│ │minister.│ │ budget  │       │    │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘       │    │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐       │    │
│  │  │ tenants │ │ office  │ │represent│ │   ai    │ │realtime │       │    │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘       │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                 │                                            │
│  ┌──────────────────────────────┴──────────────────────────────────────┐    │
│  │              SHARED DATA LAYER (PostgreSQL + Redis)                  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Portal URLs**:
- Parliamentary Portal: `e-governance.bangsamoro.site/parliament`
- Ministerial Portal: `e-governance.bangsamoro.site/ministry`
- Budget Portal: `e-governance.bangsamoro.site/budget`
- API Gateway: `e-governance.bangsamoro.site/api`

### 2.2 Architectural Principles

1. **Single Backend, Multiple Frontends** - One Django/DRF backend serves all portals
2. **Shared Component Library** - Common UI components in `@bpmp/ui`
3. **Unified Authentication** - Single auth system with portal-based routing
4. **API-First Design** - All portal communication via REST API
5. **Multi-Tenant Foundation** - Tenant isolation maintained across portals

---

## 3. Portal Definitions

### 3.1 Parliamentary Portal

**URL**: `e-governance.bangsamoro.site/parliament`

**Purpose**: Comprehensive platform for parliamentary operations, including legislative tracking, government oversight, and constituent representation.

**Primary Users**:
- Members of Parliament (MPs)
- MP Staff (legislative, oversight, and political/representation functions)
- Committee Secretariat / Staff

**Core Capabilities**:

#### Legislative Work Function

| Submodule | Features |
|-----------|----------|
| **Legislative Dashboard** | Bill pipeline overview, session calendar, committee status |
| **Legislative Tracking** | Bill registry, resolution registry, committee reports, minutes, calendar, journals |
| **Legislative Drafting** | Template library, drafting workspace, draft bills & resolutions management |
| **Legal Research** | AI-powered research workspace, legal database, research project management |
| **Legislative Analysis** | Impact analyses, stakeholder mapping, constitutional alignment checks |
| **Budget Legislation** | Budget bills, appropriations tracking, amendments, BBSA compliance |
| **Plenary Work** | Session scheduling, voting records, attendance tracking, interpellation queue |
| **Committee Work** | Committee management, hearing schedules, bill referrals, committee reports |

#### Oversight Work Function

| Submodule | Features |
|-----------|----------|
| **Oversight Dashboard** | Budget variance overview, program monitoring status, issue alerts |
| **Budget Tracking** | MOA budget overview, variance analysis, budget anomaly alerts |
| **PPA Tracking** | Program/Project/Activity monitoring, milestone tracking, BDP alignment |
| **Issue Tracking** | Oversight issues management, formal investigations, parliamentary questions |
| **M&E Analytics** | Performance scorecards, MOA rankings, monitoring & evaluation reports |

#### Representation Work Function

| Submodule | Features |
|-----------|----------|
| **Representation Dashboard** | Constituency overview, beneficiary analytics, request metrics, media coverage |
| **Constituency Services** | Geographic service map, service directory, constituency projects |
| **Beneficiary Management** | Beneficiary registry, program enrollment, aid/benefit distribution tracking |
| **Request Tracker** | Constituent request management, referral tracking, request analytics |
| **Media Affairs** | Press releases, media coverage tracking, media contacts |

#### Office Management Function

| Submodule | Features |
|-----------|----------|
| **Office Dashboard** | Staff overview, task metrics, calendar summary, announcements |
| **HR Management** | Staff directory, recruitment & onboarding, performance management, training & development, attendance & leave, compensation & benefits, employee records |
| **Task Management** | Task tracking, assignments, deadlines, progress monitoring |
| **Calendar & Scheduling** | Office calendar, meeting scheduling, event coordination |
| **Document Management** | Office documents, filing system, document workflow |

**Tenant Scope**: Parliament (with sub-tenants for MP offices, committees)

---

### 3.2 Ministerial Portal (PPA Management)

**URL**: `e-governance.bangsamoro.site/ministry`

**Purpose**: Strategic planning and Program/Project/Activity (PPA) management for Ministries, Offices, and Agencies (MOAs) following the 10-Point Framework.

**Primary Users**:
- Ministers and Deputy Ministers
- Director Generals
- Directors (Executive Directors, Deputy Executive Directors, Service/Bureau Directors)
- Division Chiefs
- Planning Officers
- Program Officers
- Budget Officers
- M&E Officers
- Other Authorized Staff

**Core Capabilities**:

#### Ministerial Planning Function (10-Point Strategic Framework)

| Point | Submodule | Features |
|-------|-----------|----------|
| — | **Planning Dashboard** | Framework progress tracking, completion metrics, BDP alignment score, recent activities, upcoming milestones |
| 1 | **Legal Alignment** | BOL provisions, administrative code, ministry charter, compliance status tracking |
| 2 | **BDP Alignment** | Bangsamoro Development Plan goals, targets, alignment matrix, progress indicators |
| 3 | **Priority Agenda** | Priority items ranking, alignment scoring, program allocation, budget per priority |
| 4 | **Stakeholder Analysis** | Stakeholder mapping, power/interest matrix, engagement plans, communications |
| 5 | **Strategy Analysis** | Vision/mission definition, core values, problem statements, strategic objectives |
| 6 | **Theory of Change** | Impact statements, outcomes, outputs, assumptions, change pathway visualization |
| 7 | **PPA Planning** | See detailed PPA structure below |
| 8 | **Resource Planning** | Budget (PS/MOOE/CO), human resources, physical resources, partnerships |
| 9 | **Annual Work & Financial** | Annual work plan, financial plan, timeline coordination, plan monitoring |
| 10 | **M&E System** | See detailed M&E structure below |

##### Point 7: PPA Planning (Detailed)

**Flexible PPA Structure** (per MFBM Budget Circular / BBP Forms):

```
Program (Cost Section: GAS, STO, Operations)
├── Activities (directly under Program)
│   └── Line Items (Ministry, Local Office allocations)
└── Projects (optional, directly under Program)
    └── Line Items (Ministry, Local Office allocations)
```

| Component | Description |
|-----------|-------------|
| **Programs** | High-level cost sections (General Administration & Support, Support to Operations, Operations). Each program can contain Activities and/or Projects directly. |
| **Projects** | Optional grouping under Programs. Projects are NOT required - Programs can have Activities directly without Projects. |
| **Activities** | Specific work items under Programs or Projects. Contains budget line items with PS/MOOE/CO breakdown. |

**PPA Attributes:**
- Code (e.g., P001, P001-PR01, P001-A01)
- UACS Code (Unified Accounts Code Structure for budget classification)
- Name and Description
- Budget Allocation (PS/MOOE/CO)
- Duration/Timeline
- Expected Outputs
- Milestones

##### PPA Management (Operational - Post-Planning)

| Feature | Description |
|---------|-------------|
| **Implementation Tracking** | Monitor PPA execution status, progress vs. plan, timeline adherence |
| **Status Management** | Track PPA status (planned, ongoing, completed, delayed, cancelled) |
| **Progress Reporting** | Quarterly accomplishment reports, physical progress tracking |
| **Issue/Risk Management** | Identify, track, and resolve implementation issues and risks |
| **Variance Analysis** | Compare planned vs. actual (budget, timeline, outputs) |
| **Document Management** | PPA-related documents, contracts, MOAs, reports |

##### Point 10: M&E System (Detailed)

**Results-Based Monitoring & Evaluation** - Operational system for tracking PPA performance:

| Tab | Features |
|-----|----------|
| **M&E Dashboard** | KPI summary, indicator progress, data collection status, upcoming evaluations |
| **Indicators** | KPIs by category (input/output/outcome/impact), baseline values, targets, actuals, progress tracking, measurement units, reporting frequency |
| **Monitoring** | Data collection methods, collection frequency, responsible units, due dates, collection status (completed/ongoing/pending), field surveys, LGU reports |
| **Evaluation** | Report templates (monthly/quarterly/annual/special), evaluation methodology, report generation, recipient management, evaluation calendar |

#### Office Management Function

| Submodule | Features |
|-----------|----------|
| **Office Dashboard** | Staff overview, task metrics, calendar summary, IPCR tracking, quick actions |
| **Organizational Structure** | Org chart, divisions, positions, staffing pattern, reporting relationships |
| **HR Management** | Staff directory, recruitment & onboarding, performance management, training & development, attendance & leave, compensation & benefits, employee records |
| **Task Management** | Kanban board, task list, timeline view, assignments, deadlines, workflow tracking |
| **Performance Management** | KPIs, performance reviews, appraisals, goal setting, metrics dashboard |
| **Calendar & Scheduling** | Events, meetings, schedules, room booking, attendee management |

**Tenant Scope**: Individual MOAs (Ministries, Offices, Agencies)

**Special Interfaces** (for consolidation, management, and oversight):
- **BPDA** - Government-wide planning consolidation and coordination
- **OCM** - Executive oversight of all MOA planning and programs
- **Office of the Parliament Speaker** - Legislative oversight of MOA plans and strategic alignment

---

### 3.3 Budget Portal

**URL**: `e-governance.bangsamoro.site/budget`

**Purpose**: BBSA-compliant budget lifecycle management covering preparation, authorization, execution, and accountability. This is a **specialized portal** focused exclusively on budget operations.

**Primary Users**:
- MFBM - All Authorized Staff
- MOA Finance Service Directors and Division Chiefs
- MOA Budget Officers
- MOA Accountants
- MOA Budget and Accounting Staff
- MOA Program Officers
- MOA GAD Focal Persons
- Other Authorized MOA Staff

**Core Capabilities**:

#### Budget Preparation Function (BBSA Phase 1)

| Submodule | Features |
|-----------|----------|
| **Preparation Dashboard** | Budget ceiling, utilization overview, MOA submission status, compliance alerts |
| **Budget Guidelines** | PS guidelines, MOOE guidelines, capital outlays, expenditure framework, tier budgeting, submission requirements, budget calendar |
| **Budget Proposals** | Forms 100-500 (BBP Forms), ministry budget proposals, justifications |
| **Line Items** | UACS-compliant line items, budget breakdown by PS/MOOE/CO |
| **Submissions** | Budget call management, submission deadlines, MOA submission tracking |
| **Budget Forms** | Form registry (BBPForm100-900 series), form validation, form workflow |
| **BEP** | Budget Execution Plan form, multi-year projections |

#### Budget Authorization Function (BBSA Phase 2)

| Submodule | Features |
|-----------|----------|
| **Authorization Dashboard** | BBSA compliance status, MOA defense status, amendment summary |
| **Budget Defense** | MOA defense preparation, key messages, anticipated questions, hearing schedule, commitments tracking |
| **Legislative Progress** | Bill timeline (Filed → Enacted), reading stages, committee deliberations |
| **Amendments** | Amendment analysis, fiscal impact assessment, committee/executive positions, disposition tracking |
| **GAAB** | General Appropriations Act Bill viewer, year-over-year data, MOA budget details, category drill-down |
| **Budget Comparison** | Cross-year comparison, budget hearing questions, variance analysis |

#### Budget Execution Function (BBSA Phase 3)

| Submodule | Features |
|-----------|----------|
| **Execution Dashboard** | Execution flow visualization (Appropriation → Allotment → Obligation → Disbursement), utilization rates, balance indicators |
| **Allotments** | SARO (Special Allotment Release Order), GAABAO releases, allotment tracking by MOA |
| **Obligations** | Obligation requests, procurement/contract commitments, obligation status tracking |
| **Disbursements** | NCA (Notice of Cash Allocation), NCAA (Non-Cash Availment Authority), payment tracking |

#### Budget Accountability Function (BBSA Phase 4)

| Submodule | Features |
|-----------|----------|
| **Accountability Dashboard** | Reports submitted, audit findings summary, compliance rate, resolution rate |
| **BFAR Reports** | Budget & Financial Accountability Reports, statement of financial position/performance, cash flows |
| **Financial Performance** | Budget vs. actual variance analysis, utilization by expense class (PS/MOOE/CO), trend indicators |
| **Audits** | COA audit findings (material/significant/minor), finding status, action plans, resolution tracking |
| **Compliance** | COA compliance checklist, monthly/quarterly/annual requirements, compliance rate tracking |

**Note**: The Budget Portal does **NOT** include Office Management. Budget Officers who need office management features (staff, tasks, calendar) access these through their organization's primary portal (Parliamentary or Ministerial).

**Special Interfaces** (for consolidation, management, and oversight):
- **MFBM** - Government-wide budget consolidation and management
- **OCM** - Executive oversight of all MOA budgets
- **Office of the Parliament Speaker** - Legislative budget oversight

**Tenant Scope**: Individual MOAs + Parliament Finance Office

---

## 4. Module-to-Portal Mapping

### 4.1 Current 7-Module Structure

| Module | Current Function |
|--------|------------------|
| Dashboard | Role-based overview and analytics |
| Legislative Work | Bills, resolutions, committees, plenary |
| Oversight Work | MOA budget/program tracking |
| Representation Work | Constituent services |
| Ministerial Planning | 10-Point Framework, PPA planning |
| Budget Management | BBSA budget lifecycle |
| Office Management | Staff, tasks, calendar |

### 4.2 Portal Assignment Matrix

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    MODULE-TO-PORTAL MAPPING                               │
├────────────────────┬─────────────┬─────────────┬─────────────────────────┤
│ Current Module     │ Parliament  │ Ministerial │ Budget                  │
│                    │ Portal      │ Portal      │ Portal                  │
├────────────────────┼─────────────┼─────────────┼─────────────────────────┤
│ Dashboard          │ ✓ (Parlia-  │ ✓ (Planning │ ✓ (Budget               │
│                    │  mentary)   │  focused)   │  focused)               │
├────────────────────┼─────────────┼─────────────┼─────────────────────────┤
│ Legislative Work   │ ✓ FULL      │ ○ View Only │ ○ Budget Bills Only     │
├────────────────────┼─────────────┼─────────────┼─────────────────────────┤
│ Oversight Work     │ ✓ FULL      │ ○ Subject   │ ○ Budget Tracking       │
│                    │             │   Only      │   Only                  │
├────────────────────┼─────────────┼─────────────┼─────────────────────────┤
│ Representation     │ ✓ FULL      │ ✗ None      │ ✗ None                  │
│ Work               │             │             │                         │
├────────────────────┼─────────────┼─────────────┼─────────────────────────┤
│ Ministerial        │ ○ View Only │ ✓ FULL      │ ○ PPA Reference         │
│ Planning           │             │             │                         │
├────────────────────┼─────────────┼─────────────┼─────────────────────────┤
│ Budget Management  │ ○ View Only │ ○ Own Prep  │ ✓ FULL                  │
│                    │             │   Only      │                         │
├────────────────────┼─────────────┼─────────────┼─────────────────────────┤
│ Office Management  │ ✓ FULL      │ ✓ FULL      │ ✗ None                  │
│                    │ (Parliament │ (MOA        │ (Specialized portal,    │
│                    │  offices)   │  offices)   │  no office mgmt)        │
└────────────────────┴─────────────┴─────────────┴─────────────────────────┘

Legend: ✓ FULL = Full access  ○ = Partial/View  ✗ = No access
```

### 4.3 Submodule Distribution

#### Parliamentary Portal Submodules

| Navigation Group | Submodules |
|------------------|------------|
| **Legislative** | Legislative Tracking, Drafting, Legal Research, Analysis, Budget Legislation, Plenary Work, Committee Work |
| **Oversight** | Budget Tracking, Program Tracking, Issue Tracking, M&E Analytics |
| **Representation** | Constituency Services, Beneficiary Management, Request Tracker, Media Affairs |
| **Office** | Organizational Structure, Staff Management, Task & Performance, Calendar |

#### Ministerial Portal Submodules

| Navigation Group | Submodules |
|------------------|------------|
| **Planning (10-Point)** | Legal Alignment, BDP Alignment, Priority Agenda, Stakeholder Analysis, Strategy Analysis, Theory of Change, PPA Planning, Resource Planning, Annual Work Plan, RBME Framework |
| **Office** | Organizational Structure, Staff Management, Task & Performance, Calendar |

#### Budget Portal Submodules

| Navigation Group | Submodules |
|------------------|------------|
| **Preparation** | Budget Estimates, Forms Management (100-500), PPA Costing, Resource Requirements |
| **Authorization** | Legislative Review, Amendments, Appropriation Bills, Approval Workflow |
| **Execution** | Allotments, Obligations, Disbursements, Monitoring |
| **Accountability** | Financial Reports, Audit Compliance, Variance Analysis, Performance Reporting |

**Note**: Budget Portal does not include Office Management. This is a specialized portal focused exclusively on BBSA budget lifecycle operations.

---

## 5. Cross-Portal Data Flows

### 5.1 Data Flow Diagram

```
                    CROSS-PORTAL DATA INTEGRATION

┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   MINISTERIAL PORTAL                    BUDGET PORTAL               │
│   ┌─────────────────────┐              ┌─────────────────────┐     │
│   │                     │              │                     │     │
│   │   PPA Planning      │─────────────▶│   Budget Prep       │     │
│   │   (Programs,        │   PPAs feed  │   (Forms 100-500)   │     │
│   │    Projects,        │   budget     │                     │     │
│   │    Activities)      │   estimates  │                     │     │
│   │                     │              │                     │     │
│   │   Resource Planning │─────────────▶│   Resource          │     │
│   │   (HR, Physical,    │   Resource   │   Requirements      │     │
│   │    Informational)   │   needs      │                     │     │
│   │                     │              │                     │     │
│   │   Annual Work Plan  │─────────────▶│   Financial Plan    │     │
│   │                     │   Timing     │   Timeline          │     │
│   └─────────────────────┘              └──────────┬──────────┘     │
│                                                   │                 │
│                                                   │ Appropriations  │
│                                                   │ & Execution     │
│                                                   ▼                 │
│                         ┌─────────────────────────────────────┐    │
│                         │       PARLIAMENTARY PORTAL           │    │
│                         │                                      │    │
│   ┌─────────────────────┤   Budget Legislation                │    │
│   │                     │   (Authorization)                    │    │
│   │  Oversight Work     │                                      │    │
│   │  ◀──────────────────┤   Budget Tracking                   │    │
│   │  Budget & Program   │   (Execution data flows to          │    │
│   │  Monitoring         │    Oversight for monitoring)        │    │
│   │                     │                                      │    │
│   └─────────────────────┴─────────────────────────────────────┘    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 5.2 Data Flow Matrix

| Source Portal | Data Type | Target Portal | Purpose |
|---------------|-----------|---------------|---------|
| Ministerial | PPAs | Budget | Budget preparation, cost estimation |
| Ministerial | Resource Requirements | Budget | Budget justification |
| Ministerial | Annual Work Plan | Budget | Timeline alignment |
| Ministerial | Strategic Objectives | Parliamentary | Oversight context |
| Budget | Appropriation Bills | Parliamentary | Legislative authorization |
| Budget | Execution Data | Parliamentary | Oversight monitoring |
| Budget | Financial Reports | Parliamentary | Accountability review |
| Parliamentary | Budget Authorization | Budget | Approved allocations |
| Parliamentary | Oversight Findings | Ministerial | Compliance feedback |
| Parliamentary | Committee Recommendations | Budget | Budget adjustments |

### 5.3 Shared Data Entities

These entities are accessed across multiple portals:

```python
# Core shared entities (backend/apps/core/models.py)

class PPA(TenantScopedModel):
    """Program/Project/Activity - shared across Ministerial and Budget portals"""
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    type = models.CharField(choices=['program', 'project', 'activity'])
    parent = models.ForeignKey('self', null=True)
    # Used by: Ministerial (planning), Budget (costing), Parliamentary (oversight)

class BudgetItem(TenantScopedModel):
    """Budget line item - shared across Budget and Parliamentary portals"""
    ppa = models.ForeignKey(PPA)
    fiscal_year = models.IntegerField()
    amount_proposed = models.DecimalField()
    amount_authorized = models.DecimalField()
    # Used by: Budget (all phases), Parliamentary (authorization, oversight)

class MOAProfile(TenantScopedModel):
    """Ministry/Office/Agency profile - referenced by all portals"""
    name = models.CharField(max_length=255)
    acronym = models.CharField(max_length=20)
    type = models.CharField(choices=['ministry', 'office', 'agency'])
    # Used by: All portals for tenant context
```

---

## 6. Authentication, Authorization & Multi-Tenancy

### 6.1 Unified Authentication Flow

```text
┌─────────────────────────────────────────────────────────────────────┐
│                    AUTHENTICATION FLOW                               │
│                                                                      │
│   User visits any portal                                             │
│          │                                                           │
│          ▼                                                           │
│   ┌───────────────────────────────────┐                             │
│   │  e-governance.bangsamoro.site/auth │  ◀─── Unified Auth Service │
│   │  (SSO/OAuth)                       │                             │
│   └──────────────────┬─────────────────┘                            │
│              │                                                       │
│              ▼                                                       │
│   ┌─────────────────────┐                                           │
│   │  Validate           │                                           │
│   │  Credentials        │                                           │
│   └──────────┬──────────┘                                           │
│              │                                                       │
│              ▼                                                       │
│   ┌─────────────────────┐                                           │
│   │  Determine Portal   │                                           │
│   │  Access Rights      │                                           │
│   └──────────┬──────────┘                                           │
│              │                                                       │
│         ┌────┴────┬────────────┐                                    │
│         ▼         ▼            ▼                                    │
│   ┌──────────┐ ┌──────────┐ ┌──────────┐                           │
│   │Parliament│ │Ministerial│ │ Budget  │                           │
│   │  Portal  │ │  Portal   │ │ Portal  │                           │
│   └──────────┘ └───────────┘ └──────────┘                           │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

### 6.2 Multi-Tenancy Architecture

BPMP implements a hierarchical multi-tenant architecture to isolate data between government organizations while supporting sub-organizational structures.

#### 6.2.1 Tenant Hierarchy

```text
┌─────────────────────────────────────────────────────────────────────┐
│                    TENANT HIERARCHY                                  │
│                                                                      │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                      TENANT (Top-Level)                      │   │
│   │   Types: parliament | ministry | office | agency             │   │
│   │                                                              │   │
│   │   Examples:                                                  │   │
│   │   - Bangsamoro Parliament (parliament)                       │   │
│   │   - Ministry of Finance (ministry)                           │   │
│   │   - Office of the Chief Minister (office)                    │   │
│   │   - BPDA (agency)                                            │   │
│   └─────────────────────────┬───────────────────────────────────┘   │
│                             │                                        │
│              ┌──────────────┼──────────────┐                        │
│              ▼              ▼              ▼                        │
│   ┌──────────────┐ ┌──────────────┐ ┌──────────────┐               │
│   │  SUB-TENANT  │ │  SUB-TENANT  │ │  SUB-TENANT  │               │
│   │  (mp_office) │ │ (committee)  │ │  (division)  │               │
│   │              │ │              │ │              │               │
│   │  MP Office   │ │ Ways & Means │ │ Finance Div  │               │
│   │  of Hon. X   │ │ Committee    │ │              │               │
│   └──────────────┘ └──────────────┘ └──────────────┘               │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

#### 6.2.2 Tenant Model Structure

```python
# backend/apps/tenants/models.py

class Tenant(models.Model):
    """Top-level organizational entity"""

    TENANT_TYPE_CHOICES = [
        ('parliament', 'Parliament'),
        ('ministry', 'Ministry'),
        ('office', 'Office'),
        ('agency', 'Agency'),
    ]

    code = models.CharField(max_length=50, unique=True)  # e.g., PARLIAMENT, MFBM, OCM
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TENANT_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)


class SubTenant(models.Model):
    """Sub-division within a Tenant"""

    SUBTENANT_TYPE_CHOICES = [
        ('mp_office', 'MP Office'),
        ('committee', 'Committee'),
        ('support', 'Support Services'),
        ('division', 'Division'),
    ]

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=SUBTENANT_TYPE_CHOICES)
```

#### 6.2.3 Tenant-Portal Mapping

| Tenant Type | Primary Portal | Secondary Portal Access |
|-------------|----------------|------------------------|
| **Parliament** | Parliamentary Portal | Budget Portal (view) |
| **Ministry** | Ministerial Portal | Budget Portal (full) |
| **Office** (OCM, Speaker) | All Portals | Oversight interfaces |
| **Agency** (MFBM, BPDA) | Specialized interfaces | Cross-portal consolidation |

#### 6.2.4 Sub-Tenant Types per Portal

| Portal | Sub-Tenant Types | Examples |
|--------|------------------|----------|
| **Parliamentary** | mp_office, committee, support | MP Office of Hon. X, Ways & Means Committee |
| **Ministerial** | division, support | Planning Division, Finance Service |
| **Budget** | division | Budget Division, Accounting Division |

#### 6.2.5 Tenant Data Isolation

All tenant-scoped models inherit from `TenantModelMixin`:

```python
# backend/apps/core/mixins.py

class TenantModelMixin(models.Model):
    """Abstract mixin for tenant-scoped models"""

    tenant = models.ForeignKey(
        'tenants.Tenant',
        on_delete=models.CASCADE,
        related_name='%(class)s_set',
        db_index=True,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.tenant_id:
            raise ValidationError("Tenant must be specified before saving.")
        super().save(*args, **kwargs)


class TenantQuerySetMixin:
    """QuerySet mixin for automatic tenant filtering"""

    def for_tenant(self, tenant):
        return self.filter(tenant_id=tenant.pk if hasattr(tenant, 'pk') else tenant)

    def for_user_tenant(self, user):
        return self.for_tenant(user.tenant)
```

---

### 6.3 Role-Based Access Control (RBAC)

BPMP implements a comprehensive RBAC system with module-level and action-level permissions.

#### 6.3.1 RBAC Model Structure

```text
┌─────────────────────────────────────────────────────────────────────┐
│                       RBAC MODEL STRUCTURE                           │
│                                                                      │
│   ┌──────────────┐         ┌──────────────┐         ┌────────────┐ │
│   │     USER     │────────▶│     ROLE     │────────▶│ PERMISSION │ │
│   │              │   1:1   │              │   M:N   │            │ │
│   │  - email     │         │  - code      │         │ - code     │ │
│   │  - tenant    │         │  - name      │         │ - module   │ │
│   │  - sub_tenant│         │  - role_type │         │ - action   │ │
│   │  - role      │         │  - level     │         │            │ │
│   └──────────────┘         │  - permissions│         └────────────┘ │
│                            └──────────────┘                         │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

#### 6.3.2 Permission Model

```python
# backend/apps/accounts/models.py

class Permission(models.Model):
    """Module-level permission with action granularity"""

    MODULE_CHOICES = [
        ('dashboard', 'Dashboard'),
        ('legislative', 'Legislative Work'),
        ('oversight', 'Oversight Work'),
        ('representation', 'Representation Work'),
        ('ministerial', 'Ministerial Planning'),
        ('budget', 'Budget Management'),
        ('office', 'Office Management'),
        ('admin', 'Administration'),
    ]

    ACTION_CHOICES = [
        ('view', 'View'),
        ('create', 'Create'),
        ('edit', 'Edit'),
        ('delete', 'Delete'),
        ('approve', 'Approve'),
        ('export', 'Export'),
        ('manage', 'Manage'),
    ]

    code = models.CharField(max_length=100, unique=True)  # e.g., "legislative.view"
    name = models.CharField(max_length=255)
    module = models.CharField(max_length=50, choices=MODULE_CHOICES)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
```

#### 6.3.3 Role Model

```python
class Role(models.Model):
    """Role with permission assignments and hierarchy"""

    ROLE_TYPE_CHOICES = [
        ('mp', 'Member of Parliament'),
        ('minister', 'Minister'),
        ('deputy_minister', 'Deputy Minister'),
        ('committee_chair', 'Committee Chair'),
        ('committee_member', 'Committee Member'),
        ('committee_staff', 'Committee Staff'),
        ('office_staff', 'Office Staff'),
        ('legislative_staff', 'Legislative Staff'),
        ('constituent', 'Constituent'),
        ('admin', 'Administrator'),
        ('super_admin', 'Super Administrator'),
    ]

    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    role_type = models.CharField(max_length=50, choices=ROLE_TYPE_CHOICES)
    permissions = models.ManyToManyField(Permission, related_name='roles')
    level = models.PositiveIntegerField(default=0)  # Higher = more privileges

    def has_permission(self, module: str, action: str) -> bool:
        return self.permissions.filter(module=module, action=action, is_active=True).exists()
```

#### 6.3.4 User-Role Integration

```python
class User(AbstractUser):
    """Custom User with multi-tenant and RBAC support"""

    email = models.EmailField(unique=True)
    tenant = models.ForeignKey('tenants.Tenant', on_delete=models.CASCADE, null=True)
    sub_tenant = models.ForeignKey('tenants.SubTenant', on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def has_module_permission(self, module: str, action: str = 'view') -> bool:
        if self.is_superuser:
            return True
        if not self.role:
            return False
        return self.role.has_permission(module, action)
```

---

### 6.4 Permission Matrix

#### 6.4.1 Module × Action Matrix

| Module | view | create | edit | delete | approve | export | manage |
|--------|------|--------|------|--------|---------|--------|--------|
| **dashboard** | All users | - | - | - | - | Admin | Admin |
| **legislative** | Parliament | Parliament | Parliament | Admin | Committee Chair | Parliament | Admin |
| **oversight** | Parliament | Parliament | Parliament | Admin | MP | Parliament | Admin |
| **representation** | Parliament | Parliament | Parliament | Admin | MP | Parliament | Admin |
| **ministerial** | MOA | MOA | MOA | Admin | Minister | MOA | Admin |
| **budget** | All | Budget Staff | Budget Staff | Admin | Budget Officer | Budget Staff | Admin |
| **office** | Own tenant | Own tenant | Own tenant | Admin | Manager | Own tenant | Admin |
| **admin** | Admin | Admin | Admin | Super Admin | Super Admin | Admin | Super Admin |

#### 6.4.2 Role-Permission Assignments

| Role | Primary Permissions | Portal Access |
|------|---------------------|---------------|
| **super_admin** | All modules, all actions | All portals |
| **mp** | legislative.*, oversight.*, representation.*, office.view | Parliamentary |
| **committee_chair** | legislative.*, oversight.approve | Parliamentary |
| **committee_staff** | legislative.view/create/edit, oversight.view | Parliamentary |
| **minister** | ministerial.*, budget.view/create/edit, office.* | Ministerial, Budget |
| **deputy_minister** | ministerial.view/create/edit, budget.view | Ministerial |
| **planning_officer** | ministerial.view/create/edit | Ministerial |
| **budget_officer** | budget.*, ministerial.view | Budget, Ministerial |
| **office_staff** | office.view/create/edit | Own portal |

---

### 6.5 Portal Access by Role

| Role | Parliament Portal | Ministerial Portal | Budget Portal |
|------|-------------------|-------------------|---------------|
| **Super Admin** | Full Access | Full Access | Full Access |
| **MP** | Full Access | View Only | View Only |
| **Committee Chair** | Full Access | View Only | View Only |
| **Committee Staff** | Full Access | View Only | View Only |
| **Minister** | View Only | Full Access | Full Access |
| **Deputy Minister** | View Only | Full Access | View Only |
| **Planning Officer** | View Only | Full Access | View Only |
| **Budget Officer** | View Only | View Only | Full Access |
| **Finance Staff** | None | None | Full Access |
| **Office Staff** | Own Portal Only | Own Portal Only | None |

---

### 6.6 DRF Permission Classes

```python
# backend/apps/core/permissions.py

class IsTenantMember(BasePermission):
    """Verify user belongs to the resource's tenant"""

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if not hasattr(obj, 'tenant'):
            return True
        return obj.tenant_id == request.user.tenant_id


class HasModulePermission(BasePermission):
    """Check user has permission for a specific module"""

    module = None  # Override in subclass
    action_map = {
        'list': 'view', 'retrieve': 'view',
        'create': 'create', 'update': 'edit',
        'partial_update': 'edit', 'destroy': 'delete',
    }

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        action = self.action_map.get(view.action, 'view')
        return request.user.has_module_permission(self.module, action)


class TenantScopedModulePermission(IsTenantMember, HasModulePermission):
    """Combined tenant + module permission check"""

    def has_permission(self, request, view):
        return (
            IsTenantMember.has_permission(self, request, view) and
            HasModulePermission.has_permission(self, request, view)
        )


# Ready-to-use permission classes
class LegislativePermission(TenantScopedModulePermission):
    module = 'legislative'

class OversightPermission(TenantScopedModulePermission):
    module = 'oversight'

class MinisterialPermission(TenantScopedModulePermission):
    module = 'ministerial'

class BudgetPermission(TenantScopedModulePermission):
    module = 'budget'

class OfficePermission(TenantScopedModulePermission):
    module = 'office'
```

---

### 6.7 JWT Token Structure

```json
{
  "user_id": "uuid",
  "email": "user@example.gov.ph",
  "tenant_id": "uuid",
  "tenant_code": "MFBM",
  "tenant_type": "ministry",
  "sub_tenant_id": "uuid",
  "sub_tenant_code": "BUDGET_DIV",
  "role": {
    "code": "budget_officer",
    "type": "budget_officer",
    "level": 5
  },
  "portal_access": ["ministerial", "budget"],
  "permissions": [
    "budget.view", "budget.create", "budget.edit", "budget.approve",
    "ministerial.view"
  ],
  "exp": 1704067200
}
```

---

### 6.8 Cross-Portal Access Patterns

#### 6.8.1 Special Interface Access

Organizations with oversight/consolidation responsibilities have special cross-portal access:

| Organization | Portal | Special Access |
|--------------|--------|----------------|
| **MFBM** | Budget Portal | Government-wide budget consolidation view |
| **BPDA** | Ministerial Portal | Government-wide planning consolidation view |
| **OCM** | All Portals | Executive oversight dashboard |
| **Speaker's Office** | Parliamentary + Budget | Legislative budget oversight |

#### 6.8.2 Cross-Portal Data Access Flow

```text
┌─────────────────────────────────────────────────────────────────────┐
│              CROSS-PORTAL ACCESS PATTERNS                            │
│                                                                      │
│   MFBM User (Budget Portal)                                         │
│   ├── Own MOA: Full budget CRUD                                     │
│   └── All MOAs: Read-only budget consolidation view                 │
│                                                                      │
│   BPDA User (Ministerial Portal)                                    │
│   ├── Own MOA: Full planning CRUD                                   │
│   └── All MOAs: Read-only planning consolidation view               │
│                                                                      │
│   OCM User (All Portals)                                            │
│   ├── Executive Dashboard: Aggregated metrics from all portals      │
│   └── Drill-down: Read-only access to specific MOA data             │
│                                                                      │
│   Speaker's Office (Parliamentary + Budget)                         │
│   ├── Parliamentary: Full legislative access                        │
│   └── Budget: Read-only budget oversight view                       │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 7. Navigation Architecture

### 7.1 Parliamentary Portal Navigation

```
┌─────────────────────────────────────────────────────────────────────┐
│  PARLIAMENTARY PORTAL - e-governance.bangsamoro.site/parliament      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────────┐  ┌─────────────────────────────────────────────┐  │
│  │   SIDEBAR   │  │              TOP NAVBAR                      │  │
│  │             │  │  [Legislative ▼] [Oversight ▼] [Represent.]  │  │
│  │  Dashboard  │  └─────────────────────────────────────────────┘  │
│  │  ─────────  │                                                    │
│  │  Legislative│  ┌─────────────────────────────────────────────┐  │
│  │  Oversight  │  │                                             │  │
│  │  Represent. │  │           CONTENT AREA                      │  │
│  │  ─────────  │  │                                             │  │
│  │  Office     │  │                                             │  │
│  │  ─────────  │  │                                             │  │
│  │  Settings   │  │                                             │  │
│  │  AI Assist  │  │                                             │  │
│  └─────────────┘  └─────────────────────────────────────────────┘  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘

Sidebar (Icons):
├── Dashboard (Home)
├── Legislative Work (Scroll)
├── Oversight Work (Search/Eye)
├── Representation Work (Users)
├── Office Management (Building)
├── Settings (Gear)
└── AI Assistant (Sparkle)

Top Navbar (Dropdowns per active module):
├── Legislative: Tracking, Drafting, Research, Analysis, Budget Bills, Plenary, Committees
├── Oversight: Budget Tracking, Program Tracking, Issues, M&E Analytics
├── Representation: Constituency, Beneficiaries, Requests, Media
└── Office: Org Structure, Staff, Tasks, Calendar
```

### 7.2 Ministerial Portal Navigation

```
┌─────────────────────────────────────────────────────────────────────┐
│  MINISTERIAL PORTAL - e-governance.bangsamoro.site/ministry         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────────┐  ┌─────────────────────────────────────────────┐  │
│  │   SIDEBAR   │  │              TOP NAVBAR                      │  │
│  │             │  │  [Planning Framework ▼] [Office ▼]           │  │
│  │  Dashboard  │  └─────────────────────────────────────────────┘  │
│  │  ─────────  │                                                    │
│  │  Planning   │  ┌─────────────────────────────────────────────┐  │
│  │  Office     │  │                                             │  │
│  │  ─────────  │  │           CONTENT AREA                      │  │
│  │  Settings   │  │                                             │  │
│  │  AI Assist  │  │      (10-Point Framework Interface)         │  │
│  │             │  │                                             │  │
│  └─────────────┘  └─────────────────────────────────────────────┘  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘

Sidebar (Icons):
├── Dashboard (Home)
├── Planning (Clipboard/Target)
├── Office Management (Building)
├── Settings (Gear)
└── AI Assistant (Sparkle)

Top Navbar (Dropdowns):
├── Planning: Points 1-10 (Legal, BDP, Priority, Stakeholders, Strategy, ToC, PPA, Resources, Work Plan, RBME)
└── Office: Org Structure, Staff, Tasks, Calendar
```

### 7.3 Budget Portal Navigation

```
┌─────────────────────────────────────────────────────────────────────┐
│  BUDGET PORTAL - e-governance.bangsamoro.site/budget (No Office Mgmt)│
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────────┐  ┌─────────────────────────────────────────────┐  │
│  │   SIDEBAR   │  │              TOP NAVBAR                      │  │
│  │             │  │  [Preparation ▼] [Authorization ▼]           │  │
│  │  Dashboard  │  │  [Execution ▼] [Accountability ▼]            │  │
│  │  ─────────  │  └─────────────────────────────────────────────┘  │
│  │  Preparation│                                                    │
│  │  Authoriz.  │  ┌─────────────────────────────────────────────┐  │
│  │  Execution  │  │                                             │  │
│  │  Account.   │  │           CONTENT AREA                      │  │
│  │  ─────────  │  │                                             │  │
│  │  Settings   │  │       (BBSA Forms & Workflows)              │  │
│  │  AI Assist  │  │                                             │  │
│  └─────────────┘  └─────────────────────────────────────────────┘  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘

Sidebar (Icons):
├── Dashboard (Home)
├── Budget Preparation (File/Document)
├── Budget Authorization (Check/Stamp)
├── Budget Execution (Play/Arrow)
├── Budget Accountability (Scale/Report)
├── Settings (Gear)
└── AI Assistant (Sparkle)

Note: No Office Management module - Budget Portal is specialized for BBSA operations only.
Budget Officers access Office Management through their organization's primary portal.

Top Navbar (Dropdowns):
├── Preparation: Estimates, Forms (100-500), PPA Costing, Resources
├── Authorization: Review, Amendments, Appropriations, Approval
├── Execution: Allotments, Obligations, Disbursements, Monitoring
└── Accountability: Reports, Audits, Variance, Performance
```

---

## 8. Shared Infrastructure

### 8.1 Shared Component Library

```
@bpmp/ui (Shared Package)
├── components/
│   ├── Button/
│   ├── Card/
│   ├── DataTable/
│   ├── Form/
│   ├── Modal/
│   ├── Navigation/
│   │   ├── Sidebar.tsx
│   │   ├── TopNavbar.tsx
│   │   └── Breadcrumb.tsx
│   ├── Charts/
│   │   ├── BarChart.tsx
│   │   ├── LineChart.tsx
│   │   └── PieChart.tsx
│   └── Maps/
│       └── BARMMMap.tsx
├── hooks/
│   ├── useAuth.ts
│   ├── useTenant.ts
│   └── usePortal.ts
├── styles/
│   └── globals.css (Tailwind base)
└── utils/
    ├── api.ts
    └── formatters.ts
```

### 8.2 API Structure

```
api.bpmp.gov.ph/v1/
├── auth/
│   ├── login/
│   ├── logout/
│   ├── refresh/
│   └── portal-access/
├── parliamentary/
│   ├── legislative/
│   ├── oversight/
│   └── representation/
├── ministerial/
│   ├── planning/
│   └── ppa/
├── budget/
│   ├── preparation/
│   ├── authorization/
│   ├── execution/
│   └── accountability/
├── office/
│   ├── staff/
│   ├── tasks/
│   └── calendar/
└── shared/
    ├── tenants/
    ├── users/
    └── notifications/
```

### 8.3 Backend App Organization

```python
# backend/config/settings/base.py

INSTALLED_APPS = [
    # Django core
    'django.contrib.admin',
    'django.contrib.auth',
    ...

    # Third-party
    'rest_framework',
    'corsheaders',
    ...

    # BPMP Core (shared across portals)
    'apps.core',
    'apps.accounts',
    'apps.tenants',
    'apps.ai',
    'apps.realtime',

    # Parliamentary Portal apps
    'apps.legislative',
    'apps.oversight',
    'apps.representation',

    # Ministerial Portal apps
    'apps.ministerial',

    # Budget Portal apps
    'apps.budget',

    # Office (shared across portals)
    'apps.office',
]
```

---

## 9. Deployment Architecture

### 9.1 Railway Deployment Structure

```
┌─────────────────────────────────────────────────────────────────────┐
│                    RAILWAY DEPLOYMENT                                │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                    RAILWAY PROJECT                           │    │
│  │                                                              │    │
│  │  ┌────────────────┐  ┌────────────────┐  ┌──────────────┐   │    │
│  │  │ parliamentary- │  │ ministerial-   │  │ budget-      │   │    │
│  │  │ frontend       │  │ frontend       │  │ frontend     │   │    │
│  │  │ (React/Vite)   │  │ (React/Vite)   │  │ (React/Vite) │   │    │
│  │  └───────┬────────┘  └───────┬────────┘  └──────┬───────┘   │    │
│  │          │                   │                   │           │    │
│  │          └───────────────────┼───────────────────┘           │    │
│  │                              │                               │    │
│  │                              ▼                               │    │
│  │  ┌─────────────────────────────────────────────────────┐    │    │
│  │  │              bpmp-backend (Django)                   │    │    │
│  │  │              api.bpmp.gov.ph                         │    │    │
│  │  └───────────────────────┬─────────────────────────────┘    │    │
│  │                          │                                   │    │
│  │          ┌───────────────┼───────────────┐                  │    │
│  │          ▼               ▼               ▼                  │    │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │    │
│  │  │  PostgreSQL  │ │    Redis     │ │ Cloudflare   │        │    │
│  │  │  (Railway)   │ │  (Railway)   │ │     R2       │        │    │
│  │  └──────────────┘ └──────────────┘ └──────────────┘        │    │
│  │                                                              │    │
│  └──────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  URL Configuration (Single Domain with Path-Based Routing):          │
│  - e-governance.bangsamoro.site/parliament → parliamentary-frontend │
│  - e-governance.bangsamoro.site/ministry → ministerial-frontend     │
│  - e-governance.bangsamoro.site/budget → budget-frontend            │
│  - e-governance.bangsamoro.site/api → bpmp-backend                  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### 9.2 Repository Structure Options

#### Option A: Monorepo (Recommended)

```
bpmp/
├── backend/                    # Django backend (unchanged)
│   ├── apps/
│   ├── api/
│   ├── config/
│   └── manage.py
├── packages/
│   └── ui/                     # Shared component library
│       ├── src/
│       └── package.json
├── portals/
│   ├── parliamentary/          # Parliamentary portal frontend
│   │   ├── src/
│   │   ├── package.json
│   │   └── vite.config.ts
│   ├── ministerial/            # Ministerial portal frontend
│   │   ├── src/
│   │   ├── package.json
│   │   └── vite.config.ts
│   └── budget/                 # Budget portal frontend
│       ├── src/
│       ├── package.json
│       └── vite.config.ts
├── package.json                # Workspace root
├── pnpm-workspace.yaml         # pnpm workspace config
└── GEMINI.md
```

#### Option B: Separate Repositories

```
github.com/bpmp/
├── bpmp-backend               # Django API
├── bpmp-ui                    # Shared component library (npm package)
├── bpmp-parliamentary         # Parliamentary portal
├── bpmp-ministerial           # Ministerial portal
└── bpmp-budget                # Budget portal
```

### 9.3 Environment Configuration

```bash
# Backend (.env)
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
ALLOWED_ORIGINS=https://e-governance.bangsamoro.site
BASE_URL=https://e-governance.bangsamoro.site
JWT_SECRET_KEY=...

# Parliamentary Frontend (.env)
VITE_API_URL=https://e-governance.bangsamoro.site/api
VITE_PORTAL_NAME=parliamentary
VITE_PORTAL_PATH=/parliament
VITE_AUTH_URL=https://e-governance.bangsamoro.site/auth

# Ministerial Frontend (.env)
VITE_API_URL=https://e-governance.bangsamoro.site/api
VITE_PORTAL_NAME=ministerial
VITE_PORTAL_PATH=/ministry
VITE_AUTH_URL=https://e-governance.bangsamoro.site/auth

# Budget Frontend (.env)
VITE_API_URL=https://e-governance.bangsamoro.site/api
VITE_PORTAL_NAME=budget
VITE_PORTAL_PATH=/budget
VITE_AUTH_URL=https://e-governance.bangsamoro.site/auth
```

---

## 10. Implementation Strategy

### 10.1 Phase 1: Foundation (Weeks 1-4)

**Objective**: Establish shared infrastructure

- [ ] Set up pnpm monorepo workspace
- [ ] Create `@bpmp/ui` shared component library
- [ ] Extract common components from current frontend
- [ ] Set up Railway services for 3 frontend deployments
- [ ] Configure CORS for multi-origin API access
- [ ] Implement portal-aware JWT tokens
- [ ] Create portal routing middleware in backend

### 10.2 Phase 2: Parliamentary Portal (Weeks 5-8)

**Objective**: Complete Parliamentary Portal

- [ ] Create parliamentary portal project
- [ ] Migrate Legislative Work module
- [ ] Migrate Oversight Work module
- [ ] Migrate Representation Work module
- [ ] Implement portal-specific dashboard
- [ ] Configure path routing: /parliament

### 10.3 Phase 3: Ministerial Portal (Weeks 9-12)

**Objective**: Complete Ministerial Portal

- [ ] Create ministerial portal project
- [ ] Migrate Ministerial Planning module
- [ ] Migrate Office Management (shared)
- [ ] Implement 10-Point Framework navigation
- [ ] Implement portal-specific dashboard
- [ ] Configure path routing: /ministry

### 10.4 Phase 4: Budget Portal (Weeks 13-16)

**Objective**: Complete Budget Portal (Specialized - No Office Management)

- [ ] Create budget portal project
- [ ] Migrate Budget Management module
- [ ] Implement BBSA forms interface
- [ ] Implement PPA-Budget linkage views
- [ ] Implement portal-specific dashboard
- [ ] Configure path routing: /budget
- [ ] Note: No Office Management migration - this is a specialized budget-only portal

### 10.5 Phase 5: Integration & Testing (Weeks 17-20)

**Objective**: Ensure cross-portal functionality

- [ ] Test cross-portal data flows
- [ ] Verify SSO across all portals
- [ ] Validate role-based access restrictions
- [ ] Performance testing
- [ ] Security audit
- [ ] User acceptance testing

---

## Appendix A: Color System per Portal

All portals use the BPMP Blue primary color (#0056D2) with portal-specific accent colors:

| Portal | Primary | Accent | Usage |
|--------|---------|--------|-------|
| Parliamentary | BPMP Blue | Emerald (#10B981) | Legislative actions |
| Ministerial | BPMP Blue | Amber (#F59E0B) | Planning highlights |
| Budget | BPMP Blue | Teal (#14B8A6) | Financial indicators |

**Note**: No purple colors are used in any portal.

---

## Appendix B: AI Agent Distribution

| Portal | AI Agents |
|--------|-----------|
| Parliamentary | Legislative Tracker, Drafting Assistant, Legal Research, Analysis, Budget Legislation, Plenary Assistant, Committee Assistant, Oversight Agents |
| Ministerial | Legal Alignment, BDP Alignment, Priority Agenda, Stakeholder, Strategy, ToC, PPA Planning, Resource Planning, Annual Planning, RBME Agents |
| Budget | Budget Prep, Authorization, Execution, Accountability Agents |

---

## Appendix C: API Endpoint Access Matrix

| Endpoint Group | Parliamentary | Ministerial | Budget |
|----------------|---------------|-------------|--------|
| `/api/v1/legislative/*` | Full | None | None |
| `/api/v1/oversight/*` | Full | Read (own) | Read (budget) |
| `/api/v1/representation/*` | Full | None | None |
| `/api/v1/planning/*` | Read | Full | Read (PPA) |
| `/api/v1/budget/*` | Read | Own prep | Full |
| `/api/v1/office/*` | Own tenant | Own tenant | None |
| `/api/v1/shared/*` | Full | Full | Full |

**Note**: Budget Portal does not access `/api/v1/office/*` endpoints. Budget Officers manage office operations through their organization's primary portal (Parliamentary or Ministerial).

---

**Document End**

*This architecture document should be reviewed and approved before implementation begins.*
