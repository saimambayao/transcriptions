# How to Use Claude Cowork Better Than 99% of People

**Channel**: Brock Mesarich | AI for Non Techies
**Duration**: 20:43
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=f95-O8C88uw
**Transcribed**: 2026-03-24 10:14

---

## Organized Notes

**What Claude Cowork Is and Why It Matters**

- **Claude Cowork** is Claude Desktop's non-developer mode that brings **Claude Code's power** to nontechnical users — it reads files, connects apps, and runs tasks autonomously
- Three modes in Claude Desktop: **Chat** (standard), **Cowork** (file/workflow-based), and **Code** (developer CLI)
- Core mechanics: give it a **folder** → it reads/edits files → makes a plan → executes the work
- Capabilities: read/edit/create files, analyze spreadsheets and PDFs, connect to apps via **MCP**, break complex tasks into steps, run **scheduled tasks**

**Level 1: Import — Migrating Context from Other LLMs**

- Anthropic built a **memory import page** that generates a prompt you paste into ChatGPT or Gemini
- The other LLM exports a structured code block of everything it knows about you
- Paste that back into Claude → **instant context transfer** in under 60 seconds
- This eliminates the biggest friction point for switching: having to re-teach a new AI about your business

**Level 2: Foundation — Building the Knowledge Base**

- Create a dedicated **folder** for Cowork to operate in — this becomes its workspace
- Key files to create:
  - **CLAUDE.md** — the "brain" of the system; instructions that persist across sessions
  - **goals.md** — north star goals on quarterly, monthly, and weekly basis (without this, responses stay generic)
  - **company.md** — brand info, business name, platforms, tech stack
  - **glossary.md** — business-specific terminology
  - Additional context files as needed (team members, channel info, etc.)
- Analogy: think of CLAUDE.md as a **"kitchen bible"** — the chef (Cowork) updates it after every session so the next session starts with full context
- The system is **self-learning** — it rewrites its own instructions to improve over time
- Think of it like **onboarding a new hire** — write the files once, Cowork reads them every time

**Level 3: Workflows — Plugins and Commands**

- **Plugins** are skill packs organized by department: finance, legal, HR, design, operations, marketing
- Pre-built plugins available through **Customize → Browse Plugins** in the Cowork interface
- Each plugin contains **commands** (slash keywords) that trigger entire workflows
- Example: the **Legal Personal plugin** includes `/brief` (contextual briefing) and `/review-contract` (full contract review with color-coded findings — yellow for flags, green for safe)
- Contract review demo: upload a PDF → type `/review-contract` → get a fully formatted document with **key findings** in ~2 minutes
- **Build your own plugins**: have Cowork perform a task, then say "make this into a plugin" — it generates the markdown workflow file
- Custom plugins are **shareable** — export the folder and teammates can import it into their Cowork

**Level 4: Ecosystem — Connecting Apps via MCP**

- **Connectors** link Cowork to external apps: Gmail, Google Calendar, Google Drive, Notion, Slack, Figma, Canva, and more
- Setup: **Customize → Connectors → Browse** → click an app → authorize → done
- With connectors + workflows combined, a single prompt can trigger actions across **multiple apps** (e.g., read emails, check calendar conflicts, draft reply, save summary to Drive)
- Currently ~**38 preset connectors** available in Cowork
- For apps not in the preset list: use **Zapier MCP** (zapier.com/mcp) to connect to **8,000+ apps**
- Zapier MCP setup: create a new MCP server → select "Claude Cowork" as client → add tools for each app (Airtable, Zendesk, etc.) → add Zapier as a connector in Cowork

**Level 5: Automation — Scheduled Tasks**

- **Scheduled tasks** let Cowork run workflows on a recurring basis without manual triggering — daily, weekly, hourly, or custom cadence
- Setup: click **Schedule → New Task** → name it, write a prompt, select model (recommends **Opus 4.6**), choose folder, set frequency
- **Limitation**: computer must be awake and Claude Desktop must be open — it cannot run if the laptop is closed
- Example: **morning brief at 7 AM** that reads CLAUDE.md, goals.md, and tasks.md, checks email and calendar, then outputs a daily briefing
- Advanced example: **competitor research dashboard** — scrapes YouTube competitors daily at 8 AM, generates an **HTML dashboard** with filming priorities, trending topics, competitor videos, and content gaps, then sends a **Slack notification**
- The system **self-improves** — after each scheduled run, Cowork rewrites its own instructions to customize future interactions
- You can convert any ad-hoc task into a scheduled task: do something in Cowork, then say "turn this into a scheduled task"

