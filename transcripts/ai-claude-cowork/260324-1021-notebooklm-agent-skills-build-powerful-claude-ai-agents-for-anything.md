# NotebookLM Agent Skills: Build POWERFUL Claude AI Agents for ANYTHING!

**Channel**: Universe of AI
**Duration**: 15:06
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=I-4cJgqF_JY
**Transcribed**: 2026-03-24 10:21

---

## Organized Notes

**The Core Problem: Building Domain-Specific Claude Skills**

- Building a good Claude skill requires **real domain knowledge** — writing the knowledge base manually takes forever, and vague prompts produce generic results
- The solution: use **NotebookLM's deep research** to generate structured expert knowledge, then feed it into Claude's skill system
- Result: a working AI agent grounded in **real research** rather than generic LLM guessing

**What Claude Skills Are**

- A skill is a **structured knowledge file** (markdown) that tells Claude how to behave in a specific context — more than a system prompt, it's a **domain brief**
- Skills define: what the task is, what good output looks like, patterns to follow, what to avoid, examples, frameworks, step-by-step instructions
- When loaded into a project or pointed at via Claude Code, Claude **adapts its behavior** accordingly
- Key benefit: you're **training Claude to be really good at one specific thing** without re-explaining yourself every session

**NotebookLM Deep Research as the Knowledge Engine**

- Deep research (added November 2025) **browses hundreds of websites** on your behalf, creates a research plan, refines searches iteratively, and outputs a structured, source-grounded report
- Unlike regular AI search, the output **persists in the notebook** — reports and sources get added and can be curated, cross-referenced, and built upon
- Run **2-3 research queries** on the same topic for comprehensive coverage (e.g., one on frameworks/strategy, one on tools/workflows, one on common mistakes)
- All queries layer into the **same notebook**, building a rich knowledge base

**The Synthesis Layer**

- After research loads in, ask NotebookLM to **organize and extract patterns**: core principles across sources, most-mentioned frameworks, step-by-step processes
- NotebookLM provides **grounded, cited answers** pulling from everything in the notebook
- You're **extracting structured insight from real research**, not writing from scratch
- Can ask targeted questions (e.g., "how to write targeted outreach, research prospects, and identify pain points") to get focused synthesis for specific skill needs

**Building the Skill in Claude**

- In Claude Desktop: **Customize → Skills → Create with Claude** (recommended for first-timers)
- Paste the NotebookLM research into a "**processes knowledge**" section along with a skill name
- Claude's skill creator asks **clarification questions** that catch things you might miss:
  - Output types (e.g., cold email, LinkedIn, phone scripts, or full multi-channel?)
  - Expected inputs (prospect name, company, product/service context)
  - How rigid the structure should be (very opinionated vs. flexible vs. loose)
- The resulting skill file includes: agent persona, input assessment logic, research mode triggers, **outreach writing principles** (under 125 words, signal-first opening, one ask only), and structured sequences

**Demo: B2B Sales Prospecting Skill**

- Built a skill for writing **cold outreach sequences** grounded in 2026 B2B sales research
- Test case: hypothetical cold email sequence for **Airbloom** (snack company) with delivery/logistics pain points
- Output: **14-day multi-channel sequence** (LinkedIn touches, emails, phone calls) with pain hypotheses, personalization notes, target identification, and bonus pain point analysis
- All generated in seconds from invoking the skill — no re-pasting frameworks

**Skill Portability and Deployment**

- Skills work across all Claude modes: **Chat, Cowork, and Code**
- In Cowork: skills combine with **calendar access, email drafting, automations, and scheduled tasks**
- Skills are **transferable** to other AI models (ChatGPT, Gemini), though Claude's Cowork integration makes it the preferred choice
- The skill library you build over time becomes **genuinely valuable** — the difference between a generic assistant and a specialized agent

---

## What This Means for Your Work

You're already doing a more advanced version of this workflow. Your `/research-pipeline` skill explicitly combines NotebookLM (free analysis) with sub-agent validation and Obsidian vault storage, and your `/expert-builder` skill creates permanent Claude Code skills from NotebookLM research. This video validates your architecture but targets a beginner audience — the interesting signal is what you can extract from the gaps.

**Your pipeline is more rigorous than what's shown here.** The video's workflow is: NotebookLM deep research → paste into Claude's GUI skill creator → done. Your pipeline adds validation (sub-agent cross-checking), persistence (Obsidian vault storage), and portability (skills-bucket repo synced to vault). The video skips verification entirely — the research goes straight from NotebookLM to skill without checking whether the "hundreds of websites" produced accurate domain knowledge. Your `/fact-checker` step addresses this gap.

