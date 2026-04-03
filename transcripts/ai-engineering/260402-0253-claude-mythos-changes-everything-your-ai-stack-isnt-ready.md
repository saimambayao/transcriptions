# Claude Mythos Changes Everything. Your AI Stack Isn't Ready.

**Channel**: AI News & Strategy Daily | Nate B Jones
**Duration**: 31:20
**Language**: en (manual) [yt-dlp subtitles]
**URL**: https://youtube.com/watch?v=hV5_XSEBZNg
**Transcribed**: 2026-04-02 02:53

---

## Organized Notes

**The Arrival of Claude Mythos (Capybara)**

- **Claude Mythos (Capybara)** has leaked as the first model trained on **Nvidia's new GB chips (GB-300)**. Anthropic has confirmed its existence and introduced a new lineage name, "Capybara," signaling a departure from the Sonnet/Opus naming scheme.
- This model represents a **step change** in AI capability, not just a incremental improvement. It is expected to be the most powerful model in the world upon release, which could be as soon as next month.
- **Security Implications**: Security researchers report that Mythos is "terrifyingly good" at finding zero-day vulnerabilities. In one test, it immediately found vulnerabilities in **Ghost** (a 50,000-star GitHub repo) that experienced humans had missed. Anthropic is proactively allowing researchers to battle-test the model to harden defenses before the public release.

**The "Bitter Lesson" of AI Development**

- The core lesson for 2026: **As models get more powerful, simpler systems work best.** Humans often try to add value through complex scaffolding and procedural instructions, but these often constrain smarter models.
- **The Simplification Mandate**: When a model is 2-3x smarter, 30-50% of existing procedural prompts (classification, step-by-step reasoning) become obsolete.
- **Job Skill Evolution**: The most valuable skill in 2026 is the ability to anticipate model improvements and **de-complexify** your AI stack before the next generation arrives.

**Four Key Areas to Audit for Mythos-Readiness**

1. **Prompt Scaffolding**:
   - Audit system prompts at a **per-line level**. Ask: "Is this here because the model needs it, or because I needed the model to need it?"
   - Move from **procedural "how"** (sequences, checks) to **outcome-based "what" and "why"**.
   - Let go of the process; specify the goal and provide the necessary guardrails.

2. **Retrieval Architecture (RAG)**:
   - Smarter models are better at deciding what to put in their context window.
   - Instead of complex hand-rolled retrieval logic, focus on providing a **well-organized, searchable repository** (documents, code, file system).
   - Trust the model to find what it needs within that context.

3. **Domain Knowledge Hardcoding**:
   - Evaluate which business rules can now be **inferred from context** rather than hardcoded.
   - Example: House styles for reports can be inferred from a single example rather than being defined in a 10-line instruction.
   - Over-specifying methodology can actually degrade performance on more intelligent models.

4. **Verification and Evals**:
   - Move away from intermediate human-in-the-loop checks. Humans are now the **bottleneck**.
   - Shift toward a **single, comprehensive eval gate** at the end of the process that tests both functional and non-functional requirements (clean code, exception handling, policy compliance).
   - If a human handoff (e.g., between Excel and PowerPoint) exists, automate it.

**Economics and Strategy**

- **Premium Access**: Mythos will likely be expensive to serve and may initially be restricted to **premium plans (e.g., $200/month)**.
- **The superpower gap**: Individuals and companies who invest in "cutting-edge" intelligence will gain a massive edge over those staying on standard "pro" plans. High-end model users will effectively have superpowers.
- **Multimodel Strategy**: Companies need a reliable way to categorize problems—deciding which require "Mythos-shaped" intelligence versus standard models.

**Architectural Patterns for 2026**

- **Outcome Specifications**: Define the intent (e.g., "Resolve this user's issue per policy X") rather than the steps.
- **Constraint-Based Guardrails**: Define what must *not* happen (e.g., "Never disclose financial data").
- **Tool Definitions**: Put more work into making tools discoverable and effective for the model to choose from.
- **Multi-Agent Coordination**: Favor **hierarchical coordination** (2-agent hierarchies) over "agent swarms." Take Mythos seriously as the **planner** of your software.

*Quotable Quotes:*

> "The first thing you should do if you are in IT or security as soon as mythos comes out is to say let's battle test it against our own systems and let's see what vulnerabilities it finds." [01:46]

> "The bitter lesson is that simpler works best. We as humans think we have a lot of value to add... we can complexify. But simplicity works best." [03:07]

> "As much as the art of prompting for the first couple years of LLM was about what you put in, increasingly the art of prompting is about what you leave out." [13:58]

