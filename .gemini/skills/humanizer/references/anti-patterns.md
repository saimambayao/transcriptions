# AI Anti-Pattern Library

Comprehensive list of AI slop patterns with frequency data. Organized by detection risk tier.

## Tier 1: Extreme Risk (100x+ AI frequency)

### Phrases to Kill on Sight

| Phrase | AI/Human Ratio | Action |
|--------|---------------|--------|
| "provide/gain valuable insights" | 902x | Delete sentence, rewrite |
| "casting long shadows" | 561x | Delete |
| "left an indelible mark" | 319x | Delete |
| "a rich tapestry" | 227x | Delete |
| "plays a crucial role in shaping" | 182x | Say what it does specifically |
| "in today's fast-paced world" | 107x | Delete, start with the point |
| "it's worth noting that" | 100x+ | Delete |
| "it's important to remember" | 100x+ | Delete |
| "navigate the complexities" | 100x+ | Delete or be specific |
| "at the heart of" | 100x+ | Delete |
| "paving the way for" | 100x+ | Say what enables what |
| "a testament to" | 100x+ | Delete |
| "the ever-evolving" | 100x+ | Delete the adjective |

### Self-Reference (294,000x ratio)
- "As an AI language model..."
- "I do not have personal..."
- "As an AI, I..."
- "I'm happy to help..."
- "Great question!"

### "By..." Sentence Starters

| Problematic | Rewrite |
|-------------|---------|
| "By implementing this policy..." | "This policy achieves..." |
| "By incorporating these changes..." | "These changes..." |
| "By leveraging technology..." | "Technology enables..." |
| "By fostering collaboration..." | "Collaboration between X and Y..." |

## Tier 2: High Risk (10-100x frequency)

### Dangling -ing Clauses

These participial phrases at the end of sentences are a strong AI signal:

| Pattern | Fix |
|---------|-----|
| "The budget increased, **reflecting** growth." | "The budget increase reflects growth." |
| "Revenue declined, **indicating** weak demand." | "Revenue declined. This indicates weak demand." |
| "The policy succeeded, **resulting** in..." | "The policy succeeded and produced..." |
| "Scores improved, **demonstrating** effectiveness." | "Scores improved. The program works." |

Full list of -ing words to watch: reflecting, indicating, suggesting, resulting, emphasizing, underscoring, demonstrating, highlighting, signifying, illustrating, showcasing, revealing, enabling, fostering, ensuring, promoting.

### High-Detection Words

| Word | AI/Human Ratio | Use Instead |
|------|---------------|-------------|
| delves | 25.2x | examines, explores, looks at |
| showcasing | 9.2x | showing, displaying |
| underscores | 9.1x | emphasizes, shows, highlights |
| landscape | 8x+ | field, area, sector |
| multifaceted | 7x+ | complex, varied, layered |
| tapestry | 6x+ | mix, combination |
| pivotal | 5x+ | important, key, central |
| nuanced | 5x+ | subtle, detailed |
| holistic | 4x+ | comprehensive, complete, whole |
| synergy | 4x+ | cooperation, combined effect |
| paradigm | 4x+ | model, approach, framework |
| leverage | 3x+ | use, apply, take advantage of |
| robust | 3x+ | strong, solid, reliable |
| streamline | 3x+ | simplify, speed up |
| cutting-edge | 3x+ | latest, modern, advanced |
| groundbreaking | 3x+ | new, innovative, first |
| game-changer | 3x+ | significant change, breakthrough |
| ecosystem | 3x+ | system, network, environment |

## Tier 3: Moderate Risk (Formal Connectors)

### Overused Formal Words

| Overused | Plain Alternatives |
|----------|-------------------|
| represents | is, serves as, shows |
| constitutes | is, makes up, forms |
| comprises | includes, contains, has |
| encompasses | includes, covers, spans |
| facilitates | helps, enables, supports |
| leverages | uses, applies, employs |
| utilizes | uses |
| implements | runs, carries out, does |
| demonstrates | shows, proves |
| illustrates | shows, makes clear |
| necessitates | requires, needs |
| endeavors | tries, works to |
| aforementioned | (just name the thing again) |
| subsequently | then, after, next |
| henceforth | from now on |
| pursuant to | under, following |

## Tier 4: Structural Patterns

### Formulaic Transitions

Max 1 per 3-4 paragraphs. Use topic sentences instead.

| Overused Transition | Better Approach |
|--------------------|-----------------|
| Moreover, | Start with the new idea directly |
| Furthermore, | Start with the new idea directly |
| Additionally, | Start with the new idea directly |
| Consequently, | "So..." or just state the result |
| Subsequently, | "Then..." or "After that..." |
| Hence, | "So..." or drop it |
| Thus, | "So..." or drop it |
| Therefore, | "So..." or state the conclusion |
| In conclusion, | Just conclude |
| To summarize, | Just summarize |
| In summary, | Just summarize |

### Three-Beat Cadences

AI loves triplets: "Fast, efficient, and reliable." Humans vary.

- Drop to 2: "Fast and reliable"
- Expand to 4+: "Fast, reliable, cheap, and built in a weekend"
- Use a different structure: "It's fast. More importantly, it's reliable."

### Em-Dash Patterns

AI uses em-dashes at 3x human rate. Replace most with:
- Commas (for parenthetical asides)
- Parentheses (for supplementary info)
- Periods (break into two sentences)
- Colons (when introducing a list or explanation)

### Uniform Length Patterns

| Symptom | Fix |
|---------|-----|
| All sentences 15-20 words | Mix: 5-word punch, then 25-word explanation |
| All paragraphs 3-4 sentences | Mix: 1-sentence paragraph, then 5-sentence |
| All bullet points same length | Mix: some 5 words, some 25 |

## Structured Content Anti-Patterns

These are specific to bullet points, lists, and organized notes — the most common AI output format.

### Bullet Format Monotony

| AI Pattern | Human Pattern |
|------------|---------------|
| Every bullet: "**Bold** — explanation here" | Mix: some bold, some plain, some questions |
| All bullets start with verbs | Start some with nouns, numbers, or "Not..." |
| All bullets are complete sentences | Mix complete sentences with fragments |
| Perfect parallelism across all items | Break parallelism deliberately on some |
| Exactly 3-5 items per list | 2 items sometimes. 7 sometimes. |

### Header Patterns

| AI Pattern | Human Pattern |
|------------|---------------|
| "Key Takeaways" | Just start listing them |
| "Overview" | Use a specific descriptive title |
| "Conclusion" | Make a statement instead |
| All H2s are nouns | Mix: questions, verb phrases, statements |
| Every section has a header | Sometimes content flows without one |

### Summary Patterns

| AI Pattern | Human Pattern |
|------------|---------------|
| "In this section, we explored..." | (Don't summarize — just move on) |
| "Let's dive into..." | (Just start the topic) |
| "Here's what you need to know:" | (Just tell them) |
| "This is important because..." | (Make the importance obvious from context) |
| "Without further ado..." | (Delete. Start.) |

## Quick Self-Test

Read your output and count:
1. How many sentences start with the same word? (>2 in a row = fix)
2. How many -ing dependent clauses? (>1 per paragraph = fix)
3. How many em-dashes? (>1 per 3 paragraphs = fix)
4. How many "Moreover/Furthermore/Additionally"? (>1 per page = fix)
5. Are all bullets the same length? (yes = fix)
6. Does it sound like you'd actually say this out loud? (no = fix)
