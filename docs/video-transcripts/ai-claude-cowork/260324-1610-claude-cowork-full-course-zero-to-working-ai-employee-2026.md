# Claude COWORK Full Course: Zero To Working AI Employee (2026)

**Channel**: KJ Rainey
**Duration**: 88:07
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=C9gKWTzRukM
**Transcribed**: 2026-03-24 16:10

---

## Organized Notes

**Course Structure and Philosophy**

- **KJ Rainey** presents a complete Claude Cowork course split into two parts: a **beginner setup** (first 16 minutes) and an **advanced masterclass** (remaining 72 minutes)
- Core thesis: Claude Cowork is fundamentally different from chat-based AI because it's an **agent with computer access** — it does things for you rather than telling you what to do
- Positions Claude Cowork as "**10 personal assistants who never sleep, have a 500 IQ**" for less than a DoorDash order ($20/month Pro plan)
- Created a **free starter pack plugin** (downloadable from his School community) that handles initial setup with pre-built skills: `/setup`, good morning, end-of-day, new project, and help

**Beginner Setup (4-Minute Quick Start)**

- Download Claude Desktop, create account, verify phone, subscribe to **Pro plan** ($20/month) or Max ($100/month)
- Select **Cowork mode** (not Chat or Code) — the best middle ground between chat simplicity and code power
- Use **Sonnet 4.6** for most tasks — Opus 4.6 is only needed for complex coding or large planning; Sonnet has bigger context window and more usage allocation
- Install the starter pack plugin via **Customize > Personal Plugins > Upload Plugin**
- Select a **single folder** as Cowork's workspace — contains everything to a single location for safety and organization
- Run `/setup` — the plugin interviews you (name, what you do, what help you want, communication preferences, timezone) and creates:
  - A **claude.md** file with all preferences
  - A **daily logs** folder for session persistence
  - A **getting started PDF** with workflow instructions
  - **Project folders** for organized work

**Daily Workflow Pattern**

- **Start**: Say "good morning" — Claude loads previous session context, recaps what was done, shows what's still open, recommends next steps
- **Work**: Talk through problems, create projects, iterate on tasks
- **End**: Say "I'm done for the day" or "let's wrap up" — triggers the end-of-day skill that creates a **daily log** documenting work completed, what's still open, and tomorrow's priorities
- Without this daily log system, Claude **forgets everything between sessions** — the plugin solves the persistence problem through structured markdown logs

**Real-Life Use Cases**

- **Second brain productivity system**: Obsidian + Claude — every note from everywhere stored and readable by AI, providing full life context, 10x productivity, and effortless content generation
- **Automated daily YouTube videos**: Claude generates 3-5 video ideas per day based on KJ's own ideas, creates titles matching his style (learned from analyzing all past titles), and auto-uploads — already generating 7,000+ views in the first 10 days
- **Full app buildout**: Saves ideas, Claude validates them and creates detailed UI mockups and instructions for his engineer, who then uses Claude as a "20x coding team"
- **Free School community** (800 members): Claude helped brainstorm setup, graphics, traffic strategy, and course creation
- **Email copywriting business** ($2,000/month): Reduced 10 hours/week of email writing to 1 hour — Claude generates ideas, drafts, formatting; KJ adds human tweaks
- **Personal health**: Lost 5+ lbs, improved posture, vocal improvement — uses Claude for diet tracking and accountability
- His wife **Caitlyn's banner business**: Set up Cowork in one session, researched camera tripods on Amazon, learned video recording techniques, started making Instagram content within a week

*Quotable Quotes:*

> "The best value in skills are using them in your personal life, not downloading other people's skills or finding stuff online, but what are problems that you have that you can solve with AI and repeatably solve it with a skill." [1:11:02]

> "Don't automate everything. That shouldn't be your goal. Automate the robotic stuff so that you can actually be creative." [1:25:07]

> "Productivity doesn't mean how many things your AI can spit out. It's tangible progress towards your goal." [1:27:08]

**The 10-20x Productivity Framework**

- **Productivity** = making tangible progress toward your specific goals (not just generating AI outputs)
- Framework: **Set a clear goal > Find ideas > Capture them > Make a plan > Test by doing > Repeat**
- **First principles thinking** (Elon Musk, Jeff Bezos model): Identify the "laws of gravity" behind reaching your goal, then build tactics on top of them
  - Example: "People pay more attention to faces" (first principle) → "Include face in thumbnail" (tactic)
  - Example: "People prefer natural-looking skin tones" → "Color correct thumbnails in Photoshop"
- **AI's role**: Does all these steps 50x faster, cheaper, and easier — finding problems, discovering principles, testing tactics, building solutions
- **Why most people fail with AI**: The robot has no context about your business, life, goals, or problems — "you have the best employee in the world, but he has no clue about your business"
- **Three sources of ideas**: Observe what people say (easier, less tested), observe what people do (harder, more tested), and think independently (hardest, highest potential)

**How AI Actually Works (Explained Simply)**

- AI is **not a magic genie** — it's a "super nerd" who is brilliant at knowledge but lacks experience, judgment, taste, and personal context
- **Strengths**: Sheer knowledge, following direct orders, processing information at scale
- **Weaknesses**: No personal context, bad long-term memory, no real-world experience/nuance, no taste
- **The "brown paint" analogy**: AI is trained on all websites (all colors), but when you ask for "a website" it averages everything and produces "brown" — you must be specific to get the pink, yellow, or exquisite output that's in its training data
- AI gives the **standard deviation** of all outputs — it defaults to average unless you provide specific context, examples, and constraints
- **Every tool covered in the course** exists to fix these specific weaknesses

**Claude's Full Power: Technical Concepts (Explained for Beginners)**

- **Tokens**: Just words — computing power costs money per word processed
- **Context window**: Claude's "whiteboard" — loaded fresh each conversation, gets worse as it fills up (keep under 500K, never try to hit 1M)
- **Markdown files**: Simple text files Claude reads instantly — giving it custom context from a "filing cabinet"
- **YAML front matter**: Tags on files so Claude knows which file to pull without reading them all — prevents loading irrelevant context
- **Folders**: Filing cabinets holding organized markdown files for different domains (content, emails, projects)
- **Skills**: Special markdown files with instructions (SOPs, context, scripts) that appear in the Cowork UI and can be toggled on/off
- **claude.md**: A "golden" markdown file loaded in every conversation — tells Claude who you are, folder structure, active projects. Exists at two levels: **global** (applies everywhere) and **local** (per-folder, specific to that workspace)
- **Plugins**: Bundles of skills and commands packaged together under one goal — "a meta-skill"
- **MCP servers**: USB ports connecting Claude to external applications (Figma, etc.) — gives Claude instructions on how to use the app
- **API keys**: Room keys for Claude to access specific services (Google, Stripe) — keep private
- **Obsidian**: Note-taking app for viewing and editing markdown files beautifully — both human and Claude work in the same "filing cabinet"
- **IDEs** (Antigravity/Windsurf): Like Obsidian but for coders — same files, different interface, with Claude Code built in

**Building Basic Skills (Live Demo)**

- Process: **Identify an annoying repetitive task > Define the desired outcome with examples > Write down your normal process > Have Claude build it > Refine > Save as skill**
- Live example: Coaching call transcription skill
  - Input: Loom transcript of 30-60 minute coaching calls
  - Output: Timestamped topic summaries formatted for school posts
  - Iterative refinement: adjusted formatting (line breaks), tone (less clickbait, more substance), length (10-15 words max per point)
  - Claude saved all refinement instructions into the skill so they persist
- **Key insight**: Always read through the generated skill.md and verify — AI sometimes misinterprets instructions or adds unwanted constraints

**Advanced Skill: YouTube Video Validation**

- KJ built a skill that validates YouTube video ideas by:
  - Pulling **competitor video analysis** (thumbnails, titles, views-to-subscriber ratio)
  - Analyzing **packaging patterns** across top-performing videos
  - **Intro analysis** of first 90 seconds of competitor videos
  - **Market trend data** — real search volume for topics
  - **Verdict**: Should you make this video? With reasoning
  - **Recommended angle**, title building blocks, 10 title ideas, thumbnail building blocks, discovery gaps, video tags
- All generated in **5 minutes** from a single skill invocation

**Four Keys to Incredible AI Outputs**

1. **Focused context only** — Give Claude only what it needs for the specific output, nothing more. "If you're making pizza, don't give him the entire pantry — just the pizza ingredients"
2. **Better inputs = better outputs** — "If Gordon Ramsay gets moldy tomatoes, the pizza will suck." Invest in quality customer research, examples, and concise skill instructions
3. **Human checkpoints and feedback** — Never let AI one-shot everything. Build review steps into the process: "What do you think, KJ?" → feedback → iterate
4. **Frequent iteration through doing** — Don't over-restrict skills. Define what NOT to do, then let Claude have creative freedom. Run the skill repeatedly, refine inputs and recipes each time

**Advanced System Design: Email System 2.0 ($2K/month)**

- **Architecture**: Separated into multiple specialized skills rather than one monolithic skill
  - **Email idea skill** — pulls general client context + condensed past content scripts → outputs 15 ideas
  - **Human checkpoint #1** — KJ selects an idea and adds refinement thoughts
  - **Type-specific email skill** (valuable insight, sales, promotion, story) — runs with focused context for that email type only
  - **Sub-agent review** — spawns a fresh agent with clean whiteboard + email quality criteria to review the draft (unbiased because it didn't write it)
  - **Human checkpoint #2** — final touches before shipping
- **Key design principle**: Separate tasks so each skill gets only the context it needs — 1.0 had one skill doing everything (bad outputs); 2.0 has specialized skills chained together (great outputs)
- **Context preparation**: Condensed hundreds of pages of client content into 2-page summaries; distilled 90 ideas from transcripts — "don't give him 150 pages of random slop"

**How to Get Ahead of 99% of People**

1. **Building with AI is a new skill** — Speedrun to as many hours as possible. "Ask AI what to ask AI." Don't just watch videos — go use it
2. **Don't automate everything** — Automate robotic tasks so you can do more creative work. "God created us to work. AI is a gift that lets us work on what we want to work on"
3. **Focus on problems, not tools** — Don't look for uses for new tools; look for tools to solve existing problems. "If you see a video about making a website, ask: Do I need a website? Is that my main problem?"
4. **Productivity isn't output volume** — It's tangible progress toward your goal. Quote from Henry David Thoreau about the telegraph: "Everybody rushed to connect Tennessee to New York — but what does Tennessee have to say to New York?"

---

## What This Means for Your Work

KJ Rainey's course covers familiar ground — folder-as-identity architecture, skills, plugins, claude.md, Obsidian integration — but through the lens of a non-technical creator who treats AI as a business operator rather than a developer tool. The unique contribution is the **four keys framework** (focused context, quality inputs, human checkpoints, iterative refinement) and the **email system 2.0 architecture** where tasks are decomposed into specialized skills chained with sub-agent review.

**Where this maps to your work:**

- **OOBC distribution model validated**: KJ's starter pack plugin (setup + daily log + project creation) is exactly the kind of package you should build for Prof. Noron Andan's staff. A `/setup` that interviews the user about their role in OOBC, creates folder structure for OBC policy work, and establishes a claude.md with BARMM-specific conventions. The "good morning / wrap up" pattern solves the session persistence problem without requiring Obsidian.
- **Email system 2.0 → Legislative briefer decomposition**: KJ's insight about separating the idea skill from the type-specific email skill maps directly to your `/legislative-briefer`. Instead of one monolithic 13-section CSW skill, consider decomposing into: (1) a research/context-gathering skill that identifies relevant BAAs, BOL provisions, and BDP chapters, (2) type-specific analysis skills (impact assessment, Shari'ah analysis, interpellation strategy), and (3) a sub-agent reviewer that checks against BOL compliance criteria without the bias of having drafted the content.
- **"Brown paint" problem in bill drafting**: KJ's analogy about AI averaging all outputs into "brown" unless given specific context is exactly why your `/bill-drafter` needs the reference files (drafting-principles.md, word-choice-guide.md, bta-legislative-process.md) you created this session. Without them, Claude produces generic legislation. With them, it produces BTA-formatted, BOL-compliant bills.
- **Sub-agent review pattern**: KJ spawns a fresh agent with clean context to review email drafts. This maps directly to your `/fact-checker` workflow — a sub-agent that receives the draft bill/briefer with only verification criteria (correct official names, valid BAA references, proper legislative formatting) and no authorship bias.
- **The "don't automate everything" principle**: Particularly relevant for your legislative work. Bill drafting, policy analysis, and interpellation strategy require human judgment and political taste that AI lacks. Your current approach (AI drafts, human reviews, /fact-checker validates) already respects this boundary — KJ's framework validates it.

