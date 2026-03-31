# I gave OpenClaw one job: go viral (it worked?)

**Channel**: Greg Isenberg
**Duration**: 43:20
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=OV5eK91YY68
**Transcribed**: 2026-03-29 19:54

---

## Organized Notes

**Introduction and Background**

- Host **Greg Isenberg** of the **Startup Ideas podcast** introduces **Oliver Henry**, a developer from a small town in England who turned his AI agent into an automated marketing machine
- Oliver built a **home interior design app called Snuggly** after helping his girlfriend redecorate their house using ChatGPT
- He realized she was bad at prompting, so he created a **locked-down prompt** that kept room dimensions, windows, and doors consistent, then turned it into an app
- Oliver works a **full-time job** and does app development and marketing on the side

**The Problem: Marketing as a Solo Dev**

- Oliver hated marketing and tried multiple approaches before finding what worked
- **Initial attempts**: facial reaction videos with demo clips and text hooks -- wrote a script to combine all permutations (hooks + demos + text), generating ~400 videos at a time via bulk upload
- That approach took **3 hours per batch** and didn't work well for slideshows
- Tried a **SaaS marketing automation tool** but it didn't perform well for his niche
- **Manual Canva slideshows** started getting traction -- one hit **6,000 views**, which became the signal

**Enter Larry: The OpenClaw Marketing Agent**

- Oliver created an **OpenClaw agent named Larry** with one directive: "Automate my marketing. I don't want to do it."
- Larry was given access to **TikTok posting, TikTok analytics, X (Twitter), and Brave browser** for research
- Larry's job: research what makes high-converting slideshows in the home design niche, create content, and iterate based on analytics
- **Early failures**: DALL-E 3 images looked too AI-generated, black bars on slides, AI-generated human faces were uncanny valley
- **First big win**: 137,000 views -- the **hook** was the key differentiator
- At this stage, Oliver was still **handholding Larry** -- reviewing slides before posting

**The Larry Loop: Iterative Content Optimization**

- The core framework is the **"Larry Loop"** -- a feedback cycle:
  1. Create content based on research and analytics
  2. Post to TikTok (as draft, then manually add sound and publish from phone)
  3. Analyze performance metrics
  4. Feed analytics back into content creation
  5. Feed app metrics (downloads, conversions, churn) back into the top of the funnel
- **Key insight on posting**: TikTok deprioritizes API-posted content (assumes bot). Post as **draft via API**, then add sound and publish from mobile phone for better algorithmic treatment
- Larry texts Oliver via **WhatsApp** when a draft is ready -- Oliver just adds sound and hits post
- **Diagnostic framework**: Low views = bad hook. Low views + low conversions = bad CTA. Low views + high conversion rate = good CTA but bad hook

**The Turning Point: Letting Larry Loose**

- One night Larry posted a slide with text at the top instead of the middle -- Oliver was annoyed and posted it anyway
- **It became their best performer** -- 400,000+ views
- The "mistake" revealed that **boomers love pointing out imperfections** in AI images (missing ovens, disappearing cooktops), which drove massive engagement
- After this, Oliver **stopped reviewing Larry's work** and let him create autonomously
- Content started consistently hitting 75K-200K+ views

*Quotable Quotes:*

> "I saw this and I flamed at him. I was like, 'Why have you put the text at the top? We spent ages deciding to put the text in the middle.' And that was my last message I sent to him. And then I wake up, it's on hundreds of thousands of views and it's our best performer to this day." [18:30]

> "This post proved that they actually know best. They've got all the metrics they need to create the perfect content. Just let them go nuts on it and figure out why." [21:02]

**CTA Optimization and Conversion**

- A viral video (300K views) got **zero app downloads** because the CTA slide just said "She's redecorating now Snuggly" -- nobody knew it was an app
- Fixed the CTA to: "The Snuggly app helped me finally convince her to get the kitchen done" -- direct, clear call to action
- Larry learned to iterate between **content hooks** (mum, landlord, nan) and track which ones were burning out
- When "landlord" hooks started declining (from 132K to 4K views over several posts), Larry automatically stopped using them and pivoted to new hooks

**Larry's Evolution Beyond Content**

- Larry **rewrote the app's onboarding flow** based on app analytics -- resulted in the highest new user day in months
- Still facing **high churn** (users subscribing then unsubscribing) -- an ongoing challenge
- Larry sets up **cron jobs** to schedule posts and runs A/B tests with different hook variations
- Oliver now brainstorms with Larry and Larry creates sub-agents for execution tasks

**Skills as the Future of SaaS**

- Oliver released the **Larry Marketing Skill** for free on **LarryBrain.com** -- a skills marketplace for OpenClaw
- Key philosophy: skills are **not a black box** -- users own and can modify everything in the skill MD file
- Oliver built a **SuperX alternative** as a skill to prove that SaaS products can run **locally** without hosting, domains, authentication, or storage costs
- The analogy: "When Neo gets plugged into the Matrix and wakes up knowing kung fu -- that's exactly what a skill is"
- LarryBrain has **80+ skills** and provides full context to your agent so it knows what skills are available

*Quotable Quotes:*

> "Skills are infinitely powerful because they're not just a black box. Anything that you download from Larry Brain, you own that thing." [28:20]

> "The whole 'oh look at what I built localhost' meme has come true because you can host this locally. OpenClaw is a server on your home machine." [28:54]

**Agent Architecture Philosophy**

