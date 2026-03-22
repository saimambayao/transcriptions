# Building a REAL feature with Claude Code: every step explained

**Channel**: Matt Pocock
**Duration**: 44:16
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=hX7yG1KVYhI
**Transcribed**: 2026-03-23 00:21

---

## Organized Notes

**Project Context & Setup**
- Matt Pocock demonstrates his **real-world workflow** using Claude Code on his **course video manager** application (~1,200 commits, ~637 closed issues)
- The app is a **React Router + TypeScript + Node** stack using **Drizzle ORM**, **Postgres**, and **Effect** for backend logic
- The app manages courses, lessons, sections, video editing, thumbnail editing, and publishing -- all run **locally** (not deployed)
- Key concepts: **ghost lessons** (exist in DB but not on disk) vs **real lessons** (exist on both DB and file system)

**The Grill Me Session**
- Purpose: **road-test and harden vague ideas** before implementation by having the AI ask probing questions
- Matt dictates rough feature ideas into the **grill me skill**, which initiates an **explore phase** (a sub-agent that reads many files and returns a summarized context to the parent agent)
- The AI challenged his assumptions -- e.g., pointed out that the **course write service** already handles deleting both ghost and real lessons, but the **UI was the gap** (no direct delete option exposed)
- The AI asked **"Willow Reagan-style" questions** -- smart, targeted questions at exactly the right point in the process (e.g., "Does direct create apply inside ghost courses too?")
- Matt sometimes **drives the conversation** and sometimes **lets the AI drive** -- the skill is flexible both ways
- He also used the **"by the way" side question** feature for quick contextual questions without polluting chat history
- The session produced **8 bullet points** of clear requirements after ~22 minutes of discussion

**Feature Requirements Produced**
1. **Course file path becomes nullable** (schema change for ghost courses)
2. **Ghost course creation** -- only asks for a name, no file path
3. **Ghost course UI** -- hide publish and export actions
4. **Create real lesson button** -- available in both real and ghost courses; in ghost courses triggers materialization cascade
5. **Create ghost lesson** -- works as today, available everywhere
6. **Delete action for real lessons** -- purges from disk and DB in one step
7. **Delete action for ghost lessons** -- unchanged
8. **Convert to ghost** -- stays for real lessons you want to keep planning but remove from disk

**Ubiquitous Language**
- Inspired by **Domain-Driven Design** -- maintaining a shared **glossary of terms** between the developer (AI) and the domain expert (human)
- Key terms defined: **ghost lesson**, **ghost section**, **ghost course**, **materialize** (transitioning ghost to real), **materialization cascade** (chain reaction when materializing a lesson inside a ghost course)
- The ubiquitous language file helps the AI **search precisely** and enables **clean communication** (e.g., "there's a bug in the materialization cascade" is immediately understood)
- Matt committed the updated ubiquitous language document as a standalone step

**Write-a-PRD Phase**
- After the grill me session, Matt invoked the **write-a-PRD skill** to generate a Product Requirements Document
- The AI performed another **explore phase** to sketch out **major modules** before writing the PRD
- Matt reviewed the **module interfaces** (not implementation details) -- e.g., whether a new method `materializeCourseAndLesson` should exist vs modifying the existing `materializeGhost` method
- He decided **not to review the PRD itself** -- trusting the AI's summarization ability from the rich Q&A conversation
- The PRD was submitted as a **GitHub issue** for later pickup by the AFK agent

**PRD-to-Issues Phase**
- The PRD was broken down into **individual GitHub issues** with **blocking relationships**
- Initially produced 6 issues; Matt felt some were **too granular** and merged two together, ending with **4 slices**
- Each issue includes: link to parent PRD, acceptance criteria, blocking dependencies, user stories, and testing decisions
- Matt did **not review individual issues** -- they are expansions of the PRD content he already validated

**The AFK Ralph Loop**
- **Ralph** is an AFK (away-from-keyboard) agent that runs in a **Docker container**, pulls GitHub issues, and implements them sequentially
- It mounts the working directory, makes commits, and patches them back to the local repo
- Ran with `pnpm ralph` with a max of **100 iterations**; completed after **5 iterations** producing **6 commits**
- Matt walked away for **~1.5 hours** (walk, tea with parents) while Ralph worked
- Key requirement: Ralph must **run tests and type checks on every commit**
- The "**day shift / night shift**" concept: human does the thinking (grilling, PRDs, issues) during the day; Claude implements AFK during the night

**The QA Loop**
- Matt created a **QA plan** (saved as a GitHub issue) by asking the AI to analyze the last 5 commits
- QA process: manually walk through the plan, use a **feedback button** in the app UI to submit bugs/feature requests as GitHub issues
- Found **7 issues in ~8 minutes** -- mix of bugs and missed features (e.g., missing confirmation modal for delete, no loading state, git repo edge case)
- **Ralph ran in the background** fixing issues while Matt continued QAing -- parallelizing QA with bug fixing
- Edge cases discovered in QA that were **impossible to predict** in the grill me session (e.g., non-git-repo failure state causing DB/filesystem desync)
- This validates Matt's belief that **specs-to-code approach will never fully work** -- QA iteration is essential

**Key Workflow Insights**
- **Focus on inputs and outputs**, not code -- review interfaces, modules, and behavior rather than reading every line
- **The grill me phase is the hard part** -- once requirements are solid, implementation is "on rails"
- **Modules and interfaces matter more than implementation** -- designing testable, well-named units using ubiquitous language
- **Token efficiency matters** -- grill me avoids the `ask_user` tool (JSON wrapping overhead); explore sub-agents keep parent context lean (~40k tokens after 22 minutes)
- **Prototyping vs. building tradeoff** -- sometimes it is better to just build one way and iterate via QA feedback rather than prototyping multiple versions
- **Flexible backlog approach** -- anytime you can queue up bug fixes and let Ralph handle them
- The **Effect library** makes it easy to create testable, composable service units in TypeScript
- Matt's aspiration: **parallelize multiple Ralph loops** (team of agents), but sequential loops create useful gaps for deep focus work

