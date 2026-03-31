# Table Patterns

Data tables with TanStack Table and shadcn/ui for CSEA.

## Basic Table

```tsx
import {
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
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
          {data.map((item) => (
            <TableRow key={item.id} className="hover:bg-gray-50">
              <TableCell className="font-medium">{item.name}</TableCell>
              <TableCell>{item.type}</TableCell>
              <TableCell>
                <Badge className="bg-emerald-100 text-emerald-800">{item.status}</Badge>
              </TableCell>
              <TableCell className="text-right">
                <Button variant="ghost" size="sm">View</Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  )
}
```

## TanStack Table with Sorting

```tsx
import { useReactTable, getCoreRowModel, getSortedRowModel, flexRender } from "@tanstack/react-table"
import { ArrowUpDown } from "lucide-react"

const [sorting, setSorting] = useState([])

const table = useReactTable({
  data,
  columns,
  getCoreRowModel: getCoreRowModel(),
  getSortedRowModel: getSortedRowModel(),
  onSortingChange: setSorting,
  state: { sorting },
})
```

## Loading State

```tsx
import { Skeleton } from "@/components/ui/skeleton"

export function TableSkeleton({ rows = 5 }) {
  return (
    <TableBody>
      {[...Array(rows)].map((_, i) => (
        <TableRow key={i}>
          <TableCell><Skeleton className="h-4 w-32" /></TableCell>
          <TableCell><Skeleton className="h-4 w-24" /></TableCell>
        </TableRow>
      ))}
    </TableBody>
  )
}
```

## Empty State

```tsx
import { FileX } from "lucide-react"

<div className="flex flex-col items-center py-12 text-gray-500">
  <FileX className="h-12 w-12 mb-4" />
  <p className="text-lg font-medium">No data found</p>
</div>
```
