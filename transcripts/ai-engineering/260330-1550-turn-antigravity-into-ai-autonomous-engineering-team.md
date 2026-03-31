# Turn Antigravity Into AN AI Autonomous Engineering Team!

**Channel**: WorldofAI
**Duration**: 14:55
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=yuaBPLNdNSU
**Transcribed**: 2026-03-30 15:50

---

## Organized Notes

**The Problem: Antigravity Plans But Cannot Execute**

- **Antigravity's mission control** is a built-in system within the IDE that handles background task delegation, lets you architect custom sub-agents with specialized skills, and treat them like **programmable AI modules**
- Example: asking mission control to "onboard new designers" automatically broke the task into sub-agents -- one crawled the company website for fonts/logos/colors, another compiled an internal walkthrough, a third drafted an onboarding email in Gmail
- The limitation: **Antigravity's agent system stops at planning** -- it does not have a secure, scalable way to take real-world actions across tools like GitHub, Slack, Google Docs, email, or calendar
- Actions across real tools are typically **brittle, hacked together, or unsafe**

**Arcade.dev as the Execution Layer**

- **Arcade.dev** is an MCP runtime (and sponsor of this video) that provides the **execution backbone** for agents to operate in the real world
- Tagline: "Go Beyond Chat: Make AI actually do things"
- Connects to **7,500+ tools** (as stated in the video) -- emails, files, calendars, APIs
- Handles **authentication automatically** via OAuth -- no API keys in code, no scraping
- Maintains **auditability** and secure structured actions
- **Pricing**: free Hobby plan (100 user challenges, 1,000 standard tool executions, 50 pro tool executions/month); Growth plan at **$25/month** (600 challenges, 2,000 standard, 100 pro executions)
- Key concept: Arcade turns agents from **planners into operators** -- they can log into tools, take real actions, and complete workflows

**Setting Up the MCP Gateway**

1. Install **Antigravity** on your OS and create an **Arcade account** (free Hobby plan works)
2. In Arcade dashboard, create an **MCP gateway** -- name it, select your tools (Gmail, Slack, Google Calendar, Google Docs, etc.)
3. Copy the MCP configuration snippet
4. In Antigravity, open **Agent Manager** (mission control), go to **Settings > MCP Servers > Manage MCP Servers**
5. Paste the Arcade MCP snippet into the **raw config JSON**
6. The single endpoint now **bundles all tools** your sub-agents need, accessible through mission control
7. OAuth is handled automatically -- edit the gateway anytime to add more tools

**Demo: AI Ops Dashboard**

- Built a **modern web app called "AI Ops Dashboard"** from a single prompt in mission control
- The dashboard logs metrics, provides KPIs, and gives environment context
- Mission control **deployed separate sub-agents**: one for the **front end**, another for the **back end** (to support Arcade integrations)
- The front end was generated and looked "absolutely amazing" -- clean AI ops dashboard with tool activity management
- Dashboard features: connected tools panel, activity logs, results (event scheduled, email sent, message posted)

**Sub-Agent Architecture**

- Mission control can **spin up multiple workspaces** within a single Antigravity project
- Each workspace can have a **dedicated sub-agent** focused on a specific part (e.g., one tool integration, back-end logic, front-end UI)
- Sub-agents **communicate efficiently** across workspaces
- Instead of one agent doing everything, you get a **team of specialized agents**, each executing their part using real tools
- You can have Antigravity **plan first**, then the execution agents follow through -- or just have it code out immediately

**Real-World Tool Integration (Gmail, Slack, Docs, Calendar)**

- **Gmail**: drafted and sent an onboarding email for a new AI designer -- visible in Gmail drafts; consumed 1 tool execution in Arcade
- **Slack**: sent a message to the World of AI channel announcing the new AI employee onboarding -- message appeared in Slack DMs
- **Google Docs**: created an "AI Designer Onboarding Guide" document -- full onboarding doc generated and accessible in Google Docs
- **Google Calendar**: scheduling capability integrated into the dashboard
- Each tool requires **OAuth authorization** the first time -- click "Authorize" in the dashboard and sign in
- **Playground** feature in Arcade lets you test individual tools before deploying them through your agents
- All tool executions are tracked in Arcade's **audit log**

*Quotable Quotes:*

> "Antigravity's agent system stops at planning. They don't actually have a secure, scalable way to take action in the real world." [00:54]

> "When you plug Antigravity's mission control into Arcade's MCP runtime, your agents stop becoming planners because they actually become operators." [02:15]