**The Five Levels Summary**

1. **Import** — bring memory from other LLMs
2. **Foundation** — build the knowledge base (CLAUDE.md, goals, company context)
3. **Workflows** — install or create plugins with slash commands
4. **Ecosystem** — connect apps via connectors and MCP
5. **Automation** — schedule recurring tasks to run without you

---

## What This Means for Your Work

This video is aimed at nontechnical founders, and you're well beyond its target audience — you already use Claude Code with 129 skills, a dual-layer memory system (Claude Code + Obsidian vault), and parallel agents across government-scale platforms. But Cowork's **scheduled tasks** and **plugin sharing** features have direct implications for your work.

**Scheduled tasks could automate your BARMM monitoring workflows.** You currently rely on manual session starts to trigger legislative research, fact-checking, and policy analysis. A scheduled Cowork task running daily at 8 AM could automatically scan for new BAAs, resolutions, or BTA agenda items and surface a briefing — similar to Brock's competitor dashboard but for parliamentary activity. This is particularly relevant for your OOBC policy work where you need to track legislation affecting Other Bangsamoro Communities across multiple government bodies.

**The plugin system maps directly to your skills-bucket architecture.** Brock's "make this into a plugin" approach is essentially what you've already built with your 50+ portable skills in ~/apps/skills-bucket/. The difference is Cowork plugins are shareable with non-developer teammates through a simple folder export. For MoroTech and the Bangsamoro Scholars Association, this means your legislative analysis workflows, bill-drafting templates, and training design patterns could be packaged as Cowork plugins for team members who don't use Claude Code CLI.

**The connector ecosystem solves your multi-app orchestration gap.** Your e-Bangsamoro platform (React 19 + Django 6.0) and other projects currently require you to manually bridge between tools. Connecting Notion (where you likely track project tasks), Gmail, and Google Drive through Cowork connectors could streamline the administrative overhead that comes with managing 9+ active software projects as a solo dev. The Zapier MCP extending to 8,000+ apps is worth evaluating for OBCMS and MoroMarket integrations.

**Concrete next steps:**
- Test Cowork's scheduled tasks for a daily BARMM legislative monitoring brief (pulling from your local reference files: BOL, BDP 2023-2028, BAAs index)
- Evaluate packaging your most-used skills (/bill-drafter, /legislative-briefer, /training-assistant) as Cowork plugins for potential OOBC team members
- Set up a Notion + Gmail connector for consolidated project status tracking across your 9 active platforms
- The "self-improving" CLAUDE.md rewriting feature is worth monitoring — it could complement your existing vault-update workflow, though you'll want to control what gets auto-modified vs. what stays locked

### How This Can Improve Your Claude Skills and Workflows

**Skill packaging for non-dev distribution.** Your 124-skill library (~/Vault/Claude-Skills/) is built for Claude Code CLI. Cowork's plugin system is the missing distribution layer for teammates who won't touch a terminal. The highest-impact candidates for Cowork plugin conversion:
- **/bill-drafter** and **/resolution-drafter** — OOBC or parliamentary staff could draft legislation through Cowork's GUI without needing Claude Code
- **/training-assistant** — MoroTech trainers could generate facilitator guides, participant handouts, and evaluation forms by invoking a plugin command
- **/legislative-briefer** — MPs' staff could produce CSW-format briefers without your direct involvement
- **/policy-recommendation** — OOBC team members could draft policy documents with the structured framework your skill enforces

**Scheduled tasks as a /session-summary and /vault-update upgrade.** Your /session-summary skill captures session work into Obsidian daily notes, but requires manual invocation. A Cowork scheduled task running at end-of-day could automatically summarize the day's Claude Code sessions and update ~/Vault/daily/. Similarly, /vault-update (which reviews vault health and recommends CLAUDE.md improvements) could run weekly as a scheduled task rather than being invoked ad-hoc.

