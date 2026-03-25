# Claude Cowork

Most people open Claude Desktop, type a question, and close the app. They repeat this cycle daily, never realizing they are using roughly ten percent of what the tool can actually do. Claude Cowork turns that pattern inside out: instead of a chatbot that forgets everything between sessions, it becomes a persistent assistant that reads files, connects to applications, learns workflows, and executes tasks on a schedule -- even while the user is away from the keyboard.

This guide synthesizes eight deep-dive tutorials on Claude Cowork into actionable patterns for building a system that compounds over time. It covers the instruction hierarchy that governs behavior, the foundational architecture (folders, identity files, projects), the second brain as a persistent context layer, the skill and plugin ecosystem, the four keys to output quality, multi-skill system design, the connector layer that bridges external tools, artifacts for rapid tool-building, and the automation engine that turns Cowork into an always-on operator. Every pattern is grounded in demonstrated workflows, not theoretical possibilities.

---

## The Instruction Hierarchy

Claude's behavior is governed by a three-layer instruction cascade: **Claude-level settings** (broadest, applied to every conversation), **Project instructions** (scoped to a specific project and its chats), and **Chat-level instructions** (narrowest, applied to a single conversation). Each layer inherits from the one above it, and narrower scopes can refine but not override broader rules. [^6]

> **Key insight**: The instruction hierarchy mirrors the architecture of production-grade systems like CLAUDE.md files in Claude Code -- global rules at the top, project-specific rules in the middle, and session-level overrides at the bottom. Understanding this cascade is what separates users who get consistent, high-quality outputs from those who fight the same formatting battles in every chat. [^6]

- **Claude-level settings** -- personal preferences, communication style, and universal rules (e.g., "always ask clarifying questions before answering"). These persist across all projects and chats. [^6]
- **Project instructions** -- domain-specific context, uploaded reference files, and behavioral rules scoped to a single project. All chats within that project inherit these instructions automatically. [^6]
- **Chat-level context** -- the narrowest scope, where a single conversation's messages and uploaded files shape Claude's responses. [^6]

A particularly effective technique is embedding a meta-instruction at the Claude-level: "For any task, ask me about the goal, context, action, and output format." This forces Claude to gather requirements before generating, producing better first drafts across every project and chat. [^6]

**The takeaway**: The instruction hierarchy is not an implementation detail -- it is the architectural foundation. Getting the right instructions at the right level eliminates repetitive corrections and makes every new chat smarter by default.

## The Folder-as-Identity Architecture

The single most important step in Cowork setup is one most users skip entirely: pointing Claude at a folder. Without a linked folder, Cowork has no memory, no file access, no skills, and no context -- it is functionally indistinguishable from a basic chatbot. [^1][^2]

> **Key insight**: Each folder functions as a separate identity. A work folder carries business rules, professional tone, and domain-specific skills; a personal folder carries different apps, different goals, and a different Claude MD file. Think of folders as different phones, each configured for a different part of life. [^1]

The architecture nests in three layers. The **project** is the outermost container, holding memory, scheduled tasks, skills, plugins, and connectors. Inside the project sit one or more **folders** -- the workspaces where files live. Inside each folder lives the **Claude MD file** -- the instruction set Claude reads before every interaction. [^5]

- **Claude MD as onboarding packet** -- a plain text file containing six elements: who you are, your audience, your tone, your business context, your rules, and what to avoid. Claude reads this before processing any user input, every single time. [^1][^2] When the folder grows into a full knowledge base, the Claude MD also serves as a **navigation layer** -- a bridge that tells the AI agent how the folder is structured and where to retrieve or save specific types of data. The agent reads the Claude MD first, discovers the folder map, then navigates to the specific documents it needs for the current task. [^8]
- **Goals file** -- a separate markdown document specifying north-star goals on quarterly, monthly, and weekly cadences. Without goals, responses stay generic; with them, every output aligns to defined priorities. [^2]
- **Supporting context files** -- company information, glossaries, team member profiles, and domain-specific terminology. These files form the knowledge base that makes Cowork responses specific rather than boilerplate. [^2]

The system is self-reinforcing. After each session, Cowork can update its own Claude MD file -- like a chef revising the kitchen bible after learning a new technique. Over time, Day 1's generic responses become Day 30's personalized outputs and Day 90's autonomous workflows. [^2][^5]

