# How to Use Claude Cowork Projects Better Than 99% of People

**Channel**: Brock Mesarich | AI for Non Techies
**Duration**: 23:53
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=5bhh8ffHN6Q
**Transcribed**: 2026-03-24 12:06

---

## Organized Notes

**What Projects Are and Why They Matter**

- **Claude Cowork Projects** is a new feature from Anthropic that adds organizational structure to Cowork — solving the biggest pain point of **scattered tasks, no structure, and lost context** between sessions
- Before projects: everything lived in one workspace, **memory got cluttered**, rules from one domain bled into another, files piled up in a single folder
- A **project** is not a folder — it's an entire **ecosystem** that holds memory, scheduled tasks, skills, plugins, connectors, and a dedicated Claude MD file
- Three nested layers: **Project** (the container) → **Folders** (the workspace where files live) → **Claude MD** (the instructions Claude reads before every task)
- Projects **compound over time**: Day 1 feels generic → Day 30 Claude knows your tone, preferences, and runs tasks automatically → Day 90 Claude is essentially a **team member** responding to keywords and handling full workflows

**The Infrastructure: How Projects Work**

- Each project contains: **Claude MD** (instructions), **files** (documents, assets, data), **outputs** (HTML dashboards, presentations, spreadsheets), **memory**, **scheduled tasks**, **skills**, and **plugins**
- **Multiple folder selection** is now supported — you can work across several folders within one project
- **Memory is project-scoped** — each project maintains its own memory that stays focused and relevant to that domain
- **Starred chats** let you pin important conversations within a project for quick reference
- All **outputs** are now organized under their specific project instead of scattered across Cowork

**Claude MD vs. Projects: They Are Not the Same**

- A **project** has memory, scheduled tasks, skills, plugins, and connectors — it's the **infrastructure** of a specific system
- A **Claude MD file** specifies who you are, how you work, your rules, and your tone — it's the **personality** layer
- Projects do **NOT replace** Claude MD files — you should have a **separate Claude MD** for each project
- Claude MD is a prompt that Claude reads **before every single task** — it eliminates the need for long, repetitive prompts
- Structure of a Claude MD: **what this is** (project description), **how to work here** (specific instructions like "use the slide skill for video intros, track all videos in spreadsheet X")

**Why Separate Projects Are Essential**

- **Memory stays focused** — YouTube rules don't bleed into finance tasks
- **Each project has its own rules** — Claude knows exactly how to behave per domain
- **Scheduled tasks are scoped** — only relevant automations run per project
- **Clean file separation** — outputs, assets, and data stay organized by domain
- Recommended separation: one project per **business area** or **major workflow** (YouTube, agency, finance, community, etc.)

**Real-World Project Examples**

- **YouTube Videos project**: slideshow generation, weekly analytics reports, competitor scanning (21 competitors every 2 hours for trending topics and content gaps), video upload tracking to spreadsheet
- **Loom Agency project**: client information, creator rate cards, agency-specific memory
- **School Community project**: auto-scans for new posts/comments, suggests response content, generates community content ideas
- **Short Form project**: newly created, configured through conversational interaction with Claude

**How to Build a Project (4-Step Setup)**

1. Open **Claude Desktop app** (required — not available on claude.ai web)
2. Click **Projects** on the left sidebar → click the **plus button**
3. Three options: **Start from scratch**, **import from Claude chat** (carry over pre-existing chat projects), or **use an existing folder** (bring context from a prior workflow)
4. Name the project, write initial instructions (or let Claude build them through conversation), add files, enable **memory**, click **Create**
- **Pro plan** is sufficient — Max plan not required
- If projects don't appear: **delete and redownload** the Claude Desktop app (may take 2-4 attempts)

**Leveling Up Projects: Skills, Plugins, and Scheduled Tasks**

- Start by giving Claude a **brain dump** — who you are, your business area, your preferences for that specific project
- **Skills and plugins** are reusable workflows triggered by keywords (e.g., say "slides" + brain dump → auto-generates slideshow)
- Convert any ad-hoc task into a **scheduled task** — tell Claude "I want you to find the five email newsletter topics for me to cover this week" and it creates the automation
- Scheduled tasks can also be **added from existing tasks** across other projects

