# Claude Code MASSIVE Update! Claude Code OS, Computer Use, /Schedule, & More!

**Channel**: WorldofAI
**Duration**: 10:37
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=hWDXS35B15A
**Transcribed**: 2026-03-24 12:19

---

## Organized Notes

**Computer Use in Claude Cowork and Claude Code**

- **Computer use** is now available inside Claude Cowork and Claude Code — Claude can **point, click, and navigate** your system like a real user
- Claude can **open files, browse the web, and interact with developer tools** automatically with no setup required
- Claude always tries **the most precise tool first** — if integrations like Slack or Google Calendar are available, it uses them directly
- If integrations aren't available, Claude **falls back to mouse, keyboard, and screen control** — scrolling, clicking, opening tabs, and exploring your system
- Claude always **asks for permission** before controlling your computer or accessing new apps
- **Safety safeguards** built in — the system actively monitors for **suspicious behaviors** and scans for **prompt injection attacks**
- Currently available in **research preview** for Claude Pro and Mac users only

**Dispatch: Remote Task Assignment**

- **Dispatch** lets you assign tasks to Claude from anywhere — desktop app or phone
- Acts like a **remote control** — assign a task and Claude executes it when it has access
- **Daniel Sand** demonstrated controlling his computer from his phone using Dispatch — asked Claude to open Twitter and like a post, completed in seconds
- When combined with **skills.md files**, you can give Claude **structured, repeatable capabilities** across your entire system
- Potential use cases: **pulling analytics metrics** into a weekly report template, **organizing files** while away, **building spreadsheets**, **deep research** with report preparation

**The /schedule Command**

- New **/schedule command** creates **recurring cloud-based jobs** directly from the terminal
- Tasks run **even after you close your laptop** — turns Claude into a **persistent background worker**
- Anthropic teams already using it internally: **auto-resolving CI failures**, pushing documentation updates, handling **repetitive dev tasks** without manual intervention
- Highlighted use case: a scheduled Claude job **maintains a twin Go library** synced with an active Python library — every time the Python side changes, Claude keeps Go in sync automatically
- Represents a shift toward **always-on AI automation** beyond one-off interactions

**Loop Duration Extended to 7 Days**

- **/loop** command now supports runs of **up to 7 days**, extended from the previous 3-day limit
- Enables **longer-running workflows** without interruption — significant for complex and ongoing automations
- The /loop command instructs Claude to **run a task continuously or repeatedly** until a goal is reached or a condition is met based on a set interval

**Effort Levels in Skills and Slash Commands**

- You can now **set effort levels directly inside skills and slash commands** — controls how long Claude thinks before answering
- **Low effort** for quick tasks, **high effort** for complex work like coding, debugging, or planning
- **Overrides session defaults** — fine-tune intelligence and depth on a **per-task basis** without changing global settings

**DOM Element Selection in Claude Code Desktop**

- Claude Code Desktop now lets you **select DOM elements directly** by clicking them instead of describing them in words
- Once selected, Claude gets the **HTML tag, classes, key styles, surrounding DOM context**, and a **cropped screenshot** of the element
- For **React apps**, Claude can also access the **source file, component name, and props**
- Makes **UI edits, debugging, and iteration** significantly faster — no more translating what you see into words

**Performance Upgrade: SSR to Static Architecture**

- Claude AI desktop apps moved from **SSR to static architecture** using **Vite and TanStack Router** served from the edge
- **Time to first byte** down **65%**, components render **50% faster**, overall navigation feels much snappier

**Improved /init Command**

- New version of **/init** actually **interviews you** to set up Claude Code inside your repo — including skills, hooks, and configs
- Enabled by launching Claude with the **environment flag** (`CLAUDE_CODE_NEW_INITIALIZATION=1`)
- Major improvement for **onboarding** new projects or integrating Claude into existing workflows

**Projects and Cowork Memory**

- Introduction of **Projects in Cowork** with **built-in memory across tasks**
- Features a **shared folder** and **connection setup** for a group of different tasks

*Quotable Quotes:*

> "This is a moment where AI starts moving beyond just tools and onto something that can actually operate within environments that you set." [02:13]

> "Instead of just running tasks locally while your computer is on, you can now have it set up things that are running even after you close your laptop. Think of it like turning Claude into a persistent worker that is always running in the background." [05:00]

> "You're giving it repeatable capabilities across your entire system, which is just powerful if you think about it." [02:08]

---

## What This Means for Your Work

