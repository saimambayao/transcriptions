---
name: budget
description: |
  Government budget and financial management for e-Bangsamoro (Bangsamoro e-Governance Platform).
  Covers BBSA-compliant budget lifecycle, appropriations, allotments, obligations, expenditure tracking,
  fiscal compliance, financial analysis, and fund management.

  Use /budget when:
  - Implementing e-Bangsamoro Budget Management module features
  - Government budget preparation and appropriation tracking
  - BBSA (Bangsamoro Budget and Financial Management Code) compliance
  - Fiscal year planning and budget execution monitoring
  - Budget monitoring, variance analysis, and reporting
  - Fund allocation and expenditure tracking
  - Building budget-related UI components and APIs

  IMPORTANT: This skill requires /prompter invocation first - invoke /prompter immediately upon skill activation.
argument-hint: "[topic]"
---

# e-Bangsamoro Budget & Finance Skill

## Gate: Invoke /prompter Immediately

DO NOT read further. DO NOT proceed with any workflow.

ACTION REQUIRED NOW:
1. INVOKE /prompter with the user's budget/finance request
2. WAIT for /prompter to complete its 5-phase workflow
3. WAIT for user confirmation ("Yes, proceed")
4. ONLY THEN return here and continue below

If user says "No" or "Adjust" - repeat /prompter
If user says "Let me rephrase" - restart with new input

---

## What is e-Bangsamoro Budget & Finance?

> "Positioning BARMM as the Philippines' first digitally-governed region through transparent fiscal management."

e-Bangsamoro Budget & Finance provides comprehensive public sector financial management capabilities for the Bangsamoro Autonomous Region, integrating domain knowledge (BBSA compliance, budget workflows), implementation (Django/React), and platform integration (Budget Portal within e-Bangsamoro).

### e-Bangsamoro (Public) vs. Corporate Finance

| Dimension | e-Bangsamoro (Public) | Corporate Finance |
|-----------|----------------------|-------------------|
| **Primary Goal** | Service delivery, fund utilization | Profitability, shareholder value |
| **Revenue Focus** | Appropriations, block grants | Sales, earnings |
| **Key Metrics** | Utilization rate, obligation rate | ROE, profit margin |
| **Framework** | BBSA, COA, DBM | GAAP, SEC |
| **Currency** | Philippine Peso (PHP) | Various |

---

## When to Use

| Use Case | Mode |
|----------|------|
| Building budget module features | Implementation Mode |
| Understanding BBSA compliance | Domain Knowledge Mode |
| Budget analysis and reporting | Analysis Mode |
| Financial dashboard development | Implementation Mode |
| Budget preparation guidance | Domain Knowledge Mode |

---

## Quick Reference

### Budget Cycle Phases

| Phase | Activities | Timeline |
|-------|------------|----------|
| **Preparation** | Budget call, agency submissions, consolidation | Q2-Q3 (prior FY) |
| **Authorization** | BTA deliberation, appropriations act | Q4 (prior FY) |
| **Execution** | Allotment, obligation, disbursement | Current FY |
| **Accountability** | Monitoring, reporting, audit | Throughout FY |

### Expense Classes

| Code | Class | Description |
|------|-------|-------------|
| **PS** | Personnel Services | Salaries, wages, benefits, allowances |
| **MOOE** | Maintenance & Other Operating Expenses | Supplies, utilities, travel, professional services |
| **CO** | Capital Outlays | Equipment, buildings, infrastructure |
| **FE** | Financial Expenses | Interest, bank charges, loan payments |

### Key Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| **Obligation Rate** | Obligations / Allotment x 100 | >90% by Q4 |
| **Disbursement Rate** | Disbursements / Obligations x 100 | >85% by year-end |
| **Utilization Rate** | Disbursements / Allotment x 100 | >80% by year-end |

### Fund Sources

| Source | Description |
|--------|-------------|
| **Block Grant** | Annual allocation from national government |
| **Special Purpose Funds** | Earmarked for specific programs |
| **Internally Generated Revenue** | BARMM taxes and fees |
| **Grants and Donations** | External funding (ODA, development partners) |

---

## Part 1: Domain Knowledge

### Budget Lifecycle (BBSA Compliant)

```text
APPROPRIATION (Parliament/BTA approved budget)
      |
      v
ALLOTMENT (Authority to incur obligations - ARO, ABM)
      |
      v
OBLIGATION (Commitment to pay - POs, contracts, payroll)
      |
      v
DISBURSEMENT (Actual payment - checks, ADA, cash)
```

### BBSA Compliance

BBSA principles: Fiscal Autonomy, Transparency, Accountability, Efficiency. Full compliance checklist and variance analysis details in reference file.

See: [bbsa-compliance.md](references/bbsa-compliance.md)

---

## Part 2: Implementation

### Key Entities

**Core:** Budget, Appropriation, Allotment, Obligation, Disbursement, BudgetItem
**Supporting:** FiscalYear, FundSource, ExpenseClass, Ministry, Program, Project

