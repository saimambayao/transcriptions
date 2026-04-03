# OBCMS Skill Catalog

**Last Updated**: 2025-11-05
**Purpose**: Static catalog of known OBCMS skills with purposes, triggers, and integration points.

This catalog is used by AppManager for skill discovery and recommendations. Update this file when new skills are added.

---

## Architecture & Planning Skills

### architect
**Purpose**: Architectural evaluation, planning, design for OBCMS
**Domain**: Architecture, System Design
**Triggers**: "design", "architect", "plan architecture", "refactor architecture"
**Use When**:
- Evaluating current system architecture
- Planning new features with architectural implications
- Designing database schemas or API endpoints
- Making decisions about Django app structure
- Planning scalability improvements

**Outputs**: Architecture diagrams, design documents, recommendations
**Integration**: Works with `database`, `backend`, `featuredev`

---

### featuredev
**Purpose**: Feature-Driven Development (FDD) methodology for building features
**Domain**: Full-stack Development
**Triggers**: "new feature", "implement feature", "build feature"
**Use When**:
- Implementing new features from scratch
- Following FDD methodology (plan, model, build, test)
- Building full-stack functionality (Django + HTMX)

**Outputs**: Feature plans, models, views, templates, tests
**Integration**: Works with `frontend`, `backend`, `database`, `unit-tests`, `coditor`

**Workflow Phases**:
1. Planning: Feature modeling and design
2. Building: Implementation (models, views, templates)
3. Testing: Unit and integration tests
4. Deployment: Coditor audit + devops guidance

---

## Development Skills

### backend
**Purpose**: Django backend development patterns
**Domain**: Backend (Django, DRF, Celery)
**Triggers**: "models", "views", "API", "serializers", "Django"
**Use When**:
- Creating or modifying Django models
- Implementing views (function-based or class-based)
- Building REST APIs with DRF
- Implementing authentication/authorization
- Background tasks with Celery

**Outputs**: Python code (models.py, views.py, serializers.py, tasks.py)
**Integration**: Works with `database`, `security`, `frontend`, `unit-tests`

**Key Patterns**:
- Multi-tenant data isolation (organization filtering)
- RBAC permissions
- Soft deletes
- Audit trails

---

### frontend
**Purpose**: Frontend development with OBCMS design standards
**Domain**: Frontend (HTMX, Alpine.js, Tailwind CSS)
**Triggers**: "UI", "template", "HTMX", "Tailwind", "frontend"
**Use When**:
- Building OBCMS UI components
- Creating forms, data tables, dashboards
- Implementing HTMX interactions
- Following OBCMS design system (blue-green gradient)

**Outputs**: Django templates, HTMX code, Tailwind CSS
**Integration**: Works with `backend`, `security` (CSP compliance), `frontend-component-scaffolder`

**Critical Requirement**: All code must be CSP-compliant (GEMINI.md Rule 12)

---

### frontend-component-scaffolder
**Purpose**: Automated scaffolding for HTMX/Tailwind components
**Domain**: Frontend (Component Generation)
**Triggers**: "scaffold component", "generate modal", "create data table"
**Use When**:
- Generating production-ready Django templates
- Creating modals, data tables, forms, stat cards
- Ensuring design system consistency

**Outputs**: Scaffolded templates with Bangsamoro color scheme
**Integration**: Works with `frontend`, `backend`

---

### database
**Purpose**: PostgreSQL database design and optimization with Django ORM
**Domain**: Database (PostgreSQL, Django ORM)
**Triggers**: "database", "migration", "schema", "query optimization"
**Use When**:
- Designing database schemas
- Writing Django migrations
- Optimizing queries (select_related, prefetch_related)
- Managing database transactions

**Outputs**: Migrations, model definitions, optimized queries
**Integration**: Works with `backend`, `safety-first`, `coditor`

**Critical**: Follow GEMINI.md Rule 13 (Migration management)

---

## AI Development Skills

