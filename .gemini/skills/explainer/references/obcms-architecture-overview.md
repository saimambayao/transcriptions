# OBCMS Architecture Overview

**Purpose**: High-level overview of OBCMS system architecture, design principles, and component organization.

**Last Updated**: 2025-12-29

---

## BARMM Context (BDP 2023-2028)

This section provides essential context about the Bangsamoro Autonomous Region in Muslim Mindanao (BARMM), drawn from the 2nd Bangsamoro Development Plan 2023-2028. Understanding this context is critical for system design decisions.

### Vision

> "A Bangsamoro that is united, enlightened, self-governing, peaceful, just, morally upright, and progressive."

The Bangsamoro government envisions a territory devoid of all types of conflict - one that is permanently peaceful where residents enjoy security, comfort, and forward-thinking leadership.

### Mission

> "Guided by moral governance and in pursuit of genuine and meaningful autonomy, the Bangsamoro government ensures the necessary conditions for enduring peace and sustained socioeconomic development suitable to the systems of life, needs, and aspirations of its people by providing services to communities, ensuring multi-stakeholder participation, and facilitating appropriate partnership."

### Overall Goal

**An empowered, cohesive, and progressive Bangsamoro.**

| Term | Definition |
|------|------------|
| **Empowered** | Improved capacity of communities through better access to quality basic social services and expanded economic opportunities |
| **Cohesive** | Improved relationships between stakeholders evidenced by reduced violent conflict and forged partnerships in governance |
| **Progressive** | Sustained ability to optimize resources in addressing development needs and realizing economic and human potential |

### Six Development Goals (2023-2028)

| Goal | Description |
|------|-------------|
| **Goal 1** | Stable, just, and accountable government |
| **Goal 2** | Equitable, competitive, and robust economy |
| **Goal 3** | Peaceful, safe, and resilient Bangsamoro communities |
| **Goal 4** | Inclusive, responsive, and quality social services |
| **Goal 5** | Rich and diverse Bangsamoro culture and identity preserved and recognized |
| **Goal 6** | Strategic, adequate, and climate-resilient infrastructure |

### Development Strategies

1. Improve and strengthen governance mechanisms for a stable, just, and accountable Bangsamoro government
2. Create an enabling environment towards an equitable, competitive, and robust economy
3. Harness technology and innovations to increase socioeconomic opportunities and improve government services
4. Improve ecological integrity, resilience of communities, and ensure a healthy and clean environment
5. Enhance and strengthen peace, public order, safety, security, and uphold human rights
6. Ensure inclusive and equitable access to quality services for social justice and human capital development
7. Mainstream Bangsamoro cultural diversity, beliefs, heritage, and identity
8. Scale-up functional, strategic, climate-resilient, and quality infrastructure

### Pillars of Moral Governance

Moral Governance is the centerpiece of BARMM's leadership (2023-2028):

1. **Integrity** - Avoid conflicts of interest in official duties
2. **Accountability** - Transparency in all decisions and actions
3. **Transparency and Honesty** - Declare interests, protect public interest
4. **Sense of Patriotism** - Invest in heritage and protect reputation
5. **Striving for Excellence** - Uphold legitimacy, prioritize process
6. **Cultural Understanding and Tolerance** - Appreciate socioeconomic differences
7. **Unwavering Loyalty to God** - Follow rules and regulations
8. **Justice** - Serve without prejudice
9. **Inclusivity** - Foster welcoming, discrimination-free environments
10. **Objectivity** - Make merit-based decisions
11. **Dialogue and Meaningful Engagement** - Consult communities
12. **Balance Between Practical Life and Moral Side** - Balance practical and ethical values

### Macroeconomic Targets (2023-2028)

