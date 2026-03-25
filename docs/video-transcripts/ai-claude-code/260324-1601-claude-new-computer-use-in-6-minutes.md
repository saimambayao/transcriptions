# Claude NEW Computer Use in 6 Minutes

**Channel**: Developers Digest
**Duration**: 6:14
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=ZUBJqLGKoZI
**Transcribed**: 2026-03-24 16:01

---

## Organized Notes

**Overview**

- Anthropic released **computer use** capability for Claude, available on both **desktop app** and **mobile app** (via Dispatch)
- Claude can now **see your screen**, take actions with **keyboard and mouse**, controlling your entire machine — not just Chrome browser as before
- Extends the **aperture of what Claude can do** beyond browser-based interactions to native desktop applications
- Available on **Pro and Max plans** only

**How Computer Use Works**

- Claude prioritizes **MCP connectors first** (Slack, Calendar, etc.) before falling back to visual computer control
- If a connector exists for an app, Claude uses it directly; if not, it **asks permission** to interact with the app visually
- This creates a **fallback mechanism**: connector-first, then visual computer control as backup
- When active, a **pulsating orange border** appears on screen edges to indicate Claude is controlling the computer

**Demo: Calendar Task**

- Simple task: "Between 6pm and 7pm, put a note on my calendar to be home for groceries"
- Claude opened the **native Calendar app** (not a web calendar) and added the event correctly
- Minimal instruction needed — Claude figured out the app interface autonomously
- After completing the task, Claude **collapses back** from the small control window to full view

**Demo: Multi-Step Workflow**

- Complex chained task: Open Reminders, add grocery items (pancakes, syrup, butter), then go to Uber Eats, find nearest Target, add those items to cart
- Claude **requested permission** to use the Reminders app, then controlled it directly
- Made a **typo** during entry ("udder" instead of "butter") but was able to **self-correct** by deleting and re-entering
- Successfully navigated to **Uber Eats**, searched for Target, and began shopping for items
- Selected **Kodiak Power Cakes Flapjack Waffle Mix Buttermilk** autonomously from search results

**Limitations and Expectations**

- **Speed**: Computer use is often **slower than doing the task yourself** because Claude must infer from visual screen content
- **Non-deterministic**: Claude has to **figure out each application's interface** as it goes, which causes stumbling
- **Error-prone on new apps**: First-time interactions with unfamiliar software require Claude to learn the UI before executing
- **Course correction**: Even when errors occur, Claude can **detect and fix its own mistakes** by re-reading the screen
- **Early days**: The pieces and infrastructure are there, but maturity is still developing

**Dispatch Integration**

- From your **phone**, you can control your entire computer using Dispatch + computer use
- Claude can send **screenshots back to the phone app** for verification
- Works "very seamlessly" with the Dispatch feature according to the presenter

**Comparison with OpenClaw**

- The presenter asks whether users will **replace OpenClaw** with Claude's computer use or use them **in combination**
- Positions Claude's offering as a direct competitor to OpenClaw for desktop automation

---

## What This Means for Your Work

This short demo validates a pattern you've already encountered in the longer WorldofAI tutorial (transcript `260324-1219`): Claude's computer use is a connector-first, visual-fallback system that works best for simple deterministic tasks but slows down significantly on multi-step workflows requiring UI exploration. The Developers Digest perspective adds a practical speed reality check — for most individual tasks, you'll be faster doing them yourself.

**Where this matters for you:**

- **OOBC workflow distribution**: The connector-first fallback pattern reinforces that packaging your legislative skills as Cowork plugins with MCP connectors (Slack, Google Drive, Notion) is the right path for Prof. Noron Andan's team. Computer use should be the last resort, not the default interaction pattern.
- **e-Bangsamoro portals**: Computer use has no direct application for your React 19 + DRF platform development. Your development workflow (Claude Code CLI + parallel agents + frontend-first) is far more precise than visual screen control.
- **Training content for MoroTech**: The "it's often faster to do it yourself" reality check is valuable framing for your SEED Initiative training modules. When teaching non-technical users about AI automation, lead with connectors and skills — not computer use demos that set unrealistic expectations.
- **BTA Parliament operations**: For staffers who need to move data between government systems that lack APIs, computer use could automate repetitive copy-paste workflows (e.g., transferring resolution data between PDF viewers and document editors). But only after MCP connectors and Zapier integrations are exhausted.

