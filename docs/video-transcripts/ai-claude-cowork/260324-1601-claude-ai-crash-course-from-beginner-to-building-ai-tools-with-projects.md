# Claude AI Crash Course | From Beginner to Building AI Tools (with Projects)

**Channel**: Mayank Aggarwal
**Duration**: 213:08
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=P1yJcMV8o90
**Transcribed**: 2026-03-24 16:01

---

## Organized Notes

**Claude's Three-Layer Architecture**

- Claude provides **three distinct products**: Claude Chat (AI), Claude Code (engineering), and Claude Cowork (desktop operator)
- **Claude Chat** is the main brain — the foundation on which Code and Cowork are built
- **Claude Code** functions as the engineering layer for developers
- **Claude Cowork** acts as the operator layer for day-to-day task automation with skills, plugins, and connectors
- The presenter is **Mayank Aggarwal**, a tech educator and AI consultant based in Bangalore

**Claude vs. ChatGPT**

- Claude excels at **complex reasoning**, handling **long context**, and producing **structured outputs**
- ChatGPT delivers **fast responses**, has a **large ecosystem**, and handles **everyday tasks** well
- For tasks requiring deep analysis, long documents, or step-by-step research, Claude consistently outperforms ChatGPT
- Claude inherently asks **clarifying questions** before answering, while ChatGPT tends to generate responses immediately
- Both are valuable — the choice depends on the task's complexity and context requirements

**Claude Models: Speed vs. Intelligence**

- **Haiku** — fastest, lowest cost, best for simple quick tasks (like "just waking up")
- **Sonnet** — balanced everyday model, default choice for most work (like "normal daily work")
- **Opus** — most capable for ambitious work, deep reasoning, and complex research (like "exam mode"); consumes usage limits faster
- **Extended Thinking** mode makes Claude create a step-by-step reasoning plan before answering, significantly improving output quality for complex tasks
- Without Extended Thinking, Claude answers from memory; with it, Claude researches, structures, and reasons before responding
- For **strategy planning, AI agents, and long document analysis**, Opus performs significantly better than Sonnet

**Effective Prompting**

- The biggest mistake is expecting AI to understand vague instructions — **clarity unlocks Claude's real power**
- Effective prompts follow a **four-part structure**: Goal, Context, Action, and Output format (GCAO)
- Providing **personal context** (health conditions, budget, preferences) dramatically improves response quality
- Think of prompting as **briefing a task to a smart assistant**, not asking a question to a search engine
- **Iterative refinement** is essential — seldom will the first response be perfect; keep refining with follow-up instructions
- Use **markdown formatting** (headings, bold, bullet points) in prompts to help Claude parse structure
- A powerful personal preferences hack: add instructions like "For any task, ask me about the goal, context, action, and output format" to Claude's settings so it always asks clarifying questions

*Quotable Quotes:*

> "The better overall instructions we give, the better will be the answer. It is just like an assistant — the more you tell how a particular work has to be done, the better of course will that work be done." [32:02]

> "Think of prompting not actually asking a question. Don't say that you're asking something to Claude but as briefing a task or as normally a solution to the problem." [41:22]

**Working with Documents and Files**

- Claude becomes **dramatically more useful** when given real documents (PDFs, Excel, images) to work with
- It can analyze a **50-page report** and generate presentation-ready infographics, charts, and visual summaries
- Claude handles **non-structured data** (images, thumbnails) equally well — analyzing composition, text, branding, and suggesting improvements
- **Multiple tasks can run in parallel** — start a new chat while another analysis is still running
- The distinction between **AI usage and powerful AI usage** is giving AI real information to work with, not just asking questions

**Artifacts: Building Interactive Tools**

- Artifacts are **interactive mini-applications** Claude generates inside the chat — calculators, dashboards, planners, websites
- Artifacts can be **published** with a shareable link, making them accessible to anyone
- Claude can build a **complete portfolio website** from a LinkedIn profile PDF in minutes, including navigation, animations, gradient hero sections, and responsive design
- Iterative refinement works on artifacts too — add dark mode, pie charts, animations through follow-up prompts
- Artifacts include full **downloadable code** that can be self-hosted
- The **embed link** feature allows embedding artifacts into existing websites

**Projects: Organizing AI Work**

- Projects solve the problem of **repeating context** in every new chat — define instructions and files once, reuse across all chats in that project
- **Instruction hierarchy** (critical concept): Claude-level settings (broadest) > Project instructions (project-specific) > Chat instructions (narrowest)
- Upload files to projects (brand guidelines, reference docs) and all chats within that project automatically reference them
- Projects function like **categorized folders** for different facets of work — clients, content creation, research, business
- The more chats a project accumulates, the better Claude's responses become over time
- Adding a chat to a project retroactively is possible through the chat menu

**Skills: Training Claude for Specialized Tasks**

- A skill is **Claude's brain + instructions + structure = specialized capability** — like training an intern with a detailed user manual
- Skills are stored as **skills.md files** — markdown instruction documents that tell Claude how to perform specific tasks
- Three ways to create skills: **Create with Claude** (AI-guided), **Write skill instructions** (manual), **Upload a skill file** (from marketplace or custom)
- Skills are stored as a **library** — Claude checks if a relevant skill exists before performing a task, just like a human checking their expertise
- **Skills marketplace** sources: Anthropic's official repository, GitHub community repos (awesome-claude-skills), and the agent-scale marketplace
- When creating skills, invest time in **detailed instructions** — the quality of the skill file directly determines the quality of consistent output
- Skills turn Claude from a **conversational assistant into a specialized system** — this capability is what caused disruption in IT consulting industries
- Security warning: **always review downloaded skills** before installing — verify they don't access files or send data externally

*Quotable Quotes:*

> "Don't confuse it like others are explaining it in a very difficult manner for you. It is just: if I have a brain, now you are just saying 'this is the user manual' — and if you are asked to do something around this, use this skill." [1:44:07]

> "Skills turn Claude from a conversational assistant into a specialized system. And that is where these things are taking overall advantage." [1:55:08]

**Connectors and Extensions**

- **Connectors** link Claude to web applications (Gmail, Google Calendar, Notion, Slack) — available in both web and desktop versions
- **Extensions** link Claude Desktop to local machine applications (Apple Notes, Chrome, file system, PDF tools) — desktop app only
- Always **review permissions carefully** — Gmail connector can view messages but cannot send emails by default
- To reduce token usage, **disable connectors** that aren't needed for the current task — having 10+ active connectors wastes tokens
- Claude can create **calendar events**, read emails, search Gmail, and list drafts through connectors
- The **Desktop Commander** extension gives Claude terminal access and local file system control

**MCP (Model Context Protocol)**

- MCP is the **underlying protocol** that powers all connectors and extensions — it defines how Claude communicates with external tools
- MCP servers come in two types: **remote** (running on the internet, like Notion) and **local** (running on your machine, like Firebase)
- You can add **custom MCP servers** through Claude's settings — provide a name and server URL for remote servers
- **Creating custom MCP servers** is possible using tools like n8n — build a workflow with an MCP server trigger, define tools (e.g., send email), and connect the server URL to Claude
- This approach solved the Gmail limitation: creating a custom MCP server with n8n that includes a "send email" tool, then connecting it to Claude as a custom connector
- The custom MCP server approach enables Claude to **perform actions** that default connectors don't support

*Quotable Quotes:*

> "Under the hood, when your Claude is getting connected to these tools, it is using something known as MCP. You can just think of MCP as a collection of tools." [2:45:12]

**Portfolio Website Project**

- Created a **complete professional portfolio website** from a LinkedIn PDF export using Claude
- The workflow: download LinkedIn profile as PDF > use ChatGPT to generate an optimized prompt > paste into Claude with the PDF
- Claude generates responsive HTML with **hero section, skills grid, experience timeline, projects showcase, and contact form**
- Iterative improvements: added navigation bar, modern gradients, icons, animations through follow-up prompts
- Attempted Google Sheets integration for **lead capture** via Google Apps Script webhook — requires deployment outside the artifact environment
- Artifacts are suitable for **prototyping and showcasing** but full production applications need proper deployment (covered in Claude Code)

**Professional Dashboard Project**

- Built a **Kanban-style productivity dashboard** with task management, priority tracking, and calendar integration
- Claude connected to Google Calendar via connectors to pull real events into the dashboard
- Added **drag-and-drop functionality** for Kanban board task management
- Dashboard included: weekly work overview, priority task panel, schedule view with IST timezone
- Limitations surfaced: artifacts cannot directly integrate with external databases or APIs — those require Claude Code for proper engineering

**Key Takeaways**

- Claude's three-layer architecture (Chat, Code, Cowork) serves different user types and use cases
- The **instruction hierarchy** (Claude-level > Project > Chat) is foundational for effective Claude usage
- **Skills are not magic** — they are structured instruction documents that leverage Claude's strong reasoning
- The **connector + MCP ecosystem** extends Claude from a chatbot to an agentic system integrated with real tools
- **Artifacts** bridge the gap between AI responses and usable tools, but production applications require Claude Code
- The combined power of skills + connectors + projects + artifacts makes Claude a **comprehensive work system**, not just a chatbot

*Quotable Quotes:*

> "At the end of the day, all scientists, all people are trying to do — even the smartest ones — are just trying to mimic how we normally work. I have a skill, I use that skill, I have developed that skill. Let me add that thing to Claude as well." [2:13:30]

> "Gone are the days where you have to do a very basic level of prompt engineering. I think now this is the way of moving forward." [1:23:49]

> "If you understand that how you want your website to work as a product builder or product manager as well, now that is more than enough." [1:28:27]

---

## What This Means for Your Work

This video is a beginner-level walkthrough — you've already implemented virtually everything Aggarwal covers, and at a significantly deeper level. Your 129-skill Claude Code setup, Obsidian vault memory, NotebookLM pipeline, and frontend-first development workflow represent the expert-tier architecture that this tutorial gestures toward as "what's possible." But the video does surface a few operational patterns worth evaluating against your current setup.

**The instruction hierarchy concept** (Claude-level > Project > Chat) maps directly to how your CLAUDE.md files already work: global `~/.claude/CLAUDE.md` > project-level `CLAUDE.md` > skill-level instructions. Aggarwal's explanation validates your architecture. The one addition worth considering: his technique of putting a "always ask about goal, context, action, output" instruction at the Claude-level settings could benefit OOBC team members who use Claude.ai (not Code) for policy drafts and communications — it forces Claude to gather context before generating, reducing the AI slop that government stakeholders reject immediately.

**The n8n custom MCP server approach** for extending connector capabilities (e.g., adding Gmail send) is a low-code bridge that could serve your OOBC use case. If team members need Claude Desktop to send legislative updates, create calendar blocks for BTA sessions, or file documents — n8n workflows could provide those tools without requiring them to use Claude Code CLI. This is particularly relevant for the OBCMS team who handle OBC coordination across multiple regions.

**The "use ChatGPT to generate prompts for Claude" cross-pollination** is a tactic you haven't explicitly systematized. For non-technical OOBC staff, this could be packaged as a simple workflow: describe what you need in ChatGPT → get a structured prompt → paste into Claude project with your files. It's the beginner-accessible version of what your /prompter skill does automatically.

### How This Can Improve Your Claude Skills and Workflows

**Skill improvements:**
- **/training-assistant** — Aggarwal's tutorial structure (concept → demo → live build → troubleshooting) is a validated pedagogical pattern for your SEED Initiative training modules and MoroAcademy courses. The "show the error, don't edit it out" approach for building trust is worth incorporating into training materials for OOBC digital literacy programs.
- **/claude-projects** — The video confirms that Claude.ai Projects use the same instruction hierarchy as CLAUDE.md. Your skill could add a "beginner onboarding" mode that helps non-technical OOBC staff set up their first Claude project with appropriate instructions and reference files.

**New skill opportunities:**
- **n8n-mcp-builder** — A skill for creating custom MCP servers via n8n for non-Code users. Check `~/Vault/Claude-Skills/index.md`: no existing skill covers this. Would allow OOBC team members using Claude Desktop to extend connector capabilities (send emails, create documents, post to internal channels) without touching code. Low priority but addresses the gap between Claude Code power users and Claude Desktop users in your team.

**Workflow changes:**
- The video demonstrates that **Claude.ai artifacts can generate publishable web tools** (calculators, dashboards, trackers). For quick stakeholder demos of e-Bangsamoro features, generating a prototype artifact in Claude.ai and sharing the published link could be faster than spinning up a dev server — especially for presenting to BARMM officials who need to see a concept before approving development resources.
- Consider creating a **Claude.ai project template** for OOBC team members that includes: OOBC brand guidelines, the officials reference file, BOL key provisions, and instructions to always ask clarifying questions. This would give non-Code users a productive starting point without requiring them to build their own skill library.

**Project-specific applications:**
- **e-Bangsamoro** — The portfolio website project pattern (LinkedIn PDF → structured website) could be adapted for generating quick profile pages for BTA MPs from their official bios, useful for the Parliamentary portal.
- **Tarbiyyah-MS** — Artifacts could generate interactive dashboards for madrasah administrators to visualize enrollment and teacher assignment data without needing the full React app deployed.
- **MoroMarket** — The budget planner artifact pattern could be adapted to create quick financial calculators for cooperatives applying through the marketplace — a tool the SEED Initiative teams could use immediately.

---

## Transcript

[00:00] Everyone is talking about clot. It is everywhere from your YouTube to your Instagram. But no one is telling that how can you master clot as complete beginner and everyone is just scratching the surface. That's why in this complete

[00:12] master class in the next 4 hours we will master clot and understand that why AI assistants are becoming essential. Where does clot sits in the full AI ecosystem and what different different products it has. What are the different way of using clot so that we can get the most out of it? How does clude compare with chat GPT

[00:32] and other AI tools? What is the different different types of models present in clot from op sonnet as well as the deep thinking mode? How can we communicate effectively with clot so that we can get the best results and write the bestest of the prompt. How can

[00:47] we work with our everyday documents, PDFs, docu PDF pictures so that we are able to provide claude with the context for our daily work. Then we will understand that how can we generate artifacts and in this we will also try to create our own per particular personal website. Then we will jump on to understand the projects in claude so that we are able to group similar kind of chats and also how they share context. After that we will understand

[01:13] the most important topic which has caused billions of dollar wiped out from the stock market and that is around the clot skills. We will understand skills in depth where we will not only use the skill which are present but we'll also understand what are the different different ways of creating a skill and we'll create multiple of them and use them in the chat. Once we have mastered all this everyone, we will connect our day-to-day chat apps like Google Sheets, Google Gmail via the cloud connectors as well as using MCP. And not only this, we

[01:44] will understand that how exactly it happens behind the back by creating our own MCP server as well. Once we have done all of this everyone, we will be doing two projects, a portfolio website builder as well as making sure that we are able to create a professional dashboard for us. With this you will be mastering claude in no time and even if you are a beginner by the end of this 4hour master class you will be having the complete idea about all claw capabilities. So hi everyone I am Gabal

[02:13] and previously I have explained you about open clock cloud co-work and you like the direct approach which I choose to practically explain these things with that I have created this master class with a lots of effort to make sure that as a beginner or someone who has no idea even about AI can master claude in no time and use it to the fullest. So now let's get started. Hey everyone. So

[02:35] welcome to the most comprehensive Claude AI crash course ever. Now just like I have covered earlier topics on my channel. I will make sure that this claude as well we are covering in a direct and easy to understand manner in a more practical way. Now this is the

[02:50] road map which we are going to follow everyone. So of course we will start with understanding claude and via this I will also make sure that first I can explain you what assistant is how claude connects with chat GPT because I do understand that many of you will be coming to claude now after seeing lots of videos or via Instagram and I want to clear that here that hey how does it compare to chat GBD which I think is an AI which everyone of us have used before. Uh after that we will understand that okay for what clot majorly is helpful. Once we have done that everyone

[03:20] then we will deep dive into clot and for that we will see that how we can understand it interface how its AI works what are the different different models which are inside cloud then what are uh let's say prompting or how you have to talk to claude in a very uh proper manner or very in expert manner so it gives you the best responses out there and then when we see that how in iteration right and that is a very very good power of plot where uh once you iterate over let's say your results you can make them a lot better. Plus, Claude can also ask question based on your query. Once we have done that everyone, then we will move forward and see that how can we now use claude to work on our documents to do a web research to understand our image as well as our writing style and how can we provide custom instructions etc to plot. So

[04:07] those also are going to be way very way very way very helpful. The idea is pretty simple. Uh we will not only be using our AI just to chat. I want to

[04:14] make sure that after understanding claude by this video, you don't have to go anywhere else and you are able to use it in your personal and your professional uh life overall. Once you have done this everyone, then we will start building with claude because it is as I said more than just a chatbot. We will see that okay what are artifacts, how can we create projects and what are the re what is the way of using reusable systems in uh claude. So we will be

[04:37] making sure that proper automations we are building from scratch and those are something which are going to actually make claude a lot useful for you. Once you have done that everyone then we will move forward and see extended thinking skills. So skills are going to be very very important. I have I will be talking

[04:52] in a lot of depth about that. We will be creating our own skills as well and then we will jump to connectors MCP etc. Once we have understood now the claw in so much depth then we will be doing some real AI projects. First will be your

[05:05] portfolio website generator just like I showed you and second will be the professional dashboard as well everyone. So again uh one will help you to uh do your job nicely and other will help you to find a job. So once you have done that then I think you will be at a point where you can build real AI tools with claude starting all the way from prompting to building a proper AI system. So with this road map everyone

[05:27] spend a lot of time in creating this in a very logical and practical manner. We will be mastering cloud once and for all. So with that let's now get started everyone and let's first directly go to Google and see that okay what exactly claude is. Now I've gone and open

[05:42] incognito window. If you will just search for say claude then in this uh don't get this sponsored link or something just see this claude.ai and I will be pasting the link as well and yeah this is actually what claude is.

[05:57] Now you can just continue by basically making sure that you are uh having a Google account or any other account as well. Maybe your company's providing the same as well everyone and it might also ask you for a phone number. It also has a desktop app. So I will come to ways of

[06:12] connecting and using clot. Okay. But for the time being once you have created your account and it's going to be pretty straightforward and pretty sure that most of you might have an account already. This is how you will be seeing

[06:23] the plot um like at its best plot new where we can just start connecting and asking question with plot. So if I send a hi it will make sure that it will reply to me. So a simple very simple message contemplating standby putting up it thinking modes and it will just quickly reply with hi how are you or how can I help you. So yes, this is in a way

[06:47] a simple simple chatbot everyone much like chat GPT which I'm pretty sure all of us have used earlier because I think yeah chat GPT is the go-to AI bot or AI assistant for a long time and now since you're moving from claude it is very very important to understand that okay how the two compares okay so now everyone that we have understood this uh before diving deep into claude I would first like to clean a little bit air around the AI assistant or the AI part of things because again I see that many people are directly jumping to claude using it and showing you but no one is talking that hey what is the mindset shift which you have to make because all is good that hey I am able to use claude I saw that video and I'm able to do this and that but I feel that you should have an mindset shift now if you're learning a technology or an AI which is as strong as cloud so with that everyone uh if we just talk about AI assistant and why they are becoming essential. It is very very important to understand to see the traditional and the new way of doing things and though I'm pretty sure that all of us are using AI in our phones in our toothbrush everywhere around us somehow in water as well maybe in some time uh the main thing I believe is that you have to shift your mindset that how these tools like chat GPD clot they are going to be your AI assistant. So before we were doing all the work manually, lots of documents, emails, uh calendar, ideas, docu uh research, each and everything was manual. It used to take

[08:19] hours. With the help of AI assistant and we have to think of them as AI assistant uh now everyone because in 2026 they are not just simple chatbots. They are able to connect to our tools, our everyday documents. They are able to understand

[08:33] that okay what skills or what work is it which we do and maybe help us to do that better. So you have to see that hey how this thing or technology can be helpful to me. So you just don't have to use it and be happy that hey I know claude and everything like other videos. My idea is

[08:48] that you actually understand that hey this is what I unlock by learning this skill. And yes if you're working with AI it will take generally minutes instead of hours. Uh we already have used chat GPT we are now moving to cloud. Both of

[09:02] us can help us in a similar manner. So with that everyone the thing is clear and uh I think just like calculators change math and Google change search uh AI assistant are now changing the way we work okay and of course each and every professional right they will be having an AI assistant in future so that is why I want that you create your ones or you understand that how to uh work or create ones uh today so with that everyone now let's move forward and let's quickly see what are the three layers which claude has now in my earlier video of claude Claude co-work. So I have also covered claude co-work. Please make sure that

[09:37] you check that out. I have explained about this uh ecosystem as well uh before that claude majorly provides you with three things. First is claude chat or claude AI and that is exactly this particular uh thing right so where you can ask it something much like chat GPT and it will give you back the answers right. So uh we have already seen the

[09:59] sign up process pretty straightforward just go to claude and create your account. As I said Claude also has a desktop app. So claude desktop app. If

[10:09] you will see download cloud everyone then another way you can download it and then run it on your laptop uh or machine. So just to show you uh this is how it looks uh very very similar honestly I don't think there is any def uh any difference. just focus on the chat for the time being okay not co-work or cloud but yes you can just use the same thing and the benefit is that it can connect to more things over your machine as well in this manner okay now this all was clawed uh chat everyone then next is claw code so using the understanding using the complete understanding our whole idea becomes that uh now how can we also make some technical things with it so that is where claw code comes in and claude co though I have covered earlier that helped us in doing day-to-day task by using that intelligence it is having skills plugins etc. So we'll highly

[11:02] again suggest that you uh just go and see that video because that will be very helpful. For today our whole focus is going to be on this claude AI which is the main brain. Claude code you can think of engineer and claude co-work like an operator. Now this distinction