**The takeaway**: A folder without a Claude MD file is just a chatbot; a folder with a well-structured Claude MD, goals file, and supporting context is the foundation of an AI employee that never forgets its training.

## Personal Context Transforms Output Quality

A recurring finding across multiple tutorials is that Claude's suggestions improve dramatically -- sometimes categorically -- when given personal context about the user. Generic prompts produce generic outputs. Personalized context produces outputs that map to the user's actual life, work, and frameworks. [^4]

> **Key insight**: Context architecture beats prompting. Investing in a personal dossier that Claude reads on every interaction yields better results than crafting elaborate individual prompts. [^4]

Nick Milo demonstrated this by asking Cowork to build an "intellectual dossier" -- a master digest of identity, beliefs, goals, and recurring themes -- by scanning his Obsidian vault. The resulting 40-note profile was "90% accurate" and transformed screenshot categorization from generic buckets into categories mapped to his personal ACE framework (Atlas, Calendar, Efforts). [^4]

The dossier goes into **Settings > General > Personal Preferences**, where it persists across all Cowork sessions. The effect is compound: every subsequent interaction benefits from the context, and the context can be periodically regenerated as roles, projects, or priorities shift.

For teams, Anthropic also built a **memory import page** that generates a structured prompt for ChatGPT or Gemini to export everything they know about a user. Paste the export back into Claude, and context transfer happens in under sixty seconds -- eliminating the biggest friction point in switching AI providers. [^2]

Without specific context, AI produces what one practitioner calls the "brown paint" effect: trained on all colors (all websites, all emails, all styles), it defaults to an undifferentiated average that satisfies nobody. The solution is not better prompting -- it is better context architecture. Feed Claude specific examples, specific rules, and specific domain knowledge, and the output shifts from generic brown to the precise shade the user actually needs. [^7]

The compounding nature of context also creates a durable competitive advantage. Every decision logged, every correction saved, every project documented, and every skill built accumulates intelligence that makes the system perform better over time. A competitor who starts six months later is not just behind on the tool -- they are behind on six months of accumulated context that cannot be replicated overnight. Even when better models arrive, the same context becomes more powerful, making the accumulated knowledge base -- not the model -- the actual moat. [^8]

**The takeaway**: The highest-leverage investment in Cowork is not learning prompt engineering; it is building a rich, accurate personal context layer that makes every prompt more effective by default -- and that compounds into an insurmountable advantage over time.

## The Second Brain Architecture: Persistent, Bidirectional, Portable

The folder-as-identity concept reaches its full potential when the linked folder is not a loose collection of files but a structured second brain -- a knowledge base organized by domain, with the AI agent reading from it and writing back to it across every session. Tools like Obsidian provide a visual overlay on what is ultimately just a folder of markdown files on disk, requiring no cloud service, no API, and no MCP server. [^8]

> **Key insight**: For AI agents to become the main interface for work, they need persistent context -- the missing layer beyond reasoning, MCPs, and skills. A second brain provides that layer: not a few facts in a memory document, but thousands of structured context files covering business strategy, projects, brand, workflows, team, and personal information. [^8]

The architecture rests on three principles:

1. **Bidirectional context flow** -- The AI agent does not merely read from the knowledge base; it writes back. Decisions, rules, project updates, and corrections made during any chat session get logged directly into the second brain. A rule added in one conversation ("never use em dashes in content") gets saved to a writing preferences document and automatically applies across every skill that references that document. The more the system is used, the more context it accumulates, and the better every subsequent interaction becomes. [^8]
2. **Cross-platform portability** -- Because the second brain is just a folder of markdown files, any AI agent can access it. Claude Cowork, Claude Code, Codex, or any other provider can be pointed at the same folder. The knowledge base is not locked into one tool's proprietary format -- it is a portable asset that transfers across platforms and survives provider switches. [^8]
3. **Team scaling** -- An entire team can share the same second brain with strategy documents, ICP understanding, tone of voice references, and company goals. Any team member's AI agent can then produce on-brand content and make context-aware decisions from day one. The structure splits into a **Business OS** (with departments, teams, onboarding, and SOP folders) for organizations, or a **Personal OS** (a simplified version without those folders) for solopreneurs. [^8]

The recommended starting point is modest: approximately five files covering identity, goals, and core business context. The system grows naturally as usage increases. Over-optimizing the file structure on day one is counterproductive; the structure should evolve to match how the AI agent actually navigates and retrieves information, with the Claude MD file updated whenever navigation breaks down. [^8]