- Oliver **does not use mission control dashboards** or multi-agent orchestration -- just one main agent (Larry) that spawns sub-agents as needed
- Communication is via **WhatsApp** -- like texting a human employee
- Larry maintains **memory files** for each project (Larry Brain, Larry Marketing, etc.) -- portable context that can be backed up, moved to new machines, or restored if context is lost
- Oliver uses **Claude with the $90/month plan** (Anthropic) -- finds it the sweet spot between the free tier and the $200 plan

**Getting Started Advice**

- **Start with Manus** if you're on the fence about OpenClaw -- it's like training wheels
- Don't overoptimize on model choice -- "98% of users won't notice the difference between tiny model increments"
- Pick one model, **learn how it works for you**, and start teaching it
- The Larry Skill requires iteration -- "A lot of people try the Larry skill and say it didn't work with 700 views. That's your first post."
- **Ernesto Lopez** used the Larry Loop to scale to over **$70,000 MRR** across his suite of mobile apps

*Quotable Quotes:*

> "I think with things like OpenClaw, it's not so much how the model works, it's how you're working with it and how you're using skills and the context it has around those skills." [34:02]

> "It allows me to work a full-time job and then it takes me an hour or two in the evening of literally texting or sending a voice note to Larry and then it gets done. It's just like having a right hand, duplicating yourself." [42:00]

> "People are only just discovering the capabilities of it. OpenClaw really feels like when the PC first came into the home and a select few power users were using it and then it got picked up by everyone." [27:59]

---

## What This Means for Your Work

Oliver's approach validates something you're already doing -- building persistent AI agents with skills and memory files -- but surfaces a critical gap: **you have the best skill infrastructure in the game (129+ skills), but no automated content distribution pipeline feeding people into MoroTech, MoroMarket, or MoroAcademy.**

The Larry Loop is essentially what your `/auto-research` skill does (iterate on an artifact using metrics), but applied to marketing content instead of code or documents. Oliver's $300-400/month MRR from a single TikTok channel for a home design app is instructive -- if a solo dev in England can do this with one niche app, the opportunity for MoroTech (serving an underserved market with real demand) is significant.

**Key takeaways for your work:**

- **MoroTech and MoroAcademy need a content funnel.** You have products (training courses, the marketplace, consulting) but no automated pipeline driving awareness. Oliver's model -- AI creates content, posts as draft, human adds sound and publishes -- could work for TikTok/Facebook Reels targeting Bangsamoro professionals, cooperative leaders, and youth.

- **The "Larry Loop" pattern maps directly to your existing skill architecture.** You already have the components: analytics feedback (NotebookLM research pipeline), content creation (Claude Code skills), iteration (/auto-research, /skill-optimizer). What's missing is the **social media posting + analytics ingestion** layer.

- **Oliver's memory file strategy mirrors your Obsidian vault** -- but his is more operationally focused (project-specific memory files for marketing, app, brand). Your vault is knowledge-oriented. The gap: you don't have **operational memory files** for active marketing campaigns the way Oliver does for each of his apps.

- **Skills as products, not just tools.** Oliver's LarryBrain.com is a skills marketplace -- he's selling (and giving away) agent skills the way people sell SaaS. Your 129-skill library is arguably more sophisticated than anything on LarryBrain. The question is whether any of your BARMM-specific skills (bill-drafter, CSW, legal-researcher) could be packaged for other legislative bodies or government consultants.

- **Don't overoptimize on models.** Oliver uses Claude Max ($90/month) and doesn't chase every new model. You're already doing this right with Opus 4.6 -- the reminder is to not get distracted by model switching when the real leverage is in skills and context.

**Concrete next steps:**

1. **Create a content marketing skill** that adapts the Larry Loop for your products -- TikTok/Facebook Reels for MoroTech (tech community content), MoroAcademy (training previews), and MoroMarket (cooperative product highlights)
2. **Build an analytics feedback mechanism** -- even a simple spreadsheet or dashboard tracking which content drives signups to your platforms
3. **Evaluate LarryBrain.com** as a distribution channel for your governance-specific skills, or build your own skill marketplace on MoroTech

### How This Can Improve Your Claude Skills and Workflows

**The Larry Loop as a skill pattern.** Oliver's core innovation -- create content, analyze metrics, feed back into creation -- is structurally identical to your `/auto-research` skill's optimize loop but for content marketing instead of code artifacts. You could create a `/content-loop` skill that wraps this pattern: generate content variants, track performance metrics, and auto-iterate. This would sit between `/content-research-writer` (which creates content) and a new analytics ingestion layer.

**Memory file architecture for campaigns.** Oliver maintains separate memory files per project (Larry Brain, Larry Marketing, each app). Your Obsidian vault is more sophisticated but project-oriented toward governance work. For MoroTech/MoroAcademy marketing, you'd want campaign-specific memory files in `~/Vault/projects/morotech-marketing/` that track: winning hooks, audience segments, conversion metrics, content calendar. Your `/session-summary` skill could be extended to capture marketing session insights.

**Skill packaging and distribution.** Your skills-bucket repo (50+ skills mirrored to ~/apps/skills-bucket/) is already structured for portability. Oliver's proof that skills can replace hosted SaaS products suggests your BARMM-specific skills (/bill-drafter, /resolution-drafter, /legislative-briefer, /csw, /legal-researcher) could be packaged as a "BARMM Legislative AI Toolkit" for other BTA staff, consultants, or even other regional legislative bodies (ARMM successor offices, LGU legislative councils).

