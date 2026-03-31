---
date: 2026-03-23
tags: [auto-research, methodology, optimization, evals, guidelines]
source: https://github.com/karpathy/autoresearch
---

# Auto Research Guidelines

Universal methodology for autonomous optimization loops. Applies to code, prompts,
content, documents, processes — anything with a measurable outcome.

Based on Andrej Karpathy's [autoresearch](https://github.com/karpathy/autoresearch) (42K+ stars),
Nick Saraev's skill optimization application, and AI Automators' harness engineering concepts.

## What Is Auto Research?

An autonomous loop where an agent:
1. Modifies a target artifact (code, prompt, document, config)
2. Measures the result against an objective metric
3. Keeps improvements, discards regressions
4. Repeats without human involvement

Karpathy's original use case: optimizing nanoGPT training overnight. The agent found
improvements a 20-year ML researcher missed — weight decay on value embeddings and
insufficiently tuned Adam betas that interact jointly.

The methodology generalizes to anything where you can define a scalar metric and automate
evaluation. If you can't evaluate it, you can't auto research it.

## The Three Ingredients

Every auto research loop needs exactly three things. No exceptions.

### 1. Objective Metric

A number you can measure. Not vibes, not "feels better", not "looks cleaner."

| Domain | Metric | Tool |
|--------|--------|------|
| **Code performance** | Execution time (ms), memory (MB) | Benchmarks, profilers |
| **Website speed** | Lighthouse score, load time (ms) | Google Lighthouse |
| **Skill/prompt quality** | Eval pass rate (%) | Binary eval suite |
| **Document quality** | Binary checklist pass rate | Agent evaluator |
| **Email/content** | Reply rate, click rate | Analytics API |
| **Bundle size** | KB after minification | Build tool output |
| **Test coverage** | % lines/branches covered | Coverage tool |
| **API latency** | p50/p95 response time (ms) | Load testing tool |
| **Accessibility** | axe-core violation count | axe CLI |
| **SEO** | Core Web Vitals scores | Lighthouse, PageSpeed |

**Rule**: if you catch yourself saying "it should be better," stop and define what "better"
means as a number.

### 2. Measurement Tool

Automated, reliable, no human in the loop. The measurement must be:
- **Deterministic** (or averaged over multiple runs for noisy domains)
- **Fast** enough to run in each iteration (minutes, not hours)
- **Independent** from the agent making changes (separate evaluator)

For code: test suites, benchmarks, linters, Lighthouse.
For prompts/content: a separate agent evaluating outputs against binary criteria.
For processes: automated checks, API analytics, log analysis.

### 3. Something to Change

The single artifact the agent modifies each iteration.

| Domain | Artifact |
|--------|----------|
| **ML training** | `train.py` — model architecture, optimizer, hyperparameters |
| **Skills/prompts** | `SKILL.md` — the instruction text |
| **Code performance** | Source files — algorithms, queries, caching |
| **Website** | HTML/CSS/JS — layout, assets, rendering |
| **Documents** | Template/instructions — structure, constraints |
| **Config** | Config files — parameters, thresholds |

**Karpathy's design**: restrict the agent to ONE file (or a small, bounded set).
This prevents cascading changes that are hard to attribute.

## The Loop

```
┌──────────────────────────────────────────────┐
│ 1. BASELINE — measure current state          │
│ 2. HYPOTHESIZE — agent proposes ONE change   │
│ 3. APPLY — modify the artifact               │
│ 4. MEASURE — run the metric                  │
│ 5. COMPARE — better, same, or worse?         │
│    ├─ Better → KEEP, commit to main branch   │
│    ├─ Same → KEEP (reduces variance)         │
│    └─ Worse → REVERT, try different change   │
│ 6. REPEAT — until target or max iterations   │
└──────────────────────────────────────────────┘
```

### Loop Parameters

| Parameter | Default | Notes |
|-----------|---------|-------|
| **Iterations** | 5-10 | More for noisy domains, fewer for deterministic |
| **Runs per iteration** | 3-5 | For noisy outputs (prompts, content). 1 for deterministic (code benchmarks) |
| **Time budget per run** | 2-5 min | Karpathy uses fixed 5-min training budget for fair comparison |
| **Mutation size** | 1 change | Minimum viable mutation — isolate what works |
| **Target** | 95%+ | Stop early when target reached |
| **Max cost** | ~$10 | Saraev's benchmark: 50 test runs for ~$10 |

