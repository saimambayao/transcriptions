# OBCMS Tech Stack Guide

**Purpose**: Detailed explanation of each technology in OBCMS stack, why it was chosen, and how it's used.

---

## Backend Stack

### Django 5.2

**What**: Python web framework

**Why Chosen**:
- "Batteries included" (auth, admin, ORM out of the box)
- Excellent for government/enterprise systems
- Strong security features (CSRF, XSS protection)
- Large ecosystem, stable, well-documented

**OBCMS Usage**:
- MVC architecture (Models, Views, Templates)
- Multi-tenant implementation (organization-scoped models)
- RBAC permissions
- Django admin for data management

### Django REST Framework (DRF)

**What**: API framework for Django

**Why Chosen**:
- Seamless Django integration
- ViewSets, Serializers for rapid API development
- Built-in permission classes

**OBCMS Usage**:
- API endpoints for HTMX
- Organization-scoped ViewSets
- Future mobile app integration

### PostgreSQL

**What**: Relational database

**Why Chosen Over MySQL**:
- Advanced features (JSON fields, full-text search, array fields)
- Better multi-tenant support (row-level security)
- Excellent performance for complex queries
- GIS support (PostGIS for geographic data)

**OBCMS Usage**:
- Production database
- Organization-scoped data
- Geographic data (provinces, municipalities, barangays)
- JSON fields for flexible data (assessment responses)

### SQLite

**What**: Embedded database

**Why Used**:
- Development database (no setup required)
- Fast for single-user development
- Easy to reset (delete db.sqlite3)

**OBCMS Usage**:
- Development only (never production)
- CRITICAL: Never delete db.sqlite3 (GEMINI.md Rule 3)

### Celery + Redis

**What**: Distributed task queue + in-memory data store

**Why Chosen**:
- Async task processing
- Scheduled tasks (cron-like)
- Django integration

**OBCMS Usage**:
- Report generation (long-running)
- Data exports (CSV, Excel)
- Notifications (email, SMS)
- Data synchronization

---

## Frontend Stack

### HTMX

**What**: JavaScript library for dynamic HTML

**Why Chosen Over React/Vue**:
- Simplicity (HTML attributes, no build step)
- Excellent Django integration (server-rendered)
- Progressive enhancement
- CSP-friendly
- Backend team expertise

**OBCMS Usage**:
- Dynamic content updates (no full page reload)
- AJAX requests via HTML attributes
- Form submissions (validation feedback)
- Delete confirmations, modal interactions

**Example**:
```html
<button
    hx-delete="/api/tasks/123/"
    hx-target="#task-123"
    hx-swap="outerHTML"
    hx-confirm="Delete?">
    Delete
</button>
```

### Alpine.js

**What**: Lightweight JavaScript framework for client-side state

**Why Chosen**:
- Minimal JavaScript for instant UI feedback
- No server roundtrip needed
- Vue-like syntax (easy to learn)

**OBCMS Usage**:
- Dropdowns, modals, toggles
- Form validation feedback
- Client-side filtering/sorting
- UI state management

**Example**:
```html
<div x-data="{ open: false }">
    <button @click="open = !open">Menu</button>
    <ul x-show="open">...</ul>
</div>
```

### Tailwind CSS

**What**: Utility-first CSS framework

**Why Chosen Over Bootstrap**:
- Utility-first approach (rapid development)
- Customization (OBCMS design system)
- Smaller CSS bundle (purge unused)
- Modern design

**OBCMS Usage**:
- OBCMS design system (blue-green gradient)
- Responsive layouts
- Component styling
- Custom utility classes

### Leaflet.js

**What**: Interactive mapping library

**Why Chosen Over Google Maps**:
- Open-source, free
- Lightweight
- Excellent for GIS data
- Customizable

**OBCMS Usage**:
- Barangay boundary maps
- Community location markers
- Geographic visualization

### FullCalendar

**What**: Calendar and scheduling library

**Why Chosen**:
- Feature-rich (day/week/month views)
- Event management
- Drag-and-drop
- Django integration

**OBCMS Usage**:
- Coordination meeting scheduling
- Event calendar
- Availability management

---

## AI Stack

### Google ADK (Agent Development Kit)

**What**: Google's framework for building multi-agent AI systems

**Why Chosen**:
- Multi-agent architecture
- Function tool integration
- Gemini integration

**OBCMS Usage**:
- obcAI coordinator
- Specialist agents (Geographic, Community, MANA, Policy)
- Function tools (organization-scoped)

### Gemini (Primary LLM)

**What**: Google's large language model

**Why Chosen**:
- Cost-effective
- Good performance
- Google Cloud integration

**OBCMS Usage**:
- Primary LLM for obcAI
- Query understanding
- Response generation

### Zhipu GLM 4.6 (Fallback LLM)

**What**: Alternative LLM

**Why Added**:
- Fallback if Gemini fails
- Cost optimization
- Redundancy

**OBCMS Usage**:
- Fallback LLM for obcAI

---

## Deployment Stack

### Railway

**What**: Cloud platform (PaaS)

**Why Chosen Over Heroku/AWS**:
- Simple deployment (git push)
- Managed PostgreSQL + Redis
- Automatic HTTPS
- Environment-based deployments (staging, production)
- Cost-effective

**OBCMS Usage**:
- Production hosting
- Staging environment
- CI/CD (auto-deploy on git push)
- Database + Redis management

### Gunicorn

**What**: WSGI HTTP server for Python

**Why Chosen**:
- Production-ready
- Django compatibility
- Multi-worker support

**OBCMS Usage**:
- Production WSGI server
- Handles HTTP requests

---

## Development Tools

### Black

**What**: Python code formatter

**Why Used**:
- Consistent code style
- No configuration needed
- 88 character line length

### isort

**What**: Import sorting tool

**Why Used**:
- Consistent import ordering
- Integration with Black

### pytest

**What**: Testing framework

**Why Used**:
- Powerful test framework
- Django plugin (pytest-django)
- Coverage reporting

---

## Technology Decision Summary

| Decision | Options Considered | OBCMS Choice | Reasoning |
|----------|-------------------|--------------|-----------|
| **Framework** | Flask vs Django | Django | "Batteries included", admin, ORM, security |
| **Frontend** | React vs Vue vs HTMX | HTMX | Simplicity, Django integration, backend team |
| **CSS** | Bootstrap vs Tailwind | Tailwind | Customization, utility-first, modern |
| **Database** | MySQL vs PostgreSQL | PostgreSQL | Advanced features, multi-tenant support |
| **Deployment** | Heroku vs Railway vs AWS | Railway | Simplicity, cost, managed services |
| **AI** | OpenAI vs Gemini vs Claude | Gemini (+ Zhipu) | Cost, Google integration, fallback |

---

**Next**: See `design-patterns.md` for common design patterns used in OBCMS.