**Computer use turns Claude into a full desktop operator for your 9+ projects.** You're constantly switching between VS Code, Chrome (e-Bangsamoro staging), Obsidian, NotebookLM, and terminal — all on Mac. With computer use in Cowork, Claude can navigate between these apps for you. When you're deep in /bill-drafter work on the ECCD Bill, Claude could pull up the relevant BAA reference in Obsidian, check the BTA Parliament Committee PDF, and cross-reference RA 11054 provisions — all without you manually switching windows. The permission-first design means you stay in control, which matters when handling sensitive BARMM governance documents.

**Dispatch from your phone changes your daily workflow.** As OOBC consultant and MoroTech founder, you're often in meetings, at the BTA Parliament, or in transit across Cotabato City. Dispatch lets you trigger tasks from your phone while away: "Add this BAA amendment note to the Parliamentarian research vault," "Pull the latest OBCMS monitoring dashboard metrics into a summary," or "Run /context on e-Bangsamoro and save to vault." Your Mac just needs to be running Claude Desktop at home or office.

**The /schedule command is the automation layer you've been building toward manually.** You already have /loop for sustained tasks, but /schedule adds persistence — tasks run even when your laptop is closed. Concrete applications: schedule a daily scan of BTA legislative agenda items and surface new BAAs to your vault inbox, weekly syncing of your skills-bucket repo with your vault Claude-Skills archive, or automated /session-summary generation at end of each work day.

**The 7-day /loop extension is significant for your /auto-research workflows.** Your Karpathy-inspired optimization loops on skills and transcription quality currently run within a 3-day window. With 7 days, you can set up longer optimization cycles — run /skill-optimizer on a batch of 10 skills, let it iterate through eval cycles over a full week, and come back to measurably improved output. Similarly, /auto-research on your bill-drafting pipeline could run sustained quality loops on section drafting accuracy.

**Effort levels per skill solve a real problem in your 129-skill setup.** Not every skill needs deep reasoning. /vault-update and /file-organizer are quick routing tasks — low effort. /bill-drafter and /policy-recommendation need deep analysis of BOL provisions and BDP chapters — high effort. /fact-checker verifying officials against your reference list is medium. Setting effort directly in each skill's definition means Claude allocates thinking time appropriately without you manually adjusting each session.

**DOM element selection accelerates your frontend-first development.** You build React 19 interfaces for e-Bangsamoro, MoroMarket, Tarbiyyah-MS, and BangsamoroHR. Instead of describing "the citizen registration form's province dropdown in the OBCMS module," you click it, and Claude gets the exact component, props, and styles. This directly speeds up your /frontend and /devwork skill workflows — especially when iterating on government portal UIs where precise element targeting matters.

### How This Can Improve Your Claude Skills and Workflows

**Create a /schedule skill to manage your recurring automation jobs.** You don't currently have a /schedule skill (confirmed: not in your 129-skill archive). Build one that wraps the new /schedule command with your specific patterns: daily vault inbox processing, weekly skills-bucket sync, legislative monitoring scans. The skill should include templates for common schedules (daily, weekly, on-commit) and integrate with your /gitops skill for CI/CD automation. Store schedule definitions in your vault at `knowledge-areas/ai-engineering/` for reference.

