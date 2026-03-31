# Tailwind CSS Patterns

Tailwind CSS v4 utilities for CSEA styling.

## Negosyo Blue Color Classes

```tsx
// Primary Blue
<div className="bg-negosyo-blue">Primary background</div>
<div className="text-negosyo-blue">Primary text</div>
<div className="border-negosyo-blue">Primary border</div>
<div className="hover:bg-negosyo-blue/90">Hover state</div>
<div className="bg-negosyo-blue/10">Light blue background</div>

// Focus rings
<Input className="focus-visible:ring-negosyo-blue" />
<Select className="focus:ring-negosyo-blue" />
```

## Responsive Layout

```tsx
// Grid system
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
  <Card />
</div>

// Container
<div className="container mx-auto px-4 sm:px-6 lg:px-8">
  {/* Content */}
</div>

// Flex layouts
<div className="flex flex-col md:flex-row gap-4">
  <div className="w-full md:w-1/3">Sidebar</div>
  <div className="flex-1">Main content</div>
</div>
```

## Buttons

```tsx
// Primary
<Button className="bg-negosyo-blue hover:bg-negosyo-blue/90 text-white">
  Primary Action
</Button>

// Secondary
<Button variant="outline" className="border-negosyo-blue text-negosyo-blue hover:bg-negosyo-blue/10">
  Secondary
</Button>

// Ghost
<Button variant="ghost" className="text-negosyo-blue hover:bg-negosyo-blue/10">
  Ghost
</Button>
```

## Cards

```tsx
// Standard card
<div className="bg-white rounded-lg shadow-md p-6">
  <h3 className="text-lg font-semibold text-gray-900">Title</h3>
  <p className="text-gray-600 mt-2">Content</p>
</div>

// Card with CSEA header
<div className="bg-white rounded-lg shadow-md overflow-hidden">
  <div className="bg-negosyo-blue px-6 py-4">
    <h3 className="text-white font-semibold">Header</h3>
  </div>
  <div className="p-6">Content</div>
</div>
```

## Status Badges

```tsx
// Success
<span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-100 text-emerald-800">
  Active
</span>

// Warning
<span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-orange-100 text-orange-800">
  Pending
</span>

// Error
<span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800">
  Expired
</span>

// Info
<span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
  Processing
</span>
```

## Forms

```tsx
<div className="space-y-2">
  <label className="block text-sm font-medium text-gray-700">
    Name <span className="text-red-600">*</span>
  </label>
  <input
    type="text"
    className="w-full rounded-md border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-negosyo-blue focus:border-transparent"
  />
  <p className="text-sm text-gray-500">Helper text</p>
</div>
```

## Typography

```tsx
<h1 className="text-4xl font-bold text-gray-900">Heading 1</h1>
<h2 className="text-3xl font-bold text-gray-900">Heading 2</h2>
<h3 className="text-2xl font-semibold text-gray-900">Heading 3</h3>
<p className="text-base text-gray-700">Body text</p>
<p className="text-sm text-gray-600">Small text</p>
<p className="text-xs text-gray-500">Extra small</p>
```

## Spacing Scale

```tsx
// 4px increments: 1, 2, 3, 4, 5, 6, 8, 10, 12
<div className="p-4">16px padding</div>
<div className="p-6">24px padding</div>
<div className="gap-4">16px gap</div>
<div className="space-y-6">24px vertical spacing</div>
```

