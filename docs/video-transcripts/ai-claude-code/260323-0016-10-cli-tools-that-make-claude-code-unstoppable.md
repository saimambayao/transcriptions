# 10 CLI Tools That Make Claude Code UNSTOPPABLE

**Channel**: Chase AI
**Duration**: 14:03
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=uULvhQrKB_c
**Transcribed**: 2026-03-23 00:16

---

## Organized Notes

**Why CLIs Over MCPs**

- The ecosystem is **shifting from MCPs to CLI tools** — CLIs live in the terminal where Claude Code lives
- **No overhead**, straight connection, **fewer tokens** than MCP equivalents
- Playwright CLI vs MCP benchmark: same task but **90,000 fewer tokens** with CLI

**The 10 Tools**

**1. CLI Anything** — meta-tool that creates other CLI tools
- From makers of **LightRAG** and **RAG Anything**
- Points Claude Code at any **open-source project** → generates a CLI tool for it
- Already done for: **Blender, Inkscape, OBS, Zoom, NotebookLM**
- Two-step install, one-step execution

**2. NotebookLM-PI** — connect Claude Code to Google's NotebookLM
- Solves Claude's weakness with **video analysis** — throw YouTube URLs at NotebookLM for free (Google's tokens)
- Creates all NotebookLM deliverables: **podcasts, videos, slide decks, infographics, quizzes, flashcards**
- Enables **batch downloads, slide revision, programmatic sharing** (not available in web UI)
- Requires a **companion skill** to teach Claude how to use it

**3. Stripe CLI** — payment and product management
- Eliminates the pain of navigating Stripe's **20-tab UI**
- Claude Code handles **product creation, setup** — still test transactions by hand
- Great for anyone building **web apps with payments**

**4. FFmpeg** — video, audio, and subtitle manipulation
- Useful for **web design animations** — chop video into frames for scroll effects
- Can **loop, reverse, stitch** video programmatically
- Gives Claude Code **multimedia capabilities** it lacks out of the box

**5. GitHub CLI** (`gh`) — essential, should already be using
- Push, commit, branch, PR management **all from terminal**
- Claude Code already knows how to use it — **one sentence to install**
- Authenticate once via browser link and done

**6. Vercel CLI** — deployment and CI/CD
- **Generous free tier** + GitHub integration = simple CI/CD pipeline
- Vercel also provides a **library of Claude Code skills** (deployment, browser automation, design/UI)
- Install + copy docs page into Claude Code → it knows what to do

**7. Supabase CLI** — backend: database + auth
- **Databases and authentication** from one place in the terminal
- Open source, can run **completely locally**
- Same generous free tier appeal

**8. Playwright CLI** — browser automation and testing
- Spin up **Chrome instances** for automated web app testing
- Instead of manually checking dev server: have Claude Code **spin up 5 tabs and attack from different angles**
- Much deeper than basic form testing — full browser automation capabilities
- Vercel also has an alternative: **Agent Browser skill**

**9. LLM-Fit** — find the right local model for your setup
- Analyzes your hardware and recommends which **local model** makes sense
- Solves the confusion of Ollama's **endless model list** with 9 versions each

**10. GWS (Google Workspace CLI)** — control entire Google suite
- Access **Gmail, Docs, Sheets** from Claude Code
- Security controls: **sandbox shared folders**, email filters, Google Armor for prompt injection protection
- Has a **massive number of skills** — point Claude Code at the repo, discuss which ones to install
- Too many skills = triggering problems, so **be selective**

**Key Pattern: CLI + Skill = Power Combo**

- Most CLI tools need a **companion skill** to teach Claude Code how to use them properly
- Install the CLI dependency first, then load the skill
- Or just give Claude Code the **repo URL** and let it install everything

## What This Means for Your Work

**You are already running most of this stack, and the gaps are strategic.** Of the ten CLI tools listed here, you actively use GitHub CLI, Playwright, and NotebookLM-PI across your 9-platform development workflow. The CLI-over-MCP argument validates your existing approach -- your 129 skills already live in the terminal, not in MCP overhead. The real takeaway is token efficiency: 90,000 fewer tokens per task means longer, more productive sessions within your 1M context window, which matters when you are running complex multi-file edits across e-Bangsamoro or e-Negosyo.

