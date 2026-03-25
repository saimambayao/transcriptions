# Claude Code + Obsidian = UNLIMITED Memory! Solves Claude's Memory Problem!

**Channel**: WorldofAI
**Duration**: 13:00
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=srqWFT_TUec
**Transcribed**: 2026-03-23 01:24

---

## Organized Notes

**The Problem**

- Even powerful models like **Opus 4.6** lose focus over long context and forget previous steps
- In large codebases, you end up **re-explaining the same context** every session
- The model drifts from your **original architectural vision** over time

**The Solution: Obsidian as Persistent Memory**

- Obsidian stores everything as **plain markdown files** in a local folder (vault)
- **No proprietary format**, no lock-in, fully private and offline
- Claude Code can directly **read, search, reference, and update** vault files
- The vault becomes a **persistent knowledge base** that survives across sessions

**What to Store in the Vault**

- **Architecture decisions** and design choices
- **Coding rules** and conventions
- **Session summaries** — what was built, what's next
- **Bug notes** and naming conventions
- **PRDs and research** from GitHub
- **Meeting transcripts** for recalling past conversations
- **Personal notes**, ideas, and long-term thinking
- **Daily notes** — what was accomplished each day

**Setting Up the Vault Structure**

- Create folders for different context types: project overviews, daily notes, coding rules, session logs
- Think of it as a **file-based memory system** for AI instead of relying on chat history
- The **graph view** gives visual context of your project memory

**Installing Obsidian Skills for Claude Code**

- Install the **Obsidian marketplace plugin** for Claude Code
- Skills teach Claude Code to:
  - **Read** and parse markdown files
  - **Write and update** notes (e.g., session summaries after coding)
  - **Search** the vault for relevant context
  - **Manage tasks** and daily notes
- Use `/obsidian` to open the CLI within Claude Code

**The Workflow in Practice**

1. **Reference prior context** — point Claude Code at vault notes about your project (stack, architecture, component patterns)
2. **Build with context** — Claude reads SHAD CN patterns, Prisma schema, component architecture from vault
3. **Update the vault** — after building, Claude writes a session note documenting what was done
4. **Next session** — Claude reads the updated vault and picks up where you left off

**Multi-Agent Benefits**

- All sub-agents share the **same vault context** — no deviation between agents
- One agent works on deal pipeline, another on analytics charts — both stay aligned
- **Consistency** in tech stack, components, and coding patterns across agents

**Key Insight**

- The vault **grows over time** — Claude always has up-to-date project memory
- After each session, generate a **daily note** documenting what was built
- Future sessions **revisit previous notes** for correct context
- Result: **less frustration**, more consistent code, smoother workflows

## What This Means for Your Work

**The "persistent memory across sessions" problem this video solves is already handled by your dual-layer system -- but the multi-agent consistency benefit is underexplored.** When you spawn sub-agents for parallel tasks (e.g., one agent working on e-Bangsamoro frontend while another works on Django API), both agents reading from the same vault ensures they use the same component patterns, authentication approach, and API conventions. This is especially critical across your 9 platforms, where consistency in shared patterns (user auth, role-based access, data tables) determines whether platforms can eventually share code.

**The workflow of "reference prior context, build with context, update vault, next session reads updated vault" should be your standard operating procedure for every platform.** After each development session on any platform, Claude should write a session note documenting what was built, what decisions were made, and what is next. Your vault at ~/Vault/projects/ should have a running log for each of your 9 platforms. When you switch from working on Tarbiyyah-MS to e-Negosyo, the first thing Claude reads is the latest session note for that platform -- picking up exactly where you left off.

**The vault structure recommendation (project overviews, daily notes, coding rules, session logs) maps to what you need per platform.** For each of your 9 platforms, create: (1) architecture overview (stack, key patterns, component library), (2) coding rules (Django conventions, React component patterns, PostgreSQL schema standards), (3) session logs (what was built, what broke, what is next), and (4) domain context (for e-Bangsamoro: governance workflows; for Tarbiyyah-MS: madrasah accreditation rules; for MoroMarket: cooperative product catalog structure). This structure ensures that any Claude session on any platform starts with the right context.