**The "Create with Claude" skill builder is worth testing for rapid prototyping.** You currently build skills manually following ~/Vault/Claude-Skills/Guidelines.md. Claude Desktop's built-in skill creator (Customize → Skills → Create with Claude) could speed up initial drafts, especially for domain skills outside your core expertise (e.g., if OOBC needs a quick skill for monitoring OBC welfare programs across regions). You'd still refine through your /skill-optimizer loop, but the first draft could be faster.

**The clarification question pattern is a design insight.** The video shows Claude's skill creator asking three targeted questions (output types, expected inputs, structure rigidity) before building. Your /grill-me skill does something similar but for plans, not skills. Consider whether /skill-creator should have a built-in clarification round — asking "What inputs should this skill expect?" and "How rigid should the template be?" before generating the skill file.

**Concrete next steps:**
- Test Claude Desktop's "Create with Claude" skill builder for a simple OOBC domain skill (e.g., OBC community registration workflow) and compare output quality against your manual skill creation
- Evaluate whether your /expert-builder skill's NotebookLM → skill pipeline could benefit from adding the structured clarification questions (output type, inputs, rigidity) shown in this video
- The video's B2B sales demo reminds you that your /research-pipeline could produce similar domain skills for non-tech BARMM staff — e.g., a "grant proposal writing" skill or "budget utilization reporting" skill built from NotebookLM research on government finance best practices

### How This Can Improve Your Claude Skills and Workflows

**Directly improves /expert-builder and /research-pipeline.** These two skills are your existing version of this workflow. The video reveals a gap: your /expert-builder creates skills from NotebookLM research but doesn't include a structured clarification round before generating the skill file. Adding the three-question pattern (output types, expected inputs, structure rigidity) would produce more focused skills on the first pass, reducing the iterations needed in /skill-optimizer.

**The "processes knowledge" section pattern maps to your references/ architecture.** The video shows pasting NotebookLM research into a "processes knowledge" section of the skill prompt. Your Skills 2.0 format already separates this into `references/` subdirectories — a cleaner architecture. But the insight is that /expert-builder should explicitly label and structure the knowledge it extracts from NotebookLM into the `references/` folder rather than embedding it inline in skill.md. This keeps skill.md under the 2,000-word guideline.

**Specific skills that could benefit from a NotebookLM knowledge refresh:**
- **/bangsamoro** — the domain expert skill's references were manually curated. Running NotebookLM deep research on "Bangsamoro governance 2025-2026 developments" could surface recent policy shifts, new BAAs, or institutional changes your local reference files don't cover yet
- **/cooperative** — RA 9520 compliance frameworks evolve. Deep research on "Philippine cooperative development 2025-2026 regulatory changes" could update the skill's knowledge base
- **/financial-analyst** — government financial reporting standards and BARMM budget execution patterns could be researched and fed into the skill for more current analysis
- **/toc** (Theory of Change) — the ToC frameworks in the skill are from specific academic sources. NotebookLM deep research could surface newer M&E frameworks relevant to BARMM's development programs

**New skill opportunities identified:**
- **Grant proposal writing** skill — your /policy-recommendation handles OOBC policy docs, but there's no skill for writing grant proposals to international development agencies (UNDP, JICA, USAID). NotebookLM deep research on "successful government grant proposals for autonomous regions" + your existing /bangsamoro domain knowledge could produce this
- **Budget utilization reporting** skill — your /financial-analyst handles analysis, but there's no skill specifically for generating the BARMM-format budget utilization reports that OOBC and other agencies must submit. Research on "Philippine government budget execution reporting requirements" could ground this

**Cross-pollination with /skill-creator.** The video's "Create with Claude" workflow is essentially what your /skill-creator skill does, but the GUI version adds implicit clarification questions. Your /skill-creator (via the skill-creator:skill-creator plugin) should adopt this pattern: before generating any skill, ask the user about output format preferences, expected inputs, and rigidity level. This is a concrete improvement to propose in the next /skill-optimizer run.

**/auto-research integration.** The video's workflow is linear: research → build → done. Your /auto-research skill could close the loop: research → build skill → run skill N times → judge outputs → mutate skill → keep best version. This means every NotebookLM-sourced skill automatically goes through quality optimization before being added to your 124-skill library. The pipeline would be: /research-pipeline → /expert-builder → /auto-research → /skill-optimizer → vault sync.

---

## Transcript

