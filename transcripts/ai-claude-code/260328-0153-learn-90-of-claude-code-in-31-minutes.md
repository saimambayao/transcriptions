# Learn 90% of Claude Code in 31 Minutes

**Channel**: Chase AI
**Duration**: 31:25
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=TwkdDcO4vWQ
**Transcribed**: 2026-03-28 01:53

---

## Organized Notes

**Chase AI** is a YouTube creator and Claude Code educator who runs the **Chase AI Plus** community and masterclass.

**Installation and Where to Use Claude Code**

- **Four ways** to use Claude Code: terminal (raw), **Claude Desktop app**, **Cowork**, and inside **IDEs** (VS Code, Cursor, Windsurf)
- All options exist on a **spectrum of control** — terminal gives the most control and insight; Cowork trades control for a simpler, more streamlined UX
- For most users, **VS Code + terminal** is the sweet spot — free, shows file explorer alongside the terminal, and lets you edit files visually
- Setup: install Claude Code via one terminal command from the docs page, then open a project folder in VS Code and launch from the integrated terminal

**Permissions — Three Levels**

- **Default**: asks permission for every file edit and shell command — safe but slow
- **Accept Edits On**: auto-approves file changes but asks before shell commands — recommended starting point for beginners
- **Bypass Permissions On** (requires `--dangerously-skip-permissions` flag): full autonomy for Claude Code — what most power users run, per Anthropic's own data
- Start with Accept Edits, graduate to Bypass as comfort grows

**Prompting — The Most Important Skill**

- **Plan Mode** is the easiest way to improve outcomes — forces Claude Code to ask clarifying questions instead of guessing
- Three prompt improvements that compound:
  1. **Focus on the outcome/why** — not "build a kanban board" but "I need to organize past and future content ideas with performance tracking"
  2. **Add visual examples** — drag screenshots from Dribbble or similar into the prompt; point to GitHub repos with code you like
  3. **Ask open-ended expert questions** — "What would an expert in [domain] be thinking about here?" and "What am I not thinking about?" — forces deeper analysis than Plan Mode's default questions
- Plan Mode's questions are **surface-level**; explicitly prompting for expert-depth questions produces materially better outcomes
- This matters more as project complexity increases — "we don't know what we don't know"

**The "Accept Monkey" Warning**

- If you just hit "recommended" on every Claude Code suggestion without understanding why, you're **indistinguishable** from anyone else using the tool
- You don't need to write code, but you **must understand software engineering fundamentals** — how pieces connect, what tech stacks mean, why certain architectures matter
- Claude Code is an "infinitely patient tutor" — when you encounter something unfamiliar (Next.js, Tailwind, React + Vite), stop and ask it to explain until you understand
- **You still drive the ship** — Claude Code does the work, but you set the destination; a "caricature of a vibe coder" will hit a wall on complex projects

*Quotable Quotes:*

> "You don't need to know how to code. You never have to write a line of code ever. But you do need to understand software engineering." [11:41]

> "You still drive the ship with Claude Code. It's going to do everything, but you're setting the destination. And if you have no clue what's happening and you're a caricature of a vibe coder, you're not going to get as far as you think." [12:07]

> "Cloud Code is the infinitely patient tutor. You just have to ask." [12:29]

**Skills — Teaching Claude Code Taste**

- Skills are **text prompts** that tell Claude Code how to do a specific thing in a specific way — nothing secret, just instructions
- **Two flavors**: (1) improving an existing capability (e.g., front-end design), (2) workflow automation combining multiple steps into one command
- The **front-end design skill** is an official Anthropic plugin — dramatically improves UI output from generic AI slop to polished designs
- Install via `/plugin` → search → install → reload; invoke with `/frontend-design` (100% trigger rate) or natural language ("fix the front end" + "with the right skill")
- **Installed ≠ in use** — skills must be explicitly invoked per session; they don't run automatically in the background

**Context Window Management**

