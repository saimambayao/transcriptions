# Give Me 20 Minutes. I'll Teach You 80% of Claude Cowork

**Channel**: Linking Your Thinking with Nick Milo
**Duration**: 21:29
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=s3ccD6m6WKc
**Transcribed**: 2026-03-24 10:40

---

## Organized Notes

**Getting Started with Claude Cowork**

- Claude Cowork is a mode in the **Claude Desktop app** that sits between Chat (basic AI) and Code (programming) — designed for **non-coders** who want AI to work with files on their computer
- Setup: download the Claude Desktop app, sign in, toggle to **Cowork mode**, then select a folder on your computer
- Once a folder is linked, Claude can **read, modify, move, rename, and create files** within it — no need to keep uploading documents or re-explaining context
- **Connectors** in the sidebar let you connect to other apps and services for extended functionality

**Screenshot Organization Use Case**

- **Nick Milo** (creator of Linking Your Thinking, author, Obsidian educator) demonstrated organizing **324 unnamed screenshots** by pointing Cowork at the folder
- Initial prompt: "review these screenshots and propose a method for sorting them by **subject, intention, and possible use case**"
- You can watch Claude's **step-by-step thought process** in real time using the toggle — useful for catching when it goes off track
- First-pass categories were generic because Claude didn't know the user yet — categories were "best guesses" not tuned to the user's life or work

**Teaching Claude About You (Personal Context)**

- Key insight: Claude's suggestions improve dramatically when given **personal context**
- Process: point Cowork at an **Obsidian vault** (ideaverse) and ask it to build a "**dossier**" — a master digest of who you are, your intellectual DNA, beliefs, goals, and recurring themes
- Milo asked Claude to review his **Atlas folder** (knowledge and ideas section of his ACE framework: Atlas, Calendar, Efforts) and pull from highest-ranked notes, personal maps, manifestos, values, and goals
- Result: a **40-note dossier** that was "90% accurate" — some overemphasis on certain people or ideas, but very good overall
- Paste the dossier into **Settings > General > Personal Preferences** so Claude always has this context
- After adding personal context, the screenshot categories became **much more relevant** — even mapping to the user's ACE framework automatically

**File Organization with Context**

- With personal context loaded, Cowork can create **subfolders**, rename screenshots with **descriptive names** and **timestamps** (YYYY-MM-DD format), and move files into the right places
- It also generates a **markdown index file** listing what's in each subfolder — making screenshots searchable without scanning every image
- Progress tracking appears in the **right-hand sidebar** showing multi-step task completion

**Skills: Turning Processes into Reusable Workflows**

- After perfecting a workflow, ask Claude to "**create a skill**" based on what you just did
- Skills are **detailed instruction files** that teach Claude how to handle specific tasks your way
- Skills can be enabled via **Customize > Skills** in the sidebar, uploaded as files, or built directly in Cowork
- Once saved, skills run **automatically** when Claude recognizes the relevant context — you can also invoke them manually
- **Scheduling**: skills can be set to run on a schedule (e.g., "run this screenshot process on the first of every month at 9:00 AM")
- This creates a **personal library of processes** — documenting what works and teaching AI to replicate it

**Research and Writing Partner**

- Cowork works naturally with **Obsidian vaults** since they're just markdown files in folders
- You can scope access to a **specific subfolder** by right-clicking in Obsidian and copying the vault folder path — Claude only sees those notes
- Example: Milo pointed Claude at 14 markdown files in an "AI research" folder (articles, Twitter/X posts, personal frameworks) and asked it to:
  1. Identify **common themes** across sources
  2. Surface **contradictions or extensions** to existing frameworks
  3. Pull out **relevant insights** for building a curriculum
- **Model selection matters**: use **Opus** for deep thinking tasks (uses more tokens but better quality), **Sonnet** for general work, **Haiku** for simple tasks like transcription

**Five Convergent Themes Surfaced**

- **Context architecture beats prompting** — having linked notes provides far better AI context than crafting individual prompts
- **Memory is the real bottleneck** — AI forgetting context mid-conversation remains the biggest friction point
- **Human judgment remains essential** — AI surfaces tensions and contradictions but cannot resolve them for you
- The research synthesis was done in **under 5 minutes** and produced a formatted markdown file with four sections: convergent themes, contradictions/extensions, relevant insights, and a possible curriculum arc

