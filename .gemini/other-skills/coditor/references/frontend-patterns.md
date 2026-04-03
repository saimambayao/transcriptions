# Frontend Pattern Detection

Pattern detection rules for OBCMS frontend code (HTMX, Alpine.js, Tailwind CSS).

## HTMX Patterns

**Severity**: Medium

### Pattern 1: Inline Event Handlers Instead of HTMX

**Detection**: onclick/onsubmit handlers where HTMX should be used.

**Example Violation**:
```html
<!-- ❌ MEDIUM: Inline handler -->
<button onclick="deleteTask(123)">Delete</button>
```

**Remediation**:
```html
<!-- ✅ CORRECT: Use HTMX -->
<button hx-delete="/api/tasks/123/" hx-confirm="Delete this task?">Delete</button>
```

### Pattern 2: Missing HTMX Indicators

**Detection**: HTMX requests without loading indicators.

**Example Violation**:
```html
<!-- ❌ MEDIUM: No loading indicator -->
<button hx-post="/api/submit/">Submit</button>
```

**Remediation**:
```html
<!-- ✅ CORRECT: With indicator -->
<button hx-post="/api/submit/" hx-indicator="#spinner">Submit</button>
<div id="spinner" class="htmx-indicator">Loading...</div>
```

### Pattern 3: Missing CSRF in HTMX

**Detection**: HTMX POST/PUT/DELETE without CSRF token configuration.

**Required**: CSRF token in meta tag + HTMX config:
```html
<meta name="csrf-token" content="{{ csrf_token }}">
<script src="{% static 'js/htmx-config.js' %}"></script>
```

---

## Alpine.js Patterns

**Severity**: Medium

### Pattern 1: Complex Logic in x-data

**Detection**: Alpine.js x-data with complex functions or API calls.

**Example Violation**:
```html
<!-- ❌ MEDIUM: Complex logic inline -->
<div x-data="{ items: [], async load() { const res = await fetch('/api/items'); this.items = await res.json(); } }">
</div>
```

**Remediation**:
```html
<!-- ✅ CORRECT: Use Alpine.data() -->
<div x-data="itemLoader"></div>

<script nonce="{{ request.csp_nonce }}">
document.addEventListener('alpine:init', () => {
    Alpine.data('itemLoader', () => ({
        items: [],
        async load() {
            const res = await fetch('/api/items');
            this.items = await res.json();
        }
    }));
});
</script>
```

### Pattern 2: Duplicate Alpine Components

**Detection**: Same Alpine.js component logic repeated across files.

**Remediation**: Extract to shared Alpine.data() in external JS file.

---

## Tailwind CSS Patterns

**Severity**: Low

### Pattern 1: Inline Style Attributes

**Detection**: style="..." attributes where Tailwind classes should be used.

**Example Violation**:
```html
<!-- ❌ LOW: Inline styles -->
<div style="padding: 1rem; margin-top: 2rem; background-color: #3b82f6;">
```

**Remediation**:
```html
<!-- ✅ CORRECT: Tailwind classes -->
<div class="p-4 mt-8 bg-blue-500">
```

### Pattern 2: Non-Standard Color Classes

**Detection**: Custom color classes instead of Tailwind's semantic colors.

**OBCMS Semantic Colors**:
- Primary: Blue-green gradient (bg-gradient-to-r from-blue-500 to-emerald-500)
- Success: green-500
- Warning: yellow-500
- Danger: red-500
- Info: blue-500

**Example Violation**:
```html
<!-- ❌ LOW: Non-standard color -->
<button class="bg-purple-500">Submit</button>
```

**Remediation**:
```html
<!-- ✅ CORRECT: OBCMS standard color -->
<button class="bg-blue-500">Submit</button>
```

### Pattern 3: Inconsistent Spacing

**Detection**: Mixing spacing units (p-2 with p-6 in similar contexts).

**OBCMS Standard Spacing**:
- Tight: p-2, m-2
- Normal: p-4, m-4
- Loose: p-6, m-6

---

## Accessibility Patterns

**Severity**: Medium

### Pattern 1: Missing ARIA Labels

**Detection**: Interactive elements without labels or ARIA attributes.

**Example Violation**:
```html
<!-- ❌ MEDIUM: No label -->
<button hx-delete="/api/tasks/123/">
    <i class="icon-trash"></i>
</button>
```

**Remediation**:
```html
<!-- ✅ CORRECT: ARIA label -->
<button hx-delete="/api/tasks/123/" aria-label="Delete task">
    <i class="icon-trash"></i>
</button>
```

### Pattern 2: Missing Alt Text on Images

**Detection**: <img> tags without alt attributes.

**Example Violation**:
```html
<!-- ❌ MEDIUM: No alt text -->
<img src="/media/logo.png">
```

**Remediation**:
```html
<!-- ✅ CORRECT: Descriptive alt text -->
<img src="/media/logo.png" alt="OBCMS Logo">
```

### Pattern 3: Poor Color Contrast

**Detection**: Text on backgrounds with insufficient contrast (<4.5:1).

**Tools**: Use browser DevTools Accessibility panel.

---

## CSP Compliance

**Severity**: High

See [security-patterns.md](security-patterns.md#csp-violations) for comprehensive CSP patterns.

**Quick Checklist**:
- [ ] No inline <script> without nonces
- [ ] No inline <style> without nonces
- [ ] No inline event handlers (onclick, onload, etc.)
- [ ] No inline style="" attributes
- [ ] HTMX attributes used for interactions
- [ ] Tailwind classes used for styling

---

## Audit Checklist

- [ ] HTMX used for dynamic interactions (no inline onclick)
- [ ] HTMX requests have loading indicators
- [ ] CSRF token configured for HTMX
- [ ] Complex Alpine.js logic uses Alpine.data()
- [ ] Tailwind classes used (no inline styles)
- [ ] OBCMS semantic colors used
- [ ] Interactive elements have ARIA labels
- [ ] Images have alt text
- [ ] Color contrast meets WCAG AA (4.5:1)
- [ ] All frontend code is CSP-compliant