[11:17] is very very important because I do understand that many of you will be as I said learning claude uh just because of some videos on Instagram and you might get confused in these things. Okay. So in the same application if I go on code and if I then ask it to provide me something it will try to give me in a coding manner with Python or any other language code and cowwork is basically saying that hey I am a brain plus I have some functionalities which you can directly use. I can work inside your

[11:43] machine in a folder I have some skills etc. But let's come back to chat because on top of that it is what all of these things are based. So with this thing clear theore everyone now let's move forward and try to see that how could you use claude. So on the surface though

[12:01] it is a overall chatbot only like it is helping you to answer questions but the best part is that you can ask it to maybe do some research etc for you. It is having very very high thinking mode. It is very good for complex kind of work as well. Then everyone you can also ask

[12:18] it to build tools something which we will be doing. So it can actually build uh very very good and advanced tool for you be it calculator, calendar or end toend website right. So we will be building your personal portfolio website everyone. Then uh it can be your

[12:33] thinking partner as well. It can help you to brainstorm ideas do web search properly create a step-by-step scenario so as to how to work on something and though most people think that hey uh claude is just like a chatbot it is not. It is actually the wrong way of thinker thinking about it. Claude can act in

[12:51] three different things depending on how we use it and these are the things it can act as a research assistant as a thinking partner and even as a tool builder. So that is the whole case everyone that how majorly claude uh works right. So if you will go on this in a bit once we understand each and everything in here we will see that okay how all of these things get uh opened okay for us to use. So that's the whole

[13:14] idea and we can just quickly check it out like let's say just I have an example of this thing I am looking for laptop for video editing budget requirement compare three good option explain the pros and con of each so it will just try everyone that it is able to think in a very complex manner see it is thinking it is searching the web so it is taking all the steps it is asking that hey I will notify you once the work is done and then it is giving you the reply so now again it It is moving in a step-by-step manner. See, it has gone through 30 pages. Again, it is searching so that it can get more idea and that is what I said like it is not going to just uh reply to you that hey these are the laptops which I remember or these are what I've trained on. No, it moves in a

[13:58] very sequential manner. So that is the biggest benefit because if you think the way now claude has been created if it help you to do your job as well in a similar manner then how nicely it can do that particular thing right and that is the reason why claude has affected so many IT industries talk and everything because of this thinking manner because of doing things the way we do it so this exactly is the something which I will follow I will make sure that hey I'm searching the internet then I'm for forming the complete nodes and then I'm telling everything and see it is weighing in everything. It is building the contenders and now it has come up with a proper answer in a very very nice manner. So this is something which I

[14:38] like about claude a lot as well that uh if I ask the same question just I will ask the same question to chat GPT and you will see the difference right that if I ask the same question here okay now uh chat GPT will try to do something of this right and at the end of the day it is searching the web and everything but the way claude normally goes about some complex task is a lot better. So see now it is giving you this thing and everything in a very very similar manner but claude it has searched way more well it has given you these things with a proper very nice manner which you can directly use in a presentation plus I have found that for a complex task claude normally is a little better than chat GPD as of now I'm not saying and I'm not doing any fear monging that hey if you use chat GPD just close it and come to clude no the idea is to understand that where cloud shines and why it is getting popular and that is the reason because now since many of us are using chat GP right uh earlier we might be using it on Gemini or something it is very important to understand that how chat GPT and claude or rather any other AI compares if I talk about chat GP it gives fast fast responses very versatile it has a large ecosystem as well and it is great for everyday task but when we come to claude everyone though both are AI assistant okay so we have understood about AI assistants as it is having a very very strong reasoning. It handle long context really really well. So if you have a very very

[16:06] long text normally claude will work a lot better on that. Then of course it is great for analysis and it can provide way better structured outputs. So the idea is again that if you have a complex task if you have some task which you feel that hey uh lots of context is there I have lots of files then maybe you will see towards moving towards uh clot. Okay. So with that everyone now

[16:27] that we have seen the demo as well. Uh one thing more to understand that if I show you if we just go on claude pricing so you will see that claude has different tiers of pricing. Now you can follow this tutorial easily while being on the free plan, right? But I will

[16:45] highly suggest that if you are actually uh interested, you can check out the pro plan as well because the value which you get on the pro plan that is way way way more than what you are paying for. Uh I am currently on the pro plan. So you can try the same out. Each and everything

[17:01] which I'm doing you can easily do on the free plan. you just might get or even I will get uh the usage issue which I will show you as well but I think that should not be a problem. We can easily just wait for some time or start a new chat and just uh like work with cloud again.

[17:17] So these are the plans everyone I will highly suggest not to unnecessarily buy it. If you actually want to get your skin in the game though I will suggest that start with the pro plan not with the max plan. uh pro is more than enough for way way way more than work. But yes

[17:30] uh in free pan you might get uh the limits notification a little bit more constantly because it is using a lots of token it is using that lots of thinking. So compared to chat gypty or other gemini other AI tools you will be seeing that hey uh the free plan it gives you that that hey token usage is exceeded please come after some time a lot something which I faced so I thought of sharing the same with you all as well so now everyone let's go back and start a new chat like it has done a very good research for us I guess yeah so this is something which you can uh see this is something which you can actually then use as well I think yeah we can download the file as well we can save it as artifact something which we will discuss about let's open a new blank chat uh chat and I'm pretty sure that now uh the understanding with chat GP and claude is also clear now I don't want that you directly jump onto claw without any idea and you do that without without any purpose as well all both are good but for complex thing which now we are moving towards with the claw is a lot way lot better so that is the whole idea so great everyone now let's move forward and since you have understood little bit about claw like how it compares what exactly it is and you have a very very good idea that okay how can you access it and the things which you can use it for. Let's now try to understand it uh full interface. So you'll have a full

[18:52] idea that hey where exactly is what uh now if you will see everyone uh this is again the chatbot uh sorry the chat window where you will be having or typing your message. Now as a very good practice you can actually kind of just uh say your message as well. So on your machine be it Windows, Mac or Linux there will be a button. So I will just

[19:11] say hey how hello how are you let me just try it out. Yeah hey how are you hello hi. So a quick way of uh basically writing your prompt or writing your message in here. Now if you will click

[19:25] on this everyone you will see different different models. Now if you're on the free plan some of them might be long but normally but normally I also use the set 4.6. Now

[19:37] there is haiku, there is opus and there is extended thinking as well. So I will talk about each and every of these things. There are some previous models as well like 4.53 and 4 uh sonnet 4.5.

[19:50] Here is where you can just use the voice mode to just chat with it. So again it will be replying you with a voice. You will be kind of saying the same thing with a voice. Each and everything will

[20:00] be in a similar manner. If you will focus on this plus uh everyone then in this you can actually add your files or photos. So if you want to just attach anything either you can drag and drop it or you can just make sure that you are like choosing this and then going to the particular file. Then of course there is

[20:18] a taking a screenshot thing everyone. So you can take a screenshot quickly. It will ask for some permission. Then there

[20:24] is add to project. Now I have also created multiple projects which I can add this particular chat to. uh we will be discussing about projects in a bit.

[20:31] Uh right now it is not very important. Then you have add from Google drive. So it can just make sure that it goes for different different things in your Google drive as well. After that GitHub

[20:41] then there is a research option everyone. So if you want to make sure that hey claude before finalizing or giving you the answer it does a very very in-depth research like the research assistant then you can select this research thing. Web search as the name suggests gives is the flexibility to search the web. If you take this away

[21:00] then it will not be searching the web and it will give you the answer based on how it has been trained on. Then of course like I will suggest always to keep this web search open because it is not like it always searches the web smartly it tries to see if it wants to go to the web or not. Then everyone there's a style. So normal, learning,

[21:19] concise, explanatory, formal, different different styles in which uh claude basically gives an answer for 80% of the use case normal will work. I sometime use concise as well and the idea is pretty simple. Uh many times claude like just go haywire and it tries to just give you lots of long response which is not useful and I I feel it like a AI slop. Then there are connectors everyone

[21:44] which we will also talk about. Now in connectors you can connect to different different applications. Now this gets lot stronger in your desktop app as well and we will be mastering them as well.

[21:55] Okay. So this is each and everything in the major overall uh interface everyone. You will see the incognito one here as well. So if you will see use this

[22:04] incognito it will not be accessing any of the things this chat will uh not be saved in the h in the history or to train uh their future models. Okay. So if there is anything which is very personal which you want that hey uh this is something which even cla should not remember where this is where you use the incognito mode or maybe I normally use incognito mode for one of things. So if

[22:27] I just want to know that hey this is something which I don't want it shows up in my chat or it keeps up in the history that is where I will be using incognito mode. Now once you open this sidebar everyone this is where you will see the option to search. So I can just click on search and say laptop and see it is able to get my previous chat. It is able to get uh like others

[22:48] chat as well past year. So I have been using claude of course for a long time. Then everyone there is customize. So you

[22:55] can customize claude based on your use case. So this is where skills and connectors come into picture. So we will be discussing them also in some time.

[23:04] Then this is where all your chats live. So all your previous chat just like how we have sent uh the laptop chat and the simple hi chat that is where everything is happening. Then everyone this is where we can create projects. So I am

[23:17] also having lots of projects. As you can see the idea is pretty simple. Uh like to make sure that different different chats uh I can just click new and although we will be covering it in depth you can create a project you can make sure that you are telling that hey this is all the things related to my work all the files will be kept in a project.

[23:35] That is majorly the idea with projects. Then is something known as artifacts. So artifacts are directly mini applications which claude can uh build out of the box. So again I think I have not built

[23:47] any artifact. Yeah. So in this account I guess I am not. Yeah. Okay. Okay. So it

[23:51] is taking the research and everything also as artifact everyone. So again I have built these artifact. We will be seeing that how can we build artifacts using claude. Then there is claude code.

[24:03] So if you will go here claude code will open up. Now again it is saying that hey either install me in the terminal or install me in VS code or just uh start cloud code web. I will be showcasing the same in a very very in-depth video similar manner. So let me close this for

[24:20] the time being. And then I guess there are all your chats. You can make sure that you uh just click here and star your chat. That is why uh how it will

[24:29] show up in this uh starred thing. Then what you can also do everyone is you can rename your chat, you can add to a project and you can delete the chat as well. So pretty simple approach just like how we handle it in WhatsApp or other places. You can start a contact,

[24:46] you can uh rename the contact, you can add the contact to some group which is there in WhatsApp or you can read on the chat. So that is the whole idea everyone. Now if you will go on this particular thing, you will just get to understand the language. I think you can

[25:00] upgrade the plan, get apps and extension, you can gift plot to someone, you can log out and in here is where all the settings are everyone. So let's quickly go to the settings as well. So again uh general like what is your name?

[25:13] What should Claude call you? If you have any personal preferences as well that hey uh make sure that you always give answer in a professional manner. So across all the chats this particular personal preferences will be taken care of. So this is a very very easy way to

[25:28] uh just personalize your clot. You can ask that hey don't unnecessary assume something. Make sure that you clarify each and everything. That is a very very

[25:36] good way. or say that hey don't uh like let's say always say yes to whatever I'm suggesting please make sure that you have a condescending and a proper research kind of a thing where you give me the best answers rather than going what I suggest something which I have seen that makes AI work a lot better then all the notification everyone you can make it dark light I think all things work different chat fonts the voice which you will be hearing so these are all the things here then there is your account privacy billing uh this usage is pretty important If you will go on usage everyone you will see that okay what is the current session so right now I have used this 6%. Okay, weekly limits. So unfortunately and no one

[26:18] normally covers it but claude also has a weekly limit. So it will be resetting in 3 hours and I have used around half of that. Okay. And has just updated a

[26:25] minute ago then you can upload more credits so that in worst case if this thing gets done you have more credits which claude can take care of or sorry which claude can use to give you the answer. Right? So that is the whole case everyone in the capabilities again search and reference chat generate memory for chat history few more capabilities we can have we should rather have this artifacts open everyone okay this is very very important because we will be using artifacts in future and all the different different parts are kind of mentioned here and then we have the connectors so I have connected different different applications we will be discussing them in depth but since it is part of UI I think we should all uh just master it and then last cloud code So how you can have the cloud code what are the different different instances I use cloud code directly on my machine.

[27:13] So that is how it is suggesting you to use it. So with that let's now go to the new chat everyone and pretty sure that now all the things in the interface is clear. I have made sure to explain each and everything in depth because as a newcomer or even as a experienced person who is using claude I see so many of you are not actually uh have not actually seen the full thing in depth. So that is

[27:36] where I thought that okay covering it is very very important. I normally always go to usage to see that okay how much usage is left because claude is a little notorious with that and yes I think once you now have a full idea that where everything is in future it will be very very important because we will be covering everything in here. Okay.

[27:54] So now everyone that the whole interface of claude is perfectly clear. Let's now try to actually understand a little bit on its different different models as well. Okay. So you will see that Claude

[28:04] uh basically says that hey I have Opus, Sonnet or Haiku and as a newcomer it might get confusing that hey why are you giving us this option and everything but yeah they they these models have some usage if you will see uh Opus most capable for ambitious work. So this is where you want it to get into the work do some research each and everything. Sonet most efficient for everyday task.

[28:25] Haiku faster for quick answers. Now there is extended thinking as well everyone which as the name suggest it is going to think in an extended manner before giving you the answer and then there are more models basically the previous iterations or previous one of them right now uh I have created a very good graphic for this as well so if you will see when we talk about claude models everyone the speed versus intelligence haiku is very good for the small smaller task it is very fast it is good for simple task it is very low cost as well okay so that is the whole idea like if you use haiku in here just as an example then you will be able to use plot for a longer time okay so just think of it like let's say your brain it is having three modes one mode is when you are in exam that can be opus where you are having the maximum efficiency and everything then one can be when you just woke up uh sorry woke up so that is haiku and sonnet is like normally when you do day-to-day work where you are doing pretty good every time so that is how you can think about this Now why this becomes important is because uh the mode which you select or the model which you select that will have an effect on what answer you get. Okay. So with that

[29:36] if you will see this is solid everyone balanced everyday work reasoning default model. So normally you will be using solid only be it free plan or the pay uh paid plan and opus again powerful complex task deep reasoning it uh of course uh just churn up a lot more token. So if you used opus you will get the usage exceeded error or like the notification a lot earlier. Now extended

[29:58] thinking everyone I have also shown here. So let me just show the extended thinking. Yeah. So if we talk about the

[30:03] claw reasoning mode uh speed versus the deep thinking everyone the idea is very simple. Think of uh normal mode where you are not selected extended thinking like how when you talk to someone he's just giving you the answer without any thinking. Right? So he's just suggesting

[30:19] you that hey what I think and everything but extended thinking is different in a standard response where there is prompt quick prediction is tries to give you the answer without any extended thinking comes up with what should be the next word or token in extended thinking it make sure that it is creating a proper stepby-step manner okay so it is saying that hey this is the work which I have to do let me create the steps let me think upon the task and then let me uh basically answer. So just like how you ask someone a question uh first he's just answering without let's say thinking much although the answer will be correct for sure. The second is when he's doing proper research going to library understanding searching on web and then giving you the answer. Okay. So

[31:03] that is the W case in a laptop example. Just ask someone for a laptop. Uh let's say he directly says that hey buy this laptop. Uh this is kind of let's say

[31:11] your normal extended one will be uh it is doing proper research again making sure that it understands the problem where it should uh like limit itself where it should not do this. All these things will be part of extended thinking. So again wherever you feel that hey uh this particular task and yes you have to take that call. Normally I

[31:30] will suggest that you can have this on sonnet and the extended thinking mode on but if you feel that hey this task or this chart is very normal I'm not just asking it very uh any problem which requires a lot of research or a lot of thinking then you can just turn off the extended thinking as well right so that is the whole idea everyone now uh let's of course test out these things as well let's try to see that how we will be prompting or we will be talking to claude and what is the best way because most people think that they can send anything to claude AI is like magic. It will just perform. But that is not the case. It is always

[32:02] and always suggested that we are working in a practical manner we are actually telling AI that what or how it should work. Because the better overall uh let's say instructions we give the better will be the answer. It is just like an assistant. The more you tell

[32:17] that hey how a particular work has to be done the better of course will that work be done. So that is the case. Now I have also created one more graphic everyone.

[32:24] This is a lot in depth uh lots of words and everything. I will highly suggest that you get your hands on this and you understand that hey what exactly is the difference between this uh where can they be used because again I have seen a lot of difference in using sonnet versus opus normally I don't use haiku and the response uh like overall quality so for a particular use case like strategy planning AI agents long document analysis I have seen that opus perform a lot better so that is where I will suggest based on my practical experience that let's let's go with opus that will be a lot better approach to go. Okay. So

[32:58] with that everyone now let's move on to the next part where we will understand that how can we communicate with uh claude basically the whole idea of effective prompting. So great everyone now let's move forward to understanding about prompting or talking with claude. So the goal of this section is that uh again we will not be discussing any over complicated prompting techniques or some random example. The idea will be that after

[33:22] this uh whole section you are able to understand that okay why bad prompts fail uh how to give better instructions and how to structure your request naturally. Okay. So that will be the whole idea. Now the biggest mistake

[33:33] which people do is expecting AI to magically understand the vague instructions. Claude overall is yes it is very very powerful but it works best when you communicate everything clearly. Right. So the easiest way to think about

[33:47] prompting is that you are simply explaining the task to a smart assistant, right? So you are not just uh let's say you are just I can take an example uh just let me copy it and let me ask it that hey give me a workout plan. So I'm just asking it a very very basic thing without any uh background without anything. So see I would love to

[34:04] help let me tailor this to you. Now a deliberately clarifying question. So okay yeah see that is again some overall thing which I wanted to show you around claude. If I just copy this thing and

[34:16] maybe ask to check GPD let me open new one then again it will try to maybe give me a very basic plan here's a simple balance weekly plan so see it has just given the full plan and that is where again claude normally or inherently is a little bit more smarter it is asking me the specific question that so before giving me the answer unnecessarily it is thinking and telling that hey uh okay what is your primary fitness goal let's say I say build muscle okay how many days per week you can work out. I normally work out 5 days per week. What equipment you have access to? So like

[34:50] okay I think I I can say maybe dumbbells and home setup because my gym is not a lot good. So in a way it has just asked you this question and comparatively Chad GP has given you the full thing. So I hope you do understand that how overall plot is a little bit better how it has given you these things right push pull legs upper body and active recovery all these things but uh here even though claude is trying to help it didn't know normally a lot about me right so in that case what I will do everyone pay a lot of attention I will just open a new chat and this time I will give this pop create a beginner friendly workout plan context I have never exercised regularly before so I'm giving it a proper context Next then goal improve general fitness and energy build muscles. Okay.

[35:38] Constraint only 30 minute per day 4 days a week. Let me make it 60 because 30 is a lot less. Give a simply weekly routine plan. So I will copy this again so that

[35:46] you can get its excess afterwards. Now I hope you do understand with this very very easy example that how nicely we have changed or we have provided our agent with a lot of context. Now you can see that I'm giving context, goal, constraint and output. Now again you can

[36:05] just play around with these words as much as you want and create your own prompting framework. You can call it CGCG, you can uh sorry CGCO, you can call it GCCO like totally on you. But the main idea is that you are giving your AI the proper uh instructions as well as proper things which might be needed by it. Okay. Okay. So if it for

[36:28] example if it needs uh let's say some uh overall health report some PDF you are providing that. Okay. So we will be coming that how can you use that as well. But that is the main idea everyone

[36:41] and that is where the overall discipline of prompt or context engineering comes into picture. prompt or context engineering where we are saying that okay to my AI let me just ask this question as well and you will see that how the response will be a lot better so even though claude asked clarified question now it is again in a thinking mode it is saying that hey I'm thinking about this architect and interactive workout plan widget so somehow it has went a lot forward and trying to bring a widget or something but yes now it is having a lot lot more uh idea about me if I would have any let's say health condition or something I would have provided this as well here so it doesn't make that mistake and you can see that how claude is giving a overall thing in a lot better manner right so as compared to other AIS and that is where it shines that is why people are moving towards it because it is getting a very nice widget and everything scheduling rest days building your weekly plan not that it is just uh let's say out anything without thinking it is properly giving the time to each and every way problem and then coming up with a response and see how nicely it is Tuesday, Wednesday each and everything is in a very very nice manner. So that is how like or that is the reason why claude actually is getting that traction because each and everything in a very nice manner right.

[38:02] So it is giving me alternate resting days pretty good. I can have a proper widget days per week per session rest days three level beginner all the things how many sets I should do reps time tip pull elbow back. So it has gone a lot ahead. So in that case it is smart but

[38:18] the second I provided it with more context the second I gave it a little bit more idea about myself it was able to actually understand a lot more in depth. So that is the whole case everyone. So unclear prompt example analyze this data set. We are missing

[38:32] the context. Why are you not saying that hey uh analyze this data set as a data analyst who are working at Microsoft or Amazon. Make sure that you do this kind of analysis. Find the strength weakness

[38:43] where there can be improvements. Then there are process instructions. So claude once it gets the instruction it processes them and once it process that everyone then if you are given it in a structured prompt that is uh let's say task context and format. Okay. So this