### ai-engineer
**Purpose**: AI engineering for OBCMS (general AI features)
**Domain**: AI/ML (LLM integration, prompt engineering, RAG)
**Triggers**: "AI", "LLM", "Gemini API", "semantic search", "RAG"
**Use When**:
- Building AI-powered features
- Implementing chatbots or intelligent automation
- Creating RAG systems or semantic search
- Prompt engineering

**Outputs**: AI integration code, prompts, embeddings
**Integration**: Works with `backend`, `security` (AI safety)

---

### obcai-engineer
**Purpose**: Specialized AI engineering for obcAI (Google ADK multi-agent system)
**Domain**: AI (Google ADK, Multi-Agent Systems)
**Triggers**: "obcAI", "ADK", "agent", "specialist agent", "function tools"
**Use When**:
- Implementing ADK specialist agents
- Creating function tools for obcAI
- Migrating handlers to ADK patterns
- Optimizing LLM costs (Gemini + Zhipu GLM 4.6)

**Outputs**: ADK agents, function tools, coordinator routing logic
**Integration**: Works with `backend`, `ai-engineer`, `security` (multi-tenant isolation)

**Key Concepts**: Gemini (primary), Zhipu GLM 4.6 (fallback), multi-tenant isolation, CSP compliance

---

## Security & Quality Skills

### security
**Purpose**: Security implementation for Django + HTMX
**Domain**: Security (Authentication, Authorization, CSP, Multi-Tenant)
**Triggers**: "security", "CSP", "authentication", "authorization", "XSS", "multi-tenant"
**Use When**:
- Implementing authentication or authorization
- Enforcing CSP compliance (GEMINI.md Rule 12)
- Preventing XSS, CSRF, SQL injection
- Ensuring multi-tenant data isolation

**Outputs**: Security patterns, middleware, CSP configurations
**Integration**: Works with `backend`, `frontend`, `coditor`

**Critical Requirements**:
- CSP compliance mandatory (nonce-based script/style loading)
- Multi-tenant data isolation (organization filtering)
- HTMX-compatible security patterns

**References**:
- `references/csp.md` - CSP implementation (400+ lines)
- `references/multi-tenant-security.md` - Multi-tenant patterns
- `references/xss-prevention.md` - XSS prevention

---

### coditor
**Purpose**: Deep code auditing for OBCMS codebase
**Domain**: Code Quality, Security Auditing
**Triggers**: "audit", "code review", "check code", "security audit"
**Use When**:
- Before deployment (mandatory for staging/production)
- After implementing security features
- Investigating code quality issues
- Systematic security audits

**Outputs**: Console + markdown reports (severity-based findings)
**Integration**: Works with all skills (quality gate)

**Audit Types**:
- Targeted (single app/component)
- Comprehensive (entire codebase)
- Issue-driven (specific problem)

**Severity Levels**: Critical (fix immediately), High (1 sprint), Medium (2-3 sprints), Low (when convenient)

**Reports**: Saved to `/Users/saidamenmambayao/apps/obcms/docs/coditor-audits/`

---

### safety-first
**Purpose**: Pre-task safety verification for OBCMS development
**Domain**: Safety, Risk Management
**Triggers**: "safety check", "verify safety", "before deployment", "before migration"
**Use When**:
- **Before ANY deployment** (staging or production)
- Before database migrations
- Before risky operations (data deletion, git operations)
- To verify git status and database safety

**Outputs**: Safety checklist results, approval/block decisions
**Integration**: Works with `devops`, `database`, `coditor`

**Critical Checks**:
- Git status (no uncommitted changes)
- Database safety (db.sqlite3 exists, no destructive operations)
- Prevents dangerous operations (GEMINI.md Rule 3)

**Usage**: Always invoke before deployment or migrations

---

## Debugging & Investigation Skills

### investigator
**Purpose**: Deep investigation of errors and issues in OBCMS
**Domain**: Research, Evidence-Based Problem Solving
**Triggers**: "investigate", "research error", "find solutions", "what's causing"
**Use When**:
- Investigating errors or production issues
- Researching solutions before implementation
- Need evidence-based alternatives
- Complex problem diagnosis

