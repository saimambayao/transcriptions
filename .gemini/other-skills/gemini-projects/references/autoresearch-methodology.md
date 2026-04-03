# Autoresearch Methodology for Project Instructions

Based on Andrej Karpathy's autoresearch concept and Nick Saraev's application to Gemini CLI skills.

**Sources:**
- Karpathy: "The End of Coding" (No Priors podcast, 2026) — autoresearch for recursive self-improvement
- Saraev: "Stop Fixing Your Gemini Skills" (YouTube, 2026) — applied autoresearch to skill optimization

## Core Principle

Remove yourself as the bottleneck. Set an objective, a metric, boundaries, and let the system run autonomously. The auto loop finds improvements that humans miss because it explores the space systematically.

## Three Ingredients

Every autoresearch loop needs exactly three things:

1. **Objective metric** — a measurable number, not vibes
   - For project instructions: **eval pass rate** (percentage of binary tests passed)
   - Not Likert scales — binary yes/no only, because scoring scales compound variability

2. **Measurement tool** — automated, reliable, no human in the loop
   - An agent that runs the instructions against test prompts and evaluates outputs
   - Must be a separate evaluator (not the same agent that generated the output)

3. **Something to change** — the variable being optimized
   - The project instructions themselves

## Designing Binary Evals

Evals are like standardized tests — they benchmark whether the instructions produce correct outputs.

**Rules for good evals:**
- **Go binary** — yes/no questions only. "Is the SECTION format correct?" not "Rate the format quality 1-5"
- **Don't be too narrow** — overly specific constraints cause the model to game the eval (passes the test without genuine quality)
- **Cover the audit dimensions** — at minimum, one eval per audit dimension (Clarity, Completeness, Structure, Effectiveness, RAG-Readiness)
- **Add project-specific evals** — based on the unique requirements of that project

**Eval categories:**

| Category | Example Evals |
|----------|--------------|
| **Format compliance** | "Does the output follow the required template structure?" |
| **Citation accuracy** | "Are all legal citations verifiable and correctly formatted?" |
| **Role adherence** | "Does the output match the specified domain expert persona?" |
| **Constraint compliance** | "Does the output avoid the specified anti-patterns?" |
| **RAG behavior** | "Does the output reference uploaded files appropriately?" |
| **Completeness** | "Does the output address all required sections?" |

## The Auto Loop

```
┌─────────────────────────────────────────────────┐
│  1. Generate: Run test prompt with instructions  │
│  2. Evaluate: Score output against binary evals  │
│  3. Score: Calculate pass rate (X/N passed)       │
│  4. Mutate: Apply ONE targeted improvement        │
│  5. Re-run: Generate again with mutated version   │
│  6. Compare: Keep the winner (higher pass rate)   │
│  7. Repeat: Until no improvement or max iterations│
└─────────────────────────────────────────────────┘
```

**Key details:**
- Run each test prompt **multiple times** (3-5x) because prompts are noisy — outputs are distributions, not deterministic
- Score the **mode/median** of results, not a single run
- Apply only **one mutation per iteration** — so you can attribute improvement to the specific change
- **Keep the winner** — if the mutation doesn't improve scores, revert and try a different mutation

## Mutation Strategies

When a test fails, the mutation should address the root cause:

| Failure Pattern | Mutation Strategy |
|----------------|-------------------|
| Format wrong | Add/improve an output example in the instructions |
| Missing content | Add a specific requirement to the relevant section |
| Wrong tone/style | Adjust the role definition or add a style example |
| Hallucinated citation | Add "flag unverifiable citations" instruction |
| Ignored constraint | Explain WHY the constraint matters (not just the rule) |
| Inconsistent behavior | Add XML tags to separate the instruction from others |

## Statistical Rigor

- Prompts produce **distributions of outputs**, not fixed results
- A single test run means nothing — run 3-5x minimum
- **Pass rate** = (tests passed / total tests) across all runs
- A 5% improvement that holds across 5 runs is more valuable than a 20% improvement that only shows in 1 run
- Total cost: approximately $10 for 50 test runs (per Saraev's benchmarks)

## When NOT to Optimize

- **Subjective output** — writing style, creative tone, design aesthetics. These need human judgment, not automated evals.
- **Insufficient test cases** — fewer than 3 test prompts means the optimization will overfit
- **Instructions already scoring >90%** — diminishing returns; focus effort on other projects
- **No clear eval criteria** — if you can't define binary pass/fail, you can't optimize

## Connection to /skill-optimizer

For the parallel Gemini CLI skill, use `/skill-optimizer` directly — it has the full eval viewer, benchmarking infrastructure, and blind comparison capabilities. The OPTIMIZE mode in `/gemini-projects` is a lighter-weight version adapted for gemini.google.com Project instructions, which can't be tested programmatically (no API). Instead, it uses Gemini CLI as a simulation environment.