**The daily note habit compounds your institutional knowledge.** As someone who splits time between OOBC consulting, legislative work, platform development, and community leadership, a daily note that captures what was accomplished across all roles creates a searchable history of your work. Six months from now, when someone asks "what was the rationale behind the cooperative registration flow in e-Negosyo?", the answer exists in your vault -- not in a forgotten chat thread or an expired Claude session.

### How This Can Improve Your Claude Skills and Workflows

**Your /obsidian skill should add a "multi-agent sync" mode.** The video highlights that all sub-agents sharing the same vault context prevents deviation. Your /obsidian skill currently handles read/write/search operations, but it doesn't have a dedicated protocol for multi-agent scenarios. Add a mode where spawned sub-agents read a standardized context file (e.g., ~/Vault/projects/{platform}/agent-context.md) at session start and write their session summary back to a shared log at session end. This ensures consistency when you dispatch parallel agents via /sp-dispatching-parallel-agents across your 9 platforms.

**The session note workflow should be automated through a /session-summary hook, not manual invocation.** The video shows manually asking Claude to write session notes after coding. Your /session-summary skill already captures this, but making it a post-session hook (triggered automatically when a Claude Code session ends or when you type /close) would eliminate the forgetting problem. The hook writes to ~/Vault/projects/{current-project}/sessions/ with timestamp, decisions made, files changed, and next steps. Your /context skill then reads the latest session note when starting a new session on that project.

**The vault structure per platform (architecture, coding rules, session logs, domain context) should be templated in /vault-update.** You have 9 platforms, each needing these four categories. Your /vault-update skill could include a "scaffold project vault" mode that creates the standard structure for a new platform project. When you spin up IPP or the next government platform, running `/vault-update --scaffold ipp` creates the folder structure with placeholder files, links it in ~/Vault/INDEX.md, and adds the project to your /context loading list.

**Cross-pollination: the multi-agent vault consistency pattern improves your /sp-subagent-driven-development superpower.** When you use /sp-subagent-driven-development to break work across multiple agents, each agent currently discovers the codebase independently. If every agent instead reads the platform's vault context file first (stack, conventions, current sprint status, recent decisions), they start aligned. The vault becomes the "team standup" that every agent attends before doing work -- especially critical when one agent works on e-Bangsamoro's React frontend while another works on the Django API.

---

## Transcript

[00:00] Everyone knows that enthropic models are incredible, especially when it comes to coding. But when you're working with large code bases and long context, you'll sometimes notice a problem. Even when the model is quite powerful itself, like the Opus 4.6, they can still lose

[00:16] focus over time and occasionally forget steps you previously gave them. And when you're building a complex project, that can slow things down. But today I want to showcase a simple solution and it's with a tool called Obsidian which is completely free. Obsidian is a

[00:33] notetaking app that stores everything as a plain markdown file inside your folder on your computer. It is called the vault. This means your notes are not just text files. No proprietary format,

[00:46] no lockups, fully private and completely offline. But what makes it perfect for cloud code is that it keeps your memory or your context persistent. It keeps it structured and it is going to be there for your entire project for the architecture decisions, the design choices, key instructions, session summaries, to-do lists, bug notes, naming conversations, basically anything that matters. Because when it comes to

[01:13] readable markdown files in a folder, Cloud Code can directly read from the vault. It can search it. It can reference specific notes and it can even update them so that it could build on sessions after sessions. This gives

[01:26] Claude the long memory that it normally lacks in a chat interface or simply through the Claude code instance. So no longer you have to reexplain the same context every single time. the model is going to stay aligned with your original vision. Remember important details

[01:42] across weeks or even months and it produces far more consistent and focused code and this will overall dramatically reduce the forgotfulness and the problem that often happens in large code bases. So in short, when you combine Obsidian with cloud code, you have persistent memory and it enables a second brain for your codebase, which overall is going to get you better generations, smoother workflows, and far less frustration when you're working on large longunning projects. Still running object detection with NMS pipelines in 2026? Well, it's

