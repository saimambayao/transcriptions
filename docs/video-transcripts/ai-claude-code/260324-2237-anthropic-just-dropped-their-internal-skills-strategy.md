# Anthropic Just Dropped Their Internal Skills Strategy

**Channel**: Ray Amjad
**Duration**: 18:43
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=7PnF8qctDi8
**Transcribed**: 2026-03-24 22:37

---

## Organized Notes

**The Default Output Problem and Distributional Convergence**

- Without skills, Claude produces the **statistically most likely output** from training data — this is fine for standard tasks (authentication systems) but terrible for creative work (design, marketing)
- The "purple gradient" design problem is caused by **distributional convergence** — all design examples in training data blend together, and Claude outputs the safe, common pattern at the high-probability center
- Skills work by **steering the model to sample from different parts of its training data distribution** — activating low-probability but high-quality regions that exist in Claude's knowledge but wouldn't surface by default
- Without skills: 1,000 people asking "build me a landing page" get nearly identical outputs. With unique skills: each person gets distinct results shaped by their brand, preferences, and experience
- **Bad skills restate obvious behavior** — they push the distribution further toward the default center instead of away from it. Example: turning a generic AI-generated design into a skill just locks in the generic pattern

**The Gotchas Section: The Most Valuable Part of Any Skill**

- Anthropic says the **gotchas section** is the single most valuable component of any skill
- Analogous to training a new employee — you don't just give instructions, you share **hard-won lessons about what goes wrong**
- Example: A customer support reply skill that starts promising "resolved in 24 hours" — add "never promise specific timelines" as a gotcha
- Skills become **richer knowledge bases over time** as more gotchas are added from real usage
- Most people **make a skill once, notice a mistake, and never improve it** — the flywheel only works if you actively maintain gotchas
- Anthropic's internal example: a billing library skill with accumulated gotchas for prorations, test mode behavior, and API keys — encoding **implicit engineer knowledge** into the skill

**Avoid Railroading Claude: Goal-First, Not Constraint-First**

- **Rigid skill instructions collapse the output distribution** into a narrow path with no room for Claude's judgment
- Bad example (interviewing skill): "Write 3 behavioral questions, 3 technical questions, 1 culture fit question" — a senior architect gets the same questions as a junior intern
- Good example: "Prepare interview questions for this role. Test for what actually predicts success here. Here are the traits our best hires have had." — gives Claude flexibility to adapt
- **Goal-first approach with context** beats constraint-first approach — define what success looks like, not the exact steps to get there
- If output is bad, don't add more constraints — add **gotchas** instead (e.g., "never ask family-related questions")

**Progressive Disclosure: Don't Cram Everything Into One File**

- Main `skill.md` should contain **goals and gotchas only** — not all reference content
- Use **separate markdown files** in subfolders (e.g., `formats/linkedin.md`, `formats/newsletter.md`, `formats/twitter.md`) for platform-specific or context-specific details
- Claude loads **only the relevant reference files** based on the current task, keeping the context window high-signal
- Ray Amjad's own approach: separate reference files for kernel tuning vs. certificate management operations — only loads what's needed

**Skill Descriptions as Routing Logic**

- Skill descriptions should be **semantic routing triggers**, not marketing copy
- Bad: "A comprehensive tool for monitoring pull request status across the deployment lifecycle"
- Good: "Monitors a PR until it merges. Triggers on: babysit, watch CI, make sure this lands"
- Include **all semantically similar phrases** a user might say when they want the skill
- Ray's example: image cleanup skill with triggers "clean up images, delete unused images, flatten images, tidy up images"

**Scripts as Pre-Built Functions**

- For skills that fetch external data, **pre-build the API interaction scripts** instead of having Claude figure out the API every time
- Without scripts: Claude reads API docs, writes requests, wastes tokens — and repeats this every skill invocation
- With scripts: Claude **composes pre-built functions** to analyze data and produce insights immediately
- Demo: Combined YouTube analytics + Stripe revenue + PostHog website data into a single skill with Python scripts, HTML report template, and `.env` for API keys
- The skill was created by first having Claude figure out the API, then telling it to **save the working code as reusable scripts** via `/skill-creator`

**On-Demand Hooks for Skill Security**

- Hooks can **restrict what a skill is allowed to do** — blocking web access, environment variable reads, file editing outside approved paths
- Solves the risk of API keys being exposed through prompt injection or unexpected behavior
- Example: The revenue report skill was locked down to only run its pre-built Python scripts and create HTML files — no web fetch, no env reads, no editing library files
- **Claude Code can generate hooks for you** via the Claude Code guide sub-agent — describe the restrictions and let it write the hook frontmatter