[38:58] is normally what I ask you to follow. Uh just make sure that you are again as I said don't fall for any of these frameworks because I personally find that although these frameworks are good at the end of the day each and everyone is trying to give the main give one and the same thing that is what task it has to perform context okay and the format so what it should return that is the whole case. So we saw this uh G C G O framework I think sorry GC A O framework where this was context uh so where we say the goal actually GCAO is goal context action and output so how it has to work on that but as I said majorly you're giving it a task which is the action you're giving it the context which comes into the goal and the overall context GC part and you're giving it the format that hey what exactly should be the output So the better you overall uh let's say provide this thing the better any AI in that case will work be it claw be it chart GPT and you will see a lot lot better results overall right now as a good practice you can actually just use any other AI as well to create prompt for you but in that case as well I will highly suggest that you will have to give more and more information so if I ask it uh give me a prompt to ask Claude about a gym plan Right now even though it will give me a way better prompt but still it is missing the context about me. So that context only you can

[40:28] suggest. So see it is seeing all these details requirement for the plan and that is why normally I suggest that okay on the prompt engineering part just uh ask the other AI try to understand what's a good prompt and towards the end we will also be making a skill right so we will make a skill which uh kind of ask us clarifying question make sure that it can create a very good prompt and then give us an answer. So that is the whole idea around connecting with your uh claude everyone and always remember that uh clarity is what unlocks the real power of claude better prompts don't just make AI smarter they make your instructions a lot more clear because you will be having different instructions so just as an example let us try out another uh case so let me open a new chat and I will just paste it see task generate ideas for a weekend activity contest group of five friend in Bangalore budget friendly prefer outdoor activities format give five option with a short description. Now let me just not

[41:22] use extended thinking this time and let me just uh enter it. Now you will see that when the extended thinking is not opening, it is just kind of giving answer a lot uh quickly, right? So it is just giving us answer out of the box. It

[41:36] has not thought about the problem though you have given each and everything in a proper uh extent you have followed a overall uh let's say manner or other instruction framework because extended thinking was not on it has given you the answer right from the memory maybe if extended thinking was on and I will just do the same thing to show you this time I will do the same thing but I will make the extended thinking on so now you will see that how before answering it will most probably try that Okay, let me think about the budget friendly. Then it gave you the answer. So simple request, no tools needed. It said that hey this

[42:12] seems like a very very simple request. I can just answer it. So it thought about the problem and based on the problem it is making that call right. So that is

[42:20] the main thing everyone uh again it is giving the tip and everything as well and that is where you have to also take the call that if your particular use case it requires any particular uh thinking it or can be done right off the box because unnecessary just burning token will not be that helpful right and now as we see the answer of course in the very first iteration so if you will remember in the go crash course road map yeah if you will see here uh we did saw that how after prompting there was a very important part of iteration right seldom will you get the right answer in a first go be it again claude or any other model for that matter so we have to make sure that we make it better by giving us our input as well so you can just say that hey uh as an example make the activities more adventurous so now it will go forward everyone and it will make sure that okay it is giving it in an adventurous manner so night trick paragliding right bouldering and rappling okay I'm not sure where it happens light water rafting, jungle camping and now everyone what I can also do is that I can ask it that okay now add approximate cost estimates so you will see that how I'm moving in a iterative manner stepbystep manner making the things a lot better so this is also one very very important way that instead of just having everything in a single prompt you can also move in an iterative manner seeing the output though still suggested that in the very very first part give it the most or the like give it the full context which is needed so that it can actually uh work and create your overall output a lot better and of course then you can keep on uh iterating and creating the answer a lot better. Claude overall is a pretty good in that. So you can see that how each and everything it has given you the good estimate per person group of five everything. Now it is saying budget trip

[44:10] night tricking and balding give you the most adventure per rupee. So yeah very very good understanding a little logical kind of answering the question and that is what we want to understand right and I'm taking these example because I feel that they are relatable to everyone uh be it from tech or non techch everyone goes for adventure trip so that is the whole case everyone and yeah we can see that how in an iterative manner as well we are able to take full advantage so just one thing I will say think of prompting not actually asking a question don't say that hey I'm asking something to claude but let's say as beefing a task or as normally a solution to the problem right so whatever you are giving it properly give it as a overall problem and then it will provide you with a solution or let's say overall as a task you have to provide someone okay don't just see your AI as a Q&A kind of a bot see it as an assistant more context you give explain the problem give the role in and out of about everything then it will give you out the whole answer overall so that is how you can actually use any AI a lot better in a iteration ation or iterative manner with very very good prompting. So just to quickly summarize make sure that whenever you are talking to a you are giving a proper starting prompt each and everything with the goal context what action it should take what should be the total output think about this in a structure prompt what is the task what is the context like let's say what all you need to provide and then the format or the output format how it should work right so that is where I think it is very very powerful and of course it is not that even if you provide the perfect prompt uh your answer will be perfect you might have to then also ask in an iterative manner give it more things make sure that the answer gets corrected that is something which you might have to follow so this I believe everyone is the perfect strategy if you want to use claude and get the best answer out there so now everyone that we understand how to communicate with claude effectively via the prompting and iteration of course we saw the question part as well let's now explore one of the most powerful capabilities that is working with real files and documents because again we will be using cloud for an array of things and our work or overall we day-to-day we work with multiple files and that is where I feel that the next capability of claude overall where we can use it for with files and everyday document is very very impressive and important so let's move on to the next part everyone where we will see that how we can use our claude with uh files and other things so great everyone now let's see that how we can work with files images documents um Excel files anything with your claude.

[46:46] Now pretty sure that we have more or less used claude or chat GPD with the same but I would like to show you like what all more is possible. That is the whole idea here. Now before we move forward I would like that you do a very very important change and believe me this one change will make your claude work a lot better. like this actually

[47:05] believe me is something which I always keep in my cloud because this helps me to make sure that even if I'm providing some vague instructions or something vague to my AI it is able to act on my behalf and ask me the questions. So I will say here that for any task which I provide please make sure that you ask me about the below things. Now I would like to make sure that in by using a hashtag like this and pretty sure that many of you might have seen that the prompts which are provided to you right. So I

[47:46] will just have let's say markdown to uh text or something. Let me just show that. Yeah. So many of you might have

[47:53] seen that if I copy let's say a particular prompt then uh you will be having these kinds of uh slashes hashes or something there right so they are actually the markdown format. Now you can read more about it but the whole idea is that if I just write something let's say hello here or uh let me just say rich text or html okay one minute let me quickly check I think markdown to rich text so the idea is I just want to show you that how normally it is visible yeah so as you can see just adding this uh hash in front of your word it actually is a markdown format which kind of tells your uh AI that hey This is a heading right? So if I write something hello, how are you? Just as an example, you will see

[48:41] that your AI will also see that hey this hello seems like some heading. So maybe I should uh treat this section as a separate one. And that is the reason like if you will just as an example if I say copy this thing and if I paste it here. Yeah, you will see that okay this

[48:59] thing is having this star star because this is for bold. So if you will see it in the right it is getting bold in here right. So this actually everyone this uh like double star is to bold things out.

[49:10] I can just show you that what exactly this markdown format is and highly suggested that if you are giving your uh prompt use this markdown format like it is pretty easy to understand. Hashtag is heading then you have this uh let's say for your best practices and everything is there for paragraph you can normally write it down everyone. Then for line breaks like you can have this in a paragraph block. For emphasises you can

[49:34] have this in a bold block. The idea is that better your AI will be able to understand better again answer it will give right. So in view of that let's go back and I will just ask my prompt uh sorry claude that below things which is the goal.

[49:50] If uh or let's say context ask if any other context is required right then I would also say that output so what should be the exact output format and I could just also mention so going with what we discussed in the prompt action what should be the course of action I would also mention now Since I showed you that how Claude is having the ask question capability, I will say that make sure that you ask me questions regarding regarding the problem so we can tackle the whole problem task effectively. So this is again very very important. The second you add this thing to your cloud for every problem like if you give it any particular problem it will make sure that these instructions will also go with your uh let's say message and the claude will make sure that uh instead of just giving you any vague answer it is uh effectively asking you these things right so this makes your overall burden of always thinking in terms of prompting framework a lot less because now claude will ask these questions with you claude will make sure that hey each and everything of this particular manner is already clear and your output will be a lot better and in the end I will just add one more line very very important uh make sure that or rather don't always agree with me make sure that you present what exactly is best for the task in hand so this I am writing everyone to make sure that we are able to understand that how uh like normally what happens is that EI is a very yesmen kind of a thing. It always if you will say that

[51:47] hey uh give me $1 billion it will just give you a plan and just praise you. I want to make sure that it should not always or unnecessary agree with me. Okay, it should actually be like my manager who is kind of correcting me at every step or someone who is my senior so that it is not okay making those mistakes and making me feel happy. So once you save this changes

[52:11] then you will see that how nice your overall responses become because for every problem now everyone we will be having these things taken care of. So with that in mind everyone now let's go back to our chat and let me just open a new chat. Let's understand about the document analysis or the working. Now

[52:29] again the main idea here is that we will be always working with files right? So it is seldom the case where we just use AI independent of any files or structure like of course we are using it either for our work. Uh normally we just don't go to claude and just ask it question etc. So for the same everyone one of the

[52:48] biggest difference between AI usage and powerful AI usage is giving AI the real information to work with right claw becomes dramatically more useful when you give it uh documents reports or data because then it is able to tell you the answer or basically generate uh the overall responses based on them. So for the same uh what we will do everyone pay a lot of attention uh we I have some files now you could of course have some files uh related to your personal school college or in your job as well uh this is just a report global startup ecosystem report so it's a 50page document and similarly I also have a excelx so this is again a excel file via which like you will see that how it is having so many of these different different uh data points our idea will be I'm I'm taking a real world use case where let's say if your manager or your you have to in a college go through a particular report or create something how will claude help you in that and one thing more to notice everyone that uh though you could do the same thing in chat GPT with proper prompting again and with connecting it with uh proper tools etc which we will see as we move forward it is going to be a lot lot more powerful so that is why it is very very important that you understand how claude overall works with this So with that let's now start. Uh you could either go here and add files or photos. You could

[54:09] either do that or you could just drag and drop this. So once you drag and drop everyone it will get attached and claude while it is getting attached. See it is taking a little bit of time though the file size was not high. It will try to

[54:22] basically make sure that is understand that it is able to extract the text etc. Now you could just paste the prompt analyze this prompt and summarize the five most important insights. return the insights in a bullet point with short explanation. Uh if you remember we also

[54:37] set up the instructions where we asked that it should ask us for the goal action all these things. So yes if it feels that more things are needed it will ask us for the same. Now I could just send it everyone and we will see that how since it is extended it will try to understand each and everything it will now start up and unlike uh other AIS and this is where actually claude is very very powerful right so that is the reason when Indian IT stock fell it was able to uh basically showcase these kind of functionalities and we will see that how unlike providing these instructions again and again we can also make them as a skill. So when we will go into skill

[55:13] section. So see now it is asking me question. The reason is that we also asked that in the main prompt the prompt which we did to personalize it that hey if you have anything please ask the question for it. So it is asking what is

[55:26] the who is this somebody for? I can say uh investor or VC audience. How deep should the explanation be? I think uh

[55:35] can be three to four lines per insights. Now since it has cleared these things out and another best part which I like everyone is that how it is giving you these option as well. So instead of just asking the question which other AI also ask it is kind of also giving you the choices as well just making your work a lot better like of course all of us are very very dizzy. uh if cla can give us

[55:58] these things then of course we are able to see a lot better results and we can just select them and even like anyone who had no experience whatsoever with AI can also work on that and see it is able to give us all the things now if you want as we said we can work on top of that we can ask it rather to make a quick uh make a short infographic to explain these which I can share with the uh let's say members in my call. So now when I will ask it for the infographics everyone it will create one very nicely make sure it is easy to understand. So not only can claude uh actually understand these things it can actually also understand your PDF report spreadsheet CSV and give you these uh the answer after the analysis in some visual way. So with

[56:50] respect to let's say of course Excel and PowerPoint presentation or even some infographics etc. So now you will see leading front- end design skill. So we will come that okay what exactly is this skill and how can we create our own skill as well when we will go and jump onto the skill section. But here the

[57:07] idea becomes that how creating crafting professional HTML infographic for investor presentation and it is showing you each and everything. If you click this it is showing you that what exactly it is doing. So it is very very important. Now again just uh getting the

[57:21] work done versus understanding that how work is getting done. This is a very very big difference. I want that you follow the latter where you are understanding as well that okay what exactly Claude is doing. So I always

[57:32] have a habit that I read through these things what basically Claude is saying or any AI for that matter. So I can understand that okay where it is taking the step. So if I don't even get a right answer, I can ask it that hey this is maybe some step which you have to correct or this is the action. So maybe

[57:49] I can ask that hey when you are creating uh make sure that you ask me for the color palette or let's say you search the web for more information. So that is the kind of a thing now it is seeing showing you the same like how it has created the same I can just see it getting created. So just a minute let us have it here and see how nicely it has created the same thing right. So pretty

[58:08] pretty good approach everyone. You can actually share it with anyone. It's pretty well versed. You can download the

[58:14] same from here. Once you download it, of course it can be in a HTML format. Here is the code as well. Now again you don't

[58:20] have to understand the code. If you want you can just uh select anything. You can just make sure that okay do this change or something that can also be done. In

[58:28] line with that in the last overall thing which it generated if you select you can just reply where this will come as a context or the reference to this particular uh chat. So if you're continuing your chat everyone and if you feel that hey uh this point needs more thinking just select this point and click reply and it will do the same or if I want so just I will say that hey uh my uh let's say can I have it in white background instead. So again a very very simple change I'm asking it to do and it will what it will do it will start making the change into this only since it is having the context I could generate actual artifacts or use uh like things which I could use in my job. So that is where it

[59:14] gets powerful everyone and that is what I want all of you to learn and this is where I feel though other AI can also do it. So again since like Claude is all the hyped up I will not as an expert say that uh okay claude is only the best others are failing. No, but claw does it a lot better. So that is the whole idea

[59:32] and it is having those skills etc as well. And see it has done the whole thing in uh white. I could actually ask it change the points also in white and use a darker text overall. Okay, I think

[59:46] it is uh still doing that. So updating car background and everything. So let it work. Actually I think it will be better

[59:52] to first uh let it close because slowly it is actually doing something. So see now it has changed these things in a step we can see that okay what is exactly it is changing. So updating full card accent and card number uh colors.

[1:00:05] So now it will be doing that in front of you. And yeah once it is done I think these also will be a little bit blacker which of course will be very easy for the readability and if you share this with your team or your manager like they will be like yes this person has actually done the work. So see how nicely it is right. It is able to

[1:00:23] understand and do the step in a do the work in a step-by-step manner. That is actually the power here. It is not that okay it is just doing it and you have no idea. It is kind of moving in a

[1:00:34] step-by-step manner and that is based on how claude has a brain thinks and do the work. So with that everyone now let's move forward and see more example as well. So now of course you could press uh give it your images etc as well. You

[1:00:48] can give it your PDFs, you can give it your uh spec sheets etc. Uh ideally you could give it anything like if you will give it a code etc as well it will it will explain understand that. So the idea is very simple that claude not only does it works and chats with you it is able to actually work by doing a lots of analysis and this is where again information can be turned into actionable intelligence. So that is the

[1:01:12] whole idea everyone that how it works and this is again very very important. So everyone now let us move forward and try to test more of plots functionality. So the way I have actually going around this crash course as you can see slowly and slowly we are trying to master each and everything rather than uh those 15 20 minutes video where like you are just bombarded with the information and at the end though you feel happy that hey I know something but yeah you don't end up actually gaining something. So now next

[1:01:38] part everyone will be fair we get a lot of use case and we have to do a analysis right. So for that majorly you might be getting a PDF uh sorry uh Excel file like this. So Excel SX. Now earlier we

[1:01:51] used to run uh data science machine learning models to get any information out. Now with uh claude etc. And I would like to show one more thing here actually if we will go and search and I will be creating videos on that as well.

[1:02:03] Claude is there now for Excel as well. Right. So I have to I like I'm trying it out actually how well it works in Mac.

[1:02:10] Do I need to have Windows etc. But the major idea is everyone that uh in future knowing things will be very very helpful because then you can uh just make sure that you're steering AI in the right direction. So the basics will still hold. But if you are someone who don't

[1:02:25] want to focus on basics and feel that AI will do something everything sorry then it's a problem. So with that now everyone let's try to give in a way better prompt here and the way I've asked for this prompt uh is based on what I taught you plus I asked Chad GBG to create a prompt for claude. Now again uh you can make sure that okay you are using these AIS to write prompt for you but still you will have to tell what you want. So in here I told that okay these

[1:02:51] are the things which I want. Now I would paste this prompt here as well everyone so that I can share that with after uh with you everyone in the end. So now if we will see you are a senior data analyst with experience in manufacturing analytics all these things. I will

[1:03:07] provide you with an Excel data set related to gelatin production yield quality metrics. Your job is to analyze the data set. Extract the most important operation insights with minimal verbosity. Then context. Okay. What all

[1:03:18] is given exactly how it has to work. Outliers provide top three factors. Top three factors affecting product quality.

[1:03:26] And this is again one of the client data which I had. So this is a real data. It is not some dummy data. And the second I

[1:03:31] enter this uh Claude will of course get started. And yes, you could have choose opus for this as well. But if I show you if I go on opus, it will say uh opus consume. So let me just get it. Opus

[1:03:45] consume uh usage limit faster than any other model. Right. So normally I have seen that yes with good prompting. Uh

[1:03:51] sonnet is also pretty good. Now again it has invoked some reading excelsx skill. So yes, it kind of is giving you traces that hey I am way more powerful with something known as skill and that is what we also have to understand every now I would like to show you one more thing so one more important part is that not only can it work with just structured data like this the best part comes where it can work on non-structured data as well right so what I mean by non-structured data like your ex uh let's say images etc so meanwhile it is running everyone uh another good part is that how we can run multiple tasks parallelly. So if you

[1:04:28] will see this task is already running, right? So this is already running. I can open a new chat. Now this is a overall

[1:04:36] uh let's say thumb lane which I have designed. Maybe I will be using this for this video as well. Uh it's a it's a pretty good one. If I could just change

[1:04:44] this icon, but I could just get it here and say analyze uh this thumbnail for a crash course on clawed AI for my YouTube channel. Okay. So again this time though it is a thumbnail it is just having this automate your life as a text and maybe some few things more majorly it will also try to understand and give you the overall output by understanding the image as well this time and I will show you that how you can make skills for each and every of these things based on your particular requirement as well right so that uh if you find that hey this particular chat has worked pretty well and I want a similar kind of thing maybe going forward then you can do that as well So now everyone if you will see uh it is giving us the answer parally this is also working okay so yeah like doing a lot of analysis I think that's why a little bit of glitch but let's go back to our thumbline so get thumbnail to work with before I dive into analysis let me ask you a few more question uh target audience channel size and how it should focus on so let me just copy this so this is how you have to work right so again see uh it is coming up everyone from the master prompt which we have given so if you all remember if I go in the settings I can get rid of this should be fine then I gave it this particular thing right and this is exactly what it is following so see uh goal are you looking to improve this existing thumbnail validated before publishing or this context action and output so now you have not specifically asked for this particular thumb uh prompt but it is taking that into consideration and that is why I feel that if you have the right way of using the claw overall then please please just make changes in here that is going to be very very helpful. You can say that hey

[1:06:32] always on and always make sure that the way you are asking or providing response is very professional if you're using claude in a professional setting and if you feel that okay you are using claude uh just for some research etc then ask it that hey please please make sure that you always search make sure that is not very long because then unnecessarily it will be sent but up to a basic length to give it a very good start right so this is like training your intern to just ask these questions now I could just provide these things uh I can just copy this maybe improve existing thumb lane then I could say uh beginners developer business users I think everyone is the target audience so I'm showing you this I will not be actually moving forward because I want to show that okay uh how exactly we correct in an iterative manner as well right so not jumping any gun here now it is a established I hope it is established and you can subscribe as well everyone then 40k uh then computer landscape any other cloud AI uh lots of them most are uh shallow or just talk about launch etc. And is there a person in you? Yes. So I am the person. Yes.

[1:07:43] Should I focus on CTR optimization? So I can just go a little down say optimization and then I can say structure critique score breakdown actionable redesign suggestion. So I think this is something which I want. So now in a way we have

[1:07:58] given the answers. I can just say below are the answers. Now if I could not have provided that prompt it might have not uh performed this well. It might have

[1:08:08] just given me out of the box. But now it knows my whole uh approach like it knows my whole intent as well. And now of course when the claude will work it will have the extended thinking open which I will suggest all of you to have and see scrutinizing thumbnail element for CTA optimization tactics perfectly. It is

[1:08:26] working on these things. Text automate your life large bold text for your life. So again it is showcasing these things right. And if I go on generating one

[1:08:34] parally this is also running. Uh okay I might have to retry it. Let us retry. So

[1:08:38] again I think this asked for a retry because it took a lot of token because this file as I told uh the Excel file which I gave it is not actually uh very easy. Okay. It is not some dummy data which it will work on since it's a proper client file. Sometimes this also

[1:08:54] happen right. So totally totally uh worth it not a problem. We are now seeing that okay it is done and in a bit I think it will be providing us with the response. So okay like see like some

[1:09:06] issue here but let us let it provide okay let it provide. So everyone uh the last one was actually facing some issue. So I have actually provided uh in a new chat uh and this happens sometimes. So I

[1:09:16] would like you to know that yes this is also perfectly possible in claude uh like I have faced it many time as well. Uh one more thing if you refresh this page uh then also like sometimes I have seen that it forgets this task. So unless it uh kind of give you the answer it is not saving the chat like I face this issue. Now uh I've just provided

[1:09:33] the same again you will see that how it is saying the task is well scoped you have covered goal action output format uh clearly. So again coming up from the major prompt uh which we have done at a user level and again see it is asking for the uh load the data set and ask one focus context question. So it is just doing all these things right. Uh as I