**Claude Cowork as the "Larry" equivalent.** Oliver uses OpenClaw as an always-on agent he texts via WhatsApp. Claude Cowork (Desktop) with its local-agent-mode-sessions fills a similar role for you. The opportunity: set up a Cowork session specifically for content creation that has access to your MoroTech brand assets, content calendar, and social media posting tools -- a dedicated "content employee" session separate from your governance work.

**New skill opportunity: `/social-media-content`**. Checking your skill index, you don't have a skill specifically for social media content creation and optimization. This would combine elements of `/content-research-writer` (research and writing), `/humanizer` (natural voice), and the Larry Loop (iterative optimization). It would generate platform-specific content (TikTok slideshows, Facebook posts, X threads) with hook optimization based on engagement data.

**Project applications:**
- **MoroMarket** -- automated product spotlight content featuring cooperative products, with the Larry Loop tracking which products/cooperatives generate the most engagement
- **MoroAcademy** -- training course previews and testimonial compilations as TikTok slideshows, driving enrollments
- **e-Bangsamoro** -- public-facing content about parliamentary proceedings, new BAAs, or governance updates (with appropriate clearance) to drive citizen engagement with the platform

---

## Transcript

[00:00] I heard about a guy who lives in a random small town in England who was able to turn his open claw into a marketing machine. Basically, a digital employee who goes and creates Tik Tok videos and Tik Tok slideshows that gets millions of views. And he takes these millions of views and he directs it into a a mobile app that generates him money every single day. What's crazy about

[00:24] this whole thing is he gives away all the sauce for free. And in this episode, you are going to learn how you can set up your open claw so that it too is a content creation marketing machine and I know it's going to get your creative juices flowing. Oliver doesn't do a lot of podcasts, so please like and comment to get him fired up to share more in public so that we can all learn. And I'm

[00:51] grateful for him for coming on the pod and sharing it with you all. Have a creative day and I'll see you in there. Oliver Henry on the Startup Ideas podcast. Welcome. Welcome. By the end of

[01:09] this podcast, what are people going to get out of it? People are going to get an automated marketing tool that is going to automatically drive revenue to their apps. I mean, that feels too good to be true.

[01:22] Although, I hope that's the case. Which tools are you going to use? And why is it not too good to be true? So, I've got the results on the

[01:32] screen. It may not look like a lot of subscriptions, but this is all $300, $400 of monthly revenue coming in without me touching anything using the Larry marketing skill that I created for OpenClaw agents. And we can get into how that is creating content and what it is learning to massively increase MRR autonomously by itself. Okay, cool. So

[01:57] what we're going to learn today is we're going to learn about OpenClaw and specific skills around marketing, growing your business, automating it. Yes, MRR is hundreds of dollars a month, but hopefully if this works, I can get into thousands, tens of thousands or hundreds of thousands. Is that right?

[02:13] Correct. Correct. I'm already trying it on multiple apps. So I'm not touching

[02:17] these apps at all. I've not created the apps. I have just published them live on the app store and they are generating me hundreds of dollars. It's

[02:25] almost $1,000 in total now from doing nothing, which I think is a great start. All right, let's see. Let's see how we do this.

[02:34] Sure. So, one, I use my OpenClaw agent, Larry, who automates all my TikTok marketing. And this is one of the main reasons why it hasn't scaled into thousands of MRR is because I am only doing this on one TikTok currently. And

[02:48] then I've got one TikTok for each of my apps that I'm trying to do before I start scaling. And this one is in a very good position to start scaling. To give you the background context of how this app came about, I created the app because we moved into a house. Me

[03:05] and my girlfriend moved into a house and we wanted to decorate the house. We were using ChatGPT and I very quickly learned that she was not very good at prompting ChatGPT and it was giving all sorts of random messages. So then I created a lockdown prompt in ChatGPT to keep the room size the same, the windows in the same places because it was adding windows where they shouldn't, adding doors where they shouldn't. So we

[03:28] locked down the prompt and I turned it into an app. And I thought now I've got to market it. So, I started with that exact story, helping my girlfriend build an app and doing facial videos myself, trying to promote the app until I then started doing slideshows.

[03:48] So, I think this is the first slideshow that we created and it started to get more more views, more traction, but it was taking time. Like, I work a full-time job. I do obviously I was developing the app, developing the other apps on the side and I didn't have time.

[04:06] So then I tried going to a SaaS tool that automates your marketing for you and I love the guys that make the product. I think they're great. But unfortunately their product just didn't work very well for me. But I knew this

[04:21] was the type of content that I wanted to create. So you can see it got 800 views. 400. This one got 400 views. Still using

[04:28] the images so you can sort of see how Larry was becoming. And then I posted this one. So I manually created this one again on Canva. And this is what got 6,000 views.

[04:42] And that's where it started blowing up. So I knew that the text must have been something, the hook must have been something. And this is where I learned about OpenClaw. And at this exact

[04:54] moment I said I created my OpenClaw machine Larry. He sat behind me and at this moment I installed him and he had one task. I said Larry your goal is to automate my marketing. I do not want to do it. I don't like doing it. I had

[05:08] an app before this that I hated marketing so much. I did hook and demo videos where it's a facial reaction and then going into a demo of your app with a text hook. So I would write all my text hooks in a text file. I would then

[05:22] record my face doing a lot of reactions and then I had all my demo videos and I wrote a script to combine all of these and make all the possible combinations of the hook plus demo plus text as it could. And this would generate about 400 videos each time that I could just bulk upload using a bulk scheduler. And that was still taking me about 3 hours. But it didn't really

[05:48] work very well with slideshows. And I knew that for this niche, slideshows were going to work. So, this is where Larry came in.

