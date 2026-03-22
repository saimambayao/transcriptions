# Your Claude Code Terminal Could Look Like This

**Channel**: Eric Tech
**Duration**: 16:08
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=Jvl_MOBPRXI
**Transcribed**: 2026-03-23 00:22

---

## Organized Notes

**What This Is About**

- Customize Claude Code's **status line** to show model name, context %, token count, git branch, and more
- Helps you **monitor context window usage** in real-time -- staying under threshold = higher AI accuracy
- Replaces needing to type `/context` manually every time

**Setup Steps**

1. Install **jq** (command-line JSON processor): `brew install jq`
2. Start a Claude Code session
3. Use the **`/statusline-setup`** command with a prompt like:
   - "I'm using Mac OS, install globally, create a separate .sh file for the script"
4. Claude creates a **bash script** that displays: model name, current directory, git branch, context remaining, output style
5. Run the generated setup command in your terminal, then **restart Claude Code**

**What the Status Bar Shows**

- **Model name** (e.g., Opus)
- **Context window %** consumed (e.g., 23% of 200k)
- **Token count** -- input tokens + output tokens + cached tokens
- **Git branch**, current directory, session info
- Customizable with **different themes** (e.g., solarized light) and colors

**Accuracy Breakdown for Token Calculation**

- Context usage = **cached read input** + **cached creation input** + **input tokens** + **output tokens**
- Displayed as percentage of max context window (e.g., 32% of 200k)
- Initial setup may show inaccurate token counts -- prompt Claude to **align it with `/context` output**

**Why Context Monitoring Matters**

- After exceeding a certain context threshold, **AI generation accuracy drops**
- By watching the status bar, you can:
  - Know when to **compact/clear context** (`/compact`)
  - Investigate **what's consuming initial context** (system prompt, MCP tools, CLAUDE.md)
  - **Remove redundant plugins** to reduce initial token consumption

**Optimizing Initial Context Usage**

- Ask Claude to **investigate high initial context consumption**
- Common culprits:
  - **System prompt** (~20k tokens)
  - **MCP tool definitions** (redundant plugins)
  - **CLAUDE.md file** (large rule sets)
  - **Duplicate plugins** (e.g., front-design appearing twice)
- Example optimization: removed **4 redundant plugins**, reduced from 13 to 9 MCP servers
  - Saved **8-12k tokens** on initial context
  - Initial consumption dropped from ~25% to ~23%
- Use **conservative optimization** to avoid losing important CLAUDE.md rules

**Reusable Setup**

- Eric created an **MD file** with setup instructions
- Pass the MD file path to any Claude Code session to **auto-install the status bar**
- Available in his free Discord community

---

## Transcript

[00:00] In this video, I'm going to show you exactly how you can turn your clock code terminal session to look something really plain like this to something like this where we have the model that we're using and also shows the progress bar exactly how much context percentage that we have used so far and as well as the current token size that we have consumed inside of the current context window. And we can also change the theme of it. For example, I have changed this to using the solarized light theme. And you

[00:23] can be able to change different colors of it for the status bar you're using based on your preference. And of course, you can also include more values like the versions, the model ID, the current directories, the project you're using, and so much more. And the reason why we do this is because we always want to stay under a certain context every time when we interact with claw code because after we exceed a certain threshold for context window, we usually get a lower accuracy for the AI generation. And we

[00:48] have to use the slash context here to see that. And that's why in this video, I'm going to show you exactly step by step on how to set this up on your local machine and how you can be able to configure this as well as walking you through an example of using clock code and how we can be able to monitor this and be able to improve our clock hose accuracies using this way to monitor our clock context. So pretty much that's what we're going to cover in this video.

[01:08] And if you do found in this video, please make sure to like this video and if you're interested, let's get into it. All right, so before we jump in, a quick intro for those who are new here. My name is Eric and I have spent years as a senior software engineer at companies like Amazon, AWS and Microsoft. And I

[01:23] have started this YouTube channel to share everything I have learned along the way from AI and coding to automations, web 3, career developments and more all broken down into practical tutorials that you can actually follow. So if you're ready to level up, make sure to check out my YouTube channel and hit that subscribe button. Now let's get back to the video. So to get started,