> "If you are depending on humans and human handoffs as a key part of your agentic software development pipeline, you're in trouble." [16:50]

> "The people who have that $200 a month plan are going to effectively have superpowers. Think about whether you want those superpowers or not." [21:05]

---

## What This Means for Your Work

As a solo developer building government-scale systems like **e-Bangsamoro** and **OBCMS**, the impending release of **Claude Mythos** represents both a massive opportunity and a call to radical simplification. Your current setup—135 specialized skills and a multi-agent Obsidian memory—is your greatest asset, but Nate Jones' "Bitter Lesson" highlights a potential trap: **over-scaffolding**.

1. **Re-evaluating the "Parliamentarian" Agents**:
   Your `Parliamentarian` app relies on specialized agents for legal analysis and BOL interpretation. With Mythos, many of the procedural checks you've built into these agents (like "first classify the intent" or "check for specific BAA numbers") might be better handled by giving the model a flatter, better-organized knowledge base and a broader outcome spec. You should prepare to "delete" portions of your system prompts that compensate for model limitations.

2. **Simplified RAG for Bangsamoro Law**:
   Your current pipeline (/bangsamoro context → domain skill → /fact-checker) is robust. However, as Mythos demonstrates "terrifyingly good" retrieval and reasoning, you could move toward a more "flat" retrieval strategy. Instead of complex routing between 78 BAAs and 546 resolutions, you might simply present the relevant index and trust Mythos to "go find what it needs" more reliably than previous models.

3. **Scaling e-Bangsamoro as a Solo Dev**:
   The video's emphasis on automated evals is critical for your work. Since you are the sole developer of high-stakes platforms like `Tarbiyyah-MS` and `BangsamoroHR`, you cannot afford to be the bottleneck for code review. Implementing a "single comprehensive eval gate" using Mythos-level intelligence would allow you to move from "writing code" to "architecting outcomes," truly leveraging the 10x multiplier needed for government-scale projects.

4. **Strategic Investment in "Superpowers"**:
   Given the high stakes of BARMM governance and your role as a "Bangsamoro governance consultant + solo dev," the potential $200/month premium plan for Mythos is not a cost, but a critical infrastructure investment. Access to "Capybara-tier" intelligence will likely be the difference between building a "good" portal and building one that is secure against zero-day vulnerabilities in a high-risk government environment.

### How This Can Improve Your Gemini Skills and Workflows

1. **Skill Optimization** ([[skill-optimizer]]):
   You should run a full audit of your `skills-bucket` using the `skill-optimizer`. Look for "procedural croft"—instructions that tell the model *how* to research or *how* to draft. As you move toward Mythos, these should be replaced with clearer **Outcome Specs** and **Guardrails**. For example, your [[bill-drafter]] skill could be simplified to focus on the *intent* of the bill while providing the 39,000-word Bill-Drafting Manual as a primary resource, letting the model infer the structuring rules.

2. **Automating Handoffs**:
   The video suggests automating handoffs between artifacts. Your current workflow often moves from a [[research-pipeline]] to a [[policy-paper]] to a [[presentation]]. You should look at creating a "meta-skill" or using [[sp-dispatching-parallel-agents]] to automate the translation between these formats, ensuring that the 99% accuracy of Mythos is preserved across the entire document chain without human intervention.

3. **Multi-Agent Memory** ([[obsidian]]):
   Your Obsidian vault is already a "planner-level" memory. You should lean into the **Hierarchical Coordination** pattern mentioned. Instead of many specialized agents, you could use a high-level "Architect" agent (Mythos) that spins up "Instantiated Agents" from your existing skill library. This maps perfectly to your `appmanager` meta-skill concept.

4. **Fact-Checking Evolution** ([[fact-checker]]):
   The [[fact-checker]] is currently a separate step. With Mythos, you might incorporate the verification directly into the generation process (self-correction) or have a second "Mythos pair of eyes" perform the check, reducing the latency between drafting and verification.

---

## Transcript

[00:00] There are moments in AI when everything changes and we just had one of those the last few days. Claude Mythos leaked. Now Claude Mythos is the first model as far as we know that has been trained on Nvidia's new GB chips. It is a massive model. It is a step forward. Anthropic has confirmed its existence and they've given it a new lineage name. So it won't be called Sonnet. It won't be called Opus. It appears to be called Capy Bara. 