**The self-improving CLAUDE.md pattern conflicts with your architecture.** Cowork rewrites its own instructions after each run. You have a deliberate separation: /vault-update produces a recommendation document that you review manually, and CLAUDE.md changes go through /claude-md-improver with explicit approval. The Cowork auto-rewrite pattern should NOT be adopted for Claude Code — it would bypass your review layer. But it could work for a Cowork-specific folder used by non-dev staff who don't need that control.

**Connector + skill combos for Parliamentarian.** Your /bangsamoro skill loads domain context, and /fact-checker verifies outputs. If the Parliamentarian platform (Python + Claude agents) were exposed via Cowork with Gmail and Google Drive connectors, it could: (1) receive legislative queries via email, (2) invoke /legal-assistant and /bill-drafter skills, (3) save the output to Google Drive, (4) draft a reply — all without you in the loop. This turns Parliamentarian from a tool you operate into a service others can access.

**MCP connector implications for e-Bangsamoro.** The Zapier MCP (8,000+ apps) opens integration paths for OBCMS (OBC Management System) — connecting to government reporting systems, BARMM internal tools, or regional LGU databases. For MoroMarket (e-Negosyo), Zapier MCP could connect to payment processors, logistics APIs, or cooperative management systems that don't have direct Claude connectors.

---

## Transcript

[00:00] Cloud Co-work is hands down the most powerful AI tool you can use right now as a nontechnical founder. It can read your files, connect your apps, and run tasks while you sleep. But most people open it up, type one prompt, and wonder why it feels like every other chatbot.

[00:13] That's because there are five levels to co-work that you need to master, and most people are stuck on level one. Each level unlocks something completely different. And by the end of this video, you'll know all five levels, and you can begin using them right now. All right,

[00:25] so first of all, we need to talk about what exactly Claude Co-work is and why you should even care to watch to the end of this video. Claude Co-work is the AI that works alongside you, not just answered questions like chatbt or even the normal Claude app that you're used to using. Claude Code is something that was built for developers. It's an

[00:41] extremely powerful tool. However, it's really difficult to use if you're not a developer. So, Claude Co-work brings the same power to everyone else. Let me

[00:49] quickly break down how exactly Claude Code works. Step one, we're going to give it access to a folder. Step two, it's able to read and make changes to your files. Step three, it makes a plan.

[01:01] And step four, it actually goes off and does this work for us. You're probably asking like, Brock, what can Claude Co-work actually do? It could read, edit, and create files on your computer, analyze, and create spreadsheets, PDFs, and documents. It could connect to all

[01:14] the different applications you use like Gmail, Google Drive, Slack, and tons more. It can break complex tasks into steps and complete them a toz. And it can even run tasks on a schedule when you're not there. So whichever apps

[01:27] you're using, there's a chance that Claude Co-work can actually connect to them, powered by MCP. And in this video, I'm going to show you exactly how to set up all this. So don't worry about if it's difficult to do. Then we have brand

[01:37] new plugins for every single job that was just released last week. So whether this is finance, legal, HR, design, operations, these are pre-built templates that we can basically plug in and import directly into our Cloud Co-work experience. And these are entire workflows, not just prompts. And again,

[01:55] I'm going to show you exactly how to set this up in this video. On top of that, we could also build our own plugins. So we essentially just write down a markdown file, define our workflow, and we could run this with one specific command. And if you don't know what a

[02:06] command is, it's basically a specific keyword that then will trigger an entire workflow for you. These are custom skills that match exactly how your business works. And one of the most underrated features was just released last week. And these are scheduled

[02:19] tasks. We can refine a specific workflow and have it run automatically without us having to actually trigger this. We can have these run daily, weekly, hourly, or basically any cadence that we choose.

[02:30] Here's some examples of exactly what Claude Co-work can do for you while you sleep. You can have morning briefs every day at 7 a.m. by summarizing emails,

[02:39] your Google calendar, and your top priorities in Notion. We can even have a weekly report sent to us every single Monday by pulling data, formatting it, and saving it to something like Google Drive. There's so many things that we can do inside of Claude Co-work with scheduled tasks and it literally acts as if it's an employee. And it's really

[02:55] insane when you begin using this. That is what Claude Co-work is, but most people are barely scratching the surface of using this incredibly powerful tool. There are five levels to claude coowork that you need to master if you really want to harness the power of it. Let me

