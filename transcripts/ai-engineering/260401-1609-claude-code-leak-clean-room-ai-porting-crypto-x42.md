# Claude Code source code LEAKED

**Channel**: Wes Roth
**Duration**: 17:32
**Language**: English (manual) [yt-dlp subtitles]
**URL**: https://youtube.com/watch?v=PNjIXYAFgCI
**Transcribed**: 2026-04-01 16:09

---

## Organized Notes

**The Anthropoic Leak: A New Era of "Clean Room" Engineering**

- **The Incident**: An accidental map file inclusion (60MB) allowed the reconstruction of ~200,000 TypeScript files and 600,000 lines of code. One GitHub mirror received over **42,000 forks** almost immediately. [00:23], [01:05]
- **AI-Powered Re-coding**: Within 12 hours of the leak, developers used **OpenAI's Codex** to completely rewrite the TypeScript codebase into **Python** and **Rust**. This "clean room engineering" with AI potentially erases copyright by creating derivative works with identical functionality but entirely different source code. [03:56], [04:46], [06:13]

*Quotable Quotes:*

> "AI is quietly erasing copyright right now. We're seeing clean room engineering at a speed never before possible—rewriting 600,000 lines of code into a new language in hours." [04:46], [06:27]

> "The 1M context Mythos model is real. It's called Capibara internally, and it's being tested as a flagship model for full reasoning." [08:47], [16:56]

**Leaked Infrastructure and Financial Protocols**

- **X42 Agentic Crypto**: The leak contains multiple references to **X42**, a protocol for **agentic crypto payments**. This suggests Anthropic is building infrastructure to allow agents to handle financial transactions autonomously. [15:12], [16:43]
- **Sentiment and Frustration Monitoring**: The source reveals that Claude is actively monitoring the user's language to detect **frustration** and **loss of patience**, adjusting its responses based on the user's emotional state. [13:28], [14:49]
- **Hexadecimal Evasion**: To avoid triggering internal build scanners that flag model code names (like **Capiara**), developers used hexadecimal encoding for the names of the 18 Tamagotchi species (e.g., "duck" spelled out in hex). [16:56], [17:56]

**Advanced Agent Features: The "Swarm" Architecture**

- **Coordinator Mode (The Swarm)**: Wes Roth notes that while the community calls them "agent swarms," Anthropic uses professional terms like **Coordinator** and **Orchestrator**. The system allows one Claude agent to orchestrate worker agents, each with its own "scratchpad" and restricted toolset. [10:05], [11:11]
- **Teleport and Bug Hunter**: New internal commands including `/teleport` (for switching between sessions) and `/bughunter` (specialized diagnostic mode) were found behind experimental flags. [11:46]
- **Ultra Plan ( CCR )**: A 30-minute remote planning session powered by an "expensive deep planning model" that fleshes out a full checklist before the coding agent begins its work. [08:59], [09:39]

---

## What This Means for Your Work

The discussion on **AI-powered Clean Room Engineering** is a "superpower" for your **MoroTech** and **e-Bangsamoro** development. If you find a proprietary logic or a leaked harness pattern that you want to integrate into your own **GSD** plugins or **Antigravity** skills, your strategy should be to "translate" those patterns into a different language (e.g., Python scripts in your `scripts/` directory) using your own agentic tools. This provides a layer of legal and technical separation while maintaining the advanced functionality of the Anthropic "harness."

Additionally, the **Agentic Crypto (X42)** insight is a major directional hint for **MoroMarket**. Since you are building a platform for Bangsamoro trade and recruitment, you should begin exploring how these protocols could facilitate autonomous payments for freelance work or trade transactions within the BARMM ecosystem. The **Sentiment Monitoring** discovery also suggests you should build "Empathy Gates" into your **humanizer** skill—if your agent detects user frustration, it should automatically trigger a "Professional Recap" or a proactive apology to maintain the high-trust relationship required for government consulting.

### How This Can Improve Your Gemini Skills and Workflows

Wes Roth's breakdown provides several elite-tier optimizations for your skills-bucket:

- **Skill Enhancements**: 
  - [[mcp-server]]: Look into the **X42** and **agentic payment** patterns to see how you can build a secure "Financial Tool" for your MCP servers.
  - [[humanizer]]: Implement a "Frustration Detection" module. If the user's prompt contains markers of frustration (identified via the leaked regex lists from Video 5), the skill should automatically switch to "Professional Mode 4" with a concise summary.
  - [[auto-research]]: Adopt the **Coordinator/Swarm** terminology and architecture. Re-structure your parallel research tasks to use a central "Orchestrator" agent that delegates to "Worker" agents with hex-encoded internal names to avoid prompt-level scanning errors.
- **Workflow Changes**:
  - **Clean Room Protocol**: For any new high-value logic you develop, create a "Derivative Port" as part of your verification plan. If you write it in TypeScript, have a background task port it to Python to ensure structural independence.
- **Project Applications**: 
  - For the **BTA Parliament**, use the **Bug Hunter** pattern to create a "Legislation Auditor" that scans bills specifically for "logical bugs" or constitutional conflicts using a specialized diagnostic agent thread.
  - In **Tarbiyyah-MS**, implement a **Teleport** skill that allows you to "move" your current conversation context to a fresh session if the history becomes too cluttered, preserving only the essential "memory files."

---

## Transcript

[00:00] All right, so this is absolutely wild news. So Anthropic accidentally leaks Claude Codes source code. No, this isn't the Mythos leak from 5 days earlier. This is a whole new massive massive leak out of anthropic. And this time it's not a blog post. It's everything that makes Claude tick. 

[00:23] So an anthropic engineer accidentally leaks the source code. The internet does what the internet does. It archives it within hours. It clones it, forks it all over GitHub within hours. We're talking about tens of thousands of copies. 

[00:46] source map can be sort of opened up, converted, transcribed into the entire source code. It's this minified obuscated version of the source code but but you can convert it into readable source code. So it's something like 200,000 type script files 600,000 lines of code. 

[01:37] some of them are pretty wild, it also kind of gives us an idea of how big the OpenClaw release was, how much of an effect it had on these AI labs, because I think it's very fair to say that a lot of these features are in some way, shape, or form a response to OpenClaw. 

[03:56] In effect what happened was they copied over the code and then they used the code to kind of copy over the functionality right because now the functionality is the same but the code is different the code is no longer the code that anthropic who wrote it's entirely different same functionality completely different code. 

[04:33] how did they manage to replicate it? Well, with codeex again, you know, OpenAI's AI coding tool, right? So, they used OpenAI's AI coding tool to completely basically recreate clot code. 

[06:45] One of the features, this is probably not the biggest one, but I thought it was interesting. It was kind of a Tamagotchi Easter egg. It was like a whole thing with Tamagotchi different creatures that did stuff and grew and had various like legendary status, common status, whatever it is. 

[08:47] Mythos model coden named capiara. So first and foremost that that is referenced in there. There's also something called chyros, a background agent. So it's an autonomous agent that runs constantly without human user input. It monitors GitHub repositories and sends updates. 

[09:39] This specific model fully goes through the entire plan, fleshes everything out, you know, gets all the checklists, everything it needs, and then from that the next step happens, whether that's like a coding agent that gets spun up or whatever. 

[10:05] coordinator mode. This is a multi- aent swarm. Now that these companies are actually developing them and they're trying to use them for, you know, enterprises, you know, they're not going to call it swarms. So the idea is simple one claude agent orchestrates a bunch of other clouds. 

[11:03] We also have persistent memory across sessions. So real memory doesn't get wiped between sessions. It accumulates. /advisor where you get a second model to overview claude's outputs. There's also slashgoodclaude slashbug hunter and slash teleport. 

[14:49] Chloe is sort of watching your language to try to figure out if you're getting frustrated, if you're maybe losing patience with Claude. So, there's some sort of a process there. It's like, is this user about to lose it? 

[15:12] 187 different verbs for the loading spinner text. There's a lot of X42 references. So this is kind of like the protocol for crypto prints. So if you were building an infrastructure to allow a Gentic crypto payments, there's a lot of references to that. 

[16:56] Capybara was being tested out internally. what they did is they just encoded all the 18 species of the Tamaguchi pets in hexadesimal. If you're not sure what that is, it's like if you have a dog and every time you say walk, it loses its freaking mind because it knows what walk means. You can't say walk, right? So what do you do? You spell it out. 
