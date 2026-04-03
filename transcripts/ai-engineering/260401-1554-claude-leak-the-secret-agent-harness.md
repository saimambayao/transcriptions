# Claude Code LEAK: What They Don't Tell You

**Channel**: Mehul Mohan
**Duration**: 18:24
**Language**: English (manual) [yt-dlp subtitles]
**URL**: https://youtube.com/watch?v=GEbfZs-FK6E
**Transcribed**: 2026-04-01 15:54

---

## Organized Notes

**The Anatomy of the Leak: Source Maps and Harnesses**

- **Source Map Mechanics**: The leak occurred because the **source map** (`cli.js.map`, a 60MB file) was accidentally published to **npm**. Source maps act as a bridge between minified production bundles and original source code, allowing for literal reconstruction of the entire 500,000-line codebase. [01:22], [05:10]
- **Harness vs. Model**: Mehul argues that the **harness** (the agentic logic, prompt strategy, and tool loop) is often more valuable than the raw model itself. While the model provides the "raw intelligence," the harness is the "front-end" that manages expensive prompt caching, complex agentic loops, and safety guardrails. [08:19], [09:59]
- **The Bun.js Debate**: While early reports blamed a Bun.js production server bug, Bun's primary maintainer (Jared) has claimed the issue is unrelated, as Claude Code does not use Bun's `serve` function in that way. [16:32]

*Quotable Quotes:*

> "In the AI world, your harness is the front-end, and the model is the back-end. What got leaked is the harness—the most valuable part of the product's differentiation." [08:41]

> "Claude dreaming is a reflective pass where it synthesizes what it learned into durable, well-organized memory so future sessions can orient quickly." [12:11]

**Advanced Architectural Features**

- **Chyros (Proactive Agent)**:
  - **The Tick Prompt**: A persistent background assistant that receives a "tick" every few seconds to decide whether to act.
  - **Blocking Budget**: It has a strict **15-second blocking budget**—if an action would interrupt the user for longer, it is deferred to avoid being annoying. [09:54], [10:35]
- **Ultra Plan (Remote Planning)**:
  - **CCR Runtime**: Spins up a remote **Claude Container Runtime** (CCR) powered by **Opus 4.6**.
  - **Teleportation**: Uses a browser-based UI for users to monitor the 30-minute planning process. Results are "teleported" back to the local terminal once approved. [10:56], [12:07]
- **The Dreaming Logic (Memory Consolidation)**: 
  - **Three-Gate System**: 
    1. **Time Gate**: At least 24 hours since the last dream.
    2. **Session Gate**: At least 5 sessions since the last dream.
    3. **Log Gate**: A mutex lock to prevent concurrent dreams. [11:13], [11:24]
  - **Dreaming State**: The sub-agent is granted read-only bash access to summarize project context into persistent memory files. [12:11]

**Ethical and Legal Evolution**

- **"Free Code" and Legal Loopholes**: Developers are porting the leaked logic to **Python** and **Rust**. By creating these "derivative works," they aim to bypass DMCA takedowns that target direct forks of the TypeScript source. These versions often strip out telemetry and safety guardrails. [17:14]
- **Undercover mode**: Internal model code names like **Capibara**, **Penguin** (Fast mode), and **Tangu** (internal prefix) are revealed as targets for the code's "internal info leak protection" modules. [14:45], [15:54]

---

## What This Means for Your Work

The distinction between the **Harness** and the **Model** is the single most important takeaway for your **MoroTech** and **e-Bangsamoro** engineering. It validates your strategy of building a robust "skills-bucket"—you aren't just sending prompts to Gemini; you've built a harness that manages state across your **Obsidian vault** and local filesystem. The **Dreaming Logic** (the three gates) provides a perfect blueprint for how you should automate your own **housekeeping** tasks. Instead of manual index updates, you can now design a "Dream Skill" that triggers specifically after 5 sessions or a 24-hour window to consolidate your transcripts into your **ai-engineering** knowledge area.

For your work with the **BTA Parliament**, the **Ultra Plan** (remote planning) concept can be adapted for massive legislative drafts. You could set up a "Parliamentary Drafting Lab" where a background agent spends 30 minutes reasoning through a complex bill like the **Bangsamoro Health Code**, then presents a "teleported" summary for your review in the browser.

### How This Can Improve Your Gemini Skills and Workflows

These leaked architectural patterns suggest direct upgrades to your existing skill library:

- **Skill Enhancements**: 
  - [[obsidian]]: Implement a "Dream Gate" script. Only run the `/fact-checker` and `/session-summary` consolidation once certain session/time thresholds are met, reducing the "taking too long" friction during rapid URL collection.
  - [[auto-research]]: Adopt the **15-second blocking budget** from **Chyros**. If an autonomous search task is taking too long, the skill should automatically background itself and notify you via a system notification.
  - [[prompter]]: Integrate the "Harness First" philosophy. Every prompt should be wrapped in your custom context-assembly logic (from the leaked `context.ts` patterns) rather than relying on the LLM's raw memory.
- **Workflow Optimization**:
  - **Derivative Strategy**: If you want to use a specific leaked pattern in your own tools, rewrite it in Python or Go first to ensure your internal tools are "legally distinct" from the leaked TypeScript source, following the "Free Code" movement's lead.
- **Project Applications**: 
  - In the **OOBC Scholarship Portal**, use the **Undercover Mode** patterns to ensure that your internal model-routing and budget-tracking logic never leaks into public git commits for the portal's front-end.
  - Implement a "Proactive Auditor" in **MoroMarket** that uses a "tick prompt" to periodically scan for transaction anomalies every 15 seconds without user intervention.

---

## Transcript

[00:00] Well, Enthropic is having a terrible week. Just a few days back, I posted this video where I talked about how a new model has been leaked and now it turns out that Claude codes full code has been leaked. There's a lot to break through in this video. 

[00:23] Claude code source code has been leaked via a map file in their npm registry and he gave this link to code and this link is actually even valid right now. You see it's using R2 which is Cloudflare R2. It's not even using like a proper domain. 

[01:13] Claude Code's entire source code got leaked via a source map in npm. Let's talk about it. So see in order to understand like what's going on we have to dive a little bit deeper into source maps and how exactly did that happen right? 

[01:42] These files are a bridge between the minified bundled production code and the original source. they exist so that when something crashes in production the stack trace can point to the actual line of code in original file. 

[02:55] Look at this JavaScript code. It's all offiscated. Right? Obviously, this is not how Excaliraw staff itself works on it. Right? So, when they are creating like a new function or a new feature functionality, they are not working with this file. They are working with real source code. 

[03:34] If you have something like this you need to be able to see that what went wrong and where. source maps are super important because source map is basically a way for reversing the source code that you're seeing into actual real code. 

[04:56] Now what claude code or their entropics team actually did is that by mistake they uploaded the cli.js.mmap file which is a staggering 60 mgabyte file. The funniest part is that there is an entire system called undercover mode specifically designed to prevent Enthropic's internal information from leaking. They built a whole subsystem to stop their AI from accidentally revealing internal code names in git commits and then shipped the entire source in a dom file likely by Claude. 

[08:03] From inside, it's a 785 KB main.tsx entry point, a custom React terminal, renderer, 40 plus tools, multi- aent orchestration system, and a background memory consolidation engine called Dream, and much more. 

[08:19] As I've told you earlier in some of my past videos, in order to build a successful AI product, you basically need a few things. First is an intelligent model. And second is the harness on top of it. This is basically in a way like more important than even the model. 

[10:56] cloud code identifies a task. It spins up a remote compute. Your terminal shows a polling states, checks every 3 seconds. Meanwhile, a browser based UI lets you watch the planning happen as it's approved or rejected. When approved, there's a special sentinel value of whatever and then that teleports the result back to your local terminal. 

[13:30] then there is the dream system where claude literally dreams claim a background memory consolidation engine that runs as a for sub agent the naming is very intentional it's claude dreaming so dream is basically you know if if it wants to like summarize the memories because it's becoming too much they're saying that it just dreams. 

[14:09] So it's a three gate system. Time gate which is 24 hours since last stream. Session gate at least five sessions since last stream. And log gate acquires a consolidation log prevents concurrent dreams. 

[14:45] Undercover mode is supposed to prevent these leaks from happening. Enthropic employees identify by user type as ant. Undercover mode prevents the AI from accidentally revealing internal information in comets and PRs. 

[15:54] the system prompt architecture so this is basically I would say a nice code that you can look into if you are building your own harness like if you're trying to understand what a frontier lab is doing. 

[17:14] people are rewriting project claw code claude code into claw code and this guy did it in Python first. Now he has started the porting to rust and he's creating basically using AI itself he's creating and using the leaked source code he's creating rust the same AI agent but in rust and the problem is that enthropic cannot take down that source code because it's a derivative work. 
