# Storefront User Journeys

User journey maps and UX patterns for Cooperatives and Social Enterprises managing and customizing their individual storefronts.

## Table of Contents
- [Overview](#overview)
- [Storefront Setup Journey](#storefront-setup-journey)
- [Shop Customization Journey](#shop-customization-journey)
- [Customer Interaction Journey](#customer-interaction-journey)
- [Storefront Analytics Journey](#storefront-analytics-journey)

## Overview

Each Cooperative and Social Enterprise has a dedicated storefront:
- **Coop Storefront**: `/coop/[shortname]`
- **SE Storefront**: `/se/[shortname]`

Storefronts serve as the public-facing shop where customers browse and purchase products.

### Key User Goals
| User | Goal |
|------|------|
| Coop/SE Manager | Create an attractive, trustworthy shop that converts visitors |
| Customer | Find products, learn about the seller, make purchases |
| CSEA | Ensure storefronts meet platform standards |

---

## Storefront Setup Journey

### Initial Setup Flow

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Choose     │───▶│  Basic      │───▶│  Add        │───▶│  Preview &  │
│  Shortname  │    │  Info       │    │  Products   │    │  Publish    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

### Step 1: Choose Shortname (URL)

**Critical decision - permanent identifier**:
```tsx
// Shortname Selection
<Card className="max-w-md">
  <CardHeader>
    <CardTitle>Choose Your Shop URL</CardTitle>
    <CardDescription>
      This will be your permanent shop address. Choose wisely!
    </CardDescription>
  </CardHeader>
  <CardContent className="space-y-4">
    <div className="space-y-2">
      <Label>Shop URL</Label>
      <div className="flex">
        <span className="inline-flex items-center px-3 rounded-l-md border border-r-0 bg-muted text-sm text-muted-foreground">
          negosyo.ph/coop/
        </span>
        <Input
          className="rounded-l-none"
          placeholder="your-coop-name"
          value={shortname}
          onChange={(e) => setShortname(slugify(e.target.value))}
        />
      </div>

      {/* Availability Check */}
      {isChecking && (
        <p className="text-sm text-muted-foreground flex items-center gap-2">
          <Loader2 className="h-4 w-4 animate-spin" />
          Checking availability...
        </p>
      )}
      {isAvailable === true && (
        <p className="text-sm text-green-600 flex items-center gap-2">
          <CheckCircle className="h-4 w-4" />
          This URL is available!
        </p>
      )}
      {isAvailable === false && (
        <p className="text-sm text-destructive flex items-center gap-2">
          <XCircle className="h-4 w-4" />
          This URL is taken. Try another.
        </p>
      )}
    </div>

    {/* Preview */}
    <div className="p-3 bg-muted rounded-lg">
      <p className="text-sm text-muted-foreground">Your shop will be at:</p>
      <p className="font-mono text-sm">
        https://negosyo.ph/coop/<span className="text-primary">{shortname || 'your-name'}</span>
      </p>
    </div>

    {/* Guidelines */}
    <Alert>
      <Info className="h-4 w-4" />
      <AlertDescription className="text-sm">
        Use lowercase letters, numbers, and hyphens only.
        This cannot be changed later.
      </AlertDescription>
    </Alert>
  </CardContent>
  <CardFooter>
    <Button className="w-full" disabled={!isAvailable}>
      Continue
    </Button>
  </CardFooter>
</Card>
```

### Step 2: Basic Information

```tsx
// Storefront Basic Info Form
<div className="space-y-6">
  {/* Logo Upload */}
  <div className="space-y-2">
    <Label>Shop Logo *</Label>
    <div className="flex items-start gap-4">
      <Avatar className="h-24 w-24">
        {logo ? (
          <AvatarImage src={logo} />
        ) : (
          <AvatarFallback className="bg-muted">
            <ImageIcon className="h-8 w-8 text-muted-foreground" />
          </AvatarFallback>
        )}
      </Avatar>
      <div className="space-y-2">
        <Button variant="outline" size="sm" onClick={openLogoUpload}>
          <Upload className="h-4 w-4 mr-2" />
          Upload Logo
        </Button>
        <p className="text-xs text-muted-foreground">
          Square image, at least 400x400px. PNG or JPG.
        </p>
      </div>
    </div>
  </div>

  {/* Cover Image */}
  <div className="space-y-2">
    <Label>Cover Image</Label>
    <div
      className="relative h-32 rounded-lg border-2 border-dashed flex items-center justify-center cursor-pointer hover:border-primary transition-colors"
      onClick={openCoverUpload}
    >
      {cover ? (
        <Image src={cover} alt="Cover" fill className="object-cover rounded-lg" />
      ) : (
        <div className="text-center">
          <ImageIcon className="h-8 w-8 mx-auto text-muted-foreground" />
          <p className="text-sm text-muted-foreground mt-2">
            Add a cover image (1200x300px recommended)
          </p>
        </div>
      )}
    </div>
  </div>

  {/* Shop Name */}
  <div className="space-y-2">
    <Label>Shop Name *</Label>
    <Input placeholder="e.g., Sulu Weavers Cooperative" />
    <p className="text-xs text-muted-foreground">
      This is your display name, different from URL
    </p>
  </div>

  {/* Tagline */}
  <div className="space-y-2">
    <Label>Tagline</Label>
    <Input placeholder="e.g., Handcrafted textiles from the heart of Sulu" maxLength={100} />
    <p className="text-xs text-muted-foreground">
      A short phrase that describes your shop
    </p>
  </div>

  {/* Description */}
  <div className="space-y-2">
    <Label>About Your Shop *</Label>
    <Textarea
      placeholder="Tell customers about your cooperative, your story, and what makes your products special..."
      rows={4}
    />
  </div>

  {/* Location */}
  <div className="grid grid-cols-2 gap-4">
    <div className="space-y-2">
      <Label>Province *</Label>
      <Select>
        <SelectTrigger>
          <SelectValue placeholder="Select province" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="lanao-del-sur">Lanao del Sur</SelectItem>
          <SelectItem value="maguindanao">Maguindanao</SelectItem>
          <SelectItem value="sulu">Sulu</SelectItem>
          <SelectItem value="basilan">Basilan</SelectItem>
          <SelectItem value="tawi-tawi">Tawi-Tawi</SelectItem>
        </SelectContent>
      </Select>
    </div>
    <div className="space-y-2">
      <Label>Municipality *</Label>
      <Select>
        <SelectTrigger>
          <SelectValue placeholder="Select municipality" />
        </SelectTrigger>
        <SelectContent>
          {/* Dynamic based on province */}
        </SelectContent>
      </Select>
    </div>
  </div>
</div>
```

---

## Shop Customization Journey

### Theme & Appearance Settings

```tsx
// Shop Appearance Settings
<div className="space-y-8">
  <div>
    <h2 className="text-lg font-semibold">Appearance</h2>
    <p className="text-sm text-muted-foreground">
      Customize how your shop looks to customers
    </p>
  </div>

  {/* Theme Color */}
  <div className="space-y-4">
    <Label>Accent Color</Label>
    <div className="flex gap-3">
      {[
        { name: 'Negosyo Blue', value: '#0056D2' },
        { name: 'Forest Green', value: '#16a34a' },
        { name: 'Ocean Teal', value: '#0d9488' },
        { name: 'Warm Orange', value: '#ea580c' },
        { name: 'Custom', value: 'custom' },
      ].map((color) => (
        <button
          key={color.value}
          onClick={() => setAccentColor(color.value)}
          className={cn(
            "h-10 w-10 rounded-full border-2 transition-transform hover:scale-110",
            accentColor === color.value && "ring-2 ring-offset-2 ring-primary"
          )}
          style={{ backgroundColor: color.value === 'custom' ? '#ccc' : color.value }}
          title={color.name}
        >
          {color.value === 'custom' && (
            <Palette className="h-4 w-4 mx-auto text-white" />
          )}
        </button>
      ))}
    </div>
  </div>

  {/* Featured Products */}
  <div className="space-y-4">
    <div className="flex items-center justify-between">
      <div>
        <Label>Featured Products</Label>
        <p className="text-sm text-muted-foreground">
          Highlight up to 4 products on your homepage
        </p>
      </div>
      <Button variant="outline" size="sm">
        <Plus className="h-4 w-4 mr-2" />
        Add Product
      </Button>
    </div>

    <div className="grid grid-cols-4 gap-4">
      {featuredProducts.map((product, i) => (
        <div key={i} className="relative group">
          <div className="aspect-square rounded-lg border bg-muted overflow-hidden">
            {product ? (
              <Image src={product.image} alt={product.name} fill className="object-cover" />
            ) : (
              <div className="h-full flex items-center justify-center">
                <Plus className="h-6 w-6 text-muted-foreground" />
              </div>
            )}
          </div>
          {product && (
            <button
              className="absolute top-1 right-1 h-6 w-6 rounded-full bg-destructive text-white opacity-0 group-hover:opacity-100 transition-opacity"
              onClick={() => removeFeatured(i)}
            >
              <X className="h-4 w-4 mx-auto" />
            </button>
          )}
        </div>
      ))}
    </div>
  </div>

  {/* Social Links */}
  <div className="space-y-4">
    <Label>Social Media Links</Label>
    <div className="space-y-3">
      <div className="flex items-center gap-3">
        <Facebook className="h-5 w-5 text-muted-foreground" />
        <Input placeholder="facebook.com/yourpage" />
      </div>
      <div className="flex items-center gap-3">
        <Instagram className="h-5 w-5 text-muted-foreground" />
        <Input placeholder="instagram.com/yourhandle" />
      </div>
      <div className="flex items-center gap-3">
        <Globe className="h-5 w-5 text-muted-foreground" />
        <Input placeholder="yourwebsite.com" />
      </div>
    </div>
  </div>

  {/* Preview Button */}
  <div className="flex gap-4">
    <Button variant="outline" asChild>
      <Link href={`/coop/${shortname}`} target="_blank">
        <Eye className="h-4 w-4 mr-2" />
        Preview Shop
      </Link>
    </Button>
    <Button>
      Save Changes
    </Button>
  </div>
</div>
```

### Live Preview Component

```tsx
// Storefront Live Preview
<div className="border rounded-lg overflow-hidden">
  {/* Preview Header */}
  <div className="bg-muted px-4 py-2 flex items-center gap-2 border-b">
    <div className="flex gap-1.5">
      <div className="h-3 w-3 rounded-full bg-red-400" />
      <div className="h-3 w-3 rounded-full bg-yellow-400" />
      <div className="h-3 w-3 rounded-full bg-green-400" />
    </div>
    <div className="flex-1 text-center">
      <span className="text-xs text-muted-foreground font-mono">
        negosyo.ph/coop/{shortname}
      </span>
    </div>
  </div>

  {/* Preview Content */}
  <div className="h-[500px] overflow-y-auto">
    {/* Mini Storefront Preview */}
    <div style={{ '--accent': accentColor } as React.CSSProperties}>
      {/* Cover */}
      <div className="h-24 bg-gradient-to-r from-[var(--accent)] to-[var(--accent)]/70" />

      {/* Logo & Info */}
      <div className="px-4 -mt-8">
        <Avatar className="h-16 w-16 border-4 border-background">
          <AvatarImage src={logo} />
          <AvatarFallback>{shopName?.[0]}</AvatarFallback>
        </Avatar>
        <h2 className="text-lg font-bold mt-2">{shopName || 'Your Shop Name'}</h2>
        <p className="text-sm text-muted-foreground">{tagline || 'Your tagline here'}</p>
      </div>

      {/* Featured Products Preview */}
      <div className="px-4 mt-6">
        <h3 className="font-medium mb-3">Featured Products</h3>
        <div className="grid grid-cols-2 gap-2">
          {featuredProducts.slice(0, 4).map((product, i) => (
            <div key={i} className="aspect-square rounded bg-muted" />
          ))}
        </div>
      </div>
    </div>
  </div>
</div>
```

---

## Customer Interaction Journey

### Chat & Inquiries Management

```tsx
// Customer Messages Dashboard
<Card>
  <CardHeader>
    <div className="flex items-center justify-between">
      <CardTitle>Customer Messages</CardTitle>
      <Badge variant="secondary">{unreadCount} unread</Badge>
    </div>
  </CardHeader>
  <CardContent>
    <div className="space-y-4">
      {conversations.map((convo) => (
        <div
          key={convo.id}
          className={cn(
            "flex items-start gap-3 p-3 rounded-lg cursor-pointer hover:bg-muted/50 transition-colors",
            convo.unread && "bg-primary/5"
          )}
          onClick={() => openConversation(convo.id)}
        >
          <Avatar>
            <AvatarImage src={convo.customer.avatar} />
            <AvatarFallback>{convo.customer.initials}</AvatarFallback>
          </Avatar>
          <div className="flex-1 min-w-0">
            <div className="flex items-center justify-between">
              <p className={cn("font-medium", convo.unread && "text-primary")}>
                {convo.customer.name}
              </p>
              <span className="text-xs text-muted-foreground">
                {formatRelativeTime(convo.lastMessage.timestamp)}
              </span>
            </div>
            <p className="text-sm text-muted-foreground truncate">
              {convo.lastMessage.preview}
            </p>
            {convo.relatedProduct && (
              <div className="flex items-center gap-2 mt-1">
                <Package className="h-3 w-3 text-muted-foreground" />
                <span className="text-xs text-muted-foreground">
                  Re: {convo.relatedProduct.name}
                </span>
              </div>
            )}
          </div>
          {convo.unread && (
            <div className="h-2 w-2 rounded-full bg-primary shrink-0" />
          )}
        </div>
      ))}
    </div>
  </CardContent>
</Card>
```

### Quick Reply Templates

```tsx
// Quick Reply Feature
<Popover>
  <PopoverTrigger asChild>
    <Button variant="outline" size="sm">
      <Zap className="h-4 w-4 mr-2" />
      Quick Reply
    </Button>
  </PopoverTrigger>
  <PopoverContent className="w-80">
    <div className="space-y-2">
      <p className="text-sm font-medium">Quick Replies</p>
      {quickReplies.map((reply) => (
        <button
          key={reply.id}
          className="w-full text-left p-2 text-sm rounded hover:bg-muted transition-colors"
          onClick={() => insertQuickReply(reply.text)}
        >
          <p className="font-medium">{reply.title}</p>
          <p className="text-muted-foreground text-xs truncate">{reply.text}</p>
        </button>
      ))}
      <Separator />
      <Button variant="ghost" size="sm" className="w-full">
        <Plus className="h-4 w-4 mr-2" />
        Add Template
      </Button>
    </div>
  </PopoverContent>
</Popover>

// Default Quick Replies
const quickReplies = [
  {
    id: 1,
    title: 'Greeting',
    text: 'Assalamu Alaykum! Thank you for your interest in our products. How can I help you today?'
  },
  {
    id: 2,
    title: 'Availability',
    text: 'Yes, this item is currently in stock and ready to ship within 2-3 business days.'
  },
  {
    id: 3,
    title: 'Shipping Info',
    text: 'We ship via J&T Express and LBC. Delivery usually takes 3-5 days within BARMM, 5-7 days to other regions.'
  },
  {
    id: 4,
    title: 'Custom Order',
    text: 'We accept custom orders! Please share your specifications and quantity, and we will provide a quote.'
  },
];
```

---

## Storefront Analytics Journey

### Shop Performance Dashboard

```tsx
// Storefront Analytics
<div className="space-y-6">
  {/* Period Selector */}
  <div className="flex items-center justify-between">
    <h2 className="text-lg font-semibold">Shop Performance</h2>
    <Select defaultValue="7d">
      <SelectTrigger className="w-32">
        <SelectValue />
      </SelectTrigger>
      <SelectContent>
        <SelectItem value="today">Today</SelectItem>
        <SelectItem value="7d">Last 7 days</SelectItem>
        <SelectItem value="30d">Last 30 days</SelectItem>
        <SelectItem value="90d">Last 90 days</SelectItem>
      </SelectContent>
    </Select>
  </div>

  {/* Key Metrics */}
  <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
    <StatCard
      title="Shop Views"
      value={metrics.views}
      change={{ value: metrics.viewsChange, trend: metrics.viewsChange > 0 ? 'up' : 'down' }}
      icon={Eye}
    />
    <StatCard
      title="Product Views"
      value={metrics.productViews}
      change={{ value: metrics.productViewsChange, trend: 'up' }}
      icon={Package}
    />
    <StatCard
      title="Add to Carts"
      value={metrics.addToCarts}
      change={{ value: metrics.cartsChange, trend: 'up' }}
      icon={ShoppingCart}
    />
    <StatCard
      title="Conversion Rate"
      value={`${metrics.conversionRate}%`}
      change={{ value: metrics.conversionChange, trend: 'up' }}
      icon={TrendingUp}
    />
  </div>

  {/* Traffic Sources */}
  <Card>
    <CardHeader>
      <CardTitle>Traffic Sources</CardTitle>
    </CardHeader>
    <CardContent>
      <div className="space-y-4">
        {trafficSources.map((source) => (
          <div key={source.name} className="space-y-2">
            <div className="flex justify-between text-sm">
              <span className="flex items-center gap-2">
                <source.icon className="h-4 w-4 text-muted-foreground" />
                {source.name}
              </span>
              <span className="font-medium">{source.percentage}%</span>
            </div>
            <Progress value={source.percentage} className="h-2" />
          </div>
        ))}
      </div>
    </CardContent>
  </Card>

  {/* Top Products */}
  <Card>
    <CardHeader>
      <CardTitle>Top Performing Products</CardTitle>
    </CardHeader>
    <CardContent>
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Product</TableHead>
            <TableHead>Views</TableHead>
            <TableHead>Cart Adds</TableHead>
            <TableHead>Sales</TableHead>
            <TableHead>Conversion</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {topProducts.map((product) => (
            <TableRow key={product.id}>
              <TableCell>
                <div className="flex items-center gap-3">
                  <Image
                    src={product.image}
                    alt={product.name}
                    width={40}
                    height={40}
                    className="rounded"
                  />
                  <span className="font-medium">{product.name}</span>
                </div>
              </TableCell>
              <TableCell>{product.views}</TableCell>
              <TableCell>{product.cartAdds}</TableCell>
              <TableCell>{product.sales}</TableCell>
              <TableCell>
                <Badge variant={product.conversion > 5 ? 'success' : 'secondary'}>
                  {product.conversion}%
                </Badge>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </CardContent>
  </Card>
</div>
```

---

## Key UX Principles for Storefronts

### 1. Brand Expression Within Guardrails
- Allow customization but maintain platform consistency
- Pre-defined color palettes and layouts
- Logo and cover image as primary brand elements

### 2. Mobile-First Storefront Management
- Managers often update from phones
- Quick photo upload from camera
- Simplified mobile editing interface

### 3. Real-Time Preview
- WYSIWYG editing experience
- See changes before publishing
- Mobile/desktop preview toggle

### 4. Customer Trust Signals
- Verified badges prominently displayed
- Response time indicators
- Order fulfillment metrics

### 5. Performance Visibility
- Easy-to-understand metrics
- Actionable insights
- Comparison with benchmarks
