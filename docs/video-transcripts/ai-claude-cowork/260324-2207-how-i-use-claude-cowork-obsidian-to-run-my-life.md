# How I use Claude Cowork + Obsidian To Run my Life

**Channel**: Ben AI
**Duration**: 21:54
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=qo4YZvC1q5I
**Transcribed**: 2026-03-24 22:07

---

## Organized Notes

**The Five Advantages of a Second Brain for AI Agents**

- **Ben van Sprundel** (AI educator, founder of the Ben AI Accelerator program) demonstrates building a **second brain in Obsidian** that plugs into Claude Cowork, Claude Code, Codex, or any AI agent
- The core thesis: for AI agents to become the main interface for work, they need **persistent context** — the missing layer beyond reasoning, MCPs, and skills

1. **Persistent context** — eliminates re-explaining everything in each chat; AI agent has access to detailed context about business, strategy, projects, brand, workflows, team, and personal information
2. **Bidirectional updates** — AI can both read from AND write back to the second brain; decisions, rules, and project updates get logged directly (e.g., "never use em dashes" gets saved to writing preferences and applies across all skills)
3. **Faster skill building** — skills point to shared reference files in the second brain instead of embedding context in each skill; updating one ICP document updates all skills that reference it
4. **Cross-platform portability** — the Obsidian vault is just a folder of markdown files; give Claude Cowork, Claude Code, Codex, or any other provider access to the same folder
5. **Team scaling** — entire team shares the same second brain with strategy docs, ICP understanding, tone of voice references; any team member's AI agent can write on-brand content

*Quotable Quotes:*

> "The value of this setup isn't in the setup itself. It's in the context that builds over time. Every decision that gets logged, every correction or rule that gets saved, every project that gets documented, and every skill that gets made — it all compounds." [11:43]

> "If your competitor starts 6 months after you, they're not just behind on the tool — they're behind on 6 months of intelligence that makes the tool actually perform far better for you." [12:19]

> "Even when better models come out, and they will, the same context just becomes more powerful. So the context I think will be your actual moat in the upcoming months and years." [12:38]

**How the System Works**

- **Obsidian is a visual overlay** of a folder on your computer — not a cloud service, no API needed, no MCP required
- **CLAUDE.md is the bridge** — an instruction file at the vault root that tells the AI agent how the folder is structured and where to retrieve/save data
- When asked a question, the AI: (1) recognizes it needs more context, (2) reads CLAUDE.md for navigation instructions, (3) reads the specific documents, (4) answers with full context
- **Claude's built-in memory is too limited** — one document of essential facts vs. thousands of context files in a structured vault
- **Wiki links** ([[double brackets]]) let the AI agent navigate between related documents (e.g., brand guidelines → ICP → pain points)

**Skills + Second Brain: The New Approach**

- **Old way**: each skill has its own reference files (ICP doc, voice guide, examples) embedded in the skill folder — updating ICP means updating dozens of skills manually
- **New way**: skills contain **only process instructions** (skills.md) and **point to** context files in the second brain — one update propagates to all skills
- Example: LinkedIn skill and newsletter skill share the same ICP, voice, and pain points documents; a rule added in one chat ("never use em dashes") automatically applies to both

**File Structure: Business OS**

