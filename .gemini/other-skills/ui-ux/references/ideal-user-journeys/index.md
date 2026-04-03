# Ideal User Journeys - Bangsamoro Digital Platform

This directory contains comprehensive user journey and role documentation for both MoroNegosyo (e-commerce) and MoroAcademy (e-training) platforms.

## Purpose

These documents serve as:
1. **Development Guide** - Reference for building new features
2. **UX Design Reference** - Understand user needs and emotions at each stage
3. **Testing Basis** - Define acceptance criteria and test scenarios
4. **Prioritization Tool** - Identify gaps and improvement opportunities

---

## Document Structure

```
ideal-user-journeys/
├── index.md                          # This file
├── moronegosyo/
│   ├── journeys/                     # Journey-based documentation
│   │   ├── shopping.md               # Product discovery → checkout
│   │   ├── account.md                # Registration → profile management
│   │   ├── onboarding.md             # Consumer → tenant manager
│   │   ├── shop-management.md        # Product & storefront management
│   │   ├── order-fulfillment.md      # Order processing → delivery
│   │   └── compliance.md             # STEPS/PESOS compliance submission
│   └── roles/                        # Role-based documentation
│       ├── anonymous.md              # Unauthenticated visitor
│       ├── consumer.md               # Registered shopper
│       ├── coop-manager.md           # Cooperative manager (tenant)
│       ├── se-manager.md             # Social Enterprise manager (tenant)
│       └── csea-staff.md             # CSEA agency staff (admin)
└── moroacademy/
    ├── journeys/                     # Journey-based documentation
    │   ├── discovery.md              # Course browsing → enrollment
    │   ├── learning.md               # Course progress → completion
    │   ├── certification.md          # Assessment → certificate
    │   ├── course-creation.md        # Instructor content creation
    │   ├── workshop.md               # Workshop registration → attendance
    │   └── provider-setup.md         # Provider onboarding
    └── roles/                        # Role-based documentation
        ├── anonymous.md              # Unauthenticated visitor
        ├── learner.md                # Registered learner
        ├── instructor.md             # Course creator/facilitator
        ├── tsp-admin.md              # Training Service Provider admin
        ├── coop-training.md          # Cooperative training coordinator
        ├── se-training.md            # SE training coordinator
        └── csea-training.md          # CSEA training admin

```

---

## MoroNegosyo (E-Commerce Platform)

### User Journeys

| Journey | Description | Primary Persona |
|---------|-------------|-----------------|
| [Shopping](./moronegosyo/journeys/shopping.md) | Product discovery through checkout | Maria, 35, small business owner |
| [Account](./moronegosyo/journeys/account.md) | Registration and profile management | Juan, 28, first-time shopper |
| [Onboarding](./moronegosyo/journeys/onboarding.md) | Consumer to tenant manager transition | Rosa, 45, cooperative officer |
| [Shop Management](./moronegosyo/journeys/shop-management.md) | Product and storefront management | Pedro, 38, coop manager |
| [Order Fulfillment](./moronegosyo/journeys/order-fulfillment.md) | Order processing to delivery | Ana, 32, SE manager |
| [Compliance](./moronegosyo/journeys/compliance.md) | STEPS/PESOS submission workflow | Miguel, 50, coop treasurer |

### User Roles

| Role | Type | Portal Access | Key Capabilities |
|------|------|---------------|------------------|
| [Anonymous](./moronegosyo/roles/anonymous.md) | Unauthenticated | Public, Storefronts | Browse, search, guest checkout |
| [Consumer](./moronegosyo/roles/consumer.md) | Authenticated | Public, Storefronts | Purchase, reviews, wishlist, loyalty |
| [Coop Manager](./moronegosyo/roles/coop-manager.md) | Tenant | Tenant Portal | Shop, orders, members, compliance |
| [SE Manager](./moronegosyo/roles/se-manager.md) | Tenant | Tenant Portal | Shop, orders, impact tracking |
| [CSEA Staff](./moronegosyo/roles/csea-staff.md) | Admin | Agency Portal | Oversight, approvals, analytics |

---

## MoroAcademy (E-Training Platform)

### User Journeys