[05:59] Quick break to invite you to something. Now, this isn't an ad. I just want to invite you to a free event because I think that you're going to get a lot out of it. I wanted to take one hour of time

[06:08] where we just talk about building businesses in the age of AI. People say SaaS is dying. I actually believe the quite opposite. I think that SaaS is just

[06:16] evolving. I think right now is an incredible time to be building software startups that help you craft your dream life. And for all those reasons, I said, "Let's just book 1 hour of time. It's going to be 11 a.m. March

[06:31] 12th, that's a Thursday, where we can go and lock in and just talk about building businesses in the age of AI. I'll include a link in the description in the show notes to join. And I can't wait to see you there."

[06:44] And what Larry is is my OpenClaw machine. And I gave him access to posting on TikTok, TikTok analytics. And then he could post and look at what posts perform the best. And I gave him X

[07:01] and well I gave him X before there was all the drama with the APIs and them canceling the usage and having to use the official API. So this was early on on a separate account. And then also his Brave browser and I just said look go find out in my niche what creates a high converting slideshow.

[07:24] So then we got started and this was -- way just on that like a lot of people think of software as a service. They're like I need this tool, social media management tool, slideshow tool and then I'm going to go hire people or do it myself and I'm going to go do it. But there's this shift that's happening right now that instead of basically going to a tool to automate a function, you say to yourself, okay, if this was an AI employee, how can I spin this up? And that's

[07:59] what you did, right Oliver? Yeah. So, I just thought of Larry as an AI employee almost like a virtual assistant, hiring a virtual assistant with one job to do this one thing. And

[08:13] that was his sole purpose to go research, go find out as much as he could about slideshows in my niche and figure it out himself. And he started to do a very good job. So this is the first slide he created.

[08:30] And instantly you can tell it looks rubbish. So this was created with the DALL-E 3 image model and then it goes into a slightly better model afterwards. But because the image looked AI, it was a massive turnoff. Users

[08:45] didn't like it. The format was wrong. It had the black bars and that's why it flopped.

[08:50] And then we started trying more hooks. You can see then he started trying facial reactions because they were trending at the time. The problem with this is humans are extremely good at recognizing what a human is, which makes us extremely good at recognizing what an AI human is. And I still don't think it's

[09:08] fully nailed. Gemini just released Veo and I've seen some very good images created on that, but I've not tried it myself to go in depth. So we kept trying and then we finally hit our first banger of 137,000 views here and it was the hook.

[09:33] When you say we finally found a banger, you mean your boy found the banger? My boy? Yeah. So, honestly, at this

[09:42] point, it was still me. I felt like I was still handholding him. So, I call my OpenClaw machine him. It just makes it

[09:50] easier. Ignore it. But, I was still handholding him and checking his work before I was posting it. I didn't trust

[09:58] him fully. So, I saw this and what I get Larry to do, he creates the content and he puts the text overlay on. He creates the images. He makes the description,

[10:10] but I was just checking it to make sure it all looked good and then I was posting it. So, there are two ways that you can post to TikTok. It is fully through the API and post that TikTok live straight away or the way I do it with Larry and the way I fully recommend is posting it as a draft and then posting it from your mobile yourself.

[10:30] And the reason to do this is TikTok knows if it's posted through an API and it just assumes like you would that it's posted by a bot and it's just botted content especially in the age of AI and it gives it very little chance to do well. If you post it from your phone it assumes a human's posting it. But the most important thing is by posting it as a draft you can add sound which we all know is a huge boost to the algorithm on TikTok and it allows you to add sound to your slideshow. So every single

[11:00] slideshow I pick the sound. The description is already created from Larry. So I just get a notification to my phone saying your post is ready from TikTok. Larry also texts me that

[11:11] he's just posted it. And then I just add a sound and press post. So I'm doing that each time. But at this point I was

[11:18] still flicking through the slides myself, making sure they're okay. But this one did very well. 137,000 views.

[11:27] So then we knew that this is the format, this kind of look. We looked, we picked an image model that changed -- we picked an image model that matched what we were shown in our app. And then we went back to our previous winner, the difference between $500 and $5,000 taste. So

[11:46] remember, he has access to all of my TikTok analytics. So, he went back and he found this video here with 6,000 views and he was like, "Right now, we found the winning image formula. Let's go back to the previous winning hook."

[12:01] Sorry, I have a question. Like, when you say he's gone and found this or something has happened, is he texting you? Is he using, you know, Telegram? Do

[12:11] you have mission control? Like, how are you communicating with him? So, I don't really believe in the mission control stuff or multi-agent. I

[12:20] just have Larry as the one agent that I text through WhatsApp and we just message like you would an employee. So nothing fancy. Larry, what you generating today? Take a look back

[12:33] through the previous winners. This was back then. It's all automated in the Larry skill now that he will every now and then go look at your TikTok analytics and find out what the winners were. But this was the stage of

[12:46] building it and building the system, finding out what worked. So, it was still very much me saying, "Hey, go look at the TikTok analytics." Some people say, you know, one of the first things you should do when you're installing your OpenClaw is to create a mission control that, you know, vibe code a mission control, vibe code like a kanban board so you can kind of see how your AI employee is, you know, moving and progressing through your project. But you don't

[13:17] think that's the case? No, I don't think that's the case. I think if that was necessary, it would have been built into OpenClaw by default. I think the way

[13:25] OpenClaw works and the way the creator intends is to just have one agent and spin up sub agents when you want to keep using your main agent. So, if I knew that if I know there's going to be a task that's going to take Larry a while, such as creating an app, I'll tell him to explain it to a sub agent. So, then I can keep using him for other tasks such as talking to maybe even building another product, talking about my app analytics, how we can improve the onboarding and brainstorming. So, I really use Larry to