[03:08] show you all of them now. All right, so level one we have import. This is basically how we bring our memory and data from our other large language models like chatbt or Gemini directly into Claude. And if you're like me, you

[03:21] probably were procrastinating switching to Claude because that means you had to start from scratch. And this can take lots of time to try to go back and forth with Claude for it to understand you and your business. I'm going to show you this one hack that allows you to give Claude a prompt, paste it into chatbt and then chatbt will export your memory and all you have to do is paste that back into Claude and this will be set up in under 60 seconds. So in order to do

[03:44] this, we're going to come to this specific page that Claude actually set up for us. There's going to be a link in the description below and guys, this is going to save you so much time. All I need to do is click on get started and there's a couple of simple steps that we're going to go through right here.

[03:56] And as you can see on my screen, we get this popup that says import memory to claude. Copy this prompt into a chat with your other AI providers. I don't need to go through this entire prompt, but I'm just going to copy this and then I'm going to bring up chatbt because this is the, you know, large language model I've been using myself over the last 3 years. I'm simply going to paste

[04:15] this prompt in. All right, so just like that, I sent it off to chatbt. We now have this code here breaking down every single thing ChatVt knows about me. And

[04:23] guys, this is such a hack. I'm just going to bring this back to Claude. paste in this prompt, add it to my memory, and now it has all of the context on me that it had inside of chatbt. I will say this right here is

[04:33] the biggest step why people aren't switching to Claude Co-work. And this gives you a level up on other people who aren't yet using it. And this will just like simplify this. So, it's very easy

[04:42] to get up to speed and actually switch to Claude Co-work. So, in order to begin using Co-work, we need to download the Claude desktop app. There's going to be a link in the description as well as the pinned comment below in order to actually come to this. We're going to

[04:55] download it for Mac or Windows, whatever type of computer you're using. And then once we do that, we can then pull up our Clawude desktop app. What we're going to see is we're going to see a couple of different options here. If I come up to

[05:06] the top of my screen, you can see we have a chat mode, we have co-work mode, which is what we're going to focus on in this video, and we have code mode. I'm just going to click on co-work. And we're going to actually see this specific interface right here. And what

[05:19] I need to do, like a couple of things we need to focus on right now is how this works is we need to give it a specific folder or in this case I'm going to create a specific one. So what I'm going to do is I'm going to come here and click choose folder. Add new folder and I'm just going to call this Claude Co-work. I'm going to call this Claude

[05:35] Co 2 since I already have another one. So I'm going to open this up. I'm going to click on allow. So this basically

[05:40] means it's able to go off and add files to this folder and make edits to it as well. All right. So the next thing inside of our level two which is foundation that I'm going to add is my goals MD. So this is crucial because

[05:52] claude coowork if it can understand our goals on like a 3month basis, a weekly basis, a year basis, it's going to help me do the things that I need to do in order to accomplish these goals. So for example, what goes into this markdown file is my north star. So whether that is to grow to 100,000 subscribers by Q3 or, you know, break down my big quarterly goals or weekly priorities, all these different things. And the

[06:15] reason that this matters is because without goals, Claude is going to give us very generic responses. But this is really going to refine exactly how Claude Co-work is going to begin interacting with us. So what I'm going to do is I'm going to come back here and I'm going to say, I want you to help me craft a goals MD file. This way you

[06:32] could help me achieve my goals whether that is on a 3-month basis, a year basis or even a weekly basis. All right, so I personally went through went back and forth with Claude Co-work to establish my goals and Vile here. So let me break it down very simply. So Q1 2026 January

[06:46] to March. I want to publish two videos per week on my YouTube channel which is eight videos published in March. Basically it shows the status of this right here. also monthly focus. It

[06:56] breaks down this also weekly habits, all these different things. And it even shows my habit streaks here inside of this. So this is kind of like my north star, you know, all the things that I want to get done on a three-month basis, a quarterly basis, and a weekly basis.

[07:09] All right. So now we see a couple of different things inside of our Claude Co-work files here. So we have our instructions, which is our Claude MD file, which is again just the brain of our system. We now have a couple of

[07:18] other things. So we have this glossery markdown file. So this is basically a glossery of all the different terms that I use in my business. So co-worker is

