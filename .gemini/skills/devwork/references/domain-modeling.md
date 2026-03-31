# Domain Modeling for Features

Analyze and model the problem domain before coding.

## User Story Format

```
As a [user role]
I want to [action/goal]
So that [business value/benefit]
```

## Domain Analysis Questions

**Entities:** What are the key concepts/nouns?

**Relationships:** How do entities relate?
- One-to-many, many-to-many, belongs-to
- Ownership and scoping (multi-tenant, org-scoped, user-scoped)

**Actions:** What verbs/behaviors exist?
- CRUD operations, status transitions, approvals, notifications

**Rules:** What business constraints apply?
- Who can perform which actions?
- What validations must be enforced?
- What state transitions are valid?

## Entity Relationship Sketch

```
[Root Entity] (scope boundary)
  +-- [Child Entity] (inherits scope)
  |     +-- [Grandchild] (further scoped)
  |           +-- created_by (User)
  |           +-- status (enum)
  +-- [Users] (members with roles)
```

## Field Design Template

| Field | Type | Required | Default | Validation |
|-------|------|----------|---------|------------|
| name | string | Yes | - | Min 1, max 255 |
| status | enum | Yes | 'draft' | Valid enum value |
| amount | decimal | Yes | - | > 0 |
| reviewed_by | FK(User) | No | NULL | Cannot be created_by |

## Permission Matrix Template

| Role | Create | View Own | View All | Approve | Delete |
|------|--------|----------|----------|---------|--------|
| User | Y | Y | N | N | Own only |
| Manager | Y | Y | Scoped | N | Own only |
| Admin | Y | Y | Scoped | Y | Any in scope |

## Data Flow Diagram

```
User action --> Validate input/permissions --> Save to DB
                                                 |
Admin views <-- Filter by scope + status    <-- Trigger notification
    |
Admin acts --> Update status + timestamp --> Audit log --> Notify user
```

## Output: Feature Specification

```markdown
# Feature: [Name]

## User Story
As a [role], I want to [goal] so that [benefit].

## Domain Model
- [Entity] model (scoped, audited)
- Relationships: [Parent] (1:N), [User] (approver)
- Status workflow: draft -> pending -> approved/rejected

## Business Rules
1. [Rule 1]
2. [Rule 2]

## Permissions
- create_[entity]: [who]
- view_[entity]: [who]
- approve_[entity]: [who]
- delete_[entity]: [who]

## UI Requirements
- List page with filters
- Create/edit form (full page)
- Detail view with status
- Delete confirmation (modal)

## Testing Requirements
- Model: constraints, validation
- API: CRUD endpoints, permissions
- UI: form submission, workflow
```
