# Architecture Documentation Workflow

> Reference for architecture document creation -- stack-agnostic.

When designing new modules or major features, create architecture documentation BEFORE implementation.

## When to Create Architecture Documents

- New module implementation
- Major feature additions requiring data models, APIs, and workflows
- Cross-module integrations
- System redesigns or refactoring

## Architecture Document Templates

Architecture documentation follows a hierarchical inheritance model.

| Level | File Pattern | Purpose |
|-------|-------------|---------|
| **Module** | `arch-[module-name].md` | Shared patterns (State, Error, Security, Performance) |
| **Submodule** | `arch-[submodule-name].md` | Entity definitions (Types, CRUD, API, Models) |
| **Feature** | `feat-[feature-name].md` | Delta-only changes for user stories |

## Architecture Document Structure (Hierarchical)

**Module Level** (Shared Patterns -- inherited by all children):

| Section | Purpose |
|---------|---------|
| Module Overview | Purpose, users, business alignment |
| Submodule Registry | List of submodules |
| State Management | Data fetching, client state, URL state patterns |
| Error Handling | Error types, boundaries, handlers |
| Security Architecture | Auth, roles, scoping |
| Performance Requirements | Load targets, budgets |
| Notification System | Toast, in-app, email patterns |
| Audit Trail | Audit model, compliance tracking |

**Submodule Level** (Entity-Specific -- references parent patterns):

| Section | Purpose |
|---------|---------|
| User Workflows | State diagrams, user journeys |
| Frontend Architecture | Pages, components, routes |
| Type Definitions | Entity interfaces, enums |
| CRUD Implementation | Mock services, hooks |
| API Endpoints | REST/GraphQL endpoints |
| Data Models | Database models, serializers |

**Feature Level** (Delta-Only -- references parent entities):

| Section | Purpose |
|---------|---------|
| Acceptance Criteria | Testable requirements |
| UI Changes | New/modified components |
| Type Changes | New/modified interfaces |
| API Changes | New/modified endpoints |
| Model Changes | New/modified fields |
| Test Cases | Tests from acceptance criteria |

## Architecture Document Workflow (Frontend-First)

**Phase 1: Research & Planning**
1. Identify the module scope and boundaries
2. Research business/legal requirements
3. Identify primary users and their roles

**Phase 2: User Experience Design**
1. Map user workflows with state diagrams
2. Define user journeys (action -> screen -> feedback)
3. Document approval workflows where needed

**Phase 3: Frontend Architecture**
1. Define page structure and routes
2. List required components per page
3. Specify form patterns (full-page, not modal)

**Phase 4: Type Contracts**
1. Define core entity types
2. Create input/output interfaces
3. Specify component props
4. Define filter and response types

**Phase 5: CRUD Implementation** (Makes UI Interactive)
1. Design mock service layer
2. Plan data-fetching hooks (queries + mutations)
3. Specify form implementation pattern
4. Define loading, success, and error feedback patterns
5. Document service switching (mock to API)

**Phase 6: API Design**
1. Define endpoints derived from frontend needs
2. Specify CRUD operations and custom actions
3. Document query parameters
4. Define response formats

**Phase 7: Data Modeling**
1. Create database models matching frontend types
2. Define relationships and constraints
3. Design scoping/multi-tenancy (if applicable)

## Architecture Document Location

Save architecture documents in a project-appropriate location:
```
docs/architecture/   OR   .claude/architecture/
|
+-- [module-name]/
    +-- arch-[module].md           # Module
    +-- arch-[submodule].md        # Submodule
    +-- feat-[feature].md          # Feature
```

## Architecture Document Quality Checklist

**Module Document:**
- [ ] Module overview states purpose and scope
- [ ] Submodule Registry lists all submodules
- [ ] State Management patterns documented
- [ ] Error Handling patterns documented
- [ ] Security Architecture defined
- [ ] Performance Requirements specified

**Submodule Document:**
- [ ] Inheritance declaration present (references module)
- [ ] Feature Registry lists all features
- [ ] User workflows have state diagrams
- [ ] Types defined for all entities
- [ ] CRUD implementation patterns specified
- [ ] API endpoints documented
- [ ] Data models include scoping

**Feature Document:**
- [ ] Parent module and submodule referenced
- [ ] User story clearly stated
- [ ] Acceptance criteria are testable
- [ ] All UI changes documented (delta)
- [ ] Type changes show exact additions
- [ ] API changes specify request/response
- [ ] Test cases cover all acceptance criteria