- **context/** — who you are, business strategy, team, brand, ICP, stakeholders, pain points
- **daily/** — daily logs across sessions and meetings (provides continuity between conversations)
- **departments/** — SOPs for each department (community, content, engineering, partnerships, operations)
- **intelligence/** — meeting transcripts, decisions, competitor research, market insights
- **onboarding/** — SOPs for onboarding new team members or clients
- **projects/** — project-specific workspaces (YouTube videos, client projects, etc.)
- **resources/** — reusable library of prompts, templates, frameworks, content examples
- **skills/** — reference materials that skills point to (strategy docs, voice guides, ICP descriptions)
- **tasks/** — to-do lists
- **teams/** — context around each team member's role and responsibilities
- **CLAUDE.md** — root instruction file telling AI how to navigate the entire structure

**Personal/Solopreneur OS** — same structure without departments, teams, and onboarding folders

**Getting Started: Key Principles**

- **Don't overoptimize** — start with ~5 files, let the system grow naturally as you use AI more
- **No perfect file structure** — it depends on your context, business, goals, and projects
- **Always point new tasks** to the same vault folder
- **Explicitly tell Claude** to "remember this in your second brain" when saving context
- **Update CLAUDE.md** when the AI has trouble navigating the structure
- **Migrate old skills** — replace embedded reference files with pointers to second brain files
- **Start early** — the compounding effect means 6 months of context is significantly more powerful than day one

**The Bigger Picture**

- Multiple AI developments converging: **better reasoning** + **MCPs for software navigation** + **skills/plugins for automation** + **persistent context** (the missing layer)
- This combination is shifting the **main interface for work** from 15 different softwares to a single AI agent
- Ben reports using Gmail, Google, and CRM **significantly less** since adopting this setup
- **Scheduled skills** + second brain enables fully autonomous end-to-end processes (e.g., email follow-ups without human involvement)

---

## What This Means for Your Work

This video describes almost exactly what you've already built — and validates it from a completely independent source. Ben's "second brain" architecture maps point-for-point to your Obsidian vault setup: `~/Vault/about-saidamen.md` is his "context" folder, your daily notes are his "daily" folder, your `knowledge-areas/` is his "intelligence," and your `Claude-Skills/` is his "skills" folder. The CLAUDE.md-as-navigation-layer concept is identical to how your vault CLAUDE.md already works. You are already living the architecture he's recommending people adopt today.

**What's different — and worth evaluating:**

The **skills-point-to-vault** pattern is the one structural difference between his approach and yours. Currently, your skills embed reference files in each skill folder (e.g., `/bangsamoro/references/barmm-officials-2025-2026.md`). Ben's approach: keep process instructions in `skills.md` but point to shared reference files in the vault. This matters for your setup because you have files like the BARMM officials list, BOL provisions, and BDP chapters that are referenced by multiple skills (`/bangsamoro`, `/bill-drafter`, `/legislative-briefer`, `/fact-checker`, `/speech-writer`). If you update the officials list after the 2025 elections, you currently need to update it in every skill that has a copy. With Ben's pattern, one update to `~/Vault/bangsamoro/barmm-officials-2025-2026.md` would propagate to all skills automatically.

The tradeoff: embedded references make skills **portable** (your skills-bucket can replicate to Gemini/Codex without needing the vault). Pointed references make skills **maintainable** but vault-dependent. Given your current sync workflow (skills-bucket mirrors vault), you could adopt a hybrid: keep authoritative files in the vault, but have the skills-bucket sync script copy referenced files into the skill folder for portability.

**The "context as moat" argument** is directly relevant to OOBC and MoroTech. Every policy recommendation drafted, every bill reviewed, every legislative briefer produced accumulates institutional knowledge in your vault. If OOBC were to adopt a shared vault for the office (even a simplified version), the compounding effect Ben describes would apply to institutional capacity — new consultants would inherit the accumulated context from day one.

### How This Can Improve Your Claude Skills and Workflows

**Skill improvements:**
- **/bangsamoro**, **/bill-drafter**, **/legislative-briefer**, **/speech-writer**, **/fact-checker** — all reference overlapping files (officials list, BOL provisions, BDP goals). Consider migrating to shared vault references with a sync-to-skill-folder fallback for portability. This would be a structural refactor of how reference files are managed across the skill library.
- **/session-summary** — Ben's daily logs serve the same purpose. Your `/session-summary` already writes to `~/Vault/daily/`. The one enhancement: Ben explicitly tells Claude to "remember this in my second brain" during chats, which you could formalize by adding a "save to vault" instruction in your global CLAUDE.md for ad-hoc context capture (not just end-of-session).

**Workflow changes:**
- **Shared vault for OOBC team** — Ben's team sharing pattern could work for OOBC if simplified. A shared vault with `context/` (BARMM officials, BOL, BDP), `intelligence/` (meeting transcripts, policy decisions), and `projects/` (ECCD Bill, OBC Peace Centers, etc.) would let any team member's AI agent have institutional context from day one. Obsidian's sync feature handles distribution.
- **Skills-bucket architecture** — your `~/apps/skills-bucket/` already serves the portability function. The vault references + sync-to-bucket pipeline would be: authoritative files in vault → skills reference vault paths → bucket sync copies files into skill folders for standalone use.