**The takeaway**: A second brain is not a note-taking system -- it is the persistent context layer that transforms Cowork from a stateless chatbot into a long-running collaborator with institutional memory. The combination of bidirectional updates, cross-platform portability, and team sharing makes the accumulated knowledge base the most valuable asset in the system.

## Skills and Plugins: Reusable Workflows That Compound

Skills are the mechanism that converts one-time workflows into repeatable, keyword-triggered processes. At their core, skills are just **markdown instruction files** (skills.md) -- not proprietary code, not compiled binaries, not magic. Each skill tells Claude how to perform a specific task: what inputs to expect, what structure to follow, and what output to produce. Claude checks its skill library before responding, applying the relevant skill automatically when it recognizes the pattern. [^1][^4][^6]

> **Key insight**: Building a skill is not just completing a task -- it is documenting what works and teaching AI to replicate it. Over time, the skill library becomes the most valuable asset in the system. [^3][^4]

A structural evolution in skill design changes how reference files are managed. The traditional approach embeds context files (ICP documents, voice guides, examples) inside each skill folder. This works but creates a maintenance burden: updating an ICP document means updating it in every skill that carries a copy. The **skills-point-to-vault** pattern inverts this: skills contain only process instructions (the skills.md file) and point to shared reference files in the second brain. A LinkedIn skill and a newsletter skill can share the same ICP, voice, and pain points documents; a rule added to writing preferences in one chat automatically applies to both. One update propagates to all skills that reference the file, eliminating manual synchronization across dozens of skills. [^8]

Skills can be created three ways: uploading a pre-built file, using Claude's built-in "Create with Claude" wizard, or converting a perfected ad-hoc workflow by saying "make this into a skill." [^1][^2][^4][^6] The built-in wizard is particularly effective because it asks structured clarification questions -- output types, expected inputs, structure rigidity -- that catch requirements the user might miss. [^3] A growing ecosystem of community skill repositories (Anthropic's official collection, GitHub repos like awesome-claude-skills, and third-party marketplaces) provides starting points, though downloaded skills should always be reviewed for security before installation -- verifying they do not access unexpected files or transmit data externally. [^6]

**Plugins** extend the skill concept into department-level workflow packs. Cowork ships with pre-built plugins organized by function (finance, legal, HR, design, operations, marketing), each containing multiple slash commands that trigger entire workflows. [^2] A legal plugin, for example, includes `/brief` for contextual briefing and `/review-contract` for full contract analysis with color-coded findings.

Custom plugins are shareable. Export a folder and teammates can import it into their own Cowork environment, inheriting the full workflow without needing to understand the underlying instructions. [^2] One particularly effective pattern is the **plugin-as-onboarding** approach: a starter pack plugin that runs a `/setup` interview (name, role, goals, communication preferences), creates the folder structure and claude.md automatically, and includes daily workflow skills (`good morning` for session resume, `wrap up` for end-of-day logging). This turns a 30-minute manual setup into a 2-minute guided experience that any non-technical user can complete. [^7]

**The takeaway**: Every ad-hoc task that might be repeated is a candidate for a skill. The discipline of converting workflows into skills creates a compounding library of institutional knowledge that gets more valuable with each addition.

## The NotebookLM-to-Skill Pipeline

Building a domain-specific skill requires domain knowledge, and acquiring that knowledge manually is the bottleneck. The NotebookLM deep research feature -- which browses hundreds of websites, creates a research plan, refines searches iteratively, and outputs a structured, source-grounded report -- collapses this bottleneck from hours to minutes. [^3]

> **Key insight**: The quality of a skill is bounded by the quality of the domain knowledge it encodes. NotebookLM deep research provides grounded, cited knowledge that transforms skills from generic prompt templates into genuine domain expertise. [^3]

The workflow follows a clear sequence:

1. **Research** -- Run 2-3 deep research queries on the target domain in NotebookLM, each covering a different angle (frameworks and strategy, tools and workflows, common mistakes). All queries layer into the same notebook, building a comprehensive knowledge base. [^3]
2. **Synthesize** -- Ask NotebookLM to extract patterns: core principles across sources, most-mentioned frameworks, step-by-step processes. The output is grounded and cited, not generated from scratch. [^3]
3. **Build** -- Paste the synthesized research into Claude's skill creator as a "processes knowledge" section. Claude's clarification questions refine the skill's output format, input expectations, and structure rigidity. [^3]
4. **Deploy** -- The resulting skill works across all Claude modes: Chat, Cowork, and Code. In Cowork, skills combine with connectors and scheduled tasks for full automation. [^3]

