# Optimization Report: humanizer

**Rounds completed:** 2 (stopped early — target reached)
**Starting score:** 14/16 (87.5%)
**Final score:** 16/16 (100%)
**Improvement:** +12.5 percentage points
**Baseline comparison:** With-skill 100% vs Without-skill 62.5% (+37.5pp delta)

## Eval Criteria Used
1. Zero Tier 1 phrases — pass rate: 100%
2. Bullet lengths vary 2x — pass rate: 100% (was 67%)
3. 70%+ active voice — pass rate: 100%
4. Zero formulaic transitions — pass rate: 100%
5. Varied bullet formats — pass rate: 100%
6. Specific numbers over vague quantifiers — pass rate: 100% (was 67%)

## Changes Applied
1. Round 2: Added "Bullet Length Variation" section with explicit 8-word/20-word targets and concrete example
2. Round 2: Expanded "Specific Over Vague" with second before/after example and [X] placeholder guidance

## Per-Eval Breakdown

| Eval | Round 1 | Round 2 | Trend |
|------|---------|---------|-------|
| E1: No Tier 1 | 100% | 100% | Stable |
| E2: Bullet 2x | 67% | 100% | Fixed |
| E3: Active 70% | 100% | 100% | Stable |
| E4: No transitions | 100% | 100% | Stable |
| E5: Varied format | 100% | 100% | Stable |
| E6: Specific | 67% | 100% | Fixed |

## Key Insight
The skill's anti-pattern detection (Tiers 1-4) was already strong — 100% pass on E1, E3, E4 from Round 1.
The weak spots were in constructive guidance: telling the model what TO DO (vary bullet lengths, use [X] placeholders)
rather than just what NOT to do. Adding concrete examples with word counts and the [X] placeholder convention
fixed both failures in one mutation.

## Remaining Recommendations
- Add full-document before/after transformation example to references/
- Consider adding the skill as a SessionStart hook to apply proactively to all output
