## Quick Start Examples

### CSEA Navigation Bar

```tsx
import Link from "next/link"
import { Button } from "@/components/ui/button"

export function Navbar() {
  return (
    <nav className="bg-negosyo-blue text-white">
      <div className="container mx-auto px-4 py-3">
        <div className="flex items-center justify-between">
          <Link href="/" className="text-xl font-bold">
            CSEA
          </Link>
          <div className="flex items-center gap-6">
            <Link href="/cooperatives" className="hover:text-gray-200">
              Cooperatives
            </Link>
            <Link href="/social-enterprises" className="hover:text-gray-200">
              Social Enterprises
            </Link>
            <Link href="/marketplace" className="hover:text-gray-200">
              Marketplace
            </Link>
          </div>
        </div>
      </div>
    </nav>
  )
}
```

### CSEA Data Table

```tsx
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import { Badge } from "@/components/ui/badge"

export function CooperativesTable({ data }) {
  return (
    <div className="rounded-lg border overflow-hidden">
      <Table>
        <TableHeader className="bg-negosyo-blue">
          <TableRow>
            <TableHead className="text-white font-semibold">Name</TableHead>
            <TableHead className="text-white font-semibold">Type</TableHead>
            <TableHead className="text-white font-semibold">Status</TableHead>
            <TableHead className="text-white font-semibold text-right">Actions</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {data.map((coop) => (
            <TableRow key={coop.id} className="hover:bg-gray-50">
              <TableCell className="font-medium">{coop.name}</TableCell>
              <TableCell>{coop.type}</TableCell>
              <TableCell>
                <Badge variant={coop.status === "active" ? "success" : "secondary"}>
                  {coop.status}
                </Badge>
              </TableCell>
              <TableCell className="text-right">
                <Button variant="ghost" size="sm">View</Button>
                <Button variant="ghost" size="sm">Edit</Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  )
}
```

### CSEA Confirmation Dialog (Modals for Confirmations Only)

```tsx
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from "@/components/ui/alert-dialog"

// ✅ CORRECT: Modal for delete confirmation (no input fields)
export function DeleteCooperativeDialog({ open, onOpenChange, onConfirm, cooperativeName }) {
  return (
    <AlertDialog open={open} onOpenChange={onOpenChange}>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>Delete Cooperative</AlertDialogTitle>
          <AlertDialogDescription>
            Are you sure you want to delete "{cooperativeName}"?
            This action cannot be undone.
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Cancel</AlertDialogCancel>
          <AlertDialogAction
            onClick={onConfirm}
            className="bg-destructive hover:bg-destructive/90"
          >
            Delete
          </AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  )
}

// ❌ WRONG: Forms should NOT be in modals
// Instead, navigate to /cooperatives/new for creation forms
// See "Interaction Pattern Guidelines" section above
```

### Stat Card

```tsx
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Users } from "lucide-react"

export function StatCard({ title, value, change, icon: Icon = Users }) {
  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between pb-2">
        <CardTitle className="text-sm font-medium text-gray-500">
          {title}
        </CardTitle>
        <Icon className="h-5 w-5 text-negosyo-blue" />
      </CardHeader>
      <CardContent>
        <div className="text-3xl font-bold text-negosyo-blue">{value}</div>
        {change && (
          <p className="text-sm text-emerald-600 mt-1">
            {change > 0 ? "+" : ""}{change}% from last month
          </p>
        )}
      </CardContent>
    </Card>
  )
}
```

---