**Skill State and Continuity**

- Skills should maintain **persistent state between runs** via log files, JSON, or SQLite databases
- Use case: A content writing skill stores previous suggestions (to avoid repeats) and published topics (to write from different angles)
- Storage options: JSON, `.txt` log, SQLite — commit for team sharing or `.gitignore` for personal state
- Using `claude-plugin-data` path ensures **data persists even when the skill itself is updated** from an external plugin library

**Skills as Operational Packages**

- Think of skills as **mini-applications**, not instruction documents — they contain scripts, assets, reference files, configuration, and runtime data
- The best skills **fall cleanly into one category** — don't span multiple distinct tasks
- Skills should **combine together** rather than overlap — a bug-hunting skill might call a DataDog skill to gather diagnostic data
- For shared skills: add a **setup wizard** via `config.json` + a `/setup` command that interviews the user for their specific parameters (channel ID, API keys, etc.)

*Quotable Quotes:*

> "The most valuable part of any skill is a gotchas section — things that Claude has to be careful of. It's very similar to hiring and training a brand new employee. You wouldn't just give them instructions. You would tell them about things that will come back and bite them." [04:40]

> "A bad skill would be restating obvious behavior to Claude Code. You'd be restating something that Claude already has a high probability of being able to do." [02:43]

> "Many people make a skill once, then they notice Claude makes one mistake, and they never bother to improve on the skill or add that as a gotcha." [05:50]

---

## What This Means for Your Work

This video directly addresses the engineering of your 124-skill library. Anthropic's internal strategy validates several patterns you already use while highlighting specific improvements.

**What validates your approach:**

- Your **progressive disclosure** architecture (skill.md + references/ + scripts/) already matches Anthropic's recommendation. Your /bill-drafter with `references/drafting-principles.md`, `references/word-choice-guide.md`, and `references/bta-legislative-process.md` is textbook progressive disclosure.
- Your **/skill-optimizer** and **/auto-research** loop already implement the iterative improvement cycle Anthropic describes — though they focus on prompt mutations rather than gotchas specifically.
- Your **skills-bucket** sync system (skill.md + references/ mirrored across vault, skills-bucket, and active skills) already treats skills as operational packages.

**What challenges your approach:**

- **Gotchas are underrepresented.** Review your top 10 most-used skills (/bill-drafter, /legislative-briefer, /fact-checker, /bangsamoro, /youtube-transcriber, /devwork, /frontend, /tdd, /prompter, /session-summary). How many have an explicit gotchas section? The distributional steering argument suggests gotchas may be more valuable than the process instructions themselves.
- **Some skills may be railroading.** Your /legislative-briefer has a rigid 13-section CSW format. While this is a government-mandated structure, the individual section content should use goal-first prompting ("assess the fiscal impact" not "write 3 paragraphs about budget implications"). Review whether process steps are constraining quality.
- **Script pre-building is underutilized.** Your /notebooklm skill has CLI commands but they're inline instructions, not pre-built scripts. The /fact-checker could pre-build web search and reference file comparison scripts.

**Concrete next steps:**

1. Audit your top 10 skills for gotchas sections — add explicit "things Claude gets wrong" based on your actual experience with each
2. Review /legislative-briefer for railroading — check whether rigid section-by-section instructions are collapsing the distribution vs. goal-first framing
3. Add semantic trigger words to skill descriptions — especially /bangsamoro, /fact-checker, and /bill-drafter which may not trigger on all relevant phrasings

### How This Can Improve Your Claude Skills and Workflows

**Skill improvements:**

- **/bill-drafter** — Add a gotchas section: "Never use 'and/or' in legislative text (cite the 10 BAAs that misuse it)", "Always check BAA-49 for existing provisions before creating new structures", "MFBM not DBM, MOLE not DOLE in BARMM context". These are exactly the hard-won lessons from your ECCD bill review that should be permanent gotchas.
- **/fact-checker** — Pre-build scripts for the most common verification patterns: name lookup against `barmm-officials-2025-2026.md`, BAA reference validation against `~/Vault/bangsamoro/bangsamoro-laws/index.md`, RA number verification. Currently Claude re-discovers these file paths each invocation.
- **/youtube-transcriber** — Your skill already has progressive disclosure (scripts/transcribe.py as pre-built). Add gotchas: "Never leave garbled non-English characters", "Always research garbled names from auto-captions", "First mention rule for people's full names and titles".
- **/legislative-briefer** — Refactor from constraint-first ("Write Section 1: Measure Description, Section 2: Background...") to goal-first with format guidance ("Produce a comprehensive legislative analysis. The output should follow CSW format with these 13 sections. For each section, assess what matters most for parliamentary decision-making.")
- **/skill-optimizer** — Add an eval criterion specifically for "gotchas density" — skills with more gotchas relative to their process instructions should score higher.
- **/bangsamoro** — Add semantic triggers to the description: "BARMM, BTA, BOL, Bangsamoro Organic Law, autonomy, peace process, Moro, MILF, MNLF, Cotabato, Marawi, wali, intergovernmental" — currently it may not trigger on all relevant Bangsamoro-related queries.