| Journey | Description | Primary Persona |
|---------|-------------|-----------------|
| [Discovery](./moroacademy/journeys/discovery.md) | Course browsing to enrollment | Fatima, 26, cooperative member |
| [Learning](./moroacademy/journeys/learning.md) | Course progress to completion | Ahmad, 32, cooperative treasurer |
| [Certification](./moroacademy/journeys/certification.md) | Assessment to certificate | Sarah, 29, SE founder |
| [Course Creation](./moroacademy/journeys/course-creation.md) | Instructor content creation | Dr. Hassan, 45, training consultant |
| [Workshop](./moroacademy/journeys/workshop.md) | Workshop registration to attendance | Aisha, 35, cooperative secretary |
| [Provider Setup](./moroacademy/journeys/provider-setup.md) | Provider onboarding workflow | BACOMSEDECO Training Office |

### User Roles

| Role | Type | Scope | Key Capabilities |
|------|------|-------|------------------|
| [Anonymous](./moroacademy/roles/anonymous.md) | Unauthenticated | Public | Browse courses, view providers |
| [Learner](./moroacademy/roles/learner.md) | Authenticated | Personal | Enroll, learn, certificates |
| [Instructor](./moroacademy/roles/instructor.md) | Provider | Provider-scoped | Create courses, facilitate workshops |
| [TSP Admin](./moroacademy/roles/tsp-admin.md) | Provider Admin | TSP-scoped | Manage TSP content, accreditation |
| [Coop Training](./moroacademy/roles/coop-training.md) | Provider | Coop-scoped | Peer training, member enrollment |
| [SE Training](./moroacademy/roles/se-training.md) | Provider | SE-scoped | Impact-aligned training |
| [CSEA Training](./moroacademy/roles/csea-training.md) | Platform Admin | Global | Platform oversight, all providers |

---

## Implementation Status Reference

For detailed implementation status of each feature, refer to:
- [MoroNegosyo User Journeys (Test Reference)](../../test/references/moronegosyo-user-journeys.md)
- [MoroAcademy User Journeys (Test Reference)](../../test/references/moroacademy-user-journeys.md)

These test reference documents include:
- ✅ Implemented features
- 🚧 Partially implemented features
- ❌ Not yet implemented features

---

## How to Use These Documents

### For Developers
1. Read the relevant journey before implementing a feature
2. Understand user emotions and pain points
3. Reference the implementation status tables
4. Follow the design requirements in each stage

### For Designers
1. Use personas as design reference
2. Consider emotions at each journey stage
3. Address identified pain points
4. Leverage improvement opportunities

### For Product Managers
1. Prioritize based on pain points and opportunities
2. Use success metrics for KPIs
3. Reference implementation status for roadmap
4. Align features with user goals

### For QA/Testing
1. Derive test cases from journey stages
2. Use success metrics as acceptance criteria
3. Test both happy path and pain point scenarios
4. Verify implementation status markers

---

## Document Template

Each journey document follows this structure:
- **Overview**: Brief journey description
- **Persona**: User profile with goals and context
- **Journey Map**: Stages with actions, touchpoints, emotions
- **Success Metrics**: Measurable outcomes
- **Implementation Status**: Feature tracking table
- **Recommendations**: Prioritized improvements

Each role document follows this structure:
- **Overview**: Role description and purpose
- **Role Definition**: Type, access, authentication
- **Capabilities**: Feature access matrix
- **Key Pages**: Portal pages with implementation status
- **Role Progression**: How users advance between roles
- **Pain Points & Opportunities**: Current issues and improvements
- **Success Metrics**: Role-specific KPIs

---

## Related Documentation

- **Test References**: `.gemini/skills/test/references/`
- **Architecture**: `docs/architecture/`
- **UI Components**: `frontend/src/components/`
- **API Schemas**: `backend/apps/*/schemas.py`

---

## Implementation Priority Matrix

This section provides a recommended build order across all journeys and roles, organized by development phases with dependencies noted.

### Priority Levels

| Level | Description | Timeframe |
|-------|-------------|-----------|
| **P0** | Critical Path - Must have for MVP | Phase 1 |
| **P1** | Core Features - Essential for launch | Phase 2 |
| **P2** | Enhanced Experience - Improves UX | Phase 3 |
| **P3** | Advanced Features - Nice to have | Phase 4 |

---

### Phase 1: Foundation (Weeks 1-8)

**Goal**: Establish core infrastructure and public-facing pages