### How This Can Improve Your Claude Skills and Workflows

**Existing skill refinements:**

- **/webapp-testing** — Your Playwright-based testing skill is more reliable than computer use for web app validation. This video confirms computer use is non-deterministic on unfamiliar UIs, reinforcing that Playwright's programmatic selectors remain superior for your e-Bangsamoro testing pipeline.
- **/devwork** and **/frontend** — No changes needed. Your frontend-first development workflow operates at the code level, not the visual level. Computer use doesn't compete with CLI-based development.
- **/training-assistant** — Add a "realistic expectations" section to training packages about AI automation. Frame the capability hierarchy: skills/commands (fastest, most reliable) > MCP connectors (fast, API-level) > computer use (slow, visual, error-prone). This maps to the Developers Digest presenter's observation that "it's going to be faster for you just to do the task."

**Workflow implications:**

- Your **parallel agents** architecture (dispatching 7+ agents for batch operations) is categorically more efficient than computer use. This video reinforces that computer use is for single-user, single-screen tasks — not the programmatic batch operations you excel at.
- Your **Obsidian vault + Claude Code** setup doesn't benefit from computer use at all. The file-level Read/Write/Edit tools are infinitely faster and more reliable than visual screen navigation.

**No new skill recommended** — this video covers the same capability as the WorldofAI transcript already in your library, just from a shorter demo perspective. The key new signal is the speed expectation management, which is a training content insight rather than a skill requirement.

---

## Transcript

[00:00] Anthropic has just released the ability to control your computer. Now, this is available both from the desktop app as well as from the mobile app. Now, one of the really cool things with this is they released Dispatch last week. And what

[00:13] this will allow you to do now is from your phone, you can actually control your entire computer. How this works is it's going to be able to see your screen. It's going to be able to take actions with your keyboard as well as mouse. And effectively now instead of

[00:27] just actually being able to control your Chrome browser like they had previously, now that same type of capability is extended across your entire machine. Now the capabilities of this really extend to be basically whatever you can imagine. And one of the really neat things with this is you can also ask it to send screenshots directly to the Claude app when you're leveraging this from the dispatch feature. So there's

[00:50] all in all a ton of different use cases. They demoed some within the video like cropping photos, editing photos. All in all, this is the type of capability that just furthers the aperture of what Claude is able to do. Okay, now for a

[01:02] quick demo. In order to get started with this, just make sure that you do have the latest version of the desktop app installed. And if you are going to be leveraging it from your phone, just make sure that you also have the update on that as well. On the left hand side,

[01:12] we're going to have this dispatch feature. Now, the first time that you go in here is you're just going to have to make sure that you pair it with your phone. It's going to ask for some permissions as well. Now, additionally,

[01:21] you do have to go into the settings and actually enable that computer use feature. And the one thing that I do want to note for people that are interested in leveraging this is it is going to be available on the pro and max plan. Now, how it will work is if you have connected apps like they have through their connectors, whether it's Slack or calendar, so on and so forth.

[01:38] What it's going to do is first it's going to try those connectors and if those connectors aren't there for the tool that you need, it's going to ask for your permission when you want to interact with different apps that are outside of those connectors. Effectively how this works, it's sort of like a fallback mechanism. If you try and say leverage Slack or integrate with Slack first, it's going to try the connector.

[01:56] But if you don't have that connector, it's going to fall back to your Slack application. For instance, what I'm going to say within here is between 6 p.m. and 7:00 p.m. put a note on my

[02:04] calendar in the calendar on my desktop app. I want to have a note to be home for groceries. So, this is what it looks like. When you're using it, what it's