**Obsidian as AI Thinking Partner**

- Claude Cowork makes Obsidian vaults accessible without requiring **command line skills** (unlike Claude Code, which required terminal comfort)
- **Holistic briefing**: ask "Where am I? What matters? What am I missing?" and Cowork analyzes your vault to produce:
  - Active projects ranked by priority
  - Progress updates on each project
  - Open questions requiring attention
  - Things you might be forgetting (taxes, logistics, deadlines, feasibility checks)
- **Image enrichment**: ask Cowork to grab and insert relevant images into notes to beautify them
- **Maps of content**: Cowork can create AI-generated maps of content that **resurface buried ideas** by traversing linked notes — finding relevant notes across the vault that might work in a larger project (e.g., a book)
- The power comes from **pre-existing note structure** — linked notes and folders act as wayfinders for AI, making search and synthesis far more efficient
- Key takeaway: **knowledge management and note-linking becomes more valuable, not less**, when combined with AI

*Quotable Quotes (Nick Milo):*

> "Context architecture beats prompting. What you need is not just one good prompt. You need fantastic context. And that's what you get with linked notes." [11:24]

> "AI can't resolve these tensions for me. They can just surface them initially so that I can use them as jumping off points to dig in for myself." [13:13]

> "I'm completing a task, but I'm also building my own library of processes, documenting what works for me, and teaching AI to do it how I like it." [08:57]

> "Structuring your knowledge and notes in your idea verse, it's actually only getting more important when you use AI. You don't want it to have to search through all this stuff from scratch." [20:17]

---

## What This Means for Your Work

Nick Milo's Cowork walkthrough validates the architecture you've already built with Claude Code — and reveals where Cowork fills gaps you may not have addressed.

**Your dossier approach is already more sophisticated.** Milo pastes a 40-note personal context digest into Claude's settings. You have `about-saidamen.md` loaded automatically via CLAUDE.md, plus a dual-layer memory system (Claude Code memory + Obsidian vault) that persists across sessions without manual copy-paste. Your setup is structurally superior — but Milo's "dossier" idea suggests you could periodically regenerate and sharpen `about-saidamen.md` by having Claude re-analyze your vault, especially as your roles shift (the OOBC consultant work is relatively new).

**Skills in Cowork vs. your 124-skill library.** Milo's "screenshot-renamer" skill is a single instruction file. You have 124 deduplicated skills with references, scripts, frontmatter, and progressive disclosure — plus a sync system across vault and skills-bucket. The gap: Milo demonstrates **scheduling** (run a skill on the first of every month). You don't have scheduled skills in Claude Code — your `/schedule` skill creates remote triggers, but recurring local automation (monthly vault cleanup, weekly briefings) isn't formalized.

**The "holistic briefing" maps directly to your `/context` skill.** Milo asks "Where am I? What matters? What am I missing?" — your `/context` skill already loads context from vault files, recent daily notes, and project files. But Milo's version explicitly surfaces **what you're forgetting** — deadlines, logistics, follow-ups. Your `/context` skill focuses on loading state, not generating actionable reminders. This is a concrete enhancement opportunity.

**Scoped folder access matters for your legislative work.** When drafting bills or resolutions, you could scope Claude's access to just the relevant BOL chapters, BAA references, and bill-drafting manual — instead of your entire vault. This reduces noise and improves accuracy for `/bill-drafter` and `/legislative-briefer` runs.

**Maps of content for buried ideas.** You have 9+ active software projects and a vault spanning governance, cooperatives, legislation, and tech. Milo's technique of generating maps of content to resurface buried ideas could help you find cross-project connections — e.g., design thinking patterns in your SEED Initiative that could inform e-Bangsamoro's citizen portal UX, or cooperative governance principles that map to parliamentary oversight workflows.

**Concrete next steps:**
1. Regenerate `about-saidamen.md` — have Claude re-analyze your vault to capture the OOBC consultant role, MoroTech evolution, and current project priorities more accurately
2. Add a "what am I forgetting?" section to your `/context` skill output
3. Create a monthly vault briefing automation using `/schedule` or a cron-based trigger
4. Experiment with scoped folder access when running legislative skills to reduce hallucination risk