| Priority | Platform | Component | Dependencies | Route Group |
|----------|----------|-----------|--------------|-------------|
| P0-1 | Shared | Authentication System | None | `(public)` |
| P0-2 | MoroNegosyo | Anonymous Role - Public Pages | Auth | `(public)` |
| P0-3 | MoroNegosyo | Shopping Journey - Browse & Search | Anonymous | `(public)` |
| P0-4 | MoroAcademy | Anonymous Role - Course Catalog | Auth | `(academy)` |
| P0-5 | MoroAcademy | Discovery Journey - Course Browsing | Anonymous | `(academy)` |
| P0-6 | MoroNegosyo | Consumer Role - Registration | Auth | `(public)` |
| P0-7 | MoroAcademy | Learner Role - Registration | Auth | `(academy)` |

**Key Deliverables**:
- Public marketplace homepage
- Product catalog with search/filters
- Course catalog with search/filters
- User registration and login
- Basic profile management

---

### Phase 2: Core User Flows (Weeks 9-16)

**Goal**: Complete primary user journeys for consumers and learners

| Priority | Platform | Component | Dependencies | Route Group |
|----------|----------|-----------|--------------|-------------|
| P1-1 | MoroNegosyo | Shopping Journey - Cart & Checkout | Consumer | `(public)` |
| P1-2 | MoroNegosyo | Account Journey - Profile & Orders | Consumer | `(public)` |
| P1-3 | MoroAcademy | Discovery Journey - Enrollment | Learner | `(academy)` |
| P1-4 | MoroAcademy | Learning Journey - Course Player | Enrollment | `(academy)` |
| P1-5 | MoroNegosyo | Consumer Role - Wishlist & Reviews | Cart | `(public)` |
| P1-6 | MoroAcademy | Learning Journey - Progress Tracking | Course Player | `(academy)` |
| P1-7 | MoroNegosyo | Storefront Pages | Products | `(coop)`, `(se)` |
| P1-8 | MoroAcademy | Certification Journey - Assessments | Progress | `(academy)` |

**Key Deliverables**:
- Complete shopping cart and checkout
- Course enrollment and player
- Progress tracking and assessments
- Individual storefronts
- Order history and tracking

---

### Phase 3: Tenant Management (Weeks 17-24)

**Goal**: Enable cooperative/SE managers and training providers

| Priority | Platform | Component | Dependencies | Route Group |
|----------|----------|-----------|--------------|-------------|
| P1-9 | MoroNegosyo | Onboarding Journey | Consumer | `(tenant)` |
| P1-10 | MoroNegosyo | Coop Manager Role - Dashboard | Onboarding | `(tenant)` |
| P1-11 | MoroNegosyo | SE Manager Role - Dashboard | Onboarding | `(tenant)` |
| P1-12 | MoroNegosyo | Shop Management Journey | Coop/SE Manager | `(tenant)` |
| P1-13 | MoroAcademy | Provider Setup Journey | Auth | `(academy)` |
| P1-14 | MoroAcademy | Instructor Role - Course Creation | Provider | `(academy)` |
| P1-15 | MoroAcademy | Course Creation Journey | Instructor | `(academy)` |
| P1-16 | MoroNegosyo | Order Fulfillment Journey | Shop Mgmt | `(tenant)` |

**Key Deliverables**:
- Tenant registration and onboarding
- Product and inventory management
- Order processing and fulfillment
- Course creation tools
- Instructor dashboards

---

### Phase 4: Compliance & Administration (Weeks 25-32)

**Goal**: Complete regulatory compliance and admin oversight

| Priority | Platform | Component | Dependencies | Route Group |
|----------|----------|-----------|--------------|-------------|
| P1-17 | MoroNegosyo | Compliance Journey - STEPS/PESOS | Coop/SE Manager | `(tenant)` |
| P1-18 | MoroNegosyo | CSEA Staff Role - Oversight | Compliance | `(admin)` |
| P1-19 | MoroAcademy | Workshop Journey | Instructor | `(academy)` |
| P1-20 | MoroAcademy | TSP Admin Role | Provider | `(academy)` |
| P1-21 | MoroAcademy | Coop Training Role | Provider | `(academy)` |
| P1-22 | MoroAcademy | SE Training Role | Provider | `(academy)` |
| P1-23 | MoroAcademy | CSEA Training Role - Platform Admin | All Providers | `(admin)` |
| P1-24 | MoroAcademy | Certification Journey - Certificates | Assessments | `(academy)` |