**Project-specific applications:**
- **e-Bangsamoro** — the vault already contains project context, but it could be structured more like Ben's "projects/" folder with dedicated workspaces per module (MANA, voting, budget). Each module workspace would have its PRD, architecture decisions, and implementation notes in one place.
- **MoroTech/SEED Initiative** — a simplified "Business OS" vault template adapted for cooperatives could be a training module deliverable: teach cooperative managers to build their own AI-augmented second brain for institutional knowledge management.

---

## Transcript

[00:00] Every month, AI agents on cloud code, co-work, and codecs are getting better at reasoning, writing code, and navigating software. But for AI agents to actually become our main interface for work and doing work autonomously, there's still one missing layer: context. So, in this video, I'll show you how I built a second brain in Obsidian that plugs into co-work, or any AI agent I use, giving them persistent context and memory around me and my business. I'll cover the five big

[00:26] advantages of this setup and show you why this might have huge implications for how we work and how businesses are run. And I'll show you how it actually works and an easy way for you to set it up and get started with this today. Now, before showing you how this works, how to set it up, and why I recommend starting with this today, let me quickly go over the five big advantages with some examples of having a second brain.

[00:46] Now, the first one is the most obvious one, and it's persistent context. Right now, most people use AI in isolated conversations. You have to reexlain everything in each chat about your situation, your project, your workflows, etc. And with a second brain, your AI

[01:00] agent has persistent access to all of this context and not just a few facts, but detailed context around everything. You can see in my Obsidian, I have context saved around everything. My business, my strategy, my projects, my brand, my workflows, my team, uh about myself, my meetings, literally everything. And here in this graph view,

[01:18] we can see the relationships between all of these documents. for example, my AI accelerator here and here's me. Now, I'll show you later how this actually works and how to set this up. But

[01:26] because of this, I can now open a new chat session with, for example, Cloud Co-work, and ask something like, "What should I focus on today? It's already connected to my knowledge, Obsidian Vault, how they call it." And you can see Claude now pulls my context to give me an answer. And because it pulled this

[01:42] context, it now knows that my main priority should be landing page copy changes, recording the Obsidian video, and organizing the Spain offsite in April. I could even ask it things like, "Write me a LinkedIn post based on AI topics we discussed in our team meetings this week. Use the LinkedIn instant uh skill." It will now go through our team

[02:02] meetings, see what AI topics we discussed, and use a LinkedIn skill to actually write it in my tone of voice, then pulls the context from my second brain, uses the skill, and then I'll put a LinkedIn post according to the topic we discussed, which is of course this second brain topic. This week, my team and I built something different. We created a second brain for our entire business. Now, this is just an example,

[02:21] but you can see the power of this. And with the new scheduled task feature, this becomes even more powerful. Secondly, besides co-work now always being able to pull up to date and complete context around me and my business in any chat, it can also directly update the context in my second brain. So, any decision, any rule, any

[02:38] project update I make in an AI chat, it can log it directly back into my second brain. For example, if I see something in this LinkedIn skill that I don't like, for example, never use um m dashes when writing content for me, I can say something like remember this in my second brain or in my AI operating system. You can see it now saved and updated this in my second brain as a role in the writing preferences. Now,

[03:00] this is huge because it means the more you and your team use AI to do tasks, the more context is built, the more guidelines it has and the better your AI becomes for yourself and your entire team. Thirdly, there's also a big advantage of having this second brain when building and using skills. Now, if you don't know what skills are yet, skills are basically saved instructions for your AI agent on cloud code or cloud co-work on how to do a specific process or task. For example, in this LinkedIn

[03:25] skill, it goes through the step-by-step process of how to write a LinkedIn post in my style and essentially allows these agents to automate workflows just like I showed you in the example. Now, I have a full video covering skills if you're still unfamiliar with it, which I'll make sure to link in the description below, too. But what changes with this second brain? Skills usually have

