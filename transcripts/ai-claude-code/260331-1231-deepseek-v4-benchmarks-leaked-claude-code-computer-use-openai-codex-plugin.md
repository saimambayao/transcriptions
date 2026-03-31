# DeepSeek V4 Benchmarks LEAKED + Claude Code Computer Use + OpenAI's Codex Plugin!

**Channel**: Universe of AI
**Duration**: 10:08
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=nAZdk1d_QzU
**Transcribed**: 2026-03-31 12:31

---

## Organized Notes

**DeepSeek V4 Benchmark Leaks**

- Unverified benchmark leaks from **Atov International** on Twitter claim DeepSeek V4 beats **Claude Opus** and **GPT 5.3**
- Leaked specs: ~**200B parameter** light version, **1M token context window**, multimodal (text, images, video)
- Scales to **1 trillion parameters** via **MHC architecture**
- Benchmark claims: **HumanEval ~90%**, **SWE-Bench >80%**, coding performance above V3.2 and all current competitors
- Sources claim these are **conservative** figures — "holding back the real numbers"
- Timeline has slipped repeatedly: Lunar New Year → March 2 → April → now "coming soon" with **NDAs at select providers**
- **Caveat**: single unverified source; DeepSeek has not confirmed any of this

**DeepSeek Quiet Model Swap**

- After a **7-hour outage**, DeepSeek appears to have **quietly swapped their model** with no announcement
- Before outage: model identified itself as **V3**; after outage: reverted to calling itself "the latest version"
- **SVG generation quality regressed** noticeably — comparison screenshots show worse output post-outage
- Pattern consistent with **previous silent model swaps** by DeepSeek
- No official confirmation from DeepSeek on what happened

**Claude Code Computer Use (Research Preview)**

- Anthropic launched **computer use inside Claude Code** — the announcement hit **2.3M views** quickly
- Claude can now **open apps, control the screen, and interact with the machine** from the CLI
- Example workflow: compile a Swift app → launch it → click through every button → screenshot results → loop back to fix bugs — all in one conversation
- **Priority order for tool selection**:
  1. **MCP server** (most precise)
  2. **Bash** (shell commands)
  3. **Claude in Chrome** (browser tasks)
  4. **Computer use** (last resort — screen control for native apps, simulators, tools without APIs)
- Available as a **built-in MCP server** called "computer use" — disabled by default, enable per project
- Requires two **macOS permissions**: Accessibility (click, type, scroll) and Screen Recording (see screen)
- **Availability**: Mac OS only, **Pro or Max plan**, Claude version 2.185+, interactive sessions only — not on Team or Enterprise yet
- **Safety guardrails**:
  - Per-approval app control (only apps approved in current session)
  - **Sentinel warnings** for apps with shell/file system/settings access
  - **Terminal excluded from screenshots** — Claude cannot read terminal content, closing prompt injection vectors
  - **Escape key** aborts computer use globally
  - **Lock file** — only one session controls the machine at a time

**Claude Code Auto Mode**

- Launched **March 24th**, rolling out to **Enterprise and API users**
- Solves the problem of Claude Code asking for approval on **every file write and bash command** — you couldn't kick off a large task and walk away
- Previous workaround was `dangerously skip permissions` — exactly as risky as it sounds
- Auto mode is a **middle path**: a classifier reviews each tool call before execution
  - **Safe actions** proceed automatically
  - **Risky actions** get blocked for approval
- Developers approve **~93% of permission prompts** anyway — auto mode automates the routine approvals
- Enable via `claude/ enable auto mode` or **Shift+Tab** to cycle to it
- Requires **Sonnet 4.6 or Opus 4.6**, available on Team plan now

**Microsoft Multimodal Deep Research**

- Microsoft added **multimodal intelligence** to their deep research agent in **Microsoft 365 Copilot**
- Architecture: **one model generates** the research, a **second model from a different lab reviews** it before final output — called **"Critique"**
- Generator and reviewer come from **Frontier Labs** including Anthropic and OpenAI
- Also launching **"Council"**: runs an **Anthropic model and OpenAI model side by side** on the same query, then a **third model synthesizes** where they agree and disagree
- Rolling out to **Enterprise Copilot users** through their Frontier program

**OpenAI Codex Plugin for Claude Code**

- OpenAI released a **Codex plugin that installs directly inside Claude Code**
- Three modes:
  1. **Standard review** — inspect your implementation
  2. **Adversarial review** — specifically challenges your implementation
  3. **Handoff mode** — pass a task to Codex entirely
