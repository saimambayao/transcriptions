---
name: storyteller
description: Narrative design specialist for MoroAcademy courses and workshops. Use when adding storytelling, creating learner personas, mapping learner journeys, or designing emotional engagement for video lessons and live training. Provides Hero's Journey mapping, 3-Act video structure, story template selection, micro-story design, empathy mapping, transformation design, and character development. Integrates with /academy for curriculum development and /gamifier for narrative-driven game elements.
argument-hint: "[topic]"
---

# Storyteller - Narrative Design for MoroAcademy

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's storytelling request                     ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

Transform courses and workshops from information delivery into memorable, emotionally engaging learning experiences through storytelling and learner-centered design.

**Core Insight**: 63% retain information in stories vs. 5% from standard presentations.

## When to Use

Invoke `/storyteller` when:
- "Add storytelling to this course"
- "Design narrative for video lessons"
- "Create learner personas for this training"
- "Map the learner journey"
- "Make this workshop more engaging"
- "Design story-based assessments"
- "Create characters for this course"
- "Structure this video with a story arc"

**Keywords**: storytelling, narrative, hero's journey, story arc, 3-act structure, learner journey, persona, empathy map, transformation, micro-story, character, engagement, emotional design

---

## Quick Start Workflows

### 1. Add Storytelling to a Course

```
INPUT: Course outline or topic
OUTPUT: Narrative-enhanced course structure

STEPS:
1. Select story framework (Hero's Journey or 3-Act)
2. Map course modules to story stages
3. Create 1-2 recurring characters
4. Add narrative hooks between modules
5. Design story-based final assessment
```

### 2. Design Video Lesson Narrative

```
INPUT: Lesson topic and duration
OUTPUT: Story-structured video script outline

STEPS:
1. Choose format: Micro-story (2-5 min) or Standard (5-15 min)
2. Apply 3-Act Structure (25% / 50% / 25%)
3. Create opening hook (first 10 seconds)
4. Build character-driven scenario
5. End with transformation + takeaway
```

### 3. Create Learner Personas

```
INPUT: Target audience description
OUTPUT: 2-3 detailed learner personas

STEPS:
1. Define persona elements (name, role, goals, barriers)
2. Create empathy map for each (8 questions)
3. Identify pain points and motivators
4. Map learning preferences
5. Document in standard template
```

### 4. Map Learner Journey

```
INPUT: Course/workshop structure
OUTPUT: Visual journey map with touchpoints

STEPS:
1. Define journey stages (Awareness → Advocate)
2. Map learner emotions at each stage
3. Identify pain points and opportunities
4. Design interventions for critical moments
5. Define success metrics per stage
```

---

## Story Frameworks

### Hero's Journey (12 Stages)

Map course structure to learner transformation:

| Stage | Course Element | Design Focus |
|-------|----------------|--------------|
| 1. Ordinary World | Pre-assessment | Current state |
| 2. Call to Adventure | Course intro | Present the challenge |
| 3. Refusal of Call | Module 1 | Address barriers |
| 4. Meeting Mentor | Instructor intro | Establish trust |
| 5. Crossing Threshold | First activity | Commit to learning |
| 6. Tests & Allies | Core modules | Practice with support |
| 7. Approach Cave | Advanced content | Build toward mastery |
| 8. Ordeal | Major assessment | Prove competence |
| 9. Reward | Skill achieved | Celebrate progress |
| 10. Road Back | Application planning | Real-world transfer |
| 11. Resurrection | Final capstone | Ultimate test |
| 12. Return with Elixir | Graduation | Share with others |

**Best for**: Multi-module courses, leadership programs, certification paths.

### 3-Act Structure

For video lessons and single sessions:

```
ACT 1 (25%): SETUP
├── Hook (first 10 seconds)
├── Context (learner's situation)
├── Problem (challenge or gap)
└── Stakes (why it matters)

ACT 2 (50%): CONFRONTATION
├── Rising Action (skill building)
├── Obstacles (practice challenges)
├── Turning Point (key insight)
└── Skills Acquired (competencies)

ACT 3 (25%): RESOLUTION
├── Climax (apply all learning)
├── Resolution (demonstrate mastery)
├── Transformation (before/after)
└── Call to Action (next steps)
```

**Best for**: Video lessons, single workshops, presentations.

---

## Story Templates

