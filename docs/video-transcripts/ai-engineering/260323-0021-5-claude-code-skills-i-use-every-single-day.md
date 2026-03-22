# 5 Claude Code skills I use every single day

**Channel**: Matt Pocock
**Duration**: 16:42
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=EJyuu6zlQCg
**Transcribed**: 2026-03-23 00:21

---

## Organized Notes

**Core Premise**

- AI agents are like **middling-to-good engineers with no memory**
- You need **strict, well-defined processes** (skills) to get useful output
- Skills = **markdown instructions** that encode your engineering process
- Result: **code quality from AI has shot up**

**Skill #1: `/grill-me`** -- Force shared understanding before coding

- Only **3 sentences long** but Matt's favorite skill
- **The actual skill prompt:**
  > "Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. And finally, if a question can be answered by exploring the codebase, explore the codebase instead."
- **Design tree** concept from Frederick P. Brooks' *The Design of Design* -- exhaust all decision branches before committing to code
- Fixes Claude Code's tendency to **spit out a plan too early** in plan mode
- Sessions can produce **30-50 questions** over 30-45 minutes
- Takeaway: skills don't have to be long -- just **the right words at the right time**
- **Workflow role:** Initial discovery phase

**Skill #2: `/write-a-prd`** -- Turn the idea into a destination document

- Steps:
  1. Ask for a **detailed description**
  2. **Explore the repo** to verify assertions
  3. **Interview relentlessly** (same as Grill Me)
  4. Sketch out **major modules** to build/modify
  5. Write the PRD using a template, submitted as a **GitHub issue**
- Includes **problem statement**, **solution**, and **user stories** (agile)
- Implementation decisions kept **non-prescriptive** so the PRD stays durable
- PRD = **the destination**, not the journey
- **Workflow role:** Bridges discovery to planning

**Skill #3: `/prd-to-issues`** -- Break the destination into an actionable journey

- Converts a PRD into **vertical slices** (not horizontal layers)
- Each issue = a **thin slice through all integration layers** ("tracer bullet" analogy)
- Key principle: **flush out unknown unknowns quickly** -- do risky integrations first
- Establishes **blocking relationships** between tasks for parallelization
- Enables **parallel agent work** when blocking relationships are clear
- Example: complex PRD broken into **4 slices** with dependency chains
- His **"Ralph loop"** auto-picks unblocked issues, implements, comments, closes, unblocks next
- **Workflow role:** Converts planning to actionable tasks

**Skill #4: `/tdd`** -- Red-green-refactor for rock-solid implementation

- Forces the agent into a **red-green-refactor loop**:
  1. Confirm required **interface changes** with user
  2. **Design interfaces** for testability
  3. Write **one failing test**
  4. Write **minimum code** to pass it
  5. Look for **refactor candidates**
- Key insight: structure codebases as **few large modules with thin interfaces** -- easier for AI to navigate and test at boundaries
- **Most consistent way** to improve agent output quality
- Includes guidance on **refactoring**, **mocking**, and **deep module design**
- Caveat: LLMs are **reluctant to refactor their own code** in context -- clearing context helps
- TDD is **hard in badly structured codebases** where boundaries are unclear
- **Workflow role:** Implementation execution with quality gates

**Skill #5: `/improve-codebase-architecture`** -- Make TDD possible

- Explores the codebase to surface **confusions**:
  - Understanding one concept requires **bouncing between many small files**
  - Pure functions extracted for testability but **real bugs hide in how they're called**
  - **Tightly coupled modules** create integration risk
- Presents **deepening opportunities** (shallow modules -> deeper ones)
- Spawns **3+ sub-agents in parallel**, each proposing a **radically different interface design**
- User picks the strongest or proposes a **hybrid**
- Creates a **refactor RFC** as a GitHub issue
- **Language-agnostic** -- works in any codebase
- Recommended: run **once a week** or after a development surge
- **Workflow role:** Continuous codebase health maintenance

**Skill Sequence (End-to-End Workflow)**

