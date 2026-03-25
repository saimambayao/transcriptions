# GSD + Claude Code, Antigravity: This Simple PLUGIN makes your Claude Code & Antigravity 2X BETTER!

**Channel**: AICodeKing
**Duration**: 12:35
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=YfJwFZ9L5JI
**Transcribed**: 2026-03-26 01:37

---

## Organized Notes

**What GSD Is and Why It Exists**

- **GSD (Get Shit Done)** is an open-source workflow system that installs on top of AI coding tools: **Claude Code, Codex, Gemini CLI, Open Code, Copilot, Cursor, and Antigravity**
- Already has **tens of thousands of stars** on GitHub — not a new IDE or model, but a **context engineering layer** for coding agents
- Solves the problem the repo calls **"context rot"** — when AI agents lose coherence over long sessions: answers get shorter, earlier decisions get forgotten, random changes creep in
- Positions itself against **"enterprise theater"** — no Jira-like overhead for solo projects
- In the same family as **Specit, OpenSpec, BMAD, and Taskmaster**, but with a more **stripped-down solo-user mindset**
- Core philosophy: **the difference between a chaotic agent and a reliable one is not the model — it is the workflow wrapped around the model**

*Quotable Quotes:*

> "The real advantage increasingly comes from harness design, context engineering, verification loops, and how work gets decomposed." [10:46]

> "The difference between a chaotic agent and a reliable one is not just the model. It is the workflow wrapped around the model." [11:02]

**Installation and Runtime Support**

- Install with `npx get-shit-done-cc@latest` — asks which runtime and whether global or project-scoped
- Supports **Mac, Windows, and Linux**
- Verify with `/gsd help` (Claude Code, Gemini CLI) or `$args-help` (Codex)
- **Codex support is skills-first** — installs skill folders into the Codex directory rather than custom prompts, fitting how Codex already works

**The GSD Workflow (6 Core Commands)**

1. **`/gsd map-codebase`** — Spawns **parallel agents** to analyze architecture, conventions, stack, and pain points before any feature work begins
   - Frontloads understanding so the model doesn't start changing code before it knows the codebase

2. **`/gsd new-project`** — Kicks off planning: asks questions, does research, extracts requirements, creates a roadmap
   - Generates persistent files: `project.mmd`, `requirements.mmd`, `roadmap.mmd`, `state.mmd`, and a `planning-research/` folder
   - Builds **persistent project memory** before implementation decisions

3. **`/gsd discuss-phase`** — Surfaces **gray areas** before planning begins
   - For UI: asks about layout, density, interactions, empty states
   - For API/CLI: asks about response format, flags, error handling, verbosity
   - Key insight: **the model is not bad at coding — it is bad at guessing what you meant**

4. **`/gsd plan-phase`** — Researches the phase, creates **small atomic task plans**, verifies against requirements
   - Plans are **small enough to run inside fresh context windows** — the core trick
   - No longer asking the agent to remember an entire product conversation while implementing task 12

5. **`/gsd execute-phase`** — Groups plans into **waves based on dependencies**
   - Independent plans run in **parallel**; dependent plans wait for earlier waves
   - **Vertical slices parallelize better than horizontal layers** — reduces conflicts, keeps each agent grounded in meaningful outcomes
   - Creates an **atomic git commit for each task** — cleaner history and rollback points

6. **`/gsd verify-work`** — Extracts **testable deliverables** and walks through them one by one
   - Goes beyond "code compiles and tests pass" — checks user-facing correctness (login flow, dashboard state, onboarding)
   - Can spawn **debug agents** and create fixed plans for re-execution if something fails

- **Bonus: `/gsd next`** — Figures out the next logical step in the workflow automatically, keeping momentum

**Practical Example: Adding Billing + Admin Dashboard to a SaaS App**

- Without GSD: one huge prompt leads to drift — Stripe gets added but edge cases ignored
- With GSD: **discuss-phase** surfaces billing edge cases, **plan-phase** breaks it into atomic tasks, **execute-phase** runs them in parallel waves, **verify-work** tests actual deliverables
- Much saner than hoping one giant prompt handles architecture, edge cases, execution, and verification

**Who GSD Is For**

- People who **already believe AI can do serious coding** but are tired of the chaos
- **Solo developers, indie hackers, and power users** wanting structure without enterprise overhead
- Best for **medium-to-large features or multi-phase projects** where context management is the bottleneck

