# Stop Fixing Your Claude Skills. Autoresearch Does It For You

**Channel**: Nick Saraev
**Duration**: 16:32
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=qKU-e0x2EmE
**Transcribed**: 2026-03-23 01:55

---

## Organized Notes

**The Auto Research Concept**

- Based on **Andrej Karpathy's auto research GitHub repo** — a system where agents autonomously optimize a process
- Karpathy's original use case was optimizing **nanoGPT training**, but the methodology applies to anything measurable
- The repo has only **three files that matter**: `prepare.py` (ML-specific, ignore), `train.py` (maps to your **skill.md**), and `program.md` (maps to your **agent instructions**)
- Core idea: provide an agent with a skill file + evaluation criteria, then let it **iteratively improve the skill prompt** automatically

**Three Ingredients for Auto Research**

1. **Objective metric** — a measurable number, not vibes
   - Website example: **load time in milliseconds** (went from 1100ms to 67ms — 81.3% improvement over 67 tests)
   - Cold email example: **reply rate**
   - Skills: **eval pass rate** (percentage of tests passed)
2. **Measurement tool** — automated, reliable, no human in the loop
   - Websites: **Google Lighthouse**
   - Skills: an **agent-written test suite** that runs evaluations in sequence
3. **Something to change** — the variable being optimized
   - Website: code changes
   - Skills: the **skill instructions / markdown prompt** itself

**Understanding Evals for Skills**

- Prompts are **inherently noisy** — same prompt can produce different outputs each run
- Must run skills **many times** (not just once) and measure the **mode and median** of results
- All AI outputs are **distributions of data**, so you need statistical rigor
- Think of evals like **school tests** — standardized questions that benchmark performance
- Best practice: use **binary yes/no** questions for each criterion

**Building an Eval Suite (Diagram Generator Example)**

- The skill generates **clean hand-drawn style diagrams** from natural language using **Nano Banana Pro 2** (~2 cents per generation)
- Four evaluation criteria defined:
  1. Is all text **legible and grammatically correct**?
  2. Does it fit the **color palette** (pastel, soft colors — no bright reds/neons)?
  3. Is it **linear** (left-to-right or top-to-bottom flow)?
  4. Is it **free of numbers, ordinals, and ordering**?
- Scoring: 10 diagrams x 4 criteria = **max score of 40**
- Started at **32/40**, reached **39/40** (97.5%) after several auto research runs

**The Auto Loop Process**

- Every **2 minutes**: generate 10 diagrams, evaluate against the 4 criteria, score out of 40, mutate the prompt, keep the winner
- Uses **Claude Sonnet vision** for evaluating diagram outputs
- Opens a **real-time dashboard** showing legibility scores and total scores per run
- Everything runs **autonomously** in the background after initial setup
- Total optimization cost: approximately **$10** for 50 test runs

**Tips for Writing Good Evals**

- **Go binary** (yes/no) wherever possible — scoring scales like Likert compound variability and make results unreliable
- **Don't be too narrow/stringent** — overly concrete constraints (word counts, symbol restrictions) cause the model to **game the eval** rather than improve quality
- Like a student who gets 100% on a test without understanding the material — the skill technically passes but actual quality suffers
- Too many eval points leads to **parroting** the criteria back without genuine improvement

**Broader Applications**

- Apply auto research to **any skill**: proposal generators, agent reviews, model chats
- Can create a **meta skill** that optimizes every skill in your repo
- Beyond skills: optimize **websites, landing pages, email copy, titles, thumbnails** — anything with a measurable outcome
- The **research data itself** (list of all attempted changes) becomes a valuable asset — pass it to future models like **GPT-6 or Opus 5.0** to continue optimization

## What This Means for Your Work

**Auto research is the methodology your /skill-optimizer and /auto-research skills already implement -- this video confirms you are on the right track and reveals calibration details.** Your ~/apps/autoresearch-mlx setup with Karpathy's nanoGPT training loop on Apple Silicon is the ML-specific implementation. But the broader application -- running iterative eval loops against any skill with a measurable metric -- applies to every skill in your 129-skill arsenal. The 81.3% improvement Nick achieved on website load time (1100ms to 67ms over 67 tests) demonstrates the scale of improvement possible when you let the loop run long enough.