[1:09:52] said since the file is uh Excel and it is a pretty long file it might take some more time either or basically lots of tokens. So that might also be an issue but yes piling let's see our uh thumb lane overview. So see if I show yeah so here it is saying that headline is wrong for your goal. Automate your life is a

[1:10:09] generic automation hook. It should it could be any zap or make cloudi full crash course master cla or cla does everything. Then logo you're holding it as recognizable at thumbl height or tightening logo strings down no losses meaning viewers won't know won't know it's claw related unless they already know the brand so either digital blog with claude wordmark logo clearly so see it has also understood that how the logo which I provided right that was not of claude actually that I think was claude co-work because again uh that's the whole idea everyone let me just get that image yeah so it did get that hey this is claude kowork not claude And then everyone it is giving more things. The

[1:10:49] background UI is wasted space. Uh text AR is flat. One big word one smaller supporting either blur it more or make you pop background UI or zoom into one striking output like a workflow result that shows claw doing something impressive. So yes it has kind of

[1:11:04] provided a very very good manner. Now do you have a transparent PNG of yourself from the shoot? Any color preferences.

[1:11:09] So want to mock up a revised thumbnail concept. So see it is asking you that if you have a PNG just provide and it will start and provide you with that particular thumbl as well. Now normally I don't use clot for image generation etc. And I would like to cover this as

[1:11:23] well because it takes a lot of token. Okay. So again if you have a max plan or something you can surely do that but I have seen that in free or pro plan after two three images it will ask that hey now I'm called up uh it will take a lot of time for me to get back. So please

[1:11:36] see that. Okay. Now in here as you can see this Excel it is taking a lot of time though I remember it was able to do that in uh like co-work but still no worries let it uh run and in a way then it will be able to give you a proper analysis. I would actually like to show

[1:11:53] you what kind of uh presentation I was able to make by working on this particular data only. So just one second and I think uh one minute. Yeah. So this

[1:12:03] was everyone the presentation which Claude created for me based on that data set right. So it ran all the things on the data set created these kind of graphs as well and it was able to give me this very good presentation. So you can just think that if you uh suggest or give this presentation overall to your client to your manager how good it will be and this complete presentation Claude was able to generate for me. So that is

[1:12:25] where I think the power lies and that is where we should try to master Claude as well. Now again it is just taking a lot of time should be fine as I said it can run in the background but for us we are able to understand that okay how exactly claude works with your documents so I've shown you PDF reports spreadsheet notes transcript of course it will work images also I've shown you and yes I will when we will cover skill you will know that okay if there is some particular file and you want that it should be handled in a other manner it can do that as well with respect to let's say any JSONs or normally some JSON or output file as Well, so this is all what happens everyone in the cloud document analysis workflow. Now this is very very important. I hope you do understand that

[1:13:07] because this is where you will be using your day-to-day files to actually use uh get the work done right so using AI is all file creating website etc. But this is where it gets lot powerful and this is where I would be liking that you use clot the most. So now with this clear everyone now let's move on to the next very very awesome and exciting topic which is clot artifacts. Now if you

[1:13:29] remember I asked you in the starting that go to your settings and uh one minute go to your settings and do make sure that in the capabilities this artifact thing is turned on. Okay and we see this artifact here. Now these are all the very very basic basic kind of an artifacts which we can ask uh clot to create but of course we will take it a step further and ask it to uh create more better things for us. So with that

[1:13:55] let's now try to understand about the artifacts. Great everyone. So now let us understand about one of the most powerful feature and in here we will be actually also building a very good uh mini project kind of with you that is your portfolio website which you can of course share to anyone. Now up to this point we have

[1:14:10] used claude mostly for generating answers or like analyzing some information right. So we were giving it some query or we were giving it some files etc. and it was able to give us with uh the answer maybe in a lot better form uh in the form of let's say some document some presentation BPDX etc. But

[1:14:28] uh claude can actually go a step further and can provide you interactive tools as well and that is where artifacts come into picture. Now you will see that these are the pre-built artifacts which Claude is saying that hey I can generate for you. Now there is entropic office simulator, raw node transformer, code vortex, QR code generator like you give it a website it will generate a QR code etc. And again like many of these things

[1:14:51] I think we can just test out a very simple one. So let's uh try to uh have this uh where's the sloth. Now in this if you will see like it's kind of a mini game but we will try to actually use it for a proper use case right. So I see

[1:15:05] that many people are just showing you the artifacts. Uh okay let me refresh it. Let us go to artifacts and let's try to see. Yeah. So I was

[1:15:16] saying that many people are showing you the artifacts but they are just kind of touching on them because I feel that uh they are not aware that what all it can do right. So in that sense everyone let's try to understand uh let's say this thing uh emoji dream on uh interpreter. Now describe your dream and claw will interpret it. So if you will

[1:15:35] see like there is a starting prompt. We can go and customize the same as well. I think there was a calculator as well. I

[1:15:41] think that is something which we can use. So let's try to see that as well everyone. Or maybe we can just try out let's say this how petty are you. So

[1:15:50] again the idea is that this time we are not asking claude to provide us with some analysis in form of text but rather we want that hey create something for us. Now if you will see let's say if I just measure the pettiness whatever it means the idea will be that okay how exactly is it working? uh if I want as I said everyone it will be creating this small app kind of for you which you can also open in new tab etc right so if you will see it can open this in a new tab where you can share it with everyone else as well so with respect to that instead of focusing on these one let's try to create one ourself artifact as I said now uh let us get cooking pick an artifact category I think it will be amps and website and let's try to actually create one so again small application that clot directly generates inside the chat so calculator, dashboard, planners and maybe many web tools. So let's actually try to have a

[1:16:40] prompt. I have created a prompt which we can use. Let me save this parallelly.

[1:16:46] Okay, where's the file? So I will just quickly save it everyone and let's see uh again I think uh I can just skip it. Let me just cancel it out and let me stop it. What I will do is uh okay you

[1:16:59] can save changes. I will just paste this. Okay, create an interactive monthly budget planner. The tool should

[1:17:04] include inputs, monthly income, rent and groceries, transportation, entertainment, other expenses and outputs. And I would just say create a web page artifact for me. So now instead of like creating some document, PDF or something, it will be able to create a very very good interactive kind of a widget or artifact. So if you will see

[1:17:27] now it has started to write the code. And again uh the best part about AI or about maybe you can say it as VIP coding is that now you don't need to understand these things right earlier this used to maybe take even a week easily and that is where I think AI is democratizing a lots of things that now even without understanding these things even if you are a proper no coder though I am a coder I understand these things even without that you can generate application at par with a experienced coder as well right so that is the whole case everyone Now let it quickly work. I think I will just quickly uh wait for it to finish. So as you can see it has

[1:18:05] created the same everyone. Now this is the artifact which it has created. Now I could just add let's say monthly income say 50,000 and now again rent and housing say 15,000. So you will see that

[1:18:15] how nicely it is able to create this right and either now you can download the same as HTML or you can publish it as well. The second I publish it everyone it is actually now very very easily like if I just open it on an incognito tab usable by everyone. So that is the benefit of creating these artifacts if you have some small small tools or widgets in your mind. Now you

[1:18:40] can just create them within a prop. So nothing nothing else required. As you can see currency set to Indian rupees and everything as well. Now just like

[1:18:47] again uh let's say having the follow-up thing we can ask it to make changes in here and claude has essentially generated a small application that we can interact with right so this is where the power of claude as a tool also lies a lot and many time you will see that how claude directly pro provides you with these artifacts right so that is the main benefit everyone now see we have added that hey improve the budget planner add a simple pie chart showing expense distribution a saving goal indicator so now it is having the context that it will pick the same up pick this particular thing up and try to make changes in here. So when we will republish the same again you will have to republish the changes will be there. So you can actually take screenshot like this and also make sure that you are passing it to claude and asking that hey make this change. So I will just show

[1:19:33] you this as well. I will just say uh make or let's say have a button for dark mode as well. So after this we will be passing this whole thing. Now you are seeing that how it is

[1:19:48] kind of doing a lots of coding in the back end writing those functions HTML script and you don't have to worry even if you are a coder I think now this is the right way right so let claw do the 90% of the job and the rest 10% the optimization everything is something which you can do and that is where the power lies so see how it has created this thing budget overview pending breakdown expenses are still there the complete expense distribution each and everything is kind of mentioned so let's say grossly 5,000 so it is basically ally able to work on that. That's the whole idea everyone. So we can get this idea and everything. I can publish the

[1:20:22] same. I think it will create a new artifact. Uh I don't see that it is updating the same. So rather let us have

[1:20:27] it support dark mode as well. Right. So it should support dark and light mode both basically. Okay. So that is the

[1:20:39] whole idea everyone. Now I do understand that yes uh these may are also few things which have been available for the last year or so and people are able to of course use them. So see it is making the code changes in the same code right and right in front of you that is kind of very very smart. So now everyone

[1:20:55] let's actually move forward and I would like that you create a portfolio website like this and I will show you that how easy it is right. So for that I want that you first go to your LinkedIn uh pretty sure you will be having a LinkedIn page. So download LinkedIn profile as PDF. Okay. So there is this

[1:21:14] way of saving your LinkedIn profile as a PDF. Just go to me uh that is your page view profile and just save to PDF. Okay.

[1:21:21] So this is what you have to do everyone. and your complete information of uh let's say LinkedIn will come to your PDF. So I will quickly grab mine. So

[1:21:31] I've got mine everyone. Let's see if it has added the dark mode or not. And you will notice one more thing. So claude

[1:21:36] has generated the logic, the interface and the calculations automatically. Right? So it is smart in that sense. It

[1:21:41] is not just doing a very basic kind of front-end development. It is able to actually do a little bit of logic handling as well. Right? So that is the

[1:21:50] whole benefit. Now it has been published. We can just go and add it or sorry access it. And there is an M link

[1:21:58] as well if you will see. So you can end this as well everyone on your website or somewhere. So that is also very powerful right. So you have created this small

[1:22:05] thing and you are just able to easily easily just end it right. So that is the benefit. Now if you see dark again it can be a little bit better but yeah I think overall this thing works right. So

[1:22:16] with that now everyone let's move forward and as I asked all of you to just get your LinkedIn profile PDF something which I have got as well as you can see now I want that you maybe go to chat GPT open a new chat and uh okay this was helpful no worries and just drag and drop your PDF ask it I want to create a artifact website on claw for my portfolio. Can you please provide me with a very good prompt to handle each and everything. Make sure that the website is uh one second.

[1:23:11] Yeah. modern, very sleek looking and pushes out my advant uh skills, advantages, everything so that if I share it with someone tomorrow, he get an idea of my expertise. Again, that's the best part honestly that now since these tools have evolved so much normally uh they are kind of providing you everything in a very nice manner. So see it is giving you the

[1:23:36] complete uh prompt uh page now uh sorry prompt which you can copy. it is having each and everything and that is I guess the right way of using these tools. Now gone are the days where you have to do a very very basic level of plot engineering. I think now this is the way

[1:23:49] of moving forward everyone right. So see uh website structure. Now the reason that I am asking chat GPT to generate it and not clot directly because again the main idea is that uh in the same chat you will have to handle lots of chat and cloud. Right now I will just copy it

[1:24:04] once it is generated. So as you can see it is done. I will just copy it.

[1:24:09] Go to claude. Let's say here uh okay this was incompet my bad let me go here open a new chat and say that okay we can go via artifact maybe create a new artifact it will ask us apps and website everything so now again we will do the same thing right so we will just paste it now it will ask few questions because we have kind of asked it in the main prompt as well so let me do while you answer feel free to also describe your idea the more everything so I just want to say portfolio website that's pretty good it is for personal. Do you have a specific tech preference? No

[1:24:44] preference. And if it starts generating then I will stop it actually. Okay. So

[1:24:50] few more question to make it uniquely yours. Also feel free to share your name, bio everything. So I think I should just stop it for the timing and I should just attach this and the prompt.

[1:25:01] Uh okay. Yeah. So please okay I think it has started. We have to

[1:25:05] stop it. So it is just saying that hey I will create without you. No worries. AI

[1:25:09] getting a lot excited but I think since we have the prompt everyone we should handle that please create the same I have pasted the prompt. So now when I ask it of course lots of thing it will have to do but the main point is that it will be able to very very nicely create the same for us within seconds. And the good part is that you can of course uh understanding that how Claude is also having a very very good technical uh capability or knowledge you can of course make it a lot more better in future as well. So this one everyone as

[1:25:44] you can see I have to created it with some other tool but cloth can create a similar like this if you copy paste the same plus overall it can even make better than this because at the end of the day uh if you provide images and everything all of these are just being kind of created by AI. So I have not even written a single line of code here. Uh let's see that how cloud works on my uh here. So it has actually created the

[1:26:07] same everyone. Lots of code it has written like it took a good two three more minutes. Uh and I guess the idea is that since I'm having a very long profile like I have added so many details it took so much time. Of course

[1:26:17] if you will add the photos it will support the photos as well. Uh now you can see that how very very nicely it has kind of handled everything. Uh I I like the this one a little good honestly because it is very to the point. Okay,

[1:26:30] the other one I created for some other use case. But yes, if you just publish it and I think all of you should also not try to create it. Uh towards the end we will also try that we can join it with in our make a project that we can join it with uh let's say Excel or something. So now if you will see

[1:26:44] everyone uh yes this if you will see is a website which of course I can share with anyone or rather I can get the code as well. Right. So that is one more benefit everyone. If you will see

[1:26:55] available for consulting collaboration not sure how it picked it up. uh view work everything. So it is showing me contact me 15,000 1500 okay not problem but anyways the idea is that founder engineer uh engineer founder uh educator pretty nice thing AI system middle passionate so see how nicely it is able to handle these things experience timeline all of this thing he got from my uh LinkedIn profile then the skills and stack okay how nicely it has created it result that speak learn from me watch on YouTube it has the link also m uh basically hyperlink Then some selected projects everyone which I have actually worked on highlighting this thing. Of course if I want then it can

[1:27:35] add these things. Uh as of now I guess if you will try to send me a message or something it will of course not work right but we can we can change. So see as of now this button is just a placeholder but no worries. Uh towards

[1:27:47] the end when we will see connectors everything we will try that how we can make this whole thing work pretty well as well right? So if someone wants to connect with us, it will just uh hold the same the query and everything in a Google sheet and let's say weekly it can send us any email or maybe we can go to the Google sheet and do that. So do make sure that you create a very very good website and everything uh built with the Bangaluru Mayankal. So I think it has

[1:28:10] got more or less everything right. So that is the whole idea everyone that is where this thing is very very helpful. So now you have to just think about uh let's say cloud artifact that it can give you ROI calculators, marketing dashboard, habit trackers, study planners, productivity tools. If you

[1:28:27] understand that okay how you want your website to work as a product builder or product manager as well. Now that is more than enough. So you have seen that how claude doesn't just answer questions, it can help you build solution and that is all what I think I had uh 1 minute. Yeah, I had in this

[1:28:44] image as well. So AI generated tool from prompt to interactive application. You give it a prompt. You give it all the

[1:28:50] context and everything logic generation, interface design, calculation engine, all these things, right? All the different different backend logic etc. Claude can do. Now up till now we have

[1:29:00] just seen actually the half of uh artifacts because it gets more powerful when you connect it with your day-to-day tools. So of course as of now we have not learned about connectors which I will be discussing in a bit but once you connect them with your day-to-day tools like let's say Gmail, Google sheet, notion which all claude also supports natively then I think it becomes very very powerful right and then you can get the interactive tool. So now for your clients as well as for uh let's say any of your uh work you should think that hey how can I have a artifact or something created because that visual thing makes it a very very good overall uh beneficial returns right if you're showcasing someone that hey this is the research I have done maybe showcase that with some good graphs and everything and of course if you have some repetitive work maybe create an artifact for that so that is the whole case everyone it helps you to instantly just generate tool So claude does just doesn't answer question. It can build you it can easily

[1:29:58] help you in building the solution as well. So now that we have seen how claude can generate tools everyone the next powerful feature is something known as projects which helps you to organize your work and create repetitive workflows. So you will see that how as of now we are kind of working and yes we are able to do lots of things but still it's a pretty messed up thing right. So

[1:30:17] we have so many chats and everything and though we have understood the overall UI and everything I think project is where next our overall power will unlock. So in the next section let's everyone try and learn about and master projects. Great everyone. So now let's move on to

[1:30:38] projects and I think this is the biggest difference between using AI casually versus as an advanced user because project helps you to categorize your overall AI or claude the way I think you have categorized your life. So seldom will be the case where you would be just opening these chats and I think that was one year before even when Chad GPD didn't have project and I remember I purchased it specifically for that. So this thing honestly is present in uh Chad GP as well. If you will see

[1:31:05] projects in here. Now the idea with cloud is like taking it to the next level and the biggest problem or frustration is that when you are using AI tools and uh every new chat uh like basically just starts from scratch right so you will be working on let's say a particular client a particular problem and if you're opening multiple chats just like how we are learning this claude today each and every time I have to kind of tell that hey what I'm doing and everything. So that is where everyone projects is very helpful and this kind of takes you to the pro level.

[1:31:34] Uh believe me I think if I show you I have project for every facet of my life every client daily AI live at Udemy AI consultancy AI training my YouTube and you can also create the same. So if I just click new project a new project gets created everyone name of the project. Let me say uh AI consultancy may okay you can give what you're trying to achieve. So let's say provide uh or

[1:31:58] let's say get clients and provide awesome solutions. Okay, awesome AI solutions. Now this is just a basic setting of your project everyone. Now I

[1:32:11] can do create project and you will see that how it has created a space within cloud for me. So that is what uh project is. Though our user goal is exactly the same now content creation, research project, business planning, we of course work on things in terms of grouping, right? So that grouping gets transformed

[1:32:28] into your project and the best part is that each new chat if you want of course it can have the access and everything about your project all together. So it is able to provide you with way better answers and instructions. You will not have to again and again give it the same instructions which is very very frustrating as I said. So project solves

[1:32:47] this problem by giving claude memory about a particular facets of life. So think of it like a folder but where each and everything is aware about everyone or maybe houses in a society where a house is having an idea that okay who lives what happens everything. So with that everyone now let's see you will see that how you can add custom instruction.

[1:33:05] So these custom instructions everyone sit on top of the main custom instruction. So I would like to clear this thing out because it might get confusing. Plus this will be very helpful in claw code as well. At a

[1:33:17] claude level everyone when we talk about the major claude level of course we have given it some instructions that hey ask us question make sure that you don't uh if I just show you to remember again remind you uh for any ask I provide ask these things make sure that you ask the question and these helps in making overall your project sorry claude work all lot better. Now inside this everyone now when you create a projects it also is having instructions which it can follow and they are on top of the main cloud instructions right and of course when you will be having multiple chats inside they can have their own instructions as well so I can open a chat and say that hey please make sure that you're very formal or assume these things and everything. So this is the hierarchy everyone please please remember this because this will be very helpful in uh clawed code as well right.

[1:34:07] So now with this thing clear let's try to add some files. What I will do is I have the brand guideline txt. Now if you will see this is also uh having proper uh this thing markdown formatting right.

[1:34:21] So I already discussed with you that how with markdown your AI is having the idea right? So if I write something like uh let's say brand this will be in a heading price. Okay. So let me add this

[1:34:32] to my project everyone. And now all the file all the chats which I will have in my uh this particular uh let's say project it will be having the context now 1% of the project capacity is used. So you can add tons of files in here and it will handle all these things referring to the file as and when needed. And now everyone if you want you

[1:34:51] can edit the details archive this delete the project as well. You can start the same as well instructions and everything I think were already provided. And now we can start just uh creating a chat for our project. So I just have to refresh.

[1:35:02] I think there was some issue but yeah now I think we can get just get started and I can say can you create a quick outreach email and draft email and draft for my uh let's say client in USA whom we are selling a voice agent solution via so taking a real life use case now it has all the brand guidelines and everything. This is where again it is taking all the instructions with respect to the main one. Now see before draft let me gather the key details. So

[1:35:39] this is I think coming from the main instructions identify client needs and everything. So it will go through the files everything as well. Client details VP solution specific tone preference all these thing it is asking me. So sending

[1:35:52] a let's say formal proposal uh I think we can have healthcare or medical should be fine. Short outreach email only. So yes short outreach email I don't want a lot high I don't want to use a lots of coupon uh sorry tokens but yes this is how your uh this will work everyone and if you will see it is asking us more and more questions so kudos to the main prompt which you write and it is genuinely asking the question which I think are very very important which maybe uh your receptionist or intern will also hire right so I can say that medical cleaning or hospital actually that is actually the case and it is lead qualification plus call handling Okay. And yes, these are

[1:36:31] actually the use case for which I have created the agent. So you can see that how smart it is. Do you have the client?

[1:36:36] No, keep it generic. So yeah, it got all the details everyone. I can ask it that hey it I think it will access the file altogether itself or I can ask that hey this is how you have to do it. I can

[1:36:46] maybe ask it uh please go through the brand guidelines to make it personalized. normally tries to access it uh nor like directly as well without my intervention but yes it is able to also you can also suggest that hey please refer to this particular file. So again projects are just a workspace where claude remembers instructions files conversation and related to a specific goal. So you can create

[1:37:14] projects for content creation research project for your clients for coding work for business use case all these things and as I said as an analogy you just have to think of them like folders in your AI workspace. So that is the best analogy everyone. Uh just to quickly remind you these are where project sits highly highly suggest that please make sure that you are using this uh for basically just categorizing your chats and everything. So if you have some chat

[1:37:41] related to a project like project is already created then please make sure that you can actually add from here as well. If I show you add to project you can add and change this from here as well. So that is the main idea. See chat

