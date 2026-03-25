# Claude.md is RUINING Claude Code (w/ One Exception)

**Channel**: Chase AI
**Duration**: 11:51
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=V3xDTx2XwGg
**Transcribed**: 2026-03-24 09:35

---

## Organized Notes

**What claude.md Files Are**

- **Claude.md files** are markdown text files that give Claude **persistent context** about a project
- They act as **system prompts** — appended invisibly to every single prompt you send
- Used to set **conventions** like indentation style, test-before-commit rules, project architecture
- **/init** is a Claude Code command that **auto-generates** a claude.md by scanning your entire project

**ETH Zurich Research: Context Files Make Agents Worse**

- Researchers at **ETH Zurich** published a report called **"Evaluating agents.md"** testing context files across multiple agents and benchmarks
- Key finding: context files **reduce task success rates** compared to providing no repository context
- Inference costs increased by **over 20%** when context files were present
- In **5 out of 8 tests**, having **no claude.md file outperformed** having one
- Even **stronger models** didn't generate better context files — the problem is architectural, not content quality

**Why claude.md Files Hurt Performance**

- **Ineffective overviews** — agents took as many or more steps to find correct files, not fewer
- **Redundant documentation** — Claude Code already traverses the codebase and discovers what it needs on its own
- **Excessive tool calling** — context files cause agents to search more files, read more files, and write more files unnecessarily
- **Context pollution** — conventions about irrelevant topics pollute the prompt when 90% of the claude.md has nothing to do with the current task
- **Increased token cost** — all the extra processing from reading and following bloated instructions burns tokens

**The One Exception: Documentation-Free Repositories**

- When researchers **removed all documentation** (readmes, markdown files, example code) from a repository, LLM-generated context files **improved performance by 2.7%**
- In this scenario, claude.md **outperformed developer-written documentation**
- The key condition: claude.md was the **only source of documentation** in the entire codebase
- This scenario is **rare for coding projects** — most sophisticated codebases already have some documentation

**The Real Use Case: Personal Assistant Projects**

- The exception maps perfectly to **personal assistant type agents** — like an **Obsidian vault** connected to Claude Code
- These are **large repositories of markdown files** with no code architecture, no readme, no formal documentation
- They have **personal conventions** about communication style and interaction patterns
- This is the **perfect scenario** for a claude.md file — but **not one to use /init for**, since the conventions are about personal interaction, not file structure

**Anthropic's Updated /init**

- Anthropic made /init an **experimental feature** (must be flagged in settings)
- The new /init is an **interactive multi-phase flow** designed to be more minimal
- It pushes users toward **skills and hooks** instead of cramming everything into claude.md
- The core question it encourages: **does this need to be in every prompt**, or should it be a skill invoked only when needed?
- A **step in the right direction** but not a silver bullet

**Practical Takeaway**

- **Less is more** — most standard coding projects don't need a claude.md file
- If you're **not technical**, you're better off with **no claude.md** than a bloated /init-generated one
- If you do use claude.md, make it **manually written and super tight** — only things Claude Code wouldn't figure out on its own
- **Move specific behaviors to skills and hooks** instead of global conventions
- Claude.md feels like a **relic** from when coding agents needed more hand-holding — modern agents are effective enough to understand codebases without it

*Quotable Quotes:*

> "Your Claude MD file is making Claude code dumber. And this isn't just my opinion. This is coming from researchers in ETH Zurich where they tested this idea with multiple agents against multiple benchmarks." [00:00]

> "It's context pollution. And all this extra movement just requires more thinking, which causes more tokens." [05:09]

> "If this isn't something that you would add to literally every single prompt, then why aren't we making it a skill? Why aren't we making it a hook?" [10:39]

> "Less is more. You probably don't need a claude.md file." [10:57]

> "I think a lot of this just feels like a relic of times past where these coding agents just weren't as good at figuring out what was going on in the codebase without extra help. But now we've gotten to a point where they are so effective, we don't need to hold its hand." [11:12]

---

## What This Means for Your Work