### How This Can Improve Your Claude Skills and Workflows

**Skill improvements:**

- **/legislative-briefer** — Apply KJ's email system 2.0 decomposition: split the monolithic 13-section briefer into a research-gathering phase (identify relevant BAAs, BOL provisions, committee reports), type-specific analysis phases (each as a focused skill with only the context needed), and a sub-agent review phase. This matches his principle of "give Claude only what it needs for the specific output."
- **/bill-drafter** — The "four keys" framework validates your existing architecture: (1) focused context via reference files, (2) quality inputs via BOL/BAA/BDP references, (3) human checkpoints at each drafting phase, (4) iterative refinement via /auto-research. No changes needed — you're already doing this.
- **/training-assistant** — KJ's starter pack plugin model (setup interview + daily log + project creation) should be replicated for MoroTech SEED Initiative facilitators. Create a Cowork plugin with `/setup-facilitator` that interviews about training topic, audience, and objectives, then creates module-specific context files.
- **/skill-optimizer** — KJ's emphasis on iterating skills through use aligns with your auto-research methodology. His advice to "not be too restrictive" and "define what NOT to do, then let Claude have creative freedom" could improve eval criteria design — test for constraint violations rather than exact format compliance.

**Workflow changes:**

- **Context preparation discipline**: KJ's practice of condensing hundreds of pages into 2-page summaries before giving them to skills validates your existing pattern of distilling knowledge notes (3-5 key takeaways) from full transcripts. Consider applying this to your 78 BAA files — create a condensed BAA summary index that `/bill-drafter` and `/legislative-briefer` can load without pulling all 78 full texts.
- **Plugin distribution for OOBC**: The starter pack plugin + School community model directly maps to your planned Cowork plugin distribution for BTA Parliament staff. Build a "BARMM Legislative Assistant" plugin with: `/setup-mp` (interviews about committee assignments, policy priorities), `/morning-brief` (scans for new BAAs/resolutions), `/wrap-up` (saves session decisions to daily log).

**No new skill recommended** — KJ's course covers patterns already in your skill library (content creation, system design, iterative refinement). The novel contribution is the distribution model (plugin + free community + starter pack) which is an operational pattern, not a skill.

---

## Transcript

[00:00] Welcome to the best cloud co-work guide on YouTube. You're about to learn how to go from a complete beginner to having AI solving real problems in your life in the next four minutes and then we're going to dive deep. In the next hour, you will understand how to use AI better than 99.9%

[00:17] of people. I'm not kidding. Which will radically change your life. You have my

[00:22] word. Because after learning how to use Claude Co-work in my life, this is what happened just last month. It's literally too much for me to read, so you can pause it and check it out. But it's

[00:30] absolutely insane, man. But you're probably thinking, KJ, I've used Chat GPT before, and it was cool, but it didn't really change my life. And I get that. I felt the same way. But Claude

[00:40] Co-work is completely different. You see, you've been using AI chats where you yap back and forth with the robot and it tells you what to go do. But Claude Co-work is an AI agent, meaning it has access to your computer. It can

[00:53] do things for you, not just tell you to do stuff. The power is actually unreal. It's like having 10 personal assistants who never sleep, have a 500 IQ that can learn anything. And did I mention it

[01:05] costs less than a Door Dash? What a freaking time to be alive, man. This is crazy. And that's why I'm making this

[01:11] video. I want to help you unlock this power for the first time in the next 2 minutes. So, let's go do it. Let's jump

[01:17] in. All right. First thing you want to do is go to Claude's website, which I'll link in the description, and you just want to come down and download Claude for Desktop on whichever operating system you have. I have Mac. So, we're

[01:26] going to download that. Then, you're going to wait for it to download and you're going to drag that sucker onto your homepage. So, we'll do it just like that. Boom. Now, we have Claude. Then,

[01:34] all you want to do is you want to double click that. You want to install it to your applications. And then, you're going to be good to go. Then, all you

[01:39] have to do is run Claude. So, I'm going to hit command space. I'm going to type Claude. And that's going to run the app.

[01:44] And this is what you should see. We're going to go ahead and click get started right here. I'm going to use Gmail. I

[01:49] always use my Gmail, but you can also just enter any email you've got. I'm going to do continue with Google. I'm going to create a brand new account. So,

[01:55] I'm going to have Caleb blur out my Gmails here. We're going to do continue with Gmail. And then I'm going to choose an account. Scroll down and click

[02:02] continue. And now it says your account needs to be verified. So, I'm going to click that. I'm going to do create

[02:06] account. And then we're going to put in my phone number right here. And I will get back to you guys when I verify that.

[02:10] All right. It has sent a code to my number. I'm going to put that code in.

[02:13] After you verify your phone, it will pull up the plan section. Now, to use co-work, we are going to have to pay for the pro or the max plan. Like I said earlier, it's like one Door Dash bill for unlimited leverage to achieve the goals you want in your life. I am in no

[02:28] way incentivized to tell you guys to use this. I have no affiliates, no nothing. It is just changed my life genuinely.

[02:34] And this is what I recommend to my family, my parents, everyone. So, I'm recommending you to do the same. It's so worth it. Just skip eating out for one

[02:40] day a month and use this and it's going to make your life incredible. So, Claude now has their own onboarding system which we're going to go ahead and go through right here, but it's super simple. I'm just going to do a test. So,

[02:50] do Johnny, which is my brother's name, and pick these three topics. I'm just going to pick something random, live stuff, uh, you know, whatever. Writing content. Let's go. Here are a few ideas.

[02:59] I'm going to say I have my own topic, and we're just going to put in something random. That way, it starts us up. I like to only have the icon selected. I

[03:07] use other software for these things. I'm going to click continue. Now, um, I'm going to go sign into my pro account and I'm going to show you guys my setup, which is honestly, I think, 10 times more useful than Claude's. So, let's go

[03:17] do that. So before we get into the complete setup, I just want to walk you guys through the basic application just to show you what's going on. So at the top we have chat like I talked about earlier. This is the classic just

[03:27] chatting with the AI. Then we have code which is a very in-depth version of like developers and how to actually write code and stuff. The best thing is co-work. It's the best in between. It's

[03:38] like using the powers of code being able to actually do stuff on your computer, but it's the simplicity of chat. It's awesome. So I'm going to show you guys how to set this up. On the left hand

[03:48] side, you will see a couple different things. We'll go over these in detail in the advanced session. But we've got new task, we've got scheduled task, which we'll cover later, ideas, customize, and you see can see all of your tasks that you've done on the left hand side right here. Then we will go to down here to

[04:03] settings. And so if you want to go to the settings, you can see like languages, upgrade plans, stuff like that. We go into settings, very simple.

[04:09] You'll see like your general, your account, your privacy, billing. I won't go into any of these quite yet because it can get a little deep. So, the one thing I do want to cover is usage. Basically,

[04:18] this allows you to use all the computers and the AI of Cloud. It does cost a lot of money to run these things, and that's what you're paying for with the plan. So, with the basic $20 month plan, you do get a lot of usage. We'll talk about

[04:29] how to maximize that later, but with the $100 month plan, you get so much that I have never run into this. Like, unless you're like doing insane amounts of coding, in which you're probably not watching this video anyway, you're never going to run out of this. It's crazy.

[04:41] Now, let's get into actually setting up co-work in an instant. It's wild. All right, with all that boring stuff out the way, let's actually start using co-work to get stuff done and change our life. So, I have made a plugin to help

[04:52] you guys set this up instantly. It walks you through all of it in a way that's extremely productive. And so, yeah, it's all free. All you got to do is go to the

[04:59] first link in description. So, let's do that. You will see my AI school. Once

[05:02] again, it's free. So, join that. I can't wait to see you in there. All you have

[05:05] to do is go to classroom, start here, YouTube resources, and you will see KJ's co-work starter pack. It's that simple. This is the easiest way for you guys to get this stuff safely. Then you're just

[05:16] going to download it. It's going to go to your downloads. I want you to drag that to your desktop. Just like this.

[05:21] Now, all we do is we go back over to Claude. We make sure we're selected co-work at the top. We're going to go to customize on the left hand side. You

[05:30] will see personal plugins. Now, these are just basically scripts and tutorials and things that people can make for you. So, Claude has a lot of plugins that they've already made. I've made one for

[05:40] you which we're going to use to set up. All you do is click on add plugin, upload plugin, and you can drag this zip right there. It's that easy. Literally

[05:48] three clicks. Then you just want to make sure that it's checked. So make sure that it's enabled. And now we go back to

[05:53] the new task. We want to select the folder. So by selecting the folder, you're choosing where you want co-work to work. And so if you select your

[06:01] desktop, it has access to everything on your desktop. So we just want to contain it to one folder to make sure that everything is safe and we have everything nice and neat. So, we're going to select that new folder that we just made. So, we're go to desktop,

[06:13] co-work home base. Awesome. This is where co-work is now going to live for this chat. You can change it for each

[06:19] chat. Next thing we're going to do is we're going to use Sonnet 4.6. So, like

[06:22] I talked about that usage bar, Opus 4.6 is the most powerful model. You really don't need it for anything besides coding or some really large planning task. I find that Sonnet, even with the

[06:34] semi-complicated work I do, Sonnet is perfect and it has a way bigger context window, way more usage. So, start there. Now, all we're going to do, pay attention, it's very easy. This is all

[06:43] you have to remember, is do slash setup. That's it. I've done everything else for you guys. And we'll just do let's go and

[06:49] let's see what happens. Let's set this puppy up. So, I'm going to collapse this. We're going to go full screen

[06:53] here. And we're going to follow along the setup. And so, let's let it do its thing. So now what it's doing is it's

[07:01] running these commands and it's setting up your home-based folder perfectly. First thing it's going to ask is what is your name? I'm going to fill this out as if I'm my wife because I actually set this up for her and it has changed her local banner business in a week which is awesome. We're going to do Caitlyn. I'm

[07:15] going to say I paint custom banners for celebrations locally. And so that's what I do right now for fun and for some side income.

[07:31] That's what my wife actually does. She's awesome at it. Cool. Now, it's going to ask us some more

[07:38] questions, which are very simple to answer. What are you hoping I can help you with? I'm just going to say, honestly, all the above. So, I just want

[07:44] you guys to type in here whatever you want co-work's help with, it can help you with. I promise. So, we're going to do all the above. How do you like to be

[07:50] served? I'm going to say, "I like you to be very friendly and encouraging because I want someone to just help me get work done and encourage me even when I'm not feeling 100%." So, that's what we'll say. Like I told you guys, I've

[08:03] programmed this plugin to remember all these things. So, every time that you use Claude in this folder, it will remember this stuff. Time zone, we'll go Eastern. Cool. And now what it's doing

[08:13] is it is setting up stuff in your folder right now, which is really cool. We'll go over that in a second. All right. And

[08:18] now it is done. It says we're all set up. Caitlyn, here's what I've created.

[08:21] It's gone over this claude MD daily logs getting started. You don't have to remember any of this, guys. I'll walk you through what it does. I've actually

[08:28] included a little PDF in this guide that it creates for you. So, let's go over what this looks like. This is the getting started PDF. So, basically, this

[08:37] just goes over the plugin that I've given you guys, how your workspace is organized. The only thing you have to remember are really this right here. So, to start your day, you just say good morning to Claude. That's all you have

[08:47] to do. It'll go back. It will remember what you were working on. Then you just

[08:51] work on your projects. You talk to Claude. You get it to, you know, help you with everything you need. And then

