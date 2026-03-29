# Claude Code + Playwright = INSANE Browser Automations

**Channel**: Chase AI
**Duration**: 13:49
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=I9kO6-yPkfM
**Transcribed**: 2026-03-28 03:49

---

## Organized Notes

**Why CLI Over MCP and Claude in Chrome**

- The **Playwright CLI** is the most token-efficient way to do browser automation in Claude Code — by far
- **Three browser automation options** exist: Playwright MCP server, Claude in Chrome extension, and Playwright CLI
- The **MCP server** dumps the entire **accessibility tree** into Claude Code's context on every interaction — massive token cost
- **Claude in Chrome** takes **screenshots** of web pages to understand them — even more expensive than MCP, can't run headless, and parallel execution is possible but significantly constrained and fragile compared to CLI
- The **CLI** saves the accessibility tree to **disk** and only passes a **summary** to Claude Code — dramatically lower token usage
- Creator **Chase AI** (Chase Lean) cites a Playwright comparison showing **~87,000 token difference** between MCP and CLI for the same task (Playwright's published benchmarks: ~114K tokens MCP vs ~27K tokens CLI — presenter rounded to "about 90,000")

| Feature | Playwright CLI | Playwright MCP | Claude in Chrome |
|---------|---------------|----------------|-----------------|
| Token usage | Lowest (~27K) | High (~114K) | Highest (screenshots) |
| Headless support | Yes | Yes | No |
| Parallel execution | Yes | Yes | Limited (fragile) |

**How Playwright Actually Works — The Accessibility Tree**

- Playwright uses the **accessibility tree** — the same structure that enables blind users to navigate websites
- The accessibility tree maps every element on a page in a machine-readable way
- MCP approach: dumps the **entire tree** into Claude Code's context (token-heavy)
- CLI approach: saves tree to **disk** as a YAML file, sends only a **file path reference** to Claude Code (token-efficient)
- This architectural difference is why the CLI is fundamentally more efficient

**Installation — Three Steps**

1. Install the Playwright CLI: `npm install -g @playwright/cli` (auto-captions garbled the package name — this is the correct npm package per official docs)
2. Install the browser engine: `npx playwright install chromium`
3. Install the Claude Code skill: `playwright-cli install --skills`
- Alternative: open Claude Code, paste the **GitHub repo link**, and say "install everything I need"
- The skill Microsoft created is a **starting point** — you can edit it, audit it with `/skill-creator`, customize it

**UI Testing Workflow with Parallel Agents**

- The demo shows **three parallel sub-agents** each running Playwright CLI to test a form submission simultaneously
- Each agent attacks the form from a **different angle**: edge cases, validation, and happy path
- Without this: you'd manually spin up the dev server, manually fill forms, manually test each scenario
- With this: **plain language instructions** to Claude Code, which executes everything via the Playwright skill
- By default, Playwright runs **headless** (invisible browser) — you must explicitly request **headed** mode to see the browser
- After testing, Claude Code provides **test results** and **screenshots** automatically

**Packaging Workflows Into Skills**

- The key insight: if you're running the same browser test repeatedly (e.g., after every form change), **turn it into a skill**
- Workflow: articulate the exact process → use **skill creator** → paste the workflow → get a reusable skill
- Example: Chase turned his "three parallel agents testing form submission" workflow into a **"form tester" skill**
- Now instead of describing the full workflow each time, just say "use the form tester skill"
- Using skill creator also enables **evals** — you can test whether the skill is actually improving

*Quotable Quotes (Chase AI / Chase Lean):*

> "The amount of things that the Playwright CLI can actually do is pretty broad. It's an extremely powerful tool. I highly suggest one of the first things you do is just have an interaction with Claude Code asking it what can you do with the Playwright CLI skill." [08:13]

> "The simplicity of use is really the value add here. You literally just talk plain language to Claude Code and it does all of it." [10:48]

> "What you need to be thinking about is how can I then turn that entire workflow into a skill? Instead of having to describe the process every time, I can just say 'Go execute that skill.'" [11:28]

**Use Cases Beyond UI Testing**

- Browser automation extends to **any browser interaction**: shopping, logging in, setting up persistent sessions with cookies
- Claude Code **abstracts the complexity** — you don't need deep Playwright knowledge to get value
- The presenter recommends starting by asking Claude Code "what can you do with the Playwright CLI skill?" to explore capabilities

---

## What This Means for Your Work

This video directly validates a tool you already use — Playwright CLI is already your preferred browser automation method (per CLAUDE.md: "Use Playwright CLI for browser automation, not Claude in Chrome"). The 90,000-token savings over MCP and the inability of Claude in Chrome to run headless or in parallel are concrete data points that justify that preference. What's new here is the **workflow-to-skill packaging pattern** and the **parallel sub-agent testing model**.

**e-Bangsamoro (4-portal platform)**: The parallel agent testing pattern is immediately applicable. Your 4-portal architecture (Parliamentary, Ministerial, Budget, Citizen) means form submissions, role-based access checks, and multi-tenant data isolation all need testing. Instead of manually verifying each portal's forms after changes, you could dispatch 3-4 parallel Playwright agents — one per portal — testing simultaneously. This compounds with your frontend-first development approach: build the UI, then immediately validate it with automated browser tests before touching the backend.

**MoroMarket / e-Negosyo**: The marketplace has cooperative storefronts, product listings, and transaction flows that are prime candidates for Playwright testing. A "marketplace tester" skill could validate the buyer flow, seller dashboard, and admin panel in parallel after each deployment.

**Solo dev force multiplication**: You're one person building 9+ platforms. The key insight from this video isn't "Playwright is useful" — you already know that. It's that **every repeated browser interaction should become a skill**. If you find yourself manually checking that the BangsamoroHR login flow works, or that the Tarbiyyah-MS student registration form validates correctly, those should be packaged skills that run with a single command.

### How This Can Improve Your Claude Skills and Workflows

**[[webapp-testing]] skill enhancement**: Your existing /webapp-testing skill already uses Playwright, but this video suggests a specific improvement: add a **parallel agent dispatch pattern** as a default mode. Instead of testing one flow at a time, the skill could automatically spawn sub-agents for happy path, validation errors, and edge cases. The accessibility tree summary approach (CLI saves to disk, sends summary) is worth documenting in the skill's references so you understand why CLI is preferred.

**New skill opportunity — project-specific test suites**: The video's "form tester" pattern maps directly to creating **per-project Playwright test skills**. You don't have project-specific test runner skills yet. A `/e-bangsamoro-test` skill that knows the 4 portals, their form structures, and their expected behaviors would be more effective than generic /webapp-testing for that project. Same for `/moromarket-test`.

**[[tdd]] and [[build]] skill integration**: The Playwright parallel testing pattern could feed into your /tdd and /build skills. After the red-green-refactor cycle completes, automatically trigger a Playwright browser validation as a final verification step — especially for UI-facing changes. This creates a **code tests + browser tests** double-check pattern.

**[[skill-optimizer]] application**: The video explicitly mentions using the skill creator to enable evals on Playwright test skills. This maps to your /skill-optimizer workflow — once you create a Playwright test skill, run the auto-research loop to optimize its test coverage, execution speed, and reliability.

**Parallel agent workflow refinement**: You already use parallel agents extensively. This video adds a specific pattern: **fan-out browser testing** where each agent gets a different test angle (edge cases, validation, happy path). Your [[sp-dispatching-parallel-agents]] superpowers skill could incorporate this as a documented pattern for Playwright-specific parallel dispatch.

---

## Transcript

[00:00] Okay, Claude Code, I want you to spin up three parallel sub aents. I want you to use the playwright CLI skill for each of them and I want you to test my form submission inside of my website since we just made some changes. Go. So, what

[00:13] you're seeing happen right now is Claude Code just spawned three sub agents. All of them are using the Playright CLI. Playright is a tool from Microsoft, totally open source, that does browser automation. And this is a huge unlock

[00:28] for claude code because browser automation despite the fact that we have claude in Chrome as an extension is a place that cloud code really struggles. And what you see here is one of the great use cases for browser automation. The idea that I can use it for UI testing. And so what we did in this

[00:45] example is I have my website. I made some adjustments to the form submission. That's what you see right here in the middle. And I'm now having Claude code

[00:52] test it from a number of different angles. Right? We're looking at edge cases, edge cases, validation, and also the happy path. And think about what

[00:59] this would look like normally. You would spin up the dev server on your own. You would manually go through it and you would manually test it, right? Hey, does

[01:05] it work when I put in a name, an email, whatever. But now I can test it from again a number of different angles simultaneously. And via the Playright CLI, we are doing this more effectively, more efficiently, and easier than really any other browser automation path. And again, I'm not

[01:24] touching anything. Cloud code via the playright skill is doing all of this. And the use cases and potential upsides of knowing how to do something like this inside of Claude Code is frankly wild.

[01:36] Anything that requires you to interact with a browser is a place where we can use this. So in this video, I'm going to show you how the Playright CLI works, how to install it, best practices, and most importantly, how to get the most out of it inside of the Clawed Code ecosystem. This is going to be a huge productivity upgrade for you. So, let's

[01:54] get started. But before we dive into Playright, first a message from our sponsor, me. So, I just released a Claude code masterass inside of Chase AI plus and I take you from zero to AI dev, no matter your technical background or lack thereof, in a practical manner. So,

[02:10] if you're looking to get way better at cloud code, definitely check it out. There's a link to it in the pin comments. Also, I have the free Chase AI community that is in the description.

[02:20] Tons of free resources. So if you're just looking for more stuff, definitely take a look. Now back to Playright. What

[02:25] is Playright? Well, it's a framework for web testing and automation. It is a Microsoft product, but Microsoft was nice enough to open source this so we can use this for free. And what

[02:35] Playright allows us to do is interact with our browsers programmatically, right? Exactly what you saw in the demo. That is the power of Playright. But

[02:42] hasn't play been around for a while? Isn't there a Playright MCP server? Why are we talking about Playright CLI? And

[02:48] again, doesn't Claude already have something like this? Why are we talking about this tool in particular? Well, the Playright CLI command line interface is actually a relatively new addition to the Playright Arsenal. This just came

[03:00] out a few weeks ago. Prior to that, we were in MCP land, and over the last month or so, you've probably seen Claude in Chrome extension. Let's talk about why the CLI is so much better than these other two, and why this is such an important video. Now, while all three of

[03:16] these can interact with your browser in a programmatic way, only one of them does it in an efficient way, and that's the CLI. Now, why is that? Dropping down to the bottom, it's because it has the lowest token usage by far. MCP is a

[03:29] token hog. In fact, there's a video that came out from Playright themselves comparing the MCP to the CLI, and it was a difference of about 90,000 tokens for the same task. And we'll go into the why in a little bit. Now, the clawed code in

[03:44] Chrome extension that you've probably seen all over the place is also extremely tokenheavy. Why is that? Because claude in Chrome, the way it works is it takes screenshots of your web page. So, you know, when we're

[03:57] looking at that in here with my web page, it would actually take screenshots to figure out what's going on and then interact with it. That is very costly. Screenshots take up tons of tokens. And

[04:08] in fact, out of all these, the claw code extension is probably the worst because it is not headless and we cannot do it in parallel. What do I mean by that? What does headless mean? Well, headless

[04:17] or headless browsers means that Playright can operate a browser without it actually being open. So, you remember the demo how I had the website up. So, this is headed. This is a headed

[04:28] browser, meaning it's actually there. I can interact with it. Headless means it's working on the browser, but it's in the background. I can't see it. It's

[04:34] sort of invisible. We like the headless browsers because it's less of a drag on our machine. It's more efficient. I

[04:39] don't have 10 million things popping up on my desktop. So the MCP can do headless as well, but so can the CLI. The other thing is, can we do this in parallel? Again, back to the demo. We

[04:48] had three CLI sub aents running tests. That's great. Can I do that with the cloud code in Chrome browser? Not

[04:57] really, right? It's only going to be able to do it one tab at a time, and it's slow and expensive. The MCP can do this, and the CLI can do this. Now

[05:04] looking at this chart, it should be pretty obvious why we're focused on the CLI then, right? I can do everything the MCP playright server can do and more at a significantly lower token usage. So that's the why in terms of the tool.

[05:18] Now, in case you're wondering why there is such a massive token difference between the CLI and the MCP, kind of an interesting discussion. I won't belver it. But the way Playright actually works, interesting enough, is it uses what's called an accessibility tree. So

[05:34] whenever you go on a website, there is what is called an accessibility tree and and it's essentially mapping this entire website in a way that someone who couldn't see it could use it. Like imagine if you were blind, how would you interact with this website? Well, people figured that out cuz guess what? Blind

[05:51] people need to use websites, too. That entire structure behind helping blind people use websites, the accessibility tree is the technology behind it. That's what Playright actually uses to work, right? Kind of cool. But the Playright

[06:06] MCP server, the way the MCP server works is it will take the entire accessibility tree and shove it into clawed code. And the accessibility tree is actually relatively large, right? And so every time it shoves the accessibility tree into clawed code, it's a massive token dump. The CLI is a little bit different

[06:26] because while it still gets that accessibility tree, right, of all this information, it doesn't dump all of it into clawed code. Instead, what it does is it takes that tree, right? Here's our accessibility tree, and it just saves it onto our computer, right? On our disc.

[06:44] This is a computer. I know you're here for my great graphics. So the CLI gets the same tree, saves it to the disk, and all it does is it gives then a summary of the tree to clawed code. So it

[06:55] doesn't give it all the information. It instead just gives it the information that it needs. This is a way lower token cost. So that's why it's working in case

[07:03] you were wondering. So how do we get this installed and working with clawed code? Actually very simple and easy.

[07:08] There's three things we're going to need. One, we need to install the Playright CLI. Two, we need to install the browser engine. And then three, we

[07:16] need to set up the claude code skill for playright. So it knows how to actually use this. And so I'll give you the commands, but understand you can also just open up claude code, give it that GitHub repo, which I will link down below and say, "Hey, install everything I need, right? But I'll show you the

[07:31] manual steps to install the CLI. It will be npm install-gplay CLI." Next, for the browser engine, npx playright install Chromium. Again, using

[07:40] a different browser engine, just reference the documentation or have Claude Code tell you the command. And then lastly, once you have the CLI installed, to install the skill, you'll do playright-cli install--sklls. Now, remember, hey, reference the skills creator video I did the other day. This

[07:54] is the skill that Microsoft came up with. And we can see the actual skill right here inside of the GitHub. You are not beholdened to this. This will work

[08:03] just fine, but also know you can create it, edit it, use the skill creator to audit it, right? It's a living, breathing document. And once you do that, just spin up cloud code and we're ready to actually work. Now, the amount

[08:13] of things that the Playright CLI can actually do is pretty broad. It's an extremely powerful tool. So, I highly suggest one of the first things you do is just have an interaction with Claude Code asking it what can you do with the Playright CLI skill and kind of going through some theoretical test cases that you think it can actually accomplish because ultimately your use cases will vary. What we're going to focus on here

[08:36] today is essentially what we saw in the demo, which is like this UI design type workflow or UI testing type workflow, which I think is something that's very common. But again, you could have this thing go like shop on Amazon for you, right? Like it has the ability to actually like log in and set up persistent sessions and sort of have like its own cookies type of deal. It

[08:55] again the waters here are very deep and we're just touching the surface, but again, clawed code is your number one friend in understanding its capabilities. But in terms of actual execution like with our UI testing again we're using cloud code cloud code uses the skill to execute the playright CLI on our behalf which means we just have to use plain language with what we want to do. Now some things to note right even though in the demo you saw all those tabs pop up by default it is going to be headless which means when I tell it hey go do this testing for me you're not going to see that browser at all. So

[09:30] you need to be specific and you know actually say hey I want it to be a headed browser I want to see it or else you won't. But for our test we'll just ask it again to do just a single headed browser test to test our form submission so we can again see it in action. So alls I said was can you use the playright CLI tool to test the form submission again make it a single agent and make it headed so I can see it. So

[09:52] we see it loaded the tool. You see it's calling the skill and now it's going to check the project and figure out what it actually wants to do. The other thing that's great for this, especially when we're doing it, you know, on our own sort of project, like it has full visibility into how our pages are look, how they look and how they set up. So, a

[10:10] much lower chance of dealing with some sort of like accessibility tree issues. It knows exactly how this page is set up. So, these sort of tests are even more effective. And so, it's opened the

[10:18] page, it's scrolled down, it's starting to fill out the form, it's starting to check boxes, and it's really that simple. And once it finishes its work, it will automatically close the browser, give you the form submission test results, and then even give you screenshots. And to up the antie and to do exactly what we did in the demo and say, "Hey, I want to run three parallel agents and I want to attack it from different angles." That's all you have

[10:38] to add to it. This is like a two sentence thing and it's going to do all of your UI testing for you. Furthermore, you can ask cloud code for the best practices, right? I didn't know the best

[10:48] way to, you know, stress test this form, but it did. So, you just kind of say like, "Hey, what what do you think is the best way to test this?" And the simplicity of use is really the value ad here. Like you literally just talk plain

[10:58] language to cloud code and it does all of it. However, if you actually want to supercharge this process, you need to learn how to package this sort of workflow into a skill itself. Now, what do I mean by that? You just saw me use

[11:13] the Playright CLI with plain language. Like, hey, run three parallel headed browser tests. That's exactly what you see here, right? Because I want to do

[11:20] three sub agents. They're going to test the UI, blah blah blah blah blah. Do I want to say this each and every time? Of

[11:28] course I don't. Yet, am I going to probably run this test on my local dev server to check the form every single time I make changes? I might be doing a ton of changes, right? I might need to

[11:37] run this test over and over and over. So, what you need to be thinking about is like again, how can I then turn that entire workflow into a skill? That's what we can do here, right? this entire

[11:46] process, this like triple agent thing you saw in the demo, we can turn that into a skill and instead of having to describe the process every time, I can just say, "Hey, go do the playright CLI UI test skill. Go execute that skill." And it goes and does that. And that's

[12:02] really easy to do actually. First, obviously, you need to articulate the actual workflow that you've done. That's what I've done here, right? Three

[12:09] parallel agents. I want you to do X, Y, and Z. like I've really nailed down like it can't mess it up at this point. And

[12:15] again, have Cloud Code spell that out for you. Next, I'm going to use the brand new skill creator tool. Check out that video I just did a few days ago, but we'll just do skill creator. And

[12:24] what are we going to say? We're going to say I want to turn this process, this workflow process into a skill. Right?

[12:29] So, I just said I want to turn this following workflow process into its own meta skill and pasted the entire workflow. So, it went ahead and created the form tester skill. So now I can just say use the form tester skill and three parallel agents will spawn just like in the demo. And because I used it via the

[12:44] skill creator, I now have the option to run tests and emails and see if this is an actual improvement, which is great. And I think this is the sort of headsp space you should be in with this stuff whenever you're doing workflows inside of cloud code, right? Can we standardize it? And if it's standardized, can we

[13:00] turn that standard flow into a skill? Right? And it just makes it super easy.

[13:05] So, like I alluded to at the beginning, the waters are deep when it comes to Playright. But with that complexity, under this surface comes a huge swath of use cases. And luckily for us, claude code allows us to like bridge that gap, right? We don't have to be crazy

[13:21] technical and in the weeds to really get a lot out of this because cloud code abstracts so much of it away. So, this is actually where I'm going to leave you guys today. I hope this was a cool intro for playright and what it could do for you. I think if nothing else, just with

[13:35] sort of, you know, the website checks, like that's a huge value ad. I know it is and has been for me. So, let me know in the comments what you thought. Make

[13:43] sure to check out Chase AI Plus if you're looking for the Claude Code Master Class and I'll see you