**New skill opportunity:**

- **/skill-auditor** — A lightweight skill that reads a skill.md and checks for: (1) presence of gotchas section, (2) description contains semantic triggers not just marketing copy, (3) progressive disclosure (references in subfolders, not embedded), (4) scripts for API interactions. Output: a quality scorecard per skill. Check `~/Vault/Claude-Skills/index.md` — no dedicated auditor skill exists (closest is /skill-optimizer which focuses on prompt optimization, not structural quality).

**Workflow changes:**

- **Hook security for /fact-checker and /notebooklm** — Both skills access external services. Add hooks restricting them to only their pre-built scripts and expected file paths, following the security pattern demonstrated in the video.
- **Skill state for /youtube-transcriber** — The transcript index (`docs/video-transcripts/index.md`) is already a form of skill state. Formalize this: add a `claude-plugin-data` reference so the index persists independently of skill updates.

---

## Transcript

[00:00] Okay, so yesterday Anthropic released the most incredible guide on writing good effective Claude Code skills that everyone has seen. Now this covers a lot of the key lessons that they learned from making hundreds of skills that they have in use across pretty much the entire organization. I'll be breaking it down with a bunch of nice images, examples, and things that you can be doing to improve your own skills and workflows. All right, now starting out

[00:22] they talk about why skills even matter and that is because of the default output problem. When you give a prompted model, it will give you statistically the most likely thing based on its training data. And this can be good in situations because if you're implementing an authentication system, you want to be given the most likely most common authentication system because it will work. You don't want the

[00:43] model to be overly creative when it comes to designing something that important. You want to follow the standard procedure that everyone else is using. Now, the problem is when it comes to things like design, it can lead to bad output. For example, we've all seen

[00:55] the purple gradient into font like same layout AI looking design websites and that is because of distributional convergence in the training data. All these examples of designs have been blended and washed together that Claude will only give the safe common patterns that it finds. But by using a skill, you can make the model sample differently from its training data distribution. So

[01:16] with the right words, you can basically make it use unique fonts, move towards experimental layouts or different kinds of animations and essentially move it away from the high probability boring center to like a more specific and creative regions of its training data. So you can kind of think of skills as being a way to differentiate yourself from everyone else. So for example, if a thousand people say build me a landing page, they will all get pretty similar designs from Claude Code. But if everyone

[01:41] has their own unique design skill that is kind of influenced and contains information about design they like and also their own experiences and kind of what they're after and their brand guidelines and so forth, then everyone will be seeing a different outcome. So the way to think about skills is that they're basically overriding the default behavior and pushing the model to less common and more specific parts of its knowledge. You're kind of invoking a different part of the model's latent space to get better and more distinct outcomes. Another way to imagine this is

[02:07] that you will get the Claude Code default behavior by not using a skill and your outputs will be very similar to pretty much everyone else's over here. But a skill is kind of like a forcing function that forces the underlying distribution to take a different shape and give you different outcomes. So whilst the knowledge that you're after does exist in the model, for example, right over here, it has a low probability. But by

[02:27] using a skill, you're kind of activating this low probability region over here to give you different outcomes. Now, what this means is that a bad skill would be restating obvious behavior to Claude Code. You'd be restating something that Claude already has a high probability of being able to do and achieving. So, for

[02:43] example, if I said make me a landing page in a brand new project and I didn't give it any additional information, then it would give me a pretty generic AI looking design right over here. And then if I told Claude Code, okay, you know what, like turn this into a skill. So, I would trigger the skill creator and be like, okay, turn this into a skill for me. Then it would take that default

[03:00] behavior, turn it into a design-related skill and make all successive designs with that skill look very AI-related. Which means that the bad distribution that would kind of look like this without a skill would end up pushing up to look more like this with a skill instead. But good skills are pushing Claude to new outputs and then steering the underlying distribution. And this

