---
name: devwork
description: Stack-agnostic feature development workflow using Frontend-First Development. Triggers when the user wants to implement a new feature, build a user story, develop full-stack functionality, create architecture documentation, or plan a module. Works with any frontend framework (React, Next.js, Vue, Svelte) and any backend framework (Django REST, Django Ninja, FastAPI, Express, Rails). Guides the developer through UI-first planning, API contract definition, backend implementation, testing, and deployment. IMPORTANT -- this skill requires /prompter invocation first; it invokes /prompter immediately upon activation.
argument-hint: "[feature to implement]"
---

# Feature Development (Stack-Agnostic)

## Gate: Invoke /prompter First

Before proceeding with any workflow:
1. INVOKE /prompter with the user's feature development request
2. WAIT for /prompter to complete its 5-phase workflow
3. WAIT for user confirmation ("Yes, proceed")
4. ONLY THEN return here and continue below

If user says "No" or "Adjust" -- repeat /prompter.
If user says "Let me rephrase" -- restart with new input.

---

Frontend-first feature development workflow. Works with any tech stack.

## Core Principle

**Build the UI first with mock data, define the API contract, then implement the backend.**

This ensures the frontend drives the API shape (not the other way around), catches UX issues early, and allows parallel frontend/backend work once the contract is locked.

## When to Use

- Implementing new user-facing features
- Building full-stack functionality (pages + API + database)
- Developing CRUD operations with data fetching
- Creating features requiring database schema changes
- Building features with authentication/authorization

## Stack Detection

At the start of each session, detect the project's stack by reading its config files (package.json, requirements.txt, pyproject.toml, go.mod, Gemfile, etc.). Adapt all phases below to the detected stack. If ambiguous, ask the user.

**Common frontend stacks:** React + Vite, Next.js (App/Pages Router), Vue + Nuxt, Svelte + SvelteKit, Angular
**Common backend stacks:** Django REST Framework, Django Ninja, FastAPI, Express, NestJS, Rails, Go/Gin
**Common data fetching:** TanStack Query, SWR, Apollo, built-in fetch/axios
**Common state management:** Zustand, Pinia, Redux, Jotai, built-in context
**Common styling:** Tailwind CSS, CSS Modules, styled-components, UnoCSS

## 5-Phase Development Workflow

```
/prompter --> Phase 1 (Frontend + Mock) --> Phase 2 (Backend + DB) --> Phase 3 (Integration) --> Phase 4 (Testing) --> Phase 5 (Deployment)
```

| Phase | Focus | Quality Gate | Deliverables |
|-------|-------|--------------|--------------|
| **1. Frontend + Mock** | UI with mock data | Build passes (lint, types, build) | Components, types, mock services, frontend tests |
| **2. Backend + Database** | Models, API, migrations | Migrations apply cleanly | Models, serializers/schemas, endpoints, backend tests |
| **3. Integration** | Connect frontend to backend | API contract match | Working full-stack feature |
| **4. Testing** | Verify requirements met | All tests pass | Code fixes, verified acceptance criteria |
| **5. Deployment** | Ship it | CI/CD passes | Merged PR, deployed feature |

---

## Phase 1: Frontend Implementation

**Define the feature first** with user story, components needed, acceptance criteria, and test scenarios.

### Feature Definition Template

```markdown
## Feature: [Name]

### User Story
As a [user type], I want to [action] so that [benefit].

### Components Needed
- [ ] Pages: [list routes]
- [ ] Components: [list components]
- [ ] API Endpoints: [list endpoints]
- [ ] Database Models: [list models]

### Acceptance Criteria
1. [Criterion 1]
2. [Criterion 2]
```

### Frontend Build Sequence

Build in this order -- each step feeds the next:

1. **Types** -- Define TypeScript/type interfaces for the feature's data
2. **Mock Data** -- Create realistic fake data matching those types
3. **Service Layer** -- Functions that return mock data (will swap to real API later)
4. **Data Hooks** -- Query/mutation hooks using TanStack Query, SWR, or framework equivalent
5. **Components** -- UI components consuming the hooks
6. **Pages/Views** -- Page-level components composing the smaller components
7. **Routes** -- Register routes in the framework's router

For code templates adapted to the current project's stack, see [references/component-templates.md](references/component-templates.md).

### Phase 1 Quality Gate

After frontend implementation, verify:
- [ ] No type errors
- [ ] No linter errors
- [ ] Build completes successfully
- [ ] Frontend unit tests pass

---

## Phase 2: Backend Implementation

**After the frontend works with mock data:**

Build in this order:

1. **Data Model** -- Create the database model/schema matching the TypeScript types
2. **Migration** -- Generate and apply database migration
3. **Serializer/Schema** -- Define input/output serialization (DRF Serializer, Ninja Schema, Pydantic model, Zod, etc.)
4. **Endpoint/View** -- Implement CRUD API endpoints
5. **Route Registration** -- Register the endpoint in the API router