[07:26] beginning to get an understanding of exactly what it is we do. It even has this one right here called Aiden Markdown just because this is the context on my co-founder AI for non techies. This is everything about my YouTube channel. And one thing I want to

[07:37] note is that right now this is very very slim in Bleke. There's not much in here. But the cool thing and one of the best things about Cloud Co-work is it just learns about you over time. Let me

[07:48] quickly show you something to explain what I mean. So right now, think of the claw empty file as kind of like our kitchen bible. And this is something that our chef is going in, you know, writing out specific instructions for for each, you know, particular recipe that it is that we're, you know, adding to our cookbook. And after every

[08:05] session, the think of the chef as like updating this book. So that way every single day when the new like when the sue chef or the, you know, the partner of the chef comes in, it understands exactly what it is that it needs to do for all these different specific tasks. So, this is a self-learning system that gets better over and over every single time that you use it. And the next bit

[08:25] of context I'm going to give is my company MD file here. So, I basically broke down my brand, my business name, the platforms I use, my tech stack, all these different things. So, let me come over to Claude now. And again, this is

[08:36] very, very simple. I'm going to, you know, refine this over time and add more and more as I, you know, go back and forth with Claude. But for the sake of this video, you know, this is what I came up with. But my actual operating

[08:46] system I use inside of co-work is much much more refined than this. All right, to recap that we just built the foundation for Claude Co-work. This is really important. I want you to think of

[08:55] this like onboarding a new hire. We write these files once and co-work is going to read them every single time that it starts a task for a specific thing that we wanted to do. And think of it like an employee that you don't need to keep giving instructions to. It just

[09:08] works automatically because it has all the context on how to get these things done. Now moving on to level three, we have workflows and this is really what takes Claud Co-work to the next level. So what exactly is a workflow in this specific system? And they are called

[09:22] plugins. Think of plugins as skill packs for every single job. So productivity, marketing, sales, finance, HR, design, all these different specific like departments for your company. They now

[09:35] have skill packs that we could upload directly into our co-work system and begin using automatically. And on top of that, not only do we have pre-built plugins we could access directly in Co-work, which I'm going to show you how to do right after this, but we could also build our own just by using natural language. So if we have a certain task that Co-work is doing for us, we just say, "Hey, I want you to, you know, turn this into a plugin that I could share with my team and they could plug that in to their system as well." I want to

[10:00] break down very simply kind of how these workflows work. So what it does is it's going to read a file that we crafted in the previous section of this video. For example, maybe it is my email inbox markdown file. It's now going to check

[10:12] my email. It's going to check my calendar. It's going to summarize it.

[10:15] And then the output will be the daily briefing. This is just a very basic example of one command that can trigger an entire workflow. So I could just type something like email or summary and it will go off and do this entire workflow for me. So in order to access these

[10:29] plugins and workflows in order to build them yourself, I'm going to show you exactly how to do that now. So we're going to come up to customize up on the top lefth hand side. We're going to see a couple of different things here. I'm

[10:39] going to click on browse plugins and we are going to see a bit of different like pre-built plugins that Enthropic actually gives us as well as we could create our own. And I'll show you how to do that. For example, let's say that we need, you know, a bit of legal help. We

[10:52] need to actually look at different documents or like non-disclosure agreements before we actually sign them. And we don't want have to hire a lawyer. Instead, we could just install this plugin which is, you know, a specific legal workflow and has a bunch of different commands and skills built inside of it. So, let me show you

[11:07] exactly what I mean. Now, if I click on this right here, this legal personal plugin, we're going to see a couple of different things. So, inside of here, we have different commands. And again,

[11:16] commands are specific keywords that trigger a workflow. So, if we select brief here and just type out brief and co-work, it's going to generate a contextual briefing for legal work, daily summary, topic research, or incident response. If I click on this, you could then see this markdown file.

[11:33] And this is basically like a very detailed um explanation of how this specific task should be completed. Let's click on review contract. This is one that I personally use for my influencer marketing agency to review contracts before signing them on behalf of our clients. So, I'm not going to go through

[11:48] this full file, but it's just a very comprehensive set of instructions that we didn't have to craft ourselves. It was built directly into this plug-in. And this is what makes this so revolutionary because you could just share this with your team and now they have access to this exact workflow. So,