[08:56] at the end of the day, all you say is, "Hey, I'm done for the day or let's wrap it up." That's it. Everything else is handled by itself. So, let's walk

[09:02] through exactly what that looks like. So, now Claude is going to ask us, "What are some projects that we want to work on?" I'm going to walk you through the flow that my wife actually did last week and she's already changing her business, which is so cool. So, let's go

[09:15] through that. The first thing I want to work on is growing my social media. And so I have an Instagram for my banner page, but I don't really know what to post. I don't really have good branding.

[09:25] And I know I should be posting reels, but I just don't know how to record them or how to actually get views on them. And the main goal of this is just to get some more local customers and to inspire other people to do something similar. I'll call it Instagram content. Let's

[09:41] call it that. What does done look like? I would say I want a very simple system to record my banner creation and then a simple way to turn that into content that gets views and also gets me clients.

[09:57] So, keep it simple and I highly recommend that you guys actually answer the questions yourself. It does give it more context and you'll probably get better results. So, let's let it cook.

[10:06] So, here we go. It's actually creating a project called Instagram content which is awesome. Let's watch what it does in here.

[10:14] All right, it is actually writing Instagram content overview. We'll go over this in depth in the advanced section of this course. But what you've got here is you can see the things that it's writing. So it's

[10:26] writing this for you guys. It's giving you the goal, the why, the tangible outcomes, the problems that you need to solve. It's so freaking powerful. It's

[10:36] so awesome. And so all this is is this is a simple text file in here. And so you can open this with like text edit and you can see that here's like what the computer sees. It's super simple. It

[10:46] makes Claude 10 times more powerful and you can see it nice and pretty over here in Claude. You can always see what you're working with over here. Let's see what it said. Here's what I mapped out.

[10:55] How to record, how to make reels that get views, what to post, basic branding. And so it's like let's dive into one of these. And so let's go into how to record. All right, let's get started

[11:05] with how to record. So, I have a DJI Osmo Pocket, but I don't really know how to use it or how to set it up in a way that I can actually record the banners. And so, can we just like get that set up and maybe I can send you some footage and you can just correct me on what to change. So, we'll just yap and see what

[11:24] it says. All right. So, now it is telling us, okay, the camera you have is great, but if you don't have a camera, you could ask it, what are the best cameras to get? Can I use my

[11:31] iPhone? It is really, really cool. So, in this real scenario, my wife had this Osmo Pocket camera that I just gave her because I wasn't using it and but she didn't know how to set it up with a tripod. And

[11:42] so, what Claude did is it went and researched the best tripods on Amazon that she needed. She ordered it that day. It was there tomorrow. She recorded

[11:50] her first reel, gave it to Claude, it corrected on like how to position it, and now she's making content, guys. It's awesome. It's so incredible. So,

[11:59] yeah, I won't go any deeper than this because honestly it's going to be tailored to your problems, but just get started. Just start solving problems with it. And so now all we're going to do is I'm just going to tell it actually Claude that's good for now. I

[12:11] think I'm done for the day. I'll come back to work tomorrow. So all you have to remember is, like I said, slash setup to set this thing up.

[12:20] And once it's up and running, the first command you have to remember is just tell it that you're done for the day. That's it. That's it. All you say is,

[12:26] "Claude, I'm done for the day." And so what this plugin that I've given you guys will do is it will now save your progress. Without this, Claude doesn't know where to start every day. It

[12:36] forgets every single day, which is so annoying because you'll have such a good session with Claude. You come back tomorrow and he doesn't even remember it. He might remember a little bit, but what it's doing is it's creating a daily log for itself. And so here you can see

[12:50] this daily log. If I click on it right here, we can actually view it. Whenever you run that skill by saying I'm done for today, it will go over what you did work that day, what's still open, and what you want to do tomorrow. So, it's

[13:01] super super simple. And like I said, this is all just text files in your folders, which is so awesome. Now, let me actually show you the other commands.

[13:09] So, if we go back here, we'll do a new task. And so, once again, I will make sure that co-work is selected. And all I will do is I'll say good morning. And so

[13:20] every time you want to start working again, you just say good morning Claude. And now let's see what it does. Let's check it out. And like I said, all of

[13:25] this is in the getting started, by the way. So pretty simple. Also, if you want to see what the claude.md is, which is basically like the instructions for Claude every time, you can check that out.

[13:37] All right. So now it's saying good morning. It's using my name because it has my actual name. But here's a quick

[13:42] recap of last session. We got your workspace set up, all the folders. We kicked off Instagram content. We built

[13:47] out this. Here's what's still open. That's the next step. Here's my

[13:51] recommendation. But also, is there anything else you want to get into? Guys, that is it. Do you see how

[13:57] magical this is? It is life-changing. It helps you actually do stuff, get things done. And so, that is it. All you have

[14:04] to remember is, like I said, we go over here to the get started. If you ever get lost, you can check this out. All you need to know is start your day with good morning, work on your projects, and then just say wrap up or end of the day whenever you're done. And if you ever

[14:16] want to create a new project, you just kind of tell Claude, "Hey, I want to start a new project." This is what it's called. And it'll actually interview you. So, let me actually run through

[14:24] that real quick. Actually, Claude, I want to work on something new today. And so, let's see. Now, he is running

[14:31] the new project skill. And so, it's creating a brand new project. It's going to say, "What's it called? What's the

[14:35] goal? Why does it matter? And what does done look like? What are your problems?"

[14:39] You don't have to answer all these guys. Just answer whatever you want. So the project is called diet tracker and the goal is I want to find healthy meals and then track those with an app so that I actually can hit my fitness goals. This

[14:53] matters to me because I want to be healthy and I just want to be more disciplined with my diet. What would done look like? It would be whenever I have a simple system that's easy to kind of find good foods, buy them and then track them. So, the problems that would

[15:06] need to be solved is I don't know, I guess helping me figure out what to cook, then helping me figure out how to make a grocery list easily, and then figuring out how to actually track those calories and what calories should I even be aiming for. And so, now we're going to just dump that in there. You can see why the voice thing is so important, by the way, which I'll show you guys how to get later on in the master class. And

[15:28] notice how it's like talking to me like I gave it the instructions to. It's very encouraging, very friendly. And so you can have this thing be like a drill sergeant. You can have it do whatever

[15:36] you want in the setup phase. And now it is creating the brand new project. So if we go to projects, we can see we now have diet tracker project. It's creating

[15:44] the overview. It's going to create all these assets for us. And like I said, you can see them on this right hand side. There's the goal. There's the why.

[15:50] Here's the outcomes. Here's the open problems. We can dive straight into it.

[15:53] Like you can literally say, "All right, I want to figure out what to cook." And you can just talk with Claude. It's so crazy, guys. If we look back on the

[15:59] Instagram content, we can see that it already started an Osmo Pocket recording setup. And so if I open this up with text edit, which if you're in the project, you can just open it up in Claude. It'll say we're going over the settings, how to position the camera, the lighting of the camera, how to mount it overhead, what to actually record, like guys, instantly. It's crazy.

[16:20] But yeah, that's the whole setup. This is all you need. You don't have to go any deeper than this. I wanted to like

[16:24] not try to get views or try to get ad revenue. I just want to give you everything you needed. Claude will help you do the rest. You don't need the rest

[16:30] of this video. But those of you who do want to dive deep and really understand the technology to unlock its full capabilities, let's dive in to the advanced portion of this master class. Leave a like if you're enjoying so far and I'll see you guys over there on the deep end. All right, welcome to

[16:44] part two, the advanced section of this master class. Things are about to get real and they're about to get powerful. I hope you're ready. So, let's go over

[16:51] what we're going to cover. The first thing we're going to cover is my ballin real life use cases. These are the use cases that have literally changed my life in the past month. This is not some

[16:59] like, oh, let's create a little website demo. No, I'm only going to show you guys what I actually use. What's really changing my life and my family's life forever. Part two, how to literally

[17:09] 10 to 20x your productivity using AI. Most people don't understand how to leverage the technology. When you get this, your entire life changes. I'm

[17:17] going to show you guys how to do that. Part three, how to access Claude's full power. So, the basic mode is very, very powerful. Don't get me wrong, I gave you

[17:24] guys everything. But when you understand all of the tools at your disposal and how everything works, that's when you unlock the real power of Claude. I'm going to show you how to do it step by step. Four is how AI actually works. So

[17:35] going over the tools and terminology so that you know what everybody's talking about in these videos in a very simple way. Part five is creating basic skills. I'm going to walk you through creating your first skill. Part six, creating advanced

[17:46] AI systems. So, how do we link together multiple different skills, plugins, context, MCP servers, all that stuff to create crazy outputs and solve big problems? And then last but not least, the cherry on top part seven, how to get ahead of 99% of people using AI.

[18:02] This is stuff that I've not heard anyone talk about. It goes much deeper than just like the basics. So, hopefully that'd be a nice ending to this master class. I can't wait. I'm very excited.

[18:09] I've been preparing this for weeks for you guys. So, let's jump in. All right.

[18:12] Welcome to ballin use cases. I thought the best way to kick off this advanced section would be to show you how I use this technology in my real life to solve real problems. Most YouTubers will show you how to make a cool website or how to organize your files, but I know you guys want more than that. You want to

[18:28] actually use this to change your life. So, I thought, what better way to do that than to show you how I actually use it every single day to change mine. So, the first thing that I have is my second brain productivity system. I'll make a

[18:39] full video on this. If you want it, let me know in the description. I also have a full course on how to set up my basic version of this in the free school. But

[18:45] what I do is I have Obsidian and this is a note-taking software that saves files locally on your computer. We'll talk about more of that in a little bit. Plus, Claude can actually read those files and can help me literally run my entire life. It knows all my

[19:00] information. I have commands built into this. Like, it is awesome. And so, every

[19:05] note from everywhere is stored and readable by AI. I get insane clarity from this. My AI has full context around my life. So, it gives me better

[19:13] judgments and outputs. I'm also 10 times more productive because it helps me stay on track. That's the most powerful part, using AI to prompt you. It's like a

[19:22] personal accountability partner who never sleeps, who knows everything about you, knows your weaknesses, your strengths, and helps you just become a better person. And content is on easy mode. So, because my entire life is in this second brain system, it can pull ideas for me immediately. Like 15 of

[19:38] them. That's how I make all my videos on my daily channel. So, super sick.

[19:42] Speaking of daily channel, the next place I use it is my automated daily YouTube videos. So, I have raw ideas and projects. Claude will generate me three to five videos per day based on my own ideas. That's the crazy part. He goes

[19:55] through and he literally creates titles and hooks based on my style. So, I fed him all of my channel titles. And if you don't have an existing channel, just steal somebody else's channel that you really like. I fed them all the titles.

[20:07] He then created a formula of how to do those titles for himself. And now he gives me the ideas, he gives me the titles, then he auto uploads every single video. I'm like weeks ahead on these videos because he does all of it.

[20:19] I've never been able to be this consistent and this valuable to you guys, but thanks to AI, now I am. And so in the first like week and a half of doing that, I already generated, you know, 7,000 views, lots of subs, and some money, some coffee money. So pretty exciting. And if I do that for

[20:34] years, this channel is going to blow up. Next is a full app buildout. This is how this thing is literally hopefully feeding my family for generations. I

[20:44] have all these random ideas and I can save these ideas and then Claude validates them and creates detailed instructions for my engineer. So, I have an engineer that works on this with me because I'm doing so much and he's incredible. But now I can actually give him full mockups and give him all my ideas and Claude creates them literally like he'll create the entire UI and everything and I can say, "Hey, I don't like that. Change that. Change this.

[21:09] Tweak that." And now my engineer knows exactly what to make and then he uses Claude to become like 20x his power. So now it's like he has an entire coding team that works for us for free essentially $100 a month. And yeah,

[21:24] I'll share more about that soon, but I've never been this excited about my life in my life about something like this. So insanely powerful. Also, the new school community that I gave you guys for free. Normally, I'd have to

[21:34] charge for something like that. And people still think I should, but I have this passion for teaching and now because of Claude, I can easily brainstorm my stuff. I can clarify my goals. Claude helped me brainstorm the

