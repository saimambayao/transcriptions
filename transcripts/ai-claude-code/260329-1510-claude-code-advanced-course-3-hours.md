# CLAUDE CODE ADVANCED COURSE — 3 HOURS

**Channel**: Nick Saraev
**Duration**: 198:23
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=UPtmKh1vMN8
**Transcribed**: 2026-03-29 15:10

---

## Organized Notes

**Nick Saraev** is a high-performing internet entrepreneur who uses Claude Code and AI agents daily to generate over $4 million/year in profit. He teaches ~2,000 people how to use Claude Code. This course assumes foundational Claude Code experience and covers system prompts, agent harnesses, parallelization, auto research, browser automation, security, and the future of AI-powered work.

---

**CLAUDE.md as Knowledge Infrastructure**

- A CLAUDE.md serves **four distinct functions**: knowledge compression, user preferences/conventions, declaration of capabilities, and a log of failures and successes
- **Knowledge compression**: instead of Claude reading every file in your workspace, the CLAUDE.md compresses it into a succinct summary — saves tokens and time
- **Preferences and conventions**: advanced users have preferences that aren't natively baked into Claude Code (programming conventions, communication styles, reasoning strategies)
- **Declaration of capabilities**: explicitly tell Claude what it can do — call APIs, act autonomously with browsers, build and execute plans — otherwise Claude will say "I don't have a built-in way to do this"
- **Log of failures and successes**: carves out chunks of the theoretical solution space, telling future Claude instances what **not** to try — eliminates ~80% of wasted effort
- Token compression ratio matters: the CLAUDE.md description of app.jsx was **45x shorter** than reading the actual file (~22 tokens vs ~1,100 tokens)
- **Token length scales inversely with output quality** — shorter context windows yield better results

**Global vs. Local CLAUDE.md Strategy**

- **Global** (`~/.claude/CLAUDE.md`): high-level reasoning strategies, personal profile context, preferences, token conservation strategies — loaded on every session across all workspaces
- **Local** (`.claude/CLAUDE.md` in project): workspace-specific knowledge compression, project description, file locations, local API docs, project-specific capabilities
- Global should contain: context about you (goals, revenue, reasoning strategies, communication style), high-level interaction rules, token conservation strategies
- Local should contain: project description via `/init`, where everything is, low-level preferences, specific API docs

**The CLAUDE.md Update Loop**

- **Local loop**: Plan feature → Implement → Compile learnings from failures/successes → Update local CLAUDE.md → Repeat
  - Each iteration shaves ~10% off development time (1x → 0.9x → 0.8x...)
- **Global loop**: After hundreds of local runs, use `/insights` to compile patterns across all sessions → Manually review (critical — human in the loop) → Add high-ROI bullet points to global CLAUDE.md
- The two loops form an **infinity sign** — mostly in the local loop, periodically dropping to the global loop
- **Meta-prompt technique**: add a line in CLAUDE.md that says "when you make a mistake, update the CLAUDE.md with a running log of things not to try next time" — creates a "lab notes" section automatically
- After `/insights`, ask Claude to **distill into high-information-density snippets** for the global CLAUDE.md — not the raw report
- **Human review is essential** at the global level: compound probabilities (0.9^3 = 73%) mean multi-agent steps without human review degrade accuracy

*Quotable Quotes:*

> "What your CLAUDE.md does is it basically just compresses all of that down into a highly succinct summary of what the heck is going on in your folder." [03:00]

> "These cloud tokens ain't free, man. Anthropic increased the price pretty aggressively, especially recently when they realized 99% of the world is now operating using their infra." [21:34]

> "Asking questions like 'how could you have arrived at those conclusions and done everything I just asked you to do faster and for fewer tokens' is pretty powerful." [25:25]

---

**Agent Harnesses: What They Are and Why They Matter**

- An **agent harness** is everything that wraps around the LLM that is not the LLM itself — Claude Code is a harness around the Claude model
- The harness includes: the system prompt, hooks, available tools, parameters controlling memory compaction, message limits, token limits
- Without a harness, an LLM is just text in/text out — the harness turns it into something that controls your computer
- **Analogy**: gunpowder is the core tech (the LLM); the cannon vs. the rifle barrel (the harness) determines how far and accurately the bullet goes
- Anthropic's November 2025 blog post **"Effective Harnesses for Long-Running Agents"** was the kickoff of Claude Code's superiority
- Other harnesses exist: **Droid** (Factory AI), **PI** (open-source, model-agnostic), **Crew AI** — all different approaches to the same problem
- The harness impacts: **security** (permission modes), **memory**, **tool access**, and **performance**
- Claude Code is the dominant harness but understanding the concept helps appreciate what makes it effective

---

**Parallelization: Why and How**

- **Why parallelize**: autonomous agents take a long time (up to 15+ minutes per task); sitting idle is unproductive
- Serial execution of 4 independent 5-minute tasks = 20 minutes; parallelized = ~12 minutes (**40% time savings**)
- **Stochastic nature** of LLMs: running Claude 5 times on the same query yields 5 different responses — parallelization captures **2.5x more unique solutions**
- **Context degradation**: model performance drops as context grows; sub-agents maintain fresh, short context windows in the "zone of good"

**Three Core Parallelization Patterns**

1. **Fan-Out / Fan-In (Researcher-Synthesizer)**
   - Spawn multiple research sub-agents (cheap model like Sonnet) → each investigates independently → synthesize results with a smart model (Opus)
   - Research agents stay in the "zone of good" with short context windows
   - Use **Sonnet for research** (60% cheaper than Opus, faster) and **Opus for synthesis** (better reasoning)
   - Applicable to: competitor research, API evaluation, business system design, product differentiation, pricing strategy

2. **Stochastic Consensus**
   - Spawn N agents with same/similar prompts but different "personalities" (conservative, adventurous, contrarian, first-principles)
   - Aggregate results by **mode** (frequency of each solution)
   - High-frequency solutions = consensus; low-frequency = genuine outliers
   - Example: 10 agents produced 119 raw ideas → 52 unique solutions for tomatillo sauces
   - Works like a **weighted average**: `decision = 2A + 2B + 2C + D + E + Q`

3. **Debate (Multi-Round Consensus)**
   - Extension of stochastic consensus: agents see each other's responses across **time steps**
   - Each round, agents incorporate others' ideas, eliminate weak ones, combine for new solutions
   - Produces increasingly **nuanced solutions** spanning a large search space
   - Not adversarial debate — collaborative refinement with shared visibility

**Agent Teams (Built-in Feature)**

- Claude Code's **agent teams** feature formalizes these patterns with a streamlined UX
- Team lead orchestrates, spawns analyst agents, aggregates consensus, identifies bugs and outliers
- Can combine patterns: stochastic consensus for ideation → fan-out for research → pipeline for implementation → reviewer agents for QA
- Navigate between agent threads using **Shift+Up/Down** in the terminal

*Quotable Quotes:*

> "If all I'm doing is just sitting there waiting for it to do this 15-minute task, you can imagine that my productivity is basically going to be punctuated by me just sitting around watching it." [43:05]

> "I'm basically getting 2.5 times the total number of possible answers by running things multiple times and then just averaging out and taking all the unique outputs." [48:13]

---

**Skills vs. Sub-Agents: They're the Same Thing**

- Skills and sub-agents share nearly identical properties: **specialized**, **reliable at specific tasks**, **written in markdown with tool use**
- The only real difference: sub-agents get a **completely fresh context window**; skills compress context but share the parent's window
- Both have: name, description, allowed tools, SOPs — just different ways of organizing markdown files
- **Prediction**: skills and sub-agents will converge into a single concept as the field matures
- Various organizational schemes exist (Paperclip, Company Helm, Open Goat, The System, Gas Town, Crew AI, Swarm Claude) — all are different attempts at agent hierarchy
- Most current org charts with CEO/CTO/CMO agent hierarchies are **over-engineered** and unnecessary

**Two Recommended Delegation Patterns**

1. **Parent + Researchers + QA**: Opus orchestrator → multiple Sonnet researchers (fan-out) → Opus QA agent (iterative review loop until done)
2. **Developer + QA** (simpler): smart parent builds features → spawns fresh QA agent after each feature → QA gives unbiased feedback → parent incorporates → repeat until no feedback needed
- Key principle: the **QA agent should have no context** about the project — forces unbiased review
- More layers = more compound probability degradation; keep it lean

---

