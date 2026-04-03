# Claude Code was just leaked... (WOAH)

**Channel**: Matthew Berman
**Duration**: 15:00
**Language**: English (manual) [yt-dlp subtitles]
**URL**: https://youtube.com/watch?v=dYG8JxtSgmM
**Transcribed**: 2026-04-01 14:49

---

## Organized Notes

**The Claude Code Source Code Leak**

- **Discovery of the Leak**: The full source code of **Claude Code** (Anthropic's agentic coding harness) was accidentally leaked via a map file in their **npm registry**. Twitter user **Fried Rice** made the zip file of the repository public. [00:00]
- **Legal Context and Re-implementation**: To circumvent potential DMCA takedowns by Anthropic, the community has already rewritten the entire codebase in **Python**. This re-writing process makes the code "copyright unenforceable" according to the speaker, allowing it to be hosted and used legally by tinkerers. [00:27], [03:48]
- **Market Reaction**: Within 24 hours, the leak reached over **22 million views** on X. Even **Elon Musk** commented, jokingly stating that Anthropic is now "officially more open than OpenAI." [00:56], [01:28]

*Quotable Quotes:*

> "Claude Code source code has been leaked via a map file in their npm registry... Just it having been rewritten [in Python] makes it copyright unenforceable." [00:12]

> "The thing that makes Claude Code so special is the combination of the Claude Code harness itself and its pairing with the Claude family of models." [02:09]

**Technical Insights into the Claude Code "Harness"**

- **Harness vs. Model**: The key takeaway is that Claude Code is a **harness** (an orchestration layer) specifically optimized for the **Claude family of models**. While it can be modified to run other models (OpenAI, Gemini), it performs best when paired with Claude. [02:09]
- **Claude.md Protocol**: A critical discovery is that `Claude.md` (or similar project instruction files) is **loaded into every single turn** of the conversation. This file should contain coding standards, architecture plans, and best practices. [06:42]
- **Parallel Execution Models**: Claude Code is built for **parallelism**. It uses three primary execution models for sub-agents:
  - **Fork**: Inherits the parent's context.
  - **Teammate**: Runs as a separate terminal pane (tmux/iTerm) and communicates via a file-based mailbox.
  - **Worktree**: Uses a **git worktree** to isolate branches per agent, preventing merge conflicts between multiple running agents. [07:42], [08:13]
- **Permission and Automation**: The **auto permission mode** uses an LLM classifier to predict if a user would allow a specific tool action, significantly reducing the "Do I have your permission?" friction while maintaining security. [09:42]

**Context and Memory Management (Compaction)**

- **The Power of Forgetting**: The harness implements five distinct types of **compaction** to manage the 1M+ token context window efficiently:
  1. **Micro-compact**: Time-based clearing of old tool outputs.
  2. **Context Collapse**: Summarization of conversation spans (lossy).
  3. **Session Memory**: Extraction of key context (task specs, file lists, errors) to a persistent file.
  4. **Full Compact**: Complete history summarization.
  5. **PTL Truncation**: Dropping the oldest message groups. [10:31]
- **Efficiency Gains**: By using the `slash compact` command proactively, users can save their "workflow state" like a video game save point, ensuring that resumable sessions (`--continue`) are more efficient than starting fresh. [11:10]

**Advanced Workflow and Hooks**

- **Tool Partitioning**: Claude Code's 66 built-in tools are divided into **Concurrent tools** (read-only operations like file reads) and **Serialized tools** (mutating operations like edits and bash commands). This partitioning allows multiple sub-agents to read the codebase simultaneously without blocking. [13:18]
- **Power User Hooks**: The system supports **hooks** for automation, such as `pre-tool use`, `post-tool use`, and `session start/end`. These can be used to automatically update documentation or run linting after every file edit. [12:15]
- **Interruption as a Cost-Saving Strategy**: Because of the streaming architecture, **interrupting the model is cheap**. If a user notices the agent going in the wrong direction, stopping it immediately saves tokens and avoids the "sunk cost fallacy" of let-ting it finish a wrong implementation. [13:54]

---

## What This Means for Your Work

As a solo developer building government-scale platforms for the Bangsamoro region (e.g., **e-Bangsamoro**, **OBCMS**, **Tarbiyyah-MS**), the leak of Claude Code's internal mechanics provides a definitive blueprint for scaling your own **Gemini CLI** orchestration. The revelation that **Claude.md** (or your `GEMINI.md`) is the "secret sauce" for turn-by-turn alignment validates your current practice of maintaining high-density project instruction files. For your work with the **OOBC** and **BTA Parliament**, where legislative precision is paramount, adopting the **Parallelism** and **Compaction** strategies mentioned can significantly reduce the latency and token cost of large-scale legal research and bill drafting.

The **Git Worktree** execution model is particularly actionable for your **e-Bangsamoro** development. Since you are managing four distinct portals (Parliamentary, Ministerial, Budget, Citizen), you can now confidently dispatch parallel agents to work on separate modules in isolated worktrees, ensuring that a bug fix in the Ministerial portal doesn't block a feature update in the Budget portal. Furthermore, the **Session Memory** concept reinforces why you should avoid "starting fresh" in your legal research sessions for MP **Sittie Fahanie S. Uy-Oyod**; the persistent memory of previous bill versions and jurisprudence findings is your primary competitive advantage in legislative capacity building.

### How This Can Improve Your Gemini Skills and Workflows

This video directly informs several of your 135+ skills and suggests significant upgrades to your AI-augmented development workflow:

- **Skill Enhancements**: 
  - [[gitops]]: Integrate the **Git Worktree** pattern to allow your parallel agent teams (e.g., in [[sp-dispatching-parallel-agents]]) to operate without file-locking conflicts.
  - [[skill-optimizer]]: Use the **Compaction** strategies (specifically micro-compact and session memory) to improve the token efficiency of your long-running research pipelines.
  - [[fact-checker]]: Implement the **Post-tool Hook** pattern to automatically trigger a fact-check after any [[bill-drafter]] or [[policy-recommendation]] output, ensuring continuous verification.
- **New Skill Opportunities**: You could develop a dedicated **Agent Orchestrator** skill that explicitly partitions tools into "Concurrent" and "Serialized" categories, mirroring Claude Code's high-efficiency read/write split.
- **Workflow Optimization**: The "Interruption is Cheap" insight should become a core part of your **Frontend-first development** disciplinary rules. Stop the agent as soon as a UI component deviates from the [[stitch-design]] or [[brand-guidelines]], rather than waiting for a full file write.
- **Project Applications**: In the **Parliamentarian** app, implementing **Session Memory** extraction will allow your legislative research agents to recall constitutional interpretations across different parliament sessions without re-reading the entire 39,000-word Bill-Drafting Manual every time.

---

## Transcript

[00:00] Claude Code was accidentally leaked. It's right here by Twitter user Fried Rice. Here is a zip file to the entire source code of Claude Code. Now we all get to look into one of the best Aentic coding harnesses on the planet. And boy did we learn a lot from it. Claude Code source code has been leaked via a map file in their npm registry. So you can go and download Cloud Code right now. 

[00:27] Now, Anthropic is probably going to be quite aggressive with their DMCA takedowns, but here's the funny thing. Somebody already converted all of the Claude Code codebase over to Python, which makes it completely legal to have. Just it having been rewritten makes it copyright uninforceable. And already people are running Claude Code locally. 

[00:45] Here is why this is such a big deal. First of all, as of less than 24 hours, the source code leak has 22 million views on X alone. And the reason why this is so special is because Claude Code is incredible. It is an amazing harness. It makes large language models work so much better by having this harness around it. 

[01:15] And there are so many little secrets that people learned to make their own harnesses better because now the source code is open- source. And even Elon Musk had to get in on the fun. Anthropic is now officially more open than open AI because yes, cloud code is now basically open- source or at least the current version is because now everybody has a source code and is examining it like crazy. 

[01:28] Here's Twitter user Alfred Versa who put together a really good explanation of what this actually means for Anthropic, for the open source community, for tinkerers like myself and probably yourself. So let me show you what he said. So, the first thing to know is there are 2300 original files from the tools code and they're all public. It's almost a half million lines of code. 

[02:09] But does that mean we have all the secrets that make Claude Code special? Kind of. The thing that makes Claude Code so special is the combination of the Claude Code harness itself and its pairing with the Claude family of models. If you were to try to plug in an open- source model to it or an OpenAI model or a Gemini model into Cloud Code, it probably wouldn't work nearly as well. Cloud code is built for cloud. 

[02:33] But we do get a lot of insights into what makes the Claude Code harness work really well. And of course, very quickly, we're going to see that dissipate out to all of the open-source harnesses out there like Open Code. And next, can it be run locally? Absolutely. You have the source code now. 

[02:48] Go download the Python version because that's the one you can actually download and run legally. Then you can plug in Claude or any other model that you want. Of course, Claude's going to work better, but you can totally do this and run it completely locally if you wanted to. 

[02:59] And I think the really important part is where he says, "What does this mean for competitors? You get to study the exact prompts and agent setup to build better or cheaper coding agents." This is especially true, as I said, for the Claude family of models. You now know how to build a harness that works incredibly well with Claude. 

[03:16] Then you also get to copy clever ideas like how it handles permissions or chains multiple AI sub agents. You can launch open source alternatives or if you already have them, you can integrate some of these findings, some of these insights directly into your open source project. 

[03:31] And it also allows you to spot any weaknesses in Anthropics Claude Code product. So if you are a nefarious actor, you can look at how to attack it. But that's the beauty of open source. When everybody has their eyes on it, it becomes a much more hardened system because people can actually point out where these things are lacking in security and fix them before it gets to this point. 

[04:05] All right. So what does it mean for anthropic? Well, not really that much. There weren't any major company insider secrets revealed other than what makes Claude Codes harness work so well. There wasn't any customer data revealed. There weren't any API keys revealed. 

[04:22] So on the spectrum of leaks, it's not that bad for them. It does make them look a little sloppy, though. And by the way, whether you use the leaked version locally or you're using Claude Code directly, Zapier makes a great pairing with it. Let me tell you about them. 

[05:29] Back to the video. All right, and next, Twitter user Mal Shake put together an excellent breakdown of what I care about most. What actually makes Claude Code special? What are the secrets they figured out that they built into their harness that make it really good, especially working with the Claude family of models? Let's read through this. 

[05:39] So, number one, Claude.MD is loaded into every single turn. Every single one. So, what does that mean? Cloud.md is your way of telling Claude how to work better. Where are the files it should really pay attention to? What are the coding standards that it should follow that you and your team implement? 

[06:09] What is the architecture of your codebase that you're trying to follow? What are the other best practices? All of this goes into CloudMD. And to be honest, I barely ever touch it. And now I'm realizing I really should. You get 40,000 characters to tell claude.md, which tells claude code exactly how you want to work. 

[06:42] And so I know for sure I'm going to be updating that file today. So put your best practices, put your patterns, put your team's taste into that file and cloud will follow it because it gets loaded into every single prompt. 

[07:13] Number two, cloud code is built for parallelism. It is built for having multiple agents running simultaneously and especially because sub aents share prompt caches. So even though you might spin up five or 10 sub aents at the same time, they are all sharing the same prompt cache which means you're basically getting parallelism for free. 

[07:42] So not only with sub aents but running multiple agents at the same time. This is the right way to do things. Boris Churnney, the inventor of Claude Code, basically said the same thing. He says he has a bunch of agents always running at the same time. By the way, get work trees is the way to do that without having these agents conflict with each other in your working branch. 

[08:13] So, more specifically, the source code literally has three execution models for sub agents. Fork inherents parent context cache optimized teammate separate pane in T-Mox or iTerm communicates via file-based mailbox and a work tree gets its own git workree isolated branch per agent. So doing everything with a single agent is the wrong way to do things. It is not optimized to say the least. 

[08:53] All right. You know how every two seconds cloud code asks you, do I have your permission to do this? you want to always allow me to do this. It gets very frustrating and it turns out there's a reason for that. So, what MAL says and what the Claude Code codebase says is it is meant to be configured for permissions. 

[09:02] Every single time you get asked whether or not you want to allow something that is a failure of that configuration. You basically should never see that because you should have everything preconfigured. Yes, I want this set of tasks, this set of commands allowed, and no, I don't want these other ones. So, be sure to set that up. 

[09:18] And there is a settings.json to allow just that. And in fact, because everybody would just click allow all the time, Enthropic rolled out a smarter permissioning system. They actually tried to predict which ones you'll say yes to, and it basically just says yes automatically, and then it says no to the ones it thinks you wouldn't want to do or are too dangerous. 

[09:42] So, dangerously skip permissions, which is the little flag that people used to have on all the time, is more or less deprecated at this point. So, there are three permission modes. Bypass, no permission checks at all, dangerous but fast, allow edits, auto allows file edits in your working directory, and auto, this is the one that I was just talking about. 

[10:11] To enable this, you do so when you're invoking Claude for the first time, runs an LLM classifier on each action. This is the sweet spot. Yes. So, auto is the way to go. That is what I use. 

[10:31] All right. Next is compaction. This is probably one of the most important things that other harnesses are going to learn. There's kind of a famous saying in the world of AI where the thing that is actually more important than what the model remembers is what it forgets. Knowing what to forget lets you remember the things that are important to remember much more accurately. 

[10:50] So they found that there are five ways that compaction happens in the cloud codebase. Number one, micro compact. This is a timebased clearing of old tool results. Next, context collapse summarizes spans of conversation. This is where you can start to lose some of that fidelity. 

[11:10] Anytime you're doing compression, it's going to be lossy. So, just be mindful of that. Next is session memory, which extracts key context to a file. We have a full compact which summarizes the entire history and a ptl truncation which I hadn't heard of which just drops the oldest message groups. 

[11:33] All right, so what do you actually do with this information? First, you want to use slash compact proactively. Don't wait for the system to autocompact and lose context you care about. If you already know what you want to remember and especially what you want to forget, slash compact, that's the way to go. 

[11:43] The default window is 200,000 tokens. You can opt into a million tokens. The million tokens work quite well. The quality past 200,000 tokens starts to drop, but it is still better than the competitors out there. Long sessions accumulate session memory, structured summaries of task specs, file list, workflow state, errors, and learnings. 

[12:15] This is why resuming a session is better than starting fresh. Yes, I do always try to continue in the same session, even if I'm usually changing what I'm coding or working on a new part of the codebase. If there's any tie to what I had previously worked on, I try to use the same session. 

[12:35] Large tool results get stored to disk with only an 8 kilobyte preview sent to the model. If you paste a massive file, the model may see only a fraction. Keep input focused. So, think of /compact like saving your game in a video game. That is what he recommends here. 

[12:56] Next is hooks. This is apparently the power user feature that I am not using at all. So, I was excited to learn more about this. Here are the different hooks that are available that you can plug into. Pre-tool use, post tool use, user prompt submit, session start, session end, and a bunch more. 

[13:18] They also have five types of hooks. So, have a command, prompt, agent, HTTP, and a function. Now, one of the things that I heard Anthropic does is automatically update their documentation. So, the codes documentation when new code is submitted. 

[13:41] What I do is I tell it make sure the documentation is updated and I have to do this all the time and it's super frustrating and I realized I can just automate it. I can just say okay when I make a new commit go ahead and just make sure my documentation is updated depending on what part of the codebase I just touched. 

[13:54] Next sessions are persistent and resumable parenthesis stop starting fresh. So every conversation is saved as JSON L at cloud projects. There's the hash, there's the session ID and JSONL file format. So you can do d- continue to resume your last session. 

[14:13] You can do d-res session. You can fork sessions basically stop starting fresh. The fresh session means no context. It's going to have to learn from scratch again. Obviously, it's a little bit more than just learning from scratch, but if you want that continuity, if you want that momentum of your existing session, this is the way to do it. 

[14:36] Claude Code has 60 6 builtin tools that it uses. Some of the obvious ones are probably ones you know of, browse the web, save files, execute code, etc. And they are partitioned into two types of tools. 

[14:46] Concurrent tools which are readonly operations and serialized tools mutating operations like edits, writes, bash commands run one at a time. So if cla delegating out to 10 different sub aents need to read 10 different parts of your codebase, it can do that in parallel with no problem. 

[14:46] The next tip is that streaming architecture means interruption is cheap. What does that actually mean? If you're coding and you notice that cloud code is going in the wrong direction, maybe it's coding something incorrectly or misunderstood your prompt, stop it immediately. There's nothing wrong with that. You're not going to lose tokens. 

[14:46] You're actually kind of dealing with the sunk cost fallacy at that point. Just cut it off, cut your losses, and try to continue from where you were, which is very possible. All right, so as you could tell, Claude Code, it's very special. But now everybody gets to see its secrets. And there's one more thing I wanted to share. 

[14:46] Remember yesterday's video meta harness where it's basically a harness that can self-improve the harness within it. Now we can actually plug cloud code into metah harness and allow it to recursively selfimprove. Imagine that. That's the beauty of open source. That is why I was kind of excited to see this leak. 

[14:46] I know anthropic doesn't want it. I know Anthropic is the most closed source of all the closed source frontier labs out there, but I was pretty happy to see it. And this is why. This is the beauty of open source. When things are open, other people can build off of those ideas and it just makes for so much more innovation. 
