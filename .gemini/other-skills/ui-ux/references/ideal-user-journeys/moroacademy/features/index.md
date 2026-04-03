# MoroAcademy Features

Feature specifications for core MoroAcademy LMS functionality.

## Feature Specifications

| Feature | Description | Status | Priority |
|---------|-------------|--------|----------|
| [Course Player](./course-player.md) | Main learning interface for enrolled learners | ❌ Not Implemented | P0 |

## Feature Categories

### Learning Experience (Learner-Facing)
- **Course Player** - Video playback, lesson navigation, progress tracking
- **Quiz Engine** - Assessment taking interface (planned)
- **Certificate Viewer** - Certificate display and download (partial)
- **Note-Taking** - In-lesson note functionality (planned)

### Content Management (Instructor-Facing)
- **Course Builder** - Drag-drop course creation (partial - admin exists)
- **Quiz Builder** - Assessment creation interface (planned)
- **Resource Manager** - File upload and management (partial)

### Platform Features
- **Live Workshops** - Real-time training sessions (implemented via programs)
- **Access Codes** - Registration via access codes (implemented)
- **Provider Profiles** - Training provider pages (implemented)

## Directory Structure

```
features/
├── index.md              # This file
├── course-player.md      # Course player specification
├── quiz-engine.md        # (Planned) Quiz/assessment system
├── certificate-system.md # (Planned) Certificate generation
└── note-taking.md        # (Planned) Note functionality
```

## Related Documentation

- [Journeys](../journeys/) - User journey maps
- [Roles](../roles/) - User role definitions
