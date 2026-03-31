# AI Optimization Guide (obcAI)

obcAI token optimization, caching strategies, batch processing.

## Token Usage Optimization

### 1. Minimize Prompt Size

```python
# ❌ Verbose prompt
prompt = f"""
User Information:
- Username: {user.username}
- Email: {user.email}
- Organization: {org.name}
- Organization Type: {org.organization_type}

Query: {query}
"""

# ✅ Minimal prompt
context = {'organization_id': org.id}
response = coordinator.query(query, context=context)
```

### 2. Use System Prompts Efficiently

```python
# ❌ Repeating instructions in every query
system_prompt = "You are an expert in OBC communities. Answer concisely. Focus on data..."

# ✅ Set once, reuse
agent = create_agent(
    system_prompt="Expert in OBC communities. Concise answers.",
    model="gemini"
)
```

## Caching Strategies

### 1. Redis Cache for Common Queries

```python
import hashlib
from django.core.cache import cache

def query_obcai(query, organization):
    # Create cache key from query + org
    cache_key = f"obcai:{organization.id}:{hashlib.md5(query.encode()).hexdigest()}"
    
    # Check cache
    cached_response = cache.get(cache_key)
    if cached_response:
        return cached_response
    
    # Query coordinator
    response = coordinator.query(query, organization_id=organization.id)
    
    # Cache for 1 hour
    cache.set(cache_key, response, 3600)
    return response
```

### 2. Different TTL for Different Query Types

```python
def get_cache_ttl(query_type):
    ttls = {
        'geographic': 86400,  # 24 hours (rarely changes)
        'policy': 3600,       # 1 hour
        'community': 300,     # 5 min (changes frequently)
        'realtime': 0,        # No cache
    }
    return ttls.get(query_type, 3600)
```

### 3. Cache Warming (Pre-populate)

```python
from celery import shared_task

@shared_task
def warm_obcai_cache():
    common_queries = [
        "What is the total OBC population?",
        "List all provinces with OBC communities",
        "What are the MANA sectors?",
    ]
    for org in Organization.objects.filter(is_active=True):
        for query in common_queries:
            query_obcai(query, org)  # Populates cache
```

## Batch Processing

### 1. Batch Multiple Queries

```python
# ❌ Individual queries
for community in communities:
    analysis = coordinator.query(f"Analyze community {community.name}")

# ✅ Batch query
community_names = [c.name for c in communities]
batch_analysis = coordinator.query(f"Analyze these communities: {', '.join(community_names)}")
```

### 2. Background Processing

```python
@shared_task
def analyze_communities_async(community_ids):
    communities = Community.objects.filter(id__in=community_ids)
    for community in communities:
        analysis = coordinator.query(f"Analyze {community.name}")
        community.ai_analysis = analysis
        community.save()
```

## Model Selection

### 1. Use Appropriate Model for Task

```python
# ❌ Using expensive model for simple task
response = coordinator.query("What is 2+2?", model="gemini-pro")  # Overkill!

# ✅ Use cheaper model for simple tasks
response = coordinator.query("What is 2+2?", model="gemini-flash")
```

### 2. Fallback Strategy

```python
def query_with_fallback(query, context):
    try:
        # Try primary (Gemini)
        return coordinator.query(query, model="gemini", context=context)
    except Exception:
        # Fallback to Zhipu GLM 4.6
        return coordinator.query(query, model="zhipu-glm-4", context=context)
```

## Response Streaming (Future)

```python
def stream_obcai_response(query, organization):
    """Stream response for long outputs"""
    for chunk in coordinator.stream(query, organization_id=organization.id):
        yield chunk
```

## AI Cost Monitoring

### 1. Log Token Usage

```python
def query_obcai_with_metrics(query, organization):
    response = coordinator.query(query, organization_id=organization.id)
    
    # Log metrics
    metrics.log('obcai_query', {
        'organization': organization.id,
        'tokens_used': response.tokens_used,
        'cost': response.tokens_used * 0.00001,  # Estimate
        'cached': response.from_cache,
    })
    
    return response
```

### 2. Set Usage Limits

```python
def check_usage_limit(organization):
    monthly_tokens = get_monthly_token_usage(organization)
    if monthly_tokens > organization.ai_token_limit:
        raise Exception("AI usage limit exceeded")
```

## AI Optimization Checklist

- [ ] Implement Redis caching for common queries
- [ ] Set appropriate TTL for different query types
- [ ] Minimize prompt size
- [ ] Use batch processing where possible
- [ ] Select appropriate model (Gemini Flash for simple tasks)
- [ ] Implement fallback to Zhipu GLM 4.6
- [ ] Monitor token usage and costs
- [ ] Cache warming for common queries
- [ ] Set usage limits per organization
