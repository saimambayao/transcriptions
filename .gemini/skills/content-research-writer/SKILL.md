---
name: content-research-writer
description: Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real-time feedback on each section. Transforms your writing process from solo effort to collaborative partnership.
argument-hint: "[topic]"
---

# Content Research Writer

This skill acts as your writing partner, helping you research, outline, draft, and refine content while maintaining your unique voice and style.

## When to Use This Skill

- Writing blog posts, articles, or newsletters
- Creating educational content or tutorials
- Drafting thought leadership pieces
- Researching and writing case studies
- Producing technical documentation with sources
- Writing with proper citations and references
- Improving hooks and introductions
- Getting section-by-section feedback while writing

## What This Skill Does

1. **Collaborative Outlining**: Helps you structure ideas into coherent outlines
2. **Research Assistance**: Finds relevant information and adds citations
3. **Hook Improvement**: Strengthens your opening to capture attention
4. **Section Feedback**: Reviews each section as you write
5. **Voice Preservation**: Maintains your writing style and tone
6. **Citation Management**: Adds and formats references properly
7. **Iterative Refinement**: Helps you improve through multiple drafts

## Verification Protocol

**After output (DETECT):**
Invoke `/fact-checker` to verify names, institutions, and legislation references.
Read `~/.gemini/skills/fact-checker/references/source-preload-protocol.md` — MANDATORY: load source text BEFORE writing any citation. No claims from training data when local source exists.
If a claim cannot be verified against loaded source files, mark it `[UNVERIFIED]` — never guess or fabricate. See source-preload-protocol.md Section 4.
For transcripts, verify all person names against `~/.gemini/skills/bangsamoro/references/barmm-officials-2025-2026.md`.

**Before publishing (CONFIRM):**
Present verification results to the user.

## How to Use

### Setup Your Writing Environment

Create a dedicated folder for your article:
```
mkdir ~/writing/my-article-title
cd ~/writing/my-article-title
```

Create your draft file:
```
touch article-draft.md
```

Open Gemini CLI from this directory and start writing.

### Basic Workflow

1. **Start with an outline**:
```
Help me create an outline for an article about [topic]
```

2. **Research and add citations**:
```
Research [specific topic] and add citations to my outline
```

3. **Improve the hook**:
```
Here's my introduction. Help me make the hook more compelling.
```

4. **Get section feedback**:
```
I just finished the "Why This Matters" section. Review it and give feedback.
```

5. **Refine and polish**:
```
Review the full draft for flow, clarity, and consistency.
```

## Instructions

When a user requests writing assistance:

1. **Understand the Writing Project**
   
   Ask clarifying questions:
   - What's the topic and main argument?
   - Who's the target audience?
   - What's the desired length/format?
   - What's your goal? (educate, persuade, entertain, explain)
   - Any existing research or sources to include?
   - What's your writing style? (formal, conversational, technical)

2. **Collaborative Outlining**
   
   Help structure the content:
   
   ```markdown
   # Article Outline: [Title]
   
   ## Hook
   - [Opening line/story/statistic]
   - [Why reader should care]
   
   ## Introduction
   - Context and background
   - Problem statement
   - What this article covers
   
   ## Main Sections
   
   ### Section 1: [Title]
   - Key point A
   - Key point B
   - Example/evidence
   - [Research needed: specific topic]
   
   ### Section 2: [Title]
   - Key point C
   - Key point D
   - Data/citation needed
   
   ### Section 3: [Title]
   - Key point E
   - Counter-arguments
   - Resolution
   
   ## Conclusion
   - Summary of main points
   - Call to action
   - Final thought
   
   ## Research To-Do
   - [ ] Find data on [topic]
   - [ ] Get examples of [concept]
   - [ ] Source citation for [claim]
   ```
   
   **Iterate on outline**:
   - Adjust based on feedback
   - Ensure logical flow
   - Identify research gaps
   - Mark sections for deep dives

3. **Conduct Research**
   
   When user requests research on a topic:
   
   - Search for relevant information
   - Find credible sources
   - Extract key facts, quotes, and data
   - Add citations in requested format
   
   Example output:
   ```markdown
   ## Research: AI Impact on Productivity
   
   Key Findings:
   
   1. **Productivity Gains**: Studies show 40% time savings for 
      content creation tasks [1]
   
   2. **Adoption Rates**: 67% of knowledge workers use AI tools 
      weekly [2]
   
   3. **Expert Quote**: "AI augments rather than replaces human 
      creativity" - Dr. Jane Smith, MIT [3]
   
   Citations:
   [1] McKinsey Global Institute. (2024). "The Economic Potential 
       of Generative AI"
   [2] Stack Overflow Developer Survey (2024)
   [3] Smith, J. (2024). MIT Technology Review interview
   
   Added to outline under Section 2.
   ```

4. **Improve Hooks**
   
   When user shares an introduction, analyze and strengthen:
   
   **Current Hook Analysis**:
   - What works: [positive elements]
   - What could be stronger: [areas for improvement]
   - Emotional impact: [current vs. potential]
   
   **Suggested Alternatives**:
   
   Option 1: [Bold statement]
   > [Example]
   *Why it works: [explanation]*
   
   Option 2: [Personal story]
   > [Example]
   *Why it works: [explanation]*
   
   Option 3: [Surprising data]
   > [Example]
   *Why it works: [explanation]*
   
   **Questions to hook**:
   - Does it create curiosity?
   - Does it promise value?
   - Is it specific enough?
   - Does it match the audience?