### How This Can Improve Your Claude Skills and Workflows

**`/context` skill enhancement.** Milo's holistic briefing produces something your `/context` skill doesn't: a "what you might be forgetting" analysis. Add a fourth output section to `/context` that scans daily notes, project files, and calendar entries to surface overdue items, abandoned threads, and approaching deadlines. This turns `/context` from a state-loader into a proactive advisor.

**`/session-summary` + `/emerge` integration.** Milo's workflow of surfacing buried ideas maps to your `/emerge` skill (surface latent insights from vault notes). But `/emerge` runs on-demand. Consider triggering an `/emerge`-lite check as part of `/session-summary` — at the end of each session, surface 2-3 connections between that session's work and unrelated vault notes. This builds the "serendipity layer" Milo describes with his maps of content.

**`/vault-update` could generate dossier refreshes.** Your `/vault-update` skill reviews the vault and recommends CLAUDE.md improvements. Extend it to also regenerate `about-saidamen.md` when your roles, projects, or priorities have materially changed — ensuring the personal context stays current without manual intervention.

**New skill opportunity: `/vault-briefing`.** Check `~/Vault/Claude-Skills/index.md` — you don't have a dedicated periodic briefing skill. Milo's "Where am I? What matters? What am I missing?" could become a `/vault-briefing` skill that produces a structured report: active projects by priority, progress since last briefing, open questions, things you're forgetting, and cross-project connections. Different from `/context` (which loads state for a task) — this would be a standalone strategic review.

**`/connect` skill amplification.** Milo's map-of-content technique is essentially what your `/connect` skill does — finding connections between two domains using vault links. But Milo's version is broader: he asks Claude to traverse the entire vault and find notes that fit a theme (book illustrations). Your `/connect` requires two explicit topics. A `/connect --broad "theme"` mode could surface unexpected matches across your governance, cooperative, and tech notes.

**Scheduling for recurring skill runs.** Milo schedules his screenshot organizer monthly. Your `/schedule` skill creates remote triggers, but you could formalize recurring vault maintenance: monthly `/vault-update`, weekly `/vault-briefing`, post-session `/session-summary` auto-runs. This creates the "background intelligence" layer Milo describes — your vault maintaining itself.

**Project-specific applications:**
- **e-Bangsamoro**: Milo's scoped folder technique could improve `/bill-drafter` accuracy by limiting context to just the relevant BOL articles and BAA references during drafting sessions
- **Parliamentarian**: The research synthesis workflow (14 notes → convergent themes + contradictions) maps perfectly to legislative research — point Claude at a folder of related BAAs and surface policy tensions before drafting interpellation questions
- **MoroTech/SEED Initiative**: The 124 training course modules could benefit from a map-of-content approach — surfacing connections between design thinking, lean canvas, and cooperative governance modules that inform curriculum redesign

---

## Transcript

[00:00] Claude Co-work combines its signature chat style with the ability to work directly with files on your computer, completing tasks, rearranging files, and even updating content in apps like Obsidian. I'm Nick Milo, and in this video, I'll cover how to set up Claude Co-work. Use it as a productivity partner on your most important work and then become a thinking companion that works alongside an idea verse in Obsidian using just the right amount of AI to manage your notes and to better improve how you link your thinking.

[00:31] Let's dive into the basics. To use co-work, download the Claude desktop app and sign in with your Claude account. Inside the desktop app, you'll see a toggle bar up top that lets you switch between three different modes. Chat is your normal AI interface. Code on the far right is an advanced mode you can use to program things with AI. And then co-work is in between, the sweet spot for doing pretty much anything that you'd want to do with AI without requiring a coding background. It works by selecting a folder on your computer, clicking allow or always allow if you don't want to keep reapproving the same folder, and then just like that, Co-work can see everything in the folder that you've linked. You don't have to keep uploading documents or reexplaining context. Claude can read files. It can make modifications, move things around, rename them, and even create new files, especially if you use the connectors in the customized section of your sidebar. It allows you to connect to other apps and services.

