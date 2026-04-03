# Component & Code Templates

> Stack-agnostic templates for the 5-phase frontend-first workflow. Adapt paths and syntax to the project's actual framework.

## Phase 1: Frontend Build Sequence Templates

### 1. Types

```typescript
// types/feature.ts
export interface Feature {
  id: string;
  name: string;
  status: 'active' | 'inactive';
  createdAt: Date;
}

export interface CreateFeatureInput {
  name: string;
  status?: string;
}

export interface UpdateFeatureInput {
  name?: string;
  status?: string;
}
```

### 2. Mock Data

```typescript
// mock/feature.ts
import type { Feature } from '@/types/feature';

export const mockFeatures: Feature[] = [
  { id: '1', name: 'Feature 1', status: 'active', createdAt: new Date() },
  { id: '2', name: 'Feature 2', status: 'inactive', createdAt: new Date() },
];
```

### 3. Service Layer (Mock)

```typescript
// services/feature.service.ts
import { mockFeatures } from '@/mock/feature';
import type { Feature } from '@/types/feature';

export async function getFeatures(): Promise<Feature[]> {
  return mockFeatures;
  // Later: return apiClient.get('/api/features');
}

export async function getFeature(id: string): Promise<Feature> {
  return mockFeatures.find(f => f.id === id)!;
}
```

### 4. Data Hook (TanStack Query example)

```typescript
// hooks/useFeatures.ts
import { useQuery } from '@tanstack/react-query';
import { getFeatures } from '@/services/feature.service';

export function useFeatures() {
  return useQuery({
    queryKey: ['features'],
    queryFn: getFeatures,
  });
}
```

### 5. Component

```typescript
// components/features/FeatureCard.tsx
import type { Feature } from '@/types/feature';

interface FeatureCardProps {
  feature: Feature;
}

export function FeatureCard({ feature }: FeatureCardProps) {
  return (
    <div>
      <h3>{feature.name}</h3>
      <p>Status: {feature.status}</p>
    </div>
  );
}
```

### 6. Page

```typescript
// pages or app route for features list
import { useFeatures } from '@/hooks/useFeatures';
import { FeatureCard } from '@/components/features/FeatureCard';

export function FeaturesPage() {
  const { data: features, isLoading } = useFeatures();

  if (isLoading) return <div>Loading...</div>;

  return (
    <div>
      {features?.map((feature) => (
        <FeatureCard key={feature.id} feature={feature} />
      ))}
    </div>
  );
}
```

### 7. Route Registration

Adapt to your router (React Router, Next.js App Router, Vue Router, etc.):

```typescript
// React Router example
{ path: '/features', element: <FeaturesPage /> }
{ path: '/features/new', element: <FeatureCreatePage /> }
{ path: '/features/:id', element: <FeatureDetailPage /> }
{ path: '/features/:id/edit', element: <FeatureEditPage /> }
```

## Phase 2: Backend Templates

Adapt to your backend framework. The pattern is the same regardless of framework:

### 1. Data Model

Define model fields that mirror the TypeScript types from Phase 1.

### 2. Migration

Generate and apply using the framework's migration tool.

### 3. Serializer / Schema

Define input and output schemas. Ensure the output shape matches the frontend TypeScript types exactly.

### 4. Endpoint / View

Implement CRUD endpoints. Include scoping (filter by tenant/org/user) and permission checks.

### 5. Route Registration

Register the endpoint in the API router.

## Phase 3: Integration Template

**Swap mock for real API in the service layer:**

```typescript
// services/feature.service.ts (updated)
import { apiClient } from '@/lib/api/client';
import type { Feature, CreateFeatureInput, UpdateFeatureInput } from '@/types/feature';

export async function getFeatures(): Promise<Feature[]> {
  const response = await apiClient.get('/api/features/');
  return response.data;
}

export async function createFeature(data: CreateFeatureInput): Promise<Feature> {
  const response = await apiClient.post('/api/features/', data);
  return response.data;
}

export async function updateFeature(id: string, data: UpdateFeatureInput): Promise<Feature> {
  const response = await apiClient.patch(`/api/features/${id}/`, data);
  return response.data;
}

export async function deleteFeature(id: string): Promise<void> {
  await apiClient.delete(`/api/features/${id}/`);
}
```

The key insight: only the **service layer** changes. Hooks, components, and pages remain untouched.
