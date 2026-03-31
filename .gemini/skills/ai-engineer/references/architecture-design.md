# AI Feature Architecture Design

Complete guide to architecting AI-powered features for OBCMS.

## Design Process

### Step 1: Requirements Analysis

**Questions to answer:**

1. **Problem Definition**
   - What specific problem does this AI feature solve?
   - Can it be solved without AI (traditional code)?
   - What's the minimum viable AI solution?

2. **User Experience**
   - Who will use this feature?
   - What's the expected interaction model?
   - What are acceptable latency ranges?
   - How should errors be communicated?

3. **Success Metrics**
   - How do we measure success?
   - What's the baseline to beat?
   - What's good enough for MVP?

**Example: Community Needs Q&A Chatbot**
```
Problem: Staff spend hours searching through hundreds of assessment reports
Traditional solution: Better search UI (insufficient - lacks context understanding)
AI solution: RAG-powered chatbot that understands natural language queries

User: OOBC staff, partner ministry analysts
Interaction: Chat interface with streaming responses
Latency: <3 seconds for initial response
Error handling: Graceful degradation to keyword search

Success metrics:
- 70% of queries answered correctly (vs 40% keyword search)
- <5 second average response time
- 80% user satisfaction rating
```

---

### Step 2: AI Capability Mapping

**Core AI capabilities:**

| Capability | Use Cases | Model Type | Complexity |
|------------|-----------|------------|------------|
| **Classification** | Categorize assessments, tag communities | Fine-tuned or zero-shot | Low |
| **Generation** | Draft reports, create summaries | LLM (Claude/GPT) | Medium |
| **Extraction** | Pull structured data from text | LLM with tool calling | Medium |
| **Summarization** | Condense long documents | LLM | Low |
| **Q&A** | Answer questions from knowledge base | RAG system | High |
| **Recommendation** | Suggest interventions | ML model or LLM | High |
| **Prediction** | Forecast community needs | ML model (regression) | Very High |

**Decision matrix:**

```
If task is:
  Classification → Check if categories are stable
    ├─ YES → Zero-shot LLM classification
    └─ NO → Consider fine-tuning or traditional ML

  Generation → Check if format is consistent
    ├─ YES → Prompt template + LLM
    └─ NO → AI agent with dynamic prompts

  Extraction → Check if schema is known
    ├─ YES → LLM with tool calling (structured output)
    └─ NO → Exploratory LLM with validation

  Q&A → Check if answers are in documents
    ├─ YES → RAG system (retrieve + generate)
    └─ NO → Direct LLM (may hallucinate)

  Recommendation → Check if rules are explicit
    ├─ YES → Rule-based + LLM explanation
    └─ NO → ML model or multi-agent reasoning

  Prediction → Check if historical data exists
    ├─ YES → ML model (regression/time-series)
    └─ NO → LLM-based forecasting (less reliable)
```

---

### Step 3: Data Strategy

**Data requirements:**

1. **Training data** (if fine-tuning)
   - Volume needed (usually 100+ examples minimum)
   - Quality requirements
   - Labeling strategy

2. **Inference data** (for all AI features)
   - Where does input come from?
   - How is it preprocessed?
   - What's the update frequency?

3. **Retrieval data** (for RAG)
   - Document corpus (assessments, reports, plans)
   - Chunking strategy (size, overlap)
   - Metadata enrichment

**OBCMS data sources:**

```python
# Available data for AI features
DATA_SOURCES = {
    'mana_assessments': {
        'count': '~500',
        'format': 'Structured + unstructured text',
        'update_frequency': 'Weekly',
        'quality': 'Medium (variable detail)',
    },
    'community_profiles': {
        'count': '~200',
        'format': 'Structured',
        'update_frequency': 'Monthly',
        'quality': 'High',
    },
    'strategic_plans': {
        'count': '~50',
        'format': 'Long documents (10-50 pages)',
        'update_frequency': 'Quarterly',
        'quality': 'High',
    },
    'budget_requests': {
        'count': '~300',
        'format': 'Structured + justification text',
        'update_frequency': 'Annually (budget cycle)',
        'quality': 'Medium',
    },
}
```

**Data preparation pipeline:**

```python
# Example: Preparing MANA assessments for RAG
def prepare_assessment_for_rag(assessment):
    """Prepare assessment document for RAG indexing."""
    # 1. Extract text content
    text = f"""
    Community: {assessment.community.name}
    Region: {assessment.community.region}
    Assessment Date: {assessment.date}

    Sectoral Needs:
    Health: {assessment.health_needs}
    Education: {assessment.education_needs}
    Infrastructure: {assessment.infrastructure_needs}
    Livelihood: {assessment.livelihood_needs}

    Priority Recommendations:
    {assessment.recommendations}
    """

    # 2. Add metadata
    metadata = {
        'document_type': 'mana_assessment',
        'community_id': assessment.community.id,
        'region': assessment.community.region.name,
        'date': str(assessment.date),
        'sectors': ['health', 'education', 'infrastructure', 'livelihood'],
    }

    return {'text': text, 'metadata': metadata}
```