| Target | Baseline | End-of-Plan Target |
|--------|----------|-------------------|
| GRDP Annual Average Growth Rate | 7.5% (2020-2021) | 8%-9% |
| GRDP Per Capita Growth Rate | 6.4% (2020-2021) | 6%-9% |
| Industry & Services Growth | 7.9% / 6.6% | 10%-12% |
| Gross Capital Formation (% of GRDP) | 16.91% (2021) | 18%-20% |
| Inflation Rate | 2.40% (2021) | 2%-4% |
| Unemployment Rate | 3.80% (2021) | 3%-5% |
| Underemployment Rate | 9.0% (2020) | 4%-7% |
| Poverty Incidence | 29.80% (2021) | 20%-25% |

### BARMM Government Structure

**Planning Authority**: Bangsamoro Planning and Development Authority (BPDA) serves as the technical secretariat of the Bangsamoro Economic and Development Council (BEDC).

**Key Sectoral Committees**:
- Development Administration Committee (DACom)
- Economic Development Committee (EDCom)
- Social Development Committee (SDCom)
- Infrastructure Development Committee (IDCom)
- Peace, Public Order, Safety and Security Committee (PPOSSCom)

**Geographic Coverage**:
- 6 Provinces: Maguindanao del Norte, Maguindanao del Sur, Lanao del Sur, Basilan, Sulu, Tawi-Tawi
- 3 Cities: Marawi City, Lamitan City, Cotabato City
- Special Geographic Area (SGA)

### Alignment Framework

The 2nd BDP is aligned with:
- **National**: 8-Point Socioeconomic Agenda (Marcos Administration), PDP 2023-2028, AmBisyon Natin 2040
- **Regional**: Mindanao Development Agenda, BIMP-EAGA
- **International**: UN Sustainable Development Goals (SDGs)

---

## System Overview

**OBCMS** (Office for Other Bangsamoro Communities Management System) is a multi-tenant, multi-organizational Django web application designed for the Office of Bangsamoro Communities (OOBC) to manage OBC communities, conduct assessments (MANA), facilitate coordination, and support planning and budgeting.

### Key Characteristics

- **Multi-Tenant**: Multiple organizations use the same application instance with strict data isolation
- **Government System**: Built for government operations (compliance, audit trails, data privacy)
- **Django Monolith**: Single Django project with multiple apps (not microservices)
- **HTMX-Powered**: Dynamic interactions without full page reloads, server-rendered HTML
- **PostgreSQL**: Production database with advanced features (JSON fields, full-text search)

---

## Architecture Layers

### 1. **Presentation Layer** (Frontend)

**Technology**: Django Templates + HTMX + Alpine.js + Tailwind CSS

**Components**:
- **Django Templates**: Server-rendered HTML
- **HTMX**: Dynamic content updates via AJAX (no full page reloads)
- **Alpine.js**: Client-side state management (dropdowns, toggles)
- **Tailwind CSS**: Utility-first styling with OBCMS design system
- **Leaflet.js**: Interactive maps (barangay boundaries, community locations)
- **FullCalendar**: Scheduling and coordination meetings

**Pattern**: Progressive Enhancement
- Works without JavaScript (basic functionality)
- Enhanced with HTMX (dynamic updates)
- Further enhanced with Alpine.js (instant UI feedback)

### 2. **Application Layer** (Backend)

**Technology**: Django 5.2 + Django REST Framework

**Components**:
- **Django Views**: Business logic, request handling
- **DRF ViewSets**: API endpoints for frontend HTMX + external integrations
- **Middleware**: Authentication, RBAC, multi-tenant isolation
- **Forms**: Data validation, form processing

**Pattern**: Multi-Tenant MVC
- **Models**: Data layer with organization scoping
- **Views**: Business logic with permission checks
- **Templates**: Presentation layer (HTMX-powered)

### 3. **Data Layer** (Database)

**Technology**: PostgreSQL (production), SQLite (development)