**Key Deliverables**:
- FRAMES compliance submission
- Registration approvals
- Workshop scheduling and attendance
- Certificate generation
- Platform-wide analytics

---

### Phase 5: Enhancement & Polish (Weeks 33-40)

**Goal**: Advanced features and UX improvements

| Priority | Platform | Component | Dependencies | Route Group |
|----------|----------|-----------|--------------|-------------|
| P2-1 | MoroNegosyo | Consumer Role - Loyalty Program | Orders | `(public)` |
| P2-2 | MoroNegosyo | Advanced Analytics | CSEA Staff | `(admin)` |
| P2-3 | MoroAcademy | Learning Paths | Courses | `(academy)` |
| P2-4 | MoroAcademy | Discussion Forums | Learner | `(academy)` |
| P2-5 | MoroNegosyo | Member Management | Coop Manager | `(tenant)` |
| P2-6 | MoroAcademy | Peer Learning Groups | Learner | `(academy)` |
| P3-1 | MoroNegosyo | AI Recommendations | Products | `(public)` |
| P3-2 | MoroAcademy | Skill Badges | Certificates | `(academy)` |

**Key Deliverables**:
- Loyalty and rewards system
- Advanced reporting dashboards
- Learning path recommendations
- Community features
- AI-powered suggestions

---

### Dependency Graph

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           FOUNDATION LAYER                                  │
│  ┌──────────────┐                                                           │
│  │    Auth      │──────────────────────────────────────────────────────────┐│
│  └──────┬───────┘                                                          ││
│         │                                                                  ││
│  ┌──────▼───────┐    ┌──────────────┐                                      ││
│  │   Anonymous  │────►   Consumer   │                                      ││
│  │   (Public)   │    │ (Registered) │                                      ││
│  └──────┬───────┘    └──────┬───────┘                                      ││
│         │                   │                                              ││
└─────────┼───────────────────┼──────────────────────────────────────────────┘│
          │                   │                                               │
┌─────────▼───────────────────▼──────────────────────────────────────────────┐│
│                           USER LAYER                                       ││
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                  ││
│  │   Shopping   │    │   Account    │    │  Storefronts │                  ││
│  │   Journey    │    │   Journey    │    │  (Coop/SE)   │                  ││
│  └──────┬───────┘    └──────┬───────┘    └──────────────┘                  ││
│         │                   │                                              ││
│         └─────────┬─────────┘                                              ││
│                   │                                                        ││
└───────────────────┼────────────────────────────────────────────────────────┘│
                    │                                                         │
┌───────────────────▼────────────────────────────────────────────────────────┐│
│                           TENANT LAYER                                     ││
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                  ││
│  │  Onboarding  │────►  Coop/SE     │────►    Shop      │                  ││
│  │   Journey    │    │  Manager     │    │  Management  │                  ││
│  └──────────────┘    └──────┬───────┘    └──────┬───────┘                  ││
│                             │                   │                          ││
│                      ┌──────▼───────┐    ┌──────▼───────┐                  ││
│                      │  Compliance  │    │    Order     │                  ││
│                      │   Journey    │    │ Fulfillment  │                  ││
│                      └──────────────┘    └──────────────┘                  ││
│                                                                            ││
└────────────────────────────────────────────────────────────────────────────┘│
                                                                              │
┌─────────────────────────────────────────────────────────────────────────────┤
│                           ADMIN LAYER                                       │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                  ││
│  │  CSEA Staff  │────►  Approvals   │────►  Analytics   │                  ││
│  │    Role      │    │  & Oversight │    │  & Reports   │                  ││
│  └──────────────┘    └──────────────┘    └──────────────┘                  ││
│                                                                            ││
└────────────────────────────────────────────────────────────────────────────┘│
                                                                              │
