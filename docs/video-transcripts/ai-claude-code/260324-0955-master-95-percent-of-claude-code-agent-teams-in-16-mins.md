# Master 95% of Claude Code Agent Teams in 16 Mins

**Channel**: Nate Herk | AI Automation
**Duration**: 16:29
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=vDVSGVpB2vc
**Transcribed**: 2026-03-24 09:55

---

## Organized Notes

**What Are Agent Teams**

- Agent teams are **multi-agent systems** in Claude Code where a **main orchestrator** creates and manages multiple specialized agents working together
- Key difference from sub-agents: sub-agents work **independently** and return results to the main agent — agent teams have a **shared task list** and teammates can **talk directly to each other**
- The main agent acts as a **team lead/project manager**, ensuring tasks get done at high quality
- Teammates can create **feedback loops** — e.g., a QA agent can reject work and send it back to developers for another pass

**Setting Up Agent Teams**

- Agent teams are **disabled by default** (experimental feature) — must be enabled via `settings.json`
- Add the environment variable to **project-level** settings in `.claude/settings.local.json`
- Recommended: **train your Claude Code project** on agent teams by fetching the official documentation URL and saving it as a local markdown reference guide in a `docs/` folder
- This gives agents **local access** to documentation for quicker lookups during builds

**Prompting Agent Teams Effectively**

- Follow this pattern: **"Create a team of X agents using [model]. The first agent is [role]..."**
- Start by **establishing a goal** — agents wake up with **no context**, so the goal helps them understand what they're working towards and why teammates exist
- Define **specific deliverables** for what you want returned at the end
- Example structure: goal → team creation → agent roles with responsibilities → inter-agent communication instructions → final deliverables

**Dos and Don'ts**

- **Do** have each agent own **specific files** — prevents agents from overwriting each other's work
- **Do** define clear **output deliverables** — avoid vague descriptions
- **Do** name message **recipients explicitly** — don't assume agents know who to talk to
- **Do** keep teams to **3-5 teammates** — avoid 10+ agent swarms (10x more expensive)
- **Do** give **full context** in prompts — no history is fed in initially (agents can still read project files)
- **Don't** use agent teams for **sequential workflows** — that's what sub-agents are for
- **Don't** use them for **simple tasks** — overkill and expensive

**Tmux Split-Pane View**

- Running Claude Code in a **tmux terminal** unlocks visual monitoring of each agent in separate panes
- Each agent gets a **color-coded pane** (blue for front-end, green for back-end, yellow for QA)
- You can **individually message** any agent from its own pane — not just through the main session
- Enables watching agents **research, create, and communicate** in real time

**Three Key Rules for Agent Teams**

1. **Own territory** — each agent should edit only their own files and deliverables
2. **Direct messaging** — agents can talk to each other without going through the main session as middleman
3. **Parallel work** — agents work simultaneously, not in a sequential handoff chain

**What Teammates Know When They Wake Up**

- They **inherit permissions** from the main session (bypass permissions, allowed bash commands)
- They can access all **project files, MCP servers, and skills**
- They have **no conversation history** — only the prompt the main session feeds them

**Plan Approval Mode**

- Agents can be required to **plan first** and get their plan approved by the main agent before executing
- Alternative: **you approve** every plan manually until you understand the team workflow
- Another option: dedicate **one teammate as a plan reviewer/approver**

**Common Pitfalls and Fixes**

- **Agents keep asking permissions** → preapprove certain tools in project/local settings
- **Deliverables feel disjointed/overwritten** → assign explicit file owners
- **An agent sits idle** → assign specific work or dependencies in the prompt
- **Burning too many tokens** → use fewer agents
- **Agents losing work** → tell them to store everything as **temporary files** they can reference later
- **Wrong approvals** → have yourself approve things until you understand the flow

**When to Use Agent Teams vs Sub-Agents**