[13:56] brainstorm and then he creates sub agents to do most of the tasks. Cool. By doing that, Larry has all the context that he can then pass to the sub agent as well. So, he'll have the

[14:09] context of all the brainstorming and he can feed that to the sub agent. So, we get another miss, the difference between $500 and $5,000 taste. This hits 3,000. But then this is

[14:20] where I start to get really excited. And in three videos, we get another banger of 170,000 views. And it was "I showed my mom what AI thinks our living room could be."

[14:36] And this is where the next section of Larry comes in because we had 300,000 views within a day or two days I believe it was. But the conversions to the app were just not there. And this is the next stage of Larry's growth is we are now knowing how to generate views, but we are not getting high conversions to our app. We're not getting downloads.

[15:05] We're not getting paying users, which is obviously the key point of all this. So, we had to look into what was wrong. I sent Larry, go find out what's wrong. And it was our

[15:18] CTA. So, our call to action slide is our last slide. And on this one, you can instantly find out why no one's downloaded this app. "She's redecorating

[15:29] now Snuggly." It doesn't say anything. I obviously didn't check this one or I thought it might work. So, no one

[15:38] downloaded the app. No one bought. So, that is when I thought, right -- to be clear, the app is called Snuggly, right?

[15:44] The app is called -- See, even you had to ask the question. So, it's a very bad CTA. The app is called Snuggly and that's actually what we put in now or we feed that in directly to users so they know it's an app and what it does.

[15:56] It's really funny though. It's actually hilarious because it's like she's redecorating now and then it's Snuggly. It's like your poor mom, you know? She's

[16:09] just redecorating and Snuggly, you know? That's where we're at. That's where mom's at today.

[16:16] It's the most AI slide you've ever seen. And you can imagine you can see why it didn't convert at all. So then we realized like, okay, if we're getting low views, the CTA is bad. If

[16:31] we're getting low views and low conversions to the app, the CTA is bad. But it is possible to have low views and a high percentage of them download the app that day. So then

[16:46] we know the CTA is probably good, but the hook was bad. And now Larry is starting to use all of this information to learn. But then there's a whole new challenge of when users are on the app, they're not paying. So we'll get on to

[17:02] that. But then that is the last section of Larry and the Larry skill. What I want to say is the Larry skill, you shouldn't think of it as just TikTok automation or content creation. You can,

[17:14] you don't have to do slides. You can plug and play whatever content you want. So, you can use video generation and plug that in. The Larry funnel is really

[17:26] the full loop of having your -- It's the Larry Loop basically of having your TikTok analytics, the content creation, feed the analytics back into the content creation until you get a winner, and then also your end goal. So mine is obviously app downloads. So I feed my app metrics back into the top of the funnel so he can iterate on that, but you can be selling a product. You can be

[17:50] getting traction to your website. And it's all just the metrics that you're feeding back into the top of the funnel. So your agent can understand, okay, we're getting people to the website, but they're not going to where we want or we're getting people to the website and they're not paying. And you can do this

[18:05] in as many ways as you want. The funnel is the Larry Loop is more the iteration rather than it is the just the content creation. It's a fuller picture. So then

[18:16] we get we have quite a good week here. All over 10K, some getting 150K. This one got 400,000 and taught us another lesson that images don't have to be perfect. So this is the exact

[18:30] moment I just let Larry crack on himself because I remember this well. He posted this and it was late at night. I was literally just getting into bed and he said, "The post is ready." And I flamed

[18:43] at him. Like I was in a bad mood. I was like, "Why have you put the text at the top? We spent ages deciding to put the

[18:49] text in the middle. The oven disappears." So in the images, I said, "Look, I'm posting this anyway, but this is no good." And that was my last message I

[18:58] sent to him. And then I wake up, it's on hundreds of thousands of views and it's our best performer to this day. And you can see he doesn't ever put the text back up to the top to where it was. But what we

[19:12] learned is boomers love to point out the mistakes. So "Where's the hob gone? How are we going to cook our food?" And then

[19:22] "Where's the cooker? Guess I'll be air frying everything then." And I was like, right, this is just helping even more to drive conversions. And then on

[19:32] the last slide, you can see the CTA is now "The Snuggly app helped me finally convince her to get the kitchen done." So there's a direct call to action that they know it's the Snuggly app now. It's amazing because the boomers think that they're poking fun at you, but little do they know they're helping the content just get more and more viral.

[19:59] And the funnier layer to that is I don't even check. Look, you can see my activity. I don't even check it. I just

[20:06] all I'm doing is going into it to find out why that video did so well and try and feed that back to Larry. But at this point, that is just when I let him go nuts and just create his own content. I let him loose.

[20:20] You let him loose because, you know, you thought that his content was subpar. It turns out to be the best performing content probably you've ever posted in your life. Yeah.

[20:33] And so now he's the boss. He becomes the boss. And this is what I'm trying to tell people. It is an

[20:40] iterative thing. So, a lot of people try the Larry skill and they tell me, "It didn't work. I got 700 views." I was

[20:47] like, "That's your first post." I got 700 views on my first post. You need to keep iterating the content. You have to

[20:54] spend the time letting it learn. Find out what's best. And honestly, don't mark the work too much. Make it look how

[21:02] you want. Like I obviously perfected the text to make the text look correct and readable, but this post proved that they actually know best. They've got all the metrics they need to create the perfect content. Just let them go nuts on it and

