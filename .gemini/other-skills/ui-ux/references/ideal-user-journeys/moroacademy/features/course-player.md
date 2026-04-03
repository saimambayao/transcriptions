# Course Player - MoroAcademy

## Overview

The **Course Player** is the main learning interface where enrolled learners consume course content. It's the heart of the MoroAcademy learning experience, providing video playback, lesson navigation, progress tracking, note-taking, and assessment capabilities in a distraction-free environment.

## What is a Course Player?

A Course Player is the interactive interface that learners use to:
- Watch video lessons
- Read text-based content
- Navigate between lessons and modules
- Track their progress through a course
- Take notes and bookmark important sections
- Complete quizzes and assessments
- Mark lessons as complete
- Access downloadable resources

Think of it as Netflix for learning - a focused, immersive interface designed to maximize learning retention and engagement.

## URL Structure

```
/academy/learn/[slug]                    # Course overview/player landing
/academy/learn/[slug]/lessons/[lessonId] # Specific lesson view
/academy/learn/[slug]/quiz/[quizId]      # Assessment/quiz interface
```

Alternative routes (for backwards compatibility):
```
/academy/courses/[slug]/learn            # Redirect to /academy/learn/[slug]
```

## User Stories

### As a Learner, I want to:
1. **Resume Learning** - Pick up exactly where I left off in a course
2. **Navigate Easily** - Move between lessons without losing my place
3. **Track Progress** - See how much of the course I've completed
4. **Watch at My Pace** - Control video playback speed, pause, rewind
5. **Take Notes** - Write notes while learning without switching apps
6. **Complete Assessments** - Take quizzes to test my understanding
7. **Download Resources** - Access course materials offline
8. **Mark Complete** - Manually mark lessons done if I already know the content

## Core Components

### 1. Course Player Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│  Header: Course Title + Exit Button                                 │
├──────────────────────────────────────┬──────────────────────────────┤
│                                      │                              │
│                                      │    Lesson Sidebar            │
│        Main Content Area             │    ────────────────          │
│                                      │    Module 1                  │
│   ┌─────────────────────────────┐   │    ├─ ✓ Lesson 1             │
│   │                             │   │    ├─ ✓ Lesson 2             │
│   │       Video Player          │   │    └─ ● Lesson 3 (current)   │
│   │                             │   │                              │
│   └─────────────────────────────┘   │    Module 2                  │
│                                      │    ├─ ○ Lesson 4             │
│   Lesson Title                       │    └─ ○ Lesson 5             │
│   Lesson Description                 │                              │
│                                      │    ────────────────          │
│   [Mark Complete] [Next Lesson →]   │    Progress: 45% complete    │
│                                      │                              │
├──────────────────────────────────────┴──────────────────────────────┤
│  Tab Bar: Overview | Resources | Notes | Discussion                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Tab Content Area (e.g., Notes, Resources, Discussion)             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 2. Component Hierarchy

```
CoursePlayer/
├── CoursePlayerLayout.tsx        # Main layout wrapper
├── CoursePlayerHeader.tsx        # Top bar with title and navigation
├── MainContent/
│   ├── VideoPlayer.tsx           # YouTube integration (EXISTS)
│   ├── TextLesson.tsx            # Rich text lesson content
│   ├── QuizLesson.tsx            # Quiz/assessment interface
│   └── ResourceLesson.tsx        # Downloadable resource display
├── LessonSidebar/
│   ├── LessonSidebar.tsx         # Collapsible sidebar
│   ├── ModuleAccordion.tsx       # Module with lessons
│   ├── LessonItem.tsx            # Individual lesson row
│   └── ProgressSummary.tsx       # Overall progress display
├── LessonControls/
│   ├── MarkCompleteButton.tsx    # Manual completion
│   ├── NextLessonButton.tsx      # Navigate to next
│   └── PrevLessonButton.tsx      # Navigate to previous
├── TabContent/
│   ├── LessonOverview.tsx        # Lesson description, objectives
│   ├── LessonResources.tsx       # Downloadable files
│   ├── LessonNotes.tsx           # User note-taking
│   └── LessonDiscussion.tsx      # Comments/Q&A
└── hooks/
    ├── useCoursePlayer.ts        # Main course player state
    ├── useLessonProgress.ts      # Progress tracking
    ├── useLessonNavigation.ts    # Navigation between lessons
    └── useLessonNotes.ts         # Note-taking functionality
```