[02:17] time for you to upgrade. And this is where I would like to introduce Ultral Litics YOLO 26, the nextG edge first vision model built end to end from the team behind YOLO version 5, YOLO version 8 as well as YOLO 11. YOLO 26 removes the non-maximum suppression entirely.

[02:37] This means true NMS free end to end inference, no fragile post-processing, lower latency as well as cleaner deployment. It removes distribution focal loss for better large object reliability and hardware compatibility. It also adds stall enhancements for stronger small object detection. It's up

[02:58] to 43% faster with CPU inference real time on existing hardware and built for edge devices in production systems. Plus, the new MUSGD optimizer improves training stability and convergences. This isn't built to win benchmarks. It's

[03:13] built to win in production. It's open source as well under the AGPL 3.0 for research and enterprise licensing is available for commercial deployment through Ultralytics. So if you're

[03:25] looking to try this out, you can do so cuz YOLO 26 is live now. You can try it out on the Ultralytics platform, which is today's video sponsor. Built end to end built for edge and this is the new standard for realtime vision AI. To get

[03:39] started, just make sure you have Claude Code ready and installed on the latest update, as well as having Obsidian installed, which is completely free to install, and I'll leave a link to this in the description below. Now, after installing, you will have this popup, and this is where you're going to need to create your vault. Now, what is a vault? Well, Obsidian basically is going

[03:58] to store all of your notes within your specific vault in a plain markdown file. This means everything is just a normal text file, but it is going to be readable, private, and easy for our tool like cloud code for example to easily access. Because these files live within this particular folder, Claude can see them, read them, search them, and update them during your coding sessions. Over

[04:21] time, the vault is going to become the persistent knowledge base for your project. Storing all of the important things that we're talking about that is prevalent within any codebase like the architecture decisions, the coding rules that you have set, bugs, session summaries, all of this could be updated and present within this one folder so that in future sessions it doesn't lose any sort of memory or any sort of behavior that you had taught it. So give it a name and you can select the location of wherever you want to place this vault. We have created the vault

[04:55] but what do we put inside it? Well this is where you want to simply start off with your file structures. You want to make sure that you are putting in all the relevant context that your cloud code agents can use. Making sure that

[05:08] you provide your GitHub related information whether that's your codebase prds research anything that claude can reference when making decisions. You can even provide meeting notes like transcripts that Claude can actually scan to recall past conversations from different sessions. You can even provide personal notes, ideas, writing, and long-term thinking that you personally have. So, we have created the vault and

[05:33] I have now added in a couple of different files, a few simple files like the project overview, my daily notes. And this is essentially where you want to provide as much context as possible, whether that's coding rules, session logs, whatever it may be. Cuz think of this as a memory file system for your AI instead of trying to remember everything inside the chat within the cloud code instance. Claude can read these notes

[05:59] whenever it needs because it's in an MD format. And this is where it gets powerful because I can simply even reference certain files or certain text stacks within this Obsidian vault before generating the code so that Claude can check how the project is structured, what frameworks I'm actually using, the coding conversations. And what I really like about Obsidian is it gives you a graph view of everything as well, so you get a better context idea of your real project memory. Now, what I would also

[06:28] recommend is installing the agent skills to use Obsidian better because this will teach Claude code how to interact with your vault that you have created better cuz it has these predefined skills that will be able to read your markdown files easier. So, Claude can parse your notes or any relevant information better. It can also write and update notes for you, which is great because after a claud session has completed for you, you can essentially have it write up a session note and upload it directly to your vault like I did over here after coding out I had created this simple note after that session so that whenever I pick up another cloud code session, I can reference this previous note so that it has that persistent memory in future generations. It also has ability to

[07:15] search and also reference content, maintain persistent memory through a normal chat instance as well as working with structured data. To get started, copy this first command, which is to install the marketplace for this plug-in. And you can then add that marketplace and then run the plug-in install command to set up the Obsidian skill. And you can set this up for your

[07:37] instance. And once that is ready, you can get started with your codebase. Now, to showcase our second brain in action and what it's capable of doing, what we're going to be doing is having it first reference a prior project. This is

