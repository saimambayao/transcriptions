# Claude Can Control Your Computer - Everything You Need To Know

**Channel**: Skill Leap AI
**Duration**: 17:52
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=Dl36TDBFUdo
**Transcribed**: 2026-04-03 11:06

---

## Organized Notes

**What Claude Computer Use Is**

- Claude Computer Use lets Claude **interact with your Mac like a person** — looking at the screen, moving the cursor, clicking buttons, typing in fields, opening apps, and switching windows
- Different from the standard Claude chatbot: instead of a back-and-forth, you **give it a task and watch it execute** on your screen in real time
- Different from Claude Cowork (background tasks in a specific folder): Computer Use gives Claude **access to your full computer** — you cannot use your computer while it's working
- Technically a feature **inside Claude Cowork** (and Claude Code), not a standalone product
- **Current status**: Mac only (not Windows), early-stage, works but is slow — best for early adopters and testers, not production workflows yet

**How to Enable Claude Computer Use**

- Requires the **Claude desktop app** on Mac (`claude.ai/downloads`)
- Requires a **paid Claude subscription** — free tier does not include Cowork
- After installing, Claude Cowork, Claude Code, and Dispatch appear on the desktop app
- **Settings to enable** (Settings → General):
  - **Keep computer awake** — required so remote tasks can run uninterrupted
  - **Allow browser use** — lets Claude interact with Chrome without asking per action
  - **Computer Use** — grants Claude permission to take screenshots and control keyboard/mouse
- **Denied apps**: you can exclude specific apps (e.g., email, calendar) from Claude's access
- **System permissions**: may need to grant Screen Recording and Accessibility in macOS System Settings

**Dispatch — Remote Control from Your Phone**

- **Dispatch** lets you send tasks to Claude on your desktop **from the Claude mobile app** on your phone
- Your phone works like a "walkie-talkie" — you send a task, Claude runs it on your desktop, you review when you return
- Setup: pair the Claude mobile app with the desktop app → enable "Dispatch" setting in Cowork
- Can run tasks on a **schedule** as well
- Key use case: **send a task before sleeping or leaving the office**, Claude works overnight, you review results in the morning

**Demo 1 — Adobe Premiere Pro File Import**

- Task: open Adobe Premiere Pro, create a new project ("Claude Demo"), find a screen recording on the desktop, and import it into the timeline
- Result: **completed successfully** after several minutes and some permission friction
- Issues encountered: needed to grant Finder and Premiere Pro permissions mid-task, a pointer-highlighting overlay app interfered and had to be quit
- Time taken: ~10 minutes for a task a human does in under 1 minute — **not efficient yet**, but demonstrated it can find apps, find files, and take actions inside third-party apps
- Real use case: having Claude move a file to Dropbox and send the link to an editor while you're away

**Demo 2 — Document Summarization + PDF Creation**

- Task: find a specific Word document buried deep in Dropbox, summarize it, rewrite it as a one-page blog post, and save as PDF to desktop
- Result: **completed quickly and cleanly** — found the file, opened Word, read and summarized 1,700 words, wrote a one-page blog post, generated a formatted PDF on the desktop
- Advantage over Cowork: could search the **entire computer including Dropbox**, without needing to specify a folder or open a browser
- Real use case: turning files on your computer into deliverables (emails, PDFs, Dropbox links) while away from desk

**Demo 3 — Website Analysis + Code Generation**

- Task: browse the creator's website, analyze it, and rebuild a new version using Claude Code
- Result: **worked unexpectedly well** — found the site, pulled relevant info, generated 2,000+ lines of code with animations
- Note: ran from the Cowork tab, not the Claude Code tab — both modes support computer use
- Demonstrates that Claude Code + Computer Use can close the loop from **research to implementation** in one prompt

**Demo 4 — Dispatch from Phone**

- Task (sent from phone): open the Downloads folder, find the latest screen recording, rename it "dispatch demo," move it to Dropbox, and send the link
- Result: **completed**, found and renamed the file, moved to Dropbox, surfaced the link in a text editor on the desktop
- Minor gap: the Dropbox link appeared in a desktop text editor, not delivered back to the phone app — still requires some manual retrieval
- Relatively fast compared to the first demo