**Your Obsidian vault is the textbook exception.** You run a 54-directory vault as your second brain — bangsamoro laws (78 BAAs, 546 resolutions), knowledge areas, 105+ transcripts, 129 skill archives, daily notes. No code architecture. No readme. Just a sea of markdown with personal conventions (YAML frontmatter, [[wikilinks]], specific folder routing). The ETH Zurich finding that claude.md improves performance in documentation-free repos validates exactly this. Without your vault CLAUDE.md, Claude Code wouldn't know that `knowledge-areas/` gets condensed takeaways while `research/` gets raw /deep-research outputs, or that new notes need frontmatter with date and tags.

**Your 9 coding projects each need a CLAUDE.md audit.** e-Bangsamoro, e-Negosyo/MoroMarket, Tarbiyyah-MS, BangsamoroHR, SBP, OBCMS, Parliamentarian, IPP — these are all coding projects where the research says context files hurt. Claude Code can traverse your React 19 components and Django endpoints to understand architecture. Strip out anything describing file structure, tech stack, or patterns inferrable from code. What to keep: Bangsamoro-specific naming conventions (BAA, BTA, BARMM terminology), multi-tenant RBAC rules, Railway deployment constraints, and the domain-specific facts Claude genuinely can't discover by reading source files.

**Your 129-skill architecture already follows the recommended pattern.** The video's core advice — "move behaviors to skills and hooks" — describes what you built over months. Your /bill-drafter, /policy-recommendation, /legislative-briefer, /fact-checker pipeline invokes domain knowledge on demand instead of cramming it into every prompt. The risk is duplication: if /devwork repeats frontend-first conventions already in e-Bangsamoro's CLAUDE.md, you're paying for both. Check your most-used project skills against their project CLAUDE.md files.

**Your markdown-only repos are the right place for context files.** Transcriptions (this repo), skills-bucket, and the Parliamentarian research platform are all documentation repos with complex routing conventions but no code architecture. These are the exception the research validated.

**Your OOBC consultancy work benefits from the skills approach.** Your 6-goal policy framework for Other Bangsamoro Communities (institutional strengthening, rights protection, social development, economic development, cultural preservation, peace advocacy) lives in skills like /policy-recommendation and /bangsamoro — not in a single bloated context file. Each gets invoked when relevant. The bill-drafting pipeline (/bangsamoro context → /bill-drafter → /fact-checker) is exactly the pattern this research recommends over front-loading everything.

**Practical next steps:**
1. **Audit e-Bangsamoro and e-Negosyo CLAUDE.md files** — remove file structure, component patterns, and architecture that Claude infers from traversal. Keep domain terminology, RBAC rules, and deployment config.
2. **Run /skill-optimizer on /devwork and /database** — these are your most-used project skills and likely have overlap with project CLAUDE.md files
3. **Keep vault, transcriptions, skills-bucket, and Parliamentarian CLAUDE.md files** — documentation-free repos where context files add genuine value
4. **Never use /init** — your manually written, domain-specific files drawing on your MPA training and 7 years of BARMM governance experience are tighter than anything /init generates

### How This Can Improve Your Claude Skills and Workflows

**The "move behaviors to skills and hooks" recommendation should trigger a migration audit of your CLAUDE.md files.** Go through each of your 9 platform CLAUDE.md files and ask: "Is this instruction something Claude needs on every single prompt, or only when doing a specific task?" Frontend-first development rules belong in /devwork (invoked when building). Bangsamoro naming conventions belong in /bangsamoro (invoked when creating governance content). Database migration rules belong in /database (invoked when modifying schema). Only truly universal instructions -- like "never commit without permission" or "use Railway for deployment" -- stay in CLAUDE.md.

**Your /skill-optimizer should include a "deduplication check" against project CLAUDE.md files.** When optimizing a skill, /skill-optimizer should first compare the skill's instructions against the active project's CLAUDE.md. If the skill repeats conventions already in CLAUDE.md (or vice versa), flag the duplication. Every repeated instruction consumes tokens twice -- once in the system prompt from CLAUDE.md and once when the skill is invoked. For high-frequency skills like /devwork, this duplication tax compounds across dozens of daily invocations.

