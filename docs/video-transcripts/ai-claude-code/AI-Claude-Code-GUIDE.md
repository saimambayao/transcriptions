# Claude Code

Most developers treat Claude Code as an autocomplete engine -- type a prompt, get code, paste it in. But the practitioners who have shipped thousands of commits through AI agents have converged on a different model entirely. They treat Claude Code as a team of engineers who happen to have no memory, infinite patience, and the ability to be cloned.

This guide synthesizes patterns from 20 practitioner-level video analyses covering skill engineering, persistent memory architecture, research offloading, autonomous optimization, agent coordination, computer use, and the reliability engineering required to move from demo to production. The core thesis: the bottleneck is no longer the model's capability -- it is the quality of the systems wrapped around it.

---

## The Five-Skill Workflow: From Vague Idea to Shipped Feature

The most common failure mode in AI-assisted development is premature implementation. A developer types a rough idea, the model races to produce code, and the result technically works but solves the wrong problem. The practitioners who avoid this trap follow a structured five-phase workflow that mirrors decades of software engineering discipline.

> **Key insight**: Skills do not need to be long -- a three-sentence skill that forces the right conversation at the right moment outperforms a page of detailed instructions. [^1]

The workflow begins with **discovery** (`/grill-me`), where the agent interviews the developer relentlessly about every aspect of the plan, walking down each branch of a "design tree" inspired by Frederick P. Brooks' *The Design of Design*. Sessions routinely produce 30-50 probing questions over 30-45 minutes, surfacing assumptions the developer did not know they held. [^1]

Discovery feeds into **destination documentation** (`/write-a-prd`), which converts the shared understanding into a Product Requirements Document filed as a GitHub issue. Implementation decisions are deliberately kept non-prescriptive -- the PRD describes where to arrive, not how to get there. [^1] The PRD then breaks down into **vertical slices** (`/prd-to-issues`), each a thin tracer bullet through every integration layer rather than a horizontal task by technology. The principle is to flush out unknown unknowns at integration boundaries first. [^1][^2]

Implementation uses **test-driven development** (`/tdd`), forcing a red-green-refactor loop: one failing test, minimum code to pass, refactor. The structural requirement that matters most for AI-assisted codebases is "few large modules with thin interfaces" -- this makes codebases navigable for agents that lack the mental model a human developer carries between sessions. [^1] Finally, **architecture review** (`/improve-codebase-architecture`) spawns parallel sub-agents proposing radically different interface designs, surfacing structural decay before it compounds. [^1]

**The takeaway**: Treat AI development like team management -- invest time in requirements and architecture, not in writing code.

## Persistent Memory: Obsidian as the Knowledge Layer

AI agents lose their memory every session. This is not a flaw to work around -- it is an architectural constraint to design for. The solution practitioners have converged on is Obsidian: a free, local, markdown-based note system that Claude Code can natively read, write, and search.

> **Key insight**: The quality of information the agent has entirely determines what it can do -- managing the vault is the highest-leverage activity in an AI-augmented workflow. [^4]

The relationship between Obsidian and Claude Code is symbiotic. Obsidian gives the developer visual insight into how notes, projects, and ideas connect through graph views and backlinks. Claude Code automates the tedious work of creating properly formatted, interlinked markdown files -- no manual double-bracket linking required. And the organized file hierarchy improves Claude Code's retrieval performance, creating a virtuous cycle that compounds over months. [^3][^5]