1. **`/grill-me`** -- Understand the problem deeply
2. **`/write-a-prd`** -- Document shared understanding as destination
3. **`/prd-to-issues`** -- Create independent, blockable task slices
4. **`/tdd`** -- Implement with quality through red-green-refactor
5. **`/improve-codebase-architecture`** -- Maintain structural clarity for future iterations

**Key Insight**

- Treat AI agents like **humans with weird constraints** -- no memory, cloned, go straight to work
- **Garbage codebase = garbage AI output**
- These skills read like a **mini markdown book of engineering processes** for humans

**Source:** [Blog post](https://www.aihero.dev/5-agent-skills-i-use-every-day) | [YouTube video](https://youtube.com/watch?v=EJyuu6zlQCg)

---

## Transcript

[00:00] I've been an engineer for nearly a decade and in all of that time right now process has never been more important. At your fingertips now you have access to a fleet of middling to good engineers that you can deploy at any time. But the weird thing about these engineers is they have no memory. They do not

[00:17] remember things they've done before. And so you need extremely strict and well-defined processes to get those agents to actually do things that are useful. So this means that you as a developer are looking constantly for ways to steer your agents to keep them on the right track. And for me that has

[00:33] resulted in a lot of skill building. Here's the repo of all the skills that I'm using right now. Each of which I have gone through and designed. Some of

[00:40] these I use relatively rarely but some of them I use every single day. And these skills help me encode my process. So the AI has a really strict path it can walk down every single time. And as

[00:51] a result of using all of these skills, the code quality that the AI is producing has shot up. Now, if you think that process is important and that real engineering skills are important, then boy, do I have a course for you. This course is called Claude Code for Real Engineers. It's a 2 week cohort that

[01:07] starts on March 30th and for seven more days, it is 40% off. If you feel like you're behind the curve on Claude Code and you want to get way ahead of the curve in just two weeks, then blime me, this is the place for you. Let's start talking about our skills with number one, which is maybe my favorite. This is

[01:24] the grill me skill. This skill, yes, it is just three sentences long. And let's just read it out in full to describe what it does. Interview me relentlessly

[01:32] about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one by one. And finally, if a question can be answered by exploring the codebase, explore the codebase instead.

[01:44] The concept of a design tree comes from this book by Frederick P. Brooks, which is the design of design. Actually, I don't know if it comes from this book, but this book is where I saw it first.

[01:53] The design tree is this idea that as you're coming towards a design, you need to walk down all of the branches of a design tree. For instance, you might be designing a search page and you need to decide whether you want an advanced search or a text box. If you choose advanced search, then you need to figure out all of the filters and all of the sorting methods that you need on advanced search. and you keep on walking

[02:12] down the tree until you figure out your design kind of in full or as full as you can before actually committing to code. This grill me skill when I invoke it, I invoke it when I want to reach a shared understanding with the LLM. I found that relatively recently claude code will tend to just spit out a plan really early when I go in plan mode and it tends to just create a document before I feel I've reached a shared understanding with the LLM. But the grill me skill

[02:37] forces that conversation. and it forces the LLM to interview me about every single part. Here's a conversation I had with Claude recently about adding a feature to my course video editor codebase. I gave it some research that I

[02:49] done in a markdown file and I said, "Grill me. I'd like to think about adding this to the right page." It loaded up the skill and the thing I want to show you is just how many questions it asked me. So, the first thing it did

[02:59] is it just explored the relevant stuff in the codebase, which is good. Then we zoom down. We can see it asked question one, where does the document live?

[03:06] Question two, what's the UI layout? Question three, which modes get the document panel? Question four, the document life cycle? Question five, what

[03:12] does the right document tool look like? Question six, the edit tool shape. Question seven, question all the way down to question 9. Question 10,

[03:20] question 11, question 12, all the way down to question freaking 16 here. And this is a relatively short grilling session in my book. I've had sessions where I've sat there for nearly half an hour, 45 minutes with the AI answering questions on really complex features.

[03:34] you know, that could be 30, 40, 50 questions all from this absolutely tiny skill. That's one thing I want you to take from this. Skills don't have to be long to be impactful. You've just got to

[03:45] choose the right words for the LLM at the right time. And this design tree, resolving dependencies, has just been absolutely great for me. By the way, if you want these skills, then they will be at a link below. Once I have reached a

[03:56] shared understanding with the LLM, once I have grilled my idea and sort of understood all of its ramifications, if I then decide I want to implement it, then I invoke my next skill, which is a write a PRD skill. I actually did this in the conversation we were just looking at. So, it said anything I've missed or got wrong and I said write a PRD. I was

[04:14] suffixing it with user because I have some that sort of live in the project. So, that's the reason why I did that. Here's what the skill looks like. This

[04:20] will be invoked when the user wants to create a PRD. You may skip steps if you don't consider them necessary. So for instance, in the previous conversation, it said, "We've already done a deep interview. Let's move to step four." So

[04:29] step one is to ask the user for a long detailed description. Then number two is to explore the repo to verify their assertions. Number three is basically to interview the user relentlessly. So just

[04:38] a copy of the grill me skill again. Next, we sketch out the major modules you will need to build or modify to complete the implementation. We're going to look at this later because it links to skills I'm going to show you in a bit in this video. And finally, once you

[04:50] have a complete understanding of the problem and the solution, use the template below to write the PRD and the PRD should be submitted as a GitHub issue. The way that my dev flow works is I take these PRDs in GitHub. I turn them into more GitHub issues that reference the parent PRD and then I have a Ralph loop that just loops over each issue until it's done. If we go back to the

[05:10] conversation where we were before, we can see that it created this PRD here. This was 4 days ago. As you can see, we've got a problem statement. The

[05:17] article writing page currently regenerates the entire document on every AI interaction. And the solution was to add a split pane document editing experience to the article writer. Chat stays on the left. A new document panel

[05:26] blah blah blah. So this is a big feature. We're adding document editing to a kind of AI chat feature. The

[05:32] important thing here is the user stories. There are many many user stories as part of this and this comes from agile methodology and we're basically trying to describe the kind of desired behavior of our system in language which is not an easy thing to do. I still haven't properly like landed on the right format for these. This is

[05:48] just something I sort of like, but you could easily use like cucumber language for these or whatever your kind of used to do used to working with. We then zoom down to the bottom and we just sort of pass in some implementation decisions. The implementation decisions here we don't want to be like overprescriptive because we want these to be durable because if the code ends up getting out of date with the PRD, then we're going to have issues when we actually go to implement it. But you can see the theory

[06:12] here. This is the kind of uh it's a really good description of the destination that we're going to. But what we don't have from the PRD is the actual journey is the is the way we're going to get to this destination. And if

[06:24] we leap back to that conversation, this is where I use my next one, which is PRD to issues. What this does is it takes a PRD, takes the destination, and it turns it into a canon board of different issues that can be independently grabbed. So the first step in here is it locates the PRD. If the PD is not

[06:41] already in your context window, fetch it with this instruction. Explore the codebase if you need to. And then draft vertical slices. It's not always

[06:50] clear how you should break a PRD down into individual tasks. This is something that developers have been doing for yonks, right? And we've developed a kind of intuition for how to do it. In my

[07:00] opinion, the best way to do it is to break it into tasks that flush out the unknown unknowns really quickly. For instance, if you're integrating with a new kind of service or integrating two things which you haven't integrated before, then you should do that work first because it's going to give you feedback on whether your approach is even valid. The right analogy here is the tracer bullet analogy. I won't go

[07:19] into what that means, but basically each issue is a thin vertical slice that cuts through all integration layers, not a horizontal slice of one layer. In the conversation, it broke down that really complicated PRD into just four slices. It first created a kind of engine with some tests applied to it. This is

[07:36] actually quite a good vertical slice because this was the engine that was going to then power the rest of the kind of setup. If this engine wasn't working for whatever reason or it wasn't feasible, then we would need to flush that out quickly. And this is what this um breakdown does. The PRD2 issues also

[07:51] establishes blocking relationships between the tasks. For instance, number two here is not actually blocked by anything. So, it can be picked up independently to one. This is really

[08:00] useful if you have a parallel agent setup where you can actually fire two agents at it at once for instance in like background tasks. And it also means that in the future you can add other issues to this like uh QA issues that you find or things that need to be improved. And you can then establish blocking relationships between that and all of the other things. We can see that

[08:18] number three here is blocked by one the editing engine and the number four the Monaco editor toggle is blocked by number two. So I said yes to all of these and it created then all of these GitHub issues. These issues reference the parent PRD so that the uh local agent can fetch it and view it and it sort of just breaks down what to build really and crucially it references the previous user stories in the PRD. We can

[08:41] then see a comment actually from claude code that ended up implementing this. It said a pure function document editing engine with 28 tests covering all acceptance criteria. And we can then take a look at the commit that references this issue. So this was

[08:53] basically my Ralph loop came and just implemented this based on the issue, commented on it, closed it and uh then the next issue was unblocked. So so far the grill me skill can help you flesh out an idea. The write a PRD skill can help you take that idea and turn it into a document and then the PRD is or PRD to issue skill helps you then turn that destination document into an actual journey. But then how do you actually

[09:17] execute on that skill? How do you make it like how do you make the implementation really rock solid and increase the code quality of what gets produced? We have got a TDD skill. TDD

[09:28] means testdriven development. And when you invoke this skill, it basically forces the agent or encourages the agent rather to follow a red green refactor loop. Unusually for my skills, there is actually a lot in here. So it's not just

[09:41] the skill itself. It's also uh ideas on refactoring, on mocking, on what deep modules are. doing really really good.

[09:47] TDD has been the most consistent way that I've improved agents outputs. So let's have a look at what's actually in here. What we can see is I'll just skip over the philosophy stuff. I'll let you

[09:57] guys read that. We are basically looking at this workflow. Yeah. Now the first

[10:01] one here is really important. Confirm with the user what interface changes are needed. Now I made a video on interfaces and implementations recently, but let me just give you the prey. When an AI looks

[10:11] at a bad codebase, it will look at or it will see something like this where it has a ton of tiny modules here that are kind of undifferiated. They're not really grouped together. It doesn't really understand how these things relate. And so it has to do a lot of

[10:25] work kind of working out, okay, what's responsible for what? What are the dependencies? How does this actually how's the codebase even function?

[10:31] Whereas if you restructure this into several larger modules with just kind of thin interfaces on top, the interface being the functions that are actually exported from this, the uh things that the callers actually call, then it's a lot easier for AI to navigate this codebase and it's a lot easier to work out how to test these modules because you just test them at their interfaces. You test them at their boundaries. You can check out the whole video on that below. So what this TDD skill is

[10:56] encouraging here is basically trying to make these interface changes really uh top of mind for the AI to get it to understand that when it changes an interface that's an important decision it needs to take time over. You confirm with the user which behaviors to test. You design the interfaces for testability linking to a dock and then we have some more stuff around planning here. It then goes into a lovely loop

[11:18] where it writes one test at a time and it writes the test first. Now, I've talked about red green refactor before. So, I'll link the video below if you're interested. But I found that red green

[11:27] refactor with agents is incredible, and it basically does this loop until it's complete. It just writes a failing test, then writes the code to make that test pass. Then, finally, it goes through and looks for refactor candidates. I haven't

[11:39] found that this is amazing. It hasn't been brilliant because often LLMs are quite uh you know, they're quite reluctant to refactor their own code. If you were to clear the context of the LLM, then it would just sort of wipe its own memory and it would be a lot less precious about the code that it's just written. But while its own code is

[11:57] sitting in its own context window, it's quite reluctant to change it. So this TDD skill is what I prompt my Ralph loops with in order to get them to do red green refactor. Now TDD demands a lot of you, or rather it demands a lot of your codebase. TDD is really hard to

[12:11] do in a badly structured codebase because the test boundaries of this are really unclear. Should it just sort of test these modules on their own? Should it test these modules on their own? What

[12:21] are the boundaries here? Whereas, when your codebase looks more like this, then it's a lot easier to test because the module boundaries are really clear. So, wouldn't it be great if there was a skill that made your codebase look more like this? Well, isn't it nice? We've

[12:34] got an improve codebase architecture skill. The process for this one is that we explore the codebase and explore it kind of like naturally as an agent would. We're trying to find confusions.

[12:44] We're not like we're trying to sort of surface naturally what the AI finds confusing so that it can then sort of like help it out later. Where does understanding one concept require bouncing around between many small files? Where have pure functions been extracted just for testability, but the real bugs hide in how they're called?

[13:02] Where do tightly coupled modules create integration risk in the seams between them? All of these are questions that a senior engineer would be asking about your codebase. Number two is you present candidates. So you present a numbered

[13:13] list of deepening opportunities. In other words, opportunities to deepen shallow modules in your codebase into deeper ones. The user then picks a candidate and then you design multiple interfaces. So it says to spawn three

[13:27] sub aents in parallel, each of which must produce a radically different interface for the deepen module. In other words, we're extracting that code and designing possible ways that it could look in the future. designing it in multiple different ways is a really great way that you can then decide on the right idea. I've seen this agent

[13:43] spawn like five different sub aents for a really big refactor. The coolest thing about this is you don't need to know a lot about interface design in order to get this working. After comparing, give them your recommendation which design you think is strongest and why. And if

[13:56] elements from different designs would combine well, then propose a hybrid. Notice that I've made this really language agnostic, really kind of sort of everything agnostic really. You can just run this in any codebase and just get a decent answer for how it could be improved. There might be four or five

[14:11] candidates that really could use some work, but really I think you should only be sort of doing one of these at a time because they really are quite hard to get your head around and they require a human in the loop to sit with them and improve the codebase because these decisions do require taste. Finally, it creates a GitHub issue. So, it creates a refactor RFC as a GitHub issue using GH issue create. Usually once this is done,

[14:34] I will then go with my PRD to issues uh skill reference that GitHub issue that's just been created and get it to you know this describes the destination. We then need a journey to get there. So just doing this every so often in a codebase you know once a week just to identify opportunities or if you have a sudden surge of development and you kind of create a whole sort of extra wing of features then this uh skill will be really really useful in just making sure it conforms to the rest of the codebase.

[15:01] making sure that it's not uh too sloppy. And as you keep running this, as you keep refining your codebase, you're going to notice the quality of the agents output goes up. Because the old adage really does apply. If you have a

[15:12] garbage codebase, then the AI is going to produce garbage within that codebase. Because to be honest, if you took all of these skills and just said, "Okay, this is like a little mini markdown book of processes for humans," then it wouldn't look out of place. I found that the most successful way to get code quality up from agents is just to treat them like humans. Humans with weird constraints.

[15:32] Sure, humans that uh have no memory and are just sort of cloned come out of the birthing pod and go right to work. But if you like me think these real engineering skills are super important, then this course is absolutely for you. What I noticed while I was creating the course is that I'm really not teaching Claude code that much. I'm teaching kind

[15:49] of what are sub aents. I'm talking about the constraints of LLMs, the sort of weird smart zone, dumb zone stuff with the context window. We're talking about steering, which is essentially just a way of documenting stuff inside your codebase, how to tackle massive tasks, understanding tracer bullets and building those into our skills, understanding how to build really great feedback loops and doing exercises with them, and crucially, how to hook these up to an autonomous agent. Every part of

[16:14] this course just sort of like leads onto the other, and I'm super happy with how it turned out. So, over the course of two weeks, you'll be working through that self-paced material with me as your guide in Discord and on live office hours. And if that sounds fun to you, then the link is below. Thanks for

[16:28] watching, folks. I'll be coming back with a lot more stuff this week. What would you like me to cover next? I find

[16:33] the intersection between this real engineering and AI is like it's such a awesome place to make content about. But anyway, thanks for watching and I will see you in the next