**Schema Design**:
- **Organization-Scoped**: Every model has `organization` ForeignKey
- **Soft Deletes**: Records marked as deleted, not hard-deleted
- **Audit Trail**: `created_by`, `modified_by`, `created_at`, `modified_at` on all models
- **Geographic Data**: Province, Municipality, Barangay (shared across organizations)

**Access Pattern**: Organization-filtered queries
```python
# Always filter by organization
queryset = Model.objects.filter(organization=request.user.organization)
```

### 4. **Background Tasks Layer**

**Technology**: Celery + Redis

**Use Cases**:
- **Async Processing**: Long-running operations (report generation, data exports)
- **Scheduled Tasks**: Periodic jobs (data synchronization, cleanup)
- **Notifications**: Email/SMS notifications (coordination meetings, assessment reminders)

### 5. **AI Layer** (obcAI)

**Technology**: Google ADK (Agent Development Kit) + Gemini + Zhipu GLM 4.6

**Components**:
- **Coordinator**: Routes queries to specialist agents
- **Specialist Agents**: Domain-specific agents (Geographic, Community, MANA, Policy, etc.)
- **Function Tools**: Python functions wrapped for ADK (organization-scoped)
- **Django Integration**: obcAI accessible via Django views/APIs

**Pattern**: Multi-Agent System with Multi-Tenant Isolation

---

## Django Project Structure

```
obcms/
├── src/                          # Django source code
│   ├── obc_management/           # Django project (settings, URLs, WSGI)
│   │   ├── settings/
│   │   │   ├── base.py           # Base settings
│   │   │   ├── development.py    # Development settings
│   │   │   └── production.py     # Production settings (Railway)
│   │   ├── urls.py               # Root URL configuration
│   │   └── wsgi.py               # WSGI application
│   │
│   ├── common/                   # ⭐ Foundation app (shared across all modules)
│   │   ├── models.py             # BaseModel, Organization, User, Geography
│   │   ├── permissions.py        # RBAC permission decorators
│   │   ├── utils.py              # Shared utilities
│   │   └── middleware.py         # Custom middleware
│   │
│   ├── communities/              # OBC community management
│   │   ├── models.py             # Community, Household, Individual
│   │   ├── views.py              # Community CRUD, profiling
│   │   └── templates/            # Community UI
│   │
│   ├── mana/                     # Multi-sectoral needs assessment
│   │   ├── models.py             # Assessment, Indicator, Response
│   │   ├── views.py              # Assessment workflows
│   │   └── templates/            # Assessment forms, dashboards
│   │
│   ├── coordination/             # Multi-stakeholder coordination
│   │   ├── models.py             # Partnership, Meeting, Task
│   │   ├── views.py              # Coordination workflows
│   │   └── templates/            # Coordination UI
│   │
│   ├── planning/                 # Strategic planning
│   ├── budget_preparation/       # Budget preparation
│   ├── budget_execution/         # Budget execution monitoring
│   ├── ai_assistant/             # obcAI (Google ADK)
│   │
│   ├── templates/                # Shared templates
│   │   ├── base.html             # Base template (navigation, layout)
│   │   ├── common/               # Shared components
│   │   └── components/           # Reusable UI components
│   │
│   ├── static/                   # Static files (CSS, JS, images)
│   └── manage.py                 # Django management script
│
├── requirements/                 # Python dependencies
│   ├── base.txt                  # Base requirements
│   ├── development.txt           # Development requirements
│   └── production.txt            # Production requirements
│
├── docs/                         # Documentation
├── .claude/                      # Gemini CLI skills
└── railway.toml                  # Railway deployment config
```

---

## Core Apps

### `common` App (Foundation)

**Purpose**: Shared functionality across all OBCMS modules

**Models**:
- `BaseModel`: Abstract model with organization, audit fields, soft delete
- `Organization`: Multi-tenant primary entity
- `User`: Extended Django User with organization relationship
- `Province`, `Municipality`, `Barangay`: Geographic hierarchy (shared data)

