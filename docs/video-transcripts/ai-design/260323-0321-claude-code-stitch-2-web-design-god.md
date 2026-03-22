# Claude Code + Stitch 2.0 = Web Design GOD

**Channel**: Chase AI
**Duration**: 13:02
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=qqcpiDXPCvY
**Transcribed**: 2026-03-23 03:21

---

## Organized Notes

**The Core Workflow: Stitch + Claude Code**

- **Stitch handles frontend design** (Claude Code's weak point), then export code to Claude Code for implementation
- Stitch is **free**, powered by **Gemini 3.1 Pro** under the hood
- The workflow: find inspiration → Stitch → iterate on canvas → export code → paste into Claude Code
- Gets you an **80-90% solution** with zero token usage in Claude Code — then refine from there
- Figma stock **dropped ~8%** after the Stitch 2.0 announcement

**Finding Design Inspiration**

- Don't start with a blank prompt — find a reference design first
- Best sources for inspiration:
  - **Dribbble** (three B's)
  - **Godly.website**
  - **Pinterest** — great UI for searching landing page designs, easy to find related ones
- Take **screenshots** of designs you like, or grab the **website URL**
- Feed the screenshot/URL into Stitch as a style reference

**Stitch's Design System (The Secret Weapon)**

- Stitch auto-generates a **design system** from your prompt + inspiration — you don't have to ask
- Includes: primary/secondary/tertiary colors, typography, corner radius, buttons, labels, search bars
- The **design.md file** is the real gem — a complete guiding document with:
  - Creative northstar and overview
  - Color strategy
  - Typography rules
  - Language about **breaking away from standard templates** (avoiding AI slop)
- The design system + themes are the **bedrock** for all generated frontends
- Easily customizable: change seed color, font, corner radius directly in the UI

**Iterating on Designs**

- **Infinite canvas** — everything visible on one page, like Midjourney for web design
- Right-click any design to **regenerate** or create **variants** (layout, color scheme, images, or custom)
- Set **creative range** (conservative to explore) and number of options (2-4 at once)
- Much faster iteration than doing this in Claude Code (no dev server, no tab switching)
- **Edit mode**: click individual components to modify them directly
- **Preview mode**: open full-screen in a new tab to see the real experience
- **Live mode**: screen-sharing with Gemini for voice-driven real-time edits (e.g., "add cursor motion to the background")
- Pro tip: use **NanoBanana Pro** to extract/edit images from screenshots, then bring edited images back into Stitch

**Exporting to Claude Code**

- Click the design → **More → Export → Code to clipboard**
- Paste into Claude Code with a prompt like "Create me a landing page, here's the frontend code"
- Claude Code builds a working page in **~60 seconds** from the exported code
- Result is a **great base** — purely frontend, not connected to backend yet
- From there, refine with tools like **21st.dev** for fancier components

**Why This Matters**

- Agentic coding tools (Claude Code, Antigravity, Codex) are **weak at frontend design** — everything looks "samey"
- Even with skills like "Frontend Design Tool" or "UI/UX Pro Max", Claude Code's visual output **leaves something to be desired**
- Stitch fills the design gap for people who aren't professional designers
- **Figma is overkill** for most developers — "a bridge too far"
- Deployment is still the same: push to **GitHub → Vercel**

---

## Transcript

[00:00] If I wanted to build a beautiful website today, I wouldn't start inside of Cloud Code. Instead, I would start here. The brand new Stitch 2.0 from Google. Now,

[00:10] Stitch just got a huge update yesterday to the point that Figma stock dropped almost 8% because of it. And that's because it gives us a free and effective way to show up one of the only weak points of cloud code, front-end design. Now, Stitch isn't replacing Claude Code.

[00:26] It's something we're going to use with clawed code. And by doing so, we are going to have a workflow that allows us to consistently create high quality websites with AI that don't look like AI slot. And in this video, I'm going to show you exactly how it works, how to get the most out of it, and how to integrate it with cloud code. So,

[00:45] Stitched allows us to create highquality front-end design mockups for our web apps and our mobile apps. And again, it's completely free. It's powered by Google. We have Gemini 3.1 under the

[00:56] hood, which is great at front-end design work. And again, this is kind of a weak point of cloud code. Even when we use things like the front-end design tool or the UIUX Pro Max skill, it leaves something to be desired. On top of that,

[01:09] when it comes to doing front-end design and visual work in general, I think having a canvas like this where I can see everything on one page where I can very quickly take a look at prototypes and how it looks is a huge value ad. Right? On top of that, it's really easy to edit here inside of Stitch. I just

[01:25] hit the edit button. I can deal with individual components. I can edit the layout at large. I can regenerate the

[01:31] layout completely two, three, four times at once. So, what this allows us to do is essentially speed up the entire design process. Because if you do this inside of cloud code, you know, it can be kind of laborious where even if I'm using all the skills, even if I'm throwing it screenshots, right, we're having it generate, spin up the dev server, switch between tabs, and at the end of the day, you'll still have to do that at the end. But if we can get an

[01:57] 80% 90% solution here inside of Stitch, well, why wouldn't we? Especially if it's free. And we're able to get that 90% solution because we can export whatever we build here as code, right? I

[02:08] can come up here. I go to more. I can view it as code. I can export it. I have

[02:13] options to send it to the AI studio, Figma, Jules, whatever. Simplest is just to put the code on a clipboard and then head to Cloud Code. Right. So, this is a

[02:23] great addition to our web design process. So, speaking of Cloud Code, a quick plug from our sponsor today, yours truly. I just released the cloud code master class about a week and a half ago and since then I've already updated 20 plus modules at an additional hour of content. So if you're trying to go from

[02:39] zero to AI dev definitely check it out. It's inside of Chase AI plus. There's a link to that in the comment. And if

[02:45] you're just all new to AI, I also have the free Chase AI community link to that in the description. So tons of resources no matter where you are in your journey. So back to Stitch. You understand the

[02:54] value prop at this point. It helps us with one of the weak points inside of Claude Code and it does it in a free manner. So why wouldn't we? So, how do

[03:00] you actually use it, right? What's the actual workflow here? So, it's pretty straightforward. We're just going to

[03:04] head to Stitch, and I'll put a link to that down below. You can just Google Google Stitch. And it's just a chatbot interface like the same one you've been using since the beginning of time, aka the end of 2022. We just describe what

[03:16] we're trying to build. Now, it breaks it down by app or web app. So, if you're doing a website, obviously you'll be doing web. And then we have the options

[03:22] of what sort of models we want to use. So, really, you have the option of three flash and 3.1 Pro. Obviously, if you can

[03:29] use 3.1 Pro, that's what I would stick with. It's a little bit slower, but it's its frontier model versus 3.0 Flash,

[03:34] which is, you know, a few months old at this point. Now, we also have the ability to upload files or add a website URL because one of the best things we can do when it comes to web design is give it some inspiration, right? I can just talk to it in plain language to give it some crappy prompt and hope it figures it out, but why don't we go find a website we actually like? And there's

[03:52] a bunch of places to help you find inspiration. We have Dribble, that's with three B's. You can go somewhere like godly.ebsite or where I've been

[03:59] really going lately, which has some good ones, is Pinterest, right? Pinterest actually has a great user interface when it comes to searching for landing page design because if you find one you like, like this one that you just saw a couple minutes ago, well, it's very easy to find some additional ones as well. And so, what I think you should do is go to one of those three places, search for something that speaks to you, and then take screenshots of it. or if you

[04:23] already have a website in mind, go grab the website URL because what's going to happen is we're going to take screenshots of what we find. And I'll be using this one today. We're going to go back into Stitch and we're going to put in the screenshot. We're going to say,

[04:35] "Hey, I want you to create a landing page that looks just like that screenshot. Let's see what you got." So, I took a screenshot of this one right here. And

[04:44] alls I said was, "Create a landing page for my AI agency, Chase AI, in the style of the screenshot. I want the exact same hero page setup as seen in the screenshot." Now, it's not going to do a one for one because what's going to happen is it's going to scene the screenshot and then it's going to use Nano Banana on the back end to essentially create a screenshot that mimics it as the image as you'll see.

[05:05] But that's pretty much it. You can add more to the prompt if you want to, but I'm going to show you why even if you have a really bland poor prompt like this one, you actually get a pretty good output. So, let's see what happens. So

[05:16] right away you'll see the screenshot here on the canvas and this is like an infinite canvas that goes everywhere forever like kind of like nad. Um we can see here on the bottom left you have an agent log where you can see what commands you've given it. We can kind of see the thinking going on in the model down here. And the first thing I want to

[05:33] draw your attention to is this. This is essentially the design system. Now what is the design system? Well, the design

[05:41] system is essentially the set of rules that Stitched aka Gemini is going to be using when it creates your web page, right? What are the primary colors, the secondary colors, tertiary, neutral? What are we doing for labels, buttons, search bars, text, all that, right? All

[05:57] the conventions for how it's going to build your front end are right here in one place. And so if we come over here on the right and you see this little button that says design system. If I click on this and we'll move over here.

[06:09] We can see our design system which it is named Obsidian Ember. And if I click on this, well, we pretty much see a copy of what's here visually, right? Our seed color. I can very easily change this. I

[06:21] can change the font. I can change the corner radius, right? How do you want your uh do you want rounded corners? How

[06:26] rounded do you want them? But let's take a look at the design. MD file. Now, I'm

[06:31] going to copy this over so it's a little easier for you to see. So, here's a look at that design system document that I just copied over. What Stitch aka Gemini does is it takes your bad prompt and whatever inspiration you give it and it turns it into this essentially the guiding document for how it's going to create your front end. And it's very

[06:48] well put together. Like, first of all, it has the overview and the creative northstar. It specifically has language about how it breaks away from standard templates aka how do we get away from AI slop aka what cloud code will give you normally and then it goes into colors color strategy typography right this is really well done and you don't have to ask for this at all it just creates it on its own and so these two pieces the design file and then the actual themes itself are essentially the bedrock for how it generates your front end let's take a look at what it gave us so is this a for one copy. Not exactly, but

[07:24] you can kind of see what it was working with, right? So, we kind of have that same like red bar coming down. We have the text on top. The sort of the big

[07:33] numbers of 50 plus versus 10x are kind of off to the side. But you can see it also started to do things on its own, right? I didn't give it anything about core capabilities or kind of what I want at the bottom. And it already generated

[07:44] it, right? And this is pretty solid and I do like how the colors work. But let's say right away I was like, nah, I don't actually like this. If I just click on

[07:51] this and then I right click, I can go to regenerate and it'll just redo it again. Or I can go to varants and you can do variance of layout, color scheme, images, right? You can actually do different variations of specific parts or you can do custom. Right? If I hit

[08:06] custom, I can give it different creative range. This is also very reminiscent of sort of majourney honestly. But we'll do explore and we'll see say I want three different options and I want all the aspects to vary. Right? Again, I ask

[08:20] you, what would this look like if we try to do the same thing inside of Cloud Code? It would take a bit longer. And so, this buys us a ton of room to iterate, iterate, iterate, and really get our creative vision kind of locked on. Now, also, in terms of editing, and

[08:34] there's actually a whole lot to do in Stitch, so I totally suggest you actually just like play around with this. If I come over here on the right, if I hit this little pencil, I can directed. So, I can click on individual components, kind of like what you saw before. I can also hit up over to the

[08:46] top for preview. I can open it up in a new tab. And so we can very easily scroll sort of full screen and on and on and on. There's a ton we can play around

[08:54] with here. So here's some more variations it gave us, right? You know, totally different vibes, which I think is great, right? I think visually you

[09:01] just kind of need to see a bunch of things to like, I actually like that. Now, what you might be thinking at this point was like, "Hey, Chase, I actually found a sick picture of something inside of Pinterest and it's just not giving me the exact thing." understand what you could also do at this point is if I took this screenshot and I brought it into something like NanoBanana Pro and I said, "Hey, give me this exact background, take out all the text." I

[09:21] can then bring that edited image back to Stitch, right? And then say, "Hey, use this as the background image, right? We we can do a lot here." And also, if you

[09:30] want to edit certain things, so let's say now I wanted to edit this one. If I just click on these different, you know, different variations, you'll see here on the bottom of the page, it will add them as essentially references. So, you know, it it's pretty easy to let Stitch know which one you're actually trying to mess with. And the last thing I'll say is

[09:49] there's also this like live mode. So, if I click live mode, it's actually now looking at my screen and I can actually have like a conversation with it. That's incredible. It's so exciting.

[10:03] What are we thinking of creating today? >> Yeah. Can we uh add some like motion to the background of this uh landing page?

[10:11] I'm I'm talking about some like cursor motion. Maybe some like light graphics. I don't know. Kind of just go crazy with

[10:16] it and let me see what you come up with. >> Which Chase AI landing page do you want me to modify? >> Uh the one I'm looking at on it. I'll add a dynamic and energetic

[10:28] background with light graphics and subtle cursor effects. >> All right. So, you know, hey, take from that what you will. I don't know how

[10:36] good that actually is. I don't know what model actually powers their live mode, but just kind of a funny thing they added there. We'll see what it comes up with. And here's what it came up with

[10:43] the motion graphics, right? You can see, might be kind of hard to see on your computer, but it has like these little dots in the background that move away from my mouse as it moves. So, pretty cool. Now, once you got something you

[10:55] actually like, now we can export it into cloud code. So, all you have to do is click on it. And to export it, you're going to go to more. You're going to go

[11:02] to export, and we're going to do code to clipboard. We'll hit copy. Then I hop inside of Cloud Code, and I just said, create me a landing page for my AI agency. Here's the front-end code.

[11:13] Pasted it in there. We're going to let it go to work. So, after about 60 seconds, Claude Code gave us this.

[11:18] Honestly, looks pretty solid. Again, this is just purely the front-end design. This isn't connected to anything on the back end, but this is a great base to start from, right? Do I

[11:29] necessarily love the image of these clouds? No, not really. Am I in love with this? Would I rather have some sort

[11:33] of like motion thing? Sure. But again, 80% 90% solution. None of the token use

[11:39] was done inside of cloud code. And I got something that looks pretty decent, right? If I was doing this purely with like the front-end design tool, as many of you have, you know, it's not the best. It all looks very sy. And now that

[11:50] the foundation is set, I can hop into things like 21st.dev, right? Start playing around with things like the buttons, get a little more fancy with kind of what's going on. But

[11:59] like this is a great starting point. So we really just touched the surface of what you can do inside of Stitched and sorted this workflow of inspiration into Stitch into Cloud Code before creating your final website. We didn't even really touch on deployment, although if you take a look at any of my other web design videos, you will see me go through that. Very simple. pushing the

[12:17] code to GitHub and then into Verscell. But I just really wanted to focus on this brand new tool because I don't think it's a surprise that like I said Figma's stock dropped like seven or eight%. Because for most of us, we're not professional web designers, right?

[12:31] Jumping into something like Figma is still like a bridge too far. But what this was able to create again just like the most basics of pro basic of prompt in a screenshot is should impress you. Again, Claude Code is amazing, anti-gravity is amazing, codeex is amazing, but a lot of these agentic coding agents miss out on front-end design, and this kind of fills that gap.

[12:52] So, we should all be excited. So, as always, let me know what you thought in the comments. Make sure to check out Chase AI Plus if you want to get your hands on that cloud code master class and I'll see you
