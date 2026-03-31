# Common Feature Patterns

> Reusable patterns for common feature types -- stack-agnostic.

## CRUD Feature (List + Create + Edit + Delete)

**Frontend structure:**
```
features/[domain]/
  ListPage
  DetailPage
  CreatePage
  EditPage
  components/
    DataTable
    Form
```

**Route pattern:**
```
/[domain]           --> List
/[domain]/new       --> Create (full page)
/[domain]/:id       --> Detail
/[domain]/:id/edit  --> Edit (full page)
```

**Hooks:**
- `useItems()` -- List query
- `useItem(id)` -- Single item query
- `useCreateItem()` -- Create mutation
- `useUpdateItem()` -- Update mutation
- `useDeleteItem()` -- Delete mutation

## Dashboard Feature

**Components:**
- Stat cards
- Charts (Recharts, Chart.js, or framework equivalent)
- Recent activity lists

**Pattern:**
```typescript
const { data: stats } = useQuery({
  queryKey: ['dashboard-stats'],
  queryFn: getDashboardStats,
});
```

## Form Feature

**Use form library + schema validation:**

```typescript
// React Hook Form + Zod example
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

const schema = z.object({
  name: z.string().min(1, 'Required'),
  status: z.enum(['active', 'inactive']),
});

export function FeatureForm() {
  const form = useForm({
    resolver: zodResolver(schema),
  });
  // ...
}
```

## Interaction Rules

| Pattern | USE FOR | NEVER USE FOR |
|---------|---------|---------------|
| **Modal/Dialog** | Delete confirmations, logout prompts | Forms, editing, creation |
| **Inline Editing** | Single-field updates (click-to-edit) | Multi-field forms |
| **Full-Page** | All forms, creation, editing flows | Simple confirmations |