[00:00] Today, I want to show you a workflow that I've been using more and more recently, and honestly, it's become one of my favorite ways to build out AI skills. It combines Notebook LM's deep research feature with Claude skill system. And that result is basically a way to turn raw research on any topic into a working AI agent that actually knows what it's doing. Here's a

[00:20] problem I keep running into. Whenever I wanted to build a cloud skill for something specific, whether that was SEO, copywriting, a specific industry, whatever, I either have to write the whole knowledge base myself, which takes forever, or I just prompt Claude with vague instructions and hope for the best. Neither of those is great. What I

[00:39] really needed was a way to get deep, structured knowledge on a topic fast and then feed that directly into a skill that Claude can actually use. And that's exactly what this workflow does. Notebook LM does the research. Claude

[00:51] builds the skill and then you got an agent that can be dropped into any chat or used inside Claude code that actually knows the domain. Let me walk you through this whole thing. Before we get into notebook, let me quickly explain what a Claude skill actually is. Because

[01:06] if you haven't used them before, this is the piece that makes everything click. A skill in Claude is basically a structured knowledge file, usually a markdown document that tells Claude how to behave in a specific context. It's not just a system prompt. It's more like

[01:20] a domain brief. You define what the task is, what good output looks like, what patterns to follow, what to avoid, and you can include examples, frameworks, step-by-step instructions, all of it. When you load a skill into a project or point Claude code at a skill folder, Claude reads it and adapts his behavior accordingly. So, if you have a skill

[01:40] for, say, writing cold outreach emails, Claude isn't just guessing what that means, is working from a defined playbook. That's the whole point. You're basically training Claude to be really good at one specific thing without having to explain yourself from scratch every single session. Now, the question

[01:56] is, how do you build a good skill? That's where Notebook LM comes in. Notebook LM added deep research back in November. And if you haven't tried it

[02:05] yet, it's genuinely one of the more useful AI research tools available right now. And it's also free. Here's how it works. You go into notebookm, you go to

[02:13] the sources panel, you select web as your source type. And then you get two options. Fast research, which is a quick scan, and deep research, which is the one we want. You type in a question or

[02:23] topic, and notebook LM literally goes and browses hundreds of websites on your behalf. It creates a research plan, refines a search as it goes, and then spits out a structured source grounded report in a few minutes. What makes it different from just googling or using another AI search tool is that the output doesn't disappear. The report and

[02:42] all the sources it pulled get added directly into your notebook LM. So now you got this rich knowledge base you can keep curing, adding to, and cross referencing. You can run multiple deeper research queries on the same topic layer in your own documents and build up a really comprehensive picture of whatever niche or subject you're working on. For

[03:01] our purposes building skills, this is incredibly useful because a good skill needs real domain knowledge. It needs to understand how professionals in that space actually think and work and deep research can pull that together for you in minutes instead of hours. Okay, so let me show you exactly how this works end to end. Step one, pick your niche or

[03:22] topic. For this demo, I'm going to use something concrete. Let's say you want to build a cloud skill for B2B sales prospecting. You want a skill that can

[03:30] help Claude write targeted outreach, research prospects, identify pain points, that kind of thing. Step two, run deep research in Notebook LM. I'm going to go into Notebook LM, open up a new notebook, go to the sources panel, select web, and hit deep research.

[03:47] My question is something like, "What are the most effective B2B sales prospecting strategies in 2026, including frameworks, outreach patterns, and show how top sales team identify and qualify leads?" You hit go, it runs in the background, and in a few minutes, you got a structured report or sources. Now, I'll usually run two or three research queries on the same topic to make sure I'm getting good coverage. Maybe one

[04:10] focused on frameworks and strategy, and one on tools and workflows, one on common mistakes, maybe. But each one pulls different sources and all of it gets layered into the same notebook. Before we continue, we just launched the universe of AI newsletter. If you want

[04:25] to stay on top of AI news without having to hunt for it, link is in the description. Don't miss out. Step three is to synthesize a notebook. LM. Now

[04:33] that I got all this research loaded in, if we take a look at this, we can see that this article over here at the top is a summary of all of these cited sources and it kind of shows us what database sales looks like, especially in 2026 and how it is transitioning to AI intelligence and signal-driven frameworks. So, we have frameworks, we also have where it's heading and things like that. I can now start asking Notebook LM to help me organize it. I

[04:58] can ask it things like what are the core principles that come up across all these sources? What frameworks are mentioned most? What does good prospecting actually look like step by step? And

[05:07] notebook LM pulls from everything in the notebook and gives me grounded cited answers. This is the synthesis layer. I'm not actually writing the skill from scratch. I'm extracting structured