**Your /bill-drafter skill is the highest-value candidate for auto research.** Define four binary eval criteria: (1) Does the draft correctly reference the relevant BOL articles? (2) Does it follow BTA parliamentary formatting standards? (3) Are all officials named with correct titles per the verified reference file? (4) Does it include proper implementing rules and repealing clauses? Run the skill 10 times against a test prompt, evaluate each output against these criteria, mutate the prompt, keep the winner. At ~$10 for 50 test runs, optimizing your most critical skill is trivially cheap compared to the cost of submitting a flawed bill to Parliament.

**The "go binary, don't be too stringent" advice is critical for your eval design.** Nick warns against overly concrete constraints (exact word counts, specific symbols) because models will game the eval rather than improve quality. For your legislative skills, this means evaluating "Does this provision align with BOL Article IX?" (binary yes/no) rather than "Does the provision contain exactly 3 whereas clauses and reference the BOL by full title?" The former tests substance; the latter tests surface compliance that the model will parrot without genuine improvement.

**The meta-skill concept (a skill that optimizes every skill in your repo) should be your next build.** With 129 skills in your skills-bucket, manually running auto research on each one is impractical. A meta-skill that iterates through your highest-use skills -- /bill-drafter, /youtube-transcriber, /fact-checker, /humanizer, /bangsamoro -- running automated eval loops on each and logging the results to your vault, would systematically improve your entire toolkit. The research data itself (all attempted prompt mutations and their scores) becomes a knowledge asset stored in ~/Vault/Claude-Skills/ for future model upgrades.

**The cost math works overwhelmingly in your favor.** At 2 cents per diagram generation and $10 per 50-test optimization run, the economics of auto research are trivial compared to the value of your outputs. A single bill draft that reaches Parliament without factual errors or BOL conflicts is worth orders of magnitude more than the $10 optimization cost. Run the loops on your critical skills and let them improve overnight.

### How This Can Improve Your Claude Skills and Workflows

**Your /skill-optimizer skill should adopt Nick's exact three-ingredient framework as its core loop.** Define (1) an objective metric (eval pass rate), (2) a measurement tool (agent-written test suite with binary yes/no criteria), and (3) the variable to change (the skill's markdown prompt). Your current /skill-optimizer already does iterative improvement, but formalizing these three ingredients as required inputs before any optimization run starts would make the process more systematic. The eval design is the bottleneck -- not the loop execution.

**Priority skill optimization queue based on usage frequency and error cost.** Your 129 skills are not equally important. Rank them by two dimensions: how often you use them and how costly a failure is. /bill-drafter (high frequency, high cost -- errors reach Parliament), /youtube-transcriber (high frequency, low cost), /fact-checker (medium frequency, extreme cost -- missed errors propagate), /bangsamoro (high frequency, medium cost -- context errors cascade through downstream skills). Run /auto-research on the top 5 first, then work down the list.

**The "don't be too stringent" warning applies directly to your Bangsamoro-specific evals.** When writing eval criteria for /bill-drafter, avoid constraints like "must contain exactly 5 whereas clauses" or "must reference the BOL by its full title in every section." These are surface-level criteria the model will game. Better evals: "Does the bill's purpose align with BDP 2023-2028 priorities?" (substance), "Would a parliamentary legal reviewer find a constitutional conflict?" (quality), "Are all named officials current per the 2025-2026 reference?" (accuracy). Binary, substantive, hard to game.

**The research data itself (list of all attempted prompt mutations) should be stored in your vault.** Nick mentions that the list of changes the model tried becomes a valuable asset for future model upgrades. After every /auto-research or /skill-optimizer run, save the mutation log to ~/Vault/Claude-Skills/{skill-name}/optimization-log.md. When Opus 5.0 or a new model drops, feed it the log and let it continue optimization from where the previous model left off. This is institutional knowledge about your skills that compounds across model generations.