**Connecting to External Tools**

- **Native connectors**: Bit.ly, Canva, GitHub, Gmail, Google Calendar, and more — set up via **Customize → Connectors → Browse**
- For apps not natively supported: use **Zapier MCP** (zapier.com/mcp) to connect to **8,000+ apps**
- Zapier MCP setup: create new MCP server → select "Claude Cowork" as client → add tools for each app (e.g., HubSpot with 58 available actions) → copy URL → paste in Claude's Zapier connector
- Set tools to **"always on"** to skip approval prompts for trusted actions

**Dispatch Mode + Projects**

- **Cowork Dispatch** lets you text Claude from the **phone app** and trigger tasks on your desktop
- Dispatch now works **with projects** — you can specify which project a task should run in
- Enables on-the-go task execution: "Hey Claude, do this thing inside my YouTube project" from your phone → runs on your desktop computer

---

## What This Means for Your Work

You already operate with a sophisticated multi-project architecture across Claude Code — 9+ active projects with dedicated CLAUDE.md files, 129 skills, and Obsidian as your second brain. Cowork Projects essentially brings this same organizational discipline to nontechnical teammates. But several patterns in this video have direct implications for how you structure your own work and distribute capabilities to others.

**Project-scoped memory validates your dual-layer memory architecture.** Brock's key insight — that memory from YouTube bleeds into finance without separation — is the exact problem your Layer 1 (Claude Code Memory) + Layer 2 (Obsidian Vault) system already solves. Your per-project CLAUDE.md files in `~/.claude/projects/` are the Claude Code equivalent of Cowork's project-scoped memory. The validation here is that Anthropic is converging on the same architecture you've already built, confirming your approach is aligned with the platform's direction.

**Cowork Projects are the distribution layer for OOBC and MoroTech.** The most actionable takeaway is that Cowork Projects give non-developer teammates an organized environment to use your skills. Instead of handing someone a terminal and saying "run /bill-drafter," you could set up a Cowork project called "OOBC Legislative" with a Claude MD file that references your bill-drafting workflow, fact-checking rules, and BARMM officials reference. Staff could then work within that project without touching Claude Code CLI.

**The "compound over time" pattern maps to your vault-update workflow.** Brock describes Day 1 → Day 30 → Day 90 progression where Claude learns preferences and becomes a team member. Your /vault-update and /session-summary skills already implement this — capturing session learnings into persistent vault notes. The difference is your system is more deliberate (explicit vault writes) vs. Cowork's implicit memory accumulation. Your approach is more reliable for high-stakes governance work where you can't afford Claude "learning" incorrect patterns.

**Separate projects per business area is immediately applicable.** You currently manage e-Bangsamoro, MoroMarket, Parliamentarian, OBCMS, Tarbiyyah-MS, BangsamoroHR, IPP, SBP, and MoroTech as separate Claude Code projects. If any of these need non-dev collaborators (OOBC staff, BSA members, Moro Developers), setting up parallel Cowork Projects with domain-specific Claude MD files and scoped memory would let them contribute without your direct involvement in every task.

**Concrete next steps:**
- Evaluate creating a **"BARMM Legislative" Cowork Project** for OOBC team members — pre-loaded with BOL references, BAA index, officials list, and a Claude MD that enforces your fact-checking and first-mention naming conventions
- Test **importing your Claude chat projects** into Cowork to see if any legislative analysis or policy research from Claude Desktop sessions can be preserved
- The **Zapier MCP + project scoping** combination could streamline MoroMarket integrations — connect payment, logistics, and cooperative management APIs within a dedicated project context
- Consider a **MoroTech Training Cowork Project** where /training-assistant workflows are packaged as plugins for facilitators who don't use Claude Code

### How This Can Improve Your Claude Skills and Workflows

**Project templates as skill distribution packages.** Your 124-skill library in ~/Vault/Claude-Skills/ is built for the CLI. Cowork Projects add a GUI distribution layer. The highest-impact conversion candidates:
- **/bill-drafter** and **/resolution-drafter** → Package as a "BARMM Legislation" Cowork Project with a Claude MD that loads /bangsamoro context automatically. Parliamentary staff could draft bills through the Cowork interface
- **/training-assistant** → A "MoroTech Training" Cowork Project where facilitators invoke training design workflows without needing the terminal
- **/legislative-briefer** and **/policy-recommendation** → An "OOBC Policy" Cowork Project that OOBC consultants could use to produce CSW-format briefers and policy documents independently

