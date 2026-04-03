# Markdown to React JSX Transformation Rules

Detailed rules and examples for converting `.md` elements to `.tsx` React JSX.

## 1. Headings
```markdown
## 1. Module Overview
### 1.1 Purpose
```
->
```tsx
<Section title="1. Module Overview" level={2}>
  <Section title="1.1 Purpose" level={3}>
```

## 2. Tables
```markdown
| Col1 | Col2 |
|------|------|
| A    | B    |
```
->
```tsx
<Table
  headers={['Col1', 'Col2']}
  rows={[['A', 'B']]}
/>
```

## 3. Tree Structures
```markdown
```
Module
├── Component A
├── Component B
└── Component C
```
```
->
```tsx
<TreeList
  title="Module"
  items={['Component A', 'Component B', 'Component C']}
/>
```

## 4. Flowcharts/Diagrams
```markdown
```
[A] -> [B] -> [C]
    |
   [D]
```
```
->
```tsx
<Diagram>
  {`[A] -> [B] -> [C]
      |
     [D]`}
</Diagram>
```

## 5. Code Blocks
```markdown
```python
class MyClass:
    pass
```
```
->
```tsx
<CodeBlock language="python">
  {`class MyClass:
    pass`}
</CodeBlock>
```

## 6. Lists
```markdown
- Item one
- Item two
- Item three
```
->
```tsx
<ul className="space-y-2 my-4">
  <li className="flex items-start gap-2">
    <CheckCircle2 size={16} className="text-emerald-500 mt-0.5" />
    <span>Item one</span>
  </li>
  ...
</ul>
```

## 7. Bold Text
```markdown
**Important text**
```
->
```tsx
<strong className="font-semibold text-slate-800">Important text</strong>
```