**Utilities**:
- RBAC permission decorators
- Multi-tenant middleware
- Shared utilities (date formatting, number formatting, etc.)

### `communities` App

**Purpose**: OBC community management and profiling

**Key Features**:
- Community profiles (demographics, socioeconomic data)
- Household and individual records
- Community indicators
- Geographic mapping (Leaflet.js)

### `mana` App

**Purpose**: Multi-sectoral Needs Assessment and Analysis

**Key Features**:
- MANA assessment workflows (13 sectors)
- Indicator-based assessment
- Scoring and analysis
- Dashboard and reporting

### `coordination` App

**Purpose**: Multi-stakeholder partnership and coordination

**Key Features**:
- Partnership management (OOBC + partner ministries + LGUs)
- Coordination meetings (FullCalendar)
- Task management (kanban, list views)
- Resource booking

### `ai_assistant` App (obcAI)

**Purpose**: Google ADK-based multi-agent AI system

**Key Features**:
- Specialist agents (Geographic, Community, MANA, Policy, etc.)
- Coordinator routing
- Function tools (organization-scoped)
- Multi-tenant AI isolation

---

## Multi-Tenant Architecture

### Organization Model

```python
class Organization(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    organization_type = models.CharField(max_length=50)  # OOBC, Partner Ministry, LGU
    is_active = models.BooleanField(default=True)
```

### User-Organization Relationship

```python
class User(AbstractUser):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    # ... other fields
```

### Data Isolation Pattern

**Every model extends BaseModel**:
```python
class BaseModel(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='+')

    objects = ActiveManager()  # Excludes soft-deleted
    all_objects = models.Manager()  # Includes soft-deleted

    class Meta:
        abstract = True
```

**All queries filter by organization**:
```python
def list_communities(request):
    communities = Community.objects.filter(
        organization=request.user.organization
    )
    return render(request, 'communities/list.html', {'communities': communities})
```

---

## Security Architecture

### 1. **Multi-Tenant Data Isolation**

- Organization field on all models
- QuerySet filtering by organization
- Row-level security via Django ORM
- Middleware enforces organization context

### 2. **RBAC (Role-Based Access Control)**

```python
# Permission decorator
@permission_required('communities.view_community')
def view_community(request, pk):
    community = get_object_or_404(
        Community,
        pk=pk,
        organization=request.user.organization  # Multi-tenant check
    )
    return render(request, 'communities/detail.html', {'community': community})
```

### 3. **CSP (Content Security Policy)** - MANDATORY

**GEMINI.md Rule 12**: All code must be CSP-compliant

```python
# CSP middleware configuration
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "'nonce-{nonce}'", "'unsafe-eval'")  # unsafe-eval for Alpine.js
CSP_STYLE_SRC = ("'self'", "'nonce-{nonce}'")
```

**Template Pattern**:
```django
{# ✅ CORRECT: Script with nonce #}
<script nonce="{{ request.csp_nonce }}">
    console.log('CSP-compliant script');
</script>

{# ❌ WRONG: Inline script without nonce #}
<script>
    console.log('CSP violation!');
</script>
```

### 4. **Audit Trail**

- All models track: created_by, modified_by, created_at, modified_at
- Soft deletes preserve history
- Django admin logs all admin actions

---

## Deployment Architecture

### Railway Platform

**Services**:
- **Web**: Django application (Gunicorn WSGI server)
- **PostgreSQL**: Managed database
- **Redis**: Caching and Celery broker

**Environment Variables**:
```bash
DJANGO_SETTINGS_MODULE=obc_management.settings.production
DEBUG=False
ALLOWED_HOSTS=<railway-domain>.railway.app
DATABASE_URL=<railway-postgres-url>
REDIS_URL=<railway-redis-url>
SECRET_KEY=<generated-secret>
```

**Deployment Flow**:
```
git push origin staging  → Railway auto-deploys to staging
git push origin main     → Railway auto-deploys to production
```