[1:37:52] remove from project chat move to project. So that is where everyone this gets very powerful. This small button you will see if you're having or connecting with a project it will show the project name as well and all the other things I think remain the same.

[1:38:06] But since it's a space where it has an idea it will give you a lot better results tailored with that particular problem. And over time when you will have lots of chat you will see the power of projects because even without you specifying the result the answers or the instructions which you will be getting right they will be tailored to that particular problem. So if I ask it uh that's let's say access that file and everything I think it should be able to hopefully I think deleting or like getting this has not done any problem.

[1:38:35] Okay so it is saying I already have the brand guidelines in context. Let me redra both email with full brand personalization project. So it is saying that hey it is adding the empowering business with intelligent solution that actually is the brand line if I show you. So let me just get the brand

[1:38:50] guidelines and if you will see here yeah this is the tagline empowering business with intelligent AI solution. So that is the benefit of project everyone I don't have to provide this thing again and again and I'm just telling you these things because since I am using clots more than here I am sharing with you the practical use case. So I'm not someone who is just learning few things and just telling no these are all the practical use case you see two versions uh anything which we can send we have the send via Gmail as well so should be not a problem and then again it is just telling that hey what all things happen my recommendation still stand go with version one for a formal proposal email to medical clinic it's sharper and of course it is asking if it want it can create more things so that is the whole benefit and everything with project everyone like a safe space where you categorize your work and everything so with the project clear everyone I think you will see that how powerful it gets now if you will go in projects and just select the project which you have created you can see all the chats in here right so now since it is having the context normally the more chats you have in here the better basically you will get the answers with time you can of course change the instructions if there is any new file any new guidelines any new uh let's say legal thing just add this into your files and the best part is that claude will handle the rest so giving you the responses inside this particular project you don't have to worry about anything. So as an example

[1:40:12] when I do use it for some communication I have already given the instruction that hey be formal be stern all these things we already handle and always remember this hierarchy of instructions that first one is your clot that is why it is asking you for the questions etc then it is the project project instruction and of course last one is the chat so if I will ask the chat to talk in Hindi of course it will first listen to this right so that is how this hierarchy goes and yes with project it gives you a way of very very nicely just organizing your life inside AI as well. So instead of repetitating your instruction every time you define them once inside the project and your chats live there as well. So very very less chances that you will be using either this search functionality or scrolling like this to get your chat. So that is

[1:40:59] the whole idea. Pretty sure that all of you must have also wasted lots of time in this. And on that note if you're using chat GPT Chad GP also has this project thing which you can use right.

[1:41:08] So if you will see homework writing it is having all the chat sources kind of in a similar manner. Now that is the whole idea right? So it can also add more context and everything but with claude of course uh the way we are understanding claudia this gets more powerful. So now with everyone now we

[1:41:23] have actually understand a lot in depth about these advanced concepts like artifacts projects everything. Now let's move on to the next step where we are going to learn about skills and I think that's the biggest biggest power of claude that is actually what caused majorly with claude being so good in terms of the brain or in terms of working on things and with this skills like how they have separated this thing this was majorly something which caused that repell in the Indian IT industry and others where we will try that we can now along with keeping our claude make it a lot more powerful in some skills and in this process everyone I have covered skills in a lot of depth. So we will try to create our own skills as well so that anytime we are doing some work where we want it to be done in a particular manner or where we want that hey whenever I have this request please please make sure that this gets done in this manner so it will be able to get your skills and also provide you a much better response and answer. So with that

[1:42:24] everyone now let's jump on to the next one which is your skills very very powerful thing we will make sure that we cover the same in lots of depth and we are also further making our own skills as well. Great everyone now let's jump on to the next topic which I believe is very very important and I would like to take a little different approach. Now I would like to showcase that why exactly this caused ripple through the industries and also explain you in an easy to understand manner. I saw that

[1:42:48] lots of people without understanding that okay skills are not that out of the box but yeah why actually they behave the way they do and make plots so powerful that would be my understanding because in that manner you will also understand that okay how can you actually make a skill and why they work the way they do okay so that is the whole plan everyone now first let's uh because I guess a lots of things have been kind of mixed up so far we have been telling claude what to do through prompts but what if claude can actually learn how to perform a task permanently Definitely that is the main idea. Okay. And that is what exactly skills do. Now

[1:43:21] I would also like to have a distinction here because that would be helpful. So prompts everyone were uh prompts were for quick task. Let me just get this thing and I will use the other images as well. Yeah. So now if you see prompts

[1:43:35] everyone were for quick task. Right. Then next we have project which are for your organized work and then we have skill which is a specialized capability. Okay. So this is what a

[1:43:51] skill is everyone. So this again is a very simple uh three lines to just have everything clear. Now if we talk a little bit more about skill everyone think about if you can just give a very very good instruction just like how you train someone right you train a employee or an intern. If you can do the same

[1:44:07] thing and that is what exactly skills are. So the main idea is that a skill is essentially a clot plus so blade of the cloud plus instructions plus the structure which finally gives you a specialized capability. Instead of writing the same prompt again and again we create a skills that claude can be used. So that is the whole idea. Now if

[1:44:25] you will see uh it is now present in the customize and of course that can move with time because earlier this was not there. In this we have the skills everyone where you will already see few of the skills. Uh many of them are kind of uh like not enabled which we can do.

[1:44:41] So brand guidelines for example we can enable it. I think it will be very helpful for us. And along with that everyone if you go on settings and in the capabilities this is also where I think you yeah this is where also you see the skills everyone. So you can go

[1:44:56] to customize. Okay. So I think they have just moved it here. know earlier I

[1:44:59] remember it being in the settings and yes uh more or less uh this is like a repository of what all claude knows now to explain in an easy to understand manner just think like if let's say we have an intern so say I just pasting it let me delete this yeah let's say that I have an intern everyone and now this intern has just joined and say that I ask that hey uh your role now is to make sure that you do this this this etc like so I'm giving it some multiple skills just like how we are having the skills is I am giving this uh intern also some user manual or how normally let's say a particular work is done I am asking it that hey go through this this is your user manual it already has a brain so just think of intern as a claude now of course we will learn about connector so it can have its own calendar Gmail LinkedIn everything and now with the instruct uh instructions everyone if you provide these instruction in a very very nice manner then the in uh this particular intern will have an idea that hey this is something which I can do and if like you have let's say a library of these different different skills and let's say that with time intern knows that hey this is where uh information instructions output format everything for a particular skill is left then it can refer to that when needed so that is actually what skill is in a simple sense so what clot does everyone is like let's say that if I choose canvas design as an example and again you can see many different different skill we will talk that how they are created and everything this particular skill skills.mmd file is having the instructions okay so it is not something out of the blue it is just that the brain is the same on top of that you are adding this file so don't confuse it like others are explaining it in a very difficult manner for you it is just if I have a brain icon then let's say this is the claw brain everyone and on top of this brain now you are just saying that hey this is the user manual and this user guide if you are asked to do something around this let's say the brand guideline thing then use this skill similarly if you provide and that is actually where you can provide and create skills for lots of things right you can create skill for uh reading excel for let's say creating word doc creating PDF creating website and each and everything you can just mention in there so this is what exactly happened you will see that these are visually instructions for creating design philosophy aesthetic movements that are expressed visually and that is all the skills which it use right so you will see skills creator so creating skill is also a skill right so earlier example I was watching YouTube videos now or let's say courses now I'm creating the same as well so again uh since it is a brain you can teach it to create skills as well right so that is the whole idea everyone now you will see that how we have the algorithmic art doc co-authoring mcp builder slack gif creator let's try to actually uh use maybe uh slack gif creator or uh theme factory web artifacts builder. We can just on of these skills and if I go back now to the chat everyone and if I like let's say have a new chat ask it to create a good Slack GIF based on all what you know about me.

[1:48:14] So I think this will be really good. I really hope it comes up with a good uh GIF. So that is the whole idea everyone.

[1:48:22] Now since again it is going through my personal recommendation everything now good thing that it is relevant like it is looking into the relevant chat and everything and I would want that all of you also do the same I think that would be really awesome right if want you can provide your image etc as well but uh with time once it gets the information then I think see it is able to get this thing and is that hey I will get some more information about you as of now don't see that it is getting anything so let's say yeah that is the case why one uh I think I'm funny and irritable where will you use this GIF most uh I think everywhere okay so maybe on WhatsApp and everything so now let's see when it will try to create since we have enabled that particular skill it will become a lot better in creating that because it is having that instruction okay so thinking about creating this thing see reading the GIF creator skill now it is having this information everyone so it is exactly like how you read the user manual and the guide and then you are doing the work in a much better manner and this is where actually it is very simple to create the skills.mmd file etc as well because in a way that they they are just having the instructions right nothing else so now if you will see installing dependencies it will be uh having I guess some v while python it will be creating the same so it is installing those dependencies pillow image io numpy everything and now it is trying to create one uh overall gif for So in the back end it is using Python and code although you don't need to be of course aware about this but yes I I like that I see that what exactly is happening in the thinking mode how this is moving because in future when you might try to create a skill it might be very helpful right so that is the whole way everyone now it is trying to create one let's uh wait and see that what it comes up with and in a similar manner so meanwhile it works you can go to skills marketplace claude and see see that there are lots of places where skills are present. Of course, Claude has given you a lot. Uh

[1:50:25] let's see them one by one. So agent scale marketplace you can go here and you can see ACP router pros one password MD Apple nodes right all of these are there business devops lifestyle I can select let's say devops and then it will show me the skills for devops and now I hope you understand because claude is so good as a brain so it is like a super intern and if you provided very very nice instructions then uh when claude introduced this with so good of an instruction it was able to perform very very nicely viously and it was like having a precreated uh intern with superpowers. So that is where skill transformed to superpowers and then of course uh that is where people thought that hey if it can do so much better if I provide and create these skills and create let's say my own agents or team then why would I need to hire people and pay them a lot. So this

[1:51:16] is everyone where the understanding and the mindset of skills and everything came into picture. So if you will see now again all of these cloud filler MD at the end of the day it will be some skills.md and other files. So you will

[1:51:28] see the name all the information and everything what exactly is present here. Now of course I think we can download the skills.zip. We can upload that zip

[1:51:37] as well directly and I think now many many different different AIs are also working on this. Similarly there is enthropic skills. So again these are the exact repository which enthropic has. I

[1:51:48] think if I will go on skills then you will see the skills which are already present right so let me go to lord and okay uh okay what it did uh okay very very strange I think it's all AI with me so can I have myself somewhere in the gif really hope that it doesn't uh affect the token limit and everything but yes uh what I was telling everyone is that if I open clawi in a separate one pay attention Then these are the skills which you see and in the back end right so they are not there out of the blue or maybe somewhere from magic no this is where these skills are present if I go into let's say uh which one are we using slack gif creator although we are able to see it there as well there is a skills.mmd sorry skills.md file the markdown file again okay so it is again a markdown file if you see it raw it will be all that hashtags and everything so I hope you are now able to connect that why I was asking you to give prompt and instructions in markdown right so yes uh this is again where all the things are present the bestest of the things if you want you can change it as well you can say that hey always give me the back black background or white background that all thing is easily possible but I want to demystify it for you and similarly there will be some requirements so I think these are the libraries because it is based on a coding part and if I go everyone to this as well collected 23 0 So let's check skills MP. Okay, I think this was the

[1:53:19] same. Yeah. Uh so yeah, there are lots of skills everyone. Just one suggestion,

[1:53:24] please make sure that if you are downloading a skill from the internet, uh please make sure that you read or had a read about it or maybe just ask claude or any chat GPT or any AI that there should be nothing suspicious. So it should not that it is somehow trying to access your file or sending because many people will say that hey this is the repository go and access from here. But in a organization as well as for a personal setting I don't want that any of your data gets leaked. So skills

[1:53:49] claude uh let's say repo I think some other repository will also be there awesome claude skills and you can see that so many of these different different skills are there right that's the whole idea that at the end of the day uh all these skills are for different different use cases and that is where again it was very helpful so for business and marketing now you can give this skill for data and analysis you can give this skill and again it was not that these skills are out of the blue no these are simple user manual you just got a very very good intern or a very very good brain in terms of clot so that is where the benefit lies it is not that if you give the skill file to maybe some uh let's say small AI or some local AI it will perform similar to claude though it has an effect because it is telling you exactly how particular thing has to be done but combined with the brain of claude this combination is deadly so that is the whole idea everyone a skill is like training claw or uh to do a job. Okay, so that is where it is very very helpful. Without skills, we will be repeating the same prompt, summarizing the images, writing content, generating reports, all of these different different things, right?

[1:55:00] So, uh pixelated version of me center. Yeah. So, that is the whole case everyone. Skills turn claude from a

[1:55:08] conversational assistant into a specialized system. And that is where these things are uh taking overall advantage and claude becomes very very helpful. further uh okay just okay let me let me do one thing let's let's get a little bit more crafty let me try to upload one let's see that how it will okay so yeah so that is where again using cloud in a fun way but of course I hope you get the idea and now everyone what you have to think of is that what are the day-to-day jobs which you do what are the skills which you have what is your process and just give all of that by creating a skill already of course few skills are present. I told you how you

[1:55:49] can download the skills from different different places as well. And what effectively a skill is, right? And if you will now go to claude and say plus, you will see three options. Create with

[1:56:02] claude, write skill instructions, upload a skill. Now from the websites as well as when the claude will create you can download them in a skill file or like MD. Basically it depends like it sometime it has more files as well and I will be g going a lot deep in claude code video in this but the main idea becomes that okay claude at the end of the day wants to just have these instructions. Claude doesn't care.

[1:56:26] Claude says that okay just give me these instructions and I will be all good. Now either you can upload the instructions either you can write it down or you can just talk with me and I will create the same for myself. So that is the whole idea everyone. Now I will show you all

[1:56:41] three of them. The main idea is that because skill is very very important and if you create skills for your day-to-day work uh each and everything use all the things which I have taught you till now in terms of project in terms of how to use cloud effectively then I think yes this can go to the next level where like of course claude will perform a way way way better than how it is performing right now. So with that let's see what it has created.

[1:57:07] Okay. So I I am pretty hopeful that it will create a pretty good one. That's the main thing with claude. But yeah,

[1:57:12] that is how it happens everyone. Now for the time being, let me try to see. So if you see skills.md examples resources

[1:57:19] like again ideally we can include everything in a single file as well. But of course the same is very very helpful if you have different different files. So it will just have the information and everything. Let's see that how can we

[1:57:32] download the same download the skills try the sample data and yeah so let's let's download this skill everyone CSV data analyzer okay let us see this let me download from here save so very very small file as I said right it is just instruction nothing out of the blue let me save it them here and I can cancel it close this and if I upload a skill now I can just drag and drop this most probably it will work right? If you will see again if I have the uploader skill empty file must contain skill name and description formatted in ML. So ML is also a format just like markdown. YML is

[1:58:12] yet another markdown I think something my bad. How did how can I forget it? But uh yet another file what is it? Yeah, yet

[1:58:21] another markup language or YML markup language. So again it is used in a lots of places with docker and integ. But yeah either you can give it that or you can give it a dotzip or a dotskll file. Okay. And of course each and every

[1:58:35] one of them should have a skills.mmd file. It in case is having the resources and samples as well. That is the main

[1:58:41] idea. See in the readme it kind of gave few things right. So join our community all my links. I can click show image. It

[1:58:48] is an external link. So maybe this is something which I need to get uh not pass unnecessary right. So that is why I said that it will be good if you not always try to just get the skills from outside without reading that can have a little problem. Similarly there is

[1:59:04] analyze py. So exactly the file has been given requirement.txt has been given and of course the skills empty which is the main file and believe me this is not something out of the blue. You can

[1:59:15] create one altogether something which we will be doing. So next is write skill instructions. So I can say skills name mayank test skill.

[1:59:25] Uh description you are a test skill that always listens to my is awesome. Now again I know that it's a throwaway skill. Of course I can go to chat GPT and claude rather only to provide me information. I could actually

[1:59:44] do something like this as well. I just give this and if I go to chat GPT open a new chat paste this give me above for a skill on creating a post on YouTube for my new videos. So again just give it to chat GPT tell it that okay at what level you want it it will give these things to you. So YouTube post creator YouTube you

[2:00:12] are a YouTube generator and everything and now again see how nicely it is kind of able to give you all these things. So that's the benefit if you're able to tell AI now what you want more or less every AI supports that hey I will provide you that in a best way. So that is the thing which we have to learn as well everyone and this is where as I said uh this becomes a lot powerful right so AI as a tech or skills overall becomes a lot powerful uh okay I think it has still not working uh okay maybe tokens are out I hope that's not the case but yes uh that is the way of adding your scale let me copy this thing up so this one is the main one copying it here then copying this here although I will highly suggest not to do like this uh the next is the main way through which we can create skills so create one and more or less it is created because at the end of the day it doesn't need anything you can provide other things as well with skills.mmd but skills.mmd is

[2:01:12] the major file which it looks forward to right so we have seen everyone two ways now just to circle back user task document data idea which is a problem to solve clause skill instruction structure output put rules uh files okay requirement.txt txt any script, Python script, any other basically code etc as well. And the idea is that the output will be consistent because of this consistency because again you are sure that okay and Claude has made sure of that that's yes once it accesses a skill then it will be performing in a very very good manner. People thought that

[2:01:48] hey why are we paying so much for let's say a content writer a legal adviser or anything and that is what caused that hey if we can and of course with claude co-work and other if we can have so many of good skills and claude can do them a lot better in a consistent manner so consistency was always the issue in here we are always telling and again these are kept as a repository as well many of you will think that hey man why can't we just copy and add these every time before the chat. Well, you can do that. But the power that it is kind of stored as a library, right? So, this is the

[2:02:24] kind of like a library where you can uh own a skill off a skill where you can also further make sure that uh create your own skill and it can access a skill when needed. So, it is not that it will be uh let's say always having this lots of context. It will not be sending all these skills. It will just have a look

[2:02:45] before doing a task that hey if I have a skill for this if it has and if you have turned it on then it will try to go with a skill something like which we human will also like to do right. So if I have to let's say create a video then of course I have a skill for it. I know that okay I have to use mic I have to use uh camera I have to record and say like this. So of course I will use that

[2:03:03] skill and that is the whole idea and I can teach you that skill as well. So think always in this real life analogies don't make it confusing with out of the world explanation. Okay. So this is

[2:03:13] exactly what skill is everyone. Uh let's see if it has created or not or it is not trying to create one. Uh I think it is trying to create one. Let me delete

[2:03:22] this photo for the time being. So seems like it is trying to create one but uh yeah maybe it is having some issues. It is saying it's done. So

[2:03:31] hopefully it will try to give it in a bit. But parally everyone we can now try to create a skill using the last way that is create with cloud. Now I will like to show you the GitHub and in this GitHub if you will see the skill creator GitHub it will also be having see agents assets eval viewer references script and skills.mmd. So Claude of course has done

[2:03:54] lots of work. You can also write a skills creator MD but of course the better context the better instruction it has. That is how it will work right. You

[2:04:03] can play cricket. Virat kohli can play cricket. Virat koh koh koh koh koh koh koh koh koh kohi will be a lot better because it has more skills more techniques. But yes if you can extract

[2:04:11] virat kohlies and get into you that is like how what claude kind of as does right. So if you will see skill creator and everything communicating with the user please pay attention to context cues to understand how to phrase your communication in the default case just to give you some data idea sorry evaluation and benchmark are borderline but okay for JSON and assertion you want to see serious cues from the user creating a skill capture intent interview and research write the skills empty skills writing guide so see this is how Claude is saying skills empty yml for front matter name description required markdown down instructions. Okay, this is what skills MD should have. Bundled resources which are

[2:04:49] optional scripts, references, assets, something which we see in other skills as well, right? And yes, progressive disclosure domain uh references AWS, GCP, Azour. So things are very very categorized in a very nice manner and the best part as I'm I will repeat it again and again it is not that this is something which we were not doing earlier. We could have done that. We

[2:05:10] were doing that. But with the overall strongness and smartness of clawed brain clawed models like opus and all these things it is able to give us in a very very good manner. So sonnet opio they are pretty good with that right. So that

[2:05:23] is where it gets helpful and yes let's see the agents as well. What is in agents analyzer comparator grader. Okay so it I think will grade evaluate expectation against execution script and outputs. So yeah I think it will just

[2:05:35] run on that. It's a pretty long process of course and then it will try to create your skill for the timing. Let's go and create a skill. Let's create a skill

[2:05:43] together using your skill creator skill. First ask me what the skill should do. So this is a starting line. Of course

[2:05:48] you can say that hey let's create a skill using skill creator. If in case you have multiple skills which are very near to each other everyone I think it's of course a very very good habit to just provide the name of the skill. Right. So

[2:06:00] though we saw that how it okay uh oh okay I think it has done a good job. That's pretty good. And yeah, if you will see here, it did got the access to the slack gif creator skill. In case if

[2:06:14] I have multiple of them, of course, I will make sure that I use them. Okay. So, let me download it. I like it

[2:06:18] honestly. And yes, then we can easily use it somewhere. So, see AI mode on. I

[2:06:25] think this is the one which I will maybe post on YouTube because that is the next skill which I'm creating everyone. So let's go here and say uh okay 1 minute yeah just a second I want that you create a skill using which I could create post for my upcoming videos which I have shot on YouTube on YouTube post LinkedIn internal groups which I have and overall any other communication which I ask you to the YouTube and the LinkedIn post should have a very very good hook line and should explain the video in a very easy to understand manner plus have the pointed summary so the person who will be a potential viewer gets excited and intrigued to watch the video. On the contrary for the internal groups I want that it should be not more than 60 to 80 words because there I have a limit and such long messages will not work.

