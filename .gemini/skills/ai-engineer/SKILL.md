---
name: ai-engineer
description: AI engineering skill for designing, implementing, and optimizing AI-powered features in Bangsamoro Development Platform. Covers LLM integration (Gemini API), prompt engineering, RAG systems, semantic search, AI agents, bias detection, and responsible AI practices. Use when building AI features, implementing chatbots, creating intelligent automation, or adding ML capabilities to Next.js + Django Ninja applications. Integrates with /backend for API endpoints and /security for data protection.
argument-hint: "[topic]"
---

# AI Engineer Skill

╔═══════════════════════════════════════════════════════════════════════════════╗
║  GATE: INVOKE /prompter IMMEDIATELY                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  DO NOT read further. DO NOT proceed with any workflow.                       ║
║                                                                               ║
║  ACTION REQUIRED NOW:                                                         ║
║  1. INVOKE /prompter with the user's AI engineering request                   ║
║  2. WAIT for /prompter to complete its 5-phase workflow                       ║
║  3. WAIT for user confirmation ("Yes, proceed")                               ║
║  4. ONLY THEN return here and continue below                                  ║
║                                                                               ║
║  If user says "No" or "Adjust" → repeat /prompter                             ║
║  If user says "Let me rephrase" → restart with new input                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

---

Comprehensive AI engineering workflow for Next.js + Django Ninja applications, covering the full lifecycle of AI feature development from design to production deployment.

## Tech Stack Coverage

This skill applies to AI engineering with:

**AI/ML:** Gemini API (Anthropic), OpenAI GPT-4, LangChain, LangGraph, RAG systems, Vector databases

**Backend:** Django 6.0, Django Ninja APIs, PostgreSQL 18 (pgvector), Python 3.14

**Frontend:** Next.js 16+, React 19+, TanStack Query, Tailwind CSS (for AI-powered UIs)

**Infrastructure:** Railway deployment, API rate limiting, caching, monitoring

**Compliance:** Responsible AI, bias detection, safety guardrails

## When to Use This Skill

Invoke this skill when:
- Designing AI-powered features or intelligent automation
- Integrating LLMs (Claude, GPT-4, Gemini) into Django Ninja + Next.js applications
- Implementing chatbots, assistants, or conversational interfaces
- Building RAG (Retrieval-Augmented Generation) systems
- Creating semantic search with embeddings and vector databases
- Implementing AI agents or multi-agent workflows
- Optimizing prompt engineering for production
- Ensuring AI safety, bias detection, and compliance
- Troubleshooting AI system performance or accuracy issues
- Planning AI feature architecture and infrastructure

## AI Engineering Workflows

The ai-engineer skill provides **6 specialized workflows** for different AI engineering tasks:

### Workflow Selection Guide

| Task | Workflow | Reference |
|------|----------|-----------|
| New AI feature design | AI Feature Architecture | [architecture-design.md](references/architecture-design.md) |
| LLM integration (Claude/GPT) | LLM Integration | [llm-integration.md](references/llm-integration.md) |
| Prompt creation & optimization | Prompt Engineering | [prompt-engineering.md](references/prompt-engineering.md) |
| RAG system implementation | RAG Implementation | [rag-implementation.md](references/rag-implementation.md) |
| AI agent development | Agent Orchestration | [agent-orchestration.md](references/agent-orchestration.md) |
| Safety & compliance | Responsible AI | [responsible-ai.md](references/responsible-ai.md) |

---

## Workflow 1: AI Feature Architecture

See [architecture-design.md](references/architecture-design.md) for use case definition, model selection decision tree, integration patterns (sync, streaming, async), and infrastructure planning.

# Django Ninja API with direct LLM call
import anthropic
from ninja import Router

router = Router()

@router.post('/summarize/{report_id}')
def generate_summary(request, report_id: int):
    report = Report.objects.get(id=report_id)

    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"Summarize this compliance report:\n\n{report.content}"
        }]
    )

    summary = message.content[0].text
    report.ai_summary = summary
    report.save()

    return {"summary": summary}
```

**Pattern 2: React Component with TanStack Query** (Frontend)
```typescript
// React hook for AI summarization
import { useMutation } from '@tanstack/react-query';

