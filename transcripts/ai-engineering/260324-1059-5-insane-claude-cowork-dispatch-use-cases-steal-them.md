# 5 Insane Claude Cowork Dispatch Use Cases (Steal Them)

**Channel**: Brock Mesarich | AI for Non Techies
**Duration**: 23:53
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=mnsDx7HDwls
**Transcribed**: 2026-03-24 10:59

---

## Organized Notes

**What Claude Cowork Dispatch Is**

- **Cowork Dispatch** lets you text Claude from your phone and have it run tasks on your computer while you're away — no need to be at your desk
- Available on the **Pro plan ($17/month)** — initially required Max ($100/month) but rolled out to Pro within days of launch
- How it works: text from phone → Cowork runs on your desktop with access to files, folders, browser, and connectors → results appear in both phone chat and desktop app
- Tasks triggered via Dispatch are labeled with a **"dispatch" tag** in the Cowork sidebar for easy identification
- **Limitation**: can't view HTML files or generated dashboards directly on the phone — only a text summary appears in Dispatch; full outputs visible on desktop

**Parallel Agents via Dispatch**

- Can send **multiple tasks simultaneously** from your phone — each runs as an independent parallel agent
- Example: Agent 1 sweeps email inbox, Agent 2 researches video topics, Agent 3 preps for meetings — all running at once
- **Key constraint**: Dispatch is **not fully sequential yet** — tasks must be independent (no agent can depend on another's output)
- Sequential workflows (e.g., "research X, then email the team about findings") aren't supported yet in Dispatch

**Use Case 1: Meeting Prep**

- Skill scans Google Calendar, email history with meeting participants, and Google Drive documents
- Generates a **briefing** with participant backgrounds, action items, talking points, and relevant documents
- Output includes an **HTML dashboard** on desktop with detailed meeting context
- Triggered from phone with a simple "meeting prep" command

**Use Case 2: Inbox Sweep**

- Skill scans Gmail, identifies **unread emails needing action**, and drafts replies automatically
- Found **15 emails** requiring responses in the demo, with drafts saved directly to Gmail
- Generates an **HTML dashboard** showing all actionable emails at a glance with suggested replies
- Triggered with "inbox sweep" from phone

**Use Case 3: Receipt Scanner / Expense Report**

- Upload PDF receipts to a folder on your computer → text "scan my receipts" from phone
- Cowork reads all PDFs, categorizes spending, and generates an **interactive expense report** as an HTML page
- Replaces manual copy-paste-categorize workflow that would take ~45 minutes
- Skills are **editable**: Customize → Skills → find the skill → edit with Claude

**Use Case 4: Quick Research**

- Text a topic from your phone → Cowork scans multiple sources and generates a **clean research report**
- Output: formatted markdown file with topic breakdown, current state, relevance assessment, and sources
- Demo researched "Claude Cowork Dispatch" itself — broke down features, access requirements, and relevance

**Use Case 5: Slack Catch-Up**

- Skill scans all Slack channels, surfaces what matters, provides a **clean summary**, and flags items needing action
- Condenses cluttered Slack channels into digestible briefings
- Requires Slack connected via **Connectors** in Cowork settings

**Connectors and Zapier MCP**

- Cowork has ~**38 built-in connectors**: Gmail, Slack, Canva, GitHub, Bit.ly, and more
- For apps without built-in connectors: use **Zapier MCP** (zapier.com/mcp) to access **8,000+ apps** with **30,000+ actions**
- Zapier MCP setup: create new MCP server → select Claude Cowork → add tools for each app → copy URL → paste as connector in Cowork

**Cowork Dispatch vs. OpenClaw**

- **OpenClaw**: free, open-source, runs locally, supports any LLM, controllable via WhatsApp/Telegram/Slack/Discord, requires DIY setup, community-built skills, user manages everything
- **Dispatch**: included with Claude Pro ($17/month), Claude models only, works out of the box in 30 seconds, no security concerns, integrated with Claude ecosystem
- **Cron jobs vs. scheduled tasks**: OpenClaw uses cron jobs for proactive tasks (e.g., auto-scanning YouTube competitors and messaging you on Telegram). Dispatch uses scheduled tasks but **requires desktop app to be open** — can't run while laptop is closed
- Verdict: **different tools for different people** — Dispatch is ideal for non-technical users who already use Claude; OpenClaw for technical users wanting full control and proactive automation
- Dispatch is currently in **preview/beta** — Anthropic likely building out more proactive features

**Plugin System for Dispatch Skills**

- Brock created a **free plugin** with all 5 skills (meeting prep, inbox sweep, receipt scanner, quick research, Slack catch-up)
- Plugins are **zip files** uploaded via Customize → Browse Plugins → Personal → Upload Plugin
- Each skill is a **markdown file** with instructions on how the task should be performed
- Skills include **trigger phrases** (e.g., "sweep my inbox", "handle my emails") that auto-invoke the skill
- Multiple folders can be selected for Cowork to work across

---

## What This Means for Your Work

Dispatch solves a real friction point you have: you manage 9+ active software projects and OOBC policy work, but you can only trigger Claude Code or Cowork workflows when you're at your desk. Dispatch lets you fire off tasks from your phone — but the practical value depends on which of your workflows can actually run independently without sequential dependencies.

**Your highest-value Dispatch candidates are monitoring and reporting workflows.** The inbox sweep and Slack catch-up patterns map directly to your multi-project management overhead. You could dispatch a "project status sweep" that checks GitHub activity across e-Bangsamoro, MoroMarket, Tarbiyyah-MS, and BangsamoroHR, then surfaces which repos have stale PRs, failing CI, or pending issues — all from your phone while commuting to OOBC.

**The receipt scanner pattern generalizes to BARMM document processing.** Your OOBC policy work involves reviewing PDFs (BAAs, resolutions, committee reports). A Dispatch-triggered "scan new PDFs" skill could read newly uploaded documents in a folder, extract key provisions, and generate a summary dashboard — similar to how the receipt scanner works but for legislative documents. This extends your existing /transcriber skill to a mobile-triggered workflow.

**The sequential task limitation is significant for your work.** Most of your valuable workflows are sequential: /bangsamoro → /bill-drafter → /fact-checker, or /research-pipeline → /expert-builder → /skill-optimizer. These can't run as Dispatch tasks yet because each step depends on the previous output. Until Dispatch supports chained tasks, your Claude Code CLI workflows remain more powerful for these multi-step pipelines.

**The desktop-must-be-open constraint limits scheduled task adoption.** Your earlier interest in scheduled tasks for BARMM legislative monitoring (from the Cowork Five Levels video) is tempered by this — if your MacBook sleeps, scheduled tasks don't run. OpenClaw's cron job approach is more reliable for truly autonomous monitoring, but requires setup you may not want to maintain as a solo dev.

**Concrete next steps:**
- Build a "project pulse" Dispatch skill that checks GitHub activity across your 9+ repos and surfaces what needs attention — testable immediately from your phone
- Create a "BARMM document scanner" skill for processing new PDFs in your ~/PDFs/ folder — triggered via Dispatch when you receive new committee assignments
- Monitor Dispatch's evolution toward sequential task support — once available, your /bangsamoro → /bill-drafter pipeline becomes phone-triggerable
- Evaluate OpenClaw for the proactive monitoring use case (auto-scanning for new BAAs or BTA agenda items) since Dispatch can't do cron jobs without the desktop open

### How This Can Improve Your Claude Skills and Workflows

**The plugin-as-zip distribution pattern complements your skills-bucket architecture.** Your ~/apps/skills-bucket/ repo stores 50+ portable skills as markdown files. Dispatch plugins are essentially the same thing — markdown skills bundled as zip files for non-CLI users. You could add a `/plugin-packager` step to your /gitops workflow that automatically zips skills-bucket skills into Cowork-compatible plugins. This gives OOBC team members, MoroTech trainers, and Bangsamoro Scholars Association colleagues access to your /bill-drafter, /legislative-briefer, and /training-assistant skills through Cowork's GUI without touching Claude Code.

**The "inbox sweep" pattern suggests a /project-sweep skill.** You don't have a skill that aggregates status across multiple GitHub repos. Your /devwork handles single-feature development, /gitops handles single-repo commits, and /session-summary captures what happened in one session. But nothing sweeps across e-Bangsamoro, MoroMarket, Tarbiyyah-MS, BangsamoroHR, SBP, OBCMS, and IPP simultaneously. A /project-sweep skill could check each repo's GitHub activity (PRs, issues, CI status), compare against /context session notes in the vault, and surface what's stale or blocked. Check ~/Vault/Claude-Skills/index.md — no equivalent exists.

**The receipt scanner workflow maps to /financial-analyst enhancements.** Your /financial-analyst skill handles budget analysis and fiscal performance, but it requires manual input. The Dispatch pattern of "drop PDFs in a folder, trigger from phone" could extend /financial-analyst to automatically process BARMM budget execution reports, appropriation documents, or OOBC fund utilization reports from PDFs. Combined with /transcriber (PDF OCR), this becomes: PDF → OCR extraction → financial analysis → dashboard output — all phone-triggered.

**The quick research skill is a simplified /research-pipeline.** Your /research-pipeline combines NotebookLM + sub-agent validation + vault storage — far more rigorous than the single-source "quick research" shown in the video. But the Dispatch trigger pattern is worth adopting: a lightweight `/quick-scan` variant of /research-pipeline that skips NotebookLM and validation, just does a fast web search and summary, optimized for mobile dispatch when you need a quick answer rather than a comprehensive report. Your /deep-research is the heavy artillery; this would be the sidearm.

**Cross-pollination with Parliamentarian.** The meeting prep skill (calendar + email + Drive + participant research) maps directly to what the Parliamentarian platform could do for MPs. A "committee hearing prep" Dispatch skill could pull the committee agenda from e-Bangsamoro's parliamentary portal, research the bill/resolution on the agenda using /legal-assistant, draft talking points via /speech-writer, and surface relevant BAA precedents via /bangsamoro — all triggered by an MP's staff member texting "prep for committee hearing" from their phone. This turns Parliamentarian from a desktop tool into a mobile-accessible legislative support system.

---

## Transcript

[00:00] You can finally use Claude co-work from your phone. I've been testing the new co-work dispatch since the day it dropped, and this one feature changes how I use Co-work completely. You can text Claude a task from your phone, and it runs on your computer while you're away. It can do any work on your

[00:16] computer for you. So, in this video, I'm going to show you five insanely practical use cases you can steal from me, and I'm going to give them away for free. And then I'm even going to break down if this is the true open claw killer that everybody's talking about.

[00:28] So, let's get into it. All right, so Claude just dropped co-work dispatch. And this honestly changes everything if you are a power claude or claude co-work user. Co-work is extremely powerful. It

[00:37] could read your files. It could send your emails, search the web, build documents, and basically do a bunch of different things on your computer. It's an amazing alternative to use some of the power of Claude code, but for completely non-technical people. And I

[00:51] honestly think about 99% of people that want to use AI should use this instead of cloud code. But there was one really big problem that we've had inside of Claude Co-work up until this point. That is that you had to be chained to your desk sitting at your computer to use it.

[01:05] So I got stuck so many times just because I had to be there for it to actually do this stuff for me. If it finished a task and I was like at the gym or at dinner or something, I couldn't do anything about it. We did not have any mobile access. So if we

[01:18] were out of the house, we could not use this at all. But what if we could use Claude Co-work from our phone and basically text it from anywhere we're at and have it do work for us? So that's exactly what Co-work Dispatch is. So let

[01:30] me talk about a bit more what it is before I show you some key use cases you could use right now that honestly have been changing the game for me. There's basically this handy little button inside of Claude on my phone now that says dispatch and I could basically pull this up and run tasks to co-work to perform tasks on my computer while I'm away doing anything. So, let's quickly break down how it works very, very simply cuz it really is pretty simple.

[01:54] So, all you have to do is text Claude from our phone here. Co-work is then running on your computer so it could access your files, your folders, and you know, even use browser use. So, it could go off and click and fill out forms for you and whatnot. And it connects to all

[02:07] the different apps you use via their connectors feature. And then we basically just come back to results either inside of Claude Co-work or you could just see a watered down version of what it did directly in the chat. So, one thing that really makes this very impactful and useful for everyday people is that you could run multiple tasks at once. So, for example, I could send

[02:27] three or five or even 10 different tasks from my phone while I'm at the gym. We then have parallel agents that are off performing each of these individual tasks for me. So, for example, I could have agent one sweeping my email inbox since it has access to my Gmail account via the connectors feature. Agent two

[02:43] could be researching OpenClaw and coming up with different ideas for my videos, using specific skills I have in there. And agent three could be prepping me for my meetings that I have later in the day. All of these different tasks are running at the exact same time without me needing to be at my computer. But

[02:57] there's one key thing that we need to talk about right now, and that is that co-work dispatch is not fully parallel yet. So let me break down exactly what this means. Each agent has to run independently. So if I go back to this

[03:09] last slide, each of these are different tasks that aren't relying on the other agent for specific information. All right? So some tasks need to go one at a time. For example, working in parallel,

[03:19] you could have multiple different tasks, whether that's researching something, sweeping your email inbox, and it's using different apps, different data, and no tasks depend on one another. It's not like waiting for one step to finish to then go off to the next task. But some tasks that you give AI agents have more sequential steps that it needs to go through. So, for example, it could

[03:37] research X, then email the team about what it found. But the problem with this is that the output from the email to the team is dependent on the researching step. We're not able to do this yet inside of Co-work Dispatch, but we're on the right track here. Tons of people are

[03:51] calling this the open claw killer, and I'm going to break down my thoughts on this later in the video, compare the two, basically break down what you should be using for specific tasks, and if it really is the co-worker, and my answer probably is going to surprise you. All right, enough of me yapping about this. So, let me show you Claude Co-work Dispatch in action and show you exactly how you can begin setting this up in just a couple of simple prompts, no matter how technical or nontechnical you are. So, first of all, we're going

[04:15] to come to this web page here that Claude gives us. There's going to be a link in the description for you to download the Claude desktop app. So, if you haven't already, go ahead, download it for Mac or Windows, whatever you're using, as well as download this on your phone, whether you're using an iPhone or an Android. And your next question is

[04:31] probably like, Brock, do I have to be a paid user or how much do I have to pay to use the new co-work dispatch mode? And let me break it down very simply. So, you need to be on the pro plan, which is their $17 per month plan. You

[04:43] don't need to be on the max plan. The day that this released a couple of days ago when I made my first video about this, you did have to be a paying user on the $100 per month plan. However, it's been rolled out to the pro users.

[04:53] So, if you are on the $17 per month plan, you should have access to this, no problem. All right. So once we have the claude desktop app downloaded, we are going to see this interface here. If

[05:03] you've never used claude before, let me just break down very simply. We have our chat mode which is basically like using chatbt, we could basically, you know, interact with claude to ask it questions and it could, you know, give us responses and give us certain outputs. However, it can't actually go and perform different tasks for us. That is

[05:17] where co-work comes in handy here. So there is this little co-work tab up here and then from here you're going to see all of our tasks that we've done inside of co-work. And I'm going to click on new task here. And from here, what I'm

[05:28] going to do is I'm going to select a specific folder. So, I have a folder called Claude Co-work Short System, which is basically the project I have in order to help me with short form content. So, what I suggest you do is you create a new folder here. So, I'm

[05:41] just going to choose a different folder. And this will pull up any of the different folders that you have on your desktop. I'm just going to select new folder. I'm going to call this co-work

[05:48] dispatch just for the sake of this video. I'm going to create that, open it, and I'm going to click allow so that we could go edit the different files in there, add things to it, and whatnot. And a key thing I want to mention is inside of co-work, we now have a new feature where you could select multiple different folders that you want to interact with. So, if you have a co-work

[06:05] dispatch folder and a documents folder that you basically want to perform different tasks in, you could select both of those. Now, I'm just going to unselect this one. I'm going to select co-work dispatch. So, now we can begin,

[06:15] you know, interacting with co-work. All right. So, here is co-work in action directly inside of the desktop app. This

[06:20] is not using dispatch yet. I'm going to get to that and then show you the five use cases that you could begin using right now with that. You could see that I said slideshow and then co-work dispatch. And then if I scroll down, it

[06:32] generated this HTML site for me. This probably looks familiar. This is basically a slideshow presentation that Co-work created for me about what Co-work Dispatch is. And this is a skill

[06:42] that I use every single day that has been incredibly helpful for helping me explain different things for YouTube videos. If I come up to customize and go to skills, you could see that I have this slide skill which is a very comprehensive markdown file here. Basically just with a set of instructions breaking down exactly how I want my slides to look for presentations and videos. So you're probably like

[07:02] asking like Brock, why are you even showing this to me right now? The reason I wanted to show you this is because before dispatch, I had to be on my computer asking Claude Co-work to do this for it to actually spin up this presentation for me. But now I could just do this directly from my phone if I'm driving. Probably not driving cuz

[07:19] probably shouldn't text and drive, but I could literally be doing anything if I have my phone. Basically text Claude and it could go ahead and spin up this presentation for me using the Claude skill that I have in Co-work. All right, so Co-works on plugins. If you don't

[07:32] know what plugins are, they're basically bundles of specific skills, tools, connectors, and workflows inside of Co-work. I actually built a plugin with five different skills and use cases for Co-work Dispatch that you could download right now for free and start running inside of Co-work. So, let me show you exactly how to install this plugin and then I'm going to show you the five use cases that you could begin using this for. All right, so in order to install

[07:56] this plugin, there's going to be a link in the description. and it's completely free to actually access this via Google Drive. There is this plug-in zip file here as well as this PDF guide inside of this folder. This is basically just like

[08:08] a document breaking down step by step exactly how to do this if you prefer to, you know, basically just read through this to make sure you're setting it up properly instead of having to, you know, listen to me talk about this. So, this is a resource that I crafted for you guys for free to help you guys set this up even though it's very simple. So, I could just click on this. What I'm going

[08:25] to do is I'm going to download this zip file. Don't unzip this file because when we upload it to co-work, it needs to be zipped. This is the specific format that Co-work basically makes us use in order to upload these. So, now that I have

[08:37] this downloaded, I'm going to come over to Co-work. I'm going to click on customize. And from here, we're going to see this little personal plugins thing here. Once we click on customize, we're

[08:47] going to click on browse plugins. There's a bunch of different plugins that are, you know, created by Anthropic that we could add or I could hit personal and then just upload my own here. So, I'm just going to click plus.

[08:57] I'm going to go to the bottom one that says upload plugin. From here, I'm going to take that exact zip file that I had. Basically, just drag it in here. I'm

[09:04] going to click on upload. I already have this downloaded, but it will just say upload. And it will take like 2 seconds and it will be inside of your co-work account. Now, in order to see if this

[09:13] was actually uploaded, you are going to come to personal plugins and it's going to be called five co-work skills as you could see here. And inside of the plugin, we have a couple of different things. We have five different skills here. here. And if I open these up, you

[09:26] can see I have one called inbox sweep. And these are basically just markdown files with different sets of instructions on how we want this task to be performed. And if I read the description, it basically says, "Use this skill whenever the user says sweep my inbox, draft replies, handle my emails." Basically, anything email

[09:42] related will trigger this skill or specific set. Let's move on to the five different use cases now. So, you've probably ran into the issue of walking into a meeting unprepared. probably

[09:51] don't know who the person is, what you guys talked about last time, and what exactly you need to talk about on the call. So, we have this meeting prep skill here that will automatically pull from your calendar, look at your email history with this specific person, pull relevant Google Drive documents in order to give you a brief on who this person is and what the meeting is about. And the best part is we could just text from our phone via Claude Dispatch and this entire workflow can be triggered for us.

[10:16] All right, so I have my phone pulled up as you could probably see on screen. And I'm going to click on the Claude app. And inside of Claude, you could see on the lefth hand side, we have chat, we have projects, we have artifacts, we have code, and we now have this handy dispatch button here. And if I come into

[10:31] this thread and if I look inside of this chat, you could see a specific thread here. This is basically where I'm texting co-work from my phone and having it go ahead and, you know, perform these different tasks for me. So, for example, I just typed in inbox sweep since that is the skill that I showed you to download. And then it said on it

[10:48] sweeping your inbox now. And it basically found 15 different emails that I have not responded to to that need to action. And all the drafts are saved inside of Gmail. So it literally read

[10:58] through my email inbox, found the ones that are urgent for me to reply to and even drafted those email responses for me just by me texting it from my phone. And if I come back to co-work on my desktop, you could see we have this exact same interface that we have on my phone here. So basically we have my message inbox sweep. you know, it went

[11:16] through and found all these emails for me. Same exact message that I received here. So, if we want to see everything that Co-work Dispatch is up to from our phone, we could see all this inside of the Co-work app, you know, on our desktop. And another key thing I want to

[11:28] mention here is on the left hand side where it shows our recent tasks, it shows dispatch here with this little label to signify that this was actually triggered from dispatch on my phone. And if I pull this up, this is that exact task for the email inbox sweep that I just had it run. And it looks a bit more detailed here. And it even generated

[11:48] this HTML dashboard for me because this is inside of that skill that I gave you guys. It will automatically scour your email inbox and then generate this like dashboard for you to see everything in this very easy to look at user interface. So I could see all the emails that I need to respond to, things to reply to soon, all these things.

[12:06] However, the reason I even mention this is we can't see this directly inside of Dispatch on our phone. That is because this is an HTML file that is downloaded onto my desktop. So there's no way for me to see that. However, we did get a

[12:18] brief explaining, you know, all the key findings from my emails inside of Dispatch. All right, so moving on to use case number two for Co-work Dispatch. You probably have a bunch of different unread emails that you're procrastinating just like me. I probably

[12:31] have hundreds at this point. So, I created this skill that is called inbox sweep that will automatically scan my Gmail, find what specific emails need replies to, and it will even draft those responses for me. And on top of that, it will generate a dashboard that I could see every single email at a glance that I need to reply to, as well as specific replies that I could actually give those emails. So, let me show you this in

[12:54] action right now. And I'm going to trigger it via dispatch. All right. So,

[12:57] as you can see, both on my phone as well as on the desktop app here, I gave the command meeting prep and it just said on it checking your calendar for what's coming up. So, it's actually going off and performing this task right now. It doesn't really look like it's doing much. So, if you want to see exactly

[13:12] what Dispatch is doing while it's performing these tasks for you, you could come up here, click on dispatch, and click on see background tasks. And from here, you can see that it's reading the transcript of specific meetings and, you know, going through this process here. And I actually just got a notification on my phone. So, let me

[13:29] come back to dispatch and we should be able to see this. All right. And just like that, it scoured my Google calendar. Basically said, my next

[13:35] meeting is the AI Mafia meeting. Shout out to the boys. Wednesday, 7:00 a.m.

[13:39] Mountain time. Looks like I have an action item. As well as it's breaking down a specific thread about our Cape Town event that we just threw, you know, about a month ago. So, it basically

[13:47] broke down all the different things that we talked about meetings. It was actually able to transcribe our meeting and then come to me with this information. Then if I come back to my recent tasks on desktop, you can see that I now have this meeting prep HTML thing here. So this is the real meat of

[14:02] this workflow. I know right now like the meeting prep command or skill isn't necessarily that insane when you see it on your phone like this, but say you're on the go and you don't have your computer with you and you wanted to go off and spin up this dashboard for you after performing, you know, a scour of your calendar, it could go ahead and do that. And then once you get back on your computer, you could see that it's labeled as dispatch. You could click on

[14:24] it and see any of the specific outputs from that workflow you invoked inside of dispatch. And if I scroll down just to show you a bit about what I mean about how this is a bit more in depth inside of this dashboard, it breaks down each of the people that are in this meeting with the background on them, context to know about, basically shows my action items, then even references the relevant documents as well as specific talking points. It said that I should give my six-month update on Loom, my agency, YouTube, and school. That is actually

[14:50] pretty cool. All right, so use case number three is something that is personally useful for me. So let's say that we have a specific folder on our computer that is full of different PDF receipts and I want to be able to turn this into an expense report so I could see exactly what I've been spending my money on. So basically I could

[15:07] understand what I need to cut back on. So before I would have had to open up this PDF, copy each individual amount, paste it into a spreadsheet and categorize this manually and I basically have probably like 45 minutes gone. Right now inside of co-work dispatch, all I have to do is from my phone text co-work dispatch and just say scan my receipts and give me an expense report.

[15:27] All right, so I triggered this from my phone via dispatch and then from there it went off and you know performed this task. I could click on this recent task here inside of co-work. And if I want, I could look at this exact, you know, prompt that it gave, which is basically this prompt that was initiated from the skill that we have set up for this. And

[15:44] I could go through each of these different steps if I really wanted to. But all I really care about is this end result here. Basically broke down the total spend, showed the receipts here, as well as it generated this expense report that I could view right here.

[15:56] This is this is pretty amazing if you think about it. We could literally just upload our receipts to a folder on our computer. And then we could have Claude automatically generate this expense report, break down spending by category, specific timeline, biggest expenses, all the receipts here, everything, and turn that into like an interactive web page for me, all by triggering this from my phone. And one thing I do want to

[16:17] mention is if you want to change how that skill works or say you don't like the way the output looks, you could just come over to customize, click on skills, then find the receipt scanner skill, and then from here you could click the three dots, click on edit with claude, and then basically just make any changes to this that we wish. So you could perfect this to your liking. All right. So this

[16:37] next use case I'm going to show you is something that is very useful for me in particular. For me personally, I will see an AI news headline and I need to understand it fast so I could cover on the channel as well as test it out myself. So, I created this skill that is called quick research that will scan multiple sources and then generate a clean report for me automatically from my phone. So, I could essentially just

[16:59] text a specific topic and then get a full briefing back from co-work via dispatch. All right, so again, all I said was quick research. Claude co-work dispatch. So, it ran this skill and it

[17:11] went off and did the research for me. It broke down dispatch, explained why it's relevant for my audience, broke down the current state as well as specific access. And as you can see here at the bottom, it says full report is in the file card above with sources, which I actually cannot click inside of Dispatch. And I will say this is one

[17:27] thing that's holding it back right now, the fact that I can't really see, you know, the specific interfaces that I generate or the documents I create inside of Dispatch. But if I go to my desktop, you could see on the lefth hand side that I do have this dispatch task here with that label. And then it actually spits out this markdown file, which is a formatted document breaking down everything about Claude Co-work Dispatch. And I could basically do this

[17:52] for anything that I want to research. And you could do the exact same thing since you have access to this via the plugin I shared for free. All right, so moving on to the last use case I'm going to show you before going ahead and showing you the key differences between this and open claw to see which you should be using. So we probably all have

[18:10] a bunch of different unread Slack messages that we haven't got to or that we're procrastinating. I know this is the case for me right now. So I built a Slack catchup skill that scans all of my channels, finds what actually matters, gives me a clean summary, and basically flags anything that needs. So it's very

[18:28] simple. It'll just basically take my cluttered Slack channels and condense this information that will be easy for me to digest. So, due to the fact that I have some sensitive information inside of my Slack channels across my different companies, I'm not going to show you the exact output that I got. But what I am

[18:43] going to show you now is how to actually add something like Slack or Gmail to Claude Co-work so that way Dispatch can perform tasks across those different applications. If you don't know, there is something inside of Claude called connectors. And this is basically the way that we could connect Claude to our different applications so it could perform tasks across those different tools. So for example, I have Gmail set

[19:05] up. I have Bit.ly. I have Canva, GitHub,

[19:07] and I even have Slack obviously for that previous skill. There are about 38 different apps that you could connect to inside of Claude. But if there's a specific app that you cannot connect to, I'm going to show you a hack right now that could basically solve that problem for you. So personally, I like to use

[19:22] something called Zap Your MCP. It connects to 8,000 different apps along with 30,000 plus different actions across those apps. So, if you want to sign up and start using this, there's a link in the description and I'm going to show you very simply how we could actually add this. I'm going to click on

[19:36] start building. From here, I'm going to click on new MCP server and I'm just going to select Claude Co-work. And once that is selected, I'm going to see a couple of different things. So, I see

[19:46] that my client is Claude and then I have different tools here that I personally have configured before this video. But if you want to add specific tools for apps that you want to connect to, you can come here and search for any of the different apps you use. So for example, I want to connect to school. So I just

[20:01] click on this. I select all the different tools I actually want access to. Looks like there's only two inside of school. I can now invite members and

[20:08] unlock course for members via Claude. So I just select all the tools I want to use. And then from there, I'm going to come to the connect tab. There's going

[20:15] to be a URL for us to copy. I'm going to come back into co-work. I'm just going to look for a specific connector called Zapier. And all I'm going to do is paste

[20:24] in that URL that I got from the Zapier MCP. And then we will have access to all the different apps inside of this MCP server. So if I click on Zapier, you can now see I have access to Google Docs, Google Drive, School, all these different platforms directly inside of this MCP server. And then I could just

[20:40] basically select this right here to always allow Plaude to perform tasks across those apps. All right, guys. So let's talk about now the key differences between Claude Co-work Dispatch and OpenClaw. So OpenClaw has obviously been

[20:54] taking the world by storm recently. So what is OpenClaw? It's a free open-source AI agent that runs locally on your computer that you can control from WhatsApp, Telegram, Slack, or even Discord or any of those messaging apps that you use. And Dispatch is what I

[21:09] just showed you. It's built into the cloud app, runs on your desktop with your files, connects to your apps and plugins. There's zero setup and it is connected to your entire Claude ecosystem. So the key big differences

[21:20] here is that OpenClaw is free and open- source. You could use any large language model you want. So you're not bound to just using Claude. A DIY setup is

[21:29] required which can be a bit difficult if you're non-technical. There's community-built skills and you have to manage everything. Whereas Dispatch is included with the Claude Pro plan. You

[21:39] could only use the Claude large. You could only use the Clawad LLM such as Claude 4.6 Sonnet or Claude 4.6 Opus

[21:47] or any of the models that come out in the future. But a key thing with dispatch is it works right out of the box. It takes maybe 30 seconds to set up and you don't have to worry about security issues. Moving on, we need to

[21:58] talk about a crucial thing here that is cron jobs versus scheduled tasks. OpenClaw uses cron jobs which basically allows it to go off and perform tasks for you at specific times or do things proactively. So, think of this as something like scanning YouTube competitor videos and then once somebody posts a video that is interesting, it could then automatically message me on Telegram and say, "Hey, Brock, there is this new video idea for you that I just scoured from YouTube. Looks like it's

[22:23] getting traction. Make a video about it." It could go ahead and do that.

[22:26] Whereas, Dispatch can't really do that. There is something called scheduled tasks that allows you to actually set up specific workflows that use different skills. For example, this morning briefing skill I have that runs every morning at 7 a.m. which basically, you

[22:39] know, has this skill, this set of instructions that will send me a Slack message and create a dashboard for for me to see basically my entire morning with all the emails I need to respond to, what's on my Google calendar, etc. But a key problem with that is that my desktop app needs to be open. If I have my computer closed while I'm sleeping, this can't actually run while I'm not on my computer. So, the question that

[22:59] everybody is asking is dispatch and open claw killer. I think these are two completely different tools for different people, but for non-technical users, I genuinely do think dispatch is probably all that you need as of right now. I will say that I could imagine Anthropic is building out some feature that allows you to text co-work over Telegram, have it go and be more proactive with something like cron jobs. But right now,

[23:21] it does feel like a beta product, which it actually is. It's in preview mode, but it is really promising if you already use Claude and you want to be able to use co-work on the go. So guys, hope you got some value from this video.

[23:33] Leave a like, subscribe to this channel for more content, and if you want to stay up to date with these different AI releases, as well as how I'm personally using them, you can join my school community. There is a link in the description to do that, as well as there is a free link to the plugins that I showed in this video for you to download. So, thank you for staying to the end. I appreciate every single one

[23:50] of you guys and I'll see you guys in the next