[02:11] going to do is it's going to have this pulsating effect where on the edges of your screen, you're going to have this orange effect. Now, what we can see within here is it went and it opened up the calendar app and it added for the date today to be at home for groceries without having to really give too much instructions. It was able to just go and do that task. Now, the one neat thing

[02:30] with this is it's one thing to actually have these one-off tasks like this, but it's a whole other thing when you stitch these things together. And then as soon as it's done that task, it's going to move away from being that smaller window like we saw on the right hand side there. And then it's going to expand back out to the full view. Okay. So next

[02:44] I want to show you is how you can begin to create workflows based on whatever you can do across your computer. So for a quick demonstration, what I'll say here is open up my reminders application and within my grocery list, let's add pancakes, syrup, as well as butter. Once those are added, let's go to Uber Eats and then let's find the target that's nearest to my location and then let's select all of those different items and add them to my basket. Let me know when

[03:10] everything is in the cart. I'll take a look and once it's ready, I'll go ahead and I'll check out. Okay, so now I see Claude wants to use my reminders. I'll

[03:17] go ahead and say yes, you can use reminders for this session. And then just like we saw before, it will open up the application for us and it will do that pulsating effect again. Now, the one thing that I didn't notice with this is it doesn't actually show you each of the individual steps of the agent going and trying to figure out the application. That's one thing that I

[03:34] often do actually like is seeing that feedback of if the agent is trying to do something. Okay, and here we go. It's actually going through. It went ahead

[03:41] and it started to add an item. I see the syrup. I see the udder. So, it did miss

[03:46] the B there, but it was able to quickly iterate through the list. Now, the one thing to know with this is since it does see the visual portion of my screen, I would assume that it can go back and actually fix all of those different errors. The one thing that I do want to highlight with this that it doesn't exactly show in the video is it does take a little bit of time. So, one of

[04:05] the things that I do want to manage expectations on is if you do think that this is going to speed up a particular workflows and you're just going to be able to instruct Claude to do something, often times it's going to be faster for you just to do the task because it is going to have to do the inference on what it sees on the screen where in this example for instance, it made an error and it has to go and course correct. For things like that, especially with things that are non-deterministic and it does have to figure out that software as it's going through and figuring out the task is often times is it will stumble a little bit. And that's one of the things with these types of agentic systems, especially when it's trying a new application or a new website or what have you, is it will have to figure out how to actually leverage the website before it goes through and figures out all the things that it needs to do. But

[04:49] the one neat thing with this is even when it does make mistakes, it's able to course correct. I can see syrup. I can see butter. And the typo that it had, it

[04:58] went ahead and it deleted it. Now, on my second screen here, I can see it navigated to Uber Eats. It's searching for Target. Now, it successfully loaded

[05:04] the Target page for us. And now, we can see it's beginning to shop for our grocery list, but searching for pancakes on Target. And then within here, it's going to be interesting to see which pancakes it decides to actually pick out for us. So, it's went ahead and it's

[05:17] selected the Kodiak Power Cakes Flapjack Waffle Mix Buttermilk for us. And I'm not going to show you the rest of the video actually seeing if it goes through and successfully goes through the whole grocery list. I'm going to make the assumption that it can actually do this task quite well. Now, the one thing that

[05:32] I really want to emphasize with this is it definitely is early days, but it is a glimpse in terms of where we're going. I think all of the pieces are there. We have the infrastructure. This clearly

[05:41] works. I was playing around with this on my phone earlier and it does work very seamlessly with this dispatch feature. So, all in all, I just wanted to take a really quick look at this new capability. I think a ton of people are

[05:52] going to be excited about this feature and I'm really curious what different workflows that you are going to be leveraging this for as well. And one thing that I am curious for those that leverage OpenClaw is are you going to be leveraging this instead of something like OpenClaw or are you going to be leveraging it in combination? Let me know in the comments below. But

[06:09] otherwise, if you found this video useful, please like, comment, share, and subscribe. Otherwise, until the next
