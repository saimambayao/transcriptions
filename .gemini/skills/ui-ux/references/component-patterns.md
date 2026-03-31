# Component Patterns

Reusable UI component patterns for the Bangsamoro Development Platform using shadcn/ui and Tailwind CSS.

## Table of Contents
- [Cards](#cards)
- [Data Display](#data-display)
- [Feedback](#feedback)
- [Navigation](#navigation)
- [Overlays](#overlays)
- [Actions](#actions)

## Cards

### Product Card

```tsx
interface ProductCardProps {
  product: {
    id: string;
    name: string;
    price: number;
    image: string;
    seller: string;
    rating: number;
    reviewCount: number;
  };
}

export function ProductCard({ product }: ProductCardProps) {
  return (
    <Card className="overflow-hidden group">
      <div className="relative aspect-square">
        <Image
          src={product.image}
          alt={product.name}
          fill
          className="object-cover transition-transform group-hover:scale-105"
        />
        <Button
          variant="secondary"
          size="icon"
          className="absolute top-2 right-2 opacity-0 group-hover:opacity-100 transition-opacity"
        >
          <Heart className="h-4 w-4" />
        </Button>
      </div>

      <CardContent className="p-4">
        <p className="text-sm text-muted-foreground">{product.seller}</p>
        <h3 className="font-medium line-clamp-2 mt-1">{product.name}</h3>

        <div className="flex items-center gap-1 mt-2">
          <Star className="h-4 w-4 fill-yellow-400 text-yellow-400" />
          <span className="text-sm">{product.rating}</span>
          <span className="text-sm text-muted-foreground">
            ({product.reviewCount})
          </span>
        </div>

        <p className="text-lg font-semibold mt-2">
          PHP {product.price.toLocaleString()}
        </p>
      </CardContent>

      <CardFooter className="p-4 pt-0">
        <Button className="w-full">Add to Cart</Button>
      </CardFooter>
    </Card>
  );
}
```

### Stat Card

```tsx
interface StatCardProps {
  title: string;
  value: string | number;
  change?: {
    value: number;
    trend: 'up' | 'down' | 'neutral';
  };
  icon?: React.ElementType;
}

export function StatCard({ title, value, change, icon: Icon }: StatCardProps) {
  return (
    <Card>
      <CardContent className="p-6">
        <div className="flex items-center justify-between">
          <p className="text-sm font-medium text-muted-foreground">{title}</p>
          {Icon && (
            <div className="h-8 w-8 rounded-full bg-primary/10 flex items-center justify-center">
              <Icon className="h-4 w-4 text-primary" />
            </div>
          )}
        </div>

        <p className="text-2xl font-bold mt-2">{value}</p>

        {change && (
          <div className="flex items-center gap-1 mt-2">
            {change.trend === 'up' ? (
              <TrendingUp className="h-4 w-4 text-green-500" />
            ) : change.trend === 'down' ? (
              <TrendingDown className="h-4 w-4 text-red-500" />
            ) : (
              <Minus className="h-4 w-4 text-muted-foreground" />
            )}
            <span className={cn(
              "text-sm",
              change.trend === 'up' && "text-green-500",
              change.trend === 'down' && "text-red-500",
              change.trend === 'neutral' && "text-muted-foreground"
            )}>
              {change.value > 0 && '+'}{change.value}%
            </span>
            <span className="text-sm text-muted-foreground">from last month</span>
          </div>
        )}
      </CardContent>
    </Card>
  );
}
```

### Info Card

```tsx
interface InfoCardProps {
  title: string;
  description: string;
  icon?: React.ElementType;
  action?: {
    label: string;
    onClick: () => void;
  };
}

export function InfoCard({ title, description, icon: Icon, action }: InfoCardProps) {
  return (
    <Card className="bg-muted/50">
      <CardContent className="p-4 flex gap-4">
        {Icon && (
          <div className="h-10 w-10 rounded-full bg-primary/10 flex items-center justify-center shrink-0">
            <Icon className="h-5 w-5 text-primary" />
          </div>
        )}
        <div className="flex-1 min-w-0">
          <h4 className="font-medium">{title}</h4>
          <p className="text-sm text-muted-foreground mt-1">{description}</p>
          {action && (
            <Button variant="link" className="p-0 h-auto mt-2" onClick={action.onClick}>
              {action.label}
            </Button>
          )}
        </div>
      </CardContent>
    </Card>
  );
}
```

## Data Display

### Data Table with Actions

```tsx
export function DataTable<T>({
  columns,
  data,
  onEdit,
  onDelete,
}: DataTableProps<T>) {
  return (
    <div className="rounded-lg border">
      <Table>
        <TableHeader>
          <TableRow>
            {columns.map((column) => (
              <TableHead key={column.key}>{column.label}</TableHead>
            ))}
            <TableHead className="w-[100px]">Actions</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {data.length === 0 ? (
            <TableRow>
              <TableCell colSpan={columns.length + 1} className="h-24 text-center">
                No results found.
              </TableCell>
            </TableRow>
          ) : (
            data.map((row, i) => (
              <TableRow key={i}>
                {columns.map((column) => (
                  <TableCell key={column.key}>
                    {column.render ? column.render(row) : row[column.key]}
                  </TableCell>
                ))}
                <TableCell>
                  <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                      <Button variant="ghost" size="icon">
                        <MoreHorizontal className="h-4 w-4" />
                      </Button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent align="end">
                      <DropdownMenuItem onClick={() => onEdit(row)}>
                        <Pencil className="h-4 w-4 mr-2" />
                        Edit
                      </DropdownMenuItem>
                      <DropdownMenuSeparator />
                      <DropdownMenuItem
                        className="text-destructive"
                        onClick={() => onDelete(row)}
                      >
                        <Trash2 className="h-4 w-4 mr-2" />
                        Delete
                      </DropdownMenuItem>
                    </DropdownMenuContent>
                  </DropdownMenu>
                </TableCell>
              </TableRow>
            ))
          )}
        </TableBody>
      </Table>
    </div>
  );
}
```

### List Item

```tsx
interface ListItemProps {
  title: string;
  subtitle?: string;
  avatar?: string;
  badge?: {
    label: string;
    variant: 'default' | 'secondary' | 'destructive' | 'outline';
  };
  action?: React.ReactNode;
}

export function ListItem({ title, subtitle, avatar, badge, action }: ListItemProps) {
  return (
    <div className="flex items-center gap-4 p-4 border-b last:border-0">
      {avatar && (
        <Avatar>
          <AvatarImage src={avatar} />
          <AvatarFallback>{title[0]}</AvatarFallback>
        </Avatar>
      )}

      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-2">
          <p className="font-medium truncate">{title}</p>
          {badge && (
            <Badge variant={badge.variant}>{badge.label}</Badge>
          )}
        </div>
        {subtitle && (
          <p className="text-sm text-muted-foreground truncate">{subtitle}</p>
        )}
      </div>

      {action && <div className="shrink-0">{action}</div>}
    </div>
  );
}
```

### Key-Value Display

```tsx
interface KeyValueProps {
  items: Array<{
    label: string;
    value: React.ReactNode;
  }>;
}

export function KeyValue({ items }: KeyValueProps) {
  return (
    <dl className="divide-y">
      {items.map(({ label, value }) => (
        <div key={label} className="py-3 flex justify-between gap-4">
          <dt className="text-sm text-muted-foreground">{label}</dt>
          <dd className="text-sm font-medium text-right">{value}</dd>
        </div>
      ))}
    </dl>
  );
}

// Usage
<KeyValue items={[
  { label: 'Order ID', value: '#12345' },
  { label: 'Status', value: <Badge>Processing</Badge> },
  { label: 'Total', value: 'PHP 1,200.00' },
]} />
```

## Feedback

### Empty State

```tsx
interface EmptyStateProps {
  icon?: React.ElementType;
  title: string;
  description?: string;
  action?: {
    label: string;
    onClick: () => void;
  };
}

export function EmptyState({ icon: Icon, title, description, action }: EmptyStateProps) {
  return (
    <div className="flex flex-col items-center justify-center py-12 text-center">
      {Icon && (
        <div className="h-12 w-12 rounded-full bg-muted flex items-center justify-center mb-4">
          <Icon className="h-6 w-6 text-muted-foreground" />
        </div>
      )}
      <h3 className="text-lg font-medium">{title}</h3>
      {description && (
        <p className="text-sm text-muted-foreground mt-1 max-w-sm">
          {description}
        </p>
      )}
      {action && (
        <Button className="mt-4" onClick={action.onClick}>
          {action.label}
        </Button>
      )}
    </div>
  );
}
```

### Error State

```tsx
interface ErrorStateProps {
  title?: string;
  message: string;
  onRetry?: () => void;
}

export function ErrorState({
  title = 'Something went wrong',
  message,
  onRetry
}: ErrorStateProps) {
  return (
    <div className="flex flex-col items-center justify-center py-12 text-center">
      <div className="h-12 w-12 rounded-full bg-destructive/10 flex items-center justify-center mb-4">
        <AlertCircle className="h-6 w-6 text-destructive" />
      </div>
      <h3 className="text-lg font-medium">{title}</h3>
      <p className="text-sm text-muted-foreground mt-1 max-w-sm">
        {message}
      </p>
      {onRetry && (
        <Button variant="outline" className="mt-4" onClick={onRetry}>
          <RefreshCw className="h-4 w-4 mr-2" />
          Try Again
        </Button>
      )}
    </div>
  );
}
```

### Success Message

```tsx
interface SuccessMessageProps {
  title: string;
  description?: string;
  action?: {
    label: string;
    onClick: () => void;
  };
}

export function SuccessMessage({ title, description, action }: SuccessMessageProps) {
  return (
    <div className="flex flex-col items-center justify-center py-12 text-center">
      <div className="h-12 w-12 rounded-full bg-green-100 flex items-center justify-center mb-4">
        <Check className="h-6 w-6 text-green-600" />
      </div>
      <h3 className="text-lg font-medium">{title}</h3>
      {description && (
        <p className="text-sm text-muted-foreground mt-1 max-w-sm">
          {description}
        </p>
      )}
      {action && (
        <Button className="mt-4" onClick={action.onClick}>
          {action.label}
        </Button>
      )}
    </div>
  );
}
```

## Navigation

### Page Header

```tsx
interface PageHeaderProps {
  title: string;
  description?: string;
  actions?: React.ReactNode;
  breadcrumbs?: Array<{ label: string; href?: string }>;
}

export function PageHeader({ title, description, actions, breadcrumbs }: PageHeaderProps) {
  return (
    <div className="mb-8">
      {breadcrumbs && (
        <nav className="flex mb-4" aria-label="Breadcrumb">
          <ol className="flex items-center gap-2 text-sm text-muted-foreground">
            {breadcrumbs.map((crumb, i) => (
              <li key={i} className="flex items-center gap-2">
                {i > 0 && <ChevronRight className="h-4 w-4" />}
                {crumb.href ? (
                  <Link href={crumb.href} className="hover:text-foreground">
                    {crumb.label}
                  </Link>
                ) : (
                  <span className="text-foreground">{crumb.label}</span>
                )}
              </li>
            ))}
          </ol>
        </nav>
      )}

      <div className="flex items-start justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold">{title}</h1>
          {description && (
            <p className="text-muted-foreground mt-1">{description}</p>
          )}
        </div>
        {actions && <div className="flex gap-2 shrink-0">{actions}</div>}
      </div>
    </div>
  );
}
```

### Tabs Navigation

```tsx
interface TabsNavProps {
  tabs: Array<{
    value: string;
    label: string;
    count?: number;
  }>;
  value: string;
  onChange: (value: string) => void;
}

export function TabsNav({ tabs, value, onChange }: TabsNavProps) {
  return (
    <div className="border-b">
      <nav className="flex gap-4 -mb-px">
        {tabs.map((tab) => (
          <button
            key={tab.value}
            onClick={() => onChange(tab.value)}
            className={cn(
              "py-3 px-1 text-sm font-medium border-b-2 transition-colors",
              value === tab.value
                ? "border-primary text-primary"
                : "border-transparent text-muted-foreground hover:text-foreground"
            )}
          >
            {tab.label}
            {tab.count !== undefined && (
              <Badge variant="secondary" className="ml-2">
                {tab.count}
              </Badge>
            )}
          </button>
        ))}
      </nav>
    </div>
  );
}
```

## Overlays

### Confirmation Dialog

```tsx
interface ConfirmDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  title: string;
  description: string;
  confirmLabel?: string;
  cancelLabel?: string;
  variant?: 'default' | 'destructive';
  onConfirm: () => void;
  isLoading?: boolean;
}

export function ConfirmDialog({
  open,
  onOpenChange,
  title,
  description,
  confirmLabel = 'Confirm',
  cancelLabel = 'Cancel',
  variant = 'default',
  onConfirm,
  isLoading,
}: ConfirmDialogProps) {
  return (
    <AlertDialog open={open} onOpenChange={onOpenChange}>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>{title}</AlertDialogTitle>
          <AlertDialogDescription>{description}</AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel disabled={isLoading}>
            {cancelLabel}
          </AlertDialogCancel>
          <AlertDialogAction
            onClick={onConfirm}
            disabled={isLoading}
            className={variant === 'destructive' ? 'bg-destructive hover:bg-destructive/90' : ''}
          >
            {isLoading && <Loader2 className="h-4 w-4 mr-2 animate-spin" />}
            {confirmLabel}
          </AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  );
}
```

### Side Panel

```tsx
interface SidePanelProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  title: string;
  description?: string;
  children: React.ReactNode;
  footer?: React.ReactNode;
}

export function SidePanel({
  open,
  onOpenChange,
  title,
  description,
  children,
  footer,
}: SidePanelProps) {
  return (
    <Sheet open={open} onOpenChange={onOpenChange}>
      <SheetContent className="flex flex-col">
        <SheetHeader>
          <SheetTitle>{title}</SheetTitle>
          {description && <SheetDescription>{description}</SheetDescription>}
        </SheetHeader>

        <div className="flex-1 overflow-y-auto py-4">
          {children}
        </div>

        {footer && (
          <div className="border-t pt-4 mt-auto">
            {footer}
          </div>
        )}
      </SheetContent>
    </Sheet>
  );
}
```

## Actions

### Action Button Group

```tsx
interface ActionButtonGroupProps {
  primaryAction: {
    label: string;
    onClick: () => void;
    isLoading?: boolean;
  };
  secondaryAction?: {
    label: string;
    onClick: () => void;
  };
}

export function ActionButtonGroup({ primaryAction, secondaryAction }: ActionButtonGroupProps) {
  return (
    <div className="flex gap-3">
      {secondaryAction && (
        <Button variant="outline" onClick={secondaryAction.onClick}>
          {secondaryAction.label}
        </Button>
      )}
      <Button onClick={primaryAction.onClick} disabled={primaryAction.isLoading}>
        {primaryAction.isLoading && (
          <Loader2 className="h-4 w-4 mr-2 animate-spin" />
        )}
        {primaryAction.label}
      </Button>
    </div>
  );
}
```

### Floating Action Button (Mobile)

```tsx
interface FABProps {
  icon: React.ElementType;
  label: string;
  onClick: () => void;
}

export function FloatingActionButton({ icon: Icon, label, onClick }: FABProps) {
  return (
    <Button
      onClick={onClick}
      className="
        fixed bottom-20 right-4
        h-14 w-14 rounded-full
        shadow-lg
        md:hidden
      "
      aria-label={label}
    >
      <Icon className="h-6 w-6" />
    </Button>
  );
}
```

### Bulk Actions Bar

```tsx
interface BulkActionsBarProps {
  selectedCount: number;
  onClearSelection: () => void;
  actions: Array<{
    label: string;
    icon: React.ElementType;
    onClick: () => void;
    variant?: 'default' | 'destructive';
  }>;
}

export function BulkActionsBar({ selectedCount, onClearSelection, actions }: BulkActionsBarProps) {
  if (selectedCount === 0) return null;

  return (
    <div className="fixed bottom-4 left-1/2 -translate-x-1/2 z-50">
      <div className="bg-background border rounded-lg shadow-lg p-2 flex items-center gap-2">
        <span className="text-sm font-medium px-2">
          {selectedCount} selected
        </span>

        <div className="h-4 w-px bg-border" />

        {actions.map((action) => (
          <Button
            key={action.label}
            variant={action.variant === 'destructive' ? 'destructive' : 'ghost'}
            size="sm"
            onClick={action.onClick}
          >
            <action.icon className="h-4 w-4 mr-2" />
            {action.label}
          </Button>
        ))}

        <div className="h-4 w-px bg-border" />

        <Button variant="ghost" size="sm" onClick={onClearSelection}>
          <X className="h-4 w-4" />
        </Button>
      </div>
    </div>
  );
}
```


---

# Common Patterns (from SKILL.md)

## Common Patterns

### Empty States
```tsx
<div className="flex flex-col items-center justify-center py-12 text-center">
  <Icon className="h-12 w-12 text-muted-foreground mb-4" />
  <h3 className="text-lg font-medium">No items yet</h3>
  <p className="text-sm text-muted-foreground mt-1 mb-4">
    Get started by adding your first item
  </p>
  <Button className="bg-negosyo-blue hover:bg-negosyo-blue/90">Add Item</Button>
</div>
```

### Confirmation Dialogs
```tsx
<AlertDialog>
  <AlertDialogTrigger asChild>
    <Button variant="destructive">Delete</Button>
  </AlertDialogTrigger>
  <AlertDialogContent>
    <AlertDialogHeader>
      <AlertDialogTitle>Are you sure?</AlertDialogTitle>
      <AlertDialogDescription>
        This action cannot be undone.
      </AlertDialogDescription>
    </AlertDialogHeader>
    <AlertDialogFooter>
      <AlertDialogCancel>Cancel</AlertDialogCancel>
      <AlertDialogAction className="bg-destructive">Delete</AlertDialogAction>
    </AlertDialogFooter>
  </AlertDialogContent>
</AlertDialog>
```

### Status Badges
```tsx
// Use semantic colors consistently
<Badge className="bg-negosyo-blue">Active</Badge>        // Negosyo Blue
<Badge variant="secondary">Pending</Badge>            // Gray
<Badge variant="destructive">Rejected</Badge>         // Red
<Badge variant="outline">Draft</Badge>                // Outline
<Badge className="bg-green-600">Approved</Badge>      // Green
```

### Progress Indicators
```tsx
// Multi-step processes
<div className="flex items-center space-x-2">
  {steps.map((step, index) => (
    <React.Fragment key={step.id}>
      <div className={cn(
        "flex items-center justify-center w-8 h-8 rounded-full text-sm font-medium",
        index < currentStep && "bg-negosyo-blue text-white",
        index === currentStep && "bg-negosyo-blue text-white ring-2 ring-offset-2 ring-negosyo-blue",
        index > currentStep && "bg-muted text-muted-foreground"
      )}>
        {index < currentStep ? <Check className="h-4 w-4" /> : index + 1}
      </div>
      {index < steps.length - 1 && (
        <div className={cn(
          "flex-1 h-0.5",
          index < currentStep ? "bg-negosyo-blue" : "bg-muted"
        )} />
      )}
    </React.Fragment>
  ))}
</div>
```


---

## FRAMES Compliance UI

The FRAMES regulatory framework covers the complete lifecycle of cooperatives and social enterprises:
- **F**ormation - Initial organization setup and documentation
- **R**egistration - Official registration and certification
- **A**uditing - Financial and operational audits
- **M**onitoring & Evaluation - Ongoing performance tracking
- **E**nforcement - Compliance enforcement actions
- **S**ustainability - Long-term viability assessment

```tsx
const framesCategories = [
  { id: 'F', name: 'Formation', icon: FileText },
  { id: 'R', name: 'Registration', icon: ClipboardCheck },
  { id: 'A', name: 'Auditing', icon: Search },
  { id: 'M', name: 'Monitoring', icon: Activity },
  { id: 'E', name: 'Enforcement', icon: Shield },
  { id: 'S', name: 'Sustainability', icon: Leaf },
];

// Display pattern for compliance dashboard
<div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
  {framesCategories.map((cat) => (
    <Card key={cat.id} className="text-center p-4">
      <cat.icon className="h-8 w-8 mx-auto text-negosyo-blue" />
      <p className="font-semibold mt-2">{cat.name}</p>
      <Progress value={complianceData[cat.id]} className="mt-2" />
      <span className="text-sm text-muted-foreground">
        {complianceData[cat.id]}% Complete
      </span>
    </Card>
  ))}
</div>
```
