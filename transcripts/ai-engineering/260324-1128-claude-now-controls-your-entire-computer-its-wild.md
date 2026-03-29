# Claude Now Controls Your Entire Computer... It's WILD

**Channel**: Paul J Lipsky
**Duration**: 8:52
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=dwYfNQzHQuY
**Transcribed**: 2026-03-24 11:28

---

## Organized Notes

**Computer Use in Claude Cowork**

- Claude Cowork now has **computer use** — it can control your mouse, type on your keyboard, and interact with native desktop apps (not just browser or file access)
- How it works: Claude takes **screenshots** of your screen, then moves the mouse and types to interact with apps
- This goes beyond MCP connectors — if an app has an MCP connector (e.g., Notion), Claude uses that. Computer use is for apps **without connectors** (Apple Calendar, Photos, Keyboard Maestro, etc.)

**Setup**

- Enable in Claude Desktop: **Claude menu → Settings → scroll to Computer Use → toggle on**
- Two system permissions required: **Accessibility** (for mouse/keyboard control) and **Screen Recording** (for screenshots)
- Screen Recording may require **manually adding Claude** via the + icon in system settings, then restarting Claude
- Warnings: some actions **cannot be undone**, websites/documents could contain **malicious instructions** that misdirect Claude
- Apps require **one-time approval** — after first use, you can toggle on **"Allow all computer actions"** to skip future permission prompts

**Demo 1: Apple Calendar**

- Asked Claude what's on the Apple Calendar for today — no MCP connector exists for Apple Calendar
- Claude opened the Calendar app, navigated it, and **read the events** — worked fast and accurately
- **Accessibility use case**: people with mobility issues could use voice-to-text + Claude to operate their computer hands-free

**Demo 2: Photo Editing via Dispatch (from phone)**

