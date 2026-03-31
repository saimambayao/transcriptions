# Cross-Skill Integration Guide

## Skill Routing Table

| Scenario | Invoke Skill | Purpose |
|----------|--------------|---------|
| Creating coop course/workshop | `/academy` | Learning design, curriculum structure |
| Building registration UI | `/frontend` | Next.js components, forms, dashboards |
| Creating Django models | `/backend` | Django Ninja API, models, auth |
| Database schema design | `/database` | PostgreSQL, migrations, optimization |
| Testing coop features | `/test` | Unit, integration, E2E tests |
| Debugging issues | `/debugger` | Root cause analysis, fixes |
| Security implementation | `/security` | Auth, authorization, data isolation |
| Deep research on topics | `/deep-research` | Multi-source validation, citations |
| UI/UX optimization | `/ui-ux` | User journeys, accessibility |
| Feature development | `/featuredev` | Full-stack feature implementation |
| Coop financial health | `/finance` | PFRF compliance, statutory funds, budgeting |
| Financial statement analysis | `/financial-analyst` | Ratio analysis, PEARLS, DuPont analysis |
| Investment/fundraising | `/investor` | Capital raising, valuation for coops |

## Integration Patterns

### Cooperative Curriculum Design
```
/cooperative + /academy + /deep-research

/cooperative  -> Domain knowledge, RA 9520, principles
/deep-research -> Validate content, find best practices
/academy      -> Structure curriculum, learning objectives
```

### Cooperative Platform Features
```
/cooperative + /featuredev + /frontend + /backend

/cooperative  -> Requirements, compliance rules, data models
/featuredev   -> Feature planning, implementation workflow
/frontend     -> UI components, forms, dashboards
/backend      -> API endpoints, models, validation
```

### Compliance Dashboard
```
/cooperative + /frontend + /database

/cooperative  -> Reporting requirements, deadlines, forms
/database     -> Schema design, queries, optimization
/frontend     -> Dashboard UI, charts, status indicators
```

### Cooperative Financial Analysis
```
/cooperative + /finance + /financial-analyst

/cooperative       -> PFRF requirements, statutory fund rules, RA 9520 compliance
/finance           -> Organizational budgeting, controls, compliance
/financial-analyst -> Ratio analysis (PEARLS), DuPont analysis, financial modeling
```