---

## Transcript

[00:00] I've been posting a lot recently about uh things you should do with Claude code and mostly I've been approaching it from the kind of philosophy angle. In other words, kind of everyone's thinking this is a new paradigm shift, but actually just the stuff we've been doing for 20 years is really really good with claw code. You get the most out of it when you treat it like someone you would delegate to in your team. In other

[00:19] words, you focus on the architecture, you focus on making sure that you've got good feedback loops. you focus on all the things we've been doing for the last 20 years, not planning too much up front, all that stuff. And in all the comments, people have been saying, "Show us something practical. Show us you

[00:34] doing it." And so, this is that video. I have no idea how long this video is going to be. I have no idea exactly what

[00:41] we're going to cover. I'm just going to go into actually doing some work with Claude Code in my work repo and I'm going to talk you through it. I'm going to show you all of the skills I'm using.

[00:50] I'm going to show you my process and we're just going to give you all the context you can on how these tools are actually used. And if you dig this then I'm running a cohort in a couple of weeks for Claude code for real engineers. It is 40% off this week and it teaches you either teaches you the skills that you need to do real engineering or it gives you the conversion course you need to take the existing skills you have and apply them to this new age. So if that sounds good

[01:14] to you then the link is below. Okay, let's start by understanding the project that I'm in and what point it is in in its life cycle, all that stuff. This is my course video manager. It's at its

[01:24] about, you know, 1,200th commit. I've closed around what 637 issues on this project. And what I'm using this for is this is my main kind of entry point for anything I do regarding creating content. In other words, I create videos

[01:38] on here. I organize my courses on here. I post videos on here. I do thumbnail

[01:43] editing on here. I do writing on here. It really is my one-stop shop for everything I need to do my job and it's amazing. In terms of the code, it's a

[01:51] React router application which uses uh TypeScript and Node and uses Drizzle for the database OM uses Postgress as its database. Does some a lot of testing with Vest. And the way I run this is I don't actually deploy it. I just

[02:07] basically run it locally. So I just tend to run start. I build it and I'm just, you know, uh run it with the start script. This is a confusing video for me

[02:16] to make because actually right now I'm recording the video that I'm making on the course video manager. Here you go. This is me. This is the uh clips that

[02:24] are being detected from the uh video that I'm recording. And there you go. That's the previous clip. This is a

[02:29] confusing video to me to make. You know what I mean? This is just got loads of stuff here. This is what the main view

[02:33] looks like. We've got courses down the lefth hand side here. Then we've got lessons and sections within those courses. And the stuff I want to show

[02:40] you is inside the free videos over here. Inside the app, I've got a concept of ghost lessons and real lessons, which you can see on the filters here. These ghost lessons basically don't exist on disk. And I need to rightclick the

[02:52] lesson and say create on disk for it to actually create the lesson on in like a repo in the disk. And the logic for this is fairly complicated because I can turn this back into a ghost here. So, and then when I do, I need to delete all of the files that are on the file system.

[03:08] convert it back to a ghost. The idea here is that it lets me plan and kind of create courses in the same UI, which ends up being really, really nice. But the thing I want to add are some enhancements here. So, I want to be able

[03:19] to when I create a lesson, I shouldn't just need to create a ghost. I should be able to add a real lesson instead of a ghost lesson. Same when I delete a real lesson, I should be able to just delete it instead of needing to turn it into a ghost first. So, this one here. Now,

[03:33] this part of the codebase is really well tested and so this should be a relatively simple build. But there is another thing I want to do as well, which is I want to when we go up to these courses up here and add a new course, I want to be able to basically create a ghost course, a course that doesn't yet exist on the file system because currently every course needs an entry in the file system. So that is my idea. I've got a very loose set of

[03:56] requirements here and this is maybe how you enter most days as a developer. you have some small tweaks that you need to make to your application that are based on some vague ideas. Maybe those are ideas that you've come up with. Maybe

[04:07] those are ideas that have come from somewhere else. And the first thing you need to do is actually road test those ideas and harden those ideas. But the first thing we're going to do is open this up in VS Code. And we're going to

[04:17] um go into this and say grill me. And I'm going to use my dictation tool to dictate some stuff into here. The way that we handle ghost and real lessons is a little bit cumbersome in places. It's

[04:28] annoying that you have to create a ghost lesson before you then create a real lesson. And it's also annoying that when you delete it or delete a real lesson, you can't just delete the real lesson. You have to turn it into a ghost lesson first. Now, at this point, I'm thinking,

[04:42] do I also in this session want to tackle the other thing? Do I want to tackle the idea of ghost courses as well? My decision space for that is like, will this crowd out the grill me session or will it all actually fairly seamlessly link together? Because the idea of this

[04:58] grill me session is I'm going to create a document out of this that I'm then going to use to um do future builds on basically. So that's my decision here is do I want to create a PRD a product requirements document that has both of these things in or are these separate concerns that I need to separate into separate PRDs. I'm going to say that this stuff actually sort of belongs together but I'm just making that decision kind of arbitrarily really. I

[05:20] also want to extend the courses functionality so that it allows me to create a course without having a file path. This would be a kind of ghost course, a planned course that I haven't actually decided whether I'm going to build yet. Now, this second section here, I haven't really explained the why. That's something that's on my mind

[05:41] now. I've sort of like I've explained what I want the feature to do, but I haven't explained why I want the feature to exist. It's always really important when you enter these sessions that you explain the why to the LLM. Because

[05:53] sure, if the LLM has the what, then it understands what you want to build. But if it doesn't know the why, then it can't suggest alternatives. The reason I want this is so that I can plan courses freely without needing to commit to an exact shape on the file system.

[06:07] initiating new repositories is kind of cumbersome and I sometimes just like to prefer or I prefer building stuff in empty space uh instead of having to commit to an actual shape. Ghost courses would have slightly different constraints on them. Ghost courses would likely have to no I guess ghost courses could have real lessons. It's just the moment

