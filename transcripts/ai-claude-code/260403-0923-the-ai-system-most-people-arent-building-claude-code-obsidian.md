# The AI System Most People Aren’t Building (Claude Code + Obsidian)

**Channel**: Rick Mulready
**Duration**: 15:33
**Language**: en (manual) [yt-dlp subtitles]
**URL**: https://youtube.com/watch?v=2COkMJPHINY
**Transcribed**: 2026-04-03 09:23

---

## Organized Notes

**The "AI Chief of Staff" Concept**

- A system designed to solve the problem of **disconnected business tools** (Slack, email, calendar, task managers) that don't "know" your business.
- Not a new standalone app, but a **three-layer architecture** using Obsidian for knowledge, Claude Skills for logic, and Claude Code for execution.
- Goal: Create an AI that is **customized to your specific workflows**, business context, team, and goals.

**The Three-Layer Architecture**

1.  **Layer 1: Obsidian (Knowledge / Memory)**
    - All business knowledge lives in **Markdown files**, which play best with AI as a universal file format.
    - Becomes the **AI's persistent memory** for the business.
2.  **Layer 2: Claude Skills (Thinking / Rules)**
    - Reusable instructions (slash commands) that define **how Claude approaches tasks**.
    - Ensures consistency so you don't have to **re-explain the thinking pattern** every time.
3.  **Layer 3: Claude Code (Execution)**
    - Runs inside **VS Code** and has the power to read, write, and search the entire Obsidian vault.
    - Connects to external tools like **Google Calendar, Slack, and email** for cross-platform execution.

**System Infrastructure and Design Decisions**

- **Control Separation**: A critical design decision between **User-owned space** (Daily Notes for messy brain dumps) and **AI-owned space** (Daily Plan for structured briefings).
- **Metadata Structure**: Using **Front Matter (YAML)** at the top of files (type, status, due date, priority) to make the vault easily searchable for both humans and AI.
- **Folders for Context**: Specialized folders for **Tasks, Projects, Ideas, People, and a Quick Capture Inbox** provide a clean taxonomy for the AI to navigate.
- **The Central Dashboard**: An Obsidian page that automatically pulls in calendar events, pending Slack DMs, unread emails, and daily tasks into a **single bird's-eye view**.

**The Daily Flywheel Workflow**

1.  **The Morning Briefing (`/today`)**: Scans calendar and communications to write a structured **Daily Plan** markdown file and refresh the dashboard.
2.  **Midday Messy Operations (`/process-inbox`)**: User brain-dumps link-free, unformatted thoughts into a daily note; Claude sorts them into the correct **Task or Idea** files later.
3.  **Midday Communication**: Sending **Slack replies directly from Claude Code** and using `/follow-up` commands to see who is waiting on a response.
4.  **The Evening Flywheel (`/daily-review`)**: Claude compares the morning plan against actual activity, updates task statuses, and **notes current project states**.
5.  **Compounding Intelligence**: Each review makes the next morning's briefing smarter because the AI is reading the **notes of previous progress**.

**Tool Comparison and Philosophy**

- **Self-Hosting vs. SaaS**: Unlike Notion AI, this system is **vendor-independent**. Files live locally, and the logic is fully customizable.
- **Tool Consolidation**: Aims to reduce the "mental tax" of switching between seven tools to just two (**Obsidian + Claude Code**).
- **Execution Consistency**: Focuses on the **behavioral habit** of using the system rather than just building the technology.

---

## What This Means for Your Work

As someone who already operates a high-complexity **129-skill system** with an Obsidian vault as persistent memory, the "AI Chief of Staff" paradigm validates your existing architecture while offering a major workflow upgrade centered on **closed-loop feedback**.

Your work with **e-Bangsamoro** and **OOBC policy development** involves fragmented inputs: Ministerial requests, BTA resolutions, legislative drafts, and ministerial coordination. Implementing the **"Evening Flywheel"** would allow you to capture the "current state" of complex bills or features before ending a session, which would then feed a **high-fidelity morning briefing** the next day. This moves your vault from a static archive to a **dynamic operations center**.