> "Instead of just one agent doing everything within Antigravity, you can get a team of specialized agents, each executing their part using real tools." [13:15]

---

## What This Means for Your Work

**How This Can Improve Your Claude Skills and Workflows**

- **Your AI Employees architecture already solves this problem differently.** Your 6 AI Employees (legislative research, legal assistant, document production, development, knowledge management, content marketing) each compose existing Claude Code skills into autonomous workflows -- no mission control dashboard needed. The video validates that the "plan + execute via sub-agents" pattern works, but your implementation uses skill composition and memory files instead of a separate execution runtime.

- **Arcade.dev's MCP approach vs. your existing MCP setup.** You already use MCP servers (Figma, Notion, Chrome, Pencil) integrated directly into Claude Code. Arcade bundles 7,500+ tools behind a single MCP gateway with managed OAuth -- useful if you needed Gmail/Slack/Calendar integration without building OAuth flows yourself. For your 9 software projects, the direct MCP approach gives you more control; Arcade would add value specifically for **cross-tool automation** (e.g., having your knowledge management employee auto-send Slack notifications after completing transcriptions).

- **The sub-agent + MCP execution pattern maps directly to Claude Code's Agent tool.** What Antigravity calls "mission control deploying sub-agents" is what you do with Claude Code's parallel agents and the Agent tool. Your 129 skills are the equivalent of Antigravity's "specialized agent modules." The key difference: Antigravity uses a visual dashboard for orchestration; you use CLAUDE.md instructions and skill composition. Your approach is more portable and version-controlled.

- **The "planners vs. operators" distinction is worth noting.** The video's core insight -- that AI agents are good at planning but weak at execution across real-world tools -- is a real gap. Your Dispatch + Remote Control + Channels architecture addresses this by keeping Claude Code as the execution layer and using phone/Telegram/iMessage as the instruction layer. Arcade addresses it by being the execution middleware between any IDE and external services.

- **Practical application for MoroTech and BARMM work.** If you eventually need your AI employees to interact with government email systems, schedule meetings on shared calendars, or post to official Slack/Teams channels, an MCP runtime like Arcade could bridge that gap without custom API integration work. Worth bookmarking for when the AI Employees move from personal productivity to organizational deployment.

---

## Transcript

[00:00] We've all gotten a chance to use Antigravity quite a bit by now. And something that people don't realize is that within the IDE, there is a mission control system. This is something that handles background task delegation, lets you architect custom sub-agents with specialized skills, and basically treat them like programmable AI modules. That is honestly a game changer.

[00:19] For example, inside Antigravity's mission control, I asked it to onboard new designers. This simple task got broken down automatically where one sub-agent crawled the company's website to extract fonts, logos, and color palettes. Another one compiled all that into a clean internal walkthrough. And thirdly, that agent drafted and sent that onboarding email in Gmail.

[00:43] And to end, that entire workflow was automated. No copy and pasting, no tab juggling, no manual handoffs. The only issue, Antigravity's agent system stops at planning. They don't actually have a secure, scalable way to take action in the real world. They can plan, but acting across tools like GitHub, Slack, Docs, email, or web is just usually brittle, hacked together, or straight up unsafe.

[01:12] But there is a new way to use Antigravity's mission control. The idea of a full team of specialized AI sub-agents that can plug into a real execution layer, a layer that can securely run tools, interact with real services, manage permissions, and act on your behalf.

[01:30] That layer is Arcade.dev, a free MCP runtime, and it's also today's video sponsor. It's the execution backbone that lets these agents operate in the real world. With Arcade, our Antigravity sub-agents can be supercharged because they can now actually execute tasks across apps securely on behalf of your users or yourself and connect to 7,500 plus tools, whether that's emails, files, calendars, APIs, you name it. These agents don't just chat, they get work done.

[02:02] Essentially, today I'm going to be showcasing how you can turn Antigravity into your full AI engineering team with sub-agents that can practically do anything. But guys, here's where things get crazy. When you plug Antigravity's mission control into Arcade's MCP runtime, your agents are going to stop becoming planners because they're going to actually become operators with this runtime. They can log into tools, take real actions, and complete workflows.

[02:30] For example, the engineering team can create a repo, open an issue, assign it, and push the first commit. Or if it's related to marketing, it can build a doc, fill it out with its research, schedule a launch, and draft the thread. This is the AI execution layer that will be enabled with this combination. Arcade is going to make this possible because it can connect to thousands of AI tools, connect to authentication systems safely, and run structured systems and actions without any sort of hacks. It maintains auditability, and it is going to make sure that everything is super safe and secure.