### Data Models

Core models: Budget (annual allocation per ministry), Appropriation (legal spending authority with expense class tracking), Obligation (committed expenditure with approval workflow). All amounts in Philippine Peso with DecimalField(max_digits=15, decimal_places=2).

See: [data-models.md](references/data-models.md)

### API Endpoints

Standard CRUD endpoints for budgets, appropriations, and obligations. Custom actions include submit/approve workflows, utilization reports, and fiscal year filtering.

See: [api-endpoints.md](references/api-endpoints.md)

### Frontend Components

Budget dashboard metrics (BudgetMetrics interface), CurrencyDisplay component (PHP formatting with Intl.NumberFormat), and UI color guidelines (emerald/amber/red status indicators, no purple).

See: [frontend-components.md](references/frontend-components.md)

---

## Part 3: Analysis & Reporting

Budget utilization analysis across expense classes (PS, MOOE, CO), common calculation formulas, variance/fund status report templates, and required government reports schedule.

See: [analysis-reporting.md](references/analysis-reporting.md)

---

## Implementation Checklist

When implementing budget features, ensure:

- [ ] All amounts use Philippine Peso (PHP)
- [ ] Fiscal year boundaries are respected
- [ ] Budget cannot exceed appropriation
- [ ] Obligations cannot exceed available balance
- [ ] Proper audit trail for all transactions
- [ ] Multi-tenant isolation enforced
- [ ] Role-based access control implemented
- [ ] BBSA workflow stages followed
- [ ] 12-Point Priority Agenda alignment verified
- [ ] BDP 2023-2028 alignment documented

---

## Related e-Bangsamoro Modules

| Module | Budget Integration |
|--------|-------------------|
| **Dashboard** | Budget utilization overview, fiscal KPIs |
| **Legislative Work** | Budget bills, appropriations tracking |
| **Oversight Work** | MOA budget monitoring, program audits |
| **Ministerial Planning** | Strategic budget alignment, 10-Point Framework |
| **Office Management** | Operational budget tracking |

---

## Skill Integration Network

| Skill | Relationship | Data Exchange |
|-------|--------------|---------------|
| `/financial-analyst` | Technical analysis | Budget analysis, ratios |
| `/e-bangsamoro-investor` | Funding strategy | Development partner financing |
| `/oversight` | Budget monitoring | MOA financial tracking |
| `/legislative` | Appropriations | Budget legislation |
| `/ministerial` | Planning alignment | Strategic budget integration |
| `/backend` | Django models/APIs | Budget implementation |
| `/frontend` | React components | Budget UI |
| `/database` | PostgreSQL schema | Budget data structures |

---

## References

### Internal References

| Reference | Purpose |
|-----------|---------|
| [bbsa-compliance.md](references/bbsa-compliance.md) | BBSA principles, compliance checklist, variance analysis |
| [budget-lifecycle.md](references/budget-lifecycle.md) | Detailed budget stages and workflows |
| [expenditure-tracking.md](references/expenditure-tracking.md) | Obligation and disbursement tracking |
| [data-models.md](references/data-models.md) | Django model definitions (Budget, Appropriation, Obligation) |
| [api-endpoints.md](references/api-endpoints.md) | REST API endpoint specifications |
| [frontend-components.md](references/frontend-components.md) | React components, TypeScript interfaces, UI guidelines |
| [analysis-reporting.md](references/analysis-reporting.md) | Utilization analysis, calculations, report templates |

### External References

| Reference | Purpose |
|-----------|---------|
| BBSA (Bangsamoro Budget and Financial Management Code) | Legal framework |
| General Appropriations Act (GAA) | Annual budget authority |
| COA Rules and Regulations | Audit and accountability |
| DBM Budget Circulars | National budget guidelines |
| BDP 2023-2028 | Development plan alignment |

---

## Constraints

- Use Philippine Peso (PHP) for all monetary values
- Follow COA (Commission on Audit) reporting standards
- Align with DBM (Department of Budget and Management) guidelines
- Respect BBSA (Bangsamoro Budget System Act) requirements
- No purple colors in UI recommendations
- Ensure data privacy for sensitive fiscal information
- Support BARMM-specific fund tracking requirements
- Align with 12-Point Priority Agenda and BDP 2023-2028

---

## Works Cited

[1] Bangsamoro Transition Authority. "Bangsamoro Budget System Act (BBSA)." 2022.
[2] Department of Budget and Management. "Budget Operations Manual for Local Government Units." 2016.
[3] Commission on Audit. "Government Accounting Manual for National Government Agencies." 2015.
[4] BARMM. "Bangsamoro Development Plan 2023-2028." Bangsamoro Planning and Development Authority.
[5] Department of Budget and Management. "Unified Accounts Code Structure (UACS)." Updated 2024.

---

## Currency Note

All financial figures in e-Bangsamoro use **Philippine Peso (PHP)**. Display Format: PHP 1,234,567.89
