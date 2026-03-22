# Claude Code Just Got a MASSIVE Upgrade (Agent Loops)

**Channel**: Chase AI
**Duration**: 10:19
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=lf2lcE4YwgI
**Transcribed**: 2026-03-23 00:21

---

## Organized Notes

**What Agent Loops Actually Are**

- `/loop` command -- runs **recurring scheduled tasks within a session**
- Syntax: `/loop <interval> <prompt>` (e.g., `/loop 5m check deployment status`)
- Default interval: **10 minutes**, max duration: **3 days**
- Runs **in the same terminal session** -- all output appears in the current window

**Limitations (What It's NOT)**

- **NOT a 24/7 agent** -- dies if you close the terminal, shut down, or computer sleeps
- **NOT persistent** -- doesn't survive restart
- **Session-based** -- if you're mid-conversation, the loop waits until Claude finishes
- **3-day max** -- auto-expires, must be re-created
- Lots of misinformation calling it "Claude 2.0" or a persistent background agent -- **pump the brakes**

**Good Use Cases for /loop (CLI)**

- **Short-term recurring tasks** during a work session:
  - Every 10 min: check deployment status
  - Every 5 min: run Playwright to verify form submission
  - Babysit PRs, autofix build issues, use worktree agents to fix comments
- Think of it as a **"skill of skills"** -- automate repetitive Claude Code tasks

**Claude Code Desktop: More Powerful for Scheduling**

- Has `/schedule` command (CLI does **not** have this)
- **No 3-day expiry** -- runs in perpetuity
- **Survives restart** -- task persists even if you close Desktop
- Creates a **new session** for each scheduled run (won't interrupt your work)
- Requires Desktop to be **open** and computer to be **on**
- Better for **long-range recurring tasks** (e.g., daily morning report via Slack MCP)
- Caveat: running every minute = **60 sessions in an hour** (resource heavy)

**GitHub Actions**

- Claude Code runs on **GitHub's infrastructure** -- no local computer needed
- Scoped to **GitHub tasks only** (PRs, code implementation, CI)
- **Not suitable** for general-purpose "talk to Claude via Telegram" use cases

**Claude Code Remote**

- Allows remote access to a Claude Code session
- Still **session-based** -- dies when terminal/computer closes
- Not a persistent solution either

**When to Use What**

| Tool | Best For | Limitation |
|------|----------|------------|
| **`/loop` (CLI)** | Short-term recurring tasks in a work session | 3-day max, session-based |
| **`/schedule` (Desktop)** | Long-range daily/weekly tasks | Needs Desktop open, computer on |
| **GitHub Actions** | CI/CD, PR automation | GitHub-scoped only |
| **Remote** | Access session from another device | Session-based, not persistent |

---

## Transcript

[00:00] So, less than 24 hours ago, Enthropic released agent loops, which is a huge unlock with how we handled scheduled tasks inside of Cloud Code. Yet, and I guess I shouldn't be surprised, there is already so much misinformation about what this new feature can actually do. I've already seen videos with people calling it Claude 2.0. It's a 247 agent.

[00:22] I saw one person saying, "Hey, here's how you can set it up so you talk to Cloud Code via Telegram." No. No. This

[00:29] is not the case. Agent loops is a very useful feature. But if you come into this thinking it is some sort of paradigm shifting moment for clawed code or that we can now have like persistent sessions of clawed code that are just like running in the background forever doing scheduled tasks, you're going to be very disappointed, which is a shame because this is a useful feature. But I

[00:50] don't blame them for all the misinformation because the fact is cloud code and schedule tasks is actually a very confusing space in part because we have two versions of cloud code we're talking about right we have cloud code desktop and we have cloud code and they handled scheduled tasks differently and in fact did you know that cloud code desktop actually gives us more power when it comes to schedule tasks? Yeah, bet you didn't know that especially if you're someone who's more terminal forward. Also what about GitHub actions?

[01:16] I mean cloud code can kind of run in the cloud all the time with that right and what about cloud code remote where's that plan so this is actually kind of murky waters and the loops feature while awesome does have some limitations that you need to be aware of or again you're going to be disappointed with the hype that's already coming about this feature. So, in this video, I'm going to break it all down for you so you understand what you're actually getting because this is a value ad, but it's important to know what to use when, what's going on with Cloud Desktop, and just like getting some sort of light shined on this space. So, excited to help you guys do that. So, let's get

[01:51] started. So, Agent Loops, like I said before, just came out yesterday in the latest update. If you don't see a forward/loop command inside of your cloud code instance, you just need to upgrade. And what has it given us the

[02:02] ability to do? Well, it allows us to do recurring scheduled tasks within a session. Within a session being the important word here. Now, this post by

[02:13] Boris Churnney, the actual creator of Claude Code, gives us some insight on some of the use cases. For example, /loop babysit all my PRs, autofix build issues, and when comments come in, use a work tree agent to fix them. Simple enough. By default, it will run every 10

[02:27] minutes. or hey every morning use the Slack MCP to give me a summary of the top post I was tagged in of note. You can do this for up to three days at a time. Now when you read this you think

[02:38] naturally that oh I just open up cloud code right I have my terminal open and I could do something like hey / loop every morning do a web report on cloud code changes and I will get a web report but it's only kind of like that right because it is session based remember I said how this was session based that means this will only occur every morning if I have this exact session this exact terminal window up if I close this terminal window it ends if I shut down my computer it ends if my computer goes to sleep it ends and it's max at 3 days. This is a huge limitation and it's why we need to understand like what's going on here and what our limitations are and why when people say this is a 24/7 agent, it's cloud 2.0 like pump the brakes [laughter] for a second. Like

[03:20] this is great in specific instances. So first of all, what are our limitations? What are our right and left lateral limits? Well, first of all, it expires

[03:27] every 3 days. So if I tell cloud code, hey, I want that report every morning, it's going to do it. But after 3 days, it shuts off automatically. Does it

[03:35] survive restart? No. Do we need the app open all the time? Yes. Does the

[03:40] computer need to be on? Yes. Does it run in the same session? Also yes. So just

[03:45] like in this session and this will make more sense later when it runs this morning report I will see the output in this exact same terminal window. So it runs in the current and what happens if I'm working on something. So let's say I'm actually talking to cloud code in the terminal. We're having some back and

[03:59] forth. If I said hey the report's supposed to come out in the next 5 minutes and we're in the middle of something. Well, you just have to pause for a second. Like, it's not going to

[04:06] stop its work to give it to you. I'll give it to you when it's done. And so, when we take that into account, what does that mean? What can the sloop

[04:12] command actually buy us? Well, what it buys us is the ability to do again almost like these micro tasks that we constantly are going to be repeating during a singular work session. And I would call a singular work session something that's like 3 days long in the same terminal. So imagine again the

[04:28] example that every 10 minutes I want you to check the deployment status of our website and make sure it's still up or every 5 minutes I want you to run playright and check to make sure the form submission still works. So this is really powerful right this is almost you can turn loop into almost like a skill or a skill of skills. So anything that you are constantly doing inside of cloud code we can now systematically do it via the loop. Right? Great stuff.

[04:55] productivity increase for sure, but these limitations are real and we need to understand them. And again, using this is as simple as doing forward slashloop. You give it the interval. So

[05:04] this could be 5 minutes, this could be an hour, this could be a morning, right? You could you have a lot of wiggle room here. And then just a prompt what you want it to do. But what about clawed

[05:12] code desktop? I said in the intro this is actually more powerful when it comes to scheduled tasks. And for all the craziness about what loops are doing, we've actually been able to do this for a little bit inside of the cloud code desktop. However, again, there are some

[05:26] limitations. So, if I go into the cloud code desktop and I head over here and I go to scheduled, I can schedule task. I can also just use the forward/chedu option. Again, inside the terminal,

[05:37] there is no forward/schedule option. This does not exist. And all I have to do is hit new task and I can just like I would with loop set up a recurring action. But again, this is actually a

[05:48] little more powerful. Why is that? Well, first of all, it's never going to expire, right? It's not on a three-day

[05:54] time limit. This will run in perpetuity. Secondly, it is not session based. So,

[05:58] it survives the restart. So, when I create something, you know, some sort of scheduled task using cloud code desktop, I can shut down desktop, right? That task doesn't disappear. Now,

[06:09] claude code desktop needs to be open for it to do the schedule task. So if I have a task that runs every hour, some instance of claude code desktop needs to be open on my computer, but it will then create its own session to do that. What do what do I mean by that? So by

[06:25] creating a new session, it's almost like it opens a new terminal window, but inside of cloud code desktop, if that makes sense, which again is different than agent loops. Agent loops, all the stuff is contained in a single terminal. With cloud code desktop, it's going to create new sessions every time that scheduler runs. That is something to

[06:42] note though because if you want to run something every minute, well guess what? Over 60 minutes you would have opened up 60 se sessions. So we need the desktop open. You do need the computer on. So

[06:51] again if desktop's closed or the computer's off these won't run. So this 24/7 agent thing, right? Again, there are some things we need to worry about.

[06:59] Creates new sessions. And again, it since it's in a se separate session, it won't interrupt your work if you're having it do something on a schedule. So when we take all that into account, what does that mean for you? Especially when

[07:10] we compare the CLI over here on the left in the cloud code desktop. Well, that means agent loops are great for again like these are things I want to do in probably a certain time interval, but it's within a specific work section, right? I don't always need cloud code to check to see what my deployment status looks like every day forever. But maybe

[07:29] I do need to check that every hour for today for the specific project. If I'm trying to do something that is longer range in scope, every single day I want a morning report about something cloud code searches. Well, Claude Code Desktop is perfect for that, right? It is a

[07:44] shame that we don't have that scheduling power of desktop in the CLI, but I imagine that's something that will change over time. But hey, two different use cases, two different versions. Know which one fits your issue. But what

[07:58] about GitHub actions? And this is a little more advanced. GitHub actions are when cloud code executes tasks inside of GitHub in a GitHub action workflow, but your computer doesn't need to be on. You

[08:10] don't need a terminal app. You don't need Cloud Code Desktop, none of that. It actually runs on GitHub's infrastructure. And while the foundation

[08:17] of that sounds like something you could like be kind of hacky with and turn cloud code again to this persistent thing that runs no matter what your computer state is, understand GitHub actions is scoped for GitHub itself. So this makes sense in regards to dealing with PRs or code implementation, these sorts of things. This doesn't make sense in terms of I want to talk to cloud code via Telegram. And then that brings us

[08:39] into the idea of remote control. If you still want to talk to cloud code via telegram, why wouldn't we just use remote control, a native thing that's already built in? Again, limitations. We

[08:49] need to understand them. What's the limitation? It's session based, right?

[08:52] If I'm using cloud code remote on something in the terminal, it's just that session. If this closes down, if the computer shuts down, that's gone. And so, all that is to say that agent loops is great, but its scope is actually pretty small and it's going to be based upon your specific project and task. This example Boris gave is great,

[09:12] right? Babysit all my PRs, autofix build issues, and use a work tree agent to solve them, right? You might need to do this for a specific amount of time on a specific project. I would argue his

[09:20] second example of every morning use the Slack MCP for a summary. That actually makes no sense in the CLI, right? Why would we do that in the CLI when I'd have to repeat that same command every 3 days? Why would I do that in the

[09:32] desktop? This is totally a cloud desktop task. Claude code desktop. Again, don't

[09:38] get confused. there's 10 million different cla things. So that's the sort of nuance that you need to bring in when you're using cla code because the difference matters and if you want the most out of these tools, you need to know when to use what. So I hope I was

[09:53] able to shine some light on this loop feature. It's very easy to use /loop time interval. What do you want it to do? Just understand its limitations or

[10:01] you're going to be upset. So that's where I'm going to leave you guys. As always, make sure you check out Chase AI Plus for my Claude Code Masterass, right? That's in the pinned comment. I

[10:10] also have the free Chase AAI community with tons of free resources if you're just getting started. That is in the description. Let me know what you thought and I'll see you
