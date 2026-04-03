# Research Methodology and Source Priorities

This reference defines how to conduct thorough research and prioritize sources when investigating errors.

## Source Priority Hierarchy

When researching solutions, prioritize sources in this order:

### Tier 1: Official Documentation (Highest Priority)

**Why**: Authoritative, maintained, version-specific, comprehensive

**Sources**:
- Official framework/library documentation (Django, HTMX, Celery, PostgreSQL, etc.)
- Official API references
- Official migration guides
- Official security advisories

**How to Use**:
- Start here for API usage questions
- Verify syntax and parameters
- Check version compatibility
- Review best practices sections

**Examples**:
- https://docs.djangoproject.com/
- https://htmx.org/docs/
- https://docs.celeryq.dev/
- https://www.postgresql.org/docs/

---

### Tier 2: Official GitHub Issues (High Priority)

**Why**: Real-world problems, maintainer responses, version-specific bugs

**Sources**:
- GitHub Issues in official repositories
- Pull requests with bug fixes
- Release notes and changelogs
- Official discussions

**How to Use**:
- Search for exact error messages
- Look for closed issues with solutions
- Check if bug is fixed in newer versions
- Review linked pull requests for fixes

**Examples**:
- https://github.com/django/django/issues
- https://github.com/bigskysoftware/htmx/issues
- https://github.com/celery/celery/issues

---

### Tier 3: Technical Communities (Medium Priority)

**Why**: Practical solutions, community validation, diverse scenarios

**Sources**:
- Stack Overflow
- Reddit (r/django, r/webdev, etc.)
- Django Forum
- PostgreSQL Mailing Lists

**How to Use**:
- Look for accepted answers with high votes
- Check answer recency (prefer recent solutions)
- Verify solution matches your version
- Read multiple answers for perspective

**Filters**:
- Stack Overflow: Sort by votes, check accepted answer
- Reddit: Look for upvoted comments from experienced users
- Forums: Check for moderator/expert responses

---

### Tier 4: Technical Blogs and Tutorials (Lower Priority)

**Why**: Detailed explanations, real-world examples, context

**Sources**:
- Developer blogs
- Tutorial sites (Real Python, SimpleIsBetterThanComplex, etc.)
- Company engineering blogs
- Personal technical blogs

**How to Use**:
- Verify author credentials
- Check publication date (prefer recent)
- Cross-reference with official docs
- Look for working code examples

**Red Flags**:
- Outdated content (>2 years old)
- No code examples
- Contradicts official documentation
- Poorly explained concepts

**Reputable Sources**:
- Real Python
- Django Stars Blog
- TestDriven.io
- Mozilla Developer Network (MDN)

---

### Tier 5: General Search Results (Lowest Priority)

**Why**: Least reliable, often outdated, unverified

**Use Only When**:
- Higher-tier sources don't address the specific issue
- Need general background understanding
- Looking for alternative perspectives

**Caution**:
- Always cross-reference with official docs
- Verify code examples work in your version
- Check publication date
- Look for author expertise

---

## Research Process

### 1. Define the Investigation Scope

Before researching, clearly define:
- **Exact error message**: Copy the full error text
- **Error context**: What action triggered it?
- **Environment**: Local dev, staging, production?
- **Recent changes**: What changed before the error?
- **Frequency**: Consistent, intermittent, or one-time?

### 2. Gather Local Evidence

**Before searching online**, collect:
- Full error stack trace
- Relevant code sections
- Configuration files
- Log excerpts (10-20 lines before/after error)
- Request/response data (if applicable)

### 3. Search Strategy

**Step 1: Exact Error Search**
- Google: `"exact error message" django` (or relevant framework)
- Include quotes for exact match
- Add framework/library name

**Step 2: Conceptual Search**
- Search for the concept if exact search fails
- Example: "Django N+1 queries" instead of specific error
- Include version: "Django 5.2 performance"

**Step 3: Comparative Search**
- Search for alternative approaches
- "Django select_related vs prefetch_related"
- "Best practices for [specific task]"

**Step 4: GitHub Issues Search**
- Use GitHub's issue search
- Filter by: is:issue, is:closed, label:bug
- Search in relevant repositories

### 4. Evidence Validation

For each source found, validate:

**Authority**:
- ✅ Official documentation
- ✅ Maintainer/core team responses
- ✅ Highly upvoted community answers
- ❌ Unverified personal blogs
- ❌ Outdated tutorials

**Recency**:
- ✅ Published/updated within last 2 years
- ✅ Matches your framework version
- ⚠️ Older content (verify still applicable)
- ❌ Pre-major-version content (e.g., Django 2.x for Django 5.x)