**Build the meta-skill Nick describes by extending /skill-optimizer with a batch mode.** Your /skill-optimizer currently runs on one skill at a time. A batch mode that iterates through your skills-bucket, runs 10-test eval loops on each, and produces a dashboard of pass rates across your entire library would give you a health score for your skill ecosystem. Skills scoring below 80% get flagged for deeper optimization; skills above 95% are marked stable. Store the dashboard in ~/Vault/Claude-Skills/optimization-dashboard.md and update it weekly.

---

## Transcript

[00:00] I freaking love Cloud Code skills. I think you do, too. But sometimes they're a little bit unreliable. I would say

[00:06] about 70% of the time I run a skill, I get an intended output. About 30% of the time, it's a bag of rocks. What I wanted to do in this video is I wanted to show you how to combine Claude Code skills with a new development in the AI space called Auto Research to achieve significantly higher reliability, accuracy, and allow your skills to quite literally improve themselves overnight.

[00:25] So, I'll keep this as simple and as straightforward as possible. First, I need to show you where this idea of auto research comes from. To make a long story short, one of the former founding members of OpenAI and later head of AI at Tesla, it's called Andre Carpathy, released an auto research GitHub repo a few days back. And what this does is

[00:44] this allows a team of agents to autonomously optimize some process. This process in his case was the training of another machine learning model called nanoGPT. But in our case, it's going to be our skill and actually improving that skill over time by making the prompt better, better, and more airtight. Now,

[01:03] you don't need to read the whole repo. There actually only a couple things in here that I think are important and immediately applicable to the purposes of, you know, business or improving skills. And they are as follows. This

[01:13] repo is deliberately kept small and only has three files that matter. The first is this file called prepare.py. The

[01:19] second is a file called train.py. And the third is program.md. So to make a

[01:24] long story short, this prepare.py, this is like machine learning specific stuff. So we don't actually need to worry about it. This is something that is specific

[01:30] to uh training a tokenizer and so on and so forth. The stuff that actually matters for us is train.py and program.md. And so I want you to pretend

[01:39] for a second that this train.py is actually your skill.md.

[01:44] And then your programm is just your agent. And basically what we do is we're going to provide a prompt to our agent in a program.md. And the prompt is going

[01:53] to say, "Hey, I want you to improve this skill using the method discussed in auto research." The way that you're going to measure whether or not the skill is fantastic or crappy is as follows. And then we're just going to give it some brief uh criteria, which in machine learning terms is typically referred to as an eval. And then in that way make

[02:11] the skill better and better over time. Now, just before I go any further, I want you to know this is a pretty big development. You don't just have to use it for skills like I'm going to show you here. And I want to make that clear in

[02:20] this video. uh just as I did in my last video. You know, earlier this morning I was a little bit bored and I was like, "Hey, what can I use this cool auto research library on and I realized that I had this old app that I developed many years ago and I was just curious, hey, how much faster could I make this thing?" So, all I did was I took the

[02:36] same repo that I just told you guys and then I said, "Hey, I want you to use the same approach to make my website faster." And over the course of about 67 different tests, this auto research methodology took my load speed from about 1100 milliseconds literally down to 67. This is sort of the same thing that we're going to do with our skill.

[02:54] It's just we're going to be responsible for developing the eval set, which I'm going to cover in a few moments. So, I mean, in our case, we had an 81.3% improvement in time. In your case, it

[03:03] might be an 81.3% improvement in accuracy. Who knows? Uh, but what's

[03:07] really cool about this is not only will you get the actual improvement itself, you get a big list of changes that the models will have tried to make in order to improve your skill. Which means since AI models are getting smarter at any point in time over the course of the next few years, you just take this big list of things, just pass it on to the next agent. You could take this big list and pass it on to GPT6 or Opus 5.0 and

[03:28] it'll be able to pick up where its predecessors left off. I think this is actually probably soon to be one of the most important and valuable assets of our time. just a bunch of research data.

[03:36] But anyway, you don't care about that. You care about how to make your skills better. So, let me run you through it.

[03:41] Uh, in order for auto research to work, you need three ingredients. You need an objective metric. Okay? Now, that's a

