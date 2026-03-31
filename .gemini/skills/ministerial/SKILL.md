---
name: ministerial
description: Ministerial planning domain skill for BPMP. Covers strategic planning, the Enhanced 12-Point Priority Agenda framework, program management, and ministerial coordination. Use when implementing planning features, KPI tracking, or ministerial dashboards.
argument-hint: "[topic]"
---

# Ministerial Planning - BPMP

## Purpose
Provides domain expertise for the Ministerial Planning module of BPMP, covering strategic planning, the Enhanced 12-Point Priority Agenda, and ministerial coordination aligned with the 2nd Bangsamoro Development Plan (BDP) 2023-2028.

## When to Use
- Implementing strategic planning features
- Building program tracking dashboards
- Creating KPI monitoring systems
- Implementing ministerial coordination tools
- Designing planning document workflows
- Aligning programs with the 12-Point Priority Agenda

## Key Entities
- **StrategicPlan**: Long-term development plans aligned with BDP
- **Program**: Ministerial programs and initiatives
- **Project**: Specific projects under programs
- **KPI**: Key Performance Indicators
- **Target**: Annual/quarterly targets
- **Achievement**: Recorded achievements against targets
- **AgendaPoint**: The 12 priority areas

## Enhanced 12-Point Priority Agenda (2023-2025)
The official BARMM development framework under Chief Minister Ahod "Al Haj Murad" Ebrahim:

1. **Stronger BARMM Bureaucracy** - Building institutional capacity and governance structures
2. **Digital Infrastructure and E-Governance** - Technology-enabled government services
3. **Revenue Generation and Economic Comparative Advantage** - Fiscal sustainability and economic growth
4. **Agri-Fishery Productivity and Food Security** - Agricultural development and food self-sufficiency
5. **Transportation, Communication, and Strategic Infrastructure** - Physical connectivity and development
6. **Energy Security** - Sustainable power and renewable energy development
7. **Social Protection and Universal Healthcare** - Health services and social safety nets
8. **Disaster Resilience and Climate Change Adaptation** - Environmental preparedness
9. **Quality and Holistic Education** - Educational development and human capital
10. **Marawi Rehabilitation Support** - Post-conflict reconstruction and recovery
11. **Peace, Justice, and Security** - Rule of law and conflict resolution
12. **Bangsamoro Culture, Heritage, and Diversity** - Cultural preservation and identity

**Cross-Cutting Themes**: Inclusion, Equality, Justice, and Moral Governance

**Source**: [BARMM Official - CM Ebrahim 12-Point Priority Agenda](https://mindanao.politiko.com.ph/cm-ebrahim-cites-btas-12-point-priority-agenda-for-2023-2025/)

## Reference Files
- [strategic-planning.md](references/strategic-planning.md) - Strategic planning frameworks
- [twelve-point-agenda.md](references/twelve-point-agenda.md) - Detailed 12-Point Priority Agenda
- [program-management.md](references/program-management.md) - Program and project management

## Data Models

### StrategicPlan
```python
class StrategicPlan(TenantModel):
    title: str
    description: str
    vision: str
    mission: str
    start_date: date
    end_date: date
    status: PlanStatus  # draft, active, completed, archived
    agenda_points: list[AgendaPoint]  # 12-Point Priority Agenda mapping
    created_by: User
```

### Program
```python
class Program(TenantModel):
    strategic_plan: StrategicPlan
    name: str
    description: str
    ministry: Ministry
    budget_allocation: Decimal
    start_date: date
    end_date: date
    status: ProgramStatus
    agenda_point: AgendaPoint  # Primary 12-Point Agenda alignment
```

### Project
```python
class Project(TenantModel):
    program: Program
    name: str
    description: str
    project_manager: User
    budget: Decimal
    timeline: DateRange
    status: ProjectStatus
    location: Location  # Municipality/Province
    beneficiaries: int
```

### KPI
```python
class KPI(TenantModel):
    program: Program
    name: str
    description: str
    unit: str  # percentage, count, peso, etc.
    baseline: Decimal
    target_value: Decimal
    current_value: Decimal
    frequency: ReportingFrequency  # monthly, quarterly, annually
```

## API Endpoints

### Strategic Plans
- `GET /api/v1/ministerial/plans/` - List strategic plans
- `POST /api/v1/ministerial/plans/` - Create plan
- `GET /api/v1/ministerial/plans/{id}/` - Get plan details
- `GET /api/v1/ministerial/plans/{id}/dashboard/` - Plan dashboard data

### Programs
- `GET /api/v1/ministerial/programs/` - List programs
- `POST /api/v1/ministerial/programs/` - Create program
- `GET /api/v1/ministerial/programs/{id}/kpis/` - Program KPIs

### Projects
- `GET /api/v1/ministerial/projects/` - List projects
- `GET /api/v1/ministerial/projects/map/` - Project locations GeoJSON

### KPIs & Achievements
- `GET /api/v1/ministerial/kpis/` - List KPIs
- `POST /api/v1/ministerial/achievements/` - Record achievement
- `GET /api/v1/ministerial/achievements/report/` - Achievement report

## Frontend Components

### Dashboard Components
- `MinisterialDashboard` - Main planning dashboard
- `AgendaProgressChart` - 12-Point Priority Agenda progress visualization
- `ProgramStatusBoard` - Kanban-style program tracking
- `KPIGaugeCard` - Individual KPI gauge display
- `ProjectMap` - Leaflet map of project locations

### Planning Components
- `StrategicPlanForm` - Plan creation/editing
- `ProgramForm` - Program management
- `ProjectTimeline` - Gantt chart for projects
- `KPITracker` - KPI entry and tracking

### Report Components
- `MinisterialReport` - Comprehensive planning report
- `AgendaReport` - Per-agenda-point report
- `AchievementSummary` - Achievement summaries

## Business Rules

### Plan Lifecycle
1. **Draft**: Initial creation, can be edited freely
2. **Under Review**: Submitted for approval
3. **Active**: Approved and being implemented
4. **Completed**: All programs finished
5. **Archived**: Historical reference

### KPI Tracking
- KPIs must have baseline and target values
- Achievements recorded against KPI targets
- Automatic progress calculation
- Alert thresholds for underperformance

### Budget Alignment
- Program budgets must align with BBSA allocations
- Cross-reference with Budget Management module
- Track budget utilization per program

## Integration Points

### With Budget Management
- Budget allocation verification
- Expenditure tracking
- Financial reporting alignment

### With Oversight Work
- MOA tracking for funded programs
- Progress monitoring
- Compliance reporting

### With Office Management
- Task assignment for program activities
- Calendar integration for milestones
- Staff workload balancing

## Reporting Requirements

### Quarterly Reports
- Per-priority-agenda progress
- Program status summary
- KPI achievement rates
- Budget utilization

### Annual Reports
- Strategic plan progress
- Year-over-year comparisons
- Impact assessments
- Recommendations

## Multi-Tenancy Considerations
- Plans scoped to BTA/Ministry tenant
- Cross-ministry visibility for Chief Minister
- Consolidated reporting for BTA leadership
