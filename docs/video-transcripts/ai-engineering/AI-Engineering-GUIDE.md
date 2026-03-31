# AI Engineering

The gap between a mediocre AI workflow and a transformative one is rarely the model itself. It is the harness -- the system prompts, the workflow discipline, the feedback loops, the memory architecture, and the integration layer that connects AI to real-world tools and platforms. Understanding how to engineer these layers is what separates casual AI usage from production-grade agent systems.

This guide synthesizes patterns from practitioners who have built autonomous agents, desktop automation pipelines, mobile-triggered workflows, and iterative content optimization systems. The insights apply to anyone building AI-augmented products or workflows, regardless of which model or platform they use.

---

## The Harness Matters More Than the Model

The most consequential decision in AI engineering is not which model to use -- it is how to wrap that model with behavioral constraints, workflow structure, and quality guardrails. A cheap model with a disciplined harness consistently outperforms an expensive model running naked.

> **Key insight**: "What people usually call premium model quality is often not just the checkpoint. It is the surrounding workflow. It is the harness. It is the instructions. It is the memory system. It is the decomposition." [^3]

This principle manifests across every successful agent architecture. The GLM Mythos stack demonstrates it explicitly: a $3 model wrapped with a discipline layer (King Mode), a taste layer (front-end design skill), and an anti-chaos layer (GSD workflow) produces output that rivals models costing 30x more. [^3] The same principle applies to OpenClaw agents, where a single directive ("automate my marketing") combined with structured memory files and analytics feedback produces autonomous content creation. [^4]

The practical implication is that engineering effort should be allocated roughly 20% to model selection and 80% to harness design:

- **System prompts** that enforce discipline, not just capability -- zero-fluff rules, complexity-assessment triggers, and explicit behavioral constraints [^3]
- **Skill stacking** where each layer addresses a specific failure mode -- one for rigor, one for aesthetics, one for workflow structure [^3][^4]
- **Memory architecture** that prevents context degradation across long-running sessions [^3][^4]

**The takeaway**: Invest in the harness, not the model -- behavioral constraints, workflow structure, and memory systems compound in ways that raw model upgrades cannot.

## Structured Execution Prevents Context Rot

The single most common failure in AI-assisted development is context rot: the model starts forgetting earlier decisions, modifies unrelated files, and loses coherence as the session grows. Structured execution workflows directly attack this problem by decomposing work into phases with explicit boundaries.

> **Key insight**: "Most people just dump one giant prompt into a model and hope it does architecture, implementation, design, testing, and product judgment all in one go. That is exactly how you get a messy result." [^3]

The GSD (Get Stuff Done) workflow separates work into five stages: map the codebase, discuss the phase, plan the phase, execute the phase, and verify the work. [^3] This is not bureaucratic overhead -- it is a context management strategy. Each phase boundary acts as a checkpoint that prevents accumulated confusion from propagating forward.

The same pattern appears in agent-driven content optimization. The Larry Loop structures content creation into discrete stages -- research, create, post, analyze, iterate -- with analytics data flowing back into each cycle. [^4] Without this structure, the agent would drift toward content that is easy to generate rather than content that performs.

Effective anti-context-rot strategies share common elements:

- **Explicit phase boundaries** that force the model to re-orient before proceeding [^3]
- **Verification that checks outcomes, not just compilation** -- can the user sign in? Does the feature persist state? Does the empty state make sense? [^3]
- **Vertical slices** that deliver thin end-to-end functionality rather than broad horizontal layers [^3]
- **Analytics feedback** that grounds the agent in measurable reality rather than its own assumptions [^4]

**The takeaway**: Structure the workflow into phases with explicit boundaries and measurable verification -- unstructured sessions inevitably degrade.

## Autonomous Agents Need Feedback Loops, Not Dashboards

The most effective agent architectures do not rely on mission-control dashboards or complex multi-agent orchestration. They use simple feedback loops: the agent acts, measures the outcome, and adjusts its next action based on real data.

