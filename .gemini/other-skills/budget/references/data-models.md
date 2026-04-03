# Budget Data Models Reference

> Extracted from `/budget` SKILL.md for detailed reference.

## Budget Model

```python
class Budget(BaseModel):
    """Annual budget for a ministry or agency."""

    tenant = models.ForeignKey('tenants.Tenant', on_delete=models.CASCADE)
    fiscal_year = models.ForeignKey('FiscalYear', on_delete=models.PROTECT)
    ministry = models.ForeignKey('ministerial.Ministry', on_delete=models.CASCADE)

    # Budget amounts (in Philippine Peso)
    proposed_amount = models.DecimalField(max_digits=15, decimal_places=2)
    approved_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True)

    status = models.CharField(max_length=20, choices=[
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('enacted', 'Enacted'),
    ], default='draft')

    class Meta:
        unique_together = ['fiscal_year', 'ministry']
```

## Appropriation Model

```python
class Appropriation(BaseModel):
    """Legal authority to spend funds."""

    budget = models.ForeignKey('Budget', on_delete=models.CASCADE)
    expense_class = models.CharField(max_length=10, choices=[
        ('PS', 'Personnel Services'),
        ('MOOE', 'Maintenance and Other Operating Expenses'),
        ('CO', 'Capital Outlay'),
        ('FE', 'Financial Expenses'),
    ])

    amount = models.DecimalField(max_digits=15, decimal_places=2)
    released_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    obligated_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    disbursed_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    @property
    def available_balance(self):
        return self.amount - self.obligated_amount
```

## Obligation Model

```python
class Obligation(BaseModel):
    """Committed expenditure against appropriation."""

    appropriation = models.ForeignKey('Appropriation', on_delete=models.CASCADE)
    obligation_number = models.CharField(max_length=50, unique=True)
    payee = models.CharField(max_length=255)
    particulars = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('certified', 'Certified'),
        ('approved', 'Approved'),
        ('disbursed', 'Disbursed'),
        ('cancelled', 'Cancelled'),
    ], default='pending')

    obligation_date = models.DateField()
```
