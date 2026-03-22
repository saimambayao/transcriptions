# How I Use Obsidian + Claude Code to Run My Life

**Channel**: Greg Isenberg
**Duration**: 58:57
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=6MBq1paspVU
**Transcribed**: 2026-03-23 01:23

---

## Organized Notes

**Core Philosophy**

- The **quality of information** the agent has entirely determines what it can do for you
- Obsidian vault = the **single source of truth** about you, your projects, your thinking
- You focus on **maintaining the vault** (writing, reflecting); the agent pulls from it to act
- **Strict separation**: Vin doesn't let agents write into his vault — only he writes, agent reads
- The vault should have the **best representation of who you are** at all times

**The Problem Obsidian Solves**

- Without it: you re-explain context every session, agent doesn't know your history
- With it: pass **project files and context** instantly via commands
- **Obsidian vs plain folders**: Obsidian tracks **inter-relationships** between files via [[links]]
- **Obsidian CLI** gives Claude Code not just files, but **relationship data** between files
- This lets agents surface **latent patterns** across domains you wouldn't see yourself

**Vin's Custom Commands (the power moves)**

Daily operations:
- **`/context`** — load full context about life, work, current state (reads context files, daily notes, follows backlinks)
- **`/today`** — morning review pulling calendar, tasks, iMessages, past week of daily notes into a prioritized plan
- **`/close-day`** — end-of-day processing: extract action items, surface vault connections, check confidence markers

