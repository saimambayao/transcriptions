---
name: explainer
description: Knowledge expert for Bangsamoro Development Platform tech stack, architecture, design, development, and administration. Provides tutorials, explanations, and helps users understand how the platform was architected, designed, developed, and maintained. Use when asking "how does X work", "explain Y", "teach me about Z", or seeking to understand patterns, conventions, and best practices across the codebase.
argument-hint: "[concept to explain]"
---

# Explainer - Bangsamoro Development Platform

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's explanation request                      ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

## Overview

Explainer is the comprehensive knowledge expert for the CSEA (Cooperative and Social Enterprise Authority) Digital Platform. It serves as an educational resource, providing detailed explanations, tutorials, and insights into CSEA's architecture, tech stack, design patterns, development workflows, and maintenance procedures.

**Core Purpose**: Help users (developers, administrators, maintainers) understand CSEA deeply so they can work with it effectively.

## When to Use This Skill

Invoke Explainer when:
- **Learning CSEA**: "How does CSEA's three-portal architecture work?"
- **Understanding Architecture**: "Explain the CSEA app structure"
- **Tech Stack Questions**: "What's the role of TanStack Query in CSEA?"
- **Design Patterns**: "Why does CSEA use Django Ninja?"
- **Development Workflows**: "How do I add a new feature to CSEA?"
- **Administration**: "How do I manage cooperatives in CSEA?"
- **Conventions**: "What are CSEA naming conventions?"
- **Tutorial Requests**: "Tutorial: Build a new CSEA component"
- **Comparison Questions**: "Why Next.js instead of plain React?"
- **Troubleshooting**: "Why am I seeing other organizations' data?"

**Keywords**: "explain", "how does", "why", "tutorial", "teach me", "show me", "what is", "understanding", "learn"

## Core Capabilities

### 1. Architecture Explanation

**High-Level Architecture**:
- Three-portal system design (Public, C/SE Portal, CSEA Staff)
- Next.js App Router structure with route groups
- Django Ninja API backend
- PostgreSQL database
- Railway deployment

**Three-Portal System**:
```
Bangsamoro Development Platform
├── Public Portal (/)
│   ├── Marketplace (products from all coops/SEs)
│   ├── Cooperative Directory
│   ├── Social Enterprise Directory
│   └── Individual Storefronts
│
├── C/SE Portal (/portal)
│   ├── Dashboard
│   ├── Profile Management
│   ├── Compliance Tracking
│   ├── Shop Management
│   └── Member Management
│
└── CSEA Staff Portal (/csea)
    ├── Registration Oversight
    ├── Compliance Monitoring
    ├── Analytics & Reporting
    └── User Management
```

**Route Groups**:
```
frontend/src/app/
├── (public)/           # Public marketplace routes
├── (tenant)/           # C/SE portal routes (authenticated)
├── (admin)/            # CSEA staff routes (admin)
├── (coop)/             # Cooperative storefronts
│   └── coop/[shortname]/
└── (se)/               # Social enterprise storefronts
    └── se/[shortname]/
```

### 2. Tech Stack Expertise

**Frontend Stack**:
| Technology | Purpose |
|------------|---------|
| Next.js 16+ | React framework with App Router |
| React 19+ | UI component library |
| TypeScript | Type safety |
| TanStack Query | Data fetching and caching |
| Tailwind CSS v4 | Utility-first styling |
| shadcn/ui | Pre-built UI components |

**Backend Stack**:
| Technology | Purpose |
|------------|---------|
| Django 6.0 | Python web framework |
| Django Ninja | Fast API framework (Pydantic) |
| PostgreSQL 18 | Relational database |

**Why These Choices**:
- **Next.js over React SPA**: SSR, App Router, file-based routing
- **Django Ninja over DRF**: Faster, Pydantic schemas, modern Python
- **TanStack Query over Redux**: Built for data fetching, simpler patterns
- **shadcn/ui over Material UI**: Customizable, Tailwind-based, lightweight

### 3. Design Pattern Education

**Frontend Patterns**:

**TanStack Query Pattern**:
```typescript
// Hook for fetching data
export function useCooperatives() {
  return useQuery({
    queryKey: ['cooperatives'],
    queryFn: getCooperatives,
  });
}

// Using in component
function CooperativeList() {
  const { data, isLoading, error } = useCooperatives();

  if (isLoading) return <Skeleton />;
  if (error) return <ErrorDisplay error={error} />;

  return data.map(coop => <CooperativeCard key={coop.id} coop={coop} />);
}
```

**Service Layer Pattern**:
```typescript
// lib/services/cooperatives.service.ts
export async function getCooperatives(): Promise<Cooperative[]> {
  const response = await apiClient.get('/api/cooperatives/');
  return response.data;
}

export async function createCooperative(data: CreateCooperativeInput) {
  const response = await apiClient.post('/api/cooperatives/', data);
  return response.data;
}
```

**Type-First Pattern**:
```typescript
// lib/types/cooperative.ts
export interface Cooperative {
  id: string;
  name: string;
  shortname: string;
  status: 'pending' | 'active' | 'suspended';
  organization_id: string;
}

export interface CreateCooperativeInput {
  name: string;
  registration_number: string;
}
```

**Backend Patterns**:

**Django Ninja Router Pattern**:
```python
# apps/cooperatives/api.py
from ninja import Router, Schema
from .models import Cooperative
from .schemas import CooperativeOut, CooperativeIn

router = Router()

@router.get('/', response=list[CooperativeOut])
def list_cooperatives(request):
    return Cooperative.objects.filter(
        organization=request.auth.organization
    )

@router.post('/', response=CooperativeOut)
def create_cooperative(request, payload: CooperativeIn):
    return Cooperative.objects.create(
        **payload.dict(),
        organization=request.auth.organization
    )
```

