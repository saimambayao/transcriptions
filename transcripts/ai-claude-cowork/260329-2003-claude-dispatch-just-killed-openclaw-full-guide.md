# Claude Dispatch Just Killed OpenClaw! (FULL GUIDE)

**Channel**: AI Impact
**Duration**: 5:05
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=pC_GpRbDQJ4
**Transcribed**: 2026-03-29 20:03

---

## Organized Notes

**Claude Dispatch: Remote Computer Control from Phone**

- **Anthropic released Claude Dispatch** -- a feature that lets you control your computer remotely from your phone through Claude
- The feature went "mega viral on Twitter" -- you can instruct Claude to open apps, navigate browsers, fill spreadsheets, and complete any desktop task from your phone
- The first version was released a week prior but was not nearly as powerful; this update is positioned as a potential **"OpenClaw killer"**

**Setup Process**

- Open Claude on your phone and find the **Dispatch section**
- Click **"Pair with your desktop"** and confirm you're signed in on your phone
- Grant permissions including the **"Keep computer awake"** feature that prevents the machine from sleeping while tasks are running
- Also requires the **Claude browser extension** installed in your desktop browser

**Demo: Financial Report Generation**

- The demo shows receiving an email with **raw financial data** (general ledger + chart of accounts, thousands of rows in CSV)
- From his phone, the creator instructed Claude to: download the email attachments, analyze the data, and create a **McKinsey-style HTML report and presentation** with visual graphs for a board of directors
- **Without touching the computer**, Claude:
  1. Opened Gmail in the browser
  2. Found and accessed the email
  3. Downloaded CSV files locally
  4. Analyzed 25,000+ general ledger entries
  5. Generated two polished HTML deliverables (financial report + board presentation)
- You can check in via phone to ask Claude how the task is progressing
- The process took 15-20 minutes -- designed for when you're on the go and come back to completed work

**Key Capabilities**

- Works in **all folders and files** on your computer
- Works in your **browser** (with Claude extension)
- Can do **anything you can physically do** at your computer, instructed remotely from your phone
- Permission management happens on your phone (e.g., granting access to Downloads folder)

---

## What This Means for Your Work

Claude Dispatch is directly relevant to your workflow because you already use Claude Cowork (Desktop) for extended tasks like bill drafting and legal analysis. Dispatch adds a mobile layer -- you could kick off heavy research tasks (legal reference compilation, guidebook chapter generation, transcript processing) from your phone while commuting or in meetings, then come home to completed work.

The "OpenClaw killer" framing is overstated -- Dispatch handles ad-hoc computer control tasks while OpenClaw/Claude Code handles persistent agent workflows with skills, memory, and iterative loops. They're complementary. Your setup already uses both layers: Claude Code for skill-based development and Cowork for extended generation tasks (like the ECCD Bill draft in `~/Library/Application Support/Claude/local-agent-mode-sessions/`).

**Practical applications:**
- Kick off `/legal-researcher` or `/deep-research` tasks from your phone while away from desk
- Have Claude process incoming emails with policy documents or legislative amendments
- Start guidebook chapter generation remotely and review when you return

### How This Can Improve Your Claude Skills and Workflows

Dispatch doesn't change your skill architecture but adds a **mobile trigger layer**. Your existing Cowork sessions at `~/Library/Application Support/Claude/local-agent-mode-sessions/` could be initiated remotely. The key insight: tasks that currently require you to be at your desk (opening PDFs, downloading email attachments, running scripts) can now be dispatched from anywhere. This is especially useful for your `/transcriber` and `/youtube-transcriber` workflows where you spot a video on your phone and want it transcribed immediately.

---

## Transcript

[00:00] So, Anthropic and Claude just released a brand new incredible feature that has gone mega viral on Twitter. You can now enable Claude to use your computer to complete tasks. It opens your apps, navigates your browser, fills in spreadsheets, anything you do sitting at your desk. So, it can basically take