> **Key insight**: "This post proved that they actually know best. They've got all the metrics they need to create the perfect content. Just let them go nuts on it and figure out why." [^4]

The Larry Loop exemplifies this pattern. An OpenClaw agent creates TikTok slideshows, posts them as drafts, analyzes performance metrics, and feeds those analytics back into content creation. [^4] The agent learned on its own that certain hooks ("mum," "landlord," "nan") had different performance curves, and automatically pivoted away from hooks that were burning out -- dropping from 132K to 4K views over several posts. [^4] No human intervention was needed for this optimization; the feedback loop drove it.

The critical architectural decisions that make autonomous feedback loops work:

- **Single main agent with sub-agent spawning** rather than pre-configured multi-agent systems -- the agent decides when to delegate [^4]
- **Communication through familiar channels** (WhatsApp, iMessage) rather than custom dashboards -- reduces friction to near zero [^1][^4]
- **Memory files per project** that serve as portable context -- can be backed up, moved to new machines, or restored when context is lost [^4]
- **Diagnostic frameworks built into the loop** -- low views means bad hook; low views plus low conversions means bad CTA; low views plus high conversion rate means good CTA but bad hook [^4]

One counterintuitive finding: agent "mistakes" can outperform human judgment. When the Larry agent placed text at the top of a slide instead of the middle (violating the established design rule), it produced their best-performing content -- 400,000+ views -- because the imperfection drove audience engagement. [^4] This suggests that agents operating within structured feedback loops should be given room to experiment beyond their initial constraints.

**The takeaway**: Design agents around tight feedback loops with real metrics, not elaborate orchestration systems -- let performance data drive iteration.

## Bridging AI to the Physical World

The most impactful AI engineering work is not happening inside code editors -- it is happening at the boundary between AI systems and physical-world interfaces: desktop applications, mobile devices, social media platforms, and communication channels.

> **Key insight**: Computer use goes beyond MCP connectors -- if an app has an MCP connector, Claude uses that; computer use is for apps without connectors. [^1]

Four bridging patterns have emerged:

- **Desktop automation via computer use** -- Claude takes screenshots, moves the mouse, and types on the keyboard to interact with native applications that lack APIs. This enables control over Apple Calendar, Keyboard Maestro, Photos, and any GUI-based application. [^1] The tradeoff is speed: simple navigation is fast, but complex multi-step interactions degrade progressively. [^1]

- **Mobile-triggered remote execution** -- Cowork Dispatch and OpenClaw both enable phone-to-desktop task triggering, but with different architectures. Dispatch runs within Claude's ecosystem with zero setup but requires the desktop app to be open. [^2] OpenClaw uses WhatsApp or Telegram as the communication layer and supports cron-scheduled proactive tasks without a desktop dependency. [^4] Each parallel Dispatch agent runs independently -- sequential workflows where one task depends on another's output are not yet supported. [^2]

- **MCP gateways as execution middleware** -- Rather than connecting each tool individually, an MCP gateway bundles dozens of tools behind a single endpoint with managed OAuth authentication. Arcade.dev demonstrates this pattern: one gateway configuration grants agents access to Gmail, Slack, Google Docs, Google Calendar, and thousands of other services without embedding API keys in code. [^5] The gateway handles authorization, audit logging, and structured actions -- turning what would be brittle per-tool integrations into a standardized execution layer. [^5] This approach complements computer use: MCP gateways handle tools with APIs, computer use handles tools without them.

- **Social media as an output channel** -- Agents can create content and post it as drafts to platforms like TikTok, but platform algorithms penalize API-posted content (assuming bots). The workaround: post as draft via API, then add sound and publish manually from a mobile device. [^4]

**The takeaway**: The highest-leverage AI engineering connects agents to real-world interfaces -- desktop apps, mobile devices, and social platforms -- not just code and files.

## Closing the Planner-Operator Gap

Most agent systems share a fundamental weakness: they are excellent planners but unreliable operators. An agent can decompose "onboard a new designer" into sub-tasks -- crawl the company website for brand assets, compile a walkthrough, draft an onboarding email -- but actually sending that email through Gmail, posting a notification in Slack, and creating a shared Google Doc requires a different kind of infrastructure than the one that produced the plan.

