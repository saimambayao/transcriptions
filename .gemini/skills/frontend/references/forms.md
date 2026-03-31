# Form Patterns

React Hook Form + Zod validation with shadcn/ui components for CSEA.

## Basic Form Setup

```tsx
import { useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import { z } from "zod"
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

const formSchema = z.object({
  name: z.string().min(2, "Name must be at least 2 characters"),
  email: z.string().email("Invalid email address"),
})

type FormValues = z.infer<typeof formSchema>

export function CooperativeForm() {
  const form = useForm<FormValues>({
    resolver: zodResolver(formSchema),
    defaultValues: { name: "", email: "" },
  })

  const onSubmit = async (data: FormValues) => {
    console.log(data)
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
        <FormField
          control={form.control}
          name="name"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Name *</FormLabel>
              <FormControl>
                <Input {...field} className="focus-visible:ring-negosyo-blue" />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <div className="flex justify-end gap-3">
          <Button variant="outline">Cancel</Button>
          <Button type="submit" className="bg-negosyo-blue hover:bg-negosyo-blue/90">
            Submit
          </Button>
        </div>
      </form>
    </Form>
  )
}
```

## Form with Select

```tsx
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

<FormField
  control={form.control}
  name="type"
  render={({ field }) => (
    <FormItem>
      <FormLabel>Type *</FormLabel>
      <Select onValueChange={field.onChange} defaultValue={field.value}>
        <FormControl>
          <SelectTrigger className="focus:ring-negosyo-blue">
            <SelectValue placeholder="Select type" />
          </SelectTrigger>
        </FormControl>
        <SelectContent>
          <SelectItem value="producer">Producer</SelectItem>
          <SelectItem value="consumer">Consumer</SelectItem>
        </SelectContent>
      </Select>
      <FormMessage />
    </FormItem>
  )}
/>
```

## Loading State

```tsx
import { Loader2 } from "lucide-react"

<Button type="submit" disabled={isSubmitting} className="bg-negosyo-blue hover:bg-negosyo-blue/90">
  {isSubmitting ? (
    <><Loader2 className="mr-2 h-4 w-4 animate-spin" />Submitting...</>
  ) : (
    "Submit"
  )}
</Button>
```

## With TanStack Query

```tsx
import { useMutation, useQueryClient } from "@tanstack/react-query"

const mutation = useMutation({
  mutationFn: (data: FormValues) => fetch("/api/cooperatives", {
    method: "POST",
    body: JSON.stringify(data),
  }),
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ["cooperatives"] })
    toast.success("Created successfully")
  },
})

const onSubmit = (data: FormValues) => mutation.mutate(data)
```
