# Claude Code Source Code Just Leaked… 8 Things You Must Do

**Channel**: Nate Herk | AI Automation
**Duration**: 12:51
**Language**: English (manual) [yt-dlp subtitles]
**URL**: https://youtube.com/watch?v=tXtCK66fPj8
**Transcribed**: 2026-04-01 15:24

---

## Organized Notes

**The Claude Code Leak: Context and Scale**

- **The Incident**: Anthropic accidentally published an **npm package** map file that pointed to readable **TypeScript** source code on their servers. The codebase contains over **2,000 files** and **500,000 lines** of production-grade code. [00:09]
- **Legal Advisory**: Anthropic holds the copyright and of-ten issues **DMCA takedowns**. The community has reacted by rewriting the logic in Python to create legally distinct versions, but users are advised to be cautious when downloading the original source. [01:10]
- **Developer Culture**: The codebase includes a list of **187 "spinner verbs"** (e.g., boondoggling, moonwalking) for the "Claude is thinking" state, reflecting a high-energy, creative development team at Anthropic. [01:24]

*Quotable Quotes:*

> "Claude Code is not a chatbot... it's a full agent runtime. It's a proper application built with Bun, TypeScript, and React." [01:44]

> "Think of Claude.md like an employee's onboarding document. It's not documentation; it's operating context." [05:04]

**Claude Code as an Agent Runtime**

- **Beyond Chat**: Claude Code is a sophisticated **execution environment**, not just a terminal chatbot. It features a tool system, command system, memory engine, and specialized modules for task management and multi-agent coordination. [01:56]
- **The Execution Pipeline**: User inputs hit a CLI parser, move to a **Query Engine**, interact with the LLM API, and enter a tool execution loop before rendering results. [02:13]

**Mastering the Command Service**

- **The 85 Hidden Commands**: Most users only know a handful of slash commands, but the codebase reveals approximately **85 available commands**. [02:49]
- **Top Leverage Commands**:
  - `/plan` / `/ultplan`: Forces the agent into planning mode to map out changes before touching files, saving both tokens and errors.
  - `/compact`: Compresses conversation history to reduce costs.
  - `/re` / `/security review`: Structured code review workflows built as first-class citizens.
  - `/cost`: Real-time session billing visibility.
  - `/summary` / `/resume`: Facilitates picking up complex tasks across different sessions. [03:15], [04:28]

**Memory Systems and Operating Manuals**

- **The Claude.md Protocol**: This file acts as the agent's **operating manual**. It should be kept short, opinionated, and operational (e.g., "Always use TypeScript strict mode," "Tests go next to source files"). [05:15]
- **Persistence Layers**: The system manages memory across three layers: **user-level memory**, **extracted session memory**, and **team memory synchronization**. [05:41]

**Automation and System Architecture**

- **Wildcard Permissions**: To avoid "babysitting" every agent action, users can configure **wildcard permissions** in `settings.json` (e.g., allow all file edits in `/src` or all `git` commands). [06:32]
- **Multi-Agent Coordination**: The architecture includes a **Coordinator subsystem** designed for decomposition — splitting one complex task into parallel background tasks (e.g., one agent exploring, one implementing, one testing). [07:17]
- **MCP Native**: Claude Code is both an **MCP client and an MCP server**, meaning it is designed as an integration layer for databases, APIs, and documentation systems. [08:33]
- **Internal Feature Flags**: The codebase reveals hidden features like **voice mode**, **daemon mode**, and **coordinator mode**, suggesting a deep roadmap being tested internally (user type: `ant` for Anthropic). [09:36]

---

## What This Means for Your Work

The "Agent Runtime" perspective presented here perfectly aligns with your role as a **solo developer building government-scale systems** (e.g., **e-Bangsamoro**, **MoroMarket**). By treating Claude Code as an infrastructure layer rather than a simple tool, you can further automate the maintenance of your 18 active repositories. The **Wildcard Permissions** strategy is a massive productivity unlock for your **OOBCMS** and **BangsamoroHR** projects — you can white-list your `/src` and `/tests` directories to allow agents to iterate autonomously while you handle strategic planning for **MP Sittie Fahanie S. Uy-Oyod** or **Prof. Noron Andan**.

The emphasis on **Decomposition** (breaking one giant request into sequential/parallel steps) reinforces why your complex multi-agent setups (like in the **Parliamentarian** app) are more successful than single-prompt attempts. You are already using the "American football through a basketball hoop" analogy's inverse — you've built the hoop (the skills-bucket) to match the ball (the Claude Code harness). This video confirms that your **obsidian vault-as-memory** strategy is actually "best practice" for the top 1% of users.

### How This Can Improve Your Gemini Skills and Workflows

This video suggests specific enhancements to your 135+ skills and your overall development discipline:

- **Skill Upgrades**:
  - [[gitops]]: Add a "Wildcard Setup" helper that configures `settings.json` for new projects, automatically white-listing safe directories to reduce permission friction.
  - [[skill-optimizer]]: Reference the **85 slash commands** to see if any built-in functions (like the security review) can replace custom logic in your existing skills.
  - [[prompter]]: Integrate a "Decomposition Check" that pauses giant requests and asks to break them into search-plan-execute-verify phases (mirroring the `/plan` command logic).
- **Workflow Changes**:
  - **Context Management as Discipline**: Treat every file in context as a financial cost. Use [[obsidian]] to strictly control what is "loaded" into the session, and use `/compact` proactively to prune history.
  - **GEMINI.md as Onboarding**: Rewrite your `GEMINI.md` files to be "opinionated and operational" onboarding docs for your agents, not just descriptions.
- **Project Applications**: 
  - For **e-Bangsamoro**, use the **Decomposition** pattern to build a "Full Feature Agent" that runs four sub-agents in parallel across your Parliamentary, Ministerial, Budget, and Citizen portals simultaneously using shared caches.
  - Use the **MCP Native** architecture to connect your **MoroMarket** database directly to a Claude Code session for real-time data auditing.

---

## Transcript

[00:00] So, Cloud Code's source code just got leaked to the internet. 2,000 files, over half a million lines of production code, the actual code base behind Cloud Code. Here's what happened. Enthropic published an MPM package that included a source map file pointing to readable TypeScript source on their servers. 

[00:09] A security researcher found it, followed the breadcrumbs, and the full source was mirrored publicly on GitHub within hours. It went super viral. So, I went through everything that people found and I went through the codebase and I pulled out every practical insight that will actually change how you use cloud code. 

[00:22] I'm talking hidden commands that most people have no idea exist, how context and tokens actually work under the hood, and what the architecture reveals about features most users never touch. I broke it down into eight key insights that we're going to talk about today, and each one builds on the previous one. 

[00:42] The first few will change how you think about the tool, but the last one ties everything together into a system, and that's where the real leverage is. So, by the end of this video, you'll know how to use Cloud Code like a top 1% user. So, let's get into it. 

[00:53] Okay, I do have to start off with a quick disclaimer. I'm not going to show you guys any of the actual source code in this video, and I'd encourage you to be careful if you go downloading it yourself. Even though this leaked through a public MPM package, Enthropic still owns the copyright, they've shown that they're willing to send DMCA takedown notices. 

[01:10] So, everything I'm covering is just based on takeaways of how you can use the tool better. All right, so just to start off real quick and to give you a taste of what's in this codebase, you know those little messages that you see while Claude Code is thinking? That's a file with 187 spinner verbs in it. 

[01:24] You've got normal ones like computing or generating, but then you've also got funny ones like boondoggling, discombobulating, fibridding, moonwalking, things like that. And someone at Enthropic got paid to write 187 of these. I just think, you know, that's the energy that I want from the people that are building my tools. 

[01:39] But anyways, that's just a quick appetizer. Let's get into the stuff that actually matters here. So, starting off with number one. It's not what you think it is. The first thing this leak reveals is that Claude code is not what most people think it is because most people think that it's basically just like Claude but in your terminal like a chatbot with access to your local files. 

[01:56] And that's completely wrong. What the source code shows is that Claude Code is a full agent runtime. It's a proper application built with bun TypeScript and React. It has a tool system, a command system, a memory system, a permission engine, a task manager, a multi-agent coordinator, and an MCP client and server all wired together under one execution pipeline. 

[02:13] So the flow goes, your input hits a CLI parser. It goes to something called the query engine, calls the LLM API, runs a tool execution loop, and then renders results back in your terminal. So I know that sound like a bunch of gibberish. 

[02:25] So why does this matter to you? Because if you're using Cloud Code like a chatbot, meaning you're just typing questions and hoping for good answers, you're using maybe 10% of what it can actually do. The rest of the value is in the systems that are built around the model. 

[02:36] And that's what the rest of this video is about. So the second piece is the command service that you're ignoring. Here's something that most people don't realize about cloud code that the source code revealed there's 85 slashcomands in cloud code roughly. Most users may know maybe five of them. 

[02:49] You probably type /help and that's about it or maybe slashcontext. But the power users, the ones getting 10 times more value out of cloud code are using commands like shortcuts. Here are the ones that matter most. You've got /init which sets up your project context. It generates a cloudmd file that acts as cloud code's operating manual for your repository. 

[03:07] And we'll talk more about why this file is so important in a second. We also have slash plan or slult plan. These put cloud code into planning mode. Instead of immediately executing, it maps out the full approach first and then it asks you before it starts touching files. 