[01:44] first thing first, going to navigate to jq and we're going to install this onto our local machine for the command line JSON processor. So I'm just going to click on download and you can be able to download this with your Mac OS or Linux operating system. And what we're going to do here is I'm just going to click on download right here. There's actually

[01:59] give you a command on exactly how we can install this. So if you have Brute installed on your local machine, you can simply just use the brute install jq and basically have this installed. So I'm just going to navigate to my terminal here. Here you can see I have a project

[02:10] open and I'm just going to simply paste this command to brew install jq. And once we have this installed, I'm just going to clear my terminal and I'm just going to start my clock session. So here you can see this is my clock session.

[02:20] And what we're going to do here is I'm just going to use the status line right here which is the command and then followed by that command I'm just going to provide the prompt. First I want to mention that I'm currently using Mac OS for the operating system and I would like to install this globally and please create a separate.sh sh file for the script. So that's basically my prompt

[02:41] and I'm just going to enter this. All right. So now you can see that the status line setup agent here has configured a global status line with our Mac OS operating system. So here is what

[02:50] it creates. So it created the scripts here which is a batch script that displays the model name, the current directory, the git branch as well as the contact remaining and also the output style. Okay. And basically it has stored

[03:01] this in the settings for the global environment. And then to complete the setup, simply we're just going to run this command in our terminal and restart our clock session. So after [clears throat] I run a command basically in my root directory here, you can see I'm just going to simply start my clock session again. And here you can

[03:15] see that this is my clock session, right? So right here you can see that we have our status bar right here showing automatically. So which model we're using, the context window and also the amount of tokens that we have consumed so far. All right. So basically what we

[03:28] can do now is I can be able to use the status line here to basically prompt it and asking what are some options uh what are some options that we can add onto our status line. So that's basically my problem. I'm just going to ask what are some options that we can include in our status line and status line command here is going to fetch what are the options we can have. Right? So right here you

[03:46] can see right off the bat it consume 23%. So we can actually be able to verify that it's actually consumed 23%. And I'm just going to say currently for the context. So if I were to type in

[03:57] context, it should show me exactly what's the consumption look like, right? But while it's doing that, I also want to show you what we have, right? So for example, we can show the model, the context for the total tokens, the context window size. There's also the

[04:10] session, the workspace, so the current directory. And here you can see if I were to do the /context, you can see that it shows that currently we have consumed 23% of our context window. Okay, so total in total we have 200k, but so far we have consumed 47K. So if I

[04:24] were to scroll all the way down, you can see that is accurate based on what we have, right? So how much we have consumed 23% as well as how much tokens we have consumed. But I think this one's a bit inaccurate because if we were to scroll all the way up, you can see that currently we have consumed this much, right? So we have consumed 23%. So I'm

[04:39] just going to copy this. And here I'm just going to say currently you can see that we have consumed 23% in our status bar. It shows 23% here in the context window. But most importantly, you can

[04:51] see the token here is inaccurate based on what we see. Can you be able to make sure that this is aligned with how much token that we have consumed in the current context window. So I'm just going to paste this prompt and pass it to the status line right here. And

[05:04] hopefully it should be able to fix this. All right. So now you can see that it has fully fixed. And here you can see

[05:08] that this is the percentage that we have and so far we have used 66k out of 200k and I also ask it to give the entire like what are the field values that you have right? So for example, it has the total input tokens, the output tokens and also the the entire context window size which is 200k and also the use percentage which which is 32 which is what we have displayed here right and then also we have our input tokens and then the output tokens. So the actual context usage here is basically the cash reinput and also the cash creation input tokens plus the input tokens and the output tokens which gives you the entire max of the 32% out of the 200k. Okay. So

[05:46] basically that gives you a calculation for how much tokens that we have used. So you can see here that we get a much more accurate answer based on this. All right. So now in this case I'm just

[05:55] going to open a new terminal and I'm just going to open the another clock session. And here you can see that it has a status inline here or status bar showing inside of our clock code session. All right. So pretty much

[06:05] that's how you can be able to install the status bar inside of your clock code. And how can you do this? And I basically wrote up a MD file here.

[06:12] Simply just pass this MD file to the CLCO session and basically have CLGO here to instruct it and follow that guide to install it, help you to install it without the pain that we just went through. Okay. And I'll make sure to put that doc inside of our community for our Discord channel which is completely free. So right now you can see I have