**Honest Downsides**

- **Not magic** — the repo says "if you know clearly what you want, this will build it for you." Vague product thinking still produces vague output
- **Overkill for small tasks** — renaming a function or fixing a small bug doesn't need discuss/plan/execute/verify
- **Skip-permissions recommendation is risky** — the repo recommends `--dangerously-skip-permissions` for frictionless flow, but beginners should be careful
- **Terminal-first and workflow-heavy** — no polished GUI or visual dashboards; there's a learning curve
- **Direct tone** — even the name may be a hard sell in buttoned-up enterprise environments

**Cost and Bigger Picture**

- GSD is **open-source and MIT licensed** — but doesn't eliminate model costs from expensive models and parallel agents
- Part of a **bigger shift**: raw models keep improving, but the real advantage comes from **context engineering, verification loops, and work decomposition**
- Repo: `github.com/gsd-build/get-shit-done`

---

## What This Means for Your Work

GSD validates the architecture you've already built intuitively. Your 129-skill Claude Code system with the Obsidian vault memory layer, parallel agents, and fact-checking pipeline is essentially a hand-crafted version of what GSD tries to provide out of the box. The difference: your system is domain-specialized (Bangsamoro governance, legislative drafting, cooperative development) while GSD is generic coding workflow.

**What GSD gets right that you should audit in your own setup:**

- **Context rot is your biggest risk at scale.** You're building 9+ platforms as a solo dev. When you context-switch between e-Bangsamoro, MoroMarket, Tarbiyyah-MS, and OBCMS in the same week, the accumulated context in each session degrades. GSD's "fresh context window per atomic task" principle maps directly to how your `/devwork` and `/sp-executing-plans` skills should decompose work — but are you actually chunking small enough? If a single Claude Code session is handling more than one vertical slice of a feature, you're inviting context rot.

- **The discuss-phase gap.** Your `/grill-me` skill already does requirement interrogation, and `/write-a-prd` captures specs. But GSD's discuss-phase is narrower and faster — it's not a full PRD, it's a 5-minute "surface the gray areas for THIS specific phase." For your legislative work (drafting bills, resolutions), this is less relevant because requirements come from law. But for e-Bangsamoro feature development where product decisions are ambiguous, you may be skipping this step and letting the model guess.

- **Verification beyond tests.** GSD's verify-work step — checking user-facing deliverables, not just test suites — is something your `/webapp-testing` (Playwright) skill already supports. But the pattern of automatically extracting testable deliverables from the plan and walking through them systematically is worth formalizing. Right now your verification is manual; GSD makes it a workflow step.

- **Parallel execution waves.** You already use parallel agents heavily, but GSD's dependency-aware wave system (independent tasks in parallel, dependent tasks sequential) is more structured than ad-hoc parallelism. For e-Bangsamoro's 4-portal architecture, this matters: the Parliamentary portal's committee module can parallelize with the Budget portal's appropriation tracker, but both depend on the shared auth system.

**What you don't need from GSD:**

- The `map-codebase` command — your CLAUDE.md files and `/context` skill already serve this purpose, and they're richer because they include domain knowledge (BOL provisions, BDP goals, BARMM officials) that a generic codebase mapper would miss.
- The persistent file format (.mmd files) — your Obsidian vault + skills-bucket is a more powerful persistence layer.
- The installation overhead — adding another workflow layer on top of your 129 skills would increase complexity without proportional benefit.

**Concrete next steps:**