[21:46] setup, the graphics, etc. Then he helped me brainstorm the traffic and now the school has 800 members without even posting a video about it yet. Insane.

[21:53] And some of the people in there like literally like what the heck? This should be paid. Wow. Yeah, it's all

[21:59] free. Go check it out. Not to even mention the courses, by the way. I built

[22:03] the two life courses using Claude. He helps me do everything. Hopefully you're seeing this at this point. Now, for

[22:08] those of you guys who like, well, how do I make money with it? Claude saved my freaking life as far as business is concerned. Jesus saved my real life. But

[22:17] as far as business, Claude literally saved it because I used to have to write these emails for my clients. It took I don't know 10 hours a week, which is a lot of mental effort. Now it takes literally one. Claude gives me the email

[22:29] ideas. He gives me the rough outline. He formats it perfectly for scheduling. I

[22:34] then add the perfect amount of human tweaks. And I make 2K a month every single month by providing these emails. And it's amazing. My clients are happy.

[22:42] I'm happy. I don't have to do a lot of work. It's amazing. And the last thing

[22:45] is I've lost 5 lbs. Actually more than that now. I have a posture check routine. My posture has improved. My

[22:49] vocals have improved. I'm just doing everything. I'm peaking right now because of how amazing Claude is. And

[22:55] you guys are going to learn how to do all of this in this video very simply. So let's move on to the next section. This is ballin use cases. And let's go

[23:01] over how to do this. All right. You're probably thinking, KJ, that stuff is cool and all, but how do I use this in my life? I'm not a YouTuber. I don't

[23:08] have a school group. I'm not trying to build an app. Well, let me show you exactly how to do that. How to 10 to 15x

[23:13] your productivity with AI. And this is not overhyped, by the way. This is actual literally the numbers you could expect, maybe even more. So, this is you

[23:20] right now and you have goals in your life, whether conscious or subconscious. You have stuff that you want to accomplish and you have whys of why you want to accomplish that stuff. But if you're watching this video, then you probably don't know how to do it exactly. So, the first step that we do

[23:35] this is we figure out what are the problems along the way to reaching this goal. Let's say my goal is to hit 100,000 subscribers. Well, there's a lot of problems. What kind of videos do I make

[23:47] about? Where do I get ideas? How do I do the title and thumbnail? How do I actually record the video? What do I put

[23:54] in the video? How do I like tag the video? How do I promote it like somewhere else? Like all these different

[23:59] problems that I have to solve in order to then reach this goal. And so, how we do that is we start by analyzing first principles. And this is not what most people do. And you don't

[24:11] have to know first principles to succeed. But there's always first principles at work when you do succeed. That is the key. So if you watch Elon,

[24:20] Jeff Bezos, you know, Steve Jobs, old stuff, like all these people think in first principles. And so they want to figure out what are the kind of the laws of gravity behind reaching this goal. And so a first principle for YouTube could be that hey people pay more attention to faces. It doesn't

[24:40] mean you should always have a face in your thumbnail, but that is a first principle. People pay attention to faces more than they do any other body part. And so the tactic to this that you could build off the first principle would be I'm going to include my face in a thumbnail. Or the first principle could

[24:54] be people prefer to see color corrected natural looking skin tones. Like people prefer natural looking footage and so the tactic could be I'm going to use Photoshop to color correct my thumbnail. And so by finding first principles, then building tactics on top of it, and you'll understand this as you go, you will then have solutions. These solutions are what actually allow you to walk across this to reach your goal. And so if I understand the principles of YouTube, how the algorithm works, how people's brains, the psychology, people's work, then I build tactics. I learn how to actually make the thumbnails, record the videos, do that. Then I actually form solutions like processes and things to help me do these things. Then I can actually start solving the problems and reaching my goal. And we'll go over how to do this

[25:38] more in depth in a second. But that's just kind of the process of how you reach your goal. And if you're not reaching your goal, it's because you either don't have any of these things going on. You have the wrong things. You

[25:49] have the wrong tactics. And so whenever you actually go to walk on this solution, it doesn't work and you fall. This is where most people quit. This is

[25:57] where you have to just try again. And try again and try again until you find a solution that actually works and you can step on it. You're like, "Okay, great. I

[26:05] know how to make a good thumbnail now." Then you go to the next problem and the next problem and you keep failing and failing and failing until you figure out all the solutions and you eventually hit your goal. People look at my like daily YouTube channel and it has like 5,000 subscribers and all I do is yap to the camera with no editing or nothing.

[26:21] And that's because I've recorded hundreds of videos. I've failed so many times that I'm slowly getting better. I'm not even at my goal yet, but I'm getting better. And so that's

[26:28] what you have to do. And so now, how is this tied into AI? I want you to imagine, okay, what I just showed you, that's how you succeed in life, by the way.

[26:38] Imagine that you have AI that does all of those things for you 50 times faster, easier, cheaper, and better. So, you have an AI that's literally finding the problems for you, helping solidify your goal, giving you first principles, trying out tactics for you, building solutions, and helping you take action. This is why AI is so powerful if you know how to use it. Not just to make a

[27:03] silly website, but how to set goals in your life, how to plan things, how to build solutions, and actually achieve what you're trying to achieve. So, the world has had AI for years. Why is everyone still broke? You have had GPT.

[27:16] You have these tools. Like, why are you still not making money? And I'll explain it. It's because for most people, your

[27:22] AI robot has no clue what the heck is going on. It doesn't know what to do. It's like you have the best employee in the world, but he has no clue about your business. He has no clue about your

[27:30] life. He has no clue what you sell. He has no clue how to actually do your business. And so, what you see is you

[27:37] see a goal and you see all these problems that you need to solve to hit your goal. But what he sees is nothing. He doesn't know. And that's the issue.

[27:47] If he knew, he could help. And so, that's what we're going to solve in this course. This is the entire point of this course. I'm going to show you guys all the

[27:52] in-depth because it's not about all these little tricks and hacks and all these things. It's just helping this very, very talented robot that's becoming even more skillful and knowledgeable over time. It's helping him see your world. Because when he can

[28:05] see it, he can go work on it. He can fix it. So, this is going to be you after this course. You're going to have this

[28:12] system. You're going to know how to set your goals. You're going to have the robots are going to know exactly what to do to actually, they're going to be able to see the bridge and start building it for you and you're going to be like, "Holy crap. Wow, this is incredible."

[28:24] And so, let's go over a real life example right now from my life. So, I like to use real stuff, not hypotheticals. This is how it helps me.

[28:30] So, let's go over it. I wanted to create the best co-work class on YouTube. So, what you're watching right now, I'm going to show you how I did this with AI. And so

[28:39] I kind of solidified the why is I want a single resource I can send to my friends, family, and viewers. Shout out to my friends and family who I sent this to if you're watching this. That takes them from knowing very little about AI to having a working setup that actually improves their lives. And also

[28:53] it gets people into my free school community where I can help them even further for free. And so that's my goal. That's what I knew. Then I had AI help

[29:02] me with the problems. And so I asked it how like what are the problems that are going to be in my way to actually hitting this goal? And then I added some of my own. So like what is the

[29:12] current market not fulfilling? So what are the other master classes not doing well? How do I make an incredible master class? Like what does a

[29:19] good master class mean? How do I make a thumbnail, title, and intro with the right people will click on? What is the outline? How do I script the intro? How

[29:27] do I make it as easy as possible for people to then see this course? And to be a little meta with you, one of the first principles is that people understand things through visuals. They understand the big picture through, guess what, big pictures. And so that's the first principle that I literally found that I'm using right now. I mean my tactic is that I'm using Miro to draw these stick figures. And so that is a first principle tactic all aimed at solving a solution which is how do I make this as easy as possible for you to comprehend. So once we had the problems, AI and my own experience helped me figure out the first principles. And so once again, the big pictures are easier to see. People want to learn stuff after they see how useful it is. That's why I showed you guys the use cases first. So all

[30:08] these things are first principles and then that allows me to build the tactics which is like I put my face in the thumbnail. I use the Miro drawings to explain these concepts. I smiled in the thumbnail because smiling makes people feel happier. First principle. I show use

[30:20] cases first and then I start teaching. All these things then led to the actual solutions. So this is real solutions that AI helped me do. So, who

[30:30] is this master class for? What makes a good master class? I literally had it help me doing all the research for the packaging. I then had it help me make

[30:38] the thumbnail. So, all these notes are from Claude. Once he understood the context of what I was trying to do, he became so helpful. He also gave me notes

[30:46] on the thumbnail. And then here's me testing out different thumbnails over and over again. So, if you guys want to see my whole YouTube system, I'll drop that in my free school course at some point. I'll make a whole thing about how

[30:55] I make these videos. But hopefully this makes sense. If it doesn't, I want you to take a second and watch this back. No

[31:02] one else is showing you how to think like first principles in YouTube because it's very, it's kind of boring and it takes a second to understand, but this is what creates success. This is how you reach your goals. And so, please watch this over again if you didn't really get it. By the way, all this was done in

[31:17] one week and now you're here. How crazy is that? This would have taken me weeks, if not maybe even months before AI, but thanks to AI, these guys are helping me do all of this at a rate of 50x what I used to do. So, pretty crazy.

[31:29] Now, a quick little bonus. This is how you be productive. So productive just means you're making progress towards your goals. So

[31:37] you're making progress meaning you're actually seeing results. Productive meaning like your goals meaning the goals that you set, not your parents, not the random society, but like what do you want to achieve? And are you making progress? And so I'll go over this real

[31:50] quick. This is my own personal framework. I'm just going to share it. I

[31:52] won't go into details. But all you have to do to reach your goal is to have validated ideas. So, you have to find what works and then you have to do it by taking action. I know

[32:02] it sounds simple because it is, but it's hard to find what actually works. You do that by setting a clear goal, finding ideas, capturing them, making a plan, and test it by doing. And then you repeat two through five until you actually succeed. That is it. Slow

[32:18] this down if you want to, you know, actually take this in, but I'm just going to move quickly. First step is filtering ideas. There's all this information in the world. You can't

[32:25] handle it all, which is why you have to set a goal to filter the information. It tells you what to pay attention to. And so, if you look down here, we've got I want to make money. I want to make money

[32:33] online. I want to make, I want to make my first $1,000 online by editing Instagram reels for fitness influencers. That specificity now sorts all these informations out in your head. So, now

[32:44] you know exactly what to pay attention to because your goal is so specific. I'm not saying to go that specific, but it's just a principle. Next is finding ideas.

[32:53] And so you can observe what people say. So teachers, books, videos like this, podcasts, coaches, etc. It's easier for you, but it's less tested because you don't really know me. I could be yapping

[33:03] up a freaking storm right now and none of this could actually be useful to you. You don't know that. It's because you're just watching me say stuff. Or

[33:10] you can observe what people do. This is studying people who are winning. So if you wanted to like win on YouTube, you would study Mr. Beast instead of watching other people talk about how to win on YouTube. It's harder to do. It

[33:22] takes more effort from you, but it's more tested because you're actually watching people win. You know that they're winning and so you know there's some first principles there that are at play. And the last one is thinking in God. So God's given us the ability to

[33:34] create out of thin air in his image. So we don't have to steal from anybody. We can literally just create brand new things because he's the ultimate creator. He created us in his image. He

[33:43] loves us. He sent Jesus to die for us so that we can be with him and have relationship with him. And he gives us the ability to create brand new things that are just incredible. Problem is,

[33:53] this is hard. They're not tested at all. It requires a lot of solitude and it requires you to actually not consume stuff, but just sit down and just be solitary with God. But it has insane

[34:05] potential and it's mandatory to win big. And so all these things allow you to find ideas. Then you capture those either in a computer or a notebook or your brain. So external storage or

[34:16] internal storage. We won't go into depth about that. I have a whole second brain course in the free school. But

[34:20] that's how you capture ideas. Then you have to make a plan, a strategy. This is where AI really, really helps when it has context. This

[34:28] went from taking days to taking minutes. You got to think which ideas do I try first? What do I actually do? How do I

[34:33] do it? When do I do it? Where do I do it? Those are when you take these