[06:27] that they have a real lesson inside them then they become a real course and you're then required to put it in the file system I guess or I don't know. I'm not sure about that flow. Maybe we can work on that together. Notice how rough

[06:39] this is. This is just a super hashed out sort of idea that I'm kind of, you know, just spewing out to the LLM and making it do all the work. If you've not seen my Grill Me skill, then uh head to my I'll I'll send it in a link below. It's

[06:53] in my top five skills article, but you'll be able to see what it does here. It is really really cool. Okay, it's going to do an explore phase. I'm going

[06:59] to um head and get a glass of water. And by the way, if you don't know what explore is, um explore is it's basically invoking a sub agent. So it's essentially just passing a message to another agent to say explore this codebase. That agent then um explores it

[07:15] within its own context window and then it takes that context, it takes a sort of summary of that and it hands it back to the parent agent. So it allows you to get a lot of juice out of an explore phase because the explore can just go bam bam bam bam read tons and tons of files and then the parent agent only gets a summary of it. So, it's very token efficient. But anyway, I need a

[07:33] glass of water. Okay, grill me has come back with a let me challenge your framing of the current pain points. It says that looking at the code, delete lesson in the course write service already handles both ghost and real lessons directly. If it's real, it

[07:45] deletes the directory and re numbers. If it's ghosts, it just removes the DB row. So, you can delete a real lesson without converting to ghost first. Is there

[07:52] something in the UI that forces the convert to ghost then delete flow? Well, yeah, there is. Yeah, in the UI there's no option to delete the lesson immediately. And what I mean by deleting

[08:04] a real lesson is it would both delete the entry from the database and um purge the on disk representation. I'll ping this off while I explain something very cool that I've just recently started doing. I've been reading a book called um domain driven design. And in this

[08:21] book they talk about how important it is that you maintain a sense of a sort of glossery of all of the terms that you use to describe the system. This ubiquitous language can then be used basically to um bridge the gap between uh devs and domain experts the thing the people you're actually building it for. So I love this because this is exactly what the LLM has to have with me. I'm

[08:44] the domain expert and the LLM is the dev. And we need some kind of shared language so that we can talk together precisely. So for instance, here we have a concept of a ghost lesson. A lesson

[08:54] that exists on Whoopsie. A lesson that exists on the database. Where is it?

[08:59] Yeah. A lesson that exists on the database but not yet on the file system. And so whenever the LLM is searching for stuff about ghost lessons, it's going to come up come across this ubiquitous language file. Okay. Okay, so it's come

[09:10] back and it said, "Yeah, the UI currently only exposes convert to ghost for real lessons, not a direct delete entirely option." That's a straightforward UI gap. Okay, that's useful. Let's quickly talk about like

[09:19] the way it's using service here and um what this actually means in my codebase. I might actually try the new um by the way side question thing here. This is really useful when you just want to ask a quick question and you don't want it to kind of enter into the chat history.

[09:34] Describe what's going on with the course write service. Uh describe the shape of it. to describe its capabilities. Let's

[09:40] see what it comes back with here. The reason I'm uh asking about this and want to show you what it is is that um I'm really proud of the way that I've designed this repo. I mean, there's definitely stuff in there that definitely needs to be um looked at, but the way I've done the services I think is quite nice. The course right service

[10:00] is the main business logic layer for mutating course data, the right side of the system. It coordinates between the database, the file system, and the path numbering and renumbering logic. It's got a really clear interface here like you can add ghost lessons, you can materialize a ghost. So, convert a ghost

[10:15] lesson to a real lesson, uh, convert it to ghost again, uh, delete lesson, etc. So, this is a big big blob of functionality. And the tests for this course write service are all in one place. So, course write service.test.ts.

[10:29] Oh, no. Okay. Used to be there. Not

[10:31] anymore. Yeah, here they are. Course e2e.test.ts. ts and this actually

[10:35] creates a test database. It sets up a temporary git repo and so it tests all of the synchronization between this. This repo is using effect and effect makes it so so nice to create these kind of like units within your system that you can test really easily. Other

[10:50] languages have this as a first class thing but effect um sort of bolts that on on top of TypeScript in a really beautiful way. I've made a video about effects before on this channel, just one video. And uh suffice to say, I still love it and I use it for literally everything or at least every backend thing that I build is all in effect.

[11:08] Anyway, this huge service, the course write service, uh where is it? DB function service. Here it is. The course

[11:14] write service. It just lives in here. So, it's a file with essentially a bunch of methods inside here. And these

[11:20] methods like materialize ghost, like add ghost section, add ghost lesson, delete lesson, etc. This is what we're talking about when we talk about this service. So then I can exit out of this by the way thing by just pressing space enter or escape. And now I'm back here. So

[11:34] this is a great question. What flow do you actually want here? Are you saying you want to create a lesson action that immediately creates the directory on disk skipping the ghost step entirely?

[11:42] Or is the pain more that the two-step process create ghost and then materialize feels like unnecessary ceremony when you already know you want a real lesson? Yes, exactly. The two-step process feels unnecessary and it says okay. So, you want a single

[11:53] create lesson action that creates both the DB entity and the on disk directory in one shot when you already know that it's going to be real. Yep. Okay. And

[12:00] now it's gone to the bigger topic. Ghost courses. Yeah. Here we go. Then you said

[12:04] something interesting and immediately hedged on it. Ghost courses could have real lessons and when they do, they become a real course and you're required to put it in the file system. Let me break this apart. First question. A

[12:12] ghost course has no file path. So, it has no git repo. Sections and lessons inside it will all be ghost by necessity. There's nowhere to put them

[12:19] on disk. when you say a ghost course could have real lessons, what does real mean without a file system? Right? So,

[12:24] here what it's doing is it's fleshing out my kind of woolly language a little bit and forcing me to be a bit more specific. This is an easy question uh for me to answer. I don't want them to have some kind of intermediate status like flesh more fleshed out than a ghost. What a great phrase. But yeah, A