**The Stripe CLI deserves immediate attention for e-Negosyo and MoroMarket.** Your cooperative marketplace platforms will need payment infrastructure, and navigating Stripe's UI for product creation across dozens of cooperative partners is exactly the kind of repetitive pain this CLI eliminates. Having Claude Code handle product setup while you manually verify transactions is the right division of labor for financial tools serving Bangsamoro cooperatives and social enterprises.

**FFmpeg fills a gap in your training content pipeline.** With 124+ training courses under SEED Initiative, you likely produce or curate video content. FFmpeg's ability to chop, loop, and stitch video programmatically -- all from Claude Code -- could streamline how you prepare training materials for Tarbiyyah-MS or cooperative development workshops. This pairs well with your existing YouTube transcription workflow.

**GWS (Google Workspace CLI) could centralize your multi-role communication.** As OOBC Consultant, MoroTech CEO, and BSA Chairperson, you operate across multiple organizational Google accounts. The ability to sandbox shared folders, filter emails, and control Docs/Sheets from Claude Code would reduce the context-switching tax of managing government, social enterprise, and community roles simultaneously. The security controls (Google Armor, sandboxed access) are non-negotiable given the sensitivity of government policy work.

**The "CLI + Skill = Power Combo" pattern maps directly to your skills-bucket architecture.** Your existing workflow of pairing tools with companion skills in ~/apps/skills-bucket/ is exactly what this video advocates. Consider auditing your 129 skills to identify which ones still use MCP connections that could be replaced with lighter CLI equivalents -- the token savings compound across every session.

### How This Can Improve Your Claude Skills and Workflows

**The CLI-over-MCP token savings should drive a systematic audit of your 129 skills.** The 90,000-token difference between Playwright CLI and MCP for the same task is dramatic. Your skills that interact with external tools (Figma via MCP, Notion via MCP, Chrome via MCP) should be benchmarked against CLI alternatives where they exist. Run /auto-research with token consumption as the metric: same task, MCP version vs CLI version, measure token usage across 10 runs. Skills that can switch to CLI equivalents without losing capability get migrated, and the token savings go directly to extending your productive session length.

**CLI Anything (the meta-tool that creates CLI tools) could expand your /notebooklm skill's capabilities.** CLI Anything has already generated CLIs for NotebookLM, Blender, and OBS. For your workflow, generating CLIs for tools you use regularly -- Obsidian (beyond the existing CLI), Google Workspace apps, or even BARMM government portals -- would give Claude Code native terminal access to these tools without MCP overhead. The pattern: point CLI Anything at the tool's API or open-source project, generate the CLI, create a companion skill via /skill-creator.

**GWS (Google Workspace CLI) should be integrated into your /legislative-briefer and /session-summary skills.** Your OOBC consulting work likely involves Google Docs for policy drafts and Google Sheets for committee tracking. A /legislative-briefer enhancement that pushes completed briefings directly to a shared Google Drive folder (via GWS CLI) would eliminate the manual step of downloading and uploading. Similarly, /session-summary could push daily session notes to a Google Doc that your OOBC team can access without needing Obsidian.

**LLM-Fit has implications for your production deployment strategy.** Your 9 platforms will eventually need AI features in production (document analysis, content classification, search). LLM-Fit's hardware analysis could help you select the right local model for each platform's specific needs: a lightweight classification model for e-Bangsamoro's legislative document categorization, a summarization model for BangsamoroHR's report generation, or a translation model for Tarbiyyah-MS's multilingual content. This feeds into your model portability planning for government infrastructure.

**The Stripe CLI integration should be a /devwork prerequisite for e-Negosyo and MoroMarket.** Before building payment features in your cooperative marketplace platforms, add Stripe CLI setup to your platform initialization checklist. Your /devwork skill could include a "payment setup" mode that uses Stripe CLI to create products, configure webhooks, and set up test environments -- all from the terminal. This keeps payment infrastructure as code-defined artifacts rather than manual UI configurations that are hard to reproduce or audit.

---

## Transcript

[00:00] If you've been paying attention to the Cloud Code ecosystem at all, then you've noticed a huge shift. Everyone, I mean everyone, is building CLI tools to enhance what Cloud Code can do. And today, I'm going to show you my 10 favorites. And they range from YouTube