**The ETH Zurich finding that context files increase inference cost by 20% should inform your /auto-research cost calculations.** If your project CLAUDE.md adds 20% overhead to every Claude interaction, then optimizing the CLAUDE.md itself is one of the highest-ROI /auto-research targets. Define the eval: (1) Task completion accuracy on 10 representative prompts, (2) Total token consumption per task. The variable to optimize: CLAUDE.md content and length. The goal: maintain or improve accuracy while reducing token consumption. Even a 10% reduction in CLAUDE.md tokens across all your daily interactions saves significant budget.

**The "documentation-free repo exception" validates your transcriptions and skills-bucket CLAUDE.md files, but with a nuance.** These repos are pure markdown with no code -- exactly the scenario where CLAUDE.md helps. However, even here, follow the "does it need to be in every prompt?" test. Your transcriptions CLAUDE.md contains transcript formatting rules, Bangsamoro content pipeline instructions, and language rules. The Bangsamoro content pipeline instructions are only relevant when transcribing governance content, not when processing AI engineering videos. Consider moving domain-specific transcription rules into /youtube-transcriber modes rather than keeping them in the global CLAUDE.md.

**Your hooks architecture is underdeveloped relative to your skills architecture.** The video recommends moving from CLAUDE.md conventions to skills and hooks. You have 129 skills but few hooks. Post-commit hooks (run /fact-checker on any markdown file committed to a governance repo), pre-session hooks (load /context automatically), and post-session hooks (/session-summary to vault) would encode behaviors that currently live in CLAUDE.md as executable automation rather than instructional text.

---

## Transcript

[00:00] Your Claude MD file is making Claude code dumber. And this isn't just my opinion. This is coming from researchers in ETH Zurich where they tested this idea with multiple agents against multiple benchmarks. And the conclusion was

[00:12] clear. These sorts of context files like claude.md make our agents worse, not better, and more expensive. So if that's

[00:21] the case, why is everybody still telling you that you need to start every project with a claude.md file? And is Claude Code's latest update to slash init actually fixed anything? In this video,

[00:31] we are going to cover all of that. I'm also going to discuss the one exception to this rule so you don't fall into this common trap. So, let's start by very quickly reviewing what claude.md files

[00:42] even are so we're on the same page here. So, claude.md files are just markdown files aka text files. They are

[00:48] instructions you write to give Claude persistent context. The idea is if I have a project, I'm going to have a claude.md file that lays out how the project is essentially set up. It's

[00:59] where I set conventions. You know, if I ever want Claude to always do something in a certain way every single time, the idea is you would put this in claude.md because Claude Code would always reference it. Emphasis on the always

[01:12] reference. Claude.md files essentially become system prompts. So, think of it

[01:16] this way. It's almost like every single time you prompt Claude Code in a project that has a claude.md file. It's like that

[01:22] claude.md file gets appended to your prompt every single time invisibly. Think of it that way. And /init is a

[01:30] command inside of Claude Code that will create a claude.md file for you for your project. It will go through your entire setup, go through all your architecture and figure out what should be in it. And

[01:38] it does it all automatically. And some sort of documentation like this makes sense in theory, right? Like if I always want Claude Code to use two-space indentation or to run npm test before committing and to have like some level of consistency, right? It makes sense,

[01:51] but what makes sense on paper doesn't always play out in reality as evidenced in this report from our researchers at Zurich. So this report is called "Evaluating agents.md." Think of agents.md

[02:02] and claude.md as the same thing, right? They're just context files that the AI agents are supposed to read to help them understand the codebase. And spoiler

[02:10] alert, what did these guys find? They found that across multiple coding agents and large language models, we find that context files tend to reduce task success rates compared to providing no repository context while also increasing inference cost by over 20%. Ultimately, we conclude that unnecessary requirements from context files make tasks harder and human-written context files should describe only minimal requirements. What does that mean? Well,

[02:37] that means in the eight tests they ran, having no claude.md file did better in five of the tests. And across all of the tests, if you had some sort of agents.md or claude.md, it ended up being

