# MoroAcademy Template Guidelines

Shared standards for all course and workshop templates. Reference this file instead of duplicating content.

---

## Video Duration Guidelines

Based on research from MIT/edX (6.9M video sessions), cognitive load theory, adult learning principles, and 2024-2025 validation studies.

| Duration | Purpose | Content Type | Word Count (~90 wpm) |
|----------|---------|--------------|---------------------|
| **3 min** | Quick definitions | Single term/concept introduction | ~270 words |
| **5 min** | Single concepts | One idea with brief explanation | ~450 words |
| **7 min** | Concepts + examples | Idea with 2-3 practical examples | ~630 words |
| **10 min** | Processes/workflows | Step-by-step procedures | ~900 words |
| **12 min** | Complex topics | Multi-part concepts with practice | ~1,080 words |
| **15 min** | Comprehensive | Full topic coverage with application | ~1,350 words |

### Key Research Findings (Validated 2024-2025)

- **6 minutes is optimal** for engagement (MIT/edX study, 6.9M sessions)
- **9% higher performance** with short videos vs long-form (2024 study)
- **25-60% retention improvement** with segmented microlearning
- **Segmenting effect size: 0.79-0.98** (strong evidence for chunking)
- Break complex topics into multiple shorter videos
- One concept per video for beginners
- Include 2-3 examples in 7-minute videos

**Full methodology**: See [video-duration-methodology.md](../video-duration-methodology.md)

---

## Script Requirements

### Bilingual Scripts

Each video lesson requires dual-language scripts:

1. **English Script** - Primary language for formal/technical terms
2. **Filipino Script** - Localized version for accessibility
3. **Timing Markers** - Scene/slide change indicators
4. **Visual Cues** - On-screen text and graphics notes

### Script Pacing (~90 WPM)

MoroAcademy uses **80-100 wpm (target ~90 wpm)** for both Filipino and English content. This slower pace is designed for BARMM's ESL beginner learners (English as L3/L4, rural conflict-affected areas, varied educational backgrounds).

**Additional pacing considerations:**
- Longer words with affixes (mag-, nag-, -in, -an) in Filipino
- Technical term explanation pairs (English term + Filipino meaning)
- Natural code-switching (Taglish) pauses
- Clearer enunciation for educational content

### Technical Term Pattern

Format: `"[English term], o [Filipino explanation]"`

**Examples:**
- "Ang **cooperative**, o kooperatiba, ay..."
- "Dapat nating i-compute ang **patronage refund**, ang bahagi ng bawat miyembro..."
- "Ang **social enterprise**, o negosyong panlipunan, ay..."
- "I-record natin ito sa **journal**, ang aklat ng mga transaksyon..."

### Timing Buffers

- Add +15 seconds per technical definition
- Add +20 seconds for example explanations
- Add +20 seconds for calculation walkthroughs
- Total buffer: 15-20% of estimated duration

### Script Template

```markdown
LESSON: [Title]
DURATION: [X] minutes
LANGUAGE: [Filipino/English]
WORD COUNT: [~90 wpm x duration in minutes]

---

[00:00] OPENING
Visual: [Description]
Narration: "[Script text]"

[00:30] SECTION 1: [Topic]
Visual: [Description]
Narration: "[Script text]"

[Continues...]

[XX:XX] CLOSING
Visual: Key takeaways
Narration: "[Summary and transition]"
```

---

## Lesson Pattern Templates

### Video Lesson Pattern

```markdown
**Lesson X.X: [Title]** (VIDEO - [X] min)
- [Bullet point 1]
- [Bullet point 2]
- [Bullet point 3]
- **Script**: English + Filipino
- **Visuals**: [Description of visual elements]
```

### Text Lesson Pattern

```markdown
**Lesson X.X: [Title]** (TEXT - [X] min)
- [Bullet point 1]
- [Bullet point 2]
- **Reading**: English + Filipino versions
```

### Quiz Pattern

```markdown
**Quiz X: [Topic]** ([N] questions)
- Covers: [Topics covered]
- Passing score: 70%
- Attempts: Unlimited
```

---

## Session Pattern Templates (Workshops)

### Lecture Session

```markdown
**Session X.X: [Title]** (45-60 min)
- Type: LECTURE
- Content:
  - [Topic 1]
  - [Topic 2]
  - [Topic 3]
- Materials: [Slides, handouts]
- Facilitator Notes: [Key points, common questions]
```

### Workshop Activity Session

```markdown
**Session X.X: [Title]** (60-90 min)
- Type: WORKSHOP
- Content:
  - [Activity description]
  - [Expected output]
- Template: [Template name]
- Output: [What participants produce]
- Facilitator Notes: [Coaching tips, time management]
```

### Simulation Session

```markdown
**Session X.X: [Simulation Name]** (90-120 min)
- Type: SIMULATION
- Setup: [Team formation, materials distribution]
- Rounds: [Number and description]
- Debrief: [Key learning points]
- Materials: [Game components list]
```

---

## Assessment Standards

### Quiz Standards

| Element | Standard |
|---------|----------|
| Questions per quiz | 10 (module) / 20-30 (final) |
| Passing score | 70% |
| Attempts | Unlimited (formative) / 3 max (summative) |
| Feedback | Immediate with explanations |
| Question types | MCQ, True/False, Short Answer |

