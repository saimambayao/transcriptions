# Claude Code + New Stitch 2.0 = UNLIMITED $10,000 Websites

**Channel**: Jack Roberts
**Duration**: 17:22
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=1aI7pAlkz4w
**Transcribed**: 2026-03-23 03:23

---

## Organized Notes

**The Full Pipeline: Stitch + Claude Code + Antigravity**

- Complete workflow from **ideation → design system → build → deploy**
- Stitch handles visual design (Claude Code's weak point), then exports to Claude Code for implementation
- **Stitch MCP integration** connects directly to Claude Code / Antigravity — can read your Stitch designs, fetch HTML, extract design tokens
- Deploy straight to **GitHub + Vercel** from Claude Code / Antigravity

**Stitch 2.0 Key Features**

- **Ideation mode**: ask Stitch to research and find top websites in any niche, then generate 3 design options based on what's working
  - Provides deep strategy docs: typography, interactions, color palette, design tokens
  - Think of it as a **"sniper" approach** — thoroughly researched before generating
- **Redesign mode**: leverages **Nano Banana 2** to generate gorgeous concept art images as reference points
  - Generates an image first (not code) — better quality reference than trying to code directly
  - Drop in any URL or screenshot, get a redesigned version
  - **15 redesign credits per day** (rate-limited during rollout)
- **Direct text editing**: click on any element and edit text inline without reprompting
- **Canvas annotations**: draw, add notes, mark up designs directly on the canvas
- **Parallel queries**: multiple design requests can run simultaneously — no queueing
- **App vs Web toggle**: choose mobile app or desktop web format on the homepage

**Stitch MCP Setup**

- **Antigravity**: Settings → MCP Service → search "Stitch" → Install → paste API key
- **Claude Code / VS Code**: run `claude mcp add` transport command (linked in video description) → paste API key
- Get API key from Stitch API key page
- Once connected, Claude Code can **read your Stitch designs** directly — ask "what was the latest design I created?" to verify

**The Design.md Workflow**

- After designing in Stitch, ask Claude Code: "Create a design.md based on those designs"
- Claude calls Stitch MCP → lists screens → fetches HTML → extracts design tokens + project metadata
- Produces a **design blueprint** with: visual theme, color palette, typography, atmosphere, spacing
- This design.md enables **style replication** — create new pages in the exact same style
- Can spin up unlimited pages/sites with **consistent branding** just by referencing the design.md

**Skills Available via Stitch MCP**

- **Design MD**: scan any project to get a design architecture blueprint
- **Stitch Loop**: autonomous multi-page generation — Claude builds one screen, passes a baton file to itself to complete the rest
- **Enhanced Prompt**: improves quality of design prompts for websites/apps
- **Shadcn UI Bridge**: converts Stitch designs into Shadcn components with best practices
- **Remotion**: generate walkthrough videos from Stitch screens with zoom effects

**Practical Workflow for $10K Websites**

1. **Ideate** in Stitch — research competitors, generate 3 design directions
2. **Pick and refine** — edit text, regenerate sections, annotate canvas
3. **Redesign** with reference images/URLs for elevated visual quality
4. **Extract design.md** via Stitch MCP through Claude Code
5. **Build pages** — Claude Code generates code matching the design system
6. **Replicate** — use design.md to spin up additional pages/sites in the same style
7. **Deploy** — push to GitHub + Vercel directly from Claude Code

**Key Insight: Image-First Design**

- Nano Banana 2 generates **concept art images** rather than trying to build code directly
- This produces **better quality references** than code-first approaches
- Think of designs as **"concept art that captures the essence"** — then implement from there

## What This Means for Your Work

**The Stitch MCP integration is a game-changer for your Claude Code workflow.** Jack Roberts demonstrates that Claude Code can directly read your Stitch designs, fetch HTML, and extract design tokens through the MCP connection. For your 9 platforms, this means you no longer need to manually copy-paste exported code. Set up the Stitch MCP once in your Claude Code environment, and your /stitch-design skill can programmatically pull designs from Stitch, generate a design.md, and build pages -- all within the terminal workflow you already use daily.

**The design.md workflow for style replication solves your multi-platform branding challenge.** You are maintaining consistent visual identity across e-Bangsamoro, e-Negosyo, MoroMarket, Tarbiyyah-MS, BangsamoroHR, SBP, OBCMS, Parliamentarian, and IPP. Roberts shows that once you extract a design.md from Stitch, you can spin up unlimited pages in the exact same style. Create one authoritative design.md per platform, store it in each project root, and every new page Claude Code generates will inherit the correct visual theme, color palette, typography, and spacing automatically.

**The ideation mode -- researching competitors before generating designs -- applies directly to your government platform work.** Before designing the e-Negosyo cooperative marketplace, you could ask Stitch to research the top 3 cooperative/marketplace platforms globally, then generate 3 design directions based on what works. This gives you evidence-backed design decisions to present to MoroTech stakeholders and SEED Initiative partners, not just AI-generated guesses.

**The Stitch Loop skill for autonomous multi-page generation addresses your biggest bottleneck as a solo dev.** Building 9 platforms means hundreds of screens. The Stitch Loop lets Claude build one screen, pass a baton file to itself, and complete the rest autonomously. For a platform like Parliamentarian that needs screens for session management, bill tracking, voting records, and committee assignments, you could design the first screen in Stitch and let the loop generate the remaining screens in the same style while you work on backend logic in a parallel Claude Code session.

**The GitHub + Vercel deployment pipeline Roberts shows is your exact production workflow.** You are already pushing React 19 to GitHub and deploying. The value add here is that the entire pipeline -- from Stitch ideation through Claude Code implementation to Vercel deployment -- can now be orchestrated from a single Claude Code session with the Stitch MCP connected. This reduces the context-switching overhead that slows down solo dev work.

### How This Can Improve Your Claude Skills and Workflows

**The design.md workflow should be codified as a standard output of your /stitch-design skill.** Roberts demonstrates that the design.md -- containing visual theme, color palette, typography, atmosphere, and spacing -- is the bridge between Stitch and Claude Code. Update /stitch-design to always generate a design.md as its final artifact, stored at each project root (e.g., `e-bangsamoro/design.md`, `moromarket/design.md`). Then update /frontend-design to check for and read this file at the start of every invocation. This creates a seamless skill chain: /stitch-design produces the blueprint, /frontend-design consumes it -- no manual copy-paste, no style drift between sessions.

**The Stitch Loop concept (autonomous multi-page generation with baton files) maps directly to a new skill: /page-generator.** For a platform like Parliamentarian that needs 15+ screens (session management, bill tracking, voting records, committee assignments, member profiles, attendance, plenary agenda), you could build a skill that takes a design.md plus a list of page specifications, generates the first page, creates a baton file with design context and completion state, and autonomously generates remaining pages. This is especially powerful when run as a parallel agent -- one agent handles the page loop while you work on Django backend models in another session.

**Your /brand-guidelines skill should be updated to consume and produce Stitch-compatible design systems.** Roberts shows that once you have a design.md, you can replicate the style across unlimited pages and even entirely new sites. For MoroTech, this means your /brand-guidelines skill should output design tokens in a format that both Stitch and Claude Code can consume. When a new platform like IPP needs to be bootstrapped, invoke /brand-guidelines to generate the MoroTech-compliant design system, feed it to Stitch for visual exploration, then extract the refined design.md back into Claude Code for implementation.

**The Stitch MCP setup process Roberts walks through should be documented in your /stitch-design skill's reference files.** The `claude mcp add` transport command, API key configuration, and verification step ("what was the latest design I created?") are one-time setup steps that you will forget in 3 months. Embed them in the skill's `references/` folder so that when you set up a new development environment or onboard a MoroTech collaborator, the skill itself contains the complete setup guide. This is the kind of operational knowledge that belongs in your skills-bucket for portability to other AI agents.

**Cross-pollination opportunity with /research-pipeline and /notebooklm: the ideation mode Roberts demonstrates is a research workflow.** When Stitch researches the top 3 websites in a niche before generating designs, it is performing competitive analysis -- the same function your /research-pipeline skill handles for policy documents and legislative analysis. Consider creating a /design-research variant that feeds Stitch's ideation output (competitor analysis, design token comparisons, typography choices) into NotebookLM as a source, alongside your existing governance research. This gives you a single knowledge base that connects design decisions to policy requirements -- useful when explaining to BARMM stakeholders why a particular interface pattern was chosen.

---

## Transcript

[00:00] Imagine if you could combine Claude Code with Google's number one design agent, Stitch. This brand new update lets you turn Claude Code into an AI design agent that can research, ideulate, and build beautiful apps and websites without the need to be a design expert, but only if you know how to do it properly. So, in this video, I'm going to show you exactly how to combine Stitch with Claw Code and anti-gravity so you can build beautiful designs faster than everybody else and get light years ahead of your competitors. And if you don't know who I

[00:29] am, my name is Jack Roberts. I'm in the UK right now, but I built and sold my last tech startup with over 60,000 customers. And now I run a very profitable AI automation business. So if

[00:38] you haven't already, grab that coffee and let's dive straight in. Now Stitch is Google's number one design agent. And when you combine that with Claude Code, you unlock very cool new capabilities.

[00:50] You can build beautiful websites and wonderful, gorgeous apps. Now, Stitch is all about designing visually. We can build beautiful websites through prompting through different strategies we come from a channel. But the idea of

[01:01] Stitch is that you can visually see things, edit them and generate them from a visual point of view. There are also so many new features that have just come out. It is now powered by the world's best design model, Gemini 3.1. It can

[01:13] find ideas for you. You can basically say to it something like, "Bind me." As you can see right here, for example, find me the top three websites, the top three coffee websites on the planet. and

[01:22] then it will design you on based on what they have, their images and exactly everything that's working for them. You can edit text dynamically. So you you no longer have to say hey do this, do this.

[01:32] You can within the visual interface edit a text and information there. Now you can do this within cloud code and also anti-gravity in an unbelievably easy way. Your agent will actually enhance a design prompt that you wouldn't normally get just using stitch by itself. You can

[01:47] build these programmatically. In other words, as many as you want to for your specific brand guidelines. You can edit screens. You can generate different

[01:55] variations. You can even achieve visual consistency across all of your designs within Stitch. And with anti-gravity, it is as simple as a one-click install. And

[02:04] we also have several new skills with the Google official MCP. We have also a design MD that will scan any project that we build to get a design architecture, a design blueprint that we can replicate across anything. Of course, we've got the stitch loop, which allows you essentially to build out multiple screens for your app, your website without you even having to be involved in the entire process. The

[02:27] stitch loop, if you don't know, is just autonomous multi-page generation. Claude builds one screen. It almost passes a baton file to itself to go and complete the rest of them. We've got enhanced

[02:36] prompt, which will improve the quality of the prompt for your websites and apps. We've got shading UI that bridges stitch designs into shadow components with the best practices based in. And then we've got remotion if you want to, you know, walk through video from stitch screens with zooms. Ultimately though,

[02:51] we have a full pipeline from ideation design system build and then deploy. Now to get the most out of this connection between stitch and claw code and anti-gravity, I'm first going to explain some of the brand new features that exist within stitch. And when we understand that, we can take your designs, your websites, and your apps to a completely new level. Now, when you

[03:10] come over to stitchwithgoogle.com, our journey begins. Now the first new feature I want to put on your radar cuz it's very cool is this idea of ideation.

[03:18] So to do this you're going to come down here to ideulate. Okay so you can click on this. Now of course you can always ideate with the model. This just makes

[03:24] it in my view easier and it's a little bit more visual. So I could say something like hey there I'm looking to start my own SAS. What I'd like you to do is do some market research and find out three SAS companies. Give me three

[03:35] different designs for a SAS pricing page. Again it could be anything. It could be give me three different ideas for I don't know, you know, what color scheme should I have for my business? My

[03:45] business is about ABC. So, think of this as a place to throw out your ideas, your questions. If you're thinking, you know, I kind of want to design for this thing, but I'm not really sure what it should look like, feel free to spitball and ideate. Direct conversations with models

[03:59] aren't amazing at this normally. Because the cool thing about Stitch is it will throw back at you three different designs that you can then pick, select, and go deeper with. Then once you've done that, basically we'll come back with three different options. The

[04:10] minimalist utility inspired by Stripe notion. And so I'm going to say, "Dude, they all sound great. I would like all three. Please just generate me three

[04:16] different visuals for me to choose from." And so now we've asked it to proceed. It's come up with three different strategies. It's done all the

[04:22] research, which is wonderful. You can come down and take a quick look at everything it said. Typography, interactions, ROI, calculator. Look at

[04:27] the level and depth it's got here, guys. Really, really cool. So, what we're going to do is I'm going to go ahead and say, "Hey, sounds great. I'd like to

[04:32] design um an example for all three of And what we want to do as well is just highlight all of them like so. So all three are selected. Then click off and send it off. Remember, you might want to

[04:41] wait a few minutes. Well, it goes ahead and and does this. This is more of a think of it as a sniper. You're really

[04:46] trying to get something decent and some of quality that's been thoroughly researched with a very clear strategy. I mean, even if you click into this one for example, right? Product overview for designing directions, screens, key workflows, use it as on a plans overview, color palette, typography, all very very cool design tokens. It's gone

[05:01] into a lot of specifics to help the model gauge to build something really cool. And just like that, based on all the design guidelines, we have three different options. We've got this pink and black one, which is pretty cool, right? Look at this. We've got all this

[05:12] information in complete upgrade. That's cool. Second one here. This is a kind of

[05:16] Times newspaper field. Price to tell to ambition. And this is all based on Russo. I think this is really cool. And

[05:22] welcome to professional. Very, very decent. And then we have this one here, right? Choose a plan. Different options.

[05:26] And you can do essentially whatever you want to. Now, let's say for example that we like the style of this one, but I want to change some of the text. I can come down here, click on this, click on modify, click on edit, and I can click on this and say pricing tailored to desire. And I can change the text

[05:40] directly on anything I want to. What I can also do here if I wish is I can highlight a page and click on this and say, hey, create me a landing page for this, whatever I want to do. Right?

[05:49] Really cool. So, now it's in that style. And this is how stitch works. Obviously,

[05:53] the idea being that you stitch things together to build out page by page. And as you can see, what it's done is it's got a when you want to buy it, this pops up. Great. And then a dashboard. So it

[06:03] just gives us the ability to edit things in your app, in your website, page by page. So if I like welcome professional, maybe I'm like, actually, dude, can we have confetti on this page, please? And let's just give it a little bit more of a warmth to it. So some kind of image

[06:17] and improve the graphic on it here, please. Exactly the same thing, right? I can kind of pick different things and change it and amend it and design it kind of like basically section by section which you can't do in a standard builder. And as you can see I just want

[06:28] to call out that you can have multiple different queries working at the same time. You don't get kind of logger jammed behind one thing then you're waiting then you go again which I think is a great feature and then we can come back and we can see that it's actually built out built with architectural precision right so this has gone a little bit too large so we can click on this we can modify it we can edit it we can do various different things. It's great that we have the ability just to literally edit the text as you want to.

[06:52] There we go. Okay. So, this is a certain size. You can edit with AI and you could

[06:56] say if you wanted to something like, "Hey dude, could you just decrease the size of a text so it fits in like no like basically one word, one line, please?" Again, you can make these little mini edits as you go about, no problem whatsoever. And again, it's built it with the exact same style so you can build out all this sort of stuff, which is awesome. And then

[07:11] essentially, it'll go ahead and do those individual changes for us. So the idea is that we just pick one of these three styles that we like and we can build out the entire website. But what we can do next with the latest image generation model is literally amazing. Now the next

[07:23] thing that you can do within stitch which is really important for you to understand is redesign. Now this is fantastic. So if you come down here you can select redesign. So what this does

[07:31] is leverage the powerful nano banana 2 to make anything we want to. We can find a website we think is cool. Let's say it's rocket. We can come over drop the

[07:38] URL in. Come over here and grab a screenshot like so. And then just clipboard this. come back over to Stitch

[07:44] and drop it in. I'm going to say something like, I would like you to redesign this for me, an entire website based on this URL. So, the beautiful image at the top, and then we may want things on there like testimonials, uh, companies we work with, how it all works together, uh, FAQs, and then a CTA and a beautiful chat interface at the bottom.

[08:03] Wonderful. Okay. And at this point, you can make any suggestions you want to.

[08:06] And maybe you didn't grab an existing website, right? Maybe you were on a website like Dribble and you want to find out existing design inspiration by searching for websites. Wherever the place is, drop your designs in as many as you want. Come over here and then

[08:19] literally go off and click on redesign. Now, one of the cool things here about leveraging Nano Banana to do this is we're not asking an AI to build the website. It's literally generating a gorgeous, beautiful image which has a way better reference point for us to build from than just trying to build up the website with code which should mean that we should get a better quality output on our first time. Wonderful. And

[08:39] it's come back now with a mobile design. So come check this out. Think it type launcher. We've got these different

[08:44] companies we work with. Describe how it works. Testimonials. Then we've got this

[08:48] chat style interface. I think that is gorgeous. Like that kind of fant, you know, that kind of like celestial background. Obviously, some bits we'd

[08:55] need to move around a little bit, but think of it as a concept art that kind of captures the essence of what you want to say. Then we've got some FAQs. And quick FYI, by the way, you can decide whether you want app or web on the homepage here. I chose app for that one,

[09:06] hence why we've got an app type design. And then I did one for you on desktop. So, this is the original image. I didn't

[09:11] ask it to change anything, hence why it's not done anything, but you can see it's recreated this. We have this trusted by innovators, love by builders, which is, I think, a really beautiful touch. Probably bring those logo size down a little bit. How rocket works. And

[09:23] then we've got this I think gorgeous FAQ section and then something at the bottom. And if I show you one I did earlier, think it type at launcher. Again, really gorgeous. Love these

[09:32] logos. Love these kind of interactive elements. And also the, you know, the design of this is fantastic. It's

[09:37] essentially an imagination engine. Now this is complete. I'll show you exactly how you can take this to a completely new level by using claw code and how easy it is to get it into anti-gravity.

[09:46] So once we're in anti-gravity, it's super easy. I'll show you this first then how you can get it into cloud code whether you're using VS code or anything you want to all you're going to do is come over here to these dots click on MCP service and if you just type in simply stitch and this is one of the cool thing about using Google products is how they're sort of all integrated with one another you click on stitch and all you're going to do is click on install like that's it it's asking for an API key we might need that so we're going to click on stitch API key then once you're on this page guys you're going to come down and click on copy key I should also call by the way that your daily redesign credits you got 15 a day just because it's brand new feature and they just make want to make sure that they're bottling everything up properly, but you may run into that as you build quite aggressively. So 15 a day is cool.

[10:26] And then you come back over to anti-gravity and enter your API key in here. But once that's complete, if you come on to a manage servers and then when you click on refresh, you'll see stitch will appear here for you on the left hand side with all the different things that you can do. Now if you were trying to install this on cloud code, all you would do is on the left hand side, come over to if you like extensions and make sure you've installed this claude code for VS Code like so. Just type in clude and it will

[10:48] appear. Then we've installed that. We're going to sum it up by clicking double clicking in the central panel and you'll see this orange thing and then it's there. And now essentially we can start

[10:56] chatting to claude code to get this installed. And then to add this to claude code, all you're going to do is enter in this base click code here which is claude mcp ad transport. I'll put this down below for you in the description. So hit enter with that and

[11:06] then it will add it to your claude MCP and then claude can now go ahead and use that. We said that's fine. Then we'll just need to provide to it the same API key that we did with anti-gravity. And

[11:14] then you can provide your API key with claude. We'll add it to your configuration. And from that point, you can chat with it in claude. You can chat

[11:20] with it in anti-gravity or whatever environment that you're using it in. So what we need to do then is really install these skills for MCP. So we're going to come over to this GitHub repo here which has got all the really cool things we can do. This is a Google

[11:32] official one. What we're going to do is come and grab the code, click on copy, come back over to anti-gravity and claude, and we're going to say, "Hey there, I would like you to add these skills, please." And essentially, it's going to come down, and then we're going to enter that in right there, and it'll just basically replicate those. Once

[11:45] again, we can also use a clip code. It really depends on whichever whichever manner in which you're using the color code. All right, wonderful. So, let's

[11:51] actually test it that it knows it's got a real thing. So, let's open up right now into a new browser and say, "Hey, dude, could you just tell me what the latest design was that I created in Stitch?" So once we know it gets an answer question, we know it's fully connected. And just like that, it's come

[12:03] back and confirmed that the latest design we have is Rocket AI chat interface with a project ID when it was last updated and everything that works, which is freaking amazing. Now, the first thing that we want to do is get what we call a design MD. So when you've been in Stitch and you've designed something, you think, Jack, I think this looks gorgeous. Maybe it's this design.

[12:21] Maybe it's this design over here with this gorgeous, beautiful, whatever the thing is, play around with it. Get creative. When you've got that, what effectively you want to do now is get the design MD, which is the the blueprint, the design blueprint of this, that we can actually codify the style.

[12:36] Now, I asked Stitch to turn all of these things here into a landing page for us. Okay, now these are images. You see, if I modify, I can annotate. What I can do

[12:46] on the canvas is like maybe I want to get rid of these trees. I can just say, hey, you know, remove these trees or I might want to hire this rocket and I could say something like make this bigger, right? You know, you get the idea. I get to do whatever I need to

[12:58] here, right? I can draw comments. I can even draw further on here. Let's just

[13:01] come over here and draw this guy up. You know, it's really cool. You can make all these really cool changes if you want to. So, I can come down here, maybe

[13:07] leave a little note as well, shall we? Here. Just say something like, I know, make bigger. Who doesn't want to make

[13:12] the rocket bigger, right? And if I click on apply, now once you've designed everything to the standard that you like, what you want to basically do is come down and ask it, I would like you to create for me a design. MD based on those designs. And then what this will

[13:23] do is call the stitch MCP list of screens, find them. Then it will fetch the HTML code from the main page to extract actual design tokens and also get the project level metadata. And what this will enable you to do for your clients, for your business, is replicate any of those pages in the exact same style that you would like. So it's all

[13:40] going to be consistent. And then just like that, now we've actually created now with Claude is this wonderful breakdown. And again, you can do this in the anti-gravity chat, you could do this in VS Code, you could do this anywhere.

[13:51] The point is that we're using the model to go ahead and build the stuff. So we've got primary project ID and then we've got the visual theme and atmosphere, the color palette, the ROS, all the sort of stuff that we like, which is really cool. So what we can now do is actually ask anti-gravity, ask cla code to go ahead and build us an additional page. So let's go ahead and

[14:07] check the page to see what would make sense. Well, what I'm going to do, guys, is actually bring out the Gemini 3 Pro high cuz it's got nano banana native to it. I'm going to say, "Hey, dude. What

[14:15] I'd like you to do is redesign the images so that they are a kind of jibli beautiful art style." I think that'd be really great. And then in the same style, what I'd like to do is go ahead and add for me a pricing section on the page and then show me what that web page looks like. Beautiful. So now this is

[14:29] complete and it's all done. Let's see what it said. It's done. Generated the

[14:32] new images, added a pricing section. And if you refresh the browser or open this up, we can see it. So let's grab this HTML and see what she's up to.

[14:39] Beautiful. So we check it out. We've got it here. Think it type launcher. We've

[14:42] got the ask me anything, which is cool. We've got the frameworks here. Trusted by these companies, one prompt, the whole app. I love the design of these.

[14:49] This is gorgeous. Son of people will try it. We've got a templates. Happiness

[14:52] speaks back end. Are you ready? We've got some different toggles we can play around with here. Sample pricing. It's

[14:57] added in the pricing section. FAQs. This is this pretty sweet actually. I quite

[15:00] like that. And then here we go. Start building our production ready apps. I

[15:03] think the highlight really is the visual imagery of this website which I think is just super crisp. And the cool thing is guys, what we can do now once we get that style and design that we really like. We can actually create a brand new chat and say, "Hey, I want the exact same style. I want you to go over and

[15:17] create a new stitch book for a SAS company that is selling VPN subscriptions." And if you're wondering how I got this page, it's just flipping between open editor and over here to agent manager. That's it. And on the

[15:27] left hand side, we can see everything to do. So here's the redesigning rocket images and creating VPN. Effectively, an anti-gravity. We can manage multiple of

[15:34] these at the exact same time. And then if I wanted to publish this on a website, all I would literally do is let's come over to start a conversation. Going to go over to we're going to go to Stitch, which is where all this stuff is happening. Then I'm just going to say

[15:45] something like, "Hey there, publish this to GitHub and Versel." And if you don't have a connection to GitHub and Versel, you can basically just say, "Hey, connect me to the GitHub CLI." And it'll open a brand new page. You enter in your

[16:00] credentials and then Versel is just a website. Basically, it's a website that lets us host a code that lives on GitHub and we can give that code to anti-gravity include and it will walk you through the process and then we can essentially host it up which means when we give it very simple command it will open up and log in. If you're unsure how to that process I'm going to link up on screen takes like 3 4 minutes. It's dead

[16:19] straightforward. Now, as you can see guys, it's now also started creating this new thing and look at what it's done here guys. It's given the full prompt based on our exact style. So,

[16:28] it's got dark modern futuristic aesthetic. Here's all the information it's given it. Now, Stitch is doing this for us automatically in the background.

[16:34] We didn't even touch stitch. I just went over to it and you can see this has all been prompted by Claude based on our existing designs, meaning we can spin up as many of the want to as many pages in our existing websites and apps as we want just by prompting it. And we'll get the same kind of consistency using Stitch. And when I do check out the app,

[16:50] I'm really impressed by the interactivity that it's managed to smash. The coolest thing I think of this entire workflow when I come over to Sturge is realistically the ability to build things. like this is the one that I said, "Hey, rebuild it in this particular style." And it's doing this

[17:02] for this VPN thing, which I think is really cool. Now, understanding how to build beautiful websites is amazing, but it's only one part of a multi-part system for building out systems on websites. Whether you want to sell it or scale your own business, connect your CRM.