[03:19] means that when you're making a skill, you usually want to be encoding something such as your own lived experience, your own expertise, or something that you found online. So, for example, if you asked Claude, "Hey, can you help me with marketing?" Then it would give you really generic and boring advice that won't really help you stand out because everything that is trained on already contains a lot of that advice and people are already following it. Now,

[03:41] Claude does know better marketing advice and it does know how to do things more uniquely. So if you gave it a few examples, then you could turn that into a skill because that skill would be steering the underlying distribution to give you better outputs more suitable for your goal. And one of the common ways that I've seen people do this is that they listen to a really good podcast episode that talks about an idea that not many people are talking about.

[04:02] And they kind of want to expand on this idea and understand how it applies to their projects and start applying it every single day. So they would get the transcript of that podcast, turn that into a skill, and then triggering that every time they're getting help with Claude for marketing. Now I have talked about this idea in more detail a few weeks ago at my Claude Code master class which is the most comprehensive class on Claude Code that you will find online. Now I am working on the Claude

[04:26] skills class of the master class which will be the most comprehensive class on Claude skills that you will find. So if you are interested there will be a link down below to sign up. Now they say the most valuable part of any skill is a gotchas section. So things that Claude

[04:40] has to be careful of when it comes to using the skill and it's very similar to hiring and training a brand new employee. You wouldn't just give them instructions and be like hey here's the work and go do it. You would usually tell them about things that they have to watch out for, things that will come back and bite them. And basically all the

[04:55] experience that you've gained so far in doing the thing yourself. Similarly you should be ingraining this knowledge into your skills as well. So for example let's say you made a skill to help you draft customer support replies. You

[05:07] might make the skill and then realize that it starts promising timelines to customers of "I promise that this will be resolved in 24 hours" and this is a real failure that your customer support people learned not to make and you did not tell Claude the exact same thing. So you would add to your skill at the bottom "never promise specific timelines, say we're working hard on it" and you would use the skill again, read its outputs, it'd be improved. And as you add in more and more gotchas, your skill becomes like a rich knowledge base that will be applied consistently over time. And this is exactly the flywheel that makes skills more and more valuable over time. A lot of people make a skill once, then they notice Claude makes one mistake, and then they never bother to improve on the skill or add that as a gotcha. So, by you taking the time to

[05:50] add that to your skill, you will already be doing better than most other people. And the example that they use is they have a skill for an internal billing library that isn't really captured inside Claude's default behavior. So, by making it a skill, they will see Claude does a better job at dealing with anything billing related inside their repository. Now, the first gotcha they

[06:10] add is like prorations round down, not nearest cent. Then they add another for test mode, another one for keys. And a lot of this knowledge would already be ingrained inside the heads of engineers and employees. So ideally

[06:22] you should be getting this knowledge, this implicit knowledge, outside of people's heads inside your Claude skills. Now next up they talk about avoid railroading Claude. And this is very similar to another idea that I talked about a few weeks ago in my Claude Code master class. But

[06:37] essentially what many people do with skills and just Claude in general is they give it a really rigid set of instructions because a lot of people say skills are kind of like recipes or you want to give it some workflows, instructions. And this can be helpful in some situations when there's a very specific way of doing things. But in other situations, it's not as flexible or versatile. So for example, let's say you made a skill to help you interview candidates and it came up with a bunch of questions that you should use. A bad

[07:05] skill would kind of be like write three behavioral questions, write three technical questions, and write one culture fit question. So this is really rigid and it doesn't allow for any flexibility. Now what would happen is that if you used a skill like this, a senior architect would get very similar questions to a junior intern and you won't really be able to pull out the best in them. Essentially you have a

[07:26] rigid recipe that gives you identical outputs regardless of the context. So you want to take a more goal-oriented approach where you give Claude some information and the flexibility to adapt. So a better example would kind of be like prepare interview questions for this role. Test for what actually

[07:41] predicts success here. Here are the traits our best hires have had. And then you give it a bunch of relevant context for your organization and then you will find your interview questions are much better for whichever roles that people are applying for. And if you notice its

[07:53] output being bad, then you can go back to the previous section and then add the gotchas such as never ask family-related questions or something. Which means that in many situations, it can be better to take a goal-first approach with context than to take a constraint-first approach instead. And to relate this to the distribution thing that I said before, the way that I imagine this in my mind is that when you railroad Claude, then you're basically collapsing this wider distribution that it has for creating a creative solution, an optimized solution, and so forth. You're