[2:07:28] Further you have to make sure that you research and get the best practices for LinkedIn and YouTube so that you are able to write a post which actually resonates with the people and also let me know that what kind of images etc should I include or attach when I'm trying to post them. The idea is to make sure that the reach of my video gets increased because of this. So everyone again I will be creating a skill live. If you have done that or if

[2:08:02] you get the idea you can fast forward it but for majority of the people I think they would love this uh whole thing in depth. So that is why I'm doing this now. Yes it did also ask the same and everything but I am just kind of creating it by giving it the instruction and that is where AI has become a lot smart now as compared to 2 years ago.

[2:08:19] Lots of context it already has. It will be having all these things. It is saying that hey don't worry about being too precise right now. Even a rough idea is

[2:08:26] enough to get the conversation going. I will ask the follow-up question to unsharpen it. But now you know that why it is asking those follow-up question.

[2:08:33] Right? So it is from here that it is asking these follow-up question. This skill is having a very very good this multiple files which tells that hey this is how you have to create a skill. So

[2:08:46] now again it will ask a lots of question and that is one more thing which I like about cloud like it's a very good stepby-step thing right. So it's saying uh also an open thing I would love to know do you already have an existing skill file that I can see in your skills folder? So I would say that I am Tekken AI for LinkedIn uh build or both equally.

[2:09:08] What info would you provide when using the skill title of description full script transcript key point bullet points? These are the thing mainly I will be invoking this inside a chat where I have worked on summarization or resource or resource creation of my video. So again I'm explaining each and everything to it that is very very important. Next. And I

[2:09:40] think it will ask me again because I don't want that it use use this YouTube post creator. That's not a very good thing. I will say uh avoid the YouTube post creator skill or I think it is trying that good. The existing skill is

[2:09:55] quite basic. Let me also check your LinkedIn post skill. Do I have a LinkedIn post skill? Yeah, I think that

[2:10:00] was internal. So if you will go in customize and skills, there was this LinkedIn post. uh both of them actually I want to honestly delete now let me try to okay and again everyone this is one thing which you can also see try and chat download if you want to share it with someone if it works pretty good it's pretty good edit with clot replace and delete I I would like to delete it let's see that okay how it works because again our that chat has an access now let me see uh okay you mentioned 6280 okay uh what platform are internal groups on affecting WhatsApp uh it's an internal edtech platform also I meant 60 to 80 words so don't miss out on these things everyone when I said 62 80 like 60 to 80 okay yeah so it picked up this thing okay it's a roughly 25 minutes read uh not 6280 so you have to handle and see these mistakes as well right because once you have created the skill then it will be used And you will be feeling that hey this is a very bad uh overall feature why taught us that it is giving me this big of a problem right so make sure that this is clear also please create from scratch using your in-depth research and I have deleted the earlier skills you referred so hopefully it will be able to join all these things I should have provided this separately But yes, this is actually everyone the main thing. This is where you have to

[2:11:38] spend a lot of time because once you have created your skill effectively in a very very nice manner then of course this is the way it will be used right. So uh yes should that skill also generate a YouTube video transcription SEO tag? No. I I would like to create

[2:11:51] another one for that. Okay. So now you will see that how it will go through the same. It will be user want me to create

[2:11:57] a brand new skill for Tekken AI YouTube channel platform uh no YouTube description all these things. Okay. So it got these things. Now let me go deep

[2:12:05] on best practices before writing a single line of the skill. This is a foundation. So you will see like it is searching the websites. Now and this is

[2:12:12] what I said everyone this is something which used to take us so many time and this is something which we used to follow right to create our own skill uh that if I want to be a very good LinkedIn writer I will search on the web. But Claude is just doing that so nicely for you. And now see video promo post or video promoter and see I have everything I need. Let me build the

[2:12:31] script from scratch. comprehensive research back in production edity and though I am also using a mix of cloud and chat GPD this kind of features if it works pretty well right of course I will move to this because as of now uh what I do is I have a chat open which kind of gives me this thing whenever I copy paste the information about the video or transcript now I can invoke the skill in any chat altogether so this is where this kind of skills and everything is helpful everyone as of now I have just provided a use case which like related to me which I do every day for you as well. I think this is what you should do right. This is what you should try to

[2:13:08] do. See where you are spending a lots of your time and then try to create a skill for yourself and once you have done that it will be called based on the usage just like how you do and I always say this thing to demystify the AI and everything. So meanwhile it is creating let me talk about that as well that all scientist all people are trying to do even the smartest one are just trying to mimic how we normally work. I have a

[2:13:30] skill I use that skill I have developed that skill. Let me add that thing to claude as well. So next time if you want to maybe wonder that hey what will be the next thing just see how you do a work or how humans basically do because at the end of the day we are creating artificial intelligence uh which is very very much motivated by human intelligence. Okay. So see it is

[2:13:51] packaging the skill and everything everyone package skill with correct output path. So this is again all the part where it is understanding the scripts and everything. Most probably it will create a skilled file. So let me

[2:14:01] show you that. Okay, it was here. So, see it is giving me a video promo post.

[2:14:09] It is telling everything. 150 care hook engineered for the see more cut off link link placed in the first comment. Avoid 30% reach penalty. LinkedIn applies to

[2:14:16] post with external links. Okay, so I was not actually aware of this as you can see. I thought that people normally give it in the first comment because uh LinkedIn doesn't shorten in in that manner but yeah uh 1500 to 250 character for dwell time bullets hashtag only at the very bottom internal hard 60 to 80 words limit zero markdown warm personal tone it also includes a visual checklist after every prompt exactly what images or clips to attach one thing I need from you the tone question you didn't answer yet I assume mix of casual insightful as your personal brand tone so it has an access to that as well if you're actually more energetic and punchier professional let me know and I will change it now everyone you can copy to your skill and let me refresh see video promo boost you can rename it and everything of course and I think yes so it is just having this thing and if you want you can download it as well as I said it's a skill file something which claude can open so internal claude file but I think and let me let me try to do it maybe uh let's say open uh txt file or something. I think more or

[2:15:23] less it will be having instructions only like let's let's try it is unsupported file format or let's say open a file in notepad so ideally you can open it with anything right so or or let me do one thing I think that will be better let's have this let me go to VS code in here let me have it here uh open anyway text editor okay so seem like not that straightforward which I was thinking it has done something. I thought that in the back end it will be having the same kind of a thing but that is not the case. In that case everyone this can be opened by your claw desktop app. So if I

[2:16:03] just have it here and if I just go to claw desktop app if I open customize skills I think I will be having this. Okay. Uh I think it has not refreshed.

[2:16:12] Let me refresh it. Skills. So see video promo skills but I can upload a skill and it support this dotskll file here.

[2:16:20] So dots skill file is supported which will of course be having everything. So that is how you share your skills if it is working pretty well and maybe we are going to enter a era where you are just sharing the skill file over WhatsApp or something right. So that is the whole case everyone pretty sure that now in and outside of the skill is pretty clear. Let's try it out as well. Let's

[2:16:39] let's try it out. Uh say open a new chat. I am creating a video on mastering clawed AI covering each and everything in depth.

[2:16:53] Can you please give me posts to promote the same YouTube LinkedIn personal? Now I could have mentioned the that use that skill and that is something which I will actually do in future but I just want to show you that how it is very quick right it updated the skill and now it will use it. So see reading the video promo post skill this is the skill which we created right so it is having the skills domd and it will follow that instructions before I deep dive and again these instructions are coming from our main instruction which I would like to keep so it will ask the questions every time so that it can give you a much better thing right what's the one thing that makes video different do you have a YouTube tutorial yet so I will say covered all the above in a easy to understand and practical manner. I think it's

[2:17:47] surely 1.5 plus hours and have kept it really practical. Okay. So, I'm not

[2:17:54] talking about the hype or something, right? I'm I'm showing you charge GP as well and everything. So, do let me know if all is good. Uh all of the above

[2:18:04] still in production. I think we we would be needing it after it's live but still it's fine. So now again everyone you will see that how since it is trained on that skill it is having that idea YouTube community post most clot tutorials scratch the surface this one doesn't I like it most people are using clot at 10% of the profession uh this is also good it talks about this video pretty nicely which I always miss out and see it is saying full video dropping soon on YouTube and hey everyone dropping a big one soon a 1.5

[2:18:31] hours complete master class visible checklist okay sure this is done use a bold thumbnail style image with uh okay yeah text masking cloud AI on your face high contrast work best if thumbnail isn't ready use a behind scene recording that is also a good suggestion actually 15 to 30 minutes second vertical teaser clip if no clip add a clean graphic plain text is fine once since the video is still in production post the LinkedIn and YouTube comedy poster teasers now to build anticipation then hit the group message the day goes live the two-way approach tends to drive stronger day one numbers so again it is going far and beyond right everyone so yeah that is all around the skill as I said I have create creat created one from scratch with you. I have shown you the skills marketplace and the library as well. What you have to take care there. The

[2:19:15] internal skills how actually they get created. So all of those things we have discussed in depth and I think that is all you need to know about skill. Just one thing more uh though we have covered not discussing about claude code cloud co-work here but in claude co-work everyone we have something known as plugins uh kind of like skills only but these plugins internally they are having the skills as well. So see skills and

[2:19:39] connectors. So see all these different different things which make your skill a lot better right? So you have to connect with your day-to-day apps. So that is

[2:19:47] actually next thing everyone which you're going to discuss. So let's now I think we have mastered skill way way way better than like you would need to. So with that let's now move forward and let's move on to the next part. This is

[2:19:57] all the skills system. Okay I created this as well. So if you will see user request skills definition instructions input format output structure output structure this is all the things which kind of gets created in skills.mmd claic

[2:20:11] core is a skill selection empire does the skill exist for it skill activated claw reasoning structured output report checklist dashboard post uh it also get the context input as well so the chat or any other thing if it will need and in the next part when we will connect it with connectors for example you ask that I go through my emails and then uh give me a summary. So it will be able to access your email as well if you have given it connectors right that is where it gets very helpful and finally you are giving a specialized result. So YouTube metadata, meeting summary, market analysis, skills allow cla to perform complex task very very consistently and that is where everyone's skill is like the most most helpful. Okay. So yeah, I think we have

[2:20:53] done skill in a lot of depth way way more than required and if now as a work for you I think you should now make sure that you are using and creating multiple skills of things which you do every day. Once you do that just like I did today, you will see that hey how Claude is very very good in helping in day-to-day task and that is where you see the real difference. So I don't want that you see this tutorial and sit on hands that hey all is good I know Claude and everything. No create these skills the

[2:21:21] way I'm creating give it multi maximum context maybe take a hour to create a skill but once that gets created see that what difference it will bring. Okay so with that everyone now let's move on to the next part which is cloud connectors and MCP. So in this we will see that how it can connect now to different different tools. The core

[2:21:40] layer becomes the MCP only but again I will keep it very simple not going in technical and everything. The idea will be to understand that why it is helpful and how do we connect different different apps. Plus from the security endpoint what and what permission we might or might not want to give to claude as well. Okay. So claude is not

[2:21:56] at the end of the day some safe heaven. It also can make mistakes. It can also cause some issues in your data etc.

[2:22:02] something which I have seen and thus it is very very helpful that you understand the connectors and MCP and everything in depth as well. So let's now move on to cloud connectors and uh complete MCP architecture or rather the way MCP helps you to connect with this particular uh different different tools. So great everyone now let's move forward and now let's try to understand claw connectors and MCP as I said we will try to keep it very very easy to understand because I think that many people are kind of afraid of MCP or they don't understand the same though for the same I have created a very good video which you can refer uh now let's try to see that okay where these connectors will be helpful now up till now we have seen claw like we have used it for I guess lots of things and we have seen that how it can analyze information generate tools create skills and other use them and of course reason about our problem ask us question then provide a very good answer but now just think that uh if you hiring an assistant or an intern like it is very smart okay so the intern is very very smart but if you say that hey can you please check my calendar and tell me what meetings I have or hey can you please read through the files which I have or based on let's say yesterday's meeting or with the tools you use right so that is where now I guess from AI to kind of agentic AI we are making it in an agent where it can interact with your day-to-day tools as well. So your daily

[2:23:26] tools like Slack, uh Gmail, Drive, Sheets, all these are the tools which we would like our clot to uh access to and of course that will make it a lot more powerful. So let's say that if you give it a request that hey uh summarize sales spreadsheet then instead of you providing that spreadsheet uh every time uploading it like of course that is also a added effort cla because it will be having the access to each and everything like it will be having the connectors maybe skills etc. it will be able to via the MCP protocol. Now we will again come

[2:23:58] to this that how exactly this happens connect to your everyday tools like Google Drive, Slack, database, local files and even APIs as well. And then of course if it has more context so after that if it gets the cloud request MCB server connect to external tool it will get the overall context and whatever data is it need and then provide you with the result. So much like again just think in terms of an intern or an assistant. Don't make it complex with oh

[2:24:24] hey Claude also has this feature. No. Now of course you will get the answer which is way very way good and on top of that for many tools it supports uh writing information as well. So you can

[2:24:34] say that hey do the analysis and maybe save as a file though we will like to have that access a little bit in a control manner because I don't want that you lose out on any of your file or let's say that it deletes any of your file like something which happened with me. So that is what we will have to uh avoid everyone. So now let's move forward and let me show you the connector tab as well. So in the

[2:24:55] customize there was skills and similarly there is connectors as well. Now you will see that how I have connected lots of tools or like overall applications already and of course we can like connect more tools as well. So let me select Gmail here and let me connect it.

[2:25:10] Now uh again it will just ask that hey connect plot to Gmail and everything. You can click continue. Then you can select the email id. I'm selecting the

[2:25:18] first one. Uh let it load and I can continue. So normally again it is asking that hey see three services that cloud for Gmail has access to. Let's see this.

[2:25:26] Uh see your primary Google email account that's fine. Uh associate with your personal info. So of course it will be getting your data and view your email messages and settings. So if you will

[2:25:35] see and this is very very important any application wherever you are giving access to please make sure that you read what uh overall permissions you are giving in here. it can just view my messages search and view the settings. Okay, so it cannot be able to send it and you should be aware about this. It

[2:25:52] should not that you promise a client or you create a service where you say that hey uh since it can connect to Gmail it can do everything. Well, that is not the case as it is right in front of us. Though I will show you that by creating our own MCP server how that can also be doable. Okay. So with that everyone I

[2:26:07] think we can close it and click continue. And now Claude will have access to my uh Gmail as well. So if you will see here uh get Gmail profile which is my profile list Gmail drafts all the drafts list Gmail labels read read search and create Gmail draft is something which is in the need approval part. Okay so these are all the

[2:26:27] permission which it has. Now again I highly suggest that you just check and give the required uh level of role here always allow needs approval blocked. Okay. So if you don't want that okay

[2:26:42] your full application or your all the emails get access to maybe maybe you can block the same or if you don't want that hey it is able to read your Gmail threads maybe block the same okay and of course in a similar manner we have the Google calendar as well write or delete as well read only we can collect any notion we can click on plus and we can browse connectors as well and you will see a lot many different different everyday applications right so this is where it becomes a lot powerful So of course we will have to make sure that we are very very uh carefully selecting which app and which permission we want to give but yes clot does support all of these things uh directly out of the box and I think there are more apps than you can think of and of course we will talk about custom connector and MCP as well and uh like on top of that everyone uh let me first show you the let's say an example so let me go to new chat and say uh hi can you tell me all the events uh one week from now from my uh calendar. Now one thing to note here uh when you have a query like this and I I do this a lot like if you know that hey I will just be connecting to a particular application maybe you can just avoid others right so you will see that okay Google calendar and everything are already there now for the time being I'm having these all but we can see that hey uh we can just uh turn off some application which we don't want because uh if you have let's say 10 plus applications connected they all will be sending some information to clot and that would lead to a lots of token usage. So some advanced level or expert level things I'm telling you here because normally people use all lots of tool then they get that hey uh the free limit has expired please wait some time and that is something which I don't want just give AI what it's what that is the main aim to make AI work better if I even give you lots of context like if I start discussing Gemini chat GB everything in here you will also get confused in a similar manner keep AI uh with only things it needs okay so for the timing let's ask the same And now hopefully because it is having connections uh it will try to load the tool. See

[2:28:55] loading tools request result list calendar events request it will give the results. It look like uh calendar is completely clear on March 24 uh 1 week from today. So uh I can check can you check every day up to 1 week if I have anything. So again uh either

[2:29:19] it will use the results or it will try to get it again. Let me show you uh let's say calendar as well and we will try to create one as well. Okay. So

[2:29:26] let's say Google calendar. Okay. So I had a meeting yesterday.

[2:29:30] Let's let's create a meeting here. Okay. So awesome cloud code. Okay. Say our next topic is

[2:29:37] going to be cloud code everyone. And now of course uh when our cloud will run it will be able to give us these events. So let's see the same. And yeah see awesome

[2:29:44] cloud good like I think I uh created it first and then I it got got to the request but yes that's the only scheduled event and all these days are completely free. I can even ask it create one uh this Sunday where I have to take a class and also uh let's say Thursday where I have to create claude code video content. So I'm just telling or showing you how it is actually useful. Now of course it will try to

[2:30:19] have the right access. So it will try to create those event as well. As I said, please make sure that the write or delete access you are kind of uh very nicely handling. Okay. So that is the

[2:30:29] whole case everyone. So again it is just asking let's say um evening 6 evening afternoon 2 and let's say I can say 30 minutes. Okay. So this is uh this

[2:30:41] is one thing which I like a lot about cloud code like how it gives questions like this and of course our main uh prompt which he gave that also has a very good role to play in that. Okay. Normally it might ask in here only. So I

[2:30:51] could say always allow that should be fine. And now it will try to create calendar event and I will show you that how they have been created. So let us refresh.

[2:31:00] One is created. Sunday Sunday Sunday Sunday it is created. Okay. So yeah

[2:31:04] that's the real u like immediate use case everyone. Now along with connecting applications on the web version that is right now we are using it in a browser. You could actually go to claude in the application. So if you remember I showed

[2:31:19] you that how you can download clot and now again it is on the free version only right. So it is nothing to do with the paid version. Then in here as well everyone if you will go and go to settings so they will be more or less the same but in the connectors here right you will see uh all these applications all the different different applications and there is one more part.

[2:31:42] So I I would just like to explain it first. So see connectors are everyone uh things which we are. So one minute we just uh okay how do we okay so one is connectors everyone of course connectors which we are able to uh easily connect our application then we have the extensions something known as extensions as well. So again they are also very

[2:32:06] very similar to connectors just that they can connect to more application and majorly inside your uh machine as well. So because this particular app right this claw code it's running on my machine running on my laptop it can connect with tools etc inside my laptop and those are known as extension so you will see desktop commander Google chrome connecting or like kind of running your Google chrome let me have this uh let's install it then read and write Apple notes so if you're aware Apple notes is not something on the web notes kind of on my machine only on my Mac only then Figma PDF tools analyze extract fill compare let's install this as well now in a similar manner again tab view poweroint bythropic control Microsoft PowerPoint with applescript automation so again the reason it is Apple script automation is because it is going to run inside my machine okay so yeah I think there will be lots of these apps everyone which we can try out and the majority we will be interested in iMessage as well as you can see read need iMessage something which I hope you know that again it is not something kept on the web that is why they are extension. So this is the difference between connectors and your extension. So again

[2:33:23] this is how you can make sure that if you are using the cloud application not only will it connect to your uh web apps but it will also be able to connect to your day-to-day apps and that is like day-to-day uh machine apps right and that is what makes cloud a lot powerful. Instead of you going to cla you going to login and everything you open this application and it will be having our connection to everything. Okay. So with

[2:33:44] that let's close this. Uh okay. I think uh we have not added the PDF one. Let's

[2:33:50] install it. Uh let it install because I think I clicked back and then it failed. So it has been done. Powerful PDF analysis

[2:33:59] toolkit for cloud desktop. So again very very important to understand because many people get confused and see them similar connectors or extension. No connectors are for your application extensions majorly work with your uh applications which are inside your uh laptop and yes of course that is only present with claude desktop right because claude from here from the web it cannot directly read my iMss or connect with my Apple notes because they are residing on my laptop. Okay. So with

[2:34:28] that everyone let's move forward. Let's let's see uh let's have the Apple not should be fine. List notes, get node, contain, add node, all these things are there. And of course like there can be

[2:34:39] desktop, interactive, web, all these things are present. You can select the web one as well. So Gmail, Google calendar, I think Google calendar we have connected. You will see others as

[2:34:47] well here. It is entropic. Connect Gmail to cloud quickly. So it is I think the

[2:34:50] same one. I can refresh and it will be already done. Let me refresh it. So I

[2:34:55] connected the Gmail on the web but didn't refresh it. Right? If you go on browse and if we now see Gmail, it will be there I guess. So let me say web. Now

[2:35:04] see Gmail is there and if I select desktop then these are all the one which are based on the desktop. Okay. So with that everyone let's open a new chat and let's try to use the Chrome one. Let me

[2:35:14] have it here. Uh normally I don't use Chrome as the default browser although I think I have that installed but let's see open Chrome and please tell me the latest AI news. Okay so this is something which I can ask it and uh again uh that is like let me just talk about a little that why connectors exist. The idea is pretty

[2:35:33] simple. Traditional AI models are limited to information which we provide them. They know the training data at the prompt and everything. But with uh let's

[2:35:41] say connectors this thing helps you to overall be a lot smart overall work with your tool and that is where I guess the main agentic AI or uh AGS I think. So uh that is kind of comes into picture right where they can actually not do something. So I think it has open chrome. Let me see. Uh seems like it has

[2:36:02] opened one. Let me have it on the other screen. Yeah. So see everyone this is