[12:02] in order for me to come and test this out, let me go ahead and just click forward slash. I'm going to come to plugins. I'm going to click legal, and then let me go ahead and select the review contract. So, again, this is just

[12:14] going to invoke a specific workflow. And I'm just going to upload a contract that I want reviewed. All right. So, I just

[12:19] uploaded this PDF document of like this fake contract here for my influencer marketing agency. And I just clicked review contract. This is the specific command I'm going to give it to invoke this workflow. I'm going to send this

[12:30] off. And again, I did not have to like come up with this specific workflow myself. This is all thanks to the new plugins feature that automatically will import this into your co-work systems.

[12:39] All right, so a couple of minutes later and we have this output from co-work. It generated this document file that I could actually open here and I could even edit if I would like, but this is a contract review. I'm not going to go through all of this, but to break down simply what this did is it added its key find. So for example, it showed in

[12:55] yellow. This is basically like, you know, flagging that something in the contract is something that we need to like take a look at. It might not be exactly how we want it to be. And then

[13:04] green is like, okay, that's all good to go. No need to worry. So, this is like literally something that would have taken hours to craft if you were like a lawyer, for example. And now using this

[13:13] plugin and this command inside of Claude Co-work, you know, we could have this on autopilot and this was generated in literally like 2 minutes. And all I had to do is upload a specific, you know, document here for an agreement and then just say slash review contract. Real quick, I just wanted to show exactly how you could create your own plugins if you don't want to use one of the ones that's inside of the clawed, you know, ecosystem with the pre-built plugins.

[13:36] So, you can see I created this one called YouTube Analytics. There's a couple of different commands in here. There's a couple of different skills as well. So, I could open this up and it's

[13:42] basically a markdown file breaking down my YouTube analytics strategy and, you know, exactly what it is I wanted to do. And in order to do this, like I just had it perform a task in here. Like I was like, "Hey, I want you to every single day go and check my YouTube." And then

[13:55] give me all these key findings. And then all I did was come here and just say like make this into a plugin. And then if I come to customize, you can see I have this little local, you know, plugin. We could customize it. Or we

[14:06] could just click here, show in folder. And then we could actually go ahead and share this folder with your team member. They could upload it to their folder and then automatically have that system running inside of their Cloud Co-work.

[14:16] All right, moving on to level four of co-work and this is ecosystem because you're probably asking like Brock, if I want to think of Claude Co-work as an employee, how can that be the case if they don't have connections to all the apps that I use? So whether you use Gmail or notion or Slack or so many other applications, it's really important that we give co-work the access that it needs to our specific applications. So, for example, with one command or one prompt, we can now access four different applications when we combine the connectors with the workflows that we created earlier on in this video. So, for example, with one

[14:53] prompt, we can now have it read my emails inside of Gmail. It could check conflicts in my Google calendar. It could draft a reply in Gmail or even send it to me. Or it could save the

[15:02] summary into Google Drive. All these different applications you can now connect to inside of Co-work. And I'm going to show you exactly how to do so.

[15:09] What you're going to do is you're simply going to come up to the left hand side. We're going to click on customize just like we did for plugins. However, we are going to click this connectors button here and we have a couple of different connectors already configured inside of my project. Let me click on the plus

[15:23] button and show you all of the different things we could connect to. There are tons of different applications we could connect to right here. Right now, I'm just connected to Gmail, Google Calendar, Notion. I can connect to

[15:33] Figma. I'm connected to Slack. All of these different options here. And it's

[15:36] as simple as just like clicking on an app. For example, if I want to connect to Canva, I'm just going to continue with Google. Log into my Google Canva account. I'm going to click allow.

[15:44] Authorization successful. And if we come back to Claude, you can now see our Canva is connected. And it has access to all these different tools here. So, it

[15:53] could search for designs. It could generate designs with AI. And we could come here and like create custom restrictions if we want. However, I'm

[15:59] going to let it do its thing inside of Canva. So now it could actually go and generate graphics using that app and pull that information back into co-work. Let's say that you have a specific, you know, connector that you want to add, but it's not in here because right now there's only like maybe like 50 different preset connectors or I think there's maybe like 38 or something inside of Cloud Co-work at this time.

