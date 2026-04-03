# Claude Code got leaked

**Channel**: The PrimeTime
**Duration**: 11:59
**Language**: English (manual) [yt-dlp subtitles]
**URL**: https://youtube.com/watch?v=GdgRpiQRsis
**Transcribed**: 2026-04-01 15:52

---

## Organized Notes

**The Root Cause: Supply Chain and Runtime Bugs**

- **Source Map Exposure**: The leak was enabled by **source maps** published to **npm**. Source maps allow minified JavaScript to be translated back into the original TypeScript structure, including long variable names and comments. [00:47]
- **The Bun.js Connection**: The leak was potentially caused by a known **Bun.js** bug (reported 3 weeks prior) where the front-end development server incorrectly served source maps in production environments. Anthropic's team had reportedly flagged this as a potential duplicate issue but failed to mitigate it before the leak. [01:37], [02:08]

*Quotable Quotes:*

> "Claude Code is very 'vibe coded.' It's staff-level spaghetti, and a company moving this fast is just going to have so many flaws." [08:55]

> "Their terms of service says you can't build a competing product. But what if you're building an always-on bot? Is that competing with Chyros? You might be deemed a competing product just by being successful." [09:19]

**Security and Safeguards: The "Vibe Coded" Reality**

- **Hard-coded Sentiment Analysis**: Instead of using an LLM to determine prompt sentiment, Claude Code uses a **hard-coded regex** white-list of "bad words" (e.g., "pissed," "damn it," "useless," "screw this") from 2005-era logic to detect negative patterns. [04:12], [05:57]
- **Static Safety Instructions**: Cyber-risk and safety instructions are stored as long, hand-crafted embedded strings. The code contains internal warnings telling developers not to modify them without reaching out to specific safety leads. [04:49]
- **Undercover Mode**: A dedicated "don't blow your cover" mode for Anthropic employees. It mandates that they never identify as Claude Code or mention their AI nature when interacting with public repositories, and forbids "co-authored by" attributions. [06:34], [07:19]

**Technical Risks and Ethical Concerns**

- **MCP Security Flaw**: The codebase reveals that the **MCP (Model Context Protocol)** command can be triggered to print sensitive environment blocks, including **secrets, headers, and O-Auth hints**, directly to the terminal if not carefully managed. [07:49]
- **Terms of Service (ToS) Enforcement**: Anthropic's ToS prohibits using Claude to build "competing products." This creates a legal gray area for developers building autonomous agents, long-term memory systems, or multi-agent orchestrators—features Anthropic is internally developing (e.g., **Chyros**, **Karios**). [09:19], [10:36]

**Easter Eggs and Creative Direction**

- **Slash Buddy**: A virtual "Tamagotchi-style" pet (e.g., species like **Cosmos Hail** or **Nebu Lynx**) that sits in the terminal. While released as an April Fool's prank, the source code reveals a deep "buddy" system with stats, feedback loops, and "shiny" rarities (reminiscent of NFTs). [05:12], [07:06]

---

## What This Means for Your Work

The security-focused analysis from **The Primeagen** highlights significant risks you must mitigate in your **e-Bangsamoro** and **OOBCMS** workflows. The **MCP Security Flaw** (where environment secrets can be leaked to the terminal) is a P0 issue for your ministerial integrations—you must audit your MCP server configurations to ensure that your **AWS** or **Bangsamoro Health** database credentials are never stored in the environment block where a Claude session can read/print them.

Furthermore, the **Terms of Service** warning about "competing products" is a strategic consideration for **MoroTech**. Since you are building a platform that uses agents for job placement and career coaching, you should be aware that your "always-on" coaching bot could technically be seen as a competitor to Anthropic's unreleased **Chyros** agent. To protect yourself, ensure your platform adds unique, domain-specific value (Bangsamoro-specific labor laws and cultural context) that differentiates it from a general-purpose coding agent.

### How This Can Improve Your Gemini Skills and Workflows

This video suggests several defensive and architectural upgrades for your skills-bucket:

- **Security Hardening**:
  - [[mcp-server]]: Add a "Secrets Audit" phase that prevents the server from exposing the `env` block to the client. Use a proxy layer to inject credentials only at the moment of execution.
  - [[fact-checker]]: Use the "hard-coded sentiment" insight to build your own lightweight, regex-based "Hallucination Trigger" list. Certain phrases (e.g., "I apologize, but as an AI...") can trigger an automatic retry with a different model.
- **Workflow Changes**:
  - **Identity Management**: Adopt a version of the **Undercover Mode** for your own automated agents. Ensure they always provide a standard disclaimer about their purpose and the user (Saidamen) they are acting for, to maintain transparency in BARMM git repos.
  - **Context-as-Cost**: Follow the "staff-level spaghetti" warning. Keep your **GEMINI.md** clean and modular—avoid the "artisanal safety string" bloat that slows down Anthropic's own runtime.