- The **1 million token** context window is Claude Code's "budget" — every prompt, response, tool call, and skill invocation consumes tokens
- **Context rot**: performance degrades as the window fills; noticeable dip after ~**200K tokens** (20%), steady decline to ~**78% effectiveness at 1M** (per presenter's reading of an Anthropic chart — closest official figure is 76% on MRCR v2; the 92% at 256K figure is unverified)
- The **green zone** is the first 200K tokens — stay there whenever possible
- `/clear` resets the entire context window; unlike a chatbot, Claude Code can **re-read project files** to regain context, so clearing is low-cost
- If carrying specific conversation context matters, ask Claude Code for a **summary to bring to the next session** before clearing
- Use `/context` or a custom **status bar** to monitor usage — "create a permanent status bar showing context window usage"

**CLI Tools — The Post-MCP Era**

- CLIs are replacing MCPs as the preferred integration pattern — they live in the terminal alongside Claude Code with **zero overhead** and lower token cost
- Two parts to every CLI tool: (1) the **tool itself** (download/install), (2) the **companion skill** (teaches Claude Code how to use it)
- **Supabase CLI** example: create databases and authentication via natural language instead of manual web UI clicks
- **Playwright CLI** example: automated browser testing — Claude Code opens Chrome instances, tests kanban board interactions (drag cards, create cards, verify colors) with no manual QA
- Install method: copy the GitHub repo URL into Claude Code and say "install this CLI, follow these instructions" — it handles everything (faster with Bypass Permissions)

**Deployment — The GitHub → Vercel Pipeline**

- Two-step deployment: **commit + push to GitHub**, then **deploy from GitHub to Vercel**
- **Git fundamentals**: `commit` = save point on your machine; `push` = upload that save point to GitHub (cloud)
- First-time push requires **GitHub authentication** — follow Claude Code's instructions, takes under 60 seconds
- **Vercel**: free hosting, auto-deploys from GitHub — sign up with GitHub credentials, import repo, click deploy
- Environment variables go in Vercel's settings for projects with API keys
- The **continuous deployment loop**: change code in Claude Code → test on dev server → commit + push → GitHub auto-triggers Vercel update → live site updated
- Both GitHub CLI and Vercel CLI exist — once you understand the manual flow, switch to natural language commands

**Six Essentials Covered**

1. **Installation** — one terminal command
2. **Where to use it** — terminal, IDE, Desktop, Cowork (spectrum of control)
3. **Prompting** — Plan Mode + outcome focus + examples + expert questions
4. **Skills** — text prompts that improve capabilities (front-end design, workflows)
5. **CLI tools** — external programs Claude Code can control (Supabase, Playwright)
6. **Deployment** — GitHub → Vercel pipeline for free web hosting

---

## What This Means for Your Work

This is a beginner-oriented video, and you're well past its target audience — you run 134 skills, manage a 1M context window daily, and have built your own CLI integrations (notebooklm, yt-dlp/Whisper pipeline). But it surfaces a few ideas worth pressure-testing against your current setup.

**The "accept monkey" framing validates your skill architecture.** Chase's core argument — that blindly accepting AI recommendations produces indistinguishable output — is exactly why your 134-skill system exists. Each skill encodes domain knowledge (BOL provisions, Feliciano citation format, ADDRESS IT methodology) that prevents Claude Code from defaulting to generic output. Your /bangsamoro context loading, /fact-checker verification pipeline, and /legal-assistant all exist because you refused to be an "accept monkey" in the Bangsamoro governance domain. The video confirms that your approach — investing in teaching Claude Code *how* to think about your domain — is the correct long-term play.

**The CLI-over-MCP argument aligns with your existing trajectory.** You already use Playwright CLI for /webapp-testing, notebooklm CLI for /research-pipeline, and yt-dlp for /youtube-transcriber. Chase frames this as "the post-MCP era" — CLIs are lower overhead, lower token cost, and more reliable. This validates your decision to build skills around CLI tools rather than MCP servers. For your deployment workflow, you already use a custom /gitops skill rather than a GitHub MCP, which is exactly this pattern.

**Context window management is where you diverge.** Chase recommends clearing at ~20% (200K tokens) and staying in the "green zone." Your workflow deliberately uses the full 1M window — long guidebook sessions, multi-chapter bill drafting with /bill-drafter, deep research sessions with /deep-research. Your CLAUDE.md explicitly says "never suggest ending sessions early." The Anthropic benchmark data he cites (92% at 256K, 78% at 1M) is worth noting, but your mitigation is different: you use parallel agents to offload independent work to fresh context windows, and your skills are designed to front-load reference material rather than accumulate it through conversation. Worth monitoring whether your parallel agent pattern effectively circumvents the degradation curve.

**The Plan Mode + expert questions pattern maps to your /grill-me skill.** Chase's advice to prompt "what would an expert think?" before building is essentially what /grill-me does — stress-testing plans through domain-expert questioning. The difference is your skill is more structured (decision trees, branch resolution) while his approach is ad-hoc prompting. No action needed — your version is more rigorous.

**Next steps:**
- Consider adding Vercel CLI and Supabase CLI skills to your toolkit if you're deploying frontends for MoroMarket, OBCMS, or SBP — the GitHub → Vercel auto-deploy pipeline he describes would streamline your current Railway/manual deployment workflow
- The "drag screenshot into Claude Code" technique for design references is something to use more deliberately with /frontend-design and /stitch-design — Dribbble as a design reference source for e-Bangsamoro UI work

### How This Can Improve Your Claude Skills and Workflows

**Skill triggering reliability.** Chase highlights that `/frontend-design` gives 100% trigger rate while natural language invocation is hit-or-miss. This is already how your system works — your CLAUDE.md instructs explicit `/skill` invocation — but it's a reminder to audit whether your superpowers skill descriptions are specific enough to trigger reliably via natural language for users who don't use slash commands.

**/skill-optimizer and /skill-creator evaluation criteria.** Chase's two-flavor taxonomy (capability improvement vs. workflow automation) is a useful lens for the /skill-optimizer eval loop. When scoring skill quality, consider adding a dimension: "Does this skill encode domain knowledge that prevents generic output (flavor 1) or does it automate a multi-step workflow (flavor 2)?" Your best skills (/csw, /bill-drafter, /guidebook-writer) are both — they encode Bangsamoro governance knowledge AND automate multi-chapter production workflows. The /skill-optimizer could flag skills that are only flavor 2 (pure automation with no domain encoding) as candidates for enrichment.

**Context window monitoring for /session-summary.** Chase's status bar idea is interesting — your /session-summary skill could benefit from automatically noting context usage at session end. When you're at 85%+ context and the session summary fires, it could flag which phases of work consumed the most tokens, helping you optimize future sessions. This is a small enhancement to the existing skill.

**CLI skill pattern for new integrations.** Chase's framing (CLI tool + companion skill = integration) is the exact pattern you've already established with notebooklm, Playwright, and yt-dlp. For your active projects, the obvious next CLI + skill pairs would be:
- **Supabase CLI + /database skill** — for BangsamoroHR and SBP backend work, replacing manual Django migration management
- **Vercel CLI + /deploy skill** — for MoroMarket and any future public-facing frontends, replacing manual Railway deploys
- **gh CLI** is already available but lacks a dedicated companion skill — a /github skill wrapping common PR/issue workflows could save tokens vs. raw gh commands

**No new skill gaps identified.** Cross-referencing against your 134-skill library in ~/Vault/Claude-Skills/index.md, Chase's video doesn't surface capabilities you're missing. Your /frontend-design, /webapp-testing (Playwright), /gitops, /grill-me, and /prompter already cover every technique he demonstrates. The value is in the validation, not new discovery.

---

## Transcript

[00:00] If you're just getting started with cloud code, it can feel incredibly confusing, especially if you don't come from any sort of technical background. And it doesn't help that half the advice out there is completely outdated. People telling you to use CloudMD files you don't need, pushing you towards MCP servers that don't make sense, and generally promoting workflows that completely pollute your context window.

[00:21] But in the next 30 minutes, we're going to completely cut through the BS. We're going to talk about what actually matters so you can get the most out of Cloud Code in 2026. So, let's begin by talking about how you can first get Claude Code installed and then jump into the first confusing part which is like where do you use it? Because there's

[00:39] like four different ways you can use Cloud Code. Now, for the install, it's very easy. If you just Google Claude Code install, it will bring you here the Cloud Code documentation page and it gives you the one command you need to run depending on your operating system.

[00:53] So, I'm in Windows. So, I would just copy this. I would just go to the search bar, look up PowerShell, open up, open up your version of the terminal, and then I would just paste it in there and run it. Now, does that mean you have to

[01:04] use cloud code inside the terminal? What about things like cloud code in the cloud desktop app? What about co-work?

[01:12] And what about IDES like VS Code or Cursor, Anti-gravity? I heard you can use cloud code inside of there. And I also heard you can use cloud code through a browser. Like, it's kind of

[01:20] confused. There's almost too many options. Which one should you use? Well,

[01:23] the good news is you can't really go wrong with any of them. Even if you decide to use something like co-work for I would say about 95% of the people and your common use cases, whatever you can do in co-work, you can do inside the terminal and in between. Now, just understand it's on a spectrum and it's a spectrum of control. If I'm inside the

[01:41] terminal, I have more control and insight to what cloud code is doing on my machine at any one time. On the other end of the spectrum, we have co-work. and co-work trades some control for a simpler, more streamlined user experience, right? It's very obvious

[01:55] what I need to do to optimize my week or organize my screenshots or start doing things versus the terminal, which like I said, sometimes it isn't as clear if you've never dealt with it before. That being said, once we get over the initial shock of the terminal, it's actually pretty simple, right? It's still just a prompt window. Everything I do,

[02:14] everything I prompt here is kind of similar to co-work. pretty much the same thing as a cloud code desktop app, but we get more control, right? It's just not as pretty. And today, we'll be using

[02:24] the terminal inside of an IDE, an integrated development environment. So, when people say they're using cloud code with anti-gravity or cursor or VS Code, this is what we're there talking about, right? It's just a terminal with some window dressing. This right here at the

[02:38] bottom, this is the same terminal as this, except now I also have a file explorer. So, as Cloud Code creates folders and files within my project, I can see them very clearly. And when I click on them, it'll be more obvious further along in the video. I can

[02:51] actually edit the text files up here as well. So, it's a nice little like in between. And VS Code is totally free and simple to set up. So, that's nice, too.

[02:58] Now, to set up VS Code, very easy. Just Google Visual Studio Code VS Code. It will take you to this main page. Just

[03:04] click download for your operating system. Run through the install wizard and open it. Now, when you open it up, it will look like this. Just go to file,

[03:11] go to open folder, and now you need to create a folder for this project. We're going to create a simple landing page for this demo today as we go over the cloud code fundamentals. So you can create the folder wherever you want, your desktop, your cloud code folder, doesn't really matter. Now, I called

[03:26] mine 2026-1. You can see it over here on the left. As more files get added, they will populate here. Now, we need to open

[03:32] up the terminal. So, hit the three buttons, three little dots at the top, go to terminal, new terminal, and we see it right here. Now to use claude we have two options. You can open it up with

[03:41] claude or we can do it dangerously. So you'll do claude space dash dash that's a flag dangerously skip permissions. Now why would I do this? Because it gives me

[03:53] the ability to use a specific permission setting that essentially gives claude code full access to my computer. Now that sounds very scary but let me explain permissions first. So we see permissions down here. See how it says

[04:05] bypass permissions on? This is like in red. This is the danger zone that I just showed you. If I hit shift tab, I can

[04:11] shift through different permissions settings. So, first is just normal default. You won't see anything there.

[04:18] What this means is that if it wants to edit a file, it's going to ask for permission. The problem with asking permission for every single file change is you will constantly be asked by cloud code, do you want to do this? Is this okay? Is this okay? Are this okay? Gets

[04:32] annoying and slows you down. Now the next permission is accept edits on. It's no longer going to need your permission to make changes to files but it will ask your permission for shell command. So

[04:43] these are like actual changes to your machine itself. All right. So it's less slow but like let's say it was trying to download a specific thing and install a dependency like a CLI tool. It would ask

[04:53] your permission first. This is probably the best place to start until you get comfortable. Lastly, we have bypass permissions on. This is where you're

[05:00] giving cloud code free range to do whatever it wants on your computer. Again, kind of frightening. We've all heard horror stories of claude code just like deleting everybody's files, you know, and they just couldn't even get them back and did all this damage. I

[05:12] will say having used claude code for hundreds and hundreds of hours. I've never run into that issue. And most people, and this is from Anthropics data themselves, if they're power users, they're on bypass permissions on. Why is

[05:23] that? Because it makes it infinitely faster to do things. And as you get more comfortable, you're going to want to be fast. So, if that's too much, stay on,

[05:31] accept that it's on. But as you get more comfortable, understand bypass permissions is there. But to have that even available, you need to do dangerously skip permissions. Now,

[05:38] before we talk about the most important skill you have to master in Claude Code, and that's knowing how to prompt it, a quick word from our sponsor, me. So, I just released the Claude Code Master Class, which essentially takes what we're talking about in this video, which is a 30-minute overview of the essentials, and goes way deeper. So, if you want to go from zero to AI dev, you really want to master cloud code, even if you aren't technical, the cloud code masterass is what you need to check out.

[06:03] There's a link to that in the pin comment in Chase AI plus, but understand if you're brand new to this AI stuff, that's just a bridge too far. I also have the free Chase AI community link to that in the description. Tons of free resources, so something for everyone.

[06:15] So, like I said, the most important skill you can master with Cloud Code is prompting. Now, for today's demo, what we're going to do is we are going to build a kanban board for social media content creators, right? Just a simple web app. And it's through this lens that

[06:30] we are going to go over all these fundamentals. Now, when it comes to prompting, the easiest way to improve your outcomes is with plan mode. Why is that? Because when I have plan mode on

[06:39] and I tell Claude Code to do something, it's not just going to go off to the races and do whatever it thinks is best. It's going to ask me clarifying questions. So, when I say something like, "Build me a kanban board for content creators," right? As poor as

[06:55] that prompt is, it's going to be like, "Hey, what about this? What about that? What about design? What about colors?"

[07:00] Right? It will try to fill the gaps versus if I don't use plan mode and I still have gaps. Well, it's just going to fill those gaps as it sees fit. And

[07:09] it'll do an okay job. It'll do okay. It's going to do an average job. And

[07:13] chances are, you don't want an average run-of-the-mill product. So, how can we fix that? Well, there's a few things.

[07:17] The first thing you want to do is actually focus on the outcome. We're not building a kanban board for the sake of it. There's a reason. And in this case,

[07:25] the reason is going to be I want to be able to organize all my past and future content ideas. I want to see how they've performed in the past, and I want to have a place where I can see what I'm planning to do in the future. So, for that, I just wrote the goal is to create a board that allows me to organize previous content and future content. If

[07:40] this was something like a landing page or something for your website, it would be like, "Hey, the point is to drive them with a call to action, to fill out a form, to, you know, sign up to my newsletter or like to sell a particular product." And the next thing we can do is add examples to the prompt. As great as it is for me to explain in words what I want the kanban board to look like, if I can give it a screenshot of something I like or even better point it toward like a GitHub repo where I can see actual code, it's going to give me a better outcome. Now, in our case, since it's a

[08:06] kanban board, it's very front-end design heavy. I can go on some place like Dribbble with three Bs and just kind of scroll till I find something I like. I found this one. I think it looks

[08:14] pretty good. So, what I'm going to do is just screenshot it and drop it into cloud code. Now, you can't copy paste it into the chat, but you can just go inside your screenshots folder and drag it in like I just did. Now, the last

[08:24] thing we want to do with the prompt is ask open-ended questions. What do I mean by that? I mean asking questions like what would an expert in kanban boards be thinking about or asking about here right this idea of saying hey like what am I missing what are the unintended consequences of adding this feature what would an expert in X whatever it is you're doing what would they be thinking about or asking about in this situation one and this is really really important because one of the things with AI that's great about it and is also kind of its downfall is the fact that it lets us play in spaces and domains we have no business being in. Right? A few years

[09:05] ago, I would never be able to build a kanban board yet. We're going to do one in like 10 minutes. Because of that though, and because I have no domain expertise, I'm probably going to approach this perhaps from the wrong angle or just not know about certain things that would never trip up an expert. And we don't

[09:22] know what we don't know, right? So to alleviate that, we need to ask questions like this, right? What would an expert think? What am I not thinking about?

[09:28] Because as good as plan mode is, and plan mode will ask us questions, it's kind of surface level. When we prompt claude code to prompt us and tell, hey, I want you to go deeper and like really think about this and what we're missing, it's actually going to give you much better outcomes. And we'll see the results here with the kanban board. But

[09:45] the truth is this is even more important when you're doing more complicated projects where you are completely out of your depth. So this is a good start. You know what we want to do, the why, examples, and open-ended questions. So

[09:56] let's see what it comes back with plan mode. So right away claude code comes back and says here's what a kanban expert would be thinking about for a content creator board specifically. This is exactly what I want. I want deeper

[10:06] questions than just what do you want the colors to be? So it's asking for the column structure. So we will do content pipeline. For platforms we'll do

[10:15] multiplatform. Metrics. Let's just do views and engagement for now. Keep it simple. And then data

[10:22] entry. For this demo we'll just do manual entry only. And we'll submit our answers. and it should come back with

[10:26] more questions after this. Now for the second round of questions it came back with these are a bit more technical and it's asking about my tech stack. Do I want to do Next.js and Tailwind HTML CSS or React plus Vite? Now this is a great

[10:38] time to talk about the other reason why having this back and forth with cloud code is so important. And this is where you're going to have some light shined on your deficiencies on the software side. And that's okay if you aren't technical. You're going to have a ton of

[10:51] them. However, you have two options when you get here. One is to just look at whatever cloud code says and whichever one it recommends and hit next and hit next and continue on forever. You can

[11:03] get really really far doing this especially if you're doing simpler things like I'm just doing web design or you know some like landing pages or kanban boards right you can get really really far because Opus 4.6 is that good and cloud code is that good. However, if you take that approach forever, I'll ask you this, like, what's the difference between you and the guy down the street who I show, you know, another Claude Code intro video to for 15 minutes. The

[11:25] fact is there's almost no difference. And the fact is, if you become just an accept monkey and you just hit recommend it every single time, you're going to eventually hit a wall if you don't actually learn what any of this means. If you see something here that you don't understand, like you don't know what Next.js or Tailwind is you need to go

[11:41] down to four and type something and say explain this and then you're going to say explain it again and explain it again. So you understand what it means because you don't need to know how to code. You never have to write a line of code ever. But you do need to understand

[11:56] software engineering. You do need to understand AI development. You need to understand the fundamentals of how these pieces come together and connect and relate because if you don't, you're going to eventually hit a wall when you start doing more complicated projects.

[12:07] And that's because you still drive the ship with cloud code. It's going to do everything, but you're setting the destination. And if you have no clue what's happening and you're a caricature of a vibe coder, you're not going to get as far as you think. No matter how good

[12:21] these models are. And again, even if you got far, if you can't differentiate yourself from anyone else, what's the point, right? Where's the value add?

[12:29] Where's the value add from you? So all that to say, you need to take an active role in your education in this place. And Cloud Code is the infinitely patient tutor. You just have to ask and

[12:40] you'll probably do recommended anyway, but over time you'll start to get what's actually happening. So for features, we'll do drag and drop cards and then we'll submit this guy. So Cloud Code came back with its eight-phase plan for our kanban board. So we're just

[12:54] going to say yes. We'll see what comes out in the first pass. So Cloud Code finished it up and it also launched a dev server for us. So you should see

[13:01] some message that says like, "Hey, it's live at localhost 4000." Localhost 4000 is just a place on your computer where you can view the web app. You view it through something like Chrome, like your actual web browser, but it's not on the internet. If you don't see this, just

[13:14] tell Cloud Code, hey, can you spin up a dev server for me and it will give you a link just like this. So, probably localhost 3000. And here's a look at our board. Now, first things first on the

[13:25] front end design, boring, pretty poor. This is about as generic as it gets in terms of the actual functionality. Kind of everything I asked for, right? We

[13:34] have the content type, descriptions, labels, platform, right? I can move the cards around. Easy enough. But the front

[13:41] end design kind of bothers me, right? I even gave it an example, and maybe the example wasn't good enough because it was just a screenshot, but like this is boring. Why is that? Well, this kind of

[13:52] segues nicely into our next conversation, which is skills, right? Because one of the areas that cloud code isn't the best in, and this is kind of an AI thing in general, is front-end design. Really, anything that requires taste, and you hear this term thrown around everywhere these days, is like AI has no taste. What that really means is AI kind

[14:12] of sucks at front-end design, and things like this that more have a more creative bent, but there are solutions. And that solution can be found in skills. Now, you've probably heard about skills, but in case you haven't, skills are simply text prompts. They're just text prompts

[14:28] that tell Claude how to do a specific thing in a specific way. They come in two flavors. The first flavor is it's essentially teaching Claude Code how to do something better than it already does. A great example is front-end

[14:40] design. Kind of what we're talking about here. Flavor number two, we're not going to go into that today, is sort of like workflow type skills where, let's say, I'm normally doing something inside of Cloud Code that has like 10 steps, but I do it all the time. I can combine all

[14:52] steps, all 10 steps into one skill, right? Just makes it easier for me. We're going to focus on that first one, right? So, a great example of this is

[15:00] front-end design. So, if I tell Cloud Code to create a landing page and I don't give it a great prompt, it's going to create something like this up top, right? Sort of this boring AI slop, purple gradients, blah blah blah. Nobody cares about this,

[15:10] right? Very ugly. However, if I give it that same prompt and I use the front-end design skill, well, we get something that's much better. Now, this isn't

[15:19] everybody's cup of tea. Some people would call this AI slop as well. But the point I'm trying to make here is that there is a huge gap between number one and number two, and we would rather be with number two. And it's simply doing

[15:31] that with a prompt. There's just a big text prompt here that we call front-end design skill, and it reads before it creates the thing. That's all that's going on. And there's nothing secret

[15:41] about these skills. The front-end design skill is an official Anthropic skill that they created and you can take a look at on Anthropic's GitHub. We're looking at it right now. This is all it

[15:50] is. It's just a text prompt. It's the same thing as if I copied this whole thing, right? Jumped inside of Claude

[15:56] Code and then pasted it in there. So, how do we actually use skills then? Well, first thing we need to do is we need to install the skill. So, if I do

[16:05] forward/plugin, this takes you to the plugin library. This is essentially a list of all the official Claude Code plugins aka skills. So to discover them, I can just, you know, tab through them or I can just search for them. So if you

[16:17] search for front-end design, it will pop up for you. It's not for me because I already have it installed. And then you just go down here, hit enter, and it will install it. To make sure it's

[16:27] installed, you can just tab over to where it says installed. And like you can see here, I have the front-end design plugin installed. Now, once you install it, it will probably prompt you to do something like plugins reload or something like that to get it up and running. Now, once a skill is installed,

[16:42] that doesn't mean that Claude Code is necessarily using it, right? There's a difference between installed and available and it actually being in use, which can be kind of confusing. So, if I want Claude Code to use that skill, there's two ways I can do it. One, I can

[16:55] do /frontend-design. So, if you ever want a 100% trigger rate on your skills, you need to do it like this. /frontend-design space and then I would give it my prompt like fix my front end right the other way to invoke prompts is simply through natural language so I could just say something like let's fix the front end by just saying let's fix the front end I'm kind of assuming that cloud code is smart enough to realize that oh shoot I have skills related to front-end design let me call those let me invoke those and use it here right so you can do it with natural language you can even say with the right skill to kind of nudge it in the right direction. Just know those are

[17:37] your kind of your two options, but it needs to be invoked. It isn't constantly in use. Now, skills themselves can actually be a pretty deep subject and I will link some of my stuff above to help you with that. But the biggest thing to

[17:47] remember is they're just text prompts and it's how we tell Claude code to do a specific thing in a specific way to improve it in some manner. So for us, we're going to do front-end design and I'm just going to give it a prompt explaining how I want it improved. So, I wrote, I want to completely rework the kanban board front end. I want a dark

[18:03] mode. I want a textured background. I want some sort of subtle motion/light animation as I move my mouse. And I also

[18:10] want some glass morphism effects for the cards that give them some weight. And here is the update. So, this obviously has a lot more going on. We kind of have

[18:20] like this background like light orb following us. It's a little much for me honestly, but it looks kind of cool when we zoom in on the sort of glass morphism cards we have going on. You can see the light behind each card. When we click on

[18:34] the card, I do wish the card continued to have the glass morphism effect. That's something we could change in the prompt. But overall, you know, using the front-end design skill and giving it a bit more of detail in terms of what we want. You see, this is infinitely better

[18:47] than the first pass. So this is a great yet simple example showing you how you can use skills to improve Claude Code's performance. Now speaking of Cloud Code's performance, the other way we can drastically improve our outputs is through context window management.

[19:02] You've probably already seen me a number of times do this /clear command. And you've probably also seen down here this little status bar that you probably don't have in your version of cloud code. What's going on with that? How do I get it? What do you mean

[19:16] by context window management? Now, context window management means keeping an eye on this, the amount of tokens we have used at any one time because the context window, this thing right here, this is Claude Code's budget for what it can spend on your project. It has a budget of 1 million tokens. Tokens are

[19:34] the currency of large language models. Tokens are essentially words. So, one word given to Claude Code in a prompt equals one token. Each word you get back

[19:43] is also considered a token. Anytime it uses skills, anytime it uses tool calls, those all take tokens. We have a million of them, which is a lot. However, even

[19:52] as cloud code has gotten a larger and larger context window, we still deal with the recurring problem known as context rot. Context rot means the more I fill up my context window, the worse cloud code performs. Now, there isn't a specific number as for where we see the largest drop off, but what we're really looking at is after about 200,000 tokens, about 20%, you do start to see a certain dip, right? And it continues to

[20:19] get worse and worse over time, which means that first 200,000 tokens, right? That's like the green zone. That's the gold zone. We always want to stay in the

[20:27] first 200,000 if we can help it. Sometimes you'll be in a project where you require requires you to have more tokens in there at once just for context purposes. But if we don't need more tokens, we don't want to use them, right? I would rather use tokens 0

[20:41] through 100 over and over and over again, then let this accumulate and be in the 500,000, 700,000, 800,000 range, right? If you don't have to be there, then why bother? I want the best outputs possible. And that is where

[20:54] /clear comes in. /clear essentially resets my entire context window. So if this thing was at 800,000, I do /clear. Well, we start all

[21:02] over. Brand new context window. What's the downside of that? Well, it now

[21:06] forgets everything it was talking about in the previous conversation. It's as if you were having a very long conversation with the cloud chatbot and then you just went ahead and you started a new chat, right? It's going to forget everything.

[21:17] In the context of a chatbot, like your normal Claude.AI, that can be a problem because everything is tied to the actual conversation you had. But that's not really the case inside of Cloud Code.

[21:26] I'm inside a project. All the files are right here for Cloud Code to take a look at. So even if I do, you know, /clear and I now ask it something about my project or tell it I want to fix something with the front-end design inside a brand new window. Well, it's

[21:40] just going to go ahead and take a look, right? So it's always able to like regain the appropriate context. Now, if I was having a very specific conversation in my last window, I was like, "Oh, I got to bring this over. I

[21:50] don't think it's going to just be able to tell from the files." Well, then just ask Claude Code, hey, give me a quick summary that I can bring to the next session. That's it. Now, as for how we

[21:59] tell where we're at in terms of the context window, if you do /context, you'll be able to see it, right? Right now, we're at 13,000 out of 100,000 tokens, so just 1%. However, that can be kind of painful.

[22:09] Instead, you know, you want to have some sort of status bar like I have down here where I can very quickly tell where I'm at in terms of my window, which here is 2%. Now, to create something like this is again very simple. You're just going to tell Claude Code to do it for you.

[22:22] Just tell it to do something like create a permanent status bar that sits below the prompt window that shows me my context window usage. That's all you need. And anytime you see it get close to say about 20%, if you don't need that context, just clear it and start over.

[22:37] Now, in case you needed more evidence, you can take a look at this chart from Anthropic, which is essentially testing how well Opus 4.6 and Sonnet 4.6 do with large context loads. So at 256K, so

[22:48] about 25%, it's at 92% effectiveness. At a million, it's at 78. So we kind of just have a steady decline as we continue to fill up the context window.

[22:57] So again, if you don't need it, just reset it. So at this point, I've given you three ways to improve Claude Code's performance. Prompting, skills, and context window management. Now, I want

[23:07] to give you a fourth tool. And this tool is really cool because this is where we give Claude code control of outside programs that it can use on our behalf. And I'm talking about CLI, command line interface tools. Now, CLI are where this

[23:22] whole space is headed. Gone are the days where everyone and everything is becoming an MCP, right? For a year and a half, that's all you heard about. MCPs,

[23:29] MCPs, MCPs. Well, as cool as MCPs are, they're kind of going by the wayside and they're being replaced by CLIs. Why is that? What even is a CLI? Well, a CLI is

[23:40] something that essentially lives in the terminal and cloud code also lives in the terminal. So, cloud code is able to control these programs with essentially no overhead. It lowers our token cost and it tends to just be more efficient in general. Now, what's an example of a

[23:54] CLI tool? Well, something like Supabase. So, Supabase is a web app where you can create databases and authentication. So, let's say we wanted

[24:01] to create a database for our kanban app. We could do it inside of Supabase. Or if we wanted to create authentication like have the ability for people to log in we could also do that in Supabase. I could start a project I could manually go in I could create the you know databases all that stuff but it's kind of a pain in the butt instead if I use the Supabase CLI tool with cloud code I can just tell cloud code do all that stuff in Supabase write an outside program and it'll do it for me right so you can imagine how like time-saving and effective that process is and for today's example we're going to be using the Playwright CLI. This is a browser

[24:36] automation CLI. So, this is going to give Cloud Code the ability to essentially create its own instances of Chrome and test our kanban board because even though there isn't, you know, a ton going on here yet, I mean, like, do you want to individually go in here and test every single thing and every single color and make sure it all works? No.

[24:52] Why don't we have Cloud Code essentially do that for us? Mimic a human being coming in here and testing all these things and making sure it works. Well, that's what we can do with Playwright CLI. Now, the majority of cloud code

[25:01] friendly CLI tools you will find will be on GitHub and most often they're going to be open source. And there's going to be two parts to almost every single CLI tool. The first is the CLI tool itself.

[25:13] So, it's something we need to actually download on our computer. Imagine like downloading an application. The second half of that is the skill. All right.

[25:20] So, cloud code can understand that Playwright lives on our computer and it's available, but we need to teach it how to best use it. So most of these repositories on GitHub also include the requisite skills. So here inside of Playwright, you know, you can see here's the installation and then here's how you also install the skills. So just by

[25:37] running these three lines of code, it downloads Playwright, installs it and teaches cloud code how to use it. And from there we just use natural language. So let's go ahead and do that. And

[25:47] remember there's two options. I can either do this manually, right? I can copy this. I can go inside of here. I

[25:53] can open a new terminal and just paste it in there. Or what I can do is I can just copy this URL, go back into cloud code, paste this in there, and say, "Hey, I want you to install the Playwright CLI. Follow these instructions." And it will do that on

[26:09] your behalf. Now, remember our permissions? Remember how I said if you're on bypass permissions on, it can do things like shell commands. If you're

[26:16] on bypass permissions on, it won't even ask for permission once you tell it to do that. If you're on any of the other permissions, it will ask for, you know, your permission. So, go ahead and do that. I suggest doing the URL method

[26:26] because it's very very simple and then we'll move on. So once you have that all ready to go, you're just going to prompt cloud code and say let's use the Playwright CLI to test out our kanban board. Come up with two tests and use headed browsers. Notice how I didn't

[26:39] even have to come up with the tests. I'm not an expert in testing kanban boards. Cloud code is going to do a better job than me of figuring out what we should test using this sort of tool. Secondly,

[26:49] I said let's use two headed browsers. What does that mean? Well, when it comes to browser automations, Cloud Code actually has the ability to use these browsers essentially in the background.

[26:59] They're invisible. You won't see like a Chrome browser pop up on your screen. But if you say use headed browsers, they will. So, if you actually want to see it

[27:09] working, you can do it that way. So, let's see what it comes up with. So here we can see cloud code opened up two browsers and you can see it quickly going through the cards, creating new cards, testing the colors, and again it's doing this all automatically on its own. Now that we've tested this thing,

[27:24] let's now talk about deployment. How do we take this web app that you built in cloud code and actually get it out onto the internet? Well, it's a two-step process. First, we're going to take all

[27:33] that code and we are going to push it to GitHub. From GitHub, we are going to push it to Vercel. And Vercel is what's going to put it online. Now the

[27:41] nice thing is all this is free. GitHub's free, Vercel is free and it's actually relatively simple. And we're first going to start in GitHub. Now I'm going to

[27:48] show you how to do all these things manually here for GitHub and Vercel. But understand they also have CLI tools. So once you understand manually how this process flows, then I highly suggest ask Cloud Code to download the GitHub CLI and the Vercel CLI. And from now on,

[28:02] you can just use natural language and tell Cloud Code, hey, push to GitHub. Hey, deploy in Vercel. So we're just going to create a new repo up here. Call

[28:10] it whatever you want. I'll call mine web demo one. For visibility, you can keep it on private. That's fine. And then

[28:16] you're going to do create repository. And once you're on this page, what you're going to do is you're just going to copy the URL of your GitHub repo. And we're going to go back inside of Cloud Code and say two things. Commit and push

[28:27] to the URL. Now, what does commit and push mean? Commit is a git command. Git

[28:34] is essentially just what we use to save our code. When I say commit, that's like creating a save point, right? So I'm saving it on my computer, but I don't want this to stay on my computer.

[28:43] I want it to go out to the internet, right? So I need to first push that to GitHub. So commit, we get the save point, and then we push all that save point code to GitHub with the push command. Now, when you do this for the

[28:56] first time, Cloud Code is going to have you authenticate with GitHub. Just follow its instructions. It should take you less than 60 seconds. But once you

[29:03] do this, it's that simple. And you should see a response from cloud code that says everything's been committed and pushed on the main branch. So if I follow this link and now all my code is inside this repository. So essentially it's almost

[29:16] like saving it into the cloud. But having it on GitHub isn't enough. We now need to move this to Vercel. So you're

[29:21] going to head to vercel.com. Again, it's totally free. When you sign up with

[29:24] Vercel, use your GitHub credentials so they're automatically connected. Once you're inside Vercel, just head to your project section and then go to add new project. Over here on the left-hand side, you should see your new repository automatically populate. You're going to

[29:38] do import and then we're just going to go ahead and deploy it. Now, if you were doing something a little more complicated, a project that had like API keys and stuff like that, you would add the environment variables here. But for today, we have something very simple.

[29:48] And now it's deploying it onto the web and it's going to give you a URL. If you get any deployment errors for whatever reason in this section, all you need to do copy the error, go into cloud code, paste it in there, and it will fix whatever it needs to fix. All right, it's deployed. Go back to the dashboard

[30:03] and you can see the URL right here. Now, if I want to add another domain, I have an actual custom URL. I can do that as well. But here it is. Here's everything

[30:13] we created on the web, right? I could share this URL with anybody and they can visit it. And now the big thing about this GitHub Vercel Cloud Code connection is any changes I make inside of Cloud Code and I test on my dev server and I like it, I just do commit and push again. That goes to GitHub. GitHub gets

[30:31] updated and then any updates in GitHub automatically trigger an update in Vercel. So it brings in all those updates and the live website will be deployed. Right? So that's why we have

[30:41] this cloud code GitHub Vercel framework. And with that we've kind of covered the essentials of cloud code. You understand how to install it, where to use it, best prompting practices, skills, CLIs, and now deployment. Now

[30:56] obviously the cloud code waters go really, really deep. And that's kind of where I would push you towards my master class. But with just this baseline, frankly, especially the prompting part and sort of that mentality thing we talked about, you're going to be way ahead of the game. So, if you're brand

[31:11] new to this stuff, I hope I was able to point you in the right direction. As always, let me know in the comments what you thought about this. Check out Chase AI Plus for the master class or the free community if you're looking for some beginner resources. And I'll see you

[31:24] around.
