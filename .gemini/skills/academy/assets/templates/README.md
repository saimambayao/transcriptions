# MoroAcademy Curriculum Templates

Quick reference to all course and workshop templates organized by category.

> **Template Version**: 2.0 | **Last Updated**: December 2025

---

## Base Templates & Guidelines

Start here when creating new courses or workshops.

| Template | Purpose |
|----------|---------|
| [_template-guidelines.md](_template-guidelines.md) | Shared standards: video duration, scripts, sessions, assessment, localization |
| [_course-template.md](_course-template.md) | Base template for online courses (self-paced) |
| [_workshop-template.md](_workshop-template.md) | Base template for live workshops (facilitated) |

---

## Template Index

### Cooperative Training (CDA/CSEA-Mandated)

| Code | Template | Type | Duration |
|------|----------|------|----------|
| **PRS** | [coop/prs-pre-registration-seminar.md](coop/prs-pre-registration-seminar.md) | Workshop | 6-8h (standard) / 3h 45m (condensed) |
| COOP-101 | [coop/coop-101-fundamentals.md](coop/coop-101-fundamentals.md) | Course | 8-16h |
| COOP-201 | [coop/coop-201-governance.md](coop/coop-201-governance.md) | Course | 8-16h |
| COOP-301 | [coop/coop-301-financial.md](coop/coop-301-financial.md) | Course | 8h |

### Social Enterprise Training

| Code | Template | Type | Duration |
|------|----------|------|----------|
| SE-101 | [se/se-101-fundamentals.md](se/se-101-fundamentals.md) | Course | 8h |

### Business Skills (Cross-Cutting)

| Code | Template | Type | Duration |
|------|----------|------|----------|
| BIZ-101 | [business/biz-101-accounting.md](business/biz-101-accounting.md) | Course | 8h |
| BIZ-201 | [business/biz-201-marketing.md](business/biz-201-marketing.md) | Course | 8h |
| — | [business/biz-training-catalog.md](business/biz-training-catalog.md) | Catalog | Various |

### Government Training

| Code | Template | Type | Duration |
|------|----------|------|----------|
| GOV-101 | [government/gov-101-csw.md](government/gov-101-csw.md) | Workshop | 16-24h |
| GOV-201 | [government/gov-201-supervision.md](government/gov-201-supervision.md) | Workshop | 16-24h |
| GOV-301 | [government/gov-301-leadership.md](government/gov-301-leadership.md) | Workshop | 24h |
| GOV-401 | [government/gov-401-planning.md](government/gov-401-planning.md) | Workshop | 16-24h |
| GOV-501 | [government/gov-501-project-management.md](government/gov-501-project-management.md) | Workshop | 24h |
| GOV-502 | [government/gov-502-results-based-me.md](government/gov-502-results-based-me.md) | Workshop | 24h |
| — | [government/gov-training-catalog.md](government/gov-training-catalog.md) | Catalog | Various |

### Multi-Day Workshops

| Code | Template | Type | Duration |
|------|----------|------|----------|
| EDP-500 | [workshops/edp-500-enterprise-development.md](workshops/edp-500-enterprise-development.md) | Workshop | 3 days |
| FRAMES | [workshops/frames-compliance-workshop.md](workshops/frames-compliance-workshop.md) | Workshop | 2-5 days |

---

## Template Structure

All templates follow a standardized structure. See base templates for full format.

### Course Template Structure

```markdown
# [CODE]: [Course Title]

## Overview (Code, Type, Duration, Target Audience, Prerequisites)
## Target Learner Personas (2-3 personas with learning styles)
## Learning Objectives (Bloom's Taxonomy verbs)
## Storytelling Opportunities (hooks, case studies, transformation arc)
## Gamification Opportunities (points, badges, engagement)
## Curriculum Structure (Modules → Lessons)
## Required Materials/Templates
## Practical Exercises
## Assessment Strategy (formative, summative, certificate)
## Follow-up Learning Paths
## BARMM Localization
## Skill Integration Notes
## Deep Research References      ← Place at end, before Version History
## Version History
```

### Workshop Template Structure

```markdown
# [CODE]: [Workshop Title]

## Overview (Code, Type, Duration, Target Audience, Max Participants)
## Target Learner Personas (with group dynamics)
## Learning Objectives (Bloom's Taxonomy verbs)
## Key Outputs (tangible deliverables)
## Storytelling Opportunities (narrative arc, case studies)
## Gamification Opportunities (team competition, simulations)
## Venue & Logistics Requirements
## Workshop Curriculum (Days → Modules → Sessions)
## Simulation/Game Materials (if applicable)
## Key Templates
## Assessment Strategy
## Facilitator Guide (before/during/after)
## BARMM Localization
## Skill Integration Notes
## Deep Research References      ← Place at end, before Version History
## Version History
```

---

## Usage

1. **Start with guidelines**: Read `_template-guidelines.md` for standards
2. **Choose base template**: `_course-template.md` or `_workshop-template.md`
3. **Copy and customize**: Fill in content for your specific program
4. **Deep research**: Invoke `/deep-research` before curriculum design
5. **Add narrative**: Invoke `/storyteller` for engaging content
6. **Add gamification**: Invoke `/gamifier` for game elements
7. **Localize**: Apply BARMM context, Islamic considerations
8. **Build**: Use `/frontend` to create MoroAcademy pages

---

## Skill Integration

| Need | Invoke | Purpose |
|------|--------|---------|
| Deep topic research | `/deep-research` | Validate curriculum content |
| Narrative design | `/storyteller` | Hero's Journey, personas, journey maps |
| Gamification | `/gamifier` | Points, badges, simulations |
| Presentation slides | `/presentation` | Session pages, facilitator UI |
| Cooperative content | `/cooperative` | RA 9520, CDA MCs, registration |
| Course UI | `/frontend` | MoroAcademy page components |
| API endpoints | `/backend` | Enrollment, progress tracking |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2025-12-28 | Added base templates, guidelines, PRS, learner personas, storytelling/gamification hooks, catalogs |
| 1.0 | 2025-12 | Initial template index |
