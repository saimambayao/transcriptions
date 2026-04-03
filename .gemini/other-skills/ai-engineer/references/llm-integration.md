## Workflow 2: LLM Integration

**For integrating Gemini API or GPT-4 into Django Ninja + Next.js applications.**

### Step 1: API Setup & Configuration

**Install dependencies (Backend):**
```bash
pip install anthropic openai langchain langchain-anthropic
```

**Configure settings:**
```python

---

# Step 2: Prompt Engineering (from SKILL.md)

### Step 2: Prompt Engineering

**Claude-Optimized Prompt Template:**

```python
from string import Template

CLAUDE_PROMPT_TEMPLATE = Template("""You are an AI assistant for the CSEA (Cooperative and Social Enterprise Authority) Digital Platform.

<context>
$context
</context>

<instructions>
$instructions
</instructions>

<constraints>
- Provide factual, evidence-based responses
- If uncertain, state limitations clearly
- Respect organization data isolation
- Follow Philippines government communication standards
</constraints>

<task>
$task
</task>

$format_instructions""")

def create_prompt(context, instructions, task, format_instructions=""):
    return CLAUDE_PROMPT_TEMPLATE.substitute(
        context=context,
        instructions=instructions,
        task=task,
        format_instructions=format_instructions
    )
```

**Example usage:**
```python
prompt = create_prompt(
    context=f"Cooperative: {coop.name}, Members: {coop.member_count}",
    instructions="Analyze the cooperative's compliance status based on FRAMES indicators",
    task="Identify top 3 compliance gaps for this cooperative",
    format_instructions="<output_format>Return JSON with: {gaps: [{area, description, severity}]}</output_format>"
)
```

**Best practices:**
- Use XML tags for structure (Claude understands XML well)
- Place context first, then instructions, then task
- Be explicit about output format
- Include constraints for safety

**See:** [references/prompt-engineering.md](references/prompt-engineering.md)

---


---

### Step 3: API Integration Patterns

**Pattern 1: Django Ninja API Endpoint**
```python
from ninja import Router, Schema
from ninja.security import HttpBearer
import anthropic

router = Router()

class PromptSchema(Schema):
    prompt: str
    max_tokens: int = 1024

class ResponseSchema(Schema):
    response: str
    tokens_used: int

@router.post('/generate', response=ResponseSchema)
def generate_text(request, payload: PromptSchema):
    """Generate text using Gemini API."""
    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    try:
        message = client.messages.create(
            model=settings.DEFAULT_LLM_MODEL,
            max_tokens=payload.max_tokens,
            messages=[{"role": "user", "content": payload.prompt}]
        )
        return {
            "response": message.content[0].text,
            "tokens_used": message.usage.input_tokens + message.usage.output_tokens
        }
    except anthropic.RateLimitError:
        raise HttpError(429, "Rate limit exceeded. Please try again later.")
    except anthropic.APIError as e:
        logger.error(f"Gemini API error: {e}")
        raise HttpError(500, "AI service temporarily unavailable.")
```

**Pattern 2: React Hook with TanStack Query**
```typescript
// lib/hooks/useAI.ts
import { useMutation, useQuery } from '@tanstack/react-query';

interface GenerateRequest {
  prompt: string;
  maxTokens?: number;
}

interface GenerateResponse {
  response: string;
  tokens_used: number;
}

export function useGenerateText() {
  return useMutation<GenerateResponse, Error, GenerateRequest>({
    mutationFn: async ({ prompt, maxTokens = 1024 }) => {
      const res = await fetch('/api/ai/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, max_tokens: maxTokens }),
      });
      if (!res.ok) throw new Error('Generation failed');
      return res.json();
    },
  });
}
```

**Pattern 3: Structured Output (Tool Calling)**
```python
def extract_compliance_issues(report_text):
    """Extract structured compliance issues using tool calling."""
    tools = [{
        "name": "record_compliance_issue",
        "description": "Record a compliance issue identified from report",
        "input_schema": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "enum": ["registration", "reporting", "governance", "financial", "social_audit"]
                },
                "description": {"type": "string"},
                "severity": {
                    "type": "string",
                    "enum": ["low", "medium", "high", "critical"]
                },
                "recommendation": {"type": "string"}
            },
            "required": ["category", "description", "severity"]
        }
    }]

    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        tools=tools,
        messages=[{
            "role": "user",
            "content": f"Extract compliance issues from this report:\n\n{report_text}"
        }]
    )

    # Parse tool calls to structured data
    issues = []
    for content in response.content:
        if content.type == "tool_use":
            issues.append(content.input)

    return issues
```

**Output:** Working LLM integration with error handling, caching, logging

**See:** [references/llm-integration.md](references/llm-integration.md)

---
