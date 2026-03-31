# Facilitator Control - Live Workshop Locking System

## Overview

The Facilitator Control system enables real-time content locking during live workshop facilitation. Facilitators can control the pace of learning by locking/unlocking modules, sessions, and individual slides, preventing participants from reading ahead.

**Location**: Integrated into the **top-right toolbar** of PresentationMode, beside the Home icon.

## Toolbar Integration

Facilitator controls are displayed in the top-right toolbar for easy access during presentations:

```
[1/15 | 🛡️ 🔒M 🔒S 🔒Slide | 🏠 | ⛶]
         ↑ Facilitator Controls (only visible to facilitators)
```

| Element | Description |
|---------|-------------|
| 🛡️ Shield Icon | Indicates facilitator mode is active |
| M | Module lock toggle (red when locked) |
| S | Session lock toggle (red when locked) |
| Slide | Current slide lock toggle (red when locked) |

**Visibility**: Only users with `admin`, `content_manager`, or `superuser` roles see these controls.

## Lock Hierarchy

```
Workshop/Program
└── Module (lockable)
    └── Session (lockable)
        └── Section/Slide (lockable)
```

### Lock Levels

| Level | Scope | Effect | Use Case |
|-------|-------|--------|----------|
| **Module** | All sessions in module | Blocks entire module | "We'll cover Module 3 tomorrow" |
| **Session** | All sections in session | Blocks one session | "Let's focus on Session 2.1" |
| **Section** | Single slide | Blocks one slide | "Don't scroll past this" |

### Lock Precedence

Locks cascade down: If a module is locked, all its sessions and sections are locked regardless of their individual states.

```
Module LOCKED → All sessions LOCKED → All sections LOCKED
Module UNLOCKED → Check session lock → Check section lock
```

---

## Architecture

### Frontend Components

#### 1. EDPContext (`/frontend/src/contexts/EDPContext.tsx`)

Central state management for lock states:

```tsx
interface EDPContextType {
  // Lock states
  isModuleLocked: boolean
  isSessionLocked: boolean
  lockedSections: string[]
  setLockStates: (states: LockStates) => void

  // Facilitator mode
  isFacilitator: boolean
  setIsFacilitator: (is: boolean) => void

  // Presentation mode
  isPresentationMode: boolean
  setIsPresentationMode: (is: boolean) => void

  // Sidebar state
  isSidebarOpen: boolean
  setIsSidebarOpen: (is: boolean) => void
}
```

#### 2. TopRightControls (`/frontend/src/components/academy/PresentationMode.tsx`)

Facilitator controls integrated into the top-right toolbar:

```tsx
function TopRightControls({
  currentIndex,
  totalSections,
  isFullscreen,
  onToggleFullscreen,
  exitUrl,
  isFacilitator = false,
  isModuleLocked = false,
  isSessionLocked = false,
  lockedSections = [],
  activeSectionId,
  onToggleLock,
}: TopRightControlsProps) {
  return (
    <motion.div className="fixed top-4 right-4 z-50 flex items-center gap-1 bg-white/95 ...">
      {/* Page indicator */}
      <div className="px-3">{currentIndex + 1} / {totalSections}</div>

      {/* Facilitator Controls */}
      {isFacilitator && onToggleLock && (
        <>
          <Shield className="w-3 h-3 text-[var(--negosyo-blue)]" />
          <Button onClick={() => onToggleLock('module')}>
            {isModuleLocked ? <Lock /> : <Unlock />} M
          </Button>
          <Button onClick={() => onToggleLock('session')}>
            {isSessionLocked ? <Lock /> : <Unlock />} S
          </Button>
          {activeSectionId && (
            <Button onClick={() => onToggleLock('section')}>
              {lockedSections.includes(activeSectionId) ? <Lock /> : <Unlock />} Slide
            </Button>
          )}
        </>
      )}

      {/* Home + Fullscreen */}
      <Link href={exitUrl}><Home /></Link>
      <Button onClick={onToggleFullscreen}>{isFullscreen ? <Minimize /> : <Maximize />}</Button>
    </motion.div>
  )
}
```

The `PresentationMode` component:
- Fetches program data and syncs lock states
- Implements `handleToggleLock` for API calls
- Passes facilitator props to `TopRightControls`

#### 3. FullPageSection (`/frontend/src/app/(academy)/academy/edp/_components/EDPContent.tsx`)

Handles locked content display:

```tsx
const isLocked = !isFacilitator && (
  isModuleLocked ||
  isSessionLocked ||
  (id && lockedSections.includes(id))
)

return (
  <section>
    <div className={cn(
      isLocked ? "blur-2xl opacity-20 scale-95" : "blur-0 opacity-100"
    )}>
      {children}
    </div>

    {isLocked && (
      <div className="absolute inset-0 flex items-center justify-center">
        <Lock className="w-12 h-12 text-red-500" />
        <h2>Content Locked</h2>
        <p>Please wait for the facilitator to unlock this content.</p>
      </div>
    )}
  </section>
)
```

---

## Backend API

### Models

```python
# backend/apps/training/models.py

class ProgramModule(models.Model):
    program = models.ForeignKey(WorkshopProgram, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    module_number = models.PositiveIntegerField()
    is_locked = models.BooleanField(default=True)  # Locked by default

class ModuleSession(models.Model):
    module = models.ForeignKey(ProgramModule, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    session_code = models.CharField(max_length=20)
    is_locked = models.BooleanField(default=True)  # Locked by default
    locked_sections = models.JSONField(default=list)  # ["intro", "concept"]
```