**Scheduled tasks per project enhance your automation layer.** Your /session-summary and /vault-update skills currently require manual invocation. Cowork's project-scoped scheduled tasks could complement this:
- A daily scheduled task in a "Legislative Monitoring" project that scans for new BAAs, BTA resolutions, and parliamentary activity — outputting a briefing to a shared folder
- A weekly /vault-update equivalent in a "Knowledge Management" project that reviews vault health and flags stale notes
- The key constraint remains: **computer must be awake and Claude Desktop open**. For governance workflows that need reliability, your Claude Code + cron approach via /gitops is more dependable

**The Claude MD per-project pattern strengthens your /context skill.** Your /context skill loads project-specific context at session start. Cowork's approach of reading Claude MD before every task is the same pattern but enforced by the platform. This validates keeping your per-project CLAUDE.md files tight and domain-specific. Consider auditing your project CLAUDE.md files to ensure each one is as focused as Brock recommends — "what this is" + "how to work here" — removing anything Claude Code would discover through codebase traversal.

**Dispatch + Projects enables mobile-triggered governance workflows.** The combination of Cowork Dispatch (phone-to-desktop) with project scoping means you could trigger legislative analysis from your phone while in meetings or field visits. "Hey Claude, run the daily brief in my BARMM Legislative project" from your phone → the analysis runs on your desktop with full context. This is particularly useful for your consulting work where you're often away from your desk but need quick policy outputs.

**The multi-folder selection feature has implications for /devwork.** Your /devwork skill orchestrates work across frontend and backend repos. Cowork's new multi-folder selection (working across several folders in one project) mirrors this pattern for non-dev workflows. For e-Bangsamoro, a Cowork Project that spans both the documentation folder and the design assets folder could let non-dev team members contribute to requirements docs and review UI mockups in context.

---

## Transcript

[00:00] Anthropic just dropped projects inside of Cloud Co-work and this fixes one of co-work's biggest problems that I can almost guarantee you have right now and that is organization. If you've been using Co-work for more than a week, you probably have tasks scattered everywhere. No structure and Claude forgetting everything between sessions.

[00:16] Well, their new projects feature fixes this completely. So, in this video, I'm going to break down exactly what a project is, what a folder is, and what a Claude MD file is because most people think they're the same, and they are not. I'm also going to show you why you need separate projects for different areas of your work and how to configure each one so Claude actually gets smarter the more you use it. By the end of this

[00:38] video, you'll have a fully configured project that actually knows how you work. So, without further ado, let's dive right in. All right, so Enthropic just dropped projects inside of Co-work.

[00:47] And this honestly changes how I'm using Claude completely. So, I'm going to break down what projects are so you understand them at a fundamental level. Explain exactly what they are and then show you how you can begin setting them up as well as show my use cases I'm using for projects later in this video.

[01:02] So, let's quickly talk about what a normal day looks like now that I have projects set up inside of co-work. I have a morning brief that is waiting for me that's breaking down my calendar, my emails, and specific news. And all this is done before I sit down. And this is

[01:16] done inside of my agency project. I then have a 9:00 am inbox sweep and automatically drafts replies to my emails for me. And again, this is inside of my agency project. Then at 11 a.m., I

[01:27] automatically have Co-work generate the slideshows that I use in these videos. So that way, I could be ready to film for the day. And this is inside of my YouTube project. I also have a weekly

[01:36] analysis report generated at 2 p.m. that basically pulls my YouTube channel data.

[01:40] And this is inside of my YouTube project. And then I have a finance project that automatically scans all of my receipts that I have inside of a folder on my computer. And the best part about this is this whole system we're building and I'm going to show you in this video compounds over time. So this

[01:55] is basically what it will look like. Day one, we set up a project. We write a Claude MD file, install a couple of different skills, and Claude is helpful, but it kind of feels a bit generic.

[02:04] Whereas on day 30, we'll now have memory on all of our preferences. Claude knows our specific tone, how we like to interact with it. tasks run automatically without us having to think about them and the prompts that we give to co-work become much shorter. And then