## Existing Components

These components already exist and can be used:

| Component | Path | Status |
|-----------|------|--------|
| `VideoPlayer` | `frontend/src/components/academy/VideoPlayer.tsx` | ✅ Exists |
| `ContinueLearningSection` | `frontend/src/components/academy/ContinueLearningSection.tsx` | ✅ Exists |
| `DocumentViewer` | `frontend/src/components/academy/DocumentViewer.tsx` | ✅ Exists |
| `DocumentPreviewModal` | `frontend/src/components/academy/DocumentPreviewModal.tsx` | ✅ Exists |

## Data Models

### Backend Models (Django)

**Lesson** (`backend/apps/training/models.py:193`):
- `id`, `title`, `slug`, `description`
- `module` (FK to Module)
- `order` (position in module)
- `lesson_type` (video, text, quiz, resource)
- `video_url`, `content_html`, `duration`
- `is_preview` (free preview available)

**LessonProgress** (`backend/apps/training/models.py:348`):
- `enrollment` (FK)
- `lesson` (FK)
- `is_completed`
- `completed_at`
- `watch_time` (seconds watched)
- `last_position` (resume point)

**Enrollment** (`backend/apps/training/models.py:267`):
- `user` (FK)
- `course` (FK)
- `enrolled_at`
- `completed_at`
- `progress_percent`

### Frontend Types

```typescript
// lib/types/academy/course-player.ts

export interface CoursePlayerData {
  course: CourseDetail;
  enrollment: Enrollment;
  modules: ModuleWithLessons[];
  currentLesson: Lesson | null;
  progress: CourseProgress;
}

export interface Lesson {
  id: number;
  title: string;
  slug: string;
  description: string;
  lessonType: 'video' | 'text' | 'quiz' | 'resource';
  videoUrl?: string;
  contentHtml?: string;
  duration?: number;
  order: number;
  isPreview: boolean;
  isCompleted: boolean;
  lastPosition?: number;
}

export interface ModuleWithLessons {
  id: number;
  title: string;
  order: number;
  lessons: Lesson[];
  lessonsCompleted: number;
  totalLessons: number;
}

export interface CourseProgress {
  enrollmentId: number;
  progressPercent: number;
  lessonsCompleted: number;
  totalLessons: number;
  currentLessonId: number | null;
  lastAccessedAt: string;
}

export interface LessonNote {
  id: number;
  lessonId: number;
  content: string;
  timestamp?: number; // Video timestamp
  createdAt: string;
  updatedAt: string;
}
```

## API Endpoints

### Required Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/training/learn/{slug}` | Get course player data (course, modules, lessons, progress) |
| GET | `/api/training/learn/{slug}/lessons/{lessonId}` | Get specific lesson content |
| POST | `/api/training/learn/{slug}/lessons/{lessonId}/progress` | Update lesson progress |
| POST | `/api/training/learn/{slug}/lessons/{lessonId}/complete` | Mark lesson complete |
| GET | `/api/training/learn/{slug}/quiz/{quizId}` | Get quiz questions |
| POST | `/api/training/learn/{slug}/quiz/{quizId}/submit` | Submit quiz answers |
| GET | `/api/training/learn/{slug}/notes` | Get user's notes for course |
| POST | `/api/training/learn/{slug}/notes` | Create/update note |
| DELETE | `/api/training/learn/{slug}/notes/{noteId}` | Delete note |

### Response Schemas