[34:38] question marks, these like iffy ideas, and actually step on them to see if they work. And that's what you do. You test by doing. So you do your plan. Either it

[34:46] fails and the idea breaks and you fall and you look stupid and then you get back up and you do the same thing again and you do that again until it works and when you step on it it becomes green and you're like, "Whoa, okay, sweet. I

[35:04] figured out how to make a good thumbnail." Then you go to the next problem and the next problem and you keep failing and failing and failing until you figure out all the solutions and you eventually hit your goal. This is how you do

[35:11] it. So this is how to really 10x your productivity using AI because now you know what productivity is. Now you know how AI plays a part in this. You should

[35:22] be set to freaking change your life. So, let's move on to the next section. All right, let's go over how AI actually works because a lot of times we have no clue how this stuff works. And if we

[35:30] did, we'd be able to use it so much more effectively. And I'm going to explain it like a third grader, so lock in. No one explains stuff like this.

[35:42] There's probably a reason for that, but hopefully you guys enjoy. So AI is not a magic genie. Your parents, maybe you as well, think that like you just rub AI and it just like spawns a genie and he just grants all your wishes. But

[35:50] sometimes he's way off. That is not AI. I want you to view AI more as like a super nerd. He's an absolute turbo nerd.

[36:02] He's great at a couple things. And so he's great at sheer knowledge and info. So he knows a lot of things, but he doesn't know how to really apply them to the real world because he doesn't have that experience.

[36:12] He's been in his nerd cave his whole life. So he knows all the facts. He knows what an elephant should look like, but he's never like been near an elephant, right? He doesn't have the

[36:19] experience. And that'll make more sense in a little bit. Very smart, 500 IQ, right? Genius, but he doesn't have

[36:28] street smarts. He wouldn't survive in the real world. He knows the stuff, but he doesn't know the judgment of when to apply. He doesn't have taste. He's also

[36:35] very good at following direct orders. And so, he'll do whatever you say. Even if it's not the right thing, he'll just do it. What he's very bad at

[36:41] though is your personal context. So, he doesn't know you. He's not a good people person. He doesn't understand how people

[36:48] are going to react to things. He just knows random knowledge. He doesn't have very good long-term memory. And so, he

[36:56] doesn't really remember everything you talked about a couple days ago. He forgot it. He has a little bit of memory, but very bad long-term memory.

[37:19] Also, he doesn't have experience, so he doesn't understand nuances. And so this is getting a little complicated, but the way that AI works is it's trained across pretty much all human knowledge. And so when you ask it for something like, hey, I want you to give me an email, it will give you the standard deviation of what it thinks an email should look like. But

[37:31] let's say you're writing emails to like 18-year-olds for this one ecom product. They probably don't want the average boomer email. And so it's not good at doing very specific nuance things. It'll just

[37:43] give you the average. And so a good way to imagine this is let's say that we're going to get a little off script here. So this is like the average of all kind of outputs.

[37:52] Let's say you want a website. So you're like, "Hey, I want a website." AI has been trained on like all the websites in the freaking world. And so

[38:06] what it does is it takes all those websites and it just kind of gives you an amalgamation of like what it thinks a normal website landing page should look like. And so let's say you have all the colors. You have green, red, blue, yellow, all these things.

[38:16] It's trained on all of them. But because it's trained on all of them, it just puts out brown because it has all the colors mixed in. It just mixes them and it's like brown. But we'll learn how to

[38:34] use skills, how to use prompts to actually get these very highly tailored nuance solutions out of AI. So if it has all the colors there, but it always outputs brown, you might think that AI sucks and then it only gives brown websites that aren't good. But there's actually a bunch of good websites in there. You just have to prompt it and

[38:44] make sure that it's very specific that it gives you the pink and the colorful website or the yellow, the purple, the nice exquisite website. It's in there. It's in its knowledge. But if you

[38:49] just say, "Hey, give me a website." It will just mix them all up and give you brown. So hopefully that makes sense.

[38:55] It'll make more sense as you play with AI. But let's keep going. It is also bad at taste.

[39:05] AI doesn't have meaning. It doesn't have human perspective. So let's say AI tells you that the best fashion is to wear like apple bottom jeans. Well, it

[39:20] doesn't understand really trends. It does if someone tells it, but like it doesn't understand how things shift. It doesn't understand how why people would buy a thing called a pet rock and they would actually, this would be a million-dollar product, which it is, by the way. Look it up. Because humans just

[39:24] find meaning in things. They have experience. They've gone through pain. They have goals. They have

[39:37] failures. AI doesn't have that. And so whenever you're making something that people are going to consume, AI has a problem really understanding what a good output is because it doesn't have taste. And so

[39:45] this will evolve over time. I'm going to show you ways to make this better. But you have to always understand, you got to be thinking what are humans going to think whenever they see this thing. So

[39:52] AI is great at coding. It's great at this stuff. But when it comes to design, when it comes to things of taste, it doesn't have that. So you got to be good

[39:58] at that. Why am I even showing you this? I know we're going all over the place, but I promise all this is going to make you powerful with AI. This is why this

[40:22] is called the advanced section. I'm going a little bit deeper for this. Every tool that we're about to cover is an attempt to fix those problems. So, those things I just showed you, not having your personal context, not having long-term memory, not having nuances and how to do very specific things, not having taste, all the tools that we're about to cover in the next module are going to show you how to bridge this gap. Also, if you don't find AI very

[40:36] useful, it's because of those problems. And once you learn how to fix them using the tools, he will become your personal assistant super nerd wizard who will completely change your life. But this is why you have to understand these things first. When you understand why these

[40:49] tools exist is to fix these problems, you'll know how to use them better. So, without further ado, let's go learn exactly how to do that. All right, welcome to the most important module of this entire video or course that you're watching. How to access Claude's full

[40:55] power. This will put you ahead, I'm not kidding, of 99.9% of people. No one knows how to do this,

[41:08] but when you learn it, oh my gosh, the edge you're about to receive. Get a coffee, get a drink, get a freaking blanket, grab your cat, pet him, and lock in for 30 minutes because this could change your next 50 years. I'm not even exaggerating. I'm not

[41:13] playing. So, let's just get straight into it. So, we talked about the problem that most people have with AI. It's that

[41:34] they have this incredible robot, but he doesn't know anything. He doesn't see your problems. He just has his built-in knowledge and he kind of just runs with it versus giving him full context, giving him the tools he needs, giving him your entire like problems and goals and him going out and building the bridge that allows you to literally walk on and achieve all your goals ridiculously fast. How do we

[41:42] get that? Well, that comes by giving him the exact tools and context that he needs. That's what it's going to do. And

[41:58] so what I'm going to do is I'm going to explain every tool to you as simple as I can possibly make it and then give you exactly how to use these things to change your life. Now the cool part is I've already baked in a lot of this into the beginner section. So like you can use these things without knowing how to use them. But when you know how

[42:06] to use them, oh my gosh, you're going to unlock an insane amount of power. I mean that's the whole point of this module. So let's break them down one at a time.

[42:23] Starting with tokens. What I want you to understand is whenever someone talks about tokens, this is basically just words. And so the reason we have to pay for Claude is because there are computers somewhere in Narnia that run all of these things for us. And every single

[42:31] word that they compute costs money. It costs computing power. It costs energy. And so you pay for like tokens

[42:39] or if you pay monthly, you get a certain amount of tokens every five hours. And they're just basically words. Just understand them as words or pieces of words or numbers. It's just

[42:46] information. And so that's what I want you to keep in mind. Now, your context window. So, this is whenever you

[42:56] spawn into Claude and you basically start a new conversation. Every conversation is what's called a context window. So, Claude has all the context for this conversation in this window. I

[43:12] want you to view this as Claude's whiteboard. So, every time you start a new context window, he has a fresh whiteboard. And so you have to plug in what he needs to know, but you also have to leave space for him to actually work on the whiteboard. And

[43:19] every time you finish working, guess what? You wipe it clean. This is like the best analogy that I can know to kind of show you every conversation. And so

[43:30] if you ever used like Claude and you're like, "Man, he just forgot everything from yesterday." It's because he cleaned off the whiteboard. He needed more space to work. And the more that he fills up his context window, the worse everything gets. And so when you're at like 90% of context use and you only have this much left, Claude's going to be pretty bad because he's got so much information in his brain that he's having a hard time focusing because all this is in his conscious memory. And so every chat within your agent has a token limit. And so this is how much that the

[43:55] AI can keep in mind at one point. So it's like how much can it keep at the front of its brain at that time. And so they actually just increased this with Opus to 1 million, but if you're using Claude, it probably has 1 million context limit. But you want to keep

[44:10] it as low as possible. You don't ever really want to hit that 1 million. You want to keep it under 500K mostly and then just start a new chat when you want to do something else.

[44:18] Like I said, this will all make sense over time. So just imagine Claude having a whiteboard. Next we have markdown files. So all a

[44:27] markdown file is on your computer is just text. It's a very simple text document that Claude can use to read super easily. So this is giving him like custom context. It's just a text

[44:39] file. That's it. And so Claude can read and write these files super fast. So, I want you to

[44:45] imagine that these markdown files are kind of like a file that you would give him out of a filing cabinet. And so, if you say, "All right, Claude, here's this markdown file on how to cook eggs." You give him that information. He then loads

[44:59] that into his context window. And now he can go and cook eggs because he knows how to do it. You gave him the right context. So, we'll keep going.

[45:10] Front matter, YAML front matter. So what this is is basically a little tag on the file. And so if you got a big filing cabinet, you don't want to read all those files at once just to figure out where the file you need is. Instead,

[45:23] you have little tabs. This is what front matter is. And so on each markdown file, there is a bit called YAML front matter, which then tells Claude exactly the context he needs to know whether to pull that file or not. So if we look over

[45:38] here, if we don't have front matter, Claude has to load in every single thing. So if we're going to make content and let's say that we want to make an Instagram post, but because he doesn't have front matter, he loads in all the context around content. So now he's got YouTube, he's got Instagram, he's got LinkedIn, he's filling up his context window and he's confused. So it

[46:00] leads to a bad output. But when you have front matter and you see on the front matter that this file says right here, you know, this is for Instagram. So whenever KJ wants to make an Instagram post, pull this file. And the other one has YouTube on it. So it's like it says

[46:14] for YouTube, he knows, okay, I'm going to pull the YouTube one since we're doing YouTube and I'm not going to pull the Instagram one, thereby saving all this context, keeping things cleaner. And Claude is like, "Okay, I know what to do. Perfect." And so that's why markdown files are so important. That's why front

[46:31] matter is so important is because without front matter you have to load in everything. But with front matter, you can just load in the front matter. So he's like, "Okay, I have one for Instagram, one for YouTube. KJ wants

[46:41] YouTube. Let's pull the full YouTube context and let's make it." So pretty cool. Now, moving on.

[46:48] We have folders. And so a folder is essentially a filing cabinet. So each folder is a cabinet that holds all of these files. Pretty cool. And so it's

[46:59] full of markdown files with the front matter for AI to thumb through. And so you give him this entire cabinet that could be called content. Inside content, he has your voice file, he has the Instagram file, he has LinkedIn file, he has like examples there. He can go and

[47:15] pull those out whenever he needs those to do what he wants. So if you say, "All right, Claude, let's write an email." He pulls out the email thing and he's like, "Okay, I want email context one, two, and three. I will pull those folders by

[47:27] looking at their front matter. I will bring them into my context and now I'm ready to write you an email." Magical.

[47:33] It's super cool. When you understand this, everything starts to click. It's really awesome. Now, skills. Let's

[47:39] talk about skills. And we'll go into depth on skills later. We'll actually build some out. But what I want you to

[47:45] understand is that a skill is just a markdown file. So, the way that Claude has programmed it is skills can actually be loaded into your Claude window, but all that they really are is just a special markdown file. And so, it allows you to see it in your Claude app, but all it is is just another markdown.

[48:03] It's instructions of how to do stuff. It's an SOP. It's context. It's scripts.