> **Key insight**: "Antigravity's agent system stops at planning. They don't actually have a secure, scalable way to take action in the real world." [^5]

The planner-operator gap exists because planning is a language task (where LLMs excel) while execution is a systems integration task (where authentication, error handling, and state management dominate). Three architectural approaches to closing this gap have emerged in practice:

- **Execution middleware** -- A dedicated runtime layer sits between the planning agent and real-world tools, handling OAuth, audit logging, and structured actions. Arcade.dev exemplifies this: one MCP gateway endpoint bundles Gmail, Slack, Google Docs, and Calendar, and the agent calls them through standardized tool interfaces rather than raw API integrations. [^5]
- **Skill composition with native tool access** -- Instead of external middleware, agent capabilities are built as composable skill files that invoke tools already available in the agent's environment (MCP servers, CLI tools, file system). This trades breadth of tool coverage for tighter integration and version control. [^3][^4]
- **Human-in-the-loop bridging** -- The agent prepares everything (draft email, scheduled event, content post) but a human approves or publishes the final action. This is the most conservative approach and works well for high-stakes operations where auditability matters. [^5][^4]

The sub-agent deployment pattern compounds the planner-operator distinction. When a mission control system decomposes a project into parallel workspaces -- one agent building the front end, another handling the back end, a third managing tool integrations -- each sub-agent needs independent access to the execution layer. [^5] The coordination overhead is minimal because each agent operates on a distinct slice of the problem, communicating through shared project artifacts rather than direct message passing.

**The takeaway**: Recognize that planning and execution require different architectural solutions -- closing the gap between them is the defining challenge of production agent systems.

## Skills as Composable, Portable Units

The emerging standard for agent capabilities is the skill: a markdown file containing instructions, constraints, and workflow definitions that can be loaded, shared, modified, and stacked. Skills are replacing monolithic prompts the way functions replaced monolithic scripts.

> **Key insight**: "Skills are infinitely powerful because they're not just a black box. Anything that you download from Larry Brain, you own that thing." [^4]

Skills differ from traditional SaaS products in a fundamental way: they run locally, require no hosting or authentication infrastructure, and can be inspected and modified by the user. [^4] This makes them composable -- a discipline skill can be stacked with a design skill and a workflow skill, each addressing a different failure mode. [^3]

The skill ecosystem is developing along several axes:

- **Skill marketplaces** like LarryBrain.com (80+ skills for OpenClaw) where community-built skills are distributed freely [^4]
- **Plugin systems** like Cowork's plugin architecture where skills are bundled as zip files with trigger phrases that auto-invoke specific workflows [^2]
- **Stacking patterns** where multiple skills layer behavioral constraints -- King Mode for discipline, front-end design for aesthetics, GSD for workflow structure [^3]
- **Skills as SaaS alternatives** -- locally-run agent skills that replace hosted products, eliminating hosting, domain, authentication, and storage costs [^4]

The portability of skills means that agent capabilities are no longer locked to a single platform. A well-written skill markdown file can be loaded into Claude Code, OpenClaw, Kilo CLI, or any agent framework that supports instruction injection. [^3][^4]

**The takeaway**: Build capabilities as composable skill files, not monolithic prompts -- skills are portable, inspectable, stackable, and shareable.

---

## For Your Work

These patterns map directly to your existing infrastructure -- your 135-skill Claude Code library, Obsidian vault memory system, and multi-pipeline architecture are already the most sophisticated implementation of "harness over model" documented in these transcripts. The gaps are in content distribution, mobile-triggered workflows, and campaign-level feedback loops.

### Applications