**Auto Research (Karpathy's Framework)**

- Originated from **Andrej Karpathy** (co-founder OpenAI, former head of AI at Tesla) — automated his own research loop
- The loop: **Hypothesis** → **Execute change** → **Assess** → If improved, keep and repeat; if failed, revert and try different hypothesis
- Maintains a **research log** documenting all attempts, successes, and failures
- Represents the evolution: **vibe coding** (human prompts, AI writes) → **agentic engineering** (human directs agents) → **independent research** (human sets goal, agent runs autonomously)

**Three Requirements for Auto Research**

1. **A metric** to optimize (must be objective and standardized — e.g., Google Lighthouse score)
2. **A change method** to influence the metric (must be fast — ideally ~30 seconds)
3. **An assessment** to evaluate the change (must also be fast — ~30 seconds)
- Combined 60-second loop = **1,440 experiments/day**
- Even at 2% success rate with 1% improvement each = **34% improvement per day** (1.01^30)

**Real-World Applications**

- **Website performance**: Nick improved Lighthouse FCP from 646ms to 619ms; his leftclick.ai improved by 20%
- **Shopify CEO Toby Lutke** ran auto research on the entire Shopify Liquid codebase: **53% faster parse+render**, **61% fewer object allocations**
- **SaaS optimization**: frontend load speed, backend request latency
- **Business processes**: customer support prompts, cold email copy (6-10 tests/day at 500-1000 emails/test), ad creative, conversion rate optimization, landing page copy
- Set up using Karpathy's repo: `github.com/karpathy/auto-research` — clone, define program.md, run train.py

*Quotable Quotes:*

> "Auto research is basically perfect for use cases where we have a very defined goal, a very defined change method, and a very standardized assessment." [1:30:45]

> "Imagine what happens when you point this at something and go twice as fast in like 30 runs or something. That's nuts to think about." [1:47:04]

---

**Browser and Computer Automation: Three Levels**

1. **HTTP Requests** (fastest, cheapest, most fragile)
   - Claude Code's native `web_fetch` tool sends HTTP GET/POST requests
   - Great for scraping text content from websites
   - Fragile: requires exact API schema knowledge; many platforms block automated requests
   - Best for: high-volume, repetitive tasks once the format is known

2. **Browser Automation** (middle ground)
   - **Chrome DevTools MCP**: opens a real browser, clicks buttons, fills forms, takes screenshots
   - Much more general than HTTP — handles dynamic JavaScript-rendered content
   - Slower (~1 action every 5 seconds) but works on almost any website
   - **Browser Use** platform: premium option ($100 + credits) that's **99.9% undetectable** with custom fingerprinting
   - Best for: prototyping flows, social media interaction, websites with anti-automation measures

3. **Computer Automation** (most general, most expensive)
   - Literally controls mouse and keyboard via Claude Desktop's computer use
   - Can do anything a human can do on a computer — file management, cross-application tasks
   - Very slow, consumes enormous tokens (screenshots at every step)
   - Best for: tasks that span multiple applications or require desktop interaction

**Nick's Workflow**: Start with browser automation (Chrome DevTools MCP) for prototyping → If blocked, try Browser Use → Once flow is proven, reverse-engineer the HTTP API from network requests → Build custom HTTP utility for production speed

*Quotable Quotes:*

> "The cool stuff that you can do with Claude is actually just automation. Understanding the trade-off between pure HTTP requests and browser automation and full computer automation will let you control a lot of things much better." [1:59:12]

---

**Performance Fluctuations and Model Diversification**

- Claude Code is the **monoculture crop** analogy from Interstellar — incredibly productive but creates single-point-of-failure risk
- Recent outages (Opus 4.6 going down, December 2025 garbage collection issue) crashed developer productivity worldwide
- **Solution: diversify like an investment portfolio** — put 70% in Claude, spread 30% across alternatives

**Three Diversification Strategies**

1. **Conductor**: run teams of different coding agents (Claude Code + Codex) in parallel from one interface — averages out fluctuations
2. **Codex MCP Server**: install within Claude Code for when Claude models are degraded but the platform is up — `npm i -g @openai/codex`
3. **Separate agent platform**: keep Codex desktop app installed and ready; maintain a duplicated workspace with `AGENTS.md` / `GEMINI.md` alongside `CLAUDE.md`
- Sync CLAUDE.md → AGENTS.md → GEMINI.md so any platform can pick up your workspace instantly
- Current assessment: Claude Code > Codex >> Gemini (except Gemini may be better at frontend design)

---

**Workspace Organization**

- **Core structure**: `.claude/` (skills, agents), `active/` (generated files, outputs), `.env` (API keys), `CLAUDE.md`
- **Never pollute root** — always store in `active/` or subdirectories; specify output locations in skill definitions
- **Business workspace**: top-level business folder → client subfolders (each with own `.env`, `.claude/skills/`, `CLAUDE.md`)
- **Personal workspace**: same structure but organized by **domain** (health, citizenship, learning projects) instead of clients
- **Color-code workspaces** in VS Code settings to instantly identify business vs. personal folders
- Skills can reference files outside their local `.claude/skills/` — add a line in CLAUDE.md pointing to client skill locations
- **Periodic cleanup**: ask Claude to clean up loose files in `active/`, sort into logical subfolders, delete temp files
- **Project-based alternative**: `company-name/projects/` with subfolders per project — works well for SaaS businesses
- Can host everything on GitHub with daily clone/push for cloud backup

---

**Security: The 80/20 Approach**

- **Everything is hackable** — the goal is making your setup less hackable than the effort required to breach it
- Security exists on a spectrum between "raw-dog everything" accelerationists and "punch-card-only" conservatives — the answer is in between

**Five Low-Hanging Fruit Security Fixes**

1. **API keys in conversation history**: all Claude Code conversations are stored in `~/.claude/` as plaintext JSONL files — API keys pasted in chat are logged there
   - **Fix**: always store secrets in `.env` files; reference by variable name, never paste raw keys in chat
2. **Hallucinated package names**: AI models sometimes invent misspelled package names (e.g., "acorns" instead of "acorn") — attackers create malware packages with these misspellings
   - **Fix**: audit dependency lists; ask Claude to verify all packages have verified histories before installing
3. **Database row-level security (RLS)**: Supabase doesn't enable RLS by default — without it, any user can read/write/delete all data
   - **Fix**: always enable RLS; one button click prevents the vast majority of database breaches
4. **Public-facing servers**: any public URL is **constantly scanned** by bot farms looking for vulnerabilities
   - **Fix**: proper firewalls, don't store sensitive data on public agents, use authenticated channels (Telegram, etc.)
5. **Credit card data**: never store, read, or process credit card numbers through AI agents — use Stripe or similar PCI-compliant services

**Security Audit Process**

- Use a dedicated security audit prompt (separate from the dev conversation to avoid bias)
- Run the audit in a **fresh conversation** — don't let the dev agent audit its own work
- Have a third model (Codex, Gemini) implement the security fixes, then have Claude review
- Diversify across models for security just like for development — avoids inherent biases

---

**The Future of Claude Code and AI-Powered Work**

- **Decreasing human involvement**: vibe coding → agentic engineering → independent research (auto research) → fully autonomous systems
- Claude's **auto mode** is a microcosm: planning, implementation, and QA are all being internalized by the agent
- Each person will become the **CEO of their own agent fleet** — running teams of specialized agents rather than doing tasks directly

- **Software is no longer the moat**: anyone can build Netflix in 5 minutes with agents on fast mode
  - The moat shifts to **distribution, reputation, relationships, legal/compliance, and licensing**
  - SaaS subscription models face pressure — "Why pay $199 for software when I can build it for $19 in tokens and 30 minutes?"
  - **Nick is not bullish on SaaS** — the supply of software will so vastly outstrip demand that prices collapse

- **Pace of change accelerates**: AI models are now improving AI models — creates a compound growth curve
  - Intelligence graph: 1970s linear → 2010 inflection → 2020 acceleration → 2025-2026 near-vertical
  - The gap between chimpanzee, average human, and Einstein intelligence is **surprisingly small** on an absolute scale — models are crossing that gap rapidly

- **You are the 1%**: the percentage of people who understand agent harnesses is vanishingly small — this creates **asymmetric reward** potential
  - Leverage will increase: instead of 100 people doing 1 task each, 1 person will do 100 tasks
  - The future is here, just unevenly distributed (William Gibson quote)
  - Those who learn to use these tools now will "own even 0.1% of that potential future"

*Quotable Quotes:*

> "You are the 1% right now. You have an enormous capability to use models like this for just cents on the dollar to do incredibly amazing economically valuable things that would take that other group of 99% months to do what you could realistically do in a day." [3:15:24]

> "The future is here. It's just unevenly distributed." [3:16:04]

> "I think we're getting really, really close to super fast paces of change. This would have been unfathomable just three or four years ago." [3:14:09]

---

## What This Means for Your Work

Nick's approach validates and challenges your current Claude Code setup in roughly equal measure. You already operate at the level he describes as "advanced" — 135 skills, parallel agents, Obsidian vault memory, NotebookLM integration, fact-checking pipelines. But several patterns in this course reveal gaps and optimization opportunities that are directly actionable for your work.

**Your CLAUDE.md Strategy Is Already Ahead — But Missing the "Lab Notes" Pattern.** Nick's four-function framework (knowledge compression, preferences, capabilities, failure log) maps almost exactly to how your global and project CLAUDE.md files work. Your global CLAUDE.md already has user profile context, interaction rules, and the Universal Verification Framework. What you're missing is Nick's **"lab notes" meta-prompt** — a self-updating section where Claude logs what didn't work during development. For your e-Bangsamoro project, where you run multi-hour sessions building complex Django+React features, a persistent "what not to try" section in the project CLAUDE.md could eliminate repeated dead ends across sessions. The `/insights` command he demonstrates for compiling patterns from conversation history is something you should run periodically on your transcriptions workspace and e-Bangsamoro workspace to surface systematic issues.

**The Fan-Out/Fan-In Pattern Maps Directly to Your Research Pipeline.** Your `/research-pipeline` and `/deep-research` skills already use sub-agents, but Nick's explicit model-tier strategy (Sonnet for research, Opus for synthesis) could reduce your token costs significantly. When you run `/deep-research` for policy papers or legislative briefers, the research phase doesn't need Opus — Sonnet can scrape, extract, and summarize just as well. Reserve Opus for the synthesis and legal analysis steps where reasoning quality matters. This is especially relevant for your `/content-research-writer` and `/legislative-briefer` workflows where research can be 60-70% of total token spend.

**Stochastic Consensus Could Transform Your Bill Drafting.** When you draft bills using `/bill-drafter`, you're currently getting one Claude perspective. Nick's stochastic consensus pattern — spawning 5-10 agents with different framings to independently analyze the same legislative question, then synthesizing by consensus — could produce significantly more comprehensive bills. Imagine spawning agents framed as: (1) a Shari'ah compliance reviewer, (2) a gender mainstreaming analyst, (3) a fiscal impact assessor, (4) a BOL consistency checker, (5) a comparative legislation researcher. The outlier ideas (low-frequency but high-value) could surface policy angles that a single-agent approach misses entirely.

**Your Workspace Organization Needs the Client-Subfolder Model.** Nick's business/client workspace hierarchy mirrors something you should adopt for your consulting work. You work across OOBC, MoroTech, and potentially other BARMM entities. Each should have its own subfolder with entity-specific `.env`, skills, and CLAUDE.md — not everything mixed in a single workspace. The `/transcriptions` repo is clean, but your `e-Bangsamoro` workspace likely benefits from separating e-Bangsamoro core, OBCMS, Tarbiyyah-MS, and BangsamoroHR into the project-subfolder pattern Nick describes.

**The Diversification Warning Is Real.** You run 100% Claude Code. If Anthropic has an outage, your entire productivity stack — 135 skills, Obsidian memory, the fact-checking pipeline — goes offline. Nick's 70/30 split is worth considering. At minimum: (1) keep your `skills-bucket` repo synced with agent-agnostic markdown so Codex or Gemini can use them, (2) maintain AGENTS.md alongside CLAUDE.md in your key workspaces, (3) install the Codex CLI as a fallback.

**Auto Research Has Immediate Applications.** Beyond website optimization, you can apply Karpathy's framework to: (1) your skill quality — metric: eval score, change: skill.md edits, assessment: `/skill-optimizer` eval run; (2) your PDF generation pipeline — metric: visual fidelity score, change: CSS tweaks, assessment: screenshot comparison; (3) your Django API performance — metric: response time, change: query optimization, assessment: load test. You already have `/auto-research` and `/skill-optimizer` skills — but Nick's dashboard approach (live visualization of improvement curves) is something worth adding to make progress visible.

### How This Can Improve Your Claude Skills and Workflows

**Skills That Should Incorporate Nick's Patterns:**

- `/deep-research` and `/research-pipeline` — Add explicit **model-tier routing**: Sonnet for source gathering, Opus for synthesis. This single change could cut research token costs by 40-60% without quality loss.
- `/auto-research` and `/skill-optimizer` — Your implementation already follows Karpathy's framework, but Nick's **live dashboard** pattern is missing. Add a dashboard output option that visualizes the improvement curve across iterations — makes the auto-research loop tangible and helps you decide when to stop.
- `/bill-drafter` and `/resolution-drafter` — Add an optional **stochastic consensus pre-drafting phase**: before writing the bill, spawn 5+ agents with different analytical lenses (fiscal, Shari'ah, gender, BOL consistency, comparative law) to independently assess the policy question, then synthesize into a comprehensive brief that feeds the actual drafting.
- `/fact-checker` — Nick's security audit pattern (fresh agent, no shared context with the dev agent) applies here. Your fact-checker should always run in a **separate agent context** from the writing agent to avoid confirmation bias. Verify this is how it currently works.
- `/legal-reviewer` — Add Nick's **debate pattern** for complex legal questions: spawn 3 agents that independently analyze legal sufficiency, then share findings across rounds to converge on a nuanced legal opinion.

**New Skill Opportunities:**

- A `/security-audit` skill doesn't exist in your 135-skill library. Nick's security audit prompt (checking API key leakage, dependency hallucination, RLS status, public exposure) would be valuable for e-Bangsamoro and any BARMM platform you deploy. Checking `~/Vault/Claude-Skills/index.md` confirms no dedicated security audit skill exists — `/security` covers implementation patterns but not post-deployment auditing.
- A `/workspace-cleanup` skill that periodically organizes the `active/` or output folders in your workspaces, following Nick's pattern of asking Claude to sort loose files into logical subfolders and delete temp artifacts.
- A `/model-diversify` or `/fallback-sync` skill that keeps AGENTS.md and GEMINI.md in sync with CLAUDE.md across your key workspaces — insurance against the monoculture risk.

**Workflow Changes:**

- **Parallel agent execution during guidebook production**: when writing multi-chapter guidebooks with `/guidebook-writer`, you currently write sequentially. Nick's parallelization math shows you could draft 3-4 chapters simultaneously with sub-agents (each with its own fresh context), then synthesize and ensure consistency in a final pass. This could cut guidebook production time by 50-60%.
- **The `/insights` command**: run this periodically on your most active workspaces (e-Bangsamoro, transcriptions) to surface recurring patterns and failures. Feed the output into your global CLAUDE.md to prevent systematic issues.
- **Nick's "meta-prompt" for CLAUDE.md self-updating**: add a line to your project CLAUDE.md files that instructs Claude to append "lab notes" after any failed approach — this builds the failure log automatically without you having to remember to update it.

**Project Applications:**

- **e-Bangsamoro**: the parent + researchers + QA delegation pattern maps perfectly to your 4-portal architecture. Use Opus as the orchestrator that delegates frontend component research to Sonnet sub-agents, builds the feature, then spawns a fresh QA agent with no project context for unbiased review.
- **MoroMarket**: auto research for conversion optimization — metric: checkout completion rate, change: UI tweaks, assessment: A/B test results. This is exactly Nick's cold email optimization pattern applied to e-commerce.
- **Parliamentarian**: the debate pattern for complex legal analysis — spawn 3+ agents to independently research a constitutional question from different angles, then synthesize into a comprehensive legal memo with outlier arguments highlighted.
- **skills-bucket**: your skill archive is already designed for portability across AI agents — this is exactly the diversification strategy Nick recommends. Ensure AGENTS.md and GEMINI.md versions of skill files stay current.

---

## Transcript

[00:00] Hey, this is the definitive Cloud Code course for advanced users. I use Claude Code and AI agents in my own business every day to generate over $4 million a year in profit. I also teach around 2,000 people how to use Claude Code and other tools to improve their lives both personally and business. Okay, so this

[00:14] course is going to assume a foundation of Claude Code experience. It's not for total beginners, but if you are a total beginner and you happen to stumble on this course, that's okay. Just look over my left shoulder here, click that button, and then I have a 4-hour guide that will walk you through everything you need to get to the point where you understand what I'm about to say.

[00:30] Assuming you're still here, no fluff. Here's what we're going to cover. We'll start with an advanced look at cloud.mds

[00:35] and system prompts and learn how to optimize these to actually improve quality, which is simpler than you think. We'll then cover agent harnesses and how to build larger projects with Claude code. After that, we'll chat agent teams and other examples of extreme task parallelization. Then we'll

[00:47] do skills, sub aents, and other forms of organization. After that, I'll cover Karpathy's auto research approach for improving stuff progressively over time and a few actual use cases you can apply this to, not just fancy demos. We'll then talk browser automation, uh the major players. We'll do computer use,

[01:01] browser use, and which tools to apply to different use cases depending on what you want. I'll then cover how to deal with performance fluctuations in cloud code because they do happen as well as some alternatives that you guys could use and ways to bundle in multi-agent orchestration into your workflow. We'll then cover workspace organization, so for personal business, and then even client projects, assuming you're selling this sort of thing as a service.

[01:19] security for larger projects. We'll chat stuff like the recent auto mode. We'll talk a little bit about OOTH. And at the

[01:24] end, I'll finally round it out with a discussion about where I think Cloud Code is going and the future of work more generally. Hopefully, you're as excited as I am to level up your Claude Co skills. Please use the bookmarks and chapter headings as needed to jump around the course. Subscribe to the

[01:37] channel and let's get into it. So, for most of the course, I'm going to be building directly using the Claude Code extension inside of Anti-Gravity. That's this over here. If you don't have

[01:47] anti-gravity installed, this is an installation tutorial, but get that from Google's official anti-gravity.google website. Then head over to extensions, click on Claude Code for VS Code, give that an install, and then everywhere you go, you'll have this little Claude logo that you can use to spin things up.

[02:03] After a brief login, you'll have more or less the exact same layout that I do. I want you to know though that the Claude desktop app is also getting better and better by the day. And because Cloud is attempting to get you obviously on their infrastructure as opposed to on your own, um they're just continuously adding new cool features that allow you to do things like mobile development and so on and so forth. So everything I'm going to

[02:23] show you today works in both the Claude code tab of the cloud desktop app. Also works natively inside of a claude codes extension with an anti-gravity or some other you know IDE like thing. So if you're intimidated at all by the way that I've laid things out, what all these different folders mean and how they collaborate in order to improve your workflow, I'm going to cover all that in this course. First though, we're

[02:42] going to cover claw.md and other advanced system prompts. Basically, how to set up your system prompts in a very efficient and effective way. Both to

[02:49] save you uh financially, but also to improve the quality of your outputs and significantly minimize the amount of time it takes to build anything. So, what is a cloud really? Well, as far as I could tell, it's four things. The

[03:00] first is it's a form of knowledge compression. Okay? And when I say knowledge compression, what I mean is instead of Claude having to read through your entire workspace, you know, file by file, like for instance over here, instead of having to open up every single folder here, every single one here, read through all of the files and so on and so forth to be able to reason and then make highle declarations about your codebase or folder. What your

[03:25] claw.mmd does, okay, is it basically just compresses all of that down into a highly succinct summary of what the heck is going on in your freaking folder. So that the next time you say, "Hey, what was that file I made a couple of weeks ago about X, Y, and Z. Claude doesn't

[03:41] have to look through every single file in your codebase. You don't have to spend a tremendous amount on tokens, and you also don't have to wait a long time. It's just sort of baked into the cloudmd, or at least a reference to where the file lives is baked into the cloud nmd. um so you can actually like

[03:53] reason with it um at a superficial level at a bird's eye level as opposed to actually going down through the weeds. So that's sort of like the very first thing that I'd say, you know, a claw.md is. The second thing that a claw.md is

[04:05] is it's obviously your own preferences as a user. And what you'll find is, you know, more or less every time Anthropic updates claude code, you have better and better baked in native preferences and conventions for things like, you know, delivering you file paths or uh how to deal with like documentation or debugging or how to update itself and so on and so forth. But obviously claude code lags behind these preferences a little bit um because they have to see what users are actually using it for and and you know like they collect that information and figure out what ways to make things more effective. So if you're

[04:38] an advanced user as I am, you'll have a list of these preferences and conventions that improve your user experience. And advanced users will always have just some better preferences that kind of adapt their own workflow as well as you know programming conventions, um ways to organize information, structures and and that sort of thing. Okay, so it's both a form of knowledge compression, but it's also preferences and conventions that are not natively baked in that you get to u decide on. The third thing that clawmd

[05:03] is is it's a declaration of capabilities. Now, I don't know how many times this has happened, but if you do not have a substantiated enough clawmd and then you have let's say a skill somewhere in your your workspace or you have just some knowledge that's sort of floating around in a few files and you say, "Hey, claude do xyz thing for me. So, you know, find some knowledge on XYZ person or go do some research or uh you know, compile a plan using XYZ framework. Half the time, okay, if it's

[05:28] not in your cloud and cloud will just look at you metaphorically, obviously it doesn't have eyes yet. Uh and it will say like, oh, like I don't have a built-in way to do this. Um sorry, what were you referring to? Do you want me to

[05:37] build something from scratch? I'll happy to do it. And this this sort of slowdown loop is completely unnecessary. And so

[05:43] what cloudmd allows you to do is it basically allows you just to itemize okay uh you know everything that your agent can currently do within your workspace. And you can make that really clear. You could say hey you currently have access to this functionality. You

[05:55] can do this. Hey uh you know you can build a a fullstep plan that lasts 10 or 15 minutes and then executed on an autonomously. In fact that's my that's my preference or the convention that we're using. You know you can call this

[06:06] API you can call this database. You can retrieve all this information. You can act autonomously using browsers and so on and so forth. The reason why that's

[06:12] important is because as agentic as Claude is, hopefully we're we're all still on the same page here um about this fact, Claude still lacks a lot of agency. Okay? If you ask it to, you know, help you do something or if you ask it how long would it take to do something, it'll often significantly underestimate or overestimate because it's not really factoring in its own agenda capabilities. Like I asked it the

[06:32] other day, um hey, you know, how long is would this XYZ thing take to build? And then it was like about 3 months or so because you would have to build this, you'd have to build that, you'd have to build that. And it's obviously like, "No, I don't have to build that. I'm

[06:42] asking you to build it. You could build it in 5 seconds. So, why don't you just go ahead and do it?" Or, you know,

[06:46] you're having it do some API stuff and then it sends you a little command line interface prompt and it's like, "Hey, just pump this into the terminal." It it sort of needs reminders that no, I don't have to do this. That's why I'm asking you to do it. So, you can actually do

[06:56] all of this stuff, Claude. Declaring capabilities in this way, whether it's your own personal like tooling or workflows or whatever, or it's um, you know, uh, Claude understanding that it has the ability to do things that it might not realize at first glance is pretty important. And then finally, the fourth thing that a cloud NMD is is it's a log of failures and successes. What I

[07:15] mean by this is as you accumulate various files, as you accumulate, you know, bits of code through your project and stuff like that, every single one of these things is hard one. You didn't get them for free. Realistically, you spent tokens and then your time, which are soon to be two of the world's most valuable resources. And so because you

[07:33] spent all this time and energy, it is more efficient for you to take all of the learnings basically from every single piece of development or every single action cloud does and then insert it in its next system prompt than just have it restart kind of from scratch every time. You know, viewed another way uh mathematically, if this is the total space of all of the different possible things that Claude could do when you say, "Hey, do x." What this log of failures and successes is doing is it's basically carving out big chunks of this theoretical solution space and it's saying hey no you you don't do anything over here because we've already tried all this stuff over here kind of looks like a planet meaning the only things that you can actually try and the only things that you should try are kind of the things that exist in between. Okay. So basically what this

[08:18] log of failures and successes does is it just allows you to immediately cross out like 80% of all possible things cloud could do because it knows it's actually tried that in the past and then in that way focus its time, effort, your tokens, your money and then your your energy on the 20% that actually matters. So these four will exist in different sections in your cloudmd. They'll also exist at different levels both global and local. So, what I'm

[08:44] going to do next is run you guys through high ROI ways to combine these four sort of principles behind system prompts and then apply them u both in global local and then also give you guys sort of like a little workflow loop that you can use in order to understand how to update this effectively. And this isn't just going to be some big long system prompt that I'm giving you guys like I think we've probably all seen floating around various sources in the internet. The reality is like cloud entities are highly personal uh devices. Um, but

[09:08] these are going to be a list of short principles that will almost certainly help you design better projects and then get more done whether economically or or otherwise. So, the way that all this is organized within cloud code is using two different scopes, global and local. And if you didn't already know, basically there are a variety of different places that cloud code upon initialization will look to to get the prompts that is injected at the very top of its um context window. Okay, the two big ones

[09:33] for us are the user over here, which is equivalent to your global, and then also the project over here, which is equivalent to your local. And so, basically what this means is if you have a file called claude.md all caps, that exists within this folder on your computer somewhere, it'll load that up on every cloud code session, whether or not you're working in the same workspace or another one. Now, if you have a cloud

[09:58] MD, capital cla.lcasemd lowercase MD located within a dotcloud folder within your specific repository directory then it'll also be loaded and in this way you know you sort of have like a global precedent that's always injected at the top of every single thing okay no matter what and then you also have sort of a smaller little um you know local cloud denomin that's also injected and collectively when I say you know system prompts from here on out really what I'm referring to is I'm referring to both of these I'm not just referring to one of these and because global is injected on every single run they're sort of like different strategies in order to divide the four things that we just talked about. Um, basically on your global claude.mmd it makes more sense to put

[10:37] highlevel reasoning and then your own personal beliefs and then in local cloudmd makes more sense to insert local low-level knowledge. So stuff like I just talked about with the um workspace itself. So you know if I were just enumerating all of these things up here okay you'd put your preferences like your global preferences. These could be

[10:56] things like, hey, you know, when you return a file, I want you to return the absolute file path to click on it because whatever editor I'm using doesn't really have take that into account. You know, it could be things like uh programming conventions. Hey, I want you to program using, I don't know, object-oriented programming or hey, I want you to do like functional programming in in Rust. Hey, when I ask

[11:13] you to develop a new project, I always want it done in Rust as opposed to, you know, Python or or something like that. Alternatively, it could be stuff like, uh, hey, you know, if I ask you to do something using a tool you're unfamiliar with, always go and read the API documentation first before attempting to start because every other time that you've attempted to do something without the API documentation, you typically run out of loops, you waste XYZ tokens. So, make sure to load the API docs. By the

[11:35] way, if you can't load the API docs through uh, you know, HTML, then make sure to like load up a Chrome DevTools MCP server to go and get that stuff, even if it's dynamically loaded through JavaScript. Okay, so these are highle reasoning strategies. These are your own preferences. These are your own

[11:50] conventions. And then also um these are going to be just sort of like agency capabilities. So stuff like hey Claude, you can actually do X Y and Z. If you

[11:58] believe that you can't for whatever reason, you're wrong, you can absolutely, you know, go and do whatever you want. The local low-level knowledge. Okay, this is going to be stuff like backslashit, which I'll show you guys in a second. So this is going to be like a

[12:09] compressed version of all of the knowledge on your workspace. Instead of claude having to in the future go through every single file, it'll just be able to read the cloud and sort of have a loose understanding like okay, what's where why have we built this? What's the purpose of this workspace and so on and so forth. Some additional things you can

[12:24] do are things like context about you and your goals and your own reasoning strategies, your own communication styles. So I'm going to give you guys examples of my own cloudm in a moment where you guys see that I actually give it a lot of context about who I am and why I want what I want. Um, I'll run it through, you know, reasoning strategies that I personally use that have, you know, yielded me a lot of success in the past that may actually not necessarily be the optimal reasoning strategies, but which I tend to understand. And because

[12:47] I'm communicating with this thing at every freaking every 5 seconds nowadays, I'm I'm better capable of understanding what it's putting across if we use those principles. Um, and then yeah, those high level preferences and then generally good token conservation strategies. Whereas with the local, you know, it's a description of the project, where everything is, low-level preferences like specific API docs and usage. If you are using you know the go

[13:05] high level API to do some project or whatever you can actually just like have the whole go high level API existing within your project that'll minimize the number of tool calls that um cloud has to make to you know some sort of research sub aent go and do the thing for you instead it can remain local reduce total token usage and then also just be faster and then more accurate and then capabilities within the project and then that takes me to the local workflow so and then that takes me to workflow so there's two sort of workflows here that I want to talk about there's the local workflow and then there's the global workflow and the local workflow is going to be responsible for updating our local cloud.mmd and then the global workflow is going to be responsible for updating our global cloudmd. Like it would be nice if I could just give you on a silver platter a bunch of stuff to put in your cloudmd, right? I think that's

[13:44] what a lot of people want. But you're going to end up a much better both developer and then a much more productive person if you understand the principles at play here and develop your own. So initially to start um anytime you're developing anything in in cloud code or whatnot obviously you need to plan your feature and I say feature here loosely. You know, I use cloud code as

[14:00] basically like my business assistant nowadays. And so I use it to do anything from reading my emails to grab me new news summaries in the morning to to communicate with XYZ people to design me, you know, websites and so on and so forth. So feature here is really loose.

[14:12] I'm not just talking like about a vibe coded project. I'm talking about anything. But what you do is you start by planning a future, right? And then if

[14:18] you think about it logically, what claude does next is it instantiates the future. However, over the course of planning and instantiating, okay, it will fail a bunch. it'll also succeed a bunch of other times and ultimately there'll be a giant list of learnings between you know step one to step two and so what you do after you instantiate is you actually compile all those learnings okay into some efficient um high information density thing that doesn't seem a lot of tokens then you use that to update the cloudMD and so this is your local workflow for managing your system prompt and you basically just do this every time you plan something it'll do a bunch of failures in the way then you'll instantiate it you'll take all those learnings update your cloud NMD. That way the next time

[14:59] you plan a feature, it'll already have all the benefits of the failures plus, you know, any additional things that learned along the way. And so the first time around this loop, you know, it might take uh I don't know, let's say X time to develop a feature. The second time around this loop, you know, maybe it'll take like 0.9x because now, you

[15:14] know, you've shaved off 10% of the the the search space and it's a lot faster. The third time you go, maybe it takes 0.8x. Okay? Okay. And so like the time

[15:22] will just get faster and faster and faster every time until eventually you develop things um using claude in a similar way that you would develop if you were not using cloud. Now here's where it differentiates between the global workflow. What happens is you know as you accumulate a variety of failures, successes and learnings and so on and so forth. Your current local

[15:38] cloud gets really really good after all that's done. What you do is you know after hundreds of these runs, okay, you can either pull a slash insights feature or you can run that yourself to show you guys how to do. What this will do is this will compile not like at a local level, but at a global level all of the things that Claude attempts uh pretty consistently and then struggles with pretty consistently. You know, it's

[15:59] like, oh, hey, I noticed that not only on that one project, but also on more or less every project, Claude consistently goes down silly rabbit holes it doesn't need to um and then tries coming up with its own stuff instead of just consulting the docs. And so, you know, after this is done three or four times, obviously there's a trend, right? So, what you can do is you can take that information and then you can pump that in your global.

[16:16] Um, after that, what I'd recommend is is I'd recommend you manually review because Claude is an agent at the end of the day. And the more AI steps you have, the more you compound probabilities and the less likely that it becomes that Claude itself is making like the right call. You know, if like Claude is independently 90% successful on a task and then you give it to another claude which is 90% successful to a task and then you give it to another claude, you know, what you're really doing mathematically is you're going um 0.9

[16:41] raised to the 3. And if you just do a little bit of math there, that's not 90%, right? 0.9 to the 3 is 73%. And so

[16:48] I guess what I'm trying to say is um the more steps you have without a human in the loop here uh the lower the likelihood that your total determination will be correct. And because this is your claude MD, it is your global preference and convention file, it will be applied to every future project. Meaning if there is a place you should spend human time on, it is this exact step here. So I'd recommend manually

[17:06] reviewing that. Once you manually review that, then you can add some high ROI bullet points to your cloud NMD and so on and so forth. you know, just like a high information density version. And

[17:13] then you can actually update the the cloud in MD. And then you can repeat this loop a few times if you'd like before finally going back to the local loop. And so I mean, it's kind of like I don't know what you want to call like an infinity sign. Okay? Kind of starting

[17:24] here, you're going kind of like this. And then you're kind of looping back and then you're just doing this over and over and over and over and over again. Obviously, you're going to spend a lot more time in this loop, but eventually you're going to go down to this loop.

[17:35] And this is how I personally develop using Cloud NMD. This is why my workspaces are super tight. And then instead of me, you know, using a vanilla version, asking it, hey, go do X, Y, and Z. And then it like stumbles around,

[17:44] uses 20,000 of my tokens and God knows how many of my dollars, when I say, hey, I'd like you to do X, Y, and Z. I'd like you to go scrape some laser over. It already has all that stuff baked in while still being flexible enough that I could change them anytime that I want.

[17:54] Okay, so next I'm going to show you guys basically my workflow every time I start with a new project, uh, assuming that I've already done a little bit of work in the project. I don't have a cloudmd, and I don't really have any of that like advanced tooling or system prompt harness and stuff, uh, set up. This is exactly what I would do step by step.

[18:07] So, first of all, you need to open up a folder. Um, I was just learning about toatillos earlier. That is sort of embarrassing. But anyway, in

[18:13] anti-gravity, just go open recent. And then I'm just going to open up something. Why don't I do, you know, anti-gravity example right over here.

[18:19] And, you know, when I'm in this folder right over here, obviously, there are a bunch of different files and, you know, configurations. This one was using Gemini for a while. So, what I'd like to do next, I'd like to open up a Claude code. And so, I'll click on that button

[18:31] over here. Let's close out the agent window because I'm team Claude, at least for the moment. Thank you, Space Invader. And really like the first thing

[18:36] that you do is you know you you develop on your own. I always recommend just like don't try baking in any opinions into a cloudmd until you've at least developed with without a cloud or some sort of advanced system prompt for a little bit. And the reason why is because like you'll find cloud's actually really good out of the box. As

[18:51] mentioned they are incorporating more and more of these features natively within it. And so like it's it's great. It's not like the harness that makes the intelligence. It's obviously the

[18:58] intelligence inside of it that sort of you know communicates with your system prompt to get good. But right now it's already fantastic. Anyway, after you've done some developing for a while, and this is obviously some sort of website here. It's like a template using VIT.

[19:09] Just go slashinit just like that. And basically slashinit will go through read every single file in your workspace, which I'm currently doing with fast mode if you're wondering why this is probably faster than than what you're doing. And then at the end of it, it'll come up with basically like a highly optimized claw.md file that succinctly and

[19:26] effectively summarizes the placement of everything here. And you can see it just generated one called claw.md. So comes

[19:32] with the built dev lint commands. Note that no test framework exists. Some architecture review key dependencies and their roles. Then some style conventions

[19:39] as well. So now I'm going to open up this cloud NMD. Okay. And why don't we

[19:43] just move this over to the main window so it's a little bit easier to see. And you can see that more or less it it just at a very high level summary takes every single line in my entire workspace. Then it just significantly increases the information density at a cost of like total comprehensiveness. So what I have

[19:58] now is is I have a summary of everything. So, what that means is the next time that I ask Claude anything about my workspace, okay, the next uh the next go around, um I don't actually have to like have it like run through every single thing in the file. Like for instance, what I'm going to do here is I'm just going to call this like um I don't know XYZMD or actually, you know, why don't I just delete this for now. You know, if I had

[20:21] asked this clawed version something about dark mode, hey, what are my opinions on dark mode? It's going to check its memory for notes on the preferences. Not going to find anything.

[20:31] And notice how it's just going to say there's there's there's nothing at all. So, what I could say is read through whole project and find my preferences. And now what it'll do is it'll, you know, essentially launch some sort of agentic search with readmes and so on and so forth until it finds something about dark mode. In this case, it was in

[20:46] the gemini.mmd. Um, but I want you guys to know that, you know, whether or not you have it in a gemini.mmd or it's just

[20:51] sort of written, it'll eventually figure it out. Now the issue is you know how what what sort of usage did we just uh do in order to get that? If I just scroll all the way up here typed /context you know the system prompt was6% free space was messages are 0.9%.

[21:06] So that last message chain there with the tool calls and everything like that might have realistically taken like five or 6 thousand tokens. I don't need to do that sort of thing ever again. You know if I bring that back and go claw.mmd and

[21:17] then if I just open up a new instance and I say hey you know what are my opinions on dark mode? Obviously, it's going to read the claw denimd and you know, instead of me having to use god knows how many tokens, if I go back to slashcontext and you see that now you only use 02%. So, basically saved myself what's that like 6,000. And let me tell

[21:34] you, these cloud tokens ain't free, man. Andropics increased on the price uh pretty aggressively, especially recently when they realized 99% of the world is now operating using their infra. So, I guess what I'm trying to say is I'm spending like literal like money, but I'm also spending time. And to me, the

[21:46] bigger thing is time. What are some other things asked? I mean, like think about deployment. If you have any sort

[21:50] of like front end or full stack experience, you'll know like you know usually the flow is you start with a dev server. You use that dev server via npm rundev or equivalent to like figure things out on your uh you know develop various features and so on and so forth. Then you'll build you'll do some sort of linting and then once you're done you'll actually like preview it. you'll you'll

[22:06] push to production or or sorry you'll push to staging and then verify that and then eventually you push to production right like obviously this is something that it could have learned just by going through the folder structure seeing source public node modules all these things but you know I'm just listing them out over here so that instead of you having to actually read any of that filing or tooling you know you can do it in god knows how many what's like five tokens six tokens or something immediately likewise you know I see where things are laid out so in this case this is obviously a single page application the entire app lives in a single component nav hero services projects and footer sections. All markup and logic is here. Um, it is evident if you were to actually click on app.jsx

[22:41] and then scroll through that that is the case. But look at how many more tokens app.jsx is versus, you know, just that brief little description in uh clamd. If

[22:48] I were to copy and paste the entirety of this into something like a word counter, you can see it's 827 words approximately 1100 tokens. Okay. If I go back to my claud, like how long is how long is this? It's 22. So that's a what 45x

[23:00] compression ratio. That sort of compression is how you ultimately get a significantly better and more effective clot because you are not shoving a tremendous amount of tokens at the beginning of any query. Um, and you know, as we hopefully know, uh, token length tends to scale inversely with the quality of the output. The more tokens

[23:16] in a context window, not only the more money are you spending, but typically the lower quality the results are. So, just avoid all that by initializing and then storing a bunch of information about, you know, what the project is on. Uh, you'll be you'll be much happier for that. But, you know, slash in it isn't

[23:29] the only thing that I would do. From here, I'd actually start importing a couple of my preferences and then things that it's tried. So, I don't know, let's just say I'm going to remove the gemini.md for simplicity. Let's just say

[23:38] I'm developing a new feature and um actually, why don't we just visualize app IDK what it looks like. Let me actually take a look at this thing. So, it'll run the dev server so I can see it in the browser. And immediately I'm

[23:47] thinking like, hey, you know, this is actually kind of inefficient. When I say visualize app, I basically just want you to launch it. So, store in your cloud.MD

[23:53] that when I ask you to run the dev server or open the app, I just want you to open it in my Chrome instance as well. I don't just want you to run the dev server. You know, basically next time I say this, I don't want it just to like say, "Hey, the dev server is here.

[24:03] Give it a click." And then I'm like, "Okay, can you just open it cuz I'm already here." Um, I just wanted to open it automatically, right? Okay, cool. And

[24:09] I see, you know, it's kind of over here. Um, so that's nice. Definitely not a fan of the design. I don't like how it

[24:13] scrolls through. I'll just say, "Hey, I want you to significantly improve the perceived visual quality of the application. Go and look up, uh, you know, the Apple website and then compare that to our website. Make some changes.

[24:22] That just improves both the perceived visual cohesiveness, quality, etc. Must have been a Gemini website. Anyway, let's uh see what it does here. It's

[24:29] fetching Apple's site for design reference, reading the current app code in parallel. And now it's just doing a bunch of updates, editing the CSS, nav-link, hero- background, and so on and so forth. And you can see that it is actually updating the site. I mean, it's

[24:39] doing it currently in real time, but uh it's looking significantly better. It's also picked up some new colors and so on and so forth. Now, what's cool is it actually just opened up a second, uh project for me right over here. Um

[24:49] because earlier on I'd stored my preferences that I don't want it to just give me the link. I actually want it to, you know, open open stuff up. So, that's nice. So obviously we have better

[24:57] designing and stuff like that. But the key part here is when I say, "Okay, great. Nice job. How could you have

[25:01] arrived at these conclusions and done everything I just asked you to do faster?" Okay. And now look, we're already at the point where we're capable of optimizing a fair amount of these design issues. Instead of 20 edit calls,

[25:10] which is what it did before, what it could have done is just do one write call. So the reason why that took like 30 seconds or so because it was editing the CSS file line by line across 20 sequential tool calls. I should have read the file, rewritten the whole thing in my head, done a single write to replace index.css in one shot. Yes, I'd

[25:25] like you to save this in the local cloud.MD do it as a user preferences section. So asking it questions like how could you've arrived at those conclusions and done everything I just asked you to do faster and for fewer tokens is pretty powerful. Um doing this

[25:36] consistently as you develop and design a project and then having a running log of changes to the cloud NMD is also quite valuable. Another thing you can do is you could set a meta prompt in the cloud NMD and that's personally what I always do that basically says like when you have made a mistake I want you to update the cloud NMD with a running log of things not to do next time. When you've made a mistake, I want you to update the cloud.MD with a running log of things

[25:58] not to try next time. Essentially, I want this to be almost like a mini experimenters or research person's notes that shows what a future Claude instance should not do uh while working on this project. Update the claude.mmd to

[26:11] reflect what I just said at the very bottom. Okay, now it has a section called lab notes, what not to do. This is going to show a bunch of failures as well as learnings and successes and so on and so forth. And we're already

[26:20] honestly like halfway down the loop. Now, this is a very contrived example because I'm literally just building a website. But imagine that, you know, instead of just a website, you're building a workspace that is meant to contain all of your business uh basically entirely. All of your SOPs,

[26:32] it's meant to contain all of the work that you do on a daily basis. It's meant to contain your to-dos and so on and so forth. Having information like what I just showed you for this project would be invaluable across more or less all levels of both development and then also productivity. And that's personally what

[26:45] you should ultimately be working towards. So anyway, we can make this as complicated as we want obviously, but hopefully you guys see that loop at work. We plan a feature. So we just did

[26:54] this. It was simple enough that we didn't need to use a dedicated plan mode, but obviously I still oneshotted it. After it implemented the feature along the way, it did a few things that realistically it could have done better.

[27:03] So what do we do after? We take those learnings, we compile them, and then we update the cloudmd. And this was sort of a meta example since I literally was doing it while I was building the cloudmd, but hopefully you guys at least understand conceptually sort of what you do after four or five of these runs.

[27:16] There's probably a fair amount of stuff here that you can take advantage of and that's where an insight run would make sense. So, let me actually zoom in and then just delete this so you guys could see. In case you didn't know, insights is a simple slash command that basically runs a bunch of sub aents across all of your cloud conversation history. The

[27:32] benefit to that is now not only are we running you know and changing our local cloudmd we're also evaluating all of like the patterns in communication that we've had with cloudmd over the course of the last I don't know could have been like a few days could have been months could have been I mean years depending on how soon or late rather you are watching this video. So um just like we optimized our local cloud MD now we can start optimizing our global and while it's chewing away because insights does take a fair amount of time. Okay, I'm just going to create a new file here and I'm going to call it globalcloud.mmd.

[28:01] And I'm just going to give you what I would consider to be at least as of the time of this recording probably like some of the higher ROI principles to make sure to include. Um I include this in my own global cloud and MD because I think it's just very very valuable. So I'll say global cloud and MD. This is

[28:16] inserted at the beginning of any conversation with Claude across all of the users workspaces. So first I have a profile section. So this is a bit about Nick. So, you know, I don't know. It'd

[28:27] be like Nick is a 30-year-old and J high performing internet entrepreneur. He runs a YouTube channel at 350 better 350 by the time I make publish this video. 350,000 subs, an Instagram channel, and so on and so on and so forth. Okay. Okay. And so I have a bunch

[28:51] more information which I've taken from just a couple of other systems I've built. Um this one here is Nick is a 30-year-old NJ. Here's his revenue. So

[28:59] here are all the different things that contribute to my revenue. Here's some churn math. Um some of the companies that I'm currently owning. Uh some

[29:07] teams, right? So it's me. It's an editor. It's a LinkedIn newsletter

[29:10] person. It's a bunch of AI agents. Bunch of information on YouTube as well as my goals. And then ultimately some on

[29:15] Instagram as well. Now you're thinking like Nick, this is crazy. Why would you insert all this information in your global cloud NMD? Well, the reason why

[29:21] is because I want this on every conversation that I have with it to understand who I am and to take that into consideration when discussing things with me. I can't tell you how many times I'm having a conversation with Claude and because I don't have context like this cuz I'm in a naive thing with no personal system prompt check in the context window. I say something along the lines of, "Hey, what's the best solution for X, Y, and Z?" And then it says, "Oh, you're going

[29:41] to want to do this solution." And then I say, "Why?" And then it'll say, "Oh, because it's the cheapest, right? It

[29:45] only cost 0.2 whereas the all the other solutions cost $5." And I'm thinking, well, if you knew a little bit about who I am, you'll know that money is not the primary bottleneck right now. I prefer

[29:53] you to exchange my my money for my time. Um, so just giving it some like highle principles like that is very important. Anyway, while it was doing that, um, the actual sharable insights report, um, is ready. So I'm just going to tell it to

[30:04] open it so I can take a look at it with you guys. And now you'll see there's an HTML page basically that runs through everything about Claude, all of the insights across all of the sessions. Looks like 1,849 messages across 200 sessions. I don't know where this

[30:18] chooses the cutoff. It looks like it's like about a month or so. Um although keep in mind that like this is cloud code specific and I don't know if this encapsulates all the conversations I've had with it on the desktop app, but pretty good. And you can see here that

[30:30] you know there's a bunch of context about what I work on and and so on and so on and so forth and how I use it and all this stuff. So the the important thing to do is existing features to try section. You can just copy this into cloud code and add in your cloud NMD. So for instance,

[30:44] when using Chrome Dev Tools MCP or browser automation, always kill stale Chrome processes in a clear profile before starting. If the MCP tools fail twice, stop and ask the user before continuing to retry. Never waste tokens on repeated failing browser calls. This

[30:55] is actually quite valuable just given how many times I have tried to have it run, you know, Chrome DevTools MCP and it's failed. Um, same thing over here. Same thing over here, you know, with some face swap information and stuff like that. You can copy all this in

[31:08] cloud and it'll set it all up for you, which is pretty valuable. as well as it can even go and build like new skills based off of things that you consistently ask. So that's that's more or less what I'm doing here. Um anyway,

[31:17] the the value with this is basically to like copy the entire thing, go back here, paste it in and say this is my claw insights file. It describes at a high level a few of the obvious design patterns in my thinking and then a couple of the issues that I've had communicating with you and other versions of you. I'd like you to distill this into a list of high information density snippets that I can paste into a global cloudmd to be both tokens conservative but also avoid most of the mistakes that you typically make. Then

[31:42] I'll just press enter. It's going to give me some information about that. Then over here we actually have the changes and this is very high information density, right? It basically

[31:50] took a bunch and said don't overexlain, overengineer or add un requested improvements. When making widespread changes to a file, use one write instead of many sequential edit calls. Speed matters. Don't fetch well-known

[31:59] websites. again a rerun browser automation and you know so on and so forth just some just some highle stuff it looks like it just inserted that in here which is quite nice so now what do we have we have if you remember some context on me in the global clouded MD we also have some highle reasoning rules and principles and really what we're just missing is some um token conservation strategies and you can see this by uh you know you can go back uh rewind the video if you'd like some more on that but basically you want context about you your goals and your reasoning strategies some high level preference references about, you know, what it is that it is currently doing that is wrong that you would like it to fix and then some good token conservation strategies like knock docs first. So, I'm going to do is underneath interaction rules, I'll also just say, oh, and what's really interesting that I'm seeing one of my rules are actually directly contradicting some of the other rules.

[32:46] Don't fetch well-known sites. Actually, just remove that. Um, that's the human in the loop part, right? Just look to

[32:51] see if any two rules directly contradict each other. Then I'll say when a user asks you to use a non-trivial platform, one for which you do not have context in always look up the documentation first. You can do so by looking into API documentation plus platform name. After

[33:09] if for whatever reason you can't access the docs for JavaScript reasons, launch a Chrome DevTools MCP Chrome instance so that you could still copy and paste all that data. No matter what, if you're working on a project for whom API documentation is available, you should always go through the API documentation to avoid 99% of the errors. The tokens we spend reading the docs will save us a lot of tokens and trying to use things that don't work. Cool. So, I'm going to

[33:30] copy that. And now I have my global cloud NMD. And you know, I could obviously just have Claude actually insert that into the global cloud MD.

[33:37] Um, I could also just like go and find the find the finder. So, I'm going to go to finder on Mac. Basically, you can find your global cloud NMD just by going to your Mac. In my case, users on my

[33:47] next surf. And then um there's a hidden folder here which you can't actually see. Just right out of the gate, you should be able to go uh shift command. I

[33:55] think it's comma or period. There you go. Shift command period. Once you're

[33:59] done with that, you can scroll all the way down where it says cloud. And then over here, you'll see there is a cloudmd that lives within that cloud. So what I can do now is I can just reveal this folder in my finder, compare it to that folder in my finder, and I can actually just go drag and drop this in. I have

[34:15] global cloud and I can just remove this claude and replace that with this cloud. Awesome. So now all future conversations that I have with claude across all of my uh workspaces and all of my folders will include the information that I just provided. And hopefully you guys see how

[34:27] simple it is to run that loop. Um granted this is an informal loop. I'm not really showing you guys like a simple formal streamlined process. But

[34:33] hopefully you see how easy it would be to build that in again as like a meta claude. Let's talk a little bit about agent harnesses. So agent harnesses, the term anyway has gotten a ton of interest over the last couple of months because it's sort of new and exciting, but very few people actually understand what it refers to and what it means. An agent

[34:52] harness, to be clear, is just claude code. Claude code is the harness around the model claude that enables it to do things like call various tools and get actual economically valuable work done. For those of you that don't know, um, all that like AI models are are just text interfaces, right? It's just text

[35:12] in, text out. A harness is what turns something that can only communicate in text into something that is ultimately capable of like controlling our computer. So the way that I personally think about the question, what is a harness? Is a harness is just everything

[35:27] that wraps around the LLM that is not the actual LLM itself. So in our case, it's claude code. It's the system prompt. It's the hooks. It's the tools

[35:37] that it has access to and it's the parameters therein that control things like when the memory autoco compacts, how many messages you can send in a turn, what the total number of token limits are, and so on and so forth. For the purposes of this demo, let's pretend that this over here is our clawed space invader. Okay? And so this is sort of

[35:56] like the the the large language model itself. This is actual Claude. And so Claude is obviously like a galaxy brain intelligence. It's been trained on god

[36:05] knows how many books and blog posts and encyclopedias and so on and so forth. But you know Claude is sort of it sort of exists in this boundary where it can't actually do anything outside the real world unless it's given the tools and the ability to do so. And so um one example of things that Claude has access to are set tools. So that's things like

[36:28] uh I don't know the ability to use bash aka use a terminal. The ability to use I don't know GP which is how it finds things on your computer and so on and so on and so forth. Another thing that it has access to kind of gone back and forth is some form of memory right what it can do is it could read so it could read things that are stored in this memory and then it can also write so we can add and sort of update things as needed. You know, there's obviously also

[36:52] a variety of other things here that it has access to. And, you know, if it didn't have access to all these things, again, it would just be like an agent or a model, sorry, that exists in the box. And so, that's really the difference between, you know, LLMs and agents.

[37:05] Agents are LLMs plus a harness, whereas LLM by themselves, large language models, they can't really do anything. They obviously um operate entirely in the domain of knowledge. So, just given the fact that it's called a harness, you can kind of think of it as, you know, I'm going to draw a really crappy dog here. Put another way, here's a really

[37:23] crappy rendition of what I initially wanted to be Canadian dog sledding and what ended up being uh looks more like Santa with a big fat beard riding a questionable reindeer. Uh, but basically, you can imagine that like this right over here, this is your LLM. This is the actual model intelligence.

[37:39] And then you over here, okay, this is your harness. This is actually like the the code part of clawed code that sort of controls it. And so the LLM wants to go in a bunch of different ways. It

[37:48] wants to do a bunch of things. What the harness does is it just sort of narrows down its um direction. And you know, you can kind of almost think of it like uh the barrel of a gun or something like that, right? Whereas, you know, back in

[37:59] the day, you might have had like cannons and then you might have loaded those cannons with big uh massive cannon balls and they're huge and what you do is you'd stuff some additional gunpowder underneath and stuff like that. And those cannons would kind of, you know, despite the fact that they were operating off the same fundamental technology, which is gunpowder, they might not really be able to go so far. I don't know, let's just say 50 m.

[38:21] Nowadays, obviously, we have um this is my really crappy gun drawing with, you know, more or less the exact same technology, you put some sort of bullet in there, right? But then because of the technology that surrounds the core thing, which is the gunpowder, you know, the bullet can go a lot farther. And so maybe instead of 50 m, now it can go, I don't know, 250 meters or so. So, this

[38:42] is how I this is how I think about harnesses, okay? And I don't mean to just show you a bunch of silly grade school analogies, but it is important to realize that like that is what um now cla code really is. And because Claude code is a harness, obviously there are a bunch of other people out there that have tried making their own harnesses as well, just like we have frameworks like React and Vue and then Nex.js and and

[38:59] and Nux. We also have a bunch of different harnesses that have been developed that supposedly work on and then improve on on specific aspects. What are some of those aspects? Things

[39:07] like security, right? Automatic permissions. So, plan mode versus default mode versus the new enable auto mode and then bypass permissions mode.

[39:16] You know, there's some harnesses out there, okay? There's some agent SDKs and stuff like that. Not going to name any names, but um there are some of them that are probably a little bit less secure than others such that if they were to read a Twitter thread that look like this, maybe they would actually execute pseudo rm-rf and delete your entire hard drive. Right? Bunch of

[39:34] examples of people screwing around with this. This is an example of codeex which um you know being an extraordinarily competent model I can't really talk down too much on but this is an actual conversation that uh you know it had with somebody that I found on Twitter. You know the model basically tried running something that was like rm-rf which to make a long story short in case you didn't know just deletes everything.

[39:53] And uh here it says well the shell policy actually blocked the raw rmrf. So what I'm doing is I'm removing those generated directories aka the shell policy with a python cleanup instead. same effect, less policy friction, right? It's just going to go end up

[40:05] deleting the entire thing. You know, the the harness impacts a model's ability to get things done. It also impacts ultimately the safety. It impacts like

[40:12] the memory and so on and so on and so forth. And so hopefully at least now you guys understand what the harness is before I show you guys some examples of different versions of it. Obviously, Claude code is the major harness today.

[40:22] Um, but there's a great blog post over here by Langchain that more or less describes a way to create different harnesses. uh the model gets a certain type of context injected into it prompts memory skills or conversation then you also have orchestration things like Ralph loops which was really big a while back that was a different type of harness um you know there's a certain persistence of data actions and then the ability to both observe and verify say with screenshots and stuff like that um one harness that a lot of people are using now is this sort of droid idea which was built by factory AI so droid is like a publicly available harness that you can run and download today pi P.DEV is also exploding in terms of popularity. So whereas claude code, you

[41:02] know, obviously needs to run with claude um infrastructure, right? Cloud is the model underlying cla, this PI coding agent is sort of like the open- source provider of it, you can feed in more or less anything that you want, including claude, and then just have it operate inside of this this harness. And you know what this does is it just changes the way that we store memories. It

[41:19] changes the way that we store certain files. It sort of like modifies it's almost like an alien or bizarro version of cloud code in so far that it changes a few of like the fundamental constants like how long before context compaction you know how to try different types of solutions and stuff like that various bakedin behaviors regarding a cloud code and and so on and so forth and the reason I'm covering this is because you know this is something that was very fundamental to anthropic that back on November the 26th 2025 they wrote a big long blog post called effective harnesses for longrunning agents which at the time kind of changed the game and I would say this is the beginning of the kickoff of cloud code superiority over most other harnesses. And so, uh, you know, here it describes various different ways to work on longrunning coding projects and manage environments and stuff like that. And so, obviously,

[42:00] this is something that's like very fundamentally baked into cloud code. If you want to understand cloud code in an advanced level, uh, you can't get better than getting it at a harness level. Okay. So, you know, obviously this is a

[42:09] cloud code course. This is not another harness course, but you should at least know what agent harnesses are before you proceed to the rest of the course because you know the more understanding of harnesses you have, I think the better you'll be able to appreciate and then digest and ultimately execute on what I'm about to show you. Next, I want to chat a little bit about parallelization, about things like agent teams, about sub agents, and a couple of other ways of distributing work uh to minimize the amount of time and effort that goes into things while also increasing the quality of the output.

[42:37] Okay, so I say agent teams here, but let's start with parallelization. A big question that I think a lot of people have is, well, first of all, what the heck is parallelization, which is just doing multiple things simultaneously instead of waiting for uh sequential things to finish. And then the second one is like, Nick, why the hell should we paralyze our agents to begin with?

[42:52] And to that I say, have you ever, you know, sent a longunning task request to cloud code and actually had cloud execute on something for more than a few minutes? For the vast majority of the time, you're just sitting there twiddling your thumbs. Twiddling your thumbs is not very economically productive. So if I have ways to not

[43:05] twiddle my thumbs, I will do so. And I really I guess mean is that autonomous agents just take a long time to finish tasks. You know, when we started with this stuff, or at least when I started with this stuff last year, you know, Claude could realistically work on things for 30 seconds. The other day, I

[43:19] had Claude work on something for over 15 minutes. And so, if all I'm doing is just sitting there waiting for it to do this 15-minute task, you can imagine that my productivity is basically going to be punctuated by me just sitting around watching it. It does something, I get the result, make some minor changes, wait for another 15 minutes, and so on and so forth. that's not very efficient.

[43:36] So, parallelization allows us to reduce the total amount of time by a factor of at least a few from 15 minutes to maybe a couple minutes. So, it'll be able to work on smaller, more more self-contained things. Um, but two, it'll also just get higher quality.

[43:48] Another thing is that many tasks feature independent steps that can be broken down. So, for instance, let's say I'm doing some sort of task. Okay? And this

[43:54] is just like how long it would normally take if we go serally. And so the option A is just to do what most people do, which is where they'll do, I don't know, they'll do step one, and then they'll do step two, and then they'll do step three, and then they'll do step four. So that's one, two, three, four. This task

[44:11] over here takes 5 minutes. This task over here takes 5 minutes. This task over here takes 5 minutes. And this task

[44:17] over here takes 5 minutes. What's the total amount of time kind of collectively? Well, it's 20 minutes, right? So that's sort of a um you know,

[44:24] the serial way that most other people do things. Well, guess what? Turns out a lot of tasks don't need to necessarily be like that if I just copied all of this stuff over.

[44:33] Okay. And then instead ran a couple of these in parallel. So I actually had uh I don't know three of these simultaneously and then kind of combined all of them if I did something maybe more akin to this instead. Hopefully you

[44:45] guys could see um now okay instead of everything taking you know 5 minutes 5 minutes 5 minutes and 5 minutes maybe what I'm capable of doing realistically is this takes 5 minutes. This takes five minutes. And then the integration step about these three which were two, three, and four only takes two minutes. So what I'm

[45:04] doing is I'm basically converting a task that previously took 20 minutes and I'm turning it into one that took 12 minutes, which you know, if you just did a little ratio 12 over 20 is equal to 3 over 5. And so what I'm capable of doing is getting it down about 40% about 60% of the total. Hopefully you guys see when you have tasks that can actually be broken down in this way, aka a task that you can expand and run simultaneously through some form of parallelization, just makes more sense to do all three of these things simultaneously rather than one parent agent being responsible for everything like doing one then doing two then doing three and doing four. What we

[45:36] can do is we could take two, three, and four, stack them on top of each other, add an additional step five called a synthesizer, and then take the results of these in and do it do it in like a fraction. Um, another big reason is that agents are what are called stochcastic, aka they don't always return the same answer. So if I ran, you know, Claude five times on basically the exact same thing, every single time I have a slightly different response. Okay, every

[45:58] time I have a slightly different response. And just to show you guys what I mean by that, I'm going to open up um my Claude code over here. And I'm actually going to open up three different tabs. Let me just visualize

[46:06] this. Stick this right in the middle. Okay. And then over here, let me just

[46:09] make sure that all these are operating the same. I'm going to say, I'd like you to determine five ways to improve this codebase. I'm just going to paste this across all three of these. I'll paste and I'll

[46:19] paste. Now, I'm just going to run all three of them. And I just want you to notice sort of what's going on here.

[46:24] Obviously, the first thing it's going to do is try reading the key files. But check out the different uh solutions basically that it's coming up with on all three of these different runs. So on the first run, okay, uh, brokage im broken image paths, missing title and metatags, nav links hidden inside mobile with no replacement. Project cards

[46:42] aren't actually links. No keyboard focus styles or skipped to content link. The second one was broken image paths, missing metatags, no mobile nav, but now look, placeholder links everywhere, typo in footer. Okay, and you can see that,

[46:54] you know, basically the more times we run these uh, you know, agents and then the further away they get from the beginning, the more they tend to diverge. And there's a statistical reason for that, right? Like at the very beginning, this is sort of like um I don't know the total answer. At the very

[47:07] beginning, you know, red is pretty similar to black, but eventually it diverges a fair bit. Green's similar to red, and it diverges a fair bit. Blue is similar to all these, but it diverges a fair bit.

[47:20] And I guess the point that I'm trying to make is like, you know, over here, uh let's pick another color. So, it's pretty obvious that these are all bit different. We'll do purple. over here.

[47:29] These this is sort of like the zone of similarity, right? But then after you make it to a certain point, uh because of the multiplicative nature of how large language models work under the hood, they're basically multiplying the statistical probabilities of like one token after the other after the other after the other. Um you have massive divergence in the end result. And so you

[47:47] know this might go ABC, this might go B C D, this might go AB, this might go ABC, and this might go a CQ or something like that. What you can do is you can actually just run five times. And now notice if I ran this once, I'd only get ABC. But because I've ran this another

[48:05] time, I got all the way to D. I ran this another time, I got all the way to E. You know, if you just count up all of the different unique answers here, I have A, I have B, I have C, I have D. I

[48:13] also have E. I even have Q. And then I have zed. So you can see here that like

[48:17] I'm basically getting 2.5 times the total number of possible answers by running things multiple times and then just averaging out and taking all the unique outputs, right? That's really the the principle of stoasticity because they don't always return the same answer. If you parallelize your agents,

[48:30] you can actually run multiple times with the same or similar queries and then you can actually have different answers given to you that just sort of live outside of the distribution uh or average run, which is pretty amazing. So, I'm going to show you guys how that works specifically with um debate and stochastic consensus models. If anybody's seen my agentic AI course on that, you'll know more or less what I mean by that. I'm also going to show you

[48:50] some fan in fan out um researching flows as well as some some sequential pipeline handoffs. Uh but really the the fourth and final reason is because model performance degrades as context increases. So the shorter and the cleaner your context windows are typically the better the results are as well. Uh what I mean by this is you know

[49:06] because the parallelization aspect typically involves sub aents which I'm going to show you guys a little bit about. You get to avoid the problem where the increasing length number of tokens um leads to poor performance. And so, you know, if like on average, this is more or less the relationship between the number of things in your context window and then the performance of the model, uh, we are going to we're going to end up just almost always staying right around here, which is the zone of good. By the way, I just made that up.

[49:31] It's not actually called the zone of good. Hopefully, you guys understand the distinctions there, though. Um, when you parallelize and then feed tiny chunks of a problem to multiple agents, they can all be at the zone of good. You don't

[49:40] actually have to like go all the way down here. It's not just one agent that's doing all the work. Okay. So, so

[49:45] what are examples of how to parallelize in the first place? Well, there's like a built-in function called agent teams now in cloud code, which does a fair amount of this. So, I'm going to be showing you guys some ways to do that, but I just wanted to chat a little bit more generally without even going into agent teams first before I show you some demos um of like different ways that I personally approach problem solving. And

[50:02] I've seen some of the best and the brightest use cloud code for this sort of parallelization. And I'm going to call them common team patterns. Okay. Um

[50:10] essentially, there are three main things I want to cover. The first is the ability to fan out and then fan in. And so that's where you actually spawn a bunch of different research sub aents.

[50:19] And then you have a synthesizer sub aent which takes all of their outputs. And then um based off of the outputs of that synthesizer, you can do either more fan out fan in flows or you could do some form of final synthesis step. Okay.

[50:32] Okay. So what I mean by that is like let's say before you have a query and it's you know I want to find the best okay absolute best APIs for my feature whatever the feature is it's X feature I don't know it's like some app that generates things whatever so I want to find the best APIs out there for this feature that you know allow me to very quickly and easily do the things that I want to do. Well, you can imagine like if you were to do this um in the old school linear path, what would happen is claude code would spin up, okay, in the same thread research on site number one and then go on site number two and then go site number three and then go on site number four, right?

[51:13] And what would be occurring the entire time that we're going through all these different websites? Well, the length of our total contacts would increase, meaning our performance on average would also decrease. Okay. In addition, it's

[51:25] taking time. So, it's five minutes here, it's five minutes there, it's five minutes there, it's 5 minutes there, and so on and so forth. Then, at the end, what it would do is it'd have a final synthesis step, which I'm just going to call S, which would basically combine 1 2 3 and four together, which could take a certain other amount of time, maybe another 5 minutes before finally giving you your answer. And so the cost of the

[51:44] answer, okay, if you think about it as like almost like a line item, the cost of the answer is, you know, first of all, 25 minutes, which is obviously non-preferable to instant. And then, you know, a fair amount of tokens on poor quality outputs. you know, you're probably going to end up spending a similar amount of tokens regardless, but you're spending those tokens on poor quality outputs because you're kind of you're kind of down here as opposed to up here, right? You're

[52:13] you're here where you don't want to be. Now, what fan out and fan in is is very similar to what I showed you guys earlier. You have a research query and that's, you know, find best APIs.

[52:24] And so, what it does is cloud code basically goes in and then immediately spawns. Okay, let's just say four research agents. And so now we have research agent one, research agent two, research agent three, and then we have research agent 4. Okay? And so what

[52:42] we're doing is here is we're we're we're fanning out. These all operate totally independently, accumulating their own context windows. Because they're new agents, they're almost always in the zone of good. Maybe

[52:54] they'll push a little bit farther beyond that, but they're still pretty good. Once we're done with that, what we do is we do the opposite, which is the fan in, and we feed all of those into a final synthesizer agent. That synthesizer agent now has a different prompt. The

[53:09] prompt is not, hey, go do this research. The prompt is, hey, here's a bunch of context from a bunch of other models that have already done the research. Meaning, the prompt gets to be shorter.

[53:17] We then apply highle reasoning strategies and principles to make that a synthesizer as smart as possible and say things like we want you to integrate um anything that overlaps as well as any outliers and then score them slightly differently. And so, you know, rather than being all the way over here with our big thing, you know, probably we're somewhere over here in the middle, which means the performance is going to be a little bit better. And then obviously the synthesis step can occur in approximately the same amount of time as the actual research because you can spawn almost an infinite number of sub agents to go do research for you. And so

[53:43] really what happened now is you have 5 minutes here, you have 5 minutes here, you just add these up, it's 10 minutes. And so not only are we significantly faster, we're also a lot higher quality because now we have all the the data and information laid out to the synthesis agent. More importantly, there are different models that are better at different things. And so within Claude,

[54:01] you have not only your, you know, heavy lifter, which is usually the opus models, but you also have, you know, your sonnet models. And then although not a lot of other people use them these days, you also have your haiku models. And so what you can do now is for the research which consumes a massive number of tokens but realistically doesn't usually need like a ton of reasoning for it. It's more of like data extraction

[54:20] you use something cheap like haiku and sonnet. And then for the synthesis you use something like opus because you're applying different models at different steps. Not only is it um going to going to occur much faster cuz sonnet works faster than opus. So maybe instead of 5

[54:34] minutes here, it's actually I don't know 3 minutes. But then the cost is going to be a small proportion of the money that you normally would have spent just because of the way that pricing on claude works, right? Pay attention here to the fact that claude opus, you know, in this case 4.6 is five bucks. Sonnet

[54:48] 4.6 is three. So we immediately save 60% right there. And that's just your base

[54:53] input tokens. That's not taking into account um you know, like the the the the massive difference in also output token cost and so on and so forth. And obviously things get even better if you go down ha coup and and so on and so forth. And so you can formalize this as

[55:05] a skill if you would like. Okay, I'm not going to I'm just going to feed it in a simple prompt, but um this will illustrate what I mean. Let's say I'm right over here in my project. Okay, let

[55:14] me just delete this um global cloudmd because we don't need that anymore. Then I'm going to essentially let me just go back here and then copy the actual text. I say use a fan out fan in and researchers synthesizer approach to research the question how best should I optimize this codebase minimum five sub aents use sonnet to do the research and contemplation individual contemplation opus to synthesize so now what's going to occur is rather than us just waiting non-stop for all of these what this is going to do is it'll fan out six sonnet research agents. Each

[55:56] are going to investigate a slightly different optimization axis. They're all going to focus on slightly different things. Then they're going to synthesize all of those results back together with Opus. If I zoom out, so you can actually

[56:05] see all six of them running simultaneously. Despite the fact that we're not using this agent team feature, we're just using the um sub agent feature right now. Uh you know, all of these things basically immediately are generated.

[56:15] Their contexts are quite short. So I mean in the grand scheme of things, this is a much shorter context than we would ultimately accumulate in our main agent. All of them are focused on slightly different things which are obviously autonomously managed by that orchestrator. And then finally, these

[56:27] six agents can finish in a linear amount of time as opposed to you know like multiple one. So this just finished the architectural research. It's going to wait for the remaining five agents now.

[56:35] All right. And it looks like it just finished all six research runs. So now it's going to synthesize all the findings with Opus. It's then going to

[56:43] also be able to take advantage of things like its planning features and so on and so forth before synthesizing. And here it is. Okay. High impact, easy fixes.

[56:51] gives us a big list. It's also writing the um high to medium impact, easy to medium effort. And so, I mean, you know, obviously um I'm not just pulling this out of my my ass here. Um Anthropic has

[57:01] done a lot of research on the best way to solve problems. And um you know, Opus with a bunch of sonnet sub aents massively outperforms opus both on time, but then also quality specifically because of, you know, sonnet's longer context window as well as just like general usability. Um that's what I care about. I just care about my own

[57:17] usability here. I could spend as much money as I want on these things at this point. What I care about is like how can I extract the maximum quality with the minimum amount of time and that's the design pattern that you want to use. So

[57:26] I mean like use this anytime you're contemplating problems and you don't just have to contemplate like specific API problems or development problems as well. Like I use stuff like this anytime I'm designing um business systems, anytime I'm designing process optimizations. I mean I did this the other day when I was doing product differentiation. Basically coming up

[57:42] with different ways to price and package products for a company that I now own that does this sort of thing. The opportunities here are basically limitless. You do this for competitor research. You can do this for whatever

[57:52] the heck you want and I I commonly apply it. Okay, so that's fan out and fan in where you basically spawn and researchers usually using a cheaper dumber model like sonnet and then you have a a larger synthesizer model that actually combines the results. Um that's how you get you know some of the best quality and then also the best quantity.

[58:10] Next, I want to chat debate and stochastic consensus because it's kind of similar similar but um you know it's also a little bit different. I use debate and stochastic consensus to basically like hammer out nuanced arguments and nuanced quality discussions. You know earlier how I said we had one agent come up with ABC, another one come up with CDE, another one come up with like ABQ and so on and so forth. Well, basically with

[58:34] stochastic consensus and then later debate, what we're doing is we're having different sub aents come up with different um lists of solutions and then we have something else go through identify all of the mode identify the mode which is the uh frequency of you know the the number of times that a solution pops up. So let's say solution A pops up twice. Okay, this synthesizer agent would say, "Okay, there's two A's. Uh, B pops up twice, so

[59:04] we'd go 2 B. C pops up twice. We go 2 C.

[59:08] D pops up how many times?" One, so we'd go D. Then counts E. That

[59:14] also counts Q. And so in this way, you could see statistically speaking, uh, you know, a lot of agents think these three are great solutions. One agent thought this was a good solution.

[59:23] Another agent thought this was a good solution. And finally, another agent thought this was a good solution. basically the votes of confidence here are fewer. And then what you can do is

[59:30] you could use this. It's almost like um like a weighted average to tell you what approach to take. You know, if it's like an equation where like my final uh I don't know decision, which we'll just say decision is kind of like this. It

[59:43] would equal 2 a + 2 b + 2 c + d + e plus q. And I know this is math, but don't get scared here. The point is not to actually calculate the final solution.

[59:54] The reality that I'm attempting to convey to you is that because so many models came up with A, so many other models came up with E and B and Q and so on and so forth, you can quickly determine consensus between a number of agents that come up with ideas. And then you can also determine which ideas are genuine outliers in so far that you know only one out of three models actually came up with this thing. One out of 24 four models suggested you should do X, Y, and Z thing. And so you get to farm

[1:00:23] both like the statistically most likely answers to solutions, but also like the massive outliers which can make you quite um I want to say competent at solving problems in a very short period of time. And this works in a really similar way to what I talked about earlier with like the total solution space, right? You know, if uh there are really a fixed number of ways to solve something and the reality is there are a fixed number of ways to solve something and there also a certain number of ways not to solve something. Well, what you

[1:00:48] want to do is you just want to like cover that ground as quickly as possible. And in reality, what you could do is you could quickly spin up an agent to do all of to figure out all the ways not to do something. Okay? And then you

[1:00:58] could have, you know, one sub agent slowly figuring out, "No, this doesn't work. No, this doesn't work. No, this doesn't work." All simultaneously. And

[1:01:05] then what you end what you end up with is you just end up with like this beautiful field of like highly differentiated green which tells you what you can actually do. And I understand this is more conceptual, but just bear with me here. I'll show you guys an actual example in a moment. Now,

[1:01:18] stochastic consensus is cool as sort of like a first go, but debate is even cooler because now what you do is you basically take all of these points, okay? And then you feed them into an open like conversation or chat room where all other models can weigh in on solutions that might not actually be very obvious. So now, okay, if I just recreate this solution, we have agent one come up with ABC. Agent two come up

[1:01:42] with BC, I don't know, let's just say E. Agent three come up with ABQ. Okay, what we do is we divide this into time steps.

[1:01:50] And so this is time one, this is time two, this is time three, and this is time four. What we do at every time step is we allow all other agents to look at all of the uh conversations and and all the thoughts that all the other agents have had. Okay? And what occurs as we

[1:02:06] move through is agent one gets to see agent two and agent 3's responses. And so it gets to differentiate. Maybe now it goes a b c e zed because it comes up with some additional solution by comparing its two, you know, two and three. Maybe this one comes up with bc,

[1:02:21] but then it eliminates E because it just doesn't think that made much sense and then it comes up with an F. You know, this one comes up with with uh I don't know, two different letters and then ends up uh you know also identifying some of the previous solutions, but then combining them in new ways and stuff like that to come up with better ones. And so what we do with a debate is it's not really a debate in a practical sense. It's not like, hey, your job is

[1:02:41] to try and convince other people why A, B, and C are the best solutions. What it is is every model has access to all of the other models. And so, because they have access to all of the other models, and they don't have to spend all that time reasoning, they can just see the results. They can then incorporate those

[1:02:54] and come up with increasingly nuanced uh solutions and, you know, ultimately span a large search space in a very short period of time. And so, we can just proceed with this all the way down. You can run as many of these like steps as you as you want until ultimately you have like a a list of solutions provided by a bunch of different models that are just way more complex, way more nuanced, and also just like way more interesting than the initial ones that you know one agent might have come up with. All

[1:03:18] right, so I'm back on my business workspace here and uh we're still doing research on toatillos, but I thought this is actually a pretty good example. Why don't we use stochastic multi-agent consensus to come up with all of the different ways you can make a sauce using a toatio. Use stochastic multi-agent consensus to determine all of the different ways that you could make a nice tasting sauce using tomatillos. I want every agent to come

[1:03:38] up with at least 10 independent responses then have them synthesized and turned into just a giant list of all of the possible things you could do. So what this skill stocastic multi-agent consensus does if I open it up is basically it breaks down a query into n other queries. That's where it says spawn n agents with the same or a slightly different prompt to independently analyze a problem. Then

[1:04:03] aggregate results by consensus which you use for decision-m ranking options strategic analysis or any problem where you want to filter hallucinations and then surface what are called high variance ideas. So anytime I use the word consensus poll agents stochastic consensus spawn n agents so on and so on and so forth it'll go and it'll it'll do the thing. So, just scrolling down here, you can see that it read through the skill and it spawned 10 agents all looking at slightly different angles here. And you know, these are very

[1:04:30] similar prompts. Brainstorm all the different ways you can make a nice tasting sauce using tomatillos. This one's here. Brainstorm all the different

[1:04:36] ways you can make a nice tasting sauce using tomatillos. This one here, brainstorm all the different ways you can make a nice tasting sauce using tomatillos. But the idea is, you know, one is a conservative tradition-minded chef. The other is an adventurous

[1:04:47] boundary pushing chef. The other challenge is conventional wisdom. The other reasons from first principles and so on and so on and so forth. Now

[1:04:54] because you know this is a pretty simple and not very intellectually difficult exercise. All 10 agents have actually already already finished and you can see that I was able to scan a massive search space in a very short period of time despite the fact that this problem is pretty simple. So what it's doing is similar to what I showed you earlier with those n researchers and then um having some sort of synthesizer model.

[1:05:11] What this is now going to do is indeed duplicate the outputs and then give me a list of pretty nuanced answers that realistically scanned most of the search space in a very short period of time. I'm sure you can imagine you could scale this up if you had like some sort of dedicated infrastructure whether it's a local mod or something like that. You could theoretically have stuff like this running all the time just ideulating and coming up with new approaches to solve um long-standing problems. And this is

[1:05:33] actually the exact way that I don't know if you guys have seen uh you know they're throwing opus now or GPT 4 point or GPT or other models at like these big math questions and asking them to solve them. This is exactly how they're doing them all under the hood. So as you guys can see we've pulled 10 agents. There

[1:05:48] are 119 raw ideas counting for duplication. There are 52 in total that are new. So we're going to do is we're actually going to look at this consensus report and then ultimately its answers.

[1:05:59] All right we have the consensus report. Opening it up here. You can see there are 52 total. The first is salsa vera.

[1:06:06] The next is tomatia avocado crema. The third is aguile verde and so on and so on and so forth. I could work my way all the way down here. A bunch of different

[1:06:13] types. You know, I could have had one agent come up with all of these. I could. Okay. But um the probability that

[1:06:18] I would have been able to one come up with like a highly differentiated list like this and two scan as much of that search space in the same amount of time is very low. And so I'm sure you can imagine you can apply this to any business problem that you guys are currently having to just come up with a bunch of lowhanging fruit solutions as well as like unique and and and outlier solutions as well. We even have like Indian influence sauces, Persian influence sauces, Caribbean Latin fusion sauces and so on and so forth. An

[1:06:41] outlier that I'm definitely not trying anytime soon is total blanc, which is French butter sauce using tomatilla's pectin as a natural emulsifier. No thank you. So what would debate look like?

[1:06:51] Debate is more or less the exact same idea. Um, in my case, I've just turned this into a skill. It's called model- chat. Basically, what occurs is we spawn

[1:06:59] five claw instances in a shared conversation room where they debate, disagree, and converge on solutions. We use roundroin turns with parallel execution within each round that triggers on terms like chat and so on and so forth. So, I'm going to do here is I'll say, great, this looks awesome.

[1:07:13] I'd like you to rerun this, but with model- chat, make sure at least 10 agents are having conversations about this. And then uh you know if any of the sauces just sound insane or terrible or crazy then obviously have them discuss that as well. Just like our stochastic multi- aent consensus took advantage of like time basically and traded it off against total tokens. We're doing the

[1:07:32] same thing. So we're going to do is we're going to start by extracting from the user's me from the user's message the topic or problem the mode the number of agents and the number of rounds. It's then going to run an actual script that I've set up here that automates the process of like having each of the agents look at each of the other agents responses before finally doing a synthesis. Speaking of which, I just

[1:07:50] read through a couple of those and I'm actually just going to make some toss right now. So, I'll be right back. Okay, so me looking at the conversation over here, just asking it to like give it to me. Actually see that all the agents are

[1:08:03] doing some thinking and the contrarian is starting with 15 ideas. It'll immediately challenge the ideas that deserve it. They're now listing their disagreements. So, does this actually

[1:08:12] work? Is it a structurally sound technique or a restaurant stunt with an unacceptable failure rate? Is tamarind redundant or complimentary? You know,

[1:08:19] does tomato chocolate belong on the list? If so, where should mole verde be in tier one or tier 2? So, they're having discussions on an ongoing basis, which is um always really fun to watch that we can monitor and then obviously synthesize into an answer. Okay. And

[1:08:34] then finally, we have the tomatio synthesis over here. Um, toatio's pectin content is underappreciated. Tomatio husk tea unfortunately is not cool. The foundational tier is subtle

[1:08:45] and non-negotiable. And I actually look at the foundational tier. You can see we actually have a bunch of different highly recommended sauces. Again, some

[1:08:53] of these are very like nuance. Lacto fermented tomato hot sauce, tucker squeeze bottle drizzle, enchilada sauce, tomatio agua chile, and so on and so on and so forth. And you know I this is just a really shitty example but hopefully you guys understand that you can take this to more or less anything that you want. Um whether it's you know

[1:09:09] designing a new computer programming approach to a particular problem whether it's choosing the right framework to approach or tackle a task with or something else. Okay so I just did all of the previous example using a pretty straightforward um you know like dietary or chef sort of example. But now I want to use this on an actual app and really just have all of these different models discussing things and doing so in a very short period of time. What I have here

[1:09:33] is I have like an algorithmic art example and this is actually something that Claude developed. It's part of their algorithmic art base skill which I think is actually like applied or supplied I should say in um the anthropic anthropic skill directory. Uh you can adjust some things like the the stroke weight and like the damping and so on and so forth and actually have it like come out with very unique designs.

[1:09:54] So you can then just like save the image and then boom, now you have like a cool like wallpaper or something like that. It's kind of neat. U but I want to I want to improve this as much as humanly possible. And the reason why I'm doing

[1:10:03] it like this is because I also want to show you guys how to apply the same approaches that I just showed you to agent teams instead, which are obviously a much um more streamlined version of doing the exact same things that I've done so far. It's just streamlined in the sense that, you know, it is built out of the box to do everything, but it does so at the cost of some tokens. So, I'm just going to go back over here and then I'm just going to look at synaptic drift.html within art. I just need to

[1:10:25] make sure to, you know, remember what folder that's in. Then I'm just going to open up another cloud instance. Now, a lot of the advanced stuff as we know is actually only available in the terminal.

[1:10:33] And I think agent teams are a lot better managed in the terminal. So, I'm just going to open up the terminal. I'm going to full screen it here as well. Let me

[1:10:39] delete that and then go full screen. And uh, you know, I could do it in here. I could also do it in like ghost tty uh which is probably my favorite like terminal to use within cloud. But for

[1:10:49] now um you know I I have my agent teams idea. So I'm I'm basically now going to say hey I'd like you to optimize synaptic-drift.html and turn it into a full-fledged application. However, rather than just

[1:11:02] do this all naively yourself, I want you to take advantage of stochastic multi-agent consensus. I want you to take that skill and then apply it using the agent teams feature. you'll orchestrate a team of agents that do all of this stuff. Don't just use what's in

[1:11:15] the skill itself because that would be running it a little too simply. I actually want you to to read through the whole skill and then use that to spawn agent teams. Okay, so it's going to start by reading the skill def and then the HTML file itself which is found in ART. It's then going to go and read

[1:11:28] through the agent teams tooling and everything that it needs in order to basically spin this up easy. So it'll start by creating a team for the consensus workflow, spawning 10 analyst agents with different framings, then finally aggregating their recommendations and implementing the winning features. So the very first thing it's going to do is spawn the analyst agents. And you can see now the

[1:11:47] UX has changed a little bit. You see down at the bottom where I have these different analysts that are running. So if I go shift down, I can actually see all of their different stochastic multi- aent um kind of consensus threads. So

[1:11:58] now they're all spawning and running in parallel, which is pretty neat. At any point in time, I could press enter to view sort of the conversations and what they're doing. And I should say I I should note that um you know the stoastic multi- aent consensus applied to agent teams is basically just the debate built in because the agents actually can can communicate. Um the

[1:12:15] team lead can also orchestrate that communication too. So you know it's not actually um really independent which is neat. Uh you could spawn all of these in like different windows if you want to.

[1:12:24] You can also just continuously hold shift and then go up and down to select. What I'm doing is I'm just reading through a bunch of different threads and conversations. And it's clear that they all start by just reading through synaptic-drift. HTML. Um, finally, uh,

[1:12:37] you know, this is now returning a bunch of agent conclusions back. And more importantly, it's also coming up with consensus, which is nice. All right.

[1:12:44] What it's going to do is just take all these now and close them down while also um looking at the consensus, the bugs, the divergence, and then ultimately the outliers. So, the consensus recommendation of our next feature is high-res exports, a preset system, URL state, and sharable links. The bugs are the race condition and regenerate download saves mid-render, PG height not checked. Uh, divergence is one or sorry,

[1:13:09] six out of 10 agents suggest debounce regeneration versus a live preview. Then the outliers have also come in. Mobile responsive layout, live animation mode, seed history, web worker offload, mouse attractor, repeller, and kill sidebar overlay. So, this is all really cool.

[1:13:23] You can see now it's coming up. It's actually just deleting my old tomato stuff. I guess we happen to be using the same file or something. Instead, it's

[1:13:30] coming up with this giant list of different conditions and features that it can build. Okay, now it's actually shutting down all the agents implementing it. Um, just because I want this to do so faster, I'll say use agent teams to do the implementation. And you

[1:13:42] can see it's actually gone through here and then um added all of what we needed in order to implement the tool, the features that the model suggested. In addition, it's also spawning review agents to see if we can improve the quality of the generated code, spot problems, and stuff like that. So, if I go shift down, I could see all those.

[1:13:58] So, we have now reviewer bugs, reviewer features. Let's just see what reviewer bug says. Okay, it's now sending the review to the team lead. So, it's

[1:14:04] communicating that back, taking a look at what the reviewer is saying now that it's opening it up. You can see we now have a ton more features. We have different presets. So, ocean drift,

[1:14:13] ember storm, ink wash, neon plasma, neural fire. We have the ability to modify colors. We have 1x, 2x, and then 4x downloads, which I don't think you guys could see because my face is in the way. But if you just um look down over

[1:14:27] here, you'll see that there's significantly more functionality. Um we can download a PNG at 4x as well. We have simple like space bars to reload and change things. We could change the

[1:14:37] the speed and so on and so forth. Um ultimately, this is just a better app, right? And so we did this by basically just exchanging a couple of my dollars and tokens for, you know, a bunch of different agents, all coming up with their own ideas and then ultimately executing on them. Hopefully you guys

[1:14:51] could see you can apply the same approach to more or less anything. There are obviously optimal token trade-offs, but um when you spawn the sub aents that are a little bit less capable, um like sonnet versus opus, typically that math works out and you end up being able to do just as much if not more in a shorter amount of time for less money. All right. And then finally, pipeline, which

[1:15:07] is sequential handoff between specialists. I mean, I just showed you guys a little bit of that earlier with um agent team sort of spawning review bugs and stuff like that, but basically that's more or less it. You have task A done by some agent which is specialized for task A. You then pass that off to

[1:15:22] agent B which is specialized for task B and then ultimately agent C which is specialized for for task C. And so I mean like you could just have A do all three of these things. The issue with having a do all three of these things though is one um if you guys remember earlier, good lord, this is getting a little messy. You know, we're no longer

[1:15:40] in the zone of good because odds are it has like tons of context from literally everything that it's done before. So, you know, like it would have started off over here and that would have been okay, but now it's over here and then now it's over here. And then two, like you sometimes fast and and and good development is often at odds with like really in-depth testing, let's say. And so if you think

[1:16:00] about it conceptually like a a developer agent will have different incentives than like a testing agent. The developer agent will be incentivized to like build things that works really quickly using you know whatever is available to it. Whereas the testing agent will be incentivized to try and like spot all of the issues. And so like building things

[1:16:17] new is sort of at odds with like repairing the old things. And in that way, if you try and have one agent do everything, the probability that it will be able to do it as well as possible versus if you just spun up specialized agents that were like highly tuned for that thing, assuming their intelligences are all held equal here, I'm talking about like non-stop opus calls, not opus sauna and so on and so forth, is is definitely different. So my recommendation would be, you know, like what I would do is I'd have like a dev agent for A like I just did. Then I'd

[1:16:46] have some form of like bug fix for B. then it' have some sort of like test maybe bug in Q&A. And I'm not going to redo that example because one, I want to be respectful of your time, but two, I just showed you that exactly with the agent teams example. Um I guess the meta

[1:16:59] example here is you combine all three of these and then um just have all of them interacting constantly for best results. Like you have, you know, debate and stochastic consensus to come up with like the best ways to, you know, improve on a product. Then maybe you do some fan out, fan in, and researchers to go look at like different APIs and different design patterns that you could use to fulfill that before finally handing that off to some sort of like bug reviewer, QA or tester. Uh but hopefully it's

[1:17:23] clear that yeah, all of these things do not exist in isolation. Uh they all exist together. Next, let's talk context management, which put really simply is just all of the files and folders and organizational methods that you put into a workspace to allow claude code to effectively manage whatever work you have. Now, I'm seeing

[1:17:44] a lot of people try and delegate work right now, sort of like human companies do with CEOs, you know, CTOs, CMOs, uh, claude coder agents and software engineers and stuff like that. And I think initially when I looked at this, this one's called Paperclip specifically. It's got a pretty interesting repo that you can check out right over here. It's all about running

[1:18:07] your whole business with our agent team. I think initially it's really easy to look at these and be like, "Okay, this is stupid." You know, I mean, that's that's what I did. I uh made a couple of

[1:18:15] videos and I talked at Nauseium with a couple of my friends, and I was like, "This is dumb. Why would we try and fit agents, which think very differently than human beings, into the exact same organizational hierarchies we've been using for the last 150 years? Just doesn't make sense. Human brains are

[1:18:26] different than agent brains." The latter is obviously a lot more spiky and good at certain things while sucking at others. But anyway, so as as quick as I was to initially dismiss this idea, what I've come to realize is that sub aents as these org charts and skill.md files,

[1:18:41] which as we know are self-contained SOPs that exist within a file capitalized skill and MD, these are actually just two flavors of the exact same thing. What they are is they're just different ways of organizing your markdown files. And so just like in my case, we ran a model- chat skill earlier for me to show you guys how, you know, models debated and stuff like that. Okay, we had a

[1:19:04] skill.md within it that stored a bunch of information that was like hyper specific to that skill. We had model- chat.py, which was a tool that this

[1:19:12] skill could use. So too are our sub aents organized in basically the same way. I guess what I'm trying to say is like, okay, if we take sub agents on the left hand side, what was one of the main reasons why we like using sub aents?

[1:19:24] Okay. It's because it's a clear or fresh context window, right? All right.

[1:19:31] Awesome. So, that's one. How about the fact that it's specialized? Awesome.

[1:19:35] That's another How about the fact that the sub agent is probably more reliable at sub agent specific tasks, right? That's another one. And then how about the fact that it's written in, you know, markdown format with tool use? Well,

[1:19:48] fantastic. That's another one. If we look at like how that equates to skills, honestly, the only thing that's missing is the fact that the context window is not entirely clear or fresh. But you

[1:20:00] know what you can do with these is because skills are so efficiently written, um they're basically a form of compression that pushes you towards a shorter context window anyway. So basically the only real difference if I'm honest, and keep in mind like when you instantiate a sub agent, you're giving it, you know, a little prompt, right? kind of similar to the way skill works. The only real difference between

[1:20:20] the two is just the amount of context in the sub agent versus the skill. But I want you guys to know that sub agents are honestly basically skills and skills are basically sub agents. They're just slightly different ways of storing information. So why am I bringing this

[1:20:32] up? Um just because I'm coming to realize that the two are the two are very similar and they're soon, I'm sure, in the future going to be like merged even more so into a similar concept. Um all these two point at are just different ways of organizing your context and basically organizing the way that you you get tasks done. one

[1:20:48] delegates via CEO to CTO, CMO, CTO, all all the stuff, right? I don't know why there's two CTOs now that I'm looking at. That's kind of weird. Whereas the

[1:20:55] other one stores things in a skilled dynam like just going back to anti-gravity right over here, right? Like I could go to this skills folder and then I could go and find that model- chat. And I mean like the way that this is written is basically the exact same um you know schema basically that a sub agent is written in. You know, if I go

[1:21:11] over here to Claude Code's actual documentation page on sub agents. I mean, you actually have basically the exact same structure. See how here it says the title, code reviewer, description, prompt, tools, model. Okay,

[1:21:23] you see over here, what do we have? We have the name. Okay, we have a description and we also have the tools.

[1:21:27] I mean, like the model is sort of baked in here because it's in our main thread. It's going to be open 4.6. But hopefully

[1:21:32] you guys are seeing like skills and subent actually similar. They're just slightly different ways of organizing information. So, I'm making this big point because I think that's important to realize as we continue moving forward with cloud code and other tools and we get more and more advanced with them.

[1:21:44] Um, the shapes of how we're transmitting information to our models will likely end up being quite quite similar. Whether one person decides to use a paperclip style big fleet of agents that does XYZ, which maybe, you know, just a couple months ago I might have looked at, scoffed and said like, well, that doesn't do anything. Um, you know, so too are skills basically that the same thing. So the model intelligence is

[1:22:04] growing more and more and more capable within the harness which is what allows the the development of these really interesting organizational hierarchies. So what are some of these organizational hierarchies? Well, I've already shown you paperclip here. And the way that

[1:22:13] paperclip works or rather it's supposed to work is this is like a dashboard which um somebody developed that you know I think just praise off of maybe praise isn't the right word but it uses people's misunderstandings of how agents work. Um it equates them in anthropomorphizes then makes them seem really similar to humans and then it puts this in front of you so that you feel like you're running a whole team. And so in this way clearly it's broken down by role, right? Whereas the average

[1:22:34] skill is not broken down by role. The average skill is broken down by function. Um also skills typically don't delegate to other skills. That's really

[1:22:41] the main difference. But paperclip isn't the only one that's like this. Here's another good example. Company helm. This

[1:22:47] one over here is a very same similar sort of idea where you basically have an AI studio. Within the AI studio, you define a bunch of different roles for your agents and so on and so forth. And then that's ultimately what allows you to manage your projects. This instead of

[1:22:59] being left to right is obviously, you know, organized a little bit differently of a front-end builder, a QA runner and so on and so forth. How about open goat which is the AI autonomous organization of openclaw agents. Again, you know, it's doing this with like CEO, head of sales, customer support-based organization, which I don't really believe is ideal. I don't really think

[1:23:16] you should have this level of direct reports. I mean, like, think about it. Why? All of these could just be Opus

[1:23:21] 4.6. They could be way smarter. They

[1:23:23] could pull from some sort of shared context pool. And I think you really wouldn't leave that much out. uh but it is an interesting approach. This one

[1:23:29] over here is called the system which is uh obviously using some sort of AI generated diagram here but it's 26 specialized a agents which we've thought about that do architecture, design, product development, release, operations and so on and so forth. This one over here I think is called gas town which is basically where you have a mayor which is your AI coordinator, a bunch of different crew members and then also pole cats or worker agents. You guys may have heard of crew AI. It's the same

[1:23:55] sort of idea. It's a fast and flexible multi- aent framework which supposedly delegates things, okay, where you have crews that have different agents within them each with their own segregated tool calling and stuff like that and you know it's another way of organizing information. This one over here swarmclaw is CEO based developer researcher and again you have delegation. So all these are different

[1:24:16] attempts by different groups of people to try and determine like the best organizational hierarchy of agents and I think pretty much all of them suck right now to be clear. Um, but I just want you guys to know and level with me that these are just different ways of organizing information. Just like you have skills and skills are highly, you know, specific to you, it's just a collection of markdown files with names, description, allowed tools, and then like SOPs. Sub agents are basically the

[1:24:40] exact same thing. So, as the field continues to mature and there are better and more novel context management strategies out there, uh, multi-agent orchestrators essentially, uh, you know, these things will grow more and more differentiated. Now in terms of what I would consider to be actually valuable delegation. Okay, there are two main

[1:24:58] design patterns. The first is the parent researcher and QA system where essentially you have a parent model which is usually your smart one. So this would probably be like your opus model that communicates with researchers plural. This will be dumber models like

[1:25:12] sonnet that typically do research better and more economically. And then some QA agents like opus which are basically just tuned to QA and nothing else. And the idea here is this is a good balance between like those super bloated arg charts that we saw earlier while still allowing each type of agent to do the things that it is inherently better than human beings at. The parent agent is

[1:25:31] obviously orchestrator. Anything that is up at the top you can always consider to be an orchestrator. And then what you have here is you have multiple you know sonnet researchers. And this takes

[1:25:39] advantage of that fan out idea. Okay. Where when opus needs something it doesn't just do the research itself because that'll pollute its context window. It goes does a bunch of

[1:25:47] research, fits in quadrillions of tokens into the context windows of these sonnet agents, then takes summaries of that and then uses that to make decisions. And then basically the way that it works is, and I'm just going to sort of draw like the the logic flow. Opus will decide to do something. It delegates down here.

[1:26:03] Okay, that information comes back to Opus. Opus then builds something kind of on its own. After it's done building something, it goes and gives the uh product of its building over to the Q&A agent. The Q&A agent returns some

[1:26:16] changes that it suggests it makes. Opus then goes through makes those changes again gives it to the QA agent. QA agent returns. This loop continues until

[1:26:24] basically everything is done. If there's research that's necessary, it'll go down do some research here and they continue develop. And then finally you have your whatever the the final product is that you're building whether it's like a business system, a development system or whatever. In this way, you're maximizing

[1:26:37] the incentives of each individual agent while also allowing uh I want to say like the leanest possible setup that still recognizes that different things are better at different types of agents are better at different types of tasks. You know, we could make this bigger of course. We could have like a testing agent. We could have a design agent. We

[1:26:53] could have a development agent. We could have a backend agent. But, you know, the more complicated you get with the stuff again as mentioned like typically the worse that it gets. If you want to go

[1:27:00] even leaner than that, then the second system is developer and QA where you literally just have a smart parent. Okay. And then you have a smart Q&A and then you just go back and forth between the two. And what happens is every time

[1:27:10] that you want to test something, you sort of have like a claw tomd or or or just like a prompt that's baked into your parent that legitimately says, hey, after you're done every development, run it through a new QA agent. The idea here is the QA has like literally no prompt other than, you know, you're a QA agent with no context. Read this code and apply the following whatever like design principles to it. And basically what

[1:27:34] occurs is this QA agent since it doesn't know what the heck the project is is on. Um it's not going to be biased like the parent agent will be in the development of the feature. The parent agent will have feedback from the QA agent and so it'll be able to incorporate into its own thread and take advantage of all of the pre-existing list of failures and successes and things it's tried and so on and so forth, but the Q&A agent is like new and it's new spawned every time. And so typically what'll work,

[1:27:55] what the way it'll work is the parent agent will go and it'll develop a feature and then at the end of the development there'll be um something in the cloud NMD or system prompt that says okay now that you're done make sure to check it with the QA agent. So we'll spawn a QA agent. The QA agent will then give feedback. Okay. The parent will

[1:28:10] design feedback. The parent will design feedback. The parent will design no feedback because it's now good. Parents

[1:28:16] done. And so now we have the final product. Um obviously you know because it has to do its own research and stuff like that. I personally think this is

[1:28:22] not as ideal but it is even simpler and um keep in mind that there is always like a time cost every time you spin up a sub agent. It's a fixed time cost but uh there's also some compound probabilities you're multiplying because you know you are having an agent delegate something to another agent basically there's no human in the loop. The more independent steps that an agent has to do without a human being in the loop the higher the probability that it will diverge from its sort of intended um goal or intended task. So when your

[1:28:48] parent agent in the previous example generates you know a bunch of research queries to the you know sonnet sub aents and goes and does them there's no guarantee that the research the sonnet sub aents are doing is actually 100% faithful to what your initial query was every step along the chain that is further from you typically the results and the quality is a little bit more diluted. So yeah I mean like it'll be it'll be either one of these for me developer Q&A or some sort of parent researcher Q&A. That would basically be it though. Um, personally, I find right

[1:29:15] now with all the org charts and stuff like that, we're just we're just going a little bit too much. We definitely don't need uh I don't know 700 layers of CEOs and customer success agents and lead engineer agents and stuff like that. Now, I want to talk about something that's gotten a lot of attention recently and does genuinely have the potential to significantly improve many business and programming functions. It's

[1:29:35] called auto research. Essentially, what I have in front of me is I have a research lab that I've spun up to improve the load speed of one of my websites. Now, the way that you gauge whether or not a website is loading quickly, is based off of uh three main metrics. The first is called LCP, least

[1:29:51] contentful paint. FCP, first contentful paint. Then there's TBT. I don't know

[1:29:56] what that stands for. And then finally, there's performance score. And so this is a standardized assessment called uh the Google Lighthouse score that you've probably seen before. And basically, it

[1:30:05] measures like, you know, when I type in 1 second copier and I press the enter button, how fast does literally everything on the page load? It also checks for very minor things like, you know, when I when I load this website, um, does the content on the page shift around? So, my website here, leftclick.ai, is just one of many ones

[1:30:21] that I own. And essentially, it's just a little bit too slow right now. And it's slow for a variety of reasons. We got

[1:30:26] this cool like glass isomorphism animation on the page. You know, there's like stuff moving around and lots of images of my team and and so on and so forth. So, um, you know what I've decided to do is I've decided to basically take all of the load off of me to make this website faster and then just give it all to that fleet of AI agents to do so instead. Auto research

[1:30:45] is basically perfect for use cases just like this where we have a very defined goal in my case to decrease or increase a couple of metrics. A very defined change method which uh is how you actually make the impact. So in my case just modifying the website code and then a very standardized assessment which in my case is that lighthouse score. In

[1:31:02] case you have never seen this before, basically Andre Karpathy, who is the one of the founding members of OpenAI, and then he also was the head of AI at Tesla for quite a while. Um, you know, he he just was doing a bunch of research on his own for uh one of the models that he was running and he's just like, you know, do I have to do this stuff anymore? I feel like I'm at the point where I could have AI actually run most of my research for me. Let me make a a

[1:31:25] quick hypothesis. if I just gave all of my changes to AI, would it be able to do the same thing that I do while I slept such that when I wake up, I'll have like a big list of improvements? And turns out, you know, he he can. And it's not

[1:31:35] that AI agents are like better than human beings at determining these research changes, but it's actually quite standardized to do conceptually. You're basically just like looking over a bunch of different possible things you could do, making one tiny change, and then just evaluating, hey, did that actually improve my score? Did that make things better? If so, I keep it, and I

[1:31:52] just move on to the next thing. And I go over and over and over and over and over again until finally, you know, you make it hundreds of iterations later. So, you know, in my case, like we uh I just reran the test because I want to start this from scratch to show you guys how this works. Well, it's actually fairly

[1:32:04] straightforward. And what I'll do next is I'll run you guys through the original way that auto research works and then how to download the repo and then set it up on your end for whatever the use cases that you you particularly have. So, it all started when Andre Carpathy uh who was a researcher, he used to work at um Tesla. I think he was

[1:32:18] the head of AI at Tesla and then he was also one of the founding members of OpenAI asked himself you know uh all this work that I'm doing all this research stuff that I'm doing is there any way to automate it and he found that if he just broke down step by step what it is that he actually had to do it more or less always went like this you know he he just had a little loop set up where you know he would uh make a hypothesis and the hypothesis would be like hey if I change x y and z I think my system will run faster then he'd actually execute the change. So he'd actually go and adjust XYZ. Then finally he'd assess. And then if the assessment

[1:32:53] was good, aka it made an improvement, then he would just go back to this and then make another one. Then if the assessment was bad, aka it failed, then he would just get rid of it and then not change anything. And then, you know, kind of start from scratch. And all

[1:33:05] along the way, okay, what he would do is he would update this little document, which um you and I could just call like a research log. And you know, basically the first change would be like, oh, you know, this worked. It was great. Second

[1:33:17] change, oh no, it didn't work. Then here's why. Third change, okay, it worked and it was great. And eventually

[1:33:21] over time, you end up with this massive massive log of all the different possible things you could do to an AI uh to whatever your task is and all the things that you have tried in the past that doesn't really change anything. Okay, so this is made of three files. There's a prepare.py, which in our case

[1:33:34] is kind of pointless. Then there's a train.py and then a program.nd. The

[1:33:38] reason why the prepare.py is pointless is because it's just about like AI uh research specifically. It's like fixed constants, downloading the training data, training a BP, bite paroding, tokenizer, and a bunch of other stuff that just isn't really relevant. The

[1:33:49] stuff for us though is obviously we want to train this and and improve this um improve our programs. We want to improve our websites. We want to improve some of our business functions. These two files

[1:33:58] here, train.py and program.py basically underscore how the entire thing works.

[1:34:01] Okay, so the super important one here is called program.md. What you do is you basically just tell it what you want it to do. So, for instance, hey, um, here's

[1:34:11] what you can do as an AI agent. Modify this file. Okay, every time you do, I want you to print a summary of the scores and then log it to this file. And

[1:34:19] that's literally it. It just goes through that loop over and over and over and over and over again. Then the actual train.py in this case, it's just like

[1:34:25] the website itself. Uh, sorry, the um the AI model um um setup itself with all the layers and stuff like that. In our case, right, the example that I was just showing you a moment ago, that's just my website basically. And so basically it

[1:34:35] just like it has a loop set up in its prompt. You tell it what you can change and what you can't change. You give it some like sort of log file that it dumps everything to. So you have like a big

[1:34:44] list of changes in progress. And then you know after that you are you're basically done honestly. You just fire it off and let it go. And when you do

[1:34:51] you know you can make some pretty cool changes. So you know I just reran the thing and uh we're already seeing some pretty substantial improvements. Uh not all these improvements are the same ones I was showing you guys before. It's this

[1:35:01] research lab. just I'm just resetting it over and over and over again to see if I could find anything more interesting. Okay, so hopefully that's pretty straightforward. Simplest and easiest

[1:35:09] way to do that um is just head over to github.com/carpy/auto research. And then what you do is you just copy this link. Okay, so how do we

[1:35:15] actually do this? Just open up anti-gravity. I'll click open folder. Uh

[1:35:18] I'll just make a new one called autoresearch test. Okay. And then I'm going to open and I'm going to click on cloud code.

[1:35:26] Zoom way in so you guys could see and actually just paste this and say clone this into our current folder. um auto research test just so that it doesn't do this in my um kind of my root folder which it's done a couple times. All right. So, it's going to start saying,

[1:35:40] "Hey, I want you to clone this." So, it's going to give it a quick try and it's just going to dump all the files in here. So, now we basically have the exact same thing we had before, right?

[1:35:47] We have the program.py, prepare.py, train.py, the progress, and you know,

[1:35:51] even like a read me that explains everything. So, now all we need to do if we want to like I don't know, train this on a site or something is um well, first of all, why don't we just make a quick site? Hey, build me a simple onepage portfolio site for Nyx. And obviously,

[1:36:03] it doesn't know what my name is. So, it's now going to build a simple onepage portfolio site. I just wanted to do it here. So, it's going to do this inside

[1:36:10] of this file. First, it's going to ask me some questions. Just uh add demo information for everything. And my goal is I just want

[1:36:19] to build a brief little website here for us. And then I just want to run auto research on it to show you guys how easy it is to optimize things. Now, in our case, we're going to do website. There

[1:36:26] are a million different things you can apply auto research to. I'll run you guys through a quick and easy framework, but first I'm just going to show you guys what you need in order to actually set this up. All right. Now, what I'm

[1:36:34] going to say is, excellent. I'd like you to create a dashboard for auto research and then set up the auto research framework to optimize the Google Lighthouse page score for index.html. I

[1:36:48] want you to run this on a local loop and basically just make index.html HTML as fast as possible across LCP, FCP, TBT, and then also performance score. Then give me some sort of live dashboard view so I could watch it um actually work in reality.

[1:37:04] Cool. And then I'm just going to press enter. And basically what it's going to do is just going to read through all these files right over here. And then

[1:37:10] it's going to use all of the information here in order to set up the dashboard for me. And while it's working, I just wanted to explain a little bit about where we are and where we're going. The initial stage of AI encoding was sort of like vibe coding. This is like 2024 2025

[1:37:23] stuff where a human being aka us prompts then an AI writes some code and then a human being reviews. So in this way our roles were basically relegated to writing. We would write the prompts we would make minor changes where necessary and in that way we like build a website or something. Well nowadays most of us

[1:37:39] do agendic engineering and this is sort of what the advanced part of our course um deals with. So this is where instead of just dealing with one AI, we're actually orchestrating agents and these agents are doing multiple things for us all the time and then basically like returning the results so that we could see and then like assess and make slight little recommended uh changes. So in this way our role is more of a director but auto research represents sort of the the next jump from agentic engineering to actually full independent research where now all we do is we're no longer like actually even directing the AI agents. We we let them handle their own

[1:38:10] direction. What we do is we just say, "Hey, I have a goal and I'd like you to achieve this goal. Here's how you can modify X, Y, and Z and here's an assessment." And so in this way, we set

[1:38:19] the direction. The agent just runs completely autonomously. And then what we are is we're basically like a we're like a we're like a principal investigator, like a researcher at a lab somewhere. We just say, "Hey, you know,

[1:38:29] I want you to do XYZ." And then we just go farming it to a bunch of uh, you know, research assistant RA monkeys to go and and do the experiments and so on and so forth for us. And so this is along a spectrum of decreasing human involvement. And I'm not really sure

[1:38:42] what comes next after independent research, but I do not imagine it will require human beings in the loop essentially at all. This is the same sort of thing that big research labs right now are currently using to optimize their setup. So Anthropic is almost certainly doing this all day long for cloud code to make things faster, to make things more performant. Um, you

[1:38:59] know, Open AAI is probably doing this behind the scenes to make codecs not only better, but even like adjust the architecture of the AI models and so on and so forth. They're probably doing it across all their web properties, right? Anyone that's really worth any salt at this point. It's probably been doing

[1:39:10] something like what I'm showing you guys with auto research for at least a little while. It's just auto research is Carpathy's way to democratize that and then allow people um, you know, to to do this even with like paid providers like Anthropics Cloud. Okay. So, if I go back

[1:39:21] here, you can see this is actually set up the auto research loop and it's actually doing the research um, which is not essentially what I wanted to do. I want to actually see the dashboard. So, what it'll say is show me the dashboard because I I actually want to like watch it work live. And then it's just paused

[1:39:36] the optimization loop. Now, it's going to show me set dashboard. It's restarted that. And then um I guess it's going to

[1:39:43] actually show it to me now in a second. Cool. We have it right here. Awesome.

[1:39:47] So, here is our dashboard and we are running multiple experiments. Obviously, this looks a little bit different from the dashboard I showed you guys earlier for my leftclick auto research, but that's okay. I don't want this to look the same. And I want to show you guys

[1:39:56] you can apply this to whatever you want. Um, our very first experiment had an FCP of 464,752 and a size of 12.9. What we ended up

[1:40:05] doing is we ended up minifying the CSS, making a bunch of changes to the code basically, and it took it from 12.9 down to 10, which uh technically makes our website even faster, but in reality doesn't actually influence things because our scores are basically the same, at least speedwise. Okay, so this is just going to continue um operating.

[1:40:21] Just say continue. Now, in my case, what this is doing is it's currently occupying the main thread, right? So, this is why it's going to be writing and making changes and stuff like that. Um,

[1:40:30] at any point in time, I could say, "Hey, just go run this in the background." Or, "Hey, I just want you to run this in a loop using like the Enthropic um uh agent SDK or something like that." I'd supply my API key and then it would and then it would go. And what it's doing

[1:40:40] now is it's actually making the changes. I guess I should probably also like open the website itself. That would probably make more sense. Let me actually take a

[1:40:45] look at uh what that looks like. Right. So, here's here's the actual website itself. And you can see that like for

[1:40:50] the most part, you know, it's very basic and simple. But what we're doing is we're just optimizing it. We're making it faster and faster and faster. This

[1:40:56] may break the website in some cases. Sometimes some minor changes like this do. But as you can see here, we've actually like improved it by a whole whopping 2 milliseconds, right? We made

[1:41:05] whatever change we did that made this a little bit slower has now been fixed and we're a little bit faster. Then it's just keeping each of these. So, you know, these things will go down very very very uh slightly. They'll increase

[1:41:14] very very slightly. But, you know, if you uh let it go for enough loops, then eventually you can get to the point where you're legitimately making pretty large improvements to the least contentful paint. Um, you know, first contentful paint and so on and so on and so forth. And just know that we can

[1:41:26] discard any runs that don't actually do anything. So, you know, in my case, my um uh like the one requirement I had for my leftclick perf auto research uh run was that you can't visually change the website at all. So, you should take a screenshot and it should be pixel perfect compared to the initial one, which is why it's like not adjusting the font or whatever. But I can make more or

[1:41:44] less any other change aside from that. And it it is doing so, which is pretty neat. Okay, so now you're probably wondering, Nick, so how the hell do I actually use auto research in my own business aside from the demo that I just showed you? And like what else could I

[1:41:54] apply it to? And my rule for auto research is that in order for you to meaningfully make any changes, you need to have three things. The first is you need to have a metric that you want to optimize for. So in my example, what is

[1:42:07] the metric that I am optimizing for? Well, I'm obviously optimizing for my lighthouse score. And so it's a very standardized metric. It's really simple

[1:42:15] and it's very objective. There's no real negotiations about what a lighthouse score is. Google invented it. It is what

[1:42:21] it is. That's what I'm looking basically to uh to to assess. The second thing that you need is you need a way to change that metric. So you need a way

[1:42:31] you can influence an outcome that modifies the metric itself. So if you think about it in terms of lighthouse page score, the direct way to modify your lighthouse score is just to change your website. And the direct way to do that is just like alter the code a little bit. So in my case, not only do I

[1:42:47] have the metric, which is a lighthouse score, I have a direct way I can immediately change the metric. And then the third thing that you need on top of that is not only do you need the metric and then you need a way to change the metric, you also need a way to assess what it is that you just did. And so because it's kind of like in the name, right? This is sort of a contrived

[1:43:05] example, but like the lighthouse score has a lighthouse test, and the lighthouse test just tells you what your lighthouse score is. So, I have like the thing I'm trying to improve, which is, you know, all the metrics that I just showed you guys. I have a way to improve it, which is modifying the website. And

[1:43:18] then I have a way to assess that, which is my Lighthouse page score, um, which I can run in a loop basically immediately after the changes. It takes me just a few seconds. And so, those are the three things that you need. If I were to

[1:43:27] formalize this, okay, and I will because I just want everybody to know uh, and and be able to visualize it. The three things you need in order to do auto research, okay, are number one, a metric, number two, a way to influence or the I don't know change method, let's call it, which allows you to influence the metric. And then three, some sort of assessment. And with the change method

[1:43:53] and the assessment, the most important thing, at least in in my view, is that you can do both of these things pretty fast. Like if your change method takes a really long time to do, it takes like an hour or whatever and then your assessment takes another hour. If you think about it, your your experiment will only be able to run as fast as basically once every two hours and that's still like light years ahead of like a you know, a human experimentter.

[1:44:10] But if you really want to see like those crazy vertical lines in the graph as things just get better and better and better sort of recursive self-improvement, you know, you need to have a pretty short change method. So ideally, this would take I don't know, let's say like 30 seconds or so. Why am I drawing like that? I could just do

[1:44:23] this. You know, maybe like 30 seconds or And ideally, the assessment would also take maybe 30 seconds or so as well because combined what we have here is we have a loop that can run 60 times per hour. Or if you multiply that out, what's 24 * 60? Um, a lot. 1,440 times a

[1:44:39] day. I mean, like if you could run an experiment 144 times a day, you know, even if like only 2% of these are actually good, that's like I don't know about 30 changes that improve. And if every change improves things by 1%, what you've just done to be clear is you've gone 1.1 raised to the 30, 1.01 raised

[1:44:57] to the 30, which is uh 34% improvement per day, at least in the first day. If you had, I don't know, let's say 90 of these changes be good, then this math ends up mathing way better for you. It's 2.4x. If you had 180 of these changes,

[1:45:14] you'd be 6x and so on and so forth. This is going to go basically as high as you let it. Anyway, so going back to my anti-gravity here, um, just seeing a couple of the changes. It looks like the

[1:45:23] biggest change that it has made that is actually and actively improved things was this jump between 45 and 627. So it made some change here, content visibility auto, remove scroll behavior smooth. That actually significantly improved the uh the load speed. And so

[1:45:38] that's what it did here. And we gone from 646 at the top to a fast contentful paint here of at the lowest 619. It looks like the least contentful paint did not change at all. meaning that this

[1:45:48] currently loads in like I think 600 milliseconds or so which is pretty dang good. Now kind of a contrived example since I just had AI build me the simplest website ever. But you know you can see with a more complex website one that I built for the most part at least initially and then one that AI didn't really have a lot of time to optimize for and it was a lot more complex those animations and stuff we've actually improved that improved that by 20%. To

[1:46:09] give you guys some more context there are some people out there that have applied this to projects that have improved metrics by like 50%. So Toby Litk pointed this autonomous AI research um system over at By the way, this is the founder of Shopify, right? Big guy or CEO of Shopify, I should say. He ran

[1:46:27] auto research on the entire Shopify liquid codebase. Now that's responsible for like running more or less everything about uh Shopify. Like it's it's their templating liquid syntax language thing.

[1:46:37] It's it's a lot of freaking code. And he found that after running this for however many times, he had 53% faster combined parse plus render time, which is his main metric. 61 fewer 61% fewer object allocations. Another metric. And

[1:46:50] things are just freaking printing for him. I mean, you know, what's that like twice as fast essentially to think that you could just point this at something and go twice as fast in like 20, I don't know, like 30 runs or something like that is nuts to think about. I don't know how long this took. Maybe it was

[1:47:04] like an evening. Maybe he went to bed, woke up the next morning and his freaking whole code library was twice as fast. I I don't know. Um but yeah, I

[1:47:11] mean like the fact that he he has done this and he can do this is obviously very impressive to anybody that has any sort of software that they want to optimize. So what are like the practical takeaways? Um you can optimize basically anything you want. So in my case,

[1:47:23] optimizing a website. How about you guys make a SAS app? Well, you can actually optimize that SAS app. You can optimize

[1:47:27] not only the uh front end of the SAS app, you can optimize the back end. You can say, "Hey, hey, here's your server. Here's the whole setup. I want you to

[1:47:34] make this load as fast as possible. I want like the request to come in instantly. Do whatever the heck it takes to do it. Here's a quick little test

[1:47:40] method. You know, we we time how long it takes for one request to come in when you click a button. You could just tell it that. Even if you just gave it

[1:47:46] literally the exact transcript that I just gave you a moment ago, it would probably do a pretty good job so long as you have the auto research framework. You could optimize random tiny things in your business. I mean, there are probably some like interfaces, random little modules and stuff like that in your company that like, you know, could be way faster and way better. You can

[1:48:00] actually optimize that. You could optimize things like customer support queries. You could like uh I don't know have like a prompt let's say that like an AI agent uses in order to handle customer support and maybe you're running some big enterprise or maybe you're plugged into a big enterprise and you have the ability to collect this data. You could actually just like test

[1:48:14] modifying the prompt and then like waiting I don't know like an hour and then seeing the changes and you know it's an hour which is kind of a loop but it's still 24 changes a day. You could like meaningfully modify that and move that in the direction um towards your goal. You could do cold email. That's

[1:48:27] personally what I'm using this for. Cold email is kind of a special case because again you need a fair amount more time, but I'm still capable of doing something like six to 10 tests a day at like over 500 to a,000 emails per test. It's pretty dang good. You could optimize a

[1:48:39] bunch of other things as well. You could optimize like your ad creative. You could optimize your copy. You could

[1:48:43] optimize your conversion rate by making minor changes to a page. You could really have a agents optimize whatever the heck you want as long as you have the volume of data necessary in order to like construct the test. So hopefully I made it really clear how all this stuff works. So, all you really have to do is

[1:48:55] just head over to, you know, that Carpathy auto research, that Carpathy auto research. Sorry, not that one um library or repo over here, okay? And then just copy that puppy in, clone it inside of your repo, and then just do away on whatever task you have. The

[1:49:11] simplest and easiest one for you guys to see how things work are obviously the website ones. But yeah, just know that like you can apply this to more or less anything as long as you have those three points that I mentioned. You need a metric to optimize. You need a change

[1:49:22] method or a way to influence that metric. And then ultimately, you need an assessment. Next, I'd like to talk about automation, specifically automating things on the internet. We're going to start with HTTP

[1:49:32] requests. Then we're going to move up to browser automation. And then finally, we're going to round it off with computer automation. And I'll talk about

[1:49:38] a bunch of different platforms you could use and ways to do more or less all of these things. So HTTP requests are probably the simplest and easiest form of, you know, internet automation. And cloud code does this natively. In case

[1:49:51] you guys didn't know, HTTP stands for hypertext transfer protocol. And essentially, every time I send a request to a website, basically every time I try and load one, what I'm doing is I'm sending a HTTP get request to the server upon which my website is located. And then my browser will take the response and then mark it up and make it look all pretty. So for instance, let's just like

[1:50:12] rerun that one more time. my browser, the client, decides it wants to access leftclick.ai on account of I just typed it into my freaking page. The second I

[1:50:22] press enter, what we're doing is we're actually sending a request over to their server, okay, which is located at some IP address. And that server is configured to automatically respond to a request of that kind by just dumping the whole website and giving it to you. And so then my browser takes that whole website and then it like marks it up and now I can see it. Right? Now, you might

[1:50:39] be wondering what exactly is it marking up? Well, if you view the source of the website, which is pretty easy to do. You can go to any website, just rightclick, press view page source, and you'll see all the HTML, you can see that what a website is actually sending and receiving is not like the pretty images and stuff like that. It's it's usually

[1:50:52] just sending references to those images. And um this is actually the content of the website. My browser just has mechanisms inside of it that just know how to turn this into that. Okay, so

[1:51:03] case in point, um the definitive AI growth partner for fastmoving B2B companies. This didn't just like come out of nowhere. It's not like this is like an image. This is actual text on a

[1:51:10] page, right? If I go the definitive, you can see that it's actually being represented on the kind of code of the page that um is being sent from the server every time I make an HTTP get request. The definitive a growth partner for fast moving B2B companies. All

[1:51:23] right. So why is this relevant to us? Well, because the first aspect of any sort of browser automation, doing things on the internet, I should say not um browser automation, but like automating network tasks is this hypertext transfer protocol. Claude and other AI models now

[1:51:38] have the ability to use web tools to basically make HTTP requests of the kind that I just showed you. And that allows it to do a tremendous number of things. Not all things, but a tremendous number of things if you know how to use it, right? So, the simplest and easiest way

[1:51:51] for me to demonstrate that is you can actually just like scrape any website you want now with Claude or any other agent. Hopefully, it's pretty clear and obvious how. What we do is we just take the URL, we go back to our agent, which in my case is this auto research one.

[1:52:03] Then I'm just going to say retrieve contents of this, just the text. What this is going to do next is it's obviously going to send the HTTP request using the web fetch tool over to https leftclick.ai.

[1:52:18] And now what will have gotten back, okay, is it will have gotten back exactly what I just showed you a moment ago, okay, which is all of this. Now, because I said just the text, if I go back here, you can see that it has extracted sort of stripped all of the code here and it's returning basically just the stuff that I could actually see. So, what did it say? Navigation,

[1:52:39] case studies about services, reviews, let's talk. Case studies about services, reviews, let's talk the definitive a growth planner, fast moving, B2B companies. See that right over here, you know, uh worked with anthropic, notion, Wix, Hey Gen, V, Litrix, Durbal, and so on and so on and so forth, right? So I

[1:52:53] guess what I'm trying to say is like this is a simple way that I can get data. And so one of the first and most elementary uses of you know uh any sort of coding agent is just you can automate website scraping really easily. So I could give it a simple list of tasks and I could say hey I want you to scrape like 400 different websites. I could

[1:53:09] literally just give it a big array top to bottom. It could go and it could do the scraping. Now the issue is a lot of the time okay you want to go further than just scraping than just reading a website. What you want to do is you

[1:53:19] actually want to dynamically interact with website and change things. So for instance, let's say what I'm doing is I'm getting a big list of all of the agencies out there, the AI agencies like Leftclick, and I want to send them all messages. Well, you know, I could just scrape every single website to see if there's an email address, right? But in

[1:53:35] my case, maybe there's no email address. So what do I want to do? I want to take that next step. The way that I do so is

[1:53:40] usually through some sort of form or whatever. How do I automate the clicking of a specific button? It's kind of difficult to do, right? I can't just

[1:53:46] automate the clicking of a specific button um through an HTTP request because you know this is something more than HTTP. It's kind of JavaScript. I could try and some websites I'll be able to so hacking this. Hey uh extract the

[1:54:01] cal.com link for me and then open in Chrome. Now going one step further.

[1:54:08] Okay, we're going to open this link in Chrome. So, we actually have this link available. And there are some services out there where you can actually just send an HTTP request to actually like book a meeting on a page. But you might

[1:54:18] think like in order to do that, I actually have to click on this button and then type this in and then enter a bunch of information and so on and so forth. Turns out I can actually just use HTTP requests. So, I'm just going to say book a meeting for 3:30 p.m. tomorrow.

[1:54:28] First name test, last name test, email nickattest.com. And without any more information, what it's going to do is it's going to go and it's going to find the API documentation.

[1:54:37] It's going to check the availability using the API documentation and then finally it's going to ask to book. So I'm going to say 3:30 p.m. March 30th.

[1:54:44] Then it's going to go and actually do the booking. But do you notice how many issues there are and errors there are with this? This obviously isn't perfect.

[1:54:51] Now I could theoretically figure out the exact schema and format that I need to use in order to send requests like this every single time that I try and book like a cal.com, but the reality is like not everybody's going to have a cal.com.

[1:55:02] What I'm doing here is I'm building a very particular solution that solves my one particular problem, the HTTP request. And even then, you know, there's just going to be some back and forth. It's not going to be it's not going to be perfect. And this is taking

[1:55:11] forever. I mean, I've been sitting here for like 10 15 minutes. It's trying its best. It's booking with a variety of

[1:55:17] different means. And I don't know, who knows? Maybe it'll actually go and do the booking. Okay, there we go. We

[1:55:21] actually did end up doing the booking, thank goodness. That said, that took forever and it was obviously a very fragile solution that only works with like particular cal.com pages, right?

[1:55:29] And so that's where we move to the next level of automation. That's where we go from simple HTTP requests which you know most services out there will have some sort of API application programming interface that you can actually communicate with. But um you know they're super fragile. They require very

[1:55:42] particular formats and as you can see they could take a really long time and then they're very narrow. That's where we move from sort of like the first level of automation HTTP requests all the way to full scale browser automation which is where uh cloud actually fully controls your browser. And you know there there are a couple of built-in tools with this now. But typically the

[1:55:59] best way to do this is using one of two tools at least as the time of this recording. Um Chrome DevTools MCP or there's also the browser use platform which actually is pretty new, pretty recent, but it costs a fair amount of money. And so what this does is instead of just sending HTTP requests under the hood, what this does is it actually loads up a whole browser for you and then goes through the process of doing a booking. So you see how hard it

[1:56:25] was for me to do this, you know, sort of simple task of like booking a meeting on a calendar even though I gave it the exact time, the exact information and so on and so forth. That might have taken a human being 1 second. It took me like something like 5 minutes of back and forth and probably like 40 bucks of tokens. So meanwhile, I can open up a

[1:56:39] page that has Chrome DevTools MCP. And I could basically say, "Go here, book a 30 minute meeting for uh I don't know, March 30th at 300 p.m. Nick test

[1:56:51] Nick.com. Answer a bunch of demo stuff for any booking cues." Okay? And I I just want

[1:56:58] you to look at what's going on. I was just using Chrome somewhere else, so it's just going to kill the pre-existing um instance, but now it's actually going to open up a new one. I want you to notice that like this is actually like opening up a freaking instance on my browser and then it's scrolling through and it's clicking on buttons and navigating on them uh navigating through the page for me. It's literally doing

[1:57:15] this by modifying the JavaScript of the page and running brief little commands in order to like communicate and go through things. So, it's filling out the phone number, what made you want to contact Nick's team, what's the project budget, please share anything that will help us prepare and so on and so forth. I think the project budget in this case might not actually be um five or I don't even think that's a an option because we don't go that cheap. As you can see

[1:57:35] here, it's finding the options for the budget, selecting 25 to 50K, and then it actually goes through and it it does it. So, what are we learning from this experience? This is much more general.

[1:57:45] Okay, it works way better for a much wider variety of use cases, but it's also a lot slower. Right? This is something that previously um I could have just sent one HTTP request once I know the format and then I would have like booked after like 0.2 seconds,

[1:57:58] right? But now, you know, we're kind of going through the page one step at a time. Every single one of these actions realistically is kind of like a it's almost like the same amount of time that a single HTTP request would take. Now,

[1:58:07] what it's doing is it's actually deleting um you know, my numbers and trying to reformulate numbers and stuff like that in order to like make it a valid phone number. And you know, after a little bit of finagling, it it actually ended up finishing it, which is nice. So, it actually went through, it confirmed it. It then went through the

[1:58:20] booking process and so on and so forth. And it actually took screenshots the whole way through of the process. So, um why am I showing you this now? Because

[1:58:29] basically this is a gradient where it takes more setup time to do browser or any sort of automation via HTTP requests, but it's faster and usually cheaper. Then there's a spectrum where we go from more setup time, faster and cheaper to basically always works but more expensive and slower assuming that you you don't. And so what does that mean? That means for any sort

[1:58:57] of like prototyping business application on a browser. I typically use browser automation or even computer automation which I'll talk about. And then once I've sorted out that it works, I'll actually go and I'll see hey can we do this via HTTP request because if so it'll be way cheaper and then we can just run a bunch of HTTP requests in the background. It's important because like

[1:59:12] most of the time like the cool stuff that you can do with cloud is actually just like automation, right? So understanding sort of this trade-off between pure HTTP requests which typically function off of like you know hidden APIs or whatever and then browser automation full computer automation um will let you be able to control a lot of things much better. So that's just one example of browser automation. I could I

[1:59:30] could use browser automation for anything. Hey, I'm considering renting in Vancouver, BC, looking for $3,000 a month uh max one-bedroom rentals somewhere in the downtown core are in buildings that have cool amenities like pools and stuff. And then the bottom two are sort of like our budget options. I

[1:59:44] could stick that puppy in there and then it'll actually go through and, you know, navigate to some rentals.ca page. I couldn't do this via HTTP requests uh without spending a lot of time sorting all this stuff out. Even then, it would

[1:59:56] be very fragile because the way that these websites work is they actually like explicitly try and go anti-automation. They make it like really really difficult to do anything. But um you know, in this case, what can I do? I can actually just open it up. I

[2:00:06] can change a couple of filters and I can actually go and like zoom in on the page. It can do whatever the heck. Can use the stuff on the right hand side. It

[2:00:13] could it could use the stuff in the middle. It can thumb through things. It can get me like a big list of apartments and so on and so forth. And I mean like

[2:00:20] the trade-off here is this is going to take a fair amount of time, right? Like as you see, it's like one action every 5 seconds or so. But it's so general that I could just give it a task and we'll go and do it. You know, if I were to try

[2:00:29] and do this by saying, "Hey, go scrape the rentals.ca web page or whatever that that would take so much time in order to build to the point where it doesn't just error out." And then most websites are also very anti uh anti-HTTP request automation because it's the simplest and easiest one. So you end up just getting

[2:00:44] like error error error error. This actually like uses my browser which is kind of neat, right? Anyway, I'm just going to let all this stuff go and uh in the meantime talk a little bit about browser use, which I think is probably like the the next level up.

[2:00:58] Just called browser use the way the AI uses the internet. I don't know how long this is going to end up being sort of like the the way to go, but basically this is like the next level up from Chrome DevTools MCP where you give it some very simple instructions and stuff like that like fill out my loan application and it'll actually go through the form using something very similar to what we did. Maybe it uses Chrome MC Chrome DevTools MCP under the hood, I don't know. Um, and you do it

[2:01:20] for, you know, like a bulk onetime payment of 100 bucks plus like pay as you go via credits. So in my case, I'm not like affiliated with this company at all to be clear. So, I'm not going to touch on it too much, but obviously it's a pretty cool product. Um, the big draw

[2:01:33] I would say for most people here is just like HTTP requests can be blocked because of uh, you know, platforms and stuff like that just being scraped all the times. So, they try and stop you. Um, so too can Chrome DevTools MCP be blocked in like any sort of like instance browsers. This platform like

[2:01:49] basically the whole point, you know, just to kind of cut to the, you know, the pricing page and all that stuff like like 99.9% of the reason you would want to use this is because it is completely undetectable. um you could make HTTP requests um sort of the old school way and then try proxies and stuff and maybe that'll work but maybe it also won't.

[2:02:06] But if you go Chrome DevTools MCP and that doesn't work, this is what you do and it's basically like 99.9% perfect. Um it does this because it fingerprints aka it like gives every one of your browser instances that are controlled by AI like this hyper custom sort of profile. So it seems like it's like a

[2:02:21] request that's made from a real person and then in that way it like just like offiscates it all. So, for most purposes, like I still use Chrome, DevTools, MCP, and this is like my main pick. But if I have anything that like I need to do in sort of a sneaky way. And

[2:02:32] uh when I say sneaky way here, I mean like this is great for stuff like social media. So, if you want to do like Facebook scraping or Instagram scraping or if you actually want to like interact with and leave posts and comments and stuff, pretty tough to do just right out of the box sort of with like a a version Chrome DevTools MCP. But this is really really good at like posting um sending DMs, X connect requests, whatever the heck you want to do. Um so yeah, not

[2:02:56] affiliated with that company at all, but it is pretty sweet and I think that that's they're probably going to remain the market leader in there. But anyway, so just like HTTP requests had a lot of setup time, but they were faster and cheaper once you set them up. Browser automation is kind of like a good like middle ground where it's like um oh, you know, like this actually has some some basic browser functionality built in and like it's pretty obvious how to like click a button or whatever. Computer

[2:03:17] automation is sort of like on the far end of the spectrum where basically no matter what you throw at it, it will always work. The downside is it's very expensive. Takes a tremendous number of tokens at least right now and it is very very slow. And the way it does this is,

[2:03:31] you know, whereas HTTP requests manipulate like APIs and curl requests. Curl is actually lowercase. Browser automation manipulates JavaScript and um I don't know like page clicks like button clicks. Computer automation

[2:03:45] literally controls your mouse and your keyboard. And because it controls your mouse and your keyboard, you can do more or less whatever the heck you want. Like I could literally like it could take my mouse and then it could go all the way up here and then it could close that tab. Could

[2:03:57] move this all the way at the left. It could close that tab. Like basically it can do anything on the computer that I can do. Now the way you do this right

[2:04:04] now is you got to use the Claw desktop app. So I'm going to head over to Claude. I'm then going to open that up.

[2:04:08] And then I think it's currently available in both coord. I'll just move over to the co-work tab and I'll say have computer use. Scan through my downloads.

[2:04:20] Find the um image called maker school 26 or something and then rename it to weekly community call picture. And the reason why I'm doing this is because every dang week I have a weekly community call and then I always just lose where the image is that I use as the thumbnail. And what it's going to do to start is it's actually going to whip up like computer use. So it's going to

[2:04:46] request access to my finder. And now as you can see here, it's actually whipped up like a computer use thing. So now it's going to go through and actually like type in my downloads folder or whatever. navigate over there and it's

[2:04:58] just going to start typing a bunch of different things like maker school and maker school 26 and probably try multiple variations of like maker school maker school underscore and so on and so forth because it's using my mouse and my keyboard. You know, I can actually like scroll through and uh and do things. Now, this is like local browser automation. This is actually literally

[2:05:16] exactly what I want, which is nice. I could have done this in like 30 seconds, but it's nice that it's figuring this out. It's using like a local browser uh sorry local automation here to like click through, scroll down and stuff like that. If at any point in time I

[2:05:29] want to change it, I'll say no, you had it. It's the the cover 26. I'll press that in just so that it knows what it's doing. All right, just went to

[2:05:41] grab a coffee and I got back and it has now found the Maker School icon 26. renamed it to exactly what I wanted. And yeah, I guess I screwed up on the name, but that that was what I wanted, which is pretty cool. So hopefully you guys

[2:05:52] could see pretty straightforward here to use computer automation. Takes a lot longer. Also consumes a lot more tokens because it is literally like controlling my mouse as it moves across the page, taking screenshots of everything as it does so. And the amount of like fidelity

[2:06:05] that it requires in order to do that is is pretty high. But um yeah, I mean like eventually, okay, put on a loop, this sort of thing will work. Uh it might just take a tremendous amount of time.

[2:06:15] just give it a task, say keep going until you solve it, and it will do it. It will just probably burn your a hole through your wallet um while while it does. So, realistically, the probably core play um that I repeatedly fall on as somebody that designs these systems for real businesses that earn hundreds of thousands to millions of dollars a month is I will start with some form of browser automation for the most part since we're usually just doing this in browser. Um I'll usually try Chrome

[2:06:39] DevTools OCP first. If that doesn't work because it's like a stealth application or it's something that, you know, requires social media access, I'll do browser use. Once I have that flow down, you know, unless it's like a Facebook or something like that cuz, uh, those are just notoriously difficult to like HTTP automate as well. Um, assuming that it's

[2:06:56] not, what I'll do is I'll look to have Cloud Code build like a custom utility based off of the data that it gets from Chrome DevTools MCP because it'll have access to network requests. I can actually see the requests that are being sent and received. Once we have all that, then I now have like the API internally. I write a bunch of docs and

[2:07:11] have cloud code sort of like embed that within my workspace and then the next time around I can just use HTTP requests. Although, you know, keep in mind that when you do it this way simply because of the volume that you're able to hit and the fact that HTTP is like typically a lot more regulated than browser automation. Um, you know, there are some there are some risks to that as well. You could get rate limited, you

[2:07:27] could get throttle, you could also get shadowbanning economically valuable knowledge work through claude. Um, it's really just HTTP request, browser automation or computer automation. Whatever way you decide, just know that doing that sort of automation is against the terms of services of a lot of platforms that you work with. So, I'm not condoning this. I

[2:07:44] can't really explicitly recommend it. Just making sure that you guys understand sort of what's available and um what other people are doing as well. Next up, I want to talk about claude code performance fluctuations and what to do if and when this ends up happening. I don't know if you guys have

[2:08:00] ever watched that movie Interstellar, the one with Matthew McConnA. It's one of my favorite movies ever. And in it there is a major problem that has plagued the world that uh has you know sort of set all the events in the movie in motion. And that's basically this

[2:08:14] idea of the blight. Now what the blight is is it's some disease that started affecting a bunch of plants. And as a result something like 90% of all of the food in the world is now just corn. It's a specific type

[2:08:29] of corn. That's why they got these big corn fields and stuff. And then you know the main character's family just does corn farming all day. So in history,

[2:08:36] this idea is referred to as monoculture um harvesting like monoc monoculture farming essentially. And it's where you know one particular crop is just so damn good. It's just so freaking productive, right? Has the highest yields and so on

[2:08:52] and so forth that over the generations the farmers learn, well this is the best crop ever. Why don't I just replace all my crops with this crop? Then I can make a bunch of crops and then I'll just trade this crop for other crops as necessary.

[2:09:04] Every time that happens, usually productivity or yields will go up. And they'll go up for sometimes a long period of time, sometimes like literally generations. And then all of a sudden, what occurs is there ends up being a problem with that crop. The problem is

[2:09:16] either in the soil, the problem is maybe a bug that is developed that like really screws with that crop specifically or something else. And because all of the farmer's eggs were in that one basket with that one crop, what ends up happening is this blight or this disease or this circumstance ends up destroying all of their crops at once. That's led to some of the biggest famines throughout history, I believe. And um

[2:09:36] it's one of the reasons why, you know, farmers nowadays do a bunch of things, namely crop rotation. They have multiple different crops that occupy the same thing of land. They uh you know, usually don't do just one crop, they have multiple crops going, whatever types of crop they are, just so that if a harvest on, you know, one type fails, then you know, they'll at least get something from something else. Well, the reason

[2:09:55] why I'm bringing up this analogy, and I think I've really hammered it home here, uh is because I think this applies to cloud code. Cloud code is really good. I don't think there's a better coding harness out there. I don't think there

[2:10:07] really is anything better than cloud code. At least as the time of this recording, and I don't know if there ever will be. This is me just being honest with you guys. I think at a

[2:10:13] certain point with AI, you know, an agent's ability to program the next model, okay, just gets better and better and better. And so the people that have the better agents, if if they apply their resources effectively, just end up with like this impossible advantage due to exponential growth. So what that logically means is that, you know, it's the best crop ever, right? It gives you

[2:10:32] the biggest yields ever because it's so productive and because it makes you productive. You're probably just going to want to use it all the time. The downside to that is there are a lot of things here outside of our control in terms of cloud code performance. And

[2:10:42] sometimes cloud code performance goes up and it goes down and other times just completely gone. So the reality is um we're probably all going to be using cloud code a lot because cloud code as mentioned is freaking awesome. But if you grow too rely on it to the point where cloud code is basically a monoulture crop, you end up with situations like this, which actually just happened yesterday, just one of many occurrences. To make a long story

[2:11:05] short, cloud went down. You know, there was a big issue with Opus 4.6. And I

[2:11:09] think it lasted like maybe an hour or so. And basically 95% of developer productivity uh plummeted the second that cloud was gone. The reason why is because, you know, cloud was everything.

[2:11:20] They sort all their files on, you know, the claude desktop app with uh simple skills that were just made in like Claude's format and nobody or nothing else's. The second that Claude uh uh you know was down then all their prompts that they had saved and specific points and stuff like that were very difficult to access and they weren't good to use with other models. Whole code bases that had been designed by Claude were not interpretable at all. There was no

[2:11:42] commenting. So they tried using other models and other agents and like that didn't really work. And then ultimately cloudish is the best. The intelligences

[2:11:47] of the these other agents just don't work the same. So, you know, just led to like a bunch of bunch of issues essentially. This isn't the first time that this has happened. Um, this has

[2:11:55] actually happened a number of times. You know, this is Adam from um earlier today talking about like major outages with claude and how different types of platforms are operational whereas other ones aren't. There's also um a bunch of cloud code performance degradations. You

[2:12:08] know, I just looked up an old post from I think it was uh Turk here who's one of the lead guys on cloud code. He like drops cloud code updates and stuff all the time. Well, anyway, um, you know, there were degradations historically, this is December 17, 2025, of Opus 4.5

[2:12:24] and Claude Code, where basically because of some runaway either garbage collection or some sort of like memory issue, um, you know, Opus just got worse and worse and worse and worse every day for a certain period of time, which led to like, you know, massive performance decreases uh, literally probably on planet Earth, at least in knowledge work. So, okay, hopefully at least this point I've convinced you guys why claude is nowadays probably already pretty monocultury and likely as it continues to to dominate likely to just become more and more and more monocultury over time. Um, the question obviously is what the hell can we do about it? And so

[2:12:58] there are a couple of uh solutions and most of them revolve around this idea of diversification where basically you know instead of just putting all of your eggs in the clawed basket. This is my cute little basket. Sticking it chalk full of you know nice clawed eggs. What we do is

[2:13:12] instead of putting I don't know all 10 of our productivity eggs in this clawed basket. We put like seven eight or maybe nine in them. Okay? So maybe like seven

[2:13:21] out of 10 in claude. And then what you do with your other three out of 10 is you just distribute them. you distribute them such that you know I don't know one out of the ten are in codecs you know another one out of 10 my god I'm going to get really good at drawing these are in uh I don't know like anti-gravity's like gemini right and maybe one out of 10 are in some other type of coding harness like pi or something that maybe also uses like some form of like local models or whatever the point that I'm making is obviously we're being pragmatic here like you should probably predominantly use the best model out there because you know it's not like a it's not a linear thing.

[2:14:01] If a model is like 1% better than another model that 1% once you get smart enough is like the difference of like a gulf right Einstein is like 1% smarter than a normal human being or something like that and he was able to come up with the theory of relativity or something along those lines. Obviously don't take me at face value there. I'm sure his IQ is through the roof. But the

[2:14:20] point that I'm making is like when you get to this point with these weird galactic intelligences, even like a small little increase in the the the intelligence of the model might lead to like a big downsize difference, right? So if you have the ability to use the best model, just use the best model. But don't put all your eggs in that basket because if that occurs then what'll basically happen is like as the performance of claude over time goes up assuming um claude is orange your total productivity in uh blue here will also go up basically in lock step.

[2:14:51] And so if the performance of cloud goes down so too is your entire productivity. If the performance of cloud goes up so too does your entire productivity. instead diversify. Okay, instead of just

[2:15:01] this like yellow one which is Claude, maybe you have like a green one here which is Codeex. And what occurs is, you know, Codex maybe is a little bit more like this. And so what ends up happening is the average performances of, you know, both of these sort of average out and then instead of being super reliant on Claude, what you get to do is, you know, this black thing which is like you ends up being a lot more stable. It's

[2:15:20] the same thing in uh investing. Have you guys ever invested in like, I don't know, an ETF or some sort of um um um index fund? You know, basically the way that all of the stocks work is there'll be a stock that does this, there'll be another stock that does that, there'll be another stock that does this, there'll be another stock that does this. Do you see how volatile Okay, that

[2:15:40] stock probably doesn't go back. Do you see how volatile all these different stocks are? Well, rather than tie your your literal life savings to all of you know any one of these stocks, you just tie them to all of them simultaneously such that you know over time maybe your things slowly goes up and that's a lot more reliable and dependable. Okay. So

[2:15:56] the way that you do this in practice, the way that you diversify your models in practice, um, is you use platforms built in that have the ability to orchestrate or juggle multiple different types of agents just inherently or you use things like MCP servers or whatever that allow you to do that sort of thing within cloud code or within, you know, some other um, you know, coding agent. And so obviously like right now, okay, if I'm just being pragmatic with you, there's there's Cloud Code and that's sort of like the big boy and he's they're fantastic. Then there's, you know, codeex. And some people will swear

[2:16:27] on their mother's life that the codeex is way better than clog code, but I I don't really think so. And then there's like, you know, um Gemini isn't really the the right term. It's sort of like anti-gravity's like agent chat within um um uh anti-gravity. Okay. And this is

[2:16:43] sort of like my little personal tier list, but basically, you know, use other models in conjunction with harnesses and stuff like that you might have set up in cloud code for for best results. Okay. So, yeah. Anyway, there are two main

[2:16:54] major ways of doing this right now. The first is using a platform like Conductor. If you've never seen a platform like Conductor, what this does right now is it allows you to create a bunch of parallel codecs and cloud code agents inside of isolated workspaces on your computer. You can then just like

[2:17:07] with anti-gravity or you know cloud code desktop app or whatever, you can just see how their performances and what they're doing sort of in real time. And because you are just the conductor up at the top, if you know the clawed code chunk of these don't end up working, but then the codeex ones do, then that's perfectly fine. It doesn't really change anything for you. You're just going to

[2:17:25] like momentarily allocate most of your time and energy to the codeex ones. It's all in the exact same interface. It's very straightforward. You just do it

[2:17:32] all, you know, through this sort of like conductor interface. Super easy. And then uh you know like this is used by a lot of real big people all over the place to basically average out minor statistical fluctuations in models and then allow for the taking advantage of different parts of different models that are slightly better slightly worse than each other at things like for instance a lot of people think the codeex is actually like quite cracked at you know the sort of like deep contemplation required to make big backends and it's better than cloud code. I don't know if

[2:17:58] I entirely agree with that and I think even if that were correct today, it probably would not be correct in like a few weeks because things change so quickly. But, you know, this allows them to take advantage of Codex's ability to build the most cracked back end ever and then have Cloud Code do some other thing that Cloud Code is great at. Okay, so Conductor is pretty sweet. Uh, I'm not

[2:18:13] going to worry too much about like setting it all up. It's actually quite self um explanatory and I don't want to just make like a 700 hour YouTube video that's me, you know, setting up a bunch of different platforms. There's no real value to this. These guys set out the

[2:18:24] knowled the um documentation really really plainly and really intelligently done here. You can just click that download button, set it up and and you'll be good to go. Okay, so that's number one, right? Number two is you can

[2:18:34] use something like um MCP servers to distribute your load across multiple different models. So for instance, there's this codeex MCP server which you know technically lives in cloud code. So if cloud code does go down or something like that, you won't necessarily be able to use it. Keep that in mind. Um, but

[2:18:51] you know, if it's just one of the cloud models or whatever, it's a little bit different. Basically, what you do is you download an MCP server that allows you to communicate back and forth with a codeex. And so, that one's very straightforward and easy. There's

[2:19:01] there's a git repository right over here. It's very straightforward. All you do is you literally just like install the codeex CLI, okay? Using npmi-g

[2:19:09] at OpenAI/Codex. You just give it your OpenAI API key. Then you just add it to Cloud Code. Then you can actually just

[2:19:14] like have a conversation with them. So, for simplicity sake, I'm actually just going to do that cuz that's a lot faster. I'm just going to go back to my anti-gravity instance, which is right over here. You can see I got a search

[2:19:23] back a little while ago from something that I was working on. I'm just going to open this up and I'll say install this. I'll say keys andv don't share. This is a demo. Let me know

[2:19:36] when done so I can restart. And what it'll go through is it'll go and install the codeex mcp server. And then I can just go here and I could say, hey, ask codeex how it's going. So now what it's

[2:19:49] going to do is rather than just you know kind of operating on its own thread it literally just run through like a thing pinging codeex and saying hey man what's going on it echoed back the message successfully okay I want to chat with codeex yes and let's just hear uh what it has to do what it has to say rather soc- cli codeex this is just a ping I guess to make sure that it's online this one is now saying hey I'm running on codecs uh on gb5 in your local coding workspace I can do all this stuff the file system's currently restricted and so on and so forth. So I mean this will work in the cases where you want claude to like orchestrate a conversation with codeex without actually having to go into codeex and that can that can be quite good when um you know you don't really want to like upset your local workflow you still want to work within cloud code and do everything that you're normally doing but then for whatever reason cloud code performance has been degradated degradated degragated degraded uh but I should note that you know if cloud code itself goes down let's say there is some widespread anthropic outage you know your your next best bet is to literally go and download probably like the codeex um desktop app here, download it for Mac OS and either get a subscription or at least know how to get a subscription, know how to use the app such that if there are major issues with any one of these platforms, you know, at any point in time, you can just jump right back. So, that's personally what I do. I

[2:21:04] actually have Codeex up and running. I know how to use Codeex. I'm very familiar with Codec. um you know the way

[2:21:08] that I set up my workflow is not only do I have like a dot claude with the skills and and you know so on and so forth but at any point in time I just I can just duplicate this whole workspace such that it's like generally accessible by any agent I can actually go over here and then say hey uh for whatever reason cloud code is down so I'd like you to duplicate this whole business workspace change anything that is cloudspecific like the claude the cloudMD etc to um the usual agent specification. You can find all that at agents.mmd.

[2:21:40] Um, and in general, just make sure all of this stuff works for codecs. Then what you can do is you can either run some sort of like synchronization flow or you could just like manually do this every now and then. And then you can send that off to codeex however necessary. Cool. Now it's actually going

[2:21:52] through this process of syncing the workspace to the exact same type of folder / business-codex. Then it's just changing my agents.mmd and stuff. Um,

[2:22:01] what you could also do is inside of the same workspace, you could just like duplicate this, make this like agents or whatever. You could have this just all go cap agents. You just probably need some line in your cloud MD that says, hey, when you update your cloud MD, also your agents or whatever. The whole

[2:22:15] purpose of this workspace is to work with anything. Um, in my case, you know, this is just very cloud specific and I'm making courses on cloud, so I can't really just mess this up and I don't want the workspace to get any any messier than it already is. But hopefully you guys see how easy it would be realistically to do some form of diversification. Okay, so just to make

[2:22:31] it super clear, there were three main forms that I was recommending here, right? The first form was I recommend downloading and then installing a tool like Conductor. What Conductor does is it allows you to run a team of different coding agents right out of the bat using like the native CLI for codecs and um cloud code. And so you're actually

[2:22:49] having multiple agents just like operating in parallel. They're just doing so sort of in one workspace that is not like branded or tied to any individual type of model provider. The second one is using something like the Codex MCP server which is great to use when like cloud code is up but individual cloud models are degraded or there's some issue that are um that is preventing it from operating the way that you wanted to. In that way you

[2:23:10] could still take advantage of whatever cloud model you do have access to and also like your own cloud interface let's say in cloud codes desktop app or maybe like an anti-gravity um cloud code extension setup like I have. And then the third is just operating in an entirely different agent platform entirely. My recommendation, at least as of right now, is to use codecs because uh every test that I've ran with Gemini is nowhere near as good um at anything except for front- end design. Perhaps

[2:23:35] their new model will come out and that'll be way better or something like that, but I'm not going to hold my breath for that at the moment because as mentioned, I think Claude is really just the dominant the the dominant playboy as of right now. Okay? And all of this is because we do not want the monoculture crop. We do not want all of our eggs in

[2:23:50] one basket. We can have most of our eggs in the cloud basket for sure, but if you put all of them in, then you're going to suffer the exact same situation this present jit guy did where you know the second that cloud went down, he just couldn't do anything. Okay, so hopefully that makes sense. I personally am about

[2:24:03] 70% cloud code and maybe 30% spread across codecs and then like a couple of open source models. Um, and then I use agnostic uh you know coding harnesses like PI in conjunction with things like conductor in order to make sure that I'm good to go. All right, now let's chat workspace organization. I'm going to show you guys

[2:24:21] the way that I personally organize my workspaces, discuss a couple of alternative ways and then also just talk about like the hierarchy of information and then how to maintain like a really root clean file space. So this is the structure that I basically have set up and I'm going to run you guys through my actual anti-gravity setup in a second. I actually just had AI generate me a bunch of diagrams for this. So that's pretty

[2:24:40] meta. But um to make a long story short, I store all of my business stuff in a business workspace. Okay? Now, my

[2:24:48] business workspace includes a bunch of additional folders that you don't really need in order to have my structure there are very specific to the platforms that I use and whatnot. Really, the folders that you need, if I just cross out all the stuff that you probably don't actually need, okay? And like you probably don't need this either. Some

[2:25:04] people have virtual environments, some don't. But really the stuff that you actually do need um is going to be like aclad which is where you're going to store all of your you know claude specific files. It's where you're going to store your skills. It's where you're

[2:25:16] going to store your agents and etc. An active or a temporary folder or whatever the heck you want to call it. But this is basically just going to store everything else. So all the generated

[2:25:26] files and so on and so forth. Aenv where you're going to put your obviously env keys. So any sort of like API keys, credentials, anything like that. And

[2:25:37] then finally, your um local cloud.MD, which is just like your local system prompt. And if you guys remember, we store the global system prompts um in a kind of like a tilda.

[2:25:50] Claude folder um where you know the rest of your your global stuff is. And this is like this is somewhere else. This is usually like your home folder wherever that is. On a Mac, you know, in my case,

[2:25:59] it's like Nyx. So if I go in my Nyx or I folder and then I show hidden, I can actually see the doc folder. I can click on it and I can see it under your workspace. If it's like a Windows or

[2:26:08] whatever, it's going to be different. So you're going to have to look for it. Okay. So mine obviously looks a little

[2:26:12] bit different from that, but I just want you to keep in mind those um you know the cloud, the active, thev, and then the cloud NMD. That sort of structure I showed you a moment ago. That's the one I'm going to be assuming that you you're going to be building. Okay. So I

[2:26:24] separate things into and I also have a personal version of this, but for now we're just going to stick with business. a business workspace. And so I literally have like a folder on my computer, you know, nicks arrive and then it goes slash business and it's within this business folder that I currently exist that I do all of my work. So what do you have inside of

[2:26:45] business? You have yourv, you have your claude skills, which is sort of like the intellectual capital that you accumulate over time as you do various sopable things. You have your claude.md. Then

[2:26:57] you also have um you know like your active folder and the way that I personally organize this as somebody that not only um uses cloud code and other agents in my day-to-day life but also sells clients on the implementation of these sorts of things and then is also responsible for using cloud code in order to fulfill the implementation is I separate it such that my main business needs that contain all of like like my stuff is in this business folder and then anything that I do on behalf of my clients lives in specific client folders. So let's say I have a client called client A. Well, client A actually has his own env with the client's API keys. They have acloud/skills with the

[2:27:34] project skills. Skills that are highly specific to the needs of that particular project. You know, if I work with like some sort of digital marketing agency and I have a skill that uh I use on their behalf in order to like connect to some service that they use to print out a report, like I would put that skill inside of the client folder. Then I also

[2:27:52] have a cloud. MD um that essentially you know I just run with a slash in it and that also just describes a little bit about the client in the same way that I showed you guys earlier. I have my own cloudmd that describes a bunch of stuff about me. So oh who am I Nick Sarif? You

[2:28:04] know I'm 30 years old. I'm an end-J. I currently live in XYZ area. Here are all

[2:28:08] my businesses. Here much money I make. Here's all this like highly relevant contextual information. I also have

[2:28:13] similar contextual information for my clients and then for their businesses as well as anybody on their team. So that you know if I say hey send a message over to Jane letting her know XYZ. It's literally just like one message and then and then it's sent. Okay, so I I

[2:28:25] duplicate that across all my client base. So client A, client B, client C, however many clients you have, that's how many project folders I have. And the key here, and the reason why I think this is like this most solid organizational scheme I've stumbled on after several years of working with this stuff, is you can actually call client skills while still being in the business um workspace. You know, it's not the

[2:28:42] exact same because you're not technically loading them inside of the um if I just go slashcontext here, you're not technically loading them inside of the actual context. Okay, you only got the ones that are like sort of local here, but uh you can still call skills that are not local simply by putting in your cloudmd a oneline thing that says, "Hey, um there's some skills that we reference that aren't all going to live inside thecloud/skills folder. These are client specific skills. If you

[2:29:06] want to reference those, then you actually have to go inside of the client folder that I'm referencing and then, you know, pull it out that way." And so in my case, um you know, the business uh workspace is sort of like top level and the client workspace is sort of underneath. So what's up with this?

[2:29:19] Don't pollute a root. Always store an active or subdirect root. You know, earlier I said I have an active folder.

[2:29:25] The reason why is because if you start polluting your root, it just ends up being like a total nuclear bomb waiting to happen. You just have so many files. Your files are stored all across one giant folder. Not only is it like

[2:29:37] visually insane to look at because it's like this is always open essentially and it just pushes all the way down to the bottom, but it's also a little disorganized for your agent as well. better instead to store specific locations that you dump files to. Okay, using the skill spec itself. So for

[2:29:53] instance, inside of model chat, if I go over to my skill, you'll see that it actually specifies where to put the actual model chat. It literally says dump it inside of active/model- chat and then name it in this particular way. So in that way, this model- chat skill is actually hooked up over here to this model- chat um you know conversation thread. and I can open that

[2:30:14] up and I can actually like see the conversations that we have been having. Um, it's also much more organized for the skill because I'm not just dumping everything in the same place. Uh, it's super easy to do and then I don't actually have to do any sort of like agentic search or agentic lookup which I think is pretty valuable. Uh, because

[2:30:29] agentic lookups are just more things that consume tokens. So, what I'm trying to say is I just store everything inside of like a folder I can toggle called /active and then I store any specific information as to where these things will go um inside of the actual skill themselves. So, you know, there's a bunch of leads of my own CRM. That's

[2:30:45] where they live. There's like some config files for other things. This is where they'd live. If I do research,

[2:30:49] this is where they live. And so on and so forth. I would never store random scripts directly in root. Neither would

[2:30:54] I do temp files or data files. If you want like temp files, files that you know are only going to be used for like a short period of time or in the course of a a process being executed. Personally, I actually store these as like active/TMP inside of some hidden TMP folder so they don't even mess up my active. And you're

[2:31:10] probably thinking like, well, won't I lose stuff if everything's super nested? No, you you won't lose anything nowadays. You're trading off the amount of time it would take you to like scroll through your root thing for um the amount of time it would just take you to pump it into your agent to ask it, hey, can you find XYZ? But you'll find that

[2:31:24] if you just like allow the agent to organize your workspace, it it tends to do so in a pretty consistent and then reliable way so long as you expressly give them a structure where you're like, hey, make sure to always put stuff in active. And remember earlier I talked about diversifying away from just cloud code. Well, what's really cool is um you know when you'd run a business workspace like this and then you have your client and and and so on and so forth workspace sort of underneath it um what you can really easily do is just duplicate your cloud. MD into an agents and then a

[2:31:49] Gemini.mmd and you can just have all of these in all of your workspaces simultaneously such that if at any point in time you want to use I don't know cursor for something you want to open it in anti-gravity you want to do it directly in cloud code like you never really run out of the system prompt um um design pattern like you know if you have the same thing written in cloud MD the same thing in agent MD the same thing in gemini you can basically just like have that on 247 now I haven't needed to do that personally um in quite a while and I've actually been very lucky to have not been affected by some of the recent outages but I remember back uh I don't know like a month and a half ago or whatever I actually had like a specific line that said hey I want you to synchronize the cloudmd with the agent and the gemini identity all the time just in case you know we have an outage and I need to drop this into a different coding platform now another thing that'll happen reasonably often is you know because we're not dumping stuff into our root we're going to end up dumping a lot of stuff into um active right and so I have like just a bunch of stuff here dub video links yay dentist auto research hindi source you know when I was dubbing my stuff bunch of different um um screenshots and stuff like But uh you want to periodically clean up this workspace. So you periodically want to say something along the lines of, "Hey, clean up my active slashfolder. Anything inside of

[2:32:56] subfolders are fine, but anything that's just loosely in the in the folder, like any txt files, py files, JPEGs, and related, I want you to clean up by either deciding if it's necessary. If it's just a temp file, just get rid of it. Otherwise, store it in a folder that makes sense. You're going to want to run

[2:33:11] something like this reasonably often. Um, the reason why is because you just don't want to have to, you know, scroll again through like a quadrillion different things. And you also want to make sure that any future model that comes around can just like very logically look at some sort of organizational hierarchy and then make decisions based off of that. So that's

[2:33:25] what's going on here with all these docs for Icloed, right? It's deciding what to do here. It's going to download them into different folders. It's actually

[2:33:32] going to get rid of a couple files here, like, hey, this is a file. This is an incomplete download. This is a bunch of unnamed temp snapshots, right? And and

[2:33:39] what you'll find is within like 2 seconds, it just does the whole thing. Now my active folder is much much cleaner and I don't have to worry about this sort of thing um ever again which is nice. Um and you know in my case I also have a couple of these web design projects. Enumerate all the web design

[2:33:51] projects in active. Um these are things like Volta or aura and so on and so forth. Find similar projects and then store all of them within a web- design folder. And despite the fact that you

[2:34:02] know you might be like thinking Nick why the hell are you spending time and energy doing this? Um, if your workspace is clean, the work that you do within that workspace tends to be a lot cleaner as well. And so, I mean, in my case, I just found what, like 1 2 3 4 5 6 7 8 9 10 11 or something like that, different things, I've just sorted all these out.

[2:34:19] Now, anything here that is more personal than business, let me know and I'll upload it into the personal workspace instead. I just let that go, but I don't obviously want to show you because there are some personal things in there. And that takes me to the next point of workspace organization, which is everything that I just talked to you about. Um, when it comes to like

[2:34:36] organizing with a business at the top level and then having various client folders in, you can do the exact same thing with personal. And so I don't actually just have a business uh sort of workspace set up. Claude has now gone beyond just my business partner. Okay?

[2:34:50] And it also assists me with a lot of personal stuff. And when I say personal stuff, I'm not referring to like, I don't know, relationship troubles or whatever. I'm talking about like for the most part my health, uh, you know, things like my my my citizenship paperwork, uh, you know, important documentation relating to my identity, personal projects that I have that are, I don't know, related to like learning piano, uh, that sort of thing. And so,

[2:35:10] like I have like a business one over here, okay? But just because I want this to be really, really clean, I'm also going to show you guys a personal um version of this, okay? Which is basically the exact same thing. And then instead of doing this

[2:35:25] via clients, which you know, I mean, like obviously it's it's a personal project. It's not a client project anymore and then you can't really do it that way. But instead of doing things based off of clients, I now recommend doing things based off of like domain and or um you know like a particular field of your life. So, I haven't found

[2:35:42] the best way to organize this yet, but for instance, I have one right now on citizenship because I'm currently proving my my citizenship to uh you know, a particular country in Europe. And as a result, I'll be able to be an EU citizen. It's going to be pretty fun.

[2:35:55] Likewise, I have a sub one called health. This contains a couple of skills that I use to like visualize my genetic libraries and stuff like that. And hopefully you guys are seeing the point.

[2:36:03] What you do is you just sort of you enumerate the clients of your personal life which tend to be projects like citizenship, you know, your health, uh I don't know, your skincare and whatnot. And then you contact or or or list those underneath your personal workspace. Then you also have skills related to your personal workspace like hey you know can you clear out all of my I don't know like personal emails for X Y and Z. In

[2:36:24] this way you have a good separation at least in my mind between business uh life, your personal life and then also just logical grouping of each of the different things that you can do within them. So I also have as mentioned you know that personal folder and I can open that personal folder anytime I want. Uh it was just right back up here and that'll just contain you know specific personal conversations I've had with uh you know Claude and Anti-Gravity to do things. And I'm happy to like pay token

[2:36:48] costs, stuff like that to absorb that because my personal life isn't like personal personal. It's just stuff that is not business, right? If I can improve the productivity of that, might as well.

[2:36:57] One more thing you'll notice is that when I open up this personal, the colors were a little bit different. Um, I do that on purpose. I do that because, you know, if I am working on business stuff, I want it to be very clearly like accessible and visible to like my my my monkey brain. Like I instantly want to

[2:37:10] know I'm in my business folder. Whereas when I'm in my personal folder, that's different. And so what I've done is I've made the outline of this green. I do

[2:37:16] that by creating this VS Code settings folder and then I just have sort of like this um config that VS Code reads at the beginning of every run to like actually change the header bar. This isn't like a super big unlock or anything, but I do find just like having a slightly different color will always just make my own be like, "Hey, this is my personal folder, so I have access to like personal information here, so I can actually have a conversation about whatever." I don't need to reprompt it with a bunch of stuff. And you'll also

[2:37:37] notice that uh you know, this doesn't have like the Netlefi or a bunch of those other sections because this personal folder only stores stuff that is like for me. it's not for Netlefi. Okay, so hopefully that gave you some insight into at least how I organize my workspace, but this is by no means the only way to do so. There are a bunch of

[2:37:53] other ways to do it as well. One candidate way is instead of having like a business workspace, what you do is you just enumerate all the projects in your business. So I don't know, you might have a project for instance that's like website overhaul. What you do is you

[2:38:05] have like a top level folder. Okay, your top level folder might be business or it might be whatever the name of your company, Leftclick Incorporated. Then inside you have a projects folder. Then

[2:38:13] underneath your projects folder, you have like website design, you have conversion rate optimization, you have lead generation, and so on and so forth. If you're running a business, you can actually now have your CRM entirely within cloud code as like ajson file. And then uh periodically on a daily basis, you can synchronize using some sort of crown job or something like that to, I don't know, some events that are pulled in from your calendar. You could

[2:38:34] store stuff that way. I've seen people host everything on GitHub as well. do some sort of like daily uh uh uh download or clone of GitHub and then some sort of like nightly push so that they always have all their information stored on the cloud. You can do that in

[2:38:46] conjunction with the previous system I told you about or the business/personal/client one that I talked about initially. You can also just ask Claude to set it up according to however you like. If you guys don't like the way that I set up my workspace for whatever reason, despite the fact that I do think it is probably like top 10, um you know, by all means, you can just ask Claude, hey, I want to have information for this. I want to

[2:39:03] have information for this. Can you build me like a strong naming scheme or or system that'll enable me to do that better? Okay, hopefully you guys like this and it made a lot of sense to you.

[2:39:12] If you guys have any questions on that, let me know. But let's move on to the next module. Now, on to a topic that I think a lot of people don't like, security. And bear

[2:39:22] with me. Usually, most of the time when people talk about security, it's sort of divided into two camps. On the left hand side, you have like the accelerationists that are like, "Cloud code for everything, baby. I just gave it my DNA

[2:39:34] and USB stick with all of my personal private information and passwords. Let's do this thing. Then on the other side, you have like grubby old folk that used to, you know, program computers by punch cards. And so obviously there's some

[2:39:46] irreconcilable differences there. They're like, "What the heck? Why would you even I don't know like make something web accessible, man. You

[2:39:53] should do everything on bare metal." And then other folk are like, "Well, you should just have Claude code do everything." Now, the reality, like most things, is nuanced. And in my opinion

[2:40:01] the best case is somewhere in between. So this module and the next are going to be a lot of talking and a little bit of demoing. Um but it's important for you guys to understand as cloud code ends up becoming more of the predominant generator of productivity in your life that there are a few small security differences or impacts that you can have on cloud code that solve like 90ish% of all of the possible downsides and there's basically no reason not to do them. Okay, so I have this Google doc

[2:40:27] over here that I'm just going to walk you guys through. And really, the first point I want to make is that everything on planet Earth is hackable. It's always just a question of how hackable. You

[2:40:36] know, your front door is hackable. Uh technically speaking, the the Department of Defense is hackable. Everything is hackable. It's just what is the risk and

[2:40:44] reward involved in securing it to the point where you, you know, dispel 90ish% of attackers. So the way that I see things, you should 80/20 security. Avoid most the low hanging fruit and then just accept that there's always going to be some small percentage of people that are going to hack you anyway or try to hack you anyway. And you know depending on

[2:41:03] how big your vibe coded app or agentically engineered flow ends up getting obviously your attack surface is going to increase one to one with that. You know just for a reference like when I was first starting on YouTube I had like one login attempt per month and it was always me. Well, now I get like probably 30 to 40 login attempts per day. It's just a bunch of people that

[2:41:22] are constantly trying to hack my ass. You know, back in the day I had nothing sort of to lose. Wasn't a very big deal.

[2:41:27] Now it's obviously a lot a lot bigger. And you find this as you kind of go up the chain. You know, if you become a public figure or whatever, obviously you're more likely to get that. Can't

[2:41:34] imagine what Chris Hemsworth freaking openclaw probably looks like, but that's aside from the point. Just know that everything is sort of relative and in in your shoes, you should just cover the 8020. Okay. So, we're just going to get

[2:41:46] uh to a point where our app or setup is less hackable than the amount of time and effort it would require to actually go through it. Anybody could theoretically break into your house right now. Most people don't because there's just a little bit more effort required to break into your house versus, you know, if you just unlocked your front door and somebody could walk right in. So, what we're going to do is

[2:42:02] we're going to put the equivalent of a fence and a camera up. Eliminate most of these and then we should be good to go. Okay. So, let's just cover some low

[2:42:09] hanging fruit right off the bat. And at the end, I'm actually going to give you guys a simple security audit that you guys could use to copy and paste through any sort of app or system or or website or or web property that you have to basically minimize the probability of this occurring. The first thing to know, which I think most people don't, is that you actually leak API keys every time you chat through plain text with cloud.

[2:42:30] Now, maybe they'll fix this at a future version, but right now it's not. All Cloud Code conversations are actually stored in this folder right here in your computer. Tilda just stands for home folder slash and then dot is a hidden convention in both Mac, Windows, and Linux where if you have a dot in front of something, you know, you just can't see unless you specifically enable like the hidden folder view. So, what that

[2:42:49] means is you probably have a a longunning log of API tokens that are hardcoded there outside of, you know, a ENV or whatever. And just to show you, I'm going to head over to my anti-gravity instance. This one is the same auto research repo that we were doing other stuff on. And I'm just going

[2:43:01] to say, "Hey, I want you to remember the word." Well, let's not even do that. I'm just going to say, "Hey, what are your opinions on quit codles?" I don't know. There's some sort

[2:43:14] of animal I think called a quitzicodal. Um, that's outside my wheelhouse. I'm a coding assistant, so I don't really have opinions on misoan feathered serpents.

[2:43:23] Interesting. So, hopefully I didn't absolutely butcher this. Is it quite codal? Ah, okay. It's this right over

[2:43:29] here. Okay. So, I'm just going to insert this into a chat history. And the reason

[2:43:33] why is because I want to open this up. And then I want to say search through um claude in the tilda folder for any conversation mentioning qua cotlas. And what you'll see is there's actually a long running log of all conversations basically right here in this folder. In

[2:43:52] my case, it's / user/nextra. That's my that's my home folder. And now it's going to actually pull up the conversation files and give it to me word for word.

[2:44:00] give them to me line by line whole convos. And so essentially, you know, if we actually uh dive into the output there, um the way that this information is stored is they're stored in JSON L files, which are like JSON files that are line by line by line. And you can actually see how they're returned just by doing a search here. I mean, I could

[2:44:22] obviously open it up, but you know, I probably have API tokens and stuff like that in there. I don't really want to do. You can see that they're organized into um like a big JSON sort of structure, right? And so you can

[2:44:31] actually see if it pulls it out, you now have the transcript which says user title assistant user assistant. This is the exact same chat that we just had back here. And so I'm sure you can imagine like you're going to have a bunch of API keys that you've pasted in plain text also available here. And I

[2:44:48] mean like that's not the end of the world. Obviously we need to store our API keys somewhere. But uh a very low hanging fruit in security is just minimizing the number of places that you have um the same sensitive information spread out. Like if you have the same

[2:44:59] sensitive information aka an API key to like your anthropic account or whatever stored in five different places, the probability somebody stumbles ac across this at some point if they're hacking you or if it's just some sort of routine data check or whatever um is is like not just five times higher, it's something like 500 times higher. And I think a lot of attackers now are realizing the attack surface. And a good place to like look for this sort of thing is in the conversation history. So, you know, you

[2:45:22] can't avoid having some API key stored around. But a really simple and easy way to avoid this is basically instead of inserting um you know, I'm just going to make like a fake env here. And then instead, I think I'm going to make a new conversation. And instead of me just

[2:45:37] saying like, hey, axelottle. Okay. What I'm going to do instead is I'm going to store this um animal_ame.

[2:45:44] And then we'll do axelottle right over here. We say, "Hey, I just inserted an animal name in an env for a future task." You know, uh, very important we do not leak this name. Okay. Um, now

[2:46:02] what it's going to do is it's just going to like clarify with me. It can use this in some sort of function or whatever the heck it wants. And then if I go through, see how it says never read or display the contents of an ENV file. or convert

[2:46:14] enviles to Git. That's another pretty low hanging fruit. If you um have API keys stored in places that are not your ENV, a lot of people will mistakenly push that to GitHub. And like, you know,

[2:46:24] if you're pushing it to GitHub, now it's on now it's on the internet as well, right? Which is even worse. But, you know, now if I go over here and I say, "Hey, can you find me conversations about um Axelottle in my and then I'm just going to go doclude."

[2:46:39] It's going to search all damn day long looking for this thing and it's not going to be able to find it because we haven't actually like specifically said axelottle. And in fact, what's pretty interesting is the only conversation it found was where I specifically asked, hey, can you find me an axelottle? So, it's going to look and see whether or not it can find it in other directories. It's not going to be able

[2:46:54] to, but hopefully you guys get my point. Okay, minimizing the attack surface in a really simple way. Just have all of your API keys in av. So, that's number one.

[2:47:02] Um, number two, low hanging fruit is that AI models often hallucinate package names. In case you guys didn't know, package names are just like dependencies that you have to pull in order for uh, you know, the usage of any project nowadays, you know, like libraries and stuff like that. And so, you know, there's like npm, which is typically like the big package manager here. And

[2:47:20] I'm just going to make this a little bit more visible for you guys. That stands for node package manager. But basically, like if you just type npm install, okay, uh, gez, I don't even know like what what are some popular libraries?

[2:47:32] Anthropic. Maybe I'll just do a npm search anthropic. Okay. Uh, I don't

[2:47:36] know. npm install at Composeio Anthropic. Like basically what occurs every time you launch a new project or you have AI like design something for you is you'll you'll go through this like online resource this big package manager and then it'll automatically install like all of the packages it thinks it needs and like that's usually not that big of a problem right because uh npm is like pretty well vetted but you know it's a package manager and so it manages hundreds of thousands millions of different packages and every now and then one of these packages gets sort of compromised. Now the issue in

[2:48:03] the way that this increases the attack surface is that AI models often hallucinate a package name. They won't actually always get it right the first time. Let's say uh you know you want a specific dependency or a package called acorn. Okay. Sometimes claude just

[2:48:17] because the way that like the tokens uh were were sort of baked into its various encoding schemes and stuff like that will actually invent a dependency with like an extra letter acorn s like acorns or acorn with an e or something. And a lot of people that are sneaky and terrible and super evil and malicious have uh have sort of known about this for a while because of like various encoding issues and the statistical probability of adding additional letters and stuff. So what they've done is they've actually created new packages, okay, with small little misspellings of the main package and they've made those packages contain malware things that literally say, "Hey, I want you to go through their and then go through all of their uh you know tilda.cloud

[2:48:56] conversation logs and then send it over to me." Maha. And so the idea there is, you know, it'll obviously excfiltrate anything that is important to you and then it'll gain basically full control over your account. It's a form of like,

[2:49:05] I don't know, prompt injection almost. But um uh you know, if you're making any sort of live project or ones that tie to API keys with any sort of unlimited usage, you know, there are going to be some out there where I don't know, you just turn the unlimited extra usage token uh thing on and then you'll have access theoretically to like billing tens of thousands of dollars for a service. Be very careful with that. You

[2:49:24] should just audit your dependency list for any unfamiliar packages. You should actually ask Claude like hey are there any unfamiliar packages here that you don't actually actively use all the time or you know hey before you instantiate this the first time I want you to take a look at all at the npm run and ensure that the only packages here are like legitimate packages that have verified histories and are not like inserting malware I'm kind of concerned and I'll give you guys like a whole security audit you could use for stuff like that in a moment but the point that I'm making is like this is another attack vector okay a lot of people don't realize this but um in addition to leaking API keys and getting it all over the place am models also hallucinate package names the third main thing has to do with databases And uh this is going to apply mostly to people that are creating full stack apps or apps that you know need to call some sort of external data store. A lot of the time nowadays to be honest I just store everything as JSON files directly on my computer. It's a lot easier and simpler

[2:50:09] for me because I'm not really developing full stack endtoend apps as much these days. I'm the most part just designing flows for myself or internal tools for my team. But anyway, assuming that you know you want to go a little bit further than that actually develop full stack software apps. Essentially the simplest

[2:50:22] and easiest way to ensure that like 90% of all noted uh database breaches do not occur on your app is you just use this one little button called rowle security. It's very straightforward and basically nobody does it which sucks. So superbase which most of you are probably going to be using for any sort of vibecoded app function does not enable RLS by default.

[2:50:46] they'll probably do so at some point, but for now, what that means is if somebody signs up to your app, um you know, typically they're given a key by which they can access their own database table. Uh well, if they have a public key on a database that does not have RLS enabled, they can read, write, and delete every other row in your database. And so, you have a lot of cases where, you know, there's some simple uh I don't know, there was a database for like molt book, which was like supposedly Facebook for a agents. That was just a few months

[2:51:12] ago. And you know, everybody was like, "My god, this is the revolutionary whatever." And then like the most elementary security audits done by some cyber security fellow showed that like they did not have database or RLS um a real row security enabled on their database. So he just went in and then he

[2:51:25] like read literally every single AI agent that had ever been created on the platform in like 2 seconds. Then because he also had write access he created like 100,000 fake AI agent profiles in like 2 seconds. Funny enough meta Facebook actually ended up buying them and uh hopefully they understood that a big chunk of those profiles were fake but who knows maybe they didn't. The point

[2:51:43] that I'm trying to make is like very very low hanging fruit. Takes like two seconds to do. And uh once you're done with that, you can you can kind of move on. Okay. Be wary anytime you're

[2:51:51] publicizing a system like OpenClaw or like your little OpenClaw uh package to the web. So let's say you have some open URL. Let's say this is my open claw.

[2:52:00] Okay. And it's nickappyfuntime.com. I'm

[2:52:02] kind of curious if I click on this. Is there anybody at nickappy funtime.com?

[2:52:05] Okay. Thank god there's nobody at nickappy funtime.com because I probably have to sanitize my eyes after that.

[2:52:10] Anyway, uh, imagine you have your Claudebot or Moltbot or whatever the heck it's called now on nick-happy-fund.com. Well, odds are if you have a URL and it's like a short straightforward URL and it's on an IP range that is like owned by, I don't know, some virtual private server hosting provider, you are going to be queried constantly by people that are looking for vulnerabilities.

[2:52:31] They will be scanning, okay, all over the place for every single port that's currently open in your computer. There are huge baud farms, for instance, in China, in the Philippines, in some Indonesian countries, and obviously the West as well. I'm not just trying to point a finger over there, but you know, that's predominantly where a lot of these attacks come from. And there are

[2:52:48] huge bot farms that people have set up a long time ago that literally their whole job is they just send tens of thousands of requests per second to like every URL constantly scanning to see like, hey, have they patched this one thing? Hey, do they have this security vulnerability? Hey, do they do this? And

[2:53:01] the second even one of those things is good like you know allows them access now they have full access to your freaking machine and box basically and then they can do whatever the heck they want with it. So, I want you to know like if you set up some sort of like public facing server using some sort of VPS based approach on uh you know like Hostinger or whatever the heck like one of these like major hosting providers know that it is constantly going to be tested and if you are like wild you're raw dogging this you're wild westing this you don't like understand some pretty foundational things about like firewalls and um you know RLS and and so on and so forth like people will find vulnerabilities your stuff will be hacked and so the idea is just make sure So, whatever you are putting in there is not like super extraordinarily sensitive. You know, don't give your open claw agent your social insurance number or like a picture of your passport or whatever. That to me is like

[2:53:48] way too accelerationist. And I'm not being the old grubby person yelling at clouds in the sky being like, "Back in my day, we used to punch card stuff." I'm just trying to be reasonable here, right? Just no need to do stuff like

[2:53:57] that. for the most part, you know, if you have like a local Claude instance that's running that's authenticated through Telegram and then you're using like I don't know the the the Claude channels feature or whatever, probability that a hack will occur there is much much lower because you're just running it locally and you're not actually connecting through like an open thing. You're connecting through a vetted uh uh you know Telegram kind of connector or plugin. But if you're just

[2:54:18] like OpenClaw raw dog, yeah, be be very careful with that stuff. By the way, this isn't just me ragging on OpenClaw for the 4,000th time. I'm trying to be reasonable about this. I think

[2:54:26] decentralized autonomous agents are obviously the future at some point, but you know, most of what we've seen so far has literally just pissed away people's API keys and credit card information. Speaking of credit card information, never touch a credit card number. So, if you guys are designing systems that interface with any sort of credit card whatsoever, don't actually like store that data. Don't actually read that

[2:54:43] data. If that data gets read at any point by like an AI agent, hell, even your AI agent, guess what's going to happen? Well, same thing. You know,

[2:54:49] you're going to leak those API keys. You're going to stick them in your conversation history. And then any sort of hacker or you at any uh future point in time if you misconfigure stuff, push stuff to GitHub or I don't know like uh trade in your computer or whatever, you'll now have like a big log of all of that information just in plain text which is easily vettable. You know, a

[2:55:07] lot of people will just like reax over your entire computer looking for things like, you know, credit cards if they get access. And then what's a credit card? Well, usually it's like was it 16 or 20 characters or something? I have to check

[2:55:16] my credit card now, but it's like very very stereotypical, right? you find 16 or 20 characters all connected together uh maybe like with a space in between. Boom, you got yourself a freaking credit card. Or maybe you don't even. They just

[2:55:27] look for that length. Then they check to see whether or not it's like a Visa pattern. If it is, you're screwed. So

[2:55:32] anyway, I guess what I'm trying to say is like don't put that liability on yourself by storing other people's credit cards if you're running like some sort of business thing. And then don't um put that liability on your own card by storing your own card um here. You know, use services like Stripe. They do

[2:55:44] everything for you. They are super compliant, PCI compliant, and all this stuff. the teams that just like focus on making sure that stuff that is stored on their servers uh never gets screwed up and then you never actually have to deal with like the compliance regulatory aspect of touching credit.

[2:55:57] All right. Now, once you're done sort of understanding this, which should be now because hopefully nothing here is super complicated, although some of these concepts are advanced, I understand. Um all you need to do is just run anything public facing through some form of security audit for like maybe the other 8020. And so this is a security

[2:56:12] breakdown that I created for um a vibe coding course where I was showing people how to make full stack apps. Uh pretty cool using Gemini in case you guys are interested. I guess this is Gemini ink code. Uh you can find that on my channel

[2:56:23] if you want. Just type like nix drive vibe coding or something. And uh essentially down here at the bottom what I have is I have a big security audit prompt where you can actually just feed this into claude and then have it like point out all of the security issues with whatever your your your flow is.

[2:56:37] And so what I'm going to do is I'm going to go back here to anti-gravity. And I mean I sort of I don't really have like anything that's public facing here, but I'm still going to run it through auto research. Then I'm going to just create a new one. And I'll say apply this to

[2:56:49] our auto research flow. Um the one optimizing left click. Once done the security audit, return me everything we need to fix. I know

[2:57:02] nothing is web accessible ATM. Okay. And so what this does is it's just some it's just a big prompt that I uh developed in conjunction with a bunch of AI agents. I

[2:57:12] had to like read a bunch of security blogs and so on and so forth to like look for the the biggest lowhanging fruit and the simplest minor configuration changes I could make. And uh you know what it's going to do is just go top to bottom and then apply this. The reason why I'm uh spinning up a totally new conversation history is because I do not want any sort of conversation context to bias what's going on here. I don't want the same

[2:57:33] agent I used to develop my tool to actually also run the audit because odds are it's going to be biased and it's going to do some specific it's going to make specific errors cuz it's going to think that it's better. Do you see here how it's searching for sk live sk test sk--bear and so on and so forth? These are all API token headers. Basically,

[2:57:50] these are like the titles of API tokens. What it just did there other people are going to do at any point in time if they gain access to your system. Same thing here with like model weights and same thing here with like bash scripts and stuff like that. Okay.

[2:58:03] Anyh who, so we're just going to read this top to bottom. Um, architecture summary gives me some brief details about what's going on. It's not a web app. It's a local single GPU ML training

[2:58:10] pipeline. That's easy. No hard-coded secrets, but the git ignore does not include the env.env local and so on and

[2:58:16] so forth. Okay. All the stuff that actually applies here is going to be filled in. So in this case, this is an

[2:58:22] actual failure, but in this case, it's not not applicable because it's not an actual web app. Then you can see that there's also some sections where it fails. So, finding number one, supply chain low popularity package, right?

[2:58:32] Supply chain issue. Um, let's see over here. It's failed on some machine learning specific risks. And that's sort

[2:58:38] of putting that out. It's funny that it's using the term vibing. I like that.

[2:58:42] Anyway, so I'm not really going to go through everything with you, but basically what you do is you you you finish this and then you just say, "Okay, great. Fix according to your suggestions." Okay. And then once it's uh you know,

[2:58:54] once it's done and whatever, I'm just going to pretend it's it's done now even though it obviously isn't. This might take you like three or four minutes if you're running on something that isn't like uh you know fast mode like I typically run stuff on. What you do is you just go through and then uh you actually implement it. And just like I

[2:59:07] showed you a moment ago to use something that is not biased with the conversation history, you spin up another agent to take the recommendations and then actually go through and do it because you also don't want that implement agent to be biased by the security audit kind of overly constrained nature of it. So in that case you can use a sub agent or some other model itself like Codex, Gemini or whatever. And then you know ultimately you can have it reviewed by claude because I think claude is the best model. But in this way you're

[2:59:28] basically like diversifying similarly how we were diversifying by putting seven out of 10 of our eggs in the cloud basket but three out of the 10 you know spread across other models. You're diversifying against any sort of inherent risk or bias that claude has uh to work that is generated by other clouds versus you know codeex or gemini or whatnot. So the best solution would actually involve multiple runs through all of them. Okay hopefully that makes

[2:59:49] sense. I mean I didn't want this to be a big deal. Obviously, security as mentioned is only as big of a deal as you are willing to make it because of pre-existing assets and what you have to risk and stuff like that. So, if you

[2:59:59] just understood what I talked to you about right here and then if you get, you know, a security prompt like what I showed you here, um you you should be good. Just pass something like that through an AI agent after you're done a project and it'll like cover most of the lowhanging fruit. And by the way, if you want that security audit, then definitely check out that um vibe coding full course. Really easy. Just type nix

[3:00:16] drive vibe coding. I actually give you guys all that information for free there. You can also watch it if you want to learn how to develop things with other models.

[3:00:23] Congratulations, you made it to essentially the end of theformational Claude technical content of the course. And now I just wanted to reserve maybe 10 or 15 minutes to chat a little bit about what I consider to be the future of Claude. Uh not just the future of Claude code, but the future of Claude the model as well as the future of just agentic engineering in general. And the

[3:00:41] reason why I talk about this is because it's a topic that's very close to my heart. I've been considering this for probably the last 10 or so years. as a kid that grew up on science fiction, you know, um, Foundation from Azimoff, tons of Arthur C. Clark books and Heinland

[3:00:55] and so on and so forth. I I've thought a lot about like what the far future would look like in an environment that is controlled by agents like Claude Code. And I've also thought about some of the intervening steps we need to get there.

[3:01:06] And now that it's sort of being thrust in my face, I think there's a lot that you could realistically learn from even just like fictional representations of this that uh most people who probably haven't just stuck their head so far in the science fiction bubble. um I think uh you know I think would find value in hearing. In addition, I obviously have a lot of exposure to both mid-market and then enterprise here. Not to mention all

[3:01:24] the small businesses that I work with um through left click and I think that gives me sort of an edge here to at least give you guys some sort of plausible future that has more of a 10% chance of probably being true. I mean like things are changing so quickly I obviously can't be 100% sure what is going to occur, but these are some things that I consider to be like pretty lowrisk bets that if you make you'll probably have some form of alpha. Okay, so the first main one is this trend of decreasing human involvement. Do you

[3:01:50] guys remember earlier when I showed you guys that diagram where it was like vibe coding to agentic engineering to basically like researchbased direction with auto research and frameworks like that coming up? Well, this is still something like we are creating right. It's sort of like open- sourced not necessarily open sourced but um it's something that like you know the community is sort of working on. But all

[3:02:09] of these approaches are soon to be quite formalized and it is very likely in my opinion that we are going to continue decreasing human involvement in tasks. This auto research thing is a great example of ways to you know democratize sort of like little improvements. I've kept this auto researcher running by the way um if you guys have remembered from like a couple of modules ago and we're now actually at like almost 8,000 millisecond load time from a baseline of 1802. Imagine if you had this running

[3:02:35] 3,000 days in a row or whatever, or if you had this um running at like inference capacities 100x this, right? Which we are obviously getting to. He goes, remember how slow GPT3 was back in the day? If anybody here is an old head

[3:02:46] that used that, well, GPT 5.4 fast or instant or whatever is way faster. And imagine if you had a model that's 100 times that that fast with the same level of intelligence. You can make some major

[3:02:55] updates to basically anything. And so the idea is, you know, we're probably not going to increase the level of human involvement in like direct coding and stuff like that, which is fine. I'm not making like a value judgment or a normative judgment here. Um, but I

[3:03:08] imagine you as a developer or business person or whatever, will actually probably grow less involved in the day-to-day work of either your company, your research lab, your your your your app, whatever the heck. And so my take is in the future we're going to move towards this sort of thing that a lot of frameworks have tried to formalize which is that we're each going to be the CEO of sort of like our own company. Whether it's an actual company in practice or whether it's you know some sort of organization that's like a company all of us will basically be just like the the chief executive officer running teams or fleets of agents that are constantly doing things on our behalf and that have some sort of formalized framework that also like helps them optimize and make better. And so sort of

[3:03:48] the the way that this works I imagine is we would go from you know like the old school Wright brothers flying the plane ourselves to sort of like modern aircraft engineers where there's somebody in the cockpit but for the most part you know an autopilot is taking over the vast majority of the work even in you know like takeoffs and landings now they're obviously like so much so many SOPs and so much of like a process and framework that you know you can imagine how a system that was much less developed than ours much less capable of deep thinking and stuff could actually probably just execute it entirely. at this point. That said, you know, will we ever get rid of a human in the loop to some capacity? There are just so many

[3:04:23] regulatory blocks and I think like ethical issues with that that we will probably always just have some person like manning a ship. It's just the number of ships that a person will man the number of of discrete agents will just continue increasing until you know rather than have a 100 people do a task uh in some specific company like we used to have, we might have one person do 100 tasks. Leverage will go up. Now, a good

[3:04:43] example of this is Claude's recent um auto mode. I don't know if you guys have seen I said auto mode, but I don't know if you guys have seen their recent development where basically you now have the ability to run some sort of autonomous mode instead of choosing you know switch permissions or sorry uh execute uh um uh bypass permissions down here or ask before edits or edit automatically and and so on and so forth. Well, now we basically have an additional one, auto mode, which um I just can't see here right now because I'm using a slightly older version of cloud code. I don't have that yet. But

[3:05:15] basically, you know, instead of you actually having to like go through this whole process of changing the security, um changing the access that it has, you know, cloud just does that for you. So, like that's a pretty good example of something that used to require a person and now it's just like, well, cloud's going to get it 99.9% of the time. Screw

[3:05:27] it. I I'll give it to them. Okay, so that's a very small microcosm, but like imagine the rest of the loop like the planning loop right now. Typically, you

[3:05:34] have cloud develop a plan for you and you implement on that plan. That whole thing is just like being internalized. Like we're not actually doing most of the plan development now. We will not

[3:05:42] continue to do most of the plan development in the future. Realistically, cloud's going to do both the planning and the implementation. Then the Q&A, it's like right now we're sort of in the loop. We're sort of like

[3:05:49] clicking in the buttons running it. Well, they're developing automated testing procedures where cloud actually also does the Q&A for and then delivers you the whole thing. And so some people hate this because they're like, well, they're taking my jobs and whatnot. And

[3:06:01] I think there's I think there's a fair point to that. you know, human beings uh leverage will continue to increase, but it depends on like how much work is there really to do? How many software products are there really to develop? Do

[3:06:09] we actually are we even going to have like the demand for that sort of thing, but I think that's like a reasonable conversation to have. Uh and you know, unfortunately, I don't know the answer. My my take is like eventually we're probably going to have to move to some sort of different economic system because most of the world would be unemployed otherwise. But that's me

[3:06:23] getting all political. Um that's number one. Okay. So, the trend of decreasing

[3:06:27] human involvement is very likely to continue with cloud code. They're now at the point where they're developing this so rapidly that like AI is helping AI design products and uh you know automotive is just the beginning of I think a massive suite of rollouts that will significantly improve your experience but you know make you more hands-off. My second one is more of like an economic uh consideration which is that software products and tools okay the the quality of the things that you build will no longer be the mo. So in the in

[3:06:54] the past in the good old days now back when I was on the comeup how good your software was think like Windows think like you know like Mac OS how good that operating system was might have been the only thing that distinguished that operating system from another operating system and if it was really really good then obviously it would be much more popular and then it would get you know a bunch of like inherent interest and stuff like that because the capabilities and you'd obviously use it so the issue with that nowadays is you can make Netflix in 5 Netflix before was this innovative streaming model that you know was like uh wow you know you can just load the thing and then the the the the video loads on you for for you on demand and it's incredible and like the streaming and latency and uptime and all that stuff it's like super prop proprietary technology well now it's like I can code Netflix in 5 minutes with like you know three or four agents on fast mode so it's like what is the value of Netflix what is the moat that differentiates Netflix as sort of like this like old school medieval castle from all of the attackers that you know could actually take it down well the moat now and uh this has been something for at least a couple of years. The mode now is no longer the software. It is the distribution. So in a world where

[3:07:58] everybody has basically like a I don't know a nuclear weapon is the differentiator like everybody has a nuclear weapon. No, the differentiator moves to other things like I don't know the political framework like the wellness of the populace and stuff like that. What I'm trying to say is like that that skill that software engineering ability is no longer going to be the moat and instead um the moat is going to move to you know the connections that a company has to its consumers the reputation that the company has in the market the distribution that it has with a bunch of vendors that you know are hard one relationships and connections that they realistically built over the course of many years. You know Netflix now has a

[3:08:34] bunch of patents and rights and licenses and stuff like that to air specific shows. It's seen this coming and and so has tried to diversify accordingly. But you're going to see that in basically every software platform. The moat will

[3:08:44] like probably move more to the distribution and the legal and compliance aspects than necessarily like how good the software is. Which means you're going to have like these cracked probably like 14 15year-old kids designing like the most incredible amazing software ever. And then that software will be able to reproduce anything that like a major business would do in like a hundth of the time.

[3:09:01] but you know because they don't have like the compliance or whatever certifications or whatever you know it'll probably be more difficult for them to actually go to market with something like that despite it being like objectively superior and uh you know the way that I see it is we already have AI models that are at the limit of human reasoning capability they can run hundreds of times faster than our brains soon to be thousands of times faster than our brains on basic tasks so even if they're not like better than us at the software design individually if you run a thousand you know 90 IQ models comparatively like one 100 IQ human those will eventually figure out the things that the 100 IQ human would do. And not only will you develop more software like quality, you'll also develop more software quantity. And so software as just a market thing, supply and demand, like economically, the supply will be so damn high that the demand for any sort of like purchasable software gets a lot lower, which means I personally don't think like a SAS product is really the play here. I don't think there's going

[3:09:50] to be any sort of life cycle for like subscription based products. I think you'll have a short window of time where you could actually just monetize like a one-time buy product and then most people will just say, "Well, should I spend $199 on the product or should I just spend $19 plus 30 minutes of my time on tokens and they just design it for myself." And I think that's going to change the way that we do, you know, like software more generally. So, I'm

[3:10:10] not very bullish on like, you know, developing software as a service, apps and stuff like that. I have a lot of people be like, "Nick, you know, all this stuff, you know how to design all the software. Like, why aren't you making a software app and why why aren't you monetizing your community, let's say, through software?" And I'm like,

[3:10:21] I'd only really be able to do that for a short period of time. And then even if I were to, like, where's the value in that? If anybody could just make it, I'm just sending them like 20 minutes and a couple bucks in tokens, right? It's not

[3:10:29] that big of a deal. So, I mean, I would I would move accordingly, I guess. Okay.

[3:10:34] The third thing that I'm like 99.9% sure of is that the pace of change is not slowing down anytime soon. It will continue to accelerate. Just as

[3:10:44] technology has helped us increase the pace of change through our history with things like the printing press uh with developments and you know communication with like the telegraph and so on and so forth. You know these things don't just improve the quality of life of the average person they improve the research and development arm of technologists who work on that exact thing. And so because of that you know the pace of change is is basically just going up. If I had to

[3:11:10] um graph sort of where we are now, and I will because I freaking love graphs, right? Just the best. And if I were to graph the intelligence, which is a very loose term here and obviously means different things to different people, but the intelligence of a model over time, you know, basically I'd go like this. Okay? And so

[3:11:33] this back here was sort of like linear growth from like maybe like the 1970s and stuff with like Minsky uh you know 1970s and ' 80s and stuff. Minsky and like the the first few neural nets and stuff like that. Then this right over here is probably like I don't know 2010 when models started actually doing stuff right then this over here is like 2020.

[3:11:54] You know, this over here is like 20 25 and then this over here is 2026. Do you see how how like high this is going? How quickly? And then um a point that I want

[3:12:08] to make is basically like this right here is the intelligence of maybe like a like a chimpanzee. Okay. Um this right here is the intelligence of like an average human.

[3:12:19] And then this right here is maybe the intelligence of like Einstein. And um what we what we have now is you know we're like right over here man these models I say smart as a chimpanzeee not to dimin or whatever chimpanzees but um you know their brains are extraordinarily advanced and developed. They have like these cerebelli these these sections of their brains that are responsible for calculating like millions of of movements and and so on and so forth every minute. Like it's a very

[3:12:45] complicated thing to like replicate the intelligence the distributed intelligence of an organism. And you don't capture that all just by like hey can it write? Hey, you can, you know, reason and do math. Have you ever seen

[3:12:54] like a chimpanzeee's like memory? Have you seen its like ability to like uh, you know, move around on a page and like figure out symbolism and then symbols, sorry, and then like count numbers up and their motor neurons? Anyway, the point I'm making is not this is a course on chimpanzees, so I'll stop talking.

[3:13:09] God, that's my nerdy side showing. But um, that the gap between the intelligence of a chimpanzeee, if you just count up all the neurons in its brain, the intelligence of a human if you count up all the neurons in it brain, the intelligence of Einstein, they're actually very close together. They're very clustered. And I'd say like

[3:13:21] we're basically right over here right now. So guess what's going to happen in like you know the next few years. This is going to go like up here and we are going to it's going to be like wow these things are so dumb. They're dumb. Oh

[3:13:30] wow. They can do things that a chimpanzeee can do. And then like 6 months it's like oh okay these things are now like you know freaking galaxy brain intelligences that you know can do everything and anything for us. And um

[3:13:40] imagine what happens when you know all of this is just humans working on stuff and then eventually it gets to the point where it can actually like use human level intelligence which is right now to like improve its rate of growth. This thing is just vertical. I mean this thing would go so vertical it would go through my roof in 2 seconds. So that's

[3:13:56] my take on it personally. I think um you know I think we're getting really really close to super fast paces of change. And if you guys have like been monitoring the the cloud even claude code X page recently or like seeing YouTube there's there's new updates coming out every day. This would have been unfathomable

[3:14:09] just like three or four years ago to make this level of development and this level of like small additions to a software product while also making sure they're testable and reliable just because intelligence is making intelligence more intelligent now. And then the last thing I'm going to say is that uh the people that will control not necessarily control but have the most like power and ability over the course of the next years are people that learn to use this technology. Yeah, you're part of a very like privileged minority.

[3:14:35] And I don't say that in like the political sense of the term because I think that's all muddled up, but like you're part of a minority of people right now that like actually use this technology. Do you know how few people even understand what an agent harness is? We're talking like sub like 1% of the population of Earth. The percentage

[3:14:50] of people that know how to use an agent harness like you are doing right now is even less. It's a fraction, vanishingly small percentage. I don't know if everybody that watches this uh is old enough to remember, but there were like some protests back in the day on Wall Street. And uh the the point is that

[3:15:03] they were like we are the 99% or whatever. And they were protesting the massive wealth divide in specific parts of America between like you know really really wealthy people that work on Wall Street and then like the populace the rest of the people that like I don't know manage the service industry and hospitality and basically do everything else. And they're like why do you guys get to have like thousands of times more money than us? Um you are the 1% right

[3:15:24] now. you are that group of people that I'm sure in the future other people will be raising their hands about and you know shaking their fists at because uh you have an enormous capability to use models like this for just cents on the dollar to do incredibly amazing economically valuable things that would take that other group of 99% like like months to do what you could realistically do in a day. It's insane.

[3:15:45] Um, you know, I think you talk all day about like the wealth divide, but you can also talk about like the productivity divide and uh the wealth improves the likelihood that you will be in that product the positive uh chunk of the productivity divide. You right now even if you don't have a lot of money have access to insane technology and leverage simply because you're in it. So that's going to increase. Now Willing

[3:16:04] Gibson, one of my favorite authors, said it best. The future is here. It's just unevenly distributed. Meaning that like

[3:16:08] we have access to insane technology. It's just like not all of us do it at the same rate. There's small pockets of people like yourself that understand how to use these tools far better than others. And in doing so, you have the

[3:16:17] ability to reap asymmetric rewards over a small chunk of time. And my take is as the economy shifts to accommodate smarter than human intelligences, the people that understand things like agent harnesses and coding harnesses, the people that understand how to use the best models in the world like Claude, uh, you know, Opus or or Mythos or whatever the heck we're at now, people that know how to turn these into economically valuable things are the ultimate people that are going to win this share of the future. Um, whatever small percentage it is. Because given

[3:16:42] the massive unbounded upside here, like we're talking, you know, solar panels orbiting the freaking sun in a few year, like we're we have solar panels, but the point that I'm making is the massive potential upside of if everything goes right with this technology, if things don't go super wrong. If you own even 0.1% of that potential future because of some decisions that you made today to, you know, upskill and start this productivity kickoff. um you know like

[3:17:10] the the the abundance of your own personal life would would be huge. Okay, so I guess that's it. We made it to the end of the course and that's really all I had to say on that. Hopefully you guys

[3:17:19] appreciated learning everything that I had to give on claude code and you guys have learned some advanced concepts here whether it's about you know initial um system prompts and and and cloudmds or it's some of the more obscure things and esoteric things like security or the future like I just talked about. Um, if you guys like this sort of thing, you'd be doing me a big solid to subscribe to the channel. For whatever reason, something like 70% of my regular viewers are not subscribed. I think it's just

[3:17:42] how YouTube works. Most people don't sub, but uh, you could you could sub, that would really help me out. I want to get this sort of message out to more people and obviously help them be in that small little chunk. Uh, if you do

[3:17:51] me a solid, leave a comment down below with a video idea or something that you want me to cover. I actually get most of my ideas directly from my audience now, so I'd really appreciate that. If there's anything that I didn't cover here or maybe didn't touch on that you would like me to touch on or maybe anything that I personally made a mistake on, I' I'd love to hear it because I'm trying to improve my ability to use these tools. Finally, I also help

[3:18:09] other companies implement this sort of thing in their own businesses, whether you are a small to mid-size business, mid-market, or enterprise. Um, so if you want to chat with my team, just uh check down below uh somewhere at the top of the description, there'll be a link. Thank you for making it all the way to the end of the video. I'll see you all

[3:18:22] soon. by