[12:39] is pretty obviously the thing here. Adding a real lesson to a ghost course is the trigger that forces you to assign a file path and materialize the course. Now, I'm already thinking from a UI point of view, what's going to be the easier thing to do? Or rather, the most

[12:51] obvious thing for the user, the cleanest UI either when we create a like real lesson inside a ghost course, we basically say, "No, you can't do that. You need to choose a thing in disk first and then you need to click away." Or we create a kind of integrated flow where you say, "Okay, you're um writing this to disk. When you do that for the first

[13:13] time inside a ghost course, you need to choose a place that it's going to live. I think I'm like veering towards the second because it's not that complicated to do that in terms of UI and uh I think it'll be a nicer flow. So, let's say that to it. Yeah, we're going to choose

[13:28] a here. Um and I think it makes sense that when you press um convert to or convert reveal in file system or or whatever the button is whenever you make it and material notice here this is where the ubiquitous language comes in really handy because I was just sort of fluffing around there. But what I mean is that when I materialize a ghost lesson when you materialize a ghost lesson you should have a modal popup that forces you to materialize the course as well. Look how clean, like how

[14:01] much cleaner that language is because I've got a concept of materializing and the word agreed on between me and the LLM. Anyway, let's fire this off and see what happens. Right. Yeah, we've got a

[14:10] concept of um versions inside the application. So, course versions. This is really important for me because I have a team of people who actually apply the course to the CMS. And so, I have a

[14:21] course and a change log. For instance, here in my Claude Code cohort, I've got several versions here. And like the sooner I approach the cohort, the more I'm sort of fixing bugs or like um switching out videos, that kind of thing. The latest version is always the

[14:35] draft version. And then I can like publish that draft version and add a commit message to it and it goes into the change log. Here you go. This is the

[14:42] UI for publishing the new version. And here's a preview of the change log. So yeah, I'm pretty sure that the schema that we rely on needs the ghost course to still have versions. Yeah, I'm fairly

[14:52] sure that the schema that we need um will require us to have versions because versions are needed in order to have sections and lessons and stuff inside them. However, it makes zero sense to be able to publish a ghost version. So, we should just hide the bits of UI that um and the actions in the menu that allow you to publish. So, let's fire this off.

[15:14] I can see in my video editor that we're about like 15 minutes in. And just notice like how long we're spending here on fleshing out these ideas. The more we do here, the less we're going to end up needing to do um when we actually guide the LLM. Okay, let me push on the file

[15:28] assignment moment. When you materialize a ghost course cuz you're materializing a lesson inside of it, you need to give it a file path. Either the repo already exists or the repo doesn't exist yet.

[15:37] When you assign a file path to a ghost course, should the app handle repo creation for you? No, it shouldn't handle repo creation. It's just pointing at an existing directory. That's an easy

[15:46] one to figure out there. Okay, this is such a lovely smart question that it's given us here. It's laying out what you're asking for. Direct delete for

[15:54] real lessons, direct create for real lessons, ghost courses, and then materializing a lesson in ghost courses. Question, does direct create apply inside ghost courses, too? That's so freaking smart. That's such a nice

[16:08] question. I can imagine my old boss Willow Reagan uh asking that question who is the guy I learned a lot of this lead developer stuff from. He had this incredible ability to just basically sit in a meeting and ask smart questions for hours and hours and hours. And this is

[16:23] exactly what the AI is doing here. It's asking really smart questions at the right point in the process. So if you're inside a ghost course and you hit create lesson, should that immediately trigger the assign file path model and create it on disk. Now again, there's a trade-off

[16:36] here. And instead of me thinking about this in my own head, which is not particularly fun viewing, why don't we model what it might look like if I sort of work this through with the LLM? Can you give me the trade-offs of both of these approaches? Okay, so it's saying

[16:49] on option A, create lesson inside a ghost course always creates a go ghost lesson. Keeps the ghost course as a pure planning space. The assigned far path moment only happens when you explicitly choose to materialize, which a clear deliberate action. There's downside. If

[17:01] you've already decided this course is real and you're just adding lessons, you're back to the twostep annoyance you're trying to fix. Option B, create lesson insider ghost course triggers the materialization cascade. Yeah, it's saying option A is the obvious choice given your stated goal. The two-step

[17:13] annoyance you described is specifically about real courses where the file system exists and you want a real lesson. Yeah, I probably agree with it. If we want a consistent UI, then we do want the ability to both create real lessons and create ghost lessons uh at whatever stage the course is at, whether it's real or ghost. That will mean a bit less

[17:30] work in the front end because we don't want to or won't need to conditionally show things blah blah blah blah blah. Yes, this makes sense to me. Option A sounds good. I think it mostly makes

[17:39] sense in the context of having two buttons, one to create a real lesson and one to create a ghost lesson. Could you just talk me through the UI a little bit and how this is going to look? Notice that I'm driving this a little bit more now. That's okay, too. The grill me

[17:53] skill is nice and flexible so that you can drive sometimes and the AI can drive. This is nice too is actually checking the current UI for lesson creation first. This is part of the skill is I get it to instead of asking me questions about everything if it's a question that can only be answered by or can be answered by looking at the code, it should look at the code first. I do

[18:11] wish that explore was faster. Explore is the thing that's like you need it in every single session, sometimes multiple times a session. And I just wish it was quicker. Okay, so here's how the current

[18:20] UI works. You right click a section header, you add a lesson. Right click an existing lesson, add lesson before, add lesson after. Also creates a ghost.

[18:28] Inside a real course, you rightclick a section, you'd see add ghost lesson and add lesson. Inside a ghost course, right click section, you'd only see add ghost lesson. Yeah, right. That's the

[18:37] question. Inside a ghost course, do you want the create real lesson button to exist at all? Now, at this point, I don't know. Like, I'm imagining this UI

[18:45] is going to get pretty crowded with this like cuz you're going to have multiple buttons there. You're going to have like add a lesson before this one and then do you make it ghost or real? I guess like oh man, this is actually quite gnarly.