[00:15] research to deploying applications to controlling my entire Google suite all from Cloud Code. And you might recognize a few of the ones we covered today, but if you leave with just a couple new ones, then I'll have done my job. So the first tool on our list is kind of a meta pick and that is CLI anything. This is a

[00:32] CLI tool that creates other CLI tools. This thing is completely open- source and it's from the makers of light rag and rag anything. So these guys are kind of titans in the AI open source world.

[00:42] Now the cell for this particular tool is that I can use CLI anything and point cloud code at any open-source project and claude code will use CLI anything to create a CLI tool for said program. And this repo shows some of the projects that they've already done this on things like Blender, Inkspace, OBS, Zoom. We actually did a full deep dive on this exact tool not too long ago. So I'll put

[01:10] a link to that above. And it looks like they've added a few since then. Notebook LM as well, right? So, the idea is if

[01:15] you want cloud code to work with some other program from the terminal and there's not like a clear API type deal to go along with it and it's open source, well, this is the perfect tool for that job. And it's also really easy to install and use. It's like two steps to install it and then it's just a one-step process to actually execute this. It runs the full pipeline on its

[01:36] own and for you the user, it's very, very simple. So before we jump into tool number two, a quick word from everybody's favorite sponsor, me. I just released the Claude Code Masterass. You

[01:46] can find it inside of Chase AI Plus. There is a link to that in the pin comment. And it is the perfect place if you're trying to figure out how can I go from zero to AI dev, especially if you don't come from a technical background.

[01:57] I add updates to this every single week and we really focus on real life practical use cases, not just feature explanations. So, if that's something you're interested in, definitely check it out. And if you're brand new, I also have the free Chase AI community. Tons

[02:12] of free resources. Link to that is in the description. So, hopefully there's something there for everybody. Now, tool

[02:18] number two is one of my personal favorites, and you've seen me showcase this before, and that is the Notebook LM-PI tool. This tool, this CLI tool, allows us to connect cloud code to Notebook LM. There's no public API for Notebook LM. So there's no way normally

[02:33] for me to control Notebook LM from the terminal unless I've created some sort of custom browser automation, but this GitHub repo fixes that. And this is something I quite literally use every day for my own research because it solves one of the issues with Claude Code and Son and Opus in general is the fact that they can't really handle videos. Notebook LM can. I can just

[02:54] throw YouTube URLs at Notebook LM. It will do all the analysis for me for free because these tokens are on Google servers, not ours. And then it just brings it back to cloud code. And on top

[03:04] of the analysis it does in notebook LM, it can create all the deliverables that notebook LM does as well. So things like podcasts, videos, slide decks, infographics, quizzes, flashcards, on and on and on. If you can do it in Notebook LM, you can do it inside of Cloud Code. And being able to control

[03:19] all of this from a terminal is a huge benefit versus doing it manually inside of Notebook LM. And it's not just a convenience thing. It's the fact that I can very easily take all the analysis from Notebook LM and integrate it into whatever I'm doing at a larger scale inside of my project. And you also get

[03:36] access to things you can't really do inside of Notebook LM's web interface. And they're all listed down here. Everything from batch downloads to slide revision to programmatic sharing. Now,

[03:45] like many of these CLI tools, it's really a two-step process because we need to one, actually install the CLI tool, the dependency on our actual computer. And then number two, you know, we need a skill. Skills and CLI tools tend to go handinand when it comes to cloud code because we need to essentially give it the functionality and then we need to teach it how to use that specific tool in the specific way.

[04:09] So, if we're talking about CLI tools that don't require a skill, I'll let you know, but this is one of them that does. And in pretty much all these repos, there will be some sort of command that you just have to copy paste to get the skills loaded. And also, you know, while all the install is spelled out for us here, there is nothing stopping you from just giving cloud code the URL to whatever repo we're talking about or you know, whatever web page happens to explain the CLI, give it the cloud code and it will install it for you. Now, I

[04:38] really like tool number three because it's all about money and that's the Stripe CLI. Now, if you've ever used Stripe to essentially create a product that's tied into something like a web app, you know what a pain in the butt it is to go through Stripe's interface. It is not userfriendly at all. However,