export function useSummarize() {
  return useMutation({
    mutationFn: async (reportId: string) => {
      const response = await fetch(`/api/summarize/${reportId}`, {
        method: 'POST',
      });
      return response.json();
    },
  });
}

// React component
function SummaryButton({ reportId }: { reportId: string }) {
  const { mutate, isPending, data } = useSummarize();

  return (
    <div>
      <button
        onClick={() => mutate(reportId)}
        disabled={isPending}
        className="px-4 py-2 bg-negosyo-blue text-white rounded"
      >
        {isPending ? 'Generating...' : 'Generate Summary'}
      </button>
      {data && <p className="mt-4">{data.summary}</p>}
    </div>
  );
}
```

**Pattern 3: Streaming Response** (Real-time UIs)
```python
# Django Ninja streaming endpoint
from django.http import StreamingHttpResponse

@router.post('/stream-response')
def stream_ai_response(request, payload: PromptSchema):
    def generate():
        with anthropic.Anthropic().messages.stream(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": payload.prompt}]
        ) as stream:
            for text in stream.text_stream:
                yield f"data: {text}\n\n"

    return StreamingHttpResponse(generate(), content_type="text/event-stream")
```

```typescript
// React component for streaming
function StreamingChat() {
  const [response, setResponse] = useState('');

  const handleSubmit = async (prompt: string) => {
    const eventSource = new EventSource(`/api/stream-response?prompt=${prompt}`);

    eventSource.onmessage = (event) => {
      setResponse(prev => prev + event.data);
    };
  };

  return <div>{response}</div>;
}
```

**Output:** Selected model, integration pattern, implementation plan

---

### Phase 3: Infrastructure Planning

See [architecture-design.md](references/architecture-design.md) for API key management, caching, cost tracking, and error handling patterns.

## Workflow 2: LLM Integration

See [llm-integration.md](references/llm-integration.md) for API setup, prompt engineering patterns, Django Ninja endpoints, React hooks, and structured output with tool calling.

# config/settings.py
ANTHROPIC_API_KEY = env('ANTHROPIC_API_KEY')
OPENAI_API_KEY = env('OPENAI_API_KEY')

# Model selection
DEFAULT_LLM_MODEL = "claude-sonnet-4-20250514"
FAST_LLM_MODEL = "claude-haiku-4-20250514"
SMART_LLM_MODEL = "claude-opus-4-20250514"

# Token limits
MAX_INPUT_TOKENS = 100000
MAX_OUTPUT_TOKENS = 4096
```

---

### Step 2: Prompt Engineering

See [llm-integration.md](references/llm-integration.md) for Gemini-optimized prompt templates and XML tag patterns.

### Step 3: API Integration Patterns

See [llm-integration.md](references/llm-integration.md) for Django Ninja endpoints, React hooks, and structured output with tool calling.

## Workflow 4: RAG Implementation

See [rag-implementation.md](references/rag-implementation.md) for RAG architecture, document ingestion, embedding, semantic search, RAG generation, and React interface patterns.

# Add to requirements.txt
pgvector==0.2.5
sentence-transformers==2.5.1
```

**Configure PostgreSQL:**
```sql
-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;
```

**Django model for embeddings:**
```python
from pgvector.django import VectorField

class DocumentEmbedding(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=50)  # 'compliance', 'report', 'policy'
    document_id = models.IntegerField()
    chunk_index = models.IntegerField()
    chunk_text = models.TextField()
    embedding = VectorField(dimensions=768)  # sentence-transformers dimension
    metadata = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['organization', 'document_type']),
        ]
```

**Embedding generation:**
```python
from sentence_transformers import SentenceTransformer

class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def chunk_document(self, text, chunk_size=500, overlap=50):
        """Split document into overlapping chunks."""
        words = text.split()
        chunks = []
        for i in range(0, len(words), chunk_size - overlap):
            chunk = ' '.join(words[i:i + chunk_size])
            chunks.append(chunk)
        return chunks

    def embed_chunks(self, chunks):
        """Generate embeddings for text chunks."""
        return self.model.encode(chunks)

    def index_document(self, document, document_type, organization):
        """Index document for RAG retrieval."""
        chunks = self.chunk_document(document.content)
        embeddings = self.embed_chunks(chunks)

        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            DocumentEmbedding.objects.create(
                organization=organization,
                document_type=document_type,
                document_id=document.id,
                chunk_index=i,
                chunk_text=chunk,
                embedding=embedding.tolist(),
                metadata={
                    'document_title': document.title,
                    'created_at': str(document.created_at),
                }
            )