[18:59] I'm thinking do I actually want a prototype of this so I can sort of see how it looks? Because there's multiple ways that we could fiddle with this and and get it like um nice. You could have it where you add a lesson then it opens a modal and you choose whether um it's a ghost lesson or a real lesson. I think

[19:15] probably what I'm going to do is I'm just going to build it one way and then maybe offer feedback afterwards. So let's say yes inside a ghost course let's have the create real lesson button. You know I could like stop this whole grilling session. I could go into

[19:29] prototyping mode here where I just sort of prototype you know three different versions five different versions of this just to see what the UI would look like. But I'm quite keen to get into implementation now. Okay. So create real

[19:39] lesson inside a ghost course triggers the full cascade. Modal asks for file path course becomes real. section materializes. Lesson gets created on on

[19:46] disk all in one flow. That's right. That model is doing a lot of work. Correct.

[19:50] It needs to grab the lesson title and the course file path. Yeah, that's it. Correct. That's it. We just need the

[19:56] lesson title and the course file path. That's it. I can feel it. We're getting

[19:59] to the end of this grilling session. Oh, maybe not. It's asking about section behavior. Sections inside ghost courses.

[20:06] And the state of a section is basically just derived from um the lesson. If there are any ghost lessons inside a section, then it's going to be a ghost. Oh, sorry. If there are any real lessons

[20:17] inside a section, then it's a real section on disk. A section basically looks like this. It's just essentially a directory on disk. You can rename it and

[20:25] rename the directory or you can add things to it, but that's basically it. Section logic should obey the current rules that we already have. There's nothing really new about sections. For

[20:34] instance, when we're inside a ghost course and we create a real lesson inside that section, then we basically flow all the way up. So, it becomes a real section, becomes a real lesson, and becomes a real course. Here we go. Let's

[20:48] keep going. Let me switch to the database schema. Right now, courses table has a file path as a required text field. For ghost courses, this would

[20:55] need to be nullable. That is the only schema change I'm envisioning. Yeah, just going to say yes to this. It's

[21:00] going to grill me on a tricky edge case. I see you have a real course with a file path. It has some real lessons and some ghost lessons. You delete all the real

[21:07] lessons or convert them all to ghost. Does the real course become a ghost course? Again, this is like a classic Willow Reagan question. It's fantastic.

[21:15] Really, really good. No, the real course does not become a ghost course. Once a course has a file path, it stays real forever because the thing that's on disc is not going anywhere. Yeah, I was

[21:25] thinking about that before and so I'm super glad that it answered it because now it's in the context and it's spelled out. Another edge case. You have a ghost course. You materialize a lesson, assign

[21:32] a file path, everything becomes real. Now the course has a file path but no real lessons. I feel like we just answered that, right? That's a weird

[21:38] one. I mean, I don't think Willow Reagan would ask that question. Yeah. Let me

[21:41] move to the deletion side. You want a direct delete action for real lessons in the UI? Currently, the context menu for real lessons shows convert to ghost, but no delete. Yeah, this is a UI thing.

[21:50] Should real lessons have both options, convert to ghost and delete? I think we need both. Okay, we're getting there.

[21:58] We're getting there. I think I've covered the main branches. Let me lay out the full scope as I understand it and you tell me if I'm missing anything.

[22:04] Courses file path becomes nullable. Ghost course creation a new course creation flow that only asks for a name. No file path. Correct. Ghost course UI

[22:12] hide the publish and export actions. Correct. Create a real lesson button available in both real and ghost courses. In a real course creates on

[22:19] disk immediately. In a ghost course triggers modal asking for the file path first then cascades materialization. That looks good. Create ghost lesson

[22:26] works as today. Available everywhere. Delete action for real lessons. purges

[22:29] from the disk and the database in one step. Yes. Delete action for ghost lessons already unchanged. And finally,

[22:35] con convert to ghost stays for real lessons that you want to keep planning but remove from the disc. Exactly. So, we've got that. This was essentially the

[22:43] eight bullet points that we just spent 22 minutes of video just uh trying to get. This to me feels really really familiar. This is how I'm working with AI a lot. I, you know, block out half an

[22:55] hour in my calendar to work out exactly the feature I want. And from here, it's pretty much all on Rails. Like, we have done the hard bit. Now, we have done the

[23:03] human in the loop bit. What I do next is I now uh I've been trying this for a few days. I get it to update my ubiquitous language document to basically just uh keep it up to date with any of the ideas that I've got in here. For instance,

[23:16] we've got some new terminology now. We've got this idea of uh ghost courses, which is new. Let's see what edit it decided to make. In fact, I'm just going

[23:24] to accept it and review it afterwards. So, there we go. We can see it's updated its idea of ghost entities here. It's

[23:29] got ghost lessons, ghost sections, and ghost courses. The verb materialize is now properly in here. The act of transitioning a ghost entity to a real entity by creating its on disk representation. I like too that it has

[23:40] this create on disk and realize like the aliases to avoid. That's really cool. And it's even got a concept for the materialization cascade. the chain

[23:48] reaction when materializing a lesson inside a ghost course. Assigns file path to course materializes section that materializes lesson. I freaking love this because later on I can say, yeah, there's a bug inside the materialization cascade and it knows exactly what I'm talking about. So, let's commit this

[24:01] update to the ubiquitous language document. Look at this. Yeah, sometimes I am actually committing code myself.

[24:06] Okay, so it's gone back to the grilling. Yeah, it's now just sort of repeated the eight sections. The existing plan entity is a separate disconnected planning tool. Yeah, I did used to have a um

[24:15] separate planning area, but then I sort of used this ghost concept to integrate it into my actual uh courses thing. Uh I've got it inside the ubiquitous language inside here uh down here. A plan, a plan section, and a plan lesson there. But this is basically deprecated.

[24:31] I am going to remove this at some point. And so we can say plans are deprecated and ghost courses are the new way to do it. And in fact, I think I'm going to go ahead and say I'm satisfied. Let's and

[24:43] I'll invoke my next skill which is let's write a PRD. So if we think about the conversation that we've just had with the LLM, it's incredibly good foder for just turning this into a sort of more uh concise summary document of everything that we want to build. I freaking love question and answer because it colllocates the question with the answer. I know that sounds like such a