- Notable: the **two biggest agentic coding tools** now have an official integration — built by OpenAI

## What This Means for Your Work

**Computer use is the missing piece for your visual verification loop.** Your CLAUDE.md already mandates screenshot-verify-fix cycles for PDFs using `pdftoppm`, but that's limited to static images. Computer use could let Claude directly open generated PDFs in Preview, interact with them (scroll, zoom, check page breaks), and verify layouts more naturally than CLI screenshot tools. For your guidebook production pipeline — where you're generating 12+ BARMM guidebooks with complex CSS layouts, tables, and diagrams — this could significantly reduce the verify-fix loop iterations. However, it's Mac-only/Pro plan and research preview, so it's worth tracking but not depending on yet.

**Auto mode changes your solo dev workflow economics.** You build government-scale platforms alone across 9+ repos. Currently, you maximize parallel agents but each one still needs approval clicks. Auto mode with the 93% auto-approval rate means you could dispatch a `/devwork` feature implementation, a `/build` verification, and a `/test` suite run — then genuinely walk away while they execute. For your frontend-first development approach on e-Bangsamoro, this means faster iteration cycles on the 4-portal system. The Shift+Tab toggle makes it easy to flip between supervised mode (legal content, policy documents) and autonomous mode (UI components, test suites).

**Microsoft's multi-model "Critique" and "Council" architecture validates your existing pattern.** You already do something similar with your `/research-pipeline` (NotebookLM generates analysis → Claude validates) and `/fact-checker` (runs after every content skill). Microsoft formalizing this as generator+reviewer from different labs confirms that cross-model validation is becoming standard practice, not just your personal workflow discipline.

**The Codex-inside-Claude-Code plugin creates an adversarial review option you don't currently have.** Your `/legal-reviewer` does 6-dimension QA and your fact-checker catches fabricated BAA numbers, but those are same-model reviews. An adversarial review from a different model (OpenAI's Codex) could catch blind spots that Claude systematically misses — particularly useful for your bill drafting and policy recommendation workflows where accuracy is non-negotiable.

**DeepSeek V4's claimed specs (1T params, 1M context, multimodal) would matter for your legal research pipeline.** If DeepSeek V4 ships with those coding benchmarks and multimodal capability, it could become a viable alternative for the heavy analysis work you currently offload to NotebookLM. But leaked benchmarks are unreliable — file this under "track, don't act."

### How This Can Improve Your Claude Skills and Workflows

**Computer use + `/webapp-testing`**: Your existing `/webapp-testing` skill uses Playwright for browser automation. Computer use could complement this for testing native app behaviors that Playwright can't reach — particularly useful if you ever build mobile wrappers for e-Bangsamoro or MoroMarket. No new skill needed yet, but worth adding a "computer use fallback" note to `/webapp-testing` references when the feature stabilizes.

**Auto mode + `/devwork` and `/build`**: Your `/devwork` skill's frontend-first workflow and `/build` verification could be updated to detect when auto mode is available and suggest enabling it for the implementation phase. This would make the "implement → verify → fix" loop genuinely autonomous for UI work on e-Bangsamoro's React 19 components.

**Adversarial review as a new skill**: You don't currently have a cross-model adversarial review skill. The Codex plugin's adversarial mode suggests a new skill opportunity — something like `/adversarial-review` that specifically routes code or documents to a different model for challenge-based review. Check if this exists: your `/legal-reviewer` and `/fact-checker` are same-model. A cross-model review would add a genuinely different perspective. This would be particularly valuable for the `/bill-drafter` and `/resolution-drafter` pipelines where legislative accuracy is critical.

**Microsoft Council pattern → `/research-pipeline` enhancement**: Your `/research-pipeline` already uses NotebookLM + Claude validation. Microsoft's "Council" (two models + synthesizer) suggests extending this to run parallel analyses from different models and synthesize disagreements. This could improve confidence scoring in `/deep-research` outputs, especially for contested policy topics in Bangsamoro governance.

**DeepSeek model instability → `/fact-checker` awareness**: The silent model swap story is a reminder that any pipeline depending on external model APIs (including your NotebookLM integration) can break without warning. Your `/fact-checker` should already catch downstream quality drops, but consider adding a "model fingerprint" check to your `/research-pipeline` that flags when NotebookLM or other external tools produce notably different quality outputs.

---

## Transcript