- **Use agent teams when**:
  - Project has **multiple specialized areas** needing parallel work
  - Agents need to **react to and communicate** with each other
  - High quality output requiring **multiple review steps**
- **Use sub-agents instead when**:
  - Work is **sequential** (step 1 → 2 → 3)
  - You need everything in **one context window**
  - Agents don't need to **communicate**
  - You want to **save tokens**
- Keep to **2-5 agents max** for cost efficiency
- **Shut down agents cleanly** — the main session sends a shutdown request and agents confirm they've saved their work before closing

*Quotable Quotes (Nate Herk):*

> "This is truly one of the most powerful AI agent features I've ever used, but you have to know how to use it." [01:16]

> "Sub agents work independently and then they send their individual result back to the main agent. Agent teams have a team lead, maybe like a project manager, and it creates all of these different agents and a shared task list." [01:47]

> "If you wanted to really really understand how agent teams work, then spin up an agent team to help you explain agent teams." [09:36]

> "Agent teams work together in parallel and need to communicate throughout the whole process." [12:03]

---

## What This Means for Your Work

**Your 9 platform projects are the use case for agent teams.** You're a solo dev building government-scale systems — e-Bangsamoro (4-portal governance platform), e-Negosyo/MoroMarket (cooperative marketplace), Tarbiyyah-MS (madrasah management), BangsamoroHR, SBP, OBCMS. Each has React 19 frontend + Django backend + PostgreSQL. Agent teams let you simulate a 3-person dev team: frontend agent, backend agent, QA agent — with the QA sending work back when integration tests fail. That feedback loop is something your current /spawn sub-agents can't do because they work independently and return results, not iterate.

**Map it to your frontend-first pipeline.** Your /devwork skill defines the sequence: React component → TanStack Query hook → DRF endpoint → integration test. An agent team automates this as a coordinated flow instead of you manually orchestrating handoffs. The frontend agent builds the component, messages the backend agent with the API contract, the backend agent builds the endpoint, and the QA agent validates both. If the QA agent finds the API response shape doesn't match the frontend's TypeScript interface, it sends the work back — no human intervention needed.

**Reserve for complex modules, not routine work.** At 3x token cost per agent, agent teams are expensive. Your e-Bangsamoro has 7 primary modules (Dashboard, Legislative, Oversight, Representation, Ministerial Planning, Budget, Office Management). Use agent teams for complex feature builds within these modules — like parliamentary voting, MANA assessment, or budget tracking dashboards. Keep using regular sub-agents for simpler parallel tasks like batch transcriptions, vault operations, or independent file edits.

**Plan approval mode fits your discipline.** You already use plan mode before implementation and require manual git commits. Having agent teammates submit plans for your approval before executing code is a natural extension — you stay in control of the architecture while agents handle implementation.

**Your OOBC and legislative work stays with skills, not agent teams.** Bill drafting (/bangsamoro → /bill-drafter → /fact-checker), policy recommendations, and legislative briefers are sequential workflows where each step needs your review. Agent teams are for parallel implementation, not sequential document pipelines.

**Concrete next steps:**
- Enable agent teams in e-Bangsamoro's `.claude/settings.local.json`
- First test: a medium-complexity e-Bangsamoro feature with 3 agents (frontend, backend, QA)
- Set up tmux split-pane monitoring before the first real build
- Create a reusable prompt template mapping to /devwork's frontend-first pipeline stages

### How This Can Improve Your Claude Skills and Workflows

**Agent teams are the implementation layer for your /sp-dispatching-parallel-agents superpower.** Your /sp-dispatching-parallel-agents currently spawns independent sub-agents. Agent teams add what sub-agents lack: shared task lists, direct inter-agent messaging, and feedback loops. For an e-Bangsamoro legislative module build, the difference is significant. Sub-agents: frontend agent builds component, backend agent builds endpoint, you manually verify they match. Agent teams: frontend agent builds component and messages backend agent with the TypeScript interface, backend agent confirms or negotiates changes, QA agent validates the integration. No human intermediary needed for the coordination step.