[02:18] day 90, hypothetically, Claude is a team member where you can just give specific keywords. It goes off and performs entire workflows for you. All of the scheduled tasks, handle all the boring things inside of your business and you rarely have to think about any of this stuff. So, let's talk about what exactly

[02:34] we are building when we begin using and tapping into the new projects features. Think of it like this. We are not setting up a folder. We're building an

[02:41] entire ecosystem where we could work and spin up different AI employees inside of Cloud Co-work. So, we have an assistant that knows who we are with our preferences, our tone, and our rules, and it never forgets how to do these things. We then have workflows that automatically run themselves with skills, scheduled tasks, and even co-work dispatch mode, which I'm going to talk about later in this video. So,

[03:02] work could happen for us while we're not even at our computer. Then we have our system connected to all of our different tools, whether that's Gmail, Slack, Calendar, Google Drive, Notion, basically anything we could think of. So it could perform tasks and actions across those apps. And the best part

[03:15] about this is it gets better every single day because inside of these projects, the memory compounds. So it learns more about you, how you want to work, and all of your preferences. So let's quickly talk about now the three different pieces we have inside of Co-work now that we have projects inside of here. So first of all we have the

[03:33] project which is basically the container. This holds everything together that we've built inside of co-work. Then inside of the projects we then have folders and this is the workspace where all of our files live.

[03:45] Then we have claude MD which is basically the instructions that Claude uses for every single prompt that you give it. I'm just going to quickly break down like the infrastructure and how this works at a high level. And then I'm going to show you inside of Co-work what this looks like and how you can begin setting these up. So they all nest

[04:01] inside of each other. So you can see on the outside we have the project here which is basically the entire ecosystem for a specific workflow or specific part of your business. And inside of that we have the cloud MD which is our instructions. We have all of our files

[04:14] such as like our documents, our assets and basically all the data that it has on our business. And we have the outputs whether that's like HTML dashboards or generated presentations or spreadsheets all those different things. And then we also have memory scheduled tasks skills and plugins. and we're going to talk

[04:29] about all those later in this video. So, the first thing we're going to do is make sure that you have the Claude desktop app downloaded on your computer. Otherwise, you cannot access this over the web. If you just come to claude.ai,

[04:42] you won't be able to access co-work here. So, I'm just going to click on this. There's going to be a link in the description as well, just to make it easy for you guys. And then just make

[04:49] sure to download this. I already have it downloaded, so I'm not going to do it, but it'll just pop up in downloads here. And double click it, and we'll instantly just download to your computer. And then

[04:58] once we open up the claude desktop app, we're going to see this interface here. It says good afternoon Brock. We have chat mode which is basically like chatbt or normal claude on the web. We can just

[05:08] chat back and forth with it. It can give us answers, do specific things, but can't really work inside of our computer and inside of our folders. So that is what co-work actually does for us. So

[05:17] I'm going to click up here, click on co-work. So, let me break down kind of simply what the co-work interface is, a couple of the different features, and then we're going to dive into the projects I have, as well as how you could begin crafting your own projects as well. So, first things first, we have folders here. As you can see, I have one

[05:33] pulled up called Claude Code short system. I have a short form content folder, a claude folder, receipts folder, all these different folders. And these are basically folders that we have on our desktop. So to show you exactly

[05:46] what I mean, if I open this folder on my computer, you can see our cloud code short system, we have a bunch of different outputs here. We have a school folder. We have different MD files. We

[05:56] have HTML things. This is basically, you know, where co-work is working and creating all these different files on our computer for us to use. So what we could do is we could either select one that we have pre-existing or I'm going to show you how to create one now. You

[06:10] just come and click on choose new folder. You could open one you already have on your computer or you could just click on new folder. I'm going to call this claw test. Click on create. I'm

[06:19] going to click on open. Click allow. So it's able to go off and do that. And

[06:22] then now you could see claude testing here. One thing I do want to mention is they did add a new feature inside of co-work where you can now select multiple different folders. So if you want to work across a couple of different, you know, folders you have on your computer, you can now just select a couple of them now. And you can see we