[48:07] Like I said, we'll go over this later, but all you have to know is that it's just a special context file that tells Claude how to do something. And you can load those into your actual app and see them here and turn them off and on, which is why they are called skills. That's why they're different than just a normal markdown, but they do the same thing. Next we have claude.md.

[48:27] So, the way that claude.md works is this is a special markdown file that is loaded in every single chat. And so, this is like my actual markdown file for my second brain, which you guys have if you use the plugin. It creates this

[48:42] for you. But it just tells Claude who I am. It tells him the structure of the folders that we're working in. It tells

[48:48] him my active projects. It just tells him everything he needs to know before we get started before every chat. And so it's amazing. And so this is basically

[48:56] like a very special golden markdown file that gets loaded every single time. So every time you open a new chat, this claude.md is now recognized. And so without getting too complicated, you have a global Claude file which is basically anywhere that you use Claude.

[49:13] It has like very basic stuff like what your name is, your preferences of how it talks to you, all that kind of stuff. But then you also have local Claude files. And so let's say that I want to bring Claude into my content system folder. So I have a folder called

[49:27] content system and I click on it. I can have a claude.md in that content system folder which explains where like how everything is laid out. So, how my

[49:37] content system works, how everything happens. And like I said, I'll explain all this in the future because I actually have these examples to show you guys later, but we're just going to stick with the theory for now. So, you can have a claude.md for each folder.

[49:47] So, basically, you can have one for every single folder that tells it what that folder is, what its job is in this folder, all that good stuff. So pretty cool. Next, we have plugins. So,

[49:58] Claude or Anthropic is always changing like plugins, commands, like skills, but essentially all a plugin is is just a bunch of skills and commands together. And so, if you got a bunch of skills when it comes to making this one thing, let's say you're going to make a YouTube video. You can have a plugin which then has finding the idea, helping with the thumbnail. It

[50:19] has all these separate skills batched together under this one goal. So, it's kind of like a meta-skill. It's a bunch of skills packaged together. And

[50:29] so the plugin I gave you guys in this course was my starter pack which has the end of the day skill, the good morning skill, the help, the new project, and the setup skill. And this is just an easy way to package it. That's really all it is. Now,

[50:43] MCP server, the easiest way to explain this, and you guys can dive deeper by asking Claude these things, but it's like plugging your Claude into a USB port on an application. So let's say that Figma has an MCP server. So without this server, Claude doesn't know how to use it. But with this server, it

[51:03] basically gives Claude an ability to plug in to its USB port, use this machine called Figma, and it also gives it instructions on how to actually use it. That's really it. MCP server just allows you to connect Claude to other apps. That's it. Now, API keys. This is

[51:20] where things get a little bit more complicated, but API keys basically allow Claude to have access to different applications where it can just pull stuff. So, it's kind of similar to an MCP server, but it gives it direct access to the app. It has its own key.

[51:38] And so, you want to keep these things private, but Claude will do this. We're not going to go into details here, but just know that an API key is like a room key. It's like if you want to go to the Google room and access all of Google's stuff, you have to have the Google API key. And so you want to keep

[51:52] these things private, keep them secret. It's like your password. It's like Claude's password to access these different things. And so you'll get an

[51:59] API key for each different application that you want to use. So also you can actually get an API key to use Claude. And so in the app that I'm building, we use Claude on the back end. And so we

[52:13] have an API key that the app uses to access Claude's functionality and to use his knowledge. So not too important for beginners but just know you can come back to this if you need to understand it later. Now what is Obsidian? Obsidian

[52:27] is not necessary but I find it very very useful. It's basically an app that allows you to view markdown files and edit them really cleanly. And so here's what Obsidian looks like. Here's

[52:38] what my Obsidian looks like. And I go over this in my free school of course. Check it out

[52:43] if you want to learn all this. But this is my Obsidian and I'm able to see all these files really easily and Claude can see them easily. So this is what the files actually are.

[52:52] They're just simple markdowns, but Obsidian makes it look like Notion. Makes it look super clean for my eyes. And so now me and Claude can both work in the same filing cabinet. And so he

[53:02] can have easy files to see and read. I can have easy files to see and read. It's the same exact files. I just like

[53:08] it a lot. Now integrated development environments, IDEs, also Antigravity. This is one of the same things. This is

[53:16] similar to kind of Obsidian. It allows you to see your folders and see all the things laid out. So, this is the same exact file that we're looking at up here in the same exact folder, but it just allows you to have Claude Code there with it. And so, it's a

[53:31] little bit more advanced, but definitely check that out if you want to dive a little bit deeper. It's all the same thing though, guys. You're still just using Claude Code to do stuff on your computer, but it's just different ways to view it. It's kind of

[53:43] like Obsidian, but on steroids for coders. It's kind of like Microsoft Word or Google Docs, but for code. So, as Google Docs allows you to easily see and edit text, this is what Antigravity does. It

[53:57] allows you to easily see and edit code with Claude Code. So, anyways, so putting it all together, where are we going with this? I know this is a lot of technical stuff, but like I just feel bad if I didn't show you this because I wish someone taught me all this this simply.

[54:11] When we put it together, this is what makes Claude powerful. So, he loads his claude.md first. He also loads in the skill front matter. So, any skills that

[54:18] you've like enabled in Claude, he loads in the name of the skill and what they do. That way, anytime that he needs those skills, he can just go pull out the file. And then you give him a filing cabinet. And so, the filing cabinet is

[54:30] the folder that he's working in. And this includes context. It includes skills. It includes pictures, videos,

[54:35] whatever you want to give Claude to work with. You give him access to the folder. Now, he only pulls it when he needs it.

[54:43] And so, he pulls out these files as he needs them as you're working on something. And so, if we go back to my second brain here, I'll tell him, "Hey, Claude, I need to write an email today." And so, he won't pull in all this stuff about my master class or my school or my speaking progress or my app. He will just go to the

[55:02] email folder because we're working on emails. And so that allows him to keep the context super clean. Then if he needs an API key, like I will give him an API key and he'll save it and he can go access Google. So if he needs to go

[55:15] access like my YouTube stuff, I give him that key and now he can upload to my YouTube. And so anytime that he needs something, he'll go to the cabinet, he will read it, he'll write it, he'll pull out what he needs. That way he gets insane results without bloated context.

[55:29] He avoids context rot and you actually get the niche nuance epic stuff done that you want to accomplish. And like I said, I'll go over tons of examples here in a minute, but this is just the theory. And then now that we have Obsidian, it allows us to easily view this filing cabinet. We can add plugins

[55:46] to this. We can change the theme. It just makes it fun for the human experience. So that is why all this

[55:51] comes together to take Claude into a superhuman being. So super robot being. This is how you unlock Claude superpowers. But now, let's get

[55:59] into actually like how this stuff works and how you actually use it. I know this was a lot of theory, but hopefully just re-watch this anytime you don't understand things and you're going to be way ahead of everyone. I promise it's so worth it. So, let's

[56:12] move on to the next module. All right. Now, let's build our first basic skill in Claude. This is going to be super fun.

[56:18] I'm going to lay this out on Miro, then we're actually going to jump in Claude and do it. So first thing I want you to do is analyze what is something small and annoying that you do manually every day or every week on your computer. So in my instance it could be transcribing coaching calls, uploading videos to YouTube, updating my finances, doing market research. What is something

[56:37] you do every single day, every single week? Then what I want you to do is list out the outcome that you want with examples and then write down the normal process that you follow to actually accomplish this. And now you just have Claude do it, you refine it, save it as a skill. So let's go do this right now.

[56:54] All right. So the first thing I've done is I've gone into Claude Co-work and I'm basically just going to select the folder that I'm working in. So you want to select the folder that you've set up your Claude Co-work in or just make a new folder and I'm going to like start making the skills. So I'm just going to

[57:06] kind of tell him what I want and we're going to get started. All right, Claude. So I have a school group. As you

[57:12] know from my second brain, I have a school community and in that school community I do weekly calls where I just chat with people who have paid the premium just to come talk to me and hang out. But what I want to do is I want to transcribe those calls. And then I want to actually build a little timestamps in the description where it makes it easy for my viewers to go back, re-watch the calls, find the subjects that they're interested in, click on the timestamp, and then just watch it. And

[57:37] then I want to create this into a skill once we've done it once and we have it refined. So I'm going to do that. And then I'm just going to say any questions. I just

[57:45] like to add this on. They actually do this automatically now, but I'm so used to just saying do you have any questions because I want it to really know what's going on. So now we're going

[57:54] to wait and see what bro can cook up. So I will pause it and be right back. All right. So he's going to ask us some

[58:01] questions. Where do these raw recordings live? I'm going to say local files because that's usually where they are. How long are they? We're going to say

[58:08] 30-60 minutes. Where do you want the final time stamps to end up? We'll do a school post and description. Cool. And we will let

[58:17] him think up with those new. All right. Now, we have some more questions. For

[58:21] the transcription step, are using local tool like Whisper or do you have a preferred method? I'm going to say whatever you recommend because I really don't have anything. All right. What

[58:30] format do you want the time stamps in? I think it's simple timestamps. Yeah, we'll just do simple. Cool. And now he's

[58:37] going to keep cooking up. This is the magic part, guys. Like, you don't have to really know how to even do what you're trying to do. He will guide you

[58:43] through it. It's just incredible. And this is a very simple skill. I know this isn't like

[58:47] groundbreaking, but when you learn how to make the simple ones, it's going to make doing the advanced one here in a minute a lot easier. So, let's see what he said. All right. Local file, Whisper

[58:56] transcription. Claude identifies topics, cleans timestamps. Whisper running locally, free, accurate. Okay, I love that. Let me get the environment set up then we'll run a real call. So now he's just doing this stuff. All right, let's see what he says. He says here's what we're building, local file Whisper transcription, Claude identifies topics, clean timestamps for school post. Cool. All right, Whisper ready to go. Test file to run a recording? Let's see. I've created a folder inside of my school folder which is called coaching calls and in there is an MP4 file ready for you to use. All right, cool. So that's what I did. I just made

[59:33] a folder, dropped the recording in and now let's see what bro cooks up. All right, he says got it. Motion 11 coaching call about 62 minutes. I'll extract the audio first. Okay, cool.

[59:51] And Claude gets better over time, guys. I've only been using this for about a month now. And it's already improved dramatically just since I've been using it. Normally it doesn't go like this

[1:00:04] smoothly. I guess it does nowadays, but it'll solve the problems for itself. It's actually just insane. Like all you

[1:00:11] really have to do is clarify your goals and make sure you know what you want and he can get you there. It's insane. All right, he's going to use that. I'll let you know when he's done

[1:00:23] and actually has something good. Also, something to mention while he's working on this. You can always see the progress of what he's doing off the top right.

[1:00:31] And so, you can kind of like ask a question or recommend a change. I actually just noticed this. Wow, that's amazing. So, yeah, you can see

[1:00:37] the progress up there. You can see like where the folders he's working on and what he's loaded into his context. And so right now it's pretty clean since this is a new project, but you can see where we talk about the claude.md, which we already discussed. He reads the

[1:00:50] claude.md of this folder every single time. So he's already got that loaded in. And yeah, now he's just going to go through the process and we'll see what he cooks up. All right, welcome to

[1:00:59] the live process of building skills. It was taking a while and so I was like, what if we just uploaded this to Loom instead and I just paste the transcript here, which you could do with YouTube or whatever. And it was like dope, that sounds way faster than having to do it on computer. So I'm like awesome,

[1:01:15] we'll do that. Then I'll just use the Loom to actually put that in the school. So, get two birds with one stone. All

[1:01:20] right, I'm going to post the transcription. Now, we'll see what it does. All right, so let's just control-V.

[1:01:25] There's the entire transcription. Now, we will see how bro does with that. And after this, I show you guys a really freaking cool skill after this just to kind of show you the level you can take this to. I know this is basic,

[1:01:39] and for the purpose of teaching you a basic skill, this is like a good explanation, but I'm going to show you something wild that I used to even make this video. So, I'll show you guys that after this. It'll be a little

[1:01:48] treat, but let's finish up this skill and see what it does with this. All right, so here are the timestamps. We've got intro, school setup, why I ditched Obsidian for Miro, Cowork master class, can AI write good copy,

