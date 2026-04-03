# Budget Analysis & Reporting Reference

> Extracted from `/budget` SKILL.md for detailed reference.

## Budget Utilization Analysis

| Metric | Formula | Target Benchmark |
|--------|---------|------------------|
| Obligation Rate | Obligations / Allotment | >90% by Q4 |
| Disbursement Rate | Disbursements / Obligations | >80% by year-end |
| Overall Utilization | Disbursements / Appropriation | >75% by year-end |
| MOOE Utilization | MOOE Disbursed / MOOE Allotted | Varies by agency |
| PS Utilization | PS Disbursed / PS Allotted | ~100% expected |
| CO Utilization | CO Disbursed / CO Allotted | Project-dependent |

## Common Calculations

```python
# Utilization Rate
utilization_rate = (obligated_amount / approved_amount) * 100

# Disbursement Rate
disbursement_rate = (disbursed_amount / obligated_amount) * 100

# Available Balance
available_balance = approved_amount - obligated_amount

# Unreleased Appropriation
unreleased = approved_amount - released_amount

# Budget Variance
budget_variance = budgeted_amount - actual_amount
variance_percentage = (budget_variance / budgeted_amount) * 100
```

## Financial Reporting Templates

### Variance Report

```text
├── Budget Item: ________________________
├── Allotment: ₱_________
├── Obligation: ₱_________
├── Disbursement: ₱_________
├── Variance: ₱_________ ( ___% )
├── Reason: ___________________________
└── Corrective Action: ________________
```

### Fund Status Report

```text
├── Fund Name: ________________________
├── Beginning Balance: ₱___________
├── Add: Receipts/Allotments: ₱____
├── Less: Disbursements: ₱_________
├── Ending Balance: ₱______________
├── Obligated (Unpaid): ₱__________
└── Available Balance: ₱___________
```

## Required Government Reports

| Report | Frequency | Due Date |
|--------|-----------|----------|
| Statement of Appropriations, Allotments, Obligations | Monthly | 10th of following month |
| Statement of Cash Flows | Monthly | 10th of following month |
| Trial Balance | Monthly | 15th of following month |
| Financial Statements | Quarterly/Annual | Per COA schedule |
| Budget Utilization Report | Quarterly | End of quarter |