Skills built this way are also portable. The same skill file can be transferred to other AI models (ChatGPT, Gemini), though Cowork's integration layer makes Claude the preferred deployment target. [^3]

**The takeaway**: NotebookLM deep research is the fastest path to building skills grounded in real domain knowledge rather than generic LLM assumptions. The research-synthesize-build-deploy pipeline turns any subject-matter expertise into a reusable AI capability.

## Four Keys to Incredible AI Outputs

Most users who report that "AI outputs are mediocre" are violating at least one of four principles that experienced practitioners have converged on independently. These are not prompting tricks -- they are architectural decisions about how context, inputs, feedback, and iteration flow through the system. [^7]

> **Key insight**: If Gordon Ramsay is given moldy tomatoes, the pizza will be bad no matter how skilled the chef. Better inputs produce better outputs -- and "inputs" means context files, examples, and skill instructions, not just the user's prompt. [^7]

The four keys are:

1. **Focused context only** -- Give Claude exactly what it needs for the specific output, no more. Writing an email? Load only the email skill and client context, not the entire second brain. The metaphor is a kitchen, not a pantry: the chef needs pizza ingredients on the counter, not the entire grocery store inventory. This is why spawning sub-agents for different process stages works so well -- each agent gets a clean whiteboard with only its task-specific context. [^7]
2. **Better inputs, better outputs** -- Quality of context files, examples, and skill instructions directly determines output quality. Great customer research, concise past examples, and well-structured skill recipes produce great outputs. Bad research, generic examples, and bloated skills produce generic outputs. [^7]
3. **Human checkpoints and feedback** -- Never let Claude one-shot a complex output. Build review steps into every multi-stage workflow: "What do you think?" after each draft, with the user adding refinement thoughts before the next stage. The lazy path (accepting the first output) always produces worse results. [^7]
4. **Frequent iteration through doing** -- Define what NOT to do rather than trying to specify every positive requirement. Let Claude have creative freedom within constraints. Run the skill repeatedly, refining inputs and recipes each time. The skill improves with each iteration -- but only if the user actually runs it and provides feedback. [^7]

**The takeaway**: Output quality is not a model problem -- it is an architecture problem. Address all four keys and even simple skills produce professional-grade results.

## Multi-Skill System Design: Chained Workflows

Single skills hit a quality ceiling because they try to handle too many responsibilities in one context. The breakthrough comes from decomposing complex workflows into chains of specialized skills, each with focused context, connected by human checkpoints and sub-agent review. [^7]

> **Key insight**: A skill that is bad at writing all email types becomes five skills that are each excellent at one type. Separation gives each skill focused context for better outputs -- the system outperforms any single monolithic skill. [^7]

A demonstrated production architecture (generating $2,000/month in email copywriting revenue) follows this pattern: [^7]

1. **Idea skill** -- pulls condensed client context (2-page summary, not 150 pages) plus distilled past content ideas → outputs 15 candidate ideas
2. **Human checkpoint #1** -- user selects an idea, adds refinement thoughts
3. **Type-specific skill** (valuable insight, sales, promotion, story) -- runs with focused context for that email type only, following a structured co-writing process
4. **Sub-agent review** -- spawns a fresh agent with a clean whiteboard and quality criteria (no authorship bias, no prior context from the drafting phase) → produces a reviewed final draft
5. **Human checkpoint #2** -- user makes finishing touches and ships

The critical design principle is context separation. Version 1.0 of this system used one skill that loaded all email types and all context -- producing mediocre results. Version 2.0 decomposed into specialized skills where each stage received only its required ingredients. The improvement was categorical, not incremental. [^7]

Building such a system follows a repeatable process: gather good examples of the desired output, document the rough manual process (Claude will suggest improvements), design concise context files (condense raw material into what Claude actually needs), run the skill at least twice to iterate, and carefully review the generated skill.md for misinterpretations. [^7]

**The takeaway**: For any workflow complex enough to have multiple stages, decompose into specialized skills chained with human checkpoints. Each skill gets focused context, and the chain produces results no single skill can match.