1. Audit your `/devwork` skill to ensure task decomposition produces plans small enough for fresh context windows (GSD's core insight)
2. Add a "phase discussion" step to `/devwork` before planning — a lighter version of `/grill-me` focused on surfacing ambiguities for the current phase only
3. Formalize verification checklists in `/sp-verification-before-completion` to extract and test user-facing deliverables, not just run the test suite

### How This Can Improve Your Claude Skills and Workflows

**Skill improvements:**

- **`/devwork`** — Add GSD's atomic task decomposition principle: each task plan should be executable in a fresh context window. Currently devwork handles feature-level scope; it should explicitly chunk into context-window-sized units with dependency ordering.
- **`/sp-executing-plans`** — Incorporate dependency-aware wave execution. Instead of dispatching all parallel agents at once, group tasks into waves where independent tasks parallelize and dependent tasks wait. This is more structured than the current "dispatch independent tasks" approach.
- **`/sp-verification-before-completion`** — Add automatic deliverable extraction: before verifying, parse the plan to identify user-facing testable outcomes (not just "tests pass" but "user can log in, dashboard renders correct state, billing flow completes"). Use `/webapp-testing` to verify each.
- **`/grill-me`** — Create a lighter "phase-discuss" mode for mid-implementation ambiguity surfacing, separate from the full pre-planning interrogation.

**Workflow changes:**

- **Context window hygiene** — GSD's central insight is that context rot kills agent quality over time. For your 1M context window, this means being more disciplined about when to start fresh sessions vs. continuing. Your `/session-summary` skill captures what happened, but you should also capture the plan state so a new session can pick up with a clean context.
- **Wave-based parallel agents** — Instead of ad-hoc `/sp-dispatching-parallel-agents`, formalize a wave scheduler: analyze task dependencies, group into waves, execute wave 1, then wave 2, etc. This prevents the scenario where a parallel agent modifies shared code that another parallel agent is also touching.

**Project-specific applications:**

- **e-Bangsamoro** — The 4-portal architecture (Parliamentary, Ministerial, Budget, Citizen) is exactly where wave-based execution shines. Portal-specific features can parallelize; shared infrastructure (auth, permissions, database) must be sequential. GSD's dependency graph model would prevent the merge conflicts that come from parallel agents touching shared modules.
- **MoroMarket** — As a marketplace with cooperative, SE, and MSME storefronts, feature development often involves both the seller portal and buyer interface. GSD's vertical slice approach (end-to-end for one user flow) is better than your current horizontal approach (build all API endpoints, then all frontend).

**No new skill needed** — GSD's workflow maps onto your existing skills (`/devwork`, `/grill-me`, `/sp-executing-plans`, `/sp-verification-before-completion`). The improvement is in how these skills decompose and sequence work, not a new capability.

---

## Transcript

[00:02] Hi, welcome to another video. So today I want to talk about one of the most interesting open-source workflows for AI coding that I have seen in a while and it is called Get Done or GSD. The name is a bit aggressive, I know, but the repo has been blowing up for a reason. It already has tens of thousands of stars on GitHub. And this is not another flashy AI IDE, and it is not a new model either. It is basically a workflow system you install on top of tools like Claude Code, Codex, Gemini CLI, Open Code, Copilot, Cursor, and Antigravity. So your agent can build larger projects without completely losing the plot halfway through.

[00:39] Now the core problem GSD is trying to solve is something the repo calls context rot. And honestly, if you have used AI coding agents seriously, you already know what that means. You start with a clean prompt. The model is brilliant for the first few turns. Then the context gets bloated. The answers get shorter. It forgets earlier decisions. It starts changing random things. And by the end, you are babysitting it more than it is helping you. GSD tries to solve that with a very opinionated spec driven workflow. And I think that is why so many people are excited about it.

[01:12] So let's get right into it. First, what actually is GSD? The simplest way to think about it is this. It is a context engineering layer for coding agents. Instead of throwing one giant prompt at Claude Code or Codex and hoping for the best, GSD gives you a repeatable process. You map the code base, create a project, discuss a phase, plan the phase, execute it in smaller pieces, verify the work, and then ship it. So rather than one huge messy session, you get smaller, more focused bursts of work with checkpoints in between, which is pretty amazing to be honest.

[01:43] And this is also why it feels different from a lot of the other spec-driven tools out there. The author very clearly positions this against what he calls enterprise theater. So this is not trying to turn your personal side project into Jira with extra steps. It is basically saying the model does better when the work is scoped properly. The research is separated, the plans are atomic, and the verification is explicit. If you have tried tools like Specit, OpenSpec, BMAD or Taskmaster, this is in that same family but with a much more stripped down solo-user mindset.

[02:12] Now, let's talk about installation because this is one of the nicer parts. To install it, you basically open your terminal and run npx get-shit-done-cc at latest. Then the installer asks which runtime you want and whether you want it globally or just for the current project. One installer now supports Claude Code, Open Code, Gemini CLI, Codex, Copilot, Cursor, Antigravity or all of them in one go. It also works on Mac, Windows, and Linux, which is obviously nice. If you're using Claude Code or Gemini CLI, you can verify it with /gsd help. If you're using Codex, you use dollar-args-help.

[02:44] And one small but important detail here is that Codex support is skills first. So instead of custom prompts, it installs skill folders into your Codex directory. I like that a lot because it fits how Codex already works instead of awkwardly forcing a different model.

[02:57] Now let me walk you through the actual workflow because this is where GSD really makes its case. The first really smart command is /gsd map-codebase. And if you already have an existing project, I think this is the right place to start. What it does is spawn parallel agents to analyze your architecture, conventions, stack, and pain points. So later when you ask for a new feature, the system already knows how your project is structured. This is huge because one of the biggest problems with agentic coding is that the model often starts changing code before it truly understands the codebase. GSD tries to frontload that understanding.

[03:40] But before we get into that, I want to quickly talk about today's sponsor On Demand. If you've been trying to build AI agents, you know the pain. You find one tool for summarization, another for web scraping, another for data analysis, and then you spend more time stitching them together than actually getting work done. On Demand solves this. On Demand is a platform where you can discover, assemble, and automate AI agents all in one place. They have an agent marketplace with over 400 agentic tools ready to go. So instead of hunting for tools and figuring out APIs, you just browse, pick what you need, and deploy. That gives you over 1,200 possible agent combinations, which is insane. But the cool part is the playground. You take these agents and assemble them into a workflow for your exact use case. And once it works, you turn it into a full automation using their flow builder. It's visual, no code, and lets you chain multi-agent workflows that run repeatedly without you touching anything. You can also bring your own models, and it's privacy first with secure connectors. Sign up through my link in the description, and you'll get $5 in free credit. Go check it out.

[04:35] After that you run /gsd new-project. This kicks off the planning flow. It asks questions, does research, extracts requirements, and creates a road map. According to the repo, it generates files like project.mmd, requirements.mmd, roadmap.mmd, state.mmd, and a planning research folder. So now you're not just chatting, you are building a persistent project memory before you start letting agents make a ton of implementation decisions.

[05:05] Then comes what I think is one of the most underrated parts of the whole system and that is /gsd discuss-phase. This is where the tool tries to surface all the gray areas before planning. So if you're building a UI, it asks about layout, density, interactions, empty states, and all that. If you are building an API or a CLI, it asks about response format, flags, error handling, and verbosity. So instead of the model silently making product decisions for you, GSD tries to drag those decisions into the open. A lot of the time the model is not bad at coding. It is bad at guessing what you meant. So this step is actually super important.

[05:42] After discussion, you go to /gsd plan-phase. This is where GSD researches the phase, creates small atomic task plans, and then verifies those plans against the requirements. The repo describes these plans as being small enough to run inside fresh context windows. And that is the whole trick. You're no longer asking the agent to remember an entire product conversation while also implementing task number 12. You are chunking the work so the agent can focus on one bounded unit at a time.

[06:07] Then you run /gsd execute-phase. And this is probably the coolest part for anyone who likes parallel agents. GSD groups plans into waves based on dependencies. Independent plans can run in parallel. Dependent plans wait for the earlier wave to finish. The repo even emphasizes that vertical slices parallelize better than horizontal layers, which is exactly right. If you split work into end-to-end slices, you reduce conflicts and you keep each agent more grounded in a meaningful outcome. Chef's kiss. Really good stuff.

[06:40] Another very nice touch is that GSD aims to create an atomic git commit for each task. So when execution is done, you do not just have a pile of mystery changes. You get cleaner history and cleaner rollback points, which is pretty great.

[06:51] Then comes /gsd verify-work. And I genuinely think more tools should copy this. Most AI coding workflows stop once the code compiles or the tests pass. But we all know that is not enough. A feature can pass tests and still be wrong in obvious user-facing ways. So GSD extracts testable deliverables and walks you through them one by one. Can the user log in? Does the onboarding flow work? Does the dashboard render the right state? If something fails, it can spawn debug agents and create fixed plans for re-execution. So the workflow does not just end at code generation. It actually tries to get you to working software.

[07:30] And if you do not want to manually think about which command comes next every time, there is also /gsd next which figures out the next logical step in the workflow for you. That might sound small, but it is actually nice for keeping momentum.

[07:46] Now let me make this more concrete with a simple example. Let's say I already have a SaaS app and I want to add billing plus a proper admin dashboard. Normally, if I dump that into a coding agent in one huge prompt, it will probably start fast and then drift. Maybe it adds Stripe but ignores edge cases. With GSD, I would run discuss-phase to surface billing edge cases, plan-phase to break it into atomic tasks, execute-phase to run them in parallel waves, and verify-work to test the actual deliverables. That is much saner than hoping one giant prompt gets everything right.

[08:14] Now, that is really the whole value proposition here. GSD is a response to raw vibe coding. Instead of hoping one giant chat can handle architecture, edge cases, execution, and verification all at once, it separates discovery from planning, planning from execution, and execution from verification. For bigger projects, that is just a much saner approach.

[08:32] Now, who is this actually for? I think GSD is for people who already believe AI can do serious coding work, but they are tired of the chaos. It is for solo developers, indie hackers, and power users who want more structure without pretending they work at a 50 person software company. If you are building medium to large features or multi-phase projects, this is a really good option for sure.

[08:57] But I also want to be honest about the downsides because there are some. First, this is not magic. The repo literally says something along the lines of if you know clearly what you want, this will build it for you. And that first part is important. If you do not know clearly what you want, no amount of workflow is going to save you completely. The plans might be cleaner, the context might be fresher, but vague product thinking still leads to vague output. So I would not look at GSD as some kind of miracle fix for unclear requirements.

[09:20] Second, for small tasks, this can absolutely be overkill. If you just want to rename a function, fix a small bug, or tweak one component, you probably do not need a whole discuss, plan, execute, verify cycle. In those cases, just ask your coding agent directly. GSD makes the most sense when the task is big enough that context management becomes the main problem.

[09:35] Third, the repo recommends running Claude Code with the --dangerously-skip-permissions flag for a frictionless workflow. And look, I understand why approving every tiny command is extremely annoying and it does slow the agent down. But I would still be careful here. On a machine you trust, in a project you understand, maybe that is fine. But I would not tell a beginner to blindly enable that everywhere and forget about it. So take that part with a grain of salt and use some common sense.

[10:04] Fourth, the whole thing is still very terminal first and workflow heavy. If you want a polished GUI with a bunch of visual dashboards and onboarding, this is not that. So there is definitely a learning curve. And fifth, the tone of the project is very direct. Personally, I think it is refreshing. But if you work in a very buttoned up enterprise environment, even the name alone might be a hard sell, which is kind of funny, but also true.

[10:28] Now, I do want to mention the cost angle because that is always important. GSD itself is open source and MIT licensed, which is great, but it does not magically make model costs disappear. If you're using expensive models and spawning parallel agents, you can still burn through tokens. For unlimited plans like Codex, Copilot, Cursor, and Antigravity, that makes the idea much more valuable.

[10:46] I also think this project is part of a bigger shift we are seeing right now. The raw models keep getting better, yes, but better models alone are not enough. The real advantage increasingly comes from harness design, context engineering, verification loops, and how work gets decomposed. GSD leans heavily into that idea. It basically says the difference between a chaotic agent and a reliable one is not just the model. It is the workflow wrapped around the model. And I think that is exactly right.

[11:11] So what's my verdict? I think GSD is one of the most practical open-source workflow layers for AI coding that I have seen recently. It is opinionated, but in useful ways. It understands that context management is the real bottleneck for larger agentic projects. It gives you a repeatable spec-driven process without drowning you in enterprise nonsense. And the support for multiple runtimes makes it even more compelling.

[11:34] It is not perfect. It can be overkill for small tasks. The skip permissions recommendation will not be for everybody. And if you hate terminals or structured workflows, you're probably not going to enjoy this. But if you're serious about building larger things with coding agents, I think this is absolutely worth trying.

[11:58] So this is great for sure. If you want to check it out, the repo is github.com/gsd-build/get-shit-done. Install it with npx get-shit-done-cc. Pick your runtime and see if this workflow clicks for you. Overall, it's pretty cool. Anyway, let me know your thoughts in the comments. If you like this video, consider donating through the super thanks option or becoming a member by clicking the join button. Also, give this video a thumbs up and subscribe to my channel. I'll see you in the next one. Until then, bye.