[02:49] 20% more expensive. Though the obvious follow-up from that is, well, why is it the case that when we give Claude Code additional documentation it actually does worse? But before we jump into

[02:59] that, just want to give a quick plug for my Claude Code masterclass. Just came out a couple weeks ago and since then we've already updated 20 plus modules and added an additional hour of content and it's all about taking you from zero to AI dev and basing it on real Claude Code use cases, not just explaining features. So if that sounds like something you're interested in definitely check it out in Chase AI Plus. There's a link to that in the comments and as always I also have the free Chase AI community links in the description for that if you're just getting started in the space. Now, back

[03:29] to answering the question, why does the claude.md file hurt Claude Code? Well, there's actually a number of reasons for this. The first is that these context files actually don't provide effective overviews. You would think if I gave

[03:42] Claude Code essentially a piece of paper that says, "Here's where everything is. Here's where you can find it." It would be able to find the correct file quicker. And that in fact was not the

[03:51] case. In these tests they ran, oftentimes it took as many steps or more steps to actually find the correct files based on whatever benchmark they were running. And remember, because each of these AI systems has to read that context file in the first place, it was more

[04:06] expensive for each and every step because it's thinking more. The second reason is that these context files are redundant documentation. When I tell Claude Code to do something, what is it going to do? It's already going to go

[04:17] through the codebase. It's already going to go through the search process and find out what it needs. So, it's doing that. Plus, it's taking a look at this

[04:24] bloated document you gave it, right? It's just excessive. It's not providing anything new or novel. Now, these files

[04:30] just aren't redundant. They cause excessive tool calling behaviors. You see that here. Adding context files

[04:36] causes agents to use more repository-specific tooling, right? They also tend to search more files, read more files, and write more files. And the issue is it's doing this for the sake of it. Why?

[04:46] Well, it's because the instructions in context files are typically followed. These agent systems are trained to follow the claude.md almost to a T, right? It treats it like a system

[04:55] prompt, which is great in theory, but in reality, right, if you have a bunch of conventions about a bunch of random stuff and your particular prompt at that time has nothing to do with 90% of what's in your claude.md, well, what's the point? In fact, it's hurting it.

[05:09] It's context pollution. And like we mentioned before, all this extra movement just requires more thinking, which causes more tokens. And these costs matter, especially if you're outside of some mega subsidized situation like Claude Code. And what's

[05:21] also interesting to know is that stronger models didn't generate better context files. So this isn't a situation where it's like the actual content of the file wasn't good enough or written well enough for AI. It's just like the architecture of it all. Even having it

[05:33] in there is a problem. So what does this actually mean for you and me? What sort of practical steps are we supposed to take now that we have this information?

[05:41] Should we just be deleting claude.md entirely, never using it, never running /init? Well, I think the reality is a bit more nuanced than that. So, the

[05:50] researcher's conclusion was that these context files have only a marginal effect on agent behavior. Many times it's negative and are likely only desirable when manually written. The idea is, hey, if it's going to be reading this every single time and we have issues with redundancy and we have issues where it's just doing too much, well, then we should have an actual human being go in there. They create the

[06:10] claude.md file and they make sure it's super super tight. They make sure this global context only has to do with things that Claude Code, for example, wouldn't naturally figure out just by going through the codebase. But that

[06:23] requires a certain level of knowledge and technical know-how that many people who are just stepping into the vibe coding space with Claude Code don't have, right? They don't come from a technical background. They're really just figuring this all out. If that's you, then I

[06:35] think the answer probably is delete the claude.md. You're probably better off with nothing than the bloat the normal /init route is going to give you versus trying to rely on your own technical know-how to get like the perfect super tight claude.md file. But I think it also really depends on the sort of project you're working on. And this

[06:54] is where we kind of go into the exception to this rule and this was kind of buried here in the report. So what they did with one test is they actually manually removed all documentation from a repository. So think of they removed like any additional markdown files, right? No example code folders, no like

[07:12] readme. So there was no documentation at all. And in those situations where claude.md was the only source of

[07:18] documentation in the entire codebase, LLM-generated context files consistently improved performance by about 2.7% on average and also outperformed developer-written documentation. Now what is that saying? That's saying, hey, in most of