**Your /devwork skill should include an "agent team mode" with a pre-built prompt template.** The video's prompting pattern (goal, team creation, agent roles, communication instructions, deliverables) should be codified as a /devwork option. When you invoke `/devwork --team`, it generates a structured agent team prompt based on the current project's CLAUDE.md, assigns file ownership based on the frontend/backend/test directory structure, and specifies the inter-agent communication protocol. This eliminates the overhead of writing a custom agent team prompt for every feature build.

**The "own territory" rule (each agent edits only their files) maps to your platform architecture.** For your React 19 + Django stack: frontend agent owns `src/components/`, `src/pages/`, and `src/hooks/`. Backend agent owns `api/`, `models/`, and `serializers/`. QA agent owns `tests/` and `playwright/`. This territorial division prevents the most common agent team failure (overwriting each other's work) and aligns with your existing directory structure across all 9 platforms.

**Plan approval mode integrates with your existing discipline of reviewing before committing.** You already use plan mode and require manual git commits. With agent teams, set the QA agent as the plan reviewer for frontend and backend agents. The QA agent checks plans against acceptance criteria from the GitHub issue before approving execution. You only intervene when the QA agent escalates. This adds a quality gate without requiring your constant attention during multi-agent builds.

**Agent teams are overkill for your legislative workflow -- keep /bill-drafter as a sequential skill pipeline.** The video warns against using agent teams for sequential work. Your bill drafting pipeline (/bangsamoro context, /bill-drafter, /fact-checker) is inherently sequential -- each step depends on the previous step's output. Agent teams add cost and complexity without benefit here. Reserve agent teams for parallel implementation work on your coding platforms; keep legislative skills as streamlined sequential flows.

**The tmux split-pane setup should be standardized as part of your development environment.** Create a tmux configuration file in your skills-bucket that launches a 3-pane layout (frontend blue, backend green, QA yellow) pre-configured for your React + Django stack. Store it as ~/apps/skills-bucket/agent-team-tmux/tmux-config and reference it in /devwork's agent team mode. This eliminates setup friction every time you spin up an agent team session.

---

## Transcript

[00:00] I just pasted in this message and I'm shooting it off to Claude and it says create a team called Neuroflow of three teammates using sonnet. The first one is a front-end developer. The second one is a backend developer and the third one is a QA agent. So this now invoked a tool

[00:12] called team create. And you can see that what it's doing is now that it's created this team, it's spawning up three teammates in parallel and these are all individual agents. So right now we can see we have our front-end developer, we have our back-end developer and we have our QA agent. So, what's happening is

[00:26] right now we have these three agents working together with our main session. They all share a task list. They can talk to each other and I'm going to check back in with you guys once this is done. Okay, so this is really

[00:35] interesting. The front end and backend developer sent work over to the QA agent and then the QA agent found three critical issues. So, the main agent said that it's going to send all of this work right back to those first two agents to take another pass at it. So, here's

[00:47] where you can see it sent off those messages to the front-end developer, the backend dev, and the QA. And now they're all back to work once again. And there we go. The second time the QA agent

[00:55] gives it a pass. All three of those critical issues have been resolved and then it was able to basically oneshot this website. Now, obviously there are some things that aren't perfect about this and we'd want to go back and iterate, but considering in the prompt all I said was to build me a landing page for a fictional AI startup and we get all of this text, we get these animations, we get all of this stuff to come in dynamically and it feels pretty polished. It came up with all the copy,

[01:16] the color scheme, all of it. This is truly one of the most powerful AI agent features I've ever used, but you have to know how to use it, right? Which is why in today's video, I'm going to explain everything you need to know. What they

[01:25] are, how to set them up, how to use them, when not to use them, everything that you need. So, let's not waste any time and get straight into the video. So, agent teams, as you guys saw in the demo, we had one get spun up called Neuroflow. And in that team, we had

[01:37] three agents. We had the front-end dev, the backend dev, and the QA. So, what happens is the main orchestrator, the cloud code session you're talking to, creates these different agents and manages them. but not in the same way

[01:47] that we do sub agents because sub aents work independently and then they send their individual result back to the main agent. Agent teams have a team lead maybe like a project manager and it creates all of these different agents and a shared task list. So the huge unlock here is that individual teammates can talk to each other. So sometimes

[02:04] there's a dependency. Teammate one needs something from teammate two and they can just talk. And you can get in these really cool loops, especially when you have the QA agent like we just saw in the demo where one of the teammates will basically say, "Hey, this isn't good enough." and send the work back. And

[02:16] then the main agent, like I said, is just making sure that the tasks are getting done and that they're all high quality. So that's the big difference between sub agents and agent teams. And I had to clear that up because I know that's probably where there's some confusion. So I am going to break more

[02:27] stuff down, but what I wanted to do first is just show you guys how to set this up because I think the best way to learn is just to be able to play around with stuff. And all you have to do to set this up is add one environment variable into your project setting. So let me show you how that works right now. All right, here I am in cloud code.

[02:40] I like to use it in VS Code, but you can use the agent teams feature wherever you decide to use cloud code. You can see that I am in a brand new project with nothing in it. So this is exactly what one of your guys' setup should look like if you want to follow along. So like I

[02:52] said, we need to enable the feature and I'm going to do that in this demo on the project level. So what I'm going to do is go to the official cloud code documentation for agent teams. And you can see right here that it says they are disabled by default because it's an experimental feature. So you have to

[03:04] enable them by adding this variable into your settings.json. So what I'm going to do is literally just copy this JSON right here and come into cloud code and say, "Hey, I need you to put this in our local settings in this project and then just paste in that JSON prompt." And I'm

[03:19] going to go ahead and shoot that off. And that should basically be able to create that file for us. So you can see that it set everything up. We now have

[03:24] acloud folder. If I click in here, we have a settings.local.json.

[03:28] and it has put that command in there. And now our project should be set up to actually be able to use agent teams. Now, before we dive in and I start showing you guys how to do that, there is one thing that I recommend doing first. And that's basically training

[03:39] your cloud code project on how agent teams work so that they can actually be used as effectively as possible. So, the easiest way to do this is you go to the documentation on agent teams. You take the URL and you copy it. And then I

[03:50] said, "Hey, create me a master reference guide for agent teams in a folder called docs. This will be used to help you build better and more effective agents in the future." And now it's going to read through that documentation. And now

[04:00] if you ever have questions about agent teams or if it ever needs to look up something while it is building them, it already has that locally here stored as markdown. So it's going to be much quicker. And it just created this documentation about enabling them, when to use them, display modes, task management, hooks, best practices, tons of stuff like that. And that can be

[04:16] found in the docs folder in this section, which is a full markdown file with hundreds of lines. And that's just a little tip. That's something that I like to do whenever I have like maybe a big MCP server or certain documentation that I know it might need to look at constantly. So, now that we're pretty

[04:30] much set up and ready to start building, let's talk about prompting. How do we actually tell Cloud Code to build us agent teams, but not just to build them, but to actually make them really good to give you what you want? Because the truth about agent teams is that they are more expensive and they are a bit slower, but you do get much higher quality if you use them right. Now, the

[04:46] good news is you can pretty much invoke them just using natural language. So, I kind of follow this pattern. create a team of X number of agents using X model. So, Haiku, Sonnet or Opus and

[04:57] then you basically just say the agents that you want. You would say the first agent is X ro this agent should be doing this and it should produce me this. It can talk to the other agents to do X Y and Z. And so pretty much just listing

[05:11] that out in natural language whether that be an API designer, a database engineer and or a test writer. So let's take a real quick look at an example prompt. So, I'm going to read this full one out. Now, what you'll notice is I

[05:22] start off by establishing a goal. The reason I do this is because when the agents wake up, they have no context. They basically only get the prompts that the main session feeds into them. So, if

[05:32] we tell the main agent a goal to give to these sub agents, they understand a little bit better, you know, like what they're working towards, but also why they have their teammates next to them. So, the goal here is to build a working full stack app with a REST API and a React front end. The end result should be a running app that I can view on a local host. It should have users and

[05:49] post functionality plus a QA test report confirming that everything works. So then I said, "Hey, create me a team of three teammates using Sonnet." The first one's a back-end dev. It should be doing

[05:58] this. The second one is a front-end dev and it should be doing this. And the third one is a QA agent that should be doing this. You can see that in the

[06:06] descriptions I said when you're done, message the front-end dev. And then in this one, I said wait for the backend dev's message and then you will send all the stuff to the QA. And then I'm saying what the final deliverables should be because the main agent spins these three up. And then it's going to get a bunch

[06:20] of information back. So what do I actually want at the end of the day? I want a running app. I want a report

[06:25] about pass and fail tests. And then I want a doc, which is basically what was built, key decisions, and how we run this moving forward. So we're about to hop right back into cloud code and live prompt an agent. But real quick, let's

[06:38] talk about some dos and don'ts. So, do have each agent own specific files because if you don't do this and agents are sharing files, they might overwrite each other's work, which is not good. Do define the output. Don't use vague

[06:49] deliverables. Do name recipients. Don't just assume that they're going to understand who to talk to and why. Do

[06:55] have about three to five teammates. Don't go for massive agent swarms of 10 plus. That'll also be 10 times more expensive. And do give full context

[07:03] because of the fact that no history is given beforehand. Now, of course, they can still read everything in the project. they can still look through all of those files, but no context is fed in initially. And I will show you exactly

[07:14] what I mean by that when we go in here and spin up a new agent team. Okay, so I'm in that project that we set up together. I'm in a fresh session and I'm going to send off this prompt. I said

[07:22] that the goal is to help me clean up the workspace. We have three agents called research team. We're using Sonnet. We've

[07:27] got a researcher, a strategist, and a critic. And they're basically just going to read through this project and make sure that everything's accurate and make sure that we're set up good. Let's take a look at what's going on. It's creating

[07:36] the research team, right? So, it's created the team and now we have a to-do list. Now, what it's doing is it's going to spawn the three teammates in parallel. And when it spawns these, I'm

[07:44] going to actually show you how. So, the first one is a researcher. If I click into this, you can see that this says in. So, this is basically saying this is

[07:51] what the main agent sent to the agent. You are the researcher on the research team. Here is what your job is and you have to be thorough and include anything that might be helpful. So, this is

[08:01] basically the prompt that spun up that agent. You can see same exact thing happened for the strategist and for the critic. And if I clicked in, we could once again read exactly what they were prompted to do and the step-by-step instructions, including stuff like when you're done, send your five use cases to the critic teammate using the send message tool, which once again validates that these agents are able to talk to each other and send messages to each other. So now we can see that all three

[08:25] of our agents are running and they are all basically just waiting for their turn. And you'll notice what it does is pretty much every time there's a new update, it updates me. So, here comes another live update. Let's see if the

[08:34] researcher is finally done. There we go. It's done. So, now what happens is we

[08:38] sent a message off to the researcher. And let's go ahead and see what that message actually said. So, this is the main agent talking to the researcher. It

[08:46] said, "Did you send your structured inventory to both the strategist and the critic? Please make sure the strategist also received it. You were asked to message both teammates." And then we can

[08:55] see that the researcher confirmed that both teammates received the inventory. And now the critic is running. All right. So, everything just finished up.

[09:01] All the reports are here, but real quick, I wanted to draw your attention to this. The main agent said, "Cool. Let me shut down the teammates and finalize." And I'll touch on this a

[09:09] little bit later, but now the main agent has sent a message to each of them, the researcher, the strategist, and the critic. And basically said, "You're done. Save your work." So anyways, we'll

[09:18] come back to that in a little bit. But we now have an output, which is a new document over here, agent teams, patterns. And it found a ton of stuff.

[09:25] There were 11 documentation gaps identified that are worth reviewing against your reference doc. So anyways, let's just click into the doc real quick. We're not going to read this whole thing cuz I'm assuming it is super long. But this is the actual output that

[09:36] we just got from this agent team. And you can see that this thing is insanely thorough. So if you wanted to really really understand how agent teams work, then spin up an agent team to help you explain agent teams. Now what you'll

[09:46] notice here is we were kind of able to see what was going on, but not really under the hood. We couldn't actually tell what the agents were thinking or doing. And that's because we're doing this in the Cloud Code extension. If you

[09:56] do this in your terminal and specifically if you have T-Mox installed, you can actually see the different agents working and thinking and you can individually send messages to them because right here we're kind of only communicating through the main session and the main session sends messages to the other ones. But one of the value props of agent teams is that I could individually message a sub agent if I wanted to. So let me show you what that looks like. All right, so right now

[10:17] I'm running Cloud Code in a T-m terminal. Now if you're on Windows, you have to take a little bit of a workaround, but you just have to be in a T-m terminal. So, I'm not going to do a full setup video on it right now, but I literally just had Cloud Code walk me through it, and it was super simple. But

[10:30] anyways, what I did here is I just pasted in this prompt, which obviously is like we talked about. We have the goal. We say create me an agent team, and then we have our front-end dev, our backend dev, and our QA. This is

[10:39] basically the same exact prompt that I ran in the demo. So, this isn't to show you the actual deliverable. What I want to show you guys here is the way that we can visually see this. So, right here,

[10:47] what it's going to do is it's going to spin up that agent team for us, right? It's setting up the task dependencies and it's assigning owners. And now it's spawning those agents. And there we go.

[10:55] We just got our front-end dev created right here. And this is the blue agent. We have another one right here, which is the backend dev. And this is the green

[11:03] agent. And there we go. We just got our QA agent, which is the yellow one. So

[11:06] now I very clearly can see what each of these agents is doing, which is super cool. And now if I wanted to, I could come over here and I could check on the team status with the main session. I could come up here and I could talk to the front-end dev. I could approve

[11:18] things or I could give it more info. Same exact thing with the QA or same exact thing with the backend dev. So now I literally have an agent team that I can watch and I can interact with any of them. And I can also watch them do

[11:29] research, create things, talk to each other. It's super super cool. So like I said, I'm not going to run this whole thing out. I just wanted to show you

[11:35] guys that this is possible. Okay, now that we've seen some cool demos, let's talk about how do we actually make these things better and better and understand a little bit more about what's going on. So here are three key rules. The first

[11:47] one is that each of these agents has their own territory. So, they should have their own file and they should be working on their own deliverables. They can send them across and they can communicate, but they should only really all be editing their own thing. The

[11:58] second thing is once again direct messaging. They can talk to each other. They don't have to use the middleman of the main session. And then the third

[12:03] piece is that they can be working at the same time. It doesn't have to be agent one hands off to agent two and then agent two hands off to agent three because that honestly might not even call for an agent team. Agent teams work together in parallel and need to communicate throughout the whole process. So what do teammates instantly

[12:18] know when they wake up because we know that they don't have any context from the jump. What they do have is they inherit the permissions from the main session. So if you're on bypass permissions, then all of your agents are going to be on bypass permissions. If

[12:29] you allow all bash commands, then those same permissions will once again be inherited by the teammates. But the other thing to know that's very important is that any of your files, any of your MCP servers, any of your skills, all of the teammates can use and access those things. We also have a really cool ability to use something called plan approval mode. So you guys know how I've

[12:47] told you always start in plan mode. If you plan with your main session before anything actually happens, it's way better. What we can do is we can have all of those agent teammates plan first and they have to basically get their plan approved by the main agent before they're actually allowed to go execute.

[13:03] So, it's really cool. You could also set it up where you're actually the one who has to approve every single plan. But, I think it's probably better to just have the main session do that. Or maybe even

[13:12] one of the teammates is just the plan reviewer and approver. So, I wanted to talk about some common pitfalls or mistakes that you might be making and what the fix could be for that. So, the first one is if the agents keep asking permissions and they keep stopping for that, you can preapprove certain tools.

[13:28] So, that would be in your project settings or your local settings. you can allow certain commands and that way they won't stop to ask you something every couple seconds. If the deliverables aren't coming out feeling holistic, maybe they're being overwritten. So,

[13:40] make sure that you assign file owners. If you spin up an agent team and you realize that one of the agents isn't really doing much or is just sitting around, then maybe you want to specifically make sure you're assigning each agent work or some sort of dependency in your plan, in your prompt. If you're burning through way too many tokens, just use fewer agents. If it

[13:56] seems like your agents are losing work, then tell them to basically store everything as a temporary file that they can then call on later. And if you're getting the wrong approval and it just seems like it's off, then maybe just try to have you be the one who approves things to start until you understand the flow of how these teams work a little better. All right, so next I wanted to talk about when to use agent teams because like I said earlier, they can be slow and expensive. So you really just

[14:15] want to use them when you need something pretty complex done and you need lots of different specialized agents. So think about using them if your specific process or project has multiple different areas. And that way you can have one specialize in each of those. If

[14:28] you need those things to be done in parallel, if you need them to be able to react to each other, assign tasks to each other, communicate with each other, and if something needs to be done at a really high quality, and you want tons of different steps to make sure, then an agent team is probably a decent idea. Now, if you have a process that could be done sequentially, meaning every time it basically goes 1 2 3, and those steps are dependent on each other, then maybe an agent team isn't the right call. Maybe that's just sub agents. If you

[14:50] need everything in one specific conversation history or one context window, then don't use teams. If you're just kind of working on the same files, don't use teams. And if it's a very simple task, then agent teams would be overkill. There might be a lot of times

[15:02] where you'd be able to use sub agents instead. Like I said, with sequential or if you need a very focused result, if you don't need the agents to communicate, and if you want to save some tokens, because once again, if you have three sessions running, that's basically going to be three times the cost. So if you have five, it'll be five times the cost. Which means I like to

[15:18] stay around maybe two to five agents max. You can keep them running parallel. Otherwise, you can use sub aents and make sure that you are shutting them down if you see them early on going off down the wrong path. Which is another

[15:30] reason why I think it's helpful to use the T-Mox version so you can actually see them in that split pane view. And when I say shut down, which is kind of what we saw earlier, I just mean basically at the end of every session saving your work. Because remember right here how we saw the main session say hey this is a shutdown request. The

[15:46] researcher agent here could have said I'm not done yet. Let me save stuff. Don't shut me down yet. So when the

[15:51] teammates actually confirm that they're ready to be shut down. That means that everything's good and we can essentially cleanly save that work. So everything gets cleaned up and then we're good to close the session and shut down that agent team rather than just force killing it right away where things might be all out of control and not cleaned up yet. Well all right that is agent teams.

[16:08] I hope by now you are excited to hop into Claude Code and start building with some agent teams. And if you want to check out other Cloud Code stuff that I've been doing to expand your learning, then definitely check out this video right up here. Hopefully I'll see you guys over there. But that is going to be

[16:20] the end of the video. So if you enjoyed or you learned something new, please give it a like. It definitely helps me out a ton. And as always, I appreciate

[16:25] you guys making it to the end of the video. I'll see you on the next one. Thanks everyone.