---

### Step 4: Model Selection

**Selection criteria:**

| Factor | Claude Haiku | Claude Sonnet | Claude Opus | GPT-4o |
|--------|--------------|---------------|-------------|--------|
| **Speed** | Fastest (300ms) | Fast (1s) | Slow (3s) | Very Fast (200ms) |
| **Cost** | $0.80/1M tokens | $3/1M tokens | $15/1M tokens | $5/1M tokens |
| **Quality** | Good | Excellent | Best | Excellent |
| **Context** | 200K tokens | 200K tokens | 200K tokens | 128K tokens |
| **Use case** | Classification, simple tasks | RAG, extraction | Complex reasoning | Fast generation |

**Cost estimation:**

```python
# Estimate monthly AI costs
def estimate_monthly_cost(feature_usage):
    """
    Example:
    - 1000 Q&A queries/month
    - Average 2K input tokens (retrieved context)
    - Average 500 output tokens (answer)
    """
    queries_per_month = 1000
    avg_input_tokens = 2000
    avg_output_tokens = 500

    # Gemini Sonnet pricing (as of 2025)
    input_cost_per_1m = 3.00
    output_cost_per_1m = 15.00

    total_input_tokens = queries_per_month * avg_input_tokens
    total_output_tokens = queries_per_month * avg_output_tokens

    monthly_cost = (
        (total_input_tokens / 1_000_000) * input_cost_per_1m +
        (total_output_tokens / 1_000_000) * output_cost_per_1m
    )

    return monthly_cost

# Result: ~$13.50/month for 1000 queries
```

---

### Step 5: Integration Architecture

**Architecture patterns:**

**Pattern 1: Synchronous (Simple Features)**
```
User Request → Django View → LLM API → Response → User
   ~1-3 seconds total
   Good for: Q&A, summarization, classification
   Bad for: Long documents, batch processing
```

**Pattern 2: Asynchronous (Background Tasks)**
```
User Request → Django View → Celery Task → LLM API → DB Update → Notification
   Immediate response, processing in background
   Good for: Batch analysis, large documents
   Bad for: Interactive features
```

**Pattern 3: Streaming (Real-time UIs)**
```
User Request → Django View → LLM Streaming API → Progressive UI Update
   Tokens stream as generated
   Good for: Chatbots, long-form generation
   Bad for: Structured output needs
```

**Pattern 4: Agent (Multi-step)**
```
User Request → Agent Orchestrator → [Tool 1, Tool 2, LLM] → Final Response
   Multiple LLM calls + tool execution
   Good for: Complex workflows, research tasks
   Bad for: Simple, fast responses
```

---

### Step 6: Infrastructure Planning

**Required components:**

1. **API Key Management**
```python
# settings/production.py
ANTHROPIC_API_KEY = env('ANTHROPIC_API_KEY')  # Railway secret
OPENAI_API_KEY = env('OPENAI_API_KEY')

# Rate limiting per organization
AI_CONFIG = {
    'rate_limits': {
        'requests_per_minute': 20,
        'tokens_per_day': 100000,
    },
    'cost_alerts': {
        'daily_threshold': 10.00,  # USD
        'monthly_threshold': 200.00,
    },
}
```

2. **Caching Layer**
```python
# Cache identical prompts to reduce costs
import hashlib
from django.core.cache import cache

def cached_llm_call(prompt, model, ttl=86400):
    """Cache LLM responses for identical prompts."""
    cache_key = f"llm:{model}:{hashlib.sha256(prompt.encode()).hexdigest()}"

    cached = cache.get(cache_key)
    if cached:
        return cached

    response = call_llm(prompt, model)
    cache.set(cache_key, response, ttl)
    return response
```

3. **Cost Tracking**
```python
# Track every AI interaction
class AIUsage(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    feature = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    input_tokens = models.IntegerField()
    output_tokens = models.IntegerField()
    cost_usd = models.DecimalField(max_digits=10, decimal_places=4)
    latency_ms = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['organization', 'created_at']),
            models.Index(fields=['feature', 'created_at']),
        ]

# Usage tracking decorator
def track_ai_usage(feature_name):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            start_time = time.time()
            result = func(request, *args, **kwargs)
            latency = int((time.time() - start_time) * 1000)

            # Log usage
            AIUsage.objects.create(
                organization=request.user.organization,
                user=request.user,
                feature=feature_name,
                model=result.get('model'),
                input_tokens=result.get('input_tokens'),
                output_tokens=result.get('output_tokens'),
                cost_usd=calculate_cost(result),
                latency_ms=latency,
            )

            return result
        return wrapper
    return decorator
```

