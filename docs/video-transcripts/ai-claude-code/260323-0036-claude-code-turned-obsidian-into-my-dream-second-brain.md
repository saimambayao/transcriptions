# Claude Code Turned Obsidian Into My Dream Second Brain

**Channel**: Mark Kashef
**Duration**: 14:00
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=2kbINqpluM0
**Transcribed**: 2026-03-23 00:36

---

## Organized Notes

**What This Is**

- Use **Obsidian + Claude Code** together as a second brain
- Obsidian = free local app that stores everything as **markdown files in a folder**
- Claude Code connects via Obsidian's **CLI (95 commands)** — no manual CLI knowledge needed
- Graph view shows **semantic relationships** between all notes, tasks, and ideas

**Why Obsidian + Claude Code Works**

- Obsidian files are **just markdown** — Claude Code reads/writes them natively
- You can open Claude Code **inside your Obsidian vault folder** for full context
- Point your `CLAUDE.md` at specific vault paths to **always inject context**
- Every note is **searchable via CLI** from Claude Code

**Setup**

1. Download **Obsidian app** from obsidian.md/download
2. Install the **Obsidian CLI**
3. Enable **CLI accessibility** in Obsidian Settings > General (bottom)
4. Install the **Obsidian skills** for Claude Code (CLI skill + JSON canvas skill)

**Vault Setup Skill (`/vault-setup`)**

- Asks **4 questions** to build your personalized vault structure:
  1. What do you do for work?
  2. What falls through the cracks / what do you wish you tracked better?
  3. Work only or personal life too?
  4. Existing files to import?
- Can use **multiple-choice format** via `ask user input` tool for less friction
- Generates vault structure in **< 5 seconds** — fully configurable
- Installs **slash commands**:
  - `/daily` — daily brief across business/life
  - `/standup` — project briefings
  - `/tldr` — summarize current conversation, extract next steps, store in Obsidian

**Importing Existing Documents (PDF Pipeline)**

1. Feed messy files (PDFs, Excel, JSON) to Claude Code → **organize by file type**
2. Use a **cheap large-context API** (e.g., Gemini Flash, 1M context) to convert PDFs → markdown
3. Second pass: **synthesize salient points** into compressed cheat sheet markdown
4. Import clean markdown cheat sheets into Obsidian via **CLI skills**
- Result: **signal without the noise** from large documents

**Key Features**

- **Canvases** — visual maps like Miro/Excalidraw, created programmatically via JSON canvas skill
- **Graph view** — filterable by attachments, orphan tasks, groupings
- **Inbox folder** — dump unorganized ideas; Claude Code **auto-categorizes** them later
- **Tags and dates** — all searchable from Claude Code
- **Mobile app** available (small cloud plan required for sync)

**The Core Value**

- One place for **all compartments of life** — work, personal, business
- Everything **well-organized, well-documented, no stale documents**
- Claude Code handles the **organization burden** — you just talk in plain English
- `/tldr` at the end of any session = **automatic knowledge capture**

## What This Means for Your Work

**You have already built a more sophisticated version of what this video describes -- but the PDF pipeline is worth adopting.** Your Obsidian vault at ~/Vault/ with dual-layer memory (Claude Code memory + vault), wikilinks, and INDEX.md routing is ahead of what Mark Kashef demonstrates. Where this video adds value is the PDF-to-markdown pipeline: use a cheap large-context API (Gemini Flash, 1M context) to convert dense PDFs to markdown, then a second pass to synthesize salient points into compressed cheat sheets. This is directly applicable to your local reference files -- the Parliament-and-Committee-2025.pdf, RA 11054 PDF, and BDP chapters could all benefit from this two-pass distillation into scannable vault notes.

**The /vault-setup skill's four-question approach is a useful template for onboarding new project vaults.** When you spin up a new platform project (say, IPP or OBCMS), asking (1) what does this platform do, (2) what falls through the cracks, (3) work scope, and (4) existing files to import -- then generating the folder structure automatically -- would standardize your project initialization. Your current approach of manually creating vault sections could be replaced with a skill that scaffolds project-specific vault structures based on your platform template.

**The /tldr command at the end of every session is a habit worth formalizing.** You already capture session context through your memory system, but Mark's approach of ending every conversation with /tldr -- which summarizes, extracts next steps, and stores in Obsidian -- would create a searchable log of every Claude Code session. For your multi-role work (OOBC consulting, legislative research, platform development, community leadership), being able to search your vault for "what did I decide about the cooperative registration flow last Tuesday?" would reduce the context re-explanation that eats into productive time.

