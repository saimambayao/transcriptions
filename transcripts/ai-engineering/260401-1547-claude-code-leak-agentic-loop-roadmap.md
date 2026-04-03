# Claude Code was just leaked... (INSANE)

**Channel**: Ras Mic
**Duration**: 17:36
**Language**: English (manual) [yt-dlp subtitles]
**URL**: https://youtube.com/watch?v=2nxlwYyGUeg
**Transcribed**: 2026-04-01 15:47

---

## Organized Notes

**The Claude Code Leak: Context and Mechanics**

- **The Leak Incident**: At 4:23 AM, the Claude Code source code was leaked via a map file in the **npm registry**. The codebase, estimated at over **500,000 lines**, provides a complete blueprint for one of the world's most advanced agentic coding harnesses. [00:00], [00:46]
- **The Agentic Loop**: The system follows a structured execution cycle:
  1. **Message Input**: User message is appended to history.
  2. **Context Assembly**: System prompt is built with current date, **Git status**, branch, recent commits, and `claude.md` memory files.
  3. **Reasoning & Tool Selection**: Model emits tool use blocks (name + structured JSON).
  4. **Permission Check**: Evaluates permissions mode (auto-approve, prompt, or block).
  5. **Tool Execution**: Approved calls run; results (files, bash output) are appended to history.
  6. **Loop/Conclusion**: Continues until no tool calls remain. [01:04], [02:46]

*Quotable Quotes:*

> "Claude Code is not a chatbot... it's a full agent runtime built with Bun, TypeScript, and React." [01:56]

> "The thing that is actually more important than what the model remembers is what it forgets. Knowing what to forget lets you remember the things that are important much more accurately." [09:34] (Wait, this was Berman - re-checking Ras Mic quotes)

*Quotable Quotes (Ras Mic):*
> "In a nutshell, this is what an agent is: a continuous loop of reasoning, tool selection, and execution until the task is complete." [02:46]

> "Sub-agents free up the main thread... allowing you to continue chatting with the main agent while the sub-agent handles the beefy tasks." [08:11]

**Core Systems: Permissions and Context**

- **Context Preservation**: Two context blocks (System and User) are **memoized** using `lodash.memoize`. System context includes a "cache-breaking injection" (ephemeral string) to bust server-side prompt caching during debugging. [03:08], [04:15]
- **Permission Modes**: 
  - **Bypass Permissions**: (`dangerously skip permissions`) skips all checks.
  - **Accept Edits**: Auto-approves file edits but prompts for bash commands.
  - **Default**: Prompts for all non-read-only actions. Read-only tools (`read`, `glob`, `grep`) are auto-approved across all modes. [06:38], [06:51]

**Multi-Agent and Extension Architecture**

- **Sub-Agent Lifecycle**: Spawned via the `agent tool` for parallel independent tasks (e.g., writing tests while updating docs) or isolated exploration (forking to prevent context pollution). The main agent only receives the final **result**, not the intermediate steps. [07:09], [09:34], [11:29]
- **Foreground vs. Background**: 
  - **Foreground agents**: Main thread waits for completion.
  - **Background agents**: Asynchronous; Claude continues working and receives a notification when done. [13:01], [13:18]
- **Event-Driven Hooks**: The `slash hooks` command allows binding scripts, endpoints, or LLM prompts to specific events like `before/after tool execution`, `tool error`, or `before response conclusion`. [10:05], [10:37]

**Future Roadmap: Leaked Experimental Features**

- **Agent Teams**: Orchestrating multiple persistent Claude Code sessions (experimental flag: `cla_agent_teams`). [13:54]
- **Remote Development**: **SSH remote development** mode and persistent session servers with O-Auth tokens and idle timeouts. [14:46]
- **Agent Self-Maintenance**:
  - **AutoDream**: Background memory consolidation ("Dreaming") that distills session transcripts into memory files when idle.
  - **Karios**: A background agent designed for long-term task finding and independent action.
  - **Proactive Mode**: Includes a `sleep` tool for agents that wake themselves up to check for tasks. [15:26], [16:31], [17:02]