[2:36:05] what like it has opened. I think uh Nvidia GTC agent stage uh I think it will be somewhere here only and I can maybe ask it that okay uh let's let's ask it some more things at least incurs 10% metamals Morgan Stanley everything right. Uh let me let me ask it some more thing. Can you also go to

[2:36:28] Google and search about latest stock report on sale media? Okay. So let's see and understand this and how it will do it. Now again I'm not

[2:36:42] controlling it as you can see uh my hands are totally free. Uh this is all being controlled by uh claude desktop with the help of of course my cla right. So I I covered the same thing in plot cowork as well but yeah this is how it kind of works. Of course it will be

[2:36:58] taking a lots of token here because it is opening the same via scripts or something then it is trying to get the results and everything and see uh then I opened the Google search for Nvidia. Here's the comprehensive breakdown. Uh if you are feeling that hey now everything it will be able to do uh of course it is still limited so maybe a year or two we have to wait uh before they start doing our work on the browser. But yes overall if you will see

[2:37:20] it is able to do all the things which we are asking it right if I ask it for YouTube for a particular website it can do that in the back end and see again it is easily connected with Chrome right that is the idea now I can also say can you tell me how many PDFs I have in my downloads folder so let's see this time which tool it will use most probably it will use the other one so see accessing local Uh I don't have access. Okay. So it is saying I think yeah I don't have direct access to local 5 system but I can check your chrome downloads page. So I think

[2:37:56] no that is not the thing which we need. IDE we should be providing it with that. So let me see uh add files add from project u style. No. So I don't have

[2:38:06] that I think. Yeah. So it is opening mac terminal. Okay. So it is saying that hey

[2:38:09] you open mac terminal and do this. But maybe I remember I had a extension here as well. So let's let's go to settings extension and advanced setting. What is this

[2:38:25] advanced setting? Okay. Enable auto update for extension. That is fine. Use

[2:38:28] built-in node for G MCB. That is all fine. I can just select the file subsystem or something.

[2:38:36] Oh yeah. Okay. This is the one. So if

[2:38:37] you see desktop commander uh you will be having a similar one in Mac uh Windows as well, right? So combine local file system access with full terminal control. Now it was saying that hey why don't you access the terminal and if I can access the terminal and if I give my claw that access then I think it will be able to do the same right because if you write something in the terminal let's say if I go to downloads then in this manner I'm able to get everything right so that is the whole idea everyone now it has been installed. Let me now go and

[2:39:06] open a new chat. And let me now ask can you check how many PDFs I have in my downloads folder. So uh again it becomes very very powerful in your day-to-day job like of course if you are working and if you have access to claude this becomes a lot powerful right. So that is the whole aim

[2:39:27] everyone. So see claude want to list PDF I can allow it and now since it is having access in the back end it will run. So see you have 399 PDF in your download folder. We can see that I'll

[2:39:37] use the latest uh PDF tool list PDF. And now since it has the access it is able to do that. One more thing which I would like to show you here everyone that if you go on customize in here you will see plugins as well. Something which is not

[2:39:51] present in the web version. So see no plugins here though I've covered the same in the overall let's say or claude co-work. The idea is exactly the same.

[2:40:01] These are also now skills plus connectors. So plug-in in a way you can think of skills plus connectors which helps you to do the job right. So skill uh let's say if I give it a very good Google chrome uh skill. So then it will

[2:40:14] know that hey I have to connect with Google Chrome. In a similar manner if I have let's say engineering as a skill let's see that if I add engineering as a skill and of course this is something which caused a lots of disruption in the skill it is architecture code review debug documentation everything. So you can you can already see that how these are all the things which a person does and in the connectors we will have everyday apps. So slack, notion, pager duty, data

[2:40:37] dog, atlacian, asana all the apps which you might need. So if you connect this in a way you are creating your virtual engineer because you also are doing the same part right you also are having lots of skills and you have the application. So this is how again Claude thought that hey if I want to actually achieve AGI then I have to see how a human work and that is how all of us work right if I have some task let's say slack then I can connect to slack see the task and then just reply to that based using the brain and it will understand that hey which skills it want to use and that is the reason if I just show you uh let's say atian stock sorry not atian in no infos as essential stock like why it is falling I think it recently gained something but in the one or 6 month you will see that how it has fallen a lot then similarly TCS 6 month fallen a lot and that is actually a lot right so 1,000 around 1/3 overall it has fallen over the last so 24%. Similarly uh Infosys

[2:41:47] 6 months 19% it has fallen. So I hope you get the idea like because these are actually all the task which earlier human used to do and that is where these consulting companies were charging right. So they were saying that hey we will get you the human we will get you the resource you pay them but now uh 30 40% of that task it is easily easily being able to do by very very smart claude or AI brains and of course if uh Claude has came up with this other AIS will be in the line coming up with the similar version of their skills connectors everything they also do have that just that Claude did a very good marketing and did a very good job at creating that brain so that is the main idea everyone now if you go on new chat uh this is also the same interface more or less uh just that if you have the paid one you will see co-work and code and you can see all these different different apps you can see the same kind of uh style everything here if you want you can change the style and all so that is all everyone now let's try to understand few more things in here so with respect to that let us open a new chat and let me ask uh can you please create and create a email for my sick leaf to my manager at tech.mmytheregmail.com.

[2:43:03] So I'm asking it that hey can you write an email for me something which of course all of us do no one writes a email now. So before I draft this again let me ask few question uh love this thanks to our main prompt it is kind of asking these questions. So let's say uh 2 3 days briefly formal.

[2:43:23] Now uh I I love this like the way we have just given this main prompt. Uh I can say manang manager let's say k n a y a m. Okay so that's opposite of my name. Any pending

[2:43:39] task? Uh no tasks. Okay. So information

[2:43:42] again it is asking all the information before just giving me something. But now you will see everyone that how it will try to of course give me the email. But if you remember right if you remember it can still not send it. If I say send the

[2:43:55] same with Gmail connector it will not be able to send it because we know that when we gave Gmail the permission right? So if I show you in the connectors when we gave Gmail the permission there was no send email permission. Okay. And uh I think I think

[2:44:13] uh again it is not being given just maybe with respect to security but yeah I don't see any other reason because it is easier but yeah it will say see uh okay let let it run. I think uh this is something which happens. Let me refresh it. So normally I've seen that if you

[2:44:26] refresh this page the request like kind of goes very outside like you're not able to see that. So let's see loading tools result everything it will try to see. I can see the Gmail connector only supports creating a draft. There is no

[2:44:38] direct send. Uh I created the draft in your Gmail account. you can send it with one from here. Okay. So this is

[2:44:43] something everyone which is a limitation in your uh web version that if you don't have any tools you are not of course able to move forward right and that is where the concept of MCP comes into picture that is where MCP becomes a lot lot powerful. So under the hood right under the hood when your claude is getting connected to these tools it is using something known as MCP. Now MCP you can just think as collection of tools right. So it is a Gmail MCP in a

[2:45:12] way which is having all these tools which uh your clone can use. So in that manner our idea is that if we can create our own MCB server where we provide a send email tool and that MCB server can be anywhere because MCP is like HTTP or any other protocol and if we provide cloud access to that then of course it will be able to do that and along with that many many applications they support uh or have their own MCP servers as well. So many apps you are seeing in here.

[2:45:44] If you see the connectors, lots of apps you are able to see in here. Okay. You can add custom connectors as well. So

[2:45:51] see name remote MCP or server URL. Right? Just as an example, I will show you Firebase MCP uh server cla. So if I search this,

[2:46:02] you will find the MCP server. And see this is the command everyone npx ybase tools. So I can just copy and add this in a similar manner. Okay. So you can

[2:46:12] see advanced setting all these things which normally a server demands and you can manually add your MCP server as well. So I will just try to explain it in a much nicer and easier manner. See all these applications the one which you see on the right they by default gets connected with MCP only. So it is just

[2:46:33] like uh let's say that you added some money into Swiggy wallet or Amazon pay and you are paying. So you just added that money but if required you can directly pay as well right cood or buy or card in a similar manner these are kind of being taken care by claude a few of them like few of the information or sorry excss but if you want you can actually connect your main or like you can connect your own application together uh directly right via the same protocol so that is exactly the same that hey uh instead of paying by swiggy pay amazon where the money was loaded something like cloud why can't I just pay by my credit card or cash directly it is the same thing right at the end of day uh I should be just paying in a similar manner in here at the end of the day you should be able to connect your clot to this application like that is what all matters right so with respect to that everyone let's now see that if we have to add our own servers right own MCP servers how can we do that I already showed you that how you can have the MCP servers for clot now if you will search clot here see it is just saying multiple things install by plug-in or run the following command under your app folder verify the installation. So again it is giving multiple different different options like for claw desktop this is the case. If you want actually if you

[2:47:46] get this you can go to claw only. Uh let's take a screenshot in here. Add custom connectors.

[2:47:54] Okay. And I can just have the chat rather a new chat. Paste this.

[2:48:03] There's I think an AI button here. Explain this code. Yeah. Paste this.

[2:48:09] and ask how can I add Firebase to claude. Okay, so it will just tell you again same thing if anything is not clear you can ask that is a brain which is sitting and very very advanced. So see expand explaining Firebase there are two different methods cloud desktop or cloud code uh something which we are not doing as of now. Uh desktop I will show

[2:48:28] you in a bit. Uh claude a web UI the form in the screen should ask for remote MCB server UI meaning we expect a hosted or remote MCB not a local. Okay. So, uh

[2:48:36] again I will just explain you quickly what happened here because I think this is important. Uh normally what happen is that when you are connecting with these third party MCB servers either it can run remotely or it can run on a machine as well. So on your machine it's a simple server which says that hey these are all the tools I have. So it is

[2:48:53] saying that hey in your claw UI since I don't have a machine or a laptop you can run a locally running uh sorry remotely running one. But if you are on a cloud desktop right if you are on a desktop where I have the access to your machine to your terminal everything then I can have a local running one as well. The Firebase one which we were checking everyone that was a local running one.

[2:49:13] So that kind of runs on your machine and then it starts. Okay. So that is just a quick uh basic idea how it happens. So

[2:49:20] let's try to see this that how can we add it to let's say uh in our claw desktop. So if you will go on settings and if you will go on extension and if you click on advanc setting I think uh built-in MCP node. Okay let me just see developer editor config. Yeah. So everyone if I

[2:49:41] show you like there is a clawed folder and in this clawed folder there is a file right. So I will just try to have this file maybe open in one of the IDE like any or you can just open text edit should be fine. See uh this is what is kept in this file uh preferences like no server I think as of now is there this is cloud desktop config now in here I could just provide that hey this is my desktop config so let's go back above is my desktop config can you please uh edit and provide the final one to me so what it will do is it will add that okay uh let me add the firebase settings so that your claw desktop can run it on your machine and then you can connect with it easily right if it would have been a lo remotely running one then you could have done it as well like it's not a problem so see it has just given that mcb server firebase if I copy this and if I just uh paste it and if I save it okay I will have to I think refresh it let's refresh it and maybe let's kill the same first and let me open it Okay. So I'll just

[2:50:55] kill clot and then open it again because I think that will something which will help us. So let's go here settings developer and see Firebase has added right. So see it is saying it is running because when it starts up it runs this command in your terminal npx - y like hey yes to all please install Firebase pools. So it is just like uh having a

[2:51:17] game which is running online right. Uh of course you can go and play some game online. uh many of different different games are there like I think farmville if anyone remembers do comment or there are some games which say that hey I need to first install even if you want to play remotely like if you I hope all of you remember counter strike right or let's say GTA V as well it has an online mode so it is exactly the same thing one is like that hey if the game is already running I can connect to it not a problem few games says that hey first I will run on your machine I will get installed and everything and then I will connect to the web so it is the second case okay so this is how again everyone you can connect to third party MCP servers. The reason it is important

[2:51:54] because not all the tools are present directly in cloud. So if you want to connect with your own tool, uh you can create an MCP server and connect to it or you can connect with other tools which provide MCB servers. Right? So

[2:52:06] that is having the MCP servers. Now let's try to create our own as well everyone. So again if you will just search for notion clawed MCP server all of them will provide you with these things right connecting to notion MCP then you can see cloud MCP add transport I think this one is the overall uh this thing so let me just copy it this is a remote running one actually so if I just say now it will be able to understand that hey I you want to add this as well and it can be added directly as well so see it gave us for notion as well right uh I can say that uh seems notion one is remote. So again there are few ways to

[2:52:45] understand that since it is having a HTTPS kind of a thing. It is running in a remote place. This should start on our machine. Okay. So as I said like just

[2:52:54] watch the MCP video. Don't get scared or confused here. MCP is a little tricky concept now and I don't want that you have a vague idea about this. Like I

[2:53:02] seen many videos uh just confusing MCP connectors and everything. Well that is not the case. It is a little vague concept and I don't want that tomorrow when you actually go to some interview or something or normally try to create one you should have things clear right else you can create one which can easily be hacked and everything something to avoid now see notion is remote can I add it to claw web UI so if we will ask mostly it will say that yes you can let's see yes exactly the form in your screenshot was for since notion has a remote URL it works perfectly with claw AI web UI. So

[2:53:37] I hope you are able to understand the distinction everyone. This server is like a game which is running on your uh internet only which cloud can directly connect. So it is saying cloud AI give notion and this thing. So remote URL add

[2:53:50] or save. So if I show you customize connectors I think notion is not connected. Yeah. Add custom. Let's say

[2:53:58] this one notion and add. Of course like we will be having a server that URL already exist. Okay, I think this is the one, right? So

[2:54:07] again, uh I think notion is already there. Either we have to remove it now. So and it has been added everyone. Now of

[2:54:20] course we will have to connect it still because even though it is running loc uh like on a remote on some notion server we have to connect with our account here so we can make sure that we are able to use it. Okay. So that is regarding the MCP uh which are running or different application. But let's get back to our

[2:54:37] problem everyone and let's see uh let's say yeah sick leave manager email. The problem which we were facing in here was that we were not able to send a email because Gmail is not giving that right. So uh in the back end as I said though they are connected with MCP some permissions are not given though we have an API for that. If I show you Gmail API

[2:55:00] docs, so Gmail API overview, you will see that how we have the API for dedicated draft everything. We can have the create and send email API as well. So see create and send email messages.

[2:55:11] There are proper APIs. If you're not aware about API, no problem at all. So just that yeah there are ways through which we can do it. Okay. So for the

[2:55:19] same now everyone what I will do now I will just quickly help you revise because I know this I have got a little bit more in depth as compared to others. We can connect with different different applications. First we understood about connectors. In connectors either we

[2:55:33] could connect directly with the applications which claude supports and there are lots of them which we are able to see here. For connecting with uh applications which are on our laptop or machine like Apple notes, Google Chrome, we have to of course go to Google uh sorry cloud desktop and in that everyone we will see more connectors which are now known as extensions. So in here you will see them as extensions because claw desktop is running on your machine.

[2:56:02] Claw desktop can control other applications running on your machine just like how it was controlling other uh like applications running on your web. So that is how it is able to connect read and write Apple desktop desktop commander PDF all these things it is able to do easily. Okay. Next I

[2:56:20] said that okay if now there is some application which you still don't see in here then you can add the same you can add the same by easily just saying that okay I would like to add it by the custom connectors in that it expects a MCP server now I told you that how in the back end all of these are also connected with MCP. So we saw that in MCP as well. Now either they will be run on your machine like uh GTA or counterstrike or it can be a perfectly normal online game. So we saw notion

[2:56:52] which is an online running MCP and we saw Firebase which is a local one which starts on your local. Okay. So this is all what we have done now everyone. Now

[2:57:01] we are saying that hey let's create our own MCB server as well and let's say that if I want to have some tools in here which my claude can use how good that will be right. So for the same everyone what I will do pay attention I will go to any again I will just use any like it is very easy to create your MCP server in here or normally also I think it is pretty easy to create your MCP server now the second I open uh any you can also do the same and I'm doing it on a free instance only not on my paid or uh major instance so create workflow in here if I do add first step then I could say MCP and you will say MCP server trigger expose edit and tools and then MCP server endpoint. So now when I do this and I can just say Gmail or Gmail send I am creating a MCP server. Okay. So this is actually a MCP

[2:57:52] server everyone. This is the link the way we had it for notion. So I think now it is very very easy to understand. And

[2:57:59] I could enter a Gmail tool. I will say that okay uh this tool can send a message to will be told by AI. Subject will be told by AI. Message will be told

[2:58:08] by AI. And now everyone this is like that notion server where all the tools will be there like excess pages everything. We have just created one for our own for our Gmail. Of course you can

[2:58:21] add other tools as well. Not a problem. If I publish it and if I say publish uh I can say got it.

[2:58:29] I can just get the production URL. So the second I get the production URL I can go to here add custom connector say n Gmail send and add and now everyone you will see that how it is having this and I can say always allow so it is able to get the tool as well because it creates a connection with that MCP server right so back end in the back end lots of things are happening and again don't get afraid of these things please try to follow it alongside with me I think I made very very easy by explaining you each and everything. So connectors extension which kind of gets connected in the back end with MCP. But let's go a layer

[2:59:10] further where we learned about MCP. All the applications are having their MCP as well either local or remote. We are creating our own MCP server as well which will be running remotely. Now if I

[2:59:20] go everyone and say that in the chat bally use n uh Gmail send connector to send the email. Let's try to see what will happen. So again it will try to hit this uh running one.

[2:59:38] Okay, it will try to hit this. Let's see this. Sending the email via the edit and Gmail connector. Send a message in Gmail. So

[2:59:45] it is saying that a request has been made. So it will again just send a request here right that's the whole thing. So again it is saying it is sent the same let's see the same everyone if I go here executions. Yeah see this execution is

[3:00:01] here in this execution we can see all the things actually uh if you want uh yeah in the Gmail see so techarval sik application dear na I hope this email finds you well and everything. And if I go to my Gmail, I could have this uh kept. So see, I'm able to receive this, right? Of course,

[3:00:25] we can remove this annotations and everything. Uh that I think earlier we have already kind of covered lots of places. But if you go on Gmail and say append attribution, you can turn it off, right? So again pretty pretty simple

[3:00:38] thing. Now the power lies that you can create lots of tools like again this is where as a wer developer you have to think that now you have so many of these different different tools which you can directly connect or rather if you want what is stopping you to connecting with the HTT or with an HTTP request. So if you want to connect with a totally different uh your own application connect it with HTTP as easy right. So

[3:01:04] yeah, this is I think everyone more more than required and in depth about uh connectors and MCP and I do want that all of you now think that what exactly has it unlocked for you right because actually we have seen each and every button like everything which is present on the clawed overall UI. We have understood the same and that is where like these are getting connected and providing with a lot more details a lot better overall AI experience where it is not just acting as a smart person where is not just connecting to your tool uh like normally it is having these skills plugins connectors extensions so that it has created a ecosystem where it can do the work with all your day-to-day tools and the intelligence and of course the skills and let's say the way of doing that work in a nice manner you can categorize your work in a project and everything so that is the idea everyone and that is I think why I hope you understand now with this proper approach that why claude is gaining that overall uh advantage or maybe the adaptability in your AI space because this all makes it very very uh easy to understand that yes how claude can now integrate into your d2 work right so instead of they selling that hey use our AI just to write email now they have given you all these tools and able to connect and I think we have as I said covered each and everything uh this small button is just to talk with claude. I think I covered that as well.

[3:02:23] So yeah, I think that is all the buttons and everything which we can see in claude everyone and we have discussed each of these things with a proper good diagram as well which I spent a lot of time in creating. So all these different different things right these are all the concept which you should be aware about connector skills uh like the usable skills projects then your different different artifacts which you can generate of course there are document analysis workflow etc which we saw then communicating with cloud right how we have to do that what are the different different models then how are they stronger so these are very very helpful everyone as well as this is also very very helpful that how the normal and the extended mode works and now let's say chat GP versus claude and all these things. So in a holistic manner we have covered everything. An advantage for all

[3:03:07] of us is that recently. So if I just go and search Claude usage limit increase you will see that how claude has temporarily doubled this usage. So now I think it's the best time for all of you to actually run claude because uh for their free plan as well they have doubled the usage for of peak cars. the

[3:03:29] biggest challenge which I faced when I was not having the pro plan of claude 6 months back because again I understand that it's a big commitment or input uh for me it is very very useful but yes as a free plan as well all the things which I've shown you nothing is there which you cannot do by a free plan okay so yeah that is the idea everyone that is where we have understood about the claude in a lot of depth and I think that nothing should be there which you should be afraid of and I think each and everything since we have explained understood with the concepts as well not just how to use it clot should now be as easy as Google for all of you. Right everyone, now let's try to do projects as well because I think that no learning is kind of complete without the projects. Though all the things which we have discussed, I think you should be able to create proper end to end projects. But I would like to actually

[3:04:12] discuss that still uh like what is possible and what is not because again I do believe that yes AI has made everything powerful and you feel a lot happy by creating these small apps. Let's try to understand that with respect to project as well. uh if you're trying to create something end to end what uh all is possible and where we might face issues right so with that everyone let's uh like try to create a AI portfolio website generator now for the same again I will be using my uh LinkedIn uh PDF right so which I asked you to download so let's go into claude and let's try to just paste it and what I will be doing is that uh it is kind of a personal website but let's say you don't want to of course spend time designing it now and we want to just see that if plot Claude can build personal website directly uh without a rum like just using your LinkedIn profile which I think is having all the things right. So

[3:05:01] let me copy this. So this is the link which I will share everyone uh the p sorry the whole uh one minute prompt. You are an expert web developer and product designer. I will upload a rum or

[3:05:16] LinkedIn profile. Your task is to convert information into modern portfolio website. So these are all the things which you can see right. we will