**The canvas feature (JSON canvas skill) could visualize your platform architectures.** Your 9 platforms share common infrastructure but serve different domains. Creating programmatic canvases showing how e-Bangsamoro connects to OBCMS, how MoroMarket relates to e-Negosyo, and how BangsamoroHR interfaces with the Parliamentarian system would give you a visual map of your entire ecosystem -- useful for planning shared components and identifying integration points.

### How This Can Improve Your Claude Skills and Workflows

**The PDF-to-markdown pipeline (two-pass distillation) should be added as a mode in your /obsidian skill.** Mark's approach -- Gemini Flash for raw PDF-to-markdown conversion, then a second Claude pass for synthesis into scannable cheat sheets -- is directly applicable to your local reference files. Your PDFs/ folder contains Parliament-and-Committee-2025.pdf and RA 11054.pdf. A `/obsidian --ingest-pdf` mode would automate: (1) send PDF to Gemini Flash (1M context, cheap), (2) receive raw markdown, (3) Claude synthesizes salient points, (4) save to ~/Vault/ with proper wikilinks and frontmatter. This preserves your token budget for analytical work.

**The /vault-setup skill's four-question onboarding pattern should be replicated for new platform projects.** When you create a new project (IPP, the next government platform), a skill that asks (1) what does this platform do, (2) what falls through the cracks in this domain, (3) scope boundaries, and (4) existing reference files to import -- then scaffolds the project's vault structure and CLAUDE.md -- would standardize your project initialization across all 9+ platforms. This is a natural addition to your /vault-update skill.

**The /tldr command pattern should be integrated as a post-session hook.** Mark's approach of ending every session with /tldr (summarize, extract next steps, store in Obsidian) aligns with your /session-summary skill but adds the critical "extract next steps" component. Your /session-summary could be enhanced to produce a structured output: (1) what was accomplished, (2) decisions made, (3) next steps with priority, (4) files changed. Store in ~/Vault/projects/{platform}/sessions/ so your /context skill loads the latest when you return to that project.

**The canvas (JSON canvas skill) has a specific application for your Bangsamoro legislative tracking.** Beyond platform architecture visualization, create programmatic canvases showing the relationship between bills in the BTA Parliament pipeline: which bills block others, which share committee jurisdiction, which align with specific BDP priorities. Your /bill-drafter skill could output a canvas node as part of its deliverable, automatically linking the new bill to related legislation in the visual map. This gives your OOBC team a legislative landscape view that no other tool provides.

---

## Transcript

[00:00] If you've always wanted to build a second brain, one that you can consistently update and more importantly leverage for all kinds of use cases, then this video is for you. I've personally tried to use a tool called Obsidian five times in my life. Five.

[00:13] And every single time I got the exact same outcome. I'd set it up, I'd organize it, and I'd use it religiously for a whole week. And the week right after, I would forget it even existed.

[00:23] But this changed on the sixth time when I combined Obsidian with Cloud Code. So, in this video, I'm going to show you how you can use this match made in heaven to build the second brain you've always wanted. I'm going to walk you through what it is, what it looks like, how you can set it up, and how you can start getting productivity gains from it today. Let's dive in. All right, so what

[00:42] you're looking at right here is a graph view of all of my thoughts, ideas, and tasks that live in the Obsidian app on my local Mac computer. Now, they have an app for both Windows and Mac, so you should be covered. And if you ever want to be able to take it mobile on the go, they also have a mobile app as well. If

[00:59] you just want to work on it on your desktop, then it's completely free. And if you want to take it on the go and use the cloud, then they do have a small cloud plan if that's of interest to you. And while this has many features, this is probably one of the coolest because if I hover over any one of these bullets, you can see this relates to a Claude skills video section. And related

[01:18] and everything that's adjacent to it is something related semantically to Claude's skills. So you can see that a few of these are existing videos that have already dropped on this channel. And beyond that, at the left hand side, this is where all of our tasks live.

[01:32] Behind the scenes, like I said, Obsidian is just a folder with a series of markdown files. So each one of these are composed of different markdown files categorized in different folders. If you have a brand new idea that doesn't necessarily have a designated home, it can land in the inbox until you, or in this case, cloud code can autocategorize and place it where it fits best. And for

[01:52] all of you notebook LM lovers, they have something called canvases where you can pull up a map in what's called your vault. That's basically the collection of markdown files in this folder. We can go through this which I produced in less than 10 seconds which is a breakdown of different genative AI concepts. So if

[02:10] you do like things like mermaid diagrams, like ask art, it lends itself to this as well. And in terms of the files themselves, they look very similar to something like Notion where you have a series of markdown headers, formatting, [music] the ability to add a date and a tag. And the best part is all of these are now searchable by using their command line interface, which I'll show you in a second with Cloud Code.

[02:33] And when it comes to looking at your graph view, you can not just look at it visibly, but you can also filter it. So you can visually filter the ones that have attachments, have existing files. if you have an orphan task, meaning one that doesn't seem to be connected to any other topic and then you can have different ways to group them and configure them. So this is the app and