[00:25] I don't know why we've switched to furry animals, but here we are. This is the biggest model in the world. It is by most measures according to Claude and it is going to be the most powerful model in the world. But don't just take my word for it. Don't just take anthropics word for how powerful it is. Look at what security researchers themselves are saying. Security researchers themselves are saying that cloud mythos is terrifyingly good at finding vulnerabilities in your own infrastructure better than a human. In fact, one of the most experienced security researchers in the world stood up at a conference in San Francisco in the past few days and said that Claude Mythos immediately found zeroday vulnerabilities in Ghost, which is a 50,000 star GitHub repo that has never had major issues before. And as soon as Mythos was let loose on it, it found a bunch of issues that even the world's best security researchers haven't found.

[01:17] And this is why Anthropic is taking the unusual step of allowing security researchers to dig into Mythos to battle test Mythos against some of the most popular utilities on the internet and to harden up their defenses ahead of time because as soon as Mythos is released, Mythos is going to be able to act as a threat to any IT repo out there and identify vulnerabilities that even good security researchers haven't been able to find, which immediately suggests that the first thing you should do if you are in IT or security as soon as mythos comes out is to say let's battle test it against our own systems and let's see what vulnerabilities it finds. That is that is job number one day zero you got to do that. But let's go beyond that.

[02:02] Let's look at what Claude mythos means. I want to be really honest with you. This model is one of the inflection points in 2026 that we all need to pay attention to. This is a chance to catch up before the train leaves the station. And I know that you may hear from me, things are getting faster. Things are getting faster a lot. But guess what? That's what it's like when you're on an exponential curve. Things keep getting faster. And I'm here to tell you, this moment before Mythos release, and it may release as soon as next month or the month after, this moment is your chance to get things figured out before it arrives and upends everything. And I don't just mean about security. I mean how you build stuff, how you prepare etc. Why is that? Well, when models get bigger, they force you to simplify. They force you to think what can I delete about my systems and my practices because the model can do so much more now that that it couldn't do before. And that is what we have to understand. That is what we would call the bitter lesson of building with LLMs. We as humans think we have a lot of value to add to these models. We can add our judgment. we can complexify. We can add a lot of scaffolding and systems around these models and it will make them better. And as they get more powerful, the bitter lesson is that simpler works best. 

[05:00] And so I'm going to go through and in this video I'm going to lay out some of the things you should be checking ahead of time. But there's a larger thing that you should take away, which is simply be sure that you are taking the idea that the LLM can do a lot more seriously. And we'll get into what that is. We'll cover mythos when it comes out. We'll talk about all of that. But for now, as we go through the next few questions, as you audit yourself, as you think about whether you're ready for mythos, that's the larger lesson. But anyone can tell you that. What are the what are the specific questions that help you know if you're ready for a big model change? If you're ready for effectively a step change. And by the way, I know that models come out all the time, but step changes are more rare. And what we get when we do a pre-training run on GB300s and it's much larger and more powerful underneath is we get the scaling law in effect. Right? So what I'm trying to tell you is yes there'll be another model along from somebody in the next week or so but until mythos comes out and there will be other models that are in that lineage that come out from other model makers that are also big that are also trained on GB300 those are the step change that we're going to see in the first half of the year. And so you need to learn to differentiate between the models that are 5 10 15% better and the models that are significantly better, a step change better. And that's why this is a big deal because we are going to have another lurch up where the models are going to get significantly stronger in the next few months. And and you need to get ready for that now. 

[06:00] Okay, here's your questions. I'm going to give you four specific things to look at that are going to likely break when Claude Mythos comes out and you need to take them seriously. If you are building in AI at all, this is going to come up. Number one is your prompt scaffolding. How you think about prompting to drive results. Ask yourself, and this is not a per prompt document question. This is a per line question. Really dig in. Is this instruction here because the model needs it or is it here because I needed the model to need it? This is the question that I want to really dig into. Anthropic's recommendation is very unambiguous here. Consider adding complexity only when it demonstrabably improves outcomes. 

[07:00] This is going to be more and more the case, right? We are going to more and more be asked to communicate with the model what and why we need something in the end and less and less about how. So for example, let's say you have a customer support agent with a 3000 token system prompt and half of it is procedural, right? Like first classify the intent, then check your response for hallucinated URLs, then do X, then do Y. That sequence was written down because the model would skip knowledge checks enough of the time that it was needed. Think about whether you're really going to need that. When a model gets two or three times smarter, you may be able to delete that like 30 40 50% of that 3,000 token prompt because so much of the procedural is just not needed when the model is more intelligent.

[08:00] Let's say you're not building agents. What's the implication for you if you're just chatting? If you're using co-work and you're wanting to get work done and you're less technical, it's pretty simple. Ask for what you want in the end and explain why in plain language. And you don't need to elaborate on how to get there. As long as the model has access to the inputs it needs, the data it needs, it's going to get there on its own. Increasingly across 2026, this is the bitter lesson we have to learn. All of the way we have described process, the things that are precious to us are things that are associated with our ability to execute work in a certain series of steps and somehow we've decided that's an important reflection of our work identity. What cloud mythos and similar models are going to teach us is that that doesn't matter anymore and what matters is the outcome and our ability to name the outcome and let go of the process.