See [storytelling-design.md](references/storytelling-design.md) for 7 story templates (Quest, Rags to Riches, Defeating the Baddie, etc.).

## Learner Personas

### Persona Template

```markdown
## [Name], [Age]

**Role**: [Job title or position]
**Background**: [Education, experience level]

### Goals
- [Primary goal]
- [Secondary goal]

### Pain Points
- [Frustration 1]
- [Frustration 2]

### Motivators
- [What drives them]

### Learning Preferences
- [How they prefer to learn]

### Barriers
- [What might prevent success]
```

### Empathy Map (8 Questions)

```
┌─────────────────┬─────────────────┐
│ What do I HEAR? │ What do I SEE?  │
│ (from others)   │ (in environment)│
├─────────────────┼─────────────────┤
│ What do I THINK?│ What do I SAY?  │
│ (private)       │ (public)        │
├─────────────────┴─────────────────┤
│     PAINS           │    GAINS    │
│ (frustrations)      │ (motivators)│
└─────────────────────┴─────────────┘
```

---

## Learner Journey Mapping

See [learner-journey-mapping.md](references/learner-journey-mapping.md) for journey stages and map elements.

## Transformation Design

See [learner-journey-mapping.md](references/learner-journey-mapping.md) for Before/After state design and transformation statements.

## Micro-Story Videos

See [storytelling-design.md](references/storytelling-design.md) for micro-story design principles, formats, and structures.

## Character Development

See [storytelling-design.md](references/storytelling-design.md) for character checklists and sample characters.

## Integration with /academy

When `/academy` invokes `/storyteller`, provide narrative-enhanced course structure, 3-Act video structures, learner personas, and journey maps.

## Output Templates

### Story Arc Document

```markdown
# Story Arc: [Course/Workshop Name]

## Framework: [Hero's Journey / 3-Act / Template Name]

## Characters
- **Protagonist**: [Name, role, challenge]
- **Mentor**: [Instructor/guide representation]
- **Allies**: [Peer learners, support]

## Arc Mapping

| Stage | Content | Emotional Beat |
|-------|---------|----------------|
| [Stage 1] | [Module/Lesson] | [Emotion] |
| ... | ... | ... |

## Narrative Hooks
- Module 1→2: [Hook/cliffhanger]
- Module 2→3: [Hook/cliffhanger]

## Transformation
- **Before**: [Starting state]
- **After**: [End state]
```

### Persona Document

```markdown
# Learner Personas: [Course Name]

## Persona 1: [Name]
[Full persona template]

## Persona 2: [Name]
[Full persona template]

## Design Implications
- [Implication for content]
- [Implication for delivery]
```

---

## References

Detailed frameworks and examples:
- [Storytelling Design](references/storytelling-design.md) - Hero's Journey, 3-Act, 7 templates, micro-stories, character development
- [Learner Journey Mapping](references/learner-journey-mapping.md) - Personas, empathy maps, journey stages, transformation framework

---

## Workflow: Storytelling in Cooperatives

See [cooperative-storytelling.md](references/cooperative-storytelling.md) for cooperative hero's journey, story archetypes, ICA principles as narrative themes, member personas, and community impact narratives.

## [Community Name] Transformation Story