## Connectors, Extensions, and the Ecosystem Layer

Without connectors, users must manually copy-paste between Claude and every other application. With connectors, Cowork can read email, check calendars, access cloud storage, post to messaging platforms, and trigger actions across the full application stack -- all from a single prompt. [^1][^2][^5]

> **Key insight**: A single prompted workflow can now span multiple applications. Read emails, check calendar conflicts, draft a reply, and save a summary to Drive -- all in one Cowork interaction. [^2]

Cowork's external integration layer splits into two categories. **Connectors** link Claude to web applications (Gmail, Google Calendar, Notion, Slack) and are available in both the web and desktop versions. **Extensions** link Claude Desktop to local machine applications (Apple Notes, Chrome, file system, PDF tools) and are desktop-only. The distinction matters: connectors reach outward to cloud services, while extensions reach inward to the user's device. [^6] Cowork currently offers approximately 38 native connectors, with setup as simple as navigating to Customize > Connectors > Browse, clicking an app, and authorizing. [^1][^2][^5]

An important operational detail: **connector hygiene**. Each active connector consumes tokens as Claude reads its available tools. Having ten or more connectors enabled when only two are needed wastes context window capacity. Disabling unused connectors for each project or task keeps token usage efficient and responses faster. [^6]

For applications without native support, two paths extend the ecosystem. **Zapier MCP** connects to over 8,000 apps with 30,000+ actions -- create an MCP server at zapier.com/mcp, select Claude Cowork as the client, add tools, and paste the URL into Cowork's connector settings. [^1][^2][^5] For more granular control, **custom MCP servers** can be built using tools like n8n. This approach solved a specific limitation: the default Gmail connector can read messages but cannot send them. By building an n8n workflow with an MCP server trigger and a "send email" tool, then connecting the server URL to Claude as a custom connector, the capability gap is closed without waiting for Anthropic to update the native connector. [^6]

Connectors become particularly powerful when combined with projects. Each project can have its own set of active connectors scoped to its domain -- a YouTube project connected to analytics APIs, a finance project connected to receipt scanners, a legislative project connected to document repositories. [^5]

**The takeaway**: Connectors and extensions transform Cowork from an intelligent text processor into an orchestration layer that can read from and write to the tools where real work happens -- and custom MCP servers ensure that no integration gap is permanent.

## Artifacts: Rapid Interactive Tool-Building

Artifacts represent a capability that sits between chat responses and full software development. When Claude generates an artifact, it produces an interactive mini-application -- a calculator, dashboard, planner, or website -- that renders live inside the chat window. Unlike plain text responses, artifacts are usable tools that can be published with a shareable link, embedded in existing websites, or downloaded as self-contained code. [^6]

> **Key insight**: Artifacts bridge the gap between "AI gave me an answer" and "AI gave me a tool." For prototyping, stakeholder demos, and quick utility-building, artifacts eliminate the deployment friction that stops most AI outputs from becoming useful. [^6]

The workflow is iterative. A first prompt generates the base artifact; follow-up prompts refine it -- adding dark mode, animations, chart visualizations, responsive layouts. Claude can build a complete portfolio website from a LinkedIn PDF, a Kanban-style productivity dashboard with calendar integration, or a budget calculator with interactive inputs, all within the artifact environment. [^6]

Artifacts have a clear boundary: they are ideal for prototyping and showcasing but cannot directly integrate with external databases or APIs at the production level. Full production applications require Claude Code for proper engineering. The value of artifacts is speed-to-demo -- a concept that would take hours to scaffold in a dev environment can be rendered in minutes, shared with stakeholders via a published link, and iterated on in real time. [^6]

**The takeaway**: Artifacts are the fastest path from idea to interactive prototype. For concepts that need to be seen and clicked before they are approved for development, artifacts compress the feedback loop from days to minutes.

## Scheduled Tasks: The Automation Engine

Scheduled tasks represent Cowork's most transformative capability: the ability to run workflows on a recurring basis without any manual trigger. Set a time, set a cadence (hourly, daily, weekdays, weekly, custom), and Cowork executes the task automatically. [^1][^2][^5]

> **Key insight**: The combination of skills, connectors, and scheduled tasks creates an AI employee that runs operations on autopilot -- trained once, executing forever. [^1]