**Outputs**: 3 evidence-based solution alternatives (ranked), research summary
**Integration**: Works with `debugger`, `backend`, `frontend`

**Research Sources**: Official docs, GitHub issues, Stack Overflow, technical blogs
**Minimum**: 5 credible sources per solution

**Note**: Research only, does NOT implement solutions

---

### debugger
**Purpose**: Systematic debugging workflow for Django + HTMX
**Domain**: Debugging, Root Cause Analysis
**Triggers**: "debug", "fix error", "track down bug", "root cause"
**Use When**:
- Debugging errors or bugs
- Tracking down root causes
- Production issue analysis
- Need systematic debugging approach

**Outputs**: Root cause analysis, permanent fixes
**Integration**: Works with `investigator`, `backend`, `frontend`, `unit-tests`

**Workflows**:
- Ultrathinking Multi-Agent (production/complex errors)
- 7-Step Basic (simple development errors)

**Note**: Automatic workflow selection based on error complexity

---

### refactor
**Purpose**: Audit codebase before creating new code
**Domain**: Code Refactoring, DRY Principle
**Triggers**: "refactor", "consolidate", "optimize", "check for existing"
**Use When**:
- Before creating new functionality (check for duplicates)
- Consolidating duplicate code
- Optimizing implementations
- Ensuring no redundant files remain

**Outputs**: Refactored code, removed redundancies
**Integration**: Works with all development skills

**Workflow**:
1. Search for existing implementations
2. Evaluate if existing code can be extended
3. Refactor or create new (remove redundant files)

---

## Testing Skills

### unit-tests
**Purpose**: Run unit tests and fix failures (root cause fixes only)
**Domain**: Testing (Unit Tests)
**Triggers**: "run tests", "unit tests", "pytest", "test coverage"
**Use When**:
- After implementing features
- Before committing code
- Verifying bug fixes
- Ensuring test coverage > 80%

**Outputs**: Test results, root cause fixes
**Integration**: Works with `backend`, `frontend`, `coditor`

**Critical**: Fixes root causes, never bypasses tests

---

### integration-tests
**Purpose**: Run integration tests and fix failures (cross-module workflows)
**Domain**: Testing (Integration Tests)
**Triggers**: "integration tests", "test workflow", "end-to-end module"
**Use When**:
- Testing cross-module workflows (e.g., MANA → coordination)
- Verifying API endpoints with full HTTP stack
- After implementing multi-app features

**Outputs**: Integration test results, root cause fixes
**Integration**: Works with `backend`, `unit-tests`, `coditor`

---

### e2e-tests
**Purpose**: Run end-to-end tests and fix failures (complete user workflows)
**Domain**: Testing (E2E Browser Tests)
**Triggers**: "e2e tests", "test user journey", "browser tests"
**Use When**:
- Testing complete user workflows (UI to database)
- Verifying user interactions
- Testing browser-based features

**Outputs**: E2E test results, root cause fixes
**Integration**: Works with `frontend`, `backend`, `chromer-agent`

---

### component-tests
**Purpose**: Run component tests and fix failures
**Domain**: Testing (Component Tests)
**Triggers**: "component tests", "test component"
**Use When**:
- Testing individual UI components
- Verifying component behavior

**Outputs**: Component test results, fixes
**Integration**: Works with `frontend`

---

## DevOps & Deployment Skills

### devops
**Purpose**: Railway deployment expert, multi-cloud planning
**Domain**: DevOps, Deployment, Infrastructure
**Triggers**: "deploy", "deployment", "Railway", "infrastructure", "multi-cloud"
**Use When**:
- Deploying to staging or production (guidance only)
- Railway deployment issues
- Multi-cloud architecture planning (GCP, AWS, Azure)
- Environment configuration

**Outputs**: Deployment guidance, helper scripts (manual execution), recommendations
**Integration**: Works with `coditor` (pre-deployment audit), `safety-first`

**⚠️ CRITICAL**: Provides GUIDANCE only. NEVER auto-commits, auto-pushes, or auto-deploys.

