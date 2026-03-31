# MoroAcademy Design Thinking Document

**Platform**: MoroAcademy Learning Management System
**URL**: https://negosyo.bangsamoro.site/academy (or moroacademy.ph)
**Framework**: Stanford d.school 5-Phase Design Thinking
**Date**: December 2024

---

## Executive Summary

MoroAcademy is the learning and capacity-building platform for the Bangsamoro region, serving cooperatives, social enterprises, aspiring entrepreneurs, and government staff. This Design Thinking document captures user insights, learning needs, and opportunity areas to create impactful learning experiences.

---

## Table of Contents

1. [Platform Overview](#platform-overview)
2. [Phase 1: Empathize](#phase-1-empathize)
3. [Phase 2: Define](#phase-2-define)
4. [Phase 3: Ideate](#phase-3-ideate)
5. [Phase 4: Prototype](#phase-4-prototype)
6. [Phase 5: Test](#phase-5-test)
7. [Implementation Roadmap](#implementation-roadmap)

---

## Platform Overview

### Vision

To build the entrepreneurial and organizational capacity of Bangsamoro through accessible, culturally-relevant, and practically-focused learning that transforms knowledge into action.

### Platform Architecture

| Component | Description | Users |
|-----------|-------------|-------|
| **Online Courses** | Self-paced video and text modules | All learners |
| **Live Workshops** | Scheduled interactive sessions | Enrolled participants |
| **Certification** | Achievement recognition | Completers |
| **Training Calendar** | Event discovery and registration | All users |
| **Provider Portal** | Course creation and management | TSPs, CSEA, Coops |

### Learning Ecosystem

```
                    ┌─────────────────────────────────────┐
                    │    CSEA (Primary Provider)          │
                    │  Regulatory training, compliance    │
                    └─────────────────┬───────────────────┘
                                      │
           ┌──────────────────────────┼──────────────────────────┐
           │                          │                          │
           ▼                          ▼                          ▼
┌─────────────────────┐   ┌─────────────────────┐   ┌─────────────────────┐
│  Training Service   │   │    Cooperatives     │   │  Partner Agencies   │
│     Providers       │   │  (Peer Learning)    │   │   MAFAR, MTIT, etc  │
│  - Private trainers │   │  - Best practices   │   │  - Sector-specific  │
│  - Consultants      │   │  - Member training  │   │  - Policy updates   │
└──────────┬──────────┘   └──────────┬──────────┘   └──────────┬──────────┘
           │                          │                          │
           └──────────────────────────┼──────────────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────┐
                    │           LEARNERS                   │
                    │  - Coop officers & members           │
                    │  - SE founders & teams               │
                    │  - Aspiring entrepreneurs            │
                    │  - Government staff                  │
                    └─────────────────────────────────────┘
```

### Learning Pathways

```
LEARNER JOURNEY PATHWAYS
│
├── COOPERATIVE DEVELOPMENT PATH
│   ├── Coop Fundamentals (RA 9520)
│   ├── Coop Governance & Management
│   ├── Financial Management for Coops
│   ├── FRAMES Compliance
│   └── Advanced: Coop Federation Leadership
│
├── SOCIAL ENTERPRISE PATH
│   ├── SE Fundamentals
│   ├── Business Model Design (Lean Canvas)
│   ├── Impact Measurement (Theory of Change)
│   ├── Financial Sustainability
│   └── Advanced: Scaling Social Impact
│
├── ENTREPRENEURSHIP PATH
│   ├── Starting a Business
│   ├── Market Research & Validation
│   ├── Digital Marketing Basics
│   ├── Financial Literacy
│   └── Advanced: Growth & Investment
│
└── SPECIALIZED TRACKS
    ├── Agriculture & Fisheries (MAFAR)
    ├── Trade & Tourism (MTIT)
    ├── Digital Skills
    └── Leadership & Soft Skills
```

---

## Phase 1: Empathize

### User Personas

#### Persona 1: Aminah - Cooperative Officer

```
┌─────────────────────────────────────────────────────────────────────────┐
│  AMINAH - COOPERATIVE OFFICER                                           │
├─────────────────────────────────────────────────────────────────────────┤
│  Demographics:                                                          │
│  - Age: 38, Female                                                      │
│  - Location: Sultan Kudarat, Maguindanao                                │
│  - Role: Treasurer, Farmers Multipurpose Cooperative                    │
│  - Education: High school graduate                                      │
│  - Tech Comfort: Low (basic smartphone user)                            │
│  - Connectivity: Intermittent mobile data                               │
├─────────────────────────────────────────────────────────────────────────┤
│  Learning Goals:                                                        │
│  - Understand FRAMES reporting requirements                             │
│  - Learn proper bookkeeping for the coop                                │
│  - Get certified to maintain her officer role                           │
│  - Help the coop pass the next CSEA audit                               │
├─────────────────────────────────────────────────────────────────────────┤
│  Learning Barriers:                                                     │
│  - Limited time (farm work, household duties)                           │
│  - Slow and expensive internet                                          │
│  - Intimidated by online learning platforms                             │
│  - Prefers learning in Maguindanaon or Filipino                         │
│  - Needs practical, not theoretical content                             │
├─────────────────────────────────────────────────────────────────────────┤
│  Learning Preferences:                                                  │
│  - Short videos (< 10 minutes)                                          │
│  - Step-by-step tutorials                                               │
│  - Downloadable materials for offline review                            │
│  - Face-to-face workshops when available                                │
│  - Learning with fellow coop members                                    │
├─────────────────────────────────────────────────────────────────────────┤
│  Quote:                                                                 │
│  "I want to learn, but I don't have time for long classes.              │
│   Just show me how to do it correctly so our coop stays compliant."     │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Persona 2: Jamal - Aspiring Social Entrepreneur

```
┌─────────────────────────────────────────────────────────────────────────┐
│  JAMAL - ASPIRING SOCIAL ENTREPRENEUR                                   │
├─────────────────────────────────────────────────────────────────────────┤
│  Demographics:                                                          │
│  - Age: 24, Male                                                        │
│  - Location: Cotabato City                                              │
│  - Status: Recent college graduate (BS Entrepreneurship)                │
│  - Tech Comfort: High                                                   │
│  - Connectivity: Good (urban area)                                      │
├─────────────────────────────────────────────────────────────────────────┤
│  Learning Goals:                                                        │
│  - Turn his social business idea into reality                           │
│  - Learn how to register as a social enterprise                         │
│  - Understand impact measurement and reporting                          │
│  - Connect with mentors and potential partners                          │
│  - Access funding opportunities                                         │
├─────────────────────────────────────────────────────────────────────────┤
│  Learning Barriers:                                                     │
│  - Information overload (doesn't know where to start)                   │
│  - Theory-heavy courses that don't apply to BARMM context               │
│  - Lack of local case studies and examples                              │
│  - No clear pathway from learning to launching                          │
│  - Isolation (no entrepreneur community nearby)                         │
├─────────────────────────────────────────────────────────────────────────┤
│  Learning Preferences:                                                  │
│  - Interactive courses with exercises                                   │
│  - Case studies from successful BARMM enterprises                       │
│  - Mentorship and community features                                    │
│  - Project-based learning (build while learning)                        │
│  - Certificates that matter to funders/partners                         │
├─────────────────────────────────────────────────────────────────────────┤
│  Quote:                                                                 │
│  "I have the passion and the idea, but I need a roadmap.                │
│   Show me how others in Bangsamoro did it, and I'll follow."            │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Persona 3: Sittie Hanna - CSEA Trainer

```
┌─────────────────────────────────────────────────────────────────────────┐
│  SITTIE HANNA - CSEA TRAINER / CONTENT PROVIDER                         │
├─────────────────────────────────────────────────────────────────────────┤
│  Demographics:                                                          │
│  - Age: 45, Female                                                      │
│  - Location: Cotabato City (BARMM Government Center)                    │
│  - Role: Senior Cooperative Development Specialist, CSEA               │
│  - Education: Master's in Cooperative Management                        │
│  - Tech Comfort: Moderate                                               │
├─────────────────────────────────────────────────────────────────────────┤
│  Goals as Trainer:                                                      │
│  - Reach more coops than in-person training allows                      │
│  - Standardize training content across BARMM                            │
│  - Track learner progress and certification                             │
│  - Update content easily when regulations change                        │
│  - Reduce travel time while increasing impact                           │
├─────────────────────────────────────────────────────────────────────────┤
│  Challenges as Trainer:                                                 │
│  - No experience creating online courses                                │
│  - Limited video/content production skills                              │
│  - Existing materials are PowerPoint-based                              │
│  - Needs to balance online with in-person training                      │
│  - Wants to track who completed training                                │
├─────────────────────────────────────────────────────────────────────────┤
│  Platform Needs:                                                        │
│  - Easy course creation (no coding required)                            │
│  - Templates for different content types                                │
│  - Analytics on learner engagement                                      │
│  - Certificate generation                                               │
│  - Ability to schedule live sessions                                    │
├─────────────────────────────────────────────────────────────────────────┤
│  Quote:                                                                 │
│  "I know the content, but I don't know how to make it online.           │
│   Give me templates and tools, and I'll fill them with value."          │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Persona 4: Rashid - Training Service Provider

```
┌─────────────────────────────────────────────────────────────────────────┐
│  RASHID - TRAINING SERVICE PROVIDER                                     │
├─────────────────────────────────────────────────────────────────────────┤
│  Demographics:                                                          │
│  - Age: 52, Male                                                        │
│  - Location: Zamboanga City (serves BARMM)                              │
│  - Role: Managing Director, Mindanao Business Development Center        │
│  - Experience: 20+ years in enterprise development training             │
│  - Tech Comfort: Moderate to high                                       │
├─────────────────────────────────────────────────────────────────────────┤
│  Business Goals:                                                        │
│  - Expand reach to BARMM coops and SEs                                  │
│  - Generate revenue from training programs                              │
│  - Build reputation as BARMM-focused provider                           │
│  - Reduce logistics costs of in-person training                         │
│  - Create recurring training income                                     │
├─────────────────────────────────────────────────────────────────────────┤
│  Platform Needs:                                                        │
│  - Ability to offer paid courses                                        │
│  - Branding for his organization                                        │
│  - Payment integration                                                  │
│  - Student management and communication                                 │
│  - Marketing exposure to BARMM audience                                 │
├─────────────────────────────────────────────────────────────────────────┤
│  Concerns:                                                              │
│  - Will learners pay for online courses?                                │
│  - How will platform take revenue share?                                │
│  - Can he protect his proprietary content?                              │
│  - Competition with free CSEA courses                                   │
├─────────────────────────────────────────────────────────────────────────┤
│  Quote:                                                                 │
│  "I have years of training expertise. I need a platform that lets       │
│   me reach BARMM learners and build a sustainable training business."   │
└─────────────────────────────────────────────────────────────────────────┘
```

### Empathy Maps

#### Coop Officer Learner Empathy Map

| Quadrant | Insights |
|----------|----------|
| **SAYS** | "I don't have time for training" / "The online system is confusing" / "Just tell me what to do" |
| **THINKS** | Worried about failing compliance / Feels inadequate for the role / Hopes for simple guidance |
| **DOES** | Attends mandatory in-person training / Asks colleagues for help / Avoids complex platforms |
| **FEELS** | Overwhelmed by requirements / Anxious about audits / Proud when coop succeeds |

#### Aspiring Entrepreneur Empathy Map

| Quadrant | Insights |
|----------|----------|
| **SAYS** | "I want to make a difference" / "Where do I start?" / "Show me local examples" |
| **THINKS** | Excited but uncertain / Comparing with peers who got jobs / Dreams of impact |
| **DOES** | Watches YouTube business videos / Follows entrepreneur influencers / Works part-time jobs |
| **FEELS** | Motivated but directionless / Isolated without community / Impatient to launch |

### Learning Journey Maps

#### Current State: Cooperative Officer Training Journey

```
STAGE           AWARENESS        REGISTRATION     LEARNING         APPLICATION      CERTIFICATION

Actions         Hears about      Travels to       Sits through     Returns to       Gets certificate
                training         training venue   2-day workshop   coop, tries to   (maybe)
                from CSEA        (time + cost)    (PowerPoint)     apply learning

Touchpoints     CSEA field       Paper forms      Physical venue   No follow-up     Paper certificate
                visit            Phone calls      Printed modules  No support       Manual records

Emotions        😐 Obligated     😰 Inconvenient  😴 Overwhelmed   😕 Confused      😊 Relieved
                                                  (info overload)  (forgot details)

Pain Points     Unaware of       Time/cost to     Passive learning No reinforcement Lost certificates
                learning need    attend           Not practical    No accountability No verification
                until audit      Limited seats    One-size-fits-all Isolated         Not recognized
```

#### Current State: Aspiring Entrepreneur Learning Journey

```
STAGE           EXPLORATION      LEARNING         VALIDATION       LAUNCH           GROWTH

Actions         Searches online  Watches random   Asks friends     Tries something  (often gives up)
                Attends seminars videos           Guesses market   Small scale
                Reads articles   No structure     No mentorship    Trial and error

Touchpoints     Google/YouTube   YouTube          Personal network Own resources    None
                DTI seminars     Random courses   No formal        Social media     No support
                Facebook groups  Books            validation       Word of mouth

Emotions        😊 Excited       😐 Overwhelmed   😰 Uncertain     😓 Stressed      😞 Discouraged
                (possibilities)  (too much info)  (is this right?) (alone)          (no support)

Pain Points     No clear path    Generic content  No local mentors High failure     Isolation
                Too many options Not BARMM-relevant No feedback    No guidance      No community
                No local focus   Theory not practice No validation  Resource gaps   Often quits
```

---

## Phase 2: Define

### Problem Statements

#### Problem 1: Accessibility Gap

```
RURAL COOPERATIVE OFFICERS need ACCESSIBLE LEARNING
that fits their schedule and connectivity because
IN-PERSON TRAINING requires travel, time, and costs
that create barriers to building necessary skills.

Impact: Undertrained officers, non-compliant coops,
        knowledge concentrated in urban areas
```

#### Problem 2: Relevance Gap

```
BANGSAMORO LEARNERS need LOCALLY-RELEVANT CONTENT
with BARMM examples and context because GENERIC CONTENT
from Manila-centric sources doesn't reflect their
realities, regulations, and opportunities.

Impact: Low engagement, poor application of learning,
        disconnect between training and practice
```

#### Problem 3: Pathway Gap

```
ASPIRING ENTREPRENEURS need CLEAR LEARNING PATHWAYS
from idea to launch because FRAGMENTED RESOURCES and
LACK OF MENTORSHIP leave them without direction or
accountability for progress.

Impact: High abandonment, untapped potential,
        ideas that never become businesses
```

#### Problem 4: Provider Enablement Gap

```
TRAINERS AND PROVIDERS need EASY CONTENT CREATION TOOLS
because TECHNICAL BARRIERS to online course development
prevent quality content from reaching learners at scale.

Impact: Limited course variety, trainer burnout,
        knowledge trapped in individuals
```

### How Might We (HMW) Statements

#### HMW - Accessibility

| HMW Statement | Opportunity Area |
|---------------|------------------|
| HMW make learning accessible to officers with limited internet and time? | Mobile-First, Offline-Capable |
| HMW bring quality training to remote barangays without requiring travel? | Digital Delivery |
| HMW create learning experiences that fit between farm work and family duties? | Microlearning |
| HMW make platform navigation simple enough for first-time smartphone users? | Simplified UX |

#### HMW - Relevance

| HMW Statement | Opportunity Area |
|---------------|------------------|
| HMW create content that reflects BARMM regulations, examples, and context? | Localized Content |
| HMW incorporate local languages without losing technical accuracy? | Multilingual Support |
| HMW use stories from successful BARMM coops/SEs as teaching tools? | Case Study Library |
| HMW ensure learning translates directly to workplace application? | Practical Exercises |

#### HMW - Pathways

| HMW Statement | Opportunity Area |
|---------------|------------------|
| HMW guide learners from "I have an idea" to "I launched a business"? | Learning Paths |
| HMW provide mentorship and community without requiring physical presence? | Virtual Mentorship |
| HMW create accountability that keeps learners progressing? | Progress Tracking |
| HMW recognize learning achievements in ways that matter? | Meaningful Credentials |

#### HMW - Provider Enablement

| HMW Statement | Opportunity Area |
|---------------|------------------|
| HMW enable subject experts to create courses without technical skills? | No-Code Course Builder |
| HMW help trainers convert existing PowerPoints into engaging online content? | Content Migration Tools |
| HMW let providers reach BARMM learners while building sustainable income? | Provider Marketplace |
| HMW ensure quality standards while enabling diverse providers? | Quality Framework |

### Insight Synthesis

```
KEY INSIGHT 1: LEARNING MUST FIT LIFE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BARMM learners juggle farming, fishing, family, and faith.
Learning that demands large time blocks will fail.
The platform must deliver value in 10-minute moments,
downloadable for offline access, and resumable anytime.

KEY INSIGHT 2: LOCAL STORIES TEACH BEST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generic business content feels foreign and irrelevant.
When learners see "someone like me" succeed,
learning becomes believable and applicable.
Feature BARMM success stories as curriculum anchors.

KEY INSIGHT 3: CERTIFICATION MATTERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
In BARMM, certificates are proof of competence and trust.
CSEA-recognized credentials matter for compliance.
Funders and partners ask for training certificates.
Make certifications visible, verifiable, and valuable.

KEY INSIGHT 4: COMMUNITY ENABLES PERSISTENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Solo learners often quit. Community creates accountability.
Cohort-based experiences mirror the bayanihan spirit.
Peer learning builds relationships beyond the course.
Design for learning together, not just learning alone.
```

---

## Phase 3: Ideate

### Opportunity Areas

#### Area 1: Microlearning for Busy Lives

**Concept**: Bite-sized learning modules (5-10 minutes) that deliver practical knowledge in moments between other responsibilities, downloadable for offline access.

**Features**:
- Short video lessons (< 7 minutes each)
- Key takeaways in text/audio
- Offline download capability
- Progress saves automatically
- Mobile-first design

**User Value**:
- Learners: Learn in available moments
- Trainers: Higher completion rates
- CSEA: Broader training reach

#### Area 2: BARMM Case Study Library

**Concept**: A curated collection of success stories from Bangsamoro cooperatives and social enterprises, designed as teaching tools with lessons, challenges, and outcomes.

**Features**:
- Video interviews with founders/leaders
- Written case narratives
- Discussion questions
- Lessons learned highlights
- Cross-linked to relevant courses

**User Value**:
- Learners: See what's possible locally
- Coops/SEs: Recognition and visibility
- Trainers: Ready-to-use examples

#### Area 3: Guided Learning Paths

**Concept**: Structured journeys from beginner to competent, with clear milestones, recommended sequence, and completion certificates that matter.

**Features**:
- Curated course sequences
- Prerequisite tracking
- Progress visualization
- Milestone certificates
- Pathway completion credential

**User Value**:
- Learners: Clear direction, no overwhelm
- CSEA: Standardized competency development
- Employers: Recognizable qualifications

#### Area 4: Cohort-Based Learning

**Concept**: Time-bound learning experiences where groups progress together, creating accountability, community, and peer support.

**Features**:
- Scheduled cohort start dates
- Group progress tracking
- Discussion forums per cohort
- Live Q&A sessions
- Graduation events

**User Value**:
- Learners: Community and accountability
- Trainers: Engaged, supported learners
- CSEA: Trackable training outcomes

#### Area 5: No-Code Course Builder

**Concept**: Simple tools that let subject experts create professional courses without technical skills, including templates and migration tools for existing content.

**Features**:
- Drag-and-drop course builder
- Video upload and editing
- Quiz and assessment builder
- PowerPoint-to-course converter
- Preview and publish workflow

**User Value**:
- Trainers: Create without developers
- CSEA: Scalable content production
- Learners: More course variety

#### Area 6: Live Workshop Integration

**Concept**: Seamless support for scheduled live training sessions, combining the reach of online with the engagement of synchronous learning.

**Features**:
- Event scheduling and calendar
- Registration and attendance
- Live video integration
- Interactive features (polls, Q&A)
- Recording for on-demand access

**User Value**:
- Trainers: Best of both worlds
- Learners: Interactive experience
- CSEA: Trackable live training

### Concept Prioritization

| Concept | Learning Impact | Feasibility | Priority |
|---------|-----------------|-------------|----------|
| Microlearning for Busy Lives | High | High | P1 |
| Guided Learning Paths | High | Medium | P1 |
| No-Code Course Builder | High | Medium | P1 |
| BARMM Case Study Library | High | Medium | P2 |
| Live Workshop Integration | Medium | Medium | P2 |
| Cohort-Based Learning | High | Low | P3 |

---

## Phase 4: Prototype

### MVP Feature Set

#### Phase 1 MVP: Foundation (Months 1-3)

| Feature | Description | User Benefit |
|---------|-------------|--------------|
| **Course Catalog** | Browse available courses | Discover learning options |
| **Video Lessons** | Stream or download lessons | Learn on any device |
| **Progress Tracking** | Resume where you left off | Continuous learning |
| **Basic Quizzes** | Knowledge checks | Reinforce learning |
| **Certificates** | Completion recognition | Proof of learning |

#### Phase 2: Paths & Tools (Months 4-6)

| Feature | Description | User Benefit |
|---------|-------------|--------------|
| **Learning Paths** | Curated course sequences | Clear direction |
| **Course Builder** | Create and publish courses | Trainer enablement |
| **Live Sessions** | Schedule and host workshops | Interactive learning |
| **Provider Profiles** | Trainer/organization pages | Credibility building |
| **Offline Mode** | Download for offline access | Rural accessibility |

#### Phase 3: Community & Scale (Months 7-12)

| Feature | Description | User Benefit |
|---------|-------------|--------------|
| **Discussion Forums** | Course-based discussions | Peer learning |
| **Case Study Library** | BARMM success stories | Local relevance |
| **Cohort Features** | Group learning support | Accountability |
| **Advanced Analytics** | Learning insights | Data-driven improvement |
| **Mobile App** | Native mobile experience | Convenience |

### Prototype Testing Plan

#### Test 1: Course Consumption (Learner)

**Participants**: 8 cooperative officers (varying digital literacy)

**Scenario**: Complete a 5-module course on FRAMES basics

**Success Metrics**:
- Completion rate > 70%
- Average session length > 10 minutes
- Satisfaction score > 4/5

**Questions to Answer**:
- Can they navigate the platform independently?
- Is video length appropriate?
- Can they learn effectively on mobile?
- Does offline download work?

#### Test 2: Course Creation (Trainer)

**Participants**: 4 CSEA trainers

**Scenario**: Create a 3-module course from existing PowerPoint

**Success Metrics**:
- Task completion rate > 80%
- Time to create < 4 hours
- Quality assessment > 3/5

**Questions to Answer**:
- Is the course builder intuitive?
- Can they add videos and quizzes?
- Does PowerPoint conversion help?
- What support do they need?

#### Test 3: Learning Path (Aspiring Entrepreneur)

**Participants**: 6 aspiring entrepreneurs

**Scenario**: Complete first three modules of SE Development Path

**Success Metrics**:
- Path enrollment > 80%
- 3-module completion > 60%
- Would recommend > 80%

**Questions to Answer**:
- Is the path structure clear?
- Does content feel relevant to BARMM?
- What motivates continued progress?
- What causes dropout?

---

## Phase 5: Test

### Validation Framework

#### Learning Effectiveness Testing

| Question | Method | Success Indicator |
|----------|--------|-------------------|
| Do learners gain knowledge? | Pre/post assessment | >20% improvement |
| Do they apply learning? | Follow-up survey (30 days) | >50% report application |
| Do they complete courses? | Completion analytics | >60% completion rate |
| Do they progress on paths? | Path analytics | >40% continue to next course |

#### Platform Usability Testing

| Question | Method | Success Indicator |
|----------|--------|-------------------|
| Can rural users access content? | Field testing | >80% successful access |
| Is navigation intuitive? | Task success rate | >85% complete key tasks |
| Does offline mode work? | Technical testing | 100% download/play success |
| Is mobile experience adequate? | Mobile usability test | >4/5 satisfaction |

#### Provider Experience Testing

| Question | Method | Success Indicator |
|----------|--------|-------------------|
| Can trainers create courses? | Task observation | >80% independent completion |
| Is content quality adequate? | Peer review | >3/5 quality rating |
| Do providers see value? | Satisfaction survey | >4/5 would continue |
| Is the effort worthwhile? | Time tracking | <10 hours for basic course |

### Feedback Loops

```
CONTINUOUS LEARNING IMPROVEMENT
│
├── In-Course Feedback
│   ├── Lesson ratings (helpful/not helpful)
│   ├── Confusion flags on specific content
│   └── End-of-module survey
│
├── Learner Journey Tracking
│   ├── Drop-off point analysis
│   ├── Time-to-completion patterns
│   └── Re-engagement triggers
│
├── Trainer Feedback
│   ├── Course builder usability reports
│   ├── Learner engagement insights
│   └── Content update suggestions
│
└── Impact Assessment
    ├── Knowledge application surveys
    ├── Behavior change tracking
    └── Business outcome correlation
```

---

## Implementation Roadmap

### Year 1: Launch and Learn

```
Q1 (Months 1-3): MVP Launch
├── Platform live with 10 foundational courses
├── CSEA as primary content provider
├── 500 learners onboarded
└── Basic course builder available

Q2 (Months 4-6): Paths & Providers
├── 3 learning paths launched
├── 5 external providers onboarded
├── Live workshop feature
└── 1,500 cumulative learners

Q3 (Months 7-9): Engagement
├── Offline mode complete
├── Case study library started (10 cases)
├── Discussion forums
└── 3,000 cumulative learners

Q4 (Months 10-12): Scale
├── 50+ courses available
├── Mobile app launched
├── Basic cohort features
└── 5,000 learners, 500 completions
```

### Success Metrics

| Metric | Year 1 Target | Measurement |
|--------|---------------|-------------|
| Registered Learners | 5,000 | Platform count |
| Course Completions | 500 | Certificate issued |
| Courses Available | 50+ | Published courses |
| Content Providers | 10 | Active providers |
| Completion Rate | 60% | Enrollments → completions |
| Learner Satisfaction | 4.2/5 | Post-course survey |
| Mobile Users | 70% | Analytics |
| Rural Reach | 40% | Location data |
| Knowledge Gain | 25% | Pre/post scores |
| Application Rate | 50% | 30-day follow-up |

---

## Learning Design Principles

### BARMM-Specific Principles

| Principle | Application |
|-----------|-------------|
| **Respect for Time** | Microlearning, flexible scheduling, offline access |
| **Local Relevance** | BARMM examples, local regulations, regional context |
| **Community Spirit** | Peer learning, cohorts, discussion |
| **Practical Focus** | Do-able exercises, workplace application, real outputs |
| **Inclusive Access** | Mobile-first, low bandwidth, multilingual |
| **Recognizable Achievement** | CSEA-endorsed certificates, verifiable credentials |

### Accessibility Standards

| Standard | Implementation |
|----------|----------------|
| **Low Bandwidth** | Compressed videos, text alternatives, progressive loading |
| **Offline Capable** | Download for offline, sync when connected |
| **Mobile Optimized** | Touch-friendly, vertical video, large buttons |
| **Language Support** | Filipino primary, key terms in local languages |
| **Literacy Levels** | Video-first, visual aids, simple language |

### Quality Framework

| Dimension | Requirement |
|-----------|-------------|
| **Content Accuracy** | Expert review, regulatory alignment |
| **Instructional Design** | Clear objectives, chunked content, assessments |
| **Production Quality** | Adequate audio/video, professional presentation |
| **Engagement Design** | Interactive elements, varied formats |
| **Application Support** | Practical exercises, real-world examples |

---

## Appendix: Course Type Templates

### Template 1: Compliance Course

```
STRUCTURE:
├── Module 1: Why This Matters (Context + Consequences)
├── Module 2: The Requirements (What you must do)
├── Module 3: Step-by-Step How-To (Practical guidance)
├── Module 4: Common Mistakes (What to avoid)
├── Module 5: Resources & Support (Where to get help)
└── Assessment: Knowledge check + practical exercise

DURATION: 1-2 hours total
FORMAT: Video + downloadable checklists + quiz
CERTIFICATE: CSEA-endorsed compliance certificate
```

### Template 2: Skill Building Course

```
STRUCTURE:
├── Module 1: Foundation (Core concepts)
├── Module 2: Application (How to use it)
├── Module 3: Practice (Exercises with feedback)
├── Module 4: Advanced Tips (Level up)
├── Module 5: Your Action Plan (Personal application)
└── Assessment: Skill demonstration + peer review

DURATION: 3-5 hours total
FORMAT: Video lessons + practice exercises + assignments
CERTIFICATE: Skill completion badge
```

### Template 3: Business Development Workshop

```
STRUCTURE:
├── Session 1: The Framework (Model introduction)
├── Session 2: Your Situation (Apply to your business)
├── Session 3: Peer Feedback (Group review)
├── Session 4: Refinement (Iterate based on feedback)
├── Session 5: Action Planning (Next steps)
└── Final: Present your plan

DURATION: 2-day equivalent (4-6 hours)
FORMAT: Live sessions + between-session work + templates
CERTIFICATE: Workshop completion + validated output
```

---

## Works Cited

[1] Stanford d.school. "Design Thinking Bootleg." https://dschool.stanford.edu/resources/design-thinking-bootleg

[2] Wiggins, G. & McTighe, J. "Understanding by Design." ASCD, 2005.

[3] Bloom, B.S. "Taxonomy of Educational Objectives." Longman, 1956.

[4] Kirkpatrick, D. "Evaluating Training Programs: The Four Levels." Berrett-Koehler, 1994.

[5] CSEA-BARMM. Internal research on cooperative training needs.

[6] RA 9520. Philippine Cooperative Code of 2008 (Training Requirements).