[04:54] when we use the Stripe CLI, it takes all of that turmoil away from you and puts it on top of Cloud Code and Cloud Code is able to navigate all that nonsense much more quickly. That being said, when you are dealing with things that have to do with money and transactions, like obviously you still want to test these out by hand, but the actual like product creation and all like the steps that require you to go through like 20 different tabs inside of Stripe. Like we can just get rid of that. This makes it

[05:21] way easier. Now, tool number four is also in this content/multimedia video game, and that's FFmpeg. And this is a collection of libraries that allow you to manipulate video and audio and subtitles. And it actually

[05:34] could be very useful in things like web design. So I was able to create this scrolling animation on my web page with ffmpeg. And what it was able to do is it was able to take an entire video that I had created of this keyboard going from, you know, completely together to like completely expanded and then chop it up into individual frames to turn it into what you see here. And if I had tried to

[05:56] do that manually be giant pain in the butt. But something like ffmpeg makes this very simple. If I wanted to do a let's say an animation on the hero section, let's say I had some sort of image back here and I wanted to loop it.

[06:08] Well, I could just give it one video. It can automatically copy the video, reverse it, stitch it. So, it gives Claude Code a lot of functionality when it comes to manipulating any sort of multimedia, which is again, it's a place that Claude Code out of the box isn't great at. So, these CLI tools that can

[06:23] give it some enhanced functionality in those spaces are always welcome. And I also have a full video breaking down how to do this exactly that I'll link above. Now, tool number five is one you probably already know about and you definitely should be using. If not,

[06:34] you're way behind. And that is the GitHub CLI. If we are doing anything where we are writing code and we want to push to GitHub, there is no reason why we wouldn't just use the GitHub CLI to do this, right? Anytime where we have

[06:48] some sort of task or workflow that we are constantly doing and pushing to GitHub and anything on the deployment side is probably one of those, we want to be looking for CLIs that help us do it. And the GitHub CLI, you really can't ask for anything better. Now, like all things Git and GitHub related, Cloud Code is already very spun up on how to do this properly. So, when it comes to

[07:06] installing the GitHub CLI and using it, quite literally, you can do that in one sentence. Open up Cloud Code and say, "Hey, I want to install the GitHub CLI." It will do it automatically. It's just

[07:15] going to ask you to authenticate, which is a really simple process where you click a link, you log into GitHub, and you're all set. And from here, when it comes to pushing code, when it comes to, you know, commits and doing branches and all these things, you can just do it from the terminal. Now, while we're on the topic of deployments, we would be remiss if we didn't talk about tool number six, Verscell CLI. Now, I love

[07:36] Verscell because they have a very generous free tier and their connection with GitHub makes it very simple to essentially create a CI/CD pipeline just with these two tools. Now, installing the Versel CLI is again very simple. And this just allows you like all these CLI tools to control some part of the architecture process, the deployment process from your terminal. also not

[07:57] switching from tabs back and forth. Now, if you're ever wondering, hey, how do I actually use this? Well, you know what I'm going to tell you? Take this page,

[08:05] copy the whole dang thing, throw it inside of Claude Code, and it will know what to do. Now, when it comes to skills with the Verscell CLI, Verscell actually has a ton of skills available for you to give to Claude Code. But if we head over here to deployment, they have a specific one for Versell CLI, and they have a few others that are in the deployment realm, specifically Versel deploy.

[08:24] But I definitely suggest checking out this page. page. I'll put a link to that down below as well because they actually have a ton of really useful skills that if you're doing anything like browser automation as well. Um, same thing like

[08:35] design and UI, you definitely want to take a look at. Now, tool number seven is all about the backend and that's the Superbase CLI. I like Superbase for the same reason I like very generous free tier and I can handle both all of my databases and authentication from one place from the terminal using this tool.

[08:52] And remember, Superbase is also open source. It was always meant to be a firebased alternative. So if you want to run Superbase completely locally, the CLI tool helps you do that as well. Now

[09:01] tool number eight is all about browser automations and giving cloud code the ability to spin up its own instances of Chrome and do things on the web for you and that's where Playright CLI comes in. Playright Playright CLI is also a great case study when we look at CLIs versus MCPs. I highly suggest you take a look at the Playright YouTube account. They