[00:00] Anthropic just dropped computer use inside Claude Code. There are Deepseek version 4 benchmarks leaks circulating that are claiming to beat Claude Opus and GPT 5.3 and DeepSeek may have quietly swapped their model after a 7-hour outage. Anthropic also launched auto

[00:15] mode for Claude Code. Microsoft is doing something interesting with multimodal deep research and OpenAI released a Codex plugin that works directly inside Claude Code. So, let's get into it.

[00:27] We have two Deepseek stories today and they're pretty different in nature. The first one, there are benchmark leaks circulating claiming Deepseek version 4 is beating Claude Opus and GPT 5.3. This

[00:38] is coming from a Twitter account called Atov International and they're upfront that it's unconfirmed and unverified, but say the sources describe numbers as conservative. But supposedly leaking is a roughly 200 billion parameter light version with a 1 million token context window with multimodal text images video. It apparently scales to 1 trillion parameters via something called MHC architecture. The benchmark numbers

[01:04] being cited are human eval around 90% software bench above 80% and coding performance claim to be above version 3.2 and every current competitor. The people sharing these numbers are also saying they're holding back the real figures. On the timeline, it was

[01:20] originally supposed to ship around Lunar New Year, then the week of March 2nd, then April. Now, it's coming soon with NDAs at select providers and no official date. Multiple postponements, which is pretty standard pre-release behavior for a model of this scale, which is worth noting. Now, to be clear, this is a

[01:37] single unverified source, and Deepseek has not confirmed any of this. Leaked benchmarks before a release don't always reflect what actually ships. With the scale being described, one trillion parameters multimodal, the context window is consistent with what you expect from a serious version 4 release, and the delays are at least real, so it's worth tracking. Big thanks to

[01:58] Hostinger for sponsoring this video. So, if you've been wanting to run your own AI agent, something that works for you 24/7, handles tasks, answers messages, all of that, Hostinger just made it really easy to do that with OpenClaw. OpenClaw is an AI agent platform, and normally setting something like this up is a headache. You're dealing with API

[02:18] keys, server configurations, all kind of stuff. With Hostinger, it's literally one click. You pick your plant, they handle the whole setup automatically, and your agent is live in minutes. No

[02:29] terminal, no technical background needed. Once it's running, you can connect it to WhatsApp, Telegram, Slack, Discord, wherever you already work, and it starts handling things for you. We're talking qualifying leads, drafting follow-ups, sorting messages, doing research, even managing your own calendar. It runs around the clock, so

[02:48] it's working even when you're not. What I also like is that your data stays private. Every instant runs in its own isolated environment, so your conversations and files aren't mixed in with anyone else's. Hostinger plan also

[03:00] offers you AI credits that come pre-installed, so you don't have to go set up some separate accounts with OpenAI or Anthropic. It's all in one place through the Hostinger dashboard. The manage plan is already 73% off at only $8.39 a month. And with my code,

[03:16] Universe of AI at checkout, you get an extra 10% on top of that. Link is in the description. There's also a 30-day money back guarantee, so it's pretty risk-f free to try as well. Now, let's get back

[03:27] into the video. The second Deep Seek story is separate and more concrete. According to a post from AI Battle, Deepseek likely swapped their model after a 7-hour outage that happened recently. Before the outage, the model

[03:40] was identifying itself as version 3. After the outage, it stopped doing that and went back to calling itself the latest version. The SVG generation quality also appears to have regressed.

[03:51] The comparison screenshots show notably worse output after the outage compared to before. This is a pattern we've seen before with DeepSeek. Quiet model swaps with no official announcement. There's

[04:02] no confirmation from Deepseek on what happened or what's currently running, but if you notice a quality drop in the last day or two, that may be why. Anthropic dropped computer use for Claude Code and the tweet announcing it already hit 2.3 million views pretty fast. Let's

[04:17] break down what it actually does. Computer use lets Claude open apps, control your screen, and work on your machine the way you would from the CLI. Claude can now compile a Swift app, launch it, click through every button, and screenshot the result all in the same conversation where it wrote the code. The key thing to understand is the

[04:35] priority order. Claude has several ways to interact with the app or a service, and computer use is the broadest and slowest. So, Claude tries the most precise tool first. If you have an MCP

[04:45] server for the service, Claude uses that. If the task is a shell command, Claude uses bash. If the task is a browser work and you have Claude in Chrome setup, Claude uses that. If none

[04:56] of those apply, Claude uses computer use. Screen control is reserved for things nothing else can reach. Native apps, simulators, and tools without an API.

