# Budget Frontend Components Reference

> Extracted from `/budget` SKILL.md for detailed reference.

## Budget Dashboard Metrics

```typescript
interface BudgetMetrics {
  totalBudget: number;
  totalObligated: number;
  totalDisbursed: number;
  utilizationRate: number;  // (obligated / budget) * 100
  disbursementRate: number; // (disbursed / obligated) * 100
}
```

## Currency Display Component

```tsx
// components/CurrencyDisplay.tsx
export function CurrencyDisplay({ amount }: { amount: number }) {
  const formatted = new Intl.NumberFormat('en-PH', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
  }).format(amount);

  return (
    <span className="font-mono">
      <span className="text-muted-foreground">₱</span> {formatted}
    </span>
  );
}
```

## Currency Formatting (TypeScript)

```typescript
// Correct Philippine Peso formatting
formatCurrency(amount: number): string {
  return new Intl.NumberFormat('en-PH', {
    style: 'currency',
    currency: 'PHP',
    minimumFractionDigits: 2
  }).format(amount);
}
// Output: "₱1,234,567.89"
```

## Color Guidelines (e-Bangsamoro UI)

| Status | Color | Usage |
|--------|-------|-------|
| **On Track** | `emerald-600` | >80% utilization |
| **Warning** | `amber-500` | 60-80% utilization |
| **Critical** | `red-600` | <60% utilization |
| **Primary** | Blue-to-Emerald gradient | Headers, buttons |

*Note: Never use purple colors in UI elements.*