[3:05:22] try to see that if we can still connect our connectors and all these things. Uh in few places you will face issues. I will talk about that as well. Let's uh

[3:05:29] quickly just give this thing and I'm doing this alongside with you uh live building so that you are able to also understand what issues you might face right. So again this will just now reading some front end design skill. Now I think this makes a lot of sense right that what exactly it is trying to do and let it run and it's I think yeah we can quickly come back once it has started or once it has completed the run. So seems

[3:05:51] like it has created something and yeah the design I think was better for the earlier one. This one seems a little bit more better but yeah that should be all fine. I think more or less because it has the same information similar kind of thing it has produced. Uh just text

[3:06:06] everything we can change. Now with that everyone let's now try to understand like of course it has created the same thing. It is an artifact which we want.

[3:06:13] Uh it should not be hire me but no worries maybe you can uh hire me not a problem. So uh now again everyone we have already seen that okay how it has done the same. Let's try to improve the same. So what I will do now I will paste

[3:06:25] this prompt improve the uh portfolio website with following enhancement. Add a navigation bar add icons modern gradient hero section and I can maybe say add some good animations to make website more interesting. Right? So

[3:06:42] these are all the things which we have already seen just helping you to revise. Of course it has all the uh all the data everything. So it is able to do that.

[3:06:48] Let's ask the same and hope that our tokens doesn't run out because that's the biggest problem like it took good 3 4 minutes lots of token lots of code but yeah let it do and let's see the result after this everyone meanwhile it's doing the same I think we can see the diagram as well like what all I wanted to show you. So yes, all of these are kind of the things we are uploading a PDF or LinkedIn. Now of course there are other tools as well where you can create but I think since Claude is becoming a lot smarter we can use that only and again it is having all the idea everything it can connect with your different uh Google sheets and everything as well provided you have some information in there. So portfolio website hero section

[3:07:24] skills all of these things are kind of something which you will try. So I think now it is kind of working on the request. So let's see the result. uh

[3:07:33] basic things like let's say changing the gradient changing the design or maybe you can just copy paste uh let's say something and it will give the same right so I will be bringing some more uh content on why coding/engineering on how you actually think about these things uh as of now of course I have not unnecessary gone that how can you connect database etc to it maybe we can use a simple MCP server connected to a Google sheet right so we can have a Google sheet like this uh this is for lead generation as an idea but yes a similar kind of a Google sheet maybe we can uh where we are having that hey who all tried to access the website or who all want to connect with me right in a similar manner uh we can have a website which call sorry we can have a button which calls my uh MCB server and sends an email though all of these things will require a AI in the fix and that AI I think will most of you will face problems so I I will be discussing that in depth right rather than saying that hey just get the key and use that no we will see that how can we create proper engineering products in the w coding master class which I plan. So let it let it run like I think this will just provide us with the main result. So it is still working like waiting for two uh minutes I think. But yeah the idea is

[3:08:43] that how so many of the code which maybe used to take ages before is being written very nicely by I. So yeah I think that is little helpful and I want that again once you do are able to watch this please share your portfolio websites with me because I think that is valid for everyone. Right. The next

[3:08:59] project which we are going to create professional dashboard uh that is also which I think any everyone can use. So this to get better jobs. Uh the next one to do your current job better right. So

[3:09:08] that's the whole idea everyone. Uh let's uh let us wait for it to complete. Uh it is again trying to do on all these things. Next we will try that somehow

[3:09:17] we're able to add some functionality or connect it to MCP and we will see if it works or not. I think that it will require a AI key so that it can call uh let's say with the information but let's see like how it will uh follow out and the main idea will be that we want that these kind of uh let's say forms work right as of now nothing happens if you click on send message so we will try that we can do some lead capturing that if someone comes to me and say that hey I want to uh connect with you so I'm able to have this thing on my website that's the whole idea now of course that is easy with core engineering and people who are little bit from the tech will know that hey m that is pretty easy but my idea is that again via v coding via basically asking plot to do that and for people who even don't have any idea how that uh those people can also do this uh same thing majorly so again it is trying to remove old files creating enhance portfolio v2 I think it is adding some animations now so as of now it was just kind of going through all my information and everything enhancing the scene let us try and I want that yeah it is all fine because that's good thing right if it is it can take the time 5 10 minutes and do all these things for us. That is where the benefit of Claude overall lies because there are like again many many websites which are coming up. But I feel

[3:10:30] that since Claude is kind of also having a lot of good technical uh knowledge as well, it may do few things little better. Although those models or those website like lovable emergent, they will also be using claude or charging the back end. Maybe uh the way they have fine- tuned them may not provide that better of a result. So let's try to see

[3:10:47] that everyone. I think it is now adding some or the other paddings and overall animation. So let it work. So as we can

[3:10:55] see though like it took a little bit of time but I think the results are pretty good like I like this overall uh effect as well. So the way this is changing uh let us let us actually try to uh publish artifact and let me show you in a full screen because overall I like this effect and everything. So let me show that. Uh yeah. So yes uh now I think the

[3:11:17] website is overall pretty good everyone you can see that how uh okay so this is also pretty good the way it is showing like this so this shows that yeah the person is kind of from tech everything right highlighting all the things tools technology so kind of it has moved a lot ahead rather it's actually a website which one can use uh project and everything okay how it is shining so just via prompt of course you can do these things and now see how nicely it has done the same as well which is way way way better than me scrolling these things and now last everyone is the get in touch but overall uh like I like the way how it is created it I cannot imagine honestly even as a developer of course I have less experience in front end uh so someone can correct me but yeah it is a big task right so that's the whole idea without AI so now everyone like this has been done now we can try to even have AI or Google sheet etc integrated so for that what I will do pay attention so I will uh just ask this and I know that it will face a problem because uh last I checked Google sheet direct connector is not available. So if I show you in claude let's see the connectors most probably we don't have any Google sheet direct connector right so either we have to have an extension or we have to do it via our own MCP right something which I told you but still let us try let us ask it and see how it will go about it so what I'm asking it is that enhance the contact form so that when someone submits the form the data send to Google app script web hook the web hook stores the data in a Google sheet right so it might ask us some API and everything okay but still let's Try that if we can have uh let's say I will delete or delete this one and say contact okay and let us let us give this uh sheet okay so let me say contacts and let us give this spreadsheet because it might need it or otherwise we can of course have different ways the idea again is that how you understand that okay things are kind of falling in place it might able to integrate it it might not but that It is where again we will learn and wipe code with AI. Right? So

[3:13:19] that is what all it is. So now it is saying I will work with the sheet ID directly. So it is saying that okay uh I knew that it will need a sheet ID. So I

[3:13:26] have provided the same thing and it is saying that okay I will rebuild the contact section with full integration. And yes now it is kind of working on that. Now I have the full picture. Let

[3:13:35] me replace the contact form JS in the HTML and create a separate production ready app script file. So it effectively everyone is kind of a script file small script file which will run and send the request to add the details right. So I want that okay if someone wants to get in touch as of now this button will do nothing right so nothing is being done all these are hyperl but in terms of button this will not do anything because we have not uh added any functionality here right so with respect to that and again yeah I can I can go above so you can of course add your photo and everything but I like the this overall right so I like this overall the weight has given each and everything and let me just uh wait so seems like it has done this uh okay get in touch one second open link maybe so okay no I think this is now how it will be done let me try the last one if I click on contact so some it takes us to the hyperlink thing right so it is saying okay now creating the Google app script file so something which it is trying to do so that it can add our overall uh functionality now I can try uh okay if I click on this uh let it still work okay let's not it a lot uh overall impatient. Let it still work and

[3:14:51] we will just quickly try it out. the idea but I hope you get that everyone this is a very very good website if you you have the code as well like that is also a very good thing right so at the end of the day you have this whole code as well if you want to self-host it you can you can ask claude only hey that how can I self-host it on a email or on a web sorry on a website or in a particular link so that is where I feel this is very very helpful right that is the whole idea of creating this project uh this port portfolio website and yes I think once it is done you can normally even send this as well I think no one kind of cares if you have a proper domain or this link because at the end of the day yes people know that how people are now creating their own with uh AI. So see uh it is saying that why no codes Google app web apps don't echo back codes uh okay that you can avoid cir is saying deploy web app everything portfolio html replace the line so now it is saying that hey you might have to deploy the same so that it can be used so portfolio this is the code and contact sheet it has created maybe some sheet right so this is the whole case uh headers and alternating row colors are created automatically on the first submission no manual setup needed so it is just saying that hey uh I have done that Okay, fetch request I have created and that is how you can do it. Now I

[3:16:04] would like to just explain you that why this is not possible directly. Uh though again as I said like it can connect to uh servers and everything. Normally it will require an AI call or something but that is how everyone you can create your overall portfolio website. Now uh I know

[3:16:18] that okay how you can easily connect that and I would try to cover it in an end to end project in claude code. So the video of claude code will also shortly be coming. For the timing, I hope you get the idea that yes, how we have created a website. And yes, if you

[3:16:31] deploy it, uh it will also work because it will be needing a code place to run. As of now, again, nothing will happen. If I just try to click on the send message, once you deploy it, then everything will work, right? And

[3:16:42] normally if you want you can even have uh so let me try it out like I can say that uh have a hidden button in the header where we will be storing all the contact query. Right? So again kind of a hack but for people who are not very techsavvy want to understand and have this thing we we can have some small button etc. not suggested at all for a

[3:17:08] paid or for a main website but yes this is the kind of a thing which we can have everyone not at all a problem our main is that okay any uh request which is coming we can just have it somewhere now ideally if you want we can just hit this thing with a API as well so I can create an API in any a web hook in any which gets hit uh from this button and it holds all the requests and adds that to your Google sheet so again uh it is easily doable nothing is difficult here but I wanted to show you these things and as I said these uh projects end to end I will be covering in claw code overall okay so clude code walk through it will be a lot more easier and better because in here it is still an artifact there it will be a proper website with local host everything right so with that everyone I hope this project is clear now let's move on to the next project so in the next product uh project everyone what we will be doing is creating a professional dashboard so the earlier project will help you to reach out to employers for a better job or maybe to reach out for opportunities. Uh this one will help you to like do your work better. The idea of the project again is that uh and the reason I'm like not going into very deep into these projects because uh I plan to do it in another video. So at least you know that

[3:18:20] hey how can I create things which are actually helpful right for the time being I don't want to get into the place where you don't know what database or APIs or web hook are and there is where you are struggling. So yes, I will be making sure that each and every of those things are clear and then we create project uh properly right. So I don't since I have a very good tech background and I know that uh just having the project without any understanding of DBs APIs how to scale or normally how things get connected will not be very helpful and though yes you can easily connect a superbase uh back end here. So again

[3:18:52] superbase is kind of providing you the database as well though you can easily provide that I want to make sure that I first explain you these things and then we kind of went into that right and for the same I am creating a master class on my coding/engineering as well but uh still I think for playing around these this is a very good project so for this as well everyone what we will do we will build a professional work uh like workspace or workboard which we can use every day and yes instead of managing the task in other different different tools we will be using this So for the time let me show you the prompt again and again I just asked the prompt from uh claude only. So keeping it very easy work task for this week. Let me just zoom it in. Prepare quarterly product

[3:19:32] and all these things. Right. So this is a very very logical scenario right. So

[3:19:38] if you provide this information to claude and then we say that hey if you can build something like this. So pay attention. You are an expert productivity system designer. convert the following work

[3:19:49] information to professional AI workflow dashboard. The dashboard should help professional create, manage priorities, deadline, focus, all these things, everything. So let us just copy this one and that is the power of FL which I want to show you right. So let me just copy

[3:20:02] till here, paste it in this. And I think we can also say have my calendar, email etc tag which can be uh received or refreshed via connectors you have access to. Right? So again uh

[3:20:29] majorly I've just given it a prompt and I'm trying to show you that how you can you build useful things right so that is the whole point everyone now again it will try to build one and it will take time but yes these are actually the things which you can easily showcase rather than some tic tac go game or something plus uh this is something which I feel you can also use as well right so I I love using or uh now bespokingly creating applications for me and this is what I believe you can do with cloth And yes uh do agree that if you have to actually create a product or a mini SAS kind of a thing you will have to know a lots of things. So as I said that we will be also covering. Uh do let me know if you want to me to cover anything else in that. I'm still in the process of

[3:21:12] creating that syllabus and everything. But yeah once uh it is happening viring the boardroom. So this is again some nice thing which it gives stacking of priorities right. I think Lord will uh

[3:21:21] give me a lots of uh usage issue for sure because of the way I am asking it but uh I think it's fine because at the end of the day you are getting to understand that what all overall is possible right so with that everyone let it run and I will just quickly come back once it gets uh done and as I said right now till at least March you have the best uh reason to learn claude because of how it has increased its inc uh claude usage increase how it has given more usages is across uh non peak hours as well as during the weekend. So weekend outside 8 to 2 uh eastern time and all weekends. Okay.

[3:21:59] So the boost likely a thank you to users who missed high demand applies to website app cloud code. Okay. So perfect time to try it out because I have seen up till now I would have easily gotten something like this right but now I'm not getting the same. Uh let me say can

[3:22:13] you create a website artifact instead? So as of right now it has just created a plugin or things here only. Although I like it to be very honest if I get it everything updated but I think yes we can still have it outside. The

[3:22:29] refreshing will be a problem in there because our claude is connected to uh connectors right like your email and your calendar but your website is not connected there. So that is the whole idea everyone and in that let me just say website artifact instead. Now it will try to do that and it will pass on the information but I don't think that it will still have that uh character thing but let's see if it can provide the same. So creating front end skill

[3:22:54] and everything. So seems like it has created a pretty good one. AI workflow website is ready.

[3:23:01] Now overview how many tasks are left? High priority task and everything. Of course we can ask the like have the yellow and that thing. And if you see

[3:23:08] the refresh is not working. uh the reason is pretty simple as I told artifact like it's little bit separate okay so this thing is very very important this I'm kind of setting up your context for clawed code or wipe coding because again this is how you will move towards a little bit more technical right so in here if you will see every even though it has created these things okay uh okay let me do one thing let me publish the artifact publish copy the link and let's try open and let's try to see the kanban Uh okay I think we will have to try to see it will open cloud only. Yeah that's a problem. So let us let us ask if we are

[3:23:48] in Kban. Okay. Okay it is scrollable right? Makes sense. So I think it is

[3:23:52] scrollable. We will have to just get it. So see it is a KBAN. As of now again you

[3:23:55] cannot change and do all these things. But my idea again as I said was to show you that how these usable things are also possible. Right now if you want you can also paste and change it into a real product. So for the same also I will

[3:24:08] show you the prompt everyone. Convert this board into interactive productivity dashboard artifact. The dashboard should include top header with weekly word overview, priority task panel all these things. Okay. So I can just uh paste

[3:24:18] this and ask it to make more changes. But uh yes the artifact which are given by cloud uh normal UI is a little bit limited as you can see right something which we will see in my code engineering and cloud code. But overall as a product it is still pretty good like I if let's say normally I am on the lookout of creating such boards which can work alongside with me though now I am having some applications which why which I handle these things but yes overall I think for small companies this is very very good and the best part is that once we understand that how it gets connected with your database everyone can create now very easily their own kind of a boards and yes get that one right productivity system connected with Jira connected with some to-do list and everything and we are all good. So that

[3:25:02] is the main benefit everyone that is how you can create these things. Plus for the initial prototyping at least uh this I believe is very very helpful right. So if you want to do initial level of prototyping do it like with claude and I think you are all set. So that is the

[3:25:15] whole idea everyone. I think this is something which is very very helpful and let it complete and then we will see that how it will work in the modern SAS kind of a way. So as you can see like it took 2 three minutes but it is saying that your interactivity diode is live here. What make it fully functional?

[3:25:29] four tab section overview canva mode schedule live IST everything so one thing with flagging I notice your calendar for this week is surprisingly sparse that's either a clean week or the presentation interview prep hasn't been blocked in Google calendar yet I would recommend adding calendar block so again it is saying that hey I have the changes and everything so seems like it has got all the events and everything and now we are able to do it I would just like one more thing so I want that I am able to also add the functionality to drag and drop the tasks on Kman. So it's little difficult functionality. Let's see how cloud will handle it because as of now I'm not able to drag and drop like this. Right. So little

[3:26:12] interactive thing how we were having in our this one like how this is following it and all these things and if you will see like it has picked up this small small uh kind of dots which are kind of flowing up. So that kind of things also it has tried to add. Let's try to see uh device drag and drop integration for carbon board task polishing every pixel and yes this is actually what everyone coding is now of course adding a proper DV adding proper scaling thing all these comes into the real engineering but for good uh initial level of things I think these are the good artifacts which you can showcase and if you're in non techch and once you understand cloud code a lot better as well then I think you can create these small small tools for your uh team as well so that they work a lot better, right? So for each client you

[3:26:57] have a different tool, for each work you have a different tool. That is the whole case everyone. So now it is saying writing garb column syncing live data kind of doing each and everything so that it is helpful. Polishing the pixel

[3:27:07] and all these things loading drag drop engine. So let it work. I think it will take 2 3 minutes. So again it is saying

[3:27:14] that it has done something but uh like I'm not able to see it in the artifact. So I think I should ask it. And now again these are also the problem which you can face right? So I'm not editing

[3:27:22] this part out because I want to show you like it's not all good and everything. We we should understand that hey how it can happen and everything or what issues can do. So I can say can you do it in the artifact website provided right? So as of now like it's saying

[3:27:42] that hey this has been done but I'm not able to see like I'm not able to see any three dots or these dotted thing here even in the initial one which it provided like this one here also I'm not able to see any three dots or something right so I either it could be doing it here or in the website but let's ask it and now it is saying uh okay now I think it is trying to do something in the code right so this is where the thing will happen I hope I still have the usage credits available let us see that so again I will show This is will be given if you go on settings and if you go on usage uh my current session is 55% use that is fine uh weekly limit is 30% use which is also fine I think not a lot of problem uh and yes I think all of this thing is totally kind of there uh I had these credits but somehow I lost them because I forgot to recharge. So one thing if you get recharge credit for free please recharge. But yeah, I have the usage still everyone. So you

[3:28:40] should be aware of checking this as well like if you're going to any particular meeting or something and I don't want that you because of free or even paid one as well like lord even limits you in the paid one right that you face this issue. So let's see where it is in the building part seems like replace the script block with a full drag and drop engine. So trying to do few things okay although I do understand that uh this expectation that claude will build a proper website is a little bit different because these artifacts are not meant to be proper websites. Okay. So you can

[3:29:09] publish it as an app and all these things. But ideally we would like to do this as I said again and again in some other way or using some other direct code part of a thing. Okay. So that is

[3:29:19] the whole case everyone. Let it uh quickly run and then we will see if it has been able to do it or not and then I think yeah you have some good projects even if you're from non techch or tech you have some good things to showcase and you can deep dive into it and in the next course when I will bring about coding and engineering plus your uh cloud code I think then it will be all good right? So yeah, I think uh if I if I just publish it, I think it should be working fine.

[3:29:43] Uh okay, copy. Okay, seems like the setting setup has been uh different but uh let us see where is this. Okay, so no worries. Let

[3:29:57] us see what is the case. I think I am able to drag it. Okay, drag and drop uh workboard. It is

[3:30:07] saying it. Can you update on the artifact? Okay, let me click this one.

[3:30:13] Maybe it is clicked. I'm able to see this now everyone. So again, I'm just showing you the issues which you can face. Publish artifact. It is already

[3:30:20] saying I can publish it and then maybe I can publish it again. Uh unpublish. Okay. So let us let us refresh it once.

[3:30:30] Okay. So these are again all the issues which you also can face, right? So let us face it together.

[3:30:35] Seems like this is the updated one where we have this thing. Let me publish publish. Okay. So, some like I think it

[3:30:42] got mixed up on all these things but let's try to have this link instead and and and uh seem like okay okay I think so it will work. I feel that it is also a problem with my dragging thing like this gets kind of triggered but since I'm able to pick it up I think this will work right. So I feel that because of this app I can try to kill it once though like it triggers that thing right so I think okay no the app is still getting triggered so no worries everyone but I think it will work the idea is that yes you can of course work on creating the same all together so with that I feel that we have also now kind of understood this and as I said like I'm putting this projects in here though we have discussed lots of projects artifact during the full learning as well the idea is that yes you can create these kind of small overall PC's and all these things as well everyone and they are super helpful right to showcase to someone and everything so with that I think this uh now we are almost officially done with everything in the cloud AI made sure to cover each and everything from complete scratch we started with understanding the cloud then we made sure that we are using the cloud effectively so right properly we are able to deep dive into these things then the superpowers everyone with document web research image understanding then building with cloud then advanced cloud extended thinking skills connectors, extensions and MCP we have done in a lot of depth and then finally the real AI projects. So with

[3:32:07] that everyone I hope you liked the whole explanation. If you have liked the same please please consider subscribing. I'm bringing as I promised more and more crash courses on this and uh back on the hood I was also working on a complete uh series in which I will make you from AI beginner to AI pro same based on my experience even if you have no experience of coding and of course a lot of tech related content is also coming soon but just kind of working on good content and that is why it takes me a lot of time but um we request all of you to please subscribe if you like the way I cover things practically without any issues helpful and I will make sure that I will see you in the next one. Please

[3:32:41] share this video with everyone and do leave a comment if anything is not clear with the time stamp and I will make sure that I clear the same out. Make sure that you do this completely because in the next cloud code crash course or masterass we will be mastering complete claude with w coding and creating these projects completely and even see that how can we deploy the same as well. So with that everyone thanks a lot and let's meet you in the next video. Thank

[3:33:02] you.
