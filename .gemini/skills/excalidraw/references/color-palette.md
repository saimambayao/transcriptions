# BARMM Excalidraw Color Palette

Institutional colors for Bangsamoro Government diagrams. Apply consistently across all Excalidraw outputs.

## Primary Colors

| Role | Hex | RGB | Excalidraw Usage |
|------|-----|-----|------------------|
| **Navy** (Primary) | `#1B365D` | 27, 54, 93 | Main node backgrounds, frames, primary elements |
| **Gold** (Accent) | `#C5A54E` | 197, 165, 78 | Decision diamonds, highlights, key connectors, emphasis |
| **Slate** (Secondary) | `#2C5F7C` | 44, 95, 124 | Secondary nodes, supporting elements, alternate groups |
| **Body** (Text) | `#2D2D2D` | 45, 45, 45 | All text labels, descriptions, annotations |

## Supporting Colors

| Role | Hex | Usage |
|------|-----|-------|
| **White** | `#FFFFFF` | Canvas background, text on dark fills |
| **Light Gray** | `#E8EDF2` | Subtle backgrounds, inactive elements |
| **Dark Gray** | `#D4DAE2` | Borders on light elements |
| **Success Green** | `#4A7C59` | Approval states, completed steps |
| **Warning Amber** | `#D4A843` | Caution states, pending items (gold variant) |
| **Error Red** | `#8B3A3A` | Rejection states, blockers, critical items |

## Application Rules

- **Primary nodes** (main process steps): Navy fill, white text
- **Secondary nodes** (supporting steps): Slate fill, white text
- **Decision points**: Gold fill, dark text
- **Connectors/arrows**: Gold stroke on dark backgrounds, Navy stroke on light backgrounds
- **Frames/groups**: Navy stroke with transparent fill
- **Annotations/callouts**: Light Gray fill, Body text
- **Alternate between Navy and Slate** for adjacent groups to create visual hierarchy

## Element Defaults

```
strokeColor: "#1B365D"     (Navy)
backgroundColor: "#1B365D"  (Navy for primary)
fillStyle: "solid"
strokeWidth: 2
roughness: 0               (clean lines for government documents)
opacity: 100
fontSize: 16
fontFamily: 1              (Virgil/hand-drawn)
textAlign: "center"
```

## Roughness Guidelines

| Context | Roughness | Why |
|---------|-----------|-----|
| Government/formal documents | `0` | Clean, professional look |
| Training materials | `1` | Approachable, less formal |
| Brainstorming/drafts | `2` | Hand-drawn, informal |