[03:47] number that you can measure. It's something that doesn't feel faster or resonate more or or whatever the heck vibes the kids are talking about these days. It's an actual number. So, in my

[03:57] website example, it was a load time in milliseconds. Um, I'm now running auto research on cold email campaigns, so it's my reply rate. In our case for skills, what this is going to be is this is going to be called our eval or evaluation pass rate. I'll show you guys

[04:10] how to make that in a second. Next, you need some form of measurement tool. This ideally would be automated, reliable.

[04:16] There'd be no human in the loop. For that website example I just showed you guys, I used a suite of basically website testing tools called Lighthouse that Google provides out of the box. That's how I figured out how long it took to load the site. You know, for my

[04:28] cold email uh suite, I'm using API analytics for instantly. Now, for us, what we're going to do is we're actually going to have an agent write what's called a test suite, which is just like an order of operations saying, "Hey, I want you to run the first evaluation, then run the second evaluation, then run the third evaluation, and so on." Finally, you obviously need something to change, right? So, you know, in my

[04:47] website example, that's the code changes. My cold email example from yesterday, that's the email copy itself. In our case, it's just going to be the skill instructions. Basically, it's

[04:55] going to be the prompt, okay? It's going to be the markdown file. And so if you think about it logically, what we're going to be doing is just like in Andre Carpathy's auto research repo is we're going to be providing the skill as sort of like our I don't know our train. py

[05:08] over here. And then we're going to be providing the agent some highle instructions. We're just going to stick that right over here in like the programm.

[05:16] And then we're just going to have it basically say, hey, every time you run the skill, I want you to evaluate it against a suite of tests that we've developed and then tell me whether or not it's better than what we did the last time. And then in this way, I just want you to get better and better and better over time. And I want you to run this every 5 minutes. And that takes me

[05:31] to this concept of eval. Now skills are just prompts, right? And prompts are inherently noisy. What I mean by that is

[05:37] sometime you'll run a prompt and it'll do X. Another time you run a prompt and it'll do Y. And so in order for us to develop a standardized set or suite of ways to improve the quality of our skills over time, we can't just run them once. What we have to do is we have to

[05:51] run them many, many times. And then we have to take the mode which is the frequency and then the median which is kind of like the average of results. You know if I run 20 skills and all of them are task to generate me an image which is going to be what we're working on today. Um you know every single time

[06:06] there going to be some slight differences but there are going to be things within each diagram or every image that is similar and there also going to be some things that are different. In reality, all machine learning and all AI outputs are distributions of data. And so, in order for us to control against that and allow us to make iterations and improvements on them, we just need to run them many, many times. But running multiple times

[06:28] is not enough. We also need to evaluate the outputs of our skills according to some standard. You know, it's kind of like testing back in school. You could

[06:37] know everything there is to know about astronomy, okay? But there's no way to assess your knowledge unless we give you a test on it. And those tests are going to be similar sorts of questions asked in similar sorts of ways. So what you

[06:49] can think of is what we're doing here is we're basically benchmarking the performance of our skills. And the best way to do that is using binary yes or no true or false questions. So as a really meta example today, I want to show you how to improve a skill that I call diagram generator. If I scroll over here

[07:06] to the right, you'll remember this diagram that I showed you guys and used to mark up a moment ago. Well, I actually used AI to make that. And that's the skill that today I want to improve successfully over time with standardized evals and out of research.

[07:19] Now, in our case, it's hard for me just to look at it and say whether it's good or bad, right? And so instead, I want to have a series of standardized questions that I could ask another agent to review it to tell me whether or not this thing is good. And realistically, I can't just say, "Hey, you know, is the text legible?" I can't just say, "Hey, you

[07:39] know, does it look good?" I need to break it down a lot more granular than that. Now, you might be wondering, well, what the heck does that look like for a diagram? In my case, I have narrowed

[07:47] down four criteria to make a high-quality diagram. The first is, is all of the text in the diagram legible and grammatically correct? If so, odds are it's an okay diagram. The second is,

[08:00] does it fit my color palette, which is defined as pastel colors, soft colors. I don't want like super bright reds or oranges or neon greens because I find that just looks unprofessional and lame. The third is, is it linear? Does it go