[06:36] now have, you know, a couple of folders here we could work inside of. Now moving on to projects. If we select this folder here, you could now see there is something called projects at the very bottom of this. And I have a couple of

[06:48] them here and I could even create a new one. But let me just break down the projects I have in co-work right now, specific use cases I'm using for them. And then I'm going to show you how you could begin building your own as well as I'm going to show best practices so you could really leverage this new feature to 10x your productivity and make it so much more organized so it's easier for you to use co-work. If I come over to

[07:08] the left-hand side, you can see we have a couple of different projects here. I have short form, I have school community, I have Loom agency, and I have YouTube videos. So for me, these are specific areas that are like different businesses or different like layers of my business. So that way I

[07:23] could stay organized. So if I click on the YouTube videos project, this is what the interface is going to look like. So, let me break down exactly how this works for my specific use case so you can understand kind of the structure of what projects are, how they work, and how you could actually leverage them. We have

[07:38] this like chat interface here where I could basically just chat with co-work. I could tell it to go do things. I could use my civic skills that I have already set in co-work, which I have a bunch right here. I actually give them away in

[07:48] my school community. There's a link in the description to sign up if you're interested. No pressure, but if you guys want to like basically get a sense of how I'm using co-work on a day-to-day basis, that is a great place to stay up to date as well as just get all the skills and workflows I have built for myself. So, a couple of different

[08:03] things. If I go down, you can now see we have this output section, which is basically any output that Co-work gives us in this specific project. So, anything YouTube related, this is where I'm going inside of Claude. Now, before

[08:16] we would have all these different tasks scattered throughout co-work, and it just was a pain to like stay organized where now we could see any output we have. For example, you could see this hooks file here. We have this output that breaks down what claude projects are. We have a teleprompter skill. We

[08:30] have a specific slideshow, which I actually generated for this video inside of this project. So, this is where all of our outputs are going to be inside of this specific project. Now, moving down, I have a starred chat here. So you could

[08:43] go and basically like star any of your chats. So that way you could kind of pin them and then we could see all of our recent history of the different chats or tasks we've had co-work do inside of this specific project. And then moving on to the right hand side and this is probably maybe one of my favorite features inside of this. We could see

[09:00] all of the scheduled tasks we have for a specific project inside of co-work. So for example, I have two that are configured right now inside of my YouTube kind of system I have built out. And let me break these down right now.

[09:12] So, this one, if I click on it, it's going to show a bit more about what it's about. So, the description says, "Check YouTube for new video uploads and add them to this kind of spreadsheet here." And this repeats every single day at 11:01 a.m. So, if I have my computer

[09:26] open and I have the Claw desktop app open, it's going off performing this task and logging if I film the video. And if it does, basically adds it along with the stats to a specific spreadsheet. So this way inside of this co-work project, it's always up to date with what's going on inside of my YouTube business. So here's an

[09:43] instruction that I have. I just had Claude actually create these instructions. We could see all of the history of, you know, every single time that this specific scheduled task ran. I

[09:52] could run it right now to test it and, you know, see if it works. And we could also add our existing tasks we have. So I have a morning briefing task that I could automatically add to YouTube.

[10:01] However, I'm going to keep that separate because my morning briefing pulls my calendar, my email, and basically gives me update on AI news. It's not really YouTube related. So, I'm going to add that personally to a different project.

[10:12] I also have this YouTube competitor scan task here that will automatically scan 21 of my different YouTube competitors for trending topics, viral content, and finds content gaps every 2 hours. So, that way I can stay up to date and understand what should I actually be making content about for the day. And then if we move down, you could see that we now have context here. So this shows

[10:34] the YouTube videos project I have. It shows all the different outputs. It shows my claude MD file, which I could actually pull up here. I have basically

[10:42] every single output that it's gave me. It shows all of the skills I have inside of this particular project that I've actually invoked. And then I also have this memory section here, which is really crucial and one of the big reasons why project is amazing because it could actually, you know, remember your previous chats. so it can

[10:57] understand, hey, what did we talk about yesterday? Instead of co-work having to start from scratch every time. This right here, guys, is so helpful because if you've used co-work before, you could lose some of the skills you have. If you