## Designing Binary Evals

This is the make-or-break step. Bad evals produce optimized garbage.

### Rules

1. **Binary only** — yes/no, pass/fail. Never use Likert scales (1-7) or scoring rubrics.
   Scoring compounds variability: a 7-point scale across 5 criteria gives 16,807 possible
   score combinations. Binary gives 32. Much easier to attribute improvement.

2. **4-6 criteria max** — more than 6 causes the agent to game the eval rather than
   genuinely improve. Like a student who memorizes the test without understanding the material.

3. **Cover different dimensions** — don't cluster all evals on format. Mix:
   - 1 structural eval (output architecture)
   - 1 content eval (substance/accuracy)
   - 1 constraint eval (specific rule adherence)
   - 1 quality eval (readability, performance)

4. **Avoid gaming traps**:
   - Too narrow: "Exactly 47 words" → agent pads/trims without quality gain
   - Too many word-level constraints → agent parrots criteria back
   - Correlated evals → two that always pass/fail together add noise, not signal

5. **Test the evals themselves** — run without the optimization first. If everything
   passes at baseline, the evals aren't testing anything useful.

### Eval Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| "Is it well-written?" | Subjective, inconsistent | "Does every paragraph have <5 sentences?" |
| "Rate quality 1-10" | Compounds variability | "Does it contain zero Tier 1 AI phrases?" |
| "Is it good?" | Meaningless | Define what "good" means as binary checks |
| "Under 500 words" | Gaming — agent truncates | Test for completeness instead |
| 10+ eval criteria | Overfitting to test | Reduce to 4-6 most discriminating |

### Good Eval Examples by Domain

**Code Performance:**
- Does the function execute in under 100ms for the test dataset?
- Does memory usage stay under 50MB?
- Do all existing tests still pass?

**Document/Content Quality:**
- Zero Tier 1 AI phrases (see [[humanizer]])
- Bullet lengths vary by at least 2x (shortest vs longest)
- 70%+ active voice sentences
- Zero formulaic transitions at sentence start

**Prompt/Skill Reliability:**
- Does the output follow the required template structure?
- Does the output contain the required sections?
- Are specific numbers used instead of vague quantifiers?

**Website Performance:**
- Lighthouse Performance score above 90?
- First Contentful Paint under 1.5s?
- No layout shift (CLS < 0.1)?

## Where to Apply Auto Research

### Perfect Fit (objective, automatable)

These domains have clear metrics and automated measurement tools:

| Domain | Metric | Artifact | Measurement |
|--------|--------|----------|-------------|
| Code performance | Speed, memory | Source code | Benchmarks |
| Skill/prompt quality | Eval pass rate | SKILL.md / prompt | Agent evaluator |
| Website speed | Lighthouse score | HTML/CSS/JS | Lighthouse CLI |
| Bundle optimization | Size (KB) | Build config | Build output |
| API performance | Latency (ms) | Endpoint code | Load tester |
| Test coverage | % covered | Test files | Coverage tool |
| Accessibility | Violation count | UI code | axe-core |
| CUDA kernels | FLOPS, throughput | Kernel code | Profiler |
| SEO | Core Web Vitals | Page content | PageSpeed API |

### Good Fit (measurable with proxy metrics)

| Domain | Proxy Metric | Notes |
|--------|-------------|-------|
| Email copy | Binary eval checklist | Reply rate too slow for loop; use quality proxies |
| Job postings | Binary readability evals | Actual applications too slow; optimize structure |
| Document templates | Checklist compliance | Human review confirms final quality |
| Policy documents | Citation accuracy + format | Content correctness needs human spot-check |
| Training materials | Structure + completeness evals | Pedagogical effectiveness needs real learners |

### Poor Fit (subjective, can't automate eval)

| Domain | Why | Alternative |
|--------|-----|-------------|
| Creative writing | Quality is subjective | Human review with /humanizer |
| Design aesthetics | "Looks good" isn't binary | Stitch exploration + human feedback |
| Strategic decisions | No single metric | /grill-me for stress-testing |
| Humor/tone | Can't evaluate computationally | Human iteration |
| Complex legal analysis | Correctness requires expertise | Expert review |