[03:15] And this is huge when you're working on something complex and you don't want it to just start editing things everywhere. You're also going to save tokens in the long run doing this. You've got /compact. And this is a big one for saving money. When your conversation gets long, context gets expensive. 

[03:34] So /compact compresses your conversation history. So you can keep the important stuff but drop the noise. And if you're burning through tokens, this is one of the fastest fixes. You can also do /compact and then give it a prompt. So if you want to compact a project but keep all of the important information about the website integration, you can specify that when you run your compaction. 

[03:53] Then we have /re and/security review. These are built-in code review workflows. Instead of asking cloud code to look at my code, you just use these commands and it runs a structured review. And the fact that these exist as dedicated commands tells you something that review isn't an afterthought in this product. It is a first class workflow. 

[04:05] Then we have /context. This manages what files cloud code is actually paying attention to. This matters because every file in context costs you tokens. So this command gives you more visibility so you can help, you know, clean up your project. /cost. This one shows you what you've actually spent. 

[04:20] Most people usually have no idea how much a session is costing them until they look at the bill. So run /cost. Then we have slume and slummary. These let you pick up where you left off between sessions without having to reexplain everything. And that's only the tip of the iceberg when it comes to all of these different built-in commands. 

[04:38] The point is better prompts are one lever, but knowing these commands is a completely separate lever that most people aren't even touching. Next one, number three, we have the memory system, and it is way more important than you think. The source code here reveals that Cloud Code has a full memory system, and the center of it is a file called cloud.md. 

[04:54] Now, most people either ignore this file or dump a bunch of random notes into it, and that's a huge mistake because claw.md is not documentation. It's operating context. So, think of it like this, and you guys know I love analogies. If Claude Code is an employee, then claw.md is their onboarding document. 

[05:09] It tells them, "Here's how we do things. Here's what matters. Here's what we never do, and here's how this project is structured." The best users keep the cloudmd file short, opinionated, and operational. Things like, "We use TypeScript strict mode." Always. Tests go in test folders next to the source file. 

[05:21] Never modify the database schema without running migrations. Use PNPM, not npm, that kind of stuff. decision rules, constraints, conventions, not a novel about your project's history. The source also reveals that there are multiple layers to this. 

[05:41] You've got user level memory, extracted memories, and even team memory synchronization. What that tells us is that cloud code has persistent memory mechanisms across project, user, and session contexts. And cloudMD is one of the highest leverage inputs shaping how it behaves in future sessions. 

[05:55] So, if you get nothing else from this video, go update your cloud.MD file today, whether that's on the global level or the project level. And remember, these get injected every single session before every single chat. 

[06:08] All right, number four, we have that permissions are why Claude might feel slow. If you've used Cloud Code, you've hit this. You ask it to do something and it keeps asking, "Allow me to do this. Will you allow me to do this? Can I run this? Can I edit this?" And it's really annoying. 

[06:16] And most people think the fix is better prompting, but it's not. The fix is permissions. The source code shows us a deep permission system with multiple modes. default mode where it asks you about everything, plan mode, and then there are things like bypass permissions or auto modes where it can just execute. 

[06:32] But here's the real gem. You can set wild card permissions. So things like allow all git commands or allow all file edits in my src folder. So instead of cloud code asking you 15 times, can I run git status or can I edit this file? Can I run this test? 

[06:41] You set the rule once and then it just works. So for recurring workflows, stuff that you do every day, this is one of the highest ROI changes that you can make. So in your settings.local.json or in your settings.json, JSON, you can set global or user level or project level permissions for things that you always want to allow or have it always deny or have it always ask to do. 

[07:06] And this lets you go from babysitting every action to actually being able to let it operate like an agent while you step away. So number five is that it is built for multi-agent work. And this one surprised me. The source code reveals a full coordinator subsystem, agent tools, team tools, and a task system designed for background and parallel work. 

[07:17] So what does this mean in plain English? that the architecture is clearly built to support decomposition, splitting work across multiple agents that can run in parallel. So think one agent exploring your codebase, another one implementing changes, and another validating tests. 

[07:30] There are even concepts in the source for background tasks, work that continues while you're focused on something else. Now, how much of this is fully userfacing today versus still rolling out? That's a little bit harder to say from the source alone, but the architecture makes the intent clear, which is that cloud code is designed to handle complex multi-step work by breaking it apart, not by cramming it all into one thread. 

[07:49] The practical takeaway here is about how you structure your requests instead of one massive prompt like refactor this entire module, update the tests, and fix the documentation. Break that up. Let cloud code decompose the work. 

[08:01] Think about it the same way I talk about workflows versus agents in something like NADN or just in general. The best results come from breaking complex work into clear sequential steps or in this case parallel steps rather than hoping that one giant general instruction to one giant general agent gets everything right. 

