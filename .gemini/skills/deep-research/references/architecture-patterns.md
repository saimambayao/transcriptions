# Deep Research Architecture Patterns

## Orchestrator-Worker Architecture

All major deep research systems (Claude, Gemini, OpenAI) converge on a hub-and-spoke orchestrator-worker pattern.

```
                    ┌─────────────────┐
                    │   ORCHESTRATOR   │
                    │  (Lead Agent)    │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
        ┌─────┴─────┐ ┌─────┴─────┐ ┌─────┴─────┐
        │Researcher A│ │Researcher B│ │Researcher C│
        │ Domain 1   │ │ Domain 2   │ │ Domain 3   │
        └─────┬─────┘ └─────┬─────┘ └─────┬─────┘
              │              │              │
              └──────────────┼──────────────┘
                             │
                    ┌────────┴────────┐
                    │   SYNTHESIS &    │
                    │  CONTRADICTION   │
                    │   DETECTION      │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
        ┌─────┴─────┐ ┌─────┴─────┐ ┌─────┴─────┐
        │ Technical  │ │ Accuracy   │ │ Styling    │
        │ Reviewer   │ │ Reviewer   │ │ Reviewer   │
        └─────┬─────┘ └─────┬─────┘ └─────┬─────┘
              │              │              │
              └──────────────┼──────────────┘
                             │
                    ┌────────┴────────┐
                    │  SELF-CORRECTION │
                    │  & FINAL OUTPUT  │
                    └─────────────────┘
```

## DAG Task Decomposition

Decompose research queries into a Directed Acyclic Graph (DAG) of sub-tasks:

**Principles:**
- **Solvability**: Each sub-task can be solved independently
- **Completeness**: All needed research covered
- **Non-redundancy**: No duplicate work across researchers

**Example DAG:**
```
User Query: "How should we implement vector search for legislative documents?"
│
├── Sub-task 1: Vector database options (pgvector, Pinecone, Weaviate)
│   └── Parallelizable with 2, 3
├── Sub-task 2: Document embedding strategies for legal text
│   └── Parallelizable with 1, 3
├── Sub-task 3: Hybrid search approaches (semantic + keyword)
│   └── Parallelizable with 1, 2
├── Sub-task 4: Performance benchmarks (depends on 1)
│   └── Sequential after 1
└── Sub-task 5: Implementation architecture (depends on 1, 2, 3)
    └── Sequential after 1, 2, 3
```

## Researcher Scaling

| Topic Complexity | Sub-tasks | Researchers | Query Target | Estimated Time |
|-----------------|-----------|-------------|--------------|----------------|
| Focused (1-2 domains) | 2-3 | 1-2 | 20-40 queries | 3-5 min |
| Standard (3-4 domains) | 4-5 | 3-4 | 40-80 queries | 5-15 min |
| Comprehensive (5+ domains) | 6-7 | 5+ | 80-160 queries | 15-30 min |

## Error Handling & Graceful Degradation

### Error Classification

| Error Type | Example | Strategy | Max Retries |
|-----------|---------|----------|-------------|
| **Transient** | Network timeout, rate limit | Retry with backoff | 2-3 |
| **Source unavailable** | 404, paywall, geo-blocked | Skip + fallback source | 1 |
| **Empty results** | No search hits | Rewrite query + broaden terms | 2 |
| **Permanent** | Invalid domain, decommissioned | Log as unavailable, proceed without | 0 |

### Fallback Strategy Chain

```
Primary: WebSearch → WebFetch (full page)
    ↓ (if fails)
Fallback 1: WebSearch with rewritten query
    ↓ (if fails)
Fallback 2: WebSearch on alternative source domains
    ↓ (if fails)
Fallback 3: Note gap, flag for user, proceed with available data
```

### Graceful Recovery (Gemini Pattern)

Maintain shared state between orchestrator and workers:
- If a researcher fails mid-execution, don't restart from scratch
- Resume from last successful checkpoint
- Redistribute failed sub-tasks to other researchers
- Log all partial results before failure

## Self-Correction Cycle

After initial synthesis, run a closed-loop correction:

```
Draft Brief → Reviewer Corrections → Apply Changes → Re-verify → Final Output
                                           │
                                           ├── If improvement: keep change
                                           └── If regression: revert change
```

Only retain changes that improve accuracy. Track metrics:
- Citation accuracy (claims match sources)
- Source diversity (not over-reliant on single source)
- Completeness (all research questions answered)
- Contradiction resolution (conflicts addressed)

## Parallel vs Sequential Decision Framework

| Condition | Approach | Rationale |
|-----------|----------|-----------|
| Researchers cover independent domains | **Parallel** | No dependencies, max speed |
| One researcher's output informs another | **Sequential** | Avoid redundant/conflicting work |
| Reviewers check independent aspects | **Parallel** | Technical, accuracy, styling are independent |
| Final synthesis from all inputs | **Sequential** | Needs all reviewer corrections first |

## Context Window Utilization (Claude-Specific)

With 1M token context:
- Load all researcher outputs simultaneously for cross-referencing
- Detect contradictions by comparing claims side-by-side
- Maintain full source log for back-referencing during synthesis
- No need to summarize intermediate results — use full outputs