**Karpathy's caveat**: "If you can't evaluate, you can't auto research it."

## Program.md: The Meta Layer

In Karpathy's framework, `program.md` is the instruction file that tells the agent
HOW to run the auto research loop. It carries three registers:

1. **Instructions** — what to search for, what changes to try
2. **Constraints** — what must not change (tests must pass, API compatibility)
3. **Stopping criteria** — when to wrap up and report

The deeper insight: **program.md itself can be optimized**. Different program.mds
produce different rates of improvement. Karpathy envisions contests where people
write competing program.mds, then feed the results to the model to write a better one.

This is **meta-optimization** — using auto research to improve auto research.

### Implications for Gemini CLI

In our context:
- `SKILL.md` = the artifact being optimized (like `train.py`)
- `/skill-optimizer` = the program.md (instructions for HOW to optimize)
- Binary evals = the metric
- The skill-optimizer skill itself could be auto-researched

For non-skill work:
- The code file = artifact
- A `research-plan.md` = program.md equivalent
- Test suite / benchmark = metric
- Gemini CLI session = the loop executor

## The March of Nines

From the AI Automators transcript — why auto research alone isn't enough for
production-scale reliability:

| Reliability per step | 10-step workflow | Failures/day (10 runs) |
|---------------------|------------------|----------------------|
| 90% | 34.9% success | 6.5 failures |
| 99% | 90.4% success | ~1 failure |
| 99.9% | 99.0% success | ~0.1 failures |

**Lesson**: Auto research on prompts/skills gets you from ~70% to ~95%. Getting from
95% to 99.9% requires **harness engineering** — wrapping the AI in deterministic code
that gates and validates each step.

### When to Graduate from Auto Research to Harness

- Auto research reached 95%+ but failures still happen
- The workflow runs >10x/day at scale
- Failures have real consequences (money, legal, trust)
- You need different models for different sub-tasks (cost control)
- Context window overflow is a problem (long-running tasks)

Auto research and harnesses are complementary:
- **Auto research** optimizes the INSTRUCTIONS within each step
- **Harnesses** guarantee the PROCESS between steps

## Applying Auto Research in Gemini CLI

### For Coding Tasks

```
1. Write the initial code
2. Define benchmarks (speed, memory, test pass rate)
3. Let an agent loop:
   - Modify ONE aspect (algorithm, data structure, query)
   - Run benchmarks
   - Keep if improved, revert if not
4. Review the final version + changelog
```

**Example**: Optimizing a database query
- Metric: query execution time (ms)
- Artifact: the SQL query or ORM queryset
- Measurement: `EXPLAIN ANALYZE` or Django Debug Toolbar
- Constraint: same result set, all tests pass

### For Non-Coding Tasks

```
1. Write the initial document/template/instructions
2. Define 4-6 binary eval criteria
3. Generate 3-5 sample outputs
4. Evaluate each against criteria
5. Mutate the template to address failures
6. Regenerate and re-evaluate
7. Keep the winning version
```

**Example**: Optimizing a legislative briefer template
- Metric: eval pass rate across 6 criteria
- Artifact: the briefer skill instructions
- Evals: "Contains all 13 CSW sections?", "Shari'ah analysis present?",
  "Proposed amendments include specific section references?"
- Measurement: agent evaluator reviewing generated outputs

### For Process Optimization

```
1. Document the current process (as a skill or workflow)
2. Define success metrics (time, cost, quality score)
3. Let the agent suggest process changes
4. Simulate the changed process
5. Measure against metrics
6. Keep improvements
```

**Example**: Optimizing the /youtube-transcriber workflow
- Metric: organized notes quality (eval pass rate)
- Artifact: the organized notes generation instructions in SKILL.md
- Evals: "Bold keywords present?", "No timestamps in notes?",
  "Quotable quotes inline, not at bottom?"

## Existing Tools in Our Stack