[01:37] Now, in a recent video, I walked through my big clean process where I cleaned and sorted the surfaces of my computer and put everything into structured folders. As a result, I end up with bigger folders of screenshots from each year, but I don't have any names or context. So, I'm curious, what if I point at that folder around 300 screenshots from this year and just see how it can organize them? Then I can type something like or speak out loud, please review these screenshots and propose a method for sorting them. I'd like to sort by subject, intention, and possible use case. Don't dig into any subfolders. And it goes to work.

[02:06] As it's working, you can actually watch what it's doing. You can click on the toggle and see its steps and thought process. And if it starts to go off track, this is how you can identify when it does. Go ahead. You can hit stop, adjust your input, and retry. In the right hand sidebar, it's tracking the progress and actually letting you know which files it's been opening up.

[02:28] Now, I chose 324 images, a substantial amount of images, so it'll take a while. And here we go. It's come back with a bunch of suggestions, categories, groupings, and some follow-up questions for me. Now, it's ready to just move ahead and process all that, but I'm not ready personally. I think this is really interesting and already has some good suggestions, but I think we can do even better.

[02:51] So, let's actually try something. Now, the fact is Claude doesn't really know me yet. So, its categories here are just best guesses. They're not tuned to my life, my work, or what I would actually use these screenshots for. So, here's what we can do. We teach it.

[03:02] If you've watched my videos before, you know that my primary thinking space is in Obsidian. Inside my idea verse, I organize things with what I call the ACE framework. Atlas for knowledge and ideas, calendar for all my timebased inputs, and then efforts for my actions and outputs. In this case, I want to pull mostly from my atlas, which is where I keep my knowledge and my ideas.

[03:28] Within that, I have some key documents about myself, my interests, my goals, my reflections, and the things I really care the most about. So, I'm going to ask Claude to do the work for me to look through my idea verse and find the stuff that matters. Claude, review my Obsidian vault, especially my atlas folder and build a dossier on me. Pull from my highest ranked notes, my personal maps, my manifestos, my values, my statements, my goals, my sources. I want a master digest of who I am, sort of my intellectual DNA, what I believe, how I think, what I keep coming back to, and write it as nice, clean markdown. And boom, there it is. Let's hit enter.

[04:07] And now we wait. Oh, funny. See, I'm just in the screenshots folder, so I actually have to then switch folders to give permission to my ideaverse. I'm okay doing this. Your mileage may vary, but now I'm going to choose a folder, which is going to be my idea verse. And now it's going to do that work.

[04:28] And now it can look at my entire idea verse, which I'm okay with. You might not be. And specifically, it'll look mainly at the Atlas folder and try to get all this juicy context that I asked for.

[04:40] Okay, amazing. The dossier is done. 40 notes across Atlas. And so what we have here now is an intellectual dossier, a master digest of who I am, what I believe, and how I think. Now, would I say this should go in my obituary? By no means. I don't think it's completely accurate. I think there are times that it's overemphasizing certain people or ideas more than I would like, but this is 90% of the way there, and it's very good.

[05:10] So, let's go ahead copy this. Then what we can do is we can go over to settings and actually go to general and then under personal preferences we can now paste in all of that. So we won't ever get generic responses. But now when Claude responds to us, it's responding to us. In this case, it's going to respond to me. It's going to have all this context of who I am, how I think, and what matters to me.

[05:41] Now, updates won't apply immediately to the chat space that you're in. So, we're going to create a new task. It's still in co-work. The folder is screenshots. That's where we want it. And now we can ask that same question. That's the question.

[05:52] And let's try it again. Ooh, already the categories are much more relevant thanks to the context on who I am, how I'm thinking, and what my life priorities are. It's even saying that its proposed sorting method is matching ACE, separating knowledge assets, the atlas area, timebased artifacts, the workshop sessions and the launches with the effort based outputs, the marketing campaigns and the admin tasks.

[06:15] But here's where it gets really useful. I'll say, please create those subfolders and name each screenshot with a short description of its contents. But at the front of the title, always include a timestamp, year, month, and date. Then go ahead and move all the screenshots into their respective subfolders. And extra credit, create a markdown file that serves as an index listing what's in each subfolder by name.