[25:05] sort of basic thing to say, but the way that these attention mechanisms work is that stuff that's close together tends to um like it sort of shows up as a hot spot for the LLM in terms of its attention mechanism just like it does for humans. And what this ends up meaning is that this is such a rich document for it to pour through. Now, it's doing another explore phase. We

[25:26] should probably do like a cursory check on our context window down here. We're currently only at like 40k tokens, which is pretty impressive given how long we've spent with the LM working on this stuff. A lot of folks have asked me why my grill me skill doesn't use the ask user question tool. Like we weren't

[25:42] actually sort of like using uh Claude's built-in mechanism for asking questions. And the reason for that is that I don't really like that UI first of all. And second, like if you have a choice between calling a tool and not calling a tool, then like not calling a tool is always going to be more token efficient because every time you call a tool, you need to wrap it in JSON. You need to do

[26:02] various things. Okie dokie. We can see here that okay, it's now sketching out the major modules before writing the PRD. I've talked before on this channel

[26:11] on how important I think um modules are and like understanding the modules in your codebase without necessarily needing to look inside them. Like the course write service that we looked at before that's a big testable module that I was very careful in designing and designing the interface for. And I think this is so important that I've baked it into my writer PRD skill. So it sketches

[26:35] out the modules and surfaces them to you. I don't necessarily need to look inside these modules. I just want to know how they're changing. For instance,

[26:42] here I can see something that's a bit dodgy, right? It wants it to make a new method on the course write service materialize course and lesson reuses the existing materialized ghost and section materializing logic internally. I'm thinking about whether it could just instead use the existing materialized ghost and pass it like an additional parameter, but I think that would be a little bit dodgy AP API wise. So, I

[27:04] think it is probably right. I think it should have a new method. Notice how I'm thinking about the interface more than I'm actually thinking about the implementation here. The implementation

[27:12] I don't really care about, but I want to make sure that this is testable and um you know that the rest of the um kind of repo and any future AI agents can understand what it's doing. And again, notice how easy these functions are to name because we've got this concept of the ubiquitous language. So module one is the ghost core schema DB operations that seems fine. The materialization

[27:32] cascade service that seems fine. It's just a new method on the course service. Here we've got two new API routes, which makes sense because we're doing direct real lesson creation, direct real lesson deletion. I could um put them into like

[27:46] other API routes, but because this is just an internal tool, I don't really care about what my API like looks like from the outside, then I don't really care about um how many API routes I have or what they look like. It's just an implementation detail. Now, it's talking about the ghost course UI. New add ghost

[28:03] course option in the sidebar. Yep, that seems fine. A materialization model, two lesson creation buttons in context menus, and a delete action. And then

[28:11] module six, the plans deprecation. Hey, I mean, I do want to deprecate the plans at some point, but I don't think I want to deprecate plans now. Certainly not as part of this PRD. And it's asking me a

[28:21] second question. Which modules do you want tests for? I want tests in the places that we already have test harnesses. So for the course, write

[28:29] service definitely. And if we have some stuff for direct deletion, I think that would be as part of the course right service too, right? So let's see what it says here. Now this is funny. It's

[28:39] saying there's no existing test harness for coarse right service. The tests in the repo are mostly for pure functions and reducers. That is rubbish. So I'm

[28:47] going to do a rafiki. I'm going to say look harder. And there we go. There they

[28:51] are. A whole suite of them split by concern. Okay. And it's satisfied. It

[28:55] has everything it's needed. It's now going to write the PD and submit it as a GitHub issue. This is what I do with my PRDs. This is what I do with all of my

[29:02] issues. I stick them in GitHub because then when we go to actually implement this with an AFK agent, the AFK agent is going to pull down all of the GitHub issues, choose the one it's going to work on, and then just work on that one. Now, a question becomes, am I going to review this PRD? And no, I'm not going

[29:19] to. LM are really, really good at summarizing things. And so, I know that this PRD will probably be a pretty good summarization of this conversation. So,

[29:27] I'm just going to accept it on faith. And I'm then going to say PRD to issues. So it's now time to break this PRD down into individual issues. The benefit of

[29:36] doing this is that this now the PRD is already in its context from having written it. And so we get to just break the issues down straight from there. These all have blocking relationships in. So it's blocked by nothing. This

[29:47] one's blocked by number one. This one's also blocked by nothing. That's cool.

[29:50] Now let's just see how many there are here. Six does feel about right, I think. And what I mean by that is this is going to get picked up by a Ralph loop. And so it's going to just sort of

[30:01] work through each of these tasks sequentially. And so I want to pick tasks that are not too big and not too small because if they're too small then we pay the cost of like having to kick up an entire agent just to do like number two here, hide the publish export UI on ghost courses. This uh is a tiny task and it can be melded in with something else. But maybe ghost course

[30:22] creation maybe. No, that seems like decently sized because it touches the UI, it touches the schema, touches the API. Two lessons creation buttons, create ghost lesson and create real lesson. This seems super small. And

[30:34] actually, I think it has broken them down a little bit too far. Except maybe the materialization cascade that needs to live in its own. So, I think maybe we just merge two and three together and I think we'll be happy. So, let's go down

[30:47] to the bottom. Let's say merge two and three together. Okay, now we got four slices. is the ghost course creation uh

[30:52] the UI stuff, the direct delete action and the materialization cascade. Good stuff. Let's go. Let's create the

[30:57] issues. Am I going to review these issues? Absolutely not. I understand. Uh

[31:01] like I've already sort of pre-reviewed them. It's just expanding out stuff that's in the PRD and then, you know, putting them in issues. This will be fine. I might just show you one of them

[31:10] just to sort of see what they look like. It links to the parent PRD. It says exactly what to build. It gives some

[31:16] acceptance criteria. Says what it's blocked by. And it also says the user stories that are addressed in the parent PRD. If the parent PRD is the kind of

