# Documentation Components Reference

Reusable React components for the documentation system, located in `frontend/src/pages/documentation/components/`.

## Section Component
```tsx
// Section.tsx
interface SectionProps {
  title: string;
  level: 2 | 3 | 4;
  children: React.ReactNode;
}

export const Section = ({ title, level, children }: SectionProps) => {
  const Tag = `h${level}` as keyof JSX.IntrinsicElements;
  const styles = {
    2: 'text-2xl font-bold text-slate-800 border-l-4 border-[#0056D2] pl-4 mb-6',
    3: 'text-xl font-semibold text-slate-700 border-l-2 border-emerald-500 pl-3 mb-4',
    4: 'text-lg font-medium text-slate-600 mb-3',
  };

  return (
    <section className="mb-8">
      <Tag className={styles[level]}>{title}</Tag>
      <div className="mt-4">{children}</div>
    </section>
  );
};
```

## Table Component
```tsx
// Table.tsx
interface TableProps {
  headers: string[];
  rows: string[][];
}

export const Table = ({ headers, rows }: TableProps) => (
  <div className="overflow-x-auto rounded-lg border border-slate-200 my-4">
    <table className="w-full">
      <thead className="bg-slate-50">
        <tr>
          {headers.map((h, i) => (
            <th key={i} className="px-4 py-3 text-left text-xs font-semibold text-slate-600 uppercase">
              {h}
            </th>
          ))}
        </tr>
      </thead>
      <tbody className="divide-y divide-slate-200">
        {rows.map((row, i) => (
          <tr key={i} className="hover:bg-slate-50">
            {row.map((cell, j) => (
              <td key={j} className="px-4 py-3 text-sm text-slate-700">{cell}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);
```

## TreeList Component
```tsx
// TreeList.tsx
interface TreeListProps {
  title?: string;
  items: (string | { label: string; children?: string[] })[];
}

export const TreeList = ({ title, items }: TreeListProps) => (
  <div className="bg-slate-50 rounded-lg p-4 my-4 border border-slate-200">
    {title && <p className="font-semibold text-slate-800 mb-3">{title}</p>}
    <ul className="space-y-2">
      {items.map((item, i) => (
        <li key={i} className="flex items-start gap-2 text-slate-700">
          <CheckCircle2 size={16} className="text-emerald-500 mt-0.5 flex-shrink-0" />
          {typeof item === 'string' ? item : item.label}
        </li>
      ))}
    </ul>
  </div>
);
```

## CodeBlock Component
```tsx
// CodeBlock.tsx
interface CodeBlockProps {
  language?: string;
  children: string;
}

export const CodeBlock = ({ language, children }: CodeBlockProps) => (
  <div className="rounded-lg overflow-hidden my-4 border border-slate-200">
    {language && (
      <div className="bg-slate-800 px-4 py-2 flex items-center gap-2">
        <span className="w-3 h-3 rounded-full bg-red-500" />
        <span className="w-3 h-3 rounded-full bg-yellow-500" />
        <span className="w-3 h-3 rounded-full bg-green-500" />
        <span className="ml-2 text-xs text-slate-400 uppercase">{language}</span>
      </div>
    )}
    <pre className="bg-slate-900 p-4 overflow-x-auto">
      <code className="text-sm text-slate-100 font-mono">{children}</code>
    </pre>
  </div>
);
```

## Diagram Component
```tsx
// Diagram.tsx
interface DiagramProps {
  children: string;
}

export const Diagram = ({ children }: DiagramProps) => (
  <div className="rounded-lg overflow-hidden my-4 border border-slate-200">
    <div className="bg-slate-800 px-4 py-2 flex items-center gap-2">
      <GitBranch size={14} className="text-slate-400" />
      <span className="text-xs text-slate-400">Diagram</span>
    </div>
    <pre className="bg-slate-900 p-4 overflow-x-auto">
      <code className="text-sm text-emerald-400 font-mono whitespace-pre">{children}</code>
    </pre>
  </div>
);
```

## Page Component Pattern

```tsx
// frontend/src/pages/documentation/pages/{Group}/{DocName}Page.tsx
import DocumentationLayout from '../../DocumentationLayout';
import { Content, meta } from '../../content/{group}/{doc-name}';

const DocNamePage = () => (
  <DocumentationLayout meta={meta}>
    <Content />
  </DocumentationLayout>
);

export default DocNamePage;
```

## DocumentationLayout Component

The layout wrapper (replaces DocumentationPage.tsx):

```tsx
// frontend/src/pages/documentation/DocumentationLayout.tsx
interface DocumentationLayoutProps {
  meta: DocumentMeta;
  children: React.ReactNode;
}

const DocumentationLayout = ({ meta, children }: DocumentationLayoutProps) => (
  <div className="min-h-screen bg-slate-50">
    <HeroSection meta={meta} />
    <div className="max-w-7xl mx-auto px-6 py-12 flex gap-8">
      <main className="flex-1 bg-white rounded-xl p-8 shadow-sm">
        {children}
      </main>
      <TableOfContents />
    </div>
    <Footer />
  </div>
);
```
