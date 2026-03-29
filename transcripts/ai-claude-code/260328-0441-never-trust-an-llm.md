# Never Trust An LLM

**Channel**: Matt Pocock
**Duration**: 14:00
**Language**: English (auto-generated)
**URL**: https://youtube.com/watch?v=9VNG0h4pLh0
**Transcribed**: 2026-03-28 04:41

---

## Organized Notes

**Why LLMs Lie — The Core Problem**

- **LLMs hallucinate constantly** — so frequently that a dedicated term exists for it; the author is "paranoid about everything an LLM says"
- Even **very smart people** don't have the intuition that LLMs hallucinate all the time — the beautiful presentation hides the unreliability
- The author is **pro-LLM** despite this: "LLMs have massively improved my quality of life in terms of my job" — the goal is calibrated use, not rejection

**Taxonomy of Hallucinations**

- **Factual errors** — incorrect claims based on training data; classic example: Google's Bard launch ad claimed JWST took the *first* pictures of an exoplanet — wrong, caused Alphabet's share price to drop ~8%
- **Intrinsic vs. Extrinsic hallucinations** — two categories with very different risk profiles:
  - **Intrinsic** — errors about information you *explicitly provided* in the current conversation (e.g., forgetting your cat's name two messages after you stated it)
  - **Extrinsic** — errors about information the LLM was never given, drawn entirely from training data (the more dangerous and common type)
- **Fabricated entities** — inventing things that don't exist: packages, government departments, laws; developers are especially exposed because LLMs confidently recommend **non-existent npm/pip packages**, opening **supply chain malware attack** vectors
- **Contextual inconsistency** — ignoring or contradicting context *explicitly passed to the model*; the Air Canada chatbot case: even with the bereavement policy in its context window, the chatbot fabricated a different policy, resulting in a court ruling against Air Canada

**Why Hallucinations Are Structurally Unavoidable**

- Training = **lossy compression**: massive datasets → compressed model weights that fit on a GPU; the analogy is JPEG compression — you lose detail, and what remains is a blurry approximation of the original
- When information was in the training data but is underrepresented or poorly preserved, the model is working from a "blobby, hyper-compressed version" — it can answer questions visible in that blur, not fine-grained specifics
- **Guessing is rewarded, refusal is punished**: LLMs prove their quality through benchmarks (LiveBench, etc.) — "if your model is really well tuned to say 'I don't know' on math, it's probably not going to score well on the maths benchmark"
- The intelligence-humility tradeoff: smart people are **confident enough to attempt answers** and also **confident enough to be wrong**; humble people refuse more often but perform worse on deep reasoning tasks — LLM designers must pick a point on this spectrum
- Per OpenAI's own paper: *"like students facing hard exam questions, large language models sometimes guess when uncertain, producing plausible yet incorrect statements instead of admitting uncertainty"*
- The author's conclusion: **"it might be solvable, but it's going to be someone way above my pay grade"**

**How to Work Around Hallucinations**

- **Rule 1 — Always provide the information**: intrinsic information (stuff you send the LLM) is *much more reliable* than extrinsic knowledge from training data; when coding, pass the actual codebase or files rather than asking from memory
- **Rule 2 — Use your search tool** (four words): most chat interfaces and agent harnesses have web search; telling the LLM "use your search tool" forces it to pull real documents into its context, converting an extrinsic question into an intrinsic one
- The search tool trick works because it **forces humility** — the LLM must acknowledge it doesn't know and go fetch; without this prompt, a confident model may skip the search and answer from stale training data
- **Rule 3 — Verify critical output yourself**: for health, legal, life-or-death topics, use search tool *and* read the source documents directly; even with explicit context, contextual inconsistencies happen (the Air Canada case is proof)
- LLMs are still **very good at coding** — when you pass the codebase, they can give "really really good insights as to what it's doing"

*Quotable Quotes:*

> "LLMs lie. They lie all the time. They lie in different ways. They lie so often it's been given a term — hallucination." [00:00]

> "When you ask an LLM a question and it's not in their training set, I want you to imagine that this is the picture they're seeing — just a blobby, crappy, hyper-compressed version of the information that was once there." [06:45]

> "LLMs hallucinate because guessing is more highly rewarded than refusal — which, to be honest, is kind of true in most walks of life anyway." [10:02]

> "For really critical stuff, for stuff that's life or death, for health related stuff, especially for legal stuff — you basically need to ask it to use its search tool, but you then need to go and actually read the documents yourselves." [12:38]

> "When you're using AI, you need to always make sure that you're providing it the information it needs to succeed." [10:45]

---

## What This Means for Your Work

This video is a **safety calibration layer** for your AI-augmented governance work. You build platforms and draft legislation where hallucinated facts carry institutional, legal, and political consequences — not just bugs. Matt Pocock's taxonomy and mitigation framework maps directly onto risks you already face daily.

**Where this hits hardest in your work:**

- **Legislative AI workflows** — When you use `/bill-drafter`, `/legal-researcher`, or `/legislative-briefer` for e-Bangsamoro or your OOBC policy work, the LLM is drawing on *extrinsic knowledge* of BOL provisions, BAA numbers, and ministry structures. This is precisely where fabricated entities and factual errors show up: invented BAA numbers, wrong article citations, non-existent ministry abbreviations. Your `/bangsamoro` context-loading step + `/fact-checker` is the correct mitigation — it converts extrinsic knowledge into intrinsic by injecting verified source documents before the model writes.

- **OBCMS and e-Bangsamoro development** — Every time you ask Claude Code to recommend a package, suggest an architecture pattern, or recall a framework API, you're in extrinsic territory. Pocock's "use your search tool" advice translates directly: passing your actual codebase files (which you already do via context engineering) is the intrinsic equivalent. The risk isn't just wrong code — it's the supply chain malware vector from hallucinated package names.

- **Parliamentarian app** — This platform is a constitutional research tool for MP Uy-Oyod, and it relies heavily on AI interpreting legal documents. The Air Canada case is a direct analogy: even with the BOL passed as context, the model could produce a contextual inconsistency. Your verification layer (fact-checker pipeline) is the right mitigation; this video validates that architecture choice.

- **MoroMarket / Tarbiyyah-MS** — Lower legislative risk, but the principle still applies when generating product copy, data schemas, or integration documentation. Always pass the relevant files; never ask from memory.

**The structural insight that matters most for your setup:**

Your entire `/bangsamoro` → domain skill → `/fact-checker` pipeline is a direct implementation of Pocock's framework: load authoritative source docs into context (convert extrinsic to intrinsic), then verify output against those same docs. The fact that you built this before watching this video means your intuition was already calibrated — but the explicit taxonomy gives you language to explain the pipeline to others (e.g., when training MP staff or writing documentation for the guidebooks).

**One gap to close:** The "contextual inconsistency" category — hallucinations about information *already in the context window* — is the hardest to defend against. Your `/fact-checker` catches this for final documents, but for intermediate reasoning steps (when Claude Code is generating a bill section and citing a BOL article it just read), there's no mid-process check. Consider adding a micro-verification step to `/bill-drafter` that re-reads the source citation immediately after generating each section.

### How This Can Improve Your Claude Skills and Workflows

- **`/fact-checker` enhancement** — Add a "contextual inconsistency" check mode: after the model generates content using provided source documents, re-read the cited passages and flag cases where the output diverges from what was explicitly given. This directly addresses the Air Canada failure mode.

- **`/bangsamoro` context-loading discipline** — Reinforce the rule (already in CLAUDE.md) that this skill must be invoked first for any Bangsamoro content. Frame it internally as "converting extrinsic knowledge to intrinsic" — the model cannot reliably recall BOL article numbers, BAA provisions, or official titles from training data alone.

- **`/youtube-transcriber` and research skills** — When generating "What This Means for Your Work" sections, always verify named frameworks, cited papers, and external references before including them (the intrinsic/extrinsic principle applies to transcript analysis too).

- **Skill documentation** — Add a note to skills that use extrinsic knowledge (e.g., `/deep-research`, `/legal-researcher`) warning: "Do not rely on model recall for specific provisions, dates, or identifiers — always load source documents first." This makes the risk explicit to future skill users.

- **LLM safety briefing** — This video is an excellent resource to share with MP staff and BARMM officials who use AI tools without understanding hallucination risk. Given your guidebook production work and training facilitation role, consider building a 1-page "LLM Safety Brief" using Pocock's taxonomy as the framework.

---

## Transcript

[00:00] LLMs lie. They lie all the time. They lie in different ways. They lie so often

[00:05] it's been given a term hallucination. These hallucinations are so unbelievably common that I am now paranoid about everything an LLM says to me. And I will never ever trust an LLM. I'm a software

[00:16] developer and every single other software developer I speak to has this same intuition. Having worked with LM for the past 6 months. Maybe you also have this intuition, but maybe someone you know doesn't. Well, I'm making this

[00:28] video so that you can share this video with that person so that they never again trust an LLM implicitly. I'm finding that even the very very smart people in my life for some reason don't have this intuition that LLMs hallucinate all the time. Now, don't get me wrong, I'm really pro LLM. I really

[00:44] like LLMs. I think LLM have massively improved my quality of life in terms of my job, in terms of what they can produce. I think LLMs are great, but they have massive downsides. And because

[00:56] they're presented so beautifully, then people just don't realize that. So, we're going to work through three things. We're going to look at all the different types of hallucinations. We're

[01:04] going to look at why hallucinations even happen in the first place and why it's such a hard problem to solve. And then we're going to look at how to work around them when you're working with LM's day-to-day. I'm going to explain these to you in simple terms because the simple terms are the only ones I really know. I've been working with LMS for,

[01:19] you know, I don't know, a year and a half or something, but I I'm I'm not a machine learning expert. I don't work at OpenAI or anything. I'm just coming at this from someone who likes to talk about LLMs and who likes to use them day-to-day. I'm going to reference a

[01:31] couple of academic papers which I will put below. In fact, the first one is this comprehensive taxonomy of hallucinations in large language models. In other words, these guys went and looked at all of the different ways that language models can hallucinate and figured out the exact taxonomy of what types of hallucinations can happen.

[01:47] Perfect for us. The first one is pretty easy to think about. It's factual errors. This has been present since the

[01:53] very beginning of LLM. For instance, when Google announced Bard, they said in its experimental conversational AI service powered by Lambda, it said, "What new discoveries from the James Web Space Telescope can I tell my 9-year-old about?" And it said JWST took the very first pictures of a planet outside of our own solar system. This was in the

[02:12] freaking advert. They didn't even try to uh road test this. This is just wrong.

[02:17] It's a hallucination. After posting this, Alphabet's share price dropped like 8%. Now, it's crucial to say here in this case, they didn't pass the LLM a document explaining all about the James Webb Space Telescope and the new discoveries. It seems like they just

[02:30] asked it based on its training data. This is a super important distinction that the paper actually makes. There are two types of hallucinations. There are

[02:39] hallucinations based on intrinsic information and exttrinsic information. Intrinsic information is stuff that you've sent to the LLM during this conversation with the LLM. For instance, I'll go on anthropic here and I'll tell it my cat is called Bandit. It gives

[02:53] some reply here saying that's a great name for a cat. Wonderful. Thank you.

[02:56] And now I'll ask it what is my cat's name. Then of course it says your cat's name is Bandit. You just told me in your previous message. So if the LLM for some

[03:04] reason got that wrong, then it would be an intrinsic hallucination. Whereas if I start a new conversation with the LLM and I say, "What is my cat's name?" Then very good. In this case, it has not

[03:13] attempted to guess my cat's name. It's just saying I don't have any information about your cat in my context. And so if it attempted to guess here, then it would be an extrinsic hallucination. The

[03:22] next type of hallucination is fabricated entities, inventing stuff that just doesn't exist. This is actually really important for developers because developers rely on these things called packages that package up useful tools to help them do their work. So if you ask an LLM, does a package exist for this purpose? Then it's very likely to just

[03:40] say, yep, it does. This has personally happened to me dozens of times, and it's now opening up developers to supply chain malware attacks. Attackers can exploit a common AI experience, false recommendations to spread malicious code via developers that use chat to create software. This is an old article, but

[03:56] this literally just happened to me the other day. And it's not just packages. LLMs will make up government departments. They will make up laws that

[04:02] don't exist. They will make up all sorts of things. The next one is contextual inconsistency. In other words, ignoring

[04:08] or contradicting context that you explicitly provided. This would be an intrinsic hallucination like what we saw before. This article is from 2024. or

[04:15] Air Canada found liable for chatbot's bad advice on plane tickets. This guy called Jake Moffett asks the Air Canada chatbot about their bereavement policy. And even though the bereavement policy was probably in the LLM's context, it had been explicitly told about it, explicitly passed into its context, it just made something up. It said, "If you

[04:32] need to travel immediately or you've already traveled and would like to submit your ticket for a reduced bereavement rate, kindly do so within 90 days of the ticket your was issued." But when they tried to get their money back, they basically responded and admitted the chatbot had had provided misleading words. In other words, a contextual inconsistency. An inconsistency with

[04:52] something that the LLM just had in its own context window. This would be kind of like the LLM not knowing my cat's name just after I gave it to it. It's baffling that these things occur, but they do. Now, I could go through all 10

[05:02] of these terms from this paper and try to explain to you about each and every one of them, but I think you're starting to get the picture. LLMs are unreliable and especially if you're relying on their extrinsic knowledge. My experience with LLM is that they're much much more reliable when you send them the information first. Of course, why

[05:20] wouldn't they be? But if you're relying on their extrinsic knowledge from their training set, then you're going to be disappointed. We should talk in a kind of basic sense about why this is. First

[05:28] of all, the process of training an LLM of taking a bunch of training data and turning it into something smaller is essentially a compression. You take, let's say, a massive file with all of the stuff that you've gathered over the course of all of your data scraping, huge amounts of data sets about all the different, you know, text or everything on the internet, let's say. You then through some very clever mechanisms that I won't go into, you compress it down into a much smaller size that can fit on a GPU. And this compressed version of

[06:00] that training set is what we can think of as the LLM's brain or its memory or its data store. And the output here is much much much smaller than the input. Now, when you're taking some massive training set and you're squishing it down into a smaller size, you're going to lose stuff. For instance, let's take

[06:16] this photo of this beautiful man. And let's compress it a little bit. Okay, it's not bad. You can still see it's me,

[06:21] but I've lost a bit of definition here. You can't quite tell how many wrinkles there are on my forehead, for instance. We compress it a bit more, and the skin has been kind of smoothed out. I've lost

[06:31] a lot of definition. and you go all the way and I just end up like this blobby looking person that you can barely recognize it's me. When you ask an LLM a question and it's not in their training set, I want you to imagine that this is the picture that they're seeing of the information they have. Just a blobby,

[06:45] crappy, hypercompressed version of the information that was once there. And look, you can still get good answers out of this image. It can still say, okay, what color is the little cap on the end of my microphone here? It is blue,

[06:56] right? That is visible from the image. You could probably just about say that this man doesn't have any hair on his head, too. But if you ask about who it

[07:03] is or how old this person is or, you know, any of that, it's not going to have a clue. So, the question then becomes, if LLMs only have this crappy low res version of all of the information in the world, why are they so insistent on guessing? Because an LLM presented with this information and you asked who they are, they will often just have a go and guess. Now, the answer for

[07:24] this comes from the second paper that I want to link to, which is below. It's from OpenAI and the title is Why Language Models Hallucinate. Like students facing hard exam questions, large language models sometimes guess when uncertain, producing plausible yet incorrect statements instead of admitting uncertainty. We argue that the

[07:40] language models hallucinate because the training and evaluation procedures reward guessing over acknowledging uncertainty. Now, what do they mean by evaluation procedures? What are they talking about? Well, LLM prove that

[07:51] they're getting better over time by showing their numbers in benchmarks. For instance, here this one is LiveBench. I mean, I think this is a leaderboard of multiple benchmarks. And you can see

[08:00] that all of the top models here are rated a number out of 100 on how good they are at different things. For instance, reasoning, coding, agentic coding, mathematics, data analysis, language, etc. Being at the top of these leaderboards is incredibly valuable for these companies. If you can say you have

[08:17] the best model in the world at something, then everyone who's doing that thing is going to want to use your model because it's actually really easy to swap models. You just like stop using one thing and go and use another thing. And there's a tension that these benchmarks introduce because if your model is really well tuned to say I don't know something when it comes to let's say maths, then it's probably not going to score very well on the maths benchmark because it might just be better on average for it to have a guess. In other words, you miss all of

[08:46] the shots that you don't take. And so LLMs try to take as many shots as possible. In fact, there's kind of a tension inherent in designing LLMs. And

[08:55] you can think of this kind of by thinking of it in human terms. It's quite rare to meet a person who's really, really smart, but also really humble about their smartness. People who are really smart, especially in an exam context, will probably be smart enough to get close to the right answer and will trust themselves and be confident enough to actually work it out. But

[09:14] people who are humble enough to say, "I don't know," will probably go in the opposite direction where they might not be confident enough to actually get it done. However, if you're really smart, you're often going to be way too confident about your own answers. And this will lead to hallucinations. In

[09:30] other words, all the stuff that we've been talking about so far. But if you're on the other side and you're not confident enough, then you're probably not going to do really well in the domains where you need really, really deep thinking. And the people who grade LLM and who train LLM need to figure out somewhere on this line. And I'm not sure

[09:47] it's a solvable problem. Or rather, it might be solvable, but it's going to be someone way above my pay grade. So to sum it up, LLM's hallucinate because guessing is more highly rewarded than refusal, which to be honest is kind of true in most walks of life anyway. So

[10:02] then we now know how LLM hallucinate and we kind of understand why LLM hallucinate. But why after all of that am I still so pro- AAI? Why do I still like AI? Well, it's because when you

[10:13] actually pass them intrinsic information here, if you actually send them stuff, if you get them to uh peruse a big document or something, then it tends to be really really accurate, way more accurate than extrinsic information. So when I'm coding for instance, I can pass my codebase or you know big files to the LLM and get it to answer questions about it, get it to explore the code and it will give me really really good insights as to what it's doing. In other words, when you're using AI, you need to always make sure that you're providing it the information it needs to succeed. But so

[10:45] you might ask, uh, that doesn't make any sense because I often use LLM for searching for information. If I have a question that I don't have the answer to, I can't use this intrinsic stuff. All I have to rely on is exttrinsic stuff. So, I'm going to tell you about a

[10:58] four-word prompt that will allow you to get the LLM to fetch intrinsic information that it doesn't yet have. Use your search tool. Most chat bots and most, let's call them agent harnesses have some kind of tool that the LLM can use in order to search the web. For

[11:15] instance, in Claude here, if we go to files, connectors, and blah blah blah blah blah, then we have this little web search thing just inside there. And I always have this turned on. And for instance, I can ask it which Arsenal players are injured right now. And it

[11:29] will go and search the web and try to find the information. So here we go. It's saying here's the current Arsenal injury picture, blah blah blah blah blah. And as you can see, there are

[11:37] citations based on where it's got the information from. Now, it's done a good job this time because, you know, Sonnet is a good model and I like this tool in general. But many tools will not by default go and do this. Especially if

[11:51] the model is confident that it knows it and its training set if it doesn't need to use its search tool. In other words, in order to use its search tool, it needs to be humble enough to be able to say, "I don't know. I need to go and fetch this." And so, if it's like tuned

[12:04] to be really smart, it might just go, "Oh, I know the answer. Let me just repeat it to you." And so, whenever you're prompting the LLM to ask it for information, say, "Use your search tool." because then it will pull the

[12:15] articles into its context and it will answer based on those articles and you'll be less likely to get hallucinations because you're relying on intrinsic information, information in the context window. However, remember there's a category of hallucinations called contextual inconsistency. In other words, even stuff that you provide explicitly to the LLM might just be ignored. Even if you're an airline and

[12:38] you have a chatbot with a bereavement policy explicitly passed to it, it might still get it wrong. And so for really critical stuff, for stuff that's life or death, for health related stuff, especially for legal stuff, you basically need to ask it, use your search tool, but you then need to go and actually read the documents yourselves. This happens all the time for me when I'm coding, too. The LLM will read some

[13:00] code and it might just misinterpret it or not know the full context and so it spews something out very confidently and I then have to say, "No, that's actually not quite right." So hopefully this video has given you a bit more understanding about what the limits of LLMs are and how you can work around them. And if you have someone in your life who you want to be better with LLMs or you notice them just slightly using them wrong, then maybe send them this video and hopefully we can build a world where people don't trust LLMs and instead use them for what they're good at. For instance, they are very very

[13:31] good at writing code and I'm running a Claude code for real engineers course over the next two weeks. If you dig that or you dig the idea that real engineering principles can still be used in the AI age, in fact, they're better than ever, then sign up to my newsletter below or sign up to learn about when the next cohort is happening. Thanks for watching, folks. This was a bit of a

[13:50] change of pace for me. I don't usually make these kind of wider videos or videos for a wider audience, but I kind of just wanted to get this out there. Thanks for watching and I will see you in the next