[31:24] destination, then these things are the journey to get there. And notice the PRD just has a bunch of user stories, some implementation decisions, and uh testing decisions as well. All of this stuff essentially just comes from the skills that I've put together. And I found that

[31:38] they're good enough to keep the LLM on Rails. I really like adding in the testing decisions because it means that it's more likely to follow TDD and do some um kind of create some feedback loops as it's going, which is great. So, all right, we have now set everything up to u make our AFK agent to give it the best chance possible to produce good work. Now, I've been like cooking my

[32:00] setup for this a little bit over the last 24 hours, and I've sort of built like a mini library to um make it work better than I had it before. The provisional name for this is sand castle and we have like a docker file here. It's going to spin up a docker container. It's going to mount the u

[32:18] working directory inside this docker file and then it's going to any commits that are made then inside the docker file by claud which is going to run in there. It's then going to patch those out. So pull out those commits as patches and apply them to my local um repo. I found that this setup is just

[32:34] like super flexible. I have a Docker file and a prompt here and I can just run a Ralph loop again and again and again passing in a bunch of issues and passing in like the last x number of commits. But you can check out the repo to sort of see the um most up-to-date file on this. I'm going to run where is

[32:51] it? I think it's PNPM Ralph. So I'll run PNPM Ralph. This is going to now spin up

[32:56] my AFK agent with a max number of iterations of 100. What it should do is it will run out of uh GitHub issues because it's going to close the GitHub issues as it creates commits for them. But at this point, I can essentially just walk away because you know we can see it's like doing things in the terminal. It's saying looking at the

[33:12] issues directly to action for blah blah blah blah. But I can now have a cup of tea or I can go make a coffee or something or have my lunch or more likely I can just open up another terminal and enter another grilling session. So for folks who say this approach seems really really slow, what you need to understand is that it's slow because you're trying to extract ideas out of your human brain. And while this

[33:33] is happening, you've got AFK agents running in the background implementing your previous grilling sessions. This is why this is revolutionary because like once we've completed thinking through the idea, our work is kind of done until we actually QA the outputs. My friend Jamon on Twitter called this the day shift and the night shift where I'm doing the day shift. I'm like, you know,

[33:54] thinking of ideas. I'm grilling with the LM. I'm turning this into PRDs and turning those PRDs into issues. And then

[34:00] the LM takes the night shift. Claude goes and actually implements this stuff AFK. So, I'm going to take a little break. I might even go for a little walk

[34:07] and I'm going to just wait and check back in with this once it's done. Okay, we are back. It is like an hour and a half later. I, you know, went for a

[34:16] walk. I went and had a cup of tea with my parents. Uh, yeah, let's see what it's done. So we can see that the agent

[34:21] signaled completion after five iterations. So we essentially ran a cleared clawed code agent five times in the repo and it should have produced for us. Yeah, I think six commits here. I

[34:33] think those commits, one of them might be one that I just haven't pushed up yet. Yeah, we can see the entire like commit history here. It's been leaving really nice detailed commit messages for us. And it should be Yeah, I think this

[34:44] was the update that I pushed before or haven't pushed so far. So at this point in the process, I need to um kind of look back over these commits. I'm kind of tempting to look over the code, but I think I just want to review the implementation first. So I'm going to

[35:00] open up a new clawed session. And I haven't come up with a skill for this yet. So I'm just going to sort of free blast it. So I'm going to say, take the

[35:08] last five commits and create a QA plan for me. Save that QA plan in a GitHub issue. The QA plan should give me a step-by-step guide on how to test every single part of the new implementation.

[35:20] This is something I've been sort of playing around with adding into my skills because I think it does make sense almost in every single sort of uh userfacing change. And while it's doing this, I'm going to rebuild the application and rerun it locally so that we can see exactly what's happening with it. Okay, so it has created for us a QA plan. Beautiful. Now, I have to say

[35:38] there is nothing more boring than watching else or watching someone else do QA. So, what I'm going to do is just walk through this uh myself and I will come back to you if I have any issues. Okay, the first one actually came super early on, which is pressing this add course model. I can see now there's two

[35:53] tabs in here. I actually really hate this. Like I just want uh every time you add a new course, it should be a ghost course. And I don't really like the

[36:02] ghost course terminology appearing in the UI. So, what I'm going to do is exit out of this. And I've got a little feedback button here, which you can see if I just remove myself there. this

[36:10] feedback button I can just describe my feedback in detail and then it will create a GitHub issue for me which can then be picked up by the Ralph loop. So I'm going to say when I open the add course modal I want the only option to be to add a ghost course and I don't want the ghost course to appear in the UI. It should just look like we're creating a course and then it creates a ghost course. So I'll submit this and

[36:36] when I go to the GitHub issues, we can see that we've now got a new issue saying hide ghost course option in add course modal create ghost course silently. So I actually used haiku to generate me a title here and then we've got the route it was submitted from and then what I said in the feedback button. This is how I do QA. This information is

[36:54] enough for Ralph to do a really nice job here. So I'm actually going to start my Ralph loop as I'm going here. I'm going to go back to the QA plan and I'm just going to add a comment to this and I'm going to say Ralph loops should not work on this one. This is a human in the loop

[37:08] task only. Or in fact, I'm just going to rename that first one to AFK. In fact, I've got something in my prompt that says if there's a human in the loop like label on it or it looks like it's for humans, don't work on it. And so, let's

[37:19] go back in here. Let's run PNPM Ralph again. And it's going to actually work on that issue while we're QAing other stuff. So, I'll go back to doing a bit

[37:26] of QA and I'll see you in a second. Okay, a new thing is when I create a ghost course here and I say new fun course for instance, then when I press create ghost course, nothing appears to happen. But actually, as you can see in the top left, oh, first of all, we get this weird minified React error. So,

[37:42] I'll just copy and paste that for the feedback form later, it does actually create the course, but we don't go to the course and the modal doesn't close. So, let's add this back into feedback. When I create a ghost course, it doesn't direct me to the new page and it shows this error. There's also no loading