```python
# Course Player Data Response
class CoursePlayerDataSchema(Schema):
    course: CourseDetailSchema
    enrollment: EnrollmentSchema
    modules: list[ModuleWithLessonsSchema]
    current_lesson: LessonDetailSchema | None
    progress: CourseProgressSchema

# Lesson Detail Response
class LessonDetailSchema(Schema):
    id: int
    title: str
    slug: str
    description: str
    lesson_type: str  # 'video', 'text', 'quiz', 'resource'
    video_url: str | None
    content_html: str | None
    duration: int | None
    order: int
    is_preview: bool
    is_completed: bool
    last_position: int | None
    resources: list[ResourceSchema]
```

## User Interactions

### Video Playback
1. **Auto-play**: Next lesson auto-plays when current ends (configurable)
2. **Resume**: Video resumes from last watched position
3. **Speed Control**: 0.5x, 0.75x, 1x, 1.25x, 1.5x, 1.75x, 2x
4. **Auto-Complete**: Lesson marked complete at 90% watch time
5. **Keyboard Shortcuts**: Space (play/pause), M (mute), F (fullscreen)

### Progress Tracking
1. **Auto-Save**: Progress saved every 30 seconds during video
2. **Manual Complete**: "Mark as Complete" button for known content
3. **Module Unlock**: Next module unlocks when previous completes (optional)
4. **Certificate**: Certificate available when 100% complete

### Navigation
1. **Sidebar Navigation**: Click any lesson to jump
2. **Next/Previous**: Buttons below video
3. **Keyboard**: Arrow keys for next/prev
4. **Mobile Swipe**: Swipe for next/prev on mobile

### Note-Taking
1. **Timestamped Notes**: Notes linked to video timestamp
2. **Auto-Save**: Notes save as user types (debounced)
3. **Export**: Export all notes as PDF/Markdown
4. **Search**: Search within notes

## UI/UX Specifications

### Layout
- **Desktop**: Two-column layout (content + sidebar)
- **Tablet**: Collapsible sidebar
- **Mobile**: Full-width content, bottom sheet for navigation

### Visual Design
- **Primary Color**: Negosyo Blue (`#0056D2`)
- **Completed Lessons**: Green checkmark icon
- **Current Lesson**: Blue highlight
- **Locked Lessons**: Gray with lock icon
- **Progress Bar**: Blue gradient

### Accessibility
- **Keyboard Navigation**: Full keyboard support
- **Screen Reader**: ARIA labels on all interactive elements
- **Captions**: Support for video captions (YouTube CC)
- **Focus Management**: Focus returns to content after modal close
- **Contrast**: WCAG AA compliant color contrast

### Performance
- **Lazy Loading**: Load lesson content on demand
- **Video Preload**: Preload next lesson video
- **Skeleton Loading**: Show skeleton while loading
- **Offline Indicator**: Show when connection lost

## Implementation Priority

### Phase 1: Core Player (P0)
- [ ] Course player page layout
- [ ] Lesson sidebar with module navigation
- [ ] Video player integration (use existing)
- [ ] Progress tracking (auto-save)
- [ ] Mark complete functionality
- [ ] Next/previous navigation

### Phase 2: Content Types (P0)
- [ ] Text lesson display
- [ ] Resource/download display
- [ ] Basic quiz interface
- [ ] Lesson overview tab

### Phase 3: Engagement (P1)
- [ ] Note-taking functionality
- [ ] Resources tab with downloads
- [ ] Discussion/comments tab
- [ ] Keyboard shortcuts

### Phase 4: Polish (P2)
- [ ] Auto-play next lesson
- [ ] Resume from last position
- [ ] Lesson bookmarking
- [ ] Certificate integration
- [ ] Mobile-optimized view

## File Structure

