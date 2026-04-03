#!/usr/bin/env python3
"""
Generate React component templates for CSEA.
Creates TypeScript components with shadcn/ui patterns.

Usage: python create_component.py ComponentName [type]

Types:
  page      - Next.js page component
  card      - Card component with CSEA header
  form      - Form with React Hook Form + Zod
  table     - Data table component
  modal     - Dialog component
"""

import sys
import os

TEMPLATES = {
    'default': '''import {{ FC }} from "react"

interface {name}Props {{
  // Add props here
}}

export const {name}: FC<{name}Props> = ({{ }}) => {{
  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold text-negosyo-blue">{name}</h2>
    </div>
  )
}}
''',

    'page': '''"use client"

export default function {name}Page() {{
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">{name}</h1>
      <div className="space-y-6">
        {{/* Page content */}}
      </div>
    </div>
  )
}}
''',

    'card': '''import {{ FC }} from "react"
import {{ Card, CardContent, CardHeader, CardTitle }} from "@/components/ui/card"
import {{ Badge }} from "@/components/ui/badge"

interface {name}Props {{
  title: string
  description?: string
  status?: "active" | "pending" | "inactive"
}}

export const {name}: FC<{name}Props> = ({{ title, description, status }}) => {{
  const statusColors = {{
    active: "bg-emerald-100 text-emerald-800",
    pending: "bg-orange-100 text-orange-800",
    inactive: "bg-gray-100 text-gray-800",
  }}

  return (
    <Card className="hover:shadow-lg transition-shadow">
      <CardHeader className="bg-negosyo-blue text-white rounded-t-lg">
        <CardTitle className="flex items-center justify-between">
          {{title}}
          {{status && (
            <Badge className={{statusColors[status]}}>{{status}}</Badge>
          )}}
        </CardTitle>
      </CardHeader>
      <CardContent className="p-6">
        {{description && <p className="text-gray-600">{{description}}</p>}}
      </CardContent>
    </Card>
  )
}}
''',

    'form': '''"use client"

import {{ useForm }} from "react-hook-form"
import {{ zodResolver }} from "@hookform/resolvers/zod"
import {{ z }} from "zod"
import {{ Button }} from "@/components/ui/button"
import {{ Input }} from "@/components/ui/input"
import {{
  Form, FormControl, FormField, FormItem, FormLabel, FormMessage,
}} from "@/components/ui/form"
import {{ Loader2 }} from "lucide-react"

const formSchema = z.object({{
  name: z.string().min(2, "Name must be at least 2 characters"),
  email: z.string().email("Invalid email address"),
}})

type FormValues = z.infer<typeof formSchema>

export function {name}Form() {{
  const form = useForm<FormValues>({{
    resolver: zodResolver(formSchema),
    defaultValues: {{ name: "", email: "" }},
  }})

  const {{ isSubmitting }} = form.formState

  const onSubmit = async (data: FormValues) => {{
    console.log(data)
    // TODO: Implement form submission
  }}

  return (
    <Form {{...form}}>
      <form onSubmit={{form.handleSubmit(onSubmit)}} className="space-y-6">
        <FormField
          control={{form.control}}
          name="name"
          render={{({{ field }}) => (
            <FormItem>
              <FormLabel>Name *</FormLabel>
              <FormControl>
                <Input {{...field}} className="focus-visible:ring-negosyo-blue" />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}}
        />

        <FormField
          control={{form.control}}
          name="email"
          render={{({{ field }}) => (
            <FormItem>
              <FormLabel>Email *</FormLabel>
              <FormControl>
                <Input type="email" {{...field}} className="focus-visible:ring-negosyo-blue" />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}}
        />

        <div className="flex justify-end gap-3">
          <Button variant="outline" type="button">Cancel</Button>
          <Button
            type="submit"
            disabled={{isSubmitting}}
            className="bg-negosyo-blue hover:bg-negosyo-blue/90"
          >
            {{isSubmitting ? (
              <><Loader2 className="mr-2 h-4 w-4 animate-spin" />Saving...</>
            ) : (
              "Submit"
            )}}
          </Button>
        </div>
      </form>
    </Form>
  )
}}
''',

    'table': '''"use client"

import {{ FC }} from "react"
import {{
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
}} from "@/components/ui/table"
import {{ Badge }} from "@/components/ui/badge"
import {{ Button }} from "@/components/ui/button"
import {{ Skeleton }} from "@/components/ui/skeleton"

interface {name}Item {{
  id: string
  name: string
  type: string
  status: "active" | "pending" | "inactive"
}}

interface {name}TableProps {{
  data: {name}Item[]
  isLoading?: boolean
}}

export const {name}Table: FC<{name}TableProps> = ({{ data, isLoading }}) => {{
  const statusColors = {{
    active: "bg-emerald-100 text-emerald-800",
    pending: "bg-orange-100 text-orange-800",
    inactive: "bg-gray-100 text-gray-800",
  }}

  if (isLoading) {{
    return (
      <div className="space-y-3">
        {{[...Array(5)].map((_, i) => (
          <Skeleton key={{i}} className="h-12 w-full" />
        ))}}
      </div>
    )
  }}

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
          {{data.map((item) => (
            <TableRow key={{item.id}} className="hover:bg-gray-50">
              <TableCell className="font-medium">{{item.name}}</TableCell>
              <TableCell>{{item.type}}</TableCell>
              <TableCell>
                <Badge className={{statusColors[item.status]}}>{{item.status}}</Badge>
              </TableCell>
              <TableCell className="text-right">
                <Button variant="ghost" size="sm">View</Button>
                <Button variant="ghost" size="sm">Edit</Button>
              </TableCell>
            </TableRow>
          ))}}
        </TableBody>
      </Table>
    </div>
  )
}}
''',

    'modal': '''"use client"

import {{ FC }} from "react"
import {{
  Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle,
}} from "@/components/ui/dialog"
import {{ Button }} from "@/components/ui/button"

interface {name}ModalProps {{
  open: boolean
  onOpenChange: (open: boolean) => void
  onConfirm?: () => void
}}

export const {name}Modal: FC<{name}ModalProps> = ({{ open, onOpenChange, onConfirm }}) => {{
  return (
    <Dialog open={{open}} onOpenChange={{onOpenChange}}>
      <DialogContent className="sm:max-w-[500px] p-0 overflow-hidden">
        <DialogHeader className="bg-negosyo-blue px-6 py-4">
          <DialogTitle className="text-white">{name}</DialogTitle>
          <DialogDescription className="text-white/80">
            Add your description here.
          </DialogDescription>
        </DialogHeader>

        <div className="p-6">
          {{/* Modal content */}}
        </div>

        <DialogFooter className="bg-gray-50 px-6 py-4">
          <Button variant="outline" onClick={{() => onOpenChange(false)}}>
            Cancel
          </Button>
          <Button
            onClick={{onConfirm}}
            className="bg-negosyo-blue hover:bg-negosyo-blue/90"
          >
            Confirm
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}}
''',
}

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_component.py ComponentName [type]")
        print("\nTypes: default, page, card, form, table, modal")
        sys.exit(1)

    name = sys.argv[1]
    component_type = sys.argv[2] if len(sys.argv) > 2 else 'default'

    if component_type not in TEMPLATES:
        print(f"Unknown type: {component_type}")
        print(f"Available types: {', '.join(TEMPLATES.keys())}")
        sys.exit(1)

    template = TEMPLATES[component_type]
    output = template.format(name=name)

    print(f"// {name}.tsx - {component_type} component")
    print(output)

if __name__ == '__main__':
    main()