[00:17] complete control of your computer and you can instruct it directly from your phone. They did release the first version of this patch last week, but it was not nearly this powerful. Now, it's basically an OpenClaw killer because straight from your phone, you can just do anything you would do actually sitting at your desk. So, let me show

[00:34] you exactly how to set it up, how it works, and do an example of how powerful this tool is. So, here on my phone, I'm just going to open Claude. And as you can see, you have the Dispatch section right here. Click pair with your

[00:48] desktop. Then, I'm just going to click that I'm signed in on my phone. You can give it certain permissions. I'm just

[00:54] going to allow all of this, including this keep computer awake feature, which prevents it from sleeping while this task is running. And once you've set it up, this is what it now looks like. So, just as an example, I sent myself this email attached to financial data from last month with a general ledger and a chart of accounts with thousands of rows of raw data in a CSV file. Now, let's

[01:16] say I was outside and I was not on my computer. I saw that email on my phone. So since Claude now has complete access to my computer, I can just write on my phone something like, I received financial data in my email just now. Can

[01:32] you download the files on my computer? Then use the data plugin and skills to make a comprehensive report and presentation of this data. Then I can confidently present to my board of directors. Make the report and presentation as an HTML with a lot of visual graphs in McKinsey style. So,

[01:49] that's an example of what you can do. So, let me just send this off on my phone and we'll see what that looks like on my computer. I basically won't touch my computer at all in this entire video and we'll just let Claude do its thing.

[02:05] So, since I already tested this off camera, it basically just says upgrading to McKinsey style HTML. I've kicked off a new task that will pull the same email data and create two polished HTML files, static report and slide presentation. But you can now see that without me doing anything, Claude with complete access to my computer opens up Gmail in my browser. It will then find

[02:29] and access the email and automatically download these CSV files that it will then analyze and turn into these reports that I asked for. And this is all from my phone. I have not touched my computer since we started this task. But for this

[02:44] to work, you do also need the Claude extension in your browser. So make sure that it's downloaded beforehand as well. And it says at the bottom, Claude is active in this tab group. You can see at

[02:55] the top which tab Claude is currently working in and it's now automatically opening the actual CSV file and will download it on my computer locally so that it can analyze it. All right, so it did take a little while but it is finished now. But in the middle of the process I just basically asked Claude how it's coming along and it obviously tells you where it is. So it told me

[03:15] that one HTML was done and it was making the other one. Obviously, I've just been waiting around for this to finish for this video, but normally when you're using this, you would probably be outside on the go and you would just come home to this task finished. So, it wouldn't really matter if it took like 15-20 minutes. But, it then went ahead

[03:31] and said, "Both McKinsey style HTML files are done. Two deliverables ready for your board. Financial report and board presentation. Both pulled from the

[03:40] full data set. 25,000 general ledger entries, key numbers, and then you should see both files delivered by the task. Open them in any browser, and you're good to present." And then since

[03:51] it didn't actually tell me where it stored it, I'm just going to ask here. All right. So, it basically said it's in a temporary location, but would you like me to save it in the downloads or desktop folder? I'm just going to say

[04:06] downloads, please. And I will then just allow Cowork the permissions for downloads. You can do that on your phone. So, you don't have to be on your

[04:13] computer for that either. And you can now see that both of the files are right here in my downloads folder. So, I can now go ahead and open these up and see what they look like. So, this is the

[04:25] financial review. You have loads of charts. You have all the data. And then

[04:30] this is the actual report. So, here you have all the data. Here you have quarterly performance. Loads of data for

[04:37] you to analyze. But obviously this was just to show you how the Dispatch feature works. It's super impressive. It

[04:42] can work in all of your folders and files. It can work in your browser. Anything that you can physically do on your computer, Claude can now basically do for you with you just instructing it remotely from your phone. Super powerful

[04:54] tool. This might have just killed OpenClaw. Who knows? I just wanted to

[04:58] show you how this worked. Hopefully you enjoyed the video and I'll see you in the next one. If you have any questions, do let me know down below.
