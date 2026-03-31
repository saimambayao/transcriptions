---
name: auto-research
description: |
  Universal autonomous optimization loop based on Karpathy's auto research methodology.
  Accepts any artifact (code, prompt, document, config, template) plus a metric and eval
  criteria, then runs an iterative improve-measure-keep loop without human involvement.
  Use when user says "auto research", "optimize this", "run the loop", "improve this
  autonomously", "auto optimize", "karpathy loop", "iterative improvement", "run evals
  on this", "make this better automatically", or wants to systematically improve any
  artifact with measurable outcomes. Also trigger when user mentions "binary evals",
  "pass rate", "optimization loop", "autonomous improvement", or "auto loop".
  Works for code performance, website speed, document quality, prompt reliability,
  config tuning, template optimization, and any domain with an objective metric.
  For skill-specific optimization, prefer /skill-optimizer which wraps this methodology
  with skill-aware eval infrastructure.
argument-hint: "[artifact-path] [--metric 'description'] [--evals 'criteria']"
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
---

# Auto Research — Universal Optimization Loop

Autonomous iterative improvement for any artifact with a measurable outcome.
Based on [Karpathy's autoresearch](https://github.com/karpathy/autoresearch).

Core principle: remove yourself as the bottleneck. Define the metric, set boundaries,
hit go. The loop finds improvements humans miss because it explores systematically.

## Three Ingredients

Every auto research loop needs exactly three things. No exceptions.

1. **Objective metric** — a number, not vibes
2. **Measurement tool** — automated, no human in the loop
3. **Artifact to change** — the single file or bounded set being optimized

If any ingredient is missing, stop and help the user define it before proceeding.

## Process

### Phase 1: Setup

1. **Identify the artifact** — what file(s) will be modified?
2. **Define the metric** — what number determines improvement?
3. **Write 4-6 binary evals** — yes/no criteria (never scoring scales)
4. **Set constraints** — what must NOT change? (tests pass, API compat, etc.)
5. **Set parameters** — iterations (default 5), runs per iteration (default 3), target (default 95%)
6. **Backup the original** — copy artifact to `{artifact}.backup`

Present the setup to the user for confirmation before starting the loop.

### Phase 2: Baseline

Run the artifact through the measurement tool and score against all evals.
Record the baseline score. This is round 0.

```
Baseline: X/Y evals passed (Z%)
```

### Phase 3: The Loop

For each round (1 to max iterations):

```
1. HYPOTHESIZE — analyze failures, propose ONE targeted change
2. APPLY — modify the artifact (minimum viable mutation)
3. MEASURE — run the metric / evals (multiple times for noisy domains)
4. COMPARE:
   ├─ Better → KEEP, log the change
   ├─ Same → KEEP (reduces variance)
   └─ Worse → REVERT, try different approach
5. Report round results
```

**Mutation rules:**
- One change per round — isolate what works
- Never remove instructions/code that currently pass
- Add constraints close to the relevant section
- Preserve the artifact's original structure and voice
- For noisy domains (prompts, content): run 3-5x and use mode/median

### Phase 4: Report

After all rounds complete (or target reached), produce:

```markdown
## Auto Research Report: {artifact}

**Rounds completed:** N
**Starting score:** X/Y (Z%)
**Final score:** X/Y (Z%)
**Improvement:** +N percentage points

### Eval Criteria
1. {criterion} — pass rate: X%
2. {criterion} — pass rate: X%

### Changes Applied
1. Round N: {description of mutation}

### Per-Eval Breakdown
| Eval | Start | Final | Trend |
|------|-------|-------|-------|

### Remaining Failures
- {description and why they're hard to fix}

### Research Log
{all attempted changes, including reverted ones — valuable for future optimization}
```

Save report to same directory as the artifact: `{artifact-name}-autoresearch-report.md`

## Domain-Specific Guidance

### Code Performance
- **Metric**: execution time (ms), memory (MB), or benchmark score
- **Measurement**: test suite, profiler, benchmark script
- **Evals**: "All tests pass?", "Under Xms?", "Memory under Y MB?"
- **Constraint**: identical behavior / output

### Prompt / Skill Quality
- **Metric**: eval pass rate (%)
- **Measurement**: agent evaluator reviewing generated outputs
- **Evals**: binary checklist (see [auto-research-guidelines](${GEMINI_SKILL_DIR}/references/methodology.md))
- **Note**: run 3-5x per iteration — prompts are distributions, not deterministic

### Document / Content Quality
- **Metric**: checklist compliance rate
- **Measurement**: agent evaluator or /humanizer criteria
- **Evals**: "Zero AI phrases?", "Bullet lengths vary 2x?", "Active voice 70%+?"

### Website / Frontend
- **Metric**: Lighthouse score, load time (ms), CLS
- **Measurement**: `npx lighthouse` CLI or Playwright
- **Evals**: "Performance > 90?", "FCP < 1.5s?", "CLS < 0.1?"

### Config / Parameters
- **Metric**: application-specific benchmark
- **Measurement**: automated test or benchmark script
- **Evals**: "Benchmark improved?", "No regressions?", "Within resource limits?"

### ML Training (Local — autoresearch-mlx)

Run Karpathy's original auto research loop on Apple Silicon. Gemini acts as the
**program.md orchestrator** — proposing changes, explaining ML concepts, and guiding
the learning process. Only triggered when the user explicitly requests it.

- **Repo**: `~/apps/autoresearch-mlx`
- **Runner**: `cd ~/apps/autoresearch-mlx && uv run train.py`
- **Metric**: val_bpb (validation bits per byte — lower is better)
- **Artifact**: `train.py` (~630 lines — model architecture, optimizer, hyperparameters)
- **Time budget**: 5 minutes per training run (fixed, for fair comparison)
- **Hardware**: Apple M4 GPU via MLX/Metal

**How to invoke**: "auto research mlx", "run a training experiment", "train the model",
"optimize train.py", "karpathy loop on mlx"

**The loop for ML training:**

```
1. BASELINE — run train.py, record val_bpb
2. READ — Gemini reads train.py and the training output
3. EXPLAIN — Gemini explains what the current architecture/config does
   (learning opportunity — explain WHY, not just WHAT)
4. HYPOTHESIZE — Gemini proposes ONE change and explains the ML concept behind it
   Examples:
   - "Increasing weight decay on value embeddings to reduce overfitting"
   - "Adjusting Adam beta2 from 0.99 to 0.95 for faster adaptation"
   - "Adding a cosine learning rate schedule for smoother convergence"
5. APPLY — Edit train.py with the mutation
6. TRAIN — Run `uv run train.py` (5 min, read output when done)
7. COMPARE — Did val_bpb improve?
   ├─ Better → KEEP, explain WHY this worked
   ├─ Same → KEEP, explain what we learned
   └─ Worse → REVERT, explain WHY it didn't work (also valuable)
8. LOG — Record the experiment in the research log
9. REPEAT or STOP — user decides
```

**Teaching mode**: After each round, Gemini explains:
- What the change was and the ML concept behind it
- Why it improved (or didn't) — connecting theory to observation
- What this tells us about the model's learning dynamics
- What to try next and why

**Constraints**:
- Never modify `prepare.py` or the tokenizer (data is fixed)
- Keep train.py as a single file (Karpathy's design)
- Each run must complete in the 5-minute budget
- Save research log to `~/apps/autoresearch-mlx/research-log.md`

## Eval Design Rules

Good evals make or break auto research. Bad evals produce optimized garbage.

1. **Binary only** — yes/no. Never Likert scales (compound variability)
2. **4-6 max** — more causes gaming (model parrots criteria without quality)
3. **Cover different dimensions** — don't cluster all on format
4. **Test the evals first** — if everything passes at baseline, evals aren't useful
5. **Avoid gaming traps**: "exactly N words" = agent pads/trims without quality gain

See [references/methodology.md](${GEMINI_SKILL_DIR}/references/methodology.md) for
comprehensive eval examples by domain, anti-patterns, and the full methodology.

## When NOT to Auto Research

- **Subjective output** — creative writing, design aesthetics, humor
- **No clear metric** — if you can't define pass/fail, you can't loop
- **Already >95%** — diminishing returns; focus effort elsewhere
- **Fewer than 3 test cases** — optimization will overfit

Karpathy's caveat: "If you can't evaluate, you can't auto research it."

## Relationship to Other Skills

| Skill | Relationship |
|-------|-------------|
| `/skill-optimizer` | Specialized wrapper — uses auto research for skills specifically |
| `/humanizer` | Provides eval criteria for document/content quality loops |
| `/tdd` | Red-green-refactor is a manual version of the same loop |
| `/build` | Provides measurement (lint, build, test) for code loops |
