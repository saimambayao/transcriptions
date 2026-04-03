# Budget API Endpoints Reference

> Extracted from `/budget` SKILL.md for detailed reference.

## Budget Endpoints

```text
GET    /api/v1/budgets/                    # List budgets
POST   /api/v1/budgets/                    # Create budget
GET    /api/v1/budgets/{id}/               # Get budget details
PUT    /api/v1/budgets/{id}/               # Update budget
DELETE /api/v1/budgets/{id}/               # Delete budget

# Custom actions
POST   /api/v1/budgets/{id}/submit/        # Submit for approval
POST   /api/v1/budgets/{id}/approve/       # Approve budget
GET    /api/v1/budgets/{id}/summary/       # Budget summary with utilization
GET    /api/v1/budgets/fiscal-year/{year}/ # Budgets by fiscal year
```

## Appropriation Endpoints

```text
GET    /api/v1/appropriations/             # List appropriations
POST   /api/v1/appropriations/             # Create appropriation
GET    /api/v1/appropriations/{id}/        # Get appropriation details
GET    /api/v1/appropriations/{id}/utilization/ # Utilization report
```

## Obligation Endpoints

```text
GET    /api/v1/obligations/                # List obligations
POST   /api/v1/obligations/                # Create obligation
GET    /api/v1/obligations/{id}/           # Get obligation details
POST   /api/v1/obligations/{id}/certify/   # Certify obligation
POST   /api/v1/obligations/{id}/approve/   # Approve obligation
```