[16:19] What you could do is you could use something called the Zapier MCP which connects to 8,000 plus different apps. So let me show you exactly how to add that. Now, first of all, what you're going to do is you're going to look up zapier.com/mcp.

[16:30] And there's going to be a link in the description as well as all the other resources I've talked about in this video. I'm going to sign in or sign up for an account. And then what we're going to do is we're going to come up to the left hand side of its interface.

[16:41] Click on new MCP server. If you don't know what an MCP server is, it basically gives you access to all the different applications and tasks for it to perform with one specific server. It's really easy to set up. You don't need to be a

[16:52] developer to do this. For the client, I'm going to select Claude Co-work. And then what I'm going to do is simply just add any of the different tools that I want access to. So, for example, if you

[17:02] use Air Table and you want to pull data from Air Table or add data to Air Table, you could just select this, select all tools, click connect, and instantly connect this server to that application. And you could do that for as many of these different apps you want. Let's say we use Zenesk. Same exact thing. I'd

[17:17] click select, click connect, and then it would then be added to our server. So then all you're going to do is come up to the connectors feature. You're going to then come to connectors, browse connectors. You're just going to search

[17:27] for Zapier. I'm going to add this here. I'm just going to click on allow. And

[17:31] just like that, we have Zapier connected. And we could see each of these different applications we added. So for example, you could see Air Table could perform all these actions for us.

[17:39] As well as you can see Gmail, Google documents, all those different tools we're now able to access directly inside of Cloud Co-Work. All right guys, we're moving on to level five. And this is maybe the most important one because this is where we could tap into the power of automation. This is a new

[17:53] feature that they just added last week that allows you to schedule anything to run without you. Whether that's daily briefs, weekly reports, generating documents, recurring tasks, all these different things you can now do inside of co-work. So, for example, my morning brief that runs every single day at 7 a.m. It reads the cloud MD file, the

[18:10] goals MD file, and the task MD file. It will check my email in my Google calendar and then it will actually send me a daily briefing to read. And the best part about this is it gets better every single time that you use it because after each run, co-work rewrites its own instructions to basically customize how you interact with it. And

[18:29] there's a couple things that you need to know. Your computer has to be awake for this to happen. Claude desktop also has to be open. If your laptop is closed,

[18:36] it's going to have to wait for you and it's not going to be able to go off and be proactive unless it actually is open. So, in order to set these specific automations, what we're going to do is we're going to make sure we're inside of the folder that we want access to. We're going to click on schedule. And all we

[18:49] have to do is click on new task, and we could give it a name. Let's just call this competitor research. I'm going to give it a prompt and a description. I

[18:57] could select whichever model I want to use. I'm going to use Claude Opus 4.6 because that is the best large language model. I'm going to select my specific

[19:03] folder. And then I could choose a frequency. I'm going to do this daily, every single day at 9:00 a.m. All right.

[19:09] So, here's an example of probably my favorite workflow that I've built inside of Cloud Co-work over the past couple of days. So, what this does is every single day at 8 a.m., this scrapes my YouTube

[19:21] competitors and then generates this entire HTML dashboard for me to understand what my top filming priorities are for the day, trending topics that I can make content about, competitor YouTube videos, so I get an understanding of like what other people are making in the space. And it even creates content gaps for me. So, every day at 8:00 a.m. it automatically will

[19:39] send this to me as well as send a message in my Slack channel updating me on everything I should make content about that day or at least take a look at. And I want to explain real quickly. I basically built out this dashboard as well as this workflow. Basically, what I

[19:52] did is I clicked forward slash I clicked schedule and basically this creates a you know scheduled task or a workflow and I said every day at 8 a.m. I want you to run this entire workflow that you just created and generate the HTML dashboard. The reason that I even

[20:06] mention this is because you don't need to go and specifically create scheduled tasks. You could also be playing around in co-work have it do something and be like, "Oh, that was pretty cool. Can you now turn this into a scheduled task where you do this every day or every hour or once a week, for example." All

[20:21] right, guys. There we have it. This was a very detailed video. We went over the

[20:24] five levels of Claude Co-work. First of all, we have import. Then we have foundation. We have workflows,

[20:29] ecosystem, and automation. So, if you guys got some value from this video, please leave a like. Subscribe to this channel for more content like this. I

[20:36] have tons more Claude Co-work videos coming out.