Thinking tools:
- **`/ghost`** — answers a question **the way you would** (builds voice profile from vault, writes in your voice, evaluates fidelity)
- **`/challenge`** — pressure tests current beliefs using vault history, finds **contradictions and counter-evidence**
- **`/emerge`** — surfaces ideas the vault **implies but never states** (conclusions from scattered premises, unnamed patterns)
- **`/drift`** — compares stated intentions against **actual behavior** over 30-60 days (surfaces what you're avoiding)
- **`/ideas`** — 30-day deep vault scan with **cross-domain pattern detection** (generates ideas for tools, films, products, projects)
- **`/trace`** — tracks how an idea has **evolved over time** across the vault
- **`/connect`** — takes two domains and connects them using the vault's link graph (e.g., "connect filmmaking and worldbuilding")
- **`/schedule`** — checks calendar but also reads daily notes and what you care about to give **contextual scheduling advice**

**Context Files Pattern**

- Vin creates **extensive context files** for each project (e.g., podcast working context, personal workflow context)
- These files contain: team members, recent hypotheses, daily schedules, how he likes to work
- Result: when agent pulls context, it has **deep understanding** not just surface-level info
- `/context` command reads all context files + daily notes + follows backlinks in one shot

**The Self-Improving Loop**

- More notes → more patterns → better agent output → better ideas → more notes
- The vault grows over time into an increasingly **accurate representation** of your thinking
- **Confidence markers** on ideas: rate how solid you feel about each hypothesis
- Agent can track how confidence evolves, which ideas you keep returning to

**OpenClaw Integration**

- OpenClaw can **autonomously** read the vault and make decisions on your behalf
- Instead of managing the agent directly, you **manage the vault** — the agent pulls from it
- If the agent makes wrong decisions, you change the vault, not the agent config

**Writing as the Core Habit**

- Writing = how you generate ideas, progress, and form original thinking
- Writing is also how you **delegate to agents** — more context files = more delegation capacity
- The vault is not just memory — it's a **thinking tool** that compounds over time

**Key Insight: Connecting Dots**

- Obsidian + Claude Code = **dot connecting machine**
- Like a therapist/coach — you do the reflecting, the tool guides and surfaces patterns
- Can reveal things about yourself you **don't know** — ideas you've been circling for years across different domains
- `/emerge` and `/connect` are the most powerful for this — surfacing the **unarticulated**

**Practical Tips**

- Can import **meeting transcripts** (Granola, Gemini notes) into vault folders
- Tag meetings back to projects for automatic relationship discovery
- Create **separate vaults** for different purposes if needed
- Commands take **longer** than normal prompts because they read many files — that's the tradeoff for depth
- All commands were created by **asking Claude Code** to make them — no manual coding

---

## Transcript

[00:00] This is Obsidian. And Obsidian is this little tool that people are using as their second brain. But what's really cool about it is they're pairing it with Claw Code and they're getting crazy results out of it. It's literally a

[00:14] gamecher. Now, I've been slow to adopt Obsidian cuz to me, it's been a little daunting to look at. So, I had my friend Vin and he clearly explains what Obsidian is, how to use it with Claude Code, how to set up these commands [music] that really drive the most out of Claude and all the LLMs. And it's an

[00:35] incredible episode, like a really gamechanging episode because I think that people who understand how to use Obsidian and how to use Claude Code together, they're going to be able to live happier, healthier, and wealthier lives. Why? because it gives incredible ideas to you on tap. So, I know that the

[00:55] people that stick around to the end of this episode, I think that for a lot of them, it's going to [music] absolutely change how they use AI and it's going to be a super impactful way because you're going to get better ideas at the right time, the right moment, and it's going to make you happier, healthier, and wealthier. Enjoy the episode. [music] >> [music] >> I've got my dear friend Vin, also known as Internet Vin, on the podcast. I

[01:26] literally begged him to come on. I [laughter] I begged him. I begged this man to come on and to teach us a very specific thing. Vin, by the end of this podcast

[01:39] episode, what are people going to learn? I want you to have an understanding of how you can use claude code and obsidian as a thinking partner. I want you to have an understanding of how you can stop uh having to explain things to agents over and over again and just pass specific files in. And I want you to

[01:57] understand how you can use Obsidian and Cloud Code to notice things about the way you think that you would not have noticed on your own without these tools. >> All right, from your lips to God's ears, [laughter] let's get into it. Okay. So, first is like what is cloud

[02:13] code? So, claude code is this like agent that you can use um in a command line interface. So, it's just basically this tool you can use that can control your computer and you can use it through natural language. Right? So, I can say

[02:29] make a file or make a file on my desktop that says hello Greg in plain text. Right. And it's going to go and do this.

[02:41] That's really cool. That's that's something that's that's new that wasn't possible before. Before this, I had to go to the desktop, open some text editor, and then like create that file, right? And now this file is on my

[02:53] desktop. So, I can say open the file. There we go. Hello, Greg. That's crazy,

[03:00] right? Um, now what's interesting about this is if you have this agent that can like control and do things on your computer, that means that whatever you can describe to it, like it can start to do. And so when you if you describe a project to it or you get into these long conversations uh with an agent, um, it can do more and more complex things. The more information it has, the

[03:24] more complex things it can do. But the problem is that if you have to let's say you know like I write some super long description about a particular project or I have like an hour conversation with this agent about a particular project it's like I don't want to have to create a new session to explain that all I don't want to have to explain that over and over and over again. Um, a lot of people are using like claude uh or chatbt on the web and it has things like memory but you you can't like control you don't know what's in that memory right you don't know what it knows and what it doesn't know and so there needs to be some way of like you know passing information into these agents that is easier and faster and the better information you can give it and the faster the information you can give it the more stuff if it can do for you and the better the faster you can delegate to it. Okay. So now even if I let's say

[04:16] let's say I had like you know let's say I wrote like a big project description here, right? create a file that describes, you know, a project um about a to-do list app that um is very minimally designed and reads from uh all of my calendar and my messages and um my Slack and Slack and interprets it into a task list that of tasks that it thinks that I should do. I don't know some some idea, right? So now this this is a file that

[05:01] could be on my desktop and what I can do when I use cloud code is I can reference that file and pass it in whenever I want. >> And why that's important is because >> it's the context, right? >> Yes.

[05:14] >> The whole game is >> feeding the beast good context. Yes, exactly. And I don't want to have to do this over and over again. And and and

[05:25] when I work on this uh over days, I I'm not going to remember like what we talked about, right? So, I want some kind of file uh that I can like pass in. Oh, sorry, Greg. One sec.

[05:36] >> Yeah. And that's that's sort of the problem that a lot of people are facing with cloud code is like they're using it and then they're saying, well, it's it's okay. It's not like gamechanging. Mhm.

[05:46] >> And the issue is they don't have they're not they're not feeding the right context at the right time. >> Yes, exactly. And so here's so here's like a a project description that it wrote and obviously I can pass this in and this is like a this is like a general one that I just created but you you can make these like very complex you can build them into like robust files right over time. So we know that uh

[06:09] cloud code can create files and it can repeat and it can um uh read files right so now I can say let's say I created a new session so here's a new session and now I can say like I want to work on this project and I go here and it's going to be um to-do app here it is boom now I didn't need to explain the file again I need I didn't need to explain the project again right so it's going to read this file and it's going to start like you know That saved me a lot of time. Great project. Before diving in, a few questions to scope the first session. So that'll continue. So now

[06:42] what is Obsidian? Right. Obsidian is this tool that it's kind of like an interface that sits on top of um uh a collection of markdown files, right? So

[06:56] here like this is reading a markdown file. How I use Obsidian story development, right? Um I have uh daily notes. This is my daily notes. This is a

[07:07] This is also um a markdown file. I should do my own fundamental analysis into thing into how things stay pure when they grow and become more mainstream. Right. This is just a file

[07:17] that I have. I have um you know like a file on Greg Eisenberg that I haven't put in. >> Oh, that's weird. That's weird.

[07:25] >> Yeah, >> that's pretty weird. >> And so I I make files like notes of things that I'm learning from people and stuff like that, too. So I have different um files for everything, right? And the interesting thing that

[07:37] makes a vault, which is Obsidian, what Obsidian interacts with, this whole thing is called a vault. What makes it different than a folder is that Obsidian is not only interacting with just like a you know a folder of files. Um but what it does is it also allows you to make inter uh to connect relationships between files. So I can say today I am

[08:00] on um a podcast with Greg Eisenberg. Now this file is linked to that Greg Eisenberg file. Super interesting. Super

[08:10] interesting. And so when people like like like people uh there's a lot of people who really really like using Obsidian and tools like Obsidian because of this ability to form inter relationships. This is unique to just having a folder. a folder on your

[08:25] computer cannot show these inter relationships. And so it gets really interesting when you start to um keep making these like interreationships over time, right? And so what happens here's a little visualization. And so in the here, these

[08:42] are each one of these circles is a file and and and it's it's showing how it's like connected to all of these other files where I've written things about. So here's like personal agent infrastructure, right? And so I could look, you know, and I guess I should also add just kind of a comment on this and what was difficult about doing this demo, there's like so much personal information in here because this is like my personal thing. So I don't even know like what's

[09:08] going to show up on the screen here, right? Um, but that's part of doing demos like this, which is which are kind of weird and interesting. But you can see personal agent infrastructure. It

[09:17] links to like Aentic AI. There's like a link here to Telegram. There's a link here to like Toby, the founder of Shopify. There's a link

[09:25] to like Presence Log, Claudebot, you know, and then here's like I I have a podcast too called the other stuff. And like you'd see I'm obviously doing a lot of like thinking about that a lot, right? And so I can also, let's say if I go to Greg Eisenberg and I go to local graph. So, here's like all the times

[09:46] I've written about Greg Eisenberg, right? Notes on time constraints, how I use Obsidian, which is just kind of interesting. Um, so if I'm listening to >> I love you, too, Vin. I love you, too.

[09:57] >> If I'm listening to a show and I'm picking up different patterns, I can I can reference that back to to Greg. So, that's really interesting. But here's the thing. The reason why people love

[10:07] Obsidian is because of these interreationships. the idea that you could open a file and then you know I just open this file and then I'm like oh interesting I mentioned Greg Eisenberg I can click that and it goes to that file that's interesting right it shows it works more to uh it works more like the way your brain works your brain connects these patterns all the time >> here question yeah >> so I see why it's interesting >> but how does this get me better output >> exactly yeah so the next thing is obsidian in released this new tool called Obsidian CLI. And what that allows you to do is it allows you to use Cloud Code and it can go and it can read all of the files in your Obsidian Vault, which is a folder of text files.

[10:56] But with the Obsidian CLI, it can give Claude code not only those files that it can read and access, but it can also give Claude code information about the inter relationships of those files. So you can see so cloud code can see that oh this file is connected to this file and this file and this file and that gets very interesting in terms of what claude code can understand about you and what claude code can uh understand about uh all of the relationships between the things that you're working on. It can start to surface patterns about what you're thinking about that you are not seeing for yourself. some idea that you

[11:34] might have been writing about for a year in this vault. It could be a latent idea and it can just immediately say like, hey, did you know that you've been writing about this same pattern in startups or in this particular project you're working on in every single note you're making across these different domains and and in seeing that for the first time can be like a huge light bulb effect. It can cause like huge progressions in your learning and your understanding and your point of view on the world but also in what you're working on. Um, so I've written out I

[12:04] wanted to demonstrate how that actually works in terms of how I can pass information into an agent that would be impossible without Obsidian and Cloud Code. So here's some commands that I have that I use. And I don't want you to be afraid of like all this stuff. I know this can

[12:19] look intense, but um here here's what um here's what I've got some commands. And this is just terminal that I've created and I'm running it in Obsidian. You don't need to use this. You can just

[12:31] also do this in your own terminal session on in whatever tool you want. But I put it in obsidian because I want to see it all together and I wanted to show you the ways in which you can like integrate and customize this environment. So here's a cool thing. So

[12:46] context/context load full context about my life, work, and current state. Reads context files, daily notes, and follows back links to build a complete picture. So I'll just show you that right here. So, like let's

[12:58] say I open a new session in in uh in Claude just on my desktop. And now it's like I'm about to work on something, but before I work on it, I can just type context demo. Now, it's going to read a whole bunch of files about where I'm currently at. Done.

[13:15] Like, I've already preloaded I've already preloaded in all this context now. So, you can see it's going to start reading all these files. It's reading a read me. It's reading context about new,

[13:24] which is a media company that I'm working on. It's reading about other stuff. It's reading my personal the other stuff is my show. It's reading a

[13:30] personal workflow context. And so I don't have to worry about it not knowing the key information that I wanted to know. I just did that one command and now it's going to get all that information done. So I can use slash

[13:42] today, which is a morning review. It pulls calendar, tasks, IME messages, and the past week of daily notes in into a prioritized plan for the day. Why does this matter? Well, okay, sure. You can

[13:53] set up an agent and give it access to your calendar and your tasks and iMes and things like that, but it's miss it's that's that doesn't have all of the information about what you're thinking about and why. If I'm writing daily notes about some particular technology or project or thing that I'm interested in, does my calendar reflect actively like does it match the subjects I'm actually writing about? If an agent has that context, you can it can it can uh more effectively give you um information about what you should do or not do or and it can more effectively make decisions on what should be in your calendar or not in your calendar. Here's

[14:28] another one. Slashclose day [clears throat] end of day processing extracts action items, surfaces vault connections, checks confidence markers, needs to be updating. So I have a bunch of hypotheses that I I think about and I give them a confidence rating. This is

[14:43] an idea I'm working on. I feel very solid about it. Here's another idea I'm working on. I'm not sure about it. So,

[14:48] these are like um daily operations things, but [clears throat] this is what I use Obsidian for the most, which is thinking tools. I really, really, really like working with LLMs as a thinking partner. It's my favorite way of using LLM. I know people like to use

[15:07] uh agents and LLMs to build things, but I really like using them to think alongside me and build when I feel like, you know, I really have a novel way of viewing things. So, let's see here. Um, so ghost here's here's a command I have.

[15:25] It answers a question the way I would. It builds a voice profile from the vault, writes in that voice, then evaluates the fidelity. So, I can just say, "What do I think of AI?" And I'm

[15:35] going to show you this challenge topic. It pressure tests current beliefs using the vault's own history, finds contradictions, counter evidence, and shifts in thinking. Why does that matter? Well, if I want to make sure

[15:47] that I'm continually developing as a human being and as a as a as in my skills, I want to make sure that, you know, the POV I have isn't overly biased or limited. So, this can challenge me. Emerge surface ideas the vault implies but never states. conclusions from

[16:05] scattered premises, unnamed patterns, unarticulated directions. This is super super useful because a lot of times, you know, I I can be stuck just surfacing ideas in a in in um in a lot of different ways, like for years, and just having someone say a simple thing to me that just says, "Hey, this is just naming the idea. Hey, did you know that you keep circling around this pattern?"

[16:28] Huge breakthroughs. Uh slashdrift. It compares it compares my stated attention intentions against actual behavior over 30 to 60 days.

[16:39] Surfaces what I am avoiding ideas. People on this podcast, the listeners will probably like this one. Deep 30-day vault scan with cross-domain pattern techni detection and graph analysis to gen generate ideas across all domains.

[16:52] This gives me um not just ideas on like things I should work on. like it gives me ideas for tools and things like this, but it also gives me ideas on like films I should watch, products I should buy. Again, all influenced by like like things I'm writing about in my vault.

[17:08] Um, trace tracks how an idea has evolved over time across the vault. So, let's see some of this stuff. The trace demo.

[17:17] So, I did this one already. And the way this would work is I just like create a tab here and I could just be like claude trace and I had to create demo versions of all of these um commands because of how much personal information is in my vault. But still I don't even know like I I I can't even control what is going to show up on the screen. And I I have

[17:39] just a dumb question. Like all those commands that >> we saw, >> is that commands that you created or is that what Obsidian created? >> That those are commands that I created.

[17:50] >> Mhm. >> And um you can create them very easily by just asking Cloud Code to create a specific command. >> Mhm. Um,

[17:58] >> we can include I'll include in the show notes and in the description just like a link where people can click to get access to some of Vin's uh skills if that's if that's >> Yeah, for sure. Totally. Yeah.

[18:14] >> So, you can see here what I did was I just typed slashtrace demo. Demo is just because I'm showing this publicly how I use Obsidian. And so what this does is it tracks my I u the way I've developed and um the way I've navigated this idea through my vault. So I have an example

[18:31] here. It's really interesting. So here I I did it and I and I and I let it run. And what it's doing is as it

[18:39] says like I'll trace how your relationship with obsidian has evolved. Let me start by building a vocabulary map and searching across a vault. So it when you have OB like so now it starts going through the vault reading all of these different files and it can see all of the files that are connected using the Obsidian CLI. This is a lot man.

[18:58] This is this is something that I would never be able to do on my own and to read all of these files to know what how they're interconnected with each other. This is just not possible for me to do as a human being. And then it spits this out. I now have everything I need to

[19:12] construct this trace. Here's the full evolution trace how I use Obsidian. First appeared January 11th, 2025. Time

[19:20] span 13 months. That's in relation to this vault specifically, meaning all the files in here. It says prevaults December 2024. The

[19:30] essay how I take notes in the west end of Toronto dated December 1st, 2024 describes a complete system where Obsidian plays no role at all. The system is audio dumps via Mac Whisper, LLM dialogue loops, Canopia for spatial mapping, physical notebooks for cognitive friction, Fuseland for tracking, arena for fragments. The pipeline is capture process crystallization. This is the baseline.

[19:51] Obsidian is not in the picture. Discovery and skepticism, January to May 2025. The first daily note in the vault, raw excitement mixed with uncertainty. I

[20:02] could probably drop transcriptions in here, too, as a way of storing them. The current theory is that in terms of note-taking birectional linking is not that useful but I don't know then it says the chosen tool um originally I was back link it says um here how I use obsidian note a pivotal realization about backlinking originally I was backlinking to general terms podcast or physical fitness or film making I'm realizing it's not the most useful way to use obsidian the most important thing to do is to create notes for each of my patterns theories, projects or perspectives and get them documented and out of my head and then link to those notes. So, it's just it's just like pulling from things I've written and it's forming this historical this history of this concept. And I

[20:51] could do this with anything. I can do this with like startups. I can do this with a particular project, with foods, my relationships, like a hobby, anything, right? And then phase four,

[21:02] January 2026, a month of explosive building, everything still require and then like everything still requires me to actively prompt and manage each section session. The next unlocked is figuring out how to get agents task to run automatically. The friction is no longer with obsidian itself, but with the boundary between the vault and agent execution. So you

[21:21] can see I'm really pushing myself, right? And it's cool. This is this is a very useful thing for me to understand how my um use of this tool is evolving.

[21:35] And it's just I think it's just absurd that I can just be making notes and then about all of these different things through my life. Like even as a parent I I can I can like reflect on the different things I'm learning. I just think this is insane that an a computer can have this much information about me and surface these patterns. I would not

[21:56] be able to do this on my own and this fast. And what a great tool it is for me like like I can just like now write in here and I'm you know as I'm thinking about things and it gives me ideas right about um my life and the projects that I'm working on. So I can say you know it's interesting the way that my relationship with Obsidian has evolved over time.

[22:23] It makes me think a lot about the way in which my relationship with computers has evolved over time since I was a kid to now. It's interesting how these things just happen and compound over time and we don't really realize it. So, it's just like a note, right? It's an idea. So that's an

[22:50] example of something. >> So I think a part of getting good at Obsidian sounds like refle, you know, inserting reflection into your everyday life because a lot of people, >> you know, we're moving from meeting to meeting. We're busy. We're parents. Um,

[23:09] you know, we grow up and we of course write things down in notebooks and stuff like that, but I feel like as we get older, we actually write and reflect less and less. >> Yes. >> Uh, you know, h how do you how have you been able to insert reflection into into your life?

[23:29] >> Yeah. I think um for me it's really about there's there's two reasons that I think reflection is interesting and making notes a lot are is interesting. One is that it's great to be able to look back on them. Like for me now,

[23:43] obviously I can use an agent, but to for me to go back and see these notes and realizing that, oh, like I'm a person that's continually changing. My skill is continually changing. Projects are continually evolving, it's it's just it's an amazing part of life to be able to reflect on how things are changing over time and how you are changing over time and how the world is changing over time. But the other thing is that

[24:04] there's like a functional reason too. The reason I like to make notes a lot is because that's how I generate ideas. When I like get when I sit down on my computer and I write things down, that's where ideas come. For example, this

[24:15] thing I just wrote here, it's just a quick note. I'm just doing it in real time. I'm just making it up right now.

[24:20] But um by writing it out, I feel like I internalize it more. And I like having good ideas. I like progressing. So

[24:28] because I like having good ideas and I like progressing, writing is how I do that. And so I think um to you know if you want to cultivate like a writing as a habit I think first you have to uh connect it with the idea that this is how you progress and this is how you generate ideas and this is how you uh have form original ways of thinking. Um the other thing I'll say is that writing right now is a big way of how you delegate things to agents. That's like a

[24:58] whole new that's a whole new aspect of it. So if you can develop a writing habit, you have a lot more context that you can pass over to an agent which then um dramatically I think increases the amount of like things you can delegate and the amount of things you can build. I hope that was a good answer.

[25:16] >> How does how [snorts] does this relate to open claw? Because if you think of open claw, it's essentially, you know, at the best case an extension of you. Yeah, >> that could go and do things you know uh independently slashbased on your guidance. So how can

[25:39] you use commands obsidian [clears throat] and open claw and reflection harmoniously? >> Yeah. So I think if you look at like here's an example of one command that I do. It's just like a schedule command.

[25:54] Um, and so what I asked this thing to do is I said schedule I said can I take a meeting with Greg Eisenberg today at at Feb 20 at 2 p.m. Right? And what this

[26:05] does is of course it can look at my calendar and stuff like that but it's also going to look through my daily notes. It's going to look through what I care about and then it's going to give me some perspective. So it says your day is stacked. You're already recording on

[26:19] Greg's podcast this morning followed by a team lunch outing and meeting with Peter and Vince. Your Feb 17 note show the Greg episode has been top of mind. The vault has a dedicated Greg Eisenberg note. No, not a two. So the

[26:30] recommendation is no, not a 2pm, but you might not need a separate meeting at all. Yeah, that's val that's actually the correct answer. How does that relate to OpenClaw? Well, OpenClaw is this like

[26:41] autonomous agent that can go and do things if you uh set it up to do that. Like it can do things without you having to prompt it all the time. it can just go and make decisions and build things for you um on your own. So now what

[26:55] OpenClaw can do is in the same way I just did this command, OpenClaw can do this on its own as well. And it can go and read my vault, find connections and then make decisions uh on behalf of me with like a deeper understanding of me. And now instead of like managing an agent or talking to another human about working on something, I just focus on managing this vault. This is like the

[27:16] new source. I just continually try and make it so that this vault has all of the information needed so that I can delegate to an agent and um the agent can just pull from this vault source and make decisions. And if it's not making the right decisions, I'm changing something on the vault, I'm not necessarily working with the agent specifically.

[27:35] >> Um kind of kind of um that's my speculation on that subject. I think it's very interesting. Yeah, I think uh one thing that worries me a little bit about it is if Obsidian [clears throat] is really your second brain, >> giving openclaw access to your second brain >> is scary.

[27:57] >> Yeah, scary. And I would say that is the um fundamental um the the weird element of this technology I would say and I have purposely given um Obsidian I mean sorry a claude code or any agent access to a lot of information. I've purposely done that because my um relationship with this is I want to understand what these things are and I want to understand what they're revealing about, you know, how our relationship with computers is changing. But um it's weird. It's like

[28:34] you have to really think about how much information you're sharing with these agents and whether that's the right decision or not the right decision. And I think um it's going to be very interesting to see how privacy as a concept evolves and changes and what we fight for or don't fight for in like the in the future of our society and our world. Even with every one of these commands, I had to create a new version of them, a demo version, so that I wouldn't reveal too much personal information while I'm on screen on this podcast. And even then, it's like a it's

[29:08] a tossup. You know, I could type the demo version, but who knows what's going to be shown on screen, you know? What other commands do you want to show?

[29:17] >> Um, so there's connect which is allow it allows me to take two domains and connect um them using the vaults link graph. So I can just say I did one here and I just asked it to uh connect film making and world building. And so it goes through and it reads all of these different files and then it can start to say okay let's let's connect these two concepts. So notes in film

[29:49] making uh notes in filmmak's neighborhood. So I was like 35 film watch list my first meeting with Toby notes in the world building neighborhood um the worldbuing essay um new as a media company. So these are different things I'm thinking about. So bridge one

[30:08] the interview portal and the constructed world in film making if I notice something specific and asked a question about it it would open a portal into a person's internal world which is often a vast universe of concepts and beliefs and visions. So worldbuilding essay I want my blog to show you what I value what I believe what I worry about like a tomb from ancient Egypt. I want my blog to be a place that you dig up and examine long after I'm gone. These are

[30:33] things that I've written and I can start to see how these ideas connect together. Bridge to always on documentary equals continuous world building. Always on documentary is a creative strategy where companies continuously narrativize their characters, pursuits, conflicts, and visions through documentary. So these are like things

[30:50] that I'm writing about and it's showing me the ways in which these are connected. Um, I think this can get very interesting depending on the kinds of things that you're willing to connect together. You could get probably pretty crazy with it as well, depending on what you're writing about in your vault. I

[31:06] could connect like shawarma and startups if I wanted to, for example, and see the kind of connections that are coming between these things. Um, again, really interesting because all of this is happening super quickly and I don't need to explain any of this to an LLM. I can just type something like slashconnect filmm worldbuilding.

[31:26] >> The the a lot of the examples you're using is personal reflection. Yes. Yes.

[31:31] >> How do you think about uh you know for example note-taking in meetings like maybe you have like a granola or Gemini notes taking you know uh taking notes or and and and sort of putting it into Obsidian or um and by the way when I say notes those could be meetings that you're not even in. They could just be like, >> you know, Tommy met with Vince and they had this meeting and I want to put it in here. >> Yes.

[32:03] >> Um, how do you think about that? >> So, it's a really good question. So, I think you can use these vaults however you want to use them in terms of like um you could put any text you want in here.

[32:13] If you want to put your granola meeting transcripts in here, you can put them in here. And you have to just make sure you know maybe you're doing something like this, right? So, you're just like meetings and then you're like, "Okay, these are this is, you know, project one." And then every time you do a

[32:26] meeting, um, you take your granola notes and you just put them in here, right? So you're like meeting Greg Eisenberg Vin plus VIN and then you know that file is created now and you can just drop your trans you can just drop your meeting notes in here and now that's in the vault and then you can pass that into the agent or the agent will discover it, right? Especially if you start tagging like oh I'm going to tag this back to you know like my podcast or something there. Now it's connected. So now the

[32:53] the the agent it has like more context and now it knows that trans this transcript is related to this other file. Great. Um I think that's up to you. I think the way that you the the

[33:04] amount of information that you put in here is up to how you want to use the vault and how you want to delegate to things to agents and maybe you even want to create different vaults for different purposes. For me per for me I use LLM and agents as a way to increase my own level of understanding of subjects. So I use it for a lot of reflection and things like that. So I don't want an

[33:25] agent to write into the files. Like I could easily get it to do that. Like I could just say like even here I' I've asked it to write a description of some commands that I can talk about today.

[33:36] But I don't I don't I don't want it to make a file to do this because I want to control all the files in my Obsidian vault because I I always want it to pull from what I think about things, right? Not what it thinks about things. And if it starts making its own files in this vault, then I don't know like is like when it's finding these patterns, is it finding patterns about things it's written or is it finding patterns about things I've written? So I create a rule

[34:00] for myself which is like a strict separation between these things. I only want it to write things on the side here and then I will take that and and and and write what I think um should be included. >> Right. Some

[34:15] >> Yeah. Go ahead. No, I was just going to say like, you know, I could see the power of just using it for your own reflections.

[34:25] >> I can also see the power of, you know, AI is really good at, you know, going out on the internet, finding information based on trends and stuff like that. Distilling it in a way that you want and having that being put into your world is also interesting. Yes, totally. I think that and also like

[34:48] let's say if you asked um the Obsidian if you asked the um cloud code to go through your Obsidian file and generate ideas which um you know ideas for tools that you should build well then you can just like say okay cool if that's if I have an idea for a tool that I should build just generate a description of that and then just build the tool. So >> exactly. >> Yeah. I want to show this one so that

[35:15] it's like less on reflection. Like for example like you know I'm a I built this thing called ideab browser.com and every single day we give this validated startup idea like someone theoretically can go and >> you know grab that information put it in an obsidian vault and then based on that basic you know help them build the actual thing right >> totally yes so I want to show you this because I think it'll it'll really make it it'll take it out of the realm of reflection ction and into the realm of building. But the only issue is this

[35:50] takes a bit. So >> yeah, so the other thing is that with all of these like with these commands, another pattern that I'm noticing is that they take a bit because it's reading so many files. And I would say that's a big difference between using Obsidian and like or using cloud code with access to this Obsidian vault that I'm noticing is all of my requests are taking way longer and it's just because it's reading so much more. So like look

[36:18] at this one. So this is ideas demo. So I'll run a comprehensive ideas generation. Let me start by gathering

[36:25] vault structure and context in parallel. And then if you look it's really interesting to see what it's doing, right? So it's like Obsidian orphans, right? So it's it's it's it's like I

[36:37] guess orphans are like files that are on their own, not connected to things, right? So that's interesting that it knows that. Obsidian dead ends, Obsidian Resolved, Obsidian tag counts. So it's

[36:46] just trying to it's trying to figure out like some connection between all these things. Um and then it says, okay, daily read. So it's reading my daily notes.

[36:55] Then it found this file called new context, which is new is this media company I'm working on. Then it's like read file the other stuff context that that's podcast. The other thing I would say to you guys is I do manage um I write uh I create context files for projects that are pretty extensive. I'll

[37:13] show you I I was I didn't know if I was going to show this because it's very personal but like for the other stuff. Look at this. So other stuff working context. What shifted recently

[37:24] frontloading profile by traveling to San Francisco, New York City to record guests. This is super personal stuff, but what is the other stuff? The format, core beliefs of the show. Research is

[37:34] the foundation. Solid. The best conversations feel like discovery solid.

[37:39] You know, here's the team that's working on it. And so what happens is this again very personal, but this is um context that it just pulled in. So now it knows who's working on my podcast, what are the what are the recent hypothesis hypotheses I'm exploring. Um, and it

[37:58] just got that information. That's just like one of the things it did. Personal workflow context. Super personal file,

[38:05] but it shows like um, you know, like uh, what my daily schedules is like, you know, things that I have to do like in my personal life. So it's like pulling that how I like to work, how I don't like to work. Personal agent infrastructure is another thing. Let's

[38:22] see what happens if I pull this up. This is a project in which I want to take a step towards increasing my personal infrastructure workflow, delegation, however you want to describe it with agents, understanding what it means to delegate to agents more and more implementation approach. So this is like what I'm writing about the file about how I'm thinking about using agents personally. And again, that's an

[38:44] example of one of the files it's reading. That's just one of them. So you saw like the other stuff, the personal workflow, and it's factoring that all in to this task I've asked it to do, which is generate ideas for me. Gathering data

[38:56] from your daily notes, calendar, and vault structure. This takes a moment since it's pulling from multiple sources. Again, one of the um things with this is that it's just going through a lot of information, man. A lot

[39:08] of information, so it takes longer. You know, it's already been going for five minutes, right? And so that's that's something I'm noticing. But for me,

[39:17] that's what I want. I want that. I want I want a response from LLMs that is very very contextual uh to the things that I'm writing about. And I think a lot and

[39:28] I think that's how me and an agent can work best together where I just focus on continually um noting that my the the where I'm currently at in terms of the projects I'm working on and what my understanding is and what I find interesting. I want to maintain that and make it as current and as deep as possible. So whenever I'm talking to an agent, it has the best representation at all times of who I am in that moment when I ask the agent for something.

[39:53] >> Yeah, I mean that's the goal, right? You that's the question that we all should be asking of ourselves, which is >> does the agent have the most upto-date information on the projects, on my preferences and my dreams and my hopes and my goals? Um because you're it's only as good as the up-to-date version of that. Correct.

[40:15] >> Yes, 100%. The quality the the quality of information that the agent has entirely determines what it can do for you. Right. If it doesn't know a lot

[40:25] about you, it's not going to be able to do a lot for you. But if it knows a lot, then it can it can it can do things for you that I I think like even some of your in some it's kind of weird to say, but I mean like that you don't even know about yourself in ways. >> I mean it makes sense, right? Cuz

[40:42] ultimately what this is doing like to distill it to its core, it's connecting the dots. >> Yes. >> Obsidian and Obsidian and Claude code here are are connecting the dots. Now,

[40:54] it's actually quite difficult as a as a business owner or just as a personal in our personal lives to connect the dots. Like why do people in a lot of ways go to you know coaches, therapists? >> Yes.

[41:06] >> Um you know if you go to a therapist and you know you have someone who is you're doing most of the talking, right? Think about it. You're doing a lot of the reflection and the therapist and coach is sort of guiding you. That's that's

[41:21] what this is doing in a lot of ways. And I'm not saying by the way that don't go to your therapist, you know, just >> but I'm but my point is it helps it helps you helps you uncover what are their dots and how you can connect them. >> Yeah, absolutely. And for me, yeah, it's

[41:40] just it's just really exciting. Um, and yeah, it's just it's just a crazy time with computers. So, let's look at this.

[41:47] This thing finished. So, this is an idea generation report. vault relationship exploration. This is this is pretty

[41:53] extensive, right? Like to get an idea report like I I think this is this is really going to show how we can move you move from reflection to something actionable. So structural highlights. So again, this is

[42:12] just Obsidian stuff, right? Orphans worth noting. There's some defense technology stuff here. just a theme

[42:18] that's growing in Canada. Massive intellectual investment sitting in isolation. Also, orphan agentic software. So, orphan just means these

[42:26] are files I haven't really linked. Random notes I just wrote once or something. Um, unresolved links that reveal latent interests.

[42:34] Uh, hidden relationships. Again, all reflection stuff. Fine. What's working?

[42:39] Obsidian cloud code as a combined system is working for me. This is producing genuine breakthroughs in thinking and output day per domain structure. when enforced. This is basically I started u

[42:50] splitting my schedule where each day has a specific focus. This is cool and this is very true. The Greg Eisenberg episode as a forcing function. It's compressing

[42:59] months of thinking about Obsidian and agents into a clear thesis with demos. Very true. It, you know, coming on the show and doing this forced me to um synthesize everything I knew and present it.

[43:12] But here's where we're going to the actionable stuff. Tools to build The slashgraduate slash command daily note idea extractor based on daily notes are full of idea sorry daily notes are full of idea tags and interesting thinking that never gets developed. The vault has nine idea tags but hundreds of undiscovered insights. Build a command

[43:33] that scans recent daily notes, identifies ideas tagged or not, and prompts you to decide create a standalone note, add to an existing file, or dismiss. This turns a daily node stream into a structured idea pipeline. Obsidian vault for new. It

[43:49] says I just have to manage and set up a central Obsidian vault for new. What that means is in the same way that I'm creating this vault and it has all my ideas and my patterns and everything like that. Um why would I not create one for my team where they like as a team we can go and ask this vault questions and we can all uh contribute to it. Here we

[44:10] go. Tools to start using. What is this?

[44:13] Typed for all external documents. Uh, interesting. A time blocking act that enforces day. A time blocking app

[44:21] that enforces day per domain. Meaning since I'm trying to focus on one thing each day, one aspect of my life, it's saying why not create a time blocking app that forces you to do that. Interesting systems to implement.

[44:35] One sentence in Obsidian agent handles arrests. This is literally the demo 3 version of the Greg Eisener. Eisenberg prep, you're already imagining it. The next step is to actually

[44:45] building it. Start small. Write schedule a call with person about topic this week in a daily note and have Otis or Claudebot or OpenClaw pick it up and handle it. So, it's saying maybe you can

[44:56] delegate right from the note itself is how I'm interpreting that. Super interesting. >> Yeah, I just inline inline delegation like >> maybe that's even like a new UX pattern.

[45:07] I don't even know, right? That you could build into like these different tools. Um, subjects to investigate. Christopher

[45:14] Alexander's pattern language applied to digital spaces. Interesting. Um, Black Mountain College as a model for the stadium. Stadium is a physical space we

[45:23] have in Toronto. Authorless media as a concept. Uh, how Shenzen's hardware ecosystem actually works. Things to

[45:31] write and publish. That'd be useful. Context architecture essay. The computer

[45:36] as a place. Software will become fashion. What Toronto theory actually is. Editorial thinking zen conversations

[45:45] to have. This is interesting. These are real people. Aaron stadium workshop host

[45:50] about becoming an anchor of technical programming. This is a space we have in Toronto. Trun another person program about making program the flagship series. Steph ango obsidian CEO about

[46:00] the vault as a place. Um and so this is like yeah this is crazy. It's it's suggesting people I should meet, right? Top five

[46:11] high impact do now. Build the graduate command or do a manual weekly idea review. Um, >> this is crazy, dude. This is actually

[46:21] crazy. Like, and the fact that it's in plain text and it just not be it's not there's no images. It It doesn't make it easy to read, but I kind of like it because it's it's like dressed down. You

[46:35] know what I mean? >> Yeah. I mean, I like that aesthetic cuz I'm a nerd, but you could just say, you know, you could you could just say, obviously, you could just say, can you turn this into a beautiful readable HTML file that is on my desktop? This is hard

[46:50] to read and it's going to do that. >> Mhm. >> Right. So, I mean, if you don't that

[46:54] says if you don't like that, just do it however you want to do it. You know what I mean? I I like it like this in this kind of like this aesthetic. Um, but

[47:02] yeah, that's how you can move out of reflection. And of course, you know, of course, we could also say like here, you know, if we don't if we don't want to do this, uh, we could also say like it it recommended that /graduate command. So I could just say build the slashgraduate command.

[47:18] >> Mhm. [sighs] >> Right. Which is interesting.

[47:22] >> And is that how you started building a lot of your commands? Like it it sort of it started suggesting it and you're like just go build it. >> Well, I started off actually like building them myself. Like I'm like, oh,

[47:34] trying to think about commands myself. But then yeah, I said I started asking the agent like, well, wait a second. >> What commands do you think would be interesting? And I just and this might

[47:43] be useful. Another thing that I like to do is I like to move to like higher levels of abstraction when I'm using an an LLM. What I mean by that is I could say like, oh, make a command that um tells me what I should focus on each day. And that's that's like um a command

[48:02] that I thought of. But when I when I another thing you can do is you can step back and I can say based on my obsidian vault and what you know about me form an understanding of what you think my level of understand like where you think my skill level is in terms of of a person and the projects that I'm working on and based on that suggest the kinds of commands I should use that would take me from the level I'm at to a higher level. Right? get like, you know, get it to

[48:33] suggest the commands for me instead of me suggesting the commands and I could pick between them. So, look at this. This is this is it was this was the agent's idea based on what it read in my vault based on the notes I'm taking.

[48:44] Right? So, let's see what this is. Daily note idea extractor ideas, insights, and original thinking accumulate in detail in daily notes, but rarely graduate into standalone notes where it can where they can compound through back links. This

[48:56] command scans recent daily notes, surfaces the best candidates, and helps decide what to promote into like an idea or something, right? Sure. So, this is how it's going to work. It scans all the

[49:07] recent daily notes. It cross references with the existing vault. It presents candidates. It graduates selected ideas.

[49:15] If uh if creating a new standalone note, create the note in the vault route. Write the note as a mini essay or working document that captures the core claim or question context from the daily note where it originated connections to other vaults notes as backlinks. Now all this stuff like it captures the core claimer question. You might be looking

[49:35] at this and think like okay this is just the text that the agent generated and it is but also it hits differently for me because I know like I'm writing a lot about these things. I know. I know. Like

[49:48] even like the mini essay thing. These are words that mean specific things to me, which is just so it's just so crazy. It's very contextual. I know what it's

[49:56] talking about because I spend a lot of time in this tool and I spend a lot of time writing. So yeah, created and it's going to create that command, right? And it's like that's that's nuts because I'm just going about making notes and I have this parallel agent that is looking at my notes and giving me ideas on how I can improve my workflow, improve my life. And then and

[50:18] then not only can it just suggest it, it just build the thing and it's done. And we have it right here. I could just hit it and it's going to run. That's crazy.

[50:29] >> If if I'm Open AI or anthropic, I'm buying Obsidian. [laughter] >> [gasps] >> Right. Cuz it's the missing link.

[50:40] >> Yeah, it's nuts. >> It's the missing link. Why? The fact

[50:42] that there are people like you've sold me on this, by the way. I have >> I've downloaded Obsidian. I think it's a free tool, right?

[50:50] >> It is. >> It's open sourced. I've downloaded it, but I have not created my vault because I wanted >> you, Vin, to take [laughter] me through.

[51:02] I knew that this was going to be great. I knew that I would go through this. This actually exceeded my expectations.

[51:08] Like this is the the fact like it makes no sense to me. It >> makes no sense. >> The the fact like that if you are if you are using if you are serious about using LLMs to take your ideas and put and and and get the most out of them. If

[51:28] you're serious about building, you know, what people are calling a personal OS, uh, and you are not using a centralized note-taking tool like this, >> Yeah. >> that uses markdown as the foundation, then you are not using LLMs properly. >> Yeah. Or at least not at the limit.

[51:50] >> Yeah. Yeah. Exactly. You're not getting

[51:51] the most out of it. >> Yeah. >> You're not getting the most out of it.

[51:54] So I think what's what's difficult about this is that it require it does require a lot of time. >> Mhm. >> And to actually set it up properly. It

[52:04] requires uh like Yeah. I mean, it takes a lot of time and and and the UI isn't is is so daunting in the sense that it's a blank canvas and it's not like, hey, you should like write your preferences over here or, you know, you kind of just have to you have to come up with these ideas yourselves. >> Yes. But

[52:29] that's still so amazing, right? Because I mean, even when we work with other humans, we have to find a way to explain things to them. And I just think it's so cool that now we can work with these agents and we still have to explain things to them, but we only need to explain them once because once we get it down on into a file, we can always reference that file. That explanation of

[52:48] a project or a preference or anything and it's always there and you can pass it in. >> Yeah. A file is like essentially perfect a perfect memory.

[52:57] >> Yes. >> Right. Human beings have memories like we recall things.

[53:02] >> Yes. But there's tons of studies that show that what we remember in fact is completely different than reality. For example, when we went and got our that haircut in Missaga, [laughter] I could have thought that I had the best haircut.

[53:19] You know, that's what my memory remembers. It was a great haircut, but who knows? It could have been the worst haircut I had ever gotten. [laughter]

[53:27] Now, Obsidian or whatever tool you end up using like you know if I had written >> yes >> like it it the memory the file the markdown file is perfect so that when I link that or I I recall it it is going to give me a perfect >> uh you know data point and the other thing about you know these files is that you hope well they're not biased basically they're as biased as the human being is in terms of writing the reflections. >> Yes. >> At that moment in time.

[54:01] >> Yes. It's crazy, man. And >> yeah, it's just crazy. And there's all

[54:09] there's all of these different aspects to it. There's the privacy of it and what that means. There's the power of it, the fact that now you can just work with these computers in natural language and just delegate to them. Um, there's a

[54:21] fact that there's people like me that are that are using these tools and trying to figure out how to delegate stuff to agents in this way. There's people that are like me that are even more hardcore in in different ways and and pushing them. And I just think it's such a crazy time to be alive because I think we are potentially watching a fundamental shift in the human relationship to computers. And it's

[54:44] [snorts] just I just I'm just really happy to be alive while this is happening. And I'm curious like how's this all going to unravel? >> Well, what's what's cool about this is 99.99%

[54:55] of people are not going to spend the time to actually set up something like this and make it a part of their daily lives. And the alpha, so to speak, is in terms of leading a more productive, happier, healthier, better, more money-making career is in in in using something like this with an LLM, >> I think. So, >> I'm not saying download Obsidian today, and I have no affiliation or whatever with them, but I'm saying like pick a It sounds like what we should all be doing.

[55:33] And I'm I'm talking I'm giving myself this this advice is like there's no excuse anymore for me not to be writing down and reflecting >> Yes. >> into markdown files. >> Yes.

[55:45] >> In a world that where LLMs use markdown files as the oxygen. >> Yes. Like people think tokens are the oxygen.

[55:54] >> Yes. >> But they're not. >> Yes.

[55:56] >> The markdown fires are the memories. Like think about what a human being is. >> Yes.

[56:02] >> You know, >> is a human being the the energy of a human being or is it the memories of you know what we recall? you know, >> I mean, that's like a philosophical question and maybe it's a a bit, you know, a bit of both, but it's, >> you know, I think that there's something really really fascinating about MD files as an underrated about them in order to to have a true computer experience in in today's day and age. >> Yeah, there's definitely something going on here. Some fundamental shift. Yeah,

[56:41] >> it's awesome. >> Yeah. And like I have bad my word, you know, I'm learning in real time, right?

[56:46] Like and I I don't have the right vocabulary to even explain this. >> Yes. And neither do I, man. Neither do

[56:52] I. I'm trying to I'm trying to figure it out in real time. That's that's why I think like I know I show something and and for me I'll do something or or I'll see something and my friends are like they kind of laugh because I'll just be sitting at my computer just tripping out. And I think it's because I really

[57:08] like computers and and I cannot believe that this is possible. I cannot believe that I can just be making notes on my computer like I have been since I was a kid and then all of a sudden this agent can scan through it and build things because of it and and like connect patterns that I could never see. It's nuts, man. It's nuts. And and at the

[57:31] root of it, you're right, is just a collection of interrelated markdown files. >> Yeah. Cool, man.

[57:37] >> I appreciate you. I don't know if you can see my mind, but my mind is blown right now. >> Thank God.

[57:43] >> Yeah. [laughter] >> Yeah. >> I wanted to do right by you. I also just

[57:46] like >> I say this every time, man, but I'm just going to keep always saying it to you all the time. I really, really, really, really appreciate everything that you do. I think your pattern recognition and your pattern matching is like like really underrated. I think there's a lot

[58:01] of things that you do that I don't think it's like difficult to see if you're not really paying attention. I I just want to say like thank you for uh for everything that you do. You're always putting on like new voices on your show.

[58:11] I see it. I really appreciate it and it's just been it's an honor to know you and yeah, just thanks for the opportunity. Thanks for everything, man.

[58:18] >> I appreciate you, Vin. You're a legend. I'll include links for where to follow criminally underfollowed internet vin on on X on his YouTube show uh podcast in the show notes and description. You can

[58:35] go and check him out there. Uh people, please play with some of these tools uh and let me know what you think. Let Vin know what you think, >> please.

[58:46] >> And uh Vin, I will beg you to come back on the show [laughter] another time. And I hope you come back on again. >> For sure, man. Thank you.