[03:42] reference files and context inside the skill folder. For example, in this uh LinkedIn skill, I have a pen profile background document, a hook template document, an ICP document, a LinkedIn example document, and a voice personality document. Now, we use these reference files in skills of course to get to better outputs, but it usually takes a long time to provide all the context every new skill needs to get to a good output. And if you have all of

[04:06] the relevant context around your ICP, your tone of voice, your business already in your second brain, it means you can build good skills far faster. This means you only need to lay out the process and point it to the right context in your second brain. And you don't have to give it the exact same context over and over again for each new skill you're building. For example, I

[04:24] have dozens of skills that share reference files around my ICP, their pain points, what my business does, etc. As you can see, my newsletter writer skill shares a lot of the same context files as my LinkedIn one. So the new way I'm building out my skills with this second brain setup is not by adding this extra context or reference files in the skill itself but by just pointing my skill to the right context in my second brain. For example, this is my new

[04:47] LinkedIn skill the LinkedIn instant and in this case you can see that I only have the skill MD only the process instructions and there I direct it to where I can find the specific context files in my second brain. And this means that any update I make to a reference file in my second brain, for example, in the ICP document, all of the skills that use this ICP document are instantly updated instead of me manually updating dozens of skills myself. It also means that this rule, for example, that I added, uh, never use mashes when writing content for me, is now updated as a rule in my writing preferences, which is one of the documents many of my content writing skills point towards. So, my

[05:25] newsletter skill is automatically updated with this same rule. Now, another huge advantage of this setup, of course, is that it works across any AI you use. So, your second brain in Obsidian is really just a folder of markdown files, which I'll explain in more detail in a second. But that's all

[05:40] it is. It's just a folder that I can now give Clot Codework access to. I can give Clot Code access to. I can give Codeex,

[05:46] Anti-gravity, or any other AI agent provider access to. For example, I can go to the code tab or just use Cloud Code in the terminal. give it access to the same folder of my second brain the Ben iOS and I can ask the same question what should I focus on today and as you can see clot code has access to the same context as you can see landing page copy Obsidian video and Spain offsite and this even works across different AI providers here I gave Codex access to the same folder as the same question as you can see landing page copy YouTube production and Spain offsite and then lastly which is huge if you're a business is that this is not only for yourself but can actually scale across your entire team and business. Me

[06:24] and my team now share this same second brain with my business strategy, ICP understanding, uh to voice references, company goals, etc. So instantly, my entire team's AI agents have access to this context that make them far more powerful and productive for my business. For example, my entire team will always have access to up-to-date strategy documents, ICP documents that their agents can instantly use. And with the

[06:47] context and skills that I've built, I can now let an engineer write my LinkedIn post with an onpoint tone of voice. In Obsidian, I can sync these updates in my context across the entire team here. And you can imagine that this setup could completely change the way you run a business, which I'll get to later in this video. But let me first

[07:03] explain how this actually works because it might look a little bit overwhelming and complicated, but it really is not. So, what is Obsidian? All Obsidian really is is just a visual overlay of a folder and its files on your computer.

[07:15] As you can see here, all these folders that I'm seeing in Obsidian, contacts, daily departments, intelligence, onboarding, I also have available here in the folder that Obsidian is connected to. And all we really do is we point cloud co-work, cloud code or codeex or any other AI agent we use to the same folder on your computer. So they can directly read and write to the same files you see in Obsidian. And that's

[07:36] why Obsidian is a great app to do this on because we don't have to sync anything, use an API or an MCP or a cloud-based software. It's all local. So in coowwork for example, all I do is give it access to that folder. But if we

[07:48] have thousands of these context files, how does our AI agent on clockwork or clock code actually know what context to use and how does it update it? Now again, this is pretty simple. The way it updates and retrieves the right data from your Obsidian folder or vault is through the cloud. MD file. Now the

[08:04] cloud.md file is basically just an instruction you give to your AI agent on cloud co-work or cloud code on how to navigate the second brain or the folder. So if I ask coworker a question like what did we talk about in our team meeting yesterday? My AI agent first of

[08:18] all knows that it needs more context to answer this question. It then reads the cloud MD file to understand where in my Obsidian vault or folder it will find more information around this. Then it reads those specific documents like for example yesterday's Firefly transcript to answer the question back to the user.