[03:05] Together, you're going to get that full AI operation layer, a programmable AI workforce running securely across your stack. If you want the best AI tools, workflows, and drops before everyone else, join my free newsletter with the link in the description below, which is completely free.

[03:22] To get started, you're obviously going to need Antigravity installed onto your computer, which you can do with whatever operating system you have. You're also going to need to make sure you have an Arcade account, which you can get started completely for free. The hobby plan is going to get you a lot of usage. But if you want the $25 plan a month, you get a lot more API calls with the MCPs and that way you also have more usage limits.

[03:48] After creating an account with Arcade, you're going to be then sent over to the main dashboard where you're going to be able to manage your agent secure structured access to real tools like the APIs, the MCPs, as well as your workflows.

[04:00] Within the tool catalog, this is where you have all the real-world actions that are going to be accessible to your AI agent APIs and tools my agent can actually use like Gmail for example and it's super easy to set up with different capabilities.

[04:15] You then have the MCP gateways and essentially this is where it acts as the bridge between my AI agent within Antigravity's mission control as well as external systems and standardizes them and secures them. And this way it is going to allow you to easily interact with Arcade's platform.

[04:30] You also have a server. This will let you host and expose tools in a controlled environment the agent can call upon which is super important. Lastly, you have your secrets which you can manage for each and individual tool or MCP as well as your OAuth providers and you can obviously manage your connections, your connected apps, user verification, as well as the audit log which will showcase everything happening in the behind.

[05:02] Then make sure you have Antigravity opened up and what you want to do is click on open Agent Manager. This will open up the mission control center and this is where you can easily direct your AI agents to build anything.

[05:17] And what we're going to be doing in today's video is building an AI ops dashboard that turns a single prompt into a real action across tools like Docs, Gmail, Calendar, and Slack using Antigravity as well as Arcade. Because Antigravity is going to decide what should happen and have it code out everything and then have Arcade actually do all the work by powering the agents to interact with these different real world tools.

[05:45] So, we're actually going to need to go back into Arcade first, and we're going to need to create an MCP gateway to have it connected to our mission control. Otherwise, it's not going to be able to power the team of sub-agents to do the task that it needs.

[06:00] So, this is where you can give it a name. I am personally going to name it Antigravity Ops Dashboard as that is the app that I'm going to be creating. You can also select your tools directly, which I would do right away. In terms of what you want your sub-agents to be using, as well as what you want within your app.

[06:15] I'm particularly going to be using Gmail. I also want to have my agents use Slack as well as Google Calendar and as well as Google Docs. Once I have selected these, what I can do is select all of these 48 tools. You can even individually select what tools you want to use if you do not want to clutter all the tools for your agent. But I'm going to be using all of them and then creating the MCP gateway.

[06:42] Once that is done, I can then copy this snippet into my settings. And you can easily have it integrated with whatever agent that you want to use like Claude Desktop, VS Code, Windsurf, or even Gemini CLI.

[06:55] What I would recommend you do is open up another Antigravity session. You want to then click on additional settings, MCP servers. Then click on manage MCP servers. And within the raw config, you want to then paste in this MCP snippet directly within the Antigravity MCP JSON file.

[07:15] And once you have done this, you can easily have it now connected to your mission control. This is where the single endpoint that bundles all the tools my agent needs is going to be accessible now through the mission control that will deploy sub-agents to use all these tools. And remember, OAuth is handled automatically. No API keys in code and no scraping.

[07:35] And remember guys, if you want to edit your MCP gateway, you can actually go ahead and add in additional tools if needed. So now that our sub-agents are powered by Arcade in terms of using real world tools and having it supercharged, now what we can do is deploy our full-on engineering team.

[07:55] This is where within the mission control you can provide as much context as you need. And in this case, we're building a modern web app called AI Ops Dashboard that has ability to log different sorts of metrics, help people in terms of providing KPIs and essentially it's a dashboard that will get you the context of your environment.

[08:15] Now, you can either have it planned out first so that the execution agents can follow through with the plan or you can easily just have it now coded out. And this is essentially where I am requesting it to use our Arcade MCP so that it is able to use all of these different tools like the Google Docs tool that we had integrated, Gmail to send emails directly from our application as well as Slack.

[08:42] After sending in the request, it is already going to start working on your front-end task of building out the AI Ops Dashboard which you can see that it is doing right now. And it is going to make sure that it follows through with our specification.