- Sent a photo via **iMessage** to the Mac Mini, then used **Dispatch** from phone to tell Claude to:
  1. Open the image from iMessage
  2. Open it in the Photos app
  3. Use the **Cleanup tool** (Apple's AI background removal) to remove a person
  4. Send the cleaned-up image back via iMessage
- Claude completed all steps: found image in iMessage, right-clicked to add to Photos library, opened Photos, selected Cleanup, chose the right person to remove, and sent result back
- First steps were fast; later steps (selecting image, sending) became slower
- Had to **download the Cleanup AI model** mid-task — Claude waited and continued after download completed
- Claude even **sent progress updates** via Dispatch during the process

**Demo 3: Keyboard Maestro Macro Setup**

- Asked Claude to open **Keyboard Maestro** (a Mac automation app) and set up a macro: every day at 1:30 AM, close and reopen the Claude app
- Claude navigated Keyboard Maestro's interface correctly: created the macro, named it, set the time trigger, selected the quit action, and chose the Claude app
- This demonstrates Claude handling a **complex, unfamiliar app UI** with multiple steps

**Key Observations**

- Computer use is **not used for apps with existing MCP connectors** — MCP is more efficient
- Works with **Dispatch** — you can trigger computer use tasks from your phone while away
- Speed varies: simple navigation is fast, complex multi-step interactions get progressively slower
- **Idea capture workflow**: screenshot ideas on phone → send to iMessage → Claude extracts info and adds to a database — all automated

---

## What This Means for Your Work

Computer use is the feature that bridges Claude Cowork from "file and API access" to "full desktop automation." For you, the immediate implications are less about the consumer demos shown (photo editing, calendar reading) and more about controlling BARMM-specific desktop apps and workflows that don't have MCP connectors.

**The Apple Calendar demo solves a real gap in your workflow.** You manage 9+ projects with meetings across government agencies, OOBC coordination, and MoroTech operations. Apple Calendar has no MCP connector, so your /session-summary and /context skills can't currently see your schedule. With computer use, a Cowork skill could read your Apple Calendar, cross-reference with project deadlines in the vault, and surface scheduling conflicts — all without you building a custom integration.

**The Keyboard Maestro pattern extends to your Mac automation.** You could have Claude set up macros to automate repetitive desktop tasks: auto-launching your development environment (iTerm + VS Code + browser tabs for e-Bangsamoro), scheduling nightly git pulls across your 9 repos, or setting up hotkeys for frequently-used Claude Code commands. This turns Claude into a Mac system administrator, not just a coding assistant.

**The "screenshot idea capture" workflow Paul describes maps to your existing knowledge pipeline.** You already have /youtube-transcriber → vault → knowledge-areas. Computer use could extend this: screenshot a Twitter thread or news article on your phone → send via iMessage → Claude extracts the content, runs /research-pipeline on the topic, and saves a knowledge note to your vault. This is a passive knowledge capture system that feeds your Obsidian vault without you opening Claude Code.

**The speed degradation on multi-step tasks is a real constraint.** Paul observed that simple navigation was fast but complex sequences slowed progressively. Your legislative workflows (/bangsamoro → /bill-drafter → /fact-checker) are already multi-step — adding computer use on top (e.g., opening a PDF in Preview, extracting text, then processing it) would compound the latency. For now, your CLI-based /transcriber skill with OCR is faster than having Claude visually navigate a PDF reader.

**Concrete next steps:**
- Enable computer use on your Mac and test it with Apple Calendar integration — verify it can read your schedule and surface conflicts
- Evaluate using computer use + Dispatch for "screenshot → vault note" passive knowledge capture from your phone
- Consider Keyboard Maestro macros for your multi-repo development environment setup, triggered by computer use
- Don't replace your MCP-based workflows with computer use — MCP is faster and more reliable for apps that support it

### How This Can Improve Your Claude Skills and Workflows

**The /context skill could gain calendar awareness.** Your /context skill loads vault context (daily notes, project files, backlinks) but has no visibility into your schedule. With computer use, /context could include a "read Apple Calendar for today and this week" step, surfacing meetings and deadlines alongside vault context. This makes the "what are we working on" output actionable — not just what's in the vault, but what's on the calendar.

**The /transcriber skill could use computer use as a fallback for stubborn PDFs.** Your /transcriber currently uses OCR tools (Tesseract, pdf2image). Some BARMM documents — especially scanned committee reports or handwritten resolutions — fail OCR. Computer use could open the PDF in Preview, zoom in on specific pages, and read text visually from screenshots. This is slower than OCR but more reliable for edge cases. Add this as a Tier 3 fallback in /transcriber, not a replacement.

**New skill opportunity: /desktop-automator.** Check ~/Vault/Claude-Skills/index.md — there's no skill for configuring Mac system automation. A /desktop-automator skill could use computer use to: set up Keyboard Maestro macros, configure Launch Agents, create Automator workflows, or set up system-level cron jobs. This fills the gap between Claude Code (developer workflows) and Claude Cowork (user-facing tasks) by automating the Mac environment itself. Relevant for setting up development environments for e-Bangsamoro, BangsamoroHR, and other projects.

**The Dispatch + computer use combo enhances /session-summary.** Currently /session-summary runs at end-of-session and writes to the vault. With computer use + Dispatch, you could trigger an end-of-day workflow from your phone that: reads today's Apple Calendar (what meetings happened), checks git log across repos (what code changed), reads the vault daily note (what was captured), and synthesizes a comprehensive daily summary — all without touching the keyboard.

**Cross-pollination with Parliamentarian.** The "control unfamiliar app UI" capability means Claude could interact with government web portals that don't have APIs. If BARMM's internal document management system or committee scheduling tool is web-based but has no API, computer use could navigate it, extract information, and feed it into your /legislative-briefer or /bill-drafter skills. This turns Claude into a bridge between legacy government systems and your modern AI-augmented workflows.

---

## Transcript

[00:00] I cannot believe what Anthropic just dropped. Claude now has the ability to actually use your computer for you. And I don't mean just access files on your computer and open up Chrome and browse around. I mean actually using apps on

[00:15] your computer. If this works well, this is going to be absolutely nuts. Let's set it up and test it out and see how well this actually works. I currently

[00:25] have co-work set up on two different computers. my main laptop and then I have it set up on the mini that has access to a lot less. So, I'm gonna set it up on the mini first just because I'm a little bit scared about this. I I

[00:39] don't know like is it going to be able to just run across my entire machine without permissions. So, let's set it up on my mini first. I'll remote into it.

[00:47] To get to this, you have to click on claw on the top and click on settings and then scroll down here. You'll see computer use. Go and toggle it on. Here

[00:57] are all the warnings about it. It tells you that Claude is going to be taking screenshots of your screen and then actually moving the mouse and typing on the keyboard for you. Keep in mind that some things it does you will not be able to undo. You are going to be approving

[01:14] apps once and then if you don't approve the app, it's not going to be able to use it. And yeah, some websites and documents could contain malicious instructions that misdirect Claude. So, you know, be very careful how you're using this. And that's why I'm setting

[01:30] this up on my second device. I'll turn this on, though. And then down here, you also have to enable two settings. One's

[01:37] for accessibility and the other is for screen recordings. So, I'll click on the one for accessibility first. That will open up the settings. You can just

[01:47] toggle it on. Enter in your password and then click modify settings. Close that out. and then do the same thing for

[01:56] screen recording. This time though, it's not showing up, so I have to manually add it by clicking the plus icon. Enter in my password again, and then actually manually select Claude in here and open it. That also requires a restart of

[02:09] Claude. So, let's do that. So, it looks like it's all set up. Let's test it out.

[02:13] Now, this isn't going to work with any tools that it already has access to. So, for instance, if it has access to Notion, it's not going to open up the Notion app and click around for you. It's going to use the MCP connector to Notion. That's more efficient. But

[02:30] notice how I don't have a connection here to Apple calendar. So, let's try that. I'll ask it what's on my Apple calendar for today. And now it's asking

[02:39] for permission to use calendar. So, I'll select allow for this session. Can I allow it permanently? I don't see a way

[02:49] to do that. So, I'll just allow for this session and see what happens. Okay. Wow.

[02:56] This is completely handsoff. Okay. Not completely hands off. I have

[03:00] to allow this. Uh, but it's still able to see the calendar. Let me just click allow here, though. Yeah, there we go.

[03:07] Wow. Yeah. Oh, that is guys, that's really cool. That is super

[03:14] impressive. What immediately comes to mind for me are people with mobility issues. Maybe they can't use their hands as well. You can just use voice to text.

[03:24] Tell Claw what you want it to do on your computer. And now it can do it. And that was really fast. Let me see if we can

[03:31] kind of push this and see if it can do something a little harder. For this next example, I'm going to use dispatch. If you're not familiar with this, this allows you to use your phone to send tasks to co-work. And then co-work will

[03:45] actually act on your computer. So for this to work, your computer needs to be on and the claud app has to be open. But using dispatch, you don't have to be sitting at your desk. You can send it

[03:54] tasks. So, what I did was I texted a photo from my phone to my Mac Mini, and I'm going to tell Coowork to open the image I just sent you on iMessage, open it in the photo app, use cleanup or whatever it's called to remove the person in the background, and then send me the cleaned up image. That sounds like a lot. I'm not sure if it's going

[04:17] to be able to handle it. But you see over here, this is now appearing inside of dispatch. After the first time that you use it, you can toggle on allow all computer actions so it doesn't keep asking you for stuff like this. Let's do

[04:31] it. I'll turn it on. I think I have to click this because it was already up. I

[04:35] could have done it on my phone as well is what I should have done for the demo, but it would it would work exactly the same. All right. So, now it found the image that I sent it. Right clicking it.

[04:46] add the photo library. So, so far it's doing everything right, and it's pretty fast. Like, you could definitely do it faster, of course, but it's going faster than I thought it would. It's clicking

[04:58] all the right places so far. All right, so we ran into a little snag here because I didn't have cleanup downloaded on this computer yet. So, it's got to wait for that. We'll skip forward and

[05:08] then we'll see what happens when it's finished downloading. All right, there we go. It's choosing the right person.

[05:14] And look, it even updated me as well. So, it told me that yeah, we we are on the right track, but I just had to download the AI model for cleaning up. Guys, it did it. We're almost there.

[05:27] So, now we are back in messages and it did select the right option to actually add the image. Now, it's just got to select the right image and press send. It's gotten a little bit stuck. I think

[05:41] it's going to figure it out. Oh, there it goes. It did figure it out, but it is taking a long time. The first few steps

[05:46] were really fast. Grabbing the image from iMessage, downloading it, bringing into photos, and choosing the cleanup button, all that was fast. From that point on, it started to get slower and slower and slower for whatever reason.

[06:01] And even now, all it has to do is press enter, and it'll send it. And it's just not doing it. I'm sure it'll get there, though. But I already think of I can

[06:09] already think of like a ton of use cases for this. So very frequently I'm looking through my phone at like Twitter or different YouTube videos and I get ideas, I screenshot them. I would love to be able to screenshot those ideas, send them to this iMessage account, and then just tell co-work, "Hey, I just sent you a new idea." And then that will

[06:28] be a skill that I can then look at that screenshot, pull the information from it, and then put it into my database with all my ideas. And so then I can just come back to my computer and have a cleaned up list of new ideas. That's going to be a really really nice use case. Uh it did finish it obviously as

[06:46] you can see. And it it did a great job. It did exactly what I asked it to do. I

[06:51] mean that is that's really impressive. That's really cool. I'll try another one. Another pretty difficult one.

[06:56] There's this program called Keyboard Maestro. I don't know if you're familiar with it, but what it does is it allows you to set up these macros that run on your computer. So basically like you can set up hotkeys, you can set up so anytime one app opens, another app opens, or at a certain time of the day, it will run certain actions on your computer. It's sort of annoying to set

[07:17] these up, but they are really powerful. So I'm wondering if Claude Co can just set one up for me. Let's give it a shot.

[07:25] I'm I'm just going to use I'm going to use dispatch for this. I'll tell it open keyboard maestro and set up a macro so that every day at 1:30 a.m. the clawed

[07:36] app closes and then opens again a few seconds later. That way it just kind of clears things out. If anything needs to be updated, that will be a time for it to get updated as well. So let's see if

[07:51] it's able to do that. And I'm not going to bore you guys by showing you this entire process, but it is working. It actually is setting up the right way.

[07:58] You can see it started the macro, gave the right name. It says every day at 1:30 a.m. Quit the app, and it's

[08:05] selecting. It's going to select Claude in a second. It's doing it all right.

[08:09] This is incredibly impressive. The fact that you can now run your computer from your phone remotely. This is truly mindblowing. This is really, really

[08:19] awesome. So, all of this is super preliminary. This literally just came out. But I'm definitely going to be

[08:25] testing it a lot more in the next few days and really pushing it to its limits to see what else it can do. So please, if you're using it, let me know in the comments section down below what awesome use cases you have found for it. And then make sure you subscribe to the channel so that when I do an update video showing some of the cool things that I've discovered you can do with this, you don't miss out on that video.

[08:46] Otherwise, if you enjoyed it, make sure to give this video a thumbs up. And then I'll see you in the next video. Bye for now.