[11:08] wanted to access a skills you had, you'd have to come up to customize, click on skills, and go through a whole list of different skills you have for tons of different like areas of your business and it would just get really cluttered. As well as any outputs. So, for example, this output right here, I have specific school guides. So whenever I make a, you

[11:23] know, resource that gets added to school, it will automatically save right there. As well as any of the different slideshows I create, it will now be under this folder. So you guys could already see just how organized this is making my co-work experience. And this

[11:36] is hands down the best feature that I've seen added to co-work since this whole entire platform came out. So this is my YouTube videos project. Let me just move on and show you real quickly a quick glimpse of how my other projects work.

[11:47] And then I'm going to break down more about like the infrastructure, how this really works, and then show you how you could begin building out your own. So I have one called Loom Agency here. So this is for my influencer marketing agency. This is where I like handle all

[11:59] of my, you know, client information. So I basically have creator rates in here. So for this agency, I basically help YouTube creators partner with different AI brands. So I break down creator rate

[12:09] cards for each of the creators we manage. I have Loom memory here, which is basically just like an understanding of my entire agency. And then moving up, I have a couple of other ones. I have

[12:17] school community, which is basically everything school related. I have this scheduled task here that will automatically scan my school community, find all of the new posts and comments, so that way I could respond to each of them individually, as well as it even comes up with auto suggestions for content for me to make in there that could address the questions that my school community members have. So again, if you guys want to join, there's a link in the description to do so. It's been a

[12:41] really valuable community to people that want to really understand co-work and different use cases as well as there's some pretty amazing people in there doing some pretty cool things. It's a great place to network. Then lastly, I have a short form project which I actually just created right before this video. So, it's pretty dry in here. I

[12:55] don't really have much in here. But in order to configure this, I could just come here and just say, you know, here's how I want this to work. I want you to, you know, use these different short form scripts. Like basically interact with

[13:04] Claude and it will build out this entire project for you with the proper context. All right. So, now that you've seen kind of how I'm using projects, what the interface looks like, what's new, let's just talk about now the best practices and I'm also going to address some questions that you probably have right now. I've had tons of people in my

[13:20] community over the last 2 days ask what's the difference between projects and a claim MD file? Like, do we need a cloud MD file now that we have projects? So, let me address that right now. So,

[13:30] think of it this way. A project has memory, scheduled tasks, skills, plugins, and connectors. This is basically the infrastructure of a specific system inside of co-work.

[13:40] Whereas the cloudmomd file, this is where we specify who we are, how we work, our rules, and our specific tone. So think of this more as like our personality kind of. Lots of people have been asking me like, does this replace the need for a cloud MD file? And the

[13:52] answer is no. You should have a claim file for each different project you have. So let's break down kind of the structure of a claude MD file and explain what are the use cases of it, why you should even have this configured. So, this is basically a

[14:04] prompt that Claude reads before every single task that you give it. So, you don't need to explain yourself anymore or give it a really long prompt. Basically, like this is how it's structured. Says what this is, breaks

[14:15] down exactly what that project is. So, for example, my hub for planning YouTube content, how to work here, use the slide skill for video intros, track all videos in a specific spreadsheet. Like, this is a very TLDDR version of what should be inside of this. It should be a bit more,

[14:30] you know, broken down instead of there being a bit of nuance. But this is kind of like high level what it would look like. So now let's talk about why we actually need separate projects inside of co-work. And this will instantly

[14:41] level up your experience. I can almost guarantee you that. So before I had one project for every single thing that I wanted done on my computer and with this memory gets cluttered fast for me.

[14:51] YouTube rules bled into my finance tasks. Claude confuses which tone to use for different tasks. scheduled tasks pile up and files from every area are inside of one folder and this is just so cluttered. Whereas now if we have

[15:04] separate projects for each different like avenue of our business, the memory now stays focused and relevant for a specific task. Each project now has its own specific rules so you could kind of configure it to how you want to. Claude knows exactly how to behave for different tasks. We have scheduled tasks

[15:20] that are scoped out and we have clean separation of files which just makes my life and your life easier. And what this would look like in practice for me obviously like we have YouTube videos so I have my Claude MD file inside there. I have my specific outputs. I have