Practical examples demonstrated across the tutorials include:

- **Morning briefing** -- runs at 7-8 AM, reads Claude MD, goals file, and task lists, checks email and calendar, outputs a structured daily briefing. [^1][^2]
- **Competitor research dashboard** -- scrapes competitor content daily, generates an HTML dashboard with trending topics, content gaps, and filming priorities, then sends a Slack notification. [^2]
- **End-of-day wrap-up** -- summarizes what Claude accomplished, lists unfinished items, and sets priorities for the next day. [^1]
- **Weekly analytics report** -- pulls channel data, formats it, and saves to Google Drive every Monday. [^2][^5]

Any ad-hoc task can be converted into a scheduled task: complete the workflow once, then tell Claude "turn this into a scheduled task." [^2] Scheduled tasks are also project-scoped, meaning only relevant automations run within each project domain. [^5]

One important constraint: the computer must be awake and Claude Desktop must be open for scheduled tasks to trigger. Tasks will not run if the laptop is closed. [^2]

**The takeaway**: Scheduled tasks close the loop on Cowork's four-superpower stack. Identity (Claude MD) + Workflows (skills) + App Access (connectors) + Automation (scheduled tasks) = a system that handles operational overhead while the user focuses on judgment-intensive work.

## Projects: The Organizational Layer That Makes Everything Scale

Cowork Projects, released in early 2026, solve the organizational problem that emerges as usage grows. Before projects, everything lived in one workspace: memory got cluttered, rules from one domain bled into another, and files accumulated in a single undifferentiated folder. [^5]

> **Key insight**: A project is not a folder -- it is an entire ecosystem that holds memory, scheduled tasks, skills, plugins, connectors, and a dedicated Claude MD file, all scoped to a single domain. [^5]

The separation has concrete benefits:

- **Memory stays focused** -- YouTube analytics rules do not contaminate finance workflows. [^5]
- **Rules are domain-specific** -- each project's Claude MD defines how Claude should behave in that context alone. [^5]
- **Scheduled tasks are scoped** -- only relevant automations run within each project. [^5]
- **Outputs stay organized** -- HTML dashboards, presentations, and reports are grouped by domain. [^5]

Projects also support **multi-folder selection** -- working across several folders within one project -- and **starred chats** for pinning important conversations for quick reference. [^5]

A particularly powerful feature is **Cowork Dispatch**: the ability to text Claude from the phone app and trigger tasks on the desktop, scoped to a specific project. This enables on-the-go task execution without being at the computer. [^5]

The recommended approach is one project per major business area or workflow. Projects compound over time: Day 1 feels generic, Day 30 Claude knows preferences and runs tasks automatically, and Day 90 Claude functions as a team member responding to keywords and handling full workflows. [^5]

**The takeaway**: Projects are the organizational infrastructure that prevents Cowork from collapsing under its own success. Without them, a growing skill library and expanding connector set become noise. With them, each domain gets a clean, focused, compounding AI workspace.

---

## For Your Work

The patterns above map directly to your multi-role architecture: OOBC governance consultant, solo developer across 9 platforms, MoroTech founder, and legislative support for the BTA Parliament. Cowork is not a replacement for your Claude Code CLI setup -- it is the distribution layer that lets non-technical collaborators access your systems. The second brain and skills-point-to-vault patterns are particularly relevant because you already operate this architecture through your Obsidian vault and skills-bucket system -- the new insight is formalizing the reference-sharing pattern and extending it to team use.

### Applications