### BEFORE the Cooperative (Year)
- **Economic**: [Poverty rate, unemployment, market access]
- **Social**: [Services available, community cohesion]
- **Infrastructure**: [What was lacking]
- **Aspirations**: [What people wanted but couldn't achieve]

### THE COOPERATIVE INTERVENTION
- **Founded**: [Year, founding members, initial capital]
- **Services**: [What the cooperative provided]
- **Approach**: [How it operated differently]

### AFTER the Cooperative (Current Year)
- **Economic**: [Income levels, employment, new businesses]
- **Social**: [New services, stronger community bonds]
- **Infrastructure**: [What was built or improved]
- **Achievements**: [What's now possible that wasn't before]

### RIPPLE EFFECTS
- [Non-members who benefited]
- [Other organizations inspired]
- [Policy changes influenced]
```

#### Impact Dimensions

| Dimension | Questions to Explore | Story Elements |
|-----------|---------------------|----------------|
| **Economic** | Jobs created? Income increased? Assets built? | Numbers, family stories, business growth |
| **Social** | Services provided? Conflicts reduced? Trust built? | Community events, mutual aid examples |
| **Environmental** | Resources protected? Sustainable practices? | Before/after landscapes, policy changes |
| **Cultural** | Traditions preserved? Identity strengthened? | Cultural programs, heritage protection |
| **Intergenerational** | Youth opportunities? Elder support? Knowledge transfer? | Family lineages in cooperative, succession |

#### Intergenerational Wealth Building

**Narrative Arc**:
```
GENERATION 1 (Founders)
├── Contributed initial capital
├── Volunteered unpaid labor
└── Established systems and values

GENERATION 2 (Builders)
├── Inherited stable institution
├── Expanded services and membership
└── Modernized operations

GENERATION 3 (Inheritors)
├── Received accumulated benefits
├── Access to loans, training, networks
└── Responsibility to continue and improve

COMMUNITY WEALTH
├── Infrastructure built by cooperative
├── Local economy strengthened
├── Human capital developed
└── Social cohesion maintained
```

---

### Practical Scenarios

Apply the frameworks to real storytelling challenges.

#### Scenario 1: Cooperative 25th Anniversary Origin Story

**Context**: A primary cooperative celebrating 25 years needs an origin story for anniversary materials (video, print, event).

**Workflow**:

1. **Research Phase**
   - Interview 3-5 founding members
   - Collect photos and documents from formation period
   - Identify the inciting incident (what problem sparked formation?)

2. **Story Structure** (Using "The Organizing Story" archetype)
   ```
   HOOK: The specific moment of decision

   ACT 1 - THE PROBLEM
   - What life was like before
   - Failed attempts at individual solutions
   - The moment of realization: "We need to work together"

   ACT 2 - THE ORGANIZING
   - First meetings and discussions
   - Obstacles overcome (skeptics, capital, regulations)
   - Key turning points
   - Registration and first operations

   ACT 3 - THE LEGACY
   - Early wins that proved the model
   - Growth over 25 years (members, capital, services)
   - Impact on community
   - Vision for next 25 years
   ```

3. **Character Focus**
   - Select 2-3 founding members as main characters
   - Include one skeptic-turned-believer for dramatic arc
   - Feature current young leader for continuity

4. **Deliverables**
   - 5-minute video script
   - Print anniversary booklet narrative
   - Speech for anniversary event

#### Scenario 2: Member Testimonial Campaign

**Context**: A cooperative wants to recruit new members using authentic testimonials.

**Workflow**:

1. **Persona Selection**
   - Identify 4-5 members representing different demographics
   - Balance genders, age groups, and service types
   - Seek diversity of experience (new member, long-time member, officer)

2. **Interview Guide**
   ```
   BEFORE QUESTIONS
   - What was your situation before joining?
   - What were your biggest challenges?
   - What did you try before the cooperative?

   TURNING POINT QUESTIONS
   - How did you hear about the cooperative?
   - What made you decide to join?
   - What was your first experience as a member?

   AFTER QUESTIONS
   - What has changed since joining?
   - What specific benefits have you received?
   - What surprised you about being a member?

   IMPACT QUESTIONS
   - How has the cooperative affected your family?
   - What would you tell someone considering joining?
   - What does being a member-owner mean to you?
   ```

3. **Story Structure per Testimonial** (2-3 minutes each)
   ```
   [0:00-0:30] HOOK + BEFORE STATE
   "My name is [Name]. Before joining the cooperative, I..."

   [0:30-1:30] TURNING POINT + EXPERIENCE
   "Then I learned about the cooperative. At first, I..."
   "What changed was when..."

   [1:30-2:30] TRANSFORMATION + INVITATION
   "Now, my life is different because..."
   "If you're considering joining, I would say..."
   ```

4. **Deliverables**
   - 5 short video testimonials (2-3 min each)
   - Quote cards for social media
   - Written testimonials for website/brochure

See [cooperative-storytelling.md](references/cooperative-storytelling.md) for Scenario 3 (Annual Report Impact Narrative) with data collection, narrative sections, visual storytelling, and deliverables.

---

## Skill Integration

| After Storyteller | Invoke | Purpose |
|-------------------|--------|--------|
| Story arc complete | `/academy` | Continue curriculum design |
| Personas defined | `/academy` | Inform content development |
| Video structure ready | `/frontend` | Build presentation UI |
| Journey mapped | `/ui-ux` | Optimize learning experience |