[02:53] now I'll show you the bridge to cloud code. So Obsidian has a command line interface. So if you write the word Obsidian after installing it and I'll show you how you can install it, you'll get this beautiful purple logo and then these are all the functionalities, all 95 of the commands. So you can see

[03:10] things here like creating brand new bases, bookmarks, different commands, having daily tasks, deleting everything that you'd need from an API or from a functionality standpoint. And the best part is you don't have to understand how to use the CLI yourself. Claude Code can onboard itself once you've installed it and understand how to leverage each and every functionality. And if you want to

[03:32] make it even easier, I'm going to show you some skills that you can install for free that will make this process of connecting the Cloud Code to your Obsidian Brain that much easier. So to download the app, all you have to do is go to obsidian.mmd/d download. And if you want to download

[03:46] the command line interface, highly recommend to be able to use it effectively. Then you'll go right here. Once you have both installed, you're going to want to go to the very bottom of the general tab of your settings and just make sure that the command line interface accessibility is set to on. So

[04:01] that's the what and the how. But when it comes to the why, the goal is just to have one place where you have different compartments of your life, your business, both that can all live in cohesion where everything's well organized, well documented, and you don't have stale documents. And depending on what you're working on or if you're thinking about something on the go, or if you're brainstorming, each different section of your life also has sub levels or subfolders. And that's

[04:27] where Obsidian can help you out because if you have a personal thing, but there's a certain category for said thing, Claude Code can just listen to you in plain English and it can help designate where this fits best so you can recall it later. Unfortunately for me, this is a cross-section of my brain where it's practically always on fire in every single department. And one thing that I've been awful at my whole life is finding a tool, an app, anything to plant my roots in. So you can name any

[04:53] tool and you'll find it in my graveyard. Whether that's notion, Apple notes, Evernote, to-d doist, bare markdown folders of my own, I've always found a way to lose track of everything. So the appeal here is pretty simple. You have

[05:08] this file cabinet of different markdown files. You can use these markdown files wherever you want on your system because they live on your folder. And then if you want to bring it into a cloud code session, you could literally tell your cloud MD, hey, always refer to insert path of all of these markdown files when I ask you about XYZ. It's so malleable

[05:28] that you could even open a brand new Cloud Code instance in your Obsidian folder if you want to be fully contextualized with each and everything in your life. Now, once you've installed everything, you can layer on these Obsidian skills where if we look at the very bottom here and we zoom in, we have one specifically for leveraging and interacting with the Obsidian CLI, which is basically that dark screen I showed you with all 95 different functionalities. This would give Claude Code a cheat code to leverage them. And

[05:57] if you enjoyed those notebook LM images and diagrams, then this skill would allow you to create those canvases that much more easily. So everything might sound and look good, but you might be asking yourself this very pertinent question. How do I even get started and set up to organize all my thoughts into these folders? Because that time

[06:16] investment alone might be worse than any benefit that you could derive from it. As usual though, I got you covered. So if we pull up a brand new instance of Claude Code, I've created this command called vault setup. And depending on who

[06:30] you are, it will ask you a series of questions. So we're just going to send this over. So it just asks you to tell me about yourself in a few sentences so I can build your vault. Now the

[06:40] prerequisite to getting the most leverage out of this skill is again having the CLI installed so you can actually do things programmatically on your behalf. And the four questions it poses to you are very simple. Number one is what do you do for work? Number two,

[06:53] what falls through the cracks the most? What do you wish you tracked better? Do you want this to be work only or personal life as well? Do you have

[07:00] existing files you want to import? Because this last one is important. If you're a business owner or a company owner, you might have 5, 10, 15 sets of PDFs that you want to be able to distill and somehow bring into your second brain. Now, if you want to remove even

[07:14] more friction, then you can ask the following. [music] Can you ask me all of these questions, but in multiplechoice style format using the ask user input tool? And now you will force Claude Code to give you multiple choice questions to make this as simple as possible. And

[07:29] there you go. You get a series of multiple choice questions. The first one I say that I'm a business owner. Then I

[07:34] say that let's say I want to prioritize projects and decisions and then I want to focus on work and personal or you can do a full life OS. You can always type something of your own. If none of these apply then you can say let's say I want to be able to import PDFs, docs, etc.

[07:53] and then send that over. Then we submit all these answers. And now we give it a better picture of what the structure of our vault should look like. Now

[08:02] obviously if you add some more specificity you'll get more results. And in less than 5 seconds you get this drafted version of your vault where the inbox stays the same but everything else here is configurable. So all of these can be changed depending on what makes sense for you. And if you want to be