[05:05] So, this isn't a hammer for everything. Is genuinely a last resort after the most precise tools have been ruled out, which is a reasonable design decision. Computer use is available as a built-in MCP server called computer use. It's off

[05:18] by default until you enable it. You can find computer use in the server list and it shows as disabled. Select it and choose enable. The setting persists per

[05:27] project, so you only do this once for each project where you want computer use to work. The first time Claude tries to use computer, you'll see a prompt to grant two Mac OS permissions. Accessibility, which lets Claude click, type, and scroll, and screen recording, which lets Claude see what's on your screen. On availability, computer use is

[05:46] in research preview on Mac OS that requires a pro or max plan, and it's not available on team or enterprises plans yet. It requires Claude Code version 2.185 or later, and an interactive session.

[05:58] The safety model is also worth understanding clearly. Unlike the sandbox bash tool, computer use runs on your actual desktop with access to the apps you approve. Claude checks each action and flags potential prompt injection from onscreen content, but the trust boundary is different. The

[06:15] built-in guardrails they've added per approval. Claude can only control apps you approved in the current session. Sentinel warnings. Apps that grant shell

[06:23] file system or system settings access are flagged before you approve. and terminal excluded from screenshots which means Claude never sees your terminal window so onscreen prompts in your sessions can't feed back into the model. There's also global escape the escape key aborts computer use from anywhere and you can lock file only one session can control your machine at a time. The

[06:44] terminal exclusion from screenshots is a smart detail. It means Claude literally cannot read what's in your terminal window which closes a whole category of injection rigs. The practical use case that makes the most sense right now is exactly what they're showing in the demo. You build something in Claude Code,

[07:00] you want Claude to open it, test it, visually confirm it's working, find the bug, and loop back. The end-to-end workflow without leaving the terminal is genuinely useful. The broader do everything on my computer is still further out, but the foundation is there. And obviously, this is still in

[07:15] research preview, so track where this update keeps going. Anthropic also launched auto mode for Claude Code on March 24th and it's now rolling out to enterprise and API users. The problem it solves: Claude Code's default permission

[07:29] is to ask for approval on every file write and batch command. It's a safe default, but it means you can't kick off a large task and walk away. The workaround people were using was dangerously skip permissions, which is exactly as risky as it sounds. But auto mode is a middle

[07:45] path. Longer task with fewer interruptions, but less risk than skipping permissions entirely. Before each tool call, a classifier reviews it.

[07:54] Safe actions proceed automatically. Risky ones get blocked. Developers approve roughly 93% of permission prompts anyway. So, auto mode is

[08:02] essentially automating the routine approvals while catching the genuinely dangerous stuff. To enable it, all you have to do is do claude/ enable auto mode from the CLI, shift plus tab to cycle to it. and it requires Sonnet 4.6

[08:16] or Opus 4.6 and it's on the team plan now with enterprise and API rolling out for long refactors or test loops on a dev branch. This is a solid improvement.

[08:26] Before we continue, we just launched the universe of AI newsletter. If you want to stay on top of AI news without having to hunt for it, link is in the description. Don't miss out. Microsoft

[08:37] also dropped multimodal intelligence in researcher today, the deep research agent inside Microsoft 365 Copilot. The short version, instead of one model doing all the work, they now have one model generating the research and a second model from a different lab reviewing it before the final reports comes out. They're calling this critique. And the generator and reviewer

[08:57] come from Frontier Labs, including Anthropic and OpenAI. They're also launching something called Council, which runs an Anthropic model and an OpenAI model side by side on the same query and then has a third model synthesized where they agree and disagree. is actually rolling out to enterprise copilot users through their Frontier program. So if you get this

[09:16] worth checking out OpenAI released a Codex plugin that installs directly inside Claude Code, so you can now pull Codex into your Claude Code workflow to get a second opinion from a different agent without ever switching tools. There's a standard review mode and an adversarial review that specifically challenges your implementation rather than just inspecting it and a handoff mode where you pass a task to codeex entirely. It's an interesting move. The

[09:42] two biggest agentic coding tools now have an official integration and it was built by OpenAI. I'll link the setup in the description if you want to try it out for yourself. But that's it for today's video. Make sure you guys are

[09:53] subscribed to the channel. Follow our new newsletter as well at universeai.behive.com. beehive.com as

[09:59] well as subscribe to the main channel World of AI and support us on X by following the universe of AIZ as well. Until then, I'll see you guys in the next