### API Endpoints

#### Get Program with Lock States

```
GET /api/training/programs/{slug}/
```

Response:
```json
{
  "id": 1,
  "title": "Enterprise Development Program",
  "slug": "enterprise-development-program-edp",
  "days": [
    {
      "day_number": 1,
      "modules": [
        {
          "id": 101,
          "module_number": 1,
          "title": "Ideation",
          "is_locked": false,
          "sessions": [
            {
              "id": 201,
              "session_code": "1.1",
              "title": "Entrepreneurship",
              "is_locked": false,
              "locked_sections": []
            }
          ]
        }
      ]
    }
  ]
}
```

#### Update Module Lock

```
PATCH /api/training/modules/{id}/
Content-Type: application/json

{
  "is_locked": true
}
```

#### Update Session Lock

```
PATCH /api/training/sessions/{id}/
Content-Type: application/json

{
  "is_locked": true,
  "locked_sections": ["activity", "takeaway"]
}
```

---

## Implementation Guide

### Step 1: Add Lock Fields to Models

```python
# In your migration
class Migration(migrations.Migration):
    operations = [
        migrations.AddField(
            model_name='programmodule',
            name='is_locked',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='modulesession',
            name='is_locked',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='modulesession',
            name='locked_sections',
            field=models.JSONField(default=list),
        ),
    ]
```

### Step 2: Create API Endpoints

```python
# backend/apps/training/api.py

@router.patch("/modules/{module_id}/")
def update_module(request, module_id: int, payload: ModuleUpdateSchema):
    module = get_object_or_404(ProgramModule, id=module_id)
    if payload.is_locked is not None:
        module.is_locked = payload.is_locked
    module.save()
    return {"success": True}

@router.patch("/sessions/{session_id}/")
def update_session(request, session_id: int, payload: SessionUpdateSchema):
    session = get_object_or_404(ModuleSession, id=session_id)
    if payload.is_locked is not None:
        session.is_locked = payload.is_locked
    if payload.locked_sections is not None:
        session.locked_sections = payload.locked_sections
    session.save()
    return {"success": True}
```

### Step 3: Frontend Service Functions

```typescript
// frontend/src/lib/services/workshop-program.service.ts

export async function updateProgramModule(
  moduleId: number,
  data: { is_locked?: boolean }
): Promise<void> {
  await apiClient.patch(`/training/modules/${moduleId}/`, data)
}

export async function updateModuleSession(
  sessionId: number,
  data: { is_locked?: boolean; locked_sections?: string[] }
): Promise<void> {
  await apiClient.patch(`/training/sessions/${sessionId}/`, data)
}
```

### Step 4: Sync Lock States

```typescript
// In layout component
useEffect(() => {
  const fetchProgram = async () => {
    const data = await getPublicProgram('your-program-slug')
    setProgram(data)
  }

  fetchProgram()

  // Poll every 30 seconds for real-time updates
  const interval = setInterval(fetchProgram, 30000)
  return () => clearInterval(interval)
}, [])
```

---

## Facilitator Roles

Users with these roles see the Facilitator Toolbar:

| Role | Access |
|------|--------|
| `admin` | Full facilitator control |
| `content_manager` | Full facilitator control |
| `superuser` | Full facilitator control |

```typescript
const isFacilitator = user?.role === 'admin' ||
                      user?.role === 'content_manager' ||
                      user?.isSuperuser
```

---

## UX Patterns

### Locked Content Display

1. **Blur Effect**: Content is heavily blurred (blur-2xl)
2. **Opacity Reduction**: Content fades to 20% opacity
3. **Scale Down**: Slight scale reduction (95%)
4. **Lock Overlay**: Centered lock icon with message
5. **Pointer Disabled**: No interaction possible

### Visual Feedback

| State | Visual |
|-------|--------|
| Locked | Red lock icon, "Content Locked" message |
| Unlocked | No overlay, full content visible |
| Lock Toggle | Button changes from Lock to Unlock icon |

### Toolbar States

```
Module Locked:    [🔒 Module] [🔒 Session] [🔒 Slide]
Module Unlocked:  [🔓 Module] [🔒 Session] [🔒 Slide]
Session Unlocked: [🔓 Module] [🔓 Session] [🔒 Slide]
All Unlocked:     [🔓 Module] [🔓 Session] [🔓 Slide]
```

---

## Best Practices

### For Facilitators

1. **Lock by default**: Start with everything locked
2. **Progressive unlock**: Unlock as you progress through content
3. **Section locking**: Use for interactive activities where you don't want participants reading ahead
4. **Re-lock after breaks**: Lock content during breaks to maintain control

### For Developers

1. **Default to locked**: New content should be locked by default
2. **Poll frequently**: 30-second polling ensures near-real-time updates
3. **Cache lock states**: Use context to avoid prop drilling
4. **Graceful degradation**: If API fails, assume locked state

---

## Troubleshooting

### Lock Not Syncing

1. Check API response includes lock fields
2. Verify polling interval is running
3. Check browser console for API errors
4. Ensure user has facilitator role

### Facilitator Toolbar Not Showing

1. Verify user role is admin/content_manager/superuser
2. Check `isFacilitator` calculation
3. Ensure program data is loaded

### Content Still Visible When Locked

1. Check `isLocked` calculation includes all levels
2. Verify `isFacilitator` is false for participants
3. Check CSS blur classes are applied