[09:22] have an entire video on this where they compared them head-to-head and CLI essentially to do the exact same thing as the MCP server was both quicker and it was like 90,000 less tokens. And that's kind of what you kind of see here with all these CLI tools versus their MCP counterparts even with the changes that Cloud Code has made when it comes to MCPS where everything isn't just frontloaded. So definitely an interesting thing, but the Playright CLI is great. If you want an alternative,

[09:49] while we're on the, you know, topic of browser automations, Verscell actually has its own, right? So, I mentioned that a little bit before, the agent browser skill. So, if you don't love Playright CLI, you can always check out the Verscell alternative. But I highly

[10:03] suggest you start integrating something like Playright CLI into your stack, especially if you're someone who builds web apps. Why is that? Because inevitably, we need to test things on the web apps we build. And I don't want

[10:14] to go into a new tab every single time, you know, go on the dev server, check out the new form myself. Why don't I just have Cloud Co do that on its own, spin up five Chrome tabs, and just attack it from a bunch of different angles automatically, right? This allows us to do that. Like almost all these,

[10:32] there is also the requisite skills we want to install here, and it's just a oneliner, and it will automatically go inside your dotcloud folder. Now, I will say Playright in particular actually is pretty deep. There's a whole lot of things you can do with it beyond just, hey, open up Chrome and test out this form submission. So, if you're really

[10:48] into browser automation, I highly suggest you kind of dive into this repo and see what's really available to you, cuz it again, these are deep waters when you go into the browser automation stuff. Now, tool number nine is a pretty interesting one. I just got introduced to it not too long ago. You might have

[11:02] seen me reference it in my how to run Cloud Code locally video, and that's LLM fit. this is a CLI tool that allows you when you run it to figure out well what local model actually makes sense for my setup. And for most people that question has a non-obvious answer. I mean if you

[11:19] head to O Lama and go to the models like it's essentially like a neverending list of different things to do and open source is being updated every 3 seconds and so you know every single model also has like nine different versions of the same model. So it's it's kind of a confusing space especially if it's not one you hang out in very often. And this project LLMIT essentially solves that issue. And last but not least is GWS,

[11:42] the Google Workspace CLI tool. This is the CLI tool that allows us to have Cloud Code control our entire Google Workspace. Right? We're giving it access

[11:51] to our email, our Docs, Sheets, everything. Right? This is extremely powerful. But this also is the place

[11:59] where you start getting into those security issues like do we necessarily want Cloud Code to have access to all our emails? But luckily, it's not too hard to set up the GWS CLI tool in a way where we almost like sandbox cloud code and it has like shared folders with us and it only has access to certain emails if we use filters. So, there is some wiggle room if you're scared about the security side. But for many people,

[12:20] having claude code have full access to the Google suite is a big deal. And even if you do give cloud code access to say your Google email, Google Workspace has something called Armor and it's all about dealing with like prompt injections and that sort of thing. So, there are guard rails in place. We

[12:36] aren't just like letting Cloud Code go off and do whatever it wants. Now, this one in particular has like a billion skills. Like, I'm not really exaggerating, right? So, a big part of

[12:47] figuring out how to use this tool um to the most effect is also figuring out which skills make the most sense, right? Skills aren't a huge context window, you know, drag. But if you have too many of them, triggering the right one becomes a problem. So this is the kind of repo

[13:03] where what I would do and what I have done when I installed this thing was I essentially pointed cloud code at this thing. I created a new directory. I had it clone the whole thing and then you can have a discussion with cloud code and say hey like all right now that you have full visibility into how this works and what's going on. What would make the

[13:18] most sense for us to actually like install and use right and that's going to be different for every single person. So that's my list of my 10 favorite CLI tools as of today. Tomorrow that list will probably change in a week. I'll

[13:28] probably have added like three more of them because I wasn't joking about it in the intro. Like this is the shift. Like we're moving away from MCPs. We're

[13:36] moving into CLIs because it just makes sense. Cloud code lives in the terminal. CLIs live in the terminal. There's no

[13:42] overhead. It's like just a straight connection and allows cloud code to do the most with the least amount of tokens for all intents and purposes. So hopefully at least a couple of these were new to you and you can begin to integrate them into your stack. So let

[13:56] me know in the comments what you thought. Make sure to check out Chase AI Plus if you're interested in the master class.