[08:22] collapsing this down into a really rigid small path. Instead, you basically eliminate all optionality and you have no room for Claude to make its own judgment. Now, next up, you want to make use of progressive disclosure and you don't want to cram every single thing into the single skill.md file. So, for

[08:39] example, if you had a content repurposing skill, then you know that different types of content does well on different platforms. What works on LinkedIn will not necessarily work on YouTube or Twitter. So, you would have your main skill.md outlining any gotchas

[08:53] and the main goal to avoid railroading Claude. And then you would have separate markdown files inside a formats folder that contains information on effective LinkedIn posts, effective newsletters, and then Twitter threads and so forth. And that means that if you were repurposing one bit of content, then Claude would be able to load in only the files that are relevant. Which

[09:12] means that if you wanted something repurposed from a newsletter to a LinkedIn post, then Claude will be able to load in only those files that are relevant, keeping the context window high-signal and avoid adding irrelevant noise to the context window. Now the way I do this in my skills is that I have reference files. So I have one file for kernel tuning. I have another one for

[09:32] operations like certificate management. And this is helpful because Claude Code may not always be troubleshooting something and just needs to know some operations stuff instead. Which means that only the relevant context will be loaded in when it needs to be. Now next

[09:44] up, your skill descriptions should be routing logic for Claude and not marketing copy. So many people write their skill descriptions kind of like they were advertising their skill to a human for example or telling a team member of what exactly it does. So a bad description would be something like "a comprehensive tool for monitoring pull request status across the deployment lifecycle." But you may notice that

[10:06] Claude may not know when to trigger the skill because it doesn't mention any other keywords that a user would be mentioning in their query. But a good skill description would be something like "monitors a PR until it merges. Triggers on: babysit, watch CI, make sure this lands." And then Claude can semantically match any user question or query to a skill easily. And you can kind of see this in this skill that I have which is an image cleanup skill for my Ray OS folder. And it says over here

[10:34] "triggers on: clean up images, delete unused images, flatten images, tidy up images" and so forth. And these are all semantically similar to things that I would potentially say when I want my images cleaned up in this project. Now, you also want to be improving your skills with scripts that Claude can run.

[10:49] And this is especially important for skills that are fetching data and using data from an external source because otherwise if you just give it an API key and say go figure it out, then Claude will spend a bunch of time looking at the API documentation, figuring out how to make the requests and stuff. And if you don't save that information inside of the skill, then that can lead to wasted tokens and time every single time that skill is triggered in the future. But if Claude has pre-built functions in a library file, then it can simply compose them together in the right way to analyze the data and give you insights rather than wasting tokens and potentially being distracted by the fact it has to figure out how an API works. And a practical example would be something like let's say I wanted to make a skill that would combine my YouTube analytics and then my Stripe data and then also PostHog as well for the website to figure out which videos are driving most of the traffic and sales to my applications. What I can

[11:42] do is I can basically make a read-only API key for Claude Code. I'll give it read-only access to everything because I don't want it doing something crazy. And then I can copy this API key, give it Claude Code, which should be fine because it's read-only. And then I can say

[11:56] something like using the Stripe API key and also Super Data, can you figure out which of my recent videos have been driving most of the sales? Can you correlate the release date with the revenue that came the days after? I think there's also some metadata attached to checkout that should help you with that. And then once you figured out how to use the API effectively, can you turn that into a set of scripts that you can call reliably so that you don't always have to make up the requests every single time. And then I can go to

[12:24] something like Super Data for example, give an API key from there as well and then also give it a link to the documentation as well. And finally, I can trigger the skill creator skill by just doing /skill-creator and say make this into a skill. Now you can see that Claude Code is trying to figure out with a bunch of Python code and testing all these scripts that it should make and run. Okay, so now finished making me the

[12:45] skill with a bunch of Python files that I can use next time to run through the skill faster and focus more on the results rather than building out the scaffolding pipeline to gather that data. And the final report kind of looks like this. So it looks pretty good to me. And then the scripts kind of look

[13:02] like this. So we have a Stripe API script. We also have a report HTML template that can use every single time and then we have an .env that contains API keys going forwards. Now they also talk

[13:13] about using on-demand hooks with Claude skills. And if you don't know much about Claude hooks then I have a whole video about that in my Claude Code master class linked down below. But essentially what you can do with Claude hooks is restrict the scope or access of the skill to make it more secure going forwards. Now, one