[08:11] left to right or top to bottom? You know, previously I was generating a lot of images that just were all over the place and I don't know, there was spread out bob bubbles and bobbles and so on and so forth, which just looked odd. And then fourth, is it free of numbers, ordinals, and ordering? in case you

[08:26] didn't know that basically is just the presence of 1 2 3 4 which is kind of meta because that's how I decided to number this. But the point is if all of my diagrams are free of all of these things, odds are that's a good prompt. You know, it does something that I want.

[08:40] So what I'm going to do is I'm going to take this give these requirements to my agent. I'm going to ask it to create an evaluation test set for me and then I can just run this thing on auto loop over and over and over again until my skill is fantastic. Okay, the first thing you need to do is set up something that allows you to communicate with Claude Code. In my case, I'm doing this

[08:58] in anti-gravity. So, I have an anti-gravity window set up with the Claude Code extension inside of it. You guys could do this in whatever way you want. Second thing you need to do is

[09:08] grab the um Andre Carpathy auto research repo. So, I'm going to go back over here and then I'm going to copy this link. Then, I'm just going to feed this directly into my agent. I'll say read

[09:19] this. Next, we need our eval test suite. So, I'm going to go back to my Chrome instance and just grab these four and head over here. And then for third, I

[09:30] should say, we actually need to tell it what we want it to do. So, I'm just going to use a voice transcription tool called Whisper Flow. And then just in natural language, ask it to do this.

[09:38] Hey, I want you to use the auto research convention in the above repo in order to build out a self-improving skill system for my diagram-generator skill. The eval suite I'd like you to run is the four constraints above. What I want to occur is every 2 minutes I want you to generate 10 diagrams for a specific function. Whatever those

[10:05] functions are are okay. And then I want you to pass them through this eval test suite, rate how many of those made it, and then alter and improve the prompt as necessary to get it to the point where it's knocking 10 out of 10 out of the park. Okay, I'm then going to press enter over here. And this is going to

[10:23] feed everything into, in my case, Opus 4.6. It'll start by reading the auto research repo, which is up here. Then

[10:31] it's going to explore the diagram generator skill. You might be wondering what the diagram generator skill is. Well, it's actually really simple. It's

[10:38] basically just generate clean handdrawn style diagrams from natural language descriptions. The output should look like a whiteboard sketch with pastel rounded rectangles, simple line art icons, thin arrows, and clean labels on a white background. The way it works under the hood is we send the request over to Nano Banana Pro 2, and then we get these things that we could paste onto my Excaladraw. My total cost is

[11:01] about 2 cents per generation using this super fast model. And that means, you know, if we're going to run 10 every single time, logically speaking, I'm going to spend about 20 cents per test. So, if within 50 tests I can get it to a good place, I will have optimized the skill for about $10. And just given how

[11:18] much money my YouTube videos make me, you know, a good banger video might make me several hundred in ad revenue per day. Um, obviously this is like a pretty positive return on investment for me. So, I'm going to give it some time, let it read everything it needs to read, and then circle back when it's ready. And

[11:31] just halfway through, I decided to clarify the scoring mechanism. So, what I want, as mentioned, is I wanted to generate 10 images. I have four criteria. So, that'll be a max score of

[11:40] 40. Um, that means that I'm going to generate 10, evaluate all 10 against the four criteria, count the score out of 40, make iterations the prompt, try again, and then pick the winner. Um, and I just gave it that because I I realized after I did the voice transcript, I didn't specifically mention I wanted to run 10 times. And it's now opening up a

[11:57] real time dashboard for me to show me the results, which I think are really cool. So, as you can see here, we have the first test already in with legibility scores and total scores right over here. And it looks like another experiment just concluded where we went from uh 32 up to 37. And it's just going

[12:15] to continue making this prompt better and better and better to adhere to my specifications over time. I mean, in my case, we started with a 32 out of 40. So, that's pretty dang good already.

[12:23] Realistically, I imagine this is only going to take a few runs to get to where we want to get it to. But that is the magic of auto research because we're all going to have different uh definitions of good. We're all going to have different, you know, constraints in Eval test suites. So what might be 32 out of

