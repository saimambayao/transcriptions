# Claude Code Cloned in 2 hours....

**Channel**: Wes Roth
**Duration**: 24:52
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=eR167BCL-4g
**Transcribed**: 2026-04-03 13:57

---

## Organized Notes

**The Leak and the DMCA Fallout**

- Anthropic accidentally leaked Claude Code's full source code ~48 hours before this video via an **April Fool's Tamagotchi pet feature** that exposed npm source maps
- Anthropic responded with **mass DMCA takedown notices** against GitHub repos — going "scorched earth," taking down not just infringing forks but also legitimate forks of Anthropic's own open-source projects
- This overreach was technically illegal; Anthropic retracted the overbroad notices and asked GitHub to reinstate wrongly-downed repos
- **Boris Cherny** is identified as the original creator of Claude Code and the one who responded to the DMCA overreach saying it was a "communication mistake"
- Irony #1: Anthropic's own AI coding tool shipped its source code by mistake
- Irony #2: The scorched-earth DMCA campaign *triggered* the very thing it was trying to prevent — a clean room rewrite that Anthropic cannot touch

**Claw Code — The Clean Room Rewrite**

- **Claw Code** (not Claude Code) was created as a clean room Python rewrite by an AI researcher referred to in the transcript as "Cigrid Jin" / "Jyn" (name possibly garbled by auto-captions — identity uncertain)
- The rewrite took **two hours** and is described as the fastest GitHub repo ever to reach 50,000 stars (reached in 2 hours); later crossed 117,000+ stars
- Written in Python; a Rust port followed within a day
- Launched under **MIT license** — fully permissive, usable for any derivative work, including model-agnostic harnesses (Claude Code was Anthropic-models-only; claw code accepts any model)
- The tool used: **Oh My Codex (OMX)** — a workflow layer built by the same developer on top of OpenAI's open-source Codex; used as the agentic scaffolding to perform the clean room rewrite
- **OpenClaw** (separate project by **Peter Steinberger**) is mentioned as another fastest-growing GitHub repo ever, crossing 200,000 stars within weeks

**Clean Room Development Explained**

- **Clean room engineering**: recreating software's *functionality* without using the original *code* — legally permissible because copyright protects code expression, not ideas or functionality
- Traditional clean room process: two teams — a "dirty team" that analyzes the original software and writes functional specs; a "clean team" that builds from those specs alone, never touching the original
- This process historically required many highly-paid developers and lawyers and took significant time
- **AI compressed that entire process to 2 hours**: AI acts as both the dirty team (analyzing the source code) and the clean team (rebuilding from scratch in a different language/framework)
- Analogy used: **Photopea** (photop.com) — a fully functional Photoshop clone built independently; perfectly legal because it recreates functionality, not code
- Claw Code is **DMCA-proof**: Anthropic cannot legally challenge a clean room reimplementation that didn't copy proprietary expressions

**Cigrid Jin's Article — What the Code Actually Proves**

- The author's key argument: *"If you're staring at the generated Python files, you're looking at the wrong layer. The code is a byproduct."*
- The real signal is the **agent coordination system** (ClawWhip + OMX) that produced the files while the developer was asleep
- **System architecture described**:
  - Developer types a sentence into **Discord**, puts phone down
  - Agents read the message, break work into tasks, assign roles, write code, test it, argue, fix failures, push
  - Human checks in the morning — port is done
  - Developer's interface: Discord chat + a send button; terminal sessions belonged to the agents
- **Three tools that formed a closed development loop**:
  1. **Oh My Codex (OMX)** — agent coordination logic between multiple agents
  2. **ClawWhip** — notification and event router running as a background daemon; watches git commits, GitHub issues, etc.; keeps monitoring work *outside* agents' context windows
  3. (Implicit: the underlying agent workers)
- Referenced a hackathon philosophy: *"Stop staying up all night at hackathons typing code by hand. That era is over. Spend your energy designing agent systems and setting up the coordination between them. You sleep; they work."*

**The Skill Shift — What Becomes Valuable**