For **MoroTech** and **OOBC**, using Claude Code to manage **multi-platform communications** (Slack, email) via commands like `/follow-up` or `/reply` would solve your "solo developer overhead" by keeping you within the VS Code environment while managing institutional relationships.

### How This Can Improve Your Claude Skills and Workflows

-   **Skill Upgrade — `/session-summary`**: You can transform your `session-summary` skill from a simple "log generator" into a **"Strategic Review"** tool that explicitly updates the state of active projects in a way that feeds tomorrow's `/today` briefing.
-   **New Skill Opportunity — `/briefing`**: Develop a master `/briefing` or `/today` skill (integrated with your **NotebookLM** and **Deep Research** outputs) that reads your `daily/` notes and active `projects/` to generate a structured 4-portal briefing for your e-Bangsamoro portals.
-   **Workflow Refinement — The "Messy Middle"**: Your current workflow is very structured. Adopting the **"Quick Capture → `/process-inbox`"** pattern would allow you to brain-dump legislative ideas or feature bugs during meetings without breaking your deep-work flow, letting Claude handle the "sorting" legwork later.
-   **Knowledge Area Integration**: This transcript directly improves your **`ai-engineering`** and **`ai-claude-code`** knowledge areas, providing a blueprint for building a "Chief of Staff" layer over your existing **Parliamentarian** and **OBCMS** development workflows.

---

## Transcript

[00:00] Most business owners are using multiple tools like Slack, email, calendar, task manager, maybe a project management tool. But the problem is none of the tools talk to each other. None of them actually know your business.

[00:11] But there's a system that changes that and almost nobody's building it. It's not a new app. It's not another AI chatbot. It's two tools, Claude Code and Obsidian connected in a way that turns your notes and your brain dumps and your ideas into an AI that knows your entire business.

[00:23] I built it. I call it my AI chief of staff. And every morning it briefs me on my whole business, my calendar, Slack, email, tasks, projects with just one command.

[00:30] So in this video, I'm going to show you why this system is so powerful, how it works, and how to build your own.

[00:49] I built an app for that inside my AI Playbook membership community, and it's called your zone of genius app. In the app, you get a complete AI team that takes care of everything in your business that isn't in your zone of genius.

[01:12] All right, let's get into the AI system that most people aren't building. And this system has three layers to it. And the first layer is Obsidian. This is where all the knowledge lives.

[01:20] Obsidian is just an organizational tool based on markdown files. And you can have folders and files and so forth in Obsidian. Markdown files are essentially a universal file format that plays really well with AI.

[01:31] It's basically the language that AI reads the best. Not PDFs, not Google Docs, plain text markdown. So, Obsidian becomes essentially Claude's memory of your business.

[01:42] Now, the second layer in this system is Claude skills, which are reusable instructions that you've written once that tell Claude how to do a specific task or job. And the skills are set up as slash commands.

[01:57] For example, when I type in forward slash today, Claude isn't just improvising. It's following a specific skill that that slash command triggers. The skill has the rules, the structure, what to pull from, what tools to use, what to write, etc.

[02:15] The third layer in this system is Claude Code which I run inside of VS Code. This is where the work actually happens. Claude Code can read, write, search every file in my Obsidian Vault. It can create new things in there.

[02:38] It connects to my Google calendar, my Slack, my email, and whatever other tool that I want it to connect to. Obsidian is the knowledge. Skills are the thinking, the way you get something done the same way every single time. And cloud code is the execution.

[02:48] That's the system. And when these three layers are connected intentionally, you get something that no single tool gives you. An AI that is custom to how you work, your workflows, your specific business.

[03:11] Now, how much control you get from this system comes down to really two decisions. The first decision you want to make is about knowledge. What Claude should know versus what Claude shouldn't touch.

[03:22] In my system, I have folders for tasks, projects, ideas, content, people I work with, and a quick capture inbox. Claude reads and writes to all of those. But I also have daily notes.