[06:34] So, let's go and see how it works. And notice on the right hand side, you can see that there's this progress list where it's tracking the multiple steps to go through for your reference as it's doing its work. And it does all of it.

[06:53] Oh, look at this list. Instead of a wall of unnamed screenshots, I have organized subfolders, descriptive file names, and a searchable index. If I need to find a screenshot later, I don't have to scan every image again. I can just search the index.

[07:05] So, let's open up Vault and Obsidian. And now we can see it has a time stamp at the front, which I love. That way I can easily sort by time. And then we can just immediately go through and see all these relate. These are all related. They're all obsidian oriented. And we have the titles right here which are really helpful. So all of this is giving me immediate context. Oh, that's my vault and obsidian screenshots. And then there's business admin light framework assets, all sorts of things right here available for me.

[07:30] And the long-term value, it shows up when you turn this process into a skill. So after you've done this and you've tweaked it and you're happy with how it turns out, then you say, "Hey Claude, create a skill based on what we just did. Call it screenshot-renamer."

[07:48] Skills in co-work are basically a set of detailed instructions packaged as simple files that teach Claude how to handle specific tasks by doing it exactly the way you like it. You can enable built-in skills by going to customize then skills and clicking the toggle. You could download a skill file and upload it or like we're doing now, we can ask Claude to build one right here.

[08:08] Claude writes the code, tests the workflow, and once you're happy, just click copy to your skills to start using it whenever. And it's done. Now I have this skill screenshot renamer, and it's saved into the cloud's skill library inside the app, and it gets used automatically when needed.

[08:21] You can just say, organize these screenshots, and it will know what skill to run and how you like it done. You can tell it to use the skill if you want, but usually it recognizes the context and will use that skill automatically.

[08:39] I could take this a step further and say, "Let's run this screenshot process on the first of every month." Let it run. Click schedule here. Done. It'll run automatically on the first of every month at 9:00 a.m. This way, I can keep my screenshots organized in the background so that they never pile up again in the same way. How cool is that?

[08:57] I'm completing a task, but I'm also building my own library of processes, documenting what works for me, and teaching AI to do it how I like it. And skills can be unique to you, built around your actual life.

[09:14] Now, let's look at how we can use Claude as a writing or research partner. Now, I store the majority of my writing in Obsidian, which is basically a bunch of markdown files in folders on my computer. So, guess what? It's easy for Claude to look at it.

[09:24] But instead of giving full access, I can always choose to identify a different folder here. Or what I can do is actually I can look at the example folder that we want to use which is called AI research. And if I right-click I can copy the path from vault folder and then just say hey look here. And it's going to know exactly where to look. Nowhere else but just these notes will be part of the context that it's about to pull up.

[09:55] These 14 markdown files. There are some articles. There are some Twitter/X posts mixed in with all that. Some of my own frameworks for playing defense and offense with AI.

[10:03] So now I can say something like, I'm trying to synthesize all of this research alongside my own thinking. Can you identify the common themes across the sources in this folder? Can you surface any areas where their approaches contradict or extend my existing frameworks? And can you pull out the most relevant insights so that I can start building out a curriculum of my own to tackle some of these ideas?

[10:18] I'm looking to try stuff out, but also to get some jumping off points for thinking through my own perspective on these new developments, especially regarding how they integrate into my idea verse.

[10:40] And with Obsidian, I'm going to ensure that I'm using Claude's Opus model on this one because it's better. It uses up tokens faster, but it will do a better job. In general, I try to use Sonnet first because it's less intensive, but pretty good. Haiku is if you're doing something really easy, maybe like transcribing a website, but I rarely use that one otherwise.

[10:54] Okay, so Co-work has gone through it all and made a markdown file that I can open right in Obsidian. It's formatted, clear, and already super interesting after less than 5 minutes of processing.

[11:06] So, part one is the five convergent themes. So, if I collapse that, part two is where the sources contradict or extend my frameworks. Part three, the most relevant insights for building a curriculum. And part four, a possible curriculum arc.

[11:17] I'm less concerned with these bottom two, and I want to focus on these top two. Five convergent themes. Context architecture beats prompting. Yes, I've been trying to say that prompting is so overrated. And what you need is not just one good prompt. You need fantastic context. And that's what you get with linked notes.