[08:35] So you can basically see that cloud.md file as sort of like a system prompt or an instruction layer that tells your AI agent how the vault or your folder is structured and where to retrieve and save data. So as you can see in this session with cloud co-work where we wrote the LinkedIn post, it has access to one file which is the instructions for the cloud MD and this is basically just instructions for the AI agent on where to find specific information in the second brain and where to save it.

[09:01] So you can see how this system works, the file structure, knowledge routing, and this same clot.md file or the instructions you also see here in the Obsidian vault. Now, don't worry, I'll show you later in this video exactly how to get to this cloud MD and how to set up these instructions easily. Now, you

[09:16] might be asking, how's this actually different from CL's built-in memory, and why would we actually need Obsidian if it's just a folder? Now, first of all, CL's built-in memory is very limited and is basically designed to remember the most essential facts about you. It's generally stored in one document. So the

[09:32] difference really is the scope of the context. My Obsidian Vault, as you can see, has thousands of pieces of context. And secondly, if Obsidian is just a folder, why would we need Obsidian? The

[09:41] short answer is you don't need it. Uh you can set this up in a folder yourself, too. But honestly, it's just a nice way for you to visualize, organize, navigate, uh search, and link your notes and files together. my context and

[09:53] knowledge sources over the last weeks have been growing really fast and honestly without Obsidian I wouldn't be able to organize it the way uh that I have right now through the graph view we can also see the relationships between all of these context files it automatically makes these connections between different documents or context files uh for example in the brand identity document you can see that we have the voice positioning where links to the ICP for our ideal customer profile and the pain points of our customer this is also what your AI agent is able to navigate so for example if it reads the brand guidelines and feels like it needs more context around my ICP, you can see this link or wiki link, what they call it, and actually look up this document to find more information. And the nice thing about Obsidian is I can really easily sync the uh updated context across my team if you're going to use this in a team setting. It's also entirely free to use and download. So, I

[10:40] just recommend using it. Now, before showing you how to set it up, let me zoom out for one second because I think this setup has much bigger implications than just some extra productivity. I think it could entirely change the way people work and businesses are run. So

[10:53] there are multiple of these big developments coming together right now in AI. Uh everyone can see that these L&Ms are becoming better at reasoning. MCPs are getting better and now allow them to efficiently navigate softwares and the internet and skills plugins, schedule tasks, etc. now allow you to

[11:08] automate uh repetitive tasks fast and easily. But the missing layer for those AI agents was really context. And with a setup like this, I think it will slowly allow people and businesses to start adopting an AI interface like cloud co-work or cloud code as the main interface to do their work instead of hopping between 15 different softwares all the time. But maybe more

[11:27] importantly, I think this is the development that will slowly allow AI agents to start doing work autonomously without our involvement. Personally, for example, since I've really started using co-work on a daily basis, I've been less and less in my Gmail inbox. I've been less on Google doing research. I'm

[11:43] barely in my CRM anymore. And now with these combination of MCPs, connectors, and scheduled skills, I can now automate end-to-end processes like email follow-ups without my involvement. And that's why I really believe you need to start building this today because the value of this setup isn't in the setup itself. It's in the context that builds

[12:00] over time. Every decision that gets logged, every correction or role that gets saved, every project that gets documented, and every skill that gets made, it all compounds. So the AI agent you and your entire team have after 6 months of using this is far more powerful than the one you start with on day one. And if your competitor for

[12:19] example starts 6 months after you, they're not just behind on the tool, they're behind on 6 month of intelligence that makes the tool actually perform far better for you. And even when better models come out, and they will, the same context just becomes more powerful. So the context I think will be your actual mode in the upcoming months and years. So how do you actually

[12:38] set this up for yourself or your business? Now, the key thing to keep in mind when you get started is that you don't want to overoptimize. It might look very overwhelming what I just showed you in my own setup, but this setup I started with just probably five files a few weeks ago. This context will

[12:52] grow very naturally the more you use AI. You just want to sort of start very simple and let the system evolve naturally. The same is the case for the file structure. It is important, but you