**Health Checks**:
- `/health/` endpoint
- Railway monitors application health

---

## Integration Points

### 1. **Django Admin**

- Organization-scoped admin (users only see their org's data)
- Customized ModelAdmin with `get_queryset()` override
- Audit log integration

### 2. **Django REST Framework (DRF)**

- API endpoints for HTMX
- External integrations (future: mobile app, third-party systems)
- Organization-scoped ViewSets

### 3. **Celery Tasks**

- Background processing (report generation, data exports)
- Scheduled tasks (data sync, cleanup)
- Organization context passed to tasks

### 4. **obcAI Integration**

- Django views call ADK coordinator
- Organization context passed to function tools
- Multi-tenant isolation in AI layer

---

## Design Principles

### 1. **Simplicity**

- Django monolith (not microservices)
- HTMX over React/Vue (less complexity)
- PostgreSQL for all data (no multiple databases)

### 2. **Security**

- Multi-tenant data isolation (organization filtering)
- RBAC permissions
- CSP compliance (mandatory)
- Audit trails

### 3. **Government Compliance**

- Data retention (soft deletes)
- Audit trails (who, what, when)
- Data privacy (organization isolation)
- Regulatory compliance (Data Privacy Act)

### 4. **Developer Experience**

- Django's "batteries included" philosophy
- Clear conventions (see `common-conventions.md`)
- Comprehensive documentation
- OBCMS design system (Tailwind + custom components)

---

## Data Flow Example: Create Community

```
1. USER ACTION
   User fills community form → Clicks "Create"

2. FRONTEND (HTMX)
   <form hx-post="/api/communities/" hx-target="#community-list">
      ...
   </form>

3. DJANGO VIEW
   @permission_required('communities.add_community')
   def create_community(request):
       form = CommunityForm(request.POST)
       if form.is_valid():
           community = form.save(commit=False)
           community.organization = request.user.organization  # Multi-tenant
           community.created_by = request.user  # Audit trail
           community.save()
           return render(request, 'communities/community_row.html', {'community': community})

4. DATABASE (PostgreSQL)
   INSERT INTO communities_community (
       name,
       organization_id,  -- Multi-tenant isolation
       created_by_id,    -- Audit trail
       created_at
   ) VALUES (...)

5. RESPONSE (HTMX)
   Django renders `community_row.html` → HTMX swaps into #community-list

6. UI UPDATE
   New community appears in list (no full page reload)
```

---

## Scaling Considerations

### Current Scale

- **Users**: 100-500 concurrent users
- **Data**: Thousands of communities, assessments, partnerships
- **Traffic**: Government system (not consumer-facing)

### Scaling Strategy

**Vertical Scaling** (current):
- Railway allows easy resource upgrades
- PostgreSQL connection pooling
- Redis caching

**Horizontal Scaling** (future, if needed):
- Railway supports multiple replicas
- Load balancing
- Read replicas for PostgreSQL

**Performance Optimizations**:
- QuerySet optimization (select_related, prefetch_related)
- Database indexing
- Redis caching (frequently accessed data)
- Celery for long-running tasks

---

## Technology Stack Summary

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Django Templates + HTMX + Alpine.js + Tailwind CSS | Server-rendered HTML with dynamic interactions |
| **Backend** | Django 5.2 + DRF | Business logic, API endpoints |
| **Database** | PostgreSQL (production), SQLite (development) | Data persistence |
| **Background** | Celery + Redis | Async tasks, scheduled jobs |
| **AI** | Google ADK + Gemini + Zhipu GLM 4.6 | Multi-agent AI system (obcAI) |
| **Deployment** | Railway | Cloud platform, CI/CD |
| **Mapping** | Leaflet.js | Interactive maps |
| **Scheduling** | FullCalendar | Calendar and meeting scheduling |

---

**Next**: See `tech-stack-guide.md` for detailed explanations of each technology choice.