- **Project Applications**: 
  - For the **Parliamentarian** app, implement a **Slash Buddy** equivalent—perhaps a "Legislative Assistant" pet that grows in "Expertise Stats" as you successfully draft more bills, making the repetitive work of legal research more engaging for your team.

---

## Transcript

[00:00] coding has largely been solved. Well, I mean, it's been largely solved thanks to Anthropic for releasing opensource all of Claude code again. Yes, this is actually the second time that Anthropic just published all of it. Now, the last time they did that, they went through and DMCA all these people on GitHub. 

[00:31] What actually ended up happening is that anthropic with cloud code published to npm all of it. All the source maps. And if you don't know what a source map is, it effectively allows you to have minified JavaScript. And then if you apply the source map, it can translate the minified JavaScript back into the original structure of the code. 

[01:05] There is some really, really, really funny things. There's some things that are less so funny and also it showed that Anthropic is susceptible to the Axios supply chain attack as well. 

[01:25] Well, it turns out 3 weeks ago, a guy named Jake G, hey, pour one out for Jake G, opens up a ticket that says, "Buns front-end development server source maps incorrectly served when in production." 3 weeks ago, GitHub actions, hey, this is probably a duplicate issue found via cloud code. 

[02:18] Okay, can we just pour one out for poor Daario? Right now he's probably making a very painful face and realizing that the safety of the world might be compromised if Claude Code's code is still available publicly. 

[03:58] How would you say determine sentiment of a prompt? Now, if you would have guessed a hard-coded reax that determines if you said the word dam or not, then you are 100% correct because that's what Claude Code does. 

[04:12] Look at this. This is on Twitter right here. If you if you say the word horrible or dumbass, awful or piss, pissed, pissing, piece of crap, junk, what the Hell broken, useless, terrible, awful, horrible. you. Screw this. you. So frustrating. This sucks. Damn it. That's a negative pattern right there. 

[04:42] Coding has largely been solved because this style of problem solving, it's been around for decades. Have you ever wondered how Claude Code does its skills? Well, it turns out there's some very great great ones inside the repo, including cyber risk instructions, which is just one long embedded string with a comment saying, "Hey, if you're going to modify this, you first need to go reach out to David or Kyla." 

[05:12] I would have at least thought that these things would have been like server side, you know, so that way no one can mess with this. Also something that kind of felt really disappointing they are actually building a buddy like a Tomagotchi inside the terminal apparently this is going to be released April 1st through the 7th and then maybe even longterm just out there at infinitum. 

[06:02] They also have a shiny chance. So, you like this is just full-on Pokemon cards. They're just creating Pokemon tradable cards inside of Claude Code. They're actually creating NFTTS right now. Somebody on the marketing team at Cloud was like, "You know what? We need we need more Tamagotchis." 

[06:34] Also, they have this weird don't blow your cover mode. So, if you are an anthropic employee poking around in a public repo, it has all these rules like, hey, you're not supposed to say that you're Claude Code or mention that you are an AI anywhere at any point. Don't mention anything internally. Don't do co-authored by lines or any other attribution. 

[07:19] It honestly just makes you sound like a bad guy. Again, Dario, you're being a bad guy. You don't have to be a bad guy. Just quit doing things that just feel slimy. 

[07:25] something that I think is pretty important to kind of talk about is that whenever these type of things happen where a bunch of source code gets leaked that was meant to be hidden and there's 500,000 lines of source code apparently spread over 1,900 files, there's just going to be bugs and security issues that would normally be very hard to discover. 

[07:49] People are in fact going to figure out how to take like advantage of you. The MCP command is wild. run claude MCP get name and it happily spits out MCP server URLs headers OOTH hints and for standard input output servers the entire environment block if your envir contain secrets they get printed straight to your terminal whoopsies. 

[08:41] But your Gemini credentials they're going to want. I just have a sneaking suspicion that we're going to see, you know, some issues kind of arise over the next 6 months of just skills that can take advantage of certain internal setups. 

[08:55] Because let's just face it, Claude Code is very vibe coded. Chad GPT called it staff level spaghetti. I actually don't know what that means. I'm not really sure the difference between a junior level and a staff level spaghetti, but nonetheless, a company moving this fast is just going to have so many flaws. 

[09:19] This last part is going to be a bigger general warning for using Clawude just in general, which is that they have a terms of service saying that you cannot use Claude to build a competing product. Well, what if you're building an always on bot? Is that competing with Chyros, the always on Collad? Maybe you're building some sort of remote planning sessions. 

[10:36] Hey, sure. We used all of yours and likely used all of your, you know, regardless of the type of license you put on there. We definitely took all of that, used all of it. But if you take our code, then we're going to sue you. Because we are the correct ones. Use the super thanks option below. Or you can consider joining our private Discord where you can access multiple subscriptions to different AI tools for free on a monthly basis. 