[08:55] What I love about the mission control is that it has the ability to deploy sub-agents to tackle multiple tasks like one focusing on creating the front end and the second one creating the back end which you see right now where it's focusing on building the backend architecture so it supports the Arcade integrations.

[09:13] And the beauty of the mission control is that you have the ability to spin up multiple workspaces. Meaning within this Antigravity workspace that I'm working on building this agent ops dashboard, you can create a new conversation and you can request this sub-agent to focus on, I don't know, maybe particularly developing out one of the tools, a part of your app, or building out the back end. And it is going to be able to efficiently communicate with multiple sub-agents.

[09:42] So you can see all the tools have been enabled with the sub-agent so that it could interact with Google Docs for example or my calendar, for something like sending an email. All of these tools have been implemented within our app and the app has actually been coded out as well which we can access off of our localhost.

[10:00] And this is essentially the app that it had created which looks absolutely amazing guys. The front end actually looks really incredible for an AI Ops Dashboard. And this is where you have the ability to manage your activity of different tools like onboarding a new designer for example. You have the connected tools on the left that have been connected to Arcade's catalog. You also have the different results like the event scheduled, the email sent as well as the message posted.

[10:28] And you'll notice that right now I don't have any of my APIs connected. And this is why you will see that within the results there is an error when I'm creating Google Docs. It is asking for a lot of these different OAuth from Gmail as well as for Slack.

[10:45] What you can do is click on authorizing it so that it is going to be able to now have it so that I can use these different features. Also, I actually recommend that within the playground you test this out so that you get a better understanding of how all your tools actually function and work with these different models.

[11:00] And you'll see that from that execution of executing onboard a new designer on our Arcade dashboard, it has now incurred one tool execution which you see over here. And that is by drafting up that email because this is one of the features that we had requested within our ops so that it is able to execute a new feature.

[11:20] And from here you can see that within our Gmail we have a new draft written up. Not just that, you can have it actually integrated with Slack as well because this is a tool that we had requested. And now I can simply sign in through this OAuth so that I can actually have our sub-agents interact and delegate task through Slack as well.

[11:45] After connecting Slack, I simply had executed this: send a message to World of AI on Slack that we had onboarded a new AI employee. And this is where it had now incurred this new execution of sending this message via Slack. And you'll see there are more executions.

[12:00] And on Slack, if we are to take a look at our DMs, it is drafting up this message. "Hey World of AI, we recently onboarded an AI designer." Not just that, it has the ability to also create documents for us because that is one of the skills that we had enabled with Arcade and that is going to power our agent to even do something like creating a Google Doc.

[12:22] This might take a bit longer, but it's going to be able to set this up. And this is something that we will see within the new Google Doc that it had created. And just like that, it was able to execute and create this doc for us where it created the AI Designer Onboarding Guide for our new employee that we had instructed through our AI Ops Dashboard.

[12:45] And you're able to see that thanks to our sub-agents being powered by Arcade, they are able to break things down that couldn't actually do anything beforehand with tools through MCPs. Each sub-agent becomes an operator with real capabilities through your applications.

[13:00] This is just one example of me deploying through an app. But you can create scripts, you can create automations that can help you send emails, create documents, schedule meetings, or use many of these other tools that we had previously mentioned. So instead of just one agent doing everything within Antigravity, you can get a team of specialized agents, each executing their part using many of these real tools.

[13:28] And guys, an important feature I want to mention is the playground. This is essentially where you can actually test out these different individual tools that you had selected so that you get a better idea as to how they actually function and how they will actually function through your apps.

[13:45] If you like this video and would love to support the channel, you can consider donating to my channel through the Super Thanks option below. Or you can consider joining our private Discord where you can access multiple subscriptions to different AI tools for free on a monthly basis, plus daily AI news and exclusive content, plus a lot more.

[14:04] But that's basically it, guys, for today's video as to how you can set up Arcade to supercharge your Antigravity agents to deploy a full team of AI engineers to do practically almost anything. This is an ideal setup that I would highly recommend. And I'm not just saying that because I'm sponsored by them. I am totally telling you guys this is an ideal setup that can help you in so many ways.

[14:28] So, use the links in the description below so that you can easily get started with Arcade and Antigravity. But with that thought guys, make sure you guys subscribe to the second channel, join the newsletter, join our Discord, follow me on Twitter. Lastly, make sure you guys subscribe, turn on notification bell, like this video, and please take a look at our previous videos so that you can stay up to date with the latest AI news. But with that thought, guys, have an amazing day, spread positivity, and I'll see you guys fairly shortly.