[07:51] where I had an active project, a CRM dashboard with this text stack that I had built previously. Now, there's a lot of missing features. And what we're going to have it do is have Claude Code first pull the project context. This is

[08:04] where we're going to have it build a deals canband board using the Prisma deal model. and we're going to have it follow the CRM component architecture as well as the SHAD CN UI patterns that were previously active within our context. This is where it will first start off by checking out the component architecture, knowing which SHAD CN components you actually use, also referencing reusable patterns by reading the Shad CN UI patterns for forms, tables, modals, and toast notifications.

[08:36] also following the coding standards. And lastly, it can even update the vault cuz after it has finished generating this, it will update it based off the context, the new context that we had generated so that for future generations, it can reference this session to get better, smarter results even further in the future. So you can see that right now it is referencing the existing CRM project and the Prisma schema and it's able to reference the detailed information that we have present within our vault. So

[09:06] rather than having it just find context every single time, this persistent memory is going to be stable and always there within this vault so that pod can continuously use it whenever it needs it. And just an FYI, when you're working with the new Obsidian skill that we had installed, you can simply just type in /obsidian and then open up the Obsidian CLI so that Claude can actually use the Obsidian CLI to either read, create, edit notes, it can search the vault. So if you want to then ingest prior context, you can use the search vault command so that it is able to give your cloud code instance the particular knowledge that it needs. You can manage

[09:45] tasks, daily notes, as well as plug-in development. When you're working on a larger project with a lot of sub agents, it is going to be able to clearly describe the context across multiple agents and so that there's no deviation from whatever you're working upon. All the agents have the same mindset and that they're able to keep the same context as it's working through the progress. So in this case, one agent

[10:09] could be working with the deal pipeline and the other one could work on the analytics chart and over time it will be able to keep the same context, the same structure, the same text stack as it develops through everything. Thanks to cloud code getting the correct context that it needed for building out a new feature for our CRM dashboard like the shaden UI components, it was able to build out the cananban board feature that we had requested. This is where it was able to keep the consistency of our overall dashboard. It was able to use

[10:40] the correct components and you can see that it coded out this beautiful functionality with animations as added in all of the components that we had looked for. And that is what this new second brain actually solves. It makes your life easier when you're working with these AI agents. What's great is

[10:57] that the vault actually grows too cuz Claude always has up-to-date project memory when you reference the vault and after you have gotten the context you can even generate and update the code and provide daily notes on what was accomplished so that your overall notes is going to be able to stay up to date and for example you can just simply use the obsidian skill the markdown skill so that it is able to create a new note so that it provides a new daily note that our future session can actually revisit. That way, it is able to get the correct context as to what was added or built. And you can see right now that it is searching our previous pattern of the CRM dashboard that I built and it's going to create a new note on whatever it had developed. If you like this video

[11:44] and would love to support the channel, you can consider donating to my channel through the super thanks option below. Or you can consider joining our private Discord where you can access multiple subscriptions to different AI tools for free on a monthly basis, plus daily AI news and exclusive content, plus a lot more. But that's basically it, guys. I

[12:04] hope you enjoyed today's video. This is essentially where you can have Claude always have up-to-date project memory with this second brain. But all you got to do is make sure that you have the correct structure set up with your file structure. and which is why I will leave

[12:19] this article in the description below. It's not extraordinary or anything, but it tells you the basic structure that you need when you're working with this workflow. But that's basically it, guys.

[12:28] I hope you found this video to be helpful. It is something that will make sure your AI sub agents within Claude have the correct context that it needs over time. I'll leave all these links in the description below. But with that

[12:40] thought, guys, thank you guys so much for watching. Make sure you join the newsletter, subscribe to our second channel, join our discord, follow me on Twitter, and lastly, make sure you guys subscribe, turn on notification bell, like this video, and please take a look at our previous videos so that you can stay up to date with the latest AI news. But with that thought, guys, have an amazing day, spread positivity, and I'll see you guys fairly shortly. his offers.
