# Claude Dispatch Just Dropped, And It Kills OpenClaw

**Channel**: Nick Saraev
**Duration**: 15:56
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=NF10evwkefM
**Transcribed**: 2026-03-29 20:03

---

## Organized Notes

**Claude Dispatch Overview**

- **Anthropic shipped Claude Dispatch** -- a feature that lets you run and manage AI agents through your phone, controlling your desktop computer remotely
- **Nick Saraev** demonstrates how Dispatch connects your phone to Claude Cowork on your desktop, enabling you to fire off skills, run workflows, and receive results -- all from your mobile device
- Positioned as **significantly better than OpenClaw** from a security, cost, and usability perspective

**Live Demo: Multi-Task Agent Execution from Phone**

- **Lead scraping**: Typed "scrape 200 agency owners in California" on his phone -- instantly reflected on desktop, ran his lead scraper skill, returned phone numbers and contact data in minutes
- **Inbox cleaner**: Fired off an email cleaning workflow that marks spam as read and pre-drafts replies for important emails based on historical reply patterns -- saves **90% of inbox time**
- **Thumbnail generation**: Shared a YouTube thumbnail link from phone, asked Claude to recreate it with his face using his face-swapping skill -- generated multiple variants
- All **three tasks ran in parallel** as separate Dispatch conversations/sub-agents
- When a skill needs permissions not pre-granted, a **permission request pops up on the phone** -- approve from mobile without touching the computer

*Quotable Quotes:*

> "Simple systems like this essentially allow me to save two or three hours a day. And before I was constrained with doing all this stuff on my computer. I had to lug around my big fat laptop with me." [05:09]

**Why Dispatch Beats OpenClaw**

- **Security**: OpenClaw has had "tens of thousands of API keys leaked" and "very elementary security errors" hitting news headlines repeatedly -- "they had to change the name multiple times"
- **Cost**: OpenClaw uses **per-token API pricing** (Nick spent ~$100 in his first few days). Dispatch uses your **flat monthly subscription** which Anthropic subsidizes at **4-8x cheaper** than API pricing
- **Trust**: "If there's a company I trust to understand how to rein in the downsides of AI agent flexibility, it's the companies that have developed the best AI agents" -- Anthropic has spent **hundreds of millions on safety infrastructure**
- **Sandboxed and local**: Dispatch is sandbox-secured with allow-listing style permissions vs. OpenClaw's open architecture
- Dispatch is a **"stand-in replacement for 80-90% of all the features"** that OpenClaw provides

*Quotable Quotes:*

> "When I tried OpenClaw I spent like a hundred bucks or so in just my first few days and then I was like okay I'm going to turn this off." [08:27]

> "This is honestly a stand-in replacement for 80 to 90% of all the features that OpenClaw and other extraordinarily insecure implementations of autonomous decentralized agents provide for you." [15:14]

**How Dispatch Works Under the Hood**

- **Architecture**: Multi-layer system -- Claude Cowork is the base agent with access to skills library and MCP servers. Dispatch on phone communicates through layers with MCP servers, skills, back to Cowork. Cowork executes, then reports back up to Dispatch
- **Sub-agent model**: Dispatch spins up **new Cowork conversations as sub-agents** -- each skill execution opens a new tab prepended with "Dispatch:" (e.g., "Dispatch: Scrape HVAC Leads Texas")
- **Progress tracking**: Progress bar in the top-right corner of each Dispatch tab. Phone receives results only when task completes

**Setup Guide (5 Minutes)**

1. **Update or install Claude Desktop** from claude.com/download -- select your OS
2. **Install/update Claude mobile app** (iOS or Android)
3. Open Claude Desktop, navigate to **Cowork** section (Cmd+2 on Mac)
4. Find the **Dispatch** section -- click "Get Started"
5. Grant permissions: **keep computer awake** (critical), Chrome access, file access, all connectors on
6. On phone: open Claude app, scroll to **Dispatch**, click **"Pair with your desktop"**
7. Start sending tasks from your phone

**Porting Claude Code Skills to Cowork/Dispatch**