- **e-Bangsamoro** -- create a Cowork Project per portal (Parliamentary, Ministerial, Budget, Citizen) with scoped Claude MD files and folder access limited to the relevant BOL chapters and BAA references, reducing hallucination risk during policy drafting; use artifacts to generate quick interactive prototypes of portal features for stakeholder demos before committing to full React development [^1][^4][^5][^6]
- **OOBC** -- package /bill-drafter, /legislative-briefer, and /policy-recommendation as Cowork plugins that Prof. Noron Andan's staff can invoke through the GUI without touching the terminal; a daily scheduled task could scan for new BAAs and BTA agenda items and surface a morning legislative briefing; add a Claude-level instruction for OOBC team members to "always ask about goal, context, action, and output format" -- this forces Claude to gather requirements before generating, reducing AI slop that government stakeholders reject; build a KJ-style onboarding plugin (`/setup-oobc`) that interviews the user about their OOBC role, creates folder structure, and generates a claude.md with BARMM-specific conventions automatically [^2][^5][^6][^7]
- **Parliamentarian** -- the research synthesis workflow (point Claude at a folder of related BAAs, surface convergent themes and contradictions) maps directly to legislative research for interpellation questions and committee hearings [^4]
- **MoroTech/SEED Initiative** -- your 124 training course modules could be distributed as Cowork plugins: /training-assistant for facilitator guides, /cooperative for cooperative governance modules, evaluation form generators triggered by slash commands [^1][^2]
- **OBCMS** -- Zapier MCP (8,000+ apps) opens integration paths for connecting to government reporting systems, BARMM internal tools, and regional LGU databases; for gaps where Zapier lacks a native connector, build custom MCP servers via n8n to extend Claude Desktop capabilities for OOBC regional coordinators [^1][^2][^5][^6]
- **Bangsamoro Scholars Association / Moro Developers Community** -- shareable Cowork project templates could onboard members with pre-configured skills for scholarship tracking, community content creation, and event coordination [^5]
- **NotebookLM + /expert-builder** -- the clarification question pattern (output types, expected inputs, structure rigidity) should be added to your /skill-creator and /expert-builder workflows to produce more focused skills on the first pass [^3]
- **Vault integration** -- your dual-layer memory system (Claude Code Memory + Obsidian Vault) is more rigorous than Cowork's self-improving Claude MD. Keep your explicit /vault-update review layer for Claude Code; use the auto-rewrite pattern only for Cowork folders used by non-dev staff who do not need that control [^2][^4] Ben's skills-point-to-vault pattern validates a structural refactor: move authoritative reference files (BARMM officials list, BOL provisions, BDP chapters) to shared vault locations and have /bangsamoro, /bill-drafter, /legislative-briefer, /fact-checker, and /speech-writer point to them instead of embedding copies. When you update the officials list after elections, one update propagates to all skills. For portability to Codex/Gemini via skills-bucket, your sync script can copy referenced files into each skill folder at export time -- giving you both maintainability (vault references) and portability (embedded copies in the bucket). [^8]
- **OOBC institutional second brain** -- Ben's team sharing pattern maps directly to OOBC. A shared vault with `context/` (BARMM officials, BOL, BDP), `intelligence/` (meeting transcripts, policy decisions, committee reports), and `projects/` (ECCD Bill, OBC Peace Centers, etc.) would let any team member's AI agent have institutional context from day one. New consultants inherit the accumulated context rather than starting from zero. The compounding effect Ben describes -- six months of logged decisions, corrections, and rules -- applies directly to institutional capacity building. [^8]
- **Context as governance moat** -- every policy recommendation drafted, every bill reviewed, every legislative briefer produced accumulates institutional knowledge in your vault. This is the compounding advantage Ben describes: if OOBC started building institutional AI context now, any future office that tries to replicate the setup would be months behind on the accumulated intelligence that makes the tools actually perform. [^8]
- **/legislative-briefer decomposition** -- apply KJ's email system 2.0 architecture: split the monolithic 13-section CSW briefer into a research-gathering skill (identifies relevant BAAs, BOL provisions, committee reports), type-specific analysis skills (impact assessment, Shari'ah analysis, interpellation strategy), and a sub-agent reviewer that checks against BOL compliance criteria without authorship bias [^7]
- **Context condensation for BAAs** -- create a condensed 2-page BAA summary index from your 78 full BAA files, following KJ's principle of "don't give him 150 pages of random slop" -- this becomes the standard input for /bill-drafter and /legislative-briefer rather than loading all full texts [^7]
- **Connector hygiene** -- when setting up Cowork projects for OOBC team members, pre-configure only the connectors each project actually needs (e.g., Gmail + Drive for legislative correspondence, Calendar for session scheduling) and disable everything else to conserve tokens and reduce noise [^6]
- **Tarbiyyah-MS / MoroMarket** -- use artifacts to generate interactive enrollment dashboards for madrasah administrators and financial calculators for cooperatives, deployable as shared links without waiting for full app releases [^6]

### Priority Actions