[03:36] Daily notes are my space. I don't let Claude touch my daily notes. That's where I'm brain dumping. These are my messy thoughts. These are screenshots I grab.

[03:45] But then I have daily plans. And the daily plan is something that Claude writes to. This is where Claude takes all the things that are ongoing in my business, my calendar, my tasks, Slack messages, and puts them into a structured daily plan page.

[04:19] Now, the second decision that you're going to want to make is about the thinking layer. What you create Claude skills for versus what you bring in at the moment. Claude skills define how Claude approaches a task every single time without you having to reexplain everything each time.

[04:44] Let me show you what I actually built here. So, what I did is I built a chief of staff system, and I want to walk you through what's actually inside it. I created a specific structure in Obsidian. Well, I actually had Claude Code do that.

[05:02] I created folders and files for tasks, projects, ideas, again, daily notes. Quick credit here, by the way. I saw how this guy **Brad** over at **Brad AI and Automation** YouTube channel structured it. I looked at his approach, made it my own, and the simplicity of it really, really works.

[05:13] I also set up what's called front matter at the top of files. For example, this is a task page here in Obsidian, and it's essentially like fields in notion. Due date, tags, priority, created, recurring, etc.

[05:28] This front matter is exactly what makes everything super easy to search both for me and for cloud code inside of Obsidian. Now, I also create a dashboard here in Obsidian. This is my default page when I go into Obsidian.

[05:39] This dashboard is showing me everything I've got going on in my business. It's pulling in from my calendar. It's pulling in from Slack. It's pulling in from my emails. It's reviewing what's in my day notes. It's creating a day page for me.

[05:55] It tells me what I have coming up this week. Also, it gives me a list of everything that I have from a task perspective. And then this is where it's capturing my ideas.

[06:30] Now, let me show you how I actually use this system day-to-day. The first scenario is the morning briefing. I open up Obsidian. The dashboard is going to load automatically. Then I open Cloud Code inside of VS Code, and I just type in forward/today.

[06:53] The today's skill that I've created pulls in from my calendar, scans my Slack DMs and Slack channels, checks my email, finds tasks that are due, and it's going to write a daily briefing for me which gets saved as my daily plan page.

[07:48] One command here in cloud code, full picture of my business set right here in Obsidian. Midday operation. The morning one is the clean version. Let me show you the messy version.

[08:04] Throughout the day, I brain dump into my daily note or my capture inbox. I don't worry about formatting. I just get it out of my head. Then I run one of my slash commands, a skill called process inbox.

[08:40] It scans the inbox sources. It takes my brain dumps and sorting that into tasks, into ideas, into people, and assigning it to people. It's going to ask me before anything that it doesn't quite know what to do with.

[09:27] Let's say I have a new task that I want to assign to somebody on my team. I can use one of the other Claude skills called `/new`. `/new follow up with Kelly about community report`.

[09:45] It checks first if **Kelly** has an existing people file. Then it asks when I need to follow up. Submit the answer. And just like that, it's created a task for me.

[10:13] It gives me the type (task), status (open), due date, tag, priority, and links back to the person Kelly in my people folder. I didn't create these pages. Claude Code created them because I explained the skills for the system.

[12:31] For the third scenario, the end of the day recap, what I call the flywheel. I created a Claude skill called `/daily-review`. Claude compares what I planned that morning compared to what I actually did.

[12:46] It updates task statuses. It gives me a picture of where things actually landed. This is where the flywheel really kicks in because the next time that Claude works on that project, it just reads those notes so it knows exactly where we are.

[14:00] Tomorrow morning when I type in the slash command today again, the briefing will be better. The plan's going to be sharper because it continues to build on each other. The system just keeps getting smarter and smarter.

[14:24] The more I add to Obsidian, the smarter the overall chief of staff system is getting. It allows me to go from using seven different tools down to just two. Obsidian and Claude Code.

[17:02] That's the system and it's not complicated to build. The real work is using it consistently. I run my entire business now through Claude Code here in VS Code and Obsidian.
