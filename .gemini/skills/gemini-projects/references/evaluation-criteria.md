# Gemini Project Instruction Evaluation Criteria

Based on Anthropic's official prompting best practices (platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) and Claude Projects documentation (support.claude.com).

## Table of Contents
1. [Scoring Rubric](#scoring-rubric)
2. [Anti-Patterns](#anti-patterns)
3. [Best Practices Checklist](#best-practices-checklist)
4. [Projects-Specific Considerations](#projects-specific-considerations)

---

## Scoring Rubric

Rate each dimension 1-5:

### Clarity (1-5)
- **1**: Vague, contradictory, or ambiguous instructions
- **2**: Some clear parts but significant gaps or confusing sections
- **3**: Generally understandable but could be more precise
- **4**: Clear and specific with minor ambiguities
- **5**: Crystal clear — a colleague with no context could follow them perfectly

Key questions: Could someone unfamiliar with the task follow these instructions? Are there words that could be interpreted multiple ways?

### Completeness (1-5)
- **1**: Missing most necessary context — role, output format, constraints
- **2**: Has a role or basic task but missing critical details
- **3**: Covers the basics but lacks edge cases, examples, or workflow details
- **4**: Comprehensive with minor gaps
- **5**: Covers role, task, format, constraints, edge cases, and examples

Key questions: Does it define what Gemini should do AND how? Are output formats specified? Are edge cases addressed?

### Structure (1-5)
- **1**: Wall of text, no organization
- **2**: Some sections but inconsistent formatting
- **3**: Organized but could use better hierarchy or XML tags
- **4**: Well-structured with clear sections and logical flow
- **5**: Uses XML tags, clear hierarchy, progressive disclosure — easy to parse

Key questions: Are instructions organized logically? Would XML tags help Claude parse them? Is there a clear hierarchy?

### Effectiveness (1-5)
- **1**: Instructions likely to produce poor or inconsistent results
- **2**: Will work sometimes but frequently miss the mark
- **3**: Produces acceptable results for common cases
- **4**: Reliably produces good results with occasional issues
- **5**: Optimized for Gemini's strengths — uses examples, context, and role framing effectively

Key questions: Does it leverage Claude's best patterns (examples, roles, context)? Does it avoid known anti-patterns?

### RAG-Readiness (1-5)
- **1**: Assumes all uploaded content is always in context (it's not with RAG)
- **2**: Vaguely references uploaded files without guidance
- **3**: Mentions files but doesn't guide Claude on how to use them
- **4**: Good file references with some retrieval guidance
- **5**: Self-contained instructions that work whether all files are in context or RAG-retrieved

Key questions: Will this work when Claude only retrieves chunks (not full files)? Are file references explicit enough for RAG?

---

## Anti-Patterns

Common mistakes found in Gemini Project instructions:

### Identity Suppression
```
BAD:  "NEVER mention that you're an AI"
WHY:  Wastes instruction tokens on something Claude rarely does unprompted.
      Can cause awkward workarounds when users ask directly.
FIX:  Remove, or soften to: "Respond as a domain expert. Don't preface
      answers with disclaimers about being an AI."
```

### Negative-Only Instructions
```
BAD:  "Don't use bullet points" / "Never start with 'Sure'" / "Don't apologize"
WHY:  Telling Claude what NOT to do is less effective than what TO do.
      Per Anthropic: "Tell Gemini what to do instead of what not to do."
FIX:  "Use flowing prose paragraphs" / "Start directly with the answer" /
      "When wrong, proceed directly to corrective action"
```

### ALL-CAPS Shouting
```
BAD:  "ALWAYS search files FIRST" / "NEVER hallucinate" / "MUST follow format"
WHY:  Claude 4.6 is more responsive to system prompts. Aggressive language
      that was needed for older models now causes overtriggering.
FIX:  Use normal language: "Search uploaded files before using general knowledge"
```

### Redundant Instructions
```
BAD:  Repeating the same constraint 3 times in different sections
WHY:  Wastes context tokens, can introduce subtle contradictions
FIX:  State once, clearly, in the right section
```

### Missing Examples
```
BAD:  "Format the output correctly" (no example of what "correctly" means)
WHY:  Examples are "one of the most reliable ways to steer Claude's output"
FIX:  Include 2-3 examples of the desired output format
```

### Vague Role Definition
```
BAD:  "You are a helpful assistant" / No role at all
WHY:  "Setting a role focuses Claude's behavior and tone"
FIX:  "You are a senior legislative drafter specializing in Bangsamoro
      parliamentary bills, with expertise in Philippine constitutional law
      and Islamic jurisprudence."
```

### Context-Ignorant File References
```
BAD:  "Use the attached files" (no specifics about what files contain)
WHY:  With RAG, Gemini may not see all files at once. It needs to know
      what to look for and where.
FIX:  "The project knowledge base contains: [list files and their purpose].
      When drafting bills, first search for relevant provisions in the BOL
      and Administrative Code files."
```

### Instruction Bloat
```
BAD:  2000+ words of instructions covering every conceivable scenario
WHY:  Long instructions compete with knowledge base for context space.
      Claude 4.6 is smart enough to generalize from clear, concise guidance.
FIX:  Keep instructions under 800 words. Use examples instead of
      exhaustive rules. Trust Claude to generalize.
```

---

## Best Practices Checklist

From Anthropic's official documentation, adapted for Projects:

### Role & Context
- [ ] Clear role definition (who Claude is in this project)
- [ ] Context for WHY instructions matter (not just WHAT)
- [ ] Domain-specific terminology defined or demonstrated

### Instructions
- [ ] Positive framing (what to do, not what to avoid)
- [ ] Sequential steps for ordered processes
- [ ] XML tags for complex instruction sets
- [ ] Examples for output format (2-3 minimum)
- [ ] Normal language (no ALL-CAPS unless truly critical)

### Output Control
- [ ] Desired format explicitly specified
- [ ] Tone and style demonstrated (not just described)
- [ ] Length expectations set where relevant

### Knowledge Base Integration
- [ ] File inventory described in instructions
- [ ] Purpose of each file/category explained
- [ ] Retrieval guidance for RAG scenarios
- [ ] Priority order when sources conflict

### Edge Cases
- [ ] What to do when information isn't in the knowledge base
- [ ] How to handle ambiguous user requests
- [ ] Fallback behavior defined

---

## Projects-Specific Considerations

### Context Isolation
Each chat in a project starts fresh. Only the knowledge base and instructions carry over. This means:
- Instructions must be self-contained (no "as we discussed" assumptions)
- Critical context should be in the knowledge base, not past chats
- Instructions should tell Gemini how to orient at the start of each chat

### RAG Behavior
On paid plans, when knowledge exceeds context limits, RAG auto-activates:
- Claude searches and retrieves relevant chunks, not full files
- Instructions should guide what to search for, not assume full file access
- File names and content descriptions in instructions help RAG work better

### Memory
Projects maintain separate memory summaries per project on paid plans:
- Memory accumulates across chats within the project
- Instructions can reference patterns that will be remembered
- Don't rely on memory for critical workflow details — put those in instructions

### Token Budget
Project instructions + knowledge base share the context window:
- Shorter instructions = more room for knowledge base content
- Every token in instructions competes with document retrieval
- Aim for maximum impact per token in instructions