For code templates, see [references/component-templates.md](references/component-templates.md).

### Phase 2 Quality Gate

After backend implementation, verify:
- [ ] Migrations generated and apply without errors
- [ ] No migration dependency issues
- [ ] Backend unit tests pass

---

## Phase 3: Integration

Update the service layer to replace mock data with real API calls. The key checkpoint: **TypeScript types must match API responses exactly.**

### Phase 3 Verification

- [ ] API calls return expected data
- [ ] Frontend types match API response shape
- [ ] Multi-tenancy / scoping is enforced (if applicable)
- [ ] CRUD operations work end-to-end

---

## Phase 4: Testing

> **Tests verify REQUIREMENTS, not just code behavior.**

When tests fail:
1. **Understand WHY** -- Is the test wrong or the code wrong?
2. **Check requirements** -- What does the acceptance criteria say?
3. **Fix the code** -- Make it meet requirements, not just pass tests
4. **Never bypass tests** -- If a test is wrong, fix the test properly

### Test Categories

| Type | Purpose | When to Run |
|------|---------|-------------|
| **Unit (Frontend)** | Component behavior, hooks, utils | Phase 1 |
| **Unit (Backend)** | Models, serializers, views | Phase 2 |
| **Integration** | API contracts, data flow | Phase 3 |
| **E2E** | User workflows, acceptance criteria | Phase 4 |

---

## Phase 5: Deployment

### Pre-Deployment Checklist

- [ ] All tests pass (Phase 4 complete)
- [ ] Build passes
- [ ] Migrations ready and tested
- [ ] Code reviewed

### Ship

Commit, push to feature branch, create PR, merge after review. Use `/gitops` if available.

---

## Common Feature Patterns

### CRUD Feature

**Frontend structure (generic):**
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
/[domain]/new       --> Create (full page, NOT modal)
/[domain]/:id       --> Detail
/[domain]/:id/edit  --> Edit (full page, NOT modal)
```

**Hooks (TanStack Query pattern):**
- `useItems()` -- List query
- `useItem(id)` -- Single item query
- `useCreateItem()` / `useUpdateItem()` / `useDeleteItem()` -- Mutations

### Dashboard Feature

Stat cards, charts, recent activity lists. Use a single query hook for aggregated stats.

### Form Feature

Use the framework's form library (React Hook Form, Formik, VeeValidate, etc.) with schema validation (Zod, Yup, Valibot).

For full pattern details, see [references/feature-patterns.md](references/feature-patterns.md).

---

## Interaction Patterns

**Golden Rule: If it has an input field, it should NOT be a modal.**

| Pattern | USE FOR | NEVER USE FOR |
|---------|---------|---------------|
| **Modal/Dialog** | Delete confirmations, logout prompts | Forms, editing, creation |
| **Inline Editing** | Single-field updates (click-to-edit) | Multi-field forms |
| **Full-Page** | All forms, creation, editing flows | Simple confirmations |

**Create/Edit = Full Page. Delete = Modal Confirmation.**

---

## Architecture Documentation

Architecture docs follow a hierarchical inheritance model (Module --> Submodule --> Feature). Create them BEFORE implementation for new modules, major features, or cross-module integrations.

**Naming convention:**
- `arch-[module-name].md` -- Module architecture (shared patterns)
- `arch-[submodule-name].md` -- Submodule architecture (entities)
- `feat-[feature-name].md` -- Feature architecture (delta changes)

For the complete workflow, templates, and quality checklists, see [references/architecture-documentation.md](references/architecture-documentation.md).
For domain modeling guidance, see [references/domain-modeling.md](references/domain-modeling.md).

---

## Anti-Patterns

**Don't:** Skip frontend-first approach, skip type definitions, create components without mock data, deploy without testing, use modals for forms, hardcode tenant/org IDs.

**Do:** Start with UI and mock data, create proper type interfaces, use data-fetching hooks for server state, test before deploying, keep files under 1000 lines, use full-page routes for forms.

---

## Integration with Other Skills

| Skill | When | Purpose |
|-------|------|---------|
| **`/prompter`** | Before Phase 1 | Clarify feature requirements |
| **`/build`** | After Phase 1 | Verify frontend builds |
| **`/database`** | After Phase 2 | Verify migrations and schema |
| **`/gitops`** | Phase 5 | Commit, push, merge |
| **`/debugger`** | Any phase | Fix implementation issues |
| **`/coditor`** | Before Phase 5 | Audit code quality |

### Skill Invocation Order

```
/prompter -> Phase 1 -> /build -> Phase 2 -> /database -> Phase 3 -> Phase 4 -> /gitops
```