[1:02:05] Bonco principal, live walkthrough. All right. Anything you'd resume, cut, or add? You happy with the format, we'll lock it in. So I would say that each timestamp needs its own line so that it's formatted clean and it's easy to read. And can we make sure that these

[1:02:20] bullet points are kind of positioned as a benefit for the viewer to watch it. And so let's just make them seem very beneficial. All right. So now we'll just refine this

[1:02:31] a little bit and see what bro does. Cool. And this is the process of making a skill. It's just iterative. And every

[1:02:38] time that you run the skill, you can also change it up as well. And so you can like iterate the skill as you run it every single time and make little incremental changes. All right. So cool.

[1:02:49] Once you're happy, locking this format and building the skill. So I'm going to like copy and paste this into the school and we're going to see if it actually works. Okay. So pasting this in

[1:02:59] the school, it did not work. I want every single timestamp to have a line break after every single bullet. So let's take this back and bring this back into Claude and we will say just that.

[1:03:12] So I was not able to copy and paste this into the school correctly. The formatting is still off. Every single timestamp needs to have its own line.

[1:03:20] Does that make sense? So let me ask it that and we'll let it cook. So this is kind of the process. It's

[1:03:27] very simple. You just have an output that you want and you keep working with Claude. Give it screenshots, give it advice, suggest other things, and then once you get it right, it'll be good to go.

[1:03:36] And so now what it's doing is it's putting this in a text file so that I can copy this really cleanly. So that's how it's problem solving. It's thinking about how to get around this. And so

[1:03:46] let's see what bro actually does. We'll just keep rolling here. All right. So

[1:03:51] now he has a text document. So I will copy this. I wonder if I can copy it there. I'll copy it right here. I'll go

[1:03:57] back to the school and I will say plop. Boom. There we go. And so now we have

[1:04:03] some pretty good stuff here. I'm going to read through these and see if I like this. Why I can't write copy? What's

[1:04:08] missing? Why AI is in every title I publish? How to tell? Okay, so I don't love this.

[1:04:16] Let me actually go back. Okay, I want you to disregard what I said about making it beneficial. I don't want it to seem like a YouTube title where it's actually hiding the thing that I'm talking about. So basically,

[1:04:30] how to tell if you're building the wrong market. I don't want that to be a bullet. I want you to actually talk about the framework or explain the framework a little bit. So yeah. All

[1:04:40] right. So this is terrible prompting since I'm recording on video and I'm just trying to get this done. But we're going to see how good AI is. Let's

[1:04:46] see if it can actually do it. So less clickbait, more substance. Perfect.

[1:04:50] That's exactly what I wanted to say in less words. So, let's see if it changes it up. And what's cool is as it's building the skill out, it'll save all those instructions that you've given it for this output and you don't have to tell it that ever again. It'll already

[1:05:04] know. That's how it's building the skill. That's why the skill is so important. And this is also going

[1:05:09] back to what we talked about with the kind of why you make skills is I want my transcripts to look a certain way for my stuff and my audience. And so it's giving me transcripts based on how it thinks that everybody wants transcripts. But what if I want something a little bit different? And it's doing that for

[1:05:27] me. And so now we're actually going to copy this and we'll check it out. So I'm going to copy this and we will paste it in. Shout out to the gang who was on

[1:05:37] that call. Okay cool. So thinking before prompting, co-work master class, he can write, AI has no taste. The guy

[1:05:45] behind. Okay, live screen share. Okay, I'm going to give it some more feedback.

[1:05:54] Okay, so this is better in terms of not being clickbait, but they're all way too long. Let's make it where every single summary or every single point is around, let's say, 10 to 15 words max and keep it super simple and concise. All right, so we'll do that. We'll go

[1:06:13] back and forth and I'm going to keep going back and forth until I get something that I like. Hopefully this is it. So yeah, I'm going to pause it until we get something. I'll let you

[1:06:21] guys know. Okay, it turns out that that one was the one. I'm pretty sure. So, I'm

[1:06:25] going to copy this and I'm going to paste this in and we're going to see if these timestamps actually work. Okay, cool. Most people skip straight to AI. Why every publish has AI in it?

[1:06:39] Cool. Dope. Well, I like that. So, we're just

[1:06:42] going to save that and we're going to make this into a skill. So, let's actually save and then we'll go back and we will do this. I'll say, "All right, looks great. Let's make this into a skill that

[1:06:54] I can use every time I have a coaching call." Cool. Now, what he's going to do is he's just going to go through and create this process into a skill that he will follow every single time that I say, "Hey, let's transcribe a coaching call." And

[1:07:07] then I'll show you what the actual skill looks like whenever he builds it. All right. So this is a skill that he's capturing. So the trigger is when I say

[1:07:14] I want to do some coaching call transcripts. Input is a Loom transcript. The process is to identify the topic shifts, write a clear label. Output is a

[1:07:21] text file. Style rules and yeah, he's going to do it. And so like I said, as you do these over time, you want to iterate the skill and make it closer and closer to what you want and just refine it. Now it's writing the skill.md file.

[1:07:35] So it's just a simple markdown with instructions of how to do this. And the trigger is what's going to be in the front matter so it knows when to actually pull this file. That's what the trigger is. And then I should be able to

[1:07:45] actually show you guys the skill.md and we can take a look at it and suggest edits. I highly recommend that you always edit the skill.md after like

[1:07:56] reading it, going through it because sometimes AI will put in stuff that you didn't really want in there or it might perceive something wrong. It didn't understand it correctly. And so the best way to do this is to actually read this skill for yourself and then tell it what to fix. And so what it

[1:08:14] does, it reads this. Show output. Right on your — we've already tested the skill. So let's just go ahead and install it. But can you pull up the skill on the right hand side so that I can actually read it? Cool.

[1:08:31] And so we will see what he does. All right, he's producing the file. Bet. So

[1:08:37] here we have the skill. So this is the actual skill thing. What you can do is you can copy it to your skills and you're good to go. And so what you're

[1:08:44] going to receive is how to identify. This is all the instructions that it's going to give itself. And so what I recommend you guys do every time for your skills is just skim through it.

[1:08:52] Make sure everything is correct. If it's not correct, all you do is just say, "Hey, go fix this." And it'll fix it.

[1:08:58] You don't have to type anything. You don't have to work on it. It's just amazing. So, that's your first skill.

[1:09:02] Now, let me actually pull up an insane fully built out skill output just so you guys can see the power. All right, this is an output of one of my special skills, which I will make a course on for free in my school at some point, but right now I'm just keeping it to myself and testing it. But what I did is I created a skill that basically validates a YouTube idea in the market and it does everything. So, let me run

[1:09:24] you through this. This is an output of one of the skills I've created. So, this is kind of the final thing that the skill brings out. It's got me all of the

[1:09:30] competitor video analysis for the idea that I have. So, this idea that I had is like basically making a video about how to build a full second brain system with Claude Code and Obsidian. So, if you want that, leave a like, leave a comment. And it gives me all these competitor thumbnails, their titles, it gives me their views to sub ratio. So,

[1:09:49] some of these guys got a ton of views, but they have a ton of subs. So, it basically, it's probably less important than these that have the green ones. I told it how to format all this. I told

[1:09:58] it how like what colors to use. Really really cool. Then it gives me packaging pattern analysis. So what are

[1:10:05] the patterns from the thumbnails that it's viewing? What are the title patterns that it sees? What things are standing out about these? Then it

[1:10:13] analyzes the intros. I don't have the transcript data in here, but normally it analyzes the first 90 seconds of every video. And then we got market takeaways and strategic direction. And

[1:10:23] so this analyzes real trend data of should I make this video? So are people searching for the topics in this video? Then it gives me a verdict. Should I make the video or should I not? And it

[1:10:34] gives me why. Then it gives me the recommended angle to use for the video. Then it gives me title building blocks.

[1:10:40] So what are the actual keywords I should use in the title. Then it gives me 10 full title ideas. Then it gives me thumbnail building blocks. And

[1:10:47] it gives me gaps to exploit with the video. It gives me video tags and it gives me like discovery tags. It's just sick. It does all this in

[1:10:56] one skill and it's done in five minutes. It's wild. This is like the full power of a fully built out skill. So, I

[1:11:02] hope you guys see the value in that. But the best value in skills are using them in your personal life, not downloading other people's skills or finding stuff online, but what are problems that you have that you can solve with AI and repeatably solve it with a skill. That's where they get very valuable. All right, so let's move on to

[1:11:19] the next module. We're going to create some advanced systems using multiple skills. All right, let's take what we did with the skills and go freaking crazy with it. Let's build entire

[1:11:27] systems to hit those goals that you want by having AI do freaking everything almost. So, this is AI system design on crack. So, there are four secrets to incredible AI outputs. This is what if

[1:11:39] people aren't getting good outputs with AI, it's because you're missing one, two, three, or all four of these keys. Let's go over how to not do that. So key number one is your Claude agent needs to only have context for the exact output you want. No less, no more. So if

[1:11:56] you give him too much context, if you tell him how to do YouTube, how to do your emails, your LinkedIn, how to wash your laundry, and your schedule for the day, and you're giving him all this stuff just so you can write an email, he has too much context. The output you want is just an email. You don't care about all those things. And

[1:12:13] so you want him to just have what he needs for that occasion. And so let's say now he has just the context he needs for an email. He has

[1:12:29] the type of email he needs to write. He has the claude.md and he has all this space to go work. That's good stuff. So

[1:12:36] this is also why we spawn multiple agents, so sub-agents for different parts of the process. We'll go over that later. But just remember, whatever you're trying to do, he doesn't need to know your entire life story if you just need him to do this one thing correctly.

[1:12:48] He just needs what he needs for that one thing. The good example is if you're trying to make a pizza, you don't need an entire pantry of a million ingredients and give that all to him on his workstation at the same time. So, he has to sift through all these vegetables and candy just to get to the stuff he needs for the pizza. Just give him the

[1:13:05] ingredients that he needs for that one output. You can have a pantry which is your, you know, second brain where you have all the ingredients stored for later, but don't give it to him in the kitchen at the same time if he's cooking. Now, key number two, better inputs, better outputs. So, keeping

[1:13:19] along with the same kind of theme here, if Gordon Ramsay was given moldy tomatoes, moldy cheese, stale bread, his pizza would be bad. No matter how good of a cook he is, the pizza would suck. But if you give him world-class ingredients to a great chef, then it's going to have an amazing output. Same

[1:13:36] thing here. If you give bad customer research, bad examples, bad skills, bad rules, you're going to get bad output. So, in this case, bad copy, bad emails, whatever. But if you have great customer

[1:13:47] research, great examples, concise skills, and a great process, really good on-par rules, then you're going to get great copy. So, remember that. Better inputs, better outputs. Now,

[1:13:57] human checkpoints and feedback. So, most people, they get lazy. As soon as they hear the word AI, they're like, "All right, I'm never doing anything again.

[1:14:05] YOLO robo, just send it." And Claude is smart. They know that if you want this, they will give it to you. So in most

[1:14:11] cases, at least it used to be really bad like this, the robot will just one-shot everything because he knows you don't want to do work. It always leads to a very bad output because you need checkpoints. You need feedback. So

[1:14:23] instead, the best way to do this is to have him say, "What do you think, Mr. KJ?" And I'll be like, "Add this." He's

[1:14:28] like, "What about now?" And I'm like, "Change that a little bit." "How's this, KJ, sir?" "Try this." And that's how you

[1:14:33] get a great output, a great piece of copy. So this is key number three, human checkpoints. And key number four is frequent iteration through doing. So like we talked about,

[1:14:43] the goal is to have a skill that is not too restrictive for Claude, but it gives him all these things not to do and then lets him just go and have creative freedom on the rest of it. And so you find those things of what not to do by running the skill, by doing it over and over and over again and frequently telling him how he should change. And so in this case, writing emails, I want him to write the emails, I'll review it, and then I'll improve the inputs. I'll

[1:15:09] improve the skills. I'll improve the recipes. I'll improve the examples. I'll