4. **Monitoring & Alerts**
```python
# Daily cost monitoring
from celery import shared_task

@shared_task
def monitor_daily_ai_costs():
    """Send alerts if daily AI costs exceed threshold."""
    today = timezone.now().date()

    for org in Organization.objects.all():
        daily_cost = AIUsage.objects.filter(
            organization=org,
            created_at__date=today
        ).aggregate(total=Sum('cost_usd'))['total'] or 0

        threshold = AI_CONFIG['cost_alerts']['daily_threshold']

        if daily_cost > threshold:
            notify_admins(
                f"AI cost alert: {org.name} spent ${daily_cost:.2f} today (threshold: ${threshold})"
            )
```

---

### Step 7: Risk Assessment

**Common risks and mitigation:**

| Risk | Impact | Likelihood | Mitigation |
|------|--------|----------|------------|
| **Hallucination** | High (wrong data) | Medium | RAG with citations, human review |
| **PII leakage** | Critical (legal) | Low | Input validation, output redaction |
| **Cost overrun** | High (budget) | Medium | Rate limiting, cost alerts, caching |
| **API downtime** | Medium (UX) | Low | Fallback models, graceful degradation |
| **Bias** | Medium (fairness) | Medium | Bias detection, diverse testing |
| **Performance** | Low (UX) | Medium | Caching, async processing, streaming |

---

## Complete Architecture Example: Community Q&A Chatbot

**Feature:** RAG-powered chatbot for OOBC community data

**Architecture:**

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interface                        │
│  HTMX form → Streaming response display → Source citations  │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│                      Django View                             │
│  - Validate input                                            │
│  - Check rate limits                                         │
│  - Log interaction                                           │
└────────────────────────┬────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
┌────────▼───────┐ ┌─────▼─────┐ ┌──────▼───────┐
│ Vector Search  │ │ LLM API   │ │ Cost Tracker │
│ (pgvector)     │ │ (Claude)  │ │ (Django)     │
└────────────────┘ └───────────┘ └──────────────┘
         │
┌────────▼───────────────────────────────────────┐
│              Document Index                     │
│  - MANA assessments (chunked)                  │
│  - Community profiles                          │
│  - Strategic plans                             │
│  - Embedding: all-MiniLM-L6-v2                 │
└────────────────────────────────────────────────┘
```

**Implementation checklist:**

- [x] Django models for document embeddings
- [x] Celery task for document indexing
- [x] pgvector setup in PostgreSQL
- [x] Vector similarity search function
- [x] RAG prompt template
- [x] Gemini API integration with streaming
- [x] HTMX chatbot UI
- [x] Cost tracking and monitoring
- [x] Rate limiting per organization
- [x] Error handling and fallbacks
- [ ] Bias detection (future)
- [ ] User feedback collection (future)

**Estimated costs:**
- Development: ~40 hours
- Monthly operating cost: $15-30 (based on 1000-2000 queries)
- Maintenance: ~4 hours/month

---

## Decision Framework

**When architecting an AI feature, ask:**

1. **Is AI necessary?**
   - Can traditional code solve this? (if yes, use traditional code)
   - Does AI provide significant value? (if no, reconsider)

2. **What's the simplest approach?**
   - Direct LLM → RAG → Agent (in order of complexity)
   - Always start simple, add complexity only if needed

3. **What are the constraints?**
   - Budget: How much can we spend monthly?
   - Latency: How fast must it be?
   - Accuracy: What error rate is acceptable?

4. **How do we validate?**
   - What does success look like?
   - How do we test before production?
   - What monitoring do we need?

**Remember:** AI features should augment human decision-making, not replace it. All AI outputs in OBCMS should be treated as suggestions requiring validation.


---

# Model Selection & Integration (from SKILL.md)

### Phase 2: Model Selection & Integration Strategy

**Model Selection Decision Tree:**

```
Question 1: Do you need latest information or domain-specific knowledge?
├─ YES → RAG system (retrieve + generate)
└─ NO → Direct LLM (prompt only)

Question 2: Do you need multiple reasoning steps or tool use?
├─ YES → AI Agent (with tools/memory)
└─ NO → Simple LLM call

Question 3: What's your budget and latency tolerance?
├─ HIGH budget, LOW latency → GPT-4o (fastest, most expensive)
├─ MEDIUM budget, MEDIUM latency → Claude Sonnet (balanced)
└─ LOW budget, HIGH latency → Claude Haiku (cheapest)

Question 4: Do you need structured output?
├─ YES → Use tool calling or JSON mode
└─ NO → Standard text generation
```

**Integration Patterns:**

**Pattern 1: Synchronous API Call** (Simple features)
```python