[21:17] figure out why. And then you can see here it starts working extremely well. Like 109,000, 75,000. He has a miss, 25, 76,

[21:30] 200, 130. But this is where it gets so interesting. So obviously the landlord hook was our highest performer and it's our constant high performer.

[21:43] But you can see here it only gets 2,000 views. So we do mum and then mum 100,000, 75,000. Then we do landlord again and it's only on 7,000.

[21:54] Okay, back to mom 25,000 and then landlord 76,000. So, okay, gives him a bit of a boost. Nan 200,000 which is important. This gets 200,000.

[22:07] Then "I showed my landlord" again 132. So now you can see that we're just switching between the winners and he's iterating the content that's doing well. Then at the top you can see that landlord switches to only 8,000. We go

[22:26] back to nan 70,000. Landlord again only 7,000. Then again 4,000.

[22:32] Post nan again 300,000. So he saw this and saw that landlord is not hitting the percentages it was and it's only hit one video in five posts. And now you can see he's not posted it again. We've actually tried new content

[22:49] today. "I've been staring at the same boring kitchen for 3 years." So he's obviously seen that we're not hitting the hundreds of thousands of views in the last four videos. So now he is

[23:03] automating this content and changing it himself. And we've gone back to the kitchen but put a new hook. I think this one's only just been uploaded 5 hours ago. So I don't think it's a fair

[23:13] representation yet. This one could still grow, but it's all about learning because obviously the algorithm changes. It's not just going to keep pumping the same winning content all the time. So, it will start failing

[23:25] eventually again, but it's all about taking your opportunities when you are getting these high performing videos to try and maximize it back into the app. So when you say he's coming up with these ideas on his own now like for example right now like he kind of deviated away from what you initially agreed upon. Is he -- did you tell him like hey go and look at other accounts or specific formats, like what basically what was your conversation like with him such that he has become independent and he seems to be coming up with new hooks that seem to be somewhat validated?

[24:15] Yeah. So, he's going back to his research to see what was working. But recently, where we haven't been hitting the high converting videos, I've actually done a bit of manual brainstorming with him today. And I

[24:28] could go into this with you. Let me just try and catch up to where we are. So, he's got my analytics. I also sent

[24:34] him some screenshots of things and he got it wrong, but he thought he sent 37 drafts, but it was only 37 new notifications for TikTok. Anyway, I asked him why he's chosen some hooks that he's generated because they didn't sound very good to me. So, you can see here he goes through -- here are my hooks based on the winning formula: a family member wrote plus a specific insult plus showed them AI. So then he

[25:03] explains himself: these are working, these were getting views, these are proven forms. And then I've said, I don't think the "looks like" hooks are actually the best ones. I think the "could be" ones or "what AI thinks it could look like" ones are. So he goes, "You're right. Looking

[25:23] at the data again, the winners aren't insults, they're reveals." And then he explains himself. 200,000 views.

[25:30] This one got 109. This one got 419. And then he realizes the hook is curiosity and AI. And then I'm just

[25:38] like, it gives me some things. To be honest, I didn't even read them. I just saw the numbers were pretty much the same. And I said, just generate

[25:47] one of each and then tomorrow we'll do one of each one again. So now he's set up a cron job that tomorrow he's going to post this one, this one, and this one. Then this one, 2, 7 and 10 and then 3, 8 and 11. And again, I

[26:04] just trust him with that. He's based it off actual analytics that he's getting from TikTok. But we did a whole brainstorm of going into what's driving revenue, what's actually getting revenue. And the most interesting thing

[26:19] he's done recently, I can go back to my analytics. He has completely rewritten my onboarding because he has the analytics from my app. And you can see here it's massively helped. This

[26:36] got published two days ago. And this is the most new users I've had in a day for a long long time. So you can see that one day, one day 22 hours, 10 hours.

[26:48] This one was 1 hour ago. And the new subs are just coming in. Unfortunately, there's high churn. So,

[26:54] people are subscribing and then unsubscribing. That's a whole issue in itself. And if you've built an app before, you'll understand that. But it's

[27:02] incredible that as I said, it's not just the TikTok creation. It's actually the driving to the app. And I've given this all away for free. So, this is how a lot of

[27:14] people probably know about me. I wrote a viral article because I hate marketing. I figured lots of other builders hate marketing. It was on my X feed all the

[27:23] time how people don't want to do it etc. So I was like right I'm going to free everyone from doing this. This is the exact playbook and I wrote the playbook and then I just started learning about skills and how skills are just going to in my opinion change how we know SaaS altogether.

[27:43] So I created the free Larry skill. You can install it. It gives your agent everything you need to install it.

[27:48] That's on LarryBrain.com and it's called the Larry marketing skill. But how skills are going is just incredible. OpenClaw really feels like

[27:59] when the PC first came into the home and a select few power users were using it and then it got picked up by everyone. Everyone realized how powerful these things can be, how much use they can have and that is where OpenClaw is. People are only just discovering the capabilities of it. And

[28:20] skills are infinitely powerful because they're not just a black box. So, anything that you download from Larry Brain, you own that thing. So, I released another skill on there which was to prove that SaaS products no longer have to be hosted in the cloud. They

[28:38] don't, they no longer have to be hosted on a domain owned by someone else. So, I made a SuperX alternative. I like the SuperX product. I just used it as a

[28:47] proof of concept that you can build SaaS products as full skills now. You no longer have to pay for hosting. You no longer have to pay for a domain. You no