- The key question: *"When a system can port an entire codebase in 60 minutes, what becomes expensive?"*
- Answer: **knowing what to build**, **why**, **how the pieces fit**, **clear mental model of target architecture**, **task decomposition**, **multi-agent coordination design**
- *"A faster agent does not reduce the need for clear thinking. It increases it."*
- Fear floating around developer communities: AI types faster → developers unnecessary. But what Cigrid Jin actually did during those 2 hours: typed maybe **10 sentences into Discord**
- *"The skill that produced claw code was not typing speed. It was architectural clarity, task decomposition, and system design. Those do not get cheaper as agents improve. They get scarce."*
- Four job categories predicted to survive in tech:
  1. **Vibe coders** — move fast with AI, think in product terms
  2. **Security and infrastructure** engineers
  3. **Client-facing roles** — humans pleasant to deal with; adults in the room (legal, finance, regulators)
  4. (Implied: judgment/taste roles)
- None of these four are about writing code — what survives is **judgment, taste, stability, human connection, conviction about what to build**

**The AGI-ASI Window — Individual Impact Spike**

- Wes Roth's thesis: there is a **narrow window between AGI and ASI** where a single individual's potential impact on the world will be historically unprecedented
- Pre-AGI: individual impact was relatively stable and modest
- Post-AGI / pre-ASI: **one person + a computer = capability never seen before in history**
- Post-ASI: AI takes over most discovery/scientific progress; individual contribution diminishes again
- The peak is *now or soon* — examples already happening (Cigrid Jin rebuilding Claude Code in 2 hours; Peter Steinberger's OpenClaw)
- Wes Roth's closing question: *"If building was easy and cheap and you just had to keep going with it — what would you build? That just might be the most important question of our time."*

*Quotable Quotes:*

> "If you're staring at the generated Python files, you're looking at the wrong layer. The code is a byproduct." [15:00]

> "A faster agent does not reduce the need for clear thinking. It increases it." [19:18]

> "The skill that produced claw code was not typing speed. It was architectural clarity, task decomposition, and system design. Those do not get cheaper as agents improve. They get scarce." [19:45]

> "Stop staying up all night at hackathons typing code by hand. That era is over. Spend your energy designing agent systems and setting up the coordination between them. You sleep; they work." [18:39]

> "If building was easy and cheap, and you just had to keep going with it — what would you build? That just might be the most important question of our time." [21:13]

---

## What This Means for Your Work

This video lands directly on what you're already doing — and sharpens the frame. You're already building 9+ platforms as a solo developer, running 129 skills, and using parallel agents. The Cigrid Jin thesis doesn't challenge your direction — it **validates it and raises the bar**.

The specific insight worth internalizing: the developer who rebuilt Claude Code in 2 hours didn't *write code for 2 hours*. He **designed a task decomposition**, **typed 10 sentences**, and **went to sleep**. The distinction between you today and the highest-leverage version of yourself is not more Claude Code sessions — it's whether your Claude Code sessions are producing systems that run while you're offline.

**For your active projects:**

- **e-Bangsamoro (4-portal platform)**: You're building the highest-complexity project in your stack. The bottleneck is not Claude's capability — it's your ability to hold architectural clarity and decompose the work into agent-executable tasks. This video is a case study in what that looks like at the extreme. The parallel agent workflows your skill library already supports (via `/spawn`, `superpowers:dispatching-parallel-agents`) are the right scaffolding. The gap is likely in *monitoring and event routing* — the ClawWhip layer that keeps track of what agents have done without clogging their context windows. Your current setup lacks this.

- **Parliamentarian and BTA legislative tools**: The article's "four surviving job categories" — vibe coder, security/infra, client-facing, judgment/taste — maps directly onto what you're building for BTA MPs. The legislative tools you're building (bill analysis, jurisprudence search, Bangsamoro governance context) are not about writing code faster. They're about **surfacing the judgment layer** — giving MPs clarity on what to legislate and why. That's the high-value lane that survives.

- **MoroTech and MoroAcademy**: If your social enterprise thesis is that Bangsamoro communities can be equipped with AI-leveraged capacity, this video is the frame for what "AI literacy" means at the cutting edge: not prompting, but **agent system design**. That is a curriculum insight worth capturing before you finalize MoroAcademy's AI modules.

**The AGI-ASI window thesis is personal.** You are a Bangsamoro solo developer building governance, legislative, and social enterprise infrastructure during the window Wes Roth describes. If the thesis is right — that this is the historical peak of individual leverage — the scarcest resource is not code, time, or money. It is **conviction about what to build and the discipline to keep going**. That is a standard to hold yourself to.

### How This Can Improve Your Claude Skills and Workflows

**Existing skills the video directly challenges or validates:**

- **`superpowers:dispatching-parallel-agents`** and **`superpowers:subagent-driven-development`**: You already have the agent parallelism skills. The gap identified by this video is the *coordination infrastructure* — the equivalent of ClawWhip (event routing, git monitoring, keeping agents' context clean) and OMX (coordination logic). Your skills handle parallel dispatch but don't yet wire in a persistent monitoring daemon that watches git commits and routes events to agents asleep in the background. This is a potential gap worth tracking.

- **`/devwork` (e-Bangsamoro feature dev workflow)**: Your frontend-first development workflow is well-structured, but the video validates going further: the developer's interface should eventually be a Discord message (or equivalent), not a Claude Code terminal session. The skills and task decomposition system you run are the spec layer. The logical next question is: what does a closed overnight loop look like for a feature you're building?

- **`/schedule` and `CronCreate`**: You have scheduled remote agents capability. This is the closest existing analog to "you sleep, agents work." Worth revisiting whether your scheduled agents are architected as closed loops (write → test → push) or just single-shot tasks.

- **`superpowers:brainstorming`** and **`superpowers:writing-plans`**: These are your task decomposition layer — the most critical skill the video identifies as scarce and getting scarcer. These are already some of your strongest skills. Worth making sure they produce outputs structured for agent delegation, not just human execution.

**New skill opportunity — not yet in your 135-skill library:**

- **`/agent-loop`** or **`/overnight-dev`**: A skill for designing *closed agent development loops* — the architectural pattern described in this video. It would formalize: (1) task decomposition into agent-executable chunks, (2) monitoring setup (what signals trigger handoffs), (3) verification gates (what must pass before push), (4) morning review format. This is distinct from your existing `devwork` skill, which is session-based. This would be a *session-independent overnight execution* pattern.

**Cross-domain insight — Bangsamoro governance:**

The clean room development story is also a **legal doctrine story** (copyright protects expression, not ideas). This connects directly to your `/legal-researcher` and `/bill-drafter` skills. There may be a Bangsamoro IP/technology bill angle here — the question of what IP frameworks are appropriate for a region building digital public goods. That is a policy design question no one in BARMM has asked yet.

---

## Transcript

[00:00] So apparently Claude code just went open source. If you haven't heard the last 48 hours in the world of AI have been absolutely mindblowingly just insane. It all started when Anthropic updated Claude Code to have some new features.

[00:14] One of them is an April Fool's little pet Tamagotchi thing that they wanted to add and accidentally they leaked the entire source code for Claude Code that happened about 48 hours ago. The internet was able to extract the source code, copied, cloned it, forked it a million times. At which point, Enthropic went completely scorched earth, issuing the DMCA takedown notices against just everybody. A lot of them technically

[00:36] illegal. We'll get to that in just a second. But all this in the end resulted in this this beefy fella over here. This

[00:44] is claw code. Not clawed code. Claw code. Like claw. What is claw code?

[00:50] Well, it's the fastest growing open source project on on GitHub in the history of the world, apparently. Apparently, anything with a claw in the title becomes the fastest growing project on GitHub ever. It's almost like a rule now. So, this is the fastest repo

[01:04] in history to surpass 50,000 stars reaching the milestone in just 2 hours after I have a new webcam and I I can't throw up certain hand gestures like apparently the P sign because it picks up that command and that means that it goes into a different mode. So, I got to be a little bit careful. So, it reached the milestone in just 2 hours after publication. This is going to be

[01:21] awkward. Okay, so what happened here? There's kind of a lot happening. It's a

[01:25] little bit hard to explain. In a nutshell, here is Cigrid Jin. This guy is kind of a beast. He got featured in a

[01:32] Wall Street article called the trillion dollar race to automate our entire lives. So, here he is. AI startup worker Secret Jin single-handedly used 25 billion of Claude Code tokens last year.

[01:45] So, he knows his way around cloth code, you can say. So, Secret Jin woke up at 4:00 a.m. I guess yesterday, one

[01:52] morning, and saw the massive amounts of DMCA requests that Anthropic was sending out. Again, Anthropic kind of, you could say, overreached a little bit because they started taking down not just things that were sort of they were legally able to take down, but also lots of other things where that law does not apply. We'll get to that in a second. But Jyn

[02:12] decided to completely rewrite cla code. And this is important because as we talked in the last video, this is going to be a big big deal moving forward. Not just for the situation, not just for cloud code, just for software as an industry and how AI is interacting with it. You're going to be hearing this term

[02:30] quite a bit. It's called clean room. Clean room engineering, clean room development. Whatever clean room

[02:36] basically means we're taking existing code and we're recreating the functions of that code without using the actual codebase. Basically, copyright laws protect existing code. So, if you write some software, you create the code for it. People love it. You're you're

[02:50] selling it. Somebody else can't just copy and paste your code and sell the same software. It's protected by copyright. But copyright does not

[02:58] protect ideas or in this case certain functionality. So if somebody creates a software that does the exact same thing, right? So all the functions and features that you've implemented, they've recreated those functions and features in their own software. Well, that's

[03:13] perfectly legal as long as they didn't use your code. There's a project online called photo p. It's at photop.com. P

[03:20] spelled pa. It's basically Photoshop. It has all the functionality that Photoshop has. This is perfectly legal. So what

[03:27] Jyn did was he rewrote Claude code in Python. He basically recreated Claude code. How long did it take him? Did it

[03:34] take him days, months, years? No. As he's saying here, people are losing their minds over the fact that the clean room Python writing of claw code took two hours. I can't put my fingers up

[03:45] like that anymore. Two hours. Just two hours. I need to disable that feature on

[03:48] my camera. Sorry. And we did Rust rewriting in a day. A complex Asian

[03:52] system reversed engineered and re-implemented from scratch before sunrise on March 31st. Repository crossed 50,000 stars in two hours. It's past 117,000 now. Okay, for those that are not

[04:05] following along, I'm going to use a photo. Again, this Photoshop clone that is perfectly legal to help you understand what's happening. Okay, if you used Photoshop, you know this is very, very similar to Photoshop. So,

[04:16] imagine if I have some software here that somebody else created. If I copy it and I call it something else, software 2, right? If I just copy the code, then I go to jail or I get into some legal trouble. That is not allowed. But if I

[04:31] create the same exact sort of software in terms of its functionality, of its abilities, just like this Photoshop thing that does everything, but it's not Photoshop. It's recreated from scratch by a developer. It didn't use the same code, but it has all the same functionality. So the original software

[04:45] and and my software, they're, you know, more or less identical. They're just this one's rewritten from scratch. It's rewritten in a different code or a different coding language or whatever.

[04:54] It's from scratch. Well, this is perfectly legal. So, this is where we get to this idea of clean room development. So, originally what it

[05:02] meant is that this was a methodology used to independently recreate a software or technology to avoid copyright or patent infringement. It involved two teams. One analyzes the target product to create a functional specifications while a separate isolated team uses only those specs to build the new product ensuring that no proprietary information is copied. So it's almost

[05:23] like this not a loophole but it's a process which technically makes it perfectly legal. So you can think of it as having a a dirty team but that dirty team doesn't actually build your product. They just do sort of the reverse engineering and then you have a a clean team that builds your product but but they're not interacting with the dirty team. uh if that makes sense. But

[05:41] as you can imagine, you know, there's a lot of complications here. Notice we're talking about different teams of developers, right? So you have a lot of highly paid people, developers. I'm sure

[05:50] there are lawyers involved to make sure all the protocols are followed, etc. This is a complicated process, tons of work in order to legally recreate software. And that process happened with clawed code turning into claw code over 2 hours. How did that happen? How is

[06:08] that possible? I think you already know the answer. It's with the magic of AI.

[06:12] AI is your clean team. AI is your dirty team. It takes, you know, the claude code, the entire harness, the entire source code of everything that claude code is. Because remember, cloud code is

[06:23] basically a harness. You can think of it around whatever model you want really. But with cloud code, Anthropic restricted it to be cla models only.

[06:31] Anthropics models only. By the way, if this new version, you can put whatever model you want. But the point here is that clot code was software. It was

[06:39] software where you put the model in. But cloud code is a harness and that harness is now fully recreated and open source. They have the MIT license, a very permissive license. So you can use it

[06:48] for whatever you want. You can use it to create your own derivative works everything. So here Jyn continuously saying developers are excited. A good

[06:54] number of them are terrified because as you can imagine there's well there's some things that are a little bit scary about this. Watching a code base of that size get rebuilt at that speed feels like something broke in our timeline. For some, it looks like a superpower they want to learn. For others, it looks

[07:08] like a pink slip. I think Jyn really strikes at the heart of this. If you think about it, Anthropic hired some of the best engineers and machine learning researchers in the world. And they

[07:17] through meticulative testing were able to create the harness for cloud code. They needed to be excellent software engineers. They also needed to be excellent machine learning researchers.

[07:28] They kind of needed both those skills. They need to have that skill stack, if you will, to be able to intelligently build something like clawed code. And as they were building it, they were also learning new things, iterating. Like

[07:38] this wasn't something that just anybody could have done. This code was expensive. This code was valuable. This

[07:45] code was proprietary. It was behind sort of locked doors. It gave Enthropic massive advantage over the competition.

[07:53] And they're planning to IPO later this year. Certainly, this would be one of those things, one of those assets that would increase how valuable the company was. All of that got cloned in two hours. Now, let's come back to this

[08:04] article by Jyn. By the way, I recommend that you read it. Again, this is a person that is obsessed with these gentic harnesses. This is a person that

[08:13] burned through how many 25 billion tokens I think they said. You know, this is somebody that knows a thing or two about AI agent. And by the way the tool that he used to you know clean room develop this thing was he calls it oh my codeex which is a workflow layer that sits on top of openi's codec. So open

[08:29] codex is open source. Jyn built some stuff on top of it called it oh my codex or omx but kind of ironic that openai open sourcing codeex was the thing that was used to open source with without consent I guess to open source cloud code. Something about that is is interesting. But it's important that

[08:49] this thing claw code is DMCA proof. Copyright doesn't protect ideas or expression or functionality or architectures only specific expression. Right? So if a developer writes code

[09:03] that code how it's written that's protected. You can't copy and paste that code. Just like JK Rowling can write about a wizard and those specific description of of events that that those books they are protected and certain names can be protected but the ideas aren't. I can create a book about mages

[09:21] that go to a university and play some game on on broomsticks. So this new claw code it captured the architecture that is clawed code. It's a clean room rewrite and anthropic cannot legally touch it. Now, when the files got

[09:36] leaked, so Enthropic, it was, you know, it was their fault that they leaked those files and they quickly started sending out DMCA requests, which is a way for companies to protect their work if they're getting shared online. Specifically here in the United States, for example, if you have some sort of a platform where users can share information, you know, pretty much everything YouTube, GitHub, Facebook X, all of that stuff falls under that umbrella. If a user posts something that's against the law, they don't have the copyright. They're engaging in

[10:03] piracy. We have certain laws that protect the network from, you know, taking the fall, taking the blame for it, they can blame it on the user as long as they follow these DMCA laws. So this allows the owner of the copyright work to be like, you got to take that content down. And then Facebook or

[10:17] YouTube or GitHub or whatever, right, they they take the content down. This actually, in my opinion, is an example of where regulations work beautifully. I mean, it's not perfect. It's far from

[10:26] perfect, but it it works. So, Enthropic uses these laws DMCA to just nuke a whole bunch of repos that cloned the leaked source code from Anthropic. And you can see the takedown requests here.

[10:38] So, GitHub does share it. And so, here's like a whole long list of things that they want taken down. Here's the problem. This went kind of overboard

[10:47] when I was saying anthropic went scorched earth. What I mean is they didn't just go specifically after kind of the infringing people that were forking the actual source code. GitHub went after any fork of any anthropic project. So there's a lot of things

[11:02] there that were not infringing but still got taken down. Now this is technically illegal. This is not how the DMCA should work. And Anthropic did retract that

[11:12] statement. Again, everything is public. Everything's online. So they said we

[11:15] retract that. So please reinstate the repos that we wrongly took down. We only meant to take down these. So they're

[11:21] saying please reinstate all other repositories that were disabled by the networkwide process. So this is Boris Cherny. So he is one of the main people behind Cloud Code. I think he's the

[11:31] original creator. So now he's got a team that's that's helping him. But this is the guy that kind of created like a lot of this. It's surprising how much this

[11:39] one person does. By the way, if you recall that Wall Street Journal article, he also makes an appearance in here somewhere. That is him, Boris Leads Cloud Code at Anthropic. And so when

[11:48] these DMCA notices were taking down repos that should not have been taken down, of course, the community was outraged. As they're saying here, this is not an April Fool's joke. Anthropic seems to be issuing mass DMC requests on code that are legit forks of Anthropic's own claude code repo. By the way, it's

[12:04] also breaking of the law to file a DMC on something that never broke it. So, Boris did respond saying this is not intentional. They're working with GitHub to fix it. Elsewhere, he mentioned that

[12:13] this was a communication mistake. Maybe some communication broke down between Anthropic and GitHub. There was this Alanis Morset song back in the days called Ironic where she sings about these ironic situations. I don't I don't

[12:24] think any of them were actual ironic situations. I'm considering using Asuno. They have a new model that's out to actually write a song that lists all of the ironic things that happened here.

[12:35] So, think about this. The AI coding tool that Anthropica created to write better code shipped its own source code accidentally. Now, that's slightly stretching it. Anthropic did say it was

[12:45] a developer mistake. So, it was a human mistake, but they also took responsibility for it saying that it's more of a structural problem, right? It's not one person's fault. They should

[12:54] have had some safeguards in place. But layer of irony number two is Enthropic goes and issues these DMCA requests that actually target forks of their own open-source structures that they meant to put out there. Also, that kind of scorched earth DMCA takedown requests.

[13:09] That was the actual thing that triggered the clean room rewrite of the entire claude code database into claw code and it became the fastest growing ever thing on on GitHub. That is ironic. I'm pretty sure like we can all agree, right? If

[13:26] you're trying really hard, you're going to like DMC request everybody to take down everything. And those very efforts trigger the the thing that makes it escape and be completely outside of your control because now it's it's its own thing and you can't DMCA take it down. Right? That's kind of like the next

[13:42] layer of irony is that that new clean room rewrite is DMCA proof. Enthropic can't touch it. Claw Code also launched with a a press release very very publicly. And as a part of the leak,

[13:54] we've uncovered that claude code. Part of that they had this undercover mode where basically they would use claude code to go and change various repos. It was specifically said that claude code shouldn't ever say that cloud code made any of it or made any changes. So it's

[14:09] basically a way for anthropic to hide anthropic's involvement in insert development processes. That mode, that feature got leaked in this process. I mean you you can't make this stuff up.

[14:20] It happened on April Fools. I mean, you can't make this stuff up. This is real life. But really fast, I do think it's

[14:27] important for us to point out this article by Jyn. So again, he's the person behind a lot of this. And so his initial point about the fact that developers are excited or terrified. You

[14:36] know, this is what a lot of people are going to be talking about. How is it possible to create a clean room implementation of something this massive in two hours? How does how does it affect the software development industry? But his point, what he's

[14:48] saying is is something a little bit different. And keep in mind this is a person with 25 billion cloudcoded tokens that were used. This is a person that somewhere else he mentions that he's obsessed with the agentic scaffolding.

[15:00] So this is somebody that lives and breathes AI agents. He's saying if you're staring at the generated Python files, you're looking at the wrong layer. The code is a byproduct. The Rust

[15:09] port that followed is also a byproduct. The thing worth studying in the claw code repository is the system that produced all of it. Claw code was always a showcase. The point was never the

[15:19] Python files or the Rust crate. The point was the Clawip based agent coordination system that built them while the developer was asleep. By the way, I'm still trying to understand everything within the system. So, keep

[15:31] in mind it's been less than 48 hours at this point. So, I think everyone's slowly processing everything, but there's like a lot to process. So, Claw Whip is this harness engine. I think

[15:41] this whole thing will deserve its own video down the road. So he continues, "Here's what the system actually looks like in practice. A person opens a Discord on their phone, types in a sentence, and puts the phone down. They

[15:52] might go make coffee. They might go to sleep. The agents read the message, break the work into tasks, assign roles amongst themselves, write code, test it, argue over it, fix what fails, and push.

[16:02] When everything passes, the person checks back in the morning. The port is done. No terminal, no IDE, no SSH session, no split pane Vim setup, Discord, a chat." By the way, if you

[16:13] don't know what these things mean, that's kind of the point. We're approaching a time or maybe we're in the time when maybe you no longer need to. I know a big part of people watching are developers. The people who are

[16:26] non-developers, pay attention because maybe you have never used a terminal or you know what SSH is, but if you can use a chat app, the amount of things that you're going to be able to to do with that by relying on these AI coding agents, well, it's changing rapidly. By the way, it doesn't mean that you don't have to learn anything, but it might mean that this is like the best time to start learning a lot of this stuff. He continues, "This is the part that most people skip over, right? The read

[16:50] includes the screenshots of the OMX, oh my codeex workflow running in terminal panes, and people assume the developer was sitting in front of those panes the whole time, manually steering each step. The terminal sessions belong to the agent. The human's interface was a Discord channel, a text box, a send button. three tools that make this work

[17:09] and they each handle a different part of the problem. I'm going to quickly summarize, but do read this article. It's not that long and uh it's going to be an important one. It has 66,000

[17:18] views. That's criminally low. So, he mentions the Oh my CEX OMX. So, that was

[17:22] built on top of OpenI's open- source codeex. Then we have Clawhip or I assume it's claw. The claw whip like you're whipping the claw, I'm assuming. Clawhip

[17:32] is the notification and event router running as a background demon. It watches git commits, github issues and etc etc. The point is this thing claw whip keeps all monitoring work outside of the agents context window and the oh my open agent provides the coordination logic between multiple agent. Here's

[17:50] kind of the important part. None of these tools alone would have shipped clock code in an hour. Wired together they form a closed development loop. The

[17:58] human provides directions through discord. The agents provide labor. The human that kicked off the process they may be sleeping. they might be making

[18:05] themselves a sandwich. The agents they keep working. He mentioned this at a Ralph sponsored by OpenAI that took place in San Francisco, saying if you've been to that one you already know this idea. The philosophy behind those events was specific and practical. Here it is: stop staying up all night at hackathons typing code by hand. That era is over. Instead spend your energy designing agent systems and setting up the coordination between them. You sleep. They work. And here's kind of the next smart question to ask. If you've sort of internalized what he's saying, this idea that you should no longer be the one writing code, you should be building systems, the processes that that build the code, optimizing agentic swarms, as it were, right? If if if that's the thing that

[18:51] you should be doing, if that's the thing, that's the new desired skill, that's the killer skill, what's the next important question? Well, when a system can port an entire codebase in 60 minutes, what becomes expensive? And the answer is knowing what to build, knowing why, understanding how the pieces should fit together, having a clear mental model of the target architecture, being able to decompose that into tasks an agent can execute, and knowing how to set up the coordination so multiple agents stay productive in parallel.

[19:18] These are the skills that get more valuable as agents get stronger. A faster agent does not reduce the need for clear thinking. It increases it.

[19:25] There's a specific fear floating around the developer communities right now. The worries that AI will type faster than humans and make them unnecessary. Claw code looks like confirmation of that fear on the surface. One hour an entire

[19:37] system rebuilt. But look at what the developer actually did during that hour. He typed maybe 10 sentences into a Discord channel. The skill that produced

[19:45] clock code was not typing speed. It was architectural clarity, task decomposition, and system design. Those do not get cheaper as agents improve.

[19:54] They get scarce. Please do read this article cuz there's tons of stuff in there. This person is a very clear thinker, a great author. He's slicing

[20:03] through time and showing you a glimpse into the future. I wish I could do it justice, but I also don't want to read the whole thing. So, please, please read it. I'll I'll link it. What I'll do is

[20:11] I'll have a link to a post that's going to have all of this, including all of the links, and little summaries that's going to go out as part of my newsletter. You should sign up, but all of this will be available whether or not you're signed up for the newsletter, including links to everything that we've talked about here. But his point is that the gap between can build and cannot build is closing fast. Developers used

[20:30] to compete on what they could build. Now that differentiator is kind of being erased. So what do people compete on instead? Well, noise, visibility, social

[20:38] positioning. There's a post circulating that only four jobs will survive. This at least in the tech companies going forward. So it's vibe coders who move

[20:45] fast with AI tools and think in product terms. Then you have your security and infrastructure people. You have people facing roles, right? These are humans

[20:53] who are pleasant to deal with and also adults in a room, right? People who can slow things down. Legal, finance, regulators, etc. And he's saying that he

[21:01] thinks about this list and it feels roughly right. What those four categories have in common is that none of them are about writing code. What's left is judgment, taste, stability, human connection. It's conviction about

[21:13] what is worth building. The most important question of all might just be what will you build? If you could build anything theoretically, if it was easy, cheap, you just had to stick with it. If

[21:24] you just had to keep going with it, keep iterating. If building it was something that most people could do if that wasn't the limiting factor, what would be the thing that you might want to build? That just might be the most important question of our time. Think about this

[21:38] on the timeline of kind of the human civilization. Let's say this is AGI and you know this is ASI. very nebulous terms I understand. You know, don't ask

[21:50] me what the definition it is. No one knows. The point is this is where AI is as good as a human. ASI is where it far

[21:57] exceeds the human and potentially even the entirety of human intelligence. Think about how much agency and ability to change the world any single human individual had throughout time. It might be one person or or a small group of people. We're not talking about massive

[22:13] organizations, kingdoms, countries, armies. We're talking about one person or just a small handful. For most of human history, the amount of impact those people could have there was it's some, but it wasn't great. You can argue

[22:26] if it was more or less, but the point is it was pretty much stable. I would also argue that in the future, assuming there's ASI, assuming there's super intelligent machines in the future, the amount of things that humans will be able to contribute in terms of scientific progress or discovery, it will be less. Most of those things will be handled by AI, right? So in the

[22:44] future, you know, we might also have, you know, our ability to impact the world. Yeah, maybe it'll be there, but it's not going to be drastic for any single individual. But I believe, and let me know what you think about this if I'm wrong, but I believe that post AGI and before ASI, the impact that one human, one individual could potentially make, it's going to spike. post AGI it

[23:05] will be reduced but there will be this moment in time when just one person in front of a computer will be capable of doing insane incredible never-before-seen things do you agree with me think about somebody like Peter Steinberger the creator of openclaw the fastest growing open source project on GitHub of all time it surpassed 200,000 GitHub stars within weeks and now this project claw code again created by Jyn under two hours by the way if you're saying, "Oh, what did he do? He just copied somebody else's work." If you're saying that, you're not listening to what he's saying in this article. The

[23:42] code is a byproduct. Don't look at the code. That's not what he created. That's

[23:47] not what he did. Stop, as he says, staring at the files. So, let me know if you agree with me or not about this idea. There's be there will be this peak

[23:56] where the potential of a single individual will become absolutely great, greater than we've ever seen before in history. and potentially even ever after that point, you know, assuming ASI rolls around, it kind of takes things over, so to speak. But do you do you agree that this is going to happen because from where I'm sitting, it sure feels like it's beginning to happen right now? Like

[24:18] we're seeing examples of this happening right before our eyes. The question becomes, are you going to be one of those people? Number one, and number two, what would you build? I look

[24:27] forward to hearing your answers. My name is Wes Roth. Please subscribe. I don't

[24:32] have anything to sell you. I am just trying to in my own small way to have some positive impact on the world. And if this is helping you, I'd like for us to take this further if you know what I mean. Don't come over to my house, but

[24:43] you know, just subscribe, hit the thumbs up, maybe share this video with someone that you think might find it useful. With that said, thank you so much for watching. I'll see you in the next