[12:38] 40 for me might have started for you at like a two out of 100. The one thing that matters is just how much time you let it run on. So if it runs for, you know, a couple of days, couple of weeks, couple of months, you can imagine you could start basically wherever the hell you want and eventually it's going to be fantastic. The core thing is just

[12:53] defining the right set of evals. And my recommendation is always just make them simple yes or no answers uh good or bad. And now it's just going on in the background. You can see here it's

[13:02] already done run one and run two. Did these two inside of the thread just so we could see how they go. Now everything else is just occurring autonomously. 10

[13:10] diagrams every 2 minutes evaluating via cloud sonnet vision mutating the prompt and then just keeping the winner. So we can apply this to any skill we have. I can apply this to my proposal generator.

[13:20] I could apply this to auto research itself. I could apply this to my agent review. I could apply this to my model chat. And you know, I will I'm going to

[13:27] create a meta skill that goes through and then performs a sort of optimization for literally every skill in my repo just to get it as close as I can to perfect. And you can see that it's actually taking my advice on the second run, okay, as it's written here. Um, none of these letters or words or anything like that are illeible. There

[13:43] are no problems. It just finished up another one, by the way. Um, it's linear, so it's left to right. It's

[13:47] experimenting with a few different styles here, but it does have those nice pastel colors, like those cute icons, and then ultimately those randed borders, which I like. And it's just getting better and better and better. This is probably one of the ones that failed. It didn't spell authorization

[13:59] right. Eventually, the runs get so good that it's in this sort of handdrawn pastel uh uh style, which is more or less exactly what I want. And, you know, we eventually hit 39 out of 40 on this experiment, which I think is pretty good. You know, for me to get 39 out of

[14:13] 40, sort of like equivalent to me getting 97.5% on a test. I'm fine with 97.5%. Some quick tips on the eval. Um,

[14:20] you know, yes or no is the simplest way to pitch it. Does this diagram contain X, Y, and Z? Only two possible answers there. You can try implementing some

[14:29] sort of scoring or scaling like a liyker scale. You know, evaluate this out of seven for X, Y, and Z. In my experience, not so good. Just because you're

[14:38] compounding probabilities here. The more variability you give the model at every step along the chain, the more like variable it gets in total. Imagine like a little cone, right? It starts over

[14:47] here really really narrow but then the more variability the more we compound out until eventually my my my answer you know my out of 40 could be at 39 out of 40 or it could be a 2 out of 40. So um yeah go binary wherever possible. Also don't go so concrete and so like narrow that the model starts optimizing for silly things like I've seen a lot of people say stuff like hey make sure this is under x words. Make sure this doesn't

[15:12] include these symbols or these characters. That's pretty that's pretty stringent I would say. And um you know if you give the model way too many of these evals what it'll eventually do is it'll just like find a way to parrot every single one of the evaluation points back to you. So even if the

[15:26] actual quality of the thing is not very good it'll technically say passes the test and it's good to go. That's sort of like a student who you know doesn't really understand the material but then still gets 100% on the test. And that's that. I'm going to give you guys access

[15:37] to this down below. No email, no gatekeeping whatsoever. Feel free to take this and then use this for your own skills. and I'm going to get to

[15:44] employing this on the rest of my own. Hopefully you guys learned how to optimize your own skills using auto research. As mentioned, there are a million things that you can apply auto research to. It's not just your skills,

[15:55] nor is it just your prompts. You can use auto research for your websites, for your landing pages, for split testing titles, thumbnails, emails, literally whatever the heck you want. I'm sure a lot of people in the ecosystem are figuring out better and uh uh more powerful ways to do so over time. If you

[16:09] guys like this sort of thing, but maybe we're a little bit lost in the actual Claude portions, definitely check out my full 4hour Claude Code course below. I cover everything, including skills, but also how the interface works from start to finish. Aside from that, leave me a comment down below with whatever you'd like to see in the next video. I read

[16:27] every one, and I'll catch all y'all in the next. Thank you very much for your time.