[09:00] Lesson number two is about retrieval architecture and memory. You're basically asking how is the model changing the way it relates to memory based on the model's gain and capabilities. And so another way of looking at it is to say in the past we had to carry a lot of the logic for retrieval on our side so the model would retrieve correctly. But really how much of my retrieval logic should belong to the model if the model's smarter. This is a much more nuanced take than takes like that say sort of rag is dead. If you're in a large context window situation, if you have like a million tokens, 10 million tokens, 100 million tokens, increasingly you should start to think about how the model wants to handle retrieval for that situation and how the model thinks it can handle it efficiently. And you should think less about predetermining how all of that works. 

[10:00] Once you've made those initial decisions, a lot of the rest of it with these very powerful models essentially relies on you being able to present a really well organized searchable repo of some sort. Maybe it's documents, maybe it's code, etc. Maybe it's the file system on your computer if you're non-technical. And then you need to say you go ahead and have a look. You look for what you want. And you need to trust the model to find what it needs to find. And there again, you see the theme. The theme is we have to let go so the model can do more. Our goal increasingly is to say here is the goal, go get it done and then to measure success. And that's it. That is the goal. And the smarter the model gets the more our work resolves down to that. and we need to get out of the way. And that in my observation is really hard.

[12:00] Number three, look at how much you have to hardcode domain knowledge versus how much the model can infer. In other words, when you're thinking about these things that you want to emphasize over and over again to a model, ask yourself, which of these business rules did I write down? Because the model could not infer this from context, and which of these can I actually let go of? This the whole point of the scaling law is that intelligence gets better at reliably answering your query. You should count your rules. You should count the things you have to remind the model of. Ask yourself, do you really need to fill the token window for better models with this? Be prepared to let go of some of that. 

[14:00] I had an example recently where there was a prompt that I was using around how I do research. And I'd been using it for a couple of model generations. And one day I forgot to put the full 10-line prompt in and I just put a oneliner and said go research and I got a better result back because the 10line prompt was over constraining my model. It had hard-coded my domain knowledge about what resources to look up, etc. And that had been really good two model generations ago. And now I needed to let it go. As much as the art of prompting for the first couple years of LLM was about what you put in, increasingly the art of prompting is about what you leave out. It's still an art. It's still hard. You still have to prompt. And the skill is valuable. It's just that the skill is evolving because the models are getting better.

[15:00] Question number four, this one's all about, did the model do what we asked it to do? Can we sniff check it and show that it worked? Now, if you're doing non-technical work, the answer is going to be increasingly clear. One of the challenges of working with good models is learning to make sure our bar is really high. Don't be afraid just because this model is really good to look at something it produces like a PowerPoint deck or an Excel and say this isn't quite right. You got 99% of this right, but this is the 1% I want fixed. Apply your high standard. That's how we get good work. That's how we don't pass slop on. 

[16:00] I would say we are moving toward a point where we want one eval gate at the end of the software process and it needs to check absolutely everything and send things back when it doesn't work because if we do intermediate evals along the way net there's enough right about what these systems build it's just not worth it. Simplify, simplify. Just write the eval at the end. And when you write the eval at the end, make sure that it tests absolutely everything. Your functional requirements, your non-functional requirements. If you are depending on humans and human handoffs as a key part of your agentic software development pipeline, you're in trouble. And there is sort of an analogy there for non- tech folks. If you are depending on humans as a handoff between PowerPoint and Excel and you're doing AI for both of those pieces, you should be looking seriously at whether you can automate those non- tech artifact handoffs because Mythos can help you do that.

[18:00] Enthropic basically confirmed that these are going to be very expensive models to run. You want to be very efficient with them. You want to make sure they're using the tokens as efficiently as possible. You don't want to clutter them up with a bunch of human described process. You want to use them as effectively as you can. I am willing to bet you that Mythos when it launches is only going to initially be available for max plan users for CLA because it's so expensive to serve. And we are headed toward a world where increasingly the first and best models are only going to be available on those premium plans because of how expensive they are to build and train and run and serve. And so we need to think to ourselves like if you're thinking about your future, about your career, you need to ask yourself basically, am I in a position where I can invest in intelligence in one of these plans in order to get access to this and then I will leverage it to the hilt and I will make it worth it. 