[13:29] of the problems in the skill that we just made so far is that Claude Code may decide like, okay, I'm going to gather some other data or I'm going to edit this Python script around and then read the environment variable directly or something like that. Then it might decide to access a random website on the internet and maybe get prompt injected and give our API key away. So, we can make our skill even more secure with a bunch of Claude hooks. So the way we do

[13:51] this is we can use a Claude hook to restrict Claude Code to only being able to run those scripts and then banning pretty much everything else. And hooks are defined at the top in the front matter. But writing hooks manually is kind of tedious. So we can get

[14:05] Claude Code to make them for us. And the way we do this is by triggering the Claude Code guide sub-agent and then we can describe the behavior that we want. Can you make a hook for the skill that will basically restrict the skill to only being able to use those Python files? It should not be able to read the

[14:22] .env. It should not be able to do any curl requests or access data online or do a web fetch or something like that. It should only be able to use those scripts and then make an HTML file for us. Basically add any relevant hooks

[14:35] that blocks any behavior that is not what I just described. All right. So now we can see that it made a bunch of hooks to block any kind of web access,

[14:42] editing the library files that we made earlier, reading the environment variables and a bunch of other stuff. So this will make our skill even more secure going forwards and it will make sure that it only does behavior that is expected of the skill. All right, so next up, you may also want to add some kind of log file or storage to your skills so it can help remember earlier things that have happened the last time it ran. Or for example, you may have a

[15:05] skill that helps you write content and any previous suggestions or outputs that are bad are stored into one log file or data file and then anything that you have previously written about and published before is stored into another file. So the skill knows not to write about the same topic again. Or if it does write about the same topic, then it knows to write about it from a different angle perhaps. And essentially this will

[15:27] help ensure continuity between skill runs because a skill will know what it did the last time it was called. And this can either take the form of a JSON file, a simple log file, .txt file, or a SQLite database. And then you can either commit this so the rest of the team can use it or you can .gitignore so that everyone has their own copy for when the skill last ran. And if

[15:47] you tell Claude Code to add this to your skill.md called claude-plugin-data, then it will store it reliably on your computer somewhere such that if the skill was updated from the external plugin library, then the data would not be lost. Okay. Now combining everything that we talked about so far, we want to be thinking of skills more as operational packages for completing a specific task. And that means that they

[16:09] should contain any scripts, assets, reference files, configuration, and also any data from the last time that they ran. Essentially, it's kind of like having an employee whose sole role is to do one particular task. And the people who are treating skills like this are getting the most value out of them.

[16:24] And you will also notice the best skills fall cleanly into one category. You shouldn't have skills trying to span too many categories or complete too many different distinct tasks at once. They should only be focused on doing their particular task really well. The analogy

[16:39] that I personally find helpful is that each skill is kind of like its own mini-application that has a specific goal. So one skill may be for gathering data from a certain source and then just making a nice visual out of it. Another skill would be only dedicated to finding the relevant websites of competitors. For

[16:56] example, another skill they have is gathering data from DataDog, for example. And that would of course be different from their bug hunting skill. And their bug hunt skill may realize that they need to use the DataDog skill to gather more data about what the bug should be. So skills should be able to

[17:11] combine together and you should be having complementary skills rather than overlapping skills. Now, finally, if you're going to be sharing your skills, you may want to consider having a setup wizard inside your skill. Now let's say I wanted to share my video revenue report skill with some friends who want to run it on their own data or YouTube channels. Then I can make a nice

[17:30] config.json file here. And then I can have something like YouTube channel ID and YouTube channel handle. And then

[17:36] in my skill.md I can have something like this. So it says "your config." And what

[17:41] this command does is it's a bash command that loads in the data from the config file in the skill folder that I have. If there's no config file, then it will just say "not configured." And then if I edit this, I can basically say ask the user what their channel handle is and then use that and the Super Data API to find their channel ID and update the config. Now, this can be really handy

[18:05] for skills that are shared widely within an organization and everyone is using the same skill but need slightly different config. But if you're not really sharing your skills with others or in an organization, then there's no real point in doing this. Anyways, there's a bunch more information in the article that I will be covering later on this week in my Claude Code skills class. So, if you are interested in

[18:24] signing up to it, then it will be available within my Claude Code master class. And there are a bunch of other classes that you may find handy about prompt engineering, context engineering, my own daily workflows, and a bunch more things as well. You also do get access to free videos from the class if you sign up to my Claude Code newsletter.

[18:40] And you also get many insights from me whenever I discover new things.
