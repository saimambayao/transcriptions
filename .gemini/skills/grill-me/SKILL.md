---
name: grill-me
description: |
  Interview the user relentlessly about a plan or design until reaching shared understanding,
  resolving each branch of the decision tree. Use when user wants to stress-test a plan,
  get grilled on their design, or mentions "grill me", "stress-test this plan",
  "interview me about this", or wants to think through a feature before coding.
  Also use when the user is about to start a complex feature and hasn't fully explored
  the design space yet — this skill prevents premature implementation.
allowed-tools: Read, Glob, Grep, Agent
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

If a question can be answered by exploring the codebase, explore the codebase instead.

## Next step

Once shared understanding is reached, suggest invoking `/write-a-prd` to formalize the plan into a Product Requirements Document.