[20:00] We are going to be in a position in a few months, 6 months maybe less, where you start to see the cost come down and you start to instead see more expensive models come out that are even better than Mythos. And so really when you start to think about what you're investing in, think about it as what trajectory, what curve do I want to be on? Do I want to pay to be on the cutting edge curve and I'm going to use it to the hilt and I'm going to build really cool things and I'm going to learn and I'm going to leverage it to 10x myself, etc. or do I want to be a step behind on like a pro plan or whatever the 20 buck a month plan is? You might think, oh, but talent will make up for it. No, human talent will not. Like increasingly the whole point of human talent is to simplify and get out of the way so that AI can do its thing. And the bigger the models get, the more that becomes obvious. And Mythos is one of those moments when I think it's going to be very very obvious that we are in a different world and that the people who have that $200 a month plan are going to effectively have superpowers.

[22:00] I fully expect that the leaked blog post that came out on the anthropic servers is broadly correct. It is going to be a big jump in coding. It is going to be a big jump in the ability to produce excellent artifacts like Excel and PowerPoint. Is going to be a big jump in the ability to reason. It is going to be a massive jump in cyber security and more. We should take that seriously. When you look at what mythos is going to mean, you should assume it means a step change that's coming in the next month or two. I've been telling you 2026 isn't slowing down. This is an inflection point. Pay attention.

[23:00] So, what does a simpler system look like? What does a mythos ready system look like? Number one, make sure you have very clear outcome specifications. Specify your intent in a way that makes sense for a smarter model. Let me give you an example. Back in the customer service world, let's say what you want to specify is resolve this customer's issue using our knowledge base, our policies, and our account history. The customer should leave satisfied, and the resolution should comply with our return policy. That is actually a decent outcome specification. Compare that to what most production systems I see look like. It's essentially a process, right? Well, first classify the intent into one of 14 categories. Then route to the appropriate handler. Then retrieve the top five knowledgebased articles using hybrid search. You see the difference? The outcome one just says I need to resolve the issue. You may not be able to do that today with today's models. But be ready to do that. 

[24:00] Number two, think about your constraints and guard rails. These are things that must be true regardless of how the model achieves the outcome. Because when you give the model more flexibility, you need to be more clear about your constraints and guardrails. For example, never disclose customer financial data. Always verify refund eligibility against our policy. These should survive model upgrades because they represent ongoing business rules. 

[25:00] Number three, think about the tools your model can use. You want to make sure you have an excellent set of tools that have the right capabilities where a model can look at the tool set and say, I know what this does. Number four, and then last but not least, if you're thinking about larger aentic software, we're going to go back to multi-agent coordination patterns. Long-term planning with agents and what it means to let an agent like Mythos spin up agents from a variety of capability sets to get a task done. You need to take the idea that Mythos is the planner of your software more seriously. And all we're doing is extending the current pattern we see at factory.ai, at Cursor, etc. These models are more capable. You're going to give them more to work with. You're going to be more confident that they will get it done well. 

[27:00] We're going to start to architect in a sense technical flows for non-technical work. our under the desk software, our software we build as nontechnical people is going to get increasingly sophisticated because we're going to have access to models that can do increasingly sophisticated things just by communicating an intent in plain chat. it's increasingly going to be possible to not just build one for your personal use that you start up personally on your laptop but like that you just build and you can deploy and maintain for the family and it's not even going to be something you think about as a piece of software because you never touched the code it just got built for you because you specified it. And so if you're looking at this from a role perspective, from a team perspective, you should be stepping back and asking yourself, how much of my role is compensating for a model's limitations today versus how much of my role is really thinking about how to architect and correctly aim artificial intelligence so it accomplishes a lot of work. That's the part you want to be on, right? That's where you want to lean your role.

[29:00] All right. So what does this mean for you? I want to step back and simplify this in the spirit of mythos. You need to take the idea that we are going to keep seeing model generations getting better very very seriously. We are not hitting a wall. That means you need to think across your role and across your technical systems about how you can dramatically simplify. How can you simplify so that the model has room to be intelligent? If you take one thing away, that is what I want you to take away. The challenge is to grow by being able to simplify what you ask the model to do against a larger outcome set so that we get out of the way and let the model do its job. And we focus on making sure that we are aiming the model in the direction of a big cool goal. And we focus on making sure we're building the pipeline and the support and the tool availability and the availability of data so the model can do its job. 

[31:00] So, Claude Mythos is coming. The inflection point is here. This is another one of those moments when you need to be able to catch the train before it leaves the station. I hope this gives you a set of actionable recommendations to go with today to actually get ready for this. If you want to be ready day one, your systems need to be ready to simplify. Get ready. It's coming. It's not going to be that long. It's a matter of weeks now.