[15:33] specific rules. If you have an agency, you should have one for your agency. If you want a project for finance cuz you want Claude Co-work to like manage your receipts or help you with bookkeeping, you should create a separate project for that. All right, so now let's talk about

[15:45] how you could begin building out a project yourself. And it's really simple. Takes about four steps and might take like 2 to 3 minutes for you. So,

[15:52] the first thing we're going to do is we're going to come back to our Claude desktop app. I'm going to come over to projects. So, if you guys don't see projects here on the lefth hand side, so many people in my community have asked like, I I don't see it in my Claude. Do

[16:05] I not have it on the pro plan? Do I need to be on the max plan? The answer is no.

[16:08] If you're on the pro plan, you will have access to this feature. You'll just need to go and reddownload claude onto your computer. And for me personally, I had to do this three or four times for it to show up. It could be a bit buggy. So, if

[16:21] it's not showing up, I'm just telling you, take this advice. Go delete the Cloud Desktop app, redownload it, see if it's there. If it didn't work, try that one or two more times, and I can almost guarantee it should be there. It'll

[16:32] probably fix your problem. But what we do now is just click on this plus button. We could either start from scratch. We could import a pre-existing

[16:40] project from normal Claude chat mode. So, if you didn't know already, Claude projects have been out for quite a while now, but it's just new specifically for Claude Co-work. So, if you have pre-existing projects in Claude that you want to carry over to co-work, you can do that with this button right here. So,

[16:55] for example, I could open this up. I could search for a specific project that I had from chat and I could just simply create that here. And then I could also choose the location and the specific folder I want this to work inside of. Or

[17:06] we could use an existing folder. So, let's say you don't have a project preconfigured from chat mode back in the day. You don't want to start from scratch. You want to take some context

[17:14] from a pre-existing folder or workflow you were working on. You could click this, select a specific folder and create that that way. What I'm going to do just for the sake of it is just start from scratch here. So, we just give this

[17:25] a name. Maybe let's call this email newsletter or something. I could write in my specific instructions here. Or the

[17:31] more you chat with Claude inside the project, it will kind of preconfigure the instructions for you. And then we could add any of the files here that we'd like to add. And then again, just choose the location. And memory is on

[17:42] here, which is really going to level up the experience inside of projects for you. Then all I would do is just click on create. And now we have five different projects here. I could click

[17:50] on it. And since this is a new project, we don't see any of this stuff configured. We don't have scheduled tasks. We have this email newsletter

[17:56] folder, but the folder is empty. And the memory, there's basically nothing here since we haven't used this yet. But as you can see, it says ask Claude to remember something. And I'll save it

[18:04] here. So let me just say I run a newsletter for people that want to keep up to date with AI. It's called AI for non techies. So now that I actually

[18:11] started this task here inside of co-work, we're going to see it now on the lefth hand side where it shows recent. It's now going to save this to this specific file here. And I'm going to show you what it looks like when it's added. And then if I come back to email

[18:22] newsletter, you can now see we have this memory markdown file that has a subfile that is called user newsletter markdown. And then we could also see this recent chat here, which I could easily pull up. It's super easy to do. Let's say we now

[18:36] want to add a scheduled task in here. We just come here, click scheduled task. We could either create a new task or we could just come here and explain to Claude and say, "Hey, I want you to find the five email newsletter topics for me to cover this week in the AI space." And

[18:50] then it will actually turn that into a scheduled task automatically. All right. So, now that we've actually begin setting up a project inside of Claude Co-work, I'm going to show you kind of powerful features we could add to really level up our experience here to add the most utility possible to Claude.

[19:04] Obviously, I showed you what the memory feature is. I suggest just like giving Claude a brain dump on who you are, your specific area in your business that you want to focus on inside of that project. And you can just do that conversationally with Claude the more and more you speak with it. And then the

[19:16] next big things are skills and plugins. So if you don't know what these are, these are basically reusable workflows that we could have for specific tasks where we could give it a keyword and we'll automatically have a specific prompt in order to complete a task for us. So, I have a skill that creates these slideshows for me for videos. And

[19:34] all I have to do is say slides, give a brain dump on what the video is about, and it will automatically preconfigure this for me. That's a quick example of what a skill is. And then, if we really want to level this up, we use scheduled tasks. So, we could then turn those