### Certificate Requirements

| Requirement | Course | Workshop |
|-------------|--------|----------|
| Completion | 80% minimum | 80% attendance |
| Quiz passing | 70% each | N/A |
| Final assessment | 70% | 70% (if applicable) |
| Outputs | Optional | Required (action plan, etc.) |

### Workshop Attendance

- Track per session (not just per day)
- 80% minimum for certificate
- Late arrivals: Count as 0.5 attendance
- Use QR code or sign-in sheet

---

## Learner Persona Framework

Include in every template to ensure learner-centered design.

### Persona Template

```markdown
## Target Learner Personas

### Persona 1: [Name]
- **Role**: [Job title, position]
- **Experience**: [Years, background]
- **Goals**: [What they want to achieve]
- **Challenges**: [Barriers to learning]
- **Tech Comfort**: [Low/Medium/High]
- **Time Availability**: [Hours per week]
- **Language**: [Primary language, English proficiency]

### Persona 2: [Name]
[Same structure]
```

### Common BARMM Personas

| Persona | Description |
|---------|-------------|
| **First-time Officer** | Newly elected, little coop experience, eager but overwhelmed |
| **Experienced Leader** | 5+ years, seeking advanced skills, time-constrained |
| **Government Staff** | Familiar with bureaucracy, needs practical application |
| **Young Entrepreneur** | Tech-savvy, ambitious, limited business experience |
| **Community Elder** | Respected, traditional, prefers face-to-face learning |

---

## Storytelling Integration

For narrative design, invoke `/storyteller` skill.

### Story Hooks Section

Include in templates to guide narrative integration:

```markdown
## Storytelling Opportunities

### Opening Hook
- [Compelling question or scenario to open each module]

### Case Studies
- [Real BARMM examples that illustrate key concepts]

### Transformation Arc
- [How learners change from beginning to end]

### Memorable Examples
- [Stories that make abstract concepts concrete]
```

### When to Invoke /storyteller

- Designing learner journey maps
- Creating video lesson narratives
- Building case study scenarios
- Crafting opening hooks and closings

---

## Gamification Integration

For game design, invoke `/gamifier` skill.

### Gamification Hooks Section

Include in templates to guide game integration:

```markdown
## Gamification Opportunities

### Progress Mechanics
- [Badges, points, levels for this course/workshop]

### Competition Elements
- [Leaderboards, challenges, team competitions]

### Simulation Games
- [Business simulations appropriate for this content]

### Engagement Boosters
- [Quick wins, streaks, social features]
```

### When to Invoke /gamifier

- Adding points/badges to courses
- Designing business simulations
- Creating competitive workshop activities
- Building engagement mechanics

---

## BARMM Localization Standards

### Context Requirements

Every template must include:

1. **Local Examples**: BARMM cooperatives, SEs, government cases
2. **Cultural Sensitivity**: Islamic principles where relevant
3. **Language Accessibility**: Filipino + local language considerations
4. **Regulatory Alignment**: CSEA requirements, not just CDA

### Cultural Sensitivity Checklist

- [ ] Include Islamic cooperative/business principles (where relevant)
- [ ] Reference halal compliance considerations
- [ ] Respect local cultural practices
- [ ] Use inclusive language
- [ ] Avoid assumptions about gender roles
- [ ] Include community-centered approaches

### Regulatory References

| Topic | CDA National | CSEA BARMM |
|-------|--------------|------------|
| Registration | CDA Regional Office | CSEA |
| Training requirements | MC 2015-09 | Adopted by CSEA |
| Compliance reports | CAIS | CSEA Portal |
| PRS requirement | CDA-accredited TSP | CSEA-accredited |

---

## Template File Naming Convention

### Courses

Format: `[code]-[short-name].md`

Examples:
- `coop-101-fundamentals.md`
- `se-101-fundamentals.md`
- `biz-101-accounting.md`

### Workshops

Format: `[code]-[short-name].md`

Examples:
- `edp-500-enterprise-development.md`
- `gov-101-csw.md`
- `prs-pre-registration-seminar.md`

### Base Templates (Prefix with underscore)

- `_course-template.md` - Base template for courses
- `_workshop-template.md` - Base template for workshops
- `_template-guidelines.md` - This file (shared standards)

---

## Skill Integration Quick Reference

| Need | Skill | Trigger |
|------|-------|---------|
| Narrative design | `/storyteller` | Hero's Journey, personas, journey maps |
| Gamification | `/gamifier` | Points, badges, simulations |
| Presentation slides | `/presentation` | Session pages, facilitator UI |
| Course UI pages | `/frontend` | MoroAcademy page components |
| API endpoints | `/backend` | Enrollment, progress tracking |
| Full features | `/featuredev` | Complete feature implementation |
| Cooperative content | `/cooperative` | RA 9520, CDA MCs, registration |
| Research | `/deep-research` | Topic validation, best practices |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2025-12-28 | Consolidated from individual templates; added persona, storytelling, gamification sections |
| 1.0 | 2025-12 | Initial template standards |