- **UI and Interaction**:
  - **Buddy**: An animated "Clippy-style" pet (species: Buddy) that provides feedback and commentary (partially an April Fool's prank but referenced in source).
  - **Away Summary**: Auto-generates a 1-3 sentence "while you were away" recap if the terminal is blurred for 5+ minutes.
  - **Ultra Plan**: Defaulting to **Opus 4.6** (or 4.7) for long-running, plan-heavy tasks. [14:46], [16:31]

---

## What This Means for Your Work

The deep technical breakdown of the **Agentic Loop** and **Memoized Context** provided in this video is vital for optimizing your **Parliamentarian** and **e-Bangsamoro** development. As a solo dev, understanding that the system prompt is assembled once and memoized means you can be more intentional about what you put in **GEMINI.md** — since those instructions are prepended to *every* API call, they are your high-frequency steering wheel. For your work with **OOBC**, the **Background Agent** pattern is a game-changer: you can launch a background research task for OBC social justice policies while simultaneously drafting a new BAA in the foreground.

The **AutoDream** (background memory consolidation) and **Away Summary** features suggest a future where your **Obsidian vault** doesn't just store what you've done, but active "dreams" (distillations) of your previous sessions. This reinforces the value of your **session-summary** skill. For **MoroMarket**, the **Advisor** pattern (a second model oversees the first) could be implemented as a mandatory QA gate for financial data processing, mirroring Anthropic's own internal quality controls.

### How This Can Improve Your Gemini Skills and Workflows

This video identifies several elite-level optimizations for your 135+ skills:

- **Skill Enhancements**: 
  - [[gitops]]: Incorporate the **System Context** pattern by building a "Repo State" provider that feeds current branch, username, and last 5 commits directly into your agentic drafts, ensuring high situational awareness.
  - [[obsidian]]: Align your vault sync with the **Session Memory** extraction logic. Use a "Distillation" sub-agent (inspired by **AutoDream**) to periodically clean up and consolidate your `transcripts/` into high-signal knowledge notes.
  - [[fact-checker]]: Implement the **Advisor** pattern from the leak — dispatch a specialized `reviewer` agent to monitor the live output of a `writer` agent, providing real-time corrections.
- **Workflow Optimization**:
  - **Interruption/Cheapness**: Embrace the streaming architecture. If you see the agent hallucinating a BAA number or a BOL article, stop it immediately. 
  - **Foreground/Background Split**: Stop doing long-running tasks in the foreground. Use the **Background Agent** pattern for data-heavy scraping or massive codebase audits.
- **Project Applications**: 
  - In **Tarbiyyah-MS**, use the **Isolated Exploration** (forking) pattern to test different database migration strategies without cluttering the main conversation context.
  - For the **Bangsamoro ECCD Bill** drafting, use the **Task Tool** to split the 51 sections among parallel sub-agents for a 4x speedup in initial drafting.

---

## Transcript

[00:00] Claude Code is open source. I'm just joking. But today, early in the morning, 4:23 a.m. to be exact, this exac account tweeted, "Claude Code source code has been leaked via map file in their MPM registry and linked a zip file in the tweet." 

[00:07] Now, a lot of people have downloaded the code and reviewed the code. I'm not going to be showing code on this screen. That is completely wrong. Enthropic, if you're watching this, PR, legal, whoever is watching this, I will not show a single line of code. 

[00:21] But what we're going to talk about is how one of the best coding agents, Cloud Code, works under the hood. What are some of the new features that are on the way without revealing a single line of code, please, Enthropic, don't take down this video, ladies and gents. Let's get into it. It's going to be a deep one. 

[01:04] User sends message. You type a message in the terminal interactive mode or pass via-print. The message is appended to the conversation history. Context is assembled. Before calling the model, cloud code assembles a system prompt that includes the current date. Interesting. get status, branch, recent commits and working tree status and any loaded claw MD memory files and all the list of available tools. 

[01:35] This context is built once per conversation and memorized. So before the conversation starts when a user sends a message before it hits the model before the API call is made what happens here is claude code is going to assemble the context. 

[01:52] Claude reasons and selects tools. The assembled conversation is sent to a thropic API. The model reasons about the task, emits one or more tool use blocks, each specifying a tool name and a structure JSON output. 

[02:06] Permission check. Before executing each tool call, Claude Code evaluates the current permissions mode and any allow deny rules. Depending on the mode, it either auto approves, prompts you for confirmation, or blocks the call entirely. 

[02:21] So you ever use cloud code and if you have dangerously skip permissions, it's just going to fly through. But if you don't have that set, it's going to ask you, do you allow me to do this set task to write to this file to access this endpoint? That's what the permissions checks do. 

[02:34] Tool executes and returns a result. Approved tool calls run. Results, file contents, command outputs, search hits are appended to the conversation as tool result blocks. And then what happens? 

[02:46] This loop continues. The model receives the tool results and either calls more tools or produces a final text response. The loop repeats until no tool calls remain in a model run. So once it's produced the final text response, once there is no need to call tools anymore, that's when the loop ends. 

[03:08] It says here at the start of each conversation, cloud code builds two context blocks that are prepended to every API call. We have system context and user context. Assembled by get system context. This is a function in context.ts contains get status, right? The current branch default/main branch get username get status. 

[03:25] So all the git information truncated to 2,00 characters if larger and the last five commits from get log- line. If you had like you know 10 20 commits when it does get log- one line it's going to get the last five ones. cache breaking injection, an optional effirmal string used internally to bust the server side prompt caching during debugging. 

[04:15] For user context it's assembled in this function in this file. We're obviously going to have the claude.md file in memory. But what's interesting is the current date also gets injected so that the model knows the date. Final thing to note is the system context and the user context are both prepended to every API call and both context blocks are memoized during the duration of the conversation. 

[06:03] So, Cloud Code does not execute tool calls anonymously by default. Each tool has a check permissions method and the result determines what happens next. If it's allowed, the tool runs immediately. Of course, if it's asked, Cloud Code pauses and renders a confirmation dialogue. 

[06:38] In bypass permissions mode, all checks are passed. In accept edits mode, file edit tools are auto approved, but bash commands still prompt. Tool calls that are safe and read only read glob and gp are genuinely auto approved across all modes. This makes sense cuz it's just read only. 

[07:09] Claude can spawn sub aents via task tool which is called the tool name is actually agent tool. Each sub aent runs its own nested agentic loop with isolated conversation and optionally a restricted tool set. Sub aents can run locally in process or on remote compute. 

[07:40] What's interesting though, it's the results that are returned to the parent agent. I don't believe that the steps it took to get to the result is fed into the parent agent. The parent agent only receives results. 

[08:11] But what you can tell openclaw to do is hey I want you to do this task use a sub agent and when it tells the sub agent to do that I can now chat with the main agent freeing up the thread in the same way you can think of sub aents like this as well in the case of cloud code. 

[10:05] A hook is a command shell script HTTP endpoint or LLM prompt bound to a specific event. When the event fires, Cloud Code runs every matching hook and uses the exit code and output to decide what to do next. And you have all these hook events, right? Before tool execution, after tool execution, after a tool error, before Claude concludes a response, before a sub agent concludes a response. 

[11:29] Claude spawns agents when a task benefits from parallelism or specialization. For example, independent parallel tasks, writing tests while also updating documentation, specialized work, using a code review agent for security audit, longunning task, background research while Claude works on something else, isolated exploration, forking itself to explore a solution without polluting the main context. 

[13:01] By default, agents run in foreground. Claude waits for each agent to complete before proceeding. Use foreground agents when Claude needs the result before it continues work. Background agents run asynchronously. 

[13:18] Claude launches them and continues with other work. You receive a notification when the agent completes. An example prompt is run the integration tests in the background while you implement the next feature. 

[13:30] Claude will not pull or check on background agents. it continues working and receives the result as a notification when the agent finishes. Now the moment you've all been waiting for. What are some of the unreleased not yet public features in cloud code? 

[14:16] Second feature is voice mode. SSH remote development. Direct connect/ session server. When you do d-t teleport, it resumes a teleport session. D- remote creates a remote session. D- remote control starts an interactive session with remote control enabled. 

[14:46] MCP channels. The buddy feature is probably my favorite one. A small animated creature with a species and a name sits behind the user's input box and occasionally comments in a speech bubble. Away summary. After the terminal has been blurred for 5 minutes, autogenerates a 1 to three sentence while you were away recap. 

[16:31] There's this autodream feature and basically what it does is background memory consolidation that runs a forked sub agent/dream when enough time has passed and enough sessions have accumulated. Coordinator mode multi- aent orchestration where one claude coordinates tools coordinates tool use across agents. We have proactive mode, autonomous agent behavior with sleep tool, clawed proactively works without user input. 