[19:46] skills or plugins into scheduled tasks so they could run automatically. So, a key thing that we really need to make sure we do in order to harness the full power of Co-work and specifically co-work projects, we need to connect Claude to all the different tools we use. So, Gmail, Slack, Google Calendar, basically any of the tools you use. If

[20:04] you want Claude to go off and perform the tasks inside those apps for you, you need to configure them properly. So, in order to do this, we just come up to customize. We come to connectors. And

[20:13] here you could see I have a couple of these preconfigured. I have Bit.ly, Canva, GitHub, Gmail, Google Calendar, all these different apps that I basically have access to inside of my co-work. And if we want to add one, we

[20:25] just click on browse connectors. You can see we have a bunch of different options here. If there is something that you can't actually connect to inside of Claude, because right now it's limited to a certain amount of different applications, I'm going to show you a hack that will show you how to connect your Claude to different apps that aren't native inside of Claude. So,

[20:41] personally, something I use to do this is I use Zap Your MCP. It's really easy to get started and begin connecting an MCP server. I'm just going to click on start building, and there's a link in the description as well if you want to set this up. Let me just preface. You

[20:53] don't need to use Zappy or MCP servers at all, unless there's a specific app that you want to connect to that isn't native inside of Claude. So, what I'm going to do is I'm going to click on new MCP server. Then, I'm going to click on Claude Co-work. From here, we're going

[21:06] to see a couple of different things. Right now, I have a couple of tools configured here that Claude Co-work has access to. Google Drive, School, and Google Docs. I could come and add any of

[21:16] these different apps here. And as you can see, there's 8,000 plus different apps that Zapier connects to. So I could select any of those. Let's say I want to

[21:24] connect to HubSpot. I'm going to click on select all tools. And you can see there's 58 different selections here.

[21:29] These are all different tasks that Claude can do and perform for us now. So we could add contact to list, create company, deprecated, create a company, create a contact. All these things we can now have Claude do. Next, all we

[21:40] have to do is click on connect, add different tools, and from here we're just going to click on this connect button. Copy a URL we're going to see inside of here. Then we're just going to go back to Claude. I'm going to click on

[21:51] browse connectors. I'm going to look up Zapier. I personally have already installed this, but we just paste in the URL we got from Zapier. And we would now

[21:59] have access to all of these different apps inside of Claude. So, as you can see, if I click on Zapier, I now have access to all of these different tools here. And if you want to basically give access so it doesn't always need to ask if it could do certain things for you, I would just click on always on so that way it doesn't need approval unless there's something that you think you need to have oversight for. so it

[22:18] doesn't go off and just like do a bunch of different things. Moving on to a new feature that just dropped a couple of days ago that I covered on this YouTube channel. If you don't know what co-work dispatches, I made a video on this YouTube channel breaking it down in depth as well as I created another video where I show five use cases I'm personally using it for. Basically, what

[22:36] this does is it allows you to text Claude in the Claude phone app and it will trigger Claude co-work on your computer so it could go off and perform tasks for you. So you have access to any of the skills you have, any of the projects, and this is all running on your desktop. So we could then take advantage of the fact that dispatch and projects now work together. So we can

[22:55] now use this on the go. Just to give you a quick example on how you could begin doing this. You would come up, click on dispatch here if you're in the desktop app. And as you can see, I have this

[23:04] chat interface here where I could basically just chat with Claude and say, "Hey Claude, I want you to go and do this thing inside of this specific project." and then it will go ahead and you know do things inside of each of the projects you have configured. And lastly, if you guys want more valuable content, make sure to join my school community. We have some highlevel

[23:21] entrepreneurs in here figuring out the best ways and best practices when it comes to Claude Co-work. And I give exclusive resources in this school community every single week. So, if you want to dive deeper into Cloud Co-work, this is the perfect place to do it, even if you're non-technical. And with that

[23:35] being said, guys, if you want more free content like this, make sure to subscribe to the YouTube channel. You don't need to be in the school community if you still want to get valuable content like this. With that being said, leave a like if you enjoyed this video.

[23:46] Let me know your thoughts in the comments below. Let me know what you want me to cover in coming videos. And with that being said, guys, I hope you have a good day and I'll see you in the next
