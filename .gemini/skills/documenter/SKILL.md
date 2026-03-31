---
name: documenter
description: |
  Transform markdown (.md) documentation files into pure React JSX components within the BPMP frontend.
  NO runtime markdown parsing - all markdown is converted to React elements at build time.
  Use when: (1) converting docs/ markdown files to React pages, (2) updating existing doc pages,
  (3) generating/updating documentation index with grouped navigation,
  (4) packaging outputs from other skills into documentation pages.
  For PDF-to-markdown transcription/OCR, use the /transcriber skill.
  Output is pure React - ZERO markdown syntax, ZERO react-markdown runtime. (project)
argument-hint: "[topic]"
---

# Documenter Skill

Transform markdown documentation into pure React JSX components - **NO runtime markdown parsing**.

> **Note**: PDF-to-markdown transcription and OCR extraction is owned by the [`/transcriber`](../transcriber/skill.md) skill. Use `/transcriber` for extracting text from PDFs.

## Architecture: Markdown -> React JSX (Build Time)

```
.md file -> /documenter -> .tsx file (React JSX) -> renders as pure React
```

**NOT this (old approach):**
```
.md file -> .ts file (markdown string) -> react-markdown at runtime
```

## Critical: Pure React Output

**Content files export React components, NOT markdown strings.**

Every markdown element becomes a React JSX element:

| Markdown | React JSX Output |
|----------|------------------|
| `# Heading` | `<h1 className="...">Heading</h1>` |
| `## Heading` | `<Section title="Heading">` |
| `**bold**` | `<strong>bold</strong>` |
| `- item` | `<ul><li>item</li></ul>` with icons |
| `| table |` | `<Table>` component with styling |
| ``` code ``` | `<CodeBlock lang="...">` component |
| Tree structures | `<TreeList>` component with nested items |
| Flowcharts | `<Diagram>` component |

## Content File Pattern (.tsx)

Content files are React components that return JSX:

```tsx
// frontend/src/pages/documentation/content/{group}/{doc-name}.tsx
import { Section, Table, CodeBlock, TreeList, Diagram } from '../../components';

export const meta = {
  title: 'Document Title',
  group: 'architecture',
  docName: 'doc-name',
  description: 'Brief description',
  lastUpdated: '2026-01-07',
  version: '1.0',
  module: 'Module Name',
  portal: 'Parliament Portal',
  status: 'Architecture'
};

export const Content = () => (
  <>
    <Section title="Module Overview" level={2}>
      <p>Paragraph text here as JSX.</p>
      <Section title="Purpose" level={3}>
        <p>The module enables...</p>
      </Section>
      <Section title="Primary Users" level={3}>
        <Table
          headers={['Role', 'Responsibilities']}
          rows={[['MPs', 'Strategic oversight'], ['Staff', 'Operations']]}
        />
      </Section>
    </Section>
  </>
);
```

## Documentation Components

Reusable components in `frontend/src/pages/documentation/components/`: Section, Table, TreeList, CodeBlock, Diagram, HeroSection.

For full component source code and interfaces, see: [references/documentation-components.md](references/documentation-components.md)

## Transformation Rules

Rules for converting each markdown element (headings, tables, tree structures, diagrams, code blocks, lists, bold text) to React JSX.

For detailed rules with before/after examples, see: [references/transformation-rules.md](references/transformation-rules.md)

## File Structure

```
frontend/src/pages/documentation/
├── DocumentationLayout.tsx        # Layout wrapper (hero, TOC, footer)
├── DocumentationIndexPage.tsx     # Index at /documentation
├── components/                    # Reusable doc components
│   ├── index.ts                   # Barrel export
│   ├── Section.tsx
│   ├── Table.tsx
│   ├── TreeList.tsx
│   ├── CodeBlock.tsx
│   ├── Diagram.tsx
│   └── HeroSection.tsx
├── content/                       # Content as React components
│   └── architecture/
│       └── arch-parliament-representation.tsx
└── pages/                         # Page wrappers
    └── architecture/
        └── ArchParliamentRepresentationPage.tsx
```

## Workflow

### 1. Create Mode (New Documentation)

1. **Read markdown file** - Parse all content
2. **Transform to JSX** - Convert every element to React
3. **Generate content file** - Create `.tsx` with React component
4. **Generate page wrapper** - Create page that imports content
5. **Update index** - Add navigation entry
6. **Update routes** - Add route to App.tsx

### 2. Update Mode (Automatic Sync)

When `/documenter` is invoked to update a `.md` file, the corresponding React page is **automatically regenerated**.

```
/documenter docs/architecture/overview.md --edit "Add API section"
```

**Workflow:**
1. **Edit source .md** - Apply requested changes to markdown file
2. **Re-transform to JSX** - Convert updated markdown to React components
3. **Regenerate content file** - Overwrite `.tsx` with new JSX
4. **Sync complete** - React page now reflects the updated documentation

**Key Principle:** Source `.md` and React `.tsx` are always in sync. Editing the markdown automatically updates the React page - no manual step required.

**Examples:**
```
# Edit existing documentation
/documenter docs/architecture/overview.md --edit "Update the API endpoints section"

# Update after external .md changes
/documenter docs/architecture/overview.md --sync

# Batch sync all docs in a directory
/documenter docs/architecture/ --sync-all
```

## Design Conventions

- **Primary**: BPMP Blue (#0056D2)
- **Accent**: Emerald (#10B981)
- **No purple colors**
- **Icons**: lucide-react (no emojis)
- **Styling**: Tailwind CSS v4

## Quick Start

### Create New Documentation Page
```
/documenter docs/architecture/my-doc.md
```
Creates:
- Content: `content/architecture/my-doc.tsx` (React component)
- Page: `pages/architecture/MyDocPage.tsx` (wrapper)
- Route: `/documentation/architecture/my-doc`

### Edit & Sync Existing Documentation
```
/documenter docs/architecture/my-doc.md --edit "Add new section about caching"
```
- Edits the source `.md` file
- Automatically regenerates the `.tsx` React page

### Sync After External Changes
```
/documenter docs/architecture/my-doc.md --sync
```
- Reads updated `.md` file
- Regenerates the `.tsx` React page to match

---

> **PDF Transcription**: For transcribing PDFs to markdown (OCR extraction of government plans, legal documents, reports), use the [`/transcriber`](../transcriber/skill.md) skill instead.
