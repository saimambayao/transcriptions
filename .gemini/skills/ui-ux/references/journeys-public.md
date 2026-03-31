# Public Portal User Journeys

User journey maps and UX patterns for consumers on the Negosyo marketplace.

## Table of Contents
- [User Personas](#user-personas)
- [Discovery Journey](#discovery-journey)
- [Purchase Journey](#purchase-journey)
- [Account Journey](#account-journey)
- [Storefront Journey](#storefront-journey)

## BARMM Context (BDP 2023-2028)

The Bangsamoro Development Plan 2023-2028 establishes the foundation for understanding user needs in the region. Key context for marketplace design:

### Regional Vision
"A Bangsamoro that is united, enlightened, self-governing, peaceful, just, morally upright, and progressive."

### Development Goals Relevant to Marketplace
- **Goal 2**: Equitable, competitive, and robust economy - economic gains benefiting all, especially poor and marginalized
- **Goal 4**: Inclusive, responsive, and quality social services - leaving no one behind regardless of tribe or affiliation
- **Macroeconomic Target**: Reduce poverty incidence from 29.8% (2021) to 20-25% by 2028

### Geographic Context
- **5 Provinces**: Basilan, Lanao del Sur, Maguindanao, Sulu, Tawi-Tawi
- **Cities**: Marawi City, Lamitan City, Cotabato City
- **Special Geographic Area (SGA)**: 63 barangays in North Cotabato
- **Island Provinces (BaSulTa)**: Basilan, Sulu, Tawi-Tawi - geographically isolated areas with unique logistics challenges

### Key Economic Indicators
- Population: 4.94 million (2020), fastest growing in Philippines at 3.26% annual growth
- Working age population: 2.79 million
- Underemployment: Rural phenomenon, target 4-7%
- AFF sector dominance with growing industry/services

---

## User Personas

### Casual Browser (Bangsamoro Consumer)
- **Goal**: Explore quality products from local cooperatives and social enterprises
- **Behavior**: Browses without intent to buy immediately, curious about local producers
- **Needs**: Easy navigation, no login walls, inspiring impact stories
- **BARMM Context**: May be in areas with limited connectivity; values support for local economy

### Intentional Buyer (Urban/Peri-Urban Consumer)
- **Goal**: Find and purchase specific product from trusted source
- **Behavior**: Uses search, compares options, checks reviews and seller verification
- **Needs**: Fast search, clear pricing, trust signals, secure payment
- **BARMM Context**: Located in Cotabato City, Marawi, or municipal centers with better connectivity

### Repeat Customer (Established Buyer)
- **Goal**: Reorder or find similar products from trusted cooperatives
- **Behavior**: Returns to saved items, checks order history, builds relationships with sellers
- **Needs**: Quick reorder, personalized recommendations, loyalty benefits
- **BARMM Context**: Values ongoing relationship with local producers

### Impact-Conscious Shopper (Development-Minded Consumer)
- **Goal**: Support local cooperatives/social enterprises to reduce poverty and create jobs
- **Behavior**: Reads about sellers, values transparency, interested in community impact
- **Needs**: Seller stories, impact metrics (members supported, jobs created), FRAMES certification badges
- **BARMM Context**: Understands role of coops/SEs in achieving BDP Goal 2 (equitable economy)

### Diaspora Buyer (OFW/External Bangsamoro)
- **Goal**: Support home region by purchasing authentic Bangsamoro products
- **Behavior**: Looks for culturally significant items, gift purchases for family
- **Needs**: Reliable shipping, product authenticity, cultural storytelling
- **BARMM Context**: Part of broader Bangsamoro identity; may order for family still in region

### Institutional Buyer (Government/NGO Procurer)
- **Goal**: Source products from verified cooperatives for programs or institutional use
- **Behavior**: Bulk ordering, requires documentation, compliance verification
- **Needs**: Invoice generation, bulk pricing, compliance certificates, supplier verification
- **BARMM Context**: Supporting social protection programs (4Ps, SLP) or development partner initiatives

---

## Discovery Journey

### Flow: Homepage → Browse → Product Detail

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Homepage   │───▶│  Category   │───▶│  Product    │───▶│  Add to     │
│             │    │  Listing    │    │  Detail     │    │  Cart       │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
      │                  │                  │
      ▼                  ▼                  ▼
  Hero banner       Filters/sort      Images, price,
  Categories        Product cards     reviews, seller
  Featured items    Pagination        Add to cart CTA
```

### Stage 1: Homepage (Awareness)

**User Goal**: Understand what the platform offers

**Must-Have Elements**:
```tsx
// Hero Section
<section className="relative h-[400px] md:h-[500px]">
  <Image src="/hero.jpg" alt="..." fill className="object-cover" />
  <div className="absolute inset-0 bg-gradient-to-r from-black/60 to-transparent">
    <div className="container h-full flex items-center">
      <div className="max-w-xl text-white">
        <h1 className="text-3xl md:text-5xl font-bold">
          Support Bangsamoro Cooperatives
        </h1>
        <p className="mt-4 text-lg">
          Discover quality products from local social enterprises
        </p>
        <div className="mt-6 flex gap-4">
          <Button size="lg">Shop Now</Button>
          <Button size="lg" variant="outline">Learn More</Button>
        </div>
      </div>
    </div>
  </div>
</section>
```

**Critical UX Points**:
- Value proposition visible in <3 seconds
- Primary CTA above the fold
- Category navigation immediately accessible
- No login required to browse

### Stage 2: Category/Search (Consideration)

**User Goal**: Find relevant products

**Must-Have Elements**:
```tsx
// Category Page Layout
<div className="container py-6">
  {/* Breadcrumb */}
  <Breadcrumb items={[
    { label: 'Home', href: '/' },
    { label: 'Food & Beverages', href: '/category/food' },
  ]} />

  <div className="flex gap-6 mt-6">
    {/* Filters Sidebar - Desktop */}
    <aside className="hidden lg:block w-64 shrink-0">
      <FilterPanel
        categories={categories}
        priceRange={priceRange}
        ratings={ratings}
        regions={regions}
      />
    </aside>

    {/* Product Grid */}
    <main className="flex-1">
      <div className="flex items-center justify-between mb-4">
        <p className="text-sm text-muted-foreground">
          {count} products found
        </p>
        <SortSelect options={sortOptions} />
      </div>

      {/* Mobile Filter Button */}
      <Sheet>
        <SheetTrigger asChild className="lg:hidden mb-4">
          <Button variant="outline" className="w-full">
            <Filter className="h-4 w-4 mr-2" />
            Filters
          </Button>
        </SheetTrigger>
        <SheetContent side="left">
          <FilterPanel {...filterProps} />
        </SheetContent>
      </Sheet>

      <ProductGrid products={products} />
      <Pagination {...paginationProps} />
    </main>
  </div>
</div>
```

**Filter UX Best Practices**:
- Show active filter count on mobile button
- Instant filtering (no "Apply" button needed)
- Clear all filters option
- Show result count after filtering
- Persist filters in URL for shareability

### Stage 3: Product Detail (Evaluation)

**User Goal**: Decide whether to purchase

**Critical Information Hierarchy**:
1. Product images (largest visual element)
2. Name and price
3. Seller/cooperative info with rating
4. Add to cart button
5. Product description
6. Reviews and ratings

```tsx
// Product Detail Page Structure
<div className="container py-6">
  <Breadcrumb items={breadcrumbs} />

  <div className="grid lg:grid-cols-2 gap-8 mt-6">
    {/* Left: Images */}
    <ProductGallery images={product.images} />

    {/* Right: Info */}
    <div className="space-y-6">
      {/* Seller Badge */}
      <Link href={`/store/${product.seller.slug}`}>
        <div className="flex items-center gap-2 text-sm">
          <Avatar className="h-6 w-6">
            <AvatarImage src={product.seller.logo} />
          </Avatar>
          <span className="text-muted-foreground">
            {product.seller.name}
          </span>
          {product.seller.verified && (
            <BadgeCheck className="h-4 w-4 text-primary" />
          )}
        </div>
      </Link>

      {/* Product Name */}
      <h1 className="text-2xl font-bold">{product.name}</h1>

      {/* Rating */}
      <div className="flex items-center gap-2">
        <StarRating value={product.rating} />
        <span className="text-sm text-muted-foreground">
          ({product.reviewCount} reviews)
        </span>
      </div>

      {/* Price */}
      <div className="text-3xl font-bold">
        PHP {product.price.toLocaleString()}
        {product.originalPrice && (
          <span className="ml-2 text-lg text-muted-foreground line-through">
            PHP {product.originalPrice.toLocaleString()}
          </span>
        )}
      </div>

      {/* Variants */}
      {product.variants && (
        <VariantSelector variants={product.variants} />
      )}

      {/* Quantity */}
      <QuantitySelector max={product.stock} />

      {/* Add to Cart - Sticky on mobile */}
      <div className="flex gap-4">
        <Button className="flex-1" size="lg">
          <ShoppingCart className="h-5 w-5 mr-2" />
          Add to Cart
        </Button>
        <Button variant="outline" size="lg">
          <Heart className="h-5 w-5" />
        </Button>
      </div>

      {/* Trust Signals */}
      <div className="grid grid-cols-3 gap-4 pt-4 border-t">
        <TrustBadge icon={Truck} label="Free Shipping" sublabel="Orders over PHP 500" />
        <TrustBadge icon={Shield} label="Secure Payment" sublabel="SSL Encrypted" />
        <TrustBadge icon={RotateCcw} label="Easy Returns" sublabel="7-day policy" />
      </div>
    </div>
  </div>

  {/* Tabs: Description, Reviews, Seller Info */}
  <Tabs defaultValue="description" className="mt-12">
    <TabsList>
      <TabsTrigger value="description">Description</TabsTrigger>
      <TabsTrigger value="reviews">Reviews ({product.reviewCount})</TabsTrigger>
      <TabsTrigger value="seller">About Seller</TabsTrigger>
    </TabsList>
    <TabsContent value="description">
      <ProductDescription content={product.description} />
    </TabsContent>
    <TabsContent value="reviews">
      <ProductReviews productId={product.id} />
    </TabsContent>
    <TabsContent value="seller">
      <SellerProfile seller={product.seller} />
    </TabsContent>
  </Tabs>
</div>

{/* Mobile Sticky CTA */}
<div className="fixed bottom-0 left-0 right-0 p-4 bg-background border-t lg:hidden">
  <div className="flex items-center gap-4">
    <div className="flex-1">
      <p className="text-lg font-bold">PHP {product.price.toLocaleString()}</p>
    </div>
    <Button size="lg">Add to Cart</Button>
  </div>
</div>
```

---

## Purchase Journey

### Flow: Cart → Checkout → Payment → Confirmation

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│    Cart     │───▶│  Checkout   │───▶│   Payment   │───▶│ Confirmation│
│             │    │  (Address)  │    │             │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                         │
                         ▼
                   Guest checkout
                   OR Sign in
```

### Cart Page

**Critical Drop-off Prevention**:
- Show item images (not just names)
- Display total prominently
- Show shipping estimate early
- Offer guest checkout option

```tsx
// Cart Summary Card
<Card className="sticky top-4">
  <CardHeader>
    <CardTitle>Order Summary</CardTitle>
  </CardHeader>
  <CardContent className="space-y-4">
    <div className="flex justify-between">
      <span>Subtotal ({itemCount} items)</span>
      <span>PHP {subtotal.toLocaleString()}</span>
    </div>
    <div className="flex justify-between">
      <span>Shipping</span>
      <span className="text-green-600">
        {shipping === 0 ? 'FREE' : `PHP ${shipping}`}
      </span>
    </div>
    {discount > 0 && (
      <div className="flex justify-between text-green-600">
        <span>Discount</span>
        <span>-PHP {discount.toLocaleString()}</span>
      </div>
    )}
    <Separator />
    <div className="flex justify-between text-lg font-bold">
      <span>Total</span>
      <span>PHP {total.toLocaleString()}</span>
    </div>
  </CardContent>
  <CardFooter className="flex-col gap-2">
    <Button className="w-full" size="lg">
      Proceed to Checkout
    </Button>
    <p className="text-xs text-center text-muted-foreground">
      Taxes calculated at checkout
    </p>
  </CardFooter>
</Card>
```

### Checkout Flow

**3-Step Maximum**:
1. Contact/Address
2. Shipping Method
3. Payment

```tsx
// Checkout Progress
<div className="flex items-center justify-center gap-4 mb-8">
  {steps.map((step, i) => (
    <div key={step.id} className="flex items-center">
      <div className={cn(
        "flex items-center justify-center w-8 h-8 rounded-full text-sm font-medium",
        i < currentStep && "bg-primary text-primary-foreground",
        i === currentStep && "bg-primary text-primary-foreground ring-4 ring-primary/20",
        i > currentStep && "bg-muted text-muted-foreground"
      )}>
        {i < currentStep ? <Check className="h-4 w-4" /> : i + 1}
      </div>
      <span className={cn(
        "ml-2 text-sm hidden sm:inline",
        i <= currentStep ? "font-medium" : "text-muted-foreground"
      )}>
        {step.label}
      </span>
      {i < steps.length - 1 && (
        <div className={cn(
          "w-8 sm:w-16 h-0.5 mx-2",
          i < currentStep ? "bg-primary" : "bg-muted"
        )} />
      )}
    </div>
  ))}
</div>
```

**Guest Checkout Prominence**:
```tsx
// Checkout Entry
<div className="space-y-4">
  <Button className="w-full" size="lg" variant="outline">
    Continue as Guest
  </Button>

  <div className="relative">
    <Separator />
    <span className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-background px-2 text-sm text-muted-foreground">
      or
    </span>
  </div>

  <Button className="w-full" size="lg">
    Sign In for Faster Checkout
  </Button>
</div>
```

### Order Confirmation

**Build Trust & Reduce Anxiety**:
```tsx
// Confirmation Page
<div className="container max-w-2xl py-12">
  <div className="text-center mb-8">
    <div className="h-16 w-16 rounded-full bg-green-100 flex items-center justify-center mx-auto mb-4">
      <Check className="h-8 w-8 text-green-600" />
    </div>
    <h1 className="text-2xl font-bold">Order Confirmed!</h1>
    <p className="text-muted-foreground mt-2">
      Order #{orderId} • {formatDate(orderDate)}
    </p>
  </div>

  {/* Order Timeline */}
  <Card className="mb-6">
    <CardContent className="pt-6">
      <OrderTimeline status={orderStatus} />
    </CardContent>
  </Card>

  {/* What's Next */}
  <Card>
    <CardHeader>
      <CardTitle>What's Next?</CardTitle>
    </CardHeader>
    <CardContent className="space-y-4">
      <div className="flex gap-4">
        <Mail className="h-5 w-5 text-muted-foreground shrink-0" />
        <div>
          <p className="font-medium">Check your email</p>
          <p className="text-sm text-muted-foreground">
            We sent a confirmation to {email}
          </p>
        </div>
      </div>
      <div className="flex gap-4">
        <Package className="h-5 w-5 text-muted-foreground shrink-0" />
        <div>
          <p className="font-medium">Track your order</p>
          <p className="text-sm text-muted-foreground">
            Estimated delivery: {estimatedDelivery}
          </p>
        </div>
      </div>
    </CardContent>
    <CardFooter className="flex gap-4">
      <Button variant="outline" asChild>
        <Link href="/account/orders">View Order</Link>
      </Button>
      <Button asChild>
        <Link href="/">Continue Shopping</Link>
      </Button>
    </CardFooter>
  </Card>
</div>
```

---

## Account Journey

### Registration Flow (Progressive)

Don't require account creation upfront. Prompt after value is delivered:

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Purchase   │───▶│  Prompt to  │───▶│  Create     │
│  Complete   │    │  Save Info  │    │  Account    │
└─────────────┘    └─────────────┘    └─────────────┘
```

```tsx
// Post-Purchase Account Prompt
<Card className="bg-muted/50">
  <CardContent className="pt-6">
    <div className="flex gap-4">
      <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center shrink-0">
        <UserPlus className="h-6 w-6 text-primary" />
      </div>
      <div>
        <h3 className="font-medium">Save your information</h3>
        <p className="text-sm text-muted-foreground mt-1">
          Create an account to track orders and checkout faster next time
        </p>
        <div className="flex gap-2 mt-4">
          <Button size="sm">Create Account</Button>
          <Button size="sm" variant="ghost">Not Now</Button>
        </div>
      </div>
    </div>
  </CardContent>
</Card>
```

---

## Storefront Journey

### Individual Cooperative/SE Store Pages

**User Goal**: Learn about and trust a specific seller

```tsx
// Storefront Header
<div className="border-b">
  <div className="container py-8">
    <div className="flex flex-col md:flex-row gap-6 items-start">
      {/* Store Logo */}
      <Avatar className="h-24 w-24">
        <AvatarImage src={store.logo} />
        <AvatarFallback>{store.name[0]}</AvatarFallback>
      </Avatar>

      {/* Store Info */}
      <div className="flex-1">
        <div className="flex items-center gap-2">
          <h1 className="text-2xl font-bold">{store.name}</h1>
          {store.verified && (
            <Badge variant="secondary">
              <BadgeCheck className="h-3 w-3 mr-1" />
              Verified
            </Badge>
          )}
        </div>

        <p className="text-muted-foreground mt-1">{store.tagline}</p>

        <div className="flex flex-wrap gap-4 mt-4 text-sm">
          <div className="flex items-center gap-1">
            <Star className="h-4 w-4 fill-yellow-400 text-yellow-400" />
            <span className="font-medium">{store.rating}</span>
            <span className="text-muted-foreground">
              ({store.reviewCount} reviews)
            </span>
          </div>
          <div className="flex items-center gap-1 text-muted-foreground">
            <Package className="h-4 w-4" />
            {store.productCount} products
          </div>
          <div className="flex items-center gap-1 text-muted-foreground">
            <MapPin className="h-4 w-4" />
            {store.location}
          </div>
        </div>

        {/* Impact Stats */}
        <div className="grid grid-cols-3 gap-4 mt-6 p-4 bg-muted rounded-lg">
          <div className="text-center">
            <p className="text-2xl font-bold text-primary">{store.members}</p>
            <p className="text-xs text-muted-foreground">Members</p>
          </div>
          <div className="text-center">
            <p className="text-2xl font-bold text-primary">{store.yearsActive}</p>
            <p className="text-xs text-muted-foreground">Years Active</p>
          </div>
          <div className="text-center">
            <p className="text-2xl font-bold text-primary">{store.ordersFulfilled}</p>
            <p className="text-xs text-muted-foreground">Orders Fulfilled</p>
          </div>
        </div>
      </div>

      {/* Actions */}
      <div className="flex gap-2 shrink-0">
        <Button variant="outline">
          <Heart className="h-4 w-4 mr-2" />
          Follow
        </Button>
        <Button variant="outline">
          <MessageCircle className="h-4 w-4 mr-2" />
          Contact
        </Button>
      </div>
    </div>
  </div>
</div>

{/* Store Navigation */}
<div className="border-b sticky top-0 bg-background z-10">
  <div className="container">
    <nav className="flex gap-6 -mb-px">
      <TabLink href={`/store/${slug}`} active={tab === 'products'}>
        Products
      </TabLink>
      <TabLink href={`/store/${slug}/about`} active={tab === 'about'}>
        About Us
      </TabLink>
      <TabLink href={`/store/${slug}/reviews`} active={tab === 'reviews'}>
        Reviews
      </TabLink>
      <TabLink href={`/store/${slug}/policies`} active={tab === 'policies'}>
        Policies
      </TabLink>
    </nav>
  </div>
</div>
```

---

## Emotional Journey Map

| Stage | User Feeling | Design Response |
|-------|-------------|-----------------|
| Discovery | Curious | Inspiring visuals, easy browsing |
| Evaluation | Cautious | Reviews, seller info, trust badges |
| Cart | Committed | Clear summary, no surprises |
| Checkout | Anxious | Progress indicator, security badges |
| Payment | Nervous | Payment logos, SSL indicator |
| Confirmation | Relieved | Clear confirmation, next steps |
| Delivery | Anticipating | Tracking updates, communication |
| Post-Purchase | Satisfied/Dissatisfied | Easy returns, review prompt |

---

## BARMM-Specific UX Considerations (BDP 2023-2028)

### Vulnerable Population Groups
Based on BDP 2023-2028 Chapter 9, the marketplace must consider these user segments:

| Group | Population/Stats | Design Implications |
|-------|------------------|---------------------|
| **Poor Families** | 29.8% poverty incidence (2021) | Affordable products, clear pricing, no hidden fees |
| **Women** | Key entrepreneurship target | Gender-sensitive design, safety features |
| **Youth (15-24)** | High unemployment | Mobile-first, entry-level products, skill-building links |
| **Senior Citizens** | 159,172 indigent seniors served | Large text, simple navigation, accessible design |
| **PWDs** | 53,483 registered | WCAG compliance, assistive technology support |
| **IDPs** | 93,525 displaced persons | Flexible delivery addresses, trauma-informed messaging |
| **Indigenous Peoples** | Present in Maguindanao, Lanao del Sur | Cultural sensitivity, traditional product categories |

### Geographic Accessibility Design
Based on BARMM's geographic distribution:

| Province/Area | Consideration | Design Response |
|---------------|---------------|-----------------|
| **Island Provinces (BaSulTa)** | Limited connectivity, shipping challenges | Offline browsing, inter-island shipping options |
| **Mainland (Maguindanao, Lanao del Sur)** | Better connectivity, road access | Standard e-commerce patterns |
| **SGA (North Cotabato)** | Transitional area | Clear jurisdiction display |
| **GIDA Areas** | Far-flung, limited services | Community pickup points, bulk ordering |
| **Urban Centers** | Cotabato City, Marawi, Lamitan | Full feature access, express delivery |

### Trust Signals for BARMM Context
Given historical challenges, marketplace must build trust:

1. **CSEA Verification Badge** - Shows cooperative/SE is registered and FRAMES-compliant
2. **Provincial Origin Tag** - Indicates where products come from (builds local pride)
3. **Development Partner Endorsement** - Products supported by recognized organizations
4. **Member Count Display** - Shows cooperative size (jobs supported)
5. **Impact Metrics** - Families benefited, livelihood created
6. **Cultural Authenticity** - Certification for traditional crafts/products

### Social Protection Integration
Marketplace should support access for beneficiaries of:
- **4Ps (Pantawid Pamilyang Pilipino Program)** - Low-income family support
- **SLP (Sustainable Livelihood Program)** - Livelihood assistance
- **Social Pension** - Support for indigent senior citizens
- **MSSD Programs** - Various social welfare interventions

### Health and Nutrition Product Priorities
Given BDP 2023-2028 health context:
- **Malnutrition prevalence**: 39.1% stunting, 10% wasting
- **Marketplace Response**: Highlight nutritious food products, fortified items
- **Categorization**: "Nutrition-Focused" product tags
- **Producer Stories**: Connect products to health outcomes

## Key Metrics to Track

| Stage | Metric | Target |
|-------|--------|--------|
| Discovery | Bounce rate | <40% |
| Evaluation | Product page → Cart | >10% |
| Cart | Cart → Checkout | >60% |
| Checkout | Checkout completion | >70% |
| Overall | Conversion rate | >3% |