[13:01] do want to start simple and let it evolve naturally. There is really no perfect file structure because it's going to be highly context dependent. It will depend on your context, your business, your goals, and your projects.

[13:13] Um, now that being said, there are two file structures that I recommend and I've seen work well as a starting file structure. One for if you're running a business uh and you want to use this across your team and one if you uh want to use this for yourself as a professional or as a soloreneur. Now, go over the file structure quickly so you understand what's in each because it is important. But we've also built a

[13:33] plug-in you can use in your AI agent on cloud co-work or cloud code to help you set up and get to these starting structures fast, which I'll show you in a second how to use. And second, what you want to keep in mind when I'm going through this is that many of these files are and can be created by your AI agent. So don't get overwhelmed. You'll get

[13:48] there naturally. So I'll cover the file structure that I use for my business setup and then I'll show you quickly the personal setup which is basically the same but with less files. So first we have the context folder and this is where you store general context around who you are, your business, your strategy, your team, your brand and it's basically everything your AI agent needs to understand about you and your situation always. For example, in

[14:09] context, I have information about my team, strategy, stakeholders, pain points, organization, operator, the ICP, and the brand. Second, we have daily. And this is basically where your AI agent logs everything that happened each day across your sessions, maybe across your meetings. And this is probably the

[14:25] most important one because it gives your AI agent that continuity between conversations. Then third we have departments. Now this is if you run a business uh you will of course have different departments. For example in my

[14:37] case community, content engineering partnerships operations etc. And then in the community folder for example we can have SOPs around work that needs to be done in my community. For example here YouTube to community repurposing. The

[14:49] fourth one is intelligence. And this is a bit like the first one context but much more detailed. And this is the place where uh things like meeting transcripts, decisions, uh competitor research, market insights get stored over time. Then we have onboarding. Um

[15:04] here you can have SOPs around uh onboarding new team members or even clients. Then we have projects here. Now projects will highly depend on uh your context. For me, projects can be for

[15:14] example different YouTube videos I'm working on. So I can ideate and work on scripting uh on one video between different chats. Uh if you run an agency, this can be a project for each client you're managing. But this will be

[15:25] highly context dependent. Then fifth, we have resources. And resources is basically anything reusable. So you can

[15:31] imagine it like a library of prompts, templates, frameworks, maybe content output examples, good examples, things like this. Then we have the skill folder. Uh an important one uh where the reference material of your skills live.

[15:45] for example, your strategy docs, your voice guides, your ICP descriptions, uh, basically additional information that your skills point to. So, you can see I have all my skills here, uh, with the reference files laid out. By the way, if you want access to all of the skills that me and my team are building out and using, uh, you can also check out my AI accelerator in the link in the description. Then, lastly, we have here

[16:04] tasks. And tasks can basically be uh, to-do lists. And then we have teams with more context uh, around each team member's role and responsibilities in your business. So your agent always has

[16:14] context around anyone in your team. And that's really it. And then at the root here, you have the clot.md file, the

[16:20] brain file, which is the instruction layer that tells your AI agent how this whole file system here works and how to navigate it. And this will also appear in the co-work section in their folder instruction that I showed you before. Now, if you're setting this up for yourself uh as a solopreneur or maybe as a professional, you can basically have the same uh structure but a little bit simpler. Uh so here I have an example of

[16:40] the personal OS. It's basically the same file structure uh without the department, without the team section, and without the onboarding. So, same file structure, just a bit simpler. Now,

[16:50] again, might look overwhelming, but I started this a few weeks ago with just five files, and this sort of naturally grew, and a lot of this uh context has been created by my AI agent. And the plug-in we built is going to make this process a lot easier and faster to do. So, how do we set it up? You can just go

[17:04] to Obsidian and download Obsidian for free. Once you've done that, you'll land on a screen like this. So you can just go here to create new vault. For

[17:11] example, I call it Benai test and then I have to choose a folder. So I just create a new folder and this is the folder that you're going to point cowork or cloth code or any AI agent you use towards to access that same vault that Obsidian visualizes for you. So we open this one and click create. So we now