[08:18] able to install out of the box some slash commands, my skill gives you that option. So if you want to be able to do a slash command daily to get a daily brief of exactly what's going on in your business, in your life, both, then that's an option. You could do slashstandup for a briefing across projects if you are constantly updating them. And this is my favorite that I use

[08:39] every single day, which is called slashtlddr. So this one is for any conversation. So let's say I'm even building something for my community. I'm vibe coding some

[08:48] form of community app and I'm stuck somewhere or I want to be able to brainstorm something. I will go through a conversation. I will end it with /tlddr. It will create a summary of the

[09:00] last next steps and the next step decisions and I'll store that in Obsidian. And in terms of your PDF, slides, and other files, I do have a pretty elegant solution for you because you most likely don't want to store the raw information that's in there to be always checked and referenced by cloud code. Odds are there's a lot of noise and some signal and we want to be able to harness signal. So I'll also show you

[09:23] my way of handling this as well. So now you could say something like build it and then it will go start cooking. Obviously, it's a lot more helpful to have the CLI and the skills because then you can actually give it the hands and the eyes it needs to go and execute this. Now, in my case, I don't want to

[09:38] overwrite my Obsidian. So, I asked it what it would do next in order so you know exactly how it works in case you want to configure what it does. So, the core things I want you to look at here is number two, which is writing the skill files so that you can leverage them. Writing some form of memory,

[09:53] opening the vault on your computer, asking about context injection. So if you want to start a cloud code session and always globally have certain markdown files injected along with any context in your cloud MD, you can maggyver cloud code to do that. So let's say you've done your initial setup, but you want to take things to the next level and take a folder like this of different types of files, whether they're PDFs, annual reports, JSON files, or Excel files, and find a way to bring that signal from these documents into your second brain. How could you go

[10:27] about doing that? Now, there's no one decisive way, but there is a way that I like to do that's pretty shorthand, pretty cheap, and most importantly, fairly scalable. What I prefer to do is take my messy set of files, then feed it to cloud code, tell it to organize it by file type with different subfolders.

[10:45] Once we do that, we can leverage a cheap API with a very large context window, a million context window that can handle those thick annual reports that can be hundreds of pages long to break that down. step one from a PDF with tons of junk metadata to a markdown file. Then take said markdown file, throw it into a prompt from Gemini that says, "Take a look at this document, synthesize all the salient points, and this is where you would want to intervene and say what those salient points might look like."

[11:16] Once it reads it, synthesizes it, and compresses it, then you're going to have a series of clean markdown files that are all cheat sheets of all of these larger files. And once you have that, now you can use the Obsidian CLI skills that I'll show you right now and plug them in. Once you install the skills, you'll be able to use them by just asking for them or actual slash commands. So if I do Obsidian CLI and I

[11:40] just enter this now, contextually Cloud Code knows that whatever I say next is in reference to my CLI. So I'll say something like this. Can you pull up all the folders we have in the vault called Mark's World? just to show you that

[11:54] functionally it can call out to it. And voila, you can see all the folders that you saw before. Now I can say something like, can we create a canvas using the JSON canvas skill to create a walkthrough of how you would take very large PDF documents, break them down using an LLM, let's say a script from Gemini 3 Flash, a new model, you don't know about it, and then break that down into cheat sheets, and then importing that into Obsidian. So basically I'm

[12:21] asking it to create a canvas of the very process that I just walked through right now. Within a few minutes we load the JSON skill successfully. Then it creates the canvas file. Then it plugs it into

[12:32] our Obsidian and it tells us exactly from left to right what it looks like. So if we just take a peek and go into our Obsidian real quick, this is exactly what it looks like. So it goes through from the large PDF documents to PDF chunker script the three flash API and this is pretty much the exact process I told you about and you can also use this as a miro or skeleadraw equivalent. So

[12:55] this is a very powerful setup and with the CLI and the skills then you're ready to take on anything. So this is everything that you need to set up your second brain of your dreams. So you have the CLI, you have the app, you have the skills and you have the beautiful connection to cloud code to make it all happen. And like I promised, I'll make

[13:13] available to you the Obsidian skills I showed you along with a full guide walking through everything I showed you today and my special vault setup skill completely for free in the second link in the description below. But if you want to go much deeper, see a longer form version of this tutorial, and see exactly how I can execute that pipeline in the middle for file conversion and file synthesis, then you're going to want to check out the first link in the description below. I've even created a turnkey way for anyone to be able to install Obsidian and its dependencies just through a terminal experience exclusively for my members. And to the

[13:47] rest of you, if you found this video helpful, if it opened your mind, maybe your second mind on what is possible with Obsidian and Cloud Code, I would beyond appreciate a like and a comment on the video. helps the video, helps the channel, and I'll see you in the next