**Enhance /loop with the 7-day window for sustained /auto-research campaigns.** Your existing /loop skill should be updated to document the extended 7-day limit and include patterns for multi-day optimization: skill quality loops (/skill-optimizer running across a skill batch), transcript pipeline quality (testing /youtube-transcriber output against gold-standard transcripts), and bill-drafting accuracy (/bill-drafter output measured against your 39,000-word manual's standards). Add checkpoint logic so /loop saves intermediate results to your vault, preventing lost work on long runs.

**Wire effort levels into /devwork, /frontend, /backend, and /tdd.** These are your core development skills. /devwork should default to high effort (it orchestrates complex builds). /tdd should use high effort for test design but medium for test execution. /frontend and /backend should use high effort for architecture decisions but low effort for boilerplate scaffolding. Update each skill's frontmatter or configuration to include an `effort:` parameter that gets passed to Claude's effort setting.

**Combine Dispatch with /sp-dispatching-parallel-agents for mobile-triggered parallel builds.** When you're away from your desk and want to kick off work, Dispatch can trigger parallel agents: one running /frontend on a new component, another running /backend on the API endpoint, a third running /tdd on test scaffolding. Your /sp-dispatching-parallel-agents skill already defines the orchestration pattern — extend it with Dispatch-compatible task definitions that work from your phone.

**Use DOM element selection to supercharge /frontend and /build debugging cycles.** When a UI component looks wrong on e-Bangsamoro or MoroMarket, your current workflow is: describe the issue in text, Claude reads the code, proposes a fix. With DOM selection: click the broken element, Claude gets the exact component tree + props + styles + screenshot. Update /frontend and /build skills to include a "visual debugging" mode that expects DOM context as input, dramatically reducing the describe-read-fix cycle.

**The /init interview pattern should inform your /expert-builder skill.** The new /init asks clarifying questions before generating configuration. Apply this pattern to /expert-builder: instead of immediately generating an expert persona, have it interview you about the domain, expected outputs, required reference files, and quality criteria. This produces tighter, more effective expert definitions — especially for Bangsamoro governance experts who need to know which BOL articles, BDP chapters, and BAAs are relevant to their domain.

**Schedule /security scans and /devops health checks as persistent background jobs.** With /schedule, set up weekly security audits on your 9 platforms (OBCMS handles sensitive OBC data, e-Bangsamoro processes citizen information). Have /security run dependency checks and vulnerability scans on a cron. Similarly, /devops can run Railway deployment health checks and Prometheus/Grafana metric summaries on a schedule, delivered to your vault inbox every Monday morning.

---

## Transcript

[00:00] Claude Code and their desktop app just keeps getting better and better. And today they dropped a major new feature that honestly replaces a lot of what tools like OpenClaw were trying to do, but in a much more seamless way. With the new Cloud Code desktop experience, you can now delegate full tasks to Claude. You can literally hand off

[00:20] something and get back a polished deliverable. But it even goes further than that because you can now put Claw to work directly on your computer, letting it operate and complete tasks autonomously, controlling your computer to do anything. They also introduce a few new commands that make everything way easier to use. So, let's dive

[00:39] straight into it. To start things off, one of the biggest updates to Claude is that you can actually use your computer to complete tasks. inside Claude co-work and Claude code. Claude can point,

[00:51] click, and navigate your system just like a real user. It has the capability of opening files, browsing the web, and even interacting with developer tools all automatically with no setup required. And it gets even more powerful with their new dispatch feature. Cuz

[01:07] dispatch lets you assign tasks to Claude from anywhere, whether that's from your desktop app or from your phone. You can literally be away from your computer, send a task, and Claude can handle it for you in the background. Now, if you're not familiar with dispatch, it's basically something that acts like a remote control for Claude. You assign it

[01:26] a task, and Claude executes it for you whenever it has access. Just take a look at it live in action. This is where Daniel Sand, which I highly recommend that you follow on Twitter. He is

[01:36] constantly posting new updates about Cloud Code first amongst all of these different developers, including myself. And this is where he had literally just controlled his computer from his phone using the dispatch update. And this is where he asked it to open Twitter and like a claude post. It was able to do it

[01:54] directly within a couple seconds. And this is where it starts to get really interesting because once you start combining this with things like your skills MD file, you can give clawed structured instructions on how to use different apps on your computer. So now you're not just triggering oneoff actions. You're giving it repeatable

[02:13] capabilities across your entire system, which is just powerful if you think about it. This is a moment where AI starts moving beyond just tools and onto something that can actually operate within environments that you set. If you want the best AI tools, workflows, and drops before everyone else, join my free newsletter with the link in the description below, which is completely free. With this new capability, Claude

[02:36] will always try to use your most precise tool first. So, it has the access to integrations like Slack, Google Calendar, and it will use them directly. But if those tools aren't available, Claude doesn't just stop there cuz it can actually take control of your computer. It can

[02:53] browse using your mouse, keyboard, and screen. And this is to complete a task itself. It can scroll, click, open tabs, and explore your system just like a human would. And importantly, it always

[03:06] asks for your permission before doing any of this. And of course, with something this powerful that controls your computer, there's a lot of safety concerns. And Enthropic clearly thought about that and they actually built a safeguard to minimize risk like prompt injection attacks. The system is

[03:22] actively monitoring what Claude is doing, and it has the capability of scanning for suspicious behaviors autonomously. On top of that, you're always fully in control, so you can stop Claude at any time. It always requests permission before accessing new apps or taking sensitive action. Now, this is a

[03:40] feature that is currently available in research preview for Cloud Pro and Mac users, and apparently the computer use is only available right now for, I believe, Mac OS users. Overall, I believe this is a huge step forward in truly autonomous AI agents that can control your computer do any sort of task. But think about the possibilities of what you can do with this. With the

[04:03] dispatch feature now also allowing you to control your computer. You can essentially have it schedule various sorts of tasks for you, like pulling my metrics from an analytics dashboard and dropping them into a weekly report template every Friday. having it organize files while you're away from your computer, building out spreadsheets for you. You also have the ability to

[04:23] have it work upon doing deep research and then preparing a report for you, analyzing notes for you, and the list just keeps on going on and on. Now, if you're on Mac and you want to access the computer use, you're going to need to actually download the latest update. Just open up co-work and then relaunch it, and then you should be able to now access this new feature. Next is a

[04:44] pretty cool feature that really stood out to me, and that is the new schedule command. This is honestly a gamecher if you're into automation, cuz with the schedule command, you can create reoccurring cloud-based jobs for cloud directly from your terminal. So instead of just running tasks locally while your computer is on, you can now have it set up things that are running even after you close your laptop. Think of it like

[05:08] turning Claude into a persistent worker that is always running in the background. Internally, this is already being used for some pretty powerful workflows. For example, the teams at Enthropic are using it automatically to resolve CI failures, pushing documentation, updates, and handling repetitive dev tasks without any manual intervention. So, instead of constantly

[05:29] checking your pipeline or fixing small issues, cloud is just going to take care of that. And it is something that's going to run on a schedule. And one of the coolest use cases I've seen is that there's actually a schedule Claude job that is going to maintain a twin library in Go for an active Python library. So

[05:47] every time changes are made on this Python side, Claude keeps the Go version in sync automatically. That is something that you can practically do with this new assistant feature. Another quick but important update is that loops can now run for up to 7 days instead of just three. So you can keep longer running

[06:06] workflows going without interruption, which is huge for complex and ongoing automations. And if you're not familiar with what loops are, you can use the /loop command. And essentially that will instruct the cloud to run a task continuously or repeatedly until a goal is reached or a condition is met based off the interval that you set. Another

[06:26] really useful and subtle update is that you can now set the effort levels directly inside skills and slash commands. This basically controls how long Claude thinks before giving you an answer. So if you want something quick, you can obviously set the effort low.

[06:41] But if you're working on something more complex like coding, debugging or planning, you can increase this effort by just using the slash command. And this way it's going to get much more of a thorough response. And the best part is this overrides your session default.

[06:57] So you won't actually constantly need to change this global setting cuz you can fine-tune intelligence and depth on per task basis. This is a feature that's more for the cloud code desktop users cuz this is something that's going to save a lot of you guys a lot of time cuz especially if you're working on front-end work. Cloud code desktop is something that will now let you select DOM elements directly. So instead of

[07:19] just trying to describe that button on the top right with a blue border, you can just simply click it. Now once you select the element, Claude gets everything it needs. The HTML tag, the classes, key styles, surrounding DOM context, and even a crop screenshot of that exact element. And if you're

[07:37] working with React apps, it gets even deeper cuz Claude can access the actual source file, the component name, and even the props before it passes it in. This makes UI edits, debugging, and iteration way faster because you're no longer translating what you see in words because you're actually just pointing it out. Now, this is one of those small UX improvements that actually makes a massive difference in real workflows.

[08:01] This is a quick performance update that is quite subtle and it relates to cloud AI and their desktop apps cuz it just got significantly faster because they moved from SSR to a static architecture using wheat and tan stack router served directly from the edge. This means time to first bite is down 65%. Comps will show up 50% faster and overall navigation feels much snappier. Small

[08:26] changes on the surface but huge upgrades to the overall experience. Another cool update they're testing out right now is the improved initialization command. And this is a new version that actually interviews you to help set up claude code inside your repo. This is including

[08:41] things like skills hooks and configs. To enable it, you just need to simply launch Claude with the environment flag with claude code new initialization set to one. And this is where you can then run the initialization command inside your repo. It will then guide you

[08:57] through the setup. This is a huge step forward for making onboarding way smoother, especially for new projects or integrating Claude into existing workflows. Lastly is the introduction of projects and co-work. This is with

[09:10] built-in memory across tasks, which is super useful as it is going to have a shared folder and connection setup for a group of different tasks. If you like this video and would love to support the channel, you can consider donating to my channel through the super thanks option below. Or you can consider joining our private Discord where you can access multiple subscriptions to different AI tools for free on a monthly basis, plus daily AI news and exclusive content, plus a lot more. But that's about it,

[09:40] guys, for today's video on the new Cloud Code updates. There are probably going to be a lot of minuscule updates that I forgot to cover. And if there is something that you think would be worth mentioning, please comment that in the description below. So then I can

[09:53] potentially highlight that and then create a condensed list of the new updates that were forgotten from this video so that other people can get a better idea of what happened in Claude Code this past week. But that is basically it guys. I hope you enjoyed today's video and got some sort of value. I'll leave all these links in the

[10:10] description below so that you can easily get started. But with that thought guys, thank you guys so much for watching. Make sure you go ahead and subscribe to our second channel. Join the newsletter.

[10:18] Join our Discord. Follow me on Twitter. And lastly, make sure you go ahead and subscribe to the main channel. Make sure

[10:24] you take a look at our previous videos. Turn on the notification bell, like this video, and take a look at our previous videos so that you can stay upto date with the latest AI news. But with that thought, guys, have an amazing day.

[10:34] Spread positivity, and I'll see you guys fairly shortly. He suffers.