---

### Phase 3: Infrastructure Planning

**Infrastructure Components:**

1. **API Key Management**
   ```python
   # config/settings.py
   ANTHROPIC_API_KEY = env('ANTHROPIC_API_KEY')
   OPENAI_API_KEY = env('OPENAI_API_KEY')

   # Rate limiting per organization
   AI_RATE_LIMITS = {
       'requests_per_minute': 20,
       'tokens_per_day': 100000,
   }
   ```

2. **Caching Strategy (Django)**
   ```python
   # Cache LLM responses for identical prompts
   from django.core.cache import cache
   import hashlib

   def get_cached_llm_response(prompt, model):
       cache_key = f"llm:{model}:{hashlib.sha256(prompt.encode()).hexdigest()}"
       cached = cache.get(cache_key)
       if cached:
           return cached

       response = call_llm(prompt, model)
       cache.set(cache_key, response, timeout=86400)  # 24 hours
       return response
   ```

3. **Cost Tracking Model**
   ```python
   class AIUsage(models.Model):
       organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
       feature = models.CharField(max_length=100)
       model = models.CharField(max_length=50)
       input_tokens = models.IntegerField()
       output_tokens = models.IntegerField()
       cost = models.DecimalField(max_digits=10, decimal_places=4)
       created_at = models.DateTimeField(auto_now_add=True)
   ```

4. **Error Handling & Fallbacks**
   ```python
   def call_llm_with_fallback(prompt, primary_model="claude-sonnet", fallback_model="claude-haiku"):
       try:
           return call_claude(prompt, model=primary_model)
       except anthropic.RateLimitError:
           # Fall back to cheaper/faster model
           return call_claude(prompt, model=fallback_model)
       except anthropic.APIError as e:
           # Log and return graceful failure
           logger.error(f"LLM API error: {e}")
           return {"error": "AI service temporarily unavailable"}
   ```

**Output:** Infrastructure plan with caching, monitoring, cost tracking

**See:** [references/architecture-design.md](references/architecture-design.md)

---


---

### Phase 1: Requirements & Use Case Definition

**Activities:**
1. **Define the AI use case**
   - What problem does AI solve that traditional code cannot?
   - What's the expected user experience?
   - What are success metrics?

2. **Identify AI capability needed**
   - Classification (categorize content)
   - Generation (create content)
   - Extraction (pull structured data from unstructured)
   - Summarization (condense information)
   - Q&A (answer questions from knowledge base)
   - Recommendation (suggest items based on context)

3. **Data requirements**
   - What data is needed for training/inference?
   - Is data available and accessible?
   - What's the data quality and volume?

**CSEA-Specific Examples:**
- AI-powered compliance assessment categorization (classification)
- Business plan generator for cooperatives (generation)
- Extracting key metrics from annual reports (extraction)
- Summarizing cooperative performance reports (summarization)
- Cooperative/SE data Q&A chatbot (Q&A + RAG)
- Product recommendation based on buyer profile (recommendation)

**Output:** Clear AI feature requirements with use case, capability, data needs

**See:** [references/architecture-design.md](references/architecture-design.md)

---


---

## Quick Reference: AI Engineering Patterns

### When to Use What

| Use Case | Solution | Why |
|----------|----------|-----|
| Simple text generation | Direct LLM call | Fast, cheap, straightforward |
| Domain-specific Q&A | RAG system | Reduces hallucination, citable sources |
| Multi-step reasoning | AI Agent (LangGraph) | Handles complex workflows |
| Classification/extraction | Structured output (tool calling) | Reliable JSON output |
| Real-time chat | Streaming API | Better UX, progressive display |
| Batch processing | Background task + async LLM | Handles volume without blocking |

### Common Pitfalls to Avoid

**DON'T:**
- Send PII to external LLM APIs without encryption/consent
- Trust LLM output without validation
- Use LLMs for critical decision-making without human review
- Ignore rate limits and cost controls
- Skip bias detection and safety checks
- Deploy without monitoring and logging

**DO:**
- Implement rate limiting and cost tracking
- Cache identical prompts to reduce costs
- Use async processing for expensive operations
- Log all AI interactions for audit
- Test prompts with edge cases before production
- Monitor for bias, toxicity, and accuracy drift
- Provide user feedback mechanisms

---


---

## Workflow 1: AI Feature Architecture

**For designing AI-powered features from concept to implementation.**

### Phase 1: Requirements & Use Case Definition

See [architecture-design.md](references/architecture-design.md) for AI use case definition, capability identification, and CSEA-specific examples.

### Phase 2: Model Selection & Integration Strategy

See [architecture-design.md](references/architecture-design.md) for model selection decision tree, integration patterns (sync, streaming, async), and code examples.
