---
name: connect
description: |
  Take two domains, topics, or concepts and find connections between them using the Obsidian
  vault's notes and link graph. Use when user says "connect X and Y", "bridge these topics",
  "how do X and Y relate", or wants to find cross-domain patterns between two seemingly
  unrelated areas.
allowed-tools: Read, Glob, Grep
---

# Connect — Bridge Two Domains

Take two topics and find connections between them using your vault's accumulated knowledge.

## Process

1. **Accept two topics** from the user (e.g., "connect cooperative development and AI engineering")

2. **Scan the vault** for notes related to each topic:
   - Search by filename, tags, and content
   - Follow [[backlinks]] to find indirect connections
   - Check daily notes for co-occurrences

3. **Find bridges** — ideas, patterns, or principles that exist in both domains:
   - Shared vocabulary or concepts
   - Similar problems with different solutions
   - One domain's solution applicable to the other's problem
   - People, tools, or frameworks that span both
   - Analogies and metaphors that transfer

4. **Present connections** as numbered bridges:

For each bridge:
- **Bridge**: the connecting idea
- **In domain A**: how it manifests
- **In domain B**: how it manifests
- **The insight**: what this connection reveals or enables
- **Evidence**: [[vault notes]] that support this

5. End with a **synthesis** — what these connections collectively suggest about the user's work or thinking.

6. This is a read-only operation. Do not modify any files.