| Tool | What It Optimizes | Auto Research? |
|------|-------------------|----------------|
| `/skill-optimizer` | Gemini CLI skills | Yes — full loop |
| `/skill-creator` | Skill descriptions (triggering) | Partial — description optimization loop |
| `/gemini-projects` | Gemini project instructions | Yes — lighter-weight loop |
| `/humanizer` | AI output quality | No — applied per-output, not looped |
| `/build` | Code builds | No — validates, doesn't optimize |
| `/tdd` | Code correctness | Partial — red-green-refactor is a loop |

### `/auto-research` Skill (Gemini CLI)

Universal optimization loop for any artifact. Invoke with `/auto-research` or trigger
by saying "auto research", "optimize this", "run the loop", "karpathy loop".

```
Input:  artifact path + metric definition + eval criteria + constraints
Output: optimized artifact + changelog + optimization report
```

Use `/auto-research` for: code performance, document quality, website speed, config
tuning, template optimization — anything with a measurable outcome.
Use `/skill-optimizer` for: skill-specific optimization (wraps the same methodology
with skill-aware eval infrastructure).

### `autoresearch-mlx` (Local ML Training)

Karpathy's original auto research applied to LLM training, running natively on Apple
Silicon via MLX (no PyTorch). Located at `~/apps/autoresearch-mlx`.

```bash
cd ~/apps/autoresearch-mlx
uv run train.py              # Single 5-minute training run
uv run train.py --budget 300  # 5-minute budget (default)
```

**What it does**: Trains a small GPT model on FineWeb-Edu data, measures validation
loss (val_bpb), then autonomously modifies `train.py` to find better hyperparameters,
architectures, and optimizer settings. Each experiment runs for a fixed time budget
so results are directly comparable.

**When to use**:
- Learning how auto research works at the ML level
- Experimenting with model training on Apple Silicon
- Understanding recursive self-improvement concepts

**When NOT to use**:
- For daily Gemini CLI work — use `/auto-research` skill instead
- When disk space is tight — training generates checkpoints

### How They Work Together

| Tool | Domain | Runs Where | Cost |
|------|--------|-----------|------|
| `/auto-research` | Any artifact (code, docs, prompts) | Gemini CLI agents | Token cost |
| `/skill-optimizer` | Gemini CLI skills specifically | Gemini CLI agents | Token cost |
| `autoresearch-mlx` | ML model training | Local M4 GPU | Electricity only |

The `/auto-research` skill applies Karpathy's methodology to your daily work.
The `autoresearch-mlx` repo lets you experience the original ML loop locally.
Both use the same core principle: objective metric + autonomous loop + keep winners.

## Pre-Flight Checklist

Before starting any auto research loop:

```
[ ] Metric defined as a single number (not vibes)
[ ] Measurement automated (no human in the loop)
[ ] Artifact scoped to 1 file or bounded set
[ ] 4-6 binary eval criteria written
[ ] Baseline measurement taken
[ ] Constraints defined (what must NOT change)
[ ] Max iterations / cost budget set
[ ] Backup of original artifact saved
```

## The Research Log

Every auto research run produces a log of attempted changes and their results.
This log is independently valuable:

- **Debugging**: understand what was tried and why it failed
- **Knowledge transfer**: hand the log to a smarter future model to continue
- **Pattern recognition**: recurring failure types reveal structural issues
- **Replication**: apply winning mutations to similar artifacts

Save research logs to `~/Vault/research/` with the format:
`yymmdd-autoresearch-{domain}-{artifact}.md`

## References

- [Karpathy's autoresearch repo](https://github.com/karpathy/autoresearch) — original implementation for nanoGPT training
- [Nick Saraev: Stop Fixing Your Gemini Skills](https://youtube.com/watch?v=qKU-e0x2EmE) — applied to Gemini CLI skills
- [Karpathy: The End of Coding](https://youtube.com/watch?v=kwSVtQ7dziU) — philosophy, recursive self-improvement, program.md
- [AI Automators: Agent Skills Will Fail](https://youtube.com/watch?v=I2K81s0OQto) — march of nines, harness engineering
- [pi-autoresearch](https://github.com/nicksaraev/pi-autoresearch) — extends autoresearch to speed, bundle size, Lighthouse
- [Shopify's 53% rendering improvement](https://fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/) — Tobi Lutke applied autoresearch to Shopify's templating engine
- [[skill-optimizer]] — our implementation for Gemini CLI skills
- [[humanizer]] — binary eval criteria for AI output quality