[1:15:14] improve the script. And then he'll write it again. And I'll do the same thing again and again and again, getting better and better outputs every single time. So let's get tactical. How do we

[1:15:22] take all these keys and make it into a very advanced system with multiple skills to actually generate money? So, let's do this. And something I want you guys to understand is I don't make my money by making these videos. I'm not a

[1:15:36] professional. This is my first video on AI. I make my money by using AI. So,

[1:15:39] this system I'm about to show you makes me multiple thousand dollars per month. And it literally gets rid of 90% of the work that I used to have to do. This is real amazing stuff. This is real

[1:15:49] value. So, I hope you guys enjoy. This is my email system 2.0 and I'll make an

[1:15:54] entire free course in my school. It just, it's going to go in depth. So I'm going to have to save that for a whole different video than this. But we will overview this so

[1:16:00] that you understand how to make these kind of systems. So the first thing we do is we have Claude with his claude.md. So he knows if he's working in this folder that I'm writing emails and he knows who my client is. He knows a

[1:16:12] little bit about my client and he knows what skills that he needs to accomplish these goals whenever I'm ready to write an email. So, I will say, "You know what, Claude? Give me some email ideas."

[1:16:21] And if I have an idea, I'll kind of tell him what type of email I kind of want him to do. Then, what he will do is he will run the email idea skill. So, when he runs the skill, what he'll do is he will pull in the general context about my client and he will pull in my client's past content scripts condensed.

[1:16:40] So, now he has everything he needs to find good ideas. I also give him the ability to search the web. So included in this is the ability to like go search the web and stuff. So this is kind of

[1:16:50] what he does. So at this point, we're just trying to get the idea. So keep in mind my 1.0 version of the system. I

[1:16:57] wasn't paying respect to the key of giving him just what he needs. So I used to have him find the idea, go through six different types of emails just to get this one output of emails. And I realized you know what I can have a skill just for the ideas which gives me better ideas which then becomes the input to the actual email skill which gives me a better output from there. And

[1:17:17] so this is how I get really really good outputs is by separating the task to give them just what they need. So for the ideas all that he needs is the skill. So you guys can see the skill here. Once again it's in the school if

[1:17:29] you want to download it. And then I give him ingredients. So the skill is the recipe and these are the ingredients. I

[1:17:34] basically will say here's Nick's general context. This is about Nick and I've made it as concise as possible. I basically asked AI like, "Hey, condense all of his market research into like two pages." And that's what he did.

[1:17:46] And then I give him past content scripts. And so these are like 90 ideas that I had him make based on hundreds of pages of transcripts from content. So I scraped the transcripts, but instead of giving him a freaking textbook of context, I had a past AI agent. So, I

[1:18:02] just opened up chat and was like, "Hey, give me all of the big ideas from all these content. Give it to me in two pages." And so, that's what he did. And

[1:18:10] so, now I have tons of bullets for ideas that he can use to make an email idea. So, that's what we do. And so, this is the input, right? This is the input that

[1:18:19] I give him. I give him the skill and I give him all his context and he comes out with 15 ballin ideas. Here's where we have human feedback. Checkpoint

[1:18:27] number one. I say, "All right, I like idea number four." And I will even give some thoughts on how to improve the idea or some points that we could add to it.

[1:18:35] Then he will run the valuable insight email skill. So I have a skill for each type of email. Just like I said, you only want to give it what it needs for that output. So if I'm only writing a

[1:18:49] one type of email, I want to give him just the skill for that type. And so now what I can do instead of having a skill that is kind of bad at writing all different types, I can have really good skills for each different type of email. So for sales, promotion, valuable insight, for a story email. And so I

[1:19:07] choose what skill I want to run. I tell him to run it. He then pulls in the context he needs. And so in this case,

[1:19:13] he already has this context loaded into his chat from the original kind of idea skill. And then he now has this valuable insight email skill where he goes through and he follows this process of me and him writing an email and it's really cool. And he also has other contexts of like past good emails.

[1:19:29] You can read through this, like I said, it's downloadable in the school but pretty cool. So now what we do is he runs the skill and he'll ask me some questions. He'll be like what's the kind of idea that we're using which he already knows because we taught him that. But also what's the value? Am I

[1:19:44] giving — is this a lesson? Are we giving them a framework? Am I giving them a resource? And whatever my client wants to do, I will basically say we're going to send them to this video and so I want you to like CTA them to book a call. Then he will use the skill. He'll

[1:19:58] use the idea, the inputs, and he will create draft number one. So this is the first output. I will then — inside the skill he spawns a sub-agent with instructions to review the email. So

[1:20:09] this sub-agent is powerful because of the principle we talked about where he doesn't have any of the prior context. All he has — he's brand new. He has a clean whiteboard and he has instructions of what a good email should look like.

[1:20:22] He's not biased because he didn't write it. And so then he will review the email and then give me a finished draft. I will also add some thoughts in myself and then we are done. I'll make the

[1:20:32] finishing touches and we ship the email. And I know this looks complicated, but I want you guys to remember that Claude made this entire process. Like he does all of it. I didn't make any of these

[1:20:41] resources. I just walked through it with him, gave him my thoughts, and we created something epic. And like I said, this makes me $2,000 every month. It's

[1:20:48] just insane. And so, how do you build this for your stuff? All right. How do

[1:20:51] you build this? First is get good examples of what a good output looks like. And so, if I'm going to make a valuable email skill or if I want to have a good YouTube idea, I need to have examples of what those good things look like. Then, you give it your process if

[1:21:05] you have one. And so, it'll suggest improvements. And you don't want to get too strict. You don't want to give it a

[1:21:10] tight recipe where it can only do one thing and it can't be creative, but you want to give it your rough process. Then you want to design your context. Don't give him 150

[1:21:21] pages of random slop. Take those pages, distill it into just what he needs into a couple pages, and then make that the context that he uses every time. You can ask it to help on this. Then you

[1:21:33] want to run the skill and test it. Iterate it at least twice. Read through the skill carefully. So like pull up the

[1:21:39] skill in Claude co-work and read through it, make sure everything is good. And then you're good to go. And so examples would be I gave him emails that I had written that had performed well. I told

[1:21:49] him my process of how I normally write emails manually. Then I gave him context for every single email and specific ones for each skill. And that's it. So

[1:21:58] this is like I want to show you guys the raw thing. This is the exact Miro board that I did while I made this skill. So, this was me like planning this out, going through iterations. This was me going

[1:22:09] through the creation process. So, like I just documented everything that I was telling it as I made the skill. And so, I'm not going to make this for you live because, you know, you're not in my situation. You're not writing emails for

[1:22:19] Nick. But, it's more about you learning the framework of how to make these systems and how to think through it. And once again, it all comes back to knowing these keys, right? Knowing how Claude

[1:22:29] works allows you to use him in a way that is super valuable to you. So yeah, like I said, I have a full course on that exact email system if you want to dive deeper, but this will give you a deeper understanding than literally freaking anybody right now. So yeah, let's move on to the last module. This

[1:22:44] one's very special. So let's go do it. Hope you guys are enjoying it. All

[1:22:47] right, let's go over how to get ahead of 99% of people. These are some tips that I don't see anyone talk about, but have been vital to AI changing my life. So let's start with number one. Building

[1:23:00] with AI is a skill. So, learning how to use this brand new technology is a new skill. You were starting over from zero hours and you have to basically speedrun to as many hours using this thing before anyone else. That's how you get ahead.

[1:23:15] This is brand new stuff that no one knows how to fully use. New stuff is coming out every single day of people learning this. This is exciting as crap, but you have to understand that this is a brand new skill. It's like learning

[1:23:26] how to be productive all over again because the landscape changed. So don't get discouraged and also be encouraged to know that like ask AI what to ask AI. Like that's what I mean by this. Like

[1:23:38] this is a whole new way to think about life. Instead of going to YouTube or going to other people or going to whatever like you can ask the tool how to use the tool. It's wild. There's

[1:23:47] never been anything like this in history. And so it's going to take time to get used to. So the point of this is just to use it. Don't sit here watching

[1:23:54] these videos all day. Go use it. Go ask it what to do. Go get creative. Just

[1:23:59] build random stuff because you need hours with the tool that'll get you ahead. Number two, the goal isn't to automate everything. It's to automate what a human shouldn't ever have to do. It's to automate what

[1:24:13] you don't enjoy doing. And so if you see these Miro boards, I did all of this by hand. Why? Because I think it is an art.

[1:24:21] I enjoy doing it. I live to make these Miro boards. I don't want to automate these things to AI. I want to

[1:24:28] automate all this boring crap like scheduling and uploading and all this stuff so that I can do more of the Miro stuff. So, I don't want you to fall in the trap of like just becoming someone who tries to automate their entire life because you're going to lose the joy of it. God created us to work. Like work is

[1:24:43] a good thing. AI is just an amazing gift that allows us to work on the things that we actually want to work on for once. Like Caleb, my editor, he used to have to go through and cut up every single little clip, every single take that I messed up. But now he has AI

[1:24:58] which can automatically cut all the video so he can just go and edit it and do his art form. And so don't automate everything. That shouldn't be your goal. Automate the robotic stuff so

[1:25:07] that you can actually be creative. It's kind of like a lot of people are like, "Bro, AI is going to replace writing copy." Writing copy is the most fun thing that I do. Like creative writing

[1:25:16] is the most fun thing to me. I don't want to automate it. In fact, I've spent my whole life getting to the point where I can write and create and teach full-time. So I don't want to automate

[1:25:25] it. And that's how you make things that actually have meaning to it. So, just keep that in mind. Also, don't look

[1:25:31] for uses for new tools. Look for new tools to solve big problems in your life. And so, this is a balance. You

[1:25:38] want to be aware of the new stuff that comes out every single day, it seems like. But also, you don't want to be a tactic hunter who just is trying to fit a square thing into a circular peg or whatever. I don't know what the freaking analogy is, but you're trying to fit a freaking apple into a banana-shaped hole. That's even worse. Goodness

[1:25:58] gracious. Anyways, all I'm saying is don't look for new ways to use the new tools. Just stay pay attention to the problems. Look for what problems in your

[1:26:09] life you want to solve. If you see a video of someone saying, "Oh, here's how to make a website." And you're like, "Oh, I'm going to go make a website." Ask yourself, "Do you need a

[1:26:17] website? Is that your main problem?" And if it's not, ask yourself, how do you use this new tool to solve your problem? So, always focus on your

[1:26:25] problems first, the tools second. So, be aware of them, but don't get obsessed and try to like just use them to do random stuff that you wouldn't have normally even tried to do. And then fourth, last but not least, productivity is not a number of outputs.

[1:26:39] AI has changed the world. It has never been easier to do stuff. But the question isn't how much stuff you can do. It's what stuff should be done in

[1:26:49] the first place. And so one of my favorite quotes from — I forget the dude who went off in the woods for a while, but he was talking about how everybody was in such a hurry to get a telephone line from Tennessee to New York when they should have been asking what does Tennessee have to even say to New York? Like is there — like should they even be communicating in the first place? And

[1:27:08] obviously they should now, but back in the day there wasn't much of a use for that. So that's what I'm saying is productivity doesn't mean how many things your AI can spit out. It's tangible progress towards your goal. So

[1:27:19] AI might spit out all this research for you for YouTube videos. It might spit out all these crazy ideas, but if you're not putting out YouTube videos into the world, then you're not making any progress. If you're not making money with your business, you're not making any progress. So just keep in mind,

[1:27:33] don't view productivity as the random AI crap. View it as what actually hits the market. What do you and AI team up on together to create change in the world?

[1:27:41] So anyways guys, that is it for this master class. Like I said, join the free school. I put out new courses all the time for free. I make my money from

[1:27:47] other stuff, not from teaching guys. So, I hope you guys enjoyed. I've really enjoyed making this. Let me know what

[1:27:51] you want to hear more of and I'll make some more AI videos because yeah, if you guys enjoy my teaching style, it means a lot to me because I think it's fun. So, I'll see you guys in the next video. And please, share this with your friends if they need to know this. Share it with them. It's going to be awesome. See you

[1:28:05] guys later.