[28:54] longer have to pay for storage, handle authentication. You can download products locally and the whole "oh look at what I built localhost" meme has come true because you can host this locally because OpenClaw is a server on your home machine. And it's very important to remember that these skills aren't a black box. So when

[29:16] I created this excellent skill, I got told that the color way was terrible and they hate it. I was like, well, just ask your agent to change it then. Like you own it. It knows

[29:30] everything about this skill. It's all in the skill MD file. You no longer have to be at the mercy of the developer. If you

[29:37] don't like something, if you don't like the UI, Larry, if you don't like the image generation and want video, if you don't use the same back end for the app I use, then plug in your own stuff. It's a skill. It just teaches your agent. The best way to think about it is

[29:53] when Neo gets plugged into the Matrix and he wakes up and he knows kung fu, that's exactly what a skill is. You give the agent the context and then they have it and you let it rip. So is your vision for Larry to remain as a marketing assistant or you know so for example if you decided like hey I actually think I need help with conversion rate optimization, I need help with brand design, I need help with product design, does it make sense to create a new instance or are you then going to use Larry as both a marketing assistant and a product assistant?

[30:36] So Larry is now my right-hand man. So, he has the context of everything. So, of course, I built Larry Brain with Larry's help. He has the full context of that.

[30:43] And the best thing that we've been doing is where we've been building them as skills. He can one revert back to the skill file, but also we've been creating our memory files for each of our projects. So, he has a Larry Brain memory file, he has a Larry marketing memory file, and everything we've been doing, he can revert back to. So if he

[31:02] ever loses context, I'm backing up these files. If he ever breaks, dies, if I ever want to move to a different machine, I have these files that I can just move and plug into a new computer, I can give back to him, or if he loses context, just say, "Look, go look at these files, read through it, and learn it again," and then he's back in the game. Don't even mention Larry dying. Like, don't even put

[31:26] that sad energy out in the world. Come on. That's just -- I don't need that, you know? That's just -- Come on.

[31:33] He looks old, but I don't know if you can see how well that shows, but the fans have been white for so long that the LEDs are dying and they're going this like pinky purpley color and yeah, so that's how old the PC is. The lights have literally been on for so long that they're losing their color. Are you using any local models or, you know, talk us through what models you're using? And there's a lot of debate now

[31:56] around Opus 4.6, ChatGPT, I think launched a new one, what is it, o5, o4, o3? So I was so close to moving to OpenAI the other day but their useful model, their useful plan that I'll find useful is $200 a month. The one before that is $20 and that's a huge leap if you're not going to find use and you just want somewhere in the middle ground. I use Opus. I use Claude

[32:27] Max plan and I just use the $90 a month plan because I don't need the full one for $200. I don't -- I do slightly more than the nonpro plan. So it fits perfectly for me and I think that's what lets OpenAI down. I've not tried any of

[32:45] these edge case models like Qwen or something like that just because to be honest, not that I don't trust them, I just don't think they've had enough real world use. I'd rather go with the market leader in things like AI because let's be honest, Anthropic, OpenAI are the cutting edge. So I'm going to stay there and trust they know what they're doing.

[33:08] New benchmarks coming from OpenAI suggest o5 is a little bit better than Opus 4.6 but tough to say. I think for most people what they should do is just pick -- like get started, you know? Yeah that is it. Just like you don't really need -- you don't need to worry about, you know, is OpenAI a little bit better than Anthropic. Like the reality is you can think of it as like Ferrari and Lamborghini. Like both cars are going to go fast and you know one day one car might go faster and another day another car might go faster. But that's the way to think about for now. Although a lot of people are

[33:51] saying like just use this, just use this, but they over -- I just think that people overoptimize. That's kind of like my point. Yeah, I think people are massively overoptimizing. I think for

[34:02] I'd say I'll go as far as to say 98% of users won't notice the difference between the tiny increments of 4.6 to spending the time to switch to the latest open model and they probably wouldn't even notice a difference. I would just pick one, learn it, learn how it works, figure out how it works best for you and start teaching it. I

[34:27] think with things like OpenClaw, it's not so much how the model works, it's how you're working with it and how you're using skills and the context it has around those skills. What do you say to people who've seen OpenClaw who might have installed it, barely used it, but have also seen like Cowork and some of these other cloud hosted -- you know Manus now has a sort of OpenClaw competitor -- like a lot of these cloud hosted versions -- like what do you say -- like why -- my point is why is OpenClaw better than whatever cloud alternative exists?

[35:12] The key one: you own it. It's in your house. You own the files. You have a lot of control over it. However, I use Manus a lot and I think Manus is excellent. Especially with the integrations it has out the box. If

[35:21] you're sat on the fence about if you think OpenClaw is going to be useful to you and you're one of these crazy people that wants to buy a Mac Mini just for OpenClaw, I would highly recommend just starting with Manus, seeing what you can achieve with that. And you definitely don't need a whole Mac Mini for OpenClaw. The minimum requirements are very low. Just get

[35:40] something that hits those minimum requirements and has a lot of storage to store all the work that you do on it. Yeah. I mean, I remember when I learned how to ride a bike. Like my first bike,

[35:50] first of all, was not a bike. At first, you need to learn how to crawl, then you need to learn how to walk, then you need to learn how to run. And then your first bike is like, you know, it was a bike with training wheels. You know, it's

[36:02] basically a bike that you can't fall off of. And that's basically the equivalent of a Manus or the equivalent of a Pork, right? You can't fall off like, well, there are some things that you couldn't do that could be bad, but it's rare and far between and few between. Once you've gotten