[17:29] have an empty folder. Now if you're going to set this up in cloud code, you can also use Obsidian CLI which I'll make sure to put in the description below. that can help you get to a basic generic setup a bit quicker. But as

[17:40] said, we've built our own plug-in which is available in my AI accelerator together with all our other plugins and skills to get you to that file structure that I showed you before a lot quicker. It helps you also populate uh your essential context a lot faster. And this plug-in will work across cloud co-work or cloud code, wherever you want to use it. So, if that's interesting to you,

[17:59] you can check it out in my AI accelerator in the link in description below. We also have unlimited one-on-one live tech help available if you want uh some help setting up these things. We also do AI workshops where we dive a lot deeper into these setups and tools. So,

[18:10] if that's interesting, definitely check it out. Also, if you're a business and you want me and my team to help you in a more personalized way to set up a business AI OS for your company, we're now opening a few limited spots to help businesses set this up. So, if you want more information, you can also check the link in the description below. In there,

[18:25] you can find a link uh with the marketplace of plugins and skills of my accelerator. And from there, if you do it in co-work, you can just go to customize. Click here on the plus and you click add marketplace and you add the link that you find in accelerator.

[18:39] Once you've done that and you go to browse plugins, you'll find a tab here at personal that says Benai skills. And in there at the bottom, you'll find our plugin, Ben Obsidian plugin. You can install that. And now you'll see that in

[18:53] your plugins, this one will appear. And there we have the skills that help you get to that setup in Obsidian a lot faster. And all we do then is we point co-work to the same folder that we just set up in Obsidian. So in this case,

[19:04] Beni test. We click always allow. And now we uh use uh the plug-in and the scale setup.

[19:12] Right? We run this and it will walk you through uh the setup on getting to this file structure a lot faster. And I'll start asking you some question to get the essential context set up. So first

[19:22] it asked me what kind of vault do I want a business setup or a solopreneur setup. So in this case I'll do uh solopreneur just to show you as an example. So now it's already created the initial folder structure and the cloud MD with the instructions on how to navigate this type of folder structure. As you can see

[19:36] now in obsidian we already have this folder structure. Now most of these are still empty of course because we haven't given cloud any context. So the next question is to really start giving it context. Right? And that's what this

[19:47] plug-in does, right? It it's going to ask you some questions to populate your initial context data set. now want to spend probably half an hour to an hour here to get your your initial setup have the initial context data set and from there it will naturally expand and I can tell you if you start using AI more and more in a couple of weeks you'll have a very expanded data set of context that really makes your AI far more powerful.

[20:09] So a couple of important things to keep in mind once you get to that initial data set is every new task you start in clock code you always want to point towards that same uh folder. Second, when there are things that you want your AI or your second brain to remember, clearly tell cloud co-work to remember this in your second brain or whatever you call your folder. If you can ideally even point it to the specific file it has to save that role to. Thirdly, if

[20:32] you see it have issues navigating the folder structure, tell it to update the cloud MD, which you can also do yourself because remember this is the bridge to point it to the right direction. So, I can add in rules all the way at the end here too. You can see I've already added some rules on how it should navigate the folder structure. And then lastly, if

[20:51] you're going to build skills, I highly recommend to take a new approach now and instead of embedding reference files into the skill here in Cloud Co-work or in Cloud Code, save the reference files in your second brain and let the skill point towards the right folders. You can also adapt your old skills by just telling claude. For example, here I said, can you adapt my LinkedIn skill and create a new skill and gave it here specific instruction instead of having the reference files in the skill point towards the files in the Ben AIOS to get the additional info instead of having them saved in the skill. And again, the

[21:23] earlier you start with this, the more powerful your AI agent is going to get over the long term. So, highly recommend to start soon with this. Now, that's it for this video. Again, if you want

[21:31] access to all of the plug-in skills that me and my team are building out, plus unlimited one-on-one live tech help and AI workshops where we dive a lot deeper into these tools, you can check out my AI accelerator in the first link in the description. And if you're a business that wants a little bit more personalized help in setting this up for your business, you can check the second link in the description below. Thank you so much for watching. If you want to

[21:48] learn more about cloth co-work uh skills, plugins, etc., You can also check out the video here above.