- If you have skills in Claude Code, you can **duplicate them to a Cloud/skills folder**
- Tell Cowork to "add them all to Cowork" -- it processes each skill and lets you click **"Copy to my skills"**
- Once copied, skills are accessible via Dispatch from your phone
- This bridges the gap between Claude Code (technical) and Cowork (accessible) -- **same intelligence, different interface**

*Quotable Quotes:*

> "Claude Cowork and Claude Code are basically the exact same thing. It's just like support for a wrapper that wraps around skills and then pre-established SOPs." [09:26]

---

## What This Means for Your Work

Nick's video is directly actionable for you because he demonstrates the exact workflow bridge you need: **porting Claude Code skills to Cowork for mobile Dispatch access**. You have 129+ skills in Claude Code that are currently desktop-only. Dispatch means you could fire off `/legal-researcher`, `/deep-research`, or `/youtube-transcriber` from your phone while commuting or in meetings.

**The security argument is the most important takeaway.** Nick's point about OpenClaw's API key leaks and per-token costs validates your choice to stay on Claude's ecosystem. Your Claude Max subscription already subsidizes the compute. OpenClaw's per-token model would be prohibitively expensive for the volume of work you do (legal research, guidebook generation, transcript processing).

**Key actions:**

1. **Port your most-used skills to Cowork**: Nick shows a simple process -- duplicate skill files to a Cowork-accessible folder and add them. Start with: `/youtube-transcriber`, `/legal-researcher`, `/deep-research`, `/fact-checker`, `/session-summary`
2. **Keep your Mac awake for Dispatch**: Enable the "keep computer awake" setting so Dispatch tasks don't fail when you're away
3. **Use Dispatch for mobile-initiated research**: When you spot a YouTube video, policy document, or email with attachments while on your phone, fire off the appropriate skill immediately instead of bookmarking it for later

**The sub-agent architecture maps to your existing setup.** You already use parallel agents in Claude Code. Dispatch creates parallel Cowork conversations the same way -- each skill execution is an independent sub-agent. This means you could fire off multiple research tasks from your phone simultaneously.

### How This Can Improve Your Claude Skills and Workflows