- **e-Bangsamoro** -- apply GSD-style phase decomposition to each portal (Parliamentary, Ministerial, Budget, Citizen) to prevent context rot during multi-portal development sessions. Your `/devwork` skill could add an explicit "map the codebase" step before jumping to frontend-first implementation [^3]
- **MoroTech / MoroAcademy** -- the Larry Loop pattern is your biggest untapped opportunity. You have products but no automated content distribution pipeline. A TikTok/Facebook Reels funnel with AI-generated content, analytics feedback, and iterative hook optimization could drive awareness without manual marketing effort [^4]
- **Skills-bucket library** -- your 135 skills are more sophisticated than anything on LarryBrain (80 skills) or Cowork's plugin marketplace. Packaging BARMM-specific skills (/bill-drafter, /csw, /legal-researcher) for distribution to other legislative bodies or government consultants is a real opportunity [^4][^2]
- **AI Employees + MCP gateway** -- your 6 AI Employees architecture already solves the planner-operator gap through skill composition rather than external middleware. But for cross-tool automation (auto-sending Slack notifications after transcriptions, scheduling meetings on shared calendars, posting to government channels), an MCP gateway like Arcade could bridge the gap without custom OAuth work -- worth evaluating when AI Employees move from personal productivity to organizational deployment [^5]
- **`/prompter` skill** -- incorporate a complexity-assessment trigger inspired by the "ultrathink" concept. Classify tasks as simple/medium/complex and adjust the depth of prompt refinement accordingly [^3]
- **`/devwork` skill** -- add vertical slice planning and explicit verification that checks functional outcomes, not just compilation. "Can the user sign in? Does state persist?" [^3]
- **Dispatch workflows** -- build a "project pulse" skill that checks GitHub activity across your 9+ repos and surfaces what needs attention, triggered from your phone [^2]
- **Desktop automation** -- test computer use for Apple Calendar integration and "screenshot to vault note" passive knowledge capture via iMessage [^1]

### Priority Actions

1. **This week**: Enable computer use on your Mac and test Apple Calendar integration -- verify it can read your schedule and surface conflicts for `/context` awareness [^1]
2. **This week**: Add a "map the codebase" phase to `/devwork` before frontend-first implementation starts, inspired by GSD's anti-context-rot structure [^3]
3. **This month**: Create a `/content-loop` skill adapting the Larry Loop pattern for MoroTech content -- TikTok/Facebook Reels with hook testing, analytics feedback, and iterative optimization [^4]
4. **This month**: Build a "project pulse" Dispatch skill that sweeps GitHub activity across your repos and surfaces stale PRs, failing CI, or blocked issues [^2]
5. **This quarter**: Evaluate packaging your BARMM legislative skills (/bill-drafter, /resolution-drafter, /legislative-briefer, /csw) as a distributable toolkit for other BTA staff or legislative consultants [^4][^2]
6. **This quarter**: Assess whether an MCP gateway (Arcade or similar) makes sense for organizational-level AI Employee deployment -- map which BARMM workflows need Gmail, Calendar, or Slack integration and whether managed OAuth justifies the dependency [^5]

---

## References

[^1]: Lipsky, Paul J. "Claude Now Controls Your Entire Computer... It's WILD."
      *Paul J Lipsky*, 8:52. YouTube, March 2026.
      https://youtube.com/watch?v=dwYfNQzHQuY

[^2]: Mesarich, Brock. "5 Insane Claude Cowork Dispatch Use Cases (Steal Them)."
      *Brock Mesarich | AI for Non Techies*, 23:53. YouTube, March 2026.
      https://youtube.com/watch?v=mnsDx7HDwls

[^3]: AICodeKing. "GLM-5.1 MYTHOS: This CRAZY GLM-5.1 Setup is INSANITY!"
      *AICodeKing*, 13:21. YouTube, March 2026.
      https://youtube.com/watch?v=adRh-xeijgk

[^4]: Isenberg, Greg. "I gave OpenClaw one job: go viral (it worked?)."
      *Greg Isenberg*, 43:20. YouTube, March 2026.
      https://youtube.com/watch?v=OV5eK91YY68

[^5]: WorldofAI. "Turn Antigravity Into AN AI Autonomous Engineering Team!"
      *WorldofAI*, 14:55. YouTube, March 2026.
      https://youtube.com/watch?v=yuaBPLNdNSU