**Helper Scripts** (all require manual execution):
- `scripts/railway-deploy.sh` - Deployment with confirmations
- `scripts/backup-database.sh` - Database backup
- `scripts/rollback.sh` - Rollback guidance
- `scripts/verify-deployment.sh` - Post-deployment verification

**Evidence-Based**: Confidence ratings (🟢 High, 🟡 Medium, 🟠 Low) with inline sources

---

## Utility Skills

### prompter
**Purpose**: Prompt improvement and requirement clarification
**Domain**: Requirements Engineering, Prompt Engineering
**Triggers**: User explicitly uses `/prompter`, or when refining ambiguous requests
**Use When**:
- Clarifying ambiguous requirements
- Enhancing prompts for better results
- Breaking down complex requests
- Planning new skills

**Outputs**: Clarified requirements, enhanced prompts, specification confirmations
**Integration**: Works with all skills (requirement clarification)

---

### skill-creator
**Purpose**: Create new skills for OBCMS
**Domain**: Skill Development
**Triggers**: User explicitly uses `/skill-creator`, "create new skill"
**Use When**:
- Creating new skills
- Following skill creation best practices
- Initializing skill directory structure

**Outputs**: New skill directories with SKILL.md, references/, scripts/, assets/
**Integration**: Works with `prompter` (for requirement clarification)

**Scripts**:
- `scripts/init_skill.py` - Initialize skill directory
- `scripts/quick_validate.py` - Validate skill structure

---

### appmanager (this skill!)
**Purpose**: Orchestrate all OBCMS skills throughout the application lifecycle
**Domain**: Workflow Orchestration, Skill Management
**Triggers**: Complex multi-skill workflows, "what should I do", "recommend workflow"
**Use When**:
- Beginning complex tasks (recommend workflow)
- Resuming interrupted workflows
- Need lifecycle-aware skill recommendations
- Skill health checks

**Outputs**: Workflow recommendations, state tracking, skill recommendations
**Integration**: Works with ALL skills (orchestration layer)

**Core Capabilities**:
1. Skill discovery (hybrid: static catalog + dynamic detection)
2. Workflow orchestration (recommend, ask permission)
3. Workflow state tracking (mandatory)
4. Lifecycle phase detection
5. Skill health checks
6. Pre-built workflow templates

---

## Skill Integration Map

### Common Skill Sequences

**New Feature Development**:
```
safety-first → featuredev → frontend → backend → unit-tests → integration-tests → coditor → devops
```

**Bug Fix**:
```
investigator → debugger → (backend|frontend) → unit-tests → coditor → devops
```

**Deployment** (Critical Safety):
```
safety-first → coditor → unit-tests → integration-tests → devops
```

**Database Migration**:
```
safety-first → database → backend → unit-tests → integration-tests → coditor → devops
```

**Security Enhancement**:
```
security → (backend|frontend) → unit-tests → coditor → devops
```

**AI Feature (obcAI)**:
```
obcai-engineer → backend → frontend → unit-tests → coditor → devops
```

---

## Skill Selection Quick Reference

| Task Type | Primary Skill | Supporting Skills |
|-----------|--------------|-------------------|
| New Feature | featuredev | frontend, backend, database, unit-tests, coditor |
| Bug Fix | investigator, debugger | backend, frontend, unit-tests |
| Deployment | devops | safety-first, coditor, unit-tests, integration-tests |
| Database Change | database | safety-first, backend, unit-tests, coditor |
| Security Issue | security | backend, frontend, coditor |
| Code Quality | coditor | refactor, unit-tests |
| Architecture | architect | database, featuredev, backend |
| AI Feature | obcai-engineer (or ai-engineer) | backend, frontend, unit-tests |
| Investigation | investigator | debugger |
| Refactoring | refactor | coditor, unit-tests |

---

## Updating This Catalog

When adding new skills:
1. Add entry to appropriate category
2. Include: Purpose, Domain, Triggers, Use When, Outputs, Integration
3. Update "Skill Integration Map" if applicable
4. Update "Skill Selection Quick Reference" if applicable
5. Commit changes to version control

**Last Verified**: 2025-11-05
**Total Skills**: 18