[06:27] navigated to another computer which is using VS Code for this particular project. And I just basically just referenced this entire path for this MD file. And I'm just going to say, please follow this MD file here to set up the status line bar, which is what I mentioned inside of this MD file. And

[06:43] that's basically my prompt to instruct CLCO here to follow the MD file to set up the status bar. So I'm just going to send this request and let's have clock here to execute this. All right. So now

[06:52] you can see that CLCO has executed everything that we mentioned inside of that document. And here you can see as at the end you can see that this is exactly what we saw inside of the other computer that we just saw, right? So right here you can see we have our opus, we have the bar, we have how much tokens we have consumed. So you don't have to

[07:08] deal with all that. Just pass the document to claw code and let clock here to install it based on the instruction that provided in documentation and have your status bar ready to go right away. And just for testing, I'm just going to stop this terminal session. Clear the

[07:21] terminal and I'm just going to restart my clock session. And right here you can see we have the bar still presents after we restart our clock session as well. So let's say if I want to give it another prompt and try to see if the status line here works. So I have start a uh

[07:36] terminal session for the application and this is what the application looks like. So you can see we have our dashboard right. So basically this is the dashboard view and also we have our transaction and what I noticed that there's a bug is that currently for the uh so I'm just going to first take a screenshot of this and come back to the clock session. paste the image here and

[07:55] I'm just going to say currently inside of the dashboard statements for the transaction table you can see that for the source file column uh if we have a CSV or if we also have a Google Sheets they actually display the same badge and what I want to do here is I want to change the icon for the badge inside of it to have a different badge for Google Sheets or the same badge for CSV or spreadsheet or Excel sheets right so in this case we want to differentiate different file types so can you be able to help me to do that. And that's basically my prompt. And I'm not going to change it to a plan mode. And

[08:28] basically have it to execute. And let's try to see if the status bar here changed. Okay. So, right off the bat,

[08:33] you can see it took 24% of our current context window. And let's try to see how much context is actually consuming for completing this task. Before we jump into the next section, I want to give a quick shout out to today's sponsor, Test Sprite. Testrite is an AI agent built

[08:47] specifically for software testing. And with the release of the Testbrite MCP, you can now use it directly inside your coding IDE. So, cursor, windsurf, cloud code, and more. Setup is super simple.

[08:58] You just add the configuration in your MCP settings, and you're good to go. What I really like about Testbrite is that it doesn't blindly run tests. It first reads through your entire codebase, understands the documentation, and validates the results your AI agents produce. It automatically generates a

[09:13] test plan from your PRD, creates test cases, ensures proper test coverage, and all of that without any manual input. From there, it executes a test and sends detailed reports back to you, clearly showing what's broken and what needs attention. Most coding agents today average around 42% accuracy. But with

[09:30] Testrite MCP, teams have been able to boost feature delivery accuracy up to 93%. So if you're interested in checking it out, you can watch the video I made on it or click the link in the description below for more details. Back to the video. Okay, so now you can see

[09:44] that it has promptly some questions. So should the CSV and Excel files share the same color or would you like them to have different colors? So I would say same color. So same color for all of

[09:54] them including spreadsheet, but it's the only the icon here that needs to change. But CSV, Excel, you can they can share with the same icon. And that's my prompt. And I'm just going to save that.

[10:03] And you can see that we also have our progress bar here changed as well as the amount of token that's changed as well. And then here you can see it gives me a plan. So I'm just going to read over the plan here. So basically differentiate

[10:13] the file type icon in the source file column. So change the source file column in the transaction table to display the distinct icons for Google Sheets versus CSV and Excel sheets. And here let's take a look at the current state. Okay.

[10:25] So this is basically before and after is that it's going to add another icon. So if it's Google Sheets, it's going to change that to the file from spreadsheets. All right. So in this

[10:34] case, I'm just going to click on clear context and bypass permission. So right here, you can see that it has cleared context while clo here is changing the code. All right. So now you can see that

[10:44] the Google sheet has the distinct sheet icon which is different from other icons that we have. Right? So these are all the icon lists that we have here. Okay.

[10:50] So what I'm going to do here is I'm going to navigate back to the uh application here. You can see this is the spreadsheet. Okay. That's pretty