[07:32] these tests, there were sophisticated codebases that already included some level of documentation, even something as simple as a readme. But if we essentially take out all the documentation, right, there's absolutely nothing there, and we then put in something like an agents.md or claude.md,

[07:50] then it actually improved it a little bit. Well, that's kind of confusing, right? So, you're saying the actual claude.md files are useful in very

[07:56] specific situations. Yes, according to this, there are very specific situations. Now, I think we need to take this with a grain of salt.

[08:04] All right, this sort of little test they did. First of all, this was with rather sophisticated codebases. This wasn't with a codebase that you just threw two prompts at it in one plan mode in Claude Code build. Those sorts of situations,

[08:15] like the vast majority of situations you will probably find yourself in, you don't need a claude.md file. Claude Code can already see the entire codebase and all of its inner workings in a simple pass and not use very many tokens. This

[08:26] is for stuff that is huge. Also, when we're talking about very large codebases, the chances are that there is no documentation in any form whatsoever in there at all is highly unlikely. So, this scenario is almost somewhat an unrealistic scenario. But with that

[08:42] being said, there is some stuff we can pull out of that. And that's the idea of, hey, claude.md files can work in large repositories that don't already include some level of context. And they

[08:52] aren't some like rather simple project someone's just spun up in a few prompts. Well, what sort of scenario describes that? Well, I think it's a scenario a lot of people of you are actually in, and that is personal assistant type agents. And when I say personal

[09:04] assistant type projects, I'm talking about something like an Obsidian vault that your Claude Code is connected to. Something like this where it's a giant repository of a bunch of subfolders and it's nothing but markdown files all the way down. There's no real code architecture for Claude Code to traverse.

[09:21] There's no readme for this thing. It's actually just a very wide, very populated, continually growing just like sea of documents. Yet, there are some conventions you would want Claude Code to follow in this instance because it's a personal assistant for you. It's

[09:35] something that's very, very personal and you probably have specific ways you want Claude Code to interact with you. This is the perfect scenario for a claude.md file, but it's also not one I would use /init in, right? Because what I want

[09:47] Claude Code to do in this scenario probably has less to do with how the files themselves are built and more to do again with like my communication style, right? So that's a perfect use case. Now speaking of /init, Anthropic recently made some updates to it. Now it's essentially an experimental

[10:04] feature. You need to go into your settings and actually flag it as true, but Anthropic understands this problem as well. So the new /init is an interactive multi-phase flow. It's meant

[10:14] to make it more minimal. It's meant to push you more towards skills and hooks, but again, like, does it actually solve the issue? Inherently, not really. It's

[10:24] definitely a step in the right direction. And I think the idea of getting you in the mindset of like, all right, does it need to be a convention that's in every single prompt, or is it just something I want done in a specific way at certain times? Right? If this

[10:39] isn't something that you would add to literally every single prompt, then why aren't we making it a skill? Why aren't we making it a hook? Like we already have ways inside of Claude Code to make it do specific things in a specific way — skills, right? So, do you need the skill

[10:54] invoked every time? No. Then don't put it in claude.md. Now, obviously, this is

[10:57] a step in the right direction, but I don't think it's a silver bullet. So, in conclusion, less is more. You probably don't need a claude.md file. There are

[11:06] certain scenarios where claude.md files make sense. We talked about them. Probably a personal assistant type thing. But if you're doing a standard

[11:12] normal coding project, unless you're someone who really knows what they're doing, I think the data points to just staying away from it, right? It's not really going to help you. Truth be told, I think a lot of this just feels like a relic of times past where these coding agents just weren't as good at figuring out what was going on in the codebase without extra help, without extra scaffolding. But now, like, we've gotten

[11:31] to a point where they are so effective, we don't need to hold its hand. Like, it's good enough to see what's there and what it needs to do. So, hopefully this was able to shed some light on it. I

[11:40] think this was a super interesting report. I will put a link to it down below. As always, let me know what you thought. Make sure to check out Chase AI

[11:47] Plus if you want to get your hands on that masterclass. And I'll see you around.