[08:21] All right, so number six is about MCP plugins and skills being the real extension layer. If you've been following my channel, you know that I've talked a lot about MCP, which is model context protocol. And here's what the source code confirms. 

[08:33] MCP isn't just supported by cloud code, but it's kind of baked into the architecture. Cloud code is both an MCP client and an MCP server. It can connect to external tools through MCP and other systems can connect to it. But it does go beyond MCP. 

[08:43] The source also reveals a skills and plug-in layer. Meaning power users can build repeatable workflows, custom capabilities, and domain specific extensions that compound over time. It's not just about connecting to one tool. 

[08:52] It's about building an ecosystem around cloud code that makes it smarter for your specific work. This is where cloud code stops being just a coding tool and it starts being an integration layer. You can connect it to databases, APIs, internal tools, documentation systems, anything with an MCP server and then you can layer skills and plugins on top for the stuff that you do repeatedly. 

[09:10] Now, the more systems you connect it to, the more useful it becomes. So, the power of course isn't the tool itself. It's what you connect to and the workflows that you start to automate and build with it. 

[09:19] Okay, number seven. There are features that we don't even have access to yet. And this one's super interesting because the codebase includes checks for something called user type. And one of the values is ant which means anthropic. 

[09:27] What this tells us is that certain capabilities are gated behind internal feature flags. The source references things like voice mode. You know, a system called chyros, a damon mode, and a coordinator mode. All behind flags that suggest that they're either internal, experimental, or maybe being rolled out gradually. 

[09:47] Now, I want to be honest here. We can't say for sure how different the internal experience actually is. Some of these could be early prototypes. Some might be close to shipping publicly. The source alone doesn't tell us that. 

[09:53] But what it does confirm is that cloud code is heavily feature flagged, meaning different users may already be getting meaningfully different experiences depending on their environment, their build, or their rollout group. The practical takeaway is pay attention to cloud code updates. 

[10:07] Capabilities that are flagged or limited today are likely on the road map. And when they land, the people who already understand the architecture, like you watching this video, will be ready to use them immediately. I mean, think about how many features and tools cloud code has been shipping lately. 

[10:19] It's because they've all been already built and tested internally. I've heard rumors that computer use has been around for a long, long time, but they just released those functions now that they were ready. 

[10:31] Moving on to number eight, we have how to actually use this to save money and to get better results. Let me tie all of this together with what I think matters most. The habits that separate top 1% users from everyone else. And the single biggest insight from this entire source code is this. 

[10:40] Top users don't just write better prompts. They design a better operating environment for their cla code. Here's what that looks like in practice. First, treat claw.mmd like a force multiplier. Keep it short. Keep it opinionated. Update it regularly. Route to other files. 

[11:00] This single file shapes every interaction that you have with cloud code. Second, learn the command service. You don't need all 85 commands, but / plan/compact/context, review, cost, and resume. These types of commands will change your daily workflow immediately. 

[11:13] Third, configure permissions for your recurring workflows. Stop babysitting every action. Set wildcard rules for the stuff that you do every day. Fourth, think in terms of decomposition, not monolithic prompts. 

[11:22] So break complex work into a search phase, a plan phase, an execute phase, a verify phase. Let Claude code use its architecture the way that it was actually designed to. Otherwise, it might feel like you're trying to shoot an American football through a basketball hoop. That's not what it was designed to do. 

[11:43] Fifth, manage your context like it's money, because it literally is. Use /compact when conversations get long. Use /context to control what's loaded. Use/summary and/resume to carry work across sessions without losing your important details. 

[11:50] Every unnecessary file in context is tokens that you're paying for. And context management isn't just a nice to have, but it is an actual discipline. It's something that you need to build a habit around. 

[12:00] Sixth, connect things to it. Whether that's MCP servers or CLIs or plugins or skills, the more tools that Cloud Code can access, the more valuable it actually becomes. 

[12:11] And seventh, treat it like infrastructure, not an app. The source reveals a massive configuration surface. model routing, sub agent model overrides, shell behavior, privacy controls, even the ability to route through different cloud backends like AWS Bedrock or Google Vertex. 

[12:27] Most people never touch these settings, but if you're using Cloud Code seriously, there's real leverage in tuning the environment to fit your workflow. Anyways, that's what was hiding inside of Cloud Code source code. 

[12:27] And I know that that was a ton of information, and I wanted to move as quick as I could so I didn't bore you guys in this video. So, I broke all of this stuff that we talked about and more into a full resource guide that you can access for completely free. 

[12:42] You get that inside of my free school community and the link for that is down in the description. But anyways, that's going to do it for today. So, if you enjoyed the video or you learned something new, please give it a like. Definitely helps me out a ton. And as always, I appreciate you guys making it to the end of the video. 