[37:58] state present on the button which looks confusing uh from the user's perspective. So let's submit that again. The agent that we kicked off to fix the previous bug has actually already finished. So let's just kick it off

[38:09] again and I'll keep QAing. This time I won't interrupt. I'll just kind of keep going through the issues and uh attempting to fix them with Ralph in the background. Okay, this one I did think

[38:17] was showing off here or worth showing off rather. When I see a new ghost section inside a ghost course and I right click here, this create ghost lesson and create real lesson doesn't seem right to me. I feel like when I go into like create ghost lesson here or create like I just want an add lesson kind of thing. We've already got a modal

[38:39] here. What we should do is just have a checkbox that says also create this on the file system. So this is something that came up in our early discussions about this feature that kind of like I couldn't get a sense for which way to go until I saw it in reality. So that's the

[38:54] way that some things go sometimes. We could have had an extra design phase or we could have had an extra prototype phase, but you know, I don't mind just jumping to code and fixing it there. So I will add some feedback for that, but I'll spare you hearing my dictation. All

[39:06] right, then. I've walked through the QA plan and I have created uh seven issues here over the last uh or six issues over the last 8 minutes. We can see that while I've been QAing, Ralph has been going in the background and is fixing the issues. Most of these issues are

[39:20] bugs, but some of them are features that we just didn't think about. So, for instance, when we're deleting real lessons, we want to add a confirmation model to make sure that it doesn't just, you know, like um we don't accidentally click it and it deletes or whatever. There were certainly some showstopper bugs here. For instance, if there's if

[39:34] it's not a git repo, uh then it gets into a super weird state. Yeah. If the course repo is not a git repository and anything about that fails, then we should walk back the creation of the directory inside it since the directory and file system and the database will then be out of sync. This is something

[39:48] again we didn't think about in the grill me session at the start. So, we're now having to find out about it in QA. It's this kind of stuff, this kind of stuff that makes me think that like the specs to code approach is just never going to work because when you're in there, when you're in the QA loop, when you're iterating towards something, you are going to find little weird edge cases like this that is really hard to plan for before. Anyway, rant over. The point

[40:10] here is that I've now done a extra QA step. Uh Ralph is now going to chew through these issues. I can probably actually close this QA plan and I might want to reopen it if I like um sort of want to redo it, let's say, but the behavior has slightly changed. So, I'm

[40:26] closing it to take it out of Ralph's or or rather the agent that I'm using's context. So, it doesn't look at this as like the the source of truth for what it's supposed to be building. Either way, I'm going to go do something else and then we'll see what happens to Ralph when it comes back. Okay, we're back and

[40:40] we've got iteration 8 which is very nearly complete. This looks like the final issue here where it's just adding the confirmation model with file details when deleting real lessons. We can see we're up to 14 commits that have been added kind of in this entire feature build as we've been going along. And the

[40:55] issues here are very nearly closed. You can see I last opened this one 30 minutes ago. So that's how long it's been running kind of. One thing I would

[41:03] like to add here is potentially parallelizing these Ralph loops and sort of having like a team of agents working on it at once. But to be honest, it's quite nice having these gaps because it means that I get to do some deep focus on something. For instance, like grilling me on something and then later I can come back and sort of come back to code and do a big QA session, send it off again, you know, you get the idea.

[41:25] Something that's crucial to the success of these Ralph loops is making sure it runs tests and types on every single commit. We can see that in most of these loops, it's adding tests, too. So, it's updating the reducer test to cover the new action. Now, it's committing and

[41:38] closing the issue. So, we should be nearly there. Okay. And we are good to

[41:41] go. I'm going to um rerun the build and let's do a little bit more QA. And I'll spare you the uh extra QA step here. But

[41:51] suffice to say, what I would do from this point on is I would go back here and I would continue QAing it, find more bugs, and at some point I would call this done and I would stop working on it. One thing that's great about having this really flexible backlog approach is that anytime I can just queue up a bunch of bug fixes and it will go in and fix them. Let's just check one thing which is we can see that the add lesson now it no longer says ghost lesson and real lesson and we can see here it's saying create on file system in a little checkbox. If I go fooar and I say create

[42:19] on file system then it's going to add the lesson and we should be able to see once that's done. It's quite slow that isn't it? I'm interested on why that's quite slow especially because this is all local. It should now be complete and

[42:32] it creates that foo bar as the second lesson. But there we go. We are by my count which is not entirely accurate.

[42:36] It'll be about 42 minutes into the video at this point. If you're here, thank you so much for watching all the way to the end. What I hope you take out of this video. I'm not sure to be honest. Like,

[42:47] this is so much looser than the videos I usually put together, which are usually fairly tight, focused on a specific goal. I hope that you're able to pick up some vibes from me in terms of how much detail and how in-depth I look at the stuff that I'm uh producing. You also notice how little I looked at the code really. Like what I'm doing here is I'm

[43:06] reviewing inputs and outputs. I'm interested in the code. Absolutely. I'm

[43:09] interested in how the interfaces are changing. I'm interested in how the modules what the modules are sort of looking like. And every so often I'll go and have a little poke around in the code just to make sure it's on the right track. But for me really what I'm doing

[43:19] is reviewing the outputs that come from AI, passing more information to it and getting into a tight loop with it. And crucially because I'm able to run the uh run claude AFK, I'm able to parallelize my own QA with the fixing of the bugs, you know, which is just amazing. I imagine though you have just dozens and dozens of questions. Um feel free to

[43:39] ping them into the comments below. Or if you want to learn this from the ground up instead of just diving through this messy video, then the cohort is the place. This one starts on March 30th, but if you're seeing this sometime in the future, then there'll probably be a a place you can sign up for the next one, too. This has been the last kind of

[43:53] two months of my life really full-time working on this. And I'm so proud of how it's come together because everything that you see here in this sort of big video has come from me thinking about this stuff deeply. And the cohort is the kind of perfect encapsulation, the easiest way to learn this from the ground up. Anyway, thank you so so much

[44:12] for watching. Thank you for getting to this point. and I will see you in the next
