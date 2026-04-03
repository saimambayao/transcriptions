## Workflow 4: RAG Implementation

**For building Retrieval-Augmented Generation systems.**

### RAG Architecture for CSEA

```
User Query → Query Processing → Vector Search → Context Retrieval → LLM Generation → Response
                                      ↓
                                Vector Database (pgvector)
                                      ↑
                        Document Ingestion Pipeline
                                      ↑
                        CSEA Documents (compliance reports, annual reports, policies)
```

---

### Step 1: Document Ingestion & Embedding

**Install pgvector:**
```bash