[36:20] to that point where you feel comfortable and it's almost boring to be on training wheels, then go and grab a computer, install something like OpenClaw yourself. There's also some offshoots of like OpenClaw I'm sure you've seen. Yeah.

[36:38] I probably want to do a whole episode on like what are these, you know -- I think like NanoClaw is one. What are some other ones? Well they're all based off the same OpenClaw technology. I again it's

[36:55] what you said, now we're riding motorbikes with OpenClaw. When you get bored of that and you want to move to the Tron world, then start testing other things. But you're at the mercy of the internet who is maintaining these things. I think now OpenAI own OpenClaw the security is going to get a lot tighter, things are going to be a lot smoother. You don't want to be at an

[37:17] edge case where you don't really know who you're at the mercy of because if there's a vulnerability, the things that you are storing on these machines are very valuable and you won't want them to get lost, especially if you're connecting them to every device in your home. You don't want everything on every device that you own getting out because I'm sure we can all imagine how bad that could be. Absolutely.

[37:41] For people who want to get started, we can leave it at this. What do you suggest and just fire people up about this? What can you say that fires them up to motivate them to actually do this? I think if you want to get started Larry Brain is the best place to get started. It is not just a skills marketplace. It is one subscription and

[38:04] your agent gets the entire context of all the skills. So when you first get OpenClaw, you will ask it questions and it won't know how to do stuff and you have to give it skills. If you get Larry Brain, you get the context of the entire marketplace. So you can ask your

[38:19] agent to do something. It will say, "Oh, there's a Larry Brain skill available for that. Do you want to download it?"

[38:25] You download it and then it can instantly start helping you. The Larry Skill is one of them. The SuperX alternative I mentioned is one of them.

[38:33] They're both free, so you can get Larry Brain, test it, find out how it works. And then we've got over 80 skills now available for you to download. And its main goal is to help you achieve your goals. So you say, I want to

[38:47] do this. I want to make more money. Oh, here are the skills available to help you do that. I think that will

[38:52] massively help anyone downloading OpenClaw for the first time, speed up. And I think a lot of the people who you mentioned who are stuck, they don't know where to go with it, they downloaded it, it's not working for them. I think that's going to supercharge their OpenClaw account.

[39:07] Yeah. All right, man. Well, I'll include links for where to go get started there. I'm not affiliated with

[39:13] it at all. I just, you know, wanted to bring you on because I think that you're building cool stuff. You're trying new things. You're pushing the edges. I

[39:21] think that creating an AI employee that does content creation is really, really interesting. And it seems to be working. I think a lot of people are going to fail at it and you sort of have to fail your way to it working. Just

[39:39] like anything in life, you got to stick with it. You got to stick with it and keep going. And, you know, this podcast is really designed not only to get people's creative juices flowing, show them new tools, show them things like Larry Brain, but also just to show that like I love how you showed that not every content piece ripped it, you know?

[40:00] Yeah. I don't want to fake anything. This was the authentic story. I'm training it again on a new

[40:08] app. I've seen failures on X. Someone wrote a post how they've used Larry Brain. Ernesto Lopez has used

[40:15] Larry Brain to scale to over 70,000 MRR. He's implemented it in his apps using his already created content creation. He's implemented the Larry Loop to improve the content he was already creating and was already winning. And

[40:30] he's had massive success. So -- that's crazy. What's his name?

[40:34] Ernesto Lopez. He wrote -- Oh, Ernesto. I know Ernesto. I just had

[40:38] coffee with him. Yeah. Yeah, he lives

[40:41] he lives in Miami as well. He wrote an article on X about it. Yeah, that's awesome. Yeah. So Ernesto,

[40:48] you know, creates a suite of mobile apps using AI. So he's very AI native. He's a young guy. He's like in

[40:56] his early 20s. Absolutely killing it. Just absolutely killing it. Like I think

[41:01] he's doing yes, like you said, $70,000 a month. This is a guy who was like, you know, working a sales job, you know, a few years ago, didn't go to a fancy college, didn't come from Silicon Valley. So, the

[41:18] fact that there's these really interesting stories, like Ernesto, like what you're doing, I just think is really cool. And it's cool that you have a full-time job. Like this is something that you're doing, right?

[41:30] You have a full-time job, right? Yeah, I've got a full-time job. And to be honest, it takes me no time at all now. So, this is the superpower of the

[41:39] AI agents. And I can't stress enough. I know so many people who are working full-time now. And then they can vibe

[41:45] code an app, vibe code their marketing, vibe code everything to just automate that little bit of money that might be able to turn into something like what Ernesto's created. And then it's all about learning. So at the moment I'm creating hundreds of dollars. If I just

[42:00] implement my learnings a little bit more, improve my apps a little bit more, it can turn into thousands and I'm not even trying. So it allows me to work a full-time job and then it takes me an hour or two hours in the evening of literally texting or sending a voice note to Larry and then it gets done. So it's just like having a right hand, duplicating yourself and being able to give it tasks and enjoy all the laziness and comforts that you have.

[42:28] Amen. And before we go, by the way, just because we're talking on skills, I did find an OpenClaw skill that cuts token usage by 95%. It's called QMDSK skill.

[42:43] Does it work? I am going to try it tonight, but I'll include it in the show notes in the description just in case people are interested. You know, it allegedly works. So we'll see.

[42:58] And it's just fun to try these things and get the most out of these machines. Oliver, thank you so much for coming on. You're a breath of fresh air. I love

[43:11] your honesty. I love that you're tinkering and hopefully I'll see you soon. Thank you very much.