**Skill portability between Code and Cowork.** Nick demonstrates copying skills from Claude Code to Cowork. Your 129-skill library in `~/.claude/skills/` and `~/apps/skills-bucket/` is already structured for portability (that's why you mirror to skills-bucket). The next step: identify which skills work in Cowork's environment (which uses Cowork's MCP servers rather than Code's Bash/Edit/Read tools). Skills that are primarily prompt-based (like `/bangsamoro`, `/humanizer`, `/content-research-writer`) should port directly. Skills that depend on file system operations (`/legal-researcher`, `/fact-checker`) may need adaptation.

**New skill opportunity: `/dispatch-quick-tasks`**. A meta-skill designed specifically for Dispatch -- it would bundle common phone-initiated tasks: "transcribe this video URL", "research this topic", "draft a response to this email", "summarize this PDF". Checking your index, you don't have a mobile-optimized meta-skill.

**Project-specific applications:**
- **Transcriptions repo**: Spot a video on your phone, fire off `/youtube-transcriber` via Dispatch, come home to a completed transcript with organized notes
- **MoroTech/MoroMarket**: Monitor marketplace metrics and content performance from your phone using Dispatch + analytics skills
- **Legal research**: When an MP or colleague sends a legislative question via chat, immediately route it to `/legal-researcher` via Dispatch instead of noting it for later

---

## Transcript

[00:00] Anthropic just shipped a feature called Claude Dispatch which lets you essentially run and manage an AI agent through your phone. In this video, I'm going to show you guys how you can use it, why it's significantly better, and probably more preferable from a security perspective than a lot of the pre-existing solutions like OpenClaw at all, and then how to set it up on your end so you guys can run everything that you need from the convenience of your device. So, as some of you guys will know, I'm a big fan of using Claude Code to do a lot of economic knowledge work for me. This

[00:25] video is not trying to say that Cowork is better than Claude Code, but it is a different and easier interface that a lot of less technical people can use to get up and running. So in Claude Code, I have a bunch of skills which are essentially tasks that I fire off one at a time. I say something like, "Hey, scrape me 100 HVAC leads in Texas." And

[00:42] this will actually go through and then literally contact the internet, run a bunch of scrapers, and then return them back to me totally autonomously. The issue is obviously using my phone with a setup like this is annoying. It's often pretty fragile and then it takes a fair amount of setup. So, Claude Cowork

[00:55] solves all this for us completely out of the box. Okay, so totally hands-off demo. I have Cowork set up with Claude Code Dispatch. It's right over here. And

[01:03] I just want to scrape 200 agency owners in California with a 1 to 10-ish size. You can see the second that I entered that in that was immediately reflected over here on my screen. And the reason why is because this is now running locally. Now, I don't know, I'm

[01:15] just on the go, right? I'm waiting for some train or something like that. And I say, "Hey, I could probably get a couple of phone calls in." So I launch it from

[01:22] here. Immediately after we see actually see a window open under Dispatch over here as a new tab and sort of our Claude Cowork ongoing conversations. So what it's doing now is it's actually running the skill. Okay, it's doing a

[01:33] bunch of the specific SOPs inside of the skill like generating search keywords, running a test scrape and so on and so forth. And then I'm going to see the results back here on my phone the second that it finishes. Okay, and then just a few minutes later I have all of them on my phone here. I don't know if you guys

[01:47] could see this but it's like data set leadsfinder. I have all the phone numbers. So, if I just wanted to, you know, click on one of these and maybe give them a ring, start doing some cold calling, I could. I just initiated

[01:57] and then completed that loop entirely from my phone, which is pretty sweet. But obviously now, that's not the only thing that I can do. I have this pretty cool inbox cleaner flow, which I like running. And what I'll do now

[02:05] is I'm just going to initiate that inbox cleaner again from my phone. So, I'll say run inbox cleaner. And then my hands are up here just so you guys could see.

[02:13] It's going to start a conversation. Go down to that tab there. And then just like it did before, it'll run my own skills on my computer using Claude Cowork. And just

[02:22] because I want to do multiple things simultaneously, I'm also going to have it run another skill. What I'm going to do is hypothetically, let's say I have found a YouTube thumbnail that I really like and I have a video that's coming up soon. So, you know, let me just make this a little bit bigger.

[02:35] Okay, there's this awesome one here from I don't know, "Don't Create an LLC." It's by Jasmine DiLucci. She's this person that creates content all about accounting and stuff like that. So, what I'm going to do is

[02:46] I'm just going to share this. I'll copy the link and then I'm also going to feed this directly into Claude Dispatch and I'm going to say, "Hey, recreate this thumbnail but with my face." Then I'm going to paste in the link. And now

[03:02] we should also pass the next message in queue. And what this is going to do is it'll launch an additional Dispatch conversation that will allow us to run multiple of these things. Okay. And

[03:13] then if you see here, we're running all three accounts in parallel, fetching, classifying, then marking read for each. Over here, we're actually reproducing a thumbnail using my thumbnail generation skill which has some face swapping functionality built in. And I'm going to get it all on my phone in just a few seconds. Now, in my case, I didn't

[03:30] realize, but one of these skills actually required a little piece of access from my computer that I hadn't given it ahead of time. And so, when that occurred, I just had a little window that popped up at the bottom of my Claude Dispatch, and it said, "Hey, you know, we're trying to reach XYZ. Do you want to allow this request?" So

[03:44] I'm the one that just instantiated the request. Obviously I'm allowing it. This sort of like security and then allow-listing style permissions is what makes this 10x more safe, secure and then scalable for business and then enterprise applications than something like OpenClaw. Okay. And then in this

[03:58] case it's now created a bunch of files. I don't think this is the best or most realistic look that I've ever had before but still not pretty bad. And you know we initiated this from my phone and it's not just available over there.

[04:10] It's also available over here. So, Dispatch is reporting back right now, letting it know that it just finished the thumbnail thing. And now it's asking me to allow it permissions to go and grab those thumbnails, which I will do in a second.

[04:22] And now it's actually showing them to me all on my phone. So, you know, I have them right over here, too, right? Can actually take a look at them. And then,

[04:28] okay, I guess I can't scroll through them, but I don't know. That's another one right over there. That's another one right over there. And so, I just

[04:33] generated all these from my phone. Basically through like an app, right? This app. But I didn't actually have to

[04:37] like whip up an app for it. I could just route this to my computer, which is pretty sweet. And then the inbox cleaner also finished. And in my case, basically

[04:43] what this does is it just automatically marks as read anything that I would consider to be some form of spam, some people soliciting me, that sort of thing. And then if there is any like important email or whatever, it goes through and then it pre-drafts a reply based off of a bunch of old replies that I've sent. And then it just allows me to QA and sort of human in the loop. So I

[05:01] then go through my inbox, but I basically save like 90% of my time. So that's pretty neat, right? Like it's done my personal Gmail, it's done a couple of other things. Simple

[05:09] systems like this essentially allow me to save two or three hours a day. And before I was constrained with doing all this stuff on my computer. I had to lug around my big fat laptop with me. But

[05:17] now, you know, I could set up my laptop or I could set up another computer or some sort of Mac Mini in the corner and then I could just like sort of port in, run whatever skills, run whatever workflows I need even while I'm over here. And then, you know, naturally I receive and then can send additional data follow-ups and everything like that from here while it's still super secure. So, in my mind, this has solved everything. I'm sure we're just a few

[05:36] stone's throws away from having this sort of stuff in Telegram. Let me show you guys how this all works under the hood. So, if it isn't clear, I think that most of these autonomous agent tools are pretty broken. And they're broken for a

[05:47] couple of reasons. The first is these OpenClaw and DIY agent stacks, which I think everybody and their mom is going to try and tell you is like the future and stuff like that. They are terrible from a security perspective. We've had

[05:58] tens of thousands of API keys leaked. Very elementary sort of security errors here have hit news headlines over and over and over again. It got so bad they had to change the name multiple times and stuff like that. And I mean like

[06:09] their core functionality is pretty cool, right? Which is that I get to text my model basically from my phone and then have it do economically valuable tasks for me. And the reason why beginners and people that aren't very tech-super into this sort of tech love it is because it's like hey I talk to my friend in Telegram and then immediately underneath I have my Claude bot in Telegram and that's awesome, right? It's just like

[06:27] good from a user experience perspective. But all of that isn't really worth risking, you know, your API keys, your credentials, your credit card numbers, your identity. Right? In addition to

[06:36] obviously massive security issues, there's also like a context explosion issue where you are paying for the most part using your API pricing instead of like a monthly recurring subscription, which Anthropic subsidizes heavily and tends to be somewhere between like 4 to 8x cheaper. What I mean by this is you are doing direct API calls to their backend and every single time you make an API call it bills you usage-wise. Like every message $0.50, every time a skill runs that's $2, every single moment that you're having a conversation with models on OpenClaw, whatever, unless they're running locally or running using something like Ollama, what you're really doing is you're just constantly like burning your money in the background. And then you know ultimately this pay-per-token plus the security problems in my view makes this like a non-starter if I'm using this in a serious business application. I'm basically never going to recommend something like OpenClaw or whatever. And so when this came out, you know, I made a bunch of videos talking about how horrific it was and all of the API keys that got leaked. And

[07:31] I was like, you know, I bet it'll just take a couple of months before Anthropic launches a native feature that does all this stuff. And that's what Claude Dispatch is. So with Claude Dispatch, you basically connect automatically to whatever your desktop is, your computer.

[07:42] So your skills, all of the pre-existing MCP connectors and all of your files. But it's also sandboxed and local. And I mean like if there's a company that I trust to understand how to rein in the downsides of AI agent flexibility it's the companies that have developed the best AI agents out there like Anthropic. They've spent

[08:02] hundreds of millions if not billions of dollars doing this exact thing. So I trust them to sandbox and make things pretty local. It's also a flat monthly charge because it's technically used as part of your subscription. Now they're talking about

[08:13] how they're going to make this available to Pro plans pretty quick. I think right now as of the time of this recording it's on Max plans but they're going to want to try and get everybody on it. And so what that means is instead of paying, you know, I don't know, it really depends on your usage and I don't want to pretend like I know exactly how much you're using. But when I tried

[08:27] OpenClaw I spent like a hundred bucks or so in just my first few days and then I was like okay I'm going to turn this off. Instead of spending that you'll probably just spend $20 to whatever the subscription amount is and it's going to be heavily subsidized. And then, you know, it says "same power" here, but I want you guys to know realistically speaking, you're probably going to get significantly more usage out of Cowork because out of Claude Dispatch because they're just going to like build in more and more and better functionality. This is a company that

[08:52] has access to basically all of the information on planet Earth at this point. I trust that they're going to do a much better job with this sort of infrastructure and architecture than some random third party. In terms of how Dispatch specifically works, it's sort of like a multi-layer system.

[09:05] Down at the bottom its brain is Claude Cowork and I usually make videos not on Cowork because that's the non-tech version of this intelligence and agent tech model. I make more videos on Claude Code, but Claude Cowork and Claude Code are basically the exact same thing. It's just like support for a wrapper that wraps around skills and then pre-established SOPs. So basically

[09:26] what happens is Claude Cowork which is your base sort of agent here has access to your skills library and a bunch of MCP servers to do things for you. Dispatch on your phone basically communicates through layers with your MCP servers, your skills, back to Claude Cowork. Cowork does something and then it kind of communicates back up the ladder to Dispatch. And that's what I was talking

[09:45] about with the fact that this is like an agentic thing. You're launching an agent. Those agents can launch sub agents and so on and so forth. All right. So, I'm going to

[09:52] show you guys how you guys could set up a Claude Dispatch in just 5 minutes. It's really easy. We're just going to update Claude Desktop or just reinstall.

[09:59] We're then going to update the Claude mobile app. If we see Dispatch in the sidebar, we're good to go. We can actually enable it and then turn all of this stuff on right now. If not, you

[10:07] know, we're just going to restart our computers until we see whatever the update logic is. This is literally -- it's probably not even going to take five full minutes. Let me show you guys how all this stuff works.

[10:15] In terms of how to set this up, this is a pretty new feature. It was launched sometime in the last 24 hours or so. And so many of you will not have this Dispatch tab added to your Claude Cowork. That's okay. If you don't

[10:28] already have this, what you need to do is you need to update the application. So just for all intents and purposes, in case you don't have Claude Desktop set up, it's as easy as heading to claude.com/download, then going from desktop over here, selecting your operating system, and then choosing either Mac OS, Windows, or Windows ARM 64. You'll also have to pair

[10:48] with the desktop app on your mobile. So, choose iOS or Android here. Once you're done on desktop, you'll have an interface that looks like this. Now, I

[10:57] should note that there's actually three different sections to Claude Desktop. There's Chat, Cowork, and Code. And for this feature, you're going to need Cowork, which you can also use hotkeys to bump to. In my case, Command+2. Now,

[11:08] once you're done, head down to this Dispatch feature, and it'll say something like "Coworking on the go." In order to get this started, it walks you through sort of the functionality, which is that your phone is like a walkie-talkie that can communicate with Claude on your computer. You just send Claude a message and it'll work on tasks locally using your computer. The one

[11:26] caveat to this is you do need to remember to keep your computer awake. This is a big thing that a lot of people were doing with OpenClaw. They would purchase specific computers like Mac Minis or whatever, plug them in, and just have them working 24/7. This is the

[11:39] exact same thing. You just have your computer where you want to do these tasks awake, and then Claude Dispatch can take care of the rest of it for you. Anyway, all you do is you click Get Started and then you have to pair with the Claude mobile app. So, I've

[11:52] already downloaded the Claude mobile app. All I'm going to do is open this puppy up. It looks like I'm already signed in to my phone. So, I have the

[11:58] Claude Desktop app open right over here. It has a chat window ready to talk to Sonnet 4.6.

[12:05] Next up, it'll ask, "Hey, can I give Claude access to your files?" So, it'll ask me when I click finish, should I keep this computer awake, which you're going to want to click yes to. Otherwise, Dispatch is going to run into some problems. Give it the ability

[12:17] to use Chrome. And then ensure that all connectors are on. Okay. Then just click

[12:22] Finish Setup. It'll ask to access files in your desktop and documents and so on and so forth. You're going to have to click this button a bunch of times. And

[12:29] now you have the ability to communicate with your phone and Claude. Now, on my phone's end, all I need to do is in my Claude app, scroll down to where it says Dispatch, click the button, and then I'll get something that looks like this. And as you can see, the UX and stuff like that is very similar to what we just did. So, all I need to do is click

[12:49] "Pair with your desktop," and then it'll connect automatically with the conversation that's in this window. So much so that my hands are off the computer now. All I'm going to do is type "hey." And I want you guys to see how

[13:01] this immediately pops up on my computer as well. And so I'm actually having a conversation with Claude Cowork through Dispatch right now. It's fully managed for me. And then I obviously

[13:10] have like a contiguous conversation history which is really sweet. And here's where I could start by I don't know running some skills. So I'll say "Run the lead scraper skill. Get me some

[13:20] leads for I don't know HVAC in Texas. Let's just do 100 to start." I'm now going to send it the message and it's going to go through the process of connecting to the skill which is in my Cowork instance. Finding all the

[13:34] session information and stuff like that and then actually launching it. And then I will have all of the information and everything I need popping up on my phone as well. And you can see when I actually kick off a skill execution, I create a new tab here that is prepended with the words "Dispatch." In this case,

[13:51] it's "Scrape HVAC Leads Texas." That actually opens this up. And then you can see the progress bar on the top right-hand corner. Just because this is a

[13:58] pre-established skill that I put together a while back. It'll go through the debugging and everything else it needs to and I'm not actually going to see a message back on my phone until this thing is done and it delivers the results. Essentially what it's doing is it's like spinning up new Cowork instances, new Cowork conversations almost as like sub agents, going, doing the task and then reporting back the results of said task to me. Also, hypothetically, if you were

[14:22] using something like Claude Code and you wanted this one-shot skill run functionality from your phone, a really simple and easy way to do it is you basically just get all your skills from whatever your IDE or your Claude Code instantiation is storing them. So, in my case, it's right over here. And then, in my case, I just duplicated them to this new folder, which is claude/skills. And

[14:40] then I just said, "Hey, I want you to add them all to Cowork." It then goes through, sends you a couple of brief little requests. Then after all this stuff is said and done, you just get a big list of skills that you can just copy over to Claude Cowork. And this

[14:51] is going to allow it to work with Dispatch really easily. So I'm just going to click "Copy to my skills." Actually, this one I think is already part of it. I just did this as a demo.

[14:58] So this one should be good. That's actually going to like add auto-research diagrams directly over to the system. The next one, face variants for instance, and so on and so forth. Then

[15:07] you'll get this "Copied to your skills" message at the top and now you can access it in Dispatch really easily. Okay, hopefully you guys appreciated this video. Dispatch is really cool.

[15:14] This is honestly a stand-in replacement for 80 to 90% of all the features that OpenClaw and other extraordinarily insecure implementations of autonomous decentralized agents provide for you. So, I'm using this thing all the time now. And it's not just because I'm like "I love Big Daddy Anthropic," although I do. It's because I just think this is

[15:31] a much safer and better solution than something like what most other people on Twitter and X are probably showing you. If you guys like this sort of video, please sub to the channel. Around 70% of you guys aren't for whatever reason. So, you'd be

[15:41] doing me a big solid. Like and then comment down below with whatever the heck you want me to make videos on. I really make videos based off of audience feedback at this point. So, if you guys have anything in particular you want me to record or cover, let me know. I'm

[15:53] more than happy to do it for you. Have a lovely rest of the day. Catch all y'all in the next one.