┌─────────────────────────────────────────────────────────────────────────────┤
│                        MOROACADEMY PARALLEL TRACK                           │
│                                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                  ││
│  │  Anonymous   │────►   Learner    │────►   Learning   │                  ││
│  │  (Catalog)   │    │   (Enroll)   │    │   Journey    │                  ││
│  └──────────────┘    └──────┬───────┘    └──────┬───────┘                  ││
│                             │                   │                          ││
│                      ┌──────▼───────┐    ┌──────▼───────┐                  ││
│                      │ Certification│    │  Workshops   │                  ││
│                      │   Journey    │    │   Journey    │                  ││
│                      └──────────────┘    └──────────────┘                  ││
│                                                                            ││
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                  ││
│  │  Provider    │────►  Instructor  │────►   Course     │                  ││
│  │   Setup      │    │    Role      │    │  Creation    │                  ││
│  └──────────────┘    └──────┬───────┘    └──────────────┘                  ││
│                             │                                              ││
│  ┌──────────────┐    ┌──────▼───────┐    ┌──────────────┐                  ││
│  │  TSP Admin   │    │ Coop/SE Train│    │ CSEA Training│                  ││
│  │    Role      │    │    Roles     │    │    Role      │                  ││
│  └──────────────┘    └──────────────┘    └──────────────┘                  ││
│                                                                            ││
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### Sprint Planning Guide

#### Sprint Structure (2-week sprints)

| Sprint | Phase | Focus Area | Primary Deliverables |
|--------|-------|------------|----------------------|
| 1-2 | 1 | Auth + Public Pages | Login, Registration, Homepage |
| 3-4 | 1 | Catalogs | Product Catalog, Course Catalog |
| 5-6 | 2 | Shopping | Cart, Checkout, Order Tracking |
| 7-8 | 2 | Learning | Enrollment, Course Player |
| 9-10 | 2 | Progress | Assessments, Progress Tracking |
| 11-12 | 3 | Onboarding | Tenant Registration, Dashboard |
| 13-14 | 3 | Shop Management | Products, Inventory, Storefront |
| 15-16 | 3 | Course Creation | Content Builder, Publishing |
| 17-18 | 3 | Orders | Fulfillment, Shipping, Tracking |
| 19-20 | 4 | Compliance | FRAMES, Document Upload |
| 21-22 | 4 | Workshops | Scheduling, Live Sessions |
| 23-24 | 4 | Certificates | Generation, Verification |
| 25-26 | 4 | Admin | Oversight, Approvals, Analytics |
| 27-28 | 5 | Enhancement | Loyalty, Learning Paths |
| 29-30 | 5 | Community | Forums, Peer Groups |
| 31-32 | 5 | AI Features | Recommendations, Badges |

---

### Cross-Platform Dependencies

| MoroNegosyo Component | MoroAcademy Component | Shared Dependency |
|-----------------------|-----------------------|-------------------|
| Consumer Registration | Learner Registration | Auth System |
| Coop/SE Manager | Provider Admin | Organization Model |
| CSEA Staff | CSEA Training | Admin Permissions |
| Product Catalog | Course Catalog | Search Infrastructure |
| Order System | Enrollment System | Transaction Processing |
| Compliance (FRAMES) | Provider Accreditation | Document Management |

---

### MVP Checklist

**MoroNegosyo MVP**:
- [ ] Public marketplace homepage
- [ ] Product catalog with search
- [ ] User registration/login
- [ ] Shopping cart
- [ ] Guest checkout
- [ ] Basic order tracking
- [ ] Cooperative directory
- [ ] Social enterprise directory

**MoroAcademy MVP**:
- [ ] Academy homepage
- [ ] Course catalog with search
- [ ] Learner registration
- [ ] Course enrollment
- [ ] Course player (video + text)
- [ ] Progress tracking
- [ ] Basic assessments
- [ ] Certificate generation

**Shared MVP**:
- [ ] Unified authentication
- [ ] Responsive design (mobile-first)
- [ ] Error handling and loading states
- [ ] Basic analytics tracking

---

### Risk Mitigation

| Risk | Impact | Mitigation Strategy |
|------|--------|---------------------|
| Auth delays | Blocks all features | Prioritize auth in Sprint 1 |
| Payment integration | Blocks checkout | Use mock payments, integrate later |
| Video hosting | Blocks course player | Use external hosting (YouTube/Vimeo) |
| Certificate generation | Blocks certification | Use PDF templates, automate later |
| Multi-tenant complexity | Delays tenant features | Start with single-tenant, add scoping |

---

*Last Updated: December 30, 2025*