[05:17] insight from real research backed in by notebook LM. So we can see our notebook LM has imported all the sources. We have the summary document as well. We can see

[05:26] already that we also have top sales methodologies over here. If I wanted to just learn about them, I can learn about them over here. But for our purposes, we want to take all this information and feed it to Claude, especially for the skill file. So, I'm going to show you

[05:39] guys exactly how to do that. You have a couple of options. You can take this specific summary document, which summarizes all of your, you know, research from all the sources. But one

[05:49] thing you'll notice is that it's pretty vague, right? We have benchmarks, we have AI, automation, and things like that. Not specific frameworks, everything. So you could do something

[05:58] simple like this. You could ask it specific questions like what are the specific frameworks or strategies and take that information for our purposes. Let's say I want to learn about how to write targeted outreach, research prospects and identify pain points and build the skill around that. I'll ask

[06:13] that question and send it to Notebook LM and then it's going to go through all that research and give me a summary of how to do that specific skill. So it's going to do that and it's going to send us an answer. So you can see that we have an answer over here basically telling us that how to research prospects the five-minute habit identifying pain points what we need to do and how to write targeted outreach.

[06:32] So once you're in claude all you got to do is click on this sidebar click on that and then click on customize and then go to your skills and then click on creating one over here. You can do create with claude or you can write skill instructions. For first timers try to do create with cloud because it makes the whole process much easier. So we'll

[06:49] do that. You can see it gives you a prompt. Let's create a skill together using your skill creator skill. First,

[06:54] ask me what this skill should do. So, instead of us starting from scratch here where most people would when they're actually doing the skills, you now have research and methodologies that you can take from notebook LM and paste into cloud instead of you typing from scratch. So, we're going to take this and we're going to give it a name. Then,

[07:11] I'm going to create a section called processes knowledge. And what I'm going to do over here is paste in all the information that we got from over there. Then you might also want to specify how you want the output to be for this purposes. Obviously, I'm going to use

[07:24] this in multiple formats. But I can just tell it that in the output use the knowledge base that we have given it over here to help generate work that aligns with the research. We want to do that. Let's say if you're kind of

[07:34] creating a skill for a specific writing style, you could do some deep research on that writing style. Bring that in and tell it the same thing and it'll align your output to that. Or if you're trying to create an AI consultant, you can study all these frameworks and you can tell it to give you an output, specify the output like implementation plan, strategic takeaways, things like that.

[07:52] This is very customizable. So you can play around with this and you can duplicate your skills and change your output format. Or you don't have to specify how you want the output and can let Claude decide for yourself. But as I

[08:03] said, it's going to be dependent on the skill you're trying to create and the specific domain knowledge you're trying to understand as well. Right? So we'll do that. So I'm going to press enter.

[08:11] And what Claude going to do is going to use that skill creator that you can see over here that skill that it has. So right now we are in a skill session. Basically it's using a skill file to create another skill file and then it's going to create that new skill which is going to be called outreach skill. You

[08:26] can see that it read that skill file but it's also asking some clarification question which is why sometimes building skills with claude is much easier because you know you might have missed something in your head that Claude kind of flags. For example, it's asking three questions. Which output types, cold email, LinkedIn, phone scripts, or full multi-channel? What inputs Claude

[08:43] should expect? How opinionated on structure? Very rigid, flexible, or loose. For our purposes, I'm going to

[08:48] select the full multi-channel sequence, which makes sense. Start off with email, then go to LinkedIn, and then phone. So, let's do that. And then

[08:55] the second question is, what should Claude need as input to use his skill? Prospect name from company, signals, triggers, your product, service, context, a target person, or ICP. Let's do your product or service context and prospect name plus company. So, I got to

[09:09] specify what I'm trying to sell and then the company and then cloud will do the rest. How opinionated should the skill be about structure? Very opinionated.

[09:17] Always follow the three-part structure. Context value as flexible. Suggest the framework but let context guided. Just

[09:23] apply the knowledge. Don't enforce a rigid template. So, this is really good because Claude is saying, "Okay, you provided me with this framework. Do you

[09:30] want me to stick to it all the time? Do you want me to be flexible or just apply the knowledge and don't enforce a rigid template? I'm going to do the middle ground which is kind of flexible suggest the framework but let me decide what I want. So now it's going to build that

[09:42] skill based off those clarification questions. So now what you're seeing is our whole skill packaged over here. We can see apply the skill whenever the user wants to write cold outreach, sales sequences, prospecting messages. You are

[09:55] an expert B2B sales strategist and copywriter. Your job is to help the user write outreach that is hyper relevant, signal driven, and structured for response, not volume. We already have this AI agent or AI skill that's going to help us a lot, save us a lot of time.