**Completeness**:
- ✅ Includes working code examples
- ✅ Explains why the solution works
- ✅ Mentions trade-offs or limitations
- ❌ Just says "it works for me"
- ❌ No explanation of the fix

**Applicability**:
- ✅ Matches your tech stack
- ✅ Addresses your specific scenario
- ✅ Compatible with your constraints (CSP, multi-tenant, etc.)
- ❌ Different framework version
- ❌ Different use case

### 5. Cross-Reference Solutions

**Never rely on a single source**. For each potential solution:

1. Find **at least 5 sources** supporting the approach
2. Check **official docs** confirm the pattern
3. Look for **counter-arguments** or warnings
4. Review **performance implications**
5. Check **security considerations**

---

## Solution Ranking Criteria

When presenting multiple solutions, rank by:

### 1. Effectiveness (Most Important)

**High Effectiveness**:
- Addresses root cause, not symptoms
- Supported by official documentation
- Verified by multiple independent sources
- Has evidence of working in production

**Medium Effectiveness**:
- Addresses symptoms but may not fix root cause
- Mentioned in community discussions
- Partially verified

**Low Effectiveness**:
- Workaround or temporary fix
- Unverified approach
- Single source only

### 2. Risk Assessment

**Low Risk**:
- Official recommended approach
- Backward compatible
- No breaking changes required
- Easy to revert

**Medium Risk**:
- Requires configuration changes
- May affect other features
- Needs thorough testing

**High Risk**:
- Major refactoring required
- Breaking changes
- Potential data loss
- Difficult to revert

### 3. Implementation Effort

**Low Effort**:
- Configuration change only
- Single file modification
- No dependencies

**Medium Effort**:
- Multiple file changes
- Requires new dependencies
- Needs migration

**High Effort**:
- Architectural changes
- Extensive refactoring
- Multiple migrations

### 4. Maintenance Burden

**Low Maintenance**:
- Standard pattern
- Well-documented
- Community support

**Medium Maintenance**:
- Custom implementation
- Requires documentation

**High Maintenance**:
- Complex workaround
- Fragile solution
- High technical debt

---

## Presenting Evidence

For each solution, provide evidence in this format:

### Solution Format

```markdown
## Solution X: [Descriptive Name]

**Approach**: [1-2 sentence summary]

**Effectiveness**: High/Medium/Low
**Risk**: Low/Medium/High
**Effort**: Low/Medium/High
**Maintenance**: Low/Medium/High

### Evidence Sources:

1. **[Source Type]**: [Title/Description]
   - URL: [link]
   - Key finding: [quote or summary]
   - Relevance: [why this matters]

2. **[Source Type]**: [Title/Description]
   - URL: [link]
   - Key finding: [quote or summary]
   - Relevance: [why this matters]

[... 5 sources total]

### Implementation Overview:

[Brief description of what needs to change]

### Trade-offs:

**Pros**:
- [Benefit 1]
- [Benefit 2]

**Cons**:
- [Limitation 1]
- [Limitation 2]

### Validation Steps:

1. [How to verify the fix works]
2. [How to test for regressions]
```

---

## Common Research Pitfalls to Avoid

### ❌ Don't: Copy-paste without understanding
**Why**: May introduce security issues or incompatibilities
**Do Instead**: Understand the solution, adapt to your context

### ❌ Don't: Trust outdated sources
**Why**: APIs change, best practices evolve
**Do Instead**: Verify publication date, check current version compatibility

### ❌ Don't: Mix solutions from different versions
**Why**: Incompatible patterns may break your app
**Do Instead**: Ensure all sources match your framework version

### ❌ Don't: Ignore warnings in documentation
**Why**: Edge cases and gotchas matter
**Do Instead**: Read "Notes", "Warnings", and "Security" sections carefully

### ❌ Don't: Stop at the first solution
**Why**: First solution may not be best for your case
**Do Instead**: Research at least 3 alternatives, compare trade-offs

### ❌ Don't: Skip official docs
**Why**: You'll miss context, best practices, security considerations
**Do Instead**: Always start with official documentation

---

## Quality Checklist

Before presenting investigation results, verify:

- [ ] Consulted official documentation for all relevant frameworks
- [ ] Found at least 5 credible sources per solution
- [ ] Verified sources are recent (within 2 years) or still applicable
- [ ] Cross-referenced solutions across multiple tiers
- [ ] Ranked solutions by effectiveness (most effective first)
- [ ] Included evidence URLs for all claims
- [ ] Explained why each solution works (not just what to do)
- [ ] Documented trade-offs and risks
- [ ] Verified compatibility with OBCMS tech stack
- [ ] Checked CSP compliance (for frontend solutions)
- [ ] Considered multi-tenant implications (for data solutions)
- [ ] Included validation/testing steps