[11:32] When you have an idea verse of notes, they're linked together and they have folders as wayfinders for AI. You have the best of both worlds. And that's where it gets really powerful for those of us who have already been doing knowledge management, who've already been making notes and linking them to other notes. Now we can actually reap the fruit of that labor in new and fascinating ways.

[11:56] Memory is the real bottleneck. I think we've all agreed on that. Context is a bummer when you're talking to AI and it suddenly forgets everything and you're like, "What's going on? Why aren't you working?"

[12:08] So markdown one definitely had a voice in that with my Obsidian Just One video. And well, I must say it's encouraging to see that we are in alignment that there needs to be strong human judgment no matter what.

[12:31] Now, what's interesting is that since I gave it my own perspective and asked it to find tension and challenges, we've got this whole section here where these sources contradict and extend your frameworks. So, tension one, deep AI integration versus sacred separation.

[12:45] So my position currently has been using the IDI framework. Some other things that we won't cover now and it's interesting to see where the sources are pushing back on that. Structure must be earned versus architecture must be designed. Very curious about this one because I can feel my blood boiling. Structure must be earned. When you try to build structure from the top down, it breaks.

[12:56] So, I am ready to just tear apart this counterargument here or at least try to understand what are they actually saying. And it goes on, for the most part, these are legitimate contradictions to my philosophy that are surfaced before I even dig in deeper myself. I'm getting a bird's eye view with this, but AI can't resolve these tensions for me. They can just surface them initially so that I can use them as jumping off points to dig in for myself.

[13:31] And the great thing is with this artifact, with this markdown file, I can edit it in Obsidian directly right here. And it's persistent. I can take it with me anywhere. I can use it as a jumping off point into another app. It's a building block for future thinking.

[13:37] All right, this is where things get really exciting. If you use Obsidian, your entire thinking system is already a folder of markdown files on your computer. That means co-work can work with your idea verse directly.

[13:49] In a previous video, I showed how you could use Claude code to do things like analyze your daily notes, populate metadata across hundreds of files, or even pull images for people notes. That was powerful, but it required the terminal and it required a comfort level with a command line interface that a lot of people just don't have. And honestly, that includes me.

[14:10] But with Claude Co-work, you don't have to worry about that. I've already shown you how to point Cowork at a folder on your computer. Ideally, your Obsidian vault, which I'm calling an ideaverse, or some duplicated vault or some subfolder so that co-work can work directly with the files within.

[14:20] As you do that, I want to share with you a few really cool applications that I'm doing. Okay, co-work based on my recent activity and active projects and just the notes and the things that I've been working on. Where am I? What matters? And what am I missing? And let's see what happens.

[14:44] Okay, and it's done. My holistic briefing, it's here. I can read the short version of it or again I can click on the markdown file and we can read it here. So let's just see from the top kind of work our way down.

[14:56] So holistic briefing first active projects by rank. So it looked into my idea verse. If I have a project in there and usually for most of my notes I'll try to give it some sort of rank scale from 1 to five. Only the greatest things get like a 5.1 and above.

[15:14] So in this case, active projects by rank. I'm working on the book and it's giving me — this is really cool. These are things that I've worked on and it's telling me right here, this is some of the progress that you've made. We can see the list keeps going.

[15:24] Book momentum. All right, we've made some great progress. Open question. It's asking me like, okay, so how are you going to communicate with your editor at Simon and Schuster?

[15:38] And then intellectual life. These are things I worked on. Let's see the dossier on myself, which we did earlier for this video. The book Beyond Belief by Near Iel that I was writing a review for. Asteroid extinction research. Very cool.

[15:48] And oh, actually I think I want to come back to this one. This is really cool. But one of the coolest sections is definitely what you might be forgetting. So there's a big move coming up and it's telling me make sure you get all the logistics in order. It's also saying taxes are coming up. Make sure that you do the things you need to do there.

[16:06] And hey, remember Obsidian Launchpad? You had a feasibility check with the team. Make sure that you actually go through that check and are you on pace for it? And it's telling me, hey, here's what you can do next. This is fantastic.