The most sophisticated implementations go beyond storage into **thinking tools**. Custom commands like `/ghost` (answer questions in the developer's voice, built from vault writing samples), `/drift` (compare stated intentions against actual behavior over 30-60 days), `/emerge` (surface ideas the vault implies but never states), and `/challenge` (pressure-test current beliefs using vault history and counter-evidence) transform the vault from a filing cabinet into a cognitive partner. [^4]

Practical vault architecture follows a clear pattern:

- **Context files** per project -- team members, recent hypotheses, how the developer works -- loaded via a `/context` command at session start [^4]
- **Session notes** written after every coding session documenting decisions, files changed, and next steps [^6][^7]
- **Daily notes** capturing accomplishments across all roles and projects [^6][^7]
- **Ubiquitous language files** maintaining shared glossaries (inspired by Domain-Driven Design) so agents and developers use identical terminology [^2]

For multi-agent scenarios, all sub-agents reading from the same vault ensures consistent component patterns, authentication approaches, and API conventions -- preventing the drift that occurs when independent agents make incompatible architectural decisions. [^7]

**The takeaway**: The vault is not a nice-to-have note system -- it is the persistent memory layer that makes every other pattern in this guide possible.

## The CLAUDE.md Paradox: Less Context, Better Results

A counterintuitive finding from ETH Zurich research challenges the conventional wisdom that more project documentation improves agent performance. Across multiple agents and benchmarks, context files like `claude.md` reduced task success rates compared to providing no repository context at all, while increasing inference costs by over 20%. [^14]

> **Key insight**: Modern coding agents are effective enough to understand codebases through traversal -- instructions that describe what the agent can already discover are not just redundant, they are actively harmful. [^14]

The mechanism is context pollution. When a `claude.md` file contains conventions about indentation, test frameworks, and architectural patterns, 90% of that content has nothing to do with the current task. The agent reads it anyway, searches more files to comply, writes more files to satisfy conventions, and ultimately takes more steps -- not fewer -- to complete the work. [^14]

The exception is illuminating. When researchers removed all documentation from a repository, LLM-generated context files improved performance by 2.7%. The condition: `claude.md` was the only source of documentation in the entire codebase. [^14] This maps precisely to **personal assistant projects** -- an Obsidian vault of thousands of markdown files with no code architecture, no readme, no formal documentation, but rich personal conventions about routing, formatting, and interaction patterns. [^3][^14]

The practical recommendation follows directly:

- **Coding projects**: strip `claude.md` to only domain-specific facts the agent genuinely cannot discover from source code (governance terminology, multi-tenant RBAC rules, deployment constraints). Move everything else to skills and hooks. [^14]
- **Documentation projects**: keep rich `claude.md` files -- these are the textbook exception where context files add genuine value. [^14]
- **Test the boundary**: for every instruction, ask "does this need to be in every single prompt?" If the answer is no, it belongs in a skill invoked on demand, not a global context file. [^14]

**The takeaway**: The best `claude.md` file is the shortest one that still contains what the agent cannot figure out alone.

## CLI Tools Over MCP: The Token Efficiency Play

The Claude Code ecosystem is shifting from MCP (Model Context Protocol) integrations to CLI tools. The reason is measurable: a Playwright CLI benchmark showed the same task completing with 90,000 fewer tokens than the equivalent MCP approach. [^8]

> **Key insight**: CLI tools live in the terminal where Claude Code lives -- no overhead, straight connection, fewer tokens, and the agent already knows how to use most of them. [^8]

The most powerful pattern is the **CLI + Skill combo**. A CLI tool provides the capability (NotebookLM-PI for research, Stripe CLI for payments, FFmpeg for multimedia, GWS for Google Workspace); a companion skill teaches Claude Code how to use it in the specific way the developer needs. [^8] The meta-tool "CLI Anything" takes this further -- point it at any open-source project and it generates a CLI tool for that program, which Claude Code can then learn through a skill. [^8]

Context monitoring reveals why token efficiency matters. A terminal status line showing real-time context percentage, token counts, and model information lets developers see exactly when their context window is filling up. Common culprits for high baseline consumption include system prompts (~20k tokens), redundant MCP tool definitions, and oversized `claude.md` files. One optimization pass -- removing 4 redundant plugins and dropping from 13 to 9 MCP servers -- saved 8-12k tokens per session. [^9]

**The takeaway**: Every token saved on infrastructure is a token available for the actual work -- and the savings compound across every session.

## NotebookLM: Free Research on Someone Else's Tokens

NotebookLM occupies a unique position in the AI tool landscape: it excels when three conditions are true. The developer already knows which documents contain the answers. Those sources are in different formats (PDFs, spreadsheets, slides, audio, video). And the AI must stick to what is in the documents without hallucination. [^10]

> **Key insight**: Research in NotebookLM, publish through Claude -- neither tool is complete alone, but the combination produces work that would take a junior analyst two days. [^11]

The practical value is token offloading. Heavy analysis runs on Google's servers at zero token cost, with synthesized results brought back to Claude Code for creative and analytical work. [^12] The reports tool generates finished briefing documents from raw sources in minutes. The mind map tool lets developers cherry-pick which topics in a dense document are worth deep examination before reading a single page -- with interactive nodes that open focused, source-grounded chats on any subtopic. [^10]

Four workflows define the NotebookLM-Claude integration: [^11]

- **Data table to interactive visualization** -- extract structured data from sources, export to Sheets, have Claude generate embeddable HTML dashboards
- **Report to social media content suite** -- NotebookLM generates research-backed reports, Claude transforms them into platform-specific posts (LinkedIn, X threads, newsletters)
- **Knowledge base to AI persona** -- load authoritative sources into NotebookLM, synthesize via deep research, feed the synthesis into Claude skill creation for a grounded domain expert
- **Claude as research strategist, NotebookLM as executor** -- Claude architects a structured research brief with specific sub-questions and exclusions, NotebookLM executes with sharper focus

**The takeaway**: Use NotebookLM for accuracy and Claude for creativity -- respecting the boundary between grounded research and generative work.

## Auto-Research: Let Skills Improve Themselves

Manual prompt engineering hits a ceiling. The alternative is auto-research: define an objective metric, a measurement tool, and a variable to change, then let the system iterate autonomously. [^13]

> **Key insight**: All AI outputs are distributions of data -- running a skill once tells you nothing; running it many times with binary evaluations reveals its true reliability. [^13]

The methodology draws from Andrej Karpathy's auto-research framework, originally designed for optimizing nanoGPT training but applicable to any process with a measurable outcome. [^15] Karpathy describes being in a state of "AI psychosis" -- a perpetual urgency to maximize token throughput, where every failure feels like a skill issue rather than a capability limitation. The deeper interest is recursive self-improvement: LLMs improving LLMs, which is what all frontier labs are pursuing. [^15]

For skill optimization, the three ingredients are: [^13]

1. **Objective metric** -- eval pass rate, not vibes. Binary yes/no criteria per evaluation point, not Likert scales that compound variability.
2. **Measurement tool** -- an agent-written test suite that runs evaluations in sequence, requiring no human in the loop.
3. **Variable to change** -- the skill's markdown prompt itself. Every 2 minutes: generate outputs, evaluate against criteria, score, mutate the prompt, keep the winner.

Eval design matters more than loop execution. The critical warning: do not be too stringent. Overly concrete constraints (exact word counts, specific formatting requirements) cause the model to game the evaluation rather than improve quality -- like a student who gets 100% on a test without understanding the material. Test substance, not surface compliance. [^13]

The research data itself -- every attempted prompt mutation and its score -- becomes a persistent asset. When the next model generation drops, feed it the optimization log and continue from where the previous model left off. [^13]

**The takeaway**: The cost of optimizing a critical skill (~$10 for 50 test runs) is trivially small compared to the cost of deploying an unreliable one.

## Skill Engineering: Anthropic's Internal Strategy

Anthropic's own engineering teams, having built hundreds of production skills across the organization, distilled their findings into a set of principles that reframe how skills should be designed. The central insight is distributional: without a skill, Claude produces the statistically most likely output from its training data. Skills work by steering the model to sample from different, lower-probability regions of its knowledge -- regions where better, more specific outputs exist but would never surface by default. [^20]

> **Key insight**: A bad skill restates what Claude already does well, reinforcing the default distribution. A good skill encodes lived experience, domain expertise, or novel approaches that push Claude into less common but higher-quality regions of its latent space. [^20]

This explains the "purple gradient" problem in AI-generated design: distributional convergence in training data blends all design examples into safe, generic patterns. A thousand users asking "build me a landing page" without skills get nearly identical outputs. Skills containing brand guidelines, design preferences, and specific examples produce distinct results because they activate different parts of the model's knowledge. [^20]

Anthropic identifies the **gotchas section** as the single most valuable component of any skill -- more valuable than process instructions or output templates. Gotchas encode the implicit knowledge that experienced practitioners carry: "never promise specific timelines in support replies," "prorations round down, not nearest cent," "test mode keys behave differently from production keys." Most users create a skill, notice one mistake, and never iterate. The practitioners who maintain a growing gotchas section create a compounding knowledge base that applies consistently across every invocation. [^20]

Three additional engineering principles complete the picture:

- **Goal-first, not constraint-first** -- rigid step-by-step instructions ("write 3 behavioral questions, 3 technical, 1 culture fit") collapse the output distribution into a narrow path. Goal-oriented framing ("prepare interview questions that test what actually predicts success here") preserves Claude's ability to adapt to context. When outputs are bad, add gotchas rather than more constraints. [^20]
- **Descriptions as routing logic** -- skill descriptions should contain semantic trigger phrases ("babysit, watch CI, make sure this lands"), not marketing copy ("a comprehensive deployment lifecycle monitoring tool"). Claude matches user queries to skill descriptions semantically. [^20]
- **Skills as operational packages** -- mature skills contain scripts (pre-built API functions that avoid re-discovering integrations each run), security hooks (restricting the skill to only its expected file paths and network access), and persistent state (log files or databases that maintain continuity between runs). The best skills fall cleanly into one category and combine with complementary skills rather than trying to span multiple responsibilities. [^20]

**The takeaway**: Skills are not instruction documents -- they are operational packages that steer Claude's output distribution, accumulate domain knowledge through gotchas, and mature into self-contained mini-applications with scripts, hooks, and state.

## From Skills to Harnesses: The Reliability Threshold

Skills alone will never reach business-scale reliability. Karpathy's "march of nines" quantifies this: at 90% reliability per step, a 10-step workflow running 10 times daily produces over 6 failures every day. At 99% per step, roughly one failure per day. At 99.9%, one failure every 10 days. [^16]

> **Key insight**: A harness is the software layer that wraps around an AI model, putting it on deterministic rails -- instead of hoping the AI does the right thing, the harness guarantees it by codifying the process in code. [^16]

Stripe demonstrated this at scale with "Minions" -- a scaffold around Claude Code that automatically validates all generated code changes against a subset of their 3 million tests. They did not prompt the AI to run tests; they baked testing into the process. Result: 1,300 pull requests merged per week. [^16]

The relationship between skills and harnesses is complementary. Skills expand capabilities and guide the AI as a co-pilot. Harnesses ensure that something happens every single time, reliably at scale. Skills remain useful even inside harnesses -- they codify what must happen, while the harness gates and validates at each stage. [^16]

**The takeaway**: If the output reaches production, parliament, or paying users, wrap the skill in a harness with validation gates between every stage.

## Agent Teams: Coordinated Parallel Development

Agent teams represent a step beyond simple sub-agents. Where sub-agents work independently and return results, agent teams share a task list and communicate directly with each other -- including sending work back when quality checks fail. [^17]

> **Key insight**: The feedback loop is what makes agent teams valuable -- a QA agent that rejects work and routes it back to the developer agent for another pass creates a self-correcting cycle that sub-agents cannot replicate. [^17]

Effective agent team prompting follows a pattern: establish a goal (agents wake up with no context), define team composition (3-5 agents maximum for cost efficiency), assign each agent specific file ownership to prevent overwriting, specify inter-agent communication protocols, and define output deliverables. [^17]

Three rules govern agent team success: [^17]

1. **Own territory** -- each agent edits only their assigned files and directories
2. **Direct messaging** -- agents communicate without routing through the main session as intermediary
3. **Parallel work** -- agents work simultaneously, not in sequential handoff chains

Agent teams are expensive (roughly 3x token cost per agent) and should be reserved for complex builds that benefit from parallel work and inter-agent communication. Sequential workflows, simple tasks, and document pipelines remain better served by regular sub-agents or skills. [^17]

**The takeaway**: Use agent teams for complex parallel implementation where feedback loops between specialists (frontend, backend, QA) add genuine value -- not as a default for every task.

## Scheduling and Loops: The Persistence Spectrum

Claude Code offers multiple persistence mechanisms, each with distinct tradeoffs. The `/loop` command runs recurring tasks within a session (now extended to **7-day maximum**, up from the previous 3-day limit), enabling longer-running optimization workflows without interruption. [^18] Claude Code Desktop's `/schedule` is more powerful -- the new cloud-based `/schedule` command creates recurring jobs that run **even after the laptop is closed**, turning Claude into a persistent background worker. [^18] Anthropic teams already use it internally for auto-resolving CI failures, pushing documentation updates, and handling repetitive dev tasks. One notable use case: a scheduled job that maintains a **twin Go library** automatically synced with an active Python library. [^18] GitHub Actions provides another truly persistent option, running on GitHub's infrastructure without a local machine, but is scoped to GitHub tasks only. [^3b]

**The takeaway**: Match the tool to the persistence requirement -- `/loop` for session tasks (up to 7 days), `/schedule` for daily routines that survive laptop closure, GitHub Actions for CI/CD that must never miss.

## Computer Use: From Tool to Operator

Claude can now control a Mac's mouse, keyboard, and screen -- opening files, browsing the web, and interacting with developer tools automatically. The system follows a precision hierarchy: it always tries the most precise tool first (MCP integrations like Slack or Google Calendar), falling back to computer use only when integrations are unavailable. [^18]

> **Key insight**: Computer use transforms Claude from a tool that generates outputs into an operator that can execute within existing environments -- including apps that have no API or integration. [^18]

Safety is built into the architecture. Claude monitors for prompt injection attacks, scans for suspicious behaviors, and always requests permission before accessing new apps or taking sensitive actions. The feature is currently in research preview for Claude Pro users on Mac. [^18]

A critical expectation to set: computer use is often **slower than doing the task manually**. The agent must infer screen state visually, navigate unfamiliar application interfaces through trial and error, and course-correct when it makes mistakes -- a typo in a text field, a misclick on a menu item, or selecting the wrong element. The self-correction capability works (Claude can detect its own errors by re-reading the screen and fix them), but each correction cycle adds latency. [^19] For single, well-defined tasks like adding a calendar event, the experience is smooth. For multi-step workflows chaining multiple applications -- adding items to a reminders list, then navigating to an e-commerce site, searching for products, and adding them to a cart -- the cumulative inference time and error-correction loops make the process significantly slower than a human performing the same steps. [^19]

When combined with Dispatch (which allows remote task assignment from a phone), computer use enables a powerful pattern: assign Claude a multi-app workflow from anywhere, and it navigates the desktop autonomously -- pulling analytics from dashboards, organizing files, or preparing reports. [^18][^19]

**The takeaway**: Computer use is the fallback layer for apps without APIs -- powerful but slower than direct integrations, and best reserved for tasks that cannot be accomplished through MCP connectors. Expect early-days performance: functional but not fast.

## Effort Levels and DOM Selection: Precision Controls

Two smaller updates significantly improve daily workflow precision. **Effort levels** can now be set directly inside skills and slash commands, controlling how deeply Claude reasons before responding. Low effort for quick routing tasks, high effort for complex coding, debugging, or planning -- and the setting overrides session defaults on a per-task basis. [^18]

**DOM element selection** in Claude Code Desktop allows developers to click directly on a UI element rather than describing it in words. Claude receives the HTML tag, classes, key styles, surrounding DOM context, and a cropped screenshot. For React apps, it additionally accesses the source file, component name, and props. [^18]

**The takeaway**: Fine-grained control over reasoning depth and visual element targeting eliminate two categories of friction that accumulate across hundreds of daily interactions.

---

## For Your Work

The patterns above map directly to your multi-role operation spanning OOBC consulting, 9-platform development, legislative drafting, and community leadership. This section translates universal patterns into specific actions for your projects and workflows.

### Applications

- **e-Bangsamoro** -- agent teams with 3 specialists (React frontend, Django backend, QA) for complex module builds like parliamentary voting or MANA assessment dashboards; sub-agents for simpler parallel work [^17][^2]
- **/bill-drafter** -- wrap in a harness modeled on the contract review demo: text extraction from reference legislation, bill classification, human-in-the-loop scope clarification, playbook loading from ~/Vault/bangsamoro/ (BOL provisions, existing BAAs, BDP chapters), provision extraction, risk analysis per provision using sub-agents with isolated context, amendment generation, formatted output [^16]
- **Obsidian vault** -- build `/context` as a universal session startup loading OOBC consulting priorities, active platform sprint status, pending bill drafts, and SEED Initiative milestones in one command; add `/drift` to compare stated development priorities against actual time allocation in daily notes [^4][^7]
- **CLAUDE.md audit** -- strip architecture descriptions from your 9 platform CLAUDE.md files that Claude infers through traversal; keep only Bangsamoro-specific naming conventions, multi-tenant RBAC rules, Railway deployment constraints, and domain facts Claude cannot discover from source code [^14]
- **/auto-research** -- run the three-ingredient loop on /bill-drafter with 4 binary eval criteria (correct BOL references, BTA parliamentary formatting, correct official titles, proper implementing rules); ~$10 for 50 test runs [^13]
- **NotebookLM** -- restructure /notebooklm skill around four named modes: data-to-visualization, report-to-social-content, knowledge-base-to-skill-creation, research-brief-to-deep-research [^10][^11]
- **MoroMarket/e-Negosyo** -- integrate Stripe CLI for cooperative product setup, replacing manual UI navigation across dozens of cooperative partners [^8]
- **SEED Initiative/Tarbiyyah-MS** -- structure cooperative and madrasah training curricula as agent-readable skill files that adapt delivery to each learner's context, following Karpathy's vision of "curricula as instructions to agents rather than lectures to humans" [^15]
- **/schedule for BARMM monitoring** -- create a cloud-based scheduled job that scans for new BAAs, BTA agenda items, and resolution filings daily, persisting even when your laptop is closed; replaces the desktop-must-be-open constraint from Cowork scheduled tasks [^18]
- **Effort levels per skill** -- set effort directly in skill frontmatter: low for /vault-update and /file-organizer, medium for /fact-checker, high for /bill-drafter, /policy-recommendation, and /legislative-briefer. Fine-tune reasoning depth without session-level toggling [^18]
- **DOM selection for e-Bangsamoro frontend** -- click directly on React components in the browser during /frontend debugging instead of describing them; Claude receives component name, props, and source file path for React 19 components [^18]
- **Gotchas audit** -- review your top 10 most-used skills (/bill-drafter, /legislative-briefer, /fact-checker, /bangsamoro, /youtube-transcriber, /devwork, /frontend, /tdd, /prompter, /session-summary) and add explicit gotchas sections encoding hard-won lessons from actual usage; Anthropic identifies gotchas as the single most valuable skill component [^20]
- **Skill descriptions as routing** -- update skill descriptions to contain semantic trigger phrases rather than marketing copy; /bangsamoro should include "BARMM, BTA, BOL, autonomy, peace process, Moro" and /fact-checker should include "verify, check names, validate, are these correct" [^20]
- **/bill-drafter gotchas** -- encode ECCD bill review lessons: "never use 'and/or' in legislative text", "always check BAA-49 for existing provisions before creating new structures", "MFBM not DBM, MOLE not DOLE in BARMM context", "always add specific repealing clauses naming replaced bodies" [^20]
- **/fact-checker scripts** -- pre-build verification scripts for the most common patterns: name lookup against officials reference, BAA reference validation against the BAA index, RA number verification against local PDF sources; eliminates re-discovery of file paths each invocation [^20]

### Priority Actions

1. **This week**: enable agent teams in e-Bangsamoro's `.claude/settings.local.json`, run a test build with 3 agents (frontend, backend, QA) on a medium-complexity module
2. **This week**: audit your 9 platform CLAUDE.md files -- remove file structure and architecture descriptions inferrable from code traversal, keep only domain-specific conventions
3. **This month**: run /auto-research on /bill-drafter with 4 binary eval criteria against 10 test prompts; store the optimization log in ~/Vault/Claude-Skills/bill-drafter/optimization-log.md
4. **This month**: build `/context` as a universal session startup command that loads all five context domains (OOBC priorities, platform sprint status, pending bills, SEED milestones, daily note) in one shot
5. **This month**: set up a `/schedule` cloud-based job for daily BARMM legislative monitoring -- scanning for new BAAs and resolutions even when laptop is closed [^18]
6. **This month**: add effort level frontmatter to your top 20 most-used skills -- categorize each as low/medium/high based on reasoning complexity [^18]
7. **This quarter**: design a harness wrapper for /bill-drafter with validation gates between each drafting phase -- modeled on the 8-phase contract review architecture, with BOL cross-referencing as the validation loop
8. **This quarter**: restructure /notebooklm into four named modes and integrate with /legislative-briefer so that policy research flows through NotebookLM before Claude drafts the briefing
9. **This week**: audit your top 10 skills for gotchas sections -- add explicit "things Claude gets wrong" from actual usage experience to each; prioritize /bill-drafter (ECCD review lessons), /fact-checker (common verification failures), and /youtube-transcriber (auto-caption noise patterns) [^20]
10. **This month**: update skill descriptions across your 124-skill library to use semantic trigger phrases instead of marketing descriptions -- start with the 20 most-used skills [^20]

---

## Related Knowledge Areas

- [[knowledge-areas/ai-agents/claude-code/index|AI Agents: Claude Code Knowledge Area]] — cross-source living synthesis

---

## References

[^1]: Pocock, Matt. "5 Claude Code Skills I Use Every Single Day."
      *Matt Pocock*, 16:42. YouTube, March 2026.
      https://youtube.com/watch?v=EJyuu6zlQCg

[^2]: Pocock, Matt. "Building a REAL Feature with Claude Code: Every Step Explained."
      *Matt Pocock*, 44:16. YouTube, March 2026.
      https://youtube.com/watch?v=hX7yG1KVYhI

[^3]: Chase. "Claude Code + Obsidian = UNSTOPPABLE."
      *Chase AI*, 14:40. YouTube, March 2026.
      https://youtube.com/watch?v=eRr2rTKriDM

[^3b]: Chase. "Claude Code Just Got a MASSIVE Upgrade (Agent Loops)."
      *Chase AI*, 10:19. YouTube, March 2026.
      https://youtube.com/watch?v=lf2lcE4YwgI

[^4]: Isenberg, Greg, and Vin. "How I Use Obsidian + Claude Code to Run My Life."
      *Greg Isenberg*, 58:57. YouTube, March 2026.
      https://youtube.com/watch?v=6MBq1paspVU

[^5]: Kashef, Mark. "Claude Code Turned Obsidian Into My Dream Second Brain."
      *Mark Kashef*, 14:00. YouTube, March 2026.
      https://youtube.com/watch?v=2kbINqpluM0

[^6]: WorldofAI. "Claude Code + Obsidian = UNLIMITED Memory! Solves Claude's Memory Problem!"
      *WorldofAI*, 13:00. YouTube, March 2026.
      https://youtube.com/watch?v=srqWFT_TUec

[^7]: Chase. "Claude Code + NotebookLM + Obsidian = GOD MODE."
      *Chase AI*, 14:34. YouTube, March 2026.
      https://youtube.com/watch?v=kU3qYQ7ACMA

[^8]: Chase. "10 CLI Tools That Make Claude Code UNSTOPPABLE."
      *Chase AI*, 14:03. YouTube, March 2026.
      https://youtube.com/watch?v=uULvhQrKB_c

[^9]: Eric. "Your Claude Code Terminal Could Look Like This."
      *Eric Tech*, 16:08. YouTube, March 2026.
      https://youtube.com/watch?v=Jvl_MOBPRXI

[^10]: Su, Jeff. "NotebookLM Changed Completely: Here's What Matters (in 2026)."
      *Jeff Su*, 20:30. YouTube, March 2026.
      https://youtube.com/watch?v=_uXnyhrqmsU

[^11]: Universe of AI. "NotebookLM Just Got a MASSIVE Update with Claude!"
      *Universe of AI*, 13:46. YouTube, March 2026.
      https://youtube.com/watch?v=gKc1Cgaocuw

[^12]: Chase. "Claude Code + NotebookLM + Obsidian = GOD MODE."
      *Chase AI*, 14:34. YouTube, March 2026.
      https://youtube.com/watch?v=kU3qYQ7ACMA

[^13]: Saraev, Nick. "Stop Fixing Your Claude Skills. Autoresearch Does It For You."
      *Nick Saraev*, 16:32. YouTube, March 2026.
      https://youtube.com/watch?v=qKU-e0x2EmE

[^14]: Chase. "Claude.md is RUINING Claude Code (w/ One Exception)."
      *Chase AI*, 11:51. YouTube, March 2026.
      https://youtube.com/watch?v=V3xDTx2XwGg

[^15]: Karpathy, Andrej. "The End of Coding: Andrej Karpathy on Agents, AutoResearch, and the Loopy Era of AI."
      *No Priors: AI, Machine Learning, Tech, & Startups*, 66:31. YouTube, March 2026.
      https://youtube.com/watch?v=kwSVtQ7dziU

[^16]: The AI Automators. "Andrej Karpathy's Math Proves Agent Skills Will Fail. Here's What to Build Instead."
      *The AI Automators*, 19:26. YouTube, March 2026.
      https://youtube.com/watch?v=I2K81s0OQto

[^17]: Herk, Nate. "Master 95% of Claude Code Agent Teams in 16 Mins."
      *Nate Herk | AI Automation*, 16:29. YouTube, March 2026.
      https://youtube.com/watch?v=vDVSGVpB2vc

[^18]: WorldofAI. "Claude Code MASSIVE Update! Claude Code OS, Computer Use, /Schedule, & More!"
      *WorldofAI*, 10:37. YouTube, March 2026.
      https://youtube.com/watch?v=hWDXS35B15A

[^19]: Developers Digest. "Claude NEW Computer Use in 6 Minutes."
      *Developers Digest*, 6:14. YouTube, March 2026.
      https://youtube.com/watch?v=ZUBJqLGKoZI

[^20]: Amjad, Ray. "Anthropic Just Dropped Their Internal Skills Strategy."
      *Ray Amjad*, 18:43. YouTube, March 2026.
      https://youtube.com/watch?v=7PnF8qctDi8