```
frontend/src/
├── app/(academy)/academy/
│   └── learn/
│       ├── [slug]/
│       │   ├── page.tsx              # Course player main page
│       │   ├── layout.tsx            # Player-specific layout
│       │   ├── lessons/
│       │   │   └── [lessonId]/
│       │   │       └── page.tsx      # Direct lesson URL
│       │   └── quiz/
│       │       └── [quizId]/
│       │           └── page.tsx      # Quiz interface
│       └── _components/
│           ├── CoursePlayerLayout.tsx
│           ├── LessonSidebar.tsx
│           ├── LessonContent.tsx
│           ├── LessonControls.tsx
│           ├── ModuleAccordion.tsx
│           ├── LessonItem.tsx
│           ├── ProgressSummary.tsx
│           ├── LessonTabs.tsx
│           ├── NotesPanel.tsx
│           ├── ResourcesPanel.tsx
│           └── DiscussionPanel.tsx
├── components/academy/
│   ├── VideoPlayer.tsx               # (EXISTS)
│   ├── TextLesson.tsx
│   ├── QuizInterface.tsx
│   └── ProgressBar.tsx
└── lib/
    ├── hooks/academy/
    │   ├── useCoursePlayer.ts
    │   ├── useLessonProgress.ts
    │   └── useLessonNotes.ts
    ├── services/academy/
    │   └── course-player.service.ts
    └── types/academy/
        └── course-player.ts
```

## Related Features

| Feature | Description | Status |
|---------|-------------|--------|
| My Learning Dashboard | Shows enrolled courses with progress | ✅ Implemented |
| Course Detail Page | Pre-enrollment course info | ✅ Implemented |
| Certificate View | Certificate after completion | 🚧 Partial |
| Quiz Engine | Assessment functionality | ❌ Not Started |

## Success Metrics

- **Lesson Completion Rate**: % of started lessons that are completed
- **Course Completion Rate**: % of enrollments that complete all lessons
- **Engagement Time**: Average time spent in course player per session
- **Video Completion Rate**: % of video watched before navigating away
- **Note Creation Rate**: % of learners who create at least one note
- **Resume Rate**: % of learners who return to continue a course

## Implementation Status

*Audited: December 30, 2025*

### Frontend Pages
| Page | Status | Path | Notes |
|------|--------|------|-------|
| Course Player Main | ❌ Not Implemented | `frontend/src/app/(academy)/academy/learn/[slug]/page.tsx` | Core page missing |
| Lesson View | ❌ Not Implemented | `frontend/src/app/(academy)/academy/learn/[slug]/lessons/[lessonId]/page.tsx` | Direct lesson URL |
| Quiz Interface | ❌ Not Implemented | `frontend/src/app/(academy)/academy/learn/[slug]/quiz/[quizId]/page.tsx` | Assessment UI |

### Components
| Component | Status | Path | Notes |
|-----------|--------|------|-------|
| VideoPlayer | ✅ Exists | `frontend/src/components/academy/VideoPlayer.tsx` | Full-featured with progress tracking |
| DocumentViewer | ✅ Exists | `frontend/src/components/academy/DocumentViewer.tsx` | For PDF/doc resources |
| LessonSidebar | ❌ Missing | - | Navigation sidebar |
| TextLesson | ❌ Missing | - | Rich text content display |
| QuizInterface | ❌ Missing | - | Quiz taking UI |
| NotesPanel | ❌ Missing | - | Note-taking functionality |

### Backend APIs
| Endpoint | Status | Notes |
|----------|--------|-------|
| GET lesson content | ✅ Exists | Via training API |
| POST lesson progress | ✅ Exists | `LessonProgressUpdateSchema` |
| POST mark complete | 🚧 Partial | Needs dedicated endpoint |
| GET/POST notes | ❌ Missing | Note-taking API |
| Quiz submission | ❌ Missing | Assessment API |

### Overall Progress
- **Frontend Pages**: 0/3 (0%)
- **Components**: 2/6 (33%)
- **Backend APIs**: 2/5 (40%)

---

## References

- [Learner Role](/Users/saidamenmambayao/apps/csea/.gemini/skills/ui-ux/references/ideal-user-journeys/moroacademy/roles/learner.md)
- [Learning Journey](/Users/saidamenmambayao/apps/csea/.gemini/skills/ui-ux/references/ideal-user-journeys/moroacademy/journeys/learning.md)
- [VideoPlayer Component](/Users/saidamenmambayao/apps/csea/frontend/src/components/academy/VideoPlayer.tsx)