```

---

### Step 2: Semantic Search & Retrieval

**Vector similarity search:**
```python
def semantic_search(query, organization, document_type=None, limit=5):
    """Search for relevant document chunks using cosine similarity."""
    embedding_service = EmbeddingService()
    query_embedding = embedding_service.model.encode([query])[0]

    queryset = DocumentEmbedding.objects.filter(organization=organization)
    if document_type:
        queryset = queryset.filter(document_type=document_type)

    # Vector similarity search using pgvector
    results = queryset.order_by(
        DocumentEmbedding.embedding.cosine_distance(query_embedding.tolist())
    )[:limit]

    return [
        {
            'text': r.chunk_text,
            'metadata': r.metadata,
            'similarity': 1 - r.embedding.cosine_distance(query_embedding)
        }
        for r in results
    ]
```

---

### Step 3: RAG Generation

**RAG prompt template:**
```python
RAG_PROMPT_TEMPLATE = """You are an AI assistant for CSEA with access to organizational knowledge.

<retrieved_context>
{context}
</retrieved_context>

<user_query>
{query}
</user_query>

<instructions>
Answer the user's query based on the retrieved context above.
- If the context contains relevant information, use it to answer
- Cite sources by mentioning document titles
- If context is insufficient, state what information is missing
- Do not make up information not present in the context
</instructions>

Answer:"""
```

**RAG chain:**
```python
def rag_query(user_query, organization):
    """Execute RAG pipeline: retrieve → generate."""
    # Step 1: Retrieve relevant context
    retrieved_docs = semantic_search(user_query, organization, limit=5)

    # Step 2: Format context for prompt
    context = "\n\n".join([
        f"Document: {doc['metadata']['document_title']}\n{doc['text']}"
        for doc in retrieved_docs
    ])

    # Step 3: Generate response with Gemini
    prompt = RAG_PROMPT_TEMPLATE.format(
        context=context,
        query=user_query
    )

    response = call_claude(prompt)

    return {
        'answer': response,
        'sources': [doc['metadata']['document_title'] for doc in retrieved_docs],
        'retrieved_docs': retrieved_docs
    }
```

**React interface for RAG:**
```typescript
// components/RAGChat.tsx
'use client';

import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';

export function RAGChat() {
  const [query, setQuery] = useState('');
  const [messages, setMessages] = useState<Array<{role: string; content: string}>>([]);

  const { mutate, isPending } = useMutation({
    mutationFn: async (q: string) => {
      const res = await fetch('/api/rag/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: q }),
      });
      return res.json();
    },
    onSuccess: (data) => {
      setMessages(prev => [
        ...prev,
        { role: 'user', content: query },
        { role: 'assistant', content: data.answer },
      ]);
      setQuery('');
    },
  });

  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((msg, i) => (
          <div key={i} className={msg.role === 'user' ? 'text-right' : 'text-left'}>
            <span className={`inline-block p-3 rounded-lg ${
              msg.role === 'user' ? 'bg-negosyo-blue text-white' : 'bg-gray-100'
            }`}>
              {msg.content}
            </span>
          </div>
        ))}
      </div>
      <form onSubmit={(e) => { e.preventDefault(); mutate(query); }} className="p-4 border-t">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask about cooperative data..."
          className="w-full p-2 border rounded"
          disabled={isPending}
        />
      </form>
    </div>
  );
}
```

**Output:** Production-ready RAG system with vector search and LLM generation

**See:** [references/rag-implementation.md](references/rag-implementation.md)

---

## Workflow 6: Responsible AI

See [responsible-ai.md](references/responsible-ai.md) for safety guardrails, input validation, output moderation, and audit logging.

## Quick Reference: AI Engineering Patterns

See [architecture-design.md](references/architecture-design.md) for use case to solution mapping and common pitfalls.

## Integration with Other Skills

Use **backend** for Django Ninja APIs, **database** for pgvector, **frontend** for AI-powered UIs, **security** for PII protection, **debugger** for troubleshooting.