[10:56] good. All right. So now let's say if I were navigate to like CSV data, you can see this is a completely different spreadsheet. So I'm just going to take a

[11:02] picture of this. Come back here. I'm just going to drag it over here. And that's going to be

[11:08] image two. And uh I'm also going to go all the way here. And I'm also going to say take a screenshot of this and take it here. I'm just going to say currently

[11:18] those two icons here looks kind of very very similar. Is there any way that we can differentiate it? My take here is probably using like a uh G or in this case the logo of Google Sheets, right?

[11:29] Try to use that for an example or maybe even better like just use G for Google Sheets or something. Uh maybe trigger the front end of design skill here to have a better design. So that's basically my prompt and let's try to continue use it and see if the progress bar here changed. All right. So as the

[11:46] end result here you can see this is what we got. So it's exactly like a Google logo which you can see right here for the source file. Right. So people can be

[11:53] able to easily differentiate that this is from Google Sheets or at least from a Google file. Right? So in this case we can be able to um have a clear differentiation of that. And if I were

[12:03] to go to the last page you can see that the CSV data here still shows the same. Okay. So which is really cool. So you

[12:09] can see that's how we can complete this right. And so far because every time when I do the plan mode and it clears the context. So right now you can see that we have around roughly around 25% of our context window have consumed. Now

[12:21] you might be wondering why is this helpful? Well, the reason is because we can be able to see this every single time and through that we can be able to see okay well initially when we try to use claw code it actually took up like 25 or 20 or 30% of the initial context window. So what you can do here is that you can be able to take this and ask claw code to investigate it and see why it takes so much context for the initial context usage. Right? So you can see

[12:42] that it has done a investigation on what's contributing for the high initial context usage inside of our clical session. And here's what it has done. So based on the investigation it has found out that the main contributions for the initial constac usage is the following.

[12:56] So you can see for example we have taken about 20K for the uh system prompt which is what we have and also the MCP tool definitions as well as the cloud MD file and also these ones right and simply we can tell cloud to basically generate a plan on exactly what are some MCP servers or what are some things in our system prompt that we can remove to make our initial context window much more shorter because the higher context consumption for the initial prompts the lower the accuracy it is and I think we all know that for the context rod right so in this case that's exactly what I did I basically tell claude hey I want you to generate a plan and basically claude is going to do the investigation on these specific plugins configurations or files that it creates a higher consumption. So you can see that it has spin a multiple sub agent here to do the research analyze the problem here and eventually here you can see it basically prompt me with a question on how aggressive do you want the on the optimization to be and here I'm just going to choose a conservative here to disable like four redundant plugins and keep the called MD file here mostly intact because we don't want to lose any rules that we set in our cloud MD file so I'm just going to enter this and hopefully it should refine this as we go. All right. So as a result here you

[14:00] can see that it basically going to remove these four uh claw coast plugins which here you can see we have our code review typescript lsp and the code simplifier and also the feature dev for the uh cloud settings and also removing the duplication front design which is already duplicates. So it's going to remove that and also here you can see this is what the clot settings look like after it has done. So it's going to remove this duplication uh which should clean up our context window initially for the prompt. And here you can see

[14:29] this is the implementation checklist. So disable the global plugins and also clean the project plugins. And then here initially before we have 13 now and after that we have nine which saves about like 8 to 12k uh for the tokens.

[14:42] So pretty much that's the plan for reducing the initial high context for the context window. So I'm just going to say continue here and it's going to spin up a new session here to basically try to uh complete this job. All right. So

[14:53] now you can see that it has removed this global settings for the four plugins and it should work now. So I'm just going to stop my terminal session and basically start a new clock session and I'm just going to say based on the current uncommitted changes right now can you be able to commit it with a detail commit message and that's my prompt and I'm just going to submit this and let's see how much consumption it takes initially. So currently you can see it takes 23% which is a lot better compared to before because before it was like 24 or 25 roughly. You can see this is how we can

[15:23] be able to clean up our token consumption initially because the lower it is the higher accuracy it gets for the AI right so pretty much that's how you can use it and benefit from it to examine the current context window for the conversation and to see how you can be able to use that to increase the accuracy for AI to producing the code that you want so pretty much that's it for this video and if you do found value in this video please make sure to like this video consider subscribe for more content like this with that being said I'll see you in the next Yeah.