**Honest Assessment: What Works vs. What Doesn't**

- **Works well**: finding named files, opening apps, basic document tasks, simple file operations, browsing + code generation
- **Struggles**: imprecise file descriptions (if you're not specific, it searches everywhere), data entry into web forms (too slow), complex multi-step editing tasks (e.g., making video cuts in Premiere)
- **Not yet practical for**: actual video editing (couldn't make basic cuts), form-filling workflows, any task where speed matters
- **Best current use case**: **async, non-urgent tasks** while away from the computer — file organization, document creation, moving/converting files, sending summaries to yourself
- Claude ships updates "almost every day" — computer use is expected to improve rapidly

*Quotable Quotes:*

> "The potential is unbelievable — to have a virtual assistant that could use a computer just like a human could, give it tasks, and it could reason through the task, figure out what to do, open applications like video editing, email, word processing, and do things for you." [03:09]

> "Your phone will work like a walkie-talkie and you could communicate with Claude on your computer. You send Claude a message and it will start the task — you could run it on a schedule whenever you want." [14:17]

> "Is it the fastest way to do the task? Obviously not. Is it going to be at some point faster than what a human could do? Most likely." [10:16]

---

## What This Means for Your Work

Claude Computer Use is still early — the demos confirm both the promise and the friction. For Saidamen's current setup, the most immediately relevant angle is **Dispatch as an async work multiplier**, not the real-time computer control itself.

**Where this directly applies:**

- **Solo dev bottleneck**: As a solo founder running 9+ active repos (e-Bangsamoro, Tarbiyyah-MS, MoroMarket, OBCMS, Parliamentarian, etc.), Saidamen's biggest constraint is attention switching. Dispatch addresses this: send a task (e.g., "move the latest DB migration export to Dropbox and email me the link") before a meeting or overnight, and Claude handles the file operations while you're away.
- **Transcription + knowledge pipeline**: The document-to-PDF demo maps directly to the existing `/youtube-transcriber` workflow. If Claude can open Word, read a document, rewrite it, and generate a PDF — that's a pattern that could eventually automate the guidebook production step where converted drafts need to be reformatted.
- **Legislative research tasks**: Saidamen's Parliamentarian app runs Claude agents for legal analysis. Computer Use could eventually close the loop — not just generating analysis but opening the right browser tab, navigating to lawphil.net, and extracting the case text directly.
- **Cowork vs. Computer Use**: The existing Claude Cowork setup (background tasks in a folder) already powers many of Saidamen's workflows. Computer Use extends that to the full computer — useful for tasks that reach outside the designated folder (e.g., the Dropbox use case, or moving files between projects).

**What to hold off on:**

- Don't restructure existing Cowork workflows around Computer Use yet — it's Mac-only, slow, and still unreliable for complex tasks. The existing `/skills-bucket` + Cowork setup is more reliable for production work.
- The form-filling and video editing demos failed — avoid using it for data-entry tasks in BARMM platforms until the speed improves.

**Concrete next steps:**
1. Enable Dispatch on the Claude mobile app — this is low-friction and immediately useful for async file operations and document tasks.
2. Test a specific Cowork + Computer Use task: "Find the latest BAA markdown in legislation/bills/enacted/, convert to PDF, and save to source-pdfs/baa/" — this is the kind of named-file, low-risk task that fits the current capability.
3. Watch for Computer Use integration with Claude Code specifically — the Demo 3 result (browse → analyze → generate 2,000 lines of code) suggests real potential for the e-Bangsamoro frontend-first dev workflow.

### How This Can Improve Your Claude Skills and Workflows

**Skill updates worth considering:**

- **`/youtube-transcriber`**: The document-to-output loop in Demo 2 (find → read → rewrite → PDF) mirrors what the transcriber does with video content. Consider adding a Cowork-aware variant that can reach files outside the designated folder for batch processing older transcripts.
- **`/scrape`**: If Computer Use can open browsers and interact with pages, this could eventually replace the Playwright-based scraper for sites that block headless browsers. Not yet — but worth tracking as computer use matures.
- **`/session-summary`**: The Dispatch demo shows Claude surfacing results in a text editor. A Dispatch-triggered session summary (send "wrap up today's session" from phone → Claude writes the session log to `~/Vault/session-logs/`) would be a clean new workflow.

**New skill opportunity — `/dispatch-tasks`:**
The skills library doesn't have a skill for structuring async Dispatch-style tasks — tasks designed to run unattended on a schedule or while away. This could define templates for common Dispatch patterns: file operations, document conversion, Dropbox moves, report generation. Low-priority for now given the tool's early stage, but worth creating when Computer Use becomes reliable.

**Project-specific:**
- **Parliamentarian**: Computer Use's browse + act loop is the missing piece for making the Parliamentarian truly autonomous — not just analyzing legal text but retrieving it from lawphil.net or the BTA parliament website on demand.
- **Guidebook production pipeline**: The Word → PDF demo is essentially what the `/guidebook-writer` does at the end of each chapter. If Computer Use can automate the "open Word, format, export PDF" step, it removes the manual conversion step that currently requires Python WeasyPrint scripts.
- **BTA Bills Scraper**: The current scraper (`scripts/scrape_bta_bills.py`) hits the WP REST API directly. If that API closes or changes, Computer Use could serve as a fallback — browse the parliament website, extract bill text, save to `legislation/bills/scraped/`.

---

## Transcript

[00:00] Thanks to HubSpot for sponsoring this video. Claude can now control your computer. You could actually watch it do actual work for you. And on top of that,

[00:09] you could control it remotely from your phone. And this is kind of a big shift from the usual chatbot experience that we're all used to. So instead of just typing a prompt into Chat GPT or Claude and getting an answer, this actually clicks around your Mac. It could open

[00:25] different apps as it needs it. It could type for you. It could work on tasks as you watch it on your screen. And when

[00:33] you pair it with this dispatch option, you could send a task directly from the phone using the Claude app. And Claude works on the desktop while you're away from your desktop. So, in this video, I want to walk you through exactly how to turn on this Claude computer use in something called Claude Co-Work. I also

[00:52] want to show you dispatch. That's where you could control Claude and your computer from your phone. and then we'll test it. Here I have a handful of real

[01:00] demos that I want to show you and then I'll show you what I think is actually genuinely useful right now and what feels a little bit early and more like a product that has not found its footing yet. Okay, first let me just walk you through what computer use actually is. So claw computer use means claude can interact with your Mac more like a person could. So it can look on your

[01:24] screen, decide what needs to do next, and then move the cursor, click on buttons, type in fields, open different apps, switch windows as it needs to, and carry out different tasks step by step. So if you're already using Claude, well, Claude could do a lot, but it's usually a back and forth, right? You're not just giving it a task and then watching it go do that task. They have something else

[01:46] called Claude co-work. Now, with co-work, and I've covered co-work in detail on this channel, but with co-work, you give it a task and it can go do things for you, but you don't watch it do things for you. You could still use your computer. It will do

[01:59] things in the background and it could do things in a specific folder that you give it access to. So, cloud computer use takes all that to the next level. So, it's technically part of cloud co-work, but you are given it permission to access your full computer and you can't use your computer while claud is going to work on your computer. So, you

[02:21] may want to get a dedicated computer for it. And before we jump into the demos, few different things I want to mention right now. This is a Macon feature. So,

[02:29] if you have a Mac, you could actually use it right now, but it's not yet available in Windows. You do also need the claw desktop app on your Mac installed. I'll put a link in the description for that. And you need the

[02:40] subscription, the paid subscription to be able to use Claude Co-work. So, the free version of Claude is not going to have this if you want to use Dispatch. And Dispatch allows you to use your phone and text the Claude app here and you'll be able to do things on your computer for you while you're away from your computer. So, that's through the

[02:59] Claude mobile app. That one you could install on your phone. And I want to mention before I show you the demos, there's going to be some things that are going to feel impressive, but a lot of it is going to still feel early. The

[03:09] potential is unbelievable though to be able to basically have a virtual assistant that could use a computer just like a human could and you could give it tasks and it could reason through the task, figure out what to do, open applications like video editing application, email applications, word processing application and do things for you is just going to be unbelievable once it's there. Some of it is going to fill pretty early as I show you some of these demos. Definitely use this at your own risk, but I will show you a hands-on demo here. I'll show you five or so

[03:38] examples so you could see it in action and see if you're comfortable using it. So, I recommend just watching this video and seeing the full experience before you install and start running it on your computer. Now, before we jump into the demos here so I could show you exactly how it works, I also want to share a free resource that I made with HubSpot that works great with Claude. And if you

[03:57] watch my channel, I've been working with HubSpot for quite a while now, but this is actually the very first time I was able to make my own resource with their help. And it was actually a really cool process. This resource is called five easy low-risk tools our marketers made with AI and it covers five tools that I've personally vibe coded with different tools and I use in our company every single week. So I've made one that

[04:22] is our entire onboarding process for our skill leap customers. I made another one that's our marketing funnels app I personally use to figure out how to improve our social campaigns and our paid ads campaigns. I have another website builder that creates landing pages for different geographies that we do business in. And I have a few other

[04:43] ones too and with each one I've shared the exact prompt I use to create these using the VIP coding app of your choice. Claude Code is actually a perfect one and you could replicate these results just like mine. I'll put a link in the description to this resource. And thanks

[04:58] to HubSpot for sponsoring this video and for helping me make this resource for my audience. Now, let me show you how to actually turn on Claude Computer Use and then I'll show you all the use cases. First, you have to make sure you have the desktop app on your Mac. So, if you

[05:12] go to claw.ai/d downloads, you'll be able to download it from here or from here. Now, I mentioned it's available as part of claude codework. technically also available as

[05:22] part of claude code which is something that could create things for you using code and I've covered claude code in a separate video too. So once you have that app installed on your computer you'll see claude co-work right on top and then you'll see claude code over here and you also have claude chat. Now claude computer use is not part of claw chat is mainly being used with claude co-work and claude code and then you'll see dispatch over here. I'm going to

[05:47] show you how to sync your phone with the desktop so you could send requests and messages here from your phone to the app too. But you still have to turn one more thing on. So you have to go to your settings and over here you have to go to general and scroll down. So few

[06:04] different things I recommend you turn on here. Keep computer awake. You could turn this on here because if your computer falls asleep, you can't remotely control it. The physical

[06:14] computer has to be accessible. Allow browser use. This will let Claude browse and interact with websites on Chrome without asking. I definitely recommend

[06:24] you turn this on. It will give it some web access here, which sometimes it's going to need. And then you have computer use. Let Claw take screenshots

[06:32] and control your keyboard and mouse in apps you allow. And you want to turn that on. Now, you could also choose to not give it access to some apps. So,

[06:41] denied apps. You could add apps here. Now, I've given it access to screen recording and accessibility. Depending

[06:48] on your setup, you may have to go to your system settings and turn a few permissions on there, too. And in this case, I don't have claude on. So, I'm going to go ahead and turn this on here, too. And one more setting inside of

[06:58] co-work, if you're going to use dispatch, make sure this is also turned on here. So, claude could be accessible from the mobile app on your phone. That's called dispatch here. Okay. Okay,

[07:09] let me show you a couple of demos here and then we'll go ahead and use dispatch too and do it from our phone because I think the real use case for this is using your computer while you're away from your computer to have Claude co-work or claude code actually work and then you could review that work maybe when you come back. So right now here's the prompt I'm going to use. I'm going to ask you to open an app for me. So

[07:31] this is a video editing app called Adobe Premiere which we use. Create a new project called Claw Demo. then find a file on my computer called claude computer use demo which is a name of a video file of a screen recording I did and saved to my desktop and import that into the premiere project. Okay, so this

[07:50] is what basically an assistant editor right now does, right? Opens it, puts it there, maybe makes some edits after that, but right now I want to see if it's able to do this. And I'm going to use the Opus 4.6 model here to do that.

[08:03] And now it's going to ask me for permission. If you normally use co-work without those permissions, it's going to ask you, well, what folder can I work in and what files can I access, this is asking me, you want to use Adobe Premiere Pro. So, it's asking for the newer version and Finder, which is how you move files around in your Mac. So,

[08:22] I'm going to allow it full control. So, again, just warning you, this is getting more access to your computer than any other app has ever asked for access. Okay, now I'm going to go hands off. You

[08:34] could see my screen here. The borders are turning red. Now, it looks like I didn't give it some of those permissions. So,

[08:42] I'm going to allow those and I'm going to take my hands off the keyboard one more time. Okay. Clicked on new project here. Typed in a new title. Now, I'm

[08:51] actually cutting couple of the pauses because I think I'm just trying to move my mouse and it's interfering with it. But, let me see what it's doing next. Now, let me click on desktop on the left sidebar to navigate. I had another app

[09:02] here that was highlighting my pointer. So, it asked me to turn it off. It was interfering with what it was trying to do. I have now turned that off. Okay, it

[09:12] finally found the clip here. Let's see if we could figure out how to import it. Okay, it imported it and it's adding it to the timeline down here. And it just

[09:25] made this full screen. So, right here the progress. Open Premiere Pro. It

[09:29] created a project called Claude demo and it found and imported that clip that I had on my desktop. And by the way, I have dozens of different video files and screenshots and a really messy desktop right now. So, it took it quite a while to try to figure out what's on my desktop. I had a pointer app that was

[09:49] highlighting my pointer that overlay was interfering with it. So, I had to quit that. So I spent maybe 10 minutes doing this task that obviously will take less than a minute here if you did it by hand. But now the second time around

[10:04] when I did it, it was a little bit faster. I just wanted to just show you the very first time I did a task here that got some hiccups. It had some permission issues, but it was able to do the task. Now, is it the fastest way to

[10:16] do the task? Obviously not. Is it going to be at some point faster than what a human could do? Most likely. But the

[10:22] nice thing about this, and this is why I actually wanted to show you this as a very first example, I wanted to show you that it could find the apps, it could find files, and it could take actions on those apps for you. How this comes in handy for me is we have a team of editors. Well, a lot of times maybe I have a file that needs to be edited, but I'm away from my computer. As long as my

[10:43] computer is up and running, meaning it's turned on and it's not asleep, I could then use my app from my phone and send request and maybe move that file to my Dropbox and send a link to my editor, things like that. Okay, for this next one, I want to see if it could find a document for me. I actually buried it deep into my Dropbox, but this has access to it. If it goes and finds it,

[11:04] I'm going to give it the exact file name. I want to see if it could summarize it and then I want to see if it could create a one-page version in a blog post format all from one prompt. This obviously comes in handy if you're away from your computer and you need something like this and then it could do that and maybe even put it in a Dropbox folder for you. You could even attach

[11:26] those creations into an email for example. Now I specifically haven't yet given it access to my email. That's one of the apps I excluded or my calendar just while I've been testing this out.

[11:38] Not yet comfortable, but right now it was able to pretty quickly I'm showing this in real time. Find that transcript on my computer. It opened the founder finder window. And now it's asking me if

[11:51] it could use Microsoft Word. Okay, I'm going to give it another permission here. This is a four-page 1700 word transcript. It looks like it's going to

[11:59] copy and paste that. So, it's doing all this on its own. is selecting all the text. Okay. In the progress bar, it's

[12:05] showing me that it found that it opened that Word doc. It read and summarized this the key details. It wrote a onepage blog post and it generated the blog post in PDF format on my desktop here. That

[12:17] is a nicely formatted PDF here that is saved to my desktop. Now, a lot of this also was available with co-work, right? So technically I could have put that doc in a folder, gave it access to that folder, but this was able to go and search my entire computer, including the Dropbox account that I have attached to my desktop. It did not have to go open a

[12:40] browser. It was able to do all of that. And this again becomes really handy when you do this when you're away. These

[12:46] files that are sitting on your computer, a lot of times they're not very accessible, especially if you don't have them in the cloud. They might just be sitting on your desktop. Well, this could take it, put it somewhere else, email you about it, put it on your calendar, summarize it for you, turn it into something else, all while you're away from your computer. For this next

[13:04] demo, I want to combine a couple of different things. I want to see if you could go search my website here on a browser, analyze and figure out how to improve it, and then create a new version of that website using clawed code because this computer use also works with clawed code. So, this demo should show you how that works here.

[13:21] Okay, that worked shockingly well. And I was actually on the co-work tab. I didn't switch over to the cloud code tab, but it worked the exact same way here. And it found the website. I mean,

[13:32] it created really nice animation here. It pulled in the relevant information. I mean, yeah, that's that's super good. In

[13:41] this case, it wrote over 2,000 lines of code to make this nice interactive looking website for me. But let me actually switch for the next demo to dispatch. And I think most people actually are going to use claude co-work and claude code with dispatch with this computer use as it is currently because it is relatively slow. Especially that

[14:02] first demo I showed you that took quite a long time to do something that's relatively simple. But if you're sleeping or if you're away from your computer, well, you could just send a message, go to sleep, and this will do things that might take, you know, a couple hours. as well. It will just do

[14:17] it in the background for you while you're not on your computer. So, your phone will work like a walkie-talkie and you could communicate with Claude on your computer. You send a Claude a message and it will start the task here using Cloud Co-work and Claude code here. And you could run it on a schedule

[14:34] whenever you wanted to. Now, I reinstalled the Claude app here on my phone. So, I'll show you my phone on screen. And it says pair with your

[14:41] desktop. So, I'm going to click that right here. And I'm going to say um sign into my phone. And I want to make sure I

[14:47] give it all these permissions so it could access the files obviously. It could keep my computer awake and it let Claude use my computer. Those are some of the settings I already showed you. So

[14:55] I'm going to finish this here. Okay. Now on my phone, I'm going to give it a task here. So I'm going to say open the

[15:01] download folder on my computer. Find the latest screen recording. Rename that screen recording to dispatch demo. Move

[15:07] it to my Dropbox folder and send me that link. By the way, the dispatch is right over here. So, if you want to see it on your computer, it's over here. But

[15:16] obviously, right now, I would be doing this while I'm away from my computer. And I'm just going to use the mobile app to do that. So, I'll let this go to work here. Now, it's going to ask me on my

[15:27] phone. So, I don't have to be near my computer to give it access. I could just say allow once here. Okay. It decided to

[15:33] open up a text editor and copy paste the link here from my Dropbox right there. And it showed me exactly what it did. So, it found the screen recording. It

[15:43] renamed it. It moved it to Dropbox. It gave me the link to Dropbox. It looks

[15:47] like it's not giving me the link in dispatch. So, I'll have to figure out how to get that from here to there. But, it did do all the things I asked for.

[15:54] And it was actually relatively fast compared to the very first demo I did. Now, a few places where this is going to struggle a lot. And I did a lot of testing, especially with some of the demos I showed you. What I was trying to

[16:05] do with the very first one was take it far more than where it was able to go, which is do an actual edit for me. And I gave it some instructions. It wasn't even able to make basic cuts for me and move clips around. So that is where I'm

[16:19] hoping it goes. So it can actually help us get rid of some of those repetitive task and make the edit more creative. The other places this struggled is when it wasn't actually sure what files to go find. if I wasn't very specific about

[16:33] the file names, it was having a hard time figuring out which one to look for and it was looking all over the place. Now, if you combine it with the Chrome option where it could open up a browser, it could also do some data entry for you. I still had some struggles there where I gave it a form and then I gave it a website and I asked it to take all the information from that form and input it to the website. It was just far too

[16:56] slow for this demo and it just didn't quite work right. That was the last demo I was trying to show. But after a little while, I just realized it's not quite there yet. So, I think this is good.

[17:06] It's for early testers, but not quite there yet where I'm using it for actual work. It was more like something I would use in a demo like I showed you. But to make this a real practical application, it's got ways to go, but the possibilities are unbelievable. And

[17:22] Claude ships new updates pretty much every single day, every other day now. So, it's not going to be long till cloud computer use inside of cloud co-work inside of cloud code becomes the next big leap for AI because right now claude co-work is my go-to AI tool and I use it now more than any other tool even more than regular things I do inside of Chad GPT and cloud. It's unbelievable the amount of things it could do. So

[17:47] definitely watch that video next if you haven't checked out the claw cowork