1. **This week**: Create a "BARMM Legislative" Cowork Project pre-loaded with BOL references, BAA index, officials list, and a Claude MD enforcing your fact-checking and first-mention naming conventions -- test with one OOBC colleague
2. **This week**: Add a Claude-level personal preference for OOBC team members: "For any task, ask about goal, context, action, and output format before generating" -- this single instruction improves output quality across all their projects
3. **This week**: Test Claude Desktop's "Create with Claude" skill builder for a simple OOBC domain skill (e.g., OBC community registration workflow) and compare output quality against your manual skill creation process
4. **This month**: Convert /bill-drafter and /legislative-briefer into Cowork plugins with simplified Claude MD files; export as shareable folders for BTA Parliament staff
5. **This month**: Set up a Cowork scheduled task for daily BARMM legislative monitoring -- pulling from local reference files (BOL, BDP 2023-2028, BAAs index) and outputting a briefing to a shared folder
6. **This month**: Build an n8n custom MCP server for OOBC email workflows (send legislative updates, distribute committee reports) to close the gap in Gmail's read-only default connector
7. **This quarter**: Build a "MoroTech Training" Cowork Project with /training-assistant packaged as a plugin, scoped to the SEED Initiative's curriculum folders -- pilot with 2-3 MoroTech facilitators
8. **This quarter**: Evaluate Cowork Dispatch for mobile-triggered governance workflows -- "Run the daily brief in my BARMM Legislative project" from your phone during field visits or BTA sessions
9. **This quarter**: Create artifact-based prototypes for 2-3 e-Bangsamoro portal features (MP profile pages, budget visualizations) to use in stakeholder presentations before committing development resources
10. **This week**: Audit your skill library for duplicated reference files (officials list, BOL provisions, BDP chapters) and identify which files should become shared vault references under the skills-point-to-vault pattern [^8]
11. **This month**: Refactor 2-3 high-use skills (/bangsamoro, /bill-drafter, /legislative-briefer) to point to shared vault references instead of embedded copies; update the skills-bucket sync script to copy referenced files into skill folders at export time for portability [^8]
12. **This month**: Draft a simplified "OOBC Institutional Second Brain" folder structure (context/, intelligence/, projects/) with a CLAUDE.md navigation file and seed it with existing vault files -- pilot with one OOBC colleague to test bidirectional context logging [^8]

---

## Related Knowledge Areas

- [[knowledge-areas/ai-agents/cowork/index|AI Agents: Cowork Knowledge Area]] — cross-source living synthesis

---

## References

[^1]: Mesarich, Brock. "Master 99% of Claude Cowork in 52 Minutes (Full Course)."
      *Brock Mesarich | AI for Non Techies*, 52:44. YouTube, March 2026.
      https://youtube.com/watch?v=9BEWaO_eEFE

[^2]: Mesarich, Brock. "How to Use Claude Cowork Better Than 99% of People."
      *Brock Mesarich | AI for Non Techies*, 20:43. YouTube, March 2026.
      https://youtube.com/watch?v=f95-O8C88uw

[^3]: Universe of AI. "NotebookLM Agent Skills: Build POWERFUL Claude AI Agents for ANYTHING!"
      *Universe of AI*, 15:06. YouTube, March 2026.
      https://youtube.com/watch?v=I-4cJgqF_JY

[^4]: Milo, Nick. "Give Me 20 Minutes. I'll Teach You 80% of Claude Cowork."
      *Linking Your Thinking with Nick Milo*, 21:29. YouTube, March 2026.
      https://youtube.com/watch?v=s3ccD6m6WKc

[^5]: Mesarich, Brock. "How to Use Claude Cowork Projects Better Than 99% of People."
      *Brock Mesarich | AI for Non Techies*, 23:53. YouTube, March 2026.
      https://youtube.com/watch?v=5bhh8ffHN6Q

[^6]: Aggarwal, Mayank. "Claude AI Crash Course | From Beginner to Building AI Tools (with Projects)."
      *Mayank Aggarwal*, 213:08. YouTube, March 2026.
      https://youtube.com/watch?v=P1yJcMV8o90

[^7]: Rainey, KJ. "Claude COWORK Full Course: Zero To Working AI Employee (2026)."
      *KJ Rainey*, 88:07. YouTube, March 2026.
      https://youtube.com/watch?v=C9gKWTzRukM

[^8]: van Sprundel, Ben. "How I use Claude Cowork + Obsidian To Run my Life."
      *Ben AI*, 21:54. YouTube, March 2026.
      https://youtube.com/watch?v=qo4YZvC1q5I