**Pydantic Schema Pattern**:
```python
# apps/cooperatives/schemas.py
from ninja import Schema
from datetime import datetime

class CooperativeOut(Schema):
    id: int
    name: str
    shortname: str
    status: str
    created_at: datetime

class CooperativeIn(Schema):
    name: str
    registration_number: str
```

### 4. Development Workflow Guidance

**Adding a New Feature (Frontend-First)**:

```
Step 1: Define Types
frontend/src/lib/types/feature.ts

Step 2: Create Mock Data
frontend/src/lib/mock/feature.ts

Step 3: Create Service
frontend/src/lib/services/feature.service.ts

Step 4: Create Hook
frontend/src/lib/hooks/useFeature.ts

Step 5: Create Components
frontend/src/components/feature/FeatureCard.tsx

Step 6: Create Page
frontend/src/app/(tenant)/portal/feature/page.tsx

Step 7: Test with Mock Data
npm run dev → verify UI works

Step 8: Create Backend API (when ready)
backend/apps/feature/api.py
backend/apps/feature/schemas.py

Step 9: Connect Frontend to Backend
Update service to call real API
```

**Creating a New Component**:
```typescript
// components/feature/FeatureCard.tsx
'use client';

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Feature } from '@/lib/types/feature';

interface FeatureCardProps {
  feature: Feature;
  onSelect?: (feature: Feature) => void;
}

export function FeatureCard({ feature, onSelect }: FeatureCardProps) {
  return (
    <Card
      className="cursor-pointer hover:border-negosyo-blue transition-colors"
      onClick={() => onSelect?.(feature)}
    >
      <CardHeader>
        <CardTitle>{feature.name}</CardTitle>
      </CardHeader>
      <CardContent>
        <p className="text-muted-foreground">{feature.description}</p>
      </CardContent>
    </Card>
  );
}
```

### 5. Multi-Tenant Architecture

**Concepts**:
- **Organization**: Primary tenant entity
- **User-Organization Relationship**: Each user belongs to one organization
- **Data Isolation**: All data is scoped to an organization

**Frontend Multi-Tenant Pattern**:
```typescript
// Context provides organization
const { organization } = useAuth();

// API calls include organization context
const { data } = useQuery({
  queryKey: ['cooperatives', organization.id],
  queryFn: () => getCooperatives(organization.id),
});
```

**Backend Multi-Tenant Pattern**:
```python
# Always filter by organization
@router.get('/cooperatives')
def list_cooperatives(request):
    return Cooperative.objects.filter(
        organization=request.auth.organization
    )

# Include organization on create
@router.post('/cooperatives')
def create_cooperative(request, payload: CooperativeIn):
    return Cooperative.objects.create(
        **payload.dict(),
        organization=request.auth.organization
    )
```

### 6. Common Conventions

**File Organization**:
```
frontend/src/
├── app/                    # Next.js pages (route groups)
├── components/
│   ├── ui/                 # shadcn/ui components
│   ├── landing/            # Public landing components
│   ├── cooperatives/       # Cooperative-specific
│   └── social-enterprises/ # SE-specific
├── lib/
│   ├── api/                # API client config
│   ├── hooks/              # Custom hooks
│   ├── services/           # API service functions
│   ├── types/              # TypeScript interfaces
│   ├── mock/               # Mock data
│   └── validations/        # Zod schemas
└── contexts/               # React contexts
```

**Naming Conventions**:
- **Components**: PascalCase (`CooperativeCard.tsx`)
- **Hooks**: camelCase with `use` prefix (`useCooperatives.ts`)
- **Services**: camelCase with `.service` suffix (`cooperatives.service.ts`)
- **Types**: PascalCase interfaces (`Cooperative`)
- **Routes**: kebab-case (`/social-enterprises`)

**Color Standards**:
- Primary: Negosyo Blue (`#0056D2`)
- Secondary Green: (`#008000`)
- No purple colors
- Use icons instead of emojis

**File Size**:
- Keep files under 1000 lines
- Split large components
- Extract reusable logic to hooks

## Explanation Patterns

### Pattern 1: Conceptual

**User**: "What is the three-portal architecture?"

**Explainer**: Explains concept, components, and purpose clearly.

### Pattern 2: Code-Focused

**User**: "How do I fetch data with TanStack Query?"

**Explainer**: Provides code examples with explanations.

### Pattern 3: Comparative

**User**: "Why Django Ninja instead of DRF?"

**Explainer**: Comparison table with pros/cons.

### Pattern 4: Tutorial-Style

**User**: "Tutorial: Create a CRUD feature"

**Explainer**: Step-by-step guide with code at each step.

### Pattern 5: Troubleshooting

**User**: "Why is my component not re-rendering?"

**Explainer**: Common causes and solutions.

## Integration with Other Skills

| When User Needs | Use Explainer + | For |
|-----------------|----------------|-----|
| Learn before implementing | Explainer → featuredev | Understand pattern, then build |
| Understand error | Explainer + investigator | Explain why error occurred |
| Architecture decision | Explainer → architect | Understand current, then plan |
| Tutorial for new team member | Explainer (standalone) | Onboarding education |
| Clarify CSEA pattern | Explainer (standalone) | Pattern explanation |

---

## Workflow: Explaining Cooperatives

See [explaining-cooperatives.md](references/explaining-cooperatives.md) for detailed cooperative concept explanations, governance, finance, membership, and audience-specific communication guides.