[10:09] And it says step one, assess what you have. Input available, prospect name, everything like that, action, skip, ask. So depending on what I give it, it also figures out what it needs to do. Step

[10:20] two, research mode when needed, leadership changes, funding round, strategic language, job posting, competitive moves depending on the situation, signal density rule, painoint deduction. So determine what the pain point is. I'll put right then this part is probably more relevant to us which is outreach writing core principles under 125 words signal first opening outcome over features one ask only no buzzword and three-part structure context value as so it has all that framework that we applied from notebook LM and then you can build that sequence we can see day one channel day one LinkedIn day two email day four phone call day seven LinkedIn. So we have that you know

[10:58] length and everything like that. So, it has this sequence already built in for us. So, we can save a bunch of time and we have subject lines and everything like that. But you can see we now have

[11:06] access to this skill and we can just copy this to our skills and it's going to be available for us to deploy whenever we want. So, now what I'm going to do is actually put my skill to test. So, I've taken this snack company, a snack company that I love. Uh, this is

[11:20] like their product. They sell lotus seeds. So, they have all these flavors.

[11:24] And what I've done is I've created a simple hypothetical situation which is to build a cold email sequence for Airbloom a snack company struggling with order delivery and logistics. Then I'm also going to ask it to try to determine other pain points that they might have. So this is all hypothetical and I've given it a link and all I have to do is now if I just press this I have access to all my skills and then I can go to over here and then you have skill but we also have the outreach one. So

[11:50] we'll click on the one that we just created and we'll do that and then I'll just press enter. So right now what it's doing is actually reading the outreach skill. So now you don't have to repeat yourself multiple times or paste in frameworks all over again. You have

[12:02] access to this whenever. So now it's doing that and just based off of that it read the skill and it's given me everything I need. For example, we have these pain hypotheses which are like order fulfillment gaps, maybe fragile product in transit, cold change or seasonal demand spikes, returns or refund ops, everything like that. And

[12:19] then what I have over here is couple of emails that I can send to them. For example, a 14-day sequence. So 14 days worth of work is done now because of the skill I have built. Number one, day one,

[12:30] LinkedIn, what to say, what to do. Then an email chain. Then if I want to cold call them, what I can do is call them over here. Everything like that. Then I

[12:39] have another LinkedIn touch, another email point touch up with them and everything like that. So I have 14 days worth of work just laid out for me within a couple of seconds. And I also did a couple of personalization notes like who to target. So founder CEO is

[12:52] saying that it's likely a small team of one to three people. And right now it says that this person Dave White appeared in the searches. So I can use his contact to you know reach out to him whatever and then everything like that.

[13:03] And then also I asked it to do a full research on it. So this is the summary of what the product is and on the bonus pain points which I asked it to do beyond the stated delivery and logistical issues there are five other areas I found as well. So all of this work was done for me within couple of seconds and I have not only one day's worth of work done but 14 days worth of cold emails or messages set up and this was just in the chat feature. If you

[13:26] were to use the co-work feature in cloud as well you could do that. You could also use it in the code feature because you have access to this skill wherever in co-work hypothetically for example you can access your skills just like you would access everything in your normal chat feature but now you also have access to your calendar in co-work you have access to your actual email for it to send drafts and everything like that. You also have access to automations and schedule tasks and everything like that. So this skill once

[13:51] you have built it from notebook LM you have access to wherever you go in cloud even you can transfer the skill into other AI models like chatbt or even a Gemini as well but I personally like claude because of co-work and everything like that. So I've chosen claude today as my demo. So that's pretty much the full workflow. You use notebook's deep

[14:09] research to pull structured expert knowledge on any domain you want. Then you take that research into Claude and build a skill file that turns that knowledge into repeatable agent behavior and you end up with Claude that doesn't just kind of know your domain. It operates from a real knowledge base and gets better every time you update it.

[14:27] The library of skills you build up over time becomes genuinely valuable. And it's the difference between using Claude as a generic assistant and using it as a specialized agent that knows your work. If you want to see me apply this to a specific domain, drop it in the comments. I'll pick a few and maybe I'll

[14:42] do a dedicated walkthrough for that as well. But if you found this helpful, make sure you guys like the video and subscribe to the channel. But that's it for today's video. Make sure you guys

[14:50] are subscribed to the channel. Follow our new newsletter as well at universeai.behive.com

[14:56] as well as subscribe to the main channel World of AI and support us on X by following the Universe of AIZ as well. Until then, I'll see you guys in the next video.