[16:13] And it's not just here, but it actually knows because I've set this up in advance where to put a note like this in my idea verse. So, I can just start to search for — well, guess what? It's the latest note. So, it shows immediately up. And here's that same holistic briefing in my idea verse in Obsidian.

[16:33] So, the next one is just do grab an image for a note. So, hey, I was looking at this asteroid thing, and there's something really cool about it. So, let's pull that one back up. I'm going to go ahead and search for this note, asteroid theory and dinosaur extinction.

[16:44] And if we twirl down the properties, we won't cover this now, but I'm telling myself that this text below was actually generated not by me, but by AI. And I don't like doing this very often, but for the sake of this example, this is a note. It came in. I just watched Dinosaurs on Netflix narrated by Morgan Freeman, produced by Steven Spielberg, retelling the dinosaur story. It's fantastic.

[17:12] And I just kind of want to beautify this note. So, I can actually go over here and say, "Hey, in this note, and I have the file path, which we went over earlier, can you please grab an image and throw it into this note to beautify it a bit?"

[17:32] And let's wait to see what happens. And boom, just like that, the image is here. And now when I look at this note, it's kind of good. It's kind of nice.

[17:38] But I think the reason that it's resonating for me is that I have something on my mind. I'm writing the linking your thinking book for the spring of 2027. And I think there's something here with ideas about how ideas emerge over time, like the theory of the asteroid. It was proposed in 1980 and it took until about 2010, 30 years for it to be the scientific consensus.

[18:04] So what did that look like? How did that idea emerge into consensus? That might be a story that I want to put into the linking your thinking book. So I'll just link up to my linking your thinking book note.

[18:18] But this has got me thinking. What if along with AI, I created a map of content that will resurface all of the rich thoughts and ideas across my ideaverse over here that might work in the big book.

[18:35] Okay, new one. Looking at this asteroid note, I'm realizing this is exactly the kind of rich unexpected idea that could bring a chapter to life in the book I'm writing. Sir Raz's poalism, for example, it's already in chapter 4. Tolkien is woven into the inner guide chapter. And I know I have more notes like this buried across my vault. Historical moments, scientific surprises, artistic breakthroughs, personal stories.

[18:49] What if I could surface them all and see what fits? So with that in mind, create a map of content on this and mark it as AI generated. This will be interesting. And the reason AI is able to do this so effectively is because my notes are linked. So when it finds one map of content that already exists on my favorite concepts or the way I like to think and rapidly it can fill up with rich context, relevant context to help resurface at the right time in the right way the notes that mean something to me.

[19:39] Okay, done. Your new map of content is Atlas Maps book illustrations map of content. It's in a perfect spot. So let's check it out. I'm really excited for this one. We can see it's the new note at the top and paradigm shifts, scientific surprises, asteroid theory, Darwin's epiphany, natural selection, where good ideas come from, emergence.

[19:53] That's all talking about the same sort of feel there. Leonardo's solution to the hardness problem with sfumato, star knight, Khayyam, and it's suggesting where it might be able to fit philosophical or conceptual gems.

[20:09] So, all these are great. I'm like, "Hey, I haven't — I wanted to use this in the book, but it was buried. It was buried." And now I can see it coming back again, and that's really exciting for me.

[20:17] So, when you have maps of content like this, it gives your AI a highlevel sense of what's already inside your idea verse. So, again, we're seeing that structuring your knowledge and notes in your idea verse, it's actually only getting more important when you use AI. You don't want it to have to search through all this stuff from scratch. You want it to have a top level understanding of how things are linked that you or your mini AI thinking partner will always be able to work more efficiently.

[20:36] All of this just scratches the surface of what we've developed and refined over the last 6 years. If you want my entire Obsidian and AI system, it's all in Obsidian Launchpad. Obsidian Launchpad will guide you from setting up Obsidian for the first time all the way through to mastering it and giving your thoughts the home they've always deserved.

[20:56] If you want to build a modern operating system in Obsidian or just want to start using Obsidian for yourself casually, start with Launchpad. The link is in the description below. And to really get the most out of any AI system, you need a system of folders, files, and memory for your AI that isn't stuck in any one app. That's what we're breaking down in the next video in the series. So, go ahead and watch that right here next.