5. **Provide Section-by-Section Feedback**
   
   As user writes each section, review for:
   
   ```markdown
   # Feedback: [Section Name]
   
   ## What Works Well
   - [Strength 1]
   - [Strength 2]
   - [Strength 3]
   
   ## Suggestions for Improvement
   
   ### Clarity
   - [Specific issue] → [Suggested fix]
   - [Complex sentence] → [Simpler alternative]
   
   ### Flow
   - [Transition issue] → [Better connection]
   - [Paragraph order] → [Suggested reordering]
   
   ### Evidence
   - [Claim needing support] → [Add citation or example]
   - [Generic statement] → [Make more specific]
   
   ### Style
   - [Tone inconsistency] → [Match your voice better]
   - [Word choice] → [Stronger alternative]
   
   ## Specific Line Edits
   
   Original:
   > [Exact quote from draft]
   
   Suggested:
   > [Improved version]
   
   Why: [Explanation]
   
   ## Questions to Consider
   - [Thought-provoking question 1]
   - [Thought-provoking question 2]
   
   Ready to move to next section!
   ```

6. **Preserve Writer's Voice**
   
   Important principles:
   
   - **Learn their style**: Read existing writing samples
   - **Suggest, don't replace**: Offer options, not directives
   - **Match tone**: Formal, casual, technical, friendly
   - **Respect choices**: If they prefer their version, support it
   - **Enhance, don't override**: Make their writing better, not different
   
   Ask periodically:
   - "Does this sound like you?"
   - "Is this the right tone?"
   - "Should I be more/less [formal/casual/technical]?"

7. **Citation Management**

   Handle references based on user preference:

   **Inline Citations**:
   ```markdown
   Studies show 40% productivity improvement (McKinsey, 2024).
   ```

   **Numbered References**:
   ```markdown
   Studies show 40% productivity improvement [1].

   [1] McKinsey Global Institute. (2024)...
   ```

   **Footnote Style**:
   ```markdown
   Studies show 40% productivity improvement^1

   ^1: McKinsey Global Institute. (2024)...
   ```

   **PDF Footnote Rendering:** When the document will be rendered as PDF, footnotes must appear on a separate page with a 'Footnotes' heading — never inline after chapter text. Ensure the `footnotes` markdown extension is enabled in generate-pdf.py, and the guidebook-template.html has `page-break-before: always` on the `.footnote` class. See `/guidebook-writer` build-pipeline.md for the full CSS pattern.

   Maintain a running citations list:
   ```markdown
   ## References
   
   1. Author. (Year). "Title". Publication.
   2. Author. (Year). "Title". Publication.
   ...
   ```

8. **Final Review and Polish**
   
   When draft is complete, provide comprehensive feedback:
   
   ```markdown
   # Full Draft Review
   
   ## Overall Assessment
   
   **Strengths**:
   - [Major strength 1]
   - [Major strength 2]
   - [Major strength 3]
   
   **Impact**: [Overall effectiveness assessment]
   
   ## Structure & Flow
   - [Comments on organization]
   - [Transition quality]
   - [Pacing assessment]
   
   ## Content Quality
   - [Argument strength]
   - [Evidence sufficiency]
   - [Example effectiveness]
   
   ## Technical Quality
   - Grammar and mechanics: [assessment]
   - Consistency: [assessment]
   - Citations: [completeness check]
   
   ## Readability
   - Clarity score: [evaluation]
   - Sentence variety: [evaluation]
   - Paragraph length: [evaluation]
   
   ## Final Polish Suggestions
   
   1. **Introduction**: [Specific improvements]
   2. **Body**: [Specific improvements]
   3. **Conclusion**: [Specific improvements]
   4. **Title**: [Options if needed]
   
   ## Pre-Publish Checklist
   - [ ] All claims sourced
   - [ ] Citations formatted
   - [ ] Examples clear
   - [ ] Transitions smooth
   - [ ] Call to action present
   - [ ] Proofread for typos
   
   Ready to publish!
   ```

## Writing Workflows

| Workflow | Steps |
|----------|-------|
| **Blog Post** | Outline > Research > Write intro (feedback) > Body sections (feedback each) > Conclusion > Polish |
| **Newsletter** | Hook ideas > Quick outline > Draft > Review for clarity > Polish |
| **Technical Tutorial** | Outline steps > Code examples > Explanations > Test > Troubleshooting > Review |
| **Thought Leadership** | Unique angle > Research perspectives > Thesis > Write with POV > Evidence > Conclusion |

## File Organization

```
~/writing/article-name/
├── outline.md          # Your outline
├── research.md         # All research and citations
├── draft-v1.md         # First draft
├── draft-v2.md         # Revised draft
├── final.md            # Publication-ready
└── sources/            # Reference materials
```

## Best Practices

- **Research**: Verify sources, use recent data, balance perspectives, link originals
- **Feedback**: Be specific ("Is this too technical?"), share concerns, ask questions
- **Voice**: Share writing samples, specify tone, flag mismatches ("Too formal for my style")

## Subagent Honesty Rules

Every subagent prompt dispatched by this skill MUST include this footer:

> HONESTY RULES:
> 1. Only extract values explicitly stated in source documents. If ambiguous or missing, leave blank with a one-line reason.
> 2. A wrong answer is 3x worse than a blank answer. When in doubt, leave it blank.
> 3. Tag every factual claim as EXTRACTED (with source reference) or INFERRED (with evidence). Inferred claims will be verified first.

## Fact-Check Before Delivery

Before delivering the final content, run `/fact-checker` on the output. Research-backed content
is high-risk for citation errors, hallucinated sources, and wrong attributions. The fact-checker
verifies all names, dates, statistics, and citations against authoritative sources.

